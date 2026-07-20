# SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:53:42.859349+08:00` to `2026-07-20T13:53:52.155703+08:00`
- Source: `pubmed`
- Lane: `VENUE`
- Family: `surveillance_measurement`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
(capture-recapture[Title/Abstract] OR "capture recapture"[Title/Abstract] OR "multiple-system estimation"[Title/Abstract] OR nowcast*[Title/Abstract] OR "reporting delay"[Title/Abstract] OR "observation process"[Title/Abstract] OR "preferential sampling"[Title/Abstract] OR "measurement error"[Title/Abstract] OR "sentinel surveillance"[Title/Abstract] OR "latent class"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `220`
- Descendant leaves: `1`
- Descendant retrieved total: `220`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01.esearch.json`
- Root ESearch SHA256: `3b64c1464b4db46f4bd8ca8d5874fbbc44599532f2a53cbf77920b089e336ad0`

```text
SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01 type=leaf interval=2010/01/01..2026/12/31 reported=220 retrieved=220
```

## Leaf SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01
- Parent search ID: `(root)`
- Reported/retrieved count: `220` / `220`
- ESearch path: `raw/SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01.esearch.json`
- ESearch SHA256: `3b64c1464b4db46f4bd8ca8d5874fbbc44599532f2a53cbf77920b089e336ad0`
- Exact leaf query:
```text
(capture-recapture[Title/Abstract] OR "capture recapture"[Title/Abstract] OR "multiple-system estimation"[Title/Abstract] OR nowcast*[Title/Abstract] OR "reporting delay"[Title/Abstract] OR "observation process"[Title/Abstract] OR "preferential sampling"[Title/Abstract] OR "measurement error"[Title/Abstract] OR "sentinel surveillance"[Title/Abstract] OR "latent class"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01.efetch.000000000-000000199.xml` | `5a99305cbcbbc218ece297f192d882dbdb42cf9de610ba5a4ac01663087ea38e` |
| 200 | 20 | 20 | `raw/SEARCH-20260720-PUBMED-VENUE-SURVEILLANCE-01.efetch.000000200-000000219.xml` | `32684c38783d1c037bcf5e6ea967a90face147f1d2981f9991829bb441a656ba` |
