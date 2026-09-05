# Lovejoy corpus — repository cleanup manifest

Date: 2026-08-28  
Status: **COMPLETE STRUCTURAL CLEANUP / CONSERVATIVE PROVENANCE PRESERVATION / RESTART-SAFE**

## 1. Scope

This pass treated the repository as a research archive rather than a software project. The aim was not minimum file count. The aim was to make current authority unambiguous while preserving enough source/provenance structure to reproduce claims and understand how conclusions were reached.

Audit categories:

1. **living authority** — current state/navigation/writing authority;
2. **terminal analytical dossiers** — source-specific or branch-closing evidence syntheses;
3. **evidence infrastructure** — matrices, consolidated CSVs, archive indexes and reproducible intermediate products;
4. **raw/source provenance** — OCR, transcriptions, source exports, edit logs and material-audit records;
5. **historical process** — batch notes, old syncs, HOLD/gap audits and superseded queues;
6. **structural debt** — files whose location/naming is imperfect but whose movement could break existing references.

## 2. Main finding

The repository was **not primarily dirty at the evidence layer**. The 2026-08-27 freeze had already removed many truly redundant process files and transcription duplicates. The remaining problem was mainly **navigation/state drift**:

- `README.md` still routed through the 2026-08-27 canonical index as if no later refrozen control line existed;
- the 2026-08-28 logical-analysis addendum still declared itself `ACTIVE` after the branch had been refrozen;
- `WORKING_RULES.md` still named an old logical-analysis handoff as an active restart point;
- `CURRENT_STATE.md` had become too large and repeated source-specific detail better kept in dossiers;
- an intermediate Friedman/Carnap ladder still carried `ACTIVE` status and an obsolete 28-Dec.-1935 Baltimore working date;
- two data-harvest scripts sat in repository root rather than `tools/`.

The corrective strategy was therefore **canonical consolidation + selective physical cleanup**, not mass deletion.

## 3. New living navigation

Created:

- `research_notes/CANONICAL_INDEX_2026-08-28.md`

It merges the base 2026-08-27 evidence surface with the refrozen 2026-08-28 logical-analysis/Carnap controls and becomes the single current canonical navigation file.

Rewritten/updated:

- `CURRENT_STATE.md` — compressed into a true living restart surface;
- `README.md` — routes to the new canonical index and current frozen state;
- `WORKING_RULES.md` — adds explicit branch lifecycle, refreeze and cleanup/provenance rules;
- `research_notes/Carnap_ladder_Friedman_scope_control_2026-08-28.md` — changed from active ladder to frozen support control and corrected the obsolete Baltimore date/state.

## 4. Files physically removed or moved

### Removed as superseded current navigation

- `research_notes/CANONICAL_INDEX_2026-08-28_LOGICAL_ANALYSIS_ADDENDUM.md`

Reason: it declared an `ACTIVE` branch and depended on the old 2026-08-27 index. Its useful content is now represented by the unified 2026-08-28 canonical index plus the terminal dossiers. Git history and `snapshot/pre-cleanup-2026-08-28` preserve the former file.

### Moved from root to `tools/`

- `harvest_gallica_lovejoy_primitive.py` → `tools/harvest_gallica_lovejoy_primitive.py`
- `harvest_lovejoy_metadata.py` → `tools/harvest_lovejoy_metadata.py`

Code content was preserved; only repository role/location changed.

## 5. Files intentionally retained

### `archive_transcriptions/`

Retained raw, corrected, clean, edit-log, diagnostic and material-audit layers. These are provenance, not redundant prose. In particular, raw/corrected/clean coexistence records transformations and should not be collapsed merely for tidiness.

### `archive_index/`

Retained archive coverage tables, locators and consolidated/delta evidence infrastructure. A batch file may be narratively obsolete while still recording search provenance or the negative scope of an archive query.

### `research_notes/` batch and matrix products

Retained consolidated matrices and most dated batch/process notes when they still preserve provenance or are referenced by later dossiers. Historical state words inside them are not current instructions.

A representative case is `research_notes/lovejoy_as_orientalist_web_sweep.md`: it still says `ACTIVE`, but later terminal syntheses supersede its state and other historical files reference it. Rewriting or deleting every such process file would produce more churn and broken links than value. Current authority is instead centralized in `CURRENT_STATE.md` + the canonical index.

### Root OCR / source / metadata payloads

Large source and derived payloads remain at existing root paths in this pass. The root includes OCR JSON, source text/HTML/EPUB, metadata CSVs and source-export ZIPs. Their layout is aesthetically imperfect, but moving them now could break path references in notebooks, matrices, external scripts or old commits.

Decision:

> **Retain legacy root data paths for stability. Any future migration into `sources/`, `ocr/`, `data/` or `exports/` should be a dedicated path-breaking migration with a redirect/path map.**

This is recorded structural debt, not an overlooked cleanup task.

## 6. Status-word policy after cleanup

The repository contains historical process files with words such as:

- `ACTIVE`
- `HOLD`
- `pending`
- `blocker`
- `missing`
- `next action`

These words are evidence about the state of a past research run. They do not define current project state.

Current-state precedence is:

`CURRENT_STATE.md`
→ `research_notes/CANONICAL_INDEX_2026-08-28.md`
→ terminal/source-specific dossier
→ process provenance.

Do not bulk-edit old process files solely to erase historical status words. Retag a historical file only when it is likely to misroute current work, as with the Friedman ladder.

## 7. Canonical state after cleanup

### Base JHI article

Frozen and draft-ready. No argument-sensitive blocker.

### Logical-analysis line

Refrozen. Final use is calibration:

- different local meanings of `logical`;
- typed relations + inferential jurisdiction as a structural candidate;
- mandatory adversarial rule `A ≠ B` does not establish independence.

### Carnap line

Refrozen field/adversarial control. Final developmental sequence:

`May 1934 conceptual liberalization`
→ `spring 1935 TM draft`
→ `June 1935 plural verification conditions + translation/equipollence`
→ `September 1935 explicit non-eliminative reduction`
→ `31 December 1935 Baltimore jurisdiction clash`
→ `1936–37 systematic publication`.

Do not reopen this line for the present Blog absent direct new primary evidence that changes a live claim.

## 8. Snapshot and rollback

Pre-cleanup safety branch:

- `snapshot/pre-cleanup-2026-08-28`

Earlier pre-freeze snapshot:

- `snapshot/pre-freeze-2026-08-27`
- base commit `249e8a29862d2daca84f1fbb6b698a2bf2fa6456`

Git history remains the process archive for physically removed working-tree files.

## 9. Connector-side branch noise

During setup, the repository connector repeatedly created several empty `maintenance/full-repo-cleanup-2026-08-28-vN` branch aliases while no file mutation had yet occurred on those refs. They do not contain independent research state. The available connector actions in this session expose branch creation/ref movement but not branch deletion, so these aliases cannot be removed programmatically here.

Treat them as tooling noise, not research branches. They can be deleted from GitHub branch management later without loss once the final cleanup commit is on `main`. The meaningful safety branch is only `snapshot/pre-cleanup-2026-08-28`.

## 10. Residual structural debt

Intentionally unresolved:

1. root-level source/OCR/data payloads have inconsistent names and several very large files;
2. some historical process notes retain old `ACTIVE`/HOLD wording;
3. dated batch files are numerous;
4. old citations may route to now-historical 2026-08-27 navigation files.

These are low-risk because authority is now centralized. Fixing them would require either path-breaking migration or mass provenance rewriting and is not justified for the present article.

## 11. Verification checklist

Before merging this cleanup into `main`, verify:

- `CURRENT_STATE.md` exists and points to the 2026-08-28 canonical index;
- `research_notes/CANONICAL_INDEX_2026-08-28.md` exists;
- the old 2026-08-28 ACTIVE addendum is absent;
- both harvest scripts exist under `tools/` and no longer at root;
- final Carnap handoff remains frozen;
- raw/clean notebook transcriptions remain untouched;
- base JHI evidence/writing files remain present;
- branch diff contains governance/navigation changes only, not accidental research-data deletion.

## 12. Restart shorthand

> **The repository is now governed as one living state + one canonical index + terminal dossiers + preserved provenance. Cleanup removed misleading current-navigation residue, not historical evidence. Large source/data paths were deliberately left stable.**
