# SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:44:54.162306+08:00` to `2026-07-20T13:45:54.093790+08:00`
- Source: `pubmed`
- Lane: `FAMILY`
- Family: `forecasting_dynamics`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
("renewal model"[Title] OR "reproduction number"[Title] OR "ensemble forecast"[Title] OR "forecast calibration"[Title] OR "early warning"[Title] OR changepoint[Title] OR "change point"[Title] OR "outbreak detection"[Title] OR "mechanistic-statistical"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `1251`
- Descendant leaves: `1`
- Descendant retrieved total: `1251`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.esearch.json`
- Root ESearch SHA256: `376569696b4fbadd589f5a0080d1bcb8d391fe06ddb5cfa1439473905a70cd45`

```text
SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01 type=leaf interval=2010/01/01..2026/12/31 reported=1251 retrieved=1251
```

## Leaf SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01
- Parent search ID: `(root)`
- Reported/retrieved count: `1251` / `1251`
- ESearch path: `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.esearch.json`
- ESearch SHA256: `376569696b4fbadd589f5a0080d1bcb8d391fe06ddb5cfa1439473905a70cd45`
- Exact leaf query:
```text
("renewal model"[Title] OR "reproduction number"[Title] OR "ensemble forecast"[Title] OR "forecast calibration"[Title] OR "early warning"[Title] OR changepoint[Title] OR "change point"[Title] OR "outbreak detection"[Title] OR "mechanistic-statistical"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000000000-000000199.xml` | `2f17fee91bafffc69af05359742221334af6e62510e914c678bc961f81414dc9` |
| 200 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000000200-000000399.xml` | `600d01a3e758514867941184291cb1d71859fba0cd733ea89bb7dafd1249218b` |
| 400 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000000400-000000599.xml` | `4a3457db5734ea521cae03b93934d64b2d0ab4d707be6a292e41a7c9e38f95ec` |
| 600 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000000600-000000799.xml` | `38dc50dd51738b3a74b7efcb0166ad8607905020f209c617411629cca7ead9fa` |
| 800 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000000800-000000999.xml` | `298d8093b78aa9828a16a31bb9e5934cf8abd5d13e97b8eb8e55ba633ceab0f9` |
| 1000 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000001000-000001199.xml` | `f7a83369c5f571937043d48005e086b478b81e857f785861c1dda53219920bba` |
| 1200 | 51 | 51 | `raw/SEARCH-20260720-PUBMED-FAMILY-FORECASTING-01.efetch.000001200-000001250.xml` | `38c534c6984aef94cc572a618666b97099958b0016376820ffa6394912b5fbd8` |
