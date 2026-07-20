# Wave 1 independent screening audit

Date: 2026-07-20

## Selection

The approved plan's primary-family strata and the production validator's full-`preliminary_families` strata were both honored. The selected set is the union of:

1. the plan formula by primary decision, reason code, and precedence-selected primary family;
2. the validator formula by primary decision, reason code, and full family string;
3. 100% of primary uncertain and `X_NOT_INFECTIOUS_TRANSFERABLE` rows; and
4. all members of every possible-title-duplicate group.

Plan strata numbered 60 and required 1,442 keys. Validator strata numbered 91 and required 1,504 keys. Their formula union contained 1,507 keys. Adding 52 otherwise unselected possible-duplicate rows produced 1,559 audited keys in 32 batches. The ordered audit-key-list SHA256 is `8bb3b09d236b1e964ebaa4845e0435225068d348f7de3fd7afd547c7e99d0b39`.

The set includes all 41 primary uncertain rows, all 543 `X_NOT_INFECTIOUS_TRANSFERABLE` rows, and all 81 rows in 40 possible-duplicate groups. Each audit batch used a fresh read-only `gpt-5.6-sol` high-reasoning session with a reviewer identity distinct from the primary batch reviewer. Primary decisions were hidden.

## Outcome

| Audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 912 |
| Open conflict | 647 |
| Resolved conflict | 0 |
| Total | 1,559 |

Every one of the 647 conflicts remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank final proposed type, and blank adjudicator. There was no automatic conflict resolution. Unselected rows retain their primary triple; agreement rows take the audit triple and reason.

Audit-decision counts were: exclude 572; applied seed 517; diagnostic/correction lead 83; method-source lead 138; simulation/mechanistic lead 249. The audit produced no unsupported `uncertain` shortcut.

`screening_audit.csv` SHA256: `b681689d94cba02972081c854624f3422b61d25f383f804ef0dc49265b5e081a`.

Both commands passed after live assembly:

```text
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
```

The first audit attempt had incorrectly selected only the validator's refined strata. Its three just-started sessions were stopped before import and contributed zero rows; the invalid fine-only materials are preserved in the ignored execution record. All reported audit results come from the corrected union selection.
