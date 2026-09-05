# Lovejoy corpus — canonical index

Last synchronized: 2026-09-05  
Status: **CONSOLIDATED STABLE NAVIGATION**

The repository is provenance-rich but the active authority surface is intentionally narrow. Do not recursively scan `research_notes/_frozen/`, `archive_index/_frozen/`, or raw `source/` payloads unless an active control identifies a specific need.

## 1. Start here

| Need | Use |
|---|---|
| Human/agent research router | `CONSOLIDATED_RESEARCH_ENTRYPOINT.md` |
| Current open/closed/frozen state | `CURRENT_STATE.md` |
| Short-form completion decisions | `LOVEJOY_SHORTFORM_COMPLETION_CHECKLIST.md` |
| Historical argument architecture | `PROJECT_ARGUMENT_MAP.md` |
| Source-critical protocol | `QUELLENFORSCHUNG_CURRENT_GATE.md` |
| Diplomatic/image completion | `TRANSCRIPTION_COMPLETION_QUEUE.md` |
| Notebook page coverage/residual limits | `ARCHIVE_TRANSCRIPTION_PROGRESS.md` |
| Article editing/calibration protocol | `AGENTS.md` |
| Working/governance rules | `WORKING_RULES.md` |
| Raw/near-raw source router | `source/SOURCE_INDEX.md` |
| Archive locator/acquisition router | `archive_index/ARCHIVE_ROUTER.md` |
| Curated exact-witness router | `research_notes/evidence/README.md` |
| Frozen research provenance | `research_notes/FROZEN_PROVENANCE_REGISTER.md` |

## 2. Terminal research syntheses

| Question | Default synthesis |
|---|---|
| Notebook 004 | `research_notes/LOVEJOY_004_TERMINAL_SYNTHESIS.md` |
| Notebook 005 | `research_notes/LOVEJOY_005_TERMINAL_SYNTHESIS.md` |
| 1897 AOS -> 1898 JAOS publication genesis | `research_notes/LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md` |
| Harvard/Boston/Paris formation 1895–99 | `research_notes/LOVEJOY_FORMATION_1895_1899_TERMINAL.md` |
| 1902/1906 later exits and scale control | `research_notes/LOVEJOY_1902_1906_EXIT_TERMINAL.md` |

If a terminal synthesis closes a domain, do not re-run its historical batch/round/sweep files merely because they remain in the frozen snapshot.

## 3. Exact notebook text authority

Authoritative page records are the paginated `*_clean.json` batches under `archive_transcriptions/`.

Integrated reading surface:

- `archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md`.

Full notebook-to-1898 correspondence witness:

- `research_notes/evidence/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md`.

Critical rule:

> `PAGE COVERAGE != DIPLOMATIC TRANSCRIPTION COMPLETION`.

The integrated filename's `final` is legacy path provenance, not a diplomatic-completion claim.

## 4. 1897–1898 publication-genesis evidence

Start with `research_notes/LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md`, then use only the exact control required:

- p.389 visual/diplomatic control: `archive_index/AOS_1897_No30_p389_direct_visual_control_2026-09-05.md`;
- title/carrier recovery: `research_notes/evidence/AOS_1897_No30_upadana_upadanakkhandha_title_recovery_2026-09-04.md`;
- 18 Mar / 10 Apr circular architecture: `archive_index/AOS_1897_Final_Circular_Lovejoy_title_attendance_control_2026-09-05.md`;
- abstract/brief-statement procedure: `archive_index/AOS_1896_1897_abstract_procedure_control_2026-09-05.md`;
- AOS record-book duties: `archive_index/AOS_1897_1899_1919_bylaw_recordbook_control_2026-09-05.md`;
- notebook-to-print concordance: `research_notes/evidence/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md`;
- archive/custody context only if specifically needed: `archive_index/ARCHIVE_ROUTER.md`.

Current direct diplomatic state is printed p.389: `upādānam / upādāna-kkhandhā`. The 10 Apr -> June transition mechanism and exact April meeting title remain bounded unknowns, not writing blockers.

## 5. Formation evidence

Start with `research_notes/LOVEJOY_FORMATION_1895_1899_TERMINAL.md`.

Repeated exact witnesses are:

- `research_notes/evidence/MS0873_France_1898_99_Wilson_transcriptions_direct_read_2026-09-03.md`;
- `research_notes/evidence/Harvard_Lovejoy_student_record_card_direct_transcription_and_Pali5_closure_2026-08-31.md`.

Course availability, enrollment/grade, teacher relation, institutional proximity, attendance, private reading, and methodological transmission remain separate propositions. Older broad formation sweeps are frozen provenance.

## 6. Archive/source-critical live work

Use `CURRENT_STATE.md` for exact HOLDs and `LOVEJOY_SHORTFORM_COMPLETION_CHECKLIST.md` for blocking versus non-blocking status.

Notebook 004 broad source work is closed for present purposes. Notebook 005 retains only explicit source/version and diplomatic HOLDs; broad 005 source hunting remains closed.

The 1897 AOS online-discovery phase is closed at its public ceiling. Direct p.389 typography is closed. JHU/Yale/AOS physical or slow archival follow-up is **optional future upgrade / not required for the current short form**. Paul Haupt is de-prioritized unless new container metadata appears.

## 7. JHI Blog production

Canonical prose authority:

1. `research_notes/JHI_blog_full_draft_v3_7_clean_submission_2026-09-03.md`
2. `research_notes/JHI_blog_v3_7_notebook_guide_quellenkritik_calibration_2026-09-03.md`
3. `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`
4. `QUELLENFORSCHUNG_CURRENT_GATE.md`
5. `AGENTS.md`

`research_notes/JHI_FULL_REPO_MICRO_REUSE_AUDIT_2026-09-05.md` is a bounded current audit control, not a successor prose draft and not authority to reopen corpus-wide research.

Earlier drafts, round controls, and experimental JHI notes are frozen provenance unless explicitly promoted here or in `CURRENT_STATE.md`.

## 8. Frozen branches

The Brinton–Boas–Lovejoy `primitive` comparative triangle remains frozen and excluded from production by default.

Historical process files are preserved at:

- `research_notes/_frozen/snapshot_2026-09-05/` — old research rounds, batches, sweeps, handoffs, drafts, source-specific process notes;
- `archive_index/_frozen/snapshot_2026-09-05/` — old archive harvests, batch CSVs, negative searches, repository coverage, superseded acquisition targets.

Do not traverse either snapshot by default.

## 9. Repository layers

- `source/` = raw and near-raw source payloads, classified by source type/context;
- `archive_index/` = curated locator, custody, acquisition, and source-identity controls;
- `archive_transcriptions/` = canonical page records, image/material audits, integrated reading surface;
- `research_notes/evidence/` = small repeatedly reused exact-witness dossiers;
- `research_notes/` top level = terminal syntheses + current production controls;
- `_frozen/` snapshots = provenance/recovery layers;
- Git history = final recovery layer.

No historical provenance has been discarded by this consolidation; it has been removed from the default search surface.

## 10. Authority rule

Default sequence:

> **AGENTS/editing protocol -> living control -> terminal synthesis -> curated exact witness -> canonical transcription/raw source/archive locator only if needed -> frozen provenance only for a specifically named question**

Historical status words inside dated notes do not override this index.