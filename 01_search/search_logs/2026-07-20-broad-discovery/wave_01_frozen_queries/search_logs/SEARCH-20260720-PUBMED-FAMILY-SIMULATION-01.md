# SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:45:55.220639+08:00` to `2026-07-20T13:47:00.822600+08:00`
- Source: `pubmed`
- Lane: `FAMILY`
- Family: `simulation_methods`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
("simulation study"[Title] OR "synthetic data"[Title] OR "data-generating process"[Title] OR "data generating process"[Title] OR "agent-based"[Title] OR "mechanistic model"[Title] OR benchmark*[Title] OR "operating characteristics"[Title] OR "coverage probability"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `1316`
- Descendant leaves: `1`
- Descendant retrieved total: `1316`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.esearch.json`
- Root ESearch SHA256: `ef9e2b1359354f0d1e63ca8d7e676c184d9531ce984e3a4b9a003d5689e8895f`

```text
SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01 type=leaf interval=2010/01/01..2026/12/31 reported=1316 retrieved=1316
```

## Leaf SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01
- Parent search ID: `(root)`
- Reported/retrieved count: `1316` / `1316`
- ESearch path: `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.esearch.json`
- ESearch SHA256: `ef9e2b1359354f0d1e63ca8d7e676c184d9531ce984e3a4b9a003d5689e8895f`
- Exact leaf query:
```text
("simulation study"[Title] OR "synthetic data"[Title] OR "data-generating process"[Title] OR "data generating process"[Title] OR "agent-based"[Title] OR "mechanistic model"[Title] OR benchmark*[Title] OR "operating characteristics"[Title] OR "coverage probability"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000000000-000000199.xml` | `6c56baf5b0b3a1200c7b6f651fe809ebab75ef0776beae4ae13f25e61dd9bc67` |
| 200 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000000200-000000399.xml` | `e3c87d79994446830d99eec304df35193da315c99965a666f6db575093f38cea` |
| 400 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000000400-000000599.xml` | `58d42de25a0ce02a00e5456c05a42684f608f412db86223db62f6bf36dffa1a8` |
| 600 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000000600-000000799.xml` | `87ef5943f8a39ce47f8ddbd24b2257fa971a9df37c83f72f9607346e1998a2c2` |
| 800 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000000800-000000999.xml` | `1084cfc7e9757e016bf0bda386f5d3d8494510eb1efd15a85764cca23b1c8b5c` |
| 1000 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000001000-000001199.xml` | `ddb10cf5ce93fc6f6a6d92de69e247451ef23410339eeb20a1701eefbdb9dbd4` |
| 1200 | 116 | 116 | `raw/SEARCH-20260720-PUBMED-FAMILY-SIMULATION-01.efetch.000001200-000001315.xml` | `da3f18c865d60197d27b7f221447300615c391d7e262874ac499617c266957a3` |
