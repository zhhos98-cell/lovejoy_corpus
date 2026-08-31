# Lovejoy manuscript transcription progress

Last synchronized: 2026-08-31  
Status: **004 71/71 FIRST PASS + SELECTIVE ROUND-16 IMAGE CORRECTIONS / 005 120/120 FIRST PASS + SELECTIVE ROUND-16 IMAGE CORRECTIONS / MATERIAL 191/191 OVERVIEW CLOSED**

## Working method and authority split

The archival layer has four distinct evidence types:

1. `diplomatic_visible_text` — manuscript wording secured from page images;
2. `editorial_argument_summary` — normalized explanation where the hand is too difficult for full diplomatic recovery;
3. `external_source_collation` — comparison with candidate/source text;
4. `material_layout_observation` — diagrams, spatial nesting, numbering, brackets, insertions, strike-throughs, slips/foldouts and facing-page relations.

These must not be collapsed. In particular, `corrected_text` in older `*_clean.json` entries is heterogeneous: some entries are close diplomatic transcriptions; others are source-supported argumentative summaries. A source-supported summary cannot serve as independent evidence for the source identification that helped produce it.

Current source-critical policy is governed by `QUELLENFORSCHUNG_CURRENT_GATE.md`.

## MS38_004_001_061_004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Source SHA-256: `1ec301a9696949c04acf1c64633377db3fa8c68348d170831b8caa53c561b75f`.
- Text coverage: **71/71 first pass complete**.
- Material coverage: **71/71 visual overview complete; selected high-value pages directly/high-resolution reviewed**.
- Round-16 propagation: **p.41–42 material/text distinction written back into the clean transcription batch**.

Batches:

- `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`

### Image-secure benchmark: pp.41–42

PDF p.41 contains a large diagram mapping dependent-origination / `nāmarūpa` relations against the khandhas. PDF p.42 / manuscript p.123 directly shows the hierarchy:

`nāmarūpa → rūpam / nāma → vedanā / saññā / saṅkhārā / viññāṇam`

Immediately below, the image-secure key sentence reads:

`Viññāṇa is temporally (?) antecedent to nāmarūpa and logically a subdivision of it.`

The clean JSON now records the sentence, the diagram and the material-layout observation separately. No visible erasure creates the contrast. Safe claim: the page materially holds classificatory inclusion apart from temporal priority. This is a local working practice, not an origin claim about the later history-of-ideas method.

### Remaining 004 text-hygiene queue

The remaining work is concentrated, not a new whole-notebook transcription:

- p.6/MS21 Sabbāsava source heading/page notation;
- p.8/MS25 Siṃsapā source string and conjectured `Oldenberg 204 f.`;
- pp.12–16 Rhys Davids 1896 start/end source marks;
- p.17 punctuation around `To R.D.'s remark it should be added`;
- p.18 practical-agnosticism paragraph;
- p.20 `present effort` paragraph;
- p.22 Warren `identity` sentence punctuation;
- p.29 Childers/Müller source numerals and transition;
- p.33 Hardy p.394 fact/manner grammar;
- pp.47–52 Senart/Oldenberg source and quotation boundaries plus compressed Pāli/Sanskrit forms.

Published-paper cross-read remains `research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md`.

## MS38_004_001_061_005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Source SHA-256: `7ebf4e672bdb2267e71a9c6b617df2078f057b1f23858f2770a3f9de004d96ad`.
- Text coverage: **120/120 first pass complete**.
- Material coverage: **120/120 visual overview complete; former MD-006 priority pages directly/high-resolution reviewed**.
- Round-16 propagation: **pp.78–80, pp.85–86, p.117 and p.119 corrected/annotated in the clean JSON batches**.

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

005 is a physically accretive, longitudinal notebook rather than a single-date object.

- strong Paris 1898–99 core, with EPHE/Marillier course alignment and documented active participation by Lovejoy;
- direct page headings/anchors include `May 29`, `Marillier — Survivance — 12 June`, and `Hist. Relig. — Dec. 20, 1905.`;
- p.44's 1905 heading dates p.44 only;
- major inserted/foldout layers occur approximately pp.29–37, pp.49–54 and pp.92–100, with smaller slips at pp.46 and p.119;
- physical insertion proves accretion, not insertion date.

### Material-form benchmarks

- pp.16–20: revisions/emphasis cluster at the boundary between ritual/social/customary determinants, strict moral desert and missionary-source criticism;
- pp.24–27: numbered/Roman-numeral schemas convert ethnographic material into explicit classes and locally revise their boundaries;
- p.103: developmental proposal → branching diagram → chronology/vicious-circle stress test.

### Round-16 transcription corrections now propagated

**p.78 / MS157**

Manuscript source line frozen as `Trumbull, "Blood-Covenant" 2?`. The uncertain numeral is not expanded from external content matching. External pp.268f/299 remain collation loci only.

**pp.79–80 / MS159–161**

Image-secure strings now in the clean transcription include:

- `Translation of Zulu prayer given by Lewis Grout, q.v.`;
- `F. prayer ... a veritable bargain`;
- `not "Give me & I will give you F. cow afterwards"`;
- `notion of substitution, like scape-goat`;
- `May F. cow carry away F. evil wh. is in me.`

This corrects the former normalized chronology: the manuscript explicitly contrasts the rite with a simple deferred-payment formula.

**pp.85–86 / MS173–175**

Exact source anchors now image-secure in the clean JSON:

- `V. Trumbull Blood Cov't 118.`
- `(quot. Trumbull p.129)`

These bracket a strong sequential-reading inference through Trumbull pp.118–129. Intervening clauses remain mixed diplomatic/editorial unless independently re-read.

**p.117**

The clean summary has been replaced by image-secure ranked wording. The page distinguishes `gt. number of cases` alimentary/anthropophagic, `next most numerous cases` expiatory/propitiatory, and states `A human sacrifice for union is altogether exceptional`. One following comparative clause remains illegible.

**p.119**

The prior neat organ-quality arrows are withdrawn. The page supports a `specific virtue or force` mechanism, some visible part/function associations, uncertainty about others, and an explicit alternative in which the selected part stands `as a repr. of [the] whole body`. A separate right-hand slip remains physically/textually separate.

### Remaining 005 text-hygiene queue

- pp.3–6 local Lovejoy wording versus Marillier/programme language;
- p.10 `American Legends, V. [Brinton?]` and Yarrow/Powers marks;
- p.11 exact Rink wording/page references;
- p.27 / p.29 / p.47 headings + first paragraphs where local wording matters;
- p.62 exact Brinton item after `art.`;
- p.89 exact Kingsley page/reference run;
- p.103 exact authorities/source marks around the already image-secure diagram.

## 191-page material closure and current access state

The 2026-08-27 material audit remains canonical for page form:

- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`.

Coverage remains **191/191 overview**. The newly re-supplied split witnesses are present at full coverage. In the current execution environment their page-image channel returns `Image unavailable` and raw-byte materialization is not authorized; therefore no fresh line reading is invented from an inaccessible render. Existing Round-16 corrections derive from earlier direct/high-resolution image controls already recorded in the repository. The residual queue is left explicitly open until blind pixels are available.

## Current archive state

**004 71/71 + 005 120/120 FIRST PASS COMPLETE / MATERIAL 191/191 OVERVIEW COMPLETE / ROUND-16 IMAGE-SECURE DELTAS PROPAGATED / LAYOUT TREATED AS INDEPENDENT EVIDENCE / REMAINING WORK = SMALL BLIND PALEOGRAPHY QUEUE, NOT A NEW ARCHIVE SWEEP.**
