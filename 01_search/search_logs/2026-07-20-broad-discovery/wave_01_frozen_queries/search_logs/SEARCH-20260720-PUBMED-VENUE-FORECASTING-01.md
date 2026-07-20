# SEARCH-20260720-PUBMED-VENUE-FORECASTING-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:51:56.646466+08:00` to `2026-07-20T13:52:17.439977+08:00`
- Source: `pubmed`
- Lane: `VENUE`
- Family: `forecasting_dynamics`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
("renewal model"[Title/Abstract] OR "reproduction number"[Title/Abstract] OR "ensemble forecast"[Title/Abstract] OR "forecast calibration"[Title/Abstract] OR "early warning"[Title/Abstract] OR changepoint[Title/Abstract] OR "change point"[Title/Abstract] OR "outbreak detection"[Title/Abstract] OR "mechanistic-statistical"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `395`
- Descendant leaves: `1`
- Descendant retrieved total: `395`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-VENUE-FORECASTING-01.esearch.json`
- Root ESearch SHA256: `95f0b5544ffba77c20a9e4183760b57fe7c795253b27c0c3081033e053db8366`

```text
SEARCH-20260720-PUBMED-VENUE-FORECASTING-01 type=leaf interval=2010/01/01..2026/12/31 reported=395 retrieved=395
```

## Leaf SEARCH-20260720-PUBMED-VENUE-FORECASTING-01
- Parent search ID: `(root)`
- Reported/retrieved count: `395` / `395`
- ESearch path: `raw/SEARCH-20260720-PUBMED-VENUE-FORECASTING-01.esearch.json`
- ESearch SHA256: `95f0b5544ffba77c20a9e4183760b57fe7c795253b27c0c3081033e053db8366`
- Exact leaf query:
```text
("renewal model"[Title/Abstract] OR "reproduction number"[Title/Abstract] OR "ensemble forecast"[Title/Abstract] OR "forecast calibration"[Title/Abstract] OR "early warning"[Title/Abstract] OR changepoint[Title/Abstract] OR "change point"[Title/Abstract] OR "outbreak detection"[Title/Abstract] OR "mechanistic-statistical"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-VENUE-FORECASTING-01.efetch.000000000-000000199.xml` | `738f0faaf9c27a33e23f2a2387303b3e999eab14a9023e0ec28084aa14a096e1` |
| 200 | 195 | 195 | `raw/SEARCH-20260720-PUBMED-VENUE-FORECASTING-01.efetch.000000200-000000394.xml` | `60f9e1f4b726f9dbe9e2e801d645acbca315e874294d2408f7276ac383c0abce` |
