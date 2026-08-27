# Repository frozen strata — 2026-08-27

Status: **POLICY FREEZE / historical process material preserved, no longer authoritative for current status.**

A branch snapshot was created before cleanup:

- `snapshot/pre-freeze-2026-08-27`
- base commit: `249e8a29862d2daca84f1fbb6b698a2bf2fa6456`

This guarantees the pre-freeze active-tree layout remains directly recoverable even where the main branch is later simplified.

## Freeze rule

The repository distinguishes four layers:

1. **Primary/source layer** — raw OCR/HTML/EPUB/source text, archive indexes, clean manuscript transcriptions. Preserve.
2. **Canonical analytical layer** — files explicitly listed in `research_notes/CANONICAL_INDEX_2026-08-27.md`. Current authority.
3. **Evidence infrastructure** — source registers, matrices, consolidated CSVs, manifests. Preserve as supporting apparatus; not narrative authority by themselves.
4. **Frozen process layer** — exploratory batches, dated sweeps, superseded drafts, old queues, temporary gap audits, version chains. Preserve historically; do not restart from them.

## Frozen filename families

Unless the canonical index explicitly whitelists a file, treat these as frozen:

- `research_notes/lovejoy_as_orientalist_web_sweep_batch*`
- `research_notes/lovejoy_global_archive_harvest_batch*`
- dated `research_notes/JHI_blog_*` architecture, pressure-test, source-lock, draft, and gate files prior to the final 2026-08-27 gate
- `research_notes/*_batchNNN.md`
- `research_notes/*_batchNNN.csv`
- exploratory `*_v1`, `*_v2`, etc. where a later version or consolidated file exists
- `remaining_evidence_priority_matrix_*`
- old `manual_*`, `*_click_queue_*`, `*_manual_scan_queue_*`, and temporary retrieval packets once their outcomes have been incorporated
- `final_web_saturation_sweep_2026-08-27.md` as a process record; its conclusions are merged into `JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`
- `JHI_latest_delta_gap_audit_2026-08-26.md` as a superseded gap snapshot

## Version-chain rule

Where several files represent explicit versions of the same table or map, the highest version is the only active version unless a canonical dossier cites an earlier version for a specific historical reason.

Example:

- `MS38_004_source_uptake_map_v1.csv` … `v6.csv` = frozen
- `MS38_004_source_uptake_map_v7.csv` = current versioned map

The same logic applies to old priority matrices and session-calendar versions.

## Batch prose rule

Batch prose often contains useful quotation packets, failed hypotheses, temporary HOLDs, and search-path provenance. It is intentionally retained because it documents research process and may contain details not repeated verbatim in a canonical dossier.

However, batch prose does **not** control:

- current blocker status;
- current claim ceiling;
- whether a source is still missing;
- whether a HOLD remains active;
- whether web research should resume.

Those questions are controlled only by:

1. `CURRENT_STATE.md`
2. `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`
3. `research_notes/CANONICAL_INDEX_2026-08-27.md`
4. source-specific canonical dossiers named there

## Old JHI drafts

Earlier drafts remain historically useful for prose recovery but are frozen because several major facts changed after they were written:

- direct recovery of `Democracy in the Twentieth Century`;
- direct recovery of the 1907 *Entangling Alliance*;
- recovery of the 1906 More review and Sutta Nipāta recurrence;
- correction of the Great Chain Buddhism/Vedānta negative-OCR impression;
- direct material-form closure of 004/005 over all 191 pages.

No older JHI draft should be submitted or treated as evidentially current without being regenerated from the final gate.

## Old queues and HOLD language

Historical files may still say `HOLD`, `pending`, `blocker`, `missing`, `next action`, `manual download`, or similar. These tokens are not active instructions after this freeze unless repeated in `CURRENT_STATE.md`.

As of the freeze:

- MD-001 Democracy — closed direct primary;
- MD-006 004/005 original pages — closed material-form audit;
- MD-007 Thomas — closed direct primary;
- MD-009 EPHE exact scolarité cote — closed negative retrieval;
- MD-010 Dahlmann — closed direct primary;
- Jastrow Congress — closed direct primary;
- Great Chain p.35/index/full audit — closed direct primary;
- 1907 Hibbert — closed direct primary;
- final 1906 grammar audit — closed.

Only Harvard exact 1896–97 course-description wording remains optional publication hygiene, not an argument blocker.

## Why the files are not mass-deleted

The project is evidence-heavy. A batch file may preserve a URL path, failed reading, temporary attribution, or negative search that is useful for auditability even when its conclusion has been superseded. Deleting hundreds of these files would reduce active-tree clutter but also erase convenient process provenance from the current branch.

The chosen freeze is therefore **semantic and navigational rather than destructive**:

- snapshot branch preserves the entire pre-freeze tree;
- main branch defines a small canonical surface;
- historical files remain searchable but explicitly non-authoritative;
- future cleanup may physically move/delete frozen strata only if storage/readability becomes a problem.

## Reopening rule

A frozen file may be promoted back to active status only if it supplies one of the following:

- a source not represented in the canonical layer;
- a direct contradiction requiring revision of a current claim;
- a publication-grade quotation/page proof unavailable elsewhere;
- a provenance fact necessary to reproduce a result.

Promotion should be explicit in `CANONICAL_INDEX_2026-08-27.md` and `CURRENT_STATE.md`.
