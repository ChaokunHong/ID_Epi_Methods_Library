from __future__ import annotations

import csv
import importlib.util
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


if __name__ == "__main__":
    unittest.main()
