# Lovejoy as Orientalist / comparative religion — Batch 146

Date: 2026-08-19  
Status: synced  
Scope: convert the remaining public-domain/manual 005 source queue from a list of viewer targets into a deterministic digital-object/API map. This batch does not substitute access metadata for reading. Its purpose is to make the next extraction pass finite and reproducible.

## Core result

After Batch 142 closed RHR 37 and Batch 145 fixed the RHR 34 / Oldenberg 1897 routes, almost the entire remaining 005 manual queue can now be expressed as stable institutional object identifiers rather than ad hoc browser searches.

Three Bavarian State Library / MDZ objects cover four of the live RHR targets:

- `bsb11809713` — RHR 34 (1896): Marillier review of Steinmetz, printed pp.113–118;
- `bsb11864666` — RHR 38 (1898): Northcote Whitridge Thomas, printed pp.295–347;
- `bsb11615030` — RHR 25 (1892): Marillier, `M. Frazer et la Diane de Nemi`, pp.71–99, and Marillier's Codrington review, pp.231–232.

The Bavarian State Library's official MDZ interface documents a stable IIIF Presentation route

`https://api.digitale-sammlungen.de/iiif/presentation/v2/{object_id}/manifest`

and page OCR route

`https://api.digitale-sammlungen.de/ocr/{object_id}/{page_num}`.

This means all four RHR targets can, in principle, be extracted by reading the manifest canvas labels and requesting only the relevant page images/OCR.

The remaining encyclopedia target is also now fixed at the object level. BnF's catalogue identifies _La Grande Encyclopédie_, tome 28 (`rabbinisme - Saas`) as digital object `NUMM-323908`, and the catalogue's `Consulter en ligne` link resolves to Gallica ARK:

`ark:/12148/bpt6k323908q`.

BnF's current API documentation gives the corresponding IIIF Presentation pattern:

`https://gallica.bnf.fr/iiif/ark:/12148/{ARK_Name}/manifest.json`

and document-text/OCR services. Thus Marillier's `Religion` article can now be treated as a finite Gallica extraction problem rather than a bibliographic unknown.

The only major live 005 primary target that is **not yet pinned to an original full-text object** is Steinmetz's 60-page _Endokannibalismus_ offprint itself. Contemporary reviews and later bibliographies securely identify it as a reprint from _Mittheilungen der Anthropologischen Gesellschaft in Wien_ XXVI (1896), pp.1–60, but the present search has not yet located a publication-grade full-view scan of the original article/offprint. This remains a true source-discovery/access problem.

No new GLA/GAL/COV identifier is created in this batch.

---

## 1. RHR 34 (1896): Marillier review of Steinmetz

Official DDB / BSB control:

- title: `Revue de l'histoire des religions ... 34 = A. 17. 1896`;
- digitization: Bayerische Staatsbibliothek;
- shelfmark: `H.g.hum. 194 fx-34`;
- URN: `urn:nbn:de:bvb:12-bsb11809713-2`;
- MDZ object ID: `bsb11809713`.

Google Books independently gives the contents boundary:

- `R Steinmetz Endokannibalismus M L Marillier` — p.113;
- next bibliographic item — p.119.

Therefore the full review is printed pp.113–118.

Deterministic machine route:

- manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11809713/manifest`
- OCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11809713/{page_num}`

Status: **object/API route resolved; page content not yet extracted/read in this environment.**

---

## 2. RHR 38 (1898): N. W. Thomas, Marillier-era student control

Official DDB record now independently confirms the identifier already preserved in the queue:

- title: `Revue de l'histoire des religions ... 38 = A. 19. 1898`;
- digitization: Bayerische Staatsbibliothek;
- shelfmark: `H.g.hum. 194 fx-38`;
- URN: `urn:nbn:de:bvb:12-bsb11864666-6`;
- object ID: `bsb11864666`.

Target:

Northcote Whitridge Thomas, `La survivance du culte totémique des animaux et les rites agraires dans le Pays de Galles`, printed pp.295–347.

Deterministic machine route:

- manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11864666/manifest`
- OCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11864666/{page_num}`

Once extracted, the relevant search vocabulary remains:

`survivance`, `origine`, `forme`, `sens`, `analogie`, `ressemblance`, `rite`, `totémisme`, `culte`, `emprunt`, `agraire`.

Status: **digitized/object route secure; primary article not yet collated in this pass.**

---

## 3. RHR 25 (1892): one object closes two remaining Marillier targets

Official DDB record:

- title: `Revue de l'histoire des religions ... 25 = A. 13. 1892`;
- digitization: Bayerische Staatsbibliothek;
- shelfmark: `H.g.hum. 194 fx-25`;
- URN: `urn:nbn:de:bvb:12-bsb11615030-8`;
- object ID: `bsb11615030`.

Google Play also exposes the 1892 RHR 25–26 bound volume as a free ebook, providing a second full-view control.

The same BSB object covers both remaining 1892 Marillier requests.

### A. `M. Frazer et la Diane de Nemi`

Bibliographically secure range:

- RHR 25 (1892), pp.71–99.

RelBib independently records this exact title/range as an electronic review of Frazer's _Golden Bough_.

Research target:

- secure primary occurrence of `mana`;
- one page before/after;
- `Codrington`, `Mélanés*` and surrounding definition/context.

### B. Review of Codrington, _The Melanesians_

Target:

- printed pp.231–232.

Research question:

what Marillier selected from Codrington at the moment of reception, especially whether `mana`, spirit-residence, taboo, efficacy, sacrifice or source-critical issues are foregrounded.

Deterministic machine route for both:

- manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11615030/manifest`
- OCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11615030/{page_num}`

Status: **one digital object now covers Priority B and Priority C; exact page text still pending.**

---

## 4. Marillier, `Religion`, _La Grande Encyclopédie_ XXVIII: exact Gallica ARK recovered

BnF catalogue identifies the thirty-one-volume _Grande Encyclopédie_ and its digitized tome 28:

- tome 28: `rabbinisme - Saas`;
- digital inventory number: `NUMM-323908`;
- `Consulter en ligne` resolves to Gallica:
  `https://gallica.bnf.fr/ark:/12148/bpt6k323908q`.

The BnF/EPHE bibliographic control gives Marillier's `Religion` at pp.341–366; some modern bibliography gives terminal p.364. The full facsimile can settle the terminal-page discrepancy.

Official BnF API documentation supplies three relevant machine services:

1. IIIF Presentation:
   `https://gallica.bnf.fr/iiif/ark:/12148/bpt6k323908q/manifest.json`
2. full document plain OCR text pattern:
   `https://gallica.bnf.fr/ark:/12148/bpt6k323908q.texteBrut`
3. content search service pattern:
   `https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k323908q&query={term}`

The current tool environment is unable to dereference these constructed Gallica URLs directly because of safe-fetch/cache restrictions, so the primary article is **not** marked recovered.

### Secondary localization control

Nicolas Meylan's _Mana: A History of a Western Category_ reports that Marillier uses `mana` six times in the article and localizes the first occurrence to p.349, where Marillier defines the term through Melanesian natural and supernatural gifts/powers. This is useful as a page target, but publication quotation should still be checked against the Gallica facsimile.

Status: **exact Gallica object and API pattern recovered; primary p.349 and article-ending facsimiles still pending.**

---

## 5. Steinmetz, _Endokannibalismus_: still the one genuine access gap

The original source is securely identified:

Rudolf S. Steinmetz, _Endokannibalismus_, Vienna, Anthropologische Gesellschaft, 1896, 60 pp.; reprinted from _Mittheilungen der Anthropologischen Gesellschaft in Wien_, vol. XXVI.

Contemporary controls:

- _The Monist_ reviewed the 60-page work in July 1896;
- W. I. Thomas reviewed it in _American Journal of Sociology_ 2 (1897), pp.610–611 and describes the tables of peoples, motives and source reliability;
- later bibliographies consistently cite the original journal as vol. XXVI (1896), pp.1–60.

Searches across Internet Archive, Google Books, DDB/MDZ and general web indexes in this pass did **not** reveal a direct full-view original scan/offprint object with stable identifier.

Thus keep the existing minimum packet request active:

- pp.36–47 (§§16–22);
- p.45 col.2;
- p.52 §26;
- pp.59–60.

Status: **bibliography and target pages secure; original page images still genuinely unresolved.**

---

## 6. Revised 005 retrieval topology

The live queue now divides into two categories.

### A. Digitized and machine-routable; extraction only

- Marillier/Steinmetz review — RHR34 / `bsb11809713` / pp.113–118;
- Thomas article — RHR38 / `bsb11864666` / pp.295–347;
- Marillier Frazer article — RHR25 / `bsb11615030` / pp.71–99;
- Marillier Codrington review — same RHR25 object / pp.231–232;
- Marillier `Religion` — Gallica `bpt6k323908q` / pp.341–366, especially p.349.

### B. Still requiring source-object discovery or manual supply

- Steinmetz _Endokannibalismus_ original/offprint, esp. pp.36–47, 45, 52, 59–60.

This is a major queue contraction. The project no longer needs broad internet discovery for A; it needs reliable extraction from known institutional manifests.

---

## 7. Evidence discipline

- Object identifiers and API patterns are access evidence, not content evidence.
- Do not cite Meylan's p.349 transcription as if it were a facsimile check.
- Do not infer Marillier's 1892 Codrington selection from his later 1897–1900 uses of `mana`.
- Do not infer Marillier's 1896 Steinmetz classification from his 1898 plural-mechanism argument.
- Do not reconstruct Steinmetz's page-level claims from Thomas/Mauss/Keane when the original packet remains pending.
- Preserve BSB/DDB rights metadata (`Kein Urheberrechtsschutz - Nur nicht kommerzielle Nutzung erlaubt`) if page images are archived locally.

## Data product

- `research_notes/MS38_005_remaining_primary_digital_routes_batch146.csv`

See also:
- `research_notes/MS38_005_manual_retrieval_queue.md`
- `research_notes/lovejoy_as_orientalist_web_sweep_batch145_primary_retrieval_endpoints_RHR34_Oldenberg1897.md`
