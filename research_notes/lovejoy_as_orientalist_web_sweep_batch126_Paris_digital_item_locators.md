# Batch 126 — Paris digital item locators: exact 6 Nov 1898 Collège de France minute locus and direct-source closure queue

Date: 2026-08-19  
Status: synced  
Scope: follow Batch125 by pushing from collection-level digitization claims down to exact item/page locators wherever the public web layer exposes them.

## Core result

The Collège de France side has now moved one level lower than a generic statement that faculty minutes are digitized. Salamandre's indexed archive tree exposes the exact annual faculty-assembly unit for the opening of the relevant academic year:

- **6 November 1898**
- fonds/series: `Assemblée des Professeurs. Registres et pièces annexes`
- volume: `2 AP 10`
- manuscript pages: **113–116**
- digital component identifier exposed in the item link: `FR075CDF_000AP0002_de-702`

The immediately adjacent annual controls are likewise exposed:

- 7 November 1897 — `2 AP 10`, pp.86–93;
- 5 November 1899 — `2 AP 10`, pp.126–134.

This is a much better target than an open-ended Collège de France archival search. The 6 Nov 1898 four-page unit can be inspected specifically for Sylvain Lévi's return from mission, resumption of the Sanskrit chair, substitute arrangements, and any teaching/leave decision. Current machine retrieval can resolve the item metadata but the image page itself returns a cache miss, so **content has not yet been read** and no Lévi claim is made from this minute.

Official indexed result:
https://salamandre.college-de-france.fr/pleade/docsearch-term.xsp?base=ead&f=lfprofesseur&r=FR075CDF_000AP0002&v=Hadamard%2C+Jacques+%281865-1963%29

Attempted component URL:
https://salamandre.college-de-france.fr/pleade/ead.html?c=FR075CDF_000AP0002_de-702&id=FR075CDF_000AP0002

---

## 1. Why 6 November 1898 matters

AGORHA independently dates Sylvain Lévi's first Asian scientific mission from **3 October 1897 to September 1898**. Lovejoy's Paris correspondence claims begin in October 1898, and Wilson says the Pāli-Buddhism course Lovejoy wanted from Lévi was not being offered. The first faculty assembly exposed after Lévi's mission window is therefore the 6 November 1898 meeting.

The evidentiary question is narrowly framed:

> Does the 6 Nov 1898 faculty minute record Lévi's return, course resumption, leave status, substitute, or any administrative condition that constrains what he was officially teaching when Lovejoy arrived?

A positive entry could explain the institutional transition. A silent four-page minute would be only a bounded negative for that meeting, not evidence that no relevant administrative action occurred elsewhere.

---

## 2. The course-poster collection remains digitized but item-level Lévi retrieval is unresolved

Salamandre's official digital-collections page confirms the digitization of:

`Affiches et programmes de cours du Collège de France, 1688–1900`

The EAD root is:

`FR075CDF_00AFF0004`

Search-engine indexing resolves the collection but has not yet surfaced an 1898–99 child item under `Sylvain Lévi`, `langue et littérature sanscrites`, or obvious spelling variants. This is a portal-indexing ceiling, not evidence that the 1898 course poster is absent.

The correct next action is now technical: traverse the EAD hierarchy around the 1898 date nodes or use the portal's own faceted search manually/API-like if an endpoint can be inferred, rather than repeating generic web queries.

---

## 3. Marillier p.247 can already be controlled against a later facsimile-backed verbatim witness, but primary RHR collation remains the standard

Batch72's p.247 proposition has a strong later verbatim control. The 1909 `Dictionnaire apologétique de la foi catholique` reproduces a long passage and explicitly attributes it to:

`L. Marillier, La place du Totémisme dans l'Evolution Religieuse, Revue des Religions, tome XXXVI, 1897, p.247`.

The quoted logic is exactly the one reconstructed in Batch72: a totemic cult cannot simply be made into a tribal/national cult while retaining its specific totemic character; once an animal totem becomes a deity of a wider group it has ceased, in the relevant sense, to function as a totem; animal and plant gods can have multiple origins/functions; a surviving index may sometimes support a bounded former-totem claim without proving that totemic status was a necessary route to divinity.

This later witness is useful for text targeting, but it does not replace the direct RHR image. JSTOR already exposes the primary 1897 Marillier installment as `stable/23661047`, pp.208–253, with downloadable/XML access, so publication-grade closure remains a direct p.247 check there or in the Google Books/BSB volume.

---

## 4. Marillier RHR 37 pp.230–231: the contemporary Hubert–Mauss pointer is exact

The 1909 facsimile-backed reprint of Hubert and Mauss's sacrifice essay gives the exact proposition and reference:

`Mais il n'est pas logiquement nécessaire que des animaux sacrés aient eu toujours ce caractère (voir Marillier, Rev. de l'Hist. des Relig., 1898, I, pp.230-231...)`

This is valuable because it fixes what to look for in the primary Marillier pages: the target is not a vague anti-totemist paragraph but the argument against making prior totemic status logically necessary for sacred animals.

Again, this is a contemporary attribution/control rather than the primary-page transcription. RHR 37 is directly digitized, so the next step is literal primary collation.

---

## 5. Revised high-value online queue after item-level resolution

1. **Open/capture `FR075CDF_000AP0002_de-702`** — 6 Nov 1898 faculty minute, 2 AP 10 pp.113–116.
2. Compare 7 Nov 1897 pp.86–93 and 5 Nov 1899 pp.126–134 for leave/return wording if the 1898 minute assumes earlier decisions.
3. Traverse `FR075CDF_00AFF0004` to the 1898 course-poster child and capture the Sanskrit chair's exact advertised course.
4. Directly collate Marillier RHR 36 p.247 and p.250 from `23661047` / alternate digitized volume.
5. Directly collate Marillier RHR 37 pp.230–231 and replace the Hubert–Mauss pointer with Marillier's own wording/context.
6. Continue EPHE `FRAN_IR_061975` at component level for image-bearing 1898–99 Vᵉ Section scolarité/attendance nodes.

## Evidence discipline

- Exact digital **locator** is not exact digital **content**. The 6 Nov 1898 meeting is now physically/page-located online, but its content remains unread in this runtime.
- A later verbatim quotation with exact original pagination is a useful control, not a substitute for the primary image when that image is already available.
- Hubert–Mauss's explicit citation to Marillier pp.230–231 establishes a contemporary interpretation and a retrieval target; it does not license attributing Hubert–Mauss's wording verbatim to Marillier.

No new GLA/GAL/COV identifier is created.
