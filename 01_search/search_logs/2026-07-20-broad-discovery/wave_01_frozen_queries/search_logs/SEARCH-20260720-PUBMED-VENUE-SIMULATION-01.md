# SEARCH-20260720-PUBMED-VENUE-SIMULATION-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:52:18.735106+08:00` to `2026-07-20T13:52:37.013129+08:00`
- Source: `pubmed`
- Lane: `VENUE`
- Family: `simulation_methods`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
("simulation study"[Title/Abstract] OR "synthetic data"[Title/Abstract] OR "data-generating process"[Title/Abstract] OR "data generating process"[Title/Abstract] OR "agent-based"[Title/Abstract] OR "mechanistic model"[Title/Abstract] OR benchmark*[Title/Abstract] OR "operating characteristics"[Title/Abstract] OR "coverage probability"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `255`
- Descendant leaves: `1`
- Descendant retrieved total: `255`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-VENUE-SIMULATION-01.esearch.json`
- Root ESearch SHA256: `564106489a9d793aedb8b32f8ef2d88d279e293a1e55e95523e25b50a00d6bc3`

```text
SEARCH-20260720-PUBMED-VENUE-SIMULATION-01 type=leaf interval=2010/01/01..2026/12/31 reported=255 retrieved=255
```

## Leaf SEARCH-20260720-PUBMED-VENUE-SIMULATION-01
- Parent search ID: `(root)`
- Reported/retrieved count: `255` / `255`
- ESearch path: `raw/SEARCH-20260720-PUBMED-VENUE-SIMULATION-01.esearch.json`
- ESearch SHA256: `564106489a9d793aedb8b32f8ef2d88d279e293a1e55e95523e25b50a00d6bc3`
- Exact leaf query:
```text
("simulation study"[Title/Abstract] OR "synthetic data"[Title/Abstract] OR "data-generating process"[Title/Abstract] OR "data generating process"[Title/Abstract] OR "agent-based"[Title/Abstract] OR "mechanistic model"[Title/Abstract] OR benchmark*[Title/Abstract] OR "operating characteristics"[Title/Abstract] OR "coverage probability"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-VENUE-SIMULATION-01.efetch.000000000-000000199.xml` | `86811326535bee014977a2b4992c664e81c7d27d8e736d27d353b9c3d4bff6c6` |
| 200 | 55 | 55 | `raw/SEARCH-20260720-PUBMED-VENUE-SIMULATION-01.efetch.000000200-000000254.xml` | `a68eb5d40051d22383155caa40cb83d58bc5337858a22e6450dd320189a79fea` |
