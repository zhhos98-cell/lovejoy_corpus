# Paris Batch128 parallel-subbatch reconciliation

Date: 2026-08-19
Status: canonical numbering note

Two independent Paris operations were committed concurrently under the label `Batch128`:

1. `Batch128-PALI` — the Lévi–Finot Pāli/Buddhist-translation teaching-precedent pass:
   - `research_notes/paris_1895_1899_pali_precedent_matrix_batch128.csv`
   - `research_notes/lovejoy_as_orientalist_web_sweep_batch128_Paris_Pali_precedent.md`
   - commits `28574b4d79fbfbf2a135d804fef227cd7fb02238` and `f2996993c43026a0af3c7847a899eed5ce107c5e`.

2. `Batch128-CDF` — the direct manual read of the user-supplied Collège de France faculty-minutes scans for 6 November 1898:
   - `research_notes/lovejoy_as_orientalist_web_sweep_batch128_Paris_CdF_6Nov1898_manual_scan_read.md`
   - commit `ad1ae1c91cb4772bf87e4851d434c3bb93a24077`.

This is a **batch-label collision only**. No GLA/GAL/COV identifier was minted in either operation, so there is no global archive-ID collision.

For citation and future internal references, use the descriptive canonical labels:

- `Batch128-PALI`
- `Batch128-CDF`

Do not rewrite historical commit messages. Batches 129 onward retain their existing numbering.
