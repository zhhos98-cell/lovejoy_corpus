# Lovejoy manuscript transcription completion queue

Last synchronized: 2026-09-02
Status: **TRANSCRIPTION INCOMPLETE / PAGE COVERAGE COMPLETE**

This file separates page coverage from transcription completion. `191/191` means that every PDF page has a page record and material overview. It does **not** mean that every page has a complete diplomatic transcription from the manuscript image.

## Completion vocabulary

Use the following terms consistently:

- **page coverage complete** — every PDF page has a record;
- **first-pass text coverage complete** — every page has some corrected text, readable fragments, or conservative editorial summary;
- **targeted original-image control** — selected proposition-bearing or uncertain loci were checked directly against the image;
- **diplomatic page complete** — the visible manuscript wording on a page has been transcribed as fully as the image permits, with unresolved characters/words explicitly marked;
- **diplomatic notebook complete** — every nonblank page has reached diplomatic page completion and all material layers/inserts are separately represented.

A page containing mainly `editorial_argument_summary`, generic prose reconstruction, or phrases such as “continuation”, “several lines remain illegible”, “Greek quotations not fully transcribed”, or equivalent language is not diplomatically complete even when `corrected_text` is populated.

## Completion criteria for a page

A page can be marked diplomatically complete only when:

1. the manuscript image has been directly inspected;
2. visible wording has been transcribed rather than replaced by an argument summary;
3. abbreviations are preserved unless an expansion is explicitly editorial;
4. uncertain letters/words are marked rather than silently reconstructed from external sources;
5. inserted leaves, slips, overlays, facing-page relations, cancellations, and diagrams are represented separately where material form matters;
6. `diplomatic_visible_text` or an equivalent clearly identified direct-image field is present for readable text;
7. `uncertain_readings`, `text_layer`, and `witness_status` accurately describe remaining limits;
8. source collation and editorial interpretation remain separate from visible manuscript wording.

## Notebook 005 — active completion queue

Notebook 005 has 120/120 first-pass page coverage and broad targeted original-image rechecks through Round 20. It is **not** diplomatically complete.

### Priority A — visibly incomplete first-pass pages

- **pp.31–36**: inserted leaves remain low or low-medium confidence; multiple entries explicitly state that most lines, proper names, source references, or geographic wording remain illegible or only partially legible. These pages require full direct-image retranscription, not further summary polishing.
- **pp.42–43**: Greek lexical/textual slips are only partially transcribed; exact Greek and several references remain open.

### Priority B — resume the interrupted systematic second pass

Round 20 explicitly hands off to **pp.47–60**. Existing upgrades at p.49, p.53, and p.55 must be preserved. The remaining pages in this block should be checked page by page for diplomatic wording, not only mechanism-changing deltas.

### Priority C — complete the rest of 005 page by page

After pp.47–60, continue through:

- pp.61–75;
- pp.76–90;
- pp.91–105;
- pp.106–120.

Targeted controls already secure important loci such as pp.64, 66, 69, 92–96, 104, and 117–120. Those controls reduce risk but do not substitute for full-page diplomatic transcription of the surrounding pages.

### Priority D — backfill pp.1–30 as needed

Rounds 19–20 materially improved pp.3–6 and pp.16–30. A later completion pass should still verify that every readable line in pp.1–30 is represented diplomatically, rather than accepting proposition-sensitive closure as page completion.

## Notebook 004 — residual completion queue

Notebook 004 has 71/71 first-pass coverage and is conceptually closed for the present research argument after targeted direct-image control. It remains short of a full diplomatic edition.

Residual work is concentrated in:

- micro-paleographic readings;
- compressed Pāli/Sanskrit/French;
- bibliographic abbreviations and references;
- crossed or overwritten words;
- pages where current `corrected_text` combines image-secure key wording with editorial summary.

004 therefore has lower research priority than 005, but it should be reopened if the project goal changes from argument control to a complete manuscript edition.

## Integrated edition status

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md` is retained at its stable historical path because many files refer to it. The word `final` in the filename is **not a completion claim**. Treat it as the current integrated working reading surface generated from the canonical JSON batches.

Do not rename or migrate this path casually. If a genuinely diplomatic edition is later completed, create a new explicitly versioned edition and update routing files then.

## Execution rule

For transcription work, the queue in this file overrides older “only proposition-sensitive hygiene” language. Proposition-sensitive rechecks remain useful for research claims; they are insufficient as a completion protocol.

Before changing a canonical batch:

1. read the current page record;
2. read the latest page/block dossier;
3. inspect the original image;
4. preserve later direct-image corrections already merged;
5. replace summary with diplomatic wording only where the image licenses it;
6. regenerate the integrated reading surface and run `python tools/audit_repository.py` after batch edits.

## Current restart point

Start with **005 pp.31–36**, then **pp.42–43**, then resume **pp.47–60**. This order addresses the clearest known first-pass incompleteness before continuing the interrupted systematic second pass.
