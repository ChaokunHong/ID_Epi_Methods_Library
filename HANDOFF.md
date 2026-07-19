# Handoff

## Project identity

`ID_Epi_Methods_Library` is a methods-first infectious-disease epidemiology translation library. It discovers, verifies, compares, and translates methods; it does not own a promoted paper's protocol or analysis. The project owner, Chaokun Hong, retains final authority for scope changes and candidate graduation.

## Current phase and status

**Bootstrap complete; broad-search execution plan pending owner review.** Tasks 1–8 local implementation and release-record work are complete on `codex/library-bootstrap`. The release evidence is `07_reviews/BOOTSTRAP_VERIFICATION_20260720.md`, prepared from pre-release commit `36d81978d39a2b08f1d5d022c5143de817192645`. Final whole-branch review, any required fixes and re-review, final validation, merge to `main`, and publication of verified `main` remain pending and controller-owned. Resolve the exact release-record commit with `git rev-parse HEAD`: a handoff file cannot embed the SHA of the commit containing that same text.

The frozen broadened seed scan was committed in `975f3ea43fb7d927b64028c2108c92e3db5a8b4f` (`freeze broadened infectious disease seed scan`), Task 6 continuity files were introduced in `de58d0c5160d6e8d5a7b14ea75cba155c22cdd92` (`add filesystem-based project handoff`), and the Task 7 reciprocal pointer was completed and recorded in full commit `e8953a920800c932df75ff39631e06a29aaaeede` (`record reciprocal project pointer`). Review corrections follow in the Git history. The approved design was committed as `c708ac2402431202c8b1af4c5fd87035460249ab` (`define infectious disease methods library design`), and the bootstrap implementation plan was committed as `9d38e235f031d0b5959e1d587ee28fe8d20a53de` (`plan methods library bootstrap`). No flagship has been selected, and no broad applied-paper or method-source search has been executed.

## Approved scope

Discovery is method/problem first, not data/disease first. Do not exclude leads because they are not AMR-specific, LMIC-specific, global, immediately public-data feasible, or solo-executable. Applied infectious-disease seeds, relevant npj/specialist applied seeds, original or authoritative methods sources, and simulation-only, synthetic-data, mechanistic, and method-comparison studies are in scope. The intended portfolio includes multiple flagship candidates, one or two lower-risk public-data projects, and a credible non-AMR infectious-disease route. A pure-simulation flagship needs a broad structural contribution.

## Immutable outputs

- Approved design: `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`, commit `c708ac2402431202c8b1af4c5fd87035460249ab`, SHA256 `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`; preserve byte-for-byte.
- Frozen seed snapshot: `01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`, commit `975f3ea43fb7d927b64028c2108c92e3db5a8b4f`, SHA256 `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`; verify with both SHA256 and `cmp` against `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md` before any claimed replacement.
- Remote: `origin` is `https://github.com/ChaokunHong/ID_Epi_Methods_Library.git` (not yet pushed).

## Registry state

All six registries contain headers only: `03_evidence_tables/papers.csv`, `03_evidence_tables/methods.csv`, `03_evidence_tables/paper_method_links.csv`, `04_translation_candidates/translation_candidates.csv`, `05_data_registry/datasets.csv`, and `06_simulation_lab/simulations.csv`. The seed scan is a frozen discovery map, not verified registry content.

## Related projects

`/Users/hongchaokun/Documents/PhD/Surveillance_AMR` is a separate AMR application project and the source of the copied seed snapshot. The reciprocal pointer at `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/ID_EPI_METHODS_LIBRARY_POINTER.md` is present but intentionally uncommitted in the dirty `Surveillance_AMR` worktree; no existing source file changed. Do not modify its protocol or application-specific decisions except through an explicit, separately reviewed task. The next scientific task belongs in this Library and must not perform a `Surveillance_AMR` protocol change.

## Known blockers and non-blockers

There are no current blockers to the controller-owned final review and publication gate. The broad-search execution plan is the next scientific plan only after reviewed `main` is merged, revalidated, and published. The Task 5 whitespace exception is narrow: the byte-locked seed snapshot alone is exempt from the Task 8 edit-level whitespace gate because line 3 has two intentional trailing spaces. Its exact SHA256 and `cmp` verification remain mandatory. This exception does not relax `git diff --check` or any other gate for Task 8 edits or future files.

## Exact next action

The controller must review the complete branch against the approved design and bootstrap plan, apply and re-review any required corrections, run final validation, merge the verified branch to `main`, and push only verified `main` with an exact remote-SHA receipt. Do not push this task branch. After publication succeeds, draft the separate methods/problem-first broad applied-paper and authoritative method-source search execution plan for owner review; do not execute that search or select a flagship during this gate.

## Verification commands

```bash
git status --short --branch
git log --oneline --decorate --all
git remote -v
shasum -a 256 docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
cmp -s 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
python3 00_governance/scripts/validate_library.py --root .
git diff --check
```

## Last updated

2026-07-20 after the Task 8 local release gate. Resolve the current exact commit with `git rev-parse HEAD`; a handoff file cannot embed the SHA of the commit containing itself. Final whole-branch review, merge, and publication remain pending.
