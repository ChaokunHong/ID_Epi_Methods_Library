# SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:50:39.263058+08:00` to `2026-07-20T13:51:20.595761+08:00`
- Source: `pubmed`
- Lane: `FAMILY`
- Family: `surveillance_measurement`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
(capture-recapture[Title] OR "capture recapture"[Title] OR "multiple-system estimation"[Title] OR nowcast*[Title] OR "reporting delay"[Title] OR "observation process"[Title] OR "preferential sampling"[Title] OR "measurement error"[Title] OR "sentinel surveillance"[Title] OR "latent class"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `980`
- Descendant leaves: `1`
- Descendant retrieved total: `980`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.esearch.json`
- Root ESearch SHA256: `9c7ccd9979b7845d748ad6a160ebe395395807f671173c700161af0fa9ba9a2d`

```text
SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01 type=leaf interval=2010/01/01..2026/12/31 reported=980 retrieved=980
```

## Leaf SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01
- Parent search ID: `(root)`
- Reported/retrieved count: `980` / `980`
- ESearch path: `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.esearch.json`
- ESearch SHA256: `9c7ccd9979b7845d748ad6a160ebe395395807f671173c700161af0fa9ba9a2d`
- Exact leaf query:
```text
(capture-recapture[Title] OR "capture recapture"[Title] OR "multiple-system estimation"[Title] OR nowcast*[Title] OR "reporting delay"[Title] OR "observation process"[Title] OR "preferential sampling"[Title] OR "measurement error"[Title] OR "sentinel surveillance"[Title] OR "latent class"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.efetch.000000000-000000199.xml` | `eabcde75378b5718a6634c4c835677aa98539619bba760bbfca5f30e2d98180a` |
| 200 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.efetch.000000200-000000399.xml` | `80afd662a701ff53b0fe488f4b3d3de9f33788fad4c2b0b6f7398f8f9b5b10bc` |
| 400 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.efetch.000000400-000000599.xml` | `7b993530799a34261c11e055a02a3f3d86ebd8c779a94cd9e21057847b044e35` |
| 600 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.efetch.000000600-000000799.xml` | `10d1632af6f1a336fa1164eb90d3641c7d62f664cea20a7b8802a7eaa8091371` |
| 800 | 180 | 180 | `raw/SEARCH-20260720-PUBMED-FAMILY-SURVEILLANCE-01.efetch.000000800-000000979.xml` | `b6f41e0409e5cd96899a3ba912cbac4845617adedb9f506eccd80fc83151c282` |
