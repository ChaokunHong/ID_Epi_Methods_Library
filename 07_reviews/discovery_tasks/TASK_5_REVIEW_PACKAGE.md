# Task 5 Review Package

## Review range

- Task: 5 — screen Wave 1 and execute, screen, audit, and reconcile the complete Wave 2 synonym expansion
- Base SHA: `961cdf859ad13f94abc1904d3b5bd8ed12913ae6`
- Original implementation SHA: `bf1a8d27a2eab227901f04af5d3b029799edf767`
- First repair SHA: `b167cb6fe583c4f3dce3a5e0dc22d3ae2a54d5a9`
- Root orchestration checkpoint SHA: `a7af704ad65219c65b7aebe529cc77e3de032292`
- Second repair SHA: `29ddc3b4f606c11d191e9a16620ac5ba817f19c2`
- Root second-review checkpoint SHA: `9056bf40aca4780c77ffbf32b3a4e952e87eb8c0`
- Third repair SHA: `9d89eb7656dab1acd576cb543070cb3b6dd5eb20`
- Exact head submitted for complete re-review: `9d89eb7656dab1acd576cb543070cb3b6dd5eb20`
- Required implementation subject: `screen broad methods discovery records`
- First repair subject: `repair Task 5 semantic screening scope`
- Second repair subject: `repair Task 5 semantic scope and provenance`
- Third repair subject: `repair Task 5 complete semantic scope`
- Initial diff package: `.superpowers/sdd/review-961cdf8..bf1a8d2.diff`
- Initial diff SHA256: `f54492223cf3a2de6da5fff8869e4c1b953a5dbf1f1fabd69c2555fcae0f57fb`
- Fixed full-range diff package: `.superpowers/sdd/review-961cdf8..29ddc3b.diff`
- Fixed full-range diff SHA256: `b220ef81a45fc27a472341994e1567c4cbdbe3dbb8acdea562a1a83ec868186d`
- Fixed full-range diff bytes: 22,665,060
- Fixed full-range commits: 4
- Third-repair full-range diff package: `.superpowers/sdd/review-961cdf8..9d89eb7.diff`
- Third-repair full-range diff SHA256: `756aa982a3da4eec7d51a434a4e6040fba6de56e37db879278d671f66b20c36e`
- Third-repair full-range diff bytes: 55,131,691
- Third-repair full-range commits: 6
- Implementer report: `.superpowers/sdd/task-5-report.md`
- Implementer report SHA256: `407674453ec6caba8a4520292ffc10fa390f857f39711fcb8f11e541518325a0`
- Current implementer report SHA256: `cf080446e0346c47a24f0fee20c5ed3d2757470be65516eeee00c844828a269e`
- Third-repair provenance: `07_reviews/discovery_screening/TASK_5_THIRD_REPAIR_PROVENANCE.md`
- Third-repair provenance SHA256: `7b2c674702e45fdc3eb50b05761722914bf06d11977a71f26736842aee7f0e74`
- Final verification receipt: `.superpowers/sdd/task5_fix3/final_verification_receipt.json`
- Final verification receipt SHA256: `1a98f7df65ab32acf4e597a04a7ee66f8bb558374e63f637fa9b98b9a09d4d40`
- Approved plan SHA256: `671f24a245c48a9c3661ecf176081f72948c5cdc0c3157df85d3781774ee4209`

## Exact scope

The complete `961cdf8..9d89eb7` range contains 193 paths: 190 additions and three modifications. The modified pre-existing paths are Wave 1 `MANIFEST_SHA256.json`, plus root-owned `HANDOFF.md` and `07_reviews/discovery_tasks/EXECUTION_LEDGER.md` in orchestration commits. The Task 5 implementation/repair paths remain confined to:

- Wave 1 primary batch manifests/CSVs, `screened_candidates.csv`, and `screening_audit.csv`;
- the complete Wave 2 query registry, receipt, raw PubMed pages, compiled candidates, primary batches, screening/audit ledgers, manifest, and narrow raw-XML `.gitattributes`;
- `global/candidates_through_wave_02.csv`;
- the planned `07_reviews/discovery_screening/*.md` implementation-evidence records plus second- and third-repair durable provenance records.

No paper, method, dataset, translation, simulation, or shortlist registry changed. No production code or test file changed. The exact base-to-head name/status list reports 190 `A` and three `M`; complete-range `git diff --check` is silent.

## Initial Wave 1 result at `bf1a8d2` (superseded)

- Raw baseline: 7,146 unique PMID candidates.
- Deterministic primary manifests: 48 (47 x 150; one x 96), exact ordered-key-list SHA256 `4462d9a531e910e5cc01896d960a3f8bedd570d58620fb4f5a3939a3a4ac2e4f`.
- Actual title/available-abstract semantic decisions: 7,146 / 7,146.
- Primary distribution: applied 2,911; method source 1,250; diagnostic/correction 794; simulation/mechanistic 1,239; exclude 911; uncertain 41.
- Corrected audit selection is the union of the plan's primary-family formula, the production validator's full-family formula, 100% uncertain and `X_NOT_INFECTIOUS_TRANSFERABLE`, and every possible-title-duplicate row.
- Plan-formula required: 1,442; validator-formula required: 1,504; formula union: 1,507; possible-duplicate additions: 52; final audit: 1,559 keys in 32 batches.
- Audit-key SHA256: `8bb3b09d236b1e964ebaa4845e0435225068d348f7de3fd7afd547c7e99d0b39`.
- Audit outcome: 912 exact triple agreements; 647 open conflicts; zero resolved or automatically resolved conflicts.
- Every open conflict ends as `uncertain_retrieve_primary` / `U_PRIMARY_RECORD_NEEDED` / blank type with blank adjudicator.
- Final distribution: exclude 613; applied 2,860; diagnostic 706; method 1,132; simulation 1,188; uncertain 647.
- `screened_candidates.csv` SHA256: `37558144c70051c0c0a8a6490181b2b3a5d828143e9ab2303ef92a1f5b94829b`.
- `screening_audit.csv` SHA256: `b681689d94cba02972081c854624f3422b61d25f383f804ef0dc49265b5e081a`.

The first fine-family-only audit selection was rejected before any audit row was imported after the root agent found that a finer-stratum top-ranked sample need not contain the plan's primary-family top-ranked sample. Three just-started sessions were interrupted with zero imported rows. The formal audit uses the union above and does not reuse those partial attempts.

## Initial Wave 2 result at `bf1a8d2` (superseded except immutable retrieval)

All six family rows are `executed` and cite inspected Wave 1 source keys for genuinely distinct labels: g-formula/g-computation; under-reporting; phylodynamic; EpiEstim; data fusion/evidence integration; and microsimulation. Every query retains the frozen infectious-disease and date blocks.

- Query registry SHA256: `05227366bcd08223483654af5075e67682d88ad5500f696bcd9fd9e08e4c1b04`.
- Run receipt SHA256: `fd55026aac0de98998f11a8abcfd436d4a72811ea43d24372e3f273c96499352`.
- Six source-reported query counts total 3,579.
- Deterministic compile: 3,571 unique PMID keys; SHA256 `1b16a66efe3bf850f23b523482c82f3c9c989dbf5cf81b3a0dcac3f73aec2011`.
- Exact Wave 1 identifier overlaps: 192; new semantic delta: 3,379.
- Primary coverage: 3,571 / 3,571 through 23 semantic manifests plus two exact-identifier-dedup manifests.
- Primary distribution: applied 1,464; diagnostic 390; method 322; simulation 539; exclude 850; uncertain 6.
- Corrected audit selection: plan required 782; validator required 790; formula union 790; duplicate-title additions 25; final 815 keys in 17 batches.
- Audit-key SHA256: `da0047c2709e3ba0dadfc51239bb5e44a07ef6c8f1c6f1811ab323045d2bec12`.
- Audit outcome: 536 exact triple agreements; 279 open conflicts; zero resolved or automatically resolved conflicts.
- Final distribution: applied 1,430; diagnostic 351; method 290; simulation 523; exclude 697; uncertain 280.
- `screened_candidates.csv` SHA256: `dcfeb03ee095659b837cd4f583ab77780f16cfa062502bcd2dfc661ce4d87e12`.
- `screening_audit.csv` SHA256: `614c9c28748a9ff2d672b349e2a3b67731506bd9ee3b0ebf8fed4a04cfadbb99`.

Wave 2 primary batch 011 had two transport stream disconnects inside one sampling session; the client reconnected automatically and only the final complete 150-row response was validated/imported. No partial transport output or hand-edited semantic row entered tracked artifacts.

## Cross-wave reconciliation and immutable baselines

- Global index: 10,525 unique identifier-level rows; SHA256 `89583437e78c4b71303ca8fefa34bc3f71de921e9159b416dd319d471a04b5bc`.
- Exactly 192 rows contribute to both waves. All 192 use `waves=wave_01|wave_02`, point to the Wave 1 screening path, retain both wave/source-row SHAs, and use `duplicate_disposition=screened_in_wave_01`.
- The other 10,333 rows have blank duplicate disposition.
- The production global validator's only deferred message is `global reconciliation missing`, whose reconciliation receipt is explicitly created in Task 7. Independent full-row Task 5 assertions cover every current global header, key, wave, SHA, screening path, final decision, and duplicate disposition.
- Wave 1 raw responses, search logs, `compiled_candidates_raw.csv`, `RUN_RECEIPT.json`, and `COUNT_RECONCILIATION.txt` have empty diffs from the Task 5 base.
- Wave 1 raw-list digest remains `4bb695152c772bfb15fdd8e63d367df4c81aaa7336998249604a7b33f3925244`; search-log digest remains `059ca974ae92b56c57a6b3f747a73d3e9907a1dbab32e9bd23a455b6b552b73b`; original 73-file baseline digest remains `122f26e0e9c53552029ff4154e626ad129b9a6a4e98a7539ff4f8beb1f0c84ef`.
- Wave 2's `.gitattributes` contains the same narrow raw-XML binary-diff rule as the owner-approved Wave 1 correction. It is manifested; raw XML remains protected by exact SHA and XML/count/receipt checks.

## First independent review and mandatory repair

The first independent review of `961cdf8..bf1a8d2` returned `NEEDS FIXES — 0 Critical / 2 Important / 0 Minor`.

1. `PMID:20826636` was falsely excluded as a duplicate of `PMID:21372330`. The former is the full Retracted Publication with DOI `10.1128/jcm.00920-10`; the latter is the distinct Retraction Notice with DOI `10.1128/jcm.00006-11`. Correction/retraction leads are in scope, and distinct bibliographic records may not be collapsed.
2. `I_SIMULATION_MECHANISTIC` had systematic scope drift: pure molecular docking, drug screening, structural biology, therapeutic/vaccine construction, and related non-epidemiological records were admitted merely because a pathogen or simulation was present. The approved simulation track is limited to estimator/diagnostic/decision/uncertainty work, reproducible analytical benchmarking, and mechanistic transmission/selection/surveillance/agent-based infectious-process modelling.

Commit `b167cb6fe583c4f3dce3a5e0dc22d3ae2a54d5a9` repairs both findings without changing a raw response, retrieval receipt, compiled raw table, count reconciliation, or normalized registry.

### Semantic repair corpus and independent decisions

- Exact conservative reread universe: 256 keys (Wave 1 205; Wave 2 51), selected from any primary/audit/final inclusion match plus the explicit false-duplicate pair.
- Universe file SHA256: `e118c48e685c7c69cb64fd1667e93ea1aed4ceaaddf7304e4b4389eb505228bd`.
- Ordered-record SHA256: `499feffa6c00fd722191fdf77d26ab43128b2becb2574fbbc6bcad9776097137`.
- Reader A: 256/256 actual title/available-abstract decisions; initial retain 138 / exclude 118; ledger SHA256 `73d32bdec8c898b7c0342b28f49e4655fc72f5bc49bcc6e01c617d2224c65b3a`.
- Independent Reader B: 256/256; retain 134 / exclude 122; combined JSONL SHA256 `bddff201849834311d4e8aae0cbe9b704f8946ff18374a5615f212857e97d9e2`.
- Exact A/B agreement: 231 triples; conflict: 25; conflict-ledger SHA256 `71ac47974b1b42bc83a95fe9ccb129211a89fd69b9f85052ff2a79c3158ddfe5`.
- A fresh blind adjudicator saw raw records and duplicate peers but no A/B labels. Its adopted 25-row response SHA256 is `7afcd19ca5069bbc2cac4fda8f74411f28d214040f4a2cddb8c364065275282f`.
- Repaired primary state in the 256-key universe: retain 132 / exclude 124 (Wave 1 86/119; Wave 2 46/5). Reader B agrees on 247 and differs on nine; no disagreement was silently resolved.

Rejected outputs are retained only in ignored evidence and contributed zero rows: a nonblind adjudicator; a blind prompt citing the wrong bootstrap plan; a blind response that misused `X_NOT_INFECTIOUS_TRANSFERABLE` and retraction status; and a provenance-invalid attempted reuse of an unrelated Task 3 reviewer. The final report names every rejection and its receipt/SHA.

### Repaired Wave 1 outcome

- Primary: applied 2,904; method source 1,223; diagnostic/correction 793; simulation/mechanistic 1,163; exclude 1,022; uncertain 41.
- Recomputed selection: plan 1,436; validator 1,499; formula union 1,502; duplicate additions 50; final 1,552 keys in 32 batches.
- Selection SHA256: `595995658afa924808305f7ed9567abd0623f43025ce4891b112401133a18aa7`.
- Audit provenance: 1,516 unchanged prior independent rows; 33 Reader B rows; three fresh CLI-session rows.
- Audit: 932 exact triple agreements; 620 open conflicts; zero resolved/automatic conflicts.
- Final: applied 2,853; method source 1,108; diagnostic/correction 706; simulation/mechanistic 1,119; exclude 740; uncertain 620.
- Screened SHA256: `32dd0d346960932be91bfafefd001783bd62fcef6e3aa1d7e21d69eed23b2e3a`.
- Audit SHA256: `1a4d0fd8706c2866e7355fe7fc254581de84a37bc3a509d9f27f471f8191f54f`.
- Manifest SHA256: `a9daab7994880a863276ce7c3e732069f5bb88e6234f4c7dfdcbe017370e3134`.
- `PMID:20826636` is now a distinct applied surveillance seed and `PMID:21372330` a distinct correction/retraction lead; both are audit agreements.
- Two evidenced preprint-to-journal duplicates are now explicit: `PMID:37131700` → `PMID:37934786` and `PMID:37873426` → `PMID:38271453`.

### Repaired Wave 2 outcome

- Immutable retrieval remains 3,579 source-reported results, 3,571 unique PMIDs, 192 exact Wave 1 overlaps, and 3,379 semantic delta keys.
- Primary: applied 1,466; method source 318; diagnostic/correction 390; simulation/mechanistic 536; exclude 855; uncertain 6.
- Recomputed selection: plan 785; validator 793; formula union 793; duplicate additions 25; final 818 keys in 17 batches.
- Selection SHA256: `ba97eb7492a2994a5085e51ebe88ab5cf3d8c6e2202492b39a220a1a71a765bc`.
- Audit provenance: 802 unchanged prior independent rows; 14 Reader B rows; two fresh CLI-session rows.
- Audit: 542 exact triple agreements; 276 open conflicts; zero resolved/automatic conflicts.
- Final: applied 1,431; method source 286; diagnostic/correction 353; simulation/mechanistic 521; exclude 703; uncertain 277.
- Screened SHA256: `ad7673b33102b536230f14bb2b3127cd88cd747a1442312e0023d231ebd3ce91`.
- Audit SHA256: `78145552cb283447e1d7df489b9359a964b4745ecf300ccc841ae911b52cc743`.
- Manifest SHA256: `876cd5c1fc01402d793ec13cbc6695ee96a5bdb993bc32d5cc3eb20e29ef0ec9`.

### Formal-audit independence and boundary proof

- Combined repaired audit: 2,370 rows; 1,474 agreements; 896 open conflicts; zero resolved conflicts.
- All 896 open conflicts end `uncertain_retrieve_primary` / `U_PRIMARY_RECORD_NEEDED` / blank type with blank adjudicator.
- Of 2,370 audit rows, 2,318 were reused only when source SHA, complete primary triple, primary reviewer, selection membership, independence, and semantic premise were unchanged; 47 came from Reader B; five newly selected keys came from a genuinely fresh app-bundled Codex CLI session.
- Fresh CLI session UUID: `019f7f90-90d4-7a83-98ff-be31b3067bd9`; reviewer identity `codex-cli-task5-formal-audit-019f7f90-90d4-7a83-98ff-be31b3067bd9`.
- Fresh five-row input SHA256: `b6e77bca5378c2f99f27b2ce71cdc76445caf95946e8b414a8e37d03d3a1a777`; response SHA256 `6a4e279be1de482234a17aa9130a7d36305ab1157f567b03172d308ed55d4ade`.
- Repaired global index remains 10,525 unique keys / 192 overlaps; SHA256 `ef35bf7f80a18ec0326b41f84222bc8df74edd8ed58f21838adec76baaee9fd9`.
- Boundary receipt covers 100 immutable discovery inputs and the exact 2,148-byte external porcelain status. It proves Wave 1 `raw/`, `search_logs/`, `compiled_candidates_raw.csv`, `RUN_RECEIPT.json`, and `COUNT_RECONCILIATION.txt` are byte-identical to `bf1a8d2`, and `Surveillance_AMR` status is unchanged.

## Validation evidence at fixed head

- Discovery plus legacy unit tests: 114 / 114 PASS.
- Wave 1 `verify`, `validate-screening`, and `validate-audit`: three `DISCOVERY PASS` results.
- Wave 2 `verify`, `validate-screening`, and `validate-audit`: three `DISCOVERY PASS` results.
- Library validator: `VALIDATION PASS`.
- Wave 1 and Wave 2 manifests contain 169 and 81 entries respectively; implementation rehash found no mismatch.
- Exact global assertions: PASS.
- Complete-range whitespace check: PASS.
- External-boundary validator: `DISCOVERY PASS`; the repair-specific 100-file/2,148-byte boundary verifier also passes.
- Worktree and index were clean at fixed head before this root-owned package was updated.

## Independent review checklist

The reviewer must independently check both specification compliance and task quality. At minimum:

1. inspect the full approved Task 5 text and exact 190-path diff, distinguish the root-owned orchestration checkpoint from implementation scope, and reject any scope outside the planned screening, Wave 2, global index, screening evidence, and approved orchestration paths;
2. recompute Wave 1 deterministic batch ordering/coverage, every source-row SHA, decision/code/type mapping, duplicate retention, and exact 7,146-key closure;
3. perform adversarial semantic spot checks across every decision class, every family, no-abstract rows, simulation/mechanistic rows, `X_NOT_INFECTIOUS_TRANSFERABLE`, title duplicates, and high-conflict strata; specifically reconstruct the 1,465-key second-repair universe, inspect both complete readers plus fresh blind adjudication, and test molecular docking/structural/vaccine/preclinical/host/product exclusions against genuinely epidemiological ABM, transmission, surveillance, estimator, diagnostic, decision, uncertainty, and benchmark inclusions;
4. recompute both current audit selections from scratch: the plan's primary-family strata and validator's full-family strata, both 100% classes, and all duplicate-group additions; prove reviewer independence per row, exact 1,561/830 key coverage, justified reuse of exactly 2,130 unchanged prior rows, 241 Reader B rows, 20 fresh-session rows, and zero falsely closed conflicts;
5. prove every primary/audit disagreement in both waves is open/final uncertain with blank adjudicator and that no open conflict can enter a registry;
6. verify every Wave 2 synonym against its cited Wave 1 titles/abstracts and the frozen Wave 1 family block, and confirm the infectious/date blocks and one-row-per-family schema;
7. independently parse/reconcile all Wave 2 ESearch/EFetch pages, receipt, manifest, compiled rows, query counts, 192 exact overlaps, 3,379 semantic delta keys, and identifier-only deduplication;
8. recompute the 10,525-row global index and all 192 overlap dispositions/paths/SHAs; confirm that only the Task 7 reconciliation receipt is deferred rather than using that deferral to hide a Task 5 coverage error;
9. rehash both manifests, prove Wave 1 locked paths byte-identical to the base, inspect the narrow Wave 2 `.gitattributes`, and prove no raw byte was rewritten to satisfy a diff gate;
10. rerun 114 tests, six wave validators, Library validator, external-boundary validator, complete-range `git diff --check`, and focused independent assertions;
11. inspect all original and repair rejected/retried-reader evidence described in `.superpowers/sdd/task-5-report.md` and `07_reviews/discovery_screening/TASK_5_SECOND_REPAIR_PROVENANCE.md`; confirm zero adoption from the nonblind, wrong-plan, invalid-reason-code, false-reviewer-provenance, identity/order-mismatch, and duplicate-only-evidence attempts, and verify every adopted blind/CLI receipt against its exact prompt, input, output, identity, UUID, and SHA;
12. confirm no registry promotion, flagship selection, systematic search claim, dataset download, or formal simulation occurred.

The owner's hard pause ended the active review turn, but the same independent reviewer identity was restored for `961cdf859ad13f94abc1904d3b5bd8ed12913ae6..29ddc3b4f606c11d191e9a16620ac5ba817f19c2`. It explicitly retested closure of all four prior Important findings and checked for regressions. Any remaining Critical or Important finding requires another focused fix and another complete fixed-range re-review.

## Fixed-head re-review result at `b167cb6` — superseded by required second repair

The fixed-head review independently reconstructed all 256 located repair keys and all 2,370 formal-audit provenance rows, and reran 114 tests plus every Wave, Library, external-boundary, repair-boundary, and whitespace validator successfully. It nevertheless returned `NEEDS FIXES — 0 Critical / 2 Important / 0 Minor` because semantic/provenance defects remain outside the mechanical validators:

1. The first locator was incomplete. At minimum, retained unaudited `PMID:33083025` (recombinant-vaccine mouse challenge), `PMID:38776389` (antiviral cell/mouse efficacy), and `PMID:22439282` (mouse foot-pad antigen screening) are preclinical or host-biology experiments rather than epidemiological estimator, diagnostic, decision, uncertainty, benchmark, transmission, selection, surveillance, or agent-based infectious-process methods. The second repair must expand only the locator, freeze its exact complete analogue universe, and semantically reread every located record; keyword matching may locate but never decide.
2. The adopted blind rows name nonexistent adjudicator `...task5_scope_adjudicator_blind_v2_protocol_rerun`. Live Codex session metadata identify session `019f7f7c-e7f5-79a1-b54c-d8dab3bf3115` as the single agent `...task5_scope_adjudicator_blind_v2`, and that same session emitted both the rejected response and the later adopted response. The second repair must use a genuinely fresh blind adjudicator, preserve its actual immutable identity/session, and commit durable prompt/input/output/receipt provenance rather than relying only on ignored scratch artifacts.

These findings were open at `b167cb6`. Commit `29ddc3b4f606c11d191e9a16620ac5ba817f19c2` is the bounded second repair now submitted for complete re-review. Task 5 still has no passing receipt, and Task 6 must not start until this exact head passes.

## Second repair result at `29ddc3b` — reviewed; third repair required

### Closure of Important 1: complete located semantic universe

- The locator inspected every Wave 1/2 row whose current primary or final decision was an inclusion, across every inclusion class rather than only simulation/mechanistic rows.
- Six conservative locator classes covered structural/product work, animal/challenge models, cell/laboratory work, product-development proximity, host-biology/physiology proximity, and assay/biosensor terms. Locator membership routed records only and never assigned a decision.
- The deterministic union also retained the old 256-record universe, all 25 invalid-provenance rows, and all three confirmed examples.
- Frozen universe: 1,465 unique `(wave, candidate_key)` rows; W1 1,011; W2 454.
- Universe SHA256: `c71762e584dc53771318bcb6899ffd26aab9c362dea73773df70b03a65839abb`.
- Ordered-record SHA256: `0e0acd5a50a6ed833ae0153934401daeba919cd713de361a6be54a76fe9e2ce4`.
- Ordered-entry SHA256, including exact locator reasons and current classes: `144e7fee78298266bfbd45ddc5bbf5810ec4e0fed6e53e9e9b344aa1eee62407`.
- Reader A and Reader B independently covered all 1,465 records in 20 read-only CLI sessions each. All 40 accepted UUIDs are unique, A/B reuse is zero, and combined output SHAs are `fc0ca4f2427719224448acfd53b26d52d85a180b7c8ce6e3d4798e4c2061a83a` and `4e51524aca1030af958b19dee0b9d680eda57616d65324f9750ca91f907da795`.
- Complete-triple comparison: 1,287 agreements and 178 conflicts. The 178 conflicts unioned with all 25 invalid-provenance rows yields 195 blind-adjudication keys because eight overlap.
- Four fresh blind adjudicator sessions covered all 195 keys with zero reader-session reuse and no A/B labels/decisions in their inputs. Combined adjudication SHA256: `7bb18b4c4c06ce6de2d611e8760fc8deb0d1f77d989f2cfdce54fbe60e67920b`.
- The three confirmed missed rows—`PMID:33083025`, `PMID:38776389`, and `PMID:22439282`—are now primary and final `exclude / X_DESCRIPTIVE_ONLY / blank type`, with A/B agreement.

### Closure of Important 2: real identity and durable provenance

- Zero tracked primary row retains nonexistent `...task5_scope_adjudicator_blind_v2_protocol_rerun`.
- All 25 rows previously carrying that alias were freshly adjudicated; zero old adopted rows survived.
- `07_reviews/discovery_screening/TASK_5_SECOND_REPAIR_PROVENANCE.md` is tracked at SHA256 `832e4f99916e3e7cf792cc9f77f48f51702b295153ec23b43ef5fe9d33a20cdd` and records exact executable/version/model, immutable UUID, prompt/input/output/receipt path and SHA, and adoption status for 45 accepted sessions and three rejected attempts.
- Accepted sessions comprise 40 readers, four blind adjudicators, and one fresh formal auditor. Three rejected whole responses—Reader A SCOPE2-020, Reader B SCOPE2-007, and blind BLIND2-001—have explicit zero-adoption receipts and were retried only under new UUIDs.
- The old true session `019f7f7c-e7f5-79a1-b54c-d8dab3bf3115` and real agent path are named only as invalid/superseded provenance, never as a current adopted reviewer.

### Recomputed formal audit and outputs

- W1 audit selection: 1,561; ordered-key SHA256 `4b82b712813c59ba073e9e4c4a99dd82c2e70329bd8598696d0938b84f674f39`; 982 agree, 579 open, zero resolved. Provenance: 1,384 unchanged prior rows, 166 Reader B rows, 11 fresh rows.
- W2 audit selection: 830; ordered-key SHA256 `fd303dbfcf79d152eea76d5e62df755761471420cd0f60651723d3580a45ae4f`; 565 agree, 265 open, zero resolved. Provenance: 746 unchanged prior rows, 75 Reader B rows, nine fresh rows.
- Combined formal audit: 2,391 selected; 1,547 agree; 844 open; zero resolved. Every disagreement remains final uncertain with blank type/adjudicator.
- Fresh 20-row formal-audit session UUID: `019f81fb-b235-74f2-9743-40be040cbd68`; response SHA256 `64f6fdf2902892c846f319ebd2e8041779146dc715c7897a190c1b44e0865a0b`; no reader/adjudicator UUID reuse.
- W1 screened/audit/manifest SHAs: `27fe02f20391a101e6ef5e57828a92c1306398a4e3b2f986c846ddbdb3b95e2b`, `2d22f008b30b35206f75abc92222d55b2881acce35fd7fda5bdd681f0fd8a5a5`, `d260c064b3b17e984d552af19c55a83bc30526fce4a6eea6c16760070807bd3d`.
- W2 screened/audit/manifest SHAs: `dc32a9b2fa2ae4cbeda9bbfa17d635c2db2c2519884f3eedcb6b6623fe271baa`, `d38d534251c371555c57f491705131ae78a1eee5578093921a35dac03cc0f814`, `b241579218b1ceb70e0805d3a1a63ff0fe7f4453701eafc572ab0980b63a6a8f`.
- Global index remains 10,525 unique identifier-level keys and 192 overlaps; SHA256 `83d320b315f3a26e83677725c2987a2ca6db401f9fd8c3f8a535ba4991949f16`.

### Fresh root verification at current head

- `test_discovery_search.py`: 89/89 PASS.
- `test_validate_library.py`: 25/25 PASS.
- Configuration, W1 verify/screen/audit, W2 verify/screen/audit, and external-boundary checks: eight `DISCOVERY PASS` results.
- Repository validator: `VALIDATION PASS`.
- Seed byte comparison: PASS.
- Complete `961cdf8..29ddc3b` diff check: PASS.
- Second-repair focused assertions: PASS for universe 1,465, two readers × 1,465, 178 conflicts, 195 adjudications, 2,391 formal-audit rows, and three confirmed examples.
- First repair boundary: PASS for 100 immutable files and 2,148 external-status bytes.
- Second repair boundary: PASS for 133 immutable/root-owned files, the pre-package root SHA, and external status.
- Post-implementation root-owned package update is expected and is outside the implementation boundary; the implementation itself preserved package SHA `2f5aef74f8077b04a1feb18f7858ff395bb208ae1e70de05aa002f34ac562cff`.

### Re-review requirements for this exact head

The reviewer must read the full `961cdf8..29ddc3b` diff and independently test both original and second-review findings. In addition to the earlier checklist, the reviewer must:

1. reproduce the 1,465-key locator universe and all three frozen hashes from raw/screened inputs; prove all current primary/final inclusion classes were eligible for location and no locator term made a decision;
2. verify exact 1,465/1,465 A/B coverage, 40 unique accepted reader sessions, two whole-response rejected reader attempts with zero adoption, 1,287 agreements, 178 conflicts, and the exact 195-key adjudication union;
3. inspect the four accepted blind inputs and prove they contain neither reader labels/decisions nor current/locator fields; verify BLIND2-001's rejected response contributed zero rows and its accepted retry has a new UUID;
4. verify every current adopted reviewer identity maps to a real accepted session and that the nonexistent alias count is zero; cross-check the tracked provenance table against exact session JSON events/receipts;
5. reconstruct W1/W2 formal-audit selections and all 2,391 per-row provenance classifications; prove the 20 fresh rows are decision-blind and the fresh auditor UUID is disjoint from all readers/adjudicators;
6. adversarially sample retained and excluded records across all locator classes, every family, and every inclusion class, including the three confirmed examples, genuine mechanistic transmission/selection/surveillance/agent-based work, analytical benchmarks, diagnostic measurement, and preclinical/host/product work;
7. rehash manifests/global output, prove all raw and out-of-scope paths unchanged, inspect the root orchestration commit separately from Task 5 implementation scope, and confirm no registry promotion or substantive claim verification occurred.

Any remaining Critical or Important finding requires another focused repair and complete fixed-range re-review. Task 6 remains blocked until the Task 5 review receipt records PASS.

## Independent review result at `29ddc3b`

The same independent reviewer completed the full `961cdf8..29ddc3b` re-review and returned `NEEDS FIXES — 0 Critical / 3 Important / 1 Minor`.

1. The 1,465-key locator is still incomplete. Seven retained rows outside it show the same out-of-scope therapeutic, host-physiology, molecular, or non-epidemiological method drift: `PMID:25450804`, `PMID:26014946`, `PMID:28358222`, `PMID:30221005`, `PMID:24731529`, `PMID:33024578`, and `PMID:28854802`. The third repair must independently scope-reread every still-retained inclusion rather than depend on a third keyword locator; keywords may never decide.
2. `PMID:21372330` is correctly distinct from `PMID:20826636` but is still misclassified `exclude / X_WRONG_RECORD_TYPE`. As a Retraction Notice that supplies correction information, it requires a correction-lead decision or honest uncertainty.
3. Root-owned `HANDOFF.md` and `EXECUTION_LEDGER.md` remained at `b167cb6`; root must advance continuity state before the next exact-head review.
4. Minor: three archived rejected receipts retain nine embedded paths that resolve to accepted retry files and therefore fail their adjacent SHAs. The archived bytes and tracked provenance are correct and zero rejected rows were adopted, but the paths must be corrected during the mandatory repair.

The reviewer independently reproduced the 1,465-key universe, all 45 accepted and three rejected real session UUIDs, the 2,391-row audit and its provenance split, both manifested waves, and the 10,525-row/192-overlap global index. It reran 114 tests plus 15 subtests, eight discovery checks, the Library validator, whitespace checks, and seed comparison successfully. These mechanical passes do not override the remaining semantic findings.

## Third repair result at `9d89eb7` — submitted for complete re-review

Commit `9d89eb7656dab1acd576cb543070cb3b6dd5eb20` is a bounded Task 5 repair with exact parent `9056bf40aca4780c77ffbf32b3a4e952e87eb8c0`. It addresses every finding from the `29ddc3b` review and makes no registry promotion, substantive verification claim, flagship selection, dataset download, or formal simulation.

- Exhaustive semantic universe: 8,984 `(wave, candidate_key)` rows, W1 6,237 and W2 2,747. It deterministically unions every current primary/final inclusion, every correction/retraction candidate, the prior 1,465-row universe, and all named findings/reviewer-axis examples. Universe SHA256: `20121c35624169c8a4743d3373140b64e8efb858ee213a583f7cea342f5fba8e`.
- Reader A and Reader B each independently read all 8,984 records in 240 accepted, unique, A/B-disjoint sessions. They agreed on 7,985 complete triples; all 999 disagreements were resolved by 20 fresh decision-blind sessions. No prior/rejected/interrupted session was reused.
- The final semantic ledger evaluates all 8,984 rows: 8,978 semantic dispositions adopted plus six W2 dispositions deliberately held at deterministic identifier-only deduplication. All 192 W1/W2 identifier overlaps remain W2 `exclude / blank type / X_DUPLICATE`, retaining the same key.
- The first 2,544-row formal-audit run was superseded with zero final adoption after the implementer detected the six identifier-layer overwrites. Its immutable artifacts remain auditable. A corrected 2,542-row selection—W1 1,656 and W2 886—was independently read from scratch in 34 fresh decision-blind sessions: 1,644 agreements, 898 open conflicts, zero resolved conflicts. Every mismatch remains final uncertain with blank type and adjudicator.
- `PMID:21372330` is now a distinct `include_diagnostic_or_correction_lead / correction / I_DIAGNOSTIC_CORRECTION` record. All seven previously missed records and both additional reviewer-axis records have explicit fresh semantic outcomes; the exact named results appear in `TASK_5_THIRD_REPAIR_PROVENANCE.md`.
- Prior rejected receipt paths were repaired without adopting rejected content. The tracked third-repair provenance records accepted, rejected, interrupted, retried, and superseded sessions with exact UUIDs, paths, SHAs, and adoption status.
- Post-commit verification receipt `1a98f7df65ab32acf4e597a04a7ee66f8bb558374e63f637fa9b98b9a09d4d40` records 17/17 PASS: 89 discovery tests plus five subtests; 25 Library tests plus ten subtests; config, both wave verifiers/screening/audit validators, Library validator, external boundary, seed `cmp`, focused verification, repair-boundary verification, and both diff checks.

### Required independent re-review at `9d89eb7`

The same independent reviewer must inspect the complete `961cdf8..9d89eb7` range, the 55,131,691-byte diff package, the current report, the tracked third-repair provenance, and live artifacts. The review must check both spec compliance and task quality and must independently:

1. retest every prior Critical/Important/Minor finding, especially complete semantic coverage, the Retraction Notice classification, continuity state, and repaired rejected-receipt paths;
2. reconstruct the 8,984-row universe and A/B/blind coverage, verify session disjointness and zero adoption from all rejected/interrupted/superseded attempts, and adversarially sample decisions across every family and inclusion/exclusion class;
3. reconstruct the corrected W1/W2 audit selection and all 2,542 audit rows, prove all 898 mismatches remain open/uncertain, and prove the superseded 2,544-row audit contributes zero final rows;
4. verify all 192 cross-wave identifier overlaps, the 10,525-key global index, manifests, immutable retrieval baselines, raw/out-of-scope boundaries, and unchanged `Surveillance_AMR` status;
5. rerun the full test and validator suite rather than accepting the implementer receipt alone.

Task 5 remains blocked until this reviewer returns `PASS — no remaining Critical or Important findings`. Any Critical or Important finding returns to the same implementation agent for a focused fix and another complete exact-head review.

## Independent review result at `9d89eb7`

The complete integrated re-review returned `NEEDS FIXES — 0 Critical / 1 Important / 0 Minor`. Standards/quality passed with 0/0/0; spec compliance found one Important semantic-scope defect.

Forty-eight rows were independently included by both fresh semantic readers and then excluded by the blind adjudicator. At least `PMID:41665488`, `PMID:32928108`, `PMID:38823290`, `PMID:40883247`, and `PMID:40893944` are unambiguous reproducibility or method-comparison discovery leads under the approved protocol. A fresh scope-specific adjudicator must re-review all 48 without treating the five named examples as an automatic decision rule. Dependent screening, audit, global, manifest, and provenance artifacts must then be regenerated and completely re-reviewed.

All prior Important and Minor findings were independently confirmed closed. All mechanical tests, validators, manifests, global/overlap reconstruction, seed comparison, and external-boundary checks passed. Task 6 remains blocked pending another complete fixed-head PASS.
