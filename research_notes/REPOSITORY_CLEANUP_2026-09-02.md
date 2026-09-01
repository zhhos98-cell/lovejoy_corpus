# Repository cleanup — 2026-09-02

## Purpose

Correct a state-model error in the Lovejoy repository: page coverage and proposition-sensitive original-image control had become too easy to read as manuscript transcription completion.

The cleanup does not alter canonical manuscript wording. It changes routing, status language, and completion criteria.

## Main correction

Before this cleanup, the repository accurately stated that 005 lacked full second-pass closure, but the navigation surface still used phrases such as `191/191`, `integrated ... final`, and `conceptually closed` in ways that could encourage a later reader or automated process to overread coverage as completion.

The governing distinction is now:

`PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION`.

Current state:

- 004: 71/71 first-pass coverage; targeted argument-control second pass conceptually closed; full diplomatic edition incomplete.
- 005: 120/120 first-pass coverage; targeted original-image rechecks through Round 20; diplomatic transcription active and incomplete.
- 191/191: material/page-record coverage only.

## New living file

Created:

`TRANSCRIPTION_COMPLETION_QUEUE.md`

It defines:

- page coverage;
- first-pass text coverage;
- targeted original-image control;
- diplomatic page completion;
- diplomatic notebook completion.

It also sets the current restart order:

1. 005 pp.31–36;
2. 005 pp.42–43;
3. 005 pp.47–60;
4. remaining 005 blocks page by page;
5. 004 residual diplomatic work only when a complete manuscript edition becomes the goal.

## Evidence for reopening transcription

The 005 p.31–45 canonical batch still contains low/low-medium pages whose records explicitly state that multiple lines, proper names, references, or geographic wording remain illegible or only partly transcribed. pp.42–43 also retain partial Greek lexical/textual slips.

`research_notes/MS38_005_round20_p016-030_contact_sociality_marillier_insert_recheck_2026-09-01.md` explicitly hands off the systematic sweep to pp.47–60.

Therefore the earlier completion boundary was a research-argument boundary, not a manuscript-edition boundary.

## Living files updated

- `README.md`
- `CURRENT_STATE.md`
- `CANONICAL_INDEX.md`
- `ARCHIVE_TRANSCRIPTION_PROGRESS.md`
- `tools/audit_repository.py`

The audit now requires `TRANSCRIPTION_COMPLETION_QUEUE.md` and labels 71/71 + 120/120 as canonical page coverage rather than transcription completion.

## Stable integrated path

The existing path:

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`

is retained because many repository references depend on it. The word `final` is treated as legacy filename provenance, not as a diplomatic-completion claim. A genuinely complete future diplomatic edition should receive a new explicit version rather than silently redefining the old path.

## Superseded AOS note removed

Removed:

`research_notes/AOS_1897_Lovejoy_membership_and_history_of_religions_section_boundary_2026-09-01.md`

Reason: it was added after the stronger terminal dossier but retained weaker state language (`section relation OPEN` and unresolved read/election questions). The current authority remains:

`research_notes/AOS_1897_Lovejoy_election_read_by_title_and_technical_terms_precursor_2026-09-01.md`

Git history preserves the deleted intermediate note.

## Result

The repository now has two independent closure models:

1. **research proposition closure**, governed by `CURRENT_STATE.md` and source-critical dossiers;
2. **manuscript transcription completion**, governed by `TRANSCRIPTION_COMPLETION_QUEUE.md`.

This prevents a conceptually closed argument from prematurely closing an archival transcription task.
