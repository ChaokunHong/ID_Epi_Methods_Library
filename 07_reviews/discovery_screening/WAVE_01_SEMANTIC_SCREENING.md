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

The table immediately below records the original 2026-07-20 primary pass. It is historical and was superseded first by the second repair and then by the exhaustive third repair documented later in this file.

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

This section records the historical second repair. Its 1,465-row locator, distributions, and post-audit totals are superseded by the exhaustive third-repair state below; they remain here only to preserve the execution history.

The fixed-head review found that the first 256-record locator was incomplete: it missed retained preclinical efficacy, host-biology, product-development, vaccine/therapeutic/antigen, and related laboratory records outside the approved epidemiological-method boundary. It also found that 25 adopted rows carried a nonexistent adjudicator alias. The second repair therefore began from every Wave 1/2 primary or final inclusion, applied conservative locator patterns to normalized title plus abstract text, and unioned the complete earlier 256-row universe, the 25 invalid-provenance rows, and all three confirmed examples. Locator membership never decided disposition.

The resulting frozen universe contains 1,465 unique `(wave, candidate_key)` rows: W1 1,011 and W2 454. Its file SHA256 is `c71762e584dc53771318bcb6899ffd26aab9c362dea73773df70b03a65839abb`; ordered-record SHA256 is `0e0acd5a50a6ed833ae0153934401daeba919cd713de361a6be54a76fe9e2ce4`; ordered-entry SHA256 is `144e7fee78298266bfbd45ddc5bbf5810ec4e0fed6e53e9e9b344aa1eee62407`. Exact construction, patterns, reason incidences, source-row SHAs, and per-session receipts are recorded in `TASK_5_SECOND_REPAIR_PROVENANCE.md`.

Two independent decision-blind, locator-blind reader sets each reread all 1,465 records in 20 batches and 40 unique read-only CLI sessions, with no session reuse. Their complete decision/code/type triples agreed for 1,287 rows and conflicted for 178. The fresh blind-adjudication set was the exact union of those 178 conflicts and all 25 invalid-provenance rows: 195 rows because eight belonged to both sets. Four new adjudicator sessions covered 195/195, shared no reader session, and saw raw records plus needed duplicate peers but no reader decisions. The final application used Reader A only for 1,270 non-conflict complete-triple agreements and fresh adjudication for the remaining 195 rows.

The repaired 1,465-row state contains 573 applied seeds, 101 method-source leads, 166 diagnostic/correction leads, 319 simulation/mechanistic leads, and 306 exclusions. Its decision-ledger SHA256 is `206d534aca05ed5a5fef24311e7f14196bcdcb813ab4e9a871c837a31d73e677`; the accepted blind-adjudication output SHA256 is `7bb18b4c4c06ce6de2d611e8760fc8deb0d1f77d989f2cfdce54fbe60e67920b`. All 25 invalid first-repair adjudications were replaced, and the nonexistent reviewer suffix is absent from the repaired primaries.

The corrected simulation boundary is the approved four-part track: epidemiological estimator evaluation, new estimator/diagnostic/uncertainty development, reproducible analytical-practice benchmarking, or mechanistic transmission/selection/surveillance/agent-based modelling. Infection-related molecular simulation alone is not sufficient.

## Rejected outputs and recovery rule

No partial row from a failed semantic response was reused. During the second repair, Reader A batch 020 and Reader B batch 007 each failed exact response identity/order checks; blind-adjudicator batch 001 supplied duplicate-only fields for a nonduplicate row. Each complete response was rejected with zero adoption and replaced by a genuinely fresh session. Exact rejected prompt/input/output/receipt paths, SHAs, session UUIDs, and rejection reasons are durable in `TASK_5_SECOND_REPAIR_PROVENANCE.md`.

## Exhaustive third repair and authoritative state

The third repair eliminated the incomplete locator class. Its frozen universe is the deterministic union of every Wave 1/2 current primary or final inclusion, every correction/retraction-status metadata candidate, every prior 1,465-key second-repair member, and every named Task 5 finding or reviewer-axis example. The result contains 8,984 unique `(wave, candidate_key)` rows: W1 6,237 and W2 2,747. The universe SHA256 is `20121c35624169c8a4743d3373140b64e8efb858ee213a583f7cea342f5fba8e`; ordered-key SHA256 is `b0ffef5fda997c9aaecdcf7524a53d6063a818c4fd71524905063318919518b0`; ordered-record SHA256 is `919d07fbea814f994385a92da83c628f546c55927dc3eb77a196f98b6e6e4484`; ordered raw-content SHA256 is `e2265c97c5829fae2adb8186225dbbc31d3cc029c6d4616b23eb24a397e20588`. Membership routed reading only and never decided a disposition.

Reader A and Reader B each semantically read all 8,984 rows in 120 accepted batches, using 240 unique, mutually disjoint, fresh read-only sessions. They reached 7,985 complete agreements and 999 conflicts. Twenty fresh blind-adjudicator sessions covered exactly 999/999 conflicts without seeing either reader's labels or identities. The final semantic ledger SHA256 is `7c6d6b9004ecd66869eec7b9d97d2720885d2021319b3d36111024dae1d615b8` and contains 4,292 applied seeds, 990 diagnostic/correction leads, 960 method-source leads, 1,740 simulation/mechanistic leads, and 1,002 exclusions.

All 8,984 universe rows were evaluated. Their semantic dispositions were adopted for 8,978 rows. Six Wave 2 rows remained deterministic identifier-only duplicates because the same candidate keys occur in Wave 1; this preserves the identifier layer rather than changing the semantic ledger. All 192 Wave 1/Wave 2 exact identifier overlaps remain Wave 2 `exclude / blank type / X_DUPLICATE` primaries retaining the identical Wave 1 key. The superseded pre-identity application and superseded audit are retained with zero final adoption in `TASK_5_THIRD_REPAIR_PROVENANCE.md`.

The authoritative Wave 1 primary ledger now contains 2,913 applied seeds, 677 diagnostic/correction leads, 696 method-source leads, 1,236 simulation/mechanistic leads, 1,584 exclusions, and 40 primary-record uncertainties. A fresh audit of the entire recomputed 1,656-row Wave 1 selection reached 1,030 complete decision/reason/type agreements and 626 open conflicts. No conflict was automatically resolved.

The authoritative 7,146-row final ledger comprises 2,882 applied seeds, 621 diagnostic/correction leads, 671 method-source leads, 1,203 simulation/mechanistic leads, 1,143 exclusions, and 626 honest primary-record uncertainties. The uncertainty rows are exactly the open independent-audit conflicts.

The six newly named Wave 1 scope misses were not forced to a predetermined result. Both-reader/blind semantic handling classified `PMID:25450804`, `PMID:26014946`, `PMID:28358222`, `PMID:30221005`, `PMID:24731529`, and `PMID:33024578` as `exclude / blank type / X_DESCRIPTIVE_ONLY`, consistent with therapeutic-product optimization, preclinical host physiology, or molecular/pathogenesis work rather than one of the approved epidemiological simulation forms. `PMID:25450804` was in the recomputed audit and received the same triple; the other five were not formula-selected and retain their primary triples.

- `screening_audit.csv` SHA256: `d4540fb9bbe5f9150d72db1a1d0f35e707a4739dfad482964c39eb0cf7e2f010`.
- `screened_candidates.csv` SHA256: `728d8297273fb4d27294bc23bed1ebe49cce3393a92b525526966b0bdd9423cc`.
- Complete executable/session/artifact provenance: `TASK_5_THIRD_REPAIR_PROVENANCE.md`.

## Claim boundary

These labels are discovery leads based on supplied bibliographic records. They do not establish method validity, authoritative lineage, software correctness, data feasibility, or suitability as a flagship study.
