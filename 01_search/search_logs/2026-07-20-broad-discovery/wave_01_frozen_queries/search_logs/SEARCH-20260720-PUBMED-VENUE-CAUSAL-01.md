# SEARCH-20260720-PUBMED-VENUE-CAUSAL-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:51:21.765355+08:00` to `2026-07-20T13:51:42.552526+08:00`
- Source: `pubmed`
- Lane: `VENUE`
- Family: `causal_policy`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
("interrupted time series"[Title/Abstract] OR "difference-in-differences"[Title/Abstract] OR "difference in differences"[Title/Abstract] OR "event study"[Title/Abstract] OR "synthetic control"[Title/Abstract] OR "regression discontinuity"[Title/Abstract] OR "instrumental variable"[Title/Abstract] OR "target trial"[Title/Abstract] OR "negative control"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `279`
- Descendant leaves: `1`
- Descendant retrieved total: `279`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-VENUE-CAUSAL-01.esearch.json`
- Root ESearch SHA256: `7413ba327209de6c91901f6c1c11008c2d228bd42fb2bc16ec86d1cf84f9467a`

```text
SEARCH-20260720-PUBMED-VENUE-CAUSAL-01 type=leaf interval=2010/01/01..2026/12/31 reported=279 retrieved=279
```

## Leaf SEARCH-20260720-PUBMED-VENUE-CAUSAL-01
- Parent search ID: `(root)`
- Reported/retrieved count: `279` / `279`
- ESearch path: `raw/SEARCH-20260720-PUBMED-VENUE-CAUSAL-01.esearch.json`
- ESearch SHA256: `7413ba327209de6c91901f6c1c11008c2d228bd42fb2bc16ec86d1cf84f9467a`
- Exact leaf query:
```text
("interrupted time series"[Title/Abstract] OR "difference-in-differences"[Title/Abstract] OR "difference in differences"[Title/Abstract] OR "event study"[Title/Abstract] OR "synthetic control"[Title/Abstract] OR "regression discontinuity"[Title/Abstract] OR "instrumental variable"[Title/Abstract] OR "target trial"[Title/Abstract] OR "negative control"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-VENUE-CAUSAL-01.efetch.000000000-000000199.xml` | `313a4017cea1e3073cd219d1869fd6d31db6b9b5349c9ab567e5ff4a697475c5` |
| 200 | 79 | 79 | `raw/SEARCH-20260720-PUBMED-VENUE-CAUSAL-01.efetch.000000200-000000278.xml` | `454936948652eaf9c007e2fd38a85d287712a7887f46c855d1e07faca2eace11` |
