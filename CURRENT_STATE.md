# Lovejoy corpus — current state

Last synchronized: 2026-09-03
Status: **JHI v3.4 HOLD / ARCHIVE PAGE COVERAGE 191/191 / 1898 PAGE CONCORDANCE 191/191 / 004 HIGH-VALUE CLAUSE OWNERSHIP CLOSED BUT NOT DIPLOMATICALLY COMPLETE / 005 DIPLOMATIC TRANSCRIPTION ACTIVE + MARILLIER PP.31–36 SOURCE OWNERSHIP RECUT / AOS 1897 DIRECT-PRIMARY CLOSURE / MS0873 FRANCE 1898–99 ARCHIVAL-TRANSCRIPTION DIRECT READ CLOSED / MS0038 DIGITIZATION QUOTES PENDING / UNIT×RELATION v0.7**

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
- no current research contradiction requires a Blog edit;
- text production awaits publication name, affiliation/short bio, and final image choice.

Keep:

> `The formation was known but differently classified.`

Keep final visibility wording:

> `later publication venues, bibliographies, and disciplinary histories make some of those arrangements easier to see than others.`

Image order: notebook 004 PDF p.42 / manuscript p.123, subject to JHU permission; fallback to the public-domain opening page of Lovejoy's 1898 JAOS article.

The 3 Sep MS-0873 actor-level evidence raises the evidentiary ceiling for the Paris formation claim but does not itself require Blog expansion. The new Marillier source-ownership recut likewise does not force a rewrite; if the Paris/Marillier sentence is reopened, reserve distinctiveness for Lovejoy's selection, reassignment, recomposition, and later generalization rather than the underlying determinant-specific decomposition.

## 2. Archival core — authoritative state

### Coverage versus completion

- notebook 004: 71/71 first-pass pages; targeted original-image second pass conceptually closed for the present argument; high-value clause-level source ownership closed through Rounds 21/21b; micro-paleographic, foreign-language, and bibliographic residue remains; **not a full diplomatic edition**;
- notebook 005: 120/120 first-pass pages; targeted original-image rechecks through Round 20; **diplomatic transcription remains active and incomplete**;
- combined material-form overview: 191/191 pages.

`191/191` is a coverage statement, not a completion statement. A populated `corrected_text` field can contain diplomatic visible wording, readable fragments, or an editorial argument summary. It must not be treated as proof that a page has been fully transcribed.

Diplomatic completion authority:

`TRANSCRIPTION_COMPLETION_QUEUE.md`

The authoritative page records are the twelve paginated clean JSON batches in `archive_transcriptions/`. No aggregate `MS38_004_clean.json` or `MS38_005_clean.json` is current or required.

The integrated human-readable reading surface is:

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`

It presents 004 pp.1–71 followed by 005 pp.1–120 and retains page metadata, confidence, witness/text-layer status, supplementary evidence fields, and uncertainty lists. The stable filename contains `final`, but this is **not** a claim of full diplomatic completion.

Source-critical authority:

- `QUELLENFORSCHUNG_CURRENT_GATE.md`;
- `research_notes/QUELLENFORSCHUNG_round21_clause_level_source_boundary_recut_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round21b_pp048-071_authorial_seams_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round22_005_pp031-036_Marillier_clause_ownership_2026-09-03.md`;
- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- Round-17 and Round-18 machine-readable delta registers under `archive_transcriptions/`.

### 004 clause-level argument/source closure

The old page-level source map has now been recut at clause level. Main current controls:

- p.17: the explicit Lovejoy supplement begins at `To R.D.'s remark it shld be added`; the preceding Rhys-Davids uptake extends farther than the visible material section break;
- pp.20–30: SN 12.2 spine + Warren/Childers/Oldenberg source apparatus + local annotations, not one continuous Lovejoy translation;
- p.30: the Saṅkhāruppatti `powerful princely family / thinks / dwells / cherishes` packet closes to Oldenberg's English *Buddha*;
- p.31: Four-Truths/twelve-nidāna parallel and direct/reverse replacement are source-owned by Rhys Davids/Oldenberg, *Vinaya Texts*, I, p.75;
- p.32: Rhys-Davids source block ends before `What appears to me ...`; subsequent `3–9 / 1–2 / 10–12` segmentation remains provisional A2;
- pp.34–35: numerical khandha and `Kamma ... is the link` continuity packet is Childers-owned;
- p.36: canonical locus is SN 38.12; exact nineteenth-century English mediation remains open;
- p.42 / ms p.123: `viññāna is temporally (?) an antecedent of nāma-rūpam, & logically a subdivision of it`; constituent facts are upstream, exact relation-pair remains local synthesis absent a closer carrier;
- pp.43–47: much of the classificatory/Milinda/Oldenberg material is source-owned, sharpening p.42 as a local seam rather than a page-wide authorial block;
- p.49: `discoverable logical system` remains a secure Lovejoy response after explicit Senart transition;
- p.51: `But is tre necessarily any ontological function involved? A.O.L.` is an unusually strong marked author seam;
- p.52: `the whole enumeration is secondary as to origin & composite as to character` belongs propositionally to the Senart historical-anatomy field; Lovejoy's new local module begins at `And what of nāmarūpa?` and the subsequent scholastic-reconciliation critique;
- p.62: `This is all that is required for the purposes of my paper` is a strong claim-jurisdiction marker;
- p.66: ethical upādisesa direction is Oldenberg-led, while Lovejoy repackages usage evidence and carries the argument almost verbatim into 1898;
- p.68: `Original Elements / Derived Elements` is a Lovejoy-specific allocation inside a field where stratification itself is inherited.

Only three narrow carrier HOLDs remain worth preserving: p.32 `v. p.167`; p.36 immediate English mediation; p.53 immediate upstream carrier despite strong notebook-to-print continuity. None justifies broad reopening.

Terminal routing:

- `research_notes/QUELLENFORSCHUNG_round21_clause_level_source_boundary_recut_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round21b_pp048-071_authorial_seams_2026-09-03.md`.

### 005 diplomatic transcription — active

Existing direct-image controls remain:

- pp.3–6: future-life continuity, moral recompense, natural/supernatural classification, vengeance, and purification separated;
- pp.16–19: missionary contact and borrowed notions treated as evidentiary contamination problems;
- pp.29–30: physically inserted Marillier survivance sheets separated from host-page prose;
- p.49: Tylor praised for not constructing theories beyond his evidence;
- pp.53, 55, 64: named sacrificial forms decomposed into distinct mechanisms;
- p.66: ritual type partly indexed by community versus technically competent priestly performer;
- p.69: human/animal substitution direction corrected from the original image;
- pp.92–96: June 13 and June 20 Marillier insert layers separated from underlying notebook continuity;
- p.104: direction fixed as human sacrifice -> domestic-animal substitute;
- pp.117–120: high-value terminal synthesis and mechanism loci rechecked.

### Round 22 — 005 pp.31–36 Marillier source-ownership recut

Primary external control: Léon Marillier, `La survivance de l'âme et l'idée de justice chez les peuples non civilisés` (1893).

State-bearing result:

- p.31 rank/age/sex/occupation continuity is Marillier-owned at proposition/classification level;
- p.32's broad non-moral determinant field — skill, hazard, ritual/bodily qualification, burial, sacrifice, access conditions — is already explicitly decomposed by Marillier;
- p.33's current `offerings/distributions versus cult addressed to the dead` distinction has no exact Marillier match recovered in the focused pass and is therefore the principal local authorial HOLD;
- p.34's Tonga/Bolotoo -> Tahiti -> Marquesas sequence is a continuous Marillier packet; source-level `[Tonga?]` can be resolved, while manuscript spelling remains image-dependent;
- p.35's rank-continuity proposition is Marillier-owned; exact Lovejoy selection/order remains open;
- p.36's old `great tree` synthesis conflates at least Futuna `fale-mate` (hollow tree/rock), New Zealand annihilation, and AmaZulu continuation packets;
- the canonical summary's phrase `Lovejoy explicitly asks whether this represents annihilation or rather continued existence...` is **withdrawn as an A2 claim** until the page image confirms a real Lovejoy question.

This does not alter canonical `corrected_text`: printed-source collation cannot license manuscript wording.

Current split-image limitation: the earlier Round-19/20 conversation had `MS38_004_001_061_005_1-40.pdf` as governing visual witness, but the current Library surface does not expose that binary. The source problem is substantially closed; diplomatic verification remains blocked on direct image access rather than on bibliography.

Direct-image priority when the split PDF is accessible:

1. p.33 — offerings/distributions versus cult distinction;
2. p.36 — separate Futuna/New Zealand/AmaZulu blocks and verify any annihilation/continuation question;
3. p.32 — test whether `struggle for survival` or equivalent is an actual Lovejoy heading/reclassification;
4. p.35 — exact examples/order;
5. p.31 — wording and any local reclassification;
6. p.34 — Lovejoy's exact spellings/abbreviations.

Terminal routing:

- `research_notes/MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md`;
- `research_notes/QUELLENFORSCHUNG_round22_005_pp031-036_Marillier_clause_ownership_2026-09-03.md`;
- `research_notes/MS38_005_round20_p016-030_contact_sociality_marillier_insert_recheck_2026-09-01.md`.

Current archive action: **finish 005 diplomatically page by page**, starting with pp.31–36 when the split image is available; otherwise advance to the next image-accessible queue item without promoting source collation into diplomatic text. The nominal queue after pp.31–36 remains pp.42–43, then pp.47–60.

## 3. AOS 1897 and the 1898 publication path — direct-primary closure

Authoritative dossier:

`research_notes/AOS_1897_Lovejoy_election_read_by_title_and_technical_terms_precursor_2026-09-01.md`

Closed:

- Lovejoy is absent from the complete 40-person attendance list for the Baltimore meeting, 22–24 April 1897;
- paper No.30 was read by title in his absence;
- the 10 April circular announces `Critical summary of the argument of the Milinda-pañha`;
- the final proceedings describe No.30 as `On the meaning of the Buddhist technical terms ...`;
- Lovejoy was elected an AOS corporate member at that meeting, on recommendation of the Directors collectively;
- the Historical Study of Religions Section was instituted at the same meeting;
- the 1898 membership structure does not list Lovejoy among the Section's members.

Safe publication-path judgment:

> **The late-April 1897 technical-terms communication is a strong direct title-chain/publication-path precursor to the 1898 JAOS article. Manuscript identity and exact textual continuity remain unproved.**

Do not write that Lovejoy personally delivered the paper, that Lanman or Toy individually nominated him, or that corporate AOS membership establishes Section membership.

## 4. Milinda notebook-to-print architecture / full 1898 concordance

Authoritative correction:

`research_notes/Milinda_witness_reassignment_MS97_direct_image_Trenckner_p32_correction_2026-09-01.md`

Current model:

> **Object recomposition + selective witness retention + source-resolution upgrade + witness reassignment/evidentiary reattachment.**

Full concordance authority:

- `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md`;
- `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.csv`.

State-bearing result:

- all 191 PDF pages are classified once: T3=16, T2=14, T1=17, C=12, A=41, N=89, X=2;
- every T3/T2/T1 positive page-to-print correspondence belongs to MS38_004;
- MS38_005 supplies no direct textual or argumentative antecedent to the 1898 article; its A pages are analytical parallels only;
- the concordance closes page accounting, not diplomatic transcription or manuscript identity with the 1897 communication.

## 5. Governing analytical architecture

Core:

`WHAT UNIT? -> WHAT RELATION? -> WHAT EVIDENCE LICENSES IT?`

Revision control:

`CHALLENGE -> WHAT CHANGES?`

Source-ownership control:

`WHO OWNS THE PROPOSITION? -> WHO OWNS THE RELATION? -> WHAT DOES LOVEJOY ACTUALLY CHANGE?`

Keep separate:

1. claim revision or scope restriction;
2. case substitution with claim held fixed;
3. analytic-unit rescaling;
4. carrier/canonical reclassification;
5. circulation with no demonstrated change.

Active matrix:

`research_notes/unit_relation_matrix_v0_7_augmented_1892_2026_2026-08-31.tsv`

Do not create v0.8 until a genuinely distinct proposition family accumulates.

## 6. Hard firewalls

- `PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION`.
- `PAGE-LEVEL CORRESPONDENCE != DIPLOMATIC TEXTUAL IDENTITY`.
- `ANALYTIC PARALLEL != PUBLICATION GENEALOGY`.
- `NOTEBOOK HANDWRITING != PROPOSITION AUTHORSHIP`.
- `SOURCE-OWNED CONSTITUENTS != SOURCE-OWNED RELATION`.
- `PRINTED SOURCE COLLATION != RECOVERY OF ILLEGIBLE MANUSCRIPT WORDING`.
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
- `ARCHIVAL TRANSCRIPTION WITNESS != AUTOGRAPH LETTER`.
- `INTENDED COURSE != ACTUAL COURSE != PRIVATE SUBSTITUTE PEDAGOGY`.

## 7. Exact next actions

1. Archive: if `MS38_004_001_061_005_1-40.pdf` becomes directly accessible, execute the Round-22 image queue p.33 -> p.36 -> p.32 -> p.35 -> p.31 -> p.34; do not import Marillier print into the hand.
2. If that split image remains unavailable, continue with the next directly accessible 005 queue item: pp.42–43, then pp.47–60.
3. After a canonical transcription batch actually changes, regenerate the integrated reading surface and run `python tools/audit_repository.py`.
4. AOS: obtain a true page image of JAOS 18 (1897), p.389 and diplomatically transcribe the full No.30 title; then search correspondence/submission records for the version relation.
5. Publication genetics, if intentionally resumed: phrase-level collate the T3 notebook loci against a page-image/OCR-controlled JAOS witness.
6. Blog: when user/editor inputs are ready, regenerate the v3.4 DOCX and rerun render QA.
7. Wider method control: direct-read a post-Mew Skinner text only if that comparative branch is intentionally resumed.
8. JHU reproduction: **wait for the formal Digitization quotes** for Box 62 item 2 and Box 38 folders 9–11; do not send a duplicate request.

## 8. Paris 1898–99 / MS-0873 archival transcription witness — direct-read closure

Authoritative dossier:

`research_notes/MS0873_France_1898_99_Wilson_transcriptions_direct_read_2026-09-03.md`

Archival logistics / rights / pending reproduction:

`archive_index/JHU_MS0873_MS0038_remote_reproduction_status_2026-09-03.md`

Source status:

- JHU supplied `MS873_001_001_France 1898-99.pdf`, 18 scanned pages of Daniel J. Wilson's transcriptions;
- JHU reports MS-0873 consists of five chronological binders;
- this is direct access to an **archival transcription witness**, not direct inspection of Lovejoy's autograph letters.

State-bearing actor-level results:

1. **9 Oct 1898:** Lovejoy expects an interesting year of work in `philosophy and comparative religion`.
2. **20 Oct 1898:** Lovejoy defines a Buddhist project `from a philosophical point of view` and diagnoses a jurisdiction gap: philologists expound the literature but neglect philosophy, while philosophers reconstruct conceptions without attending to textual technicalities.
3. **20 Oct 1898:** Sylvain Lévi is selected as the scholar Lovejoy wants to study under; Buddhism and biblical Wisdom are joined through the problem of evil; Lovejoy simultaneously says his fellowship requires principal work in what is ordinarily understood as philosophy.
4. **1/5 Dec 1898:** there is no Pāli Buddhism course that year. Lovejoy proposes occasional private reading at Lévi's house. Wilson's typescript reads **`Petakas`**. Preserve `Petakas` diplomatically; likely normalization to `Piṭakas` remains editorial. Do not silently substitute `Jātakas`.
5. The same December letter documents Maurice Vernes on Psalms for the `Wisdom work`, Jean Réville on the Fourth Gospel, Faculty of Theology library use for Wisdom commentaries, and a Sabatier Acts course tried and abandoned as too far outside that year's work / too technically presuppositional.
6. **29 Jan 1899:** Lovejoy records enthusiastic reading of Guyau. Treat this as adjacent intellectual evidence, not a demonstrated causal source for later method.

Current strongest formulation:

> **Before and during the Paris year, Lovejoy explicitly described a research problem produced by the separation of philological textual expertise from philosophical reconstruction, and sought study capable of joining the two.**

This upgrades the Paris branch from later biography to actor-level wording preserved in Wilson's archival transcription. It does not close autograph verification and does not establish a total-method genealogy from Lévi, Marillier, comparative religion, or any single teacher.

JHU MS-0038 reproduction status:

- Box 62 item 2, `Evolution of Religion notes`: very fragile, detached covers, approx.230 pages, formal quote pending;
- Box 38 folders 9–11, `Primitive Religion`: double-sided notes, often folded or inside envelopes, formal quote pending;
- known generic Digitization rate from correspondence: $35/hour, with an earlier stated processing time up to eight weeks;
- JHU source-credit request for publication images: `Special Collections, Sheridan Libraries, Johns Hopkins University`; JHU does not claim copyright in the Lovejoy papers and leaves copyright investigation to the researcher.

## Restart shorthand

> **Current = 191/191 page coverage, not diplomatic completion. 004 high-value source ownership is clause-level closed for the present argument, with only three narrow carrier HOLDs. 005 diplomatic transcription is active. For pp.31–36, Marillier source ownership is substantially recut: much of the apparent determinant-specific future-life typology is source-owned, while p.33 and any page-level Lovejoy headings/questions/reorderings remain image-dependent. If the 1–40 split image is unavailable, move to the next image-accessible queue rather than upgrading editorial summaries. AOS 1897 and the full 1898 page concordance remain closed at their stated ceilings. MS-0873 France 1898–99 is direct-read at archival-transcription level, autograph verification remains open. JHU reproduction quotes are pending. Blog v3.4 is production-held, not research-blocked.**
