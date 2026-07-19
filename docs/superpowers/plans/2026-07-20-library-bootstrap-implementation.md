# ID Epidemiology Methods Library Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the approved design into a clean, auditable, remotely backed-up methods-library repository whose state can be recovered from files alone.

**Architecture:** The bootstrap uses Markdown for governance and research cards, header-only CSV files for linked registries, and one Python-standard-library validator for schemas, identifiers, foreign keys, required paths, and frozen-file checksums. The repository remains a library and control plane; literature-search execution, evidence extraction, simulation work, and individual paper projects are separate later plans.

**Tech Stack:** Git; GitHub repository `ChaokunHong/ID_Epi_Methods_Library`; Markdown; CSV encoded as UTF-8; Python 3.12 standard library; `unittest`; SHA-256 via `hashlib`/`shasum`.

## Global Constraints

- Approved design: `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`, commit `c708ac2`, SHA256 `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`.
- The project is methods-first; AMR, LMIC relevance, global scope, and immediate public-data access are downstream attributes, never discovery-stage exclusion gates.
- Simulation-only, synthetic-data, mechanistic-modelling, and method-comparison studies are eligible.
- Stable identifiers follow exactly: `P-YYYY-NNNN`, `M-FAMILY-NNN`, `D-OWNER-NNN`, `T-DOMAIN-NNN`, and `S-FAMILY-NNN`.
- Discovery claims and verified claims remain distinct; primary sources are required for substantive method, software, and dataset claims.
- `Surveillance_AMR` protocols and existing files must not be changed; the only permitted old-repository write is one new reciprocal-pointer file after a before/after status check.
- The broadened seed scan is copied, never moved, from `Surveillance_AMR`; its expected SHA256 is `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`.
- Do not select a flagship study, execute the systematic search, download candidate datasets, run simulations, or create paper repositories during bootstrap.
- Every task ends in an independently reviewable commit; push only after the complete local verification gate passes.

---

## File Map

| Path | Responsibility |
|---|---|
| `README.md` | Human entry point, purpose, navigation, and current phase |
| `AGENTS.md` | Mandatory reading order and operating rules for future agents |
| `HANDOFF.md` | Live state, immutable outputs, blockers, and exact next action |
| `.gitignore` | Exclude OS/runtime debris without excluding manifests or research records |
| `00_governance/PROJECT_CHARTER.md` | Stable scope, outputs, boundaries, and graduation rule |
| `00_governance/SCOPE_AND_ELIGIBILITY.md` | Inclusion, exclusion, source, and verification rules |
| `00_governance/DECISION_LOG.md` | Append-only material decisions |
| `00_governance/WORKFLOW.md` | Seven-stage operating workflow and gates |
| `00_governance/REGISTRY_SCHEMA.md` | Exact registry columns, relationships, enums, and null rules |
| `00_governance/scripts/validate_library.py` | Repository, registry, link, and checksum validator |
| `00_governance/tests/test_validate_library.py` | Validator contract tests |
| `01_search/SEARCH_LOG_TEMPLATE.md` | Reusable reproducible search log |
| `01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md` | Frozen seed-scan snapshot |
| `01_search/seed_scans/SEED_SCAN_PROVENANCE.md` | Snapshot origin, source status, SHA, and limitations |
| `01_search/seed_scans/MANIFEST_SHA256.json` | Machine-readable checksum receipt for the frozen seed snapshot |
| `02_method_library/METHOD_CARD_TEMPLATE.md` | Required 18-section method-card contract |
| `03_evidence_tables/papers.csv` | Paper registry |
| `03_evidence_tables/methods.csv` | Method registry |
| `03_evidence_tables/paper_method_links.csv` | Many-to-many paper-to-method relationships |
| `04_translation_candidates/TRANSLATION_CARD_TEMPLATE.md` | Translation opportunity and gate template |
| `04_translation_candidates/translation_candidates.csv` | Translation registry |
| `05_data_registry/DATASET_CARD_TEMPLATE.md` | Access, licence, grain, denominator, and feasibility audit |
| `05_data_registry/datasets.csv` | Dataset registry |
| `06_simulation_lab/SIMULATION_CARD_TEMPLATE.md` | Data-generating-process and operating-characteristic contract |
| `06_simulation_lab/simulations.csv` | Simulation registry |
| `07_reviews/REVIEW_TEMPLATE.md` | Review record that separates findings from owner decisions |
| `00_governance/RESUME_PROMPT.md` | Copy-paste prompt for a new Codex task rooted in this repository |
| `Surveillance_AMR/ID_EPI_METHODS_LIBRARY_POINTER.md` | Only reciprocal pointer added to the existing application project |

## Interfaces

The bootstrap validator exposes these Python interfaces for all later tasks:

```python
def validate_repository(root: Path) -> list[str]: ...
def validate_csv(root: Path, spec: RegistrySpec) -> list[str]: ...
def validate_foreign_keys(root: Path) -> list[str]: ...
def validate_seed_checksum(root: Path) -> list[str]: ...
def main(argv: Sequence[str] | None = None) -> int: ...
```

`validate_repository` returns an empty list on success and human-readable error strings on failure. The command-line interface prints `VALIDATION PASS` and exits `0` on success; it prints `VALIDATION FAIL` followed by one error per line and exits `1` on failure.

---

### Task 1: Establish repository entry points and remote boundary

**Files:**
- Create: `.gitignore`
- Create: `README.md`
- Create: `AGENTS.md`
- Modify: `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`
- Modify: Git configuration only, by adding `origin`

**Interfaces:**
- Consumes: approved design at commit `c708ac2`; empty GitHub repository supplied by the owner.
- Produces: stable human/agent entry points and remote `origin` without pushing.

- [ ] **Step 1: Reconfirm local and remote preconditions**

Run:

```bash
git status --short --branch
git log -1 --oneline
git remote -v
git ls-remote https://github.com/ChaokunHong/ID_Epi_Methods_Library.git HEAD refs/heads/main
```

Expected: local branch is `main`, latest commit is `c708ac2`, worktree is clean, no remote is configured, and `ls-remote` returns no reference. If the remote contains a reference, stop and inspect it before changing Git configuration.

- [ ] **Step 2: Create the repository hygiene and entry-point files**

Create `.gitignore` with exactly:

```gitignore
.DS_Store
._*
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
venv/
.Rhistory
.RData
.Rproj.user/
*.tmp
*.swp
```

Create `README.md` with:

```markdown
# Infectious Disease Epidemiology Methods Translation Library

This repository builds an evidence-backed library of epidemiological and quantitative methods that may be translated into antimicrobial-resistance or other infectious-disease research.

The project is methods-first. Geography, LMIC relevance, AMR relevance, public-data access, and solo-researcher feasibility are evaluated after a method is understood; they are not initial discovery filters. Simulation, synthetic-data, mechanistic-modelling, and method-comparison studies are eligible.

## Start here

1. Read `HANDOFF.md` for the live state.
2. Read `00_governance/PROJECT_CHARTER.md` for stable scope.
3. Read `00_governance/DECISION_LOG.md` for binding decisions.
4. Read `00_governance/WORKFLOW.md` before adding evidence.
5. Run `python3 00_governance/scripts/validate_library.py --root .` before committing.

## Current phase

Bootstrap. The approved design is `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`. No flagship study has been selected and the broad search has not yet been executed.

## Related project

`../Surveillance_AMR` is the first AMR application project and the provenance source for the initial seed scan. Its protocol and application-specific decisions are not governed by this repository.
```

Create `AGENTS.md` with:

```markdown
# Agent Entry Point

Before acting, read these files in order:

1. `HANDOFF.md`
2. `00_governance/PROJECT_CHARTER.md`
3. `00_governance/DECISION_LOG.md`
4. `00_governance/WORKFLOW.md`
5. the active approved plan named in `HANDOFF.md`

Operating rules:

- Verify the live worktree and referenced SHA values instead of trusting prior narration.
- Keep discovery claims separate from verified claims.
- Use primary sources for substantive method, software, and dataset claims.
- Do not use AMR, LMIC status, global scope, or public-data availability as discovery-stage exclusion gates.
- Preserve failed and null designs; never relax a gate merely to promote a candidate.
- Do not modify `../Surveillance_AMR` except through an explicit, separately reviewed task.
- Update `HANDOFF.md` at every stopping point and record the exact Git commit.
- Run `python3 00_governance/scripts/validate_library.py --root .` before reporting completion.
```

- [ ] **Step 3: Mark the approved design accurately**

Replace the design status line with:

```markdown
**Status:** Approved by the owner on 2026-07-20; bootstrap governed by `docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md`.
```

- [ ] **Step 4: Add and verify the GitHub remote without pushing**

Run:

```bash
git remote add origin https://github.com/ChaokunHong/ID_Epi_Methods_Library.git
git remote -v
```

Expected: fetch and push URLs both equal the supplied GitHub URL.

- [ ] **Step 5: Review and commit the entry points**

Run:

```bash
git diff --check
git status --short
git add .gitignore README.md AGENTS.md docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
git commit -m "bootstrap repository entry points"
```

Expected: `git diff --check` prints nothing; the commit succeeds and includes only the four listed files.

---

### Task 2: Add stable governance and workflow documents

**Files:**
- Create: `00_governance/PROJECT_CHARTER.md`
- Create: `00_governance/SCOPE_AND_ELIGIBILITY.md`
- Create: `00_governance/DECISION_LOG.md`
- Create: `00_governance/WORKFLOW.md`

**Interfaces:**
- Consumes: design sections 1–8 and 11–14.
- Produces: stable scope rules used by cards, registries, search plans, and future promotion decisions.

- [ ] **Step 1: Create `PROJECT_CHARTER.md`**

Use these sections and binding statements:

```markdown
# Project Charter

## Mission

Build a durable, evidence-backed library of epidemiological and quantitative methods that have produced strong infectious-disease research and may be translated into AMR or other infectious-disease studies.

## Intended outputs

1. Multiple flagship candidates with strong identification or methodological novelty.
2. Lower-risk studies executable by an independent researcher with public data.
3. At least one credible non-AMR infectious-disease route.

## Scope boundary

The Library discovers, verifies, compares, and translates methods. It does not own the protocol or analysis of a promoted paper. A promoted candidate receives a separate repository; this Library retains its evidence trail and graduation decision.

## Binding principles

- Methods first; feasibility second.
- Primary sources over derivative descriptions.
- Estimands, assumptions, diagnostics, and stop rules over journal prestige.
- Simulation and failed designs are first-class evidence.
- Portfolio categories remain separate: flagship, lower-risk public-data, infrastructure/prospective, collaboration-dependent, and no-go.

## Ownership and authority

Chaokun Hong is the project owner and final authority for scope changes and candidate graduation. Agent findings do not constitute owner approval.

## Change control

Material changes to taxonomy, eligibility, stable identifiers, graduation requirements, or claim boundaries require a dated entry in `DECISION_LOG.md` before implementation.
```

- [ ] **Step 2: Create `SCOPE_AND_ELIGIBILITY.md`**

Include exact rules:

```markdown
# Scope and Eligibility

## Eligible records

- Applied infectious-disease papers that demonstrate a potentially transferable design.
- Original or authoritative methods papers from epidemiology, biostatistics, statistics, econometrics, modelling, or computational epidemiology.
- Corrections, critiques, diagnostics, reporting guidance, and reproducibility resources needed to use a method responsibly.
- Simulation-only, synthetic-data, mechanistic, agent-based, and method-comparison studies.
- Work outside infectious diseases when transferability can be stated explicitly.

## Discovery-stage non-exclusions

Do not exclude a method because it is not AMR-specific, not LMIC-specific, not global, lacks immediately public data, requires collaboration, or is not yet executable by one researcher.

## Exclusions

- Purely descriptive applications with no transferable design contribution.
- Commentary without enough methodological content to support a claim; it may remain a discovery lead.
- Duplicate reports that add no method, diagnostic, dataset, or correction information.
- Sources whose central claims cannot be traced to an authoritative source after documented attempts.

## Verification states

- `discovery`: identified but substantive claims not source-verified.
- `verified`: bibliographic identity and relevant claims checked against primary sources.
- `extracted`: required method or dataset fields completed and internally reviewed.
- `retired`: retained for provenance but excluded with a recorded reason.

## Source hierarchy

Use original papers, official dataset-owner documentation, official repositories, specifications, and source code. Reviews and secondary pages guide discovery but do not verify owner-controlled facts.

## Search period

The main applied search covers 2010–2026. Earlier papers are eligible when foundational, unusually informative natural experiments, or necessary for method lineage.
```

- [ ] **Step 3: Create the append-only `DECISION_LOG.md`**

```markdown
# Decision Log

Do not rewrite prior decisions. Add a new row when a decision is superseded and cite the earlier decision ID.

| Decision ID | Date | Status | Decision | Rationale | Evidence or authority | Supersedes |
|---|---|---|---|---|---|---|
| DEC-20260720-001 | 2026-07-20 | active | Create `ID_Epi_Methods_Library` as a sibling repository of `Surveillance_AMR`. | Separates reusable method discovery from one application protocol. | Owner approval and approved design `c708ac2`. | — |
| DEC-20260720-002 | 2026-07-20 | active | Use methods-first discovery; treat AMR, LMIC relevance, public-data feasibility, and solo workload as downstream attributes. | Prevents premature narrowing and supports flagship discovery. | Owner approval and approved design `c708ac2`. | — |
| DEC-20260720-003 | 2026-07-20 | active | Include simulation-only, synthetic-data, mechanistic, and method-comparison studies. | Some important methodological contributions do not require a real-data analysis. | Owner approval and approved design `c708ac2`. | — |
| DEC-20260720-004 | 2026-07-20 | active | Use five permanent ID namespaces for papers, methods, datasets, translations, and simulations. | Makes cross-file relationships stable when titles change. | Approved design section 6. | — |
```

- [ ] **Step 4: Create `WORKFLOW.md`**

Create it with exactly:

```markdown
# Workflow

## Stage 1 — Broad discovery

- **Inputs:** reproducible searches, citation chasing, journal scans, and the frozen seed scan.
- **Required record:** a dated search log and paper-registry discovery record.
- **Exit gate:** the record has a resolvable title, year, source URL, discovery route, and preliminary method label.
- **Forbidden shortcut:** excluding a lead because it is not AMR, not LMIC-specific, not global, not immediately public, or not executable by one researcher.

## Stage 2 — Method lineage

- **Inputs:** promising applied seeds and method-led papers from Stage 1.
- **Required record:** linked original or authoritative method sources, later corrections, accepted diagnostics, and duplicate-name resolution.
- **Exit gate:** the method's lineage and current defensible use can be described from primary sources.
- **Forbidden shortcut:** treating a high-impact application or review article as the authoritative method source without checking lineage.

## Stage 3 — Card construction

- **Inputs:** verified method lineage and relevant infectious-disease applications.
- **Required record:** a method card linked to paper IDs.
- **Exit gate:** estimand, required data signature, identification assumptions, mandatory diagnostics, falsification tests, common misuses, and stop rules are explicit; unresolved assumptions are recorded as defects.
- **Forbidden shortcut:** completing a card that only summarizes papers or lists software.

## Stage 4 — Translation generation

- **Inputs:** a mature method card.
- **Required record:** linked translation cards for one direct AMR application, one AMR mechanism/policy/surveillance/transmission application, and one non-AMR infectious-disease application when scientifically coherent.
- **Exit gate:** each candidate states a question, estimand, setting, identification route, falsification strategy, and stop rules.
- **Forbidden shortcut:** choosing a familiar dataset first and retrofitting a method without a defensible question or estimand.

## Stage 5 — Feasibility and data audit

- **Inputs:** translation candidates and official dataset sources.
- **Required record:** dataset cards covering access, licence, time/geographic grain, unit, numerator, denominator, observation process, missingness, revisions, linkage, compute, LMIC relevance, and solo workload.
- **Exit gate:** access and licence are verified or explicitly unresolved, and the data structure can or cannot identify the candidate estimand for stated reasons.
- **Forbidden shortcut:** calling data public because a paper used them or because a landing page exists.

## Stage 6 — Portfolio ranking

- **Inputs:** mature cards, feasibility audits, novelty checks, and design preflights.
- **Required record:** an auditable category decision and rationale.
- **Exit gate:** candidate is classified as `flagship`, `lower_risk_public_data`, `infrastructure_prospective`, `collaboration_dependent`, or `no_go`; categories are not collapsed into one score.
- **Forbidden shortcut:** relaxing thresholds, hiding failed preflights, or promoting solely on journal fit.

## Stage 7 — Project graduation

- **Inputs:** owner-reviewed portfolio candidate.
- **Required record:** mature method card, data audit, novelty check, estimand, falsification strategy, preflight plan, decision-log entry, and owner approval.
- **Exit gate:** a separate paper repository and protocol are authorized; the Library retains immutable links and the graduation decision.
- **Forbidden shortcut:** running the definitive analysis or treating an agent recommendation as owner approval.
```

- [ ] **Step 5: Review and commit governance**

Run:

```bash
rg -n "LMIC|public.data|simulation|graduat|primary source|decision" 00_governance
git diff --check
git add 00_governance/PROJECT_CHARTER.md 00_governance/SCOPE_AND_ELIGIBILITY.md 00_governance/DECISION_LOG.md 00_governance/WORKFLOW.md
git commit -m "define library governance and workflow"
```

Expected: each required concept appears in at least one governing file; whitespace check passes; commit contains four files.

---

### Task 3: Create research-card contracts and persistent folder structure

**Files:**
- Create: `01_search/SEARCH_LOG_TEMPLATE.md`
- Create: `01_search/search_protocols/README.md`
- Create: `01_search/search_logs/README.md`
- Create: `01_search/journal_registry/README.md`
- Create: `02_method_library/METHOD_CARD_TEMPLATE.md`
- Create: six family `README.md` files under `02_method_library/`
- Create: `04_translation_candidates/TRANSLATION_CARD_TEMPLATE.md`
- Create: three category `README.md` files under `04_translation_candidates/`
- Create: `05_data_registry/DATASET_CARD_TEMPLATE.md`
- Create: `06_simulation_lab/SIMULATION_CARD_TEMPLATE.md`
- Create: four component `README.md` files under `06_simulation_lab/`
- Create: `07_reviews/REVIEW_TEMPLATE.md`
- Create: `99_archive/README.md`

**Interfaces:**
- Consumes: approved taxonomy and seven-stage workflow.
- Produces: standardized records that later registries point to by relative path.

- [ ] **Step 1: Create the search log contract**

Create `SEARCH_LOG_TEMPLATE.md` with exactly:

```markdown
# Search Log

## Control

- Search ID:
- Database or site:
- Searcher:
- Executed date and time with timezone:
- Coverage dates requested:
- Result count reported by source:
- Export path and format:

## Exact query

Copy the executed query verbatim, including filters and field tags. A rerun receives a new search ID even when the query is unchanged.

## Processing

- Deduplication action and software:
- Records retained for screening:
- Screening decision summary:
- Included paper IDs:
- Excluded records and coded reasons:
- Unresolved leads:

## Deviations and limitations

Record interface constraints, inaccessible results, pagination limits, query changes, and any departure from the approved search protocol.
```

- [ ] **Step 2: Create the 18-section method-card template**

Create `METHOD_CARD_TEMPLATE.md` with the title `# M-FAMILY-NNN — Method name`, followed by this exact body:

```markdown
## Record control

- Method ID:
- Taxonomy family:
- Verification state:
- Author:
- Reviewer:
- Created date:
- Updated date:
- Linked paper IDs:

Every substantive claim below must cite a linked paper ID and primary-source URL. Empty evidence remains an explicit defect rather than an inferred claim.

## 1. Canonical name and variants

Record the authoritative name, common variants, and labels that should be merged or kept distinct.

## 2. Problem addressed

State the structural epidemiological or inferential problem, not merely the software model used.

## 3. Representative high-impact application

Identify an informative application and explain what the method contributed. Journal prestige is not evidence of validity.

## 4. Original or authoritative method sources

Link the originating or currently authoritative sources, later corrections, and accepted guidance.

## 5. Estimand

Define the target quantity, population, time, treatment/exposure contrast, and scale.

## 6. Required data signature

Specify unit, time structure, intervention variation, comparator structure, denominators, sample size geometry, and linkage requirements.

## 7. Identification assumptions

List assumptions in falsifiable or diagnosable form and separate structural assumptions from modelling convenience.

## 8. Mandatory diagnostics and falsification tests

Name required diagnostics, negative controls, placebo tests, pre-trend checks, calibration checks, or sensitivity analyses and state what failure means.

## 9. Common misuse patterns

Record documented failure modes and misleading interpretations with primary-source support.

## 10. Software and reproducibility resources

Link official packages, source repositories, examples, and version requirements; distinguish maintained tools from discovery leads.

## 11. Existing use in AMR and infectious diseases

Summarize verified use without treating repeated datasets or papers as independent validation.

## 12. Direct AMR translation opportunities

Describe at least one direct AMR outcome or surveillance application when scientifically coherent.

## 13. AMR mechanism, policy, surveillance, or transmission opportunities

Describe a distinct mechanistic or policy route rather than repeating section 12.

## 14. Non-AMR infectious-disease opportunities

Describe at least one credible cross-disease route when scientifically coherent.

## 15. Public-data feasibility

Record verified access, licence, grain, numerator/denominator availability, and unresolved acquisition dependencies.

## 16. LMIC relevance

Assess scientific and data relevance after the method is understood; LMIC status is not a discovery gate.

## 17. Independent-researcher workload, novelty crowding, and flagship potential

Assess compute, engineering, access, collaboration, novelty saturation, and the type of contribution needed for a strong paper.

## 18. Stop rules

State empirical, identification, access, leverage, power, or novelty findings that would retire or redesign an application.

## Evidence defects and next verification action

List every unresolved claim, missing primary source, ambiguous method label, and the exact next verification action.
```

- [ ] **Step 3: Create translation, dataset, simulation, and review templates**

Create `TRANSLATION_CARD_TEMPLATE.md` with exactly:

```markdown
# T-DOMAIN-NNN — Candidate title

## Control
- Candidate ID:
- Verification state:
- Linked method IDs:
- Linked dataset IDs:
- Author and reviewer:

## Research question
## Target population and setting
## Exposure or intervention
## Estimand and outcome
## Identification route and assumptions
## Diagnostics and falsification strategy
## Data dependencies and access state
## AMR, infectious-disease, or cross-domain classification
## LMIC relevance
## Public-data feasibility and independent-researcher workload
## Novelty and crowding audit
## Geometry or simulation preflight
## Stop rules
## Portfolio category
## Graduation decision

The graduation decision records reviewer findings separately from owner approval and links the decision-log entry.
```

Create `DATASET_CARD_TEMPLATE.md` with exactly:

```markdown
# D-OWNER-NNN — Dataset name

## Control
- Dataset ID:
- Verification state:
- Access state:
- Linked candidate IDs:

## Owner and official source
## Access route and licence
## Geographic coverage and grain
## Temporal coverage and grain
## Unit of observation
## Numerator, denominator, and outcome construction
## Observation and ascertainment process
## Missingness, suppression, and inclusion rules
## Revisions, versions, and release dates
## Linkage keys and crosswalks
## Restrictions and governance
## Retrieval verification date
## Reproducible acquisition procedure
## Suitability defects and next action

Do not mark access `public_verified` until the file or API, applicable licence, required fields, and usable grain have been checked directly.
```

Create `SIMULATION_CARD_TEMPLATE.md` with exactly:

```markdown
# S-FAMILY-NNN — Simulation title

## Control
- Simulation ID:
- Verification state:
- Linked method IDs:
- Linked candidate IDs:

## Structural problem
## Empirical motivation for the data-generating process
## Data-generating process
## Estimands and truth definitions
## Competing methods
## Bias, coverage, calibration, power, error, and decision metrics
## Boundary scenarios
## Stress-test scenarios
## Acceptance thresholds fixed before execution
## Random-seed strategy
## Software environment and reproducibility
## Real-data illustration: necessary, helpful, or misleading
## Safeguard against a generic small-sample demonstration
## Stop, redesign, and promotion rules
```

Create `REVIEW_TEMPLATE.md` with exactly:

```markdown
# Review Record

## Scope
## Immutable artifact, commit, and checksum
## Verification performed
## Critical findings
## Major findings
## Minor findings
## Evidence for each finding
## Required corrections and acceptance tests
## Reviewer verdict
## Owner decision

The reviewer verdict is an evidence-backed recommendation, not owner approval. The owner decision is recorded separately and may accept, reject, or request changes.
```

- [ ] **Step 4: Persist the approved directory taxonomy**

Create each README with the exact sentence shown:

| Path | Exact content after the `#` title |
|---|---|
| `01_search/search_protocols/README.md` | `Approved reproducible search protocols live here. Execution logs belong in ../search_logs/.` |
| `01_search/search_logs/README.md` | `Completed search logs follow ../SEARCH_LOG_TEMPLATE.md and retain exact queries, dates, exports, and deviations.` |
| `01_search/journal_registry/README.md` | `Journal and source coverage decisions live here; journal prestige never substitutes for method verification.` |
| `02_method_library/causal_policy/README.md` | `Method cards for causal and policy evaluation live here and follow ../METHOD_CARD_TEMPLATE.md.` |
| `02_method_library/surveillance_measurement/README.md` | `Method cards for surveillance and measurement live here and follow ../METHOD_CARD_TEMPLATE.md.` |
| `02_method_library/spatial_transmission/README.md` | `Method cards for spatial and transmission epidemiology live here and follow ../METHOD_CARD_TEMPLATE.md.` |
| `02_method_library/forecasting_dynamics/README.md` | `Method cards for dynamics, forecasting, and early warning live here and follow ../METHOD_CARD_TEMPLATE.md.` |
| `02_method_library/evidence_synthesis/README.md` | `Method cards for triangulation, robustness, transportability, and evidence synthesis live here and follow ../METHOD_CARD_TEMPLATE.md.` |
| `02_method_library/simulation_methods/README.md` | `Method cards for simulation and methodological evaluation live here and follow ../METHOD_CARD_TEMPLATE.md.` |
| `04_translation_candidates/amr/README.md` | `AMR translation cards live here after method-card construction; use ../TRANSLATION_CARD_TEMPLATE.md.` |
| `04_translation_candidates/infectious_diseases/README.md` | `Non-AMR infectious-disease translation cards live here; use ../TRANSLATION_CARD_TEMPLATE.md.` |
| `04_translation_candidates/flagship_portfolio/README.md` | `Owner-reviewed portfolio decisions and comparison tables live here; a candidate is not promoted by folder placement alone.` |
| `06_simulation_lab/dgp_specs/README.md` | `Frozen data-generating-process specifications live here and follow ../SIMULATION_CARD_TEMPLATE.md.` |
| `06_simulation_lab/scripts/README.md` | `Executable simulation code lives here only after a simulation specification is approved.` |
| `06_simulation_lab/tests/README.md` | `Simulation-code tests and deterministic fixtures live here.` |
| `06_simulation_lab/reports/README.md` | `Immutable simulation reports, operating characteristics, and manifests live here.` |
| `99_archive/README.md` | `Superseded records are retained here with provenance; archival does not erase registry or decision-log history.` |

Use a Markdown title derived from the directory name above each exact sentence. Do not add evidence claims to folder README files.

- [ ] **Step 5: Verify templates and commit**

Run:

```bash
test "$(rg -n '^## ([0-9]+\.|Record control|Evidence defects)' 02_method_library/METHOD_CARD_TEMPLATE.md | wc -l | tr -d ' ')" -eq 20
find 01_search 02_method_library 04_translation_candidates 05_data_registry 06_simulation_lab 07_reviews 99_archive -type f | sort
git diff --check
git add 01_search 02_method_library 04_translation_candidates 05_data_registry 06_simulation_lab 07_reviews 99_archive
git commit -m "add research card and folder contracts"
```

Expected: the method template has the control section, 18 numbered sections, and the evidence-defects section; all approved folders contain a tracked contract or README; commit succeeds.

---

### Task 4: Define registries and build the validator test-first

**Files:**
- Create: `00_governance/REGISTRY_SCHEMA.md`
- Create: `03_evidence_tables/papers.csv`
- Create: `03_evidence_tables/methods.csv`
- Create: `03_evidence_tables/paper_method_links.csv`
- Create: `04_translation_candidates/translation_candidates.csv`
- Create: `05_data_registry/datasets.csv`
- Create: `06_simulation_lab/simulations.csv`
- Create: `00_governance/tests/test_validate_library.py`
- Create: `00_governance/scripts/validate_library.py`

**Interfaces:**
- Consumes: stable ID rules and record templates.
- Produces: the five registries, relationship table, and validator functions defined under global interfaces.

- [ ] **Step 1: Freeze exact CSV schemas in `REGISTRY_SCHEMA.md`**

Define these exact header orders:

```text
papers.csv: paper_id,title,year,record_type,verification_state,doi,url,card_path,notes
methods.csv: method_id,canonical_name,family,verification_state,card_path,notes
paper_method_links.csv: paper_id,method_id,relationship,notes
translation_candidates.csv: candidate_id,title,domain,portfolio_category,verification_state,card_path,notes
datasets.csv: dataset_id,name,owner,access_state,verification_state,official_url,card_path,notes
simulations.csv: simulation_id,title,family,verification_state,card_path,notes
```

Define allowed values:

```text
record_type = method_source | applied_seed | diagnostic | correction | guidance | reproducibility
verification_state = discovery | verified | extracted | retired
relationship = originates | applies | critiques | corrects | diagnoses | implements
domain = amr | infectious_disease | cross_domain
portfolio_category = unranked | flagship | lower_risk_public_data | infrastructure_prospective | collaboration_dependent | no_go
access_state = unknown | public_verified | registration_required | application_required | restricted | unavailable
family = causal_policy | surveillance_measurement | spatial_transmission | forecasting_dynamics | evidence_synthesis | simulation_methods
```

State that empty registries contain only headers; IDs and paths become mandatory once a data row exists; optional unknown text values remain empty rather than using invented facts.

- [ ] **Step 2: Create a failing validator test suite**

Write `test_validate_library.py` with exactly:

```python
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
```

Each test must construct only the minimal files it exercises and assert on a stable error substring: `invalid ID`, `duplicate ID`, `invalid value`, `unknown method_id`, `card_path does not exist`, or `seed checksum mismatch`.

- [ ] **Step 3: Run tests and confirm the expected failure**

Run:

```bash
python3 -m unittest 00_governance/tests/test_validate_library.py -v
```

Expected: import or file-not-found failure because `validate_library.py` does not yet exist.

- [ ] **Step 4: Implement the minimum complete validator**

Create `validate_library.py` with exactly:

```python
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
```

- [ ] **Step 5: Create header-only registries**

Create each CSV with exactly the header from Step 1 and a trailing newline. Do not create sample or fabricated rows.

- [ ] **Step 6: Run unit and repository validation**

Run:

```bash
python3 -m unittest 00_governance/tests/test_validate_library.py -v
python3 00_governance/scripts/validate_library.py --root .
```

Expected: seven unit tests pass. Repository validation may report only the seed-scan and handoff files not yet created; no registry-schema, ID, enum, or foreign-key errors are allowed.

- [ ] **Step 7: Commit schemas and validator**

Run:

```bash
git diff --check
git add 00_governance/REGISTRY_SCHEMA.md 00_governance/scripts/validate_library.py 00_governance/tests/test_validate_library.py 03_evidence_tables 04_translation_candidates/translation_candidates.csv 05_data_registry/datasets.csv 06_simulation_lab/simulations.csv
git commit -m "add validated linked library registries"
```

Expected: commit contains documentation, six header-only CSVs, validator, and tests.

---

### Task 5: Freeze and register the broadened seed scan

**Files:**
- Copy: `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`
- Create: `01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`
- Create: `01_search/seed_scans/SEED_SCAN_PROVENANCE.md`
- Create: `01_search/seed_scans/MANIFEST_SHA256.json`

**Interfaces:**
- Consumes: source snapshot with expected SHA256 `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`.
- Produces: immutable in-repository discovery seed with honest provenance; no verified registry records.

- [ ] **Step 1: Verify the source without modifying it**

Run:

```bash
shasum -a 256 /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR status --short -- 02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
```

Expected: checksum equals the frozen value and the source is reported as untracked. Record that status; do not describe the old-repository file as committed or immutable.

- [ ] **Step 2: Copy the verified bytes**

Run:

```bash
cp /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
```

Expected: copied file has exactly the expected SHA.

- [ ] **Step 3: Write provenance without upgrading claims**

Create `SEED_SCAN_PROVENANCE.md` stating:

```markdown
# Seed Scan Provenance

- Snapshot name: `INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`
- Copied into this repository: 2026-07-20
- Source repository: `/Users/hongchaokun/Documents/PhD/Surveillance_AMR`
- Source path: `02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`
- Source tracking state at copy: untracked in the source worktree
- SHA256 before and after copy: `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`
- Status in this Library: frozen discovery seed after this file and the snapshot are committed

This scan is a discovery map, not a systematic-review result and not a set of verified registry entries. Its links and methodological claims must be checked against primary sources before extraction into the paper, method, dataset, translation, or simulation registries. Copying it does not alter or supersede the `Surveillance_AMR` protocol.
```

Create `MANIFEST_SHA256.json` with exactly:

```json
{
  "algorithm": "SHA256",
  "files": [
    {
      "path": "01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md",
      "sha256": "520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55"
    }
  ]
}
```

- [ ] **Step 4: Validate and commit the frozen snapshot**

Run:

```bash
python3 00_governance/scripts/validate_library.py --root .
git diff --check
git add 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md 01_search/seed_scans/SEED_SCAN_PROVENANCE.md 01_search/seed_scans/MANIFEST_SHA256.json
git commit -m "freeze broadened infectious disease seed scan"
```

Expected: checksum validation passes; any remaining validator errors concern only continuity files not yet created.

---

### Task 6: Add recoverable handoff and new-task resume instructions

**Files:**
- Create: `HANDOFF.md`
- Create: `00_governance/RESUME_PROMPT.md`

**Interfaces:**
- Consumes: committed governance, templates, registries, validator, and seed scan.
- Produces: conversation-independent recovery state.

- [ ] **Step 1: Create `HANDOFF.md` from live evidence**

Include these headings:

```markdown
# Handoff

## Project identity
## Current phase and status
## Approved scope
## Immutable outputs
## Registry state
## Related projects
## Known blockers and non-blockers
## Exact next action
## Verification commands
## Last updated
```

Record exact commit SHAs from `git log --oneline`, the design SHA, seed-scan SHA, remote URL, and that all registries contain headers only. State that the next action is to write and approve a separate broad-search execution plan, not to select a flagship from the seed scan.

- [ ] **Step 2: Create the copy-paste `RESUME_PROMPT.md`**

Use this complete prompt:

```markdown
Work in `/Users/hongchaokun/Documents/PhD/ID_Epi_Methods_Library`.

First read `AGENTS.md`, `HANDOFF.md`, `00_governance/PROJECT_CHARTER.md`, `00_governance/DECISION_LOG.md`, and `00_governance/WORKFLOW.md`. Verify the live Git status and all SHAs named in the handoff before trusting prior narration.

This is a methods-first infectious-disease epidemiology translation library. Do not restrict discovery to AMR, LMICs, global studies, or immediately public data. Simulation-only, synthetic-data, mechanistic, and method-comparison studies are eligible. Keep discovery leads separate from primary-source-verified records.

Resume from the exact next action in `HANDOFF.md`. Do not modify the `Surveillance_AMR` protocol or promote a flagship candidate without the documented gates and owner approval. Run `python3 00_governance/scripts/validate_library.py --root .` before reporting completion, update `HANDOFF.md`, and commit each independently reviewable unit.
```

- [ ] **Step 3: Validate recoverability**

Run:

```bash
rg -n "Current phase|Immutable outputs|Exact next action|Verification commands" HANDOFF.md
python3 00_governance/scripts/validate_library.py --root .
```

Expected: all handoff headings are found and validator prints `VALIDATION PASS` before the reciprocal pointer is added. If the validator requires that pointer, its absence must be a clearly named single error.

- [ ] **Step 4: Commit continuity files**

Run:

```bash
git diff --check
git add HANDOFF.md 00_governance/RESUME_PROMPT.md
git commit -m "add filesystem-based project handoff"
```

Expected: commit contains only the handoff and resume prompt.

---

### Task 7: Add the reciprocal pointer without touching existing Surveillance_AMR files

**Files:**
- Create only: `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/ID_EPI_METHODS_LIBRARY_POINTER.md`
- Modify: `HANDOFF.md`

**Interfaces:**
- Consumes: new Library remote and local path; dirty source worktree whose existing changes belong to the owner.
- Produces: reciprocal navigation while preserving every pre-existing source-tree path and byte.

- [ ] **Step 1: Capture and store the exact pre-write source status**

Run:

```bash
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR status --porcelain=v1 > /tmp/id_epi_library_surveillance_status_before.txt
test ! -e /Users/hongchaokun/Documents/PhD/Surveillance_AMR/ID_EPI_METHODS_LIBRARY_POINTER.md
```

Expected: status capture succeeds and pointer does not exist. If it already exists, stop and review it rather than overwriting it.

- [ ] **Step 2: Add exactly one new pointer file using `apply_patch`**

Create the file with:

```markdown
# Infectious Disease Epidemiology Methods Library

Reusable method discovery, method lineage, simulation-method evaluation, and cross-disease translation work has moved to the sibling repository:

- Local: `/Users/hongchaokun/Documents/PhD/ID_Epi_Methods_Library`
- GitHub: `https://github.com/ChaokunHong/ID_Epi_Methods_Library`
- Entry point: `HANDOFF.md`

`Surveillance_AMR` remains the application-specific home for the GLASS–GRAM construct-comparison protocol, its data audit, and its Stage A diagnostic evidence. The new Library does not supersede or modify that protocol.
```

- [ ] **Step 3: Prove that no existing source-tree status changed**

Run:

```bash
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR status --porcelain=v1 | sed '/^?? ID_EPI_METHODS_LIBRARY_POINTER.md$/d' > /tmp/id_epi_library_surveillance_status_after.txt
diff -u /tmp/id_epi_library_surveillance_status_before.txt /tmp/id_epi_library_surveillance_status_after.txt
```

Expected: `diff` prints nothing. If any prior path changes status, stop, report it, and do not stage or commit in the old repository.

- [ ] **Step 4: Record pointer state in the Library handoff**

Add the pointer path and state `present but intentionally uncommitted in the dirty Surveillance_AMR worktree; no existing source file changed`. Do not claim it is part of the old repository history.

- [ ] **Step 5: Commit only the Library-side handoff update**

Run:

```bash
git add HANDOFF.md
git commit -m "record reciprocal project pointer"
```

Expected: the Library commit contains one file. Run `git -C ../Surveillance_AMR diff --name-only` and confirm no tracked file was modified by this task.

---

### Task 8: Run the full release gate and publish the bootstrap

**Files:**
- Modify: `HANDOFF.md`
- Create: `07_reviews/BOOTSTRAP_VERIFICATION_20260720.md`

**Interfaces:**
- Consumes: all bootstrap outputs and empty GitHub remote.
- Produces: a verified local release, pushed `main`, and an exact remote commit receipt.

- [ ] **Step 1: Run all automated checks**

Run:

```bash
python3 -m unittest 00_governance/tests/test_validate_library.py -v
python3 00_governance/scripts/validate_library.py --root .
git diff --check
git status --short
```

Expected: all unit tests pass, validator prints `VALIDATION PASS`, whitespace check is silent, and only the planned verification/handoff edits are uncommitted.

- [ ] **Step 2: Run structural and provenance checks**

Run:

```bash
shasum -a 256 docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
find . -path ./.git -prune -o -type f -print | sort
for registry in 03_evidence_tables/papers.csv 03_evidence_tables/methods.csv 03_evidence_tables/paper_method_links.csv 04_translation_candidates/translation_candidates.csv 05_data_registry/datasets.csv 06_simulation_lab/simulations.csv; do test "$(wc -l < "$registry" | tr -d ' ')" -eq 1 || exit 1; done
```

Expected: design and seed checksums match global constraints; file inventory matches the architecture; every registry contains exactly one header line.

- [ ] **Step 3: Write the verification report**

Record: date/time and timezone; Python and Git versions; unit-test count; validator result; design and seed SHA values; registry row counts; source-tree pointer status; local commit before release; remote pre-push state; and any explicitly deferred work. Include commands, exit codes, and concise outputs, not unsupported statements such as “all links are valid” unless they were actually checked.

- [ ] **Step 4: Update handoff and commit the release record**

Set the current phase to `Bootstrap complete; broad-search execution plan pending owner review`. Name the verification report and exact next action. Then run:

```bash
git add HANDOFF.md 07_reviews/BOOTSTRAP_VERIFICATION_20260720.md
git commit -m "verify methods library bootstrap"
git status --short --branch
```

Expected: local `main` is clean and contains the complete bootstrap history.

- [ ] **Step 5: Push the verified history**

Run:

```bash
git push -u origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Expected: push succeeds; local `HEAD` equals the remote `refs/heads/main` SHA.

- [ ] **Step 6: Final handoff report**

Report to the owner: local repository link; GitHub URL; final commit SHA; design and seed-scan checksums; validator/test results; exact state of the reciprocal pointer; and the next gated task. Do not state that literature evidence has been verified or that a flagship has been selected.

---

## Deferred Plans

After this bootstrap passes, write separate specs/plans in this order:

1. broad applied-paper and method-source search with journal/query registry;
2. primary-source verification and method-card extraction;
3. translation-candidate generation and feasibility/data audit;
4. portfolio ranking and candidate-graduation gates;
5. simulation-program design for questions that survive the prevalence-of-practice audit.

This separation is intentional: each subsystem produces an independently reviewable evidence state and none is silently treated as complete because the repository skeleton exists.
