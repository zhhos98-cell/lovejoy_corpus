# Martin Guerre and the manufacture of reference states — enrollment, inherited authority, and the changing jurisdiction of witnesses

Date: 2026-09-03  
Status: **TERMINAL HISTORY-OF-KNOWLEDGE CONTROL / NON-GENEALOGICAL / CURRENT-STANDARDS CALIBRATION**  
Companions:
- `martin_guerre_21c_reappearances_history_of_knowledge_sidecar_2026-09-03.md`
- `martin_guerre_21c_verification_regimes_digital_identity_proof_of_humanity_addendum_2026-09-03.md`
- `martin_guerre_davis_about_denis_parliament_identification_regime_source_chain_2010_2020_2026-09-03.md`
- `martin_guerre_case_portability_vs_identification_concept_transmission_2007_2024_2026-09-03.md`
- `martin_guerre_identification_benchmark_convergent_recoding_cole_higgs_thorburn_cgd_2001_2018_2026-09-03.md`

## Central correction

The strongest distinction between the Martin Guerre affair and contemporary digital-identity systems is **not** `memory versus documents`, `subjective recognition versus objective biometrics`, or even `premodern uncertainty versus modern certainty`.

The sharper history-of-knowledge variable is **when and by whom an authoritative reference state is manufactured**.

In the Martin Guerre litigation, the court largely had to construct the relevant reference state **retrospectively, at adjudication**, out of dispersed and differently authorized traces: remembered bodily features, speech and manner, intimate knowledge, kinship recognition, household history, property relations, material signs such as the shoe lasts emphasized by Simon Cole, and the conflicting testimony of people who claimed to know the absent Martin.

In contemporary digital identity, much of the evidentiary labor is moved **upstream**. An identity document or digital credential counts strongly partly because an earlier issuing institution already performed a proofing and enrollment procedure, created or inherited an authoritative record, bound attributes and often biometrics to that record, and retained enough provenance that a later verifier can validate the evidence against an issuing or otherwise authoritative source.

This gives the first approximation:

`Artigat: reconstruct the person from distributed traces when the claim is disputed`

versus

`modern proofing: manufacture / inherit a reference state before later authentication events`.

But the current standards force a second correction: this is not a clean replacement of social knowledge by databases. **Witnesses survive.** Their epistemic jurisdiction changes.

The 2025 NIST identity-proofing standard explicitly permits `applicant references` who can vouch for an applicant's identity, attributes, or circumstances when ordinary evidence, validation, or verification routes are unavailable. What changes is that this testimony is proceduralized: the reference is themselves identity-proofed, the permitted relationship is specified, the role is recorded, statements and signatures may be retained, legal/liability consequences are disclosed, and the use of the reference is entered into the subscriber account.

Thus the better historical contrast is:

`distributed interpersonal knowledge as ordinary evidentiary environment`

→ `heterogeneous evidence ranked, routed, provenance-controlled, and assigned to explicit exception pathways`.

The modern transformation is therefore not the disappearance of the witness. It is the **reallocation of evidentiary jurisdiction**.

## 1. `Reference state` — project vocabulary, not actor vocabulary

`Reference state` is used here as an analytical term. It does not appear as such in Coras, Davis, NIST SP 800-63A-4, eIDAS, or France Identité.

Definition for this dossier:

> **Reference state** = the organized set of prior assertions, records, attributes, bodily/biometric representations, identifiers, relationships, and provenance claims against which a later identity claim can be compared with institutional consequences.

A reference state has at least six variables:

1. **time of production** — before the disputed claim or during its adjudication;
2. **producer** — household/community, clerk, court, state issuer, credential service provider, regulated/private issuer;
3. **carrier** — memory, testimony, inscription, registry, card, number, portrait, biometric template, digital assertion;
4. **validation path** — how the reference itself becomes trusted;
5. **scope/jurisdiction** — which later decisions the reference may authorize;
6. **provenance retention** — whether later users can reconstruct how the reference was made.

This avoids turning `document` or `biometric` into a magic noun. A passport photograph is useful because it participates in an issuance and validation chain; a biometric template is useful because it was enrolled under procedures that establish whose template it is supposed to be. The carrier by itself does not manufacture authority.

## 2. Artigat: a reference state assembled during dispute

The sixteenth-century case has plenty of reference material. The point is not absence of evidence. It is the absence of a single durable, externally maintained, institutionally authoritative record at the resolution required to settle the claim.

The court therefore faced what a modern standards document would separate into several operations at once:

- **resolution**: which socially remembered Martin is the claimant supposed to be?
- **evidence validation**: are remembered marks, relations, and material traces reliable?
- **attribute validation**: are particular bodily traits, biographical details, kinship claims, or household facts accurate?
- **verification**: does the claimant now appearing correspond to those traces?
- **adjudication**: when sources conflict, which relations carry enough authority to settle the legal identity proposition?

These functions were not absent because they lacked NIST names. They were not modularized into a standardized sequence owned by separate institutions and records.

The court had to make a historical person available for comparison while simultaneously deciding which witnesses and signs deserved confidence. **The reference state and the verdict were partly co-produced.**

That co-production is why the case is so epistemically rich: the supposed object of verification, `Martin Guerre`, cannot simply be read from an independent database. His identity has to be assembled from the very social world whose recognition is under dispute.

## 3. NIST 2025: modern identity proofing as a chain of distinct operations

NIST SP 800-63A-4, *Digital Identity Guidelines: Identity Proofing and Enrollment* (published July/August 2025), provides a current high-resolution model of the operations that contemporary identity systems try to separate.

The standard's common sequence is:

`resolution` → `validation` → `verification` → `enrollment`.

### Resolution

The credential service provider (CSP) gathers identity evidence and attributes in order to resolve the applicant to a unique identity in the relevant population and to establish that the claimed identity corresponds to a real-life person.

### Validation

Presented evidence must be shown to be authentic, accurate, and valid. Core attributes are checked against `authoritative or credible sources`.

NIST defines an **authoritative source** as the issuing source of the evidence/attributes or a source with direct access to issuing-source information. A **credible source** can trace its information to authoritative sources or correlate information from multiple sources under regulatory oversight.

### Verification

The CSP then tests whether the applicant is the genuine owner of the validated evidence. Depending on assurance level and pathway, this may involve possession of a digital credential, delivery of codes to validated addresses, visual face-to-document comparison, or automated biometric comparison against the evidence or associated authoritative record.

### Enrollment

After proofing succeeds, the applicant is enrolled into a subscriber account. That account becomes a new managed institutional state from which future authentication and federation operations can proceed.

This sequence exposes a key temporal shift. **Modern verification normally depends on evidence that has already passed through prior issuance events.** The current verifier does not begin from a blank slate.

## 4. Superior evidence proves that authority is inherited from prior proofing

NIST's requirements for `SUPERIOR` identity evidence are exceptionally revealing for the history-of-knowledge argument.

To count at this level, the issuing source must have followed written identity-proofing procedures that gave it high confidence that the claimed identity was associated with the subject; the process is subject to recurring external/public accountability; the subject must have participated in an attended enrollment/proofing procedure confirming physical existence; the evidence must be delivered to the person to whom it relates; it must contain a name, unique reference number, facial image or other biometric, and security features; and later validation must be possible, including cryptographic validation for digital evidence.

The decisive point is recursive:

> **A present verifier can trust strong evidence partly because an earlier issuer already performed an identity-proofing operation.**

The contemporary reference state is therefore not merely `stored data`. It is **stored data plus inherited procedure**.

A chain can look like:

`earlier issuing authority proves subject`

→ `issuer creates evidence + reference number + portrait/biometric + protected data`

→ `later CSP receives applicant + evidence`

→ `CSP validates evidence against issuing/authoritative source`

→ `CSP verifies applicant owns evidence`

→ `CSP enrolls subscriber`

→ `subscriber account records proofing provenance and authenticators`

→ `future relying party authenticates or performs identity matching`.

This suggests a stronger concept than simple `prospective enrollment`:

## **recursive reference-state manufacturing**

Each new identity system can inherit an earlier authorized assertion, validate it, and manufacture a new reference state suitable for later transactions.

## 5. The subscriber account is not just an account; it is a provenance ledger for identity proofing

NIST requires a CSP to maintain a unique subscriber account from enrollment to closure. Importantly for this analysis, the account is required to record not merely the resulting name or identifier but the **history of how the identity proposition was established**.

The record includes, among other things:

- type and issuer of identity evidence;
- proofing type (remote/on-site; attended/unattended);
- validation and verification methods;
- use of trusted referees or exception handling;
- use and identifier of applicant references;
- maximum identity assurance level achieved;
- validated attributes;
- authenticators bound to the account;
- relevant consent records.

This means that modern identity infrastructure can store a second-order fact:

`not only who this subscriber is said to be`

but

`how the system came to be entitled to say so`.

That second-order record is crucial. It converts evidentiary provenance into part of the operational identity object.

The contrast with Martin Guerre is therefore even sharper than `memory versus database`. In Artigat, the court creates a narrative and juridical aggregation of heterogeneous testimony. In NIST's model, the system aims to retain a machine/actionable trace of **which proof pathways generated the asserted identity state**.

## 6. Applicant references: the witness survives inside the machine

The most important corrective in the current standards is the explicit survival of interpersonal vouching.

NIST defines `applicant references` as people with sufficient knowledge to aid identity proofing when other evidence, validation, and verification are unavailable. They may:

- vouch for core attributes;
- vouch for the applicant's identity when sufficient evidence is absent;
- vouch for circumstances affecting the applicant's ability to complete ordinary proofing, such as homelessness or disaster.

Yet this is no return to unstructured village recognition. The reference is themselves proofed to the same or higher assurance level intended for the applicant. The CSP documents permitted uses, may require proof of the relationship, records the relationship and the reference's role in the subscriber account, and may capture statements, signatures, consent, and acknowledgement of legal/liability consequences.

This is an unusually clean example of **epistemic jurisdiction shift**.

### Artigat

`I know this man` can enter the central judicial struggle over identity because ordinary social knowledge is one of the principal reference systems available.

### NIST exception path

`I know this applicant` is admissible only under a defined policy route, from a reference whose own identity and relationship can themselves be proofed and whose intervention acquires a stored provenance trail.

The witness changes from:

`source of substantive person-knowledge`

toward

`regulated component in a larger assurance architecture`.

That is not simply demotion. In some cases the reference may be indispensable. What changes is **jurisdiction, modularity, and auditability**.

## 7. Modernization as proceduralization, not substitution

This finding cuts across a familiar history:

`village memory` → `paper identity` → `biometric identity` → `digital identity`.

That sequence is too carrier-centered. NIST's exception handling shows that memory, relationships, documents, biometrics, addresses, digital accounts, and institutional records can coexist inside one contemporary system. The system's novelty lies less in possessing one superior kind of evidence than in being able to:

1. classify evidence by strength;
2. assign each source a validation path;
3. specify which combinations are sufficient at each assurance level;
4. define exception routes;
5. record provenance;
6. separate proofing from later authentication;
7. bind the result to a subscriber account and authenticator;
8. retain a record of the proofing path for later relying parties.

The historical shift can therefore be restated as:

`heterogeneous evidence socially aggregated in a case`

→ `heterogeneous evidence procedurally ranked and routed in advance`.

This is far more defensible than `subjective witness → objective biometric`.

## 8. France Identité 2026: the parliamentary genealogy becomes an implemented reference-state chain

The France-specific sequence is now especially strong because the 2020 National Assembly report can be connected to a live state identity system rather than left at the level of policy discourse.

France Identité currently offers an `identité numérique certifiée` at the highest security/assurance level. The public procedure requires the user to create the digital identity in the application, initiate certification, confirm email, enter a personal code, read the electronic national identity card by NFC, generate a QR code, and then appear at a mairie or consulate with the card, phone, and QR code. The certification result is returned later to the application.

The current terms of use are even more revealing. For the high eIDAS assurance level, certification includes **face-to-face verification by an authorized municipal agent**, relying especially on comparison of the user's fingerprints with those stored in the electronic component of the national identity card. The stated purpose is to establish with high confidence that the digital identity is issued to the legitimate holder.

Thus the actual reference-state chain is layered:

`civil/biometric identity previously enrolled into CNIe`

→ `card chip stores protected reference data`

→ `app reads CNIe / user initiates digital identity`

→ `authorized municipal agent performs attended face-to-face check + fingerprint-to-chip comparison`

→ `digital identity receives high-assurance certification`

→ `later sensitive transactions (e.g. FranceConnect+, fully online voting proxy) can inherit that certification and dispense with a new police/gendarmerie identity check`.

This is almost a textbook instance of recursive reference-state manufacturing. A physically attended state issuance/certification event is **spent once** to produce a portable digital assertion that can later replace repeated physical appearances.

The relation to Martin Guerre should remain analytical rather than genealogical:

`the court reconstructs an absent prior person at the moment of dispute`

versus

`France Identité deliberately creates a transportable high-assurance state before future remote disputes/transactions occur`.

## 9. Face-to-face recognition has not vanished either

France Identité creates another useful correction. Digital identity does not necessarily remove the face-to-face encounter. At high assurance it can **concentrate** it at enrollment/certification so that later transactions can be remote.

The temporal transformation is therefore:

`repeat local recognition at each consequential encounter`

→ `perform a controlled high-assurance physical encounter once, then reuse its result digitally`.

This makes `at a distance` more precise. Identification at a distance often depends on **a prior moment of controlled proximity**.

That formulation connects Noiriel/Cole/About-Denis to current implementation without turning the sequence into simple technological progress.

## 10. Reference-state recursion versus original identity

A subtle consequence follows. Contemporary identity systems rarely compare a living subject directly to an abstract `original identity`. They compare a new claim to a chain of earlier institutionally accepted claims.

For example:

`current face/fingerprint`

is compared to

`biometric stored on CNIe`,

whose authority depends on

`earlier CNI issuance/enrollment`,

which depends on

`civil-status and supporting records`,

which themselves inherit earlier registrations and institutional assertions.

The authority is recursive rather than foundational.

This suggests a history-of-knowledge question more exact than `how certain is identification?`:

> **How long is the chain of inherited assertions, where can it be independently checked, and where does the system decide that a prior institutional assertion is authoritative enough to stop reopening the whole identity history?**

Martin Guerre is valuable here because the chain has broken. The claimant returns after absence without a sufficiently transportable prior state, so the court has to reopen an unusually large portion of the person's social history.

Modern identity systems try to prevent precisely that epistemic cost by making selected prior assertions portable.

## 11. Identity evidence as compressed historical labor

A useful project formulation follows:

> **An identity credential is compressed historical labor.**

A card, subscriber account, or digital assertion appears at the point of use as a compact token, but its warrant depends on earlier work:

- document collection;
- institutional registration;
- face-to-face checks;
- biometric capture;
- validation against records;
- issuance controls;
- provenance retention;
- cryptographic signing;
- exception handling;
- periodic governance and oversight.

This explains why later systems can appear to `know` identity instantly. They externalize and precompute much of the historical reconstruction that Artigat had to perform during litigation.

The comparison should therefore avoid opposing `human memory` to `machine certainty`. The sharper contrast is:

`adjudication-time evidentiary labor`

versus

`precomputed / inherited evidentiary labor`.

## 12. A revised matrix

| Variable | Martin Guerre litigation | NIST 2025 identity proofing | France Identité certified identity |
|---|---|---|---|
| Reference state | distributed social/biographical reconstruction | evidence + attributes traceable to authoritative/credible sources | CNIe + state records + biometric data + certification event |
| Time of main evidence production | largely retrospective / dispute-time | earlier issuance inherited, then new proofing/enrollment creates subscriber state | earlier CNI issuance plus later certification before sensitive remote use |
| Core verifier | witnesses + court | CSP / proofing agent / validation source | France Titres system + authorized municipal/consular agent |
| Body relation | remembered marks, appearance, embodied recognition | document portrait/biometric or live evidence comparison | fingerprint comparison with CNIe chip, attended check |
| Social witness | central and ordinary evidence source | explicit fallback/exception path (`applicant reference`) | not central in standard certification route |
| Provenance | juridical record/testimony, uneven prior records | proofing path stored in subscriber account | state title/certification process and system records |
| Reuse | verdict settles legal case | subscriber state supports future authentication/federation | certification supports FranceConnect+ and remote sensitive procedures |
| Main epistemic risk | false recognition / misleading memory / conflicting testimony | fraudulent evidence, impersonation, false representation, compromised proofing | usurpation / false holder / compromised credential or process |

## 13. New operator: witness jurisdiction shift

### Definition

**Witness jurisdiction shift** = a historical change in where interpersonal testimony is admitted, how it is ranked relative to other evidence, and what procedural/provenance conditions govern its ability to alter an identity decision.

This is preferable to saying that modernity `eliminates witnesses` or `replaces memory with documents`.

It also creates a better bridge to histories of expertise and proof. The issue is not only whether a witness knows something. It is whether a particular institutional regime allows that knowledge to bear on the target proposition, at which stage, and under what recordkeeping requirements.

The same person's statement can therefore move from:

`primary identification evidence`

→ `corroboration`

→ `exception evidence`

→ `inadmissible/irrelevant for a particular automated transaction`.

That is an historical redistribution of epistemic authority.

## 14. New operator: recursive reference-state manufacturing

### Definition

**Recursive reference-state manufacturing** = the process by which an identity system validates a claimant against evidence whose authority derives from earlier proofing/issuance operations and, after successful proofing, creates a new institutional state that can itself become authoritative evidence for later systems.

Formally:

`R₀` = earlier civil/social/issuer records  
`P₁(R₀, claimant)` → issued evidence `R₁`  
`P₂(R₁, claimant)` → subscriber/certified state `R₂`  
`A₃(R₂, transaction)` → later authentication/assertion.

The recursion terminates operationally when a relying system accepts an earlier authority rather than reopening all prior proof.

This is why modern identity is simultaneously more portable and more infrastructurally dependent.

## 15. Connection to the `retrospective protocolization` finding

The previous note showed how Gelb and Diofasi Metz retrospectively mapped Martin Guerre evidence into modern authentication slots. The current standards show what that mapping leaves out.

Modern assurance is not only about having several factors. It is about:

- **how each factor or evidence item was issued**;
- **which source can validate it**;
- **what assurance level it supports**;
- **whether the claimant owns it**;
- **which exception pathway was used**;
- **whether that proofing history is retained**.

Thus `something you know / have / are` is only one layer. The deeper contemporary architecture is **provenance of the factor itself**.

A sixteenth-century witness relation can be fitted into a factor slot, but doing so hides the fact that modern standards ask a second-order question the historical court also faced in a less modular form:

`Why should we trust this source of recognition?`

## 16. The surprising continuity: identity systems still need social knowledge at the margins

The most important anti-teleological result is that even a highly formal contemporary standard anticipates people who cannot satisfy its normal documentary/reference requirements.

Homelessness, disaster, inaccessible records, minors, and other circumstances create situations in which ordinary authoritative-source validation is insufficient or unavailable. NIST therefore formally reincorporates social knowledge.

This suggests that interpersonal identification is not a superseded historical stage. It is a **residual and sometimes indispensable substrate** that reappears when infrastructural reference states are missing, broken, inaccessible, or mismatched.

The difference between Artigat and NIST is therefore one of **default architecture**, not absolute presence/absence:

- Artigat: social knowledge is structurally central;
- NIST: social knowledge is procedurally exceptional but institutionally anticipated.

That distinction is stronger than a modernization binary.

## 17. What this does to the Martin Guerre afterlife thesis

The 21C case now supports a more exact sequence:

1. Martin Guerre is remembered as an identification failure.
2. Historians turn identification itself into an autonomous object.
3. Policy and technical fields formalize multiple operations previously bundled together.
4. The historical case is retrospectively protocolized into those operations.
5. Current standards reveal that the actual technical novelty is not a single better identifier but **procedural control over evidence provenance, reference-state production, assurance, exception handling, and later reuse**.
6. The surviving role of applicant references prevents the story from becoming `community → state → machine`.

The durable relation is now best stated as:

`claimant` ↔ `reference state` ↔ `validation path` ↔ `verifier` ↔ `authorized assertion`.

## 18. Strongest compressed formulation

**Martin Guerre is most useful to a twenty-first-century history of knowledge when the comparison moves beyond `identity` and even beyond `verification` to the manufacture of reference states. The Artigat court had to reconstruct a disputed person's reference state retrospectively from memories, bodies, relations, material traces, and witnesses while simultaneously deciding which of those sources deserved authority. Current digital-identity systems try to move much of that labor upstream: an issuer proofs a subject, produces protected evidence and an authoritative record; a later CSP validates that evidence against the issuer or another authoritative source, verifies that the applicant owns it, then enrolls a new subscriber state whose proofing provenance is itself retained for later authentication. France Identité makes the recursion concrete: a face-to-face municipal certification and fingerprint comparison against an already-issued electronic identity card generate a high-assurance digital identity that can later substitute for repeated physical identity checks. Yet NIST's explicit `applicant references` show that interpersonal testimony has not vanished. Its epistemic jurisdiction has changed: where ordinary infrastructures fail, social knowledge re-enters as a formal exception path whose witness, relationship, statements, and liability are themselves proofed and recorded. The modern transformation is therefore not memory into database, but heterogeneous knowledge into a procedurally ranked, provenance-bearing, recursively reusable assurance architecture.**

## Sources

### Current US digital-identity standard

- NIST SP 800-63A-4, *Digital Identity Guidelines: Identity Proofing and Enrollment* (2025):
  https://pages.nist.gov/800-63-4/sp800-63a.html
- NIST publication record:
  https://csrc.nist.gov/pubs/sp/800/63/A/4/final

Key sections to retain:
- Identity Proofing Overview: resolution, validation, verification, enrollment.
- Evidence requirements / `SUPERIOR` evidence.
- Validation Sources: authoritative and credible sources.
- Trusted referees and Applicant References.
- Subscriber Accounts.

### France Identité / current French implementation

- `L'identité numérique certifiée France Identité`:
  https://france-identite.gouv.fr/identite-numerique-certifiee/
- France Identité terms of use, section 7, high-assurance certification and face-to-face fingerprint comparison:
  https://france-identite.gouv.fr/conditions-generales-utilisation/cgu-sgin/
- `La procuration de vote`:
  https://france-identite.gouv.fr/usages/la-procuration-de-vote/
- France Identité, `Obtenir son identité numérique à la remise de sa CNI`:
  https://france-identite.gouv.fr/actualite/activation-a-la-remise/

### European framework

- Regulation (EU) 2024/1183, European Digital Identity Framework, especially wallet issuance/onboarding, person identification data, authentication, and cross-border identity matching:
  https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng

### Historical comparative control

- Simon A. Cole, *Suspect Identities: A History of Fingerprinting and Criminal Identification* (Harvard University Press, 2001), especially ch. 1 on Martin Guerre and ch. 9 `Identification at a Distance`.
- Natalie Zemon Davis, *The Return of Martin Guerre* (1983) and Jean de Coras, *Arrest memorable* as primary/historiographical base. Do not use modern standards vocabulary as actors' vocabulary for the sixteenth-century proceedings.

## Evidence cautions

1. `Reference state`, `recursive reference-state manufacturing`, and `witness jurisdiction shift` are project analytical vocabulary.
2. NIST SP 800-63A-4 is a current US federal digital-identity guideline, not a universal description of all modern identification systems.
3. France Identité is a contemporary French state implementation and should not be projected backward onto the 2020 parliamentary report as if every later design detail had already been determined there.
4. The comparison with Martin Guerre is structural, not genealogical. There is no claim that NIST, France Identité, eIDAS, or their designers derived their procedures from the historical affair.
5. `Prospective enrollment` remains useful but is now subordinate to the more accurate recursive model: modern proofing often depends on earlier proofing and issuance, then manufactures a new reusable state.

## Next bounded checks

1. **Historical recursion control:** compare Bertillon/fingerprint enrollment and dossier/index-card systems with NIST's subscriber-account provenance model. The goal is to locate when identity systems begin to preserve not only identifying traces but enough provenance to support repeated institutional reuse.
2. **Witness-jurisdiction history:** trace how personal guarantors, witnesses, referees, notaries, sponsors, and `vouching` survive in passports, immigration, banking/KYC, refugee documentation, homelessness services, and digital-ID exception processing.
3. **France chain:** inspect technical/ANSSI documentation for France Identité's high-assurance certification to separate public-facing procedure from the exact security/reference-state architecture.
4. **Failure/recovery:** investigate account recovery and re-proofing. A reference state is historically most visible when it fails, is compromised, or has to be re-established. This may provide the closest contemporary structural analogue to Martin Guerre's broken continuity.
