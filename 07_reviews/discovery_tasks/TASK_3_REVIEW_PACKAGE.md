# Task 3 Review Package

## Review range

- Task: 3 — deterministic PubMed retrieval and metadata compilation
- Base SHA: `179059084eb655f7dc5ad6ac0bbfb8da67c01c0c`
- Implementation SHA: `f8de39eb063ab0a436d8235c2c0a41212ca09956`
- Fix SHA: `3bae05606f74a2ac45787624fbce51029f3b5e5a` (`close discovery retrieval validation gaps`)
- Second fix SHA: `888cc2775315af40f317356488191c146071e53e` (`enforce closed discovery artifact ownership`)
- Exact re-reviewed head: `888cc2775315af40f317356488191c146071e53e`
- SDD diff package: `.superpowers/sdd/review-1790590..f8de39e.diff`
- Diff package SHA256: `a14b60a245595bea4b04d92d106a4c771c30213fb5a32e4bab0b85768cf71dbf`
- Re-review diff package: `.superpowers/sdd/review-1790590..3bae056.diff`
- Re-review diff SHA256: `288e1940abf2f77f430c5794c093776561158d7dd7797ea1284f17960387963e`
- Second re-review diff package: `.superpowers/sdd/review-1790590..888cc27.diff`
- Second re-review diff SHA256: `a706d159ac1504233f491df39ac4e15fb25eb03a0724116a91a07be48479c581`
- Implementer report: `.superpowers/sdd/task-3-report.md`

## Changed paths

- Modified `00_governance/scripts/discovery_search.py` (+2139/-22)
- Modified `00_governance/tests/test_discovery_search.py` (+1793/-22)

No other path is present in the implementation range.

## TDD and verification evidence

- Initial focused tests failed because `execute_pubmed_cell` and `compile_pubmed_candidates` did not exist.
- Twelve later RED/GREEN cycles covered recursive split, resume, Crossref/Wave 2, heterogeneous lineage, CLI execution, semantic receipt revalidation, compiler manifest ownership, lineage partial preservation, cross-root pacing, Wave 2 query identity/semantics, and raw/receipt recomputation.
- Final discovery suite: 77/77 PASS.
- Post-review-fix discovery suite: 82/82 PASS.
- Post-second-review-fix discovery suite: 86/86 PASS.
- Final legacy validator suite: 25/25 PASS.
- `validate-config`: `DISCOVERY PASS`.
- repository validator: `VALIDATION PASS`.
- external-boundary validator: `DISCOVERY PASS`.
- Python bytecode compilation: PASS.
- `git diff --check`: PASS.
- Changed-path assertion: exactly the two Task 3 paths.
- Test suite uses injected fake openers; no live PubMed/Crossref call was made.

## Functional contract under review

The implementation adds atomic PubMed ESearch/EFetch execution, complete recursive date splitting, manifest-backed page/count verification, deterministic resume, PMID/DOI compilation and title-only duplicate grouping, bounded Crossref candidates without automatic decisions, Wave 2 registry execution including the strict empty-wave state, heterogeneous Wave 3 lineage execution and candidate tables, lineage audit/ledger validation, CLI `run`/`run-wave`/`run-lineage`/`compile`, and aggregate `verify-all` composition.

## Review checklist

The independent reviewer must evaluate both specification compliance and task quality over the exact diff. At minimum, inspect:

1. exact NCBI/Crossref request parameters, URL encoding, pacing, and API-key non-persistence;
2. atomic file publication and cleanup on every stable failure path;
3. ESearch parent/leaf manifestation, year-month-day interval splitting, unsplittable-day failure, leaf page/count reconciliation, and resume revalidation;
4. XML extraction for both direct record types, deterministic candidate keys/row hashes, only PMID/DOI auto-deduplication, and title-only grouping without deletion;
5. Wave 2 exact registry/family/query/date rules, executed-only dispatch, and strict all-no-expansion artifacts;
6. Wave 3 1–3 query/source dispatch, overbroad PubMed pre-EFetch failure, source-conditional receipts and two candidate tables;
7. complete independent lineage audit, conflict, provenance, raw-response recomputation, selected-key, URL, and ledger closure rules;
8. CLI error containment, `verify-all` composition, absence of real network calls in tests, and absence of unrelated scope.

Because the production module grows substantially, assess internal cohesion and defect risk directly rather than treating test count as sufficient. Any Critical or Important finding requires correction by the original implementation agent and a full-range re-review.

## Known deferred work

- Live PubMed execution belongs to Task 4.
- Human title/abstract screening and independent screening audit belong to Task 5.
- Human named-source identity decisions and discovery registry promotion belong to Task 6.
- `verify-all` is expected to fail honestly until all later artifacts exist.

## First formal review

The independent reviewer returned `NEEDS FIXES — 0 Critical, 5 Important, 0 Minor` for `179059084eb655f7dc5ad6ac0bbfb8da67c01c0c..f8de39eb063ab0a436d8235c2c0a41212ca09956`.

1. `validate_search_run` did not recompute `compiled_candidates_raw.csv` from manifested EFetch XML, and did not reject manifested raw artifacts without receipt ownership. A header-only compiled table with an updated manifest and an orphan manifested ESearch file both passed.
2. Wave 2 registry validation allowed an executed query to replace the frozen `2010/01/01`–`2026/12/31` interval with a shorter internally consistent interval.
3. Non-empty Wave 2 validation did not derive the expected executed cells from `QUERY_REGISTRY.csv`; a receipt could change family, lane, query, and related fields and still pass.
4. A manifested Crossref response whose `items` list contained a non-object caused `validate_lineage` to raise `AttributeError` rather than return a stable validation error.
5. Lineage audit validation allowed `unresolved_after_three_queries` after only one supporting query and allowed a blank primary reviewer.

All five are Important because they permit incomplete, altered, or malformed discovery artifacts to pass validation or escape stable error containment. The original implementation agent must add focused failing tests, correct the contracts without weakening any existing standard, rerun the complete verification suite, and commit a separate fix. The same reviewer must re-review the complete base-to-fixed-head range.

## First-review fix cycle

The original implementation agent added five focused tests that all failed at `f8de39eb063ab0a436d8235c2c0a41212ca09956` and then passed after the correction. The fix commit `3bae05606f74a2ac45787624fbce51029f3b5e5a`:

1. derives the exact canonical compiled table from receipt-owned manifested EFetch pages, compares it with the stored CSV, and rejects all manifested raw artifacts without receipt ownership;
2. requires every executed Wave 2 row to retain the frozen configuration interval;
3. derives non-empty Wave 2 receipt root cells from the fully validated registry and compares their identity/query/date/lane/source fields one-to-one;
4. rejects non-object Crossref candidates stably and uses component-wise no-follow confined reads for raw-response recomputation;
5. requires exactly three supporting queries for `unresolved_after_three_queries` and nonblank, distinct primary/audit reviewers with terminal status agreement.

The focused command passed 5/5; full discovery passed 82/82; legacy passed 25/25; configuration, repository, and external-boundary validators passed; compilation and whitespace checks passed. The same independent reviewer must now re-review the complete range `179059084eb655f7dc5ad6ac0bbfb8da67c01c0c..3bae05606f74a2ac45787624fbce51029f3b5e5a`, verify all five Important findings are closed, and scan for regressions.

## Second formal review

The same reviewer independently confirmed all five first-review findings closed, then returned `NEEDS FIXES — 0 Critical, 4 Important, 1 Minor` after the complete-range regression scan.

1. A source-conditional lineage receipt missing fields such as Crossref `response_sha256` could record a missing-field error and then enter candidate recomputation, where direct dictionary indexing raised `KeyError`; equivalent PubMed-page missing-field paths require the same containment.
2. Raw ownership was not a three-way equality. Wave 1/2 accepted unmanifested files in `raw/`; Wave 3 accepted both manifested and unmanifested orphan raw files. The required invariant is `actual regular raw files == manifested raw files == receipt-owned raw files`, with symlinks, temporary files, extra directories, and orphan raw rejected.
3. The strict all-no-expansion Wave 2 contract ran only when `empty_reason` was already present. Removing that field and adding `screening_batches/.keep` allowed search, screening, and audit validation to pass. The validator must derive zero executed rows from the validated registry, require the exact empty reason and exact artifacts, and forbid `empty_reason` for a non-empty wave.
4. Reviewer independence compared unnormalized strings, so `reviewer-a` and ` reviewer-a ` were accepted as different people. Reviewer fields must be canonical/nonblank and compared after normalization.

The Minor finding is that the changed-line counts in this package describe only the first implementation commit; the root agent will replace them with the final base-to-head counts after all fixes. The original implementation agent must add focused failing tests for the four Important findings, correct them without relaxing any contract, rerun full verification, and commit a separate fix. The same reviewer must re-review the new complete range.

## Second-review fix cycle

The original implementation agent added four focused tests that failed 4/4 at `3bae05606f74a2ac45787624fbce51029f3b5e5a` and passed 4/4 after the correction. The fix commit `888cc2775315af40f317356488191c146071e53e`:

1. prevents invalid source-conditional lineage receipts from entering candidate recomputation and makes PubMed/Crossref recomputation helpers stable for missing fields;
2. enforces component-confined, no-follow three-way equality among actual direct regular `raw/` files, manifested raw entries, and receipt-owned raw paths across Wave 1/2/3, including direct Wave 3 tests for orphan, symlink, temporary, and extra-directory states;
3. derives Wave 2 empty/non-empty status from the validated registry in search, screening, and audit validation, requires the exact empty contract for zero executed rows, and forbids `empty_reason` for non-empty waves;
4. requires canonical nonblank reviewer strings and compares reviewer identity after trim and case normalization.

The focused command passed 4/4; full discovery passed 86/86; legacy passed 25/25; configuration, repository, and external-boundary validators passed; compilation and whitespace checks passed. The changed-line counts above now reflect the full three-commit base-to-head range. The same reviewer must re-review `179059084eb655f7dc5ad6ac0bbfb8da67c01c0c..888cc2775315af40f317356488191c146071e53e`, verify all four Important findings and the statistics Minor are closed, and scan for regressions.

## Final independent review conclusion

The same independent reviewer completed the third full-range review and returned `PASS — 0 Critical, 0 Important, 0 Minor` for `179059084eb655f7dc5ad6ac0bbfb8da67c01c0c..888cc2775315af40f317356488191c146071e53e`. The reviewer independently reproduced closure of all second-review findings, tested 18 raw-closure variants across Wave 1/2/3, cross-probed strict zero/nonzero Wave 2 behavior through search/screening/audit validation, verified missing source-conditional fields remain contained, and confirmed normalized reviewer independence. The reviewer also reran 86/86 discovery tests, 25/25 legacy tests, all three validators, `py_compile`, and `git diff --check` successfully.
