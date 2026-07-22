# Task 8 Independent Review

## Current verdict

`NEEDS FIXES / ACK withheld — 0 Critical, 1 Important, 0 Minor`

- Spec compliance: NEEDS FIXES — one Important release-gate failure
- Task quality: PASS — 0 Critical, 0 Important, 0 Minor
- Review range: `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52..70e5820dadf073cea19cc4fe7eb3f1bca377b269`
- Reviewed head: `70e5820dadf073cea19cc4fe7eb3f1bca377b269`
- Implementation commit: `70e5820dadf073cea19cc4fe7eb3f1bca377b269`
- Review package: `07_reviews/discovery_tasks/TASK_8_REVIEW_PACKAGE.md`
- Exact diff package: `.superpowers/sdd/review-140b7f2..70e5820.diff`
- Exact diff SHA256: `3f899fc3448b156501b9e198ad3850bcef5111b5f4a977f1227aa6bd31f95878`

## Important finding

### External release gate is not satisfied

The approved Task 8 plan requires all validators to pass and requires the live filtered `Surveillance_AMR` status to equal the phase-start receipt. Fresh independent execution of `verify-external-boundary` returned exit `1`, `DISCOVERY FAIL`, and exactly one diagnostic: `external filtered status mismatch`.

The frozen phase-start pointer-filtered default status is 16 lines with SHA256 `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e`. The live pointer-filtered default status is 17 lines with SHA256 `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd`. The additional state is the already-documented owner-owned untracked GBD directory.

This is Important rather than Critical because the Library content, calculations, verification report, and claim boundaries are correct and the failure is reported honestly. It nevertheless blocks the explicit release gate, so Task 8 cannot receive PASS and whole-branch review, merge, and push cannot begin under the current approved contract.

The finding cannot be repaired by editing `07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md` or `HANDOFF.md`. The plan forbids writing to `Surveillance_AMR`, and neither the frozen baseline nor validator may be changed merely to make the gate green.

## Closure conditions

One of the following owner-controlled conditions is required before re-review:

1. A separately authorized and independently reviewed external operation restores the exact phase-start boundary so `verify-external-boundary` returns exit `0` / `DISCOVERY PASS`, including the 16-line pointer-filtered status and SHA256 `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e`, while source HEAD, pointer/index, and seed-source states continue to match; then rerun the complete Task 8 gate.
2. The owner explicitly approves an independently reviewed plan revision that replaces the current external release contract with a new contract; then rerun the complete Task 8 gate and independent review against that revision.

Do not close the finding by silently deleting owner-owned GBD material, editing the frozen baseline, weakening the validator, or relabeling the failed command as PASS.

## Passing checks

- Exact implementation range: one commit with subject `verify broad methods discovery phase`
- Exact tracked scope: added verification report and modified handoff only
- Executed-ID ledger: 741/741 rows independently matched
- Manifest integrity: 1,594/1,594 entries rehashed without mismatch
- Wave receipts and tables: 12 Wave 1 roots, six Wave 2 queries, 723 Wave 3 queries, 7,146 / 3,571 screened rows, 634 lineage candidates, and 620 lineage-ledger rows
- Registries: 7,779 papers, 277 methods, and eight deferred normalized registries header-only
- Library tests: 25/25 PASS
- Discovery tests: 95/95 PASS
- `validate-config`, `verify-all`, Library validator, and exact-range `git diff --check`: PASS
- Required discovery-versus-verified claim boundary, immutable hashes, seed byte comparison, remote baseline, deferred work, and next-plan statement: PASS
- Reviewed worktree: clean

The reviewer made no Library or `Surveillance_AMR` write. Task 8 remains blocked at its independent review gate pending one of the explicit owner-controlled closure conditions.
