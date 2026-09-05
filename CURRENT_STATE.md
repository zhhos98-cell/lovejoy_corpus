# Lovejoy corpus — current state

Last synchronized: 2026-09-05  
Status: **SHORT-FORM ARGUMENT READY / ACTIVE SURFACE CONSOLIDATED / HISTORICAL PROCESS FROZEN**

This is the single living state file. Historical status language elsewhere does not override it.

Default entry: `CONSOLIDATED_RESEARCH_ENTRYPOINT.md`. Do not begin from a full-repository scan.

## 1. Active research domains

### Notebook 004

Default synthesis: `research_notes/LOVEJOY_004_TERMINAL_SYNTHESIS.md`.

State: **71/71 first-pass pages; argument-level source ownership closed for the present project.** Remaining residue is diplomatic, micro-paleographic, foreign-language, bibliographic, or exact-quotation level. Reopen broad 004 work only for a direct new witness, contradiction, publication-grade exact quotation, or source identification that could materially change authorial attribution.

### Notebook 005

Default synthesis: `research_notes/LOVEJOY_005_TERMINAL_SYNTHESIS.md`.

State: **120/120 first-pass pages; broad source ownership closed; diplomatic transcription incomplete.** Live HOLDs remain controlled by `TRANSCRIPTION_COMPLETION_QUEUE.md`, especially p.117, p.55, p.90, p.87, p.33/p.36, and pp.92–99. They do not block the current 004-centered short form unless a final sentence directly depends on them.

Do not resume broad 005 source hunting.

### 1897–1898 publication genesis

Default synthesis: `research_notes/LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md`.

Secure carrier chain:

`10 Apr 1897 — Final Circular: Critical summary of the argument of the Milinda-pañha`

→ `22–24 Apr — Baltimore meeting: No.30 later recorded among papers read by title; Lovejoy-specific brief-statement status OPEN; exact meeting title OPEN`

→ `June 1897 — JAOS 18 Second Half: printed Proceedings p.389 gives On the meaning of the Buddhist technical terms upādānam and upādāna-kkhandhā`

→ `1898 — The Buddhistic technical terms upādāna and upādisesa`.

Direct p.389 typography is **CLOSED**. The June technical title is a post-meeting printed-carrier state and must not automatically be dated to 22–24 April. The 10 Apr -> June mechanism remains unknown. Treat each carrier as a distinct documentary state; do not infer one unchanged manuscript.

Short-form status: **argument-ready**. No JHU/Yale/AOS physical archival recovery is required for the current piece. Such work is optional future upgrading only; it is not an active research queue and need not be mentioned in finished prose unless rhetorically useful.

Exact active witnesses:

- `research_notes/evidence/AOS_1897_No30_upadana_upadanakkhandha_title_recovery_2026-09-04.md`;
- `archive_index/AOS_1897_No30_p389_direct_visual_control_2026-09-05.md`;
- `research_notes/evidence/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md`.

Archive/custody history is routed separately through `archive_index/ARCHIVE_ROUTER.md` and should not be traversed by default.

### Formation 1895–1899

Default synthesis: `research_notes/LOVEJOY_FORMATION_1895_1899_TERMINAL.md`.

Strongest actor-level controls are now promoted into `research_notes/evidence/`:

- Harvard student record / advanced-Pāli enrollment closure;
- JHU MS-0873 Wilson transcription witness for Paris 1898–99.

Current safe result: Lovejoy combined philosophical training with technical Buddhist/Indic and comparative-religion work; in 1898 he explicitly formulated a problem produced by the split between philological textual expertise and philosophical reconstruction. Do not convert this into a single-teacher genealogy. Wilson's Paris witness remains an archival transcription, not autograph-level inspection.

### 1902–1906 exits

Default synthesis: `research_notes/LOVEJOY_1902_1906_EXIT_TERMINAL.md`.

Use later material only as scale/reaggregation control. Do not reopen it as a retrospective key to notebooks 004/005.

## 2. Current JHI production state

Canonical prose: `research_notes/JHI_blog_full_draft_v3_7_clean_submission_2026-09-03.md`.

Calibration/evidence authority is defined in `CANONICAL_INDEX.md` and `AGENTS.md`. Repository consolidation does not authorize a successor draft, a whole-draft regeneration, or another corpus-wide research sweep.

The former full-repository micro-reuse audit is **frozen**. Reusable small units are consolidated in `research_notes/JHI_MICRO_REUSE_TERMINAL_2026-09-05.md`. Micro-reuse is now demand-driven by a specific sentence or note.

## 3. Repository routing state

Active layers are now:

- `research_notes/` — terminal syntheses + current JHI production controls;
- `research_notes/evidence/` — four repeatedly reused exact-witness dossiers;
- `archive_transcriptions/` — canonical notebook records/direct-image controls;
- `archive_index/` — curated locator/acquisition/custody controls;
- `source/` — classified raw and near-raw payloads.

Historical layers are preserved but non-routing:

- `research_notes/_frozen/snapshot_2026-09-05/`;
- `archive_index/_frozen/snapshot_2026-09-05/`;
- Git history.

Do not recurse into frozen snapshots or raw OCR payloads by default.

## 4. Governing firewalls

- `PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION`.
- `NOTEBOOK HANDWRITING != PROPOSITION AUTHORSHIP`.
- `SOURCE-OWNED CONSTITUENTS != SOURCE-OWNED RELATION`.
- `FAILED SOURCE RECOVERY != LOVEJOY ORIGINALITY`.
- `CITATION / ADJACENCY != UPTAKE / ASSENT`.
- `TITLE CONTINUITY != MANUSCRIPT IDENTITY`.
- `MEETING DATE != AUTOMATIC DATE OF A TITLE PRINTED IN JUNE PROCEEDINGS`.
- `READ BY TITLE != BARE TITLE ONLY`.
- `GROUP-LEVEL WITH/WITHOUT BRIEF STATEMENT != LOVEJOY-SPECIFIC BRIEF STATEMENT`.
- `NORMALIZED TERM FORM != DIPLOMATIC PRINTED TITLE FORM`.
- `PUBLIC CATALOGUE NO-HIT != ARCHIVAL ABSENCE`.
- `INSTITUTIONAL PROXIMITY != ATTENDANCE / UPTAKE / INFLUENCE`.
- `MORPHOLOGICAL ORDER != HISTORICAL ORDER`.
- `CROSS-ACTOR ANALYTICAL SIMILARITY != HISTORICAL ARGUMENT`.

Compact Lovejoy-local control:

> **one relation is not allowed automatically to answer for another.**

## 5. Frozen branches

The Brinton–Boas–Lovejoy `primitive` triangle remains frozen and excluded from production. Historical batch/round/sweep/delta files, old handoffs, generic archive searches, and superseded draft states remain provenance only.

## 6. Default continuation

When the user says `continue`, identify the domain first and enter through its terminal control:

- 004 -> `research_notes/LOVEJOY_004_TERMINAL_SYNTHESIS.md`;
- 005 -> `research_notes/LOVEJOY_005_TERMINAL_SYNTHESIS.md`;
- AOS / Milinda / 1897–98 -> `research_notes/LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md`;
- Harvard / Paris -> `research_notes/LOVEJOY_FORMATION_1895_1899_TERMINAL.md`;
- 1902/1906 -> `research_notes/LOVEJOY_1902_1906_EXIT_TERMINAL.md`;
- exact notebook wording -> `archive_transcriptions/` + `TRANSCRIPTION_COMPLETION_QUEUE.md`;
- archive locator/custody -> `archive_index/ARCHIVE_ROUTER.md`;
- raw source payload -> `source/SOURCE_INDEX.md`;
- Blog -> `CANONICAL_INDEX.md` + `AGENTS.md`.

Do not interpret `continue` as permission to resume a full-repository or full-archive sweep.