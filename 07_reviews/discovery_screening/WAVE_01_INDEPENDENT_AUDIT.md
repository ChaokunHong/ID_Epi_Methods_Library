# Wave 1 independent screening audit

Date: 2026-07-20; authoritative fourth-repair refresh: 2026-07-21

## Selection

The approved plan's primary-family strata and the production validator's full-`preliminary_families` strata were both honored. The selected set is the union of:

1. the plan formula by primary decision, reason code, and precedence-selected primary family;
2. the validator formula by primary decision, reason code, and full family string;
3. 100% of primary uncertain and `X_NOT_INFECTIOUS_TRANSFERABLE` rows; and
4. all members of every possible-title-duplicate group.

The earlier second-repair selection of 1,561 rows and third-repair selection of 1,656 rows are historical and superseded. After the fourth-repair semantic replacement, the authoritative recomputation has 60 plan primary-family strata requiring 1,548 keys and 90 validator full-family strata requiring 1,612 keys. Their formula union contains 1,615 keys. Adding 38 otherwise unselected possible-duplicate rows produces 1,653 audited keys in 23 source batches. The ordered audit-key-list SHA256 is `dae22cad0a64d8454ebdf5dc410e5339b9815a1737a74dbf2120c6036817cde3`.

The set includes complete coverage of all 701 primary uncertain or `X_NOT_INFECTIOUS_TRANSFERABLE` rows and all 81 rows in 40 possible-title-duplicate groups. Wave 1 is part of the 2,535-row two-wave fourth-repair selection. Across both waves, 2,529 prior audit rows were reused only after per-row proof that source SHA, complete primary triple, primary reviewer, and selection membership were unchanged; six rows received one fresh decision-blind read. Thirty-five immutable read-only `gpt-5.6-sol` sessions cover the combined selection, and every audit reviewer remains independent of the corresponding primary reviewer and the fourth-repair semantic sessions.

## Outcome

| Audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 1,032 |
| Open conflict | 621 |
| Resolved conflict | 0 |
| Total | 1,653 |

Every one of the 621 conflicts remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank final proposed type, and blank adjudicator. There was no automatic conflict resolution. Unselected rows retain their primary triple; agreement rows take the audit triple and reason.

Audit-decision counts are: exclude 605; applied seed 537; diagnostic/correction lead 128; method-source lead 170; simulation/mechanistic lead 212; and one explicit primary-record uncertainty. The audit produced no unsupported shortcut.

`screening_audit.csv` SHA256: `08316f05366e27c54ec03ab10b3de1faea843dfe23d71468a976e4378eafd671`.

Across both waves, the authoritative formal audit contains 2,535 rows: W1 1,653 and W2 882. It reached 1,647 agreements and 888 open conflicts. The complete ordered selection SHA256 is `e17aa6a335b36bb0d771063c897b915b78be518a13ad30f70e97e6fa0aebb3c8`; combined accepted audit-decision SHA256 is `397f13e7afda807bb23b1a68c47ca47629e5349c267b1bad8e8bf78c48561a95`; formal-audit proof-ledger SHA256 is `f71bd8a5195ec33fef7c19297a2ea8b3482bba2c0d1e05ebcfcf16783c1547d1`. Exact reuse, fresh-execution, per-row, and per-session provenance is recorded in `TASK_5_FOURTH_REPAIR_PROVENANCE.md`.

Both commands passed after live assembly:

```text
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
```

All authoritative audit results come from the fourth-repair recomputed union selection. Reuse is limited to the 2,529 rows with explicit equality and independence proof; the six changed/newly selected rows use the fresh fourth-repair auditor.
