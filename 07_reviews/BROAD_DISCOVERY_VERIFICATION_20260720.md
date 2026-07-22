# Broad Discovery Verification Receipt

- Phase run: `01_search/search_logs/2026-07-20-broad-discovery`
- Verification started: `2026-07-22T16:10:52+08:00`
- Report assembled: `2026-07-22T16:21:34+08:00`
- Timezone: `Asia/Shanghai`
- Python: `Python 3.12.0`
- Git: `git version 2.50.1 (Apple Git-155)`
- Branch: `codex/broad-methods-discovery`
- Exact pre-receipt head: `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52`

## Scope and claim boundary

This receipt verifies the bounded broad-discovery and lineage-locating artifacts at the exact pre-receipt head. It is an implementation receipt for Task 8 Steps 1–5; it is not the independent Task 8 review receipt and not the whole-branch review.

This phase produced discovery leads and bibliographic-role records, not verified substantive method claims. It did not select a flagship, verify public-data feasibility, download candidate datasets, or execute a formal simulation.

The six coverage verdicts are bounded readiness judgments for primary-source verification. They are not claims of exhaustive, complete, or saturated discovery.

## Initial Task 8 command evidence

| Command | Exit | Exact captured result |
|---|---:|---|
| `python3 -m unittest 00_governance/tests/test_validate_library.py -v` | 0 | `Ran 25 tests in 0.077s`; `OK` |
| `python3 -m unittest 00_governance/tests/test_discovery_search.py -q` | 0 | `Ran 95 tests in 30.979s`; `OK` |
| `python3 00_governance/scripts/discovery_search.py validate-config --root .` | 0 | `DISCOVERY PASS` |
| `python3 00_governance/scripts/discovery_search.py verify-all --root . --run-dir 01_search/search_logs/2026-07-20-broad-discovery` | 0 | `DISCOVERY PASS` |
| `python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR` | 1 | `DISCOVERY FAIL`; `- external filtered status mismatch` |
| `python3 00_governance/scripts/validate_library.py --root .` | 0 | `VALIDATION PASS` |
| `git diff --check` | 0 | silent |
| `git status --short --branch` | 0 | `## codex/broad-methods-discovery` |
| four-file SHA command | 0 | all values shown under Immutable inputs |
| frozen-seed `cmp -s` | 0 | silent byte equality |
| second external-boundary invocation | 1 | same sole mismatch; no second diagnostic |
| `git ls-remote origin refs/heads/main` | 0 | `e161163d5ba3682395ca3e4846b81e355b7cd0b9 refs/heads/main` |

A first verbose 95-test invocation emitted item-level results but the tool display clipped its final summary. It is not used as PASS evidence; the fresh quiet invocation above is the authoritative captured completion.

## Immutable inputs and remote baseline

| Artifact | Last modifying commit | SHA256 |
|---|---|---|
| Approved design (`docs/superpowers/specs/2026-07-20-id-epi-methods-library-design.md`) | `c708ac2402431202c8b1af4c5fd87035460249ab` | `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57` |
| Bootstrap plan (`docs/superpowers/plans/2026-07-20-library-bootstrap-implementation.md`) | `9d38e235f031d0b5959e1d587ee28fe8d20a53de` | `6302aca22c6b46ff0c473af1b7c487dbd974d7850264b92cd4013a1ecd4af3ec` |
| Broad-discovery plan (`docs/superpowers/plans/2026-07-20-broad-methods-discovery-search.md`) | `155bf99eefa759d8c54bedeb78ef5d4a7908687c` | `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209` |
| Frozen seed (`01_search/seed_scans/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`) | `975f3ea43fb7d927b64028c2108c92e3db5a8b4f` | `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55` |

Seed byte comparison against `/Users/hongchaokun/Documents/PhD/Surveillance_AMR/02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`: exit 0.

- local `main`: `e161163d5ba3682395ca3e4846b81e355b7cd0b9`
- tracking `origin/main`: `e161163d5ba3682395ca3e4846b81e355b7cd0b9`
- live remote `refs/heads/main`: `e161163d5ba3682395ca3e4846b81e355b7cd0b9`
- branch merge-base with `main`: `e161163d5ba3682395ca3e4846b81e355b7cd0b9`; `main` is an ancestor of the branch.
- No merge or push was performed.

## Task 1–7 implementation, fix, and review receipts

| Task | Implementation commit | Fix commits | Reviewed head | Review receipt commit | Verdict |
|---:|---|---|---|---|---|
| 1 | `2da0eef6bf5fe6038548c64649b3ecc26025cdd8` | none | `2da0eef6bf5fe6038548c64649b3ecc26025cdd8` | `67cb499b0b7ad6d11755143e27e63da241e001c7` | PASS; 0 Critical / 0 Important / 0 Minor |
| 2 | `a4e323459bf14c567c11bbb5922542a5a8fb9937` | `802a4ff6e3c80f196ab02f0b7114488adeb34f62`<br>`7b0612624d55bb401b904123c2fd68680515b463`<br>`837dbbaadb6c949ce60760d7020d6d03a320a1d7` | `837dbbaadb6c949ce60760d7020d6d03a320a1d7` | `179059084eb655f7dc5ad6ac0bbfb8da67c01c0c` | PASS; 0 Critical / 0 Important / 0 Minor |
| 3 | `f8de39eb063ab0a436d8235c2c0a41212ca09956` | `3bae05606f74a2ac45787624fbce51029f3b5e5a`<br>`888cc2775315af40f317356488191c146071e53e` | `888cc2775315af40f317356488191c146071e53e` | `a7fa175944173ff6f1f17cfbfe767ee47e7a3375` | PASS; 0 Critical / 0 Important / 0 Minor |
| 4 | `4f76f6692f62ec94591628b5b78edd8d1fe03017` | `4b7248a98bb1d23e582d79fe6d6f1d8b2e68fe85`<br>`1f1b54169018b2d24353554eb1dc937d7d0b1cd2` | `1f1b54169018b2d24353554eb1dc937d7d0b1cd2` | `961cdf859ad13f94abc1904d3b5bd8ed12913ae6` | PASS; 0 Critical / 0 Important / 0 Minor |
| 5 | `bf1a8d27a2eab227901f04af5d3b029799edf767` | `b167cb6fe583c4f3dce3a5e0dc22d3ae2a54d5a9`<br>`29ddc3b4f606c11d191e9a16620ac5ba817f19c2`<br>`9d89eb7656dab1acd576cb543070cb3b6dd5eb20`<br>`b976d3baede36e7d82a1d9b86e57d48c0101f21a` | `b976d3baede36e7d82a1d9b86e57d48c0101f21a` | `44d6392996e1d53c438282c422ad35eb62f82539` | PASS; 0 Critical / 0 Important / 0 Minor |
| 6 | `b66102089630b9a10db2ee07bcd4dada0b898191` | `1b3a233549aa5473cfc95d7ca15030e982a2a1b8` | `1b3a233549aa5473cfc95d7ca15030e982a2a1b8` | `b2cc2d2d062d570ed5d6f2e18ee3c8d3519d4223` | PASS; 0 Critical / 0 Important / 0 Minor |
| 7 | `100ad236792ef0c0414eb1fe3e525b49c1a0a89b` | none | `100ad236792ef0c0414eb1fe3e525b49c1a0a89b` | `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52` | PASS; 0 Critical / 0 Important / 0 Minor |

Review-receipt commits were resolved live with `git log -1 --format=%H -- 07_reviews/discovery_tasks/TASK_N_REVIEW.md`.

## Query and configuration hashes

| Path | SHA256 |
|---|---|
| `01_search/search_protocols/2026-07-20-broad-methods-discovery-protocol.md` | `e3b1013862e2f18314702cbf1e1e0e5c2c6b9e0d2b78113b23b9e65e2ccb20df` |
| `01_search/search_protocols/discovery_queries.json` | `7e7e6bd7eeb4704e43ffa30e3c002a4ce5d044b5ac0c722fce7dd5d34f24a3e1` |
| `01_search/journal_registry/journals.csv` | `ef65e25ccb8ef1feb7220fc82c476bf2322c7e78db8fd1c05d463347aa688cc8` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/QUERY_REGISTRY.csv` | `05227366bcd08223483654af5075e67682d88ad5500f696bcd9fd9e08e4c1b04` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/LINEAGE_QUERY_REGISTRY.csv` | `8c9a2f35440801c6bfc0ec0be49d4b85227a5357665c30689d8498044573537b` |

## Retrieval, compilation, screening, and audit totals

| Scope | Root/query cells | Source-reported | Retrieved | Compiled/deduplicated | Screened | Audit sample | Audit agreement | Open audit conflicts |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Wave 1 | 12 | 7551 | 7551 | 7146 | 7146 | 1653 | 1032 | 621 |
| Wave 2 | 6 | 3579 | 3579 | 3571 | 3571 | 882 | 615 | 267 |
| Combined wave rows | 18 | 11130 | 11130 | 10717 | 10717 | 2535 | 1647 | 888 |
| Cross-wave identifier level | — | — | — | 10525 unique after 192 overlaps | 10525 reconciled | — | — | — |

### Screening decisions

- Wave 1 final decisions: exclude=1124; include_applied_seed=2892; include_diagnostic_or_correction_lead=623; include_method_source_lead=673; include_simulation_or_mechanistic_lead=1213; uncertain_retrieve_primary=621.
- Wave 1 final reason codes: I_APPLIED_TRANSFERABLE_DESIGN=2892; I_DIAGNOSTIC_CORRECTION=623; I_METHOD_SOURCE=673; I_SIMULATION_MECHANISTIC=1213; U_PRIMARY_RECORD_NEEDED=621; X_COMMENTARY_ONLY=54; X_DESCRIPTIVE_ONLY=647; X_DUPLICATE=3; X_NOT_INFECTIOUS_TRANSFERABLE=411; X_WRONG_RECORD_TYPE=9.
- Wave 2 final decisions: exclude=921; include_applied_seed=1333; include_diagnostic_or_correction_lead=297; include_method_source_lead=248; include_simulation_or_mechanistic_lead=500; uncertain_retrieve_primary=272.
- Wave 2 final reason codes: I_APPLIED_TRANSFERABLE_DESIGN=1333; I_DIAGNOSTIC_CORRECTION=297; I_METHOD_SOURCE=248; I_SIMULATION_MECHANISTIC=500; U_PRIMARY_RECORD_NEEDED=272; X_COMMENTARY_ONLY=28; X_DESCRIPTIVE_ONLY=429; X_DUPLICATE=200; X_NOT_INFECTIOUS_TRANSFERABLE=255; X_WRONG_RECORD_TYPE=9.
- Global identifier level final decisions: exclude=1853; include_applied_seed=4225; include_diagnostic_or_correction_lead=920; include_method_source_lead=921; include_simulation_or_mechanistic_lead=1713; uncertain_retrieve_primary=893.
- Global identifier level final reason codes: I_APPLIED_TRANSFERABLE_DESIGN=4225; I_DIAGNOSTIC_CORRECTION=920; I_METHOD_SOURCE=921; I_SIMULATION_MECHANISTIC=1713; U_PRIMARY_RECORD_NEEDED=893; X_COMMENTARY_ONLY=82; X_DESCRIPTIVE_ONLY=1076; X_DUPLICATE=11; X_NOT_INFECTIOUS_TRANSFERABLE=666; X_WRONG_RECORD_TYPE=18.

- Wave 1 audit status: agree=1032; conflict_open=621; not_selected=5493.
- Wave 2 audit status: agree=615; conflict_open=267; not_selected=2689.
- All 888 combined audit disagreements remain open and end as uncertain; none was automatically resolved.

## Search ID and source-reported count ledger

This table contains every executed ID: 12 Wave 1 roots, six Wave 2 queries, and 723 Wave 3 lineage queries (741 total). For PubMed lineage queries, retrieved count is the sum of manifested page parsed counts.

| Wave | Search/query ID | Source | Source-reported count | Retrieved/candidate count | Status |
|---|---|---|---:|---:|---|
| wave_01 | `SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01` | pubmed | 922 | 922 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01` | pubmed | 146 | 146 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01` | pubmed | 1251 | 1251 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01` | pubmed | 1316 | 1316 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01` | pubmed | 1416 | 1416 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01` | pubmed | 980 | 980 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-VENUE-CAUSAL-01` | pubmed | 279 | 279 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01` | pubmed | 155 | 155 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-VENUE-FORECASTING-01` | pubmed | 395 | 395 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-VENUE-SIMULATION-01` | pubmed | 255 | 255 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-VENUE-SPATIAL-01` | pubmed | 216 | 216 | complete |
| wave_01 | `SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01` | pubmed | 220 | 220 | complete |
| wave_02 | `SEARCH-20260720-PUBMED-FAMILY-CAUSAL-02` | pubmed | 141 | 141 | complete |
| wave_02 | `SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-02` | pubmed | 125 | 125 | complete |
| wave_02 | `SEARCH-20260720-PUBMED-FAMILY-FORECASTING-02` | pubmed | 43 | 43 | complete |
| wave_02 | `SEARCH-20260720-PUBMED-FAMILY-SIMULATION-02` | pubmed | 349 | 349 | complete |
| wave_02 | `SEARCH-20260720-PUBMED-FAMILY-SPATIAL-02` | pubmed | 1138 | 1138 | complete |
| wave_02 | `SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-02` | pubmed | 1783 | 1783 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-98` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-100` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-101` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-102` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-103` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-104` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-105` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-106` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-107` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-108` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-109` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-110` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-111` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-112` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-113` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-114` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-116` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-117` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-118` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-119` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-120` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-123` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-124` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-125` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-127` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-128` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-129` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-130` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-131` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-132` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-133` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-134` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-135` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-136` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-138` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-139` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-140` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-141` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-143` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-144` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-145` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-146` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-147` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-149` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-150` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-151` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-152` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-153` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-154` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-155` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-157` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-159` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-160` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-161` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-162` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-164` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-165` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-166` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-167` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-168` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-169` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-170` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-171` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-175` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-176` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-177` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-178` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-179` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-180` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-183` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-184` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-185` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-186` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-187` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-188` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-189` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-191` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-193` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-194` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-195` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-196` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-197` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-198` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-199` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-200` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-202` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-203` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-204` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-206` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-207` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-208` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-209` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-210` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-211` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-212` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-213` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-214` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-215` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-216` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-217` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-218` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-219` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-220` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-221` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-222` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-223` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-224` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-225` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-226` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-227` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-228` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-229` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-230` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-231` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-232` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-233` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-234` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-235` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-236` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-237` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-238` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-239` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-240` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-241` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-242` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-243` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-244` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-CAUSAL-245` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-100` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-101` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-102` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-103` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-104` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-107` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-108` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-109` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-111` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-112` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-114` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-115` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-116` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-117` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-118` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-119` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-120` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-122` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-123` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-126` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-129` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-131` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-132` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-133` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-134` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-135` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-136` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-137` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-138` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-139` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-140` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-141` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-142` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-143` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-144` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-145` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-146` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-149` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-150` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-151` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-152` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-153` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-154` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-155` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-156` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-157` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-158` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-159` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-160` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-161` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-162` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-163` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-164` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-165` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-166` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-167` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-168` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-169` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-170` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-171` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-172` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-173` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-174` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-176` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-177` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-178` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-179` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-180` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-181` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-182` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-183` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-184` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-185` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-186` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-187` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-188` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-189` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-190` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-191` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-192` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-193` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-195` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-196` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-197` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-198` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-199` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-200` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-201` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-202` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-203` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-204` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-205` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-206` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-207` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-208` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-209` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-210` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-211` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-212` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-213` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-214` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-215` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-216` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-217` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-218` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-219` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-220` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-221` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-222` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-223` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-224` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-225` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-226` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-227` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-228` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-229` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-230` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-231` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-232` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-233` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-234` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-235` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-236` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-237` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-238` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-239` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-240` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-241` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-242` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-243` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-244` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-245` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-246` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-247` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-248` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-249` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-250` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-251` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-252` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-253` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-254` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-255` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-256` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-257` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-258` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-259` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-260` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-261` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-262` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-263` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-264` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-265` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-266` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-267` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-268` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-269` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-270` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-271` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-272` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-273` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-274` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-275` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-276` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-277` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-278` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-279` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-280` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-281` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-282` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-283` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-284` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-285` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-286` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-287` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-288` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-289` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-290` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-291` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-292` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-293` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-294` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-295` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-296` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-297` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-298` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-299` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-300` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-301` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-302` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-303` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-304` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-305` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-306` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-307` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-308` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-309` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-310` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-311` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-312` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-313` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-314` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-315` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-316` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-317` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-318` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-319` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-320` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-321` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-322` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-323` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-324` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-325` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-326` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-327` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-328` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-329` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-330` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-331` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-332` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-333` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-334` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-335` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-336` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-337` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-338` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-339` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-340` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-341` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-342` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-343` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-344` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-345` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-346` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-347` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-348` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-349` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-350` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-351` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-352` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SURVEILLANCE-353` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-58` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-60` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-61` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-62` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-63` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-65` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-67` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-68` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-69` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-70` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-71` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-72` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-73` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-74` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-75` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-76` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-77` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-78` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-79` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-80` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-82` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-83` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-84` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-86` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-87` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-89` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-90` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-91` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-92` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-93` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-94` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-95` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-96` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-97` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-98` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-100` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-101` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-102` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-103` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-104` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-105` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-107` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-108` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-110` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-111` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-112` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-113` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-114` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-115` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-116` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-118` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-119` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-120` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-121` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-122` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-123` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-124` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-125` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-126` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-127` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-128` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-129` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-130` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-131` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-132` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-133` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-134` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-135` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-136` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-137` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-138` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-139` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-140` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-141` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-142` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-143` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-144` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-145` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-146` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-147` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-148` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-149` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-150` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SPATIAL-151` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-90` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-91` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-92` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-93` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-94` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-95` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-96` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-97` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-98` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-99` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-100` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-103` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-104` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-105` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-106` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-108` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-109` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-110` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-111` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-112` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-113` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-114` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-115` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-116` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-117` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-118` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-119` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-120` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-121` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-124` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-125` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-127` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-128` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-129` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-130` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-131` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-132` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-133` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-134` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-135` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-136` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-137` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-138` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-139` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-140` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-141` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-142` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-144` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-145` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-146` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-147` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-149` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-150` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-151` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-153` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-154` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-155` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-156` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-157` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-158` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-159` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-160` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-161` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-162` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-163` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-164` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-165` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-166` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-167` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-171` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-172` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-173` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-174` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-176` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-177` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-178` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-179` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-180` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-183` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-186` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-187` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-189` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-190` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-191` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-192` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-193` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-195` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-196` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-197` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-198` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-199` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-200` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-201` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-202` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-203` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-204` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-205` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-206` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-207` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-208` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-209` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-210` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-211` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-212` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-213` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-214` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-215` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-216` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-217` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-218` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-219` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-220` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-221` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-222` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-223` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-224` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-225` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-226` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-227` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-228` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-229` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-230` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-231` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-232` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-233` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-234` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-235` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-236` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-237` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-238` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-239` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-240` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-241` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-242` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-243` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-244` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-245` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-246` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-247` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-248` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-249` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-250` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-251` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-252` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-253` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-254` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-255` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-256` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-257` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-258` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-259` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-260` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-261` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-262` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-FORECASTING-263` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-60` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-61` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-62` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-63` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-64` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-67` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-68` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-69` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-70` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-73` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-75` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-76` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-78` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-79` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-83` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-87` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-88` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-89` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-90` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-91` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-92` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-93` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-94` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-95` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-96` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-97` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-98` | pubmed | 2 | 2 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-99` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-102` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-103` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-105` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-106` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-108` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-109` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-110` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-112` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-113` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-114` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-115` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-116` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-117` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-118` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-119` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-121` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-123` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-124` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-125` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-128` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-129` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-130` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-131` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-132` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-133` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-134` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-135` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-136` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-137` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-138` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-139` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-140` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-141` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-142` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-143` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-144` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-145` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-146` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-EVIDENCE-147` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-35` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-38` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-39` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-43` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-44` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-45` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-46` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-49` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-51` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-52` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-53` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-55` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-57` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-58` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-59` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-60` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-62` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-63` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-66` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-69` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-70` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-74` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-75` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-76` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-77` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-78` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-79` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-80` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-81` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-82` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-83` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-84` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-85` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-86` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-87` | pubmed | 0 | 0 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-88` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-89` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-90` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-91` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-92` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-93` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-94` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-95` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-96` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-97` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-98` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-99` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-100` | pubmed | 1 | 1 | complete |
| wave_03 | `SEARCH-20260722-LINEAGE-SIMULATION-101` | pubmed | 1 | 1 | complete |

## Family coverage and retained method concepts

| Family | Unique candidates | Retained | Applied | Method-source | Diagnostic/correction | Simulation/mechanistic | Canonical methods | Uncertain records | Unresolved lineage | Coverage verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| causal_policy | 1252 | 1236 | 998 | 88 | 86 | 64 | 61 | 148 | 0 | `adequate_for_primary_source_verification` |
| surveillance_measurement | 2911 | 1662 | 961 | 200 | 414 | 87 | 84 | 243 | 1 | `adequate_for_primary_source_verification` |
| spatial_transmission | 2618 | 2340 | 1644 | 242 | 64 | 390 | 32 | 160 | 2 | `adequate_for_primary_source_verification` |
| forecasting_dynamics | 1606 | 1198 | 437 | 307 | 185 | 269 | 46 | 163 | 0 | `adequate_for_primary_source_verification` |
| evidence_synthesis | 409 | 309 | 151 | 49 | 99 | 10 | 36 | 57 | 1 | `adequate_for_primary_source_verification` |
| simulation_methods | 1860 | 1034 | 34 | 35 | 72 | 893 | 18 | 138 | 0 | `adequate_for_primary_source_verification` |

Current global state is 7,779 retained records, 893 uncertain records, 1,853 exclusions, and 277 canonical discovery-state method concepts.

## Lineage query, identity, and role counts

- Wave 3 execution: 2026-07-22T11:30:22.684593+08:00 (Asia/Shanghai); 723/723 queries have status `complete`; source-reported total 634.
- Query sources: pubmed=723.
- Query families: causal_policy=128; evidence_synthesis=67; forecasting_dynamics=155; simulation_methods=49; spatial_transmission=84; surveillance_measurement=240.
- Query source roles: authoritative_candidate=190; correction=22; diagnostic=148; guidance=68; implementation=47; infectious_application=237; original_candidate=11.
- Candidate tables: PubMed=634; Crossref=0; unique manifested candidates=634.
- Named-source identity outcomes: ambiguous=2; resolved=616; unresolved_after_three_queries=2; conflicts: none=620.
- Lineage-ledger statuses: ambiguous=2; resolved_identity_role_unverified=616; unresolved_after_three_queries=2.
- Named-source roles: authoritative_candidate=171; correction=20; diagnostic=126; guidance=59; implementation=44; infectious_application=191; original_candidate=9.
- Assignment-level lineage roles: authoritative_candidate=1004; correction=35; diagnostic=939; guidance=252; implementation=205; infectious_application=4291; none=1031; original_candidate=22.
- Provisional relationship decisions: emit=6711; omit=1068.
- Emitted provisional relationship roles: <omitted>=1068; applies=4396; corrects=34; critiques=154; diagnoses=913; implements=197; originates=1017.
- All 620 lineage-ledger rows remain `verification_state=discovery`. The 6,711 emitted relationships remain provisional and outside the normalized authoritative link registry; 1,068 assignments are explicit omissions.

## Registry validation

The live Library validator returned `VALIDATION PASS`. Registry row counts are:

| Registry | Data rows |
|---|---:|
| `03_evidence_tables/candidate_dataset_links.csv` | 0 |
| `03_evidence_tables/candidate_method_links.csv` | 0 |
| `03_evidence_tables/methods.csv` | 277 |
| `03_evidence_tables/paper_method_links.csv` | 0 |
| `03_evidence_tables/papers.csv` | 7779 |
| `03_evidence_tables/simulation_candidate_links.csv` | 0 |
| `03_evidence_tables/simulation_method_links.csv` | 0 |
| `04_translation_candidates/translation_candidates.csv` | 0 |
| `05_data_registry/datasets.csv` | 0 |
| `06_simulation_lab/simulations.csv` | 0 |

The papers and methods registries contain discovery-state records. The other eight normalized registries are header-only.

## Manifest and artifact verification

The aggregate `verify-all` command returned `DISCOVERY PASS`. A separate live SHA-256 recomputation of every manifest entry found:

| Wave | Manifest entries | SHA mismatches | Manifest SHA256 |
|---|---:|---:|---|
| wave_01_frozen_queries | 169 | 0 | `5eae2041ee03bd6f6bdfec01a94c3f72b9f9231a3699a78c5407e0fd46428890` |
| wave_02_synonym_expansion | 81 | 0 | `d61d218f7e9e551efb48adc338cbd620870c329f6259f35b6f0938da8fb107fa` |
| wave_03_lineage_resolution | 1344 | 0 | `ffa418de2eb2d0017da8202f362f4080fe444c2ca1029bae9b54479fcbe473b7` |

Major live artifact hashes:

| Path | SHA256 |
|---|---|
| `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/RUN_RECEIPT.json` | `69d70bdfa3069aeb255ab0cff75cadbb687f6200651021efccde2530fb917dde` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/MANIFEST_SHA256.json` | `5eae2041ee03bd6f6bdfec01a94c3f72b9f9231a3699a78c5407e0fd46428890` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/compiled_candidates_raw.csv` | `70cc6adb6ce40ed5c678ba0901cf4a23b78f64e5839304cd89002a7b19c46ec4` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/screened_candidates.csv` | `699eb12f8d746fd559d048875ee8b96afda36394e4882d313ce6d6907012d62c` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/screening_audit.csv` | `08316f05366e27c54ec03ab10b3de1faea843dfe23d71468a976e4378eafd671` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/RUN_RECEIPT.json` | `fd55026aac0de98998f11a8abcfd436d4a72811ea43d24372e3f273c96499352` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/MANIFEST_SHA256.json` | `d61d218f7e9e551efb48adc338cbd620870c329f6259f35b6f0938da8fb107fa` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/compiled_candidates_raw.csv` | `1b16a66efe3bf850f23b523482c82f3c9c989dbf5cf81b3a0dcac3f73aec2011` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/screened_candidates.csv` | `19c48b7b27b8ce79fc49f9cfa66bbcbcf226b1f1c625ba17cb98223c8b0db5d6` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/screening_audit.csv` | `613e8476e8e9e39b11b956710c4010b0bc6e081cf2f4b6587d79239b3fc39ece` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/LINEAGE_RUN_RECEIPT.json` | `02f1ba3f3feedea38df35850feea5e04c0158aa393b7b8947a9cfcbe9131cc38` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/MANIFEST_SHA256.json` | `ffa418de2eb2d0017da8202f362f4080fe444c2ca1029bae9b54479fcbe473b7` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/pubmed_lineage_candidates.csv` | `fdb86fe0585e6cf2c5956f2ba01e9ad5e19bd22d301de4a44a8ce8b0d0bba3b5` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/crossref_candidates.csv` | `64a113a8c253204b422d1687062430cfa1a8c2a49a62774672f61b5d59c2a2d3` |
| `01_search/search_logs/2026-07-20-broad-discovery/wave_03_lineage_resolution/lineage_identity_audit.csv` | `977837ae51eb64e3ea572d0ba392bd01f68b1e883ba5c01c4b061295e2413b53` |
| `01_search/search_logs/2026-07-20-broad-discovery/global/candidates_through_wave_02.csv` | `fccb499f711bc7858f8f9ac1825d03877f169f3b80a5fcc9097e1390167102dd` |
| `01_search/search_logs/2026-07-20-broad-discovery/global/lineage_ledger.csv` | `f19655bf299bb1f7be8a469a9455c5afb5e967dc1904cb3ce6a74b40b16d631d` |
| `01_search/search_logs/2026-07-20-broad-discovery/global/discovery_relationships.csv` | `2a5942a861e51deb284386911b8f493e58159a30637bc08c9a0be93d041ced65` |
| `01_search/search_logs/2026-07-20-broad-discovery/global/coverage_matrix.csv` | `a7d8ecb9e0022bed3f0ec487f1227a06b5d5d29dbdb3a3240490caaeee8148df` |
| `01_search/search_logs/2026-07-20-broad-discovery/global/GLOBAL_KEY_RECONCILIATION.txt` | `9d9c4548ab97c0d5d2ac6c1803e95559f4444c017afd793339b01d9b5b855f1d` |

The global reconciliation receipt ends with `ALL WAVE, SCREENING, REGISTRY, AND LINEAGE KEYS RECONCILE`.

## External read-only boundary before Task 8 edits

- Capture time: `2026-07-22T16:10:52+08:00`; timezone `Asia/Shanghai`.
- Source HEAD: `eb5d15656b8fe69a8359705c80125d695a1c0782`.
- Default porcelain status: 18 lines; SHA256 `a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2`.
- Pointer-filtered default status: 17 lines; SHA256 `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd`.
- Expanded status: 195 lines; SHA256 `160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56`.
- Pointer-filtered expanded status: 194 lines; SHA256 `f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b`.
- Pointer status: `?? ID_EPI_METHODS_LIBRARY_POINTER.md`; pointer index paths: empty.
- Seed-source status: `?? 02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`.

The phase-start baseline was 16 pointer-filtered default lines with SHA256 `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e`. The later owner-owned untracked GBD directory makes the live validator return only `external filtered status mismatch`. The frozen baseline, validator, and external worktree were not changed to make this green.

This before capture is path/status evidence only; it is not dirty-file byte proof. The governing proof limit remains: Path/status evidence only; no pre-phase byte manifest exists for paths already dirty at baseline.

## Deferred work and explicit non-actions

- A fresh independent Task 8 reviewer must create the Task 8 package/review receipt and update the execution ledger. This implementation does not self-review.
- The separate whole-branch review, correction of any blocking findings, merge, full-gate rerun on main, push, and worktree/branch cleanup remain deferred.
- The next independent scientific plan is primary-source verification and complete method-card extraction, pending owner approval.
- The 893 uncertain screening records, two ambiguous identities, two unresolved-after-three-query identities, and 1,068 relationship omissions remain explicit work for that plan.
- Stage 3 method cards, authoritative normalized paper-method links, translation candidates, dataset access/licence/grain audits, portfolio ranking, candidate graduation, and any formal simulation remain deferred.
- The additional untracked GBD external status belongs to the owner. No GBD path, pointer, seed, frozen baseline, or external validator was modified.
- The bootstrap Minor about redundant validator-test wrappers remains non-blocking and deferred.
- No flagship was selected, no candidate dataset was downloaded, no public-data feasibility was verified, no formal simulation was executed, and no discovery-branch merge or push occurred.

## Post-edit fresh verification

The complete required gate was rerun after creating this receipt and updating `HANDOFF.md`.

| Command | Started/captured | Exit | Exact captured result |
|---|---|---:|---|
| `python3 -m unittest 00_governance/tests/test_validate_library.py -v` | `2026-07-22T16:24:25+08:00` | 0 | `Ran 25 tests in 0.065s`; `OK` |
| `python3 -m unittest 00_governance/tests/test_discovery_search.py -q` | `2026-07-22T16:24:35+08:00` | 0 | `Ran 95 tests in 33.421s`; `OK` |
| `python3 00_governance/scripts/discovery_search.py validate-config --root .` | post-edit | 0 | `DISCOVERY PASS` |
| `python3 00_governance/scripts/discovery_search.py verify-all --root . --run-dir 01_search/search_logs/2026-07-20-broad-discovery` | post-edit | 0 | `DISCOVERY PASS` |
| `python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR` | post-edit | 1 | `DISCOVERY FAIL`; `- external filtered status mismatch` |
| `python3 00_governance/scripts/validate_library.py --root .` | post-edit | 0 | `VALIDATION PASS` |
| four immutable SHA-256 checks | post-edit | 0 | design `e5fe20a5502c903b01cad98528991f81f23dface5eb6d51dd364074d15632c57`; bootstrap plan `6302aca22c6b46ff0c473af1b7c487dbd974d7850264b92cd4013a1ecd4af3ec`; broad plan `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`; seed `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55` |
| frozen-seed `cmp -s` | post-edit | 0 | silent byte equality |
| `git ls-remote origin refs/heads/main` | post-edit | 0 | `e161163d5ba3682395ca3e4846b81e355b7cd0b9 refs/heads/main` |

The external after-capture at `2026-07-22T16:26:40+08:00` reproduced the before-capture exactly:

| External view | Before lines / SHA256 | After lines / SHA256 | Result |
|---|---|---|---|
| default | 18 / `a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2` | 18 / `a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2` | identical |
| pointer-filtered default | 17 / `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd` | 17 / `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd` | identical |
| expanded | 195 / `160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56` | 195 / `160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56` | identical |
| pointer-filtered expanded | 194 / `f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b` | 194 / `f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b` | identical |

Source HEAD remained `eb5d15656b8fe69a8359705c80125d695a1c0782`; the pointer remained `?? ID_EPI_METHODS_LIBRARY_POINTER.md`, absent from the index; and the seed source remained untracked. This proves no Task 8 path/status change in the external worktree. It remains path/status proof only and is not dirty-file byte proof.

## Receipt boundary

This report intentionally does not create `07_reviews/BROAD_DISCOVERY_REVIEW_20260720.md`, a Task 8 review receipt, or a whole-branch review. The exact commit containing this report is resolved after commit with `git log -1 --format=%H -- 07_reviews/BROAD_DISCOVERY_VERIFICATION_20260720.md`; a file cannot embed the SHA of the commit that contains itself.

## Owner-approved Task 8 external release-contract repair

Chaokun Hong approved the narrow external release-contract amendment on 2026-07-22 under `DEC-20260722-010`. The governing amendment is `docs/superpowers/plans/2026-07-22-broad-discovery-external-release-contract-amendment.md`, last modified in reviewed amendment commit `d0d873abe08256184bd5028fde8cf1f2f020b576`; its durable independent PASS receipt is present at repository head `97cde95c43a1b65328478885cdaa3e2911e44248`. The resulting static contract is `07_reviews/external_boundaries/BROAD_DISCOVERY_SURVEILLANCE_RELEASE_CONTRACT_20260722.json`, byte-locked with trailing newline to SHA256 `6f7e7f71d300f820ef46e7ffc98bd54aa57061e566f187362f1c44ab07e05422`.

### Nonpassing legacy check retained honestly

Command:

```text
python3 00_governance/scripts/discovery_search.py verify-external-boundary --root . --source-root /Users/hongchaokun/Documents/PhD/Surveillance_AMR
```

Underlying exit: `1`. Exact output:

```text
DISCOVERY FAIL
- external filtered status mismatch
```

This is a **nonpassing legacy check** and is not relabelled as PASS. The owner-approved amendment requires that exact legacy result to remain visible and independently requires the amended gate below.

### Complete pre-edit amended-gate output

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

### Exact amended-gate pre/post status views

| Named status view | Pre-edit lines / SHA256 | Post-edit lines / SHA256 | Result |
|---|---|---|---|
| `default` | 18 / `a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2` | 18 / `a4ced68b5f0b91c3289b9e5c7a3d184556d8245bc6aeb7a516ffbe06f6cf2df2` | identical |
| `pointer_filtered_default` | 17 / `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd` | 17 / `d3273ff3b5aba70d91e72f06d59d65d1d83eafb3f0a3bd33f163e05d3cb6ebfd` | identical |
| `expanded` | 195 / `160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56` | 195 / `160824ab59e7e738689a76cb7c894ad473795b7eccac3b0bcf7a31a141125a56` | identical |
| `pointer_filtered_expanded` | 194 / `f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b` | 194 / `f3477c25000858130bd6d3d1dd2705f11d41556aa3a779806a33713a04040d4b` | identical |
| `filter_gbd_default` | 17 / `4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c` | 17 / `4e61e54d6671ef2b048e3d1967a90d0ff96524ac329689ea2aaaf4cb347f955c` | identical |
| `filter_gbd_expanded` | 36 / `f2492a704dff8d15031a2360ef97ad7a39e8d988830352ba628233ed00bc81ad` | 36 / `f2492a704dff8d15031a2360ef97ad7a39e8d988830352ba628233ed00bc81ad` | identical |
| `filter_pointer_and_gbd_default` | 16 / `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e` | 16 / `e756dbcdc0e0ab309ed1929ad1deeae1617e7d36a6389dec6ac49060775c9c6e` | identical |
| `filter_pointer_and_gbd_expanded` | 35 / `e002cc129aeea29aea4c61d059390535bf2f3332e48192b8dc5667bf588ef565` | 35 / `e002cc129aeea29aea4c61d059390535bf2f3332e48192b8dc5667bf588ef565` | identical |

The complete pre-edit and post-edit amended-gate outputs were byte-for-byte identical. Equality covers all four live views, all four reconstructed views, the GBD 1/159 counts and exact prefix, source HEAD, pointer/index state, and seed status/SHA/byte comparison.

The exact allowlisted porcelain prefix is `?? "Global Burden of Disease Study 2021 (GBD 2021) Bacterial Antimicrobial Resistance Burden Estimates 1990-2021 and Forecasts 2022-2050/`. The required and observed GBD entry counts are one default entry and 159 expanded entries; no other delta is allowed.

Source HEAD is `eb5d15656b8fe69a8359705c80125d695a1c0782`. The reciprocal pointer remains exactly `?? ID_EPI_METHODS_LIBRARY_POINTER.md` and absent from the index. The seed source remains exactly `?? 02_source_registry/INFECTIOUS_EPIDEMIOLOGY_PUBLIC_DATA_IDEA_SCAN_20260719.md`; source and Library copies both have SHA256 `520a634d7a876a7096ca8d19598c5de16785a71e27e6e58ae2fd62da6d791b55` and compare byte-equal. The repair made no external write and did not modify the pointer, GBD paths, seed source, frozen baseline, validator, original plan, search artifacts, registries, waves, reviews, or execution ledger.

Proof limit: Path/status evidence only; no pre-phase byte manifest exists for paths already dirty at baseline.

The same Task 8 reviewer must re-review the complete range from original Task 8 base `140b7f2cf725aa9f0ecb1369369a2432eb6f9b52` through the exact repair head before whole-branch review may begin. Resolve that head after commit with `git rev-parse HEAD`; whole-branch review, merge, and push remain blocked until the reviewer returns `PASS — no remaining Critical or Important findings`.
