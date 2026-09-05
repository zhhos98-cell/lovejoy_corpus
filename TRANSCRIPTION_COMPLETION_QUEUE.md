# Lovejoy manuscript transcription completion queue

Last synchronized: 2026-09-05
Status: **TRANSCRIPTION INCOMPLETE / PAGE COVERAGE COMPLETE / CANONICAL WITNESS-LAYER HYGIENE UPDATED**

This file separates page coverage from transcription completion. `191/191` means that every PDF page has a page record and material overview. It does **not** mean that every page has a complete diplomatic transcription from the manuscript image.

## 2026-09-05 execution note

A corpus-wide canonical transcription-hygiene pass was completed across notebook 005 without pretending that unavailable page images had been reread. The pass propagated already-existing direct-image controls and later source-ownership adjudications into the canonical JSON records.

Canonical batch changes in this pass:

- `p046-060`: p.55 reduced to the image-secure `not ritual but alimentary`, male-flesh preference, and existence of a male/female gastronomic contrast; exact taste direction, source boundary, and power/value connective returned to diplomatic HOLD — commit `ebeb58c150a108d1b31d89aec9c36be805e0543c`;
- `p076-090`: p.84 anti-union relation and p.90 guardian-spirit/direct-blood relation downgraded from editorially overstrong Lovejoy claims to explicit relation-level HOLDs — commit `0121bfb65bb8f32c5bfb3a3713dc7365a8890615`;
- `p091-105`: pp.92–99 re-tagged as Marillier-mediated insert packets unless a local image-secure intervention is demonstrated; p.103 explicitly registered as W3 for the `involves a vicious circle` chronology veto; p.104 W3 path exclusion/selection preserved — commit `c75c6c564366daf8340851de46efb7161f1877ab`;
- `p106-120`: p.112 calibrated as strong case-adjudication with exact-wording HOLD; p.117 remains W3 wording with proposition-authorship HOLD; p.119 downgraded from a Lovejoy-origin explanatory fork to an undated late-insert authorship/chronology HOLD — commit `6f9682233d6318fcf1920a60bf74f00568e74dc2`;
- `p061-075`: source-owned mechanisms separated from local relations; p.66 retained as strong W3 mechanism→jurisdiction relation, p.69 counter-arrow calibrated to the Robertson-Smith field, p.73 narrowed to local explanatory reassignment — commit `e0bcf54ff56b0de74d40dd540fcc4d81a50ccf60`;
- `p031-045`: pp.31–36 and pp.42–43 now carry explicit `DIPLOMATIC HOLD` / `text_layer` / source-collation metadata; no Marillier wording was imported into the manuscript — commit `ce79786a7b35b37c156d2c2d964da4c88734a105`.

This pass **did not mark any new page diplomatically complete**. It made the remaining incompleteness more explicit and prevented editorial/source summaries from masquerading as manuscript wording or Lovejoy proposition ownership.

### Current image-access constraint

The split original scans are identified in the user's file Library, including `MS38_004_001_061_005_1-40.pdf`, `..._41-80.pdf`, and `..._81-120.pdf`. In the 2026-09-05 runtime, direct page-image rendering returned no pixels and raw/page-range materialization returned a 403. Therefore criterion 1 below could not be satisfied for a fresh diplomatic pass. This is a tooling/access constraint, **not** evidence that the images or manuscript are absent.

Until direct image access returns, do not use OCR or Marillier/source collation to manufacture diplomatic wording.

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

Notebook 005 has 120/120 first-pass page coverage and broad targeted original-image rechecks through Round 20 plus later proposition/source-specific direct-image controls. It is **not** diplomatically complete.

### Priority A — visibly incomplete first-pass pages

- **pp.31–36**: inserted leaves remain low or low-medium confidence. Canonical records now explicitly mark these as `DIPLOMATIC HOLD`. Marillier collation narrows the likely source packets but is stored only as `external_source_collation`; these pages still require full direct-image retranscription.
- **pp.42–43**: Greek lexical/textual slips remain only partially transcribed. Canonical records now separate the host-page outline from loose slips and explicitly mark the Greek layer as diplomatically incomplete.

### Priority B — resume the interrupted systematic second pass

Resume **pp.47–60** when the original image is directly visible. Existing image-secure controls at p.49 and p.53 must be preserved. At p.55 preserve only what is currently W3 unless fresh image inspection closes the disputed sex/taste direction and source boundary.

The 2026-09-05 hygiene pass reviewed this entire batch for witness/source ceilings, but **that review is not a substitute for page-by-page diplomatic retranscription**.

### Priority C — complete the rest of 005 page by page

After pp.47–60, continue through:

- pp.61–75;
- pp.76–90;
- pp.91–105;
- pp.106–120.

The 2026-09-05 pass has already made the main known witness/source boundaries explicit in these batches, including p.66, p.84, p.90, pp.92–99, pp.103–104, p.112, p.117, and p.119. This reduces interpretive risk but does not establish full-page diplomatic completion.

### Priority D — backfill pp.1–30 as needed

Rounds 19–20 materially improved pp.3–6 and pp.16–30. The original-image sweep of pp.20–28 found no mechanism-changing delta, so do not manufacture one. A later edition pass should still verify that every readable line in pp.1–30 is represented diplomatically rather than accepting proposition-sensitive closure as page completion.

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

`archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md` is retained at its stable historical path because many files refer to it. The word `final` in the filename is **not a completion claim**.

**Synchronization warning, 2026-09-05:** the canonical 005 JSON batches listed above were changed after the last generated integrated surface. In the present connector-only runtime the repository generator cannot be executed against the GitHub working tree, and there is no safe partial-patch action for the generated file. Therefore the integrated Markdown is temporarily **STALE RELATIVE TO THE CANONICAL JSON**. Until regenerated, use the paginated canonical JSON batches as page authority.

Required regeneration when repo-shell access is available:

```bash
python tools/build_integrated_transcription.py
python tools/build_integrated_transcription.py --check
python tools/audit_repository.py
```

Do not manually rewrite the 191-page integrated file merely to conceal this synchronization state.

## Execution rule

For transcription work, the queue in this file overrides older “only proposition-sensitive hygiene” language. Proposition-sensitive rechecks remain useful for research claims; they are insufficient as a completion protocol.

Before changing a canonical batch:

1. read the current page record;
2. read the latest page/block dossier;
3. inspect the original image;
4. preserve later direct-image corrections already merged;
5. replace summary with diplomatic wording only where the image licenses it;
6. regenerate the integrated reading surface and run `python tools/audit_repository.py` after batch edits when repo-shell access permits; if it does not, record the generated-surface divergence explicitly rather than claiming synchronization.

## Current restart point

When direct image access returns, start with **005 pp.31–36**, then **pp.42–43**, then resume **pp.47–60**. The 2026-09-05 hygiene pass has already narrowed the exact uncertainty and source-ownership burden at these and later loci, so the next pass should be paleographic/diplomatic rather than another thematic source sweep.
