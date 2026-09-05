# Source tree

`source/` is the mandatory home for raw or near-raw source payloads that are used by research notes but should not sit in the repository root.

Route by evidentiary/provenance function rather than file extension:

- `archive/` — archival scans/OCR derivatives, grouped by repository.
- `institutions/` — institutional publications, programs, reports, and related OCR payloads.
- `lovejoy/` — Lovejoy publications and later Lovejoy corpus material.
- `reference/` — dictionaries, bibliographies, and biographical/reference works.
- `context/` — contemporaneous books, periodicals, and text witnesses used for contextual/source comparison.
- `discovery/` — search/export/metadata payloads. These are discovery aids, not automatically evidentiary witnesses.
- `notebooks/` — notebook-level indexes and, when present, notebook source payloads/derivatives.
- `_unclassified/` — retained raw payloads whose bibliographic identity is not yet secure enough for a semantic folder. Do not infer identity from filename alone.

## Retrieval rule

Future research should begin from `SOURCE_INDEX.md`, the relevant terminal synthesis, or a curated transcription/index. Do not recursively scan the whole source tree merely to rediscover a previously routed witness.

A JSON/XML/TXT derivative is not automatically canonical just because it is machine-readable. Canonical transcription and argument authority remain defined by the living controls and terminal syntheses.

## Root rule

Raw source payloads do not belong in repository root. New downloads/OCR exports should be placed under the appropriate `source/` branch at ingestion time and registered in `SOURCE_INDEX.md` when they are intended for reuse.
