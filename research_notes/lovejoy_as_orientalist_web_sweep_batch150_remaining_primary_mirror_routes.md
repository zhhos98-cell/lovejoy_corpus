# Lovejoy as Orientalist / comparative religion — Batch 150

Date: 2026-08-19  
Status: synced  
Scope: continue the full remaining-primary sweep after Batch 149, but keep **object discovery / route resolution** separate from **primary-text recovery**. This pass tests whether the still-live 004/005 manual targets can be converted from institution-specific viewer bottlenecks into redundant, deterministic digital routes.

## Core result

The remaining queue is now narrower than the living notes implied. No new substantive primary text has been recovered in this pass, so none of the still-live Marillier / Thomas / Jacobi targets is marked resolved. What has changed is access topology.

Three previously fragile viewer problems now have redundant object-level routes:

1. **RHR 34 (1896), Marillier on Steinmetz, pp.113–115** — official BSB/MDZ object remains `bsb11809713`; Google Books independently confirms the bibliographic boundary `Steinmetz / Marillier` p.113 → Diekamp p.116; an Open Library edition exposes Internet Archive mirror identifier **`revuedelhistoir32alphgoog`** (OL edition **`OL20537121M`**).
2. **RHR 25 (1892), Marillier on Frazer pp.71–99 + Codrington pp.231–232** — official BSB/MDZ object remains `bsb11615030`; an Open Library edition exposes Internet Archive mirror identifier **`revuedelhistoir27alphgoog`** (OL edition **`OL20486552M`**). Thus both live 1892 targets have a second complete-volume route.
3. **Göttingische Gelehrte Anzeigen 1897, Jacobi review of Dahlmann, pp.267–273** — the official Göttingen Academy repository already exposes the complete 159th year and a first-volume PDF; the GDZ serial tree independently identifies the 1897 first half as **159,1**, with child identifier **`PPN385030444_159_1`**. The problem is therefore page extraction, not year/volume discovery.

RHR 38 (1898), the N. W. Thomas student-product target, also has stronger redundancy: the official BSB/DDB object `bsb11864666` remains authoritative, while Google Books/Play, HathiTrust preservation records, and other full-volume mirrors independently confirm the same volume. The Thomas article itself remains unread in this environment.

The practical change is important: **the project should no longer describe these items as bibliographically missing. They are exact-object, exact-page extraction tasks.** The only claim that still requires restraint is substantive interpretation: a known object or mirror is not evidence for what a page says.

No new GLA/GAL/COV identifier is created in this batch.

---

## 1. RHR 34 (1896): Marillier–Steinmetz is now multiply routed, still unread

Live target:

Léon Marillier, review of Rudolf Steinmetz, _Endokannibalismus_, _Revue de l'histoire des religions_ 34 (1896), printed **pp.113–115**.

### Boundary control

Google Books exposes the relevant contents sequence in a full-volume witness:

- `R Steinmetz Endokannibalismus M L Marillier` — p.113;
- Diekamp, `Une fausse lettre de saint Basile contre Eunomius` — p.116;
- Bérenger-Féraud, `Superstitions et survivances` — p.119.

This independently confirms Batch 148's correction that the Marillier review ends on p.115. Any older `113–118` note remains superseded.

### Route stack

**Official BSB/MDZ**

- object: `bsb11809713`;
- URN: `urn:nbn:de:bvb:12-bsb11809713-2`;
- IIIF pattern: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11809713/manifest`;
- OCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11809713/{page_num}`.

**Google Books**

- complete RHR 34 witness; contents and common-term index are exposed;
- useful as boundary/bibliographic control, not yet as page-text recovery in the present runtime.

**Open Library / Internet Archive mirror newly pinned**

- Open Library edition: `OL20537121M`;
- Internet Archive identifier exposed by the Open Library read/borrow route: `revuedelhistoir32alphgoog`.

### Status

**EXACT_OBJECT_AND_MIRRORS_RESOLVED / PRIMARY_TEXT_PENDING.**

The three pages still have to be read before answering Batch 149's decisive question: where does Marillier place Steinmetz's origin hierarchy, transfer-of-vital-force explanation, and ritual refunctionalization?

Do not infer the answer from Marillier 1897–98, Mauss, or Steinmetz himself.

---

## 2. RHR 25 (1892): one second mirror covers both Marillier targets

Live targets:

- Marillier, `M. Frazer et la Diane de Nemi`, pp.71–99 — locate and control the early Melanesian `mana` occurrence;
- Marillier review of Codrington, _The Melanesians_, pp.231–232 — determine what he selected at first reception.

### Official route retained

- BSB/MDZ object: `bsb11615030`;
- URN: `urn:nbn:de:bvb:12-bsb11615030-8`.

### New redundant mirror

Open Library exposes an 1892 RHR edition with:

- Open Library edition: `OL20486552M`;
- Internet Archive identifier: `revuedelhistoir27alphgoog`.

This makes the two live 1892 problems a single-volume extraction task across two page ranges rather than two independent discovery problems.

### Secondary locator retained but not upgraded

Nicolas Meylan's later history remains useful for the claim that Marillier mentions Melanesian `mana` in his 1892 Frazer review and for bibliographic localization. It does **not** substitute for reading the original page. The present sweep did not expose the exact primary phrase or page number.

### Status

**EXACT_OBJECT_AND_SECOND_MIRROR_RESOLVED / PRIMARY_PASSAGES_PENDING.**

Do not claim that Marillier foregrounded `mana`, spirit residence, taboo or efficacy in the Codrington notice until pp.231–232 are read.

---

## 3. RHR 38 (1898): Thomas remains a content target, not an access mystery

Target:

Northcote Whitridge Thomas, `La survivance du culte totémique des animaux et les rites agraires dans le Pays de Galles`, _RHR_ 38 (1898), pp.295–347.

### Official control

- BSB/MDZ: `bsb11864666`;
- URN: `urn:nbn:de:bvb:12-bsb11864666-6`.

Independent bibliographic searches repeatedly confirm the exact article title/range. Full-volume RHR 38 routes also exist through Google Books/Play and long-run preservation/mirror services.

### Research question unchanged

This remains valuable as a **same-teacher student-product control** at the threshold of Lovejoy's Paris year. The discriminating vocabulary remains:

`survivance`, `origine`, `forme`, `sens`, `analogie`, `ressemblance`, `rite`, `totémisme`, `culte`, `emprunt`, `agraire`.

### Status

**EXACT_DIGITAL_OBJECT_RESOLVED / ARTICLE_TEXT_PENDING.**

Do not infer Lovejoy access to Thomas, and do not infer Thomas's analytical operator from his later 1905/1911 writings.

---

## 4. Jacobi's 1897 Dahlmann review: exact GDZ child object now pinned

Target:

Hermann Jacobi, review of Joseph Dahlmann, _Nirvāṇa: Eine Studie zur Vorgeschichte des Buddhismus_, _Göttingische Gelehrte Anzeigen_ 1897, especially printed pp.268 and 272; retrieve pp.267–273.

### Official Academy repository

The Göttingen Academy repository confirms:

- year: 1897;
- 159th Jahrgang;
- total extent: 1064 pages;
- separate first-volume and second-volume PDFs;
- DOI: `10.26015/adwdocs-374`.

The first-volume PDF is therefore the correct container for pp.267–273.

### Independent GDZ serial-tree route

The GDZ master record for _Göttingische gelehrte Anzeigen_ exposes an 1897 child labelled **159,1**. The child URL resolves to identifier:

`PPN385030444_159_1`

This is a cleaner deterministic object key than relying only on the 70MB repository PDF filename.

### Status

**YEAR / HALF-VOLUME / CHILD OBJECT RESOLVED / REVIEW TEXT PENDING.**

This should no longer be described as a genuine source-discovery bottleneck. It is an exact-page extraction problem.

The substantive questions remain unchanged:

- what does Jacobi accept/reject in Dahlmann's genealogy in 1897?
- does he privilege lexical genealogy, conceptual resemblance, usage, or systematic reconstruction?
- how exactly do his pp.268/272 claims feed the 1898 nidāna article?

No claim about Lovejoy reading Jacobi 1897 follows from recovery of this route.

---

## 5. What the unsuccessful binary fetches mean

In this runtime, catalogue/metadata pages are often fetchable while constructed IIIF, PDF, borrow, or OCR endpoints fail because of cache/safe-fetch/DNS restrictions. That is an **environmental access condition**, not evidence that the underlying digital object is unavailable.

Accordingly, statuses are separated into:

- `DISCOVERY_PENDING` — no exact digital object known;
- `OBJECT_RESOLVED_TEXT_PENDING` — exact digital object and page range known, content not yet read;
- `PRIMARY_TEXT_RECOVERED` — substantive primary text actually inspected;
- `FACSIMILE_CONTROL_PENDING` — text/OCR recovered, but image verification still desirable for quotation.

After this pass, Marillier RHR34, Thomas RHR38, Marillier RHR25, and Jacobi GGA 1897 all belong in the **OBJECT_RESOLVED_TEXT_PENDING** class, not `DISCOVERY_PENDING`.

---

## 6. Revised next extraction order after Batch 149 + Batch 150

### P0 — Marillier on Steinmetz, RHR34 pp.113–115

Still first because Batch 149 has made it a genuinely discriminating three-page intervention in the `origin hierarchy → relational/ritual reclassification → mechanism decomposition` problem.

### P0b — Jacobi 1897, GGA pp.267–273

The strongest remaining 004 controversy control. Exact official container and GDZ child are now fixed.

### P1 — N. W. Thomas, RHR38 pp.295–347

Same-teacher student product; potentially shows what Marillier-directed research looked like in published practice immediately before Lovejoy's documented Paris participation.

### P1 — RHR25 two-locus extraction

Read the Frazer review's secure `mana` occurrence and the Codrington review together from the same complete volume. This is more efficient than treating them as separate retrieval projects.

### P2 — Marillier, `Religion`, Grande Encyclopédie XXVIII

Still useful for conceptual wording and chronology, but no longer the best proof that Marillier possessed a `mana`/magical-force vocabulary before Lovejoy; later 1897–98 primary evidence already establishes that.

---

## 7. Research consequence

Batch 149 clarified the substantive axis: not `monism → pluralism`, but a shift in which explanatory level governs classification. Batch 150 clarifies the archival axis: the most important missing middle sources are no longer vague bibliographic desiderata. They are **three-page, seven-page, and bounded-article extraction jobs attached to exact digital objects and redundant mirrors**.

That matters methodologically because the next step can be proposition-level collation rather than another broad web sweep.

The strongest immediate chain remains:

`Steinmetz 1896 primary`  
→ `Marillier review 1896 pp.113–115 [exact object known; text pending]`  
→ `Mauss contemporary reclassification`  
→ `Marillier 1897–98 anti-unilateral / mechanism-sensitive print`  
→ `Lovejoy documented 1898–99 EPHE participation + 005`  
→ `1906 Primitive Energetics`.

The unresolved Marillier review can strengthen, complicate, or break a simple middle-stage narrative. That is exactly why it must remain unread rather than reconstructed from its neighbors.

## Data product

- `research_notes/remaining_primary_mirror_route_resolution_batch150.csv`

## Controls

- Batch 145–148: object/pagination/access corrections.
- Batch 149: Steinmetz–Mauss–Lovejoy explanatory-level shift.
- Living 004 and 005 retrieval queues are updated separately in Batch 150.