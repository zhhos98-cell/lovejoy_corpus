# MS38_004 Round 18: direct-image transcription refinements on pp. 7, 13, 15, 16

Date: 2026-09-01

Status: **CANONICAL CLEAN JSON UPDATED / FOUR DIRECT-IMAGE REFINEMENTS PROPAGATED / NO EXTERNAL-EDITION NORMALIZATION USED**

## Witness

Governing witness: `MS38_004_001_061_004_1-36.pdf`.

Canonical file updated:

`archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`

Commit: `18ef72f93d12ad2276a33ee4ffee44ac2b8a5ce1`.

The governing rule remains:

`ORIGINAL IMAGE -> SECURE READING -> TRANSCRIPTION DELTA -> INTERPRETIVE CONSEQUENCE`

## p. 7 / ms p. 23

The earlier clean text contained two visible-word errors in the Sutta-Nipata transition:

- `auto-philos.` -> **`anti-philos.`**
- `inquisitiveness agt disputation` -> **`injunctions agt disputation`**

The opening syntax of the transition remains difficult. The clean file now records only the image-supported core as `[there seem to be expressions] of an anti-philos. sort` and retains an explicit syntax HOLD rather than smoothing the sentence into invented prose.

This matters because Lovejoy is not describing an actor who possesses an “auto-philosophical” attitude. He is characterizing a set of textual expressions as apparently anti-philosophical, then testing whether they are better read as injunctions against fruitless disputation.

## p. 13 / ms p. 55

The previous clean transcription silently supplied:

`perhaps certainly 2 or 3 centuries before Christ in Manu`

Direct image control supports instead:

`certainly 2 or 3 centuries earlier, in Manu, e.g., & in F. Bhag. Gita`

The phrase **`before Christ` is not the visible reading at this point**. Removing it matters because the notebook is making a relative chronological comparison with the surviving Sāṃkhya texts, not inserting an independently fixed absolute date in that clause.

## p. 15 / ms p. 59

The previously held heading for nos. 19-50 is directly legible in the supplied original image as:

`Uddhama-Aghatanika`

The clean file now transcribes that spelling as written. No modern diacritics or edition-based normalization have been silently supplied.

This resolves one Pass-A technical-heading uncertainty while keeping the archival layer distinct from later philological normalization.

## p. 16 / ms p. 61

The previous clean file read:

`The other #4 = F. Sankhya.`

The image instead supports:

`Neither #4 = F. Sankhya.`

The visible reading is secure; the exact semantic force of the compressed marginal/synthetic line remains unclear and is therefore still marked as an interpretive HOLD.

This correction is important precisely because the former wording made the line look like a positive identification. The manuscript wording does not license that paraphrase.

## Result

Four corrections are now propagated into the canonical p001-018 clean JSON. Two are ordinary but consequential lexical corrections (`anti-philos.`, `injunctions`), one removes a silently interpolated absolute chronology (`before Christ`), one resolves a technical heading (`Uddhama-Aghatanika`), and one reverses a misleading synthetic phrase (`The other #4` -> `Neither #4`).

The remaining uncertainty on p. 7 is syntactic rather than conceptual; the remaining uncertainty on p. 16 is semantic rather than paleographic.
