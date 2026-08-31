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

## Round 16.2 — MS38_004_001_061_005 PDF p.119

### Original-image result

The left page is again readable enough to recover the structure, but several words remain genuinely difficult. Secure fragments include:

> `Note ... fashion of ... human flesh — indicates a specific virtue or force ...`

> `Note also organs wh. are chosen ... Some we can well enough understand — frontal bone ... of head often regarded as seat of intelligence, [illegible] as seat of breath & hence of life, and genital organs ...`

> `T. reason for this is not entirely clear — perh. as a repr. of [the] whole body, thus giving to eater possession of [the] force ... of [the] eaten.`

The physically separate right-hand slip is unrelated back-matter/outline material and should stay separate from the cannibalism argument.

### Correction to the prior clean reading

The existing clean text normalized the page into a neat organ-to-quality mapping:

`head/brain -> intelligence; heart -> courage/breath/life; sexual organs -> sexual power`.

The image does not sustain that full triplet at W3. What it does sustain is more interesting and more cautious:

1. selected human flesh/body parts can be treated as carrying a **specific virtue or force**;
2. Lovejoy thinks some selections are intelligible because a body part is conventionally associated with a function or quality, with the head/frontal-bone/intelligence relation among the clearest visible examples;
3. he explicitly says the reason for other selections is `not entirely clear`;
4. he entertains an alternative mechanism in which the **part represents the whole body**, allowing the eater to acquire the force of the eaten person.

This is a genuine correction, not merely a lexical cleanup. The earlier transcription made Lovejoy more systematic than the page itself is.

### W/S/T/A recalibration

For the selected-part mechanism:

- **W2-W3** — the core mechanism and several phrases are image-secure, while some body-part nouns and the exact quality assignments remain uncertain;
- **S0** — no external source needed yet;
- **T0** — source transmission remains untested at this stage;
- **A2** — direct local analytical alternatives are visible: part-specific virtue versus part-as-representative-of-whole.

### Current evidentiary effect

The 005→1906 bridge remains viable at the level of **transferable efficacy / force**, but the manuscript should no longer be cited for the fully normalized three-arrow body-part schema. Publication-side comparison must use the weaker and more faithful formulation until exact words are collated.

## Round 16 queue

Next high-priority original-image checks:

1. 005 pp.79-80 — Zulu ancestral-sacrifice sequence, but note that the existing clean reading was already viewed during this working session, so this will be an image-controlled recheck rather than a perfectly source-blind first pass;
2. 005 p.78 — Trumbull numeral/locus;
3. 005 p.62 — exact Brinton sacrifice item;
4. 005 p.10 — `American Legends V [name]` paleography;
5. 004 p.13/p.42 and other Round-15 priority loci after the 005 late-synthesis block is closed.

## Repository authority

Until the clean JSON batch is propagated, the correction ledger
`research_notes/MS38_005_transcription_corrections_round16_original_image_2026-08-31.csv`
controls exact quotation from pp.117 and 119 and supersedes the older editorial-summary wording at those loci.
