# Project 2 — Archives nationales SIV URL / image-range ledger

**Date recovered:** 2026-08-19

This note records the exact URLs, gallery identifiers, image sequences, and code entry points recovered while tracing EPHE Vth Section material for the Marillier–Lovejoy student-notebook control project.

---

## 1. Main EPHE digitization inventory

Project inventory:

https://www.siv.archives-nationales.culture.gouv.fr/siv/IR/FRAN_IR_061975

Interactive inventory page:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/ir/consultationIR.action?irId=FRAN_IR_061975

Archives-numérisées results, second half of the 88-result list:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/recherche/ir/rechercheConsultationResultat.action?etatsauvegarde=&formCaller=&irId=FRAN_IR_061975&gotoArchivesNums=true&details=false&page=45&defaultResultPerPage=45

PDF export:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/ir/pdfIR.action?irId=FRAN_IR_061975

XML export:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/ir/exportXML.action?irId=FRAN_IR_061975

---

## 2. SIV direct-image URL pattern

The gallery serves individual JPEGs at stable URLs:

`https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_XXXXX_L-medium.jpg`

Once the image-ID interval is known, the JavaScript gallery is not needed for sequential harvesting.

---

## 3. Recovered Range A — 383 views

Observed total: **383 views**.

Recovered sequence:

- gallery view 1 → `FRAN_0464_06736_L-medium.jpg`
- gallery view 383 → `FRAN_0464_07118_L-medium.jpg`

Direct first image:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_06736_L-medium.jpg

Direct last image:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07118_L-medium.jpg

The first inspected image is a letter on Lycée Louis-le-Grand letterhead dated **26 July 1897**. The navigation context places this range in the late-1890s Vth Section secretariat correspondence target. Before making a final cote-level citation, retain the gallery `udId` / parent mapping if recovered from the browser.

PowerShell command:

```powershell
.\tools\harvest_siv_gallery.ps1 `
    -StartImage 6736 `
    -EndImage 7118 `
    -Name "EPHE_FRAN0464_06736_07118"
```

Expected output:

- `~/Downloads/EPHE_FRAN0464_06736_07118/` — 383 JPEGs + manifest + log
- `~/Downloads/EPHE_FRAN0464_06736_07118.pdf`

---

## 4. Recovered Range B — 435 views

Gallery URL:

https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/multimedia/Galerie.action?irId=FRAN_IR_061975&udId=c-4djk5r1n8--72f9e5zjfghl

Observed total: **435 views**.

Recovered sequence:

- gallery view 1 → `FRAN_0464_07119_L-medium.jpg`
- gallery view 428 → `FRAN_0464_07546_L-medium.jpg`
- gallery view 429 → `FRAN_0464_07547_L-medium.jpg`
- gallery view 430 → `FRAN_0464_07548_L-medium.jpg`
- gallery view 431 → `FRAN_0464_07549_L-medium.jpg`
- gallery view 432 → `FRAN_0464_07550_L-medium.jpg`
- gallery view 433 → `FRAN_0464_07551_L-medium.jpg`
- gallery view 434 → `FRAN_0464_07552_L-medium.jpg`
- gallery view 435 → `FRAN_0464_07553_L-medium.jpg`

Direct first image:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07119_L-medium.jpg

Direct view 428:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07546_L-medium.jpg

Direct view 429:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07547_L-medium.jpg

Direct view 430:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07548_L-medium.jpg

Direct view 431:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07549_L-medium.jpg

Direct view 432:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07550_L-medium.jpg

Direct view 433:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07551_L-medium.jpg

Direct view 434:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07552_L-medium.jpg

Direct last image / view 435:

https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07553_L-medium.jpg

Internal evidence near views 426–434 dates this gallery to the **1900–1912** correspondence sequence rather than the 1886–1899 target. It contains Marcel Mauss's 1901 candidature material after Marillier's death and C. P. Tiele's recommendation dated Leiden, 1 November 1901.

PowerShell command:

```powershell
.\tools\harvest_siv_gallery.ps1 `
    -StartImage 7119 `
    -EndImage 7553 `
    -Name "EPHE_FRAN0464_07119_07553"
```

Expected output:

- `~/Downloads/EPHE_FRAN0464_07119_07553/` — 435 JPEGs + manifest + log
- `~/Downloads/EPHE_FRAN0464_07119_07553.pdf`

---

## 5. Run both recovered ranges

Wrapper script:

`tools/harvest_project2_ephe_ranges.ps1`

Run from repository root:

```powershell
.\tools\harvest_project2_ephe_ranges.ps1
```

This calls `tools/harvest_siv_gallery.ps1` twice and produces both PDFs.

---

## 6. Code behavior

`tools/harvest_siv_gallery.ps1`:

- downloads the sequential SIV JPEG range;
- sends a browser-like User-Agent and SIV Referer;
- skips already-downloaded files above a minimum size threshold;
- retries failures;
- inserts a polite delay between requests;
- writes `manifest.tsv` with gallery index → image ID → filename → direct URL;
- writes `download_log.txt`;
- validates expected file count and suspiciously small files;
- installs `img2pdf` if absent;
- merges the JPEGs in numeric order into a single PDF without decoding all images into memory.

The explicit code is stored in:

- `tools/harvest_siv_gallery.ps1`
- `tools/harvest_project2_ephe_ranges.ps1`

---

## 7. Relevant cote-level targets from FRAN_IR_061975

From the 2025 detailed inventory PDF:

- `F/17/13618` — Vth Section, includes **Élèves : nominations (1889–1932)**; article digitized in full, images exposed through the original finding aid.
- `20190568/49`, dossier 1 — Vth Section assembly handwritten minutes, **16 Feb 1886–17 Jun 1906**, digitized in full.
- `20190568/69` — Vth Section secretariat, **Correspondance générale 1886–1899**, digitized in full, divided into three online sub-ensembles.
- `20190568/70` — **Correspondance générale 1900–1912**, digitized in full, divided into three online sub-ensembles.
- `20190568/86` — original conference reports / annuaire preparation, **1885–1891 only**.
- `20190568/391` — large-format conference programmes, **1886–1999**, digitized in full.

---

## 8. Research-use caution

Do not infer a cote solely from a sequential image ID. The JPEG sequence is a delivery-layer identifier, not an archival citation. Final citations should retain:

1. inventory ID (`FRAN_IR_061975` or original finding aid),
2. archival cote / dossier / sub-ensemble,
3. gallery `udId` where available,
4. SIV image ID (`FRAN_0464_XXXXX`),
5. handwritten/internal folio or page number where present.
