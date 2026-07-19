# Infectious Disease Epidemiology Methods Translation Library — Design

**Date:** 2026-07-20  
**Owner:** Chaokun Hong  
**Repository:** `/Users/hongchaokun/Documents/PhD/ID_Epi_Methods_Library`  
**Status:** Approved concept; implementation awaits review of this written design.

## 1. Purpose

Build a durable, evidence-backed library of epidemiological and quantitative methods that have produced strong infectious-disease research and may be translated into antimicrobial resistance (AMR) or other infectious-disease studies.

The project is methods-first. It does not begin by restricting the search to AMR, low- and middle-income countries (LMICs), global comparisons, public data, or immediately executable studies. Those features are evaluated only after a method has been understood.

The library must support three research outputs:

1. multiple flagship study candidates with strong identification or methodological novelty;
2. lower-risk studies executable by an independent researcher using public data; and
3. at least one credible non-AMR route into infectious-disease epidemiology.

## 2. Core design decisions

1. The Library is a new sibling repository, not a subdirectory of `Surveillance_AMR`.
2. `Surveillance_AMR` remains an AMR application project and the provenance source for the first seed scan.
3. High-impact applied papers are search seeds, not the sole definition of methodological quality.
4. Every applied seed is traced to the original or authoritative method literature.
5. Relevant Nature Portfolio `npj` journals and strong specialist journals are eligible alongside general medical and science journals.
6. Methods developed or evaluated mainly through simulation, synthetic data or mathematical modelling are fully eligible.
7. Public-data feasibility, LMIC relevance and solo-researcher workload are downstream scoring dimensions, not initial inclusion gates.
8. A new paper project leaves the Library and receives its own repository once it passes the portfolio gate.

## 3. Search universe

### 3.1 Applied-paper seeds

The search covers, without treating journal brand as proof of validity:

- general medicine and public health, including *The Lancet*, *NEJM*, *JAMA*, *BMJ* and *PLOS Medicine*;
- general and translational science, including *Nature Medicine*, *Nature*, *Science* and *PNAS*;
- infectious disease and microbiology, including *The Lancet Infectious Diseases*, *Clinical Infectious Diseases*, *Nature Microbiology*, *Emerging Infectious Diseases* and *Eurosurveillance*;
- global health, including *The Lancet Global Health*;
- relevant `npj` journals and comparable high-quality specialist outlets;
- high-quality applied work from other disciplines when its design is demonstrably transferable.

The main applied search period is 2010–2026. Earlier papers enter when they are foundational applications, unusually influential natural experiments, or necessary to understand the method lineage.

### 3.2 Method sources

Method sources include epidemiology, biostatistics, statistics, econometrics, infectious-disease modelling and computational epidemiology. A method card cites both:

1. the original or authoritative method source; and
2. at least one informative infectious-disease application when one exists.

### 3.3 Evidence-source rule

Claims about datasets, software and methods use primary sources wherever possible: official data-owner documentation, original papers, official repositories, specifications and source code. Review papers may guide discovery but do not replace the source that owns the claim.

## 4. Method taxonomy

The initial taxonomy has six families:

1. **Causal and policy evaluation** — controlled interrupted time series, modern difference-in-differences, event studies, synthetic controls, regression discontinuity, instrumental variables, target-trial emulation and negative controls.
2. **Surveillance and measurement** — capture–recapture, multiple-system estimation, reporting-delay nowcasting, sentinel calibration, observation-process models, preferential sampling, measurement-error models and latent evidence synthesis.
3. **Spatial and transmission epidemiology** — endemic–epidemic models, metapopulation and network models, border designs, gravity/radiation models, self-exciting processes, phylogeography and genomic diffusion.
4. **Dynamics, forecasting and early warning** — renewal models, reproduction-number estimation, ensemble forecasting, calibration, change-point detection, outbreak detection and mechanistic–statistical hybrids.
5. **Triangulation and robustness** — cross-system comparison, denominator/outcome-definition sensitivity, transportability, multiverse/specification curves, hierarchical borrowing and negative-control structures.
6. **Simulation and methodological evaluation** — operating-characteristic studies, synthetic benchmarks, new estimators or diagnostics, mechanistic models and studies of structural bias in common epidemiological designs.

The taxonomy is versioned. New families require a decision-log entry rather than silent folder proliferation.

## 5. Simulation track

Simulation-only and simulation-led work is eligible in four forms:

1. evaluation of existing estimators under infectious-disease or AMR-specific data-generating processes;
2. development of a new estimator, diagnostic, decision rule or uncertainty method;
3. reproducible benchmarking of common published analytical practices;
4. mechanistic transmission, selection, surveillance or agent-based modelling.

Every simulation card records:

- the structural problem being investigated;
- the data-generating process and its empirical justification;
- estimands and truth definitions;
- competing methods;
- bias, coverage, calibration, power, error or decision metrics;
- boundary and stress-test scenarios;
- whether a real-data illustration is necessary, helpful or potentially misleading;
- what would make the study more than a generic demonstration of small-sample failure.

The Stage A experience in `Surveillance_AMR` is a seed for a possible simulation programme on country-level ecological infectious-disease studies with small numbers of countries, concentrated policy leverage, changing ascertainment and model-derived outcomes. It is not automatically promoted to a paper without a broader literature and prevalence-of-practice audit.

## 6. Library entities and stable identifiers

The project uses five linked entities:

| Entity | ID pattern | Purpose |
|---|---|---|
| Paper | `P-YYYY-NNNN` | Original paper, method source or applied seed |
| Method | `M-FAMILY-NNN` | Standard method card |
| Dataset | `D-OWNER-NNN` | Public, restricted or prospective dataset record |
| Translation candidate | `T-DOMAIN-NNN` | Method × question × setting opportunity |
| Simulation study | `S-FAMILY-NNN` | Data-generating process and comparison design |

IDs are permanent. Titles may change; IDs do not. Relationships are stored in registries rather than inferred from filenames.

## 7. Standard method card

Each method card contains:

1. canonical name and variants;
2. problem addressed;
3. representative high-impact application;
4. original or authoritative method sources;
5. estimand;
6. required data signature;
7. identification assumptions;
8. mandatory diagnostics and falsification tests;
9. common misuse patterns;
10. software and reproducibility resources;
11. existing use in AMR and infectious diseases;
12. AMR translation opportunities;
13. non-AMR infectious-disease opportunities;
14. public-data feasibility;
15. LMIC relevance;
16. independent-researcher workload;
17. novelty crowding and flagship potential;
18. stop rules.

No card is complete if it only summarizes an article without identifying the estimand, assumptions and required data structure.

## 8. Workflow

### Stage 1 — Broad discovery

Identify high-impact applications and method-led papers without filtering on geography or current data access. Record search strings, databases, dates and screening decisions.

### Stage 2 — Method lineage

Trace each promising application to authoritative methods, later corrections and accepted diagnostics. Merge duplicate labels that refer to the same method family.

### Stage 3 — Card construction

Create the method card, link papers, and grade the evidence and reproducibility. Unresolved assumptions are explicit card defects.

### Stage 4 — Translation generation

For each mature method, generate at least:

- one direct AMR application;
- one AMR mechanism, policy, surveillance or transmission application; and
- one non-AMR infectious-disease application when scientifically coherent.

### Stage 5 — Feasibility and data audit

Only now assess public availability, time and geographic grain, denominators, intervention timing, missingness, licensing, compute, LMIC relevance and solo workload.

### Stage 6 — Portfolio ranking

Rank candidates separately as flagship, lower-risk public-data, infrastructure/prospective, collaboration-dependent or no-go. Do not collapse these categories into one numeric score.

### Stage 7 — Project graduation

A candidate graduates only after its method card, data audit, novelty check, estimand, falsification strategy and preflight plan are complete. It then receives a separate repository and protocol; the Library retains a pointer and immutable decision record.

## 9. Repository architecture

```text
ID_Epi_Methods_Library/
├── AGENTS.md
├── README.md
├── HANDOFF.md
├── 00_governance/
│   ├── PROJECT_CHARTER.md
│   ├── SCOPE_AND_ELIGIBILITY.md
│   ├── DECISION_LOG.md
│   └── WORKFLOW.md
├── 01_search/
│   ├── search_protocols/
│   ├── search_logs/
│   ├── journal_registry/
│   └── seed_scans/
├── 02_method_library/
│   ├── causal_policy/
│   ├── surveillance_measurement/
│   ├── spatial_transmission/
│   ├── forecasting_dynamics/
│   ├── evidence_synthesis/
│   └── simulation_methods/
├── 03_evidence_tables/
├── 04_translation_candidates/
│   ├── amr/
│   ├── infectious_diseases/
│   └── flagship_portfolio/
├── 05_data_registry/
├── 06_simulation_lab/
│   ├── dgp_specs/
│   ├── scripts/
│   ├── tests/
│   └── reports/
├── 07_reviews/
├── 99_archive/
└── docs/superpowers/
    ├── specs/
    └── plans/
```

Process files must live in their assigned folders. The repository root remains limited to entry-point and governance files.

## 10. Continuity and handoff

Continuity is filesystem-based rather than dependent on conversation memory.

- `AGENTS.md` tells every future agent to read `HANDOFF.md`, the charter and the decision log before acting.
- `HANDOFF.md` records current status, live agents, latest immutable outputs, blockers and the exact next action.
- `PROJECT_CHARTER.md` stores stable scope and claim boundaries.
- `DECISION_LOG.md` records material inclusions, exclusions and taxonomy changes.
- Search and evidence registries use stable IDs and source URLs.
- Each stopping point updates the handoff and records the Git commit.

The new repository and `Surveillance_AMR` will contain reciprocal pointers. Existing Surveillance_AMR research files are not deleted or silently moved. The completed seed scan is copied with its original SHA and provenance after it is frozen.

## 11. Governance and quality gates

1. Separate discovery claims from verified claims.
2. Prefer primary sources and record retrieval dates.
3. Do not equate journal prestige with identification validity.
4. Do not label observational associations causal without defensible identification.
5. Do not call data public until access and licence are verified.
6. Do not treat repeated pathogen or region observations as independent units without modelling dependence.
7. Require explicit denominators and observation-process discussion for surveillance studies.
8. Require a simulation or geometry preflight before high-risk small-sample designs.
9. Preserve null and failed designs as auditable evidence; do not tune gates to force promotion.
10. Keep literature screening, evidence extraction and portfolio judgment separately auditable.

## 12. Initial migration

The bootstrap will:

1. create entry-point governance files and directories;
2. freeze the broadened infectious-disease methods seed scan in `01_search/seed_scans/` with source path and SHA;
3. create empty registries with documented schemas, not fabricated entries;
4. add a reciprocal pointer to `Surveillance_AMR` without disturbing its existing dirty worktree;
5. write a copy-paste resume prompt for a new Codex project rooted here;
6. verify links, Git status and manifest receipts.

## 13. Non-goals for bootstrap

The bootstrap does not:

- choose a flagship paper;
- execute a systematic review;
- download every candidate dataset;
- run a simulation study;
- modify `Surveillance_AMR` protocols;
- claim the first seed scan is a complete methods library;
- create separate paper repositories before candidates pass the graduation gate.

## 14. Success criteria

The Library is functioning when:

1. a new conversation can recover the project state from entry-point files alone;
2. every substantive method claim links to a primary source;
3. every mature card states an estimand, assumptions, data signature and stop rules;
4. empirical, simulation and hybrid methods are represented;
5. candidates can be ranked without making LMIC status or immediate public data an initial gate;
6. multiple flagship candidates and lower-risk studies can coexist without being conflated;
7. promoted studies leave behind an auditable decision trail.

