from __future__ import annotations

import contextlib
import csv
from datetime import date
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


PROJECT_ROOT = Path(__file__).parents[2]
MODULE_PATH = PROJECT_ROOT / "00_governance/scripts/discovery_search.py"
SPEC = importlib.util.spec_from_file_location("discovery_search", MODULE_PATH)
search = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = search
SPEC.loader.exec_module(search)

VALIDATOR_PATH = PROJECT_ROOT / "00_governance/scripts/validate_library.py"
VALIDATOR_SPEC = importlib.util.spec_from_file_location(
    "task_2_validate_library", VALIDATOR_PATH
)
validator = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC.loader is not None
sys.modules[VALIDATOR_SPEC.name] = validator
VALIDATOR_SPEC.loader.exec_module(validator)


class DiscoverySearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "library"
        self.source_root = Path(self.temporary.name) / "source"
        self.root.mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def sha(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def write_csv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def copy_configuration(self) -> None:
        for relative in (
            search.PROTOCOL_PATH,
            search.QUERY_CONFIG_PATH,
            search.JOURNAL_REGISTRY_PATH,
        ):
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(PROJECT_ROOT / relative, destination)

    def write_journals(self, rows: list[dict[str, str]]) -> None:
        self.write_csv(
            self.root / search.JOURNAL_REGISTRY_PATH,
            list(search.JOURNAL_HEADERS),
            rows,
        )

    def add_artifact(self, run_dir: Path, relative: str, data: bytes) -> dict[str, str]:
        path = run_dir / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return {"path": relative, "sha256": self.sha(path)}

    def write_run(self, run_dir: Path, cells: list[dict[str, object]], files: list[dict[str, str]]) -> Path:
        receipt = {
            "schema_version": 1,
            "executed_at": "2026-07-20T12:00:00+08:00",
            "timezone": "Asia/Shanghai",
            "tool_version": "test",
            "source": "pubmed",
            "configuration_files": [
                {"path": str(search.PROTOCOL_PATH), "sha256": self.sha(self.root / search.PROTOCOL_PATH)},
                {"path": str(search.QUERY_CONFIG_PATH), "sha256": self.sha(self.root / search.QUERY_CONFIG_PATH)},
                {"path": str(search.JOURNAL_REGISTRY_PATH), "sha256": self.sha(self.root / search.JOURNAL_REGISTRY_PATH)},
            ],
            "cells": cells,
        }
        (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt), encoding="utf-8")
        (run_dir / "MANIFEST_SHA256.json").write_text(
            json.dumps({"algorithm": "SHA256", "files": files}), encoding="utf-8"
        )
        return run_dir

    def make_leaf(
        self,
        run_dir: Path,
        search_id: str = "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
        date_start: str = "2020/01/01",
        date_end: str = "2020/12/31",
        reported_count: int = 1,
    ) -> tuple[dict[str, object], list[dict[str, str]]]:
        stem = search_id
        esearch = self.add_artifact(run_dir, f"raw/{stem}.esearch.json", b"{}")
        page_receipts: list[dict[str, object]] = []
        files = [esearch]
        for retstart in range(0, reported_count, 200):
            parsed_count = min(200, reported_count - retstart)
            page = self.add_artifact(
                run_dir,
                f"raw/{stem}.efetch.{retstart:09d}-{retstart + 199:09d}.xml",
                (
                    b"<PubmedArticleSet>"
                    + b"<PubmedArticle />" * parsed_count
                    + b"</PubmedArticleSet>"
                ),
            )
            files.append(page)
            page_receipts.append(
                {
                    "retstart": retstart,
                    "retmax": parsed_count,
                    "path": page["path"],
                    "sha256": page["sha256"],
                    "parsed_count": parsed_count,
                }
            )
        cell: dict[str, object] = {
            "search_id": search_id,
            "lane": "FAMILY",
            "family": "causal_policy",
            "query": "test query",
            "date_start": date_start,
            "date_end": date_end,
            "reported_count": reported_count,
            "parent_search_id": "",
            "cell_type": "leaf",
            "esearch_path": esearch["path"],
            "esearch_sha256": esearch["sha256"],
            "status": "complete",
            "usehistory": True,
            "webenv": "test-webenv",
            "query_key": "1",
            "retrieved_count": reported_count,
            "efetch_pages": page_receipts,
        }
        return cell, files

    def make_valid_run(self, parent: Path | None = None) -> Path:
        self.copy_configuration()
        run_dir = (parent or self.root) / "run"
        run_dir.mkdir(parents=True)
        cell, files = self.make_leaf(run_dir)
        compiled = self.add_artifact(
            run_dir,
            "compiled_candidates_raw.csv",
            (
                "candidate_key,row_sha256,pmid,doi,title,year,journal,authors,abstract,"
                "publication_types,search_ids,lanes,preliminary_families,source_url,"
                "deduplication_basis,possible_duplicate_group\n"
            ).encode(),
        )
        return self.write_run(run_dir, [cell], [*files, compiled])

    def make_valid_split_run(self) -> Path:
        self.copy_configuration()
        run_dir = self.root / "split-run"
        run_dir.mkdir(parents=True)
        parent_esearch = self.add_artifact(run_dir, "raw/parent.esearch.json", b"{}")
        first, first_files = self.make_leaf(
            run_dir,
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-02",
            "2020/01/01",
            "2020/06/30",
            5000,
        )
        second, second_files = self.make_leaf(
            run_dir,
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-03",
            "2020/07/01",
            "2020/12/31",
            5000,
        )
        first["parent_search_id"] = "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01"
        second["parent_search_id"] = "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01"
        parent_cell: dict[str, object] = {
            "search_id": "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "lane": "FAMILY",
            "family": "causal_policy",
            "query": "test query",
            "date_start": "2020/01/01",
            "date_end": "2020/12/31",
            "reported_count": 10000,
            "parent_search_id": "",
            "cell_type": "split_parent",
            "esearch_path": parent_esearch["path"],
            "esearch_sha256": parent_esearch["sha256"],
            "status": "complete",
            "retrieved_count": 0,
            "children": [first, second],
        }
        compiled = self.add_artifact(run_dir, "compiled_candidates_raw.csv", b"header\n")
        return self.write_run(
            run_dir,
            [parent_cell],
            [parent_esearch, *first_files, *second_files, compiled],
        )

    def make_valid_screened_run(self, parent: Path | None = None) -> Path:
        run_dir = self.make_valid_run(parent)
        candidate_key = "PMID:1"
        row_sha = "d" * 64
        raw_headers = [
            "candidate_key", "row_sha256", "pmid", "doi", "title", "year",
            "journal", "authors", "abstract", "publication_types", "search_ids",
            "lanes", "preliminary_families", "source_url", "deduplication_basis",
            "possible_duplicate_group",
        ]
        self.write_csv(
            run_dir / "compiled_candidates_raw.csv",
            raw_headers,
            [{key: (candidate_key if key == "candidate_key" else row_sha if key == "row_sha256" else "") for key in raw_headers}],
        )
        manifest_path = run_dir / "MANIFEST_SHA256.json"
        manifest = json.loads(manifest_path.read_text())
        next(item for item in manifest["files"] if item["path"] == "compiled_candidates_raw.csv")["sha256"] = self.sha(run_dir / "compiled_candidates_raw.csv")
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        primary_headers = [
            "candidate_key", "source_row_sha256", "primary_decision",
            "primary_proposed_record_type", "primary_reason_code", "primary_reason",
            "primary_reviewer", "batch_id", "retained_candidate_key",
        ]
        primary = {
            "candidate_key": candidate_key,
            "source_row_sha256": row_sha,
            "primary_decision": "include_applied_seed",
            "primary_proposed_record_type": "applied_seed",
            "primary_reason_code": "I_APPLIED_TRANSFERABLE_DESIGN",
            "primary_reason": "The abstract describes a transferable infectious-disease design.",
            "primary_reviewer": "reviewer-a",
            "batch_id": "BATCH-001",
            "retained_candidate_key": "",
        }
        self.write_csv(run_dir / "screening_batches/BATCH-001.csv", primary_headers, [primary])

        screened_headers = [
            "candidate_key", "source_row_sha256", "primary_decision",
            "primary_proposed_record_type", "primary_reason_code", "primary_reason",
            "final_decision", "final_proposed_record_type", "final_reason_code",
            "final_reason", "primary_reviewer", "batch_id", "audit_status",
            "retained_candidate_key",
        ]
        screened = dict(primary)
        screened.update(
            final_decision=primary["primary_decision"],
            final_proposed_record_type=primary["primary_proposed_record_type"],
            final_reason_code=primary["primary_reason_code"],
            final_reason=primary["primary_reason"],
            audit_status="agree",
        )
        self.write_csv(run_dir / "screened_candidates.csv", screened_headers, [screened])

        audit_headers = [
            "candidate_key", "source_row_sha256", "primary_reviewer", "audit_stratum",
            "audit_rank", "audit_reviewer", "primary_decision", "primary_reason_code",
            "primary_proposed_record_type", "audit_decision", "audit_reason_code",
            "audit_proposed_record_type", "audit_reason", "conflict_status", "adjudicator",
            "final_decision", "final_reason_code", "final_proposed_record_type", "final_reason",
        ]
        audit = {
            "candidate_key": candidate_key,
            "source_row_sha256": row_sha,
            "primary_reviewer": "reviewer-a",
            "audit_stratum": "include_applied_seed|I_APPLIED_TRANSFERABLE_DESIGN|",
            "audit_rank": hashlib.sha256(f"{candidate_key}|audit-v1".encode()).hexdigest(),
            "audit_reviewer": "reviewer-b",
            "primary_decision": "include_applied_seed",
            "primary_reason_code": "I_APPLIED_TRANSFERABLE_DESIGN",
            "primary_proposed_record_type": "applied_seed",
            "audit_decision": "include_applied_seed",
            "audit_reason_code": "I_APPLIED_TRANSFERABLE_DESIGN",
            "audit_proposed_record_type": "applied_seed",
            "audit_reason": primary["primary_reason"],
            "conflict_status": "none",
            "adjudicator": "",
            "final_decision": "include_applied_seed",
            "final_reason_code": "I_APPLIED_TRANSFERABLE_DESIGN",
            "final_proposed_record_type": "applied_seed",
            "final_reason": primary["primary_reason"],
        }
        self.write_csv(run_dir / "screening_audit.csv", audit_headers, [audit])
        return run_dir

    def delete_one_required_audit_row(self, run_dir: Path) -> None:
        path = run_dir / "screening_audit.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            headers = next(csv.reader(handle))
        self.write_csv(path, headers, [])

    def make_valid_lineage_run(self, parent: Path) -> Path:
        self.copy_configuration()
        lineage_registry = self.root / "LINEAGE_QUERY_REGISTRY.csv"
        if not lineage_registry.exists():
            lineage_registry.write_text("query_id\n", encoding="utf-8")
        run_dir = parent / "wave_03_lineage_resolution"
        run_dir.mkdir(parents=True)
        pubmed = self.add_artifact(run_dir, "pubmed_lineage_candidates.csv", b"candidate_key\n")
        crossref = self.add_artifact(run_dir, "crossref_candidates.csv", b"candidate_key\n")
        (run_dir / "MANIFEST_SHA256.json").write_text(
            json.dumps({"algorithm": "SHA256", "files": [pubmed, crossref]}), encoding="utf-8"
        )
        receipt = {
            "schema_version": 1,
            "executed_at": "2026-07-20T12:00:00+08:00",
            "timezone": "Asia/Shanghai",
            "tool_version": "test",
            "configuration_files": [
                {"path": str(search.PROTOCOL_PATH), "sha256": self.sha(self.root / search.PROTOCOL_PATH)},
                {"path": str(search.QUERY_CONFIG_PATH), "sha256": self.sha(self.root / search.QUERY_CONFIG_PATH)},
                {"path": str(search.JOURNAL_REGISTRY_PATH), "sha256": self.sha(self.root / search.JOURNAL_REGISTRY_PATH)},
                {"path": "LINEAGE_QUERY_REGISTRY.csv", "sha256": self.sha(self.root / "LINEAGE_QUERY_REGISTRY.csv")},
            ],
            "queries": [],
        }
        (run_dir / "LINEAGE_RUN_RECEIPT.json").write_text(json.dumps(receipt), encoding="utf-8")
        return run_dir

    def make_valid_phase_run(self) -> Path:
        self.copy_configuration()
        (self.root / "LINEAGE_QUERY_REGISTRY.csv").write_text("query_id\n", encoding="utf-8")
        phase = self.root / "phase"
        phase.mkdir()
        for wave in ("wave_01_frozen_queries", "wave_02_synonym_expansion"):
            staged = self.make_valid_screened_run(phase)
            wave_dir = phase / wave
            staged.rename(wave_dir)
            if wave == "wave_01_frozen_queries":
                receipt_path = wave_dir / "RUN_RECEIPT.json"
                manifest_path = wave_dir / "MANIFEST_SHA256.json"
                receipt = json.loads(receipt_path.read_text())
                manifest = json.loads(manifest_path.read_text())
                configured = search.build_search_cells(self.root, date(2026, 7, 20))
                first = receipt["cells"][0]
                first.update(
                    search_id=configured[0].search_id,
                    lane=configured[0].lane,
                    family=configured[0].family,
                    query=configured[0].query,
                    date_start=configured[0].date_start,
                    date_end=configured[0].date_end,
                )
                cells = [first]
                for configured_cell in configured[1:]:
                    esearch = self.add_artifact(
                        wave_dir,
                        f"raw/{configured_cell.search_id}.esearch.json",
                        b"{}",
                    )
                    manifest["files"].append(esearch)
                    cells.append(
                        {
                            **configured_cell.__dict__,
                            "reported_count": 0,
                            "cell_type": "leaf",
                            "esearch_path": esearch["path"],
                            "esearch_sha256": esearch["sha256"],
                            "status": "complete",
                            "usehistory": True,
                            "webenv": "empty-history",
                            "query_key": "1",
                            "retrieved_count": 0,
                            "efetch_pages": [],
                        }
                    )
                receipt["cells"] = cells
                receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
                manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            if wave == "wave_02_synonym_expansion":
                receipt_path = wave_dir / "RUN_RECEIPT.json"
                receipt = json.loads(receipt_path.read_text())
                query_registry = wave_dir / "QUERY_REGISTRY.csv"
                query_registry.write_text("family\n", encoding="utf-8")
                relative_registry = query_registry.relative_to(self.root).as_posix()
                receipt["configuration_files"].append(
                    {"path": relative_registry, "sha256": self.sha(query_registry)}
                )
                receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.make_valid_lineage_run(phase)
        return phase

    def make_external_boundary_fixture(self) -> None:
        self.source_root.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=self.source_root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.source_root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.source_root, check=True)
        seed = self.source_root / search.EXTERNAL_SEED_SOURCE_PATH
        seed.parent.mkdir(parents=True)
        seed.write_text("seed\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.source_root, check=True)
        subprocess.run(["git", "commit", "-qm", "baseline"], cwd=self.source_root, check=True)
        seed.write_text("changed seed\n", encoding="utf-8")
        (self.source_root / search.EXTERNAL_POINTER_PATH).write_text("pointer\n", encoding="utf-8")
        status = subprocess.run(
            ["git", "status", "--short"], cwd=self.source_root, check=True,
            text=True, stdout=subprocess.PIPE,
        ).stdout.splitlines()
        pointer_line = f"?? {search.EXTERNAL_POINTER_PATH.as_posix()}"
        filtered = [line for line in status if line != pointer_line]
        filtered_text = "\n".join(filtered) + ("\n" if filtered else "")
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=self.source_root, check=True,
            text=True, stdout=subprocess.PIPE,
        ).stdout.strip()
        receipt_path = self.root / search.EXTERNAL_BOUNDARY_PATH
        receipt_path.parent.mkdir(parents=True)
        receipt_path.write_text(
            json.dumps(
                {
                    "captured_at": "2026-07-20T12:00:00+08:00",
                    "timezone": "Asia/Shanghai",
                    "source_repository": str(self.source_root),
                    "source_head": head,
                    "filtered_pointer_line": pointer_line,
                    "filtered_status_line_count": len(filtered),
                    "filtered_status_sha256": hashlib.sha256(filtered_text.encode()).hexdigest(),
                    "pointer_status": "untracked",
                    "pointer_index_paths": [],
                    "seed_source_status": "modified",
                    "proof_limit": search.EXTERNAL_PROOF_LIMIT,
                }
            ),
            encoding="utf-8",
        )

    def mutate_source_porcelain_fixture(self) -> None:
        (self.source_root / "new-untracked.txt").write_text("new\n", encoding="utf-8")

    def test_configuration_builds_twelve_unique_cells(self):
        self.copy_configuration()
        errors = search.validate_configuration(self.root)
        cells = search.build_search_cells(self.root, date(2026, 7, 20))
        self.assertEqual(errors, [])
        self.assertEqual(len(cells), 12)
        self.assertEqual(len({cell.search_id for cell in cells}), 12)
        self.assertTrue(all("2010/01/01" in cell.query and "2026/12/31" in cell.query for cell in cells))
        self.assertTrue(all("[Title/Abstract]" not in cell.query.split(" AND ")[0] for cell in cells if cell.lane == "FAMILY"))

    def test_configuration_requires_all_six_families(self):
        self.copy_configuration()
        config = json.loads((self.root / search.QUERY_CONFIG_PATH).read_text())
        config["families"] = config["families"][:-1]
        (self.root / search.QUERY_CONFIG_PATH).write_text(json.dumps(config))
        self.assertIn("family set mismatch", "\n".join(search.validate_configuration(self.root)))

    def test_journal_tokens_must_be_unique_and_nonblank(self):
        self.copy_configuration()
        path = self.root / search.JOURNAL_REGISTRY_PATH
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[1]["pubmed_token"] = rows[0]["pubmed_token"]
        self.write_journals(rows)
        self.assertIn("duplicate pubmed_token", "\n".join(search.validate_configuration(self.root)))

    def test_search_run_rejects_sha_mismatch(self):
        run_dir = self.make_valid_run()
        raw = next((run_dir / "raw").glob("*.xml"))
        raw.write_bytes(raw.read_bytes() + b"altered")
        self.assertIn("checksum mismatch", "\n".join(search.validate_search_run(run_dir)))

    def test_search_run_rejects_missing_receipt_fields(self):
        run_dir = self.make_valid_run()
        receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text())
        del receipt["executed_at"]
        (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt))
        self.assertIn("missing receipt field", "\n".join(search.validate_search_run(run_dir)))

    def test_search_run_recomputes_configuration_file_hashes(self):
        run_dir = self.make_valid_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["configuration_files"][0]["sha256"] = "f" * 64
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "configuration file checksum mismatch",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_wave_two_cannot_replace_a_frozen_configuration_file(self):
        phase_dir = self.make_valid_phase_run()
        run_dir = phase_dir / "wave_02_synonym_expansion"
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["configuration_files"][0] = {
            "path": "ANOTHER_QUERY_REGISTRY.csv",
            "sha256": "f" * 64,
        }
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "wave 2 configuration_files mismatch",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_wave_two_requires_its_exact_run_local_query_registry(self):
        phase_dir = self.make_valid_phase_run()
        run_dir = phase_dir / "wave_02_synonym_expansion"
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["configuration_files"][-1] = {
            "path": "LINEAGE_QUERY_REGISTRY.csv",
            "sha256": self.sha(self.root / "LINEAGE_QUERY_REGISTRY.csv"),
        }
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "wave 2 configuration_files mismatch",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_search_run_rejects_path_traversal_and_bad_page_count(self):
        run_dir = self.make_valid_run()
        manifest = json.loads((run_dir / "MANIFEST_SHA256.json").read_text())
        manifest["files"][0]["path"] = "../escape"
        (run_dir / "MANIFEST_SHA256.json").write_text(json.dumps(manifest))
        errors = "\n".join(search.validate_search_run(run_dir))
        self.assertIn("path traversal", errors)
        receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text())
        receipt["cells"][0]["efetch_pages"][0]["parsed_count"] = 0
        (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt))
        self.assertIn("parsed count mismatch", "\n".join(search.validate_search_run(run_dir)))

    def test_page_ranges_use_retmax_for_contiguous_terminal_coverage(self):
        self.copy_configuration()
        run_dir = self.root / "paged-run"
        run_dir.mkdir()
        cell, files = self.make_leaf(run_dir, reported_count=201)
        compiled = self.add_artifact(run_dir, "compiled_candidates_raw.csv", b"header\n")
        self.write_run(run_dir, [cell], [*files, compiled])
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["cells"][0]["efetch_pages"][0]["retmax"] = 199
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        rendered = "\n".join(search.validate_search_run(run_dir))
        self.assertIn("page interval gap", rendered)
        self.assertIn("parsed count exceeds retmax", rendered)

    def test_raw_page_path_cannot_be_counted_twice(self):
        run_dir = self.make_valid_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        cell = receipt["cells"][0]
        first_page = dict(cell["efetch_pages"][0])
        first_page.update(retmax=1, parsed_count=1)
        second_page = dict(first_page)
        second_page["retstart"] = 1
        cell.update(reported_count=2, retrieved_count=2, efetch_pages=[first_page, second_page])
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "duplicate raw page path",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_split_parent_requires_contiguous_nonoverlapping_children(self):
        run_dir = self.make_valid_split_run()
        self.assertEqual(search.validate_search_run(run_dir), [])
        receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text())
        receipt["cells"][0]["children"][1]["date_start"] = "2020/07/02"
        (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt))
        self.assertIn("split interval gap", "\n".join(search.validate_search_run(run_dir)))

    def test_split_parent_requires_a_splittable_source_count(self):
        run_dir = self.make_valid_split_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["cells"][0]["reported_count"] = 9999
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "split parent count below 10000",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_split_parent_reconciles_child_counts_and_status(self):
        run_dir = self.make_valid_split_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["cells"][0]["reported_count"] = 10001
        receipt["cells"][0]["status"] = "failed"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        rendered = "\n".join(search.validate_search_run(run_dir))
        self.assertIn("split parent count mismatch", rendered)
        self.assertIn("invalid cell status", rendered)

    def test_malformed_split_child_returns_error_without_exception(self):
        run_dir = self.make_valid_split_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["cells"][0]["children"][0] = None
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "invalid cell receipt",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_leaf_requires_history_and_page_fields(self):
        run_dir = self.make_valid_run()
        self.assertEqual(search.validate_search_run(run_dir), [])
        receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text())
        del receipt["cells"][0]["query_key"]
        (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt))
        self.assertIn("missing leaf receipt field", "\n".join(search.validate_search_run(run_dir)))

    def test_lineage_enforces_source_conditional_fields(self):
        run_dir = self.make_valid_lineage_run(self.root)
        self.assertEqual(search.validate_lineage(self.root, run_dir), [])
        receipt = json.loads((run_dir / "LINEAGE_RUN_RECEIPT.json").read_text())
        receipt["queries"] = [{
            "query_id": "SEARCH-20260720-LINEAGE-CAUSAL-01",
            "source": "crossref", "query": "citation", "reported_count": 1,
            "raw_path": "raw/crossref.json", "raw_sha256": "e" * 64,
            "status": "complete", "response_path": "raw/crossref.json",
            "response_sha256": "e" * 64, "returned_candidate_count": 1,
            "total_results": 10, "rows": 5, "query_key": "forbidden",
        }]
        (run_dir / "LINEAGE_RUN_RECEIPT.json").write_text(json.dumps(receipt))
        self.assertIn("prohibited crossref field", "\n".join(search.validate_lineage(self.root, run_dir)))

    def test_lineage_rejects_non_string_query_id_without_exception(self):
        run_dir = self.make_valid_lineage_run(self.root)
        receipt_path = run_dir / "LINEAGE_RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["queries"] = [{
            "query_id": [], "source": "crossref", "query": "citation",
            "reported_count": 0, "raw_path": "missing.json",
            "raw_sha256": "a" * 64, "status": "complete",
            "response_path": "missing.json", "response_sha256": "a" * 64,
            "returned_candidate_count": 0, "total_results": 0, "rows": 5,
        }]
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "invalid lineage query_id",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_lineage_raw_response_has_single_query_ownership(self):
        run_dir = self.make_valid_lineage_run(self.root)
        raw = self.add_artifact(run_dir, "raw/shared-crossref.json", b"{}")
        manifest_path = run_dir / "MANIFEST_SHA256.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["files"].append(raw)
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        base_query = {
            "source": "crossref", "query": "citation", "reported_count": 1,
            "raw_path": raw["path"], "raw_sha256": raw["sha256"],
            "status": "complete", "response_path": raw["path"],
            "response_sha256": raw["sha256"], "returned_candidate_count": 1,
            "total_results": 10, "rows": 5,
        }
        receipt_path = run_dir / "LINEAGE_RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["queries"] = [
            {**base_query, "query_id": "SEARCH-20260720-LINEAGE-CAUSAL-01"},
            {**base_query, "query_id": "SEARCH-20260720-LINEAGE-CAUSAL-02"},
        ]
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "duplicate lineage raw path",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_external_boundary_rejects_filtered_status_change(self):
        self.make_external_boundary_fixture()
        self.assertEqual(search.validate_external_boundary(self.root, self.source_root), [])
        self.mutate_source_porcelain_fixture()
        self.assertIn(
            "external filtered status mismatch",
            "\n".join(search.validate_external_boundary(self.root, self.source_root)),
        )

    def test_external_boundary_requires_the_exact_pointer_exclusion(self):
        self.make_external_boundary_fixture()
        receipt_path = self.root / search.EXTERNAL_BOUNDARY_PATH
        receipt = json.loads(receipt_path.read_text())
        receipt["filtered_pointer_line"] = "?? some-other-file"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "external filtered pointer line mismatch",
            "\n".join(search.validate_external_boundary(self.root, self.source_root)),
        )

    def test_external_boundary_preserves_receipt_claim_limits(self):
        self.make_external_boundary_fixture()
        receipt_path = self.root / search.EXTERNAL_BOUNDARY_PATH
        receipt = json.loads(receipt_path.read_text())
        receipt["source_repository"] = "/different/repository"
        receipt["proof_limit"] = "All dirty files are byte-identical."
        receipt["captured_at"] = ""
        receipt["timezone"] = ""
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        rendered = "\n".join(search.validate_external_boundary(self.root, self.source_root))
        self.assertIn("external source repository mismatch", rendered)
        self.assertIn("external proof limit mismatch", rendered)
        self.assertIn("external captured_at invalid", rendered)
        self.assertIn("external timezone mismatch", rendered)

    def test_screening_and_audit_validators_recompute_complete_coverage(self):
        run_dir = self.make_valid_screened_run()
        self.assertEqual(search.validate_screening(run_dir), [])
        self.assertEqual(search.validate_screening_audit(run_dir), [])
        self.delete_one_required_audit_row(run_dir)
        self.assertIn("missing required audit key", "\n".join(search.validate_screening_audit(run_dir)))

    def test_audit_rejects_a_disagreement_marked_as_no_conflict(self):
        run_dir = self.make_valid_screened_run()
        path = run_dir / "screening_audit.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0].update(
            audit_decision="include_method_source_lead",
            audit_reason_code="I_METHOD_SOURCE",
            audit_proposed_record_type="method_source",
        )
        self.write_csv(path, list(search.AUDIT_HEADERS), rows)
        self.assertIn(
            "falsely closed audit conflict",
            "\n".join(search.validate_screening_audit(run_dir)),
        )

    def test_audit_reconciles_primary_and_screened_provenance(self):
        run_dir = self.make_valid_screened_run()
        path = run_dir / "screening_audit.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0].update(
            primary_decision="include_method_source_lead",
            primary_reason_code="I_METHOD_SOURCE",
            primary_proposed_record_type="method_source",
            audit_decision="include_method_source_lead",
            audit_reason_code="I_METHOD_SOURCE",
            audit_proposed_record_type="method_source",
            final_decision="include_method_source_lead",
            final_reason_code="I_METHOD_SOURCE",
            final_proposed_record_type="method_source",
        )
        self.write_csv(path, list(search.AUDIT_HEADERS), rows)
        rendered = "\n".join(search.validate_screening_audit(run_dir))
        self.assertIn("audit primary decision mismatch", rendered)
        self.assertIn("screened audit result mismatch", rendered)

    def test_unaudited_final_decision_is_locked_to_primary(self):
        run_dir = self.make_valid_screened_run()
        path = run_dir / "screened_candidates.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0].update(
            final_decision="include_method_source_lead",
            final_reason_code="I_METHOD_SOURCE",
            final_proposed_record_type="method_source",
            final_reason="The record is reclassified without an audit.",
            audit_status="not_selected",
        )
        self.write_csv(path, list(search.SCREENED_HEADERS), rows)
        self.assertIn(
            "unaudited final result mismatch",
            "\n".join(search.validate_screening(run_dir)),
        )

    def test_wave_one_requires_all_twelve_configured_roots(self):
        phase_dir = self.make_valid_phase_run()
        run_dir = phase_dir / "wave_01_frozen_queries"
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["cells"] = []
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "wave 1 root cell mismatch",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_verify_all_composes_every_phase_validator(self):
        phase_dir = self.make_valid_phase_run()
        self.assertEqual(search.validate_all(self.root, phase_dir), [])
        (phase_dir / "wave_02_synonym_expansion" / "RUN_RECEIPT.json").unlink()
        self.assertIn("wave_02", "\n".join(search.validate_all(self.root, phase_dir)))

    def test_validation_cli_contract(self):
        self.copy_configuration()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = search.main(["validate-config", "--root", str(self.root)])
        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue().strip(), "DISCOVERY PASS")

    def test_deferred_execution_cli_preserves_the_declared_arguments(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = search.main(
                [
                    "run",
                    "--root", str(self.root),
                    "--date", "2026-07-20",
                    "--email", "test@example.invalid",
                    "--api-key", "runtime-only",
                    "--output", str(self.root / "wave"),
                ]
            )
        self.assertEqual(result, 1)
        self.assertIn("DISCOVERY FAIL", output.getvalue())

    def test_repository_validator_requires_and_validates_discovery_configuration(self):
        required = {
            str(search.PROTOCOL_PATH),
            str(search.QUERY_CONFIG_PATH),
            str(search.JOURNAL_REGISTRY_PATH),
            "01_search/PAPER_DISCOVERY_RECORD_TEMPLATE.md",
            "01_search/METHOD_DISCOVERY_RECORD_TEMPLATE.md",
            str(search.EXTERNAL_BOUNDARY_PATH),
            "00_governance/scripts/discovery_search.py",
        }
        self.assertTrue(required.issubset(set(validator.REQUIRED_PATHS)))
        self.copy_configuration()
        config_path = self.root / search.QUERY_CONFIG_PATH
        config = json.loads(config_path.read_text())
        config["families"] = []
        config_path.write_text(json.dumps(config), encoding="utf-8")
        errors = validator.validate_repository(self.root)
        self.assertIn(
            "discovery configuration: family set mismatch",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
