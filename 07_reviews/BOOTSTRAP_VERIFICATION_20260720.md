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
  > /tmp/id_epi_library_surveillance_status_task8_review_live.txt
shasum -a 256 /tmp/id_epi_library_surveillance_status_before_task7.txt /tmp/id_epi_library_surveillance_status_task8_review_live.txt
wc -l /tmp/id_epi_library_surveillance_status_before_task7.txt /tmp/id_epi_library_surveillance_status_task8_review_live.txt
diff -u /tmp/id_epi_library_surveillance_status_before_task7.txt /tmp/id_epi_library_surveillance_status_task8_review_live.txt
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR status --porcelain=v1 -- ID_EPI_METHODS_LIBRARY_POINTER.md
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR ls-files --error-unmatch ID_EPI_METHODS_LIBRARY_POINTER.md
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR diff --cached --name-only
git -C /Users/hongchaokun/Documents/PhD/Surveillance_AMR rev-parse HEAD
```

The fresh live-receipt generation, digest, line-count, and comparison commands exited `0`. Concise output:

```text
e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e  /tmp/id_epi_library_surveillance_status_before_task7.txt
e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e  /tmp/id_epi_library_surveillance_status_task8_review_live.txt
16 /tmp/id_epi_library_surveillance_status_before_task7.txt
16 /tmp/id_epi_library_surveillance_status_task8_review_live.txt
32 total
?? ID_EPI_METHODS_LIBRARY_POINTER.md
eb5d15656b8fe69a8359705c80125d695a1c0782
```

`diff -u` produced no output. The `ls-files --error-unmatch` command exited `1`, confirming that the pointer is not tracked; the source index command returned no paths. After filtering only the exact pointer status line, the current 16-line porcelain receipt byte-matched the 16-line baseline receipt. This proves that no pre-existing path/status entry changed. It does not independently prove byte identity for files that were already dirty because no pre-write byte-hash manifest of those paths was captured.

The authorized Task 7 action log records that `apply_patch` wrote only the new pointer and that no staging or commit command was run in `Surveillance_AMR`; Task 8 likewise ran no source write, staging, or commit command. That action-scope evidence is distinct from the narrower independent status-receipt proof. The pointer remains present and intentionally untracked.

## Original pre-release branch and named-ref receipt

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
git ls-remote origin HEAD refs/heads/main: exit 0 with no output
```

This original receipt was captured at pre-release HEAD `36d81978d39a2b08f1d5d022c5143de817192645`. It proves only that the two named refs, `HEAD` and `refs/heads/main`, were absent at that time; it was not an all-ref query.

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

The initial release record is commit `64286301f4d04edba22d01571e4d8fba70e9f7b0`, subject `verify methods library bootstrap`, whose parent is the pre-release commit above.

## Review-correction and current pre-publication receipt

The first receipt-correction commit is `6a44aa5c71cbf6455bf26a9db1cb6d296b20e1c1`, subject `correct bootstrap verification receipts`, whose parent is the initial release-record commit.

Fresh commands run at that corrected branch tip:

```bash
date '+%Y-%m-%d %H:%M:%S %Z %z'
printf 'TZ=%s\n' "${TZ:-not-set}"
git rev-parse HEAD
git branch --show-current
git status --short --branch
git ls-remote origin
```

Exit code: `0`. Concise output:

```text
2026-07-20 07:38:46 CST +0800
TZ=not-set
6a44aa5c71cbf6455bf26a9db1cb6d296b20e1c1
codex/library-bootstrap
## codex/library-bootstrap
git ls-remote origin: no output
```

The process did not set `TZ`; the system receipt resolved `CST +0800` in the Asia/Shanghai context. The full `git ls-remote origin` all-ref query exited `0` with empty output, proving that no remote refs existed at this later current-pre-publication checkpoint. No push had occurred.

`git rev-parse HEAD` resolves the current corrected branch tip. At the timestamp above it returned the first receipt-correction commit; after this chronology clarification is committed it will resolve the newer clarification commit, not the initial release-record commit. The new commit cannot embed its own SHA in this tracked report; use `git rev-parse HEAD` for the live tip and the explicit immutable SHAs above for the two earlier Task 8 commits.

## Deferred work and next gate

The following work was not performed by Task 8:

1. controller whole-branch review;
2. correction and re-review of any whole-branch findings;
3. final validation of the reviewed branch;
4. merge to `main`;
5. push of verified `main` and remote-SHA equality receipt; and
6. broad applied-paper and authoritative method-source search planning or execution.

No candidate dataset was downloaded and no simulation was executed during bootstrap. Dataset acquisition and simulation execution remain deferred to separately approved plans after the applicable evidence, feasibility, and specification gates.

The exact next operational action is the controller-owned whole-branch review. Only after reviewed `main` is merged, revalidated, and published may the next scientific action begin: draft the separate broad-search execution plan for owner review. That future plan must remain methods/problem first; combine applied seeds with authoritative method lineage; preserve a portfolio of multiple flagship candidates, one or two lower-risk public-data projects, and a non-AMR infectious-disease route; and require a broad structural contribution for any pure-simulation flagship.

## Whole-branch review correction addendum — 2026-07-20

This addendum records the single owner-approved correction wave based on `0864f98f651965903e712d171d5813b7edbcb5ed`. It supplements and does not rewrite the historical Task 8 receipts above. The correction adds normalized relationship registries and hardens validation; it does not provide whole-branch re-review or publication authority.

### TDD and validator receipt

The focused RED command was:

```bash
python3 -m unittest 00_governance/tests/test_validate_library.py -v
```

Against the unchanged validator, it exited `1` after `Ran 19 tests` with `FAILED (failures=19)`. The expected failures demonstrated absent handling for non-object manifests, surplus and missing CSV fields, required fields, paper year consistency, method/candidate/simulation prefix consistency, composite-link uniqueness, all four new link-table foreign keys, design checksum validation, taxonomy README requirements, and the ten-registry minimal valid case.

After the minimum implementation, the same command exited `0`: `Ran 19 tests in 0.039s` and `OK`. The public signatures of `validate_repository`, `validate_csv`, `validate_foreign_keys`, `validate_seed_checksum`, and `main` remain unchanged.

Repository validation:

```bash
python3 00_governance/scripts/validate_library.py --root .
```

Exit code: `0`. Output: `VALIDATION PASS`.

An empty temporary root exercised the invalid CLI path: output began `VALIDATION FAIL` and the command exited `1`. The live repository path printed `VALIDATION PASS` and exited `0`.

### Registry and architecture receipt

The correction adds these four files, each with one header line and zero data rows:

- `03_evidence_tables/candidate_method_links.csv`
- `03_evidence_tables/candidate_dataset_links.csv`
- `03_evidence_tables/simulation_method_links.csv`
- `03_evidence_tables/simulation_candidate_links.csv`

The six pre-existing registries also remain one line with zero data rows. A ten-path `wc -l` loop exited `0` and reported `lines=1 data_rows=0` for every registry. After staging the four additions, `git ls-files | wc -l` reported 51 tracked paths. The sorted index-plus-untracked candidate inventory byte-matched the sorted filesystem architecture inventory after pruning `.git`, `.superpowers`, and Python bytecode caches; both contained 51 paths and `diff -u` exited `0`.

### Immutable-artifact receipt

```text
e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57  docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55  01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
```

`cmp` of the design against approved commit `c708ac2402431202c8b1af4c5fd87035460249ab` exited `0`. `cmp` of the Library seed against the named `Surveillance_AMR` source exited `0`. `git diff --exit-code 0864f98f651965903e712d171d5813b7edbcb5ed --` for the approved design and implementation plan exited `0`.

### Reciprocal pointer, remote, and scope boundary

The reciprocal pointer remains present and untracked. The Task 7 filtered baseline and the fresh filtered `Surveillance_AMR` porcelain status both had SHA256 `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e`, 16 lines, and `diff -u` exit `0`. The exact pointer status remained `?? ID_EPI_METHODS_LIBRARY_POINTER.md`; `git ls-files --error-unmatch` exited `1`; the source index contained no staged paths; and source HEAD remained `eb5d15656b8fe69a8359705c80125d695a1c0782`. This proves unchanged path/status state after excluding the pointer, not byte identity for paths that were already dirty before Task 7.

At `2026-07-20 08:02:49 CST +0800`, the full command `git ls-remote origin` exited `0` with no output, so the remote still had no refs. This correction wave did not push, merge, create a pull request, modify `main`, run a literature search, download candidate data, execute simulations, select a flagship, or write any `Surveillance_AMR` file. The exact next action remains whole-branch re-review followed by the final validation/publication gate.

## Validator error-boundary correction addendum — 2026-07-20

This addendum records the bounded read-failure correction based on `2040adee0e4435a00a056798ea31b49d5ada8f33`. It preserves all earlier receipts and does not confer re-review, merge, or publication authority.

### RED, GREEN, and validator receipt

Six focused tests were added before production edits. The focused RED command exited `1` with `Ran 6 tests` and `FAILED (failures=6)`. The failures showed uncaught invalid-UTF-8 registry and manifest reads, an uncaught registry `PermissionError`, permissive acceptance of an unterminated quoted CSV field, unsafe foreign-key rereading, and an escaping CLI exception.

After the minimum implementation, the same six focused tests exited `0` with `OK`. The full command `python3 -m unittest 00_governance/tests/test_validate_library.py -v` then exited `0` with `Ran 25 tests in 0.042s` and `OK`, preserving the prior 19 behaviors. `python3 00_governance/scripts/validate_library.py --root .` exited `0` and printed `VALIDATION PASS`.

The validator now uses strict CSV parsing and converts `csv.Error`, `UnicodeError`, and `OSError` into path-specific human-readable errors. Foreign-key endpoint metadata is stored on each canonical registry specification; link and target reads are cached per call, and every target ID set is built at most once per call. The five public function signatures remain unchanged.

### Malformed CLI probes

Three real subprocess probes used temporary roots. Each printed `VALIDATION FAIL`, exited `1`, and produced zero `Traceback` occurrences:

```text
invalid registry: 03_evidence_tables/papers.csv: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
invalid UTF-8 registry CLI exit=1 traceback_count=0

invalid seed manifest: 01_search/seed_scans/MANIFEST_SHA256.json: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
invalid UTF-8 manifest CLI exit=1 traceback_count=0

invalid registry: 03_evidence_tables/papers.csv: Error: unexpected end of data
malformed quoted CSV CLI exit=1 traceback_count=0
```

### Registry, provenance, pointer, and remote receipt

All ten registries remained exactly one line with zero data rows. The immutable hashes remained:

```text
e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57  docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55  01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
```

The design comparison against approved commit `c708ac2402431202c8b1af4c5fd87035460249ab` and the seed comparison against the named `Surveillance_AMR` source each exited `0`. The fresh filtered `Surveillance_AMR` status still matched the 16-line Task 7 baseline with `diff -u` exit `0`; the exact pointer status remained `?? ID_EPI_METHODS_LIBRARY_POINTER.md`; the source index had zero staged paths; and source HEAD remained `eb5d15656b8fe69a8359705c80125d695a1c0782`. This remains path/status proof, not byte-identity proof for paths already dirty before Task 7.

At `2026-07-20 08:18:26 CST +0800`, the full `git ls-remote origin` query exited `0` with no output, so the remote remained empty. This wave did not push, merge, create a pull request, modify `main`, run a search, download data, execute a simulation, select a flagship, or write any `Surveillance_AMR` file. The next action is whole-branch re-review, followed by the final validation/merge/publication gate.
