# Lovejoy corpus — CURRENT STATE

Last synchronized: 2026-08-29  
Status: **BASE JHI EVIDENCE FROZEN / CLEAN-SUBMISSION v3.3 ACTIVE / 1,878-WORD BODY / 4 TRUE ENDNOTES / WORD PACKAGE GENERATED + RENDER-QA PASSED / IMAGE FALLBACK CLOSED / NO BLOG BLOCKER**

This is the single living project-state file. For evidence routing use `research_notes/CANONICAL_INDEX_2026-08-28.md`; for final evidence ceilings use `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`. Historical `ACTIVE`, `HOLD`, `pending`, `next action`, `blocker`, or `missing` language elsewhere does not override this file.

## 1. Active JHI Blog layer

Current clean-submission source:

- `research_notes/JHI_blog_full_draft_v3_3_clean_submission_2026-08-29.md`
- body: **1,878 words**;
- argument / paragraph architecture frozen;
- published sources hyperlinked on first substantive mention with parenthetical page references where useful;
- endnotes reduced to **four publication-useful notes**: (1) 1948 bibliography/version + Monboddo chronology; (2) notebook 004 archival citation; (3) Harvard catalogue + enrollment firewall; (4) notebook 005 composite/Paris provenance;
- copyedit pass 1 completed; the published 1898 article title preserves its historical `Upadana / Upadisesa` spelling while technical terms in prose use normalized diacritics;
- Harvard wording tightened from an over-specific `study with these figures` formulation to the evidence-controlled `within this training environment`.

Supporting controls:

- `research_notes/JHI_blog_v3_2_citation_hygiene_2026-08-29.md`
- `research_notes/JHI_blog_image_caption_permission_plan_2026-08-29.md`

Word production layer:

- a submission DOCX named `JHI_Blog_Lovejoy_Buddhism_v3_3_submission_draft.docx` has been generated as the current conversation artifact;
- Word package contains **true OOXML endnotes**, working hyperlinks, preserved italics/diacritics, title + author/affiliation placeholders, an author-bio placeholder, and a Figure 1 placeholder/caption at the manuscript-p.123 discussion;
- endnote separator OOXML was explicitly repaired so separator objects are not mis-rendered as empty endnotes;
- final DOCX was rendered to **5 pages** and every page visually inspected; no clipping, missing glyphs, broken hyperlinks-as-text, note loss, or layout overlap was found.

Only unresolved production inputs are user/editor supplied rather than research problems:

1. preferred publication name;
2. exact affiliation / short author bio;
3. final image choice once JHU permission timing is known.

No new research is needed unless copyediting exposes a genuine source contradiction.

## 2. Image status: no blocker

First choice:

- notebook 004, source PDF p. 42 / manuscript p. 123;
- Arthur O. Lovejoy notebook labelled `Sankhya + Buddhism`, digitized source ID `MS38_004_001_061_004`;
- *Arthur Oncken Lovejoy papers*, MS-0038, Special Collections, The Johns Hopkins University.

Use JHU's current publication/rights route for the image. Do not assume the research scan itself carries publication permission.

Fallback:

- opening page (printed p. 126) of Lovejoy's 1898 JAOS article;
- JSTOR's Open JSTOR record for vol. 19 explicitly states that, to JSTOR's knowledge, the 1898 issue is public domain;
- Google Books/Play supplies a free scan of vol. 19, part 2.

Decision rule: use notebook p. 123 if permission / publication-quality image arrives on a workable schedule; otherwise use the 1898 JAOS page without delaying text submission.

## 3. Archival and citation ceilings

Notebooks remain the evidentiary center:

- 004 corrected: **71/71 pages**;
- 005 corrected: **120/120 pages**;
- total material-form review: **191/191 pages**;
- authoritative corrected text: `archive_transcriptions/*_clean.json`;
- material ledger: `archive_transcriptions/MS38_004_005_material_audit_manifest_2026-08-27.json`;
- closure: `research_notes/MS38_004_005_material_form_closure_2026-08-27.md`.

Highest-value visual control remains 004 PDF p. 42 / manuscript p. 123: `viññāṇa` is spatially nested inside the `nāma` / `nāmarūpa` classification while adjacent prose treats it as temporally antecedent to `nāmarūpa` and logically a subdivision. The page visibly preserves distinct relations.

JHU citation ceiling:

- collection identity is securely *Arthur Oncken Lovejoy papers*, MS-0038, Special Collections, The Johns Hopkins University;
- the public finding aid does not presently expose an independently verified Box/Folder mapping for the digitized notebooks;
- cite notebook title/source ID + collection + manuscript/PDF locus;
- **do not infer Box 61 from the `061` component of the digitization ID.**

Other locked citations:

- original 1948 *Essays* bibliography: 1898–1948, pp. 339–44; later expanded form runs through 1951 but retains the Buddhist article first;
- Wilson, *Annotated Bibliography*, p. 12, entry 17: 1895 `James Burnett, Lord Monboddo`;
- Schaffer 2010, p. 484: Lovejoy studied Pāli and Sanskrit in Paris;
- 1902 `Religion and the Time-Process`: Aristotle/Vedānta locus pp. 446–47;
- 1906 `Democracy in the Twentieth Century`: `longitudinally and cross-wise` p. 94; political applications pp. 101–2; Black franchise passage p. 102;
- *Great Chain*: preface + pp. 30, 35, 97.

## 4. Publication-facing thesis and architecture

Governing thesis:

> **This essay does not add a forgotten Buddhist episode to Lovejoy's biography; it changes the status of a known one. His notebooks show Buddhist materials as a site where the young Lovejoy repeatedly tested what textual and historical evidence could establish about identity, sequence, causation, borrowing, and arrangement; reading those notes beside the 1898 article and later writings shows what entered print, what was narrowed or left behind, and why later histories of Lovejoy made other parts of his career more central.**

Shortest working question:

> **The question is not whether Lovejoy studied Buddhism, but what kind of historical work he did when he did so.**

Five movements remain fixed:

1. retrospective bibliography → archive;
2. notebook 004 → Warren/Senart → 1898 publication;
3. notebook 005 → Paris → 1902;
4. notebook questions → 1906 political/scalar enlargement;
5. *Great Chain* → differentiated historiographical memory.

Do not reintroduce the relation inventory table. Do not make Skinner the opening architecture. Do not turn the mature book into a teleological endpoint. Do not claim Buddhism caused the unit-idea method.

## 5. Frozen calibration / governance

Logic and Carnap branches remain refrozen as background calibration. The operative anti-leakage rule remains:

> **A ≠ B does not establish that A is historically or functionally independent of B.**

Repository navigation authority:

1. `CURRENT_STATE.md`
2. `research_notes/CANONICAL_INDEX_2026-08-28.md`
3. `research_notes/JHI_FINAL_EVIDENCE_GATE_2026-08-27.md`
4. source-specific terminal dossiers
5. raw/transcription/provenance layers

Reopen a frozen research line only if a newly digitized/direct primary changes a live proposition, a direct source contradicts current evidence, publication editing requires exact facsimile/page/quotation verification, or a category already used in the draft requires materially different actor-level reconstruction. Otherwise continue production rather than research.

## Restart shorthand

> **Active text is `JHI_blog_full_draft_v3_3_clean_submission_2026-08-29.md`: 1,878-word body, four publication-useful endnotes, strong public primary links, argument frozen. A 5-page Word submission package with true endnotes and Figure 1 placeholder has been generated and passed page-by-page render QA. Remaining inputs are publication name/affiliation-bio and final image selection: notebook 004 ms p.123 through JHU permission if practical, otherwise the public-domain 1898 JAOS opening page. Do not reopen the argument.**
