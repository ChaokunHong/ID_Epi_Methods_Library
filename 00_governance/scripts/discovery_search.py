from __future__ import annotations

import argparse
import calendar
import csv
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
import hashlib
import importlib.util
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import time
from typing import Callable, Iterable, Sequence
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo


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
APPROVED_JOURNAL_TITLES = frozenset(
    {
        "The Lancet",
        "New England Journal of Medicine",
        "JAMA",
        "BMJ",
        "PLOS Medicine",
        "Nature",
        "Science",
        "Proceedings of the National Academy of Sciences",
        "Nature Medicine",
        "The Lancet Infectious Diseases",
        "Clinical Infectious Diseases",
        "Nature Microbiology",
        "Emerging Infectious Diseases",
        "Eurosurveillance",
        "The Lancet Global Health",
        "Epidemiology",
        "International Journal of Epidemiology",
        "American Journal of Epidemiology",
        "npj Digital Medicine",
        "npj Vaccines",
        "npj Biofilms and Microbiomes",
        "npj Systems Biology and Applications",
    }
)
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
LINEAGE_REGISTRY_HEADERS = (
    "query_id", "named_source_id", "method_label", "canonical_name", "family",
    "source_role", "source", "query_variant", "query", "seed_candidate_keys",
    "reviewer",
)
PUBMED_LINEAGE_HEADERS = (
    "candidate_key", "query_id", "named_source_id", "candidate_rank", "pmid",
    "doi", "title", "year", "journal", "authors", "source_url", "raw_path",
    "raw_sha256",
)
CROSSREF_LINEAGE_HEADERS = (
    "candidate_key", "query_id", "named_source_id", "bibliographic_query",
    "candidate_rank", "doi", "title", "year", "container_title", "first_author",
    "type", "url", "raw_path", "raw_sha256",
)
WAVE_TWO_QUERY_HEADERS = (
    "family", "search_id", "status", "new_synonyms", "rationale",
    "source_candidate_keys", "source", "query", "date_start", "date_end",
    "reviewer",
)
LINEAGE_SOURCES = frozenset({"pubmed", "crossref"})
LINEAGE_QUERY_VARIANTS = (
    "exact_title",
    "title_first_author",
    "method_author_year",
)
LINEAGE_SOURCE_ROLES = frozenset(
    {
        "original_candidate",
        "authoritative_candidate",
        "correction",
        "diagnostic",
        "guidance",
        "implementation",
        "infectious_application",
    }
)
FAMILY_TOKENS = {
    "causal_policy": "CAUSAL",
    "surveillance_measurement": "SURVEILLANCE",
    "spatial_transmission": "SPATIAL",
    "forecasting_dynamics": "FORECASTING",
    "evidence_synthesis": "EVIDENCE",
    "simulation_methods": "SIMULATION",
}
LINEAGE_AUDIT_HEADERS = (
    "identity_decision_id", "named_source_id", "supporting_query_ids",
    "candidate_keys_considered", "primary_selected_candidate_key",
    "primary_decision", "primary_reason", "primary_reviewer",
    "audit_selected_candidate_key", "audit_decision", "audit_reason",
    "audit_reviewer", "conflict_status", "adjudicator",
    "final_selected_candidate_key", "final_decision", "final_reason",
    "inspected_primary_url",
)
LINEAGE_LEDGER_HEADERS = (
    "identity_decision_id", "named_source_id", "final_candidate_key",
    "method_label", "canonical_name", "family", "source_role", "title", "year",
    "doi", "pmid", "primary_url", "discovery_route",
    "bibliographic_role_evidence", "verification_state", "search_ids", "status",
    "notes",
)
GLOBAL_INDEX_HEADERS = (
    "candidate_key", "waves", "wave_source_row_sha256s", "screening_path",
    "final_decision", "final_proposed_record_type", "final_reason_code",
    "duplicate_disposition",
)
CONFIG_REQUIRED_FIELDS = (
    "schema_version",
    "applied_date_start",
    "applied_date_end",
    "source",
    "family_method_field",
    "venue_method_field",
    "infectious_disease_block",
    "families",
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

PUBMED_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CROSSREF_WORKS_URL = "https://api.crossref.org/works"
TOOL_NAME = "ID_Epi_Methods_Library"
TOOL_VERSION = "1"
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


class DiscoveryExecutionError(RuntimeError):
    """A stable, user-facing retrieval failure."""


class _PacedOpener:
    _discovery_handles_pacing = True

    def __init__(
        self,
        opener: Callable[..., object],
        delay: float,
    ) -> None:
        self._opener = opener
        self._delay = delay
        self._calls = 0

    def __call__(self, *args: object, **kwargs: object) -> object:
        if self._calls:
            time.sleep(self._delay)
        self._calls += 1
        return self._opener(*args, **kwargs)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _atomic_bytes(
    path: Path,
    data: bytes,
    validator: Callable[[bytes], None] | None = None,
) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{time.time_ns()}.tmp")
    try:
        temporary.write_bytes(data)
        if validator is not None:
            validator(data)
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    return _sha256_bytes(data)


def _read_manifest_entries(output_dir: Path) -> dict[str, str]:
    path = output_dir / "MANIFEST_SHA256.json"
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError):
        return {}
    if not isinstance(payload, dict) or not isinstance(payload.get("files"), list):
        return {}
    entries: dict[str, str] = {}
    for item in payload["files"]:
        if isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(
            item.get("sha256"), str
        ):
            entries[item["path"]] = item["sha256"]
    return entries


def _write_manifest_entries(output_dir: Path, entries: dict[str, str]) -> None:
    payload = {
        "algorithm": "SHA256",
        "files": [
            {"path": path, "sha256": entries[path]}
            for path in sorted(entries)
        ],
    }
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    _atomic_bytes(output_dir / "MANIFEST_SHA256.json", rendered)


def _manifest_artifact(output_dir: Path, path: Path, digest: str) -> None:
    relative = path.relative_to(output_dir).as_posix()
    entries = _read_manifest_entries(output_dir)
    entries[relative] = digest
    _write_manifest_entries(output_dir, entries)


def _urlopen_bytes(
    opener: Callable[..., object],
    endpoint: str,
    parameters: dict[str, object],
) -> bytes:
    url = f"{endpoint}?{urllib.parse.urlencode(parameters)}"
    request = urllib.request.Request(url, headers={"User-Agent": f"{TOOL_NAME}/{TOOL_VERSION}"})
    try:
        response = opener(request, timeout=60)
        if hasattr(response, "__enter__"):
            with response as opened:
                data = opened.read()
        else:
            data = response.read()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as error:
        raise DiscoveryExecutionError(
            f"network request failed: {type(error).__name__}: {error}"
        ) from error
    if not isinstance(data, bytes):
        raise DiscoveryExecutionError("network response was not bytes")
    return data


def _parse_esearch(data: bytes) -> tuple[int, str, str]:
    try:
        payload = json.loads(data.decode("utf-8"))
        result = payload["esearchresult"]
        count = int(result["count"])
        webenv = str(result["webenv"])
        query_key = str(result["querykey"])
    except (UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise DiscoveryExecutionError("malformed PubMed ESearch JSON") from error
    if count < 0 or not webenv or not query_key:
        raise DiscoveryExecutionError("malformed PubMed ESearch JSON")
    return count, webenv, query_key


def _parse_pubmed_page(data: bytes) -> tuple[ET.Element, int]:
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise DiscoveryExecutionError("malformed PubMed EFetch XML") from error
    if root.tag.rsplit("}", 1)[-1] != "PubmedArticleSet":
        raise DiscoveryExecutionError("malformed PubMed EFetch XML")
    count = sum(
        child.tag.rsplit("}", 1)[-1] in {"PubmedArticle", "PubmedBookArticle"}
        for child in root
    )
    return root, count


def execute_pubmed_cell(
    cell: SearchCell,
    output_dir: Path,
    email: str,
    api_key: str | None = None,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> dict[str, object]:
    """Execute one PubMed root, recursively splitting oversized date intervals."""
    output_dir = Path(output_dir)
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    request_number = 0
    try:
        id_prefix, id_suffix = cell.search_id.rsplit("-", 1)
        next_suffix = int(id_suffix) + 1
    except (TypeError, ValueError) as error:
        raise DiscoveryExecutionError("invalid PubMed search ID") from error

    def request(endpoint: str, parameters: dict[str, object]) -> bytes:
        nonlocal request_number
        if request_number and not getattr(opener, "_discovery_handles_pacing", False):
            time.sleep(0.11 if api_key else 0.34)
        request_number += 1
        if api_key:
            parameters = {**parameters, "api_key": api_key}
        return _urlopen_bytes(opener, endpoint, parameters)

    def allocate_search_id() -> str:
        nonlocal next_suffix
        allocated = f"{id_prefix}-{next_suffix:02d}"
        next_suffix += 1
        return allocated

    def query_for_interval(query: str, start: date, end: date) -> str:
        replacement = (
            f'("{start:%Y/%m/%d}"[Date - Publication] : '
            f'"{end:%Y/%m/%d}"[Date - Publication])'
        )
        updated, replacements = re.subn(
            r'\("\d{4}/\d{2}/\d{2}"\[Date - Publication\]\s*:\s*'
            r'"\d{4}/\d{2}/\d{2}"\[Date - Publication\]\)\s*$',
            replacement,
            query,
        )
        if replacements != 1:
            raise DiscoveryExecutionError("PubMed query lacks terminal date interval")
        return updated

    def split_intervals(start: date, end: date) -> list[tuple[date, date]]:
        if start.year != end.year:
            return [
                (
                    max(start, date(year, 1, 1)),
                    min(end, date(year, 12, 31)),
                )
                for year in range(start.year, end.year + 1)
            ]
        if start.month != end.month:
            intervals: list[tuple[date, date]] = []
            for month in range(start.month, end.month + 1):
                month_end = date(start.year, month, calendar.monthrange(start.year, month)[1])
                intervals.append(
                    (
                        max(start, date(start.year, month, 1)),
                        min(end, month_end),
                    )
                )
            return intervals
        if start != end:
            return [
                (start + timedelta(days=offset), start + timedelta(days=offset))
                for offset in range((end - start).days + 1)
            ]
        return []

    def execute_interval(current: SearchCell) -> dict[str, object]:
        esearch_data = request(
            PUBMED_ESEARCH_URL,
            {
                "db": "pubmed",
                "term": current.query,
                "retmode": "json",
                "retmax": 0,
                "usehistory": "y",
                "tool": TOOL_NAME,
                "email": email,
            },
        )
        count, webenv, query_key = _parse_esearch(esearch_data)
        esearch_path = raw_dir / f"{current.search_id}.esearch.json"
        esearch_sha = _atomic_bytes(
            esearch_path, esearch_data, lambda data: _parse_esearch(data)
        )
        _manifest_artifact(output_dir, esearch_path, esearch_sha)
        common: dict[str, object] = {
            "search_id": current.search_id,
            "lane": current.lane,
            "family": current.family,
            "query": current.query,
            "date_start": current.date_start,
            "date_end": current.date_end,
            "reported_count": count,
            "parent_search_id": current.parent_search_id,
            "esearch_path": esearch_path.relative_to(output_dir).as_posix(),
            "esearch_sha256": esearch_sha,
            "status": "complete",
        }
        if count >= 10000:
            start = _parse_date(current.date_start)
            end = _parse_date(current.date_end)
            if start is None or end is None:
                raise DiscoveryExecutionError("invalid PubMed split interval")
            intervals = split_intervals(start, end)
            if not intervals:
                raise DiscoveryExecutionError("unsplittable PubMed cell")
            children: list[dict[str, object]] = []
            for child_start, child_end in intervals:
                child = SearchCell(
                    search_id=allocate_search_id(),
                    lane=current.lane,
                    family=current.family,
                    source=current.source,
                    query=query_for_interval(current.query, child_start, child_end),
                    parent_search_id=current.search_id,
                    date_start=f"{child_start:%Y/%m/%d}",
                    date_end=f"{child_end:%Y/%m/%d}",
                )
                children.append(execute_interval(child))
            if sum(int(child["reported_count"]) for child in children) != count:
                raise DiscoveryExecutionError("PubMed split count mismatch")
            return {
                **common,
                "cell_type": "split_parent",
                "retrieved_count": 0,
                "children": children,
            }

        pages: list[dict[str, object]] = []
        page_finals: list[Path] = []
        retrieved = 0
        try:
            for retstart in range(0, count, 200):
                retmax = min(200, count - retstart)
                page_data = request(
                    PUBMED_EFETCH_URL,
                    {
                        "db": "pubmed",
                        "retmode": "xml",
                        "rettype": "abstract",
                        "WebEnv": webenv,
                        "query_key": query_key,
                        "retstart": retstart,
                        "retmax": retmax,
                        "tool": TOOL_NAME,
                        "email": email,
                    },
                )
                _, parsed_count = _parse_pubmed_page(page_data)
                page_path = raw_dir / (
                    f"{current.search_id}.efetch.{retstart:09d}-"
                    f"{retstart + retmax - 1:09d}.xml"
                )
                digest = _atomic_bytes(
                    page_path, page_data, lambda data: _parse_pubmed_page(data)
                )
                page_finals.append(page_path)
                pages.append(
                    {
                        "retstart": retstart,
                        "retmax": retmax,
                        "path": page_path.relative_to(output_dir).as_posix(),
                        "sha256": digest,
                        "parsed_count": parsed_count,
                    }
                )
                retrieved += parsed_count
            if retrieved != count:
                raise DiscoveryExecutionError(
                    f"PubMed count mismatch: reported {count}, retrieved {retrieved}"
                )
        except BaseException:
            entries = _read_manifest_entries(output_dir)
            for path in page_finals:
                entries.pop(path.relative_to(output_dir).as_posix(), None)
                path.unlink(missing_ok=True)
            _write_manifest_entries(output_dir, entries)
            raise
        for page in pages:
            _manifest_artifact(
                output_dir,
                output_dir / str(page["path"]),
                str(page["sha256"]),
            )
        return {
            **common,
            "cell_type": "leaf",
            "usehistory": True,
            "webenv": webenv,
            "query_key": query_key,
            "retrieved_count": retrieved,
            "efetch_pages": pages,
        }

    return execute_interval(cell)


def _tree_artifact_receipts(cell: object) -> list[tuple[str, str, str]]:
    if not isinstance(cell, dict):
        return []
    artifacts: list[tuple[str, str, str]] = []
    if isinstance(cell.get("esearch_path"), str) and isinstance(
        cell.get("esearch_sha256"), str
    ):
        artifacts.append(
            (str(cell["esearch_path"]), str(cell["esearch_sha256"]), "esearch")
        )
    if cell.get("cell_type") == "leaf":
        pages = cell.get("efetch_pages")
        if isinstance(pages, list):
            for page in pages:
                if isinstance(page, dict) and isinstance(page.get("path"), str) and isinstance(
                    page.get("sha256"), str
                ):
                    artifacts.append((str(page["path"]), str(page["sha256"]), "page"))
    elif cell.get("cell_type") == "split_parent":
        children = cell.get("children")
        if isinstance(children, list):
            for child in children:
                artifacts.extend(_tree_artifact_receipts(child))
    return artifacts


def _resumable_root_matches(
    expected: SearchCell,
    existing: object,
    output_dir: Path,
) -> bool:
    if not isinstance(existing, dict):
        return False
    for field in (
        "search_id", "lane", "family", "query", "parent_search_id", "date_start",
        "date_end",
    ):
        if existing.get(field) != getattr(expected, field):
            return False
    if existing.get("status") != "complete":
        return False
    artifacts = _tree_artifact_receipts(existing)
    if not artifacts:
        return False
    manifest = _read_manifest_entries(output_dir)
    for relative, expected_sha, kind in artifacts:
        safe = _safe_relative(relative)
        if safe is None or manifest.get(safe) != expected_sha:
            return False
        try:
            artifact_bytes, confined_error = _confined_artifact_bytes(
                output_dir, safe, f"resumable {kind}"
            )
            if confined_error is not None or artifact_bytes is None:
                return False
            if hashlib.sha256(artifact_bytes).hexdigest() != expected_sha:
                return False
            if kind == "page":
                _parse_pubmed_page(artifact_bytes)
        except (OSError, DiscoveryExecutionError):
            return False
    leaves = _leaf_receipts([existing])
    if not leaves:
        return False
    for leaf in leaves:
        pages = leaf.get("efetch_pages")
        if not isinstance(pages, list):
            return False
        parsed = sum(
            int(page.get("parsed_count", -1))
            for page in pages
            if isinstance(page, dict)
        )
        if parsed != leaf.get("reported_count") or parsed != leaf.get("retrieved_count"):
            return False
    return not _validate_cell(
        output_dir,
        existing,
        manifest,
        set(),
        set(),
        set(),
        set(),
        expected.source,
    )


def _remove_root_artifacts(output_dir: Path, root_search_id: str) -> None:
    prefix = root_search_id.rsplit("-", 1)[0] + "-"
    entries = _read_manifest_entries(output_dir)
    raw = output_dir / "raw"
    if raw.is_dir():
        for path in raw.iterdir():
            if path.is_file() and (
                path.name.startswith(prefix)
                or (path.name.startswith(f".{prefix}") and path.name.endswith(".tmp"))
            ):
                try:
                    relative = path.relative_to(output_dir).as_posix()
                except ValueError:
                    continue
                entries.pop(relative, None)
                path.unlink(missing_ok=True)
    _write_manifest_entries(output_dir, entries)


def _configuration_receipts(root: Path, extra: Sequence[Path] = ()) -> list[dict[str, str]]:
    receipts: list[dict[str, str]] = []
    for relative in (PROTOCOL_PATH, QUERY_CONFIG_PATH, JOURNAL_REGISTRY_PATH, *extra):
        path = root / relative
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as error:
            raise DiscoveryExecutionError(f"configuration file missing: {relative}") from error
        receipts.append({"path": Path(relative).as_posix(), "sha256": digest})
    return receipts


def _write_json_atomic(path: Path, payload: object) -> None:
    _atomic_bytes(
        path,
        (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    )


def execute_pubmed_run(
    root: Path,
    cells: Sequence[SearchCell],
    output_dir: Path,
    email: str,
    api_key: str | None = None,
    opener: Callable[..., object] = urllib.request.urlopen,
    extra_configuration: Sequence[Path] = (),
    empty_reason: str = "",
) -> dict[str, object]:
    """Execute root cells, preserving verified roots and restarting invalid roots."""
    root = Path(root)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    receipt_path = output_dir / "RUN_RECEIPT.json"
    existing_cells: dict[str, dict[str, object]] = {}
    existing_executed_at = ""
    if receipt_path.is_file():
        try:
            existing = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError, UnicodeError):
            existing = None
        if isinstance(existing, dict) and isinstance(existing.get("cells"), list):
            existing_executed_at = str(existing.get("executed_at", ""))
            existing_cells = {
                str(item.get("search_id")): item
                for item in existing["cells"]
                if isinstance(item, dict) and isinstance(item.get("search_id"), str)
            }
    completed: list[dict[str, object]] = []
    executed_at = existing_executed_at or datetime.now(ZoneInfo("Asia/Shanghai")).isoformat()
    receipt: dict[str, object] = {
        "schema_version": 1,
        "executed_at": executed_at,
        "timezone": "Asia/Shanghai",
        "tool_version": TOOL_VERSION,
        "source": "pubmed",
        "configuration_files": _configuration_receipts(root, extra_configuration),
        "cells": completed,
    }
    if empty_reason:
        receipt["empty_reason"] = empty_reason
    paced_opener = _PacedOpener(opener, 0.11 if api_key else 0.34)
    for cell in cells:
        old = existing_cells.get(cell.search_id)
        if _resumable_root_matches(cell, old, output_dir):
            completed.append(old)
        else:
            _remove_root_artifacts(output_dir, cell.search_id)
            completed.append(
                execute_pubmed_cell(
                    cell,
                    output_dir,
                    email,
                    api_key=api_key,
                    opener=paced_opener,
                )
            )
        _write_json_atomic(receipt_path, receipt)
    if not cells:
        _write_json_atomic(receipt_path, receipt)
    compile_pubmed_candidates(output_dir)
    return receipt


def resolve_crossref_candidates(
    query_id: str,
    bibliographic_query: str,
    output_dir: Path,
    email: str,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> dict[str, object]:
    """Freeze one bounded Crossref bibliographic candidate response."""
    output_dir = Path(output_dir)
    data = _urlopen_bytes(
        opener,
        CROSSREF_WORKS_URL,
        {
            "query.bibliographic": bibliographic_query,
            "rows": 5,
            "select": "DOI,title,published,container-title,author,type,URL",
            "mailto": email,
        },
    )
    try:
        payload = json.loads(data.decode("utf-8"))
        message = payload["message"]
        items = message["items"]
        total_results = int(message["total-results"])
    except (UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise DiscoveryExecutionError("malformed Crossref response JSON") from error
    if (
        not isinstance(message, dict)
        or not isinstance(items, list)
        or len(items) > 5
        or not all(isinstance(item, dict) for item in items)
        or total_results < 0
    ):
        raise DiscoveryExecutionError("malformed Crossref response JSON")
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", query_id)
    response_path = output_dir / "raw" / f"{safe_id}.crossref.json"
    digest = _atomic_bytes(
        response_path,
        data,
        lambda raw: json.loads(raw.decode("utf-8")),
    )
    _manifest_artifact(output_dir, response_path, digest)
    relative = response_path.relative_to(output_dir).as_posix()
    return {
        "query_id": query_id,
        "source": "crossref",
        "query": bibliographic_query,
        "reported_count": total_results,
        "raw_path": relative,
        "raw_sha256": digest,
        "status": "complete",
        "response_path": relative,
        "response_sha256": digest,
        "returned_candidate_count": len(items),
        "total_results": total_results,
        "rows": 5,
    }


def _validate_wave_two_registry(
    path: Path,
    root: Path | None = None,
) -> tuple[list[dict[str, str]], list[str]]:
    headers, rows, errors = _read_csv(path, "invalid Wave 2 query registry")
    if errors:
        return rows, errors
    if headers != list(WAVE_TWO_QUERY_HEADERS):
        return rows, ["Wave 2 query registry header mismatch"]
    families = [row.get("family", "") for row in rows]
    if len(rows) != len(FAMILIES) or set(families) != FAMILIES or len(families) != len(
        set(families)
    ):
        errors.append("Wave 2 family set mismatch")
    seen_ids: set[str] = set()
    infectious_block = ""
    frozen_date_start = ""
    frozen_date_end = ""
    if root is not None:
        config_object, config_errors = _read_json(
            Path(root) / QUERY_CONFIG_PATH, "invalid discovery query JSON"
        )
        errors.extend(config_errors)
        if isinstance(config_object, dict) and isinstance(
            config_object.get("infectious_disease_block"), str
        ):
            infectious_block = str(config_object["infectious_disease_block"])
            frozen_date_start = str(config_object.get("applied_date_start", ""))
            frozen_date_end = str(config_object.get("applied_date_end", ""))
    for row in rows:
        family = row.get("family", "")
        status_value = row.get("status", "")
        if status_value not in {"executed", "no_expansion_needed"}:
            errors.append(f"invalid Wave 2 status: {family}")
            continue
        if not row.get("rationale", "").strip() or not row.get(
            "source_candidate_keys", ""
        ).strip() or not row.get("reviewer", "").strip():
            errors.append(f"incomplete Wave 2 rationale provenance: {family}")
        execution_fields = (
            "search_id", "source", "query", "date_start", "date_end"
        )
        if status_value == "executed":
            if any(not row.get(field, "").strip() for field in execution_fields) or not row.get(
                "new_synonyms", ""
            ).strip():
                errors.append(f"incomplete executed Wave 2 row: {family}")
            if row.get("source") != "pubmed":
                errors.append(f"invalid Wave 2 source: {family}")
            search_id = row.get("search_id", "")
            if search_id in seen_ids:
                errors.append("duplicate Wave 2 search_id")
            seen_ids.add(search_id)
            expected_token = FAMILY_TOKENS.get(family, "")
            if re.fullmatch(
                rf"SEARCH-\d{{8}}-PUBMED-(?:FAMILY|VENUE)-"
                rf"{re.escape(expected_token)}-\d{{2}}",
                search_id,
            ) is None:
                errors.append(f"Wave 2 search_id family mismatch: {family}")
            start = _parse_date(row.get("date_start"))
            end = _parse_date(row.get("date_end"))
            if start is None or end is None or start > end:
                errors.append(f"invalid Wave 2 date interval: {family}")
            if (
                frozen_date_start
                and frozen_date_end
                and (
                    row.get("date_start") != frozen_date_start
                    or row.get("date_end") != frozen_date_end
                )
            ):
                errors.append(f"Wave 2 frozen date interval mismatch: {family}")
            if _query_date_interval(row.get("query")) != (
                row.get("date_start"),
                row.get("date_end"),
            ):
                errors.append(f"Wave 2 query date mismatch: {family}")
            if infectious_block and infectious_block not in row.get("query", ""):
                errors.append(f"Wave 2 infectious block mismatch: {family}")
        elif any(row.get(field, "") for field in (*execution_fields, "new_synonyms")):
            errors.append(f"no-expansion Wave 2 row contains execution field: {family}")
    return rows, list(dict.fromkeys(errors))


def _write_header_only_csv(path: Path, headers: Sequence[str]) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{time.time_ns()}.tmp")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with temporary.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerow(headers)
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def execute_wave(
    root: Path,
    query_registry: Path,
    output_dir: Path,
    email: str,
    api_key: str | None = None,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> dict[str, object]:
    """Validate and execute the bounded Wave 2 synonym registry."""
    root = Path(root)
    query_registry = Path(query_registry)
    output_dir = Path(output_dir)
    rows, errors = _validate_wave_two_registry(query_registry, root)
    if errors:
        raise DiscoveryExecutionError("; ".join(errors))
    try:
        registry_relative_root = query_registry.relative_to(root)
        query_registry.relative_to(output_dir)
    except ValueError as error:
        raise DiscoveryExecutionError("Wave 2 registry must be inside the Library run") from error
    cells = [
        SearchCell(
            search_id=row["search_id"],
            lane="FAMILY",
            family=row["family"],
            source="pubmed",
            query=row["query"],
            parent_search_id="",
            date_start=row["date_start"],
            date_end=row["date_end"],
        )
        for row in sorted(rows, key=lambda item: item["family"])
        if row["status"] == "executed"
    ]
    empty_reason = "all_families_no_expansion_needed" if not cells else ""
    receipt = execute_pubmed_run(
        root,
        cells,
        output_dir,
        email,
        api_key=api_key,
        opener=opener,
        extra_configuration=(registry_relative_root,),
        empty_reason=empty_reason,
    )
    _manifest_artifact(
        output_dir,
        query_registry,
        hashlib.sha256(query_registry.read_bytes()).hexdigest(),
    )
    if not cells:
        for filename, headers in (
            ("screened_candidates.csv", SCREENED_HEADERS),
            ("screening_audit.csv", AUDIT_HEADERS),
        ):
            path = output_dir / filename
            _write_header_only_csv(path, headers)
            _manifest_artifact(
                output_dir, path, hashlib.sha256(path.read_bytes()).hexdigest()
            )
    return receipt


def _empty_wave_contract_errors(run_dir: Path) -> list[str] | None:
    receipt_path = run_dir / "RUN_RECEIPT.json"
    if not receipt_path.is_file():
        return None
    payload, read_errors = _read_json(receipt_path, "invalid run receipt")
    if read_errors or not isinstance(payload, dict):
        return None
    declared = payload.get("empty_reason") == "all_families_no_expansion_needed"
    if not declared:
        return None
    errors: list[str] = []
    if payload.get("cells") != []:
        errors.append("empty Wave 2 contains search cells")
    raw = run_dir / "raw"
    if raw.exists() and (not raw.is_dir() or any(raw.iterdir())):
        errors.append("empty Wave 2 contains raw artifacts")
    manifest_errors, manifest = _validate_manifest(run_dir)
    errors.extend(manifest_errors)
    required = {
        "QUERY_REGISTRY.csv",
        "compiled_candidates_raw.csv",
        "screened_candidates.csv",
        "screening_audit.csv",
    }
    if not required.issubset(manifest):
        errors.append("empty Wave 2 manifest coverage mismatch")
    if any(path.startswith("raw/") for path in manifest):
        errors.append("empty Wave 2 manifest contains raw artifact")
    rows, registry_errors = _validate_wave_two_registry(
        run_dir / "QUERY_REGISTRY.csv", _configuration_root(run_dir)
    )
    errors.extend(registry_errors)
    if rows and any(row.get("status") != "no_expansion_needed" for row in rows):
        errors.append("empty Wave 2 registry contains executed row")
    for filename, headers in (
        ("compiled_candidates_raw.csv", COMPILED_HEADERS),
        ("screened_candidates.csv", SCREENED_HEADERS),
        ("screening_audit.csv", AUDIT_HEADERS),
    ):
        received_headers, rows, csv_errors = _read_csv(
            run_dir / filename, f"invalid empty Wave 2 {filename}"
        )
        errors.extend(csv_errors)
        if received_headers != list(headers) or rows:
            errors.append(f"empty Wave 2 table mismatch: {filename}")
    return list(dict.fromkeys(errors))


def _validate_lineage_registry(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    headers, rows, errors = _read_csv(path, "invalid lineage query registry")
    if errors:
        return rows, errors
    if headers != list(LINEAGE_REGISTRY_HEADERS):
        return rows, ["lineage query registry header mismatch"]
    if not rows:
        errors.append("lineage query registry is empty")
    seen_queries: set[str] = set()
    groups: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        query_id = row.get("query_id", "")
        named_source_id = row.get("named_source_id", "")
        family = row.get("family", "")
        if not query_id or query_id in seen_queries:
            errors.append("duplicate or blank lineage registry query_id")
        else:
            seen_queries.add(query_id)
        token = FAMILY_TOKENS.get(family, "")
        if not token or re.fullmatch(
            rf"SEARCH-\d{{8}}-LINEAGE-{re.escape(token)}-\d{{2}}", query_id
        ) is None:
            errors.append(f"invalid lineage query_id: {query_id}")
        if not named_source_id:
            errors.append("blank lineage named_source_id")
        groups.setdefault(named_source_id, []).append(row)
        if family not in FAMILIES:
            errors.append(f"invalid lineage family: {query_id}")
        if row.get("source") not in LINEAGE_SOURCES:
            errors.append(f"invalid lineage source: {query_id}")
        if row.get("query_variant") not in LINEAGE_QUERY_VARIANTS:
            errors.append(f"invalid lineage query variant: {query_id}")
        if row.get("source_role") not in LINEAGE_SOURCE_ROLES:
            errors.append(f"invalid lineage source role: {query_id}")
        for field in (
            "method_label", "canonical_name", "query", "seed_candidate_keys", "reviewer"
        ):
            if not row.get(field, "").strip():
                errors.append(f"blank lineage registry field: {query_id}: {field}")
    for named_source_id, group in groups.items():
        if len(group) > 3:
            errors.append(
                f"lineage named source has over three queries: {named_source_id}"
            )
        variants = [row.get("query_variant", "") for row in group]
        if len(variants) != len(set(variants)):
            errors.append(f"duplicate lineage query variant: {named_source_id}")
        try:
            ranks = [LINEAGE_QUERY_VARIANTS.index(variant) for variant in variants]
        except ValueError:
            ranks = []
        if ranks and ranks != sorted(ranks):
            errors.append(f"lineage query variants out of order: {named_source_id}")
        for field in ("method_label", "canonical_name", "family", "source_role"):
            if len({row.get(field, "") for row in group}) != 1:
                errors.append(f"lineage named source field mismatch: {named_source_id}: {field}")
    return rows, list(dict.fromkeys(errors))


def _execute_pubmed_lineage_query(
    query_id: str,
    query: str,
    output_dir: Path,
    email: str,
    api_key: str | None,
    opener: Callable[..., object],
) -> dict[str, object]:
    request_number = 0

    def request(endpoint: str, parameters: dict[str, object]) -> bytes:
        nonlocal request_number
        if request_number and not getattr(opener, "_discovery_handles_pacing", False):
            time.sleep(0.11 if api_key else 0.34)
        request_number += 1
        if api_key:
            parameters = {**parameters, "api_key": api_key}
        return _urlopen_bytes(opener, endpoint, parameters)

    esearch_data = request(
        PUBMED_ESEARCH_URL,
        {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": 0,
            "usehistory": "y",
            "tool": TOOL_NAME,
            "email": email,
        },
    )
    count, webenv, query_key = _parse_esearch(esearch_data)
    esearch_path = output_dir / "raw" / f"{query_id}.esearch.json"
    esearch_sha = _atomic_bytes(
        esearch_path, esearch_data, lambda raw: _parse_esearch(raw)
    )
    _manifest_artifact(output_dir, esearch_path, esearch_sha)
    if count >= 10000:
        raise DiscoveryExecutionError("overbroad lineage identity query")
    pages: list[dict[str, object]] = []
    page_finals: list[Path] = []
    retrieved = 0
    try:
        for retstart in range(0, count, 200):
            retmax = min(200, count - retstart)
            data = request(
                PUBMED_EFETCH_URL,
                {
                    "db": "pubmed",
                    "retmode": "xml",
                    "rettype": "abstract",
                    "WebEnv": webenv,
                    "query_key": query_key,
                    "retstart": retstart,
                    "retmax": retmax,
                    "tool": TOOL_NAME,
                    "email": email,
                },
            )
            _, parsed_count = _parse_pubmed_page(data)
            page_path = output_dir / "raw" / (
                f"{query_id}.efetch.{retstart:09d}-{retstart + retmax - 1:09d}.xml"
            )
            page_sha = _atomic_bytes(
                page_path, data, lambda raw: _parse_pubmed_page(raw)
            )
            page_finals.append(page_path)
            pages.append(
                {
                    "retstart": retstart,
                    "retmax": retmax,
                    "path": page_path.relative_to(output_dir).as_posix(),
                    "sha256": page_sha,
                    "parsed_count": parsed_count,
                }
            )
            retrieved += parsed_count
        if retrieved != count:
            raise DiscoveryExecutionError(
                f"PubMed count mismatch: reported {count}, retrieved {retrieved}"
            )
    except BaseException:
        entries = _read_manifest_entries(output_dir)
        for page_path in page_finals:
            entries.pop(page_path.relative_to(output_dir).as_posix(), None)
            page_path.unlink(missing_ok=True)
        _write_manifest_entries(output_dir, entries)
        raise
    for page in pages:
        _manifest_artifact(
            output_dir, output_dir / str(page["path"]), str(page["sha256"])
        )
    relative = esearch_path.relative_to(output_dir).as_posix()
    return {
        "query_id": query_id,
        "source": "pubmed",
        "query": query,
        "reported_count": count,
        "raw_path": relative,
        "raw_sha256": esearch_sha,
        "status": "complete",
        "date_start": "",
        "date_end": "",
        "query_scope": "unbounded_identity",
        "esearch_path": relative,
        "esearch_sha256": esearch_sha,
        "usehistory": True,
        "webenv": webenv,
        "query_key": query_key,
        "efetch_pages": pages,
    }


def _write_rows_atomic(
    path: Path,
    headers: Sequence[str],
    rows: Sequence[dict[str, str]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{time.time_ns()}.tmp")
    try:
        with temporary.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _pubmed_lineage_candidate_rows(
    registry: dict[str, str],
    receipt: dict[str, object],
    output_dir: Path,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    rank = 0
    for page in receipt.get("efetch_pages", []):
        if not isinstance(page, dict):
            continue
        relative = str(page.get("path", ""))
        page_bytes, confined_error = _confined_artifact_bytes(
            output_dir, relative, "PubMed lineage raw"
        )
        if confined_error is not None or page_bytes is None:
            raise DiscoveryExecutionError(
                confined_error or f"PubMed lineage raw missing: {relative}"
            )
        root, _ = _parse_pubmed_page(page_bytes)
        for record in root:
            if record.tag.rsplit("}", 1)[-1] not in {
                "PubmedArticle", "PubmedBookArticle"
            }:
                continue
            rank += 1
            fields = _pubmed_record_fields(record)
            key, _ = _candidate_key(fields)
            rows.append(
                {
                    "candidate_key": key,
                    "query_id": registry["query_id"],
                    "named_source_id": registry["named_source_id"],
                    "candidate_rank": str(rank),
                    "pmid": fields["pmid"],
                    "doi": fields["doi"],
                    "title": fields["title"],
                    "year": fields["year"],
                    "journal": fields["journal"],
                    "authors": fields["authors"],
                    "source_url": (
                        f"https://pubmed.ncbi.nlm.nih.gov/{fields['pmid']}/"
                        if fields["pmid"]
                        else f"https://doi.org/{fields['doi']}" if fields["doi"] else ""
                    ),
                    "raw_path": str(page["path"]),
                    "raw_sha256": str(page["sha256"]),
                }
            )
    return rows


def _crossref_lineage_candidate_rows(
    registry: dict[str, str],
    receipt: dict[str, object],
    output_dir: Path,
) -> list[dict[str, str]]:
    relative = str(receipt.get("response_path", ""))
    response_bytes, confined_error = _confined_artifact_bytes(
        output_dir, relative, "Crossref lineage raw"
    )
    if confined_error is not None or response_bytes is None:
        raise DiscoveryExecutionError(
            confined_error or f"Crossref lineage raw missing: {relative}"
        )
    try:
        payload = json.loads(response_bytes.decode("utf-8"))
        items = payload["message"]["items"]
    except (UnicodeError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise DiscoveryExecutionError("malformed Crossref response JSON") from error
    if not isinstance(items, list):
        raise DiscoveryExecutionError("malformed Crossref response JSON")
    rows: list[dict[str, str]] = []
    for rank, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise DiscoveryExecutionError(
                f"invalid Crossref candidate item: {rank}"
            )
        doi = _normalize_doi(str(item.get("DOI", "")))
        titles = item.get("title", [])
        containers = item.get("container-title", [])
        authors = item.get("author", [])
        date_parts = item.get("published", {}).get("date-parts", []) if isinstance(
            item.get("published"), dict
        ) else []
        title = _normalize_whitespace(str(titles[0])) if isinstance(titles, list) and titles else ""
        container = _normalize_whitespace(str(containers[0])) if isinstance(
            containers, list
        ) and containers else ""
        first_author = ""
        if isinstance(authors, list) and authors and isinstance(authors[0], dict):
            first_author = _normalize_whitespace(
                " ".join(
                    str(authors[0].get(field, ""))
                    for field in ("given", "family")
                    if authors[0].get(field)
                )
            )
        year = ""
        if (
            isinstance(date_parts, list)
            and date_parts
            and isinstance(date_parts[0], list)
            and date_parts[0]
        ):
            year = str(date_parts[0][0])
        key = f"DOI:{doi}" if doi else f"CROSSREF:{registry['query_id']}:{rank:03d}"
        rows.append(
            {
                "candidate_key": key,
                "query_id": registry["query_id"],
                "named_source_id": registry["named_source_id"],
                "bibliographic_query": registry["query"],
                "candidate_rank": str(rank),
                "doi": doi,
                "title": title,
                "year": year,
                "container_title": container,
                "first_author": first_author,
                "type": str(item.get("type", "")),
                "url": str(item.get("URL", "")),
                "raw_path": str(receipt["response_path"]),
                "raw_sha256": str(receipt["response_sha256"]),
            }
        )
    return rows


def _lineage_query_resumable(
    registry: dict[str, str],
    receipt: object,
    output_dir: Path,
) -> bool:
    if not isinstance(receipt, dict):
        return False
    for field in ("query_id", "source", "query"):
        if receipt.get(field) != registry.get(field):
            return False
    if receipt.get("status") != "complete" or not _integer(
        receipt.get("reported_count")
    ):
        return False
    manifest = _read_manifest_entries(output_dir)
    raw_path = _safe_relative(receipt.get("raw_path"))
    raw_sha = receipt.get("raw_sha256")
    if (
        raw_path is None
        or not isinstance(raw_sha, str)
        or manifest.get(raw_path) != raw_sha
    ):
        return False
    raw_data, confined_error = _confined_artifact_bytes(
        output_dir, raw_path, "lineage resume raw"
    )
    if confined_error is not None or raw_data is None:
        return False
    if hashlib.sha256(raw_data).hexdigest() != raw_sha:
        return False
    count = int(receipt["reported_count"])
    if registry["source"] == "crossref":
        prohibited = {
            "esearch_path", "esearch_sha256", "usehistory", "webenv",
            "query_key", "efetch_pages",
        }
        if prohibited & set(receipt):
            return False
        if (
            receipt.get("response_path") != raw_path
            or receipt.get("response_sha256") != raw_sha
            or receipt.get("rows") != 5
        ):
            return False
        try:
            payload = json.loads(raw_data.decode("utf-8"))
            message = payload["message"]
            items = message["items"]
            total = int(message["total-results"])
        except (UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            return False
        return (
            isinstance(items, list)
            and len(items) <= 5
            and receipt.get("returned_candidate_count") == len(items)
            and receipt.get("total_results") == total
            and count == total
        )
    if registry["source"] != "pubmed":
        return False
    try:
        raw_count, raw_webenv, raw_query_key = _parse_esearch(raw_data)
    except DiscoveryExecutionError:
        return False
    if (
        count >= 10000
        or raw_count != count
        or receipt.get("raw_path") != receipt.get("esearch_path")
        or receipt.get("raw_sha256") != receipt.get("esearch_sha256")
        or receipt.get("date_start") != ""
        or receipt.get("date_end") != ""
        or receipt.get("query_scope") != "unbounded_identity"
        or receipt.get("usehistory") is not True
        or receipt.get("webenv") != raw_webenv
        or receipt.get("query_key") != raw_query_key
    ):
        return False
    return not _validate_pages(
        output_dir,
        receipt.get("efetch_pages"),
        count,
        manifest,
        set(),
        {raw_path},
    )


def _remove_lineage_query_artifacts(output_dir: Path, query_id: str) -> None:
    entries = _read_manifest_entries(output_dir)
    raw_dir = output_dir / "raw"
    if raw_dir.is_dir():
        for path in raw_dir.iterdir():
            if path.is_file() and (
                path.name.startswith(query_id)
                or (path.name.startswith(f".{query_id}") and path.name.endswith(".tmp"))
            ):
                entries.pop(path.relative_to(output_dir).as_posix(), None)
                path.unlink(missing_ok=True)
    _write_manifest_entries(output_dir, entries)


def _publish_lineage_candidate_tables(
    output_dir: Path,
    pubmed_candidates: Sequence[dict[str, str]],
    crossref_candidates: Sequence[dict[str, str]],
) -> None:
    for filename, headers, candidate_rows in (
        ("pubmed_lineage_candidates.csv", PUBMED_LINEAGE_HEADERS, pubmed_candidates),
        ("crossref_candidates.csv", CROSSREF_LINEAGE_HEADERS, crossref_candidates),
    ):
        path = output_dir / filename
        _write_rows_atomic(path, headers, candidate_rows)
        _manifest_artifact(
            output_dir, path, hashlib.sha256(path.read_bytes()).hexdigest()
        )


def execute_lineage(
    root: Path,
    query_registry: Path,
    output_dir: Path,
    email: str,
    api_key: str | None = None,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> dict[str, object]:
    """Execute a frozen heterogeneous lineage identity query registry."""
    root = Path(root)
    query_registry = Path(query_registry)
    output_dir = Path(output_dir)
    rows, errors = _validate_lineage_registry(query_registry)
    if errors:
        raise DiscoveryExecutionError("; ".join(errors))
    try:
        registry_relative_root = query_registry.relative_to(root)
    except ValueError as error:
        raise DiscoveryExecutionError("lineage registry must be inside the Library") from error
    output_dir.mkdir(parents=True, exist_ok=True)
    receipt_path = output_dir / "LINEAGE_RUN_RECEIPT.json"
    existing_queries: dict[str, dict[str, object]] = {}
    existing_executed_at = ""
    if receipt_path.is_file():
        try:
            existing_payload = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            existing_payload = None
        if isinstance(existing_payload, dict) and isinstance(
            existing_payload.get("queries"), list
        ):
            existing_executed_at = str(existing_payload.get("executed_at", ""))
            existing_queries = {
                str(item.get("query_id")): item
                for item in existing_payload["queries"]
                if isinstance(item, dict) and isinstance(item.get("query_id"), str)
            }
    _manifest_artifact(
        output_dir,
        query_registry,
        hashlib.sha256(query_registry.read_bytes()).hexdigest(),
    )
    queries: list[dict[str, object]] = []
    pubmed_candidates: list[dict[str, str]] = []
    crossref_candidates: list[dict[str, str]] = []
    receipt: dict[str, object] = {
        "schema_version": 1,
        "executed_at": existing_executed_at
        or datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "timezone": "Asia/Shanghai",
        "tool_version": TOOL_VERSION,
        "configuration_files": _configuration_receipts(
            root, (registry_relative_root,)
        ),
        "queries": queries,
    }
    paced_opener = _PacedOpener(opener, 0.11 if api_key else 0.34)
    _publish_lineage_candidate_tables(
        output_dir, pubmed_candidates, crossref_candidates
    )
    _write_json_atomic(receipt_path, receipt)
    for row in rows:
        old = existing_queries.get(row["query_id"])
        if _lineage_query_resumable(row, old, output_dir):
            query_receipt = old
        else:
            _remove_lineage_query_artifacts(output_dir, row["query_id"])
            if row["source"] == "pubmed":
                query_receipt = _execute_pubmed_lineage_query(
                    row["query_id"],
                    row["query"],
                    output_dir,
                    email,
                    api_key,
                    paced_opener,
                )
            else:
                query_receipt = resolve_crossref_candidates(
                    row["query_id"],
                    row["query"],
                    output_dir,
                    email,
                    opener=paced_opener,
                )
        if row["source"] == "pubmed":
            pubmed_candidates.extend(
                _pubmed_lineage_candidate_rows(row, query_receipt, output_dir)
            )
        else:
            crossref_candidates.extend(
                _crossref_lineage_candidate_rows(row, query_receipt, output_dir)
            )
        queries.append(query_receipt)
        _publish_lineage_candidate_tables(
            output_dir, pubmed_candidates, crossref_candidates
        )
        _write_json_atomic(receipt_path, receipt)
    return receipt


def _text(element: ET.Element, path: str) -> str:
    found = element.find(path)
    return "" if found is None else "".join(found.itertext()).strip()


def _normalize_whitespace(value: str) -> str:
    return " ".join(value.split())


def _normalize_title(value: str) -> str:
    return _normalize_whitespace(unicodedata.normalize("NFKC", value)).casefold()


def _normalize_doi(value: str) -> str:
    normalized = value.strip().casefold()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix):]
    return normalized.strip()


def _pubmed_record_fields(record: ET.Element) -> dict[str, str]:
    pmid = _normalize_whitespace(_text(record, ".//PMID"))
    doi = ""
    for item in record.findall(".//ArticleId"):
        if str(item.attrib.get("IdType", "")).casefold() == "doi":
            doi = _normalize_doi("".join(item.itertext()))
            break
    if not doi:
        for item in record.findall(".//ELocationID"):
            if str(item.attrib.get("EIdType", "")).casefold() == "doi":
                doi = _normalize_doi("".join(item.itertext()))
                break
    title = _normalize_whitespace(_text(record, ".//ArticleTitle"))
    year = _normalize_whitespace(_text(record, ".//PubDate/Year"))
    if not year:
        medline_date = _text(record, ".//PubDate/MedlineDate")
        matched = re.search(r"(?:19|20)\d{2}", medline_date)
        year = matched.group(0) if matched else ""
    journal = _normalize_whitespace(
        _text(record, ".//Journal/Title") or _text(record, ".//Journal/ISOAbbreviation")
    )
    authors: list[str] = []
    for author in record.findall(".//AuthorList/Author"):
        collective = _normalize_whitespace(_text(author, "./CollectiveName"))
        personal = _normalize_whitespace(
            " ".join(
                part
                for part in (_text(author, "./ForeName"), _text(author, "./LastName"))
                if part
            )
        )
        if collective or personal:
            authors.append(collective or personal)
    abstract = _normalize_whitespace(
        " ".join("".join(item.itertext()) for item in record.findall(".//AbstractText"))
    )
    publication_types = sorted(
        {
            _normalize_whitespace("".join(item.itertext()))
            for item in record.findall(".//PublicationType")
            if _normalize_whitespace("".join(item.itertext()))
        }
    )
    return {
        "pmid": pmid,
        "doi": doi,
        "title": title,
        "year": year,
        "journal": journal,
        "authors": "; ".join(authors),
        "abstract": abstract,
        "publication_types": "|".join(publication_types),
    }


def _leaf_receipts(cells: object) -> list[dict[str, object]]:
    leaves: list[dict[str, object]] = []
    if not isinstance(cells, list):
        return leaves
    for cell in cells:
        if not isinstance(cell, dict):
            continue
        if cell.get("cell_type") == "leaf":
            leaves.append(cell)
        elif cell.get("cell_type") == "split_parent":
            leaves.extend(_leaf_receipts(cell.get("children")))
    return leaves


def _candidate_key(fields: dict[str, str]) -> tuple[str, str]:
    if fields["pmid"]:
        return f"PMID:{fields['pmid']}", "pmid"
    if fields["doi"]:
        return f"DOI:{fields['doi']}", "doi"
    fallback = "|".join(
        (_normalize_title(fields["title"]), fields["year"], _normalize_title(fields["journal"]))
    )
    return f"TITLE:{hashlib.sha256(fallback.encode()).hexdigest()[:16]}", "title_year_journal"


def _derive_pubmed_candidates(run_dir: Path) -> list[dict[str, str]]:
    """Purely derive deterministic candidates from receipt-owned manifested pages."""
    run_dir = Path(run_dir)
    try:
        receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as error:
        raise DiscoveryExecutionError("invalid run receipt for compilation") from error
    manifest = _read_manifest_entries(run_dir)
    observations: list[dict[str, str]] = []
    for leaf in _leaf_receipts(receipt.get("cells")):
        pages = leaf.get("efetch_pages")
        if not isinstance(pages, list):
            raise DiscoveryExecutionError("invalid EFetch page receipt for compilation")
        for page in pages:
            if not isinstance(page, dict) or _safe_relative(page.get("path")) is None:
                raise DiscoveryExecutionError("invalid EFetch page receipt for compilation")
            relative = str(page["path"])
            expected_sha = page.get("sha256")
            if (
                not isinstance(expected_sha, str)
                or manifest.get(relative) != expected_sha
            ):
                raise DiscoveryExecutionError(
                    f"compile input checksum mismatch: {relative}"
                )
            page_bytes, confined_error = _confined_artifact_bytes(
                run_dir, relative, "compile input"
            )
            if confined_error is not None or page_bytes is None:
                raise DiscoveryExecutionError(
                    confined_error or f"missing EFetch page for compilation: {relative}"
                )
            if hashlib.sha256(page_bytes).hexdigest() != expected_sha:
                raise DiscoveryExecutionError(
                    f"compile input checksum mismatch: {relative}"
                )
            root, _ = _parse_pubmed_page(page_bytes)
            for record in root:
                if record.tag.rsplit("}", 1)[-1] not in {"PubmedArticle", "PubmedBookArticle"}:
                    continue
                fields = _pubmed_record_fields(record)
                if not any(fields[field] for field in ("pmid", "doi", "title")):
                    continue
                fields.update(
                    search_ids=str(leaf.get("search_id", "")),
                    lanes=str(leaf.get("lane", "")),
                    preliminary_families=str(leaf.get("family", "")),
                )
                observations.append(fields)

    groups: list[list[dict[str, str]]] = []
    for observation in observations:
        matched_groups = [
            group
            for group in groups
            if any(
                (observation["pmid"] and observation["pmid"] == member["pmid"])
                or (observation["doi"] and observation["doi"] == member["doi"])
                for member in group
            )
        ]
        if not matched_groups:
            groups.append([observation])
            continue
        primary = matched_groups[0]
        primary.append(observation)
        for redundant in matched_groups[1:]:
            primary.extend(redundant)
            groups.remove(redundant)

    rows: list[dict[str, str]] = []
    for group in groups:
        representative = min(
            group,
            key=lambda item: (
                not bool(item["pmid"]),
                not bool(item["doi"]),
                _normalize_title(item["title"]),
            ),
        )
        fields = {
            name: representative[name]
            for name in (
                "pmid", "doi", "title", "year", "journal", "authors", "abstract",
                "publication_types",
            )
        }
        for provenance in ("search_ids", "lanes", "preliminary_families"):
            fields[provenance] = "|".join(
                sorted(
                    {
                        value
                        for item in group
                        for value in item[provenance].split("|")
                        if value
                    }
                )
            )
        key, basis = _candidate_key(fields)
        if len(group) > 1:
            pmids = [item["pmid"] for item in group if item["pmid"]]
            dois = [item["doi"] for item in group if item["doi"]]
            if len(pmids) != len(set(pmids)):
                basis = "pmid"
            elif len(dois) != len(set(dois)):
                basis = "doi"
        fields.update(
            candidate_key=key,
            source_url=(
                f"https://pubmed.ncbi.nlm.nih.gov/{fields['pmid']}/"
                if fields["pmid"]
                else f"https://doi.org/{fields['doi']}" if fields["doi"] else ""
            ),
            deduplication_basis=basis,
            possible_duplicate_group="",
        )
        rows.append(fields)

    by_title: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        normalized = _normalize_title(row["title"])
        if normalized:
            by_title.setdefault(normalized, []).append(row)
    for normalized, same_title in by_title.items():
        if len(same_title) > 1:
            group_id = f"TITLE-DUP:{hashlib.sha256(normalized.encode()).hexdigest()[:16]}"
            for row in same_title:
                row["possible_duplicate_group"] = group_id

    rows.sort(key=lambda item: item["candidate_key"])
    for row in rows:
        hash_fields = {header: row.get(header, "") for header in COMPILED_HEADERS if header != "row_sha256"}
        row["row_sha256"] = hashlib.sha256(
            json.dumps(
                hash_fields,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
    return rows


def _render_compiled_candidates(rows: Sequence[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=COMPILED_HEADERS)
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def compile_pubmed_candidates(run_dir: Path) -> list[dict[str, str]]:
    """Compile all manifested PubMed pages into a deterministic raw candidate table."""
    run_dir = Path(run_dir)
    rows = _derive_pubmed_candidates(run_dir)
    path = run_dir / "compiled_candidates_raw.csv"
    _atomic_bytes(path, _render_compiled_candidates(rows))
    _manifest_artifact(run_dir, path, hashlib.sha256(path.read_bytes()).hexdigest())
    return rows


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
            rows: list[dict[str, str]] = []
            errors: list[str] = []
            for row in reader:
                headers = reader.fieldnames or []
                if None in row or any(row.get(header) is None for header in headers):
                    errors.append(
                        f"CSV row width mismatch: {kind}: {path}: line {reader.line_num}"
                    )
                rows.append(
                    {
                        header: row.get(header)
                        if isinstance(row.get(header), str)
                        else ""
                        for header in headers
                    }
                )
            return reader.fieldnames, rows, errors
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
    for field in CONFIG_REQUIRED_FIELDS:
        if field not in config:
            errors.append(f"missing discovery configuration field: {field}")
    if config.get("schema_version") != 1:
        errors.append("invalid discovery configuration field: schema_version")
    for field in (
        "applied_date_start",
        "applied_date_end",
        "source",
        "family_method_field",
        "venue_method_field",
        "infectious_disease_block",
    ):
        if not isinstance(config.get(field), str) or not config.get(field, "").strip():
            errors.append(f"invalid discovery configuration field: {field}")
    if config.get("source") != "pubmed":
        errors.append("invalid discovery configuration field: source")
    if config.get("family_method_field") != "Title":
        errors.append("invalid discovery configuration field: family_method_field")
    if config.get("venue_method_field") != "Title/Abstract":
        errors.append("invalid discovery configuration field: venue_method_field")
    configured_dates = {
        field: _parse_date(config.get(field))
        for field in ("applied_date_start", "applied_date_end")
    }
    for field, parsed in configured_dates.items():
        if field in config and parsed is None:
            errors.append(f"invalid discovery configuration field: {field}")
    if (
        configured_dates["applied_date_start"] is not None
        and configured_dates["applied_date_end"] is not None
        and configured_dates["applied_date_start"]
        > configured_dates["applied_date_end"]
    ):
        errors.append("discovery configuration date range inverted")
    families = config.get("families")
    if not isinstance(families, list):
        errors.append("invalid discovery configuration field: families")
        families = []
    names = {
        row.get("family")
        for row in families
        if isinstance(row, dict) and isinstance(row.get("family"), str)
    }
    if names != FAMILIES or len(families) != len(FAMILIES):
        errors.append("family set mismatch")
    for family in families:
        if (
            not isinstance(family, dict)
            or set(family) != {"family", "token", "method_block"}
            or any(
                not isinstance(family.get(field), str)
                or not family.get(field, "").strip()
                for field in ("family", "token", "method_block")
            )
        ):
            errors.append("malformed family configuration")
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

    active_rows = [row for row in journals if (row.get("status") or "").strip() == "active"]
    if len(journals) != 22 or len(active_rows) != 22:
        errors.append("journal registry must contain exactly 22 active rows")
    titles = {(row.get("title") or "").strip() for row in journals}
    if titles != APPROVED_JOURNAL_TITLES:
        errors.append("approved journal title set mismatch")
    seen_ids: set[str] = set()
    seen_tokens: set[str] = set()
    for row in journals:
        status_value = (row.get("status") or "").strip()
        if status_value not in JOURNAL_STATUSES:
            errors.append("invalid journal status")
        journal_id = (row.get("journal_id") or "").strip()
        if JOURNAL_ID_PATTERN.fullmatch(journal_id) is None:
            errors.append("invalid journal_id")
        elif journal_id in seen_ids:
            errors.append("duplicate journal_id")
        else:
            seen_ids.add(journal_id)
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
    except Exception as error:
        errors.append(
            "unable to build search cells: "
            f"{type(error).__name__}: {error}"
        )
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
    if not journal_tokens:
        raise ValueError("active journal registry is empty")
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


def _confined_artifact_sha256(
    root: Path,
    relative: str,
    kind: str,
) -> tuple[str | None, str | None]:
    parts = PurePosixPath(relative).parts
    open_fds: list[int] = []
    try:
        current_fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
        open_fds.append(current_fd)
        for index, part in enumerate(parts):
            try:
                mode = os.stat(part, dir_fd=current_fd, follow_symlinks=False).st_mode
            except FileNotFoundError:
                return None, f"{kind} file missing: {relative}"
            if stat.S_ISLNK(mode):
                return None, f"{kind} path contains symlink: {relative}"
            if index < len(parts) - 1:
                if not stat.S_ISDIR(mode):
                    return None, f"{kind} parent is not a directory: {relative}"
                try:
                    current_fd = os.open(
                        part,
                        os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                        dir_fd=current_fd,
                    )
                except OSError:
                    return None, f"{kind} path contains symlink: {relative}"
                open_fds.append(current_fd)
                continue
            if not stat.S_ISREG(mode):
                return None, f"{kind} path is not a regular file: {relative}"
            try:
                artifact_fd = os.open(
                    part,
                    os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW,
                    dir_fd=current_fd,
                )
            except OSError:
                return None, f"{kind} path contains symlink: {relative}"
            open_fds.append(artifact_fd)
            if not stat.S_ISREG(os.fstat(artifact_fd).st_mode):
                return None, f"{kind} path is not a regular file: {relative}"
            digest = hashlib.sha256()
            while chunk := os.read(artifact_fd, 1024 * 1024):
                digest.update(chunk)
            return digest.hexdigest(), None
    except OSError as error:
        return None, _error(f"{kind} file unreadable", Path(relative), error)
    finally:
        for descriptor in reversed(open_fds):
            try:
                os.close(descriptor)
            except OSError:
                pass


def _confined_artifact_bytes(
    root: Path,
    relative: str,
    kind: str,
) -> tuple[bytes | None, str | None]:
    safe = _safe_relative(relative)
    if safe is None:
        return None, f"{kind} path traversal: {relative}"
    parts = PurePosixPath(safe).parts
    open_fds: list[int] = []
    try:
        current_fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
        open_fds.append(current_fd)
        for index, part in enumerate(parts):
            try:
                mode = os.stat(part, dir_fd=current_fd, follow_symlinks=False).st_mode
            except FileNotFoundError:
                return None, f"{kind} file missing: {relative}"
            if stat.S_ISLNK(mode):
                return None, f"{kind} path contains symlink: {relative}"
            if index < len(parts) - 1:
                if not stat.S_ISDIR(mode):
                    return None, f"{kind} parent is not a directory: {relative}"
                current_fd = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=current_fd,
                )
                open_fds.append(current_fd)
                continue
            if not stat.S_ISREG(mode):
                return None, f"{kind} path is not a regular file: {relative}"
            artifact_fd = os.open(
                part,
                os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW,
                dir_fd=current_fd,
            )
            open_fds.append(artifact_fd)
            if not stat.S_ISREG(os.fstat(artifact_fd).st_mode):
                return None, f"{kind} path is not a regular file: {relative}"
            chunks: list[bytes] = []
            while chunk := os.read(artifact_fd, 1024 * 1024):
                chunks.append(chunk)
            return b"".join(chunks), None
    except OSError as error:
        return None, _error(f"{kind} file unreadable", Path(relative), error)
    finally:
        for descriptor in reversed(open_fds):
            try:
                os.close(descriptor)
            except OSError:
                pass


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
        actual, artifact_error = _confined_artifact_sha256(
            run_dir,
            relative,
            "manifest",
        )
        if artifact_error is not None:
            errors.append(artifact_error)
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


def _integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _parse_date(value: object) -> date | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        return datetime.strptime(value, "%Y/%m/%d").date()
    except ValueError:
        return None


def _query_semantic_core(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(
        r'\s+AND\s+\("\d{4}/\d{2}/\d{2}"\[Date - Publication\]\s*:\s*'
        r'"\d{4}/\d{2}/\d{2}"\[Date - Publication\]\)',
        "",
        value,
    ).strip()


def _query_date_interval(value: object) -> tuple[str, str] | None:
    if not isinstance(value, str):
        return None
    matched = re.search(
        r'\("(\d{4}/\d{2}/\d{2})"\[Date - Publication\]\s*:\s*'
        r'"(\d{4}/\d{2}/\d{2})"\[Date - Publication\]\)\s*$',
        value,
    )
    return matched.groups() if matched else None


def _validate_pages(
    run_dir: Path,
    pages: object,
    source_count: int,
    manifest: dict[str, str],
    owned_page_paths: set[str],
    owned_raw_paths: set[str],
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
            if relative in owned_raw_paths:
                errors.append(f"duplicate raw artifact path: {relative}")
            else:
                owned_raw_paths.add(relative)
        if relative is not None and relative in manifest:
            try:
                page_bytes, confined_error = _confined_artifact_bytes(
                    run_dir, relative, "PubMed page"
                )
                if confined_error is not None or page_bytes is None:
                    raise DiscoveryExecutionError(
                        confined_error or f"invalid PubMed XML: {relative}"
                    )
                _, actual_count = _parse_pubmed_page(page_bytes)
            except (ET.ParseError, OSError, DiscoveryExecutionError):
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
    owned_raw_paths: set[str],
    expected_source: str,
    expected_parent: dict[str, object] | None = None,
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
    expected_parent_id = str(expected_parent["search_id"]) if expected_parent else ""
    if cell["parent_search_id"] != expected_parent_id:
        errors.append(f"parent_search_id mismatch: {search_id}")
    if "source" in cell and cell["source"] != expected_source:
        errors.append(f"cell source mismatch: {search_id}")
    if expected_parent is not None:
        for field in ("lane", "family"):
            if cell[field] != expected_parent[field]:
                errors.append(f"child {field} mismatch: {search_id}")
        if _query_semantic_core(cell["query"]) != _query_semantic_core(
            expected_parent["query"]
        ):
            errors.append(f"child query semantic core mismatch: {search_id}")
        if _query_date_interval(cell["query"]) != (
            cell["date_start"],
            cell["date_end"],
        ):
            errors.append(f"child query date interval mismatch: {search_id}")
    if cell["status"] != "complete":
        errors.append(f"invalid cell status: {search_id}")
    parsed_dates = {field: _parse_date(cell[field]) for field in ("date_start", "date_end")}
    for field, parsed in parsed_dates.items():
        if parsed is None:
            errors.append(f"blank or invalid cell date: {field}")
    if (
        parsed_dates["date_start"] is not None
        and parsed_dates["date_end"] is not None
        and parsed_dates["date_start"] > parsed_dates["date_end"]
    ):
        errors.append("cell date range inverted")
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
    esearch_result: tuple[int, str, str] | None = None
    if esearch_path is not None:
        if esearch_path in owned_esearch_paths:
            errors.append(f"duplicate esearch path: {esearch_path}")
        else:
            owned_esearch_paths.add(esearch_path)
        if esearch_path in owned_raw_paths:
            errors.append(f"duplicate raw artifact path: {esearch_path}")
        else:
            owned_raw_paths.add(esearch_path)
        if esearch_path in manifest:
            try:
                esearch_bytes, confined_error = _confined_artifact_bytes(
                    run_dir, esearch_path, "PubMed ESearch"
                )
                if confined_error is not None or esearch_bytes is None:
                    raise DiscoveryExecutionError(
                        confined_error
                        or f"invalid PubMed ESearch JSON: {esearch_path}"
                    )
                esearch_result = _parse_esearch(esearch_bytes)
            except (OSError, DiscoveryExecutionError):
                errors.append(f"invalid PubMed ESearch JSON: {esearch_path}")
            else:
                if esearch_result[0] != reported_count:
                    errors.append("esearch reported count mismatch")
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
        if esearch_result is not None and (
            cell.get("webenv") != esearch_result[1]
            or cell.get("query_key") != esearch_result[2]
        ):
            errors.append("esearch history mismatch")
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
                owned_raw_paths,
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
                    owned_raw_paths,
                    expected_source,
                    cell,
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
        digest, artifact_error = _confined_artifact_sha256(
            root,
            relative,
            "configuration",
        )
        if artifact_error is not None:
            errors.append(artifact_error)
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
    wave_two_registry_rows: list[dict[str, str]] = []
    if wave_two:
        wave_two_registry_rows, wave_two_registry_errors = _validate_wave_two_registry(
            run_dir / "QUERY_REGISTRY.csv", configuration_root
        )
        errors.extend(wave_two_registry_errors)
    cells = payload["cells"]
    owned_esearch_paths: set[str] = set()
    owned_page_paths: set[str] = set()
    owned_raw_paths: set[str] = set()
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
        if wave_two:
            expected_wave_two_roots = {
                (
                    row.get("search_id"),
                    "FAMILY",
                    row.get("family"),
                    row.get("query"),
                    "",
                    row.get("date_start"),
                    row.get("date_end"),
                    "pubmed",
                )
                for row in wave_two_registry_rows
                if row.get("status") == "executed"
            }
            actual_wave_two_roots = {
                (
                    cell.get("search_id"),
                    cell.get("lane"),
                    cell.get("family"),
                    cell.get("query"),
                    cell.get("parent_search_id"),
                    cell.get("date_start"),
                    cell.get("date_end"),
                    cell.get("source", payload.get("source")),
                )
                for cell in cells
                if isinstance(cell, dict)
            }
            if (
                len(cells) != len(expected_wave_two_roots)
                or actual_wave_two_roots != expected_wave_two_roots
            ):
                errors.append("Wave 2 root cell mismatch")
        search_ids: set[str] = set()
        for cell in cells:
            errors.extend(
                _validate_cell(
                    run_dir,
                    cell,
                    manifest,
                    search_ids,
                    owned_esearch_paths,
                    owned_page_paths,
                    owned_raw_paths,
                    str(payload["source"]),
                )
            )
    if "compiled_candidates_raw.csv" not in manifest:
        errors.append("compiled_candidates_raw.csv absent from manifest")
    manifest_raw_paths = {path for path in manifest if path.startswith("raw/")}
    for path in sorted(manifest_raw_paths - owned_raw_paths):
        errors.append(f"unowned manifest raw artifact: {path}")
    try:
        expected_compiled = _derive_pubmed_candidates(run_dir)
    except DiscoveryExecutionError as error:
        errors.append(f"compiled candidates cannot be recomputed: {error}")
    else:
        compiled_headers, compiled_rows, compiled_errors = _read_csv(
            run_dir / "compiled_candidates_raw.csv",
            "invalid compiled candidates",
        )
        errors.extend(compiled_errors)
        if (
            compiled_headers != list(COMPILED_HEADERS)
            or compiled_rows != expected_compiled
        ):
            errors.append("compiled candidates content mismatch")
    empty_errors = _empty_wave_contract_errors(run_dir)
    if empty_errors is not None:
        errors.extend(empty_errors)
    return list(dict.fromkeys(errors))


def _validate_lineage_pages(
    run_dir: Path,
    row: dict[str, object],
    count: int,
    manifest: dict[str, str],
    owned_page_paths: set[str],
    owned_raw_paths: set[str],
) -> list[str]:
    return _validate_pages(
        run_dir,
        row.get("efetch_pages"),
        count,
        manifest,
        owned_page_paths,
        owned_raw_paths,
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
    receipt_queries: dict[str, dict[str, object]] = {}
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
            receipt_queries[query_id] = row
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
            raw_relative = _safe_relative(row["raw_path"])
            if raw_relative is not None and raw_relative in manifest:
                try:
                    raw_bytes, confined_error = _confined_artifact_bytes(
                        run_dir, raw_relative, "PubMed lineage raw"
                    )
                    if confined_error is not None or raw_bytes is None:
                        raise DiscoveryExecutionError(
                            confined_error or "PubMed lineage raw missing"
                        )
                    raw_count, raw_webenv, raw_query_key = _parse_esearch(raw_bytes)
                except DiscoveryExecutionError:
                    errors.append("invalid PubMed lineage ESearch JSON")
                else:
                    if (
                        raw_count != reported_count
                        or raw_webenv != row["webenv"]
                        or raw_query_key != row["query_key"]
                    ):
                        errors.append("PubMed lineage esearch mismatch")
            if reported_count >= 10000:
                errors.append("overbroad lineage identity query")
            else:
                errors.extend(
                    _validate_lineage_pages(
                        run_dir,
                        row,
                        reported_count,
                        manifest,
                        owned_page_paths,
                        owned_raw_paths,
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
                    errors.append(
                        "crossref receipt contains pubmed field: "
                        f"{field} (prohibited crossref field)"
                    )
            if any(field not in row for field in required):
                continue
            if row["raw_path"] != row["response_path"] or row["raw_sha256"] != row["response_sha256"]:
                errors.append("Crossref lineage raw/response mismatch")
            if row["rows"] != 5:
                errors.append("Crossref rows must equal 5")
            for field in ("returned_candidate_count", "total_results"):
                if not _integer(row[field]):
                    errors.append(f"invalid nonnegative integer count: {field}")
            raw_relative = _safe_relative(row["raw_path"])
            if raw_relative is not None and raw_relative in manifest:
                try:
                    raw_bytes, confined_error = _confined_artifact_bytes(
                        run_dir, raw_relative, "Crossref lineage raw"
                    )
                    if confined_error is not None or raw_bytes is None:
                        raise DiscoveryExecutionError(
                            confined_error or "Crossref lineage raw missing"
                        )
                    raw_payload = json.loads(raw_bytes.decode("utf-8"))
                    raw_message = raw_payload["message"]
                    raw_items = raw_message["items"]
                    raw_total = int(raw_message["total-results"])
                except (
                    OSError,
                    UnicodeError,
                    json.JSONDecodeError,
                    KeyError,
                    TypeError,
                    ValueError,
                    DiscoveryExecutionError,
                ):
                    errors.append("invalid Crossref lineage response JSON")
                else:
                    if (
                        not isinstance(raw_items, list)
                        or len(raw_items) > 5
                        or row["returned_candidate_count"] != len(raw_items)
                        or row["total_results"] != raw_total
                        or reported_count != raw_total
                    ):
                        errors.append("Crossref lineage raw count mismatch")
        else:
            errors.append("invalid lineage source")
    for table in ("pubmed_lineage_candidates.csv", "crossref_candidates.csv"):
        if table not in manifest:
            errors.append(f"lineage candidate table absent from manifest: {table}")
    errors.extend(
        _validate_lineage_decisions(
            root, run_dir, manifest, payload["configuration_files"], receipt_queries
        )
    )
    return list(dict.fromkeys(errors))


def _pipe_values(value: object) -> list[str]:
    if not isinstance(value, str) or not value:
        return []
    return [part for part in value.split("|") if part]


def _validate_lineage_decisions(
    root: Path,
    run_dir: Path,
    manifest: dict[str, str],
    configuration_files: object,
    receipt_queries: dict[str, dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    if not receipt_queries:
        errors.append("lineage query coverage missing")

    registry_path: Path | None = None
    if isinstance(configuration_files, list):
        for item in configuration_files:
            if isinstance(item, dict) and str(item.get("path", "")).endswith(
                "LINEAGE_QUERY_REGISTRY.csv"
            ):
                registry_path = root / str(item["path"])
                break
    if registry_path is None:
        registry_rows: list[dict[str, str]] = []
        errors.append("lineage query registry missing")
    else:
        registry_rows, registry_errors = _validate_lineage_registry(registry_path)
        errors.extend(registry_errors)
    registry_by_query: dict[str, dict[str, str]] = {}
    for row in registry_rows:
        query_id = row.get("query_id", "")
        if not query_id or query_id in registry_by_query:
            errors.append("duplicate or blank lineage registry query_id")
        else:
            registry_by_query[query_id] = row
    if set(registry_by_query) != set(receipt_queries):
        errors.append("lineage query registry coverage mismatch")
    for query_id, receipt in receipt_queries.items():
        registry = registry_by_query.get(query_id)
        if registry is None:
            continue
        for field in ("source", "query"):
            if registry.get(field) != receipt.get(field):
                errors.append(f"lineage query registry field mismatch: {query_id}: {field}")

    candidates_by_query: dict[str, list[dict[str, str]]] = {}
    candidates_by_key: dict[str, list[dict[str, str]]] = {}
    table_rows_by_source: dict[str, list[dict[str, str]]] = {
        "pubmed": [],
        "crossref": [],
    }
    for filename, headers in (
        ("pubmed_lineage_candidates.csv", PUBMED_LINEAGE_HEADERS),
        ("crossref_candidates.csv", CROSSREF_LINEAGE_HEADERS),
    ):
        rows, row_errors = _rows_with_headers(
            run_dir / filename, headers, "lineage candidate table"
        )
        errors.extend(row_errors)
        source = "pubmed" if filename.startswith("pubmed") else "crossref"
        table_rows_by_source[source] = rows
        for row in rows:
            query_id = row.get("query_id", "")
            key = row.get("candidate_key", "")
            registry = registry_by_query.get(query_id)
            receipt = receipt_queries.get(query_id)
            if registry is None or receipt is None or registry.get("source") != source:
                errors.append(f"lineage candidate query provenance mismatch: {key}")
                continue
            if row.get("named_source_id") != registry.get("named_source_id"):
                errors.append(f"lineage candidate named source mismatch: {key}")
            errors.extend(
                _reference_errors(
                    row.get("raw_path"), row.get("raw_sha256"), manifest, "lineage candidate"
                )
            )
            if source == "crossref":
                if row.get("raw_path") != receipt.get("response_path") or row.get(
                    "raw_sha256"
                ) != receipt.get("response_sha256"):
                    errors.append(f"lineage candidate provenance mismatch: {key}")
            else:
                page_pairs = {
                    (page.get("path"), page.get("sha256"))
                    for page in receipt.get("efetch_pages", [])
                    if isinstance(page, dict)
                }
                if (row.get("raw_path"), row.get("raw_sha256")) not in page_pairs:
                    errors.append(f"lineage candidate provenance mismatch: {key}")
            candidates_by_query.setdefault(query_id, []).append(row)
            candidates_by_key.setdefault(key, []).append(row)

    expected_rows_by_source: dict[str, list[dict[str, str]]] = {
        "pubmed": [],
        "crossref": [],
    }
    for query_id, registry in registry_by_query.items():
        receipt = receipt_queries.get(query_id)
        if receipt is None:
            continue
        try:
            if registry.get("source") == "pubmed":
                expected_rows_by_source["pubmed"].extend(
                    _pubmed_lineage_candidate_rows(registry, receipt, run_dir)
                )
            elif registry.get("source") == "crossref":
                expected_rows_by_source["crossref"].extend(
                    _crossref_lineage_candidate_rows(registry, receipt, run_dir)
                )
        except (DiscoveryExecutionError, OSError, UnicodeError) as error:
            errors.append(
                "lineage candidate table cannot be recomputed: "
                f"{query_id}: {error}"
            )
    for source in ("pubmed", "crossref"):
        headers = (
            PUBMED_LINEAGE_HEADERS if source == "pubmed" else CROSSREF_LINEAGE_HEADERS
        )
        normalize = lambda row: tuple(row.get(field, "") for field in headers)
        if sorted(map(normalize, table_rows_by_source[source])) != sorted(
            map(normalize, expected_rows_by_source[source])
        ):
            errors.append(f"lineage candidate table content mismatch: {source}")

    audit_rows, audit_errors = _rows_with_headers(
        run_dir / "lineage_identity_audit.csv",
        LINEAGE_AUDIT_HEADERS,
        "lineage identity audit",
    )
    errors.extend(audit_errors)
    if not (run_dir / "lineage_identity_audit.csv").is_file():
        errors.append("lineage identity audit missing")
    ledger_path = run_dir.parent / "global/lineage_ledger.csv"
    ledger_rows, ledger_errors = _rows_with_headers(
        ledger_path, LINEAGE_LEDGER_HEADERS, "lineage ledger"
    )
    errors.extend(ledger_errors)
    if not ledger_path.is_file():
        errors.append("lineage ledger missing")
    ledger_by_decision: dict[str, dict[str, str]] = {}
    for row in ledger_rows:
        decision_id = row.get("identity_decision_id", "")
        if not decision_id or decision_id in ledger_by_decision:
            errors.append("duplicate or blank lineage ledger decision")
        else:
            ledger_by_decision[decision_id] = row

    named_queries: dict[str, set[str]] = {}
    for query_id, registry in registry_by_query.items():
        named_queries.setdefault(registry.get("named_source_id", ""), set()).add(query_id)
    covered_queries: list[str] = []
    seen_decisions: set[str] = set()
    seen_named: set[str] = set()
    allowed_decisions = {"resolved", "ambiguous", "rejected", "unresolved_after_three_queries"}
    for audit in audit_rows:
        decision_id = audit.get("identity_decision_id", "")
        named_source = audit.get("named_source_id", "")
        if not decision_id or decision_id in seen_decisions or not named_source or named_source in seen_named:
            errors.append("duplicate or blank lineage identity decision")
            continue
        seen_decisions.add(decision_id)
        seen_named.add(named_source)
        supporting = _pipe_values(audit.get("supporting_query_ids"))
        if (
            supporting != sorted(supporting)
            or len(supporting) != len(set(supporting))
            or set(supporting) != named_queries.get(named_source, set())
        ):
            errors.append(f"lineage supporting query coverage mismatch: {decision_id}")
        covered_queries.extend(supporting)
        available_keys = {
            row.get("candidate_key", "")
            for query_id in supporting
            for row in candidates_by_query.get(query_id, [])
        }
        considered = _pipe_values(audit.get("candidate_keys_considered"))
        if (
            considered != sorted(considered)
            or len(considered) != len(set(considered))
            or not set(considered).issubset(available_keys)
        ):
            errors.append(f"lineage candidate provenance mismatch: {decision_id}")
        if not audit.get("primary_reviewer", "").strip():
            errors.append(f"blank lineage primary reviewer: {decision_id}")
        if not audit.get("audit_reviewer", "").strip():
            errors.append(f"blank lineage audit reviewer: {decision_id}")
        if audit.get("audit_reviewer") == audit.get("primary_reviewer"):
            errors.append(f"lineage audit reviewer is not independent: {decision_id}")
        stages = (
            ("primary", "primary_selected_candidate_key"),
            ("audit", "audit_selected_candidate_key"),
            ("final", "final_selected_candidate_key"),
        )
        for stage, selected_field in stages:
            stage_decision = audit.get(f"{stage}_decision", "")
            selected = audit.get(selected_field, "")
            if not audit.get(f"{stage}_reason", "").strip():
                errors.append(f"blank lineage {stage} reason: {decision_id}")
            if stage_decision not in allowed_decisions:
                errors.append(f"invalid lineage {stage} decision: {decision_id}")
            if stage_decision == "resolved":
                if not selected or selected not in considered or selected not in available_keys:
                    errors.append(f"lineage candidate provenance mismatch: {decision_id}")
            elif selected:
                errors.append(f"invalid lineage selected key: {decision_id}: {stage}")
        if any(
            audit.get(f"{stage}_decision") == "unresolved_after_three_queries"
            for stage, _ in stages
        ) and len(supporting) != 3:
            errors.append(
                "unresolved_after_three_queries requires exactly three "
                f"supporting queries: {decision_id}"
            )
        conflict = audit.get("conflict_status", "")
        primary_pair = (
            audit.get("primary_decision"),
            audit.get("primary_selected_candidate_key"),
        )
        audit_pair = (
            audit.get("audit_decision"),
            audit.get("audit_selected_candidate_key"),
        )
        final_pair = (
            audit.get("final_decision"),
            audit.get("final_selected_candidate_key"),
        )
        if conflict == "none" and (primary_pair != audit_pair or final_pair != audit_pair):
            errors.append(f"lineage conflict mismatch: {decision_id}")
        elif conflict == "open":
            if primary_pair == audit_pair or final_pair != ("ambiguous", ""):
                errors.append(f"open lineage conflict resolved improperly: {decision_id}")
        elif conflict == "resolved":
            if primary_pair == audit_pair:
                errors.append(f"lineage conflict mismatch: {decision_id}")
            if not audit.get("adjudicator", "").strip():
                errors.append(f"resolved lineage conflict missing adjudicator: {decision_id}")
            if not audit.get("final_reason", "").strip():
                errors.append(f"resolved lineage conflict missing final reason: {decision_id}")
        elif conflict not in {"none", "open", "resolved"}:
            errors.append(f"invalid lineage conflict status: {decision_id}")
        if audit.get("final_decision") == "resolved" and not audit.get(
            "inspected_primary_url", ""
        ).strip():
            errors.append(f"resolved lineage identity missing primary URL: {decision_id}")

        ledger = ledger_by_decision.get(decision_id)
        if ledger is None or ledger.get("named_source_id") != named_source:
            errors.append(f"lineage ledger decision missing: {decision_id}")
            continue
        final_key = audit.get("final_selected_candidate_key", "")
        if ledger.get("final_candidate_key") != final_key:
            errors.append(f"lineage ledger final key mismatch: {decision_id}")
        if ledger.get("search_ids") != "|".join(sorted(supporting)):
            errors.append(f"lineage ledger search coverage mismatch: {decision_id}")
        registry = registry_by_query.get(supporting[0]) if supporting else None
        if registry is not None:
            for field in ("method_label", "canonical_name", "family", "source_role"):
                if ledger.get(field) != registry.get(field):
                    errors.append(
                        f"lineage ledger registry mismatch: {decision_id}: {field}"
                    )
        expected_status = (
            "resolved_identity_role_unverified"
            if audit.get("final_decision") == "resolved"
            else audit.get("final_decision")
        )
        if ledger.get("status") != expected_status or ledger.get("verification_state") != "discovery":
            errors.append(f"lineage ledger status mismatch: {decision_id}")
        if final_key:
            candidate_rows = [
                row
                for query_id in supporting
                for row in candidates_by_query.get(query_id, [])
                if row.get("candidate_key") == final_key
            ]
            candidate = candidate_rows[0] if candidate_rows else None
            if candidate is None:
                errors.append(f"lineage candidate provenance mismatch: {decision_id}")
            else:
                expected_url = candidate.get("url") or candidate.get("source_url") or ""
                for field in ("title", "year", "doi", "pmid"):
                    if ledger.get(field, "") != candidate.get(field, ""):
                        errors.append(f"lineage ledger candidate mismatch: {decision_id}: {field}")
                if (
                    ledger.get("primary_url") != expected_url
                    or ledger.get("primary_url") != audit.get("inspected_primary_url")
                ):
                    errors.append(f"lineage ledger primary URL mismatch: {decision_id}")
        elif any(
            ledger.get(field, "")
            for field in ("title", "year", "doi", "pmid", "primary_url")
        ):
            errors.append(
                f"unresolved lineage ledger identity fields populated: {decision_id}"
            )
    if sorted(covered_queries) != sorted(receipt_queries) or len(covered_queries) != len(
        set(covered_queries)
    ):
        errors.append("lineage query decision coverage mismatch")
    if seen_named != set(named_queries):
        errors.append("lineage named source decision coverage mismatch")
    if set(ledger_by_decision) != seen_decisions:
        errors.append("lineage ledger decision coverage mismatch")
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
    empty_errors = _empty_wave_contract_errors(run_dir)
    if empty_errors is not None:
        return empty_errors
    compiled, errors = _compiled_index(run_dir)
    primary, primary_errors = _primary_index(run_dir)
    errors.extend(primary_errors)
    screened_rows, screened_errors = _rows_with_headers(
        run_dir / "screened_candidates.csv", SCREENED_HEADERS, "screened candidates"
    )
    errors.extend(screened_errors)
    audit_rows, audit_errors = _rows_with_headers(
        run_dir / "screening_audit.csv", AUDIT_HEADERS, "screening audit"
    )
    errors.extend(audit_errors)
    audit_keys = {
        row.get("candidate_key", "")
        for row in audit_rows
        if row.get("candidate_key", "")
    }
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
        if row.get("audit_status") == "not_selected" and key in audit_keys:
            errors.append(f"unexpected audit row for not_selected: {key}")
        if row.get("audit_status") in {"agree", "conflict_open", "conflict_resolved"} and key not in audit_keys:
            errors.append(f"missing audit row for screened status: {key}")
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
    empty_errors = _empty_wave_contract_errors(run_dir)
    if empty_errors is not None:
        return empty_errors
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


def validate_global_reconciliation(phase_run_dir: Path) -> list[str]:
    phase_run_dir = Path(phase_run_dir)
    errors: list[str] = []
    global_dir = phase_run_dir / "global"
    rows, row_errors = _rows_with_headers(
        global_dir / "candidates_through_wave_02.csv",
        GLOBAL_INDEX_HEADERS,
        "global candidate index",
    )
    errors.extend(row_errors)
    reconciliation = global_dir / "GLOBAL_KEY_RECONCILIATION.txt"
    terminal_marker = "ALL WAVE, SCREENING, REGISTRY, AND LINEAGE KEYS RECONCILE"
    if not reconciliation.is_file():
        errors.append("global reconciliation missing")
    else:
        try:
            reconciliation_lines = reconciliation.read_text(encoding="utf-8").splitlines()
        except OSError as error:
            errors.append(_error("invalid global reconciliation", reconciliation, error))
        else:
            if not reconciliation_lines or reconciliation_lines[-1] != terminal_marker:
                errors.append("global reconciliation terminal marker missing")

    wave_rows: dict[str, dict[str, dict[str, str]]] = {}
    wave_screened: dict[str, dict[str, dict[str, str]]] = {}
    wave_directories = (
        ("wave_01", "wave_01_frozen_queries"),
        ("wave_02", "wave_02_synonym_expansion"),
    )
    for wave, directory_name in wave_directories:
        directory = phase_run_dir / directory_name
        compiled, compiled_errors = _compiled_index(directory)
        errors.extend(f"{wave} compiled: {error}" for error in compiled_errors)
        screened_rows, screened_errors = _rows_with_headers(
            directory / "screened_candidates.csv",
            SCREENED_HEADERS,
            f"{wave} screened candidates",
        )
        errors.extend(screened_errors)
        screened: dict[str, dict[str, str]] = {}
        for screened_row in screened_rows:
            key = screened_row.get("candidate_key", "")
            if not key or key in screened:
                errors.append(f"duplicate or blank {wave} screened candidate key")
            else:
                screened[key] = screened_row
        wave_rows[wave] = compiled
        wave_screened[wave] = screened

    global_by_key: dict[str, dict[str, str]] = {}
    for row in rows:
        key = row.get("candidate_key", "")
        if not key or key in global_by_key:
            errors.append("duplicate or blank global candidate key")
        else:
            global_by_key[key] = row
    all_keys = set().union(*(set(index) for index in wave_rows.values()))
    if set(global_by_key) != all_keys:
        errors.append("global candidate key coverage mismatch")

    directory_by_wave = dict(wave_directories)
    for key in sorted(all_keys & set(global_by_key)):
        row = global_by_key[key]
        contributing = sorted(wave for wave, index in wave_rows.items() if key in index)
        expected_waves = "|".join(contributing)
        if row.get("waves") != expected_waves:
            errors.append(f"global contributing waves mismatch: {key}")
        expected_hashes = "|".join(
            f"{wave}:{wave_rows[wave][key].get('row_sha256', '')}"
            for wave in contributing
        )
        if row.get("wave_source_row_sha256s") != expected_hashes:
            errors.append(f"global source row SHA coverage mismatch: {key}")

        screening_wave = "wave_01" if "wave_01" in contributing else contributing[0]
        expected_screening_path = (
            f"{directory_by_wave[screening_wave]}/screened_candidates.csv"
        )
        if row.get("screening_path") != expected_screening_path:
            errors.append(f"global screening path mismatch: {key}")
        screened = wave_screened[screening_wave].get(key)
        if screened is None:
            errors.append(f"global screening decision missing: {key}")
        else:
            for global_field, screened_field in (
                ("final_decision", "final_decision"),
                ("final_proposed_record_type", "final_proposed_record_type"),
                ("final_reason_code", "final_reason_code"),
            ):
                if row.get(global_field) != screened.get(screened_field):
                    errors.append(f"global final decision mismatch: {key}: {global_field}")
        expected_disposition = (
            "screened_in_wave_01"
            if contributing == ["wave_01", "wave_02"]
            else ""
        )
        if row.get("duplicate_disposition") != expected_disposition:
            errors.append(f"global duplicate disposition mismatch: {key}")
    return list(dict.fromkeys(errors))


def _validate_repository_for_all(root: Path) -> list[str]:
    module_path = Path(__file__).with_name("validate_library.py")
    spec = importlib.util.spec_from_file_location(
        "_discovery_library_repository_validator", module_path
    )
    if spec is None or spec.loader is None:
        return ["repository validator import failed"]
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
        repository_errors = module.validate_repository(root)
    except (ImportError, OSError, AttributeError) as error:
        return [_error("repository validator import failed", module_path, error)]
    return list(repository_errors)


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
    errors.extend(
        f"global: {error}" for error in validate_global_reconciliation(phase_run_dir)
    )
    errors.extend(f"repository: {error}" for error in _validate_repository_for_all(root))
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
        try:
            cells = build_search_cells(args.root, args.date)
        except Exception as error:
            return _emit(
                [
                    "unable to build search cells: "
                    f"{type(error).__name__}: {error}"
                ]
            )
        for cell in cells:
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
    try:
        if args.command == "run":
            errors = validate_configuration(args.root)
            if errors:
                return _emit(errors)
            cells = build_search_cells(args.root, args.date)
            execute_pubmed_run(
                args.root,
                cells,
                args.output,
                args.email,
                api_key=args.api_key,
                opener=urllib.request.urlopen,
            )
            return _emit(validate_search_run(args.output))
        if args.command == "run-wave":
            errors = validate_configuration(args.root)
            if errors:
                return _emit(errors)
            execute_wave(
                args.root,
                args.query_registry,
                args.output,
                args.email,
                api_key=args.api_key,
                opener=urllib.request.urlopen,
            )
            return _emit(validate_search_run(args.output))
        if args.command == "run-lineage":
            errors = validate_configuration(args.root)
            if errors:
                return _emit(errors)
            execute_lineage(
                args.root,
                args.query_registry,
                args.output,
                args.email,
                api_key=args.api_key,
                opener=urllib.request.urlopen,
            )
            return _emit([])
        if args.command == "compile":
            compile_pubmed_candidates(args.run_dir)
            return _emit([])
    except (DiscoveryExecutionError, OSError, UnicodeError, ValueError) as error:
        return _emit([str(error)])
    return _emit([f"unsupported discovery command: {args.command}"])


if __name__ == "__main__":
    sys.exit(main())
