# Batch 198 — Wilson entry 176 and the Indic visibility hierarchy: Vedānta, Deussen, Śaṅkara, Rāmānuja, and index granularity

Date: 2026-08-26
Status: synced / INCOMING-EDGE + INDEX-GRANULARITY CONTROL
Scope: follow-up to Batches196–197. This pass audits Wilson entry 176, Lovejoy's 1907 review of Paul Deussen's *Outline of the Vedanta System of Philosophy, according to Shankara*, for outgoing and incoming formal cross-references, then compares the recoverability of `Deussen`, `Vedānta`, `Śaṅkara`, `Rāmānuja`, `Hindu philosophy`, and `India` across Wilson's annotation, author/title index, and subject index.

## Core result

Entry 176 strengthens the partition identified in Batch197, but adds a more precise mechanism: **Indic material survives in Wilson at different levels of bibliographic visibility**.

The recovered architecture is not simply `indexed` versus `not indexed`. It has at least three grades:

1. **subject-index visibility** — e.g. `Buddhism, 19, 243`;
2. **author/title-index visibility without a subject genealogy** — entry176 is recoverable under `Deusen [Deussen], Paul, 176` and `Outline of the Védanta System of Philosophy, 176`;
3. **annotation-only visibility** — Śaṅkara, Rāmānuja, and `Hindu philosophy` are substantively present in Wilson's annotation of entry176, but no separate alphabetic index headings for them are recovered in the corresponding index ranges.

At the formal cross-reference layer, entry176 is even thinner:

- no outgoing `See` line occurs before entry177 begins;
- an exact-text audit for `See 176` returns no recovered match in Wilson's searchable full text or the repository OCR witness.

The safest formulation is therefore:

> **Entry176 is richly informative at annotation level, author/title-indexed at retrieval level, but presently unconnected at Wilson's formal `See` layer.**

This makes the early Indic corpus less a case of disappearance than a case of **progressive loss of relational resolution** across bibliographic layers.

---

## 1. Entry176 is a complete review node

Wilson's entry is:

**176. Deussen, Paul. *Outline of the Vedanta System of Philosophy, according to Shankara*. JP 4 (1907), 23–24.**

Wilson's annotation records three distinct facts about Lovejoy's review:

- the English outline derives from Deussen's larger *System des Vedānta*;
- Lovejoy considers the translation useful for those teaching Hindu philosophy;
- Lovejoy urges scholars to study the Vedānta system of **Rāmānuja** rather than continue multiplying studies of **Śaṅkara**.

This is considerably more than a generic notice of a book on India. It documents an evaluative intervention inside contemporary Vedānta scholarship: Lovejoy distinguishes between already heavily studied Śaṅkara and a comparatively under-studied Rāmānuja line and makes a recommendation about future scholarly allocation.

### Evidence grade

`DIRECT BIBLIOGRAPHIC ANNOTATION` — Wilson's representation of Lovejoy's 1907 review.

To recover Lovejoy's exact wording, reasoning, and bibliographic knowledge, the 1907 review itself remains the required primary-text control.

---

## 2. Entry176 has no outgoing formal `See` edge

The recovered sequence is decisive at the entry level:

- entry176 citation;
- Wilson's complete annotation;
- immediately thereafter entry177 begins;
- entry177 itself ends with `See 178`.

There is therefore no space in the recovered entry for an outgoing `See` line.

Controlled statement:

`176 → ∅ [W-SEE outgoing]`.

This puts 176 in the same formal category as the already controlled early Indic nodes:

`19 → ∅ [W-SEE outgoing]`

`243 → ∅ [W-SEE outgoing]`

`176 → ∅ [W-SEE outgoing]`.

The three nodes differ sharply, however, in the kinds of indexing that preserve them.

---

## 3. No incoming `See 176` has been recovered

An exact full-text search for the string:

`See 176`

returns no match in the searchable Wilson text. The repository OCR witness independently returns zero exact matches, although its JSON structure and OCR variability make a zero result weaker than a positive match.

Current graph status:

`? → 176 [W-SEE incoming] = NONE RECOVERED`.

This should **not** be upgraded to the absolute statement `no incoming reference to 176 exists anywhere under any OCR variant`. The controlled conclusion is narrower:

> no formal incoming `See 176` is presently recoverable by exact-text audit.

For graph construction, 176 should therefore remain an **entry-level formal dead end** until a contrary witness is found.

---

## 4. Wilson nevertheless makes 176 retrievable twice in the index

The index provides two explicit routes to entry176.

### Author route

`Deusen, Paul, 176`

The spelling `Deusen` is an OCR/rendering defect for Deussen, but the entry number is unambiguous.

### Title route

`Outline of the Védanta System of Philosophy, 176`.

Thus entry176 is not bibliographically invisible. It has **categorical retrieval through named bibliographic objects** even though it lacks a formal developmental cross-reference.

This suggests an index-role refinement to the Batch196 taxonomy:

- `W-IDX-SUBJ` — subject heading links multiple works through a category;
- `W-IDX-AUTH` — author-name index retrieval;
- `W-IDX-TITLE` — work-title index retrieval.

All remain subtypes of `W-IDX`; the refinement prevents author/title discoverability from being mistaken for subject-level conceptual grouping.

For 176:

`Deussen —[W-IDX-AUTH]→ 176`

`Outline of the Védanta System of Philosophy —[W-IDX-TITLE]→ 176`.

There is no recovered `Vedānta —[W-IDX-SUBJ]→ 176` heading.

---

## 5. Śaṅkara and Rāmānuja survive at annotation level, not as recovered index nodes

Wilson's annotation names both **Śaṅkara** and **Rāmānuja**. Yet examination of the alphabetic index ranges gives a different retrieval picture.

### R-range

The index moves through Ramsperger, Randall, Rationalism, Religion, Riley, Rousseau, Royce, Russell, etc. No separate `Rāmānuja / Ramanuja` heading is recovered.

### S-range

The index moves through Santayana, Schelling, Schiller, Schopenhauer, Science, Seligman, Sharp, Smith, Spinoza, etc. No separate `Śaṅkara / Shankara` heading is recovered.

The distinction is therefore:

`Śaṅkara` = `W-ANN content inside 176`

`Rāmānuja` = `W-ANN content inside 176`

rather than recovered independent `W-IDX` nodes.

This is not a trivial indexing detail. Wilson's annotation preserves Lovejoy's internal distinction between two Vedānta systems, while the index collapses retrieval back to the reviewed author/title object.

The conceptual resolution available to a reader who reads the annotation is therefore higher than the resolution available to a reader navigating only the index.

---

## 6. `Hindu philosophy` is likewise annotation-level language

Wilson says the translation would be useful for people teaching **Hindu philosophy**.

The H-range of the index contains items such as history of ideas, Hobbes, Hume, and human nature, but no recovered standalone `Hindu philosophy` heading.

Thus:

`Hindu philosophy` = `W-ANN conceptual field`

without a recovered independent `W-IDX-SUBJ` route.

This is particularly important because the phrase is broader than the book title's `Vedānta`. Wilson's prose recognizes a wider pedagogical field, yet the index does not visibly promote that field to a retrieval category.

---

## 7. `Vedānta` is preserved through title indexing, not as a recovered subject heading

The searchable text contains `Vedanta / Védanta` around entry176 and the title index entry `Outline of the Védanta System of Philosophy, 176`.

No independent alphabetic subject entry of the form:

`Vedānta, 176`

has been recovered.

This distinction matters because a title containing a concept is not the same bibliographic act as a subject index assigning that concept as a category.

The retrieval chain is:

`reader knows Deussen` → 176

or

`reader knows the title` → 176.

It is not visibly:

`reader searches Vedānta as a subject` → 176.

By contrast:

`reader searches Buddhism as a subject` → 19,243.

So the 1907 Indic material has a narrower Wilson retrieval aperture than the explicit Buddhist pair.

---

## 8. `India` survives in content but is not a recovered standalone index category

The explicit word `India` is recoverable in entry243's lecture title:

`The Place of Buddhism among the Philosophies of India`.

Batch197 also controlled Wilson's annotation of entry21, where Lovejoy's history of otherworldliness ranges across Western and Indian civilizations.

Yet inspection of the I-range of Wilson's index moves from Idealism / ideas to intellectual history and international topics without a recovered standalone `India` or `Indian philosophy` heading.

Current safe distinction:

- `India / Indian` = present in bibliographic annotations and titles;
- `India / Indian philosophy` = no standalone subject-index heading recovered in the audited index range.

This is stronger than a raw keyword search because the alphabetic location where such a heading would occur has been directly inspected.

---

## 9. A three-level visibility hierarchy now explains the Indic partition

Batches196–197 described differences between `formal genealogy` and `categorical continuity`. Entry176 allows that second category to be decomposed further.

### Level 1 — subject-index categorical continuity

Example:

`Buddhism —[W-IDX-SUBJ]→ 19,243`.

This tells a reader that multiple Lovejoy objects belong to one conceptual field.

### Level 2 — author/title bibliographic retrieval

Example:

`Deussen —[W-IDX-AUTH]→ 176`

`Outline of the Védanta System of Philosophy —[W-IDX-TITLE]→ 176`.

This makes a specific bibliographic object retrievable without constructing a wider Indic conceptual cluster.

### Level 3 — annotation-only semantic resolution

Example:

`Śaṅkara`

`Rāmānuja`

`Hindu philosophy`.

These become visible only once the reader enters Wilson's prose annotation.

This hierarchy sits beneath a fourth, stronger level already established elsewhere:

### Level 0 — formal genealogical routing

Examples:

`21 ↔ 22 ↔/→ 51 → 5`

`17 ↔ 139`

`26 ↔ 57`.

Those networks make diachronic continuity explicit through `See` edges and retrospective annotation.

The early Indic material is therefore not merely `sparse`. Its components occupy systematically weaker relation layers.

---

## 10. Comparative topology: 19 / 243 / 176 versus 21 / 22 / 51

### Indic / Buddhist / Vedānta nodes

```text
19 Buddhistic Technical Terms
  → ∅ [outgoing W-SEE]
  ↘
   Buddhism [W-IDX-SUBJ]
  ↗
243 Philosophy of Buddhism syllabus
  → ∅ [outgoing W-SEE]

176 Deussen / Vedānta review
  → ∅ [outgoing W-SEE]
  ← no exact incoming `See 176` recovered
  ← Deussen [W-IDX-AUTH]
  ← Outline of the Védanta System... [W-IDX-TITLE]
  contains Śaṅkara / Rāmānuja / Hindu philosophy [W-ANN]
```

### Temporalist / Great-Chain nodes

```text
21 Religion and the Time-Process
 ↔ 22 Dialectic of Bruno and Spinoza
 ↘  ↙
   51 Obsolescence of the Eternal
    ↓
    5 Great Chain of Being
```

The difference is not the difference between `present` and `absent`.

It is the difference between:

- **formal diachronic routing**, and
- **increasingly local retrieval metadata**.

That is a more exact historiographical object.

---

## 11. What Wilson preserves about Lovejoy's 1907 intervention

Even though the graph around 176 is thin, Wilson's annotation preserves a surprisingly specific scholarly judgment.

Lovejoy is not merely receiving `Indian philosophy` as a single generic body of doctrine. He discriminates within Vedānta scholarship and recommends a shift of attention from Śaṅkara toward Rāmānuja.

At minimum this implies that Wilson had evidence in Lovejoy's review for:

- awareness of differentiated Vedānta traditions;
- awareness of the asymmetry of modern scholarship devoted to them;
- an evaluative view about where further study should go.

The 1907 primary review must now be recovered because it can answer a question Wilson cannot:

> What exactly did Lovejoy know about Rāmānuja, and on what textual or scholarly basis did he judge the Rāmānuja line under-studied?

That is a source-level question, not a bibliographic one.

---

## 12. Historiographical consequence: `index-granularity loss`

The recurring problem can now be named descriptively without attributing motive:

**index-granularity loss** = information preserved in annotation prose but not promoted to an independent retrieval node.

For entry176:

`Deussen / book title` survive as explicit index entries;

while

`Śaṅkara / Rāmānuja / Hindu philosophy` remain embedded in annotation prose.

For the earlier corpus:

`Buddhism` receives a subject node joining 19 and243;

while the cross-links between Buddhism, Indian otherworldliness, Vedānta material in entry22, and the 1907 review are not encoded as a Wilson genealogy.

The practical effect is that a reader following Wilson by explicit cross-reference or index heading can recover the pieces but is unlikely to reconstruct the same cross-disciplinary Indic field that emerges when the primary texts are read across genre boundaries.

This is an observable property of the bibliography's architecture. It does not require a claim about Wilson's intention.

---

## 13. Updated relation taxonomy

Batch196's `W-IDX` should now be treated as a family:

| Code | Meaning | Example |
|---|---|---|
| `W-IDX-SUBJ` | Wilson subject-heading relation | `Buddhism → 19,243` |
| `W-IDX-AUTH` | Wilson author-name index relation | `Deussen → 176` |
| `W-IDX-TITLE` | Wilson work-title index relation | `Outline of the Védanta System... → 176` |
| `W-ANN` | relation/content present only in annotation prose | `176 → Śaṅkara / Rāmānuja / Hindu philosophy` |
| `W-SEE` | formal entry cross-reference | none recovered for 176 |

Do not infer equal historiographical force from these edge types.

---

## Evidence ceiling

### DIRECT BIBLIOGRAPHIC

Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography* (1982):

- entry176 and transition to entry177;
- Index D-range: `Deusen, Paul, 176`;
- Index O-range: `Outline of the Védanta System of Philosophy, 176`;
- Index R-range: no recovered Rāmānuja heading;
- Index S-range: no recovered Śaṅkara heading;
- Index H-range: no recovered `Hindu philosophy` heading;
- Index I-range: no recovered `India` / `Indian philosophy` heading;
- entry243: `Philosophies of India` inside the Buddhism syllabus;
- `Buddhism, 19,243` and `Otherworldliness, 21–22`, controlled in Batch197.

### INCOMING-EDGE CONTROL

- exact searchable-text audit: no recovered `See 176`;
- repository OCR exact-string audit: zero `See 176` matches, treated as corroborative rather than conclusive because OCR/JSON structure can produce false negatives.

### DO NOT CLAIM YET

- that no imaginable OCR variant could conceal an incoming reference to 176;
- that Rāmānuja, Śaṅkara, or Hindu philosophy are absent from Lovejoy's wider corpus;
- that Wilson consciously downgraded Indic materials;
- that the absence of a subject heading measures historical importance;
- that Lovejoy's 1907 recommendation concerning Rāmānuja was based on direct reading of Rāmānuja primary texts;
- that 19 → 243 → 176 is a causal developmental chain.

## Next controls

1. Recover Lovejoy's **1907 Deussen review** itself and identify his exact claim about Rāmānuja, including any named sources or textual basis.
2. Run a complete **incoming-reception audit** across Wilson's Part II for entries 19,243,176 and their exact titles, separating secondary discussions from index-only mentions.
3. Search the primary bibliography after 1907 for further review/article nodes involving Indian philosophy under names other than `Buddhism` or `Vedānta`.
4. Compare the index-granularity hierarchy against the actual early primary corpus: determine which relations Wilson leaves annotation-only that Lovejoy himself makes operational in argument.
5. Keep the working distinction: **formal genealogy / subject categorization / author-title retrieval / annotation-only semantics**.

## Evidence rule added

> **Bibliographic visibility has levels. A concept or figure preserved in annotation prose but absent as a subject/index node is not absent from the bibliography; it is harder to retrieve relationally. Formal `See`, subject index, author/title index, and annotation-only presence must remain separate evidence classes.**
