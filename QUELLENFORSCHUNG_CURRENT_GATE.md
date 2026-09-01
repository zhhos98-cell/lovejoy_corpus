# Quellenforschung current gate

Last synchronized: 2026-09-01
Status: **GOVERNING SOURCE-CRITICAL POLICY / 004 TARGETED SECOND PASS CONCEPTUALLY CLOSED / 005 TARGETED SECOND PASS THROUGH ROUND 20 / ARCHITECTURE STABLE**

This file governs source, transcription, provenance, and uptake claims in `lovejoy_corpus`. Historical Round 12–20 files preserve the route by which readings changed; they do not override this policy or the current paginated clean batches.

## 1. Evidence layers

The archival corpus separates:

- `diplomatic_visible_text`: wording secured from the manuscript image;
- `editorial_argument_summary`: normalized argumentative content where the hand is not fully recovered;
- `external_source_collation`: comparison with an identified candidate/source text;
- `material_layout_observation`: evidence from diagrams, nesting, numbering, brackets, insertions, cancellations, slips, folds, overlays, blanks, and facing-page relations.

Compact rule:

> **MANUSCRIPT VISIBLE TEXT != EDITORIAL SUMMARY != EXTERNAL COLLATION != MATERIAL OBSERVATION.**

`corrected_text` in `*_clean.json` is not uniformly equivalent to Lovejoy's exact manuscript wording. A source-supported summary cannot independently prove the source identification that helped produce it. Exact quotation requires the page-level evidence state.

## 2. Four-axis protocol

Consequential claims are graded separately:

- **W — manuscript witness**: `W3` image/diplomatic secure; `W2` key wording visible but syntax or label partly uncertain; `W1` editorial/source-supported reconstruction; `W0` no manuscript witness.
- **S — source-text match**: `S3` explicit anchor plus distinctive match; `S2` distinctive phrase/sequence; `S1` proposition/case cluster; `S0` field context only.
- **T — transmission/uptake**: `T3` direct uptake demonstrated; `T2` strong source-family/carrier hypothesis; `T1` documented route only; `T0` comparison only.
- **A — Lovejoy authorial operation**: `A3` image-secure operation plus publication transformation; `A2` direct local supplementation/reweighting/recomposition; `A1` probable operation inferred from editorial reconstruction; `A0` source-owned or unassignable.

No single label such as `closed` substitutes for these axes. An explicit manuscript author/page anchor can establish a textual node without proving possession of one unique physical edition.

## 3. Current text authority

The twelve paginated clean batches listed in `CANONICAL_INDEX.md` are authoritative corrected text. There are no current aggregate notebook JSONs.

Merged direct-image audit trails remain provenance:

- `archive_transcriptions/MS38_004_001_061_004_round17_direct_image_deltas_p042_p049-052_2026-09-01.json`;
- `archive_transcriptions/MS38_004_005_round18_direct_image_deltas_2026-09-01.json`;
- `research_notes/MS38_004_005_transcription_corrections_round17_original_image_2026-09-01.csv`.

Material overview authority:

- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`.

Where a delta is marked merged, quote from the current clean batch while using the delta/dossier as the audit explanation.

## 4. Current witness state — notebook 004

004 has 71/71 first-pass coverage and a targeted original-image second pass that is conceptually closed for the present argument. Important later controls include:

- p.17: comparison is weighted rather than merely accumulated;
- p.20: `careful analysis (i.e. a comparison of texts)`;
- p.29: Childers/Müller recorded as an interpretive fork;
- p.33: `Up.`, not `MP`; Hardy p.394 attached;
- p.42: temporal antecedence and logical subdivision both explicit;
- p.49: `discoverable logical system`, not `technical system`;
- pp.49–52: composite origin, logical arrangement, temporal sequence, and scholastic reconciliation separated;
- pp.55–71: high-value references and readable lexical items recontrolled.

Residual uncertainty is genuinely diplomatic or bibliographic: compressed foreign-language forms, crossed wording, and small references. Do not reopen 004 as a broad research queue merely because the corpus is not a full diplomatic edition.

## 5. Current witness state — notebook 005

005 has 120/120 first-pass coverage plus broad, proposition-sensitive original-image rechecks through Round 20. It does not have full second-pass closure.

Current direct-image controls require:

- moral recompense, social continuity, ritual condition, and naturalistic future-life explanation to remain separate;
- missionary/contact influence to be treated as source contamination, not silently assimilated evidence;
- visible ritual form to remain distinct from mechanism;
- community versus specialist performer to be usable as evidence about ritual jurisdiction;
- host-page prose and physically inserted Marillier sheets to remain distinct chronological/argumentative witnesses;
- developmental arrows to be controlled from exact verbs and syntax rather than reconstructed from thematic proximity;
- overwritten source words to remain overwritten/illegible rather than being filled by semantic best fit.

The p.62 former `Brinton article` expansion remains withdrawn. The p.69 and p.104 developmental directions must follow the corrected original-image readings. The pp.92–96 June 13/June 20 inserts cannot be flattened into underlying host-page continuity.

## 6. Material-form rules

1. A scan page can contain more than one physical and chronological witness.
2. Physical insertion proves accretion, not the date of insertion.
3. A dated heading normally dates the local page or sheet, not the whole notebook.
4. Facing-page blanks, abrupt closures, gutters, overlays, and author initials can delimit thought blocks or source/author seams.
5. Layout can establish a local operation while remaining insufficient for a genealogy of the mature unit-idea method.
6. The digitization component `061` does not establish archival Box 61.

## 7. Language controls

Avoid as default formulations:

- `Lovejoy invented/discovered`;
- `X taught Lovejoy method Y`;
- `citation proves assent`;
- `same form means same mechanism`;
- `source match recovers illegible manuscript text`;
- `overview complete means diplomatic transcription complete`;
- `A != B therefore A is historically independent of B`.

Prefer:

- `explicit source node`;
- `textual archetype` or `translation lineage`;
- `local supplementation/reweighting/recomposition`;
- `session-linked stratum`;
- `materially distinct insert layer`;
- `strong reconstructed sequence`;
- `editorial summary awaiting diplomatic verification`.

Additional rule:

> **A named category may be reclassified after mechanism, performer, source authority, material layer, and historical direction are inspected separately.**

## 8. Authority order

1. `CURRENT_STATE.md` for branch state.
2. This file for source-critical policy.
3. `CANONICAL_INDEX.md` for current file routing.
4. Current paginated clean JSON batch for corrected page text.
5. Latest terminal direct-image dossier for the rationale and evidence ceiling.
6. Delta register/CSV for machine-readable audit history.
7. Earlier rounds for provenance only.

## 9. Governing historical claim

> **Lovejoy worked within sophisticated philological and comparative-religion source environments. At selected image-secure manuscript seams, the notebooks show him redistributing evidentiary jobs: quotation versus inference, temporal order versus classificatory inclusion, fact versus manner, visible ritual form versus causal mechanism, competent performer versus ritual category, host page versus inserted witness, and developmental proposal versus chronological test. Publication may retain propositions while reassigning their primary-text warrants. These are local operational claims, not a priority or origin story for the mature unit-idea method.**

## 10. Reopening gate

Reopen a locus only for a direct new witness, a contradiction, a publication-level exact quotation, or a proposition-sensitive uncertainty that could change mechanism, direction, source attribution, or material chronology. Otherwise preserve the current closure/limit and continue from the explicit queue in `CURRENT_STATE.md`.
