# Task 8 External Release-Contract Amendment Independent Review

## Current verdict

`PASS — 0 Critical, 0 Important, 0 Minor`

- Spec compliance: PASS — 0 Critical, 0 Important, 0 Minor
- Task quality: PASS — 0 Critical, 0 Important, 0 Minor
- Complete review range: `352588c0059122de7385498c6d17f8fcdbd495f3..d0d873abe08256184bd5028fde8cf1f2f020b576`
- Initial amendment: `2927eae1b01e634bb18e007f6914a998e167e8d9`
- Repair and reviewed head: `d0d873abe08256184bd5028fde8cf1f2f020b576`
- Review package: `07_reviews/discovery_tasks/TASK_8_EXTERNAL_CONTRACT_AMENDMENT_REVIEW_PACKAGE.md`
- Exact diff SHA256: `9e621bab349900b5847220e02acc87452eddc19aef68dec8496ad5f9838e03df`

## Closed findings

1. **Important — untracked JSON absent from the pre-commit diff gate.** Closed by exact order-independent pre-stage status validation, staging only the three repair paths, and exact cached path/status/SHA/whitespace/content review before commit.
2. **Minor — release-contract JSON and executable constants not automatically bound.** Closed by byte-locking the exact JSON, including its trailing newline, to SHA256 `6f7e7f71d300f820ef46e7ffc98bd54aa57061e566f187362f1c44ab07e05422` at creation, full-gate, and cached-blob checkpoints. An amended-gate PASS cannot compensate for a JSON SHA mismatch.

## Passing evidence

- Complete range changes exactly `00_governance/DECISION_LOG.md` and the new amendment plan; the repair commit changes only the plan.
- `DEC-20260722-010` is the first available decision ID; existing `DEC-20260722-009` remains unchanged.
- Original plan, baseline, validator, approved design, bootstrap plan, and frozen seed are unchanged.
- The amended gate produced the exact 14-line PASS output.
- Ten amended-gate negative probes and three JSON-drift probes blocked.
- The legacy validator remained exit `1` with exactly `DISCOVERY FAIL` and `- external filtered status mismatch`; it was not relabelled PASS.
- Seven Bash blocks and the Step 7 set logic passed syntax/logic review.
- Library validator and complete-range whitespace checks passed.
- `Surveillance_AMR` before/after snapshots were byte-identical; the review made no external write.

The amendment is accepted. The original Task 8 implementer may now create the exact release-contract JSON, update the verification report and handoff, run every amended and original Task 8 gate, and commit `repair Task 8 external release contract`. The same Task 8 reviewer must then re-review the complete original Task 8 range before whole-branch review may begin.
