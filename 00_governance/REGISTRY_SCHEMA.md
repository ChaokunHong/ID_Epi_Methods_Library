# Registry Schema

## Header order

```text
papers.csv: paper_id,title,year,record_type,verification_state,doi,url,card_path,notes
methods.csv: method_id,canonical_name,family,verification_state,card_path,notes
paper_method_links.csv: paper_id,method_id,relationship,notes
translation_candidates.csv: candidate_id,title,domain,portfolio_category,verification_state,card_path,notes
datasets.csv: dataset_id,name,owner,access_state,verification_state,official_url,card_path,notes
simulations.csv: simulation_id,title,family,verification_state,card_path,notes
```

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

## Empty registries and null values

Empty registries contain only headers. IDs and paths become mandatory once a data row exists. Optional unknown text values remain empty rather than using invented facts.
