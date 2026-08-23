# Archive-side Batch 111 — registry integrity repair and the Wilson descriptive/transcription provenance problem

Date: 2026-08-19  
Status: synced  
Scope: follow Batch110's JHU authority sweep by auditing the global component registry before creating more IDs, then reconstruct the descriptive genealogy linking Daniel J. Wilson to the Lovejoy papers while keeping MS-0873 separate from MS-0038 unless item-level provenance proves a relation.

## Core result

Batch111 produces **no new global archival component IDs by design**. Instead, it repairs an identifier error introduced in Batch110 and establishes a stricter provenance model for Wilson's work.

The master component index already contained three JHU presences that Batch110 mistakenly re-harvested under new IDs:

- `GLA0053` duplicates canonical `GLA0020` — History of Ideas Club records, RG-15-120;
- `GLA0054` duplicates canonical `GLA0010` — Daniel J. Wilson transcriptions of Arthur O. Lovejoy letters, MS-0873;
- `GLA0055` duplicates canonical `GLA0011` — Richard Macksey papers, exact Lovejoy file dated 1948-06-16.

The three Batch110 IDs are now formally `deprecated_duplicate_id` aliases. They remain visible in the historical Batch110 delta so the error is auditable, but they must not be counted as additional components and must never be reused for different objects. Future citations should redirect to the canonical IDs. The next unassigned global component ID therefore remains `GLA0056`.

This is encoded in `archive_index/lovejoy_global_archive_duplicate_aliases_batch111.csv`.

The broader methodological lesson is simple: **a new retrieval is not a new archival object until it has been checked against the canonical registry and prior deltas.** Richer wording, a new search route, or a different authority page does not create a second component.

---

## 1. Wilson is securely part of the descriptive history of MS-0038

The current Johns Hopkins finding aid gives an unusually explicit processing genealogy for the Arthur Oncken Lovejoy papers, MS-0038.

- **1963** — Marjorie Nicolson examined the papers at George Boas's request and arranged some material into labeled envelopes; JHU says that categorization has been retained.
- **1974-1975** — Daniel J. Wilson prepared a detailed index of the collection, listing the subject or title of each item, and also prepared a complete index to the large correspondence corpus.
- **1979** — the papers were reboxed, while the order corresponding to Wilson's index was retained.
- **1993** — a container list was created to align the material with box numbers, with the series arrangement continuing to follow Wilson's index.
- **2005** — an envelope of five French manuscripts omitted from the container list was found and reintegrated into Box 66, a useful control showing that descriptive omission and physical absence are not identical states.
- **2019** — the collection was completely re-described; the arrangement was preserved, but folder titles and scope/content information were checked against the physical holdings folder by folder. JHU identifies the resulting finding aid as its most up-to-date and complete listing.
- **August 2023** — biographical and scope notes and some folder titles were revised under JHU's conscientious-description guidelines; the previous version remains available on request.

Official control: https://aspace.library.jhu.edu/repositories/3/resources/54

This sequence matters for older scholarship. A citation made against Wilson's index, the 1979 reboxing, the 1993 container list, or the current ArchivesSpace hierarchy may employ different locator layers while still referring to the same underlying collection. Locator disagreement must therefore be treated as a version/provenance problem before it is treated as a document-identity problem.

---

## 2. MS-0873 is a separate derivative manifestation domain

JHU separately catalogs `Daniel J. Wilson transcriptions of Arthur O. Lovejoy letters`, MS-0873, in Box 1 (public authority data gives barcode `31151034446595`). The description states that the collection consists of transcriptions of Lovejoy letters dated 1872-1962, mostly typewritten with some handwritten.

Official control: https://aspace.library.jhu.edu/agents/people/66

That evidence establishes a derivative Lovejoy-letter corpus. It does **not** establish its source corpus.

The tempting equation is:

`Wilson indexed MS-0038 in 1974-75`  
`+ Wilson is associated with MS-0873 transcriptions`  
`= MS-0873 was transcribed from MS-0038`.

The first two propositions are supported; the third is not. JHU's public description does not say that MS-0873 was created from MS-0038, that every transcription has an original in MS-0038, or that every source repository is Hopkins. The two Wilson roles are historically adjacent but must remain evidentially separate until a transcription itself supplies a source note or can be matched to an independently verified original.

The correct sequence is therefore:

`transcription heading/text -> literal date and correspondents -> source/repository notation if present -> candidate original -> object-level collation`.

Only after that may a row be classified as a derivative manifestation of a specific historical letter event.

---

## 3. Wilson's 1982 bibliography corroborates manuscript use without resolving MS-0873 provenance

In the preface to *Arthur O. Lovejoy: An Annotated Bibliography* (Garland, 1982), Wilson retrospectively describes his 1974-75 work at Johns Hopkins as cataloging Lovejoy's professional correspondence together with other notes and manuscripts available there in typescript. He also explains that manuscript searching brought additional Lovejoy essays and published letters to light. The book then names a distributed group of smaller correspondence repositories, including the Ferdinand Hamburger Jr. Archives at Hopkins, the AAUP archives, Berkeley, Harvard/Houghton, Missouri, Stanford, and Washington University in St. Louis.

Method-source control: the accessible scan is a published secondary bibliography containing Wilson's first-person account of his research procedure. Book metadata independently identifies Daniel J. Wilson, *Arthur O. Lovejoy: An Annotated Bibliography*, New York: Garland Publishing, 1982.

This supports two secure conclusions:

1. Wilson's 1974-75 cataloging of the Hopkins Lovejoy manuscripts was not merely passive archival processing; it fed his later Lovejoy bibliographical research.
2. Wilson understood the Lovejoy correspondence corpus as distributed across multiple repositories.

It still does not identify MS-0873 as the product of that cataloging project. Nor does Wilson's 1982 repository list function as a modern component locator. Repository names, custody, call numbers, arrangement, and public description may have changed in the intervening decades.

Accordingly the Wilson repository list remains a **historical discovery graph / recall seed**, not a holdings table.

---

## 4. The Missouri control shows why historical leads and current components must stay separate

Earlier project work already followed Wilson's Missouri lead into current University of Missouri Archives description. The primary box list independently verifies a Lovejoy component in `C:1/131/7 (A11-54)`, Series 15 photographic prints and negatives: `FF - Lon-Ly`, `Lovejoy, Arthur, 1939`. That is canonical `GLA0019`.

But this photographic component is not the correspondence collection Wilson had in mind when listing Missouri among smaller correspondence repositories. Finding one Lovejoy object in the same repository does not discharge a different historical lead.

The Missouri case therefore supplies a clean control:

`historical secondary repository lead`  
`!= current primary component`  
`unless material class / collection / object evidence connects them`.

The same rule now governs Berkeley, Stanford, Washington University, and the Ferdinand Hamburger Jr. Archives.

---

## 5. Why the Batch110 duplication matters methodologically

The Batch110 error was not caused by weak source material. All three duplicated rows were based on legitimate JHU descriptions. The failure occurred one layer later: **entity resolution against the project's own registry**.

That means source verification and registry verification are separate operations.

Before issuing a new `GLA` identifier, the workflow must now test at least:

1. repository;
2. collection/call number;
3. series/hierarchy;
4. component title/date where exposed;
5. manifestation class;
6. existing master and batch-delta IDs.

A match on the first four normally indicates the same archival presence unless there is positive evidence for multiple physical manifestations. A newly discovered material-form distinction may justify a new manifestation row, but a richer description of the same folder or collection does not.

Deprecated IDs remain tombstones. They are never recycled, because reuse would make old commits and research notes semantically unstable.

---

## 6. Data products created in Batch111

- `archive_index/lovejoy_global_archive_duplicate_aliases_batch111.csv` — deprecates GLA0053-GLA0055 and redirects them to GLA0020, GLA0010, and GLA0011;
- `archive_index/lovejoy_wilson_transcription_provenance_batch111.csv` — nine-stage MS-0038/MS-0873/Wilson descriptive-provenance matrix;
- `archive_index/lovejoy_global_archive_repository_coverage_batch_deltas_consolidated.csv` — COV0040-COV0041, covering the JHU provenance audit and Wilson's historical multi-repository discovery list;
- this synthesis note.

No new GLA component is added in this batch.

## Highest next moves

1. **MS-0873 Box 1** — inspect every transcription and capture heading, literal date, sender, recipient, typewritten/handwritten status, source notation, editorial brackets, annotations, and any repository/call-number reference. This is now the highest-value conversion from derivative corpus to historical-letter graph.
2. **Ferdinand Hamburger Jr. Archives** — Wilson explicitly named this as a smaller correspondence repository at Johns Hopkins. Resolve its present collection identity and search for an exact Lovejoy component.
3. **Wilson 1982 bibliography source-note sweep** — identify exact entries whose annotations cite Stanford, Berkeley, Missouri, Washington University, AAUP, Harvard, or Hamburger archival material. Exact secondary archival citations can then be tested against current repository description.
4. **RG-15-120** — recover the exact History of Ideas Club folders, but use canonical `GLA0020`; do not create a new component simply because the file-level locator improves.
5. **Macksey 1948-06-16** — resolve the existing canonical `GLA0011` physical container/direction/form rather than creating another row.

## Evidence rules added

> **A re-harvest is not a new archival component until canonical-registry entity resolution has been completed.**

> **Deprecated duplicate IDs are permanent tombstones and must not be reused.**

> **Shared processor/editor identity does not establish source-corpus identity.**

> **A published historical repository list is a discovery graph, not a current locator.**

> **Descriptive omission, physical absence, and archival loss are different evidence states.**
