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
import urllib.error
import urllib.parse
from unittest import mock


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

    @staticmethod
    def shorten_first_csv_row(path: Path) -> None:
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[1] = lines[1].split(",", 1)[0]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    @staticmethod
    def extend_first_csv_row(path: Path) -> None:
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[1] += ",unexpected-extra-field"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def copy_configuration(self) -> None:
        for relative in (
            search.PROTOCOL_PATH,
            search.QUERY_CONFIG_PATH,
            search.JOURNAL_REGISTRY_PATH,
        ):
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(PROJECT_ROOT / relative, destination)

    def copy_repository_validation_fixture(self) -> None:
        for relative in (*validator.REQUIRED_PATHS, validator.SEED_PATH):
            source = PROJECT_ROOT / relative
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        for registry_spec in validator.REGISTRY_SPECS:
            source = PROJECT_ROOT / registry_spec.path
            destination = self.root / registry_spec.path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

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
        esearch = self.add_artifact(
            run_dir,
            f"raw/{stem}.esearch.json",
            json.dumps(
                {
                    "esearchresult": {
                        "count": str(reported_count),
                        "webenv": "test-webenv",
                        "querykey": "1",
                    }
                }
            ).encode(),
        )
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
            "query": (
                f'test query AND ("{date_start}"[Date - Publication] : '
                f'"{date_end}"[Date - Publication])'
            ),
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
        parent_esearch = self.add_artifact(
            run_dir,
            "raw/parent.esearch.json",
            json.dumps(
                {
                    "esearchresult": {
                        "count": "10000",
                        "webenv": "unused-parent",
                        "querykey": "1",
                    }
                }
            ).encode(),
        )
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
            "query": (
                'test query AND ("2020/01/01"[Date - Publication] : '
                '"2020/12/31"[Date - Publication])'
            ),
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
        run_dir = parent / "wave_03_lineage_resolution"
        run_dir.mkdir(parents=True)
        query_id = "SEARCH-20260720-LINEAGE-CAUSAL-01"
        named_source_id = "NS-CAUSAL-001"
        candidate_key = "DOI:10.1234/example"
        response = self.add_artifact(
            run_dir,
            "raw/crossref.json",
            json.dumps(
                {
                    "status": "ok",
                    "message": {
                        "total-results": 10,
                        "items": [
                            {
                                "DOI": "10.1234/example",
                                "title": ["Example method"],
                                "published": {"date-parts": [[2020]]},
                                "container-title": ["Example Journal"],
                                "author": [{"family": "Smith"}],
                                "type": "journal-article",
                                "URL": "https://doi.org/10.1234/example",
                            }
                        ],
                    },
                }
            ).encode(),
        )
        pubmed_headers = [
            "candidate_key", "query_id", "named_source_id", "candidate_rank",
            "pmid", "doi", "title", "year", "journal", "authors", "source_url",
            "raw_path", "raw_sha256",
        ]
        crossref_headers = [
            "candidate_key", "query_id", "named_source_id", "bibliographic_query",
            "candidate_rank", "doi", "title", "year", "container_title",
            "first_author", "type", "url", "raw_path", "raw_sha256",
        ]
        self.write_csv(run_dir / "pubmed_lineage_candidates.csv", pubmed_headers, [])
        self.write_csv(
            run_dir / "crossref_candidates.csv",
            crossref_headers,
            [{
                "candidate_key": candidate_key,
                "query_id": query_id,
                "named_source_id": named_source_id,
                "bibliographic_query": "Example method Smith 2020",
                "candidate_rank": "1",
                "doi": "10.1234/example",
                "title": "Example method",
                "year": "2020",
                "container_title": "Example Journal",
                "first_author": "Smith",
                "type": "journal-article",
                "url": "https://doi.org/10.1234/example",
                "raw_path": response["path"],
                "raw_sha256": response["sha256"],
            }],
        )
        pubmed = {
            "path": "pubmed_lineage_candidates.csv",
            "sha256": self.sha(run_dir / "pubmed_lineage_candidates.csv"),
        }
        crossref = {
            "path": "crossref_candidates.csv",
            "sha256": self.sha(run_dir / "crossref_candidates.csv"),
        }
        (run_dir / "MANIFEST_SHA256.json").write_text(
            json.dumps({"algorithm": "SHA256", "files": [response, pubmed, crossref]}), encoding="utf-8"
        )
        lineage_registry = run_dir / "LINEAGE_QUERY_REGISTRY.csv"
        registry_headers = [
            "query_id", "named_source_id", "method_label", "canonical_name", "family",
            "source_role", "source", "query_variant", "query", "seed_candidate_keys",
            "reviewer",
        ]
        self.write_csv(
            lineage_registry,
            registry_headers,
            [{
                "query_id": query_id,
                "named_source_id": named_source_id,
                "method_label": "Example method",
                "canonical_name": "Example method",
                "family": "causal_policy",
                "source_role": "original_candidate",
                "source": "crossref",
                "query_variant": "exact_title",
                "query": "Example method Smith 2020",
                "seed_candidate_keys": "PMID:1",
                "reviewer": "reviewer-a",
            }],
        )
        registry_relative = lineage_registry.relative_to(self.root).as_posix()
        receipt = {
            "schema_version": 1,
            "executed_at": "2026-07-20T12:00:00+08:00",
            "timezone": "Asia/Shanghai",
            "tool_version": "test",
            "configuration_files": [
                {"path": str(search.PROTOCOL_PATH), "sha256": self.sha(self.root / search.PROTOCOL_PATH)},
                {"path": str(search.QUERY_CONFIG_PATH), "sha256": self.sha(self.root / search.QUERY_CONFIG_PATH)},
                {"path": str(search.JOURNAL_REGISTRY_PATH), "sha256": self.sha(self.root / search.JOURNAL_REGISTRY_PATH)},
                {"path": registry_relative, "sha256": self.sha(lineage_registry)},
            ],
            "queries": [{
                "query_id": query_id,
                "source": "crossref",
                "query": "Example method Smith 2020",
                "reported_count": 10,
                "raw_path": response["path"],
                "raw_sha256": response["sha256"],
                "status": "complete",
                "response_path": response["path"],
                "response_sha256": response["sha256"],
                "returned_candidate_count": 1,
                "total_results": 10,
                "rows": 5,
            }],
        }
        (run_dir / "LINEAGE_RUN_RECEIPT.json").write_text(json.dumps(receipt), encoding="utf-8")
        identity_headers = [
            "identity_decision_id", "named_source_id", "supporting_query_ids",
            "candidate_keys_considered", "primary_selected_candidate_key",
            "primary_decision", "primary_reason", "primary_reviewer",
            "audit_selected_candidate_key", "audit_decision", "audit_reason",
            "audit_reviewer", "conflict_status", "adjudicator",
            "final_selected_candidate_key", "final_decision", "final_reason",
            "inspected_primary_url",
        ]
        self.write_csv(
            run_dir / "lineage_identity_audit.csv",
            identity_headers,
            [{
                "identity_decision_id": "ID-DEC-001",
                "named_source_id": named_source_id,
                "supporting_query_ids": query_id,
                "candidate_keys_considered": candidate_key,
                "primary_selected_candidate_key": candidate_key,
                "primary_decision": "resolved",
                "primary_reason": "The candidate identity matches the inspected record.",
                "primary_reviewer": "reviewer-a",
                "audit_selected_candidate_key": candidate_key,
                "audit_decision": "resolved",
                "audit_reason": "Independent inspection confirms the identity.",
                "audit_reviewer": "reviewer-b",
                "conflict_status": "none",
                "adjudicator": "",
                "final_selected_candidate_key": candidate_key,
                "final_decision": "resolved",
                "final_reason": "Independent inspection confirms the identity.",
                "inspected_primary_url": "https://doi.org/10.1234/example",
            }],
        )
        global_dir = parent / "global"
        ledger_headers = [
            "identity_decision_id", "named_source_id", "final_candidate_key",
            "method_label", "canonical_name", "family", "source_role", "title",
            "year", "doi", "pmid", "primary_url", "discovery_route",
            "bibliographic_role_evidence", "verification_state", "search_ids",
            "status", "notes",
        ]
        self.write_csv(
            global_dir / "lineage_ledger.csv",
            ledger_headers,
            [{
                "identity_decision_id": "ID-DEC-001",
                "named_source_id": named_source_id,
                "final_candidate_key": candidate_key,
                "method_label": "Example method",
                "canonical_name": "Example method",
                "family": "causal_policy",
                "source_role": "original_candidate",
                "title": "Example method",
                "year": "2020",
                "doi": "10.1234/example",
                "pmid": "",
                "primary_url": "https://doi.org/10.1234/example",
                "discovery_route": "lineage query",
                "bibliographic_role_evidence": "Title and publisher record inspected.",
                "verification_state": "discovery",
                "search_ids": query_id,
                "status": "resolved_identity_role_unverified",
                "notes": "",
            }],
        )
        return run_dir

    def make_valid_phase_run(self) -> Path:
        self.copy_repository_validation_fixture()
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
                        json.dumps(
                            {
                                "esearchresult": {
                                    "count": "0",
                                    "webenv": "empty-history",
                                    "querykey": "1",
                                }
                            }
                        ).encode(),
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
        global_dir = phase / "global"
        global_headers = [
            "candidate_key", "waves", "wave_source_row_sha256s", "screening_path",
            "final_decision", "final_proposed_record_type", "final_reason_code",
            "duplicate_disposition",
        ]
        self.write_csv(
            global_dir / "candidates_through_wave_02.csv",
            global_headers,
            [{
                "candidate_key": "PMID:1",
                "waves": "wave_01|wave_02",
                "wave_source_row_sha256s": f"wave_01:{'d' * 64}|wave_02:{'d' * 64}",
                "screening_path": "wave_01_frozen_queries/screened_candidates.csv",
                "final_decision": "include_applied_seed",
                "final_proposed_record_type": "applied_seed",
                "final_reason_code": "I_APPLIED_TRANSFERABLE_DESIGN",
                "duplicate_disposition": "screened_in_wave_01",
            }],
        )
        (global_dir / "GLOBAL_KEY_RECONCILIATION.txt").write_text(
            "ALL WAVE, SCREENING, REGISTRY, AND LINEAGE KEYS RECONCILE\n",
            encoding="utf-8",
        )
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

    @staticmethod
    def fake_response(data: bytes):
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self) -> bytes:
                return data

        return Response()

    @staticmethod
    def pubmed_xml(records: list[dict[str, str]]) -> bytes:
        rendered: list[str] = ["<PubmedArticleSet>"]
        for record in records:
            record_type = record.get("record_type", "PubmedArticle")
            rendered.append(
                f"""<{record_type}>
  <MedlineCitation>
    <PMID>{record.get('pmid', '')}</PMID>
    <Article>
      <Journal><Title>{record.get('journal', 'Journal')}</Title><JournalIssue><PubDate><Year>{record.get('year', '2020')}</Year></PubDate></JournalIssue></Journal>
      <ArticleTitle>{record.get('title', 'Title')}</ArticleTitle>
      <Abstract><AbstractText>{record.get('abstract', 'Abstract')}</AbstractText></Abstract>
      <AuthorList><Author><ForeName>Ada</ForeName><LastName>Lovelace</LastName></Author></AuthorList>
      <PublicationTypeList><PublicationType>Journal Article</PublicationType></PublicationTypeList>
    </Article>
  </MedlineCitation>
  <PubmedData><ArticleIdList><ArticleId IdType="doi">{record.get('doi', '')}</ArticleId></ArticleIdList></PubmedData>
</{record_type}>"""
            )
        rendered.append("</PubmedArticleSet>")
        return "".join(rendered).encode()

    def test_execute_pubmed_cell_writes_atomic_complete_artifacts(self):
        output = self.root / "wave"
        query = (
            '("difference in differences"[Title]) AND infection*[Title/Abstract] '
            'AND ("2020/01/01"[Date - Publication] : '
            '"2020/12/31"[Date - Publication])'
        )
        cell = search.SearchCell(
            search_id="SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            lane="FAMILY",
            family="causal_policy",
            source="pubmed",
            query=query,
            parent_search_id="",
            date_start="2020/01/01",
            date_end="2020/12/31",
        )
        calls: list[dict[str, list[str]]] = []

        def opener(request, timeout=0):
            del timeout
            parsed = urllib.parse.urlparse(request.full_url)
            params = urllib.parse.parse_qs(parsed.query)
            calls.append(params)
            if parsed.path.endswith("esearch.fcgi"):
                self.assertEqual(params["term"], [query])
                self.assertEqual(params["usehistory"], ["y"])
                return self.fake_response(
                    json.dumps(
                        {"esearchresult": {"count": "201", "webenv": "ENV-EXACT", "querykey": "7"}}
                    ).encode()
                )
            retstart = int(params["retstart"][0])
            count = 200 if retstart == 0 else 1
            self.assertEqual(params["WebEnv"], ["ENV-EXACT"])
            self.assertEqual(params["query_key"], ["7"])
            return self.fake_response(
                self.pubmed_xml(
                    [
                        {
                            "pmid": str(retstart + offset + 1),
                            "doi": f"10.1000/{retstart + offset + 1}",
                            "title": f"Paper {retstart + offset + 1}",
                            "record_type": "PubmedBookArticle" if offset == count - 1 else "PubmedArticle",
                        }
                        for offset in range(count)
                    ]
                )
            )

        with mock.patch("time.sleep") as sleep:
            receipt = search.execute_pubmed_cell(
                cell, output, "test@example.invalid", opener=opener
            )

        self.assertEqual(receipt["query"], query)
        self.assertEqual(receipt["webenv"], "ENV-EXACT")
        self.assertEqual(receipt["query_key"], "7")
        self.assertEqual(receipt["retrieved_count"], 201)
        self.assertEqual(
            [(page["retstart"], page["retmax"], page["parsed_count"]) for page in receipt["efetch_pages"]],
            [(0, 200, 200), (200, 1, 1)],
        )
        manifest = json.loads((output / "MANIFEST_SHA256.json").read_text())
        self.assertEqual(len(manifest["files"]), 3)
        self.assertTrue(all((output / item["path"]).is_file() for item in manifest["files"]))
        self.assertEqual(list(output.rglob("*.tmp")), [])
        self.assertNotIn("api_key", json.dumps(receipt))
        self.assertEqual(len(calls), 3)
        self.assertEqual(sleep.call_count, 2)

    def test_compile_flags_title_only_possible_duplicates(self):
        run_dir = self.root / "run"
        run_dir.mkdir()
        page_a = self.add_artifact(
            run_dir,
            "raw/a.xml",
            self.pubmed_xml(
                [{"pmid": "101", "doi": "10.1000/a", "title": "Café transmission", "year": "2020"}]
            ),
        )
        page_b = self.add_artifact(
            run_dir,
            "raw/b.xml",
            self.pubmed_xml(
                [{"pmid": "202", "doi": "10.1000/b", "title": "CAFÉ   TRANSMISSION", "year": "2021"}]
            ),
        )
        receipt = {
            "cells": [
                {
                    "search_id": "SEARCH-1",
                    "lane": "FAMILY",
                    "family": "causal_policy",
                    "cell_type": "leaf",
                    "efetch_pages": [{"path": page_a["path"], "sha256": page_a["sha256"]}],
                },
                {
                    "search_id": "SEARCH-2",
                    "lane": "VENUE",
                    "family": "causal_policy",
                    "cell_type": "leaf",
                    "efetch_pages": [{"path": page_b["path"], "sha256": page_b["sha256"]}],
                },
            ]
        }
        (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt), encoding="utf-8")
        (run_dir / "MANIFEST_SHA256.json").write_text(
            json.dumps({"algorithm": "SHA256", "files": [page_a, page_b]}),
            encoding="utf-8",
        )

        rows = search.compile_pubmed_candidates(run_dir)

        self.assertEqual(len(rows), 2)
        self.assertNotEqual(rows[0]["candidate_key"], rows[1]["candidate_key"])
        groups = {row["possible_duplicate_group"] for row in rows}
        self.assertEqual(len(groups), 1)
        self.assertNotEqual(groups, {""})
        self.assertTrue((run_dir / "compiled_candidates_raw.csv").is_file())
        compiled_entry = next(
            item
            for item in json.loads((run_dir / "MANIFEST_SHA256.json").read_text())["files"]
            if item["path"] == "compiled_candidates_raw.csv"
        )
        self.assertEqual(compiled_entry["sha256"], self.sha(run_dir / compiled_entry["path"]))

    def test_pubmed_http_and_timeout_failures_are_stable_and_atomic(self):
        cell = search.SearchCell(
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "FAMILY", "causal_policy", "pubmed", "query", "",
            "2020/01/01", "2020/12/31",
        )
        failures = (
            urllib.error.HTTPError("https://example.invalid", 503, "unavailable", {}, None),
            TimeoutError("timed out"),
        )
        for index, failure in enumerate(failures):
            with self.subTest(failure=type(failure).__name__):
                output = self.root / f"failure-{index}"

                def opener(_request, timeout=0):
                    del timeout
                    raise failure

                with self.assertRaisesRegex(search.DiscoveryExecutionError, "network request failed"):
                    search.execute_pubmed_cell(
                        cell, output, "test@example.invalid", opener=opener
                    )
                self.assertEqual(list(output.rglob("*.tmp")), [])
                self.assertEqual(list((output / "raw").glob("*")), [])

    def test_malformed_esearch_json_leaves_no_final_artifact(self):
        output = self.root / "malformed-esearch"
        cell = search.SearchCell(
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "FAMILY", "causal_policy", "pubmed", "query", "",
            "2020/01/01", "2020/12/31",
        )

        with self.assertRaisesRegex(search.DiscoveryExecutionError, "malformed PubMed ESearch JSON"):
            search.execute_pubmed_cell(
                cell,
                output,
                "test@example.invalid",
                opener=lambda *_args, **_kwargs: self.fake_response(b"not-json"),
            )
        self.assertEqual(list(output.rglob("*.tmp")), [])
        self.assertEqual(list((output / "raw").glob("*")), [])

    def test_malformed_xml_and_count_mismatch_leave_no_final_page(self):
        cell = search.SearchCell(
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "FAMILY", "causal_policy", "pubmed", "query", "",
            "2020/01/01", "2020/12/31",
        )
        for name, page, message in (
            ("xml", b"<not-closed", "malformed PubMed EFetch XML"),
            ("count", b"<PubmedArticleSet />", "PubMed count mismatch"),
        ):
            with self.subTest(name=name):
                output = self.root / f"bad-{name}"
                responses = iter(
                    (
                        self.fake_response(
                            json.dumps(
                                {"esearchresult": {"count": "1", "webenv": "ENV", "querykey": "1"}}
                            ).encode()
                        ),
                        self.fake_response(page),
                    )
                )
                with mock.patch("time.sleep"):
                    with self.assertRaisesRegex(search.DiscoveryExecutionError, message):
                        search.execute_pubmed_cell(
                            cell,
                            output,
                            "test@example.invalid",
                            opener=lambda *_args, **_kwargs: next(responses),
                        )
                self.assertEqual(list(output.rglob("*.tmp")), [])
                self.assertEqual(list((output / "raw").glob("*.xml")), [])
                self.assertEqual(len(list((output / "raw").glob("*.esearch.json"))), 1)

    def test_recursive_split_manifests_parents_and_year_month_day_leaves(self):
        output = self.root / "split"
        cell = search.SearchCell(
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "FAMILY", "causal_policy", "pubmed",
            'method AND ("2020/01/01"[Date - Publication] : "2021/12/31"[Date - Publication])',
            "", "2020/01/01", "2021/12/31",
        )
        counts = {
            ("2020/01/01", "2021/12/31"): 10000,
            ("2020/01/01", "2020/12/31"): 10000,
            ("2021/01/01", "2021/12/31"): 0,
            ("2020/01/01", "2020/01/31"): 10000,
        }
        for month in range(2, 13):
            last = 29 if month == 2 else 30 if month in {4, 6, 9, 11} else 31
            counts[(f"2020/{month:02d}/01", f"2020/{month:02d}/{last:02d}")] = 0
        for day in range(1, 32):
            counts[(f"2020/01/{day:02d}", f"2020/01/{day:02d}")] = 9999 if day == 1 else 1 if day == 2 else 0
        efetch_offsets: dict[str, int] = {}

        def opener(request, timeout=0):
            del timeout
            parsed = urllib.parse.urlparse(request.full_url)
            params = urllib.parse.parse_qs(parsed.query)
            if parsed.path.endswith("esearch.fcgi"):
                interval = search._query_date_interval(params["term"][0])
                self.assertIn(interval, counts)
                query_key = f"Q{len(efetch_offsets) + 1}"
                efetch_offsets[query_key] = counts[interval]
                return self.fake_response(
                    json.dumps(
                        {
                            "esearchresult": {
                                "count": str(counts[interval]),
                                "webenv": f"ENV-{query_key}",
                                "querykey": query_key,
                            }
                        }
                    ).encode()
                )
            query_key = params["query_key"][0]
            retmax = int(params["retmax"][0])
            return self.fake_response(
                b"<PubmedArticleSet>"
                + b"<PubmedArticle />" * retmax
                + b"</PubmedArticleSet>"
            )

        with mock.patch("time.sleep"):
            receipt = search.execute_pubmed_cell(
                cell, output, "test@example.invalid", opener=opener
            )

        self.assertEqual(receipt["cell_type"], "split_parent")
        self.assertEqual(len(receipt["children"]), 2)
        year_2020 = receipt["children"][0]
        self.assertEqual(year_2020["cell_type"], "split_parent")
        self.assertEqual(len(year_2020["children"]), 12)
        january = year_2020["children"][0]
        self.assertEqual(january["cell_type"], "split_parent")
        self.assertEqual(len(january["children"]), 31)
        leaves = search._leaf_receipts([receipt])
        self.assertTrue(all(leaf["reported_count"] < 10000 for leaf in leaves))
        manifest = json.loads((output / "MANIFEST_SHA256.json").read_text())
        esearch_entries = [item for item in manifest["files"] if item["path"].endswith(".esearch.json")]
        self.assertEqual(len(esearch_entries), 46)
        self.assertNotIn("webenv", receipt)
        self.assertNotIn("query_key", receipt)

    def test_unsplittable_pubmed_day_stops_before_efetch(self):
        output = self.root / "unsplittable"
        cell = search.SearchCell(
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "FAMILY", "causal_policy", "pubmed",
            'method AND ("2020/01/01"[Date - Publication] : "2020/01/01"[Date - Publication])',
            "", "2020/01/01", "2020/01/01",
        )

        def opener(request, timeout=0):
            del timeout
            self.assertTrue(request.full_url.startswith(search.PUBMED_ESEARCH_URL))
            return self.fake_response(
                json.dumps(
                    {"esearchresult": {"count": "10000", "webenv": "ENV", "querykey": "1"}}
                ).encode()
            )

        with self.assertRaisesRegex(search.DiscoveryExecutionError, "unsplittable PubMed cell"):
            search.execute_pubmed_cell(
                cell, output, "test@example.invalid", opener=opener
            )
        manifest = json.loads((output / "MANIFEST_SHA256.json").read_text())
        self.assertEqual(len(manifest["files"]), 1)
        self.assertEqual(list((output / "raw").glob("*.xml")), [])

    def test_run_resume_skips_valid_leaf_and_restarts_tampered_leaf_with_fresh_history(self):
        self.copy_configuration()
        output = self.root / "resume"
        cell = search.SearchCell(
            "SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01",
            "FAMILY", "causal_policy", "pubmed",
            'method AND ("2020/01/01"[Date - Publication] : "2020/12/31"[Date - Publication])',
            "", "2020/01/01", "2020/12/31",
        )

        def opener_for(history: str, calls: list[str]):
            def opener(request, timeout=0):
                del timeout
                parsed = urllib.parse.urlparse(request.full_url)
                calls.append(parsed.path)
                if parsed.path.endswith("esearch.fcgi"):
                    return self.fake_response(
                        json.dumps(
                            {"esearchresult": {"count": "1", "webenv": history, "querykey": "1"}}
                        ).encode()
                    )
                return self.fake_response(
                    self.pubmed_xml([{"pmid": "1", "title": "Resume paper"}])
                )

            return opener

        first_calls: list[str] = []
        with mock.patch("time.sleep"):
            first = search.execute_pubmed_run(
                self.root,
                [cell],
                output,
                "test@example.invalid",
                opener=opener_for("ENV-OLD", first_calls),
            )
        self.assertEqual(first["cells"][0]["webenv"], "ENV-OLD")
        self.assertEqual(len(first_calls), 2)

        skipped_calls: list[str] = []
        second = search.execute_pubmed_run(
            self.root,
            [cell],
            output,
            "test@example.invalid",
            opener=opener_for("ENV-SHOULD-NOT-BE-USED", skipped_calls),
        )
        self.assertEqual(skipped_calls, [])
        self.assertEqual(second["cells"][0]["webenv"], "ENV-OLD")

        page = next((output / "raw").glob("*.xml"))
        page.write_bytes(page.read_bytes() + b"tampered")
        fresh_calls: list[str] = []
        with mock.patch("time.sleep"):
            third = search.execute_pubmed_run(
                self.root,
                [cell],
                output,
                "test@example.invalid",
                opener=opener_for("ENV-FRESH", fresh_calls),
            )
        self.assertEqual(third["cells"][0]["webenv"], "ENV-FRESH")
        self.assertEqual(len(fresh_calls), 2)
        self.assertEqual(list(output.rglob("*.tmp")), [])
        self.assertNotIn("api_key", (output / "RUN_RECEIPT.json").read_text())
        self.assertEqual(search.validate_search_run(output), [])

        page = next((output / "raw").glob("*.xml"))
        page.write_bytes(b"<PubmedArticleSet />")
        changed_sha = self.sha(page)
        manifest_path = output / "MANIFEST_SHA256.json"
        manifest = json.loads(manifest_path.read_text())
        next(item for item in manifest["files"] if item["path"].endswith(".xml"))[
            "sha256"
        ] = changed_sha
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        receipt_path = output / "RUN_RECEIPT.json"
        forged = json.loads(receipt_path.read_text())
        forged["cells"][0]["efetch_pages"][0]["sha256"] = changed_sha
        receipt_path.write_text(json.dumps(forged), encoding="utf-8")
        semantic_calls: list[str] = []
        with mock.patch("time.sleep"):
            fourth = search.execute_pubmed_run(
                self.root,
                [cell],
                output,
                "test@example.invalid",
                opener=opener_for("ENV-SEMANTIC-FRESH", semantic_calls),
            )
        self.assertEqual(fourth["cells"][0]["webenv"], "ENV-SEMANTIC-FRESH")
        self.assertEqual(len(semantic_calls), 2)

    def test_compile_identifier_matches_auto_deduplicate_and_merge_provenance(self):
        run_dir = self.root / "dedup"
        run_dir.mkdir()
        first = self.add_artifact(
            run_dir,
            "raw/first.xml",
            self.pubmed_xml([{"pmid": "101", "doi": "10.1000/SAME", "title": "First rendering"}]),
        )
        second = self.add_artifact(
            run_dir,
            "raw/second.xml",
            self.pubmed_xml([{"pmid": "202", "doi": "https://doi.org/10.1000/same", "title": "Second rendering"}]),
        )
        (run_dir / "RUN_RECEIPT.json").write_text(
            json.dumps(
                {
                    "cells": [
                        {
                            "search_id": "SEARCH-A", "lane": "FAMILY",
                            "family": "causal_policy", "cell_type": "leaf",
                            "efetch_pages": [first],
                        },
                        {
                            "search_id": "SEARCH-B", "lane": "VENUE",
                            "family": "simulation_methods", "cell_type": "leaf",
                            "efetch_pages": [second],
                        },
                    ]
                }
            ),
            encoding="utf-8",
        )
        (run_dir / "MANIFEST_SHA256.json").write_text(
            json.dumps({"algorithm": "SHA256", "files": [first, second]}),
            encoding="utf-8",
        )

        rows = search.compile_pubmed_candidates(run_dir)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["search_ids"], "SEARCH-A|SEARCH-B")
        self.assertEqual(rows[0]["lanes"], "FAMILY|VENUE")
        self.assertEqual(rows[0]["preliminary_families"], "causal_policy|simulation_methods")
        self.assertEqual(rows[0]["deduplication_basis"], "doi")

    def test_compile_rejects_page_not_matching_its_manifest_receipt(self):
        run_dir = self.root / "compile-lock"
        run_dir.mkdir()
        page = self.add_artifact(
            run_dir,
            "raw/page.xml",
            self.pubmed_xml([{"pmid": "1", "title": "Manifested paper"}]),
        )
        (run_dir / "RUN_RECEIPT.json").write_text(
            json.dumps(
                {
                    "cells": [
                        {
                            "search_id": "SEARCH-A", "lane": "FAMILY",
                            "family": "causal_policy", "cell_type": "leaf",
                            "efetch_pages": [page],
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        (run_dir / "MANIFEST_SHA256.json").write_text(
            json.dumps({"algorithm": "SHA256", "files": [page]}),
            encoding="utf-8",
        )
        (run_dir / "raw/page.xml").write_bytes(
            self.pubmed_xml([{"pmid": "2", "title": "Unmanifested replacement"}])
        )
        with self.assertRaisesRegex(
            search.DiscoveryExecutionError, "compile input checksum mismatch"
        ):
            search.compile_pubmed_candidates(run_dir)

    def test_crossref_resolution_is_bounded_manifested_and_has_no_decision(self):
        output = self.root / "crossref"
        calls: list[dict[str, list[str]]] = []

        def opener(request, timeout=0):
            del timeout
            params = urllib.parse.parse_qs(urllib.parse.urlparse(request.full_url).query)
            calls.append(params)
            return self.fake_response(
                json.dumps(
                    {
                        "status": "ok",
                        "message": {
                            "total-results": 12,
                            "items": [
                                {
                                    "DOI": "10.1000/ONE",
                                    "title": ["Method one"],
                                    "published": {"date-parts": [[2020]]},
                                    "container-title": ["Journal"],
                                    "author": [{"family": "Smith", "given": "A"}],
                                    "type": "journal-article",
                                    "URL": "https://doi.org/10.1000/one",
                                },
                                {
                                    "title": ["Method two"],
                                    "published": {"date-parts": [[2021]]},
                                    "container-title": ["Journal"],
                                    "author": [{"family": "Jones"}],
                                    "type": "journal-article",
                                    "URL": "https://example.invalid/two",
                                },
                            ],
                        },
                    }
                ).encode()
            )

        receipt = search.resolve_crossref_candidates(
            "SEARCH-20260720-LINEAGE-CAUSAL-01",
            "Exact method citation Smith 2020",
            output,
            "test@example.invalid",
            opener=opener,
        )

        self.assertEqual(calls[0]["query.bibliographic"], ["Exact method citation Smith 2020"])
        self.assertEqual(calls[0]["rows"], ["5"])
        self.assertEqual(calls[0]["mailto"], ["test@example.invalid"])
        self.assertNotIn("cursor", calls[0])
        self.assertEqual(receipt["returned_candidate_count"], 2)
        self.assertEqual(receipt["total_results"], 12)
        self.assertEqual(receipt["rows"], 5)
        self.assertFalse(any("decision" in key for key in receipt))
        manifest = json.loads((output / "MANIFEST_SHA256.json").read_text())
        self.assertEqual(len(manifest["files"]), 1)
        raw = output / receipt["response_path"]
        self.assertEqual(receipt["response_sha256"], self.sha(raw))

    def wave_two_rows(self, status_by_family: dict[str, str]) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        infectious_block = json.loads(
            (PROJECT_ROOT / search.QUERY_CONFIG_PATH).read_text(encoding="utf-8")
        )["infectious_disease_block"]
        tokens = {
            "causal_policy": "CAUSAL",
            "surveillance_measurement": "SURVEILLANCE",
            "spatial_transmission": "SPATIAL",
            "forecasting_dynamics": "FORECASTING",
            "evidence_synthesis": "EVIDENCE",
            "simulation_methods": "SIMULATION",
        }
        for number, family in enumerate(sorted(search.FAMILIES), 1):
            status = status_by_family.get(family, "no_expansion_needed")
            executed = status == "executed"
            rows.append(
                {
                    "family": family,
                    "search_id": f"SEARCH-20260720-PUBMED-FAMILY-{tokens[family]}-{number + 1:02d}" if executed else "",
                    "status": status,
                    "new_synonyms": "new method label" if executed else "",
                    "rationale": "The completed Wave 1 review documented this family decision.",
                    "source_candidate_keys": "PMID:1",
                    "source": "pubmed" if executed else "",
                    "query": (
                        f'new method label[Title] AND {infectious_block} '
                        'AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])'
                    ) if executed else "",
                    "date_start": "2010/01/01" if executed else "",
                    "date_end": "2026/12/31" if executed else "",
                    "reviewer": "reviewer-a",
                }
            )
        return rows

    def test_run_wave_rejects_missing_family_and_executes_only_executed_rows(self):
        self.copy_configuration()
        output = self.root / "wave_02_synonym_expansion"
        registry = output / "QUERY_REGISTRY.csv"
        headers = [
            "family", "search_id", "status", "new_synonyms", "rationale",
            "source_candidate_keys", "source", "query", "date_start", "date_end",
            "reviewer",
        ]
        rows = self.wave_two_rows({"causal_policy": "executed"})
        self.write_csv(registry, headers, rows[:-1])
        calls: list[str] = []

        def no_network(request, timeout=0):
            del request, timeout
            calls.append("called")
            raise AssertionError("malformed registry must fail before network")

        with self.assertRaisesRegex(search.DiscoveryExecutionError, "Wave 2 family set mismatch"):
            search.execute_wave(
                self.root, registry, output, "test@example.invalid", opener=no_network
            )
        self.assertEqual(calls, [])

        self.write_csv(registry, headers, rows)

        def opener(request, timeout=0):
            del timeout
            calls.append(urllib.parse.urlparse(request.full_url).path)
            return self.fake_response(
                json.dumps(
                    {"esearchresult": {"count": "0", "webenv": "EMPTY", "querykey": "1"}}
                ).encode()
            )

        receipt = search.execute_wave(
            self.root, registry, output, "test@example.invalid", opener=opener
        )
        self.assertEqual(len(receipt["cells"]), 1)
        self.assertEqual(len(calls), 1)
        self.assertEqual(receipt["cells"][0]["family"], "causal_policy")

    def test_run_wave_rejects_wrong_family_id_and_missing_infectious_block(self):
        self.copy_configuration()
        output = self.root / "wave_02_synonym_expansion"
        registry = output / "QUERY_REGISTRY.csv"
        headers = list(search.WAVE_TWO_QUERY_HEADERS)
        rows = self.wave_two_rows({"causal_policy": "executed"})
        executed = next(row for row in rows if row["status"] == "executed")
        executed["search_id"] = "SEARCH-20260720-PUBMED-FAMILY-SPATIAL-99"
        executed["query"] = (
            'new method label[Title] AND '
            '("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])'
        )
        self.write_csv(registry, headers, rows)

        with self.assertRaisesRegex(
            search.DiscoveryExecutionError,
            "Wave 2 search_id family mismatch.*Wave 2 infectious block mismatch",
        ):
            search.execute_wave(
                self.root,
                registry,
                output,
                "test@example.invalid",
                opener=lambda *_args, **_kwargs: self.fail("invalid registry called network"),
            )

    def test_run_wave_accepts_exact_all_no_expansion_empty_artifacts(self):
        self.copy_configuration()
        output = self.root / "wave_02_synonym_expansion"
        registry = output / "QUERY_REGISTRY.csv"
        headers = [
            "family", "search_id", "status", "new_synonyms", "rationale",
            "source_candidate_keys", "source", "query", "date_start", "date_end",
            "reviewer",
        ]
        self.write_csv(registry, headers, self.wave_two_rows({}))

        receipt = search.execute_wave(
            self.root,
            registry,
            output,
            "test@example.invalid",
            opener=lambda *_args, **_kwargs: self.fail("empty wave called network"),
        )

        self.assertEqual(receipt["cells"], [])
        self.assertEqual(receipt["empty_reason"], "all_families_no_expansion_needed")
        self.assertFalse((output / "raw").exists())
        self.assertEqual(search.validate_search_run(output), [])
        self.assertEqual(search.validate_screening(output), [])
        self.assertEqual(search.validate_screening_audit(output), [])

    def lineage_registry_rows(self) -> list[dict[str, str]]:
        return [
            {
                "query_id": "SEARCH-20260720-LINEAGE-CAUSAL-01",
                "named_source_id": "NS-CAUSAL-001",
                "method_label": "Method A",
                "canonical_name": "Method A",
                "family": "causal_policy",
                "source_role": "original_candidate",
                "source": "pubmed",
                "query_variant": "exact_title",
                "query": '"Exact PubMed method title"[Title]',
                "seed_candidate_keys": "PMID:seed-a",
                "reviewer": "reviewer-a",
            },
            {
                "query_id": "SEARCH-20260720-LINEAGE-SIMULATION-01",
                "named_source_id": "NS-SIMULATION-001",
                "method_label": "Method B",
                "canonical_name": "Method B",
                "family": "simulation_methods",
                "source_role": "guidance",
                "source": "crossref",
                "query_variant": "exact_title",
                "query": "Exact Crossref method citation",
                "seed_candidate_keys": "PMID:seed-b",
                "reviewer": "reviewer-c",
            },
        ]

    def complete_lineage_decisions(self, output: Path) -> None:
        registry_path = output / "LINEAGE_QUERY_REGISTRY.csv"
        with registry_path.open(encoding="utf-8", newline="") as handle:
            registry = {row["query_id"]: row for row in csv.DictReader(handle)}
        candidates: dict[str, dict[str, str]] = {}
        for filename in ("pubmed_lineage_candidates.csv", "crossref_candidates.csv"):
            with (output / filename).open(encoding="utf-8", newline="") as handle:
                for row in csv.DictReader(handle):
                    candidates[row["query_id"]] = row
        audit_rows: list[dict[str, str]] = []
        ledger_rows: list[dict[str, str]] = []
        for number, query_id in enumerate(sorted(registry), 1):
            source = registry[query_id]
            candidate = candidates[query_id]
            key = candidate["candidate_key"]
            url = candidate.get("source_url") or candidate.get("url") or ""
            decision_id = f"ID-DEC-{number:03d}"
            audit_rows.append(
                {
                    "identity_decision_id": decision_id,
                    "named_source_id": source["named_source_id"],
                    "supporting_query_ids": query_id,
                    "candidate_keys_considered": key,
                    "primary_selected_candidate_key": key,
                    "primary_decision": "resolved",
                    "primary_reason": "The candidate matches the inspected primary bibliographic record.",
                    "primary_reviewer": source["reviewer"],
                    "audit_selected_candidate_key": key,
                    "audit_decision": "resolved",
                    "audit_reason": "Independent inspection confirms the same bibliographic identity.",
                    "audit_reviewer": f"independent-{number}",
                    "conflict_status": "none",
                    "adjudicator": "",
                    "final_selected_candidate_key": key,
                    "final_decision": "resolved",
                    "final_reason": "Both reviewers independently selected the same record.",
                    "inspected_primary_url": url,
                }
            )
            ledger_rows.append(
                {
                    "identity_decision_id": decision_id,
                    "named_source_id": source["named_source_id"],
                    "final_candidate_key": key,
                    "method_label": source["method_label"],
                    "canonical_name": source["canonical_name"],
                    "family": source["family"],
                    "source_role": source["source_role"],
                    "title": candidate["title"],
                    "year": candidate["year"],
                    "doi": candidate["doi"],
                    "pmid": candidate.get("pmid", ""),
                    "primary_url": url,
                    "discovery_route": "bounded lineage identity query",
                    "bibliographic_role_evidence": "Bibliographic identity only; source role remains unverified.",
                    "verification_state": "discovery",
                    "search_ids": query_id,
                    "status": "resolved_identity_role_unverified",
                    "notes": "",
                }
            )
        self.write_csv(
            output / "lineage_identity_audit.csv",
            list(search.LINEAGE_AUDIT_HEADERS),
            audit_rows,
        )
        self.write_csv(
            output.parent / "global/lineage_ledger.csv",
            list(search.LINEAGE_LEDGER_HEADERS),
            ledger_rows,
        )

    def test_run_lineage_rejects_over_three_queries_before_network(self):
        self.copy_configuration()
        output = self.root / "phase/wave_03_lineage_resolution"
        registry = output / "LINEAGE_QUERY_REGISTRY.csv"
        base = self.lineage_registry_rows()[0]
        variants = ("exact_title", "title_first_author", "method_author_year", "exact_title")
        rows = [
            {
                **base,
                "query_id": f"SEARCH-20260720-LINEAGE-CAUSAL-{number:02d}",
                "query_variant": variant,
                "query": f"query {number}",
            }
            for number, variant in enumerate(variants, 1)
        ]
        self.write_csv(registry, list(search.LINEAGE_REGISTRY_HEADERS), rows)
        with self.assertRaisesRegex(
            search.DiscoveryExecutionError, "lineage named source has over three queries"
        ):
            search.execute_lineage(
                self.root,
                registry,
                output,
                "test@example.invalid",
                opener=lambda *_args, **_kwargs: self.fail("invalid registry called network"),
            )

    def test_run_lineage_dispatches_sources_and_validates_heterogeneous_receipt(self):
        self.copy_configuration()
        output = self.root / "phase/wave_03_lineage_resolution"
        registry = output / "LINEAGE_QUERY_REGISTRY.csv"
        self.write_csv(
            registry,
            list(search.LINEAGE_REGISTRY_HEADERS),
            self.lineage_registry_rows(),
        )
        calls: list[str] = []

        def opener(request, timeout=0):
            del timeout
            parsed = urllib.parse.urlparse(request.full_url)
            calls.append(parsed.path)
            if parsed.path.endswith("esearch.fcgi"):
                return self.fake_response(
                    json.dumps(
                        {"esearchresult": {"count": "1", "webenv": "LINEAGE-ENV", "querykey": "3"}}
                    ).encode()
                )
            if parsed.path.endswith("efetch.fcgi"):
                return self.fake_response(
                    self.pubmed_xml(
                        [
                            {
                                "pmid": "303",
                                "doi": "10.1000/pubmed-method",
                                "title": "Exact PubMed method title",
                                "year": "2018",
                            }
                        ]
                    )
                )
            return self.fake_response(
                json.dumps(
                    {
                        "status": "ok",
                        "message": {
                            "total-results": 1,
                            "items": [
                                {
                                    "DOI": "10.1000/crossref-method",
                                    "title": ["Exact Crossref method citation"],
                                    "published": {"date-parts": [[2019]]},
                                    "container-title": ["Methods Journal"],
                                    "author": [{"family": "Smith", "given": "A"}],
                                    "type": "journal-article",
                                    "URL": "https://doi.org/10.1000/crossref-method",
                                }
                            ],
                        },
                    }
                ).encode()
            )

        with mock.patch("time.sleep"):
            receipt = search.execute_lineage(
                self.root,
                registry,
                output,
                "test@example.invalid",
                opener=opener,
            )

        self.assertEqual([row["source"] for row in receipt["queries"]], ["pubmed", "crossref"])
        pubmed_receipt = receipt["queries"][0]
        self.assertEqual(pubmed_receipt["date_start"], "")
        self.assertEqual(pubmed_receipt["date_end"], "")
        self.assertEqual(pubmed_receipt["query_scope"], "unbounded_identity")
        self.assertEqual(pubmed_receipt["webenv"], "LINEAGE-ENV")
        crossref_receipt = receipt["queries"][1]
        self.assertFalse(any(field in crossref_receipt for field in ("webenv", "query_key", "efetch_pages")))
        self.assertEqual(len(calls), 3)
        with (output / "pubmed_lineage_candidates.csv").open(encoding="utf-8", newline="") as handle:
            self.assertEqual(len(list(csv.DictReader(handle))), 1)
        with (output / "crossref_candidates.csv").open(encoding="utf-8", newline="") as handle:
            self.assertEqual(len(list(csv.DictReader(handle))), 1)

        resume_calls: list[str] = []
        resumed = search.execute_lineage(
            self.root,
            registry,
            output,
            "test@example.invalid",
            opener=lambda request, timeout=0: (
                resume_calls.append(request.full_url),
                self.fail("valid lineage query called network"),
            )[1],
        )
        self.assertEqual(resume_calls, [])
        self.assertEqual(resumed["queries"], receipt["queries"])

        self.complete_lineage_decisions(output)
        self.assertEqual(search.validate_lineage(self.root, output), [])
        payload = json.loads((output / "LINEAGE_RUN_RECEIPT.json").read_text())
        payload["queries"][0]["webenv"] = "forged-history"
        (output / "LINEAGE_RUN_RECEIPT.json").write_text(json.dumps(payload), encoding="utf-8")
        self.assertIn(
            "PubMed lineage esearch mismatch",
            "\n".join(search.validate_lineage(self.root, output)),
        )
        payload["queries"][0]["webenv"] = "LINEAGE-ENV"
        payload["queries"][1]["query_key"] = "forbidden"
        (output / "LINEAGE_RUN_RECEIPT.json").write_text(json.dumps(payload), encoding="utf-8")
        self.assertIn(
            "crossref receipt contains pubmed field",
            "\n".join(search.validate_lineage(self.root, output)),
        )

    def test_crossref_lineage_receipt_recomputes_raw_counts(self):
        run_dir = self.make_valid_lineage_run(self.root)
        receipt_path = run_dir / "LINEAGE_RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["queries"][0].update(
            reported_count=99,
            total_results=99,
            returned_candidate_count=0,
        )
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "Crossref lineage raw count mismatch",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_lineage_preserves_completed_query_before_later_failure(self):
        self.copy_configuration()
        output = self.root / "partial/wave_03_lineage_resolution"
        registry = output / "LINEAGE_QUERY_REGISTRY.csv"
        self.write_csv(
            registry,
            list(search.LINEAGE_REGISTRY_HEADERS),
            self.lineage_registry_rows(),
        )
        calls: list[str] = []

        def first_opener(request, timeout=0):
            del timeout
            path = urllib.parse.urlparse(request.full_url).path
            calls.append(path)
            if path.endswith("esearch.fcgi"):
                return self.fake_response(
                    json.dumps(
                        {"esearchresult": {"count": "1", "webenv": "KEEP", "querykey": "1"}}
                    ).encode()
                )
            if path.endswith("efetch.fcgi"):
                return self.fake_response(
                    self.pubmed_xml([{"pmid": "11", "title": "Kept PubMed query"}])
                )
            raise urllib.error.HTTPError(request.full_url, 503, "later failure", {}, None)

        with mock.patch("time.sleep"):
            with self.assertRaisesRegex(search.DiscoveryExecutionError, "network request failed"):
                search.execute_lineage(
                    self.root,
                    registry,
                    output,
                    "test@example.invalid",
                    opener=first_opener,
                )
        partial = json.loads((output / "LINEAGE_RUN_RECEIPT.json").read_text())
        self.assertEqual(len(partial["queries"]), 1)
        self.assertEqual(partial["queries"][0]["webenv"], "KEEP")

        rerun_calls: list[str] = []

        def second_opener(request, timeout=0):
            del timeout
            path = urllib.parse.urlparse(request.full_url).path
            rerun_calls.append(path)
            self.assertTrue(path.endswith("/works"))
            return self.fake_response(
                json.dumps(
                    {
                        "status": "ok",
                        "message": {"total-results": 0, "items": []},
                    }
                ).encode()
            )

        completed = search.execute_lineage(
            self.root,
            registry,
            output,
            "test@example.invalid",
            opener=second_opener,
        )
        self.assertEqual(len(completed["queries"]), 2)
        self.assertEqual(len(rerun_calls), 1)

    def test_overbroad_pubmed_lineage_query_stops_before_efetch(self):
        self.copy_configuration()
        output = self.root / "phase/wave_03_lineage_resolution"
        registry = output / "LINEAGE_QUERY_REGISTRY.csv"
        self.write_csv(
            registry,
            list(search.LINEAGE_REGISTRY_HEADERS),
            [self.lineage_registry_rows()[0]],
        )
        calls: list[str] = []

        def opener(request, timeout=0):
            del timeout
            parsed = urllib.parse.urlparse(request.full_url)
            calls.append(parsed.path)
            self.assertTrue(parsed.path.endswith("esearch.fcgi"))
            return self.fake_response(
                json.dumps(
                    {"esearchresult": {"count": "10000", "webenv": "OVERBROAD", "querykey": "1"}}
                ).encode()
            )

        with self.assertRaisesRegex(
            search.DiscoveryExecutionError, "overbroad lineage identity query"
        ):
            search.execute_lineage(
                self.root, registry, output, "test@example.invalid", opener=opener
            )
        self.assertEqual(len(calls), 1)
        self.assertEqual(list((output / "raw").glob("*.xml")), [])
        self.assertEqual(len(list((output / "raw").glob("*.esearch.json"))), 1)

    def test_lineage_candidate_tables_are_required_and_manifest_locked(self):
        run_dir = self.make_valid_lineage_run(self.root)
        candidate_table = run_dir / "crossref_candidates.csv"
        candidate_table.write_bytes(candidate_table.read_bytes() + b"tampered")
        self.assertIn(
            "checksum mismatch",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )
        candidate_table.unlink()
        self.assertIn(
            "lineage candidate table missing",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_lineage_candidate_table_must_recompute_from_raw_response(self):
        run_dir = self.make_valid_lineage_run(self.root)
        candidate_path = run_dir / "crossref_candidates.csv"
        with candidate_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["title"] = "Fabricated title not present in the raw response"
        self.write_csv(
            candidate_path, list(search.CROSSREF_LINEAGE_HEADERS), rows
        )
        manifest_path = run_dir / "MANIFEST_SHA256.json"
        manifest = json.loads(manifest_path.read_text())
        next(
            item for item in manifest["files"]
            if item["path"] == "crossref_candidates.csv"
        )["sha256"] = self.sha(candidate_path)
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertIn(
            "lineage candidate table content mismatch",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_lineage_rejects_reused_query_and_unclosed_resolved_key_conflict(self):
        run_dir = self.make_valid_lineage_run(self.root)
        audit_path = run_dir / "lineage_identity_audit.csv"
        with audit_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        query_id = rows[0]["supporting_query_ids"]
        rows[0]["supporting_query_ids"] = f"{query_id}|{query_id}"
        self.write_csv(audit_path, list(search.LINEAGE_AUDIT_HEADERS), rows)
        self.assertIn(
            "lineage supporting query coverage mismatch",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

        run_dir = self.make_valid_lineage_run(self.root / "key-conflict")
        candidates_path = run_dir / "crossref_candidates.csv"
        with candidates_path.open(encoding="utf-8", newline="") as handle:
            candidates = list(csv.DictReader(handle))
        second = dict(candidates[0])
        second.update(
            candidate_key="DOI:10.1234/second",
            doi="10.1234/second",
            title="Second plausible candidate",
            url="https://doi.org/10.1234/second",
        )
        self.write_csv(
            candidates_path,
            list(search.CROSSREF_LINEAGE_HEADERS),
            [*candidates, second],
        )
        manifest_path = run_dir / "MANIFEST_SHA256.json"
        manifest = json.loads(manifest_path.read_text())
        next(
            item for item in manifest["files"]
            if item["path"] == "crossref_candidates.csv"
        )["sha256"] = self.sha(candidates_path)
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        audit_path = run_dir / "lineage_identity_audit.csv"
        with audit_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["candidate_keys_considered"] = (
            "DOI:10.1234/example|DOI:10.1234/second"
        )
        rows[0]["audit_selected_candidate_key"] = "DOI:10.1234/second"
        self.write_csv(audit_path, list(search.LINEAGE_AUDIT_HEADERS), rows)
        self.assertIn(
            "lineage conflict mismatch",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_execution_cli_runs_all_pubmed_cells_and_compile_action(self):
        self.copy_configuration()
        output = self.root / "cli-run"
        calls: list[str] = []

        def opener(request, timeout=0):
            del timeout
            calls.append(urllib.parse.urlparse(request.full_url).path)
            return self.fake_response(
                json.dumps(
                    {"esearchresult": {"count": "0", "webenv": "EMPTY", "querykey": "1"}}
                ).encode()
            )

        stdout = io.StringIO()
        with mock.patch.object(search.urllib.request, "urlopen", side_effect=opener):
            with mock.patch("time.sleep") as sleep:
                with contextlib.redirect_stdout(stdout):
                    result = search.main(
                        [
                            "run", "--root", str(self.root), "--date", "2026-07-20",
                            "--email", "test@example.invalid", "--api-key", "runtime-only",
                            "--output", str(output),
                        ]
                    )
        self.assertEqual(result, 0)
        self.assertEqual(stdout.getvalue().strip(), "DISCOVERY PASS")
        self.assertEqual(len(calls), 12)
        self.assertEqual(sleep.call_count, 11)
        self.assertTrue(all(call.args == (0.11,) for call in sleep.call_args_list))
        receipt = json.loads((output / "RUN_RECEIPT.json").read_text())
        self.assertEqual(len(receipt["cells"]), 12)
        self.assertNotIn("runtime-only", json.dumps(receipt))

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = search.main(["compile", "--run-dir", str(output)])
        self.assertEqual(result, 0)
        self.assertEqual(stdout.getvalue().strip(), "DISCOVERY PASS")

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

    def test_configuration_rejects_malformed_family_without_cli_traceback(self):
        self.copy_configuration()
        path = self.root / search.QUERY_CONFIG_PATH
        config = json.loads(path.read_text())
        del config["families"][0]["method_block"]
        path.write_text(json.dumps(config), encoding="utf-8")
        self.assertIn(
            "malformed family configuration",
            "\n".join(search.validate_configuration(self.root)),
        )
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                result = search.main(
                    ["list-cells", "--root", str(self.root), "--date", "2026-07-20"]
                )
        except Exception as error:
            self.fail(f"list-cells raised {type(error).__name__}: {error}")
        self.assertEqual(result, 1)
        self.assertIn("DISCOVERY FAIL", output.getvalue())

    def test_configuration_requires_top_level_fields_and_list_cells_is_stable(self):
        self.copy_configuration()
        path = self.root / search.QUERY_CONFIG_PATH
        config = json.loads(path.read_text())
        del config["applied_date_start"]
        path.write_text(json.dumps(config), encoding="utf-8")
        self.assertIn(
            "missing discovery configuration field: applied_date_start",
            "\n".join(search.validate_configuration(self.root)),
        )
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                result = search.main(
                    ["list-cells", "--root", str(self.root), "--date", "2026-07-20"]
                )
        except Exception as error:
            self.fail(f"list-cells raised {type(error).__name__}: {error}")
        self.assertEqual(result, 1)
        self.assertIn("DISCOVERY FAIL", output.getvalue())

    def test_list_cells_contains_unexpected_builder_errors(self):
        self.copy_configuration()
        output = io.StringIO()
        with mock.patch.object(
            search,
            "build_search_cells",
            side_effect=RuntimeError("simulated builder failure"),
        ):
            try:
                with contextlib.redirect_stdout(output):
                    result = search.main(
                        ["list-cells", "--root", str(self.root), "--date", "2026-07-20"]
                    )
            except Exception as error:
                self.fail(f"list-cells raised {type(error).__name__}: {error}")
        self.assertEqual(result, 1)
        self.assertIn("unable to build search cells: RuntimeError", output.getvalue())

    def test_journal_tokens_must_be_unique_and_nonblank(self):
        self.copy_configuration()
        path = self.root / search.JOURNAL_REGISTRY_PATH
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[1]["pubmed_token"] = rows[0]["pubmed_token"]
        self.write_journals(rows)
        self.assertIn("duplicate pubmed_token", "\n".join(search.validate_configuration(self.root)))

    def test_journal_registry_requires_the_approved_active_coverage(self):
        self.copy_configuration()
        self.write_journals([])
        rendered = "\n".join(search.validate_configuration(self.root))
        self.assertIn("journal registry must contain exactly 22 active rows", rendered)
        with self.assertRaisesRegex(ValueError, "active journal registry is empty"):
            search.build_search_cells(self.root, date(2026, 7, 20))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = search.main(
                ["list-cells", "--root", str(self.root), "--date", "2026-07-20"]
            )
        self.assertEqual(result, 1)
        self.assertIn("DISCOVERY FAIL", output.getvalue())
        self.assertNotIn("()", output.getvalue())

    def test_journal_registry_rejects_duplicate_ids_and_unapproved_titles(self):
        self.copy_configuration()
        path = self.root / search.JOURNAL_REGISTRY_PATH
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[1]["journal_id"] = rows[0]["journal_id"]
        rows[2]["title"] = "Unapproved Journal"
        self.write_journals(rows)
        rendered = "\n".join(search.validate_configuration(self.root))
        self.assertIn("duplicate journal_id", rendered)
        self.assertIn("approved journal title set mismatch", rendered)

    def test_configuration_csv_rejects_short_rows_without_traceback(self):
        self.copy_configuration()
        self.shorten_first_csv_row(self.root / search.JOURNAL_REGISTRY_PATH)
        self.assertIn(
            "CSV row width mismatch",
            "\n".join(search.validate_configuration(self.root)),
        )

    def test_screening_csv_rejects_short_rows_without_traceback(self):
        run_dir = self.make_valid_screened_run(self.root / "screening-width")
        self.shorten_first_csv_row(run_dir / "screened_candidates.csv")
        self.assertIn(
            "CSV row width mismatch",
            "\n".join(search.validate_screening(run_dir)),
        )

    def test_audit_csv_rejects_extra_fields_without_traceback(self):
        run_dir = self.make_valid_screened_run(self.root / "audit-width")
        self.extend_first_csv_row(run_dir / "screening_audit.csv")
        self.assertIn(
            "CSV row width mismatch",
            "\n".join(search.validate_screening_audit(run_dir)),
        )

    def test_lineage_csv_rejects_short_rows_without_traceback(self):
        run_dir = self.make_valid_lineage_run(self.root / "lineage-width")
        self.shorten_first_csv_row(run_dir / "lineage_identity_audit.csv")
        try:
            rendered = "\n".join(search.validate_lineage(self.root, run_dir))
        except Exception as error:
            self.fail(f"validate_lineage raised {type(error).__name__}: {error}")
        self.assertIn("CSV row width mismatch", rendered)

    def test_search_run_rejects_sha_mismatch(self):
        run_dir = self.make_valid_run()
        raw = next((run_dir / "raw").glob("*.xml"))
        raw.write_bytes(raw.read_bytes() + b"altered")
        self.assertIn("checksum mismatch", "\n".join(search.validate_search_run(run_dir)))

    def test_search_run_recomputes_esearch_count_and_history(self):
        run_dir = self.make_valid_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        cell = receipt["cells"][0]
        esearch_path = run_dir / cell["esearch_path"]
        esearch_path.write_text(
            json.dumps(
                {
                    "esearchresult": {
                        "count": "2",
                        "webenv": "different-history",
                        "querykey": "9",
                    }
                }
            ),
            encoding="utf-8",
        )
        changed_sha = self.sha(esearch_path)
        cell["esearch_sha256"] = changed_sha
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        manifest_path = run_dir / "MANIFEST_SHA256.json"
        manifest = json.loads(manifest_path.read_text())
        next(
            item for item in manifest["files"]
            if item["path"] == cell["esearch_path"]
        )["sha256"] = changed_sha
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        rendered = "\n".join(search.validate_search_run(run_dir))
        self.assertIn("esearch reported count mismatch", rendered)
        self.assertIn("esearch history mismatch", rendered)

    def test_manifest_rejects_a_symlinked_parent_outside_the_run(self):
        run_dir = self.make_valid_run()
        outside_raw = self.root / "outside-raw"
        (run_dir / "raw").rename(outside_raw)
        (run_dir / "raw").symlink_to(outside_raw, target_is_directory=True)
        self.assertIn(
            "manifest path contains symlink",
            "\n".join(search.validate_search_run(run_dir)),
        )

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

    def test_configuration_receipts_are_confined_without_following_parent_symlinks(self):
        run_dir = self.make_valid_run()
        self.assertEqual(search.validate_search_run(run_dir), [])

        outside_configuration = self.root.parent / "outside-configuration"
        (self.root / "01_search").rename(outside_configuration)
        (self.root / "01_search").symlink_to(
            outside_configuration,
            target_is_directory=True,
        )
        self.assertIn(
            "configuration path contains symlink",
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
            "sha256": self.sha(
                phase_dir
                / "wave_03_lineage_resolution/LINEAGE_QUERY_REGISTRY.csv"
            ),
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

    def test_raw_artifact_cannot_cross_esearch_and_page_roles(self):
        run_dir = self.make_valid_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        page = receipt["cells"][0]["efetch_pages"][0]
        receipt["cells"][0]["esearch_path"] = page["path"]
        receipt["cells"][0]["esearch_sha256"] = page["sha256"]
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "duplicate raw artifact path",
            "\n".join(search.validate_search_run(run_dir)),
        )

    def test_search_cells_use_the_top_level_source_contract(self):
        run_dir = self.make_valid_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["cells"][0].pop("source", None)
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertEqual(search.validate_search_run(run_dir), [])

        receipt["cells"][0]["source"] = "crossref"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertIn(
            "cell source mismatch",
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

    def test_split_children_inherit_semantic_core_and_valid_dates(self):
        run_dir = self.make_valid_split_run()
        receipt_path = run_dir / "RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        child = receipt["cells"][0]["children"][1]
        child.update(
            lane="VENUE",
            family="spatial_transmission",
            source="crossref",
            query="different method core",
            date_start="2021/01/01",
            date_end="2020/12/31",
        )
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        rendered = "\n".join(search.validate_search_run(run_dir))
        self.assertIn("cell date range inverted", rendered)
        self.assertIn("child lane mismatch", rendered)
        self.assertIn("child family mismatch", rendered)
        self.assertIn("cell source mismatch", rendered)
        self.assertIn("child query semantic core mismatch", rendered)
        self.assertIn("child query date interval mismatch", rendered)

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

    def test_lineage_rejects_empty_query_and_decision_coverage(self):
        run_dir = self.make_valid_lineage_run(self.root)
        receipt_path = run_dir / "LINEAGE_RUN_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["queries"] = []
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        rendered = "\n".join(search.validate_lineage(self.root, run_dir))
        self.assertIn("lineage query coverage missing", rendered)

    def test_lineage_requires_identity_audit_and_query_registry_coverage(self):
        run_dir = self.make_valid_lineage_run(self.root)
        (run_dir / "lineage_identity_audit.csv").unlink()
        self.assertIn(
            "lineage identity audit missing",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_lineage_rejects_same_reviewer_and_borrowed_candidate(self):
        run_dir = self.make_valid_lineage_run(self.root)
        path = run_dir / "lineage_identity_audit.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["audit_reviewer"] = rows[0]["primary_reviewer"]
        rows[0]["candidate_keys_considered"] = "DOI:10.9999/borrowed"
        rows[0]["primary_selected_candidate_key"] = "DOI:10.9999/borrowed"
        rows[0]["audit_selected_candidate_key"] = "DOI:10.9999/borrowed"
        rows[0]["final_selected_candidate_key"] = "DOI:10.9999/borrowed"
        self.write_csv(path, list(rows[0]), rows)
        rendered = "\n".join(search.validate_lineage(self.root, run_dir))
        self.assertIn("lineage audit reviewer is not independent", rendered)
        self.assertIn("lineage candidate provenance mismatch", rendered)

    def test_lineage_ledger_must_match_final_decision(self):
        run_dir = self.make_valid_lineage_run(self.root)
        path = run_dir.parent / "global/lineage_ledger.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["final_candidate_key"] = "DOI:10.9999/wrong"
        self.write_csv(path, list(rows[0]), rows)
        self.assertIn(
            "lineage ledger final key mismatch",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

    def test_unresolved_lineage_ledger_cannot_retain_resolved_identity_fields(self):
        run_dir = self.make_valid_lineage_run(self.root)
        audit_path = run_dir / "lineage_identity_audit.csv"
        with audit_path.open(encoding="utf-8", newline="") as handle:
            audit_rows = list(csv.DictReader(handle))
        audit_rows[0].update(
            primary_selected_candidate_key="",
            primary_decision="rejected",
            primary_reason="The candidate does not resolve the named source.",
            audit_selected_candidate_key="",
            audit_decision="rejected",
            audit_reason="Independent review rejects the candidate identity.",
            final_selected_candidate_key="",
            final_decision="rejected",
            final_reason="Independent review rejects the candidate identity.",
            inspected_primary_url="",
        )
        self.write_csv(audit_path, list(search.LINEAGE_AUDIT_HEADERS), audit_rows)

        ledger_path = run_dir.parent / "global/lineage_ledger.csv"
        with ledger_path.open(encoding="utf-8", newline="") as handle:
            ledger_rows = list(csv.DictReader(handle))
        ledger_rows[0].update(final_candidate_key="", status="rejected")
        self.write_csv(ledger_path, list(search.LINEAGE_LEDGER_HEADERS), ledger_rows)
        self.assertIn(
            "unresolved lineage ledger identity fields populated",
            "\n".join(search.validate_lineage(self.root, run_dir)),
        )

        for field in ("title", "year", "doi", "pmid", "primary_url"):
            ledger_rows[0][field] = ""
        self.write_csv(ledger_path, list(search.LINEAGE_LEDGER_HEADERS), ledger_rows)
        self.assertEqual(search.validate_lineage(self.root, run_dir), [])

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

    def test_screened_audit_status_has_bidirectional_row_coverage(self):
        run_dir = self.make_valid_screened_run()
        self.delete_one_required_audit_row(run_dir)
        self.assertIn(
            "missing audit row for screened status",
            "\n".join(search.validate_screening(run_dir)),
        )

    def test_not_selected_screening_rejects_an_audit_row(self):
        run_dir = self.make_valid_screened_run()
        path = run_dir / "screened_candidates.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["audit_status"] = "not_selected"
        self.write_csv(path, list(search.SCREENED_HEADERS), rows)
        self.assertIn(
            "unexpected audit row for not_selected",
            "\n".join(search.validate_screening(run_dir)),
        )

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

    def test_verify_all_requires_global_reconciliation_and_repository_validation(self):
        phase_dir = self.make_valid_phase_run()
        reconciliation = phase_dir / "global/GLOBAL_KEY_RECONCILIATION.txt"
        reconciliation.unlink()
        self.assertIn("global reconciliation missing", "\n".join(search.validate_all(self.root, phase_dir)))
        reconciliation.write_text(
            "ALL WAVE, SCREENING, REGISTRY, AND LINEAGE KEYS RECONCILE\n",
            encoding="utf-8",
        )
        (self.root / "README.md").unlink()
        self.assertIn("repository: required file missing: README.md", "\n".join(search.validate_all(self.root, phase_dir)))

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
