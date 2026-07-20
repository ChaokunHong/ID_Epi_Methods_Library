# Handoff

## Project identity

`ID_Epi_Methods_Library` is a methods-first infectious-disease epidemiology translation library. It discovers, verifies, compares, and translates methods; it does not own a promoted paper's protocol or analysis. The project owner, Chaokun Hong, retains final authority for scope changes and candidate graduation.

## Current phase and status

**Bootstrap is complete and published.** The implementation and both correction waves passed final whole-branch re-review of `13e133417e44c6b869dca40b7fff2afd046bf42b` with `Ready to merge: Yes`, 0 Critical findings, 0 Important findings, and one deferred non-blocking Minor concerning redundant `try`/`except` test wrappers. The first verified publication equality was `local main = origin/main = remote refs/heads/main = 36379bf4d648909854140d383959ebeefe88e569`. The release evidence and dated review addenda are in `07_reviews/BOOTSTRAP_VERIFICATION_20260720.md`, and the owner-approved correction schema is recorded as `DEC-20260720-005`. This publication-state receipt is a later commit, so resolve its exact live commit with `git rev-parse HEAD` and use `git ls-remote origin refs/heads/main` for final remote equality. The separate methods/problem-first broad applied-paper and authoritative method-source search execution plan is pending owner review. No broad search, data download, formal simulation, or flagship selection has started.

The frozen broadened seed scan was committed in `975f3ea43fb7d927b64028c2108c92e3db5a8b4f` (`freeze broadened infectious disease seed scan`), Task 6 continuity files were introduced in `de58d0c5160d6e8d5a7b14ea75cba155c22cdd92` (`add filesystem-based project handoff`), and the Task 7 reciprocal pointer was completed and recorded in full commit `e8953a920800c932df75ff39631e06a29aaaeede` (`record reciprocal project pointer`). Review corrections follow in the Git history. The approved design was committed as `c708ac2402431202c8b1af4c5fd87035460249ab` (`define infectious disease methods library design`), and the bootstrap implementation plan was committed as `9d38e235f031d0b5959e1d587ee28fe8d20a53de` (`plan methods library bootstrap`). No flagship has been selected, no broad applied-paper or method-source search has been executed, no candidate dataset has been downloaded, and no simulation has been executed.

## Approved scope

Discovery is method/problem first, not data/disease first. Do not exclude leads because they are not AMR-specific, LMIC-specific, global, immediately public-data feasible, or solo-executable. Applied infectious-disease seeds, relevant npj/specialist applied seeds, original or authoritative methods sources, and simulation-only, synthetic-data, mechanistic, and method-comparison studies are in scope. The intended portfolio includes multiple flagship candidates, one or two lower-risk public-data projects, and a credible non-AMR infectious-disease route. A pure-simulation flagship needs a broad structural contribution.

## Immutable outputs

- Approved design: `docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`, commit `c708ac2402431202c8b1af4c5fd87035460249ab`, SHA256 `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`; preserve byte-for-byte.
- Frozen seed snapshot: `01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`, commit `975f3ea43fb7d927b64028c2108c92e3db5a8b4f`, SHA256 `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`; verify with both SHA256 and `cmp` against `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md` before any claimed replacement.
- Remote: `origin` is `https://github.com/ChaokunHong/ID_Epi_Methods_Library.git`; `main` was first published with verified local, tracking-ref, and remote equality at `36379bf4d648909854140d383959ebeefe88e569`.

## Registry state

All ten registries contain headers only: `03_evidence_tables/papers.csv`, `03_evidence_tables/methods.csv`, `03_evidence_tables/paper_method_links.csv`, `03_evidence_tables/candidate_method_links.csv`, `03_evidence_tables/candidate_dataset_links.csv`, `03_evidence_tables/simulation_method_links.csv`, `03_evidence_tables/simulation_candidate_links.csv`, `04_translation_candidates/translation_candidates.csv`, `05_data_registry/datasets.csv`, and `06_simulation_lab/simulations.csv`. Under `DEC-20260720-005`, normalized registries are the authoritative relationship store and linked-ID fields in Markdown cards are mirrors that must match once records exist. The seed scan is a frozen discovery map, not verified registry content.

## Related projects

`/Users/hongchaokun/Documents/PhD/Surveillance_AMR` is a separate AMR application project and the source of the copied seed snapshot. The reciprocal pointer at `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/ID_EPI_METHODS_LIBRARY_POINTER.md` is present but intentionally uncommitted in the dirty `Surveillance_AMR` worktree. The authorized Task 7 action log records only creation of that pointer. After filtering only its exact untracked status line, the current 16-line porcelain receipt equals the 16-line pre-write receipt, proving that no pre-existing path/status entry changed; because no pre-write byte-hash manifest was captured for already-dirty paths, this does not independently prove their byte identity. Do not modify the source protocol or its application-specific decisions except through an explicit, separately reviewed task. The next scientific task belongs in this Library and must not perform a `Surveillance_AMR` protocol change.

## Known blockers and non-blockers

There are no bootstrap blockers. The one deferred Minor—redundant `try`/`except` wrappers around several validator-test assertions—is non-blocking and does not alter validator behavior or release readiness. The separate broad-search execution plan is pending owner review and must not be executed before approval. The Task 5 whitespace exception is narrow: the byte-locked seed snapshot alone is exempt from the Task 8 edit-level whitespace gate because line 3 has two intentional trailing spaces. Its exact SHA256 and `cmp` verification remain mandatory. This exception does not relax `git diff --check` or any other gate for correction edits or future files.

## Exact next action

The controller must first run final validation of the current `main`, push the current `main`, and then verify that `git rev-parse HEAD`, `git rev-parse origin/main`, and the SHA reported by `git ls-remote origin refs/heads/main` are identical. Only after that current three-way equality passes is the next scientific gate owner review of the separate methods/problem-first broad applied-paper and authoritative method-source search execution plan. Until that plan is approved, do not execute the search, download candidate data, run a formal simulation, or select a flagship.

## Verification commands

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
git ls-remote origin refs/heads/main
git log --oneline --decorate --all
git remote -v
shasum -a 256 docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
cmp -s 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
python3 00_governance/scripts/validate_library.py --root .
git diff --check
```

## Last updated

2026-07-20 after the first verified publication equality at `36379bf4d648909854140d383959ebeefe88e569` and creation of the later publication-state receipt. That initial publication remains verified, but the current `main` is locally ahead until the controller finishes final validation, pushes it, and confirms current three-way SHA equality. Resolve the current exact commit with `git rev-parse HEAD`; a handoff file cannot embed the SHA of the commit containing itself. Owner review of the separate broad-search execution plan follows only after that equality passes.
