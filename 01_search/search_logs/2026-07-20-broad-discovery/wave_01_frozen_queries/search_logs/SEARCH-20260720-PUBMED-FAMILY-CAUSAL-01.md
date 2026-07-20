# SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01

## Execution control
- Run executed at (receipt): `2026-07-20T13:44:01.058821+08:00`
- Timezone: `Asia/Shanghai`
- Raw publication window (filesystem metadata only): `2026-07-20T13:44:01.974836+08:00` to `2026-07-20T13:44:40.654221+08:00`
- Source: `pubmed`
- Lane: `FAMILY`
- Family: `causal_policy`
- Date interval: `2010/01/01` to `2026/12/31`
- Screening status: `not started`
- Deviations: None recorded.

## Exact root query
```text
("interrupted time series"[Title] OR "difference-in-differences"[Title] OR "difference in differences"[Title] OR "event study"[Title] OR "synthetic control"[Title] OR "regression discontinuity"[Title] OR "instrumental variable"[Title] OR "target trial"[Title] OR "negative control"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

## Split tree and counts
- Root type: `leaf`
- Root reported count: `922`
- Descendant leaves: `1`
- Descendant retrieved total: `922`
- Root ESearch: `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.esearch.json`
- Root ESearch SHA256: `094e01d665a07226e08e3dbdac34d2904a64567ddc356ed6f6aea11a6afdee28`

```text
SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01 type=leaf interval=2010/01/01..2026/12/31 reported=922 retrieved=922
```

## Leaf SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01
- Parent search ID: `(root)`
- Reported/retrieved count: `922` / `922`
- ESearch path: `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.esearch.json`
- ESearch SHA256: `094e01d665a07226e08e3dbdac34d2904a64567ddc356ed6f6aea11a6afdee28`
- Exact leaf query:
```text
("interrupted time series"[Title] OR "difference-in-differences"[Title] OR "difference in differences"[Title] OR "event study"[Title] OR "synthetic control"[Title] OR "regression discontinuity"[Title] OR "instrumental variable"[Title] OR "target trial"[Title] OR "negative control"[Title]) AND ("Communicable Diseases"[Mesh] OR infection*[Title/Abstract] OR infectious[Title/Abstract] OR outbreak*[Title/Abstract] OR epidemic*[Title/Abstract] OR pathogen*[Title/Abstract] OR vaccin*[Title/Abstract] OR antimicrobial resistance[Title/Abstract]) AND ("2010/01/01"[Date - Publication] : "2026/12/31"[Date - Publication])
```

| retstart | retmax | parsed_count | raw page | SHA256 |
|---:|---:|---:|---|---|
| 0 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.efetch.000000000-000000199.xml` | `153e13fc34842608ad5efcdf07b823987199d1df4b1ce94279e62b59df3fa06e` |
| 200 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.efetch.000000200-000000399.xml` | `ec462c9b33a79da9a128d01441cffc918bc2d2c626c15b64728d34cc10e1df59` |
| 400 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.efetch.000000400-000000599.xml` | `a6cded09144095ef6d87bc5cc08b635d6f78f2e7cbf2c7bfdfbb228607eb4b19` |
| 600 | 200 | 200 | `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.efetch.000000600-000000799.xml` | `b61bdbed072befdf295c3c4d6575aeafc64319eeb78560f2acf27305bbb7385e` |
| 800 | 122 | 122 | `raw/SEARCH-20260720-PUBMED-FAMILY-CAUSAL-01.efetch.000000800-000000921.xml` | `d6876243bc206d4a4ba90e03dfad80343f80ce7d3df479122ebc424032cfd4a3` |
