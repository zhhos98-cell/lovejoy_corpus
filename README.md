# Arthur O. Lovejoy corpus

Research archive for Arthur O. Lovejoy's early Buddhist and Indian studies, comparative religion, political thought, philosophical practice, and the prehistory of his historical method.

**Current state (2026-09-01):** the JHI Blog text is at v3.4 (1,880 body words; four endnotes) and remains on production hold; notebook 004 has 71/71 first-pass coverage plus a conceptually closed targeted original-image second pass; notebook 005 has 120/120 first-pass coverage plus targeted original-image rechecks through Round 20, but not a complete diplomatic second pass. The AOS 1897 presentation, election, and publication-path questions now have direct-primary closure at the stated evidence ceilings.

`CURRENT_STATE.md` is the only authority for whether a branch is active, held, frozen, or complete. Historical state language elsewhere is process provenance.

## Start here

1. [`CURRENT_STATE.md`](CURRENT_STATE.md) — compact living state and exact restart points.
2. [`CANONICAL_INDEX.md`](CANONICAL_INDEX.md) — stable navigation surface for current evidence.
3. [`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`](archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md) — integrated human-readable transcription, 004 pp.1–71 followed by 005 pp.1–120.
4. [`ARCHIVE_TRANSCRIPTION_PROGRESS.md`](ARCHIVE_TRANSCRIPTION_PROGRESS.md) — notebook coverage, authority, and remaining limits.
5. [`QUELLENFORSCHUNG_CURRENT_GATE.md`](QUELLENFORSCHUNG_CURRENT_GATE.md) — governing source-critical protocol.
6. [`WORKING_RULES.md`](WORKING_RULES.md) — repository and evidence-governance rules.

The dated `research_notes/CANONICAL_INDEX_2026-08-28.md` and earlier state files are historical snapshots. They no longer route current work.

## Current research boundary

The project does **not** argue that Buddhism caused Lovejoy's mature unit-idea method. It reconstructs a documented practice of moving among claims at different evidentiary resolutions.

Working model:

> **Shared problem/category field -> local redivision or reweighting -> relation-specific judgment -> internally stratified historical object -> transverse comparison -> possible broader reaggregation.**

Governing evidentiary rule:

> **A stronger proposition does not automatically inherit evidence that established a weaker proposition.**

Recurring firewalls include:

- citation does not establish assent;
- adjacency does not establish uptake;
- curriculum or teacher relation does not establish total method transmission;
- relation non-identity does not establish historical independence;
- material page order, ink, or hand alone does not establish composition chronology;
- a first-pass argument summary is not automatically diplomatic manuscript wording;
- a named ritual form does not determine one causal mechanism;
- corporate AOS membership is distinct from membership in the Historical Study of Religions Section.

## Archive center

Notebooks 004 and 005 remain the archival center.

- 004: 71/71 first-pass pages; targeted original-image second pass conceptually closed; micro-paleographic residue remains.
- 005: 120/120 first-pass pages; broad targeted original-image rechecks completed through Round 20; no claim of full second-pass closure.
- Combined material-form overview: 191/191 pages.
- Human-readable final reading surface: `archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`.
- Authoritative corrected text: the twelve paginated `archive_transcriptions/MS38_004_001_061_{004,005}_p*_clean.json` files.
- Machine-readable direct-image audit trails: the Round-17 and Round-18 delta JSON files in `archive_transcriptions/`.

The highest-value material control remains notebook 004, PDF p.42 / manuscript p.123. `viññāṇa` is spatially nested under `nāma/nāmarūpa`, while adjacent prose treats it as temporally antecedent and logically a subdivision. The page holds distinct relation types apart without licensing an origin story about the later unit-idea method.

## Repository layers

| Layer | Authority / purpose |
|---|---|
| Living state | `CURRENT_STATE.md` |
| Current navigation | `CANONICAL_INDEX.md` |
| Source-critical policy | `QUELLENFORSCHUNG_CURRENT_GATE.md` |
| Human-readable notebook edition | `archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md` |
| Machine-readable notebook authority | paginated `archive_transcriptions/*_clean.json` batches |
| Audit and provenance | delta JSON/CSV, material manifest, `archive_index/`, terminal dossiers |
| Historical process | dated batches, sweeps, old state deltas, queues, and superseded notes in Git history |
| Legacy payloads | root OCR, metadata, source exports, and source texts retained at stable paths |

The root payload layout is known structural debt. Moving large OCR/source files would break many historical references, so any migration to `sources/`, `ocr/`, `data/`, or `exports/` must be a separately mapped path migration.

## JHI production state

The active text is `research_notes/JHI_blog_full_draft_v3_4_clean_submission_2026-08-31.md` (1,880 body words; four endnotes). The latest generated DOCX remains v3.3 until v3.4 is regenerated and render-QA'd. Text production awaits user/editor inputs rather than further research: publication name, affiliation/short bio, and final image choice.

Preferred image: notebook 004 PDF p.42 / manuscript p.123, subject to JHU publication permission. Fallback: the public-domain opening page of Lovejoy's 1898 JAOS article.

## Validation

Run:

```bash
python tools/audit_repository.py
```

The audit checks the required navigation surface, parses every tracked JSON file, validates the twelve canonical clean-transcription batches, verifies that the integrated 191-page edition exactly matches them, and reports Markdown links to missing local files.

## Reopening rule

Reopen a frozen research line only if direct new primary evidence changes a live proposition, a direct source contradicts the current state, publication editing requires exact facsimile/page/quotation verification, or an analytical category already in use requires materially different actor-level reconstruction. Otherwise, continue the stated production or archival queue rather than following stale `ACTIVE`, `HOLD`, `missing`, or `next action` language in historical notes.
