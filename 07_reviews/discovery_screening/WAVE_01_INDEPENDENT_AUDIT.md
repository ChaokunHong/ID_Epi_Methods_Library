# Wave 1 independent screening audit

Date: 2026-07-20

## Selection

The approved plan's primary-family strata and the production validator's full-`preliminary_families` strata were both honored. The selected set is the union of:

1. the plan formula by primary decision, reason code, and precedence-selected primary family;
2. the validator formula by primary decision, reason code, and full family string;
3. 100% of primary uncertain and `X_NOT_INFECTIOUS_TRANSFERABLE` rows; and
4. all members of every possible-title-duplicate group.

Plan strata number 60 and require 1,451 keys. Validator strata number 92 and require 1,514 keys. Their formula union contains 1,517 keys. Adding 44 otherwise unselected possible-duplicate rows produces 1,561 audited keys in 32 batches. The ordered audit-key-list SHA256 is `4b82b712813c59ba073e9e4c4a99dd82c2e70329bd8598696d0938b84f674f39`.

The set includes all 41 primary uncertain rows, all 558 `X_NOT_INFECTIOUS_TRANSFERABLE` rows, and all 81 rows in 40 possible-duplicate groups. The recomputation preserved 1,384 prior independent rows only where source SHA, complete primary triple, primary reviewer, selection membership, reviewer independence, and semantic premise were unchanged. One hundred sixty-six selected scope-reread rows use the fully independent Reader B decision, and 11 newly selected rows use fresh read-only Codex CLI session `019f81fb-b235-74f2-9743-40be040cbd68`. Every audit reviewer identity differs from the corresponding primary reviewer; primary decisions were hidden from Reader B and the fresh CLI session.

## Outcome

| Audit outcome | Count |
|---|---:|
| Complete decision/reason/type agreement | 982 |
| Open conflict | 579 |
| Resolved conflict | 0 |
| Total | 1,561 |

Every one of the 579 conflicts remains `conflict_status=open` with `final_decision=uncertain_retrieve_primary`, `final_reason_code=U_PRIMARY_RECORD_NEEDED`, blank final proposed type, and blank adjudicator. There was no automatic conflict resolution. Unselected rows retain their primary triple; agreement rows take the audit triple and reason.

Audit-decision counts are: exclude 615; applied seed 504; diagnostic/correction lead 92; method-source lead 127; simulation/mechanistic lead 223. The audit produced no unsupported `uncertain` shortcut.

`screening_audit.csv` SHA256: `2d22f008b30b35206f75abc92222d55b2881acce35fd7fda5bdd681f0fd8a5a5`.

Across both waves, the recomputed formal audit contains 2,391 rows: 2,130 legally reused unchanged independent rows, 241 Reader B scope-reread rows, and 20 newly selected rows independently read in fresh session `019f81fb-b235-74f2-9743-40be040cbd68`. The 20-row response SHA256 is `64f6fdf2902892c846f319ebd2e8041779146dc715c7897a190c1b44e0865a0b`; the session receipt SHA256 is `cb8b66e128ed7bd8bb8c4d29f85b1f68db93f1600596da7a68f2e9873d63b8d2`. Exact per-row source proof and per-session provenance are recorded in `TASK_5_SECOND_REPAIR_PROVENANCE.md`.

Both commands passed after live assembly:

```text
python3 00_governance/scripts/discovery_search.py validate-screening --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
python3 00_governance/scripts/discovery_search.py validate-audit --run-dir .../wave_01_frozen_queries
DISCOVERY PASS
```

All reported audit results come from the corrected union selection and the full second-repair recomputation. No changed-primary audit row was allowed to reuse an audit with a changed semantic premise.
