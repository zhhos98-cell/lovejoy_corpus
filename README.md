# lovejoy_corpus

Working corpus for Arthur O. Lovejoy research. The repository currently combines OCR/text sources, bibliographic/metadata harvests, and a separate archival-transcription layer for manuscript notebooks.

## Manuscript transcription

Notebook correction is proceeding in batches of 15–20 PDF pages, checked visually against the manuscript images rather than accepting OCR at face value. Uncertain readings remain explicitly marked.

Current progress: see [`ARCHIVE_TRANSCRIPTION_PROGRESS.md`](ARCHIVE_TRANSCRIPTION_PROGRESS.md).

First completed batch: [`archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`](archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json), from the notebook labelled **“Sankhya + Buddhism.”**

## Data-layer rule

Raw/source-derived corpora and corrected archival transcriptions should remain distinguishable from later interpretive research notes. Source filenames and SHA-256 hashes are retained where possible so transformations can be audited.
