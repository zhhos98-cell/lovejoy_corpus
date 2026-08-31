# Quellenforschung Round 16 — original-image verification

Date: 2026-08-31
Status: ACTIVE
Scope: post-Round-15 manuscript-image recheck of high-value transcription claims

## Governing protocol

This round implements the original-image gate set in `QUELLENFORSCHUNG_CURRENT_GATE.md`.

For each target locus:

1. inspect the manuscript image before consulting the candidate external source;
2. make a diplomatic transcription with uncertain graphemes explicitly marked;
3. freeze that reading;
4. compare against the existing `*_clean.json` reading;
5. only then reopen source candidates for source-text collation;
6. assign W/S/T/A independently.

The immediate purpose is not to generate another interpretive summary. It is to recover the manuscript witness strongly enough to decide which earlier transcription claims can remain, which require lexical correction, and which must stay at editorial-summary level.

## Round 16.1 — MS38_004_001_061_005 PDF p.117

### Why this page was first

Round 15 had downgraded the late sacrifice synthesis at p.117 because the existing clean transcription was an editorial/source-supported summary (`W1-W2`) rather than a frozen diplomatic reading. This was one of the highest-priority blind pages in the gate.

### Original-image result

The left-hand page is substantially readable at high resolution. The key manuscript sequence is:

> `[continuation:] Times it is even adults married men who are beaten. At all events, we have no reason for connecting [the] observance with human sacrifice. The idea in gt. number of cases is alimentary, i.e. a case of anthropophagy. In [the] next most numerous cases, it is expiatory & propitiatory. A human sacrifice for union is altogether exceptional, while the [illegible/abbrev.] sac. of union is more frequent than alimentary [illegible]. Of course we shall have presently to consider a number of actual examples; but they are none the less relatively rare.`

Square brackets here mark editorial uncertainty only. No external sacrifice-theory source was used to supply missing words.

### Correction to the prior clean reading

The earlier clean text got the main architecture right but flattened Lovejoy's comparative grammar too aggressively. The manuscript does not simply give three coequal labels such as `alimentary common / expiatory-propitiatory common / sacramental union exceptional`.

The recoverable wording is more specific:

- `in gt. number of cases` → alimentary / anthropophagic;
- `in [the] next most numerous cases` → expiatory & propitiatory;
- `a human sacrifice for union is altogether exceptional`;
- an immediately following comparative clause about a `... sac. of union` remains paleographically uncertain and must not be silently normalized.

This matters analytically. The page contains a ranked frequency claim and a restriction specifically on **human sacrifice for union**, not a generic taxonomy with three equal bins.

### W/S/T/A recalibration

For the distributional synthesis itself:

- **W3** — direct image/diplomatic wording secure for the key sentences;
- **S0** — no source-text match is required to establish the local wording;
- **T0** — transmission is not at issue at this stage;
- **A2** — direct Lovejoy local synthesis/reweighting on the manuscript page.

The uncertain clause after `while the` remains excluded from any stronger lexical claim until a later paleographic pass.

### Current evidentiary effect

The Round-15 downgrade on p.117 is partially reversed. The page may now be quoted for the ranked late synthesis, with diplomatic abbreviations retained and the uncertain clause omitted or marked. It should not be paraphrased as proof that Lovejoy originated the underlying sacrifice categories.

The governing historical claim therefore becomes stronger locally without reviving an originality story: the manuscript witness securely shows Lovejoy ranking the incidence and evidentiary weight of competing sacrificial mechanisms.

## Round 16 queue

Next high-priority original-image checks:

1. 005 p.119 — selected-body-part / transferable-efficacy wording;
2. 005 pp.79-80 — Zulu ancestral-sacrifice sequence, but note that the existing clean reading was already viewed during this working session, so this will be an image-controlled recheck rather than a perfectly source-blind first pass;
3. 005 p.78 — Trumbull numeral/locus;
4. 005 p.62 — exact Brinton sacrifice item;
5. 005 p.10 — `American Legends V [name]` paleography;
6. 004 p.13/p.42 and other Round-15 priority loci after the 005 late-synthesis block is closed.

## Repository authority

Until the clean JSON batch is propagated, the correction ledger
`research_notes/MS38_005_transcription_corrections_round16_original_image_2026-08-31.csv`
controls exact quotation from p.117 and supersedes the older editorial-summary wording at that locus.
