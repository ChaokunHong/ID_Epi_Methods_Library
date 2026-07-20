# SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:44:41.777168+08:00` to `2026-07-20T13:44:52.366375+08:00`
- Source: `pubmed`
- Lane: `FAMILY`
- Family: `evidence_synthesis`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
(triangulation[Title] OR "specification curve"[Title] OR multiverse[Title] OR transportability[Title] OR generalizability[Title] OR "outcome definition"[Title] OR denominator[Title] OR "hierarchical borrowing"[Title] OR "modelled versus observed"[Title] OR "modeled versus observed"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `146`
- Descendant leaves: `1`
- Descendant retrieved total: `146`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01.esearch.json`
- Root ESearch SHA256: `eb3078380eff29aa5e728b908fa94dd4f4da8c6adf3ccab607282d8c737e082a`

```text
SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01 type=leaf interval=2010/01/01..2026/12/31 reported=146 retrieved=146
```

## Leaf SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01
- Parent search ID: `(root)`
- Reported/retrieved count: `146` / `146`
- ESearch path: `raw/SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01.esearch.json`
- ESearch SHA256: `eb3078380eff29aa5e728b908fa94dd4f4da8c6adf3ccab607282d8c737e082a`
- Exact leaf query:
```text
(triangulation[Title] OR "specification curve"[Title] OR multiverse[Title] OR transportability[Title] OR generalizability[Title] OR "outcome definition"[Title] OR denominator[Title] OR "hierarchical borrowing"[Title] OR "modelled versus observed"[Title] OR "modeled versus observed"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 146 | 146 | `raw/SEARCH-20260720-PUBMED-FAMILY-EVIDENCE-01.efetch.000000000-000000145.xml` | `22838ad2d257909581dfae5afe3107a5f87fbada539f0ba5aff2c37a5cbcdb97` |
