# Working rules

Last updated: 2026-08-28

## 1. Durable-state rule

This repository is the durable research state. Do not leave thesis-bearing progress only in a chat session.

During an active research run:

1. **Synchronize early and repeatedly.** Commit every material evidentiary result, correction, bounded negative, branch decision, or superseded hypothesis.
2. **Optimize for restart safety.** A checkpoint should state what was tested, source/locator, result, warrant/confidence, what changed, and the exact next action.
3. **Keep one living state.** `CURRENT_STATE.md` is the only authority for whether a branch is live, frozen, parked, or complete.
4. **Use one current canonical index.** `research_notes/CANONICAL_INDEX_2026-08-28.md` is the routing surface for current evidence. Older indices are historical snapshots unless explicitly reactivated.
5. **Do not reconstruct from chat memory when repo state exists.** Restart from `CURRENT_STATE.md`, then the canonical index, then the terminal/source-specific dossier.
6. **Record negative controls.** Failed locators and bounded negatives are evidence when they constrain claims; distinguish search-layer failure from archival absence.
7. **Separate evidence levels.** Keep direct primary, mediated quotation, field control, analyst-level structural homology, and genealogy/influence claims distinct.

Compact rule:

> **Sync often enough that losing the conversation costs at most one small research step.**

## 2. Branch lifecycle

Every thesis-bearing research branch should move through:

`reopen / define question`
→ `source-specific checkpoints`
→ `terminal synthesis / closure dossier`
→ `update CURRENT_STATE + canonical index`
→ **refreeze**.

After refreeze:

- old `ACTIVE`, `HOLD`, `pending`, `next action`, `blocker`, or `missing` text inside process files is historical;
- the final handoff/closure and canonical index control interpretation;
- do not reopen simply because an old queue remains unfinished;
- broad exploratory sweeps should not continue after the live proposition is already saturated.

A frozen branch may reopen only when direct new primary evidence changes a live proposition, a current source is contradicted, publication requires exact citation/facsimile verification, or an analytical category already in use requires materially different historical reconstruction.

## 3. Cleanup and provenance

The working tree should privilege:

`CURRENT_STATE`
→ `current canonical index`
→ `terminal dossiers`
→ `evidence infrastructure / raw provenance`.

Rules:

1. Raw manuscripts, transcriptions, source payloads, material-audit records, edit logs and reproducible data should be preserved unless independently proven redundant.
2. Consolidated matrices/batch outputs may remain when they preserve provenance or reproduce a claim, even if they are not narrative authority.
3. Process notes that are fully superseded and add no unique provenance may be removed from the working tree after their terminal conclusion is preserved; Git history remains the process archive.
4. Do not move large legacy OCR/metadata payloads merely for aesthetics if existing references may depend on their paths. Record the legacy layout and migrate only in a dedicated path-breaking cleanup.
5. Scripts belong under `tools/`; root should be reserved primarily for project navigation and legacy source/data payloads whose paths are intentionally stable.
6. A cleanup pass should leave a dated manifest under `research_notes/` describing retained layers, removed/moved files, and any intentionally unresolved structural debt.

## 4. Interpretation hygiene

For the current Lovejoy project specifically:

- relation non-identity does not establish historical independence;
- decomposition or proposition insulation is not uniquely Lovejoyian;
- structural recurrence is not genealogy;
- teacher/curricular adjacency is not total-method transmission;
- logical-analysis controls calibrate the notebook argument rather than create a standalone Blog section;
- the Carnap line is frozen field/adversarial control unless direct new primary evidence changes a live claim.

## 5. Restart shorthand

> **Read `CURRENT_STATE.md`, then `research_notes/CANONICAL_INDEX_2026-08-28.md`. Treat everything else as source, support, or history unless those two files say otherwise.**
