# Wave 1 independent screening audit

Date: 2026-07-20

## Selection

The approved plan's primary-family strata and the production validator's full-`preliminary_families` strata were both honored. The selected set is the union of:

1. the plan formula by primary decision, reason code, and precedence-selected primary family;
2. the validator formula by primary decision, reason code, and full family string;
3. 100% of primary uncertain and `X_NOT_INFECTIOUS_TRANSFERABLE` rows; and
4. all members of every possible-title-duplicate group.

Plan strata number 60 and require 1,436 keys. Validator strata number 91 and require 1,499 keys. Their formula union contains 1,502 keys. Adding 50 otherwise unselected possible-duplicate rows produces 1,552 audited keys in 32 batches. The ordered audit-key-list SHA256 is `595995658afa924808305f7ed9567abd0623f43025ce4891b112401133a18aa7`.

The set includes all 41 primary uncertain rows, all 541 `X_NOT_INFECTIOUS_TRANSFERABLE` rows, and all 81 rows in 40 possible-duplicate groups. The recomputation preserved 1,516 prior independent rows only where source SHA, complete primary triple, primary reviewer, selection membership, and semantic premise were unchanged. Thirty-three selected scope-reread rows use the fully independent Reader B decision, and three newly selected rows use a fresh read-only Codex CLI session. Every audit reviewer identity differs from the corresponding primary reviewer; primary decisions were hidden from Reader B and the fresh CLI session.

## Outcome

| Audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 932 |
| Open conflict | 620 |
| Resolved conflict | 0 |
| Total | 1,552 |

Every one of the 620 conflicts remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank final proposed type, and blank adjudicator. There was no automatic conflict resolution. Unselected rows retain their primary triple; agreement rows take the audit triple and reason.

Audit-decision counts are: exclude 583; applied seed 512; diagnostic/correction lead 83; method-source lead 134; simulation/mechanistic lead 240. The audit produced no unsupported `uncertain` shortcut.

`screening_audit.csv` SHA256: `1a4d0fd8706c2866e7355fe7fc254581de84a37bc3a509d9f27f471f8191f54f`.

Across both waves, the recomputed formal audit contains 2,370 rows: 2,318 legally reused unchanged independent rows, 47 Reader B scope-reread rows, and five newly selected rows independently read in the fresh session `019f7f90-90d4-7a83-98ff-be31b3067bd9`. The five-row response SHA256 is `6a4e279be1de482234a17aa9130a7d36305ab1157f567b03172d308ed55d4ade`; the session receipt SHA256 is `a0617df7c9b4c5d58ec4970030352eb4ae90a9ca1ba1bae88a42ee6192c36c18`. A briefly dispatched unrelated Task 3 follow-up was interrupted before response and contributed zero rows.

Both commands passed after live assembly:

```text
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
```

The first audit attempt had incorrectly selected only the validator's refined strata. Its three just-started sessions were stopped before import and contributed zero rows; the invalid fine-only materials are preserved in the ignored execution record. All reported audit results come from the corrected union selection and its full post-repair recomputation.
