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
| `include_applied_seed` | 2,891 |
| `include_method_source_lead` | 1,128 |
| `include_diagnostic_or_correction_lead` | 815 |
| `include_simulation_or_mechanistic_lead` | 1,110 |
| `uncertain_retrieve_primary` | 41 |
| `exclude` | 1,161 |

Primary reason-code counts are: `I_APPLIED_TRANSFERABLE_DESIGN` 2,891; `I_METHOD_SOURCE` 1,128; `I_DIAGNOSTIC_CORRECTION` 815; `I_SIMULATION_MECHANISTIC` 1,110; `U_PRIMARY_RECORD_NEEDED` 41; `X_NOT_INFECTIOUS_TRANSFERABLE` 558; `X_DESCRIPTIVE_ONLY` 401; `X_COMMENTARY_ONLY` 102; `X_WRONG_RECORD_TYPE` 66; and `X_DUPLICATE` 34.

## Post-review scope correction

The fixed-head review found that the first 256-record locator was incomplete: it missed retained preclinical efficacy, host-biology, product-development, vaccine/therapeutic/antigen, and related laboratory records outside the approved epidemiological-method boundary. It also found that 25 adopted rows carried a nonexistent adjudicator alias. The second repair therefore began from every Wave 1/2 primary or final inclusion, applied conservative locator patterns to normalized title plus abstract text, and unioned the complete earlier 256-row universe, the 25 invalid-provenance rows, and all three confirmed examples. Locator membership never decided disposition.

The resulting frozen universe contains 1,465 unique `(wave, candidate_key)` rows: W1 1,011 and W2 454. Its file SHA256 is `c71762e584dc53771318bcb6899ffd26aab9c362dea73773df70b03a65839abb`; ordered-record SHA256 is `0e0acd5a50a6ed833ae0153934401daeba919cd713de361a6be54a76fe9e2ce4`; ordered-entry SHA256 is `144e7fee78298266bfbd45ddc5bbf5810ec4e0fed6e53e9e9b344aa1eee62407`. Exact construction, patterns, reason incidences, source-row SHAs, and per-session receipts are recorded in `TASK_5_SECOND_REPAIR_PROVENANCE.md`.

Two independent decision-blind, locator-blind reader sets each reread all 1,465 records in 20 batches and 40 unique read-only CLI sessions, with no session reuse. Their complete decision/code/type triples agreed for 1,287 rows and conflicted for 178. The fresh blind-adjudication set was the exact union of those 178 conflicts and all 25 invalid-provenance rows: 195 rows because eight belonged to both sets. Four new adjudicator sessions covered 195/195, shared no reader session, and saw raw records plus needed duplicate peers but no reader decisions. The final application used Reader A only for 1,270 non-conflict complete-triple agreements and fresh adjudication for the remaining 195 rows.

The repaired 1,465-row state contains 573 applied seeds, 101 method-source leads, 166 diagnostic/correction leads, 319 simulation/mechanistic leads, and 306 exclusions. Its decision-ledger SHA256 is `206d534aca05ed5a5fef24311e7f14196bcdcb813ab4e9a871c837a31d73e677`; the accepted blind-adjudication output SHA256 is `7bb18b4c4c06ce6de2d611e8760fc8deb0d1f77d989f2cfdce54fbe60e67920b`. All 25 invalid first-repair adjudications were replaced, and the nonexistent reviewer suffix is absent from the repaired primaries.

The corrected simulation boundary is the approved four-part track: epidemiological estimator evaluation, new estimator/diagnostic/uncertainty development, reproducible analytical-practice benchmarking, or mechanistic transmission/selection/surveillance/agent-based modelling. Infection-related molecular simulation alone is not sufficient.

## Rejected outputs and recovery rule

No partial row from a failed semantic response was reused. During the second repair, Reader A batch 020 and Reader B batch 007 each failed exact response identity/order checks; blind-adjudicator batch 001 supplied duplicate-only fields for a nonduplicate row. Each complete response was rejected with zero adoption and replaced by a genuinely fresh session. Exact rejected prompt/input/output/receipt paths, SHAs, session UUIDs, and rejection reasons are durable in `TASK_5_SECOND_REPAIR_PROVENANCE.md`.

## Post-audit final state

After recomputing the complete audit selection from the repaired primary ledger, the 7,146 final rows comprise 2,846 applied seeds, 1,022 method-source leads, 738 diagnostic/correction leads, 1,077 simulation/mechanistic leads, 884 exclusions, and 579 honest primary-record uncertainties. The uncertainty rows are caused only by open independent-reader conflicts; none was automatically adjudicated.

`screened_candidates.csv` SHA256: `27fe02f20391a101e6ef5e57828a92c1306398a4e3b2f986c846ddbdb3b95e2b`.

## Claim boundary

These labels are discovery leads based on supplied bibliographic records. They do not establish method validity, authoritative lineage, software correctness, data feasibility, or suitability as a flagship study.
