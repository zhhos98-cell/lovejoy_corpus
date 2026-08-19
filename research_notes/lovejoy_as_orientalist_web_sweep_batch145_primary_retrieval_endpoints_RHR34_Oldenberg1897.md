# Lovejoy as Orientalist / comparative religion — Batch 145

Date: 2026-08-19  
Status: synced  
Scope: remove avoidable viewer ambiguity from the two highest-value still-live source-control targets by converting them into deterministic digital-object/API routes: (A) Marillier's 1896 review of Steinmetz in RHR 34, and (B) Oldenberg's true 1897 third enlarged edition of `Buddha`.

## Core result

Two remaining retrieval problems are now more tightly bounded.

1. **RHR 34 / Marillier–Steinmetz** is no longer merely a Google Books/BSB viewer problem. The Bavarian State Library's official MDZ documentation exposes a stable IIIF Presentation API and page-level OCR API. Because the RHR 34 object identifier is already securely `bsb11809713`, the exact machine route is deterministic:

   - manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11809713/manifest`
   - OCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11809713/{page_num}`

   The manifest should supply canvas labels and the image/OCR endpoints needed to map printed pp.113–118 without guessing scan offsets. The current execution environment cannot complete the final API call because of network/safe-fetch restrictions; therefore the review remains **unread**, not resolved.

2. **Oldenberg 1897, third enlarged edition** is now independently fixed as a full-view digital object rather than a bibliographic possibility. Google Books metadata identifies the 1897 Hertz volume as **Edition 3**, 460 pages, original from the Bavarian State Library, and its table of contents explicitly places the Sāṁkhya excurs at **pp.443–455**. A second Google/Play object for the same 1897 edition is also free/full-view. This sharply reduces the risk of repeating the previous wrong-edition upload.

No substantive claim from either still-unread target is added. This batch is retrieval forensics, not interpretation.

---

## 1. RHR 34 object identity is primary-institutionally secure

Deutsche Digitale Bibliothek records:

- title: `Revue de l'histoire des religions ... 34 = A. 17. 1896`;
- digitization: Bayerische Staatsbibliothek;
- shelfmark: `H.g.hum. 194 fx-34`;
- URN: `urn:nbn:de:bvb:12-bsb11809713-2`;
- object identifier embedded in the URN: `bsb11809713`.

Google Books independently identifies the same volume and gives the contents sequence:

- `R Steinmetz Endokannibalismus M L Marillier` — p.113;
- `J B Bérenger-Féraud Superstitions et survivances M L Marillier` — p.119.

Therefore the Steinmetz notice occupies printed **pp.113–118**. This is no longer an inferred three-page notice: the next item boundary fixes the full six-page range.

---

## 2. MDZ's official IIIF/OCR interface turns the extraction into a deterministic machine task

The Bavarian State Library / Munich Digitization Centre documents its Presentation API as:

`https://api.digitale-sammlungen.de/iiif/presentation/v2/{object_id}/manifest`

and its OCR endpoint as:

`https://api.digitale-sammlungen.de/ocr/{object_id}/{page_num}`.

The manifest contains:

- bibliographic metadata;
- `sequences[0].canvases` for every scan page;
- Image API service identifiers for the facsimiles;
- where available, `seeAlso` links to page OCR/hOCR.

Applied to the RHR 34 object, the route is therefore:

`https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11809713/manifest`

Once the manifest is accessible, the correct workflow is:

1. locate canvases labelled printed 113–118 (or identify their sequence by neighboring printed labels);
2. capture the corresponding Image API IDs;
3. download only those six facsimile pages;
4. use the per-page OCR endpoint only as a reading scaffold;
5. collate Marillier's wording against Steinmetz p.52 §26, Mauss's reclassification, and Lovejoy 005 pp.106–119.

This avoids manual viewer clicking and avoids guessing that printed p.113 equals scan image 113.

### Current execution limitation

The present tool environment can read the MDZ API documentation and the DDB object metadata but cannot resolve the constructed manifest endpoint because direct API DNS/safe-URL calls are blocked. That is a tooling limitation, not an access-status uncertainty about the source.

Status remains:

> **digitized + exact API route known + page content still pending.**

---

## 3. Why the Marillier review remains decisive after Batch 143

Batch 143 strengthened the downstream comparison:

- Marillier 1898 p.351 explicitly separates direct/immediate blood efficacy from aid by protective gods and cites Trumbull/Strack/Dorman/Kingsley;
- Marillier's `Threshold-Covenant` review reopens Trumbull's blood evidence and attacks over-generalization;
- p.417 decomposes foundation blood into guardian-spirit, direct magical blood-force, and propitiatory-sacrifice mechanisms;
- Lovejoy 005 independently cites exact Trumbull and Kingsley pages and performs analogous reclassification.

The missing 1896 review can now answer a chronological question rather than merely a thematic one:

> **Was Marillier already applying this anti-unilateral / mechanism-sensitive operator to Steinmetz's endocannibalism in 1896, or did the sharper printed formulation emerge between the Steinmetz review and the 1897–98 Jevons/Trumbull work?**

Either answer is useful. A descriptive or communion-accepting review would date the later sharpening rather than weaken the project.

---

## 4. Mauss supplies the contemporary control but does not substitute for Marillier's review

Mauss's `La religion et les origines du droit pénal d'après un livre récent` begins in the same RHR volume 34 at pp.269–295. Its critical continuation supplies the already-secure controls:

- Steinmetz's `Endokannibalismus`, §§16–22 / pp.36–47, is cited as an example of his counterfact-sensitive method of exposition;
- p.45 col.2 is used for corpse-mutilation/body-part practices connected with magical vengeance/danger from the dead;
- p.52 §26 underlies Mauss's re-naming of `endocannibalisme` as ritual anthropophagy of relatives and his transfer-of-virtues account;
- Mauss explicitly cites Marillier's 1896 `Tabou mélanésien`, pp.53–56, as a collected Melanesian text packet;
- elsewhere Mauss says he owes much to Marillier's bibliography and course notes.

This makes the 1896 controversy unusually dense. But Mauss must remain a **contemporary Marillier-linked control**, not a proxy for what Marillier says on pp.113–118.

---

## 5. Oldenberg 1897: correct third edition is now digitally authenticated

The live 004 problem requires:

- the Senart-related note at printed **p.273** cited by Jacobi;
- the Sāṁkhya/Buddhism excurs at **pp.443–455**, especially p.448ff.

The earlier uploaded `buddhaseinleben03oldegoog` object was visually proven to be the 1890 **second edition** and cannot answer the question.

Google Books now gives a clean edition control for a different object:

- Hermann Oldenberg, `Buddha: sein Leben, seine Lehre, seine Gemeinde`;
- Hertz, 1897;
- **Edition 3**;
- 460 pages;
- original from the Bavarian State Library;
- contents explicitly list `... zum Sânkhyasystem 443–455`.

Primary route:

`https://books.google.com/books/about/Buddha.html?id=ta7rJ6uWLfwC`

A second free/full-view 1897 Google Play object:

`https://play.google.com/store/books/details/Hermann_Oldenberg_Buddha?id=BXM_AAAAYAAJ`

The second object is useful as a pagination/control witness if the first viewer behaves badly.

### Status correction

The correct wording is now:

> **true third edition digitally authenticated and full-view; target pages not yet extracted into the project corpus.**

not:

> `third edition still bibliographically uncertain`.

---

## 6. Finite retrieval packet after Batch 145

### RHR 34 / Marillier

Need only:

- printed pp.113–118;
- preferably facsimile + OCR/hOCR;
- title/item boundary visible at p.113 and next item at p.119 if practical.

### Oldenberg 1897

Need only:

- title/front matter showing third edition;
- printed p.273 including full note apparatus;
- pp.443–455, especially p.448ff.

No full-book upload is necessary unless page slicing is inconvenient.

---

## 7. Evidence discipline

- A deterministic IIIF/OCR endpoint is not the same as having read the pages.
- Do not infer Marillier's 1896 mechanism classification from his 1898 writings.
- Do not use Mauss's communion/family-solidarity interpretation as Marillier's position.
- Google Books edition metadata is sufficient to identify the 1897 Oldenberg object, but the p.273 and pp.443–455 claims still require page extraction.
- The BSB source is marked as having no copyright protection with a non-commercial-use condition in DDB; preserve source/rights metadata when archiving page images.

## Retrieval register

See:
- `research_notes/primary_retrieval_endpoint_register_batch145.csv`
- `research_notes/MS38_005_manual_retrieval_queue.md`
- `research_notes/manual_retrieval_queue_004_batch32.md`

No new GLA/GAL/COV identifier is created in this batch.
