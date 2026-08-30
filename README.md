# Arthur O. Lovejoy corpus

Research repository for Arthur O. Lovejoy's early Buddhist/Indian studies, comparative religion, political thought, philosophical practice, and the prehistory of his historical method.

**Current state:** base JHI evidence frozen; clean-submission v3.3 active; 1,878-word body and four publication-useful endnotes fixed; Word submission package generated and render-QA passed; image fallback closed; no research or argument blocker remains.

`CURRENT_STATE.md` is the single living project-state file. Historical `ACTIVE`, `HOLD`, `pending`, `next action`, `blocker`, or `missing` language elsewhere does not override it.

A pre-cleanup snapshot is preserved at `snapshot/pre-cleanup-2026-08-28`. The earlier pre-freeze snapshot remains at `snapshot/pre-freeze-2026-08-27` (base commit `249e8a29862d2daca84f1fbb6b698a2bf2fa6456`).

## Start here

Read in this order:

1. [`CURRENT_STATE.md`](CURRENT_STATE.md) — single living project and production state.
2. [`research_notes/JHI_blog_full_draft_v3_3_clean_submission_2026-08-29.md`](research_notes/JHI_blog_full_draft_v3_3_clean_submission_2026-08-29.md) — current clean-submission source.
3. [`research_notes/CANONICAL_INDEX_2026-08-28.md`](research_notes/CANONICAL_INDEX_2026-08-28.md) — current canonical evidence/navigation surface.
4. [`research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`](research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md) — publication-facing evidence ceilings.
5. [`research_notes/JHI_blog_v3_2_citation_hygiene_2026-08-29.md`](research_notes/JHI_blog_v3_2_citation_hygiene_2026-08-29.md) and [`research_notes/JHI_blog_image_caption_permission_plan_2026-08-29.md`](research_notes/JHI_blog_image_caption_permission_plan_2026-08-29.md) — current citation/image production controls.
6. [`research_notes/REPOSITORY_CLEANUP_2026-08-28.md`](research_notes/REPOSITORY_CLEANUP_2026-08-28.md) — structural-cleanup/governance manifest.
7. [`ARCHIVE_TRANSCRIPTION_PROGRESS.md`](ARCHIVE_TRANSCRIPTION_PROGRESS.md) — notebook transcription/material-audit status.

The earlier first-draft architecture files remain writing-history provenance, not the current submission source. Older dated indices, sync logs, HOLD files, batch notes and queue language are provenance unless `CURRENT_STATE.md` or the current canonical index explicitly routes to them.

## Current production boundary

The argument and paragraph architecture are frozen. The current clean-submission source has a 1,878-word body and four endnotes. A five-page Word package with true OOXML endnotes, working hyperlinks, preserved italics/diacritics, author/affiliation placeholders and a Figure 1 placeholder has been generated and visually checked.

Remaining production inputs are not research queues:

- preferred publication name;
- exact affiliation / short author bio;
- final image choice once JHU permission timing is known.

Preferred image: notebook 004, source PDF p.42 / manuscript p.123, subject to JHU publication permission. Fallback: the opening page of Lovejoy's 1898 JAOS article. Image choice does not block text submission.

## Core argument

The project does **not** argue that Buddhism caused Lovejoy's mature unit-idea method. It reconstructs a documented practice of moving among claims at different evidentiary resolutions.

Working model:

> **Shared problem/category field → local redivision/reweighting → relation-specific judgment → internally stratified historical object → transverse comparison → possible broader reaggregation.**

Governing evidentiary rule:

> **A stronger proposition does not automatically inherit evidence that established a weaker proposition.**

The central historical question is what kinds of warrant allowed Lovejoy to move among textual, semantic, logical, chronological, causal, psychological and historical relations without assuming those relations were interchangeable.

## Archive center

Notebooks 004 and 005 remain the archival center.

- 004 corrected text: **71/71 pages**
- 005 corrected text: **120/120 pages**
- combined material-form overview: **191/191 pages**
- authoritative corrected text: `archive_transcriptions/*_clean.json`
- material ledger: `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`
- closure: `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`

Highest-value material control remains 004 PDF p.42 / manuscript p.123: `viññāṇa` is spatially nested within `nāma`/`nāmarūpa` while adjacent prose treats it as temporally antecedent to `nāmarūpa` and logically a subdivision. Different relation-types are materially held apart on one page.

## 2026-08-28 logical-analysis control

The reopening historicalized the analytical vocabulary used to describe Lovejoy. Its final result is a calibration, not a new Blog section.

Controlled model:

> **Lovejoy used different analytical operations in different contexts. `Logical` did not have one stable local meaning; the stronger recurring candidate is typed relations + inferential jurisdiction rather than one transported formal-logical technique.**

Mandatory adversarial warning:

> **A ≠ B does not establish that A is historically or functionally independent of B.**

Lovejoy's distinctions sometimes need checking for overpartition, scope widening, or loss of the target actor's bridge between two non-identical relations.

The Carnap comparison is frozen as a field/adversarial control. It is not an active Blog branch.

## Repository layers

### Living navigation / production

- `CURRENT_STATE.md`
- `research_notes/JHI_blog_full_draft_v3_3_clean_submission_2026-08-29.md`
- `research_notes/CANONICAL_INDEX_2026-08-28.md`
- `WORKING_RULES.md`

### Primary/source and provenance

- `archive_transcriptions/` — raw/corrected/clean text, edit logs, diagnostics and material audits.
- `archive_index/` — archive/source coverage, locators, search and provenance infrastructure.
- root OCR/metadata/export payloads — legacy source/derived payloads intentionally retained at their existing paths to avoid breaking references.

The root payload layout is recorded structural debt, not an active cleanup queue. Any future migration into `sources/`, `ocr/`, `data/` or `exports/` must be a dedicated path-breaking migration with an explicit path map.

### Canonical analytical layer

Defined by the current canonical index. Terminal source-specific dossiers remain under `research_notes/`.

### Process provenance

Historical batch matrices, web sweeps, HOLD/gap audits, old sync logs and exploratory notes remain searchable where they preserve provenance. Their embedded historical state words are not executable instructions.

Git history is also the process archive; genuinely superseded navigation/process files may be removed only after terminal conclusions and required references are preserved.

## Evidence discipline

Do not infer:

- citation = assent;
- adjacency = uptake;
- teacher relation = total method transmission;
- curricular availability = exact enrollment;
- thematic similarity = textual reading;
- relation non-identity = historical independence;
- decomposition = uniquely Lovejoyian method;
- page order/ink/hand alone = composition chronology;
- mature Western narrative center = disappearance of Buddhism;
- known Buddhist formation = historiographical development of its technical scholarly content.

## Reopening rule

Reopen frozen research only if:

1. a newly digitized/direct primary bears directly on a live proposition;
2. a direct source contradicts the current evidence state;
3. publication editing requires exact facsimile/page/quotation verification; or
4. an analytical category already used in the draft requires materially different actor-level historical reconstruction.

Otherwise continue submission production, compression and citation placement rather than research expansion.
