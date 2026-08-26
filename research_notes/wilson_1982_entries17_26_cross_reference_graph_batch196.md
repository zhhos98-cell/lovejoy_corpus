# Batch 196 — Wilson (1982), primary entries 17–26: cross-reference graph, bibliographic partitions, and the isolated Buddhist node

Date: 2026-08-26
Status: synced / BIBLIOGRAPHIC-ARCHITECTURE CONTROL
Scope: Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography* (1982), Part I.C, primary-source entries 17–26, with later-entry, introduction, and index cross-controls. This batch follows Batches193–195 and separates Wilson's own reference architecture from primary-text relations reconstructed independently in the repository.

## Core result

Wilson's entries 17–26 form a chronological run, but **not one relational genealogy**. Once formal `See` references, annotation prose, introduction-level retrospective claims, index co-location, and later secondary-source links are kept separate, the ten entries partition into several different subnetworks.

The strongest immediate result is negative only in a controlled bibliographic sense:

> Wilson's explicit retrospective route into the later history-of-ideas / *Great Chain of Being* narrative runs primarily through entries **21–22**, while entry **19**, the 1898 Buddhist technical-terminology article, is not incorporated into that route by a formal `See` edge in the recovered entry text.

At the same time, Wilson's index does not leave entry19 wholly unconnected: under **Buddhism** it co-indexes entry19 with entry **243**, the 1901 `Syllabus: The Philosophy of Buddhism`.

Thus there are two different architectures:

`19 (1898 technical Buddhist philology)`

→ `Buddhism` subject index

→ `243 (1901 Buddhism syllabus)`

versus

`21 (1902 religion / time-process)`

↔ `22 (1904 Bruno / Spinoza)`

→ later temporalism / otherworldliness / Great-Chain reception.

This is a **bibliographic partitioning effect**. It is evidence about Wilson's reference architecture, not evidence of an intention to marginalize Buddhism or of Lovejoy's own intellectual priorities.

---

## 1. Edge taxonomy

The graph uses six distinct edge types.

- `W-SEE` — Wilson's formal `See` cross-reference in an entry.
- `W-ANN` — a relation asserted in Wilson's annotation prose but not encoded in that entry's formal `See` line.
- `W-INTRO` — a retrospective relation asserted in Wilson's introduction.
- `W-IDX` — co-location or routing created by Wilson's index.
- `S-IN` — an incoming relation from a later secondary-source entry in Wilson's bibliography.
- `P-INFER` — a relation reconstructed independently from Lovejoy's primary text by this repository. **Never treat this as a Wilson edge.**

The distinction is essential because Wilson's annotations are critical guides, not merely neutral metadata, and the formal cross-reference network is itself selective.

---

## 2. Entry-by-entry graph

| Entry | Work | Formal outgoing `See` | Other Wilson relation | Primary network |
|---|---|---|---|---|
| 17 | `James Burnett, Lord Monboddo` (1895) | 139 | 139 later returns to 17 and 116 | evolution / intellectual history |
| 18 | `Some Harvard Notes` (1896) | 20 | 20 returns to 18 | university / education |
| 19 | `The Buddhistic Technical Terms upadāna and upādisea` (1898) | **none recovered in entry text** | index co-locates 19 with 243 under `Buddhism` | Buddhist / Indic philology |
| 20 | `The Social Rôle of the French University` (1900) | 18 | reciprocal with 18 | university / education |
| 21 | `Religion and the Time-Process` (1902) | 5, 22, 51, 435 | introduction pairs 21–22 as early history-of-ideas work; indexed under eternalism / temporalism / religion | religion / time / later Great-Chain genealogy |
| 22 | `The Dialectic of Bruno and Spinoza` (1904) | 21, 51, 435 | annotation says argument anticipates later *Great Chain*; introduction pairs 21–22 | history of ideas / Great Chain |
| 23 | `Ethics and International Relations` (1904) | 6–8, 16 | index routes to international relations / organizations | international ethics |
| 24 | `Recent Literature in Philosophy and Ethics` (1904) | **none recovered in entry text** | Wilson compresses a twelve-book review ecology into a short annotation; Batch195 restores internal relation types | review ecology / contemporary philosophy |
| 25 | `Religious Instruction in Non-Sectarian Colleges and Universities` (1904) | 82, 127–128 | connects forward into academic freedom / religious-neutrality corpus | academic freedom / religious neutrality |
| 26 | `Some Eighteenth Century Evolutionists` (1904) | 17, 48, 54, 57 | index places it inside a broad evolution cluster | evolution / history of science |

`none recovered` is deliberately narrower than `no cross-reference exists anywhere in the bibliography`. It means no formal `See` line has been recovered from that entry's own text in the present audit.

---

## 3. The Monboddo line is explicitly reciprocal and retrospectively rewritten

Entry17, the 1895 Monboddo essay, formally points to entry139. Entry139, `Monboddo and Rousseau` (1933), points back to **17** and also to **116**, `The Supposed Primitivism of Rousseau's Discourse on Inequality`.

This gives a real Wilson-encoded longitudinal chain:

`17 (1895 Monboddo)`

↔ `139 (1933 Monboddo and Rousseau)`

→ `116 (Rousseau / supposed primitivism)`.

Wilson's annotation of 139 makes the retrospective transformation visible. The later essay argues that Monboddo and Rousseau are not adequately described as simple advocates of primitivism. Monboddo instead participates in a new historical conception in which humanity begins in animality and ascends gradually toward rational and social existence, requiring a `new historical science` to reconstruct the process.

This is one of the strongest control cases in the 17–26 block because Wilson does not merely place the two Monboddo pieces near one another: he formally cross-links them across almost four decades.

**Graph status:** `W-SEE`, reciprocal 17 ↔ 139; 139 → 116.

---

## 4. The university pair is a closed reciprocal micro-network

Entries18 and20 are explicitly reciprocal:

`18 Some Harvard Notes`

↔

`20 The Social Rôle of the French University`.

The connection is institutional rather than doctrinal. Both concern universities as social/intellectual organisms, educational organization, public function, and the relation between academic institutions and wider civic life.

The importance for the present graph is formal: chronological adjacency does not explain the edge. Wilson has chosen to encode a thematic university network, while nearby philosophical and religious items receive different routing.

**Graph status:** `W-SEE`, reciprocal 18 ↔ 20.

---

## 5. Entry19: technically important, bibliographically fenced into `Buddhism`

Entry19 is Lovejoy's 1898 `The Buddhistic Technical Terms upadāna and upādisea`. Wilson summarizes it as a technical intervention whose interpretation of two terms is essential to understanding Buddhist doctrine and whose argument proceeds by correcting previous interpretations through analysis.

In the recovered entry text, **no formal `See` line appears**.

Wilson's index supplies a different relation. The subject heading `Buddhism` contains:

- 19 — the 1898 technical article;
- 243 — `Syllabus: The Philosophy of Buddhism` (Washington University Association, 1901).

Entry243 is a syllabus for four lectures:

1. `The Place of Buddhism among the Philosophies of India`;
2. and 3. `Two Essential Formulas of Buddhism`;
4. `Buddhist Ethics and its Goal`.

Thus the safest graph is:

`19`

— `W-IDX: Buddhism` —

`243`.

This is **not yet a formal 19 ↔ 243 `See` relation**. That control remains open.

The distinction becomes historiographically important because entry19 precedes entries21–22, yet Wilson's explicit Great-Chain / early-history-of-ideas retrospective architecture does not, in the recovered material, use entry19 as an upstream node. Instead, 19 is retained in a Buddhism-specific subject cluster.

What can be claimed now:

> Wilson's bibliography preserves the Buddhist work, but its recovered reference topology classifies it differently from the 21–22 line later routed toward temporalism, otherworldliness, and the Great Chain.

What cannot be claimed:

> Wilson deliberately excluded Buddhist material from Lovejoy's intellectual genealogy.

Intent is not recoverable from the graph alone.

---

## 6. Entries21–22 are Wilson's privileged early history-of-ideas pair

Entry21, `Religion and the Time-Process`, formally points to:

- 5;
- 22;
- 51;
- 435.

Entry22, `The Dialectic of Bruno and Spinoza`, formally points to:

- 21;
- 51;
- 435.

So 21 and22 are explicitly reciprocal:

`21 ↔ 22`.

Wilson's **introduction** strengthens this pair by identifying Lovejoy's early work on the history of religion and philosophy, especially 21 and22, as early exercises in the history-of-ideas method and as places where Platonic materials later central to his scholarship appear.

But formal and prose relations are not identical. Wilson's annotation of entry22 says that the Bruno–Spinoza argument anticipates *The Great Chain of Being*, while the entry22 `See` line itself does **not** include entry5. Entry21 does include 5.

Therefore:

- `21 → 5` = `W-SEE`;
- `22 → 5` = `W-ANN`;
- `21 ↔ 22` = `W-SEE`;
- Wilson's introduction grouping 21–22 = `W-INTRO`.

This asymmetry is precisely why the project must not collapse every Wilson relation into one undifferentiated edge.

---

## 7. Later secondary reception intensifies the 21–22 route

The 21–22 cluster receives later incoming support inside Wilson's bibliography.

A later entry by Robert M. Grant on chains of being in early Christianity directs readers to 5 and 21–22. Wilson's own 1980 article, entry435, `Arthur O. Lovejoy and the Moral of The Great Chain of Being`, retrospectively argues that Lovejoy's research into the problem antedated 1902 and that by the 1904 Bruno–Spinoza essay much of the later framework was already in place.

These are **secondary retrospective edges**, not primary evidence of what Lovejoy in 1898–1904 believed about the future trajectory of his work.

Graphically:

`later secondary reception`

→ `21–22`

→ `Great Chain`.

The network density around 21–22 is therefore partly produced by later historiography as represented and annotated by Wilson.

**Graph status:** `S-IN`.

---

## 8. Entry23 belongs to an international-ethics network, not the philosophy-of-history chain

Entry23, `Ethics and International Relations`, points formally to entries 6–8 and16.

Wilson's index independently groups `international organizations` around 6–8 and16 and `international relations` around 23 and later items. The immediate 1904 text discusses the moral status of intervention, the application of ethical principles to nations, Grotius, growing global interdependence, Suez/Panama, and a utilitarian criterion of general human well-being.

The formal edge therefore identifies a political / international-organizational subnetwork.

**Graph status:** `W-SEE`: 23 → 6–8,16.

Target titles for 6–8 and16 are not required to establish the edge; where not yet re-resolved in the current pass they remain `TITLE-PENDING` rather than being guessed.

---

## 9. Entry24 exposes bibliographic compression

Wilson's entry24 is `Recent Literature in Philosophy and Ethics`, the 1904 review essay analyzed in Batch195.

Wilson's annotation accurately identifies its broad scope — current philosophical literature, pragmatism, ethics, and history of philosophy — but the bibliography necessarily compresses the review's internal architecture.

Batch195 showed that the primary text contains at least six separate relation types:

- directly reviewed books;
- historical subjects reconstructed through those books;
- structural/classificatory comparanda;
- antecedent and influence nodes;
- translation/textual-control objects;
- historiographical-method exemplars.

No formal `See` line has been recovered in entry24 itself.

This makes entry24 an important methodological control:

`Wilson bibliographic node`

≠

`full primary-text relation graph`.

The absence of many graph edges at bibliographic level does not imply the absence of those relations in Lovejoy's 1904 text.

---

## 10. Entry25 is routed forward into academic freedom and religious neutrality

Entry25, `Religious Instruction in Non-Sectarian Colleges and Universities`, formally points to:

- 82;
- 127;
- 128.

Entry127 is `Anti-Evolution Laws and the Principle of Religious Neutrality` (1929), which analyzes anti-evolution statutes through the principle of religious neutrality. The surrounding later corpus includes Wilson's academic-freedom / AAUP materials.

Thus the 1904 essay is retrospectively routed into a long institutional and constitutional problem rather than into the 21–22 history-of-ideas cluster.

**Graph status:** `W-SEE`: 25 → 82,127,128.

Entries82 and128 remain `NUMBER-RESOLVED / TITLE-PENDING` in this pass; their thematic placement is controlled independently by Wilson's annotations and introduction.

---

## 11. Entry26 closes 1904 back onto Monboddo and forward into pre-Darwinian evolution

Entry26, `Some Eighteenth Century Evolutionists`, formally points to:

- 17;
- 48;
- 54;
- 57.

This is a dense longitudinal history-of-science line.

Entry48 is `The Argument for Organic Evolution Before 'The Origin of Species'` (1909), extending the pre-Darwinian problem into British biology/geology and Robert Chambers.

Entry54 is `Kant and Evolution` (1910–1911), where Lovejoy argues against the retrospective classification of Kant as a pioneer of biological evolution and stresses the danger of extracting expressions from their contexts and ignoring the meanings Kant gives to terms.

Entry57 remains `TITLE-PENDING` in this pass.

Most importantly, entry26 returns directly to 17. Wilson therefore encodes continuity between:

`1895 Monboddo`

→ `1904 eighteenth-century evolutionists`

→ `1909/1910–11 pre-Darwinian evolution studies`.

The index `Evolution` also includes 17,26,48,50–51,53–54,57 and many later items, confirming that this is one of Wilson's major subject networks.

**Graph status:** `W-SEE`: 26 → 17,48,54,57; reinforced by `W-IDX: Evolution`.

---

## 12. Seven subnetworks inside ten chronological entries

The 17–26 sequence is therefore better represented as seven subnetworks:

### A. University / educational institution

`18 ↔ 20`

### B. Explicit Buddhism / Indic philology

`19 —[W-IDX Buddhism]— 243`

### C. Religion / time / history of ideas / Great Chain

`21 ↔ 22`

`21 → 5,51,435`

`22 → 51,435`

`22 → 5 [W-ANN]`

### D. International ethics / organization

`23 → 6–8,16`

### E. Contemporary philosophy / review ecology

`24` as a bibliographically compressed node; internal graph restored separately in Batch195.

### F. Academic freedom / religious neutrality

`25 → 82,127,128`

### G. Evolution / pre-Darwinian intellectual history

`17 ↔ 139 → 116`

`26 → 17,48,54,57`.

The central rule is:

> **chronological adjacency ≠ Wilson's genealogical adjacency.**

---

## 13. Historiographical consequence for entry19

Batch193 identified a possible problem: Wilson's later narrative appeared to privilege those early essays that could be retrospectively made continuous with Lovejoy's canonical history-of-ideas work.

Batch196 now sharpens that observation from impression to reference topology.

The evidence is not that Wilson suppresses entry19. He includes it, annotates it, and indexes it under Buddhism together with entry243.

The evidence is that **the mechanisms by which Wilson later constructs longitudinal continuity are unevenly distributed**:

- 17 receives a reciprocal late-career Monboddo link;
- 18 and20 receive a reciprocal institutional link;
- 21 and22 receive reciprocal links, introduction-level elevation, Great-Chain routing, and later-secondary incoming edges;
- 25 and26 receive long forward chains into academic freedom and evolution;
- 19, in the recovered architecture so far, receives subject-index co-location with another Buddhist item rather than a formal forward genealogy.

This difference is analytically usable even without imputing intention.

A precise formulation is:

> **The partition is recoverable as an effect of Wilson's bibliographic architecture even where authorial intention is not inferable.**

---

## 14. Why this matters for the primary-source project

The repository's primary-text work now complicates Wilson's topology in two ways.

First, Batch192 showed that Indic material did not simply disappear after 1898: the 1904 Bruno–Spinoza article contains direct Vedānta / Muṇḍaka reuse within a Western metaphysical genealogy.

Second, Batches194–195 showed that Lovejoy's early method depends on preserving different relation types — historical source, structural comparandum, translation witness, transmission evidence, classification, and milieu — which a later annotated bibliography cannot fully encode.

Therefore Wilson remains indispensable as a map of reception and bibliographic organization, but his graph must be treated as an object of historiographical analysis rather than as a transparent substitute for Lovejoy's own archive.

---

## 15. Evidence ceiling

### DIRECT BIBLIOGRAPHIC

Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography* (1982):

- primary entries 17–26;
- entries 48,54,127,139,243 and later secondary cross-controls;
- Introduction;
- Index headings including `Buddhism`, `Eternalism`, `Evolution`, `International organizations`, `International relations`, `Spinoza`, and `Temporalism`.

### PRIMARY-TEXT CROSS-CONTROL

Repository Batches192, 194, and195.

### DO NOT CLAIM YET

- that entry19 has no incoming formal `See` anywhere in Wilson's entire bibliography until every occurrence of `See 19` is audited;
- that entry243 has or lacks a formal `See` to entry19 until the continuation of its entry is recovered;
- that Wilson intentionally marginalized Buddhist or non-Western material;
- that Wilson's index categories reproduce Lovejoy's own categories;
- that entry19 is causally continuous with 21 or22 merely because the texts are chronologically adjacent;
- that Wilson's Great-Chain routing exhausts the intellectual relations present in Lovejoy's primary texts.

## Next controls

1. Audit every exact occurrence of `See 19` and `See 243` in Wilson.
2. Recover the complete entry243, including any continuation and formal cross-reference line.
3. Compare index headings `Buddhism`, `India`, `Indian`, `religion`, `otherworldliness`, and `eternalism` to determine how the same non-Western material is partitioned across subject headings.
4. Test whether entry21's explicit discussion of India is indexed under `Buddhism` or only under broader religion/time categories.
5. Recover titles for graph targets 51,57,82,128 and 6–8,16 without altering already secure numbered edges.
6. Build Batch197 around the 19 / 21 / 243 boundary only after those controls are complete.

## Evidence rule added

> **A bibliographic cross-reference graph is itself a historiographical object. Formal `See` edges, annotation claims, introduction narratives, subject-index co-location, and later-secondary reception must remain separate relation types; otherwise the bibliography silently becomes a genealogy.**
