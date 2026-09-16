# 2화 「요동성」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)
> Đếm theo `04_veo/scenes_ep2.json` (287 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.

## 1. Nhân vật (CHAR) — số SC xuất hiện
| CHAR | SC | Derived state trong 2화 (SC) |
|---|---|---|
| CHAR_001 | 63 | CHAR_001_dust_light_ep2 (7), CHAR_001_dusty_ep2 (56) |
| CHAR_002 | 24 | CHAR_002_dust_ep2 (11), CHAR_002_soot_ep2 (13) |
| CHAR_003 | 46 | CHAR_003_bandage_thin_ep2 (17), CHAR_003_bandaged_ep2 (7), CHAR_003_burned_hands_ep2 (3), CHAR_003_oil_ep2 (18), CHAR_003_soot_ep2 (1) |
| CHAR_004 | 15 | CHAR_004_bloody_sleeves_ep2 (13), CHAR_004_headlamp_ep2 (2) |
| CHAR_005 | 9 | CHAR_005_ash_ep2 (4), CHAR_005_dust_ep2 (5) |
| CHAR_006 | 12 | CHAR_006_paint_faded_ep2 (12) |
| CHAR_101 | 42 | CHAR_101_ash_ep2 (20), CHAR_101_cloak_incognito_ep2 (5), CHAR_101_plain_ep2 (17) |
| CHAR_104 | 22 | CHAR_104_burnt_cloak_ep2 (2), CHAR_104_helmet_ep2 (4), CHAR_104_siege_ep2 (16) |
| CHAR_105 | 18 | CHAR_105_ash_ep2 (18) |
| CHAR_106 | 16 | CHAR_106_limp_ep2 (16) |
| CHAR_107 | 9 | CHAR_107_hemp_scarf_ep2 (4), CHAR_107_scarf_ep2 (5) |
| CHAR_201 | 11 | CHAR_201_field_dust_ep2 (6), CHAR_201_robe_fan_ep2 (5) |
| CHAR_202 | 3 | — (base) |
| CHAR_203 | 3 | — (base) |
| CHAR_205 | 16 | CHAR_205_camp_ep2 (9), CHAR_205_fire_ep2 (2), CHAR_205_magazine_ep2 (5) |

### Derived state text-only của bible (không ref riêng → đính ref gốc/biến thể gần nhất)
- `CHAR_201_field_dust_ep2` → ref `CHAR_201_ref` (6 SC): Gilded cuirass, fine dust on the yellow hem and red boots, irritated expression, a round silk fan in the left hand.

### Derived state 2화 do veo-prompt-engineer đặt thêm (không có trong bible — đề xuất character-designer nhập; đính ref gốc/biến thể gần nhất)
- `CHAR_201_robe_fan_ep2` → ref `CHAR_201_robe_only_ep3` (5 SC): Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged, a round silk fan in the left hand.
- `CHAR_001_dust_light_ep2` → ref `CHAR_001_ref` (7 SC): Fine grey stone dust on helmet and shoulders after three weeks in the field, sleeves rolled to the elbow, one-day stubble, sweat at the temples.
- `CHAR_002_dust_ep2` → ref `CHAR_002_ref` (11 SC): Grey stone dust on helmet and shoulders, sleeves rolled, forearms smudged with old gunpowder residue, two-day stubble.
- `CHAR_003_oil_ep2` → ref `CHAR_003_ref` (18 SC): Mechanic gloves dark with engine oil, grey stone dust on the patrol cap and shoulders, two-day salt-and-pepper stubble, a small green notebook in the chest pocket.
- `CHAR_003_burned_hands_ep2` → ref `CHAR_003_soot_ep2` (3 SC): Face blackened with soot from a vehicle fire, left eyebrow half singed, both hands red, blistered and shaking, sleeves scorched, patrol cap pushed back.
- `CHAR_003_bandaged_ep2` → ref `CHAR_003_soot_ep2` (7 SC): Both hands wrapped in clean white bandages to the wrists, left eyebrow half singed, soot smudges still on the face, two-day salt-and-pepper stubble, patrol cap pushed back.
- `CHAR_003_bandage_thin_ep2` → ref `CHAR_003_ref` (17 SC): Thin white bandages wrapped around both palms, left eyebrow half regrown, grey stone dust on the patrol cap and shoulders, salt-and-pepper stubble.
- `CHAR_004_headlamp_ep2` → ref `CHAR_004_ref` (2 SC): Headlamp switched on over the helmet, grey stone dust on shoulders, blue nitrile gloves, medic bag on the shoulder.
- `CHAR_005_ash_ep2` → ref `CHAR_005_ref` (4 SC): Ash and soot on face and uniform, one corner of the hard drone case on his back scorched black, red-rimmed eyes.
- `CHAR_005_dust_ep2` → ref `CHAR_005_ref` (5 SC): Grey stone dust on helmet and shoulders, sleeves rolled, faint stubble.
- `CHAR_006_paint_faded_ep2` → ref `CHAR_006_facepaint_ep1` (12 SC): The green and black face paint smeared and fading into grey stone dust, two-day stubble, grass stalks gone from the scrim scarf.
- `CHAR_101_plain_ep2` → ref `CHAR_101_ref` (17 SC): Helmet plume removed: plain iron lamellar armor without the tall plume or white feathers, a black lacquered bamboo dispatch tube at the belt, road dust on the boots, cloak folded away.
- `CHAR_101_ash_ep2` → ref `CHAR_101_ref` (20 SC): Full armor with the tall dark plume and two white feathers, a black lacquered bamboo dispatch tube at the belt, light grey ash on the shoulder guards.
- `CHAR_104_helmet_ep2` → ref `CHAR_104_ref` (4 SC): Iron helmet worn on the head instead of under the arm, grey stone dust in the beard, the heavy gray wool cloak thrown back, iron ring of keys at the belt.
- `CHAR_104_burnt_cloak_ep2` → ref `CHAR_104_ref` (2 SC): Iron helmet worn on the head, the gray wool cloak scorched with a smoking burnt hole at the hem, stone dust in the beard, sweat, fierce eyes.
- `CHAR_105_ash_ep2` → ref `CHAR_105_ref` (18 SC): Light grey ash and stone dust on the armor, sweat, the single white feather singed brown at the tip.
- `CHAR_106_limp_ep2` → ref `CHAR_106_forge_ep2` (16 SC): Leather apron blackened with soot, sleeves pushed up showing burn-scarred forearms, a small hammer at the belt, walking with a slight limp on the right leg.
- `CHAR_107_hemp_scarf_ep2` → ref `CHAR_107_ref` (4 SC): A coarse hemp scarf over the head and shoulders, small cloth herb pouch at the waist, stone dust on the skirt hem, small smear of blood on the fingertips.
- `CHAR_205_camp_ep2` → ref `CHAR_205_ref` (9 SC): Fox-fur cap on, a Goguryeo arrowhead on a leather cord at the neck, road dust on the leather armor, calm watchful face.
- `CHAR_205_fire_ep2` → ref `CHAR_205_ref` (2 SC): Fox-fur cap on, a Goguryeo arrowhead on a leather cord at the neck, soot smudges on the cheek and armor, firelight in the eyes, no torch in hand.
- `CHAR_205_magazine_ep2` → ref `CHAR_205_ref` (5 SC): Fox-fur cap on, a Goguryeo arrowhead on a leather cord at the neck, an empty black steel rifle magazine hanging from the bronze plaque belt, dust on the leather armor.

### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)
| Extra | SC | ref đính |
|---|---|---|
| GOG_INFANTRY | 27 | WPN_102_ref |
| SUI_PUSHERS | 17 | — |
| SUI_SIEGE_GENERAL | 10 | EXTRA_sui_siege_general_ref |
| SUI_TOWER_MEN | 9 | WPN_201_ref |
| GOG_ARCHERS | 8 | WPN_102_ref |
| GOG_CIVILIANS | 8 | — |
| K2_COMMANDER | 6 | — |
| SUI_COURIER | 5 | — |
| ROK_SOLDIERS | 5 | — |
| BOY_SCOUT | 4 | EXTRA_boy_scout_ref |
| ROK_SENTRY | 4 | — |
| GOG_STONEMASONS | 4 | — |
| MORTAR_CREW | 4 | — |
| PZF_GUNNER | 4 | — |
| K2_CREW | 4 | — |
| SUI_GENERALS | 4 | WPN_201_ref |
| GOG_SPEARMEN | 4 | WPN_102_ref |
| BOY_SCOUT_FEVER | 3 | EXTRA_boy_scout_ref |
| SUI_CRAFTSMEN | 3 | — |
| XIANBEI_DEPUTY | 3 | VEH_206_ref |
| BOY_SCOUT_THIN | 3 | EXTRA_boy_scout_ref |
| K2_GUNNER | 3 | — |
| GOG_CAVALRYMEN | 3 | VEH_101_ref |
| GOG_SENTRY | 2 | WPN_102_ref |
| SUI_DIGGERS | 2 | — |
| SUI_OFFICIAL | 2 | — |
| SUI_EUNUCH | 2 | — |
| GOG_SOLDIER_RUNNER | 2 | — |
| GOG_WOUNDED | 2 | — |
| K21_CREW | 2 | — |
| SUI_OFFICER_HORSE | 2 | — |
| MORTAR_GUNNER | 2 | — |
| XIANBEI_SCOUTS | 2 | VEH_206_ref |
| XIANBEI_FIRE_PARTY | 2 | VEH_206_ref |
| PZF_GUNNERS | 2 | — |
| ROK_SOLDIER | 2 | — |
| SUI_MARCHERS | 2 | WPN_201_ref |
| SUI_SCRIBE | 1 | — |
| ROK_SICK | 1 | — |
| SUI_SURVIVORS | 1 | WPN_201_ref |
| GOG_FARMER | 1 | — |
| SUI_INTERPRETER | 1 | — |
| XIANBEI_FIRE_ARCHERS | 1 | VEH_206_ref |
| XIANBEI_THREE | 1 | VEH_206_ref |
| ROK_BURNED_TWO | 1 | — |
| GOG_TORCH_SQUAD | 1 | — |
| SUI_CROSSBOWMEN | 1 | WPN_201_ref |
| K3_GUNNER | 1 | — |
| ROK_BURNED | 1 | — |

## 2. Địa điểm (LOC) — số SC
| LOC | SC | Sub-lock (SC) |
|---|---|---|
| LOC_001 | 6 | LOC_001_march_night (1), LOC_001_muster_night (1), LOC_001_supply_road (1), LOC_001_xianbei_camp (3) |
| LOC_002 | 184 | LOC_002 (11), LOC_002_barbican_in (1), LOC_002_bastion_se (12), LOC_002_bastion_se_k2 (17), LOC_002_breach (2), LOC_002_breach_in (8), LOC_002_breach_repaired (1), LOC_002_causeway (5), LOC_002_courtyard (4), LOC_002_drawing (2), LOC_002_eastgate_chisel (2), LOC_002_eastgate_night_k2 (1), LOC_002_eastwall_night (1), LOC_002_gate_tower (1), LOC_002_granary_fire (2), LOC_002_hall (15), LOC_002_hall_day (3), LOC_002_infirmary (5), LOC_002_k2_interior (2), LOC_002_marker_field (1), LOC_002_northgate (1), LOC_002_pagoda_view (1), LOC_002_ramp (7), LOC_002_ramp_work (5), LOC_002_se_corner_out (4), LOC_002_south_plain (13), LOC_002_southwall (29), LOC_002_southwall_fog (3), LOC_002_stair (1), LOC_002_sui_lines (5), LOC_002_sui_yard (3), LOC_002_tunnel (2), LOC_002_veranda (4), LOC_002_wall_base_in (6), LOC_002_wall_face_out (2), LOC_002_well_yard (2) |
| LOC_003 | 77 | LOC_003_drums (2), LOC_003_drums_fire (3), LOC_003_fire_wide (2), LOC_003_ford_northbank (1), LOC_003_fork_night (1), LOC_003_hearth (2), LOC_003_hill_south_night (1), LOC_003_hillside_pov (1), LOC_003_hilltop_enemy (1), LOC_003_k2 (3), LOC_003_k2_day (14), LOC_003_line (9), LOC_003_line_jun (8), LOC_003_line_night (5), LOC_003_medic (2), LOC_003_medic_day (2), LOC_003_mortar_day (4), LOC_003_op_west (1), LOC_003_tent (1), LOC_003_tent_ext_day (3), LOC_003_trail_day (3), LOC_003_trail_night (4), LOC_003_valley_apr (1), LOC_003_wreck_dawn (2), LOC_003_wreck_day (1) |
| LOC_004 | 19 | LOC_004 (2), LOC_004_gate_night (1), LOC_004_hall_day (4), LOC_004_pavilion_day (1), LOC_004_pavilion_int (7), LOC_004_platform (4) |

## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/UAV/EQP) — số SC
| ID | SC |
|---|---|
| VEH_001 | 47 |
| VEH_201 | 39 |
| VEH_002 | 30 |
| WPN_201 | 19 |
| VEH_203 | 15 |
| EQP_002 | 13 |
| VEH_202 | 12 |
| VEH_003 | 8 |
| WPN_005 | 8 |
| VEH_206 | 7 |
| UAV_001 | 6 |
| WPN_101 | 5 |
| VEH_004 | 4 |
| WPN_002 | 4 |
| WPN_001 | 3 |
| VEH_101 | 2 |
| EQP_001 | 1 |
| WPN_003 | 1 |
- VEH_002: 천둥 2/3/4 phân biệt bằng `veh_state` (numeral 2 · numeral 3 + chốt sắt · numeral 4 → `VEH_002_burned`); VEH_201 tháp: `TOWER_HIDE` (P1–P5) → `TOWER_MUD` + ref `VEH_201_mud_ep2` (SC_099+); VEH_202: `RAM_MUD` từ SC_074; VEH_001: `K2_CLEAN` → `K2_WET_NET` (P6–P7) → `K2_SOOT` (SC_249+).

## 4. Đạo cụ (PROP) — số SC
| PROP | SC |
|---|---|
| PROP_016 | 18 |
| PROP_021 | 15 |
| PROP_007 | 12 |
| PROP_006 | 8 |
| PROP_019 | 8 |
| PROP_009 | 8 |
| PROP_012 | 5 |
| PROP_008 | 4 |
| PROP_011 | 3 |
| PROP_015 | 3 |
| PROP_010 | 2 |
| PROP_013 | 2 |
| PROP_022 | 2 |
| PROP_017 | 1 |
| PROP_018 | 1 |

## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)
| # | ref id | thư mục | số SC đính | trạng thái |
|---|---|---|---|---|
| 1 | CHAR_001_dusty_ep2 | characters | 56 | có job |
| 2 | VEH_001_ref | vehicles | 47 | có job |
| 3 | WPN_102_ref | vehicles | 39 | có job (ep1 extra, DUYỆT) |
| 4 | LOC_003_valley_ep2 | locations | 38 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 5 | CHAR_101_ref | characters | 37 | có job |
| 6 | LOC_002_detail | locations | 36 | có job |
| 7 | CHAR_003_ref | characters | 35 | có job |
| 8 | WPN_201_ref | vehicles | 33 | có job |
| 9 | LOC_002_south_plain_ep2 | locations | 31 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 10 | LOC_002_southwall_ep2 | locations | 29 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 11 | LOC_002_bastion_se_ep2 | locations | 29 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 12 | VEH_002_ref | vehicles | 25 | có job |
| 13 | LOC_003_wide | locations | 24 | có job |
| 14 | LOC_002_interior | locations | 22 | có job |
| 15 | VEH_201_mud_ep2 | vehicles | 20 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 16 | VEH_201_ref | vehicles | 19 | có job |
| 17 | CHAR_105_ref | characters | 18 | có job |
| 18 | CHAR_106_forge_ep2 | characters | 16 | có job |
| 19 | CHAR_104_siege_ep2 | characters | 16 | có job |
| 20 | CHAR_205_ref | characters | 16 | có job |
| 21 | VEH_203_ref | vehicles | 15 | có job |
| 22 | PROP_021_ref | props | 15 | có job |
| 23 | EQP_002_ref | vehicles | 13 | có job |
| 24 | CHAR_004_bloody_sleeves_ep2 | characters | 13 | có job |
| 25 | VEH_206_ref | vehicles | 13 | có job |
| 26 | CHAR_002_soot_ep2 | characters | 13 | có job |
| 27 | LOC_003_valley_burned_ep2 | locations | 13 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 28 | CHAR_006_facepaint_ep1 | characters | 12 | có job |
| 29 | VEH_202_ref | vehicles | 12 | có job |
| 30 | LOC_002_wide | locations | 12 | có job |
| 31 | PROP_007_ref | props | 12 | có job |
| 32 | CHAR_002_ref | characters | 11 | có job |
| 33 | LOC_004_detail | locations | 11 | có job |
| 34 | CHAR_003_soot_ep2 | characters | 11 | có job |
| 35 | LOC_002_breach_ep2 | locations | 11 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 36 | EXTRA_boy_scout_ref | characters | 10 | có job (ep1 extra, DUYỆT) |
| 37 | EXTRA_sui_siege_general_ref | characters | 10 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 38 | CHAR_005_ref | characters | 9 | có job |
| 39 | PROP_006_ref | props | 8 | có job |
| 40 | PROP_019_ref | props | 8 | có job |
| 41 | PROP_009_ref | props | 8 | có job |
| 42 | VEH_003_ref | vehicles | 8 | có job |
| 43 | WPN_005_ref | vehicles | 8 | có job |
| 44 | CHAR_001_ref | characters | 7 | có job |
| 45 | CHAR_104_ref | characters | 6 | có job |
| 46 | UAV_001_ref | vehicles | 6 | có job |
| 47 | LOC_001_wide | locations | 6 | có job |
| 48 | CHAR_201_ref | characters | 6 | có job |
| 49 | CHAR_201_robe_only_ep3 | characters | 5 | có job |
| 50 | WPN_101_ref | vehicles | 5 | có job |
| 51 | LOC_002_infirmary_ep2 | locations | 5 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 52 | CHAR_101_cloak_incognito_ep2 | characters | 5 | có job |
| 53 | CHAR_107_scarf_ep2 | characters | 5 | có job |
| 54 | VEH_002_burned | vehicles | 5 | có job |
| 55 | PROP_012_ref | props | 5 | có job |
| 56 | LOC_004_wide | locations | 4 | có job |
| 57 | CHAR_107_ref | characters | 4 | có job |
| 58 | VEH_004_ref | vehicles | 4 | có job |
| 59 | WPN_002_ref | vehicles | 4 | có job |
| 60 | PROP_008_ref | props | 4 | có job |
| 61 | LOC_004_platform_ep2 | locations | 4 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 62 | PROP_011_ref | props | 3 | có job |
| 63 | WPN_001_ref | vehicles | 3 | có job |
| 64 | LOC_002_eastgate_chisel_ep2 | locations | 3 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 65 | VEH_101_ref | vehicles | 3 | có job |
| 66 | CHAR_202_ref | characters | 3 | có job |
| 67 | CHAR_203_ref | characters | 3 | có job |
| 68 | PROP_015_ref | props | 3 | có job |
| 69 | LOC_002_tunnel_ep2 | locations | 2 | **CHƯA CÓ — job trong ref_jobs_ep2_extra.json** |
| 70 | CHAR_004_ref | characters | 2 | có job |
| 71 | PROP_010_ref | props | 2 | có job |
| 72 | PROP_013_ref | props | 2 | có job |
| 73 | PROP_022_ref | props | 2 | có job |
| 74 | PROP_017_ref | props | 1 | có job |
| 75 | LOC_003_detail | locations | 1 | có job |
| 76 | LOC_003_ford_night | locations | 1 | có job (ep1 extra, DUYỆT) |
| 77 | EQP_001_ref | vehicles | 1 | có job |
| 78 | WPN_003_ref | vehicles | 1 | có job |

### Ref CHƯA CÓ trong ref_jobs.json (2화 — job đã ghi `05_references/extra/ref_jobs_ep2_extra.json`; world-designer/character-designer duyệt, glabs-operator tạo trước lô ảnh cảnh)
- `LOC_002_southwall_ep2` (locations, 16:9) mặt tường nam đang bị vây: lan can đá, 치, giá tên, chum, nồi, trống — phía ngoài là đồng bằng giẫm nát, hào lấp, hàng tháp Tùy, biển lều — sub-lock `LOC_002_southwall` (P1–P10, nhiều SC nhất). — 29 SC.
- `LOC_002_south_plain_ep2` (locations, 16:9) đồng bằng nam thành từ phía Tùy: hào lấp thành đường đắp, hàng tháp 8 bánh + thang, cờ, lều; tường granite + tháp cổng phía sau — sub-lock `LOC_002_south_plain`, `_sui_lines`, `_sui_yard`, `_causeway`, `_se_corner_out`, `_marker_field`. — 31 SC.
- `LOC_002_bastion_se_ep2` (locations, 16:9) 치 đông-nam SAU khi cải tạo: khe châu mai đục vuông cỡ nòng pháo, dốc đất 20° phía sau (tường trong tháo 10 hàng), K2 trên 치 — sub-lock `LOC_002_bastion_se_k2`, `_ramp`, `_ramp_work` (P9–P10). — 29 SC.
- `LOC_002_eastgate_chisel_ep2` (locations, 16:9) vòm cổng đông nhỏ có giàn gỗ, hai vách đục lộ đá trắng mới (반 미터) — sub-lock `LOC_002_eastgate_chisel`, `_eastgate_night_k2` (SC_179, 182–183, 195). — 3 SC.
- `LOC_002_infirmary_ep2` (locations, 16:9) nội thất nhà gỗ bệnh xá cạnh tường: chiếu cói, ổ rơm, chậu, thảo dược treo, cửa chớp lưới — sub-lock `LOC_002_infirmary` (SC_043–047). — 5 SC.
- `LOC_002_tunnel_ep2` (locations, 16:9) hầm Tùy: cột chống gỗ, đèn dầu, vách rỉ nước, giỏ đất — sub-lock `LOC_002_tunnel` (SC_010, 230). — 2 SC.
- `LOC_002_breach_ep2` (locations, 16:9) lỗ hổng 80 m tường nam: mặt ngoài đổ thành dốc đá, tường trong còn — sub-lock `LOC_002_breach`, `_breach_in`, `_breach_repaired` (P10–P12). — 11 SC.
- `LOC_003_valley_ep2` (locations, 16:9) thung lũng 2화 tháng 4: lưới bạc màu, 3 K21 hàng ngang, 2 phuy sau bao cát cách xe 30 bước, sồi chớm lá — sub-lock `LOC_003_valley_apr`, `_line`, `_line_night`, `_drums`, `_drums_fire`, `_k2_day`, `_tent_ext_day`, `_hillside_pov`. — 38 SC.
- `LOC_003_valley_burned_ep2` (locations, 16:9) thung lũng SAU hỏa công: xác 천둥 4 đen, xe tải cháy sém, hố phuy, tro — sub-lock `LOC_003_fire_wide`, `_wreck_dawn`, `_wreck_day`, `_line_jun` (P7–P12). — 13 SC.
- `LOC_004_platform_ep2` (locations, 16:9) đài quan sát gỗ của 양제 phía nam thành: lọng vàng, cờ vàng, đuốc chân đài, tường thành phía xa — sub-lock `LOC_004_platform` (SC_200, 213, 221, 248). — 4 SC.
- `VEH_201_mud_ep2` (vehicles, 16:9, phông trắng) 팔륜누차 PHỦ CHIẾU BÙN ĐẤT (derived VEH_201): mặt trước/hông/đỉnh phủ chiếu rơm ngâm bùn + lớp đất ướt, màu nâu đất thay da đen — dùng cho mọi tháp từ SC_099 (P5 đêm) tới hết tập (~25 SC). — 20 SC.
- `EXTRA_sui_siege_general_ref` (characters, 3:4) 수 공성총관 ~45 tuổi, gầy rắn, râu đen ngắn vuông, áo choàng đỏ sẫm, chỏm tua ĐEN — PHẢI khác 전군총관 1화 (55, râu đen-xám, chỏm đỏ) và 우중문 (râu trắng) — 12 SC (P2, P4, P5, P7, P10). — 10 SC.

### Thứ tự chạy ref đề xuất (P1 → P3)
- **P1 (≥15 SC):** CHAR_001_dusty_ep2, VEH_001_ref, WPN_102_ref, LOC_003_valley_ep2, CHAR_101_ref, LOC_002_detail, CHAR_003_ref, WPN_201_ref, LOC_002_south_plain_ep2, LOC_002_southwall_ep2, LOC_002_bastion_se_ep2, VEH_002_ref, LOC_003_wide, LOC_002_interior, VEH_201_mud_ep2, VEH_201_ref, CHAR_105_ref, CHAR_106_forge_ep2, CHAR_104_siege_ep2, CHAR_205_ref, VEH_203_ref, PROP_021_ref
- **P2 (5–14 SC):** EQP_002_ref, CHAR_004_bloody_sleeves_ep2, VEH_206_ref, CHAR_002_soot_ep2, LOC_003_valley_burned_ep2, CHAR_006_facepaint_ep1, VEH_202_ref, LOC_002_wide, PROP_007_ref, CHAR_002_ref, LOC_004_detail, CHAR_003_soot_ep2, LOC_002_breach_ep2, EXTRA_boy_scout_ref, EXTRA_sui_siege_general_ref, CHAR_005_ref, PROP_006_ref, PROP_019_ref, PROP_009_ref, VEH_003_ref, WPN_005_ref, CHAR_001_ref, CHAR_104_ref, UAV_001_ref, LOC_001_wide, CHAR_201_ref, CHAR_201_robe_only_ep3, WPN_101_ref, LOC_002_infirmary_ep2, CHAR_101_cloak_incognito_ep2, CHAR_107_scarf_ep2, VEH_002_burned, PROP_012_ref
- **P3 (<5 SC):** LOC_004_wide, CHAR_107_ref, VEH_004_ref, WPN_002_ref, PROP_008_ref, LOC_004_platform_ep2, PROP_011_ref, WPN_001_ref, LOC_002_eastgate_chisel_ep2, VEH_101_ref, CHAR_202_ref, CHAR_203_ref, PROP_015_ref, LOC_002_tunnel_ep2, CHAR_004_ref, PROP_010_ref, PROP_013_ref, PROP_022_ref, PROP_017_ref, LOC_003_detail, LOC_003_ford_night, EQP_001_ref, WPN_003_ref

## 6. SC cần ảnh ĐẠI QUÂN / AERIAL (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)
| SC | t | type | nội dung |
|---|---|---|---|
| SC_006 | 0:40 | video8s | Binocular POV: circular double-lens mask, slow pan right |
| SC_007 | 0:48 | still_kenburns | Still for ken-burns: very high aerial wide, pulling out slowly |
| SC_012 | 1:22 | video8s | Wide from behind three figures on the wall, static |
| SC_013 | 1:30 | still_kenburns | Still for ken-burns: very high aerial wide in clear daylight, pulling out from the fortress to a felled forest |
| SC_015 | 1:50 | video8s | Low aerial tracking shot along the front rank of an assault wave |
| SC_023 | 2:54 | still_kenburns | Still for ken-burns: high aerial wide following a single dust plume west |
| SC_055 | 7:18 | video8s | Low aerial gliding sideways along a line of advancing siege towers |
| SC_068 | 9:02 | video8s | Wide from the wall top looking down at the causeway, static |
| SC_072 | 9:34 | video8s | Wide along the wall top and the plain, static |
| SC_092 | 12:22 | video8s | Wide on the burning towers, then a slow pan to the wall ending on one man |
| SC_097 | 13:02 | still_kenburns | Still for ken-burns: wide at sunset along the tower line, pulling out |
| SC_098 | 13:12 | video8s | Medium-wide by torchlight, static |
| SC_100 | 13:28 | still_kenburns | Still for ken-burns: high aerial at dawn sliding along the tower line |
| SC_103 | 14:00 | still_kenburns | Still for ken-burns: high aerial by day sliding slowly along the earth-covered towers |
| SC_125 | 17:00 | still_kenburns | Still for ken-burns: wide from the pagoda at night, pulling out |
| SC_134 | 18:18 | still_kenburns | Still for ken-burns: high aerial at dawn pulling out from the golden pavilion |
| SC_143 | 19:34 | video8s | Low wide, camera shaking, static base |
| SC_146 | 19:58 | video8s | Wide from across the valley, static |
| SC_151 | 20:38 | still_kenburns | Still for ken-burns: wide from the valley rim at night, pulling out slowly |
| SC_174 | 24:00 | still_kenburns | Still for ken-burns: high aerial by day sliding along the tower line to a south-east cluster |
| SC_179 | 24:44 | still_kenburns | Still for ken-burns: high angle from the wall top over the worksite, sliding to the east gate |
| SC_194 | 26:50 | still_kenburns | Still for ken-burns: high aerial at night pulling out from a golden canopy |
| SC_199 | 27:38 | video8s | High aerial gliding over the plain at dawn |
| SC_209 | 28:58 | video8s | Wide from the wall over the tower line, static |
| SC_218 | 30:10 | video8s | Wide from the south wall looking across to the bastion, static |
| SC_220 | 30:26 | video8s | Medium aerial over the Sui field, static |
| SC_223 | 30:50 | video8s | Wide from the wall, static |
| SC_231 | 31:54 | video8s | Wide from the bastion looking west along the wall, static |
| SC_232 | 32:02 | video8s | Low aerial rushing toward the breach with the assault |
| SC_236 | 32:36 | video8s | Wide from the wall, static |
| SC_238 | 32:52 | video8s | Wide from the bastion along the wall to the breach (keyframe = beat A) |
| SC_240 | 33:08 | video8s | Low aerial tracking the head of a cavalry column, single move |
| SC_242 | 33:24 | video8s | Lateral tracking shot along the corner, single move |
| SC_247 | 34:04 | still_kenburns | Still for ken-burns: high wide at sunset, pulling out very slowly |
| SC_256 | 35:20 | still_kenburns | Still for ken-burns: high aerial at night pushing in on the golden pavilion |
| SC_260 | 35:54 | still_kenburns | Still for ken-burns: medium-wide by torchlight, sliding along the line of men to the banners |
| SC_267 | 36:52 | still_kenburns | Still for ken-burns: very high aerial under the moon, pulling out slowly |
| SC_281 | 38:54 | still_kenburns | Still for ken-burns: very high aerial under the moon, drifting east |
| SC_282 | 39:04 | still_kenburns | Still for ken-burns: high aerial at the tail of the columns, pushing in on a small party |

## 7. SC có OVERLAY ở edit (số/chữ KHÔNG vẽ bằng AI)
| SC | overlay |
|---|---|
| SC_035 | Bảng gỗ (KO, chữ phấn): 포탄 22 · 40mm 140/140/200 · 박격포 110 · PZF 18 · 드론 3 · 전차 360 · 발전기 30일 |
| SC_075 | Bảng gỗ: PZF 18 → 17 (phấn, xóa và viết) |
| SC_154 | Bảng gỗ (chữ 태오): K21 2 · 드럼 1 · 드론 2 · 40mm −200 |
| SC_172 | Bảng gỗ (chữ 태오): K21 2 · 드럼 1 · 드론 2 · 항생제 0 · 포탄 22 · 10 (khoanh tròn 2 vòng) |
| SC_217 | Màn hình bộ đếm: 잔탄 22 |
| SC_222 | Insert bộ đếm: 잔탄 21 |
| SC_229 | Màn hình bộ đếm: 잔탄 16 |
| SC_238 | Insert bộ đếm: 잔탄 12 |
| SC_287 | END CARD: 살수 612 · 3화 남하 |

## 8. SC RỦI RO AI & cách né trong prompt
| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |
|---|---|---|
| SC_001 | màn đen + mặt cận trong sương | 1 mặt, tĩnh; beat A = đen ở edit nếu veo không giữ |
| SC_002 | 2 người + sương | mặt lính gác khuất mũ, 1 chuyển động máy |
| SC_003 | hàng chục chân người + tháp khổng lồ | chỉ chân/lưng, không mặt; tilt 1 chiều |
| SC_004 | mũi nỏ cắm gỗ cạnh tay | 1 vật thể bay, tay nắm dùi rõ, không cận ngón |
| SC_005 | 2 người chạy cầu thang | tracking 1 chiều, không tay cầm súng cận |
| SC_006 | POV ống nhòm + đám đông | mask tròn, chi tiết mờ, 'no readable detail' |
| SC_007 | đại quân | aerial rất cao, tháp = đảo trong sương |
| SC_008 | chữ trên bản vẽ | 'no readable characters', chỉ nét vẽ |
| SC_009 | chữ | không ký tự; hình cắt ngang hầm đơn giản |
| SC_010 | nhiều người trong không gian hẹp | lưng/tay, mặt cúi, ánh đèn thấp |
| SC_011 | 2 mặt + tháp nền | tháp mờ hậu cảnh, 2 mặt rõ |
| SC_012 | 40 tháp + đại quân | wide từ sau lưng, tháp xa nhỏ dần |
| SC_013 | đại quân | aerial rất cao, lều = hoa văn ô lưới |
| SC_014 | chữ trên thẻ | thẻ gỗ trơn; hàng hoạn quan = mặt cúi xa |
| SC_015 | đám đông chạy | aerial thấp, mũ che mặt, bụi |
| SC_016 | nhiều lính + nước sôi | máy sau lưng hàng người, 1 thang, không gore |
| SC_017 | đá rơi | ít mảnh, 1 vết nứt rõ, không người rơi |
| SC_018 | 2 người | 1 mặt chính, lính phụ mờ |
| SC_019 | đám đông trên thang + tướng | tướng xa trên ngựa, mặt lính thang quay đi |
| SC_020 | 2 mặt | medium, nền lính rút mờ |
| SC_021 | chân dung | 1 mặt, biểu cảm nhỏ |
| SC_022 | chữ trên lụa | dải lụa trơn + ấn son; ngựa phi = tracking 1 con |
| SC_023 | đại quân | aerial rất cao, khối ô vuông |
| SC_024 | 2 lính nằm | lính gác mặt khuất, 1 mặt |
| SC_025 | đám đông dưới sân | nhỏ, từ trên xuống, không mặt |
| SC_026 | đám đông lao động | tracking, mặt quay đi, 1 nhân vật ID rõ |
| SC_027 | tay cầm búa cận | búa nhỏ, 3 nhịp gõ chậm |
| SC_028 | 2 người khiêng đá | 1 tảng đá, tay không cận |
| SC_030 | hàng lính ngồi | lưng/mũ, xa mờ |
| SC_031 | walk-and-talk 2 người | tracking lùi đều, đám đông sau lưng mờ |
| SC_032 | mồ hôi cận | 1 mặt, giọt mồ hôi đơn giản |
| SC_033 | 3 người nội thất | hoàng đế mặt che quạt, 2 người quỳ/cúi |
| SC_035 | chữ trên bảng | 'rain-smeared chalk marks that cannot be read'; số overlay |
| SC_036 | walk-and-talk + xe | tracking 1 chiều, sổ đóng |
| SC_037 | thùng đạn nhiều + phấn | 'chalk tally marks', không chữ |
| SC_038 | tay cận cầm que | 1 tay, que dài, găng dầu che ngón |
| SC_040 | 3 drone + 2 người | drone nhỏ trên ca-pô, không HUD |
| SC_041 | xe chuyển động + tay trên xe | tracking chậm, 1 bàn tay |
| SC_042 | 3 người | lính ốm mặt cúi, 2 mặt ID |
| SC_043 | nhiều thương binh + mũi nỏ | hàng thương binh mờ, 2 mũi nỏ tĩnh cắm cột |
| SC_044 | bỏng cẳng tay cận | 'red and blistered', không vết hở |
| SC_045 | 13 lọ giống nhau | hàng lọ trắng trong túi, đếm ngón tay, không chữ nhãn |
| SC_046 | kim tiêm cận | 1 tay găng, kim đơn giản, chuyển động chậm |
| SC_049 | 4 người wide | áo choàng không mặt, 3 người xa |
| SC_053 | tay cận | 1 bàn tay tĩnh trên đá, 5 ngón rõ |
| SC_054 | chữ trên lụa | không đọc được, nắm tay vò |
| SC_055 | tháp + hàng trăm người + bò | aerial thấp, lưng cúi |
| SC_056 | nhiều tên lửa | 1 loạt, tháp nền, cung thủ máy sau lưng |
| SC_057 | cận chiến đám đông | medium-wide, mũ che mặt, không máu |
| SC_058 | giáo + khiên cận | 1 giáo, 1 khiên, lính Tùy mặt khuất |
| SC_059 | người rơi thang | xa, mờ trong hơi nước |
| SC_062 | nhiều chân dưới mái | chỉ chân, không mặt; tracking 1 chiều |
| SC_065 | chạy trên tường + lính ép lan can | tracking lùi, mặt phụ quay đi |
| SC_066 | ống PZF cận + 4 người | xạ thủ mặt khuất kính ngắm |
| SC_068 | nổ + mảnh | 1 vụ nổ, wide từ trên, không người cận |
| SC_069 | đám đông lùi | mũ che mặt, medium-wide |
| SC_070 | ngựa + kỵ sĩ | 1 ngựa, medium |
| SC_071 | tay cận | 1 bàn tay, 1 ngón giơ |
| SC_072 | đại quân rút | wide, mặt lính Goguryeo cúi |
| SC_074 | đám đông lao động đêm | đuốc + lưng, không mặt |
| SC_075 | chữ trên bảng | 'smudged and unreadable', số overlay |
| SC_078 | 6 người nội thất | wide, mỗi người 1 dấu hiệu, mặt 2 người ngồi/đứng chính rõ |
| SC_086 | tay trên vũ khí | tay trên tay quay, đạn 1 viên, không mặt |
| SC_087 | nổ xa | 2 cột đất nhỏ ở hậu cảnh |
| SC_090 | lặp động tác | nhịp đơn giản, 2 ống, tay không cận |
| SC_091 | nổ + người nhảy | medium-long, người nhỏ, không gore |
| SC_092 | 2 tháp cháy + đám đông | pan 1 chiều, cuối = 1 mặt |
| SC_093 | tay đếm ngón cận | 1 bàn tay, gập chậm |
| SC_098 | hàng nghìn người kéo | đuốc + lưng, wide |
| SC_099 | đám đông lao động | tracking, lưng |
| SC_102 | chân dung lịch sử | theo lock hư cấu |
| SC_104 | 3 người + khăn | khăn olive rõ, không chữ sổ |
| SC_105 | chữ trên đất | 'a simple smith's mark, not a character' |
| SC_106 | 6 người + bản đồ | wide, bản đồ 'painted rivers and a square fortress, no characters' |
| SC_114 | đám đông + lửa + trẻ em | tracking, mặt dân quay đi, 1 nguồn lửa |
| SC_118 | trúng tên | không cận, gập người, không máu |
| SC_119 | tay cận trên bản đồ | 1 tay, bản đồ không chữ |
| SC_120 | chữ trên thẻ tre | thẻ trơn |
| SC_121 | xác bò + người gục | không gore, mặt cúi |
| SC_127 | chữ trên bản đồ | 'no writing' |
| SC_128 | 3 người | thông ngôn mặt nghiêng cúi, 2 mặt |
| SC_131 | đêm không trăng + 4 người | silhouette, 1 mặt chính khi liếc |
| SC_132 | POV đêm + xe xa | hình khối tối, 1 đốm đỏ, 2 ngón tay |
| SC_133 | dao cận | lưỡi dao không chạm ai, 1 tay chặn cổ tay |
| SC_135 | 3 người nội thất | 2 người quỳ mặt cúi/nghiêng, hoàng đế rõ |
| SC_138 | chân dung lịch sử | lock hư cấu |
| SC_139 | 2 beat + POV xanh | POV ngắn không HUD, 2 địa điểm gần nhau |
| SC_140 | hàng người đêm | cằm sáng đỏ, mặt tối, 1 mặt chính |
| SC_141 | 10 cung thủ + 10 vệt lửa | wide từ trên, mặt tối |
| SC_142 | lửa + bắn súng | chớp đầu nòng xa, 1 nguồn lửa chính |
| SC_143 | nổ lớn | 1 cột lửa, wide thấp, người nằm rạp = hình khối |
| SC_144 | 2 người + phuy lăn + lửa | tracking 1 chiều, tay trên phuy không cận ngón |
| SC_145 | xe cháy + 3 người | 1 xe, 1 nguồn lửa, người = hình khối |
| SC_146 | nổ chuỗi | chớp qua nắp, wide, người nằm |
| SC_147 | giết cận | máy sau lưng, không lưỡi dao chạm, không máu, chớp lửa đầu nòng |
| SC_148 | tay bỏng cận | 'red and blistered', không da tróc |
| SC_149 | 2 người ngã + lửa | 1 chuyển động, lửa hậu cảnh |
| SC_154 | chữ trên bảng | 'smudged and unreadable'; số overlay |
| SC_155 | thương binh băng | băng trắng, mặt quay đi |
| SC_158 | cận chiến | medium-wide, không gore |
| SC_172 | chữ trên bảng | chalk marks không đọc được; số overlay |
| SC_179 | đám đông lao động | high angle, mặt cúi; 2 điểm mốc rõ (khe, vòm) |
| SC_182 | giàn + thợ đục | thợ mặt quay vào đá, tracking lùi |
| SC_187 | màn hình nhiệt | chấm trắng trên nền đen, không chữ/số |
| SC_188 | nổ đêm | 3 chớp nhỏ, người = silhouette |
| SC_195 | xe + vòm hẹp | máy tĩnh, 1 chuyển động xe, ref LOC_002_eastgate_chisel_ep2 |
| SC_198 | xe leo dốc | 1 chuyển động, máy tĩnh |
| SC_199 | đại quân | aerial cao, 1 chuyển động máy |
| SC_200 | hàng tướng quỳ | lưng/mũ, xa |
| SC_201 | 4 người + xe + cờ | low angle wide, mỗi người 1 dấu hiệu |
| SC_204 | ngựa phi + đám đông | tracking 1 con ngựa, lưng người đẩy |
| SC_210 | đám đông leo thang | low angle, mũ che mặt |
| SC_212 | cận chiến | 1 mặt ID, còn lại mũ/khiên, không máu |
| SC_215 | tay mở 10 ngón | 2 bàn tay rõ, tĩnh |
| SC_217 | màn hình + số | không digit, panel sáng trơn; overlay 22 |
| SC_218 | chớp lửa đầu nòng | 1 chớp, wide |
| SC_219 | người bay | xa, bụi che, không gore |
| SC_220 | đại quân | aerial trung, khối người |
| SC_222 | insert màn hình | không digit; overlay |
| SC_226 | hàng nỏ thủ | sau khiên, mặt khuất |
| SC_228 | trúng nỏ | mũi nỏ cắm vai giáp, không máu; sparks trên thép |
| SC_229 | màn hình | không digit; overlay |
| SC_230 | lửa trong hầm + người chạy | 1 nguồn lửa, lưng người |
| SC_231 | tường sập + người rơi | wide xa, bụi che |
| SC_232 | đám đông xung phong | aerial thấp, mũ che |
| SC_233 | bắn súng cận | xạ thủ mặt khuất sau súng, chớp đầu nòng |
| SC_238 | 2 beat | nếu veo không cắt, glabs tạo 2 clip 4 s; màn hình không digit |
| SC_239 | hàng giáo | mặt lính khuất mũ, 1 mặt ID |
| SC_240 | 300 kỵ | aerial thấp, đầu đoàn rõ, sau bụi |
| SC_242 | xe + kỵ + đám đông | tracking 1 chiều, bụi che |
| SC_243 | cận chiến | không máu, 1 mặt ID |
| SC_248 | hàng tướng quỳ rạp | lưng, không mặt |
| SC_250 | xác chết | dưới vải gai, giáo dựng, không mặt |
| SC_253 | tay + súng | súng dựng, tay băng không khép, 1 chuyển động |
| SC_257 | 4 người nội thất | mỗi người 1 dấu hiệu; bản đồ 'no characters' |
| SC_259 | chữ trên thẻ tre | vạch đếm, không ký tự |
| SC_260 | đám đông | lưng cúi, đuốc |
| SC_262 | chân dung lịch sử | lock |
| SC_264 | chữ trên đất | chấm + vạch, không ký tự |
| SC_272 | 6 vật giống nhau | hàng thẳng, giẻ đánh dấu khác màu |
| SC_280 | tay cầm mũi tên | 1 tay, 1 mũi tên |
| SC_283 | 2 kỵ sĩ | 2 ngựa đứng yên, medium |
| SC_287 | chữ | không tạo ảnh; end card ở edit |

### Quy tắc né chung (áp dụng toàn tập — kế thừa 1화 + riêng 2화)
- **Đám đông cận**: mọi cảnh ≥6 người → wide/aerial hoặc máy sau lưng hàng người, mặt lính phụ quay đi/khuất mũ; chỉ nhân vật có ID mới thấy mặt rõ.
- **Chữ**: bảng gỗ phấn, bộ đếm 잔탄, màn hình nhiệt, thẻ lụa/thẻ tre, bản vẽ binh thư, end card → prompt 'chalk marks / blurred figures / no readable characters'; số thật = OVERLAY (edit) — bảng §7.
- **Tay cầm súng**: K2C1 luôn 'muzzle down / slung'; PZF: mặt xạ thủ khuất sau kính ngắm; bắn = wide hoặc chớp lửa đầu nòng, không cận ngón tay trên cò.
- **Tháp công thành + hàng trăm người đẩy**: aerial thấp/wide, người đẩy = 'backs bent, faces down'; tháp = ref VEH_201 (da) hoặc VEH_201_mud_ep2 (đất) đính đúng giai đoạn.
- **Lửa/nổ**: 1 nguồn lửa chính mỗi khung, máy tĩnh hoặc 1 chuyển động; nổ phuy (SC_143) = wide thấp, mọi người nằm rạp; 40mm nổ dây chuyền (SC_146) = chớp qua nắp nóc, không cận.
- **Thương tích/bỏng**: băng trắng, không vết thương hở cận; bỏng = 'red, blistered' trên tay/cẳng tay, không mặt.
- **Chân dung lịch sử (을지문덕/양제/우중문/우문술)**: theo lock hư cấu, không giống người thật; 을지문덕 SC_049–077 KHÔNG lộ mặt (mũ trùm, lưng, bàn tay).
- **K2 trên 치 / chui vòm cổng**: 1 chuyển động xe, máy tĩnh; khe đục/vòm = ref LOC_002_bastion_se_ep2 / LOC_002_eastgate_chisel_ep2 để giữ hình dạng đá.
- **Hangul trên xe**: KHÔNG vẽ (chỉ số Ả Rập 1/2/3/4 + 태극기 nhỏ); '천둥' chỉ ở thoại/radio.
