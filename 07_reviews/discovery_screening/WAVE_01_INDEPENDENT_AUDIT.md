# Wave 1 independent screening audit

Date: 2026-07-20

## Selection

The approved plan's primary-family strata and the production validator's full-`preliminary_families` strata were both honored. The selected set is the union of:

1. the plan formula by primary decision, reason code, and precedence-selected primary family;
2. the validator formula by primary decision, reason code, and full family string;
3. 100% of primary uncertain and `X_NOT_INFECTIOUS_TRANSFERABLE` rows; and
4. all members of every possible-title-duplicate group.

The earlier second-repair selection of 1,561 rows is historical and superseded. After exhaustive semantic application, the authoritative recomputation has 60 plan primary-family strata requiring 1,551 keys and 90 validator full-family strata requiring 1,616 keys. Their formula union contains 1,618 keys. Adding 38 otherwise unselected possible-duplicate rows produces 1,656 audited keys in 23 source batches. The ordered audit-key-list SHA256 is `f93d7df08a5fd44a76eacebb7bc4b91275532decdf1ac50b3934734f68b417fe`.

The set includes complete coverage of all 704 primary uncertain or `X_NOT_INFECTIOUS_TRANSFERABLE` rows and all 81 rows in 40 possible-title-duplicate groups. No earlier audit decision was reused. Wave 1 is part of a fresh decision-blind audit of the entire 2,542-row two-wave recomputed selection. Thirty-four immutable read-only `gpt-5.6-sol` sessions cover the combined selection; every audit reviewer is disjoint from all semantic-reader and blind-adjudicator sessions and differs from the corresponding primary reviewer.

## Outcome

| Audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 1,030 |
| Open conflict | 626 |
| Resolved conflict | 0 |
| Total | 1,656 |

Every one of the 626 conflicts remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank final proposed type, and blank adjudicator. There was no automatic conflict resolution. Unselected rows retain their primary triple; agreement rows take the audit triple and reason.

Audit-decision counts are: exclude 606; applied seed 538; diagnostic/correction lead 129; method-source lead 170; simulation/mechanistic lead 212; and one explicit primary-record uncertainty. The audit produced no unsupported shortcut.

`screening_audit.csv` SHA256: `d4540fb9bbe5f9150d72db1a1d0f35e707a4739dfad482964c39eb0cf7e2f010`.

Across both waves, the authoritative formal audit contains 2,542 freshly audited rows: W1 1,656 and W2 886. It reached 1,644 agreements and 898 open conflicts. The complete ordered selection SHA256 is `5e01b9a19c0e83d0a439637d473a33b834da57fdf408f1c3ff5935e76f42cbd1`; combined accepted audit-decision SHA256 is `e99327ffa175e642ec60ea30c65a253c35fac9f8cc93f4cf4260e1fdd5c74311`; formal-audit proof-ledger SHA256 is `2f7106e5cd6feee14f7f4a40b14cab9aad61d4f6e94ea5d4bc4b5ff84660175f`. Exact per-row and per-session provenance is recorded in `TASK_5_THIRD_REPAIR_PROVENANCE.md`.

Both commands passed after live assembly:

```text
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
```

All authoritative audit results come from the exhaustive third-repair union selection and the fresh full recomputation. No prior audit row or session was reused.
