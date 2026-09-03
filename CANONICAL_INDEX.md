# Lovejoy corpus — canonical index

Last synchronized: 2026-09-03
Status: **CURRENT STABLE NAVIGATION**

This is the repository's current routing surface. `CURRENT_STATE.md` controls branch state. `TRANSCRIPTION_COMPLETION_QUEUE.md` controls the distinction between page coverage and diplomatic manuscript completion. Dated canonical indices, state deltas, sync logs, batch notes, and queue language are historical unless one of these living files explicitly routes to them.

## 1. Core authority

| Need | Use |
|---|---|
| Current project state | `CURRENT_STATE.md` |
| Diplomatic transcription completion and exact restart pages | `TRANSCRIPTION_COMPLETION_QUEUE.md` |
| Notebook coverage and residual limits | `ARCHIVE_TRANSCRIPTION_PROGRESS.md` |
| Source-critical protocol | `QUELLENFORSCHUNG_CURRENT_GATE.md` |
| Integrated working page-by-page reading surface | `archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md` |
| Full notebook-to-1898 page concordance | `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md` + `.csv` companion |
| Working/governance rules | `WORKING_RULES.md` |
| Current Blog source | `research_notes/JHI_blog_full_draft_v3_4_clean_submission_2026-08-31.md` |
| Publication-facing evidence ceilings | `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md` |
| `research_notes/` routing | `research_notes/README.md` |
| Transcription-directory authority map | `archive_transcriptions/README.md` |
| Archive-index authority map | `archive_index/README.md` |
| Legacy root payload inventory | `root_payload_index.md` |
| Repository cleanup record | `research_notes/repository_cleanup_2026-09-02.md` |

The dated `research_notes/CANONICAL_INDEX_2026-08-28.md` is retained as a historical freeze snapshot. `research_notes/REPOSITORY_CLEANUP_2026-09-01.md` records the preceding authority-consolidation pass. Neither overrides current routing.

## 2. Notebook text and material authority

### Authoritative page records

Integrated working reading surface:

- `archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md` — 004 pp.1–71 + 005 pp.1–120, generated deterministically from the canonical batches. The legacy filename contains `final`; it is not a claim of full diplomatic transcription.

Notebook 004:

- `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
- `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`

Notebook 005:

- `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json`
- `archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json`

There are no current aggregate `MS38_004_clean.json` or `MS38_005_clean.json` files. The paginated batches are authoritative page records.

**Critical status rule:** `corrected_text` is heterogeneous. It may contain diplomatic visible wording, direct-image key fragments plus conservative summary, or an editorial argument summary. Page presence and `191/191` coverage therefore do not establish diplomatic completion.

### Material and audit trails

- `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`
- `archive_transcriptions/MS38_004_001_061_004_round17_direct_image_deltas_p042_p049-052_2026-09-01.json`
- `archive_transcriptions/MS38_004_005_round18_direct_image_deltas_2026-09-01.json`
- `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`
- `research_notes/MS38_004_005_transcription_corrections_round17_original_image_2026-09-01.csv`

Directory-local authority and mutation rules: `archive_transcriptions/README.md`.

## 3. Current archival routing

### Diplomatic completion

Start with:

- `TRANSCRIPTION_COMPLETION_QUEUE.md`

Current restart order:

1. 005 pp.31–36 — source packets are now substantially narrowed by `research_notes/MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md`, but diplomatic wording remains open because printed-source collation cannot substitute for direct image reading;
2. 005 pp.42–43 — partial Greek lexical/textual slips;
3. 005 pp.47–60 — explicit Round-20 handoff, preserving existing later upgrades at p.49, p.53, and p.55;
4. remaining 005 blocks page by page;
5. 004 only when the goal expands from present argument control to a full diplomatic edition.

### Notebook 004 argument-control dossiers

- `research_notes/Lovejoy_original_image_second_pass_cross_notebook_recheck_2026-09-01.md`
- `research_notes/QUELLENFORSCHUNG_round18_residual004_broad005_hygiene_2026-09-01.md`
- `research_notes/MS38_004_round19_direct_image_reference_and_lexical_refinements_2026-09-01.md`
- `research_notes/MS38_004_round17c_p049-052_material_page_form_addendum_2026-09-01.md`

State: 71/71 first pass; targeted second-pass conceptual queue closed for present argument; exact diplomatic residue remains.

### Notebook 005 targeted-control and source-collation dossiers

- `research_notes/MS38_005_pp031-036_Marillier_source_collation_2026-09-02.md` — external-source collation; narrows source packets, does not change diplomatic text.
- `research_notes/QUELLENFORSCHUNG_round18b_005_source_evaluation_jurisdiction_and_insert_layers_2026-09-01.md`
- `research_notes/MS38_005_round19_p003-006_moral_natural_purification_direct_image_2026-09-01.md`
- `research_notes/MS38_005_round20_p016-030_contact_sociality_marillier_insert_recheck_2026-09-01.md`

State: 120/120 first-pass page coverage plus broad targeted original-image checks through Round 20; diplomatic transcription active and incomplete. For pp.31–36, the source-identification problem is narrower than the manuscript-transcription problem.

## 4. AOS 1897, Milinda, and publication selection

Full-coverage notebook-to-print authority:

- `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.md` — terminal 191-page classification and interpretive warrant;
- `research_notes/MS38_004_005_to_1898_page_concordance_full_coverage_2026-09-03.csv` — one machine-readable row per PDF page.

Use this pair for page accounting. Positive T3/T2/T1 correspondence is confined to MS38_004. MS38_005 pages marked A are analytical parallels only and must not be cited as genealogical antecedents of the 1898 article. The older `research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md` remains useful thematic discussion but is not the full-coverage authority.


Authoritative AOS dossier:

- `research_notes/AOS_1897_Lovejoy_election_read_by_title_and_technical_terms_precursor_2026-09-01.md`

Authoritative Milinda correction and supporting syntheses:

- `research_notes/Milinda_witness_reassignment_MS97_direct_image_Trenckner_p32_correction_2026-09-01.md`
- `research_notes/Milinda_source_resolution_upgrade_RhysDavids_to_Trenckner_2026-09-01.md`
- `research_notes/Milinda_1897_to_technical_terms_1898_object_reallocation_publication_selection_2026-09-01.md`
- `research_notes/004_proof_architecture_publication_selection_consolidated.md`

Use the AOS terminal dossier rather than weaker membership-only intermediate notes. Safe state: Lovejoy was absent; No. 30 was read by title; he was elected a corporate member; the Historical Study of Religions Section was instituted at the same meeting; corporate membership does not establish Section membership; the technical-terms title is a strong direct precursor to the 1898 publication, while manuscript identity remains held.

## 5. Harvard, Paris, and early formation

Start with:

- `research_notes/Harvard_Lovejoy_student_record_card_direct_transcription_and_Pali5_closure_2026-08-31.md`
- `research_notes/Harvard_Lovejoy_student_record_card_UAV161_272_5_and_AOS_1897_Milinda_2026-08-31.md`
- `research_notes/Harvard_Anthropology1_to_Paris005_classification_vs_proof_architecture_2026-08-31.md`
- `research_notes/lovejoy_harvard_orientalist_training_1895_1898.md`
- `research_notes/005_Quellenforschung_and_reading_path_reconstruction_round13_2026-08-31.md`

Stable rule: reconstruct a distributed training and research ecology. Curriculum availability, grades, institutional proximity, and teacher relation carry different proof burdens and do not by themselves establish total method transmission.

## 6. 1898–1906 and later Lovejoy

Start with:

- `research_notes/004_005_1902_1906_proof_warrant_architecture_consolidated.md`
- `research_notes/004_005_1906_diagnostic_mechanism_reaggregation_consolidated.md`
- `research_notes/1906_primitive_energetics_reception_transformation_consolidated.md`
- `research_notes/1910_self_revision_controls_consolidated.md`
- `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`

Stable ceiling: notebook and publication are different claim states; textual, semantic, logical, chronological, causal, psychological, and historical relations need separate warrants. Do not turn recurring operations into a priority or origin claim.

## 7. JHI Blog production

Writing authority:

1. `research_notes/JHI_blog_full_draft_v3_4_clean_submission_2026-08-31.md`
2. `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`
3. `research_notes/JHI_blog_v3_2_citation_hygiene_2026-08-29.md`
4. `research_notes/JHI_blog_image_caption_permission_plan_2026-08-29.md`

The v3.3 DOCX remains the latest generated and render-QA'd package. Regenerate only when moving v3.4 into production.

## 8. Comparative method and venue controls

Active matrix and handoff:

- `research_notes/unit_relation_matrix_v0_7_augmented_1892_2026_2026-08-31.tsv`
- `research_notes/HANDOFF_Lovejoy_JHI_global_history_round10_2026-08-31.md`

Representative terminal controls:

- `research_notes/Skinner_1970_1974_Mew_counterexample_scope_revision_Hobbes_Locke_case_substitution_2026-08-31.md`
- `research_notes/Pocock_1973_1984_2009_same_text_carrier_reclassification_version_proofburden_2026-08-31.md`
- `research_notes/Haddock_1976_Vico_Anachronism_fulltext_1979_JHI_sameactor_method_case_reuse_2026-08-31.md`

These lines calibrate unit, relation, revision, carrier, and canon claims. They are not a mandate to expand the current Blog.

## 9. Provenance layers

- `archive_index/` — archive coverage, locators, entity resolution, custody, and search provenance; see `archive_index/README.md`.
- `archive_transcriptions/` — canonical page records, delta registers, material audits, and integrated reading surface; see `archive_transcriptions/README.md`.
- `research_notes/` — terminal dossiers plus historical batch/process provenance; see `research_notes/README.md`.
- root payloads — legacy OCR, metadata, source text, and exports retained at stable paths and inventoried in `root_payload_index.md`.
- Git history — superseded state/navigation files and removed supersession-only process material.

A historical note can contain useful evidence while its `ACTIVE`, `HOLD`, `final`, `complete`, or `next action` language is obsolete. Follow the authority chain above.

## 10. Reopening rule

Research-argument reopening and transcription completion are separate. Reopen a frozen research line only for a new/direct primary bearing on a live proposition, a contradiction in current evidence, publication-level exact verification, or a materially necessary actor-level reconstruction of an analytical category already in use. Continue the diplomatic transcription queue whenever manuscript completion is the archival objective.
