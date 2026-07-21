# Task 5 fourth-repair scope-adjudication provenance

Date: 2026-07-21
Status: durable tracked provenance for the fourth-repair semantic replacement and dependent formal-audit recomputation; discovery classifications only.

## Authority and frozen scope

The reviewed Task 5 implementation is `9d89eb7656dab1acd576cb543070cb3b6dd5eb20`. The fourth repair was dispatched from review checkpoint `51059b95ce846b24abc44fee24ce137d201a0d10`, whose direct parent is that reviewed implementation. The repair replaces only the semantic dispositions of the exact 48 records identified by fixed-head review; it does not reroute or reclassify any other semantic-universe row.

- Parent third-repair semantic universe: 8,984 rows (`W1` 6,237; `W2` 2,747), `.superpowers/sdd/task5_fix3/exhaustive_semantic_universe.json` / `20121c35624169c8a4743d3373140b64e8efb858ee213a583f7cea342f5fba8e`.
- Parent final semantic ledger: `.superpowers/sdd/task5_fix3/final_semantic_decisions.jsonl` / `7c6d6b9004ecd66869eec7b9d97d2720885d2021319b3d36111024dae1d615b8`.
- Ordered newline-terminated 48-key list: `.superpowers/sdd/task5_fix4/scope_keys.txt` / `9af5818c90c9644cf30e0006adce5ae65efca52bd7a548e2b5d4afb967b910d4`; `W1` 27 and `W2` 21.
- Decision-blind scope input: `.superpowers/sdd/task5_fix4/scope_input.json` / `247e1493551df722acc78ce470974780e572b2653ee6fd6175de6cc260b29a4a`.
- Scope manifest: `.superpowers/sdd/task5_fix4/scope_manifest.json` / `3f2709a2e31b189cfb4304aaf43e95c58fb2064cdf41e618cd6c1519c8b04694`; ordered record SHA256 `b46ec703b1fa5131db33d7d0bfbb1fbfc3d24e30a9614fa189cbe55683b6a71a`; ordered raw-record SHA256 `8000f1b215ef8a33d91a58a6ada1beb3c6bfecf68cea16e5410a714d1b9962bc`.
- Prompt/schema: `.superpowers/sdd/task5_fix4/scope_prompt.txt` / `58dff62789393d7e1a5c41528ff74ad284d3b0c6fb996bf4fe313ac8609a10fc`; `.superpowers/sdd/task5_fix4/scope_schema.json` / `7c275a432fb9ac2e50a4df92071932055f3ce04b461265a3a3ee0111b95294da`.
- Initial package receipt: `.superpowers/sdd/task5_fix4/PACKAGE_RECEIPT.json` / `780eb324524abf9f4367eef26e2c28c2286867b86599da64f8474bac89c8139b`.
- Immutable sources: Wave 1 `01_search/search_logs/2026-07-20-broad-discovery/wave_01_frozen_queries/compiled_candidates_raw.csv` / `70cc6adb6ce40ed5c678ba0901cf4a23b78f64e5839304cd89002a7b19c46ec4`; Wave 2 `01_search/search_logs/2026-07-20-broad-discovery/wave_02_synonym_expansion/compiled_candidates_raw.csv` / `1b16a66efe3bf850f23b523482c82f3c9c989dbf5cf81b3a0dcac3f73aec2011`. All 48 `source_row_sha256` values were recomputed from these files.

The scope manifest proves that reader inputs contain raw bibliographic records and identity/source hashes, but no named-finding designation, prior or current decision/reason, reviewer identity, locator/routing state, audit state, or five-example hint. The prompt contains the approved scope distinctions needed to separate transferable epidemiological reproducibility, method-comparison, diagnostic, genomic-epidemiology, simulation, and applied leads from product development or generic laboratory work.

## Collision-free execution and zero-adoption attempts

Every external attempt used `/Applications/Codex.app/Contents/Resources/codex`, `codex-cli 0.145.0-alpha.18`, model `gpt-5.6-sol`, reasoning effort `high`, and read-only sandbox. Every attempt had a frozen worklist with absent leaf output paths before execution.

- Attempt 1 worklist: `.superpowers/sdd/task5_fix4/reader_worklist_001.json` / `ba453191a5f18977d1dfcca32615b78fafa7ac5ecf386233f2cc963507d0019a`. Reader A session `019f8322-ff51-70f1-bf02-50c5ef8cd625` and Reader B session `019f8322-ff51-7d31-bb1d-8b2a740e5f11` returned no `output-last-message`; `.superpowers/sdd/task5_fix4/executions/reader_attempt_001/reader_a/SCOPE4-A-001.receipt.json` / `b22bc26752f398bc5fd39e638ebf5c3dda56fc3eecc483f277f6444490891eb1` and `.superpowers/sdd/task5_fix4/executions/reader_attempt_001/reader_b/SCOPE4-B-001.receipt.json` / `1cbd88bf7bca6ff9af1feed847cc748885b7e0008a65bab84daad2d13b862999` reject both in full with zero adoption.
- Attempt 2 worklist/package: `.superpowers/sdd/task5_fix4/reader_worklist_002.json` / `7db09a11d833e1a29a65afdd0fa03b41cda1f5a1501d6d1b4aed56d0dea26e50`; `.superpowers/sdd/task5_fix4/reader_retry_attempt_002/RETRY_PACKAGE_RECEIPT_002.json` / `266bbf7d228f6bbd78aa44ef476c4d556b318411122391ac7cbd7946103b7d6b`. Reader A session `019f8329-fe5f-7823-be75-2560c583e26b` was rejected in full for an identity/order mismatch at `PMID:33564871`; `.superpowers/sdd/task5_fix4/executions/reader_attempt_002/reader_a/SCOPE4-A-002.receipt.json` / `fccf442ef985220a7ad376e9621f1b79ee041e00c997abc0dddfbd2a6bac3d7d` records zero adoption. Reader B from this attempt was accepted.
- Attempt 3 worklist/package: `.superpowers/sdd/task5_fix4/reader_worklist_003.json` / `33a6814714a1276ffb052f48ef088034f896bc905d0dd9d832817181d828223f`; `.superpowers/sdd/task5_fix4/reader_retry_attempt_003/RETRY_PACKAGE_RECEIPT_003.json` / `61fac13c50e0c72ab25e2ce250502f4e6671b57c22ac3c2586815b006d1d9535`. It executed only the missing Reader A role and preserved the already accepted Reader B bundle.

## Accepted semantic executions

The accepted sessions are mutually disjoint and absent from the frozen prior-Task-5 inventories. Each accepted response passed strict schema, exact ordered coverage, identity/source SHA, allowed decision/code/type mapping, and record-specific-reason validation before adoption.

| Role / rows | Session and reviewer | Prompt / input / schema | Response | Receipt | Adoption |
|---|---|---|---|---|---|
| Reader A / 48 | `019f8330-bf5c-7c11-ae49-e8daabcce874`<br>`codex-cli-task5-fix4-reader-a-019f8330-bf5c-7c11-ae49-e8daabcce874` | `.superpowers/sdd/task5_fix4/reader_retry_attempt_003/scope_prompt_003.txt` / `58dff62789393d7e1a5c41528ff74ad284d3b0c6fb996bf4fe313ac8609a10fc`<br>`.superpowers/sdd/task5_fix4/reader_retry_attempt_003/scope_input_003.json` / `247e1493551df722acc78ce470974780e572b2653ee6fd6175de6cc260b29a4a`<br>`.superpowers/sdd/task5_fix4/reader_retry_attempt_003/scope_schema_003.json` / `7c275a432fb9ac2e50a4df92071932055f3ce04b461265a3a3ee0111b95294da` | `.superpowers/sdd/task5_fix4/executions/reader_attempt_003/reader_a/SCOPE4-A-003.response.json` / `1dcbc8df68d6b1e91a3ec74581d513275740091346feb37199cf2a58717bd670` | `.superpowers/sdd/task5_fix4/executions/reader_attempt_003/reader_a/SCOPE4-A-003.receipt.json` / `f82096fb7a71af538fdefeca3b8deba7f8c9c240ec0244552087968223feadd1` | accepted; 36 agreement rows supply Reader A reasons; 12 conflicts require resolver |
| Reader B / 48 | `019f8329-fe5f-7e01-8411-97a23b5514b8`<br>`codex-cli-task5-fix4-reader-b-019f8329-fe5f-7e01-8411-97a23b5514b8` | `.superpowers/sdd/task5_fix4/reader_retry_attempt_002/scope_prompt_002.txt` / `58dff62789393d7e1a5c41528ff74ad284d3b0c6fb996bf4fe313ac8609a10fc`<br>`.superpowers/sdd/task5_fix4/reader_retry_attempt_002/scope_input_002.json` / `247e1493551df722acc78ce470974780e572b2653ee6fd6175de6cc260b29a4a`<br>`.superpowers/sdd/task5_fix4/reader_retry_attempt_002/scope_schema_002.json` / `7c275a432fb9ac2e50a4df92071932055f3ce04b461265a3a3ee0111b95294da` | `.superpowers/sdd/task5_fix4/executions/reader_attempt_002/reader_b/SCOPE4-B-002.response.json` / `155a36fadfaf4dadb8d0acd8181328d6b68c825f3003e988c77f425a84294f90` | `.superpowers/sdd/task5_fix4/executions/reader_attempt_002/reader_b/SCOPE4-B-002.receipt.json` / `6ddc40e06122c4e4d6880177a23844e955c2f2840c18ba74174c3e94c3fdff22` | accepted; comparison only; no unilateral adoption |
| Blind resolver / 12 | `019f833b-2107-7290-8e35-f37c128955ba`<br>`codex-cli-task5-fix4-resolver-019f833b-2107-7290-8e35-f37c128955ba` | `.superpowers/sdd/task5_fix4/resolver_package/resolver_prompt_001.txt` / `3ca60436d18952e91bc55b7ec09d1c90d5ac0ae68273556e193f411f00b12701`<br>`.superpowers/sdd/task5_fix4/resolver_package/resolver_input_001.json` / `2def6e505faaac387748202864a4bea76c31d5eaefe984317a6d95de36739189`<br>`.superpowers/sdd/task5_fix4/resolver_package/resolver_schema_001.json` / `fce377b1ce75a3402e34600a84f68f85b00b9cf1b66f828d32106d9270b44639` | `.superpowers/sdd/task5_fix4/executions/resolver_attempt_001/resolver/SCOPE4-R-001.response.json` / `cc417ec42b9a8dcc36a50aee52ba839416264433611d0096cd72c53f88b81832` | `.superpowers/sdd/task5_fix4/executions/resolver_attempt_001/resolver/SCOPE4-R-001.receipt.json` / `55a86ec24f4a4533da6ee3b41ed66b88524678f8aabd8d3ce6c7b90673106c05` | accepted; all 12 conflict rows adopted |

Reader comparison: `.superpowers/sdd/task5_fix4/reader_pair_comparison.json` / `475b83457d45cc769f87fe2502fc9d8492df2b0fb33ae78a2accc70a5f4525ba`; 36 complete-triple agreements and 12 conflicts; ordered conflict-key SHA256 `ce42b0aa396aab1e051948f4f1551dc9f83df42817ef0886ebfa2c998551e1c9`. The resolver received raw records and scope only, not either reader's decision, reason, or identity. Its collision-free worklist is `.superpowers/sdd/task5_fix4/resolver_worklist_001.json` / `d19d4400933fed3d6efd9f891196add42cbee21fd20e1f6fb7ef7fbc6d2c61fa`; package receipt `.superpowers/sdd/task5_fix4/resolver_package/RESOLVER_PACKAGE_RECEIPT_001.json` / `1864d21cb999e11ecf7ec3cd1511de50caa35b7824c36eb549acba90b0560047`.

## Semantic adoption and exact replacement boundary

- Accepted 48-row ledger: `.superpowers/sdd/task5_fix4/final_48_semantic_decisions.jsonl` / `e5dd0e9e97e8114906ed62e38dfced3b8ee1b2720897e6e146cc09c662c72007`.
- Rebuilt 8,984-row semantic ledger: `.superpowers/sdd/task5_fix4/final_semantic_decisions.jsonl` / `3e93fb841462f6c38fbd31d0bff5ddf3d179007c534de877ef58a89a38c07006`.
- Semantic boundary proof: `.superpowers/sdd/task5_fix4/semantic_replacement_boundary_proof.json` / `36e013fceed1a4ccd63c263ca78250d9366af4f274f9d9bf448bbe1c1e55d67b`.
- Dry-run receipt: `.superpowers/sdd/task5_fix4/semantic_replacement_dry_run_receipt.json` / `5783ee3ee93eb1777ae7790092e2b358bcdfa356c8fcd7c13e96e1eda6006ed5`.
- Primary-application preflight/receipt: `.superpowers/sdd/task5_fix4/primary_application_preflight.json` / `ea4f42d05e05a37494639fe495cccd75f5802d7ee09bdd4f2874728e56f96821`; `.superpowers/sdd/task5_fix4/primary_application_receipt.json` / `d7d09a6414f3dec893b48e0628a3290cf85f0f3ceebbdbe980fd1e2a9e6f4cbf`.

Exactly 48 semantic rows were replaced; the other 8,936 rows are semantically identical by key and fields, and all 8,984 identity/source fields match the parent ledger. The fourth-repair outcomes are 16 applied seeds, 5 diagnostic/correction leads, 5 method-source leads, 16 simulation/mechanistic leads, and 6 exclusions. Thirty-six came from complete Reader A/B agreement and 12 from the fresh resolver. The rebuilt 8,984-row semantic ledger contains 4,308 applied seeds, 995 diagnostic/correction leads, 965 method-source leads, 1,756 simulation/mechanistic leads, and 960 exclusions.

The 48-row scope intersects none of the 192 Wave 2 identifier-only duplicates. All 192 retain deterministic Wave 2 `exclude / blank type / X_DUPLICATE` primaries; the six identifier-overlap rows inside the 8,984-row semantic universe remain held at that identifier layer during primary application.

### Named fixed-head outcomes

| Candidate | Accepted primary triple | Route | Current final state |
|---|---|---|---|
| `PMID:41665488` | `include_simulation_or_mechanistic_lead / method_source / I_SIMULATION_MECHANISTIC` | fresh resolver | same triple; not audit-selected |
| `PMID:32928108` | `include_simulation_or_mechanistic_lead / method_source / I_SIMULATION_MECHANISTIC` | Reader A/B agreement | same triple; not audit-selected |
| `PMID:38823290` | `include_simulation_or_mechanistic_lead / method_source / I_SIMULATION_MECHANISTIC` | Reader A/B agreement | same triple; not audit-selected |
| `PMID:40883247` | `include_simulation_or_mechanistic_lead / method_source / I_SIMULATION_MECHANISTIC` | fresh resolver | same triple; not audit-selected |
| `PMID:40893944` | `include_simulation_or_mechanistic_lead / method_source / I_SIMULATION_MECHANISTIC` | fresh resolver | same triple; not audit-selected |
| `PMID:41540427` | `include_simulation_or_mechanistic_lead / method_source / I_SIMULATION_MECHANISTIC` | fresh resolver | same triple; not audit-selected |

The five unambiguous records therefore no longer carry `X_DESCRIPTIVE_ONLY`. The explicitly borderline `PMID:41540427` was not forced; the fresh resolver classified its sequencing/assembly workflow comparison as an eligible reproducibility and surveillance-method lead.

## Dependent formal-audit recomputation

The first local selection/reuse attempt used an incorrect expected complete-primary count and was rejected before any external execution or adoption. Its immutable zero-adoption receipt is `.superpowers/sdd/task5_fix4/formal_audit_failed_001/FAILED_ATTEMPT_RECEIPT.json` / `5d0bdec0f684c50de11a9c64c8d036d72abcbb753a460e4d93acac741fc8c67a`.

The corrected deterministic audit selection contains 2,535 rows: `W1` 1,653 and `W2` 882. The complete ordered `(wave, candidate_key)` SHA256 is `e17aa6a335b36bb0d771063c897b915b78be518a13ad30f70e97e6fa0aebb3c8`; selection receipt `.superpowers/sdd/task5_fix4/formal_audit/selection_receipt.json` / `7d372cd6d817de97773796448805df786d8b20460743e1e28caed7845d9c6637`. The decision-blind complete input is `.superpowers/sdd/task5_fix4/formal_audit/complete_selected_input.json` / `1a55e846612f3590ce6d51e7ca7e3fb9f49be88331d0a3adea23df3249830a3c`.

Relative to the definitive 2,542-row identity-preserved third-repair audit, 2,529 rows were reusable, 6 required fresh audit, and 12 were no longer selected. Reuse required exact equality of source SHA, primary decision/reason/type triple, primary reviewer, and selection membership, plus reviewer independence. The per-row proof ledger and reused decisions are `.superpowers/sdd/task5_fix4/formal_audit/audit_reuse_proof_ledger.json` / `f015fbfd73af43137b20b214852e5a12ad835c9c242c4c351996e0c5f26e0540` and `.superpowers/sdd/task5_fix4/formal_audit/reused_audit_decisions.jsonl` / `853ebb9002192feff1e5c6f4e464b33c8cf2d9802b2b884779f18a2fcd1a5952`; reuse receipt `.superpowers/sdd/task5_fix4/formal_audit/audit_reuse_receipt.json` / `69a8bf2cb7e9eccc4e1c94f8ba37f6989fd031c66c392372f7e73b81a7149513`.

The six changed/newly selected rows were audited in one fresh, decision-blind session disjoint from all 490 known Task 5 sessions, including the fourth-repair semantic readers and resolver:

| Role / rows | Session and reviewer | Prompt / input / schema | Response | Receipt | Adoption |
|---|---|---|---|---|---|
| Fresh formal auditor / 6 | `019f8352-2d58-7863-8b00-abee72636170`<br>`codex-cli-task5-fix4-fresh-auditor-019f8352-2d58-7863-8b00-abee72636170` | `.superpowers/sdd/task5_fix4/formal_audit/fresh_package_001/fresh_audit_prompt_001.txt` / `800a31cf016c59fabae884440825302541c010cbdec317578cff44f067cbd767`<br>`.superpowers/sdd/task5_fix4/formal_audit/fresh_package_001/fresh_audit_input_001.json` / `823d45954dfe54c33c1f2d77aa427de34f74239e1de28551813955a009250769`<br>`.superpowers/sdd/task5_fix4/formal_audit/fresh_package_001/fresh_audit_schema_001.json` / `a7fba48af2447087d1bd0b32fdab5f9ff47b36a6bd09210e76e1dc4465b45ab5` | `.superpowers/sdd/task5_fix4/formal_audit/executions/fresh_attempt_001/FIX4-AUDIT-001.response.json` / `1d94672c9d8f827f932c0421be11cd31091d351e4bad5aeaabe25a5a45685048` | `.superpowers/sdd/task5_fix4/formal_audit/executions/fresh_attempt_001/FIX4-AUDIT-001.receipt.json` / `e0770df91609314af9415506f7dfb459c52ab8efdd3a2b3269c01100fff4221a` | accepted; all 6 adopted |

Fresh worklist/package receipt: `.superpowers/sdd/task5_fix4/formal_audit/fresh_audit_worklist_001.json` / `072c007694f2ca4347d922cef8d08a5575c974e1e182f979cf9c696ee0cf1bb3`; `.superpowers/sdd/task5_fix4/formal_audit/fresh_package_001/FRESH_AUDIT_PACKAGE_RECEIPT_001.json` / `fe6600924fa2cd7a71573738249b0b0baf0af61441608f3c57affe3b62c11844`.

Five fresh rows agreed. `W2|PMID:32473976` had primary `exclude / blank / X_COMMENTARY_ONLY` versus audit `exclude / blank / X_DESCRIPTIVE_ONLY`; it therefore remains `conflict_open` with final `uncertain_retrieve_primary / blank / U_PRIMARY_RECORD_NEEDED` and blank adjudicator. No mismatch was automatically resolved.

- Combined audit decisions: `.superpowers/sdd/task5_fix4/formal_audit/combined_audit_decisions.jsonl` / `397f13e7afda807bb23b1a68c47ca47629e5349c267b1bad8e8bf78c48561a95`.
- Auditor-session map: `.superpowers/sdd/task5_fix4/formal_audit/auditor_session_map.json` / `a36a6ed398c4d49f91fa50e6ff21530a76495631adc55f5b6ec862b80b37a8d7`; 35 unique accepted audit sessions (34 reusable prior sessions plus the fresh session above).
- Formal-audit proof ledger: `.superpowers/sdd/task5_fix4/formal_audit/formal_audit_proof_ledger.json` / `f71bd8a5195ec33fef7c19297a2ea8b3482bba2c0d1e05ebcfcf16783c1547d1`.
- Merge preflight/render receipt: `.superpowers/sdd/task5_fix4/formal_audit/audit_merge_preflight.json` / `066f1b71337f87e2ac9311a45eff0f4e72fbaeff61ea4479ff24d6e40f27950c`; `.superpowers/sdd/task5_fix4/formal_audit/render_receipt.json` / `782eb270bfa09843ef5788865cf8983f925ea50df7f5546f7616b5d7bebd93de`.

The final formal audit has 1,647 complete agreements and 888 open conflicts: Wave 1 1,032/621 and Wave 2 615/267. Every mismatch is open, final uncertain, and blank-adjudicator.

## Authoritative regenerated files and counts

Primary and final rows remain complete (`W1` 7,146; `W2` 3,571). Exactly 29 batch CSVs changed: Wave 1 batches `010, 015, 016, 020, 025, 026, 031, 033, 034, 035, 036, 042, 043, 045, 046, 047, 048`; Wave 2 batches `001, 004, 005, 007, 009, 010, 011, 014, 016, 020, 021, 022`. Their individual hashes are frozen in the regenerated wave manifests.

| Artifact | SHA256 | Current counts |
|---|---|---|
| Wave 1 `screened_candidates.csv` | `699eb12f8d746fd559d048875ee8b96afda36394e4882d313ce6d6907012d62c` | final: 2,892 applied; 623 diagnostic/correction; 673 method; 1,213 simulation/mechanistic; 1,124 exclude; 621 uncertain |
| Wave 1 `screening_audit.csv` | `08316f05366e27c54ec03ab10b3de1faea843dfe23d71468a976e4378eafd671` | 1,653 rows; 1,032 agreement; 621 open |
| Wave 1 `MANIFEST_SHA256.json` | `5eae2041ee03bd6f6bdfec01a94c3f72b9f9231a3699a78c5407e0fd46428890` | 169 entries |
| Wave 2 `screened_candidates.csv` | `19c48b7b27b8ce79fc49f9cfa66bbcbcf226b1f1c625ba17cb98223c8b0db5d6` | final: 1,333 applied; 297 diagnostic/correction; 248 method; 500 simulation/mechanistic; 921 exclude; 272 uncertain |
| Wave 2 `screening_audit.csv` | `613e8476e8e9e39b11b956710c4010b0bc6e081cf2f4b6587d79239b3fc39ece` | 882 rows; 615 agreement; 267 open |
| Wave 2 `MANIFEST_SHA256.json` | `d61d218f7e9e551efb48adc338cbd620870c329f6259f35b6f0938da8fb107fa` | 81 entries |
| Global `candidates_through_wave_02.csv` | `fccb499f711bc7858f8f9ac1825d03877f169f3b80a5fcc9097e1390167102dd` | 10,525 unique keys; 192 cross-wave overlaps |

Wave 1 primary decisions are 2,923 applied seeds, 679 diagnostic/correction leads, 698 method-source leads, 1,246 simulation/mechanistic leads, 1,560 exclusions, and 40 primary-record uncertainties. Wave 2 primaries are 1,384 applied seeds, 316 diagnostic/correction leads, 266 method-source leads, 507 simulation/mechanistic leads, 1,093 exclusions, and 5 primary-record uncertainties.

## Historical audit-path correction

The superseded first third-repair package/complete input contains 2,544 rows, while the current bytes at `.superpowers/sdd/task5_fix3/formal_audit/selection_receipt.json` contain a later 2,542-row recomputation. `TASK_5_THIRD_REPAIR_PROVENANCE.md` now records the immutable 2,544-row complete-input, package, and combined-output hashes separately from the definitive identity-preserved 2,542-row paths. No historical artifact was overwritten for this correction.

## Claim and limitation boundary

These are title/abstract bibliographic discovery classifications, not verified substantive method claims, lineage determinations, software validations, data-feasibility findings, or promotion decisions. The 888 formal-audit disagreements explicitly remain unresolved pending primary-record retrieval or separately authorized adjudication. Reused audits were accepted only under per-row equality and independence proofs; reuse is not a new semantic read. This repair did not relax discovery gates, modify raw retrieval/query artifacts, change the approved design/plan/protocol, edit normalized registries or downstream cards/datasets/translations/simulations, modify `Surveillance_AMR`, or begin Task 6.
