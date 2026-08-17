# lovejoy_corpus

Working corpus for Arthur O. Lovejoy research. The repository currently combines OCR/text sources, bibliographic/metadata harvests, and a separate archival-transcription layer for manuscript notebooks.

## Manuscript transcription

Notebook correction is proceeding in batches of 15–20 PDF pages, checked visually against the manuscript images rather than accepting OCR at face value. Uncertain readings remain explicitly marked.

Current progress: see [`ARCHIVE_TRANSCRIPTION_PROGRESS.md`](ARCHIVE_TRANSCRIPTION_PROGRESS.md).

**MS38_004_001_061_004 — “Sankhya + Buddhism” is now complete through PDF p. 71 (first-pass transcription).** Four corrected batches are stored under `archive_transcriptions/`:

- [`archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`](archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json)
- [`archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`](archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json)
- [`archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`](archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json)
- [`archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`](archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json)

A second notebook, **MS38_004_001_061_005**, is being processed in parallel; see the progress log for its current state.

## Data-layer rule

Raw/source-derived corpora and corrected archival transcriptions should remain distinguishable from later interpretive research notes. Source filenames and SHA-256 hashes are retained where possible so transformations can be audited.
