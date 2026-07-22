# Task 6 Independent Review

## Current verdict

`NEEDS FIXES — 0 Critical, 6 Important, 1 Minor`

- Spec compliance: NEEDS FIXES
- Task quality: NEEDS FIXES
- Review range: `75d0b1456716f46d20fb0682a836335b33f04d42..b66102089630b9a10db2ee07bcd4dada0b898191`
- Reviewed head: `b66102089630b9a10db2ee07bcd4dada0b898191`
- Implementation commit: `b66102089630b9a10db2ee07bcd4dada0b898191`
- Review package: `07_reviews/discovery_tasks/TASK_6_REVIEW_PACKAGE.md`
- Exact diff package: `.superpowers/sdd/review-75d0b14..b661020.diff`
- Exact diff SHA256: `e222f622c7a1d55e790fac83fd3b707d96f18b15288ed8164267afc6c04428b5`

## Blocking findings

1. **Lineage tracing is incomplete.** All 435 named sources are already-retained Task 5 records, and Wave 3 mainly re-identifies those records. Seventy-one of 277 concepts have no method-source candidate; for example, heterogeneity-robust staggered difference-in-differences records only one infectious-disease application and no authoritative-method-source attempt. Each concept must inspect assigned records for actually named/cited sources and must trace authoritative sources, directly named corrections/guidance/implementations, or record an honest unresolved attempt.
2. **All 513 active query IDs misuse the execution-date field.** The receipt records execution on 2026-07-22, while IDs use 20260719, 20260718, and 20260717 as revision keys. The approved namespace defines that token as the execution date. The fix must use the true execution date, preserve globally unique IDs, and explicitly support sequence values above 99 when required.
3. **Method-card variants are semantically invalid.** In 273 of 277 cards, provisional routing buckets that were split across multiple concepts are presented as `Known label variants`. Only evidenced synonyms may remain variants; rejected routing buckets belong only in merge/split provenance.
4. **Provisional relationship roles are mechanically overclaimed.** All 1,780 `method_source` records were mapped to `originates` and all 254 `guidance` records to `critiques`, including examples whose inspected title/abstract does not support that relation. Every emitted `provisional_role` requires row-level semantic evidence; omit a relationship when no allowed role is supported.
5. **Continuity artifacts contradict the reviewed head.** `HANDOFF.md` and `EXECUTION_LEDGER.md` still say Task 6 has no semantic output or implementation. They must record the implementation SHA, exact current counts, this failed verdict, and the required repair without claiming PASS.
6. **The new `.gitattributes` rules disable the whitespace gate too broadly.** They suppress checking for every CSV/XML/log in active and archive Wave 3, including formal registries and decision tables. Normalize generated CSV to LF or use only a narrow `cr-at-eol` allowance; reserve `-whitespace` for byte-preserved raw evidence that cannot be normalized.

## Minor finding

- Replace the contradictory route phrase `bounded unbounded-date identity queries` with the accurate `bounded date-unrestricted identity queries`.

## Independently confirmed structure

- The 7,779 retained keys and 7,779 assignments are the same unique set and map to 277 concepts with matching counts.
- All 53 adopted A/B/C evidence artifacts exist; none of the eight zero-adoption attempts entered final assignments.
- Seven archive manifests rehash 1,817 entries with zero missing files or SHA mismatches; active and archived query-ID sets are disjoint.
- Current mechanical lineage counts are 435 named sources, 513 active queries, 450 candidates, and 432 resolved / two ambiguous / one unresolved terminal outcomes with reviewer independence.
- Paper and method registry/card counts are 7,779 and 277. Deferred normalized registries remain header-only; `02_method_library` is unchanged and `frozen_002` is absent.
- Library validation, both Wave 1/2 screening/audit validators, `verify-lineage`, and the fresh 89-test discovery suite passed.
- `Surveillance_AMR` remained at HEAD `eb5d15656b8fe69a8359705c80125d695a1c0782`; the external validator's only drift is the already-known post-baseline untracked GBD directory.

Task 7 remains blocked. The original Task 6 implementer must fix every Important finding, commit the repair, regenerate the complete base-to-repaired-head review package, and obtain an independent re-review with zero Critical and zero Important findings.
