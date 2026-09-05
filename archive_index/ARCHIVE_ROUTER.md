# Archive index router

Status: **ACTIVE ARCHIVE ROUTING SURFACE**

Use this file instead of scanning the historical archive-index corpus.

## Current canonical controls kept at `archive_index/`

- `AOS_1897_No30_p389_direct_visual_control_2026-09-05.md` — direct printed p.389 title control.
- `AOS_1897_Final_Circular_Lovejoy_title_attendance_control_2026-09-05.md` — 18 Mar / 10 Apr AOS circular-response architecture.
- `AOS_1896_1897_abstract_procedure_control_2026-09-05.md` — abstract / brief-statement procedure.
- `AOS_1897_1899_1919_bylaw_recordbook_control_2026-09-05.md` — AOS record-book duties and By-Law V.
- `JHU_RG04090_Paul_Haupt_1878_1916_carrier_ceiling_2026-09-05.md` — de-prioritized Paul Haupt public-discovery ceiling.

These paths remain stable because living terminal syntheses cite them directly.

## AOS / 1897 context

Use `aos_context/` for supporting carrier and institutional-context controls: officer/editorial workflow, Baltimore press, Ira Price, the Johns Hopkins local-host association, and Yale/AOS custody-recordbook searches. These are supporting controls, not the primary 1897 route.

## Johns Hopkins

Use `jhu/` for MS-0038/MS-0873 acquisition targets, remote-reproduction status, and the Harvard Graduate Philosophical Society minutes preserved in the Lovejoy papers. Use `jhu/jhu_ms0038_correspondence_component_index.csv` only when exact correspondence-component routing is needed.

## Harvard

Use `harvard/` for Harvard institutional/acquisition controls: History of Religions Club, James Walker Fellowship, permission receipt, and the Dorsey/Brinton curriculum-exchange target.

## Lovejoy acquisition targets

Use `lovejoy_targets/` for named unresolved or later acquisition objects that remain useful as locators but are not part of the current short-form evidence chain.

## Research correspondence

Use `correspondence/research_correspondence_Lovejoy_archive_and_JHI_crosswalk_2026-09-02.md` for public-safe request/reply provenance. It records why sources were requested and what archive responses changed; it is not primary historical evidence.

## Frozen archive-search history

The complete former flat `archive_index/` tree is preserved verbatim at:

`_frozen/snapshot_2026-09-05/`

Historical batch CSVs, global repository sweeps, handoffs, negative searches, superseded target notes, and old crosswalks live there. They should not be searched by default.

Default path:

> **terminal synthesis -> ARCHIVE_ROUTER -> one exact active control -> frozen snapshot only for provenance or a specifically named old search**
