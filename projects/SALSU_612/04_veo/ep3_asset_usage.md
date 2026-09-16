# 3화 「남하」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)
> Đếm theo `04_veo/scenes_ep3.json` (287 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro. Lock = continuity_master.json v3.

## 1. Nhân vật (CHAR) — số SC xuất hiện
| CHAR | SC | Derived state trong 3화 (SC) |
|---|---|---|
| CHAR_001 | 65 | CHAR_001_helmet_ep3 (9), CHAR_001_rain_ep3 (53), CHAR_001_valley_ep3 (3) |
| CHAR_002 | 23 | CHAR_002_k3_rain_ep3 (2), CHAR_002_rain_ep3 (19), CHAR_002_soot_ep2 (2) |
| CHAR_003 | 35 | CHAR_003_rain_ep3 (32), CHAR_003_valley_ep3 (3) |
| CHAR_004 | 11 | CHAR_004_pass_ep3 (2), CHAR_004_rain_ep3 (9) |
| CHAR_005 | 37 | CHAR_005_captive_ep3 (2), CHAR_005_captive_patch_ep3 (4), CHAR_005_nvg_ep3 (7), CHAR_005_rain_ep3 (22), CHAR_005_stripped_ep3 (2) |
| CHAR_006 | 26 | CHAR_006_bare_hands_ep3 (3), CHAR_006_nvg_ep3 (13), CHAR_006_rain_ep3 (9), CHAR_006_valley_ep3 (1) |
| CHAR_101 | 26 | CHAR_101_false_surrender_ep3 (13), CHAR_101_hall_seated_ep4 (9), CHAR_101_rain_armor_ep3 (4) |
| CHAR_105 | 49 | CHAR_105_plain_robe_ep3 (10), CHAR_105_radio_ep3 (12), CHAR_105_radio_helmet_off_ep3 (1), CHAR_105_radio_wet_ep3 (3), CHAR_105_rain_ep3 (23) |
| CHAR_106 | 17 | CHAR_106_forge_ep2 (3), CHAR_106_rain_south_ep3 (13), CHAR_106_valley_ep3 (1) |
| CHAR_107 | 18 | CHAR_107_rain_ep3 (11), CHAR_107_scarf_burnt_ep3 (6), CHAR_107_scarf_ep2 (1) |
| CHAR_201 | 1 | CHAR_201_robe_only_ep3 (1) |
| CHAR_202 | 13 | CHAR_202_camp_chair_ep3 (5), CHAR_202_horse_rain_ep3 (1), CHAR_202_road_tent_ep3 (3), CHAR_202_tent_ep4 (3) |
| CHAR_203 | 7 | CHAR_203_rain_ep3 (7) |
| CHAR_205 | 23 | CHAR_205_nvg_down_ep3 (2), CHAR_205_nvg_ep3 (4), CHAR_205_nvg_hand_ep3 (1), CHAR_205_rain_ep3 (16) |

### Trạng thái do veo-prompt-engineer đặt cho 3화 (chưa có trong continuity_master → đề xuất character-designer nhập bible)
- `CHAR_001_valley_ep3` (CHAR_001, đính `CHAR_001_dusty_ep2`, 3 SC): Fine yellow-grey stone dust and black soot on helmet, shoulders and cheeks, sweat streaks at the temples, sleeves rolled to the elbow, small field bandage on the back of the left hand, one-day stubble, black pistol in a thigh holster on the right leg. The shaft of a Goguryeo arrow protruding from the left chest pocket.
- `CHAR_001_helmet_ep3` (CHAR_001, đính `CHAR_001_rain_ep3`, 9 SC): Rain-soaked uniform darkened with water, mud caked to the knees, four-day stubble, hollow cheeks, helmet on with wet cover, black pistol in a thigh holster on the right leg, the shaft of a Goguryeo arrow protruding from the left chest pocket. A second empty combat helmet with a bare night-vision mount held in the left hand.
- `CHAR_002_rain_ep3` (CHAR_002, đính `CHAR_002_ref`, 19 SC): Helmet on with wet cover, rain-soaked uniform, mud to the knees, four-day stubble, right sleeve scorched at the cuff, goggles on the helmet fogged with water.
- `CHAR_003_valley_ep3` (CHAR_003, đính `CHAR_003_hands_bandaged_ep2`, 3 SC): Both hands wrapped in dirty white field bandages, no gloves, left eyebrow half singed, soot-streaked tired face, patrol cap, red rag in belt.
- `CHAR_003_valley_plate_ep3` (CHAR_003, đính `CHAR_003_hands_bandaged_ep2`, 0 SC): Both hands wrapped in dirty white field bandages, no gloves, left eyebrow half singed, soot-streaked tired face, patrol cap, red rag in belt, a small olive-drab steel vehicle nameplate with a white numeral 3 tied to his backpack strap.
- `CHAR_004_rain_ep3` (CHAR_004, đính `CHAR_004_ref`, 9 SC): Helmet on with wet cover, rain-soaked uniform, mud to the knees, hair bun tight, blue nitrile gloves, a small brown hemp herb pouch tied at the belt, medic bag on the shoulder.
- `CHAR_004_pass_ep3` (CHAR_004, đính `CHAR_004_ref`, 2 SC): Helmet on with wet cover, rain-soaked uniform, mud to the knees, dried blood on both forearms to the elbows and on the nitrile gloves, a small brown hemp herb pouch tied at the belt, medic bag on the shoulder, pale tired face.
- `CHAR_005_rain_ep3` (CHAR_005, đính `CHAR_005_ref`, 22 SC): Helmet on with wet cover, rain-soaked uniform, mud to the knees, faint stubble, the drone controller on the chest harness under a clear rain cover, hard olive drone case on the back.
- `CHAR_005_valley_ep3` (CHAR_005, đính `CHAR_005_ref`, 0 SC): Ash and soot on face and uniform, one corner of the hard drone case on his back scorched black, red-rimmed eyes.
- `CHAR_005_nvg_ep3` (CHAR_005, đính `CHAR_005_ref`, 7 SC): Helmet on with wet cover and a night-vision monocular flipped up on the helmet mount, rain-soaked uniform, mud to the knees, faint stubble, the drone controller on the chest harness, hard olive drone case on the back, a rope tied around the waist.
- `CHAR_005_stripped_ep3` (CHAR_005, đính `CHAR_005_captive_ep3`, 2 SC): No helmet, no body armor, no boots, torn dirty camo uniform and socks, the small Korean flag patch still on the right shoulder, hands bound behind the back with hemp rope, mud on face, frightened.
- `CHAR_005_captive_patch_ep3` (CHAR_005, đính `CHAR_005_captive_ep3`, 4 SC): Prisoner: no helmet, no body armor, no boots, torn dirty camo uniform and socks, the small Korean flag patch still sewn on the right shoulder, hands bound behind the back with hemp rope, split lip, bruised swollen left eye, hair hacked short unevenly, mud on face, frightened but defiant.
- `CHAR_006_valley_ep3` (CHAR_006, đính `CHAR_006_ref`, 1 SC): Grey stone dust and soot on the boonie hat and shoulders, a night-vision monocular flipped up on a cord over the hat brim, two-day stubble, no face paint.
- `CHAR_006_rain_ep3` (CHAR_006, đính `CHAR_006_ref`, 9 SC): Boonie hat soaked with the brim drooping, rain-soaked uniform, wet mud over chest, knees and forearms, five-day stubble, no face paint.
- `CHAR_006_nvg_ep3` (CHAR_006, đính `CHAR_006_ref`, 13 SC): Boonie hat soaked with the brim drooping, a night-vision monocular strapped to the front of the hat with cord over the right eye, rain-soaked uniform, wet mud over chest, knees and forearms, five-day stubble, no face paint.
- `CHAR_006_bare_hands_ep3` (CHAR_006, đính `CHAR_006_ref`, 3 SC): Boonie hat soaked, no night-vision device, rain-soaked uniform, wet mud over chest and knees, bare hands scraped and bleeding at the knuckles, five-day stubble, no face paint.
- `CHAR_101_rain_armor_ep3` (CHAR_101, đính `CHAR_101_ref`, 4 SC): Armor, plume and feathers darkened with rain, water beading on the lamellar plates and running down the short silver beard, mud on boots.
- `CHAR_105_rain_ep3` (CHAR_105, đính `CHAR_105_ref`, 23 SC): Rain-soaked armor and jacket, wet feather, mud on boots and skirt, no radio.
- `CHAR_105_radio_helmet_off_ep3` (CHAR_105, đính `CHAR_105_radio_ep3`, 1 SC): A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Iron helmet held under the left arm, black topknot bare, head bowed.
- `CHAR_105_radio_wet_ep3` (CHAR_105, đính `CHAR_105_radio_ep3`, 3 SC): A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Soaked to the skin after two nights of riding, water streaming from the armor, a bamboo tally tied with red cord in one hand.
- `CHAR_106_valley_ep3` (CHAR_106, đính `CHAR_106_rain_south_ep3`, 1 SC): Coarse hemp cloak over the jacket, walking staff, tool roll on the back, mud on sandals, soot smudges from the burning vehicles on the cloak.
- `CHAR_107_rain_ep3` (CHAR_107, đính `CHAR_107_scarf_ep2`, 11 SC): A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. Rain-damp braids stuck to the cheeks, mud on the hem of the skirt, a coarse hemp cloak over the shoulders.
- `CHAR_202_camp_chair_ep3` (CHAR_202, đính `CHAR_202_ref`, 5 SC): Seated on a folding wooden camp chair, helmet on, the red silk cloak damp at the hem, wet planks underfoot.
- `CHAR_202_horse_rain_ep3` (CHAR_202, đính `CHAR_202_ref`, 1 SC): Mounted on a tall war horse with a red silk caparison, the red cloak soaked dark and heavy with rain, straight sword drawn.
- `CHAR_202_road_tent_ep3` (CHAR_202, đính `CHAR_202_ref`, 3 SC): Helmet off showing the white topknot, red silk cloak soaked dark with rain, beard wet, mud on the boots.
- `CHAR_203_rain_ep3` (CHAR_203, đính `CHAR_203_ref`, 7 SC): Plain dark armor beaded with rain, a bundle of bamboo writing slips in one hand, grey tired face.
- `CHAR_205_rain_ep3` (CHAR_205, đính `CHAR_205_ref`, 16 SC): An empty black rifle magazine hanging from a cord on the bronze plaque belt, rain-darkened leather armor, wet fox fur on the cap, mud on boots.
- `CHAR_205_nvg_hand_ep3` (CHAR_205, đính `CHAR_205_ref`, 1 SC): An empty black rifle magazine hanging from a cord on the bronze plaque belt, rain-darkened leather armor, mud on boots, a small black night-vision monocular held in both hands.
- `CHAR_205_nvg_down_ep3` (CHAR_205, đính `CHAR_205_nvg_ep3`, 2 SC): A modern night-vision monocular device strapped with a leather strap over the front of the fox-fur cap, an empty black rifle magazine hanging from the belt, rain-darkened leather armor, mud on boots. The monocular swung down over the right eye with a faint green glow at the eyepiece.

### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)
| Extra | SC | ref đính |
|---|---|---|
| RADIO_HANDHELD | 20 | — |
| ROK_SOLDIERS | 20 | — |
| GOG_CAVALRYMEN | 20 | VEH_101_ref |
| XIANBEI_DEPUTY | 10 | EXTRA_xianbei_deputy_ref |
| GOG_CAVALRYMEN_WALKING | 9 | VEH_101_ref |
| XIANBEI_RIDERS_EARS | 8 | VEH_206_ref |
| XIANBEI_TORCHBEARERS | 8 | VEH_206_ref |
| SUI_SCOUTS_HORSE | 7 | VEH_207_ref |
| SUI_CAVALRY_ENVOY | 5 | VEH_207_ref |
| XIANBEI_WARRIORS_FOOT | 5 | VEH_206_ref |
| K3_GUNNER | 5 | WPN_003_ref |
| SUI_MARCHERS | 4 | WPN_201_ref |
| OX_TEAMS | 4 | VEH_002_captured |
| SUI_GUARDS | 3 | WPN_201_ref |
| SUI_VANGUARD_WET | 3 | WPN_201_ref |
| SUI_CROWD_CHARGING | 3 | WPN_201_ref |
| XIANBEI_RIDERS | 3 | VEH_206_ref |
| BOY_SCOUT_RIDING | 3 | EXTRA_boy_scout_ref |
| XIANBEI_CLIMBERS | 3 | VEH_206_ref |
| PZF_GUNNER | 2 | WPN_005_ref |
| ROK_SOLDIER | 2 | — |
| SUI_DIGGERS | 2 | WPN_201_ref |
| SUI_DESERTER | 2 | — |
| ROK_SOLDIERS_MOUNTED | 2 | — |
| SUI_SOLDIERS_STARVING | 2 | WPN_201_ref |
| MORTAR_GUNNER | 2 | WPN_002_ref |
| MORTAR_CREW | 2 | WPN_002_ref |
| SUI_VANGUARD_GENERAL | 2 | EXTRA_sui_vanguard_general_ref |
| SUI_SCOUTS_FOOT | 2 | — |
| GOG_ARCHERS_TWO | 2 | WPN_101_ref |
| SUI_COURIER | 2 | — |
| K2_DRIVER | 2 | — |
| GOG_VILLAGERS | 2 | — |
| XIANBEI_ARCHERS_PRONE | 2 | VEH_206_ref |
| SUI_RAIDERS | 2 | VEH_207_ref |
| ROK_RIFLEMEN_TWO | 2 | — |
| K3_GUNNERS | 2 | WPN_003_ref |
| SUI_SOLDIER_YOUNG | 1 | — |
| SUI_OFFICER_HORSE | 1 | VEH_207_ref |
| ROK_BURNED_HANDS_TWO | 1 | — |
| SUI_OFFICER_LANTERN | 1 | — |
| GOG_COURIER | 1 | — |
| SUI_DIGGERS_BANK | 1 | WPN_201_ref |
| BOY_SCOUT | 1 | EXTRA_boy_scout_ref |
| SUI_GUARD_STARVING | 1 | — |
| SUI_EUNUCH | 1 | — |
| SUI_ENVOY | 1 | — |
| GOG_ESCORT_FOUR | 1 | — |
| GOG_GATE_GUARD | 1 | — |
| GOG_RIDER_WOUNDED | 1 | — |
| SUI_ARCHERS_LEDGE | 1 | — |
| ROK_SOLDIER_ASLEEP | 1 | — |
| GOG_SCOUTS_THREE | 1 | — |
| ROK_RADIOMAN | 1 | — |
| ROK_WOUNDED | 1 | — |
| ROK_WOUNDED_TWO | 1 | — |
| K3_GUNNER_DEAD | 1 | WPN_003_ref |
| GOG_CAVALRYMEN_GRAVE | 1 | VEH_101_ref |
| XIANBEI_CAMP_MEN | 1 | VEH_206_ref |
| GOG_INTERPRETER_CAPTIVE | 1 | — |
| XIANBEI_MESSENGER | 1 | VEH_206_ref |

## 2. Địa điểm (LOC) — số SC
| LOC | SC | Sub-lock (SC) |
|---|---|---|
| LOC_001 | 7 | LOC_001_plain_camp_night (2), LOC_001_plain_camp_tent_edge (1), LOC_001_plain_night_aerial (2), LOC_001_plain_road (2) |
| LOC_003 | 26 | LOC_003_ravine (1), LOC_003_ravine_hearth (3), LOC_003_ravine_k2rear (5), LOC_003_ravine_mouth (4), LOC_003_ravine_poncho (1), LOC_003_ravine_stream_nvg (1), LOC_003_ravine_tent (1), LOC_003_valley_fire (1), LOC_003_valley_k21 (6), LOC_003_valley_k21_rain (1), LOC_003_valley_mouth (1), LOC_003_valley_westledge (1) |
| LOC_004 | 1 | LOC_004_pavilion_int (1) |
| LOC_005 | 64 | LOC_005 (3), LOC_005_aerial_south (2), LOC_005_camp_edge_pits (1), LOC_005_camp_lane (3), LOC_005_ford (2), LOC_005_mortar_pit (2), LOC_005_north_fire (3), LOC_005_north_horses (1), LOC_005_north_horses_dawn (1), LOC_005_north_road (5), LOC_005_north_road_night (2), LOC_005_shoal_north (3), LOC_005_shoal_south (6), LOC_005_south_forest (6), LOC_005_south_forest_edge (1), LOC_005_south_hill (9), LOC_005_south_ledge_k3 (1), LOC_005_sui_road_tent (3), LOC_005_sui_tent (7), LOC_005_sui_tent_2 (3) |
| LOC_007 | 15 | LOC_007 (2), LOC_007_aerial_reeds (1), LOC_007_north_sand (7), LOC_007_reeds_arrival (1), LOC_007_water_edge (4) |
| LOC_008 | 80 | LOC_008_aerial_split (1), LOC_008_fort_aerial (1), LOC_008_fort_gate (1), LOC_008_fort_granary_shed (3), LOC_008_fort_tent (11), LOC_008_fort_tent_ext (1), LOC_008_fort_trail (2), LOC_008_fort_wall (2), LOC_008_fort_yard (2), LOC_008_hill_fort (1), LOC_008_hill_gap (2), LOC_008_mountain_road (5), LOC_008_ridge_day (2), LOC_008_ridge_night (6), LOC_008_road_bend_amnok (1), LOC_008_road_pine (1), LOC_008_village_edge (1), LOC_008_village_forge (6), LOC_008_village_forge_day (1), LOC_008_village_fort_wall (1), LOC_008_village_gate (1), LOC_008_village_granary_floor (1), LOC_008_village_house_int (1), LOC_008_village_k2 (8), LOC_008_village_k2_side (1), LOC_008_village_night_wide (1), LOC_008_village_porch (2), LOC_008_village_sandtable (9), LOC_008_village_street (1), LOC_008_village_terraces (2), LOC_008_village_terraces_up (1), LOC_008_village_upward (1) |
| LOC_009 | 94 | LOC_009_barrier_gap (9), LOC_009_barrier_line (6), LOC_009_cliff_top_above_outcrop (1), LOC_009_cliff_top_far (1), LOC_009_east_foot (6), LOC_009_east_road (10), LOC_009_far_ridge (2), LOC_009_goat_path (2), LOC_009_goat_path_fog (2), LOC_009_goat_path_foot (1), LOC_009_goat_path_upper (3), LOC_009_grave (1), LOC_009_north_ledge (1), LOC_009_nw_cliff_torches (2), LOC_009_outcrop_path (3), LOC_009_outcrop_top (8), LOC_009_outcrop_top_dawn (2), LOC_009_rockslide (1), LOC_009_saddle_dawn (4), LOC_009_saddle_dusk (2), LOC_009_saddle_night (6), LOC_009_south_descent (3), LOC_009_south_flat (2), LOC_009_south_foot (2), LOC_009_south_gate (4), LOC_009_trail_night (1), LOC_009_xianbei_camp_night (4), LOC_009_xianbei_camp_pine (4), LOC_009_xianbei_forest (1) |

## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/UAV/EQP) — số SC
| ID | SC |
|---|---|
| VEH_001 | 52 |
| VEH_101 | 30 |
| VEH_206 | 22 |
| VEH_002 | 14 |
| VEH_207 | 14 |
| WPN_003 | 11 |
| UAV_001 | 8 |
| EQP_001 | 8 |
| WPN_001 | 5 |
| WPN_201 | 5 |
| WPN_101 | 4 |
| WPN_004 | 3 |
| WPN_002 | 3 |
| VEH_003 | 2 |
| WPN_005 | 2 |
| EQP_002 | 2 |

### Trạng thái xe 3화 (build.py VEH_STATE — theo vehicle_bible damage state 3화)
- `K2_VALLEY`: Camouflage netting removed, cut pine branches lashed over the turret roof, a green 20-liter jerrycan and one dark olive 200-liter fuel drum roped to the rear of the turret, black soot around the muzzle, an extra black whip antenna, fresh mud on the tracks.
- `K2_DRUM`: Wet mud sprayed over the lower half of the hull, cut pine branches lashed over the turret roof, a green jerrycan and one dark olive 200-liter fuel drum roped to the rear of the turret, black soot around the muzzle, an extra black whip antenna, one skirt plate missing on the left side.
- `K2_MULE`: Wet mud over the lower half of the hull, cut pine branches over the turret roof, two heavy machine guns, mortar tubes and olive ammunition cans lashed under a net on the engine deck, a green jerrycan and a dark olive 200-liter drum roped to the turret rear, black soot around the muzzle, an extra black whip antenna, one skirt plate missing on the left side.
- `K2_MULE_STEAM`: Wet mud over the lower half of the hull, cut pine branches over the turret roof, machine guns, mortar tubes and ammunition cans lashed under a net on the engine deck, a green jerrycan and a dark olive drum roped to the turret rear, black soot around the muzzle, one skirt plate missing on the left side, white steam venting from the rear engine grille.
- `K2_MULE_SCORCH`: Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black where a fire arrow struck, machine guns, mortar tubes and ammunition cans lashed under a net on the engine deck, no fuel drum, black soot around the muzzle, an extra black whip antenna, one skirt plate missing on the left side.
- `K2_MULE_PATCH`: Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black, the rear engine grille propped open showing a bright red copper sleeve lashed with black pitch-soaked leather cord over a coolant hose, machine guns and ammunition cans lashed on the engine deck, no fuel drum, one skirt plate missing on the left side.
- `K2_PASS`: Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black, machine guns, mortar tubes and ammunition cans lashed under a net on the engine deck, no fuel drum, a bundle of charging cables running from a socket at the rear of the hull, black soot around the muzzle, one skirt plate missing on the left side, engine silent.
- `K2_AFTER`: Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black, fresh black soot around the muzzle, several broken arrows stuck in the stowage net over the engine deck, machine guns and ammunition cans lashed on the engine deck, no fuel drum, one skirt plate missing on the left side.
- `K21_3_INTACT`: White numeral 3 on the turret side beside a small Korean flag, camouflage net removed, rear troop ramp lowered and open, a crude hand-forged iron pin with hammer marks through the third road wheel on the right side, wet armor reflecting orange firelight.
- `K21_3_HOLES`: White numeral 3 on the turret side beside a small Korean flag, camouflage net removed, rear troop ramp lowered and open, a crude hand-forged iron pin through the third road wheel on the right side, two small empty bolt holes on the hull side where a nameplate was removed, wet armor reflecting orange firelight.
- `K21_2_DRAINED`: White numeral 2 on the turret, rear troop ramp open, camouflage net removed, black soot around the short muzzle, fuel drained, standing dark and empty forty meters away.
- `K21_2_BURNING`: White numeral 2 on the turret, hull torn open at the side, engulfed in tall orange flame with sparks and intermittent detonations flashing inside the open troop compartment.
- `K21_3_CAPTURED`: Mud-streaked hull, rear troop ramp open, a red and yellow Sui silk banner with black tassels tied to the turret, thick hemp tow ropes lashed around the hull front leading forward to two files of oxen, two small empty bolt holes on the hull side where a nameplate was removed, a small white arrow mark painted on the ramp, no fuel cans, no camouflage net.
- `K21_3_PARKED`: Mud-streaked hull, rear troop ramp open, a red and yellow Sui silk banner with black tassels tied to the turret, slack hemp tow ropes lying in the mud in front of the hull, two small empty bolt holes on the hull side, no camouflage net, wet armor reflecting torchlight.
- `K21_INTERIOR`: Inside the troop compartment: nine folding seats along the walls, an unlit red dome lamp, an empty metal rack with loose straps where a hard case was mounted, a rack of 40mm rounds under the turret basket, torchlight falling through the open roof hatch.
- `TRUCKS_BURNING`: Two six-wheeled military cargo trucks and a boxy 4x4 command vehicle engulfed in tall orange flame, canvas covers burned away, black smoke rising.
- `XIANBEI_EARS`: The horses' ears stuffed with rolled felt and tied with cord across the cheeks.
- `DRONE_WRECK`: The drone with one arm snapped, two propellers broken, the gimbal camera cracked, dried mud on the body.

## 4. Đạo cụ (PROP) — số SC
| PROP | SC |
|---|---|
| PROP_021 | 15 |
| PROP_006 | 9 |
| PROP_005 | 9 |
| PROP_012 | 7 |
| PROP_016 | 6 |
| PROP_009 | 5 |
| PROP_018 | 5 |
| PROP_022 | 4 |
| PROP_007 | 3 |
| PROP_023 | 3 |
| PROP_025 | 3 |
| PROP_002 | 2 |
| PROP_019 | 2 |
| PROP_015 | 2 |
| PROP_011 | 2 |
| PROP_020 | 2 |
| PROP_010 | 1 |
| PROP_001 | 1 |
| PROP_017 | 1 |

## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)
| # | ref id | thư mục | số SC đính | trạng thái |
|---|---|---|---|---|
| 1 | CHAR_001_rain_ep3 | characters | 62 | có job (bible) |
| 2 | VEH_001_mule_ep3 | vehicles | 45 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 3 | VEH_101_ref | vehicles | 34 | có job (bible) |
| 4 | VEH_206_ref | vehicles | 33 | có job (bible) |
| 5 | CHAR_003_rain_ep3 | characters | 32 | có job (bible) |
| 6 | LOC_009_wide | locations | 31 | có job (bible) |
| 7 | LOC_008_wide | locations | 31 | có job (bible) |
| 8 | CHAR_005_ref | characters | 29 | có job (bible) |
| 9 | LOC_005_wide | locations | 28 | có job (bible) |
| 10 | CHAR_006_ref | characters | 26 | có job (bible) |
| 11 | LOC_008_hill_fort_ep3 | locations | 24 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 12 | CHAR_105_ref | characters | 23 | có job (bible) |
| 13 | LOC_009_saddle_night_ep3 | locations | 22 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 14 | CHAR_002_ref | characters | 19 | có job (bible) |
| 15 | LOC_005_south_hill_ep3 | locations | 19 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 16 | CHAR_107_scarf_ep2 | characters | 18 | có job (bible) |
| 17 | LOC_008_mountain_road_ep3 | locations | 18 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 18 | WPN_201_ref | vehicles | 18 | có job (bible) |
| 19 | VEH_207_ref | vehicles | 17 | có job (bible) |
| 20 | CHAR_205_ref | characters | 17 | có job (bible) |
| 21 | LOC_003_mobile | locations | 16 | có job (bible) |
| 22 | CHAR_105_radio_ep3 | characters | 16 | có job (bible) |
| 23 | PROP_021_ref | props | 15 | có job (bible) |
| 24 | CHAR_106_rain_south_ep3 | characters | 14 | có job (bible) |
| 25 | LOC_009_outcrop_ep3 | locations | 14 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 26 | CHAR_101_false_surrender_ep3 | characters | 13 | có job (bible) |
| 27 | LOC_005_sui_tent_ep3 | locations | 13 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 28 | LOC_007_wide | locations | 13 | có job (bible) |
| 29 | CHAR_004_ref | characters | 11 | có job (bible) |
| 30 | WPN_003_ref | vehicles | 11 | có job (bible) |
| 31 | LOC_003_valley_fire_ep3 | locations | 10 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 32 | CHAR_105_plain_robe_ep3 | characters | 10 | có job (bible) |
| 33 | CHAR_202_ref | characters | 10 | có job (bible) |
| 34 | EXTRA_xianbei_deputy_ref | characters | 10 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 35 | LOC_009_xianbei_camp_ep3 | locations | 10 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 36 | PROP_006_ref | props | 9 | có job (bible) |
| 37 | CHAR_101_hall_seated_ep4 | characters | 9 | có job (bible) |
| 38 | LOC_009_detail | locations | 9 | có job (bible) |
| 39 | UAV_001_ref | vehicles | 8 | có job (bible) |
| 40 | EQP_001_ref | vehicles | 8 | có job (bible) |
| 41 | LOC_009_aftermath | locations | 8 | có job (bible) |
| 42 | CHAR_005_captive_ep3 | characters | 8 | có job (bible) |
| 43 | VEH_002_ref | vehicles | 7 | có job (bible) |
| 44 | LOC_001_plain_rain_ep3 | locations | 7 | **CHƯA CÓ — job trong ref_jobs_ep3_extra.json** |
| 45 | VEH_001_ref | vehicles | 7 | có job (bible) |
| 46 | CHAR_203_ref | characters | 7 | có job (bible) |
| 47 | PROP_012_ref | props | 7 | có job (bible) |
| 48 | VEH_002_captured | vehicles | 7 | có job (bible) |
| 49 | LOC_008_detail | locations | 7 | có job (bible) |
| 50 | CHAR_205_nvg_ep3 | characters | 6 | có job (bible) |
| 51 | PROP_009_ref | props | 5 | có job (bible) |
| 52 | WPN_101_ref | vehicles | 5 | có job (bible) |
| 53 | WPN_001_ref | vehicles | 5 | có job (bible) |
| 54 | PROP_022_ref | props | 4 | có job (bible) |
| 55 | LOC_005_detail | locations | 4 | có job (bible) |
| 56 | EXTRA_boy_scout_ref | characters | 4 | có job (ep1 extra) |
| 57 | CHAR_101_ref | characters | 4 | có job (bible) |
| 58 | CHAR_003_hands_bandaged_ep2 | characters | 3 | có job (bible) |
| 59 | PROP_007_ref | props | 3 | có job (bible) |
| 60 | CHAR_001_dusty_ep2 | characters | 3 | có job (bible) |
| 61 | PROP_025_ref | props | 3 | có job (bible) |
| 62 | WPN_004_ref | vehicles | 3 | có job (bible) |
| 63 | WPN_002_ref | vehicles | 3 | có job (bible) |
| 64 | CHAR_202_tent_ep4 | characters | 3 | có job (bible) |
| 65 | CHAR_106_forge_ep2 | characters | 3 | có job (bible) |
| 66 | VEH_003_ref | vehicles | 2 | có job (bible) |
| 67 | CHAR_002_soot_ep2 | characters | 2 | có job (bible) |
| 68 | WPN_005_ref | vehicles | 2 | có job (bible) |
| 69 | PROP_002_ref | props | 2 | có job (bible) |
| 70 | EQP_002_ref | vehicles | 2 | có job (bible) |
| 71 | EXTRA_sui_vanguard_general_ref | characters | 2 | có job (ep1 extra) |
| 72 | PROP_019_ref | props | 2 | có job (bible) |
| 73 | PROP_015_ref | props | 2 | có job (bible) |
| 74 | PROP_011_ref | props | 2 | có job (bible) |
| 75 | CHAR_002_k3_rain_ep3 | characters | 2 | có job (bible) |
| 76 | PROP_010_ref | props | 1 | có job (bible) |
| 77 | PROP_001_ref | props | 1 | có job (bible) |
| 78 | PROP_017_ref | props | 1 | có job (bible) |
| 79 | CHAR_201_robe_only_ep3 | characters | 1 | có job (bible) |
| 80 | LOC_004_detail | locations | 1 | có job (bible) |
| 81 | LOC_007_detail | locations | 1 | có job (bible) |

### Ref CHƯA CÓ (11) — `05_references/extra/ref_jobs_ep3_extra.json` (glabs-operator tạo trước lô ảnh cảnh; world-designer/character-designer duyệt)
- `LOC_003_valley_fire_ep3` (locations): thung lũng sau 요동성 đêm D1, xe cháy, cỏ xanh tháng 6 — sub-lock `LOC_003_valley_fire`.
- `LOC_001_plain_rain_ep3` (locations): đồng bằng đông 요동성 tháng 6 — đường lầy, cỏ xanh, mưa — sub-lock `LOC_001_plain_road` (LOC_001 lock gốc là cỏ vàng đầu xuân → KHÔNG dùng cho 3화).
- `LOC_008_mountain_road_ep3` (locations): đường núi bùn đỏ, thông + sồi non, mưa phùn — sub-lock `LOC_008_mountain_road` (P2/P3, montage D4–D8).
- `LOC_008_hill_fort_ep3` (locations): sơn thành nhỏ đêm mưa, cổng gỗ + đuốc, kho thóc nâng sàn, lều 삼족오 — sub-lock `LOC_008_hill_fort` (P6, 24 SC).
- `LOC_005_south_hill_ep3` (locations): mỏm đá dưới tán thông bờ nam nhìn xuống bãi cuội + trại Tùy — sub-lock `LOC_005_south_hill` (P4/P5).
- `LOC_005_sui_tent_ep3` (locations): lều 우중문 sàn ván ướt, ghế gấp, bàn bút lụa — sub-lock `LOC_005_sui_tent` (P4/P5/P11, 12 SC).
- `LOC_009_saddle_night_ep3` (locations): yên đèo đêm, ải đá hở 5 m, đèn sạc đỏ — sub-lock `LOC_009_saddle_night` (P10 wide; cận dùng bible `LOC_009_detail`).
- `LOC_009_outcrop_ep3` (locations): đỉnh mỏm đá 10×10 m cao 200 m — sub-lock `LOC_009_outcrop_top` (P10 태오, 10 SC).
- `LOC_009_xianbei_camp_ep3` (locations): trại Tiên Ti cao nguyên đêm D15, lửa dưới thông, ngựa bịt tai — sub-lock `LOC_009_xianbei_camp_night` (P11).
- `VEH_001_mule_ep3` (vehicles, 16:9): K2 'con la' — K6 + ống cối + hộp đạn buộc đuôi, cành thông nóc, bùn nửa thân, mất 1 tấm váy xích trái — dùng cho ~70 SC K2 từ D4 (state `K2_MULE*`).
- `EXTRA_xianbei_deputy_ref` (characters, 3:4): 선비 부장 (phó của 탁발흠) — 9 SC ENEMY POV; cần ref riêng để không trộn với 탁발흠 (không sẹo, có ria, ~30).

### Thứ tự chạy ref đề xuất (P1 → P3)
- **P1 (≥15 SC):** CHAR_001_rain_ep3, VEH_001_mule_ep3, VEH_101_ref, VEH_206_ref, CHAR_003_rain_ep3, LOC_009_wide, LOC_008_wide, CHAR_005_ref, LOC_005_wide, CHAR_006_ref, LOC_008_hill_fort_ep3, CHAR_105_ref, LOC_009_saddle_night_ep3, CHAR_002_ref, LOC_005_south_hill_ep3, CHAR_107_scarf_ep2, LOC_008_mountain_road_ep3, WPN_201_ref, VEH_207_ref, CHAR_205_ref, LOC_003_mobile, CHAR_105_radio_ep3, PROP_021_ref
- **P2 (5–14 SC):** CHAR_106_rain_south_ep3, LOC_009_outcrop_ep3, CHAR_101_false_surrender_ep3, LOC_005_sui_tent_ep3, LOC_007_wide, CHAR_004_ref, WPN_003_ref, LOC_003_valley_fire_ep3, CHAR_105_plain_robe_ep3, CHAR_202_ref, EXTRA_xianbei_deputy_ref, LOC_009_xianbei_camp_ep3, PROP_006_ref, CHAR_101_hall_seated_ep4, LOC_009_detail, UAV_001_ref, EQP_001_ref, LOC_009_aftermath, CHAR_005_captive_ep3, VEH_002_ref, LOC_001_plain_rain_ep3, VEH_001_ref, CHAR_203_ref, PROP_012_ref, VEH_002_captured, LOC_008_detail, CHAR_205_nvg_ep3, PROP_009_ref, WPN_101_ref, WPN_001_ref
- **P3 (<5 SC):** PROP_022_ref, LOC_005_detail, EXTRA_boy_scout_ref, CHAR_101_ref, CHAR_003_hands_bandaged_ep2, PROP_007_ref, CHAR_001_dusty_ep2, PROP_025_ref, WPN_004_ref, WPN_002_ref, CHAR_202_tent_ep4, CHAR_106_forge_ep2, VEH_003_ref, CHAR_002_soot_ep2, WPN_005_ref, PROP_002_ref, EQP_002_ref, EXTRA_sui_vanguard_general_ref, PROP_019_ref, PROP_015_ref, PROP_011_ref, CHAR_002_k3_rain_ep3, PROP_010_ref, PROP_001_ref, PROP_017_ref, CHAR_201_robe_only_ep3, LOC_004_detail, LOC_007_detail

## 6. SC cần ảnh ĐẠI QUÂN / AERIAL (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)
| SC | t | type | nội dung |
|---|---|---|---|
| SC_009 | 1:04 | still_kenburns | Still for ken-burns: very high aerial, night, wide |
| SC_012 | 1:30 | still_kenburns | Still for ken-burns: very high aerial, grey drizzly day, wide |
| SC_013 | 1:42 | still_kenburns | Still for ken-burns: high wide along the road, slightly elevated |
| SC_032 | 4:20 | still_kenburns | Still for ken-burns: very high aerial, night, wide |
| SC_051 | 7:00 | still_kenburns | Still for ken-burns: high aerial of the river valley, misty morning |
| SC_054 | 7:28 | video8s | A handheld drone controller screen filling the frame: high-angle live aerial view, rain specks on the lens |
| SC_075 | 10:20 | still_kenburns | Still for ken-burns: high aerial of the river valley in rain |
| SC_079 | 10:54 | still_kenburns | Still for ken-burns: high aerial of the ford in rain |
| SC_083 | 11:30 | video8s | Wide from mid-height above the south shoal, static |
| SC_084 | 11:38 | video8s | Wide from the water's edge, slight pan with the cavalry |
| SC_087 | 12:02 | video8s | Mid-height aerial wide over the shoal, static |
| SC_089 | 12:18 | video8s | Wide from mid-height above the water's edge, static |
| SC_092 | 12:42 | video8s | Mid-height aerial wide over the shoal, static |
| SC_125 | 17:20 | still_kenburns | Still for ken-burns: aerial of the hill fort at night in rain |
| SC_196 | 27:10 | still_kenburns | Still for ken-burns: aerial of the pass saddle at dusk |
| SC_198 | 27:30 | still_kenburns | Still for ken-burns: aerial of the saddle as the last light dies |
| SC_216 | 29:56 | video8s | Mid-height wide over the saddle, static (keyframe = beat A) |
| SC_240 | 33:08 | video8s | Wide from above the east mouth of the pass at night, static |
| SC_249 | 34:20 | still_kenburns | Still for ken-burns: aerial of the saddle in grey rain |
| SC_256 | 35:20 | still_kenburns | Still for ken-burns: elevated wide on the fork below the pass in rain |
| SC_264 | 36:26 | still_kenburns | Still for ken-burns: elevated wide on the muddy road in rain |
| SC_268 | 37:00 | still_kenburns | Still for ken-burns: high aerial of the valley in rain |
| SC_271 | 37:30 | still_kenburns | Still for ken-burns: high aerial of the river, monsoon afternoon |
| SC_283 | 39:12 | still_kenburns | Still for ken-burns: aerial of the north-bank reed bed in rain |
| SC_284 | 39:22 | still_kenburns | Still for ken-burns: high aerial of the southward road in rain |

## 7. SC RỦI RO AI & cách né trong prompt
| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |
|---|---|---|
| SC_001 | tay cận cầm vật thể | 1 bàn tay băng, ống cao su, không thấy ngón; 1 vật thể chuyển động (dầu) |
| SC_002 | mặt cận + lửa nền | lửa out of focus, 1 người, không tay trong khung |
| SC_003 | 2 beat + vũ khí bắn | beat A insert riêng; beat B 1 chớp lửa, xạ thủ mặt khuất, xe mục tiêu xa |
| SC_004 | hai xe giống nhau + chữ số | xe cháy out of focus, số 3 trầy (chỉ 1 chữ số, không Hangul) |
| SC_005 | vật nhỏ trong tay | lựu đạn trụ xám cầm thấp, ngón cái trên vòng kéo, không cận ngón tay |
| SC_006 | 2 mặt cận + lửa | ánh lửa từ 1 phía, máy tĩnh |
| SC_007 | đuốc xa nhiều điểm | chuỗi chấm lửa trên sườn tối, không hình người |
| SC_008 | đám lính chạy nền | out of focus, quay lưng |
| SC_009 | đại quân | aerial rất cao, chỉ chấm lửa |
| SC_010 | 2 beat + đám đông đi bộ | beat B insert riêng; beat A wide, mặt lính quay đi, 2 nhân vật ID gần máy |
| SC_011 | lỗ bu-lông cận | 2 lỗ tròn nhỏ, không chữ |
| SC_012 | đại quân | aerial rất cao, cột đen không chi tiết |
| SC_013 | đám đông | máy trên cao sau lưng hàng người, mưa che chi tiết |
| SC_014 | ngựa + người cận | ngựa vào từ mép phải, chỉ chân ngựa và tay roi; mặt lính quay xuống |
| SC_015 | đoàn đông + ngựa | tracking lùi, mặt lính khuất mũ, 2 nhân vật ID gần máy, xe bò/ngựa ở nền |
| SC_016 | tay cận + chân | 1 gót chân, kéo trong tay, không ngón rõ; mặt lính ngoài khung |
| SC_017 | 2 người đi + mưa | tracking ngang chậm, không vật thể khác chuyển động |
| SC_018 | — | — |
| SC_019 | rack focus 2 lớp | 2 người, tracking chậm |
| SC_020 | kỵ binh hai phe xa | wide từ trên cao, mưa che chi tiết, 2 nhân vật ID sau lưng |
| SC_021 | va chạm kỵ binh | wide trên cao, mưa/bùn che chân ngựa, không cận |
| SC_022 | súng cận + ngựa vào khung | súng nòng hạ, tay đặt trên ốp; ngựa vào từ sau lưng |
| SC_023 | đốm lửa xa nhiều | chấm cam, không hình lều rõ |
| SC_024 | đám đông cận qua kính đêm | hạt nhiễu, hình người cúi lưng, không mặt |
| SC_025 | — | — |
| SC_026 | — | — |
| SC_027 | bàn chân trần cận | chỉ 1 bàn chân góc khung, nứt nẻ, không ngón rõ |
| SC_028 | nhiều người + đèn chuyển động | tracking chậm 1 nguồn sáng, mặt khuất |
| SC_029 | — | — |
| SC_030 | — | — |
| SC_031 | — | — |
| SC_032 | đại quân | aerial rất cao |
| SC_033 | — | — |
| SC_034 | chữ trên bảng | 'blurred marker figures'; 2 người nhưng chỉ 1 mặt |
| SC_035 | tay cận cầm vật | 2 bàn tay chậm, 1 vật thể, không nút bấm có chữ |
| SC_036 | — | — |
| SC_037 | nhiều vật nhỏ + tay | high angle tĩnh, 1 bàn tay, không màn hình có chữ |
| SC_038 | nhiều người quanh lửa | lính phụ ở rìa, mặt khuất; 3 nhân vật ID |
| SC_039 | — | — |
| SC_040 | chữ trên thẻ tre | 'blurred carved marks' |
| SC_041 | — | — |
| SC_042 | bản đồ có chữ | 'contour lines, grease-pencil marks, no readable text' |
| SC_043 | hàng ngựa nền | dắt bộ chậm, người dắt quay lưng |
| SC_044 | vật lộn cận | POV kính đêm nhiễu hạt, 2 người, dao chỉ ánh, không máu |
| SC_045 | 3 mặt + lửa | 서아 chỉ tay, lính Tùy cúi đầu |
| SC_046 | ngựa + người leo | 1 con ngựa, wide, chuyển động chậm; lính phụ cười mặt quay đi |
| SC_047 | lên ngựa | 1 động tác, ngựa đứng yên, wide đủ thấy cả người |
| SC_048 | nhiều vật buộc + 2 người trên xe | máy tĩnh, 3 nhân vật ID, khối đồ mô tả gọn |
| SC_049 | đoàn đông cưỡi ngựa | wide bên hông, mưa che, mặt khuất |
| SC_050 | — | — |
| SC_051 | đại quân/trại | aerial, lều là mảng xám |
| SC_052 | 3 nhân vật | 을지문덕 quay lưng (giảm mặt) |
| SC_053 | drone cất cánh cận | 1 vật thể bay lên, bàn tay mở |
| SC_054 | đám đông từ trên cao | nhìn qua màn hình, mưa lấm ống kính, hình người cúi |
| SC_055 | người nhỏ từ trên cao | chỉ 6 chấm người rõ màu áo, không mặt |
| SC_056 | nhiều yếu tố | máy tĩnh, K2 nền tối, súng máy cận không tay cầm cò |
| SC_057 | hai hàng lính cận | chỉ 2–3 mặt nét, còn lại mờ; mặt hóp không gore |
| SC_058 | — | — |
| SC_059 | 5+ người trong lều | wide từ cửa, vệ sĩ mặt khuất mũ, 4 ID |
| SC_060 | — | — |
| SC_061 | chữ + tay cận | 'blurred brush strokes', 1 bàn tay cầm bút chậm |
| SC_062 | — | — |
| SC_063 | — | — |
| SC_064 | — | — |
| SC_065 | tracking lùi + hai hàng lính | lính out of focus |
| SC_066 | — | — |
| SC_067 | kỵ binh đông đuổi | ở hậu cảnh, mưa/bùn che, 2 ID gần máy |
| SC_068 | màn hình có số | chỉ chấm và bờ nước, số overlay |
| SC_069 | súng máy cận + tay | tay ngoài vành cò, mặt sau thước ngắm |
| SC_070 | ngựa dựng đứng số đông | wide thấp, nước bắn che, 1 sĩ quan rõ, không cận vó |
| SC_071 | lội nước tracking | 2 người, nước tới gối, chuyển động chậm |
| SC_072 | drone hạ cận | 1 vật thể, bàn tay mở, chuyển động chậm |
| SC_073 | — | — |
| SC_074 | — | — |
| SC_075 | — | — |
| SC_076 | — | — |
| SC_077 | — | — |
| SC_078 | — | — |
| SC_079 | đại quân | aerial cao, cột người là vệt |
| SC_080 | 3 ID + ngựa | ngựa đứng yên bên cạnh, máy tĩnh |
| SC_081 | — | — |
| SC_082 | — | — |
| SC_083 | kỵ binh đông | wide trên cao, mưa che chi tiết chân ngựa |
| SC_084 | va chạm số đông | wide, không cận thương vong |
| SC_085 | người trên ngựa cận | ngựa đứng, thân trên; kiếm 1 động tác |
| SC_086 | kỵ binh tán loạn | wide, cờ rơi là điểm nhìn |
| SC_087 | đám đông chạy | aerial trung, không mặt |
| SC_088 | lửa đầu nòng cối | chớp cam ngắn, tay xạ thủ chỉ đưa vào ống |
| SC_089 | nổ trong đám đông | wide, cột nước/cuội che, không cận |
| SC_090 | — | — |
| SC_091 | tay trên cò | máy sau lưng, tay 한승우 trên nắp tiếp đạn là điểm nhìn |
| SC_092 | đám đông đổi hình | aerial, không mặt |
| SC_093 | nhiều ngựa trong rừng | ngựa đứng, mờ, 2 ID |
| SC_094 | chữ trên bảng | 'blurred marker figures' |
| SC_095 | — | — |
| SC_096 | 40 bò + kỵ | POV ống nhòm xa, hai hàng bò là khối, người quay lưng |
| SC_097 | — | — |
| SC_098 | biển số cận | 1 chữ số 3 trầy, không Hangul |
| SC_099 | — | — |
| SC_100 | bò + ngựa + xe | still, hai hàng bò là khối, người quay lưng |
| SC_101 | — | — |
| SC_102 | — | — |
| SC_103 | 3 ID trong lều | máy tĩnh, đèn dầu 1 phía |
| SC_104 | bản đồ + tay cận | 2 ngón tay, nét vẽ mờ, không chữ |
| SC_105 | — | — |
| SC_106 | — | — |
| SC_107 | ngựa qua cổng đêm | wide, dắt bộ chậm |
| SC_108 | 4 ID trong lều | 을지문덕 quay lưng tiền cảnh, 3 mặt |
| SC_109 | — | — |
| SC_110 | — | — |
| SC_111 | vật nhỏ trong tay | 2 bàn tay dâng, máy tĩnh |
| SC_112 | — | — |
| SC_113 | — | — |
| SC_114 | chữ trên lụa | 'columns of brush calligraphy, no readable characters' |
| SC_115 | POV kính đêm | nhiễu hạt, người là khối sáng, không mặt |
| SC_116 | vật lộn tối | wide, chuyển động ngắn, không cận |
| SC_117 | — | — |
| SC_118 | — | — |
| SC_119 | vết thương | không gore, chỉ vải và nước nâu |
| SC_120 | — | — |
| SC_121 | — | — |
| SC_122 | — | — |
| SC_123 | — | — |
| SC_124 | — | — |
| SC_125 | — | — |
| SC_126 | nhiều người cầm đuốc | đứng yên, mặt quay đi, 1 người leo |
| SC_127 | vật kim loại cận + tay | 1 bàn tay, 1 viên đạn, chậm |
| SC_128 | — | — |
| SC_129 | — | — |
| SC_130 | — | — |
| SC_131 | ngựa + trống + nhiều người | 1 con ngựa gần máy, người quay đi |
| SC_132 | vật nhỏ trong tay | drone vỡ 1 khối, hai tay nâng |
| SC_133 | 2.000 kỵ nền | khối mờ phía sau, 1 ID rõ |
| SC_134 | hơi nước + xe + người chạy | 1 hiện tượng (hơi trắng), pan chậm |
| SC_135 | — | — |
| SC_136 | — | — |
| SC_137 | kỵ binh hai phe | wide, mưa, không cận; 1 ID rõ |
| SC_138 | dây thòng lọng kéo người | wide, 1 động tác |
| SC_139 | lửa nhỏ + vải đập | 1 ngọn lửa trên cành, 2 ID, không cận tay |
| SC_140 | dân + trẻ con + xe | tracking lùi, dân ở cửa xa, mặt khuất |
| SC_141 | — | — |
| SC_142 | tia lửa + tay búa | chuyển động búa chậm, tia lửa nhỏ |
| SC_143 | — | — |
| SC_144 | đại quân xa | vệt đen dưới thung lũng, không chi tiết |
| SC_145 | — | — |
| SC_146 | — | — |
| SC_147 | — | — |
| SC_148 | chữ trên bảng | vệt bút dạ mờ |
| SC_149 | — | — |
| SC_150 | — | — |
| SC_151 | — | — |
| SC_152 | kỵ binh + dân + chó | wide trên cao, không cận |
| SC_153 | bắn + ngựa ngã | wide, chớp nòng, không cận |
| SC_154 | — | — |
| SC_155 | 3 ID quanh lò | máy tĩnh, ánh lò 1 phía |
| SC_156 | — | — |
| SC_157 | — | — |
| SC_158 | tay cận + búa | 2 bàn tay già, búa nhỏ, chuyển động đều chậm |
| SC_159 | — | — |
| SC_160 | tracking lùi 3 người | chậm, mưa nhẹ |
| SC_161 | — | — |
| SC_162 | màn hình có số | cột pin không số, overlay |
| SC_163 | — | — |
| SC_164 | — | — |
| SC_165 | nhiều người ngủ | mặt quay vào tường, ánh sáng thấp |
| SC_166 | — | — |
| SC_167 | — | — |
| SC_168 | — | — |
| SC_169 | — | — |
| SC_170 | nhiều cung thủ trên gờ | nằm rạp thành khối, sương che, 1 ID |
| SC_171 | — | — |
| SC_172 | — | — |
| SC_173 | 2 bàn tay cận | tĩnh, vật thể 1 (ống đồng) |
| SC_174 | — | — |
| SC_175 | — | — |
| SC_176 | — | — |
| SC_177 | — | — |
| SC_178 | ngựa phi + tên | tracking ngang, sương che, 1 con ngựa gần máy |
| SC_179 | — | — |
| SC_180 | màn hình có số | sáng không số, overlay |
| SC_181 | — | — |
| SC_182 | — | — |
| SC_183 | — | — |
| SC_184 | — | — |
| SC_185 | — | — |
| SC_186 | chữ phấn | chỉ đường cong, chấm, mũi tên |
| SC_187 | kỵ binh | wide, không cận |
| SC_188 | — | — |
| SC_189 | ngựa + 2 ID + lính nền | máy tĩnh, lính quay lưng |
| SC_190 | — | — |
| SC_191 | — | — |
| SC_192 | tay + kim cận | 3 mũi chậm, patch rõ 7×4 cm |
| SC_193 | — | — |
| SC_194 | — | — |
| SC_195 | — | — |
| SC_196 | — | — |
| SC_197 | đoàn dài | wide, mặt khuất |
| SC_198 | — | — |
| SC_199 | — | — |
| SC_200 | nhiều vật nhỏ + đèn đỏ | tĩnh, hàng ngang |
| SC_201 | 4 người leo | máy tĩnh trên cao, mặt lính phụ khuất mũ |
| SC_202 | màn hình có số | sáng không số, overlay |
| SC_203 | POV kính đêm | nhiễu hạt, người là khối sáng |
| SC_204 | 80 người + 4 ID trong tối | silhouette, đèn đỏ là điểm nhìn, không mặt rõ |
| SC_205 | — | — |
| SC_206 | màn hình nhiệt có số | chỉ vệt trắng/xám, overlay |
| SC_207 | tên cắm thép cận | 1 mũi tên, rung, máy tĩnh |
| SC_208 | hàng trăm đuốc + kỵ | chuỗi lửa là chủ thể, người là bóng |
| SC_209 | — | — |
| SC_210 | tracer + đuốc | 3 vệt đỏ, máy sau lưng xạ thủ |
| SC_211 | ngựa phi cận số đông | thấp, ngắn, bùn/tối che chân, tai bịt là chi tiết |
| SC_212 | 80 người bắn | wide dọc tường, chớp nòng, mặt khuất |
| SC_213 | — | — |
| SC_214 | — | — |
| SC_215 | — | — |
| SC_216 | đám đông kỵ đổi hướng | wide trên cao, không mặt |
| SC_217 | người tụt dây từ trên cao | high angle, bóng, không mặt |
| SC_218 | — | — |
| SC_219 | màn hình + mặt | ánh xanh-trắng từ dưới, không số |
| SC_220 | — | — |
| SC_221 | bắn nhiều hướng | 2 nhóm rõ, mặt khuất mũ |
| SC_222 | — | — |
| SC_223 | tracking rung + ngựa + tên | 3 người, ngựa 1 con thoáng qua |
| SC_224 | — | — |
| SC_225 | vết thương | mũi tên trên vai giáp, không máu phun |
| SC_226 | — | — |
| SC_227 | tháp xoay + nòng nâng | 1 chuyển động cơ khí chậm |
| SC_228 | chớp nòng lớn | 1 chớp trắng, máy tĩnh, bụi thổi ra |
| SC_229 | đá vỡ | 1 hiện tượng vật lý, bụi che |
| SC_230 | thác đá + đuốc | 1 hiện tượng, bụi cam, máy tĩnh |
| SC_231 | — | — |
| SC_232 | đá bay | 1 tảng, 1 va chạm, bụi |
| SC_233 | trúng tên | wide, ngã nghiêng, không máu |
| SC_234 | vật lộn | 1 tay từ sau, 1 động tác, khung trống cuối |
| SC_235 | — | — |
| SC_236 | phóng PZF | 1 chớp, máy sau lưng, mục tiêu xa |
| SC_237 | — | — |
| SC_238 | drone hạ + tay chộp | 1 vật thể, 1 bàn tay |
| SC_239 | — | — |
| SC_240 | va chạm kỵ số đông đêm | wide, không cận |
| SC_241 | người leo dốc đá tối | bóng, wide |
| SC_242 | — | — |
| SC_243 | — | — |
| SC_244 | xác + mũ | xác quay mặt đi, không máu |
| SC_245 | — | — |
| SC_246 | xác bọc poncho | không mặt; súng dính máu = vệt sẫm |
| SC_247 | bóng xa | silhouette, không chi tiết mặt |
| SC_248 | — | — |
| SC_249 | — | — |
| SC_250 | nhiều người cúi đầu | mặt cúi/khuất, 2 ID rõ |
| SC_251 | patch cận | 1 lá cờ nhỏ, không chữ |
| SC_252 | — | — |
| SC_253 | — | — |
| SC_254 | — | — |
| SC_255 | chữ trên bảng | vệt mờ |
| SC_256 | — | — |
| SC_257 | vật nhỏ + dây | 2 bàn tay, chậm |
| SC_258 | POV kính đêm | mặt lính Tiên Ti nhòe xanh, chỉ 태오 rõ |
| SC_259 | — | — |
| SC_260 | 3 người | thông ngôn mặt bầm nhưng không gore |
| SC_261 | — | — |
| SC_262 | patch cận | 1 lá cờ nhỏ 7×4 cm, 1 động tác giật |
| SC_263 | — | — |
| SC_264 | bò + kỵ số đông | still elevated, khối |
| SC_265 | — | — |
| SC_266 | — | — |
| SC_267 | — | — |
| SC_268 | — | — |
| SC_269 | — | — |
| SC_270 | đêm không đuốc | hình rất tối, chỉ ánh xanh mờ là điểm nhìn |
| SC_271 | — | — |
| SC_272 | xe vào lau | 1 chuyển động, lau che |
| SC_273 | — | — |
| SC_274 | — | — |
| SC_275 | ngựa phi cận | 10 kỵ, cát bắn, dừng |
| SC_276 | đại quân nền | mảng đen xa |
| SC_277 | chữ thẻ tre | 'blurred carved marks' |
| SC_278 | — | — |
| SC_279 | — | — |
| SC_280 | — | — |
| SC_281 | — | — |
| SC_282 | — | — |
| SC_283 | — | — |
| SC_284 | — | — |
| SC_285 | — | — |
| SC_286 | — | — |
| SC_287 | — | — |

## 8. [OVERLAY] ở edit (số/chữ KHÔNG vẽ trong ảnh)
| SC | overlay |
|---|---|
| SC_017 | Subtitle 4 câu Hán + âm Hàn: 神策究天文 / 妙算窮地理 / 戰勝功既高 / 知足願云止 (신책구천문 / 묘산궁지리 / 전승공기고 / 지족원운지) |
| SC_034 | Bảng gỗ (nếu cần): '400 km' — chữ trong ảnh chỉ vệt bút dạ mờ |
| SC_053 | Màn hình controller: 배터리 30 |
| SC_068 | Màn hình controller: 배터리 19 · 거리 200 m |
| SC_072 | Màn hình controller: 배터리 14 |
| SC_094 | Bảng gỗ: 60 → 50 |
| SC_134 | Insert màn hình lái: vạch nhiệt đỏ + đèn cảnh báo (không chữ) |
| SC_148 | Bảng gỗ: 3 km |
| SC_162 | Tablet: 드론 1 · 충전 1회 · 야시경 40% |
| SC_180 | Màn hình controller: 배터리 14 → 비행 10 |
| SC_202 | Màn hình controller: 배터리 14 · 비행 10:00 |
| SC_206 | Màn hình: 비행 8:40 남음 |
| SC_228 | Insert thước ngắm: 잔탄 12 |
| SC_230 | Insert thước ngắm: 잔탄 08 |
| SC_255 | Bảng gỗ: 야시경 10 · 드론 0 |
| SC_287 | END CARD: 살수 612 · 4화 평양 |

### Quy tắc né chung (áp dụng toàn tập)
- **Đám đông cận**: mọi cảnh ≥6 người → wide/aerial hoặc máy sau lưng hàng người, mặt lính phụ quay đi/khuất mũ; chỉ nhân vật có ID mới thấy mặt rõ. Trại Tùy/bãi cuội/vượt sông = aerial hoặc trung cảnh 'không thấy điểm cuối'.
- **Chữ**: màn hình drone/tablet/bảng gỗ/lụa 필담/thẻ tre/thơ → prompt chỉ 'brush calligraphy / blurred marker figures / empty dark screen'; số thật overlay ở edit (decisions #1, #6). Biển '3' chỉ số Ả Rập.
- **Tay cầm súng**: K2C1/K3 'muzzle down / slung / resting on stones'; bắn = wide hoặc chớp lửa đầu nòng, không cận ngón tay trên cò. K6 = xạ thủ tì vai, mặt sau thước ngắm.
- **Ngựa + kỵ sĩ số đông**: aerial/tracking thấp, mưa/bụi che chi tiết chân ngựa; không cận vó. 40 con bò = wide, hai hàng, người đánh bò quay lưng.
- **POV kính đêm / màn hình drone / nhiệt**: 'monochrome green night-vision view with grain' / 'white-hot thermal aerial view' — không vẽ HUD số; overlay ở edit.
- **Xe + nước/hơi nước/lửa** (SC_003–004, 134–135, 227–230): 1 hiện tượng vật lý rõ (hơi trắng / chớp nòng / thác đá), máy tĩnh.
- **Mưa**: mọi SC D2+ có 'rain/drizzle' trong Light — không vẽ tia mưa dày che mặt; ướt bề mặt + hạt mưa trên vai/ống kính.
- **Hangul trên xe**: KHÔNG vẽ (chỉ số Ả Rập 1/2/3 + 태극기 nhỏ); '천둥' chỉ ở thoại/radio.
