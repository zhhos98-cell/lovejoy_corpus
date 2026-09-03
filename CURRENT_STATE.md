# Lovejoy corpus — current state

Last synchronized: 2026-09-03
Status: **JHI v3.4 HOLD / ARCHIVE PAGE COVERAGE 191/191 / 1898 PAGE CONCORDANCE 191/191 / 004 ARGUMENT-CONTROL CLOSED BUT NOT DIPLOMATICALLY COMPLETE / 005 DIPLOMATIC TRANSCRIPTION ACTIVE / AOS 1897 DIRECT-PRIMARY CLOSURE / UNIT×RELATION v0.7**

This is the repository's single living state file. Historical status language elsewhere does not override it.

## Restart order

1. `CURRENT_STATE.md` — this file.
2. `TRANSCRIPTION_COMPLETION_QUEUE.md` — active manuscript completion criteria and exact page queue.
3. `CANONICAL_INDEX.md` — current navigation and authority map.
4. `ARCHIVE_TRANSCRIPTION_PROGRESS.md` and `QUELLENFORSCHUNG_CURRENT_GATE.md` for notebook work.
5. The terminal dossier named under the relevant branch below.

## 1. JHI Blog — production hold

Active text:

`research_notes/JHI_blog_full_draft_v3_4_clean_submission_2026-08-31.md`

State:

- 1,880 body words;
- four endnotes;
- no v3.5;
- generated DOCX remains v3.3 until v3.4 is regenerated and render-QA'd;
- no research contradiction currently requires a Blog edit;
- text production awaits publication name, affiliation/short bio, and final image choice.

Keep:

> `The formation was known but differently classified.`

Keep final visibility wording:

> `later publication venues, bibliographies, and disciplinary histories make some of those arrangements easier to see than others.`

Image order: notebook 004 PDF p.42 / manuscript p.123, subject to JHU permission; fallback to the public-domain opening page of Lovejoy's 1898 JAOS article.

## 2. Archival core — authoritative state

### Coverage versus completion

- notebook 004: 71/71 first-pass pages; targeted original-image second pass conceptually closed for the present argument; micro-paleographic, foreign-language, and bibliographic residue remains; **not a full diplomatic edition**;
- notebook 005: 120/120 first-pass pages; targeted original-image rechecks through Round 20; **diplomatic transcription remains active and incomplete**;
- combined material-form overview: 191/191 pages.

`191/191` is a coverage statement, not a completion statement. A populated `corrected_text` field can contain diplomatic visible wording, readable fragments, or an editorial argument summary. It must not be treated as proof that a page has been fully transcribed.

Diplomatic completion authority:

`TRANSCRIPTION_COMPLETION_QUEUE.md`

The authoritative page records are the twelve paginated clean JSON batches in `archive_transcriptions/`. No aggregate `MS38_004_clean.json` or `MS38_005_clean.json` is current or required.

The integrated human-readable reading surface is:

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`

It presents 004 pp.1–71 followed by 005 pp.1–120 and retains page metadata, confidence, witness/text-layer status, supplementary evidence fields, and uncertainty lists. The stable filename contains `final`, but this is **not** a claim of full diplomatic completion. It is generated from, and must remain exactly synchronized with, the twelve canonical JSON batches.

Source-critical authority:

- `TRANSCRIPTION_COMPLETION_QUEUE.md`;
- `ARCHIVE_TRANSCRIPTION_PROGRESS.md`;
- `QUELLENFORSCHUNG_CURRENT_GATE.md`;
- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- Round-17 and Round-18 machine-readable delta registers under `archive_transcriptions/`.

### 004 argument-control closure

The residual argument-bearing queue at p.17 and p.29 is closed by direct-image control. The earlier pp.49–52 conceptual blind queue is also closed. Main current controls include:

- p.20: `through a careful analysis (i.e. a comparison of texts)`;
- p.33: `Up.` means upādāna, not `MP`; Hardy p.394 is the immediate visible source attachment;
- p.42 / ms p.123: `viññāna is temporally (?) an antecedent of nāma-rūpam, & logically a subdivision of it`;
- p.49: `discoverable logical system`, with the crossed qualifier left unresolved;
- pp.49–52: composite origin, logical arrangement, temporal sequence, and scholastic reconciliation are distinct relations;
- pp.55–71: readable references and lexical items have been recontrolled against originals.

Terminal routing:

- `research_notes/QUELLENFORSCHUNG_round18_residual004_broad005_hygiene_2026-09-01.md`;
- `research_notes/MS38_004_round19_direct_image_reference_and_lexical_refinements_2026-09-01.md`;
- `research_notes/Lovejoy_original_image_second_pass_cross_notebook_recheck_2026-09-01.md`.

004 is conceptually closed for the present argument. It remains open as a future diplomatic-edition task if complete manuscript transcription becomes the goal.

### 005 diplomatic transcription — active

The broadened original-image pass has corrected or secured several mechanism-bearing loci:

- pp.3–6: future-life continuity, moral recompense, natural/supernatural classification, vengeance, and purification separated;
- pp.16–19: missionary contact and borrowed notions treated as evidentiary contamination problems;
- pp.29–30: physically inserted Marillier survivance sheets separated from host-page prose;
- p.49: Tylor praised for not constructing theories beyond his evidence;
- pp.53, 55, 64: named sacrificial forms decomposed into distinct mechanisms;
- p.66: ritual type partly indexed by community versus technically competent priestly performer;
- p.69: human/animal substitution direction corrected from the original image;
- pp.92–96: June 13 and June 20 Marillier insert layers separated from underlying notebook continuity;
- p.104: direction fixed as human sacrifice -> domestic-animal substitute, not the reverse;
- pp.117–120: high-value terminal synthesis and mechanism loci rechecked.

These controls establish research propositions; they do not complete the transcription of surrounding pages.

Known incomplete zones include pp.31–36, where several inserted leaves remain low/low-medium confidence with substantial illegible or untranscribed text, and pp.42–43, where Greek lexical slips remain partial. Round 20 also explicitly hands off to pp.47–60.

Terminal routing:

- `TRANSCRIPTION_COMPLETION_QUEUE.md`;
- `research_notes/QUELLENFORSCHUNG_round18b_005_source_evaluation_jurisdiction_and_insert_layers_2026-09-01.md`;
- `research_notes/MS38_005_round19_p003-006_moral_natural_purification_direct_image_2026-09-01.md`;
- `research_notes/MS38_005_round20_p016-030_contact_sociality_marillier_insert_recheck_2026-09-01.md`.

Current archive action: **finish 005 diplomatically page by page**, starting with pp.31–36, then pp.42–43, then pp.47–60, preserving later direct-image deltas already merged. After that, continue the remaining 005 blocks. Proposition-sensitive hygiene remains useful but no longer defines the completion boundary.

## 3. AOS 1897 and the 1898 publication path — direct-primary closure

Authoritative dossier:

`research_notes/AOS_1897_Lovejoy_election_read_by_title_and_technical_terms_precursor_2026-09-01.md`

Closed:

- Lovejoy is absent from the complete 40-person attendance list for the Baltimore meeting, 22–24 April 1897;
- paper No. 30 was read by title in his absence; the record does not identify whether his paper received the optional brief content statement;
- the 10 April circular announces `Critical summary of the argument of the Milinda-pañha`;
- the final proceedings describe No. 30 as `On the meaning of the Buddhist technical terms ...`;
- Lovejoy was elected an AOS corporate member at that meeting, on recommendation of the Directors collectively;
- the Historical Study of Religions Section was formally instituted at the same meeting;
- the 1898 membership structure does not list Lovejoy among the Section's members.

Safe publication-path judgment:

> **The late-April 1897 technical-terms communication is a strong direct title-chain/publication-path precursor to the 1898 JAOS article. Manuscript identity and exact textual continuity remain unproved.**

Do not write that Lovejoy personally delivered the 1897 paper, that Lanman or Toy individually nominated him, or that corporate AOS membership establishes Section membership.

## 4. Milinda notebook-to-print architecture — corrected

Authoritative correction:

`research_notes/Milinda_witness_reassignment_MS97_direct_image_Trenckner_p32_correction_2026-09-01.md`

State-bearing result:

- notebook MS95 explicitly uses Milinda as a witness for an alternate dependent-origination sequence;
- MS97 reads `Up.` and formulates upādāna as cause of the fact, karma as cause of the manner, of continued existence; it cites Hardy p.394;
- the 1898 article's explicit Milinda loci are Trenckner pp.65, 32, and 60, all in the upādāna section;
- Section II on upādi/upādisesa contains no explicit Milinda citation.

Current model:

> **Object recomposition + selective witness retention + source-resolution upgrade + witness reassignment/evidentiary reattachment.**

Hold manuscript-level identity among the 10 April announcement, late-April No. 30, and the 1898 article. The exact terms missing from the 1897 proceedings OCR remain a page-image task.

### Full notebook-to-1898 page concordance

Authoritative terminal dossier:

- `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md`;
- machine-readable companion: `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.csv`.

State-bearing result:

- all 191 PDF pages are classified once: T3=16, T2=14, T1=17, C=12, A=41, N=89, X=2;
- every T3/T2/T1 positive page-to-print correspondence belongs to MS38_004;
- MS38_005 supplies no direct textual or argumentative antecedent to the 1898 article: its 41 A pages are analytical parallels only, 77 pages are out of scope, and 005:012 plus 005:044 are chronologically excluded by post-1898 evidence;
- the densest print carryovers are the karma/upādāna causal-role distinction, the non-strict temporal architecture of dependent origination, the refusal to infer meaninglessness from composite provenance, the explicitly omitted khandha–nidāna worksheet, and the ethical-residue interpretation of upādisesa.

This closes page accounting, not diplomatic transcription. The concordance does not alter the active 005 completion queue or establish manuscript identity with the 1897 communication.

## 5. Governing analytical architecture

Core:

`WHAT UNIT? -> WHAT RELATION? -> WHAT EVIDENCE LICENSES IT?`

Revision control:

`CHALLENGE -> WHAT CHANGES?`

Keep separate:

1. claim revision or scope restriction;
2. case substitution with claim held fixed;
3. analytic-unit rescaling;
4. carrier/canonical reclassification;
5. circulation with no demonstrated change.

Active matrix:

`research_notes/unit_relation_matrix_v0_7_augmented_1892_2026_2026-08-31.tsv`

Round-10 terminal handoff:

`research_notes/HANDOFF_Lovejoy_JHI_global_history_round10_2026-08-31.md`

Do not create v0.8 until a genuinely distinct proposition family accumulates. The wider Skinner/Pocock/Haddock venue-and-revision line remains a comparative control; it does not override the Lovejoy archival core or trigger a Blog expansion.

## 6. Hard firewalls

- `PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION`.
- `PAGE-LEVEL CORRESPONDENCE != DIPLOMATIC TEXTUAL IDENTITY`.
- `ANALYTIC PARALLEL != PUBLICATION GENEALOGY`.
- `A != B` does not prove independence.
- `UNIT TYPE != RELATION TYPE`.
- `UNIT TYPE BELONGS TO CLAIM`.
- `COMMENT / CONTACT != REVISION CAUSE` without local actor or version evidence.
- `CASE SUBSTITUTION != CLAIM REVISION`.
- `SAME TEXT FAMILY != SAME VERSION STATE != SAME CANONICAL ROLE`.
- `THEORY CONSTRAINS POSSIBILITY != THEORY PROVES ACTUAL HISTORY`.
- `ANALYTICALLY EXTRACTABLE DOCTRINE != HISTORICALLY INTENDED DOCTRINE`.
- `TEXTUAL RESEMBLANCE != TRANSMISSION`.
- `ARGUMENTATIVE RUPTURE != CARRIER-FORM RUPTURE`.
- `PROGRAMME != PRACTICE != INFRASTRUCTURE != CANON`.

## 7. Exact next actions

1. Archive: follow `TRANSCRIPTION_COMPLETION_QUEUE.md`; begin 005 pp.31–36, then pp.42–43, then pp.47–60, and continue page by page.
2. Archive after each batch: regenerate the integrated reading surface and run `python tools/audit_repository.py`.
3. AOS: obtain a true page image of JAOS 18 (1897), p.389 and diplomatically transcribe the full No. 30 title; then search correspondence/submission records for the version relation.
4. Publication genetics, if intentionally resumed: phrase-level collate the T3 notebook loci against a page-image/OCR-controlled JAOS witness and record exact quotation/citation transformations.
5. Blog: when user/editor inputs are ready, regenerate the v3.4 DOCX and rerun render QA.
6. Wider method control: direct-read a post-Mew Skinner text only if that comparative branch is intentionally resumed.

## Restart shorthand

> **Current = one living state, one stable canonical index, one explicit diplomatic-completion queue, one integrated 191-page working reading surface generated from twelve paginated page-record batches, and terminal dossiers. Page coverage is complete; manuscript transcription is not. 004 is argument-control closed but not a full diplomatic edition. 005 diplomatic transcription is active, restarting at pp.31–36, pp.42–43, then pp.47–60. AOS 1897 is closed for absence/read-by-title/corporate election/Section firewall, while manuscript identity into 1898 remains held. The notebook-to-1898 concordance now classifies all 191 pages and confines positive page-to-print carryover to 004; 005 contributes analytical parallels but no direct antecedent. Blog v3.4 is production-held, not research-blocked.**
