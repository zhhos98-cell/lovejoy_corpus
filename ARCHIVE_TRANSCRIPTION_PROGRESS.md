# Lovejoy manuscript transcription progress

## Working method

Manuscript notebooks are corrected in 15–20 PDF-page batches against page images; PaddleOCR-VL is only a scaffold. Corrected JSON preserves readable abbreviations, marks uncertain/illegible readings, records visible manuscript labels, and retains source PDF/OCR SHA-256 values. Interpretive research notes remain separate from transcription files.

The archival layer now has two distinct authorities:

1. `*_clean.json` = corrected textual transcription.
2. `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json` = page-form/material evidence only.

The two layers must not be collapsed. A material feature can calibrate how a proposition was worked on the page without silently changing the corrected-text reading.

## MS38_004_001_061_004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Source SHA-256: `1ec301a9696949c04acf1c64633377db3fa8c68348d170831b8caa53c561b75f`.
- Text status: **71/71 complete, first pass**.
- Material status: **71/71 visual overview complete; high-value pages directly/high-resolution reviewed**.
- Batches:
  - `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`
- Remaining text hygiene only: second-pass verification of marked French, Pāli/Sanskrit and compressed bibliographic readings where publication drafting requires exact wording.
- Published-paper cross-read: `research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md`.
- Direct formal counterpart: Arthur O. Lovejoy, “The Buddhistic Technical Terms upādāna and upādisesa,” *Journal of the American Oriental Society* 19 (1898), 126–136.

Key source-derived structure: Sāṁkhya method → Buddhist agnosticism/flux → dependent origination → khandhas → `upādāna/upādhi/upādisesa` → Nirvāṇa. The notebook closes with Lovejoy’s own historical decomposition: **original elements = flux / Three Characteristics + Dependent Origination; derived elements = sense-perception theory + psychology + khandhas.**

### Material-form closure: pp.41–42

PDF p.41 contains a large diagram mapping dependent-origination / `nāmarūpa` relations against khandha categories.

PDF p.42 / manuscript p.123 is the strongest direct material control. Lovejoy draws a nested classification in which `viññāṇa` appears under `nāma` inside `nāmarūpa`, then immediately writes below that `viññāṇa` is temporally (?) antecedent to `nāmarūpa` and logically a subdivision of it.

Therefore the page **spatially holds apart classificatory inclusion and temporal priority**. No visible erasure creates the key sentence. Safe claim: the mismatch among relation types is a feature of the working page, not merely an editorial reconstruction from prose.

Do not generalize this local working practice into a claim that Buddhist material singly generated Lovejoy’s later method.

## MS38_004_001_061_005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Source SHA-256: `7ebf4e672bdb2267e71a9c6b617df2078f057b1f23858f2770a3f9de004d96ad`.
- Text status: **120/120 complete, first pass**.
- Material status: **120/120 visual overview complete; former MD-006 priority pages directly/high-resolution reviewed**.
- Batches:
  - `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json`
- Remaining text hygiene only: second-pass verification of ethnographic names, French/German titles, source-page references and marked low-confidence fragments where exact quotation is needed.

### Provenance and chronology

005 is a **composite longitudinal and physically accretive notebook**, not a single-date object.

- Strong **Paris 1898–99 core**: Paris stationery; internal `Dec. 14`, `May 29`, and `Marillier — Survivance — 12 June`; official EPHE 1898–99 report names Lovejoy among auditors taking an active part in Léon Marillier’s conferences on survival of the soul, human sacrifice and ritual anthropophagy.
- Marillier’s published/course programme closely matches the notebook’s early and middle trajectory: non-moral future-life beliefs, origin of death, funerary/expiatory/magical/fecundative sacrifice, African and North-American evidence, blood, agricultural rites and anthropophagy.
- PDF p.44 is directly confirmed from the page image as **`Hist. Relig. — Dec. 20, 1905.`** This proves reuse/extension through 1905; it does not date neighboring leaves or inserts automatically.
- The page-image audit now independently proves physical accretion: major inserted/foldout layers span approximately pp.29–37, pp.49–54 and pp.92–100, with smaller separate slips at pp.46 and 119. Physical insertion proves compositeness, not insertion date.

### Material-form closure: selector and revision pages

Former MD-006 priority pages are now directly reviewed:

- **pp.16–20:** interlinear additions, emphasis and strike-throughs cluster where ritual/social/customary determinants are separated from strict moral desert. P.17 particularly emphasizes that suicide/custom violation need not be `moral fault`; p.19 visibly emphasizes the source-critical warning about missionary influence.
- **pp.24–27:** numbered/Roman-numeral schemas visibly convert ethnographic material into distinct afterlife classes, with local deletion/rewrite at category boundaries. P.27 begins an explicit `May 29` entry and brackets a later paragraph.
- **p.67 / p.76 and other secondary checks:** conspicuous local strike-through/interlinear revision confirms active reworking, but deleted wording is not used to reconstruct an unproved conceptual trajectory.
- **p.103:** a branching diagram is embedded inside a developmental hypothesis about cultivated plants, domestic animals and sacrifice and is followed by a chronological objection. Material sequence: `proposed relation → diagram → stress test`.

The proper material conclusion is:

> **005 preserves visible decomposition, reclassification and hypothesis testing, together with multiple inserted source-note layers.**

A strike-through proves revision activity, not the direction of conceptual change unless both deleted and replacement readings are secure. An insert proves accretion, not its date.

### Current research bridge

Working 005→1906 comparison:
- `research_notes/MS38_004_001_061_005_vs_1906_Primitive_Philosophy_working_comparison.md`
- `research_notes/MS38_004_001_061_005_vs_1906_addendum_after_complete_notebook.md`

Current model: **Marillier/EPHE comparative-religion source collection (1898–99) → continued/reused `Hist. Relig.` notebook work documented in 1905 → theoretical condensation around causal efficacy / “primitive energetics” in 1906.** The strongest manuscript signals are decomposition by mechanism, fetish vs charm/amulet, intrinsic vs indwelling-spirit efficacy, transferable blood/body-part power, and p.105’s “quasi-mechanical and magical rather than sacramental.”

### Major source-derived topic blocks

- pp.1–30: future life, death, non-moral vs moral determinants, survival/second death, missionary/contact source criticism.
- pp.31–45: totemism, Hebrew eschatology, `nephesh/ruach`, Greek `psychē/thymos`, comparative teaching outlines; p.44 dated **20 Dec. 1905**.
- pp.46–75: sacrifice typologies, blood/communion, funerary provision, magical vs personal-divine mechanisms, critique of simple evolutionary sequences.
- pp.76–90: messenger/substitution sacrifice, ancestral bargains, circumcision/blood brotherhood, foundation rites, charms/fetishes, transferable efficacy.
- pp.91–105: first fruits, layered ancestor/nature/high-god classifications, agricultural/fecundative sacrifice, chronology of agriculture/domestication, vegetation spirits, quasi-mechanical magical action.
- pp.106–119: cannibalism by mechanism, propitiation vs communion, rejection of circumcision-as-partial-sacrifice, initiation/purification/social-status mechanisms, selected organs as transferable efficacy; sustained argument ends p.119.
- p.120: back-matter memorandum rather than continuation of the main argument.

## 2026-08-27 material-form audit closure

The newly surfaced/rendered PDFs exactly match the source hashes preserved in the original corrected-transcription provenance. The earlier renderer-empty / HTTP 403 state was transient.

Whole-corpus material coverage is now:

- 004: 71/71 visual overview.
- 005: 120/120 visual overview.
- Total: **191/191 pages visually audited at overview level**.
- Argument-sensitive pages: direct/high-resolution second pass complete.

Canonical material files:

- Page ledger: `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`.
- Interpretive closure: `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`.

**MD-006 is closed. There is no remaining archive-side material blocker for the JHI argument.**

## Cross-project research status

The manuscript text and material layers are publication-stable. Current priority is drafting/compression, not another archive sweep.

Core comparisons remain:

1. **004 → 1898 JAOS → 1902 “Religion and the Time-Process”**.
2. **005 Paris/Marillier layer → 005 1905 reuse → 1906 “Primitive Philosophy.”**
3. **005 Hebrew/`Hist. Relig.` layer → 1907 “The Origins of Ethical Inwardness in Jewish Thought.”**

See the canonical live research log: `research_notes/lovejoy_as_orientalist_web_sweep.md`.