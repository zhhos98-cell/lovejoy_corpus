# Repository CSV batch consolidation manifest

Date: 2026-08-23
Scope: logically lossless consolidation of historical CSV batch deltas; manuscript transcriptions, research prose, primary-source OCR, and curated canonical indexes are retained.

## Preservation method

- Each consolidated row contains `source_file`, `source_batch`, `source_row`, and `source_field_count`.
- Original source headers are preserved below; consolidated tables use the union of all source columns without silently normalizing distinct fields.
- Pre-existing overlong CSV records are preserved in explicit `source_overflow_N` columns; short rows retain their original field count.
- Every original CSV row was hashed as its exact parsed field sequence and verified against its reconstruction from the consolidated output before removal.
- Original complete file bytes remain retrievable from the preceding Git commit; SHA-256 values below verify exact recovery.
- Existing Markdown references to old delta paths were redirected to their corresponding consolidated tables.
- Pre-existing canonical indexes and versioned, referenced source-uptake maps were not overwritten or deleted.

## Summary

| Family | Original files | Data rows | Union data columns | Consolidated file |
|---|---:|---:|---:|---|
| Orientalist source-register deltas | 61 | 420 | 22 | `research_notes/lovejoy_orientalist_source_register_batch_deltas_consolidated.csv` |
| Notebook 005 source-register deltas | 26 | 183 | 40 | `research_notes/MS38_005_source_register_batch_deltas_consolidated.csv` |
| Global archive repository-coverage deltas | 17 | 51 | 12 | `archive_index/lovejoy_global_archive_repository_coverage_batch_deltas_consolidated.csv` |
| Global archive lead deltas | 13 | 31 | 14 | `archive_index/lovejoy_global_archive_leads_batch_deltas_consolidated.csv` |
| Global archive component deltas | 10 | 28 | 21 | `archive_index/lovejoy_global_archive_component_batch_deltas_consolidated.csv` |

Original delta files consolidated: **127**.
Original data rows preserved: **713**.

## Pre-existing CSV field-count anomalies

| Original file | Source row | Header columns | Actual fields |
|---|---:|---:|---:|
| `research_notes/lovejoy_orientalist_source_register_batch16_delta.csv` | 5 | 8 | 12 |
| `research_notes/lovejoy_orientalist_source_register_batch29_delta.csv` | 8 | 8 | 9 |
| `research_notes/lovejoy_orientalist_source_register_batch101_delta.csv` | 7 | 9 | 8 |
| `research_notes/MS38_005_source_register_batch57_delta.csv` | 7 | 9 | 11 |
| `archive_index/lovejoy_global_archive_component_batch96_delta.csv` | 5 | 20 | 21 |

## Orientalist source-register deltas

Consolidated destination: `research_notes/lovejoy_orientalist_source_register_batch_deltas_consolidated.csv`

| Original file | Rows | SHA-256 | Original header |
|---|---:|---|---|
| `research_notes/lovejoy_orientalist_source_register_batch11_delta.csv` | 8 | `b5e8af19de9092b49e42ca43dac1a53d7ca40096a699187769f85c2e8e6fccbb` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch12_delta.csv` | 7 | `c448778ad6f454087e474bd1d229801801ee8ef16e7f31781384b8f0b29c4854` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch15_delta.csv` | 5 | `ea156338d5f384376813fc3e07080c16ffe1f92e10c5c575286525a64d894785` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch16_delta.csv` | 6 | `f243b189c61ef0e59aca64dff16ff3684441fdad27479a7899b53fa96fdf8944` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch17_delta.csv` | 9 | `d6e9be43802af9787fb4f42b3acf6a1e7b46aa472fa3039f47836a5adedfc5cb` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch18_delta.csv` | 6 | `dce83d5971e42e93e88c172056b3b48660bc4df1d9c5c404c36f59a61684370e` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch19_delta.csv` | 5 | `7fd49ecc6a73a9d8a7abcd305de1bad39785975531039633aaf62e20e260556c` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch20_delta.csv` | 6 | `f43e93116e3ff392a37b059e075ec8852e907015afd0306d2ed9a9d12bcfb036` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch21_delta.csv` | 6 | `75f3cdd1e775b523d2e6ade26ff22eaed30747f19929af488f2b6c4259bc85e4` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch22_delta.csv` | 8 | `78ced6eaa2911ebdabb1b9e9af3e0ef52af3eba5b7246d5a2d226f3f6c8ddbf9` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch23_delta.csv` | 19 | `58d8888b9dd739aa001073e32a3442f9b544e861d16a33154de3a6a3546a5384` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch24_delta.csv` | 8 | `13a966f715ec4ac2fa633aad3e4342ede81919d818c49a0e397c5d81e5d105a2` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch25_delta.csv` | 8 | `cdc18da83e7bd0c871f78e0da5b5afbfb48ba5ea985a505b9ed570860edb25ba` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch26_delta.csv` | 5 | `4789d1d3b64775d26b80dc9e22e50bde69718f46c45086ed224dc62a5197a78f` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch27_delta.csv` | 8 | `b74e82d714a9b529f62991d9f761fc5f555d2109922ae6d8074d26a6ad7cfc7c` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch28_delta.csv` | 8 | `c197e7c56a59a5a81a04c99beb78aea9a1e56af7c7ae56a708b2be5441bbc1ca` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch29_delta.csv` | 7 | `0de023afe6f9a32261ee1e0f4ec2f060a5a08f21bdfb24b2539b2daf47aec98d` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch30_delta.csv` | 6 | `59be2bed07200d7a900602520052a466435f35b690d59d7faf11dbc8d271eb32` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch31_delta.csv` | 7 | `e6c69e5f1ed3ed86016e3f5f1426a92451e8e36ef2996295bb42b9c4d1533e36` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch32_delta.csv` | 8 | `94c2fa325c69587922261724a2369024bc05d4d56dac06dbc60ba5144f7532dc` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch33_delta.csv` | 10 | `a29a3f6b2f9abf5b59b5086c90cf2e8fd33581368e5daedf45041b6a3c21d665` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch35_delta.csv` | 6 | `2161cc2784867b32a5222443a086ac75d98ad5971a5a60db8ce460b5261c66e6` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch39_delta.csv` | 6 | `ca9cff6307f65ee78a2886718107b92dc932266ee16728d42c91a30b27c8d867` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch40_delta.csv` | 5 | `eacb02cd0c0fc21d70ed28dddba90a7c2b433bf0e3e764b0d7496000e3355b9a` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch41_delta.csv` | 6 | `d4989cc1a7c94b68c858fb4788dd52324981a1756e5b7f5d053859c63b464e67` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch42_delta.csv` | 9 | `395fd8513ba1c0b37affae0ee810c40f6daf1aabd56c51cc3690ec257d8f1f75` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch43_delta.csv` | 6 | `2f9166b95d5fbd4664a58cf4d898cb7d02a1c5c42897f78dcb16c7cfc7bcae54` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch44_delta.csv` | 5 | `a0c35a89fef657a65b9abc5d9d316e447ee90ad35530b091b6053cc9a30ee499` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch45_delta.csv` | 5 | `bd0c366753d17b5ef10a6c7b3766b4d60fbe73e0edc6dcef73873a460abb9521` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch46_delta.csv` | 5 | `29cba9691e246f61c90cb9b9efe8c520aea40eb3bfc493722ce4f26847cdbd03` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch47_delta.csv` | 5 | `cbf1cef65c5e7761b9979f35c8331223d0291545a084398aa91d6efe4d0c34c9` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch48_delta.csv` | 7 | `aaac6818ccd390c608331443b7f1d7be1ea0a1a8083bf892ac430b5c5035b751` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch75_delta.csv` | 7 | `746397246ede68c9104e29221da6586257a6cf4e295ef0b7da4727948a3b3404` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch76_delta.csv` | 6 | `abdd347855116dc61bbadd977512a188119d961dbd522c46c9aa65691aaa4f79` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch77_delta.csv` | 8 | `f8d6e6165ca410e8aeba84a2834fa6a5a434bad78279635ca7b9ca9e64e55871` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch78_delta.csv` | 8 | `f4d8aa508f37a733982ada42543a42627abc776fec56ca8361e68f1abd90fee2` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch79_delta.csv` | 7 | `4f22b5428c58a51cc9709beed6a0788e840adf9d8545ff87b29279387ef2c7cf` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch80_delta.csv` | 6 | `97dae7622e55aa48970fe5d2c08e1a0ca82a98c7dd4cee94961e8e69d2ba6573` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch81_delta.csv` | 9 | `01fde40a19947ee6e9d4a9608ada209479932523bd91389185d0414df46c7e42` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch82_delta.csv` | 5 | `146ec98cbb7979f02b0de186f08e0972947875f4f44b4be1553ab9891c6d2ef5` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch83_delta.csv` | 4 | `d47c0adbf7fa48582699991b6c480306fdaccc479fdbc2ec2eacc22dbe37f711` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch84_delta.csv` | 4 | `73ea063b2a1ea9d877b128c37c6f80694c5a9f9f6e6fe5f25203f8bdc515094b` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch85_delta.csv` | 4 | `a07f617e9675deac19092a5fe5454d353937e8988b0d5bcca74bd0febc875af1` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch86_delta.csv` | 5 | `0c66dbf954da3c1778debe69fe547244b7d46659a444c82e6d51a9291cbcbdca` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch87_delta.csv` | 7 | `a5f5acfe9c2127b62e51e52fd940b6f99c95409ff92d452658798d149a5f3deb` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch89_delta.csv` | 6 | `fd91f1482a6b9dd5997aa20c735fa8bc792a6b80e1ed7c0709df2ed0cb0c20d5` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch91_delta.csv` | 7 | `ed1ad7af130372adcf2275f50a871ae41bd95a588cb10c4e66d7b5df1f02f3a3` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch92_delta.csv` | 5 | `22baa0fe51b935c007e3985fa5e18fa33f83fcda52afd4875d1e94f8936f1ee6` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch93_delta.csv` | 8 | `c1833ee80b0dc50e43592966ead4b65aad1135b2a08f813b36f4b5d3a06fd8df` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch94_delta.csv` | 5 | `68490e97d9a411c4f43b7ec7aeb8d0d8d0e26023ea2d8325fa639509317b7052` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch96_delta.csv` | 8 | `babd5fb2b80db1308b64648fd4c443059cab9ca5b1d59626cd00865a42332267` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch97_delta.csv` | 6 | `762557e871dee83591111164df6c2f613e88dfc7bca651b29b4f31648e633b90` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch99_delta.csv` | 8 | `ee4bd79029ad9bb2aa61e2c12f17d26c701f42088eca22f1c0caf81945f4966a` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch101_delta.csv` | 7 | `f573c509a4c9c1654e3a669c8723443ee5a466ef710bd86e20a2d30eef48cbe8` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch104_delta.csv` | 5 | `434c8fbc4ede780936a5e002c3d5c9464785dc5342df1b155d9364b7780406b4` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch106_delta.csv` | 8 | `e6a999cabd4c1fd2d9c1ac861696cd9c37589e338120bdf999bbab5c1afa5e6d` | `source_id, date, author, title, venue_or_repository, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch117_delta.csv` | 9 | `f47f7ba1d7f506357d077016d99da497304a970315fd2267f676f24b5e8456ca` | `source_id, date, author, title_or_object, repository_or_venue, locus, status, use, limitations` |
| `research_notes/lovejoy_orientalist_source_register_batch13_14_delta.csv` | 6 | `a42c55d382fcab237d1d02eb94efe86e71193af97b685d858e7400671384eaf6` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch29_sacrifice_primary_delta.csv` | 6 | `96dfa8745c77c55376fcc9b387dd86f2a160c3a305cd008c684216f95ead3584` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batch30_marillier1900_delta.csv` | 10 | `6092c9948f307820805798ee79dd042f5a84bb9332a69b1cc94fcdd278743182` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/lovejoy_orientalist_source_register_batches25_26_delta.csv` | 11 | `a9e98d473335d50b3c13d9b5ef675078a31c93382fc44abc1d8d6669e1667316` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |

## Notebook 005 source-register deltas

Consolidated destination: `research_notes/MS38_005_source_register_batch_deltas_consolidated.csv`

| Original file | Rows | SHA-256 | Original header |
|---|---:|---|---|
| `research_notes/MS38_005_source_register_batch41_delta.csv` | 3 | `a60ca85e7210c0c4ecd74920abf5e851242ea36ccca390c75033a417007d6cb7` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch42_delta.csv` | 3 | `7ae6464639f073704138d6b02071e3950ba8c6f355c56f2acf870583d2c860dd` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch43_delta.csv` | 4 | `e48482f093560ecf6baf36589066f69fb504162c3d179773495d6a6d5868f4f1` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch44_delta.csv` | 5 | `15cee9ff0f85134d774e522bbe9195ff9270cdcdd6a426d9fba6b523e556ceda` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch45_delta.csv` | 5 | `d45dcc242edb4392dfa130f5f8cc9a83c911662bc11bd7c0d92dfb24ccefa7f8` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch46_delta.csv` | 6 | `762518a9edcc35520b1d5b81f8d1001fe7f35e8cf6b625d1e4b20c13027f8c8b` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch47_delta.csv` | 6 | `cf5381a81c0a09729051af900673bbe8b291e53cfa91ffd1e0da9436359b3549` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch48_delta.csv` | 9 | `55b8651010830a196c4a71574aa499b62a44357e84b46da273ceeaf0d99b27e4` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch49_delta.csv` | 11 | `865e91d9c747c493e5a01715a2d2c3b19c8f53ef13920bc0947ff2106e4a4c4c` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch50_delta.csv` | 5 | `cd0f21829273885b76f065c894d3bf7fc0b994bad0d911229a745ee97bec422c` | `source_id, source_type, date, title_or_description, author_or_signature, location_or_url, relevance_to_MS38_005, evidentiary_use, caution` |
| `research_notes/MS38_005_source_register_batch51_delta.csv` | 6 | `39ecea506c19a792dd6a0719a840a13f4eba0d2750beb336a99cd7cce12beae3` | `source_id, source_type, date, title_or_description, author, local_file, relevance_to_004_005, evidentiary_use, caution` |
| `research_notes/MS38_005_source_register_batch52_delta.csv` | 6 | `279ffa5caa47139c717a82cfdaf7ac3bdd05d4e6debde05b8589c8d2056c45d9` | `source_id, source_type, date_or_stage, proposition, evidentiary_use, claim_strength, notes` |
| `research_notes/MS38_005_source_register_batch53_delta.csv` | 8 | `f49319792e17a776b0f1836b42cc5d04d0d55ea23edd39a205f4b145926fc28f` | `source_id, source_type, date, locus, claim, evidence_status, use` |
| `research_notes/MS38_005_source_register_batch54_delta.csv` | 10 | `ec8ff32b2542620cc2a64ac8fcb1d07d1fa0b15f5f6655a0523fa9be2f183670` | `source_type, author, date, title_or_item, locus_or_pages, url_or_archive, role_in_argument, evidence_status, caution` |
| `research_notes/MS38_005_source_register_batch55_delta.csv` | 11 | `ce18b07565ad2c163bbcdf7188c5d756a4b971f833e4aab86e71793ab7452ede` | `source_type, author, date, title_or_item, locus_or_pages, url_or_archive, role_in_argument, evidence_status, caution` |
| `research_notes/MS38_005_source_register_batch56_delta.csv` | 7 | `b07edb219e0fc06fcea8e37ee1decba021e0cabc33fefd43055c279be70d7d26` | `source_type, author, date, title_or_item, locus_or_pages, url_or_archive, role_in_argument, evidence_status, caution` |
| `research_notes/MS38_005_source_register_batch57_delta.csv` | 8 | `7029465591535fdf91dc7447fa3e694b144b0026cb14b9058e119fb45f7150ae` | `source_type, author, date, title_or_item, locus_or_pages, url_or_archive, role_in_argument, evidence_status, caution` |
| `research_notes/MS38_005_source_register_batch58_delta.csv` | 7 | `4a89433c9276902b5d5e2c57e3558d1f88a662f5089fabae735a8ee3e9a7cbd3` | `source_id, author, date, title, exact_locus, source_type, relevance, evidence_status, relation_to_lovejoy, notes` |
| `research_notes/MS38_005_source_register_batch59_delta.csv` | 5 | `12519abbd8c09ff8fac37219b2a9b253716769db974ef75b677572347a735e75` | `source_id, author, date, title, exact_locus, source_type, relevance, evidence_status, relation_to_lovejoy, notes` |
| `research_notes/MS38_005_source_register_batch60_delta.csv` | 9 | `f64612ae8be3fb62702d793edc4ca70fd8b2becbc501bf9860fc667b62e86d77` | `source_id, author, date, title, exact_locus, source_type, relevance, evidence_status, relation_to_lovejoy, notes` |
| `research_notes/MS38_005_source_register_batch61_delta.csv` | 11 | `5b3ed482d79b4c25c7feea60d1691e4abf6d38fbdbe8d186eaf41b400da35f0f` | `source_id, actor, date, title_or_description, source_type, url_or_location, relevance, evidence_status, notes` |
| `research_notes/MS38_005_source_register_batch62_delta.csv` | 8 | `1b6a3578a115c8868e93c2f6433b9a4dce7601a67be6127a03c60f67530bfb5c` | `source_id, actor, date, title_or_description, source_type, url_or_location, relevance, evidence_status, notes` |
| `research_notes/MS38_005_source_register_batch68_delta.csv` | 7 | `698e6b1caf254eb0bbb92ba5020708fcda010c62d4b1c73d49d25cbd3e3bcdc8` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch69_delta.csv` | 9 | `115e04bbf23748abfa29140f93752c31ba8903e584be081b17c5445c42c6221a` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch70_delta.csv` | 6 | `5b0ff45e37d3000ded2adec31a45e530a8b5e5fce29aec6c2e124306f89108fb` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |
| `research_notes/MS38_005_source_register_batch72_delta.csv` | 8 | `7c051e139169e260a65f270ba3a4155c130b4defe9051ce1703e964f2ef76c02` | `date_or_range, evidence_class, scope, item_or_person, source_or_repository, status, significance, next_action` |

## Global archive repository-coverage deltas

Consolidated destination: `archive_index/lovejoy_global_archive_repository_coverage_batch_deltas_consolidated.csv`

| Original file | Rows | SHA-256 | Original header |
|---|---:|---|---|
| `archive_index/lovejoy_global_archive_repository_coverage_batch90_delta.csv` | 5 | `11c889fd4b7c09f27e65b30a64ae51b27f3f8b53e5528adb8d18df424a35b369` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch103_delta.csv` | 3 | `7c23f1320f860b1e8da4f351176370c3c35a99909831524583264fc77f0f6648` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch105_delta.csv` | 1 | `ddba5f3d49e47a8955e3cc31b717b76abc640bbcf5515cfafb08e17c9b498a94` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch107_delta.csv` | 5 | `ea74ed2d62abf73c9d51d8ab7bbb61dd7c6eaa906262b09794bf07f4dd49629a` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch108_delta.csv` | 2 | `1bc050b482f1265015270a002aab19f1dc7387e2f0b921ec97fe3f9a2410027a` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch109_delta.csv` | 4 | `4cc750cf95c0523388e24bdc65d38310a51170c806bb9132f449226f9ef5d608` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch110_delta.csv` | 2 | `eab4132647a22dfc569eeb0c6f264b36f0fc9834cb6114db6e762b4937f92fa0` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch111_delta.csv` | 2 | `8ebe7b25bf0acdc976f0ff94c015ae1d31bff5afa20f19ab7bbc0fd197960d25` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch112_delta.csv` | 4 | `1b1d443722dfe449cfe058f4f641ffc18b8c16484e7425585096e5e72ecac174` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch113_delta.csv` | 3 | `44dd884e364c918a57882add8f462d5a87ec31600b6d7295303493dd22ef9ace` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch114_delta.csv` | 4 | `e1f7d799fde330087cfd947aab26836213f5587dcc3002333c48f62eca0155a7` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch115_delta.csv` | 3 | `cc6b51ee034e874a8d73b61f8b18ff8f6f38b9bd6ec38699114987ac85070d33` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch116_delta.csv` | 3 | `4dedee0b6302749a39d01b7787102ade89f191b83483ace05d1fbf4b0f3cc171` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch118_delta.csv` | 4 | `02991bb81aca07a3479a6319106b6ca95798895f6cd83b9563be8a5051ae5551` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch120_delta.csv` | 4 | `e68faefafbbd168718b4a2b904bf161d39e86d6223cc619d3a8545d0d3bc35b5` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch121_delta.csv` | 1 | `82b4c4dc3acec089af07bd00a465ccb6f0240fc728ef46aa9c4597fd003ee41f` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |
| `archive_index/lovejoy_global_archive_repository_coverage_batch122_delta.csv` | 1 | `932d0159c075d242f3aa9be3830cc63063f81e6a224c0b7bac29dedf7b34b0be` | `coverage_id, country, repository_or_portal, query_mode, query_terms, primary_hits, new_components_added, unresolved_leads, negative_result_scope, next_action, checked_at, source_url` |

## Global archive lead deltas

Consolidated destination: `archive_index/lovejoy_global_archive_leads_batch_deltas_consolidated.csv`

| Original file | Rows | SHA-256 | Original header |
|---|---:|---|---|
| `archive_index/lovejoy_global_archive_leads_batch90_delta.csv` | 3 | `211df0deb0fef3ccec1f4272cedfdbe64a7097b9f92dfb9f91ed11dfef8bcdba` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch95_delta.csv` | 6 | `326cc7e068a994bb853a1c55249bf7f5ad66b8e4cee1b5143a8d99f970e775ba` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch96_delta.csv` | 4 | `c8537f13fd498adb3d9e902b22d3d91b0d0f5675201c35e860d8215382627def` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch100_delta.csv` | 4 | `c1c13eb15b03917d65837ad9865fb50fb5ffd0efe232f5c408f94f5ad02ca478` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch102_delta.csv` | 2 | `7ea153d8a6daf92425d3666722691b5634101f381a70f066bac4044ca81e246d` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch103_delta.csv` | 2 | `1d4bdb1826f65f0c458e6accc0882084fccdf82f27b045e55afa5dbac4b1a4e6` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch107_delta.csv` | 2 | `298d3daba6d12dc78c5a1e31d04e5c6a08c8cbdf08f6b403065cdc87187b0a6f` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch112_delta.csv` | 2 | `b80681d4948561cbd3b52f49b505dab78fc7827bab177b8c0358e2a4ffc2822d` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch113_delta.csv` | 1 | `a3ec8cea0370105717e6eb038d115e79b820334f6998f8dc1ee2b9a0ebfbac33` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch114_delta.csv` | 1 | `377c63715da436e8993cf74facb1a56d6c51d3aed1c0de29560bcc08996b86d4` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch120_delta.csv` | 2 | `36768adab1c68913ab57e75173ebb002172450c34f7633dfa3c8e6551b5048fb` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch121_delta.csv` | 1 | `fe326e7272b733722ddf53444602e4b3e9d4ed713c8d0b38cfde89be42e0fad7` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |
| `archive_index/lovejoy_global_archive_leads_batch122_delta.csv` | 1 | `7ee843e3bba3ff284eb11be8a6fa978ebcccbf2f76178e1c2d9112d810409ef6` | `delta_action, lead_id, country, repository, collection_title, collection_id, lead_basis, person_or_network_pivot, expected_material, primary_presence_status, component_locator_status, source_url, next_query, notes` |

## Global archive component deltas

Consolidated destination: `archive_index/lovejoy_global_archive_component_batch_deltas_consolidated.csv`

| Original file | Rows | SHA-256 | Original header |
|---|---:|---|---|
| `archive_index/lovejoy_global_archive_component_batch90_delta.csv` | 2 | `5df40fed10c2cf5f1e904c58f6821a284e3f28de46556948bd046872269c6f19` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch95_delta.csv` | 6 | `383c28f6fbd9f2489e078c9b0e98b6810f9ab7437f5ffbf5027c1bb38c4b654a` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch96_delta.csv` | 4 | `30a735df7f43aaf8bc947a120cd3d0bef8fa5348ab5d9d8c35730f1680c6865d` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch98_delta.csv` | 2 | `d7e8723bfc5f6fb5a4a558e3a9b4c104d67fd49d509e66ebc697bd57356ac22c` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch100_delta.csv` | 2 | `9e3426e829fcb7f10b52fe53dd905fc93942bc0bc7a31c926ba21c835c1d2e9a` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch102_delta.csv` | 2 | `c9d0ce765c5ed10c916be40d07c0b405d304d178848683a4e5198e51ba6f487b` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch105_delta.csv` | 4 | `2be428e26956a0793ef62c4e2d8fc0370bbca20cfaf00f0c144a08a0ffc4a8dd` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch107_delta.csv` | 2 | `fd1f3560515430333d7f4343c17a512b6ab17bd57fd22c69b379f15718095e5b` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch110_delta.csv` | 3 | `59e315e85758b25709c2ea07af2724ab3bc0fe6ddcfc214d0d1439f3617b3584` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |
| `archive_index/lovejoy_global_archive_component_batch112_delta.csv` | 1 | `7dcd5536e9b8ee036b6656710f8da7c6117d53cf71e11daed66d2589f9695766` | `record_id, country, repository, collection_title, collection_id, series_path, component_title, description_level, date_start, date_end, extent, lovejoy_role, other_party, box, folder, item_or_folio, source_status, verification_status, source_url, notes` |

## Exact duplicate removed

- Removed: `gallica_lovejoy_primitive_raw.csv`
- Retained identical copy: `gallica_lovejoy_primitive_deduped.csv`
- Size: 160 bytes
- SHA-256: `aff4788e27b932196e1a3bfe9573e4d8519bbb4ec22cae26febbe5962c368171`

## Changed historical notes

- `README.md`
- `research_notes/lovejoy_global_archive_harvest_batch100_1919_pensions_Stone_CFAT_Cattell.md`
- `research_notes/lovejoy_global_archive_harvest_batch102_Box83_custody_address_Tyler.md`
- `research_notes/lovejoy_global_archive_harvest_batch103_Box24_citation_conflicts_Young_Hodder_Eggert.md`
- `research_notes/lovejoy_global_archive_harvest_batch105_Science_Service_RU7091.md`
- `research_notes/lovejoy_global_archive_harvest_batch107_Science_Service_morgue_opportunity_map.md`
- `research_notes/lovejoy_global_archive_harvest_batch108_Science_Service_1941_1962.md`
- `research_notes/lovejoy_global_archive_harvest_batch109_Science_Service_1941_gap_provenance.md`
- `research_notes/lovejoy_global_archive_harvest_batch110_JHU_authority_crosscollection.md`
- `research_notes/lovejoy_global_archive_harvest_batch111_Wilson_registry_provenance.md`
- `research_notes/lovejoy_global_archive_harvest_batch112_Hamburger_Russell_Stanford_Elliott.md`
- `research_notes/lovejoy_global_archive_harvest_batch113_Goodnow_filing_Stanford_letterpress.md`
- `research_notes/lovejoy_global_archive_harvest_batch114_JHU_secretary_Stanford_manifestation_domains.md`
- `research_notes/lovejoy_global_archive_harvest_batch115_Hamburger_RG02001_Elliott_Ross_cluster.md`
- `research_notes/lovejoy_global_archive_harvest_batch116_JHU_departmental_files_Stanford_microfilm.md`
- `research_notes/lovejoy_global_archive_harvest_batch118_Russell_Woods_interception.md`
- `research_notes/lovejoy_global_archive_harvest_batch120_Harvard_president_Corporation.md`
- `research_notes/lovejoy_global_archive_harvest_batch121_Foakes_Jackson_reciprocal.md`
- `research_notes/lovejoy_global_archive_harvest_batch122_McGiffert_reciprocal.md`
- `research_notes/lovejoy_global_archive_harvest_batch90_Eiseley_Hamburger_Hook_Tamiment.md`
- `research_notes/lovejoy_global_archive_harvest_batch95_WWI_academic_freedom_and_manifestation_audit.md`
- `research_notes/lovejoy_global_archive_harvest_batch98_AAUP_foundation_crosswalk.md`
