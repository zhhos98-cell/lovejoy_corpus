# QUELLENFORSCHUNG CURRENT GATE

Date: 2026-08-31  
Status: **GOVERNING SOURCE-CRITICAL EVIDENCE GATE**

This file governs all source/provenance claims in `lovejoy_corpus` after the Round-15 hostile philological re-audit and the beginning of Round-16 original-image verification.

It supersedes, for Quellenforschung purposes only, older status language that describes `archive_transcriptions/*_clean.json` as uniformly `authoritative corrected text` or treats earlier `closed`, `direct-lock`, or `immediate carrier` labels as final.

Historical files are retained as provenance and should not be rewritten retroactively.

## 1. Critical correction to the transcription layer

The `*_clean.json` corpus is **heterogeneous in transcription mode**.

Some pages are close diplomatic/manual transcriptions of visible manuscript wording. Other batches explicitly allow the editor, where handwriting is too difficult, to retain only `source-supported argumentative structure` rather than reconstruct every lexical item.

Therefore:

> **`corrected_text` is not uniformly equivalent to Lovejoy's exact manuscript wording.**

No source attribution may use a source-supported editorial summary as independent evidence for the source that helped generate that summary.

The anti-circularity rule is:

`MANUSCRIPT VISIBLE TEXT`
≠
`EDITORIAL ARGUMENT SUMMARY`
≠
`EXTERNAL SOURCE COLLATION`.

These three layers must be kept separate.

## 2. Governing four-axis protocol

Every consequential source claim should be coded separately on four axes.

### W — manuscript witness

- `W3`: direct image/diplomatic wording secure;
- `W2`: key wording visible but syntax/source label partly uncertain;
- `W1`: editorial/source-supported argumentative reconstruction;
- `W0`: no manuscript witness.

### S — source-text match

- `S3`: explicit bibliographic anchor plus distinctive text match;
- `S2`: distinctive phrase/sequence concordance;
- `S1`: proposition/case-cluster concordance;
- `S0`: controversy-field availability only.

### T — transmission/uptake

- `T3`: direct uptake demonstrated;
- `T2`: strong carrier/source-family hypothesis, intermediary not excluded;
- `T1`: documented field/controversy route only;
- `T0`: comparison only.

### A — Lovejoy authorial operation

- `A3`: direct manuscript operation plus publication transformation;
- `A2`: direct manuscript supplementation/reweighting/recomposition;
- `A1`: probable operation inferred from editorial reconstruction;
- `A0`: source-owned or not presently assignable to Lovejoy.

## 3. Current high-confidence benchmark relations

These presently survive hostile source-critical scrutiny at the highest level or close to it:

- 004 Garbe p.150 explicit source seam; avoid claiming Lovejoy personally translated every English sentence without further proof;
- 004 Warren p.150 explicit uptake;
- 004 Rhys Davids 1896 pp.24–36 as the near-certain textual archetype of the long Sāṃkhya chronology run, while literal physical-copy possession remains a narrower question;
- 004 p.17 `To R.D.'s remark it should be added` as an actor-marked source/supplement seam;
- 004 Warren taṇhā/upādāna source sharpening;
- 004 Hardy p.394 → notebook fact/manner problem → 1898 publication stabilization;
- 004 p.42/MS123 relation split, independently checked against the manuscript page image; uniqueness/priority is not claimed;
- 005 Marillier 1898–99 programme, weekday/topic structure, and Lovejoy's documented active participation;
- 005 May 29 / June 6 / June 12 session-linked date anchors; they do not make the notebook a lecture transcript;
- 005 explicit Trumbull *Blood Covenant* p.118 and p.129 anchors;
- 005 pp.16–20 and pp.24–27 material revision/schema evidence independently checked from page images;
- **005 p.117 late sacrifice synthesis, now Round-16 image-secure at W3 for the key ranked wording:** `in gt. number of cases` alimentary/anthropophagic; `next most numerous cases` expiatory and propitiatory; `a human sacrifice for union is altogether exceptional`. One immediately following comparative clause remains paleographically uncertain and is not normalized.

## 4. Claims downgraded pending original-page recheck

The following earlier closures remain hypotheses or source-lineage identifications rather than final immediate-carrier claims:

- Sabbāsava → Rhys Davids SBE XI physical carrier;
- Siṃsapā → Oldenberg/Hoey physical carrier and conjectured manuscript `204 f.`;
- p.10 `American Legends, V. [Brinton?]` author/title reading;
- p.62 exact Brinton sacrifice item;
- p.78 Trumbull numeral and p.268f/p.299 locus assignment;
- pp.79–80 Grout as exact immediate carrier and the precise Lovejoy-local classification of the Zulu case;
- Kingsley sequential reading run unless its page numbers are independently image-secure;
- p.119 selected-body-part wording used for the 005→1906 continuity argument.

## 5. Governing language restrictions

Do not use the following as default evidentiary labels:

- `closed`;
- `direct-lock`;
- `immediate carrier`;
- `Lovejoy invention`;
- `Lovejoy discovered`;
- `X taught Lovejoy method Y`.

Prefer:

- `textual archetype`;
- `translation lineage`;
- `leading carrier candidate`;
- `explicit source node`;
- `source-family concordance`;
- `local Lovejoy supplementation`;
- `unmatched in sources checked to date`;
- `session-linked stratum`;
- `strong reconstructed sequence`;
- `editorial summary awaiting diplomatic recheck`.

## 6. Next original-image protocol

For every high-value difficult page:

1. inspect the manuscript image **without the candidate source open**;
2. make a diplomatic transcription, marking uncertain graphemes;
3. freeze that transcription;
4. only then open the external source candidate;
5. collate exact agreements, differences, omissions and sequence;
6. assign W/S/T/A grades separately.

Highest-priority remaining blind/image-controlled pages:

- 004 p.6/MS21, p.8/MS25, p.12/MS53, p.17, p.20, p.22, p.29, p.33, p.42, pp.47–52;
- 005 pp.3–6, p.10, p.11, p.27, p.29, p.47, p.62, p.78, **pp.79–80**, pp.85–86, p.89, p.103, p.119.

Round-16 completed locus:

- **005 p.117** — key late-synthesis wording recovered directly from original image; see `research_notes/QUELLENFORSCHUNG_round16_original_image_verification_2026-08-31.md` and `research_notes/MS38_005_transcription_corrections_round16_original_image_2026-08-31.csv`.

Use:

- `research_notes/QUELLENFORSCHUNG_round15_Grafton_grade_critical_reaudit_2026-08-31.md` for the full Round-15 rationale;
- `research_notes/Quellenforschung_round15_evidence_matrix_2026-08-31.csv` for the live claim-by-claim recheck ledger;
- `research_notes/QUELLENFORSCHUNG_round16_original_image_verification_2026-08-31.md` for original-image verification progress.

## 7. Governing historical claim after recalibration

The project should not depend on a priority/origin story about Lovejoy.

The strongest defensible formulation is:

> **Lovejoy worked within already sophisticated philological and comparative-religion source environments. At selected manuscript seams where the witness is secure, the notebooks show him redistributing evidentiary jobs: quotation versus inference, temporal order versus classificatory inclusion, fact versus manner, visible ritual form versus causal mechanism, and synthetic field map versus lower-witness test.**

Round-16 p.117 adds a secure late example of the last operation: Lovejoy explicitly ranks the relative incidence of sacrificial mechanisms rather than merely listing them.

This is stronger than an originality claim because the relevant transformations can be demonstrated locally without assigning Lovejoy ownership of the upstream categories or methods.
