# Lovejoy corpus — root payload index

Date: 2026-09-04  
Status: **STRUCTURAL INVENTORY / LEGACY PATHS PRESERVED**

This file accounts for tracked files that remain directly in the repository root but are not living navigation/governance files. Root payloads are intentionally retained at stable paths because many historical notes and commits refer to them. Presence here means **preserved and indexed**, not **canonical authority**.

Current living root controls are `README.md`, `CONSOLIDATED_RESEARCH_ENTRYPOINT.md`, `CURRENT_STATE.md`, `TRANSCRIPTION_COMPLETION_QUEUE.md`, `CANONICAL_INDEX.md`, `ARCHIVE_TRANSCRIPTION_PROGRESS.md`, `QUELLENFORSCHUNG_CURRENT_GATE.md`, and `WORKING_RULES.md`. Directory-level routing is in `archive_transcriptions/README.md`, `archive_index/README.md`, and `research_notes/README.md`.

## 1. Lovejoy primary / near-primary text payloads

- `The Buddhistic technical terms upadana and upadisesa..html` — Lovejoy 1898 Buddhist article text witness.
- `Essays in the history of ideas -- Lovejoy, Arthur O_ (Arthur Oncken), 1873-1962; Johns Hopkins -- 1948 -- Johns Hopkins Press -- cc7531823bda79c765b81259197e7f9c -- Anna’s Archive.pdf_by_PaddleOCR-VL-1.6.json` — OCR payload for *Essays in the History of Ideas*.
- `THE GREAT CHAIN OF BEING -- ARTHUR O_ LOVEJOY -- 1966 -- 2e5f16e16c0949b3f83865561f0d1beb -- Anna’s Archive.pdf_by_PaddleOCR-VL-1.6.json` — OCR witness/edition of *The Great Chain of Being*.
- `The Great Chain of Being A Study of the History of an Idea (Arthur O. Lovejoy) (z-library.sk, 1lib.sk, z-lib.sk).pdf_by_PaddleOCR-VL-1.6.json` — second OCR witness/edition of *The Great Chain of Being*; retained because it is not an exact-content duplicate of the preceding file.
- `Primitivism and related ideas in antiquity -- Lovejoy, Arthur O_ (Arthur Oncken), 1873-1962, Boas, George, -- Contributions to the history of -- oclc 1036786831 -- 250cd1e7a22202fb5935aa4ffb12bac3 -- Anna’s Archive..json` — OCR/text payload for *Primitivism and Related Ideas in Antiquity*.
- `提取自studiesinphilos00univgoog.pdf_by_PaddleOCR-VL-1.6.json` — legacy extracted periodical/book payload used in early Lovejoy source work; preserve path until identity/reference migration is explicitly mapped.

## 2. Archival discovery, bibliography, and institutional context

- `MS_0038.pdf_by_PaddleOCR-VL-1.6.json` — JHU MS-0038 finding-aid/archive baseline.
- `Arthur O. Lovejoy An Annotated Bibliography (Daniel J. Wilson) (z-library.sk, 1lib.sk, z-lib.sk).pdf_by_PaddleOCR-VL-1.6.json` — Daniel J. Wilson bibliography OCR.
- `URN-3-HUL.ARCH-39991521.pdf_by_PaddleOCR-VL-1.6.json` — Harvard archival/catalogue witness used for course/context control.
- `hvd-hnav7c-1787789071.txt` — Harvard-derived legacy text payload; retain stable path until a mapped rename is justified.
- `The Hatchet 1906.pdf_by_PaddleOCR-VL-1.6.json` — 1906 institutional/periodical context payload.
- `Quellenforschung_master_summary_2026-08-23.md` — legacy root synthesis; useful provenance, but current routing is controlled by `QUELLENFORSCHUNG_CURRENT_GATE.md` and `CANONICAL_INDEX.md`.

## 3. Comparative religion, Orientalist, anthropological, and reception sources

- `ephe_0000-0002_1893_num_7_3_19382.pdf_by_PaddleOCR-VL-1.6.json` — Léon Marillier, *La survivance de l'âme et l'idée de justice chez les peuples non civilisés*; critical external-source witness for notebook 005.
- `EPHE_20190568_391_Programmes.pdf_by_PaddleOCR-VL-1.6.json` — EPHE programmes.
- `EPHE_20200033_174_Affiches.pdf_by_PaddleOCR-VL-1.6.json` — EPHE notices/affiches context.
- `b22427624.pdf_by_PaddleOCR-VL-1.6.json` — legacy Buddhist/Orientalist printed-source OCR; preserve opaque source identifier.
- `Wiener_Zeitschrift_für_die_Kunde_des_Mo.pdf_by_PaddleOCR-VL-1.6.json` — Orientalist periodical source payload.
- `S0035869X00145927.pdf_by_PaddleOCR-VL-1.6.json` — legacy periodical/review OCR witness.
- `35.pdf_by_PaddleOCR-VL-1.6.json` — legacy numbered printed-source OCR; identity remains path-opaque and should be normalized only through a reference migration.
- `Annual_Report_of_the_Board_of_Regents_of.pdf_by_PaddleOCR-VL-1.6.json` — Smithsonian/Board of Regents anthropological source payload.
- `Memoirs_of_the_International_congress_of_anthropology_(IA_memoirsofinterna00inte).pdf_by_PaddleOCR-VL-1.6.json` — anthropology congress source payload.
- `hibbertjournal05londuoft.pdf_by_PaddleOCR-VL-1.6.json` — *Hibbert Journal* context/reception payload.
- `F_Max_Müller_als_Mythendichter(OCR).pdf_by_PaddleOCR-VL-1.6.json` — Max Müller reception/context payload.
- `THEREV~1.PDF_by_PaddleOCR-VL-1.6.json` — legacy short-name OCR payload; identity should be resolved from usage before any rename.
- `Annual_Register.epub` — legacy annual-register source payload.

## 4. Harvest, metadata, and export payloads

- `lovejoy_metadata_raw.csv` — raw metadata harvest.
- `lovejoy_metadata_deduped.csv` — deduplicated metadata derivative.
- `gallica_query_summary.csv` — Gallica query/run summary.
- `gallica_lovejoy_primitive_deduped.csv` — deduplicated Gallica primitive/Lovejoy result set.
- `export_job_27972014.zip` — legacy export bundle.
- `export_job_27972044.zip` — legacy export bundle.

## 5. Preservation and migration rule

Do not rename or move a root payload merely to make the tree look cleaner. A path migration is justified only when all of the following are done together:

1. establish source identity and target canonical name;
2. create a machine-readable old-path -> new-path redirect map;
3. rewrite tracked Markdown/backtick references where appropriate;
4. preserve provenance for opaque source identifiers;
5. run `python tools/audit_repository.py` and inspect any warnings;
6. commit the migration as one auditable operation.

New source payloads should normally enter an appropriate subdirectory rather than the root. If a new root payload is unavoidable, add it to this index in the same commit. The repository audit enforces that rule.
