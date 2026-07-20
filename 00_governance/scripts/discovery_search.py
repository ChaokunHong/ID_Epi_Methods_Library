from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
from typing import Iterable, Sequence
import xml.etree.ElementTree as ET


PROTOCOL_PATH = Path(
    "01_search/search_protocols/2026-07-20-broad-methods-discovery-protocol.md"
)
QUERY_CONFIG_PATH = Path("01_search/search_protocols/discovery_queries.json")
JOURNAL_REGISTRY_PATH = Path("01_search/journal_registry/journals.csv")
EXTERNAL_BOUNDARY_PATH = Path(
    "07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json"
)
EXTERNAL_POINTER_PATH = Path("ID_EPI_METHODS_LIBRARY_POINTER.md")
EXTERNAL_SEED_SOURCE_PATH = Path(
    "02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md"
)
EXTERNAL_PROOF_LIMIT = (
    "Path/status evidence only; no pre-phase byte manifest exists for paths already "
    "dirty at baseline."
)

JOURNAL_HEADERS = (
    "journal_id",
    "title",
    "group",
    "search_role",
    "pubmed_token",
    "official_url",
    "status",
    "notes",
)
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
JOURNAL_GROUPS = frozenset(
    {
        "general_medicine",
        "general_science",
        "infectious_disease",
        "global_health",
        "epidemiology",
        "npj",
    }
)
JOURNAL_SEARCH_ROLES = frozenset({"applied_seed", "method_source", "both"})
JOURNAL_STATUSES = frozenset({"active", "inactive"})
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
JOURNAL_ID_PATTERN = re.compile(r"^J-[A-Z]+-[0-9]{3}$")

RUN_REQUIRED_FIELDS = (
    "schema_version",
    "executed_at",
    "timezone",
    "tool_version",
    "source",
    "cells",
    "configuration_files",
)
CELL_REQUIRED_FIELDS = (
    "search_id",
    "lane",
    "family",
    "query",
    "date_start",
    "date_end",
    "reported_count",
    "parent_search_id",
    "cell_type",
    "esearch_path",
    "esearch_sha256",
    "status",
)
LEAF_REQUIRED_FIELDS = (
    "usehistory",
    "webenv",
    "query_key",
    "retrieved_count",
    "efetch_pages",
)
PAGE_REQUIRED_FIELDS = ("retstart", "retmax", "path", "sha256", "parsed_count")
LINEAGE_REQUIRED_FIELDS = (
    "schema_version",
    "executed_at",
    "timezone",
    "tool_version",
    "configuration_files",
    "queries",
)
LINEAGE_QUERY_FIELDS = (
    "query_id",
    "source",
    "query",
    "reported_count",
    "raw_path",
    "raw_sha256",
    "status",
)

COMPILED_HEADERS = (
    "candidate_key",
    "row_sha256",
    "pmid",
    "doi",
    "title",
    "year",
    "journal",
    "authors",
    "abstract",
    "publication_types",
    "search_ids",
    "lanes",
    "preliminary_families",
    "source_url",
    "deduplication_basis",
    "possible_duplicate_group",
)
PRIMARY_HEADERS = (
    "candidate_key",
    "source_row_sha256",
    "primary_decision",
    "primary_proposed_record_type",
    "primary_reason_code",
    "primary_reason",
    "primary_reviewer",
    "batch_id",
    "retained_candidate_key",
)
SCREENED_HEADERS = (
    "candidate_key",
    "source_row_sha256",
    "primary_decision",
    "primary_proposed_record_type",
    "primary_reason_code",
    "primary_reason",
    "final_decision",
    "final_proposed_record_type",
    "final_reason_code",
    "final_reason",
    "primary_reviewer",
    "batch_id",
    "audit_status",
    "retained_candidate_key",
)
AUDIT_HEADERS = (
    "candidate_key",
    "source_row_sha256",
    "primary_reviewer",
    "audit_stratum",
    "audit_rank",
    "audit_reviewer",
    "primary_decision",
    "primary_reason_code",
    "primary_proposed_record_type",
    "audit_decision",
    "audit_reason_code",
    "audit_proposed_record_type",
    "audit_reason",
    "conflict_status",
    "adjudicator",
    "final_decision",
    "final_reason_code",
    "final_proposed_record_type",
    "final_reason",
)

DECISION_MAP = {
    "include_applied_seed": ({"I_APPLIED_TRANSFERABLE_DESIGN"}, {"applied_seed"}),
    "include_method_source_lead": ({"I_METHOD_SOURCE"}, {"method_source"}),
    "include_diagnostic_or_correction_lead": (
        {"I_DIAGNOSTIC_CORRECTION"},
        {"diagnostic", "correction", "guidance", "reproducibility"},
    ),
    "include_simulation_or_mechanistic_lead": (
        {"I_SIMULATION_MECHANISTIC"},
        {"method_source", "applied_seed"},
    ),
    "uncertain_retrieve_primary": ({"U_PRIMARY_RECORD_NEEDED"}, {""}),
    "exclude": (
        {
            "X_DESCRIPTIVE_ONLY",
            "X_COMMENTARY_ONLY",
            "X_DUPLICATE",
            "X_NOT_INFECTIOUS_TRANSFERABLE",
            "X_NO_RESOLVABLE_IDENTITY",
            "X_WRONG_RECORD_TYPE",
        },
        {""},
    ),
}


@dataclass(frozen=True)
class SearchCell:
    search_id: str
    lane: str
    family: str
    source: str
    query: str
    parent_search_id: str
    date_start: str
    date_end: str


def _error(kind: str, path: Path, error: BaseException) -> str:
    return f"{kind}: {path}: {type(error).__name__}: {error}"


def _read_json(path: Path, kind: str) -> tuple[object | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except (json.JSONDecodeError, UnicodeError, OSError) as error:
        return None, [_error(kind, path, error)]


def _read_csv(path: Path, kind: str) -> tuple[list[str] | None, list[dict[str, str]], list[str]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            return reader.fieldnames, list(reader), []
    except (csv.Error, UnicodeError, OSError) as error:
        return None, [], [_error(kind, path, error)]


def load_configuration(root: Path) -> tuple[dict[str, object], list[dict[str, str]]]:
    config = json.loads((root / QUERY_CONFIG_PATH).read_text(encoding="utf-8"))
    with (root / JOURNAL_REGISTRY_PATH).open("r", encoding="utf-8", newline="") as handle:
        journals = list(csv.DictReader(handle, strict=True))
    if not isinstance(config, dict):
        raise ValueError("discovery query configuration must be an object")
    return config, journals


def validate_configuration(root: Path) -> list[str]:
    root = Path(root)
    required = (PROTOCOL_PATH, QUERY_CONFIG_PATH, JOURNAL_REGISTRY_PATH)
    missing = [path for path in required if not (root / path).is_file()]
    if missing:
        return [f"required discovery file missing: {path}" for path in missing]

    config_object, json_errors = _read_json(
        root / QUERY_CONFIG_PATH, "invalid discovery query JSON"
    )
    if json_errors or not isinstance(config_object, dict):
        return json_errors or ["invalid discovery query JSON: expected object"]
    config = config_object
    errors: list[str] = []
    families = config.get("families")
    if not isinstance(families, list):
        families = []
    names = {
        row.get("family")
        for row in families
        if isinstance(row, dict) and isinstance(row.get("family"), str)
    }
    if names != FAMILIES or len(families) != len(FAMILIES):
        errors.append("family set mismatch")
    tokens = [
        str(row.get("token", "")).strip()
        for row in families
        if isinstance(row, dict)
    ]
    if len(tokens) != len(set(tokens)):
        errors.append("duplicate family token")

    headers, journals, csv_errors = _read_csv(
        root / JOURNAL_REGISTRY_PATH, "invalid journal registry"
    )
    errors.extend(csv_errors)
    if csv_errors:
        return list(dict.fromkeys(errors))
    if headers != list(JOURNAL_HEADERS):
        errors.append("journal header mismatch")
        return list(dict.fromkeys(errors))

    seen_tokens: set[str] = set()
    for row in journals:
        status_value = (row.get("status") or "").strip()
        if status_value not in JOURNAL_STATUSES:
            errors.append("invalid journal status")
        if JOURNAL_ID_PATTERN.fullmatch((row.get("journal_id") or "").strip()) is None:
            errors.append("invalid journal_id")
        if (row.get("group") or "").strip() not in JOURNAL_GROUPS:
            errors.append("invalid journal group")
        if (row.get("search_role") or "").strip() not in JOURNAL_SEARCH_ROLES:
            errors.append("invalid journal search_role")
        if not (row.get("title") or "").strip():
            errors.append("blank journal title")
        if not (row.get("official_url") or "").strip():
            errors.append("blank official_url")
        if status_value == "active":
            token = (row.get("pubmed_token") or "").strip()
            if not token:
                errors.append("blank pubmed_token")
            elif token in seen_tokens:
                errors.append("duplicate pubmed_token")
            else:
                seen_tokens.add(token)

    try:
        cells = build_search_cells(root, date(2000, 1, 1))
    except (KeyError, TypeError, ValueError):
        cells = []
    ids = [cell.search_id for cell in cells]
    if len(ids) != len(set(ids)):
        errors.append("duplicate search_id")
    return list(dict.fromkeys(errors))


def build_search_cells(root: Path, executed_date: date) -> list[SearchCell]:
    config, journals = load_configuration(Path(root))
    date_start = str(config["applied_date_start"])
    date_end = str(config["applied_date_end"])
    infectious = str(config["infectious_disease_block"])
    date_block = f'("{date_start}"[Date - Publication] : "{date_end}"[Date - Publication])'
    journal_tokens = sorted(
        (row.get("pubmed_token") or "").strip()
        for row in journals
        if (row.get("status") or "").strip() == "active"
    )
    journal_block = "(" + " OR ".join(f'"{token}"[Journal]' for token in journal_tokens) + ")"
    families = [row for row in config["families"] if isinstance(row, dict)]
    cells: list[SearchCell] = []
    for lane in ("FAMILY", "VENUE"):
        for family in sorted(families, key=lambda row: str(row["token"])):
            method = str(family["method_block"])
            if lane == "FAMILY":
                method = method.replace("[Title/Abstract]", "[Title]")
                parts = (method, infectious, date_block)
            else:
                parts = (method, infectious, journal_block, date_block)
            token = str(family["token"])
            cells.append(
                SearchCell(
                    search_id=(
                        f"SEARCH-{executed_date:%Y%m%d}-PUBMED-{lane}-{token}-01"
                    ),
                    lane=lane,
                    family=str(family["family"]),
                    source=str(config["source"]),
                    query=" AND ".join(parts),
                    parent_search_id="",
                    date_start=date_start,
                    date_end=date_end,
                )
            )
    return cells


def _safe_relative(raw: object) -> str | None:
    if not isinstance(raw, str) or not raw:
        return None
    path = PurePosixPath(raw)
    if path.is_absolute() or ".." in path.parts or "." in path.parts:
        return None
    return path.as_posix()


def _validate_manifest(run_dir: Path) -> tuple[list[str], dict[str, str]]:
    path = run_dir / "MANIFEST_SHA256.json"
    if not path.is_file():
        return ["manifest missing: MANIFEST_SHA256.json"], {}
    payload, errors = _read_json(path, "invalid manifest")
    if errors:
        return errors, {}
    if not isinstance(payload, dict) or payload.get("algorithm") != "SHA256" or not isinstance(payload.get("files"), list):
        return ["invalid manifest shape"], {}
    entries: dict[str, str] = {}
    for item in payload["files"]:
        if not isinstance(item, dict):
            errors.append("invalid manifest entry")
            continue
        relative = _safe_relative(item.get("path"))
        digest = item.get("sha256")
        if relative is None:
            errors.append("manifest path traversal")
            continue
        if relative in entries:
            errors.append(f"duplicate manifest path: {relative}")
            continue
        if not isinstance(digest, str) or SHA256_PATTERN.fullmatch(digest) is None:
            errors.append(f"invalid manifest sha256: {relative}")
            continue
        entries[relative] = digest
        artifact = run_dir / relative
        try:
            mode = artifact.lstat().st_mode
        except OSError:
            errors.append(f"manifest file missing: {relative}")
            continue
        if artifact.is_symlink() or not stat.S_ISREG(mode):
            errors.append(f"manifest path is not a regular file: {relative}")
            continue
        try:
            actual = hashlib.sha256(artifact.read_bytes()).hexdigest()
        except OSError as error:
            errors.append(_error("manifest file unreadable", Path(relative), error))
            continue
        if actual != digest:
            errors.append(f"checksum mismatch: {relative}")
    return errors, entries


def _reference_errors(
    relative_raw: object,
    digest_raw: object,
    manifest: dict[str, str],
    label: str,
) -> list[str]:
    relative = _safe_relative(relative_raw)
    if relative is None:
        return [f"{label} path traversal"]
    if relative not in manifest:
        return [f"{label} path absent from manifest: {relative}"]
    if not isinstance(digest_raw, str) or digest_raw != manifest[relative]:
        return [f"{label} SHA disagreement: {relative}"]
    return []


def _count_xml_records(path: Path) -> int:
    root = ET.parse(path).getroot()
    return sum(
        child.tag.rsplit("}", 1)[-1] in {"PubmedArticle", "PubmedBookArticle"}
        for child in root
    )


def _integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _parse_date(value: object) -> date | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        return datetime.strptime(value, "%Y/%m/%d").date()
    except ValueError:
        return None


def _validate_pages(
    run_dir: Path,
    pages: object,
    source_count: int,
    manifest: dict[str, str],
    owned_page_paths: set[str],
) -> list[str]:
    if not isinstance(pages, list):
        return ["missing leaf receipt field: efetch_pages"]
    errors: list[str] = []
    expected_start = 0
    parsed_total = 0
    for page in pages:
        if not isinstance(page, dict):
            errors.append("invalid page receipt")
            continue
        for field in PAGE_REQUIRED_FIELDS:
            if field not in page:
                errors.append(f"missing page receipt field: {field}")
        if any(field not in page for field in PAGE_REQUIRED_FIELDS):
            continue
        retstart = page["retstart"]
        retmax = page["retmax"]
        parsed_count = page["parsed_count"]
        if not _integer(retstart) or not _integer(retmax) or not _integer(parsed_count):
            errors.append("invalid page count")
            continue
        if retmax == 0 or retmax > 200:
            errors.append("invalid page retmax")
        if retstart > expected_start:
            errors.append("page interval gap")
        elif retstart < expected_start:
            errors.append("page interval overlap")
        if parsed_count > retmax:
            errors.append("parsed count exceeds retmax")
        expected_start = retstart + retmax
        parsed_total += parsed_count
        errors.extend(
            _reference_errors(page["path"], page["sha256"], manifest, "page")
        )
        relative = _safe_relative(page["path"])
        if relative is not None:
            if relative in owned_page_paths:
                errors.append(f"duplicate raw page path: {relative}")
            else:
                owned_page_paths.add(relative)
        if relative is not None and relative in manifest:
            try:
                actual_count = _count_xml_records(run_dir / relative)
            except (ET.ParseError, OSError):
                errors.append(f"invalid PubMed XML: {relative}")
            else:
                if actual_count != parsed_count:
                    errors.append(f"parsed count mismatch: {relative}")
    if expected_start != source_count or parsed_total != source_count:
        errors.append("page ranges do not end at source count")
    return errors


def _validate_cell(
    run_dir: Path,
    cell: object,
    manifest: dict[str, str],
    search_ids: set[str],
    owned_esearch_paths: set[str],
    owned_page_paths: set[str],
    expected_parent: str = "",
) -> list[str]:
    if not isinstance(cell, dict):
        return ["invalid cell receipt"]
    errors: list[str] = []
    for field in CELL_REQUIRED_FIELDS:
        if field not in cell:
            errors.append(f"missing cell receipt field: {field}")
    if any(field not in cell for field in CELL_REQUIRED_FIELDS):
        return errors
    search_id = cell["search_id"]
    if not isinstance(search_id, str) or not search_id.strip():
        errors.append("blank search_id")
    elif search_id in search_ids:
        errors.append("duplicate search_id")
    else:
        search_ids.add(search_id)
    if cell["parent_search_id"] != expected_parent:
        errors.append(f"parent_search_id mismatch: {search_id}")
    if cell["status"] != "complete":
        errors.append(f"invalid cell status: {search_id}")
    for field in ("date_start", "date_end"):
        if _parse_date(cell[field]) is None:
            errors.append(f"blank or invalid cell date: {field}")
    reported_count = cell["reported_count"]
    if not _integer(reported_count):
        errors.append("invalid nonnegative integer count: reported_count")
        return errors
    errors.extend(
        _reference_errors(
            cell["esearch_path"], cell["esearch_sha256"], manifest, "esearch"
        )
    )
    esearch_path = _safe_relative(cell["esearch_path"])
    if esearch_path is not None:
        if esearch_path in owned_esearch_paths:
            errors.append(f"duplicate esearch path: {esearch_path}")
        else:
            owned_esearch_paths.add(esearch_path)
    cell_type = cell["cell_type"]
    if cell_type == "leaf":
        for field in LEAF_REQUIRED_FIELDS:
            if field not in cell:
                errors.append(f"missing leaf receipt field: {field}")
        if any(field not in cell for field in LEAF_REQUIRED_FIELDS):
            return errors
        if reported_count >= 10000:
            errors.append("leaf count at or above 10000")
        if cell["usehistory"] is not True:
            errors.append("leaf usehistory must be true")
        for field in ("webenv", "query_key"):
            if not isinstance(cell[field], str) or not cell[field].strip():
                errors.append(f"blank leaf receipt field: {field}")
        retrieved_count = cell["retrieved_count"]
        if not _integer(retrieved_count):
            errors.append("invalid nonnegative integer count: retrieved_count")
        elif retrieved_count != reported_count:
            errors.append("retrieved_count does not equal reported_count")
        errors.extend(
            _validate_pages(
                run_dir,
                cell["efetch_pages"],
                reported_count,
                manifest,
                owned_page_paths,
            )
        )
    elif cell_type == "split_parent":
        if reported_count < 10000:
            errors.append("split parent count below 10000")
        if cell.get("retrieved_count") != 0:
            errors.append("parent records counted as retrieved")
        for field in ("usehistory", "webenv", "query_key", "efetch_pages"):
            if field in cell:
                errors.append(f"split parent persists history/page field: {field}")
        children = cell.get("children")
        if not isinstance(children, list) or not children:
            errors.append("split parent requires children")
            return errors
        parent_start = _parse_date(cell["date_start"])
        parent_end = _parse_date(cell["date_end"])
        expected_start = parent_start
        child_reported_total = 0
        all_children_are_objects = all(isinstance(child, dict) for child in children)
        for child in children:
            child_start = _parse_date(child.get("date_start")) if isinstance(child, dict) else None
            child_end = _parse_date(child.get("date_end")) if isinstance(child, dict) else None
            if expected_start is not None and child_start is not None:
                if child_start > expected_start:
                    errors.append("split interval gap")
                elif child_start < expected_start:
                    errors.append("split interval overlap")
            if child_end is not None:
                expected_start = child_end + timedelta(days=1)
            if isinstance(child, dict) and _integer(child.get("reported_count")):
                child_reported_total += child["reported_count"]
            errors.extend(
                _validate_cell(
                    run_dir,
                    child,
                    manifest,
                    search_ids,
                    owned_esearch_paths,
                    owned_page_paths,
                    str(search_id),
                )
            )
        if (
            all_children_are_objects
            and parent_start is not None
            and _parse_date(children[0].get("date_start")) != parent_start
        ):
            errors.append("split children do not cover parent start")
        if (
            all_children_are_objects
            and parent_end is not None
            and _parse_date(children[-1].get("date_end")) != parent_end
        ):
            errors.append("split children do not cover parent end")
        if child_reported_total != reported_count:
            errors.append("split parent count mismatch")
    else:
        errors.append("invalid cell_type")
    return errors


def _validate_configuration_files(items: object, lineage: bool = False) -> list[str]:
    if not isinstance(items, list):
        return ["invalid configuration_files"]
    expected = {str(PROTOCOL_PATH), str(QUERY_CONFIG_PATH), str(JOURNAL_REGISTRY_PATH)}
    expected_count = 4 if lineage else 3
    if len(items) != expected_count:
        return ["configuration_files mismatch"]
    paths: set[str] = set()
    errors: list[str] = []
    for item in items:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            errors.append("invalid configuration file receipt")
            continue
        path = item["path"]
        digest = item["sha256"]
        if not isinstance(path, str) or not path:
            errors.append("invalid configuration file path")
        else:
            paths.add(path)
        if not isinstance(digest, str) or SHA256_PATTERN.fullmatch(digest) is None:
            errors.append("invalid configuration file sha256")
    if not expected.issubset(paths):
        errors.append("configuration_files mismatch")
    if lineage and not any(path.endswith("LINEAGE_QUERY_REGISTRY.csv") for path in paths):
        errors.append("lineage configuration_files mismatch")
    return errors


def _configuration_root(run_dir: Path) -> Path | None:
    for candidate in (run_dir, *run_dir.parents):
        if all(
            (candidate / relative).is_file()
            for relative in (PROTOCOL_PATH, QUERY_CONFIG_PATH, JOURNAL_REGISTRY_PATH)
        ):
            return candidate
    return None


def _validate_configuration_file_hashes(
    root: Path, items: object
) -> list[str]:
    if not isinstance(items, list):
        return ["invalid configuration_files"]
    errors: list[str] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        relative = _safe_relative(item.get("path"))
        if relative is None:
            errors.append("configuration file path traversal")
            continue
        path = root / relative
        if not path.is_file() or path.is_symlink():
            errors.append(f"configuration file missing: {relative}")
            continue
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as error:
            errors.append(_error("configuration file unreadable", Path(relative), error))
            continue
        if digest != item.get("sha256"):
            errors.append(f"configuration file checksum mismatch: {relative}")
    return errors


def validate_search_run(run_dir: Path) -> list[str]:
    run_dir = Path(run_dir)
    manifest_errors, manifest = _validate_manifest(run_dir)
    errors = list(manifest_errors)
    receipt_path = run_dir / "RUN_RECEIPT.json"
    if not receipt_path.is_file():
        errors.append("RUN_RECEIPT.json missing")
        return list(dict.fromkeys(errors))
    payload, receipt_errors = _read_json(receipt_path, "invalid run receipt")
    errors.extend(receipt_errors)
    if receipt_errors or not isinstance(payload, dict):
        return list(dict.fromkeys(errors or ["invalid run receipt shape"]))
    for field in RUN_REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing receipt field: {field}")
    if any(field not in payload for field in RUN_REQUIRED_FIELDS):
        return list(dict.fromkeys(errors))
    wave_two = run_dir.name == "wave_02_synonym_expansion"
    configuration_root = _configuration_root(run_dir)
    config_errors = _validate_configuration_files(payload["configuration_files"])
    if wave_two:
        items = payload["configuration_files"]
        required_paths = {
            str(PROTOCOL_PATH),
            str(QUERY_CONFIG_PATH),
            str(JOURNAL_REGISTRY_PATH),
        }
        received_paths = {
            str(item.get("path", ""))
            for item in items
            if isinstance(item, dict)
        } if isinstance(items, list) else set()
        extra_paths = received_paths - required_paths
        expected_query_registry = ""
        if configuration_root is not None:
            try:
                expected_query_registry = (
                    run_dir.resolve().relative_to(configuration_root.resolve())
                    / "QUERY_REGISTRY.csv"
                ).as_posix()
            except (OSError, ValueError):
                expected_query_registry = ""
        if (
            not isinstance(items, list)
            or len(items) != 4
            or not required_paths.issubset(received_paths)
            or extra_paths != {expected_query_registry}
        ):
            config_errors = ["wave 2 configuration_files mismatch"]
        else:
            config_errors = [error for error in config_errors if error != "configuration_files mismatch"]
    errors.extend(config_errors)
    if configuration_root is None:
        errors.append("configuration root not found")
    else:
        errors.extend(
            _validate_configuration_file_hashes(
                configuration_root, payload["configuration_files"]
            )
        )
    if payload.get("source") != "pubmed":
        errors.append("invalid run source")
    cells = payload["cells"]
    if not isinstance(cells, list):
        errors.append("invalid cells receipt")
    else:
        if run_dir.name == "wave_01_frozen_queries":
            try:
                executed_date = datetime.fromisoformat(str(payload["executed_at"])).date()
                expected_roots = build_search_cells(configuration_root, executed_date)
            except (KeyError, TypeError, ValueError, OSError):
                expected_roots = []
            expected_signatures = {
                (
                    cell.search_id,
                    cell.lane,
                    cell.family,
                    cell.query,
                    cell.parent_search_id,
                    cell.date_start,
                    cell.date_end,
                )
                for cell in expected_roots
            }
            actual_signatures = {
                (
                    cell.get("search_id"),
                    cell.get("lane"),
                    cell.get("family"),
                    cell.get("query"),
                    cell.get("parent_search_id"),
                    cell.get("date_start"),
                    cell.get("date_end"),
                )
                for cell in cells
                if isinstance(cell, dict)
            }
            if len(cells) != 12 or actual_signatures != expected_signatures:
                errors.append("wave 1 root cell mismatch")
        search_ids: set[str] = set()
        owned_esearch_paths: set[str] = set()
        owned_page_paths: set[str] = set()
        for cell in cells:
            errors.extend(
                _validate_cell(
                    run_dir,
                    cell,
                    manifest,
                    search_ids,
                    owned_esearch_paths,
                    owned_page_paths,
                )
            )
    if "compiled_candidates_raw.csv" not in manifest:
        errors.append("compiled_candidates_raw.csv absent from manifest")
    return list(dict.fromkeys(errors))


def _validate_lineage_pages(
    run_dir: Path,
    row: dict[str, object],
    count: int,
    manifest: dict[str, str],
    owned_page_paths: set[str],
) -> list[str]:
    return _validate_pages(
        run_dir, row.get("efetch_pages"), count, manifest, owned_page_paths
    )


def validate_lineage(root: Path, run_dir: Path) -> list[str]:
    root = Path(root)
    run_dir = Path(run_dir)
    manifest_errors, manifest = _validate_manifest(run_dir)
    errors = list(manifest_errors)
    path = run_dir / "LINEAGE_RUN_RECEIPT.json"
    if not path.is_file():
        errors.append("LINEAGE_RUN_RECEIPT.json missing")
        return list(dict.fromkeys(errors))
    payload, read_errors = _read_json(path, "invalid lineage receipt")
    errors.extend(read_errors)
    if read_errors or not isinstance(payload, dict):
        return list(dict.fromkeys(errors or ["invalid lineage receipt shape"]))
    for field in LINEAGE_REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing lineage receipt field: {field}")
    if any(field not in payload for field in LINEAGE_REQUIRED_FIELDS):
        return list(dict.fromkeys(errors))
    errors.extend(_validate_configuration_files(payload["configuration_files"], lineage=True))
    errors.extend(
        _validate_configuration_file_hashes(root, payload["configuration_files"])
    )
    queries = payload["queries"]
    if not isinstance(queries, list):
        errors.append("invalid lineage queries")
        queries = []
    seen: set[str] = set()
    owned_page_paths: set[str] = set()
    owned_raw_paths: set[str] = set()
    for row in queries:
        if not isinstance(row, dict):
            errors.append("invalid lineage query receipt")
            continue
        for field in LINEAGE_QUERY_FIELDS:
            if field not in row:
                errors.append(f"missing lineage query field: {field}")
        if any(field not in row for field in LINEAGE_QUERY_FIELDS):
            continue
        query_id = row["query_id"]
        if not isinstance(query_id, str) or not query_id.strip():
            errors.append("invalid lineage query_id")
        elif query_id in seen:
            errors.append("duplicate lineage query_id")
        else:
            seen.add(query_id)
        reported_count = row["reported_count"]
        if not _integer(reported_count):
            errors.append("invalid nonnegative integer count: reported_count")
            continue
        errors.extend(_reference_errors(row["raw_path"], row["raw_sha256"], manifest, "lineage raw"))
        lineage_raw_path = _safe_relative(row["raw_path"])
        if lineage_raw_path is not None:
            if lineage_raw_path in owned_raw_paths:
                errors.append(f"duplicate lineage raw path: {lineage_raw_path}")
            else:
                owned_raw_paths.add(lineage_raw_path)
        source = row["source"]
        if row.get("status") != "complete":
            errors.append("invalid lineage query status")
        if source == "pubmed":
            required = (
                "date_start", "date_end", "query_scope", "esearch_path",
                "esearch_sha256", "usehistory", "webenv", "query_key", "efetch_pages",
            )
            for field in required:
                if field not in row:
                    errors.append(f"missing PubMed lineage field: {field}")
            if any(field not in row for field in required):
                continue
            if row["date_start"] != "" or row["date_end"] != "":
                errors.append("PubMed lineage dates must be blank")
            if row["query_scope"] != "unbounded_identity":
                errors.append("invalid PubMed lineage query_scope")
            if row["raw_path"] != row["esearch_path"] or row["raw_sha256"] != row["esearch_sha256"]:
                errors.append("PubMed lineage raw/esearch mismatch")
            if row["usehistory"] is not True or not str(row["webenv"]).strip() or not str(row["query_key"]).strip():
                errors.append("invalid PubMed lineage history fields")
            if reported_count >= 10000:
                errors.append("overbroad lineage identity query")
            else:
                errors.extend(
                    _validate_lineage_pages(
                        run_dir, row, reported_count, manifest, owned_page_paths
                    )
                )
        elif source == "crossref":
            required = (
                "response_path", "response_sha256", "returned_candidate_count",
                "total_results", "rows",
            )
            for field in required:
                if field not in row:
                    errors.append(f"missing Crossref lineage field: {field}")
            for field in ("esearch_path", "esearch_sha256", "usehistory", "webenv", "query_key", "efetch_pages"):
                if field in row:
                    errors.append(f"prohibited crossref field: {field}")
            if any(field not in row for field in required):
                continue
            if row["raw_path"] != row["response_path"] or row["raw_sha256"] != row["response_sha256"]:
                errors.append("Crossref lineage raw/response mismatch")
            if row["rows"] != 5:
                errors.append("Crossref rows must equal 5")
            for field in ("returned_candidate_count", "total_results"):
                if not _integer(row[field]):
                    errors.append(f"invalid nonnegative integer count: {field}")
        else:
            errors.append("invalid lineage source")
    for table in ("pubmed_lineage_candidates.csv", "crossref_candidates.csv"):
        if table not in manifest:
            errors.append(f"lineage candidate table absent from manifest: {table}")
    return list(dict.fromkeys(errors))


def _rows_with_headers(path: Path, expected: tuple[str, ...], kind: str) -> tuple[list[dict[str, str]], list[str]]:
    if not path.is_file():
        return [], [f"{kind} missing: {path.name}"]
    headers, rows, errors = _read_csv(path, f"invalid {kind}")
    if not errors and headers != list(expected):
        errors.append(f"{kind} header mismatch")
    return rows, errors


def _decision_errors(decision: str, code: str, proposed_type: str, label: str) -> list[str]:
    if decision not in DECISION_MAP:
        return [f"invalid {label} decision"]
    codes, types = DECISION_MAP[decision]
    errors: list[str] = []
    if code not in codes:
        errors.append(f"invalid {label} reason code mapping")
    if proposed_type not in types:
        errors.append(f"invalid {label} proposed record type mapping")
    return errors


def _compiled_index(run_dir: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    rows, errors = _rows_with_headers(
        run_dir / "compiled_candidates_raw.csv", COMPILED_HEADERS, "compiled candidates"
    )
    index: dict[str, dict[str, str]] = {}
    for row in rows:
        key = (row.get("candidate_key") or "").strip()
        if not key or key in index:
            errors.append("duplicate or blank compiled candidate key")
        else:
            index[key] = row
    return index, errors


def _primary_index(run_dir: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    rows: list[dict[str, str]] = []
    batch_dir = run_dir / "screening_batches"
    if not batch_dir.is_dir():
        return {}, ["screening batches missing"]
    for path in sorted(batch_dir.glob("*.csv")):
        batch_rows, batch_errors = _rows_with_headers(path, PRIMARY_HEADERS, "screening batch")
        rows.extend(batch_rows)
        errors.extend(batch_errors)
    index: dict[str, dict[str, str]] = {}
    for row in rows:
        key = row.get("candidate_key", "")
        if key in index:
            errors.append(f"duplicate primary screening key: {key}")
        else:
            index[key] = row
    return index, errors


def validate_screening(run_dir: Path) -> list[str]:
    run_dir = Path(run_dir)
    compiled, errors = _compiled_index(run_dir)
    primary, primary_errors = _primary_index(run_dir)
    errors.extend(primary_errors)
    screened_rows, screened_errors = _rows_with_headers(
        run_dir / "screened_candidates.csv", SCREENED_HEADERS, "screened candidates"
    )
    errors.extend(screened_errors)
    screened: dict[str, dict[str, str]] = {}
    for key, raw in primary.items():
        if key not in compiled:
            errors.append(f"orphan primary screening key: {key}")
            continue
        if raw.get("source_row_sha256") != compiled[key].get("row_sha256"):
            errors.append(f"source row SHA mismatch: {key}")
        errors.extend(
            _decision_errors(
                raw.get("primary_decision", ""),
                raw.get("primary_reason_code", ""),
                raw.get("primary_proposed_record_type", ""),
                "primary",
            )
        )
        if not raw.get("primary_reason", "").strip():
            errors.append(f"blank primary reason: {key}")
        if raw.get("primary_reason_code") == "X_DUPLICATE" and not raw.get("retained_candidate_key", "").strip():
            errors.append(f"duplicate exclusion missing retained key: {key}")
    for row in screened_rows:
        key = row.get("candidate_key", "")
        if key in screened:
            errors.append(f"duplicate screened candidate key: {key}")
            continue
        screened[key] = row
        if key not in primary or key not in compiled:
            errors.append(f"orphan screened candidate key: {key}")
            continue
        for field in PRIMARY_HEADERS:
            if field in row and row[field] != primary[key][field]:
                errors.append(f"screened primary field mismatch: {key}: {field}")
        errors.extend(
            _decision_errors(
                row.get("final_decision", ""),
                row.get("final_reason_code", ""),
                row.get("final_proposed_record_type", ""),
                "final",
            )
        )
        if row.get("audit_status") not in {"not_selected", "agree", "conflict_open", "conflict_resolved"}:
            errors.append(f"invalid audit_status: {key}")
        if row.get("audit_status") == "not_selected" and (
            row.get("final_decision") != row.get("primary_decision")
            or row.get("final_reason_code") != row.get("primary_reason_code")
            or row.get("final_proposed_record_type")
            != row.get("primary_proposed_record_type")
            or row.get("final_reason") != row.get("primary_reason")
        ):
            errors.append(f"unaudited final result mismatch: {key}")
    for key in sorted(set(compiled) - set(primary)):
        errors.append(f"missing primary screening key: {key}")
    for key in sorted(set(compiled) - set(screened)):
        errors.append(f"missing screened candidate key: {key}")
    return list(dict.fromkeys(errors))


def _audit_stratum(row: dict[str, str], compiled: dict[str, dict[str, str]]) -> str:
    family = compiled.get(row.get("candidate_key", ""), {}).get("preliminary_families", "")
    return "|".join((row.get("primary_decision", ""), row.get("primary_reason_code", ""), family))


def validate_screening_audit(run_dir: Path) -> list[str]:
    run_dir = Path(run_dir)
    compiled, errors = _compiled_index(run_dir)
    primary, primary_errors = _primary_index(run_dir)
    errors.extend(primary_errors)
    screened_rows, screened_errors = _rows_with_headers(
        run_dir / "screened_candidates.csv", SCREENED_HEADERS, "screened candidates"
    )
    errors.extend(screened_errors)
    screened = {
        row.get("candidate_key", ""): row
        for row in screened_rows
        if row.get("candidate_key", "")
    }
    audit_rows, audit_errors = _rows_with_headers(
        run_dir / "screening_audit.csv", AUDIT_HEADERS, "screening audit"
    )
    errors.extend(audit_errors)
    strata: dict[str, list[str]] = {}
    required: set[str] = set()
    for key, row in primary.items():
        stratum = _audit_stratum(row, compiled)
        strata.setdefault(stratum, []).append(key)
        if row.get("primary_decision") == "uncertain_retrieve_primary" or row.get("primary_reason_code") == "X_NOT_INFECTIOUS_TRANSFERABLE":
            required.add(key)
    for keys in strata.values():
        ranked = sorted(keys, key=lambda key: hashlib.sha256(f"{key}|audit-v1".encode()).hexdigest())
        required.update(ranked[: min(len(ranked), max(10, math.ceil(0.1 * len(ranked))))])
    audit: dict[str, dict[str, str]] = {}
    for row in audit_rows:
        key = row.get("candidate_key", "")
        if key in audit:
            errors.append(f"duplicate audit key: {key}")
            continue
        audit[key] = row
        if key not in primary or key not in compiled:
            errors.append(f"orphan audit key: {key}")
            continue
        source = primary[key]
        if row.get("source_row_sha256") != compiled[key].get("row_sha256"):
            errors.append(f"audit source row SHA mismatch: {key}")
        if row.get("primary_reviewer") != source.get("primary_reviewer"):
            errors.append(f"audit primary reviewer mismatch: {key}")
        if (
            row.get("primary_decision") != source.get("primary_decision")
            or row.get("primary_reason_code") != source.get("primary_reason_code")
            or row.get("primary_proposed_record_type")
            != source.get("primary_proposed_record_type")
        ):
            errors.append(f"audit primary decision mismatch: {key}")
        if row.get("audit_reviewer") == row.get("primary_reviewer"):
            errors.append(f"audit reviewer is not independent: {key}")
        if row.get("audit_stratum") != _audit_stratum(source, compiled):
            errors.append(f"audit stratum mismatch: {key}")
        expected_rank = hashlib.sha256(f"{key}|audit-v1".encode()).hexdigest()
        if row.get("audit_rank") != expected_rank:
            errors.append(f"audit rank mismatch: {key}")
        for prefix, decision_field, code_field, type_field in (
            ("primary", "primary_decision", "primary_reason_code", "primary_proposed_record_type"),
            ("audit", "audit_decision", "audit_reason_code", "audit_proposed_record_type"),
            ("final", "final_decision", "final_reason_code", "final_proposed_record_type"),
        ):
            errors.extend(_decision_errors(row.get(decision_field, ""), row.get(code_field, ""), row.get(type_field, ""), prefix))
        conflict = row.get("conflict_status")
        if conflict not in {"none", "open", "resolved"}:
            errors.append(f"invalid audit conflict status: {key}")
        primary_triple = (
            row.get("primary_decision"),
            row.get("primary_reason_code"),
            row.get("primary_proposed_record_type"),
        )
        audit_triple = (
            row.get("audit_decision"),
            row.get("audit_reason_code"),
            row.get("audit_proposed_record_type"),
        )
        if conflict == "none" and primary_triple != audit_triple:
            errors.append(f"falsely closed audit conflict: {key}")
        if conflict == "open" and (
            row.get("final_decision") != "uncertain_retrieve_primary"
            or row.get("final_reason_code") != "U_PRIMARY_RECORD_NEEDED"
            or row.get("final_proposed_record_type") != ""
        ):
            errors.append(f"falsely closed audit conflict: {key}")
        if conflict == "resolved" and not row.get("adjudicator", "").strip():
            errors.append(f"resolved audit conflict missing adjudicator: {key}")
        final_triple = (
            row.get("final_decision"),
            row.get("final_reason_code"),
            row.get("final_proposed_record_type"),
        )
        if conflict == "none" and final_triple != audit_triple:
            errors.append(f"audit final result mismatch: {key}")
        screened_row = screened.get(key)
        expected_audit_status = {
            "none": "agree",
            "open": "conflict_open",
            "resolved": "conflict_resolved",
        }.get(conflict)
        if (
            screened_row is None
            or screened_row.get("final_decision") != row.get("final_decision")
            or screened_row.get("final_reason_code") != row.get("final_reason_code")
            or screened_row.get("final_proposed_record_type")
            != row.get("final_proposed_record_type")
            or screened_row.get("final_reason") != row.get("final_reason")
            or screened_row.get("audit_status") != expected_audit_status
        ):
            errors.append(f"screened audit result mismatch: {key}")
    for key in sorted(required - set(audit)):
        errors.append(f"missing required audit key: {key}")
    return list(dict.fromkeys(errors))


def validate_external_boundary(root: Path, source_root: Path) -> list[str]:
    root = Path(root)
    source_root = Path(source_root)
    receipt_path = root / EXTERNAL_BOUNDARY_PATH
    if not receipt_path.is_file():
        return [f"external boundary receipt missing: {EXTERNAL_BOUNDARY_PATH}"]
    payload, errors = _read_json(receipt_path, "invalid external boundary receipt")
    if errors or not isinstance(payload, dict):
        return errors or ["invalid external boundary receipt shape"]
    if payload.get("source_repository") != str(source_root):
        errors.append("external source repository mismatch")
    if payload.get("proof_limit") != EXTERNAL_PROOF_LIMIT:
        errors.append("external proof limit mismatch")
    try:
        captured_at = datetime.fromisoformat(str(payload.get("captured_at", "")))
    except ValueError:
        errors.append("external captured_at invalid")
    else:
        if captured_at.tzinfo is None or captured_at.utcoffset() is None:
            errors.append("external captured_at invalid")
    if payload.get("timezone") != "Asia/Shanghai":
        errors.append("external timezone mismatch")

    def git(*arguments: str) -> str:
        return subprocess.run(
            ["git", "-C", str(source_root), *arguments],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout

    try:
        status_lines = git("status", "--short").splitlines()
        head = git("rev-parse", "HEAD").strip()
        pointer_index_paths = [
            line.split("\t", 1)[1]
            for line in git("ls-files", "--stage", "--", str(EXTERNAL_POINTER_PATH)).splitlines()
            if "\t" in line
        ]
        pointer_lines = git("status", "--short", "--", str(EXTERNAL_POINTER_PATH)).splitlines()
        seed_lines = git("status", "--short", "--", str(EXTERNAL_SEED_SOURCE_PATH)).splitlines()
    except (OSError, subprocess.CalledProcessError) as error:
        return [_error("external boundary git error", source_root, error)]

    excluded = payload.get("filtered_pointer_line")
    expected_pointer_line = f"?? {EXTERNAL_POINTER_PATH.as_posix()}"
    if excluded != expected_pointer_line:
        errors.append("external filtered pointer line mismatch")
    filtered = [line for line in status_lines if line != excluded]
    filtered_text = "\n".join(filtered) + ("\n" if filtered else "")
    digest = hashlib.sha256(filtered_text.encode()).hexdigest()
    if payload.get("filtered_status_line_count") != len(filtered) or payload.get("filtered_status_sha256") != digest:
        errors.append("external filtered status mismatch")

    def status_name(lines: list[str]) -> str:
        if not lines:
            return "clean"
        code = lines[0][:2]
        if code == "??":
            return "untracked"
        if "M" in code:
            return "modified"
        if "A" in code:
            return "added"
        if "D" in code:
            return "deleted"
        return code.strip() or "clean"

    if payload.get("pointer_status") != status_name(pointer_lines):
        errors.append("external pointer status mismatch")
    if payload.get("pointer_index_paths") != pointer_index_paths:
        errors.append("external pointer index mismatch")
    if payload.get("seed_source_status") != status_name(seed_lines):
        errors.append("external seed source status mismatch")
    if payload.get("source_head") != head:
        errors.append("external source HEAD mismatch")
    return list(dict.fromkeys(errors))


def validate_all(root: Path, phase_run_dir: Path) -> list[str]:
    root = Path(root)
    phase_run_dir = Path(phase_run_dir)
    errors = [f"configuration: {error}" for error in validate_configuration(root)]
    for label, directory in (
        ("wave_01", phase_run_dir / "wave_01_frozen_queries"),
        ("wave_02", phase_run_dir / "wave_02_synonym_expansion"),
    ):
        errors.extend(f"{label} search: {error}" for error in validate_search_run(directory))
        errors.extend(f"{label} screening: {error}" for error in validate_screening(directory))
        errors.extend(f"{label} audit: {error}" for error in validate_screening_audit(directory))
    lineage = phase_run_dir / "wave_03_lineage_resolution"
    errors.extend(f"wave_03 lineage: {error}" for error in validate_lineage(root, lineage))
    return list(dict.fromkeys(errors))


def _emit(errors: Iterable[str]) -> int:
    errors = list(errors)
    if errors:
        print("DISCOVERY FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("DISCOVERY PASS")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Execute and validate discovery searches")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_config = subparsers.add_parser("validate-config")
    validate_config.add_argument("--root", type=Path, default=Path.cwd())
    list_cells = subparsers.add_parser("list-cells")
    list_cells.add_argument("--root", type=Path, default=Path.cwd())
    list_cells.add_argument("--date", type=date.fromisoformat, required=True)
    verify = subparsers.add_parser("verify")
    verify.add_argument("--run-dir", type=Path, required=True)
    screening = subparsers.add_parser("validate-screening")
    screening.add_argument("--run-dir", type=Path, required=True)
    audit = subparsers.add_parser("validate-audit")
    audit.add_argument("--run-dir", type=Path, required=True)
    lineage = subparsers.add_parser("verify-lineage")
    lineage.add_argument("--root", type=Path, default=Path.cwd())
    lineage.add_argument("--run-dir", type=Path, required=True)
    verify_all = subparsers.add_parser("verify-all")
    verify_all.add_argument("--root", type=Path, default=Path.cwd())
    verify_all.add_argument("--run-dir", type=Path, required=True)
    external = subparsers.add_parser("verify-external-boundary")
    external.add_argument("--root", type=Path, default=Path.cwd())
    external.add_argument("--source-root", type=Path, required=True)

    run = subparsers.add_parser("run")
    run.add_argument("--root", type=Path, default=Path.cwd())
    run.add_argument("--date", type=date.fromisoformat, required=True)
    run.add_argument("--email", required=True)
    run.add_argument("--api-key")
    run.add_argument("--output", type=Path, required=True)
    for command in ("run-wave", "run-lineage"):
        deferred = subparsers.add_parser(command)
        deferred.add_argument("--root", type=Path, default=Path.cwd())
        deferred.add_argument("--query-registry", type=Path, required=True)
        deferred.add_argument("--email", required=True)
        deferred.add_argument("--api-key")
        deferred.add_argument("--output", type=Path, required=True)
    compile_parser = subparsers.add_parser("compile")
    compile_parser.add_argument("--run-dir", type=Path, required=True)

    args = parser.parse_args(argv)
    if args.command == "validate-config":
        return _emit(validate_configuration(args.root))
    if args.command == "list-cells":
        errors = validate_configuration(args.root)
        if errors:
            return _emit(errors)
        for cell in build_search_cells(args.root, args.date):
            print(json.dumps(asdict(cell), sort_keys=True))
        return 0
    if args.command == "verify":
        return _emit(validate_search_run(args.run_dir))
    if args.command == "validate-screening":
        return _emit(validate_screening(args.run_dir))
    if args.command == "validate-audit":
        return _emit(validate_screening_audit(args.run_dir))
    if args.command == "verify-lineage":
        return _emit(validate_lineage(args.root, args.run_dir))
    if args.command == "verify-all":
        return _emit(validate_all(args.root, args.run_dir))
    if args.command == "verify-external-boundary":
        return _emit(validate_external_boundary(args.root, args.source_root))
    return _emit([f"{args.command} is deferred to the retrieval implementation task"])


if __name__ == "__main__":
    sys.exit(main())
