# JHI full-repository micro-reuse audit — 2026-09-05

Status: **IN PROGRESS — corpus-wide sentence/micro-unit pass**

Authority note: this is an audit/router only. It does **not** supersede `research_notes/JHI_blog_full_draft_v3_7_clean_submission_2026-09-03.md`, `research_notes/JHI_blog_v3_7_notebook_guide_quellenkritik_calibration_2026-09-03.md`, `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`, `QUELLENFORSCHUNG_CURRENT_GATE.md`, or the terminal syntheses.

## Audit rule

The question for every tracked file is no longer only whether it supplies a central argument. The pass asks whether any sentence or record preserves a reusable micro-unit: person, institution, book/article title, course, journal, date, page, archival locator, exact phrase, URL, source relationship, provenance warning, bibliographic correction, or bounded negative finding. Reuse destinations are classified as `BODY`, `NOTE`, `LINK`, `BIBLIO`, `SOURCE-CONTEXT`, `QUARANTINE`, `NO-FIT`, or `ALREADY-REPRESENTED`.

The pass does **not** force material into the article. In particular, previously removed parallel theses (comparative `primitive`, 1906 politics, Great Chain, broad later-career exits) remain outside the body unless a genuinely local micro-unit improves an existing claim. Raw OCR/JSON, exports, binary archives, and duplicate witnesses are accounted for separately: where a canonical transcription/dossier already controls the same semantic content, the derivative is marked `ALREADY-REPRESENTED`; binary/non-prose files are not falsely described as sentence-read.

Completion criterion: **every tracked path must receive an explicit disposition**. Until then this file remains `IN PROGRESS`.

## High-confidence micro-units already recovered

| source | micro-unit | destination | action |
|---|---|---|---|
| `research_notes/004_Hardy_causal_microgenesis_consolidated.md` | R. Spence Hardy, *A Manual of Budhism, in its Modern Development* (1853), pp. 394–396; 004 p.33/ms97 explicitly cites p.394 under `Upādāna, Relation to Karma`; Hardy already separates renewed existence from the manner/specification supplied by karma | NOTE/BIBLIO | add to causal paragraph note; frame as source reworking, not Lovejoy priority |
| `research_notes/004_Senart_Jacobi_Oldenberg_primary_controversy_consolidated.md` | Oldenberg, *Buddha*, 3rd ed. (1897), pp.272–273, already rejects Senart's `upādāna = upādānakkhandha`; Lovejoy's delta is selection/reweighting/recombination, not priority | NOTE/BIBLIO/LINK | add compact priority-control note; Google Books locator available |
| `research_notes/004_upadisesa_lexical_semantic_recomposition_consolidated.md` | Oldenberg English *Buddha* (1882) p.433; Rhys Davids, *Buddhism* rev. ed. (1894) p.113; Edward Müller, *A Simplified Grammar of the Pali Language* (1884), Lovejoy cites p.30 although relevant passage is p.36; Dahlmann, *Nirvāṇa* (1896) p.14 | NOTE/BIBLIO | add lexical-source note; preserve the Müller page discrepancy rather than silently emend it |
| `research_notes/Harvard_Lovejoy_student_record_card_direct_transcription_and_Pali5_closure_2026-08-31.md` | first registration 26 Sep. 1895; Sanskrit 1¹/1² in 1895–96; Sanskrit 5 and Semitic 13 in 1896–97; Philosophy 20c paper `Have Kant's Characteristic Contributions to Philosophy a Permanent Value?` (15 Feb. 1897) | NOTE/SOURCE-CONTEXT | enrich Harvard-training note without enlarging body |
| `research_notes/lovejoy_harvard_orientalist_training_1895_1898.md` | Lanman's Harvard Oriental Series context; Henry Clarke Warren's *Buddhism in Translations* was HOS III (1896), produced in Lanman's institutional orbit and dedicated to Lanman | NOTE/SOURCE-CONTEXT | use only as contextual bridge between course environment and notebook source packet |
| `research_notes/MS0873_France_1898_99_Wilson_transcriptions_direct_read_2026-09-03.md` | 9 Oct. 1898: `philosophy and comparative religion`; 20 Oct.: Buddhism/Hebrew Wisdom and philology/philosophy split; Dec.: BnF work, Maurice Vernes, Israel Lévi, Faculty of Theology, private `Petakas` reading with Sylvain Lévi | NOTE/SOURCE-CONTEXT | enrich Paris note selectively; no single-teacher genealogy |
| `archive_index/Lovejoy_James_Walker_Fellowship_1898_99_Harvard_target_2026-09-03.md` | Harvard Corporation elected Lovejoy James Walker Fellow on 13 Jun. 1898; fellowship context helps explain why his `principal work` in Paris remained philosophy | NOTE/SOURCE-CONTEXT | candidate for Paris note if stated at the level actually supported |
| `archive_index/AOS_1897_Final_Circular_Lovejoy_title_attendance_control_2026-09-05.md` | 18 Mar. circular solicited contributor name/title and attendance separately; Hanns Oertel, Acting Corresponding Secretary, 31 York Square; 10 Apr. printed `Critical summary of the argument of the Milinda-pañha` | NOTE/BIBLIO | enrich publication-genesis note |
| `archive_index/AOS_1897_Oertel_Moore_title_workflow_control_2026-09-05.md` | Oertel was title-intake node; George F. Moore was Recording Secretary/editorial node; this identifies carrier roles but not who changed Lovejoy's title | NOTE/SOURCE-CONTEXT | use as bounded institutional context only |
| `archive_index/AOS_1897_No30_p389_direct_visual_control_2026-09-05.md` | direct visual control fixes p.389 entry: `Mr. Arthur O. Lovejoy, Harvard University; On the meaning of the Buddhist technical terms upādānam and upādāna-kkhandhā.` | NOTE/BIBLIO | already represented in current draft; retain exact roman final `m`, hyphen, macrons |
| `The Buddhistic technical terms upadana and upadisesa..html` | NTU full-text carrier; article metadata; names/citations include Warren, Burnouf, Senart, Feer, Childers, Hardy, Oldenberg, Rhys Davids, Müller, Dahlmann | LINK/BIBLIO | harvest stable link and source names where an existing note needs them |
| `research_notes/JHI_blog_v3_2_citation_hygiene_2026-08-29.md` | stable locators: Oldenberg Google Books; Senart Persée authority; Schaffer DOI; Folger/NLM Lovejoy bibliography carriers; Warren and Senart bibliographic details | LINK/BIBLIO | reuse links only where they support an already-used source |

## Path ledger — completed semantic pass so far

### Root control / production files

| path | disposition | note |
|---|---|---|
| `AGENTS.md` | ALREADY-REPRESENTED | workflow/authority constraints; no article fact |
| `CANONICAL_INDEX.md` | ALREADY-REPRESENTED | production router |
| `QUELLENFORSCHUNG_CURRENT_GATE.md` | ALREADY-REPRESENTED | source-ownership gate; used to prevent false Lovejoy attribution |
| `root_payload_index.md` | ALREADY-REPRESENTED | raw-payload router; used for accounting, not article evidence |
| `The Buddhistic technical terms upadana and upadisesa..html` | LINK/BIBLIO | primary article carrier and embedded references |

### `research_notes/` — completed high-authority/current-relevance files

| path | disposition |
|---|---|
| `README.md` | ALREADY-REPRESENTED |
| `LOVEJOY_004_TERMINAL_SYNTHESIS.md` | BODY/NOTE/ALREADY-REPRESENTED |
| `LOVEJOY_005_TERMINAL_SYNTHESIS.md` | BODY/NOTE/ALREADY-REPRESENTED |
| `LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md` | BODY/NOTE/ALREADY-REPRESENTED |
| `LOVEJOY_FORMATION_1895_1899_TERMINAL.md` | NOTE/SOURCE-CONTEXT |
| `LOVEJOY_1902_1906_EXIT_TERMINAL.md` | NO-FIT except existing 1902 exit sentence |
| `JHI_blog_v3_2_citation_hygiene_2026-08-29.md` | LINK/BIBLIO |
| `JHI_blog_v3_7_notebook_guide_quellenkritik_calibration_2026-09-03.md` | ALREADY-REPRESENTED |
| `JHI_blog_v3_7_round0_7_calibration_control_2026-09-05.md` | ALREADY-REPRESENTED; prevents re-expansion |
| `004_Senart_Jacobi_Oldenberg_primary_controversy_consolidated.md` | NOTE/BIBLIO/LINK |
| `004_Hardy_causal_microgenesis_consolidated.md` | NOTE/BIBLIO |
| `004_proof_architecture_publication_selection_consolidated.md` | NOTE/SOURCE-CONTEXT |
| `004_upadisesa_lexical_semantic_recomposition_consolidated.md` | NOTE/BIBLIO |
| `005_Marillier_selector_alignment_consolidated.md` | QUARANTINE/NOTE only if needed for source priority |
| `005_boundary_controls_consolidated.md` | NO-FIT for current article except provenance warnings |
| `Harvard_Lovejoy_student_record_card_direct_transcription_and_Pali5_closure_2026-08-31.md` | NOTE/SOURCE-CONTEXT |
| `lovejoy_harvard_orientalist_training_1895_1898.md` | NOTE/SOURCE-CONTEXT; stale claims must yield to direct card control |
| `MS0873_France_1898_99_Wilson_transcriptions_direct_read_2026-09-03.md` | NOTE/SOURCE-CONTEXT |

### `archive_index/` — completed prose control files

| path | disposition |
|---|---|
| `AOS_1896_1897_abstract_procedure_control_2026-09-05.md` | NOTE/SOURCE-CONTEXT |
| `AOS_1897_1899_1919_bylaw_recordbook_control_2026-09-05.md` | NOTE/SOURCE-CONTEXT; record-book existence rule, not surviving-volume proof |
| `AOS_1897_AV_Williams_Jackson_editor_carrier_control_2026-09-05.md` | SOURCE-CONTEXT/NO-FIT |
| `AOS_1897_Baltimore_contemporaneous_press_carriers_2026-09-05.md` | NO-FIT; useful negative control only |
| `AOS_1897_Final_Circular_Lovejoy_title_attendance_control_2026-09-05.md` | NOTE/BIBLIO |
| `AOS_1897_Ira_Price_Semitic_Club_carrier_control_2026-09-05.md` | NO-FIT; no Lovejoy hit |
| `AOS_1897_No30_p389_direct_visual_control_2026-09-05.md` | NOTE/BIBLIO/ALREADY-REPRESENTED |
| `AOS_1897_Oertel_Moore_title_workflow_control_2026-09-05.md` | NOTE/SOURCE-CONTEXT |
| `Dorsey_Brinton_1894_Harvard_General_Anthropology_curriculum_exchange_target_2026-08-31.md` | QUARANTINE; comparative branch frozen |
| `Harvard_History_of_Religions_Club_Lovejoy_attendance_1895_98_target_2026-08-31.md` | QUARANTINE; participation unresolved |
| `Harvard_permission_request_receipt_UAV161_272_5_2026-09-03.md` | NO-FIT; permissions state only |
| `JHU_MS0038_box38_folder10_Manitouism_unprinted_parts_Religion_Lectures_1900_1906_2026-09-03.md` | NO-FIT; later branch |
| `JHU_MS0038_box61_folder2_Mathematics_notebook_Gospel_historicity_early_warrant_target_2026-09-03.md` | QUARANTINE; content/date not controlled enough |
| `JHU_MS0038_box62_item3_totemism_1898_99_Bibliotheque_Nationale_target_2026-09-03.md` | QUARANTINE; provenance probabilistic, content unopened |
| `JHU_MS0873_MS0038_remote_reproduction_status_2026-09-03.md` | SOURCE-CONTEXT/NO-FIT; archive logistics/provenance |
| `JHU_Philological_Association_1897_local_host_carrier_2026-09-05.md` | NOTE/LINK candidate; local-host context only |
| `JHU_RG04090_Paul_Haupt_1878_1916_carrier_ceiling_2026-09-05.md` | NO-FIT; no 1897 container recovered |
| `LOVEJOY_1897_SESSION_HANDOFF_2026-09-05_1336.md` | QUARANTINE/STALE; contains superseded p.380 state and must not override p.389 visual control |
| `Lovejoy_1898_Paris_Wisdom_work_named_carrier_target_2026-09-03.md` | NOTE/SOURCE-CONTEXT for named Paris work; archival folder hypotheses remain targets only |
| `Lovejoy_1915_Declaration_draft_version_packet_exact_targets_2026-09-03.md` | NO-FIT; later branch removed |
| `Lovejoy_James_Walker_Fellowship_1898_99_Harvard_target_2026-09-03.md` | NOTE/SOURCE-CONTEXT |
| `Lovejoy_UC_Magazine_1896_1902_primary_packet_and_editorial_provenance_target_2026-09-03.md` | BIBLIO/NO-FIT; early publication list, not needed in present body |
| `Lovejoy_primary_acquisition_priority_queue_2026-09-03.md` | ALREADY-REPRESENTED/NO-FIT; acquisition router |
| `MS0038_Graduate_Philosophical_Society_minutes_box37_folder1_2026-09-05.md` | QUARANTINE; requested/unopened, not evidence |
| `README.md` | ALREADY-REPRESENTED |
| `Yale_AOS_1897_recordbook_locator_search_2026-09-05.md` | SOURCE-CONTEXT; exact 1897 successor shelfmark unresolved |
| `Yale_RU129_YRG37_AOS_records_management_survey_1978_1980_2026-09-05.md` | NO-FIT; 1978–80 survey is not the 1897 record book |
| `research_correspondence_Lovejoy_archive_and_JHI_crosswalk_2026-09-02.md` | SOURCE-CONTEXT/NO-FIT; correspondence/provenance router |

## Still to traverse before closure

1. Remaining `research_notes/` prose controls, older drafts, source dossiers, bibliography/link registers, and experimental branches: harvest unique micro-units but do not revive superseded claims.
2. Every `archive_index/*.csv`: inspect row-level names, repositories, locators, dates, URLs, and negative controls; route only article-local units.
3. Every `archive_transcriptions/` path: account raw page/transcription derivatives against 004/005/formation controls and inspect any unique filename/provenance metadata.
4. Every root raw payload (`*.json`, `*.txt`, `*.csv`, `*.epub`, `*.zip`): classify whether semantically controlled, uniquely reusable, binary/non-prose, or duplicate.
5. `tools/`: account scripts/configuration as reproducibility infrastructure; inspect comments/embedded source locators for any unique links.
6. Patch the canonical JHI draft only after candidate harvesting is stable enough to avoid note churn.

## Non-negotiable corrections during this pass

- Printed June 1897 Proceedings locator is **p.389**, not p.380.
- Exact June entry is `upādānam` (roman final `m`) and `upādāna-kkhandhā`.
- The exact 10 Apr → June title-transition mechanism remains open.
- `read by title, and with or without a brief statement` is a group-level formula and does not establish whether Lovejoy supplied a brief statement.
- Harvard student-card evidence controls actual registered courses; older inference-heavy dossiers yield to it.
- A finding-aid target, request receipt, or archival probability is not upgraded into document content.
