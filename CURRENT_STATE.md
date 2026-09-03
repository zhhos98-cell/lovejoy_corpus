# Lovejoy corpus — current state

Last synchronized: 2026-09-03
Status: **JHI v3.4 HOLD / ARCHIVE PAGE COVERAGE 191/191 / 1898 PAGE CONCORDANCE 191/191 / 004 HIGH-VALUE CLAUSE OWNERSHIP CLOSED BUT NOT DIPLOMATICALLY COMPLETE / 005 DIPLOMATIC TRANSCRIPTION ACTIVE + SOURCE OWNERSHIP RECUT THROUGH PP.31–36 AND PP.47–75 / AOS 1897 DIRECT-PRIMARY CLOSURE / MS0873 FRANCE 1898–99 ARCHIVAL-TRANSCRIPTION DIRECT READ CLOSED / MS0038 DIGITIZATION QUOTES PENDING / UNIT×RELATION v0.7**

This is the repository's single living state file. Historical status language elsewhere does not override it.

## Restart order

1. `CURRENT_STATE.md` — this file.
2. `TRANSCRIPTION_COMPLETION_QUEUE.md` — active manuscript completion criteria and exact page queue.
3. `CANONICAL_INDEX.md` — current navigation and authority map.
4. `ARCHIVE_TRANSCRIPTION_PROGRESS.md` and `QUELLENFORSCHUNG_CURRENT_GATE.md` for notebook work.
5. Current terminal dossiers: Rounds 21/21b for 004; Rounds 22–24 for the first major 005 source-ownership blocks.

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

The 3 Sep MS-0873 actor-level evidence raises the ceiling for the Paris formation claim but does not require Blog expansion. Rounds 22–24 further narrow what may be called Lovejoy-specific in the Paris comparative-religion notebook: reserve distinctiveness for selection, reassignment, recomposition, source evaluation, social-jurisdiction mapping, and later generalization rather than for the underlying determinant/mechanism categories themselves.

## 2. Archival core — authoritative state

### Coverage versus completion

- notebook 004: 71/71 first-pass pages; targeted original-image second pass conceptually closed for the present argument; high-value clause-level source ownership closed through Rounds 21/21b; micro-paleographic, foreign-language, and bibliographic residue remains; **not a full diplomatic edition**;
- notebook 005: 120/120 first-pass pages; targeted original-image rechecks through Round 20; **diplomatic transcription remains active and incomplete**;
- combined material-form overview: 191/191 pages.

`191/191` is a coverage statement, not a completion statement. A populated `corrected_text` field can contain diplomatic visible wording, readable fragments, or an editorial argument summary. It must not be treated as proof that a page has been fully transcribed.

Diplomatic completion authority:

`TRANSCRIPTION_COMPLETION_QUEUE.md`

The authoritative page records are the twelve paginated clean JSON batches in `archive_transcriptions/`. No aggregate `MS38_004_clean.json` or `MS38_005_clean.json` is current or required.

Integrated human-readable surface:

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`

The stable filename contains `final`; this is **not** a claim of full diplomatic completion.

Source-critical authority:

- `QUELLENFORSCHUNG_CURRENT_GATE.md`;
- `research_notes/QUELLENFORSCHUNG_round21_clause_level_source_boundary_recut_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round21b_pp048-071_authorial_seams_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round22_005_pp031-036_Marillier_clause_ownership_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round23_005_pp047-060_sacrifice_clause_ownership_2026-09-03.md`;
- `research_notes/QUELLENFORSCHUNG_round24_005_pp061-075_mechanism_jurisdiction_reinterpretation_2026-09-03.md`;
- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- Round-17 and Round-18 machine-readable delta registers under `archive_transcriptions/`.

### 004 clause-level argument/source closure

Main current controls:

- p.17: explicit Lovejoy supplement begins at `To R.D.'s remark it shld be added`; preceding Rhys-Davids uptake extends beyond the visible material section break;
- pp.20–30: SN 12.2 spine + Warren/Childers/Oldenberg source apparatus + local annotations, not one continuous Lovejoy translation;
- p.30: Saṅkhāruppatti `powerful princely family / thinks / dwells / cherishes` packet closes to Oldenberg's English *Buddha*;
- p.31: Four-Truths/twelve-nidāna parallel and direct/reverse replacement are source-owned by *Vinaya Texts*, I, p.75;
- p.32: Rhys-Davids block ends before `What appears to me ...`; subsequent `3–9 / 1–2 / 10–12` segmentation remains provisional A2;
- pp.34–35: numerical khandha and `Kamma ... is the link` continuity packet is Childers-owned;
- p.36: canonical locus is SN 38.12; exact nineteenth-century English mediation remains open;
- p.42 / ms p.123: `viññāna is temporally (?) an antecedent of nāma-rūpam, & logically a subdivision of it`; constituent facts are upstream, exact relation-pair remains local synthesis absent a closer carrier;
- p.49: `discoverable logical system` remains a secure Lovejoy response after explicit Senart transition;
- p.51: `But is tre necessarily any ontological function involved? A.O.L.` remains a strong marked author seam;
- p.52: `the whole enumeration is secondary as to origin & composite as to character` belongs propositionally to the Senart historical-anatomy field; the local module begins at `And what of nāmarūpa?`;
- p.62: `This is all that is required for the purposes of my paper` remains a strong claim-jurisdiction marker;
- p.66: ethical upādisesa direction is Oldenberg-led; Lovejoy repackages usage evidence and carries the argument almost verbatim into 1898;
- p.68: `Original Elements / Derived Elements` is a Lovejoy-specific allocation inside an inherited stratification problem.

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
- pp.53, 55, 64: direct-image mechanism wording controlled;
- p.65: mingling / `delicate analysis` / prior distinctness controlled at W3 for key wording;
- p.66: whole-community expiation versus magically skilled priestly performance controlled at W3;
- p.69: animal→human substitution direction controlled at W3;
- p.73: protective rationale → `another meaning` / spirit-release reinterpretation controlled at W3 for the key relation;
- pp.92–96: June 13 and June 20 Marillier insert layers separated from underlying notebook continuity;
- p.104: direction fixed as human sacrifice -> domestic-animal substitute;
- pp.117–120: high-value terminal synthesis and mechanism loci rechecked.

### Round 22 — 005 pp.31–36 Marillier source-ownership recut

Primary control: Léon Marillier, `La survivance de l'âme et l'idée de justice chez les peuples non civilisés` (1893).

State-bearing result:

- p.31 rank/age/sex/occupation continuity is Marillier-owned at proposition/classification level;
- p.32 broad non-moral determinant field — skill, hazard, ritual/bodily qualification, burial, sacrifice, access conditions — is already explicitly decomposed by Marillier;
- p.33 `offerings/distributions versus cult addressed to the dead` has no exact Marillier match recovered and remains the principal local authorial HOLD;
- p.34 Tonga/Bolotoo -> Tahiti -> Marquesas sequence is a continuous Marillier packet;
- p.35 rank-continuity proposition is Marillier-owned; exact Lovejoy selection/order remains open;
- p.36 old `great tree` synthesis conflates at least Futuna `fale-mate`, New Zealand annihilation, and AmaZulu continuation packets;
- canonical summary phrase `Lovejoy explicitly asks whether this represents annihilation or rather continued existence...` is **withdrawn as an A2 claim** until image confirmation.

This does not alter canonical `corrected_text`: printed-source collation cannot license manuscript wording.

Direct-image priority when the 1–40 split image is accessible:

1. p.33 — offerings/distributions versus cult distinction;
2. p.36 — separate Futuna/New Zealand/AmaZulu blocks and verify any annihilation/continuation question;
3. p.32 — test whether `struggle for survival` or equivalent is an actual Lovejoy heading/reclassification;
4. p.35 — exact examples/order;
5. p.31 — wording and any local reclassification;
6. p.34 — exact spellings/abbreviations.

Terminal routing:

- `research_notes/MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md`;
- `research_notes/QUELLENFORSCHUNG_round22_005_pp031-036_Marillier_clause_ownership_2026-09-03.md`.

### Round 23 — 005 pp.47–60 sacrifice clause ownership

State-bearing result:

- p.49 source-ranking norm remains Lovejoy-local: Tylor is praised as `the only one wh. does not construct theories beyond his evidence` and should be kept at hand;
- p.50 first three sacrifice class families are substantially Robertson-Smith-owned; the local delta is the fourth `magiques` class and the exact rebracketing/subdivision unless a closer carrier appears;
- p.51 god-man vitality transfer is Frazer-owned; blood/common-meal/communion mechanisms belong to the Robertson-Smith field;
- p.52 expiation/scapegoat/purification is inherited field material;
- p.53 `purely mechanical` cannot carry an originality claim: Frazer supplies impersonal/direct magic grammar and Marillier supplies sacrifice-as-magical-force; the possible Lovejoy delta is their local recombination on one sacrificial mechanism;
- p.55 Manyéma facts are Cameron-owned, while `not ritual but alimentary` remains a strong Lovejoy-local case reclassification;
- p.55 gender/taste direction is a **DIPLOMATIC HOLD** because the recovered Cameron source and current editorial summary point in different directions;
- pp.56–60 anti-Robertson-Smith single-union criticism is field-inherited; the local notebook operation is the use of a multi-mechanism dossier to restrict the theory's scope.

Terminal routing:

`research_notes/QUELLENFORSCHUNG_round23_005_pp047-060_sacrifice_clause_ownership_2026-09-03.md`

### Round 24 — 005 pp.61–75 mechanism / jurisdiction / reinterpretation

State-bearing result:

- p.64 extends the p.53 source field: Frazer owns the impersonal/mechanical magic grammar; Marillier owns magical sacrifice; Lovejoy locally separates personal-god coercion from direct action on natural forces;
- p.65 mixed motives/survivance are inherited problems, while the W3 `delicate analysis` sequence remains a local analytical dissociation of presently fused elements;
- **p.66 is the strongest surviving local relation in this block:** `expiatory sacrifice -> whole community` versus `magical sacrifice -> priests possessing magical skill in charms`; constituent facts are common field material, but no closer source has been recovered for the exact horizontal mechanism→social-jurisdiction/competent-performer mapping;
- p.69 animal→human substitution is **Robertson-Smith-owned at developmental-arrow level**; the notebook's local value is using that counter-arrow to reject victim species as a universal progress index;
- pp.70–72 should be read as case-level negative controls/reclassifications, not invention of ritual mechanisms;
- p.73 object-soul/destruction-as-release is Tylor-owned and the broader survivance/reinterpretation problem is already present in Marillier; the local A2 seam is the explicit reassignment of one continuing funerary form from protection-against-return to `another meaning`.

Strongest current 005 formulation:

> **Notebook 005 does not document Lovejoy inventing mechanism-specific comparative religion. It documents him working inside a field already populated by competing functional explanations and repeatedly reallocating those explanations across cases, sources, social bearers, and historical meanings.**

Strongest current 005→1906 ceiling:

> **The Paris notebook does not supply the component theory of impersonal efficacy from nothing. It shows Lovejoy repeatedly reallocating available causal and ritual categories across ethnographic cases; the 1906 article later reaggregates one family of those relations at a broader comparative scale.**

Direct-image priority for pp.47–75 when the 41–80 split image is accessible:

1. p.55 — resolve male/female gastronomic-direction conflict and source cue;
2. p.66 — exact jurisdiction grammar;
3. p.65 — exact `delicate analysis` / syncretism wording;
4. p.73 — exact `another meaning` connective;
5. p.50 — source heading/cue on the four-class slip;
6. pp.53/64 — transition clauses joining magical compulsion, machine analogy, direct natural action;
7. p.69 — exact auxiliary/source cue in animal→human substitution;
8. pp.70–72 — immediate ethnographic carriers.

Terminal routing:

`research_notes/QUELLENFORSCHUNG_round24_005_pp061-075_mechanism_jurisdiction_reinterpretation_2026-09-03.md`

Current archive action: **finish 005 diplomatically page by page when split images are available; while they are not, continue clause-level source ownership into the next 005 batch without promoting source collation or editorial summaries into manuscript wording.** The next source-critical batch is pp.76–90.

## 3. AOS 1897 and the 1898 publication path — direct-primary closure

Authoritative dossier:

`research_notes/AOS_1897_Lovejoy_election_read_by_title_and_technical_terms_precursor_2026-09-01.md`

Closed:

- Lovejoy is absent from the complete 40-person attendance list for the Baltimore meeting, 22–24 April 1897;
- paper No.30 was read by title in his absence;
- the 10 April circular announces `Critical summary of the argument of the Milinda-pañha`;
- final proceedings describe No.30 as `On the meaning of the Buddhist technical terms ...`;
- Lovejoy was elected an AOS corporate member at that meeting, on recommendation of the Directors collectively;
- Historical Study of Religions Section was instituted at the same meeting;
- 1898 membership structure does not list Lovejoy among the Section's members.

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
- concordance closes page accounting, not diplomatic transcription or manuscript identity with the 1897 communication.

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

1. Archive image queue: if `MS38_004_001_061_005_1-40.pdf` becomes directly accessible, execute Round-22 queue p.33 -> p.36 -> p.32 -> p.35 -> p.31 -> p.34; do not import Marillier print into the hand.
2. If `MS38_004_001_061_005_41-80.pdf` becomes accessible, execute Round-23/24 queue p.55 -> p.66 -> p.65 -> p.73 -> p.50 -> pp.53/64 -> p.69 -> pp.70–72.
3. If split images remain unavailable, continue source-critical ownership with 005 pp.76–90, then pp.91–105, while leaving canonical wording untouched.
4. After a canonical transcription batch actually changes, regenerate the integrated reading surface and run `python tools/audit_repository.py`.
5. AOS: obtain a true page image of JAOS 18 (1897), p.389 and diplomatically transcribe the full No.30 title; then search correspondence/submission records for the version relation.
6. Publication genetics, if intentionally resumed: phrase-level collate T3 notebook loci against a page-image/OCR-controlled JAOS witness.
7. Blog: when user/editor inputs are ready, regenerate v3.4 DOCX and rerun render QA.
8. Wider method control: direct-read a post-Mew Skinner text only if that comparative branch is intentionally resumed.
9. JHU reproduction: **wait for formal Digitization quotes** for Box 62 item 2 and Box 38 folders 9–11; do not send a duplicate request.

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
5. Same December letter documents Maurice Vernes on Psalms for the `Wisdom work`, Jean Réville on the Fourth Gospel, Faculty of Theology library use for Wisdom commentaries, and a Sabatier Acts course tried and abandoned as too far outside that year's work / too technically presuppositional.
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

> **Current = 191/191 page coverage, not diplomatic completion. 004 high-value source ownership is clause-level closed for the present argument, with only three narrow carrier HOLDs. 005 diplomatic transcription is active. Rounds 22–24 now recut the first major 005 source blocks: pp.31–36 are heavily Marillier-owned; pp.47–60 are largely assembled from Robertson Smith, Frazer, Marillier and Cameron with narrower Lovejoy reclassification/recombination seams; pp.61–75 retain p.66 mechanism→social-jurisdiction/competent-performer mapping as the strongest local relation, while p.69's animal→human arrow is Robertson-Smith-owned and p.73's object-soul/reinterpretation constituents are Tylor/Marillier-owned. If split images are unavailable, continue source ownership into pp.76–90 without upgrading editorial summaries. AOS 1897 and the full 1898 page concordance remain closed at their stated ceilings. MS-0873 France 1898–99 is direct-read at archival-transcription level, autograph verification remains open. JHU reproduction quotes are pending. Blog v3.4 is production-held, not research-blocked.**