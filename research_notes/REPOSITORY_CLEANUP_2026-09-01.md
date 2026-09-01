# Lovejoy corpus — repository cleanup manifest

Date: 2026-09-01
Status: **COMPLETE NAVIGATION/STATE CONSOLIDATION / CONSERVATIVE EVIDENCE PRESERVATION**

## 1. Scope and finding

This pass treated the repository as a research archive. The evidence layer was not the main problem: the twelve clean notebook batches, audit deltas, material manifest, archive indexes, and terminal dossiers were internally valuable and had no exact-content duplicates. The problem was authority drift:

- `README.md` still described the 2026-08-29 v3.3 production state;
- `CURRENT_STATE.md` stopped at 2026-08-31 while eight later root-level state deltas carried 2026-09-01 results;
- the dated canonical index still pointed to nonexistent aggregate `MS38_004_clean.json` and `MS38_005_clean.json` files;
- `ARCHIVE_TRANSCRIPTION_PROGRESS.md` and `QUELLENFORSCHUNG_CURRENT_GATE.md` stopped at Round 17 although original-image work had reached Rounds 18–20;
- two late membership-only AOS notes reintroduced unresolved presentation/election language after a stronger direct-proceedings dossier had already closed those questions;
- the repository had no repeatable integrity check for current navigation, JSON validity, canonical page coverage, or local Markdown links.

The cleanup therefore consolidated current authority and removed superseded navigation/process residue. It did not rearrange raw sources or rewrite historical analytical dossiers.

## 2. New current navigation

Created:

- root `CANONICAL_INDEX.md` as the stable, undated routing surface;
- `tools/audit_repository.py` as a read-only integrity audit;
- this manifest.

Rewritten and synchronized:

- `README.md`;
- `CURRENT_STATE.md`;
- `ARCHIVE_TRANSCRIPTION_PROGRESS.md`;
- `QUELLENFORSCHUNG_CURRENT_GATE.md`;
- `WORKING_RULES.md`.

The dated `research_notes/CANONICAL_INDEX_2026-08-28.md` is retained but explicitly marked as a historical snapshot.

Current authority order:

`CURRENT_STATE.md`
-> `CANONICAL_INDEX.md`
-> source-critical/progress gate
-> current paginated clean batch
-> terminal dossier and audit trail
-> historical process provenance.

## 3. Consolidated state

### JHI production

- active source: v3.4;
- 1,880 body words and four endnotes;
- generated DOCX still v3.3 pending deliberate regeneration and render QA;
- production hold is user/editor-facing, not a research blocker.

### Notebook 004

- 71/71 first-pass coverage;
- targeted original-image second pass conceptually closed;
- p.17/p.29 residual argument-bearing queue closed;
- pp.49–52 conceptual blind queue closed;
- micro-paleographic and foreign-language residue remains, so the corpus is not represented as a full diplomatic edition.

### Notebook 005

- 120/120 first-pass coverage;
- broad targeted original-image rechecks through Round 20;
- current corrections include source-evaluation criteria, mechanism/performer distinctions, Marillier insert separation, and directionality repairs;
- no claim of full second-pass closure.

### AOS/Milinda

- Lovejoy's absence, paper read by title, corporate election, and the Section-membership firewall are directly closed by the proceedings dossier;
- the technical-terms communication is a strong publication-path precursor to the 1898 JAOS article;
- manuscript identity/version continuity remains held;
- MS97=`Up.`, Hardy p.394, and published Milinda p.32 (not p.33) are the current corrected witness architecture.

## 4. Files removed from the working tree

Eight root-level state deltas were removed after their state-bearing conclusions and terminal routing were merged into `CURRENT_STATE.md`, `CANONICAL_INDEX.md`, the progress/gate files, and this manifest:

- `CURRENT_STATE_DELTA_2026-08-31_HARVARD.md`
- `CURRENT_STATE_DELTA_2026-08-31_HARVARD_LOCAL_NETWORK.md`
- `CURRENT_STATE_DELTA_2026-09-01_AOS1897.md`
- `CURRENT_STATE_DELTA_2026-09-01_AOS1897_PUBLICATION_SELECTION.md`
- `CURRENT_STATE_DELTA_2026-09-01_MILINDA_NOTEBOOK_RETENTION.md`
- `CURRENT_STATE_DELTA_2026-09-01_ROUND17_WITNESS.md`
- `CURRENT_STATE_DELTA_2026-09-01_ROUND17B_004_RELATION.md`
- `CURRENT_STATE_DELTA_2026-09-01_ROUND17C_004_PAGEFORM_MERGE.md`

Three weaker or supersession-only AOS process notes were removed after the stronger direct-proceedings dossier was made authoritative:

- `research_notes/AOS_1897_Lovejoy_membership_Milinda_and_History_of_Religions_section_2026-09-01.md`
- `research_notes/AOS_1897_membership_History_of_Religions_Section_and_Lovejoy_status_2026-09-01.md`
- `research_notes/AOS_1897_Lovejoy_membership_and_history_of_religions_section_infrastructure_2026-09-01.md`

Their historical content remains recoverable in Git. None was a raw source, transcription, machine-readable audit record, or unique terminal dossier.

## 5. Files intentionally preserved

- all twelve authoritative paginated clean-transcription JSON batches;
- Round-17 and Round-18 machine-readable delta registers;
- the 191-page material audit manifest;
- all archive indexes and source/custody/provenance tables;
- terminal analytical dossiers;
- root OCR, metadata, source-text, and export payloads at their existing paths;
- the broader Unit×Relation v0.7 comparative-control layer.

No source payload was moved merely for aesthetic consistency. Existing path references are numerous, so a future `sources/ocr/data/exports` migration must be separately mapped and validated.

## 6. Validation

`python tools/audit_repository.py` performs a read-only check of:

- required current navigation files;
- JSON parsing for every tracked JSON file;
- exact canonical page coverage (004=1–71; 005=1–120);
- local Markdown link targets;
- exact duplicate-content warnings.

Validation result at cleanup completion:

- canonical 004 coverage: 71/71;
- canonical 005 coverage: 120/120;
- all tracked JSON payloads parse;
- no broken local Markdown links detected;
- no exact duplicate-content sets detected;
- audit: PASS.

## 7. Residual structural debt

Intentionally unresolved:

1. root source/OCR payload names are inconsistent and sometimes very long;
2. `research_notes/` remains a large flat provenance layer;
3. historical process notes retain obsolete `ACTIVE`, `HOLD`, `pending`, and `next action` language;
4. old backtick path references are prose, not Markdown links, and may still name historical files;
5. remote branch aliases from the 2026-08-28 connector cleanup remain tooling noise.

These items do not obscure current authority after this pass. A deeper path migration would be a separate operation with a machine-readable redirect map and link/reference rewrite.

## 8. Restart shorthand

> **Read root `CURRENT_STATE.md`, then root `CANONICAL_INDEX.md`. Use the twelve paginated clean JSON batches as notebook text authority, with the current source-critical gate and terminal dossier controlling exact evidentiary use. Git history holds the removed state/process residue.**
