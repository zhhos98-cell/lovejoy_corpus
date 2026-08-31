# 004/005 Round 14 — original-image re-audit and transcription-integrity checkpoint

Date: 2026-08-31

## Scope

This checkpoint is based on renewed direct inspection of the manuscript page images, not on OCR, existing `clean.json` wording, or source-match back-projection. The target pages were chosen from the Round 13/14 HOLD register:

- 004 PDF pp. 6, 8, 17, 33, 42
- 005 PDF pp. 10, 62, 78–80, 103, 117

The principal purpose was to separate three different states that had previously been easy to conflate:

1. paleography actually recoverable from the manuscript image;
2. source identification recoverable only by external collation;
3. wording in `clean.json` that is analytic reconstruction rather than diplomatic transcription.

## Executive delta

### 004 p.8 / MS p.25 — Siṃsapā carrier: CLOSED at manuscript-label level

The source line is directly legible in the manuscript:

> `v. Oldenberg, p. 204 — Gotama + leaves of Simsapa-wood.`

This supersedes the existing clean transcription’s `[Source illegible], p. 20f.` reading.

Consequences:

- Oldenberg is no longer merely an A-grade content match inferred from external collation.
- The manuscript itself names Oldenberg and gives p. 204.
- Round 14’s previous residual paleographic HOLD on the source label can be closed.
- The immediate carrier is Hermann Oldenberg, *Buddha: His Life, His Doctrine, His Order*, Eng. trans. William Hoey (1882), p. 204 ff.

This is the strongest image-level correction produced in the present re-audit.

### 004 p.6 / MS p.21 — Sabbāsava passage

The manuscript page confirms Lovejoy’s heading and the direct use of the Sabbāsava material, including the sequence of questions about past, future, and present self-existence. The page itself does **not** visibly name Rhys Davids as translator/carrier.

Therefore the current source-status should remain split:

- translation family / clause-order match to Rhys Davids, SBE XI: strong;
- physical copy / immediate carrier named in Lovejoy’s hand: not established on this page.

Do not convert the external translation-family identification into a manuscript citation.

### 004 p.42 / MS p.123 — relation-specific ordering: CONFIRMED verbatim

The key sentence is directly legible:

> `In other words, viññāna is temporally (?) an antecedent of nama-rupa, and logically a sub-division of it.`

This confirms that the temporal/logical distinction is Lovejoy’s own explicit relational formulation on the page. It is not an editorial paraphrase introduced by the clean transcription.

The existing analytical conclusion remains valid: the notebook is not imposing one flat sequence; it explicitly permits different order-relations under different predicates.

### 005 p.10 / MS p.17 — `American Legends`: Brinton paleography CLOSED, source-function still split

The manuscript line is sufficiently clear to read:

> `American Legends, v. Brint.`

This is stronger than the existing `[Brinton?]` reading. The abbreviated author pointer is Brinton.

But the image also supports the Round 14 functional split:

- this is best read as a topical pointer (`American Legends — vide Brinton`), not proof of a work entitled *American Legends*;
- on the same page, the right-hand bibliography separately includes `A Further Contribution to Funeral Customs, same vol.`;
- the moon/coyote witness must therefore remain routed through the Yarrow/Powers chain rather than being forced through Brinton.

Paleographic HOLD closed; bibliographic function clarified.

### 005 p.62 / MS p.125 — Brinton sacrifice item: exact-title HOLD is intrinsic to the manuscript

The page is headed `Sacrifice` / `Bibliography` and clearly contains:

- `In L'Anthropologie article`
- `... Brint. art. [heavily overwritten/cancelled] for good bibliography & fair sketch of subject.`
- `Blood-Covenant ... H. Clay Trumbull`
- `Strack’s Der Blut-Aberglaube ...`

The decisive new point is negative: the word following `art.` is not merely low-resolution. It is heavily overwritten/cancelled in Lovejoy’s own hand. Even on a clean manuscript render it cannot be converted responsibly into a stable title.

Therefore:

- do not continue treating image resolution as the bottleneck;
- *Religions of Primitive Peoples* (1897), Lecture V remains the strongest external content candidate;
- exact identification requires Brinton bibliography / publication-history evidence, not another attempt to sharpen the scan;
- if no external bibliographic item fits better, the honest terminal state is `EXACT TITLE UNRECOVERABLE FROM MANUSCRIPT; EXTERNAL CANDIDATE STRONG`.

### 005 p.78 / MS p.157 — Trumbull numeral remains a genuine authorial uncertainty

The manuscript visibly cites:

> `Trumbull, "Blood-Covenant." 2?`

The mark after the initial `2` is itself uncertain-looking; it should **not** be silently expanded to `268`, `299`, or any other externally inferred page.

This changes the status of the old HOLD:

- content loci can still be resolved externally (notably the grave/animal and ghost-union discussions already isolated in Round 14);
- the handwritten page reference should remain diplomatic as uncertain rather than be replaced by the best source locus.

External source localization and manuscript numeral are two different evidence questions.

### 005 pp.79–80 / MS pp.159–161 — Lewis Grout immediate carrier: CLOSED by the notebook itself

The right-hand page of PDF p.79 explicitly reads:

> `Translation of Zulu prayer given by Lewis Grout, q.v.`

The following lines describe the preliminary procedure by which illness is attributed to ancestral shades, a sacrifice is demanded, and a particular cow can be specified. The continuation on p.80 preserves the transactional logic of the prayer and the later discussion of substitution / removal of evil.

Consequences:

- Grout 1889 is not merely a point-for-point external parallel; Lovejoy himself names Lewis Grout as the source of the Zulu prayer.
- The Round 14 Grout source closure is therefore upgraded from external collation to direct manuscript attestation.
- Callaway remains relevant as parallel Zulu/ancestor-sacrifice bibliography, but not as the immediate carrier of this particular prayer sequence.

### 005 p.103 / MS p.193 — Jevons direct-reading HOLD: strengthened negative control

Direct inspection confirms the page’s argument against a universal developmental sequence linking agrarian sacrifice, wild/domestic animals, agriculture, and domestication. Lovejoy explicitly argues that in Africa agriculture can precede domestication and that domestic animals need not contribute agricultural labor.

No `Jevons`, title, or Jevons page citation is visible on this target page.

Therefore:

- Jevons remains a secure proposition/controversy target at field level;
- Marillier remains a strong mediation environment;
- Lovejoy’s direct physical reading of Jevons remains HOLD.

Do not reopen this branch without a concrete documentary trace such as a title, page number, borrowing slip, correspondence, or verbal extraction.

### 005 p.117 — synthetic conclusion vs diplomatic transcription

The manuscript page does support Lovejoy’s explicit negative move away from reading bodily injury/initiation automatically as human sacrifice, and it continues his synthetic classification of sacrificial mechanisms.

However, the existing `clean.json` wording is substantially analytic/synthetic rather than diplomatic line-by-line transcription. This page is representative of a broader integrity issue in the later 005 batches: `corrected_text` sometimes stores source-supported reconstruction of the argument rather than literal manuscript wording.

This is not necessarily false, but downstream source-matching must not treat every `corrected_text` field as verbatim quotation.

## Transcription-integrity rule going forward

The image re-audit shows that the archive currently contains at least two different textual products under one field name:

- **diplomatic / near-diplomatic transcription** — wording follows the manuscript closely;
- **analytic reconstruction** — wording summarizes the recoverable argument where the hand was difficult.

For source criticism and phrase matching, these must be distinguished.

Recommended future schema addition per page:

- `text_mode: "diplomatic" | "near_diplomatic" | "analytic_reconstruction"`

Until such a schema migration is performed, any page whose `corrected_text` is visibly more polished than the manuscript should be treated as a research aid, not a quotation witness.

## Immediate archival corrections now justified

1. 004 p.8: replace `[Source illegible], p. 20f.` with `v. Oldenberg, p. 204 — Gotama + leaves of Simsapa-wood.`
2. 005 p.10: replace `American Legends, V. [Brinton?]` with `American Legends, v. Brint.`
3. 005 p.62: do **not** invent a Brinton title; record the post-`art.` title as overwritten/cancelled and externally unresolved.
4. 005 p.78: preserve the Trumbull page mark diplomatically as `2?` / uncertain; do not substitute externally reconstructed loci.
5. 005 p.79: mark Lewis Grout as direct manuscript attestation for the Zulu prayer source.

## Revised HOLD register after image recovery

### Closed

- 004 Siṃsapā source-label paleography → Oldenberg p.204.
- 005 p.10 Brinton author pointer → `Brint.`
- 005 pp.79–80 immediate Zulu-prayer carrier → Lewis Grout, explicitly named.

### Intrinsically unresolved / bounded

- 005 p.62 exact Brinton item title — overwritten/cancelled in manuscript; external bibliography required.
- 005 p.78 Trumbull handwritten page number — Lovejoy’s mark itself uncertain; external content loci must remain separate.
- 005 p.103 Jevons direct reading — no direct citation on target page; branch saturated absent new documentary trace.

### Still lower priority

- several African bibliographic abbreviations elsewhere in 005;
- systematic migration of later `clean.json` pages from analytic reconstruction toward explicit `text_mode` tagging.

## Restart statement

Original page images are now available again and can be used as the controlling witness. Future corrections should follow:

`MANUSCRIPT IMAGE → blind reading → compare clean.json → edit archive layer → only then use external source match for interpretation.`

Do not reverse that order on high-value source-identification pages.