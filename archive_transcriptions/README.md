# `archive_transcriptions/` — authority map

Date: 2026-09-02  
Status: **CANONICAL PAGE-RECORD LAYER / DIPLOMATIC COMPLETION IN PROGRESS**

This directory contains the machine-readable page authority for Lovejoy notebooks 004 and 005, material-form audit records, direct-image delta registers, and the generated integrated reading surface. Root `TRANSCRIPTION_COMPLETION_QUEUE.md` controls diplomatic completion status.

## 1. Canonical page batches

Notebook 004:

- `MS38_004_001_061_004_p001-018_clean.json`
- `MS38_004_001_061_004_p019-036_clean.json`
- `MS38_004_001_061_004_p037-054_clean.json`
- `MS38_004_001_061_004_p055-071_clean.json`

Notebook 005:

- `MS38_004_001_061_005_p001-015_clean.json`
- `MS38_004_001_061_005_p016-030_clean.json`
- `MS38_004_001_061_005_p031-045_clean.json`
- `MS38_004_001_061_005_p046-060_clean.json`
- `MS38_004_001_061_005_p061-075_clean.json`
- `MS38_004_001_061_005_p076-090_clean.json`
- `MS38_004_001_061_005_p091-105_clean.json`
- `MS38_004_001_061_005_p106-120_clean.json`

These twelve paginated files, not any hypothetical aggregate `MS38_004_clean.json` or `MS38_005_clean.json`, are the current page-record authority.

## 2. Reading surface

`MS38_004_005_integrated_page_by_page_final_2026-09-01.md` is generated from the twelve canonical batches and must remain synchronized with them. Its legacy filename contains `final`; that word does **not** mean every page has a complete diplomatic transcription.

Run after canonical batch edits:

```bash
python tools/build_integrated_transcription.py
python tools/audit_repository.py
```

## 3. Field/layer rule

A populated `corrected_text` field is heterogeneous. It can contain:

- direct manuscript wording;
- readable fragments;
- conservative normalized text;
- an editorial argument summary.

Therefore `191/191` page coverage does not establish diplomatic completion. A page is diplomatically complete only when the manuscript image has been directly inspected, readable wording has been represented as fully as the image permits, uncertainty remains explicit, and source collation is kept separate from visible manuscript wording.

Use/retain fields that distinguish at least:

- `diplomatic_visible_text`;
- `editorial_argument_summary`;
- `external_source_collation`;
- `material_layout_observation`;
- `uncertain_readings`;
- `text_layer`;
- `witness_status`.

## 4. Audit/provenance records

Core material and delta trails include:

- `MS38_004_005_material_audit_manifest_2026-08-27.json`
- `MS38_004_001_061_004_round17_direct_image_deltas_p042_p049-052_2026-09-01.json`
- `MS38_004_005_round18_direct_image_deltas_2026-09-01.json`

Once a delta is merged, the paginated clean batch again becomes page authority; the delta stays as an audit trail.

## 5. Current completion boundary

Notebook 005 is active. Restart at pp.31–36, then pp.42–43, then pp.47–60, and continue page by page. `research_notes/MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md` narrows source packets for pp.31–36 but explicitly does not replace direct manuscript rereading.

Notebook 004 is argument-control closed for the present research project but remains short of a full diplomatic edition.

## 6. Mutation rule

Before changing a canonical page record:

1. inspect the current batch record;
2. read the latest page/block dossier;
3. inspect the original manuscript image;
4. preserve already merged later direct-image corrections;
5. mark unresolved readings rather than importing external source wording;
6. rebuild the integrated reading surface;
7. run the repository audit.
