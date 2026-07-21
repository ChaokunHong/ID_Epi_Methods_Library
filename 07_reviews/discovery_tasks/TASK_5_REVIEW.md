# Task 5 Independent Review

## Current verdict

`NEEDS FIXES — 0 Critical, 1 Important, 0 Minor`

- Spec compliance: NEEDS FIXES — 0 Critical, 1 Important, 0 Minor
- Task quality: PASS — 0 Critical, 0 Important, 0 Minor
- Review range: `961cdf859ad13f94abc1904d3b5bd8ed12913ae6..9d89eb7656dab1acd576cb543070cb3b6dd5eb20`
- Reviewed head: `9d89eb7656dab1acd576cb543070cb3b6dd5eb20`
- Implementation commit: `bf1a8d27a2eab227901f04af5d3b029799edf767`
- Repair commits: `b167cb6fe583c4f3dce3a5e0dc22d3ae2a54d5a9`, `29ddc3b4f606c11d191e9a16620ac5ba817f19c2`, `9d89eb7656dab1acd576cb543070cb3b6dd5eb20`
- Exact diff package: `.superpowers/sdd/review-961cdf8..9d89eb7.diff`
- Exact diff SHA256: `756aa982a3da4eec7d51a434a4e6040fba6de56e37db879278d671f66b20c36e`
- Review package SHA256 at dispatch: `d9a9c6786a8c65d2dfd864f03ec6a834e962d7768e8a30ed12b4b409b5232113`

## Important finding

Blind adjudication falsely excludes eligible reproducibility and method-comparison leads as `exclude / X_DESCRIPTIVE_ONLY`.

Both fresh independent readers included each of the following clear discovery leads, but the blind adjudicator subsequently excluded them:

- `PMID:41665488`: explicitly benchmarks WGS workflows, MLST/cgMLST, SNP profiling, and AMR prediction for outbreak genomic epidemiology.
- `PMID:32928108`
- `PMID:38823290`
- `PMID:40883247`
- `PMID:40893944`

These outcomes conflict with the eligible discovery roles in the protocol and the approved spatial/transmission and simulation/methodological-evaluation families. The reviewer independently joined all fresh-reader and adjudication outputs and found 48 rows with the same double-include then blind-exclude pattern. `PMID:41540427` is more borderline and is not one of the five unambiguous examples, but it belongs in the required re-review set.

## Required repair

1. Freshly and independently re-adjudicate all 48 double-include then blind-exclude rows against the approved design and protocol.
2. Correct at least the five unambiguous records above; do not use their identities as an automatic rule for the other rows.
3. Regenerate affected primary batches, screened outputs, deterministic audit, global index, manifests, and durable provenance while preserving identifier-only deduplication and all immutable raw inputs.
4. Rerun the complete test, validator, boundary, seed, and diff suite and submit the complete fixed range for another independent review.

## Prior-finding closure

| Prior finding | Status at `9d89eb7` |
|---|---|
| Incomplete semantic universe | CLOSED — exact 8,984-row universe independently reconstructed |
| `PMID:21372330` Retraction Notice | CLOSED — distinct correction lead |
| Rejected-receipt stale paths | CLOSED — all referenced paths and SHAs resolve |
| Stale continuity | CLOSED in root-owned review/ledger/handoff files |

## Independent verification

- Exact 8,984-row universe, 2 x 8,984 reader coverage, 7,985 agreements, 999 blind conflicts, and final semantic ledger reconstructed.
- 294 final accepted sessions and 2,058 referenced artifacts independently verified against local immutable rollout evidence; session UUID, cwd, branch, parent, model, effort, sandbox, prompt, and response matched.
- Corrected audit reconstructed to W1 1,656 plus W2 886 = 2,542 rows; 1,644 agreements, 898 open conflicts, and zero resolved conflicts.
- All 192 cross-wave identifier overlaps and the 10,525-key global index reconstructed.
- Discovery tests: 89 passed plus five subtests.
- Library tests: 25 passed plus ten subtests.
- Configuration, both wave verification/screening/audit checks, Library validator, external-boundary validator, both diff checks, and seed byte comparison: PASS.
- Seed SHA256: `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`.
- `Surveillance_AMR` remained at HEAD `eb5d15656b8fe69a8359705c80125d695a1c0782`; default status SHA256 `4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c`, pointer-filtered SHA256 `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e`.

Task 6 remains blocked. The same Task 5 implementation agent must perform the focused repair, and this independent reviewer must then re-review the complete fixed range.
