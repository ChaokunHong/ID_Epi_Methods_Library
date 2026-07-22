# Broad Discovery External Release Contract Amendment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the sole Task 8 external-boundary blocker by recording and enforcing the owner-approved, exact allowlisted GBD status delta without changing the frozen baseline, existing validator, external worktree, or any scientific artifact.

**Architecture:** This is a narrow owner-approved amendment to `docs/superpowers/plans/2026-07-20-broad-methods-discovery-search.md`; it is not a new scientific task. It replaces only the Task 8 Step 1 release interpretation that the existing external validator must exit `0` and the Task 8 Step 2 release interpretation that live pointer-filtered status must equal the phase-start receipt. The legacy validator remains mandatory and nonpassing, while a static JSON contract plus exact read-only assertions establish whether the sole live delta is the owner-owned untracked GBD directory.

**Tech Stack:** Git; Markdown; JSON; Python 3.12 standard library; SHA-256; read-only Git porcelain inspection.

## Global Constraints

- Owner approval: Chaokun Hong approved this narrow replacement contract on 2026-07-22.
- Decision authority: `DEC-20260722-010`; `DEC-20260722-009` was already occupied and remains unchanged.
- Original approved plan: `docs/superpowers/plans/2026-07-20-broad-methods-discovery-search.md`, SHA256 `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`; preserve its bytes.
- Frozen external baseline: `07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json`, SHA256 `d1b48eb6c11b4e3701acfba5135bcd678ba101d44516b494f2e31d33f21b087b`; preserve its bytes.
- Task 8 blocker receipt: `07_reviews/discovery_tasks/TASK_8_REVIEW.md`, reviewed head `70e5820dadf073cea19cc4fe7eb3f1bca377b269`, verdict `NEEDS FIXES / ACK withheld — 0 Critical, 1 Important, 0 Minor`.
- Original Task 8 review base: `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52`; the same Task 8 reviewer must re-review the complete range from this base through the repair head.
- Source repository: `/Users/hongchaokun/Documents/PhD/Surveillance_AMR`; every command in this amendment is read-only there.
- Do not modify any search, screening, registry, lineage, coverage, wave, manifest, validator, frozen baseline, GBD, pointer, seed-source, or other external file.
- Do not use the ignored custom runtime harness. This amendment uses only the exact commands below and the existing repository tests and validators.
- The existing `verify-external-boundary` command must still run. Its required observed result remains exit `1` with `DISCOVERY FAIL` and exactly `- external filtered status mismatch`; record it as a nonpassing legacy check and never relabel it `PASS`.
- Any mismatch in source HEAD, pointer/index state, seed status/SHA/byte comparison, live status, allowlisted GBD counts/prefix, historical reconstruction, or checkpoint equality blocks release.
- Proof remains path/status evidence only, not dirty-file byte identity.
- Every original Task 8 gate not explicitly replaced above remains binding, including the same-reviewer Task 8 gate, whole-branch review, merged-`main` rerun, remote equality, and push gate.

---

## Amendment Boundary

This amendment replaces exactly these two release interpretations and nothing else:

1. Task 8 Step 1: replace “the existing external validator must exit `0` for release” with “run and record the existing validator at exit `1`, then require the amended external release gate below to pass.”
2. Task 8 Step 2: replace “live pointer-filtered status must equal the phase-start receipt” with “the exact owner-approved GBD-only delta must reconstruct the phase-start default receipt and the separately recorded historical expanded receipts.”

The original plan text remains immutable. This amendment supplements its execution contract; it does not rewrite history or call the existing validator successful.

Before a Task 8 repair begins, a fresh independent reviewer must review the exact base-to-amendment-commit diff and return `PASS — no remaining Critical or Important findings`. The reviewer must confirm the two-file amendment scope, exact constants, unchanged original-plan and baseline hashes, and absence of any external write.

## File Map

| Path | Responsibility |
|---|---|
| `07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722.json` | Static owner-approved release contract and exact external-state constants |
| `07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md` | Historical legacy-validator result plus repair pre/post amended-gate evidence |
| `HANDOFF.md` | Live Task 8 repair/re-review state and exact next action |

No other tracked path belongs to the Task 8 repair commit.

## Release Contract JSON Interface

The JSON root is an object with exactly these keys and types:

- `schema_version`: integer, exactly `1`.
- `contract_id`: string, exactly `BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722`.
- `status`: string, exactly `owner_approved_active`.
- `authority`, `amendment_scope`, `legacy_validator`, `source`, `pointer`, `seed`, `allowlisted_delta`, `live_status`, `historical_reconstruction`, and `release_gate`: objects with exactly the fields and values shown below.
- `amendment_scope.replaces`, `release_gate.required_checkpoints`, and `release_gate.forbidden_green_actions`: arrays of strings.
- `pointer.required_index_paths`: an empty array.
- Every `line_count`, `required_exit`, and allowlisted-entry count: integer.
- Every `sha256`: 64-character lowercase hexadecimal string.
- `seed.cmp_required` and `allowlisted_delta.other_delta_allowed`: booleans.

Create the contract with exactly this content and a trailing newline:

```json
{
  "schema_version": 1,
  "contract_id": "BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722",
  "status": "owner_approved_active",
  "authority": {
    "owner": "Chaokun Hong",
    "approved_on": "2026-07-22",
    "decision_id": "DEC-20260722-010",
    "blocker_receipt": "07_reviews/discovery_tasks/TASK_8_REVIEW.md",
    "blocker_reviewed_head": "70e5820dadf073cea19cc4fe7eb3f1bca377b269",
    "amended_plan": "docs/superpowers/plans/2026-07-20-broad-methods-discovery-search.md",
    "amended_plan_sha256": "671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209",
    "amendment_plan": "docs/superpowers/plans/2026-07-22-broad-discovery-external-release-contract-amendment.md"
  },
  "amendment_scope": {
    "replaces": [
      "Task 8 Step 1 release interpretation that verify-external-boundary must exit 0",
      "Task 8 Step 2 release interpretation that live pointer-filtered status must equal the phase-start receipt"
    ],
    "preserves": "Every other command, gate, review, merge, merged-main rerun, remote-equality, and push requirement in the original plan."
  },
  "legacy_validator": {
    "command": "python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR",
    "required_exit": 1,
    "required_output_lines": [
      "DISCOVERY FAIL",
      "- external filtered status mismatch"
    ],
    "classification": "recorded_nonpassing_legacy_check_not_reclassified_as_pass"
  },
  "source": {
    "repository": "/Users/hongchaokun/Documents/PhD/Surveillance_AMR",
    "required_head": "eb5d15656b8fe69a8359705c80125d695a1c0782",
    "write_policy": "read_only"
  },
  "pointer": {
    "path": "ID_EPI_METHODS_LIBRARY_POINTER.md",
    "required_porcelain_line": "?? ID_EPI_METHODS_LIBRARY_POINTER.md",
    "required_tracking_state": "untracked",
    "required_index_paths": []
  },
  "seed": {
    "source_path": "02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md",
    "library_path": "01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md",
    "required_source_porcelain_line": "?? 02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md",
    "required_tracking_state": "untracked",
    "required_sha256": "520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55",
    "cmp_required": true
  },
  "allowlisted_delta": {
    "porcelain_prefix": "?? \"Global Burden of Disease Study 2021 (GBD 2021) Bacterial Antimicrobial Resistance Burden Estimates 1990-2021 and Forecasts 2022-2050/",
    "required_default_entries": 1,
    "required_expanded_entries": 159,
    "required_tracking_state": "untracked",
    "other_delta_allowed": false
  },
  "live_status": {
    "default": {
      "line_count": 18,
      "sha256": "a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2"
    },
    "pointer_filtered_default": {
      "line_count": 17,
      "sha256": "d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd"
    },
    "expanded": {
      "line_count": 195,
      "sha256": "160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56"
    },
    "pointer_filtered_expanded": {
      "line_count": 194,
      "sha256": "f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b"
    }
  },
  "historical_reconstruction": {
    "filter_gbd_default": {
      "line_count": 17,
      "sha256": "4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c"
    },
    "filter_gbd_expanded": {
      "line_count": 36,
      "sha256": "f2492a704dff8d15031a2360ef97ad7a39e8d988830352ba628233ed00bc81ad"
    },
    "filter_pointer_and_gbd_default": {
      "line_count": 16,
      "sha256": "e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e"
    },
    "filter_pointer_and_gbd_expanded": {
      "line_count": 35,
      "sha256": "e002cc129aeea29aea4c61d059390535bf2f3332e48192b8dc5667bf588ef565"
    }
  },
  "release_gate": {
    "proof_type": "path_status_only_not_dirty_file_byte_identity",
    "proof_limit": "Path/status evidence only; no pre-phase byte manifest exists for paths already dirty at baseline.",
    "mismatch_result": "BLOCK",
    "required_checkpoints": [
      "task8_repair_pre_edit",
      "task8_repair_post_edit",
      "same_task8_reviewer_re_review",
      "merged_main_before_push"
    ],
    "forbidden_green_actions": [
      "modify the frozen baseline",
      "modify or weaken the existing validator",
      "modify, rename, remove, stage, or commit the GBD paths",
      "modify, stage, or commit the reciprocal pointer",
      "modify, stage, or commit any Surveillance_AMR path"
    ]
  }
}
```

## Exact Read-only Amended Gate Command

Run this command at every checkpoint named by the contract. It performs no external write and exits nonzero on the first mismatch.

```bash
python3 - <<'PY'
from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess


SOURCE = Path("/Users/hongchaokun/Documents/PhD/Surveillance_AMR")
LIBRARY_SEED = Path(
    "01_search/seed_scans/"
    "INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md"
)
SOURCE_SEED = SOURCE / (
    "02_source_registry/"
    "INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md"
)
POINTER = b"?? ID_EPI_METHODS_LIBRARY_POINTER.md"
SEED_STATUS = (
    b"?? 02_source_registry/"
    b"INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md"
)
GBD_PREFIX = (
    b'?? "Global Burden of Disease Study 2021 (GBD 2021) Bacterial '
    b'Antimicrobial Resistance Burden Estimates 1990-2021 and Forecasts '
    b'2022-2050/'
)
GBD_NEEDLE = b"Global Burden of Disease Study 2021 (GBD 2021)"


def fail(message: str) -> None:
    raise SystemExit(f"AMENDED EXTERNAL RELEASE GATE FAIL: {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def git(*args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(SOURCE), *args],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout


def split_status(raw: bytes) -> list[bytes]:
    require(not raw or raw.endswith(b"\n"), "porcelain output lacks final newline")
    return raw.splitlines()


def rebuild(lines: list[bytes]) -> bytes:
    return b"".join(line + b"\n" for line in lines)


def measure(raw: bytes) -> tuple[int, str]:
    return len(split_status(raw)), hashlib.sha256(raw).hexdigest()


default = git("status", "--porcelain=v1")
expanded = git("status", "--porcelain=v1", "--untracked-files=all")
default_lines = split_status(default)
expanded_lines = split_status(expanded)
pointer_default = rebuild([line for line in default_lines if line != POINTER])
pointer_expanded = rebuild([line for line in expanded_lines if line != POINTER])
gbd_default = [line for line in default_lines if line.startswith(GBD_PREFIX)]
gbd_expanded = [line for line in expanded_lines if line.startswith(GBD_PREFIX)]
require(
    all(not (GBD_NEEDLE in line) or line.startswith(GBD_PREFIX) for line in default_lines),
    "default GBD path is not exact untracked allowlist prefix",
)
require(
    all(not (GBD_NEEDLE in line) or line.startswith(GBD_PREFIX) for line in expanded_lines),
    "expanded GBD path is not exact untracked allowlist prefix",
)
without_gbd_default = rebuild(
    [line for line in default_lines if not line.startswith(GBD_PREFIX)]
)
without_gbd_expanded = rebuild(
    [line for line in expanded_lines if not line.startswith(GBD_PREFIX)]
)
without_pointer_gbd_default = rebuild(
    [line for line in default_lines if line != POINTER and not line.startswith(GBD_PREFIX)]
)
without_pointer_gbd_expanded = rebuild(
    [line for line in expanded_lines if line != POINTER and not line.startswith(GBD_PREFIX)]
)

expected = {
    "default": (18, "a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2"),
    "pointer_filtered_default": (17, "d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd"),
    "expanded": (195, "160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56"),
    "pointer_filtered_expanded": (194, "f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b"),
    "filter_gbd_default": (17, "4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c"),
    "filter_gbd_expanded": (36, "f2492a704dff8d15031a2360ef97ad7a39e8d988830352ba628233ed00bc81ad"),
    "filter_pointer_and_gbd_default": (16, "e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e"),
    "filter_pointer_and_gbd_expanded": (35, "e002cc129aeea29aea4c61d059390535bf2f3332e48192b8dc5667bf588ef565"),
}
observed = {
    "default": measure(default),
    "pointer_filtered_default": measure(pointer_default),
    "expanded": measure(expanded),
    "pointer_filtered_expanded": measure(pointer_expanded),
    "filter_gbd_default": measure(without_gbd_default),
    "filter_gbd_expanded": measure(without_gbd_expanded),
    "filter_pointer_and_gbd_default": measure(without_pointer_gbd_default),
    "filter_pointer_and_gbd_expanded": measure(without_pointer_gbd_expanded),
}
require(observed == expected, f"status view mismatch: {observed!r}")
require(len(gbd_default) == 1, "default GBD allowlist count is not 1")
require(len(gbd_expanded) == 159, "expanded GBD allowlist count is not 159")
require(
    git("rev-parse", "HEAD").decode().strip()
    == "eb5d15656b8fe69a8359705c80125d695a1c0782",
    "source HEAD mismatch",
)
require(
    git("status", "--porcelain=v1", "--", "ID_EPI_METHODS_LIBRARY_POINTER.md")
    == POINTER + b"\n",
    "pointer status mismatch",
)
require(
    git("ls-files", "--stage", "--", "ID_EPI_METHODS_LIBRARY_POINTER.md") == b"",
    "pointer is present in the index",
)
require(
    git(
        "status",
        "--porcelain=v1",
        "--",
        "02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md",
    )
    == SEED_STATUS + b"\n",
    "seed source status mismatch",
)
source_seed_bytes = SOURCE_SEED.read_bytes()
library_seed_bytes = LIBRARY_SEED.read_bytes()
required_seed_sha = "520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55"
require(hashlib.sha256(source_seed_bytes).hexdigest() == required_seed_sha, "source seed SHA mismatch")
require(hashlib.sha256(library_seed_bytes).hexdigest() == required_seed_sha, "library seed SHA mismatch")
require(source_seed_bytes == library_seed_bytes, "seed cmp mismatch")

print("AMENDED EXTERNAL RELEASE GATE PASS")
print("source_head=eb5d15656b8fe69a8359705c80125d695a1c0782")
for name, (count, digest) in observed.items():
    print(f"{name}={count}/{digest}")
print("allowlisted_gbd_entries=default:1 expanded:159")
print("pointer=untracked index_absent:true")
print(f"seed=untracked sha256:{required_seed_sha} cmp:equal")
print("proof=path/status only; not dirty-file byte identity")
PY
```

Expected output is exactly:

```text
AMENDED EXTERNAL RELEASE GATE PASS
source_head=eb5d15656b8fe69a8359705c80125d695a1c0782
default=18/a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2
pointer_filtered_default=17/d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd
expanded=195/160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56
pointer_filtered_expanded=194/f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b
filter_gbd_default=17/4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c
filter_gbd_expanded=36/f2492a704dff8d15031a2360ef97ad7a39e8d988830352ba628233ed00bc81ad
filter_pointer_and_gbd_default=16/e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e
filter_pointer_and_gbd_expanded=35/e002cc129aeea29aea4c61d059390535bf2f3332e48192b8dc5667bf588ef565
allowlisted_gbd_entries=default:1 expanded:159
pointer=untracked index_absent:true
seed=untracked sha256:520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55 cmp:equal
proof=path/status only; not dirty-file byte identity
```

---

### Task 1: Repair and re-review the existing Task 8 release receipt

This is a repair inside Task 8, not scientific Task 9.

**Files:**
- Create: `07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722.json`
- Modify: `07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md`
- Modify: `HANDOFF.md`

**Interfaces:**
- Consumes: owner approval, `DEC-20260722-010`, the independently reviewed amendment commit, original Task 8 base `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52`, implementation `70e5820dadf073cea19cc4fe7eb3f1bca377b269`, and the exact external state above.
- Produces: one static release-contract JSON, an honest verification addendum, and a handoff ready for the same Task 8 reviewer.

- [ ] **Step 1: Verify the repair preconditions and immutable bytes**

Run:

```bash
git status --short --branch
git branch --show-current
git merge-base --is-ancestor 70e5820dadf073cea19cc4fe7eb3f1bca377b269 HEAD
shasum -a 256 docs/superpowers/plans/2026-07-20-broad-methods-discovery-search.md
shasum -a 256 07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json
git log -1 --format=%H -- docs/superpowers/plans/2026-07-22-broad-discovery-external-release-contract-amendment.md
```

Expected: the worktree is clean on `codex/broad-methods-discovery`; the ancestry command exits `0`; the original plan SHA is `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`; the baseline SHA is `d1b48eb6c11b4e3701acfba5135bcd678ba101d44516b494f2e31d33f21b087b`; and the final command returns the exact 40-character amendment commit independently reviewed with no remaining Critical or Important findings. Any deviation blocks the repair.

- [ ] **Step 2: Run and record the nonpassing legacy validator**

Run:

```bash
set +e
legacy_output=$(python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR 2>&1)
legacy_exit=$?
set -e
printf 'legacy-validator-exit=%s\n%s\n' "$legacy_exit" "$legacy_output"
test "$legacy_exit" -eq 1
test "$legacy_output" = $'DISCOVERY FAIL\n- external filtered status mismatch'
```

Expected output:

```text
legacy-validator-exit=1
DISCOVERY FAIL
- external filtered status mismatch
```

The final two shell assertions validate faithful recording of the legacy result; they do not convert the underlying exit `1` into a validator pass.

- [ ] **Step 3: Capture the amended gate before any repair edit**

Run the exact read-only amended gate command above. Require the exact stated output and save its values for the verification-report pre-edit table. A mismatch blocks; do not edit any file to accommodate it.

- [ ] **Step 4: Create the static release contract and update the two Task 8 documents**

Create the JSON with the exact content under “Release Contract JSON Interface.” Append a section titled `## Owner-approved Task 8 external release-contract repair` to `07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md` that records:

1. owner approval date, `DEC-20260722-010`, amendment-plan path and resolved amendment commit;
2. the legacy validator command, exit `1`, and its exact two output lines, explicitly labelled `nonpassing legacy check`;
3. the complete pre-edit amended-gate output;
4. an exact pre/post table with the same eight named status views; enter the pre-edit values in this step and insert the post-edit values only after Step 5 runs;
5. the exact GBD prefix and 1/159 entry counts;
6. source HEAD, pointer/index, seed status/SHA/cmp, no-external-write statement, and the path/status-only proof limit;
7. that the same Task 8 reviewer must re-review `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52` through the repair head before whole-branch review.

Update `HANDOFF.md` so the live status says the owner-approved narrow amendment has been implemented for Task 8 and is awaiting the same Task 8 reviewer. Add the contract path, amendment-plan path, exact external constants, retained legacy exit `1`, and exact next action: re-review from original Task 8 base `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52` through the exact repair commit. Keep whole-branch review, merge, and push blocked until that reviewer returns `PASS — no remaining Critical or Important findings`.

Do not rewrite the historical legacy-validator evidence in either file. Add the amendment and current state explicitly.

- [ ] **Step 5: Capture the amended gate after all repair edits and prove exact equality**

Run the exact read-only amended gate command again. Its output must be byte-for-byte identical to the expected output and therefore identical to Step 3. Complete the report's post-edit table with the exact values. Record that equality covers all four live views, all four reconstructed views, GBD 1/159 counts, source HEAD, pointer/index, and seed status/SHA/cmp.

- [ ] **Step 6: Rerun every original Task 8 check under the amended interpretation**

Run:

```bash
python3 -m json.tool 07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722.json >/dev/null
python3 -m unittest 00_governance/tests/test_validate_library.py -v
python3 -m unittest 00_governance/tests/test_discovery_search.py -v
python3 00_governance/scripts/discovery_search.py validate-config --root .
python3 00_governance/scripts/discovery_search.py verify-all --root . --run-dir 01_search/search_logs/2026-07-20-broad-discovery
python3 00_governance/scripts/validate_library.py --root .
shasum -a 256 docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md
shasum -a 256 docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md
shasum -a 256 docs/superpowers/plans/2026-07-20-broad-methods-discovery-search.md
shasum -a 256 07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_BASELINE.json
shasum -a 256 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
cmp -s 01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md /Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md
git ls-remote origin refs/heads/main
git diff --check
git status --short --branch
```

Also rerun Step 2's legacy-validator command and the exact amended gate command. Expected: JSON parses; 25 Library tests and 95 discovery tests pass; `validate-config` and `verify-all` print `DISCOVERY PASS`; the Library validator prints `VALIDATION PASS`; immutable hashes remain design `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`, bootstrap plan `6302aca22c6b46ff0c473af1b7c487dbd974d7850264b92cd4013a1ecd4af3ec`, original broad plan `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`, external baseline `d1b48eb6c11b4e3701acfba5135bcd678ba101d44516b494f2e31d33f21b087b`, and seed `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`; seed comparison exits `0`; remote `main` remains `e161163d5ba3682395ca3e4846b81e355b7cd0b9`; whitespace check is silent; exactly the three named Task 8 repair paths are changed. The legacy validator remains exit `1` with its exact failure, and the amended gate prints `AMENDED EXTERNAL RELEASE GATE PASS`.

- [ ] **Step 7: Review the repair scope and commit**

Run:

```bash
git diff --name-only
git diff --check
git diff -- 07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722.json 07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md HANDOFF.md
git add 07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722.json 07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md HANDOFF.md
git diff --cached --name-only
git commit -m "repair Task 8 external release contract"
git status --short --branch
```

Expected: unstaged and staged path lists contain exactly the three named paths; the commit subject is exactly `repair Task 8 external release contract`; the worktree is clean after commit. Do not modify a review receipt or execution ledger in this repair commit.

- [ ] **Step 8: Return the complete Task 8 range to the same reviewer**

Resolve and print the exact range after the repair commit:

```bash
repair_head=$(git rev-parse HEAD)
test "$(git log -1 --format=%s "$repair_head")" = "repair Task 8 external release contract"
printf '%s..%s\n' 140b7f2cf725aa9f0ecb1369369a2432eb6f9b52 "$repair_head"
```

Expected: the test exits `0` and the printed range contains the exact 40-character repair commit returned by `git rev-parse HEAD`.

The reviewer must reread the approved design, original plan, this independently reviewed amendment, `TASK_8_REVIEW.md`, `TASK_8_REVIEW_PACKAGE.md`, the release-contract JSON, verification report, and handoff; rerun every original Task 8 check; record the legacy exit `1` honestly; run the amended gate; independently reconstruct all eight status views and GBD 1/159 counts; verify repair pre/post equality; and confirm no external write. Critical or Important findings return to the original Task 8 implementer. Whole-branch review begins only after the same reviewer records `PASS — no remaining Critical or Important findings` for the complete range and the normal Task 8 package/review/ledger receipt is committed under the original per-task gate.

## Unchanged Downstream Release Gates

After Task 8 passes, execute original Task 8 Steps 7 and 8 without any further interpretation change:

1. independent whole-branch base-to-head review and correction of every Critical or Important finding;
2. commit the whole-branch review receipt;
3. fast-forward only the reviewed branch when `main` is an ancestor;
4. on merged `main`, rerun every original Task 8 check, record the legacy external validator exit `1`, and rerun the exact amended gate against the same constants;
5. require merged-`main` external state to equal the Task 8 repair pre/post state exactly;
6. push only after local `HEAD`, `origin/main`, and live remote `refs/heads/main` equality is established.

Any merged-`main` mismatch blocks push. This amendment does not authorize merge, push, worktree removal, branch deletion, or any external mutation by its author or Task 8 repair implementer.
