# Broad Methods Discovery and Lineage Search Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute a reproducible, methods/problem-first discovery search that locates transferable infectious-disease applications and their original or authoritative method sources without prematurely verifying substantive claims, judging data feasibility, or selecting flagship studies.

**Architecture:** The phase uses two linked discovery lanes. The applied lane searches PubMed across all six approved method families and a declared journal set; the lineage lane starts from retained applied/method leads and traces original methods, corrections, diagnostics, guidance, and official software sources. Raw API responses are immutable and SHA-256 manifested, semantic screening is auditable, and only bibliographic-role claims directly supported by primary records enter the formal registries.

**Tech Stack:** Git; Python 3.12 standard library; `unittest`; NCBI PubMed E-utilities; Crossref REST API for DOI/bibliographic resolution only; Markdown; CSV; JSON; SHA-256.

## Global Constraints

- Approved Library design: `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`, commit `c708ac2402431202c8b1af4c5fd87035460249ab`, SHA256 `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`.
- Bootstrap publication baseline: `1571301044e8d59329c65a2f67e19587e4739c98`; local `main`, `origin/main`, and GitHub `main` were equal before this plan was written.
- The background authority includes the Library discussion in Codex task `019f78e2-e49c-7c01-bc36-599a250e5bc1`: the work began from the owner's need for an independent-researcher portfolio, but discovery must be method/problem first rather than public-data, disease, AMR, LMIC, or geography first.
- The intended later portfolio remains multiple flagship candidates, one or two lower-risk public-data projects, and at least one credible non-AMR infectious-disease route. This search phase does not rank or select them.
- The main applied-search period is 2010-01-01 through 2026-12-31. Earlier records are eligible for method lineage, foundational applications, and unusually informative natural experiments.
- Applied seeds and original/authoritative methods are separate source roles. High-impact applications and journal prestige never verify a method claim.
- Relevant `npj` and specialist outlets are eligible. The journal registry is a coverage device, not an inclusion or quality gate.
- Simulation-only, synthetic-data, mechanistic, agent-based, and method-comparison work is fully eligible. A possible pure-simulation flagship must later show a broad structural contribution; generic small-sample failure is insufficient.
- Discovery records use `verification_state=discovery`. `verified` and `extracted` are forbidden in this plan unless a later owner-approved verification plan supplies the required primary-source checks.
- This plan may retrieve bibliographic metadata and abstracts. It must not bulk-download full text, candidate datasets, restricted material, or software repositories.
- This plan must not execute a formal simulation, data feasibility audit, translation ranking, or project graduation; it must not select a flagship.
- The frozen seed scan remains a discovery map, not verified evidence. Its SHA256 must remain `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`.
- Do not write to `/Users/hongchaokun/Documents/PhD/Surveillance_AMR`. Its existing dirty state and untracked reciprocal pointer belong outside this plan.
- Normalized link registries remain authoritative under `DEC-20260720-005`; Markdown linked-ID fields are mirrors.
- Every executed query receives a permanent search ID, exact query text, source-reported count, execution timestamp with timezone, raw response path, and SHA-256 receipt.
- Network failures must leave no partially named final artifact. Write to a temporary sibling path, validate the response, then atomically replace the final path.
- Do not reduce a search query, stop screening, or change a gate merely to obtain convenient counts. Query splits preserve semantics and are logged as deviations.
- Every task ends in a separately reviewable commit. Critical or Important review findings are fixed and re-reviewed before the next task.

## Per-task implementation and review gate

Tasks 1–8 use eight fresh implementation subagents, one per task. After each implementation subagent commits its bounded task, the orchestrator creates `07_reviews/discovery_tasks/TASK_N_REVIEW_PACKAGE.md` containing the task base SHA, implementation/fix SHAs, exact reviewed head, changed paths, requirement checklist, commands and live outputs, known limitations, and external-boundary status when applicable. A different, fresh review subagent reads the approved design, this plan, the exact base-to-head diff, and the package, then checks both specification compliance and task quality in one review.

The review result is recorded in `07_reviews/discovery_tasks/TASK_N_REVIEW.md` with counts and details by `Critical`, `Important`, and `Minor` severity. Any Critical or Important finding returns to that task's original implementation subagent for a focused fix commit; the same independent reviewer then re-reviews the new exact head. The next task may start only when the result says `PASS — no remaining Critical or Important findings`. The orchestrator commits the final package and review receipt with subject `record task N discovery review`. Minor deferrals require an explicit risk statement and next-action owner. Review agents never implement their own findings.

`07_reviews/discovery_tasks/EXECUTION_LEDGER.md` is updated after every implementation, fix, review, and receipt commit. Each row records `task`, `status`, `base_sha`, `implementation_sha`, `fix_shas`, `reviewed_head`, `review_verdict`, `review_receipt_path`, and `next_action`. It never tries to store the SHA of the commit that contains its own current contents. Resolve the passing receipt commit with `git log -1 --format=%H -- <review_receipt_path>`. On restart or context compaction, the ledger plus live Git history is authoritative; a task whose receipt path resolves to a passing reviewed head is never repeated.

---

## Phase Boundary

This plan implements:

1. Stage 1 broad discovery: reproducible applied-paper and method-led searches, raw metadata freezing, deduplication, and semantic screening.
2. The locating portion of Stage 2 method lineage: identify candidate original/authoritative method sources, corrections, diagnostics, guidance, and official software resources.
3. Discovery-state paper and method records with explicitly bounded bibliographic-role evidence.

This plan defers:

1. verification of substantive claims against full primary sources;
2. completion and review of all 18 method-card sections;
3. translation generation, dataset access verification, feasibility scoring, portfolio ranking, simulation execution, and flagship selection.

## Search Lanes

### Applied-family lane

For each approved family, combine a frozen high-precision title method block with a frozen infectious-disease block in PubMed. This is an all-journal method-led discovery lane, not a venue restriction. Retrieve every matching record from every executable leaf cell.

### Applied-venue lane

For each family, combine the broader title/abstract method block and infectious-disease block with the active journal block. This lane tests coverage of high-impact, `npj`, and specialist applied outlets but does not exclude papers found outside them.

### Method-lineage lane

For every retained applied or method lead, inspect the primary record and trace cited or named method sources. Search Crossref only to generate bounded bibliographic identity/DOI candidates when PubMed metadata are absent or ambiguous. A human reviewer resolves or leaves each candidate unresolved; no Crossref match automatically upgrades identity, source role, or a substantive claim. Publisher pages, original papers, official repositories, specifications, and source code are the later verification authorities.

### Immutable search waves

- `wave_01_frozen_queries`: the 12 preregistered PubMed cells.
- `wave_02_synonym_expansion`: at most one documented synonym-gap query per family, derived from completed Wave 1 screening.
- `wave_03_lineage_resolution`: bounded PubMed/Crossref bibliographic candidates derived from retained method concepts and inspected primary records.

Waves 1 and 2 each have their own raw directory, manifest, receipt, compiled raw table, screening batches, screening audit, and verification result. Wave 3 has its own raw directory, manifest, heterogeneous-source receipt, lineage candidate/decision ledgers, independent identity audit, and verification result. A later wave never rewrites an earlier wave. Global compilation is regenerated from verified wave outputs and checks every identifier-level candidate key exactly once while retaining all contributing-wave provenance.

## Search Identifiers

Use exactly:

```text
SEARCH-YYYYMMDD-PUBMED-FAMILY-<FAMILY>-NN
SEARCH-YYYYMMDD-PUBMED-VENUE-<FAMILY>-NN
SEARCH-YYYYMMDD-LINEAGE-<FAMILY>-NN
```

where `<FAMILY>` is one of `CAUSAL`, `SURVEILLANCE`, `SPATIAL`, `FORECASTING`, `EVIDENCE`, or `SIMULATION`. `NN` is the zero-padded next unused positive integer within the `(execution date, lane, family)` namespace. Root queries are allocated in sorted wave/lane/family order; split descendants are allocated depth-first and record the parent search ID. No later wave reuses an earlier ID. Every Wave 3 `query_id` follows the `LINEAGE` pattern, with the row's separate `source` field distinguishing PubMed from Crossref.

## File Map

| Path | Responsibility |
|---|---|
| `01_search/search_protocols/2026-07-20-broad-methods-discovery-protocol.md` | Frozen scope, lanes, screening rules, reason codes, query-split rule, and stopping rule |
| `01_search/search_protocols/discovery_queries.json` | Machine-readable infectious-disease and six-family term blocks plus date/source settings |
| `01_search/journal_registry/journals.csv` | Declared applied-seed coverage set and active PubMed journal tokens |
| `01_search/PAPER_DISCOVERY_RECORD_TEMPLATE.md` | Minimal discovery-state paper record contract; contains no substantive method claims |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/` | Immutable raw responses and screening for the 12 preregistered PubMed cells |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/` | Immutable raw responses and screening for bounded synonym-gap searches |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/` | Immutable PubMed/Crossref resolution candidates and lineage decisions |
| `01_search/search_logs/2026-07-20-broad-discovery/global/` | Cross-wave candidate index, screening key coverage, lineage ledger, and coverage audit |
| `00_governance/scripts/discovery_search.py` | Validate configuration, build exact queries, execute/freeze PubMed responses, compile/deduplicate metadata, and verify manifests |
| `00_governance/tests/test_discovery_search.py` | Unit and command-line contract tests for search configuration and artifacts |
| `01_search/discovery_records/P-YYYY-NNNN.md` | Retained paper discovery records |
| `01_search/method_discovery_records/M-FAMILY-NNN.md` | Minimal discovery-state method records; these are not Stage 3 method cards |
| `03_evidence_tables/papers.csv` | Retained discovery papers after semantic screening and bibliographic identity checks |
| `03_evidence_tables/methods.csv` | Canonical discovery-state method concepts after duplicate-label resolution |
| `01_search/search_logs/2026-07-20-broad-discovery/global/discovery_relationships.csv` | Provisional discovery-state paper/method source roles; formal normalized links remain header-only until primary-source verification |
| `07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json` | Phase-start filtered source-worktree status digest, line count, pointer/source states, and honest proof limitation |
| `07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md` | Commands, counts, checksums, screening coverage, review verdicts, limitations, and deferred work |
| `HANDOFF.md` | Live state and exact next independent plan |

## Interfaces

The search subsystem exposes:

```python
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

def load_configuration(root: Path) -> tuple[dict[str, object], list[dict[str, str]]]: ...
def validate_configuration(root: Path) -> list[str]: ...
def build_search_cells(root: Path, executed_date: date) -> list[SearchCell]: ...
def execute_pubmed_cell(
    cell: SearchCell,
    output_dir: Path,
    email: str,
    api_key: str | None = None,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> dict[str, object]: ...
def compile_pubmed_candidates(run_dir: Path) -> list[dict[str, str]]: ...
def resolve_crossref_candidates(
    query_id: str,
    bibliographic_query: str,
    output_dir: Path,
    email: str,
    opener: Callable[..., object] = urllib.request.urlopen,
) -> dict[str, object]: ...
def validate_search_run(run_dir: Path) -> list[str]: ...
def validate_screening(run_dir: Path) -> list[str]: ...
def validate_screening_audit(run_dir: Path) -> list[str]: ...
def validate_lineage(root: Path, run_dir: Path) -> list[str]: ...
def validate_all(root: Path, phase_run_dir: Path) -> list[str]: ...
def validate_external_boundary(root: Path, source_root: Path) -> list[str]: ...
def main(argv: Sequence[str] | None = None) -> int: ...
```

The command-line contract is:

```text
python3 00_governance/scripts/discovery_search.py validate-config --root .
python3 00_governance/scripts/discovery_search.py list-cells --root . --date 2026-07-20
python3 00_governance/scripts/discovery_search.py run --root . --date 2026-07-20 --email <email> [--api-key <runtime-key>] --output <wave-dir>
python3 00_governance/scripts/discovery_search.py run-wave --root . --query-registry <wave-02-query-registry> --email <email> [--api-key <runtime-key>] --output <wave-02-dir>
python3 00_governance/scripts/discovery_search.py run-lineage --root . --query-registry <wave-03-query-registry> --email <email> [--api-key <runtime-key>] --output <wave-03-dir>
python3 00_governance/scripts/discovery_search.py compile --run-dir <run-dir>
python3 00_governance/scripts/discovery_search.py verify --run-dir <run-dir>
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir <run-dir>
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir <run-dir>
python3 00_governance/scripts/discovery_search.py verify-lineage --root . --run-dir <run-dir>
python3 00_governance/scripts/discovery_search.py verify-all --root . --run-dir <phase-run-dir>
python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR
```

All validation actions print `DISCOVERY PASS` and exit `0` on success. They print `DISCOVERY FAIL`, one stable error per line, and exit `1` on failure. `run`, `run-wave`, and `run-lineage` exit nonzero on the first incomplete executable query and keep already completed immutable queries; re-running skips only queries whose raw manifest entries and receipt fields validate.

## Execution preflight before Task 1

1. Commit this independently reviewed plan on `main`, record its SHA-256 and commit in `HANDOFF.md`, rerun the Library validator, and push that planning baseline.
2. Use `superpowers:using-git-worktrees`: verify the current checkout is not already linked, confirm `.worktrees/` is ignored, then create `.worktrees/broad-methods-discovery` on `codex/broad-methods-discovery` from the planning baseline.
3. In the isolated worktree, run both existing unit-test commands and the Library validator. A baseline failure is a blocker; do not attribute it to this plan or continue without resolution.
4. Ensure `.superpowers/sdd/progress.md` is ignored through the repository-local Git exclude, create it as the skill's scratch recovery ledger, and create the committed `07_reviews/discovery_tasks/EXECUTION_LEDGER.md` with the fields in the global gate. Commit only the durable ledger with subject `initialize broad discovery execution ledger`.
5. Use `superpowers:subagent-driven-development`. Before each task, generate its bounded task brief from this plan. Dispatch exactly one fresh implementation subagent; review with a different fresh subagent after the implementation commit; never run two file-writing implementation tasks in parallel.

---

### Task 1: Freeze the discovery protocol, query vocabulary, and journal coverage set

**Files:**
- Create: `01_search/search_protocols/2026-07-20-broad-methods-discovery-protocol.md`
- Create: `01_search/search_protocols/discovery_queries.json`
- Create: `01_search/journal_registry/journals.csv`
- Create: `01_search/PAPER_DISCOVERY_RECORD_TEMPLATE.md`
- Create: `01_search/METHOD_DISCOVERY_RECORD_TEMPLATE.md`
- Create: `07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json`
- Modify: `00_governance/DECISION_LOG.md`

**Interfaces:**
- Consumes: approved design sections 1–8 and the owner-approved Library discussion in task `019f78e2-e49c-7c01-bc36-599a250e5bc1`.
- Produces: frozen human- and machine-readable search configuration used by every later task.

- [ ] **Step 1: Add the phase decision without rewriting earlier decisions**

Append this row to `00_governance/DECISION_LOG.md`:

```markdown
| DEC-20260720-006 | 2026-07-20 | active | Execute broad method discovery in two auditable lanes—infectious-disease applications and method lineage—while keeping all new records at `discovery` until a separate primary-source verification plan. | Preserves the owner's methods-first intent and prevents high-impact applications, search-index metadata, or the seed scan from being misreported as verified evidence. | Owner continuation approval; approved design `c708ac2`; Library discussion in Codex task `019f78e2-e49c-7c01-bc36-599a250e5bc1`. | — |
```

- [ ] **Step 2: Write the protocol with binding screening and stopping rules**

The protocol must contain these headings and exact rules:

```markdown
# Broad Methods Discovery Protocol

## Purpose and phase boundary
This is a broad, reproducible discovery map, not a systematic-review claim and not substantive evidence verification. It may identify records and bibliographic roles; it does not complete method cards, judge feasibility, rank candidates, or select a flagship.

## Eligible discovery leads
- Applied infectious-disease papers demonstrating a potentially transferable design.
- Original or authoritative method papers named by retained applications or method-led searches.
- Corrections, critiques, diagnostics, guidance, official software, reproducibility resources, simulation-only studies, synthetic-data evaluations, and mechanistic or agent-based models.
- Work outside infectious diseases only when a concrete infectious-disease transfer route can be stated without inventing evidence.

## Discovery-stage non-exclusions
Do not exclude for being non-AMR, non-LMIC, regional rather than global, currently without public data, collaboration-dependent, computationally difficult, or simulation-only.

## Exclusion reason codes
- `X_DESCRIPTIVE_ONLY`: no transferable design contribution is identifiable from title/abstract/primary record.
- `X_COMMENTARY_ONLY`: commentary or news without enough method content to support a discovery role.
- `X_DUPLICATE`: duplicate bibliographic record; retained record key must be named.
- `X_NOT_INFECTIOUS_TRANSFERABLE`: outside infectious diseases and no explicit transfer route can be stated.
- `X_NO_RESOLVABLE_IDENTITY`: title, year, and primary or DOI URL cannot be resolved after documented attempts.
- `X_WRONG_RECORD_TYPE`: editorial, protocol, conference abstract, or non-research record that adds no method, diagnostic, correction, guidance, or reproducibility information.

## Inclusion and uncertainty reason codes
- `I_APPLIED_TRANSFERABLE_DESIGN`: applied infectious-disease use of a potentially transferable design.
- `I_METHOD_SOURCE`: candidate original, authoritative, or methodological source.
- `I_DIAGNOSTIC_CORRECTION`: diagnostic, correction, guidance, or reproducibility lead.
- `I_SIMULATION_MECHANISTIC`: simulation-only, synthetic-data, mechanistic, agent-based, or method-comparison lead.
- `U_PRIMARY_RECORD_NEEDED`: available metadata are insufficient for a responsible include/exclude decision.

## Screening decisions
- `include_applied_seed`
- `include_method_source_lead`
- `include_diagnostic_or_correction_lead`
- `include_simulation_or_mechanistic_lead`
- `uncertain_retrieve_primary`
- `exclude`

Every included row also receives one human-assigned `proposed_record_type` from the existing registry enum. The mapping is constrained as follows:

- `include_applied_seed` -> `applied_seed`
- `include_method_source_lead` -> `method_source`
- `include_diagnostic_or_correction_lead` -> `diagnostic | correction | guidance | reproducibility`
- `include_simulation_or_mechanistic_lead` -> `method_source | applied_seed`, chosen from the paper's actual role
- `uncertain_retrieve_primary | exclude` -> blank and not eligible for registry promotion

The screening reason code is exact and decision-bound: the four inclusion decisions use their corresponding `I_*` code, `uncertain_retrieve_primary` uses `U_PRIMARY_RECORD_NEEDED`, and `exclude` uses one `X_*` code. A one-sentence record-specific reason is required in addition to the code.

## Claim boundary
Search-index metadata and abstracts support discovery and bibliographic-role screening only. Substantive claims about estimands, assumptions, diagnostics, software behavior, datasets, or performance remain unverified until checked against the owning primary source in a later plan.

## Search execution
Execute every active family cell in both PubMed lanes. ESearch always uses `usehistory=y`. A cell with fewer than 10,000 matches is an executable leaf. A larger cell is a `split_parent`: recursively split its date interval into non-overlapping year, then month, then day intervals until every leaf has fewer than 10,000 matches. Parent cells never execute EFetch. Record the parent/child tree and prove that child intervals are contiguous, non-overlapping, and cover the parent interval. If one day still has 10,000 or more matches, stop with `unsplittable PubMed cell`; do not cap or narrow it silently.

Wave 1 contains the 12 frozen queries. After Wave 1 semantic screening, Wave 2 contains at most one synonym-gap query per family and its complete delta screening. Wave 3 contains bounded lineage-resolution candidates and their complete human resolution. Waves 1/2 have immutable raw, compiled, screened, and screening-audit artifacts; Wave 3 has immutable raw, lineage decision, and lineage identity-audit artifacts.

## Semantic screening
Every unique title and available abstract is read semantically in deterministic batches of 150 records. Each batch consumes a manifested raw-candidate slice and produces one strict CSV row per key. Keyword rules may route records but never make the final inclusion/exclusion decision. A reason code and one-sentence rationale are mandatory. PMID and normalized DOI may auto-deduplicate; equal normalized titles create only a `possible_duplicate_group` and require human comparison of title, year, journal, authors, PMID, DOI, and source before exclusion as duplicate.

## Lineage tracing
For every retained method concept, attempt to locate an original or currently authoritative method source and any directly named correction, diagnostic, guidance, or official implementation. Record unresolved lineage honestly; do not infer `originates` from citation order or journal prestige.

## Coverage stopping rule
Complete Wave 1 and its screening, then execute and screen Wave 2 synonym-gap queries. Execute Wave 3 lineage resolution only after canonical discovery concepts are frozen. Waves 1/2 contribute to coverage only after raw retrieval, compilation, semantic screening, screening audit, and key reconciliation pass. Wave 3 contributes only after its raw heterogeneous receipt/manifest, named-source identity decisions, 100% independent identity audit, lineage ledger, and query/decision reconciliation pass. After these three bounded waves, report residual gaps; do not claim exhaustive saturation.

## External boundary
At phase start, hash the exact `Surveillance_AMR` porcelain status after filtering only `?? ID_EPI_METHODS_LIBRARY_POINTER.md`. Record line count, digest, source HEAD, pointer status, pointer index absence, and seed-source status in the Library receipt. This is path/status evidence only and does not prove byte identity for files already dirty at baseline.
```

- [ ] **Step 3: Create the machine-readable query configuration**

Create `discovery_queries.json` with this exact structure and term blocks:

```json
{
  "schema_version": 1,
  "applied_date_start": "2010/01/01",
  "applied_date_end": "2026/12/31",
  "source": "pubmed",
  "family_method_field": "Title",
  "venue_method_field": "Title/Abstract",
  "infectious_disease_block": "(\"Communicable Diseases\"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract])",
  "families": [
    {
      "family": "causal_policy",
      "token": "CAUSAL",
      "method_block": "(\"interrupted time series\"[Title/Abstract] OR \"difference-in-differences\"[Title/Abstract] OR \"difference in differences\"[Title/Abstract] OR \"event study\"[Title/Abstract] OR \"synthetic control\"[Title/Abstract] OR \"regression discontinuity\"[Title/Abstract] OR \"instrumental variable\"[Title/Abstract] OR \"target trial\"[Title/Abstract] OR \"negative control\"[Title/Abstract])"
    },
    {
      "family": "surveillance_measurement",
      "token": "SURVEILLANCE",
      "method_block": "(capture-recapture[Title/Abstract] OR \"capture recapture\"[Title/Abstract] OR \"multiple-system estimation\"[Title/Abstract] OR nowcast*[Title/Abstract] OR \"reporting delay\"[Title/Abstract] OR \"observation process\"[Title/Abstract] OR \"preferential sampling\"[Title/Abstract] OR \"measurement error\"[Title/Abstract] OR \"sentinel surveillance\"[Title/Abstract] OR \"latent class\"[Title/Abstract])"
    },
    {
      "family": "spatial_transmission",
      "token": "SPATIAL",
      "method_block": "(\"endemic-epidemic\"[Title/Abstract] OR metapopulation[Title/Abstract] OR \"network model\"[Title/Abstract] OR \"border discontinuity\"[Title/Abstract] OR \"spatial diffusion\"[Title/Abstract] OR \"gravity model\"[Title/Abstract] OR \"radiation model\"[Title/Abstract] OR Hawkes[Title/Abstract] OR phylogeograph*[Title/Abstract] OR \"genomic epidemiology\"[Title/Abstract])"
    },
    {
      "family": "forecasting_dynamics",
      "token": "FORECASTING",
      "method_block": "(\"renewal model\"[Title/Abstract] OR \"reproduction number\"[Title/Abstract] OR \"ensemble forecast\"[Title/Abstract] OR \"forecast calibration\"[Title/Abstract] OR \"early warning\"[Title/Abstract] OR changepoint[Title/Abstract] OR \"change point\"[Title/Abstract] OR \"outbreak detection\"[Title/Abstract] OR \"mechanistic-statistical\"[Title/Abstract])"
    },
    {
      "family": "evidence_synthesis",
      "token": "EVIDENCE",
      "method_block": "(triangulation[Title/Abstract] OR \"specification curve\"[Title/Abstract] OR multiverse[Title/Abstract] OR transportability[Title/Abstract] OR generalizability[Title/Abstract] OR \"outcome definition\"[Title/Abstract] OR denominator[Title/Abstract] OR \"hierarchical borrowing\"[Title/Abstract] OR \"modelled versus observed\"[Title/Abstract] OR \"modeled versus observed\"[Title/Abstract])"
    },
    {
      "family": "simulation_methods",
      "token": "SIMULATION",
      "method_block": "(\"simulation study\"[Title/Abstract] OR \"synthetic data\"[Title/Abstract] OR \"data-generating process\"[Title/Abstract] OR \"data generating process\"[Title/Abstract] OR \"agent-based\"[Title/Abstract] OR \"mechanistic model\"[Title/Abstract] OR benchmark*[Title/Abstract] OR \"operating characteristics\"[Title/Abstract] OR \"coverage probability\"[Title/Abstract])"
    }
  ]
}
```

`build_search_cells` uses the stored `method_block` unchanged for the venue lane. For the family lane it replaces every exact `[Title/Abstract]` field tag in that block with `[Title]`; it does not change words, Boolean operators, or the infectious-disease block.

- [ ] **Step 4: Create the journal coverage registry**

Use the exact header:

```csv
journal_id,title,group,search_role,pubmed_token,official_url,status,notes
```

Add active rows for: The Lancet; New England Journal of Medicine; JAMA; BMJ; PLOS Medicine; Nature; Science; Proceedings of the National Academy of Sciences; Nature Medicine; The Lancet Infectious Diseases; Clinical Infectious Diseases; Nature Microbiology; Emerging Infectious Diseases; Eurosurveillance; The Lancet Global Health; Epidemiology; International Journal of Epidemiology; American Journal of Epidemiology; npj Digital Medicine; npj Vaccines; npj Biofilms and Microbiomes; and npj Systems Biology and Applications. Use the exact PubMed journal token returned by an official PubMed/NLM query; do not guess abbreviations. `search_role` is `applied_seed`, and `notes` states `coverage device, not quality gate`.

`journal_id` is unique and matches `^J-[A-Z]+-[0-9]{3}$`. Allowed `group` values are `general_medicine`, `general_science`, `infectious_disease`, `global_health`, `epidemiology`, and `npj`. Allowed `search_role` values are `applied_seed`, `method_source`, and `both`. Allowed `status` values are `active` and `inactive`. Active PubMed tokens are unique and nonblank; title and official URL are mandatory.

- [ ] **Step 5: Create the minimal paper discovery record contract**

Create `PAPER_DISCOVERY_RECORD_TEMPLATE.md` with exactly:

```markdown
# P-YYYY-NNNN — Paper title

## Bibliographic control
- Paper ID:
- Verification state: discovery
- Record type:
- Title:
- Year:
- DOI:
- PMID:
- Primary or DOI URL:

## Discovery provenance
- Search IDs:
- Discovery route:
- Preliminary method family:
- Screening decision:
- Screening reason:

## Bibliographic role evidence
Record only what the title, abstract, or inspected primary record directly supports about whether this is an applied seed, method-source lead, diagnostic, correction, guidance, reproducibility resource, or simulation/mechanistic lead.

## Claim boundary and evidence defects
No substantive method, software, dataset, effect, or performance claim is verified at discovery state. List the exact primary source and sections that a later verification plan must inspect.
```

- [ ] **Step 6: Create the minimal method discovery record contract**

Create `METHOD_DISCOVERY_RECORD_TEMPLATE.md` with exactly:

```markdown
# M-FAMILY-NNN — Canonical discovery label

## Discovery control
- Method ID:
- Verification state: discovery
- Preliminary family:
- Canonical discovery label:
- Known label variants:
- Linked discovery paper IDs:
- Discovery search IDs:
- Author:
- Reviewer:
- Created date:
- Updated date:

## Structural problem lead
State only the preliminary problem class directly supported by inspected titles, abstracts, or primary records. Do not state an estimand, assumption, diagnostic, performance result, or software claim as verified.

## Lineage candidates
List candidate original/authoritative sources, corrections, diagnostics, guidance, and official implementations with their discovery routes and ambiguity status. These are leads, not normalized authoritative relationships.

## Infectious-disease transfer route
State the concrete infectious-disease context that made this concept eligible for discovery. Public-data access, AMR relevance, LMIC relevance, and solo workload remain unevaluated.

## Evidence defects and next verification action
List unresolved identity or lineage issues and the exact primary records/sections required by the next primary-source verification plan. A Stage 3 method card must not be created from this record until lineage and substantive claims are verified.
```

- [ ] **Step 7: Capture the external-worktree status baseline without writing there**

Create the baseline JSON from read-only commands. It contains exactly: `captured_at`, `timezone`, `source_repository`, `source_head`, `filtered_pointer_line`, `filtered_status_line_count`, `filtered_status_sha256`, `pointer_status`, `pointer_index_paths`, `seed_source_status`, and `proof_limit`. `proof_limit` is exactly `Path/status evidence only; no pre-phase byte manifest exists for paths already dirty at baseline.`

The filtered digest excludes only the exact pointer status line. Do not store or modify any source-worktree file.

- [ ] **Step 8: Review and commit the frozen search configuration**

Run:

```bash
python3 -m json.tool 01_search/search_protocols/discovery_queries.json >/dev/null
test "$(python3 -c 'import json; print(len(json.load(open("01_search/search_protocols/discovery_queries.json"))["families"]))')" -eq 6
test "$(($(wc -l < 01_search/journal_registry/journals.csv) - 1))" -eq 22
rg -n "discovery|verified|flagship|LMIC|simulation|primary" 01_search/search_protocols/2026-07-20-broad-methods-discovery-protocol.md
git diff --check
git add 00_governance/DECISION_LOG.md 01_search/search_protocols/2026-07-20-broad-methods-discovery-protocol.md 01_search/search_protocols/discovery_queries.json 01_search/journal_registry/journals.csv 01_search/PAPER_DISCOVERY_RECORD_TEMPLATE.md 01_search/METHOD_DISCOVERY_RECORD_TEMPLATE.md 07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json
git commit -m "define broad methods discovery protocol"
```

Expected: JSON parses; there are six families and 22 journal rows; the protocol states the claim and phase boundaries; external baseline contains only read-only status evidence; commit contains only the seven named files.

---

### Task 2: Build configuration and artifact validation test-first

**Files:**
- Create: `00_governance/tests/test_discovery_search.py`
- Create: `00_governance/scripts/discovery_search.py`
- Modify: `00_governance/scripts/validate_library.py`

**Interfaces:**
- Consumes: Task 1 query JSON, journal registry, and protocol.
- Produces: `load_configuration`, `validate_configuration`, `build_search_cells`, `validate_search_run`, and the discovery CLI contract.

- [ ] **Step 1: Write failing configuration tests**

Create tests covering these exact contracts:

```python
def test_configuration_builds_twelve_unique_cells(self):
    self.copy_configuration()
    errors = search.validate_configuration(self.root)
    cells = search.build_search_cells(self.root, date(2026, 7, 20))
    self.assertEqual(errors, [])
    self.assertEqual(len(cells), 12)
    self.assertEqual(len({cell.search_id for cell in cells}), 12)

def test_configuration_requires_all_six_families(self):
    self.copy_configuration()
    config = json.loads((self.root / search.QUERY_CONFIG_PATH).read_text())
    config["families"] = config["families"][:-1]
    (self.root / search.QUERY_CONFIG_PATH).write_text(json.dumps(config))
    self.assertIn("family set mismatch", "\n".join(search.validate_configuration(self.root)))

def test_journal_tokens_must_be_unique_and_nonblank(self):
    self.copy_configuration()
    path = self.root / search.JOURNAL_REGISTRY_PATH
    rows = list(csv.DictReader(path.open()))
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

def test_split_parent_requires_contiguous_nonoverlapping_children(self):
    run_dir = self.make_valid_split_run()
    receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text())
    receipt["cells"][0]["children"][1]["date_start"] = "2021/01/02"
    (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt))
    self.assertIn("split interval gap", "\n".join(search.validate_search_run(run_dir)))

def test_leaf_requires_history_and_page_fields(self):
    run_dir = self.make_valid_run()
    receipt = json.loads((run_dir / "RUN_RECEIPT.json").read_text())
    del receipt["cells"][0]["query_key"]
    (run_dir / "RUN_RECEIPT.json").write_text(json.dumps(receipt))
    self.assertIn("missing leaf receipt field", "\n".join(search.validate_search_run(run_dir)))

def test_external_boundary_rejects_filtered_status_change(self):
    self.make_external_boundary_fixture()
    self.mutate_source_porcelain_fixture()
    self.assertIn(
        "external filtered status mismatch",
        "\n".join(search.validate_external_boundary(self.root, self.source_root)),
    )

def test_screening_and_audit_validators_recompute_complete_coverage(self):
    run_dir = self.make_valid_screened_run()
    self.assertEqual(search.validate_screening(run_dir), [])
    self.assertEqual(search.validate_screening_audit(run_dir), [])
    self.delete_one_required_audit_row(run_dir)
    self.assertIn("missing required audit key", "\n".join(search.validate_screening_audit(run_dir)))

def test_verify_all_composes_every_phase_validator(self):
    phase_dir = self.make_valid_phase_run()
    self.assertEqual(search.validate_all(self.root, phase_dir), [])
    (phase_dir / "wave_02_synonym_expansion" / "RUN_RECEIPT.json").unlink()
    self.assertIn("wave_02", "\n".join(search.validate_all(self.root, phase_dir)))
```

Use temporary directories and Task 1 files as fixtures. Do not call the network in unit tests.

- [ ] **Step 2: Run the tests and confirm RED**

Run:

```bash
python3 -m unittest 00_governance/tests/test_discovery_search.py -v
```

Expected: import or missing-interface failure because `discovery_search.py` does not yet exist.

- [ ] **Step 3: Implement configuration loading and the 12-cell builder**

Implement the declared dataclass and constants. `build_search_cells` must produce one `FAMILY` and one `VENUE` cell per family. The venue query adds the OR-combined active PubMed journal tokens. Both lanes add the applied date range. Preserve exact query text in each `SearchCell`.

The stable validation errors are:

```text
required discovery file missing
invalid discovery query JSON
family set mismatch
duplicate family token
journal header mismatch
blank pubmed_token
duplicate pubmed_token
invalid journal status
invalid journal_id
invalid journal group
invalid journal search_role
blank journal title
blank official_url
duplicate search_id
```

- [ ] **Step 4: Implement manifest and receipt validation**

Use this exact manifest shape:

```json
{
  "algorithm": "SHA256",
  "files": [
    {
      "path": "raw/SEARCH-ID.esearch.json",
      "sha256": "64-lowercase-hex"
    },
    {
      "path": "raw/SEARCH-ID.efetch.000000000-000000199.xml",
      "sha256": "64-lowercase-hex"
    },
    {
      "path": "raw/SEARCH-ID.efetch.000000200-000000399.xml",
      "sha256": "64-lowercase-hex"
    }
  ]
}
```

Wave 1/2 `RUN_RECEIPT.json` requires: `schema_version`, `executed_at`, `timezone`, `tool_version`, `source`, `cells`, and `configuration_files`. `configuration_files` is an array with exactly three `path`/`sha256` objects for the protocol, query JSON, and journal registry for Wave 1; Wave 2 additionally includes its exact query-registry path/SHA. Every PubMed cell requires: `search_id`, `lane`, `family`, `query`, nonblank `date_start`, nonblank `date_end`, `reported_count`, `parent_search_id`, `cell_type`, `esearch_path`, `esearch_sha256`, and `status`.

A `split_parent` has `retrieved_count=0`, a separately manifested raw ESearch response matching `esearch_path`/`esearch_sha256`, no persisted or used history/page fields, and a nonempty `children` list whose intervals are contiguous, non-overlapping, and exactly cover the parent interval. Only leaf descendants contribute retrieved records.

An executable `leaf` has `reported_count < 10000`, `usehistory=true`, nonblank `webenv`, nonblank `query_key`, `retrieved_count`, and `efetch_pages`. Each page has `retstart`, `retmax`, `path`, `sha256`, and `parsed_count`. `parsed_count` is the number of direct `PubmedArticleSet` children whose tag is `PubmedArticle` or `PubmedBookArticle`. Page ranges start at zero, are contiguous/non-overlapping, use `retmax <= 200`, and end exactly at the source count. The raw page files are preserved exactly; no XML concatenation or reserialization is called raw. `compiled_candidates_raw.csv` is explicitly a derived artifact and has its own SHA entry.

Validation rejects path traversal, duplicate manifest paths, missing files, non-regular files, checksum mismatch, absent receipt fields, a non-integer or negative count, leaf counts at or above 10,000, split gaps/overlaps, page gaps/overlaps, a page SHA disagreement with the manifest, `retrieved_count != reported_count` for leaves, parent records counted as retrieved, and receipt paths absent from the manifest.

Wave 3 uses separate source-conditional `LINEAGE_RUN_RECEIPT.json` with top-level `schema_version`, `executed_at`, `timezone`, `tool_version`, `configuration_files`, and `queries`. Its `configuration_files` contains exactly four path/SHA objects: protocol, query JSON, journal registry, and lineage query registry. Common query-row fields are `query_id`, `source`, `query`, `reported_count`, `raw_path`, `raw_sha256`, and `status`. PubMed rows additionally require blank `date_start`/`date_end`, `query_scope=unbounded_identity`, `esearch_path`, `esearch_sha256`, `usehistory=true`, nonblank `webenv`, nonblank `query_key`, and `efetch_pages`; `raw_path`/`raw_sha256` equal the ESearch path/SHA. Crossref rows additionally require `response_path`, `response_sha256`, `returned_candidate_count`, `total_results`, and `rows=5`; `raw_path`/`raw_sha256` equal the response path/SHA. Crossref rows prohibit `esearch_path`, `esearch_sha256`, `usehistory`, `webenv`, `query_key`, and `efetch_pages`. `validate_lineage` checks these source-conditional fields and every referenced manifest entry.

- [ ] **Step 5: Integrate search configuration into the repository validator**

Add the five Task 1 search/config/template files, the external-boundary receipt, and `00_governance/scripts/discovery_search.py` to `REQUIRED_PATHS`. Import or call `validate_configuration(root)` and prefix returned errors with `discovery configuration: `. Implement `verify-external-boundary` so it recomputes the filtered status line count/SHA, exact pointer status/index absence, seed-source status, and source HEAD comparison without writing to the source root. A changed source HEAD is reported separately from a path/status mismatch; neither is converted into byte-identity evidence. Do not require an executed search run until Task 4 adds Wave 1 and its verification report.

- [ ] **Step 6: Run GREEN and commit**

Run:

```bash
python3 -m unittest 00_governance/tests/test_discovery_search.py -v
python3 -m unittest 00_governance/tests/test_validate_library.py -v
python3 00_governance/scripts/discovery_search.py validate-config --root .
python3 00_governance/scripts/validate_library.py --root .
git diff --check
git add 00_governance/scripts/discovery_search.py 00_governance/tests/test_discovery_search.py 00_governance/scripts/validate_library.py
git commit -m "validate discovery search artifacts"
```

Expected: all old and new tests pass; both CLIs print their PASS token; commit contains only the three named files.

---

### Task 3: Implement deterministic PubMed retrieval and metadata compilation

**Files:**
- Modify: `00_governance/tests/test_discovery_search.py`
- Modify: `00_governance/scripts/discovery_search.py`

**Interfaces:**
- Consumes: validated 12-cell configuration.
- Produces: atomic PubMed ESearch/per-page EFetch snapshots, split-tree receipts, manifest records, Crossref resolution candidates, and derived `compiled_candidates_raw.csv` tables.

- [ ] **Step 1: Add failing retrieval tests with a fake opener**

Tests must demonstrate:

1. query text is URL-encoded and preserved in the receipt;
2. ESearch sends `usehistory=y`, preserves `WebEnv` and `query_key`, and those exact values drive paginated EFetch calls in batches of 200;
3. every split parent and leaf ESearch response is separately manifested; every raw EFetch page is separately manifested; and a leaf is complete only when the summed direct-child `PubmedArticle` plus `PubmedBookArticle` count equals the source-reported count;
4. HTTP, timeout, malformed JSON, malformed XML, and count mismatches return stable errors with no final partial file;
5. a valid completed leaf whose ESearch/page SHA values match is skipped on resume; an incomplete leaf is restarted with a fresh history session and no old partial final files;
6. recursive split parents preserve their ESearch raw path/SHA, terminate into contiguous non-overlapping year, month, then day leaves below 10,000, and an unsplittable day fails;
7. matching PMID or normalized DOI auto-deduplicates; matching normalized titles without matching identifiers creates a `possible_duplicate_group` and does not auto-delete a row;
8. a Crossref resolution request stores a bounded raw candidate response with no automatic decision and can be resolved only by the later independently audited named-source identity decision;
9. `run-wave` rejects a malformed/missing-family Wave 2 registry, executes only `status=executed` rows, and accepts the exact all-`no_expansion_needed` empty-artifact contract;
10. `run-lineage` rejects a malformed or over-three-query named-source group, dispatches each valid registry row to PubMed history retrieval or the bounded Crossref resolver according to `source`, and fails a PubMed identity query reporting 10,000 or more matches with `overbroad lineage identity query` before EFetch;
11. a valid heterogeneous Wave 3 receipt with one PubMed and one Crossref row passes, while a Crossref row containing any ESearch/history/page field fails with `crossref receipt contains pubmed field`;
12. lineage validation accepts one independently audited terminal named-source decision covering all of that source's query IDs, and rejects an unaudited rejection, same-person audit, orphan query, reused query, missing/tampered candidate table, candidate borrowed from another query/source, stage-specific invalid selected key, two resolved reviewers selecting different keys without conflict, open resolved status, or ledger/final-key mismatch with stable errors.

Use fake responses; never call NCBI from the test suite.

- [ ] **Step 2: Run focused RED tests**

Run:

```bash
python3 -m unittest 00_governance.tests.test_discovery_search.DiscoverySearchTests.test_execute_pubmed_cell_writes_atomic_complete_artifacts -v
python3 -m unittest 00_governance.tests.test_discovery_search.DiscoverySearchTests.test_compile_flags_title_only_possible_duplicates -v
```

Expected: FAIL because retrieval and compilation are not implemented.

- [ ] **Step 3: Implement ESearch and complete EFetch retrieval**

Use official NCBI endpoints:

```text
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi
```

ESearch parameters are `db=pubmed`, `term=<exact query>`, `retmode=json`, `retmax=0`, `usehistory=y`, `tool=ID_Epi_Methods_Library`, `email=<CLI value>`, and optional runtime `api_key`. Parse `count`, `webenv`, and `querykey` from the response. EFetch uses `db=pubmed`, `retmode=xml`, `rettype=abstract`, the exact returned `WebEnv`, exact returned `query_key`, `retstart`, `retmax=200`, and the same tool/email/API-key values. Sleep at least 0.34 seconds between requests without a key or 0.11 seconds with one; never commit a key or write it to a receipt.

Before EFetch, recursively count/split any interval with 10,000 or more matches by calendar year, then month, then day. Every ESearch response, including a split parent's, is atomically saved in its own raw file and manifested before its count is used. Parent search IDs record ESearch path/SHA, child IDs, and counts; only leaves persist/use history fields and call EFetch. A day with 10,000 or more matches raises `unsplittable PubMed cell` and stops.

Write each page to a unique `*.tmp` sibling, parse it, count both direct-child record types (`PubmedArticle` and `PubmedBookArticle`), record its independent count/SHA, then use `Path.replace`. Publish the leaf receipt/manifest entry only after all pages reconcile. On failure remove only exact temporary siblings and any uncommitted page finals for that leaf; keep previously verified leaves and waves. Compilation extracts both record types and preserves a stable bibliographic row whenever either supplies the required identity fields.

- [ ] **Step 4: Implement deterministic PubMed XML compilation**

Write the immutable derived baseline `compiled_candidates_raw.csv` with this exact header:

```csv
candidate_key,row_sha256,pmid,doi,title,year,journal,authors,abstract,publication_types,search_ids,lanes,preliminary_families,source_url,deduplication_basis,possible_duplicate_group
```

Auto-deduplicate only on PMID, then normalized lowercase DOI. `candidate_key` is `PMID:<id>`, otherwise `DOI:<doi>`, otherwise `TITLE:<sha256-of-normalized-title-year-journal-prefix-16>`. Rows sharing only a Unicode-normalized lowercase title receive the same `possible_duplicate_group` and remain separate until human adjudication. Merge provenance only for identifier-confirmed duplicates as sorted pipe-separated unique values. Keep abstract text exactly as returned except XML entity decoding and whitespace normalization. `row_sha256` hashes the canonical JSON serialization of every bibliographic/provenance field except itself.

- [ ] **Step 5: Implement bounded Crossref candidate resolution and lineage validation**

Use `https://api.crossref.org/works` with `query.bibliographic=<exact title or method-source citation>`, `rows=5`, `select=DOI,title,published,container-title,author,type,URL`, and `mailto=<email>`. Save each raw JSON response separately and manifest it. Do not use cursor pagination because each query is an explicitly bounded five-candidate identity-resolution request, not a corpus download.

`run-lineage` generates and manifests two source-specific derived candidate tables, including header-only files when a source has no registry row:

`pubmed_lineage_candidates.csv`:

```csv
candidate_key,query_id,named_source_id,candidate_rank,pmid,doi,title,year,journal,authors,source_url,raw_path,raw_sha256
```

`crossref_candidates.csv`:

```csv
candidate_key,query_id,named_source_id,bibliographic_query,candidate_rank,doi,title,year,container_title,first_author,type,url,raw_path,raw_sha256
```

PubMed `candidate_key` uses the same PMID/DOI/title fallback contract as applied compilation and points to the exact EFetch page. Crossref `candidate_key` is `DOI:<normalized-doi>` when present and otherwise `CROSSREF:<query_id>:<zero-padded-rank>`. Candidate rank preserves source-return order within each query. Both tables contain no decision fields. The sole human decision is the later named-source decision in `lineage_identity_audit.csv`, made after comparing every considered candidate's title, year, author, container, DOI, and inspected primary/publisher record. `verify-lineage` rejects missing or unmanifested candidate tables, row/raw SHA disagreement, candidate keys outside their named source/query response, automatic identity decisions, or a resolved choice lacking a primary URL in the audit and lineage ledger.

`run-wave` consumes the exact Wave 2 registry schema defined in Task 5, validates one row for every family and the executed/no-expansion field rules, then applies the same PubMed history, recursive-split, per-page raw, receipt, and resume contract to each executed row.

`run-lineage` consumes `LINEAGE_QUERY_REGISTRY.csv` with this exact header:

```csv
query_id,named_source_id,method_label,canonical_name,family,source_role,source,query_variant,query,seed_candidate_keys,reviewer
```

`source` is `pubmed` or `crossref`; `query_variant` is `exact_title`, `title_first_author`, or `method_author_year`; `source_role` is one of `original_candidate`, `authoritative_candidate`, `correction`, `diagnostic`, `guidance`, `implementation`, or `infectious_application`; and every `named_source_id` has one to three unique ordered variants. PubMed lineage rows are exact, unbounded-by-date identity queries: `LINEAGE_RUN_RECEIPT.json` uses blank `date_start`/`date_end` plus `query_scope=unbounded_identity`. They use ESearch history and complete per-page EFetch only when the count is below 10,000; a count at or above 10,000 fails with `overbroad lineage identity query`, writes no EFetch pages, and requires an explicit registry revision rather than silent date filtering or capping. Crossref rows use the five-candidate contract above and the Task 2 Crossref receipt fields. `run-lineage` writes the source-conditional receipt with exact source/count/raw path/SHA per query and a single manifest covering all raw responses and both derived candidate tables; it never treats a candidate as an automatic identity decision.

Implement the aggregate `verify-all` action as a pure composition of configuration validation, each immutable wave's search-run validation, Wave 1/2 screening and audit validation, Wave 3 lineage validation, global key reconciliation, and the repository validator. It must name the failing component and must not downgrade or suppress component errors. Before later artifacts exist it fails explicitly rather than treating an absent wave as empty.

- [ ] **Step 6: Run GREEN, malformed-input probes, and commit**

Run:

```bash
python3 -m unittest 00_governance/tests/test_discovery_search.py -v
python3 -m unittest 00_governance/tests/test_validate_library.py -v
python3 00_governance/scripts/discovery_search.py validate-config --root .
python3 00_governance/scripts/validate_library.py --root .
git diff --check
git add 00_governance/scripts/discovery_search.py 00_governance/tests/test_discovery_search.py
git commit -m "add reproducible PubMed discovery retrieval"
```

Expected: all tests pass; malformed fixture probes exit `1` with `DISCOVERY FAIL` and no traceback; repository validator passes.

---

### Task 4: Execute and freeze Wave 1's complete 12-cell search corpus

**Files:**
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/raw/*`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/MANIFEST_SHA256.json`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/RUN_RECEIPT.json`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/compiled_candidates_raw.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/COUNT_RECONCILIATION.txt`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/search_logs/*.md`

**Interfaces:**
- Consumes: Task 3 CLI and frozen configuration.
- Produces: an immutable Wave 1 raw/derived corpus; no screening decision is stored in the raw table.

- [ ] **Step 1: Capture the pre-run state and configuration hashes**

Run the status, three configuration SHA commands, and `list-cells`. Expected: clean task worktree and exactly 12 unique root cells. Save the three hashes in the Wave 1 receipt.

- [ ] **Step 2: Execute every root cell and all required split leaves**

Run:

```bash
python3 00_governance/scripts/discovery_search.py run \
  --root . \
  --date 2026-07-20 \
  --email "$(git config user.email)" \
  --output 01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries
```

The program performs count-first recursive date splitting and complete per-page EFetch retrieval. It must never request or count a split parent as a leaf, cap a result, or concatenate raw XML pages.

- [ ] **Step 3: Compile the immutable raw baseline and verify the wave**

Run `compile` and `verify` against the Wave 1 directory. `compiled_candidates_raw.csv` is manifested after deterministic PMID/DOI deduplication and title-only duplicate grouping. Each search log copies exact root/leaf queries, split tree, counts, page paths/SHAs, timestamps, and deviations. Screening status is `not started`.

- [ ] **Step 4: Independently reconcile every page and leaf count**

Use a separate standard-library parser that counts direct `PubmedArticleSet` children tagged `PubmedArticle` or `PubmedBookArticle` in every manifested page, sums per leaf, and reconciles leaf/root totals without double-counting split parents. It also proves every root, split-parent, and leaf ESearch raw response is manifested and matches the receipt SHA. Save one line per leaf and end with `ALL LEAF AND ROOT COUNTS MATCH`. The reconciliation parser must not import the production count function.

- [ ] **Step 5: Review and commit Wave 1**

Run the wave verifier, Library validator, and whitespace check. Commit only the Wave 1 directory with subject `freeze broad applied methods discovery search`.

Expected: 12 root cells and all leaf descendants verify; all raw pages and the derived baseline are manifested; no record has a screening or evidence-verification claim.

---

### Task 5: Screen Wave 1 and execute the complete synonym-expansion wave

**Files:**
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/screening_batches/*`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/screened_candidates.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/screening_audit.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/*`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/candidates_through_wave_02.csv`
- Create: `07_reviews/discovery_screening/*.md`

**Interfaces:**
- Consumes: immutable Wave 1 raw candidates.
- Produces: complete screened/audited Wave 1 and Wave 2 delta decisions plus a cross-wave key index.

- [ ] **Step 1: Freeze deterministic 150-record Wave 1 batches**

Sort unique raw rows by primary family precedence and candidate key. Split into consecutive batches of at most 150. Every batch manifest records: `batch_id`, source raw CSV path/SHA, protocol path/SHA, row count, first/last key, and ordered `candidate_keys`. Each key appears in exactly one primary batch.

Each batch writes strict CSV rows with this header:

```csv
candidate_key,source_row_sha256,primary_decision,primary_proposed_record_type,primary_reason_code,primary_reason,primary_reviewer,batch_id,retained_candidate_key
```

- [ ] **Step 2: Perform actual semantic title/abstract reading for every Wave 1 key**

For each batch, read every title and available abstract and assign an allowed decision, record-type mapping, decision-bound reason code, one-sentence rationale, and reviewer. Duplicate exclusion requires a human comparison and `retained_candidate_key`. Invalid rationales such as `relevant`, `interesting`, `top journal`, or `not suitable` alone fail validation.

The Task 5 implementation subagent is the sole file-writing integrator. It may dispatch multiple bounded, non-writing semantic-reader agents over disjoint manifested batches; each reader returns strict rows only for its assigned keys. Before merging, the integrator verifies batch SHA, exact ordered key coverage, allowed enums, rationale quality, and zero cross-batch duplicates. Audit batches go to readers who did not perform the corresponding primary decision. Reader agents never edit files, commit, or alter gates.

- [ ] **Step 3: Generate and execute the deterministic independent audit**

Write `screening_audit.csv` with:

```csv
candidate_key,source_row_sha256,primary_reviewer,audit_stratum,audit_rank,audit_reviewer,primary_decision,primary_reason_code,primary_proposed_record_type,audit_decision,audit_reason_code,audit_proposed_record_type,audit_reason,conflict_status,adjudicator,final_decision,final_reason_code,final_proposed_record_type,final_reason
```

Audit 100% of uncertain records and `X_NOT_INFECTIOUS_TRANSFERABLE` exclusions. For every other primary-decision × reason-code × primary-family stratum—including inclusion strata—compute `audit_rank = sha256(candidate_key + "|audit-v1")`, sort ascending, and select `max(10, ceiling(0.10 * stratum_size))`, capped at the stratum size. `audit_reviewer` must differ from `primary_reviewer`. Allowed conflict states are `none`, `open`, and `resolved`; open conflicts use `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, and blank final proposed type, and may not enter a registry. Audit and final decision/code/type triples obey the same exact mapping as primary triples.

- [ ] **Step 4: Preserve the raw baseline and validate screening/audit closure**

Combine batch and audit decisions into the derived `screened_candidates.csv` with exact header:

```csv
candidate_key,source_row_sha256,primary_decision,primary_proposed_record_type,primary_reason_code,primary_reason,final_decision,final_proposed_record_type,final_reason_code,final_reason,primary_reviewer,batch_id,audit_status,retained_candidate_key
```

`audit_status` is `not_selected`, `agree`, `conflict_open`, or `conflict_resolved`. Unselected rows copy the primary triple/reason into final fields; audited rows take final fields only from the audit/adjudication record. Do not edit `compiled_candidates_raw.csv` or primary batch outputs. `validate-screening` checks exact key coverage, each `source_row_sha256`, primary and final decision/reason/type mappings, duplicate retention rules, and that only final inclusion triples are registry-eligible. `validate-audit` recomputes all strata/ranks/sample sizes, checks reviewer independence, validates primary/audit/final triples separately, and rejects missing or falsely closed conflicts.

- [ ] **Step 5: Derive and execute Wave 2 synonym-gap queries**

After Wave 1 validation, create exactly one `QUERY_REGISTRY.csv` row per family with header:

```csv
family,search_id,status,new_synonyms,rationale,source_candidate_keys,source,query,date_start,date_end,reviewer
```

Allowed status is `executed` or `no_expansion_needed`. An executed row has a unique search ID, `source=pubmed`, exact query, both dates, genuinely distinct labels found during Wave 1 screening, and retains the infectious-disease/date blocks. A `no_expansion_needed` row has blank search ID/source/query/dates but requires a rationale and inspected source keys. Execute with `run-wave`, manifest, compile, and verify the complete Wave 2 delta in its own directory.

```bash
python3 00_governance/scripts/discovery_search.py run-wave \
  --root . \
  --query-registry 01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/QUERY_REGISTRY.csv \
  --email "$(git config user.email)" \
  --output 01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion
```

If all six families are `no_expansion_needed`, Wave 2 is still a valid immutable empty wave: `RUN_RECEIPT.json` contains zero cells, `empty_reason=all_families_no_expansion_needed`, and the query-registry path/SHA; `MANIFEST_SHA256.json` covers the registry plus header-only `compiled_candidates_raw.csv`, `screened_candidates.csv`, and `screening_audit.csv`; `raw/` is absent or empty. `verify`, `validate-screening`, and `validate-audit` accept this exact state and reject any other missing-wave shortcut.

- [ ] **Step 6: Screen and independently audit every Wave 2 delta key**

Remove only PMID/DOI duplicates already present in Wave 1, preserving provenance. Screen remaining Wave 2 keys in 150-record batches using the identical schema and audit algorithm. Reconcile every raw Wave 2 key to either an identifier-confirmed earlier key or one complete Wave 2 screening decision.

- [ ] **Step 7: Create the cross-wave key index and commit**

`candidates_through_wave_02.csv` records `candidate_key,waves,wave_source_row_sha256s,screening_path,final_decision,final_proposed_record_type,final_reason_code,duplicate_disposition`. There is exactly one global row per identifier-level candidate key. `waves` is the sorted pipe-separated contributing wave set; `wave_source_row_sha256s` contains sorted `wave:sha256` pairs; a Wave 2 identifier duplicate points to the retained Wave 1 screening path and uses `duplicate_disposition=screened_in_wave_01`. Validate Wave 1, Wave 2, both audits, and global key coverage; run Library validator and whitespace check. Commit screening/audit artifacts, Wave 2, and the global index with subject `screen broad methods discovery records`.

Expected: raw baselines remain immutable; every Wave 1/2 key is screened or identifier-deduplicated; every required audit row is independent and closed or honestly uncertain; no registry promotion has occurred.

---

### Task 6: Trace method lineage and register discovery-state papers and methods

**Files:**
- Create: `01_search/discovery_records/P-YYYY-NNNN.md`
- Create: `01_search/method_discovery_records/M-FAMILY-NNN.md`
- Modify: `03_evidence_tables/papers.csv`
- Modify: `03_evidence_tables/methods.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/LINEAGE_QUERY_REGISTRY.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/LINEAGE_RUN_RECEIPT.json`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/pubmed_lineage_candidates.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/crossref_candidates.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/lineage_identity_audit.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/*`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/lineage_ledger.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/discovery_relationships.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/lineage_logs/*.md`

**Interfaces:**
- Consumes: retained and uncertain screened records.
- Produces: stable discovery-state paper/method IDs and provisional discovery-role evidence outside the authoritative link registry; substantive claims remain unverified.

- [ ] **Step 1: Build a provisional canonical-method label table**

Group retained leads by actual design concept, not keyword. Keep variants distinct when their estimands or identification assumptions differ. Examples that must not be silently collapsed include simple versus controlled ITS, legacy versus heterogeneity-robust staggered DiD, descriptive spatial clustering versus endemic–epidemic models, and mechanistic simulation versus estimator operating-characteristic studies.

Every merge/split decision records the labels, retained canonical name, family, evidence inspected, reviewer, and decision rationale. Freeze canonical concepts in deterministic batches of at most 50 concepts; each batch manifest stores the through-Wave-2 index SHA, ordered concept labels, first/last label, and row count.

- [ ] **Step 2: Execute bounded lineage tracing for every canonical method concept**

For each concept, inspect every retained discovery record assigned to that concept and run bounded exact lineage resolution. Attempt to locate:

1. original or currently authoritative method source;
2. later correction or limitation paper when directly named;
3. accepted diagnostic/reporting guidance when directly named;
4. official implementation or reproduction resource when directly named;
5. at least one informative infectious-disease application when one exists.

For each named/cited source, preregister one to three documented identity queries in `LINEAGE_QUERY_REGISTRY.csv`: exact title; exact title plus first author; and method name plus first author/year. PubMed identity search is preferred when indexed; otherwise select Crossref. Execute the frozen registry with `run-lineage`. Every raw response is stored in Wave 3 and manifested. After all queries for one `named_source_id` terminate, create exactly one named-source identity decision that cites every supporting query and every candidate considered. Allowed terminal decisions are `resolved`, `ambiguous`, `rejected`, and `unresolved_after_three_queries`; a distinct reviewer audits 100% of all four terminal states. Do not create an authoritative normalized link in this phase.

Run:

```bash
python3 00_governance/scripts/discovery_search.py run-lineage \
  --root . \
  --query-registry 01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/LINEAGE_QUERY_REGISTRY.csv \
  --email "$(git config user.email)" \
  --output 01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution
```

The lineage ledger header is:

```csv
identity_decision_id,named_source_id,final_candidate_key,method_label,canonical_name,family,source_role,title,year,doi,pmid,primary_url,discovery_route,bibliographic_role_evidence,verification_state,search_ids,status,notes
```

All rows use `verification_state=discovery`. `search_ids` is the sorted pipe-separated supporting query-ID set. Allowed `status` values are `resolved_identity_role_unverified`, `ambiguous`, `rejected`, and `unresolved_after_three_queries`. Even `resolved_identity_role_unverified` means bibliographic identity is resolved while authoritative/source role awaits the next primary-source verification plan.

Write `lineage_identity_audit.csv` with:

```csv
identity_decision_id,named_source_id,supporting_query_ids,candidate_keys_considered,primary_selected_candidate_key,primary_decision,primary_reason,primary_reviewer,audit_selected_candidate_key,audit_decision,audit_reason,audit_reviewer,conflict_status,adjudicator,final_selected_candidate_key,final_decision,final_reason,inspected_primary_url
```

Allowed primary/audit/final identity decisions are `resolved`, `ambiguous`, `rejected`, and `unresolved_after_three_queries`; allowed conflict states are `none`, `open`, and `resolved`. There is exactly one audit row per `named_source_id` and `identity_decision_id`. `supporting_query_ids` is the sorted pipe-separated complete set of that named source's 1–3 registry query IDs; every executed Wave 3 query appears in exactly one such set, never zero or two. `candidate_keys_considered` is the sorted pipe-separated set drawn only from manifested PubMed/Crossref candidate rows for those supporting queries.

Each stage's selected-key field is validated against its own decision: `primary_selected_candidate_key`, `audit_selected_candidate_key`, or `final_selected_candidate_key` is nonblank and belongs to the considered set exactly when that stage's decision is `resolved`; it is blank for the other three decisions. Equality of decision labels is not agreement when two resolved stages select different candidate keys; that is a conflict. The lineage ledger's `final_candidate_key` equals `final_selected_candidate_key` for resolved outcomes and is blank otherwise, and its title/IDs/URL must derive from that exact candidate row.

The audit reviewer differs from the primary reviewer, and every terminal primary decision—including `rejected` and `unresolved_after_three_queries`—is independently audited. An open conflict has `final_decision=ambiguous` and may not populate a resolved ledger row. A resolved conflict requires a named adjudicator and final reason. Every final `resolved` row has a nonblank inspected publisher/primary URL, and the matching lineage-ledger row uses `status=resolved_identity_role_unverified` with the same URL; the other final decisions map exactly to their same-named ledger statuses. `verify-lineage` checks complete query/decision/audit coverage, reviewer independence, conflict closure, one-to-one decision IDs, candidate provenance, URLs, and ledger/audit agreement.

- [ ] **Step 3: Assign permanent paper IDs and create paper discovery records**

Assign IDs by publication year, then stable sort on normalized DOI, PMID, and title. Continue from existing IDs if any; never renumber committed IDs. Populate `papers.csv` only for retained papers whose `final_decision` is an inclusion, `final_reason_code` and `final_proposed_record_type` form a valid mapped triple, identity is resolved, and title/year/primary-or-DOI URL are present. Uncertain/open-conflict/ambiguous-identity records remain only in search ledgers. `card_path` points to the paper discovery record.

Each paper record is instantiated from `PAPER_DISCOVERY_RECORD_TEMPLATE.md`. Bibliographic-role evidence cites the inspected title/abstract/primary record; the claim-boundary section remains explicit.

- [ ] **Step 4: Assign method IDs and create minimal method discovery records**

Assign IDs using the approved prefix mapping and stable alphabetical ordering within family. Instantiate `METHOD_DISCOVERY_RECORD_TEMPLATE.md` under `01_search/method_discovery_records/`. Point `methods.csv.card_path` to that minimal record. Do not create or modify any Stage 3 method card under the six `02_method_library/<family>/` directories in this phase.

- [ ] **Step 5: Record provisional discovery relationships outside the authoritative registry**

Leave `03_evidence_tables/paper_method_links.csv` header-only. Create `discovery_relationships.csv` with:

```csv
paper_id,method_id,provisional_role,verification_state,evidence_location,search_id,status,notes
```

Allowed provisional roles mirror the normalized relationship enum, but every row uses `verification_state=discovery` and `status=not_authoritative_until_primary_source_verification`. Evidence location names the inspected title/abstract/primary-record section. Do not infer relationships from keyword co-occurrence, citation order, or journal prestige. The next plan must verify before copying any row into the normalized link registry.

- [ ] **Step 6: Validate registries/cards and commit**

Run:

```bash
python3 00_governance/scripts/validate_library.py --root .
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir 01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir 01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir 01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir 01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion
python3 00_governance/scripts/discovery_search.py verify-lineage --root . --run-dir 01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution
git diff --check
git add 01_search/discovery_records 01_search/method_discovery_records 01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution 01_search/search_logs/2026-07-20-broad-discovery/global/lineage_ledger.csv 01_search/search_logs/2026-07-20-broad-discovery/global/discovery_relationships.csv 01_search/search_logs/2026-07-20-broad-discovery/global/lineage_logs 03_evidence_tables/papers.csv 03_evidence_tables/methods.csv
git commit -m "register discovery methods and lineage leads"
```

Expected: all IDs, required fields, card paths, and enums validate; every new entity registry row remains `discovery`; normalized relationship/translation/dataset/simulation registries remain header-only; every Wave 3 identity decision is independently audited or honestly unresolved.

---

### Task 7: Audit cross-wave family coverage and residual uncertainty

**Files:**
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/COVERAGE_AUDIT.md`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/coverage_matrix.csv`
- Create: `01_search/search_logs/2026-07-20-broad-discovery/global/GLOBAL_KEY_RECONCILIATION.txt`

**Interfaces:**
- Consumes: executed search, screening, lineage, and registry artifacts.
- Produces: an honest coverage assessment and the exact unresolved scope for the next verification plan.

- [ ] **Step 1: Build the six-family coverage matrix**

Use this header:

```csv
family,wave_01_root_cells,wave_01_leaf_cells,wave_02_status,wave_02_unique_delta,wave_03_lineage_queries,unique_candidates,retained_applied_seeds,retained_method_source_leads,retained_diagnostic_correction_leads,retained_simulation_mechanistic_leads,canonical_method_concepts,unresolved_records,unresolved_lineage,new_synonym_labels,new_lineage_role_candidates,coverage_verdict,notes
```

Counts are computed from all three wave receipts, screened ledgers, audits, registries, and lineage ledgers, not manually copied.

- [ ] **Step 2: Reconcile every cross-wave candidate and concept key**

Prove that every Wave 1/2 raw candidate key is identifier-deduplicated or has exactly one final screened decision, every included resolved-identity paper maps to one permanent paper ID, every canonical concept maps to one method discovery ID, and every Wave 3 query has one terminal audited status. Save counts and end with `ALL WAVE, SCREENING, REGISTRY, AND LINEAGE KEYS RECONCILE`.

- [ ] **Step 3: Confirm immutable waves and absence of post-screen search additions**

Verify each wave manifest/receipt independently, then confirm global indexes reference only manifested wave artifacts. No search may be executed or appended in Task 7. Any newly discovered synonym or lineage lead is recorded as a residual gap for a future plan, not inserted after screening closure.

- [ ] **Step 4: Write coverage verdicts without claiming exhaustiveness**

Allowed verdicts are:

```text
adequate_for_primary_source_verification
provisional_with_documented_gaps
insufficient_requires_search_revision
```

No verdict may use `complete`, `exhaustive`, or `saturated`. A family is `adequate_for_primary_source_verification` only when both frozen root cells and all leaves executed, Wave 1/2 screening/audits are complete, at least one applied or simulation/mechanistic lead is retained, at least one method-source candidate or explicit unresolved three-query lineage attempt exists, and Wave 2/3 bounded expansion evidence is documented.

- [ ] **Step 5: Commit the coverage audit before the Task 7 review gate**

Run:

```bash
python3 00_governance/scripts/discovery_search.py verify-all --root . --run-dir 01_search/search_logs/2026-07-20-broad-discovery
python3 00_governance/scripts/validate_library.py --root .
git diff --check
git add 01_search/search_logs/2026-07-20-broad-discovery/global
git commit -m "audit broad methods discovery coverage"
```

Expected: the audit names gaps rather than relaxing gates; all immutable waves and keys reconcile; Task 7 added no search record. After this implementation commit, execute the global per-task package/review/fix/receipt gate for Task 7 before dispatching Task 8.

---

### Task 8: Verify, hand off, merge, and publish the discovery phase

**Files:**
- Create: `07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md`
- Create after Task 8's per-task gate: `07_reviews/BROAD_DISCOVERY_REVIEW_20260720.md`
- Modify: `HANDOFF.md`

**Interfaces:**
- Consumes: all Tasks 1–7 and independent review verdicts.
- Produces: a verified and published discovery-state Library whose next plan is primary-source verification and method-card extraction.

- [ ] **Step 1: Run all automated and structural checks**

Run:

```bash
python3 -m unittest 00_governance/tests/test_validate_library.py -v
python3 -m unittest 00_governance/tests/test_discovery_search.py -v
python3 00_governance/scripts/discovery_search.py validate-config --root .
python3 00_governance/scripts/discovery_search.py verify-all --root . --run-dir 01_search/search_logs/2026-07-20-broad-discovery
python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR
python3 00_governance/scripts/validate_library.py --root .
git diff --check
git status --short --branch
```

Expected: tests and all validators pass; only the planned verification/HANDOFF edits are uncommitted.

- [ ] **Step 2: Recheck immutable bootstrap and external-boundary receipts**

Run:

```bash
shasum -a 256 docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
shasum -a 256 docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
cmp -s 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR
git ls-remote origin refs/heads/main
```

Expected: locked hashes and seed byte comparison pass; the current filtered source status digest/line count and pointer/index/source states equal the phase-start receipt; the report repeats that this is path/status rather than dirty-file byte proof; remote `main` still equals the pre-merge local baseline.

- [ ] **Step 3: Write the verification report from live outputs**

Record exact date/time/timezone, Python/Git versions, task commits and reviews, query/config hashes, every search ID and source count, total raw/retrieved/deduplicated/screened counts, screening decisions/reason codes, audit sample and agreement, retained record/method counts by family, lineage-role counts, coverage verdicts, manifest verification, registry validation, immutable SHAs, source-worktree status boundary, and all deferred work.

The report must explicitly state:

```text
This phase produced discovery leads and bibliographic-role records, not verified substantive method claims. It did not select a flagship, verify public-data feasibility, download candidate datasets, or execute a formal simulation.
```

- [ ] **Step 4: Update the live handoff**

Set the phase to `Broad discovery and lineage locating complete; primary-source verification and method-card extraction plan pending owner review`. Name the run directory, verification report, coverage audit, current discovery-state registry counts, gaps, and exact next independent plan. Preserve the bootstrap history and claim boundaries.

- [ ] **Step 5: Commit the phase receipt**

Run:

```bash
git add HANDOFF.md 07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md
git commit -m "verify broad methods discovery phase"
git status --short --branch
```

Expected: clean task branch and a two-file verification commit.

- [ ] **Step 6: Complete the independent Task 8 review gate**

Generate Task 8's exact implementation diff package only after Step 5 commits. Run the global per-task package/review/fix/receipt gate with a fresh Task 8 reviewer; do not substitute the whole-branch review. Proceed only when the Task 8 receipt says `PASS — no remaining Critical or Important findings` and its ledger row resolves to that receipt commit.

- [ ] **Step 7: Complete whole-branch review and correct all blocking findings**

Give an independent reviewer the exact base-to-head diff plus the approved design, this plan, task review packages, test output, manifests, screening audit, lineage ledger, coverage audit, and external-boundary receipts. Fix and re-review every Critical or Important finding.

The whole-branch reviewer checks:

1. approved-design and protocol compliance;
2. query completeness and uncapped retrieval;
3. raw-manifest/count integrity, including both PubMed record types;
4. semantic-screening completeness and independent audit coverage;
5. discovery-versus-verified claim separation;
6. stable IDs, minimal discovery-record paths, and continued header-only normalized relationships;
7. lineage-role evidence and all terminal query statuses;
8. absence of flagship selection, data downloads, simulation execution, and `Surveillance_AMR` writes.

Record the final verdict and any fix/re-review cycle in `07_reviews/BROAD_DISCOVERY_REVIEW_20260720.md`, then commit that review receipt before merge. Minor findings may be deferred only with a written risk assessment and named next-action owner.

- [ ] **Step 8: Merge only the reviewed branch, rerun the full gate on `main`, and push verified `main`**

Use `superpowers:finishing-a-development-branch`. Fast-forward merge when `main` is an ancestor. Rerun Steps 1–2 from the main checkout, then push `main` only. Verify:

```bash
git rev-parse HEAD
git rev-parse origin/main
git ls-remote origin refs/heads/main
```

Expected: all three SHAs are identical. Remove the isolated worktree and delete the merged task branch only after equality passes.

---

## Deferred Independent Plans

After this phase passes, write and obtain owner approval for these plans in order:

1. primary-source verification and complete method-card extraction;
2. translation-candidate generation and cross-disease opportunity mapping;
3. official dataset access/licence/grain audit;
4. portfolio ranking, novelty review, geometry preflight, and graduation gates;
5. formal simulation programme for questions surviving the prevalence-of-practice and structural-contribution audits.

The frozen discovery corpus may inform those plans but cannot be treated as verified evidence merely because it passed search-artifact validation.
