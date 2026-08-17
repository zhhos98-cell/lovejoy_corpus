# lovejoy_corpus

Working corpus for Arthur O. Lovejoy research. The repository currently combines OCR/text sources, bibliographic/metadata harvests, a separate archival-transcription layer for manuscript notebooks, and research notes linking manuscript work to Lovejoy's publications.

## Manuscript transcription

Notebook correction is proceeding in batches of 15–20 PDF pages, checked visually against the manuscript images rather than accepting OCR at face value. Uncertain readings remain explicitly marked.

Current progress: see [`ARCHIVE_TRANSCRIPTION_PROGRESS.md`](ARCHIVE_TRANSCRIPTION_PROGRESS.md).

**MS38_004_001_061_004 — “Sankhya + Buddhism” is complete through PDF p. 71 (first-pass transcription).** Four corrected batches are stored under `archive_transcriptions/`:

- [`archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`](archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json)
- [`archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`](archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json)
- [`archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`](archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json)
- [`archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`](archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json)

The completed notebook has now been cross-read against Lovejoy's 1898 *Journal of the American Oriental Society* article, **“The Buddhistic Technical Terms upādāna and upādisesa.”** The comparison is recorded in [`research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md`](research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md). Current conclusion: the article is a sharply delimited publication extracted from a broader Sāṁkhya/Buddhism research notebook; the strongest continuity lies in Lovejoy's treatment of upādāna/upādisesa, overlapping nidāna/khandha classifications, and his argument that historically composite or borrowed elements can nevertheless acquire an intelligible and characteristic arrangement.

A second notebook, **MS38_004_001_061_005**, is being processed in parallel; see the progress log for its current state (currently complete through PDF p. 75).

## Data-layer rule

Raw/source-derived corpora, corrected archival transcriptions, and later interpretive research notes remain distinguishable. Source filenames and SHA-256 hashes are retained where possible so transformations can be audited.
