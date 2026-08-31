# Quellenforschung Round 16 — transcription propagation + layout gate

Date: 2026-08-31  
Status: **IMAGE-SECURE DELTAS PROPAGATED / RESIDUAL BLIND PALEOGRAPHY QUEUE ONLY**

## Purpose

This note closes the propagation stage after the Round-15 source-critical recalibration and the Round-16 original-image rechecks. The task is no longer to infer sources from a fluent `corrected_text` field. It is to keep four evidence layers distinct:

1. `diplomatic_visible_text`;
2. `editorial_argument_summary`;
3. `external_source_collation`;
4. `material_layout_observation`.

The fourth layer is mandatory because page layout is itself an analytical object: diagrams, spatial nesting, numbering, marginal additions, strike-throughs, facing-page relations, slips and foldouts can record an operation that prose transcription alone obscures.

## Propagated transcription corrections

### 004 p.42 / MS p.123

`archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json` now separates the image-secure relation from upper-page editorial context.

Image-secure content:

- hierarchical diagram: `nāmarūpa → rūpam / nāma → vedanā / saññā / saṅkhārā / viññāṇam`;
- key sentence: `Viññāṇa is temporally (?) antecedent to nāmarūpa and logically a subdivision of it.`

Material observation is now explicit: the diagram spatially nests `viññāṇa` inside `nāma/nāmarūpa`, while the immediately adjacent prose assigns temporal antecedence. No visible erasure creates the contrast. The page therefore holds relation-types apart materially as well as verbally. This remains a local notebook operation, not an originality claim.

### 005 p.78 / MS p.157

`archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json` now freezes the manuscript citation as:

`Trumbull, "Blood-Covenant" 2?`

The numeral is not expanded. External p.268f/p.299 content loci remain in `external_source_collation` only.

### 005 pp.79–80 / MS pp.159–161

The clean JSON now carries the image-secure Grout source seam and Lovejoy's own visible transactional/substitution language:

- `Translation of Zulu prayer given by Lewis Grout, q.v.`;
- `F. prayer ... a veritable bargain`;
- `not "Give me & I will give you F. cow afterwards"`;
- `notion of substitution, like scape-goat`;
- `May F. cow carry away F. evil wh. is in me.`

This corrects the earlier normalized chronology in which the cow could be read as payment promised after cure. The manuscript explicitly rejects that simple deferred-payment formula.

### 005 pp.85–86 / MS pp.173–175

Exact image-secure Trumbull anchors are now in the clean JSON:

- p.85: `V. Trumbull Blood Cov't 118.`;
- p.86: `(quot. Trumbull p.129)`.

The intervening material still supports a strong sequential-reading inference through Trumbull pp.118–129, but the exact anchors and the surrounding argumentative summaries are now kept as different evidence layers.

### 005 p.117

The former editorial summary has been replaced by image-secure ranked wording. The key distribution is not three coequal bins:

- `in gt. number of cases` → alimentary / anthropophagic;
- `next most numerous cases` → expiatory & propitiatory;
- `A human sacrifice for union is altogether exceptional`.

The immediately following comparative clause remains partly illegible and stays marked rather than normalized.

### 005 p.119

The former clean arrow-set `head/brain → intelligence; heart → courage/life; sexual organs → sexual power` has been withdrawn. The image supports a weaker and more interesting mechanism:

- selected flesh/body parts may carry a `specific virtue or force`;
- some part/function associations are visible, especially head/frontal bone and intelligence;
- Lovejoy says the reason for other selections is `not entirely clear`;
- he considers the alternative that a part functions `as a repr. of [the] whole body`, allowing the eater to acquire the force of the eaten.

The physically separate right-hand slip remains outside the cannibalism transcription.

## Layout evidence retained as an independent layer

The 2026-08-27 direct material audit remains the governing material witness for the whole 191-page corpus. Its strongest controls remain:

- 004 pp.41–42: facing/cross-system diagram sequence culminating in the `viññāṇa` relation contrast;
- 005 pp.16–20: revision/emphasis concentrated at the moral/non-moral/custom/source-critical boundary;
- 005 pp.24–27: numbered/Roman-numeral schemas and local category-boundary revisions;
- 005 pp.29–37, pp.49–54, pp.92–100 plus slips at pp.46/119: physical accretion and inserted source-note layers;
- 005 p.44: `Hist. Relig. — Dec. 20, 1905.` as a local date only;
- 005 p.103: developmental proposal → branching diagram → chronology/vicious-circle stress test.

The governing material rule is unchanged:

> A strike-through proves revision activity, not the direction of conceptual change unless deleted and replacement wording are both secure. An insert proves accretion, not its date. A diagram proves a spatial/classificatory act, not by itself a general method.

## Residual original-image queue

The source-critical architecture is now stable, but several exact lexical items still require blind high-resolution rereading before they can be upgraded. They are intentionally retained rather than source-normalized:

### 004

- p.6/MS21 Sabbāsava source heading/page notation;
- p.8/MS25 Siṃsapā source string and the conjectured `Oldenberg 204 f.`;
- pp.12–16 Rhys Davids 1896 start/end source marks;
- p.17 punctuation around `To R.D.'s remark it should be added`;
- p.18 full practical-agnosticism paragraph;
- p.20 full `present effort` paragraph;
- p.22 Warren `identity` sentence punctuation;
- p.29 Childers/Müller source numerals and transition;
- p.33 Hardy p.394 fact/manner grammar;
- pp.47–52 Senart/Oldenberg quotation/source boundaries and compressed Pāli/Sanskrit forms.

### 005

- pp.3–6 local Lovejoy additions versus Marillier/programme language;
- p.10 `American Legends, V. [Brinton?]` and Yarrow/Powers details;
- p.11 exact Rink wording/page marks;
- p.27 / p.29 / p.47 session headings and first paragraphs, where wording rather than date alignment matters;
- p.62 exact Brinton bibliography item after `art.`;
- p.89 exact Kingsley page/reference run;
- p.103 all authority/source marks around the image-secure diagram.

These are now **text-hygiene / paleography tasks**, not unresolved global-source architecture.

## Current access boundary

The newly supplied split witnesses remain present at 191/191 coverage. In the current execution environment, the page-image bridge for those project PDFs returns `Image unavailable`, and raw-byte materialization is not authorized. No reading in this round has therefore been invented from an unavailable current rendering. All changes above come from previously completed direct/high-resolution original-image controls already recorded in the repository; claims requiring a fresh blind page read remain in the residual queue.

This is an execution constraint, not an evidentiary downgrade of the already image-secure loci.

## Files changed in this propagation stage

- `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`;
- `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`;
- `archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json`;
- `research_notes/MS38_005_transcription_corrections_round16_original_image_2026-08-31.csv`;
- `research_notes/Quellenforschung_round15_evidence_matrix_2026-08-31.csv`.

## Current state

**QUELLENFORSCHUNG ARCHITECTURE RECALIBRATED / IMAGE-SECURE ROUND-16 DELTAS PROPAGATED / LAYOUT EVIDENCE EXPLICIT / REMAINING WORK = BLIND PALEOGRAPHIC HYGIENE ON A SMALL PRIORITY QUEUE.**
