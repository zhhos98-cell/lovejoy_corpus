# Quellenforschung current gate

Last synchronized: 2026-09-03
Status: **GOVERNING SOURCE-CRITICAL POLICY / 004 TARGETED IMAGE CONTROL + HIGH-VALUE CLAUSE-LEVEL SOURCE OWNERSHIP CLOSED / 005 SOURCE-FIRST DIPLOMATIC COMPLETION ACTIVE / ARCHITECTURE STABLE**

This file governs source, transcription, provenance, and uptake claims in `lovejoy_corpus`. Historical Round 12–21 files preserve the route by which readings and attributions changed; they do not override this policy or the current paginated clean batches.

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
- **A — Lovejoy authorial operation**: `A3` image-secure operation with unusually strong actor-level boundary or publication transformation; `A2` direct local supplementation/reweighting/recomposition; `A1` probable operation inferred from selection, placement, or editorial reconstruction; `A0` source-owned or unassignable.

No single label such as `closed` substitutes for these axes. An explicit manuscript author/page anchor can establish a textual node without proving possession of one unique physical edition.

## 3. Clause-level source-ownership rules

Round 21 adds a stricter attribution discipline:

> **Notebook handwriting is a carrier, not proof of authorship of the proposition carried. Source ownership must be exhausted before Lovejoy's local operation is assigned.**

And:

> **Source ownership of the constituent propositions does not automatically establish source ownership of the relation Lovejoy draws between them.**

Operational consequences:

- `PAGE CONTAINS PROPOSITION != LOVEJOY AUTHORS PROPOSITION`;
- `COPIED FIRST-PERSON SOURCE LANGUAGE != LOVEJOY FIRST-PERSON JUDGMENT`;
- `MATERIAL SECTION BREAK != SOURCE BREAK`;
- `SOURCE-OWNED MODEL IN NOTEBOOK != LOVEJOY'S OWN SOLUTION`;
- `SOURCE-SUPPLIED FACT A + SOURCE-SUPPLIED FACT B != SOURCE-SUPPLIED RELATION A:B`;
- an exact source match may lower `A` while simultaneously making a nearby explicit Lovejoy seam more secure.

Primary clause-level routing:

- `research_notes/QUELLENFORSCHUNG_round21_clause_level_source_boundary_recut_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round21b_pp048-071_authorial_seams_2026-09-03.md`.

## 4. Current text authority

The twelve paginated clean batches listed in `CANONICAL_INDEX.md` are authoritative corrected text. There are no current aggregate notebook JSONs.

Merged direct-image audit trails remain provenance:

- `archive_transcriptions/MS38_004_001_061_004_round17_direct_image_deltas_p042_p049-052_2026-09-01.json`;
- `archive_transcriptions/MS38_004_005_round18_direct_image_deltas_2026-09-01.json`;
- `research_notes/MS38_004_005_transcription_corrections_round17_original_image_2026-09-01.csv`.

Material overview authority:

- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`.

Where a delta is marked merged, quote from the current clean batch while using the delta/dossier as the audit explanation. Where a later clause-level source dossier changes authorial attribution without changing visible manuscript wording, preserve the clean text and use the later dossier to govern `A` and source ownership.

## 5. Current witness/source state — notebook 004

004 has 71/71 first-pass coverage, a targeted original-image second pass conceptually closed for the present argument, and a high-value clause-level source-ownership recut now closed across the notebook.

The recut materially narrows several older page-level attributions:

- pp.12–16: Rhys Davids source uptake continues through the Brahmajāla sixty-two-opinion packet; the clean explicit Lovejoy supplement begins at p.17, `To R.D.'s remark it shld be added`;
- pp.20–30: use the model `SN 12.2 definitional spine + Warren parallel translation/commentary + Childers lexical mediation + Oldenberg explanatory grafts + local Lovejoy interventions`;
- p.30: the `powerful princely family / thinks this thought / dwells / cherishes` Saṅkhāruppatti packet closes to Oldenberg's English *Buddha*;
- p.31: Four-Truths/twelve-nidāna parallelism and direct/reverse-order replacement close to Rhys Davids and Oldenberg, *Vinaya Texts*, Part I, p.75; withdraw any statement that Lovejoy independently observed this on the page;
- p.32: Rhys Davids owns the Milindapañha source block; Lovejoy's explicit seam begins `What appears to me ...`, after which the `1–2 / 3–9 / 10–12` segmentation remains provisional A2;
- pp.34–35: the khandha numerics and `Kamma ... is the link` continuity model are Childers-owned;
- p.36: the canonical four-upādāna/removal-path locus is SN 38.12; immediate English mediation remains unresolved;
- pp.43–47: Rhys Davids/Childers/Milindapañha/Oldenberg own much of the surrounding classification and argument packet;
- p.42: the constituent facts are source-supplied, but no exact upstream formulation has surfaced for `temporally (?) an antecedent ... & logically a subdivision`; retain as strong local recomposition, not a priority claim;
- pp.48–49: Senart owns the duplication/compositeness problem and `ordre plus ou moins accidentel`; Lovejoy's explicit response begins `On Senart's account of the matter ...`, leading to `entirely false` and `discoverable logical system`;
- p.51: the initialled `But is there necessarily any ontological function involved? A.O.L.` is a high-value actor seam;
- p.52: `the whole enumeration is secondary as to origin & composite as to character` expresses Senart's proposition and is A0–A1; Lovejoy's next clean pivot is `And what of nāmarūpa?` and the subsequent local critique;
- p.53: notebook-to-1898 causal continuity is strong, but the exact upstream carrier remains HOLD;
- p.54: Childers owns the lexical field; Lovejoy's local operation is the use/semantic-transition test;
- p.56: `I incline to suspect ...` is an explicitly conjectural Lovejoy historical hypothesis; the later convergence of differently derived terms into one system-level function is a multi-source synthesis;
- pp.57–60 and pp.69–71: default to source apparatus, A0–A1, unless a specific connective clause is separately secured;
- p.62: `This is all that is required for the purposes of my paper` is W3/A3 claim-jurisdiction control;
- pp.63–66: Oldenberg already supplies much of the ethical-residue direction and evidence; p.66 is the strongest Lovejoy usage-based argument and carries near-verbatim into 1898;
- p.68: historical stratification is field-inherited, while the exact `Original Elements / Derived Elements` allocation remains a Lovejoy synthesis/hypothesis.

Residual 004 source holds are now bounded:

1. p.32 trailing `v. p.167`;
2. p.36 immediate English mediation for SN 38.12;
3. p.53 exact upstream carrier;
4. minor French/Pāli/bibliographic carriers that do not presently change authorial attribution.

These holds do **not** reopen 004 as a broad research queue. 004 remains open only for publication-grade exact quotation, a direct new source that changes authorial ownership, or future full diplomatic-edition work.

## 6. Current witness/source state — notebook 005

005 has 120/120 first-pass coverage plus broad, proposition-sensitive original-image rechecks through Round 20. It does not have full diplomatic completion.

Current direct-image controls require:

- moral recompense, social continuity, ritual condition, and naturalistic future-life explanation to remain separate;
- missionary/contact influence to be treated as source contamination, not silently assimilated evidence;
- visible ritual form to remain distinct from mechanism;
- community versus specialist performer to be usable as evidence about ritual jurisdiction;
- host-page prose and physically inserted Marillier sheets to remain distinct chronological/argumentative witnesses;
- developmental arrows to be controlled from exact verbs and syntax rather than reconstructed from thematic proximity;
- overwritten source words to remain overwritten/illegible rather than being filled by semantic best fit.

The active source-first rule for 005 is now:

`IDENTIFY PRINTED SOURCE PACKET -> EXHAUST SOURCE-OWNED ETHNOGRAPHIC / CLASSIFICATORY PROSE -> LOCATE LOVEJOY QUESTION / REORDERING / CONTRAST / SOURCE-EVALUATION SEAM -> ONLY THEN UPGRADE DIPLOMATIC OR ARGUMENTATIVE ATTRIBUTION`.

For pp.31–36, use `research_notes/MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md` as the source map. It already narrows:

- p.31 to Marillier's rank/status/occupation continuity problem;
- pp.32–33 to ritual access/provision versus moral desert;
- p.34 to the Tonga/Bolotoo -> Tahiti/Marquesas rank packet;
- p.35 to Aht/Natchez and West African rank-continuity packets;
- p.36 to distinct Futuna `fale-mate`, AmaZulu/Callaway, and possible annihilation/degradation packets.

Do not import Marillier's printed French wording into Lovejoy's notebook. Source collation can stabilize names, cases, and packet boundaries without licensing diplomatic manuscript text.

The p.62 former `Brinton article` expansion remains withdrawn. The p.69 and p.104 developmental directions must follow the corrected original-image readings. The pp.92–96 June 13/June 20 inserts cannot be flattened into underlying host-page continuity.

## 7. Material-form rules

1. A scan page can contain more than one physical and chronological witness.
2. Physical insertion proves accretion, not the date of insertion.
3. A dated heading normally dates the local page or sheet, not the whole notebook.
4. Facing-page blanks, abrupt closures, gutters, overlays, and author initials can delimit thought blocks or source/author seams.
5. Layout can establish a local operation while remaining insufficient for a genealogy of the mature unit-idea method.
6. The digitization component `061` does not establish archival Box 61.
7. A material break and a source break are independent observations and must be established separately.

## 8. Language controls

Avoid as default formulations:

- `Lovejoy invented/discovered`;
- `X taught Lovejoy method Y`;
- `Lovejoy observes X` when X is source-owned;
- `citation proves assent`;
- `same form means same mechanism`;
- `source match recovers illegible manuscript text`;
- `overview complete means diplomatic transcription complete`;
- `A != B therefore A is historically independent of B`.

Prefer:

- `explicit source node`;
- `textual archetype` or `translation lineage`;
- `source-owned proposition`;
- `local authorial seam`;
- `local supplementation/reweighting/recomposition`;
- `session-linked stratum`;
- `materially distinct insert layer`;
- `strong reconstructed sequence`;
- `editorial summary awaiting diplomatic verification`.

Additional rule:

> **A named category may be reclassified after mechanism, performer, source authority, material layer, and historical direction are inspected separately.**

## 9. Authority order

1. `CURRENT_STATE.md` for branch state.
2. This file for source-critical policy.
3. `CANONICAL_INDEX.md` for current file routing.
4. Current paginated clean JSON batch for corrected page text.
5. Latest terminal clause-level/source-critical dossier for source ownership and authorial ceiling.
6. Latest terminal direct-image dossier for image-reading rationale.
7. Delta register/CSV for machine-readable audit history.
8. Earlier rounds for provenance only.

## 10. Governing historical claim

> **Lovejoy worked within sophisticated philological and comparative-religion source environments that already supplied many of the distinctions, classifications, historical decompositions, and semantic problems visible in his notebooks. The strongest notebook evidence lies at image- or source-secure seams where he interrupts an authority, changes the relation assigned, restricts the scale of an inference, recombines source-supplied relations, or explicitly limits the jurisdiction of his own claim. In 005, the same attribution discipline applies to ethnographic packets, material insertions, mechanisms, performers, and developmental claims. These are local operational claims, not a priority or origin story for the mature unit-idea method.**

## 11. Reopening gate

Reopen a 004 locus only for a direct new witness, a contradiction, a publication-level exact quotation, or a source identification that could materially change authorial attribution. Otherwise preserve the Round-21/21b closure and residual HOLDs.

For 005, continue the active source-first diplomatic queue in `CURRENT_STATE.md` and `TRANSCRIPTION_COMPLETION_QUEUE.md`: source collation may narrow the reading target, but only direct manuscript images can license Lovejoy's exact wording.