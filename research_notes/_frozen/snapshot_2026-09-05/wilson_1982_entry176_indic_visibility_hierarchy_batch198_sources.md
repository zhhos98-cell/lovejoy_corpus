# Batch 198 source register

Date: 2026-08-26
Scope: source controls for `wilson_1982_entry176_indic_visibility_hierarchy_batch198.md`.

| ID | Source | Locator / recovered text | Function | Grade |
|---|---|---|---|---|
| B198-S1 | Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography* (1982) | entry176, pp. 78–79 of Primary Sources: Deussen, *Outline of the Vedanta System of Philosophy, according to Shankara*; annotation names Śaṅkara, Rāmānuja, and Hindu philosophy | establishes 176 content and entry boundary | direct bibliographic |
| B198-S2 | same | immediately after entry176 annotation, entry177 begins; entry177 later has its own `See 178` | controls absence of outgoing `See` from 176 | direct bibliographic |
| B198-S3 | same, searchable full text | exact search `See 176`: no match recovered | incoming-edge audit | negative search control |
| B198-S4 | repository Wilson OCR JSON | exact search `See 176`: zero matches | corroborative incoming-edge audit | OCR negative control |
| B198-S5 | Wilson index, D-range | `Deusen, Paul, 176` [OCR/rendering for Deussen] | author-index route | direct index |
| B198-S6 | Wilson index, O-range | `Outline of the Védanta System of Philosophy, 176` | title-index route | direct index |
| B198-S7 | Wilson index, R-range | inspected alphabetic range around Ramsperger–Russell; no recovered `Ramanuja` heading | index-granularity control | direct index / negative range control |
| B198-S8 | Wilson index, S-range | inspected alphabetic range around Santayana–Syllabus; no recovered `Shankara` heading | index-granularity control | direct index / negative range control |
| B198-S9 | Wilson index, H-range | inspected `History...`, Hobbes, Human nature, Hume range; no recovered `Hindu philosophy` heading | index-granularity control | direct index / negative range control |
| B198-S10 | Wilson index, I-range | inspected Idealism → Intellectual history → International...; no recovered `India` / `Indian philosophy` heading | index-granularity control | direct index / negative range control |
| B198-S11 | Wilson entry243 | `The Place of Buddhism among the Philosophies of India` inside `Syllabus: The Philosophy of Buddhism` | proves India remains textually present | direct bibliographic |
| B198-S12 | Wilson index | `Buddhism, 19,243` | subject-index comparison | direct index |
| B198-S13 | Wilson index | `Otherworldliness, 21–22` | subject-index comparison | direct index |

## Search-control cautions

- A zero OCR/string-search result is weaker than a positive textual witness. It is used here only together with direct inspection of the entry boundary or the relevant alphabetic index range.
- The public searchable rendering and the repository OCR contain minor transcription defects (`Deusen`, `V@édanta`, etc.). Stable entry numbers and surrounding alphabetic order are therefore stronger controls than exact diacritics.
- No negative index claim should be generalized beyond Wilson's 1982 bibliography.

## New graph subtypes

- `W-IDX-SUBJ` — subject-heading relation.
- `W-IDX-AUTH` — author-name retrieval relation.
- `W-IDX-TITLE` — title retrieval relation.
- `W-ANN` — content/relation visible in annotation prose only.
- `W-SEE` — formal cross-reference.
