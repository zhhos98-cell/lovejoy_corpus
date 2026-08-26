# Active-tree cleanup manifest — 2026-08-26

Purpose: record repository consolidation without duplicating the research argument. Files removed from the **active tree** remain recoverable through Git history.

## 1. Recovery / deletion rule

- Git history is the archive layer; do not recreate deleted working files under an `archive/` folder merely for preservation.
- Remove a batch/process/prose file only after its unique verdict and primary-source implications have an explicit living home.
- Retain primary/corrected transcriptions, source matrices, source registers, row-level data, and genuinely unique source microhistories.
- A later canonical dossier replaces the **interpretive function** of older batch prose; it does not erase the historical path by which the result was reached.
- Because `main` can receive concurrent writes, every update/delete must use the current exact blob SHA.

## 2. Current restart layer

- `CURRENT_STATE.md`
- `Quellenforschung_master_summary_2026-08-23.md`
- `research_notes/manual_primary_returns_2026-08-26.md`
- `research_notes/manual_download_click_backlog.md` — only living manual queue

## 3. Canonical thematic replacements

### 004

- `research_notes/004_proof_architecture_publication_selection_consolidated.md`
- `research_notes/004_Senart_Jacobi_Oldenberg_primary_controversy_consolidated.md`
- `research_notes/004_Hardy_causal_microgenesis_consolidated.md`
- `research_notes/004_upadisesa_lexical_semantic_recomposition_consolidated.md`
- `research_notes/lovejoy_as_orientalist_canonical_delta_batches42-47.md`

### 005 / Paris / 1902 / 1906

- `research_notes/005_Marillier_selector_alignment_consolidated.md`
- `research_notes/005_shared_source_apparatus_consolidated.md`
- `research_notes/005_Steinmetz_Mauss_controversy_context.md`
- `research_notes/005_Steinmetz_Mauss_Marillier_explanatory_level_consolidated.md`
- `research_notes/005_boundary_controls_consolidated.md`
- `research_notes/004_005_1906_diagnostic_mechanism_reaggregation_consolidated.md`
- `research_notes/004_005_1902_1906_proof_warrant_architecture_consolidated.md`

### 1904 / 1908–10

- `research_notes/Lovejoy_1904_Bruno_Spinoza_primary_consolidated.md`
- `research_notes/Lovejoy_1904_Recent_Literature_primary_consolidated.md`
- `research_notes/lovejoy_1904_evolutionists_source_criticism_proof_levels_batch189.md` — retained independent primary autopsy
- `research_notes/lovejoy_1903_stlouis_settlement_institutional_identity_and_program_batch190.md` — retained institutional object
- `research_notes/1908_1909_decomposition_recombination_reception_consolidated.md`
- `research_notes/1910_self_revision_controls_consolidated.md`

### Institutional / Indic continuity / reception

- `research_notes/AOS_membership_Indic_practice_continuity_consolidated.md`
- `research_notes/Lovejoy_1906_early_reception_Leuba_King_Jung_consolidated.md`
- `research_notes/Lovejoy_1906_citation_shadow_source_transformation_consolidated.md`
- `research_notes/Wilson_1982_Indic_reception_topology_consolidated.md`
- `research_notes/lovejoy_1898_post1981_buddhist_afterlife_memory_split_batch200.md`
- `research_notes/lovejoy_1907_deussen_vedanta_primary_review_batch201.md`

### JHI Blog

- `research_notes/JHI_blog_full_draft_v2_submission_edit_2026-08-20.md`
- `research_notes/JHI_blog_historiography_novelty_control_consolidated.md`

## 4. Current cleanup total

The cleanup line had reached **net −86 active-tree files** before the recent consolidation passes.

Subsequent net changes:

- Wilson 1982 Batches196–199 staged prose: 6 removed / 1 canonical added = **−5**;
- 1904 Batches188/191/192/193/194/195: 6 removed / 2 canonicals added = **−4**;
- proof/warrant Batches68/69/70/72/73/74/75/76/77/78/79/80: 12 removed / 1 canonical added = **−11**;
- early reception Batches81–87: 7 removed / 1 canonical added = **−6**;
- citation-shadow/source-transformation Batches91/92/93/94/97/99: 6 removed / 1 canonical added = **−5**.

Therefore:

> **Current cumulative net active-tree reduction: 117 files.**

This is a net structural count relative to the pre-cleanup working tree, not a raw deletion count.

A separately observed concurrent removal of Batch47 is not included in this cleanup-line total.

## 5. Major retired families

### State / checkpoints / logistics

Superseded restart briefs, session logs, old manual queues, resolved retrieval routes and readiness/saturation snapshots exited after their live state moved into `CURRENT_STATE.md`, `manual_download_click_backlog.md`, canonical dossiers or Git history.

### 004 source/proof chain

- Batches152–155 → `004_proof_architecture_publication_selection_consolidated.md`.
- old controversy/retrieval states including 22/32/34/42/43/44/46/151 retired after direct-primary closure.
- duplicate controversy prose → `004_Senart_Jacobi_Oldenberg_primary_controversy_consolidated.md`.
- Hardy staged prose → `004_Hardy_causal_microgenesis_consolidated.md`.
- `upādisesa` staged prose → `004_upadisesa_lexical_semantic_recomposition_consolidated.md`.
- Batch31 inference prose retired while its data concordance remained.

### 005 / Marillier / Steinmetz / Mauss

- selector/originality staged prose → `005_Marillier_selector_alignment_consolidated.md`.
- shared-source apparatus and Steinmetz/Mauss interpretation layers moved to their retained thematic objects.
- Batches33–35, 41, 147–149 staged discovery/interpretation were absorbed into later explanatory-level controls; matrices remained.

### 004→005→1906 mechanism and proof

- Batches156–157 → `004_005_1906_diagnostic_mechanism_reaggregation_consolidated.md`.
- Batches68–80 except archival Batch71 → `004_005_1902_1906_proof_warrant_architecture_consolidated.md`.
- Batch71 remains because it is archival targeting, not another proof-theory prose layer.

### 1904

- Bruno–Spinoza Batches188/192/193/194 → `Lovejoy_1904_Bruno_Spinoza_primary_consolidated.md`.
- `Recent Literature` Batches191/195 → `Lovejoy_1904_Recent_Literature_primary_consolidated.md`.
- Batch189 evolution autopsy and Batch190 St. Louis institutional object remain active because their source functions are independent.

### 1908–10

- Batches160–162/167 staged interpretation → `1908_1909_decomposition_recombination_reception_consolidated.md`.
- Batches217–218 plus terminal audit/meta prose → `1910_self_revision_controls_consolidated.md`.

### AOS / institutional continuity

Older AOS Batches68/69/70 and related staged chronology were replaced by `AOS_membership_Indic_practice_continuity_consolidated.md` once later evidence moved the last positive corporate-member control to December 1901. The active exit interval is after Dec.1901 / before Jan.1903.

### Wilson 1982

Created `Wilson_1982_Indic_reception_topology_consolidated.md` and retired six staged prose files from Batches196–199.

Retained the four `*_sources.md` registers and other structured data. Batch200 remains separate because it is post-1981 external reception.

### Lovejoy 1906 early reception — Batches81–87

Created:

- `research_notes/Lovejoy_1906_early_reception_Leuba_King_Jung_consolidated.md`.

Retired the seven prose batches covering:

- immediate Leuba/King/James/Marett reception;
- Jung 1917 proof-bearing appropriation;
- Leuba reproof through child psychology;
- Lovejoy 1914 feedback;
- Jung 1916→1917 revision insertion;
- Jung 1928 epistemic re-audit;
- King–Leuba reception triangle.

Retained reception matrices, proposition-verdict matrices and source-register deltas.

### Citation shadow / source transformation — Batches91–94,97,99

Created:

- `research_notes/Lovejoy_1906_citation_shadow_source_transformation_consolidated.md`.

Retired prose on:

- Malinowski citation shadow;
- Jones→Lovejoy→Leuba→Malinowski verdict zigzag;
- mechanical analogy spectrum / false-positive fingerprint control;
- etic retention / emic de-abstraction;
- Codrington same-source Lovejoy/Durkheim ellipsis comparison;
- Durkheim→Swain→Hardy quotation-packet inheritance.

Retained all corresponding matrices/source-register deltas.

Key safeguards retained in the canonical:

- `mechanical` / `force` / `energy` are distributed field vocabulary, not Lovejoy fingerprints;
- citation edge does not imply proposition assent;
- no direct Lovejoy→Malinowski edge is established;
- Durkheim's Codrington ellipsis is visibly marked selective quotation, not evidence of secret falsification or deceptive intent;
- Swain/Hardy establish a transmission history of the shortened quotation packet, not dependence for their entire theories.

## 6. Explicitly outside the latest reception consolidations

The following families remain active pending a separate archive/provenance audit:

- Batches88–90 — Cattell/Princeton, Lowe/ACCF/Kennedy, Eiseley/Hamburger/Hook/Tamiment archive/provenance leads;
- Batches95–96 — academic-freedom/AAUP/fonds/MS0038/Cornell documentary chains;
- Batch98 — AAUP foundation/archive synthesis;
- Batch100 — Stone/CFAT/Cattell/pensions/insurance archive leads.

These are not to be deleted merely because later reception prose has been consolidated. Before any retirement, test whether later archive-index CSVs/canonical archive syntheses fully carry their unique repository/folder/date-conflict information.

## 7. Future cleanup rule

The next cleanup pass should prefer clusters where:

1. multiple prose batches describe the same archival/reception object;
2. a later canonical or structured matrix demonstrably carries every unique finding;
3. unresolved HOLDs remain explicit after consolidation;
4. deleting prose does not remove the only human-readable map to an archive component.

If those conditions are not met, retain the file.