from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "validate_library.py"
SPEC = importlib.util.spec_from_file_location("validate_library", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_registry(self, spec, rows: list[dict[str, str]]) -> None:
        path = self.root / spec.path
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=spec.headers)
            writer.writeheader()
            writer.writerows(rows)

    def write_csv(
        self,
        relative_path: str,
        headers: tuple[str, ...],
        rows: list[list[str]],
    ) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(headers)
            writer.writerows(rows)

    def write_all_registry_headers(self) -> None:
        for registry_spec in validator.REGISTRY_SPECS:
            self.write_registry(registry_spec, [])
        for relative_path, headers in (
            (
                "03_evidence_tables/candidate_method_links.csv",
                ("candidate_id", "method_id", "notes"),
            ),
            (
                "03_evidence_tables/candidate_dataset_links.csv",
                ("candidate_id", "dataset_id", "notes"),
            ),
            (
                "03_evidence_tables/simulation_method_links.csv",
                ("simulation_id", "method_id", "notes"),
            ),
            (
                "03_evidence_tables/simulation_candidate_links.csv",
                ("simulation_id", "candidate_id", "notes"),
            ),
        ):
            self.write_csv(relative_path, headers, [])

    def blank_row(self, spec) -> dict[str, str]:
        return {column: "" for column in spec.headers}

    def make_card(self, relative_path: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Test card\n", encoding="utf-8")

    def test_empty_header_only_registries_pass(self):
        errors: list[str] = []
        for registry_spec in validator.REGISTRY_SPECS:
            self.write_registry(registry_spec, [])
            errors.extend(validator.validate_csv(self.root, registry_spec))
        errors.extend(validator.validate_foreign_keys(self.root))
        self.assertEqual(errors, [])

    def test_bad_identifier_fails(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/papers.csv"]
        row = self.blank_row(spec)
        row.update(
            paper_id="paper-1",
            title="Example",
            year="2020",
            record_type="applied_seed",
            verification_state="discovery",
            card_path="cards/paper.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn("invalid ID", "\n".join(validator.validate_csv(self.root, spec)))

    def test_duplicate_identifier_fails(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/methods.csv"]
        row = self.blank_row(spec)
        row.update(
            method_id="M-CAUSAL-001",
            canonical_name="Example",
            family="causal_policy",
            verification_state="discovery",
            card_path="cards/method.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row, row])
        self.assertIn("duplicate ID", "\n".join(validator.validate_csv(self.root, spec)))

    def test_invalid_enum_fails(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/papers.csv"]
        row = self.blank_row(spec)
        row.update(
            paper_id="P-2020-0001",
            title="Example",
            year="2020",
            record_type="prestigious",
            verification_state="discovery",
            card_path="cards/paper.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn("invalid value", "\n".join(validator.validate_csv(self.root, spec)))

    def test_missing_method_foreign_key_fails(self):
        papers = validator.REGISTRY_BY_PATH["03_evidence_tables/papers.csv"]
        methods = validator.REGISTRY_BY_PATH["03_evidence_tables/methods.csv"]
        links = validator.REGISTRY_BY_PATH["03_evidence_tables/paper_method_links.csv"]
        self.write_registry(papers, [])
        self.write_registry(methods, [])
        row = self.blank_row(links)
        row.update(
            paper_id="P-2020-0001",
            method_id="M-CAUSAL-001",
            relationship="applies",
        )
        self.write_registry(links, [row])
        self.assertIn(
            "unknown method_id",
            "\n".join(validator.validate_foreign_keys(self.root)),
        )

    def test_missing_card_path_fails_for_nonempty_value(self):
        spec = validator.REGISTRY_BY_PATH["05_data_registry/datasets.csv"]
        row = self.blank_row(spec)
        row.update(
            dataset_id="D-WHO-001",
            name="Example",
            owner="WHO",
            access_state="unknown",
            verification_state="discovery",
            card_path="05_data_registry/cards/missing.md",
        )
        self.write_registry(spec, [row])
        self.assertIn(
            "card_path does not exist",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_seed_checksum_mismatch_fails(self):
        seed = self.root / validator.SEED_PATH
        seed.parent.mkdir(parents=True, exist_ok=True)
        seed.write_text("altered\n", encoding="utf-8")
        self.assertIn(
            "seed checksum mismatch",
            "\n".join(validator.validate_seed_checksum(self.root)),
        )

    def test_non_object_seed_manifests_return_error_without_exception(self):
        seed = self.root / validator.SEED_PATH
        seed.parent.mkdir(parents=True, exist_ok=True)
        seed.write_text("altered\n", encoding="utf-8")
        manifest = self.root / validator.SEED_MANIFEST_PATH
        for payload in ([], None, "text", 7):
            with self.subTest(payload=payload):
                manifest.write_text(json.dumps(payload), encoding="utf-8")
                try:
                    errors = validator.validate_seed_checksum(self.root)
                except Exception as error:  # pragma: no cover - desired contract forbids this
                    self.fail(f"non-object manifest raised {type(error).__name__}: {error}")
                self.assertIn("invalid seed manifest", "\n".join(errors))

    def test_over_width_and_under_width_rows_fail(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/papers.csv"]
        self.make_card("cards/paper.md")
        valid_values = [
            "P-2020-0001",
            "Example",
            "2020",
            "applied_seed",
            "discovery",
            "",
            "",
            "cards/paper.md",
            "",
        ]
        for label, values in (
            ("over-width", valid_values + ["surplus"]),
            ("under-width", valid_values[:-1]),
        ):
            with self.subTest(label=label):
                self.write_csv(spec.path, spec.headers, [values])
                self.assertIn(
                    "row width mismatch",
                    "\n".join(validator.validate_csv(self.root, spec)),
                )

    def test_missing_required_field_fails(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/methods.csv"]
        row = self.blank_row(spec)
        row.update(
            method_id="M-CAUSAL-001",
            family="causal_policy",
            verification_state="discovery",
            card_path="cards/method.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn(
            "required field is blank: canonical_name",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_paper_year_must_match_identifier_year(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/papers.csv"]
        row = self.blank_row(spec)
        row.update(
            paper_id="P-2020-0001",
            title="Example",
            year="2021",
            record_type="applied_seed",
            verification_state="discovery",
            card_path="cards/paper.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn(
            "paper year does not match paper_id",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_method_family_must_match_identifier_prefix(self):
        spec = validator.REGISTRY_BY_PATH["03_evidence_tables/methods.csv"]
        row = self.blank_row(spec)
        row.update(
            method_id="M-CAUSAL-001",
            canonical_name="Example",
            family="spatial_transmission",
            verification_state="discovery",
            card_path="cards/method.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn(
            "family does not match method_id prefix",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_candidate_domain_must_match_identifier_prefix(self):
        spec = validator.REGISTRY_BY_PATH[
            "04_translation_candidates/translation_candidates.csv"
        ]
        row = self.blank_row(spec)
        row.update(
            candidate_id="T-AMR-001",
            title="Example",
            domain="cross_domain",
            portfolio_category="unranked",
            verification_state="discovery",
            card_path="cards/candidate.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn(
            "domain does not match candidate_id prefix",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_simulation_family_must_match_identifier_prefix(self):
        spec = validator.REGISTRY_BY_PATH["06_simulation_lab/simulations.csv"]
        row = self.blank_row(spec)
        row.update(
            simulation_id="S-SIMULATION-001",
            title="Example",
            family="causal_policy",
            verification_state="discovery",
            card_path="cards/simulation.md",
        )
        self.make_card(row["card_path"])
        self.write_registry(spec, [row])
        self.assertIn(
            "family does not match simulation_id prefix",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_duplicate_composite_link_fails(self):
        spec = validator.REGISTRY_BY_PATH[
            "03_evidence_tables/paper_method_links.csv"
        ]
        row = self.blank_row(spec)
        row.update(
            paper_id="P-2020-0001",
            method_id="M-CAUSAL-001",
            relationship="applies",
        )
        self.write_registry(spec, [row, row])
        self.assertIn(
            "duplicate composite link",
            "\n".join(validator.validate_csv(self.root, spec)),
        )

    def test_each_new_link_type_reports_missing_foreign_key(self):
        cases = (
            (
                "03_evidence_tables/candidate_method_links.csv",
                ("candidate_id", "method_id", "notes"),
                ["T-AMR-001", "M-CAUSAL-001", ""],
                "unknown candidate_id",
            ),
            (
                "03_evidence_tables/candidate_dataset_links.csv",
                ("candidate_id", "dataset_id", "notes"),
                ["T-AMR-001", "D-WHO-001", ""],
                "unknown dataset_id",
            ),
            (
                "03_evidence_tables/simulation_method_links.csv",
                ("simulation_id", "method_id", "notes"),
                ["S-CAUSAL-001", "M-CAUSAL-001", ""],
                "unknown method_id",
            ),
            (
                "03_evidence_tables/simulation_candidate_links.csv",
                ("simulation_id", "candidate_id", "notes"),
                ["S-CAUSAL-001", "T-AMR-001", ""],
                "unknown candidate_id",
            ),
        )
        for relative_path, headers, values, expected in cases:
            with self.subTest(relative_path=relative_path):
                self.write_all_registry_headers()
                self.write_csv(relative_path, headers, [values])
                self.assertIn(
                    expected,
                    "\n".join(validator.validate_foreign_keys(self.root)),
                )

    def test_design_checksum_mismatch_fails(self):
        design = self.root / (
            "docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md"
        )
        design.parent.mkdir(parents=True, exist_ok=True)
        design.write_text("altered design\n", encoding="utf-8")
        self.assertIn(
            "design checksum mismatch",
            "\n".join(validator.validate_repository(self.root)),
        )

    def test_missing_taxonomy_readme_is_required(self):
        errors = validator.validate_repository(self.root)
        self.assertIn(
            "required file missing: 02_method_library/causal_policy/README.md",
            errors,
        )

    def test_valid_minimal_entity_and_link_rows_pass(self):
        cards = {
            "paper": "cards/paper.md",
            "method": "cards/method.md",
            "candidate": "cards/candidate.md",
            "dataset": "cards/dataset.md",
            "simulation": "cards/simulation.md",
        }
        for card_path in cards.values():
            self.make_card(card_path)

        rows_by_path = {
            "03_evidence_tables/papers.csv": [
                {
                    "paper_id": "P-2020-0001",
                    "title": "Example paper",
                    "year": "2020",
                    "record_type": "applied_seed",
                    "verification_state": "discovery",
                    "doi": "",
                    "url": "",
                    "card_path": cards["paper"],
                    "notes": "",
                }
            ],
            "03_evidence_tables/methods.csv": [
                {
                    "method_id": "M-CAUSAL-001",
                    "canonical_name": "Example method",
                    "family": "causal_policy",
                    "verification_state": "discovery",
                    "card_path": cards["method"],
                    "notes": "",
                }
            ],
            "03_evidence_tables/paper_method_links.csv": [
                {
                    "paper_id": "P-2020-0001",
                    "method_id": "M-CAUSAL-001",
                    "relationship": relationship,
                    "notes": "",
                }
                for relationship in ("applies", "implements")
            ],
            "04_translation_candidates/translation_candidates.csv": [
                {
                    "candidate_id": "T-AMR-001",
                    "title": "Example candidate",
                    "domain": "amr",
                    "portfolio_category": "unranked",
                    "verification_state": "discovery",
                    "card_path": cards["candidate"],
                    "notes": "",
                }
            ],
            "05_data_registry/datasets.csv": [
                {
                    "dataset_id": "D-WHO-001",
                    "name": "Example dataset",
                    "owner": "World Health Organization",
                    "access_state": "unknown",
                    "verification_state": "discovery",
                    "official_url": "",
                    "card_path": cards["dataset"],
                    "notes": "",
                }
            ],
            "06_simulation_lab/simulations.csv": [
                {
                    "simulation_id": "S-CAUSAL-001",
                    "title": "Example simulation",
                    "family": "causal_policy",
                    "verification_state": "discovery",
                    "card_path": cards["simulation"],
                    "notes": "",
                }
            ],
        }
        for registry_spec in validator.REGISTRY_SPECS:
            self.write_registry(
                registry_spec,
                rows_by_path.get(registry_spec.path, []),
            )

        self.write_csv(
            "03_evidence_tables/candidate_method_links.csv",
            ("candidate_id", "method_id", "notes"),
            [["T-AMR-001", "M-CAUSAL-001", ""]],
        )
        self.write_csv(
            "03_evidence_tables/candidate_dataset_links.csv",
            ("candidate_id", "dataset_id", "notes"),
            [["T-AMR-001", "D-WHO-001", ""]],
        )
        self.write_csv(
            "03_evidence_tables/simulation_method_links.csv",
            ("simulation_id", "method_id", "notes"),
            [["S-CAUSAL-001", "M-CAUSAL-001", ""]],
        )
        self.write_csv(
            "03_evidence_tables/simulation_candidate_links.csv",
            ("simulation_id", "candidate_id", "notes"),
            [["S-CAUSAL-001", "T-AMR-001", ""]],
        )

        errors: list[str] = []
        for registry_spec in validator.REGISTRY_SPECS:
            errors.extend(validator.validate_csv(self.root, registry_spec))
        errors.extend(validator.validate_foreign_keys(self.root))
        self.assertEqual(len(validator.REGISTRY_SPECS), 10)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
