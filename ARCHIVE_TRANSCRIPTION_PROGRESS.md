# Lovejoy manuscript transcription progress

## Working method

Manuscript notebooks are corrected in batches of 15–20 PDF pages against the page images. PaddleOCR-VL is used only as a scaffold. The corrected JSON preserves Lovejoy's abbreviations where readable, marks uncertain/illegible readings explicitly, records visible manuscript page labels, and keeps source PDF/OCR SHA-256 values so each batch is auditable.

## MS38_004_001_061_004 — “Sankhya + Buddhism”

- Source PDF: 71 pages.
- Completed: PDF pp. 1–71.
- Status: **complete first pass**.
- GitHub batches:
  - `archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json`
  - `archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json`
- Remaining work is second-pass verification only: explicitly marked low/medium-confidence French quotations, Pali/Sanskrit passages, and compressed bibliographic references.
- **Published-paper cross-read completed:** `research_notes/MS38_004_001_061_004_vs_1898_Buddhistic_Technical_Terms.md`.
- Direct formal counterpart identified: Arthur O. Lovejoy, “The Buddhistic Technical Terms upādāna and upādisesa,” *Journal of the American Oriental Society* 19 (1898), 126–136. Repository already contains a full-text HTML copy.
- Current evidential judgment: later portions of the notebook are very likely preparatory or contemporaneous working notes for the 1898 paper, but exact notebook dating remains to be established; the whole notebook appears broader than the published article.

### Source-derived topics in pp. 55–71

- Lovejoy maps the twelve nidānas onto the khandhas and compares Buddhist technical vocabulary with Sāṁkhya and Vedānta.
- Extended analysis of `upādāna`, `upādhi`, `upādisesa`, and `anupādisesa`.
- Nirvāṇa is separated from parinirvāṇa / extinction without residue.
- Notebook closes with a historical-structural outline: original elements = flux / Three Characteristics + Dependent Origination; derived elements = theory of sense-perception + psychology + khandhas.

### Notebook ↔ 1898 article: current result

- The article directly publishes the notebook's late-stage `upādāna` / `upādisesa` problem and its Senart–Oldenberg–Childers–Rhys Davids source constellation.
- Notebook work on overlapping nidāna/khandha taxonomies is compressed in print into a three-stage interpretation of dependent origination; the article explicitly rejects a strict temporal-sequence reading.
- A central continuity is methodological: Lovejoy accepts that terms/ideas may be historically borrowed or composite while arguing that their arrangement can still be original, characteristic, and intelligible.
- The notebook's final “original elements / derived elements” outline is not printed as such. Its first half survives strongly in the article's elevation of dependent origination + the Three Characteristics; much of the Sāṁkhya chronology, sensory psychology, and khandha taxonomy is omitted.
- The article therefore looks like a sharply delimited extraction from a broader notebook project, not a transcription of the notebook as a whole.

## MS38_004_001_061_005 — faint front-leaf title “Symbolism” [?]

- Source PDF: 120 pages.
- Completed: PDF pp. 1–90.
- GitHub batches:
  - `archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json`
  - `archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json`
- Batch 6 manuscript page labels: 153, 155, 157, 159, 161, 163, 165, 167, 171, 173, 175, 177, 179, 181, 183. (The visible sequence skips 169 in the scan organization; PDF p. 84 carries 171.)
- Next batch: PDF pp. 91–105.
- Correction policy: especially difficult ethnographic names, multilingual titles, and compressed source references remain provisional; where handwriting is too poor for diplomatic transcription, only source-supported argumentative structure is retained.

### Source-derived topics in pp. 1–15

- Future-life beliefs initially treated as continuations of this-worldly status rather than inherently moral reward/punishment.
- Distinction between moral, magical, ritual, social/community, and status-based determinants of post-mortem destiny.
- Origin-of-death myths and an analytic outline moving from naturalistic continuity through ritual/social determinants toward strictly moral guilt.

### Source-derived topics in pp. 16–30

- Lovejoy repeatedly distinguishes naturalistic continuity, ritual/social selection, and strictly moral desert in future-life beliefs.
- Suicide, missionary influence, differentiated post-mortem destinations, corporeal/functional soul conceptions, and a limited future life ending in a “second death” or annihilation.

### Source-derived topics in pp. 31–45

- Shift to totemism, clan/gens definitions, Hebrew eschatology, `nephesh` / `ruach`, blood and life, and Greek `psychē` / `thymos` comparisons.
- Comparative outline spanning Old Testament, Greek primitive, New Testament/intermediate, Hellenistic-Roman, and Persian materials.

### Source-derived topics in pp. 46–60

- Extended comparative typology of sacrifice: funerary/alimentary, mystical or communion, expiatory/scapegoat, magical, fecundative, and god-man/divine-victim forms.
- Blood, shared meals, and corporate ritual as mechanisms for producing kinship or union.
- Robertson Smith and Frazer handled critically; Lovejoy warns against constructing anthropological schemes beyond the evidence.
- “Living god-man” distinctions among human representative, god in propria persona, funerary/substitutionary sacrifice, and magical efficacy.

### Source-derived topics in pp. 61–75

- Magical or imitative sacrifice is separated from sacrifice directed to personal gods: some rites act directly on forces of nature rather than by persuading or constraining divine wills.
- Lovejoy treats syncretism historically. Rituals that now look like one sacrificial form may combine motives that were once distinct; analysis must separate inherited ritual elements before assigning a type.
- Funerary sacrifice is treated first as provision and social continuity for the dead: food, blood, property, attendants, wives, slaves, or retainers continue the deceased person's household and status into the next life.
- Human versus animal sacrifice is explicitly rejected as a simple evolutionary index. Animal sacrifice can be later than human sacrifice, and apparent “advancement” cannot be inferred from victim type alone.
- Ritual killing, cannibalism, punishment of failed rain-makers/diviners, animal sanctity, totemic-looking restrictions, and sacrifice are repeatedly distinguished rather than collapsed into one category.
- Southern-African bibliography and cases dominate the comparative apparatus, especially Callaway, Bleek, Hahn, Kolbe, Casalis, Livingstone, Cowper Rose, Lewis Grout, and related works; several titles remain provisional because of handwriting.
- Destruction or burning of property at funerals is treated as a case of reinterpretation: a practice may begin as prevention of the dead's return and later be explained as releasing/transferring the object's spirit to the dead.
- Offerings to dead chiefs often contain expected advantage or reciprocity, but Lovejoy also identifies loyalty to the deceased as a distinct motive that should not automatically be redescribed as propitiation or contract.

### Source-derived topics in pp. 76–90

- Human sacrifice can function as utilitarian communication with the dead: the victim may serve as a messenger rather than as the object of worship.
- Zulu ancestral-sacrifice material (via Lewis Grout) is treated transactionally: illness, neglected ancestors, a demanded cow, and an explicit bargain for cure. Lovejoy separates this from unconditional gift and from mystical union.
- Substitution/scapegoat mechanisms appear alongside alimentary and funerary sacrifice; the sacrificed cow can be asked to carry away illness or evil, while its skull/horns become protective or fetish objects.
- Circumcision is analyzed as incorporation through blood. Shared shedding of blood creates fraternity/blood-brotherhood and admission into the tribal or paternal circle, with rights and responsibilities transmitted socially through the rite.
- Foundation/building sacrifices and use of human flesh, bones, eyes, or blood as protective charms are repeatedly separated from sacramental communion. The victim's material remains can be credited with direct magical efficacy.
- Blood is treated as life-giving, curative, rejuvenating, protective, and transferable; Lovejoy compares Trumbull and Strack and explicitly distinguishes magical use from medical effect or sacrifice proper.
- A conceptual distinction emerges between fetish and charm/amulet. A fetish depends on an indwelling/present spirit; an amulet, plant, drug, stone, or body substance can be credited with efficacy intrinsic to the object.
- Miss Kingsley's West-African material supports a broader point: for the conceptual world Lovejoy is reconstructing, medicinal, magical, natural, and supernatural efficacies are not sharply separated. Belladonna and mandragora can be treated as parallel kinds of efficacious things.
- Human sacrifice can also be used to bind/control a spirit at a place, while blood sprinkled at houses during epidemic disease functions as a protective charm rather than necessarily as sacrifice.
