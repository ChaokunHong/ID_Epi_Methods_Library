# Wave 1 semantic screening record

Date: 2026-07-20
Scope: discovery classification only; no substantive method claim was verified and no record was promoted to a normalized registry.

## Locked input

- Raw candidate table: 7,146 unique PMID keys.
- `compiled_candidates_raw.csv` SHA256: `70cc6adb6ce40ed5c678ba0901cf4a23b78f64e5839304cd89002a7b19c46ec4`.
- Protocol SHA256: `e3b1013862e2f18314702cbf1e1e0e5c2c6b9e0d2b78113b23b9e65e2ccb20df`.
- Deterministic order: fixed family precedence followed by candidate key.
- Ordered-key-list SHA256: `4462d9a531e910e5cc01896d960a3f8bedd570d58620fb4f5a3939a3a4ac2e4f`.
- Batches: 48 manifests, 47 of 150 records and one of 96 records.

Every semantic reader received the exact manifested title and available abstract for each assigned key. Readers were read-only and returned strict rows; the sole integrator checked source SHA, exact ordered key coverage, decision/reason/type mapping, sentence-level rationale quality, duplicate retention, and cross-batch uniqueness before writing a CSV.

## Primary decisions

| Decision | Count |
|---|---:|
| `include_applied_seed` | 2,911 |
| `include_method_source_lead` | 1,250 |
| `include_diagnostic_or_correction_lead` | 794 |
| `include_simulation_or_mechanistic_lead` | 1,239 |
| `uncertain_retrieve_primary` | 41 |
| `exclude` | 911 |

Primary reason-code counts were: `I_APPLIED_TRANSFERABLE_DESIGN` 2,911; `I_METHOD_SOURCE` 1,250; `I_DIAGNOSTIC_CORRECTION` 794; `I_SIMULATION_MECHANISTIC` 1,239; `U_PRIMARY_RECORD_NEEDED` 41; `X_NOT_INFECTIOUS_TRANSFERABLE` 543; `X_DESCRIPTIVE_ONLY` 185; `X_COMMENTARY_ONLY` 97; `X_WRONG_RECORD_TYPE` 61; and `X_DUPLICATE` 25.

## Rejected outputs and recovery rule

No partial row from a failed semantic response was reused. Two initial collaboration-reader attempts produced zero usable rows. Later failures included transport interruption, missing/duplicated keys, and illegal decision mappings in batches 033, 034, 037, 040, and 041. Each affected complete batch was rejected, preserved in the ignored execution record, and reread through a fresh schema-constrained session or fresh contiguous subparts. The final 48 CSVs each passed the complete-manifest validator.

## Post-audit final state

After the independent audit, the 7,146 final rows comprise 2,860 applied seeds, 1,132 method-source leads, 706 diagnostic/correction leads, 1,188 simulation/mechanistic leads, 613 exclusions, and 647 honest primary-record uncertainties. The increase in uncertainty is caused only by open independent-reader conflicts; none was automatically adjudicated.

`screened_candidates.csv` SHA256: `37558144c70051c0c0a8a6490181b2b3a5d828143e9ab2303ef92a1f5b94829b`.

## Claim boundary

These labels are discovery leads based on supplied bibliographic records. They do not establish method validity, authoritative lineage, software correctness, data feasibility, or suitability as a flagship study.
