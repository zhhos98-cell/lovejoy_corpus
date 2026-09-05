# AGENTS.md — Lovejoy Article Research, Writing, and Editing Protocol

This file is the persistent instruction set for ChatGPT, Codex, and other agents working in this repository. Read it before any article edit or research expansion. It records the user's established workflow and should prevent future sessions from regenerating, flattening, over-defending, or re-theorizing the project. Do not rewrite or shorten this file unless the user explicitly asks.

## 1. Canonical article and version control

The canonical prose draft is:

`research_notes/JHI_blog_full_draft_v3_7_clean_submission_2026-09-03.md`

Rules:

- **Never create a successor JHI prose draft merely because a new pass begins.**
- All substantive prose edits patch the canonical draft directly unless the user explicitly requests a submission snapshot, export, or archival freeze.
- `research_notes/JHI_blog_v3_7_notebook_guide_quellenkritik_calibration_2026-09-03.md` is a calibration/control document, not an independent prose draft.
- Earlier and exploratory drafts are provenance unless `CURRENT_STATE.md` or `CANONICAL_INDEX.md` explicitly promotes them.
- Before every write, fetch the current blob/file SHA. Sequential edits to the same file must use the latest returned SHA.
- Report the exact path, commit SHA, and the historical/conceptual effect of each meaningful edit.

## 2. Editing method: surgical patch, never regeneration

- **Edit by surgical patch, not regeneration.** Intellectual diff must stay local even if the API technically transmits the whole file.
- Preserve surrounding prose verbatim unless a specific local restructuring is necessary.
- Do not rewrite a paragraph or section merely for flow, completeness, elegance, tone, balance, symmetry, smoother transitions, or because a new idea could be made more self-contained.
- User annotations are local instructions. Fix the annotated place; do not use a comment as permission to rewrite its neighborhood.
- Do not let model completion automatically add explanatory closure, roadmap sentences, paragraph-end verdicts, balanced mini-essays, or defensive qualifications.
- Do not compress controlled historical sequences into abstract summary merely to make the article shorter or smoother. If an event has several relevant actions, let those actions happen in the prose.
- Growth should come from evidence, textual work, chronology, and intellectual history, not generic exposition.

Working maxim:

> The event must finish happening; it does not have to be explained to exhaustion.

Or, in the user's formulation: **不是事情一定要解释完，而是事情得发生完。**

## 3. Revise by local reading, not remote redesign

Begin from the paragraph as it currently exists.

For each passage:

1. ask what historical or historiographical burden it already carries;
2. inspect only the immediately relevant source/control;
3. add, subtract, or replace only the sentence or short passage needed there;
4. preserve the surrounding prose unless the local logic genuinely breaks;
5. let larger structure emerge cumulatively from these local readings.

Do not revise a distant section from an abstract architecture held in the model's head. Do not regenerate surrounding prose merely to make a new idea feel complete.

## 4. Source lock and evidentiary levels

Factual expansion is source-locked to controlled material.

A restored date, place, person, action, quotation, title, correspondence sequence, archival object, source attribution, or causal link must come from one of the following:

1. the canonical draft or controlled earlier draft state;
2. canonical notebook transcriptions, terminal syntheses, evidence maps, archive controls, research notes, or primary-source witnesses in this repository;
3. newly verified external research that has first been recorded in a bounded repo research/control note.

Never fill a historical gap from model memory, general knowledge, plausibility, or stylistic completion.

Use three evidence levels:

- **BODY / SECURE** — directly controlled enough to carry narrative or argument;
- **NOTE / PARTIAL** — relation, object, or locator is secure but wording/content/date/mechanism is incomplete; use with exact qualification;
- **QUARANTINE / UNCONTROLLED** — interesting lead whose identity, context, wording, or carrier is not secure; do not narrativize.

When two sources conflict, preserve the discrepancy. Do not silently normalize dates, titles, page numbers, archival labels, source ownership, or identities.

Critical rule:

> **PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION.**

Likewise:

> **NOTEBOOK HANDWRITING != PROPOSITION AUTHORSHIP.**

and:

> **FAILED SOURCE RECOVERY != LOVEJOY ORIGINALITY.**

## 5. External research is bounded and currently secondary

Generic retrieval is closed for the present short-form article.

Open new external research only when the canonical draft exposes a specific factual or conceptual gap that could materially change a sentence, note, attribution, quotation, or event chain.

For external research:

1. identify the bounded gap;
2. search only that gap;
3. verify the source and evidentiary level;
4. record the result in a repo control/delta;
5. only then patch the canonical draft.

Do not reopen notebook-wide, actor-wide, or institution-wide discovery merely because further material may exist.

The current non-journal article is **argument-ready**. Request-ready or slow archival routes are future upgrades, not prerequisites.

## 6. The article's conceptual center is Lovejoy's Buddhism problem

The article must remain centered on a concrete historical problem visible in Lovejoy's late-1890s Buddhist work:

> How could doctrines described by philologists be reconstructed philosophically without allowing philosophical reconstruction to outrun the texts?

The strongest local answer is not a claim that Lovejoy already possessed a mature later method. It is that, in solving specific Buddhist problems, he repeatedly separated relations that could not safely answer for one another.

Current compact control:

> **One relation is not allowed automatically to answer for another.**

The historically important distinctions include, where directly supported:

- temporal sequence;
- logical inclusion or subdivision;
- causal function;
- classification;
- semantic equivalence;
- resemblance;
- genealogy or historical derivation;
- historical stratum.

The article should show these distinctions happening in texts, notebook pages, source disputes, and publication choices. Do not turn the compact control into a slogan repeated through the prose.

## 7. Do not write the mature Lovejoy backward

The project is not a precursor hunt for *The Great Chain of Being* or the mature unit-idea method.

Do not write:

`1890s notebooks -> mature history-of-ideas method`

as a teleology.

Later Lovejoy may be used only when a later text clarifies a bounded continuity, exit, reaggregation, or change of scale already visible in the earlier evidence.

The article may say that the 1890s work reveals local analytical practices. It may not claim that the mature method was already present unless direct evidence warrants that proposition.

## 8. Notebook 004 is the primary analytical core

For the current article, notebook 004 is the strongest manuscript center.

Use it to reconstruct concrete operations:

- comparison of texts;
- testing of Warren, Senart, Oldenberg, Rhys Davids, Childers, and related witnesses where source ownership is controlled;
- separation of temporal, logical, causal, semantic, classificatory, and genealogical questions;
- narrowing of claims to the burden of a particular paper;
- selective omission of worksheets, chronology branches, and broader allocations when moving toward print.

Do not convert every notebook distinction into a general theory of method.

Do not treat the notebook as a transparent draft of the 1897 communication or the 1898 article. Notebook, announced communication, meeting handling, printed Proceedings carrier, and published article are distinct documentary states.

## 9. Notebook 005 is supporting evidence, not a second article

Notebook 005 has 120/120 first-pass coverage and remains useful for showing that Lovejoy could separate chronology, classification, mechanism, source authority, historical layer, and developmental language in comparative-religion materials.

But for the present short-form article:

- 005 is subordinate to the Buddhist/004 center;
- do not reopen broad 005 source hunting;
- do not build a parallel article on sacrifice, fetish, magic, afterlife, agrarian rites, or comparative religion;
- use only passages that sharpen the central problem already established through 004 and the 1898 article;
- unresolved diplomatic/source-version HOLDs remain non-blocking unless a final sentence quotes them directly.

The physically and chronologically composite nature of 005 must remain visible. Later reuse does not automatically date adjacent leaves.

## 10. `primitive`, developmental language, politics, and 1902–1906 are exits, not the center

The article currently contains later material on `primitive`, developmental ranking, 1902, 1906, and *The Great Chain of Being*.

These materials may remain only when they clarify what became of distinctions already visible in the 1890s.

Rules:

- `primitive` must not become a second conceptual center;
- the Brinton–Boas–Lovejoy comparative triangle remains frozen and excluded from production;
- 1902 and 1906 are scale/reaggregation controls, not retrospective master keys;
- political and civilizational hierarchy must remain visible where the article invokes developmental language;
- do not imply that relation-separation made Lovejoy anti-evolutionary, anti-hierarchical, or politically innocent.

A useful control is coexistence:

> analytical differentiation and ranked developmental language can occupy the same corpus.

Do not force one to cancel the other.

## 11. Formation evidence: preserve the philologist/philosopher jurisdiction problem

The 1898–99 Paris correspondence is important because Lovejoy explicitly described the gap the article reconstructs: philologists could handle textual technicalities while philosophers could reconstruct systems too freely.

Use this evidence carefully:

- the present witness is Daniel J. Wilson's archival transcription, not autograph-level verification;
- Lovejoy's October–December 1898 statements can support actor-level framing of the problem;
- they do not prove one teacher, one influence genealogy, or one already-complete method;
- course availability, enrollment, grades, private reading, teacher contact, and methodological transmission remain separate propositions.

Formation should support the article's problem, not become a separate institutional biography.

## 12. 1897 publication genesis is a control, not a required archival mystery

Keep the known documentary states distinct:

`10 Apr 1897 Final Circular — Critical summary of the argument of the Milinda-pañha`

→ `22–24 Apr Baltimore meeting — Lovejoy No. 30 later recorded among papers read by title; exact meeting title and Lovejoy-specific brief statement unresolved`

→ `June 1897 printed Proceedings carrier — technical-term title state`

→ `1898 published JAOS article — upādāna / upādisesa`.

Current direct visual control places Lovejoy No. 30 on **printed p. 389**, not p. 380. The printed title gives the first term in the form **upādānam** and the second as **upādāna-kkhandhā**. Treat normalized discussion forms separately from diplomatic transcription.

Firewalls:

- **MEETING DATE != AUTOMATIC DATE OF A TITLE FOUND ONLY IN THE LATER PRINTED PROCEEDINGS.**
- **TITLE CONTINUITY != MANUSCRIPT IDENTITY.**
- **READ BY TITLE != BARE TITLE ONLY.**
- **GROUP-LEVEL `WITH OR WITHOUT A BRIEF STATEMENT` != LOVEJOY-SPECIFIC BRIEF STATEMENT.**

For the present article, the mechanism of the 10 April -> June title/object transition may remain unknown. Do not make the article wait for archival recovery of that mechanism. A short sentence or note is sufficient unless the user explicitly chooses to make publication genesis central.

## 13. Counterevidence and awkward facts must stay

Do not turn the article into a triumphal story of Lovejoy naturally discovering methodological pluralism.

Preserve, where relevant:

1. Lovejoy's use of ranked developmental language such as `higher stage of culture` and `primitive peoples`;
2. the fact that internal stratification does not erase civilizational hierarchy;
3. the 1898 article's unresolved contrary passages and refusal to claim final settlement on *upādisesa*;
4. evidence that resemblance, classification, genealogy, chronology, and causal explanation are sometimes left open rather than resolved;
5. uncertainty over source ownership or diplomatic wording where the manuscript or witness does not permit stronger claims;
6. the distinction between a useful local analytical practice and a fully articulated general method.

Counterevidence should survive a prose-cleaning pass. Synthetic defensive scaffolding should not.

## 14. Chronology and event-chain rules

Read every paragraph for temporal orientation.

Use time anchors when they prevent genuine confusion:

- Harvard 1896–97 training;
- spring 1897 AOS title/publication states;
- 1898 publication;
- Paris 1898–99 correspondence;
- later reuse of notebook 005;
- 1902/1906 exits.

Preferred reconstruction:

`date/place/action → document/text → response/problem → consequence`.

Do not calculate every interval mechanically.

Do not summarize a dense sequence as `Lovejoy's interests developed` when the repository controls a more precise chain.

## 15. Facts, materials, historiography, inference

Keep four voices distinguishable:

1. **fact/event** — who did what, when;
2. **material/source** — what a notebook, article, circular, correspondence witness, scan, or archival object shows;
3. **historiography** — what secondary scholarship has argued;
4. **article inference** — what this article concludes from the material.

Do not turn these into visible `[FACT] / [SOURCE] / [METHOD]` labels in finished prose.

A reader should be able to disagree with the source reading, historiographical relation, or inference separately.

## 16. Historiography must be layered by patch

Every secondary source in the body must have a job:

`inherit / correct / refute / converge / narrow / redirect / expose a gap`.

Do not add a standalone literature-review block merely to make the article look more historiographical.

Preferred operation:

> An earlier historian makes X visible; the present primary evidence confirms, narrows, redirects, or complicates X at a specific point.

A secondary source belongs in the body only when the case does something with its proposition. Otherwise use a note or omit it.

Do not use secondary literature to substitute for primary reconstruction when controlled primary material exists.

## 17. Prose style and defensive temperature

Finished prose should sound like historical scholarship, not an agent explaining its own reasoning.

Avoid:

- workbench labels and invented technical vocabulary unless precision genuinely requires them;
- repeated `relation-separation`, `reaggregation`, `scale contraction`, `proof-burden separation`, `carrier state`, `source ownership`, or similar repo terms in public prose when ordinary historical language will do;
- slogans invented during drafting;
- repeated `this does not mean`, `rather`, `not X but Y`, and pre-emptive qualifications;
- symmetrical counterargument paragraphs added merely for balance;
- roadmap sentences and paragraph-end verdicts;
- excessive proper-name density;
- one-sentence paragraphs created only to mark analytical layers.

Use technical language only when the word earns its precision.

Paragraphs should usually let one historical or intellectual action unfold. Merge adjacent short paragraphs when they perform the same action; do not merge distinct events merely to increase paragraph length.

Name-density rule: keep a proper name in the body only when the actor, author, or source attribution itself carries argumentative work. Otherwise prefer the text, problem, role, institution, or note citation.

## 18. Notes

Notes can carry:

- concise background a reader may lack;
- chronology and provenance;
- archive/source locators;
- translation or normalization choices;
- uncertainty and source-status explanations;
- later or comparative material that is secure but not central enough for the body.

Do not bury the main conceptual step in a note.

Do not let notes become defensive mini-essays.

For Pāli and Sanskrit forms, distinguish diplomatic printed/manuscript form from normalized discussion form when the distinction matters.

## 19. How to grow or strengthen the article

Do not solve weakness by whole-draft regeneration or abstract explanation.

Strengthen through:

- close reading of a controlled notebook passage;
- a completed source dispute;
- movement from notebook problem to published argument;
- a clear distinction between two relations Lovejoy himself had to adjudicate;
- an event chain that explains why a document appears when it does;
- a historiographical disagreement that actually changes the reading of the case;
- a counterexample that prevents the article from becoming teleological.

If a draft pass makes prose smoother while reducing source density, source specificity, or historical sequence, it is probably the wrong pass.

## 20. Round-by-round calibration protocol

Do not run every pass as a fresh full-repo redesign. Keep the canonical draft at the center and use one calibration question per round.

Recommended order:

### Round 0 — factual hygiene

Correct verified factual, bibliographic, page-number, title, carrier, and diplomatic errors. Close stale HOLD language when direct evidence now resolves it. Do not alter argument structure.

### Round 1 — chronology and event chains

Ask whether each event finishes happening and whether the reader knows who acted, when, through what document/text, and with what consequence. Add only missing anchors.

### Round 2 — sentence-level source control

Test each factual sentence for witness, evidence level, source ownership, and verb strength. Lower claims that outrun the witness; do not inflate partial evidence.

### Round 3 — conceptual center

Ask whether every paragraph serves Lovejoy's Buddhism problem. Compress or remove material that opens a parallel article on `primitive`, politics, later Lovejoy, comparative religion, or institutional biography without sharpening the central problem.

### Round 4 — historiography

Give every secondary source a specific function. Remove citation density that does not alter the case.

### Round 5 — prose temperature

Remove synthetic defensive scaffolding, repeated slogans, agent vocabulary, roadmap sentences, and unnecessary verdicts while preserving genuine uncertainty and counterevidence.

### Round 6 — notes and diplomatic cleanup

Clean locators, page references, Pāli/Sanskrit forms, normalization notes, and remaining quotation-level diplomatic issues actually used in the article.

### Round 7 — final counter-test

For every paragraph ask: if this paragraph disappeared, what historical, evidentiary, conceptual, or historiographical work would be lost? If the answer is only `completeness`, `context`, or `showing how much research exists`, compress or remove it.

Each round should produce a bounded local diff and stop when its own question is exhausted.

## 21. Current publication QA and stop rules

For the present short-form article:

- notebook 004 broad argument-level work is closed;
- notebook 005 broad source work is closed;
- the 1897 AOS online-discovery phase is closed at its present public ceiling;
- slow JHU/Yale/AOS archival follow-up is non-blocking;
- autograph-level verification of Wilson's 1898–99 transcription is optional unless exact quotation or paleographic argument requires it;
- 1902–06 expansion and the Brinton–Boas–Lovejoy comparative branch must not be reopened by default;
- publication-genesis mechanics between 10 April and the June 1897 carrier may remain unresolved.

Current factual hygiene priority before prose calibration: eliminate stale `p.380` references to Lovejoy No. 30 and stale language treating the exact p. 389 Pāli typography as unresolved.

## 22. Final pre-write checklist

Before committing an edit, ask:

1. Is every new fact source-controlled?
2. Did the historical event actually finish happening?
3. Is the reader temporally oriented?
4. Is Lovejoy's Buddhism problem still the conceptual center?
5. Did a supporting concept accidentally become a parallel article?
6. Did notebook evidence remain distinct from publication/manuscript identity claims?
7. Are April meeting handling and June printed carrier still kept distinct?
8. Are counterevidence, hierarchy, uncertainty, and awkward facts still visible?
9. Did I add defensive prose, a slogan, or invented jargon?
10. Did I regenerate more than the local problem required?
11. Did the draft grow or change through historical/intellectual substance rather than explanation for its own sake?
12. Did I fetch the current SHA before writing?
13. Can I report exactly what changed and why?
