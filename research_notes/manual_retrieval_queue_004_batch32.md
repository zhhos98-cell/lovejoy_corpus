# Manual retrieval queue — notebook 004 / source-control problem

Date: 2026-08-18  
Last live sync: **2026-08-19, Batch 151**  
Status: active; substantially reduced after the full GPT-backend upload scan and deterministic route sweep.

This is a living queue. Batch 142 controls the uploaded source resolutions; Batch 150 updates access topology for Jacobi 1897; Batch 151 upgrades the Oldenberg 1897 third-edition target from edition uncertainty to an exact full-view edition-3 problem. Earlier resolved items remain documented in Batch 33/41/42 and Git history.

## Batch 142 resolution summary

### RESOLVED — Dahlmann, _Nirvāṇa_ (1896), Lovejoy's p.14 target

The uploaded full OCR resolves printed pp.13–15.

Printed p.14 does support a close/internal relation between Buddhist `anupādisesanibbāna` and orthodox `anupādhīśeṣanirvāṇa`, but Dahlmann immediately warns that the orthodox substantial-self framework cannot simply be transferred into Buddhism. Lovejoy's 1898 description of Dahlmann as placing Sanskrit `upadhi` on the `Pāli upādi` side of the lexical fork is therefore a compression of a more doctrinal/historical comparison.

**Remove from live retrieval list.**

### RESOLVED — Rhys Davids exact quotation locus

The uploaded 1894 new/revised edition of T. W. Rhys Davids, _Buddhism: Being a Sketch…_, contains the exact source of Lovejoy's quotation on printed **p.113**. Rhys Davids calls `upādi` a comprehensive name for the five skandhas and derives it, in allusion to their cause `upādāna`, from `upādā`, `to grasp`.

**Remove from live retrieval list.**

### CORRECTION — Müller p.30 is negative in the uploaded 1884 Trübner witness

Lovejoy's own 1898 article really prints `Pali Grammar, p. 30`.

In the uploaded Edward Müller, _A Simplified Grammar of the Pali Language_ (1884):

- printed **p.30** contains ordinary consonantal phonology and no relevant `upādi/upadhi` statement;
- printed **p.36** contains the relevant aspiration-loss correspondence, OCR approximately `upādisea=upadhiqesha`, with a reference to Oldenberg, _Buddha_, p.437ff.

Safest present judgment: **probable six-page citation slip in Lovejoy**, unless another differently paginated witness explains the p.30 reference. Do not silently emend the footnote.

This is no longer a missing-text problem. A pagination/edition control is optional rather than priority retrieval.

### CONTROL CONFIRMED — uploaded `buddhaseinleben03oldegoog` is the wrong edition

The title page explicitly says **`ZWEITE AUFLAGE`** and the preface is `Vorwort zur zweiten Auflage`; this is the 1890 second edition. Its printed p.273 lacks the later Senart-related note sought through Jacobi's reference.

Batch 151 now separately identifies the true 1897 third edition; keep the uploaded 1890 book only as an earlier-edition control.

### ALREADY RESOLVED / now locally controlled

- Senart 1896, `À propos de la théorie bouddhique des douze nidânas`, pp.281–297 — full _Mélanges Charles de Harlez_ upload now supplies a stable local witness.
- Jacobi 1898, `Über das Verhältnis...`, pp.1–15 — uploaded local primary control.
- Oldenberg, `Buddhistische Studien`, ZDMG 52 (1898), core pp.690–694 — uploaded extract now supplies local control through p.695.
- Hardy 1853 pp.394–396 — already recovered.
- Oldenberg 1882 English `upādisesa` excursus — already recovered.

The combined result still rejects a Lovejoy priority claim for the basic Senart/Jacobi/Oldenberg problem. The live historical question is how Lovejoy allocates evidentiary burdens and recomposes those controls.

# P0 — Jacobi's 1897 review of Dahlmann, printed pp.268–272

**This remains the highest-yield 004 retrieval. Status after Batch 150: `OBJECT_RESOLVED_TEXT_PENDING`, not source-discovery pending.**

Hermann Jacobi, review/notice of Joseph Dahlmann, _Nirvāṇa: Eine Studie zur Vorgeschichte des Buddhismus_, _Göttingische Gelehrte Anzeigen_ (1897).

Jacobi 1898 explicitly points backward to his own notice at printed **p.272** and **p.268**.

Need:
- printed **pp.268–272**, preferably **267–273** for title/boundaries/signature.

Why:
- it sits exactly between Dahlmann 1896 and Jacobi 1898;
- it can show what Jacobi thought Dahlmann's Sāṁkhya/Nirvāṇa genealogy established before the later nidāna controversy;
- it supplies a contemporary control for the standards of historical inference in the field Lovejoy entered.

### Official Academy route

Göttingen Academy repository:

- 1897, **159. Jahrgang**;
- 1064 pages total;
- separate first-volume and second-volume PDFs;
- DOI `10.26015/adwdocs-374`;
- landing page `https://rep.adw-goe.de/handle/11858/00-001S-0000-0023-BEBB-3`.

First-volume PDF remains the correct container for pp.267–273:

`https://rep.adw-goe.de/bitstream/handle/11858/00-001S-0000-0023-BEBB-3/PPN385030444_1897_159.Jg._1Bd..pdf?isAllowed=y&sequence=3`

### Batch 150 independent GDZ child-object route

The GDZ serial tree separately exposes the 1897 first half as **159,1** with child identifier:

`PPN385030444_159_1`

This is now the preferred deterministic child-object key for another extraction attempt.

Prior Internet Archive full-year mirror remains:

`https://archive.org/details/GoettingischeGelehrteAnzeigen1897-1-2`

Upload preference: page images/PDF slice covering printed **267–273**. No OCR required.

Important status rule: exact object recovery does **not** mean the review has been read. No substantive Jacobi 1897 claim is upgraded until these pages are actually inspected.

# P1 — Hermann Oldenberg, _Buddha_, true 3rd enlarged ed. (1897)

**Status after Batch 151: `TRUE_1897_EDITION_DIGITALLY_RESOLVED / EXACT_PAGE_TEXT_PENDING`.**

Need:
1. title/front matter confirming **3rd enlarged ed., 1897**;
2. printed **p.273 note** cited by Jacobi on Senart's `upādāna = upādānakkhandha` view;
3. **pp.443–455**, especially **p.448ff**, the Sāṁkhya/Buddhism excurs.

### True 1897 edition routes now controlled

Google Books full-view witness:

- object `ta7rJ6uWLfwC`;
- W. Hertz, 1897;
- metadata explicitly says **Edition 3**;
- 460 pages;
- table of contents independently places the Sāṁkhya/Buddhism appendix at **pp.443–455**.

Second full-view/free witness:

- Google Books / Google Play object `BXM_AAAAYAAJ`;
- W. Hertz, 1897;
- 460 pages;
- Google Play marks it free.

Independent page-image control:

- Online Books Page indexes the W. Hertz **1897** edition at HathiTrust.

Thus the problem is no longer finding/identifying the true third edition. It is extracting the exact page text.

### Parallel witness: Foucher 1903

Alfred Foucher's second French edition, Paris: Félix Alcan, 1903, is explicitly described in contemporary bibliography as:

`2e édition française, revue et augmentée d'après la 3e édition allemande`.

Louis de La Vallée Poussin later specifically notes that Oldenberg's `Buddha³ (1897)` Sāṁkhya appendix was suppressed in later German editions but remained in **Foucher², Paris 1903**.

Therefore Foucher 1903 is a useful parallel witness to the controversy-specific third-edition textual state. It must not replace the 1897 German text for quotation or pagination.

### Why this edition state matters

The 1897 third edition is not just a repaginated book. Jacobi points directly into a Sāṁkhya appendix that Oldenberg later removed from German editions. The correct longitudinal control is therefore:

`1890 second edition`  
→ `1897 third enlarged edition / controversy-specific additions`  
→ `1898 ZDMG intervention`  
→ `later German revision/removal`.

This may show more precisely what changed in Oldenberg's evidentiary apparatus during the exact controversy in which Lovejoy 004/1898 sits.

Upload preference: title page + p.273 + **whole pp.443–455**, not just p.448, because the appendix itself is edition-specific.

See Batch 151: `research_notes/lovejoy_as_orientalist_web_sweep_batch151_Oldenberg_1897_third_edition_parallel_witness.md`.

# P2 — Childers facsimile / citation hygiene

R. C. Childers, _A Dictionary of the Pali Language_, entry `Upādiseso`.

Current wording is already available through a modernized close reproduction. An original page capture is useful for final publication citation but no longer decisive for the 004 argument because Rhys Davids p.113 is now primary-secure.

# Optional control — Müller pagination

Only if easy: another 1884/near-contemporary Müller witness that might explain why Lovejoy cites p.30 while the relevant passage in the uploaded Trübner copy is on p.36.

The default working hypothesis should remain **citation slip**, not silently corrected fact.

# P2 — Dahlmann 1897 reception controls

Useful for controversy ecology, not evidence of Lovejoy access:

1. _Wiener Zeitschrift für die Kunde des Morgenlandes_ 11 (1897), pp.190–197, Dahlmann notice, strongly attributable to Leopold von Schroeder but still worth heading/signature control.
2. _Journal of the Royal Asiatic Society_ 29.2 (1897), pp.407–410, Dahlmann notice.

Retrieve only after the GGA Jacobi review and Oldenberg third-edition exact pages unless access is trivial.

# Harvard/Lovejoy access evidence

Batch 141 supplies exact official digital routes for Harvard course/enrollment records. The live access question remains whether Lovejoy can be shown to have encountered the newest 1897 German controversy before his 1898 article.

High-value evidence:
- Harvard 1896–97 / 1897–98 course descriptions and enrollment records around Lanman/Everett/Toy;
- Lovejoy → Wallace W. Lovejoy letters, late 1897 / early 1898;
- Lanman teaching/correspondence/Harvard Oriental Series circulation evidence.

## Current live Lovejoy tests

1. **Division of evidentiary burdens:** Senart already has filiation/stratification; Lovejoy's more specific move is to limit what genealogy can establish about semantic/systematic function.
2. **Historical-functional recomposition:** Hardy → 004 → 1898 karma/upādāna allocation.
3. **Usage under underdetermined genealogy:** Childers/Rhys-Davids versus Müller/Dahlmann plus Oldenberg → Lovejoy brackets etymology and reconstructs meaning from textual distribution/usage.
4. **Citation practice as evidence:** the Müller p.30/p.36 discrepancy is now a real source-critical problem in Lovejoy's own article, not a missing-source placeholder.
5. **Edition-state control:** Oldenberg 1897 must be treated as a controversy-specific textual state rather than silently substituted by the 1890 second edition or later German/French revisions.
6. **1902 transport:** test analogous separation of resemblance from demonstrated transmission in `Religion and the Time-Process`.

See also:
- `research_notes/lovejoy_as_orientalist_web_sweep_batch142_uploaded_manual_targets_full_scan.md`
- `research_notes/lovejoy_as_orientalist_web_sweep_batch150_remaining_primary_mirror_routes.md`
- `research_notes/lovejoy_as_orientalist_web_sweep_batch151_Oldenberg_1897_third_edition_parallel_witness.md`
- `research_notes/remaining_primary_mirror_route_resolution_batch150.csv`
