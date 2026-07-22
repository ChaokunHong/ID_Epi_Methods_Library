# Cross-wave family coverage and residual uncertainty audit

## Scope and claim boundary

This Task 7 audit was computed from the live, frozen Wave 1, Wave 2, Wave 3, screening, registry, and lineage artifacts at base `b2cc2d2d062d570ed5d6f2e18ee3c8d3519d4223`. It assesses whether each approved method family is ready to enter a later primary-source verification plan. It does not verify substantive method or source-role claims, rank candidates, select a flagship, or assert comprehensive retrieval.

Task 7 executed no query, appended no search record, and changed no Wave 1, Wave 2, or Wave 3 search input or output. Synonym and lineage-lead counts below describe records already frozen by earlier waves; they are not Task 7 additions.

## Computation rules

| Matrix field | Live derivation |
|---|---|
| `wave_01_root_cells` | Root receipt rows in `wave_01_frozen_queries/RUN_RECEIPT.json`, grouped by `family`. |
| `wave_01_leaf_cells` | Recursive terminal leaf receipt rows from the same receipt, grouped by `family`. |
| `wave_02_status` | The sole family row in `wave_02_synonym_expansion/QUERY_REGISTRY.csv`; each row says `executed` and has a matching receipt cell. |
| `wave_02_unique_delta` | Unique Wave 2 raw candidate keys absent from the Wave 1 raw key set, counted in every Wave 2 `preliminary_families` route to which the key belongs. |
| `wave_03_lineage_queries` | Unique `query_id` rows in `LINEAGE_QUERY_REGISTRY.csv`, joined exactly to `LINEAGE_RUN_RECEIPT.json`. |
| `unique_candidates` | Unique identifier-level keys in the Wave 1/2 union, counted once within every contributing raw `preliminary_families` route. A cross-family key may therefore contribute to more than one family row. |
| Four retained-role columns | The 7,779 rows in `canonical_method_assignments.csv`, grouped by final canonical family and final screened decision. These four columns partition the retained assignment set. |
| `canonical_method_concepts` | Rows in `canonical_method_concepts.csv`, grouped by final family; each concept is joined to exactly one `method_id`. |
| `unresolved_records` | Global keys with `final_decision=uncertain_retrieve_primary`, counted in every contributing raw family route. There are 893 unique keys globally; family memberships sum to 909 because 16 are cross-family memberships. |
| `unresolved_lineage` | Rows in `global/lineage_ledger.csv` whose terminal status is `ambiguous` or `unresolved_after_three_queries`, grouped by family. |
| `new_synonym_labels` | Pipe-delimited labels already frozen in the sole Wave 2 query-registry row for each family. |
| `new_lineage_role_candidates` | Rows already frozen in `LINEAGE_NAMED_SOURCES.csv`, grouped by family. These are bibliographic/source-role leads at `discovery`, not verified role claims. |

## Six-family result

The machine-readable result is `coverage_matrix.csv`.

| Family | W1 root/leaf | W2 unique delta | W3 queries / candidate rows | Raw unique candidates | Retained A/M/D/S | Concepts | Screen unresolved | Lineage unresolved | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `causal_policy` | 2 / 2 | 137 | 128 / 111 | 1,252 | 998 / 88 / 86 / 64 | 61 | 148 | 0 | `adequate_for_primary_source_verification` |
| `surveillance_measurement` | 2 / 2 | 1,740 | 240 / 205 | 2,911 | 961 / 200 / 414 / 87 | 84 | 243 | 1 | `adequate_for_primary_source_verification` |
| `spatial_transmission` | 2 / 2 | 1,027 | 84 / 74 | 2,618 | 1,644 / 242 / 64 / 390 | 32 | 160 | 2 | `adequate_for_primary_source_verification` |
| `forecasting_dynamics` | 2 / 2 | 29 | 155 / 142 | 1,606 | 437 / 307 / 185 / 269 | 46 | 163 | 0 | `adequate_for_primary_source_verification` |
| `evidence_synthesis` | 2 / 2 | 120 | 67 / 59 | 409 | 151 / 49 / 99 / 10 | 36 | 57 | 1 | `adequate_for_primary_source_verification` |
| `simulation_methods` | 2 / 2 | 333 | 49 / 43 | 1,860 | 34 / 35 / 72 / 893 | 18 | 138 | 0 | `adequate_for_primary_source_verification` |

`A/M/D/S` means applied seed / method-source lead / diagnostic-or-correction lead / simulation-or-mechanistic lead. Wave 3 candidate rows are the 634 rows in `pubmed_lineage_candidates.csv` plus the zero rows in `crossref_candidates.csv`, joined to query family. Each candidate key is unique in the active Wave 3 candidate tables.

All six families satisfy the plan's stated threshold: both frozen Wave 1 roots and their leaves reached terminal success; Wave 1/2 screening and audits validate; each family retains at least one applied or simulation/mechanistic lead and at least one method-source lead; and every family has an executed Wave 2 bounded synonym expansion plus terminally audited Wave 3 lineage queries. The verdict therefore means readiness for the next verification stage, not proof that no additional method label or source exists.

## Cross-wave and registry reconciliation

- Wave 1 has 7,146 unique raw keys and 7,146 matching screened keys. Wave 2 has 3,571 unique raw keys and 3,571 matching screened keys. Each raw key has exactly one final screened decision in its wave.
- The two raw sets overlap on 192 identifier keys. Their union is 10,525 keys, exactly equal to the 10,525 unique rows in `candidates_through_wave_02.csv`. The global index contains 10,717 manifested source-row SHA references: one per contributing wave and two for each overlap key; zero references are invalid.
- Global decisions partition the union into 7,779 retained keys, 893 `uncertain_retrieve_primary` keys, and 1,853 excluded keys.
- The 7,779 retained keys equal the key set in `canonical_method_assignments.csv`. All 7,779 assignments have one unique permanent paper ID, and that ID set equals `03_evidence_tables/papers.csv`.
- The 277 canonical concept keys each map to exactly one method ID through the assignment table. Those 277 IDs equal `03_evidence_tables/methods.csv`.
- Wave 3 has 723 unique query-registry IDs, 723 matching receipt query IDs, and 723 query IDs represented through the supporting-query fields of terminal identity audits. All receipt queries reached terminal success.
- The 634 active Wave 3 candidate rows reference registered queries and manifested raw artifacts. The 620 named sources equal the 620 identity-audit rows and the 620 global lineage-ledger rows.
- Identity outcomes are 616 resolved, two ambiguous, and two unresolved after three queries, with zero open conflicts. Every resolved row has one unique retained candidate key and one matching permanent paper ID: 616 of 616.
- Provisional relationship decisions partition the 7,779 assignments into 6,711 emitted discovery relationships and 1,068 explicit omissions. The normalized authoritative relationship registry remains header-only pending a later primary-source verification plan.

The exact machine-readable proof and required terminal marker are in `GLOBAL_KEY_RECONCILIATION.txt`.

## Immutable-wave and no-search proof

Each validator was run independently before this audit was written:

| Frozen component | Validation result | Receipt / manifest SHA256 |
|---|---|---|
| Wave 1 search | `DISCOVERY PASS` | receipt `69d70bdfa3069aeb255ab0cff75cadbb687f6200651021efccde2530fb917dde`; manifest `5eae2041ee03bd6f6bdfec01a94c3f72b9f9231a3699a78c5407e0fd46428890` |
| Wave 1 screening | `DISCOVERY PASS` | Recomputed against the manifested raw table and screened ledger. |
| Wave 1 audit | `DISCOVERY PASS` | Recomputed against primary and screened provenance. |
| Wave 2 search | `DISCOVERY PASS` | query registry `05227366bcd08223483654af5075e67682d88ad5500f696bcd9fd9e08e4c1b04`; receipt `fd55026aac0de98998f11a8abcfd436d4a72811ea43d24372e3f273c96499352`; manifest `d61d218f7e9e551efb48adc338cbd620870c329f6259f35b6f0938da8fb107fa` |
| Wave 2 screening | `DISCOVERY PASS` | Recomputed against the manifested raw table and screened ledger. |
| Wave 2 audit | `DISCOVERY PASS` | Recomputed against primary and screened provenance. |
| Wave 3 lineage | `DISCOVERY PASS` | query registry `8c9a2f35440801c6bfc0ec0be49d4b85227a5357665c30689d8498044573537b`; receipt `02f1ba3f3feedea38df35850feea5e04c0158aa393b7b8947a9cfcbe9131cc38`; manifest `ffa418de2eb2d0017da8202f362f4080fe444c2ca1029bae9b54479fcbe473b7` |

Before/after SHA256 tree digests over each wave's raw directory plus its query registry where applicable, receipt, manifest, and active candidate tables where applicable are identical:

- Wave 1: 58 files, `7aa9211f6296031c73a15f69d51f0cf8b4f16f2038822359b056df56ddd63250`.
- Wave 2: 29 files, `ea8cb830dcac78f48689b9ff772b8483d45942f35501ef562fc8da34aaceb6ff`.
- Wave 3: 1,346 files, `762b91a32a37ad91be29900356f3c6a01b3af94025acff84b5773356d15333cd`.

The Task 7 diff is confined to this audit, the matrix, and the global reconciliation proof. Search additions in Task 7: zero.

## Residual uncertainty for a future plan

- The 893 unique `uncertain_retrieve_primary` screening records remain deferred. They are not silently excluded or promoted.
- Four lineage identities remain non-resolved: `NS-EVIDENCE-033` and `NS-SPATIAL-049` are ambiguous; `NS-SPATIAL-031` and `NS-SURVEILLANCE-156` are unresolved after three queries. They remain explicit future verification work.
- The 11 Wave 2 synonym labels (`g-formula`, `g formula`, `g-computation`, `under-reporting`, `underreporting`, `under-report`, `phylodynamic*`, `EpiEstim`, `data fusion`, `evidence integration`, and `microsimulation`) and 620 Wave 3 named-source leads remain frozen discovery provenance. Any later synonym or lineage expansion requires a separately approved plan.
- All 277 method concepts, 7,779 paper records, and 6,711 provisional relationships remain at `discovery`. Primary-source verification, mature cards, translation generation, feasibility work, portfolio ranking, and project graduation remain outside Task 7.
