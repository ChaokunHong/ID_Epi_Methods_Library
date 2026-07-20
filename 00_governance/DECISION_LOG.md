# Decision Log

Do not rewrite prior decisions. Add a new row when a decision is superseded and cite the earlier decision ID.

| Decision ID | Date | Status | Decision | Rationale | Evidence or authority | Supersedes |
|---|---|---|---|---|---|---|
| DEC-20260720-001 | 2026-07-20 | active | Create `ID_Epi_Methods_Library` as a sibling repository of `Surveillance_AMR`. | Separates reusable method discovery from one application protocol. | Owner approval and approved design `c708ac2`. | — |
| DEC-20260720-002 | 2026-07-20 | active | Use methods-first discovery; treat AMR, LMIC relevance, public-data feasibility, and solo workload as downstream attributes. | Prevents premature narrowing and supports flagship discovery. | Owner approval and approved design `c708ac2`. | — |
| DEC-20260720-003 | 2026-07-20 | active | Include simulation-only, synthetic-data, mechanistic, and method-comparison studies. | Some important methodological contributions do not require a real-data analysis. | Owner approval and approved design `c708ac2`. | — |
| DEC-20260720-004 | 2026-07-20 | active | Use five permanent ID namespaces for papers, methods, datasets, translations, and simulations. | Makes cross-file relationships stable when titles change. | Approved design section 6. | — |
| DEC-20260720-005 | 2026-07-20 | active | Use normalized link registries as the authoritative relationship store; linked-ID fields in Markdown cards are human-readable mirrors and must match registry links once records exist. | Preserves auditable many-to-many relationships without inventing an unapproved relationship enum. | Owner-approved whole-branch correction schema. | — |
| DEC-20260720-006 | 2026-07-20 | active | Execute broad method discovery in two auditable lanes—infectious-disease applications and method lineage—while keeping all new records at `discovery` until a separate primary-source verification plan. | Preserves the owner's methods-first intent and prevents high-impact applications, search-index metadata, or the seed scan from being misreported as verified evidence. | Owner continuation approval; approved design `c708ac2`; Library discussion in Codex task `019f78e2-e49c-7c01-bc36-599a250e5bc1`. | — |
