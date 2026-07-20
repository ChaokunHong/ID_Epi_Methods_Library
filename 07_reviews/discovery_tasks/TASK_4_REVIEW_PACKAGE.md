# Task 4 Review Package

## Review range

- Task: 4 — execute and freeze Wave 1's complete 12-cell PubMed corpus
- Base SHA: `a7fa175944173ff6f1f17cfbfe767ee47e7a3375`
- Implementation SHA: `4f76f6692f62ec94591628b5b78edd8d1fe03017`
- Self-review fix SHA: `4b7248a98bb1d23e582d79fe6d6f1d8b2e68fe85`
- Formal-review fix SHA: `1f1b54169018b2d24353554eb1dc937d7d0b1cd2` (`fix Wave 1 compilation and transport handling`)
- Exact re-reviewed head: `1f1b54169018b2d24353554eb1dc937d7d0b1cd2`
- Exact diff package: `.superpowers/sdd/review-a7fa175..4b7248a.diff`
- Diff package SHA256: `43a463423763655667587bb86794c0b9e700b4701de7a7f8189a5832b8842795`
- Re-review diff package: `.superpowers/sdd/review-a7fa175..1f1b541.diff`
- Re-review diff SHA256: `bdd1f53e3835558b90001386857f5bc6091a384c7199a8b79e09516082df50c3`
- Implementer report: `.superpowers/sdd/task-4-report.md`

## Changed paths and approved correction

The implementation/self-review range creates 73 paths, all beneath `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/`:

- 12 ESearch JSON responses;
- 44 EFetch XML pages;
- 12 search logs;
- `RUN_RECEIPT.json`, `MANIFEST_SHA256.json`, `compiled_candidates_raw.csv`, and `COUNT_RECONCILIATION.txt`;
- one owner-approved local `.gitattributes` containing only `raw/*.xml -diff` plus an explanatory comment.

The owner explicitly approved the `.gitattributes` correction after NCBI raw XML was found to contain source-supplied trailing whitespace. The 44 raw pages were not rewritten. The attribute is itself manifested and limits Git diff presentation only for the immutable raw XML; SHA, regular-file/path ownership, XML parsing, count reconciliation, and validators remain mandatory.

The complete fixed range contains 75 paths: those 73 Wave 1 paths plus `00_governance/scripts/discovery_search.py` and `00_governance/tests/test_discovery_search.py`, which the first formal review required to fix upstream compilation and transport defects. The formal fix changes only those two code/test paths plus the derived compiled CSV and its manifest entry; raw responses, receipt, independent reconciliation, and all search logs remain byte-identical to `4b7248a98bb1d23e582d79fe6d6f1d8b2e68fe85`.

## Live execution results

- Execution date/timezone: `2026-07-20T13:44:01.058821+08:00`, `Asia/Shanghai`.
- API key: none.
- Root cells: 12; leaf cells: 12; split parents: 0.
- ESearch responses: 12; EFetch pages: 44.
- Source-reported records: 7,551; retrieved direct PubMed records: 7,551.
- Direct record types: 7,547 `PubmedArticle`; 4 `PubmedBookArticle`.
- Deterministically compiled unique candidates: 7,146.
- Candidate keys: all 7,146 are `PMID:*`.
- Deduplication basis: 7,145 `pmid`; one `doi`.
- Title-only possible duplicates: 81 rows in 40 groups; none auto-deleted.
- Raw bytes: 160,394,734.
- Manifest entries: 71; independent root-agent rehash failures: none.
- Independent reconciliation final line: `ALL LEAF AND ROOT COUNTS MATCH`.

Root source/retrieved counts are: FAMILY CAUSAL 922; EVIDENCE 146; FORECASTING 1,251; SIMULATION 1,316; SPATIAL 1,416; SURVEILLANCE 980; VENUE CAUSAL 279; EVIDENCE 155; FORECASTING 395; SIMULATION 255; SPATIAL 216; SURVEILLANCE 220. Every pair reconciles exactly.

## Configuration and boundary receipts

- Protocol SHA256: `e3b1013862e2f18314702cbf1e1e0e5c2c6b9e0d2b78113b23b9e65e2ccb20df`.
- Query configuration SHA256: `7e7e6bd7eeb4704e43ffa30e3c002a4ce5d044b5ac0c722fce7dd5d34f24a3e1`.
- Journal registry SHA256: `ef65e25ccb8ef1feb7220fc82c476bf2322c7e78db8fd1c05d463347aa688cc8`.
- Approved plan SHA256 remains `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`.
- Design SHA256 remains `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`.
- Seed SHA256 remains `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`.
- `verify-external-boundary`: `DISCOVERY PASS`; no `Surveillance_AMR` write was authorized or made.

## Retry and deviation evidence

Three NCBI chunked transfers ended with `http.client.IncompleteRead`: two attempts for FAMILY-SPATIAL and one for VENUE-SPATIAL. The same frozen command safely resumed. Completed roots were revalidated and skipped; each incomplete root was cleaned by prefix and restarted with a fresh history. Final raw/manifest/receipt ownership is closed and contains no temporary/orphan path.

At the initial reviewed head the run CLI did not catch `IncompleteRead`, so those attempts printed Python tracebacks rather than a stable application error. The first formal review classified this as Important. The formal-review fix now catches HTTP stream exceptions as stable execution errors while preserving the same atomic cleanup and fresh-history resume behavior; the reviewer must independently verify this correction.

The first required-subject commit was created by a shell command that continued after the initial whitespace failure. The second commit normalizes only the derived CSV from CRLF to LF, updates its manifest SHA, and adds the approved narrow attribute. The two-commit audit trail is intentionally preserved.

## Verification evidence

- Discovery tests: 86/86 PASS, independently rerun by the root agent.
- Post-fix discovery tests: 89/89 PASS, independently rerun by the root agent.
- Legacy validator tests: 25/25 PASS, independently rerun by the root agent.
- Wave verifier: `DISCOVERY PASS`.
- Repository validator: `VALIDATION PASS`.
- External-boundary validator: `DISCOVERY PASS`.
- Complete-range `git diff --check`: PASS.
- Worktree at reviewed head: clean before this root-owned review package.
- Exact complete-range changed-path assertion: 75 paths; 73 Wave 1 paths plus the two formally authorized upstream code/test paths.

## Independent review checklist

The reviewer must check both specification compliance and task quality. At minimum:

1. recompute the 12 configured roots and compare exact IDs/family/lane/query/date/source to the receipt;
2. independently parse all ESearch JSON and EFetch XML without importing the production count function, including both direct PubMed record types;
3. prove receipt, manifest, and filesystem raw sets are equal, every SHA matches, no temporary/symlink/extra path exists, and all page/root counts reconcile without counting parents;
4. independently regenerate or compare the canonical compiled table, candidate keys, provenance, row SHA, identifier-only deduplication, and title-only grouping;
5. inspect all 12 search logs for exact query/tree/count/page/timestamp/deviation and `Screening status: not started`;
6. confirm no screening/evidence/verified claim entered the raw CSV and no Task 5 artifact was created;
7. assess the owner-approved `.gitattributes` narrowly and prove raw bytes remain protected by manifest/count validation;
8. assess the three historical retries and independently confirm the fixed `IncompleteRead` containment, atomic cleanup, no traceback, and fresh-history resume behavior;
9. verify locked configuration SHAs, external boundary, and the exact complete-range scope of 73 Wave 1 paths plus the two formally authorized upstream code/test paths.

Any Critical or Important finding requires a focused fix by the original implementation agent and a full-range re-review.

## First formal review

The independent reviewer returned `NEEDS FIXES — 0 Critical, 3 Important, 1 Minor` for `a7fa175944173ff6f1f17cfbfe767ee47e7a3375..4b7248a98bb1d23e582d79fe6d6f1d8b2e68fe85`.

1. The production PubMed parser reads only `ArticleTitle`. Four real `PubmedBookArticle` records use `BookDocument/Book/BookTitle`, leaving their compiled titles empty and preventing Task 5 title-level semantic screening. The fix must use a real BookTitle fallback and, when present, `CollectionTitle` as a container fallback without inventing a journal.
2. The production compiled-CSV renderer uses the default CRLF terminator, while the frozen table was mechanically normalized to LF. Re-running the documented `compile` command changes SHA `77c22f...` back to `ddd56d...`, so the frozen derived artifact is not byte-reproducible. All production CSV writers must explicitly use `lineterminator="\n"`, with a byte-level idempotence regression test.
3. `http.client.IncompleteRead`/related HTTP stream exceptions escape the CLI instead of becoming a stable `DISCOVERY FAIL`. Atomic cleanup and fresh-history resume were independently proven safe, but the failure occurred three times in the live run and the same client will execute Waves 2/3. The fix must contain the exception, preserve cleanup/resume behavior, and prove no traceback.

The Minor finding corrects this package and the implementation report: all 7,146 candidate keys are `PMID:*`; `deduplication_basis` is 7,145 `pmid` and one `doi`. The original implementation agent must add focused failing tests for the three Important findings, fix the production code, recompile only the derived CSV and update its manifest SHA without changing any raw response, rerun complete verification, and commit a focused fix. The same reviewer must re-review the full base-to-fixed-head range.

## First-review fix cycle

The original implementation agent added four focused tests. Against `4b7248a98bb1d23e582d79fe6d6f1d8b2e68fe85`, two failed, one raised the expected escaping `IncompleteRead`, and one existing transport-control test passed. After the minimal fix all four passed. Commit `1f1b54169018b2d24353554eb1dc937d7d0b1cd2`:

1. adds a realistic `PubmedBookArticle/BookDocument/Book/BookTitle` fallback and uses only an actual `CollectionTitle` for the container field;
2. sets LF terminators in both production CSV writers and proves repeated production compile is byte/SHA idempotent;
3. catches HTTP stream exceptions as stable execution errors and proves cleanup, no traceback, stale-root removal, fresh-history resume, and closed ownership.

The fixed production compiler was run once. It changed only four live book rows and the compiled manifest entry. All four book PMIDs now have nonblank titles; three use real `CollectionTitle` values and PMID `33030851` correctly retains a blank container. The new compiled SHA256 is `70cc6adb6ce40ed5c678ba0901cf4a23b78f64e5839304cd89002a7b19c46ec4`, contains no carriage return, and remains unchanged after a second production compile.

The root agent independently proved all 56 raw files are byte-identical to the pre-fix head, reran 89/89 discovery tests and 25/25 legacy tests, and obtained PASS from Wave, Library, external-boundary, bytecode, and complete-range whitespace checks. The same reviewer must now re-review `a7fa175944173ff6f1f17cfbfe767ee47e7a3375..1f1b54169018b2d24353554eb1dc937d7d0b1cd2`, verify all three Important findings and the statistics Minor are closed, and scan for regressions.

## Final independent review conclusion

The same independent reviewer completed the fixed full-range review and returned `PASS — 0 Critical, 0 Important, 0 Minor` for `a7fa175944173ff6f1f17cfbfe767ee47e7a3375..1f1b54169018b2d24353554eb1dc937d7d0b1cd2`. The reviewer independently rebuilt the complete compiled table from raw, ran production compile twice with identical bytes/SHA/manifest, checked the four live BookTitle records and real CollectionTitle mappings, reproduced stable `IncompleteRead` containment plus fresh-history resume, proved all 56 raw files unchanged, and reran 89/89 discovery tests, 25/25 legacy tests, and all validators. The documentation Minor was then corrected and rechecked without changing tracked code or artifacts.
