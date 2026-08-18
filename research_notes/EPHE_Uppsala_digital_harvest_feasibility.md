# EPHE / Archives nationales / Uppsala: digital-harvest feasibility for the Marillier–Lovejoy project

## Status

The digital situation has changed enough that the EPHE side is now **machine-harvestable in principle**, while the Söderblom side is **metadata-harvestable but the crucial 1898–1901 notebooks are not presently exposed as digitized scans**.

The distinction matters:

- EPHE / Archives nationales: inventory metadata, XML-EAD and a large corpus of digitized images are now online and openly reusable. The immediate task is to identify which exact 1898–1899 Vᵉ Section registration/attendance units have digital images attached.
- Uppsala / Alvin: metadata can be harvested via OAI-PMH and digitized items can be downloaded, but the Nathan Söderblom archive itself is catalogued as `Non digital`; its catalogue nevertheless reveals exactly the diary/notebook series that overlap Lovejoy's Marillier year.

---

## 1. EPHE digitization project: now live

EPHE announced that its project **“L'EPHE dans la recherche française pendant le premier siècle de son existence (1868–1968): inventaire et numérisation des archives scientifiques”** was completed in May 2025.

The project digitized a selection of:

- ministry supervisory records;
- EPHE institutional archives;
- three scholar fonds;
- including institutional materials such as **registres d'inscription**, **listes de présence**, and section assembly registers.

EPHE states that the inventory and digitizations are online in the Archives nationales SIV under:

`FRAN_IR_061975`

This is the most important current access point for reconstructing the Marillier seminar cohort.

### Relevant Vᵉ Section fonds

EPHE's archive inventory identifies:

- Vᵉ Section institutional archives, 1886–2005: `20190568/001-399`
- **scolarité**: `20190568/185-368`

The 1898–1899 registration and attendance evidence should therefore be sought first within this scolarité block and in the digitized project instrument `FRAN_IR_061975`.

**Caution:** EPHE explicitly says registration registers and attendance lists are among the institutional records available for this project, but the public project announcement alone does not prove that the exact 1898–1899 Marillier register/list is in the digitized subset. The next technical task is to resolve the unit-level `daogrp` / digital-image links in the EAD.

---

## 2. Archives nationales open-data layer: suitable for batch harvesting

The Archives nationales now publish two especially useful open datasets.

### A. Inventory index

Dataset: **Liste des inventaires des Archives nationales publiés en ligne**.

It contains more than 31,000 online inventories and exposes fields including:

- `fran_ir`
- title
- cote range
- date range
- producer
- `documents_numérisés`
- SIV permalink
- direct XML-EAD file link

The field `documents_numérisés = oui` indicates that at least one digital document is attached to that inventory (`<daogrp>` in EAD), not that the whole fonds is digitized.

Current CSV resource ID recovered from the download redirect:

`c486d8ae-30ca-4084-8ac4-b5f0ff8d172d`

### B. Digitized-corpus index

Dataset: **Corpus de documents numérisés des Archives nationales**.

As of the July 2026 update it contains 719 digitized corpora and fields including:

- SIV image/inventory URL
- approximate number of views/images
- `cotes_concernées`
- archive status
- document type
- theme
- period
- persons
- XML inventory link
- observations, including image-file naming roots

Current CSV resource ID:

`944d7b79-46a6-437d-8af4-24cc99484ba9`

This is potentially enough to automate the first-stage harvest: identify `FRAN_IR_061975` and/or `20190568`, retrieve the EAD, locate digitized component nodes, then enumerate image-bearing cotes.

### Practical implication

We no longer need to treat the Archives nationales SIV as a purely manual webpage. The discovery layer is structured and downloadable. A local harvest can be designed as:

1. ingest AN inventory CSV;
2. filter for `FRAN_IR_061975`, `20190568`, `École pratique des hautes études`, `Vᵉ section`;
3. fetch the corresponding XML-EAD;
4. parse `<c>` hierarchy and `<daogrp>` / digital-object links;
5. isolate 1897–1900 scolarité / registration / attendance units;
6. build a cote-level manifest before attempting image capture.

At present the exact 1898–1899 image-bearing cote has **not yet been resolved**, because the public SIV page is difficult to fetch automatically and the static data.gouv CSV redirect was not retrievable in the current runtime. The infrastructure and identifiers are nevertheless confirmed.

---

## 3. Nathan Söderblom archive: exact notebook ranges now identified

Official Alvin record:

- archive: `Nathan Söderbloms efterlämnade papper`
- institution: Uppsala University Library, Carolina Rediviva
- shelfmark: `N. Söderblom`
- archive format: **Non digital**

The online archive tree nevertheless identifies three notebook/diary groups directly overlapping the Marillier period:

- `Dag- och anteckningsböcker 1894-1899`
- `Dag- och anteckningsböcker 1896-1901`
- `Dag- och anteckningsböcker 1898-1915`

and:

- `Almanackor 1892-1899`

This is a major narrowing of the onsite/digitization target. The archive record also provides digitized PDF paper catalogues for:

- `C. Manuskript`
- `E. Handlingar i särskilda ämnen`
- `D. Minnen`

The catalogue notes explicitly state that only digitized letters are individually specified in the archive list. Therefore the 1894–1901 notebooks should currently be treated as **physical manuscript targets whose metadata/finding aids are online, not as already scanned notebooks**.

---

## 4. Alvin is harvestable at metadata level

Alvin officially exposes metadata under **OAI-PMH 2.0** and releases metadata under **CC0**.

OAI endpoint:

`https://www.alvin-portal.org/oai/oai?verb=Identify`

All genuinely digitized Alvin material may be downloaded and used freely according to the portal. This means a reusable harvesting pipeline can be built for:

- Söderblom archive record and children;
- digitized correspondence;
- authority records;
- any future digitization of the relevant diaries/notebooks.

For the present research question, however, OAI harvesting will not substitute for obtaining scans of the diary/notebook groups, because the parent archive is explicitly marked `Non digital`.

---

## 5. Why Söderblom is now the highest-value control witness

The 1898–1899 EPHE report lists Söderblom as a regular student in Marillier's conferences while listing Lovejoy among the auditors who took an active part in the work.

Söderblom's 1898 EPHE diploma was:

`Traces dans le Mazdéisme d'une ancienne conception sur la survivance des morts`

Bibliographic authority data describes it as prepared **under the direction of Léon Marillier**.

This gives an unusually tight control configuration:

- same teacher;
- same year;
- same `survivance` problem;
- one surviving Lovejoy notebook;
- one surviving Söderblom archive with notebooks spanning 1898–1899.

The immediate archival question is therefore no longer merely “does Söderblom have papers?” but:

> **Which physical volume(s) inside `Dag- och anteckningsböcker 1894-1899` and `1896-1901` cover Paris / EPHE / Marillier, and do they contain course notes or bibliography comparable to Lovejoy 005?**

---

## 6. Current yes/no matrix

| Target | Metadata harvest | Full digital images now confirmed | Current action |
|---|---:|---:|---|
| EPHE project `FRAN_IR_061975` | **Yes** | **Yes, for a selected corpus** | resolve unit-level 1898–99 cotes |
| Vᵉ Section `20190568/185-368` | **Yes** | **Not yet confirmed for exact 1898–99 units** | parse EAD / `daogrp` |
| AN inventory dataset | **Yes** | n/a | batch ingest/filter |
| AN digitized-corpus dataset | **Yes** | points directly to image-bearing corpora | batch ingest/filter |
| Söderblom archive metadata | **Yes, OAI-PMH** | archive parent = **Non digital** | harvest metadata/catalogue |
| Söderblom 1894–1901 notebooks | catalogue identification **Yes** | **No scan confirmed** | request/digitize exact volumes |
| Söderblom digitized letters | **Yes** | **Some letters yes** | search Marillier / Paris / EPHE correspondence |

---

## 7. Immediate next technical targets

### EPHE / AN

1. Obtain the XML-EAD for `FRAN_IR_061975`.
2. Extract every component whose dates intersect `1898-1899` and whose title contains registration, attendance, student, scolarité, Vᵉ Section, sciences religieuses, or conference terms.
3. Record `unitid`, `unittitle`, `unitdate`, parent hierarchy and all `<daogrp>` / digital-object references.
4. Cross-search resulting student names against the 1898–1899 Marillier report: Söderblom, Travers, Schaefer, Lovejoy, W. S. Andrews, Lorette.

### Uppsala

1. Capture the attached C/E and D finding-aid PDFs.
2. Identify capsule/volume numbers for `Dag- och anteckningsböcker 1894-1899` and `1896-1901`.
3. Search digitized correspondence metadata for `Marillier`, `Paris`, `École pratique des hautes études`, `survivance`, and French religious-studies correspondents.
4. If notebooks remain non-digital, request targeted digitization rather than an open-ended archive scan.

## Bottom line

**Yes: the EPHE / Archives nationales digital archive has reached the point where a systematic machine harvest is technically justified now.** The exact Marillier 1898–1899 attendance/register images still have to be resolved at component level, but the institution has published both the digitization project and structured open-data discovery layers.

**Uppsala is one step behind:** its metadata and finding aids can already be harvested, and the exact relevant notebook date ranges are known, but the crucial Söderblom notebooks are not presently exposed as digital scans. That should become a targeted digitization request once the volume/capsule identifiers are extracted.