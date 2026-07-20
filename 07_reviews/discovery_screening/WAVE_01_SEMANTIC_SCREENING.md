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
| `include_applied_seed` | 2,904 |
| `include_method_source_lead` | 1,223 |
| `include_diagnostic_or_correction_lead` | 793 |
| `include_simulation_or_mechanistic_lead` | 1,163 |
| `uncertain_retrieve_primary` | 41 |
| `exclude` | 1,022 |

Primary reason-code counts are: `I_APPLIED_TRANSFERABLE_DESIGN` 2,904; `I_METHOD_SOURCE` 1,223; `I_DIAGNOSTIC_CORRECTION` 793; `I_SIMULATION_MECHANISTIC` 1,163; `U_PRIMARY_RECORD_NEEDED` 41; `X_NOT_INFECTIOUS_TRANSFERABLE` 541; `X_DESCRIPTIVE_ONLY` 297; `X_COMMENTARY_ONLY` 97; `X_WRONG_RECORD_TYPE` 61; and `X_DUPLICATE` 26.

## Post-review scope correction

The first Task 5 review found that `PMID:20826636` had been incorrectly collapsed into the distinct retraction notice `PMID:21372330` and that molecular docking, product-design, structural-biology, and vaccine-construction records had drifted into the simulation track. The correction did not use keywords as exclusion rules. It froze and semantically reread an exact 256-record locator universe: all 205 Wave 1 and 51 Wave 2 records matching the review locator, plus the explicit `PMID:20826636`/`PMID:21372330` pair. The frozen universe SHA256 is `e118c48e685c7c69cb64fd1667e93ea1aed4ceaaddf7304e4b4389eb505228bd`; its ordered-record SHA256 is `499feffa6c00fd722191fdf77d26ab43128b2becb2574fbbc6bcad9776097137`.

Two independent title-and-abstract readers reread all 256 records. Reader A initially retained 138 and excluded 118; Reader B retained 134 and excluded 122. Their 25 complete-triple disagreements were frozen before a separate blind adjudicator received only raw bibliographic records and duplicate peers. Twenty of those 25 triples changed at adjudication. The corrected 256-record primary state retains 132 and excludes 124: Wave 1 retains 86 and excludes 119; Wave 2 retains 46 and excludes 5. Reader B agrees with the repaired primary triple on 247 of 256 records; the remaining nine semantic disagreements were not silently resolved.

The adopted blind-adjudication response SHA256 is `7afcd19ca5069bbc2cac4fda8f74411f28d214040f4a2cddb8c364065275282f`; its validation/application receipt SHA256 is `915fc3ea6c9eb5896d0404af0b7d15f5afd3fc4e61b21296bc7ad6aabc1f4f39`. Three earlier adjudication attempts were rejected with zero adoption: one exposed reader labels, one named the wrong approved plan, and one misapplied `X_NOT_INFECTIOUS_TRANSFERABLE` and treated retraction status as `X_WRONG_RECORD_TYPE`.

The corrected simulation boundary is the approved four-part track: epidemiological estimator evaluation, new estimator/diagnostic/uncertainty development, reproducible analytical-practice benchmarking, or mechanistic transmission/selection/surveillance/agent-based modelling. Infection-related molecular simulation alone is not sufficient.

## Rejected outputs and recovery rule

No partial row from a failed semantic response was reused. Two initial collaboration-reader attempts produced zero usable rows. Later failures included transport interruption, missing/duplicated keys, and illegal decision mappings in batches 033, 034, 037, 040, and 041. Each affected complete batch was rejected, preserved in the ignored execution record, and reread through a fresh schema-constrained session or fresh contiguous subparts. The final 48 CSVs each passed the complete-manifest validator.

## Post-audit final state

After recomputing the complete audit selection from the repaired primary ledger, the 7,146 final rows comprise 2,853 applied seeds, 1,108 method-source leads, 706 diagnostic/correction leads, 1,119 simulation/mechanistic leads, 740 exclusions, and 620 honest primary-record uncertainties. The uncertainty rows are caused only by open independent-reader conflicts; none was automatically adjudicated.

`screened_candidates.csv` SHA256: `32dd0d346960932be91bfafefd001783bd62fcef6e3aa1d7e21d69eed23b2e3a`.

## Claim boundary

These labels are discovery leads based on supplied bibliographic records. They do not establish method validity, authoritative lineage, software correctness, data feasibility, or suitability as a flagship study.
