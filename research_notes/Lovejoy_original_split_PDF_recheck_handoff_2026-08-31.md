# Lovejoy original split-PDF recheck handoff — 2026-08-31

## Purpose

Record the newly re-supplied original scan witnesses for notebooks `MS38_004_001_061_004` and `MS38_004_001_061_005`, and fix the next archive-side execution order without disturbing the already publication-stable corrected transcription layer.

## Source packets now in the active conversation

### `MS38_004_001_061_004` — “Sankhya + Buddhism”

- `MS38_004_001_061_004_1-36.pdf` — global PDF pp. 1–36
- `MS38_004_001_061_004_37-71.pdf` — global PDF pp. 37–71
- coverage: **71/71 pages**

### `MS38_004_001_061_005` — faint front-leaf title “Symbolism” [?]

- `MS38_004_001_061_005_1-40.pdf` — global PDF pp. 1–40
- `MS38_004_001_061_005_41-80.pdf` — global PDF pp. 41–80
- `MS38_004_001_061_005_81-120.pdf` — global PDF pp. 81–120
- coverage: **120/120 pages**

Combined active original-image coverage: **191/191 pages**.

These are split delivery packets of the two notebook witnesses, not new conceptual sources. Split-file SHA-256 values have not yet been recorded; do not invent or back-fill them from the whole-PDF hashes already stored in the transcription provenance.

## Governing repo state before this refresh

The existing archival layer remains authoritative until a page-level original-image recheck proves a correction:

- 004 corrected transcription: **71/71, first pass complete**;
- 005 corrected transcription: **120/120, first pass complete**;
- material-form overview: **191/191 complete**;
- corrected-text authority: `archive_transcriptions/*_clean.json`;
- material-form authority: `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- interpretive closure: `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`.

The new upload therefore changes **witness availability**, not the current substantive argument state. No existing reading should be silently replaced merely because the scans have been re-supplied.

## Recheck protocol

1. Use the newly supplied split PDFs as the governing visual witness for the second pass.
2. Compare page-by-page against the relevant `*_clean.json` entry.
3. Prioritize entries already marked `low`, `low-medium`, or `medium`, plus publication-sensitive technical terms, names, dates, page references, and quotations.
4. Preserve Lovejoy’s abbreviations and spelling where legible. Do not modernize Pāli/Sanskrit or ethnographic names silently.
5. Any correction to a transcription must be traceable to a specific global PDF page and, where present, manuscript page label.
6. Keep material evidence separate from corrected text. Strike-through, insertion, spatial nesting, paper format, and diagram structure may calibrate an argument but must not silently alter the textual transcription.
7. Keep interpretation separate again: an improved reading can license a stronger or weaker historical claim only after the textual correction is independently secured.

Compact evidence rule:

`ORIGINAL IMAGE -> SECURE READING -> TRANSCRIPTION CORRECTION -> INTERPRETIVE CONSEQUENCE`

Never reverse that sequence.

## High-value page mapping inside the split packets

### Notebook 004

- global p.42 / ms p.123, the `viññāṇa` / `nāma` / `nāmarūpa` relation page, is **local p.6** of `MS38_004_001_061_004_37-71.pdf`.
- global pp.37–54, the dependent-origination → khandha → `upādāna/upadhi` block, occupy **local pp.1–18** of the same packet.

This remains the strongest manuscript control for holding classificatory inclusion apart from temporal priority.

### Notebook 005

- global p.44, the directly dated `Hist. Relig. — Dec. 20, 1905.` page, is **local p.4** of `MS38_004_001_061_005_41-80.pdf`.
- global p.103, the branching developmental-hypothesis diagram followed by a chronology objection, is **local p.23** of `MS38_004_001_061_005_81-120.pdf`.
- global p.119, the end of the sustained main argument, is **local p.39** of `MS38_004_001_061_005_81-120.pdf`.
- global p.120, back-matter memorandum, is **local p.40** of that packet.

## Immediate execution order

### Pass A — 004 textual verification

Start with existing uncertain clusters rather than rereading high-confidence prose indiscriminately:

- pp.6–8: Sabbāsava / Sutta Nipāta source lines and technical vocabulary;
- pp.12–18: Sāṁkhya/Buddhist priority, Brahmajāla classification and Rhys Davids cross-reading;
- pp.37–54: low/medium-confidence technical and bibliographic readings around causal series, khandhas, `viññāṇa`, `upādāna/upadhi`, Senart, `saṅkhāra`, and `āsava`;
- then remaining marked uncertain readings in pp.19–36 and pp.55–71.

### Pass B — 005 textual verification

Recheck marked uncertainty by topic cluster:

- future-life / missionary-source criticism;
- sacrifice and blood/body-part efficacy;
- charms/fetishes and intrinsic vs indwelling efficacy;
- agricultural/fecundative sacrifice and chronology;
- cannibalism, initiation, purification, social-status mechanisms;
- all exact ethnographic names, French/German titles, source-page numerals and dates needed for publication quotation.

### Pass C — source-to-publication bridge

Only after secure textual deltas are logged, rerun the two principal bridges:

1. `004 -> 1898 JAOS -> 1902 Religion and the Time-Process`;
2. `005 Paris/Marillier -> 1905 reuse -> 1906 Primitive Philosophy`.

The current anti-origin firewall remains active: notebook evidence may demonstrate working relations, source uptake, decomposition, reclassification and hypothesis testing; it does not by itself establish a single-source origin of Lovejoy’s mature method.

## Current status after sync

**ORIGINAL SPLIT WITNESSES PRESENT / 191-PAGE COVERAGE CLOSED / SECOND-PASS TEXTUAL RECHECK READY / NO NEW ARGUMENT CLAIM YET.**

Next archive action: execute the original-image verification pass and write only page-specific deltas back into the corresponding transcription or research-note files.