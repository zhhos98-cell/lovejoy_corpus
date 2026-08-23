# Archive-side Batch 116 — JHU presidential departmental-file architecture and the Stanford Jordan microfilm extent problem

Date: 2026-08-19  
Status: synced  
Scope: continue Batch115's two most bounded retrieval problems: translate the old Hamburger-Archives citation for the Hopkins–Russell packet into a more exact RG-02-001 Series 1 departmental-file request, and determine whether the David Starr Jordan microfilm edition can be used as a reliable derivative route toward the 15 April 1901 Lovejoy→Elliott manifestation test.

## Core result

Batch116 adds **no new GLA component** and **no new GAL lead**. The next unassigned component remains `GLA0057`; the next unassigned lead remains `GAL0047`.

The Johns Hopkins side becomes substantially more precise. Two independently published legacy citations show that `RG-02-001 / Office of the President / Series 1` contained numbered **departmental subject files**:

- **File 56 — Department of Philosophy and Psychology**, used in scholarship on the James Mark Baldwin affair and citing material through 1910;
- **File 115 — Department of Psychology, 1913-1919 / 1920-1921**, used in published archival work on John B. Watson and Frank J. Goodnow.

Current JHU authority description independently states that Philosophy, Psychology, and Education were combined from 1908 to 1915 and split into separate departments around 1915. The current Philosophy finding aid gives the same institutional break more precisely as a formal division into three seminaries in **1915-1916**, and identifies Arthur O. Lovejoy as Professor of Philosophy from 1910.

These controls do not reveal the file number for the post-1915 Department of Philosophy. They do, however, change the retrieval target for canonical `GLA0030` / BRACERS `121122` from:

`search RG-02-001 for Lovejoy/Russell`

to:

`RG-02-001 -> Series 1 -> Department of Philosophy -> 1915-1917 -> Lovejoy / Russell / lecture / visiting appointment / technical philosophy / war-pacifism`.

That is a genuine increase in physical precision without inventing a locator.

The Stanford side produces a different kind of result. The official NHPRC project catalog describes the **David Starr Jordan Papers microfilm edition** as **187 reels with a 31-page guide**. A Library of Congress catalog-derived description, however, reports an LC holding of **184 microfilm reels**, local shelving `Microfilm 17,501-184P`, with a finding aid available in the Manuscript Reading Room. The source describes the film as being made from originals in the Stanford University Archives.

This becomes `GAC0008`, but it is deliberately classified as a **representation-level extent discrepancy**, not as evidence that three reels are missing or that Lovejoy material differs between copies. The NHPRC number may describe the complete published edition while the LC number may describe a particular institutional holding, a variant catalog state, or a subset. Only reel-level comparison can resolve it.

The 31-page guide did not surface as freely indexed full text in this pass. It therefore remains a retrieval object rather than an inspected source.

---

## 1. JHU Series 1 preserves a departmental-subject-file architecture

Batch115 established one exact old-label/current-record-group bridge: archival scholarship citing the historical `Ferdinand Hamburger, Jr. Archives` also gave `RG 02.001 / Office of the President / Series 1 / File 115 / Department of Psychology` for Watson/Goodnow correspondence.

Batch116 adds an earlier control from published work on James Mark Baldwin:

`Records of the Office of the President / RG 02.001 / Series 1 / File No. 56 / Department of Philosophy and Psychology`.

This matters because the two controls bracket an institutional reorganization.

Current JHU authority history gives:

- Department of Philosophy and Psychology: **1903-1908**;
- Department of Philosophy, Psychology, and Education: **1908-1915**;
- around **1915**, the three fields separated into their own departments.

Current Philosophy Department history adds that they were formally divided into three seminaries in **1915-1916**.

Thus the archival controls are coherent with the institutional chronology:

`pre-split combined department -> numbered Series 1 departmental file (File 56)`

`post-split Psychology -> distinct numbered Series 1 departmental file (File 115)`.

The most economical hypothesis is therefore not a specific file number but a filing class: a **post-1915 Department of Philosophy Series 1 subject file** is now the correct thing to ask the repository to identify.

### What this licenses

A reference request can now say:

> Please identify the Office of the President records, RG-02-001, Series 1 file(s) for the Department of Philosophy covering approximately 1915-1917, especially correspondence or memoranda concerning Arthur O. Lovejoy, Bertrand Russell, visiting lectures or appointments.

### What it does not license

It does not establish:

- that the Philosophy file still survives;
- that it had one continuous file number;
- that it was adjacent to File 115;
- that BRACERS `121122` is in it;
- that Goodnow was the recipient of `121122`;
- that File 56 continued after the 1915 split.

The gain is **series + filing class + department + date**, not an invented box/file number.

---

## 2. RG-04-120 remains a later archival domain, not the direct 1916 path

The current Philosophy Department records, `RG-04-120`, begin in 1922, while their Administrative Records begin in 1942. The same finding aid nevertheless provides the history of the 1915-16 institutional split and Lovejoy's role.

This is a useful illustration of the distinction already adopted in Batch114:

`institutional history represented in a finding aid`

`!= physical date coverage of that record group`.

The 1916 Russell-planning document can be historically a Department of Philosophy record without surviving in the current Department of Philosophy record group. The presidential Series 1 file architecture is therefore currently the stronger route for an original or office-copy manifestation.

---

## 3. Stanford microfilm: the guide exists, but the public web does not yet expose it

The official National Archives NHPRC catalog states that Stanford University Libraries produced a David Starr Jordan Papers microfilm edition containing correspondence, writings, pamphlets, leaflets, clippings and photographs, including substantial Stanford University material. It gives the extent as:

`187 reels + 31-page guide`.

The NHPRC page points to Stanford SearchWorks record `4085322` and OCLC `1260484`, but the 31-page guide itself did not surface as readable full text in the present web sweep.

The current OAC finding aid independently records the physical-history fact that, after the microfilm edition had been approved, **59 volumes of Jordan letter books, chronological files**, were transferred from the Registrar's Office to the Archives.

That chronology is important but ambiguous. It does not tell us whether those 59 volumes:

- were transferred in time to be filmed;
- were included only partly;
- were excluded from the filmed corpus;
- or were represented under another microfilm series.

Therefore the microfilm edition cannot yet be treated as a completeness proxy for the 1901 letterpress manifestation test.

---

## 4. The Library of Congress holding introduces GAC0008

A current catalog-derived archival directory record for the Library of Congress Manuscript Division reports:

- title: `David Starr Jordan papers, 1861-1964`;
- additional format: microfilm of originals in the Stanford University Archives;
- extent: **184 microfilm reels**;
- local shelving: `Microfilm 17,501-184P`;
- finding aid available in the Library of Congress Manuscript Reading Room;
- LCCN: `mm80058172`;
- acquisition: purchase, 1978.

This disagrees numerically with the NHPRC's `187 reels`.

The project records this as `GAC0008`, with field `extent` and status:

`open_representation_extent_discrepancy_possible_edition_vs_holding_difference`.

The distinction matters. An edition can contain 187 reels while a repository owns 184; a catalog can omit supplements; guide/index reels may be counted differently; or one description may reflect a different state of the edition. None of these possibilities can be selected without the reel lists.

Accordingly:

`187 != 184`

is a real descriptive discrepancy,

but

`187 - 184 = three missing content reels`

is **not** yet an archival conclusion.

---

## 5. Implication for GLA0056

Canonical `GLA0056` remains:

`Arthur O. Lovejoy -> Orrin L. Elliott, 15 April 1901, Elliott MSS, Stanford`.

Its physical form and current container remain unresolved.

Batch116 does not create a microfilm manifestation of this letter. To do that, one of the following must occur:

1. the 31-page guide/reel list explicitly identifies the relevant 1901 Elliott/President's Office/letterpress material and the reel can be inspected;
2. an LC or Stanford microfilm reel yields the literal Lovejoy-to-Elliott text;
3. a current Stanford physical component and a filmed image can be collated object by object.

Only then can a second manifestation be considered for `GLA0057`.

---

## 6. Data products

- `archive_index/lovejoy_jhu_rg02001_departmental_file_controls_batch116.csv` — File 56, File 115, post-1915 Philosophy target, and RG-04-120 negative control;
- `archive_index/lovejoy_stanford_jordan_microfilm_extent_audit_batch116.csv` — NHPRC/Stanford/LC representation audit;
- `archive_index/lovejoy_global_archive_description_conflicts_batch116.csv` — `GAC0008`, 187-vs-184 reel extent discrepancy;
- `archive_index/lovejoy_global_archive_repository_coverage_batch_deltas_consolidated.csv` — `COV0056-COV0058`;
- this synthesis note.

No new `GLA` or `GAL` IDs are created.

## Highest next moves

1. **JHU reference-level file identification** — recover the RG-02-001 Series 1 post-1915 `Department of Philosophy` file number and date range.
2. **Then test GLA0030 inside that file** — Lovejoy/Russell/lecture/technical philosophy/war-pacifism; record literal recipient, date, form and modern container.
3. **Obtain the 31-page Jordan microfilm guide** — Stanford/SearchWorks, OCLC holding, or LC Manuscript Reading Room finding aid.
4. **Resolve GAC0008 reel-by-reel** — determine why NHPRC says 187 and LC says 184 before treating the LC copy as complete.
5. **Use the guide to identify 1901 incoming-letter/letterpress coverage** — only then test for a microfilm manifestation of GLA0056.
6. **Keep the Elliott physical witness first-order** — establish original/copy/transcription status independently of the microfilm route.

## Evidence rules added

> **Two dated departmental files in the same presidential series can establish a filing architecture without licensing an unobserved file number.**

> **Institutional reorganization can change the filing key; pre-split file identity must not be projected into a post-split department.**

> **Published-edition extent and repository-holding extent are different descriptive levels.**

> **A reel-count discrepancy is not automatically a preservation gap.**

> **A microfilm edition becomes a Lovejoy manifestation only when the relevant item or faithful surrogate is identified, not when the parent collection is known to have been filmed.**
