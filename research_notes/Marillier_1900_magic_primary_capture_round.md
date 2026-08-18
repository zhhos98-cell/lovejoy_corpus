# Marillier 1900 `Religion`: primary-capture round and immediate controls

## Result of this retrieval round

The 1900 `Religion` article is now bibliographically and digitally localized tightly enough for automated capture, but the primary page text has not yet been downloaded into this repository.

### Publication window

*La Grande Encyclopédie*, vol. XXVIII was issued between **3 May and 29 October 1900**. Marillier's `Religion` occupies printed pp. 341–364. This narrows the article to the same calendar year in which Lovejoy later said his own conclusions were reached, but it does not establish chronological priority within 1900.

### Public-domain digital witnesses

- Gallica ark `bpt6k24663w` (IIIF-capable).
- Wikisource / Wikimedia `Grande Encyclopédie XXVIII.djvu`; the source scan explicitly identifies Internet Archive item `lagrandeencyclop28dref`.
- Working offset places the article around scans 353–376; this remains a locator only until verified against printed pagination.

### Machine-access routes

Internet Archive documents an experimental book API supporting:

- `/books/{itemid}/searchinside?q={query}`
- `/books/{itemid}/pages/{page}/ocr`
- page-image and manifest endpoints.

Gallica documents IIIF Presentation and Image APIs for its digitized books.

The current execution environment still blocks the final direct fetch for these specific generated URLs, so no primary image/OCR is claimed as captured locally yet.

---

## Strong near-contemporary control: Britannica 1911

The 1911 *Encyclopædia Britannica* article `Magic` explicitly attributes a three-class theory to **L. Marillier**:

1. word/act magic, including mimetic rites, rain-making, disease-making and sympathetic magic; some rites act directly upon nature, others through a coerced god/spirit;
2. efficacy conditioned by the ritual state of the performer, such as ceremonial purity or initiation;
3. special persons invested with magical power (`mana`), whose words or presence can affect weather and fertility, sometimes with the power attached to person/office or explained by indwelling deity.

The same Britannica bibliography explicitly directs readers to the article `Religion` in *La Grande Encyclopédie*. This makes Britannica a useful near-contemporary relay, not a substitute for Marillier's own text.

### Notebook 005 mapping

- 005 p.64: magical sacrifice can operate directly on forces of nature; rain-making example; machine-like language.
- 005 pp.82 and 112–117: initiation, purity, bodily qualification, incorporation rather than sacrifice.
- 005 pp.85–90: intrinsic efficacy versus indwelling spirit.
- 005 pp.99–105: transfer of fecundating power to crops; p.105 quasi-mechanical/magical rather than sacramental.
- 005 p.119: transferable qualities through selected body parts.

This correspondence is now strong enough to make direct collation of Marillier 1900 pp.349–351 a top-priority textual task.

---

## Primary institutional control: Mauss 1901–1902

Marcel Mauss's official EPHE report for 1901–1902 describes his Tuesday conference as a critical study of documents on **magic among the Melanesians** and states that he attempted to maintain the traditions implanted in this field by his teacher Marillier.

This establishes independently that Melanesian magic was understood immediately after Marillier's death as a Marillier seminar tradition, not merely a later historiographical association.

---

## Söderblom 1901: second student witness

Internet Archive item `laviefuturedapr00sdgoog` is confirmed as a 468-page public-domain University of Michigan / Google scan of Söderblom's 1901 *La vie future d'après le mazdéisme*; full-text, PDF, ABBYY and image-download options are exposed by the item page.

Later source-critical scholarship points to p.37, where Söderblom explicitly uses generalized `mana` language attributed to Marillier. Direct p.37 capture remains outstanding, so the exact primary wording is not yet promoted to repository evidence.

---

## New bibliographic target resolved one step further

Marillier's posthumous(?) 1901 **`Notes sur la coutume, le tabou et l'obligation morale`**, Paris: Félix Alcan, now has an exact Sudoc identifier:

`086800310`

No full digital text was located in this sweep. The title is unusually relevant to 005 pp.14–20, where Lovejoy separates custom/taboo/ritual determination from genuinely moral desert. Before treating that notebook taxonomy as a Lovejoy extension, this text must be checked.

---

## Current evidential hierarchy

**Primary and directly online:** Lovejoy 005; EPHE 1898–99 Marillier report; Mauss 1901–02 EPHE report; Söderblom IA item metadata; Wikisource/IA provenance for *Grande Encyclopédie* XXVIII.

**Near-contemporary relay:** Britannica 1911 three-class Marillier magic scheme, with explicit bibliographic pointer to `Religion`.

**Secondary locator requiring primary capture:** exact six `mana` occurrences in Marillier 1900 and Söderblom 1901 p.37.

## Next technical actions

1. Resolve printed pp.349–351 to exact DjVu/IIIF canvases and capture the page images/OCR.
2. Run IA `searchinside` for `mana` and `Marillier` in both `lagrandeencyclop28dref` and `laviefuturedapr00sdgoog` when endpoint access succeeds.
3. Resolve Sudoc `086800310` holdings and determine whether `Notes sur la coutume...` is a monograph/offprint or article reprint.
4. Continue the Archives nationales EAD route to isolate the 1898–99 Vᵉ Section registration/attendance unit within `20190568/185-368`.
