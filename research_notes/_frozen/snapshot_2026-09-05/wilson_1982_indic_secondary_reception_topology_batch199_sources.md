# Batch 199 source register

Date: 2026-08-26
Scope: source controls for `wilson_1982_indic_secondary_reception_topology_batch199.md`.

| ID | Source | Locator / relation | Function | Grade |
|---|---|---|---|---|
| B199-S1 | Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography* (1982) | Index preface: first title-entry number is the item's annotation; subsequent numbers identify items commenting on it | defines `W-IDX-REC` semantics | direct bibliographic method |
| B199-S2 | same, title index | `The Buddhistic Technical Terms upadāna and upādisea, 19` | no subsequent indexed commentary number | direct index |
| B199-S3 | same, title index | `Syllabus: The Philosophy of Buddhism, 243` | no subsequent indexed commentary number | direct index |
| B199-S4 | same, title index | `Outline of the Védanta System of Philosophy, 176` | no subsequent indexed commentary number | direct index |
| B199-S5 | same, title index | `The Dialectic of Bruno and Spinoza, 22, 435` | positive control showing title-index reception edge | direct index |
| B199-S6 | same, entry435 | Daniel J. Wilson, `Arthur O. Lovejoy and the Moral of The Great Chain of Being` (1980) | identifies secondary item attached to 22 | direct secondary annotation |
| B199-S7 | same, Preface | secondary bibliography complete so far as Wilson knew to June 1981, with caveat for possible missed materials | bounds reception claim | direct bibliographic method |

## Graph rule

`W-IDX-REC` = a subsequent number after the primary annotation number in a Wilson title-index entry, under Wilson's explicit statement that subsequent numbers mark items commenting on the indexed work.

Examples:

- `435 → 22 [W-IDX-REC]`;
- `19 ← ∅ [W-IDX-REC]`;
- `243 ← ∅ [W-IDX-REC]`;
- `176 ← ∅ [W-IDX-REC]`.

## Cautions

- `no subsequent title-index number` means no Wilson-indexed commentary item, not no historical mention anywhere.
- Wilson's completeness claim is bounded by his own knowledge and June 1981 cutoff.
- Post-1981 reception requires an independent external survey.
