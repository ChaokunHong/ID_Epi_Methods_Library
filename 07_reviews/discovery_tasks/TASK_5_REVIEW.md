# Task 5 Independent Review

## Current verdict

`NEEDS FIXES — 0 Critical, 3 Important, 1 Minor`

- Spec compliance: NEEDS FIXES
- Task quality: NEEDS FIXES
- Critical: 0
- Important: 3
- Minor: 1
- Review range: `961cdf859ad13f94abc1904d3b5bd8ed12913ae6..29ddc3b4f606c11d191e9a16620ac5ba817f19c2`
- Reviewed head: `29ddc3b4f606c11d191e9a16620ac5ba817f19c2`
- Implementation commit: `bf1a8d27a2eab227901f04af5d3b029799edf767` (`screen broad methods discovery records`)
- Repair commits: `b167cb6fe583c4f3dce3a5e0dc22d3ae2a54d5a9`, `29ddc3b4f606c11d191e9a16620ac5ba817f19c2`
- Exact diff package: `.superpowers/sdd/review-961cdf8..29ddc3b.diff`
- Exact diff SHA256: `b220ef81a45fc27a472341994e1567c4cbdbe3dbb8acdea562a1a83ec868186d`
- Review package SHA256: `1a10cf96a1fa6dadf40c43526b0e7d1bf1ee80b756951725d7b694563c11b969`

## Important findings

1. The second-repair locator remains incomplete. Seven retained records outside its 1,465-key universe show the same therapeutic, host-physiology, molecular, or non-epidemiological method drift: `PMID:25450804`, `PMID:26014946`, `PMID:28358222`, `PMID:30221005`, `PMID:24731529`, `PMID:33024578`, and `PMID:28854802`. The next repair must stop relying on another keyword-bounded analogue locator: every still-retained Wave 1/2 inclusion must receive a complete independent scope reread, with blind adjudication of disagreements and no keyword-made decision.
2. `PMID:21372330` is a distinct Retraction Notice and has correctly been separated from retracted article `PMID:20826636`, but it remains `exclude / X_WRONG_RECORD_TYPE`. Because it supplies correction/retraction information, the protocol requires a correction lead or an honest uncertain decision if the available metadata are insufficient.
3. Root continuity state is stale. `HANDOFF.md` and `07_reviews/discovery_tasks/EXECUTION_LEDGER.md` still stop at `b167cb6` and the previous review. This is root orchestration scope, not implementer scope, and must be corrected before the next exact-head review.

## Minor finding

The three archived rejected-attempt receipts retain nine embedded `events_path`/`stderr_path`/`response_path` fields pointing to the accepted retry locations. The archived bytes exist and match the recorded hashes, and the tracked provenance table points to the correct archives, so no rejected row was adopted. Correct the embedded paths and recompute dependent provenance hashes during the mandatory repair.

## Findings already closed

- `PMID:20826636` and `PMID:21372330` are no longer falsely collapsed; their distinct identities and DOIs are preserved.
- `PMID:33083025`, `PMID:38776389`, and `PMID:22439282` are now A/B-agreed `exclude / X_DESCRIPTIVE_ONLY` rows.
- The nonexistent adjudicator alias count is zero; 45 accepted and three rejected UUID-backed sessions were found in real Codex session metadata.
- The 1,465-key second-repair universe, 40 reader sessions, 178 conflicts, 195-key blind-adjudication union, and 2,391-row formal audit all reconstruct exactly.

## Independent verification

The reviewer reran 89 discovery tests and 25 Library tests, plus 15 subtests; all passed. Configuration, Wave 1 verify/screen/audit, Wave 2 verify/screen/audit, and external-boundary checks produced eight `DISCOVERY PASS` results. The Library validator passed. Both manifests rehashed exactly, the global index reconstructed to 10,525 unique keys and 192 overlaps with SHA256 `83d320b315f3a26e83677725c2987a2ca6db401f9fd8c3f8a535ba4991949f16`, both whitespace checks passed, and the seed copy remained byte-identical.

Task 6 remains blocked. Any Critical or Important finding at the next fixed head requires another repair and full-range re-review.
