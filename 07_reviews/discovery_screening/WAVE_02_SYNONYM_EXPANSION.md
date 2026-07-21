# Wave 2 synonym-expansion record

Date: 2026-07-20
Status at creation: retrieval and compilation verified; complete semantic screening and independent audit recorded below when closed.

## Derivation

Actual Wave 1 title/abstract reading identified one bounded synonym gap per family. The registry cites inspected candidate keys and retains the exact infectious-disease and frozen publication-date blocks.

| Family | New labels | Example inspected Wave 1 keys | PubMed count |
|---|---|---|---:|
| causal policy | `g-formula`, `g formula`, `g-computation` | `PMID:40492009`, `PMID:42350043` | 141 |
| surveillance measurement | `under-reporting`, `underreporting`, `under-report` | `PMID:23691004`, `PMID:24122943` | 1,783 |
| spatial transmission | `phylodynamic*` | `PMID:22251065`, `PMID:24787998` | 1,138 |
| forecasting dynamics | `EpiEstim` | `PMID:36812522`, `PMID:37639484` | 43 |
| evidence synthesis | `data fusion`, `evidence integration` | `PMID:23569606`, `PMID:39218437` | 125 |
| simulation methods | `microsimulation` | `PMID:28918407`, `PMID:33188729` | 349 |

The queries were not narrowed after observing their counts. `run-wave`, `compile`, and `verify` each returned `DISCOVERY PASS`. The 3,579 raw query results compiled to 3,571 unique PMID candidates.

- `QUERY_REGISTRY.csv` SHA256: `05227366bcd08223483654af5075e67682d88ad5500f696bcd9fd9e08e4c1b04`.
- `RUN_RECEIPT.json` SHA256: `fd55026aac0de98998f11a8abcfd436d4a72811ea43d24372e3f273c96499352`.
- `compiled_candidates_raw.csv` SHA256: `1b16a66efe3bf850f23b523482c82f3c9c989dbf5cf81b3a0dcac3f73aec2011`.
- Ordered candidate-key-list SHA256: `11426333ef52e3aa4bfbbfe9064f89ffe7debe0c98ff1cb5d4725b5b99510f1d`.

## Cross-wave reconciliation and screening design

Exactly 192 candidate keys already occur in Wave 1. They are preserved as Wave 2 provenance rows and assigned identifier-confirmed `X_DUPLICATE` primary dispositions pointing to the same retained Wave 1 key. The remaining 3,379 keys are frozen in 23 semantic manifests: 22 batches of 150 and one batch of 79. Every semantic batch is read by a fresh read-only model session and accepted only on exact key order, legal mapping, concrete rationale, and source SHA.

Independent audit selection uses the same strict union contract as Wave 1: plan primary-family strata, validator full-family strata, complete uncertain/`X_NOT_INFECTIOUS_TRANSFERABLE` coverage, and every possible-title-duplicate member. Exact Wave 1 identifier matches selected by the formula are shown the prior bibliographic record during audit.

## Closure results

All 3,379 cross-wave delta keys were semantically read in 23 complete manifests (22 of 150 records and one of 79). Together with the 192 identifier-confirmed Wave 1 overlaps, primary screening covers all 3,571 Wave 2 keys. Twenty-three fresh semantic-reader identities cover the delta manifests; the deterministic identifier-deduplication reader is recorded separately. Every complete batch passed exact key order, decision/code/type mapping, concrete-reason, and source-SHA checks before integration. Two transport reconnects occurred inside the batch 011 client session, but only its eventual complete 150-row response was imported; no partial transport output was reused.

Primary decisions are 1,438 applied seeds, 379 diagnostic/correction leads, 323 method-source leads, 527 simulation/mechanistic leads, 898 exclusions, and 6 primary-record uncertainties. The 898 exclusions comprise 39 commentary-only, 326 descriptive-only, 218 duplicates (including all 192 exact Wave 1 identifier matches), 293 not-infectious/transferable, and 22 wrong-record-type decisions.

The strict audit union selects 830 keys in 17 batches: the plan formula requires 797 keys, the validator formula requires 805, and their formula union contains 805. It includes complete coverage of all 299 primary uncertain or `X_NOT_INFECTIOUS_TRANSFERABLE` rows and all 38 possible-title-duplicate rows, of which 25 are additional to the formula union. The ordered audit-key-list SHA256 is `fd303dbfcf79d152eea76d5e62df755761471420cd0f60651723d3580a45ae4f`. The recomputation preserves 746 prior independent rows only where source SHA, full primary triple, primary reviewer, selection membership, reviewer independence, and semantic premise are unchanged; it uses Reader B for 75 selected scope-reread rows and fresh session `019f81fb-b235-74f2-9743-40be040cbd68` for nine newly selected records. Every reviewer remains independent from the corresponding primary reader.

| Independent-audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 565 |
| Open conflict | 265 |
| Resolved conflict | 0 |
| Total | 830 |

Every conflict remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank proposed type, and blank adjudicator. There was no automatic resolution. The final screened ledger contains 1,405 applied seeds, 351 diagnostic/correction leads, 294 method-source leads, 510 simulation/mechanistic leads, 745 exclusions, and 266 primary-record uncertainties.

- `screened_candidates.csv` SHA256: `dc32a9b2fa2ae4cbeda9bbfa17d635c2db2c2519884f3eedcb6b6623fe271baa`.
- `screening_audit.csv` SHA256: `d38d534251c371555c57f491705131ae78a1eee5578093921a35dac03cc0f814`.
- `validate-screening`: `DISCOVERY PASS`.
- `validate-audit`: `DISCOVERY PASS`.

The second scope repair semantically reread 454 Wave 2 locator records instead of applying keyword exclusions. Their repaired primary state contains 220 applied seeds, 53 diagnostic/correction leads, 46 method-source leads, 87 simulation/mechanistic leads, and 48 exclusions. This is the Wave 2 portion of the frozen 1,465-record universe documented in the Wave 1 semantic-screening record and `TASK_5_SECOND_REPAIR_PROVENANCE.md`.

## Claim boundary

Wave 2 is a bounded synonym-gap expansion, not evidence of exhaustive saturation. All retained rows remain discovery leads; no substantive method claim, authoritative lineage, dataset feasibility, or flagship status is established here.
