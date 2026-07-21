# Wave 1 possible-duplicate review

Date: 2026-07-20; fourth-repair boundary refresh: 2026-07-21

The raw compiler created title-only possible-duplicate groups without collapsing them. There are 40 groups containing 81 PMID records. Primary readers compared available bibliographic metadata before using `X_DUPLICATE`; the third-repair independent audit then received every group member plus the other members' title, year, journal, authors, PMID, DOI, and source URL. The second-repair counts previously recorded here are historical and superseded. None of the exact 48 fourth-repair records belongs to a possible-title-duplicate group, so these rows and audit decisions were unchanged and passed the fourth-repair reuse proofs.

The authoritative fourth-repair Wave 1 primary ledger still assigns `X_DUPLICATE` to 64 rows overall, including 55 of the 81 possible-title-group rows. The independent audit assigns `X_DUPLICATE` to one possible-title-group row. Within the 81-row possible-title set, 22 complete primary/audit triples agree and 59 remain open conflicts; none ends with an agreed final `X_DUPLICATE` label. The full Wave 1 final ledger contains three `X_DUPLICATE` rows outside these title-only groups. No key was collapsed or deleted.

Identifier-only cross-wave reconciliation is a separate layer. All 192 exact Wave 1/Wave 2 key overlaps remain deterministic Wave 2 `exclude / blank type / X_DUPLICATE` primaries retaining the identical key. The fourth-repair semantic set intersects none of them. Forty-eight were independently audited and all 48 agreed; the remaining 144 were outside the formula selection. Thus all 192 remain final Wave 2 `X_DUPLICATE` exclusions, while the global index still preserves them as Wave 2 provenance overlaps.

The third repair resolves `TITLE-DUP:59dc520eb78ae555` as two distinct records. `PMID:20826636` is the original retracted Candida surveillance study with DOI `10.1128/jcm.00920-10`; its primary and audit agree on `include_applied_seed / applied_seed / I_APPLIED_TRANSFERABLE_DESIGN`. `PMID:21372330` is the distinct Retraction Notice with DOI `10.1128/jcm.00006-11`; its primary and audit agree on `include_diagnostic_or_correction_lead / correction / I_DIAGNOSTIC_CORRECTION`. Neither carries a `retained_candidate_key`, so the two identities are not collapsed.

The preprint/journal examples remain separate records, and the fresh audit prevents false closure where the readers disagree. `PMID:37131700` has a primary `X_DUPLICATE` link to `PMID:37934786`, but the auditor returned `X_DESCRIPTIVE_ONLY`; it is therefore an open conflict and final primary-record uncertainty. `PMID:37934786` has agreeing `X_DESCRIPTIVE_ONLY` primary and audit decisions. `PMID:37873426` has a primary `X_DUPLICATE` link to `PMID:38271453`, while its auditor returned `X_NOT_INFECTIOUS_TRANSFERABLE`; it remains open. `PMID:38271453` likewise has a primary duplicate link to `PMID:37873426` and an audit `X_NOT_INFECTIOUS_TRANSFERABLE`, so it also remains open. These are discovery classifications, not final bibliographic identity determinations.

| Group | Candidate keys |
|---|---|
| `TITLE-DUP:0a04b6c05f1bf8c9` | `PMID:40766476`, `PMID:41214871` |
| `TITLE-DUP:0ee7101a7030ef62` | `PMID:41376665`, `PMID:42370026` |
| `TITLE-DUP:0f0062eb07582532` | `PMID:32663910`, `PMID:33503338` |
| `TITLE-DUP:1156cce4351b56b8` | `PMID:40463569`, `PMID:40585271` |
| `TITLE-DUP:12114823739c7969` | `PMID:38559244`, `PMID:39737444` |
| `TITLE-DUP:126685e1dcfc6ce1` | `PMID:40386571`, `PMID:41194012` |
| `TITLE-DUP:138202b363637c10` | `PMID:36945423`, `PMID:38820570` |
| `TITLE-DUP:1fad225654aecb94` | `PMID:30977801`, `PMID:31056644` |
| `TITLE-DUP:23c8f8a5031597ea` | `PMID:38352502`, `PMID:39230264` |
| `TITLE-DUP:38e2f8cf0af878a3` | `PMID:36854387`, `PMID:37151133` |
| `TITLE-DUP:3bdde3d4ab9e5d56` | `PMID:41282703`, `PMID:42102594` |
| `TITLE-DUP:3ce762c4fd0996a2` | `PMID:25331668`, `PMID:26550630` |
| `TITLE-DUP:3fb8accfd3dbd9ac` | `PMID:40492084`, `PMID:41366207` |
| `TITLE-DUP:41edbe0a2e80e8c5` | `PMID:41445609`, `PMID:42391403` |
| `TITLE-DUP:4d6d8e2bbe619e85` | `PMID:37205456`, `PMID:38129864` |
| `TITLE-DUP:53491b214649647e` | `PMID:41646366`, `PMID:41646813` |
| `TITLE-DUP:561d8abf551dc757` | `PMID:41757286`, `PMID:42317814` |
| `TITLE-DUP:59dc520eb78ae555` | `PMID:20826636`, `PMID:21372330` |
| `TITLE-DUP:5db46c913194e85c` | `PMID:39504969`, `PMID:39554028` |
| `TITLE-DUP:670fec3ec75fdc9c` | `PMID:37693183`, `PMID:38915911`, `PMID:39109971` |
| `TITLE-DUP:6fdeb4f0a03b960d` | `PMID:39677427`, `PMID:41933361` |
| `TITLE-DUP:7c2ed28cd3cb7324` | `PMID:35350548`, `PMID:39524693` |
| `TITLE-DUP:7e87c0a150efc235` | `PMID:32676611`, `PMID:32836597` |
| `TITLE-DUP:8e63ac86a89d2c0d` | `PMID:24611126`, `PMID:25914857` |
| `TITLE-DUP:926eb3be8975aadc` | `PMID:39005464`, `PMID:41953710` |
| `TITLE-DUP:9c9525ec5d58530a` | `PMID:35982666`, `PMID:37738280` |
| `TITLE-DUP:ad7f06aa2b22ee54` | `PMID:33173888`, `PMID:34750974` |
| `TITLE-DUP:b013d8ba6f8a1062` | `PMID:40832423`, `PMID:41445937` |
| `TITLE-DUP:b3066b8af42e0621` | `PMID:37131700`, `PMID:37934786` |
| `TITLE-DUP:b87333a4363c168a` | `PMID:33501461`, `PMID:34798545` |
| `TITLE-DUP:ba7817279921787a` | `PMID:25733563`, `PMID:26150555` |
| `TITLE-DUP:bfccec976edcf490` | `PMID:35979401`, `PMID:38617598` |
| `TITLE-DUP:c029a09ae6616cb2` | `PMID:37873426`, `PMID:38271453` |
| `TITLE-DUP:c1ab72faa19f21bf` | `PMID:40666369`, `PMID:42316273` |
| `TITLE-DUP:ce798a399612508a` | `PMID:37808804`, `PMID:38557892` |
| `TITLE-DUP:d2bb847ed238feaf` | `PMID:39974088`, `PMID:40630514` |
| `TITLE-DUP:d3bb8ec617ab284a` | `PMID:38496513`, `PMID:41004543` |
| `TITLE-DUP:de27359687d065cc` | `PMID:36238719`, `PMID:38127835` |
| `TITLE-DUP:e4e9fc9e7356a21e` | `PMID:33980718`, `PMID:34035040` |
| `TITLE-DUP:f67e8330b96f3ac8` | `PMID:38343863`, `PMID:40953059` |

Equal normalized titles alone were never treated as proof of identity. Open conflicts and nonduplicate judgments preserve separate candidate keys for primary-source identity work.
