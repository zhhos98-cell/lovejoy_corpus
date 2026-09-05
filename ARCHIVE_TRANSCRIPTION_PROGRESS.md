# Lovejoy manuscript transcription progress

Last synchronized: 2026-09-05  
Status: **PAGE COVERAGE 191/191 / 004 ARGUMENT-CONTROL CLOSED BUT NOT DIPLOMATICALLY COMPLETE / 005 DIPLOMATIC TRANSCRIPTION ACTIVE / CANONICAL WITNESS LAYERS RECALIBRATED**

## Authority and method

The archival layer separates four evidence types:

1. `diplomatic_visible_text` — wording secured from the manuscript image;
2. `editorial_argument_summary` — normalized explanation where full diplomatic recovery is not available;
3. `external_source_collation` — comparison with candidate/source text;
4. `material_layout_observation` — diagrams, nesting, numbering, brackets, revisions, slips, foldouts, overlays, blank leaves, and facing-page relations.

These categories are not interchangeable. In particular, `corrected_text` in the clean JSON corpus is heterogeneous. A populated page record may contain direct transcription, readable fragments, or an editorial summary. Therefore:

> **PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION**

A source-supported summary cannot independently prove the source identification that helped produce it. Exact quotation requires the page record and governing direct-image evidence, not the filename suffix alone.

Current protocol: `QUELLENFORSCHUNG_CURRENT_GATE.md`.

Active diplomatic completion queue: `TRANSCRIPTION_COMPLETION_QUEUE.md`.

Integrated human-readable reading surface:

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`

The stable filename contains `final`, but this is not a claim of full diplomatic completion. The twelve paginated JSON batches remain the machine-readable page authority.

**2026-09-05 synchronization warning:** six 005 canonical batches were updated after the currently committed integrated Markdown was last generated. The current connector-only runtime cannot execute the repository generator against the GitHub working tree. Until `python tools/build_integrated_transcription.py` is run again, the integrated Markdown is **stale relative to the canonical JSON** and must not override the page batches.

## 2026-09-05 canonical hygiene pass

The pass did not claim fresh image access or new diplomatic page completion. It propagated already-secured image readings and later source/authorial adjudications into the current page records so that editorial summaries no longer overstate manuscript wording or proposition ownership.

Updated canonical batches:

- `005_p031-045` — explicit diplomatic HOLDs at pp.31–36 and pp.42–43; Marillier collation separated from manuscript text; commit `ce79786a7b35b37c156d2c2d964da4c88734a105`;
- `005_p046-060` — p.55 sex/taste direction and power/value connective returned to HOLD while preserving image-secure classification and male preference; commit `ebeb58c150a108d1b31d89aec9c36be805e0543c`;
- `005_p061-075` — source mechanisms separated from local relations; p.66 W3 jurisdiction relation retained, p.69/p.73 recut; commit `e0bcf54ff56b0de74d40dd540fcc4d81a50ccf60`;
- `005_p076-090` — p.84 and p.90 editorial relation-level overclaims downgraded; commit `0121bfb65bb8f32c5bfb3a3713dc7365a8890615`;
- `005_p091-105` — pp.92–99 explicitly Marillier-mediated by default, p.103 registered as W3 chronology veto, p.104 path control preserved; commit `c75c6c564366daf8340851de46efb7161f1877ab`;
- `005_p106-120` — p.112 strong case adjudication with diplomatic residue, p.117 wording W3/authorship HOLD, p.119 authorship+chronology HOLD; commit `6f9682233d6318fcf1920a60bf74f00568e74dc2`.

No page moved from “first-pass/targeted control” to “diplomatic page complete” solely because of this pass.

## Completion vocabulary

- **Page coverage complete:** every PDF page has a record.
- **First-pass text coverage complete:** every page has some corrected text, readable fragments, or conservative summary.
- **Targeted original-image control:** selected loci were checked directly against the image because they bear on a research proposition or uncertainty.
- **Diplomatic page complete:** the visible manuscript wording has been transcribed as fully as the image permits, with unresolved readings marked.
- **Diplomatic notebook complete:** every nonblank page has reached diplomatic page completion and distinct material layers are represented separately.

Current 191/191 status satisfies the first two conditions, not the last.

## Notebook 004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Source SHA-256: `1ec301a9696949c04acf1c64633377db3fa8c68348d170831b8caa53c561b75f`.
- First-pass text coverage: 71/71.
- Material overview: 71/71.
- Targeted original-image second pass: conceptually closed for the present argument.
- Diplomatic edition status: **incomplete**.
- Remaining limit: micro-paleographic, compressed Pāli/Sanskrit/French, bibliographic, crossed-word, and mixed summary/transcription residue.

Authoritative batches:

- `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`

Current terminal dossiers:

- `research_notes/Lovejoy_original_image_second_pass_cross_notebook_recheck_2026-09-01.md`
- `research_notes/QUELLENFORSCHUNG_round18_residual004_broad005_hygiene_2026-09-01.md`
- `research_notes/MS38_004_round19_direct_image_reference_and_lexical_refinements_2026-09-01.md`

### Stable high-value controls

- p.17/ms p.63: Rhys Davids comparison is actively weighted; generic resemblance is demoted in favor of a relation Lovejoy treats as structurally central.
- p.20/ms p.71: `through a careful analysis (i.e. a comparison of texts)` is image-secure.
- p.29/ms p.89: Childers and Müller are recorded as an interpretive fork around Dhammapada 1 rather than silently harmonized.
- p.33/ms p.97: heading `Upādāna, Relation to Karma`; `Up.`, not `MP`; Hardy p.394 is the immediate visible source attachment.
- p.42/ms p.123: `viññāna is temporally (?) an antecedent of nāma-rūpam, & logically a subdivision of it.`
- p.48/ms p.135: repetition concerns skandha constituents under a collective upādāna designation, not four doctrinal forms of upādāna.
- p.49/ms p.137: `discoverable logical system`, not `technical system`; crossed qualifier remains unresolved.
- pp.49–52: historical origin, logical arrangement, temporal sequence, and scholastic reconciliation are explicitly non-identical problems.
- pp.55–71: high-value references and readable lexical loci were recontrolled against the original images in Rounds 18–19.

The pp.49–52 conceptual blind queue and the p.17/p.29 residual argument-bearing queue are closed for the present argument. This closure does not convert 004 into a complete diplomatic edition.

## Notebook 005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Source SHA-256: `7ebf4e672bdb2267e71a9c6b617df2078f057b1f23858f2770a3f9de004d96ad`.
- First-pass text coverage: 120/120.
- Material overview: 120/120.
- Targeted original-image rechecks: broad pass through Round 20 plus later locus-specific controls.
- Diplomatic edition status: **active and incomplete**.

Authoritative batches:

- `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json`

Current terminal/direct-image dossiers include:

- `research_notes/QUELLENFORSCHUNG_round18b_005_source_evaluation_jurisdiction_and_insert_layers_2026-09-01.md`
- `research_notes/MS38_005_round19_p003-006_moral_natural_purification_direct_image_2026-09-01.md`
- `research_notes/MS38_005_round20_p016-030_contact_sociality_marillier_insert_recheck_2026-09-01.md`
- later Round 23–36 source/authorial adjudications preserved in the frozen 2026-09-05 snapshot and propagated into the canonical page records where they change witness ceilings.

### Known incomplete transcription zones

The clearest first-pass incompleteness remains:

- **pp.31–36:** inserted leaves remain low or low-medium confidence. Canonical records now explicitly distinguish editorial summary from Marillier source collation and mark continuous wording as `DIPLOMATIC HOLD`;
- **pp.42–43:** Greek lexical/textual slips are only partially transcribed and are now explicitly separated from the host-page outline;
- **pp.47–60:** mechanism/source ceilings have been cleaned, but the block still requires a page-by-page diplomatic second pass once the image is directly visible.

After these blocks, the rest of 005 still requires systematic full-page diplomatic completion. The 2026-09-05 hygiene pass reduces false confidence in pp.61–120; it does not replace that work.

### Current image-access constraint

The split original scans are present in the user's Library, but the 2026-09-05 reading channel returned no rendered page pixels and materialization failed with 403. No fresh direct-image transcription was claimed under that condition. Source collation and OCR remain prohibited as substitutes for the hand.

### Provenance and material chronology

005 is physically accretive and longitudinal, not a single-date object. Direct headings include `May 29`, `Marillier — Survivance — 12 June`, `Marillier — June 13 — Sacrifice`, `Marillier ... June 20`, and `Hist. Relig. — Dec. 20, 1905.` These date local sheets/pages only. Physical insertion proves accretion, not insertion date.

Major inserted/foldout regions occur around pp.29–37, pp.49–54, and pp.92–100, with smaller slips elsewhere. Host-page continuity and inserted-text continuity must be reconstructed separately.

### Stable high-value controls after the 2026-09-05 recut

- pp.3–6: afterlife continuity of status/power is distinct from moral recompense; analytic natural/supernatural division is distinguished from the actor's classification.
- pp.16–19: missionary intercourse and borrowed notions are treated as provenance/contact problems.
- pp.29–30: inserted Marillier survivance sheets are distinct physical witnesses; `survivance != immortality` remains a local problem, not a teacher-origin claim.
- pp.31–36: source packets are narrowed by Marillier collation, but manuscript wording remains diplomatically open.
- pp.42–43: host outline readable; Greek loose slips remain incomplete.
- p.49: Tylor is explicitly praised as the one who does not construct theories beyond his evidence.
- p.53: sacrifice may operate as purely mechanical compulsion in which divine will is not the relevant mechanism.
- p.55: W3 only for `not ritual but alimentary`, male-flesh preference, and existence of a male/female gastronomic contrast; exact taste direction/source boundary/power-value connective HOLD.
- p.64: magical sacrifice is differentiated into technical contest with personal gods and direct action on natural forces; general mechanical-magic grammar remains field-owned.
- p.65: W3 `delicate analysis` / dissociation of mingled elements.
- p.66: W3 mechanism -> competent social bearer/jurisdiction relation.
- p.69: W3 animal-not-advancement and animal->human substitution direction; direction itself belongs to the Robertson-Smith field.
- p.73: W3 `another meaning` reinterpretation; object-soul and survivance mechanisms are source-field owned.
- p.84: foundation-sacrifice packet present, but old Lovejoy-authored anti-union decomposition withdrawn pending exact syntax; source field strongly prefigures the decomposition.
- p.90: guardian-spirit localization and gateway-blood packets are source-closed; exact Lovejoy relation between them and the old `turning of a key` wording remain HOLD.
- pp.92–99: explicit Marillier-mediated insert regime; no current W3 Lovejoy-local intervention recovered inside the packet.
- p.103: W3 `involves a vicious circle` and cross-domain agriculture/domestication chronology veto; underlying economic facts are field-owned.
- p.104: W3 human-sacrifice -> domestic-animal route and rejection of direct wild-animal -> domestic-animal derivation.
- p.112: strong case-level rejection/preference relation between partial-sacrifice genealogy and initiation/incorporation mechanism; exact rejection wording/source cue remains diplomatic residue.
- p.117: ranked distribution wording is W3; exact proposition authorship remains HOLD.
- p.119: W2–W3 selected-organ and `perh. as a repr. of the whole body` wording; undated late-insert chronology prevents treating the juxtaposition as a secure Lovejoy-origin A2 fork.
- p.120: scheduling/back-matter fragments are physically distinct from the sustained argument.

## Machine-readable audit trails

- `archive_transcriptions/MS38_004_001_061_004_round17_direct_image_deltas_p042_p049-052_2026-09-01.json`
- `archive_transcriptions/MS38_004_005_round18_direct_image_deltas_2026-09-01.json`
- `research_notes/MS38_004_005_transcription_corrections_round17_original_image_2026-09-01.csv`
- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`

Where a delta is marked merged, the paginated clean batch is again the active page authority and the delta remains the audit trail.

## Current next action

Follow `TRANSCRIPTION_COMPLETION_QUEUE.md`.

When direct image access is available, start with **pp.31–36**, then **pp.42–43**, then **pp.47–60**. Continue afterward through the remaining blocks page by page. The next pass should be paleographic/diplomatic, not another thematic source sweep.

When repo-shell access is available, regenerate and verify the integrated reading surface before treating it as synchronized:

```bash
python tools/build_integrated_transcription.py
python tools/build_integrated_transcription.py --check
python tools/audit_repository.py
```

For 004, retain argument-control closure for current research while recording that a complete diplomatic edition remains a separate future task.
