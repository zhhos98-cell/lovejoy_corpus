# Lovejoy manuscript transcription progress

## Working method

Manuscript notebooks are corrected in batches of 15–20 PDF pages against the page images. PaddleOCR-VL is used only as a scaffold. The corrected JSON preserves Lovejoy's abbreviations where readable, marks uncertain/illegible readings explicitly, records visible manuscript page labels, and keeps source PDF/OCR SHA-256 values so each batch is auditable.

## MS38_004_001_061_004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Completed: PDF pp. 1–36.
- GitHub batches:
  - `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
- Batch 2 visible manuscript page labels: 67, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103. (The scan images are spreads, so the visible right-hand label is not a one-to-one PDF-page counter.)
- Next batch if resumed: PDF pp. 37–54.
- First-pass uncertainties remain explicitly marked rather than silently reconstructed. In batch 2 the most difficult passages are p. 20 on the interrelation of the nidanas, p. 27 lower-right nāmarūpa commentary, p. 29 Childers/viññāṇa commentary, p. 30 source details around avijjā, p. 31 the short “Relation to F. Truths” paragraph, and one analytical sentence on p. 32.

### Source-derived topics in pp. 1–18

- Sankhya method and sources of knowledge: pramana, perception, syllogism, testimony.
- Buddhist “agnosticism” and refusal/indifference toward speculative questions.
- Flux, impermanence, becoming, and the continuity problem.
- Lovejoy's chronological question about the priority/relationship of Sankhya and Buddhism.
- Brahma-jala / Digha-Nikaya classification of sixty-two heresies.
- Comparison of Sankhya dualism with early Buddhist formulations concerning self, world, soul/body, and future life.

### Source-derived topics in pp. 19–36

- Paticca-samuppada / dependent origination becomes the organizing problem: Lovejoy explicitly treats the twelve nidanas as the technical working-out of Buddhism’s general philosophical position.
- The nidanas are decomposed term by term: birth, bhava, upadana, tanha, sensation, contact, ayatana, namarupa, consciousness, sankhara, and avijja.
- PDF p. 27 contains a diagram mapping consciousness → namarupa → sense-organs → contact → sensation → desire across the six sensory channels.
- Lovejoy repeatedly compares Warren, Childers, Oldenberg, Rhys Davids, Buddhaghosa, Hardy, and Hopkins rather than relying on a single authority; the notebook is visibly a comparative philological working apparatus.
- He asks how the nidana chain relates to the Four Truths and whether direct/reverse causal order can substitute for their formulation.
- Karma and the khandhas become a problem of continuity and identity: khandhas perish, karma carries causal continuity, and Nirvana raises the question of whether annihilation applies merely to the aggregates or to existence itself.

## MS38_004_001_061_005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Completed: PDF pp. 1–15.
- GitHub batch: `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
- Visible manuscript page labels securely or provisionally recorded in this batch: 3 [?], 5 [?], 7, 9, 11, 13, 15, 17, 19, 23 [?], 25, 27, 29.
- Next batch: PDF pp. 16–30.
- Correction policy on especially difficult pages (8–14): preserve readable argumentative structure and source names; use `[illegible]` / `[?]` rather than silently supplying ethnographic names or myth details from outside knowledge.

### Source-derived topics in pp. 1–15

- Future-life beliefs initially treated as continuations of this-worldly status rather than inherently moral reward/punishment.
- Distinction between moral, magical, ritual, social/community, and status-based determinants of post-mortem destiny.
- Modes of death (suicide, drowning, childbirth) as independent determinants of post-mortem destinations.
- Death among “non-civilized” peoples treated in the notebook as something requiring an extraordinary/supernatural causal explanation rather than as an intrinsically natural necessity.
- Origin-of-death myths: failed rejuvenation, mistaken messages, taboo breaking, hostile spirits, and the Hesiod/Pandora example.
- Ethnographic reading notes drawing on Wyatt Gill, Brough Smyth, Codrington, Duff MacDonald, and Rink.
- PDF pp. 14–15 contain an explicit analytic outline moving from naturalistic continuity, through ritual and social determinants, toward strictly moral guilt.
