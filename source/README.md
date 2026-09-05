# Source tree

`source/` is the mandatory home for raw or near-raw source payloads used by research notes but not appropriate for repository root.

Route by evidentiary/provenance function rather than file extension:

- `archive/` — archival scans/OCR derivatives, grouped by repository.
- `institutions/` — institutional publications, programs, reports, and related OCR payloads.
- `lovejoy/` — Lovejoy publications and later Lovejoy corpus material.
- `reference/` — dictionaries, bibliographies, and biographical/reference works.
- `context/` — contemporaneous books, periodicals, articles, and text witnesses used for contextual/source comparison.
- `discovery/` — search/export/metadata payloads; discovery aids, not automatically evidentiary witnesses.
- `notebooks/` — notebook-level indexes and notebook source payloads/derivatives when present.

As of 2026-09-05, every payload migrated from repository root has a bibliographic/source-class destination. The temporary `_unclassified/` holding area is no longer active.

## Retrieval rule

Future research should begin from `SOURCE_INDEX.md`, the relevant terminal synthesis, or a curated transcription/index. Do not recursively scan the whole source tree merely to rediscover a previously routed witness.

A JSON/XML/TXT derivative is not automatically canonical because it is machine-readable. Canonical transcription and argument authority remain defined by the living controls and terminal syntheses.

## Ingestion rule

Raw source payloads do not belong in repository root. New downloads/OCR exports should be placed under the appropriate `source/` branch at ingestion time and registered in `SOURCE_INDEX.md` when intended for reuse.

If a new payload genuinely cannot be identified from its own metadata/front matter, a temporary `_unclassified/` path may be created, but it should be resolved before the payload becomes part of an active evidence chain.
