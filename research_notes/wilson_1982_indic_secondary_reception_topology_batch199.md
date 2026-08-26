# Batch 199 — Wilson's indexed secondary reception of the early Indic nodes: 19, 243, 176

Date: 2026-08-26
Status: synced / SECONDARY-RECEPTION TOPOLOGY CONTROL
Scope: follow-up to Batches196–198. This pass asks whether Wilson's Part II / Part III bibliography contains later items that he explicitly indexes as commenting on Lovejoy's 1898 Buddhist technical article (19), 1901 Buddhism syllabus (243), or 1907 Deussen/Vedānta review (176).

## Core result

Wilson supplies an unusually strong internal control for this question. His index instructions state that, for **title entries**:

- the **first number** is the annotation number of the work itself;
- **subsequent numbers** identify items which `in some fashion` comment on that book or essay.

This means title-index topology can be used as an explicit reception map rather than inferred from raw keyword frequency.

Under that rule, the three early Indic nodes are stark:

- `The Buddhistic Technical Terms upadāna and upādisea, 19`
- `Syllabus: The Philosophy of Buddhism, 243`
- `Outline of the Védanta System of Philosophy, 176`

Each title carries **only its own primary item number**. No subsequent commentary number is supplied.

By contrast, a nearby canonical control gives:

- `The Dialectic of Bruno and Spinoza, 22, 435`

where 435 is Wilson's 1980 retrospective article connecting the 1904 essay to *The Great Chain of Being*.

Therefore the strongest safe conclusion is:

> **Within Wilson's own index architecture, no secondary item in the bibliography is indexed as commenting on entries 19, 243, or 176, while entry22 has an explicit indexed secondary-reception edge to 435.**

This is stronger than saying the Indic material has a thin formal `See` graph. It shows that its **indexed reception graph is also empty** in Wilson's bibliography through his 1981 secondary-source cutoff.

---

## 1. Wilson explicitly defines how title-index reception edges work

Wilson's index preface states that the index cites author, title, and subject by item numbers. It then gives a special rule for title entries:

> the first number is the item's own annotation; subsequent numbers indicate items which in some fashion comment on the book or essay.

This turns the title index into a machine-readable relation layer.

We can therefore define:

`W-IDX-REC`

= a secondary or later item number appearing after the primary item's number in a Wilson title-index entry.

Example:

`The Dialectic of Bruno and Spinoza, 22, 435`

means:

`22 ←[W-IDX-REC]— 435`.

This relation is editorially asserted by Wilson's index design. It is stronger than our own thematic inference and distinct from a formal primary-entry `See` edge.

---

## 2. Entry19 has no indexed secondary-reception edge

The title index gives:

`The Buddhistic Technical Terms upadāna and upādisea, 19`.

There is no number after 19.

Under Wilson's stated title-index rule:

`19 ← ∅ [W-IDX-REC]`.

This complements the earlier controls:

- entry19 has no outgoing formal `See`;
- `Buddhism` subject index links 19 with 243;
- no title-indexed later commentary is attached to 19.

The topology is therefore:

```text
19
├── outgoing W-SEE: ∅
├── W-IDX-SUBJ: Buddhism → {19,243}
└── incoming W-IDX-REC: ∅
```

This is a much stronger form of bibliographic thinness than simple chronological isolation.

---

## 3. Entry243 has no indexed secondary-reception edge

The title index gives:

`Syllabus: The Philosophy of Buddhism, 243`.

Again, there is no subsequent number.

Thus:

`243 ← ∅ [W-IDX-REC]`.

Combined with Batch197:

- no outgoing formal `See`;
- subject co-indexed with 19 under `Buddhism`;
- no indexed later commentary.

The syllabus is retained as a primary bibliographic object and subject-category partner, but Wilson records no indexed secondary literature returning to it.

---

## 4. Entry176 has no indexed secondary-reception edge

The title index gives:

`Outline of the Védanta System of Philosophy, 176`.

There is no subsequent number.

Thus:

`176 ← ∅ [W-IDX-REC]`.

Batch198 had already established:

- outgoing `W-SEE`: none;
- exact incoming `See 176`: none recovered;
- author-index route: Deussen →176;
- title-index route: *Outline...* →176;
- Śaṅkara, Rāmānuja, and Hindu philosophy remain annotation-level content.

Batch199 adds the missing layer:

- **no Wilson-indexed secondary commentary on the review itself**.

This means 176 is retrievable as a bibliographic object but not visibly activated as a node in later Lovejoy scholarship represented by Wilson.

---

## 5. Entry22 provides the decisive positive control

Wilson's index gives:

`The Dialectic of Bruno and Spinoza, 22, 435`.

By Wilson's own rule, the second number means that item435 comments on entry22.

Entry435 is Daniel J. Wilson's 1980 article:

`Arthur O. Lovejoy and the Moral of The Great Chain of Being`.

Wilson's annotation of 435 retrospectively argues that Lovejoy's work on the Great-Chain problem began before 1902 and that much of the later framework was already visible by the 1904 Bruno–Spinoza essay.

So the canonical line possesses yet another explicit relation type:

`435 → 22 [W-IDX-REC]`.

That relation sits alongside:

- `22 ↔ 21 [W-SEE]`;
- `22 → 51 [W-SEE]`;
- `22 → 435 [W-SEE]`;
- `22 → 5 [W-ANN]`;
- `21–22 [W-INTRO]` as early history-of-ideas work;
- `Otherworldliness, 21–22 [W-IDX-SUBJ]`.

The difference in relation density is therefore multiply demonstrable.

---

## 6. The Indic nodes have primary preservation without indexed reception

The three nodes occupy different genres:

- 19: technical journal article;
- 243: lecture syllabus;
- 176: book review.

Yet all three share the same title-index reception state:

```text
19  ← ∅ W-IDX-REC
243 ← ∅ W-IDX-REC
176 ← ∅ W-IDX-REC
```

This common pattern cuts across genre.

Therefore the thinness cannot be explained solely by Wilson placing syllabi in a `Brief Notes` section or book reviews in a separate category. The 1898 peer-reviewed article shows the same lack of indexed later commentary.

The stronger historiographical question becomes:

> Was the early Indic corpus simply under-discussed in the secondary Lovejoy literature available to Wilson, rather than merely under-connected by Wilson's own editorial cross-referencing?

Wilson's title index supports that possibility, but cannot by itself decide why the secondary literature is thin.

---

## 7. Editorial architecture versus reception history

Batches196–198 mostly examined **Wilson's architecture**:

- which `See` edges he inserted;
- which subject headings he created;
- which concepts remained only in annotation prose.

Batch199 adds a distinct object:

**the reception literature Wilson claims to have indexed**.

The two should not be conflated.

### Editorial thinness

Wilson could have connected primary works through `See` or subject headings even in the absence of secondary literature.

### Reception thinness

Wilson's title-index rule indicates whether later bibliography entries comment on a specific work.

For 19,243,176, both forms are thin:

- weak/absent formal primary cross-routing;
- no title-indexed secondary commentary.

For 22, both forms are dense:

- multiple primary and retrospective `See`/annotation routes;
- explicit indexed secondary commentary through 435.

This distinction prevents us from assigning all topology to Wilson's editorial choices.

---

## 8. Wilson's secondary cutoff makes this a bounded historical claim

Wilson says his secondary bibliography is complete, so far as he knows, to **June 1981**, while acknowledging that some unindexed or inaccessible items may have escaped him.

Therefore Batch199's conclusion is bounded:

> As represented in Wilson's bibliography of secondary literature through June 1981, no later item is title-indexed as commenting on Lovejoy's entries 19,243,176.

It is **not** a claim that no one anywhere before 1981 ever mentioned them, still less that no post-1981 scholarship discusses them.

The next external historiographical task is therefore clear: search post-1981 scholarship and modern databases to determine whether these early Indic works remained invisible after Wilson or were subsequently recovered.

---

## 9. Reception-density comparison

| Primary node | Outgoing `W-SEE` | Subject-index relation | Title-index reception `W-IDX-REC` | Retrospective canonical routing |
|---|---|---|---|---|
| 19 Buddhist technical terms | none | `Buddhism → 19,243` | none | none recovered |
| 243 Buddhism syllabus | none | `Buddhism → 19,243` | none | none recovered |
| 176 Deussen/Vedānta review | none | no Vedānta subject heading recovered | none | none recovered |
| 22 Bruno–Spinoza | `21,51,435` | `Otherworldliness`, Neo-Platonism etc. | `435` | annotation + introduction + Great Chain route |

This table now separates three things that previously risked collapsing together:

1. Lovejoy's own early corpus;
2. Wilson's editorial relation architecture;
3. later secondary reception represented inside Wilson.

---

## 10. Consequence for the `Indic disappearance` question

The evidence now supports a more exact sequence.

### Primary corpus

Indic engagement recurs:

- 1898 technical Buddhist philology;
- 1901 Buddhism teaching;
- 1902 Indian civilization inside the otherworldliness problem;
- 1904 Indic/Vedānta material inside Bruno–Spinoza;
- 1907 Deussen / Śaṅkara / Rāmānuja review.

### Wilson's primary-source architecture

Those materials are partitioned among:

- Buddhism subject indexing;
- otherworldliness / temporalism;
- Western philosophical history;
- book review metadata.

### Wilson's represented secondary reception

The explicitly Indic items 19,243,176 have no title-indexed commentary nodes.

So what appears later as an `Indic disappearance` may be generated by **two successive processes**:

1. bibliographic repartition of the primary materials;
2. weak secondary reception of the explicitly Indic nodes.

This is a more defensible mechanism than attributing the effect to a single editorial decision.

---

## 11. New relation code

Add to the repository graph taxonomy:

`W-IDX-REC` — a later item number attached to a primary work's title entry under Wilson's explicit rule that subsequent numbers identify items commenting on that work.

Examples:

- `435 → 22 [W-IDX-REC]`;
- no such edges recovered for 19,243,176.

This edge should be kept distinct from:

- `W-SEE` formal cross-reference;
- `W-ANN` annotation relation;
- `W-INTRO` introduction genealogy;
- `W-IDX-SUBJ` subject classification;
- `W-IDX-AUTH` author retrieval;
- `W-IDX-TITLE` title retrieval;
- `S-IN` independently reconstructed secondary incoming relation.

`W-IDX-REC` is especially valuable because Wilson explicitly defines its semantics.

---

## Evidence ceiling

### DIRECT BIBLIOGRAPHIC / INDEX-METHOD CONTROL

Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography* (1982), Index preface:

- first number in title entry = item's annotation;
- subsequent numbers = items which in some fashion comment on the work.

### DIRECT TITLE-INDEX CONTROLS

- `The Buddhistic Technical Terms upadāna and upādisea, 19`;
- `Syllabus: The Philosophy of Buddhism, 243`;
- `Outline of the Védanta System of Philosophy, 176`;
- positive control: `The Dialectic of Bruno and Spinoza, 22,435`.

### SECONDARY-BIBLIOGRAPHY BOUNDARY

Wilson's preface states that the secondary sources are complete, so far as he knows, to June 1981, while allowing for possible missed unindexed material.

### DO NOT CLAIM YET

- that no pre-1981 scholar ever mentioned 19,243,176;
- that Wilson read every possible secondary source;
- that post-1981 scholarship continued the same reception pattern;
- that absence of indexed commentary proves low historical importance;
- that Wilson caused the secondary neglect;
- that all relations among Indic materials are recoverable from title indexing.

## Next controls

1. Run a post-1981 historiographical search for the exact titles of entries 19,243,176 and for `Lovejoy + Buddhism / Vedānta / Indian philosophy`.
2. Recover the 1907 Deussen review as primary text before making claims about Lovejoy's Rāmānuja knowledge.
3. Search Lovejoy's later primary bibliography for Indian-philosophy material hidden under personal names, review titles, or comparative philosophy rather than subject terms.
4. Compare post-1981 recovery, if any, against Wilson's 1982 reception baseline.

## Evidence rule added

> **Wilson's title index contains an explicit reception code: subsequent item numbers mark works that comment on the indexed title. A title followed only by its own item number is therefore evidence of no Wilson-indexed secondary reception, not evidence that the work never received any comment anywhere.**
