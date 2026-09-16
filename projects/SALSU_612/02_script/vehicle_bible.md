# 살수 612 — VEHICLE / WEAPON BIBLE (v3 · 2026-09-16 · world-designer — gom sau QC 5 kịch bản; nguồn SC = full_script_ep1 v3 / ep2 v2 / ep3 v2 / ep4 v2.1 / ep5 v2)

> Nguồn sự thật: `series_foundation.md` §5 (khí tài & tài nguyên), §7 (arc: 2화 K21 cháy · 3화 bỏ xe, 1 K21 nguyên vẹn rơi vào tay 탁발흠 · 4화 K2 còn 6 viên · 5화 K2 hết đạn, mắc bùn), §9 (visual). Không mâu thuẫn; muốn đổi → `logs/proposals.md`.
> ID: VEH_00x / WPN_00x / UAV_00x / EQP_00x = ROK hiện đại (khớp §5). **VEH_1xx / WPN_1xx = Goguryeo lịch sử · VEH_2xx / WPN_2xx = Tùy / Tiên Ti lịch sử** (theo quy ước CHAR_1xx / CHAR_2xx của foundation).
> `VISUAL_LOCK_EN` dán NGUYÊN VĂN vào mọi prompt có khí tài đó. `REF_PROMPT_EN` = 3/4 view, phông trắng thuần, 16:9 — dùng làm reference image `@name` cho G-Labs.
> Style tag ref phông trắng: `pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`
> Style tag cảnh (trong phim): bỏ "pure white background, even studio lighting".

---

## 0. QUY ƯỚC CHUNG ĐẠI ĐỘI 천둥 (ROK Army)

- **Camo xe:** ROK 3 màu — **xanh lá sẫm (chủ đạo ~50%) / nâu đất (~35%) / đen (~15%)** vệt lớn mềm, không pixel. Prompt: `three-tone green-brown-black South Korean army camouflage`.
- **Số hiệu:** mật danh đại đội "천둥" + số xe. Trên ảnh chỉ vẽ **số Ả Rập trắng** (1/2/3/4) stencil nhỏ ở hông tháp pháo/cửa — KHÔNG vẽ chữ Hangul (style tag "no text" và AI dễ sai chữ). Chữ "천둥" chỉ tồn tại trong thoại/radio. → xem Phụ lục C mục 1.
- **Cờ:** **태극기 nhỏ** (≈15 cm) dán trên hông tháp pháo sau số hiệu; lính: patch 태극기 **vai PHẢI** (quy định ROK: 부대마크 왼팔, 태극기 오른팔 — decisions P-38; cờ trên xe là marking xe, độc lập). Không vẽ phù hiệu lữ đoàn thật.
- **Ăng-ten:** xe chỉ huy và K2 có ăng-ten whip đen; sau 3화 ăng-ten K151 tháo gắn lên K2.
- **Damage timeline chung:** 1화 sạch, phủ **bụi vàng mịn** · 2화 vệt **khói đen + tro + vết cháy sém** một bên · 3화 **bùn ướt**, cành cây ngụy trang, thùng/phuy buộc ngoài · 4화 bùn dày, lau sậy phủ, trầy xước, vết tên · 5화 **bùn kín đến nửa thân, cháy sém, mắc mô cát, hết đạn**.
- Luôn có **người bên cạnh xe** để lấy tỷ lệ trong cảnh (channel style §13).

---

## VEH_001 — K2 흑표 (Black Panther) · "천둥 1" · HERO VEHICLE

| Trường | Nội dung |
|---|---|
| Model / type | Xe tăng chủ lực **K2 흑표** (Hyundai Rotem), ROK Army, ~55 tấn, pháo nòng trơn **120 mm L/55**, súng đồng trục 7.62 mm, **K6 12.7 mm trên cupola trưởng xe** (súng gắn liền xe — không phải WPN_004), kíp 3 người (전차장 / 포수 / 조종수) |
| Shape | Thân thấp dài, mũi vát dốc; **tháp pháo góc cạnh hình nêm**, mặt trước tháp hai mảng chéo; đuôi tháp (bustle) vuông chứa máy nạp đạn tự động; kính ngắm toàn cảnh trưởng xe (khối trụ nhỏ trên nóc trái), kính ngắm pháo thủ (hộp vuông trước phải); **6 ống phóng lựu khói mỗi bên tháp**; váy xích (side skirt) tấm dày phủ bánh; lưới thoát khí động cơ ở đuôi thân; giá đồ + thùng chứa ngoài đuôi tháp |
| Color / camo | Three-tone green-brown-black ROK camo (mục 0). 1화: phủ bụi vàng nhạt |
| Turret | Nêm thấp, quay 360°; nòng pháo dài có ống hút khói (bore evacuator) giữa nòng và bao nhiệt; cupola trưởng xe có K6 12.7; nắp pháo thủ phía trước |
| Wheels / tracks | **6 bánh chịu nặng mỗi bên** (bánh đôi cao su viền), bánh dẫn động sau, bánh dẫn hướng trước, xích thép guốc cao su; treo thủy khí (xe có thể "quỳ" hạ mũi — dùng khi bắn qua lỗ châu mai 2화 và chôn mình trong cát 5화) |
| Exterior markings | Số **1** trắng stencil hông tháp hai bên; 태극기 nhỏ sau số; **không** phù hiệu đơn vị thật; ăng-ten đen 2 cần |
| Interior đáng chú ý | Khoang trưởng xe: 2 màn hình màu (bản đồ số, hình ảnh kính ngắm nhiệt); màn hình hiển thị **"위성 0개"** (GPS mất) và **bộ đếm đạn "잔탄 22 → … → 06 → 00"** — đây là đạo cụ kể chuyện; máy nạp tự động ở bustle (16 viên sẵn) + giá 6 viên trong thân = **22 viên** (tải huấn luyện); ghế pháo thủ với thị kính; khoang lái nằm ngả với cần lái kiểu yoke |
| Tài nguyên (§5) | 22 viên 120 mm · 1 bình dầu (~400 km) · sau 3화 gánh toàn bộ dầu của đại đội; **APU** (máy phát phụ) nuôi pháo/FCS/sạc khi tắt máy chính |
| **Cái KHÔNG làm được (khóa cho script/veo)** | (a) **Lội nước không chuẩn bị ~1,2 m** — sâu hơn, nước tràn qua **lưới hút gió/ống xả ở đuôi thân** → động cơ sặc, tắt (5화 SC_197 박기철 "도하 준비 없이 일 점 이 미터. 가슴이면 아슬아슬합니다." → SC_206 "물이 껐습니다. 여울 목. 정지."): sông tắt máy, không phải người. (b) **Engine off + APU: pháo, tháp, FCS vẫn dùng được** — KHÔNG dùng lý do "xe ngủ = không bắn" (QC 3화); ràng buộc kịch 3화 = tháp "bị buộc dây" khi ổ sạc ngoài đang kéo tải (7 kính + drone + 4 radio cắm ổ đuôi) → rút dây mất ~2 phút. (c) Tắt máy chính để giấu nhiệt/tiếng, không phải vì không bắn được. (d) 1 lần sạc drone = **600 m** K2; APU 2 ngày = **3 km** (3화 SC_036/148). |

**Damage state theo tập**
| Tập | Trạng thái |
|---|---|
| 1화 | Sạch, sơn mới, phủ lớp bụi vàng mịn; lưới ngụy trang phủ khi đậu. Không bắn pháo chính (bị GIỮ vì dầu) |
| 2화 | Vệt bồ hóng đen quanh miệng nòng (đã bắn ~12 viên), vết cháy sém váy xích bên trái (hỏa công đêm), tro bám nóc, 3–4 mũi tên gãy cắm trong lưới/giá đồ, bụi vàng dày |
| 3화 | Bùn ướt bắn lên nửa thân; **can nhiên liệu (jerrycan) và 1 phuy 200L cuối buộc dây trên đuôi tháp** (P1 xi-phông, SC_001) → từ D4 **"전차가 노새가 됐습니다"**: 2 K6 + ống cối + thùng đạn buộc đuôi, 을보/아리 ngồi trên buồng động cơ (SC_048); cành thông phủ nóc; ăng-ten K151 gắn thêm; váy xích trái mất 1 tấm; **P7 rò nước làm mát trên dốc → 을보 gò miếng đồng vá ống** (vết đồng đỏ sáng trên đường ống hông trái, SC_118/1xx); **vết cháy sém tên lửa trên nóc** (아리 dập bằng khăn olive, P7); P10 bắn 4 viên vào vách đèo → bồ hóng mới, tên gãy cắm giá đồ |
| 4화 | Nằm im trong **đảo lau** (LOC_007 sub-lock `LOC_007_reed_island`): bùn dày, lau sậy cắm kín nóc và giá đồ, lưới phủ; vết cào của tên; đèn pha vỡ 1; P7 bắn 2 viên tại chỗ (SC_144–145; overlay bộ đếm 잔탄 08→07→06) → bồ hóng mới; trượt 3 km về đảo lau thứ hai (vết xích trong bùn, 5화 SC_057 "이틀 전 밤… 삼 킬로") |
| 5화 (P1–P9) | Ở mép lau cách **cổng họng bãi (여울 목) 300 m**, phủ lau; 6 viên cuối bắn từ đây (SC_078–086); bộ đếm 잔탄 06→00 |
| 5화 (P10 Phase 1–2, SC_197–208) | **Chạy 300 m cuối** xuống cổng họng, nước ngang ngực người; **nước qua lưới hút gió đuôi → động cơ sặc, tắt giữa khe** (SC_206), xích quay nửa vòng rồi lún cát, xe nghiêng nhẹ — **thân xe chắn ngang khe 60 m** = "cái nút chai"; 박기철 **xả van nhiên liệu** → vệt dầu loang quanh xe trôi xuống cổng họng (SC_207) |
| 5화 (P10 Phase 3–5, SC_213–249) | Tên đập nóc như mưa đá; 한승우 thả **lựu đạn nhiệt nhôm (PROP_025) vào khay máy nạp** → cửa tháp phun **lửa trắng-vàng, mép tháp đỏ, sắt lỏng trắng chói chảy xuống váy xích** → dầu trên nước bén lửa thành **vòng lửa quanh xe** trôi xuôi (SC_227); 탁발흠 đứng trên nóc xe cháy, giương cung, trúng tên 해모루, ngã xuống sông (SC_245–249) |
| 5화 (P11–P12, SC_251/281–283) | Aerial dưới cột nắng: tháp cháy đỏ, khói trắng, thân lún nghiêng, nước nâu tràn qua váy xích và nóc thân (SC_251). Mấy ngày sau, nước rút: **K2 nằm nghiêng 10° trong cát, thân đen sém, nửa thân chìm bùn khô nứt, nòng hạ, nắp cupola mở, tên gãy cắm nóc, 태극기 nhỏ hé dưới bùn** (SC_281); **biển tên "3" (PROP_023) đặt trên mép tháp cạnh số "1"** — 천둥 1 và 천둥 3 nằm cạnh nhau (SC_282); 박기철 "영입니다. 전부 영." |

**VISUAL_LOCK_EN (≤60 từ):**
`South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a South Korean K2 Black Panther main battle tank, three-quarter front-left view, low angular wedge-shaped turret, long 120mm smoothbore gun with bore evacuator, six twin rubber-rimmed road wheels per side under thick side skirts, six smoke grenade launchers on each side of the turret, commander's panoramic sight on the turret roof, 12.7mm machine gun on the commander's cupola, stowage basket at the turret rear, three-tone green-brown-black South Korean army camouflage, small white numeral 1 stenciled on the turret side with a small Korean flag beside it, two black whip antennas, clean factory condition with light yellow dust on the hull, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

**REF_PROMPT_EN_EP5 (3/4 view, phông trắng, 16:9 — derived state cuối 5화 P11–P12, SC_281–282):**
`Product-style reference photo of a destroyed South Korean K2 Black Panther main battle tank, three-quarter front-left view, hull tilted ten degrees and sunk to half its height in cracked dry grey-brown river mud, low angular wedge-shaped turret scorched black with heat-discolored blue-brown steel around the open commander's hatch, long 120mm gun depressed low, one side skirt panel missing, broken arrow shafts stuck on the roof and in the stowage basket, one headlight smashed, faded three-tone green-brown-black camouflage showing through mud and soot, small white numeral 1 and small Korean flag half hidden under dried mud on the turret side, a small scorched olive-drab steel nameplate with a scratched white numeral 3 lying on the turret edge beside the numeral 1, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## VEH_002 — K21 보병전투차 ×3 · "천둥 2 / 3 / 4"

| Trường | Nội dung |
|---|---|
| Model / type | Xe chiến đấu bộ binh **K21** (Hanwha/Doosan), ~25 tấn, pháo tự động **40 mm** + súng đồng trục 7.62, kíp 3 + 9 lính; **lội nước** bằng phao hơi gấp hai bên hông (đặc điểm nhận dạng — phao xẹp gấp thành tấm dày dọc hông) |
| Shape | Thân hộp góc cạnh, mũi vát mạnh, nóc phẳng có lối lính lên; **tháp pháo 2 người lệch phải**, nhỏ, góc cạnh, nòng 40 mm ngắn hơn K2 nhiều, có bao nòng; cửa đuôi hạ (ramp) cho lính; ống phóng khói 2 cụm |
| Color / camo | ROK three-tone (mục 0) |
| Turret | Nhỏ, vuông, lệch phải; kính ngắm trưởng xe/pháo thủ hộp trên nóc; nòng 40 mm có ống giảm giật mảnh |
| Wheels / tracks | **6 bánh chịu nặng mỗi bên**, xích thép hẹp hơn K2, váy xích tấm cao su-composite mỏng, tấm phao gấp dọc hông trên váy |
| Exterior markings | Số trắng **2 / 3 / 4** hông tháp; 태극기 nhỏ; 천둥 3 có thêm **vệt sơn trắng nhỏ hình mũi tên** trên cửa đuôi (để khán giả nhận ra xe bị Tùy chiếm ở 3화–5화) |
| Interior | Khoang lính 9 ghế treo dọc hai bên, đèn đỏ trần, giá súng K2C1, thùng đạn 40 mm dưới tháp; màn hình trưởng xe |
| Tài nguyên (§5) | 200 viên 40 mm/xe · 1 bình dầu/xe |

**Damage state theo tập (từng xe)**
| Tập | 천둥 2 | 천둥 3 | 천둥 4 |
|---|---|---|---|
| 1화 | Sạch, bụi vàng; bắn 40 mm đầu tiên vào kỵ binh Tiên Ti (P5 −60, P10 −60 "마지막 탄띠" SC_233); P10 kẹt bùn ở bến suối → **bò của dân + kỵ Goguryeo kéo ra** | Sạch, bụi vàng; **P10 hỏng bánh chịu nặng (bánh thứ 3 bên phải) khi vượt rãnh → P11 을보 rèn chốt sắt tạm ("쇠는 쇠요", PROP_019a)** — chạy được nhưng yếu | Sạch, bụi vàng |
| 2화 | Bồ hóng nòng, vết tên, tro; sortie cổng bắc/góc đông-nam −60 (SC_188); dầu **≈ cạn** cuối tập ("장갑차는 바닥" SC_273 — 2 tháng chạy máy sưởi/sạc/kính nhiệt đêm) | Bồ hóng nòng, tro; chốt sắt thô ở bánh phải, vệt dầu; dầu ≈ cạn | **CHÁY** trong hỏa công đêm ở LOC_003 (SC_139–150): thân đen sạm, phao hơi cháy rụi, tháp lệch, **200 viên 40 mm + hộp drone #2 nổ/cháy trong khoang**, khói âm ỉ đến sáng — xác xe ở lại thung lũng |
| 3화 | Rút hết dầu → **2 quả PZF-3 + dầu** (P1, SC_003–004): thân thủng, cháy cùng 2 K511 + K151; **160 viên 40 mm nổ trong xe** | Rút hết dầu, **biển tên "3" bị 박기철 tháo (PROP_023, SC_004/011)**, để nguyên vẹn (đuốc 탁발흠 cách 10 phút) → **탁발흠 chiếm**: cửa đuôi mở, kỵ Tiên Ti trèo lên, **cờ Tùy đỏ-vàng cắm lên tháp**, **40 con bò kéo** theo cột quân 70리/ngày (SC_097–098); ~60 viên 40 mm còn trong xe; **KHÔNG vượt 압록** — gửi về tây từ bờ bắc 압록 D16 với 200 kỵ hộ tống (decisions P-40 ep3) | Xác cháy |
| 4화 | — | Trên đường về tây (bò kéo, 70리/ngày); tới sân 육합성/요동 ~3화 D22 = 4화 D3 (P-53) | — |
| 5화 | — | **Đứng trong sân 육합성 15 ngày** trên cỗ xe gỗ khổng lồ bánh lún bùn, phủ **vải dầu bám bùn khô** (một góc váy xích + bánh chịu nặng lộ, **vệt sơn trắng hình mũi tên trên cửa đuôi**), cờ Tùy cắm trên vải rũ nước, bò đã tháo ách; **hộp sơn mài đen đựng drone #4** trên tay hoạn quan (SC_270); 양제 kéo vải dầu, đặt tay lên thép: "…내년." (SC_271) — open loop series 2 「613」 | — |

**VISUAL_LOCK_EN (≤60 từ):**
`South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9 — bản gốc 천둥 2):**
`Product-style reference photo of a South Korean K21 infantry fighting vehicle, three-quarter front-left view, angular boxy hull with steep sloped glacis, small two-man turret offset to the right with a short 40mm autocannon and boxy sights on top, folded rubberized flotation panels along the hull sides above thin side skirts, six road wheels per side, rear troop ramp, smoke grenade launchers, three-tone green-brown-black South Korean army camouflage, small white numeral 2 stenciled on the turret side with a small Korean flag beside it, one black whip antenna, clean condition with light yellow dust, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

**REF_PROMPT_EN_CAPTURED (3/4 view, phông trắng, 16:9 — 천둥 3 trong tay Tùy, 3화–5화):**
`Product-style reference photo of a captured South Korean K21 infantry fighting vehicle, three-quarter rear-left view, angular boxy hull in mud-streaked three-tone green-brown-black camouflage, rear troop ramp lowered and open, a red and yellow Sui dynasty silk banner with black tassels tied to the turret, thick hemp ropes lashed around the hull front for horses to tow, a small white arrow mark painted on the ramp, dried mud and grass on the tracks, no fuel cans, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

**REF_PROMPT_EN_BURNED (3/4 view, phông trắng, 16:9 — 천둥 4 sau hỏa công, 2화):**
`Product-style reference photo of a burned-out South Korean K21 infantry fighting vehicle, three-quarter front-right view, hull scorched black and rust-brown, paint blistered, flotation panels burned away, turret slightly dislodged, rubber on the road wheels melted, thin grey smoke still rising from the open hatches, charred remains of a camouflage net hanging from the side, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## VEH_003 — K511A1 2½톤 트럭 ×2

| Trường | Nội dung |
|---|---|
| Model / type | Xe tải quân sự **K511A1** (Kia), 6×6, 2,5 tấn; **xe #1 chở đạn** (thùng đạn, đạn cối, PZF), **xe #2 chở 2 phuy dầu 200L** + phụ tùng |
| Shape | Ca-bin cứng góc cạnh 2 chỗ, mũi dài có lưới tản nhiệt dọc, thùng sau khung vòm bạt xanh olive; bậc lên thùng sau; lốp gai lớn |
| Color / camo | ROK three-tone; bạt thùng **olive đơn sắc**, bạc màu |
| Turret | Không; xe #1 có **vòng gắn K6 12.7 mm trên nóc ca-bin** (WPN_004 #1) |
| Wheels | 6 bánh lốp gai lớn (2 trước, 4 sau đôi); lốp trước phải xe #2 có **mũi tên Goguryeo cắm** (tín hiệu xuyên không đầu tiên — 1화 SC_001; **do 소년 척후 ~17 tuổi đi theo 해모루 bắn**, không phải 해모루 — P-36; 백성민 trả mũi tên này, 한승우 giữ một mũi khác rút từ gỗ cổng đông — P-28) |
| Exterior markings | Số trắng nhỏ trên cửa; 태극기 nhỏ; xe #2 có ký hiệu **hình tam giác đỏ (nhiên liệu)** nhỏ trên bạt sau |
| Interior | Ca-bin: vô-lăng, radio gắn, bản đồ nhét cửa; thùng #1: thùng đạn xanh xếp chồng, dây chằng; thùng #2: 2 phuy 200L đứng buộc dây, can nhựa, hộp dụng cụ, lốp dự phòng |

**Damage state:** 1화 sạch bụi vàng, lốp xe #2 thủng tên (thay lốp dự phòng — cảnh đầu) · 2화 tro, bạt cháy xém một góc (hỏa công), xe #2 mất 1 phuy · 3화 **đốt** ở LOC_003 (P1 SC_001–010: 2 K511 + K151 cháy sau lưng 박기철 đang xi-phông; "트럭은 반" dầu 2화 SC_273) · 4–5화 không xuất hiện.

**VISUAL_LOCK_EN (≤60 từ):**
`South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a South Korean K511A1 six-wheeled military cargo truck, three-quarter front-left view, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows with the rear flap open showing two green 200-liter fuel drums strapped upright, big lugged tires, a machine gun ring mount on the cab roof, three-tone green-brown-black South Korean army camouflage on the cab, faded olive canvas, small Korean flag on the door, light yellow dust, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## VEH_004 — K151 소형전술차 (xe chỉ huy)

| Trường | Nội dung |
|---|---|
| Model / type | Xe chiến thuật hạng nhẹ **K151** (Kia KLTV), 4×4 bọc thép nhẹ, bản chỉ huy: radio PRC-999K gắn xe, **máy phát điện nhỏ** kéo theo/đặt sau (sạc drone, kính đêm, tablet) |
| Shape | Thân hộp cao, kính chắn gió chia 2 tấm dốc, cửa dày, nóc có **cửa nóc tròn (hatch) gắn K6** (WPN_004 #2), 3 ăng-ten whip, giá đồ nóc, lốp lớn, đèn pha tròn có lồng |
| Color / camo | ROK three-tone |
| Wheels | 4 bánh lốp gai lớn run-flat |
| Exterior markings | Số trắng nhỏ; 태극기 nhỏ; **tấm pin mặt trời gấp** trên nóc — **chỉ sạc pin AA chậm, KHÔNG sạc drone** (decisions #5: giữ áp lực tài nguyên) |
| Interior | 4 ghế, giá radio giữa 2 ghế trước, đèn màn hình xanh, bản đồ giấy kẹp, dây sạc chằng chịt ra sau → đây là "ổ điện" của đại đội |

**Damage state:** 1화 sạch bụi; màn hình nhiễu trắng rồi tắt đêm 철원 (SC_021), sáng "위성 0개" · 2화 tro, kính nứt vì đá ném; máy phát "드론 열다섯 번 = 삼십 일" (SC_079) · 3화 **đốt** P1 (radio + ăng-ten tháo lên K2; máy phát gom nhiên liệu vào "사백") · 4–5화 không xuất hiện.

**VISUAL_LOCK_EN (≤60 từ):**
`South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a South Korean K151 light tactical 4x4 command vehicle, three-quarter front-right view, tall boxy lightly-armored body, two-piece sloped windshield, thick doors, round roof hatch with a 12.7mm heavy machine gun, three black whip antennas, roof rack with a folded solar panel and a small portable generator, big lugged tires, caged round headlights, three-tone green-brown-black South Korean army camouflage, small Korean flag on the door, light yellow dust, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## WPN_001 — K2C1 소총 ×90

| Trường | Nội dung |
|---|---|
| Model | Súng trường tấn công **K2C1** 5.56 mm (bản K2 nâng cấp có ray Picatinny), băng 30 viên; ~240 viên/người (8 băng) |
| Shape | Thân đen, **ốp tay ray 4 mặt**, báng **gập ngang** kiểu K2 (khung thép), tay cầm ống, ống ngắm điểm đỏ nhỏ trên ray, đèn pin kẹp bên; dây đeo 2 điểm |
| Color | Đen mờ; băng đạn thép đen; ống ngắm đen |
| Markings | Không |
| Damage | 1화 sạch · 3화 bùn, băng dán băng keo đôi · 5화 xước, dây buộc, nhiều khẩu **hết đạn, cắm lưỡi lê** (K2C1 gắn lưỡi lê được) |

**VISUAL_LOCK_EN:** `South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a South Korean K2C1 5.56mm assault rifle, three-quarter view from the right side, black matte finish, quad Picatinny rail handguard, side-folding skeleton stock extended, 30-round steel magazine, small red-dot sight on the top rail, tactical light clamped to the side rail, two-point sling, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## WPN_002 — 81mm 박격포 KM187 ×2

| Trường | Nội dung |
|---|---|
| Model | Cối **81 mm KM187**, 120 viên (HE + vài viên khói/chiếu sáng); tổ 4 người/khẩu |
| Shape | Nòng thép dài ~1.3 m, **chân hai càng (bipod)** có tay quay tầm/hướng, **đế tròn** nhôm, kính ngắm cối nhỏ; đạn hình giọt nước có cánh đuôi, xếp trong ống nhựa xanh |
| Color | Xanh olive sẫm, nòng đen |
| Damage | 2화 nòng cháy sém, đế lún cát · 5화 chôn nửa đế trong cát mô, chân càng cong |

**VISUAL_LOCK_EN:** `81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of an 81mm KM187 infantry mortar set up for firing, three-quarter view, dark olive steel tube on a two-leg bipod with traversing and elevating handwheels, round aluminum baseplate, small optical sight, three finned high-explosive mortar bombs and their green plastic carrying tubes laid beside it, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## WPN_003 — K3 경기관총 ×6

| Trường | Nội dung |
|---|---|
| Model | Súng máy hạng nhẹ **K3** 5.56 mm (kiểu Minimi), 1.000 viên/khẩu, băng dây trong hộp nhựa 200 viên |
| Shape | Nòng dài có tay xách, **chân hai càng gập**, hộp dây đạn nhựa xanh gắn dưới, báng cố định, tay cầm |
| Color | Đen; hộp đạn xanh olive |

**VISUAL_LOCK_EN:** `South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a South Korean K3 5.56mm light machine gun on its folding bipod, three-quarter view from the right, black finish, long barrel with carrying handle, green 200-round plastic belt box attached under the receiver with a length of linked ammunition, fixed stock, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## WPN_004 — K6 중기관총 12.7mm ×2

| Trường | Nội dung |
|---|---|
| Model | Súng máy hạng nặng **K6** 12.7 mm (dòng M2), 800 viên/khẩu; **#1 trên vòng nóc K511 #1, #2 trên hatch K151** (K6 trên cupola K2 là của xe, không tính) |
| Shape | Thân hộp thép dài, nòng dày có tản nhiệt lỗ, tay cầm đôi phía sau, khóa nòng kéo bên phải, dây đạn 12.7 to bản; **3화 tháo xuống giá 3 chân** (tripod M3 nặng), 2 người khiêng |
| Color | Đen xám kim loại; giá ba chân olive |
| Damage | 3화 tháo khỏi xe, khiêng bộ → 5화 đặt trên mô cát cạnh K2, bùn |

**VISUAL_LOCK_EN:** `K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a K6 12.7mm heavy machine gun on a heavy olive tripod, three-quarter view from the rear-left, long boxy grey-black steel receiver, thick perforated barrel jacket, twin spade grips, a wide belt of 12.7mm cartridges feeding from a green ammunition can, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## WPN_005 — 판처파우스트 3 (PZF-3) ×6 · 18 quả

| Trường | Nội dung |
|---|---|
| Model | Súng chống tăng vác vai **PZF-3**, 6 bộ ngắm/ống phóng, 18 quả đạn (2화 dùng 6 vào tháp công thành → 5화 còn 6) |
| Shape | Ống phóng dài xanh olive, **đầu đạn to hình nón nhô trước ống**, cụm ngắm + cò tháo rời gắn bên trái, đệm vai, lá chắn kính ngắm |
| Color | Olive sẫm, đầu đạn đen |
| Damage | 2화: 6 ống rỗng vứt lại tường thành (ống dùng 1 lần, cụm ngắm giữ) |

**VISUAL_LOCK_EN:** `Panzerfaust 3 shoulder-fired anti-tank launcher, long dark olive tube with a large black conical warhead protruding from the front, detachable sight and trigger unit on the left side, shoulder rest`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a Panzerfaust 3 shoulder-fired anti-tank weapon, three-quarter view, long dark olive launch tube with a large black conical warhead protruding from the front, detachable sight and trigger unit mounted on the left side, shoulder rest, one spare warhead-and-tube beside it, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## WPN_006 — K4 고속유탄기관총 ×2 · 300 viên

| Trường | Nội dung |
|---|---|
| Model | Súng phóng lựu tự động **K4** 40 mm (dòng Mk19), 300 viên trong hộp dây 32 viên |
| Shape | Hộp thép vuông lớn, nòng ngắn dày, tay cầm đôi, **giá ba chân** nặng, hộp đạn thép gắn bên trái, dây lựu 40 mm hạt tròn |
| Color | Đen xám; giá olive |

**VISUAL_LOCK_EN:** `K4 40mm automatic grenade launcher, large square steel receiver, short thick barrel, twin grips, heavy olive tripod, steel ammunition can with a belt of 40mm grenades`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a K4 40mm automatic grenade launcher on a heavy olive tripod, three-quarter view from the rear-right, large square grey-black steel receiver, short thick barrel, twin grips, steel ammunition can on the left feeding a belt of 40mm grenades, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## UAV_001 — 정찰 드론 (quadcopter) ×4

| Trường | Nội dung |
|---|---|
| Model / type | Drone trinh sát quadcopter quân dụng cỡ nhỏ (sải ~80 cm), 4 rotor, camera gimbal 3 trục có **kênh nhiệt**; pin 30 phút; sạc từ K151; điều khiển bằng tay cầm có màn hình 7 inch (PROP_005). Không nêu hãng |
| Shape | Thân xám sẫm, 4 cánh tay gập, chân đáp ngắn, gimbal camera hình cầu dưới bụng, đèn LED nhỏ xanh/đỏ, ăng-ten cụt; hộp vận chuyển cứng đen |
| Color | Xám graphite mờ, viền cam nhỏ ở đầu cánh (nhận diện) |
| Markings | Số **1–4** trắng nhỏ trên cánh tay; 태극기 tem nhỏ trên thân |
| Damage / số lượng theo tập | 1화: 4 → **3** (drone #1 bị tên Tiên Ti bắn rơi trên thảo nguyên — xác vỡ cánh) · 2화: 3 → **2** (drone #2 cháy cùng xe trong hỏa công) · 3화: 2 → **1** (drone #3 hết pin giữa chuyến, không sạc được vì mất K151 — rơi xuống rừng) → **0** (drone #4 bị bắt cùng 태오 ở khe núi, nguyên vẹn, trong tay 탁발흠) · 4화: 0 · 5화: 0; **drone #4 trong hộp trên đường về Lạc Dương** (kết) |

**VISUAL_LOCK_EN (≤60 từ):**
`Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body`

**REF_PROMPT_EN (phông trắng, 16:9):**
`Product-style reference photo of a small dark graphite-grey military reconnaissance quadcopter drone, three-quarter view slightly from above, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera with thermal lens under the belly, tiny status LEDs, small white numeral on one arm, tiny Korean flag sticker on the body, its handheld controller with a seven-inch screen and folding antennas beside it, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## EQP_001 — 야간투시경 PVS-11K ×12

| Trường | Nội dung |
|---|---|
| Model | Kính nhìn đêm **PVS-11K** đơn nhãn (monocular), gắn mũ bằng cần gập, pin AA; 12 chiếc, ưu tiên trinh sát/lái xe/trưởng xe |
| Shape | Ống trụ đen ngắn ~12 cm, vật kính tròn trước, thị kính cao su sau, cần gập kim loại gắn mũ K1 (mũ sắt Hàn), khối pin nhỏ |
| Color | Đen mờ |
| Diễn biến | 1–2화: dùng đêm; 3화: **2 chiếc rơi vào tay địch** (cùng 태오) → 4화: **탁발흠 đội kính đêm lên mắt** — ảnh visual signature (xem VISUAL_LOCK_EN_ENEMY) · 5화: pin gần hết, chỉ vài chiếc còn sáng |

**VISUAL_LOCK_EN:** `PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack`

**VISUAL_LOCK_EN_ENEMY (탁발흠 đội, 4화):** `a black modern monocular night-vision tube strapped over one eye with cut leather cords onto a Xianbei fur-trimmed leather cap, the other eye bare, faint green glow in the eyepiece`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a PVS-11K monocular night vision device, three-quarter view, short black cylindrical tube with a round objective lens and a rubber eyecup, flip-up metal helmet mount arm, small battery pack, mounted on the front of a dark green South Korean K1 combat helmet, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## EQP_002 — 무전기 PRC-999K

| Trường | Nội dung |
|---|---|
| Model | Radio VHF **PRC-999K** bản đeo lưng + bản gắn xe; tầm 5–10 km địa hình đồi; **không vệ tinh**; pin sạc từ K151 → sau 3화 chỉ còn pin dự trữ |
| Shape | Hộp kim loại xanh olive sẫm ~30×25 cm, mặt điều khiển núm xoay + màn hình LCD nhỏ, ăng-tên whip dài 1.2 m hoặc ăng-ten băng ngắn, tổ hợp cầm tay (handset) dây xoắn, khung đeo lưng |
| Color | Olive sẫm, núm đen |
| Diễn biến | 1화: "위성 0개", chỉ nội bộ · 3화 tháo khỏi K151 gắn K2 · 5화: 1 máy còn pin, dùng ra hiệu lệnh cuối cùng |

**VISUAL_LOCK_EN:** `PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a PRC-999K South Korean military VHF backpack radio, three-quarter view, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset resting on top, mounted on a backpack frame, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

# PHẦN 2 — KHÍ TÀI LỊCH SỬ

## VEH_101 — 개마무사 (kỵ binh giáp ngựa Goguryeo)

| Trường | Nội dung |
|---|---|
| Type | Kỵ binh nặng Goguryeo (theo bích họa 안악 3호분 / 덕흥리): **ngựa mặc giáp lamellar toàn thân** (마갑) từ cổ đến mông, **mặt nạ ngựa sắt** (마면갑) có lỗ mắt; kỵ sĩ giáp lamellar sắt kín thân + tay + ống chân, **mũ trụ sắt chỏm lông đỏ hoặc trắng**, giáo dài 삭 (~4 m), đao ngang lưng, cung treo yên |
| Shape | Ngựa Goguryeo tầm trung, dáng ngực rộng; giáp ngựa lamellar hình vảy chữ nhật sắt xỉn, viền da; kỵ sĩ dáng "khối sắt" |
| Color | Sắt xỉn xám đen, dây da nâu, chỏm lông **đỏ** (kỵ binh 해모루) hoặc trắng (vệ binh 을지문덕), áo lót 저고리 đỏ sẫm/nâu; cờ 삼족오 đen trên nền vàng cắm sau lưng vài kỵ sĩ dẫn đầu |
| Xuất hiện | 1화 (해모루 thu quân), 3화 (hành quân song song), 4화 (vệ binh 을지문덕), **5화 (lao từ hai bờ xuống sông — cảnh đại quy mô)** |
| Damage | 5화: giáp ngựa dính bùn, tên cắm vảy giáp, một số ngựa không giáp (đã mất) |

**VISUAL_LOCK_EN (≤60 từ):**
`Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a Goguryeo heavy cavalryman of 612 AD standing beside his horse, three-quarter view, the horse fully armored in dull dark iron lamellar barding from neck to rump with an iron face mask with eye holes and leather edging, the rider in full iron lamellar armor with arm and shin guards over a dark red long tunic, iron helmet with a red horsehair plume, holding a four-meter lance, sword at the waist, composite bow on the saddle, a small black three-legged crow pennant on a yellow field on his back, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## WPN_101 — 고구려 활과 쇠뇌 (cung 맥궁 & nỏ Goguryeo)

| Trường | Nội dung |
|---|---|
| Type | **맥궁**: cung composite phản khúc ngắn (~1 m) sừng-gỗ-gân, cánh cung cong ngược mạnh khi chưa căng; tên thân tre/liễu, đầu sắt hình lá liễu hoặc đầu **tam giác có ngạnh** (mũi tên cắm lốp 1화 = loại này), lông vũ xám 3 cánh; **쇠뇌 (nỏ)** trên tường thành: thân gỗ dài, lẫy đồng, cánh nỏ gỗ-sừng, tên nỏ ngắn nặng |
| Color | Gỗ nâu sẫm bọc vỏ cây anh đào, sừng đen, gân vàng nhạt, dây gai; đầu tên sắt xám |
| Xuất hiện | 1화 (tên cắm lốp — PROP_016; 해모루 bắn), 2화 (nỏ trên tường), 5화 |

**VISUAL_LOCK_EN:** `Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of Goguryeo archery equipment of 612 AD laid out together, a short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, strung, a leather quiver with a dozen arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, and a heavy wooden crossbow with a bronze trigger and short thick bolts, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## VEH_201 — 팔륜누차 (tháp công thành 8 bánh Tùy) — THẬT (隋書)

| Trường | Nội dung |
|---|---|
| Type | Tháp công thành di động **8 bánh gỗ** đặc, cao 3–4 tầng (~12–15 m, cao hơn tường 요동성), khung gỗ nặng, **mặt trước và hông bọc da trâu ướt** chống lửa, tầng trên có **cầu bập bênh** hạ xuống tường, tầng dưới lính đẩy + trâu kéo; cung thủ tầng 2–3 bắn qua lỗ; cờ Tùy đỏ trên đỉnh |
| Shape | Hình hộp thuôn lên trên, thang trong lòng, bánh gỗ đặc đường kính ~1.5 m |
| Color | Gỗ thô vàng nâu, da trâu nâu đen ướt, dây gai, cờ đỏ |
| Xuất hiện | **2화** (nhiều tháp — K2 và PZF phá; thử thách của 을지문덕: phá bằng ít đạn nhất) |
| Damage | 2화: 3–5 tháp cháy đổ, một tháp đổ nghiêng tựa vào tường thành, lính rơi |

**VISUAL_LOCK_EN (≤60 từ):**
`Sui dynasty eight-wheeled siege tower, tall four-story raw timber frame narrowing upward, front and sides covered in wet dark ox hide, drop-bridge at the top, arrow slits, eight solid wooden wheels, red Sui banner on top, pushed by hundreds of soldiers and oxen`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a Sui dynasty eight-wheeled siege tower of 612 AD, three-quarter front view, tall four-story raw timber frame narrowing upward with an internal ladder, front and sides covered in wet dark ox hides lashed with hemp rope, a hinged drop-bridge at the top, arrow slits on the upper floors, eight solid wooden wheels about one and a half meters tall, towing ropes and pushing beams at the base, a red Sui banner on top, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## VEH_202 — 충차 (xe phá cổng)

| Trường | Nội dung |
|---|---|
| Type | Xe phá cổng: **thân gỗ dài bịt đầu sắt** treo dây xích/thừng dưới **mái che gỗ hình mai rùa bọc da ướt**, 4–6 bánh gỗ, 30–40 lính đẩy bên trong |
| Color | Gỗ nâu, da đen ướt, đầu sắt xám |
| Xuất hiện | 2화 (nhắm 옹성 cổng nam — cối và K6 chặn) |

**VISUAL_LOCK_EN:** `Sui battering ram cart, long timber ram with iron head hung on chains under a low turtle-shell wooden roof covered in wet dark hide, six solid wooden wheels`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a Sui dynasty battering ram cart of 612 AD, three-quarter view, a long timber ram with a forged iron head hung on iron chains under a low turtle-shell-shaped wooden roof covered in wet dark ox hides, six solid wooden wheels, pushing bars along the sides, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## VEH_203 — 운제 (thang mây)

| Trường | Nội dung |
|---|---|
| Type | Xe thang: bệ gỗ 4 bánh, **thang gập 2 đoạn** có bản lề, đầu thang có **móc sắt** bám tường, có thể tựa lên tường cao 10 m; 10–15 lính đẩy |
| Color | Gỗ nâu, móc sắt |
| Xuất hiện | 2화 (hàng chục cái tựa tường — K3 và cung thủ Goguryeo bắn) |

**VISUAL_LOCK_EN:** `Sui cloud ladder: four-wheeled wooden cart base with a two-section hinged extending ladder, iron hooks at the top, hemp ropes`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a Sui dynasty cloud ladder siege cart of 612 AD, three-quarter view, a heavy four-wheeled wooden cart base carrying a two-section hinged extending ladder raised halfway, iron hooks at the top rung, hemp ropes and pulleys, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## VEH_204 — 수나라 누선 (thuyền chiến Tùy của 내호아)

| Trường | Nội dung |
|---|---|
| Type | **누선 (lâu thuyền)**: thuyền chiến nhiều tầng, thân gỗ dài ~40 m, **2–3 tầng lầu gỗ** có lan can, buồm vải nâu vuông, dãy mái chèo hai bên, mũi thuyền chạm đầu thú, cờ đỏ-vàng; thuyền đổ bộ nhỏ (bè, thuyền phẳng) đi kèm |
| Color | Gỗ nâu đỏ sơn, lầu sơn son bạc màu, buồm nâu, cờ đỏ |
| Xuất hiện | **4화** (hạm đội trên Đại Đồng giang, đổ bộ 4 vạn; sau phục kích: thuyền cháy trên sông) |

**VISUAL_LOCK_EN (≤60 từ):**
`Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a Sui dynasty tower warship of 612 AD, three-quarter bow view, long dark red-brown wooden hull about forty meters, two stories of wooden deckhouses with red railings and a small tower at the stern, square brown cloth sail furled, rows of oars on both sides, carved beast head at the prow, red and yellow silk banners with black tassels, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## VEH_205 — 요하 부교 (cầu phao sông Liêu) — THẬT

| Trường | Nội dung |
|---|---|
| Type | Cầu phao Tùy (우문개 thiết kế, 하조 nối dài — thật): **thuyền gỗ đáy phẳng** dài ~8 m neo cạnh nhau bằng dây gai + xích, **ván gỗ ghép** mặt cầu rộng ~4 m, cọc neo hai bờ; 3 cầu; dài 400–600 m |
| Color | Gỗ thô vàng xám, dây gai, nước nâu |
| Xuất hiện | 1화 (drone thấy — xem LOC_001), 3화 ken-burns |

**VISUAL_LOCK_EN:** `Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river`

**REF_PROMPT_EN (phông trắng, 16:9 — đoạn cầu):** `Product-style reference photo of a twenty-meter section of a Sui dynasty pontoon bridge of 612 AD, three-quarter view, flat-bottomed wooden boats about eight meters long moored side by side with thick hemp rope and iron chain, a plank deck four meters wide laid across them, wooden mooring stakes and a red banner at one end, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## VEH_206 — 선비 기병 (kỵ binh Tiên Ti của 탁발흠)

| Trường | Nội dung |
|---|---|
| Type | Kỵ binh nhẹ thảo nguyên: **ngựa thảo nguyên lùn, bờm dày, đuôi dài, không giáp ngựa**; kỵ sĩ **giáp da lamellar nâu** (vảy da sơn đen) hoặc áo da dài, **mũ da viền lông cáo/sói**, quần da, ủng mềm, **cung composite** + ống tên bên hông, đao cong ngắn, **thòng lọng**; đội của 탁발흠 ~200–300 kỵ |
| Shape | Nhỏ gọn, nhanh, dáng cúi thấp trên yên; cờ đuôi ngựa (툭) đen trên cán thay cờ vải |
| Color | Da nâu, lông xám, ngựa hung/xám/đen; 탁발흠 có **áo choàng da sói xám** (nhận diện) |
| Xuất hiện | 1화 (đuổi đoàn dân — trận đầu), 2화 (hỏa công đêm — tên lửa), 3화 (chiếm K21, phục ở khe núi), 4화 (săn bằng kính đêm), 5화 (đột kích bờ bắc) |
| Damage / thích nghi | 2화: mang **đuốc + tên lửa + bình dầu**; 3화: 1 kỵ sĩ **cầm drone** như chiến lợi phẩm; 4화: 탁발흠 **đội kính đêm** (EQP_001 lock enemy); 5화: giáp bùn, ngựa mất |

**VISUAL_LOCK_EN (≤60 từ):**
`Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a Xianbei steppe cavalryman of 612 AD standing beside his horse, three-quarter view, a short stocky steppe horse with thick mane and long tail and no armor, the rider in brown leather lamellar armor with black-painted scales over a long leather coat, fur-trimmed leather cap, soft leather boots, composite bow in a case at the hip with a quiver of arrows, short curved saber, coiled rope lasso on the saddle, a black horse-tail standard on a pole, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

## VEH_207 — 수 기병 / 수 장군 기마 (kỵ binh Tùy — ngựa Hán, giáp 명광개) · MỚI v3 (decisions "sau QC 5화", P-50 ep5)

| Trường | Nội dung |
|---|---|
| Type | **Kỵ binh chính quy nhà Tùy** và **ngựa của tướng lĩnh** — KHÁC VEH_206 (Tiên Ti: ngựa lùn thảo nguyên, giáp da, mũ lông) và KHÁC VEH_101 (개마무사 Goguryeo: ngựa bọc giáp sắt kín). Dùng cho 우중문 (CHAR_202), 우문술 (CHAR_203), 수 후군 장수 (신세웅 [史], EXTRA), 수 기병 sườn/hậu quân, kỵ sứ/전령 Tùy |
| Ngựa | **Ngựa chiến Hán cao hơn ngựa thảo nguyên** (vai ~1,45 m), cổ dài, bờm tỉa ngắn dựng; **yên gỗ cao mũi-hậu (yên cao), bàn đạp sắt**, dây cương da có **khóa đồng mạ vàng**, tua đỏ dưới hàm; **tấm phủ ngựa lụa đỏ viền vàng (giáp ngựa lụa — không phải giáp sắt)** cho ngựa tướng; ngựa lính: yếm da đơn giản, không phủ lụa |
| Kỵ sĩ (tướng) | Giáp **명광개** hai tấm gương ngực bóng, viền mạ vàng (우중문), hoặc giáp hai mảnh sơn đen không trang trí + cổ lông (우문술 — theo CHAR lock); **áo choàng đỏ** (우중문) / xám (우문술); mũ sắt tua đỏ; kiếm thẳng chuôi mạ; cờ đại quân cắm bên yên |
| Kỵ sĩ (lính) | Giáp lamellar sắt + mũ sắt chỏm nhọn có tua, giáo dài, đao thẳng, khiên tròn nhỏ; cờ đuôi nheo đỏ trên giáo của kỵ dẫn đầu |
| Màu | Ngựa: **우중문 ngựa đen** · **우문술 ngựa xám** · 신세웅/kỵ sứ ngựa hung; lụa đỏ, đồng vàng, sắt bóng; cờ đỏ-vàng |
| Xuất hiện | 1화 (kỵ sứ Tùy — ít) · 2화 (đài 양제, kỵ tuần) · 3화 (kỵ Tùy sườn P2, kỵ sứ đuổi 을지문덕 P4) · 4화 (hậu quân bờ nam) · **5화 (21 SC: SC_006/015/016/018/047/052/062–064/070/072/079/081/091/094/112/113/214/236/237/239)** |
| Damage / diễn biến 5화 | Ướt mưa, cổ lông bết (우문술 SC_015); nước lên bụng ngựa giữa khối (SC_062); 신세웅 ngã khỏi yên, mũ tua đỏ trôi (SC_091); **우중문 trên ngựa không yên bước hụt hố cát lở, ngã xuống nước, cán cờ gãy nổi lên** (SC_236) → bị bắt sống |
| Phân biệt cho QC ảnh | Có **lụa đỏ + đồng vàng + gương ngực** = Tùy (VEH_207) · lông thú + da nâu + ngựa lùn = Tiên Ti (VEH_206) · ngựa mặc giáp sắt kín + mặt nạ = Goguryeo (VEH_101). Tuyệt đối không đính `@sui_pontoon` (VEH_205) cho kỵ Tùy |

**VISUAL_LOCK_EN (≤60 từ):**
`Sui dynasty cavalry: tall Han war horses with trimmed upright manes, high-pommel wooden saddles with iron stirrups, red silk caparisons with gold borders on the generals' horses, riders in mingguang iron lamellar armor with polished round chest plates and pointed iron helmets with red tassels, long spears, red and yellow banners`

**REF_PROMPT_EN (3/4 view, phông trắng, 16:9):**
`Product-style reference photo of a Sui dynasty cavalry general of 612 AD mounted on a tall black Han war horse, three-quarter front-left view, the horse with a trimmed upright mane, high-pommel and high-cantle wooden saddle with iron stirrups, red silk caparison with a gold border and red tassels under the jaw, gilded bronze harness fittings, the rider in mingguang iron lamellar armor with two polished round chest plates and gilded edges, a red silk cloak, a pointed iron helmet with a red tassel crest, straight sword at the hip, holding a long spear with a small red pennant, beside him a dismounted Sui cavalryman in plain iron lamellar armor holding a grey horse with a simple leather breast strap and no silk, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## WPN_201 — 수나라 보병 무장 (bộ binh Tùy — để dựng đại quân)

| Trường | Nội dung |
|---|---|
| Type | Bộ binh Tùy: **giáp 명광개** (hai tấm tròn ngực bóng), mũ sắt chỏm nhọn, giáo dài, khiên gỗ chữ nhật sơn đỏ, đao thẳng; cung thủ áo bông xanh xám + mũ vải; kỵ binh chính quy giáp sắt + ngựa có yếm da |
| Color | Sắt bóng, khiên đỏ, cờ đỏ-vàng, áo lính xanh xám bẩn |
| Xuất hiện | Mọi tập (đại quân aerial wide) |

**VISUAL_LOCK_EN:** `Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners`

**REF_PROMPT_EN (phông trắng, 16:9):** `Product-style reference photo of a Sui dynasty infantryman of 612 AD, three-quarter view, mingguang armor with two polished round iron chest plates over lamellar, pointed iron helmet with neck guard, long spear, red rectangular wooden shield, straight sword at the waist, grey-blue padded coat beneath, leather boots, pure white background, even studio lighting, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

---

## PHỤ LỤC A — BẢNG TRẠNG THÁI KHÍ TÀI THEO TẬP (khớp resource_ledger.md)

| ID | 1화 | 2화 | 3화 | 4화 | 5화 |
|---|---|---|---|---|---|
| VEH_001 K2 | sạch/bụi vàng, giữ, dầu 400→370 | bắn 10 viên (22→12), sém 1 bên, dầu 300 | "400 딱" gom; 노새; miếng đồng vá; bắn 4 (→8); dầu ~20 | đảo lau, bắn 2 (→6), dầu 20 | 6 viên → 0; 300 m; nước tắt máy ở cổng họng; nhiệt nhôm; chìm bùn; biển "3" cạnh "1" |
| VEH_002 K21 ×3 | 3 sạch; 천둥 3 hỏng bánh → chốt sắt 을보 | **천둥 4 cháy**; dầu ≈ cạn | 천둥 2 PZF ×2 + dầu, **천둥 3 bị chiếm** (biển tên tháo) | 천둥 3 bò kéo về tây | 천둥 3 trong sân 육합성 15 ngày; 양제 chạm: "내년" |
| VEH_003 K511 ×2 | lốp thủng tên | mất 1 phuy | **bỏ lại, đốt** | — | — |
| VEH_004 K151 | "위성 0개" | kính nứt | **bỏ lại**, radio/máy phát lên K2 | — | — |
| UAV_001 ×4 | 4 → 3 | 3 → 2 | 2 → 1 → **0** | 0 | 0 (drone #4 về Lạc Dương) |
| EQP_001 ×12 | 12 | 12 | **10** (2 mất) | 탁발흠 đội | pin cạn |
| WPN_004 K6 ×2 | trên xe | trên xe | **tháo, khiêng** | giá 3 chân | mô cát |
| WPN_005 PZF ×18 quả | 18 | 12 | 10 | 6 | 0 |
| VEH_201 팔륜누차 | — | 3–5 tháp cháy | — | — | — |
| VEH_204 누선 | — | — | — | hạm đội + cháy | — |
| VEH_207 kỵ Tùy | kỵ sứ | đài 양제 | kỵ sườn, kỵ sứ | hậu quân bờ nam | 21 SC; 우중문 ngã ngựa bị bắt |

## PHỤ LỤC B — DANH SÁCH `@name` CHO G-LABS (khớp ref_jobs.json)
`K2_hero` (VEH_001) · `K2_ep5` · `K21_base` (천둥 2) · `K21_captured` (천둥 3) · `K21_burned` (천둥 4) · `K511_truck` · `K151_cmd` · `K2C1_rifle` · `KM187_mortar` · `K3_lmg` · `K6_hmg` · `PZF3` · `K4_agl` · `drone_quad` · `PVS11K_nvg` · `PRC999K_radio` · `goguryeo_cataphract` · `goguryeo_bow` · `sui_siege_tower` · `sui_ram` · `sui_ladder` · `sui_warship` · `sui_pontoon` · `xianbei_cavalry` · `sui_infantry` · **`sui_cavalry` (VEH_207, v3)**

## PHỤ LỤC C — ĐIỂM CẦN USER QUYẾT (TRẠNG THÁI v3 — decisions.md "sau world-designer": 1 → overlay ở edit, ảnh chỉ số Ả Rập · 2 → K6 cupola dùng chung kho 1.600 · 3 → giữ pin mặt trời, chỉ sạc AA, KHÔNG sạc drone · 4 → DUYỆT (thứ tự drone, ~60 viên trong 천둥 3) · 5 → giữ, QC loại plate armor phương Tây)
1. **Số hiệu "천둥 1" bằng Hangul trên xe**: tôi chọn chỉ vẽ số Ả Rập trắng (1/2/3/4) + 태극기 nhỏ, vì style tag "no text" và AI hay sai chữ Hàn; "천둥" chỉ tồn tại trong thoại. Nếu user muốn Hangul thật trên xe → phải làm post-production (overlay) hoặc chấp nhận tỉ lệ lỗi.
2. **K6 trên cupola K2**: foundation §5 chỉ có WPN_004 K6 ×2 (800 viên/khẩu). K2 thật có K6 gắn liền; tôi để nó là "súng của xe" và **không tính đạn** trong ledger (đề xuất: 1.000 viên 12.7 riêng, hoặc coi như dùng chung kho 12.7 với WPN_004). Cần chốt để script-writer không bắn "vô hạn".
3. **Tấm pin mặt trời gấp trên K151**: tôi thêm để hợp lý hóa sạc drone/kính đêm những ngày không nổ máy phát (tiết kiệm dầu) — nhưng nó cũng có thể làm "hậu cần" bớt căng. Nếu user thấy làm loãng engine LIMITED RESOURCES → bỏ, tôi sửa prompt.
4. **Thứ tự mất drone 3화** (hết pin rơi trước, rồi #4 bị bắt) và **천둥 3 còn ~60 viên 40 mm bên trong khi bị chiếm** là đề xuất của tôi (foundation chỉ nói "nguyên vẹn") — mở đường cho series 2 (Tùy có đạn nhưng không biết nạp). Chốt hay bỏ?
5. **Ngựa Goguryeo mặc giáp toàn thân ở 5화**: cảnh kỵ binh lao xuống sông với giáp ngựa lamellar rất "đắt" hình nhưng AI có thể vẽ thành kỵ sĩ châu Âu; tôi khóa mô tả theo bích họa 안악 3호분. QC cần loại ảnh có plate armor phương Tây.

---
## Cập nhật theo outline (2026-09-16)
- **VEH_002 천둥 3**: 1화 P10 hỏng bánh chịu nặng (road wheel) khi vượt rãnh → **을보 rèn chốt sắt tạm ngay 1화 P11** ("쇠는 쇠요", SC_2xx; P-36 — không phải 2화); là xe còn chạy được nhưng yếu → 3화 bị bỏ lại nguyên vẹn và rơi vào tay 탁발흠 (khớp foundation). Damage state 2화: bánh thứ 3 bên phải có chốt sắt thô, vệt dầu.
- **VEH_002 천둥 4**: cháy 2화 (hỏa công) — xác xe đen ở LOC_003.
- **PROP_023 biển tên "천둥 3"**: 박기철 tháo ở 3화 P1 trước khi bỏ xe (SC_004/011), mang trên ba lô 1 tháng, 5화 nhét túi ngực (SC_168) → **đặt lên mép tháp K2 cạnh số "1"** (SC_282).
- **v3 (sau 5 kịch bản):** VEH_207 kỵ Tùy thêm (Phần 2) · K2 giới hạn lội 1,2 m + APU (bảng VEH_001) · damage state K2 5화 tách 4 pha · 천둥 3 timeline: bờ bắc 압록 → gửi về tây D16 (200 kỵ) → sân 육합성 15 ngày · K4 (WPN_006) **không xuất hiện trong 5 kịch bản** → coi như bỏ lại/cháy cùng xe tải 3화 (ledger v3) · mọi khí tài ROK không còn ở kết: "영입니다. 전부 영."
