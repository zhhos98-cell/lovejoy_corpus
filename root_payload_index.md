# Root payload compatibility index

Status: COMPATIBILITY ROUTER / RAW PAYLOADS MIGRATED 2026-09-05

The repository root is no longer a source-payload directory. Raw and near-raw PDFs, OCR JSON/XML/TXT, HTML witnesses, EPUBs, ZIP exports, and discovery CSVs belong under `source/`.

Use:

- `source/README.md` for the directory contract;
- `source/SOURCE_INDEX.md` for the active payload map;
- `archive_transcriptions/` for curated/canonical transcriptions;
- `archive_index/` for archive-level registry and locator controls;
- `research_notes/FROZEN_PROVENANCE_REGISTER.md` and terminal syntheses for research-state routing.

This file remains at the old path because older notes and agents may still look for `root_payload_index.md`. It is now a compatibility pointer only. Do not add new raw payload entries here.

## Migration rule

A new raw download or OCR derivative must be ingested directly into the appropriate branch under `source/` and, when intended for reuse, registered in `source/SOURCE_INDEX.md`. Do not put it in repository root first.

The 2026-09-05 migration reused the existing Git blobs at new paths; source bytes were not rewritten by the structural move. Old root paths remain recoverable through Git history.
