# UNIT × RELATION codebook v2 and seed-matrix recoding manifest

Date: 2026-08-31
Status: **CODEBOOK CORRECTION / DO NOT AGGREGATE SEED v0.1 UNTIL RECODED / ANALYTIC ONTOLOGY MADE EXPLICIT**

## Why this correction exists

The first seed matrix (`research_notes/unit_relation_matrix_seed_1898_2026_2026-08-31.tsv`, commit `93953c80...`) immediately exposed a category error in its own unit ontology.

The provisional code `U7` was used too broadly for things that are not the same historical unit:

- institutional relation;
- learned institution;
- debate;
- historiographical tradition;
- selector schema;
- comparative generalization;
- analytic type.

They share only the weak property `larger/more distributed than one author or proposition`.

That is precisely the kind of false aggregation this project is designed to prevent.

Therefore **do not calculate unit-frequency trends from seed v0.1 as currently coded**.

The mistake is analytically useful:

> **Unit typing is itself a historical/analytical claim. A codebook can reproduce the same relation-collapsing errors it is meant to diagnose.**

This correction is retained explicitly rather than silently overwritten.

---

# I. Revised UNIT ontology

## `U1 — SEMANTIC / PROPOSITIONAL UNIT`

Examples:

- technical term;
- proposition;
- doctrine fragment;
- word/concept;
- recurrent idea-pattern.

Typical risks:

`lexical identity != semantic identity`;
`propositional similarity != historical continuity`.

## `U2 — DOCUMENT / TEXTUAL-SEGMENT UNIT`

Examples:

- passage;
- page;
- dated entry;
- textual layer;
- diagram/schema as a document feature.

Typical risks:

`one dated entry != date of adjacent layer`;
`page adjacency != genetic sequence`.

## `U3 — AGENT / UTTERANCE UNIT`

Examples:

- author;
- speaker;
- source-recipient pair;
- intended linguistic act;
- complex work insofar as treated as an authored intervention.

Typical risks:

`contact != influence`;
`authorial intention != one unitary intention for whole work`.

## `U4 — PRACTICE / RITE / EVENT UNIT`

Examples:

- ritual;
- ceremonial act;
- social practice;
- ethnographic case;
- political practice.

Typical risks:

`outward similarity != common function/origin`;
`surviving form != surviving belief`.

## `U5 — SOURCE / WITNESS / RESEARCH-INFRASTRUCTURE UNIT`

Examples:

- bibliography;
- synthesis;
- lower-level witness;
- source collection;
- field map;
- reference infrastructure.

Typical risks:

`citation/use != doctrinal influence`;
`bibliographic dependence != theoretical dependence`.

## `U6 — TRADITION / CANON / REPRODUCED TEXTUAL FORMATION`

Examples:

- intellectual tradition;
- canonical textual tradition;
- regional history-of-thought tradition;
- portable anthology canon;
- reproduced practice-text complex.

Typical risks:

`tradition != one author`;
`canonization != historical priority`;
`reproduction != identical meaning`.

## `U7 — INSTITUTIONAL / COLLECTIVE ARENA UNIT`

Narrowed from seed v0.1.

Examples:

- learned institution;
- committee;
- journal/editorial field;
- classroom/workshop;
- debate considered as a multi-speaker arena;
- professional relation (teacher/pupil) when its institutional form matters.

Typical risks:

`institutional proximity != intellectual uptake`;
`venue publication != venue official position`;
`committee form != shared epistemic programme`.

## `U8 — TRACEABLE NETWORK / CHAIN UNIT`

Examples:

- mediated influence chain;
- correspondence network;
- translation/circulation route;
- interpretive succession where identifiable links can be traced.

Typical risks:

`possible route != demonstrated transmission`;
`network adjacency != causal chain`.

## `U9 — DISTRIBUTED FIELD / LARGE CORPUS UNIT`

Examples:

- climate of opinion;
- discursive field;
- large textual corpus;
- population-scale distribution;
- aggregate computational field.

Typical risks:

`aggregate pattern != individual causal mechanism`;
`frequency != meaning`;
`field availability != uptake`.

## `U10 — COMPOSITE MATERIAL / ARCHIVAL OBJECT UNIT`

Examples:

- accretive notebook;
- composite manuscript packet;
- archive assembled across material layers.

Typical risks:

`physical compositeness != chronological ordering`;
`collection identity != one production event`.

## `U11 — ANALYTIC CONSTRUCT / CLASSIFICATORY APPARATUS`

New in v2.

Examples:

- selector schema;
- analytic type;
- comparative generalization;
- historian-created classification;
- model or category used to group cases;
- field/problem map considered as an analytical construction rather than an institution/tradition.

Typical risks:

`analytical category != historical population`;
`type identity != chronological priority`;
`classification != causal explanation`;
`schema coherence != source-world coherence`.

This category is essential because Lovejoy/Marillier/Söderblom repeatedly **construct and revise units of comparison** rather than merely discover pre-given collective entities.

---

# II. Revised RELATION ontology remains provisionally stable

The first relation list survives the unit-code correction more successfully:

- `R1 SEMANTIC / CONCEPTUAL IDENTITY`
- `R2 CLASSIFICATORY INCLUSION`
- `R3 TEMPORAL SEQUENCE / PRIORITY`
- `R4 CAUSATION`
- `R5 TRANSMISSION / INFLUENCE / BORROWING`
- `R6 FUNCTION / MECHANISM`
- `R7 REPRESENTATIVENESS / DISTRIBUTION`
- `R8 SOURCE DERIVATION / PROVENANCE`
- `R9 CONTINUITY / SURVIVAL`
- `R10 RECEPTION / TRANSFORMATION / REPRODUCTION`.

One likely later refinement:

`R7 REPRESENTATIVENESS`
may need separation from
`DISTRIBUTIONAL FREQUENCY`,
particularly when the computational/census branch becomes quantitative.

Do not split yet until cases demand it.

---

# III. Seed-v0.1 recoding manifest

The following rows currently misuse provisional U7 and should be recoded before any aggregate calculation.

| case | v0.1 code | v2 correction |
|---|---|---|
| `LJ005_MORAL_BOUNDARY` | `U4 + U7_SELECTOR_SYSTEM` | `U4 + U11_SELECTOR_SYSTEM` |
| `LJ005_SELECTOR_SCHEMA` | `U7_SELECTOR_SYSTEM` | `U11_SELECTOR_SYSTEM` |
| `MARILLIER_MONOGRAPH` | `U4 + U7_COMPARATIVE_GENERALIZATION` | `U4 + U11_COMPARATIVE_GENERALIZATION` |
| `SODERBLOM_REDIVISION` | `U7_SHARED_PROBLEM_FIELD` | primarily `U11_ANALYTIC_REDIVISION`, with U6/U7 only if a tradition/workshop relation is separately being claimed |
| `LOVEJOY_PRIMITIVE_ENERGETICS` | `U7_ANALYTIC_TYPE` | `U11_ANALYTIC_TYPE` |
| `LOVEJOY_1914_TYPE_TIME` | `U7_ANALYTIC_TYPE` | `U11_ANALYTIC_TYPE` |
| `RICHTER_PROGRAMME` | `U7_METHOD_TRADITION` | `U6_METHOD_TRADITION` when discussing inherited methodological canon; `U7` only for institutional field |
| `KELLEY_NEW_IH` | `U7_FIELD_PROGRAMME + U6_CANON` | `U7_INSTITUTIONAL_FIELD + U6_CANON` — valid after semantic narrowing |
| `ARDAO_POSITIVISM` | `U6_TRADITION + U7_RECEPTION_FIELD` | usually `U6_REGIONAL_TRADITION`; add U7 only if institutional reception arena is evidenced |
| `CHING_CONFUCIAN` | `U6_TRADITION + U7_INTERNAL_SUCCESSION` | `U6_TRADITION + U8_TRACEABLE_SUCCESSION` if historical succession links are the object |
| `IQTIDAR_INTERPRETIVE_CHAIN` | `U7_CHAIN + U7_INSTITUTION` | `U8_INTERPRETIVE_CHAIN + U7_LEARNED_INSTITUTION` |
| `JENCO_HISTORICISM` | `U7_HISTORIOGRAPHICAL_TRADITION` | `U6_HISTORIOGRAPHICAL_TRADITION` |
| `BAJPAI_DEBATE` | `U7_DEBATE_AS_ENTITY` | retain `U7_COLLECTIVE_DEBATE_ARENA` |
| `CANON_BLAU` | `U6_METHOD_PLATFORM + U7_CONFERENCE_NETWORK` | retain: portable canon/platform U6 + conference arena U7 |

Also reconsider:

`LJ004_SYSTEM_MAPPING` currently codes `U2_SCHEMA`; if the claim concerns the **diagram as material source**, U2 is correct. If the claim concerns the **classification produced by the diagram**, add U11. One artifact can instantiate more than one unit depending on the proposition being tested.

This last point is crucial:

> **Unit type belongs to the claim, not permanently to the object.**

The same manuscript page can be U2 when dated/materially analyzed and U11 when treated as a classification.

---

# IV. No single unit ontology should be forced on a source

The codebook is intentionally multi-label.

A source can participate in several claims:

Example: notebook 005.

- as physical codex: `U10`;
- as individual dated entry: `U2`;
- as classification: `U11`;
- as ethnographic case collection: `U5`;
- as a window into a learned workshop: `U7` only when institutional linkage is separately established.

Example: Confucian classics in Tan.

- as transmitted canon: `U6`;
- as practiced way of life: `U4`;
- a particular passage may still be `U2`;
- a historically identifiable utterance inside the corpus could be `U3` if evidence permits.

Therefore the aim is not to discover the one true ontology of each historical object.

It is to prevent an inference licensed for one unit-construal from leaking into another.

---

# V. Codebook-level anti-leakage rule

Add to project governance:

> **UNIT-CONSTRUAL A ≠ UNIT-CONSTRUAL B. Evidence licensed under A cannot automatically migrate to B merely because both construals concern the same physical source or named tradition.**

Examples:

- p.44 date licenses U2-entry chronology, not U10-notebook chronology;
- teacher/pupil status licenses U7 institutional relation, not U3 doctrinal influence;
- anthology inclusion licenses U6 canonical portability, not historical representativeness of the whole debate;
- traditional reproduction licenses U6 continuity claims only after transformation is considered, not semantic identity of every layer.

---

# VI. Statistical prohibition until v2 recode

A private exploratory count of seed v0.1 immediately showed apparent chronological shifts in U7 frequency. That result is invalid because U7 itself was heterogeneous.

Therefore:

- do not publish or commit frequency claims from v0.1;
- do not write `early X -> later U7` from those counts;
- create a recoded v2 TSV before any period comparison;
- only then test whether admissible unit repertoires actually expand over time.

This is a useful methodological success, not a failed analysis: the matrix detected instability in its own categories before the instability was converted into a historical claim.

---

# VII. Next coding workflow

1. Recode the 40-row seed matrix under v2.
2. Add fields:
   - `unit_primary`;
   - `unit_secondary`;
   - `unit_construal_note`;
   - `relation_primary`;
   - `relation_secondary`.
3. Never encode more than two unit types unless the row is deliberately a comparison of construals.
4. Split one historical case into multiple rows when the proposition changes materially.
5. Add `claim_level`:
   - `OBJECT_LEVEL`;
   - `SOURCE_USE`;
   - `METHOD_PROGRAMME`;
   - `INSTITUTIONAL`;
   - `CANON_MEMORY`.
6. Only compare frequency within the same claim level unless the comparison itself is the research question.
7. Then augment the JHI 1940–75 execution census with unit coding.

---

## Governance shorthand

`UNIT TYPE != RELATION TYPE`.

`ANALYTIC CONSTRUCT != INSTITUTIONAL COLLECTIVE`.

`UNIT TYPE BELONGS TO THE CLAIM, NOT ONCE-FOR-ALL TO THE PHYSICAL OBJECT`.

`MULTI-LABEL != LICENSE TO CODE EVERYTHING AS EVERYTHING`.

`RECODE BEFORE COUNTING`.

## Restart shorthand

> **UNIT CODEBOOK v2: seed v0.1 exposed an overbroad U7. Split analyst-built schemas/types/generalizations into new `U11_ANALYTIC_CONSTRUCT`; reserve U7 for institutional/collective arenas; U8 for traceable networks/chains; U6 for traditions/canons. Critical insight: unit type belongs to the historical claim, not permanently to the named/physical object. Same notebook page can be U2 material segment and U11 classification under different propositions. Do not aggregate v0.1 frequencies. Recode matrix with primary/secondary unit and claim-level fields before adding unit types to the 40-case JHI census.**