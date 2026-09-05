# `archive_transcriptions/` — authority map

Date: 2026-09-05  
Status: **CANONICAL PAGE-RECORD LAYER / DIPLOMATIC COMPLETION IN PROGRESS / INTEGRATED SURFACE PENDING REGENERATION**

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

A 2026-09-05 witness/source-layer hygiene pass changed six 005 batches (`p031-045` through `p106-120`). It propagated existing image-secure controls and later source-ownership ceilings but did **not** claim new diplomatic page completion.

## 2. Reading surface

`MS38_004_005_integrated_page_by_page_final_2026-09-01.md` is generated from the twelve canonical batches. Its legacy filename contains `final`; that word does **not** mean every page has a complete diplomatic transcription.

**Current synchronization state, 2026-09-05:** the generated Markdown predates the six canonical 005 batch edits made in the current connector-only pass. Until regenerated, it is **STALE RELATIVE TO THE CANONICAL JSON**. Use the twelve paginated batches as authority.

The current runtime can write GitHub files but cannot execute the repository generator against the connected working tree. Do not manually rewrite the 191-page generated file merely to hide the divergence.

Run when repo-shell access is available:

```bash
python tools/build_integrated_transcription.py
python tools/build_integrated_transcription.py --check
python tools/audit_repository.py
```

After those commands pass, remove the stale warning here and in the root progress/queue files.

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

Notebook 005 is active. Restart diplomatically at pp.31–36, then pp.42–43, then pp.47–60, and continue page by page. The active canonical `p031-045` batch now records the pp.31–36 Marillier map only as `external_source_collation` and explicitly marks those pages `DIPLOMATIC HOLD`; source collation does not replace direct manuscript rereading.

The 2026-09-05 hygiene pass also made the principal later witness ceilings explicit: p.55 taste-direction/source boundary HOLD; p.66 W3 mechanism→jurisdiction; p.84 relation-level downgrade; p.90 relation-level HOLD; pp.92–99 Marillier-mediated by default; p.103 W3 chronology veto; p.104 W3 path exclusion; p.112 argument-level case adjudication with exact-wording residue; p.117 W3 wording/authorship HOLD; p.119 authorship+chronology HOLD.

Notebook 004 is argument-control closed for the present research project but remains short of a full diplomatic edition.

## 6. Mutation rule

Before changing a canonical page record:

1. inspect the current batch record;
2. read the latest page/block dossier;
3. inspect the original manuscript image;
4. preserve already merged later direct-image corrections;
5. mark unresolved readings rather than importing external source wording;
6. rebuild the integrated reading surface when repo-shell access permits; otherwise record the generated-surface divergence explicitly;
7. run the repository audit after regeneration.
