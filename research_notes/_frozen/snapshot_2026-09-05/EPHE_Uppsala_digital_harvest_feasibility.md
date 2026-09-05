# EPHE / Archives nationales / Uppsala: digital-harvest feasibility for the Marillier–Lovejoy project

## Status — updated 2026-08-19

The digital situation is now much clearer than in the first reconnaissance.

- **EPHE / Archives nationales:** the 2025 digitization project is not merely machine-harvestable in principle. The SIV delivery layer has now been reverse-engineered far enough to recover sequential image ranges directly from stable JPEG URLs and merge them locally to PDF.
- **Uppsala / Alvin:** the Nathan Söderblom archive remains catalogued as `Non digital`, but the archive tree now exposes several notebook groups that directly overlap 1898–99. A separate Uppsala finding aid also isolates a `Parisåren` block for 1894–1901.

The detailed live sweep is recorded in:

- `research_notes/project2_contemporary_student_notebooks_sweep_2026-08-19.md`
- `research_notes/project2_siv_url_and_image_range_ledger_2026-08-19.md`
- `tools/harvest_siv_gallery.ps1`
- `tools/harvest_project2_ephe_ranges.ps1`

---

## 1. EPHE digitization project

EPHE's project **“L'EPHE dans la recherche française pendant le premier siècle de son existence (1868–1968): inventaire et numérisation des archives scientifiques”** was completed in May 2025.

Main SIV inventory:

https://www.siv.archives-nationales.culture.gouv.fr/siv/IR/FRAN_IR_061975

PDF export:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/ir/pdfIR.action?irId=FRAN_IR_061975

XML export:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/ir/exportXML.action?irId=FRAN_IR_061975

The project includes selected institutional materials from the EPHE sections, ministry oversight files, and scholar fonds. Registration registers and attendance lists are highlighted by EPHE as especially useful institutional records, but the exact 1898–99 register/list still needs cote-level resolution in the full Vth-Section archive rather than being assumed to be part of every digitized subset.

---

## 2. Vth Section targets now resolved from the detailed inventory

### F/17/13618

`F/17/13618 — Ve et VIe sections, 1885-1933`

For the Vth Section the description includes:

- organization;
- course creation/candidatures;
- personnel;
- **Élèves : nominations (1889–1932)**;
- posters/programmes.

The detailed inventory states that the article was digitized in full. Its images are exposed through the original finding aid rather than necessarily as a direct node in the 88-result project gallery.

This is a high-value route to resolving Travers / Schaefer and other student identities.

### 20190568/49

Vth Section assembly minutes:

`Assemblée de section : cahiers manuscrits des procès-verbaux`

- dossier 1: **16 février 1886–17 juin 1906**
- fully digitized

Potential yield: diploma/student decisions, section business, Marillier-related institutional discussion.

### 20190568/69

Vth Section secretariat:

`Correspondance générale, 1886–1899`

- fully digitized
- split online into three `Sous-ensemble`

This is the strongest direct secretariat target for the 1898–99 Marillier year.

### 20190568/70

`Correspondance générale, 1900–1912`

- fully digitized
- split online into three `Sous-ensemble`

One recovered gallery from this sequence contains Marcel Mauss's 1901 candidature material after Marillier's death. This is useful methodological context but is not the center of Project 2.

### 20190568/86

`Annuaires de la section, 1885–1891` — original manuscript conference reports / correspondence.

Important for early Vth-Section practice, but **does not reach 1898–99**.

### 20190568/391

Large-format conference programmes:

`1886–1999`, fully digitized.

Useful for formal schedule/course reconstruction.

---

## 3. SIV delivery layer is now directly harvestable

The Archives nationales gallery exposes stable per-image JPEG URLs:

`https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_XXXXX_L-medium.jpg`

Two sequential ranges were recovered on 2026-08-19.

### Range A — 383 views

- first: `FRAN_0464_06736_L-medium.jpg`
- last: `FRAN_0464_07118_L-medium.jpg`
- total: **383**

Direct first image:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_06736_L-medium.jpg

Direct last image:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07118_L-medium.jpg

The first inspected document is dated **26 July 1897** on Lycée Louis-le-Grand letterhead. Browser navigation context places this range in the late-1890s Vth-Section correspondence target, making it directly relevant to the 1898–99 sweep. Final archival citation should still preserve the exact gallery `udId` / parent mapping once recorded.

### Range B — 435 views

Gallery URL:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/multimedia/Galerie.action?irId=FRAN_IR_061975&udId=c-4djk5r1n8--72f9e5zjfghl

- first: `FRAN_0464_07119_L-medium.jpg`
- last: `FRAN_0464_07553_L-medium.jpg`
- total: **435**

Internal evidence near views 426–434 dates this range to the 1901 succession/candidature context and therefore to the later 1900–1912 correspondence sequence.

The two ranges are directly consecutive (`07118` → `07119`).

### Local harvest

Generic harvester:

`tools/harvest_siv_gallery.ps1`

Project wrapper:

`tools/harvest_project2_ephe_ranges.ps1`

Commands:

```powershell
.\tools\harvest_siv_gallery.ps1 -StartImage 6736 -EndImage 7118 -Name "EPHE_FRAN0464_06736_07118"
.\tools\harvest_siv_gallery.ps1 -StartImage 7119 -EndImage 7553 -Name "EPHE_FRAN0464_07119_07553"
```

Each run:

- downloads sequential JPEGs with retries and a delay;
- skips valid existing files;
- writes a manifest and log;
- validates the expected image count;
- merges the range in numeric order to a single PDF with `img2pdf`.

---

## 4. Incidental 1901 Mauss material

The later 435-view gallery contains, near views 426–434:

- Marcel Mauss's candidature/career statement after Marillier's death;
- a C. P. Tiele recommendation dated Leiden, 1 November 1901;
- Mauss's description of his critical work for *L'Année sociologique* and a continually refined classification of religious facts;
- an explicit intention to continue work in the direction Marillier had taken, especially the **gathering and criticism of ethnographic materials**;
- attached bibliographic/classification working sheets for several periodicals;
- `Söderblom: Les Fravashis` classified among beliefs/rites concerning the dead.

This is a useful vertical witness to Marillier's methodological afterlife, but it should remain ancillary to the main Project 2 question: **find an independent Marillier-student notebook/working corpus comparable to Lovejoy 005.**

---

## 5. Nathan Söderblom archive: notebook ranges now confirmed

Official Alvin record:

https://alvin-portal.org/alvin/view.jsf?pid=alvin-record%3A13019

Archive:

- `Nathan Söderbloms efterlämnade papper`
- Uppsala University Library, Carolina Rediviva
- shelfmark: `N. Söderblom`
- format: **Non digital**

The archive tree explicitly lists notebook/diary groups that overlap the Marillier period:

- `Dag- och anteckningsböcker 1894-1899`
- `Dag- och anteckningsböcker 1896-1901`
- `Dag- och anteckningsböcker 1898-1915`
- `Almanackor 1892-1899`

This materially upgrades the earlier finding-aid description. The archive should be treated as a physical notebook target with online metadata/finding aids, not as an already digitized notebook corpus.

A separate user-supplied 25-page Uppsala finding aid inspected on 2026-08-19 contains a distinct block:

`Minnen 1894-1901. Parisåren`

including categories such as:

- `Föreningar och institut`
- `Religion och kyrka`
- invitations/programmes
- `Diverse`

This Paris-years block is a secondary target and should not be confused with the actual `Dagböcker / anteckningsböcker` series.

---

## 6. Why Söderblom remains the highest-value control

Marillier's 1898–99 EPHE report lists Söderblom as a regular student and Lovejoy among the auditors taking an active part. Söderblom's 1898 diploma project was:

`Traces dans le Mazdéisme d'une ancienne conception sur la survivance des morts`

prepared under Léon Marillier and later expanded into *Les Fravashis* (1899).

This gives the ideal control configuration:

- same teacher;
- same year;
- closely related `survivance` problem;
- Lovejoy 005 survives;
- Söderblom notebook groups spanning 1898–99 survive.

Immediate archival question:

> Which exact physical volume(s) in the Söderblom notebook series cover Paris / EPHE / Marillier, and can Uppsala provide targeted scans?

---

## 7. Current matrix

| Target | Metadata / catalogue | Digital images | Current action |
|---|---:|---:|---|
| `FRAN_IR_061975` | **Yes** | **Yes, selected corpus** | harvest exact late-1890s ranges |
| `20190568/69` | **Yes** | **Yes, fully digitized** | scan 1897–99 correspondence for cohort names / Marillier |
| `20190568/49` dossier 1 | **Yes** | **Yes, fully digitized** | inspect 1898–99 assembly minutes |
| `F/17/13618` | **Yes** | **Yes, fully digitized via original IR** | locate student nominations / identities |
| Söderblom archive | **Yes** | parent archive = **Non digital** | identify exact notebook volume/capsule |
| Söderblom notebook groups | **Yes** | no public facsimile confirmed | targeted digitization request |
| Söderblom Paris-years `Minnen` | **Yes** | not established | inspect as secondary ephemera/loose-paper target |

---

## Bottom line

The EPHE side has moved from “in principle harvestable” to **operationally harvestable**: exact sequential SIV image ranges can be downloaded outside the unstable front end and merged into local PDFs.

Uppsala remains the decisive student-notebook target. The next high-return sequence is:

**harvest late-1890s EPHE material → resolve Travers/Schaefer identities → identify Söderblom notebook volume(s) → request targeted scans.**
