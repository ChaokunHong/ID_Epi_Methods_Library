# Registry Schema

## Header order

The Library has ten normalized CSV registries with these exact header orders:

```text
papers.csv: paper_id,title,year,record_type,verification_state,doi,url,card_path,notes
methods.csv: method_id,canonical_name,family,verification_state,card_path,notes
paper_method_links.csv: paper_id,method_id,relationship,notes
candidate_method_links.csv: candidate_id,method_id,notes
candidate_dataset_links.csv: candidate_id,dataset_id,notes
simulation_method_links.csv: simulation_id,method_id,notes
simulation_candidate_links.csv: simulation_id,candidate_id,notes
translation_candidates.csv: candidate_id,title,domain,portfolio_category,verification_state,card_path,notes
datasets.csv: dataset_id,name,owner,access_state,verification_state,official_url,card_path,notes
simulations.csv: simulation_id,title,family,verification_state,card_path,notes
```

CSV data rows must have exactly the same number of fields as the header. Surplus and missing fields are invalid even when the omitted field would otherwise be optional.

## Required fields

Once a data row exists, the following fields must be nonblank:

- papers: `paper_id,title,year,record_type,verification_state,card_path`
- methods: `method_id,canonical_name,family,verification_state,card_path`
- paper-method links: `paper_id,method_id,relationship`
- translation candidates: `candidate_id,title,domain,portfolio_category,verification_state,card_path`
- datasets: `dataset_id,name,owner,access_state,verification_state,card_path`
- simulations: `simulation_id,title,family,verification_state,card_path`
- candidate-method links: `candidate_id,method_id`
- candidate-dataset links: `candidate_id,dataset_id`
- simulation-method links: `simulation_id,method_id`
- simulation-candidate links: `simulation_id,candidate_id`

## Allowed values

```text
record_type = method_source | applied_seed | diagnostic | correction | guidance | reproducibility
verification_state = discovery | verified | extracted | retired
relationship = originates | applies | critiques | corrects | diagnoses | implements
domain = amr | infectious_disease | cross_domain
portfolio_category = unranked | flagship | lower_risk_public_data | infrastructure_prospective | collaboration_dependent | no_go
access_state = unknown | public_verified | registration_required | application_required | restricted | unavailable
family = causal_policy | surveillance_measurement | spatial_transmission | forecasting_dynamics | evidence_synthesis | simulation_methods
```

## Identifier semantics

- A paper `year` is exactly four digits and must equal the year embedded in `P-YYYY-NNNN`.
- Method and simulation family prefixes map as follows: `CAUSAL` to `causal_policy`, `SURVEILLANCE` to `surveillance_measurement`, `SPATIAL` to `spatial_transmission`, `FORECASTING` to `forecasting_dynamics`, `EVIDENCE` to `evidence_synthesis`, and `SIMULATION` to `simulation_methods`.
- Translation prefixes map as follows: `AMR` to `amr`, `ID` to `infectious_disease`, and `CROSS` to `cross_domain`.
- In `D-OWNER-NNN`, `OWNER` is an uppercase namespace token. It is not mechanically equated to the free-text `owner` field. Any future owner-prefix mapping requires a new owner-approved decision.

## Relationship authority, foreign keys, and uniqueness

The five normalized link registries are the authoritative relationship store. Linked-ID fields in Markdown cards are human-readable mirrors and must match the applicable registry links once records exist.

Every link ID is mandatory and foreign-key checked against its entity registry. The pair in each of the four new link registries must be unique. In `paper_method_links.csv`, the `(paper_id, method_id, relationship)` tuple must be unique; the same paper-method pair may appear more than once only when the relationship values differ.

## Empty registries and null values

Empty registries contain only headers. Optional unknown text values remain empty rather than using invented facts or placeholder tokens. Required fields never use blank values once a row exists.
