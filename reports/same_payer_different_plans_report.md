# Same Payer, Different Plans — Report

_Generated: 2026-11-02 02:33:34_

**Identity rule:** A payer is uniquely identified by its **Federated Payer Identifier (FPI)**. Directory names are for human convenience only. The intended design is **one file per payer**: plans with different endpoint sets are placed in separate `plan_groups` within that single file, and plans sharing the same endpoint set belong in the same `plan_group`. The same FPI appearing in multiple files is an anomaly worth review.

## Summary

| Metric | Count |
|--------|------:|
| Total payer files scanned | 788 |
| Files successfully parsed | 784 |
| Unique FPIs (distinct payers) | 784 |
| **FPIs appearing in multiple files** (anomalies to review) | **0** |
| FPIs appearing in exactly one file | 784 |
| Redirect/tombstone files (retired FPIs pointing to new files) | 4 |
| Files missing an FPI | 0 |
| Parse errors | 0 |

## Distribution: Number of Files per FPI (Payer)

Each row shows how many payers (FPIs) have exactly N files. Payers with N > 1 are anomalies: the intended design is one file per payer.

| Files per FPI | # Payers | Notes |
|-------------:|---------:|-------|
| 1 | 784 | expected: one file per payer |

## FPIs in Multiple Files (Anomalies to Review)

_No FPI currently appears in more than one file. This is the intended design: one file per payer, with distinct endpoint sets expressed as separate plan_groups within that file._

## Single-File Payers (Intended Design)

These **784 payers** each have exactly one file. Payers with more than one endpoint group are the 'same payer, different plans' cases, expressed as multiple plan_groups within their single file. Sorted by number of endpoint groups (descending), then plan count (descending).

| FPI | Payer Legal Name | # Endpoint Groups | # Plan IDs | Category |
|-----|-----------------|----------------:|----------:|----------|
| `e70682ba-9bbd-5f22-93b3-1f614b5e97e3` | CARE IMPROVEMENT PLUS SOUTH CENTRAL INSURANCE CO. | 18 | [288](per_fpi/care_improvement_plus_south_central_insurance_co.md) | medicare_advantage |
| `3810db9f-6f86-5ffa-aae8-dcac4ad54100` | ANTHEM INSURANCE COMPANIES, INC. | 8 | [72](per_fpi/anthem_insurance_companies_inc.md) | medicare_advantage |
| `4a1989ae-68b4-543d-8fd5-f1c450c570ee` | HEALTHSPRING LIFE & HEALTH INSURANCE COMPANY, INC. | 6 | [147](per_fpi/healthspring_life_health_insurance_company_inc.md) | medicare_advantage |
| `86b3404d-15ba-5cd9-9943-7d37b988ea31` | UnitedHealthcare Benefits of Texas, Inc. | 5 | [93](per_fpi/unitedhealthcare_benefits_of_texas_inc.md) | medicare_advantage |
| `9cba4b22-e8eb-50cc-8ee6-60407f67bc98` | UNITEDHEALTHCARE OF WISCONSIN, INC. | 4 | [155](per_fpi/unitedhealthcare_of_wisconsin_inc.md) | medicare_advantage |
| `b4b01325-46ac-59f0-ba40-a9b60f160265` | UNITEDHEALTHCARE INSURANCE COMPANY | 4 | [79](per_fpi/unitedhealthcare_insurance_company.md) | medicare_advantage |
| `3aa3a6db-78cd-50ce-a2a1-7607ecd6850c` | BRAVO HEALTH PENNSYLVANIA, INC. | 4 | [32](per_fpi/bravo_health_pennsylvania_inc.md) | medicare_advantage |
| `635d88a7-4343-5d10-b6f9-19557bb2c090` | CALIFORNIA PHYSICIANS' SERVICE | 4 | [30](per_fpi/california_physicians_service.md) | medicare_advantage |
| `802add3a-5485-5113-8382-9f99ed799975` | ATRIO HEALTH PLANS | 4 | [20](per_fpi/atrio_health_plans.md) | medicare_advantage |
| `62d427ba-0a19-51c0-a850-929a7a13b7fa` | BLUE CROSS AND BLUE SHIELD OF NORTH CAROLINA | 4 | [19](per_fpi/blue_cross_and_blue_shield_of_north_carolina.md) | medicare_advantage |
| `e4230a2d-0bcd-50cc-945a-01bda86afcea` | MASS GENERAL BRIGHAM HEALTH PLAN, INC | 4 | [13](per_fpi/mass_general_brigham_health_plan_inc.md) | medicare_advantage |
| `f03f57b1-6793-5eca-adab-2d7ea4be6a73` | UNITEDHEALTHCARE OF NEW ENGLAND, INC. | 4 | [7](per_fpi/unitedhealthcare_of_new_england_inc.md) | medicare_advantage |
| `d7da1a2a-9065-52b7-81ed-784d34a852a0` | KAISER FOUNDATION HP, INC. | 3 | [65](per_fpi/kaiser_foundation_hp_inc.md) | medicare_advantage |
| `4d80cbfa-cc05-5e98-85f8-4d9f86ace59f` | AETNA HEALTH INC. (PA) | 3 | [64](per_fpi/aetna_health_inc_pa.md) | medicare_advantage |
| `7bfc9422-b9e8-5393-a738-be518372b4af` | MMM HEALTHCARE, LLC | 3 | [58](per_fpi/mmm_healthcare_llc.md) | medicare_advantage |
| `de0b5352-4910-5038-947b-84f2386a7774` | SCAN HEALTH PLAN | 3 | [58](per_fpi/scan_health_plan.md) | medicare_advantage |
| `d200dd80-cef2-5f2d-973f-8c34cfcf9779` | HEALTHKEEPERS, INC. | 3 | [40](per_fpi/healthkeepers_inc.md) | medicare_advantage |
| `a0a279d8-03e2-5c72-be75-d1d8d969d39c` | TUFTS ASSOCIATED HEALTH MAINTENANCE ORGANIZATION | 3 | [25](per_fpi/tufts_associated_health_maintenance_organization.md) | medicare_advantage |
| `2bf4e887-1f3b-5586-b90f-8197ab78cb09` | MEDICA HEALTH PLANS | 3 | [19](per_fpi/medica_health_plans.md) | medicare_advantage |
| `7ddebcff-f6ac-5c04-9e50-726b90ee1461` | MVP HEALTH PLAN, INC. | 3 | [18](per_fpi/mvp_health_plan_inc.md) | medicare_advantage |
| `3509d768-fa7e-59b0-92fb-8423bd348369` | NETWORK HEALTH INSURANCE CORPORATION | 3 | [17](per_fpi/network_health_insurance_corporation.md) | medicare_advantage |
| `29524cbd-c255-5097-a691-1bd7cd075c35` | COMMUNITY INSURANCE COMPANY | 3 | [14](per_fpi/community_insurance_company.md) | medicare_advantage |
| `2bbe8987-ed5d-5d13-b000-f2bd8c58dcdd` | HEALTHFIRST HEALTH PLAN, INC. | 3 | [9](per_fpi/healthfirst_health_plan_inc.md) | medicare_advantage |
| `51804d38-3c94-5913-a059-69e63258101d` | MERIDIAN HEALTH PLAN OF MICHIGAN, INC. | 3 | [9](per_fpi/meridian_health_plan_of_michigan_inc.md) | medicare_advantage |
| `1cc05dc0-cdc8-5bfc-9ac0-9e47c75fbcb6` | SANFORD HEALTH PLAN | 3 | [9](per_fpi/sanford_health_plan.md) | medicare_advantage |
| `de4043cd-3e66-538a-a076-da281afba40c` | FALLON COMMUNITY HEALTH PLAN | 3 | [8](per_fpi/fallon_community_health_plan.md) | medicare_advantage |
| `2e9a30eb-6366-5776-9092-8e101adf0d63` | HAWAII MEDICAL SERVICE ASSOCIATION (HMSA) | 3 | [3](per_fpi/hawaii_medical_service_association_hmsa.md) | medicare_advantage |
| `26b98260-d3c6-588b-8ff5-5638059ef168` | SIERRA HEALTH AND LIFE INSURANCE COMPANY, INC. | 2 | [176](per_fpi/sierra_health_and_life_insurance_company_inc.md) | medicare_advantage |
| `e3083786-ea3b-5182-9309-a4434b66219f` | HEALTH CARE SERVICE CORPORATION | 2 | [84](per_fpi/health_care_service_corporation.md) | medicare_advantage |
| `d762c1aa-f916-53c2-95c4-d4be587289cb` | SILVERSCRIPT INSURANCE COMPANY | 2 | [73](per_fpi/silverscript_insurance_company.md) | medicare_advantage |
| `70fde76f-d2fe-5154-9f43-87236074d1d3` | UNITEDHEALTHCARE OF THE MIDLANDS, INC. | 2 | [68](per_fpi/unitedhealthcare_of_the_midlands_inc.md) | medicare_advantage |
| `e34a9e9f-7ecb-5e77-9e1f-9e445ec05547` | ALIGNMENT HEALTH PLAN | 2 | [45](per_fpi/alignment_health_plan.md) | medicare_advantage |
| `f845400e-1cb2-56c4-be5a-223ca536855f` | TRIPLE S ADVANTAGE, INC. | 2 | [38](per_fpi/triple_s_advantage_inc.md) | medicare_advantage |
| `9c1841f7-ee00-5dfb-90e6-a96b30cd30c6` | EXCELLUS HEALTH PLAN, INC. | 2 | [35](per_fpi/excellus_health_plan_inc.md) | medicare_advantage |
| `f3b818fd-0e36-5778-b571-b0ad18365a80` | ZING HEALTH OF MICHIGAN, INC. | 2 | [33](per_fpi/zing_health_of_michigan_inc.md) | medicare_advantage |
| `dd1a1b69-b2a7-5e69-a02d-b9ff1841ea34` | PRIORITY HEALTH | 2 | [30](per_fpi/priority_health.md) | medicare_advantage |
| `f85c0872-dadd-5ef8-8dfe-67f85d30a230` | BLUE CROSS AND BLUE SHIELD OF FLORIDA, INC. | 2 | [25](per_fpi/blue_cross_and_blue_shield_of_florida_inc.md) | medicare_advantage |
| `4362ee58-edf3-5b8c-a3e5-c00d926d137d` | UNITEDHEALTHCARE OF THE ROCKIES, INC. | 2 | [25](per_fpi/unitedhealthcare_of_the_rockies_inc.md) | medicare_advantage |
| `05685002-f569-596d-ab46-2483cce42cc4` | Sunshine State Health Plan, Inc. | 2 | [24](per_fpi/sunshine_state_health_plan_inc.md) | medicare_advantage |
| `79eb93d9-1e50-50a2-bc9a-d1d1a2190748` | Anthem HP, LLC | 2 | [20](per_fpi/anthem_hp_llc.md) | medicare_advantage |
| `bab23acc-4386-5882-9251-499d422ab7eb` | DEVOTED HEALTH PLAN OF NORTH CAROLINA INC | 2 | [20](per_fpi/devoted_health_plan_of_north_carolina_inc.md) | medicare_advantage |
| `968ce0f6-dad2-5f3a-831c-cab1913dd3fe` | Highmark Western and Northeastern New York Inc. | 2 | [20](per_fpi/highmark_western_and_northeastern_new_york_inc.md) | medicare_advantage |
| `31e1e607-57a8-5151-9e9a-7b354200da6d` | INDEPENDENT HEALTH BENEFITS CORPORATION | 2 | [20](per_fpi/independent_health_benefits_corporation.md) | medicare_advantage |
| `76997d1c-b107-5702-ada9-45e3d82c6e38` | PACIFICSOURCE COMMUNITY HEALTH PLANS | 2 | [20](per_fpi/pacificsource_community_health_plans.md) | medicare_advantage |
| `06fc9dfc-5a8d-5837-90ab-8a0111002d89` | BCBSM, Inc. | 2 | [19](per_fpi/bcbsm_inc.md) | medicare_advantage |
| `3caaab70-bd6b-5cea-9629-41464381631c` | DEVOTED HEALTH PLAN OF OHIO INC | 2 | [19](per_fpi/devoted_health_plan_of_ohio_inc.md) | medicare_advantage |
| `01d07022-750c-5513-bbde-7d8e365d786b` | HEALTHPARTNERS, INC. | 2 | [19](per_fpi/healthpartners_inc.md) | medicare_advantage |
| `5674dcd3-81a7-5b24-80d0-79f3372f9e6e` | BLUE CROSS OF CALIFORNIA PARTNERSHIP PLAN, INC. | 2 | [18](per_fpi/blue_cross_of_california_partnership_plan_inc.md) | medicare_advantage |
| `e4727998-af85-5e5f-81a9-0947f9bf23bb` | COVENTRY HEALTH CARE OF ILLINOIS, INC. | 2 | [18](per_fpi/coventry_health_care_of_illinois_inc.md) | medicare_advantage |
| `df53db1f-a123-5ec6-ac0f-44acd82ff900` | ALIGNMENT HEALTH PLAN OF NORTH CAROLINA, INC. | 2 | [17](per_fpi/alignment_health_plan_of_north_carolina_inc.md) | medicare_advantage |
| `83f65c03-0a8a-530a-8adc-710df9ad570f` | UNITEDHEALTHCARE OF NEW YORK, INC. | 2 | [17](per_fpi/unitedhealthcare_of_new_york_inc.md) | medicare_advantage |
| `bbc298be-7484-562d-9deb-10eef0ff76e9` | BCBS OF MICHIGAN MUTUAL INSURANCE COMPANY | 2 | [16](per_fpi/bcbs_of_michigan_mutual_insurance_company.md) | medicare_advantage |
| `9244f3ba-4304-586e-bc60-0b3e3586992d` | BLUE CROSS OF IDAHO HEALTH SERVICE, INC. | 2 | [16](per_fpi/blue_cross_of_idaho_health_service_inc.md) | medicare_advantage |
| `43dbd5dc-51eb-55f6-bdb2-3d062a0161c8` | PEOPLES HEALTH, INC. | 2 | [16](per_fpi/peoples_health_inc.md) | medicare_advantage |
| `f771c63e-8db8-5cad-a6a1-e43c2d064194` | SUPERIOR HEALTHPLAN, INC. | 2 | [16](per_fpi/superior_healthplan_inc.md) | medicare_advantage |
| `2aaa0b79-5315-5566-999f-e17c5622d6ce` | WELLCARE OF GEORGIA, INC. | 2 | [15](per_fpi/wellcare_of_georgia_inc.md) | medicare_advantage |
| `d4ce548c-92c8-5b9a-99f7-ffbf33b6d293` | BLUECROSS AND BLUESHIELD OF SOUTH CAROLINA | 2 | [14](per_fpi/bluecross_and_blueshield_of_south_carolina.md) | medicare_advantage |
| `f9eaa64d-9b83-5df9-a14e-74d9a39838b2` | MEDICAL MUTUAL OF OHIO | 2 | [14](per_fpi/medical_mutual_of_ohio.md) | medicare_advantage |
| `f26c3fb5-972a-58ec-9c7b-52d8c44edd91` | UNITEDHEALTHCARE COMMUNITY PLAN OF TEXAS, L.L.C. | 2 | [14](per_fpi/unitedhealthcare_community_plan_of_texas_l_l_c.md) | medicare_advantage |
| `7140441f-fdae-5656-8b04-0e4555b5e45d` | ANTHEM HEALTH PLANS, INC. | 2 | [13](per_fpi/anthem_health_plans_inc.md) | medicare_advantage |
| `48703f73-abbe-52a7-8fa0-93a62461f5a5` | DEAN HEALTH PLAN, INC. | 2 | [13](per_fpi/dean_health_plan_inc.md) | medicare_advantage |
| `5f6b5b70-8934-5f7b-80a0-b51935a2a1d1` | AMERICAN PROGRESSIVE LIFE & HLTH INS COMPANY OF NY | 2 | [12](per_fpi/american_progressive_life_hlth_ins_company_of_ny.md) | medicare_advantage |
| `891f883a-9652-59fa-bb6d-e610c20ef26f` | BCBS  OF MASSACHUSETTS HMO BLUE, INC. | 2 | [12](per_fpi/bcbs_of_massachusetts_hmo_blue_inc.md) | medicare_advantage |
| `79f4a501-9061-5779-8649-0c04fa9b5fd8` | HEALTH NEW ENGLAND, INC. | 2 | [12](per_fpi/health_new_england_inc.md) | medicare_advantage |
| `9b2030b9-fe6b-5241-88fe-07647f944f4f` | USABLE MUTUAL INSURANCE COMPANY | 2 | [12](per_fpi/usable_mutual_insurance_company.md) | medicare_advantage |
| `d1dcfe38-272a-5b66-86b2-057c1db30f6c` | BLUE CROSS & BLUE SHIELD OF RHODE ISLAND | 2 | [11](per_fpi/blue_cross_blue_shield_of_rhode_island.md) | medicare_advantage |
| `b8e11313-3ebf-5d33-b92b-d3175e0e2cd7` | MARTIN'S POINT GENERATIONS ADVANTAGE, INC. | 2 | [11](per_fpi/martin_s_point_generations_advantage_inc.md) | medicare_advantage |
| `7e79a360-e83c-516e-9b4c-7868d98042fa` | AETNA HEALTH INC. (GA) | 2 | [10](per_fpi/aetna_health_inc_ga.md) | medicare_advantage |
| `00dc2085-57e1-58db-bfbb-329903f4841a` | HEALTH INSURANCE PLAN OF GREATER NEW YORK | 2 | [10](per_fpi/health_insurance_plan_of_greater_new_york.md) | medicare_advantage |
| `e1007a4c-3b18-5d76-b4a1-6a3beb35589f` | HIGHMARK BCBSD, INC. | 2 | [10](per_fpi/highmark_bcbsd_inc.md) | medicare_advantage |
| `d8a8f3e0-a8df-52a3-88a1-f662d14352f3` | NEW YORK QUALITY HEALTHCARE CORPORATION | 2 | [10](per_fpi/new_york_quality_healthcare_corporation.md) | medicare_advantage |
| `2815d5d6-0a50-5989-b7f1-6d8d953f2e27` | WELLCARE HEALTH INSURANCE OF ARIZONA, INC. | 2 | [10](per_fpi/wellcare_health_insurance_of_arizona_inc.md) | medicare_advantage |
| `5fdd02dc-e85b-58fa-9fc7-e4d6804ea417` | CAREFIRST ADVANTAGE PPO, INC. | 2 | [9](per_fpi/carefirst_advantage_ppo_inc.md) | medicare_advantage |
| `34f06611-5079-54c4-b7d3-30fbe00e24d1` | QCC INSURANCE COMPANY | 2 | [9](per_fpi/qcc_insurance_company.md) | medicare_advantage |
| `65ff12e6-070c-55f9-9e7c-57b153bd67b5` | REGENCE BLUECROSS BLUESHIELD OF OREGON | 2 | [9](per_fpi/regence_bluecross_blueshield_of_oregon.md) | medicare_advantage |
| `b0d77de3-506c-5cef-85d0-db6796d8d927` | WELLCARE HEALTH INSURANCE COMPANY OF KENTUCKY, INC | 2 | [9](per_fpi/wellcare_health_insurance_company_of_kentucky_inc.md) | medicare_advantage |
| `bf53b386-343f-5483-a4c1-e83f9027bc80` | SAPPHIRE EDGE, INC. | 2 | [8](per_fpi/sapphire_edge_inc.md) | medicare_advantage |
| `e31a77db-4b6f-5d1c-bc27-dbb1af7d8163` | UNITEDHEALTHCARE OF THE MID-ATLANTIC, INC. | 2 | [8](per_fpi/unitedhealthcare_of_the_mid_atlantic_inc.md) | medicare_advantage |
| `616f8458-a32e-5437-8153-d6044228372e` | ALIGNMENT HEALTH ADVANTAGE PLAN INC. | 2 | [7](per_fpi/alignment_health_advantage_plan_inc.md) | medicare_advantage |
| `c162b24a-164f-58ec-a7bf-145ad631677d` | BUCKEYE COMMUNITY HEALTH PLAN, INC. | 2 | [7](per_fpi/buckeye_community_health_plan_inc.md) | medicare_advantage |
| `adb8767f-3f31-51e6-bd37-3889dba67e84` | CARE N' CARE INSURANCE COMPANY OF NORTH CAROLINA | 2 | [7](per_fpi/care_n_care_insurance_company_of_north_carolina.md) | medicare_advantage |
| `3ffb4943-7259-519f-8f2e-8f0a1c72504d` | HOPKINS HEALTH ADVANTAGE, INC. | 2 | [7](per_fpi/hopkins_health_advantage_inc.md) | medicare_advantage |
| `7496fe09-c03d-5fbe-bda4-5cda142de91e` | MOLINA HEALTHCARE OF ILLINOIS INC | 2 | [7](per_fpi/molina_healthcare_of_illinois_inc.md) | medicare_advantage |
| `42077c02-9f3c-5e40-99d2-abb7c73a28b0` | NEBRASKA TOTAL CARE, INC. | 2 | [7](per_fpi/nebraska_total_care_inc.md) | medicare_advantage |
| `c0c2d45e-c587-5f49-9284-1c3a2c65075e` | REGENCE BLUESHIELD | 2 | [7](per_fpi/regence_blueshield.md) | medicare_advantage |
| `42ef6515-685a-5ee1-8d07-936095dccb4f` | COORDINATED CARE CORPORATION | 2 | [6](per_fpi/coordinated_care_corporation.md) | medicare_advantage |
| `732dac1f-75ef-554e-97c6-0e83f241e6e6` | MERIDIAN HEALTH PLAN OF ILLINOIS, INC. | 2 | [6](per_fpi/meridian_health_plan_of_illinois_inc.md) | medicare_advantage |
| `59dedb80-0f1d-51d9-be82-a5b9c937ad2e` | MOLINA HEALTHCARE OF TEXAS, INC. | 2 | [6](per_fpi/molina_healthcare_of_texas_inc.md) | medicare_advantage |
| `73acd73c-b15a-5b12-9b34-b0dc289a124a` | SUNFLOWER STATE HEALTH PLAN, INC. | 2 | [6](per_fpi/sunflower_state_health_plan_inc.md) | medicare_advantage |
| `cf638a3a-9adc-5467-9f1b-774ae5d0a3a9` | WELLCARE OF SOUTH CAROLINA, INC. | 2 | [6](per_fpi/wellcare_of_south_carolina_inc.md) | medicare_advantage |
| `bb51ea7b-fd3f-5ff5-beea-b98af7e62fde` | AETNA BETTER HEALTH OF MICHIGAN INC. | 2 | [5](per_fpi/aetna_better_health_of_michigan_inc.md) | medicare_advantage |
| `352578a1-e8c8-5bf5-88c8-c9baf321c0a7` | SOUTHEASTERN INDIANA HEALTH ORGANIZATION, INC. | 2 | [4](per_fpi/southeastern_indiana_health_organization_inc.md) | medicare_advantage |
| `f116b686-97bf-5ef5-8c8e-2f0ad52b973d` | UNITEDHEALTHCARE COMMUNITY PLAN, INC. | 2 | [4](per_fpi/unitedhealthcare_community_plan_inc.md) | medicare_advantage |
| `1049ade9-b07a-5a3c-a8f2-3790bbc7d471` | ETERNALHEALTH, INC. | 2 | [3](per_fpi/eternalhealth_inc.md) | medicare_advantage |
| `d66a597b-1d42-57fd-8cc3-2a84f66e8135` | MOLINA HEALTHCARE OF CALIFORNIA | 2 | [3](per_fpi/molina_healthcare_of_california.md) | medicare_advantage |
| `f11c7850-e8b9-5fd2-aea9-9834ea5aa36d` | ORANGE COUNTY HEALTH AUTHORITY | 2 | [3](per_fpi/orange_county_health_authority.md) | medicare_advantage |
| `7d00d7c3-ba77-569b-a1cf-5a9462a9dcab` | SENIOR WHOLE HEALTH, LLC | 2 | [3](per_fpi/senior_whole_health_llc.md) | medicare_advantage |
| `3d1f1587-f654-5520-b69f-fc04d3bc8cca` | USABLE HMO, INC. | 2 | [3](per_fpi/usable_hmo_inc.md) | medicare_advantage |
| `e4d4119d-7a88-56be-9701-3b280f3e0029` | COMMONWEALTH CARE ALLIANCE, INC. | 2 | [2](per_fpi/commonwealth_care_alliance_inc.md) | medicare_advantage |
| `90603419-0c53-551b-95b6-ae6697c8a4bc` | COMMUNITY HEALTH GROUP | 2 | [2](per_fpi/community_health_group.md) | medicare_advantage |
| `27f1b030-6583-5f7a-aef5-5af2cfa35918` | PRIMEWEST RURAL MN HEALTH CARE ACCESS INITIATIVE | 2 | [2](per_fpi/primewest_rural_mn_health_care_access_initiative.md) | medicare_advantage |
| `8097711b-9336-5229-94b1-b56c649eadf7` | SOUTH COUNTRY HEALTH ALLIANCE | 2 | [2](per_fpi/south_country_health_alliance.md) | medicare_advantage |
| `8dcf98bb-6b38-5030-91fd-a0dc73bb6e85` | HEALTHY MISSISSIPPI, INC. | 2 | [1](per_fpi/healthy_mississippi_inc.md) | medicare_advantage |
| `cc8ee1d0-aa21-546a-9038-b6e7d2ec3f4a` | HEALTHY ARKANSAS, INC. | 2 | [0](per_fpi/healthy_arkansas_inc.md) | medicare_advantage |
| `d476c29e-5c66-559b-99de-b11454be84bc` | HUMANA INSURANCE COMPANY | 1 | [330](per_fpi/humana_insurance_company.md) | medicare_advantage |
| `a04283f0-5a1d-5df8-a744-e252652a1783` | AETNA LIFE INSURANCE COMPANY | 1 | [237](per_fpi/aetna_life_insurance_company.md) | medicare_advantage |
| `370fa3a4-f96c-597f-b3f8-926241f83db9` | EMPHESYS INSURANCE COMPANY | 1 | [115](per_fpi/emphesys_insurance_company.md) | medicare_advantage |
| `08eac1f4-81cb-5916-b6ac-932ab165e626` | UNITEDHEALTHCARE INS. CO. & UHC INS. CO. OF NY | 1 | [111](per_fpi/unitedhealthcare_ins_co_uhc_ins_co_of_ny.md) | medicare_advantage |
| `b8871bc5-892d-5703-be75-2d91a2b78e6f` | HUMANA MEDICAL PLAN, INC. | 1 | [108](per_fpi/humana_medical_plan_inc.md) | medicare_advantage |
| `2e3bb0d7-5ae6-56fd-84b4-10db172d1d6c` | Humana Insurance Co. & Humana Insurance Co. of NY | 1 | [107](per_fpi/humana_insurance_co_humana_insurance_co_of_ny.md) | medicare_advantage |
| `be096f84-0f01-5721-acdb-c73ad89cf341` | ARCADIAN HEALTH PLAN, INC. | 1 | [74](per_fpi/arcadian_health_plan_inc.md) | medicare_advantage |
| `3a48f3e5-2910-567c-91d2-6c2e0ef84cc5` | DEVOTED HEALTH PLAN OF FLORIDA, INC. | 1 | [72](per_fpi/devoted_health_plan_of_florida_inc.md) | medicare_advantage |
| `dcd99036-b7a0-565a-8fa5-3257c9830377` | MEDCO CONTAINMENT LIFE AND MEDCO CONTAINMENT NY | 1 | [70](per_fpi/medco_containment_life_and_medco_containment_ny.md) | medicare_advantage |
| `000e3086-4430-59d4-a74e-adefa6212c25` | WELLCARE PRESCRIPTION INSURANCE, INC. | 1 | [68](per_fpi/wellcare_prescription_insurance_inc.md) | medicare_advantage |
| `ff3610bd-c40f-5560-a648-96351050f884` | HUMANA WI HEALTH ORGANIZATION INSURANCE CORP | 1 | [59](per_fpi/humana_wi_health_organization_insurance_corp.md) | medicare_advantage |
| `1bb307a6-c023-59af-9a93-1b5ede7f0542` | HUMANA BENEFIT PLAN OF ILLINOIS, INC. | 1 | [55](per_fpi/humana_benefit_plan_of_illinois_inc.md) | medicare_advantage |
| `3a6fa3ac-04a2-5e6b-98ad-8849fc80d995` | AETNA HEALTH INC. (FL) | 1 | [51](per_fpi/aetna_health_inc_fl.md) | medicare_advantage |
| `5a9fa2fc-147e-57b9-8a9f-e43836218896` | CARITEN HEALTH PLAN INC. | 1 | [50](per_fpi/cariten_health_plan_inc.md) | medicare_advantage |
| `7ce29967-93bf-5099-a2e3-4f88bc8e6ac9` | SIMPLY HEALTHCARE PLANS, INC. | 1 | [50](per_fpi/simply_healthcare_plans_inc.md) | medicare_advantage |
| `39e07b49-229e-5418-ba1b-098d94b8db21` | CHA HMO, INC. | 1 | [46](per_fpi/cha_hmo_inc.md) | medicare_advantage |
| `92cdb058-4280-5a82-b390-1deb2cba96a6` | UHC OF CALIFORNIA | 1 | [46](per_fpi/uhc_of_california.md) | medicare_advantage |
| `d2688a5e-7e05-59a7-80d3-62c27e80162a` | COVENTRY HEALTH AND LIFE INSURANCE COMPANY | 1 | [38](per_fpi/coventry_health_and_life_insurance_company.md) | medicare_advantage |
| `ef7ebf45-26ee-511f-b44f-ecf4da077edd` | HIGHMARK SENIOR HEALTH COMPANY | 1 | [37](per_fpi/highmark_senior_health_company.md) | medicare_advantage |
| `cfe8f2f7-41e0-548e-80bf-f71a17449b64` | PREFERRED CARE PARTNERS, INC. | 1 | [36](per_fpi/preferred_care_partners_inc.md) | medicare_advantage |
| `f2315744-0a27-522a-b0d0-f1a76d6216ac` | MCS ADVANTAGE, INC. | 1 | [35](per_fpi/mcs_advantage_inc.md) | medicare_advantage |
| `2039ae24-53f2-58ec-8677-f7c958b2a2db` | CAREPLUS HEALTH PLANS, INC. | 1 | [33](per_fpi/careplus_health_plans_inc.md) | medicare_advantage |
| `690e8968-c344-5e46-84e7-0cb74305f4e1` | COVENTRY HEALTH CARE OF MISSOURI, INC. | 1 | [33](per_fpi/coventry_health_care_of_missouri_inc.md) | medicare_advantage |
| `88eeadce-ebf0-5f68-ba8f-f2cbeaff5f5f` | UNITEDHEALTHCARE INSURANCE COMPANY OF NEW YORK | 1 | [33](per_fpi/unitedhealthcare_insurance_company_of_new_york.md) | medicare_advantage |
| `f1e4bbd8-5aa9-5dc3-b34c-ea6fb6e8bad3` | DEVOTED HEALTH PLAN OF TEXAS, INC. | 1 | [32](per_fpi/devoted_health_plan_of_texas_inc.md) | medicare_advantage |
| `a7ce6ba0-c7c0-5b83-a23b-639a8be0b867` | MEDCO CONTAINMENT LIFE & MEDCO CONTAINMENT NY & HEALTH CARE SERVICE CORPORATION | 1 | [29](per_fpi/medco_containment_life_medco_containment_ny_health_care_service_corporation.md) | medicare_advantage |
| `71883f8c-9de5-5549-a1e9-2489b39cdb1c` | BLUE CROSS OF CALIFORNIA | 1 | [28](per_fpi/blue_cross_of_california.md) | medicare_advantage |
| `3caf5cc9-552f-502f-bae2-0bbe8e520a69` | AETNA HEALTH OF OHIO INC. | 1 | [26](per_fpi/aetna_health_of_ohio_inc.md) | medicare_advantage |
| `2298bcd1-4147-5d70-a642-f9e6c7d2b7cb` | HCSC INSURANCE SERVICES COMPANY | 1 | [26](per_fpi/hcsc_insurance_services_company.md) | medicare_advantage |
| `77365ae2-3c43-5e52-8931-be1dfe6af7e4` | PHYSICIANS HEALTH CHOICE OF TEXAS, LLC | 1 | [26](per_fpi/physicians_health_choice_of_texas_llc.md) | medicare_advantage |
| `68d4ceb9-93f6-548c-912b-f9f43eb79683` | AETNA HEALTH AND LIFE INSURANCE COMPANY | 1 | [25](per_fpi/aetna_health_and_life_insurance_company.md) | medicare_advantage |
| `d887d34b-5509-51a2-b57d-1ae20a8cb800` | FREEDOM HEALTH, INC. | 1 | [25](per_fpi/freedom_health_inc.md) | medicare_advantage |
| `970b75e4-7657-5182-b992-e3db65fd7431` | HUMANA HEALTH BENEFIT PLAN OF LOUISIANA, INC. | 1 | [24](per_fpi/humana_health_benefit_plan_of_louisiana_inc.md) | medicare_advantage |
| `b4b27b31-c5ef-5ecc-b231-0588abc286dc` | SOLIS HEALTH PLANS, INC. | 1 | [24](per_fpi/solis_health_plans_inc.md) | medicare_advantage |
| `3426e238-f98b-5612-abe9-775e1106c67f` | KAISER FDTN HLTH PLAN OF THE MID-ATLANTIC STATES | 1 | [23](per_fpi/kaiser_fdtn_hlth_plan_of_the_mid_atlantic_states.md) | medicare_advantage |
| `0866e8ea-fc6d-578b-b96c-03cdb9296775` | KAISER FOUNDATION HP OF CO | 1 | [23](per_fpi/kaiser_foundation_hp_of_co.md) | medicare_advantage |
| `0415a42d-47c6-55fa-91b8-c8faf3530002` | AETNA BETTER HEALTH INC. (GA) | 1 | [22](per_fpi/aetna_better_health_inc_ga.md) | medicare_advantage |
| `b1affe56-4f6e-59a1-893e-f611f1dd8b5b` | AETNA HEALTH INC. (TX) | 1 | [22](per_fpi/aetna_health_inc_tx.md) | medicare_advantage |
| `cd4ee33d-e65d-51eb-9017-baefee71d11d` | HARMONY HEALTH PLAN,  INC. | 1 | [22](per_fpi/harmony_health_plan_inc.md) | medicare_advantage |
| `39a826af-3886-59d7-ac38-fcb73597eeba` | HIGHMARK CHOICE COMPANY | 1 | [22](per_fpi/highmark_choice_company.md) | medicare_advantage |
| `f03b01ab-3a70-5e59-9c29-407739d9b1c1` | HMO COLORADO, INC. | 1 | [22](per_fpi/hmo_colorado_inc.md) | medicare_advantage |
| `a7483286-f29d-5fa3-9586-734db3161777` | BLUECROSS BLUESHIELD OF TENNESSEE, INC. | 1 | [21](per_fpi/bluecross_blueshield_of_tennessee_inc.md) | medicare_advantage |
| `1a33c798-a7df-56d7-a4c4-b1e6ee93e751` | DEVOTED HEALTH PLAN OF PENNSYLVANIA INC | 1 | [20](per_fpi/devoted_health_plan_of_pennsylvania_inc.md) | medicare_advantage |
| `254facaa-4ace-5db7-af42-85e91921c307` | AETNA HEALTH INC. (NY) | 1 | [19](per_fpi/aetna_health_inc_ny.md) | medicare_advantage |
| `61e938dc-9301-5ec9-8501-27f8f105bac9` | FLORIDA BLUE MEDICARE, INC. | 1 | [19](per_fpi/florida_blue_medicare_inc.md) | medicare_advantage |
| `e9895113-428b-54c4-9c55-f6593b0c8e0f` | HUMANA INSURANCE COMPANY OF NEW YORK | 1 | [19](per_fpi/humana_insurance_company_of_new_york.md) | medicare_advantage |
| `8d8cd330-9584-58cc-92ab-644761c06855` | KAISER FOUNDATION HEALTH PLAN OF WASHINGTON | 1 | [19](per_fpi/kaiser_foundation_health_plan_of_washington.md) | medicare_advantage |
| `c9ebf1a2-de89-50c2-b3ec-870f07112c8d` | MEDICA INSURANCE COMPANY | 1 | [19](per_fpi/medica_insurance_company.md) | medicare_advantage |
| `25e1871f-1b76-51cc-a083-02543e08130f` | SELECTHEALTH, INC. | 1 | [19](per_fpi/selecthealth_inc.md) | medicare_advantage |
| `a1571955-9c15-53d7-9d57-6650a719e32f` | COMPCARE HEALTH SERVICES INSURANCE CORPORATION | 1 | [18](per_fpi/compcare_health_services_insurance_corporation.md) | medicare_advantage |
| `9434452e-b4ea-5ccb-9df6-1e5b4af7fae4` | FENYX HEALTH INSURANCE COMPANY | 1 | [18](per_fpi/fenyx_health_insurance_company.md) | medicare_advantage |
| `698a7bd1-d175-50e2-b4f8-8545815ff004` | HEALTHIER NEW JERSEY INSURANCE COMPANY | 1 | [18](per_fpi/healthier_new_jersey_insurance_company.md) | medicare_advantage |
| `cb9b375f-85c1-57f2-86f6-5c6668cdb6d8` | MG INSURANCE COMPANY | 1 | [18](per_fpi/mg_insurance_company.md) | medicare_advantage |
| `44d60086-fc07-5d51-a36e-16aee6a23975` | HEALTHSPRING OF FLORIDA, INC. | 1 | [17](per_fpi/healthspring_of_florida_inc.md) | medicare_advantage |
| `c002c086-1624-5801-98ef-29f54b381268` | WELLCARE OF TEXAS, INC. | 1 | [17](per_fpi/wellcare_of_texas_inc.md) | medicare_advantage |
| `3f2c6711-c405-5110-84e6-b322cdbe97a0` | AETNA BETTER HEALTH, INC. (LA) | 1 | [16](per_fpi/aetna_better_health_inc_la.md) | medicare_advantage |
| `2fa615f5-20ec-5683-8cf2-a18805b5160b` | DEVOTED HEALTH PLAN OF MISSOURI INC | 1 | [16](per_fpi/devoted_health_plan_of_missouri_inc.md) | medicare_advantage |
| `ef641e63-05a4-5240-a385-4630e394072b` | KS PLAN ADMINISTRATORS, LLC | 1 | [16](per_fpi/ks_plan_administrators_llc.md) | medicare_advantage |
| `ce16ef2a-a1d4-5d0c-99bb-724498416f85` | MOUNT CARMEL HEALTH PLAN, INC. | 1 | [16](per_fpi/mount_carmel_health_plan_inc.md) | medicare_advantage |
| `4e4196cb-9060-5a9c-a454-7b3aa817bd76` | QUARTZ HEALTH PLAN CORPORATION | 1 | [16](per_fpi/quartz_health_plan_corporation.md) | medicare_advantage |
| `f165f9aa-f454-53a3-8147-c3d265a481bc` | ULTIMATE HEALTH PLANS, INC. | 1 | [16](per_fpi/ultimate_health_plans_inc.md) | medicare_advantage |
| `c1b819fa-c9df-57c6-8128-498da1d9c2f4` | WELLPOINT TEXAS, INC. | 1 | [16](per_fpi/wellpoint_texas_inc.md) | medicare_advantage |
| `6c19728c-663a-5670-be98-9159991269c1` | AETNA HEALTH OF CALIFORNIA INC. | 1 | [15](per_fpi/aetna_health_of_california_inc.md) | medicare_advantage |
| `e0c26c3c-0620-5ceb-940e-1ca60bb9fc62` | CLOVER INSURANCE COMPANY | 1 | [15](per_fpi/clover_insurance_company.md) | medicare_advantage |
| `78d74282-7f45-56b1-aca4-4a677226d554` | DEVOTED HEALTH INSURANCE COMPANY OF INDIANA | 1 | [15](per_fpi/devoted_health_insurance_company_of_indiana.md) | medicare_advantage |
| `3bb55a39-a5c1-5e2b-9cd0-cc550ecebd15` | DEVOTED HEALTH PLAN OF ARIZONA, INC. | 1 | [15](per_fpi/devoted_health_plan_of_arizona_inc.md) | medicare_advantage |
| `46e73cb0-a030-514a-a368-3bd63e32a5f7` | OPTIMUM HEALTHCARE, INC. | 1 | [15](per_fpi/optimum_healthcare_inc.md) | medicare_advantage |
| `bc68830d-2628-5ef2-88dc-fb78698b60b6` | CAPITAL ADVANTAGE INSURANCE COMPANY | 1 | [14](per_fpi/capital_advantage_insurance_company.md) | medicare_advantage |
| `81ba6b78-0bd2-5f37-aeb5-e241e6b088d9` | ESSENCE HEALTHCARE, INC. | 1 | [14](per_fpi/essence_healthcare_inc.md) | medicare_advantage |
| `42d6d2b8-81e3-5663-b347-404792f6a5ed` | KEYSTONE HEALTH PLAN EAST, INC. | 1 | [14](per_fpi/keystone_health_plan_east_inc.md) | medicare_advantage |
| `87b1a68b-7388-50eb-ace9-e5bc93e58853` | PROMINENCE HEALTHFIRST OF TEXAS | 1 | [14](per_fpi/prominence_healthfirst_of_texas.md) | medicare_advantage |
| `4655fa59-e3ff-528e-9cff-67a5ede8bfe5` | SCOTT AND WHITE HEALTH PLAN | 1 | [14](per_fpi/scott_and_white_health_plan.md) | medicare_advantage |
| `4afe6536-df1c-526e-ab3d-3078535a4917` | DEVOTED HEALTH INSURANCE COMPANY OF ALABAMA INC | 1 | [13](per_fpi/devoted_health_insurance_company_of_alabama_inc.md) | medicare_advantage |
| `c2423511-7df0-52e2-b976-d5f68d1a734c` | DEVOTED HEALTH INSURANCE COMPANY OF TENNESSEE INC | 1 | [13](per_fpi/devoted_health_insurance_company_of_tennessee_inc.md) | medicare_advantage |
| `247afaad-1689-5305-8225-3cffeca4cb6e` | HEALTHSUN HEALTH PLANS, INC. | 1 | [13](per_fpi/healthsun_health_plans_inc.md) | medicare_advantage |
| `cdbeb799-aab0-5875-8377-4f926d8e4564` | PROMINENCE HEALTHFIRST | 1 | [13](per_fpi/prominence_healthfirst.md) | medicare_advantage |
| `8d72f9f6-b44e-5b9b-9f8c-b87df42c9d4e` | PROVIDENCE HEALTH ASSURANCE | 1 | [13](per_fpi/providence_health_assurance.md) | medicare_advantage |
| `bdec929d-ceec-52b8-aeb9-abf9762f5f9c` | VERMONT BLUE ADVANTAGE, INC. | 1 | [13](per_fpi/vermont_blue_advantage_inc.md) | medicare_advantage |
| `6efca3f5-3a86-5dce-8fc0-20fac4e81158` | AETNA HEALTH OF MICHIGAN INC. | 1 | [12](per_fpi/aetna_health_of_michigan_inc.md) | medicare_advantage |
| `6ec2d199-297f-5dd2-aec2-0a753eb8bbc7` | BLUE CROSS AND BLUE SHIELD OF ALABAMA | 1 | [12](per_fpi/blue_cross_and_blue_shield_of_alabama.md) | medicare_advantage |
| `881a13e6-e901-5925-ba25-9e9d13add5f8` | BLUE CROSS BLUE SHIELD HEALTHCARE PLAN OF GEORGIA | 1 | [12](per_fpi/blue_cross_blue_shield_healthcare_plan_of_georgia.md) | medicare_advantage |
| `2f6e8cd8-201f-574a-93c2-bcac9d031fcd` | CENTRAL HEALTH PLAN OF CALIFORNIA, INC. | 1 | [12](per_fpi/central_health_plan_of_california_inc.md) | medicare_advantage |
| `5ca8c6c2-3829-58c8-bfd5-4791698dc271` | HEALTH NET OF ARIZONA, INC. | 1 | [12](per_fpi/health_net_of_arizona_inc.md) | medicare_advantage |
| `1592c710-32ca-5ad1-865c-0a7ec95d0929` | HEALTH NET OF CALIFORNIA, INC. | 1 | [12](per_fpi/health_net_of_california_inc.md) | medicare_advantage |
| `1151cbab-23c4-5f8f-9767-e69c7d375f27` | HUMANA INSURANCE OF PUERTO RICO, INC. | 1 | [12](per_fpi/humana_insurance_of_puerto_rico_inc.md) | medicare_advantage |
| `1a67e9f0-ac60-5d46-9e26-fd6513140a33` | KAISER FOUNDATION HP OF GA, INC. | 1 | [12](per_fpi/kaiser_foundation_hp_of_ga_inc.md) | medicare_advantage |
| `b174584d-69ec-50ab-b681-2573843b47dc` | OPTUM INSURANCE OF OHIO, INC. | 1 | [12](per_fpi/optum_insurance_of_ohio_inc.md) | medicare_advantage |
| `27f83aa5-14a8-50c5-bbc6-2140c39905be` | ALIGNMENT HEALTH INSURANCE COMPANY OF ARIZONA INC | 1 | [11](per_fpi/alignment_health_insurance_company_of_arizona_inc.md) | medicare_advantage |
| `0286aa80-272b-576c-a884-9e323eabc016` | ALLINA HEALTH AND AETNA INSURANCE COMPANY | 1 | [11](per_fpi/allina_health_and_aetna_insurance_company.md) | medicare_advantage |
| `5e3e074f-543d-55b9-981c-e1b90788830d` | DEVOTED HEALTH INSURANCE COMPANY OF GEORGIA INC | 1 | [11](per_fpi/devoted_health_insurance_company_of_georgia_inc.md) | medicare_advantage |
| `0fef8ca0-1ae4-5c18-9c3b-6ca1f0069b79` | ESSENCE HEALTHCARE PPO, INC. | 1 | [11](per_fpi/essence_healthcare_ppo_inc.md) | medicare_advantage |
| `8a2b0108-a05a-57a6-b055-967c799fcda2` | GEISINGER HEALTH PLAN | 1 | [11](per_fpi/geisinger_health_plan.md) | medicare_advantage |
| `e7b17873-5b98-5ded-b1fd-7e8514371b94` | HEALTH FIRST HEALTH PLANS | 1 | [11](per_fpi/health_first_health_plans.md) | medicare_advantage |
| `0606f1aa-ca84-5a54-bf1b-e9d5c08dca9a` | HEALTHSPRING HEALTHCARE OF COLORADO, INC. | 1 | [11](per_fpi/healthspring_healthcare_of_colorado_inc.md) | medicare_advantage |
| `94a40cd9-7d79-5151-aa9d-cd80d6cf2cff` | HIGHMARK SENIOR SOLUTIONS COMPANY | 1 | [11](per_fpi/highmark_senior_solutions_company.md) | medicare_advantage |
| `73f59c79-a1a6-5339-9720-e0c4981b0884` | HUMANA EMPLOYERS HEALTH PLAN OF GEORGIA, INC. | 1 | [11](per_fpi/humana_employers_health_plan_of_georgia_inc.md) | medicare_advantage |
| `94d436ea-3a9e-53fb-94a8-62549de3568a` | PRESBYTERIAN HEALTH PLAN | 1 | [11](per_fpi/presbyterian_health_plan.md) | medicare_advantage |
| `0d68c7e6-4a83-58e2-8021-e6027f526622` | SUMMACARE INC. | 1 | [11](per_fpi/summacare_inc.md) | medicare_advantage |
| `6d08d844-3004-5c0c-97e4-3b69fc15ba7c` | UPMC HEALTH NETWORK, INC. | 1 | [11](per_fpi/upmc_health_network_inc.md) | medicare_advantage |
| `109331b1-f479-5426-a28d-0abb561551dc` | WELLMARK ADVANTAGE HEALTH PLAN, INC. | 1 | [11](per_fpi/wellmark_advantage_health_plan_inc.md) | medicare_advantage |
| `11bc9f14-6b58-5f56-9f65-fd80c8b21d92` | AETNA BETTER HEALTH OF CALIFORNIA INC. | 1 | [10](per_fpi/aetna_better_health_of_california_inc.md) | medicare_advantage |
| `98db7c7a-69f6-5afa-bc4a-300ff25d0901` | AETNA HEALTH INC. (CT) | 1 | [10](per_fpi/aetna_health_inc_ct.md) | medicare_advantage |
| `63318594-05ad-5f06-b8b1-d70a16f16321` | ALIGNMENT HEALTH PLAN OF ARIZONA, INC. | 1 | [10](per_fpi/alignment_health_plan_of_arizona_inc.md) | medicare_advantage |
| `fe1919e3-a51f-59a4-9037-6019e65286a3` | ALIGNMENT HEALTH PLAN OF NEVADA, INC. | 1 | [10](per_fpi/alignment_health_plan_of_nevada_inc.md) | medicare_advantage |
| `ce7fd07d-860a-55bb-b34c-d528c80e6707` | AULTCARE HEALTH INSURING CORPORATION | 1 | [10](per_fpi/aultcare_health_insuring_corporation.md) | medicare_advantage |
| `a212f6e9-6d55-5fcf-a4b9-f4d1d5d482f4` | CAREPARTNERS OF CONNECTICUT, INC. | 1 | [10](per_fpi/carepartners_of_connecticut_inc.md) | medicare_advantage |
| `ea4455af-35df-5c1d-aeb5-7fda4f188fa2` | COVENTRY HEALTH CARE OF KANSAS, INC. | 1 | [10](per_fpi/coventry_health_care_of_kansas_inc.md) | medicare_advantage |
| `dc49966c-ef33-5a5a-9faa-c938be4c3238` | DEVOTED HEALTH PLAN OF VIRGINIA INC | 1 | [10](per_fpi/devoted_health_plan_of_virginia_inc.md) | medicare_advantage |
| `03b95fb8-1315-5f8c-a475-113b0875fd27` | Devoted of Illinois, Inc. | 1 | [10](per_fpi/devoted_of_illinois_inc.md) | medicare_advantage |
| `881f267e-e9cd-5597-960e-ecd0444c5630` | GRANITE ALLIANCE INSURANCE COMPANY | 1 | [10](per_fpi/granite_alliance_insurance_company.md) | medicare_advantage |
| `5a4dcb3c-04ec-5ad0-9773-e6be51a50603` | HEALTH ALLIANCE PLAN OF MICHIGAN | 1 | [10](per_fpi/health_alliance_plan_of_michigan.md) | medicare_advantage |
| `9b799d4a-869b-5fa5-b42f-2ff73a7b36ca` | HUMANA MEDICAL PLAN OF MICHIGAN, INC. | 1 | [10](per_fpi/humana_medical_plan_of_michigan_inc.md) | medicare_advantage |
| `f187e85f-1af9-5190-b871-b291551c807c` | INDEPENDENT HEALTH ASSOCIATION, INC. | 1 | [10](per_fpi/independent_health_association_inc.md) | medicare_advantage |
| `f42000f1-914e-5652-991a-4f07929afafc` | SCAN DESERT HEALTH PLAN, INC. | 1 | [10](per_fpi/scan_desert_health_plan_inc.md) | medicare_advantage |
| `bf78fc62-ca28-5791-8e8b-17a49a63bae6` | UPMC HEALTH PLAN, INC. | 1 | [10](per_fpi/upmc_health_plan_inc.md) | medicare_advantage |
| `5a10dc93-6396-5e2a-bee6-2a62489bf4ca` | VIVA HEALTH, INC. | 1 | [10](per_fpi/viva_health_inc.md) | medicare_advantage |
| `398330a4-57c3-5fac-a74a-e543db856de2` | BRAVO HEALTH MID-ATLANTIC, INC. | 1 | [9](per_fpi/bravo_health_mid_atlantic_inc.md) | medicare_advantage |
| `403ccf65-b4d8-57fe-9d12-ffdb2f7cf518` | COVENTRY HEALTH CARE OF NEBRASKA, INC. | 1 | [9](per_fpi/coventry_health_care_of_nebraska_inc.md) | medicare_advantage |
| `acd45b79-a4a6-5687-a462-d248686829f4` | DEVOTED HEALTH INSURANCE COMPANY OF LOUISIANA | 1 | [9](per_fpi/devoted_health_insurance_company_of_louisiana.md) | medicare_advantage |
| `626f8c14-47a2-591b-961d-de51a0256ac9` | DEVOTED HEALTH PLAN OF COLORADO INC | 1 | [9](per_fpi/devoted_health_plan_of_colorado_inc.md) | medicare_advantage |
| `fbec3978-71ec-59a3-9d22-e284132f39af` | DEVOTED HEALTH PLAN OF TENNESSEE INC | 1 | [9](per_fpi/devoted_health_plan_of_tennessee_inc.md) | medicare_advantage |
| `5233cc6f-4f6c-51c0-9481-e62ddee6d401` | DOCTORS HEALTHCARE PLANS, INC. | 1 | [9](per_fpi/doctors_healthcare_plans_inc.md) | medicare_advantage |
| `f648bc8f-895a-5e66-84e2-363fc7c98bfa` | HMO LOUISIANA, INC. | 1 | [9](per_fpi/hmo_louisiana_inc.md) | medicare_advantage |
| `d16a22b6-80af-508f-9da5-9037a30e3b42` | HUMANA HEALTH COMPANY OF NEW YORK, INC. | 1 | [9](per_fpi/humana_health_company_of_new_york_inc.md) | medicare_advantage |
| `63f74d5f-3843-5f30-abe5-b6fa9d6a63d9` | KAISER PERMANENTE INSURANCE COMPANY | 1 | [9](per_fpi/kaiser_permanente_insurance_company.md) | medicare_advantage |
| `eceb3c3d-2b0f-578a-a552-1f2aca24ade7` | MEDICAL ASSOCIATES HEALTH PLAN, INC. | 1 | [9](per_fpi/medical_associates_health_plan_inc.md) | medicare_advantage |
| `9687d61e-f42f-51a0-93d4-35a4031ce7e5` | WELLPOINT TENNESSEE, INC. | 1 | [9](per_fpi/wellpoint_tennessee_inc.md) | medicare_advantage |
| `44681ced-513f-5281-9d49-b06e6b34a068` | AETNA HEALTH INC. (NJ) | 1 | [8](per_fpi/aetna_health_inc_nj.md) | medicare_advantage |
| `6c972693-b7ac-5b21-b51e-00cd4c2d4f8f` | Baylor Scott & White Insurance Company | 1 | [8](per_fpi/baylor_scott_white_insurance_company.md) | medicare_advantage |
| `7dd27196-0998-5e5c-8ecb-ed0c6f55b0a1` | CAPITAL HEALTH PLAN | 1 | [8](per_fpi/capital_health_plan.md) | medicare_advantage |
| `f5c12ef2-dc1d-5c95-8da5-7cd98666094b` | CHRISTUS HEALTH PLAN | 1 | [8](per_fpi/christus_health_plan.md) | medicare_advantage |
| `49983cba-58ba-5818-84c8-a627900d48f0` | DEVOTED HEALTH INSURANCE COMPANY OF ARKANSAS INC | 1 | [8](per_fpi/devoted_health_insurance_company_of_arkansas_inc.md) | medicare_advantage |
| `da1e0b80-94de-58fb-8df2-0ef0c3576281` | DEVOTED HEALTH INSURANCE COMPANY OF MISSISSIPPI | 1 | [8](per_fpi/devoted_health_insurance_company_of_mississippi.md) | medicare_advantage |
| `68f5c7e3-c22e-566f-8211-04f2a0cdee59` | DEVOTED HEALTH INSURANCE COMPANY OF OKLAHOMA | 1 | [8](per_fpi/devoted_health_insurance_company_of_oklahoma.md) | medicare_advantage |
| `66e289de-d4a4-5f34-8aa9-e03731f6aacf` | GLOBALHEALTH, INC. | 1 | [8](per_fpi/globalhealth_inc.md) | medicare_advantage |
| `7dc2f1dd-ddc9-5942-9e4a-0f9138f99c40` | HAWAII MEDICAL SERVICE ASSOCIATION | 1 | [8](per_fpi/hawaii_medical_service_association.md) | medicare_advantage |
| `7d30c4fa-0c7a-5bad-be11-d9373ee24619` | HEALTH PARTNERS PLANS, INC. | 1 | [8](per_fpi/health_partners_plans_inc.md) | medicare_advantage |
| `66582bf2-5e52-5584-ba8a-6128c3768264` | HOMETOWN HEALTH PLAN, INC. | 1 | [8](per_fpi/hometown_health_plan_inc.md) | medicare_advantage |
| `04ad0007-1a45-54bd-8bcf-5b2400ac4cb9` | KEYSTONE HEALTH PLAN CENTRAL, INC. | 1 | [8](per_fpi/keystone_health_plan_central_inc.md) | medicare_advantage |
| `fe57bd40-9242-5962-af53-529bd70a883d` | MOUNT CARMEL HEALTH PLAN OF IDAHO, INC. | 1 | [8](per_fpi/mount_carmel_health_plan_of_idaho_inc.md) | medicare_advantage |
| `4864ef82-b5ea-5bf9-a413-7752bcb6fe8e` | NEXTBLUE OF NORTH DAKOTA INSURANCE COMPANY | 1 | [8](per_fpi/nextblue_of_north_dakota_insurance_company.md) | medicare_advantage |
| `8c80369d-f1f8-52ae-9b2c-e0bc6c4eb938` | SCAN HEALTH PLAN (NM) | 1 | [8](per_fpi/scan_health_plan_nm.md) | medicare_advantage |
| `699ff1d7-c8bf-54db-acbd-fe608acc0604` | SCAN HEALTH PLAN NEVADA, INC. | 1 | [8](per_fpi/scan_health_plan_nevada_inc.md) | medicare_advantage |
| `1b744087-dc26-50bf-b593-cd4cbf7914c4` | SCAN HEALTH PLAN TEXAS, INC. | 1 | [8](per_fpi/scan_health_plan_texas_inc.md) | medicare_advantage |
| `35f70f0d-fff1-5683-8329-288cee159b9b` | THE HEALTH PLAN OF WEST VIRGINIA, INC. | 1 | [8](per_fpi/the_health_plan_of_west_virginia_inc.md) | medicare_advantage |
| `0c757d3c-3f79-5038-80b6-179409756b1d` | AETNA HEALTH INC. (ME) | 1 | [7](per_fpi/aetna_health_inc_me.md) | medicare_advantage |
| `dc97aa3c-b6ed-57cd-b67d-a7ced3fb4b25` | ALLIANCE HEALTH AND LIFE INSURANCE COMPANY | 1 | [7](per_fpi/alliance_health_and_life_insurance_company.md) | medicare_advantage |
| `e8af7381-fdae-5781-b158-48587617ace4` | ASTIVA HEALTH, INC. | 1 | [7](per_fpi/astiva_health_inc.md) | medicare_advantage |
| `a1ae6152-0213-5280-9799-197e9cb9ac60` | Avalon Insurance Company | 1 | [7](per_fpi/avalon_insurance_company.md) | medicare_advantage |
| `d470438a-a2ee-59ab-9071-834af7ffda85` | BCBS OF ALABAMA & UTIC INSURANCE COMPANY | 1 | [7](per_fpi/bcbs_of_alabama_utic_insurance_company.md) | medicare_advantage |
| `e3bef9aa-0e1b-5294-b489-27b385e4e26e` | BLUE CARE NETWORK OF MICHIGAN | 1 | [7](per_fpi/blue_care_network_of_michigan.md) | medicare_advantage |
| `bf8f1e72-58f8-56a4-888d-1a59545b069d` | BLUECROSS BLUESHIELD KANSAS SOLUTIONS, INC. | 1 | [7](per_fpi/bluecross_blueshield_kansas_solutions_inc.md) | medicare_advantage |
| `e5e05ab3-7a58-562a-954a-2488d907342e` | CAPITAL DISTRICT PHYSICIANS' HEALTH PLAN, INC. | 1 | [7](per_fpi/capital_district_physicians_health_plan_inc.md) | medicare_advantage |
| `b76127f6-51ef-5520-84af-57c249fdf1dc` | CHAMPION HEALTH PLAN OF CALIFORNIA INC | 1 | [7](per_fpi/champion_health_plan_of_california_inc.md) | medicare_advantage |
| `45b83526-1da0-5f5d-8b04-feaec9ec3a28` | CHAMPION HEALTH PLAN OF NEVADA, INC. | 1 | [7](per_fpi/champion_health_plan_of_nevada_inc.md) | medicare_advantage |
| `31992aa8-af00-5658-966a-177a1472e8c2` | COMMUNITYCARE GOVERNMENT PROGRAMS, INC. | 1 | [7](per_fpi/communitycare_government_programs_inc.md) | medicare_advantage |
| `cd908614-d9bf-5228-aa04-b6da9917f936` | DEVOTED HEALTH INSURANCE COMPANY OF HAWAII INC | 1 | [7](per_fpi/devoted_health_insurance_company_of_hawaii_inc.md) | medicare_advantage |
| `3df92505-613b-554c-bc5b-5625cfd2cc56` | DEVOTED HEALTH INSURANCE COMPANY OF KANSAS | 1 | [7](per_fpi/devoted_health_insurance_company_of_kansas.md) | medicare_advantage |
| `e4618178-3ebe-5b71-8b8f-ba91060cf9c6` | DEVOTED HEALTH PLAN OF NEW MEXICO, INC. | 1 | [7](per_fpi/devoted_health_plan_of_new_mexico_inc.md) | medicare_advantage |
| `6eb4e6e5-0cb0-5be8-9c63-009824d8abea` | HUMANA MEDICAL PLAN OF UTAH, INC. | 1 | [7](per_fpi/humana_medical_plan_of_utah_inc.md) | medicare_advantage |
| `90639341-fa2e-5bff-95b9-ab9b68608d22` | MOUNT CARMEL HEALTH INSURANCE COMPANY | 1 | [7](per_fpi/mount_carmel_health_insurance_company.md) | medicare_advantage |
| `b77a540b-f4c4-5ea5-9a91-0f8f4fd0562c` | REGENCE BLUECROSS BLUESHIELD OF UTAH | 1 | [7](per_fpi/regence_bluecross_blueshield_of_utah.md) | medicare_advantage |
| `82f2775d-a3c1-55a6-b4bd-d1a137933262` | SHARP HEALTH PLAN | 1 | [7](per_fpi/sharp_health_plan.md) | medicare_advantage |
| `3c5929e2-d372-5ca3-8e03-d11711816425` | WELLCARE HEALTH INSURANCE OF CONNECTICUT, INC. | 1 | [7](per_fpi/wellcare_health_insurance_of_connecticut_inc.md) | medicare_advantage |
| `f427aab1-64d8-520c-b982-4f983675f0a6` | WELLPOINT HEALTH PLANS, INC. | 1 | [7](per_fpi/wellpoint_health_plans_inc.md) | medicare_advantage |
| `9d157022-7eb8-5a48-845c-16cba299be60` | WELLPOINT INSURANCE COMPANY | 1 | [7](per_fpi/wellpoint_insurance_company.md) | medicare_advantage |
| `b1db4583-cbc8-59d7-ba93-d3294ed80ba2` | ALTERWOOD ADVANTAGE, INC. | 1 | [6](per_fpi/alterwood_advantage_inc.md) | medicare_advantage |
| `ae722784-bbbc-592f-8849-04c7dfc70e44` | ARKANSAS HEALTH & WELLNESS HEALTH PLAN, INC. | 1 | [6](per_fpi/arkansas_health_wellness_health_plan_inc.md) | medicare_advantage |
| `1bd01dff-8406-5cdd-b48f-a1db236b78e3` | BLUE CROSS BLUE SHIELD ASSOCIATION | 1 | [6](per_fpi/blue_cross_blue_shield_association.md) | medicare_advantage |
| `a59b79c6-dae8-5792-941b-4948baafa0e2` | CONNECTICARE, INC. | 1 | [6](per_fpi/connecticare_inc.md) | medicare_advantage |
| `4e50d9b5-b289-5ca9-8560-d62a1dc8c1e3` | COVENTRY HEALTH CARE OF WEST VIRGINIA, INC. | 1 | [6](per_fpi/coventry_health_care_of_west_virginia_inc.md) | medicare_advantage |
| `118ccf73-69a4-5c6c-9e26-1d7f9285af6c` | DEAN HEALTH INSURANCE, INC. | 1 | [6](per_fpi/dean_health_insurance_inc.md) | medicare_advantage |
| `9fb82109-bf6e-5a6d-af57-6ba1435e7b85` | DEVOTED HEALTH INSURANCE COMPANY OF KENTUCKY INC | 1 | [6](per_fpi/devoted_health_insurance_company_of_kentucky_inc.md) | medicare_advantage |
| `a66fa3e7-48b4-5849-9283-e2409f3ad9b6` | DEVOTED HEALTH INSURANCE COMPANY OF NEBRASKA | 1 | [6](per_fpi/devoted_health_insurance_company_of_nebraska.md) | medicare_advantage |
| `aed49611-dc38-5a87-938a-afbea0f1a57e` | DEVOTED HEALTH INSURANCE COMPANY OF PENNSYLVANIA INC | 1 | [6](per_fpi/devoted_health_insurance_company_of_pennsylvania_inc.md) | medicare_advantage |
| `57ea794b-dd03-55ee-9bb5-b275b25034e4` | DEVOTED HEALTH INSURANCE COMPANY OF SOUTH CAROLINA INC | 1 | [6](per_fpi/devoted_health_insurance_company_of_south_carolina_inc.md) | medicare_advantage |
| `4810a8d7-7c44-5f44-8d81-5b72e3e5cb0f` | DEVOTED HEALTH PLAN OF ALABAMA INC | 1 | [6](per_fpi/devoted_health_plan_of_alabama_inc.md) | medicare_advantage |
| `19709589-580f-56c1-9b90-037c19739bf3` | DEVOTED HEALTH PLAN OF OREGON INC | 1 | [6](per_fpi/devoted_health_plan_of_oregon_inc.md) | medicare_advantage |
| `1674cef3-2d36-5c86-8e0e-cc50572a3d99` | ELDERPLAN, INC. | 1 | [6](per_fpi/elderplan_inc.md) | medicare_advantage |
| `a1f6e992-a7ff-5909-9f1d-36c4f6535a13` | GOLD KIDNEY OF FLORIDA INC | 1 | [6](per_fpi/gold_kidney_of_florida_inc.md) | medicare_advantage |
| `80c8f59d-a2d0-547e-96b2-2723fa922c5a` | Group Retiree Health Solutions, Inc. | 1 | [6](per_fpi/group_retiree_health_solutions_inc.md) | medicare_advantage |
| `5e28bbd9-6e5c-584f-ac41-f0bfff9dc645` | HM HEALTH INSURANCE COMPANY | 1 | [6](per_fpi/hm_health_insurance_company.md) | medicare_advantage |
| `1b981948-369d-5aed-8b77-67ae7b244a65` | KAISER FOUNDATION HP OF THE N W | 1 | [6](per_fpi/kaiser_foundation_hp_of_the_n_w.md) | medicare_advantage |
| `88cd33f5-0037-569d-b1c3-24a223d03606` | LOUISIANA HEALTH SERVICE & INDEMNITY COMPANY | 1 | [6](per_fpi/louisiana_health_service_indemnity_company.md) | medicare_advantage |
| `231fb284-233b-5545-8567-e1675317cf27` | MATTHEW THORNTON HEALTH PLAN, INC. | 1 | [6](per_fpi/matthew_thornton_health_plan_inc.md) | medicare_advantage |
| `d72ce542-a0ea-551d-a868-ac147d91b77f` | MEMORIAL HERMANN HEALTH PLAN | 1 | [6](per_fpi/memorial_hermann_health_plan.md) | medicare_advantage |
| `30d54fcd-ff52-57ea-b99b-029f4b725c94` | PARAMOUNT CARE, INC. | 1 | [6](per_fpi/paramount_care_inc.md) | medicare_advantage |
| `05bcacad-2ad9-5794-8b41-7948cb04e603` | PERENNIAL ADVANTAGE OF COLORADO, INC. | 1 | [6](per_fpi/perennial_advantage_of_colorado_inc.md) | medicare_advantage |
| `7f300332-8c25-5918-81f4-44b5e3ceb197` | Preferred Care Network, Inc. | 1 | [6](per_fpi/preferred_care_network_inc.md) | medicare_advantage |
| `85f7671c-33d9-5418-b9a3-2dd5624f7271` | SECURITY HEALTH PLAN OF WISCONSIN, INC. | 1 | [6](per_fpi/security_health_plan_of_wisconsin_inc.md) | medicare_advantage |
| `c585e109-ef30-53a4-be95-23aff9db29f4` | WELLCARE HEALTH PLANS OF NEW JERSEY, INC. | 1 | [6](per_fpi/wellcare_health_plans_of_new_jersey_inc.md) | medicare_advantage |
| `708f3c62-0e66-590a-bb5c-83c94a7277d9` | ASPIRE HEALTH PLAN | 1 | [5](per_fpi/aspire_health_plan.md) | medicare_advantage |
| `b69b1866-28a2-5981-afb3-38e7c81a3cbd` | CHINESE COMMUNITY HEALTH PLAN | 1 | [5](per_fpi/chinese_community_health_plan.md) | medicare_advantage |
| `705181d6-4b10-5932-ad0c-b5ed6bfcda57` | COORDINATED CARE OF WASHINGTON, INC. | 1 | [5](per_fpi/coordinated_care_of_washington_inc.md) | medicare_advantage |
| `74fd82a4-e0f7-588e-8fde-a1bf63d4fb5c` | DEVOTED HEALTH INSURANCE COMPANY OF ARIZONA, INC. | 1 | [5](per_fpi/devoted_health_insurance_company_of_arizona_inc.md) | medicare_advantage |
| `3671e72a-6ebe-5f33-af79-f1c822f2c0e2` | DEVOTED HEALTH INSURANCE COMPANY OF COLORADO INC | 1 | [5](per_fpi/devoted_health_insurance_company_of_colorado_inc.md) | medicare_advantage |
| `3e758bc9-6dec-5be8-b4a1-7147b5ebab41` | DEVOTED HEALTH INSURANCE COMPANY OF UTAH, INC. | 1 | [5](per_fpi/devoted_health_insurance_company_of_utah_inc.md) | medicare_advantage |
| `f612e97f-3660-57b3-8374-f6f1ab719b72` | DEVOTED HEALTH PLAN OF HAWAII, INC. | 1 | [5](per_fpi/devoted_health_plan_of_hawaii_inc.md) | medicare_advantage |
| `20189e69-f93e-5c0c-9648-c2f2526e5154` | GOLD KIDNEY OF ARIZONA | 1 | [5](per_fpi/gold_kidney_of_arizona.md) | medicare_advantage |
| `cd7ffc9f-2043-504e-a83e-731c3c7b3b29` | HEALTH NET LIFE INSURANCE COMPANY | 1 | [5](per_fpi/health_net_life_insurance_company.md) | medicare_advantage |
| `fa324734-aa63-5cd1-984d-0a592f8e9244` | HORIZON INSURANCE COMPANY | 1 | [5](per_fpi/horizon_insurance_company.md) | medicare_advantage |
| `b2b4a6a4-1432-5f47-a566-99e5d7b5e336` | MOUNT CARMEL HEALTH PLAN OF NEW YORK, INC. | 1 | [5](per_fpi/mount_carmel_health_plan_of_new_york_inc.md) | medicare_advantage |
| `650277c4-57de-5db0-b8b5-47d11aea1f72` | OXFORD HEALTH PLANS (NJ), INC. | 1 | [5](per_fpi/oxford_health_plans_nj_inc.md) | medicare_advantage |
| `8301d0ec-de53-5a41-a140-32019352714d` | PENNSYLVANIA HEALTH & WELLNESS, INC. | 1 | [5](per_fpi/pennsylvania_health_wellness_inc.md) | medicare_advantage |
| `02e3888e-7e11-59db-8125-123684928490` | PROMINENCE HEALTHFIRST OF FLORIDA INC | 1 | [5](per_fpi/prominence_healthfirst_of_florida_inc.md) | medicare_advantage |
| `91465cdf-74b6-5090-8697-3aa0975ade02` | QUARTZ HEALTH PLAN MN CORPORATION | 1 | [5](per_fpi/quartz_health_plan_mn_corporation.md) | medicare_advantage |
| `a28de7d6-2bc4-5afd-99f4-bfd93c3cd75f` | REGENCE BLUESHIELD OF IDAHO, INC. | 1 | [5](per_fpi/regence_blueshield_of_idaho_inc.md) | medicare_advantage |
| `4ba9c959-3080-5b52-9e35-79a70b327000` | TRINITY HEALTH PLAN OF MICHIGAN INC | 1 | [5](per_fpi/trinity_health_plan_of_michigan_inc.md) | medicare_advantage |
| `29975961-9181-5919-91c9-35455cfca15e` | AETNA HEALTH OF UTAH INC. | 1 | [4](per_fpi/aetna_health_of_utah_inc.md) | medicare_advantage |
| `4de59954-0db3-594c-bd61-46dcb4baa588` | AMH HEALTH, LLC | 1 | [4](per_fpi/amh_health_llc.md) | medicare_advantage |
| `972dc706-f382-54db-9575-e59b99e7a163` | ANTHEM INSURANCE CO. & BCBSMA & BCBSRI & BCBSVT | 1 | [4](per_fpi/anthem_insurance_co_bcbsma_bcbsri_bcbsvt.md) | medicare_advantage |
| `09b436c4-ccd4-5cfd-ba5d-b52328b06509` | BLUE CROSS AND BLUE SHIELD OF KANSAS | 1 | [4](per_fpi/blue_cross_and_blue_shield_of_kansas.md) | medicare_advantage |
| `9472dac0-a1b9-5f40-a0dc-42047d73468e` | BOSTON MEDICAL CENTER HEALTH PLAN, INC. | 1 | [4](per_fpi/boston_medical_center_health_plan_inc.md) | medicare_advantage |
| `1cb31ab9-4d4a-59c3-878c-956936dfcd7b` | CENTRAL MASS HEALTH, LLC | 1 | [4](per_fpi/central_mass_health_llc.md) | medicare_advantage |
| `5ba48c13-b71a-5096-980b-bf763e847eab` | CLEVER CARE OF GOLDEN STATE, INC. | 1 | [4](per_fpi/clever_care_of_golden_state_inc.md) | medicare_advantage |
| `a504acc0-8289-56b3-bd5f-2609df7b3c62` | DEVOTED HEALTH INSURANCE COMPANY | 1 | [4](per_fpi/devoted_health_insurance_company.md) | medicare_advantage |
| `7486d04b-a322-51d7-a00f-949f823d3cd6` | DEVOTED HEALTH INSURANCE COMPANY OF WASHINGTON | 1 | [4](per_fpi/devoted_health_insurance_company_of_washington.md) | medicare_advantage |
| `ce05d53c-c22d-57fa-be66-1a06fc759846` | DEVOTED HEALTH PLAN OF ILLINOIS, INC. | 1 | [4](per_fpi/devoted_health_plan_of_illinois_inc.md) | medicare_advantage |
| `42fd0acb-154b-54da-b470-ab9783808d00` | EMBLEMHEALTH PLAN, INC. | 1 | [4](per_fpi/emblemhealth_plan_inc.md) | medicare_advantage |
| `951aa0c1-27a6-5e17-830d-902fbfbd7f10` | ETERNALHEALTH OF ARIZONA INC | 1 | [4](per_fpi/eternalhealth_of_arizona_inc.md) | medicare_advantage |
| `7a7d73d5-31c4-53c3-ba81-9887ffe03b3c` | EXCELLUS HEALTH PLAN COMMUNITY CARE LLC | 1 | [4](per_fpi/excellus_health_plan_community_care_llc.md) | medicare_advantage |
| `28b08ce1-49c4-5cb4-9bc1-b0307a7c5cd0` | GATEWAY HEALTH PLAN, INC. | 1 | [4](per_fpi/gateway_health_plan_inc.md) | medicare_advantage |
| `b37f8e4d-0e1a-57ee-bcf4-5b50cbd56234` | GEISINGER INDEMNITY INSURANCE COMPANY | 1 | [4](per_fpi/geisinger_indemnity_insurance_company.md) | medicare_advantage |
| `3f4119df-af3e-5305-b51e-3f4d80b603ea` | GHS HEALTH MAINTENANCE ORGANIZATION, INC. | 1 | [4](per_fpi/ghs_health_maintenance_organization_inc.md) | medicare_advantage |
| `7b88c479-1427-53d0-89ea-66e293006983` | GHS INSURANCE COMPANY | 1 | [4](per_fpi/ghs_insurance_company.md) | medicare_advantage |
| `59ce5f1b-785e-5167-bc59-e11e45cb0709` | HEALTHPARTNERS INSURANCE COMPANY | 1 | [4](per_fpi/healthpartners_insurance_company.md) | medicare_advantage |
| `6a3cf7dd-b7f2-5441-a18f-a895a61ef187` | HOME STATE HEALTH PLAN, INC. | 1 | [4](per_fpi/home_state_health_plan_inc.md) | medicare_advantage |
| `dddfbbf5-7b02-5206-80df-79b7bbb0efa9` | HUMANA HEALTH INSURANCE COMPANY OF FLORIDA, INC. | 1 | [4](per_fpi/humana_health_insurance_company_of_florida_inc.md) | medicare_advantage |
| `7c455315-7920-5f4f-8bc6-e9a81336da1c` | LEON HEALTH, INC. | 1 | [4](per_fpi/leon_health_inc.md) | medicare_advantage |
| `f201aa5f-b772-5a78-9e4c-8e3a0b62365c` | MEDICAL ASSOCIATES CLINIC HEALTH PLAN | 1 | [4](per_fpi/medical_associates_clinic_health_plan.md) | medicare_advantage |
| `5b1f62f0-889c-50d6-872a-73607a4f8fec` | MEDISUN, INC. | 1 | [4](per_fpi/medisun_inc.md) | medicare_advantage |
| `eac61809-0caf-5edf-8800-2d142b8aa0df` | MODA HEALTH PLAN, INC. | 1 | [4](per_fpi/moda_health_plan_inc.md) | medicare_advantage |
| `2065cdad-c2b1-5859-9440-50fee4894021` | MOLINA HEALTHCARE OF ARIZONA, INC. | 1 | [4](per_fpi/molina_healthcare_of_arizona_inc.md) | medicare_advantage |
| `c4ed9731-b5b6-5165-9374-bb09f3a7541e` | MOLINA HEALTHCARE OF UTAH, INC. | 1 | [4](per_fpi/molina_healthcare_of_utah_inc.md) | medicare_advantage |
| `48be33f4-f41a-5f18-baf6-d0f51967e420` | SENIORLIFE WASHINGTON, INC. | 1 | [4](per_fpi/seniorlife_washington_inc.md) | medicare_advantage |
| `33bad3a0-fade-51ee-9114-36e3f7325260` | THP INSURANCE COMPANY | 1 | [4](per_fpi/thp_insurance_company.md) | medicare_advantage |
| `a8579dcb-f845-5659-95c6-ba232d8c2a21` | TOTAL LONGTERM CARE, INC. | 1 | [4](per_fpi/total_longterm_care_inc.md) | medicare_advantage |
| `be9af402-5e21-5c11-a01d-47e3039dd6de` | VERDA HEALTH PLAN OF TEXAS INC | 1 | [4](per_fpi/verda_health_plan_of_texas_inc.md) | medicare_advantage |
| `af6583ee-72b2-517f-a389-cf6de5e12e01` | WELLCARE HEALTH INSURANCE COMPANY OF WASHINGTON | 1 | [4](per_fpi/wellcare_health_insurance_company_of_washington.md) | medicare_advantage |
| `34639693-e775-5546-b256-36e982341ba0` | WELLCARE HEALTH INSURANCE OF NORTH CAROLINA, INC. | 1 | [4](per_fpi/wellcare_health_insurance_of_north_carolina_inc.md) | medicare_advantage |
| `5b3906e3-9011-511d-8f28-38e1b6bd6e30` | WELLCARE OF CONNECTICUT, INC. | 1 | [4](per_fpi/wellcare_of_connecticut_inc.md) | medicare_advantage |
| `78c16684-8e8f-5992-8b70-32d5eca55b55` | WELLCARE OF IOWA, INC. | 1 | [4](per_fpi/wellcare_of_iowa_inc.md) | medicare_advantage |
| `be6cf6c7-1d3a-504e-a63e-6a1806e649a1` | WELLCARE OF MAINE, INC. | 1 | [4](per_fpi/wellcare_of_maine_inc.md) | medicare_advantage |
| `c890d713-7cc8-5de3-9043-84072ebd1f91` | WYOBLUE ADVANTAGE INC | 1 | [4](per_fpi/wyoblue_advantage_inc.md) | medicare_advantage |
| `d6799be6-ce1d-58d0-b114-8d4711e7d92d` | AETNA BETTER HEALTH OF OKLAHOMA INC. | 1 | [3](per_fpi/aetna_better_health_of_oklahoma_inc.md) | medicare_advantage |
| `3f9af4c3-d735-5c9b-9674-33cdd1864d6b` | AETNA BETTER HEALTH OF TEXAS INC. | 1 | [3](per_fpi/aetna_better_health_of_texas_inc.md) | medicare_advantage |
| `ae111e98-25f2-5085-b19c-1320fe0a76e0` | AETNA HEALTH INC. (LA) | 1 | [3](per_fpi/aetna_health_inc_la.md) | medicare_advantage |
| `e1a5fbff-a164-550c-bedd-ec99fe7d52ca` | ALIGN SENIOR CARE CALIFORNIA INC. | 1 | [3](per_fpi/align_senior_care_california_inc.md) | medicare_advantage |
| `9b30f550-5316-51a5-96ff-d93443eb530e` | AMERIHEALTH INSURANCE COMPANY OF NEW JERSEY | 1 | [3](per_fpi/amerihealth_insurance_company_of_new_jersey.md) | medicare_advantage |
| `9494bf46-99aa-5a88-a286-f7a4ffe06f65` | ANTHEM BLUE CROSS LIFE AND HEALTH INS COMPANY | 1 | [3](per_fpi/anthem_blue_cross_life_and_health_ins_company.md) | medicare_advantage |
| `4abe342b-e6ec-5c2f-bc08-adf270924bfb` | ASURIS NORTHWEST HEALTH | 1 | [3](per_fpi/asuris_northwest_health.md) | medicare_advantage |
| `d0ea6590-8a29-5493-809d-a8f486681769` | BAYCARE SELECT HEALTH PLANS, INC. | 1 | [3](per_fpi/baycare_select_health_plans_inc.md) | medicare_advantage |
| `ed07e152-e410-5841-ab3e-74d059589521` | CDPHP UNIVERSAL BENEFITS, INC. | 1 | [3](per_fpi/cdphp_universal_benefits_inc.md) | medicare_advantage |
| `dbf8df1a-9ff8-58cc-9b42-fe3ea67527ed` | CELTIC INSURANCE COMPANY | 1 | [3](per_fpi/celtic_insurance_company.md) | medicare_advantage |
| `a197bd29-d8b6-5f14-9e0d-df6d6d9a726e` | COMMUNITY CARE HEALTH PLAN OF LOUISIANA, INC. | 1 | [3](per_fpi/community_care_health_plan_of_louisiana_inc.md) | medicare_advantage |
| `45cdc41c-21c8-53c6-8e4b-a63fa271d3c8` | COX HEALTH SYSTEMS HMO INC | 1 | [3](per_fpi/cox_health_systems_hmo_inc.md) | medicare_advantage |
| `80b2acbb-a674-5a5d-97fd-e4006d9d2bd9` | DEVOTED HEALTH INSURANCE COMPANY OF DELAWARE | 1 | [3](per_fpi/devoted_health_insurance_company_of_delaware.md) | medicare_advantage |
| `bb77212c-f054-59b8-9670-1d6fde434569` | EL PASO FIRST HEALTH PLANS, INC. | 1 | [3](per_fpi/el_paso_first_health_plans_inc.md) | medicare_advantage |
| `cb97e0d0-70d0-53f7-aaf4-e49a84c1677a` | HEALTH NET COMMUNITY SOLUTIONS, INC. | 1 | [3](per_fpi/health_net_community_solutions_inc.md) | medicare_advantage |
| `e83de0ab-e8ff-555e-840f-17ca2f93280a` | HEALTH NET HEALTH PLAN OF OREGON, INC. | 1 | [3](per_fpi/health_net_health_plan_of_oregon_inc.md) | medicare_advantage |
| `d146bafe-15b5-5c0f-a052-178d2542a376` | HPMP OF FLORIDA, INC. | 1 | [3](per_fpi/hpmp_of_florida_inc.md) | medicare_advantage |
| `21840c71-6646-5780-b2ee-2b62d7921268` | HUMANA HEALTH PLAN OF OHIO, INC. | 1 | [3](per_fpi/humana_health_plan_of_ohio_inc.md) | medicare_advantage |
| `f8a84207-4ba2-58f6-9b36-755af38fa100` | HUMANA INSURANCE COMPANY OF KENTUCKY | 1 | [3](per_fpi/humana_insurance_company_of_kentucky.md) | medicare_advantage |
| `b16b145a-7c54-5902-9eed-0db82fc93f90` | IMPERIAL HEALTH PLAN OF CALIFORNIA, INC. | 1 | [3](per_fpi/imperial_health_plan_of_california_inc.md) | medicare_advantage |
| `f99a29ff-28d2-533d-949b-5428218bde66` | LIBERTY ADVANTAGE, LLC | 1 | [3](per_fpi/liberty_advantage_llc.md) | medicare_advantage |
| `bb6ab506-9965-5acc-8ea2-87c34c22bd7c` | MANAGED HEALTH SERVICES INSURANCE CORP. | 1 | [3](per_fpi/managed_health_services_insurance_corp.md) | medicare_advantage |
| `e3bda3d2-7f04-50e7-a6c1-9e2758ce184b` | MARQUIS ADVANTAGE, INC. | 1 | [3](per_fpi/marquis_advantage_inc.md) | medicare_advantage |
| `9cbc49dc-70c3-5372-a567-69802f26bab4` | MCLAREN HEALTH PLAN, INC. | 1 | [3](per_fpi/mclaren_health_plan_inc.md) | medicare_advantage |
| `c3599418-98c4-5b93-9903-3ecf808522f4` | MERCY CARE | 1 | [3](per_fpi/mercy_care.md) | medicare_advantage |
| `34c8e646-7300-5a67-be17-cf8e6a6bb790` | METROPLUS HEALTH PLAN, INC. | 1 | [3](per_fpi/metroplus_health_plan_inc.md) | medicare_advantage |
| `e77f21f9-e818-5c56-b3d0-c779f3b6fb6c` | MOLINA HEALTHCARE OF KENTUCKY, INC. | 1 | [3](per_fpi/molina_healthcare_of_kentucky_inc.md) | medicare_advantage |
| `0396f212-3a7d-50d9-9ba0-7853a19d4857` | MOLINA HEALTHCARE OF MICHIGAN, INC. | 1 | [3](per_fpi/molina_healthcare_of_michigan_inc.md) | medicare_advantage |
| `b7054fda-df11-586c-8928-b0bd96a6d3c0` | PARTNERS INSURANCE COMPANY INC | 1 | [3](per_fpi/partners_insurance_company_inc.md) | medicare_advantage |
| `2449aa32-5f49-5eaf-85ce-8bc4c1563756` | PATRIUS HEALTH, INC. | 1 | [3](per_fpi/patrius_health_inc.md) | medicare_advantage |
| `287ef078-4ee3-57e0-82a9-f4c7d1f3cc2e` | PERENNIAL ADVANTAGE OF OHIO, INC. | 1 | [3](per_fpi/perennial_advantage_of_ohio_inc.md) | medicare_advantage |
| `933049df-0b57-55aa-adde-8ba7b5523cbd` | PROCARE ADVANTAGE, LLC | 1 | [3](per_fpi/procare_advantage_llc.md) | medicare_advantage |
| `39f11426-9fa1-5735-b211-91a4d0c864cd` | PROVIDER PARTNERS HEALTH PLAN OF INDIANA | 1 | [3](per_fpi/provider_partners_health_plan_of_indiana.md) | medicare_advantage |
| `502f63fc-f893-5b6f-b2eb-8bde1548c63d` | PROVIDER PARTNERS HEALTH PLAN OF MISSOURI, INC. | 1 | [3](per_fpi/provider_partners_health_plan_of_missouri_inc.md) | medicare_advantage |
| `81c31a1d-b515-5848-8bf4-79e2b43099b0` | PROVIDER PARTNERS HEALTH PLAN OF NORTH CAROLINA | 1 | [3](per_fpi/provider_partners_health_plan_of_north_carolina.md) | medicare_advantage |
| `2f2d2d6b-41ea-5bcc-a3a7-9339c95ac8f2` | PROVIDER PARTNERS HEALTH PLAN OF PENNSYLVANIA, INC | 1 | [3](per_fpi/provider_partners_health_plan_of_pennsylvania_inc.md) | medicare_advantage |
| `ae76ea88-056e-5805-a899-631d4b505514` | PROVIDER PARTNERS HEALTH PLAN, INC. | 1 | [3](per_fpi/provider_partners_health_plan_inc.md) | medicare_advantage |
| `54ce34f5-7f49-5423-b7f2-6f7fe0201545` | PRUITTHEALTH PREMIER, INC. | 1 | [3](per_fpi/pruitthealth_premier_inc.md) | medicare_advantage |
| `35a8ba14-b422-525a-89f4-c243183cfe70` | REGENCE BLUESHIELD OF IDAHO AND REGENCE BC BS UTAH | 1 | [3](per_fpi/regence_blueshield_of_idaho_and_regence_bc_bs_utah.md) | medicare_advantage |
| `d7b06200-3729-5131-bf8f-9c5d75e2ebce` | SECUR INC | 1 | [3](per_fpi/secur_inc.md) | medicare_advantage |
| `086fbd9f-a605-5b24-afbd-2fb0b3233f64` | SELECTCARE OF TEXAS, INC. | 1 | [3](per_fpi/selectcare_of_texas_inc.md) | medicare_advantage |
| `76a8e424-e3f9-58cb-b6e2-b98ecf45505b` | SIMPRA ADVANTAGE, INC. | 1 | [3](per_fpi/simpra_advantage_inc.md) | medicare_advantage |
| `8fa93f7e-5759-5389-8508-d8d97f275cae` | TRILLIUM COMMUNITY HEALTH PLAN, INC. | 1 | [3](per_fpi/trillium_community_health_plan_inc.md) | medicare_advantage |
| `7f24a6d2-b8df-5ad7-a9fb-7c0ec42c5604` | UNITEDHEALTHCARE OF FLORIDA, INC. | 1 | [3](per_fpi/unitedhealthcare_of_florida_inc.md) | medicare_advantage |
| `b7f8e38b-58ee-5dca-9846-0c2f102f3618` | UNITEDHEALTHCARE PLAN OF THE RIVER VALLEY, INC. | 1 | [3](per_fpi/unitedhealthcare_plan_of_the_river_valley_inc.md) | medicare_advantage |
| `4974aa31-e9fa-54d9-917a-a0b90230bd33` | UPMC HEALTH BENEFITS, INC. | 1 | [3](per_fpi/upmc_health_benefits_inc.md) | medicare_advantage |
| `4b0b6575-0260-5362-8c45-0c04dc067752` | VILLAGE SENIOR SERVICES CORPORATION | 1 | [3](per_fpi/village_senior_services_corporation.md) | medicare_advantage |
| `e3d1afaf-d0e1-50c1-8072-fd2c0c4a871a` | VISITING NURSE ASSOCIATION OF CENTRAL NEW YORK | 1 | [3](per_fpi/visiting_nurse_association_of_central_new_york.md) | medicare_advantage |
| `83e5065f-8065-53aa-ba7e-9fe8738c66e1` | VNS CHOICE | 1 | [3](per_fpi/vns_choice.md) | medicare_advantage |
| `23096bd9-ecd4-5d89-b44c-2e3fed58c0b1` | VOLUNTEER STATE HEALTH PLAN | 1 | [3](per_fpi/volunteer_state_health_plan.md) | medicare_advantage |
| `e7e8b96a-7722-5aa1-95ed-8bf37abdd438` | WELLCARE HEALTH INSURANCE COMPANY OF OKLAHOMA, INC. | 1 | [3](per_fpi/wellcare_health_insurance_company_of_oklahoma_inc.md) | medicare_advantage |
| `7bda142b-a492-5f6a-931e-fca836ff940f` | WELLCARE OF CALIFORNIA, INC. | 1 | [3](per_fpi/wellcare_of_california_inc.md) | medicare_advantage |
| `6bf20c71-4139-5c32-bdfd-7f846d4da2ef` | WELLCARE OF MISSOURI HEALTH INSURANCE COMPANY, INC | 1 | [3](per_fpi/wellcare_of_missouri_health_insurance_company_inc.md) | medicare_advantage |
| `3f624556-6b2d-55c1-9247-aa5ebe07bae1` | WELLMARK  IA & SD, & BCBS MN, MT, NE, ND,& WY | 1 | [3](per_fpi/wellmark_ia_sd_bcbs_mn_mt_ne_nd_wy.md) | medicare_advantage |
| `5f200667-823c-5bc0-ae4f-e8f2f9925811` | WELLPOINT LIFE AND HEALTH INSURANCE COMPANY | 1 | [3](per_fpi/wellpoint_life_and_health_insurance_company.md) | medicare_advantage |
| `fe9bc765-3597-5330-aabe-bf8e38e0ae37` | WELLPOINT NEW JERSEY, INC. | 1 | [3](per_fpi/wellpoint_new_jersey_inc.md) | medicare_advantage |
| `431d1a85-df8a-5c00-96a2-8b993390e45f` | WELLPOINT WEST VIRGINIA , INC. | 1 | [3](per_fpi/wellpoint_west_virginia_inc.md) | medicare_advantage |
| `420b3db9-c616-5413-b902-9c6a34210577` | 1818 WESTERN, LLC | 1 | [2](per_fpi/1818_western_llc.md) | medicare_advantage |
| `b4da4b0b-e590-562e-b443-abb310d3be42` | A&D CHARITABLE FOUNDATION, INC. | 1 | [2](per_fpi/a_d_charitable_foundation_inc.md) | medicare_advantage |
| `41d9086f-f23d-5235-b90f-a0c445dacf70` | ACUTECARE PACE FRANKLIN, LLC | 1 | [2](per_fpi/acutecare_pace_franklin_llc.md) | medicare_advantage |
| `4321b5af-766f-54ac-9fd5-90e4e2377af4` | AETNA BETTER HEALTH OF WASHINGTON, INC. | 1 | [2](per_fpi/aetna_better_health_of_washington_inc.md) | medicare_advantage |
| `5fca82db-3e97-5415-a9fa-4bf66d449cda` | AETNA HEALTH OF IOWA INC. | 1 | [2](per_fpi/aetna_health_of_iowa_inc.md) | medicare_advantage |
| `27816cf9-aafc-55f2-a8aa-f84acd806c65` | AGEWELL PACE | 1 | [2](per_fpi/agewell_pace.md) | medicare_advantage |
| `58ae19a0-919c-515c-8207-2b9c623b7bd5` | ALBRIGHT CARE SERVICES | 1 | [2](per_fpi/albright_care_services.md) | medicare_advantage |
| `aaec3479-b308-576e-8778-48f16eb1253a` | ALEXIAN BROTHERS COMMUNITY SERVICES | 1 | [2](per_fpi/alexian_brothers_community_services.md) | medicare_advantage |
| `a4ec8013-260e-52f1-8a5a-c73cd8c40100` | ALIGN SENIOR CARE FLORIDA, INC. | 1 | [2](per_fpi/align_senior_care_florida_inc.md) | medicare_advantage |
| `46770022-7afb-541e-b940-4f20c3d7ee40` | ALIGN SENIOR CARE MI, LLC | 1 | [2](per_fpi/align_senior_care_mi_llc.md) | medicare_advantage |
| `318fe529-af37-541b-b529-1f5c5ef84348` | ALOHACARE | 1 | [2](per_fpi/alohacare.md) | medicare_advantage |
| `83a44bc0-328c-5549-84b3-c2a94b9265d4` | ALTAMED HEALTH SERVICES CORPORATION | 1 | [2](per_fpi/altamed_health_services_corporation.md) | medicare_advantage |
| `bed5ccdd-f302-5181-87ea-14115d67c260` | AMARILLO MULTISVC CTR FR THE AGING INC | 1 | [2](per_fpi/amarillo_multisvc_ctr_fr_the_aging_inc.md) | medicare_advantage |
| `6e67dd5d-47ea-521a-ac0c-4a53e18a83ea` | AMERICAN HEALTH PLAN OF IOWA INC | 1 | [2](per_fpi/american_health_plan_of_iowa_inc.md) | medicare_advantage |
| `9fa27371-8c30-5ade-951c-2dd21361dfc0` | AMERICAN HEALTH PLAN OF MISSOURI, INC. | 1 | [2](per_fpi/american_health_plan_of_missouri_inc.md) | medicare_advantage |
| `431b920f-2235-548c-be6e-9f931d95e051` | AMERICAN HEALTH PLAN OF UT, INC. | 1 | [2](per_fpi/american_health_plan_of_ut_inc.md) | medicare_advantage |
| `2708616a-1bdb-5ab0-9014-8ea8d36dbcba` | APPALACHIAN AGENCY FOR SENIOR CITIZENS, INC. | 1 | [2](per_fpi/appalachian_agency_for_senior_citizens_inc.md) | medicare_advantage |
| `199faf16-ee63-5378-9777-ca24b3e92d93` | ARIZONA PHYSICIANS IPA, INC. | 1 | [2](per_fpi/arizona_physicians_ipa_inc.md) | medicare_advantage |
| `2b359857-03bd-5936-aa30-26bc2b33ac29` | ARKANSAS SUPERIOR SELECT, INC. | 1 | [2](per_fpi/arkansas_superior_select_inc.md) | medicare_advantage |
| `0b8f5d6f-91fc-5f56-98a6-106b1ec2fa98` | ASCENSION LIVING ST. VINCENT PACE, INC. | 1 | [2](per_fpi/ascension_living_st_vincent_pace_inc.md) | medicare_advantage |
| `890a2fef-74d0-517f-acf8-d3cdae1e1229` | ASPIRUS HEALTH PLAN, INC. | 1 | [2](per_fpi/aspirus_health_plan_inc.md) | medicare_advantage |
| `e9470828-3283-553d-b2d5-d7e1f589cd66` | ATLANTICARE HEALTH SERVICES, INC. | 1 | [2](per_fpi/atlanticare_health_services_inc.md) | medicare_advantage |
| `460f9953-f51a-5b73-8db6-c70caef4e26f` | Advocates for a Healthy Community, Inc. dba Jordan | 1 | [2](per_fpi/advocates_for_a_healthy_community_inc_dba_jordan.md) | medicare_advantage |
| `9f540191-73cf-55bf-ba18-fef64558e4e9` | AmeriHealth Caritas VIP Next, Inc. | 1 | [2](per_fpi/amerihealth_caritas_vip_next_inc.md) | medicare_advantage |
| `9c73ca0c-c3a3-530a-a7cb-165fc1d2d8bb` | BANNER - UNIVERSITY CARE ADVANTAGE | 1 | [2](per_fpi/banner_university_care_advantage.md) | medicare_advantage |
| `b4c90288-f426-566b-bab8-3ce782bf3bcb` | BEACON OF LIFE CENTRAL NJ, LLC | 1 | [2](per_fpi/beacon_of_life_central_nj_llc.md) | medicare_advantage |
| `463fd08a-d632-5a12-9a82-0d2a80af8587` | BEACON OF LIFE NORTH NJ, LLC | 1 | [2](per_fpi/beacon_of_life_north_nj_llc.md) | medicare_advantage |
| `c28ea61a-e0e3-5b4f-9528-2ed325ad8ade` | BEACON OF LIFE SC, LLC | 1 | [2](per_fpi/beacon_of_life_sc_llc.md) | medicare_advantage |
| `7a24a5f9-fb96-5bd4-80af-22ade7456d8e` | BEACON PACE ILLINOIS, LLC | 1 | [2](per_fpi/beacon_pace_illinois_llc.md) | medicare_advantage |
| `943316e9-c8c6-5e73-8d12-26f855db8f0d` | BESHP, INC. | 1 | [2](per_fpi/beshp_inc.md) | medicare_advantage |
| `019b031a-762a-59ba-841b-2b1b30c9a12f` | BIENVIVIR SENIOR HEALTH SERVICES | 1 | [2](per_fpi/bienvivir_senior_health_services.md) | medicare_advantage |
| `d9d44612-1aa6-5cb6-a4c1-10924a3be1f5` | BLUE RIDGE INDEPENDENCE AT HOME, INC. | 1 | [2](per_fpi/blue_ridge_independence_at_home_inc.md) | medicare_advantage |
| `4116a613-d6f6-5cdf-a37b-a70d5df41916` | BLUESTEM PACE, INC. | 1 | [2](per_fpi/bluestem_pace_inc.md) | medicare_advantage |
| `be3f373b-c0b8-5da1-b8b6-db9831c55bbd` | BOLDAGE PACE INDIANA, LLC | 1 | [2](per_fpi/boldage_pace_indiana_llc.md) | medicare_advantage |
| `c673b91b-f67b-59fc-8651-10eccdca3d8e` | BOLDAGE PACE KENTUCKY, LLC | 1 | [2](per_fpi/boldage_pace_kentucky_llc.md) | medicare_advantage |
| `5e7418ca-d0bc-52a5-82da-82fcf7e8d380` | BRANDMAN CENTERS FOR SENIOR CARE, INC. | 1 | [2](per_fpi/brandman_centers_for_senior_care_inc.md) | medicare_advantage |
| `a72e0d99-ab86-5696-b4cc-019feebda4e1` | BROWARD PACE PROGRAM LLC | 1 | [2](per_fpi/broward_pace_program_llc.md) | medicare_advantage |
| `6088b81d-544d-519e-9dd2-1d9fcd4b802d` | Bridgeway Health Solutions of Arizona, Inc. | 1 | [2](per_fpi/bridgeway_health_solutions_of_arizona_inc.md) | medicare_advantage |
| `12da8116-92fb-595e-b0f7-b094cc46234c` | CAMBRIDGE PUBLIC HEALTH COMMISSION | 1 | [2](per_fpi/cambridge_public_health_commission.md) | medicare_advantage |
| `7dbe77da-a8e5-5871-b57a-3eb5973a2036` | CAPITAL HEALTH LIFE | 1 | [2](per_fpi/capital_health_life.md) | medicare_advantage |
| `6b4b0003-427b-510a-a98e-1e228ef7eaf1` | CARE GUIDE PARTNERS, INC. | 1 | [2](per_fpi/care_guide_partners_inc.md) | medicare_advantage |
| `f4479834-baf4-5f8f-984a-2957156068cb` | CARE RESOURCES | 1 | [2](per_fpi/care_resources.md) | medicare_advantage |
| `2a517d70-20eb-59cd-9355-d11222ab184d` | CAREPARTNERS REHABILITATION HOSPITAL, LLLP | 1 | [2](per_fpi/carepartners_rehabilitation_hospital_lllp.md) | medicare_advantage |
| `97c4e3b6-999d-5b30-8e2b-68fe5ac040dd` | CARESOURCE GEORGIA CO. | 1 | [2](per_fpi/caresource_georgia_co.md) | medicare_advantage |
| `945395fd-464e-57dc-86ca-04e0f5515571` | CAROLINA SENIORCARE | 1 | [2](per_fpi/carolina_seniorcare.md) | medicare_advantage |
| `b1be3b15-386a-5600-8896-d4408c9fe508` | CATHOLIC HEALTH SYSTEM BUFFALO PACE | 1 | [2](per_fpi/catholic_health_system_buffalo_pace.md) | medicare_advantage |
| `d15fd079-5871-5c9a-ba00-9b62277111d0` | CATHOLIC MANAGED LONG TERM CARE, INC. | 1 | [2](per_fpi/catholic_managed_long_term_care_inc.md) | medicare_advantage |
| `b9b577e7-df47-579c-a387-b0fa603dd35d` | CENTENE VENTURE COMPANY TENNESSEE | 1 | [2](per_fpi/centene_venture_company_tennessee.md) | medicare_advantage |
| `29cdeba0-18c3-5a99-a28c-9a247b05e30c` | CENTER FOR ELDERS INDEPENDENCE | 1 | [2](per_fpi/center_for_elders_independence.md) | medicare_advantage |
| `29298aaa-28fc-5c8e-823a-6a045f70eabb` | CENTERLIGHT HEALTHCARE, INC. | 1 | [2](per_fpi/centerlight_healthcare_inc.md) | medicare_advantage |
| `e67580b0-af2c-59f8-b73d-9b04bcafd547` | CENTRA HEALTH, INC. | 1 | [2](per_fpi/centra_health_inc.md) | medicare_advantage |
| `5d2e10e7-1814-5058-9fda-1130fae2ae2e` | CHEROKEE NATION COMPREHENSIVE CARE AGENCY | 1 | [2](per_fpi/cherokee_nation_comprehensive_care_agency.md) | medicare_advantage |
| `7302a7ac-c39d-5d06-90ab-e2e90c617823` | CHINATOWN SERVICE CENTER | 1 | [2](per_fpi/chinatown_service_center.md) | medicare_advantage |
| `31b06d8a-60a5-5dd0-a8b8-f06f8a9c64be` | CLINICAS DE SALUD DEL PUEBLO, INC. | 1 | [2](per_fpi/clinicas_de_salud_del_pueblo_inc.md) | medicare_advantage |
| `8211e08f-3b70-5f89-baf6-49c3f1b6e382` | CLOVER HMO OF NEW JERSEY INC. | 1 | [2](per_fpi/clover_hmo_of_new_jersey_inc.md) | medicare_advantage |
| `3cf045a9-dd71-5669-b7f9-68d92c06c274` | COLLABRIA CARE | 1 | [2](per_fpi/collabria_care.md) | medicare_advantage |
| `4f934323-1bde-5a82-a310-56febcce6c0e` | COMMUNITY CARE, INC. | 1 | [2](per_fpi/community_care_inc.md) | medicare_advantage |
| `607531ab-d579-5eb1-9d5a-b5d332abdfcf` | COMMUNITY ELDERCARE OF SAN DIEGO | 1 | [2](per_fpi/community_eldercare_of_san_diego.md) | medicare_advantage |
| `f0daf465-d06c-5a0e-a8f2-63b23b484a7e` | COMMUNITY FIRST HEALTH PLANS, INC. | 1 | [2](per_fpi/community_first_health_plans_inc.md) | medicare_advantage |
| `7773cee2-dbc4-5a41-9b55-7ce2eeb6e67c` | COMMUNITY HEALTH CHOICE TEXAS, INC. | 1 | [2](per_fpi/community_health_choice_texas_inc.md) | medicare_advantage |
| `b0516499-3bf9-5a96-974b-a3d808243efc` | COMMUNITY HEALTH PLAN OF WASHINGTON | 1 | [2](per_fpi/community_health_plan_of_washington.md) | medicare_advantage |
| `7c6ebe4d-5892-56b1-9d5d-6ecf7a2ffb79` | COMMUNITY PACE AT HOME, INC | 1 | [2](per_fpi/community_pace_at_home_inc.md) | medicare_advantage |
| `c1a9b373-2f03-5cde-8df7-02960fbe02cd` | COMPLETE CARE PACE PROGRAM | 1 | [2](per_fpi/complete_care_pace_program.md) | medicare_advantage |
| `46c10306-69e3-54ee-bf44-d003468c6ea0` | COMPLETE HEALTH WITH PACE | 1 | [2](per_fpi/complete_health_with_pace.md) | medicare_advantage |
| `9c446e32-c7ac-5b80-afe5-cddf48e0f89e` | COMPLETE SENIOR CARE, INC. | 1 | [2](per_fpi/complete_senior_care_inc.md) | medicare_advantage |
| `67e9659e-49cb-5ae9-ae38-3c3f94c915fc` | COMPREHENSIVE SENIOR CARE CORPORATION | 1 | [2](per_fpi/comprehensive_senior_care_corporation.md) | medicare_advantage |
| `0fa06367-64de-551a-b077-1545d28095f8` | CONCERTOHEALTH OF NORTHERN VIRGINIA, LLC | 1 | [2](per_fpi/concertohealth_of_northern_virginia_llc.md) | medicare_advantage |
| `972c1405-227e-58ed-98cb-39a354015163` | CONCERTOHEALTH PACE OF LOS ANGELES, LLC | 1 | [2](per_fpi/concertohealth_pace_of_los_angeles_llc.md) | medicare_advantage |
| `fdabe56c-215d-5589-92f4-815845f6446e` | Center for Gerontology | 1 | [2](per_fpi/center_for_gerontology.md) | medicare_advantage |
| `0fc8de2b-bf28-56f2-bc1d-8322239e01ca` | DENVER HEALTH MEDICAL PLAN, INC. | 1 | [2](per_fpi/denver_health_medical_plan_inc.md) | medicare_advantage |
| `de99dd67-a726-5a76-afa4-6c981c1ebdb8` | DEVOTED HEALTH INSURANCE COMPANY OF TEXAS | 1 | [2](per_fpi/devoted_health_insurance_company_of_texas.md) | medicare_advantage |
| `2f35b9ac-6e7f-5a2c-a719-df7818400793` | DEVOTED HEALTH PLAN OF SOUTH CAROLINA INC | 1 | [2](per_fpi/devoted_health_plan_of_south_carolina_inc.md) | medicare_advantage |
| `8cdb091d-1745-5bfd-a2a0-1e5c06ff79a5` | Devoted Health Insurance Company of Illinois, Inc. | 1 | [2](per_fpi/devoted_health_insurance_company_of_illinois_inc.md) | medicare_advantage |
| `d43c42d5-c59d-5ae0-8c29-ae5395d37508` | EDUCATORS MUTUAL INSURANCE ASSOCIATION | 1 | [2](per_fpi/educators_mutual_insurance_association.md) | medicare_advantage |
| `5872ad70-db23-59ca-b5f9-c2c26086f3e5` | ELDERHAUS INC. | 1 | [2](per_fpi/elderhaus_inc.md) | medicare_advantage |
| `27fc6ce2-27e5-5b04-8a5f-1ec1c4df27aa` | ELDERSERVE HEALTH, INC. | 1 | [2](per_fpi/elderserve_health_inc.md) | medicare_advantage |
| `a4cb437b-1a6b-5f0e-90f4-c1e9f969cfdd` | ELEMENT CARE, INC. | 1 | [2](per_fpi/element_care_inc.md) | medicare_advantage |
| `e269b805-ce89-5c98-8a12-a4d2dbbddadc` | ELITE HEALTH PLAN, INC. | 1 | [2](per_fpi/elite_health_plan_inc.md) | medicare_advantage |
| `55b7e3d9-c98c-553d-9003-691fac186d52` | EMPATH LIFE, INC. | 1 | [2](per_fpi/empath_life_inc.md) | medicare_advantage |
| `78c22b51-1062-53b1-974d-a6bde8725de7` | ESPERANZA HEALTH CENTERS | 1 | [2](per_fpi/esperanza_health_centers.md) | medicare_advantage |
| `1db2d530-f01a-5c85-9207-889b27e8df9d` | FALLON HEALTH WEINBERG, INC. | 1 | [2](per_fpi/fallon_health_weinberg_inc.md) | medicare_advantage |
| `c614baae-639f-5141-a7c7-036d0ac419d8` | FAMILY HEALTH CENTERS OF SAN DIEGO, INC | 1 | [2](per_fpi/family_health_centers_of_san_diego_inc.md) | medicare_advantage |
| `0b4c9d01-a10c-50fa-9f17-eff87f42dfe9` | FIRST HEALTH LIFE & HEALTH INSURANCE COMPANY | 1 | [2](per_fpi/first_health_life_health_insurance_company.md) | medicare_advantage |
| `b4d23c1e-e320-5235-a1a3-c147eda5d22b` | FLORIDA PACE CENTERS, INC. | 1 | [2](per_fpi/florida_pace_centers_inc.md) | medicare_advantage |
| `514e2af0-5517-573e-9d8c-edc3fecec8fd` | FRANCISCAN ACO, INC. | 1 | [2](per_fpi/franciscan_aco_inc.md) | medicare_advantage |
| `0facffb2-f7f6-545d-9db2-3186f5ea6799` | FRANCISCAN PACE, INC. | 1 | [2](per_fpi/franciscan_pace_inc.md) | medicare_advantage |
| `40f8a052-cb8e-5bfc-af9e-da030c812f41` | Family HealthCare Network (FHCN) PACE | 1 | [2](per_fpi/family_healthcare_network_fhcn_pace.md) | medicare_advantage |
| `391652ff-f18b-5ecf-b1eb-a52323c661fb` | GARY AND MARY WEST SENIOR SERVICES, INC. | 1 | [2](per_fpi/gary_and_mary_west_senior_services_inc.md) | medicare_advantage |
| `7fcee51d-a3fe-5f88-aea6-123c20ead8c2` | GEISINGER COMMUNITY HEALTH SERVICES | 1 | [2](per_fpi/geisinger_community_health_services.md) | medicare_advantage |
| `2c232d65-57df-5067-9dbb-29e1348f520b` | GEORGIA ASSURANCE, INC. | 1 | [2](per_fpi/georgia_assurance_inc.md) | medicare_advantage |
| `c7260544-904d-5acc-800d-a5361c31ce44` | GOLDEN VALLEY HEALTH CENTERS | 1 | [2](per_fpi/golden_valley_health_centers.md) | medicare_advantage |
| `28712fb4-71b5-56f0-b154-3fdeb59ce409` | GOOD SAMARITAN INSURANCE PLAN OF NEBRASKA, INC. | 1 | [2](per_fpi/good_samaritan_insurance_plan_of_nebraska_inc.md) | medicare_advantage |
| `34f7c78d-3c39-588e-b674-dd51d8553d43` | GROUP HEALTH COOPERATIVE OF EAU CLAIRE | 1 | [2](per_fpi/group_health_cooperative_of_eau_claire.md) | medicare_advantage |
| `2bb079d0-36ce-5077-97f9-6c452199614f` | HAMASPIK, INC. | 1 | [2](per_fpi/hamaspik_inc.md) | medicare_advantage |
| `ae70a8ec-5e18-5b8d-bb9a-55adcf9f4159` | HARBOR HEALTH SERVICES, INC. | 1 | [2](per_fpi/harbor_health_services_inc.md) | medicare_advantage |
| `0432ab06-1407-5ad0-bc4b-6fa40215f81a` | HIGH DESERT PACE, INC, | 1 | [2](per_fpi/high_desert_pace_inc.md) | medicare_advantage |
| `70981a1b-6f9b-591c-b3f1-013bafde1847` | HOPE HOSPICE AND COMMUNITY SERVICES, INC. | 1 | [2](per_fpi/hope_hospice_and_community_services_inc.md) | medicare_advantage |
| `d98275fd-70e3-53fa-a3e8-4b9ec87f166f` | HOPEWEST | 1 | [2](per_fpi/hopewest.md) | medicare_advantage |
| `97d099e4-24f6-5dce-bd49-e364d60bdcd4` | HORIZON-PACE, LLC | 1 | [2](per_fpi/horizon_pace_llc.md) | medicare_advantage |
| `ce26e032-4505-58ce-814a-ff4da217ef21` | HOSPICE OF METRO DENVER, INC | 1 | [2](per_fpi/hospice_of_metro_denver_inc.md) | medicare_advantage |
| `ede161e6-50ba-5b57-8f30-4acbbb6aac2a` | HOSPICE OF THE BLUEGRASS, INC | 1 | [2](per_fpi/hospice_of_the_bluegrass_inc.md) | medicare_advantage |
| `f757db87-c3aa-50d3-9af8-65408fc6c6ce` | HUMANA MEDICAL PLAN OF PENNSYLVANIA, INC. | 1 | [2](per_fpi/humana_medical_plan_of_pennsylvania_inc.md) | medicare_advantage |
| `2fd928a9-9d9a-52d4-83ce-692b6ac8dd1c` | HUMANA REGIONAL HEALTH PLAN, INC. | 1 | [2](per_fpi/humana_regional_health_plan_inc.md) | medicare_advantage |
| `98eade34-3907-54ef-8af1-bb0e5063a839` | HUMBOLDT SENIOR RESOURCE CENTER, INC. | 1 | [2](per_fpi/humboldt_senior_resource_center_inc.md) | medicare_advantage |
| `5662e61a-ccfd-55b7-85a8-689683d556c4` | INDEPENDENT LIVING FOR SENIORS, INC. | 1 | [2](per_fpi/independent_living_for_seniors_inc.md) | medicare_advantage |
| `7fa97fcf-8b29-59d3-8b21-ea6eb64a0a40` | INNOVAGE CALIFORNIA PACE-SACRAMENTO, LLC | 1 | [2](per_fpi/innovage_california_pace_sacramento_llc.md) | medicare_advantage |
| `036f2cc7-ad35-515d-9ce9-c9d6d9cf037a` | INNOVAGE FLORIDA PACE II, LLC | 1 | [2](per_fpi/innovage_florida_pace_ii_llc.md) | medicare_advantage |
| `b2a4510d-779b-5de9-902e-739ef2ad23f6` | INNOVAGE FLORIDA PACE, LLC | 1 | [2](per_fpi/innovage_florida_pace_llc.md) | medicare_advantage |
| `47ef287e-4a8f-54f0-917f-a7ae707e902d` | INNOVAGE PENNSYLVANIA LIFE, LLC | 1 | [2](per_fpi/innovage_pennsylvania_life_llc.md) | medicare_advantage |
| `1b729132-56c1-513d-aebb-352a64be3b93` | INNOVAGE VIRGINIA PACE II, LLC | 1 | [2](per_fpi/innovage_virginia_pace_ii_llc.md) | medicare_advantage |
| `a4affe69-94c3-52e3-8a9a-4675d3c555bf` | INNOVAGE VIRGINIA PACE-CHARLOTTESVILLE, LLC | 1 | [2](per_fpi/innovage_virginia_pace_charlottesville_llc.md) | medicare_advantage |
| `35570bbf-c273-5e73-8f73-c60bb3fbcb0c` | INNOVAGE VIRGINIA PACE-ROANOKE VALLEY, LLC | 1 | [2](per_fpi/innovage_virginia_pace_roanoke_valley_llc.md) | medicare_advantage |
| `563951a0-5113-5d27-a783-4101d4783131` | INNOVATIVE INTEGRATED HEALTH, INC. | 1 | [2](per_fpi/innovative_integrated_health_inc.md) | medicare_advantage |
| `97550a74-de3f-57d2-accc-8584f10696b7` | INSPIRA HEALTH NETWORK LIFE, INC. | 1 | [2](per_fpi/inspira_health_network_life_inc.md) | medicare_advantage |
| `4a654366-6c90-5806-a2c8-270a99ea66d9` | INTERNATIONAL COMMUNITY HEALTH SERVICES | 1 | [2](per_fpi/international_community_health_services.md) | medicare_advantage |
| `881a1b8e-ac60-5169-a51c-124c4b0be641` | ISNP VENTURES, LLC | 1 | [2](per_fpi/isnp_ventures_llc.md) | medicare_advantage |
| `8689440b-cbc6-55d0-8db3-013bf87c83b8` | K-DAY, INC. | 1 | [2](per_fpi/k_day_inc.md) | medicare_advantage |
| `59aafe7b-7114-5c6f-8dac-a86e2ca4c7be` | KANSAS SUPERIOR SELECT, INC. | 1 | [2](per_fpi/kansas_superior_select_inc.md) | medicare_advantage |
| `2ea68d0f-e5c4-560f-9de6-2925fadf345b` | KINSHIP PACE OF INDIANA, LLC | 1 | [2](per_fpi/kinship_pace_of_indiana_llc.md) | medicare_advantage |
| `9d43c8fc-3709-58d0-9927-8cdf745d07fa` | LA COAST PACE, LLC | 1 | [2](per_fpi/la_coast_pace_llc.md) | medicare_advantage |
| `a10446b9-1e2a-5737-a06a-11e6c5324650` | LAWNDALE CHRISTIAN HEALTH CENTER | 1 | [2](per_fpi/lawndale_christian_health_center.md) | medicare_advantage |
| `9ffde4d9-7983-507d-bfa7-ce4ebb749274` | LIFE AT LOURDES, INC. | 1 | [2](per_fpi/life_at_lourdes_inc.md) | medicare_advantage |
| `5e645c76-ea92-59bc-b857-0365ca251840` | LIFE AT ST. FRANCIS HEALTHCARE, INC. | 1 | [2](per_fpi/life_at_st_francis_healthcare_inc.md) | medicare_advantage |
| `42f8cf1d-ade7-5559-b1ec-1a63e4c3679f` | LIFE COORDINATED COMMONWEALTH PACE INC | 1 | [2](per_fpi/life_coordinated_commonwealth_pace_inc.md) | medicare_advantage |
| `9abee382-3c73-5bf5-bdc9-a63181fb73a4` | LIFE Northwestern Pennsylvania, LLC | 1 | [2](per_fpi/life_northwestern_pennsylvania_llc.md) | medicare_advantage |
| `57d3dafd-8ebd-5939-b2e1-c8db809c1771` | LIFE PACE | 1 | [2](per_fpi/life_pace.md) | medicare_advantage |
| `52970b49-a677-54fc-a1ff-04302e625173` | LIFE ST. JOSEPH OF THE PINES, INC. | 1 | [2](per_fpi/life_st_joseph_of_the_pines_inc.md) | medicare_advantage |
| `692d45f5-f7aa-5e6d-98ba-8ccc51a0d7de` | LIFE ST. MARY | 1 | [2](per_fpi/life_st_mary.md) | medicare_advantage |
| `9773b371-9ad4-5e27-abfa-daf8b96f200b` | LIFECIRCLES | 1 | [2](per_fpi/lifecircles.md) | medicare_advantage |
| `0a46c060-a025-5755-836c-392fb2b5dbf6` | LIFEWORKS ADVANTAGE, LLC | 1 | [2](per_fpi/lifeworks_advantage_llc.md) | medicare_advantage |
| `b39c5721-a7bb-5c35-8264-0ef03252526a` | LIVING INDEPENDENCE FOR THE ELDERLY PITTSBURGH INC | 1 | [2](per_fpi/living_independence_for_the_elderly_pittsburgh_inc.md) | medicare_advantage |
| `fd3fd715-2879-5175-a29d-d0d6a41512e9` | LOMA LINDA UNIVERSITY MEDICAL CENTER | 1 | [2](per_fpi/loma_linda_university_medical_center.md) | medicare_advantage |
| `c46a23e9-2b83-5cdf-8e8e-dd92926ea321` | LONGEVITY HEALTH PLAN OF NEW JERSEY INSURANCE COMP | 1 | [2](per_fpi/longevity_health_plan_of_new_jersey_insurance_comp.md) | medicare_advantage |
| `f881374b-5389-539a-8250-443e56aee8e7` | LORETTO INDEPENDENT LIVING SERVICES, INC. | 1 | [2](per_fpi/loretto_independent_living_services_inc.md) | medicare_advantage |
| `0653e52c-ab4a-52c8-841d-686da4033d51` | LUBBOCK REGIONAL MENTAL HEALTH MENTAL RETARDATION | 1 | [2](per_fpi/lubbock_regional_mental_health_mental_retardation.md) | medicare_advantage |
| `32265427-ed36-5550-8ec3-27f5d35190e6` | LUTHERAN SENIOR HEALTHCARE, INC. | 1 | [2](per_fpi/lutheran_senior_healthcare_inc.md) | medicare_advantage |
| `b97c8116-9605-55e8-a93e-d9cb325b7b8b` | MCGREGOR PACE | 1 | [2](per_fpi/mcgregor_pace.md) | medicare_advantage |
| `f2167b47-c8dd-56a6-9c65-3efb6919db67` | MERCY LIFE OF ALABAMA | 1 | [2](per_fpi/mercy_life_of_alabama.md) | medicare_advantage |
| `0459200f-a16c-5778-8ff2-29cb879d5de2` | MERCY LIFE, INC. | 1 | [2](per_fpi/mercy_life_inc.md) | medicare_advantage |
| `63044013-71b6-57fe-bbfc-1818daffe776` | MIDLAND CARE CONNECTION | 1 | [2](per_fpi/midland_care_connection.md) | medicare_advantage |
| `a776dc91-71b9-5b0b-a4f2-75f66b5fac2d` | MILFORD WELLNESS VILLAGE PACE | 1 | [2](per_fpi/milford_wellness_village_pace.md) | medicare_advantage |
| `72a57139-c4f1-59a6-b0f0-88c8ae4d7970` | MISSOURI CARE, INCORPORATED | 1 | [2](per_fpi/missouri_care_incorporated.md) | medicare_advantage |
| `1e4acf06-b25f-5a78-ac0d-fe929b0b6365` | MOLINA HEALTHCARE OF OHIO, INC. | 1 | [2](per_fpi/molina_healthcare_of_ohio_inc.md) | medicare_advantage |
| `6c4f6b9a-c8b5-5f69-9f88-41dccdf52389` | MOLINA HEALTHCARE OF WASHINGTON, INC. | 1 | [2](per_fpi/molina_healthcare_of_washington_inc.md) | medicare_advantage |
| `908cab5e-7965-5419-b175-93f38e30076f` | MORSE LIFE HOME CARE, INC. | 1 | [2](per_fpi/morse_life_home_care_inc.md) | medicare_advantage |
| `c998b148-b03c-5bf7-b56f-7725c769e0f6` | MOUNT SINAI ELDERCARE, INC. | 1 | [2](per_fpi/mount_sinai_eldercare_inc.md) | medicare_advantage |
| `9a64bdb1-e642-5517-b060-3f7699c371fc` | MOUNTAIN EMPIRE OLDER CITIZENS, INC. | 1 | [2](per_fpi/mountain_empire_older_citizens_inc.md) | medicare_advantage |
| `4c2f96a1-29c1-5a3a-88b6-0dfdaf5da92c` | MYPLACE SOUTH LA PACE INC. | 1 | [2](per_fpi/myplace_south_la_pace_inc.md) | medicare_advantage |
| `de79aa41-dda2-5e70-a732-652e9bba2420` | Mercy LIFE | 1 | [2](per_fpi/mercy_life.md) | medicare_advantage |
| `02127131-1361-56b0-89db-124e66127a74` | Molina Healthcare of Wisconsin, Inc. | 1 | [2](per_fpi/molina_healthcare_of_wisconsin_inc.md) | medicare_advantage |
| `cd06dbfa-9d70-5806-9bc9-5ba64c5021e8` | NEIGHBORHEALTH CORPORATION | 1 | [2](per_fpi/neighborhealth_corporation.md) | medicare_advantage |
| `7c8b2e38-20c3-5bbb-8086-8aa42cf23467` | NEIGHBORHOOD HEALTH PLAN OF RHODE ISLAND | 1 | [2](per_fpi/neighborhood_health_plan_of_rhode_island.md) | medicare_advantage |
| `15635c13-63b6-5fb0-9edb-39fa73f1baff` | NEIGHBORHOOD HEALTHCARE | 1 | [2](per_fpi/neighborhood_healthcare.md) | medicare_advantage |
| `4429f328-9170-5b01-9689-365be3690e4b` | NEW CENTURY HEALTH PLAN, INC. | 1 | [2](per_fpi/new_century_health_plan_inc.md) | medicare_advantage |
| `75a80eda-8c7e-5191-ae77-e6e61886223e` | NHC ADVANTAGE, LLC | 1 | [2](per_fpi/nhc_advantage_llc.md) | medicare_advantage |
| `1a161a89-9d96-5802-a949-c69d7154e767` | NORTH EAST MEDICAL SERVICES | 1 | [2](per_fpi/north_east_medical_services.md) | medicare_advantage |
| `caebf110-0ff5-5770-99df-9a9cbff0c704` | NORTHLAND PACE PROGRAM | 1 | [2](per_fpi/northland_pace_program.md) | medicare_advantage |
| `4046e416-e7a8-5335-838e-738426da2a77` | OH CHS SNP INC. | 1 | [2](per_fpi/oh_chs_snp_inc.md) | medicare_advantage |
| `ce275cd2-8713-5667-8913-0093bf1777e8` | ON LOK SENIOR HEALTH SERVICES | 1 | [2](per_fpi/on_lok_senior_health_services.md) | medicare_advantage |
| `b5c093a1-bc86-5ae0-926e-7f1fac3b373a` | ONE SENIOR CARE KENTUCKY, LLC | 1 | [2](per_fpi/one_senior_care_kentucky_llc.md) | medicare_advantage |
| `ba3f23cf-7674-5a51-82ba-25490a1f5844` | ONE SENIOR CARE OHIO, LLC | 1 | [2](per_fpi/one_senior_care_ohio_llc.md) | medicare_advantage |
| `6009ef32-0673-5a4b-a010-812634ae306b` | OSF HEALTHCARE SYSTEM | 1 | [2](per_fpi/osf_healthcare_system.md) | medicare_advantage |
| `c9540637-cdb1-5d7a-8e96-4b6896e80309` | Orangeburg Senior Helping Center, LLC | 1 | [2](per_fpi/orangeburg_senior_helping_center_llc.md) | medicare_advantage |
| `d8c3eeab-51d1-5c39-8934-11a3d017a9ff` | PACE @ HOME, INC. | 1 | [2](per_fpi/pace_home_inc.md) | medicare_advantage |
| `eb514f6f-7a3b-571a-8ec3-43dde56c8f7b` | PACE AT HUDSON HEADWATERS, INC. | 1 | [2](per_fpi/pace_at_hudson_headwaters_inc.md) | medicare_advantage |
| `fd4515fb-ab42-54c9-90d1-939582315555` | PACE CENTRAL MICHIGAN, INC. | 1 | [2](per_fpi/pace_central_michigan_inc.md) | medicare_advantage |
| `de173cc6-2c06-5a61-9ffb-524a12020861` | PACE GREATER NEW ORLEANS | 1 | [2](per_fpi/pace_greater_new_orleans.md) | medicare_advantage |
| `eb6f409c-7416-5bdb-845a-746d97b1df2e` | PACE IOWA | 1 | [2](per_fpi/pace_iowa.md) | medicare_advantage |
| `9614a14e-cb5c-5564-be45-80791dd38236` | PACE KC, LLC | 1 | [2](per_fpi/pace_kc_llc.md) | medicare_advantage |
| `e6dd799b-5e53-53ec-9d85-5da54f8c5c94` | PACE NEBRASKA | 1 | [2](per_fpi/pace_nebraska.md) | medicare_advantage |
| `1c7066f7-2895-53a4-9a2b-fc0b227d44eb` | PACE NORTH, INC. | 1 | [2](per_fpi/pace_north_inc.md) | medicare_advantage |
| `ace4edb0-4ff2-5f77-b35b-5079c5c0b968` | PACE NORTHEAST MICHIGAN | 1 | [2](per_fpi/pace_northeast_michigan.md) | medicare_advantage |
| `1d1544b5-a78e-5a67-9c6f-5206e4f5ec40` | PACE OF GUILFORD AND ROCKINGHAM COUNTIES, INC. | 1 | [2](per_fpi/pace_of_guilford_and_rockingham_counties_inc.md) | medicare_advantage |
| `e2859929-7af8-5c51-80aa-1c234e722af4` | PACE OF NORTHEAST INDIANA, LLC | 1 | [2](per_fpi/pace_of_northeast_indiana_llc.md) | medicare_advantage |
| `93bb206f-7b74-5c2a-ba9f-7e01593ae66e` | PACE OF SOUTHWEST MICHIGAN, INC. | 1 | [2](per_fpi/pace_of_southwest_michigan_inc.md) | medicare_advantage |
| `d12e662a-3a46-5aea-b79a-6153dd724b6a` | PACE OF THE SOUTHERN PIEDMONT, INC. | 1 | [2](per_fpi/pace_of_the_southern_piedmont_inc.md) | medicare_advantage |
| `7c87526a-ba55-54aa-bae1-0d80234761f7` | PACE ORGANIZATION OF RHODE ISLAND | 1 | [2](per_fpi/pace_organization_of_rhode_island.md) | medicare_advantage |
| `3c88bdf8-bd74-5a52-a16d-32c09d76420b` | PACE PARTNERS OF NORTHEAST FLORIDA, INC. | 1 | [2](per_fpi/pace_partners_of_northeast_florida_inc.md) | medicare_advantage |
| `7cdf5496-fdaa-5950-bd51-807dbf625578` | PACE SOUTHEAST MICHIGAN | 1 | [2](per_fpi/pace_southeast_michigan.md) | medicare_advantage |
| `49611326-5f4c-59d2-8ad8-1cf3f01fa296` | PACE4DC LLC | 1 | [2](per_fpi/pace4dc_llc.md) | medicare_advantage |
| `9150144e-d9a2-52ca-b4e7-1b9fffcf8d9a` | PACIFIC PACE, LLC | 1 | [2](per_fpi/pacific_pace_llc.md) | medicare_advantage |
| `9da8ab28-7956-5150-98d1-e7526d19a22f` | PACIFICSOURCE PACE, LLC | 1 | [2](per_fpi/pacificsource_pace_llc.md) | medicare_advantage |
| `55efd42f-6223-5f36-b9e0-6d15d0984f67` | PARTNERS INSURANCE COMPANY OF NEW JERSEY INC | 1 | [2](per_fpi/partners_insurance_company_of_new_jersey_inc.md) | medicare_advantage |
| `0852fe7b-0064-5f64-84d5-2ca761912bca` | PEAK HEALTH INSURANCE CORPORATION | 1 | [2](per_fpi/peak_health_insurance_corporation.md) | medicare_advantage |
| `75d14793-ee13-509f-8b54-c0d826a06ecb` | PENNSYLVANIA PACE, INC. | 1 | [2](per_fpi/pennsylvania_pace_inc.md) | medicare_advantage |
| `c4331318-225e-5f94-9143-4d3673188f18` | PIEDMONT HEALTH SERVICES, INC. | 1 | [2](per_fpi/piedmont_health_services_inc.md) | medicare_advantage |
| `860b1989-d780-5c30-94cc-a83215877ca6` | PITTSBURGH CARE PARTNERSHIP, INC. | 1 | [2](per_fpi/pittsburgh_care_partnership_inc.md) | medicare_advantage |
| `a5a6e608-9695-534a-9e58-0a9bd47bec9a` | PNW PACE PARTNERS, LLC | 1 | [2](per_fpi/pnw_pace_partners_llc.md) | medicare_advantage |
| `b26a279c-5668-52e1-8b9a-77a9ab4d4239` | PRIME ACQUISITIONS, LLC | 1 | [2](per_fpi/prime_acquisitions_llc.md) | medicare_advantage |
| `7ad24516-feda-5649-94fd-22a31b238622` | PRIORITY HEALTH CHOICE, INC. | 1 | [2](per_fpi/priority_health_choice_inc.md) | medicare_advantage |
| `7b54a9c6-b255-58c3-baa8-7c211b914d0e` | PRIORITY HEALTH INSURANCE COMPANY | 1 | [2](per_fpi/priority_health_insurance_company.md) | medicare_advantage |
| `d5afa7c2-57e6-5960-a0cf-a03531ade86e` | PRISMA HEALTH-MIDLANDS | 1 | [2](per_fpi/prisma_health_midlands.md) | medicare_advantage |
| `e394a895-ccc0-59f3-b91f-44a26da06575` | PRISMA HEALTH-UPSTATE | 1 | [2](per_fpi/prisma_health_upstate.md) | medicare_advantage |
| `a41c385f-43c3-524b-ab22-f5ca330d6fd2` | PROVIDENCE HEALTH & SERVICES - OREGON | 1 | [2](per_fpi/providence_health_services_oregon.md) | medicare_advantage |
| `c6652fe2-9095-5f4c-8360-2e0f90ff70c0` | PROVIDENCE HEALTH & SERVICES â€“ WASHINGTON | 1 | [2](per_fpi/providence_health_services_washington.md) | medicare_advantage |
| `7501a471-031a-5103-ae44-2c69171eaa98` | PRUITTHEALTH PREMIER NORTH CAROLINA, LLC | 1 | [2](per_fpi/pruitthealth_premier_north_carolina_llc.md) | medicare_advantage |
| `0cb87db5-5412-5534-9951-bf4c5b55efa9` | PSERS HOP PROGRAM | 1 | [2](per_fpi/psers_hop_program.md) | medicare_advantage |
| `88bc2de8-b688-5a31-9728-566f77e5c9e5` | REGION VII AREA AGENCY ON AGING | 1 | [2](per_fpi/region_vii_area_agency_on_aging.md) | medicare_advantage |
| `162eddea-c52d-5962-98f9-2c3355758db3` | REID HOSPITAL & HEALTH CARE SERVICES, INC. | 1 | [2](per_fpi/reid_hospital_health_care_services_inc.md) | medicare_advantage |
| `5f6673f6-2ced-5b28-94f2-a59248a48643` | ROCKY MOUNTAIN HEALTH CARE SERVICES | 1 | [2](per_fpi/rocky_mountain_health_care_services.md) | medicare_advantage |
| `51fd762a-c7d5-566e-a877-4502e068ac81` | SAINT JOSEPH PACE | 1 | [2](per_fpi/saint_joseph_pace.md) | medicare_advantage |
| `f71f54fa-8554-5fb6-92e5-0a857267ce9b` | SANFORD HEALTH PLAN OF MINNESOTA | 1 | [2](per_fpi/sanford_health_plan_of_minnesota.md) | medicare_advantage |
| `8bd6e8f9-f8c7-5ebd-b7e8-827ed21e4332` | SCAN HEALTH PLAN (WA) | 1 | [2](per_fpi/scan_health_plan_wa.md) | medicare_advantage |
| `1cf4d80f-7091-5b96-9f0d-cae4a3191577` | SEEN HEALTH SAN GABRIEL VALLEY, LLC | 1 | [2](per_fpi/seen_health_san_gabriel_valley_llc.md) | medicare_advantage |
| `09894ca7-c353-582b-a1d1-e424d77f8dd4` | SENIOR CARE CONNECTION, INC. | 1 | [2](per_fpi/senior_care_connection_inc.md) | medicare_advantage |
| `f5e711f8-94a2-5ee3-ad95-95ef18cbd05a` | SENIOR LIFE ALTOONA, INC. | 1 | [2](per_fpi/senior_life_altoona_inc.md) | medicare_advantage |
| `d4c415db-8050-5468-bd18-bea36cac762c` | SENIOR LIFE GREENSBURG, INC. | 1 | [2](per_fpi/senior_life_greensburg_inc.md) | medicare_advantage |
| `2cafb55e-b0e8-5017-9128-eb4892bd7c03` | SENIOR LIFE LEHIGH VALLEY, INC. | 1 | [2](per_fpi/senior_life_lehigh_valley_inc.md) | medicare_advantage |
| `0781335c-f889-53ad-9378-cebad662a07c` | SENIOR LIFE YORK, INC. | 1 | [2](per_fpi/senior_life_york_inc.md) | medicare_advantage |
| `34c855ff-c16d-56d1-90cf-55078baef9c2` | SENIOR TOTAL LIFE CARE, INC. | 1 | [2](per_fpi/senior_total_life_care_inc.md) | medicare_advantage |
| `1052bbbc-3800-56ac-a9d1-fed5cc07da70` | SENIOR WHOLE HEALTH OF NEW YORK, INC. | 1 | [2](per_fpi/senior_whole_health_of_new_york_inc.md) | medicare_advantage |
| `8afdc11a-ae6c-551b-9aa6-34541b23cc68` | SENTARA HEALTH PLANS | 1 | [2](per_fpi/sentara_health_plans.md) | medicare_advantage |
| `d9edbdbb-ad05-53b6-a12f-fab8a9ee576a` | SENTARA LIFE CARE CORPORATION, INC | 1 | [2](per_fpi/sentara_life_care_corporation_inc.md) | medicare_advantage |
| `0c162139-9fd8-57a0-9b59-03edc9705edc` | SEQUOIA PACE, LLC | 1 | [2](per_fpi/sequoia_pace_llc.md) | medicare_advantage |
| `2456416a-8035-5a78-8519-09fc1d4e4026` | SERENITY CARE, INC. | 1 | [2](per_fpi/serenity_care_inc.md) | medicare_advantage |
| `8c8c720e-20c7-590a-919e-e792e6bd330e` | SIGNATURE ADVANTAGE, LLC | 1 | [2](per_fpi/signature_advantage_llc.md) | medicare_advantage |
| `d3f7180a-1a9c-5148-861a-052a2359ee57` | SIOUXLAND PACE, INC. | 1 | [2](per_fpi/siouxland_pace_inc.md) | medicare_advantage |
| `612c7075-030b-5cb4-b0a0-494b0b804e9d` | STAYWELL SENIOR CARE, INC. | 1 | [2](per_fpi/staywell_senior_care_inc.md) | medicare_advantage |
| `c4573594-4072-54de-931b-5b42d6c4c721` | STOCKTON PACE | 1 | [2](per_fpi/stockton_pace.md) | medicare_advantage |
| `fe83ed07-9a0d-5356-b057-07e3170f4646` | STRATUM LIFE, LLC | 1 | [2](per_fpi/stratum_life_llc.md) | medicare_advantage |
| `07002b1e-9003-523b-b4ea-c5e12899e11b` | SUNCOAST PACE, INC. | 1 | [2](per_fpi/suncoast_pace_inc.md) | medicare_advantage |
| `b4c9ed6f-318c-5eac-96df-e35e08cfed27` | SUTTER VALLEY HOSPITALS | 1 | [2](per_fpi/sutter_valley_hospitals.md) | medicare_advantage |
| `f243b3f2-a8c1-594b-b36c-8a8b57d12b85` | San Diego PACE, LLC | 1 | [2](per_fpi/san_diego_pace_llc.md) | medicare_advantage |
| `1b07e724-3431-5087-b8f1-ae7b35fbf186` | Senior CommUnity Care Of Kentucky | 1 | [2](per_fpi/senior_community_care_of_kentucky.md) | medicare_advantage |
| `487bc10e-ff98-5890-8e7c-9bb0a0da2c0c` | TEXAS INDEPENDENCE HEALTH PLAN, INC. | 1 | [2](per_fpi/texas_independence_health_plan_inc.md) | medicare_advantage |
| `c1fdd1e8-927b-5125-b3f2-66b3220d136c` | THE CASCADE PACE, INC. | 1 | [2](per_fpi/the_cascade_pace_inc.md) | medicare_advantage |
| `e3d2f602-bc0f-5a81-84d0-4c1f7069976b` | THE JOHNS HOPKINS HEALTH SYSTEM CORPORATION | 1 | [2](per_fpi/the_johns_hopkins_health_system_corporation.md) | medicare_advantage |
| `835264c2-ea72-5812-9661-42b992521aa8` | THE WASHTENAW PACE | 1 | [2](per_fpi/the_washtenaw_pace.md) | medicare_advantage |
| `bf287a98-5693-52f6-b867-eee232e35919` | TOTAL COMMUNITY CARE, L.L.C. | 1 | [2](per_fpi/total_community_care_l_l_c.md) | medicare_advantage |
| `06e85d7c-1bf2-5911-b606-b0607046986b` | TOTAL LIFE HEALTHCARE | 1 | [2](per_fpi/total_life_healthcare.md) | medicare_advantage |
| `7caf9241-b3ea-598e-a68c-12ecc5a91bbf` | TOTAL SENIOR CARE, INC. | 1 | [2](per_fpi/total_senior_care_inc.md) | medicare_advantage |
| `f127d350-52f4-573b-98d4-c8dff5990631` | TRIHEALTH G, LLC | 1 | [2](per_fpi/trihealth_g_llc.md) | medicare_advantage |
| `0fe1a077-afa7-521a-8b55-b9866b6e5ee7` | TRINITY HEALTH LIFE PENNSYLVANIA, INC. | 1 | [2](per_fpi/trinity_health_life_pennsylvania_inc.md) | medicare_advantage |
| `35dd340a-7fee-54ae-b861-8bca7a19d829` | TRINITY HEALTH PACE OF ALEXANDRIA | 1 | [2](per_fpi/trinity_health_pace_of_alexandria.md) | medicare_advantage |
| `6f093597-421e-5300-bc5c-f41be097689e` | TRINITY HEALTH PACE OF MONTGOMERY COUNTY | 1 | [2](per_fpi/trinity_health_pace_of_montgomery_county.md) | medicare_advantage |
| `9fe8a944-4945-5e72-9540-20629d60c332` | TRINITY HEALTH PACE OF PENSACOLA | 1 | [2](per_fpi/trinity_health_pace_of_pensacola.md) | medicare_advantage |
| `eb661b6d-3f00-53ea-a01e-e30757c271fc` | TROY HEALTH, INC. | 1 | [2](per_fpi/troy_health_inc.md) | medicare_advantage |
| `48446f5c-8b49-5aee-8500-683a91378528` | TRU COMMUNITY CARE | 1 | [2](per_fpi/tru_community_care.md) | medicare_advantage |
| `469172ab-33a1-56eb-920a-439d1af281c4` | TUFTS HEALTH PUBLIC PLANS, INC. | 1 | [2](per_fpi/tufts_health_public_plans_inc.md) | medicare_advantage |
| `f227f674-19d2-54a3-9a2e-cffab2a9289c` | TUNGSTEN HEALTH SACRAMENTO, LLC | 1 | [2](per_fpi/tungsten_health_sacramento_llc.md) | medicare_advantage |
| `e5041843-2a08-5780-a1e6-e9fe42395d71` | TUNGSTEN HEALTH SOUTH LOS ANGELES, LLC | 1 | [2](per_fpi/tungsten_health_south_los_angeles_llc.md) | medicare_advantage |
| `7efa14bc-c4c9-5e60-a139-9da1ca5afec9` | UNITEDHEALTHCARE COMMUNITY PLAN OF OHIO, INC. | 1 | [2](per_fpi/unitedhealthcare_community_plan_of_ohio_inc.md) | medicare_advantage |
| `227561e9-8e45-5443-a39a-6dc01202eaf7` | UPHAMS CORNER HEALTH COMMITTEE, INC. | 1 | [2](per_fpi/uphams_corner_health_committee_inc.md) | medicare_advantage |
| `9c937a53-a54b-5dfb-8b96-47077c93e0f4` | UPMC FOR YOU, INC | 1 | [2](per_fpi/upmc_for_you_inc.md) | medicare_advantage |
| `53928c9d-f6af-5f0b-88df-5b248e76d9d2` | VALIR PACE | 1 | [2](per_fpi/valir_pace.md) | medicare_advantage |
| `a652f96e-cf56-5cc7-8350-b8185489ed55` | VALLEY PACE, LLC | 1 | [2](per_fpi/valley_pace_llc.md) | medicare_advantage |
| `27b857b5-6fb7-5e38-a178-c7f54f934cab` | VERDA HEALTH PLAN OF ARIZONA, INC. | 1 | [2](per_fpi/verda_health_plan_of_arizona_inc.md) | medicare_advantage |
| `1720bb58-0ab3-5140-b6d0-5276b7b55a31` | VIA CHRISTI HEALTHCARE OUTREACH FOR ELDERS, INC. | 1 | [2](per_fpi/via_christi_healthcare_outreach_for_elders_inc.md) | medicare_advantage |
| `e6231b83-e86f-5643-9ab1-8a6b6b648d5d` | VIECARE ARMSTRONG, LLC | 1 | [2](per_fpi/viecare_armstrong_llc.md) | medicare_advantage |
| `ef902167-3cfd-5901-ae31-cdea2aee9f3f` | VIECARE BEAVER, LLC | 1 | [2](per_fpi/viecare_beaver_llc.md) | medicare_advantage |
| `c3923a60-371c-529a-807d-a0dc90e435d9` | VIECARE BUTLER, LLC | 1 | [2](per_fpi/viecare_butler_llc.md) | medicare_advantage |
| `27e0e86d-cd7a-5823-b03b-de45c35f68dc` | VISTA COMMUNITY CLINIC | 1 | [2](per_fpi/vista_community_clinic.md) | medicare_advantage |
| `84852ef7-4f58-5825-ba93-6e81df167e8c` | VISTA HEALTH PLAN, INC. | 1 | [2](per_fpi/vista_health_plan_inc.md) | medicare_advantage |
| `9adb3f53-3535-5000-839e-f52b5bcbbad6` | VOANS SENIOR COMMUNITY CARE OF COLORADO, INC | 1 | [2](per_fpi/voans_senior_community_care_of_colorado_inc.md) | medicare_advantage |
| `6335c5ce-5f54-5de2-bb99-1ce2443e11af` | VOANS SENIOR COMMUNITY CARE OF JEFFERSON COUNTY | 1 | [2](per_fpi/voans_senior_community_care_of_jefferson_county.md) | medicare_advantage |
| `c55feed4-84d0-51bd-b770-2daea68f99e7` | VOANS SENIOR COMMUNITY CARE OF MARYLAND | 1 | [2](per_fpi/voans_senior_community_care_of_maryland.md) | medicare_advantage |
| `968fe895-9ef0-5b89-aa77-89c8d998f83b` | VOANS SENIOR COMMUNITY CARE OF MICHIGAN, INC. | 1 | [2](per_fpi/voans_senior_community_care_of_michigan_inc.md) | medicare_advantage |
| `c205c831-fec7-5a16-8e77-c5a20c70e6b2` | VOANS SENIOR COMMUNITY CARE OF NORTH CAROLINA, INC | 1 | [2](per_fpi/voans_senior_community_care_of_north_carolina_inc.md) | medicare_advantage |
| `c33fa976-64f3-5687-bb67-351e4a2cce22` | VOANS SENIOR COMMUNITY CARE OF NORTHERN KENTUCKY | 1 | [2](per_fpi/voans_senior_community_care_of_northern_kentucky.md) | medicare_advantage |
| `41a1d22e-2890-57d9-920d-320ae8d5f408` | WASHINGTON REGIONAL MEDICORP | 1 | [2](per_fpi/washington_regional_medicorp.md) | medicare_advantage |
| `c58f42ea-9c0e-58c3-a995-59268e787641` | WELBEHEALTH BAY AREA PACE, LLC | 1 | [2](per_fpi/welbehealth_bay_area_pace_llc.md) | medicare_advantage |
| `ba5b3eb0-949a-52ad-aa15-d416d4d01a70` | WELBEHEALTH INLAND EMPIRE PACE, LLC | 1 | [2](per_fpi/welbehealth_inland_empire_pace_llc.md) | medicare_advantage |
| `b8be4d41-2b3e-5dcc-8001-528ae42d8e3d` | WELBEHEALTH SAN BERNARDINO PACE, LLC | 1 | [2](per_fpi/welbehealth_san_bernardino_pace_llc.md) | medicare_advantage |
| `828ffd35-74d4-5efe-aa10-ebb1070dc24f` | WELLCARE NATIONAL HEALTH INSURANCE COMPANY | 1 | [2](per_fpi/wellcare_national_health_insurance_company.md) | medicare_advantage |
| `dc0baba1-8a80-5e0f-83cf-6dbd42b4ec38` | WELLCARE OF MISSISSIPPI, INC. | 1 | [2](per_fpi/wellcare_of_mississippi_inc.md) | medicare_advantage |
| `2efc44e0-b96f-5d5c-9efb-35fcc6ec8642` | WELLPOINT IOWA, INC. | 1 | [2](per_fpi/wellpoint_iowa_inc.md) | medicare_advantage |
| `3568f966-dce7-58cb-812d-8f27b8a65408` | WELLPOINT WASHINGTON, INC. | 1 | [2](per_fpi/wellpoint_washington_inc.md) | medicare_advantage |
| `b5e0ce09-f479-544f-b880-a1612bcbc462` | WELLQUEST RIVER VALLEY, LLC | 1 | [2](per_fpi/wellquest_river_valley_llc.md) | medicare_advantage |
| `569d4920-f1e7-59c1-9b11-20a260da01f6` | WEST BALTIMORE PACE COMMUNITY COALITION | 1 | [2](per_fpi/west_baltimore_pace_community_coalition.md) | medicare_advantage |
| `a61fc3cc-cd55-5c67-a67a-9cae27ad040b` | myPlace Greater LA PACE Inc. | 1 | [2](per_fpi/myplace_greater_la_pace_inc.md) | medicare_advantage |
| `d5568d7e-fe22-572b-9e58-444a992d906d` | ABSOLUTE TOTAL CARE, INC. | 1 | [1](per_fpi/absolute_total_care_inc.md) | medicare_advantage |
| `a85212d5-c543-5afb-a036-e1f3379adf23` | AETNA BETTER HEALTH INC. (NJ) | 1 | [1](per_fpi/aetna_better_health_inc_nj.md) | medicare_advantage |
| `59915f0c-a88e-5fc1-b5b5-c9688f902660` | AETNA BETTER HEALTH PREMIER PLAN MMAI INC. | 1 | [1](per_fpi/aetna_better_health_premier_plan_mmai_inc.md) | medicare_advantage |
| `35bd7548-4ab6-580f-b70e-b591b7254265` | AIDS HEALTHCARE FOUNDATION | 1 | [1](per_fpi/aids_healthcare_foundation.md) | medicare_advantage |
| `c72df2a4-4cc0-5268-8cc8-a6f6772c1898` | ALAMEDA ALLIANCE FOR HEALTH | 1 | [1](per_fpi/alameda_alliance_for_health.md) | medicare_advantage |
| `a3949624-87ca-55fc-89d8-5c4a7b0a54cf` | ALLCARE HEALTH PLAN, INC. | 1 | [1](per_fpi/allcare_health_plan_inc.md) | medicare_advantage |
| `19b9ee07-50ea-5182-80cb-a5167b1e9592` | AMERICAN HEALTH PLAN OF FL, INC. | 1 | [1](per_fpi/american_health_plan_of_fl_inc.md) | medicare_advantage |
| `036a8cf6-29fc-51c7-beec-d40d3224688b` | AMERICAN HEALTH PLAN OF INDIANA INC | 1 | [1](per_fpi/american_health_plan_of_indiana_inc.md) | medicare_advantage |
| `db183419-12c5-50d8-bb54-b5fd2d416846` | AMERICAN HEALTH PLAN OF MS, INC. | 1 | [1](per_fpi/american_health_plan_of_ms_inc.md) | medicare_advantage |
| `147cd3e4-7ce2-518f-af95-9b178048a1a3` | AMERICAN HEALTH PLAN OF PENNSYLVANIA INC | 1 | [1](per_fpi/american_health_plan_of_pennsylvania_inc.md) | medicare_advantage |
| `1abb9417-7a53-514b-9514-e694db6de753` | AMERICAN HEALTH PLAN OF TX, INC. | 1 | [1](per_fpi/american_health_plan_of_tx_inc.md) | medicare_advantage |
| `b7de864c-bbc4-5c7b-9c46-1deef0f3bc29` | AMERICAN HEALTH PLAN, INC. | 1 | [1](per_fpi/american_health_plan_inc.md) | medicare_advantage |
| `4356054a-3adf-5279-8a2e-b6434018f631` | AMERIHEALTH CARITAS FLORIDA, INC. | 1 | [1](per_fpi/amerihealth_caritas_florida_inc.md) | medicare_advantage |
| `b06fbe6d-e7b2-5732-815a-827a84271b09` | AMERIHEALTH CARITAS LOUISIANA, INC. | 1 | [1](per_fpi/amerihealth_caritas_louisiana_inc.md) | medicare_advantage |
| `26e0fe3a-e3c0-535e-af9f-38ccc38f5f62` | AMERIHEALTH CARITAS NORTH CAROLINA, INC. | 1 | [1](per_fpi/amerihealth_caritas_north_carolina_inc.md) | medicare_advantage |
| `a9bc102f-0525-55d3-8496-fc0bdd25d8a1` | AMERIHEALTH MICHIGAN, INC. | 1 | [1](per_fpi/amerihealth_michigan_inc.md) | medicare_advantage |
| `b968072b-a875-5dca-b968-1ed76a1aa415` | AMH HEALTH PLANS OF MAINE, INC. | 1 | [1](per_fpi/amh_health_plans_of_maine_inc.md) | medicare_advantage |
| `b830eda5-6733-5cc6-8f10-e8abf2d029b5` | BANNER HEALTH PLAN, INC. | 1 | [1](per_fpi/banner_health_plan_inc.md) | medicare_advantage |
| `3fc1c678-7d7c-5a31-bfef-ba639409d4c8` | BUCKEYE HEALTH PLAN COMMUNITY SOLUTIONS, Inc. | 1 | [1](per_fpi/buckeye_health_plan_community_solutions_inc.md) | medicare_advantage |
| `cda44356-c83d-52c4-9f6c-aa8663a19c24` | CAREFIRST ADVANTAGE DSNP, INC. | 1 | [1](per_fpi/carefirst_advantage_dsnp_inc.md) | medicare_advantage |
| `9b956fd7-0f3e-5bac-9233-2874591f7e1c` | CARESOURCE OHIO, INC. | 1 | [1](per_fpi/caresource_ohio_inc.md) | medicare_advantage |
| `fc48f28c-4b4d-5d0e-a8c1-885efe12277d` | CENTENE VENTURE COMPANY MICHIGAN | 1 | [1](per_fpi/centene_venture_company_michigan.md) | medicare_advantage |
| `6b070f48-8f5a-5061-82be-2668174c49b6` | COMMUNITY CARE HEALTH PLAN, INC. | 1 | [1](per_fpi/community_care_health_plan_inc.md) | medicare_advantage |
| `ee8c6d23-8ce7-5661-9740-e2a698d0ba6a` | CONNECTICARE INSURANCE COMPANY, INC. | 1 | [1](per_fpi/connecticare_insurance_company_inc.md) | medicare_advantage |
| `daad03cc-f8c6-52d4-8b26-456170a58607` | CONTRA COSTA COUNTY MEDICAL SERVICE DBA CONTRA COSTA HEALTH PLAN | 1 | [1](per_fpi/contra_costa_county_medical_service_dba_contra_costa_health_plan.md) | medicare_advantage |
| `f9b4c561-14af-50e1-a571-cba36f6daab0` | COVENTRY HEALTH CARE OF VIRGINIA, INC. | 1 | [1](per_fpi/coventry_health_care_of_virginia_inc.md) | medicare_advantage |
| `a361bf4a-9fb0-5eaa-afc2-70ae4c8ac118` | DEVOTED HEALTH  PLAN OF OREGON | 1 | [1](per_fpi/devoted_health_plan_of_oregon.md) | medicare_advantage |
| `f7ab7fb8-7eb6-55ae-8bfd-b1cce1519e75` | DIGNITY CARE CORPORATION | 1 | [1](per_fpi/dignity_care_corporation.md) | medicare_advantage |
| `3fa7bee8-d4f7-57e2-a5bf-e6271e6444e2` | GEISINGER QUALITY OPTIONS, INC. | 1 | [1](per_fpi/geisinger_quality_options_inc.md) | medicare_advantage |
| `6473aade-8332-5674-b1d8-f38869f77041` | HAP CARESOURCE | 1 | [1](per_fpi/hap_caresource.md) | medicare_advantage |
| `6380ffa8-2bb2-55d9-ae72-6fe7ddcea223` | HEALTH CHOICE ARIZONA, INC. | 1 | [1](per_fpi/health_choice_arizona_inc.md) | medicare_advantage |
| `1ce4ce70-6fa0-5dab-8d25-3085a6396b3e` | HEALTH PLAN OF CAREOREGON, INC. | 1 | [1](per_fpi/health_plan_of_careoregon_inc.md) | medicare_advantage |
| `d9a598f3-208c-5795-a616-3569f2363ca1` | HEALTHFIRST INSURANCE COMPANY, INC. | 1 | [1](per_fpi/healthfirst_insurance_company_inc.md) | medicare_advantage |
| `eaca3ed6-1d8c-5db5-ab20-af87c8651f38` | HIGHMARK HEALTH OPTIONS WEST VIRGINIA INC. | 1 | [1](per_fpi/highmark_health_options_west_virginia_inc.md) | medicare_advantage |
| `37681396-0795-5f23-84ef-0d7a3baa4a70` | HMO Minnesota | 1 | [1](per_fpi/hmo_minnesota.md) | medicare_advantage |
| `eb1be3c7-5787-5e0f-97db-ed9e12ff4d51` | HORIZON HEALTHCARE OF NEW JERSEY, INC. | 1 | [1](per_fpi/horizon_healthcare_of_new_jersey_inc.md) | medicare_advantage |
| `387dce3d-56cc-58af-bc38-b60e42c5ceba` | HUMANA BENEFIT PLAN OF SOUTH CAROLINA, INC. | 1 | [1](per_fpi/humana_benefit_plan_of_south_carolina_inc.md) | medicare_advantage |
| `e5f7e470-5bd7-5ca0-8a79-7f0aaa7a4eca` | HUMANA BENEFIT PLAN OF TEXAS, INC. | 1 | [1](per_fpi/humana_benefit_plan_of_texas_inc.md) | medicare_advantage |
| `826c7416-72f5-5bf7-88af-c2bc08d42e79` | HUMANA HEALTH PLAN OF TEXAS, INC. | 1 | [1](per_fpi/humana_health_plan_of_texas_inc.md) | medicare_advantage |
| `0ed84fb5-7e56-5fa8-89cf-161369bb50d5` | HUMANA HEALTH PLAN, INC. | 1 | [1](per_fpi/humana_health_plan_inc.md) | medicare_advantage |
| `16fc6654-449a-5ac0-876b-c4ac91d723aa` | ILLINOIS BLUE CROSS BLUE SHIELD INSURANCE COMPANY | 1 | [1](per_fpi/illinois_blue_cross_blue_shield_insurance_company.md) | medicare_advantage |
| `b783e118-664f-584c-8b67-9ffd07963048` | IMPERIAL COUNTY LOCAL HEALTH AUTHORITY | 1 | [1](per_fpi/imperial_county_local_health_authority.md) | medicare_advantage |
| `9f810bfc-2cd8-5a4f-a7e2-8cface212c5e` | INDEPENDENT CARE HEALTH PLAN | 1 | [1](per_fpi/independent_care_health_plan.md) | medicare_advantage |
| `98af13c8-1f7b-52b3-8d22-57723ef080d3` | ITASCA MEDICAL CARE | 1 | [1](per_fpi/itasca_medical_care.md) | medicare_advantage |
| `a3862519-16ae-566b-98c8-c6cf5c46c92b` | Inland Empire Health Plan | 1 | [1](per_fpi/inland_empire_health_plan.md) | medicare_advantage |
| `dbe95878-5b08-5d02-a91a-342d665eb2f2` | JOHNS HOPKINS HEALTH PLAN OF VIRGINIA, INC. | 1 | [1](per_fpi/johns_hopkins_health_plan_of_virginia_inc.md) | medicare_advantage |
| `14388739-9d4c-592d-b5bd-1dc795bf6a30` | KAISER FOUNDATION HEALTH PLAN OF WASHINGTON OPTIONS INC | 1 | [1](per_fpi/kaiser_foundation_health_plan_of_washington_options_inc.md) | medicare_advantage |
| `da717792-b48e-5a3d-987b-32d90d0d1232` | KERN HEALTH SYSTEMS | 1 | [1](per_fpi/kern_health_systems.md) | medicare_advantage |
| `e6a11d3b-4cc1-53b2-8d2e-4a8346bdf5b7` | LAGNIAPPE ADVANTAGE INSURANCE COMPANY | 1 | [1](per_fpi/lagniappe_advantage_insurance_company.md) | medicare_advantage |
| `a641782e-f45f-576a-b772-d8ac01c18216` | LOCAL INITIATIVE HEALTH AUTHORITY FOR LA COUNTY | 1 | [1](per_fpi/local_initiative_health_authority_for_la_county.md) | medicare_advantage |
| `b8657f10-589f-57ae-8734-61644ad28e2c` | LONGEVITY HEALTH PLAN OF COLORADO, INC. | 1 | [1](per_fpi/longevity_health_plan_of_colorado_inc.md) | medicare_advantage |
| `8965816b-d6e8-5ca7-aee5-d95e7fd86496` | LONGEVITY HEALTH PLAN OF FLORIDA, INC. | 1 | [1](per_fpi/longevity_health_plan_of_florida_inc.md) | medicare_advantage |
| `881c8dba-6622-5c23-840a-19f599be677d` | LONGEVITY HEALTH PLAN OF ILLINOIS, INC. | 1 | [1](per_fpi/longevity_health_plan_of_illinois_inc.md) | medicare_advantage |
| `1955d5a8-aa01-5e2b-8613-c72132c7b87a` | LONGEVITY HEALTH PLAN OF MICHIGAN, INC. | 1 | [1](per_fpi/longevity_health_plan_of_michigan_inc.md) | medicare_advantage |
| `cdb1ef35-5498-5fee-b1fe-306cc47ed80d` | LONGEVITY HEALTH PLAN OF NEW YORK, INC. | 1 | [1](per_fpi/longevity_health_plan_of_new_york_inc.md) | medicare_advantage |
| `6c79d2e0-7d7c-5e19-b891-4ee2fbe726f7` | LONGEVITY HEALTH PLAN OF NORTH CAROLINA, INC. | 1 | [1](per_fpi/longevity_health_plan_of_north_carolina_inc.md) | medicare_advantage |
| `e0d51c64-f709-5c4f-b0af-2739056d7e11` | LOUISIANA HEALTHCARE CONNECTIONS, INC. | 1 | [1](per_fpi/louisiana_healthcare_connections_inc.md) | medicare_advantage |
| `5209906e-d184-525d-9f0c-ce9f878bb89d` | MAGNOLIA HEALTH PLAN, INC. | 1 | [1](per_fpi/magnolia_health_plan_inc.md) | medicare_advantage |
| `4c4dadbb-7ec4-5067-8965-5f86047cc69b` | MOLINA HEALTHCARE OF NEVADA INC | 1 | [1](per_fpi/molina_healthcare_of_nevada_inc.md) | medicare_advantage |
| `e128f224-c22a-5b2f-a165-46d1966bc0c9` | MOLINA HEALTHCARE OF SOUTH CAROLINA,INC | 1 | [1](per_fpi/molina_healthcare_of_south_carolina_inc.md) | medicare_advantage |
| `64f76a87-585c-5c93-af0f-ec64d53cc950` | OKLAHOMA SUPERIOR SELECT, INC. | 1 | [1](per_fpi/oklahoma_superior_select_inc.md) | medicare_advantage |
| `d9cf97ce-2a75-503c-8d53-6a5caa7da919` | PARAMOUNT INSURANCE COMPANY | 1 | [1](per_fpi/paramount_insurance_company.md) | medicare_advantage |
| `8d0e1e84-ff7e-5073-82ad-1e276294ae8c` | PROVIDER PARTNERS HEALTH PLAN OF ILLINOIS | 1 | [1](per_fpi/provider_partners_health_plan_of_illinois.md) | medicare_advantage |
| `858910f3-6bcd-57e0-bb4b-c0c40449ee4d` | PROVIDER PARTNERS HEALTH PLAN OF KENTUCKY | 1 | [1](per_fpi/provider_partners_health_plan_of_kentucky.md) | medicare_advantage |
| `8df5ebc9-a58d-5dbb-bc4e-269fd0379bc0` | PROVIDER PARTNERS HEALTH PLAN OF TEXAS, INC. | 1 | [1](per_fpi/provider_partners_health_plan_of_texas_inc.md) | medicare_advantage |
| `bfdcdb39-fd88-59f2-867f-64e89aefdae3` | SAMARITAN HEALTH PLANS, INC. | 1 | [1](per_fpi/samaritan_health_plans_inc.md) | medicare_advantage |
| `4cc7f3b4-7b76-5379-9a62-8ff250e10567` | SAN FRANCISCO HEALTH AUTHORITY DBA SAN FRANCISCO HEALTH PLAN | 1 | [1](per_fpi/san_francisco_health_authority_dba_san_francisco_health_plan.md) | medicare_advantage |
| `5e05e273-0eb7-5d74-aa42-4dbc5ef36f5c` | SAN JOAQUIN COUNTY HEALTH COMMISSION | 1 | [1](per_fpi/san_joaquin_county_health_commission.md) | medicare_advantage |
| `52427a1f-5b72-5d63-a8c8-dad434f013e9` | SAN MATEO HEALTH COMMISSION | 1 | [1](per_fpi/san_mateo_health_commission.md) | medicare_advantage |
| `315f813f-f320-519f-b3a9-dc0a26c52878` | SANTA BARBARA SAN LUIS OBISPO REGIONAL HEALTH AUTHORITY DBA CENCAL HEALTH | 1 | [1](per_fpi/santa_barbara_san_luis_obispo_regional_health_authority_dba_cencal_health.md) | medicare_advantage |
| `ce532baa-daae-56cd-a0a1-1b034130c3a4` | SANTA CLARA COUNTY HEALTH AUTHORITY | 1 | [1](per_fpi/santa_clara_county_health_authority.md) | medicare_advantage |
| `c61db3f1-8c52-5d83-a352-26ba5e564260` | SANTA CRUZ MONTEREY MERCED SAN BENITO MARIPOSA MANAGED MEDICAL CARE COMMISSION | 1 | [1](per_fpi/santa_cruz_monterey_merced_san_benito_mariposa_managed_medical_care_commission.md) | medicare_advantage |
| `f0d7eff2-057a-5080-bd16-e590d7d13ac4` | SELECT HEALTH OF SOUTH CAROLINA, INC. | 1 | [1](per_fpi/select_health_of_south_carolina_inc.md) | medicare_advantage |
| `13bbbf23-7625-5f84-8aa1-1cef1a5b75fb` | TSG GUARD, INC. | 1 | [1](per_fpi/tsg_guard_inc.md) | medicare_advantage |
| `03aadf7e-9e67-56f1-95d5-c46ccc959696` | UPMC HEALTH COVERAGE, INC. | 1 | [1](per_fpi/upmc_health_coverage_inc.md) | medicare_advantage |
| `c2d59b54-7335-5e34-a3f8-9356b41c13c7` | UPPER PENINSULA HEALTH PLAN, LLC | 1 | [1](per_fpi/upper_peninsula_health_plan_llc.md) | medicare_advantage |
| `2223f855-b9b0-55f7-8399-a3c78b53d3f8` | Ventura County Medi-Cal Managed Care Commission | 1 | [1](per_fpi/ventura_county_medi_cal_managed_care_commission.md) | medicare_advantage |
| `61cee842-3ddd-5253-99e2-050ff43a11ea` | WELLCARE HEALTH INSURANCE COMPANY OF AMERICA | 1 | [1](per_fpi/wellcare_health_insurance_company_of_america.md) | medicare_advantage |
| `7a07152d-c9a1-5ef8-b785-3ef3ad369d2b` | WELLCARE HEALTH INSURANCE COMPANY OF NEW JERSEY | 1 | [1](per_fpi/wellcare_health_insurance_company_of_new_jersey.md) | medicare_advantage |
| `7ad2c9e2-cd53-521b-8cd6-9dcaea8df7af` | WELLCARE OF NEW HAMPSHIRE, INC. | 1 | [1](per_fpi/wellcare_of_new_hampshire_inc.md) | medicare_advantage |
| `8956a079-acc8-5a00-a237-496f9dd75d9e` | WELLPOINT SOUTH CAROLINA, INC. | 1 | [1](per_fpi/wellpoint_south_carolina_inc.md) | medicare_advantage |
| `5f615172-4d3d-502e-9e87-6383504566cf` | WEST VIRGINIA SENIOR ADVANTAGE, INC. | 1 | [1](per_fpi/west_virginia_senior_advantage_inc.md) | medicare_advantage |
| `480ec990-421f-52a9-abc5-a891caff5c58` | AETNA BETTER HEALTH INC. (CT) | 1 | [0](per_fpi/aetna_better_health_inc_ct.md) | medicare_advantage |
| `720088af-d74d-558e-87c3-010ee7dd3222` | ALIGN SENIOR CARE IOWA INSURANCE COMPANY | 1 | [0](per_fpi/align_senior_care_iowa_insurance_company.md) | medicare_advantage |
| `11be517a-1e6c-55c0-8d84-9cb7d480803e` | AMERIHEALTH HMO, INC | 1 | [0](per_fpi/amerihealth_hmo_inc.md) | medicare_advantage |
| `f487e10a-cfde-53e0-84fb-8a8adca3c78c` | C AND O EMPLOYEES' HOSPITAL ASSOCIATION | 1 | [0](per_fpi/c_and_o_employees_hospital_association.md) | medicare_advantage |
| `2fdb1bcd-8ed0-5ffa-ac57-23e88f0466a5` | CONSOLIDATED ASSOC OF RAILROAD EMPLOYEES HC | 1 | [0](per_fpi/consolidated_assoc_of_railroad_employees_hc.md) | medicare_advantage |
| `7007873f-1f80-5f5f-a19d-09628b4b698f` | DEVOTED HEALTH INSURANCE COMPANY OF CONNECTICUT | 1 | [0](per_fpi/devoted_health_insurance_company_of_connecticut.md) | medicare_advantage |
| `5a55ceb7-2770-53a0-bdce-3823a19d2b89` | DEVOTED HEALTH INSURANCE COMPANY OF MICHIGAN | 1 | [0](per_fpi/devoted_health_insurance_company_of_michigan.md) | medicare_advantage |
| `974ec651-77af-50b9-b18e-f7239c8c465e` | DEVOTED HEALTH INSURANCE COMPANY OF MISSOURI | 1 | [0](per_fpi/devoted_health_insurance_company_of_missouri.md) | medicare_advantage |
| `0e219156-fded-55f2-8763-f8da04094772` | DEVOTED HEALTH INSURANCE COMPANY OF NEW HAMPSHIRE | 1 | [0](per_fpi/devoted_health_insurance_company_of_new_hampshire.md) | medicare_advantage |
| `3ba2a491-c627-5a6a-9a02-e3a0aff63967` | DEVOTED HEALTH INSURANCE COMPANY OF NEW JERSEY | 1 | [0](per_fpi/devoted_health_insurance_company_of_new_jersey.md) | medicare_advantage |
| `2ba2fe07-8207-566a-b181-ec32579bf082` | DEVOTED HEALTH INSURANCE COMPANY OF NEW YORK | 1 | [0](per_fpi/devoted_health_insurance_company_of_new_york.md) | medicare_advantage |
| `5f082005-058a-5f7c-bb00-d7248cb280ee` | DEVOTED HEALTH PLAN OF WASHINGTON, INC. | 1 | [0](per_fpi/devoted_health_plan_of_washington_inc.md) | medicare_advantage |
| `3d5df28d-7e6a-5395-976d-a0f4f5807ec4` | HUMANA HEALTH PLAN OF CALIFORNIA, INC. | 1 | [0](per_fpi/humana_health_plan_of_california_inc.md) | medicare_advantage |
| `0c33b0ec-88e8-5578-a8ff-10c680fc6d1f` | HUMANADENTAL INSURANCE COMPANY | 1 | [0](per_fpi/humanadental_insurance_company.md) | medicare_advantage |
| `d89162b5-2c4f-50c3-930a-2367985f9e29` | MEDCARE PARTNERS HEALTH PLAN OF TEXAS, LLC | 1 | [0](per_fpi/medcare_partners_health_plan_of_texas_llc.md) | medicare_advantage |
| `cee2fbd7-9ba5-5f9d-bc71-9a33c62e22f9` | MOLINA HEALTHCARE OF IOWA, INC. | 1 | [0](per_fpi/molina_healthcare_of_iowa_inc.md) | medicare_advantage |
| `bc19a007-d5a5-5e77-8dc1-beb345adf309` | MOLINA HEALTHCARE OF NEBRASKA, INC. | 1 | [0](per_fpi/molina_healthcare_of_nebraska_inc.md) | medicare_advantage |
| `bfb0ab2c-a60a-589c-ab37-d4ba7377eddb` | MOLINA HEALTHCARE OF NEW MEXICO, INC. | 1 | [0](per_fpi/molina_healthcare_of_new_mexico_inc.md) | medicare_advantage |
| `020e6e4d-8eb8-56a1-a91d-616471ee30d2` | MULTICARE HEALTH PLAN | 1 | [0](per_fpi/multicare_health_plan.md) | medicare_advantage |
| `b4ccc9fa-1972-578f-9581-fffc911e8f5f` | NATIVE ADVANTAGE, INC. | 1 | [0](per_fpi/native_advantage_inc.md) | medicare_advantage |
| `25daac3a-c4fb-579d-b83b-cae93ccc5812` | NY HOTEL TRADES COUNCIL & HOTEL ASSOCIATION OF NYC | 1 | [0](per_fpi/ny_hotel_trades_council_hotel_association_of_nyc.md) | medicare_advantage |
| `62091daa-3b73-55f8-baf9-4354b39765e8` | RANGE HEALTH, INC. | 1 | [0](per_fpi/range_health_inc.md) | medicare_advantage |
| `6b357203-5fc2-539d-a1d8-9869e55316bc` | SCAN HEALTH PLAN (OR) | 1 | [0](per_fpi/scan_health_plan_or.md) | medicare_advantage |
| `e105b254-c0bf-5d55-9eed-9160a85409ab` | ST. LUKE'S HEALTH PLAN, INC. | 1 | [0](per_fpi/st_luke_s_health_plan_inc.md) | medicare_advantage |
| `09630ef2-1b25-551c-99d8-adaa567f6489` | UNION HEALTH SERVICES, INC. | 1 | [0](per_fpi/union_health_services_inc.md) | medicare_advantage |
| `28122919-e0d1-52f8-8589-113fa8223676` | UNITED MINE WORKERS OF AMERICA HLTH & RETIREMENT | 1 | [0](per_fpi/united_mine_workers_of_america_hlth_retirement.md) | medicare_advantage |
| `6b132572-bc60-5b63-b2f6-5b81929f6e7f` | VNA HOMECARE OPTIONS, LLC | 1 | [0](per_fpi/vna_homecare_options_llc.md) | medicare_advantage |

## Redirect / Tombstone Files

These files carry a retired FPI in their filename and contain only a `new_file` pointer to the payer's current well-known file:

- `medicare_advantage/aetna_better_health_of_texas_inc/aetna_better_health_of_texas_inc_b8010e50-6078-5f92-b303-db16d1ae5047.well_known_payer.json` → `payer_index_files/medicare_advantage/aetna_better_health_of_texas_inc/aetna_better_health_of_texas_inc_3f9af4c3-d735-5c9b-9674-33cdd1864d6b.well_known_payer.json`
- `medicare_advantage/aetna_health_and_life_insurance_company/aetna_health_and_life_insurance_company_e9928c4d-f9ca-5b5e-ba83-0d0d46099771.well_known_payer.json` → `payer_index_files/medicare_advantage/aetna_health_and_life_insurance_company/aetna_health_and_life_insurance_company_68d4ceb9-93f6-548c-912b-f9f43eb79683.well_known_payer.json`
- `medicare_advantage/aetna_health_inc_tx/aetna_health_inc_tx_fbf6a17b-f8df-5772-9ddc-692b912af2b7.well_known_payer.json` → `payer_index_files/medicare_advantage/aetna_health_inc_tx/aetna_health_inc_tx_b1affe56-4f6e-59a1-893e-f611f1dd8b5b.well_known_payer.json`
- `medicare_advantage/aetna_life_insurance_company/aetna_life_insurance_company_72c771e1-464f-51d6-b6e3-1c2deaef5e50.well_known_payer.json` → `payer_index_files/medicare_advantage/aetna_life_insurance_company/aetna_life_insurance_company_a04283f0-5a1d-5df8-a744-e252652a1783.well_known_payer.json`

