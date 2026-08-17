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

A second notebook, **MS38_004_001_061_005**, is being processed in parallel; the canonical progress log now records completion through **PDF p. 105**, with pp. 106–120 remaining as the final batch. See [`ARCHIVE_TRANSCRIPTION_PROGRESS.md`](ARCHIVE_TRANSCRIPTION_PROGRESS.md) for the live batch-by-batch state.

A second manuscript→publication relationship is now under active test: **005 → Lovejoy's 1906 “The Fundamental Concept of the Primitive Philosophy.”** Corrected pp. 76–105 distinguish personal/spiritual agency from intrinsic magical efficacy and p. 105 explicitly calls one sacrificial mechanism **“quasi-mechanical and magical rather than sacramental,”** strikingly close to the 1906 paper's independently documented “quasi-mechanical” theory of primitive power. This remains a strong working hypothesis until the full 1906 primary text is ingested and concorded. See [`research_notes/MS38_004_001_061_005_vs_1906_Primitive_Philosophy_working_comparison.md`](research_notes/MS38_004_001_061_005_vs_1906_Primitive_Philosophy_working_comparison.md).

## Lovejoy as Orientalist / comparative religion — live research sweep

A whole-web research stream is active, with evidence separated into primary works, archival/institutional context, reception, and inference:

- live narrative log: [`research_notes/lovejoy_as_orientalist_web_sweep.md`](research_notes/lovejoy_as_orientalist_web_sweep.md)
- structured source/evidence register: [`research_notes/lovejoy_orientalist_source_register.csv`](research_notes/lovejoy_orientalist_source_register.csv)
- web sweep batch 02 (1906 / notebook 005 / reception): [`research_notes/lovejoy_as_orientalist_web_sweep_batch02_1906_and_005.md`](research_notes/lovejoy_as_orientalist_web_sweep_batch02_1906_and_005.md)

Current provisional shape: a direct Buddhist/Indic specialist episode in the late 1890s–1901; a likely transformation into comparative religion by 1906; and later Asian/Near Eastern material re-entering the mature history-of-ideas program through Chinese transmission research and collaboration with area specialists such as William F. Albright and Paul-Émile Dumont. A particularly important formation lead is the Harvard context: during Lovejoy's graduate residence, Charles Rockwell Lanman led Sanskrit/Indo-Iranian studies, Henry Clarke Warren's *Buddhism in Translations* appeared in the Harvard Oriental Series (1896), and Lanman publicly lectured on Buddhism, Sāṁkhya/Vedānta, Sanskrit and Pāli in April 1896. Direct Lovejoy enrollment/attendance/contact is not yet proved.

The second web batch adds another potentially important sequence: notebook 005's analyses of fetish/charm, blood and transferable efficacy, natural/supernatural causation, and quasi-mechanical magical action converge closely with the published 1906 theory later called **“primitive energetics.”** The 1906 paper also had a broader reception than the 1898 Buddhist article: James H. Leuba discussed it by 1912, and C. G. Jung later cited Lovejoy repeatedly in treatments of `mana` and primitive energy. The full 1906 article is public domain and preserved in *The Monist* vol. 16 through HathiTrust / Internet Archive Scholar; locating and ingesting the current scan is the next primary-source priority.

## Data-layer rule

Raw/source-derived corpora, corrected archival transcriptions, and later interpretive research notes remain distinguishable. Source filenames and SHA-256 hashes are retained where possible so transformations can be audited.
