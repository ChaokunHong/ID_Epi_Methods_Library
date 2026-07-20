# SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:49:31.247275+08:00` to `2026-07-20T13:50:37.341190+08:00`
- Source: `pubmed`
- Lane: `FAMILY`
- Family: `spatial_transmission`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: Two transient NCBI chunked-transfer IncompleteRead failures occurred before the complete successful attempt. Each incomplete attempt was discarded by the validated resume path; query, date interval, page size, and count gates were unchanged.

## Exact root query
```text
("endemic-epidemic"[Title] OR metapopulation[Title] OR "network model"[Title] OR "border discontinuity"[Title] OR "spatial diffusion"[Title] OR "gravity model"[Title] OR "radiation model"[Title] OR Hawkes[Title] OR phylogeograph*[Title] OR "genomic epidemiology"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `1416`
- Descendant leaves: `1`
- Descendant retrieved total: `1416`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.esearch.json`
- Root ESearch SHA256: `a619a1aa7501d5d3b494ef26cff5f4ea94c0a9edcf9025f9b5730a9bfc423ec1`

```text
SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01 type=leaf interval=2010/01/01..2026/12/31 reported=1416 retrieved=1416
```

## Leaf SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01
- Parent search ID: `(root)`
- Reported/retrieved count: `1416` / `1416`
- ESearch path: `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.esearch.json`
- ESearch SHA256: `a619a1aa7501d5d3b494ef26cff5f4ea94c0a9edcf9025f9b5730a9bfc423ec1`
- Exact leaf query:
```text
("endemic-epidemic"[Title] OR metapopulation[Title] OR "network model"[Title] OR "border discontinuity"[Title] OR "spatial diffusion"[Title] OR "gravity model"[Title] OR "radiation model"[Title] OR Hawkes[Title] OR phylogeograph*[Title] OR "genomic epidemiology"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000000000-000000199.xml` | `e764f3ccfd620f6cf3adc5f008be3a7c181158269d0e6d2ed2657e1ccf2822c1` |
| 200 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000000200-000000399.xml` | `0fb44a2f78339a1bfba6358f438597fe153b0a91c0b1abaaf60f7f28fc8e0f93` |
| 400 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000000400-000000599.xml` | `2435ee39543402ef53d467beeabf8d1a5cb1c86bd790906833a4b5339b16320a` |
| 600 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000000600-000000799.xml` | `5513fbc675eb6e543b6e74f8240e2f4845ce1bc4ce110d2bebd2d611efaecca5` |
| 800 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000000800-000000999.xml` | `2d2f1a3bd0aaaf75c249487aeeaa389ffcc99a95c4d2c25d5bde0e06d1937fea` |
| 1000 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000001000-000001199.xml` | `f2f5bba62978e937271fcd2c21cc9d352f867c3922bcdc5c3bd7f5839d00f522` |
| 1200 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000001200-000001399.xml` | `2d8e3276c39a0198857bf90135b2ca2b4be8e0516d6b075a93d16f7146f19384` |
| 1400 | 16 | 16 | `raw/SEARCH-20260720-PUBMED-FAMILY-SPATIAL-01.efetch.000001400-000001415.xml` | `0f9c0c8f61012dd1f2e1a03a47e8ecdcf0c8d5c86fabf7c465bd37cc43a72051` |
