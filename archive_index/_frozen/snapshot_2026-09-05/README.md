# `archive_index/` — discovery and provenance map

Date: 2026-09-02  
Status: **ARCHIVAL DISCOVERY / LOCATOR / CUSTODY LAYER**

This directory records archive coverage, locators, entity resolution, correspondence/component indexes, search harvests, custody/provenance, and acquisition targets. It answers **where evidence may be, what has been searched, and how a record is identified**. It is not manuscript transcription authority and does not independently establish an historical claim.

## 1. Current correspondence / acquisition crosswalk

- `research_correspondence_Lovejoy_archive_and_JHI_crosswalk_2026-09-02.md` — public-repo-safe provenance crosswalk for JHU, Harvard, WashU, and JHI editorial correspondence. It records why archive requests were made, what institutional replies established, what remains open, and which repository dossiers those exchanges generated. Treat it as research-process and acquisition provenance, not as evidence about Lovejoy by itself.

This crosswalk preserves the distinction between an archive request, an institutional reply, receipt of a scan, and historical proof from the underlying source. Rights-restricted scans and private download links remain outside the public repository.

## 2. What belongs here

Typical contents include:

- JHU MS-0038 component, box/folder, correspondence, and cross-collection indexes;
- Harvard/AOS and other archive discovery targets;
- entity/authority records for people, organizations, and archival components;
- custody and search-provenance tables;
- acquisition/search target notes where the evidentiary object has not yet been obtained or closed;
- public-safe correspondence crosswalks documenting why a source was requested and what the archive response changed in the research workflow.

## 3. Authority boundaries

Use this directory for:

`LOCATOR -> SOURCE IDENTITY -> SEARCH / ACQUISITION PROVENANCE`.

Use `archive_transcriptions/` for manuscript page text and direct-image audit trails. Use `research_notes/` terminal dossiers for claim-level synthesis. Use root `CURRENT_STATE.md` and `CANONICAL_INDEX.md` for current branch status and routing.

A catalogue entry proves catalogue content. A programme proves programme wording. An archive target proves a search target. An email proves what was requested or reported by the correspondent. None of those alone proves attendance, uptake, influence, transmission, or the content of a manuscript page.

## 4. Preservation rule

Archive indexes are first-class evidence infrastructure. Do not delete a table because a claim has been closed; negative searches, failed identifications, alternate authority records, correspondence provenance, and custody history can matter later. If a newer index supersedes an older one, keep the old file when it carries unique search/provenance data and mark its routing status in a terminal dossier or this directory map rather than silently flattening it.

## 5. Naming rule for new index work

Prefer stable object-first lowercase `snake_case` filenames, archival IDs where necessary, ISO dates for dated snapshots, and explicit `target`, `audit`, `index`, `manifest`, `crosswalk`, or `correspondence` functions. Avoid creating new root-level archive tables unless a stable path is already required by external tooling.
