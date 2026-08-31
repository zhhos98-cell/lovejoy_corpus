# Quellenforschung Round 15 — Grafton-grade critical re-audit of MS38 004 / 005

Date: 2026-08-31  
Status: **SUPERSEDING CALIBRATION LAYER / DO NOT DELETE ROUND 12–14 SNAPSHOTS**  
Scope: line-by-line re-audit of the strongest 004/005 source claims under stricter philological standards.

## Executive verdict

The principal historical architecture survives, but several labels used in Rounds 13–14 were too confident.

The main problem is not that the external source identifications were generally wrong. The main problem is **evidentiary category slippage**:

1. distinctive verbal concordance was sometimes promoted from `textual lineage` to `immediate physical carrier`;
2. source-supported editorial reconstructions inside some `*_clean.json` files were sometimes treated as though they were diplomatic manuscript wording;
3. failure to find an analogue was sometimes used too positively to assign an operation to Lovejoy;
4. a named author in a bibliography was occasionally allowed to stand for a whole local causal package;
5. seminar/date alignment was sometimes narrated one step too close to a reconstructed session transcript;
6. nineteenth-century publication metadata, edition history and reprint routes need to be kept distinct from the text actually in Lovejoy's hand.

The new governing rule is:

> **Similarity is a locator, not a transmission proof. A source relation must be graded separately at the witness, external-text, transmission, and authorial-operation levels.**

The strongest relations remain very strong: Garbe p.150, Warren p.150, Rhys Davids 1896 pp.24–36, Hardy p.394, explicit Trumbull pp.118/129, dated Marillier seminar anchors, and the directly re-inspected p.42 viññāṇa page. Other relations are downgraded from `closed` to `strong hypothesis` pending the manuscript originals.

---

# I. New four-axis evidence protocol

Do not use one undifferentiated A/B/C grade.

## W — manuscript witness status

- **W3 — direct image / diplomatic wording secure.** Key words, punctuation or source citation visibly controlled from the manuscript image.
- **W2 — partially diplomatic.** Key lexical items are visible but syntax/connecting prose contains uncertainty.
- **W1 — editorial argumentative reconstruction.** `corrected_text` preserves source-supported argumentative structure because handwriting is difficult; it is not quotable as Lovejoy's exact wording.
- **W0 — no manuscript witness.** External reconstruction only.

## S — external source-text match

- **S3 — explicit bibliographic anchor + distinctive text match.** Author/title/page or equivalent is visible and the external page fits.
- **S2 — distinctive phrase/sequence concordance.** Unlikely to be generic, but no direct manuscript bibliographic anchor.
- **S1 — proposition/case-cluster concordance.** The same argument or case family exists; independent convergence remains plausible.
- **S0 — controversy-field availability only.** Relevant proposition exists in the surrounding literature.

## T — transmission / uptake status

- **T3 — direct uptake demonstrated.** Explicit author/title/page, or a sufficiently long and distinctive extraction plus local bibliographic control.
- **T2 — strong immediate-carrier/source-family hypothesis.** Textual lineage is clear, but an intermediary anthology/requotation or another edition has not been excluded.
- **T1 — field / controversy route only.** Proposition was available in the documented environment; direct Lovejoy reading unproved.
- **T0 — no transmission claim.** Comparison only.

## A — Lovejoy authorial-operation status

- **A3 — direct manuscript operation + publication transformation.** Manuscript wording/diagram is image-secure and later print changes its function or form.
- **A2 — direct manuscript reweighting/recomposition.** Lovejoy's own connective or classificatory act is visible, but no publication transformation is required.
- **A1 — probable operation inferred from editorial reconstruction.** Plausible, but exact authorial wording awaits image control.
- **A0 — source-owned / cannot presently be assigned to Lovejoy.**

No single relation should be called `closed` without stating all four axes.

---

# II. Structural correction: the transcription layer is heterogeneous

This is the most important Round-15 correction.

Several 005 `*_clean.json` batches explicitly state the policy:

> `Where handwriting is too poor for diplomatic transcription, retain only source-supported argumentative structure rather than hallucinating lexical detail.`

This policy was responsible and useful for corpus navigation. It also means that the field named `corrected_text` is **not uniformly a diplomatic transcription**.

The problem is especially acute in:

- `MS38_004_001_061_005_p076-090_clean.json`;
- `MS38_004_001_061_005_p091-105_clean.json`;
- `MS38_004_001_061_005_p106-120_clean.json`.

Many entries are fluent editorial summaries: `Lovejoy stresses...`, `Lovejoy concludes...`, `Lovejoy asks...`. These sentences cannot be cited as Lovejoy's words and cannot by themselves prove that a source supplied the summarized wording.

A related, though less severe, problem occurs in `MS38_004_001_061_004_p037-054_clean.json`: several pages are argumentative summaries rather than diplomatic transcription. Fortunately, some crucial pages, especially 004 p.42, were independently rechecked against high-resolution page images in `MS38_004_005_material_form_closure_2026-08-27.md`.

### Anti-circularity rule

From now on:

`SOURCE-SUPPORTED EDITORIAL SUMMARY`
**cannot be used as independent evidence**
for
`SOURCE IDENTIFICATION`.

Only independently visible manuscript strings, bibliographic marks, diagrams, dates, or quotations may support the high transmission grades.

### Required next-round repair

When the originals are uploaded, build for every high-value page three separate fields:

1. `diplomatic_visible_text`;
2. `editorial_expansion_or_argument_summary`;
3. `external_source_collation`.

Never merge these again.

---

# III. 004 — source-by-source recalibration

## 004-01 Garbe 1894 pp.150–151 — **keep strong, modify the wording of the claim**

### Previous formulation

`GARBE → LOVEJOY WORKING TRANSLATION`.

### Philological objection

The notebook visibly says `Garbe p.150`, and the English notes closely follow the German 1894 text. That establishes Garbe as a direct source node. It does **not**, strictly speaking, prove that Lovejoy himself translated every English sentence. A lost English excerpt, lecture paraphrase or another intermediary remains logically possible until excluded.

Garbe's *Die Sâmkhya-Philosophie* (Leipzig: Haessel, 1894) is demonstrably German; no pre-1898 English edition of that monograph has been identified in this audit.

### New code

**W3 / S3 / T3- / A0–A1**

Safe wording:

> `Lovejoy's notebook explicitly cites Garbe p.150 and preserves a close English working rendering of Garbe's discussion.`

Avoid:

> `Lovejoy translated Garbe` unless the linguistic transformation itself is demonstrated.

### Substantive consequence

Round 13 was right to remove from Lovejoy the ownership of the distinction between foreign historical element and local systematic relevance. The methodological environment is source-owned.

---

## 004-02 Sabbāsava — **translation lineage strong; physical carrier not closed**

Rhys Davids, *Buddhist Suttas*, SBE XI (1881), pp.298–300 gives the ordered sequence:

- things that ought not to be considered;
- past/future/present self-interrogation;
- six notions;
- permanent/lasting/eternal self;
- jungle/wilderness of delusion.

The 004 early transcription is sufficiently close and relatively diplomatic.

But `heresy` in Lovejoy's notes versus Rhys Davids's `delusion` deserves attention. Warren's active Buddhist vocabulary uses `heresy`, `heretical jungle`, etc.; Lovejoy may be normalizing terminology from another source already in use. Another pre-1898 reprint of Rhys Davids could also intervene.

### New code

**W2–W3 / S2+ / T2+ / A0 for the quotation; A2 provisional for the surrounding calibration.**

Supersedes Round 14's phrase `translation family closed` only in the sense that `closed` should be reserved for bibliographically demonstrated uptake.

Safe wording:

> `The extract belongs very closely to the Rhys-Davids SBE XI translation lineage; Rhys Davids is the leading immediate-carrier candidate.`

Not yet:

> `Lovejoy had SBE XI open.`

---

## 004-03 Siṃsapā leaves — **major downgrade of the word “immediate”**

Oldenberg/Hoey 1882 pp.204–205 contains the highly distinctive English sequence:

`brings you no profit`
→ `turning from the earthly`
→ `subjection of all desire`
→ `cessation of the transitory`
→ `peace / knowledge / illumination / Nirvana`.

This is an excellent textual-lineage match.

But the notebook source line is currently `[Source illegible], p. 20f.`. The conjecture that this conceals `Oldenberg, p.204 f.` is a **conjectural emendation**, not a paleographic reading.

### New code

**W2 / S2++ / T2+ / A0 for source wording.**

Round 14's status `SIṂSAPĀ IMMEDIATE CARRIER CLOSED TO OLDENBERG 1882` is too strong and is hereby superseded.

Safe wording:

> `Lovejoy's English wording descends from, or is extraordinarily close to, the Hoey translation of Oldenberg pp.204–205. The manuscript's illegible source line should be tested against “Oldenberg, 204 f.” when the image is supplied.`

Do not call `204` a recovered manuscript page number before image confirmation.

---

## 004-04 Sutta-Nipāta / Fausbøll — **retain only at source-family level until re-collated**

Round 13 says the Atthaka-vagga lines are close to Fausbøll/SBE. This audit did not re-establish the exact clause-level collation from the primary edition.

### New code

**W2 / S1–S2 / T2 provisional / A0.**

Do not let the strong Sabbāsava and Siṃsapā identifications raise this neighboring source by association.

---

## 004-05 Warren p.150 / Visuddhimagga — **keep as direct uptake**

The notebook explicitly writes `V. Warren p.150 f. Vis Mag.` and reproduces the chariot-wheel / one-thought-duration sequence.

### New code

**W3 / S3 / T3 / A0 for quotation; A2 for the subsequent continuity/time objection if the connecting prose is image-secure.**

This remains one of the clean benchmark source edges against which weaker identifications should be measured.

---

## 004-06 Mahāparinibbāna authenticity ranking — **Lovejoy ownership downgraded pending historiographical source control**

Round 13 treated:

- `last sayings likely preserved with unusual fidelity`;
- death narrative has `extreme plausibility & verisimilitude`;
- therefore impermanence historically central

as Lovejoy inferential steps.

The early 004 transcription does appear close to diplomatic and preserves those first-person judgments. However, historical criticism of the Buddha biography was a major late-nineteenth-century field problem. Oldenberg explicitly presented himself as sifting legend from reliable historical residue; Rhys Davids likewise reconstructed a historical Buddha from Pāli narrative.

Therefore an actorial judgment visible in Lovejoy is not automatically an independently originated judgment.

### New code

**W3 / S0–S1 for possible upstream historiographical precedents / T0–T1 / A2? provisional.**

Safe wording:

> `Lovejoy explicitly performs an authenticity ranking here. Whether the criterion itself is his own or borrowed from contemporary historical-Buddhist criticism remains open.`

This is a genuine Lovejoy act on the page, but not yet a Lovejoy-origin method.

---

## 004-07 Rhys Davids 1896 pp.24–36 — **upgrade textual dependence; distinguish physical copy**

This is stronger than Round 13's ordinary `digest` language suggests.

Rhys Davids, *Buddhism: Its History and Literature* (1896), pp.24ff., contains the same long ordered sequence preserved in 004:

- Sāṃkhya as possible stepping-stone;
- Kapila before Buddha;
- Garbe's position;
- `The point seems to me, I confess, to be most doubtful`;
- late Sāṃkhya texts and the chronological gap;
- evidence for earlier thinkers but not mature system;
- sixty-two theories / school-identity qualification.

The length, order, rare first-person phrasing and matching p.24 locus make chance convergence extremely implausible.

### New code

**W2–W3 / S3- / T3- textual uptake, T2+ physical-copy status / A0 for the imported chronology language.**

Safe wording:

> `The immediate textual archetype of this multi-page notebook run is Rhys Davids 1896 pp.24–36 with near certainty. Whether Lovejoy copied the Putnam volume itself or a faithful intermediary remains a narrower bibliographical question.`

This distinction matters because `direct textual dependence` can be stronger than `physical-book possession`.

---

## 004-08 p.17 `To R.D.'s remark it should be added` — **one of the cleanest Lovejoy hinges; keep**

The syntax itself marks source boundary and authorial supplementation.

### New code

**W3 if image confirms the phrase / S3 for R.D. context / T3 / A2.**

This is exactly the kind of evidence a philologist prefers: the actor marks the seam himself.

Remaining caution: `Lovejoy's diagnostic specificity` should mean **this local supplementation**, not priority for the general scholarly operator of diagnostic specificity.

---

## 004-09 p.18 practical agnosticism — **keep the Round-13 downgrade, perhaps downgrade further**

Round 13 correctly backed away from calling the entire paragraph an independent Lovejoy synthesis. Warren already links false presupposition / `question out of court` with Buddhism's practical aim.

### New code

**W2–W3 / S1–S2 / T2–T3 depending exact citation / A2 only for demonstrable reweighting language.**

Until the original page is rechecked word by word, use:

> `Lovejoy appears to reweight an already available Warren/Rhys-Davids problem field.`

not

> `Lovejoy reframes...` as though all connective logic were securely his.

---

## 004-10 p.20 `present effort` programme — **keep, with witness-specific wording**

The p.19–36 transcription is comparatively diplomatic and contains explicit first-person/programmatic prose: `The most that can be hoped for in the present effort...`.

### New code

**W3- / S0 / T0 / A2.**

This remains a legitimate notebook-programme statement, though it should not be elevated into a generalized lifelong methodology.

---

## 004-11 Warren on taṇhā/upādāna identity — **Round-12 correction is secure**

Warren does use `tenacity of desire`, but he also preserves the alternative:

`desire = quest before object obtained`
vs
`attachment = seizing object once within reach`.

Lovejoy's notebook explicitly says Warren regards the relation as `identity` and then objects.

### New code

**W3 / S3 / T3 / A2.**

Safe interpretation:

> `Lovejoy sharpens Warren into a stronger identity claim in order to test it against the four attachments and six desires.`

Do not say Warren himself taught simple identity.

---

## 004-12 Childers + Müller at viññāṇa — **keep source-router correction; avoid independent-two-source story**

Müller's Dhammapada note itself reports Childers's earlier and later positions and rejects the strong primacy reading. This validates Round 13's correction that Müller is a controversy router as well as a counter-reading.

### New code

**W3-ish for p.29 references / S3 / T3 for Childers and Müller if both are visibly named / A2 for Lovejoy leaving the claim open.**

Do not narrate the page as if Lovejoy independently discovered two isolated authorities whose conflict he created.

---

## 004-13 p.42 viññāṇa: temporal antecedence / logical subdivision — **page fact secure; originality claim downgraded**

This needs a sharp distinction.

### What is secure

The high-resolution material audit directly rechecked PDF p.42/MS123. The page visually nests viññāṇa inside nāma/nāmarūpa and the prose below states a different temporal relation. There is no need to rely on the summary-style `clean.json` for this physical claim.

Therefore:

**W3 / A2 for holding distinct relation types on one page.**

### What is not secure

Round 13 says no identified source states the exact temporal/logical pair and therefore codes it as Lovejoy recomposition. This is too positive an inference from a negative search.

Warren's 1893 causation article already uses relation-specific language such as `necessary antecedent`, `cause and effect`, `material cause`; Oldenberg 1882 treats consciousness and nāmarūpa as both sequential and reciprocally dependent in different passages. The field therefore already contained pressure to distinguish kinds of relation even if the exact formula `temporally antecedent / logically subdivision` has not been found.

### New code

**W3 / S0–S1 field parallels / T0–T1 / A2 local recomposition; originality status = UNMATCHED-TO-DATE, NOT PROVED UNIQUE.**

Safe wording:

> `The exact pair has not yet been matched in the sources checked. The page securely shows Lovejoy himself formulating the two relations together; priority or uniqueness is not claimed.`

This is a stronger philological sentence than `Lovejoy invented the pair`.

---

## 004-14 Hardy p.394 fact/manner — **keep as a benchmark source-transformation chain, but distinguish source wording from notebook grammar**

Jacobi 1898 independently quotes Hardy p.394:

`by upādāna a new existence is produced, but the manner ... controlled by karma ... sometimes upādāna efficient cause, at others karma`.

This directly confirms the external source locus. Notebook p.33 explicitly cites Hardy p.394 under `Upādāna, Relation to Karma`; the `fact` versus `manner` opposition is reported as visually secure at conceptual level, though exact grammar is less secure.

### New code

**W3 for Hardy citation; W2–W3 for exact fact/manner syntax / S3 / T3 / A2 notebook sharpening; A3 for notebook→1898 publication stabilization.**

This remains one of the repo's strongest microgenesis chains.

Important title control: use R. Spence Hardy, *A Manual of Budhism, in its Modern Development* (1853), not *Eastern Monachism*.

---

## 004-15 Senart compositeness / upādāna = upādānakkhandha — **keep as controversy object; sentence-level ownership still needs primary recheck**

Round 13 made the right conceptual correction: Senart is analytically sophisticated, and compositeness/stratification cannot be attributed to Lovejoy.

But this audit has not fully re-collated every Senart/Oldenberg sentence used in the Round-13 synthesis.

### New code

**W2 / S1–S2 / T2–T3 where Senart page is explicit / A2 provisional for burden-of-proof redistribution.**

Keep:

`Lovejoy grants historical compositeness but tests whether alleged duplicates have the same semantic/causal function.`

Avoid until primary recollation:

`Oldenberg 1897 already supplies exactly composite inheritance ≠ incoherence` as a sentence-level claim.

---

# IV. 005 — source-by-source recalibration

## 005-01 The Marillier framework is more upstream than our prose sometimes admitted

This is a major substantive correction.

Marillier's *La survivance de l'âme et l'idée de justice chez les peuples non civilisés* directly frames the problem of whether future life originates in moral compensation. The 1898–99 EPHE report says explicitly that the Monday conference aimed to establish that **no moral element intervenes at the origin** and that the other life is a **continuation, not compensation/reparation/punishment**, with new evidence especially from the Americas. The Tuesday conference treats human sacrifice and ritual anthropophagy by distinct types: expiatory, funerary, anthropophagic, magical, with agrarian/fecundative sacrifice.

Lovejoy is explicitly listed among auditors taking an active part.

### Correction

Earlier formulations such as `MARILLIER PROBLEM FIELD → LOVEJOY COMPACT MORAL-SELECTOR TEST` still leave too much ownership with Lovejoy if read incautiously.

The general selector criterion, the non-moral-origin thesis, the heterogeneous sacrifice-type field, and the insistence on causal differentiation are substantially **upstream / seminar-owned**.

### New code

**Marillier framework: S3 institutional primary / T3 environment and seminar participation / A0 for general criterion.**

Lovejoy's stronger candidate delta is narrower:

- local witness reallocation;
- exact boundary work in selected cases;
- conversion into personal schemas;
- re-use of external evidence for different classificatory jobs.

Do not claim Lovejoy owns the moral/non-moral selector as such.

---

## 005-02 Bibliographic date of Marillier's `Survivance` — **normalize metadata carefully**

Persée metadata records the report under `Année 1893`, pp.1–46, for the exercise 1893–94; EPHE/prosopographic catalogues also record a standalone Imprimerie nationale issue in 1894.

Therefore the repo should not treat `1893` and `1894` as two distinct works.

Publication-grade citation must specify which bibliographic object is meant:

- serial/report metadata: 1893, annual/report context;
- standalone imprint: Paris, Imprimerie nationale, 1894.

This is a classic edition/imprint issue and should be fixed before final citation.

---

## 005-03 `M. Surviv.` / `V. Surviv.` early references — **probable, not self-evidently Marillier until image recheck**

P.29 explicitly reads `Marillier — Survivance — 12 June`; this makes expansion of earlier abbreviated `M. Surviv.` highly plausible.

But abbreviation expansion by analogy is still an editorial act.

### New code

**W2 / S2 contextual / T2+ / A0.**

Safe wording:

> `The early abbreviations are very likely references to Marillier's survivance work, especially in light of the explicit June-12 slip.`

Not:

> `The early pages definitively cite Marillier.`

until the originals are checked.

---

## 005-04 May 29 / June 6 / June 12 session alignment — **keep strong, but never equate alignment with transcript status**

The weekday alignment is exact:

- 29 May 1899 = Monday;
- 6 June 1899 = Tuesday;
- 12 June 1899 = Monday.

Marillier's 1898–99 programme independently specifies Monday survivance and Tuesday sacrifice/anthropophagy; Lovejoy is an active auditor.

### New code

**W3 dates/headings where image-secure / S3 institutional programme / T3 session-environment relation / A0 regarding lecture content not literally recorded.**

Safe:

> `session-linked stratum`.

Unsafe:

> `lecture transcript`, `Lovejoy copied Marillier on June 6`, or day-by-day intellectual chronology beyond the anchors.

Round 13 mostly respected this distinction; retain it rigorously.

---

## 005-05 Early Greenland / Rink as “adversarial witness” — **good hypothesis, actorial rhetoric slightly too strong**

The early 005 batch is closer to a diplomatic transcription than later batches and explicitly points to Rink by page. Rink's account contains reward/punishment-like ambiguity, while Lovejoy's page says `No moral notion is implied at all` and reallocates the determinant.

### New code

**W2–W3 / S3 / T3 / A2.**

`Adversarial witness` should remain **our analytical role label**, not actor-native terminology. Use quotation marks sparingly and explain the observable operation instead.

---

## 005-06 p.10 `American Legends, V. [Brinton?]` — **Round 14 source split basically sound; keep the name itself HOLD**

Yarrow's 1881 *A Further Contribution to the Study of the Mortuary Customs of the North American Indians* contains the moon/coyote story and explicitly routes it to Stephen Powers, *Tribes of California*, p.341. The notebook page also has a title-like reference close to `A Further Contribution...` and `moon & coyote`.

This strongly supports the Yarrow→Powers chain for that specific case.

However `American Legends, V. [Brinton?]` remains a paleographic uncertainty. `vide Brinton` is a good semantic conjecture, not a recovered reading.

### New code

Yarrow/Powers: **W2 / S2+ / T2+** pending image.  
Brinton line: **W1–W2 / S0–S1 / T1 / HOLD.**

Do not use the uncertain Brinton line to prove a continuous Brinton reading run.

---

## 005-07 Brinton as macro field map — **reduce causal weight because Marillier supplies the same macro problem institutionally**

Brinton remains a real multi-role source:

- explicit *The American Race* slip;
- explicit Brinton sacrifice bibliography entry;
- strong content concordances.

But the early eschatology macro-problem does not need Brinton as its primary router. Marillier's 1893/1898–99 work directly supplies the non-moral afterlife problem and American evidence field.

Therefore:

`BRINTON/MARILLIER-TYPE GENERAL PROBLEM`

should usually be replaced by a differentiated statement:

`MARILLIER = documented programme/problem frame`
+
`BRINTON = possible/secure source in specific American bibliographic functions`.

This prevents over-crediting Brinton because his printed formulation happens to match our analytic summary.

---

## 005-08 p.62 Brinton sacrifice item — **do not close by content matching**

The manuscript has `Brinton, article [title uncertain] — for good bibliography & fair sketch of subject` in the conservative transcription.

*Religions of Primitive Peoples* (1897), Lecture V is indeed the strongest content-level candidate because it compresses the same sacrifice/communion field. But a monograph lecture is not naturally an `article`, and no exact title has been paleographically recovered.

### New code

**W2 / S1–S2 / T2 candidate / exact item HOLD.**

Do not upgrade further until the original page is supplied.

This is exactly the sort of attractive identification a Grafton-style reader would refuse to print without the word on the page.

---

## 005-09 Grout p.79–80 — **external cluster secure; immediate-carrier and Lovejoy-delta claims downgraded because the current transcript is editorialized**

Grout 1889 genuinely contains the remarkable sequence:

particular cow → recovery test → prayer → cow bellows → removal of evil → gall → meat left for shades → communal eating.

That external identification is excellent.

But the current p.79–80 `corrected_text` is fluent editorial prose created under a policy that allows source-supported argumentative reconstruction. Therefore it cannot independently establish that Lovejoy wrote every feature in that same sequence or used the words `bargain`, `transactional`, `alimentary`, `expiatory`, `funerary`, `little evidence for mystical union` exactly as summarized.

### New code

External Grout cluster: **S2++**.  
Manuscript witness for named `Grout`: **W? pending original-image confirmation from the next round**.  
Transmission: **T2+**, rising to T3 only if `Grout` / quotation / page is directly visible.  
Lovejoy classificatory delta: **A1 pending image**, not A2 secure.

This supersedes Round 14's status `GROUT 1889 = IMMEDIATE NARRATIVE-PRAYER CARRIER` as too categorical.

Callaway remains a parallel Zulu documentary control, not necessarily the immediate carrier.

---

## 005-10 p.78 Trumbull — **content analogues found; `content locus closed` was too strong**

Trumbull p.299, via Herbert Spencer, discusses blood offered over the dead as creating a bond/union between living giver and ghost. Trumbull p.268f. contains grave-centered animal sacrifice morphology.

These are real and useful external analogues.

But p.78 `corrected_text` is itself an editorial argument summary. Consequently we cannot yet say that Lovejoy's manuscript literally formulated `establishing a relation between the dead and the sacrificer`, nor that one of these page numbers was the illegible manuscript numeral.

### New code

**W1 / S1–S2 / T1–T2 / A1.**

Round 14's phrase `CONTENT LOCUS SUBSTANTIALLY CLOSED` is superseded.

New status:

> `Trumbull pp.268f. and 299 are priority loci to test against the original p.78 image.`

This is a target list, not a closure.

---

## 005-11 Trumbull pp.118–129 — **retain as benchmark direct-reading run, but split anchors from inferred continuity**

Separate two levels.

### Explicit anchors

High-resolution reinspection previously recovered:

- `V. Trumbull Blood Cov't 118.`
- `(quot. Trumbull p.129)`.

These are direct uptake evidence.

**W3 / S3 / T3.**

### Intervening continuous-reading inference

The notebook's intervening examples follow Trumbull's source order from curative/life-bearing blood through prophylaxis and transferable qualities.

That makes continuous reading highly likely, but it remains an inference between the two anchors.

**T2++ for the continuous-run claim.**

Safe wording:

> `Two direct page anchors bracket an intervening sequence that strongly suggests continuous extraction through pp.118–129.`

This is better than treating every intervening clause as directly proven copied from Trumbull.

---

## 005-12 Kingsley exact-page sequence — **retain only if the exact manuscript page numbers are independently image-secure**

Round 13 calls `Travels p.511 → Lovejoy contrast → p.525` Grade A. The principle is good, but Round 15 requires the same witness firewall used for Trumbull.

If the Kingsley page references were recovered by direct visual audit, keep **W3/S3/T3**. If they exist only in the editorial `clean.json` summary, downgrade to W1/T2 until original reinspection.

The next image round should explicitly tick this box.

---

## 005-13 Jevons — **Round 14 negative control is correct; do not chase proposition fit into transmission**

Jevons 1896 is a real controversy target for a material-progress/totemism/domestication master sequence. Marillier's 1897–98 critique explicitly targets Jevons and Lovejoy later participates actively in Marillier's programme.

No current notebook reading securely gives Jevons title/page beside p.103.

### New code

**S0–S1 / T1 / direct-reading HOLD.**

Keep Round 14's negative-control conclusion.

---

## 005-14 p.103 agriculture/domestication diagram — **material fact secure; exact intellectual target not**

The direct image audit independently confirms a branching diagram and a chronological objection on p.103. Therefore the local operation exists on the manuscript regardless of the summary transcript.

### New code

**W3 / A2.**

But `Jevons` as the intended target is only **S0/T1** unless named. The proposition may have arrived through Marillier or the wider controversy.

Safe wording:

> `Lovejoy visibly stress-tests a developmental chronology. Jevons supplies a close controversy-field analogue, not a demonstrated immediate source.`

---

## 005-15 p.117 common/common/exceptional sacrifice distribution — **downgrade exact wording until image control**

This conclusion is important to the 005 argument, but the current p.117 `corrected_text` is editorialized under the `source-supported argumentative structure` policy.

Until the original p.117 page is re-read:

### New code

**W1–W2 / A1.**

Use internally:

> `The first-pass page reading indicates a late synthesis in which alimentary and expiatory/propitiatory forms are treated as common and sacramental union as exceptional.`

Do not quote `common/common/exceptional` as Lovejoy's literal formulation yet.

This becomes one of the highest-priority pages for the next original-image upload.

---

## 005-16 revisions at pp.16–20 and schemas pp.24–27 — **retain, because they have independent image control**

The material-form audit directly re-inspected these pages and confirms:

- revision activity around moral/non-moral boundaries;
- `not as a moral fault` emphasis;
- missionary-contamination warning;
- numbered/Roman-numeral classificatory schemas;
- May 29 date.

### New code

**W3 / A2 for visible boundary work.**

Still retain the crucial negative rule:

> strike-through ≠ direction of conceptual conversion unless deleted wording is legible.

---

# V. Recalibrated hierarchy of the strongest relations

## Tier 1 — can survive a hostile philological referee now

1. **004 Garbe p.150** — explicit source + exact external page relation; only `Lovejoy himself translated it` is withheld.
2. **004 Warren p.150** — explicit title/page + matching passage.
3. **004 Rhys Davids 1896 pp.24–36** — long, ordered, rare verbal correspondence; immediate textual archetype essentially secure.
4. **004 p.17 `To R.D.'s remark it should be added`** — actor marks source seam and supplementation.
5. **004 Warren taṇhā/upādāna** — explicit source and demonstrable Lovejoy sharpening.
6. **004 Hardy p.394** — explicit source, external wording controlled, notebook→publication transformation.
7. **004 p.42 material relation split** — direct page-image control; local operation secure, uniqueness withheld.
8. **005 Marillier 1898–99 institutional link** — programme, weekdays/topics, Lovejoy active participation secure.
9. **005 May29 / June6 / June12 session-date alignment** — direct dates + independent seminar timetable; transcript inference withheld.
10. **005 Trumbull pp.118 and 129 explicit anchors** — direct page citations visually recovered.
11. **005 pp.16–20 / pp.24–27 material boundary work** — independent high-resolution image audit.

## Tier 2 — strong, but next original-image round should decide the last step

1. Sabbāsava → Rhys Davids SBE XI physical carrier.
2. Siṃsapā → Oldenberg/Hoey physical carrier and conjectured `204 f.` manuscript reading.
3. 005 Yarrow/Powers moon–coyote chain.
4. early `M. Surviv.` expansion to Marillier.
5. p.62 exact Brinton sacrifice item.
6. p.79–80 Grout immediate-carrier status and exact Lovejoy classification.
7. p.78 Trumbull numeral / locus.
8. Kingsley sequential page run if not already separately image-logged.
9. p.117 exact distributional wording.

## Tier 3 — controversy-field controls, not source edges

1. Jevons direct reading.
2. Hubert–Mauss direct reading.
3. exact Oldenberg/Senart sentence-level ancestry where no Lovejoy bibliographic anchor is present.
4. any claim that Marillier `caused` the 1906 energetics category.
5. any claim that p.42 relation language is unique to Lovejoy because no analogue has yet been found.

---

# VI. Language that should be retired or restricted

Retire unless the four-axis grade warrants it:

- `closed`;
- `direct-lock`;
- `immediate carrier`;
- `Lovejoy invention`;
- `Lovejoy discovered`;
- `source X taught Lovejoy method Y`;
- `the notebook proves he read X` from proposition fit alone;
- `reading path` where only physical page order exists;
- `chronology` where only accretion/order exists.

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

---

# VII. What the argument still looks like after the downgrades

The downgrades do **not** destroy the project. They actually sharpen it.

The strongest historical claim is no longer:

> Lovejoy independently invented a sophisticated classificatory method while reading Buddhism and comparative religion.

It is:

> **Lovejoy worked inside already sophisticated philological and comparative-religion source environments — Garbe, Rhys Davids, Warren, Hardy, Oldenberg, Marillier and others — and the surviving notebooks let us observe, at selected image-secure seams, how he redistributed evidentiary jobs: quotation versus inference, temporal order versus classificatory inclusion, fact versus manner, visible ritual form versus causal mechanism, and field synthesis versus lower-witness test.**

That claim is harder to knock down because it depends less on originality and more on demonstrable transformations at explicit seams.

A second surviving claim is material:

> **the notebooks preserve operations that publication often hides: explicit source seams, diagrams holding incompatible relation types, numbered schemas, revision at category boundaries, source slips, and exact-page extraction runs.**

Again, this is not a genealogy of later `unit-ideas`; it is evidence of research practice.

---

# VIII. Highest-priority checklist for the next original-image upload

Do these before any new conceptual expansion.

## 004

1. p.6/MS21 — source heading before Sabbāsava: test for `R.D.`, `SBE`, page number, or another carrier.
2. p.8/MS25 — source heading before Siṃsapā: test specifically for `Old.`, `Oldenberg`, `204`, `20?`, `f.`.
3. p.12/MS53 — source line before Rhys Davids p.24 sequence: recover the author/title abbreviation exactly.
4. p.17 — photograph the exact `To R.D.'s remark it should be added` seam.
5. p.20 — diplomatic line-by-line transcription of the `present effort` paragraph.
6. p.22 — exact Warren `identity` wording and punctuation.
7. p.29 — exact Childers/Müller source seams.
8. p.33 — exact `fact / manner` wording around Hardy p.394.
9. p.42/MS123 — fresh diplomatic transcription of every line below the diagram, despite prior image control.
10. pp.47–52 — exact Senart references and speaker/source boundaries.

## 005

1. pp.3–6 — exact `M. Surviv.` / `V. Surviv.` expansions and punctuation.
2. p.10/MS17 — `American Legends, V. [Brinton?]` at maximum resolution.
3. p.11 — exact Rink language versus Lovejoy's `No moral notion` sentence.
4. p.27 — `May 29` page, with local brackets/revisions.
5. p.29 — `Marillier — Survivance — 12 June` full slip.
6. p.47 — `Sac. June 6.` plus first lines below heading.
7. p.62/MS125 — exact Brinton item after author name: this is a priority bibliographic crux.
8. p.78/MS157 — exact Trumbull numeral and surrounding words; test 268/299 only as hypotheses.
9. pp.79–80/MS159–161 — **retranscribe diplomatically from scratch without looking at Grout first**; only then collate Grout/Callaway. This is essential to eliminate circularity.
10. pp.85–86 — preserve image crops showing `118` and `129` anchors.
11. p.89 — exact Kingsley source/page wording.
12. p.103 — diagram + authorities cited in the chronology objection.
13. p.117 — **diplomatic transcription from scratch** of the alleged common/common/exceptional synthesis.
14. p.119 — exact selected-body-part language if it is to carry the 005→1906 transfer argument.

### Blinding protocol for difficult pages

For p.79–80, p.78 and p.117, the next transcription should be done in this order:

1. image only, no external source open;
2. diplomatic reading with uncertain graphemes marked;
3. freeze the transcription;
4. then open Grout/Trumbull/Brinton/etc.;
5. record exact matches and non-matches separately.

This prevents source expectation from feeding back into paleography.

---

# IX. Files explicitly superseded in status language, not deleted

The following remain useful research history but their strongest status labels should not govern future prose:

- `004_round14_Sabbasava_Simsapa_immediate_carrier_closure_2026-08-31.md` — superseded on `immediate carrier closed`; use `translation lineage / leading carrier candidate`.
- `005_round14_Grout_1889_p079-080_immediate_source_closure_2026-08-31.md` — superseded on immediate-carrier certainty and Lovejoy-local classificatory wording until diplomatic p.79–80 recheck.
- `005_round14_Trumbull_p078_content_locus_p268_299_2026-08-31.md` — p.268f/p.299 remain priority comparison loci, but `content locus closed` is superseded.
- `005_Quellenforschung_and_reading_path_reconstruction_round13_2026-08-31.md` — keep its architecture, but treat all claims deriving solely from summary-style 005 `clean.json` batches as W1 until image-rechecked.

No old file should be rewritten retroactively. Round 15 is the provenance-preserving correction layer.

---

# X. Compact restart statement

> **After a hostile philological re-audit, the project should distinguish manuscript witness, external source match, transmission, and authorial operation. Several spectacular phrase matches remain genuine but no longer automatically prove the physical book in Lovejoy's hand. More importantly, some later 005 `clean.json` files are editorial argumentative reconstructions rather than diplomatic transcriptions, so source identifications derived from them must be rechecked blind against the original pages. The strongest source seams survive: Garbe p.150, Warren p.150, Rhys Davids 1896 pp.24–36, Hardy p.394, explicit Trumbull pp.118/129, the Marillier EPHE programme/date anchors, and 004 p.42's directly inspected relation split. Lovejoy's defensible historical delta is not ownership of the upstream methods or categories, but observable redistribution of evidentiary function at selected manuscript seams.**

## Primary public controls used in this re-audit

- T. W. Rhys Davids, *Buddhist Suttas*, SBE XI (1881), Sabbāsava: https://www.sacred-texts.com/bud/sbe11/sbe1109.htm
- T. W. Rhys Davids, *Buddhism: Its History and Literature* (1896), bibliographic object: https://www.deutsche-digitale-bibliothek.de/item/K5LCCB2D6BZXU44437JEH4S2HNUPB5HW
- Henry Clarke Warren, *Buddhism in Translations* (1896), digitized volume: https://digicoll.lib.berkeley.edu/record/206215
- Hermann Jacobi, `Über das Verhältnis der buddhistischen Philosophie zum Sāṃkhya-Yoga und die Bedeutung der Nidānas`, ZDMG 52 (1898), 1–15: https://fid4sa-repository.ub.uni-heidelberg.de/4716/
- Richard Garbe, *Die Sâmkhya-Philosophie* (1894): https://books.google.com/books?id=UtpZAAAAMAAJ
- Arthur O. Lovejoy, `The Buddhistic technical terms upādāna and upādisesa`, JAOS 19 (1898), 126–136: https://www.jstor.org/stable/592475
- Léon Marillier, `La survivance de l'âme et l'idée de justice chez les peuples non civilisés`: https://www.persee.fr/doc/ephe_0000-0002_1893_num_7_3_19382
- Marillier, EPHE 1898–99 report: https://www.persee.fr/doc/ephe_0000-0002_1898_num_12_8_19501
- Lewis Grout, `Religious Views and Practices of the Zulus`, *Missionary Review of the World* (Oct. 1889): https://cafis.org/files/MRW-1889-10.pdf
- H. C. Yarrow, *A Further Contribution to the Study of the Mortuary Customs of the North American Indians* (1881): https://repository.si.edu/handle/10088/91605
