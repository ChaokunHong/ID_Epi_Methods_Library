# Bootstrap Verification — 2026-07-20

## Verdict and scope

The local bootstrap implementation and release record passed the Task 8 gate on branch `codex/library-bootstrap`, using pre-release commit `36d81978d39a2b08f1d5d022c5143de817192645`. This is a local verification result, not publication authority. Final whole-branch review, any required fix and re-review cycle, final validation, merge to `main`, and push of verified `main` are explicitly deferred to the controller.

This gate verifies the repository structure, validator contract, frozen design and seed bytes, empty registry state, reciprocal-pointer receipt, and Git boundary described below. It does not verify every external link, literature claim, method claim, dataset claim, or candidate, and it does not select a flagship.

## Environment receipt

Command:

```bash
git --version
python3 --version
date '+%Y-%m-%d %H:%M:%S %Z %z'
printf 'TZ=%s\n' "${TZ:-not-set}"
```

Exit code: `0`.

Concise output:

```text
git version 2.50.1 (Apple Git-155)
Python 3.12.0
2026-07-20 07:20:22 CST +0800
TZ=not-set
```

The process did not set `TZ`; the system `date` receipt resolved the local zone as `CST +0800` (Asia/Shanghai context).

## Automated checks

Command:

```bash
python3 -m unittest 00_governance/tests/test_validate_library.py -v
```

Exit code: `0`. Concise output: seven named tests ran in `0.008s`; `Ran 7 tests` and `OK` were reported, with zero failures or errors.

Command:

```bash
python3 00_governance/scripts/validate_library.py --root .
```

Exit code: `0`. Output: `VALIDATION PASS`.

Command:

```bash
git diff --check
git status --short
```

Initial pre-authoring exit code: `0`; output was empty. The same whitespace and status boundary was rerun on the authored Task 8 files with exit code `0`; `git status --short` showed only:

```text
 M HANDOFF.md
?? 07_reviews/BOOTSTRAP_VERIFICATION_20260720.md
```

The Task 5 exception remains narrow: the byte-locked seed snapshot is exempt because its required bytes include trailing spaces at line 3. Its integrity is enforced by both SHA256 and byte comparison below. Both Task 8 edits remain subject to `git diff --check` without exclusions; the exception does not broaden to any other edit.

## Frozen-artifact provenance

Commands:

```bash
shasum -a 256 docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
cmp -s 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
```

Combined exit code: `0`.

```text
e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57  docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55  01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
```

`cmp -s` produced no output and exited `0`, so the Library seed bytes match the named source snapshot. The seed remains a discovery map, not verified registry evidence.

## Registry receipts

Command:

```bash
for registry in 03_evidence_tables/papers.csv 03_evidence_tables/methods.csv 03_evidence_tables/paper_method_links.csv 04_translation_candidates/translation_candidates.csv 05_data_registry/datasets.csv 06_simulation_lab/simulations.csv; do
  lines=$(wc -l < "$registry" | tr -d ' ')
  rows=$((lines - 1))
  test "$lines" -eq 1 || exit 1
  printf '%s lines=%s data_rows=%s\n' "$registry" "$lines" "$rows"
done
```

Exit code: `0`.

| Registry | Lines | Data rows |
|---|---:|---:|
| `03_evidence_tables/papers.csv` | 1 | 0 |
| `03_evidence_tables/methods.csv` | 1 | 0 |
| `03_evidence_tables/paper_method_links.csv` | 1 | 0 |
| `04_translation_candidates/translation_candidates.csv` | 1 | 0 |
| `05_data_registry/datasets.csv` | 1 | 0 |
| `06_simulation_lab/simulations.csv` | 1 | 0 |

Each registry therefore contains exactly one header line and zero data rows.

## Architecture and execution-control boundary

Commands:

```bash
find . -path ./.git -prune -o -type f -print | LC_ALL=C sort
git ls-files | LC_ALL=C sort
find . -path ./.git -prune -o -path ./.superpowers -prune -o -path '*/__pycache__' -prune -o -type f -print | LC_ALL=C sort
git check-ignore -v .superpowers/sdd/task-8-brief.md .superpowers/sdd/task-8-report.md
```

Exit codes: `0` for the inventories and ignore check. Before authoring this report, the raw inventory contained 75 files: 46 tracked repository files, 27 ignored `.superpowers/sdd/` execution-control files, and two ignored Python bytecode-cache files. The raw inventory intentionally exposed those categories rather than silently treating all filesystem files as repository artifacts.

`.superpowers/sdd/` contains the task briefs, implementation reports, review packages, and progress ledger required to execute the plan. It is intentionally ignored by `.superpowers/sdd/.gitignore` and is not part of the planned repository architecture; it was preserved, not deleted. Python `__pycache__/` output is also ignored runtime material. The tracked inventory and the `find` inventory that explicitly prunes `.superpowers` and bytecode caches matched the 46-file pre-release repository architecture. This verification report becomes the forty-seventh tracked architecture file when staged and committed.

Pre-release tracked architecture inventory:

```text
.gitignore
00_governance/DECISION_LOG.md
00_governance/PROJECT_CHARTER.md
00_governance/REGISTRY_SCHEMA.md
00_governance/RESUME_PROMPT.md
00_governance/SCOPE_AND_ELIGIBILITY.md
00_governance/WORKFLOW.md
00_governance/scripts/validate_library.py
00_governance/tests/test_validate_library.py
01_search/SEARCH_LOG_TEMPLATE.md
01_search/journal_registry/README.md
01_search/search_logs/README.md
01_search/search_protocols/README.md
01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
01_search/seed_scans/MANIFEST_SHA256.json
01_search/seed_scans/SEED_SCAN_PROVENANCE.md
02_method_library/METHOD_CARD_TEMPLATE.md
02_method_library/causal_policy/README.md
02_method_library/evidence_synthesis/README.md
02_method_library/forecasting_dynamics/README.md
02_method_library/simulation_methods/README.md
02_method_library/spatial_transmission/README.md
02_method_library/surveillance_measurement/README.md
03_evidence_tables/methods.csv
03_evidence_tables/paper_method_links.csv
03_evidence_tables/papers.csv
04_translation_candidates/TRANSLATION_CARD_TEMPLATE.md
04_translation_candidates/amr/README.md
04_translation_candidates/flagship_portfolio/README.md
04_translation_candidates/infectious_diseases/README.md
04_translation_candidates/translation_candidates.csv
05_data_registry/DATASET_CARD_TEMPLATE.md
05_data_registry/datasets.csv
06_simulation_lab/SIMULATION_CARD_TEMPLATE.md
06_simulation_lab/dgp_specs/README.md
06_simulation_lab/reports/README.md
06_simulation_lab/scripts/README.md
06_simulation_lab/simulations.csv
06_simulation_lab/tests/README.md
07_reviews/REVIEW_TEMPLATE.md
99_archive/README.md
AGENTS.md
HANDOFF.md
README.md
docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md
docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
```

## Reciprocal source-pointer receipt

Commands:

```bash
test -f /Users/hongchaokun/Documents/PhD/Surveillance_AMR/ID_EPI_METHODS_LIBRARY_POINTER.md
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR status --porcelain=v1 \
  | sed '/^?? ID_EPI_METHODS_LIBRARY_POINTER.md$/d' \
  | cmp -s - /tmp/id_epi_library_surveillance_status_before_task7.txt
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR status --porcelain=v1 -- ID_EPI_METHODS_LIBRARY_POINTER.md
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR ls-files --error-unmatch ID_EPI_METHODS_LIBRARY_POINTER.md
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR diff --cached --name-only
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR rev-parse HEAD
```

Exit code: `0` for file presence and the exact filtered-status comparison. Concise output:

```text
?? ID_EPI_METHODS_LIBRARY_POINTER.md
eb5d15656b8fe69a8359705c80125d695a1c0782
```

The `ls-files --error-unmatch` command exited `1`, confirming that the pointer is not tracked; the source index command returned no paths. After filtering only the exact pointer status line, current source status byte-matched `/tmp/id_epi_library_surveillance_status_before_task7.txt`. The pointer is present and intentionally untracked; Task 8 staged or committed nothing in `Surveillance_AMR` and did not modify its pre-existing dirty paths.

## Git and remote pre-publication receipt

Commands:

```bash
git branch --show-current
git rev-parse HEAD
git status --short --branch
git log --oneline --decorate --all
git remote -v
git ls-remote origin HEAD refs/heads/main
```

Exit code: `0`. Pre-release state:

```text
branch: codex/library-bootstrap
HEAD: 36d81978d39a2b08f1d5d022c5143de817192645
origin fetch: https://github.com/ChaokunHong/ID_Epi_Methods_Library.git
origin push: https://github.com/ChaokunHong/ID_Epi_Methods_Library.git
remote HEAD and refs/heads/main: no output (empty remote)
```

Pre-release log:

```text
36d8197 (HEAD -> codex/library-bootstrap) update handoff after reciprocal pointer
e8953a9 record reciprocal project pointer
f14f3fb clarify recoverable handoff state
ef2d78f correct handoff evidence
de58d0c add filesystem-based project handoff
975f3ea freeze broadened infectious disease seed scan
bab42d6 add validated linked library registries
c9f2954 add research card and folder contracts
3a66dd1 define library governance and workflow
5082ebd bootstrap repository entry points
1c49f69 (main) ignore isolated worktrees
9d38e23 plan methods library bootstrap
c708ac2 define infectious disease methods library design
```

The local release record is committed with subject `verify methods library bootstrap`. Because a tracked report cannot embed the SHA of the commit that contains itself, resolve that exact release-record commit with `git rev-parse HEAD` after the commit.

## Deferred work and next gate

The following work was not performed by Task 8:

1. controller whole-branch review;
2. correction and re-review of any whole-branch findings;
3. final validation of the reviewed branch;
4. merge to `main`;
5. push of verified `main` and remote-SHA equality receipt; and
6. broad applied-paper and authoritative method-source search planning or execution.

The exact next operational action is the controller-owned whole-branch review. Only after reviewed `main` is merged, revalidated, and published may the next scientific action begin: draft the separate broad-search execution plan for owner review. That future plan must remain methods/problem first; combine applied seeds with authoritative method lineage; preserve a portfolio of multiple flagship candidates, one or two lower-risk public-data projects, and a non-AMR infectious-disease route; and require a broad structural contribution for any pure-simulation flagship.
