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
