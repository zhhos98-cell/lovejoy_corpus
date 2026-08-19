# Lovejoy as Orientalist / comparative religion — Batch 142

Date: 2026-08-19  
Status: synced  
Scope: full pass over the twelve newly available GPT-backend OCR JSON objects, treated as manual-retrieval/source-control returns rather than as a fresh transcription layer for notebooks 004/005. The pass checks each whole object, resolves the live GitHub retrieval questions where the evidence permits, and records negative controls where the uploaded witness is the wrong edition or does not contain the expected locus.

## Core result

This upload round closes several long-running source-control problems at once and materially strengthens the Marillier/005 argument.

On the 004 side, the exact Rhys Davids locus behind Lovejoy's quotation is now recovered at printed p.113; Dahlmann p.14 is now primary-controlled and proves a close comparison between Buddhist `anupādisesanibbāna` and orthodox `anupādhīśeṣanirvāṇa` while explicitly warning against simply transferring the orthodox substantial-self meaning into Buddhism; and the Müller check produces a citation correction rather than the expected confirmation: in the uploaded 1884 Trübner witness, printed p.30 contains ordinary consonantal phonology and no `upādi/upadhi` statement, whereas the relevant equation appears on printed p.36. Because Lovejoy's own 1898 article really prints `Pali Grammar, p. 30`, the safest present conclusion is a probable six-page citation slip, pending another-edition/pagination control.

On the 005 side, the complete `Revue de l'histoire des religions`, tome XXXVII (1898), resolves the whole 1898 continuation of Marillier's `La place du totémisme`, identifies the previously anonymous RHR reviews of Rhys Davids and Trumbull, and supplies a substantially closer contemporary control for the classificatory operations visible in notebook 005. Most importantly, Marillier himself reviewed H. Clay Trumbull's `The Threshold-Covenant` in this volume and explicitly attacked the reduction of heterogeneous religious facts to a single explanatory principle. This moves the argument from a later retrospective reconstruction of a `Marillier method` to a contemporaneous 1898 printed operator, while leaving the direct-reading/transmission question open.

No new GLA/GAL/COV identifier is created in this batch.

---

## 1. Upload audit and source identity

The following GPT-backend OCR JSONs were scanned as complete objects rather than by first-hit search. SHA-256 values are recorded so that later replacement OCRs or differently paginated witnesses can be distinguished.

| Uploaded JSON | SHA-256 | Source/status |
|---|---|---|
| `MS38_004_001_061_004.pdf_by_PaddleOCR-VL-1.6.json` | `e14956e2904f2c907d29163bbea3f3f162a011da2a53928dbf370efe7d031d84` | notebook 004, 71 pp.; already first-pass transcribed; baseline control only |
| `MS38_004_001_061_005.pdf_by_PaddleOCR-VL-1.6.json` | `e420b098a2cf2bdd272e918434fb452fae923a9fcfb730117825d9dd366ef9c2` | notebook 005, 120 pp.; already first-pass transcribed; baseline control only |
| `lovejoy_clean_text_corpus_20260817_211123.json` | `cc2bbc38d76a70d986f8176acfeef6a0abb214f309bfa3480bc0962111b1e351` | project clean-text corpus; Lovejoy 1898 article used as authorial citation control |
| `1898_Über das Verhältnis der buddhistischen Philosophie zu Smankhya-Yoga und die Bedeutung der Nidanas.pdf_by_PaddleOCR-VL-1.6.json` | `22032b4dc005945469cb2185f4e51fcd15e854bedd89e76f71a52802ac8d9d80` | Hermann Jacobi 1898, pp.1–15; already resolved, now local control |
| `提取自12946592543477.pdf_by_PaddleOCR-VL-1.6.json` | `4d90ddb33241d5a385b8887a5e3a50f8e0bb1fc6a9f225803185ed8462a0723f` | Hermann Oldenberg, `Buddhistische Studien`, ZDMG 52 (1898), relevant section pp.681–695; already resolved, now local control |
| `mlangescharlesd00goog.pdf_by_PaddleOCR-VL-1.6.json` | `bfa9b7474ca3b028c81dee3ca749a61c9476133aabd4f2bfd76358ff7ea16028` | full `Mélanges Charles de Harlez`; Senart 1896 article pp.281–297; already resolved, now stable full-volume witness |
| `Nirvāṇa.pdf_by_PaddleOCR-VL-1.6.json` | `4208ba84fe5580369d1d3c6ef9941ee60386161c34e5b3c40d2644cf6698ba79` | Joseph Dahlmann, `Nirvāṇa` (1896); P0 p.14 target resolved |
| `A simplified grammar of the Pali language -- E_ Müller -- 1884 -- 49974c7ed7dd5c19598b36ae3a773025 -- Anna’s Archive.pdf_by_PaddleOCR-VL-1.6.json` | `bd10b03d1283b3f8287aa9b15a7b4ed3473202eea96fb025e7744c15eda81923` | Edward Müller, 1884 Trübner; p.30 target checked negative, relevant material p.36 |
| `buddhismbeingske00daviiala.pdf_by_PaddleOCR-VL-1.6.json` | `c89228951a85079a5ebb282ec908fd781510885078ef869fc5ae20143464d953` | T. W. Rhys Davids, `Buddhism: Being a Sketch...`, 1894 revised ed.; exact Lovejoy quotation locus resolved at p.113 |
| `buddhaseinleben03oldegoog.pdf_by_PaddleOCR-VL-1.6.json` | `84fbe9f24394b0419fb7057e0ff546665173ac3e93c655d30b642439a10f9a3f` | Oldenberg `Buddha`, title page explicitly `ZWEITE AUFLAGE`; 1890 second edition; edition-control negative for the required 1897 third-edition loci |
| `23661047.pdf_by_PaddleOCR-VL-1.6.json` | `5e3ad9d3a656cf545e8db5dd8fe7fd56b45f34083968f78f72df5845ce53c50d` | Marillier, `La place du totémisme`, RHR 36 (1897), first installment pp.208–253; primary/control witness |
| `Revue_de_l_histoire_des_religions.pdf_by_PaddleOCR-VL-1.6.json` | `741c17e8aaa93f9807a834465e1276ca503f9c0a880d37f6d6196651dc365bba` | complete RHR tome 37 (1898), 509 OCR pages; major new resolution for 005 |

OCR is treated as a reading scaffold. Printed page numbers were checked from page-number blocks where possible; unusual Pāli/Sanskrit spellings are not silently regularized from PaddleOCR output.

---

## 2. 004 lexical fork: Rhys Davids exact locus is now resolved

The uploaded 1894 revised edition of T. W. Rhys Davids, `Buddhism: Being a Sketch of the Life and Teachings of Gautama, the Buddha`, contains the exact passage Lovejoy quotes in his 1898 article on printed **p.113**.

Rhys Davids there calls `upādi` a comprehensive name for the five skandhas and derives it, with an explicit allusion to their cause `upādāna`, from `upādā`, `to grasp`. He then uses the relation to explain the conventional distinction between the Arahat's living state, in which the skandhas remain, and final extinction.

This closes the Batch 32 / Batch 41 `Rhys Davids exact locus` target:

> **Rhys Davids, 1894 revised ed., printed p.113.**

It also confirms that Lovejoy's quotation is not a secondary paraphrase accidentally attributed to Rhys Davids. The wording and argumentative context are in the primary book itself.

Research consequence: the Childers/Rhys-Davids side of Lovejoy's lexical fork is now page-level primary-secure. A Childers facsimile remains desirable for final citation hygiene but is no longer needed to establish Rhys Davids's own formulation.

---

## 3. Dahlmann p.14: resolved, but Lovejoy compresses the nature of the comparison

The uploaded Dahlmann `Nirvāṇa` resolves printed **pp.13–15**, including Lovejoy's exact footnote target p.14.

The sequence is more nuanced than a bare lexical equation.

- On p.13 Dahlmann explains the orthodox framework of individualizing `upādhi` conditions and the two-stage salvation vocabulary in which liberation can occur while such conditions remain and become complete when they disappear.
- On p.14 he argues that a closer/internal connection exists between Buddhist `anupādisesanibbāna` and orthodox `anupādhīśeṣanirvāṇa`.
- But in the same movement he explicitly says that the orthodox sense cannot simply be sought in Buddhism, because Buddhism does not posit the same enduring substantial self behind the conditions.
- P.15 continues the anti-substantialist consequence.

This means Lovejoy's 1898 sentence — that according to Müller and Dahlmann Sanskrit `upadhi` is the equivalent of Pāli `upādi` — is a compressed characterization of Dahlmann's comparison. Dahlmann p.14 supports a close historical/conceptual relation, but not a context-free dictionary identity.

Status: **P0 resolved**.

Research consequence: Lovejoy's methodological move on p.134 remains important. The sources he sets against Childers/Rhys Davids are not simply giving a rival one-word gloss; at least Dahlmann embeds the parallel in a broader problem of doctrinal continuity and difference. Lovejoy reduces that field to an etymological fork and then refuses to let either genealogy decide semantics by itself.

---

## 4. Müller p.30: the expected citation does not work in the uploaded 1884 witness

This is the most important negative result on the 004 side.

Lovejoy's clean 1898 text explicitly prints footnote 3 as:

`Pali Grammar, p. 30.`

The uploaded Edward Müller 1884 Trübner grammar is therefore the correct bibliographic work to test. In that witness:

- printed **p.30** is ordinary consonantal/phonological discussion and contains no `upādi`, `upadhi`, `upādisesa`, or equivalent statement relevant to Lovejoy's claim;
- printed **p.36** contains the relevant phonological equation. PaddleOCR reads the critical expression approximately as `upādisea=upadhiqesha`, followed by a reference to Oldenberg, `Buddha`, p.437ff. The OCR spelling is imperfect, but the location and function of the example are clear: Müller is discussing loss of aspiration and gives the Pāli/Sanskrit correspondence here.

Current safest judgment:

> **In this 1884 Trübner witness, Lovejoy's p.30 citation does not support the claim he attaches to it; the relevant Müller evidence occurs on printed p.36. The most economical explanation is a six-page citation slip, but this remains a hypothesis until a differently paginated witness or Lovejoy's own working copy can be excluded.**

Do not silently emend Lovejoy's footnote to p.36 in quotation. The discrepancy is itself source-critical evidence.

Status: **target checked; expected p.30 claim negative; relevant locus p.36 recovered; edition/pagination control remains optional.**

---

## 5. The Oldenberg `...03...` upload is definitively the wrong edition for the live 1897 problem

The uploaded file whose filename contains `buddhaseinleben03oldegoog` is not the required third edition. Its title page explicitly says **`ZWEITE AUFLAGE`**, and its preface is `Vorwort zur zweiten Auflage`; the library stamp/date is 1890.

Printed p.273 in this second edition discusses Buddhist `substanzlose Causalität`; its footnotes do not contain the Senart `upādāna = upādānakkhandha` note to which Jacobi later points in the third edition.

That negative result is historically coherent: Senart's relevant article appeared in 1896, so the 1890 second edition could not contain a response to it.

Status: **edition-control resolved; live retrieval not resolved.**

Still needed:

- Oldenberg, `Buddha`, true **3rd enlarged ed. (1897)**;
- title/front matter;
- printed p.273 note;
- pp.443–455, especially Jacobi's p.448ff reference.

This upload should remain in the corpus as an earlier-edition control, not be treated as a failed extraction.

---

## 6. Senart, Jacobi 1898, and Oldenberg 1898 uploads: full local controls, no reversal of Batch 33

The full `Mélanges Charles de Harlez` object reproduces Senart's 1896 `À propos de la théorie bouddhique des douze nidânas` at printed pp.281–297 and confirms the Batch 33 reconstruction: Senart explicitly decomposes the formula historically, treats `upādāna` as a compressed skandha term, discusses filiation/stratification, and warns against reading inherited numerical nomenclature as a transparently deliberate philosophical system.

The uploaded Jacobi 1898 article and Oldenberg ZDMG 52 extract likewise confirm the already-recovered controversy controls. They do not restore a Lovejoy priority claim. The central 004 history remains:

> **Lovejoy entered an active Senart–Jacobi–Oldenberg dispute and recomposed already-live philological controls rather than independently inventing the problem.**

The still-missing Jacobi 1897 GGA review of Dahlmann remains the highest-value 004 manual target because Jacobi 1898 explicitly points backward to that notice at printed pp.268 and 272.

---

## 7. RHR 37 (1898): Priority E is fully resolved

The uploaded complete `Revue de l'histoire des religions`, tome XXXVII (1898), contains both remaining installments of Marillier's `La place du totémisme dans l'évolution religieuse`:

- third article: printed **pp.204–233**;
- fourth and final article: printed **pp.345–404**.

This closes the old 005 retrieval queue's Priority E in full.

The new primary text matters because it moves several methodological claims closer to Lovejoy's Paris year than the later Mauss retrospective evidence.

### 7.1 Blood as direct/magical efficacy, not automatically sacramental union

At printed p.210 Marillier describes cases in which what acts is the magical virtue of blood, intensified when the blood belongs to a chief possessing superior `mana`. In the same discussion, blood can invigorate, cure, or communicate force.

At p.351 he analyzes a protective blood rite as having immediate/direct efficacy against hostile spirits rather than working through the assistance of protective gods. This is a particularly close contemporary comparator for the causal distinctions later visible in 005.

### 7.2 Co-occurrence and resemblance do not establish causal origin

At printed p.211 Marillier makes the evidentiary point explicitly: the coexistence of two kinds of practice/conception in the same populations does not by itself establish a cause-and-effect relation between them. In context, magical properties attributed to blood need not therefore be generated by one specific form of totemic social organization.

At p.401 the same discipline is applied to resemblance and borrowing: undeniable similarities are insufficient grounds for hurriedly inferring borrowing or conscious imitation; even where borrowing of ritual forms occurs, the receiving cult may have existed or developed independently.

This is an unusually clean contemporary primary control for the project's `provenance/function` distinction. It should not be converted into a claim that Lovejoy read this exact page.

### 7.3 Marillier's final sacrifice classification is explicitly plural

Printed p.402 gives a compact menu of different possible sacrificial mechanisms: gift/propitiatory transaction; common meal or sacramental communion; expiatory/purificatory immolation; and blood effusion endowed with magical value/efficacy.

That is structurally close to notebook 005's repeated decomposition of sacrifice by mechanism. The important point is not identity of vocabulary but refusal to infer one causal class from a shared outward form.

### 7.4 The final anti-Jevons judgment is stronger than the earlier partial installments alone showed

Across pp.383–404 Marillier repeatedly rejects a universal totemic derivation of agrarian, first-fruit, celestial, and sacrificial rites. P.383 calls the forced totemic reading of first-fruit practices unduly simplifying where a vegetation-divinity explanation fits the evidence better; p.392 allows a first-fruit rite to function as communion while also neutralizing/diverting sacred power and while its agricultural function may be independent in origin; p.403 concludes that the attempt to derive all religious forms from totemism depends on an artificial unity that excludes contrary facts.

The resulting rule is not `totemism is false`; it is a rule about explanatory scope:

> **a locally successful explanation does not gain universal jurisdiction merely because analogous forms recur.**

This is the best current printed comparator for the anti-unilateral operator already reconstructed in 005.

---

## 8. New source-network result at Marillier 1898 p.351

The footnotes to Marillier's printed p.351 materially tighten the shared-source field around 005.

In the discussion of magical/protective blood efficacy, Marillier explicitly cites:

- H. C. Trumbull, `The Blood Covenant` (1893), for magical/curative blood material;
- Dorman;
- Mary Kingsley, `Travels in West Africa`, p.451;
- H. Clay Trumbull, `The Threshold-Covenant` (1896), chapters 1–3;
- further blood-covenant/cannibalism comparanda.

Existing 005 source work independently shows Lovejoy using Trumbull and Kingsley at other exact pages. The page numbers are not identical, so this is **not** proof of page-to-page copying or of a shared handout. What it does establish is a named-source overlap in the immediate Marillier research apparatus at the threshold of Lovejoy's Paris seminar year.

The evidentiary upgrade is therefore:

> `same broad comparative-religion themes`
>
> → **`same Marillier institutional environment + contemporaneous Marillier print method + overlapping named source field`**.

Direct transmission still requires a manuscript/report/letter/course-paper link.

---

## 9. Reviewer identities in RHR 37 are now resolved; Batch 61's negative is superseded

Batch 61 correctly refused to infer reviewer identities from issue adjacency because the accessible metadata then did not establish them. The full RHR 37 upload now settles both.

### Rhys Davids review

The review of T. W. Rhys Davids, `Buddhism, its history and literature`, begins at printed p.241 and ends at p.249 with the signature **`L. Finot.`** The volume table of contents independently lists the item as `(L. Finot)`.

This matters because Finot's review itself is methodologically alert to the question of Buddhist originality and possible antecedents. It is useful as Paris reception ecology, not as evidence that Lovejoy read the review.

### Trumbull review

The review of H. Clay Trumbull, `The Threshold-Covenant`, begins at printed p.405 and runs through p.419. The table of contents attributes it to **L. Marillier**, and the review itself ends with `L. MARILLIER.`

This is a major correction/upgrade. We can now say securely:

> **Marillier personally reviewed `The Threshold-Covenant` in RHR 37 (1898).**

We still cannot say that Lovejoy obtained Trumbull from Marillier or read this review unless independent evidence establishes that route.

---

## 10. Marillier's Trumbull review: a contemporaneous statement of the operator visible in 005

The Trumbull review, printed pp.405–419, is one of the highest-value returns in the upload round.

Marillier grants Trumbull's documentary labor and the reality of many of his facts, but attacks the scale of the inference drawn from them.

- Pp.406–407: a theory may explain only part of the facts; theological premises can push an ethnographic synthesis beyond what its evidence warrants.
- P.407: Marillier objects to making all divine relations into alliance and all sacrifice into mystical union; he explicitly points to protective magical rites whose efficacy is not divine assistance.
- P.408: the cited facts can be accurate while being assigned a scope and generality they do not possess. Marillier describes the recurring error as explaining everything through one order of facts and arbitrarily reducing the others to it.
- Pp.409–410: mutually incompatible one-factor theories — all magic, all union, all fear, all love — share the same defect: exclusivism. The methodological rule is to distrust overly simple explanations and claims that one primordial rite or belief generated the whole religious field. More highly specified institutions may be endpoints rather than origins of an evolutionary process.

This gives a stronger chronology for the 005 argument than relying only on Mauss's 1902 retrospective credit to Marillier's `critique des faits`.

Safe historical formulation:

> **Immediately before/during the intellectual world of Lovejoy's Paris year, Marillier's own published work was explicitly policing the move from accurate facts to overgeneralized causal classes. Notebook 005 repeatedly performs a comparable operation by retaining cases while redistributing them among different causal mechanisms.**

Do not upgrade this to `Lovejoy learned the rule from this review` without a reading/transmission trace.

---

## 11. Relation to the existing EPHE/005 concordance

The new RHR evidence strengthens, but does not replace, the independent institutional anchor: Lovejoy is already documented as taking an active part in Marillier's 1898–99 EPHE conferences, while 005 moves through survival of the soul, human sacrifice, ritual anthropophagy, magical sacrifice, blood, agrarian/fecundative rites, and competing causal mechanisms.

The new source layer adds three things:

1. **contemporaneity** — the strongest methodological parallels are now present in Marillier's own 1898 print, not only in later testimony about his method;
2. **source overlap** — Trumbull and Kingsley are demonstrably in Marillier's immediate printed source apparatus, while 005 independently uses those authors;
3. **mechanism vocabulary** — Marillier explicitly separates sacramental communion, expiation/purification, gift, and magical blood efficacy in the same article sequence.

This is enough to upgrade the working model from generic thematic influence to a historically specified comparative-research field. It is still not enough to reconstruct a literal seminar handout or direct article-to-notebook copying chain.

---

## 12. `23661047` Marillier 1897 first installment: useful primary control, but no false `mana` hit

The separate JSTOR OCR `23661047` is the first 1897 installment of `La place du totémisme`, RHR 36, pp.208–253.

It directly supports the already-established anti-unilateral rule: hypotheses may be only partially exact; a given motive need not be unique; later forms need not derive exclusively from totemism.

A simple substring search for `mana` is unsafe in this OCR because it produces false positives inside unrelated strings. This 47-page object should therefore **not** be cited as the secure location of Marillier's `mana` usage. The complete 1898 RHR 37 upload, by contrast, does contain secure `mana supérieur` passages at printed p.210.

This distinction matters for publication-grade source control.

---

## 13. Revised live manual-retrieval queue after the full upload pass

### 004 — highest remaining

1. **P0: Jacobi's 1897 GGA review of Dahlmann**, printed pp.267–273, especially pp.268 and 272. This remains the highest-yield missing bridge.
2. **P1: Oldenberg `Buddha`, true 3rd enlarged ed. (1897)**: title/front matter, p.273 note, pp.443–455/p.448ff.
3. **P2 / citation hygiene: Childers facsimile**, entry `Upādiseso`.
4. Optional Müller edition/pagination control if we want to establish whether Lovejoy's `p.30` can be explained by a different witness rather than a citation slip.

Dahlmann p.14 and Rhys Davids p.113 are no longer manual targets.

### 005 — highest remaining

1. **P0: Marillier review of Steinmetz, `Endokannibalismus`, RHR 34 (1896), pp.113–118**, with pp.113–115 minimum. This remains the strongest unresolved proposition-level test because 005 explicitly writes the Steinmetz title.
2. **P0/A2: Steinmetz primary packet**, especially p.45, p.52, pp.59–60; pp.36–47 if convenient.
3. **P1: N. W. Thomas, RHR 38 (1898), pp.295–347**, as the Marillier-era student-product control.
4. **P1: Marillier review of Codrington, RHR 25 (1892), pp.231–232.**
5. **P2: Marillier 1892 Frazer article exact `mana` locus** and 1900 `Religion` p.349/final pagination for wording/history controls.

The old Priority E (`La place du totémisme`, RHR 37, 1898) is **fully resolved** and should be removed from the live request list.

---

## 14. Evidence discipline after Batch 142

### Primary-secure

- Rhys Davids 1894 revised ed. p.113 is the exact source of the formulation Lovejoy quotes.
- Dahlmann 1896 p.14 directly establishes a close Buddhist/orthodox comparison but also marks a doctrinal limit to transferring the orthodox meaning.
- Müller 1884 printed p.30 does not contain the cited equation in this witness; printed p.36 contains the relevant phonological correspondence.
- the uploaded Oldenberg `Buddha` is the 1890 second edition, not the required 1897 third.
- RHR 37 contains Marillier's 1898 continuation pp.204–233, 345–404.
- the RHR 37 Rhys Davids review is by L. Finot.
- the RHR 37 `Threshold-Covenant` review is by Léon Marillier.
- Marillier 1898 explicitly distinguishes several sacrificial mechanisms and repeatedly limits inference from resemblance/co-occurrence to common origin.

### Strong contextual/institutional combination

- Lovejoy's documented EPHE participation + 005's mechanism sorting + Marillier's contemporaneous 1898 printed method + overlapping named sources now form a substantially stronger historical field reconstruction than a generic `French influence` claim.

### Still inference / not established

- that Lovejoy personally read RHR 37;
- that Marillier handed Lovejoy the Trumbull/Kingsley references found at p.351;
- that 005 directly copies the 1898 article or the `Threshold-Covenant` review;
- that Lovejoy's Müller p.30 is certainly a simple typo rather than pagination inherited from another witness;
- the wording of Oldenberg's 1897 third-edition p.273 note;
- the contents of Jacobi's 1897 GGA notice beyond what the 1898 article's backward references establish.

## Working paper consequence

The 005 case can now be stated more precisely:

> **The strongest Paris continuity lies not in a single borrowed doctrine but in a disciplined way of limiting explanatory scope. Marillier's 1898 writings distinguish co-presence from causation, resemblance from borrowing, sacramental union from magical efficacy, and partial explanation from universal origin. Lovejoy's Paris notebook repeatedly carries out the same kind of decomposition across afterlife, sacrifice, blood, fetish/charm and anthropophagy. The EPHE record supplies the institutional bridge; the RHR volume supplies a contemporaneous primary control for the operator.**

This should remain a methodological-field claim unless direct seminar papers, letters, or reading traces tighten the transmission chain further.
