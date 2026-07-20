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

Primary decisions were 1,464 applied seeds, 390 diagnostic/correction leads, 322 method-source leads, 539 simulation/mechanistic leads, 850 exclusions, and 6 primary-record uncertainties. The 850 exclusions comprise 37 commentary-only, 286 descriptive-only, 217 duplicates (including all 192 exact Wave 1 identifier matches), 288 not-infectious/transferable, and 22 wrong-record-type decisions.

The strict audit union selected 815 keys in 17 batches: the plan formula required 782 keys, the validator formula required 790, and their formula union contained 790. It includes complete coverage of all 294 primary uncertain or `X_NOT_INFECTIOUS_TRANSFERABLE` rows and all 38 possible-title-duplicate rows, of which 25 were additional to the formula union. The ordered audit-key-list SHA256 is `da0047c2709e3ba0dadfc51239bb5e44a07ef6c8f1c6f1811ab323045d2bec12`. Each audit batch used a fresh read-only reviewer identity, received no primary decision, and—where applicable—received the prior Wave 1 bibliographic peer for comparison.

| Independent-audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 536 |
| Open conflict | 279 |
| Resolved conflict | 0 |
| Total | 815 |

Every conflict remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank proposed type, and blank adjudicator. There was no automatic resolution. The final screened ledger contains 1,430 applied seeds, 351 diagnostic/correction leads, 290 method-source leads, 523 simulation/mechanistic leads, 697 exclusions, and 280 primary-record uncertainties.

- `screened_candidates.csv` SHA256: `dcfeb03ee095659b837cd4f583ab77780f16cfa062502bcd2dfc661ce4d87e12`.
- `screening_audit.csv` SHA256: `614c9c28748a9ff2d672b349e2a3b67731506bd9ee3b0ebf8fed4a04cfadbb99`.
- `validate-screening`: `DISCOVERY PASS`.
- `validate-audit`: `DISCOVERY PASS`.

## Claim boundary

Wave 2 is a bounded synonym-gap expansion, not evidence of exhaustive saturation. All retained rows remain discovery leads; no substantive method claim, authoritative lineage, dataset feasibility, or flagship status is established here.
