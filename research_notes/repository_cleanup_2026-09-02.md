# Lovejoy corpus — full-repository structural cleanup

Date: 2026-09-02  
Status: **SECOND-PASS STRUCTURAL ROUTING COMPLETE / EVIDENCE PRESERVED**

## Scope

The 2026-09-01 cleanup solved authority drift: it consolidated living state/navigation, removed supersession-only AOS process notes and root state deltas, retained canonical page records and raw source payloads, and installed a structural audit. The remaining problem was not contradictory evidence but repository shape: `research_notes/` remained physically flat, `archive_index/` and `archive_transcriptions/` had no directory-local authority guides, and the intentionally unmigrated root payloads had no exhaustive structural inventory.

This second pass therefore organized the repository without a broad path migration or evidence deletion.

## Changes

Created:

- `research_notes/README.md` — thematic routing plus terminal/provenance distinction;
- `archive_transcriptions/README.md` — twelve-batch authority map, field semantics, completion workflow;
- `archive_index/README.md` — discovery/locator/custody authority boundary;
- `root_payload_index.md` — inventory and preservation policy for non-control root files;
- this manifest.

Updated:

- root `README.md` — routes readers through the new directory maps and root payload inventory;
- root `CANONICAL_INDEX.md` — records the directory maps, current cleanup record, and 005 pp.31–36 Marillier source-collation handoff;
- `tools/audit_repository.py` — requires the new routing files and fails if a new tracked root payload appears without being registered in `root_payload_index.md`.

## 005 pp.31–36 integration

`MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md` is now explicitly routed as an `external_source_collation` dossier. It narrows source packets for rank/status continuity, ritual/provision conditions, Tonga/Bolotoo -> Tahiti/Marquesas, Aht/Natchez, Futuna `fale-mate`, and Callaway/AmaZulu material. It does not alter canonical manuscript wording because the original page image was not available through the active Library reading channel during that pass.

The diplomatic restart therefore remains pp.31–36. The source problem is narrower; the manuscript-reading problem is still open.

## Deletion/migration decision

No additional research dossier, archive index, canonical transcription batch, OCR payload, metadata file, or export bundle was deleted in this pass. Existing root payloads remain stable because a cosmetic move would break historical references. `research_notes/` remains physically flat for the same reason; the new directory README supplies an authority layer without rewriting hundreds of paths.

A future physical migration is allowed only with a machine-readable redirect map, reference rewrite, and audit in the same operation.

## Current repository model

`CURRENT_STATE.md`
-> `CANONICAL_INDEX.md`
-> directory-local README / governing gate
-> canonical page/source/index object
-> terminal dossier / audit trail
-> historical process provenance / Git history.

This keeps archival evidence, uncertainty, rejected readings, and negative searches visible while preventing old process language from acting as current authority.
