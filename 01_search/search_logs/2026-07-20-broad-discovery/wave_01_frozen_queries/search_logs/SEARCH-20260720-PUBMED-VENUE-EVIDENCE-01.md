# SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:51:44.182829+08:00` to `2026-07-20T13:51:54.877557+08:00`
- Source: `pubmed`
- Lane: `VENUE`
- Family: `evidence_synthesis`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
(triangulation[Title/Abstract] OR "specification curve"[Title/Abstract] OR multiverse[Title/Abstract] OR transportability[Title/Abstract] OR generalizability[Title/Abstract] OR "outcome definition"[Title/Abstract] OR denominator[Title/Abstract] OR "hierarchical borrowing"[Title/Abstract] OR "modelled versus observed"[Title/Abstract] OR "modeled versus observed"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `155`
- Descendant leaves: `1`
- Descendant retrieved total: `155`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01.esearch.json`
- Root ESearch SHA256: `5a5533b8f581e67f46532768df48aaca345c91fd2efcd10cb3419733983fcc37`

```text
SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01 type=leaf interval=2010/01/01..2026/12/31 reported=155 retrieved=155
```

## Leaf SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01
- Parent search ID: `(root)`
- Reported/retrieved count: `155` / `155`
- ESearch path: `raw/SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01.esearch.json`
- ESearch SHA256: `5a5533b8f581e67f46532768df48aaca345c91fd2efcd10cb3419733983fcc37`
- Exact leaf query:
```text
(triangulation[Title/Abstract] OR "specification curve"[Title/Abstract] OR multiverse[Title/Abstract] OR transportability[Title/Abstract] OR generalizability[Title/Abstract] OR "outcome definition"[Title/Abstract] OR denominator[Title/Abstract] OR "hierarchical borrowing"[Title/Abstract] OR "modelled versus observed"[Title/Abstract] OR "modeled versus observed"[Title/Abstract]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("Am J Epidemiol"[Journal] OR "BMJ"[Journal] OR "Clin Infect Dis"[Journal] OR "Emerg Infect Dis"[Journal] OR "Epidemiology"[Journal] OR "Euro Surveill"[Journal] OR "Int J Epidemiol"[Journal] OR "JAMA"[Journal] OR "Lancet"[Journal] OR "Lancet Glob Health"[Journal] OR "Lancet Infect Dis"[Journal] OR "N Engl J Med"[Journal] OR "NPJ Biofilms Microbiomes"[Journal] OR "NPJ Digit Med"[Journal] OR "NPJ Syst Biol Appl"[Journal] OR "NPJ Vaccines"[Journal] OR "Nat Med"[Journal] OR "Nat Microbiol"[Journal] OR "Nature"[Journal] OR "PLoS Med"[Journal] OR "Proc Natl Acad Sci U S A"[Journal] OR "Science"[Journal]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 155 | 155 | `raw/SEARCH-20260720-PUBMED-VENUE-EVIDENCE-01.efetch.000000000-000000154.xml` | `5a17109e8d027605aab7d2068f4f7308bfdb6e9e2d8d697bb57be5daf361241e` |
