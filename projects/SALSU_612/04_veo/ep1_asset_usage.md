# 1화 「요하」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)
> Đếm theo `04_veo/scenes_ep1.json` (291 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.

## 1. Nhân vật (CHAR) — số SC xuất hiện
| CHAR | SC | Derived state trong 1화 (SC) |
|---|---|---|
| CHAR_001 | 75 | — (base) |
| CHAR_002 | 27 | CHAR_002_powder_ep1 (13), CHAR_002_smoke_ep1 (2) |
| CHAR_003 | 31 | CHAR_003_mud_ep1 (5), CHAR_003_oil_ep1 (25) |
| CHAR_004 | 14 | CHAR_004_gloves_ep1 (4) |
| CHAR_005 | 22 | — (base) |
| CHAR_006 | 30 | CHAR_006_facepaint_ep1 (29) |
| CHAR_102 | 1 | CHAR_102_seated_throne (1) |
| CHAR_104 | 18 | CHAR_104_dust_ep1 (18) |
| CHAR_105 | 27 | CHAR_105_dusty_ep1 (27) |
| CHAR_106 | 13 | CHAR_106_bandaged_ep1 (11), CHAR_106_refugee_ep1 (2) |
| CHAR_107 | 9 | CHAR_107_camp_ep1 (6), CHAR_107_refugee_ep1 (3) |
| CHAR_201 | 5 | CHAR_201_robe_only_ep3 (4) |
| CHAR_205 | 23 | CHAR_205_survivor_ep1 (19) |

### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)
| Extra | SC |
|---|---|
| ROK_SOLDIERS | 30 |
| GOG_CAVALRYMEN | 17 |
| BOY_SCOUT | 13 |
| GOG_INFANTRY | 9 |
| XIANBEI_SCOUTS | 9 |
| REFUGEES | 7 |
| ROK_SOLDIER | 6 |
| GOG_ARCHERS | 4 |
| SUI_VANGUARD_GENERAL | 4 |
| SUI_EUNUCH | 3 |
| XIANBEI_ARCHER | 2 |
| ROK_DRIVER | 2 |
| OX_DRIVER | 2 |
| SUI_EUNUCH_READER | 1 |
| ROK_RADIOMAN | 1 |
| SUI_LABORERS | 1 |
| SUI_VANGUARD_CMDR_DEAD | 1 |
| ROK_GUNNER_TURRET | 1 |
| PYONGYANG_COURIER | 1 |

## 2. Địa điểm (LOC) — số SC
| LOC | SC | Sub-lock (SC) |
|---|---|---|
| LOC_001 | 24 | LOC_001 (5), LOC_001_bank (7), LOC_001_canal (1), LOC_001_march (3), LOC_001_north_steppe (2), LOC_001_sui_camp_day (1), LOC_001_sui_camp_night (1), LOC_001_sui_tent (4) |
| LOC_002 | 44 | LOC_002 (2), LOC_002_eastgate (4), LOC_002_eastroad (8), LOC_002_eastwall (5), LOC_002_gate (7), LOC_002_gateyard (3), LOC_002_granary (5), LOC_002_hall (5), LOC_002_night_road (2), LOC_002_siege_works (1), LOC_002_westwall (2) |
| LOC_003 | 183 | LOC_003_dawn (11), LOC_003_ford (3), LOC_003_ford_northbank (11), LOC_003_gully (13), LOC_003_hearth (3), LOC_003_hill_ford (10), LOC_003_hollow (27), LOC_003_k2 (7), LOC_003_medic (3), LOC_003_mortar (4), LOC_003_mouth (17), LOC_003_northridge (5), LOC_003_ridge_sunset (25), LOC_003_rim_day (1), LOC_003_steppe (17), LOC_003_tent (5), LOC_003_tent_ext (18), LOC_003_trail (1), LOC_003_westrim (2) |
| LOC_004 | 12 | LOC_004_parade (3), LOC_004_pavilion_ext (2), LOC_004_pavilion_int (7) |
| LOC_006 | 1 | LOC_006_hall (1) |
| LOC_008 | 18 | LOC_008_hill (7), LOC_008_steppe (11) |
| LOC_010 | 9 | LOC_010 (9) |

## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/UAV/EQP) — số SC
| ID | SC |
|---|---|
| VEH_002 | 58 |
| UAV_001 | 30 |
| VEH_001 | 29 |
| VEH_004 | 28 |
| VEH_206 | 28 |
| VEH_101 | 20 |
| WPN_201 | 18 |
| EQP_001 | 17 |
| VEH_003 | 15 |
| EQP_002 | 15 |
| VEH_205 | 10 |
| WPN_001 | 8 |
| WPN_101 | 6 |
| WPN_002 | 5 |
| WPN_003 | 2 |
| WPN_005 | 1 |
| WPN_004 | 1 |
| VEH_201 | 1 |

## 4. Đạo cụ (PROP) — số SC
| PROP | SC |
|---|---|
| PROP_005 | 27 |
| PROP_016 | 21 |
| PROP_015 | 17 |
| PROP_021 | 13 |
| PROP_012 | 9 |
| PROP_013 | 7 |
| PROP_009 | 7 |
| PROP_001 | 6 |
| PROP_006 | 5 |
| PROP_022 | 4 |
| PROP_007 | 3 |
| PROP_018 | 3 |
| PROP_019 | 3 |
| PROP_017 | 1 |
| PROP_002 | 1 |
| PROP_008 | 1 |
| PROP_010 | 1 |

## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)
| # | ref id | thư mục | số SC đính | trạng thái trong ref_jobs.json |
|---|---|---|---|---|
| 1 | CHAR_001_ref | characters | 75 | có job |
| 2 | LOC_003_wide | locations | 66 | có job |
| 3 | LOC_003_hollow_d1 | locations | 65 | **CHƯA CÓ — cần thêm job** |
| 4 | VEH_002_ref | vehicles | 58 | có job |
| 5 | CHAR_003_ref | characters | 31 | có job |
| 6 | UAV_001_ref | vehicles | 30 | có job |
| 7 | VEH_001_ref | vehicles | 29 | có job |
| 8 | CHAR_006_facepaint_ep1 | characters | 29 | có job |
| 9 | LOC_003_ford_night | locations | 29 | **CHƯA CÓ — cần thêm job** |
| 10 | VEH_004_ref | vehicles | 28 | có job |
| 11 | VEH_206_ref | vehicles | 28 | có job |
| 12 | CHAR_002_ref | characters | 27 | có job |
| 13 | CHAR_105_ref | characters | 27 | có job |
| 14 | LOC_002_detail | locations | 26 | có job |
| 15 | CHAR_005_ref | characters | 22 | có job |
| 16 | VEH_101_ref | vehicles | 20 | có job |
| 17 | CHAR_205_survivor_ep1 | characters | 19 | có job |
| 18 | WPN_201_ref | vehicles | 18 | có job |
| 19 | LOC_008_steppe_ep1 | locations | 18 | **CHƯA CÓ — cần thêm job** |
| 20 | CHAR_104_ref | characters | 18 | có job |
| 21 | PROP_015_ref | props | 17 | có job |
| 22 | LOC_003_steppe_d1 | locations | 17 | **CHƯA CÓ — cần thêm job** |
| 23 | EQP_001_ref | vehicles | 17 | có job |
| 24 | VEH_003_ref | vehicles | 15 | có job |
| 25 | EQP_002_ref | vehicles | 15 | có job |
| 26 | CHAR_004_ref | characters | 14 | có job |
| 27 | LOC_001_wide | locations | 13 | có job |
| 28 | PROP_021_ref | props | 13 | có job |
| 29 | EXTRA_boy_scout_ref | characters | 13 | **CHƯA CÓ — cần thêm job** |
| 30 | CHAR_106_refugee_ep1 | characters | 13 | có job |
| 31 | LOC_002_wide | locations | 13 | có job |
| 32 | WPN_102_ref | vehicles | 12 | **CHƯA CÓ — cần thêm job** |
| 33 | LOC_001_detail | locations | 11 | có job |
| 34 | VEH_205_ref | vehicles | 10 | có job |
| 35 | LOC_010_wide | locations | 9 | **CHƯA CÓ — cần thêm job** |
| 36 | PROP_012_ref | props | 9 | có job |
| 37 | CHAR_107_refugee_ep1 | characters | 9 | có job |
| 38 | WPN_001_ref | vehicles | 8 | có job |
| 39 | PROP_013_ref | props | 7 | có job |
| 40 | PROP_009_ref | props | 7 | có job |
| 41 | LOC_004_detail | locations | 7 | có job |
| 42 | PROP_001_ref | props | 6 | có job |
| 43 | WPN_101_ref | vehicles | 6 | có job |
| 44 | PROP_006_ref | props | 5 | có job |
| 45 | LOC_004_wide | locations | 5 | có job |
| 46 | WPN_002_ref | vehicles | 5 | có job |
| 47 | LOC_003_detail | locations | 5 | có job |
| 48 | LOC_002_interior | locations | 5 | có job |
| 49 | CHAR_205_ref | characters | 4 | có job |
| 50 | EXTRA_sui_vanguard_general_ref | characters | 4 | **CHƯA CÓ — cần thêm job** |
| 51 | PROP_022_ref | props | 4 | có job |
| 52 | CHAR_201_robe_only_ep3 | characters | 4 | có job |
| 53 | PROP_007_ref | props | 3 | có job |
| 54 | PROP_019_ref | props | 3 | có job |
| 55 | WPN_003_ref | vehicles | 2 | có job |
| 56 | PROP_017_ref | props | 1 | có job |
| 57 | CHAR_201_ref | characters | 1 | có job |
| 58 | CHAR_006_ref | characters | 1 | có job |
| 59 | PROP_002_ref | props | 1 | có job |
| 60 | WPN_005_ref | vehicles | 1 | có job |
| 61 | PROP_008_ref | props | 1 | có job |
| 62 | PROP_010_ref | props | 1 | có job |
| 63 | WPN_004_ref | vehicles | 1 | có job |
| 64 | VEH_201_ref | vehicles | 1 | có job |
| 65 | CHAR_102_ref | characters | 1 | có job |
| 66 | LOC_006_interior | locations | 1 | có job |

### Ref CHƯA CÓ trong ref_jobs.json (đề xuất world-designer/character-designer thêm; glabs-operator tạo trước lô ảnh cảnh)
- `LOC_003_steppe_d1` (locations, 16:9): thảo nguyên cỏ vàng phẳng D1 + đoạn đường nhựa 50 m bị cắt + đoàn xe không lưới — prompt = sub-lock `LOC_003_steppe` trong build.py + style tag.
- `LOC_003_hollow_d1` (locations, 16:9): hõm cỏ trũng D1, xe dưới lưới, gò cỏ phía đông — sub-lock `LOC_003_hollow`.
- `LOC_003_ford_night` (locations, 16:9): bến suối đá cuội đêm, hai bờ bùn, gò bắc — sub-lock `LOC_003_ford` (trận P10).
- `LOC_008_steppe_ep1` (locations, 16:9): thảo nguyên đông-nam, đoàn dân chạy nạn, khói làng cháy chân trời — sub-lock `LOC_008_steppe` (LOC_008 lock gốc là làng núi xanh 3화 → KHÔNG dùng cho 1화).
- `LOC_010_wide` (locations, 16:9): đêm 철원 đường đất đóng băng giữa đồi thông (P-27 đã DUYỆT, bible chưa có) — sub-lock `LOC_010`.
- `WPN_102_ref` (vehicles, 16:9): bộ binh + cung thủ Goguryeo (giáp lamellar, mũ chỏm ngắn, giáo dài, khiên tròn, cung 맥궁) — dùng cho trận cầu phao P4, 치 cổng đông P10, 500 창병 P10 (hiện chỉ có VEH_101 kỵ giáp ngựa và WPN_101 cung).
- `EXTRA_boy_scout_ref` (characters, 3:4): 소년 척후 ~17 tuổi — xuất hiện 13 SC (P4, P6) → cần ref riêng để không drift.
- `EXTRA_sui_vanguard_general_ref` (characters, 3:4): 수 전군총관 (râu đen-xám, ~55 — PHẢI khác CHAR_202 râu trắng) — 6 SC (P7, P12).

### Thứ tự chạy ref đề xuất (P1 → P3)
- **P1 (≥15 SC):** CHAR_001_ref, LOC_003_wide, LOC_003_hollow_d1, VEH_002_ref, CHAR_003_ref, UAV_001_ref, VEH_001_ref, CHAR_006_facepaint_ep1, LOC_003_ford_night, VEH_004_ref, VEH_206_ref, CHAR_002_ref, CHAR_105_ref, LOC_002_detail, CHAR_005_ref, VEH_101_ref, CHAR_205_survivor_ep1, WPN_201_ref, LOC_008_steppe_ep1, CHAR_104_ref, PROP_015_ref, LOC_003_steppe_d1, EQP_001_ref, VEH_003_ref, EQP_002_ref
- **P2 (5–14 SC):** CHAR_004_ref, LOC_001_wide, PROP_021_ref, EXTRA_boy_scout_ref, CHAR_106_refugee_ep1, LOC_002_wide, WPN_102_ref, LOC_001_detail, VEH_205_ref, LOC_010_wide, PROP_012_ref, CHAR_107_refugee_ep1, WPN_001_ref, PROP_013_ref, PROP_009_ref, LOC_004_detail, PROP_001_ref, WPN_101_ref, PROP_006_ref, LOC_004_wide, WPN_002_ref, LOC_003_detail, LOC_002_interior
- **P3 (<5 SC):** CHAR_205_ref, EXTRA_sui_vanguard_general_ref, PROP_022_ref, CHAR_201_robe_only_ep3, PROP_007_ref, PROP_019_ref, WPN_003_ref, PROP_017_ref, CHAR_201_ref, CHAR_006_ref, PROP_002_ref, WPN_005_ref, PROP_008_ref, PROP_010_ref, WPN_004_ref, VEH_201_ref, CHAR_102_ref, LOC_006_interior

## 6. SC cần ảnh ĐẠI QUÂN / AERIAL (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)
| SC | t | type | nội dung |
|---|---|---|---|
| SC_006 | 0:40 | video8s | Very high aerial wide, static, no zoom |
| SC_007 | 0:48 | still_kenburns | Still for ken-burns: wide low-angle from beside a great war drum, pulling out to the whole parade ground |
| SC_009 | 1:00 | still_kenburns | Still for ken-burns: high aerial wide along a great road, sliding sideways along a line of army banners |
| SC_012 | 1:22 | video8s | Wide from a low rise, static |
| SC_022 | 2:42 | still_kenburns | Still for ken-burns: wide, from black opening onto silver dawn, very slow pull-out |
| SC_027 | 3:20 | still_kenburns | Still for ken-burns: medium-wide along a marching column, slow push |
| SC_028 | 3:30 | still_kenburns | Still for ken-burns: wide lateral slide, high vantage |
| SC_029 | 3:40 | still_kenburns | Still for ken-burns: very high aerial, slow pull-out |
| SC_032 | 4:06 | still_kenburns | Still for ken-burns: extreme high aerial, slow pull-out |
| SC_045 | 5:54 | still_kenburns | Still for ken-burns: straight-down drone view with a soft dark vignette, slow tilt toward the river |
| SC_047 | 6:10 | still_kenburns | Still for ken-burns: high drone aerial over the west bank, very slow pull-out |
| SC_053 | 7:00 | video8s | Slow aerial wide over the river, single slow drift |
| SC_059 | 7:48 | video8s | Wide from the east bank, Goguryeo line in the foreground, static |
| SC_074 | 9:50 | still_kenburns | Still for ken-burns: wide, slow drift east after a running figure |
| SC_077 | 10:16 | still_kenburns | Still for ken-burns: high aerial, slow pull-out |
| SC_092 | 12:18 | video8s | Medium-high aerial, single slow drift |
| SC_101 | 13:32 | still_kenburns | Still for ken-burns: wide of the hillside, pulling out from arrows in the grass to the commander |
| SC_103 | 13:50 | still_kenburns | Still for ken-burns: wide from the plain, slow push toward a figure on the hill |
| SC_105 | 14:08 | still_kenburns | Still for ken-burns: wide of a cavalry line on a ridge, backlit, slow lateral pull along the line |
| SC_126 | 16:58 | still_kenburns | Still for ken-burns: wide, sun on the horizon, slow lateral slide |
| SC_129 | 17:22 | still_kenburns | Still for ken-burns: wide, slow push along a column into darkness |
| SC_130 | 17:30 | still_kenburns | Still for ken-burns: high wide over a night camp, slow push toward the general's tent |
| SC_148 | 19:58 | still_kenburns | Still for ken-burns: high aerial, slow pull-out |
| SC_153 | 20:40 | still_kenburns | Still for ken-burns: high wide of a cavalry column, slow lateral slide |
| SC_155 | 21:00 | video8s | Very high aerial at night, one slow glide |
| SC_200 | 27:12 | video8s | From behind, pulling out wide, single move |
| SC_201 | 27:20 | still_kenburns | Still for ken-burns: wide, silhouette foreground, slow pull-out |
| SC_206 | 28:02 | video8s | Night-vision view from the hill, monochrome green, static |
| SC_234 | 31:46 | video8s | Low aerial following the head of the charge, single move |
| SC_245 | 33:16 | video8s | Wide from on the wall looking down, static |
| SC_248 | 33:40 | video8s | Low aerial along the slope, single slow drift |
| SC_263 | 35:46 | still_kenburns | Still for ken-burns: high aerial by day, slow pull-out |
| SC_264 | 35:56 | still_kenburns | Still for ken-burns: wide lateral slide over siege works |
| SC_274 | 37:22 | still_kenburns | Still for ken-burns: wide on the west wall, slow pull-out |
| SC_281 | 38:24 | still_kenburns | Still for ken-burns: wide exterior at night, slow push to the silk doorway |
| SC_289 | 39:32 | still_kenburns | Still for ken-burns: very high aerial at night, very slow pull-out |

## 7. SC RỦI RO AI & cách né trong prompt
| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |
|---|---|---|
| SC_001 | cận vật thể + lông vũ | tĩnh, 1 vật thể, không tay người trong khung (né deformed hands) |
| SC_002 | tay cận cầm vật thể | 1 bàn tay, chuyển động chậm, găng đen che chi tiết ngón |
| SC_003 | 2 beat trong 1 clip | nếu veo không cắt được, glabs-operator tạo 2 clip 4 s (insert giày + captain) và edit ghép |
| SC_004 | chữ trên màn hình | prompt 'empty dark map, crossed-out satellite icon, no readable text'; số 0/0 overlay edit |
| SC_005 | mặt lính phụ | máy sau lưng, mũ che |
| SC_006 | đám đông kỵ binh | aerial rất cao, chấm đen dưới bụi, không chi tiết |
| SC_007 | đám đông lính cận | khối ô vuông từ xa, mũ sắt lấp lánh, không mặt |
| SC_008 | chữ trong ảnh | 'soft unreadable brush calligraphy', shallow focus; không vẽ chữ Hán thật |
| SC_009 | đại quân | aerial, khối bụi thay người |
| SC_010 | chân dung lịch sử | không giống người thật (bible); nét mặt hư cấu theo lock |
| SC_011 | 2 nhân vật + xe | mặt hai người rõ, khoảng cách xa, không đám đông |
| SC_012 | nhiều lính nhỏ + 7 xe | wide xa, lính chỉ là bóng nhỏ, không mặt |
| SC_013 | 7 xe chuyển động + đêm | tracking 1 chiều, đèn pha che chi tiết, không mặt lính |
| SC_014 | tay cận + sổ chữ | sổ chỉ 'pencil marks', không chữ đọc được |
| SC_015 | drone nhỏ lơ lửng + tay | 1 vật, chuyển động chậm |
| SC_016 | nhãn lọ có chữ | 'plain white plastic bottles, no labels' |
| SC_018 | chữ tablet | 'soft glow, no readable text' |
| SC_019 | chữ trên bản đồ | chỉ đường đồng mức + lưới, không địa danh đọc được |
| SC_020 | kim la bàn quay | chuyển động nhỏ trong vật nhỏ; nếu veo không làm được, chấp nhận flash + rung kim |
| SC_021 | nhiều đèn tắt lần lượt | chuỗi đơn giản, máy tĩnh |
| SC_023 | mép nhựa quá thẳng có thể AI vẽ như vỉa hè | 'clean knife-straight edge, no curb, no kerb stone' |
| SC_025 | LCD chữ | 'faint channel glow, no readable text' |
| SC_026 | mặt lính phụ | handset che mặt |
| SC_027 | đám đông lính | bụi che chân/mặt, hàng dài xa dần |
| SC_028 | đám đông dân phu | high vantage, bụi, không mặt |
| SC_030 | tay cận | 1 bàn tay đeo găng, đất rơi |
| SC_034 | tay cận | bàn tay phẳng, không cầm gì |
| SC_035 | hàng lính đứng | nhìn từ sau/profile, chỉ 박기철 rõ mặt |
| SC_037 | chữ/số trong ảnh | blurred pencil, không ký tự; số thật overlay edit |
| SC_040 | 4 mặt trong 1 khung | wide, mỗi người 1 dấu hiệu (la bàn / kính bảo hộ / mũ lưỡi trai / boonie) |
| SC_043 | drone qua khe lưới | 1 vật nhỏ bay lên, máy tĩnh |
| SC_044 | màn hình + 3 mặt | mặt nghiêng, screen chiếm khung; không chữ HUD |
| SC_045 | HUD drone | chỉ vignette mềm, không chữ/số |
| SC_046 | đại quân trên màn hình | chấm nhỏ từ trên cao, không mặt |
| SC_050 | số pin trên màn hình | 'amber indicator, no digits'; số overlay edit |
| SC_053 | đại quân + tên bay | aerial, không cận |
| SC_054 | đám đông cận + tên | mũ/khiên che mặt, wide-medium, không máu |
| SC_055 | hàng lính cận | low angle ngược sáng, mũ che mặt |
| SC_056 | nhiều người trong nước | khiên che, tracking đều |
| SC_057 | cận giao chiến | không máu, giáp che, medium không cận mặt |
| SC_058 | cái chết | không máu, chỉ khuỵu + kéo lùi |
| SC_060 | ngựa giáp + kỵ sĩ số đông | tracking thấp, bụi bùn che chân |
| SC_061 | tay cận rút tên | 2 tay trên 1 cán, chuyển động 1 nhát |
| SC_062 | tay cầm súng | súng đeo chéo nòng xuống, máy sau lưng |
| SC_063 | tay cầm cung căng | 1 người, hai tay rõ, tĩnh |
| SC_064 | tay cầm súng | súng hạ chậm, kết thúc tay trống |
| SC_065 | 2 người + vật nhỏ | profile rõ, tay mở |
| SC_076 | tay cầm súng | nhặt rồi đeo nòng xuống |
| SC_078 | số pin | 'amber indicator, no digits' |
| SC_079 | đám đông từ trên cao | chấm người, không mặt |
| SC_080 | kỵ binh số đông trên màn hình | aerial, dải bụi |
| SC_081 | nhân vật trên màn hình nhỏ | chỉ 2 bím tóc đỏ + bọc hành lý làm dấu |
| SC_087 | 2 xe + lính nhảy lên | wide, lính nhỏ |
| SC_088 | 2 xe chạy + người | tracking 1 chiều, bụi che chi tiết xích |
| SC_089 | kỵ binh phi nước đại + cận | 1 kỵ sĩ rõ, còn lại bụi |
| SC_091 | ngựa ngã số đông | wide xa, bụi che, không cận |
| SC_094 | 3 mặt + máu | medium, máu chỉ trên vải quần, không vết thương cận |
| SC_095 | tay cận | 2 bàn tay tĩnh, găng xanh + tay già |
| SC_096 | màn hình + độ cao | không HUD số |
| SC_097 | tay cầm cung cận | 1 cung thủ, tư thế chuẩn |
| SC_098 | màn hình quay tít | chuỗi 3 hình: quay / nhiễu / đen |
| SC_099 | thương binh + tên cắm | medium, không máu cận, mặt quay đi |
| SC_100 | tay cầm súng bắn | lính phụ nghiêng, súng ở vai, chớp lửa nhỏ; tay 을보 trên thép là hành động chính |
| SC_102 | tay cầm vật | 1 tay, drone gãy rõ hình |
| SC_104 | tay cận cầm drone | 2 tay, xoay chậm |
| SC_105 | 300 kỵ | ngược sáng, silhouette, chỉ 해모루 rõ |
| SC_131 | 2 mặt + vật nhỏ | medium, tay cầm cánh quạt 2 ngón |
| SC_133 | chữ trên bản đồ | 'painted rivers and a square fortress, no characters' |
| SC_135 | POV kính đêm | monochrome green, grain, không chữ HUD |
| SC_136 | nhiều kỵ binh đêm | bóng tối che, 1 chuyển động máy; kỵ chỉ là hình khối |
| SC_137 | 2 nhóm lính | lính Goguryeo trên tường ngược sáng đuốc, lính Hàn từ sau |
| SC_144 | nhiều kỵ đêm | silhouette dưới trăng, wide xa |
| SC_146 | tay cầm dao | mũi dao vạch đất, tay 1 |
| SC_157 | 12 vật giống nhau | 2 hàng đều, đếm bằng bút |
| SC_164 | chữ trên bản đồ | nét nguệch ngoạc không đọc được |
| SC_168 | hàng lính | máy sau lưng hàng người |
| SC_170 | tay thả đạn cối | tay 1, đạn 1 |
| SC_174 | POV kính đêm + tay trên súng | tay chỉ trên chốt, không cận cò |
| SC_175 | bắn súng | chớp lửa đầu nòng xa, không cận tay |
| SC_193 | kỵ binh + lính đêm | silhouette, tĩnh |
| SC_194 | màn hình nhiệt | không HUD số |
| SC_198 | POV kính đêm | green mono, không HUD |
| SC_199 | dao + giết | không lưỡi dao cận, không máu; 1 chuyển động tay |
| SC_202 | POV kính đêm + kỵ số đông | hình khối xanh, không chi tiết |
| SC_205 | lặp chuyển động | nhịp đơn giản, tay không cận |
| SC_206 | nổ + ngựa | green POV xa, hình khối |
| SC_214 | kỵ binh đêm tracking | bóng tối, 1 mặt rõ |
| SC_215 | đám đông dân | torches + bóng, không mặt |
| SC_216 | giao chiến đám đông | wide, không máu |
| SC_217 | tay cầm súng bắn | lính nghiêng/sau, chớp lửa |
| SC_224 | xe qua nước | tĩnh, 1 chuyển động xe, bụi nước |
| SC_228 | đám đông trong xe | mặt cúi, đèn đỏ, khói |
| SC_229 | bắn súng cận | lính từ ngực lên, khói che |
| SC_234 | 300 kỵ | aerial thấp, đầu đoàn rõ, sau bụi/tối |
| SC_235 | giao chiến kỵ | medium-wide, tối + lửa |
| SC_236 | dây + móc | 1 dây rõ, không nhiều dây |
| SC_238 | dây căng + xích | tĩnh, cận 2 vật |
| SC_239 | cung thủ số đông | low angle ngược sáng đuốc |
| SC_243 | 500 lính | khối hàng ngũ, đuốc, không mặt |
| SC_245 | 500 lính | wide từ trên tường |
| SC_247 | nhiều yếu tố | medium-wide, tracer làm đường dẫn |
| SC_259 | 6 thương binh | hàng ngang, mặt quay đi |
| SC_264 | đám đông lao động | wide, không mặt |
| SC_265 | tay rút tên | 1 tay, 1 mũi tên |
| SC_269 | patch cờ + cờ lụa | tĩnh, cận, không chữ |
| SC_275 | 4 người nội thất | wide, mỗi người 1 dấu hiệu |
| SC_276 | chữ trên chiếu | 'soft unreadable brush calligraphy' |
| SC_277 | chữ | mờ, không ký tự thật; chữ Hán/dịch = subtitle edit |
| SC_281 | hàng trăm hoạn quan | hàng đầu cúi, xa, không mặt |
| SC_284 | tay cận đeo nhẫn | 1 tay, 1 vật |
| SC_291 | chữ | không tạo ảnh; end card ở edit |

### Quy tắc né chung (áp dụng toàn tập)
- **Đám đông cận**: mọi cảnh ≥6 người → wide/aerial hoặc máy sau lưng hàng người, mặt lính phụ quay đi/khuất mũ; chỉ nhân vật có ID mới thấy mặt rõ.
- **Chữ**: màn hình GPS/pin/HUD, sổ tay bút chì, chiếu chỉ, end card → prompt chỉ mô tả 'columns of brush calligraphy / blurred pencil figures / empty dark map screen'; số & chữ thật overlay ở edit (decisions #1, #6).
- **Tay cầm súng**: K2C1 luôn 'muzzle down / slung across chest / resting on a rock'; cận tay chỉ khi tay KHÔNG cầm súng (chạm tên, la bàn, bản đồ); bắn = wide hoặc chớp lửa đầu nòng, không cận ngón tay trên cò.
- **Ngựa + kỵ sĩ số đông**: aerial/tracking thấp, bụi che chi tiết chân ngựa; không cận vó.
- **POV kính đêm / màn hình drone**: mô tả 'monochrome green night-vision view with grain' / 'handheld screen showing…' — không vẽ HUD số; overlay ở edit.
- **Xe + nước/bùn** (SC_224–225, 236–241): 1 hành động vật lý rõ (nước bắn / xích quay / dây căng), máy tĩnh, không nhiều vật thể chuyển động.
- **Hangul trên xe**: KHÔNG vẽ (chỉ số Ả Rập 1/2/3 + 태극기 nhỏ); '천둥' chỉ ở thoại/radio.
