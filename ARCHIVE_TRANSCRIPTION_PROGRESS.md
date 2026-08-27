# Lovejoy manuscript transcription progress

## Working method

Manuscript notebooks are corrected in 15–20 PDF-page batches against page images; PaddleOCR-VL is only a scaffold. Corrected JSON preserves readable abbreviations, marks uncertain/illegible readings, records visible manuscript labels, and retains source PDF/OCR SHA-256 values. Interpretive research notes remain separate from transcription files.

## MS38_004_001_061_004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Status: **71/71 complete, first pass**.
- Batches:
  - `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`
- Remaining work: second-pass verification of marked French, Pāli/Sanskrit, and compressed bibliographic readings.
- Published-paper cross-read: `research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md`.
- Direct formal counterpart: Arthur O. Lovejoy, “The Buddhistic Technical Terms upādāna and upādisesa,” *Journal of the American Oriental Society* 19 (1898), 126–136.
- Current judgment: the later notebook is preparatory/contemporaneous working material for the 1898 paper, while the whole notebook is broader than that article.

Key source-derived structure: Sāṁkhya method → Buddhist agnosticism/flux → dependent origination → khandhas → `upādāna/upādhi/upādisesa` → Nirvāṇa. The notebook closes with Lovejoy’s own historical decomposition: **original elements = flux / Three Characteristics + Dependent Origination; derived elements = sense-perception theory + psychology + khandhas.**

## MS38_004_001_061_005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Status: **120/120 complete, first pass**.
- Batches:
  - `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json`
- Remaining work: second-pass verification of ethnographic names, French/German titles, source-page references, and marked low-confidence fragments.

### Provenance and chronology

005 is now treated as a **composite longitudinal notebook**, not a single-date object.

- Strong **Paris 1898–99 core**: Paris stationery; internal `Dec. 14`, `May 29`, and `Marillier — Survivance — 12 June`; official EPHE 1898–99 report names Lovejoy among auditors taking an active part in Léon Marillier’s conferences on survival of the soul, human sacrifice and ritual anthropophagy.
- Marillier’s published/course programme closely matches the notebook’s early and middle trajectory: non-moral future-life beliefs, origin of death, funerary/expiatory/magical/fecundative sacrifice, African and North-American evidence, blood, agricultural rites and anthropophagy.
- **Second-pass correction completed:** PDF p.44 is securely read as **`Hist. Relig. — Dec. 20, 1905.`** The archival JSON `MS38_004_001_061_005_p031-045_clean.json` has been updated accordingly, with a second-pass note and confidence upgrade. The previous first-pass `1805 [or 1905?]` reading is superseded.
- The p.44 outline continues primitive religion, Old Testament material, `psychē`, `nephesh/ruach`, ancestor worship and totemism, proving reuse/extension at least through 1905. Surrounding pages should not automatically be assigned to 1905 without further stratigraphy.

### Current research bridge

Working 005→1906 comparison:
- `research_notes/MS38_004_001_061_005_vs_1906_Primitive_Philosophy_working_comparison.md`
- `research_notes/MS38_004_001_061_005_vs_1906_addendum_after_complete_notebook.md`

Current model: **Marillier/EPHE comparative-religion source collection (1898–99) → continued/reused `Hist. Relig.` notebook work documented in 1905 → theoretical condensation around causal efficacy / “primitive energetics” in 1906.** The strongest manuscript signals are decomposition by mechanism, fetish vs charm/amulet, intrinsic vs indwelling-spirit efficacy, transferable blood/body-part power, and p.105’s “quasi-mechanical and magical rather than sacramental.” Direct dependence still awaits ingestion of the full 1906 primary text.

### Major source-derived topic blocks

- pp.1–30: future life, death, non-moral vs moral determinants, survival/second death, missionary/contact source criticism.
- pp.31–45: totemism, Hebrew eschatology, `nephesh/ruach`, Greek `psychē/thymos`, comparative teaching outlines; p.44 dated **20 Dec. 1905**.
- pp.46–75: sacrifice typologies, blood/communion, funerary provision, magical vs personal-divine mechanisms, critique of simple evolutionary sequences.
- pp.76–90: messenger/substitution sacrifice, ancestral bargains, circumcision/blood brotherhood, foundation rites, charms/fetishes, transferable efficacy.
- pp.91–105: first fruits, layered ancestor/nature/high-god classifications, agricultural/fecundative sacrifice, chronology of agriculture/domestication, vegetation spirits, quasi-mechanical magical action.
- pp.106–119: cannibalism by mechanism, propitiation vs communion, rejection of circumcision-as-partial-sacrifice, initiation/purification/social-status mechanisms, selected organs as transferable efficacy; sustained argument ends p.119.
- p.120: back-matter memorandum rather than continuation of the main argument.

## 2026-08-27 full material-form audit layer

The two original source PDFs are now confirmed in the user's Library `/lovejoy` folder:

- `/lovejoy/MS38_004_001_061_004.pdf` — 45,542,867 bytes, 71 pages.
- `/lovejoy/MS38_004_001_061_005.pdf` — 106,709,841 bytes, 120 pages.

This resolves the earlier source-location uncertainty. **The originals are present; they are not missing.** The current technical problem is narrower: the Library page renderer returns no page image/content for these scans, and raw materialization currently returns HTTP 403. Exact byte equality against the source-PDF SHA-256 values retained in the corrected JSON has therefore not yet been revalidated.

A separate non-duplicative material ledger is now initialized:

- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`

Coverage is **191/191 pages structurally registered**. Each page points back to its authoritative `*_clean.json` corrected-text chunk. The second pass will record material evidence only: crossings-out, overwriting, insertions, arrows/connectors, marginalia, numbering/reordering marks, hand/ink shifts, page geometry and spatial relations.

Important evidence rule: `pending_visual_second_pass` means **not yet visually re-audited**, not “feature absent.” Textual/relational claims remain controlled by the completed corrected transcriptions; pen-level/spatial claims remain capped until page images render.

Priority close-audit pages remain:
- 004: the `viññāṇa` / `nāmarūpa` temporal-versus-logical relation page, ideally ±1.
- 005: pp.16–20 and 24–27; then 34–36, 67, 69–70, 76, 103.

The user has requested that the visual second pass cover **the entire 191-page corpus**, not only these priority pages, so the final material layer should be whole-notebook coverage with extra resolution on the argument-sensitive pages.

## Cross-project research status

The manuscript text layer is publication-stable; the only remaining archive-side task is the all-page material-form second pass just described. Current priority comparisons are:

1. **004 → 1898 JAOS → 1902 “Religion and the Time-Process”**.
2. **005 Paris/Marillier layer → 005 1905 reuse → 1906 “Primitive Philosophy.”**
3. **005 Hebrew/`Hist. Relig.` layer → 1907 “The Origins of Ethical Inwardness in Jewish Thought.”**

See the canonical live research log: `research_notes/lovejoy_as_orientalist_web_sweep.md`.