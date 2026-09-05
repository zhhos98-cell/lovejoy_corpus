# JHI full-repository micro-reuse audit — resumed 2026-09-05

Status: **IN PROGRESS — EXPLICIT USER REACTIVATION OF FULL-REPO SENTENCE/MICRO-UNIT PASS**

This file is the live continuation ledger for the explicitly reopened full-repository pass. Historical audit provenance remains at `research_notes/_frozen/snapshot_2026-09-05/JHI_FULL_REPO_MICRO_REUSE_AUDIT_2026-09-05.md` and is not edited. The canonical prose authority remains `research_notes/JHI_blog_full_draft_v3_7_clean_submission_2026-09-03.md`.

The user explicitly reopened the previously frozen corpus-wide pass on 2026-09-05 with the instruction to inspect the whole repository sentence by sentence for material that can be inserted first. This overrides the default freeze for discovery scope, but **does not override surgical editing, source-lock, attribution, or evidence-firewall rules**.

## Disposition vocabulary

- `BODY` — secure micro-unit changes or sharpens an existing body sentence.
- `NOTE` — secure but supporting/provenance detail suitable for an endnote.
- `LINK/BIBLIO` — locator or bibliographic improvement only.
- `SOURCE-CONTEXT` — useful source/environment control, normally not prose.
- `QUARANTINE` — target/lead/partial object that cannot yet be narrated.
- `NO-FIT` — secure material but outside the present short-form burden.
- `ALREADY-REPRESENTED` — semantic content already controlled in the canonical draft or promoted terminal/evidence file.

Completion means every tracked path is assigned a disposition. Raw/binary/derivative paths may be dispositioned at file/path level when canonical semantic controls already exhaust them; they are not falsely described as sentence-read. In particular, a machine OCR derivative is not counted as a second independent sentence-level witness when a higher-grade direct image, direct transcription, printed primary or controlled clean transcription already exhausts its evidentiary function.

## Canonical draft patches produced by this resumed pass

### Commit `2bb5cec891f1481104d2bd233b6be963e002faf9`

- `NOTE`: Harvard first registration 26 Sep. 1895 and 1895–96 Sanskrit half-course sequence before the 1896–97 advanced Pāli year.
- `NOTE`: 9 Oct. 1898 Paris-year self-description as `philosophy and comparative religion`; 20 Oct. Buddhism/Hebrew-Wisdom pairing.
- `NOTE`: AOS administrative title path from Hanns Oertel title intake to George F. Moore Recording Secretary/editorial record, without assigning authorship of the title change.

### Commit `17e000deed81ac679259ec888576f848edc125fd`

- `BODY`: direct-image p.17 / MS p.63 source boundary, `To R.D.'s remark it shld be added`, followed by the shift toward Sāṃkhya `thorough-going dualism` / separateness of Self and World.
- `BODY`: direct-image p.51 / MS p.141 initialled question, `But is there necessarily any ontological function involved? A.O.L.`
- `NOTE`: notebook 005 pp.103–104 branching genealogy, chronology objection and possible `vicious circle`, including agriculture anterior to domestication in Africa.
- `BODY + NOTE`: bounded 1906 More review reuse of *Sutta Nipāta* 1073–1076 to constrain a positive Nirvāṇa reconstruction.

### Commit `637e093…`

- `BODY + NOTE`: notebook 004 p.27 relation diagram in which six consciousness lines converge on *nāmarūpa* and fan into parallel sensory/contact/sensation/desire channels.
- `BODY + NOTE`: notebook 005 p.53 `purely mechanical` sacrifice with the god potentially uninvolved; p.65 `delicate analysis` of mingled sacrificial forms; p.69 animal sacrifice `not an evidence of advancement`.
- `NOTE`: independent 004 p.50 recurrence of temporal/logical relation language.

### Commit `7b4e322…`

- `BODY`: direct 1898 printed-primary control that *upādānakkhandha* does not itself lock one causal direction; Lovejoy accepts commentary allowing the skandhas to be produced by *upādāna* or to stand as its causes.
- `BODY`: printed restriction that Buddhism is `based, not upon a metaphysic, but upon a Psychology of sensation`; first *nidāna* is not promoted to an ontological Absolute.
- `NOTE`: Lovejoy's own `preliminary study` calibration on p.126.

### Commit `00721e1…`

- `BODY + NOTE`: EPHE official report identifies Lovejoy among `auditeurs ayant pris une part active aux travaux` in Marillier's conferences, while separately listing `élèves titulaires`; this supports active-auditor participation but not titulaire status or a claim that notebook 005 is a lecture transcript.
- `BODY/NOTE`: primary bibliography appended to *Essays in the History of Ideas* records the 1901 Washington University Association four-lecture `Syllabus: The philosophy of Buddhism`; syllabus text remains unrecovered.

### Commit `a1b1af4783509da13dc3472f571cec061ceb3a9b`

- `BODY + NOTE`: bounded 1904 recurrence of relation-specific analysis in `The Dialectic of Bruno and Spinoza`, pp.145–147: finite being / `that` and determinate nature / `what` are separated, with Vedānta used as a worked example in which the first relation can be affirmed and the second denied.
- `NOTE`: exact edition behind Lovejoy's Muṇḍaka wording remains unidentified; no Buddhist-notebook → 1904 genealogy or transmission claim is made.

## High-weight semantic surfaces completed in resumed pass

### `archive_transcriptions/`

- The integrated 191-page corrected-text reading surface has been read across all 71 pages of notebook 004 and all 120 pages of notebook 005.
- This is **191/191 first-pass / corrected-text semantic coverage**, not a claim of 191-page diplomatic completion. Explicit 005 image/source-version holds remain holds.
- The twelve canonical clean JSON batches are semantically represented by the integrated surface; direct-image delta files and material manifest were separately checked for source/hand/material exceptions.
- Result: p.27 004 diagram and p.53/p.65/p.69/p.103–104 005 units were promoted; remaining transcription derivatives are `ALREADY-REPRESENTED / SOURCE-CONTEXT` at path level unless a future image-control problem reopens them.

### raw 1898 Lovejoy primary

- `source/lovejoy/1898/The Buddhistic technical terms upadana and upadisesa..html` was read sentence by sentence against the active argument.
- Result: bidirectional causal reading, anti-ontological / psychology restriction and `preliminary study` calibration promoted.

### `tools/`

- All six tool files were read for embedded locators/comments and operational assumptions.
- Result: `REPRODUCIBILITY / SOURCE-CONTEXT`; no code/comment sentence is promoted as historical evidence.

### root/governance/source routing

- Active root governance/router files were read sufficiently to enforce evidence ceilings and avoid confusing first-pass transcription with diplomatic completion.
- `source/README.md` and `source/SOURCE_INDEX.md` were checked against recursive subtree enumerations. The source router is path-complete for the current `source/` tree; no active `_unclassified/` payload remains.

## Research-note / old-draft dispositions completed in resumed pass

| path | disposition | result |
|---|---|---|
| `research_notes/JHI_MICRO_REUSE_TERMINAL_2026-09-05.md` | ALREADY-REPRESENTED / ROUTER | used to recover prior terminal micro-units; no independent prose insertion |
| frozen `JHI_FULL_REPO_MICRO_REUSE_AUDIT_2026-09-05.md` | PROVENANCE / ROUTER | resumed from its explicit unfinished queues rather than restarting already completed paths |
| frozen `004_proof_architecture_publication_selection_consolidated.md` | BODY/NOTE | p.17 source seam promoted; remaining publication-selection architecture already represented |
| frozen `QUELLENFORSCHUNG_round21b_pp048-071_authorial_seams_2026-09-03.md` | BODY/NOTE | p.51 initialled seam promoted; p.49/p.62/p.66 already represented; p.52 source-owned proposition remains attribution control |
| `research_notes/LOVEJOY_004_TERMINAL_SYNTHESIS.md` | BODY/NOTE/ALREADY-REPRESENTED | used as authority ceiling; no broad re-expansion |
| `research_notes/LOVEJOY_005_TERMINAL_SYNTHESIS.md` | BODY/NOTE/ALREADY-REPRESENTED | selected 005 operations remain sufficient |
| frozen `005_boundary_controls_consolidated.md` | NOTE/NO-FIT | pp.103–104 concrete chronology test promoted; broader classifications remain supporting only |
| frozen `JHI_blog_full_draft_v3_11_first_order_8314w_2026-09-04.md` | MICRO-HARVEST / MOSTLY NO-FIT | p.17, p.51, Paris details, p.103 chronology and bounded 1906 continuity harvested; broad politics / `primitive` sections remain out |
| `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md` | BODY/NOTE/CONTROL | confirms More/*Sutta Nipāta* continuity and 004/005 evidence ceilings; broad 1906 scalar laboratory remains outside short-form center |
| frozen `004_Hardy_causal_microgenesis_consolidated.md` | NOTE/SOURCE-CONTEXT | Hardy instability / inherited two-factor architecture now represented in [^7] |
| frozen `004_Senart_Jacobi_Oldenberg_primary_controversy_consolidated.md` | NOTE/SOURCE-CONTEXT | Oldenberg p.447 field-level control now represented in [^7]; availability is not treated as uptake |
| frozen `004_upadisesa_lexical_semantic_recomposition_consolidated.md` | NOTE/ALREADY-REPRESENTED | Oldenberg/Childers/Rhys Davids/Müller/Dahlmann fork and Müller p.30→p.36 discrepancy represented |
| frozen `005_Marillier_selector_alignment_consolidated.md` | SOURCE-CONTEXT/NO-FIT | removes originality claims for selector taxonomy/serial redivision; supports a shared field rather than body expansion |
| frozen `005_Steinmetz_Mauss_Marillier_explanatory_level_consolidated.md` | SOURCE-CONTEXT/NO-FIT | mechanism/form distinction is controversy-level field; current 005 examples carry the short-form burden |
| frozen `JHI_blog_full_draft_v3_2_citation_ready_2026-08-29.md` | BIBLIO | supplied exact 1906 More review bibliographic identity |
| frozen `Lovejoy_1904_Bruno_Spinoza_primary_consolidated.md` + associated 1904 source-role dossiers | BODY/NOTE/NO-FIT | `that/what` relation split promoted as one bounded continuity sentence; broader Bruno/Spinoza genealogy, influence taxonomy and Occidental closing rhetoric remain outside current center |

## `archive_index` CSV traversal — current disposition

The recursive frozen `archive_index` inventory was enumerated path-completely. Earlier high-relevance CSVs were row-read. For the remaining control/infrastructure families, a cross-file early-date exception sweep was run for 1895, 1897, 1898, 1901, 1902, 1904 and 1906 before assigning family/path dispositions. This distinction matters: the control families below are **not falsely described as individually sentence/row-read when their function is archival routing rather than prose evidence**.

### Earlier row-read / inspected CSVs

| path | disposition | result |
|---|---|---|
| `jhu_lovejoy_authority_record_crosscollection_batch110.csv` | ALREADY-REPRESENTED / NO-FIT / QUARANTINE by row | MS-0873 derivative status relevant and controlled; later authority associations do not enter short form |
| `jhu_ms0038_correspondence_component_index.csv` | NO-FIT | later correspondence locators without current-article dates/content |
| `lovejoy_paris_hopkins_priority_archival_targets_batch171.csv` | QUARANTINE / SOURCE-CONTEXT / NO-FIT by row | early rows identify MS-0873, Lanman, Harvard History of Religions Club, EPHE, Lévi and Marillier MS99 targets; target status is not narratable evidence |
| `lovejoy_wilson_transcription_provenance_batch111.csv` | NOTE/SOURCE-CONTEXT | MS-0873 is a separately catalogued derivative one-box transcription collection; current [^2] respects the distinction |
| `lovejoy_jhu_manifestation_domains_batch110.csv` | SOURCE-CONTEXT/ALREADY-REPRESENTED | original fonds versus derivative-transcription distinction controlled |
| `lovejoy_stanford_1901_manifestation_opportunity_batch113.csv` | NO-FIT / QUARANTINE | exact Ross-case event, unresolved manifestation, outside Buddhist short form |
| `jhu_ms0038_box24_document_delta_batch103.csv` | NO-FIT | 1917–18 wartime academic-freedom correspondence |
| `jhu_ms0038_third_party_document_map_batch102.csv` | NO-FIT / SOURCE-CONTEXT | 1917–20 third-party/AAUP traffic and custody control |

### Remaining CSV families after early-date exception sweep

- AAUP formation/foundation, 1915/1919 pensions, WWI academic-freedom, Cornell, Tyler and related documentary chains: `NO-FIT / SOURCE-CONTEXT`.
- Russell/Harvard/Hopkins/Woods 1916 state-control, invitation, interception, retrieval and custody graphs: `NO-FIT / SOURCE-CONTEXT`.
- Science Service / Smithsonian 1940s correspondence, opportunity, split-custody and preservation-gap families: `NO-FIT / SOURCE-CONTEXT`.
- Stanford manifestation/citation/microfilm files: `NO-FIT / QUARANTINE / SOURCE-CONTEXT`; the only person-level early branch is the already-known 1901 Ross-case, not a Buddhist-evidence unit.
- Global archive component/lead/coverage/conflict/upgrade/concurrency/ambiguity families: `SOURCE-CONTEXT / QUARANTINE / MOSTLY NO-FIT`. Early-year hits were checked before this family disposition. They consist chiefly of collection date ranges, finding-aid labels, archive leads or the Cattell 1904–09 box-label conflict, not new Lovejoy Buddhist propositions.
- derivative/original crosswalk, custody/address separation, duplicate-alias, preservation-gap and document-family control CSVs: `SOURCE-CONTEXT / ALREADY-REPRESENTED`.
- discovery/candidate-folder CSVs (`IACF/ACCF`, Tamiment and similar): `QUARANTINE / NO-FIT` until object-level evidence exists; none alters the current article.

### Early-date exception sweep result

- `1898`: only the already-read Paris/Hopkins target file plus global lead metadata.
- `1895`: one 1916 Russell letter's retrospective Berlin reference plus broad target date ranges; no Lovejoy-1895 article unit.
- `1897`: no frozen CSV code-search hit.
- `1901`: Stanford Ross-case branch plus collection-range/global-control hits; no new Buddhist evidence.
- `1902`: Marillier obituary is a retrieval target; Science Service hit is a collection range.
- `1904`: Cattell/AAUP archival date-label conflict and archive-index metadata; no current-article micro-unit.
- `1906`: Stanford/global collection-range metadata; no new Buddhist evidence beyond the already-promoted More review.

**CSV result:** no additional `BODY` or `NOTE` unit remains to promote from the frozen archive-index control families.

## `source/` path-complete disposition

`source/README.md` defines raw/near-raw routing by evidentiary function and explicitly denies automatic canonical status to machine-readable derivatives. `source/SOURCE_INDEX.md` was checked against recursive trees for `archive/`, `institutions/`, `lovejoy/`, `reference/`, `context/`, `discovery/` and `notebooks/`; the listed payload inventory matches the current trees.

### `source/archive/`

- JHU MS-0873 France 1898–99 PaddleOCR derivative: `ALREADY-REPRESENTED / SOURCE-CONTEXT`; direct Wilson-transcription controls carry [^2].
- JHU MS-0038 PaddleOCR derivative: `ALREADY-REPRESENTED / SOURCE-CONTEXT`; image-controlled and clean-transcription notebook surfaces outrank it.
- Harvard archival PaddleOCR derivative: `ALREADY-REPRESENTED / SOURCE-CONTEXT`; researcher transcript/direct primary course controls carry [^3].

### `source/institutions/`

- three EPHE OCR payloads: `ALREADY-REPRESENTED / SOURCE-CONTEXT`; official report/programme controls already supply the active-auditor and course-context claims with their ceiling.
- Smithsonian annual-report OCR: `NO-FIT / SOURCE-CONTEXT` for the present short form.

### `source/lovejoy/`

- 1898 local HTML: `BODY / NOTE`; sentence-read and promoted as described above.
- *Essays in the History of Ideas* OCR: `BIBLIO / ALREADY-REPRESENTED` for the 1901 syllabus entry; later corpus material is `NO-FIT`.
- *Primitivism and Related Ideas in Antiquity* OCR/JSON: `NO-FIT` for the current short-form center.
- two *Great Chain of Being* OCR derivatives: `NO-FIT / ALREADY-REPRESENTED` as later-method controls; no mature-method exit is restored.

### `source/reference/`

- Childers Pāli dictionary OCR: `SOURCE-CONTEXT / ALREADY-REPRESENTED`; lexical fork is already controlled in [^8].
- Daniel J. Wilson annotated bibliography OCR: `BIBLIO / SOURCE-CONTEXT`; its Buddhism index routes to the 1898 article and 1901 syllabus, with no third explicitly indexed Buddhism item promoted. It remains a later bibliographic control, not a primary Lovejoy witness.
- *Annual Register* EPUB: `SOURCE-CONTEXT / NO-FIT` for this argument.

### `source/context/`

- 1904 Bruno–Spinoza scan/OCR: `BODY / NOTE / ALREADY-REPRESENTED`; one bounded `that/what` relation-split sentence promoted via higher-grade primary dossier.
- Oltramare 1909 twelve-causes OCR: `SOURCE-CONTEXT / NO-FIT`; later field history, not evidence for Lovejoy's 1898 act.
- Max Müller, anthropology congress, Thomas 1898, Hibbert/Wiener/other periodical OCRs and contextual text witness: `SOURCE-CONTEXT / NO-FIT` unless a proposition-level source question is reopened. Indexed exception checks did not surface another Lovejoy primary object; machine code-search absence is not treated as a full-text negative proof.
- *The Hatchet* 1906 and other later contextual periodical payloads: `NO-FIT / SOURCE-CONTEXT`.

### `source/discovery/`

- two ZIP export jobs: `DISCOVERY / SOURCE-CONTEXT`; binary search exports, not prose evidence.
- Gallica and Lovejoy raw/deduplicated metadata CSVs: `DISCOVERY / SOURCE-CONTEXT / NO-FIT`; retrieval aids, not proposition witnesses.

### `source/notebooks/`

- `page_by_page_index_004_005_bilingual.md`: `ROUTER / ALREADY-REPRESENTED`; it does not outrank the 191-page integrated clean reading surface or direct-image controls.

**Source result:** current `source/` subtree is disposition-complete; no new unclassified or unregistered payload exists, and no additional body sentence arises from the remaining raw/derivative families.

## Closed candidate queue from earlier ledger state

1. Hardy wording instability / inherited two-factor architecture — **CLOSED / represented in [^7]**.
2. Oldenberg 1897 p.447 different-question/function control — **CLOSED / represented in [^7]**.
3. Cameron ownership of the p.55 Manyéma report — **NO-FIT at present**; Lovejoy's local reclassification is already safely described without expanding the note's proper-name burden.
4. MS-0873 Box 1 derivative-collection precision — **CLOSED / source distinction already explicit in [^2] and provenance controls**.

## Remaining completion queue

1. Continue the frozen `research_notes/` micro-harvest for old drafts/source dossiers not already dispositioned in the historical audit or this resumed ledger. This is now the principal remaining prose-bearing surface.
2. Reconcile any root/archive-index non-CSV prose paths that the historical ledger left unresolved; raw/code/source/transcription families are already dispositioned above.
3. When every remaining prose path has a disposition, mark this ledger `COMPLETE` and synchronize `JHI_MICRO_REUSE_TERMINAL_2026-09-05.md` without regenerating the article.
