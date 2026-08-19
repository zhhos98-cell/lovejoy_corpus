# Lovejoy as Orientalist / comparative religion — Batch 159

Date: 2026-08-19  
Status: synced  
Scope: synchronize the live evidence queue against newly uploaded source files before any further web work, so that already-resolved objects are not re-retrieved.

## Core result

The three Class-A items that Batch158 still treated as manual/text-retrieval controls are now **locally present in OCR-accessible source form**. They should no longer be searched for on the open web. The remaining task for all three is proposition-level collation against the existing 004/005 argument, not retrieval.

This changes the working mode from `targeted closing retrieval` to `targeted collation / falsification control` for A1–A3.

## A1 — Jacobi 1897 review of Dahlmann

New local witness:

- `GoettingischeGelehrteAnzeigen1897-1-2_text.pdf_by_PaddleOCR-VL-1.6.json`

Source identification is secure. The issue is *Göttingische gelehrte Anzeigen*, 159. Jahrgang, Nr. IV, issued 25 April 1897; contents list `Dahlmann, Nirvāna. Von Jacobi ..... 265–279`.

The OCR includes the review through Jacobi's signed conclusion (`Bonn, 18. November 1896. Hermann Jacobi`). The source is therefore no longer `OBJECT_RESOLVED_TEXT_PENDING`.

New status: `SOURCE_INGESTED_PRIMARY_COLLATION_PENDING`.

Next action: collate pp.267–273 against the Batch153–158 `diagnostic specificity` claim. In particular, test whether Jacobi already distinguishes evidence for isolated doctrines/components from evidence for a system-level genealogy before Lovejoy's notebook formulation.

## A2 — Oldenberg, *Buddha*, true 3rd ed. 1897

New local witness:

- `Buddha.pdf_by_PaddleOCR-VL-1.6 (1).json`

Edition identity is secure from the title page: `DRITTE VERMEHRTE AUFLAGE`; OCR throughout carries `Oldenberg, Buddha. 3. Auflage.` The full-volume source is now locally available, including the controversy-specific edition state required by Batch151–158.

New status: `TRUE_1897_EDITION_SOURCE_INGESTED_PAGE_COLLATION_PENDING`.

Next action: extract/collate printed p.273 and pp.443–455, then compare the 1897 wording with the already-ingested 1890 second-edition baseline, Jacobi 1898, Oldenberg 1898, and Lovejoy 004/1898.

## A3 — Marillier review of Steinmetz, 1896

New local witness:

- `17871212438888bsb11809713.pdf_by_PaddleOCR-VL-1.6.json`

The OCR securely identifies the notice as `R. S. STEINMETZ. — Endokannibalismus`, Vienna 1896. The text explicitly frames the religious/magical character of endocannibalism, summarizes Steinmetz's attempt to treat religious motives as superadded, and introduces the relation between ritual anthropophagy and human sacrifice.

New status: `SOURCE_INGESTED_PRIMARY_COLLATION_PENDING`.

Next action: isolate printed pp.113–115 and compare Marillier's 1896 response with Steinmetz's original, Marillier's 1897–98 anti-unilateral method, notebook 005, and the 1906 `Fundamental Concept` argument.

## Consequence for further research

Do **not** rerun open-web retrieval for A1, A2, or A3. The repo's Batch158 saturation judgment remains valid, but its evidence queue is now stale on those three rows.

Immediate order of work:

1. A1 Jacobi 1897 proposition-level collation.
2. A2 Oldenberg 1897 exact-page/edition-state collation.
3. A3 Marillier 1896 proposition-level collation.
4. Only after those controls are integrated should new web work resume, and then only on Class B/C targets or on the newly defined first-order intellectual-history question around comparison, borrowing, doctrine, arrangement, and system.

No novelty claim is upgraded merely by source arrival. This batch records retrieval state only.