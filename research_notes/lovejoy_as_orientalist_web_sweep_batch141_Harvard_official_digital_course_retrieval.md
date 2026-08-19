# Batch 141 — Harvard 1892–97 official course/enrollment records are already digitized: a finite route to Babbitt–Lanman and Lovejoy's exact training

Date: 2026-08-19  
Status: synced  
Scope: convert the remaining Harvard-side uncertainties from generic archive targets into exact official digital series and years.

## Core result

Harvard's own digital library exposes two continuous official series that cover every year needed to test the Babbitt–Lanman and Lovejoy training chains without an archive visit:

1. **Faculty of Arts and Sciences, Courses of Instruction, 1879–2009** — official ListView root includes child objects for 1892–93, 1895–96, 1896–97 and 1897–98.
2. **Annual Reports of the President and Treasurer of Harvard College, 1877–1903** — official ListView root includes the same relevant years and normally reports course enrollment counts by rank.

A third parallel digital series exists for **Radcliffe Courses of Instruction**, including 1896–97. Because Radcliffe often mirrored Harvard instructors/courses, it can serve as a control if the Harvard child viewer is difficult.

This means two important unresolved claims are now finite digital retrieval problems:

- identify the exact 1892–93 Lanman course that Babbitt and More reportedly constituted by themselves, and test the `class of two` claim against official enrollment data;
- recover the exact 1896–97 descriptions of the Lovejoy courses Wilson identifies through Harvard records and Lovejoy letters — Lanman Sanskrit/Buddhist texts, Everett comparative religion, Toy Hebrew religion — and add enrollment scale/level.

The present automation can index the series roots but is rate-limited when opening individual ListView child objects. A manual click can therefore save substantial time; this is a viewer-access problem, not missing digitization.

---

## 1. Official FAS Courses of Instruction series

Harvard ListView:
https://listview.lib.harvard.edu/lists/drs-467484628

Persistent archival root:
`HUL.ARCH:40128815`

The indexed series explicitly lists annual children including:

- 1892–1893;
- 1895–1896;
- 1896–1897;
- 1897–1898.

The historical title for the relevant period is `Announcement of courses of instruction provided by the Faculty of Arts and Sciences for the academic year`.

This is the cleanest source for exact course number/title, instructor, timetable and level.

### 1892–93 target

Batch140 strengthened the Babbitt–Lanman edge through Dakin's statement that Babbitt and Paul Elmer More together formed the entirety of one Lanman class in autumn 1892. The official 1892–93 announcement should tell us which Indo-Iranian/Sanskrit courses Lanman actually offered.

The ideal closure is:

`course description + enrollment total 2`

which would identify the class independently.

### 1896–97 target

Wilson's Lovejoy reconstruction cites a Harvard Archives course list and Harvard Catalogue 1896–97 pp.73, 75, 99 alongside Lovejoy's October/November 1896 letters. We already know from Wilson what Lovejoy took; the official announcement can replace paraphrase with exact institutional wording.

Search/capture:

- Indo-Iranian / Sanskrit / Lanman;
- Semitic / Hebrew religion / Toy;
- Everett / comparative religion / psychological basis of religious faith;
- any graduate-level prerequisites or research/seminar wording.

---

## 2. Official Annual Reports series can add the missing enrollment scale

Harvard ListView:
https://listview.lib.harvard.edu/lists/drs-2574409

Persistent archival root:
`HUL.ARCH:15002`

The series runs 1877–1903 and explicitly exposes 1892–93 and 1896–97.

Contemporary Harvard report citations elsewhere show the annual reports list courses with enrollment broken down by status — graduate, senior, junior, etc. This makes them especially valuable for distinguishing:

`a large public/undergraduate lecture`

from

`a tiny advanced graduate textual course`.

For Babbitt/More, an enrollment total of two attached to a Lanman course would directly corroborate Dakin's biographical statement.

For Lovejoy, enrollment scale could materially sharpen how to describe his Sanskrit/Buddhist or religion courses: a small advanced seminar is historiographically different from merely taking a broad survey.

---

## 3. Radcliffe provides a parallel witness

Harvard/Radcliffe ListView:
https://listview.lib.harvard.edu/lists/drs-34299933

The series contains a 1896–97 child.

A contemporary Crimson report already shows why this parallel matters. In June 1895 it says that in Indo-Iranian languages Lanman would take charge of the Sanskrit courses that had been conducted the previous year by More.

Primary text:
https://www.thecrimson.com/article/1895/6/8/radcliffe-elective-pamphlet-the-radcliffe-college/

Thus Radcliffe course pamphlets can independently verify instructor succession and sometimes preserve descriptions very close to Harvard's own courses. They remain a control, not a substitute for Lovejoy's Harvard enrollment.

---

## 4. The Babbitt–Lanman chain is now testable against an exact numerical prediction

The important methodological change is that Batch140's biography-derived statement gives a falsifiable documentary prediction:

> If Babbitt and More really formed the whole of one Lanman class in autumn 1892, an appropriate Lanman/Indo-Iranian course in the 1892–93 President's Report may have an enrollment of exactly two, likely graduate students.

Possible outcomes:

- **one Lanman course, total 2** → very strong independent identification;
- several Lanman courses with total 2 → need course content/More or Babbitt records to choose;
- no total-2 course → Dakin may refer to a half-year, informal advanced exercise, or a course whose enrollment reporting aggregates differently;
- no detailed Indo-Iranian enrollment → biographical statement remains strong but not numerically testable from that report.

Do not treat a failed numerical match as disproving the biography until the reporting conventions are understood.

---

## 5. The Lovejoy side can likewise move from biography to exact institutional language

Current secure evidence, mediated through Wilson's consultation of Harvard records, says Lovejoy studied:

- Sanskrit and sacred Buddhist texts with Lanman;
- comparative religion and psychological religion with Everett;
- Hebrew religion with Toy.

The 1896–97 official digital sources should let us answer four sharper questions:

1. What were the exact course titles?
2. Were they formally graduate courses, mixed graduate/undergraduate courses, or Divinity/FAS cross-listed offerings?
3. What texts/topics did the catalogue itself specify?
4. How many students were enrolled?

This will matter for the Paris argument because it determines the actual degree of preparation Lovejoy brought into an EPHE system that Finot/Foucher described as stratified between beginners and prepared/veteran students.

---

## 6. Manual retrieval is now narrowly specified

If the Harvard ListView child objects open in a browser, no full-volume download is needed at first.

### Highest-return manual action

Open:
https://listview.lib.harvard.edu/lists/drs-467484628

Choose **1896–1897**.

Then send screenshots/downloads of the pages containing:

- `Indo-Iranian` / `Sanskrit` / `Lanman`;
- `Toy` / Hebrew religion;
- `Everett` / comparative religion.

If page numbers corresponding to Wilson's **73, 75, 99** are visible in the related Harvard Catalogue object, those three pages are especially valuable.

### Second action

Open:
https://listview.lib.harvard.edu/lists/drs-2574409

Choose **1892–1893** and search for `Lanman`, `Sanskrit`, `Indo-Iranian`; capture the enrollment table around each hit.

The user need not transcribe anything; full-page screenshots with page/frame numbers are enough.

---

## Evidence discipline

- A digitized official series is not the same as having read the relevant child pages.
- Radcliffe parallels do not prove Lovejoy enrollment.
- Wilson's Harvard-course reconstruction remains the direct evidence for what Lovejoy took until the underlying course list/letters are recovered.
- The Babbitt/More `class of two` is a biography-derived proposition awaiting official numerical control.
- Failure to find a course in one announcement must account for half-courses, omitted courses, research arrangements and cross-registration.

## Data product

- `research_notes/harvard_1892_1897_official_digital_course_retrieval_batch141.csv`

No new GLA/GAL/COV identifier is created in this batch.
