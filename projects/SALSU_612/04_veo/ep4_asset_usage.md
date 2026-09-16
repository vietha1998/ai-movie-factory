# 4화 「평양」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)
> Đếm theo `04_veo/scenes_ep4.json` (287 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.

## 1. Nhân vật (CHAR) — số SC xuất hiện
| CHAR | SC | Derived state trong 4화 (SC) |
|---|---|---|
| CHAR_001 | 42 | CHAR_001_reeds_ep4 (42) |
| CHAR_002 | 23 | CHAR_002_reeds_ep4 (23) |
| CHAR_003 | 15 | CHAR_003_reeds_ep4 (15) |
| CHAR_004 | 18 | CHAR_004_braid_ep4 (18) |
| CHAR_005 | 25 | CHAR_005_cage_ep4 (19), CHAR_005_helmet_ep4 (5), CHAR_005_rescued_ep4 (1) |
| CHAR_006 | 42 | CHAR_006_mudface_ep4 (10), CHAR_006_raid_hemp_ep4 (19), CHAR_006_reeds_ep4 (13) |
| CHAR_101 | 10 | CHAR_101_helmet_off_tent (2), CHAR_101_rain_ep4 (8) |
| CHAR_102 | 5 | CHAR_102_hall_ep4 (5) |
| CHAR_103 | 12 | CHAR_103_ambush_ep4 (4), CHAR_103_council_ep4 (3), CHAR_103_helmet_off (2), CHAR_103_rain_ep4 (3) |
| CHAR_105 | 23 | CHAR_105_radio_ep3 (23) |
| CHAR_106 | 10 | CHAR_106_reeds_ep4 (10) |
| CHAR_107 | 25 | CHAR_107_fog_trail_ep4 (11), CHAR_107_reedcutter_ep4 (8), CHAR_107_scarf_ep2 (6) |
| CHAR_202 | 15 | CHAR_202_rain_ep4 (4), CHAR_202_tent_ep4 (4), CHAR_202_tent_plain_ep4 (7) |
| CHAR_203 | 9 | CHAR_203_rain_ep4 (9) |
| CHAR_204 | 6 | CHAR_204_ambush_ep4 (2), CHAR_204_landing_ep4 (4) |
| CHAR_205 | 21 | CHAR_205_bandaged_day_ep4 (4), CHAR_205_bandaged_night_ep4 (1), CHAR_205_bareheaded_ep4 (1), CHAR_205_capless_night_ep4 (1), CHAR_205_fog_ep4 (6), CHAR_205_night_hunt_ep4 (2), CHAR_205_nvg_ep3 (1), CHAR_205_retreat_ep4 (5) |

### Trạng thái trong tập do veo đặt (không có trong character_bible — đề xuất character-designer nhập DERIVED_STATES; ref đính = ref gần nhất)
| state_id | CHAR | ref đính | câu trạng thái |
|---|---|---|---|
| CHAR_003_reeds_ep4 | CHAR_003 | CHAR_003_rain_ep3 | Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. |
| CHAR_005_cage_ep4 | CHAR_005 | CHAR_005_captive_ep3 | Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. |
| CHAR_005_helmet_ep4 | CHAR_005 | CHAR_005_goguryeo_helmet_ep5 | Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief. |
| CHAR_006_reeds_ep4 | CHAR_006 | CHAR_006_ref | Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. |
| CHAR_006_mudface_ep4 | CHAR_006 | CHAR_006_ref | Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. |
| CHAR_006_raid_hemp_ep4 | CHAR_006 | CHAR_006_night_raid_ep4 | No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. |
| CHAR_101_rain_ep4 | CHAR_101 | CHAR_101_salsu_rain_ep5 | Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. |
| CHAR_102_hall_ep4 | CHAR_102 | CHAR_102_wall_night_ep4 | A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps. |
| CHAR_103_rain_ep4 | CHAR_103 | CHAR_103_ref | Armor and blue jacket dark with rain, water running from the red crest, round shield slung on the back, mud on the boots. |
| CHAR_103_council_ep4 | CHAR_103 | CHAR_103_ambush_ep4 | Helmet carried under one arm, black topknot loosened, smoke smudges on face and armor, right forearm wrapped in a cloth bandage, no shield, wet armor. |
| CHAR_106_reeds_ep4 | CHAR_106 | CHAR_106_ref | Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. |
| CHAR_107_reedcutter_ep4 | CHAR_107 | CHAR_107_scarf_ep2 | Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. |
| CHAR_107_fog_trail_ep4 | CHAR_107 | CHAR_107_night_trail_ep4 | Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. |
| CHAR_202_rain_ep4 | CHAR_202 | CHAR_202_ref | Armor and breast mirrors streaming with rain, red cloak heavy with water, white beard dripping, mud splashed to the thighs. |
| CHAR_202_tent_plain_ep4 | CHAR_202 | CHAR_202_tent_ep4 | Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. |
| CHAR_203_rain_ep4 | CHAR_203 | CHAR_203_ref | Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. |
| CHAR_205_capless_night_ep4 | CHAR_205 | CHAR_205_night_hunt_ep4 | Fox-fur cap lost, braid exposed and dripping, night-vision monocular knocked askew over the right eye, wet dark cloak over the armor, mud on the knees, a fresh cut on the right forearm, turning to flee. |
| CHAR_205_bareheaded_ep4 | CHAR_205 | CHAR_205_night_hunt_ep4 | Fox-fur cap lost, braid exposed and dripping, wet dark cloak over the armor, mud to the thighs, a fresh cut on the right forearm, the night-vision monocular held in one hand on its strap. |
| CHAR_205_bandaged_day_ep4 | CHAR_205 | CHAR_205_nvg_ep3 | A modern night-vision monocular device mounted on the front of a fox-fur cap, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud on boots. |
| CHAR_205_bandaged_night_ep4 | CHAR_205 | CHAR_205_night_hunt_ep4 | Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, the right forearm wrapped in a grey cloth bandage. |
| CHAR_205_fog_ep4 | CHAR_205 | CHAR_205_ref | No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. |
| CHAR_205_retreat_ep4 | CHAR_205 | CHAR_205_nvg_ep3 | Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs. |

### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)
| Extra | SC |
|---|---|
| GOG_CAVALRYMEN | 18 |
| ROK_RAIDERS_2 | 13 |
| XIANBEI_RIDER | 12 |
| SUI_SOLDIERS_STARVING | 11 |
| ROK_SOLDIERS | 11 |
| XIANBEI_RIDERS_FOOT | 11 |
| VILLAGE_WOMEN | 8 |
| SUI_SOLDIERS_LOOTING | 8 |
| GOG_INFANTRY | 7 |
| ROK_WOUNDED | 7 |
| GOG_OFFICER | 6 |
| ROK_SENTRY_PLAIN | 6 |
| ROK_SOLDIER | 5 |
| OXEN_CARTS | 5 |
| SUI_OFFICER_MOUNTED | 4 |
| ROK_SENTRY_NVG | 4 |
| SUI_COURIER | 4 |
| DOG | 4 |
| SUI_SOLDIER_BACK | 3 |
| SUI_OFFICER | 3 |
| SUI_SENTRY | 3 |
| GOG_ARCHERS | 3 |
| SUI_TORCHBEARERS | 3 |
| GOG_ENVOY | 3 |
| XIANBEI_GUARDS_2 | 3 |
| SUI_FEET | 2 |
| SUI_STRAGGLERS | 2 |
| XIANBEI_DEPUTY | 2 |
| SUI_ARCHERS | 2 |
| GOG_FLAGBEARER | 2 |
| SUI_MARINES | 1 |
| SUI_NAVAL_DEPUTY | 1 |
| GOG_GUARDS | 1 |
| GOG_INTERPRETER | 1 |
| XIANBEI_OFFICER_TORCH | 1 |
| ROK_MORTAR_CREW | 1 |
| ROK_PZF_GUNNERS | 1 |

## 2. Địa điểm (LOC) — số SC
| LOC | SC | Sub-lock (SC) |
|---|---|---|
| LOC_006 | 40 | LOC_006 (1), LOC_006_alley (2), LOC_006_estuary (1), LOC_006_gate_tower (1), LOC_006_gate_yard (1), LOC_006_haepo (1), LOC_006_hall (8), LOC_006_hall_corridor (1), LOC_006_landing (6), LOC_006_market (5), LOC_006_river_burning (1), LOC_006_river_road_night (1), LOC_006_rooftops (1), LOC_006_temple_doors (1), LOC_006_temple_int (4), LOC_006_warship_bow (1), LOC_006_water_gate (4) |
| LOC_007 | 200 | LOC_007_aerial (5), LOC_007_aerial_night (1), LOC_007_aid (9), LOC_007_cage (5), LOC_007_camp_east_fog (2), LOC_007_camp_fog (4), LOC_007_channel_fog (5), LOC_007_channel_north_fog (2), LOC_007_channel_south (1), LOC_007_east_meadow_fog (3), LOC_007_ford_mouth (2), LOC_007_island1 (15), LOC_007_island1_abandoned (2), LOC_007_island1_k2 (7), LOC_007_island2 (9), LOC_007_island2_k2 (14), LOC_007_island_edge (16), LOC_007_marsh_night (5), LOC_007_north_ford (7), LOC_007_outpost (7), LOC_007_reed_path (8), LOC_007_reed_path_fog (8), LOC_007_reeds_ford (9), LOC_007_retreat_path (1), LOC_007_river_fog (1), LOC_007_river_surface (1), LOC_007_sandbar_mid (2), LOC_007_sandbar_north_fog (3), LOC_007_sandtable (6), LOC_007_shelter (15), LOC_007_south_camp (1), LOC_007_south_hills (1), LOC_007_south_horses (1), LOC_007_south_sentry_fog (1), LOC_007_south_shore (4), LOC_007_stake (8), LOC_007_tent_tuoba (1), LOC_007_water_point (8) |
| LOC_008 | 47 | LOC_008_aerial_north (1), LOC_008_fields (1), LOC_008_gog_camp_hill (1), LOC_008_gog_tent (2), LOC_008_hills_rain (3), LOC_008_hillside_rock (1), LOC_008_hilltop (1), LOC_008_knoll (2), LOC_008_mud_road_night (1), LOC_008_road_column (3), LOC_008_road_west (1), LOC_008_square (3), LOC_008_square_head (5), LOC_008_square_inside (2), LOC_008_sui_camp_cook (1), LOC_008_sui_camp_edge (1), LOC_008_sui_camp_gate (1), LOC_008_sui_camp_mountain (2), LOC_008_sui_tent (14), LOC_008_sui_tent_door (1) |

## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/EQP) — số SC
| ID | SC | ghi chú |
|---|---|---|
| WPN_201 | 32 |  |
| EQP_001 | 29 |  |
| VEH_001 | 28 |  |
| VEH_101 | 21 |  |
| VEH_206 | 17 |  |
| WPN_001 | 15 |  |
| EQP_002 | 14 |  |
| VEH_207 | 11 | **LOCK_PENDING** — lock tạm build.py, cần world-designer khóa continuity_master |
| VEH_204 | 9 |  |
| WPN_003 | 9 |  |
| WPN_101 | 6 |  |
| WPN_004 | 6 |  |
| WPN_002 | 3 |  |
| WPN_005 | 3 |  |
| VEH_002 | 1 |  |

## 4. Đạo cụ (PROP) — số SC
| PROP | SC |
|---|---|
| PROP_020 | 26 |
| PROP_021 | 17 |
| PROP_018 | 9 |
| PROP_009 | 8 |
| PROP_013 | 8 |
| PROP_016 | 8 |
| PROP_012 | 7 |
| PROP_014 | 7 |
| PROP_001 | 6 |
| PROP_015 | 6 |
| PROP_006 | 4 |
| PROP_008 | 3 |
| PROP_010 | 2 |
| PROP_017 | 2 |
| PROP_011 | 1 |
| PROP_019 | 1 |

## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)
| # | ref id | thư mục | số SC đính | trạng thái |
|---|---|---|---|---|
| 1 | LOC_007_island_ep4 | locations | 93 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 2 | WPN_201_ref | vehicles | 45 | có job |
| 3 | CHAR_001_reeds_ep4 | characters | 42 | có job |
| 4 | LOC_007_detail | locations | 33 | có job |
| 5 | VEH_206_ref | vehicles | 32 | có job |
| 6 | LOC_007_south_camp_ep4 | locations | 29 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 7 | EQP_001_ref | vehicles | 29 | có job |
| 8 | VEH_001_ref | vehicles | 28 | có job |
| 9 | LOC_008_hills_rain_ep4 | locations | 25 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 10 | CHAR_002_reeds_ep4 | characters | 23 | có job |
| 11 | CHAR_006_ref | characters | 23 | có job |
| 12 | CHAR_105_radio_ep3 | characters | 23 | có job |
| 13 | LOC_007_fog_ep4 | locations | 22 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 14 | VEH_101_ref | vehicles | 21 | có job |
| 15 | CHAR_005_captive_ep3 | characters | 20 | có job |
| 16 | CHAR_006_night_raid_ep4 | characters | 19 | có job |
| 17 | CHAR_004_braid_ep4 | characters | 18 | có job |
| 18 | PROP_021_ref | props | 17 | có job |
| 19 | LOC_006_wide | locations | 17 | có job |
| 20 | WPN_001_ref | vehicles | 15 | có job |
| 21 | CHAR_003_rain_ep3 | characters | 15 | có job |
| 22 | LOC_008_sui_tent_ep4 | locations | 15 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 23 | CHAR_107_scarf_ep2 | characters | 14 | có job |
| 24 | EQP_002_ref | vehicles | 14 | có job |
| 25 | WPN_102_ref | vehicles | 14 | có job |
| 26 | LOC_007_marsh_night_ep4 | locations | 14 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 27 | VEH_207_ref | vehicles | 11 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 28 | CHAR_202_tent_ep4 | characters | 11 | có job |
| 29 | CHAR_107_night_trail_ep4 | characters | 11 | có job |
| 30 | CHAR_106_ref | characters | 10 | có job |
| 31 | CHAR_205_nvg_ep3 | characters | 10 | có job |
| 32 | PROP_018_ref | props | 9 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 33 | VEH_204_ref | vehicles | 9 | có job |
| 34 | CHAR_103_ambush_ep4 | characters | 9 | có job |
| 35 | CHAR_203_ref | characters | 9 | có job |
| 36 | LOC_006_interior | locations | 9 | có job |
| 37 | WPN_003_ref | vehicles | 9 | có job |
| 38 | LOC_007_wide | locations | 8 | có job |
| 39 | CHAR_101_salsu_rain_ep5 | characters | 8 | có job |
| 40 | EXTRA_village_women_ref | characters | 8 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 41 | PROP_009_ref | props | 8 | có job |
| 42 | LOC_006_market_ep4 | locations | 8 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 43 | PROP_013_ref | props | 8 | có job |
| 44 | PROP_012_ref | props | 7 | có job |
| 45 | EXTRA_rok_wounded_ref | characters | 7 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 46 | PROP_014_ref | props | 7 | có job |
| 47 | WPN_101_ref | vehicles | 6 | có job |
| 48 | PROP_001_ref | props | 6 | có job |
| 49 | PROP_015_ref | props | 6 | có job |
| 50 | WPN_004_ref | vehicles | 6 | có job |
| 51 | CHAR_205_ref | characters | 6 | có job |
| 52 | LOC_006_detail | locations | 5 | có job |
| 53 | CHAR_205_night_hunt_ep4 | characters | 5 | có job |
| 54 | LOC_008_sui_camp_ep4 | locations | 5 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 55 | CHAR_102_wall_night_ep4 | characters | 5 | có job |
| 56 | CHAR_005_goguryeo_helmet_ep5 | characters | 5 | có job |
| 57 | CHAR_202_ref | characters | 4 | có job |
| 58 | CHAR_204_ref | characters | 4 | có job |
| 59 | PROP_006_ref | props | 4 | có job |
| 60 | EXTRA_sui_courier_ref | characters | 4 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 61 | WPN_002_ref | vehicles | 3 | có job |
| 62 | WPN_005_ref | vehicles | 3 | có job |
| 63 | PROP_008_ref | props | 3 | có job |
| 64 | CHAR_103_ref | characters | 3 | có job |
| 65 | EXTRA_gog_envoy_ref | characters | 3 | **CHƯA CÓ — job trong ref_jobs_ep4_extra.json** |
| 66 | PROP_010_ref | props | 2 | có job |
| 67 | CHAR_204_ambush_ep4 | characters | 2 | có job |
| 68 | PROP_017_ref | props | 2 | có job |
| 69 | CHAR_101_ref | characters | 2 | có job |
| 70 | PROP_011_ref | props | 1 | có job |
| 71 | PROP_019_ref | props | 1 | có job |
| 72 | VEH_002_captured | vehicles | 1 | có job |

### Ref CHƯA CÓ (job: `05_references/extra/ref_jobs_ep4_extra.json` — glabs-operator tạo trước lô ảnh cảnh)
- `LOC_007_island_ep4` (locations, 16:9): đảo lau (đảo 1 & 2): gò đất thấp giữa lau ngập, mái lau bó tạm, K2 = mô bùn cắm lau — sub-lock `LOC_007_island1`/`_island2`/`_shelter`/`_k2`/`_aid`/`_sandtable` (≈100 SC).
- `LOC_007_south_camp_ep4` (locations, 16:9): trại hậu quân Tùy bờ nam: lều da/nỉ, xe bò chở hòm, ngựa buộc, gốc liễu + cũi tre — sub-lock `LOC_007_south_camp`/`_cage`/`_south_shore`/`_water_point`/`_camp_fog`…
- `LOC_007_fog_ep4` (locations, 16:9): sông 살수 rạng đông D7 sương trắng đặc, chỉ ngọn lau nhô — sub-lock `LOC_007_river_fog`/`_reed_path_fog`/`_channel_fog`/`_sandbar_north_fog` (P10).
- `LOC_007_marsh_night_ep4` (locations, 16:9): đầm lau bờ bắc đêm mưa, nước đen tới đùi, không đuốc — sub-lock `LOC_007_marsh_night`/`_outpost`/`_torch_line`/`_channel_south`/`_retreat_path` (P4, P7).
- `LOC_008_hills_rain_ep4` (locations, 16:9): đồi xanh mưa bắc 평양, đường lầy trong thung — sub-lock `LOC_008_hills_rain`/`_road_column`/`_hilltop`/`_square*`/`_knoll` (P2, P5–P7, P9, P11–P12). KHÔNG phải làng núi LOC_008 gốc.
- `LOC_008_sui_tent_ep4` (locations, 16:9): nội thất lều 우중문 dựa núi: vách da, ghế gấp, bàn bản đồ da, đèn dầu, giá kiếm — sub-lock `LOC_008_sui_tent`/`_door` (16 SC).
- `LOC_008_sui_camp_ep4` (locations, 16:9): trại Tùy 30리 dựa núi trong mưa, hàng vạn lều, khói bếp thưa — sub-lock `LOC_008_sui_camp_mountain`/`_gate`/`_cook`/`_edge`.
- `LOC_006_market_ep4` (locations, 16:9): phố chợ ngoại thành 평양 bỏ trống trong mưa: sạp lụa, vò rượu, xe bò, ngõ hẹp tới cửa chùa — sub-lock `LOC_006_market`/`_alley`/`_rooftops`.
- `VEH_207_ref` (vehicles, 16:9): **LOCK_PENDING** kỵ binh Tùy (tướng/sĩ quan/전령 trên ngựa Hán, yên cao, giáp 명광개) — decisions sau QC 5화; prompt = lock tạm build.py.
- `PROP_018_ref` (props, 16:9): tù và sừng trâu đen có **7 vạch khắc** trên cán (SC_016/124/193/225/226) — chi tiết nhận diện cần ref.
- `EXTRA_village_women_ref` (characters, 16:9): 5 bà làng bờ bắc (áo gai, khăn đầu, váy buộc gối, rổ đậy lá, liềm) — 9 SC (P2, P10).
- `EXTRA_rok_wounded_ref` (characters, 3:4): 부상병 trúng tên bụng (mặt tròn, ~22) — 6 SC (P7, P8, P11) thấy mặt → cần ref để không drift.
- `EXTRA_gog_envoy_ref` (characters, 3:4): 사자 Goguryeo (áo bào không giáp, cờ trắng cuộn) — 3 SC (P9).
- `EXTRA_sui_courier_ref` (characters, 3:4): 전령 Tùy kỵ mã (bùn tới ngực) — 3 SC (P5, P7).

### Thứ tự chạy ref đề xuất (P1 → P3)
- **P1 (≥15 SC):** LOC_007_island_ep4, WPN_201_ref, CHAR_001_reeds_ep4, LOC_007_detail, VEH_206_ref, LOC_007_south_camp_ep4, EQP_001_ref, VEH_001_ref, LOC_008_hills_rain_ep4, CHAR_002_reeds_ep4, CHAR_006_ref, CHAR_105_radio_ep3, LOC_007_fog_ep4, VEH_101_ref, CHAR_005_captive_ep3, CHAR_006_night_raid_ep4, CHAR_004_braid_ep4, PROP_021_ref, LOC_006_wide, WPN_001_ref, CHAR_003_rain_ep3, LOC_008_sui_tent_ep4
- **P2 (5–14 SC):** CHAR_107_scarf_ep2, EQP_002_ref, WPN_102_ref, LOC_007_marsh_night_ep4, VEH_207_ref, CHAR_202_tent_ep4, CHAR_107_night_trail_ep4, CHAR_106_ref, CHAR_205_nvg_ep3, PROP_018_ref, VEH_204_ref, CHAR_103_ambush_ep4, CHAR_203_ref, LOC_006_interior, WPN_003_ref, LOC_007_wide, CHAR_101_salsu_rain_ep5, EXTRA_village_women_ref, PROP_009_ref, LOC_006_market_ep4, PROP_013_ref, PROP_012_ref, EXTRA_rok_wounded_ref, PROP_014_ref, WPN_101_ref, PROP_001_ref, PROP_015_ref, WPN_004_ref, CHAR_205_ref, LOC_006_detail, CHAR_205_night_hunt_ep4, LOC_008_sui_camp_ep4, CHAR_102_wall_night_ep4, CHAR_005_goguryeo_helmet_ep5
- **P3 (<5 SC):** CHAR_202_ref, CHAR_204_ref, PROP_006_ref, EXTRA_sui_courier_ref, WPN_002_ref, WPN_005_ref, PROP_008_ref, CHAR_103_ref, EXTRA_gog_envoy_ref, PROP_010_ref, CHAR_204_ambush_ep4, PROP_017_ref, CHAR_101_ref, PROP_011_ref, PROP_019_ref, VEH_002_captured

## 6. SC cần ảnh ĐẠI QUÂN / AERIAL (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)
| SC | t | type | nội dung |
|---|---|---|---|
| SC_005 | 0:32 | video8s | Medium-high aerial, slow lateral drift along the column |
| SC_010 | 1:12 | still_kenburns | Still for ken-burns: very high aerial, slow pull-out |
| SC_012 | 1:30 | still_kenburns | Still for ken-burns: high aerial over the south bank, slow slide from the river southward |
| SC_014 | 1:48 | video8s | Wide lateral tracking shot at slope height, no close-ups |
| SC_018 | 2:22 | still_kenburns | Still for ken-burns: high aerial over grey sea, slow pull from open water into the river mouth |
| SC_041 | 5:36 | still_kenburns | Still for ken-burns: high aerial over the south bank, slow pull from the carts to the whole shore |
| SC_052 | 7:08 | still_kenburns | Still for ken-burns: high aerial in rain, slow pull from the ships up to the fortress |
| SC_053 | 7:18 | video8s | Wide shot on the beach, static, no close-ups of casualties |
| SC_056 | 7:42 | video8s | Medium-high aerial along the ranks, slow drift, no end to the ranks in frame |
| SC_075 | 10:18 | still_kenburns | Still for ken-burns: high aerial at night in rain, very slow pull-out |
| SC_076 | 10:30 | still_kenburns | Still for ken-burns: high aerial in rain, slow slide from the gate into the streets |
| SC_082 | 11:20 | video8s | Wide from the middle of the street facing the temple, static |
| SC_087 | 12:00 | video8s | Medium-high aerial over the gate and beach, static |
| SC_088 | 12:08 | video8s | Wide from the beach toward the water, static |
| SC_091 | 12:32 | still_kenburns | Still for ken-burns: wide from the flames out to the river, slow pull |
| SC_093 | 12:50 | still_kenburns | Still for ken-burns: high aerial over a grey bay, slow pull-out to open sea |
| SC_101 | 14:00 | still_kenburns | Still for ken-burns: high aerial in rain, slow pull-out |
| SC_130 | 18:02 | still_kenburns | Still for ken-burns: wide on the night shore, slow slide along the line of fire |
| SC_134 | 18:35 | video8s | Wide, backlit by torches behind the ranks, static — only silhouettes and bows |
| SC_144 | 19:55 | video8s | Wide from the island across the water to the ford mouth, static (keyframe = beat B) |
| SC_145 | 20:03 | video8s | Medium-high aerial over the ford mouth, static |
| SC_181 | 25:10 | video8s | Wide, static |
| SC_185 | 25:42 | still_kenburns | Still for ken-burns: high aerial at rainy dusk, slow pull-out |
| SC_226 | 31:16 | video8s | Low wide as the cavalry burst from the fog, static (keyframe = beat B) |
| SC_227 | 31:24 | video8s | Wide, static |
| SC_239 | 33:00 | video8s | Lateral tracking shot at water level |
| SC_241 | 33:16 | video8s | Wide over the channel, static (keyframe = beat B) |
| SC_259 | 35:44 | still_kenburns | Still for ken-burns: high aerial in rain, slow slide along the train |
| SC_260 | 35:54 | video8s | Medium-high aerial, static |
| SC_271 | 37:30 | still_kenburns | Still for ken-burns: very high aerial in rain, slow pull-out to the northern horizon |
| SC_272 | 37:40 | video8s | Wide, static, rain |
| SC_276 | 38:14 | still_kenburns | Still for ken-burns: aerial in rain, slow slide along the line of stakes |
| SC_283 | 39:16 | video8s | High aerial, slow drift from the square to the silver band |
| SC_286 | 39:42 | still_kenburns | Still for ken-burns: aerial at rainy dusk, very slow pull-out |

## 7. OVERLAY ở edit (chữ/số KHÔNG vẽ trong ảnh)
| SC | overlay |
|---|---|
| SC_033 | 92 · 8 · 20km · 50 · 9 · 10 (30%) · 50% · 0 (cột số sổ 박기철, giọt mưa nhòe số 0) |
| SC_143 | 잔탄 08 (màn hình trưởng xe, beat B — ô readout trống trong ảnh) |
| SC_144 | 잔탄 07 (nháy ở góc khung cuối beat B) |
| SC_145 | 잔탄 06 (nháy — kết clip, dùng lại ảnh màn hình insert SC_143) |
| SC_153 | 잔탄 06 · 위성 0개 (hai ô readout trống trên màn hình trưởng xe) |
| SC_159 | 항생제 0 · 모르핀 9 · 붕대… (sổ y tế 서아; ken-burns đẩy vào số 0) |
| SC_177 | 神策究天文 / 妙算窮地理 + phụ đề Hàn 「신책구천문 · 묘산궁지리」 |
| SC_178 | 戰勝功既高 / 知足願云止 + phụ đề Hàn 「전승공기고 · 지족원운지」 |
| SC_254 | 92 → 91 · 30 → 20 (gạch số cũ, viết số mới cạnh — sổ 박기철) |
| SC_279 | 잔탄 06 (màn hình trưởng xe qua cửa tháp hé) |
| SC_287 | 살수 612 · 5화 살수 (最終話) — end card trắng trên đen |

## 8. 2-BEAT / INSERT_CLIP (clip tách riêng 3–4 s, ghép ở edit)
| SC | insert (s) | nội dung insert |
|---|---|---|
| SC_139 | 4 | Beat A insert, 4 s, close on the eastern torch line at night in rain: mortar bombs burst along the line of torches in the flooded reeds, water and mud geysering… |
| SC_143 | 4 | Beat B insert, 4 s, extreme close-up inside the turret at night: the commander's cold blue screen showing a small blank readout box with no readable characters,… |
| SC_144 | 3 | Beat A insert, 3 s, close on the tank's gun muzzle at night in rain: the 120mm gun fires — a white-orange flash tears the wet night open for one instant, reeds … |
| SC_209 | 4 | Beat A insert, 4 s, close-up in fog: the first sleeping guard slumps forward into the arms of the mud-faced scout in a hemp jacket without ever opening his eyes… |
| SC_215 | 3 | Beat A insert, 3 s, extreme close-up on a brown dog's muzzle in fog: it barks furiously, the sound ringing in the whiteness, and lunges toward the edge of the w… |
| SC_226 | 3 | Beat A insert, 3 s, extreme close-up in fog: lips on the bronze mouthpiece of a black buffalo-horn trumpet, one long deep note. Sound: a long low horn call roll… |
| SC_231 | 4 | Beat B insert, 4 s, wide at the mouth of the reed passage in thinning fog: the churned brown water goes still, ripples spreading out, and one arm in brown leath… |
| SC_240 | 4 | Beat A insert, 4 s, close-up on the sandbar: an armored Goguryeo gauntlet hauls a thin boy in a torn camouflage uniform up across a saddle; a girl in a hemp jac… |
| SC_241 | 3 | Beat A insert, 3 s, close on the muzzle of a heavy machine gun in a reed hole on the north bank: a long burst, muzzle flame flickering, spent brass casings flyi… |

## 9. SC RỦI RO AI & cách né trong prompt
| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |
|---|---|---|
| SC_001 | cận mắt + móng ngựa | 1 mắt, 1 móng, máy tĩnh; không thấy toàn thân ngựa (né deformed legs) |
| SC_002 | đám đông chân | chỉ chân + khiên, tiêu cự nông, không mặt |
| SC_003 | lính Tùy cận | quay lưng, out-focus; hơi nước thay chi tiết |
| SC_004 | tay cận + súng | 2 bàn tay, chuyển động chậm, súng nằm im |
| SC_005 | đại quân | aerial trung-cao, người là chấm |
| SC_006 | mặt lính Tùy | out-focus sâu, quay đi ngay |
| SC_007 | ngón tay cận trên cò | chuyển động chậm, 1 ngón, súng tĩnh |
| SC_008 | chân địch + tay | tiêu cự nông, 1 bàn tay, chân out-focus |
| SC_009 | ngựa + xe | 1 ngựa, xe là mô bùn (không chi tiết thép) |
| SC_010 | đại quân | aerial rất cao, không chi tiết |
| SC_011 | tay cận | 1 bàn tay mở, tĩnh |
| SC_012 | đại quân | aerial cao, cột là vệt |
| SC_013 | 2 kỵ sĩ + ngựa giáp | máy ngang, ngựa đứng yên |
| SC_014 | kỵ số đông + cung | wide tracking, bùn/mưa che chân ngựa |
| SC_015 | đám đông đuổi | theo cờ, người phụ out-focus |
| SC_016 | tay + dao cận | tĩnh, 2 bàn tay, dao nhỏ |
| SC_017 | tướng trên ngựa + đám đông | tracking ngang, lính phụ out-focus quay đi |
| SC_018 | hàng trăm thuyền | aerial cao, thuyền là hình khối |
| SC_019 | thuyền + người | máy tĩnh, 1 nhân vật, thuyền là boong |
| SC_020 | nhiều lính | thấp, out-focus, mặt khuất |
| SC_021 | tay + xe | 3 người, chuyển động đơn giản |
| SC_022 | tay già cận | chuyển động chậm, 2 bàn tay |
| SC_023 | nhiều người | still, lính quay mặt xuống |
| SC_026 | 6 người | từ sau lưng |
| SC_028 | trại + người | still wide |
| SC_029 | liềm + tay | chuyển động cắt đơn giản |
| SC_033 | chữ trong ảnh | blurred pencil lines, không ký tự; số OVERLAY |
| SC_035 | nhiều vật thể nhỏ | pan chậm, không chữ |
| SC_039 | địch sát nhân vật | tiêu cự nông, địch out-focus |
| SC_040 | số trên máy đếm | không cận mặt số |
| SC_041 | trại + đoàn xe | aerial |
| SC_049 | nhiều lính nền | nằm, out-focus |
| SC_051 | nhân vật quay lưng | không mặt (né drift) |
| SC_052 | hạm đội + thành | aerial |
| SC_053 | đám đông đổ bộ | wide tĩnh |
| SC_056 | 4만 | aerial, không cận |
| SC_059 | phố + lính | tracking, mặt quay đi |
| SC_060 | đám đông trong nhà | wide tĩnh, người ngồi thấp, tối dần |
| SC_062 | POV kính đêm | mono green, không HUD |
| SC_063 | đám đông đêm | viền người, rất tối; state có 'fresh cut' trước SC_070 |
| SC_064 | mặt lính phụ | bùn + tối |
| SC_066 | POV kính đêm | mono green, hình khối |
| SC_068 | cận chiến 4 người | nửa dưới nước, chỉ lưng và tay, nước bắn che |
| SC_069 | cận chiến | nửa dưới nước, nước sủi |
| SC_070 | dao cận + 2 người | rất tối, chớp xanh nhỏ, không máu cận |
| SC_071 | súng nâng | không cận cò, tay đập nòng |
| SC_072 | xác | nổi úp, tối |
| SC_075 | aerial đêm | tối, điểm sáng nhỏ |
| SC_076 | đại quân | aerial |
| SC_077 | đám đông cướp phá | tracking, mặt quay đi, out-focus |
| SC_080 | đám đông tối | out-focus, hình khối |
| SC_082 | đám đông | wide tĩnh |
| SC_083 | đám đông | wide, không cận |
| SC_084 | ngựa dựng + cận chiến | 1 ngựa, máy tĩnh |
| SC_085 | cung thủ số đông | low angle, hình dáng trên mái |
| SC_087 | đám đông + kỵ | aerial |
| SC_088 | đám đông + thuyền | wide |
| SC_089 | người leo ngựa | tracking, chuyển động 1 người 1 ngựa |
| SC_092 | xác | phủ vải, mép khung |
| SC_096 | chữ trên thẻ tre | chỉ vạch |
| SC_098 | mặt lính phụ | cận nồi, mặt out-focus |
| SC_103 | 3 nhân vật | wide đối xứng, mặt nhỏ |
| SC_106 | bản đồ có chữ | 'painted in ink', không ký tự |
| SC_110 | chữ trên lụa | 'short column of brush calligraphy', không đọc được |
| SC_111 | ngựa phi đêm | still |
| SC_114 | chữ trên lụa | không ký tự thật |
| SC_116 | tên cắm cận + lính | 1 mũi tên, người bất động |
| SC_126 | 4 người khiêng | wide, mặt quay đi |
| SC_128 | 3 người + song | máy qua nan tre, tĩnh |
| SC_130 | đám đông đuốc | still wide |
| SC_131 | POV kính đêm | mono green; 1 bàn tay + găng |
| SC_134 | 500 cung thủ | ngược sáng, viền người |
| SC_136 | tên trúng người | không cận vết |
| SC_138 | lặp chuyển động | nhịp đơn giản, tay không cận |
| SC_139 | 2 beat khác góc | insert riêng 4 s; tracer = vệt sáng, không cận súng |
| SC_140 | PZF + nổ | sau vai, chỉ ống và chớp lửa |
| SC_141 | 2 người trúng tên | không cận vết thương, người kéo xuống khuất |
| SC_143 | chữ màn hình | 'small blank readout box', số OVERLAY; tháp pháo lộ khỏi bùn = 1 chuyển động |
| SC_144 | nổ + đám đông | wide xa, cột nước che chi tiết |
| SC_145 | đám đông vỡ | aerial |
| SC_147 | nhiều người + xe trong nước | tracking chậm, xe là khối tối |
| SC_150 | bản đồ | 'painted in ink', không ký tự |
| SC_153 | chữ màn hình | ô trống, số OVERLAY |
| SC_157 | vết thương | băng ép + cán tên ngắn, không máu cận |
| SC_159 | chữ | blurred pencil, OVERLAY |
| SC_160 | vỏ đạn 120mm cận | 'steel ring as wide as his hand, black with soot', không chữ |
| SC_163 | 3 nhân vật | top-down, chỉ tay và bàn cát |
| SC_164 | tháo băng đạn | tay đơn giản, súng không chĩa |
| SC_173 | chữ | brush calligraphy không rõ ký tự |
| SC_175 | lính gầy | mặt quay đi, out-focus |
| SC_177 | chữ | nét bút mềm không đọc được; chữ thật OVERLAY |
| SC_178 | chữ | OVERLAY |
| SC_181 | kỵ số đông | wide |
| SC_186 | 3 nhân vật | tĩnh, khung rộng vừa |
| SC_192 | dao + cử chỉ cổ | chậm, không chạm da |
| SC_199 | 7 người | từ sau, sương che |
| SC_203 | 300 kỵ | sương che, hình khối |
| SC_204 | 9 người | ngang mặt nước, sương |
| SC_209 | giết lính gác | không lưỡi dao, không vết, 'slumps' |
| SC_217 | khung trắng | chấp nhận ảnh gần trống, hạt nhiễu |
| SC_223 | tay trên súng | không cận cò, ngón cái trên khóa |
| SC_226 | 300 kỵ | low wide, sương che, nước bùn |
| SC_227 | đám đông | wide |
| SC_228 | 3 nhân vật + 2 phụ | cửa lau hẹp, lần lượt |
| SC_231 | đánh dao dưới nước | chỉ lưng/tay/nước, không máu |
| SC_237 | ngón tay trên cò | cận mặt, tay mờ mép khung |
| SC_238 | nhiều người + ngựa | wide xa |
| SC_239 | kỵ số đông | tracking, nước che chân ngựa |
| SC_240 | nhiều người + ngựa | wide nhanh; insert cận 2 người |
| SC_241 | ngựa dựng ×3 | wide xa, cột nước che |
| SC_243 | công tắc | không chữ, nắp che |
| SC_246 | 3 nhân vật + lính | tĩnh, lính nền mờ |
| SC_248 | mũ trống ngàm | 'empty night-vision mount', không thiết bị |
| SC_252 | người chết | mặt yên, không chi tiết |
| SC_253 | nhiều người | tĩnh, mặt lính cúi |
| SC_254 | chữ | blurred pencil, OVERLAY |
| SC_255 | 2 mũ trong khung | mũ Hàn 'empty mount', mũ sắt 'no plume' |
| SC_259 | xe dưới bạt | chỉ khối phủ da |
| SC_260 | đại quân | aerial |
| SC_261 | 2 tướng + đám đông | tracking ngang, lính phụ out-focus |
| SC_262 | 2 ngựa + 2 người | low angle, tĩnh |
| SC_268 | chữ | brush calligraphy |
| SC_270 | xe xa | 'dim mud mound', không chi tiết |
| SC_272 | kỵ số đông | wide |
| SC_273 | đám đông | tracking, mặt khuất |
| SC_279 | chữ | blank readout, OVERLAY |
| SC_286 | xe xa | 'dim mud mound' |
| SC_287 | chữ | không tạo ảnh; end card ở edit |

### Quy tắc né chung (áp dụng toàn tập)
- **Người nằm trong lau + chân lính Tùy đi qua** (P1): máy thấp ngang mặt nước, chỉ chân/dép/vạt khiên của địch, không mặt địch; 1 nhân vật có ID trong khung.
- **Đám đông**: mọi cảnh ≥6 người → aerial/wide hoặc máy sau lưng, mặt phụ quay đi/khuất mũ; 4만/30만/방진 = aerial rất cao, không cận.
- **Chữ/số**: sổ tay, màn hình trưởng xe, bài thơ, thẻ tre, end card → prompt 'blurred pencil lines / small blank readout / columns of brush calligraphy'; số & chữ thật OVERLAY ở edit (decisions #1, #6).
- **Tay cầm súng/dao**: K2C1 luôn bọc vải/đặt xuống; dao găm cận chỉ khi tay KHÔNG làm động tác phức tạp; bắn = chớp lửa đầu nòng hoặc wide, không cận ngón tay trên cò (SC_004/007/011 ngoại lệ có chủ ý: 1 bàn tay, chuyển động chậm).
- **Đánh dao dưới nước** (SC_068–070, 231): 'bodies half under brown water, only backs, arms and churned water visible', không vết thương, không máu cận.
- **Ngựa + nước/sương** (P10): tracking thấp, nước bắn che chân ngựa; số ngựa ≤3 khi cận.
- **POV kính đêm**: 'monochrome green night-vision view with grain' — không HUD; SC_217 trắng lóa toàn khung.
- **K2 = mô bùn**: luôn dán VEH_STATE `VEH_001_mud` sau lock; chỉ SC_143–144 tháp pháo lộ khi xoay/bắn.
- **Hangul trên xe**: KHÔNG vẽ; '천둥' chỉ ở thoại/radio.
- **Nhân vật lịch sử**: diện mạo hư cấu theo lock; 주법상/사자/전령/통역 = lock tạm EXTRAS (1–3 SC), không ref trừ 사자/전령.
