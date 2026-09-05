# Frozen research-note index

Status: FROZEN SNAPSHOT ROUTER / 2026-09-05

## Snapshot

`research_notes/_frozen/snapshot_2026-09-05/` is a byte-preserving Git-tree snapshot of the former flat `research_notes/` directory (tree `5074eb4de1f44b4e4da019ca04523fbe0120ab48`). It contains the accumulated round files, batch matrices, handoffs, exploratory drafts, source-recovery logs, superseded controls, and copies of the files that remain active today.

The snapshot is provenance, not the default research surface.

## Default retrieval order

1. current root controls (`CURRENT_STATE.md`, `CANONICAL_INDEX.md`, `PROJECT_ARGUMENT_MAP.md`);
2. active `research_notes/README.md`;
3. the relevant terminal synthesis;
4. `FROZEN_PROVENANCE_REGISTER.md`;
5. only then a specifically identified file inside `_frozen/snapshot_2026-09-05/`.

Do not run broad recursive review across the snapshot to answer a question already closed by a terminal synthesis.

## Legacy path rule

A pre-migration reference of the form:

`research_notes/<OLD_NAME>`

maps to:

`research_notes/_frozen/snapshot_2026-09-05/<OLD_NAME>`

unless `<OLD_NAME>` is one of the active files still present directly in `research_notes/`.

This mapping is intentionally one-way. Do not recreate flat compatibility copies; doing so would reintroduce the search clutter this freeze is designed to remove.

## What was frozen

The snapshot includes, among other things:

- round-numbered research passes;
- batch CSV matrices and deltas;
- HANDOFF files;
- source-recovery rounds and failed/partial recovery logs;
- exploratory or superseded JHI drafts and calibration passes;
- pre-terminal 004/005 dossiers;
- comparative-primitive, formation, later-Lovejoy, and institutional side investigations already governed by terminal or frozen controls.

Nothing was deleted from Git history. The move changes the active retrieval surface, not the evidentiary record.

## Reactivation

Reactivate evidence, not whole workflows. When a frozen file contains a genuinely needed point, record that point in the relevant active terminal/control with its old filename and snapshot path. Keep the old round frozen.
