# 5화 「살수」 (最終話) — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)
> Đếm theo `04_veo/scenes_ep5.json` (289 SC, xếp theo t_start — SC_169 trước SC_165). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.

## 1. Nhân vật (CHAR) — số SC xuất hiện
| CHAR | SC | Derived state trong 5화 (SC) |
|---|---|---|
| CHAR_001 | 58 | CHAR_001_final_ep5 (4), CHAR_001_helmet_hand_ep5 (1), CHAR_001_muddy_bloody_ep5 (44), CHAR_001_reeds_ep4 (2), CHAR_001_river_oil_ep5 (3), CHAR_001_river_oil_rifle_ep5 (4) |
| CHAR_002 | 28 | CHAR_002_final_ep5 (3), CHAR_002_muddy_bloody_ep5 (13), CHAR_002_reeds_helmet_ep5 (12) |
| CHAR_003 | 39 | CHAR_003_capless_ep5 (9), CHAR_003_crutch_ep5 (2), CHAR_003_driver_ep5 (4), CHAR_003_muddy_ep5 (19), CHAR_003_wounded_ep5 (5) |
| CHAR_004 | 15 | CHAR_004_muddy_bloody_ep5 (15) |
| CHAR_005 | 15 | CHAR_005_goguryeo_helmet_ep5 (13), CHAR_005_helmet_hand_ep5 (2) |
| CHAR_006 | 8 | CHAR_006_afoot_ep5 (2), CHAR_006_horseback_ep5 (6) |
| CHAR_101 | 17 | CHAR_101_false_surrender_ep3 (2), CHAR_101_salsu_rain_ep5 (15) |
| CHAR_102 | 3 | CHAR_102_hall_night_ep4 (3) |
| CHAR_103 | 2 | CHAR_103_court_ep5 (2) |
| CHAR_105 | 21 | CHAR_105_bandaged_ep5 (2), CHAR_105_bow_ep5 (7), CHAR_105_charge_ep5 (2), CHAR_105_radio_ep3 (3), CHAR_105_reeds_ep5 (5), CHAR_105_wounded_ep5 (2) |
| CHAR_106 | 10 | CHAR_106_final_ep5 (3), CHAR_106_salsu_ep5 (7) |
| CHAR_107 | 9 | CHAR_107_final_ep5 (3), CHAR_107_scarf_burnt_ep3 (6) |
| CHAR_201 | 5 | CHAR_201_defeat_news_ep5 (3), CHAR_201_rain_k21_ep5 (2) |
| CHAR_202 | 12 | CHAR_202_defeat_ep5 (3), CHAR_202_rain_ep5 (6), CHAR_202_river_ep5 (3) |
| CHAR_203 | 10 | CHAR_203_chained_ep5 (2), CHAR_203_rain_mounted_ep5 (7), CHAR_203_retreat_ep5 (1) |
| CHAR_205 | 17 | CHAR_205_bow_ep5 (2), CHAR_205_capless_ep5 (7), CHAR_205_final_ep5 (2), CHAR_205_waiting_ep5 (6) |

### Trạng thái trong tập do veo đặt (không có trong continuity_master.derived_states — đề xuất character-designer nhập DERIVED_STATES; ref đính = ref gần nhất)
| state_id | CHAR | ref đính | câu trạng thái |
|---|---|---|---|
| CHAR_001_river_oil_rifle_ep5 | CHAR_001 | CHAR_001_river_oil_ep5 | Helmet off, hair plastered flat, soaked to the chest, uniform and face streaked with the black sheen of fuel oil, water running from the sleeves, exhausted fierce eyes, a black assault rifle in his hands. |
| CHAR_001_helmet_hand_ep5 | CHAR_001 | CHAR_001_final_ep5 | Helmet held in one hand, hair dry and uncombed, mud dried grey on the uniform, a strip of cloth bandage wrapped around the right hand, empty thigh holster, quiet still face lit by warm sunlight. |
| CHAR_002_reeds_helmet_ep5 | CHAR_002 | CHAR_002_muddy_bloody_ep5 | Helmet on with chinstrap hanging loose and reed stalks in the band, tactical goggles pushed up on the helmet, mud smeared on the face, a field bandage wrapped around the left upper arm, mud to the thighs, rain-soaked uniform, K3 light machine gun with cloth tape on the stock. |
| CHAR_002_final_ep5 | CHAR_002 | CHAR_002_muddy_bloody_ep5 | Helmet on with chinstrap hanging loose, goggles missing, blood-soaked field bandage wrapped around the left upper arm, mud drying grey on the uniform, jaw clenched, exhausted eyes, no weapon in hand, warm sunlight. |
| CHAR_003_capless_ep5 | CHAR_003 | CHAR_003_muddy_ep5 | No cap: wet salt-and-pepper hair plastered to the forehead, mud caked to the hips, engine oil and blood on both forearms, week-old gray stubble, exhausted but calm face, the metal vehicle nameplate still tied to the backpack strap. |
| CHAR_003_driver_ep5 | CHAR_003 | CHAR_003_muddy_ep5 | No cap and no backpack: wet salt-and-pepper hair plastered to the forehead, mud caked to the hips, engine oil and blood on both forearms, week-old gray stubble, calm face, a small olive-drab steel nameplate showing in the chest pocket of the body armor. |
| CHAR_003_wounded_ep5 | CHAR_003 | CHAR_003_crutch_ep5 | No cap, wet salt-and-pepper hair, soaked to the chest, an arrow shaft standing from the left thigh with the trouser leg dark with blood, mud and oil on both forearms, week-old gray stubble, face white with pain but calm, teeth clenched. |
| CHAR_005_helmet_hand_ep5 | CHAR_005 | CHAR_005_goguryeo_helmet_ep5 | Mounted on a Goguryeo warhorse, a plain Goguryeo iron plate helmet without plume held in his hands, hacked short hair, borrowed body armor over a torn camo uniform with no flag patch on the right shoulder, a fading bruise on the left eye, right foot splinted with reeds and bandage, mud drying on the trousers, warm sunlight. |
| CHAR_006_afoot_ep5 | CHAR_006 | CHAR_006_horseback_ep5 | On foot holding the reins of a Goguryeo warhorse with leather saddle and iron stirrups, boonie hat drying, scrim scarf, K2C1 rifle slung across the chest, mud drying grey on the boots and trousers, warm sunlight. |
| CHAR_103_court_ep5 | CHAR_103 | CHAR_103_ref | Helmet removed, black topknot neat, armor cleaned and dry, no shield and no spear, standing at the foot of the dais, face lit warm from one side by oil lamps. |
| CHAR_105_reeds_ep5 | CHAR_105 | CHAR_105_radio_ep3 | A dead modern olive-green handheld radio with its light off clipped to the chest armor lacing, rain-soaked armor and green jacket, the white feather on the helmet broken and bent, no cloak, mud to the thighs, a black horn trumpet on a leather cord at the hip, quick alert eyes. |
| CHAR_105_bow_ep5 | CHAR_105 | CHAR_105_radio_ep3 | A dead modern olive-green handheld radio clipped to the chest armor lacing, a composite bow slung across the back, a black horn trumpet on a leather cord at the hip, rain-soaked armor and green jacket, the white feather on the helmet broken and bent, no cloak, mud to the thighs, quick alert eyes. |
| CHAR_105_charge_ep5 | CHAR_105 | CHAR_105_radio_ep3 | Ring-pommel sword drawn in the right hand, a composite bow slung across the back, a black horn trumpet at the hip, a dead handheld radio clipped to the chest armor, rain-soaked armor and green jacket, the white feather on the helmet broken, no cloak, wading in shallow brown water. |
| CHAR_106_salsu_ep5 | CHAR_106 | CHAR_106_ref | Hemp clothes and scorched leather forge apron soaked with rain, mud to the knees, wet wispy white beard, a hand-forged iron pry bar with a hooked end in his hands, no hammer at the belt. |
| CHAR_106_final_ep5 | CHAR_106 | CHAR_106_ref | Hemp clothes and leather forge apron drying stiff with mud, wet wispy white beard, a hand-forged iron pry bar with a hooked end planted in the sand beside him, warm sunlight. |
| CHAR_107_final_ep5 | CHAR_107 | CHAR_107_scarf_ep2 | The olive military scarf with one corner scorched black and frayed, braids damp and stuck with dried blood, dried blood on both hands, the jacket sleeves tied up with strips of cloth, mud on the hem of the skirt, warm sunlight. |
| CHAR_202_river_ep5 | CHAR_202 | CHAR_202_defeat_ep5 | Thrown into the river: soaked to the skin, helmet lost, white hair loosening from the topknot, beard streaming with muddy water, one breast mirror dented, red cloak torn to half its length, clutching a broken banner pole, chest-deep in brown water, stunned face. |
| CHAR_203_rain_mounted_ep5 | CHAR_203 | CHAR_203_retreat_ep5 | Mounted on a tall grey Han war horse with a high wooden saddle and a plain leather breast strap, helmet on, the fur collar of the cloak wet and matted, cloak soaked and heavy with rain, face gray with exhaustion, mud on the boots. |
| CHAR_205_waiting_ep5 | CHAR_205 | CHAR_205_final_ep5 | Mounted on a short stocky steppe horse with white cloth stuffed in its ears, fox-fur cap on and soaked, braid wet, a cracked night-vision device hanging from a cord around the neck, composite bow slung across the back, saber sheathed, right forearm wrapped in a black cloth bandage, rain on the face, calm assessing eyes. |
| CHAR_205_capless_ep5 | CHAR_205 | CHAR_205_final_ep5 | Fox-fur cap lost, braid loose and wet and swinging, a cracked night-vision device hanging from a cord around the neck, composite bow slung across the back, ring-pommel saber drawn in the right hand with blood on the blade, right forearm wrapped in a black cloth bandage, mud to the thighs, blood on the tunic, rain, fierce calm face. |
| CHAR_205_bow_ep5 | CHAR_205 | CHAR_205_final_ep5 | Fox-fur cap lost, braid loose and wet, a cracked night-vision device hanging from a cord around the neck, composite recurve bow in the left hand with an arrow nocked, the bandaged right forearm drawing the string, mud to the thighs, blood on the tunic, standing on scorched steel in white smoke. |

### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)
| Extra | SC | ref đính |
|---|---|---|
| XIANBEI_RIDERS | 29 | VEH_206_ref |
| SUI_WADERS | 21 | WPN_201_ref |
| GOG_CAVALRYMEN | 21 | VEH_101_ref |
| SUI_INFANTRY | 14 | WPN_201_ref |
| SUI_SHIELD_WALL | 13 | WPN_201_ref |
| GOG_SPEARMEN | 13 | WPN_102_ref |
| ROK_K3_GUNNER | 9 | — |
| GOG_DEPUTY | 9 | EXTRA_gog_deputy_ref |
| ROK_SOLDIERS | 7 | — |
| SUI_STANDARD_BEARER | 7 | PROP_021_ref |
| ROK_SOLDIERS_2 | 7 | — |
| DEAD_HORSE | 7 | — |
| ROK_SOLDIER | 5 | — |
| SUI_INFANTRY_BACKS | 4 | WPN_201_ref |
| SUI_REAR_GENERAL | 4 | VEH_207_ref |
| SUI_DEPUTY | 4 | WPN_201_ref |
| SUI_CAVALRYMEN | 4 | VEH_207_ref |
| ROK_WOUNDED | 4 | — |
| GOG_FLAG_BEARER | 3 | WPN_102_ref |
| GOG_HORN_BLOWER | 3 | WPN_102_ref |
| ROK_K6_CREW | 3 | — |
| VILLAGE_WOMEN_3 | 3 | — |
| ROK_MORTAR_CREW | 3 | — |
| XIANBEI_SCOUTS_2 | 3 | VEH_206_ref |
| SUI_ARCHERS | 3 | WPN_201_ref |
| GOG_YOUNG_RIDER | 3 | EXTRA_gog_young_rider_ref |
| XIANBEI_RIDER_ON_HULL | 3 | VEH_206_ref |
| GOG_SPEARMEN_SUN | 3 | WPN_102_ref |
| ROK_SOLDIERS_SUN | 3 | — |
| SUI_FEET | 2 | WPN_201_ref |
| GOG_CAV_OFFICER | 2 | VEH_101_ref |
| GOG_FIRE_ARCHERS | 2 | WPN_102_ref |
| GOG_FINGER | 2 | — |
| ROK_PZF_GUNNERS | 2 | — |
| ROK_DRIVER | 2 | EXTRA_k2_driver_ref |
| XIANBEI_ARCHER | 2 | VEH_206_ref |
| SUI_ROUT | 2 | WPN_201_ref |
| SUI_OX_DRIVER | 2 | — |
| SUI_WADER_FACE | 1 | WPN_201_ref |
| XIANBEI_LEADERS_2 | 1 | VEH_206_ref |
| GOG_ARCHER_OFFICER | 1 | WPN_102_ref |
| GOG_DRUMMERS | 1 | WPN_102_ref |
| VILLAGE_WOMAN | 1 | — |
| ROK_GUNNER_TURRET | 1 | — |
| ROK_HAND | 1 | — |
| SUI_STRAGGLERS | 1 | WPN_201_ref |
| SUI_EUNUCHS | 1 | — |
| SUI_GUARDS_WET | 1 | WPN_201_ref |
| SUI_EUNUCH_BOX | 1 | — |
| SUI_EUNUCH_UMBRELLA | 1 | — |
| SUI_SOLDIERS_SILHOUETTE | 1 | — |

## 2. Địa điểm (LOC) — số SC
| LOC | SC | Sub-lock (SC) |
|---|---|---|
| LOC_001 | 3 | LOC_001_cart_bench (1), LOC_001_retreat_rain (1), LOC_001_road_west (1) |
| LOC_002 | 1 | LOC_002_siege_613 (1) |
| LOC_004 | 8 | LOC_004_jiangdu_618 (1), LOC_004_pavilion_int_rain (3), LOC_004_rain (1), LOC_004_yard_rain (3) |
| LOC_005 | 1 | LOC_005_south_bank (1) |
| LOC_006 | 6 | KB_poem (1), LOC_006_hall (3), LOC_006_hall_door (2) |
| LOC_007 | 270 | KB_notebook (1), KB_sand_plan (1), KB_silk_map (4), LOC_007 (8), LOC_007_aftermath (4), LOC_007_aid (6), LOC_007_dawn_aerial (4), LOC_007_east_hill (1), LOC_007_east_shore (9), LOC_007_east_shore_sun (3), LOC_007_ford (7), LOC_007_ford_surface (1), LOC_007_k2_driver_int (1), LOC_007_k2_reeds (16), LOC_007_k2_reeds_flat (46), LOC_007_k2_roof (6), LOC_007_k2_turret_int (4), LOC_007_mid_bar (8), LOC_007_mortar_pit (3), LOC_007_mud_bank (1), LOC_007_north_flat (2), LOC_007_north_flat_edge (13), LOC_007_north_flat_sun (5), LOC_007_north_hill_foot (4), LOC_007_north_line (20), LOC_007_reeds (22), LOC_007_reeds_night (2), LOC_007_small_bar (6), LOC_007_small_bar_sun (5), LOC_007_south_edge (8), LOC_007_south_field (3), LOC_007_south_knoll (12), LOC_007_south_shore (6), LOC_007_throat (3), LOC_007_throat_k2 (12), LOC_007_throat_rim (6), LOC_007_throat_sun (2), LOC_007_upstream_bar (4), LOC_007_west_reeds (1) |

## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/EQP) — số SC
| ID | SC | ghi chú |
|---|---|---|
| VEH_001 | 89 | K2 damage 4 pha (VEH_STATE k2_reeds → after_fire → arrows → running → stalled → burning → sunk → wreck); SC_281–284 đính `VEH_001_ep5` |
| VEH_206 | 32 | kỵ Tiên Ti ngựa bịt tai (v206_ears/v206_water) |
| WPN_001 | 29 |  |
| EQP_002 | 25 |  |
| VEH_101 | 25 | 개마무사 — kỵ thật; 'giáo 삭' của 창병 → EXTRA GOG_SPEARMEN + WPN_102_ref (không đính VEH_101) |
| VEH_207 | 24 | kỵ Tùy v3 — 우중문 ngựa đen (v207_black), 우문술 ngựa xám (v207_grey), 후군 장수 ngựa hung; KHÔNG đính VEH_205 |
| WPN_003 | 18 |  |
| EQP_001 | 12 |  |
| WPN_101 | 5 |  |
| VEH_002 | 4 | 천둥 3 bị thu: `VEH_002_captured` + k21_captured/k21_road |
| WPN_004 | 3 |  |
| WPN_002 | 3 |  |
| WPN_005 | 2 |  |
| VEH_205 | 1 | chỉ SC_273 (cầu phao 요하) |
| VEH_201 | 1 |  |
| VEH_203 | 1 |  |

## 4. Đạo cụ (PROP) — số SC
| PROP | SC | ghi chú |
|---|---|---|
| PROP_021 | 25 |  |
| PROP_009 | 11 |  |
| PROP_018 | 9 | tù và 3 hồi = hiệu lệnh (SC_076/208) — không ref bible → PROP_018_ref (dup ep4) |
| PROP_024 | 8 | cờ đỏ hiệu lệnh — cuộn (SC_004–184) / bung (SC_066+, VISUAL_LOCK_EN_OPEN dán trong Action) |
| PROP_019 | 6 |  |
| PROP_025 | 6 | nhiệt nhôm — túi ngực (SC_161) → khay nạp (SC_189) → cài áo (SC_213) → thả (SC_224) |
| PROP_006 | 5 |  |
| PROP_020 | 5 |  |
| PROP_026 | 5 | nút bầu — không ref (cận cảnh) |
| SILK_MAP | 4 | **LOCK_PENDING** bản đồ lụa 을지문덕 (script tag PROP_001) |
| K5_PISTOL | 4 |  |
| PROP_008 | 3 |  |
| GOURD_BOTTLE | 2 |  |
| PROP_012 | 2 |  |
| PROP_023 | 2 | biển '3' — ba lô (P1–P8) → túi ngực (SC_168) → mép tháp K2 cạnh số 1 (SC_282) |
| PROP_011 | 2 |  |
| WATER_BOWL | 2 |  |
| LACQUER_BOX | 2 |  |
| OX_CART_GIANT | 2 |  |
| PROP_016 | 1 |  |
| PROP_017 | 1 |  |
| PROP_015 | 1 |  |
| SMALL_CROW_PENNANT | 1 | **LOCK_PENDING** cờ hiệu nhỏ (script tag PROP_012) |
| MORPHINE | 1 |  |
| PROP_014 | 1 |  |

## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)
| # | ref id | thư mục | số SC đính | trạng thái |
|---|---|---|---|---|
| 1 | LOC_007_k2_reeds_ep5 | locations | 73 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 2 | VEH_001_ref | vehicles | 58 | có job |
| 3 | WPN_201_ref | vehicles | 56 | có job |
| 4 | CHAR_001_muddy_bloody_ep5 | characters | 44 | có job |
| 5 | LOC_007_north_line_ep5 | locations | 42 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 6 | CHAR_003_muddy_ep5 | characters | 32 | có job |
| 7 | VEH_206_ref | vehicles | 32 | có job |
| 8 | CHAR_002_muddy_bloody_ep5 | characters | 28 | có job |
| 9 | LOC_007_throat_ep5 | locations | 28 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 10 | LOC_007_wide | locations | 26 | có job |
| 11 | WPN_001_ref | vehicles | 26 | có job |
| 12 | LOC_007_detail | locations | 25 | có job |
| 13 | WPN_102_ref | vehicles | 24 | có job |
| 14 | VEH_207_ref | vehicles | 24 | có job |
| 15 | PROP_021_ref | props | 22 | có job |
| 16 | VEH_101_ref | vehicles | 20 | có job |
| 17 | WPN_003_ref | vehicles | 18 | có job |
| 18 | CHAR_105_radio_ep3 | characters | 17 | có job |
| 19 | CHAR_205_final_ep5 | characters | 17 | có job |
| 20 | CHAR_101_salsu_rain_ep5 | characters | 15 | có job |
| 21 | CHAR_005_goguryeo_helmet_ep5 | characters | 15 | có job |
| 22 | CHAR_004_muddy_bloody_ep5 | characters | 14 | có job |
| 23 | LOC_007_south_knoll_ep5 | locations | 12 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 24 | EQP_002_ref | vehicles | 11 | có job |
| 25 | PROP_009_ref | props | 11 | có job |
| 26 | LOC_007_small_bar_ep5 | locations | 11 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 27 | CHAR_106_ref | characters | 10 | có job |
| 28 | LOC_007_finale_light | locations | 10 | có job |
| 29 | CHAR_107_scarf_ep2 | characters | 9 | có job |
| 30 | EXTRA_gog_deputy_ref | characters | 9 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 31 | PROP_024_ref | props | 8 | có job |
| 32 | CHAR_203_retreat_ep5 | characters | 8 | có job |
| 33 | PROP_018_ref | props | 8 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** (trùng ep4 extra — chạy 1 lần) |
| 34 | CHAR_006_horseback_ep5 | characters | 8 | có job |
| 35 | LOC_007_mid_bar_ep5 | locations | 8 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 36 | LOC_007_aid_ep5 | locations | 7 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 37 | LOC_007_north_hill_ep5 | locations | 7 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 38 | CHAR_003_crutch_ep5 | characters | 7 | có job |
| 39 | CHAR_001_river_oil_ep5 | characters | 7 | có job |
| 40 | CHAR_202_rain_ep5 | characters | 6 | có job |
| 41 | CHAR_202_defeat_ep5 | characters | 6 | có job |
| 42 | PROP_025_ref | props | 6 | có job |
| 43 | PROP_006_ref | props | 5 | có job |
| 44 | WPN_101_ref | vehicles | 5 | có job |
| 45 | VEH_001_interior_ref | vehicles | 5 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 46 | CHAR_001_final_ep5 | characters | 5 | có job |
| 47 | LOC_006_interior | locations | 5 | có job |
| 48 | EXTRA_silk_map_ref | props | 4 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 49 | LOC_007_upstream_bar_ep5 | locations | 4 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 50 | LOC_004_detail | locations | 4 | có job |
| 51 | VEH_002_captured | vehicles | 4 | có job |
| 52 | VEH_001_ep5 | vehicles | 4 | có job |
| 53 | LOC_007_aftermath_ep5 | locations | 4 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 54 | WPN_004_ref | vehicles | 3 | có job |
| 55 | WPN_002_ref | vehicles | 3 | có job |
| 56 | EXTRA_gog_young_rider_ref | characters | 3 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 57 | CHAR_201_defeat_news_ep5 | characters | 3 | có job |
| 58 | LOC_004_yard_rain_ep5 | locations | 3 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 59 | CHAR_102_hall_night_ep4 | characters | 3 | có job |
| 60 | CHAR_001_reeds_ep4 | characters | 2 | có job |
| 61 | PROP_008_ref | props | 2 | có job |
| 62 | WPN_005_ref | vehicles | 2 | có job |
| 63 | EXTRA_k2_driver_ref | characters | 2 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 64 | PROP_023_ref | props | 2 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 65 | CHAR_105_wounded_ep5 | characters | 2 | có job |
| 66 | PROP_011_ref | props | 2 | có job |
| 67 | CHAR_105_bandaged_ep5 | characters | 2 | có job |
| 68 | CHAR_203_chained_ep5 | characters | 2 | có job |
| 69 | CHAR_201_rain_k21_ep5 | characters | 2 | có job |
| 70 | CHAR_103_ref | characters | 2 | có job |
| 71 | CHAR_101_false_surrender_ep3 | characters | 2 | có job |
| 72 | LOC_001_road_west_ep5 | locations | 2 | **CHƯA CÓ — job trong ref_jobs_ep5_extra.json** |
| 73 | PROP_019_ref | props | 1 | có job |
| 74 | PROP_017_ref | props | 1 | có job |
| 75 | PROP_012_ref | props | 1 | có job |
| 76 | EQP_001_ref | vehicles | 1 | có job |
| 77 | PROP_015_ref | props | 1 | có job |
| 78 | LOC_005_wide | locations | 1 | có job |
| 79 | LOC_004_wide | locations | 1 | có job |
| 80 | VEH_205_ref | vehicles | 1 | có job |
| 81 | LOC_001_wide | locations | 1 | có job |
| 82 | VEH_201_ref | vehicles | 1 | có job |
| 83 | VEH_203_ref | vehicles | 1 | có job |
| 84 | LOC_002_wide | locations | 1 | có job |
| 85 | PROP_014_ref | props | 1 | có job |

### Ref CHƯA CÓ (job: `05_references/extra/ref_jobs_ep5_extra.json` — glabs-operator tạo trước lô ảnh cảnh)
- `LOC_007_k2_reeds_ep5` (locations, 16:9): K2 trát bùn cắm lau ở mép bãi lau bờ bắc cách cổng họng 300 m (P1–P9) — sub-lock `LOC_007_k2_reeds`/`_k2_reeds_flat`/`_south_edge`/`_mortar_pit` (≈80 SC).
- `LOC_007_throat_ep5` (locations, 16:9): cổng họng bãi (여울 목): khe 60 m nước ngang ngực giữa bãi lau (tây) và bờ bùn dốc (đông), cọc gỗ nghiêng, KHÔNG có xe — sub-lock `LOC_007_throat`/`_throat_k2`/`_k2_roof`/`_mud_bank`/`_throat_rim` (P10 ≈45 SC).
- `LOC_007_north_line_ep5` (locations, 16:9): tuyến bắc: mép lau gặp bãi cát bắc, hố bao cát nối nhau, K6 giá ba chân phủ lau — sub-lock `LOC_007_north_line`/`_east_shore`/`_north_flat_edge`.
- `LOC_007_south_knoll_ep5` (locations, 16:9): gò nam: cỏ ướt, vài cây thông ngả gió, nhìn xuống sông đầy quân — sub-lock `LOC_007_south_knoll` (v3 nguyên văn; 12 SC 을지문덕/cờ đỏ/나각).
- `LOC_007_north_hill_ep5` (locations, 16:9): bãi cát bắc → đồi thấp bắc trong mưa, lau thấp chân đồi (2.000 kỵ Tiên Ti) — sub-lock `LOC_007_north_flat` (v3)/`_north_hill_foot`/`_east_hill`.
- `LOC_007_small_bar_ep5` (locations, 16:9): mô cát nhỏ cạnh cổng họng, xác ngựa Tùy, tên gãy, cờ đỏ ngã — sub-lock `LOC_007_small_bar` (v3)/`_small_bar_sun` (Phase 3–5, P11 ≈16 SC).
- `LOC_007_mid_bar_ep5` (locations, 16:9): mô cát giữa sông đầy lính Tùy + cụm cờ quanh tướng cưỡi ngựa, cát lở — sub-lock `LOC_007_mid_bar` (v3, SC_063–064/079/081/087/098/192/236).
- `LOC_007_upstream_bar_ep5` (locations, 16:9): mô cát thượng lưu 1,5 km đông, nước tới bụng ngựa, kỵ Goguryeo hàng một — sub-lock `LOC_007_upstream_bar` (v3).
- `LOC_007_aid_ep5` (locations, 16:9): trạm cứu thương sâu trong lau: chiếu lau hàng, mái lau, bát thuốc, băng — sub-lock `LOC_007_aid`/`_west_reeds`.
- `LOC_007_aftermath_ep5` (locations, 16:9): D+10 nước rút, nắng: bãi cát khô nứt, lạch nông, xác K2 cháy nghiêng — sub-lock `LOC_007_aftermath` (v3; SC_281–284). Khác `LOC_007_finale_light` (còn nước lũ).
- `LOC_004_yard_rain_ep5` (locations, 16:9): sân 육합성 mưa D+5: cỗ xe gỗ khổng lồ lún bùn chở K21 phủ vải dầu, cờ Tùy — sub-lock `LOC_004_yard_rain` (SC_270–272).
- `LOC_001_road_west_ep5` (locations, 16:9): đường đất lầy về tây trong mưa, xe bò 40 con kéo cỗ xe khổng lồ — sub-lock `LOC_001_road_west`/`_cart_bench` (SC_286–287).
- `VEH_001_interior_ref` (vehicles, 16:9): nội thất K2 (2 panel: ghế trưởng xe + thị kính + khay máy nạp + màn hình trống · khoang lái yoke + kính tiềm vọng) — 12 SC trong xe; né drift nội thất.
- `PROP_018_ref` (props, 16:9): tù và sừng trâu đen ~50 cm, miệng đồng, dây da — hiệu lệnh 3 hồi (SC_076/208) + 해모루 (trùng đề xuất ep4 extra → chạy 1 lần).
- `PROP_023_ref` (props, 16:9): biển thép ô-liu 10×25 cm số '3' trắng trầy, 2 lỗ bu-lông, mép cháy sém (SC_168/282 cận) — không Hangul.
- `EXTRA_silk_map_ref` (props, 16:9): **LOCK_PENDING** bản đồ lụa 을지문덕 vẽ mực (sông cong, cọc, mô cát, lau tô dày, đồi vảy, chấm son đỏ) — 4 still KB (SC_012/014/029/107).
- `EXTRA_gog_deputy_ref` (characters, 3:4): 고구려 부장 (~45, râu ngắn đen, giáp dây đỏ, chỏm lông đen) — 9 SC thấy mặt (P2, P6, P7, P9, P10, P11).
- `EXTRA_gog_young_rider_ref` (characters, 3:4): 고구려 전령 trẻ (~20, không râu, chỏm lông đỏ, ngựa hạt dẻ giáp) — SC_117/172/184.
- `EXTRA_k2_driver_ref` (characters, 3:4): 조종수 K2 phối thuộc (~28, mặt vuông, mũ crew) — SC_139/140 trúng tên vai phải.

### Thứ tự chạy ref đề xuất (P1 → P3)
- **P1 (≥15 SC):** LOC_007_k2_reeds_ep5, VEH_001_ref, WPN_201_ref, CHAR_001_muddy_bloody_ep5, LOC_007_north_line_ep5, CHAR_003_muddy_ep5, VEH_206_ref, CHAR_002_muddy_bloody_ep5, LOC_007_throat_ep5, LOC_007_wide, WPN_001_ref, LOC_007_detail, WPN_102_ref, VEH_207_ref, PROP_021_ref, VEH_101_ref, WPN_003_ref, CHAR_105_radio_ep3, CHAR_205_final_ep5, CHAR_101_salsu_rain_ep5, CHAR_005_goguryeo_helmet_ep5
- **P2 (5–14 SC):** CHAR_004_muddy_bloody_ep5, LOC_007_south_knoll_ep5, EQP_002_ref, PROP_009_ref, LOC_007_small_bar_ep5, CHAR_106_ref, LOC_007_finale_light, CHAR_107_scarf_ep2, EXTRA_gog_deputy_ref, PROP_024_ref, CHAR_203_retreat_ep5, PROP_018_ref, CHAR_006_horseback_ep5, LOC_007_mid_bar_ep5, LOC_007_aid_ep5, LOC_007_north_hill_ep5, CHAR_003_crutch_ep5, CHAR_001_river_oil_ep5, CHAR_202_rain_ep5, CHAR_202_defeat_ep5, PROP_025_ref, PROP_006_ref, WPN_101_ref, VEH_001_interior_ref, CHAR_001_final_ep5, LOC_006_interior
- **P3 (<5 SC):** EXTRA_silk_map_ref, LOC_007_upstream_bar_ep5, LOC_004_detail, VEH_002_captured, VEH_001_ep5, LOC_007_aftermath_ep5, WPN_004_ref, WPN_002_ref, EXTRA_gog_young_rider_ref, CHAR_201_defeat_news_ep5, LOC_004_yard_rain_ep5, CHAR_102_hall_night_ep4, CHAR_001_reeds_ep4, PROP_008_ref, WPN_005_ref, EXTRA_k2_driver_ref, PROP_023_ref, CHAR_105_wounded_ep5, PROP_011_ref, CHAR_105_bandaged_ep5, CHAR_203_chained_ep5, CHAR_201_rain_k21_ep5, CHAR_103_ref, CHAR_101_false_surrender_ep3, LOC_001_road_west_ep5, PROP_019_ref, PROP_017_ref, PROP_012_ref, EQP_001_ref, PROP_015_ref, LOC_005_wide, LOC_004_wide, VEH_205_ref, LOC_001_wide, VEH_201_ref, VEH_203_ref, LOC_002_wide, PROP_014_ref

## 6. SC cần ảnh ĐẠI QUÂN / AERIAL / CLIMAX (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)
| SC | t | type | aerial | nội dung |
|---|---|---|---|---|
| SC_005 | 0:32 | still_kenburns | aerial | Very high aerial still, straight down at a steep angle, ken-burns slow pull-out |
| SC_006 | 0:40 | video8s | aerial | Low wide shot from a sandbar, static camera |
| SC_011 | 1:20 | still_kenburns | aerial | High aerial still, ken-burns very slow push-in on the mid-river sandbar |
| SC_013 | 1:42 | video8s | aerial | Aerial, slow drift from south to north across the whole ford |
| SC_017 | 2:18 | video8s | aerial | Wide medium shot, static camera |
| SC_031 | 4:18 | still_kenburns | aerial | High aerial still, ken-burns very slow pull-out |
| SC_046 | 6:24 | video8s | aerial | Wide medium shot, static camera |
| SC_048 | 6:40 | still_kenburns | aerial | Very high aerial still, ken-burns slow pull-out |
| SC_049 | 6:50 | still_kenburns | aerial | Lower aerial still, ken-burns slow push-in on the great banner |
| SC_062 | 8:36 | video8s | aerial | Low aerial shot, slow drift over the center division |
| SC_065 | 9:00 | still_kenburns | aerial | Very high aerial still, ken-burns slow push-in on the center |
| SC_069 | 9:34 | video8s | aerial | Wide medium shot, static camera |
| SC_079 | 10:54 | video8s | aerial | Wide medium shot, static camera |
| SC_081 | 11:10 | video8s | climax | Medium shot at water level, static camera |
| SC_083 | 11:26 | video8s | aerial | Low aerial shot, slow drift |
| SC_087 | 11:58 | video8s | aerial | Low aerial shot, slow drift |
| SC_089 | 12:14 | video8s | climax | Wide shot from the reed edge, static camera |
| SC_090 | 12:22 | video8s | climax | Wide shot from behind the gunners, static camera |
| SC_091 | 12:30 | video8s | aerial | Wide medium shot, static camera |
| SC_095 | 13:02 | video8s | aerial | Low aerial shot following the flow of men |
| SC_101 | 13:50 | still_kenburns | aerial | Wide still from the north hill over the commander's shoulder, ken-burns push from the riders past him down to the reed bed |
| SC_114 | 15:40 | video8s | climax | Wide shot from inside the reeds, static camera |
| SC_123 | 16:52 | still_kenburns | aerial | Wide still of the north hillside, ken-burns pull-out from a horse's ear to the whole flow |
| SC_126 | 17:18 | still_kenburns | aerial | High aerial still, ken-burns very slow pull-out |
| SC_128 | 17:38 | video8s | aerial | Low tracking shot with the front rank of the charge |
| SC_152 | 20:50 | still_kenburns | aerial | High aerial still, ken-burns slow push-in on the left flank |
| SC_191 | 26:12 | video8s | aerial | Low aerial shot, slow drift |
| SC_193 | 26:28 | still_kenburns | aerial | Very high aerial still of the whole board, ken-burns very slow pull from the south knoll across the river to the upstream sandbars |
| SC_201 | 27:38 | video8s | climax | Low wide shot from behind the tank, static camera |
| SC_202 | 27:46 | video8s | climax | Wide shot, static camera |
| SC_204 | 28:02 | video8s | climax | Low lateral tracking shot with the tank |
| SC_205 | 28:10 | video8s | climax | Low angle from the water surface, static camera |
| SC_206 | 28:18 | video8s | climax | Wide shot from the reed side, static camera |
| SC_208 | 28:34 | video8s | aerial | Aerial straight down on the throat, very slow push-in |
| SC_210 | 28:50 | video8s | aerial | High tracking shot from the bank following the riders down |
| SC_211 | 28:58 | video8s | climax | Medium shot on the knoll, static camera |
| SC_212 | 29:06 | video8s | climax | Medium shot level with the turret, static camera |
| SC_225 | 30:50 | video8s | climax | Low backlit shot from the water, static camera |
| SC_227 | 31:06 | video8s | climax | Wide shot, static camera |
| SC_230 | 31:30 | video8s | aerial | Low aerial shot following the file |
| SC_231 | 31:38 | video8s | aerial | Wide shot, static camera |
| SC_232 | 31:46 | video8s | aerial | Wide medium shot, static camera |
| SC_234 | 32:02 | video8s | climax | Medium shot, static camera |
| SC_238 | 32:34 | video8s | aerial | Low aerial shot, slow drift |
| SC_244 | 33:22 | video8s | climax | Low angle from the water surface, static camera |
| SC_245 | 33:30 | video8s | climax | Close-up widening to medium, slow pull-back |
| SC_248 | 33:54 | video8s | climax | Close two-shot, static camera |
| SC_249 | 34:02 | video8s | climax | Medium shot on the roof, static camera |
| SC_250 | 34:10 | video8s | aerial | Wide shot, very slow lateral drift |
| SC_251 | 34:18 | still_kenburns | aerial | Aerial still under a shaft of sun, ken-burns very slow push-in on the water crossing the hull |
| SC_252 | 34:30 | video8s | aerial | Low aerial shot, slow drift toward the river |
| SC_266 | 36:26 | still_kenburns | aerial | Wide still, ken-burns from the distant stone fortress to the gate of the mobile fortress |
| SC_273 | 37:30 | still_kenburns | aerial | Aerial still in rain, ken-burns from the stone fortress to the pontoon bridges |
| SC_274 | 37:40 | still_kenburns | aerial | Wide still, ken-burns from the siege tower to the retreating column |
| SC_286 | 39:22 | still_kenburns | aerial | Wide still, ken-burns very slow pull-out |

## 7. OVERLAY ở edit (chữ/số KHÔNG vẽ trong ảnh) + END CARD
| SC | overlay |
|---|---|
| SC_008 | 잔탄 06 (màn hình bộ đếm đạn trong tháp — cold blue screen, small blank readout) |
| SC_082 | Bộ đếm đạn góc màn hình: 04 → 03 (overlay số lên 'small blank readout') |
| SC_086 | Bộ đếm đạn: 01 → 00 (overlay lên màn hình trống) |
| SC_093 | 잔탄 00 (màn hình bộ đếm qua cửa tháp mở — small blank readout) |
| SC_189 | Bộ đếm '00' sáng xanh cạnh khay nạp (overlay lên màn hình trống) |
| SC_213 | Bộ đếm '00' (small blank readout) |
| SC_282 | (tùy chọn) chữ '천둥' nếu edit muốn — ảnh chỉ số 3 và 1 |
| SC_285 | Subtitle 知足願云止 + dịch Hàn khi narrator đọc (decisions #6) |
| SC_288 | END CARD: 「살수 612 — 끝」 (chữ trắng giữa khung, nền đen); âm mưa trên nắp hộp vọng 3 s rồi im |
| SC_289 | END CARD: 「다음: 613」 (chữ trắng nhỏ hơn, giữa khung, nền đen); im tuyệt đối, giây cuối 1 hồi tù và rất xa — gieo series 2 |

## 8. 2-BEAT / INSERT_CLIP (clip tách riêng 3–4 s, ghép ở edit)
| SC | 2-beat | insert (s) | nội dung insert |
|---|---|---|---|
| SC_001 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_002 | yes | 4 | Close-up at water level, static: a row of Sui soldiers' legs in torn wet cloth trousers and straw sandals wading down into muddy brown water, mud clouding with every step… |
| SC_003 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_004 | yes | 4 | Extreme close-up, static: a large plain red silk signal banner rolled tightly around a bamboo pole and tied with hemp cord, the knots untied by no one, rain streaming dow… |
| SC_078 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_080 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_082 | yes | 4 | Low static shot from behind a ROK sergeant kneeling at the mud-caked track of a K2 tank in flattened reeds in monsoon rain, one hand over his ear, the other keying a radi… |
| SC_084 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_085 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_086 | yes | 4 | Static close-up inside the cramped commander's station of a K2 tank: a 34-year-old Korean captain in a mud-smeared reed-stuck helmet with his eye at the commander's sight… |
| SC_128 | yes | 3 | Extreme close-up, static: the ear of a short stocky steppe horse packed tight with white cloth, a leather cord tied across its wet brow, rain on the dark hide, a fur-trim… |
| SC_204 | yes | 4 | Static close-up inside the reclined driver's compartment of a K2 tank: a 42-year-old Korean sergeant with wet salt-and-pepper hair plastered to his forehead, mud and oil … |
| SC_207 | yes | 3 | Static close-up inside the driver's compartment of a K2 tank: a 42-year-old Korean sergeant with wet salt-and-pepper hair twisting in his seat to reach a small steel hand… |
| SC_208 | yes | 4 | Medium shot, static: a 32-year-old Korean man with a sharp hawk-like face in light Goguryeo iron lamellar chest armor over a dark green jacket with red border, iron helme… |
| SC_211 | yes | 4 | Medium shot, static: a 27-year-old Korean lieutenant in a mud-smeared reed-stuck helmet with the chinstrap loose, goggles missing, a blood-soaked bandage on his left uppe… |
| SC_215 | yes | 3 | Close-up inside the driver's compartment of a K2 tank: a 42-year-old Korean sergeant with wet salt-and-pepper hair pulls the driver's hatch shut over his head and throws … |
| SC_218 | yes | 3 | Medium shot, static: the driver's hatch at the bow of a mud-caked arrow-bristling K2 tank stalled in chest-deep brown river water springs open and the head of a 42-year-o… |
| SC_220 | yes | 4 | Handheld shot at water level, shaking: a 34-year-old Korean captain in a mud-smeared reed-stuck helmet, chest-deep in brown river water with oil sheen, hauling a 42-year-… |
| SC_223 | yes | 4 | Handheld shot at water level: a 34-year-old Korean man, helmet off, hair plastered flat, face and uniform streaked with black fuel oil, surfaces from under the belly of a… |
| SC_224 | yes | 4 | Handheld shot on the arrow-bristling roof of a K2 tank stalled in brown river water: a bareheaded 34-year-old Korean man streaked with black oil drives his whole body int… |
| SC_245 | yes | — | beat A/B trong 1 clip (cùng góc máy) |
| SC_249 | yes | 4 | Extreme close-up at water level, static: on brown river water streaked with oil sheen and lit by nearby fire, a small full-color embroidered South Korean Taegukgi flag pa… |

## 9. CHAIN_FROM (tail-frame → start_image)
027→028, 038→039, 041→042, 060→061, 063→064, 099→100, 104→105, 108→109, 112→113, 115→116, 118→119, 137→138, 139→140, 146→147, 158→159, 162→163, 163→164, 166→167, 177→178, 181→182, 182→183, 194→195, 209→210, 221→222, 236→237, 240→241, 242→243, 246→247, 255→256, 256→257, 260→261, 261→262, 263→264, 267→268, 268→269, 276→277, 277→278, 283→284

## 10. SC RỦI RO AI & cách né trong prompt
| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |
|---|---|---|
| SC_001 | Feet/sandal deformation | 1 foot cận, rest out of focus; no faces |
| SC_002 | Crowd faces | only one face sharp near lens, others under shields/turned away |
| SC_003 | Hand/finger tapping | single hand, slow motion, gloved |
| SC_004 | Banner unrolling by itself | 'rolled tightly, tied with hemp cord' repeated |
| SC_005 | Mass crowd aerial | very high, troops as texture, no faces |
| SC_006 | Mass crowd + horses in water | wide, static, horses ≤3 sharp in foreground |
| SC_007 | Row of soldiers | faces turned away/mud, only the private's face visible |
| SC_008 | Screen digits | 'small blank readout', number overlaid at edit |
| SC_009 | Binoculars+hands | binoculars small, gloved hands |
| SC_010 | Screen text | 'single short battery bar', no digits |
| SC_011 | Mass column aerial | texture, no faces |
| SC_012 | Map text hallucination | 'brush strokes, no readable writing' repeated |
| SC_013 | Aerial geography drift | reeds west, mud bank east of the gap stated |
| SC_014 | Text | none; squares and arrows only |
| SC_015 | Two generals confusion | grey horse + black cuirass + grey beard stated |
| SC_016 | Banner text | plain red silk with yellow border, no writing |
| SC_017 | Horses en masse | riders ≤6 in mid-ground, mud spray hiding legs |
| SC_018 | Generic Sui general drift | same description verbatim each time |
| SC_019 | Many figures | archers as a line seen from behind, cavalry as silhouettes |
| SC_020 | Hands on cord | simple two-hand pull |
| SC_021 | Two men + tank | both faces visible, tank side skirt only |
| SC_022 | Text on tape | 'cloth tape, writing illegible/blurred' |
| SC_023 | Hangul on hull | none; only the numeral 1 and flag corner |
| SC_024 | Five+ figures | women from behind, three named faces only |
| SC_026 | 300 cavalry | background silhouettes in low reeds; 3 faces |
| SC_027 | Night exposure | faces only as grey sheen; stopper close and sharp |
| SC_028 | Small object | close, sharp, single hand |
| SC_029 | Extra fingers | one finger, rest of hand out of frame |
| SC_031 | Aerial mass | texture |
| SC_032 | 90 faces | half ring seen from behind the sergeant, faces small and mud-dark |
| SC_033 | Counting objects | 'three rows of ten' stated; hands simple |
| SC_034 | Ammo belts | no digits, simple hands |
| SC_035 | Finger count | exactly four fingers up, thumb folded; single hand |
| SC_036 | Readable text | 'pencil marks blurred and unreadable' |
| SC_037 | Small objects | eight tubes in a row, no labels |
| SC_038 | Panning across many faces | faces mud-dark, helmets low, slow pan |
| SC_040 | Pistol in holster only, not drawn | — |
| SC_041 | Hands passing objects | one hand, one palm at a time, slow |
| SC_042 | Hands at the chin strap | simple, slow |
| SC_044 | Old man in water | upper body sharp, water motion simple |
| SC_046 | Cavalry mass | mid-ground, mud/spray hiding legs, no gore |
| SC_047 | Crowd | shields and helmets, faces hidden |
| SC_048 | Aerial mass | texture |
| SC_049 | Aerial mass | texture |
| SC_050 | Crowd | shields overhead hide faces; reeds in foreground |
| SC_051 | Crowd | eye-level distance, faces small |
| SC_055 | Feet | out of focus beyond the nearest pair |
| SC_057 | Track marks | 'two deep parallel ruts' simple; horses ≤2 |
| SC_058 | Finger on trigger | hand on muzzle is the action, trigger hand soft-focus |
| SC_059 | Galloping horses | 2 horses, mud spray on legs |
| SC_060 | Cavalry ranks | silhouettes in reeds; ≤3 horses sharp |
| SC_061 | Finger counting | slow, one hand |
| SC_062 | Mass in water | heads and shields texture, one general sharp |
| SC_064 | Horse legs | 2 forelegs only, water motion simple |
| SC_065 | Aerial mass | texture |
| SC_066 | Banner physics | single unfurl, 'plain red silk, no emblem, no border' |
| SC_067 | Many bows | row from a low three-quarter angle, hands simple |
| SC_069 | Cavalry mass | mid-ground, spray |
| SC_071 | Line of horses | silhouettes against the sky, ≤3 sharp |
| SC_077 | Turret interior glimpse | only a slit of blue-lit face |
| SC_078 | Muzzle flash | single flash, smoke; no fireball fantasy |
| SC_079 | Explosion | one column of sand/water, no fire; crowd texture |
| SC_080 | Muzzle close | single flash |
| SC_081 | Horse throwing rider | one horse, rear + fall as one motion |
| SC_082 | Turret interior | sub-lock + interior ref; no readable text |
| SC_083 | Crowd in water | heads and shields texture |
| SC_085 | Crowded ford | distant texture |
| SC_087 | Crowd | texture |
| SC_088 | Hands dropping bombs | simple repeated motion |
| SC_089 | Explosions | sand columns, no fireballs |
| SC_090 | Six explosions | wide, small in frame |
| SC_091 | Lance strike | no gore, fall in mid-ground |
| SC_094 | Crowd | backs and shields |
| SC_095 | Mass | texture from above |
| SC_099 | Finger count | 'one fist and one folded finger' simple |
| SC_101 | Aerial mass | texture |
| SC_103 | Running crowd | file from the side, faces under helmets |
| SC_106 | Distant cavalry | 'dark stain flowing down the hillside' |
| SC_114 | Crowd | shield wall as a texture, faces hidden |
| SC_121 | Shield wall casualties | mid-distance, no gore |
| SC_122 | Arrow rain | many thin shafts, simple |
| SC_123 | Cavalry mass | texture on the slope |
| SC_124 | Galloping horse | mud spray on legs |
| SC_126 | Aerial | texture |
| SC_127 | Cavalry line | background texture |
| SC_128 | Cavalry charge | front rank ≤6 sharp, rest mud haze |
| SC_129 | Falling horses | mid-distance, mud, no gore |
| SC_130 | Horse over hole | single horse leap, wound off-frame |
| SC_131 | Rifle in hands | braced on the lip, side view |
| SC_132 | Goggles flying | simple break, helmet stays |
| SC_133 | Violence | off-frame; gun toppling is the action |
| SC_134 | Close combat | clash at frame edge, no gore |
| SC_135 | Blow | one swing, fall into mud, no blood |
| SC_136 | Wounded soldier | arrow shaft only, face turned away |
| SC_137 | Pistol in hands | two-handed grip from behind the shoulder, no close finger |
| SC_138 | Pistol mechanics | simple: slide back, magazine drops |
| SC_139 | Arrow hit | shaft appears, no blood spray |
| SC_140 | Blood | 'spreading on the uniform', not excessive |
| SC_142 | Many lances | line from a three-quarter angle |
| SC_145 | 300 cavalry | background |
| SC_146 | Sword blow | off-frame |
| SC_148 | Dead | covered with ponchos, faces hidden |
| SC_149 | Wound | arrow shaft in trouser leg, no open wound |
| SC_152 | Aerial | texture |
| SC_154 | Small brass | simple repeated motion |
| SC_155 | Screen | 'single dot', no digits |
| SC_158 | Three named faces | OK (≤3) |
| SC_160 | Two crowds | distance, texture |
| SC_161 | Three small objects | close, sharp, described in order |
| SC_168 | Numeral on plate | Arabic 3 only, no Hangul |
| SC_171 | Group | backs, mats, two named faces |
| SC_174 | Ring of men | kneeling shapes, faces down |
| SC_175 | Four kneeling men | high angle, faces partly down |
| SC_176 | Text | none, marks only |
| SC_178 | Screen | dot then dark, no digits |
| SC_180 | Pennant | small, plain crow mark, no writing |
| SC_186 | Group | backs and mats, two named faces |
| SC_189 | Interior | sub-lock + interior ref; readout blank |
| SC_191 | Crowd | texture |
| SC_193 | Aerial | texture |
| SC_197 | Interior | interior ref; no readable instruments |
| SC_198 | Many faces | distant, lifted, mud-dark |
| SC_201 | Tank motion | single direction, tracks in sand |
| SC_202 | Crowd | texture, faces hidden |
| SC_204 | Arrows on armor | 'skipping off like hail', many thin shafts |
| SC_205 | Water splash | single event, brown water |
| SC_207 | Oil slick | 'rainbow sheen', simple drift |
| SC_208 | Aerial masses | texture; tank clearly broadside |
| SC_210 | Many horses in water | mud/spray, ≤6 sharp |
| SC_212 | Many arrows | thin shafts, no faces sharp |
| SC_213 | Interior | interior ref |
| SC_215 | Climbing men | 2–3 figures |
| SC_218 | Shot + fall | fall off-frame |
| SC_219 | Arrow strike | shaft appears, no blood spray |
| SC_220 | Two men in water | upper bodies, simple motion |
| SC_221 | Dead horse | lying still, no gore |
| SC_223 | Dive under horse | insert, simple surfacing shot |
| SC_224 | Fight | insert; pin pull simple |
| SC_225 | Fire | white smoke + white glare, not orange fireball |
| SC_227 | Fire on water | 'thin sheet of flame on the oil', not explosion |
| SC_229 | Shooting | braced rifle, hits off-frame |
| SC_230 | Long file | from above, texture beyond the first six |
| SC_231 | Cavalry line | wide, ≤6 sharp |
| SC_232 | Cavalry collision | mid-distance, spray |
| SC_234 | Arrow hit | shaft appears, no blood spray |
| SC_236 | Horse fall | one horse, sideways |
| SC_237 | Three horses in water | close group, simple |
| SC_238 | Crowd | texture |
| SC_241 | Bayonet fixing | one motion, hands simple |
| SC_243 | Wound | shaft and dark stain only |
| SC_244 | Man climbing from horse to tank | single motion |
| SC_245 | Bow draw | side view, trembling described |
| SC_248 | Bow draw | side view |
| SC_249 | Death | no blood, fall out of frame |
| SC_250 | Two lines of many men | wide, faces small |
| SC_252 | Crowd + cavalry | aerial texture |
| SC_253 | Many faces | turned away or lowered |
| SC_254 | Patch | small, exact design |
| SC_262 | Line of men | wide, backs of the general and captain, faces small |
| SC_270 | Hangul on hull | none; only the white arrow mark |
| SC_274 | Two times in one still | accepted (KB), dark corner |
| SC_275 | No faces; robe = the emperor's (no person) | — |
| SC_276 | Three named in one frame | wide, faces sharp enough |
| SC_281 | Wreck | ref VEH_001_ep5; numeral 1 only |
| SC_282 | Numerals | Arabic 3 and 1 only; pencil figure blurred; NO Hangul |
| SC_283 | Seven named figures | wide, each with one identifier (armband, helmet in hand, boonie, iron bar, olive scarf) |
| SC_284 | Six named faces in a drift | each briefly, sharp one at a time |
| SC_285 | Calligraphy | 'columns of brush calligraphy', no legible characters; subtitle at edit |
| SC_286 | Forty oxen | line from behind, texture |

### Quy tắc né chung (áp dụng toàn tập)
- **Đại quân trong nước** (방진 30만, trung quân ngang ngực): luôn aerial/wide, 'heads and shields in brown water', mặt phụ quay đi; không cận đám đông; số ngựa ≤3 khi cận.
- **K2 + nước/dầu/lửa** (SC_205–227, 244–251): 1 hành động vật lý rõ mỗi clip (sóng bùn / xích lún / dầu loang / khói trắng / vòng lửa), máy tĩnh hoặc 1 chuyển động; VEH_STATE đúng pha; không vẽ chữ trên tháp ngoài số 1.
- **Nội thất K2** (tháp/khoang lái): sub-lock `_k2_turret_int`/`_k2_driver_int` + ref `VEH_001_interior_ref`; màn hình 'small blank readout' — số 잔탄 overlay.
- **Chữ/số**: bản đồ lụa (brush strokes, no writing), sổ tay (blurred pencil lines), bài thơ (columns of brush calligraphy), biển '3' (chỉ số Ả Rập), end card → overlay.
- **Tay cầm súng/cung**: K2C1 gác bao cát/lau, bắn = chớp lửa hoặc wide; K5 hai tay (SC_137–138) máy vai, không cận ngón tay trên cò; cung 탁발흠/해모루 (SC_245/248) cận mặt + dây cung tới má, tay run mô tả bằng 'trembling'.
- **Ngựa Tùy vs Tiên Ti vs Goguryeo**: VEH_207 (lụa đỏ, gương ngực, ngựa cao) / VEH_206 (ngựa lùn, da nâu, lông cáo, tai nhét vải) / VEH_101 (giáp sắt kín) — QC loại plate armor phương Tây (vehicle_bible C.5).
- **Vết thương**: 해모루 cán tên dưới xương đòn TRÁI (bible), 박기철 tên đùi TRÁI (bible/ref — script ghi bắp chân phải → cần quyết), 탁발흠 băng cẳng tay PHẢI; không gore, không cận vết thương hở.
- **Hangul trên xe**: KHÔNG vẽ; '천둥' chỉ ở thoại/radio.
- **Nhân vật lịch sử**: diện mạo hư cấu theo lock; 수 후군 장수 (신세웅) = EXTRA lock tạm, không ref (P-44).
