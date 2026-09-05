# Lovejoy corpus — routing cleanup after 2026-09-03 research expansion

Date: 2026-09-03  
Status: **AUTHORITY DRIFT CORRECTED / NO EVIDENCE MIGRATION**

## Scope

The 2026-09-02 structural cleanup established the correct repository model: living root authority files, directory-local routing guides, stable legacy payload paths, and a flat-but-routed `research_notes/` provenance layer. Research on 2026-09-03 then advanced several branches quickly: notebook 005 targeted adjudication reached Round 37, the JHI Blog writing authority moved from v3.6 to v3.7, the `primitive` argument gained the Brinton/Boas/Lovejoy three-way control, and a large Martin Guerre comparative-method sidecar was added.

The resulting problem was **authority drift**, not contradictory evidence. `CURRENT_STATE.md` and `CANONICAL_INDEX.md` had the newer state, while the root `README.md`, `PROJECT_ARGUMENT_MAP.md`, and parts of `research_notes/README.md` still routed readers through older v3.6 / Round-28-era language or gave comparative controls too much visual weight.

## Changes

Updated:

- `README.md` — rewritten as a compact repository entrance rather than a second state dossier; current state now routes to JHI v3.7, notebook 005 Round 37, the two-track model, and the five `primitive` operations.
- `PROJECT_ARGUMENT_MAP.md` — recalibrated around the current `date` versus `position` problem, the 1897–98 scale-contraction route, notebook 005 internal stratification, Lovejoy 1906 transverse reaggregation, Brinton stage-first synchronization, and Boas process-first comparability; JHI restart routing updated to v3.7.
- `research_notes/README.md` — tightened terminal routing, added current p.117 and Round 37 source/version controls, updated JHI production authority to v3.7, and collapsed the Martin Guerre cluster back behind `martin_guerre_21c_readme.md` as a comparative-method sidecar.
- `CANONICAL_INDEX.md` — updated in the same cleanup pass to route current terminal controls and this manifest.

## Explicit non-changes

No raw manuscript record, OCR payload, metadata file, export bundle, source capture, archive locator, canonical transcription batch, or historical research note was moved or deleted.

`research_notes/` remains physically flat. Root payloads remain at stable paths indexed by `root_payload_index.md`. This avoids breaking historical links and provenance chains.

No source-critical conclusion was upgraded by cleanup alone. In particular:

- page coverage remains distinct from diplomatic transcription completion;
- notebook handwriting remains distinct from proposition authorship;
- source-owned constituents remain distinct from source-owned relations;
- failed source recovery remains distinct from Lovejoy originality;
- structural comparison remains distinct from historical influence;
- Martin Guerre remains a comparative-method control, not part of the Lovejoy evidence chain.

## Current repository model

`CURRENT_STATE.md`

→ `CANONICAL_INDEX.md`

→ `PROJECT_ARGUMENT_MAP.md` / governing source or transcription gate

→ canonical page/source/index object

→ terminal dossier

→ process provenance / comparative sidecars

→ Git history.

## Current restart shorthand

> **Read `CURRENT_STATE.md`, then `CANONICAL_INDEX.md`. Use `PROJECT_ARGUMENT_MAP.md` only for the historical argument, not evidentiary authority. For notebook text or source ownership, route through the transcription/source-critical gates. Comparative sidecars remain outside the Lovejoy evidence chain unless a direct historical relation is independently established.**
