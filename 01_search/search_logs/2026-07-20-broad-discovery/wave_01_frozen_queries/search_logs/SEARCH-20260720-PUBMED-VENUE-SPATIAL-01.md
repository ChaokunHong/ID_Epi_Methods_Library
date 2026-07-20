# SEARCH-20260720-PUBMED-VENUE-SPATIAL-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:53:25.535825+08:00` to `2026-07-20T13:53:41.711201+08:00`
- Source: `pubmed`
- Lane: `VENUE`
- Family: `spatial_transmission`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: One transient NCBI chunked-transfer IncompleteRead failure occurred before the complete successful attempt. The incomplete attempt was discarded by the validated resume path; query, date interval, page size, and count gates were unchanged.

## Exact root query
```text
("endemic-epidemic"[Title/Abstract] OR metapopulation[Title/Abstract] OR "network model"[Title/Abstract] OR "border discontinuity"[Title/Abstract] OR "spatial diffusion"[Title/Abstract] OR "gravity model"[Title/Abstract] OR "radiation model"[Title/Abstract] OR Hawkes[Title/Abstract] OR phylogeograph*[Title/Abstract] OR "genomic epidemiology"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `216`
- Descendant leaves: `1`
- Descendant retrieved total: `216`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-VENUE-SPATIAL-01.esearch.json`
- Root ESearch SHA256: `d22f676292fea95fab3ed697bbf945f7750ce8402f95914e8b1e3e844c4c4024`

```text
SEARCH-20260720-PUBMED-VENUE-SPATIAL-01 type=leaf interval=2010/01/01..2026/12/31 reported=216 retrieved=216
```

## Leaf SEARCH-20260720-PUBMED-VENUE-SPATIAL-01
- Parent search ID: `(root)`
- Reported/retrieved count: `216` / `216`
- ESearch path: `raw/SEARCH-20260720-PUBMED-VENUE-SPATIAL-01.esearch.json`
- ESearch SHA256: `d22f676292fea95fab3ed697bbf945f7750ce8402f95914e8b1e3e844c4c4024`
- Exact leaf query:
```text
("endemic-epidemic"[Title/Abstract] OR metapopulation[Title/Abstract] OR "network model"[Title/Abstract] OR "border discontinuity"[Title/Abstract] OR "spatial diffusion"[Title/Abstract] OR "gravity model"[Title/Abstract] OR "radiation model"[Title/Abstract] OR Hawkes[Title/Abstract] OR phylogeograph*[Title/Abstract] OR "genomic epidemiology"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-VENUE-SPATIAL-01.efetch.000000000-000000199.xml` | `7a9ebcbe56ba6ffb47a8267ccd0e586b7a71027f449b9b396a041d55b9d18291` |
| 200 | 16 | 16 | `raw/SEARCH-20260720-PUBMED-VENUE-SPATIAL-01.efetch.000000200-000000215.xml` | `282140dadbe8dca5d1335033dde35f9e8778080f7f21170b0551abe2b7e1bb48` |
