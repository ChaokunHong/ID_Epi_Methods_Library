from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Mapping, Sequence


SEED_PATH = Path(
    "01_search/seed_scans/"
    "INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md"
)
SEED_SHA256 = "520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55"
SEED_MANIFEST_PATH = Path("01_search/seed_scans/MANIFEST_SHA256.json")

VERIFICATION_STATES = frozenset({"discovery", "verified", "extracted", "retired"})
FAMILIES = frozenset(
    {
        "causal_policy",
        "surveillance_measurement",
        "spatial_transmission",
        "forecasting_dynamics",
        "evidence_synthesis",
        "simulation_methods",
    }
)


@dataclass(frozen=True)
class RegistrySpec:
    path: str
    headers: tuple[str, ...]
    id_column: str | None
    id_pattern: str | None
    enums: Mapping[str, frozenset[str]]


REGISTRY_SPECS = (
    RegistrySpec(
        "03_evidence_tables/papers.csv",
        (
            "paper_id",
            "title",
            "year",
            "record_type",
            "verification_state",
            "doi",
            "url",
            "card_path",
            "notes",
        ),
        "paper_id",
        r"^P-\d{4}-\d{4}$",
        {
            "record_type": frozenset(
                {
                    "method_source",
                    "applied_seed",
                    "diagnostic",
                    "correction",
                    "guidance",
                    "reproducibility",
                }
            ),
            "verification_state": VERIFICATION_STATES,
        },
    ),
    RegistrySpec(
        "03_evidence_tables/methods.csv",
        (
            "method_id",
            "canonical_name",
            "family",
            "verification_state",
            "card_path",
            "notes",
        ),
        "method_id",
        r"^M-(CAUSAL|SURVEILLANCE|SPATIAL|FORECASTING|EVIDENCE|SIMULATION)-\d{3}$",
        {"family": FAMILIES, "verification_state": VERIFICATION_STATES},
    ),
    RegistrySpec(
        "03_evidence_tables/paper_method_links.csv",
        ("paper_id", "method_id", "relationship", "notes"),
        None,
        None,
        {
            "relationship": frozenset(
                {"originates", "applies", "critiques", "corrects", "diagnoses", "implements"}
            )
        },
    ),
    RegistrySpec(
        "04_translation_candidates/translation_candidates.csv",
        (
            "candidate_id",
            "title",
            "domain",
            "portfolio_category",
            "verification_state",
            "card_path",
            "notes",
        ),
        "candidate_id",
        r"^T-(AMR|ID|CROSS)-\d{3}$",
        {
            "domain": frozenset({"amr", "infectious_disease", "cross_domain"}),
            "portfolio_category": frozenset(
                {
                    "unranked",
                    "flagship",
                    "lower_risk_public_data",
                    "infrastructure_prospective",
                    "collaboration_dependent",
                    "no_go",
                }
            ),
            "verification_state": VERIFICATION_STATES,
        },
    ),
    RegistrySpec(
        "05_data_registry/datasets.csv",
        (
            "dataset_id",
            "name",
            "owner",
            "access_state",
            "verification_state",
            "official_url",
            "card_path",
            "notes",
        ),
        "dataset_id",
        r"^D-[A-Z][A-Z0-9_]*-\d{3}$",
        {
            "access_state": frozenset(
                {
                    "unknown",
                    "public_verified",
                    "registration_required",
                    "application_required",
                    "restricted",
                    "unavailable",
                }
            ),
            "verification_state": VERIFICATION_STATES,
        },
    ),
    RegistrySpec(
        "06_simulation_lab/simulations.csv",
        ("simulation_id", "title", "family", "verification_state", "card_path", "notes"),
        "simulation_id",
        r"^S-(CAUSAL|SURVEILLANCE|SPATIAL|FORECASTING|EVIDENCE|SIMULATION)-\d{3}$",
        {"family": FAMILIES, "verification_state": VERIFICATION_STATES},
    ),
)

REGISTRY_BY_PATH = {spec.path: spec for spec in REGISTRY_SPECS}

REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "HANDOFF.md",
    "00_governance/PROJECT_CHARTER.md",
    "00_governance/SCOPE_AND_ELIGIBILITY.md",
    "00_governance/DECISION_LOG.md",
    "00_governance/WORKFLOW.md",
    "00_governance/REGISTRY_SCHEMA.md",
    "00_governance/RESUME_PROMPT.md",
    "01_search/SEARCH_LOG_TEMPLATE.md",
    "01_search/seed_scans/SEED_SCAN_PROVENANCE.md",
    "01_search/seed_scans/MANIFEST_SHA256.json",
    "02_method_library/METHOD_CARD_TEMPLATE.md",
    "04_translation_candidates/TRANSLATION_CARD_TEMPLATE.md",
    "05_data_registry/DATASET_CARD_TEMPLATE.md",
    "06_simulation_lab/SIMULATION_CARD_TEMPLATE.md",
    "07_reviews/REVIEW_TEMPLATE.md",
    "docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md",
    "docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md",
)


def _read_rows(path: Path) -> tuple[list[str] | None, list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames, list(reader)


def validate_csv(root: Path, spec: RegistrySpec) -> list[str]:
    errors: list[str] = []
    path = root / spec.path
    if not path.is_file():
        return [f"required registry missing: {spec.path}"]

    headers, rows = _read_rows(path)
    if headers != list(spec.headers):
        errors.append(
            f"{spec.path}: header mismatch; expected {list(spec.headers)!r}, got {headers!r}"
        )
        return errors

    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        if spec.id_column is not None and spec.id_pattern is not None:
            identifier = (row.get(spec.id_column) or "").strip()
            if re.fullmatch(spec.id_pattern, identifier) is None:
                errors.append(
                    f"{spec.path}:{line_number}: invalid ID in {spec.id_column}: {identifier!r}"
                )
            elif identifier in seen:
                errors.append(
                    f"{spec.path}:{line_number}: duplicate ID in {spec.id_column}: {identifier}"
                )
            else:
                seen.add(identifier)

        for column, allowed in spec.enums.items():
            value = (row.get(column) or "").strip()
            if value and value not in allowed:
                errors.append(
                    f"{spec.path}:{line_number}: invalid value for {column}: {value!r}"
                )

        if "card_path" in spec.headers:
            raw_card_path = (row.get("card_path") or "").strip()
            if not raw_card_path:
                errors.append(f"{spec.path}:{line_number}: card_path is required")
            else:
                card_path = (root / raw_card_path).resolve()
                try:
                    card_path.relative_to(root.resolve())
                except ValueError:
                    errors.append(
                        f"{spec.path}:{line_number}: card_path escapes repository: {raw_card_path}"
                    )
                else:
                    if not card_path.is_file():
                        errors.append(
                            f"{spec.path}:{line_number}: card_path does not exist: {raw_card_path}"
                        )
    return errors


def _registry_ids(root: Path, relative_path: str, id_column: str) -> set[str]:
    path = root / relative_path
    if not path.is_file():
        return set()
    _, rows = _read_rows(path)
    return {(row.get(id_column) or "").strip() for row in rows}


def validate_foreign_keys(root: Path) -> list[str]:
    errors: list[str] = []
    links_path = root / "03_evidence_tables/paper_method_links.csv"
    if not links_path.is_file():
        return errors

    paper_ids = _registry_ids(root, "03_evidence_tables/papers.csv", "paper_id")
    method_ids = _registry_ids(root, "03_evidence_tables/methods.csv", "method_id")
    _, rows = _read_rows(links_path)
    for line_number, row in enumerate(rows, start=2):
        paper_id = (row.get("paper_id") or "").strip()
        method_id = (row.get("method_id") or "").strip()
        if paper_id not in paper_ids:
            errors.append(
                f"03_evidence_tables/paper_method_links.csv:{line_number}: "
                f"unknown paper_id: {paper_id}"
            )
        if method_id not in method_ids:
            errors.append(
                f"03_evidence_tables/paper_method_links.csv:{line_number}: "
                f"unknown method_id: {method_id}"
            )
    return errors


def validate_seed_checksum(root: Path) -> list[str]:
    path = root / SEED_PATH
    if not path.is_file():
        return [f"required seed file missing: {SEED_PATH}"]
    errors: list[str] = []
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != SEED_SHA256:
        errors.append(
            f"seed checksum mismatch: expected {SEED_SHA256}, got {digest}: {SEED_PATH}"
        )
    manifest_path = root / SEED_MANIFEST_PATH
    if not manifest_path.is_file():
        errors.append(f"required seed manifest missing: {SEED_MANIFEST_PATH}")
        return errors
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"invalid seed manifest: {error}")
        return errors
    expected_entry = {"path": str(SEED_PATH), "sha256": SEED_SHA256}
    if manifest.get("algorithm") != "SHA256" or manifest.get("files") != [expected_entry]:
        errors.append("seed manifest mismatch")
    return errors


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors = [
        f"required file missing: {relative_path}"
        for relative_path in REQUIRED_PATHS
        if not (root / relative_path).is_file()
    ]
    for spec in REGISTRY_SPECS:
        errors.extend(validate_csv(root, spec))
    errors.extend(validate_foreign_keys(root))
    errors.extend(validate_seed_checksum(root))
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the methods library")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    errors = validate_repository(args.root)
    if errors:
        print("VALIDATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
