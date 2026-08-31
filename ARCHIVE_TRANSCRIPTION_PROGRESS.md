# Lovejoy manuscript transcription progress

Last synchronized: 2026-09-01  
Status: **004 71/71 FIRST PASS + ROUND-16 PROPAGATED + ROUND-17/17B ORIGINAL-WITNESS DELTAS + P.37-54 CLEAN MERGE / 005 120/120 FIRST PASS + ROUND-16 PROPAGATED + ROUND-17 ORIGINAL-WITNESS DELTAS / MATERIAL 191/191 OVERVIEW COMPLETE**

## Working method and authority split

The archival layer has four distinct evidence types:

1. `diplomatic_visible_text` — manuscript wording secured from page images;
2. `editorial_argument_summary` — normalized explanation where the hand is too difficult for full diplomatic recovery;
3. `external_source_collation` — comparison with candidate/source text;
4. `material_layout_observation` — diagrams, spatial nesting, numbering, brackets, insertions, strike-throughs, slips/foldouts and facing-page relations.

These must not be collapsed. In particular, `corrected_text` in older `*_clean.json` entries is heterogeneous: some entries are close diplomatic transcriptions; others are source-supported argumentative summaries. A source-supported summary cannot serve as independent evidence for the source identification that helped produce it.

Current source-critical policy is governed by `QUELLENFORSCHUNG_CURRENT_GATE.md`. Round-17 exact quotation deltas are governed by:

- `research_notes/QUELLENFORSCHUNG_round17_original_witness_verification_2026-09-01.md`;
- `research_notes/QUELLENFORSCHUNG_round17b_004_p042_p049-052_direct_image_2026-09-01.md`;
- `research_notes/MS38_004_005_transcription_corrections_round17_original_image_2026-09-01.csv`;
- `archive_transcriptions/MS38_004_001_061_004_round17_direct_image_deltas_p042_p049-052_2026-09-01.json`;
- `research_notes/MS38_004_round17c_p049-052_material_page_form_addendum_2026-09-01.md` for the page-form and clause-layout addendum.

Where a Round-17 delta has been merged into a `*_clean.json` batch, that clean batch is again the active text authority and the delta register remains its audit trail. Unmerged loci continue to be governed by the dossier/ledger.

## MS38_004_001_061_004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Source SHA-256: `1ec301a9696949c04acf1c64633377db3fa8c68348d170831b8caa53c561b75f`.
- Text coverage: **71/71 first pass complete**.
- Material coverage: **71/71 visual overview complete; selected high-value pages directly/high-resolution reviewed**.
- Round-16 propagation: **p.41–42 material/text distinction written back into the clean transcription batch**.
- Round-17/17b propagation: **p.48 substantive skandha-recurrence correction plus p.42 and pp.49–52 direct-image wording/material controls are now merged into `MS38_004_001_061_004_p037-054_clean.json`.**
- Round-17 renewed originals: **p.6, p.8, pp.12–14, p.18, p.20, p.22, p.33, pp.47–52 directly re-read; several former blind loci upgraded to W3.**

Batches:

- `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`

### Stable benchmark: pp.41–42

PDF p.41 contains the diagrammatic mapping of dependent-origination / `nāmarūpa` relations against the khandhas. PDF p.42 / manuscript p.123 directly shows the hierarchy:

`nāmarūpam → rūpam / nāma → vedanā / saññā / saṅkhārā / viññāṇam`

Immediately below, the image-secure diplomatic key sentence now merged into the clean batch reads:

`viññāna is temporally (?) an antecedent of nāma-rūpam, & logically a subdivision of it.`

Safe claim: the page materially holds classificatory inclusion apart from temporal priority. This is a local working practice, not an origin claim about the later history-of-ideas method.

### Round-17 004 witness deltas

- **p.6/MS21**: W3 for `Buddh. Agnosticism`, `Sabbāsava Sutta of F. Maj. Nik.`, and quotation onset; overwritten explanatory line stays W2.
- **p.8/MS25**: major upgrade. Direct image reads `v. Oldenberg p. 204 — Gotama + leaves of Simsapa-wood.` The former `Oldenberg 204` conjecture is now manuscript evidence.
- **pp.12–14/MS53–57**: W3 source-run start `Rhys Davids on Contemp. Date of Sankhya & Buddhism.` / `Am. Lect.: Buddhi., p. 24.`; p.14 right begins a visibly new underlined/numbered section, giving the local material endpoint of the continuous run.
- **p.18/MS65**: W3 for the opening practical-agnosticism reweighting, including `not a necessary interpretation`.
- **p.20/MS71**: W3 programme frame `The most that can be hoped for in F. present effort is ...` plus `through a careful analysis + comparison of texts;`; middle phrase stays partly uncertain.
- **p.22/MS75**: W3 Warren attribution to `identity` and Lovejoy's `But not so` objection.
- **p.33/MS97**: W3 Hardy grammar: `fact of continued existence` versus `manner of continued existence?`, `Hardy, p.394`; visible question mark retained.
- **p.48/MS135**: original-image recheck corrects the first-pass object of repetition. The page is testing recurrence of skandha constituents under a collective `upādāna` designation, not enumerating the four doctrinal forms of `upādāna`; this correction is merged.
- **p.49/MS137**: direct wording corrects `discoverable technical system` to **`discoverable logical system`**. `homogeneous` is visibly inserted over the first right-leaf line; the following qualifier is struck/overwritten, so `strict temporal relation` is withdrawn as diplomatic wording. The anti-Senart clauses `illogical & unintelligible`, `jumbled together`, and `repetitions are intentional` are W3. These controls are merged.
- **p.50/MS139**: W3 anchors for `not merely a double but a triple enumeration`, `Namarupa ... a collective designation`, and `precede both temporally as well as logically`. The facing right leaf is almost entirely blank, now recorded as page-form evidence of an abrupt thought-block closure. These controls are merged.
- **p.51/MS141**: W3 for `Nidānas:`, the Senart p.285 quotation onset, the `very practical & natural` / `ontological function` contrast, and the explicitly initialled question `But is tre necessarily any ontological function involved? A.O.L.`. The `A.O.L.` marker is an image-secure author/source seam and is now recorded in the clean batch.
- **p.52/MS143**: W3 for `the whole enumeration is secondary as to origin & composite as to character`, the standalone pivot `And what of namarupa?`, `scholastic expedient, without warrant`, and the closing `theory, conceived all of a piece` phrase. The page visibly decomposes the problem into modules and ends with substantial blank space; these controls are merged.

### Remaining 004 text-hygiene queue

The high-value blind queue is now narrow:

- p.17 exact new-witness location/punctuation around `To R.D.'s remark it should be added`;
- p.29 Childers/Müller exact source numerals and transition grammar;
- pp.49–52 only **micro-paleographic** residue remains: the crossed p.49 qualifier and compressed Pāli/Sanskrit middle clauses if a fully diplomatic line-by-line edition or verbatim publication quotation requires them.

The conceptual blind queue for pp.49–52 is closed. Published-paper cross-read remains `research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md`.

## MS38_004_001_061_005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Source SHA-256: `7ebf4e672bdb2267e71a9c6b617df2078f057b1f23858f2770a3f9de004d96ad`.
- Text coverage: **120/120 first pass complete**.
- Material coverage: **120/120 visual overview complete; selected high-value pages directly/high-resolution reviewed**.
- Round-16 propagation: **pp.78–80, pp.85–86, p.117 and p.119 corrected/annotated in the clean JSON batches**.
- Round-17 renewed originals: **p.10, p.11, p.62, pp.89–90 directly re-read; one prior bibliographic expansion withdrawn.**

Batches:

- `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json`

### Provenance/material chronology

005 remains a physically accretive, longitudinal notebook rather than a single-date object.

- strong Paris 1898–99 core, with EPHE/Marillier course alignment and documented active participation by Lovejoy;
- direct page headings/anchors include `May 29`, `Marillier — Survivance — 12 June`, and `Hist. Relig. — Dec. 20, 1905.`;
- p.44's 1905 heading dates p.44 only;
- major inserted/foldout layers occur approximately pp.29–37, pp.49–54 and pp.92–100, with smaller slips at pp.46 and p.119;
- physical insertion proves accretion, not insertion date.

### Round-16 propagated benchmarks

- **p.78/MS157**: `Trumbull, "Blood-Covenant" 2?`; external pp.268f/299 remain collation loci only.
- **pp.79–80/MS159–161**: `Translation of Zulu prayer given by Lewis Grout, q.v.`, `veritable bargain`, anti-deferred-payment formula, `notion of substitution, like scape-goat`, and `May F. cow carry away F. evil wh. is in me.` are image-secure.
- **pp.85–86/MS173–175**: exact anchors `V. Trumbull Blood Cov't 118.` and `(quot. Trumbull p.129)` bracket the sequential-reading inference.
- **p.117**: ranked distributional synthesis is W3: greatest number alimentary/anthropophagic; next most numerous expiatory/propitiatory; `A human sacrifice for union is altogether exceptional`.
- **p.119**: prior neat organ-quality arrows withdrawn; image supports `specific virtue or force`, some part/function associations, uncertainty about others, and part-as-representative-of-whole.

### Round-17 005 witness deltas

- **p.10/MS17**: direct line `American Legends, v. Brint.` The manuscript field is frozen at `Brint.` rather than silently expanded.
- **p.11/MS19**: W3 for `V. Rink`, `Tales & Traditions of F. Eskimos`, and `p. 36-37`; intervening imprint/parenthetical remains W2.
- **p.62/MS125**: major correction. Direct image reads `Enc. Brtt. art. [overwritten/illegible], for good bibliography & fair sketch of subject.` Earlier `Brinton, article [title uncertain]` expansion is withdrawn. The title position is physically overwritten and remains unrecovered.
- **pp.89–90/MS181–183**: Kingsley page-run is now W3 at the manuscript level: `Kingsley, Travels of W. Afr. 511` and later `Miss Kingsley ... 525`.

### Remaining 005 text-hygiene queue

- pp.3–6 local Lovejoy wording versus Marillier/programme language;
- p.27 / p.29 / p.47 headings + first paragraphs where local wording matters;
- p.103 exact authorities/source marks around the already image-secure diagram.

## 191-page material closure and current access state

The 2026-08-27 material audit remains canonical for its recorded page-form inspection level:

- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`.

Coverage remains **191/191 overview**. The newly re-supplied split witnesses are now directly readable at page-image level in the active execution environment. The former `Image unavailable` blocker is lifted. Fresh line readings must still be recorded page by page; overview-level review is never promoted silently into diplomatic transcription.

## Current archive state

**004 71/71 + 005 120/120 FIRST PASS COMPLETE / MATERIAL 191/191 OVERVIEW COMPLETE / ROUND-16 IMAGE-SECURE DELTAS PROPAGATED / ROUND-17B P.42 + PP.49-52 CLEAN MERGE COMPLETE / P.48 SKANDHA-RECURRENCE CORRECTION MERGED / p.49 `LOGICAL SYSTEM` SECURE / p.51 `A.O.L.` AUTHOR-SEAM SECURE / 004 CONCEPTUAL BLIND QUEUE PP.49-52 CLOSED / p.62 `BRINTON` OVER-EXPANSION WITHDRAWN / NEXT = RESIDUAL P.17 + P.29 VERIFICATION OR PAPER-CENTERED 004 -> 1898 -> 1902 CROSS-READ.**
