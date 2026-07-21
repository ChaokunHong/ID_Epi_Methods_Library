# Task 6 Semantic Runtime Preflight Blocker

Date: 2026-07-21

Branch: `codex/broad-methods-discovery`

Tracked HEAD entering the blocker checkpoint: `a466095da7a49810102f63c2cefc0282d5c25d11`

## Verdict

**BLOCK — do not create or execute `frozen_002`.** The installed Codex runtime cannot presently prove that the semantic readers receive an empty model-callable tool set. Replacing that requirement with a post-hoc assertion that no tool call was observed would relax the predeclared gate and is not permitted.

Task 6 remains incomplete. Tasks 7 and 8 must not start. No formal Task 6 semantic output, lineage run, discovery registry row, implementation commit, or Task 6 PASS receipt exists.

## Independent review result

The third independent Task 6 preflight review examined tracked HEAD `a466095da7a49810102f63c2cefc0282d5c25d11`, pipeline SHA256 `47ed5559f7457daad30d1448f9e087669ef794d4d79b68ff0df5d1c962e8aac0`, and tests SHA256 `ad022731e8dff30ee1637acda1b5dea233b6b219d47a0005563c0178262868a9`. It returned **FAIL / ACK withheld: 0 Critical, 3 Important, 0 Minor**:

1. non-canary bulk QA was fail-open;
2. pure transport failure lacked a recoverable journal and made the same execution ID unsafe to retry;
3. the declared capability-empty runtime was not enforced by the actual Codex request.

The original Task 6 implementation agent fixed findings 1 and 2 with RED-to-GREEN tests. Finding 3 remains open because it cannot be closed through a supported configuration of the installed CLI.

## Frozen post-I2 implementation checkpoint

The implementation and tests remain ignored SDD artifacts and are not Task 6 production outputs:

- pipeline: `.superpowers/sdd/task6_semantic/semantic_pipeline_v2.py`
- pipeline SHA256: `ad1786eafbf6e5b9b076e86e5d3038ab96791a73446d50af6516bcd9a2aaa58f`
- tests: `.superpowers/sdd/task6_semantic/test_semantic_pipeline_v2.py`
- tests SHA256: `0ce8c55ca5dd5e3e61b62881db00d9c8d6644cade615cb7d80a41bd4e2e0138b`
- defined tests: 65
- I1/I2 focused verification: 4 tests, 20.033 seconds, `OK`
- existing bulk/resolver state-machine regressions: 2 tests, 112.586 seconds, `OK`

I1 now applies the same deterministic duplicate-rationale, invalid-evidence, and anomalous-primary-concentration gates to bulk reader A, reader B, and final outputs before completion or registry extension. Failure writes a signed zero-adoption substantive rejection and requires a fresh package version and fresh execution IDs.

I2 now distinguishes retryable transport failure from substantive invalidity, hashes partial-output evidence before safely removing non-adoptable partial files, permits the same execution ID to retry, and binds a signed per-execution transport journal into completion. Reader and resolver paths share this behavior; journal tampering prevents relaunch.

No full-suite PASS is claimed for the post-I2 checkpoint because launch finding I3 remains open. The prior exact-SHA baseline completed 61 tests in 596.602 seconds with `OK`; that baseline predates the I1/I2 repair.

## Runtime and request evidence

Installed production target:

- executable: `/Applications/Codex.app/Contents/Resources/codex`
- version: `codex-cli 0.145.0-alpha.18`
- executable SHA256: `f0b214b476e04175bee104fe441caea874baeef3efc3828bfb79e972266156a9`

The probes used an empty temporary working directory, an explicit `env -i` allowlist, `--ignore-user-config`, `--ignore-rules`, `--ephemeral`, `--strict-config`, `web_search="disabled"`, disabled apps, and every relevant supported feature disable. They sent the first Responses request to a loopback-only mock provider and did not submit project records to a model.

| evidence | request result | SHA256 | bytes |
|---|---|---|---:|
| `/tmp/id-epi-tools-request-18766.json` | fallback-model request retained `update_plan`, `request_user_input`, and `view_image`; `tool_choice=auto` | `c123439fe76d750286472beec85cc9e275f9d6870d63a3ee49f73cab6e906ff1` | 32621 |
| `/tmp/id-epi-tools-request-18770.json` | after the supported request-user-input gate was disabled, `update_plan` and `view_image` remained; `tool_choice=auto` | `4493d62e150ac9edb2b272eef20cf5da68d0764ef10d32eb2a02c779008abb83` | 30598 |
| `/tmp/task6_raw_http_capture_20260721_b.bin` | exact `gpt-5.6-sol` catalog path exposed `additional_tools`: `exec` with nested `apply_patch`/`update_plan`/`view_image`, `wait`, `request_user_input`, and collaboration tools | `19f9473262f9361a320a72b9ac00175beace74b6c07f349fb16a615a6be75421` | 38684 |
| `/tmp/task6_raw_http_capture_20260721_c.bin` | supported direct-mode catalog override still exposed `update_plan`, `request_user_input`, `view_image`, and collaboration tools | `7d02efb190e356061c1bc083ed85aa7b68369e395e4ba4fb97dc5604cd884ea7` | 33549 |

The raw loopback captures are temporary diagnostic evidence and are not committed because they include complete model-request context. This report records only their non-secret normalized findings, sizes, and hashes.

## Exact-version source verification

The official `openai/codex` tag `rust-v0.145.0-alpha.18` resolves to source commit `f84f9a6406cc55b210395f71b4c6aed236fc7ebb`. In `codex-rs/core/src/tools/spec_plan.rs`, `add_core_utility_tools` unconditionally adds `PlanHandler`, conditionally adds `RequestUserInputHandler`, and adds `ViewImageHandler` whenever a local execution environment exists. The exact-version `ToolsToml` supports the request-user-input gate but no built-in plan/view-image allow-none switch.

Live `--strict-config` checks rejected proposed built-in-tool keys including `tools.view_image`, `tools.update_plan`, `tools.request_user_input`, `tools.enabled`, and `tools.disabled_tools`. The older installed Homebrew CLI (`codex-cli 0.24.0`) sent a `shell` tool and lacks the required user-config/rules isolation, ephemeral execution, strict config, feature disables, and output-schema support. It is not an acceptable fallback.

## External boundary recheck

The Library validator passed at this checkpoint. The separate read-only `verify-external-boundary` check correctly failed with `external filtered status mismatch` because the live dirty `Surveillance_AMR` worktree acquired one additional untracked top-level status entry outside the authorized Library pointer action:

`?? "Global Burden of Disease Study 2021 (GBD 2021) Bacterial Antimicrobial Resistance Burden Estimates 1990-2021 and Forecasts 2022-2050/"`

Source HEAD remains `eb5d15656b8fe69a8359705c80125d695a1c0782`. Current default status has 18 lines at SHA256 `a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2`; after filtering only the authorized pointer it has 17 lines at SHA256 `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd`. Expanded status has 195 lines at SHA256 `160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56`; after filtering only the pointer it has 194 lines at SHA256 `f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b`.

A read-only delta reconstruction removed exactly that one default entry, and exactly its 159 expanded file entries, from the live status. The resulting four hashes exactly reproduced the prior receipts: default `4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c`, pointer-filtered default `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e`, expanded `f2492a704dff8d15031a2360ef97ad7a39e8d988830352ba628233ed00bc81ad`, and pointer-filtered expanded `e002cc129aeea29aea4c61d059390535bf2f3332e48192b8dc5667bf588ef565`. Thus every previously recorded status entry remains unchanged; this proof is status/path-only and does not establish byte identity. This Library checkpoint performed no write, stage, or commit action in `Surveillance_AMR`.

## Fresh checkpoint verification

- `python3 -m unittest 00_governance/tests/test_validate_library.py -v`: 25 tests in 0.094 seconds, `OK`.
- `python3 -m unittest 00_governance/tests/test_discovery_search.py -v`: 89 tests in 22.440 seconds, `OK`.
- `python3 00_governance/scripts/validate_library.py --root .`: `VALIDATION PASS`.
- `git diff --check`: pass.
- No `frozen_002` exists; all ten registries remain header-only.
- Design SHA256: `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`.
- broad-discovery plan SHA256: `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`.
- seed SHA256: `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55`; byte comparison with the named source returned `cmp=0`.
- local `main`, `origin/main`, and GitHub `refs/heads/main` all resolve to `e161163d5ba3682395ca3e4846b81e355b7cd0b9`.

The post-I2 semantic-pipeline tests are reported separately above. These repository tests do not close I3 and must not be used to authorize formal semantic execution.

## Safe resume gate

Task 6 may resume only through a separately reviewed execution-path decision that satisfies one of these conditions without weakening the gate:

1. a direct Responses API executor sends `tools=[]` (or omits tools), sets or proves `tool_choice=none`, exposes no `additional_tools`, and produces immutable request/runtime attestations; or
2. an installed and independently verified Codex CLI version supports a true built-in allow-none configuration, with a loopback capture proving no top-level tools, no dynamic/additional tools, and no inherited project/thread context.

The current environment has no `OPENAI_API_KEY`, so the direct API option adds a credential and authorization boundary. Updating or replacing the installed CLI is also an external runtime change. Either path requires owner direction and a focused reviewed amendment before execution.

Closing I3 alone is not sufficient. After the runtime amendment is implemented, the complete current 65-test suite must pass on the exact pipeline and test SHAs. The independent preflight reviewer must then re-review I1, I2, and I3 as one integrated package and issue ACK/PASS with no remaining Critical or Important finding. If the original reviewer is unavailable, a fresh independent reviewer must reconstruct the complete preflight review rather than review only the runtime delta. Only after that receipt exists may a new `frozen_002` be created or executed.

An event allowlist remains necessary but insufficient. It can prove that one run emitted only allowed message/reasoning lifecycle events; it cannot prove that the model was never given tool capability.

## Blocker-checkpoint review receipt

A fresh independent checkpoint reviewer, with a separate fresh specification-axis subreviewer, reviewed this report, `EXECUTION_LEDGER.md`, and `HANDOFF.md` against live artifacts, the approved plan/protocol, request captures, exact-version runtime source, repository tests, immutable hashes, Git/remote state, and the read-only external boundary. The first pass found one Important recovery-gate omission and two Minor terminology/ledger issues. All three were corrected, then re-reviewed.

Final checkpoint verdict: **PASS — 0 Critical / 0 Important / 0 Minor** on both spec/plan compliance and checkpoint quality.

This receipt accepts only the accuracy and recoverability of the blocker checkpoint. It does not change the underlying Task 6 preflight verdict of FAIL / ACK withheld, does not close I3, and does not authorize `frozen_002` or formal execution.
