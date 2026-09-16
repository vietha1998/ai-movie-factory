# 살수 612 — 1화 「요하」 · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep1.md` v3 (291 SC · 40:00) · `continuity_master.json` (LOCKED) · character/location/vehicle/prop bible · template 04 §C–§H · decisions.md.
> Format §C. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit.
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (ví dụ `@CHAR_001_ref`, `@CHAR_006_facepaint_ep1`, `@LOC_002_detail`) — tag = đúng `name` trong `reference_images` để G-Labs bind chính xác (substring `@CHAR_001` vẫn khớp). VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json; derived state = câu trạng thái nguyên văn từ character_bible (ref biến thể ✔ đính thay ref gốc; state không có ref → đính ref gốc). Không tên riêng, không chữ trong ảnh; Hangul trên xe KHÔNG vẽ (decisions #1) — chỉ số Ả Rập; số/HUD/chữ trên màn hình & sổ tay = overlay ở edit.
> **Sub-lock địa điểm:** cảnh nội thất/cận dùng đoạn REF_PROMPT_EN_DETAIL/INTERIOR của bible (nguyên văn) thay vì lock wide; khu vực chưa có trong bible (thảo nguyên D1 + đường nhựa cắt, hõm cỏ D1, khe cạn, bến suối đêm, thảo nguyên dân chạy nạn 1화, đêm 철원 LOC_010) dùng sub-lock cố định trong `logs/scratch/veo-ep1/build.py` — DÙNG NGUYÊN VĂN mọi SC → đề xuất world-designer đưa vào location_bible (proposals).
> **Nhân vật phụ không ID** (소년 척후, 전군총관, 전령, 환관, lính Hàn, bộ binh/cung thủ Goguryeo, trinh sát Tiên Ti, dân chạy nạn): lock tạm cố định (build.py EXTRAS) — mặt lính Hàn phụ luôn quay đi/khuất mũ để né drift.
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói, 1 chuyển động camera. `CUT_HALF: yes` = hook 0–30 s + khối trận P4/P5/P10 → edit cắt 2 shot 4 s. Đại quân = aerial wide (⚑ AERIAL/QUALITY → dùng veo_31_quality cho video, nano_banana_pro + upscale 2K cho ảnh).
> **CHAIN_FROM:** chỉ khi SC trước là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (tools/glabs_client.py `--chain`). Không chain quá 3 clip liên tiếp (drift).
> **Ánh sáng theo bảng ngày/đêm (header script):** D0 đêm 철원 (SC_013–021) · D1 rạng sáng (022–034) → sáng (001–012) → trưa (035–060) → chiều (061–076) · D3 chiều (078–103) → hoàng hôn (104–129) → đêm (130–144) · D4 bình minh (145–152) → ngày (153–154) → đêm (155–253) · D5 bình minh–sáng (254–274) → tối (275–280) → đêm (281–290). Bụi vàng trên lính từ D3; 백성민 sơn mặt (facepaint_ep1) toàn tập trừ flashback.
> **Style tag (§D, cuối mọi image prompt):** `photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`
> **Negative (§E, ghi 1 lần — glabs-operator dán vào field negative nếu model hỗ trợ):** `cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, modern buildings in historical scene, anachronistic clothing`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.


**Tổng:** 291 SC · 237 video8s · 54 still_kenburns · 2400 s · chain_from: 37 · cut_half: 85 · aerial/quality: 36

---


## [Phần 1] 콜드 오픈 — 「있을 수 없는 아침」 (0:00–1:30) · hook, không narrator 0–30 s

### SC_001 | 0:00–0:08 | LOC_003 (LOC_003_steppe) | — | VEH_003 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Extreme close-up, static camera with a very slow push-in
IMAGE_PROMPT: Extreme close-up, static camera with a very slow push-in. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: The front right tire of a parked six-wheeled military cargo truck fills the frame; a single Goguryeo arrow is buried to half its shaft in the thick lugged rubber, grey three-vane fletching trembling in the wind, dry yellow grass behind the wheel, the truck's canvas cover flapping slightly at the top of frame, no people. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–3 s): frame held on pure black, only wind. Beat B (3–8 s): cut to the arrow in the tire, static camera pushing in very slowly toward the arrow shaft, fletching trembling in gusts, grass bending behind; no people enter. Sound: constant steppe wind, dry grass rustling, canvas slapping softly, no music.
ACTION_START: black frame → arrow in tire, fletching still
ACTION_END: tight on arrow shaft, fletching trembling, grass bending behind
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: gió liên tục, cỏ khô cọ vào nhau, bạt xe đập nhẹ. Không nhạc.
CONTINUITY: Mở tập. Xe chưa phủ lưới. Lốp trước phải K511 #2 (script). Mũi tên này = PROP_015 xuyên suốt (SC_061 rút ra, SC_065 trả).
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_003_ref, PROP_015_ref, LOC_003_steppe_d1
AI_RISK: cận vật thể + lông vũ → tĩnh, 1 vật thể, không tay người trong khung (né deformed hands)

### SC_002 | 0:08–0:16 | LOC_003 (LOC_003_steppe) | CHAR_003 | VEH_003 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Close-up, low angle at wheel height, static then slow tilt up
IMAGE_PROMPT: Close-up, low angle at wheel height, static then slow tilt up. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: A black mechanic-gloved hand smeared with oil enters from the left and closes around the arrow shaft buried in the truck's front tire, testing it; the stocky sergeant in a patrol cap crouches beside the wheel, his broad round face unsmiling, salt-and-pepper temples visible under the cap brim, eyes on the arrow. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera static at wheel height: the gloved hand grips the arrow shaft and rocks it once — it does not move — then the fingers stroke the grey fletching; camera tilts slowly up to the sergeant's face, patrol cap, salt-and-pepper temples, no smile; he speaks one short line. Sound: wind, faint rubber creak when the arrow is rocked, one line of Korean dialogue.
ACTION_START: gloved hand reaching for arrow, face out of frame
ACTION_END: tilted up on sergeant's unsmiling face, hand still on arrow
NARRATION_KO: 
DIALOGUE_KO: 박기철: 타이어에… 화살입니다.
SOUND: gió; tiếng cao su kêu khẽ khi lắc tên.
CONTINUITY: Kế SC_001: cùng lốp, cùng mũi tên. 박기철 găng dính dầu (state 1화). Chưa có bụi vàng (D1).
CHAIN_FROM: SC_001
CUT_HALF: yes
REFS: CHAR_003_ref, VEH_003_ref, PROP_015_ref, LOC_003_steppe_d1
AI_RISK: tay cận cầm vật thể → 1 bàn tay, chuyển động chậm, găng đen che chi tiết ngón

### SC_003 | 0:16–0:24 | LOC_003 (LOC_003_steppe) | CHAR_001 | VEH_004 | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Medium-wide, low angle, static (keyframe = beat B)
IMAGE_PROMPT: Medium-wide, low angle, static (keyframe = beat B). @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: The captain stands on the flat roof of the boxy 4x4 command vehicle, binoculars lowered to his chest, looking out at a horizon of nothing but flat yellow grass under a pale grey sky, no power lines, no mountains, the lensatic compass on its cord swinging slightly at his chest, wind flattening the grass around the vehicle. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): insert — combat boots step through dry yellow grass at ankle height, camera whips up to the small Korean flag patch on a right shoulder fluttering in wind. Beat B (4–8 s): low-angle medium-wide, the captain on the vehicle roof lowers binoculars to chest height and stares at the empty yellow horizon; compass on the cord sways; wind gusts. Sound: dry grass under boots, strengthening wind, binoculars tapping body armor, no music.
ACTION_START: boots in grass (insert) / captain raising binoculars
ACTION_END: captain standing still on roof, binoculars at chest, looking at horizon
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: cỏ khô dưới giày; gió mạnh hơn, ống nhòm chạm áo giáp.
CONTINUITY: Xe K151 chưa lưới. La bàn trên cổ (identifier). Vệt bụi chưa xuất hiện. Beat (a) = insert tách riêng ở edit nếu veo tạo 1 clip.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_ref, VEH_004_ref, PROP_006_ref, LOC_003_steppe_d1
AI_RISK: 2 beat trong 1 clip → nếu veo không cắt được, glabs-operator tạo 2 clip 4 s (insert giày + captain) và edit ghép
INSERT_CLIP (4 s, tách riêng): Beat A insert, 4 s: low camera at ankle height, combat boots in granite-pattern digital camo trousers step through dry knee-high yellow grass, then a fast tilt-pan up the uniform to a small full-color Korean Taegukgi flag patch on the right shoulder fluttering in wind, no face; cold grey overcast morning, wind. Sound: dry grass under boots, wind.

### SC_004 | 0:24–0:32 | LOC_003 (LOC_003_steppe) | CHAR_002, CHAR_005 | VEH_004 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Interior medium close-up from the passenger side, static
IMAGE_PROMPT: Interior medium close-up from the passenger side, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: Inside the cramped cab of the 4x4 command vehicle: the tall lieutenant in the front seat, sleeves rolled, goggles pushed up on his helmet, jabs a thick finger at a dashboard navigation screen that shows only an empty dark map with a crossed-out satellite icon and no readable text; behind him in the rear seat the boyish private with the drone controller on his chest harness looks from the screen to the lieutenant. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static interior shot: the lieutenant taps the dark navigation screen once, twice, then hits it hard with his fingertips; camera holds; the private in the back leans forward, looks at the screen, then up at the lieutenant and says one line. Sound: plastic taps, the vehicle's ventilation fan humming, one line of Korean dialogue. Screen stays dark — no numbers appear.
ACTION_START: lieutenant's finger touching screen, private looking at screen
ACTION_END: private looking up at lieutenant, lieutenant's hand flat on screen
NARRATION_KO: 
DIALOGUE_KO: 장태오: 위성 0개입니다. 하나도 안 잡힙니다.
SOUND: tiếng gõ nhựa, quạt máy K151 ro ro.
CONTINUITY: Cùng K151 của SC_003 (한승우 trên nóc). Màn hình tối, KHÔNG vẽ chữ '위성 0/0' — overlay ở edit.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, CHAR_005_ref, VEH_004_ref, LOC_003_steppe_d1
AI_RISK: chữ trên màn hình → prompt 'empty dark map, crossed-out satellite icon, no readable text'; số 0/0 overlay edit

### SC_005 | 0:32–0:40 | LOC_003 (LOC_003_steppe) | ROK_SOLDIER | VEH_002 | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Over-the-shoulder from behind a sentry on the roof of an IFV, static
IMAGE_PROMPT: Over-the-shoulder from behind a sentry on the roof of an IFV, static. ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: From behind the helmeted shoulders of a sentry standing on the roof of a K21 IFV (white numeral 2 on the turret), binoculars pressed to his eyes, left hand raised flat in a halt signal; beyond him the flat yellow steppe runs to a pale grey horizon, a faint smudge of dust far to the right. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera static behind the sentry: he holds binoculars to his eyes, then slowly raises his left hand in a flat halt signal and keeps it up; wind tugs his sleeve; far right on the horizon a faint dust smudge drifts. He calls one line without turning. Sound: wind, binocular focus ring clicking, one line of Korean dialogue.
ACTION_START: sentry with binoculars up, hand down
ACTION_END: sentry frozen, left hand raised, binoculars up, dust smudge on horizon
NARRATION_KO: 
DIALOGUE_KO: 초병: 11시 방향… 사람입니다.
SOUND: gió; tiếng ống nhòm chỉnh nét.
CONTINUITY: Lính gác không mặt (từ sau lưng). K21 천둥 2 chưa lưới. Vệt bụi = kỵ Goguryeo thu quân (không thấy cờ).
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_002_ref, PROP_006_ref, LOC_003_steppe_d1
AI_RISK: mặt lính phụ → máy sau lưng, mũ che

### SC_006 | 0:40–0:48 | LOC_001 (LOC_001_north_steppe) | — | — | PROPS: — | TYPE: video8s | 8s
SHOT: Very high aerial wide, static, no zoom  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Very high aerial wide, static, no zoom. Setting @LOC_001_wide: Open yellow steppe north of the Goguryeo fortress, dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, low grassy rises, cold pale grey sky, early spring, no trees. Action: From very high above: the gently rolling yellow steppe stretches to every horizon under a cold pale grey sky; about three kilometers away toward the lower right a long thin line of yellow dust rises along a moving column of tiny dark specks — horsemen too distant to show any banner or armor — moving across the grass; no vehicles in frame, no trees, no buildings. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera locked high above the steppe, absolutely static: the distant dust line creeps slowly across the lower right of the frame, the specks beneath it barely resolving as riders, cloud shadows drift across the grass. No zoom, no tilt. Sound: high-altitude wind, the faintest far-off drumming of hooves under the wind.
ACTION_START: dust column at lower right, riders as specks
ACTION_END: dust column advanced slightly right, still unresolved
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: gió trên cao, xa xa tiếng vó ngựa mơ hồ.
CONTINUITY: '기병 미상' — KHÔNG đính ref Tiên Ti hay Goguryeo; chỉ chấm đen dưới bụi. Hướng đông-nam.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_001_wide
AI_RISK: đám đông kỵ binh → aerial rất cao, chấm đen dưới bụi, không chi tiết

### SC_007 | 0:48–0:54 | LOC_004 (LOC_004_parade) | — | WPN_201 | PROPS: PROP_017, PROP_021 | TYPE: still_kenburns | 6s
SHOT: Still for ken-burns: wide low-angle from beside a great war drum, pulling out to the whole parade ground  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide low-angle from beside a great war drum, pulling out to the whole parade ground. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_017_ref: Goguryeo war drum one meter across, faded red lacquered wooden body with bronze studs and hide heads on an X-shaped wooden stand; Sui war drum larger, bright red with gold patterns in a red lacquered frame. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_004_wide: A vast packed-earth parade ground at dawn, 612 AD: tens of thousands of Sui infantry in mingguang armor with polished round chest plates standing in square blocks to the horizon, huge red-lacquered war drums with gold patterns on wooden frames either side of a red-lacquered timber reviewing platform, red and yellow silk banners with black tassels, low bright sun through dust haze. Action: Hard cut to blinding early light: beside a huge bright red Sui war drum with gold patterns in its red lacquered frame, a sea of Sui infantry in mingguang armor with polished round chest plates stands in perfect square blocks to the horizon, tens of thousands of pointed iron helmets catching the sun, tall red and yellow banners, dust haze; a red-lacquered timber reviewing platform in the middle distance; no faces distinct, no modern objects. Light: Bright early morning sun cutting through dust haze, hard highlights on polished armor, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (6 s): start tight on the red war drum, slow pull-out to reveal the armored blocks to the horizon. Sound: one heavy Sui drum stroke, its reverberation rolling out.
ACTION_START: tight on drum
ACTION_END: full parade ground revealed
NARRATION_KO: 612년 정월. 탁군. 오늘날의 베이징 근처입니다.
DIALOGUE_KO: 
SOUND: một hồi trống Tùy nặng, vang.
CONTINUITY: HARD CUT lịch sử. Palette đối lập: nắng chói vs thảo nguyên xám. Không mặt lính nào rõ.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_017_ref, PROP_021_ref, LOC_004_wide
AI_RISK: đám đông lính cận → khối ô vuông từ xa, mũ sắt lấp lánh, không mặt

### SC_008 | 0:54–1:00 | LOC_004 (LOC_004_parade) | SUI_EUNUCH_READER | WPN_201 | PROPS: PROP_013 | TYPE: still_kenburns | 6s
SHOT: Still for ken-burns: close-up on an open silk scroll held in two hands, shallow focus, sea of armor blurred behind
IMAGE_PROMPT: Still for ken-burns: close-up on an open silk scroll held in two hands, shallow focus, sea of armor blurred behind. Sui court official in a dark blue silk robe and black gauze cap with side wings, holding an open pale yellow silk scroll with columns of black brush calligraphy. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_004_wide: A vast packed-earth parade ground at dawn, 612 AD: tens of thousands of Sui infantry in mingguang armor with polished round chest plates standing in square blocks to the horizon, huge red-lacquered war drums with gold patterns on wooden frames either side of a red-lacquered timber reviewing platform, red and yellow silk banners with black tassels, low bright sun through dust haze. Action: Two hands in dark blue silk sleeves hold open a pale yellow silk edict scroll on a black lacquered rod; columns of black brush calligraphy run down the silk, deliberately soft and unreadable, a large square red seal impression at the end; behind and far out of focus, a blur of silver armor and red banners under bright sun. Light: Bright morning sun, silk glowing warm, background blown to soft silver. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (6 s): slow vertical drift down the columns of calligraphy, background blur unchanged. Sound: a distant droning voice reading, the drum silent.
ACTION_START: top of scroll
ACTION_END: red seal at bottom of scroll
NARRATION_KO: 수 양제가 조서를 읽습니다. 전투 병력 113만 3천 8백. 세상은 이백만이라 불렀습니다.
DIALOGUE_KO: 
SOUND: giọng đọc chiếu xa, ù, trống ngừng.
CONTINUITY: Chữ = brush calligraphy mờ (decisions #6). Ấn son đỏ vuông. Không mặt người đọc.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_013_ref, LOC_004_wide
AI_RISK: chữ trong ảnh → 'soft unreadable brush calligraphy', shallow focus; không vẽ chữ Hán thật

### SC_009 | 1:00–1:06 | LOC_001 (LOC_001_march) | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 6s
SHOT: Still for ken-burns: high aerial wide along a great road, sliding sideways along a line of army banners  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial wide along a great road, sliding sideways along a line of army banners. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_wide: A wide beaten dirt road across the flat North China plain in early spring 612 AD, dry knee-high yellow grass to the horizon bending under constant wind, drifting yellow dust, cold pale grey overcast sky, no trees, no buildings. Action: A broad beaten road runs across the flat yellow plain to the horizon; along it, twenty-four separate army columns march in sequence, each under its own cluster of tall red and yellow silk banners with black tassels, each raising its own block of yellow dust, the columns receding smaller and smaller into the haze; no faces, no modern objects. Light: Pale morning sun through dust haze, silver sky, long low shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (6 s): slow lateral slide along the line of banners from foreground column toward the horizon. Sound: layered drums and horns from many armies far apart, overlapping out of step.
ACTION_START: foreground column and banners
ACTION_END: distant columns fading into haze
NARRATION_KO: 24군이 하루에 한 군씩, 40리 간격으로 떠납니다. 다 떠나는 데 사십 일이 걸립니다. 길 위의 군대만으로 나라 하나 크기였습니다.
DIALOGUE_KO: 
SOUND: trống và kèn xa, nhiều lớp chồng nhau.
CONTINUITY: 24군 = 24 cụm cờ + 24 khối bụi. Aerial, không cận.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_001_wide
AI_RISK: đại quân → aerial, khối bụi thay người

### SC_010 | 1:06–1:14 | LOC_004 (LOC_004_parade) | CHAR_201 | — | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Low-angle medium close-up, slow push-in
IMAGE_PROMPT: Low-angle medium close-up, slow push-in. @CHAR_201_ref: Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_004_wide: A vast packed-earth parade ground at dawn, 612 AD: tens of thousands of Sui infantry in mingguang armor with polished round chest plates standing in square blocks to the horizon, huge red-lacquered war drums with gold patterns on wooden frames either side of a red-lacquered timber reviewing platform, red and yellow silk banners with black tassels, low bright sun through dust haze. Action: The Sui emperor stands alone at the front edge of a red-lacquered timber reviewing platform, spotless in gilded ceremonial armor over an ochre-yellow dragon robe, tall black crown with gold beams, thin goatee; he does not look down at the army — his half-lidded eyes are fixed on the eastern horizon; yellow silk banners with red tassels frame him, dust haze and blurred silver armor far below. Light: Bright morning sun from the side, gold armor gleaming, dust haze behind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in from low angle on the emperor's face: banner tassels stir in the wind, dust drifts; he never blinks, never looks down; his jaw tightens once. Sound: wind snapping silk tassels, very distant drums.
ACTION_START: emperor full figure on platform edge, eyes east
ACTION_END: tight on the emperor's face, still looking east
NARRATION_KO: 목표는 하나. 고구려였습니다. 황제는 직접 요동으로 갈 것이었습니다.
DIALOGUE_KO: 
SOUND: gió lay tua cờ; trống nền rất xa.
CONTINUITY: CHAR_201 base lock (giáp mạ vàng — ban ngày). Sạch tuyệt đối. Không xuất hiện lại cho tới P12 (robe_only).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_201_ref, PROP_021_ref, LOC_004_wide
AI_RISK: chân dung lịch sử → không giống người thật (bible); nét mặt hư cấu theo lock

### SC_011 | 1:14–1:22 | LOC_003 (LOC_003_steppe) | CHAR_001, CHAR_003 | VEH_004, VEH_003 | PROPS: PROP_006, PROP_015 | TYPE: video8s | 8s
SHOT: Medium two-shot, slight low angle, static
IMAGE_PROMPT: Medium two-shot, slight low angle, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: Hard cut back to grey steppe: the captain, standing on the roof of the 4x4 command vehicle, lowers his binoculars and looks down at the stocky sergeant standing beside the cargo truck's arrow-pierced front tire; the two men hold each other's eyes for a beat; the captain's right hand moves to the radio handset clipped on his left shoulder strap. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the captain lowers the binoculars, looks down; the sergeant looks up; a one-beat pause; the captain turns his head toward the handset on his shoulder and presses it, speaking one short order. Sound: wind, the click of the push-to-talk, one line of Korean dialogue.
ACTION_START: captain with binoculars up on roof, sergeant by tire looking up
ACTION_END: captain's hand on shoulder handset, mouth open on the order
NARRATION_KO: 하늘에 위성은 없었습니다. 땅 위에는 화살이 있었습니다.
DIALOGUE_KO: 한승우: 전 차량, 위장망. 지금.
SOUND: gió; tiếng bấm PTT.
CONTINUITY: Kế SC_003/SC_002: cùng vị trí xe. HARD CUT từ Tùy. Lệnh phủ lưới → SC_012.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_003_ref, VEH_004_ref, VEH_003_ref, PROP_006_ref, PROP_015_ref, LOC_003_steppe_d1
AI_RISK: 2 nhân vật + xe → mặt hai người rõ, khoảng cách xa, không đám đông

### SC_012 | 1:22–1:30 | LOC_003 (LOC_003_steppe) | ROK_SOLDIERS | VEH_001, VEH_002, VEH_003, VEH_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from a low rise, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide from a low rise, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: From a low grassy rise: the small convoy sits in a sea of yellow grass — the K2 tank, three K21 IFVs, two cargo trucks and the 4x4 command vehicle — and tiny figures of soldiers drag green-brown camouflage netting up over the tank and the IFVs, nets billowing in the wind; on the far south-eastern horizon a thin dust line still crawls across the sky; the stub of asphalt road is a dark streak beside the vehicles. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera static on the rise: soldiers haul the netting over the tank and IFVs, the nets bellying in the gusts and settling; the distant dust line moves slowly along the horizon. Sound: rustling nets, faint shouted commands carried on the wind, steppe wind, no music.
ACTION_START: nets half raised over vehicles, dust line on horizon
ACTION_END: nets settling over tank and IFVs, soldiers stepping back
NARRATION_KO: 그 조서는 두 달 전의 일이었습니다. 그 113만이 향하는 길 위에, 94명의 대한민국 군인이 서 있었습니다.
DIALOGUE_KO: 
SOUND: lưới ngụy trang sột soạt, lệnh nhỏ, gió.
CONTINUITY: Kết P1: xe bắt đầu phủ lưới (từ đây LOC_003_hollow có lưới). Vệt bụi đông-nam. 7 xe: K2 + 3 K21 + 2 K511 + K151.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_002_ref, VEH_003_ref, VEH_004_ref, LOC_003_steppe_d1
AI_RISK: nhiều lính nhỏ + 7 xe → wide xa, lính chỉ là bóng nhỏ, không mặt


## [Phần 2] 발견 — 「여기가 어디인가」 (1:30–4:30) · flashback 철원 + phát hiện

### SC_013 | 1:30–1:38 | LOC_010 | ROK_SOLDIERS | VEH_001, VEH_002, VEH_003, VEH_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot alongside a moving convoy, low angle, single lateral move
IMAGE_PROMPT: Tracking shot alongside a moving convoy, low angle, single lateral move. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: Cold blue-grey winter night on a frozen dirt road between pine hills: the K2 tank leads with its numeral 1 visible on the turret, followed by three K21 IFVs, two cargo trucks and the 4x4 command vehicle bringing up the rear, headlights cutting through the fogging breath of soldiers riding on top, frost on the ruts, exhaust steaming; no title card, no text. Light: Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera tracks laterally alongside the moving convoy at low angle, headlights sweeping across frost and pine trunks, engines hauling, treads biting the frozen road, breath fogging from soldiers on the hulls; one continuous lateral move. Sound: heavy diesel engines, tracks grinding ice, winter night wind.
ACTION_START: tank nose entering frame from left, headlights on
ACTION_END: command vehicle passing, convoy continuing right
NARRATION_KO: 그 전날 밤. 철원, 겨울 훈련장이었습니다. 여단 훈련 사흘째, 실탄은 제한 수량이었습니다. 기계화보병중대 하나에 전차 한 대가 붙은 편성이었습니다.
DIALOGUE_KO: 
SOUND: động cơ diesel nặng, xích nghiến băng, gió đêm.
CONTINUITY: FLASHBACK — không title card, chỉ ánh sáng xanh xám lạnh. Xe sạch, không bụi vàng, không lưới. Không cột điện trong khung (P-27).
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_002_ref, VEH_003_ref, VEH_004_ref, LOC_010_wide
AI_RISK: 7 xe chuyển động + đêm → tracking 1 chiều, đèn pha che chi tiết, không mặt lính

### SC_014 | 1:38–1:46 | LOC_010 | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on hands then tilt up to face, hooded red flashlight, static
IMAGE_PROMPT: Close-up on hands then tilt up to face, hooded red flashlight, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: At the rear deck of the K2 tank at night, a hooded flashlight throwing a small red pool of light: the stocky sergeant in a patrol cap pulls a long dipstick from the tank's engine deck, reads the mark, wipes the rod with the red shop rag from his belt and pencils a number into a small green-covered notebook, brow furrowed, breath fogging. Light: Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up under red flashlight: the dipstick slides out, the sergeant tilts it to read, wipes it with the red rag, then camera tilts up as he writes in the notebook and grumbles one line, breath fogging in the red light. Sound: metal on metal, pencil scratching paper, idling engine, one line of Korean dialogue.
ACTION_START: hands pulling dipstick from engine deck
ACTION_END: sergeant's face, pencil on notebook, mouth closing on the line
NARRATION_KO: 훈련은 사흘. 연료는 그 사흘을 위한 것이었습니다. 박기철은 숫자를 두 번 말하는 버릇이 있었습니다.
DIALOGUE_KO: 박기철: 연료, 한 통입니다. 딱 한 통.
SOUND: kim loại chạm, bút chì trên giấy, động cơ nền.
CONTINUITY: Flashback. Giẻ đỏ ở thắt lưng (identifier). Sổ bìa xanh = prop lặp lại toàn tập (SC_035, 121, 145, 260). Số trong sổ không vẽ chữ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_010_wide
AI_RISK: tay cận + sổ chữ → sổ chỉ 'pencil marks', không chữ đọc được

### SC_015 | 1:46–1:54 | LOC_010 | CHAR_005 | VEH_004, UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Low-angle medium shot, static
IMAGE_PROMPT: Low-angle medium shot, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: Behind the parked 4x4 command vehicle at night, the boyish private stands with the drone controller on his chest harness glowing cold blue-white on his face; a small graphite-grey quadcopter with orange-tipped propellers lifts off his open palm and hangs a meter above his head, its gimbal camera rotating, tiny red and green LEDs; four spare batteries in a pouch on his body armor, breath fogging. Light: Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the quadcopter rises off the private's palm, hovers just above his head with its gimbal camera turning, LEDs blinking, while his face stays lit blue by the controller screen; he looks up, then down at the screen and reports one line. Sound: drone rotors whining, controller beeps, one line of Korean dialogue.
ACTION_START: drone resting on open palm, private looking at it
ACTION_END: drone hovering above head, private looking at controller screen
NARRATION_KO: 장태오 일병, 스물한 살. 중대에서 가장 어린 병사였습니다. 드론 넷과 배터리 여덟 개가 그의 재산이었습니다.
DIALOGUE_KO: 장태오: 1호기 이상 무. 배터리 백 퍼센트입니다.
SOUND: tiếng rotor drone vo ve, bíp controller.
CONTINUITY: Flashback. Drone #1 nguyên vẹn (sẽ rơi SC_098). 4 pin dán số (số chỉ chấm nhỏ, không vẽ chữ).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, VEH_004_ref, UAV_001_ref, LOC_010_wide
AI_RISK: drone nhỏ lơ lửng + tay → 1 vật, chuyển động chậm

### SC_016 | 1:54–2:02 | LOC_010 | CHAR_004 | VEH_003 | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Static close-up on hands and face inside a red-lit truck bed
IMAGE_PROMPT: Static close-up on hands and face inside a red-lit truck bed. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: Inside the canvas-covered cargo bed of a military truck under a dim red lamp: the young female medic, red cross armband on her left arm, kneels over her open olive medic bag and lines up small white plastic medicine bottles in a row on the lid of an ammunition can, counting with a fingertip and writing in a small notebook, face calm and focused in the red light. Light: Night interior, dim red lamp inside a canvas truck bed, deep shadows. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: her gloved fingertip taps each bottle in the row in turn, she writes in the notebook, then looks up at the row again and speaks one line quietly. Sound: plastic caps clicking, faint hum of the red lamp, one line of Korean dialogue.
ACTION_START: hands setting last bottle in row
ACTION_END: medic looking at the row, pen down, line spoken
NARRATION_KO: 윤서아 하사, 의무병. 이 가방 하나가 아흔네 명의 병원이었습니다.
DIALOGUE_KO: 윤서아: 항생제 스무 개, 모르핀 서른 개. 이상 없습니다.
SOUND: nắp nhựa lách cách, đèn đỏ ù nhẹ.
CONTINUITY: Flashback. Băng chữ thập đỏ tay trái + nốt ruồi mắt trái (identifier). Túi quân y đầy (20 lọ). Không chữ trên lọ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_ref, VEH_003_ref, PROP_009_ref, LOC_010_wide
AI_RISK: nhãn lọ có chữ → 'plain white plastic bottles, no labels'

### SC_017 | 2:02–2:10 | LOC_010 | CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Low medium close-up, static
IMAGE_PROMPT: Low medium close-up, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: At the edge of a dark pine wood at night the wiry staff sergeant in a boonie hat kneels on one knee, a red-filtered flashlight in his left hand lighting a deer's hoofprint in the frozen ground, the fingertips of his right hand touching the rim of the print; the scar splitting his left eyebrow is visible as he lifts his eyes toward the black trees. Light: Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: his fingertips brush the edge of the hoofprint in the red light, he lifts his head slowly and looks into the dark pines, listening; a branch snaps far away; he says one line without looking back. Sound: forest silence, one distant branch crack, one line of Korean dialogue.
ACTION_START: kneeling, fingertips on hoofprint, eyes down
ACTION_END: kneeling, head raised, eyes on dark forest
NARRATION_KO: 백성민 중사, 강원도 산골 사냥꾼의 아들. 땅을 읽는 사람이었습니다. 그는 하루 전 발자국과 한 시간 전 발자국을 구별했습니다.
DIALOGUE_KO: 백성민: 고라니. 한 시간 전.
SOUND: im lặng rừng, cành gãy xa.
CONTINUITY: Flashback — CHAR_006 base (KHÔNG sơn mặt; facepaint từ SC_023). Mũ boonie, khăn ngụy trang.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_ref, LOC_010_wide

### SC_018 | 2:10–2:18 | LOC_010 | CHAR_002 | VEH_004 | PROPS: PROP_002 | TYPE: video8s | 8s
SHOT: Medium shot, static, slight low angle
IMAGE_PROMPT: Medium shot, static, slight low angle. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @PROP_002_ref: rugged black rubber-armored military tablet with a diagonal crack across the upper right of its ten-inch screen, screen showing an empty dark digital map with a crossed-out satellite icon, hand strap on the back. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: The tall muscular lieutenant leans against the open door of the 4x4 command vehicle at night, a rugged black military tablet in one hand, reading, a one-sided smirk on his face; his sleeves are rolled to the elbow despite the winter cold, tactical goggles pushed up on his helmet, breath fogging; the tablet screen shows only a soft glow with no readable text. Light: Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium shot: he scrolls the tablet with a thumb, snorts, the smirk widens; he glances up toward the convoy and delivers one line with a shrug. Sound: tablet beep, wind, one line of Korean dialogue.
ACTION_START: leaning on door, reading tablet, smirk forming
ACTION_END: looking up from tablet, line delivered, smirk
NARRATION_KO: 오태민 중위, 부중대장. 화력이 답이라고 믿는 사람이었습니다. 그날 밤까지는 농담이었습니다. 훈련 시나리오는 늘 과장되어 있었습니다.
DIALOGUE_KO: 오태민: 가정, 적 삼십만 남하… 반나절이면 끝납니다.
SOUND: tablet bíp, gió.
CONTINUITY: Flashback. Tay áo xắn, kính bảo hộ trên mũ (identifier). Tablet chưa nứt (PROP_002 nứt từ 2화 — ở đây chỉ 'rugged black tablet' không vết nứt). Không chữ trên màn hình.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, VEH_004_ref, PROP_002_ref, LOC_010_wide
AI_RISK: chữ tablet → 'soft glow, no readable text'

### SC_019 | 2:18–2:26 | LOC_010 | CHAR_001 | VEH_004, EQP_002 | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: High-angle close-up over the map then tilt to face, static
IMAGE_PROMPT: High-angle close-up over the map then tilt to face, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: The captain spreads a folded military paper map across the hood of the 4x4 command vehicle at night under a hooded red flashlight, brown contour lines and a black grid, red and blue grease-pencil marks; his gloved index finger stops on a bend of a river; his other hand reaches for the radio handset on his left shoulder strap, the lensatic compass on its cord resting on the map. Light: Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static high angle: the finger traces the river and stops at the bend; the captain presses the shoulder handset and gives one short order, breath fogging red; camera tilts up slightly to his calm face. Sound: paper map crackling, push-to-talk click, one line of Korean dialogue.
ACTION_START: finger moving along river on map
ACTION_END: finger stopped on bend, handset pressed, captain's face
NARRATION_KO: 한승우 대위, 중대장. 아흔네 명의 목숨을 맡은 사람이었습니다.
DIALOGUE_KO: 한승우: 전 소대, 여기는 천둥 지휘. 한탄강 여울 확보 후 대기한다.
SOUND: giấy bản đồ, tiếng PTT.
CONTINUITY: Flashback. Bản đồ Cheorwon = PROP_001 (sạch, chưa vẽ than mặt sau). La bàn trên dây (identifier).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, PROP_001_ref, LOC_010_wide
AI_RISK: chữ trên bản đồ → chỉ đường đồng mức + lưới, không địa danh đọc được

### SC_020 | 2:26–2:34 | LOC_010 | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Extreme close-up of the compass on the captain's chest, static, then a lightning flash
IMAGE_PROMPT: Extreme close-up of the compass on the captain's chest, static, then a lightning flash. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: Dry lightning tears across the black sky above the pine hills without rain; in a sharp white flash the lensatic compass hanging on its cord against the captain's granite-camo body armor fills the frame, its needle spinning wildly under the glass; his chin and closed lips are visible at the top of frame as he looks down at it in silence. Light: Winter night, cold blue-grey darkness cut by dry lightning without rain, sharp white flashes, breath fogging. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Extreme close-up: a white lightning flash strobes the frame, the compass needle spins and spins under the glass, the captain's chin tilts down into frame as he watches; no rain falls, no thunder follows on time. Sound: rising electrostatic hiss, hair-raising crackle, no thunder.
ACTION_START: compass hanging still, dark
ACTION_END: needle spinning, lightning flash, captain looking down
NARRATION_KO: 비는 없었습니다. 나침반은 십 초 동안 돌았습니다. 그 십 초를 설명할 사람은 이후에도 없었습니다.
DIALOGUE_KO: 
SOUND: tiếng rít tĩnh điện tăng dần, tóc gáy, không sấm.
CONTINUITY: Flashback — sét khô. La bàn quay loạn (bùa của 한승우). Nối SC_021 (màn hình nhiễu, đèn tắt).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_010_wide
AI_RISK: kim la bàn quay → chuyển động nhỏ trong vật nhỏ; nếu veo không làm được, chấp nhận flash + rung kim

### SC_021 | 2:34–2:42 | LOC_010 | CHAR_005, CHAR_002 | VEH_004, VEH_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium-wide from behind the command vehicle toward the convoy, static, fading to black
IMAGE_PROMPT: Medium-wide from behind the command vehicle toward the convoy, static, fading to black. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_010_wide: A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights. Action: At night behind the 4x4 command vehicle: every screen inside the cab and the drone controller on the boyish private's chest burst into white static, lighting the private and the tall lieutenant beside him in flickering grey; ahead, the headlights of the K2 tank and the convoy behind it go out one after another as if blown out, leaving only pine silhouettes against a black sky. Light: Winter night, cold blue-grey darkness cut by dry lightning without rain, sharp white flashes, breath fogging. Modern soldiers' uniforms clean and crisp, cold-weather breath fogging. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the screens flare white with static on the two soldiers' faces, the private shouts one line; ahead the tank's headlights die, then the next vehicle's, then the next, until the frame sinks into total black for the final two seconds. Sound: electrostatic hiss climbing to a peak, then absolute silence.
ACTION_START: screens flaring white static, headlights on
ACTION_END: total black frame
NARRATION_KO: 그것이 철원의 마지막 밤이었습니다. 다음 아침은 다른 세기의 아침이었습니다.
DIALOGUE_KO: 장태오: 화면이 전부… 나갔습니다!
SOUND: rít tĩnh điện đạt đỉnh → cắt im tuyệt đối.
CONTINUITY: Kết flashback → đen 2 s → SC_022 mở ra bình minh. 2 nhân vật, 1 người nói.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, CHAR_002_ref, VEH_004_ref, VEH_001_ref, LOC_010_wide
AI_RISK: nhiều đèn tắt lần lượt → chuỗi đơn giản, máy tĩnh

### SC_022 | 2:42–2:48 | LOC_003 (LOC_003_steppe) | — | VEH_001, VEH_002 | PROPS: — | TYPE: still_kenburns | 6s
SHOT: Still for ken-burns: wide, from black opening onto silver dawn, very slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide, from black opening onto silver dawn, very slow pull-out. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: Silver-grey dawn: the convoy stands motionless on a fifty-meter stub of asphalt in a sea of dry yellow grass that runs to every horizon, the K2 tank and three K21 IFVs bare with no camouflage netting, dew beading on their armor, thin mist on the grass, no mountains, no trees, no power lines, no people visible. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (6 s): fade up from black onto the still convoy, then a very slow pull-out widening the emptiness around it. Sound: cold wind, one field bird calling.
ACTION_START: black → convoy on asphalt stub in mist
ACTION_END: wider, convoy small in endless grass
NARRATION_KO: 아침이었습니다. 아무 소리도 나지 않았습니다. 차 소리도, 비행기 소리도. 오직 바람이었습니다. 군인들은 그 침묵을 먼저 들었습니다.
DIALOGUE_KO: 
SOUND: gió lạnh, một con chim đồng kêu.
CONTINUITY: TRƯỚC P1 (chưa lưới, chưa tên trong lốp phát hiện). Sương bám giáp xe. Đường nhựa cắt = mốc LOC_003_steppe.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_002_ref, LOC_003_steppe_d1

### SC_023 | 2:48–2:56 | LOC_003 (LOC_003_steppe) | CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: POV walking forward at eye height, slow, stopping at the road's edge
IMAGE_PROMPT: POV walking forward at eye height, slow, stopping at the road's edge. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: Point of view of the staff sergeant on morning watch: the asphalt road runs straight ahead fifty meters under his boots and then ends in a clean knife-straight edge, beyond which dry knee-high yellow grass bends away in the wind to a grey horizon; the toes of his combat boots are visible at the bottom of frame at the very edge of the cut asphalt. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow forward walking POV along the asphalt, boots entering the bottom of frame with each step, stopping exactly at the clean cut edge; grass bends beyond; the frame holds, he does not step over. Sound: boots on asphalt, then silence at the edge, wind.
ACTION_START: POV walking on asphalt toward the cut
ACTION_END: POV stopped at the cut edge, grass beyond
NARRATION_KO: 도로는 오십 미터 앞에서 끝났습니다. 그 너머는 다른 땅이었습니다. 백성민은 그 선을 넘지 않았습니다. 아직은.
DIALOGUE_KO: 
SOUND: giày trên nhựa → im khi tới mép; gió.
CONTINUITY: POV → CHAR_006 chỉ có giày trong khung (ref để giữ giày/đồ). Mép nhựa cắt gọn = hình ảnh chủ đạo P2.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, LOC_003_steppe_d1
AI_RISK: mép nhựa quá thẳng có thể AI vẽ như vỉa hè → 'clean knife-straight edge, no curb, no kerb stone'

### SC_024 | 2:56–3:04 | LOC_003 (LOC_003_steppe) | CHAR_006 | EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Low-angle medium close-up, static
IMAGE_PROMPT: Low-angle medium close-up, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: The staff sergeant in a boonie hat stands at the cut edge of the asphalt looking straight up into an enormous empty grey sky with not a single contrail; he glances at the black watch on his wrist, looks up again, then presses the radio handset clipped on his shoulder without any change in expression. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: he tilts his head back to scan the empty sky, checks his wristwatch, looks up once more, then presses the shoulder handset and reports one flat line. Sound: wind, push-to-talk click, one line of Korean dialogue.
ACTION_START: looking up at empty sky
ACTION_END: handset pressed at shoulder, eyes still on sky
NARRATION_KO: 백성민은 하늘을 먼저 보았습니다. 비행운이 없는 하늘은 처음이었습니다. 그가 아는 하늘에는 언제나 무언가 날고 있었습니다.
DIALOGUE_KO: 백성민: 중대장님. 도로가… 끊겨 있습니다.
SOUND: gió; tiếng PTT.
CONTINUITY: Kế SC_023 (cùng vị trí mép đường). Sơn mặt 2 vệt (facepaint_ep1) từ đây.
CHAIN_FROM: SC_023
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, EQP_002_ref, LOC_003_steppe_d1

### SC_025 | 3:04–3:12 | LOC_003 (LOC_003_steppe) | CHAR_001 | VEH_004, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Interior close-up from the driver's side, static
IMAGE_PROMPT: Interior close-up from the driver's side, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: The captain sits in the front passenger seat of the 4x4 command vehicle, the vehicle radio's coiled-cord handset pressed to his ear, eyes on the small dark LCD panel of the olive backpack radio showing nothing but a faint channel glow; morning light through the windshield, compass on its cord against his body armor. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static interior: he presses the handset, speaks one call, releases — and only white hiss answers; he keeps the handset at his ear a beat longer, staring at the dead panel. Sound: one line of Korean dialogue, then long radio white noise.
ACTION_START: handset to ear, about to transmit
ACTION_END: handset still at ear, hiss, eyes on panel
NARRATION_KO: 여단 지휘소는 십 킬로 밖에 있어야 했습니다. 응답은 없었습니다. 기계는 멀쩡했습니다. 없는 것은 상대편이었습니다.
DIALOGUE_KO: 한승우: 여단 지휘소, 여기는 천둥 지휘. 감명도?
SOUND: rít trắng radio kéo dài sau câu nói.
CONTINUITY: Trong K151. Không chữ trên LCD.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, LOC_003_steppe_d1
AI_RISK: LCD chữ → 'faint channel glow, no readable text'

### SC_026 | 3:12–3:20 | LOC_003 (LOC_003_steppe) | CHAR_001, ROK_RADIOMAN | VEH_004, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Interior two-shot from the rear of the cab, static
IMAGE_PROMPT: Interior two-shot from the rear of the cab, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. young ROK Army radio operator in granite-pattern digital camo uniform, matching body armor, covered ballistic helmet, headset over the helmet, Korean flag patch on right shoulder, face partly hidden by the handset. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: Inside the 4x4 command vehicle: in the rear seat a young radio operator with a headset over his helmet turns the channel knob of the olive backpack radio click after click and shakes his head, face half hidden by the handset; in the front seat the captain sets the handset down slowly and looks out through the windshield at the yellow grass. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the operator clicks through channels, shaking his head, and says one line; the captain lowers the handset slowly into its cradle and turns his gaze out to the grass beyond the glass. Sound: knob clicking, white noise, wind outside, one line of Korean dialogue.
ACTION_START: operator turning knob, captain with handset up
ACTION_END: captain's handset down, eyes out windshield
NARRATION_KO: 무전은 중대 안에서만 들렸습니다. 세상이 십 킬로로 줄어든 것이었습니다.
DIALOGUE_KO: 무전병: 중대 내부만 됩니다. 십 킬로 밖은 아무것도 없습니다.
SOUND: núm xoay lách cách, rít trắng, gió ngoài xe.
CONTINUITY: Kế SC_025 cùng xe. 무전병 = extra không mặt rõ (handset che).
CHAIN_FROM: SC_025
CUT_HALF: no
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, LOC_003_steppe_d1
AI_RISK: mặt lính phụ → handset che mặt

### SC_027 | 3:20–3:30 | LOC_001 (LOC_001_march) | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide along a marching column, slow push  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: medium-wide along a marching column, slow push. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_wide: A wide beaten dirt road across the flat North China plain in early spring 612 AD, dry knee-high yellow grass to the horizon bending under constant wind, drifting yellow dust, cold pale grey overcast sky, no trees, no buildings. Action: A Sui infantry column marches along a wide beaten dirt road across the yellow plain — pointed iron helmets, mingguang armor with polished round chest plates, red rectangular wooden shields on their backs, long spears — yellow dust rolling up around their legs, red and yellow banners all leaning the same way in the wind, the column stretching away into haze; faces lost in dust and helmet shadow. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push along the column toward the receding banners. Sound: the tread of tens of thousands of feet, a marching drum keeping time.
ACTION_START: column mid-frame, near soldiers large
ACTION_END: pushed toward distant banners in haze
NARRATION_KO: 같은 봄. 수나라 24군이 차례로 요하로 향했습니다. 한 군이 떠나면 다음 군이 하루 뒤에 떠났습니다. 좌군 열둘, 우군 열둘이었습니다. 황제가 요동에 닿기까지 두 달이 걸렸습니다.
DIALOGUE_KO: 
SOUND: bước chân hàng vạn người, trống nhịp hành quân.
CONTINUITY: Ken-burns sử. Không mặt lính rõ (bụi che).
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_001_wide
AI_RISK: đám đông lính → bụi che chân/mặt, hàng dài xa dần

### SC_028 | 3:30–3:40 | LOC_001 (LOC_001_canal) | SUI_LABORERS | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide lateral slide, high vantage  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide lateral slide, high vantage. Sui conscript laborers in undyed hemp jackets and head cloths hauling two-wheeled wooden supply carts loaded with grain sacks under cloth covers. Setting @LOC_001_wide: A straight man-made canal cutting across the flat yellow plain in early spring 612 AD, packed with flat-bottomed wooden grain barges under cloth covers, a towpath beside it, dry yellow grass, drifting yellow dust, cold pale grey overcast sky. Action: An endless line of conscript laborers in undyed hemp hauls two-wheeled wooden grain carts along a towpath, bent under the ropes; behind them a straight canal is jammed bank to bank with flat wooden barges under cloth covers, oar-poles bristling; yellow dust over everything, grey sky; no faces distinct. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow lateral slide along the cart line and the barge-choked canal. Sound: wooden wheels, ragged breathing, a whip crack.
ACTION_START: carts foreground, canal behind
ACTION_END: slid along to more carts and barges
NARRATION_KO: 군량을 나르는 민부가 병사의 두 배였습니다. 운하는 곡식 배로 막혔습니다. 병사와 민부를 합치면 삼백만이 넘었습니다. 이 원정은 싸우기 전에 먼저 먹어 치웠습니다.
DIALOGUE_KO: 
SOUND: bánh xe gỗ, tiếng thở, roi.
CONTINUITY: Ken-burns sử (hậu cần). Không mặt rõ.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_001_wide
AI_RISK: đám đông dân phu → high vantage, bụi, không mặt

### SC_029 | 3:40–3:50 | LOC_001 (LOC_001_march) | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: very high aerial, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: very high aerial, slow pull-out. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_wide: A wide beaten dirt road across the flat North China plain in early spring 612 AD, dry knee-high yellow grass to the horizon bending under constant wind, drifting yellow dust, cold pale grey overcast sky, no trees, no buildings. Action: From very high above: a single ribbon of red and yellow banners and yellow dust runs from the bottom of the frame straight to the far horizon with no visible end, the marching army beneath it reduced to a dark thread on the yellow plain, a silver sun behind thin cloud. Light: Pale silver sun behind thin cloud, high haze, flat shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): very slow pull-out, the ribbon of banners never ending. Sound: drums of many armies overlapping out of rhythm, wind.
ACTION_START: ribbon of banners from foreground to horizon
ACTION_END: pulled out, ribbon thinner, still endless
NARRATION_KO: 깃발은 960리에 이어졌습니다. 앞뒤 군의 북소리가 서로 들렸습니다. 이런 규모의 원정은 그 전에도, 그 후에도 없었습니다. 그리고 그 끝은 아무도 보지 못했습니다.
DIALOGUE_KO: 
SOUND: trống của nhiều quân đoàn chồng nhau, lệch nhịp.
CONTINUITY: '960리' — không thấy điểm cuối. Aerial thuần.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_001_wide

### SC_030 | 3:50–3:58 | LOC_003 (LOC_003_steppe) | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on a hand, slow push-in tilting up to the face
IMAGE_PROMPT: Close-up on a hand, slow push-in tilting up to the face. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: Hard cut: the captain kneels on one knee just past the cut edge of the asphalt, his gloved hand closed around a fistful of dry earth and yellow grass stalks; he squeezes, the earth trickles out between his fingers, and he looks out at the horizon, compass on its cord swinging, face unreadable. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in on the gloved fist: dry earth and grass crumble out between the fingers; camera drifts up to the captain's still face looking at the horizon; he says nothing. Sound: wind, dry earth falling, no music.
ACTION_START: fist closed on earth, eyes down
ACTION_END: hand open and empty, eyes on horizon
NARRATION_KO: 이 풀은 철원의 풀이 아니었습니다. 그는 그것만은 알았습니다. 나머지는 알 필요가 없다고 정했습니다. 그것이 그가 지휘하는 방식이었습니다.
DIALOGUE_KO: 
SOUND: gió, đất khô rơi.
CONTINUITY: HARD CUT về từ sử. Mép nhựa ở tiền cảnh. 한승우 quỳ 1 gối.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_003_steppe_d1
AI_RISK: tay cận → 1 bàn tay đeo găng, đất rơi

### SC_031 | 3:58–4:06 | LOC_003 (LOC_003_steppe) | CHAR_002, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot from behind and to the side, static
IMAGE_PROMPT: Medium two-shot from behind and to the side, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: The tall lieutenant walks up behind the kneeling captain at the road's edge and stops, looking out at the same yellow horizon, goggles on his helmet, sleeves rolled; the captain does not turn — he rises to his feet and brushes the dust from his gloves, his back to the lieutenant. Light: Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the lieutenant steps in behind the captain and halts, looks at the horizon, and speaks one quiet line; the captain rises without turning, claps the dust off his gloves once, and stands facing the grass. Sound: boots on dry grass, wind, one line of Korean dialogue.
ACTION_START: lieutenant arriving behind kneeling captain
ACTION_END: captain standing, back to lieutenant, brushing gloves
NARRATION_KO: 누군가는 먼저 말해야 했습니다. 한승우는 대답하지 않았습니다. 말하면 사실이 되기 때문이었습니다.
DIALOGUE_KO: 오태민: 중대장님, 여기… 철원이 아닙니다.
SOUND: giày trên cỏ khô, gió.
CONTINUITY: Kế SC_030 (cùng chỗ). 오태민 lần đầu nói nhỏ.
CHAIN_FROM: SC_030
CUT_HALF: no
REFS: CHAR_002_ref, CHAR_001_ref, LOC_003_steppe_d1

### SC_032 | 4:06–4:14 | LOC_003 (LOC_003_steppe) | — | VEH_001, VEH_002, VEH_003, VEH_004 | PROPS: — | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: extreme high aerial, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: extreme high aerial, slow pull-out. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: From extreme height: the convoy under green-brown camouflage netting is a tiny dark smudge on an endless carpet of yellow grass, the fifty-meter stub of asphalt lying beside it like a strip of tape dropped on a rug, no other feature to any horizon. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow pull-out until the convoy is almost lost in the yellow. Sound: high wind only.
ACTION_START: convoy and asphalt stub small at center
ACTION_END: pulled out, convoy nearly invisible
NARRATION_KO: 아무도 그 말을 입에 올리지 않았습니다. 대신, 땅을 읽었습니다. 군인은 이유보다 위치를 먼저 묻습니다. 위치는 곧 알게 될 것이었습니다.
DIALOGUE_KO: 
SOUND: gió trên cao.
CONTINUITY: Lưới đã phủ (sau P1 SC_012 theo thứ tự thời gian D1 sáng). Aerial.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_002_ref, VEH_003_ref, VEH_004_ref, LOC_003_steppe_d1

### SC_033 | 4:14–4:22 | LOC_003 (LOC_003_steppe) | CHAR_006, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Low tracking shot following two men, then static as they crouch
IMAGE_PROMPT: Low tracking shot following two men, then static as they crouch. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: The staff sergeant in a boonie hat walks bent forward along a line of marks in the hard earth beside the grass verge, the captain following two steps behind; the sergeant stops, drops into a squat and points one finger at the ground without a word; the captain crouches down beside him. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Low camera follows the two men along the track line, then holds as the sergeant squats and points at the ground; the captain crouches beside him; neither speaks. Sound: dry grass, wind, two men breathing.
ACTION_START: two men walking, sergeant leading, bent forward
ACTION_END: both crouched, sergeant's finger pointing at ground
NARRATION_KO: 그날 아침 백성민이 읽은 것은 발자국이었습니다. 말 스무 필. 두 시간 전. 발자국은 걷지 않고 달렸습니다. 급한 자의 것이었습니다.
DIALOGUE_KO: 
SOUND: cỏ khô, gió, hai người thở.
CONTINUITY: Vết móng ngựa (20 con) trên đất cứng. Dẫn vào SC_034 cận.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, CHAR_001_ref, LOC_003_steppe_d1

### SC_034 | 4:22–4:30 | LOC_003 (LOC_003_steppe) | CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Macro close-up on the ground, static, then tilt up to face
IMAGE_PROMPT: Macro close-up on the ground, static, then tilt up to face. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Setting @LOC_003_steppe_d1: Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it. Action: A horse's hoofprint pressed deep into hard dried mud: a natural rounded hoof shape with no iron rim and no nail holes; the staff sergeant's bare hand rests flat beside it for scale; camera-facing, his painted face with the scarred eyebrow looks up from the print. Light: Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static macro on the unshod hoofprint with the hand beside it for a long beat, then a slow tilt up to the sergeant's painted face as he looks up and says one line. Sound: wind, silence, one line of Korean dialogue.
ACTION_START: hoofprint with hand beside it
ACTION_END: sergeant's face looking up, line spoken
NARRATION_KO: 
DIALOGUE_KO: 백성민: 말발굽 자국인데… 편자가 없습니다.
SOUND: gió, im.
CONTINUITY: Open loop P2: '편자가 없습니다'. Kế SC_033. Tay trần (không găng) để thấy tỷ lệ.
CHAIN_FROM: SC_033
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, LOC_003_steppe_d1
AI_RISK: tay cận → bàn tay phẳng, không cầm gì


## [Phần 3] 재고 조사 (4:30–7:00) · kiểm kê, drone thấy cầu phao · MID-ROLL 1 @7:00

### SC_035 | 4:30–4:38 | LOC_003 (LOC_003_hollow) | CHAR_003, ROK_SOLDIERS | VEH_001, VEH_002, VEH_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Static wide from the front of the formation, sergeant in the foreground
IMAGE_PROMPT: Static wide from the front of the formation, sergeant in the foreground. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: In a shallow grassy hollow the vehicles stand in a line under green-brown camouflage netting — the K2 tank, three K21 IFVs and two cargo trucks, one truck with a punctured tire lashed on its bed; in front of them a rank of helmeted soldiers stands at ease seen mostly from behind and in profile; nearest the camera the stocky sergeant in a patrol cap holds an open green-covered notebook and reads aloud without raising his head. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the sergeant reads from the notebook without looking up, one line; wind rattles the netting over the vehicles; the rank of soldiers stands still, a few heads turning slightly. Sound: wind through camouflage netting, a page turning, one line of Korean dialogue.
ACTION_START: sergeant opening notebook, rank at ease
ACTION_END: sergeant reading, eyes on page
NARRATION_KO: 아흔네 명. 그 숫자가 이 이야기의 시작이었습니다. 다섯 달 뒤까지 매일 다시 세어질 숫자였습니다.
DIALOGUE_KO: 박기철: 현재 인원 아흔네 명. 전원 이상 없습니다.
SOUND: gió lùa qua lưới, giấy lật.
CONTINUITY: Từ đây xe dưới lưới (LOC_003_hollow). Lốp thủng buộc trên thùng K511 #2. Hàng lính = sau lưng/profile, không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, VEH_002_ref, VEH_003_ref, LOC_003_hollow_d1
AI_RISK: hàng lính đứng → nhìn từ sau/profile, chỉ 박기철 rõ mặt

### SC_036 | 4:38–4:46 | LOC_003 (LOC_003_hollow) | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, static, slight low angle
IMAGE_PROMPT: Medium close-up, static, slight low angle. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The stocky sergeant turns his body and points the pencil at the K2 tank's turret under the camouflage netting behind him, then taps the pencil on his open notebook; his broad round face shows no emotion, salt-and-pepper temples under the patrol cap. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the pencil points back at the tank turret, returns to tap the notebook page, and he says one line to camera-left without expression. Sound: wind, pencil tapping the notebook cover, one line of Korean dialogue.
ACTION_START: pencil pointing at turret
ACTION_END: pencil on notebook, face to camera-left
NARRATION_KO: 훈련 적재량이었습니다. 실전용이 아니었습니다. 실전이라면 두 배를 실었을 것입니다.
DIALOGUE_KO: 박기철: 포탄 스물두 발. 그게 전부입니다.
SOUND: gió, bút gõ lên bìa sổ.
CONTINUITY: Kế SC_035. Không chữ đọc được trong sổ.
CHAIN_FROM: SC_035
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_003_hollow_d1

### SC_037 | 4:46–4:56 | LOC_003 (LOC_003_hollow) | — | WPN_002, WPN_005, UAV_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: top-down close-up of an open notebook page, shallow focus, slow vertical drift
IMAGE_PROMPT: Still for ken-burns: top-down close-up of an open notebook page, shallow focus, slow vertical drift. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. @WPN_005_ref: Panzerfaust 3 shoulder-fired anti-tank launcher, long dark olive tube with a large black conical warhead protruding from the front, detachable sight and trigger unit on the left side, shoulder rest. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Top-down: an open green-covered field notebook lies on the lid of an olive ammunition can, its page covered in soft pencil columns of figures and short strokes rendered as blurred handwriting with no readable characters; beside the notebook, out of focus, the olive tube of an 81mm mortar bomb in its green plastic case, the black conical warhead of a Panzerfaust and one folded grey quadcopter drone; a gloved thumb holds the page flat. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow vertical drift down the page from top to bottom. Sound: faint wind, paper.
ACTION_START: top of page
ACTION_END: bottom of page, objects beside
NARRATION_KO: 40밀리 600발. 박격포탄 120발. 판처파우스트 18발. 드론 넷, 한 대에 30분. 여기서 하나도 늘지 않을 숫자들이었습니다. 박기철은 이 페이지를 매일 밤 다시 썼습니다.
DIALOGUE_KO: 
SOUND: gió nhỏ, giấy.
CONTINUITY: Chữ số Ả Rập thật (40mm ×3, 박격포, PZF, 드론) overlay ở edit. Ảnh chỉ 'blurred pencil columns'.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_002_ref, WPN_005_ref, UAV_001_ref, LOC_003_hollow_d1
AI_RISK: chữ/số trong ảnh → blurred pencil, không ký tự; số thật overlay edit

### SC_038 | 4:56–5:06 | LOC_003 (LOC_003_hollow) | — | VEH_001, VEH_003 | PROPS: PROP_007, PROP_008 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide, slow push-in on two fuel drums
IMAGE_PROMPT: Still for ken-burns: medium-wide, slow push-in on two fuel drums. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_007_ref: dark olive 200-liter steel fuel drum with two raised ribs, twin screw caps, a small red triangle painted on the side, dents, strapped with rope, a hand pump and a green 20-liter jerrycan beside it. @PROP_008_ref: olive-green steel ammunition cans with hinged latched lids and carry handles, a wooden crate of 81mm mortar bombs in green plastic tubes, and a single one-meter 120mm tank round with a copper-brown semi-combustible case and black projectile. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Two dark olive 200-liter steel fuel drums with a small red triangle on the side stand behind a low sandbag wall, a hand pump and a green jerrycan beside them; behind, the K2 tank under camouflage netting and the open bed of a cargo truck stacked with olive ammunition cans; cold grey light, no people. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push-in on the two drums. Sound: wind, truck canvas slapping.
ACTION_START: drums, tank and truck behind
ACTION_END: tight on the two drums and red triangle
NARRATION_KO: 연료는 전차 한 통과 드럼 두 개. 물 이틀. 항생제 한 가방. 전차 한 통은 사백 킬로였습니다. 그 사백 킬로가 이 부대의 수명이었습니다.
DIALOGUE_KO: 
SOUND: gió, bạt xe đập.
CONTINUITY: 2 phuy + 'tam giác đỏ' = hình ảnh lặp lại (SC_247, 251 — 탁발흠 nhìn thấy). Phuy cách xe 30 m sau bao cát.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_003_ref, PROP_007_ref, PROP_008_ref, LOC_003_hollow_d1

### SC_039 | 5:06–5:14 | LOC_003 (LOC_003_hollow) | CHAR_003, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The stocky sergeant snaps the green notebook shut and pushes it into his chest pocket, looks straight ahead at the unseen rank of soldiers, then turns his head to the captain standing at his side with hands clasped behind his back; camouflage netting and yellow grass behind them. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the notebook closes, goes into the chest pocket; the sergeant looks forward, then to the captain, and says one line; the captain does not react. Sound: notebook snapping shut, wind, one line of Korean dialogue.
ACTION_START: notebook closing
ACTION_END: sergeant turned to captain, line spoken
NARRATION_KO: 그것이 이 부대의 전 재산이었습니다. 박기철은 숫자 앞에 형용사를 붙이지 않았습니다.
DIALOGUE_KO: 박기철: 식량 사흘, 물 이틀. 들어오는 건 없습니다.
SOUND: sổ gập, gió.
CONTINUITY: Kế SC_036 vị trí. 한승우 tay chắp sau lưng (tư thế identifier).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_001_ref, LOC_003_hollow_d1

### SC_040 | 5:14–5:22 | LOC_003 (LOC_003_hollow) | CHAR_001, CHAR_002, CHAR_003, CHAR_006 | VEH_004 | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Wide four-shot around the vehicle hood, slight high angle, static
IMAGE_PROMPT: Wide four-shot around the vehicle hood, slight high angle, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Four men stand around the hood of the 4x4 command vehicle where a useless folded paper map lies spread, one corner lifting in the wind: the captain with hands clasped behind his back gazing to the south-east where the morning dust has gone, the tall lieutenant with rolled sleeves, the stocky sergeant in a patrol cap, and the staff sergeant in a boonie hat with painted face; camouflage netting over the vehicle behind. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the map corner flaps in the wind; the captain stares south-east for a beat, then turns his head slowly to the west and speaks one line; the other three look at him. Sound: map flapping, wind, one line of Korean dialogue.
ACTION_START: captain looking south-east, others at map
ACTION_END: captain's head turned west, others looking at him
NARRATION_KO: 머무르면 안전했습니다. 사흘 동안만. 움직이면 위험했습니다. 하지만 알 수 있었습니다.
DIALOGUE_KO: 한승우: 선택은 둘이다. 여기 있거나, 움직이거나.
SOUND: bản đồ phần phật, gió.
CONTINUITY: 4 nhân vật chính lần đầu chung khung (chỉ 1 nói). Bản đồ vô dụng trên mui. Vệt bụi đã tan.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_002_ref, CHAR_003_ref, CHAR_006_facepaint_ep1, VEH_004_ref, PROP_001_ref, LOC_003_hollow_d1
AI_RISK: 4 mặt trong 1 khung → wide, mỗi người 1 dấu hiệu (la bàn / kính bảo hộ / mũ lưỡi trai / boonie)

### SC_041 | 5:22–5:30 | LOC_003 (LOC_003_hollow) | CHAR_002, CHAR_003 | VEH_004 | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Medium two-shot across the vehicle hood, static
IMAGE_PROMPT: Medium two-shot across the vehicle hood, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The tall lieutenant slaps his palm down on the hood of the 4x4 command vehicle beside the spread paper map and thrusts his other arm out pointing west; beside him the stocky sergeant in a patrol cap shakes his head very slightly, eyes never leaving the map. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the palm hits the sheet metal, the arm shoots out pointing west, one loud line; the sergeant's head shakes once, barely, eyes on the map. Sound: hand slapping metal, wind, one line of Korean dialogue.
ACTION_START: lieutenant's hand raised over hood
ACTION_END: arm pointing west, sergeant's slight head shake
NARRATION_KO: 오태민은 먼지 쪽을 가리켰습니다. 그에게 모르는 것은 곧 적이었습니다. 모르는 것과 싸울 수는 없었습니다.
DIALOGUE_KO: 오태민: 움직입니다. 먼지 난 쪽으로 밀고 갑니다.
SOUND: tay đập tôn xe, gió.
CONTINUITY: Kế SC_040 (cùng mui K151). Đối lập 오태민 (đánh) / 박기철 (dầu).
CHAIN_FROM: SC_040
CUT_HALF: no
REFS: CHAR_002_ref, CHAR_003_ref, VEH_004_ref, PROP_001_ref, LOC_003_hollow_d1

### SC_042 | 5:30–5:38 | LOC_003 (LOC_003_hollow) | CHAR_001, CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium two-shot, slight low angle, static
IMAGE_PROMPT: Medium two-shot, slight low angle, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The captain turns from the vehicle hood toward the boyish private standing a few steps away hugging a hard drone case against his chest, controller on his harness; the captain's eyes give the order before his mouth does, and the private straightens to attention under the camouflage netting. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the captain turns, locks eyes with the private; the private snaps straight; the captain gives one short order; the private's hands go to the case latches. Sound: wind, drone case latches clicking open, one line of Korean dialogue.
ACTION_START: captain turning, private hugging case
ACTION_END: private at attention, hands on case latches
NARRATION_KO: 먼지는 동남쪽으로, 발자국은 서쪽에서 왔습니다. 한승우는 발자국이 온 곳을 먼저 보았습니다. 사람 대신 드론이었습니다.
DIALOGUE_KO: 한승우: 장 일병. 1호기, 서쪽. 낮게 말고 높게.
SOUND: gió, hộp drone mở khóa.
CONTINUITY: Drone #1 (sẽ rơi SC_098). Pin dán số: chỉ chấm nhỏ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_005_ref, UAV_001_ref, LOC_003_hollow_d1

### SC_043 | 5:38–5:46 | LOC_003 (LOC_003_hollow) | CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Low angle looking up through camouflage netting, static
IMAGE_PROMPT: Low angle looking up through camouflage netting, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: From the ground looking up: the small graphite-grey quadcopter with orange-tipped propellers lifts off the boyish private's open palm, rises through a gap in the green-brown camouflage netting and climbs into the pale grey sky; the private's face tilts up after it, both thumbs on the controller sticks on his chest harness. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Low angle: the drone lifts off the palm, threads up through the netting gap, shrinks against the grey sky; the private looks up, thumbs working, and reports one line. Sound: rotors whining loud then fading with altitude, one line of Korean dialogue.
ACTION_START: drone on palm, netting overhead
ACTION_END: drone a speck in grey sky through the netting, private looking up
NARRATION_KO: 하늘 위의 눈. 이 부대가 가진 가장 귀한 것이었습니다. 이 시대에는 하늘에서 보는 자가 없었습니다.
DIALOGUE_KO: 장태오: 1호기 이륙. 배터리 삼십 분.
SOUND: rotor vo ve mạnh rồi nhỏ dần theo độ cao.
CONTINUITY: Kế SC_042. Drone bay tây (theo vết móng). Pin 30 phút.
CHAIN_FROM: SC_042
CUT_HALF: no
REFS: CHAR_005_ref, UAV_001_ref, LOC_003_hollow_d1
AI_RISK: drone qua khe lưới → 1 vật nhỏ bay lên, máy tĩnh

### SC_044 | 5:46–5:54 | LOC_003 (LOC_003_hollow) | CHAR_005, CHAR_001, CHAR_002 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen with heads clustered around it, static
IMAGE_PROMPT: Close-up on the controller screen with heads clustered around it, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Tight on the seven-inch controller screen in the private's hands: a live aerial view of yellow grass sliding past far below, nothing but grass and cloud shadows, no HUD text; around the screen three helmets lean in almost touching — the private, the captain and the lieutenant — faces lit grey by the screen, camouflage netting behind. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: grass slides continuously across the screen, cloud shadows drifting; the three heads hold still, then the private speaks one line without looking up. Sound: faint rotor buzz from the controller speaker, breathing, one line of Korean dialogue.
ACTION_START: screen showing grass, heads leaning in
ACTION_END: same, grass still sliding, private speaking
NARRATION_KO: 팔 킬로. 그 사이에 마을 하나, 길 하나 없었습니다. 철원이라면 팔 킬로 안에 도로 셋, 마을 둘이 있었습니다.
DIALOGUE_KO: 장태오: 팔 킬로… 아직 풀입니다.
SOUND: tiếng rotor nhỏ qua loa controller, thở.
CONTINUITY: Màn hình drone = 'cửa sổ narrator' (prop_bible). Không HUD/số trên màn hình.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, CHAR_001_ref, CHAR_002_ref, LOC_003_hollow_d1
AI_RISK: màn hình + 3 mặt → mặt nghiêng, screen chiếm khung; không chữ HUD

### SC_045 | 5:54–6:02 | LOC_001 | — | VEH_205 | PROPS: — | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: straight-down drone view with a soft dark vignette, slow tilt toward the river  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: straight-down drone view with a soft dark vignette, slow tilt toward the river. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. Setting @LOC_001_wide: Wide brown Liao River under a cold pale grey sky, three long Sui pontoon bridges of lashed flat boats crossing it, endless Sui army columns and tents to the horizon on the far bank, near bank a flat steppe of dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, early spring, no trees. Action: Straight-down aerial view as seen on a drone feed, soft dark vignette at the frame edges and no HUD text: yellow steppe fills the frame, and at the very top edge a wide band of muddy brown river appears between the grass, the near end of a pontoon bridge of lashed flat boats just entering the corner. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): very slow tilt/drift upward from grass toward the brown river at the top edge. Sound: rotor buzz through a small speaker, a soft off-screen 'eh…'.
ACTION_START: grass with river at top edge
ACTION_END: river band centered, bridge end visible
NARRATION_KO: 요하였습니다. 고구려와 수나라의 경계였습니다. 폭 오백 미터, 흙탕물의 강이었습니다. 이 강을 건너는 것이 원정의 첫 관문이었습니다. 고구려는 이 강을 이백 년 동안 지켜 왔습니다.
DIALOGUE_KO: 
SOUND: rotor qua loa, một tiếng "어…" nhỏ ngoài hình.
CONTINUITY: POV drone → viền vignette mờ (không HUD). Sông Liêu lần đầu.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_205_ref, LOC_001_wide
AI_RISK: HUD drone → chỉ vignette mềm, không chữ/số

### SC_046 | 6:02–6:10 | LOC_001 | CHAR_005 | VEH_205, WPN_201 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen then tilt up to the operator's face, static
IMAGE_PROMPT: Close-up on the controller screen then tilt up to the operator's face, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_001_wide: Wide brown Liao River under a cold pale grey sky, three long Sui pontoon bridges of lashed flat boats crossing it, endless Sui army columns and tents to the horizon on the far bank, near bank a flat steppe of dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, early spring, no trees. Action: The controller screen fills most of the frame with a drone's-eye view: three long pontoon bridges of lashed flat boats being pushed out across the brown river from the far bank by thousands of tiny figures, columns of Sui infantry in ranks on the planks, dust and smoke drifting; above the screen the boyish private's face, breathing fast, eyes wide. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static on the screen: the bridges inch across the river with columns of tiny soldiers on them; camera tilts up to the private's face as he swallows and says one line. Sound: rotor buzz through the speaker, a dry swallow, one line of Korean dialogue.
ACTION_START: screen: bridges being pushed across river
ACTION_END: private's face, mouth open on the line
NARRATION_KO: 수나라 공부상서 우문개가 세운 다리였습니다. 셋이었습니다.
DIALOGUE_KO: 장태오: 다리… 다리를 놓고 있습니다.
SOUND: rotor, tiếng nuốt nước bọt.
CONTINUITY: Cầu phao ĐANG được đẩy (D1) — chưa chạm bờ. Không HUD. Lính trên cầu = chấm nhỏ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, VEH_205_ref, WPN_201_ref, LOC_001_wide
AI_RISK: đại quân trên màn hình → chấm nhỏ từ trên cao, không mặt

### SC_047 | 6:10–6:20 | LOC_001 | — | VEH_205, WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high drone aerial over the west bank, very slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high drone aerial over the west bank, very slow pull-out. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_wide: Wide brown Liao River under a cold pale grey sky, three long Sui pontoon bridges of lashed flat boats crossing it, endless Sui army columns and tents to the horizon on the far bank, near bank a flat steppe of dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, early spring, no trees. Action: High aerial from the drone: the west bank of the brown river covered with grey felt tents in grid rows to the horizon, thousands of thin columns of cooking smoke, red and yellow banners, horse lines, the three pontoon bridges reaching out from the bank; the east bank empty yellow grass; no visible end to the camp. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): very slow pull-out, the camp never ending. Sound: rotor buzz through a speaker, then human silence.
ACTION_START: camp filling frame, bridges at bottom
ACTION_END: pulled out, camp still to the horizon
NARRATION_KO: 탁군을 떠난 지 두 달. 24군이 요하 서안에 모여 있었습니다. 강 하나가 고구려와 그들 사이에 있었습니다. 천막의 수를 세는 것은 의미가 없었습니다.
DIALOGUE_KO: 
SOUND: rotor qua loa; im lặng người.
CONTINUITY: Ảnh đại quân chủ đạo P3. Aerial thuần, 'không thấy điểm cuối'.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_205_ref, WPN_201_ref, PROP_021_ref, LOC_001_wide

### SC_048 | 6:20–6:28 | LOC_003 (LOC_003_hollow) | CHAR_005 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Extreme close-up on the operator's face, static
IMAGE_PROMPT: Extreme close-up on the operator's face, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The boyish private's face fills the frame lit grey-blue from below by the controller screen, large eyes unblinking, lips trembling slightly, a strand of camouflage netting shadow across his helmet, yellow grass out of focus behind. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up: the screen glow flickers on his face, his eyes do not blink, his lips tremble, then he whispers one line. Sound: faint rotor buzz from the speaker, wind, one whispered line of Korean dialogue.
ACTION_START: face lit by screen, eyes wide
ACTION_END: lips parted after the line, still staring
NARRATION_KO: 끝이 없다는 말은 과장이 아니었습니다. 화면이 닿는 곳까지가 전부 진영이었습니다. 사람의 눈으로는 끝을 볼 수 없는 진영이었습니다.
DIALOGUE_KO: 장태오: 끝이… 안 보입니다.
SOUND: rotor qua loa, gió.
CONTINUITY: Chỉ 1 mặt. Dấu hiệu: mặt tròn búng sữa, mũi hếch.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, LOC_003_hollow_d1

### SC_049 | 6:28–6:36 | LOC_003 (LOC_003_hollow) | CHAR_002, CHAR_003 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium two-shot, static, both faces in frame
IMAGE_PROMPT: Medium two-shot, static, both faces in frame. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The tall lieutenant stares down at the controller screen held out of frame below, jaw clenched, silent for the first time, the goggles on his helmet reflecting the screen's grey glow; beside him the stocky sergeant does not look at the screen at all — he watches the lieutenant's face. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: nothing moves but the lieutenant's jaw working and the reflection flickering in his goggles; the sergeant's eyes stay on him; nobody speaks for the whole clip. Sound: rotor buzz through a speaker, wind, no dialogue.
ACTION_START: lieutenant staring down, sergeant watching him
ACTION_END: same, lieutenant's jaw tighter
NARRATION_KO: 삼십만이면 반나절이라던 사람이었습니다. 화면 속 숫자는 그 세 배를 넘었습니다. 그는 셈을 다시 하고 있었습니다.
DIALOGUE_KO: 
SOUND: rotor, gió, không ai nói.
CONTINUITY: Không thoại. Kính bảo hộ phản chiếu màn hình.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, CHAR_003_ref, LOC_003_hollow_d1

### SC_050 | 6:36–6:44 | LOC_003 (LOC_003_hollow) | CHAR_005, CHAR_001 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller corner then rack to the two faces, static
IMAGE_PROMPT: Close-up on the controller corner then rack to the two faces, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Tight on the corner of the controller screen where a small battery indicator glows amber with no readable digits; the boyish private lifts his eyes to the captain standing beside him; the captain gives a single nod; the private's thumb pushes the stick and the aerial image on the screen swings around toward the east. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the amber battery indicator blinks once; the private looks up and asks one line; the captain nods once; the thumb pushes the stick and the screen image swings east. Sound: a battery warning beep, rotor buzz, one line of Korean dialogue.
ACTION_START: battery indicator, private looking down
ACTION_END: captain's nod, screen image swinging east
NARRATION_KO: 배터리 십팔 분. 돌아올 거리를 빼면 볼 수 있는 시간은 끝났습니다. 여섯 분은 돌아오는 값이었습니다.
DIALOGUE_KO: 장태오: 배터리 십팔 분. 복귀시킵니까?
SOUND: bíp cảnh báo pin, rotor.
CONTINUITY: Pin 19→18 = overlay số ở edit; ảnh chỉ 'amber indicator'.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, CHAR_001_ref, LOC_003_hollow_d1
AI_RISK: số pin trên màn hình → 'amber indicator, no digits'; số overlay edit

### SC_051 | 6:44–6:52 | LOC_003 (LOC_003_hollow) | CHAR_001 | VEH_001, VEH_004 | PROPS: PROP_005 | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: over-the-shoulder into a dark screen, slow push-in
IMAGE_PROMPT: Still for ken-burns: over-the-shoulder into a dark screen, slow push-in. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The captain looks down at the now-dark controller screen; on its black glass his own dim reflection and the reflections of helmeted soldiers behind him; beyond, the K2 tank under camouflage netting and the 4x4 command vehicle with its small generator silent under a closed cover; grey noon light. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow push-in on the dark glass and the reflections. Sound: wind, and far away, almost imagined, Sui drums.
ACTION_START: captain over dark screen, tank behind
ACTION_END: tight on reflections in the black glass
NARRATION_KO: 그는 숫자를 세지 않았습니다. 발전기도 돌리지 않았습니다. 소리는 십 리를 갔습니다. 강 건너에 있는 건 군대가 아니었습니다. 나라 하나가 움직이고 있었습니다.
DIALOGUE_KO: 
SOUND: gió, xa xa vọng trống Tùy — gần như tưởng tượng.
CONTINUITY: Máy phát K151 tắt (không sạc — tiếng động). Kết P3 trước mid-roll.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_001_ref, VEH_004_ref, LOC_003_hollow_d1

### SC_052 | 6:52–7:00 | LOC_003 (LOC_003_hollow) | — | UAV_001 | PROPS: — | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: wide sky shot, slow push toward the western horizon
IMAGE_PROMPT: Still for ken-burns: wide sky shot, slow push toward the western horizon. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: A pale grey sky over yellow steppe: the small grey quadcopter is a speck flying toward the camera, low; far on the western horizon a thin line of yellow dust hangs; the grassy hollow with camouflage netting at the bottom of frame. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow push toward the western horizon and its thin dust line. Sound: rotors fading in, wind.
ACTION_START: drone speck and horizon
ACTION_END: tight on the western dust line
NARRATION_KO: 드론은 돌아왔습니다. 배터리 여섯 분이 남아 있었습니다. 그게 무엇이든, 이쪽으로 오고 있었습니다. 이제 그들에게 필요한 것은 총이 아니라 시간이었습니다.
DIALOGUE_KO: 
SOUND: rotor xa dần, gió.
CONTINUITY: Mid-roll 1 @7:00 sau cảnh này.
CHAIN_FROM: —
CUT_HALF: no
REFS: UAV_001_ref, LOC_003_hollow_d1


## [Phần 4] 첫 접촉 (7:00–10:30) · trận cầu phao [史] + cậu bé trinh sát

### SC_053 | 7:00–7:08 | LOC_001 | GOG_ARCHERS | VEH_205, WPN_201 | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Slow aerial wide over the river, single slow drift  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Slow aerial wide over the river, single slow drift. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_wide: Wide brown Liao River under a cold pale grey sky, three long Sui pontoon bridges of lashed flat boats crossing it, endless Sui army columns and tents to the horizon on the far bank, near bank a flat steppe of dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, early spring, no trees. Action: High aerial: three pontoon bridges of lashed flat boats are being pushed out from the west bank across the brown river, thousands of Sui soldiers packed on the planks under red banners; on the high east bank, lines of Goguryeo archers in iron lamellar rise from the yellow grass and the first probing arrows fall into the water around the bridge heads, red shields lifting; no faces. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: One slow aerial drift along the river: bridges creeping east, arrows dropping into the water around the bridge heads, red shields rising; no dialogue, no narration. Sound: slow Sui drums, chanting of men pushing the bridges, arrows plunking into water.
ACTION_START: bridges mid-river, archers rising on east bank
ACTION_END: bridges closer, arrows splashing, shields up
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: trống Tùy nhịp chậm, tiếng hò đẩy cầu, tên rơi nước.
CONTINUITY: Sau mid-roll 1: không thoại, không narration. Trận sử. CUT_HALF (khối trận).
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, VEH_205_ref, WPN_201_ref, PROP_021_ref, LOC_001_wide
AI_RISK: đại quân + tên bay → aerial, không cận

### SC_054 | 7:08–7:16 | LOC_001 (LOC_001_bank) | — | VEH_205, WPN_201 | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Medium-wide from on the bridge deck looking toward the east bank, static
IMAGE_PROMPT: Medium-wide from on the bridge deck looking toward the east bank, static. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: From the plank deck of the pontoon bridge: the bridge's front edge stops short in brown water three meters from the steep muddy east bank; Sui soldiers in mingguang armor crowd the edge with red rectangular shields; the first volley of arrows from the high bank slams into the planks and the men, soldiers toppling into the water, shields coming up too late; helmets and shields hide faces. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static from the deck: arrows hammer into the planks, men at the edge stagger and fall into the water, red shields jerk upward; camera holds. Sound: water, arrows thudding into wood, shouting, the drums stopping.
ACTION_START: soldiers crowding bridge edge, shields down
ACTION_END: arrows in planks, men falling, shields up
NARRATION_KO: 다리는 동쪽 기슭보다 한 장, 세 미터가 짧았습니다. 그 세 미터가 첫 번째 싸움을 결정했습니다. 다리를 놓은 사람은 강폭을 잘못 쟀습니다.
DIALOGUE_KO: 
SOUND: nước, tên cắm gỗ, la hét, trống ngừng.
CONTINUITY: Cầu ngắn 1장 (3 m). Không gore, không mặt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_205_ref, WPN_201_ref, PROP_021_ref, LOC_001_detail
AI_RISK: đám đông cận + tên → mũ/khiên che mặt, wide-medium, không máu

### SC_055 | 7:16–7:24 | LOC_001 (LOC_001_bank) | GOG_ARCHERS, GOG_INFANTRY | WPN_101 | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Low angle from the water's edge looking up the bank, static
IMAGE_PROMPT: Low angle from the water's edge looking up the bank, static. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: From the waterline looking up the steep muddy bank: a rank of Goguryeo soldiers in iron lamellar armor and plumed iron helmets rises out of the yellow grass on the crest, short composite reflex bows drawn together, black three-legged crow banners on tall poles behind them; arrows already in the air; faces shadowed by helmet brims. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the rank rises out of the grass, bows come up and draw as one, the volley releases, a second volley follows. Sound: bowstrings snapping in unison, arrows hissing.
ACTION_START: soldiers rising from grass, bows down
ACTION_END: bows released, second volley drawn
NARRATION_KO: 고구려군은 높은 기슭에서 기다리고 있었습니다. 수나라가 강을 재는 동안 그들은 기슭을 골랐습니다. 기슭이 곧 성벽이었습니다.
DIALOGUE_KO: 
SOUND: dây cung bật hàng loạt, tên rít.
CONTINUITY: Goguryeo lần đầu thấy rõ (giáp lamellar, chỏm lông, cờ 삼족오). WPN_102 ref cần tạo.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, WPN_101_ref, PROP_012_ref, LOC_001_detail
AI_RISK: hàng lính cận → low angle ngược sáng, mũ che mặt

### SC_056 | 7:24–7:32 | LOC_001 (LOC_001_bank) | — | VEH_205, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Lateral tracking shot at water level
IMAGE_PROMPT: Lateral tracking shot at water level. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: Sui soldiers leap from the bridge head into chest-deep brown water, red rectangular shields held over their heads, wading toward the muddy bank; arrows stick in the shields and plunk into the water; a man goes down and drags the one behind him under; the bridge and its red banners behind; no faces clear. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera tracks sideways at water level with the wading men: shields overhead taking arrows, water churning, one man falling and pulling down another; single lateral move. Sound: splashing water, arrows thumping into wooden shields, shouting.
ACTION_START: men jumping from bridge head into water
ACTION_END: men wading, shields overhead, one going under
NARRATION_KO: 먼저 물에 들어간 쪽이 불리했습니다. 갑옷은 젖으면 두 배로 무거웠습니다. 고구려는 그것을 알고 물가에서 기다렸습니다.
DIALOGUE_KO: 
SOUND: nước bắn, khiên gỗ chịu tên, la hét.
CONTINUITY: Không gore. Khiên đỏ che mặt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_205_ref, WPN_201_ref, LOC_001_detail
AI_RISK: nhiều người trong nước → khiên che, tracking đều

### SC_057 | 7:32–7:40 | LOC_001 (LOC_001_bank) | GOG_INFANTRY | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the waterline, static, no gore
IMAGE_PROMPT: Medium shot at the waterline, static, no gore. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: At the water's edge: Goguryeo soldiers in iron lamellar stand on the high slick mud and thrust long spears downward; below them Sui soldiers in wet mingguang armor slip and slide on the steep mud, unable to climb, red shields raised, water to their waists; helmets and shields hide faces; no blood. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium: spears thrust down from the mud crest, the men below slide back on the mud, shields catching spear points, wet armor dragging them down; no blood shown. Sound: spear shafts on armor, sucking mud, hard breathing.
ACTION_START: spears raised on crest, men below climbing
ACTION_END: spears thrust, men sliding back down the mud
NARRATION_KO: 물속에서 싸운 쪽이 졌습니다. 진흙 기슭은 오르는 자에게 벽이었습니다. 이기려면 기슭에 서 있어야 했습니다.
DIALOGUE_KO: 
SOUND: giáo chạm giáp, bùn, tiếng thở.
CONTINUITY: Bùn dốc = tường. Không gore.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, WPN_201_ref, LOC_001_detail
AI_RISK: cận giao chiến → không máu, giáp che, medium không cận mặt

### SC_058 | 7:40–7:48 | LOC_001 (LOC_001_bank) | SUI_VANGUARD_CMDR_DEAD | VEH_205, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: High angle from the bridge looking down at its edge, static
IMAGE_PROMPT: High angle from the bridge looking down at its edge, static. Sui general around 50 with a short black beard, in mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: From above on the bridge deck: a Sui general in mingguang armor with two polished round chest plates, red silk cloak and red-tasseled helmet sinks to his knees at the plank edge; two soldiers seize him under the arms and drag him back along the planks, his red cloak trailing on the brown water; no visible wound. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static high angle: the general folds to his knees at the edge, two soldiers grab him and haul him backward along the planks, the red cloak dragging through the water. Sound: shouting, water, Sui drums flaring in panic then cutting off.
ACTION_START: general standing at plank edge
ACTION_END: general dragged back along planks, cloak in water
NARRATION_KO: 선봉장 맥철장이 그 물가에서 죽었습니다. 황제의 장수가 강 하나를 건너지 못한 것입니다.
DIALOGUE_KO: 
SOUND: la hét, nước, trống Tùy vang lên gấp gáp rồi tắt.
CONTINUITY: 맥철장 chết — 1 shot, không vết thương rõ. Extra không ID.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_205_ref, WPN_201_ref, LOC_001_detail
AI_RISK: cái chết → không máu, chỉ khuỵu + kéo lùi

### SC_059 | 7:48–7:56 | LOC_001 (LOC_001_bank) | GOG_ARCHERS | VEH_205, WPN_101 | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Wide from the east bank, Goguryeo line in the foreground, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide from the east bank, Goguryeo line in the foreground, static. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: From the east bank behind a foreground line of Goguryeo archers in iron lamellar with black three-legged crow banners: all three pontoon bridges are being hauled back toward the west bank, mooring ropes taut, Sui soldiers still on the planks crawling backward clutching the ropes while arrows hiss after them; the brown river surface littered with drifting red shields. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the bridges drag slowly back toward the far bank, ropes straining, men crawling on the planks, arrows still flying from the foreground line, red shields turning in the current. Sound: hemp ropes creaking, arrows into water, the river.
ACTION_START: bridges near east bank, archers loosing
ACTION_END: bridges pulled back mid-river, shields drifting
NARRATION_KO: 전사웅, 맹차 두 장수도 함께 죽었습니다. 수나라는 다리를 도로 끌어갔습니다. 첫 도하는 실패였습니다. 다리는 그날 밤 다시 만들어지기 시작했습니다.
DIALOGUE_KO: 
SOUND: dây thừng nghiến, tên rơi nước, nước.
CONTINUITY: Cầu bị kéo về. Aerial-ish wide. Cờ 삼족오 tiền cảnh.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, VEH_205_ref, WPN_101_ref, PROP_012_ref, LOC_001_detail

### SC_060 | 7:56–8:04 | LOC_001 (LOC_001_bank) | GOG_CAVALRYMEN | VEH_101, WPN_101, WPN_201 | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Low lateral tracking shot along the mud flat
IMAGE_PROMPT: Low lateral tracking shot along the mud flat. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_001_detail: East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it. Action: Goguryeo cataphracts — horses in dull iron lamellar barding with iron face masks, riders in full iron lamellar with red-plumed helmets and long lances — thunder down the mud flat after the last Sui soldiers wading back toward the retreating bridge head; from the far bank, Sui crossbow bolts stab into the mud around the hooves; the lead rider hauls his horse to a halt at the water's edge, lance up; no wounded shown. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Low camera tracks sideways with the charging cataphracts along the mud flat; bolts kick up mud around the hooves; the lead riders rein in hard at the water's edge, horses rearing slightly, and hold; a horn sounds. Sound: hooves on mud, Sui crossbows snapping, bolts thudding into mud, a recall horn.
ACTION_START: cataphracts charging along mud flat
ACTION_END: lead riders halted at water's edge, lances up
NARRATION_KO: 고구려는 이겼습니다. 그날은. 강 건너의 숫자는 하나도 줄지 않았습니다. 이틀 뒤, 다리는 다시 올 것이었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa trên bùn, nỏ Tùy bật, tên cắm bùn, tù và thu quân.
CONTINUITY: VEH_101 개마무사 lần đầu. Kết trận sử. Kỵ Goguryeo này = 'vệt bụi' SC_006/012.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_101_ref, WPN_101_ref, WPN_201_ref, PROP_012_ref, LOC_001_detail
AI_RISK: ngựa giáp + kỵ sĩ số đông → tracking thấp, bụi bùn che chân

### SC_061 | 8:04–8:12 | LOC_003 (LOC_003_hollow) | CHAR_006 | VEH_003 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Close-up at wheel height, static
IMAGE_PROMPT: Close-up at wheel height, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Hard cut: the staff sergeant with painted face kneels beside the cargo truck's arrow-pierced front tire under camouflage netting, both hands wrapped around the Goguryeo arrow shaft; he yanks it out in one pull, examines the barbed triangular iron head, and slides the arrow under the lacing of his chest armor. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: both hands grip the shaft, one hard pull, the arrow comes free with a long hiss of escaping air; he turns the barbed head to the light, then tucks the arrow into his chest armor lacing. Sound: a long tire hiss, wind, no dialogue.
ACTION_START: hands on arrow shaft in tire
ACTION_END: arrow tucked into chest armor, tire flat
NARRATION_KO: 화살에는 주인이 있었습니다. 백성민은 그 주인을 찾으러 갔습니다. 셋만 데리고, 총은 어깨에 멘 채였습니다.
DIALOGUE_KO: 
SOUND: lốp xì, gió.
CONTINUITY: HARD CUT về hiện đại (chiều D1). Cùng lốp SC_001 — lốp này đã thay? Script SC_035 nói lốp thủng buộc trên thùng; ở SC_061 rút tên khỏi lốp → coi như lốp thủng vẫn còn tên khi buộc trên thùng: prompt để 'arrow-pierced tire' cạnh xe (dưới lưới) — QC chấp nhận.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, VEH_003_ref, PROP_015_ref, LOC_003_hollow_d1
AI_RISK: tay cận rút tên → 2 tay trên 1 cán, chuyển động 1 nhát

### SC_062 | 8:12–8:20 | LOC_003 (LOC_003_gully) | CHAR_006, ROK_SOLDIERS | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot from behind three men moving low, single move, then hold
IMAGE_PROMPT: Tracking shot from behind three men moving low, single move, then hold. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: From behind: the staff sergeant in a boonie hat leads two helmeted soldiers in a crouch along a line of hoofprints through knee-high yellow grass and down into a dry gully floored with grey cobbles; rifles slung muzzle-down; his left hand rises in a fist and the three drop to a crouch at the gully lip. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera follows low behind the three men through the grass and down into the gully, then holds as the sergeant's fist comes up and all three sink into a crouch. Sound: dry grass, cobbles shifting underfoot, wind.
ACTION_START: three men moving low through grass toward gully
ACTION_END: three crouched at gully lip, fist raised
NARRATION_KO: 발자국은 동쪽으로, 마른 개울까지 이어졌습니다. 말 한 필. 편자는 없었습니다. 백성민은 발자국의 주인이 혼자라고 판단했습니다.
DIALOGUE_KO: 
SOUND: cỏ khô, đá cuội lăn, gió.
CONTINUITY: 2 lính trinh sát = extras sau lưng. Súng đeo, nòng xuống.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, WPN_001_ref, LOC_003_hollow_d1
AI_RISK: tay cầm súng → súng đeo chéo nòng xuống, máy sau lưng

### SC_063 | 8:20–8:28 | LOC_003 (LOC_003_gully) | CHAR_006, BOY_SCOUT | WPN_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Over-the-shoulder from behind the sergeant, static
IMAGE_PROMPT: Over-the-shoulder from behind the sergeant, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: Over the staff sergeant's boonie-hatted shoulder: ten meters away on the cobbles of the dry gully a Goguryeo boy of about seventeen in a coarse brown hemp jacket and cloth headband stands with a short composite bow drawn to full draw, arrow pointed straight at the camera, both hands visibly shaking, eyes huge. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static over-the-shoulder: the boy holds full draw, the bow arm trembling visibly, his breath fast; the sergeant's shoulder does not move. Sound: bowstring creaking under tension, the boy's ragged breathing, wind over the gully.
ACTION_START: boy at full draw, shaking
ACTION_END: boy still at full draw, trembling harder
NARRATION_KO: 열일곱쯤 된 소년이었습니다. 요동성의 척후였습니다. 어제 타이어에 화살을 쏜 것도 그였습니다.
DIALOGUE_KO: 
SOUND: dây cung kêu căng, thở gấp của cậu bé, gió trên khe.
CONTINUITY: 소년 척후 lần đầu (EXTRA_boy_scout_ref cần tạo). Cung 맥궁.
CHAIN_FROM: SC_062
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, EXTRA_boy_scout_ref, WPN_101_ref, LOC_003_hollow_d1
AI_RISK: tay cầm cung căng → 1 người, hai tay rõ, tĩnh

### SC_064 | 8:28–8:36 | LOC_003 (LOC_003_gully) | CHAR_006, ROK_SOLDIERS | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot facing the sergeant, slight low angle, static
IMAGE_PROMPT: Medium shot facing the sergeant, slight low angle, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: The staff sergeant slowly lowers his black assault rifle to the cobbles at his feet, then opens both empty palms outward at chest height and takes half a step back; his left hand makes a small downward signal behind him and the two soldiers behind lower their rifle muzzles to the ground; painted face calm. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the rifle goes down to the stones slowly, both palms open, a half step back, the hand signal behind; the two soldiers' muzzles drop; nobody speaks. Sound: rifle stock touching stone, wind, no dialogue.
ACTION_START: rifle in hands, being lowered
ACTION_END: rifle on stones, both palms open, soldiers' muzzles down
NARRATION_KO: 이 땅에서 처음 만난 사람이었습니다. 총을 겨눌 수는 없었습니다. 백성민은 그렇게 배웠습니다. 사냥꾼은 처음 보는 것을 쏘지 않는 법이었습니다.
DIALOGUE_KO: 
SOUND: báng súng chạm đá, gió.
CONTINUITY: Kế SC_063 (đảo góc). Súng đặt xuống = hành động chính.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, WPN_001_ref, LOC_003_hollow_d1
AI_RISK: tay cầm súng → súng hạ chậm, kết thúc tay trống

### SC_065 | 8:36–8:44 | LOC_003 (LOC_003_gully) | CHAR_006, BOY_SCOUT | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium two-shot in profile across the gully, static
IMAGE_PROMPT: Medium two-shot in profile across the gully, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: In profile: the staff sergeant draws the Goguryeo arrow from his chest armor lacing and holds it out in both open hands, nock toward the boy, barbed head toward himself, then bends and lays it on a flat grey stone midway between them and steps back; the boy, bow still half drawn, watches. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static profile: the arrow comes out of the armor lacing, is offered in two flat hands, laid on the flat stone, and the sergeant steps back saying one line; the boy's bow arm wavers. Sound: arrow shaft on stone, wind, one line of Korean dialogue.
ACTION_START: arrow drawn from chest armor
ACTION_END: arrow on stone, sergeant stepped back, boy watching
NARRATION_KO: 화살을 돌려주는 것. 그가 아는 유일한 인사였습니다. 소년은 그 인사를 알아들었습니다.
DIALOGUE_KO: 백성민: 네 화살이다. 돌려준다.
SOUND: mũi tên chạm đá, gió.
CONTINUITY: Trả mũi tên (payoff P1). Cùng mũi tên SC_001/061.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, EXTRA_boy_scout_ref, PROP_015_ref, LOC_003_hollow_d1
AI_RISK: 2 người + vật nhỏ → profile rõ, tay mở

### SC_066 | 8:44–8:52 | LOC_003 (LOC_003_gully) | BOY_SCOUT | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Close-up on the boy's face, static
IMAGE_PROMPT: Close-up on the boy's face, static. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: Close on the Goguryeo boy's dust-streaked face: his eyes drop to the arrow lying on the stone, lift to a small red-and-blue cloth patch on the shoulder of the man out of focus in front of him, and the bow sinks a little at a time, his lips parting. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes go to the arrow, up to the shoulder patch, the bow lowers in small jerks, and he speaks one cracked line. Sound: bowstring slackening, breath, one line of Korean dialogue.
ACTION_START: boy's eyes on arrow, bow up
ACTION_END: bow lowered, mouth open after the line
NARRATION_KO: 소년에게 세상은 둘뿐이었습니다. 고구려와 수나라. 이들은 둘 다 아니었습니다.
DIALOGUE_KO: 소년 척후: 수나라… 수나라 사람이오?
SOUND: dây cung chùng, thở.
CONTINUITY: Không mặt 백성민 (out of focus). Patch 태극기 mờ tiền cảnh.
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_boy_scout_ref, PROP_015_ref, LOC_003_hollow_d1

### SC_067 | 8:52–9:00 | LOC_003 (LOC_003_gully) | CHAR_006, BOY_SCOUT | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: The staff sergeant shakes his head slowly, once; the Goguryeo boy bends, snatches the arrow from the stone, then thrusts his arm out pointing west, hand still shaking, mouth working as if he has run all night; grey cobbles and gully walls around them. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: one slow head shake from the sergeant; the boy scoops up the arrow and points west with a shaking arm, saying one line twice over. Sound: wind, a dry swallow, one line of Korean dialogue.
ACTION_START: sergeant's head shake, boy bending for arrow
ACTION_END: boy pointing west with arrow in fist
NARRATION_KO: 백만. 소년이 서쪽에서 본 것은 그것이었습니다. 그는 그 숫자를 성에 전하러 가는 길이었습니다.
DIALOGUE_KO: 소년 척후: 백만. 백만이오.
SOUND: gió, tiếng nuốt.
CONTINUITY: '백만' — chỉ tây.
CHAIN_FROM: SC_065
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, EXTRA_boy_scout_ref, PROP_015_ref, LOC_003_hollow_d1

### SC_068 | 9:00–9:10 | LOC_003 (LOC_003_gully) | BOY_SCOUT | — | PROPS: PROP_015 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up portrait, slow push into the eyes
IMAGE_PROMPT: Still for ken-burns: close-up portrait, slow push into the eyes. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: Portrait of the Goguryeo boy scout: face streaked with yellow dust, huge eyes, the returned arrow clenched in his fist against his chest, the grey rock wall of the gully behind him. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push-in into the boy's eyes. Sound: wind, silence.
ACTION_START: portrait with arrow at chest
ACTION_END: tight on eyes
NARRATION_KO: 백만. 소년은 그 수를 세어 본 적이 없었습니다. 들었을 뿐입니다. 하지만 그 말은 정확했습니다. 백만은 이백만이 아니었지만, 소년에게는 같은 말이었습니다.
DIALOGUE_KO: 
SOUND: gió, im.
CONTINUITY: Chân dung 소년 척후 — dùng làm ref phụ nếu cần.
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_boy_scout_ref, PROP_015_ref, LOC_003_hollow_d1

### SC_069 | 9:10–9:18 | LOC_003 (LOC_003_gully) | CHAR_001, BOY_SCOUT, ROK_SOLDIERS | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the gully floor looking up at the rim, static
IMAGE_PROMPT: Low angle from the gully floor looking up at the rim, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: From the gully floor: the captain and two helmeted soldiers arrive at the rim above and stop, looking down, rifles slung muzzle-down; in the foreground the Goguryeo boy looks up and his eyes fix on the small red-and-blue flag patch on the captain's right shoulder — blank, unrecognizing — then drop to the rifle muzzles. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the three figures appear at the rim and stop; the boy's gaze goes to the shoulder patch, holds blankly, then falls to the rifle muzzles; nobody speaks. Sound: grass, wind, a cobble rolling.
ACTION_START: rim empty, boy looking up
ACTION_END: captain and two soldiers at rim, boy staring at patch
NARRATION_KO: 태극기. 소년이 알 리 없는 깃발이었습니다. 천 년도 더 뒤에 생길 깃발이었습니다.
DIALOGUE_KO: 
SOUND: cỏ, gió, đá lăn.
CONTINUITY: 한승우 tới mép khe. Lính phụ không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, EXTRA_boy_scout_ref, WPN_001_ref, LOC_003_hollow_d1

### SC_070 | 9:18–9:26 | LOC_003 (LOC_003_gully) | CHAR_001, BOY_SCOUT | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot at the boy's eye level, static
IMAGE_PROMPT: Medium two-shot at the boy's eye level, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: The captain slides down into the gully and drops to one knee on the cobbles at the Goguryeo boy's eye level; he touches his own chest, shakes his head, then points east; he speaks slowly, one word at a time; the boy watches his mouth. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the captain slides down, kneels, touches his chest, shakes his head, points east, and speaks one slow line; the boy stares at his mouth. Sound: cobbles, wind, one line of Korean dialogue spoken slowly.
ACTION_START: captain sliding down into gully
ACTION_END: captain kneeling, arm pointing east, boy watching
NARRATION_KO: 한승우는 첫 질문으로 성을 물었습니다. 이유가 아니라 위치였습니다. 이유를 물으면 답이 없었습니다. 위치를 물으면 답이 있었습니다.
DIALOGUE_KO: 한승우: 우리는 수나라가 아닙니다. 성은 어디입니까?
SOUND: gió, im.
CONTINUITY: Kế SC_069. La bàn trên cổ (identifier) ngang tầm mắt cậu bé.
CHAIN_FROM: SC_069
CUT_HALF: no
REFS: CHAR_001_ref, EXTRA_boy_scout_ref, LOC_003_hollow_d1

### SC_071 | 9:26–9:34 | LOC_003 (LOC_003_gully) | CHAR_001, BOY_SCOUT | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot from inside the gully with the rise behind, static
IMAGE_PROMPT: Medium shot from inside the gully with the rise behind, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: The Goguryeo boy raises his arm to point east, lips forming a word — and behind the grassy rise above the gully the small angular turret of a K21 IFV with its short 40mm autocannon heaves up into view over the grass as the engine roars into life, dust shaking off it; the captain, kneeling, does not turn. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the boy points east and speaks one broken line; at that moment the engine roar hits, the IFV turret rises over the grass behind, dust shivering off the hull; the boy's face freezes. Sound: a diesel engine bursting into life, echoing off the gully walls, one line of Korean dialogue.
ACTION_START: boy pointing east, rise empty behind
ACTION_END: IFV turret above the grass, boy frozen
NARRATION_KO: 요동성. 소년의 입에서 처음 나온 지명이었습니다. 요동의 심장. 백만이 노리는 첫 번째 성이었습니다.
DIALOGUE_KO: 소년 척후: 요동… 요동성이오.
SOUND: động cơ K21 nổ đột ngột, dội vách đá.
CONTINUITY: K21 천둥 2 nổ máy. Tháp pháo nhô lên gò.
CHAIN_FROM: SC_070
CUT_HALF: no
REFS: CHAR_001_ref, EXTRA_boy_scout_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_072 | 9:34–9:42 | LOC_003 (LOC_003_gully) | CHAR_006, BOY_SCOUT | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, low angle on the gully floor, static
IMAGE_PROMPT: Medium shot, low angle on the gully floor, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: The Goguryeo boy has fallen on his backside on the cobbles and scrambles backward on his hands, eyes locked on the K21 turret above the rise; the staff sergeant with painted face holds one hand out open and low — it's all right — but the boy is already twisting up onto his feet. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the boy crab-scrambles backward over the cobbles, staring up at the turret; the sergeant's open hand extends slowly; the boy rolls and springs up. Sound: cobbles scattering, engine idling, fast breathing.
ACTION_START: boy on the ground scrambling back
ACTION_END: boy up on his feet, sergeant's hand still out
NARRATION_KO: 쇠로 된 집이 울었습니다. 소년에게는 그렇게 보였습니다. 그 소리는 그가 아는 어떤 짐승의 것도 아니었습니다.
DIALOGUE_KO: 
SOUND: đá cuội, động cơ nền, thở gấp.
CONTINUITY: Kế SC_071.
CHAIN_FROM: SC_071
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, EXTRA_boy_scout_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_073 | 9:42–9:50 | LOC_003 (LOC_003_gully) | CHAR_001, BOY_SCOUT, ROK_SOLDIERS | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Wide from the gully rim toward the east, static
IMAGE_PROMPT: Wide from the gully rim toward the east, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: Wide: the Goguryeo boy sprints away east through knee-high yellow grass, bow on his back, the arrow still clenched in his fist; two helmeted soldiers lurch forward to chase and the captain throws his arm straight out sideways, barring them without a word. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the boy runs east through the grass, growing smaller; the two soldiers start after him and stop dead against the captain's outstretched arm; the arm stays up. Sound: grass trampled, breathing, wind.
ACTION_START: boy breaking into a run, soldiers starting forward
ACTION_END: boy small in the grass, captain's arm out, soldiers halted
NARRATION_KO: 한승우는 소년을 보냈습니다. 그가 달려가는 곳에 성이 있을 것이었습니다. 잡아 두면 얻는 것은 적 하나뿐이었습니다.
DIALOGUE_KO: 
SOUND: cỏ khô bị đạp, thở, gió.
CONTINUITY: Cậu bé chạy về đông (요동성). Lính phụ không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, EXTRA_boy_scout_ref, PROP_015_ref, LOC_003_hollow_d1

### SC_074 | 9:50–10:00 | LOC_003 (LOC_003_gully) | BOY_SCOUT | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide, slow drift east after a running figure  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide, slow drift east after a running figure. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. Setting @LOC_003_hollow_d1: A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees. Action: A small running figure — the Goguryeo boy — shrinks across a sea of yellow grass toward a grey eastern horizon, his long shadow stretching beside him, nothing else in the frame. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow drift east following the running figure. Sound: wind.
ACTION_START: running figure mid-frame
ACTION_END: figure tiny near horizon
NARRATION_KO: 소년은 성으로 달렸습니다. 보고할 말은 하나였습니다. 쇠로 된 집. 그 말은 그날 저녁 말객의 귀에 들어갔습니다. 쇠로 된 집. 말객은 그 말을 두 번 되물었습니다.
DIALOGUE_KO: 
SOUND: gió.
CONTINUITY: Ken-burns chuyển cảnh.
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_boy_scout_ref, LOC_003_hollow_d1

### SC_075 | 10:00–10:08 | LOC_003 (LOC_003_hollow) | CHAR_002, CHAR_001 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the grass up at an IFV roof, static
IMAGE_PROMPT: Low angle from the grass up at an IFV roof, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The tall lieutenant stands on the roof of the K21 IFV with fists on his hips, goggles pushed up on his helmet, shouting down; below in the yellow grass the captain looks up at him, face unchanged; camouflage netting half pulled back from the vehicle. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the lieutenant shouts one line down from the roof, arms spread; the captain looks up without any change of expression; the engine dies. Sound: engine shutting off, wind, one shouted line of Korean dialogue.
ACTION_START: lieutenant on roof, fists on hips
ACTION_END: lieutenant arms spread after the line, captain looking up
NARRATION_KO: 오태민은 포로를 원했습니다. 한승우는 길잡이를 원했습니다. 두 사람은 같은 소년에게서 다른 것을 보았습니다.
DIALOGUE_KO: 오태민: 왜 보내십니까? 잡았어야 합니다!
SOUND: động cơ K21 tắt, gió.
CONTINUITY: Xe 천둥 2 vừa nổ máy (SC_071) giờ tắt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, CHAR_001_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_076 | 10:08–10:16 | LOC_003 (LOC_003_hollow) | CHAR_001, CHAR_006 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The captain ignores the shouting behind him and turns to the staff sergeant, who is picking his black assault rifle back up from the grass, muzzle down; the captain points east; the sergeant nods and pulls a small notebook from a chest pocket to note the bearing, compass at the captain's neck. Light: Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting. Modern soldiers' uniforms clean and crisp, a light film of dew on body armor. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the captain turns, points east and gives one order; the sergeant nods, shoulders the rifle muzzle-down, pulls out a small notebook and writes. Sound: wind, pencil scratching, one line of Korean dialogue.
ACTION_START: captain turning, sergeant lifting rifle
ACTION_END: sergeant writing in notebook, captain pointing east
NARRATION_KO: 방향은 동쪽. 성은 그쪽에 있었습니다. 백만은 반대쪽이었습니다. 이제 이 부대에게도 방향이 생겼습니다.
DIALOGUE_KO: 한승우: 백 중사. 소년이 간 방향, 기록해.
SOUND: gió, bút.
CONTINUITY: Kết P4 track hiện đại. Súng nòng xuống.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_006_facepaint_ep1, WPN_001_ref, LOC_003_hollow_d1
AI_RISK: tay cầm súng → nhặt rồi đeo nòng xuống

### SC_077 | 10:16–10:26 | LOC_001 | GOG_CAVALRYMEN | VEH_205, WPN_201, VEH_101 | PROPS: PROP_021, PROP_012 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial, slow pull-out. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_001_wide: Wide brown Liao River under a cold pale grey sky, three long Sui pontoon bridges of lashed flat boats crossing it, endless Sui army columns and tents to the horizon on the far bank, near bank a flat steppe of dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, early spring, no trees. Action: High aerial two days later: all three pontoon bridges now reach fully to the east bank; Sui columns pour across in ranks under red and yellow banners; on the east bank the Goguryeo line breaks under a rain of arrows and Sui horsemen, and Goguryeo cataphracts pull back east into rolling yellow dust; no faces. Light: Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow pull-out over the crossing. Sound: urgent Sui drums, hooves, a Goguryeo recall horn.
ACTION_START: bridges at east bank, columns crossing
ACTION_END: pulled out, Goguryeo retreating east in dust
NARRATION_KO: 그 사이 요하에서는 두 번째 도하가 준비되고 있었습니다. 다리는 이틀 뒤 다시 놓였습니다. 이번엔 길이가 맞았습니다. 고구려군 만 명이 물가에서 무너졌고, 남은 이들은 요동성으로 물러났습니다.
DIALOGUE_KO: 
SOUND: trống Tùy dồn dập, vó ngựa, tù và Goguryeo thu quân.
CONTINUITY: [史] D3 sáng: cầu nối đủ dài, Goguryeo mất 1만 rút vào thành. Open loop P4.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_205_ref, WPN_201_ref, VEH_101_ref, PROP_021_ref, PROP_012_ref, LOC_001_wide


## [Phần 5] 첫 방아쇠 (10:30–14:00) · trận Tiên Ti vs K21 · narrator im 11:54–13:14 · MID-ROLL 2 @14:00

### SC_078 | 10:26–10:34 | LOC_003 (LOC_003_hollow) | CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium low angle under the netting, static
IMAGE_PROMPT: Medium low angle under the netting, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Late afternoon under green-brown camouflage netting: the small grey quadcopter hovers low over the grassy hollow and climbs; the boyish private stands beneath it with the controller glowing on his chest harness, its corner indicator amber with no digits; four spare batteries still strapped untouched in the pouch on his body armor. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the drone hovers, then climbs out through the netting gap; the private watches it, thumbs on the sticks, and reports one line. Sound: rotors, wind, one line of Korean dialogue.
ACTION_START: drone hovering low, private beneath
ACTION_END: drone gone up through netting, private looking up
NARRATION_KO: 이틀 뒤 오후. 다리가 놓인 지 반나절, 수나라 기병이 동안으로 올라왔습니다.
DIALOGUE_KO: 장태오: 1호기, 배터리 십이 분. 새 건전지는 아낍니다.
SOUND: rotor, gió.
CONTINUITY: D3 chiều: bụi vàng bắt đầu trên lính. Drone #1 pin 12 phút (không sạc).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, UAV_001_ref, LOC_003_hollow_d1
AI_RISK: số pin → 'amber indicator, no digits'

### SC_079 | 10:34–10:42 | LOC_008 (LOC_008_steppe) | CHAR_005, REFUGEES | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen, private's thumb in frame, static
IMAGE_PROMPT: Close-up on the controller screen, private's thumb in frame, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: The controller screen fills the frame with a drone view from height: a long straggling line of Goguryeo refugees on foot across yellow grass — cloth bundles, two-wheeled ox carts, children — and far behind them a black column of smoke from a burned village; the private's thumb trembles on the stick at the edge of frame; no HUD text. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static on the screen: the refugee column crawls across the grass, smoke drifting far behind; the thumb trembles; the private says one line off-camera. Sound: rotor buzz through the speaker, one line of Korean dialogue.
ACTION_START: screen: refugee column, smoke behind
ACTION_END: same, column slightly advanced
NARRATION_KO: 요하 동쪽 마을들은 불탔습니다. 사람들은 성으로 걸었습니다. 성까지는 이틀 길이었습니다.
DIALOGUE_KO: 장태오: 피난민입니다. 삼백쯤… 소달구지도 있습니다.
SOUND: rotor qua loa.
CONTINUITY: LOC_008 1화 = thảo nguyên đoàn dân (sub-lock steppe), KHÔNG dùng lock làng núi.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, LOC_008_steppe_ep1
AI_RISK: đám đông từ trên cao → chấm người, không mặt

### SC_080 | 10:42–10:50 | LOC_008 (LOC_008_steppe) | CHAR_005 | VEH_206 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen, static
IMAGE_PROMPT: Close-up on the controller screen, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: The controller screen: the drone view pans right to show two hundred Xianbei light horsemen — short stocky steppe horses, fur-trimmed caps, bows — sweeping in a wide arc across the yellow grass to cut in ahead of the refugee column, their dust rising in a long band; no HUD text; the private's face reflected faintly in the glass. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static on the screen: the view pans right across the arc of horsemen and their dust band curving ahead of the refugees; fast breathing off-camera; one line. Sound: rotor buzz through the speaker, the private's ragged breathing, one line of Korean dialogue.
ACTION_START: screen: refugee column at left
ACTION_END: screen: horsemen arc and dust band at right
NARRATION_KO: 이백 기. 피난민의 앞을 끊는 데는 충분한 수였습니다. 선비 기병은 앞을 끊고, 옆을 돌고, 뒤에서 쏩니다.
DIALOGUE_KO: 장태오: 기병… 이백. 앞을 끊고 있습니다.
SOUND: rotor; tiếng thở gấp của 태오.
CONTINUITY: VEH_206 Tiên Ti lần đầu (qua màn hình). 200 kỵ.
CHAIN_FROM: SC_079
CUT_HALF: no
REFS: CHAR_005_ref, VEH_206_ref, LOC_008_steppe_ep1
AI_RISK: kỵ binh số đông trên màn hình → aerial, dải bụi

### SC_081 | 10:50–10:58 | LOC_008 (LOC_008_steppe) | CHAR_004, CHAR_005 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium close-up over the private's shoulder onto the screen, static
IMAGE_PROMPT: Medium close-up over the private's shoulder onto the screen, static. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: The controller screen shows the drone view zoomed on a tipped-over two-wheeled ox cart in yellow grass: a girl with two long braids tied with red thread drags an old man with a cloth bundle on his back out from under the cart shaft, the old man dragging one leg; over the boyish private's shoulder the young female medic leans in, one hand rising to her mouth, red cross armband on her left arm. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: on the screen the girl hauls the old man clear of the cart, his leg dragging; the medic's hand comes up to her mouth; nobody speaks. Sound: rotor buzz, a tiny distant scream through the speaker.
ACTION_START: screen: girl pulling old man from cart; medic leaning in
ACTION_END: old man clear of cart on screen; medic's hand at mouth
NARRATION_KO: 선비족 기병이었습니다. 수나라의 눈이자 사냥개였습니다. 정면으로 싸우지 않고, 돌아서 끊는 자들이었습니다.
DIALOGUE_KO: 
SOUND: rotor; tiếng thét rất nhỏ qua loa.
CONTINUITY: 아리 + 을보 lần đầu (qua màn hình, nhỏ — không cần ref chi tiết). 서아 phản ứng.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_ref, CHAR_005_ref, LOC_008_steppe_ep1
AI_RISK: nhân vật trên màn hình nhỏ → chỉ 2 bím tóc đỏ + bọc hành lý làm dấu

### SC_082 | 10:58–11:06 | LOC_003 (LOC_003_hollow) | CHAR_002, CHAR_001 | VEH_004, VEH_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium two-shot beside the command vehicle, static
IMAGE_PROMPT: Medium two-shot beside the command vehicle, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Beside the 4x4 command vehicle: the tall lieutenant, face red, jabs his whole arm at the K2 tank crouched under camouflage netting behind him, shouting; the captain stands motionless, eyes on the controller screen held by the private just out of frame, jaw set. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the lieutenant's arm stabs toward the tank, one loud line; the captain does not move his eyes from the screen. Sound: wind, rotor buzz through a speaker, one loud line of Korean dialogue.
ACTION_START: lieutenant pointing at tank, captain looking at screen
ACTION_END: lieutenant's arm still out, captain unmoved
NARRATION_KO: 오태민에게 답은 늘 하나였습니다. 가장 큰 것을 쓰는 것. 그것은 사실이기도 했습니다.
DIALOGUE_KO: 오태민: 전차 내보냅니다. 한 발이면 다 흩어집니다.
SOUND: gió, rotor qua loa.
CONTINUITY: Tranh cãi 1: 오태민 đòi K2. K2 dưới lưới phía sau.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, CHAR_001_ref, VEH_004_ref, VEH_001_ref, LOC_003_hollow_d1

### SC_083 | 11:06–11:14 | LOC_003 (LOC_003_hollow) | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, slight low angle, static
IMAGE_PROMPT: Medium shot, slight low angle, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The stocky sergeant in a patrol cap leans against the thick side skirt of the K2 tank under the netting, one gloved hand flat on the armor plate as if holding the tank back, and speaks slowly, quietly, to camera-left. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: his palm presses the armor; he speaks one slow quiet line; the hand stays on the plate. Sound: wind, one line of Korean dialogue.
ACTION_START: hand on tank skirt, mouth closed
ACTION_END: hand on tank skirt, line delivered
NARRATION_KO: 박기철에게도 답은 하나였습니다. 기름은 목숨이었습니다. 전차 한 발은 시동 한 번이었고, 시동은 곧 노출이었습니다.
DIALOGUE_KO: 박기철: 나가면 들킵니다. 기름도요.
SOUND: gió.
CONTINUITY: Tay trên váy xích K2 = cử chỉ lặp lại (SC_165, 187).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_003_hollow_d1

### SC_084 | 11:14–11:22 | LOC_003 (LOC_003_hollow) | CHAR_004, CHAR_001 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium two-shot then slow push-in on the captain, single move
IMAGE_PROMPT: Medium two-shot then slow push-in on the captain, single move. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The young female medic says nothing — she looks at the controller screen, then up at the captain; the captain looks at the screen: on it the girl still drags the old man, and the horsemen's dust band is now only a short gap behind the refugee column; the captain's face tightens. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in: the medic's eyes go from the screen to the captain; the captain's eyes stay on the screen, where the dust band closes on the column; the push ends tight on his face; no dialogue. Sound: rotor buzz through the speaker, a faint scream, wind.
ACTION_START: medic looking at screen, captain beside
ACTION_END: tight on the captain's face
NARRATION_KO: 아흔네 명을 데리고 돌아가는 것. 그것이 한승우의 임무였습니다. 화면 속 삼백 명은 임무에 없었습니다.
DIALOGUE_KO: 
SOUND: rotor qua loa, tiếng thét mơ hồ, gió.
CONTINUITY: Không thoại. Chuẩn bị quyết định SC_085.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_ref, CHAR_001_ref, LOC_003_hollow_d1

### SC_085 | 11:22–11:30 | LOC_003 (LOC_003_hollow) | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Close on the captain's face: his eyes leave the screen below, move to the left toward the lieutenant, then to the right toward the sergeant; camouflage netting shadow across his helmet, compass cord at his throat; he speaks one short line without raising his voice. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes off the screen, to the left, to the right, and one short low line; nothing else moves. Sound: the wind stops for a beat, one line of Korean dialogue.
ACTION_START: eyes down on screen
ACTION_END: eyes level, line delivered
NARRATION_KO: 
DIALOGUE_KO: 한승우: 쏜다. 대신 전차는 안 나간다.
SOUND: gió ngừng một nhịp.
CONTINUITY: Direct quote #1: '쏜다. 대신 전차는 안 나간다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_003_hollow_d1

### SC_086 | 11:30–11:38 | LOC_003 (LOC_003_hollow) | CHAR_001, ROK_SOLDIERS | EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static, soldiers running in the background
IMAGE_PROMPT: Medium shot, static, soldiers running in the background. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The captain presses the radio handset on his left shoulder strap, eyes fixed south-east over the netting; behind him helmeted soldiers of a platoon sprint through the yellow grass toward two K21 IFVs under netting, seen from behind, faces hidden. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: handset pressed, one radio order spoken to the south-east; soldiers stream past behind him toward the vehicles. Sound: push-to-talk click, boots on grass, one line of Korean dialogue.
ACTION_START: handset pressed, soldiers starting to run
ACTION_END: order given, last soldiers passing behind
NARRATION_KO: 전차는 남았습니다. 쏘되, 가장 큰 것은 숨긴다. 그것이 첫 결정의 모양이었습니다.
DIALOGUE_KO: 한승우: 천둥 2, 3. 1소대 탑승. 팔백 미터, 정지 사격.
SOUND: PTT, giày chạy trên cỏ.
CONTINUITY: Lệnh: 천둥 2, 3 + 1소대, 800 m. Lính sau lưng.
CHAIN_FROM: SC_085
CUT_HALF: no
REFS: CHAR_001_ref, EQP_002_ref, LOC_003_hollow_d1

### SC_087 | 11:38–11:46 | LOC_003 (LOC_003_hollow) | CHAR_003, ROK_SOLDIERS | VEH_002, VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static, from the rim of the hollow
IMAGE_PROMPT: Wide, static, from the rim of the hollow. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Two K21 IFVs (white numerals 2 and 3 on their turrets) burst up out of the grassy hollow tearing camouflage netting off their hulls, rear ramps closing on the last soldiers jumping in; the K2 tank stays crouched under its netting; the stocky sergeant stands beside the tank watching the two vehicles go, red rag at his belt. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the two IFVs lurch up out of the hollow, netting sliding off, ramps rising, dust boiling behind them; the tank does not move; the sergeant beside it watches. Sound: two diesel engines roaring, tracks tearing grass.
ACTION_START: IFVs starting to move, netting still on
ACTION_END: IFVs clear of the hollow, tank still under netting
NARRATION_KO: 한승우의 첫 번째 결정이었습니다. 그 결과는 이 부대를 끝까지 따라갈 것이었습니다.
DIALOGUE_KO: 
SOUND: hai động cơ K21 gầm, xích nghiến cỏ.
CONTINUITY: Narrator im lặng từ 11:54 (SC_089). K2 ở lại (quyết định 1). CUT_HALF khối trận P5 từ đây.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_003_ref, VEH_002_ref, VEH_001_ref, LOC_003_hollow_d1
AI_RISK: 2 xe + lính nhảy lên → wide, lính nhỏ

### SC_088 | 11:46–11:54 | LOC_008 (LOC_008_steppe) | CHAR_002 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Low lateral tracking shot alongside the moving vehicles
IMAGE_PROMPT: Low lateral tracking shot alongside the moving vehicles. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: Two K21 IFVs race side by side across the yellow steppe, dust boiling off their tracks; the tall lieutenant rides half out of the commander's hatch of the lead vehicle (white numeral 2), goggles now pulled down over his eyes, the small turret's 40mm autocannon swinging to the right. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera tracks low alongside the two racing IFVs: dust streaming, the lieutenant braced in the hatch with goggles down, the turret traversing right; single lateral move. Sound: engines, tracks, wind roaring.
ACTION_START: IFVs entering frame at speed
ACTION_END: IFVs abreast of camera, turret turned right
NARRATION_KO: 팔백 미터. 화살이 닿지 않는 거리였습니다.
DIALOGUE_KO: 
SOUND: động cơ, xích, gió lùa.
CONTINUITY: Kính bảo hộ KÉO XUỐNG (khác mọi cảnh khác). 천둥 2 dẫn đầu.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, LOC_008_steppe_ep1
AI_RISK: 2 xe chạy + người → tracking 1 chiều, bụi che chi tiết xích

### SC_089 | 11:54–12:02 | LOC_008 (LOC_008_steppe) | CHAR_205 | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Lateral tracking shot at rider's height
IMAGE_PROMPT: Lateral tracking shot at rider's height. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: The Xianbei commander gallops at the head of his light horsemen across the yellow grass — pale scar from temple to jaw, fox-fur brimmed cap, single thick braid flying, composite bow in hand — twisting in the saddle to look back at the head of the refugee column, then raising the bow overhead to signal a flanking sweep; riders and dust behind him. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera tracks beside the galloping commander: he looks back over his shoulder toward the refugees, then raises the bow high and sweeps it sideways; riders behind peel off in the direction of the bow. Sound: massed hooves, a high ululating cry from the riders.
ACTION_START: commander galloping, looking back
ACTION_END: bow raised in signal, riders peeling off
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: vó ngựa dồn, tiếng hú của kỵ binh.
CONTINUITY: 탁발흠 base lock (mũ lông còn, trước trận). KHÔNG áo choàng da sói (không trong lock — ghi proposals).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, VEH_206_ref, LOC_008_steppe_ep1
AI_RISK: kỵ binh phi nước đại + cận → 1 kỵ sĩ rõ, còn lại bụi

### SC_090 | 12:02–12:10 | LOC_008 (LOC_008_hill) | CHAR_002 | VEH_002 | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Medium close-up at the commander's hatch, static
IMAGE_PROMPT: Medium close-up at the commander's hatch, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: The K21 IFV (white numeral 2) brakes hard on a low grassy rise, dust rolling over it; the tall lieutenant crouches in the open commander's hatch, one hand pressing his headset, binoculars in the other raised toward horsemen eight hundred meters away, giving a fire order to the gunner below; goggles pushed up again. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the vehicle rocks to a stop, dust washing over the hull; the lieutenant presses the headset, raises binoculars, and speaks one crisp fire order. Sound: brakes, tracks halting, push-to-talk click, one line of Korean dialogue.
ACTION_START: vehicle braking, dust rising
ACTION_END: lieutenant with binoculars up, order given
NARRATION_KO: 
DIALOGUE_KO: 오태민: 포수, 선두 전방 오십. 점사.
SOUND: phanh, xích dừng, PTT.
CONTINUITY: Lệnh nội bộ xe. Xe dừng trên gò.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, PROP_006_ref, LOC_008_steppe_ep1

### SC_091 | 12:10–12:18 | LOC_008 (LOC_008_steppe) | — | VEH_002, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from behind the IFV toward the horsemen, static
IMAGE_PROMPT: Wide from behind the IFV toward the horsemen, static. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: Wide from behind the K21 IFV on the rise: its short 40mm autocannon fires a burst and a row of earth geysers erupts fifty meters in front of the leading Xianbei horsemen; horses rear and throw riders, the ranks behind pile into the leaders, dust and clods flying; no wounded shown. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: three sharp bursts from the autocannon, three earth columns erupt ahead of the horsemen, horses rear, riders spill, the formation crumples on itself in dust. Sound: three hard 40mm reports, earth raining down, horses screaming.
ACTION_START: horsemen charging in line, gun about to fire
ACTION_END: earth geysers, horses rearing, formation collapsing
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: 40mm nổ đanh ba phát, đất văng, ngựa hí.
CONTINUITY: Bắn chặn trước mũi. Không thương vong cận.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, VEH_206_ref, LOC_008_steppe_ep1
AI_RISK: ngựa ngã số đông → wide xa, bụi che, không cận

### SC_092 | 12:18–12:26 | LOC_008 (LOC_008_steppe) | — | VEH_002, VEH_206, WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-high aerial, single slow drift  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Medium-high aerial, single slow drift. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: From medium height: the Xianbei formation shatters into wheeling clusters, panicked horses bolting back through their own ranks; from the roofs of the two K21 IFVs, light machine guns lay bright tracer streaks flat across the grass; dust blankets everything; no faces. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: One slow aerial drift over the chaos: tracer lines streaking across the grass from the two vehicles, horses wheeling, dust spreading; the lieutenant's voice on the radio, one line. Sound: long machine-gun bursts, a second autocannon burst, horses, push-to-talk.
ACTION_START: formation breaking, first tracers
ACTION_END: dust over everything, tracers still streaking
NARRATION_KO: 
DIALOGUE_KO: 오태민: 수레로 전진!
SOUND: K3 quét dài, 40mm loạt thứ hai, ngựa, PTT.
CONTINUITY: 오태민 thoại off (radio). Tracer = vệt sáng.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, VEH_206_ref, WPN_003_ref, LOC_008_steppe_ep1

### SC_093 | 12:26–12:34 | LOC_008 (LOC_008_hill) | CHAR_205 | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: The Xianbei commander hauls his stocky horse to a rearing halt at the foot of a grassy hill; he does not look at the sky — he stares straight at the two dark vehicle shapes on the distant rise — then bellows an order and wrenches his horse around toward the hillside on the right; surviving riders stream after him. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the horse rears and lands, the commander's eyes lock on the distant vehicles, he shouts one hoarse line and yanks the horse around uphill; riders pour past following him. Sound: horse screaming, one hoarse shouted line of Korean dialogue, distant machine-gun fire.
ACTION_START: horse rearing, commander staring at vehicles
ACTION_END: commander wheeling uphill, riders following
NARRATION_KO: 
DIALOGUE_KO: 탁발흠: 흩어져라! 언덕으로!
SOUND: ngựa hí, lệnh hét khàn, K3 xa.
CONTINUITY: Base lock vẫn còn mũ lông (mất mũ sau — SC_101+). 40 kỵ mất.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, VEH_206_ref, LOC_008_steppe_ep1

### SC_094 | 12:34–12:42 | LOC_008 (LOC_008_steppe) | CHAR_004, CHAR_106, CHAR_107, ROK_SOLDIERS | VEH_002 | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium-wide at the overturned cart, static
IMAGE_PROMPT: Medium-wide at the overturned cart, static. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, someone else's blood on the right sleeve, walking staff, frightened exhausted face. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A coarse hemp scarf over the head, yellow dust on clothes and face, tear tracks through the dust, one straw sandal broken, clutching a basket, frightened. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: Beside a tipped two-wheeled ox cart in yellow grass, helmeted soldiers fan out into a ring seen from behind; the young female medic kneels over the old man's blood-soaked lower leg, trauma shears cutting away his hemp trouser leg, medic bag open beside her; the girl in braids tied with red thread clutches the medic's sleeve, talking fast; a K21 IFV idles beyond. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the shears cut through the trouser leg, the medic's hands work fast; the girl tugs at her sleeve and cries out one line; the soldiers around hold their ring. Sound: boots in grass, shears cutting cloth, a child crying far off, one line of Korean dialogue.
ACTION_START: medic kneeling to the leg, girl grabbing sleeve
ACTION_END: trouser cut open, girl's line, medic's hands on the wound
NARRATION_KO: 
DIALOGUE_KO: 아리: 할아버지 다리요! 피가 안 멈춰요!
SOUND: giày trên cỏ, kéo cắt vải, tiếng khóc trẻ con xa.
CONTINUITY: 을보 refugee_ep1 + 아리 refugee_ep1 lần đầu cận. Máu ở chân 을보 (medium, không cận vết thương).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_004_ref, CHAR_106_refugee_ep1, CHAR_107_refugee_ep1, VEH_002_ref, PROP_009_ref, LOC_008_steppe_ep1
AI_RISK: 3 mặt + máu → medium, máu chỉ trên vải quần, không vết thương cận

### SC_095 | 12:42–12:52 | LOC_008 (LOC_008_steppe) | CHAR_004, CHAR_106 | — | PROPS: PROP_009 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up on hands, slow push-in
IMAGE_PROMPT: Still for ken-burns: close-up on hands, slow push-in. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Blue nitrile gloves stained with fresh blood, a few loose strands of hair escaping the bun, fine yellow dust on helmet. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, someone else's blood on the right sleeve, walking staff, frightened exhausted face. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: Close on hands: the medic's blue nitrile gloves, streaked with blood, cinch a white pressure bandage tight around an old man's calf above a hemp trouser hem and straw sandal; a huge gnarled calloused old hand comes down and rests on top of her gloved hand; yellow grass around. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push-in on the two hands. Sound: wind, breathing, an idling engine far off.
ACTION_START: bandage being cinched, old hand arriving
ACTION_END: tight on old hand over gloved hand
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: gió, thở, xa xa động cơ K21.
CONTINUITY: Không thoại. Từ đây 을보 = bandaged (băng trắng chân phải).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_004_ref, CHAR_106_refugee_ep1, PROP_009_ref, LOC_008_steppe_ep1
AI_RISK: tay cận → 2 bàn tay tĩnh, găng xanh + tay già

### SC_096 | 12:52–13:00 | LOC_003 (LOC_003_hollow) | CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on face and screen under the netting, static
IMAGE_PROMPT: Close-up on face and screen under the netting, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: Under the camouflage netting the boyish private hunches over the controller: on its screen the drone view follows a stream of horsemen climbing a grassy hillside; he pushes the stick forward and the image sinks lower, the grass growing larger in the frame; his young face lit by the screen, lips pressed tight. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: on the screen the horsemen climb the hill and the view descends toward them, grass swelling in the frame; the private says one line through his teeth. Sound: rotor buzz, altitude beeps, one line of Korean dialogue.
ACTION_START: screen: horsemen on hill, view high
ACTION_END: screen: view low, grass large, private tense
NARRATION_KO: 
DIALOGUE_KO: 장태오: 저 놈이 우두머리입니다. 따라갑니다.
SOUND: rotor, bíp độ cao.
CONTINUITY: Drone hạ thấp 40 m bám 탁발흠 → sẽ bị bắn (SC_097).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_005_ref, UAV_001_ref, LOC_003_hollow_d1
AI_RISK: màn hình + độ cao → không HUD số

### SC_097 | 13:00–13:08 | LOC_008 (LOC_008_hill) | CHAR_205, XIANBEI_ARCHER | VEH_206, UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the hillside up at the sky, static
IMAGE_PROMPT: Low angle from the hillside up at the sky, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Xianbei horse archer in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow drawn, hip quiver. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: On the grassy hillside among his horsemen the Xianbei commander tilts his head back — forty meters above him a small grey quadcopter hovers, whining; he thrusts a finger up at it; beside him a Xianbei horse archer draws a composite bow to his ear, tracks the drone for a beat, and releases. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the commander looks up and points; the archer beside him draws, tracks the hovering drone, and looses; the arrow streaks up out of frame. Sound: drone rotors close overhead, bowstring snap, arrow hissing.
ACTION_START: commander looking up, archer bow down
ACTION_END: arrow released upward, drone above
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: rotor gần, dây cung bật, tên rít.
CONTINUITY: Cung thủ Tiên Ti = extra. 탁발흠 vẫn base (mũ lông).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, VEH_206_ref, UAV_001_ref, LOC_008_steppe_ep1
AI_RISK: tay cầm cung cận → 1 cung thủ, tư thế chuẩn

### SC_098 | 13:08–13:16 | LOC_003 (LOC_003_hollow) | CHAR_005 | — | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen and face, static
IMAGE_PROMPT: Close-up on the controller screen and face, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_hollow_d1: A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings. Action: The controller screen: the drone image spins violently, a broken orange-tipped propeller blade whips across the lens, yellow grass rushes up — then grey static, then black; the boyish private jams the sticks uselessly, mouth open, eyes wide in the dead screen's dark glow. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the screen image whirls, a propeller fragment flashes past, grass slams up, static, black; the private stabs at the sticks and cries one line. Sound: rotor shrieking off-balance, signal breakup, a lost-link beep, one line of Korean dialogue.
ACTION_START: screen spinning, propeller fragment
ACTION_END: screen black, private's hands frozen on sticks
NARRATION_KO: 
DIALOGUE_KO: 장태오: 1호기… 신호 끊겼습니다.
SOUND: rotor rít lệch, tín hiệu đứt, bíp mất kết nối.
CONTINUITY: Drone #1 mất (4→3).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_005_ref, LOC_003_hollow_d1
AI_RISK: màn hình quay tít → chuỗi 3 hình: quay / nhiễu / đen

### SC_099 | 13:16–13:24 | LOC_008 (LOC_008_steppe) | CHAR_004, ROK_SOLDIERS | VEH_002 | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium shot behind the IFV's rear ramp, static, no wound close-ups
IMAGE_PROMPT: Medium shot behind the IFV's rear ramp, static, no wound close-ups. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Blue nitrile gloves stained with fresh blood, a few loose strands of hair escaping the bun, fine yellow dust on helmet. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: In the lee of a K21 IFV (white numeral 3) with its rear ramp down, two helmeted soldiers are dragged into cover by comrades — one with a Goguryeo arrow through the forearm sleeve, one with a shaft in the thigh, both seen at medium distance with faces turned away; the young female medic, calm, knots an orange tourniquet high on the thigh; arrows drop sparsely in the grass around the vehicle. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium: the two wounded are hauled behind the ramp, the medic cinches the orange tourniquet and pulls it tight, an arrow drops into the grass nearby; a shouted command off-screen. Sound: arrows falling sporadically, a groan, a shouted 'up!' in Korean off-screen.
ACTION_START: wounded being dragged in, medic reaching for tourniquet
ACTION_END: tourniquet knotted, medic looking up
NARRATION_KO: 총이 있어도, 화살은 여전히 피를 냈습니다. 방탄복은 가슴만 가렸습니다.
DIALOGUE_KO: 
SOUND: tên rơi lác đác quanh xe, rên, lệnh "올려!".
CONTINUITY: 2 thương binh (tổng 2). Không cận vết thương. Mặt lính quay đi.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_004_ref, VEH_002_ref, PROP_009_ref, LOC_008_steppe_ep1
AI_RISK: thương binh + tên cắm → medium, không máu cận, mặt quay đi

### SC_100 | 13:24–13:32 | LOC_008 (LOC_008_steppe) | CHAR_106, CHAR_107, ROK_SOLDIERS | VEH_002, WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the open rear ramp of the IFV, static
IMAGE_PROMPT: Medium shot at the open rear ramp of the IFV, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A coarse hemp scarf over the head, yellow dust on clothes and face, tear tracks through the dust, one straw sandal broken, clutching a basket, frightened. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_008_steppe_ep1: Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees. Action: At the lowered rear ramp of a K21 IFV: a helmeted soldier supports the old man with the bandaged leg and the bundle on his back, the girl in red-threaded braids close behind hugging her basket; an arrow strikes the steel hull beside the old man's shoulder with a clang — he does not flinch; he stops, lays his huge calloused palm flat on the armor plate and strokes it like a horse's neck, left eye squinting; the soldier beside him fires a short burst toward the hillside, rifle at the shoulder. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the arrow clangs off the hull; the old man halts, sets his palm on the steel and strokes it slowly, squinting; the soldier beside him fires a short burst uphill; the old man says one line and steps onto the ramp. Sound: arrow on steel, a short rifle burst, engine idling, a palm on steel, one line of Korean dialogue.
ACTION_START: old man arriving at ramp, arrow striking hull
ACTION_END: old man's palm on the armor, line spoken, foot on ramp
NARRATION_KO: 을보 영감, 요동성의 대장장이. 쇠를 만지는 것은 그의 인사였습니다. 그는 쇠를 만지고 나서야 사람을 믿었습니다.
DIALOGUE_KO: 을보: 이 쇠는… 우리 쇠가 아니야.
SOUND: tên đập thép, K2C1 loạt ngắn, động cơ xe chờ, bàn tay trên thép.
CONTINUITY: 을보 'chạm sắt' = nghi lễ (lặp SC_256). Băng trắng chân. Lính bắn = extra sau/nghiêng, súng ở vai.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_106_refugee_ep1, CHAR_107_refugee_ep1, VEH_002_ref, WPN_001_ref, LOC_008_steppe_ep1
AI_RISK: tay cầm súng bắn → lính phụ nghiêng, súng ở vai, chớp lửa nhỏ; tay 을보 trên thép là hành động chính

### SC_101 | 13:32–13:42 | LOC_008 (LOC_008_hill) | CHAR_205, XIANBEI_ARCHER | VEH_206, VEH_002 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide of the hillside, pulling out from arrows in the grass to the commander  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide of the hillside, pulling out from arrows in the grass to the commander. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Xianbei horse archer in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow drawn, hip quiver. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: Wide on the yellow hillside: the Xianbei commander, now bareheaded with his braid exposed and dust over his armor, stands dismounted among his remaining horsemen; on his signal a line of Xianbei archers looses a test volley toward two K21 IFVs turning away east on the plain below — the arrows fall in a clump into the grass far short of the vehicles; riderless horses scatter across the flat, dust thinning. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): from the clump of arrows stuck in the grass, slow pull-out up the hill to the commander. Sound: massed bowstrings, arrows falling into grass far off, wind, a horse whinnying.
ACTION_START: arrows in the grass
ACTION_END: wide: commander on hill, vehicles far below
NARRATION_KO: 탁발흠은 기병 마흔을 잃었습니다. 그는 물러나지 않았습니다. 화살 한 줄을 쏘게 했습니다. 닿지 않았습니다. 그것도 배움이었습니다. 살아남은 백육십 기는 언덕 위에서 쉬었습니다.
DIALOGUE_KO: 
SOUND: dây cung hàng loạt, tên rơi cỏ xa, gió, ngựa hí.
CONTINUITY: Từ đây 탁발흠 = survivor_ep1 (mất mũ, máu tai trái). Loạt tên thử — hụt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, VEH_206_ref, VEH_002_ref, LOC_008_steppe_ep1

### SC_102 | 13:42–13:50 | LOC_008 (LOC_008_hill) | CHAR_205 | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, static
IMAGE_PROMPT: Medium close-up, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: The Xianbei commander walks to a patch of flattened grass, bends, and lifts the wrecked grey quadcopter by one snapped arm, turning it slowly before his face — broken orange-tipped propellers, a dangling gimbal camera — a line of dried blood running from his left ear down his neck; he raises his eyes past the drone toward the distant vehicles: no fear, only memorizing. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he bends, lifts the broken drone by its arm, turns it slowly before his face, then lifts his eyes over it toward the plain and holds; no dialogue. Sound: cracked plastic creaking, wind.
ACTION_START: bending to the drone in the grass
ACTION_END: drone held up, eyes fixed on the distant vehicles
NARRATION_KO: 그는 이름을 붙이지 않았습니다. 먼저 살펴보았습니다. 요술이라 부르는 자는 배우지 못하는 법이었습니다.
DIALOGUE_KO: 
SOUND: nhựa gãy kêu, gió.
CONTINUITY: Xác drone #1 → prop lặp lại (SC_104, 131–134, 272, 282–288).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, UAV_001_ref, LOC_008_steppe_ep1
AI_RISK: tay cầm vật → 1 tay, drone gãy rõ hình

### SC_103 | 13:50–14:00 | LOC_008 (LOC_008_hill) | CHAR_205, REFUGEES | UAV_001, VEH_002 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide from the plain, slow push toward a figure on the hill  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide from the plain, slow push toward a figure on the hill. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: Wide: on the yellow hillside the Xianbei commander is a small standing figure holding the wrecked drone; below on the plain the refugee column re-forms and moves east on foot with its ox carts, two K21 IFVs rolling along either flank, dust drifting; late silver sun. Light: Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push from the refugee column up toward the small figure on the hill. Sound: wind.
ACTION_START: wide: column and vehicles, hill above
ACTION_END: tight on the figure with the drone
NARRATION_KO: 쇠수레 둘. 사람은 백 남짓. 탁발흠은 도망치지 않았습니다. 언덕에서, 그는 세고 있었습니다.
DIALOGUE_KO: 
SOUND: gió.
CONTINUITY: Mid-roll 2 @14:00 sau cảnh này. Open loop P5.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, UAV_001_ref, VEH_002_ref, LOC_008_steppe_ep1


## [Phần 6] 어느 성의 군사요 (14:00–17:30) · 해모루, năm 612, quyết đi đêm

### SC_104 | 14:00–14:08 | LOC_008 (LOC_008_hill) | CHAR_205 | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Extreme close-up on hands and drone, static
IMAGE_PROMPT: Extreme close-up on hands and drone, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_008_steppe_ep1: A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees. Action: Close: the wrecked grey quadcopter turns slowly in the Xianbei commander's scarred hands — snapped propeller, one arm bent, dead LEDs, a tiny Korean flag sticker on the body — against an orange-grey sunset sky; his leather-armored forearms and bronze plaque belt at the frame edge, no face. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the hands turn the drone slowly one full rotation, a fingertip touching the tiny flag sticker; no dialogue, no narration. Sound: wind, plastic creaking softly.
ACTION_START: drone in hands, flag sticker hidden
ACTION_END: drone turned, flag sticker under fingertip
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: gió, nhựa gãy kêu khẽ.
CONTINUITY: Sau mid-roll 2: không thoại, không narration. Tem 태극기 nhỏ trên drone.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, UAV_001_ref, LOC_008_steppe_ep1
AI_RISK: tay cận cầm drone → 2 tay, xoay chậm

### SC_105 | 14:08–14:18 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105, BOY_SCOUT, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_012 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide of a cavalry line on a ridge, backlit, slow lateral pull along the line  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide of a cavalry line on a ridge, backlit, slow lateral pull along the line. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: On a low grassy ridge against the setting sun three hundred Goguryeo cataphracts stand in line, horses in iron lamellar barding, red-plumed helmets, black three-legged crow banners; at the center the clean-shaven Goguryeo officer with a single white feather on his helmet sits his horse, dust on his armor; beside his stirrup the boy scout stands pointing down the slope; the riders silhouetted, faces lost in backlight. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow lateral drift along the cavalry line toward the officer and the boy. Sound: horses blowing, armor clinking, evening wind.
ACTION_START: cavalry line, officer at center
ACTION_END: tight on officer and boy pointing
NARRATION_KO: 해 질 무렵, 삼백 기가 언덕에 섰습니다. 소년이 길을 안내했습니다. 쇠로 된 집이라는 말을 확인하러 온 것이었습니다. 삼백 기 앞에 선 것은 쇠수레 셋과 아흔네 명이었습니다.
DIALOGUE_KO: 
SOUND: ngựa thở, giáp lách cách, gió chiều.
CONTINUITY: 해모루 lần đầu (dusty_ep1, không râu, 1 lông trắng). 300 kỵ = silhouette ngược sáng.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, EXTRA_boy_scout_ref, VEH_101_ref, PROP_012_ref, LOC_003_hollow_d1
AI_RISK: 300 kỵ → ngược sáng, silhouette, chỉ 해모루 rõ

### SC_106 | 14:18–14:26 | LOC_003 (LOC_003_ridge_sunset) | CHAR_002, ROK_SOLDIERS | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Over-the-shoulder from behind the lieutenant on the IFV roof, looking up at the ridge, static
IMAGE_PROMPT: Over-the-shoulder from behind the lieutenant on the IFV roof, looking up at the ridge, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: From behind the tall lieutenant on the roof of a K21 IFV, headset pressed to one ear: below the ridge three K21 IFVs stand abreast with their 40mm barrels lowered, helmeted soldiers crouched behind the hulls; on the ridge above, the line of Goguryeo cavalry is a row of dark silhouettes against the sunset. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static over-the-shoulder: the lieutenant presses the headset and says one line, eyes locked on the ridge; the silhouettes on the ridge do not move; the engines idle. Sound: engines idling, push-to-talk click, one line of Korean dialogue.
ACTION_START: lieutenant looking up at ridge
ACTION_END: same, line delivered, barrels lowered
NARRATION_KO: 삼백 기, 사거리 안. 오태민의 셈은 늘 그렇게 시작했습니다. 그에게 사거리 안은 곧 표적이었습니다.
DIALOGUE_KO: 오태민: 중대장님, 삼백입니다. 사거리 안입니다.
SOUND: động cơ chờ, PTT.
CONTINUITY: Thuốc súng trên cẳng tay 오태민 (powder_ep1) từ sau trận.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_107 | 14:26–14:34 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001 | VEH_002, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-wide from the side, static
IMAGE_PROMPT: Medium-wide from the side, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The captain stands alone in the open ground in front of the nose of a K21 IFV (white numeral 3), the radio handset in his left hand, his right arm swept back level toward the vehicles in a hold signal; behind him the IFV's 40mm barrel dips lower still; the cavalry ridge glows in sunset beyond. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the captain's right arm sweeps back in the hold signal and stays; he presses the handset and gives one order; the barrel behind him dips lower. Sound: push-to-talk click, turret motor whirring down, one line of Korean dialogue.
ACTION_START: captain stepping into open ground, arm rising
ACTION_END: arm level back, barrel down, order given
NARRATION_KO: 한승우의 셈은 달랐습니다. 이들은 서쪽의 그들이 아니었습니다. 쏘지 않는 것이 그날 두 번째 결정이었습니다.
DIALOGUE_KO: 한승우: 전 차량, 포신 내려. 사격 금지.
SOUND: PTT, tháp pháo quay hạ.
CONTINUITY: Quyết định 2: không bắn. 한승우 một mình giữa khoảng trống.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_002_ref, EQP_002_ref, LOC_003_hollow_d1

### SC_108 | 14:34–14:42 | LOC_003 (LOC_003_ridge_sunset) | CHAR_106 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-wide, static, low angle from the open ground
IMAGE_PROMPT: Medium-wide, static, low angle from the open ground. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The old blacksmith limps out into the open ground between the two lines, white bandage on his lower leg, bundle on his back, and raises both arms toward the ridge, shouting up at it in the hoarse voice of an old man afraid of nothing; the sunset behind the ridge. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he limps forward into the open, plants his feet, raises both arms and shouts one line up at the ridge; the arms stay up. Sound: wind, one hoarse shouted line of Korean dialogue echoing.
ACTION_START: old man limping into the open
ACTION_END: both arms raised, line shouted
NARRATION_KO: 을보 영감이 먼저 나섰습니다. 예순여섯 살 노인에게 두 군대 사이는 무섭지 않았습니다. 이들이 손녀를 살렸기 때문입니다.
DIALOGUE_KO: 을보: 이들이 우릴 살렸소!
SOUND: gió, tiếng gào vang.
CONTINUITY: Băng trắng chân phải (bandaged_ep1).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_refugee_ep1, LOC_003_hollow_d1

### SC_109 | 14:42–14:50 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105 | VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot tracking the officer walking downhill, slow push-in at the end
IMAGE_PROMPT: Medium shot tracking the officer walking downhill, slow push-in at the end. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The Goguryeo officer with the single white feather swings down from his armored horse, tosses the reins to a rider, and walks down the slope alone, hands nowhere near his sword hilt; he stops three paces from the camera — his eyes fixed on a small red-and-blue flag patch on the right shoulder of the man in front of him, out of focus in the foreground. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera holds as he dismounts, then pushes in slowly as he walks down the slope and stops, his eyes dropping to the shoulder patch in the blurred foreground. Sound: leather boots on grass, armor clinking.
ACTION_START: officer dismounting on the ridge
ACTION_END: officer stopped three paces away, eyes on the patch
NARRATION_KO: 해모루 말객. 을지문덕 장군의 사람이었습니다. 칼보다 질문을 먼저 꺼내는 사람이었습니다. 그는 이날 처음으로 답이 없는 질문을 하게 됩니다.
DIALOGUE_KO: 
SOUND: giày da trên cỏ, giáp lách cách.
CONTINUITY: Mặt 해모루 rõ; 한승우 chỉ là vai áo mờ tiền cảnh.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, VEH_101_ref, LOC_003_hollow_d1

### SC_110 | 14:50–14:58 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105, CHAR_006, BOY_SCOUT | VEH_002 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Wide three-figure shot, static
IMAGE_PROMPT: Wide three-figure shot, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. 17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The boy scout runs down the slope and stops behind the Goguryeo officer, arm thrust out pointing at the staff sergeant in a boonie hat standing beside a K21 IFV's track, the arrow the boy got back still clenched in his fist; the officer half turns to follow the pointing arm. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the boy runs in and stops behind the officer, points at the sergeant by the vehicle, and says one line; the officer's head turns to look. Sound: running feet on grass, fast breathing, one line of Korean dialogue.
ACTION_START: boy running down, officer standing
ACTION_END: boy pointing at sergeant, officer turned
NARRATION_KO: 소년은 약속을 지켰습니다. 그것이 첫 번째 신용이었습니다. 화살을 돌려준 자는 적이 아니었습니다. 소년의 법이었습니다.
DIALOGUE_KO: 소년 척후: 저 사람이오. 화살을 돌려준 사람.
SOUND: gió, thở gấp.
CONTINUITY: Cậu bé giữ lời (mũi tên trong tay).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, CHAR_006_facepaint_ep1, EXTRA_boy_scout_ref, VEH_002_ref, PROP_015_ref, LOC_003_hollow_d1

### SC_111 | 14:58–15:06 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Close on the Goguryeo officer's clean-shaven angular face under the iron helmet with its single white feather: his eyes rise from a shoulder patch below the frame to meet the camera at eye level, even and unreadable, dust on his cheekbones, sunset rim light on the helmet. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the eyes lift from below to the lens and he speaks one even line, neither hostile nor warm. Sound: wind, one line of Korean dialogue.
ACTION_START: eyes down on the patch
ACTION_END: eyes level, line delivered
NARRATION_KO: 
DIALOGUE_KO: 해모루: 삼족오가 아니오. 그대들은 어느 성의 군사요?
SOUND: gió.
CONTINUITY: Direct quote #3: '삼족오가 아니오. 그대들은 어느 성의 군사요?'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, LOC_003_hollow_d1

### SC_112 | 15:06–15:14 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Close on the captain's face: one silent beat — his eyes go down the line of three K21 IFVs behind him, then return to the man in front of him; the compass cord at his throat, the sunset on one side of his face; he answers honestly. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes travel to the vehicles and back, a held beat, then one quiet halting line. Sound: wind, a horse whinnying far off, one line of Korean dialogue.
ACTION_START: eyes moving toward the vehicles
ACTION_END: eyes back on the officer, line spoken
NARRATION_KO: 성이 없다. 이 시대에 그것은 군대가 아니라는 뜻이었습니다. 성이 없는 자는 어디에도 속하지 않는 자였습니다.
DIALOGUE_KO: 한승우: 성이… 없습니다.
SOUND: gió, xa xa ngựa hí.
CONTINUITY: '성이… 없습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_113 | 15:14–15:22 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, slow pan following his gaze then back, single move
IMAGE_PROMPT: Medium shot, slow pan following his gaze then back, single move. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The Goguryeo officer's eyes travel along the flank of the nearest K21 IFV — the folded flotation panels, the road wheels, the short 40mm barrel — then swing back to fix on the captain in front of him; he asks his question like an interrogator who does not need to raise his voice. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow pan along the vehicle's flank following the officer's gaze, then back to his face as it locks forward and he asks one line. Sound: armor clinking, one line of Korean dialogue.
ACTION_START: officer's eyes on the vehicle flank
ACTION_END: officer facing forward, question asked
NARRATION_KO: 해모루는 쇠수레보다 사람을 먼저 보았습니다. 어디서 왔는지가 무엇을 가졌는지보다 중요했습니다. 그가 을지문덕에게 보고할 것도 그것이었습니다.
DIALOGUE_KO: 해모루: 그대들은 어디서 왔소?
SOUND: giáp lách cách.
CONTINUITY: '그대들은 어디서 왔소?'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_114 | 15:22–15:30 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Close-up with the ridge soft behind, static
IMAGE_PROMPT: Close-up with the ridge soft behind, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Close on the captain: he does not answer the question — his eyes move from the line of lamellar-armored cavalry on the ridge to a black three-legged crow banner, then west toward where the boy pointed; his lips shape words silently one by one like sums, and then he says the result aloud. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the eyes go to the cavalry, to the banner, to the west; lips move silently; then one line spoken slowly, the last word landing. Sound: wind, whispering under breath, one line of Korean dialogue.
ACTION_START: eyes on the cavalry line
ACTION_END: line spoken, eyes back to the officer
NARRATION_KO: 한승우는 대답 대신 셈을 했습니다. 수나라, 백만, 요동성. 학교에서 배운 세 단어였습니다. 세 단어가 가리키는 해는 하나뿐이었습니다.
DIALOGUE_KO: 한승우: 수나라… 백만… 요동성. 육백십이 년.
SOUND: gió, thì thầm.
CONTINUITY: 한승우 tự suy năm: '수나라… 백만… 요동성. 육백십이 년.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_101_ref, PROP_012_ref, LOC_003_hollow_d1

### SC_115 | 15:30–15:38 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Close on the Goguryeo officer: his brow knits — the number means nothing to him — and he answers with his own calendar, slowly, each word distinct, like correcting a man who has misspoken; white feather stirring in the evening wind. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the brow creases, then he speaks one slow deliberate line, correcting. Sound: wind, one line of Korean dialogue.
ACTION_START: brow knitting
ACTION_END: line delivered, face settled
NARRATION_KO: 해모루는 이 땅의 달력으로 답했습니다. 왕의 이름이 아니라, 왕의 햇수였습니다. 그것이 확인이었습니다.
DIALOGUE_KO: 해모루: 대왕 재위 이십삼 년이오.
SOUND: gió.
CONTINUITY: '대왕 재위 이십삼 년이오.' — không 시호 (decisions).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, LOC_003_hollow_d1

### SC_116 | 15:38–15:46 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001, CHAR_003 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot beside the IFV, static
IMAGE_PROMPT: Medium two-shot beside the IFV, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Beside the K21 IFV's track the captain turns half around to the stocky sergeant standing close behind him and says something very low, almost to himself; the sergeant looks at him blankly — then his broad face changes. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the captain half turns and murmurs one line; the sergeant's face is blank for a beat, then his eyes widen. Sound: wind, a whispered line of Korean dialogue.
ACTION_START: captain turning to sergeant
ACTION_END: sergeant's face changed, captain looking away
NARRATION_KO: 재위 이십삼 년. 한승우의 셈과 같은 해였습니다. 초등학교 교과서의 두 단어가 눈앞에 있었습니다.
DIALOGUE_KO: 한승우: 육백십이년… 살수.
SOUND: gió, tiếng thì thầm.
CONTINUITY: '육백십이년… 살수.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_003_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_117 | 15:46–15:54 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001, GOG_CAVALRYMEN | VEH_101 | PROPS: — | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: close-up looking down at the compass, slow push-in
IMAGE_PROMPT: Still for ken-burns: close-up looking down at the compass, slow push-in. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The captain looks down at the lensatic compass hanging on its cord against his chest armor, its needle steady; behind him, soft and out of focus, the line of armored Goguryeo cavalry on the ridge is a row of silhouettes against the sunset. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow push-in on the compass. Sound: wind.
ACTION_START: captain looking down, ridge soft behind
ACTION_END: tight on compass
NARRATION_KO: 영양왕 23년, 서기 612년. 대한민국 군인이라면 누구나 배운 해였습니다. 살수대첩의 해. 을지문덕, 삼십만 오천, 살아 돌아간 자 이천칠백. 결말을 아는 것과 그 안에서 사는 것은 다른 일이었습니다.
DIALOGUE_KO: 
SOUND: gió.
CONTINUITY: Narrator giải thích 612 (SC_117 N). Payoff la bàn (SC_020).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_101_ref, LOC_003_hollow_d1

### SC_118 | 15:54–16:02 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The Goguryeo officer points at the line of K21 IFVs, then swings his arm east toward the fortress beyond the horizon, speaking as a man who has already decided for the people in front of him; dust on his armor, sunset behind. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the arm points at the vehicles, then swings east; one line delivered with finality. Sound: wind, one line of Korean dialogue.
ACTION_START: arm pointing at vehicles
ACTION_END: arm pointing east, line done
NARRATION_KO: 해모루의 제안은 명령에 가까웠습니다. 성주의 판단, 그것이 이 땅의 법이었습니다.
DIALOGUE_KO: 해모루: 쇠수레를 요동성으로 들이시오. 성주께서 판단하실 것이오.
SOUND: gió.
CONTINUITY: Đề nghị vào thành.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_119 | 16:02–16:10 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The captain shakes his head once, slowly, hands clasped behind his back, feet planted in the yellow grass, sunset lighting one side of his face; he speaks one short flat line. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: one slow head shake, hands stay clasped behind the back, one short line. Sound: wind, one line of Korean dialogue.
ACTION_START: head beginning to shake
ACTION_END: head still, line spoken
NARRATION_KO: 한승우는 성을 알았습니다. 성은 지키는 곳이지, 나가는 곳이 아니었습니다. 전차에게 성벽은 보호가 아니라 감옥이었습니다.
DIALOGUE_KO: 한승우: 성 안은 안 됩니다. 갇힙니다.
SOUND: gió.
CONTINUITY: '성 안은 안 됩니다. 갇힙니다.' Tay chắp sau lưng (identifier).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_003_hollow_d1

### SC_120 | 16:10–16:18 | LOC_003 (LOC_003_ridge_sunset) | CHAR_002 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static, low angle
IMAGE_PROMPT: Medium shot, static, low angle. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The tall lieutenant vaults down from the roof of the K21 IFV, lands hard, strides up beside the captain and thrusts his arm out west toward the sun sitting on the horizon, goggles on his helmet, powder-smudged forearms bare. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he drops from the roof, lands, strides in, and flings his arm west with one loud line; the sun sits on the horizon behind his pointing hand. Sound: boots hitting ground, one loud line of Korean dialogue.
ACTION_START: lieutenant jumping from roof
ACTION_END: arm pointing west at the sun, line delivered
NARRATION_KO: 오태민은 다리를 원했습니다. 다리를 끊으면 백만이 강 저쪽에 묶인다고 믿었습니다. 다리는 셋이었고, 이미 기병이 건너 있었습니다.
DIALOGUE_KO: 오태민: 서쪽으로 갑니다. 다리를 끊으면 끝입니다.
SOUND: giày đập đất.
CONTINUITY: 오태민 đòi đi tây (cắt cầu).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_121 | 16:18–16:26 | LOC_003 (LOC_003_ridge_sunset) | CHAR_003 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, static
IMAGE_PROMPT: Medium close-up, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The stocky sergeant in a patrol cap looks at no one; he opens the small green-covered notebook, reads one line to himself, and closes it; his flat delivery ends the argument; sunset on the salt-and-pepper temple. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: notebook opens, eyes read, notebook closes, one flat line; nothing else. Sound: the notebook snapping shut, wind, one line of Korean dialogue.
ACTION_START: opening notebook
ACTION_END: notebook closed, line spoken
NARRATION_KO: 이틀. 어느 쪽으로 가든 사흘째는 굶는 것이었습니다. 박기철의 숫자는 늘 논쟁을 끝냈습니다.
DIALOGUE_KO: 박기철: 식량 이틀 치입니다. 이틀.
SOUND: sổ gập.
CONTINUITY: '식량 이틀 치입니다. 이틀.' Sổ bìa xanh.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, LOC_003_hollow_d1

### SC_122 | 16:26–16:34 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The Goguryeo officer looks at the sergeant off-frame — he grasps the number even without the words — then turns back to the captain and points west across the darkening plain toward the last band of orange; behind him on the ridge the cavalry line stirs, horses shifting. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: his gaze shifts, returns, his arm points west at the dying light; one line, level, not a threat; cavalry silhouettes shift on the ridge behind. Sound: wind, horses moving on the ridge, one line of Korean dialogue.
ACTION_START: officer looking off toward the sergeant
ACTION_END: arm pointing west, line spoken
NARRATION_KO: 곡식은 성에 있었습니다. 벌판은 내일이면 수나라의 것이었습니다. 해모루는 협박하지 않았습니다. 시간을 말했을 뿐입니다.
DIALOGUE_KO: 해모루: 곡식은 성에 있소. 단, 오늘 밤 안에 떠나야 하오.
SOUND: gió, kỵ binh trên gò chuyển động.
CONTINUITY: '곡식은 성에 있소. 단, 오늘 밤 안에 떠나야 하오.' Hoàng hôn → dusk.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, VEH_101_ref, LOC_003_hollow_d1

### SC_123 | 16:34–16:42 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001, CHAR_002, CHAR_003 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium three-shot, static
IMAGE_PROMPT: Medium three-shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The captain looks at the tall lieutenant (jaw clenched), then at the stocky sergeant (a slight nod), then turns his head east into the dusk; a K21 IFV's hull behind them; he gives one short order. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static three-shot: eyes to the lieutenant, to the sergeant, head turns east, one short order. Sound: wind, one line of Korean dialogue.
ACTION_START: captain looking at lieutenant
ACTION_END: captain facing east, order given
NARRATION_KO: 결정은 배가 내렸습니다. 한승우는 그것을 알면서 명령했습니다. 전차를 맨 뒤에 둔 것은 기름 때문이었습니다. 먼지 때문이기도 했습니다.
DIALOGUE_KO: 한승우: 밤에 이동한다. 전차는 맨 뒤.
SOUND: gió.
CONTINUITY: '밤에 이동한다. 전차는 맨 뒤.' 3 người, 1 nói.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_002_ref, CHAR_003_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_124 | 16:42–16:50 | LOC_003 (LOC_003_ridge_sunset) | CHAR_006, CHAR_105 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot in profile, static
IMAGE_PROMPT: Medium two-shot in profile, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The staff sergeant in a boonie hat with two streaks of face paint stands beside a K21 IFV's track; the Goguryeo officer walks past, checks half a step, and looks at him — two scouts recognizing each other; the officer gives the smallest nod; the sergeant nods back; dusk light. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static profile two-shot: the officer walks into frame, stops half a step, the two men look at each other, one tiny nod each; no words; the officer walks on. Sound: armor clinking, wind, no dialogue.
ACTION_START: officer walking past, sergeant still
ACTION_END: two nods exchanged, officer moving on
NARRATION_KO: 말은 필요 없었습니다. 척후는 척후를 알아보는 법이었습니다. 두 사람은 이후 넉 달을 같은 길에서 보내게 됩니다.
DIALOGUE_KO: 
SOUND: giáp lách cách, gió.
CONTINUITY: Không thoại. 백성민 ↔ 해모루.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, CHAR_105_ref, VEH_002_ref, LOC_003_hollow_d1

### SC_125 | 16:50–16:58 | LOC_003 (LOC_003_ridge_sunset) | CHAR_106, CHAR_001, CHAR_107 | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the IFV's rear ramp, static
IMAGE_PROMPT: Medium shot at the IFV's rear ramp, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A coarse hemp scarf over the head, yellow dust on clothes and face, tear tracks through the dust, one straw sandal broken, clutching a basket, frightened. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The old blacksmith limps toward the lowered rear ramp of a K21 IFV where the girl in red-threaded braids waits hugging her basket; passing the captain he speaks without turning his head, an old man addressing a younger one; dusk, bandaged leg, bundle on his back. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the old man limps past the captain toward the ramp and speaks one line without looking back; the captain's head turns after him; the girl waits at the ramp. Sound: a foot dragging on grass, one line of Korean dialogue.
ACTION_START: old man passing the captain
ACTION_END: old man at the ramp beside the girl, captain looking after him
NARRATION_KO: 을보 영감은 성주를 알았습니다. 이 땅에서 그보다 좋은 소개장은 없었습니다.
DIALOGUE_KO: 을보: 대장 양반, 성주는 내가 아는 사람이야.
SOUND: chân lết trên cỏ.
CONTINUITY: '대장 양반, 성주는 내가 아는 사람이야.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_refugee_ep1, CHAR_001_ref, CHAR_107_refugee_ep1, VEH_002_ref, LOC_003_hollow_d1

### SC_126 | 16:58–17:06 | LOC_003 (LOC_003_ridge_sunset) | GOG_CAVALRYMEN | VEH_001, VEH_002, VEH_003, VEH_004, VEH_101 | PROPS: PROP_012 | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: wide, sun on the horizon, slow lateral slide  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide, sun on the horizon, slow lateral slide. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Wide: the sun touches the horizon; a column of Goguryeo cataphracts forms up leading east, black three-legged crow banners; behind them the modern convoy with nets rolled and stowed — three K21 IFVs, two cargo trucks, the 4x4 command vehicle, and the K2 tank last — all backlit in glowing yellow dust. Light: Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow lateral slide along the forming column from cavalry to tank. Sound: slow hooves, engines starting one after another.
ACTION_START: cavalry head of column
ACTION_END: K2 tank at the tail
NARRATION_KO: 삼백 기가 앞장섰습니다. 쇠수레 일곱 대가 뒤를 따랐습니다. 요동성까지 삼십 킬로. 전차에게는 기름 삼십 킬로였습니다. 밤길 삼십 킬로. 고구려 기병에게는 익숙한 길이었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa chậm, động cơ nổ máy lần lượt.
CONTINUITY: K2 đi cuối (dầu + bụi). 7 xe.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_002_ref, VEH_003_ref, VEH_004_ref, VEH_101_ref, PROP_012_ref, LOC_003_hollow_d1

### SC_127 | 17:06–17:14 | LOC_003 (LOC_003_ridge_sunset) | CHAR_105, CHAR_001 | VEH_101, VEH_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, low angle, static
IMAGE_PROMPT: Medium two-shot, low angle, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: The Goguryeo officer, mounted again on his armored horse, reins it around to look once more at a K21 IFV, curiosity winning over suspicion, and calls a question down to the captain who has one boot on the step of the 4x4 command vehicle; dusk. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the horse turns, the officer's eyes go to the vehicle, then down to the captain, and he asks one line; the captain pauses on the step. Sound: the horse stamping, engines idling, one line of Korean dialogue.
ACTION_START: officer reining around, captain stepping up
ACTION_END: officer asking, captain paused on the step
NARRATION_KO: 해모루는 쇠수레의 속도를 물었습니다. 한승우는 기름을 생각했습니다. 말보다 빠른 것은 확실했습니다. 말보다 오래 달리지는 못했습니다.
DIALOGUE_KO: 해모루: 한 대장. 저 쇠수레, 말보다 빠르오?
SOUND: ngựa dậm chân, động cơ.
CONTINUITY: '한 대장. 저 쇠수레, 말보다 빠르오?'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, CHAR_001_ref, VEH_101_ref, VEH_004_ref, LOC_003_hollow_d1

### SC_128 | 17:14–17:22 | LOC_003 (LOC_003_ridge_sunset) | CHAR_001 | VEH_004 | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Close-up inside the vehicle, static, ending on the compass
IMAGE_PROMPT: Close-up inside the vehicle, static, ending on the compass. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: Inside the 4x4 command vehicle at dusk: the captain sits, unfolds the paper map with its brown contour lines and grease-pencil marks, looks at it one second, folds it and shoves it into a pocket; camera on the lensatic compass on its cord at his chest — needle steady, pointing north. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: map unfolded, a one-second look, folded and pocketed; camera settles on the compass and its steady needle. Sound: paper folding, engine idling.
ACTION_START: map being unfolded
ACTION_END: tight on steady compass needle
NARRATION_KO: 철원의 지도는 이제 종이일 뿐이었습니다. 나침반만이 아직 쓸모가 있었습니다. 그것은 철원에서 가져온 것 중 유일하게 쓸모 있는 것이었습니다.
DIALOGUE_KO: 
SOUND: giấy gấp, động cơ.
CONTINUITY: Không thoại. Bản đồ vô dụng; la bàn = vật duy nhất có ích.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_004_ref, PROP_001_ref, LOC_003_hollow_d1

### SC_129 | 17:22–17:30 | LOC_003 (LOC_003_ridge_sunset) | GOG_CAVALRYMEN | VEH_001, VEH_101 | PROPS: — | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: wide, slow push along a column into darkness  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide, slow push along a column into darkness. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_003_hollow_d1: The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage. Action: A long column — armored cavalry ahead, modern vehicles behind, the K2 tank last — files east into gathering darkness, only a thin band of orange left in the sky behind them, headlights off, dust glowing faintly. Light: Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow push along the column into the dark. Sound: tracks, hooves, night wind.
ACTION_START: column mid-frame, orange band behind
ACTION_END: pushed toward the dark head of the column
NARRATION_KO: 612년 봄. 살수까지는 넉 달이 남아 있었습니다. 한승우는 이 전쟁의 결말을 알고 있었습니다. 문제는, 자신들이 그 결말에 없다는 것이었습니다.
DIALOGUE_KO: 
SOUND: xích, vó ngựa, gió đêm.
CONTINUITY: Kết P6. Open loop.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, VEH_101_ref, LOC_003_hollow_d1


## [Phần 7] 쇠집은 문을 못 지난다 (17:30–21:00) · trại Tùy, hành quân đêm, 요동성 · MID-ROLL 3 @21:00

### SC_130 | 17:30–17:40 | LOC_001 (LOC_001_sui_camp_night) | — | WPN_201 | PROPS: PROP_016, PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high wide over a night camp, slow push toward the general's tent  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high wide over a night camp, slow push toward the general's tent. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_001_wide: Sui vanguard camp on the east bank of the Liao River at night: grid rows of grey felt tents, lines of burning torches, red and yellow banners with black tassels on black lacquered poles, a large general's tent in the center, wooden watchtowers, horse lines, the three pontoon bridges glittering with torches on the wide black river beyond. Action: Night on the east bank of the Liao River: a Sui vanguard camp in grid rows of grey felt tents, lines of torches, red and yellow banners, a large general's tent at the center glowing from inside, wooden watchtowers, horse lines; far beyond, the three pontoon bridges glitter with torches across the black river. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push from the wide camp toward the glowing general's tent. Sound: night drums, horses, fire crackling.
ACTION_START: wide camp with bridges beyond
ACTION_END: tight on the general's tent
NARRATION_KO: 같은 밤. 요하 동안, 수나라 전군 진영이었습니다. 대군이 오기 전에 길을 여는 부대였습니다. 그들은 대군보다 먼저 보고, 먼저 죽는 자들이었습니다.
DIALOGUE_KO: 
SOUND: trống đêm, ngựa, lửa.
CONTINUITY: Trại tiền quân Tùy bờ đông (sub-lock).
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_001_wide

### SC_131 | 17:40–17:48 | LOC_001 (LOC_001_sui_tent) | CHAR_205, SUI_VANGUARD_GENERAL | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot across a low table, static
IMAGE_PROMPT: Medium two-shot across a low table, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Chinese man in his mid-50s, heavy broad build, wide fleshy face with thick black brows, long black beard streaked grey to mid-chest, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest, gilt-hilted straight sword. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_001_detail: Interior of a Sui vanguard general's campaign tent at night: grey felt walls, a low black lacquered table, silk lanterns giving warm orange light, a silk map painted with rivers and a square fortress hung on a wooden frame, a sword rack, a red and yellow banner, a bronze brazier. Action: Inside the general's tent under silk lanterns: the Xianbei commander, bareheaded, dust and dried blood on his neck, sets the wrecked grey quadcopter on a low black lacquered table before a Sui general with a long black-grey beard in mingguang armor and red cloak; the general lifts a snapped orange-tipped propeller between two fingers and laughs aloud. Light: Night interior, warm orange silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the drone is set on the table; the general picks up the broken propeller between two fingers, looks at it, and laughs out loud, saying one line; the Xianbei commander's face does not change. Sound: lantern flames, a loud laugh, one line of Korean dialogue.
ACTION_START: drone being set down on table
ACTION_END: general laughing with propeller held up
NARRATION_KO: 총관은 웃었습니다. 웃는 자는 보고를 반만 들었습니다. 선비 낭장의 말을 한족 장수가 다 믿을 리 없었습니다.
DIALOGUE_KO: 수 전군총관: 고구려 요술이로군.
SOUND: lửa đèn, tiếng cười.
CONTINUITY: 전군총관 (EXTRA — râu đen-xám, KHÁC 우중문 râu trắng). Xác drone #1.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, EXTRA_sui_vanguard_general_ref, UAV_001_ref, LOC_001_detail
AI_RISK: 2 mặt + vật nhỏ → medium, tay cầm cánh quạt 2 ngón

### SC_132 | 17:48–17:56 | LOC_001 (LOC_001_sui_tent) | CHAR_205 | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, slight high angle, static
IMAGE_PROMPT: Medium close-up, slight high angle, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_001_detail: Interior of a Sui vanguard general's campaign tent at night: grey felt walls, a low black lacquered table, silk lanterns giving warm orange light, a silk map painted with rivers and a square fortress hung on a wooden frame, a sword rack, a red and yellow banner, a bronze brazier. Action: The Xianbei commander kneels on one knee on the tent floor, head bowed, dried blood tracing from his left ear down his neck, braid over one shoulder, hands resting on his knee; he reports in short flat sentences like a technical report without raising his head; the wrecked drone on the table edge above him. Light: Night interior, warm orange silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: kneeling, head down, he speaks one flat line; he does not look up. Sound: lantern flames, armor creaking, one line of Korean dialogue.
ACTION_START: kneeling, silent
ACTION_END: kneeling, line delivered, head still down
NARRATION_KO: 탁발흠은 숫자로 보고했습니다. 요술이라는 말은 쓰지 않았습니다. 본 것만 말하는 것. 그것이 그가 살아남는 방식이었습니다.
DIALOGUE_KO: 탁발흠: 요술이 아닙니다. 쇠수레가 둘, 사람은 백 남짓입니다.
SOUND: lửa, giáp.
CONTINUITY: Bible: mũ lông đã mất (survivor_ep1) — script nói 'mũ lông cầm tay' → theo lock (mũ mất); ghi proposals.
CHAIN_FROM: SC_131
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, UAV_001_ref, LOC_001_detail

### SC_133 | 17:56–18:04 | LOC_001 (LOC_001_sui_tent) | CHAR_205, SUI_VANGUARD_GENERAL | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Chinese man in his mid-50s, heavy broad build, wide fleshy face with thick black brows, long black beard streaked grey to mid-chest, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest, gilt-hilted straight sword. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_001_detail: Interior of a Sui vanguard general's campaign tent at night: grey felt walls, a low black lacquered table, silk lanterns giving warm orange light, a silk map painted with rivers and a square fortress hung on a wooden frame, a sword rack, a red and yellow banner, a bronze brazier. Action: The Sui general tosses the broken propeller onto the table, rises, and drags a silk map hung on its wooden frame into the lantern light; his thick finger stabs the painted plain east of a square fortress; the kneeling Xianbei commander below the frame edge, the drone on the table. Light: Night interior, warm orange silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the propeller clatters on the table, the general stands, hauls the silk map into the light and jabs it east of the fortress with one commanding line. Sound: plastic on lacquered wood, silk rustling, one line of Korean dialogue.
ACTION_START: general seated tossing the propeller
ACTION_END: general standing, finger on the map
NARRATION_KO: 이천 기. 총관에게는 작은 값이었습니다. 성을 치는 것은 대군의 일, 굶기는 것은 기병의 일이었습니다.
DIALOGUE_KO: 수 전군총관: 기병 이천을 주겠다. 요동성 동쪽을 막아라.
SOUND: cánh quạt rơi trên gỗ, lụa.
CONTINUITY: Bản đồ lụa: chỉ sông + ô vuông thành, không chữ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_ref, EXTRA_sui_vanguard_general_ref, UAV_001_ref, LOC_001_detail
AI_RISK: chữ trên bản đồ → 'painted rivers and a square fortress, no characters'

### SC_134 | 18:04–18:12 | LOC_001 (LOC_001_sui_tent) | CHAR_205, SUI_VANGUARD_GENERAL | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the general's finger on the map, then tilt down to the kneeling commander, single move
IMAGE_PROMPT: Close-up on the general's finger on the map, then tilt down to the kneeling commander, single move. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Chinese man in his mid-50s, heavy broad build, wide fleshy face with thick black brows, long black beard streaked grey to mid-chest, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest, gilt-hilted straight sword. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_001_detail: Interior of a Sui vanguard general's campaign tent at night: grey felt walls, a low black lacquered table, silk lanterns giving warm orange light, a silk map painted with rivers and a square fortress hung on a wooden frame, a sword rack, a red and yellow banner, a bronze brazier. Action: Close: the Sui general's thick finger presses on the painted road east of the square fortress on the silk map, his bloodshot eyes turned down toward the kneeling Xianbei commander; at the bottom of frame the commander bends and retrieves the snapped propeller from the table, turning it between two fingers, looking at it and not at the general. Light: Night interior, warm orange silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera on the finger pressing the map as the general speaks one line, then tilts down as the kneeling commander picks the broken propeller off the table and turns it slowly between his fingers, eyes on it. Sound: lantern flames, plastic turning, one line of Korean dialogue.
ACTION_START: finger on map, general's eyes down
ACTION_END: commander turning the propeller, eyes on it
NARRATION_KO: 성을 무너뜨리는 것은 사다리가 아니라 굶주림이었습니다. 탁발흠은 믿을 필요가 없었습니다. 더 볼 필요가 있었을 뿐입니다.
DIALOGUE_KO: 수 전군총관: 동쪽에서 쌀 한 톨도 못 들어가게 하라.
SOUND: lửa, nhựa xoay.
CONTINUITY: Open loop P7 phần (a). 탁발흠 giữ cánh quạt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, EXTRA_sui_vanguard_general_ref, UAV_001_ref, LOC_001_detail

### SC_135 | 18:12–18:20 | LOC_002 (LOC_002_night_road) | CHAR_006 | VEH_001, EQP_001, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV from the tank's rear, monochrome green, static
IMAGE_PROMPT: Night-vision POV from the tank's rear, monochrome green, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_002_wide: Night on the open yellow steppe west of the Goguryeo fortress: dry knee-high yellow grass under thin moonlight, drifting dust, the dark mass of the fortress on its low rise with torches along dry-stacked grey granite walls and a timber gate tower far ahead. Action: Monochrome green night-vision view from the rear deck of the K2 tank at the tail of the column: grainy green steppe, and four hundred meters back five or six horsemen bent low over their saddles following the column, no banners, no plumes, glowing faintly as warm shapes; at the bottom edge a gloved hand rises toward a shoulder handset. Light: Night, monochrome green night-vision view with grain and faint scan noise, black sky, bright green highlights on warm bodies. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static green night-vision POV: the riders behind slow as the column slows, hold their distance; the gloved hand at the bottom rises and presses the handset. Sound: tank tracks moving slowly, wind, the thin whine of a night-vision device, push-to-talk click.
ACTION_START: riders following at distance
ACTION_END: riders holding distance, hand on handset
NARRATION_KO: 요동성까지 삼십 킬로. 뒤에서 여섯 기가 따라오고 있었습니다. 삼족오 깃발은 없었습니다. 탁발흠은 사람을 잃고도 눈을 잃지 않았습니다.
DIALOGUE_KO: 
SOUND: xích K2 chậm, gió, rít kính đêm, PTT.
CONTINUITY: POV kính đêm → không HUD. VEH_206 = bóng mờ xanh lục.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, VEH_001_ref, EQP_001_ref, VEH_206_ref, LOC_002_wide
AI_RISK: POV kính đêm → monochrome green, grain, không chữ HUD

### SC_136 | 18:20–18:28 | LOC_002 (LOC_002_night_road) | CHAR_105, CHAR_006, GOG_CAVALRYMEN, XIANBEI_SCOUTS | VEH_101, VEH_206, VEH_003, WPN_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot from the tank's rear deck toward the back of the column, single move
IMAGE_PROMPT: Tracking shot from the tank's rear deck toward the back of the column, single move. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. Setting @LOC_002_wide: Night on the open yellow steppe west of the Goguryeo fortress: dry knee-high yellow grass under thin moonlight, drifting dust, the dark mass of the fortress on its low rise with torches along dry-stacked grey granite walls and a timber gate tower far ahead. Action: Night from the K2 tank's rear deck: the Goguryeo officer gallops back down the column on his armored horse, follows the staff sergeant's pointing arm into the dark, and raises his hand — ten Goguryeo cataphracts wheel out of line and charge into the blackness; in the dark the Xianbei shapes scatter three ways and a single arrow flies back and thuds into the canvas of the last cargo truck. Light: Night, thin cold moonlight, deep blue-black shadows, dust drifting. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera on the tank's rear deck tracks the action behind: the officer rides up, follows the pointing arm, raises his hand, ten riders peel off into the dark; shapes scatter out there; one arrow arcs back and hits the truck canvas. Sound: hooves charging away, a distant bowstring, arrow thudding into canvas, a short ululating cry cut off by wind.
ACTION_START: officer riding up alongside the tank
ACTION_END: ten riders gone into the dark, arrow in the truck canvas
NARRATION_KO: 해모루는 열 기를 돌려보냈습니다. 선비 척후는 싸우지 않았습니다. 흩어졌다가, 다시 모일 것이었습니다. 그것이 그들의 방식이었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa lao đi, dây cung xa, tên cắm bạt, tiếng hú ngắn tắt trong gió.
CONTINUITY: Mini-combat P7. Nhiều yếu tố → giữ xa, tối, chỉ 2 mặt chính.
CHAIN_FROM: SC_135
CUT_HALF: yes
REFS: CHAR_105_ref, CHAR_006_facepaint_ep1, VEH_101_ref, VEH_206_ref, VEH_003_ref, WPN_101_ref, LOC_002_wide
AI_RISK: nhiều kỵ binh đêm → bóng tối che, 1 chuyển động máy; kỵ chỉ là hình khối

### SC_137 | 18:28–18:38 | LOC_002 (LOC_002_gate) | GOG_INFANTRY, ROK_SOLDIERS | VEH_002 | PROPS: PROP_016, PROP_012 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: low angle at the gate, slow tilt from the vehicle up the wall
IMAGE_PROMPT: Still for ken-burns: low angle at the gate, slow tilt from the vehicle up the wall. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: Low angle at night: a K21 IFV halts before the semicircular stone barbican of the fortress's south gate, its narrow arched passage of dry-stacked grey granite lit by torches from the wall above; Goguryeo soldiers in iron lamellar lean over the parapet staring down at the iron vehicle; helmeted modern soldiers on the ground stare up at the wall; black three-legged crow banners. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow tilt from the vehicle up the granite wall to the torchlit parapet. Sound: torches crackling, whispering on the wall, an engine idling.
ACTION_START: vehicle at the gate
ACTION_END: parapet with soldiers looking down
NARRATION_KO: 요동성. 돌을 쌓아 올린 성벽 둘레 이 킬로, 높이 십 미터. 요동의 모든 길이 이 성을 지났습니다. 성벽 위의 병사들은 처음으로 쇠로 된 집을 보았습니다. 그들은 두려워하지 않았습니다. 궁금해했습니다. 문은 그 집보다 좁았습니다.
DIALOGUE_KO: 
SOUND: lửa đuốc, thì thầm trên tường, động cơ chờ.
CONTINUITY: 요동성 lần đầu (cổng nam 옹성). 2 loại lính = bóng, không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_102_ref, VEH_002_ref, PROP_012_ref, LOC_002_detail
AI_RISK: 2 nhóm lính → lính Goguryeo trên tường ngược sáng đuốc, lính Hàn từ sau

### SC_138 | 18:38–18:46 | LOC_002 (LOC_002_gate) | CHAR_003 | VEH_001 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium shot inside the arched gate passage, static
IMAGE_PROMPT: Medium shot inside the arched gate passage, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: Inside the narrow torchlit stone passage of the barbican: the stocky sergeant in a patrol cap paces its width in measured steps, lips counting; at the iron-sheathed gate doors he stops, spreads both arms and touches the rock on either side, then turns to look back through the arch at the K2 tank waiting outside — and shakes his head. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he paces across the passage counting under his breath, stops, spreads his arms to touch both walls, turns to look out at the tank and shakes his head with one line. Sound: boots echoing in the stone vault, torches, one line of Korean dialogue.
ACTION_START: pacing the passage
ACTION_END: arms spread touching both walls, head shaking
NARRATION_KO: 옹성의 문은 사람과 말을 위한 것이었습니다. 오십 톤짜리 쇠수레를 위한 문은 세상에 없었습니다.
DIALOGUE_KO: 박기철: 전차는 안 들어갑니다. 반 미터 모자랍니다.
SOUND: bước chân vang trong vòm đá.
CONTINUITY: '전차는 안 들어갑니다. 반 미터 모자랍니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_002_detail

### SC_139 | 18:46–18:54 | LOC_002 (LOC_002_gate) | CHAR_104 | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Low angle from below the gate tower, static
IMAGE_PROMPT: Low angle from below the gate tower, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: On the timber gate tower above the barbican, framed by torches on either side: the stout fortress commander with a bushy grey-streaked beard, heavy grey wool cloak, iron helmet under one arm and a ring of iron keys at his belt looks down at the vehicles below; dark tiled roof and a black crow banner above him. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: he leans on the timber rail looking down, torch flames bending in the wind, and calls one line down. Sound: torches, wind, one line of Korean dialogue.
ACTION_START: commander looking down from the tower
ACTION_END: line called down, torches bending
NARRATION_KO: 고정수 성주. 병사보다 백성을 먼저 세는 사람이었습니다. 이 성의 백성 절반이 아직 성 밖에 있었습니다.
DIALOGUE_KO: 고정수: 쇠수레를 성 안에 들이시오.
SOUND: lửa đuốc, gió.
CONTINUITY: 고정수 lần đầu. Mũ cầm tay, chìa khóa (identifier).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, LOC_002_detail

### SC_140 | 18:54–19:02 | LOC_002 (LOC_002_gate) | CHAR_001 | VEH_001 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium shot, slight low angle, static
IMAGE_PROMPT: Medium shot, slight low angle, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: The captain stands before the nose of the K2 tank outside the barbican, looking up at the gate tower; he points at the narrow torchlit gate passage, then at the tank behind him; his face composed, respectful; torchlight on the tank's glacis. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he looks up, points at the gate passage, then at the tank, and speaks one clear formal line. Sound: wind, torches, one line of Korean dialogue.
ACTION_START: captain looking up at the tower
ACTION_END: hand pointing at the tank, line finished
NARRATION_KO: 성 안의 전차는 움직일 수 없는 전차였습니다. 움직이지 못하는 전차는 과녁이었습니다.
DIALOGUE_KO: 한승우: 성주님. 성 안에 갇힌 전차는 관입니다.
SOUND: gió, lửa.
CONTINUITY: '성주님. 성 안에 갇힌 전차는 관입니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_001_ref, LOC_002_detail

### SC_141 | 19:02–19:10 | LOC_002 (LOC_002_gate) | CHAR_105 | VEH_101 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium shot, low angle, static
IMAGE_PROMPT: Medium shot, low angle, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: The Goguryeo officer on his armored horse beside the captain looks up at the gate tower, speaking fast and respectfully like a field liaison proposing a solution; torchlight on the horse's iron face mask and the white feather on his helmet. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: he looks up at the tower and speaks one quick respectful line; the horse shifts. Sound: the horse stamping, wind, one line of Korean dialogue.
ACTION_START: officer looking up
ACTION_END: line delivered
NARRATION_KO: 해모루가 길을 냈습니다. 그는 이미 이 부대의 쓸모를 계산하고 있었습니다.
DIALOGUE_KO: 해모루: 성 뒤에 골짜기가 있습니다. 산길로 통합니다.
SOUND: ngựa, gió.
CONTINUITY: '성 뒤에 골짜기가 있습니다. 산길로 통합니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, VEH_101_ref, LOC_002_detail

### SC_142 | 19:10–19:18 | LOC_002 (LOC_002_gate) | CHAR_104 | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium close-up on the tower, static
IMAGE_PROMPT: Medium close-up on the tower, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: The fortress commander stands silent on the gate tower, one fist closed around the iron ring of keys at his belt; his eyes go down to the tank, to the captain, to the line of refugees waiting behind the vehicles, and he decides; torches either side. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: his fist tightens on the keys, eyes move down and across, then he speaks one decisive line. Sound: keys clinking, torches, one line of Korean dialogue.
ACTION_START: silent, fist on keys
ACTION_END: line delivered
NARRATION_KO: 성주는 조건을 걸었습니다. 이 땅에서 신뢰는 사람을 맡기는 것이었습니다.
DIALOGUE_KO: 고정수: 좋소. 대신 한 대장과 열 명은 성 안에서 자시오.
SOUND: chìa khóa lách cách.
CONTINUITY: '좋소. 대신 한 대장과 열 명은 성 안에서 자시오.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, LOC_002_detail

### SC_143 | 19:18–19:26 | LOC_002 (LOC_002_gate) | CHAR_001, CHAR_002 | VEH_001 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners. Action: Before the tank's nose the captain glances sideways at the tall lieutenant, whose face is sour and whose head shakes slightly, then looks up at the gate tower and nods once; torchlight. Light: Night, warm orange torchlight against deep blue-black darkness, thin moon. Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the captain's eyes go to the lieutenant, the lieutenant's slight head shake, the captain looks up and nods, speaking one line. Sound: wind, one line of Korean dialogue.
ACTION_START: captain glancing at lieutenant
ACTION_END: captain nodding up at the tower, line spoken
NARRATION_KO: 열 명은 인질이었습니다. 신뢰는 그렇게 시작되었습니다. 오태민은 그 열 명에 들지 않았습니다. 한승우가 뺐습니다.
DIALOGUE_KO: 한승우: 알겠습니다. 열 명은 제가 고릅니다.
SOUND: gió.
CONTINUITY: '알겠습니다. 열 명은 제가 고릅니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_002_ref, VEH_001_ref, LOC_002_detail

### SC_144 | 19:26–19:34 | LOC_003 (LOC_003_trail) | CHAR_105, GOG_CAVALRYMEN, XIANBEI_SCOUTS | VEH_003, VEH_101, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Low wide from the trail looking up the slope, static
IMAGE_PROMPT: Low wide from the trail looking up the slope, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_wide: A dirt trail at night skirting low hills of bare oak scrub and dry yellow grass into a shallow valley, thin moonlight, dark oak thickets on the slopes above. Action: Night: the convoy turns onto a dirt trail along a hillside of bare oak scrub into a shallow valley; on the slope above, three Xianbei riders show for a moment under thin moonlight; Goguryeo cataphracts led by the officer with the white feather cry out and drive up the slope; two arrows thud into the cargo bed of the last truck; the three shapes wheel and vanish into the oak scrub. Light: Night, thin cold moonlight, deep blue-black shadows, dust drifting. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low wide: three rider silhouettes appear on the moonlit slope; the cavalry surges uphill with a cry; two arrows strike the truck bed; the silhouettes wheel and melt into the trees. Sound: a war cry, hooves climbing, arrows into wood, branches snapping.
ACTION_START: riders visible on slope, convoy on trail
ACTION_END: cavalry on the slope, riders gone, arrows in truck
NARRATION_KO: 골짜기는 동문에서 2킬로였습니다. 산길 하나로만 통했습니다. 그날 밤부터 그곳이 천둥 기지였습니다. 그리고 그 산길을, 선비 척후 셋이 보고 갔습니다.
DIALOGUE_KO: 
SOUND: hú, vó ngựa lên dốc, tên cắm gỗ, cành gãy.
CONTINUITY: Mini-combat: 3 trinh sát đã thấy đường mòn. Từ đây LOC_003 = thung lũng thật.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_ref, VEH_003_ref, VEH_101_ref, VEH_206_ref, LOC_003_wide
AI_RISK: nhiều kỵ đêm → silhouette dưới trăng, wide xa

### SC_145 | 19:34–19:42 | LOC_003 (LOC_003_dawn) | CHAR_003, CHAR_001 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot at the tank's engine deck, static
IMAGE_PROMPT: Medium two-shot at the tank's engine deck, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: Cold blue-hour dawn in the valley: the stocky sergeant pulls the dipstick from the K2 tank's engine deck, tilts it to the light, wipes it with the red rag and writes in the green notebook; the captain walks in from the direction of the fortress with dew on his shoulders and stops beside him; mist on the grass. Light: Cold blue-hour dawn, thin mist on the ground, dew on metal and grass, first grey light without sun. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: dipstick out, read, wiped, notebook written; the captain arrives and stands; the sergeant speaks one line without looking up. Sound: dawn birds, metal on metal, pencil, one line of Korean dialogue.
ACTION_START: dipstick coming out, captain approaching
ACTION_END: sergeant writing, captain standing beside, line spoken
NARRATION_KO: 삼십 킬로. 사백 킬로 중 삼십이 하룻밤에 사라졌습니다. 삼백칠십 킬로. 박기철은 그 숫자를 새 페이지에 적었습니다.
DIALOGUE_KO: 박기철: 간밤에 전차 삼십 킬로 썼습니다.
SOUND: chim sớm, kim loại, bút chì.
CONTINUITY: D4 bình minh: '간밤에 전차 삼십 킬로 썼습니다.' K2 dưới lưới trong thung.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_001_ref, VEH_001_ref, LOC_003_wide

### SC_146 | 19:42–19:50 | LOC_003 (LOC_003_dawn) | CHAR_006, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, high angle over the drawing, static
IMAGE_PROMPT: Medium shot, high angle over the drawing, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The staff sergeant, boonie hat soaked with dew, kneels and draws in the dirt with the tip of a fixed-blade knife — a line, a hooking arc across it — the captain crouched opposite; he reports like a telegram. Light: Cold blue-hour dawn, thin mist on the ground, dew on metal and grass, first grey light without sun. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static high angle: the knife tip cuts a line in the dirt, then an arc across it; he looks up and says one clipped line. Sound: knife scratching earth, one line of Korean dialogue.
ACTION_START: knife starting the line
ACTION_END: arc drawn, sergeant looking up
NARRATION_KO: 동쪽 길. 성으로 들어오는 마지막 길이었습니다. 길이 끊기면 성은 섬이 되는 것이었습니다.
DIALOGUE_KO: 백성민: 동쪽 길, 오늘 밤이면 끊깁니다. 기병 천 이상.
SOUND: dao vạch đất.
CONTINUITY: Dao lưỡi cố định (cùng dao SC_199).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, CHAR_001_ref, LOC_003_wide
AI_RISK: tay cầm dao → mũi dao vạch đất, tay 1

### SC_147 | 19:50–19:58 | LOC_003 (LOC_003_dawn) | CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the drawing then tilt to the face, single move
IMAGE_PROMPT: Close-up on the drawing then tilt to the face, single move. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: Close: the knife tip adds a long row of dots along the drawn road in the dirt — people and carts — then the staff sergeant lifts his painted face to the captain off-frame. Light: Cold blue-hour dawn, thin mist on the ground, dew on metal and grass, first grey light without sun. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera on the knife tapping a row of dots along the dirt line, then tilts up to his face as he delivers one line. Sound: knife tapping earth, wind, one line of Korean dialogue.
ACTION_START: knife tapping dots
ACTION_END: face up, line delivered
NARRATION_KO: 삼천 명. 곡식 수레. 백성민의 보고에는 형용사가 없었습니다. 형용사는 셈을 흐리기 때문이었습니다.
DIALOGUE_KO: 백성민: 길 위에 피난민 삼천. 곡식 수레도 있습니다.
SOUND: dao vạch đất, gió.
CONTINUITY: Kế SC_146.
CHAIN_FROM: SC_146
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, LOC_003_wide

### SC_148 | 19:58–20:08 | LOC_002 (LOC_002_eastroad) | REFUGEES | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial, slow pull-out. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: High aerial by day: a dirt road runs across the yellow steppe to the east gate of the granite fortress; along it a long line of refugees on foot and two-wheeled ox carts heaped with grain sacks stretches back for kilometers; far to the north a thin band of horsemen's dust hangs above the grass. Light: Grey overcast daylight, flat diffused light, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow pull-out over the road and the column. Sound: high wind, distant oxen lowing.
ACTION_START: road and column, gate at top
ACTION_END: pulled out, dust band visible to the north
NARRATION_KO: 동쪽 마을들이 곡식을 싣고 성으로 오고 있었습니다. 삼천 명이었습니다. 성이 버틸 여름이 그 수레 위에 있었습니다. 수레는 백 대. 사람은 걸었고, 소는 끌었습니다.
DIALOGUE_KO: 
SOUND: gió trên cao, xa xa tiếng bò.
CONTINUITY: 3.000 dân + 100 xe bò.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_002_wide

### SC_149 | 20:08–20:16 | LOC_002 (LOC_002_eastwall) | CHAR_104, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot on the wall, static
IMAGE_PROMPT: Medium two-shot on the wall, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_002_detail: On top of the east wall of the Goguryeo fortress: dry-stacked grey granite blocks without mortar forming a rectangular protruding bastion with a low stone parapet and narrow arrow slits, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner on a pole, the dirt road below running east through dry yellow steppe. Action: On the east wall of the fortress beside a protruding stone bastion: the fortress commander in his grey cloak and the captain in digital camo stand side by side looking down at the east road; the commander holds a bundle of bamboo tally slips and taps them on the granite parapet. Light: Cold blue-hour dawn, thin mist on the ground, dew on metal and grass, first grey light without sun. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: both look down at the road; the commander taps the tally slips on the stone and speaks one line. Sound: wind over the wall, bamboo slips clicking, one line of Korean dialogue.
ACTION_START: two men looking down at the road
ACTION_END: commander tapping slips, line spoken
NARRATION_KO: 스무 날. 성주는 창고를 날짜로 셌습니다. 박기철이 기름을 세는 방식이었습니다.
DIALOGUE_KO: 고정수: 창고에 곡식이 스무 날 치요. 스무 날.
SOUND: gió trên tường, thẻ tre.
CONTINUITY: Contrast bắt buộc: camo cạnh áo choàng xám trên tường đá 치.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, CHAR_001_ref, LOC_002_detail

### SC_150 | 20:16–20:24 | LOC_002 (LOC_002_eastwall) | CHAR_104 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. Setting @LOC_002_detail: On top of the east wall of the Goguryeo fortress: dry-stacked grey granite blocks without mortar forming a rectangular protruding bastion with a low stone parapet and narrow arrow slits, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner on a pole, the dirt road below running east through dry yellow steppe. Action: The fortress commander points down over the parapet at the distant line of ox carts on the east road, then swings his arm west toward the plain where grey Sui tents are springing up like mushrooms; grey sky, grey cloak, keys at his belt. Light: Grey overcast daylight, flat diffused light, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: arm points down east at the carts, then swings west toward the tents; one line. Sound: wind, one line of Korean dialogue.
ACTION_START: pointing east at the carts
ACTION_END: arm pointing west, line finished
NARRATION_KO: 성주가 세는 것은 곳간만이 아니었습니다. 문 밖의 삼천도 그의 셈에 있었습니다.
DIALOGUE_KO: 고정수: 저 수레가 못 들어오면 삼천이 성 밖에서 죽소.
SOUND: gió.
CONTINUITY: '저 수레가 못 들어오면 삼천이 성 밖에서 죽소.'
CHAIN_FROM: SC_149
CUT_HALF: no
REFS: CHAR_104_ref, LOC_002_detail

### SC_151 | 20:24–20:32 | LOC_002 (LOC_002_eastwall) | CHAR_104, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_002_detail: On top of the east wall of the Goguryeo fortress: dry-stacked grey granite blocks without mortar forming a rectangular protruding bastion with a low stone parapet and narrow arrow slits, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner on a pole, the dirt road below running east through dry yellow steppe. Action: The fortress commander turns his whole body to face the captain squarely on the wall — not pleading, not ordering — handing over a task like handing over a key; the captain listens, compass at his throat; grey sky. Light: Grey overcast daylight, flat diffused light, cold wind, yellow dust. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the commander turns square to the captain and speaks one line; the captain holds his gaze. Sound: wind, one line of Korean dialogue.
ACTION_START: commander turning to face the captain
ACTION_END: line delivered, captain listening
NARRATION_KO: 부탁이 아니었습니다. 성주는 이 부대의 쓸모를 정한 것이었습니다. 쇠수레는 성 밖에서 쓸모가 있어야 했습니다.
DIALOGUE_KO: 고정수: 동쪽 길을 하룻밤만 지켜 주시오.
SOUND: gió.
CONTINUITY: '동쪽 길을 하룻밤만 지켜 주시오.'
CHAIN_FROM: SC_150
CUT_HALF: no
REFS: CHAR_104_ref, CHAR_001_ref, LOC_002_detail

### SC_152 | 20:32–20:40 | LOC_002 (LOC_002_eastwall) | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_002_detail: On top of the east wall of the Goguryeo fortress: dry-stacked grey granite blocks without mortar forming a rectangular protruding bastion with a low stone parapet and narrow arrow slits, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner on a pole, the dirt road below running east through dry yellow steppe. Action: Close on the captain on the wall: his eyes go down to the east road, then over to the valley where the vehicles are hidden, a long silent beat, then a single nod; grey light on his face. Light: Grey overcast daylight, flat diffused light, cold wind, yellow dust. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes to the road, to the valley, a long beat, one nod and one short line. Sound: wind, a distant horn inside the fortress, one line of Korean dialogue.
ACTION_START: eyes on the road
ACTION_END: nod, line spoken
NARRATION_KO: 하룻밤. 한승우가 이 땅에 내건 첫 번째 약속이었습니다. 약속은 짧았습니다. 그래서 지킬 수 있었습니다.
DIALOGUE_KO: 한승우: 하룻밤. 그 이상은 없습니다.
SOUND: gió, tù và xa trong thành.
CONTINUITY: '하룻밤. 그 이상은 없습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_002_detail

### SC_153 | 20:40–20:50 | LOC_001 (LOC_001_north_steppe) | CHAR_205 | VEH_206 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high wide of a cavalry column, slow lateral slide  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high wide of a cavalry column, slow lateral slide. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_001_wide: Open yellow steppe north of the Goguryeo fortress, dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, low grassy rises, cold pale grey sky, early spring, no trees. Action: High wide by day: two thousand Xianbei light horsemen cut diagonally across the yellow steppe toward the east under black horse-tail standards, fur caps, bows, their dust a long river behind them; at the head a bareheaded rider with a single thick braid — the commander; the column's end lost in dust. Light: Grey overcast daylight, flat diffused light, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow lateral slide along the column in the direction of travel. Sound: thousands of hooves, wind.
ACTION_START: head of column with the commander
ACTION_END: slid along the column into its dust
NARRATION_KO: 탁발흠은 이천 기와 함께 동쪽으로 돌았습니다. 본대보다 하루 빨랐습니다. 그는 길을 막는 법을 알았습니다. 이천 기는 성 하나를 굶기기에 충분한 수였습니다.
DIALOGUE_KO: 
SOUND: vó ngựa ngàn con, gió.
CONTINUITY: 2.000 kỵ vòng đông. 탁발흠 = survivor (bím tóc lộ).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, VEH_206_ref, LOC_001_wide

### SC_154 | 20:50–21:00 | LOC_002 (LOC_002_eastwall) | CHAR_104, CHAR_001 | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide from behind, two figures on the wall, slow push-in
IMAGE_PROMPT: Still for ken-burns: wide from behind, two figures on the wall, slow push-in. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_002_detail: On top of the east wall of the Goguryeo fortress: dry-stacked grey granite blocks without mortar forming a rectangular protruding bastion with a low stone parapet and narrow arrow slits, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner on a pole, the dirt road below running east through dry yellow steppe. Action: From behind: two figures stand on the east wall's granite parapet looking down the same road — one in a heavy grey wool cloak with an iron helmet under his arm, one in granite-pattern digital camo with a covered helmet — yellow grass and grey sky beyond, the road with its distant line of carts. Light: Grey overcast daylight, flat diffused light, cold wind, yellow dust. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push-in on the two backs. Sound: wind.
ACTION_START: two figures wide
ACTION_END: tight on the two backs
NARRATION_KO: 두 사람은 같은 수레를 보고 있었습니다. 성주는 쌀을 원했습니다. 탁발흠도 같은 것을 원했습니다.
DIALOGUE_KO: 
SOUND: gió.
CONTINUITY: Mid-roll 3 @21:00 sau cảnh này. Open loop P7.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, CHAR_001_ref, LOC_002_detail


## [Phần 8] 건전지 나흘 (21:00–24:00) · tài nguyên, lều đỏ, cối đăng ký, tên cắm lưới

### SC_155 | 21:00–21:08 | LOC_002 | — | — | PROPS: — | TYPE: video8s | 8s
SHOT: Very high aerial at night, one slow glide  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Very high aerial at night, one slow glide. Setting @LOC_002_wide: Goguryeo plain fortress on a low rise in yellow steppe: dry-stacked grey granite walls slightly battered inward, rectangular protruding bastions every fifty meters, semicircular stone barbican at the south gate, two-story timber gate tower with dark grey tiled roof, wooden corner watchtowers, a three-story wooden pagoda inside, black three-legged crow banners, amber low sun through yellow dust. Action: Very high aerial at night: the fortress is a dark mass on its rise in the middle of the black plain; to the west and south tens of thousands of Sui campfires curve around it in an arc that is closing; to the east the plain is still dark; thin moonlight. Light: Night from high above, tens of thousands of orange campfires on a black plain, thin moonlight. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: One slow high glide over the fortress; campfires flicker in their closing arc; the dark east side stays dark. No dialogue. Sound: night wind, very distant Sui drums, a Goguryeo horn answering.
ACTION_START: fortress centered, fire arc west and south
ACTION_END: glided slightly east, dark side in frame
NARRATION_KO: 하루에 한 군씩, 불빛이 늘어났습니다.
DIALOGUE_KO: 
SOUND: gió đêm, trống Tùy rất xa, tù và Goguryeo đáp lại.
CONTINUITY: Sau mid-roll 3: không thoại. 'Hàng vạn đốm lửa'.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_002_wide

### SC_156 | 21:08–21:16 | LOC_003 (LOC_003_tent_ext) | CHAR_003 | VEH_004, UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium close-up under a hooded red flashlight, static
IMAGE_PROMPT: Medium close-up under a hooded red flashlight, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: At night behind the 4x4 command vehicle a small humming generator glows faintly; the stocky sergeant plugs a charging cable into a grey quadcopter drone's battery, reads the generator's small fuel gauge, and writes in the green notebook under a hooded red flashlight, patrol cap, red rag at his belt. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the cable clicks into the drone battery, he bends to read the fuel gauge, straightens and writes, then says one line. Sound: generator humming, pencil on paper, one line of Korean dialogue.
ACTION_START: cable being plugged in
ACTION_END: writing in notebook, line spoken
NARRATION_KO: 충전은 곧 연료였습니다. 연료는 곧 거리였습니다. 드론 한 번에 전차 육백 미터가 사라졌습니다.
DIALOGUE_KO: 박기철: 드론 한 번 충전, 경유 2리터.
SOUND: máy phát ro ro, bút chì.
CONTINUITY: Drone #2 sạc. Máy phát K151 chạy (đêm 4).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_004_ref, UAV_001_ref, LOC_003_wide

### SC_157 | 21:16–21:24 | LOC_003 (LOC_003_tent) | CHAR_003, CHAR_001 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: High angle over the table then medium two-shot, static
IMAGE_PROMPT: High angle over the table then medium two-shot, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_detail: Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air. Action: Inside the red-lit command tent: twelve black monocular night-vision devices lie in two rows on the steel folding table with columns of AA batteries stacked beside them; the stocky sergeant counts them with a pencil tip; the captain stands watching with his hands clasped behind his back. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the pencil tip touches each device in turn, the sergeant looks up and speaks one line; the captain does not move. Sound: batteries clicking, the generator outside, one line of Korean dialogue.
ACTION_START: pencil counting the devices
ACTION_END: sergeant looking up, line spoken, captain still
NARRATION_KO: 야시경은 건전지를 먹었습니다. 건전지는 충전할 수 없는 것이었습니다. 열두 개를 켜면 나흘, 여섯 개를 켜면 여드레였습니다.
DIALOGUE_KO: 박기철: 오늘 밤 다 쓰면, 건전지는 나흘치입니다.
SOUND: pin lách cách, máy phát ngoài lều.
CONTINUITY: 12 kính đêm, pin AA. Lều đèn đỏ (LOC_003_tent).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_001_ref, EQP_001_ref, LOC_003_detail
AI_RISK: 12 vật giống nhau → 2 hàng đều, đếm bằng bút

### SC_158 | 21:24–21:32 | LOC_003 (LOC_003_medic) | CHAR_004, ROK_SOLDIER | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium close-up, static
IMAGE_PROMPT: Medium close-up, static. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_003_wide: The aid station of the hidden company base at night: a canvas awning off an olive-green army tent, a folding stretcher on olive ammunition cans, a headlamp and a shaded red lamp, camouflage netting, brown hemp Goguryeo tents beside, dry yellow grass, dark oak scrub slopes. Action: At the aid station under a shaded lamp the young female medic changes the dressing on a soldier's bandaged forearm, gives an injection, sets an empty white plastic bottle aside, and counts the remaining bottles in her open medic bag with a fingertip; headlamp on her helmet, red cross armband; the soldier's face turned away. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: dressing off and on, the injection, the empty bottle set down, fingertip counting bottles in the bag; she says one line. Sound: bandage tearing, bottles clicking, one line of Korean dialogue.
ACTION_START: unwrapping the forearm
ACTION_END: counting bottles in the bag, line spoken
NARRATION_KO: 스무 개 중 열여덟 개. 화살 하나가 항생제 하나였습니다. 그 셈이 앞으로의 셈이었습니다.
DIALOGUE_KO: 윤서아: 항생제, 아흔 퍼센트 남았습니다. 두 명분 썼습니다.
SOUND: băng xé, lọ chạm.
CONTINUITY: Kháng sinh 20→18. Lọ không nhãn.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_ref, PROP_009_ref, LOC_003_wide

### SC_159 | 21:32–21:40 | LOC_003 (LOC_003_medic) | CHAR_107, CHAR_004 | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium two-shot, static, low
IMAGE_PROMPT: Medium two-shot, static, low. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_003_wide: The aid station of the hidden company base at night: a canvas awning off an olive-green army tent, a folding stretcher on olive ammunition cans, a headlamp and a shaded red lamp, camouflage netting, brown hemp Goguryeo tents beside, dry yellow grass, dark oak scrub slopes. Action: The girl in red-threaded braids squats beside the medic, pulls a handful of dried leaves from the small cloth pouch at her waist and holds it out, pointing at the soldier's wound; the medic takes the leaves, raises them to her nose, and looks at the girl; shaded lamp, tent canvas stirring. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the girl offers the leaves and points at the wound with one line; the medic lifts them, smells them, and looks at the girl. Sound: dry leaves rustling, wind against the tent, one line of Korean dialogue.
ACTION_START: girl pulling leaves from pouch
ACTION_END: medic smelling the leaves, looking at the girl
NARRATION_KO: 아리, 열다섯 살. 그 풀의 이름을 서아는 몰랐습니다. 이 시대의 약은 풀이었습니다.
DIALOGUE_KO: 아리: 언니, 이 풀은 피를 멎게 해요.
SOUND: lá khô, gió lùa lều.
CONTINUITY: Túi thảo dược 아리 (lock). '언니, 이 풀은 피를 멎게 해요.'
CHAIN_FROM: SC_158
CUT_HALF: no
REFS: CHAR_107_refugee_ep1, CHAR_004_ref, PROP_009_ref, LOC_003_wide

### SC_160 | 21:40–21:48 | LOC_003 (LOC_003_hearth) | ROK_SOLDIERS | — | PROPS: PROP_010 | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: close-up on a bowl in a gloved hand, slow push-in
IMAGE_PROMPT: Still for ken-burns: close-up on a bowl in a gloved hand, slow push-in. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @PROP_010_ref: South Korean army combat ration: square olive-brown plastic pouches, a flameless heating bag steaming, plastic spoon, compressed biscuit, instant coffee sachet; later a Goguryeo clay bowl of millet. Setting @LOC_003_wide: A Goguryeo stone hearth fire at the hidden company base at night: a ring of grey stones, a clay pot over orange flames, brown hemp Goguryeo tents with wooden poles beside olive-green army tents, camouflage netting over dark vehicle shapes behind, dry yellow grass, bare oak scrub. Action: Close: a Goguryeo wooden bowl of yellow millet porridge in a black-gloved hand with an army spoon, a clay pot on a ring of hearth stones behind it, and beyond, out of focus, a few helmeted soldiers grimacing but eating; firelight. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow push-in on the bowl. Sound: fire, spoon on wood.
ACTION_START: bowl and hearth
ACTION_END: tight on the bowl
NARRATION_KO: 첫 고구려 밥이었습니다. 조죽 한 그릇. 아무도 남기지 않았습니다. 이 밥부터 이 부대는 고구려에 빚을 졌습니다. 빚은 갚아야 했습니다. 어떤 방식으로든.
DIALOGUE_KO: 
SOUND: lửa, thìa chạm gỗ.
CONTINUITY: Bữa Goguryeo đầu tiên. PROP_010 (bát đất/ gỗ).
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_010_ref, LOC_003_wide

### SC_161 | 21:48–21:56 | LOC_003 (LOC_003_tent_ext) | CHAR_001, CHAR_002, CHAR_003, ROK_SOLDIERS | VEH_004, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Static wide outside the command tent at night
IMAGE_PROMPT: Static wide outside the command tent at night. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: Outside the olive command tent glowing faintly red: two helmeted soldiers sit on ammunition cans swapping AA batteries into black night-vision monoculars, faces down; the generator hums behind them; the captain, the tall lieutenant and the stocky sergeant walk past them in single file, lift the tent flap and go in. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the two soldiers work on the devices; the three men walk through frame, lift the flap and disappear inside; the flap falls. No dialogue. Sound: generator, batteries clicking, tent flap.
ACTION_START: three men approaching, soldiers working
ACTION_END: flap falling behind the three, soldiers still working
NARRATION_KO: 세 사람이 지휘 천막으로 들어갔습니다. 지금부터 할 이야기는 세 사람만의 것이었습니다. 나머지 아흔한 명에게는 무거운 것이었습니다.
DIALOGUE_KO: 
SOUND: máy phát, pin lách cách, cửa lều.
CONTINUITY: Insert 1 (decisions). Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_002_ref, CHAR_003_ref, VEH_004_ref, EQP_001_ref, LOC_003_wide

### SC_162 | 21:56–22:04 | LOC_003 (LOC_003_tent) | CHAR_001 | — | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Medium shot inside the tent, static
IMAGE_PROMPT: Medium shot inside the tent, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_003_detail: Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air. Action: Inside the red-lit command tent the captain pulls the flap closed behind him and turns to the folding table where a hand-drawn pencil map lies; he lowers his voice and speaks slowly, eyes moving from one side of the table to the other; red lamplight on his face. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: flap pulled shut, he turns to the table, looks left then right, and says one slow low line. Sound: the tent zipper, the generator faint outside, one line of Korean dialogue.
ACTION_START: pulling the flap shut
ACTION_END: facing the table, line spoken
NARRATION_KO: 
DIALOGUE_KO: 한승우: 이 싸움은 역사가 이미 이겼다. 우리는 망치지만 않으면 된다.
SOUND: khóa lều, máy phát rất xa.
CONTINUITY: Direct quote #4: '이 싸움은 역사가 이미 이겼다…'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, PROP_001_ref, LOC_003_detail

### SC_163 | 22:04–22:12 | LOC_003 (LOC_003_tent) | CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, static, low angle over the table
IMAGE_PROMPT: Medium close-up, static, low angle over the table. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. Setting @LOC_003_detail: Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air. Action: The tall lieutenant plants both hands on the steel folding table and leans in over the hand-drawn map, his face in red lamplight, goggles on his helmet, each word heavy but not loud. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: both hands hit the table, he leans in and delivers one heavy quiet line. Sound: the folding table creaking, one line of Korean dialogue.
ACTION_START: hands landing on the table
ACTION_END: leaning in, line delivered
NARRATION_KO: 역사는 고구려의 승리를 적었습니다. 그 책에 아흔네 명은 없었습니다. 한승우는 답이 없었습니다.
DIALOGUE_KO: 오태민: 역사책이 우리 94명을 지켜줍니까?
SOUND: bàn gấp kêu.
CONTINUITY: '역사책이 우리 94명을 지켜줍니까?'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, LOC_003_detail

### SC_164 | 22:12–22:20 | LOC_003 (LOC_003_tent) | CHAR_001 | — | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Extreme close-up on a hand on a hand-drawn map, static
IMAGE_PROMPT: Extreme close-up on a hand on a hand-drawn map, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_003_detail: Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air. Action: Close in red lamplight: the captain's gloved hand rests on the back of the folded army map where a pencil sketch is drawn — a winding river, a square for a fortress, an arrow pointing south-east, and at the paper's edge another bend of river marked with a single unreadable scrawl; his index finger comes to rest on that scrawl. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up: the finger slides across the sketch from the fortress square along the arrow and stops on the scrawl at the paper's edge; holds. No dialogue. Sound: silence, the generator faint, paper.
ACTION_START: finger at the fortress square
ACTION_END: finger resting on the scrawl at the edge
NARRATION_KO: 손으로 그린 지도였습니다. 요하, 요동성, 그리고 아직 가 보지 않은 강 하나. 살수. 그 강까지 사백 킬로였습니다. 전차 한 통이었습니다.
DIALOGUE_KO: 
SOUND: im, máy phát rất xa, giấy.
CONTINUITY: Insert 2. Chữ '살수' = 'single unreadable scrawl' (no text).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, PROP_001_ref, LOC_003_detail
AI_RISK: chữ trên bản đồ → nét nguệch ngoạc không đọc được

### SC_165 | 22:20–22:28 | LOC_003 (LOC_003_k2) | CHAR_002 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot following him from the tent to the tank, single move
IMAGE_PROMPT: Tracking shot following him from the tent to the tank, single move. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond. Action: The tall lieutenant shoves the tent flap aside and strides through the dark straight to the K2 tank under its camouflage netting, slaps the thick side skirt twice with his palm — the same spot the sergeant always pats — then turns to look back at the tent's red glow. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera tracks with him from the tent flap to the tank; two palm slaps on the side skirt; he turns back toward the tent glow and speaks one line. Sound: tent flap, boots on dirt, palm on steel twice, one line of Korean dialogue.
ACTION_START: pushing out of the tent
ACTION_END: at the tank, turned toward the tent, line spoken
NARRATION_KO: 두 번째 요구였습니다. 같은 쇠를 같은 손짓으로 두드리는 두 사람이 있었습니다. 아끼는 쪽과 쓰는 쪽이었습니다.
DIALOGUE_KO: 오태민: 전차를 내보내면 야시경은 필요 없습니다.
SOUND: cửa lều, giày trên đất, tay vỗ thép.
CONTINUITY: Walk-and-talk. Cùng chỗ vỗ váy xích (SC_083/187).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, VEH_001_ref, LOC_003_wide

### SC_166 | 22:28–22:36 | LOC_003 (LOC_003_tent_ext) | CHAR_001 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the tent door, static
IMAGE_PROMPT: Medium shot at the tent door, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The captain stands in the tent doorway, red light behind him, looking without blinking toward the lieutenant at the tank in the dark; his voice drops lower still; compass cord at his throat. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he stands in the doorway, unblinking, and says one low line. Sound: wind, the generator, one line of Korean dialogue.
ACTION_START: standing in the doorway
ACTION_END: line delivered, still unblinking
NARRATION_KO: 스물두 발과 사백 킬로. 한승우는 그것을 마지막을 위해 남겼습니다. 마지막이 언제인지는 그도 몰랐습니다.
DIALOGUE_KO: 한승우: 전차는 그물 밑에 둔다. 두 번 말 안 한다.
SOUND: gió, máy phát.
CONTINUITY: '전차는 그물 밑에 둔다. 두 번 말 안 한다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_001_ref, LOC_003_wide

### SC_167 | 22:36–22:44 | LOC_003 (LOC_003_tent) | CHAR_001, CHAR_003 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot over the table, static
IMAGE_PROMPT: Medium two-shot over the table, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_detail: Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air. Action: Back inside the red tent the captain slides a case of black night-vision monoculars across the folding table toward the stocky sergeant, who catches it with both gloved hands; the rows of devices and batteries on the table. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the case slides across the table, the sergeant stops it; the captain gives one order. Sound: the case sliding on steel, one line of Korean dialogue.
ACTION_START: case being pushed
ACTION_END: sergeant's hands on the case, order given
NARRATION_KO: 볼 수 있으면 살 수 있었습니다. 건전지 나흘치가 그 값이었습니다.
DIALOGUE_KO: 한승우: 야시경 열두 개, 전부 켠다. 오늘 밤은 봐야 한다.
SOUND: kính đêm trượt trên bàn.
CONTINUITY: Quyết định 2: bật hết 12 kính đêm.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_003_ref, EQP_001_ref, LOC_003_detail

### SC_168 | 22:44–22:52 | LOC_003 (LOC_003_tent_ext) | CHAR_003, CHAR_005, ROK_SOLDIERS | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: From behind a line of soldiers toward the sergeant, static
IMAGE_PROMPT: From behind a line of soldiers toward the sergeant, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: From behind a short line of helmeted soldiers at night: the stocky sergeant hands each man a black night-vision monocular and notes it in the green notebook; the boyish private takes the last one and turns toward camera — his face clear — snaps it onto his helmet mount and flips it down: his left eye glows faint green. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static from behind the line: devices handed out one by one; the private takes the last, turns, mounts it and clicks it down, his left eye lit green. No dialogue. Sound: metal mounts folding, pencil, a click as the device switches on.
ACTION_START: sergeant handing out devices, line from behind
ACTION_END: private facing camera, device down, green eye
NARRATION_KO: 야시경 열두 개. 이 부대가 밤을 보는 눈이었습니다. 박격포 백이십. 40밀리 오백사십. 드론 셋. 쓰는 것은 줄어들고, 채워지는 것은 없었습니다.
DIALOGUE_KO: 
SOUND: cần gập kim loại, bút chì, tiếng "딸깍" bật kính.
CONTINUITY: Mặt đám đông = sau lưng; chỉ 태오 quay lại rõ mặt (decisions).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_005_ref, EQP_001_ref, LOC_003_wide
AI_RISK: hàng lính → máy sau lưng hàng người

### SC_169 | 22:52–23:02 | LOC_003 (LOC_003_northridge) | CHAR_205, XIANBEI_SCOUTS | VEH_206 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide on a night ridge, slow push toward a faint red glow below
IMAGE_PROMPT: Still for ken-burns: wide on a night ridge, slow push toward a faint red glow below. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A low grassy ridge north of the valley at night: dry knee-high yellow grass under thin moonlight, bare oak scrub, the dark hollow of a valley below with a faint red glow leaking through camouflage netting. Action: Night on a grassy ridge a kilometer north of the valley: the bareheaded Xianbei commander stands beside his horse among a few riders, looking down — below in the black fold of the valley a very faint red glow leaks through camouflage netting. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push from the ridge down toward the faint red glow. Sound: night wind, a horse breathing, a faint far-off generator hum.
ACTION_START: commander on ridge, valley dark below
ACTION_END: tight on the faint red glow
NARRATION_KO: 같은 시각, 북쪽 능선. 탁발흠은 골짜기에서 새는 붉은 빛을 보고 있었습니다. 낮에는 길을 막고, 밤에는 쇠수레를 찾았습니다. 그는 척후 셋을 내려보냈습니다.
DIALOGUE_KO: 
SOUND: gió đêm, ngựa thở, xa xa tiếng máy phát mơ hồ.
CONTINUITY: Insert 3. 탁발흠 thấy đèn đỏ lều.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, VEH_206_ref, LOC_003_ford_night

### SC_170 | 23:02–23:10 | LOC_003 (LOC_003_mortar) | CHAR_003, ROK_SOLDIERS | WPN_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot in the mortar pit, static
IMAGE_PROMPT: Medium shot in the mortar pit, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. Setting @LOC_003_wide: A sandbagged mortar pit on a small grassy knoll at the south end of the hidden valley base at night: two 81mm mortars on bipods, round baseplates, olive ammunition cans, a range card on a stake, dry yellow grass, dark oak scrub slopes, the valley below. Action: In a sandbagged mortar pit on the knoll at night: two 81mm mortars on bipods; the stocky sergeant points with one finger and a lensatic compass toward the stream ford to the east; a helmeted gunner, face down, turns the elevation handwheel and another drops a finned bomb into the tube. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the sergeant points east with the compass; the gunner turns the handwheel; a bomb slides into the tube; the gunner calls one line. Sound: handwheel clicking, the bomb sliding down the tube, one line of Korean dialogue.
ACTION_START: sergeant pointing, gunner adjusting
ACTION_END: bomb dropped into tube, line called
NARRATION_KO: 표적을 미리 등록하면 밤에도 맞출 수 있었습니다. 대신 두 발이 들었습니다.
DIALOGUE_KO: 사수: 박격포 1번, 개울 여울 제원. 두 발 사격.
SOUND: tay quay, đạn trượt nòng.
CONTINUITY: Đăng ký mục tiêu bến suối. Lính = extra không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, WPN_002_ref, LOC_003_wide
AI_RISK: tay thả đạn cối → tay 1, đạn 1

### SC_171 | 23:10–23:18 | LOC_003 (LOC_003_mortar) | ROK_SOLDIERS | WPN_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from the knoll toward the distant ford, static
IMAGE_PROMPT: Wide from the knoll toward the distant ford, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. Setting @LOC_003_wide: A sandbagged mortar pit on a small grassy knoll at the south end of the hidden valley base at night: two 81mm mortars on bipods, round baseplates, olive ammunition cans, a range card on a stake, dry yellow grass, dark oak scrub slopes, the valley below. Action: Wide at night: the two mortars in their sandbagged pit fire — twin orange flashes lighting the sandbags and the crouched crews — and far out across the dark valley two columns of earth erupt at the stream ford in a one-second glare. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: two muzzle flashes in the pit, a four-second silence, then two distant flashes and earth columns at the ford. Sound: two hollow mortar thumps, silence, two rolling detonations echoing back.
ACTION_START: mortars about to fire
ACTION_END: distant impacts at the ford lit up
NARRATION_KO: 여울에 표적을 등록했습니다. 박격포탄 두 발. 이제 백십팔 발이었습니다.
DIALOGUE_KO: 
SOUND: cối "퉁, 퉁", 4 giây im, hai tiếng nổ dội về.
CONTINUITY: Cối 120→118.
CHAIN_FROM: SC_170
CUT_HALF: no
REFS: WPN_002_ref, LOC_003_wide

### SC_172 | 23:18–23:26 | LOC_003 (LOC_003_hearth) | CHAR_106, CHAR_107, CHAR_004 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot by the hearth, static
IMAGE_PROMPT: Medium shot by the hearth, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Setting @LOC_003_wide: A Goguryeo stone hearth fire at the hidden company base at night: a ring of grey stones, a clay pot over orange flames, brown hemp Goguryeo tents with wooden poles beside olive-green army tents, camouflage netting over dark vehicle shapes behind, dry yellow grass, bare oak scrub. Action: By the stone hearth fire the old blacksmith sits with his bandaged leg stretched out, bundle beside him; as the distant explosions roll in he does not cover his ears — he lifts his head toward the sound, left eye squinting, and nods slowly; the girl in braids and the medic beside him, hands over their ears. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the boom rolls in; the old man lifts his head toward it, squints, nods, and says one line; the two beside him lower their hands. Sound: the echo of two explosions, fire crackling, one line of Korean dialogue.
ACTION_START: old man by fire, explosion arriving
ACTION_END: head raised, nod, line spoken
NARRATION_KO: 을보는 귀를 막지 않았습니다. 대장장이는 쇠 소리를 압니다. 그는 그 소리에서 쇠의 두께를 들었습니다.
DIALOGUE_KO: 을보: 쇠가 우는 소리군.
SOUND: dư âm nổ, lửa bếp.
CONTINUITY: '쇠가 우는 소리군.' Băng chân, búa nhỏ ở thắt lưng.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_refugee_ep1, CHAR_107_refugee_ep1, CHAR_004_ref, LOC_003_wide

### SC_173 | 23:26–23:34 | LOC_003 (LOC_003_hearth) | CHAR_107, CHAR_004 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Setting @LOC_003_wide: A Goguryeo stone hearth fire at the hidden company base at night: a ring of grey stones, a clay pot over orange flames, brown hemp Goguryeo tents with wooden poles beside olive-green army tents, camouflage netting over dark vehicle shapes behind, dry yellow grass, bare oak scrub. Action: The girl in red-threaded braids lowers her hands from her ears and looks at the medic; the medic smiles a little and touches the girl's shoulder; firelight, hemp Goguryeo tents behind. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: hands come down from the ears, the girl asks one line; the medic smiles and touches her shoulder. Sound: fire, wind, one line of Korean dialogue.
ACTION_START: girl with hands on ears
ACTION_END: medic's hand on the girl's shoulder
NARRATION_KO: 아리의 질문에 서아는 답이 없었습니다. 매일 날지, 아무도 몰랐습니다. 열다섯 살에게 이 소리는 어제까지 없던 것이었습니다.
DIALOGUE_KO: 아리: 언니, 저 소리… 매일 나요?
SOUND: lửa bếp, gió.
CONTINUITY: '언니, 저 소리… 매일 나요?'
CHAIN_FROM: SC_172
CUT_HALF: no
REFS: CHAR_107_refugee_ep1, CHAR_004_ref, LOC_003_wide

### SC_174 | 23:34–23:42 | LOC_003 (LOC_003_northridge) | ROK_SOLDIER, XIANBEI_SCOUTS | EQP_001, EQP_002, WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV, monochrome green, static
IMAGE_PROMPT: Night-vision POV, monochrome green, static. ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_003_ford_night: A low grassy ridge north of the valley at night: dry knee-high yellow grass under thin moonlight, bare oak scrub, the dark hollow of a valley below with a faint red glow leaking through camouflage netting. Action: Monochrome green night-vision view from the valley rim: on the ridge to the north three human shapes lie flat in the grass looking down into the valley, glowing faintly, one of them drawing a bow; at the frame edge a gloved hand presses a shoulder handset while the other hand rests on a rifle's selector. Light: Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static green POV: the three prone shapes on the ridge shift slightly, one raising a bow; the gloved hand presses the handset; a safety lever clicks. Sound: night-vision whine, push-to-talk click, a safety catch, wind.
ACTION_START: three shapes prone on ridge
ACTION_END: one shape drawing a bow, handset pressed
NARRATION_KO: 나흘째 밤. 골짜기 북쪽 능선에 셋이 엎드려 있었습니다. 그들도 보고 있었습니다.
DIALOGUE_KO: 
SOUND: rít kính đêm, PTT, chốt an toàn, gió.
CONTINUITY: POV kính đêm lính gác (không mặt).
CHAIN_FROM: —
CUT_HALF: yes
REFS: EQP_001_ref, EQP_002_ref, WPN_001_ref, LOC_003_ford_night
AI_RISK: POV kính đêm + tay trên súng → tay chỉ trên chốt, không cận cò

### SC_175 | 23:42–23:50 | LOC_003 (LOC_003_k2) | CHAR_003, ROK_SOLDIER | VEH_001, WPN_001 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Low wide at the tank, static
IMAGE_PROMPT: Low wide at the tank, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_wide: The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond. Action: Night: an arrow hisses down and sticks in the camouflage netting on the K2 tank's turret roof directly above the stocky sergeant sleeping against the track — he jerks upright; at the valley rim a helmeted soldier fires three single shots toward the north ridge, three muzzle flashes; on the ridge three shapes vanish. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low wide: the arrow thuds into the netting; the sergeant lurches awake; three muzzle flashes from the rim; the shapes on the ridge disappear. Sound: arrow hiss and thud, three single rifle shots, a shout in Korean off-screen.
ACTION_START: sergeant asleep, arrow arriving
ACTION_END: sergeant upright, muzzle flashes at the rim
NARRATION_KO: 화살 하나가 전차의 그물에 박혔습니다. 총성 세 발. 능선은 비었습니다. 탁발흠의 척후는 골짜기를 찾았습니다.
DIALOGUE_KO: 
SOUND: tên rít, cắm lưới, ba phát súng đơn, tiếng "북쪽 능선!" ngoài hình.
CONTINUITY: Tên cắm lưới K2 — vẫn còn ở SC_176/262. Lính bắn = extra xa.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_003_ref, VEH_001_ref, WPN_001_ref, PROP_015_ref, LOC_003_wide
AI_RISK: bắn súng → chớp lửa đầu nòng xa, không cận tay

### SC_176 | 23:50–24:00 | LOC_003 (LOC_003_k2) | CHAR_003, CHAR_001 | VEH_001 | PROPS: PROP_015 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up under a hooded flashlight, slow push-in
IMAGE_PROMPT: Still for ken-burns: close-up under a hooded flashlight, slow push-in. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_wide: The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond. Action: A hooded flashlight lights a broken Goguryeo arrow stuck in the camouflage netting on the K2 tank's turret roof; the stocky sergeant's gloved hand holds the shaft; behind, the captain stands looking off toward the dark north ridge. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push-in on the arrow in the netting. Sound: wind, silence.
ACTION_START: arrow, hand, captain behind
ACTION_END: tight on the arrow
NARRATION_KO: 건전지는 열두 개씩, 나흘. 그 다음은 없었습니다. 그날 밤 열두 개의 야시경이 켜졌습니다. 다음 날 밤엔 여섯 개만 켤 수 있었습니다.
DIALOGUE_KO: 
SOUND: gió, im.
CONTINUITY: Kết P8. Open loop kính đêm.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_001_ref, VEH_001_ref, PROP_015_ref, LOC_003_wide


## [Phần 9] 동쪽 길, 하룻밤 (24:00–27:30) · sa bàn, kế 7 điểm, drone lần 1 · MID-ROLL 4 @27:30

### SC_177 | 24:00–24:08 | LOC_003 (LOC_003_tent_ext) | CHAR_105, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: High angle over the dirt drawing, static
IMAGE_PROMPT: High angle over the dirt drawing, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: Under a hooded flashlight in front of the command tent: the Goguryeo officer kneels and scratches in the bare earth with the tip of a knife — a road, a ford, a valley mouth, a fortress with two small squares for its bastions; the captain, crouched opposite, presses small wooden pegs into the dirt as markers. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static high angle: the knife draws the road and ford, the captain pushes pegs in at the points; no dialogue. Sound: knife scratching earth, pegs pressed in, wind.
ACTION_START: knife starting the road line
ACTION_END: drawing complete, pegs placed
NARRATION_KO: 계획은 흙 위에서 세워졌습니다. 고구려 말객과 대한민국 대위가 같은 흙을 그렸습니다. 한쪽은 흙을 알았고, 한쪽은 총을 알았습니다.
DIALOGUE_KO: 
SOUND: dao vạch đất, que cắm.
CONTINUITY: Sa bàn đất = prop tạm (SC_177–190).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, CHAR_001_ref, LOC_003_wide

### SC_178 | 24:08–24:16 | LOC_003 (LOC_003_tent_ext) | CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot over the dirt map, static
IMAGE_PROMPT: Medium shot over the dirt map, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The Goguryeo officer points the knife tip at the ford on the dirt map north of the road, scratches two strips either side of it — mud — and raps the knife butt on the streambed — stone; flashlight low, white feather on his helmet. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: knife tip on the ford, two strips scratched either side, the butt raps the streambed; he says one line. Sound: knife on earth, a knock, one line of Korean dialogue.
ACTION_START: knife pointing at ford
ACTION_END: knife butt rapping the streambed, line spoken
NARRATION_KO: 여울. 북쪽에서 길로 내려오는 유일한 길목이었습니다. 적도 그리로 올 것이라고 모두 생각했습니다.
DIALOGUE_KO: 해모루: 여울은 북쪽에서 길로 오는 유일한 길목이오. 돌바닥이고 양쪽은 진창이오.
SOUND: dao gõ đất.
CONTINUITY: '여울은 북쪽에서 길로 오는 유일한 길목이오…'
CHAIN_FROM: SC_177
CUT_HALF: no
REFS: CHAR_105_ref, LOC_003_wide

### SC_179 | 24:16–24:24 | LOC_003 (LOC_003_tent_ext) | CHAR_001, CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on hands over the dirt map, static
IMAGE_PROMPT: Close-up on hands over the dirt map, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: Close: the captain's gloved fingers set two pebbles on the two small squares at the fortress's east gate on the dirt map; the Goguryeo officer's leather-gloved hand rests on his knee beside it; he nods once, the white feather dipping into frame. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: two pebbles placed on the two squares, one line from the captain; the feather dips once as the officer nods. Sound: pebbles set on earth, one line of Korean dialogue.
ACTION_START: pebbles being placed
ACTION_END: pebbles on the squares, nod
NARRATION_KO: 치. 성벽에서 튀어나온 돌 망루. 고구려 성의 특징이었습니다. 문 앞을 양쪽에서 쏠 수 있었습니다.
DIALOGUE_KO: 한승우: 동문 치 두 곳. 궁수는 여기.
SOUND: sỏi đặt xuống đất.
CONTINUITY: '동문 치 두 곳. 궁수는 여기.'
CHAIN_FROM: SC_178
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_105_ref, LOC_003_wide

### SC_180 | 24:24–24:34 | LOC_003 (LOC_003_tent_ext) | — | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: top-down on the dirt map, slow slide from the ford to the gate
IMAGE_PROMPT: Still for ken-burns: top-down on the dirt map, slow slide from the ford to the gate. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: Straight down on the dirt map under a red-rimmed flashlight beam: scratched lines, wooden pegs, two pebbles at the gate squares, a spent brass 40mm cartridge case standing at the valley mouth, a small bottle cap at the ford; bare earth and a few grass stalks. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow slide from the ford across the valley mouth to the gate. Sound: wind, silence.
ACTION_START: ford and bottle cap
ACTION_END: gate squares and pebbles
NARRATION_KO: 여울, 골짜기 입구, 동문. 세 곳이 계획의 전부였습니다. 적이 여울로 온다면 세 곳이면 충분했습니다. 계획은 적이 어디로 오느냐에 달려 있었습니다.
DIALOGUE_KO: 
SOUND: gió, im.
CONTINUITY: Sa bàn = red herring (kế đặt trên giả định địch đánh bến).
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_003_wide

### SC_181 | 24:34–24:42 | LOC_003 (LOC_003_tent_ext) | CHAR_001, CHAR_006 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The captain points a wooden peg at the high ground above the ford on the dirt map and looks up at the staff sergeant, who stands with a night-vision monocular folded up on the front of his boonie hat and a painted face; the sergeant nods without a word. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the peg points at the high ground; the captain looks up and gives one order; the sergeant nods once. Sound: wind, one line of Korean dialogue.
ACTION_START: peg on the high ground
ACTION_END: sergeant's nod
NARRATION_KO: 여섯 명과 야시경 여섯 개. 싸우지 않는 눈이 가장 오래 보는 법이었습니다.
DIALOGUE_KO: 한승우: 백 중사, 여섯 명. 고지에서 방향만 보고한다.
SOUND: cần kính đêm gập.
CONTINUITY: Kính đêm gập trên mũ boonie (EQP_001 mount).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_006_facepaint_ep1, EQP_001_ref, LOC_003_wide

### SC_182 | 24:42–24:50 | LOC_003 (LOC_003_tent_ext) | CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The boyish private hugs a freshly charged grey quadcopter to his chest, two batteries strapped on his body armor, the controller on his harness; he looks down at the bottle cap on the dirt map where the captain's finger points and speaks. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he looks from the bottle cap up to the captain and says one line, hugging the drone. Sound: wind, one line of Korean dialogue.
ACTION_START: looking down at the dirt map
ACTION_END: looking up, line spoken
NARRATION_KO: 이십사 분. 밤새 지켜야 할 길에 하늘 눈은 이십사 분뿐이었습니다. 태오는 그것을 둘로 나눴습니다.
DIALOGUE_KO: 장태오: 2호기, 두 번 비행. 열두 분씩만 씁니다.
SOUND: gió.
CONTINUITY: Drone #2, 2 lần bay × 12 phút.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, UAV_001_ref, LOC_003_wide

### SC_183 | 24:50–24:58 | LOC_003 (LOC_003_tent_ext) | CHAR_001, CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static, low over the dirt map
IMAGE_PROMPT: Medium two-shot, static, low over the dirt map. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The captain stands the spent brass 40mm cartridge case at the valley mouth on the dirt map and keeps his gloved hand on it, looking up at the tall lieutenant across the map; red-rimmed flashlight, goggles on the lieutenant's helmet. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the cartridge case is set down, the hand stays on it, the captain looks up and gives one order; the lieutenant's jaw sets. Sound: brass on earth, one line of Korean dialogue.
ACTION_START: setting the cartridge case
ACTION_END: hand on the case, eyes on the lieutenant
NARRATION_KO: 안 쫓는다. 이 계획에서 가장 어려운 명령이었습니다. 오태민은 그 자리를 견디는 법을 배운 적이 없었습니다.
DIALOGUE_KO: 한승우: 천둥 2, 3은 골짜기 입구. 안 쫓는다.
SOUND: đồng chạm đất.
CONTINUITY: '천둥 2, 3은 골짜기 입구. 안 쫓는다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_002_ref, LOC_003_wide

### SC_184 | 24:58–25:06 | LOC_003 (LOC_003_tent_ext) | CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: Close on the tall lieutenant: jaw clenched, eyes down on the brass cartridge case below the frame, red light on his rectangular face, a long beat, then a reluctant nod. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the jaw works, eyes down, a long beat, then one reluctant nod and one grudging line. Sound: wind, one line of Korean dialogue.
ACTION_START: jaw clenched, eyes down
ACTION_END: nod, line spoken
NARRATION_KO: 그는 약속했습니다. 그 약속은 세 시간을 갔습니다.
DIALOGUE_KO: 오태민: …안 쫓습니다.
SOUND: gió.
CONTINUITY: '…안 쫓습니다.' — lời hứa 3 giờ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_ref, LOC_003_wide

### SC_185 | 25:06–25:14 | LOC_003 (LOC_003_tent_ext) | CHAR_105 | — | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The Goguryeo officer scratches a circle on the hill above the ford on the dirt map with the knife and touches the curved black buffalo-horn trumpet slung at his hip; red-rimmed flashlight, white feather. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the knife draws the circle, his hand goes to the horn at his hip, he says one line. Sound: knife on earth, the horn knocking against armor, one line of Korean dialogue.
ACTION_START: drawing the circle
ACTION_END: hand on the horn, line spoken
NARRATION_KO: 나각 한 번. 삼백 기는 한 번만 쓸 수 있었습니다. 부는 때는 해모루가 정했습니다.
DIALOGUE_KO: 해모루: 삼백 기는 여울 위 언덕에 숨소. 신호는 나각이오.
SOUND: dao vạch, tù và chạm giáp.
CONTINUITY: Tù và (PROP_018) — hiệu lệnh SC_234.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, LOC_003_wide

### SC_186 | 25:14–25:22 | LOC_003 (LOC_003_tent_ext) | CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, static
IMAGE_PROMPT: Medium close-up, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The Goguryeo officer points the knife at the east gate on the dirt map and speaks for the fortress commander who is inside the walls; dust on his cheekbones in the red-rimmed light. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: knife on the gate, one line. Sound: wind, one line of Korean dialogue.
ACTION_START: knife moving to the gate
ACTION_END: line delivered
NARRATION_KO: 문이 열리는 순간 성은 벌판이 되었습니다. 그래서 오백을 문 안에 세웠습니다.
DIALOGUE_KO: 해모루: 성주께서 보병 오백으로 문을 지키실 것이오. 수레가 올 때만 여실 것이오.
SOUND: gió.
CONTINUITY: '성주께서 보병 오백으로 문을 지키실 것이오…'
CHAIN_FROM: SC_185
CUT_HALF: no
REFS: CHAR_105_ref, LOC_003_wide

### SC_187 | 25:22–25:30 | LOC_003 (LOC_003_k2) | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond. Action: The stocky sergeant stands beside the K2 tank under its netting and pats the thick side skirt twice with his palm like a horse's neck, then looks toward the dirt map off-frame; thin moonlight on the netting. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: two pats on the side skirt, he looks over toward the planning group and says one line. Sound: palm on steel twice, wind, one line of Korean dialogue.
ACTION_START: hand rising to the skirt
ACTION_END: looking off, line spoken
NARRATION_KO: 시동을 끈 전차. 기름을 아끼는 가장 확실한 방법이었습니다. 박기철에게 시동 소리는 곧 기름 냄새였습니다.
DIALOGUE_KO: 박기철: 전차는 그물 밑. 시동 끕니다.
SOUND: tay vỗ thép.
CONTINUITY: '전차는 그물 밑. 시동 끕니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_003_wide

### SC_188 | 25:30–25:40 | LOC_003 (LOC_003_k2) | CHAR_003 | VEH_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide of the tank at night, slow push toward the gun barrel
IMAGE_PROMPT: Still for ken-burns: medium-wide of the tank at night, slow push toward the gun barrel. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond. Action: The K2 tank under camouflage netting in the dark valley, a thin moon glinting along its long 120mm gun barrel; the stocky sergeant sits on the ground leaning against the track, the green notebook on his knee, patrol cap tipped forward. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push along the gun barrel. Sound: wind, silence.
ACTION_START: tank and sergeant
ACTION_END: tight on the barrel
NARRATION_KO: 스물두 발은 그대로였습니다. 이 밤에도 전차는 울지 않을 것이었습니다. 박기철은 그 옆에서 잤습니다. 자식 옆에서 자는 아비처럼.
DIALOGUE_KO: 
SOUND: gió, im.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_003_wide

### SC_189 | 25:40–25:48 | LOC_003 (LOC_003_tent_ext) | CHAR_106, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The old blacksmith limps up to the dirt map, cloth bundle retied on his back, small hammer at his belt, white bandage on his lower leg, and speaks to the captain the way an old man speaks to a grandson; red-rimmed flashlight. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he limps in, stops, and says one line to the captain. Sound: a foot dragging, wind, one line of Korean dialogue.
ACTION_START: old man limping in
ACTION_END: stopped, line spoken
NARRATION_KO: 마지막 수레는 을보의 아우네 것이었습니다. 남은 피붙이가 그 수레 위에 있었습니다.
DIALOGUE_KO: 을보: 마지막 수레는 내 아우네 것이야. 내가 타고 가겠네.
SOUND: chân lết, gió.
CONTINUITY: '마지막 수레는 내 아우네 것이야…'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_refugee_ep1, CHAR_001_ref, LOC_003_wide

### SC_190 | 25:48–25:56 | LOC_003 (LOC_003_tent_ext) | CHAR_001, CHAR_004, CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium three-shot, static
IMAGE_PROMPT: Medium three-shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The captain looks at the old man's back as he limps away, then at the medic — she shakes her head slightly (the leg) — then turns to the staff sergeant standing close, and gives an order; red-rimmed light, painted face, red cross armband. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the captain's eyes follow the old man off, go to the medic's small head shake, then to the sergeant; one order. Sound: wind, one line of Korean dialogue.
ACTION_START: captain watching the old man leave
ACTION_END: captain turned to the sergeant, order given
NARRATION_KO: 한승우는 말리지 않았습니다. 이 땅의 노인에게 명령할 권한은 그에게 없었습니다.
DIALOGUE_KO: 한승우: 백 중사, 영감님 수레 뒤에 둘 붙여.
SOUND: gió.
CONTINUITY: '백 중사, 영감님 수레 뒤에 둘 붙여.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_004_ref, CHAR_006_facepaint_ep1, LOC_003_wide

### SC_191 | 25:56–26:04 | LOC_003 (LOC_003_tent_ext) | CHAR_107, CHAR_106 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot beside the tents, static
IMAGE_PROMPT: Medium two-shot beside the tents, static. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The girl in red-threaded braids runs up and grabs the old blacksmith's hemp sleeve; he pries her fingers loose gently, places her hand into the hand of the medic arriving beside them, shakes his head, and says nothing; hemp tent behind, faint red light. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: she runs in, grabs his sleeve with one line; he loosens her fingers, puts her hand into the medic's hand, shakes his head. Sound: hemp cloth, breathing, one line of Korean dialogue.
ACTION_START: girl grabbing the sleeve
ACTION_END: girl's hand placed in the medic's hand, head shake
NARRATION_KO: 아리에게 마을에서 남은 것은 할아버지 하나였습니다. 그 하나가 수레로 갔습니다. 열다섯 살의 세상은 하룻밤 사이에 노인 하나로 줄었습니다.
DIALOGUE_KO: 아리: 할아버지, 저도 가요.
SOUND: vải gai, thở.
CONTINUITY: '할아버지, 저도 가요.' 3 người trong khung nhưng chỉ 2 CHAR chính rõ (서아 tay).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_refugee_ep1, CHAR_106_refugee_ep1, LOC_003_wide

### SC_192 | 26:04–26:12 | LOC_003 (LOC_003_tent_ext) | CHAR_004, CHAR_107 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close. Setting @LOC_003_wide: Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes. Action: The medic draws the girl in and wraps an arm around her shoulders, both looking after the old man's back disappearing into the dark between the tents; faint red light on the medic's armband and the girl's braids. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the arm goes around the girl's shoulders, both watch the dark, the medic says one line. Sound: wind, a small sob, one line of Korean dialogue.
ACTION_START: drawing the girl in
ACTION_END: arm around her, watching the dark
NARRATION_KO: 서아에게 아리는 첫 번째 환자가 아니라 첫 번째 동생이었습니다. 동생은 환자보다 어려웠습니다.
DIALOGUE_KO: 윤서아: 아리는 나랑 여기 있어요.
SOUND: gió, tiếng nấc nhỏ.
CONTINUITY: '아리는 나랑 여기 있어요.'
CHAIN_FROM: SC_191
CUT_HALF: no
REFS: CHAR_004_ref, CHAR_107_refugee_ep1, LOC_003_wide

### SC_193 | 26:12–26:22 | LOC_003 (LOC_003_hill_ford) | CHAR_006, CHAR_105, GOG_CAVALRYMEN, ROK_SOLDIERS | VEH_101, EQP_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide on the dark hill, slow lateral slide
IMAGE_PROMPT: Still for ken-burns: wide on the dark hill, slow lateral slide. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: Night on the grassy hill above the ford: Goguryeo cavalrymen lead their armored horses up the slope in the dark, red plumes black in the moonlight; beside them the staff sergeant and five helmeted soldiers climb with night-vision monoculars flipped down, the lenses catching a faint green glint; the Goguryeo officer at the head. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow lateral slide along the climbing line. Sound: muffled hooves, armor, night-vision mounts folding down.
ACTION_START: cavalry and scouts climbing
ACTION_END: slid along to the officer at the head
NARRATION_KO: 고구려 기병과 야시경이 같은 언덕에 올랐습니다. 이런 밤은 처음이었습니다. 천사백 년의 거리가 언덕 하나에 있었습니다. 누구도 그 거리를 말하지 않았습니다.
DIALOGUE_KO: 
SOUND: vó ngựa êm, giáp, cần kính đêm gập.
CONTINUITY: '1.400 năm trên một ngọn đồi'. Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, CHAR_105_ref, VEH_101_ref, EQP_001_ref, LOC_003_ford_night
AI_RISK: kỵ binh + lính đêm → silhouette, tĩnh

### SC_194 | 26:22–26:30 | LOC_003 (LOC_003_mouth) | CHAR_005 | VEH_002, UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen beside the IFV, static
IMAGE_PROMPT: Close-up on the controller screen beside the IFV, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: At the valley mouth beside a K21 IFV the boyish private holds the controller: its screen shows a blue-white thermal aerial view — a long line of ox carts and walking figures as bright dots moving along a dark road; no HUD text; his face lit cold blue. Light: Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the thermal dots crawl along the road on the screen; he reports one line. Sound: rotor buzz through the speaker, one line of Korean dialogue.
ACTION_START: thermal screen: cart column
ACTION_END: same, column advanced, line spoken
NARRATION_KO: 사 킬로. 수레의 걸음으로 한 시간이었습니다. 한 시간 뒤면 여울이었습니다. 계획대로라면.
DIALOGUE_KO: 장태오: 수레 행렬, 사 킬로. 앞은 아직 조용합니다.
SOUND: rotor qua loa.
CONTINUITY: Drone #2 lần bay 1. Ảnh nhiệt = trắng-xanh.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_ref, VEH_002_ref, UAV_001_ref, LOC_003_wide
AI_RISK: màn hình nhiệt → không HUD số

### SC_195 | 26:30–26:38 | LOC_003 (LOC_003_mouth) | CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen, static
IMAGE_PROMPT: Close-up on the controller screen, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The controller's thermal view pans north: behind the dark ridge a dense mass of bright dots packed in ranks — hundreds of horses and riders massing; the boyish private swallows, thumb frozen on the stick, blue light on his face. Light: Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the view pans to the massed dots behind the ridge; he swallows and reports one line. Sound: rotor buzz, a beep, a dry swallow, one line of Korean dialogue.
ACTION_START: screen panning north
ACTION_END: massed dots on screen, line spoken
NARRATION_KO: 수백. 여울이 아니라 북쪽 언덕 뒤였습니다. 계획은 여울이었습니다. 태오는 그것을 보고했습니다. 아무도 계획을 바꾸지 않았습니다.
DIALOGUE_KO: 장태오: 북쪽 언덕 뒤… 기병 집결. 수백입니다.
SOUND: rotor, bíp.
CONTINUITY: Kỵ binh tập kết sau gò bắc — không ở bến.
CHAIN_FROM: SC_194
CUT_HALF: no
REFS: CHAR_005_ref, UAV_001_ref, LOC_003_wide

### SC_196 | 26:38–26:46 | LOC_003 (LOC_003_mouth) | CHAR_105, CHAR_001 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium shot over the private's shoulder, static
IMAGE_PROMPT: Medium shot over the private's shoulder, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The Goguryeo officer leans in over the private's shoulder to look at the glowing thermal screen — the first time he has seen the iron bird see in the dark — then turns to the captain beside him with real curiosity, white feather catching the screen glow. Light: Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he leans in, stares at the screen, straightens and asks the captain one line. Sound: rotor buzz through the speaker, armor creaking, one line of Korean dialogue.
ACTION_START: officer leaning over the screen
ACTION_END: officer turned to the captain, question asked
NARRATION_KO: 해모루는 두려워하지 않았습니다. 그는 물었습니다. 그것이 그와 수나라 총관의 차이였습니다. 두려움 없이 묻는 자가 가장 빨리 배웁니다.
DIALOGUE_KO: 해모루: 그 쇠새가 밤에도 보오?
SOUND: rotor qua loa, giáp.
CONTINUITY: '그 쇠새가 밤에도 보오?' (태오 chỉ là vai).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, CHAR_001_ref, UAV_001_ref, LOC_003_wide

### SC_197 | 26:46–26:54 | LOC_003 (LOC_003_mouth) | CHAR_001 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The captain looks at the thermal screen, then at the Goguryeo officer, answers shortly, and raises a hand signaling the private to bring the drone home; blue screen glow, the dark valley mouth. Light: Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: eyes to the screen, to the officer, one short line, then the hand signal to recall. Sound: rotor buzz, one line of Korean dialogue.
ACTION_START: looking at the screen
ACTION_END: hand raised in the recall signal
NARRATION_KO: 밤에 더 잘 본다. 해모루는 그 말을 기억했습니다. 그는 배운 것을 잊지 않는 사람이었습니다.
DIALOGUE_KO: 한승우: 밤에 더 잘 봅니다.
SOUND: rotor.
CONTINUITY: '밤에 더 잘 봅니다.'
CHAIN_FROM: SC_196
CUT_HALF: no
REFS: CHAR_001_ref, UAV_001_ref, LOC_003_wide

### SC_198 | 26:54–27:04 | LOC_003 (LOC_003_hill_ford) | CHAR_006, XIANBEI_SCOUTS | EQP_001, VEH_206 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: night-vision POV, monochrome green, slow push toward a crawling figure
IMAGE_PROMPT: Still for ken-burns: night-vision POV, monochrome green, slow push toward a crawling figure. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: Monochrome green night-vision view with heavy grain: on the grassy slope thirty meters away a lone Xianbei scout crawls flat through the grass toward the camera, bow on his back; either side of the frame the faint warm shapes of six prone soldiers lie motionless. Light: Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push toward the crawling figure. Sound: wind, dry grass barely moving, night-vision whine.
ACTION_START: crawler small, six shapes either side
ACTION_END: tight on the crawler
NARRATION_KO: 첫 비행이 끝났습니다. 남은 것은 열두 분이었습니다. 그 열두 분을 쓰기도 전에, 언덕 위로 누군가 기어오고 있었습니다.
DIALOGUE_KO: 
SOUND: gió, cỏ khô rất khẽ, rít kính đêm.
CONTINUITY: POV 백성민 (ref chỉ để giữ thiết bị). Trinh sát Tiên Ti bò lên.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_facepaint_ep1, EQP_001_ref, VEH_206_ref, LOC_003_ford_night
AI_RISK: POV kính đêm → green mono, không HUD

### SC_199 | 27:04–27:12 | LOC_003 (LOC_003_hill_ford) | CHAR_006, XIANBEI_SCOUTS, ROK_SOLDIER | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low medium shot in the grass, static, then cut to a soldier's face
IMAGE_PROMPT: Low medium shot in the grass, static, then cut to a soldier's face. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: Night in the grass: the staff sergeant lies flat, night-vision monocular flipped up on his boonie hat, a fixed-blade knife drawn silently from his chest armor; a Xianbei scout in leather lamellar crawls past an arm's length away; the sergeant's hand clamps over the scout's mouth and pulls him down into the grass; no blade edge visible, no blood; nearby a young helmeted soldier shuts his eyes. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low: the scout crawls past; the hand clamps over his mouth and drags him down out of frame; cut to the young soldier beside closing his eyes; no blade shown, no blood. Sound: grass crushed, one choked breath, then wind.
ACTION_START: scout crawling past, sergeant flat
ACTION_END: scout pulled down out of frame, soldier's eyes shut
NARRATION_KO: 언덕 위에서 첫 번째 피가 흘렀습니다. 소리는 나지 않았습니다. 탁발흠은 그 척후를 다시 보지 못했습니다.
DIALOGUE_KO: 
SOUND: cỏ đè, một tiếng thở bị chặn, rồi gió.
CONTINUITY: Máu đầu tiên — không cận lưỡi dao, không máu. Lính bên = extra.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, EQP_001_ref, LOC_003_ford_night
AI_RISK: dao + giết → không lưỡi dao cận, không máu; 1 chuyển động tay

### SC_200 | 27:12–27:20 | LOC_003 (LOC_003_westrim) | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: From behind, pulling out wide, single move  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: From behind, pulling out wide, single move. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_wide: The western rim of the hidden valley at night: dry yellow grass and bare oak scrub on the crest, and beyond it the whole dark plain covered with tens of thousands of Sui campfires like a field of fallen stars to the horizon, the black mass of the Goguryeo fortress in between. Action: The captain climbs to the western rim of the valley and stops; below and beyond him the whole night plain is covered with tens of thousands of Sui campfires to the horizon like a field of fallen stars, the black mass of the fortress between; he stands very still. Light: Night from high above, tens of thousands of orange campfires on a black plain, thin moonlight. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera behind him pulls slowly back and up, the field of campfires opening wider and wider beyond his silhouette; he does not move. Sound: wind, many layers of distant drums.
ACTION_START: captain reaching the rim, fires beyond
ACTION_END: wide, captain small against the field of fires
NARRATION_KO: 불빛 하나가 천막 하나였습니다. 그는 세다가 그만두었습니다. 백만은 셀 수 없는 숫자였습니다. 그래서 그는 아흔네 명만 셌습니다.
DIALOGUE_KO: 
SOUND: gió, trống Tùy xa nhiều lớp.
CONTINUITY: Hàng vạn đốm lửa. Aerial-ish.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_003_wide

### SC_201 | 27:20–27:30 | LOC_003 (LOC_003_westrim) | CHAR_001 | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide, silhouette foreground, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide, silhouette foreground, slow pull-out. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Setting @LOC_003_wide: The western rim of the hidden valley at night: dry yellow grass and bare oak scrub on the crest, and beyond it the whole dark plain covered with tens of thousands of Sui campfires like a field of fallen stars to the horizon, the black mass of the Goguryeo fortress in between. Action: The captain's silhouette in the foreground on the rim; the night plain below scattered with countless orange campfires to the horizon like stars fallen to the ground; thin moon. Light: Night from high above, tens of thousands of orange campfires on a black plain, thin moonlight. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow pull-out. Sound: wind, distant drums.
ACTION_START: silhouette and fires
ACTION_END: pulled out, fires to the horizon
NARRATION_KO: 불빛 아래 백만이 잠들어 있었습니다. 그중 이천은 깨어 있었습니다. 계획은 완벽했습니다. 적이 그 계획대로 와 준다면.
DIALOGUE_KO: 
SOUND: gió, trống xa.
CONTINUITY: Mid-roll 4 @27:30 sau cảnh này. Open loop P9.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, LOC_003_wide


## [Phần 10] 동문 야전 (27:30–34:30) · 6 phase · narrator im 31:30–33:00 · CUT_HALF toàn khối

### SC_202 | 27:30–27:38 | LOC_003 (LOC_003_ford) | CHAR_006, XIANBEI_SCOUTS | EQP_001, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV from the hill, monochrome green, static
IMAGE_PROMPT: Night-vision POV from the hill, monochrome green, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A shallow stream ford north of the valley mouth at night: a bed of pale grey cobbles under a hand's depth of black water, wide banks of dark grey mud on both sides, dry yellow reeds and grass, a low grassy ridge rising to the north, thin moonlight. Action: Monochrome green night-vision view with heavy grain: below, the pale cobble ford glows faintly between two dark mud banks; from the north a long file of Xianbei horsemen wades down into the water, riders and horses as bright moving shapes; no HUD text. Light: Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static green POV: the file of horsemen wades into the ford, more and more shapes entering the water; no dialogue, no narration. Sound: wind, faint distant splashing, night-vision whine.
ACTION_START: first riders entering the ford
ACTION_END: long file in the water
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: gió, tiếng nước rất xa, kính đêm rít nhẹ.
CONTINUITY: Sau mid-roll 4: không thoại. Phase 1 bắt đầu. CUT_HALF toàn P10.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, EQP_001_ref, VEH_206_ref, LOC_003_ford_night
AI_RISK: POV kính đêm + kỵ số đông → hình khối xanh, không chi tiết

### SC_203 | 27:38–27:46 | LOC_003 (LOC_003_hill_ford) | CHAR_006 | EQP_001, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, low in the grass, static
IMAGE_PROMPT: Close-up, low in the grass, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: The staff sergeant lies prone in the dark grass, the night-vision monocular down over his left eye glowing faintly green, painted face, boonie hat, one hand pressing the shoulder handset; he speaks in flat telegraphic phrases. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the handset is pressed and he reports one flat line, rhythm never changing. Sound: push-to-talk click, wind, one line of Korean dialogue.
ACTION_START: prone, handset rising
ACTION_END: handset pressed, line delivered
NARRATION_KO: 사백. 이천 중 사백이었습니다.
DIALOGUE_KO: 백성민: 고지. 기병 사백, 여울 진입. 북에서 남.
SOUND: PTT, gió.
CONTINUITY: '고지. 기병 사백, 여울 진입. 북에서 남.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, EQP_001_ref, EQP_002_ref, LOC_003_ford_night

### SC_204 | 27:46–27:54 | LOC_003 (LOC_003_mortar) | ROK_SOLDIERS | WPN_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot in the mortar pit, static
IMAGE_PROMPT: Medium shot in the mortar pit, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. Setting @LOC_003_wide: A sandbagged mortar pit on a small grassy knoll at the south end of the hidden valley base at night: two 81mm mortars on bipods, round baseplates, olive ammunition cans, a range card on a stake, dry yellow grass, dark oak scrub slopes, the valley below. Action: In the sandbagged mortar pit at night a helmeted gunner reads a range card on a stake by red flashlight and nods to the crew beside the second mortar; two men lift finned bombs ready in both hands; faces down under helmet brims. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the gunner reads the card, nods across; two bombs come up ready; one order called. Sound: mortar bombs clicking, one line of Korean dialogue.
ACTION_START: gunner reading the card
ACTION_END: bombs held ready, order called
NARRATION_KO: 
DIALOGUE_KO: 사수: 박격포, 여울 제원 사격. 여덟 발.
SOUND: đạn cối lách cách.
CONTINUITY: '박격포, 여울 제원 사격. 여덟 발.' Lính không mặt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_002_ref, LOC_003_wide

### SC_205 | 27:54–28:02 | LOC_003 (LOC_003_mortar) | ROK_SOLDIERS | WPN_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-wide on the pit, static
IMAGE_PROMPT: Medium-wide on the pit, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. Setting @LOC_003_wide: A sandbagged mortar pit on a small grassy knoll at the south end of the hidden valley base at night: two 81mm mortars on bipods, round baseplates, olive ammunition cans, a range card on a stake, dry yellow grass, dark oak scrub slopes, the valley below. Action: The two mortars fire in quick succession — orange flashes lighting the sandbag walls and the crouched crews — the gunners dropping bomb after bomb into the tubes without looking, four each, empty green plastic cases scattered. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: flash, flash, flash — bombs dropped and fired in fast rhythm, the crews' hands moving mechanically; eight rounds. Sound: rapid hollow mortar thumps, cases clattering.
ACTION_START: first bomb dropping
ACTION_END: last of eight fired, crews still
NARRATION_KO: 등록된 표적이었습니다. 조준은 필요 없었습니다.
DIALOGUE_KO: 
SOUND: "퉁, 퉁, 퉁" dồn dập.
CONTINUITY: Cối −8 (118→110).
CHAIN_FROM: SC_204
CUT_HALF: yes
REFS: WPN_002_ref, LOC_003_wide
AI_RISK: lặp chuyển động → nhịp đơn giản, tay không cận

### SC_206 | 28:02–28:10 | LOC_003 (LOC_003_ford) | — | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision view from the hill, monochrome green, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Night-vision view from the hill, monochrome green, static. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A shallow stream ford north of the valley mouth at night: a bed of pale grey cobbles under a hand's depth of black water, wide banks of dark grey mud on both sides, dry yellow reeds and grass, a low grassy ridge rising to the north, thin moonlight. Action: Monochrome green night-vision view from the hill: mortar bombs burst in the middle of the file of horsemen wading the ford — columns of water and cobbles leap up white-green, horses go down in the water, the leading riders scatter to both banks; no close wounded. Light: Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static green view: eight bursts walk through the ford one after another, water and stone geysering, the file breaking apart to both banks. Sound: eight detonations rolling across the water, horses screaming.
ACTION_START: file in the ford, first burst
ACTION_END: ford churned, riders scattering
NARRATION_KO: 선두는 물속에서 멈췄습니다. 물속에서 멈춘 기병은 과녁이었습니다.
DIALOGUE_KO: 
SOUND: tám tiếng nổ dội qua nước, ngựa hí.
CONTINUITY: Không thương vong cận.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, LOC_003_ford_night
AI_RISK: nổ + ngựa → green POV xa, hình khối

### SC_207 | 28:10–28:18 | LOC_003 (LOC_003_hill_ford) | ROK_SOLDIERS | WPN_003, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from the hill down to the ford, static
IMAGE_PROMPT: Wide from the hill down to the ford, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: From the hill at night: a light machine gun on its bipod in the grass pours a slanting line of bright tracer down at the ford; below, horsemen in the water wheel and scramble back up the north bank; muzzle flash lights the gunner's helmet from below, face hidden. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the tracer stream pours down into the ford, the horsemen turn and climb the north bank. Sound: long machine-gun bursts, splashing.
ACTION_START: first tracers leaving the gun
ACTION_END: horsemen retreating up the north bank
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: K3 quét dài, nước.
CONTINUITY: K3 từ gò.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_003_ref, VEH_206_ref, LOC_003_ford_night

### SC_208 | 28:18–28:26 | LOC_003 (LOC_003_mouth) | CHAR_001 | VEH_004, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot beside the command vehicle, static
IMAGE_PROMPT: Medium shot beside the command vehicle, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: At the valley mouth beside the 4x4 command vehicle the captain stands with the radio handset at his ear, eyes on the distant ford where fire flickers; helmet on, compass at his throat, thin moonlight. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: handset at the ear, distant flashes on his face, one order. Sound: push-to-talk click, distant detonations, one line of Korean dialogue.
ACTION_START: handset up, watching
ACTION_END: order given
NARRATION_KO: 쫓지 않는 것. 계획의 첫 번째 시험이었습니다.
DIALOGUE_KO: 한승우: 천둥 2, 접촉. 안 쫓는다.
SOUND: PTT, nổ xa.
CONTINUITY: '천둥 2, 접촉. 안 쫓는다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, LOC_003_wide

### SC_209 | 28:26–28:34 | LOC_003 (LOC_003_mouth) | — | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from behind the IFV at the valley mouth, static
IMAGE_PROMPT: Wide from behind the IFV at the valley mouth, static. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: From behind a K21 IFV (white numeral 2) parked at the valley mouth at night: its short 40mm autocannon fires a burst toward the ford — earth erupting at the water's north edge in the distance — and the vehicle does not move from its position. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: three flashes from the autocannon, three distant earth bursts at the water's edge; the vehicle stays put. Sound: three sharp 40mm reports, distant impacts.
ACTION_START: vehicle static, gun aimed
ACTION_END: impacts at the water's edge, vehicle unmoved
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: 40mm ba phát, dội.
CONTINUITY: 천둥 2 giữ vị trí.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, LOC_003_wide

### SC_210 | 28:34–28:42 | LOC_003 (LOC_003_northridge) | CHAR_205, XIANBEI_SCOUTS | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, low angle, static
IMAGE_PROMPT: Medium shot, low angle, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A low grassy ridge north of the valley at night: dry knee-high yellow grass under thin moonlight, bare oak scrub, the dark hollow of a valley below with a faint red glow leaking through camouflage netting. Action: On the north ridge behind his formation the bareheaded Xianbei commander watches the ford flashing below without any change of expression; he raises his arm and spreads three fingers; the riders around him split into three streams in the dark. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: distant flashes flicker on his face; the arm rises, three fingers spread; around him the horsemen divide into three moving streams. Sound: distant detonations, hooves separating in three directions.
ACTION_START: commander watching, arm down
ACTION_END: three fingers up, riders dividing
NARRATION_KO: 탁발흠은 사백을 보냈습니다. 자신은 가지 않았습니다.
DIALOGUE_KO: 
SOUND: nổ xa, vó ngựa tách hướng.
CONTINUITY: 탁발흠 không xuống bến. Chia 3.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, VEH_206_ref, LOC_003_ford_night

### SC_211 | 28:42–28:50 | LOC_003 (LOC_003_mouth) | CHAR_005 | VEH_002, UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen and the private's face, static
IMAGE_PROMPT: Close-up on the controller screen and the private's face, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: Beside the K21 IFV the boyish private holds the controller: the thermal screen shows the mass of bright dots on the north ridge splitting into three; his mouth opens and he shouts into the shoulder handset; blue glow on his face. Light: Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the dots on the screen split three ways; he shouts one line into the radio. Sound: rotor buzz, push-to-talk, one shouted line of Korean dialogue.
ACTION_START: dots massed on screen
ACTION_END: dots in three groups, line shouted
NARRATION_KO: 탁발흠은 첫 파도로 여울을 샀습니다. 그 값으로 이쪽의 눈을 여울에 묶었습니다.
DIALOGUE_KO: 장태오: 기병… 셋으로 갈라집니다!
SOUND: rotor qua loa, PTT.
CONTINUITY: Drone #2 lần bay 2.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_005_ref, VEH_002_ref, UAV_001_ref, LOC_003_wide

### SC_212 | 28:50–28:58 | LOC_003 (LOC_003_mouth) | CHAR_005 | UAV_001 | PROPS: PROP_005 | TYPE: video8s | 8s
SHOT: Close-up on the controller screen, private's finger in frame, static
IMAGE_PROMPT: Close-up on the controller screen, private's finger in frame, static. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. dark grey handheld drone controller with two thumbsticks, a seven-inch screen mounted on top showing a live aerial feed, two folding antennas, neck strap. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The thermal screen: one group halts short of the ford and tiny hot sparks arc from it toward the valley mouth — fire arrows; the two larger groups sweep around the north ridge toward the east road; the boyish private's finger jabs the screen. Light: Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: sparks arc on the screen, the two big groups curve around the ridge; the finger stabs the glass; one line. Sound: rotor buzz, a beep, one line of Korean dialogue.
ACTION_START: screen: groups beginning to move
ACTION_END: finger on the screen, line spoken
NARRATION_KO: 두 무리. 천 기 이상이 수레로 향했습니다.
DIALOGUE_KO: 장태오: 두 무리가 북쪽 언덕을 돕니다. 수레 쪽입니다!
SOUND: rotor, bíp.
CONTINUITY: '두 무리가 북쪽 언덕을 돕니다. 수레 쪽입니다!'
CHAIN_FROM: SC_211
CUT_HALF: yes
REFS: CHAR_005_ref, UAV_001_ref, LOC_003_wide

### SC_213 | 28:58–29:06 | LOC_003 (LOC_003_mouth) | CHAR_002 | VEH_002, EQP_001 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium shot at the IFV's commander hatch, static
IMAGE_PROMPT: Medium shot at the IFV's commander hatch, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: A fire arrow with a burning cloth-wrapped head thumps into the grass a few meters in front of a K21 IFV (white numeral 3) and small flames lick outward; in the open hatch the tall lieutenant jerks his night-vision monocular up off his eye against the glare and stares toward the ford — no archer visible. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the fire arrow lands and the grass catches; the lieutenant flips the monocular up, squints toward the dark ford; nobody speaks. Sound: the fire arrow hissing in, grass crackling.
ACTION_START: arrow landing in grass
ACTION_END: grass burning, lieutenant staring
NARRATION_KO: 불화살은 맞히기 위한 것이 아니었습니다. 붙들어 두기 위한 것이었습니다.
DIALOGUE_KO: 
SOUND: tên lửa rít, cỏ cháy lép bép.
CONTINUITY: Tên lửa = ghìm chân. Kính đêm gập lên.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, EQP_001_ref, LOC_003_wide

### SC_214 | 29:06–29:14 | LOC_003 (LOC_003_northridge) | CHAR_205 | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Lateral tracking shot in the dark
IMAGE_PROMPT: Lateral tracking shot in the dark. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A low grassy ridge north of the valley at night: dry knee-high yellow grass under thin moonlight, bare oak scrub, the dark hollow of a valley below with a faint red glow leaking through camouflage netting. Action: The bareheaded Xianbei commander leads the main body at a gallop around the flank of the north ridge in darkness, bow in hand, no torches; the horsemen flow behind him through the grass like water; thin moonlight on the braid and leather armor. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera tracks sideways with the galloping commander and the dark flow of riders behind him; no shouting, only hooves. Sound: massed hooves, no voices.
ACTION_START: commander galloping into frame
ACTION_END: riders flowing past behind him
NARRATION_KO: 그는 쇠수레를 노리지 않았습니다. 총관의 명령은 쌀이었습니다. 그는 명령을 정확히 읽었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa dồn, không tiếng hô.
CONTINUITY: Không đuốc, không tiếng hô.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, VEH_206_ref, LOC_003_ford_night
AI_RISK: kỵ binh đêm tracking → bóng tối, 1 mặt rõ

### SC_215 | 29:14–29:22 | LOC_002 (LOC_002_eastroad) | REFUGEES | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium-wide on the road, static
IMAGE_PROMPT: Medium-wide on the road, static. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: Night on the east road: a line of ox carts heaped with grain sacks climbs the slope toward the fortress's east gate, refugees walking either side, a few torches; from the black north comes the sound of hooves — heads turn, an ox stops. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: carts creak uphill; heads turn toward the dark north; an ox halts; a first scream. Sound: wooden wheels, hooves approaching, the first scream.
ACTION_START: column moving, torches
ACTION_END: column halted, heads turned north
NARRATION_KO: 삼천 명이 문에서 이 킬로 떨어져 있었습니다.
DIALOGUE_KO: 
SOUND: bánh xe gỗ, vó ngựa tới gần, tiếng thét đầu tiên.
CONTINUITY: 3.000 dân cách cổng 2 km.
CHAIN_FROM: —
CUT_HALF: yes
REFS: LOC_002_wide
AI_RISK: đám đông dân → torches + bóng, không mặt

### SC_216 | 29:22–29:30 | LOC_002 (LOC_002_eastroad) | REFUGEES | VEH_206 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Wide from the roadside, static, no gore
IMAGE_PROMPT: Wide from the roadside, static, no gore. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: Xianbei horsemen burst into the tail of the cart column: curved sabers slash the yoke ropes, a cart tips over spilling grain sacks across the road, refugees scatter uphill, torches fall and gutter; no blood, no faces. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the riders hit the column's tail, ropes cut, a cart goes over, sacks tumble, people run uphill; no blood shown. Sound: sabers, an ox bellowing, sacks bursting, screams.
ACTION_START: riders hitting the column tail
ACTION_END: cart overturned, refugees scattering
NARRATION_KO: 수레가 먼저였습니다. 사람은 나중이었습니다. 그것이 명령이었습니다.
DIALOGUE_KO: 
SOUND: đao, bò rống, thóc đổ, thét.
CONTINUITY: Địch nhắm xe bò (adaptation). Không gore.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, LOC_002_wide
AI_RISK: giao chiến đám đông → wide, không máu

### SC_217 | 29:30–29:38 | LOC_002 (LOC_002_eastroad) | CHAR_106, ROK_SOLDIERS | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the last cart, static
IMAGE_PROMPT: Medium shot at the last cart, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: The old blacksmith sits on the shaft of the last ox cart, small hammer gripped in his fist, shouting the ox onward; two helmeted soldiers kneel beside the cart and fire short bursts toward rider shadows in the dark, rifles at the shoulder, faces turned away from camera. Light: Night, warm orange torchlight against deep blue-black darkness. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the old man shouts and beats the shaft with the hammer, the ox strains on; the two soldiers fire short bursts into the dark. Sound: short rifle bursts, the ox, hammer on wood.
ACTION_START: old man on the shaft, soldiers kneeling
ACTION_END: ox moving, soldiers firing
NARRATION_KO: 을보의 수레는 맨 뒤였습니다. 맨 뒤가 가장 먼저 닿는 자리였습니다.
DIALOGUE_KO: 
SOUND: K2C1 loạt ngắn, bò, búa gõ càng.
CONTINUITY: Xe cuối = 을보 + 2 lính. Súng ở vai, mặt lính quay đi.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_106_refugee_ep1, WPN_001_ref, LOC_002_wide
AI_RISK: tay cầm súng bắn → lính nghiêng/sau, chớp lửa

### SC_218 | 29:38–29:46 | LOC_003 (LOC_003_hill_ford) | CHAR_006 | EQP_002, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up in the grass, static
IMAGE_PROMPT: Close-up in the grass, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: The staff sergeant, prone, swings his night-vision monocular toward the east road where torches tumble in confusion at the tail of the cart column; he presses the shoulder handset, voice still flat. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the head turns toward the distant torch confusion, the handset is pressed, one flat line. Sound: push-to-talk, wind, one line of Korean dialogue.
ACTION_START: head turning east
ACTION_END: handset pressed, line delivered
NARRATION_KO: 미끼. 백성민이 그 말을 쓴 것은 처음이었습니다.
DIALOGUE_KO: 백성민: 수레 후미 피격. 기병 이백 이상. 여울은 미끼입니다.
SOUND: PTT, gió.
CONTINUITY: '…여울은 미끼입니다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, EQP_002_ref, EQP_001_ref, LOC_003_ford_night

### SC_219 | 29:46–29:54 | LOC_003 (LOC_003_mouth) | CHAR_001 | VEH_004, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The captain listens to the handset, looks down at the dirt map at his feet — pegs and pebbles under his boots, the plan gone wrong — then looks toward the east road and presses the handset. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he listens, his eyes drop to the dirt map, lift toward the east, the handset is pressed and one order given. Sound: push-to-talk, distant detonations, one line of Korean dialogue.
ACTION_START: listening, eyes on the dirt map
ACTION_END: looking east, order given
NARRATION_KO: 계획은 여울에 있었습니다. 적은 수레에 있었습니다. 한승우는 계획을 버리지 않았습니다.
DIALOGUE_KO: 한승우: 천둥 2, 3 위치 고수. 백 중사, 후미 계속 보고.
SOUND: PTT, nổ xa.
CONTINUITY: '천둥 2, 3 위치 고수. 백 중사, 후미 계속 보고.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, LOC_003_wide

### SC_220 | 29:54–30:02 | LOC_003 (LOC_003_hill_ford) | CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: Close on the Goguryeo officer mounted among his cavalry in the shadow of the hill: the black horn trumpet gripped in his fist, eyes bright, clean-shaven face turned toward the distant tumbling torches at the tail of the cart column; he waits, not yet blowing. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the horn stays at his fist, eyes on the distant torches; his horse shifts under him; he waits. Sound: a horse stamping, armor, distant screams.
ACTION_START: horn at his fist, watching
ACTION_END: same, still waiting
NARRATION_KO: 해모루는 기다렸습니다. 삼백 기는 한 번만 쓸 수 있었습니다.
DIALOGUE_KO: 
SOUND: ngựa dậm, giáp, thét xa.
CONTINUITY: Chờ thổi (SC_234).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_ref, VEH_101_ref, LOC_003_ford_night

### SC_221 | 30:02–30:10 | LOC_003 (LOC_003_mouth) | CHAR_002 | VEH_002, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up at the hatch, static
IMAGE_PROMPT: Close-up at the hatch, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The tall lieutenant in the open hatch of a K21 IFV (white numeral 3) stares through the night-vision monocular toward the east road; his jaw locks; his fist slams down on the hatch rim. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: he stares through the monocular, jaw locking, then his fist hammers the steel hatch rim. Sound: fist on steel, distant screams through the night.
ACTION_START: staring through the monocular
ACTION_END: fist on the hatch rim
NARRATION_KO: 오태민이 보는 것은 수레가 아니었습니다. 죽어 가는 사람이었습니다.
DIALOGUE_KO: 
SOUND: tay đập thép, thét xa qua kính.
CONTINUITY: 오태민 thấy dân chết.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, EQP_001_ref, LOC_003_wide

### SC_222 | 30:10–30:18 | LOC_003 (LOC_003_mouth) | CHAR_002, ROK_DRIVER | VEH_002, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Interior medium shot inside the IFV, static
IMAGE_PROMPT: Interior medium shot inside the IFV, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. ROK Army vehicle driver in granite-pattern digital camo uniform and crew helmet with boom microphone, seen from behind in a cramped driver's seat. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: Inside the red-lit K21 IFV the tall lieutenant drops down through the hatch, slaps the driver's shoulder from behind, and gives the intercom order against the captain's command; the driver's crew helmet from behind, red light on both. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static interior: he drops in, hits the driver's shoulder, and barks one intercom order; the engine note rises. Sound: intercom click, engine revving, one line of Korean dialogue.
ACTION_START: dropping through the hatch
ACTION_END: hand on the driver's shoulder, order given
NARRATION_KO: 안 쫓는다는 약속은 세 시간을 갔습니다.
DIALOGUE_KO: 오태민: 조종수, 전진. 여울 건너 측면 친다.
SOUND: intercom, động cơ nổ.
CONTINUITY: '조종수, 전진. 여울 건너 측면 친다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, EQP_002_ref, LOC_003_wide

### SC_223 | 30:18–30:26 | LOC_003 (LOC_003_mouth) | CHAR_001 | VEH_004, EQP_002, VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot beside the command vehicle, static
IMAGE_PROMPT: Medium shot beside the command vehicle, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The captain sees the K21 IFV (white numeral 3) lurch away from the valley mouth with its dim driving lights on; he shouts into the handset — the first time his voice has risen — helmet, compass, thin moonlight. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the IFV pulls away behind him with its lights on; he shouts one line into the handset, then again. Sound: push-to-talk, tracks grinding, one shouted line of Korean dialogue.
ACTION_START: IFV starting to move behind him
ACTION_END: shouting into the handset
NARRATION_KO: 무전은 닿았습니다. 명령은 닿지 않았습니다.
DIALOGUE_KO: 한승우: 천둥 3, 정지! 오 중위, 정지!
SOUND: PTT, xích nghiến.
CONTINUITY: '천둥 3, 정지! 오 중위, 정지!' — lần đầu cao giọng.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, VEH_002_ref, LOC_003_wide

### SC_224 | 30:26–30:34 | LOC_003 (LOC_003_ford) | — | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Low wide at the ford, static
IMAGE_PROMPT: Low wide at the ford, static. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_ford_night: A shallow stream ford north of the valley mouth at night: a bed of pale grey cobbles under a hand's depth of black water, wide banks of dark grey mud on both sides, dry yellow reeds and grass, a low grassy ridge rising to the north, thin moonlight. Action: The K21 IFV (white numeral 3) plunges into the ford at night, black water sheeting up either side, tracks grinding cobbles, driving lights snapping off; it crosses and its nose rears up onto the far bank. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low wide: the vehicle hits the water, spray sheets out, lights go dark, tracks churn cobbles, the nose climbs the far bank. Sound: engine roaring, water, stone under tracks.
ACTION_START: IFV entering the water
ACTION_END: nose rearing up the far bank
NARRATION_KO: 천둥 3호가 골짜기 입구를 떠났습니다. 명령은 그 반대였습니다.
DIALOGUE_KO: 
SOUND: động cơ gầm, nước, đá.
CONTINUITY: Xe + nước → 1 hành động vật lý.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, LOC_003_ford_night
AI_RISK: xe qua nước → tĩnh, 1 chuyển động xe, bụi nước

### SC_225 | 30:34–30:42 | LOC_003 (LOC_003_ford_northbank) | ROK_DRIVER | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the tracks in mud, static
IMAGE_PROMPT: Close-up on the tracks in mud, static. ROK Army vehicle driver in granite-pattern digital camo uniform and crew helmet with boom microphone, seen from behind in a cramped driver's seat. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: The far bank is all deep grey mud: the IFV's tracks spin without biting, mud spraying in a fan, the vehicle sinking and tilting, nose buried, rear rising; close on the churning track and flying mud. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the track spins, mud sprays, the hull settles deeper and tilts; the driver's voice on the intercom. Sound: tracks spinning, mud, engine howling, one line of Korean dialogue.
ACTION_START: track biting then slipping
ACTION_END: track spinning free, hull tilted
NARRATION_KO: 돌바닥은 여울까지였습니다. 그 너머는 해모루가 말한 진창이었습니다.
DIALOGUE_KO: 조종수: 빠졌습니다! 궤도가 헛돕니다!
SOUND: xích quay tít, bùn, động cơ rú.
CONTINUITY: '빠졌습니다! 궤도가 헛돕니다!' (조종수 off).
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, LOC_003_ford_night

### SC_226 | 30:42–30:50 | LOC_003 (LOC_003_ford_northbank) | — | VEH_206, VEH_002 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium-wide from the bank, static
IMAGE_PROMPT: Medium-wide from the bank, static. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: Out of the dark a Xianbei horseman gallops past the stuck IFV and hurls a burning torch onto its roof; the torch rolls across the camouflage netting still lashed on the hull and the net catches, flames spreading along the mesh. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the rider sweeps past, the torch arcs onto the roof, rolls, the netting flares and the fire runs along it. Sound: hooves, a torch clattering on steel, fire catching.
ACTION_START: rider approaching with torch
ACTION_END: netting burning on the roof
NARRATION_KO: 그들은 쇠를 뚫을 수 없었습니다. 그래서 불을 던졌습니다.
DIALOGUE_KO: 
SOUND: vó ngựa, đuốc rơi thép, lửa bắt.
CONTINUITY: Lửa bám lưới (탁발흠 học — 2화 hỏa công).
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, VEH_002_ref, LOC_003_ford_night

### SC_227 | 30:50–30:58 | LOC_003 (LOC_003_ford_northbank) | CHAR_205 | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static, firelight
IMAGE_PROMPT: Close-up, static, firelight. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: The bareheaded Xianbei commander reins in a hundred meters from the stuck vehicle and watches the fire crawl over the netting on its roof, firelight reflected in his steady eyes, the scar and dried blood on his neck; he lowers his bow without shooting. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: firelight flickers on his face; his eyes track the flames; the bow lowers slowly; he says nothing. Sound: distant fire, his horse breathing.
ACTION_START: watching, bow half raised
ACTION_END: bow lowered, eyes on the fire
NARRATION_KO: 탁발흠은 배웠습니다. 불은 쇠에 붙지 않았지만, 그물에는 붙었습니다.
DIALOGUE_KO: 
SOUND: lửa xa, ngựa thở.
CONTINUITY: Không thoại. Ghi nhớ.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, VEH_206_ref, LOC_003_ford_night

### SC_228 | 30:58–31:06 | LOC_003 (LOC_003_ford_northbank) | CHAR_002, ROK_SOLDIERS | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Interior medium shot in the troop compartment, static
IMAGE_PROMPT: Interior medium shot in the troop compartment, static. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: Inside the red-lit troop compartment of the tilted IFV: smoke seeps in, helmeted soldiers cough with faces down; the tall lieutenant hauls the ramp lever — the rear ramp drops halfway and jams in mud; arrows rap on the hull outside. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static interior: smoke drifts in, coughing; the lever is hauled, the ramp drops and stops dead in the mud; arrows tap on the outside; one shouted order. Sound: coughing, hydraulic whine, ramp hitting mud, arrows on steel, one line of Korean dialogue.
ACTION_START: hand on the ramp lever
ACTION_END: ramp jammed half open, order shouted
NARRATION_KO: 문이 막힌 쇠집 안에 아홉 명이 있었습니다.
DIALOGUE_KO: 오태민: 후방 램프 막혔다! 위로!
SOUND: ho, thép rít, tên gõ.
CONTINUITY: '후방 램프 막혔다! 위로!' 9 lính = extras không mặt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, LOC_003_ford_night
AI_RISK: đám đông trong xe → mặt cúi, đèn đỏ, khói

### SC_229 | 31:06–31:14 | LOC_003 (LOC_003_ford_northbank) | ROK_SOLDIERS | VEH_002, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-wide from the bank, static
IMAGE_PROMPT: Medium-wide from the bank, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: The stuck IFV's small turret traverses and its 40mm autocannon fires short bursts into the dark around it — Xianbei riders scatter wider but do not leave; the roof hatch is open and two helmeted soldiers rise out firing rifles at the shoulder, smoke from the burning netting pouring over them. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: turret swings and fires, riders scatter outward in the dark, two soldiers rise from the hatch firing, smoke rolling over the roof. Sound: 40mm bursts, rifle fire, fire roaring.
ACTION_START: turret traversing
ACTION_END: soldiers up in the hatch firing, riders scattered
NARRATION_KO: 기관포는 적을 쫓았습니다. 진창은 쫓지 못했습니다.
DIALOGUE_KO: 
SOUND: 40mm, K2C1, lửa.
CONTINUITY: Kỵ Tiên Ti giữ khoảng cách.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, VEH_206_ref, LOC_003_ford_night
AI_RISK: bắn súng cận → lính từ ngực lên, khói che

### SC_230 | 31:14–31:22 | LOC_003 (LOC_003_hill_ford) | CHAR_006 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: The staff sergeant's night-vision monocular flickers, its green glow dimming — then dead black; he does not curse; his fingertips find the battery pack in the dark and unclip it; his naked eye looks out at the ford where only firelight shows. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the green glow flickers and dies; his fingers unclip the battery by feel; his bare eye looks out at the distant fire. Sound: the device clicking off, batteries, breathing.
ACTION_START: green glow on the eye
ACTION_END: device dark, eye bare, looking out
NARRATION_KO: 야시경 하나가 꺼졌습니다. 건전지였습니다.
DIALOGUE_KO: 
SOUND: pin lách cách, thở.
CONTINUITY: Kính đêm tắt (pin). Narrator im từ SC_232.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, EQP_001_ref, LOC_003_ford_night

### SC_231 | 31:22–31:30 | LOC_003 (LOC_003_mouth) | CHAR_001 | VEH_004, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The captain stands straight beside the 4x4 command vehicle, handset in hand, watching the fire burning on the stuck vehicle across the ford; he gives the remaining vehicle its order; thin moon, distant firelight on his face. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: distant firelight on his face; the handset comes up, one order. Sound: push-to-talk, distant fire and gunfire, one line of Korean dialogue.
ACTION_START: watching the distant fire
ACTION_END: order given
NARRATION_KO: 천둥 2호는 남았습니다. 명령은 이번엔 지켜졌습니다.
DIALOGUE_KO: 한승우: 천둥 2, 여울 앞 사격 지원. 건너지 마라.
SOUND: PTT, lửa xa.
CONTINUITY: '천둥 2, 여울 앞 사격 지원. 건너지 마라.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, LOC_003_wide

### SC_232 | 31:30–31:38 | LOC_003 (LOC_003_hill_ford) | CHAR_006 | EQP_001, VEH_002, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up then night-vision POV, static
IMAGE_PROMPT: Close-up then night-vision POV, static. @CHAR_006_facepaint_ep1: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: The staff sergeant clicks a fresh battery pack into the night-vision monocular by feel; the eyepiece glows green again — and in the green view below, the stuck IFV burns on its roof while a ring of Xianbei horsemen circles it just out of range; no dialogue. Light: Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the battery clicks in, the green glow returns, cut to the green POV: the burning vehicle and the circling riders. Sound: a click, night-vision whine, distant fire.
ACTION_START: battery going in
ACTION_END: green POV of the burning vehicle
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: "딸깍", rít kính đêm, lửa xa.
CONTINUITY: Không thoại, không narration.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_facepaint_ep1, EQP_001_ref, VEH_002_ref, VEH_206_ref, LOC_003_ford_night

### SC_233 | 31:38–31:46 | LOC_003 (LOC_003_mouth) | ROK_GUNNER_TURRET | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Interior close-up in the turret, static
IMAGE_PROMPT: Interior close-up in the turret, static. ROK Army vehicle gunner in granite-pattern digital camo uniform and crew helmet with boom microphone, seen inside a cramped red-lit turret, face half in shadow. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: Inside the cramped red-lit turret of a K21 IFV the gunner in a crew helmet hauls the last belt of 40mm rounds into the feed tray and looks down at the empty steel ammunition can at his feet; face half in shadow. Light: Night, dim red tactical lamplight on faces and hands, deep black shadows beyond. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the belt is dragged into the feed, his eyes drop to the empty can, one line shouted. Sound: ammunition belt clattering, engine, one line of Korean dialogue.
ACTION_START: belt being fed
ACTION_END: looking at the empty can, line shouted
NARRATION_KO: 
DIALOGUE_KO: 사수: 40밀리, 즉응탄 마지막입니다!
SOUND: băng đạn lách cách, động cơ.
CONTINUITY: '40밀리, 즉응탄 마지막입니다!' 사수 = extra.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, LOC_003_wide

### SC_234 | 31:46–31:54 | LOC_003 (LOC_003_hill_ford) | CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Low aerial following the head of the charge, single move  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Low aerial following the head of the charge, single move. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_003_ford_night: A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight. Action: The Goguryeo officer raises the black horn trumpet and blows one long note; three hundred cataphracts pour down the hill toward the ford — horses in iron lamellar barding gleaming in the firelight, long lances leveling, red plumes; low aerial tracking the head of the charge. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Low aerial tracks the charge from the hilltop down to the ford: the horn note, then the wave of armored horses breaking downhill, lances dropping level. Sound: one long deep horn note, hooves like thunder, armor.
ACTION_START: horn raised on the hill
ACTION_END: charge reaching the ford, lances level
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: tù và trầm dài, vó ngựa như sấm, giáp.
CONTINUITY: Tù và 1 hồi. 300 kỵ = aerial thấp.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_ref, VEH_101_ref, LOC_003_ford_night
AI_RISK: 300 kỵ → aerial thấp, đầu đoàn rõ, sau bụi/tối

### SC_235 | 31:54–32:02 | LOC_003 (LOC_003_ford_northbank) | GOG_CAVALRYMEN | VEH_101, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-wide, static
IMAGE_PROMPT: Medium-wide, static. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: Goguryeo cataphracts crash into the ring of Xianbei horsemen around the stuck vehicle; the Xianbei do not meet them — they fan out to both sides and shoot arrows back over their shoulders as they run; firelight from the burning netting; no wounded close. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium-wide: the armored wave hits, the light horsemen split and fan away shooting backward. Sound: lances on armor, horses screaming, arrows hissing.
ACTION_START: cataphracts hitting the ring
ACTION_END: Xianbei fanning out, arrows flying back
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: giáo chạm giáp, ngựa hí, tên rít.
CONTINUITY: Tiên Ti không đón đòn.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_101_ref, VEH_206_ref, LOC_003_ford_night
AI_RISK: giao chiến kỵ → medium-wide, tối + lửa

### SC_236 | 32:02–32:10 | LOC_003 (LOC_003_ford_northbank) | CHAR_105, GOG_CAVALRYMEN | VEH_101, VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the vehicle's nose, static
IMAGE_PROMPT: Medium shot at the vehicle's nose, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: The Goguryeo officer leaps from his armored horse beside the stuck IFV's mud-buried nose and hurls a coil of hemp rope up over the tow hook; two cavalrymen hitch the rope's end to their saddles and the armored horses lean into it. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he jumps down, the rope coil flies over the tow hook, two riders hitch it and their horses strain forward. Sound: rope on steel, horses grunting, fire.
ACTION_START: officer jumping down with rope
ACTION_END: rope on hook, horses straining
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: dây thừng, thép, ngựa thở.
CONTINUITY: Dây thừng — hành động cứu 1.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_ref, VEH_101_ref, VEH_002_ref, LOC_003_ford_night
AI_RISK: dây + móc → 1 dây rõ, không nhiều dây

### SC_237 | 32:10–32:18 | LOC_003 (LOC_003_ford_northbank) | OX_DRIVER | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. Goguryeo ox-cart driver in a coarse undyed hemp jacket and trousers, cloth headband, straw sandals, cracking a leather whip. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: Four oxen under wooden yokes are led back from the cart column to the stuck vehicle and hitched to the rope; a Goguryeo ox-driver in a coarse hemp jacket bellows at them and lays a whip across the rump of the lead ox; firelight from the vehicle's roof. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the oxen are hitched, the driver shouts and cracks the whip, the yokes creak as they lean. Sound: oxen bellowing, wooden yokes, a shout, the whip.
ACTION_START: oxen being hitched
ACTION_END: oxen leaning into the yokes
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: bò rống, ách gỗ, quát, roi.
CONTINUITY: Bò dân kéo xe sắt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, LOC_003_ford_night

### SC_238 | 32:18–32:26 | LOC_003 (LOC_003_ford_northbank) | GOG_CAVALRYMEN | VEH_002, VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on rope and track, static
IMAGE_PROMPT: Close-up on rope and track, static. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: Close: the hemp rope stretched taut as a bowstring, oxen straining, armored horses digging in, cavalrymen hauling on the rope with their hands; the IFV's track turns slowly — bites — and a long crack opens in the grey mud. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up on the taut rope and the track: the rope quivers, the track creeps, bites, the mud splits along a long crack. Sound: rope creaking, mud tearing, men and animals grunting.
ACTION_START: rope taut, track still
ACTION_END: track biting, mud cracking
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: dây rít, bùn nứt, thở của người và thú.
CONTINUITY: 1 hành động vật lý.
CHAIN_FROM: SC_237
CUT_HALF: yes
REFS: VEH_002_ref, VEH_101_ref, LOC_003_ford_night
AI_RISK: dây căng + xích → tĩnh, cận 2 vật

### SC_239 | 32:26–32:34 | LOC_002 (LOC_002_eastgate) | GOG_ARCHERS | WPN_101 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Low angle from the road up at the bastions, static
IMAGE_PROMPT: Low angle from the road up at the bastions, static. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: East gate of the Goguryeo fortress at night: two-leaf wooden gate doors sheathed with iron plates and studded with large iron nails, a heavy wooden crossbar, a stone gate passage in dry-stacked grey granite walls flanked by two rectangular protruding bastions, burning torches in iron brackets, black three-legged crow banners. Action: From the road below the east gate at night: on the two protruding stone bastions flanking the gate, ranks of Goguryeo archers draw and loose together — a rain of arrows arcs down and plants a bristling fence between the Xianbei riders and the cart column on the slope; torches on the wall. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: bows draw and release together on both bastions, the volley arcs down and stitches a line of shafts into the slope. Sound: hundreds of bowstrings, arrows falling like hail.
ACTION_START: archers drawing on the bastions
ACTION_END: arrow fence planted in the slope
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: dây cung hàng trăm, tên rơi như mưa đá.
CONTINUITY: 치 cổng đông — cung thủ.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, WPN_101_ref, LOC_002_detail
AI_RISK: cung thủ số đông → low angle ngược sáng đuốc

### SC_240 | 32:34–32:42 | LOC_003 (LOC_003_ford_northbank) | CHAR_002, CHAR_105, ROK_SOLDIERS | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static, both faces
IMAGE_PROMPT: Medium two-shot, static, both faces. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Face smudged black with net smoke, one lens of the goggles cracked, wet mud on sleeves and forearms, sweat cutting lines through the grime. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: The IFV heaves up out of the mud; soldiers on the roof tear the burning netting off and fling it into the water; the tall lieutenant rises in the hatch, face black with smoke, one goggle lens cracked, and looks down at the Goguryeo officer standing by the hull holding the rope; the officer looks up at him and says nothing. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the hull lurches up, netting goes over the side hissing into the water, the lieutenant rises in the hatch and looks down; the officer looks up; both hold the look; no words. Sound: track biting stone, burning net hissing in water.
ACTION_START: hull heaving up, netting being torn off
ACTION_END: lieutenant and officer looking at each other
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: xích bám đá, lưới cháy xèo trong nước.
CONTINUITY: 오태민 = smoke_ep1 từ đây (mặt đen, kính vỡ 1 mắt).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, CHAR_105_ref, VEH_002_ref, LOC_003_ford_night

### SC_241 | 32:42–32:52 | LOC_003 (LOC_003_ford_northbank) | GOG_CAVALRYMEN, OX_DRIVER | VEH_002, VEH_101 | PROPS: PROP_016 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide, slow push along the tow rope
IMAGE_PROMPT: Still for ken-burns: medium-wide, slow push along the tow rope. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. Goguryeo ox-cart driver in a coarse undyed hemp jacket and trousers, cloth headband, straw sandals, cracking a leather whip. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_003_ford_night: The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight. Action: A mud-plastered K21 IFV is hauled up the slope by four oxen on a hemp rope, Goguryeo cavalrymen in iron lamellar walking either side of the rope, a torch or two, the burnt netting still smoking in the water behind; night. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push along the rope from the oxen to the vehicle. Sound: rope, oxen, tracks, fire dying.
ACTION_START: oxen and rope
ACTION_END: mud-covered vehicle
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: dây, bò, xích, lửa.
CONTINUITY: Không narration.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_002_ref, VEH_101_ref, LOC_003_ford_night

### SC_242 | 32:52–33:00 | LOC_003 (LOC_003_northridge) | CHAR_205 | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_003_ford_night: A low grassy ridge north of the valley at night: dry knee-high yellow grass under thin moonlight, bare oak scrub, the dark hollow of a valley below with a faint red glow leaking through camouflage netting. Action: On the north ridge the bareheaded Xianbei commander sees the iron vehicle being dragged clear — no regret, no long look; he lifts his bow and points it at the tail of the cart column on the distant slope; the riders around him wheel to follow the bow. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: a glance at the distant vehicle, then the bow points at the cart column and the riders around him turn that way; no dialogue. Sound: hooves gathering toward one direction.
ACTION_START: glancing at the vehicle
ACTION_END: bow pointing at the carts, riders turning
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: vó ngựa dồn về một hướng.
CONTINUITY: Kết Phase 4 (narrator im).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, VEH_206_ref, LOC_003_ford_night

### SC_243 | 33:00–33:08 | LOC_002 (LOC_002_gateyard) | CHAR_104, GOG_INFANTRY | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium shot on the wall above the gate, static
IMAGE_PROMPT: Medium shot on the wall above the gate, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: Inside the east gate of the Goguryeo fortress at night: a packed-earth yard behind two-leaf iron-sheathed wooden gate doors, a stone stair climbing the dry-stacked grey granite wall, torches in iron brackets, black three-legged crow banners, timber halls with dark tiled roofs behind. Action: On the wall above the east gate the fortress commander in his grey cloak looks down: the cart column is two hundred meters from the gate, its tail pressed by Xianbei riders, torches falling; behind him in the torchlit gate yard five hundred Goguryeo spearmen stand silent in ranks, spears upright. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he looks down the slope at the harried column, then back at the silent ranks behind him. Sound: screams from the slope, armor shifting in the yard.
ACTION_START: looking down the slope
ACTION_END: looking back at the spearmen
NARRATION_KO: 수레는 문에서 이백 미터였습니다. 이백 미터를 지켜 줄 것은 성 안에만 있었습니다.
DIALOGUE_KO: 
SOUND: thét dưới dốc, giáp bộ binh.
CONTINUITY: 500 창병 = khối sau lưng, không mặt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_104_ref, WPN_102_ref, LOC_002_detail
AI_RISK: 500 lính → khối hàng ngũ, đuốc, không mặt

### SC_244 | 33:08–33:16 | LOC_002 (LOC_002_gateyard) | CHAR_104, GOG_INFANTRY | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Tracking shot down the stone stair, single move
IMAGE_PROMPT: Tracking shot down the stone stair, single move. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: Inside the east gate of the Goguryeo fortress at night: a packed-earth yard behind two-leaf iron-sheathed wooden gate doors, a stone stair climbing the dry-stacked grey granite wall, torches in iron brackets, black three-legged crow banners, timber halls with dark tiled roofs behind. Action: The fortress commander runs down the stone stair from the wall, tears the iron ring of keys from his belt and throws it to a gate guard, draws a short sword for the first time, and roars at the ranks; torches, grey cloak flying. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera follows him down the stair; the keys fly to the guard; the sword comes out; he shouts one order. Sound: keys jingling through the air, a sword drawn, boots on stone, one shouted line of Korean dialogue.
ACTION_START: running down the stair
ACTION_END: sword drawn, order roared
NARRATION_KO: 성문을 닫는 것이 성주의 첫째 임무였습니다. 그는 그 임무를 알았습니다.
DIALOGUE_KO: 고정수: 문을 열어라! 창병 오백, 나를 따르라!
SOUND: chìa khóa, kiếm rút, giày trên đá.
CONTINUITY: '문을 열어라! 창병 오백, 나를 따르라!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_104_ref, WPN_102_ref, LOC_002_detail

### SC_245 | 33:16–33:24 | LOC_002 (LOC_002_eastgate) | CHAR_104, GOG_INFANTRY | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Wide from on the wall looking down, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide from on the wall looking down, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: East gate of the Goguryeo fortress at night: two-leaf wooden gate doors sheathed with iron plates and studded with large iron nails, a heavy wooden crossbar, a stone gate passage in dry-stacked grey granite walls flanked by two rectangular protruding bastions, burning torches in iron brackets, black three-legged crow banners. Action: From the wall: the two iron-sheathed gate doors swing open and the fortress commander in his grey cloak leads five hundred Goguryeo spearmen out in ranks down the slope, torches on either flank, spears leveling as they go to meet the cart column. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide from above: the doors open, the ranks stream out and down the slope behind the commander, torches bobbing. Sound: the crossbar lifting, spear shafts, a massed shout.
ACTION_START: gate doors opening
ACTION_END: ranks out on the slope, spears level
NARRATION_KO: 성주는 문을 열었습니다. 그의 백성이 문 밖에 있었기 때문입니다. 왕의 글은 아직 오지 않았습니다.
DIALOGUE_KO: 
SOUND: then cổng, giáo, tiếng hô "가자!".
CONTINUITY: 고정수 mở cổng (trái lệnh vua chưa tới).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_104_ref, WPN_102_ref, LOC_002_detail
AI_RISK: 500 lính → wide từ trên tường

### SC_246 | 33:24–33:32 | LOC_003 (LOC_003_mouth) | CHAR_001 | VEH_004, EQP_002 | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: The captain lowers his binoculars — he has seen the gate open — and presses the handset with a single sentence that redirects every gun; thin moonlight, compass at his throat. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: binoculars down, handset pressed, one order. Sound: push-to-talk, one line of Korean dialogue.
ACTION_START: binoculars up
ACTION_END: binoculars down, order given
NARRATION_KO: 한승우는 계획을 바꿨습니다. 이제 중심은 창이었습니다.
DIALOGUE_KO: 한승우: K3, K6 전부 동문 양옆. 창병 측면 엄호.
SOUND: PTT.
CONTINUITY: 'K3, K6 전부 동문 양옆. 창병 측면 엄호.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_ref, VEH_004_ref, EQP_002_ref, PROP_006_ref, LOC_003_wide

### SC_247 | 33:32–33:40 | LOC_002 (LOC_002_eastroad) | ROK_SOLDIERS, GOG_INFANTRY | VEH_003, VEH_004, WPN_004 | PROPS: PROP_007 | TYPE: video8s | 8s
SHOT: Medium-wide at the foot of the slope, static
IMAGE_PROMPT: Medium-wide at the foot of the slope, static. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. @PROP_007_ref: dark olive 200-liter steel fuel drum with two raised ribs, twin screw caps, a small red triangle painted on the side, dents, strapped with rope, a hand pump and a green 20-liter jerrycan beside it. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: At night a cargo truck (two fuel drums with a red triangle visible under its rolled-back canvas) and the 4x4 command vehicle roll up to the foot of the slope below the east gate; from their roofs two heavy machine guns hammer long streams of tracer past both flanks of the Goguryeo spear ranks; Xianbei riders on the flanks peel away into the dark. Light: Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the two vehicles halt, the heavy guns open up, tracer streams pass either side of the spearmen, the riders on the flanks scatter. Sound: heavy machine guns thudding, tracers.
ACTION_START: vehicles arriving
ACTION_END: tracer streams past the spear ranks
NARRATION_KO: 창과 총이 같은 문 앞에 섰습니다.
DIALOGUE_KO: 
SOUND: K6 nặng "둥둥둥", tracer.
CONTINUITY: K511 #2 + 2 phuy (foreshadow 2화). K6 trên nóc.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, VEH_003_ref, VEH_004_ref, WPN_004_ref, PROP_007_ref, LOC_002_wide
AI_RISK: nhiều yếu tố → medium-wide, tracer làm đường dẫn

### SC_248 | 33:40–33:48 | LOC_002 (LOC_002_eastroad) | GOG_INFANTRY | VEH_206 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Low aerial along the slope, single slow drift  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Low aerial along the slope, single slow drift. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: Low aerial at night: the Goguryeo spear block advances down the slope in tight ranks with spears leveled, opening to take the cart column into its middle; the Xianbei horsemen do not charge — they circle outside spear reach loosing single arrows; torches, thin moon. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: One slow low aerial drift along the advancing spear block; riders circle wide, single arrows flying. Sound: spear shafts, marching feet in step, lone arrows.
ACTION_START: spear block advancing
ACTION_END: carts inside the block, riders circling
NARRATION_KO: 선비 기병은 창을 정면으로 받지 않았습니다. 그것이 그들의 방식이었습니다.
DIALOGUE_KO: 
SOUND: giáo, bước chân đều, tên lẻ.
CONTINUITY: Tiên Ti không đón giáo.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, VEH_206_ref, LOC_002_wide

### SC_249 | 33:48–33:56 | LOC_002 (LOC_002_eastroad) | CHAR_106, GOG_INFANTRY | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot on the last cart, static
IMAGE_PROMPT: Medium shot on the last cart, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: The old blacksmith on the shaft of the last ox cart drives it through the gap between two lines of Goguryeo spearmen; an arrow thuds into the cart's side a hand's width from him — he does not duck, only whips the ox on; bandaged leg, hammer in his fist. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the cart rolls through the gap, the arrow strikes the side beside him, he does not flinch and whips the ox. Sound: arrow into wood, cart wheels, the ox.
ACTION_START: cart entering the gap
ACTION_END: arrow in the cart side, ox whipped on
NARRATION_KO: 을보는 몸을 낮추지 않았습니다. 예순여섯 해를 산 사람의 고집이었습니다.
DIALOGUE_KO: 
SOUND: tên cắm gỗ, bánh xe, bò.
CONTINUITY: 을보 không cúi.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_106_refugee_ep1, WPN_102_ref, LOC_002_wide

### SC_250 | 33:56–34:04 | LOC_002 (LOC_002_eastgate) | CHAR_104, CHAR_106 | — | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: From inside the gate looking out through the closing doors, static
IMAGE_PROMPT: From inside the gate looking out through the closing doors, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_detail: East gate of the Goguryeo fortress at night: two-leaf wooden gate doors sheathed with iron plates and studded with large iron nails, a heavy wooden crossbar, a stone gate passage in dry-stacked grey granite walls flanked by two rectangular protruding bastions, burning torches in iron brackets, black three-legged crow banners. Action: From inside the gate passage: the last ox cart with the old blacksmith on its shaft rolls in through the doors; the fortress commander walks in last behind it, short sword in hand; the two iron-sheathed doors swing shut behind him and three arrows thud into the outside of the wood through the narrowing gap. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static from inside: the cart rolls in, the commander steps in last, the doors swing closed and three arrows strike the outer face as the gap narrows to black. Sound: the crossbar dropping, arrows into wood.
ACTION_START: cart entering, doors open
ACTION_END: doors shut, arrows in the wood
NARRATION_KO: 곡식 백 수레. 요동성이 여름을 버틸 양이었습니다.
DIALOGUE_KO: 
SOUND: then cổng hạ, tên cắm gỗ.
CONTINUITY: Cổng đóng. 2 CHAR trong khung (không ai nói).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_104_ref, CHAR_106_refugee_ep1, LOC_002_detail

### SC_251 | 34:04–34:12 | LOC_002 (LOC_002_eastroad) | CHAR_205 | VEH_206, VEH_002, VEH_003 | PROPS: PROP_007, PROP_016 | TYPE: video8s | 8s
SHOT: Close-up on the commander, then a slow pan following his gaze, single move
IMAGE_PROMPT: Close-up on the commander, then a slow pan following his gaze, single move. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @VEH_003_ref: South Korean K511A1 six-wheeled military cargo truck, boxy hard cab with long hood and vertical grille, canvas-covered cargo bed on arched bows, big lugged tires, three-tone green-brown-black camouflage cab, faded olive canvas, small Korean flag on the door. @PROP_007_ref: dark olive 200-liter steel fuel drum with two raised ribs, twin screw caps, a small red triangle painted on the side, dents, strapped with rope, a hand pump and a green 20-liter jerrycan beside it. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_002_wide: The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall. Action: Beyond arrow range in the dark the bareheaded Xianbei commander halts his horse and raises his hand: withdraw; riders melt into the night behind him; he turns for a last look — by the ford the mud-covered IFV being hauled up the slope by oxen, and near the foot of the gate slope a cargo truck with its canvas rolled back, two round black steel drums showing under torchlight. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Close on the commander as his hand rises and the riders fade; then a slow pan following his gaze across to the hauled vehicle and coming to rest on the two black drums in the truck bed. Sound: hooves withdrawing, distant rope and oxen.
ACTION_START: hand raised, riders behind
ACTION_END: pan resting on the two fuel drums
NARRATION_KO: 탁발흠은 다시 물러났습니다. 두 번째였습니다. 그는 두 번 다 보고 있었습니다. 마지막으로 본 것은 수레 위의 검은 통이었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa rút xa, dây bò xa.
CONTINUITY: 탁발흠 nhìn thấy 2 phuy → hỏa công 2화.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_survivor_ep1, VEH_206_ref, VEH_002_ref, VEH_003_ref, PROP_007_ref, LOC_002_wide

### SC_252 | 34:12–34:20 | LOC_003 (LOC_003_mouth) | CHAR_002, ROK_SOLDIERS | VEH_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Static medium-wide at the valley mouth
IMAGE_PROMPT: Static medium-wide at the valley mouth. @CHAR_002_ref: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Face smudged black with net smoke, one lens of the goggles cracked, wet mud on sleeves and forearms, sweat cutting lines through the grime. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_wide: The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond. Action: At the valley mouth the tall lieutenant stands breathing hard beside the mud-plastered K21 IFV (white numeral 3), one goggle lens cracked, face black with smoke, one hand braced on the hull, looking toward the distant east gate; the helmeted soldiers around him do not cheer — they sit down heavily in the grass. Light: Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base. Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he leans on the hull breathing hard, looking toward the gate; the soldiers around him sink down into the grass one by one; nobody speaks. Sound: far-off cheering from the fortress wall; close by, hard breathing and hot metal ticking as it cools.
ACTION_START: lieutenant leaning on the hull, soldiers standing
ACTION_END: soldiers sitting in the grass, lieutenant still
NARRATION_KO: 고구려는 환호했습니다. 천둥 중대는 아니었습니다. 이긴 것은 그들의 총이 아니었습니다.
DIALOGUE_KO: 
SOUND: reo hò rất xa; gần: thở, kim loại nguội kêu tách.
CONTINUITY: 1 địa điểm (reo hò = âm xa).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_ref, VEH_002_ref, LOC_003_wide

### SC_253 | 34:20–34:30 | LOC_002 (LOC_002_eastgate) | — | — | PROPS: PROP_016, PROP_015 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium on the closed gate, slow push to the crossbar
IMAGE_PROMPT: Still for ken-burns: medium on the closed gate, slow push to the crossbar. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_002_detail: East gate of the Goguryeo fortress at night: two-leaf wooden gate doors sheathed with iron plates and studded with large iron nails, a heavy wooden crossbar, a stone gate passage in dry-stacked grey granite walls flanked by two rectangular protruding bastions, burning torches in iron brackets, black three-legged crow banners. Action: The east gate closed at night: the iron-sheathed wooden doors bristling with arrow shafts, torches burning either side in iron brackets, the heavy wooden crossbar in place; beyond the walls, darkness. Light: Night, warm orange torchlight against deep blue-black darkness. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in to the crossbar. Sound: wind, torches, silence.
ACTION_START: closed gate with arrows
ACTION_END: tight on the crossbar
NARRATION_KO: 삼천 명이 성으로 들어갔습니다. 문은 닫혔습니다. 이제 나갈 길도 닫힌 것입니다.
DIALOGUE_KO: 
SOUND: gió, đuốc, im.
CONTINUITY: Kết P10. Open loop.
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_015_ref, LOC_002_detail


## [Phần 11] 쇠는 쇠요 (34:30–37:30) · cái giá, kho lương, tường tây

### SC_254 | 34:30–34:40 | LOC_003 (LOC_003_dawn) | — | VEH_002 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide, slow push to a road wheel on the grass
IMAGE_PROMPT: Still for ken-burns: medium-wide, slow push to a road wheel on the grass. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: Cold grey dawn in the valley: a K21 IFV (white numeral 3) plastered with dried grey mud to its roof, the camouflage netting on it burnt black and torn; one rubber-rimmed road wheel lies removed on the yellow grass with tools scattered around it; mist. Light: Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in to the removed road wheel. Sound: dawn birds, wind, cold metal ticking.
ACTION_START: vehicle and wheel
ACTION_END: tight on the wheel
NARRATION_KO: 새벽. 천둥 3호는 바퀴 하나를 잃었습니다. 바퀴는 여섯 개 중 하나였습니다. 부품은 이 시대에 없었습니다. 있는 것은 대장간뿐이었습니다.
DIALOGUE_KO: 
SOUND: chim sớm, gió, kim loại lạnh.
CONTINUITY: 천둥 3 hỏng bánh chịu nặng (vehicle_bible). D5 bình minh.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_002_ref, LOC_003_wide

### SC_255 | 34:40–34:48 | LOC_003 (LOC_003_dawn) | CHAR_003, CHAR_005 | VEH_002, UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low medium shot at ground level, static
IMAGE_PROMPT: Low medium shot at ground level, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Wet grey mud on gloves, forearms and chest of the body armor, patrol cap pushed back, grease streak on one cheek. @CHAR_005_ref: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The stocky sergeant lies on his back half under the mud-caked K21 IFV, arms up in the running gear with a multi-tool, mud on his gloves and chest; the boyish private kneels beside him handing in a wrench, a grey quadcopter drone resting on the grass next to him; grey dawn. Light: Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low: the sergeant works under the hull, the private passes the wrench; the sergeant speaks one line from under the vehicle. Sound: tool on steel, breathing, one line of Korean dialogue.
ACTION_START: private handing in the wrench
ACTION_END: sergeant's line from under the hull
NARRATION_KO: 휜 축. 철원이라면 반나절 일이었습니다. 여기서는 불가능한 일이었습니다. 부품 없는 기계는 이 시대의 돌과 같았습니다.
DIALOGUE_KO: 박기철: 지지륜 축이 휘었습니다. 부품은 없습니다.
SOUND: kìm, thép, thở.
CONTINUITY: 박기철 = mud_ep1 (bùn ướt). Drone #2 bên cạnh.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_005_ref, VEH_002_ref, UAV_001_ref, LOC_003_wide

### SC_256 | 34:48–34:56 | LOC_003 (LOC_003_dawn) | CHAR_106, CHAR_003 | VEH_002 | PROPS: PROP_019 | TYPE: video8s | 8s
SHOT: Medium shot at the running gear, static
IMAGE_PROMPT: Medium shot at the running gear, static. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Wet grey mud on gloves, forearms and chest of the body armor, patrol cap pushed back, grease streak on one cheek. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_019_ref: hand-forged iron pry bar one point two meters long with a flattened end and a hooked end showing hammer marks, and a modern folding entrenching shovel re-handled with a new oak shaft and a hand-forged iron collar. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The old blacksmith limps up on his bandaged leg holding a small hammer and a hand-forged iron bar still dark with forge soot; he lays the bar against the bent axle of the IFV's running gear, taps it twice with the hammer, squints his left eye, and nods; the sergeant's mud-caked legs stick out from under the hull. Light: Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he limps in, fits the bar to the axle, two taps of the hammer, a squint, a nod, one line. Sound: hammer on iron ringing, one line of Korean dialogue.
ACTION_START: old man arriving with the bar
ACTION_END: bar on the axle, nod, line spoken
NARRATION_KO: 을보는 밤새 쇠를 두드렸습니다. 다친 다리로, 남의 쇠를 위해서였습니다. 대장장이는 쇠에 주인을 묻지 않았습니다.
DIALOGUE_KO: 을보: 쇠는 쇠요.
SOUND: búa gõ sắt, tiếng "쨍".
CONTINUITY: '쇠는 쇠요.' PROP_019 (thanh sắt rèn).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_refugee_ep1, CHAR_003_ref, VEH_002_ref, PROP_019_ref, LOC_003_wide

### SC_257 | 34:56–35:04 | LOC_003 (LOC_003_dawn) | CHAR_003, CHAR_106 | VEH_002 | PROPS: PROP_019 | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Wet grey mud on gloves, forearms and chest of the body armor, patrol cap pushed back, grease streak on one cheek. @CHAR_106_refugee_ep1: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_019_ref: hand-forged iron pry bar one point two meters long with a flattened end and a hooked end showing hammer marks, and a modern folding entrenching shovel re-handled with a new oak shaft and a hand-forged iron collar. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The stocky sergeant crawls out from under the IFV, takes the hand-forged iron bar, fits it to a track pin, turns it, and looks at the old blacksmith; the two craftsmen of two eras nod at each other, no more words needed; grey dawn, mud, forge-black iron. Light: Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he crawls out, fits the bar to the pin, turns it, looks up; the two men nod; one line from the sergeant. Sound: iron on iron, one line of Korean dialogue.
ACTION_START: sergeant crawling out
ACTION_END: two men nodding, bar on the pin
NARRATION_KO: 두 대장장이는 서로의 말을 몰라도 됐습니다. 쇠가 말을 대신했습니다.
DIALOGUE_KO: 박기철: 영감님, 이거… 되겠습니다.
SOUND: sắt chạm sắt.
CONTINUITY: '영감님, 이거… 되겠습니다.'
CHAIN_FROM: SC_256
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_106_refugee_ep1, VEH_002_ref, PROP_019_ref, LOC_003_wide

### SC_258 | 35:04–35:14 | LOC_003 (LOC_003_dawn) | — | VEH_002 | PROPS: PROP_019 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: macro on the repair, slow push-in
IMAGE_PROMPT: Still for ken-burns: macro on the repair, slow push-in. @VEH_002_ref: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. @PROP_019_ref: hand-forged iron pry bar one point two meters long with a flattened end and a hooked end showing hammer marks, and a modern folding entrenching shovel re-handled with a new oak shaft and a hand-forged iron collar. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: Macro: a rough hand-forged iron bar with hammer marks pinned temporarily into a machined steel track link of a modern vehicle, dried mud, a wrap of steel wire; cold dawn light. Light: Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in on the join between forged iron and machined steel. Sound: wind, then an old hoarse voice off-screen calling one word.
ACTION_START: repair wide
ACTION_END: tight on the join
NARRATION_KO: 고구려 대장간의 쇠가 쇠수레의 발을 붙들었습니다. 천사백 년 된 방식이 오늘의 기계를 고쳤습니다. 이 부대는 이제 고구려 없이는 굴러가지 못했습니다. 그리고 박기철에게는 새 이름이 생겼습니다.
DIALOGUE_KO: 을보: 쇠쟁이.
SOUND: gió, im; tiếng gọi khàn ngoài hình.
CONTINUITY: 을보 gọi '쇠쟁이' off-screen.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_002_ref, PROP_019_ref, LOC_003_wide

### SC_259 | 35:14–35:22 | LOC_003 (LOC_003_medic) | CHAR_004, ROK_SOLDIERS | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium shot along a row of wounded, static
IMAGE_PROMPT: Medium shot along a row of wounded, static. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Blue nitrile gloves stained with fresh blood, a few loose strands of hair escaping the bun, fine yellow dust on helmet. ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_003_wide: The aid station of the hidden company base at night: a canvas awning off an olive-green army tent, a folding stretcher on olive ammunition cans, a headlamp and a shaded red lamp, camouflage netting, brown hemp Goguryeo tents beside, dry yellow grass, dark oak scrub slopes. Action: Six helmeted soldiers sit in a row on olive ammunition cans at dawn, bandaged arms and legs, faces turned away or down; at the end of the row the young female medic finishes a shoulder dressing, then counts the bottles in her open medic bag with a fingertip and writes in a notebook. Light: Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the last dressing is tied, the fingertip counts bottles, she writes and says one line. Sound: bandage, bottles, one line of Korean dialogue.
ACTION_START: tying the shoulder dressing
ACTION_END: counting bottles, line spoken
NARRATION_KO: 부상 여섯. 돌아오지 않는 숫자였습니다. 화살이 스무 개면 항생제는 끝이었습니다.
DIALOGUE_KO: 윤서아: 부상 여섯. 항생제는 아직 아흔 퍼센트입니다.
SOUND: băng, lọ.
CONTINUITY: 6 thương binh (0 KIA).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_ref, PROP_009_ref, LOC_003_wide
AI_RISK: 6 thương binh → hàng ngang, mặt quay đi

### SC_260 | 35:22–35:30 | LOC_003 (LOC_003_dawn) | CHAR_003, CHAR_001 | VEH_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot beside the command vehicle, static
IMAGE_PROMPT: Medium two-shot beside the command vehicle, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Wet grey mud on gloves, forearms and chest of the body armor, patrol cap pushed back, grease streak on one cheek. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_004_ref: South Korean K151 light tactical 4x4 command vehicle, tall boxy lightly-armored body, two-piece sloped windshield, round roof hatch with a 12.7mm machine gun, three black whip antennas, roof rack, big lugged tires, caged round headlights, three-tone green-brown-black camouflage, small Korean flag on the door. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The stocky sergeant wipes his hands on the red rag, opens the green notebook and reads to the captain leaning against the 4x4 command vehicle; flat voice like reading an invoice; grey morning. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: hands wiped on the red rag, the notebook opened, one line read out. Sound: paper, wind, one line of Korean dialogue.
ACTION_START: wiping hands
ACTION_END: reading, line delivered
NARRATION_KO: 사백팔십, 백십, 사흘치. 숫자는 하룻밤에 이만큼 줄었습니다. 박기철은 줄어드는 숫자만 읽었습니다. 늘어나는 숫자는 없었습니다.
DIALOGUE_KO: 박기철: 40밀리 사백팔십. 박격포 백십. 야시경 건전지 사흘치.
SOUND: giấy, gió.
CONTINUITY: '40밀리 사백팔십. 박격포 백십. 야시경 건전지 사흘치.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_ref, CHAR_001_ref, VEH_004_ref, LOC_003_wide

### SC_261 | 35:30–35:38 | LOC_003 (LOC_003_dawn) | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, static
IMAGE_PROMPT: Medium close-up, static. @CHAR_003_ref: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Wet grey mud on gloves, forearms and chest of the body armor, patrol cap pushed back, grease streak on one cheek. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The stocky sergeant turns a page in the green notebook, stops at the last line, and looks over at the K2 tank under its netting before he speaks; grey morning light on the salt-and-pepper temple. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: a page turns, his eyes stop, lift to the tank, then one line. Sound: paper, one line of Korean dialogue.
ACTION_START: turning the page
ACTION_END: looking at the tank, line spoken
NARRATION_KO: 삼백칠십. 박기철은 남은 것부터 말하는 사람이 되어 가고 있었습니다. 싸우지 않아도 기름은 줄었습니다. 움직이는 것만으로도.
DIALOGUE_KO: 박기철: 간밤에 삼십 킬로. 남은 건 삼백칠십.
SOUND: giấy lật.
CONTINUITY: ★ '간밤에 삼십 킬로. 남은 건 삼백칠십.'
CHAIN_FROM: SC_260
CUT_HALF: no
REFS: CHAR_003_ref, VEH_001_ref, LOC_003_wide

### SC_262 | 35:38–35:46 | LOC_003 (LOC_003_dawn) | CHAR_001 | VEH_001 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium shot, static, tank behind
IMAGE_PROMPT: Medium shot, static, tank behind. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_003_wide: The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed. Action: The captain looks at the K2 tank under the netting — its long gun barrel clean, not a streak of soot, last night's broken arrow still stuck in the netting on the turret; he speaks softly as if writing it in his own notebook. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: his eyes rest on the clean barrel and the arrow in the net; one soft line. Sound: wind, one line of Korean dialogue.
ACTION_START: looking at the tank
ACTION_END: line spoken
NARRATION_KO: 스물두 발은 그대로였습니다. 하지만 삼백칠십은 사백이 아니었습니다. 스물두 발을 아끼는 값은 매일 기름으로 치르고 있었습니다.
DIALOGUE_KO: 한승우: 전차는 한 발도 안 쐈다.
SOUND: gió.
CONTINUITY: '전차는 한 발도 안 쐈다.' Mũi tên gãy còn trên lưới (SC_175).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, VEH_001_ref, PROP_015_ref, LOC_003_wide

### SC_263 | 35:46–35:56 | LOC_002 | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial by day, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial by day, slow pull-out. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_002_wide: Goguryeo plain fortress on a low rise in yellow steppe: dry-stacked grey granite walls slightly battered inward, rectangular protruding bastions every fifty meters, semicircular stone barbican at the south gate, two-story timber gate tower with dark grey tiled roof, wooden corner watchtowers, a three-story wooden pagoda inside, black three-legged crow banners, amber low sun through yellow dust. Action: High aerial by day: the granite fortress in the middle of the plain; grey felt Sui tents now cover the plain to the west, south and north in an unbroken ring; to the east a small valley with a thin thread of camouflage netting lies just inside the ring; pale grey sky. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow pull-out showing the closed ring. Sound: high wind, Sui drums from several directions.
ACTION_START: fortress and valley
ACTION_END: pulled out, ring closed
NARRATION_KO: 포위는 하룻밤 사이에 닫혔습니다. 골짜기는 그 안에 있었습니다. 들어올 수는 있어도 나갈 수는 없는 자리였습니다. 포위된 것은 성이 아니라 이 부대였습니다. 성은 늘 포위될 준비가 되어 있었습니다.
DIALOGUE_KO: 
SOUND: gió trên cao, trống Tùy nhiều hướng.
CONTINUITY: Vòng vây khép — thung lũng nằm trong.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_002_wide

### SC_264 | 35:56–36:06 | LOC_002 (LOC_002_siege_works) | — | WPN_201, VEH_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide lateral slide over siege works  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide lateral slide over siege works. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @VEH_201_ref: Sui dynasty eight-wheeled siege tower, tall four-story raw timber frame narrowing upward, front and sides covered in wet dark ox hide, drop-bridge at the top, arrow slits, eight solid wooden wheels, red Sui banner on top, pushed by hundreds of soldiers and oxen. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_002_wide: The yellow plain west of the Goguryeo fortress: Sui soldiers digging a ditch and raising earth banks, wooden watchtowers going up, the raw timber frames of siege towers being assembled, grey felt tents in grid rows behind, dry-stacked grey granite fortress walls with rectangular bastions and a timber gate tower in the background, cold grey sky. Action: On the plain west of the fortress: Sui soldiers by the thousand dig a ditch and pile earth, raise wooden watchtowers, and assemble the raw timber frames of tall siege towers on the trampled grass; grey sky; no faces distinct. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow lateral slide along the works. Sound: hammers, timber, distant shouted orders.
ACTION_START: ditch diggers
ACTION_END: siege tower frames
NARRATION_KO: 수나라는 이 성을 여러 달 에워쌀 것이었습니다. 요동성이 버티는 동안, 백만 대군은 여기 묶여 있었습니다. 성 안에는 스무 날 치 곡식에 백 수레가 더해졌습니다. 그것이 하룻밤의 값이었습니다.
DIALOGUE_KO: 
SOUND: búa, gỗ, hô lệnh xa.
CONTINUITY: VEH_201 khung tháp đang lắp (chưa bọc da).
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, VEH_201_ref, PROP_021_ref, LOC_002_wide
AI_RISK: đám đông lao động → wide, không mặt

### SC_265 | 36:06–36:14 | LOC_002 (LOC_002_gateyard) | CHAR_001 | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium shot inside the gate, static
IMAGE_PROMPT: Medium shot inside the gate, static. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_002_detail: Inside the east gate of the Goguryeo fortress at night: a packed-earth yard behind two-leaf iron-sheathed wooden gate doors, a stone stair climbing the dry-stacked grey granite wall, torches in iron brackets, black three-legged crow banners, timber halls with dark tiled roofs behind. Action: By day inside the east gate the captain walks past the gate doors bristling with arrows; he stops, pulls one arrow out of the wood, turns its barbed triangular head in the light, slides it into his chest pocket, and walks on down the packed-earth street toward the granaries; no dialogue. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he stops at the door, works an arrow free, looks at the head, pockets it, and walks on out of frame. Sound: an arrow drawn from wood, boots on packed earth, unloading sounds far off.
ACTION_START: walking past the arrow-studded door
ACTION_END: arrow pocketed, walking away
NARRATION_KO: 그는 화살 하나를 가졌습니다. 이 땅이 그에게 준 첫 번째 것이었습니다. 화살은 이 땅의 말이었습니다. 그는 아직 그 말을 배우는 중이었습니다.
DIALOGUE_KO: 
SOUND: tên rút khỏi gỗ, giày trên đất nện, tiếng dỡ hàng xa.
CONTINUITY: Mũi tên P-28: 한승우 giữ suốt series.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, PROP_015_ref, LOC_002_detail
AI_RISK: tay rút tên → 1 tay, 1 mũi tên

### SC_266 | 36:14–36:22 | LOC_002 (LOC_002_granary) | CHAR_104, CHAR_001, REFUGEES | — | PROPS: PROP_022 | TYPE: video8s | 8s
SHOT: Medium shot at the granary door, static
IMAGE_PROMPT: Medium shot at the granary door, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. @PROP_022_ref: grey hemp grain sacks about forty kilograms tied at the mouth, half-buried in a shallow wet earth pit, spilled millet and pressed millet cakes, a bamboo carrying pole. Setting @LOC_002_detail: Inside the Goguryeo fortress at a raised-floor timber granary standing on thick wooden posts with a dark grey tiled roof, wooden steps up to its door, grey hemp grain sacks, a packed-earth street, two-wheeled ox carts, timber halls and a three-story wooden pagoda behind, the dry-stacked grey granite wall in the distance, cold grey daylight. Action: At the raised-floor timber granary villagers in hemp carry grey grain sacks up the wooden steps from ox carts; the fortress commander stands at the granary door with a bundle of bamboo tally slips, tapping one for each sack that passes, not turning as the captain steps into the doorframe behind him; grey light. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: sacks go past up the steps, a tally slip taps for each; the captain appears in the doorframe; the commander speaks one line without turning. Sound: sacks landing on wood, bamboo slips, villagers, one line of Korean dialogue.
ACTION_START: sacks passing, captain arriving
ACTION_END: captain in the doorframe, commander's line
NARRATION_KO: 성주의 첫 마디는 감사가 아니었습니다. 사실이었습니다. 성주는 빚을 말했습니다. 갚아야 할 쪽은 성이었습니다.
DIALOGUE_KO: 고정수: 그대들이 없었으면 쌀은 못 들어왔소.
SOUND: bao thóc đặt xuống sàn gỗ, thẻ tre gõ, tiếng dân.
CONTINUITY: Kho lương (sub-lock). Dân = extras không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, CHAR_001_ref, PROP_022_ref, LOC_002_detail

### SC_267 | 36:22–36:30 | LOC_002 (LOC_002_granary) | CHAR_104 | — | PROPS: PROP_022 | TYPE: video8s | 8s
SHOT: Medium close-up, static
IMAGE_PROMPT: Medium close-up, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @PROP_022_ref: grey hemp grain sacks about forty kilograms tied at the mouth, half-buried in a shallow wet earth pit, spilled millet and pressed millet cakes, a bamboo carrying pole. Setting @LOC_002_detail: Inside the Goguryeo fortress at a raised-floor timber granary standing on thick wooden posts with a dark grey tiled roof, wooden steps up to its door, grey hemp grain sacks, a packed-earth street, two-wheeled ox carts, timber halls and a three-story wooden pagoda behind, the dry-stacked grey granite wall in the distance, cold grey daylight. Action: The fortress commander taps his bamboo tally slip on the last grain sack and turns his head to look at the captain off-frame for the first time; grey-streaked beard, grey cloak, keys at his belt; the second sentence heavier than the first. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the slip taps the sack, his head turns, one heavy line. Sound: bamboo on hemp sack, one line of Korean dialogue.
ACTION_START: tapping the last sack
ACTION_END: head turned, line delivered
NARRATION_KO: 두 번째 마디도 사실이었습니다. 쇠수레가 오지 않았다면 이천 기도 오지 않았을 것입니다.
DIALOGUE_KO: 고정수: 그대들이 있어서 저들도 여기 온 것이오.
SOUND: thẻ tre, bao thóc.
CONTINUITY: '그대들이 있어서 저들도 여기 온 것이오.'
CHAIN_FROM: SC_266
CUT_HALF: no
REFS: CHAR_104_ref, PROP_022_ref, LOC_002_detail

### SC_268 | 36:30–36:38 | LOC_002 (LOC_002_granary) | CHAR_001, REFUGEES | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium shot in the doorframe, slow push-in
IMAGE_PROMPT: Medium shot in the doorframe, slow push-in. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_002_detail: Inside the Goguryeo fortress at a raised-floor timber granary standing on thick wooden posts with a dark grey tiled roof, wooden steps up to its door, grey hemp grain sacks, a packed-earth street, two-wheeled ox carts, timber halls and a three-story wooden pagoda behind, the dry-stacked grey granite wall in the distance, cold grey daylight. Action: The captain stands silent in the granary doorframe; behind him villagers still carry sacks; his right hand rises to the arrow in his chest pocket and rests there; his face gives nothing away. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in: the hand rises to the chest pocket and stays on the arrow; the face holds; no dialogue. Sound: sacks, bamboo slips, Sui drums faint beyond the wall.
ACTION_START: standing in the doorframe
ACTION_END: tight on face, hand on the pocket
NARRATION_KO: 감사는 없었습니다. 계산이 있었습니다. 한승우도 계산하고 있었습니다. 그의 계산에는 아흔네 명이 있었습니다. 두 계산은 아직 같은 답을 내지 않았습니다.
DIALOGUE_KO: 
SOUND: bao thóc, thẻ tre, trống Tùy xa ngoài tường.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, PROP_015_ref, LOC_002_detail

### SC_269 | 36:38–36:48 | LOC_002 (LOC_002_westwall) | CHAR_001 | — | PROPS: PROP_012 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: extreme close-up on a shoulder patch beside a banner, slow pull-out
IMAGE_PROMPT: Still for ken-burns: extreme close-up on a shoulder patch beside a banner, slow pull-out. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_002_detail: On a rectangular protruding bastion of the west wall of the Goguryeo fortress: dry-stacked grey granite parapet with arrow slits, a black three-legged crow banner on a tall bamboo pole, and beyond the wall an ocean of grey felt Sui tents with red and yellow banners covering the trampled yellow plain to the horizon under a pale silver sky. Action: Extreme close-up: the small full-color Korean flag patch on the right shoulder of the captain's granite-camo uniform, and right beside it a black three-legged crow on a yellow silk banner flapping on its bamboo pole set into the grey granite parapet; grey sky. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. The flag patch: small full-color embroidered South Korean Taegukgi flag patch, red and blue taeguk circle with four black trigrams on white, about seven by four centimeters, on the RIGHT shoulder as in the character lock. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow pull-out from the two flags side by side. Sound: the banner snapping in wind.
ACTION_START: patch and banner tight
ACTION_END: pulled out, wall and banner
NARRATION_KO: 성벽 위에 두 개의 깃발이 나란히 섰습니다. 서로 알지 못하는 깃발이었습니다. 하나는 이 땅의 옛 깃발이었고, 하나는 이 땅의 먼 훗날 깃발이었습니다.
DIALOGUE_KO: 
SOUND: cờ đập gió.
CONTINUITY: Contrast bắt buộc: 태극기 cạnh 삼족오. LƯU Ý: PROP_011 lock ghi 'left shoulder' ↔ CHAR lock 'right shoulder' → KHÔNG dán PROP_011 (mâu thuẫn), mô tả patch theo CHAR lock vai phải; cần user/world-designer sửa PROP_011 (xem báo cáo).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, PROP_012_ref, LOC_002_detail
AI_RISK: patch cờ + cờ lụa → tĩnh, cận, không chữ

### SC_270 | 36:48–36:56 | LOC_002 (LOC_002_granary) | CHAR_105, CHAR_104 | — | PROPS: PROP_022 | TYPE: video8s | 8s
SHOT: Medium two-shot at the granary, static
IMAGE_PROMPT: Medium two-shot at the granary, static. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @PROP_022_ref: grey hemp grain sacks about forty kilograms tied at the mouth, half-buried in a shallow wet earth pit, spilled millet and pressed millet cakes, a bamboo carrying pole. Setting @LOC_002_detail: Inside the Goguryeo fortress at a raised-floor timber granary standing on thick wooden posts with a dark grey tiled roof, wooden steps up to its door, grey hemp grain sacks, a packed-earth street, two-wheeled ox carts, timber halls and a three-story wooden pagoda behind, the dry-stacked grey granite wall in the distance, cold grey daylight. Action: The Goguryeo officer with the white feather steps into the granary, road dust on his armor, and bows his head to the fortress commander, speaking briefly and formally; grain sacks, bamboo slips. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he steps in, bows his head, one short formal line. Sound: armor, boots on wooden floor, one line of Korean dialogue.
ACTION_START: officer entering
ACTION_END: head bowed, line delivered
NARRATION_KO: 평양. 왕이 있는 곳이었습니다. 왕의 글은 요동까지 열흘이 걸렸습니다. 그래도 명령은 왕의 것이었습니다.
DIALOGUE_KO: 해모루: 성주, 평양에서 전령이 왔습니다.
SOUND: giáp, giày trên sàn gỗ.
CONTINUITY: '성주, 평양에서 전령이 왔습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_ref, CHAR_104_ref, PROP_022_ref, LOC_002_detail

### SC_271 | 36:56–37:04 | LOC_002 (LOC_002_granary) | CHAR_104 | — | PROPS: PROP_022 | TYPE: video8s | 8s
SHOT: Medium shot, single slow pan following him out
IMAGE_PROMPT: Medium shot, single slow pan following him out. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @PROP_022_ref: grey hemp grain sacks about forty kilograms tied at the mouth, half-buried in a shallow wet earth pit, spilled millet and pressed millet cakes, a bamboo carrying pole. Setting @LOC_002_detail: Inside the Goguryeo fortress at a raised-floor timber granary standing on thick wooden posts with a dark grey tiled roof, wooden steps up to its door, grey hemp grain sacks, a packed-earth street, two-wheeled ox carts, timber halls and a three-story wooden pagoda behind, the dry-stacked grey granite wall in the distance, cold grey daylight. Action: The fortress commander sets the bamboo tally slips down on a grain sack, looks at the row of uncounted sacks, walks out of the granary and stops at the foot of a stone stair up the west wall, looking up toward where Sui drums sound over the parapet — then turns away toward the halls. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera pans slowly with him: slips set down, a look at the sacks, out the door, a pause at the foot of the stair looking up, then he turns away. No dialogue. Sound: keys, bamboo slips, distant drums.
ACTION_START: setting down the slips
ACTION_END: turning away from the stair
NARRATION_KO: 왕의 글이었습니다. 성주는 읽기 전에 내용을 알았습니다. 왕의 글은 언제나 하나였습니다. 지키라. 곳간 셈은 끝나지 않았습니다.
DIALOGUE_KO: 
SOUND: chìa khóa, thẻ tre, trống xa.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, PROP_022_ref, LOC_002_detail

### SC_272 | 37:04–37:14 | LOC_001 (LOC_001_sui_camp_day) | CHAR_205, XIANBEI_SCOUTS | VEH_206, UAV_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide, slow slide west
IMAGE_PROMPT: Still for ken-burns: medium-wide, slow slide west. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_001_wide: Sui camp on the east bank of the Liao River by day: grid rows of grey felt tents to the horizon, red and yellow banners, horse lines, cooking smoke, trampled yellow grass and dust, cold pale grey sky. Action: Morning in the Sui camp: the bareheaded Xianbei commander lashes the wrecked grey quadcopter behind his saddle with leather cord; a few Xianbei riders already mounted beside him; the road west runs through a sea of grey tents. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow slide toward the west along the road through the tents. Sound: leather cord, horses, a noisy camp.
ACTION_START: commander tying the drone
ACTION_END: road west through the tents
NARRATION_KO: 같은 아침, 탁발흠은 서쪽으로 말을 몰았습니다. 안장에는 쇠새가 묶여 있었습니다. 그는 황제에게 직접 보고할 수 있는 몇 안 되는 사람이었습니다.
DIALOGUE_KO: 
SOUND: dây da, ngựa, trại ồn.
CONTINUITY: 탁발흠 đi ~45 km về hành doanh 양제 (D5 đêm).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, VEH_206_ref, UAV_001_ref, LOC_001_wide

### SC_273 | 37:14–37:22 | LOC_003 (LOC_003_rim_day) | CHAR_107, CHAR_004 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot from behind and to the side, static
IMAGE_PROMPT: Medium two-shot from behind and to the side, static. @CHAR_107_refugee_ep1: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close. @CHAR_004_ref: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Blue nitrile gloves stained with fresh blood, a few loose strands of hair escaping the bun, fine yellow dust on helmet. Setting @LOC_003_wide: The eastern rim of the hidden valley by day: dry yellow grass and bare oak scrub, and in the distance the Goguryeo fortress of dry-stacked grey granite on its low rise with black banners, the yellow plain beyond it covered with grey felt Sui tents to the horizon under a pale grey sky. Action: The girl in red-threaded braids and the medic sit side by side on the valley's eastern rim looking out at the granite fortress and the sea of grey tents beyond it; the girl asks without turning her head; the medic does not answer — she only closes her hand tighter around the girl's. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the girl asks one line without turning; the medic says nothing and her hand tightens on the girl's. Sound: wind, grass, one line of Korean dialogue.
ACTION_START: two sitting, looking out
ACTION_END: medic's hand tightened, no answer
NARRATION_KO: 돌아갈 길은 없었습니다. 서아는 그 말을 하지 않았습니다. 거짓말도 하지 않았습니다.
DIALOGUE_KO: 아리: 언니, 돌아갈 수 있어요? 언니네 집으로요.
SOUND: gió, cỏ.
CONTINUITY: '언니, 돌아갈 수 있어요? 언니네 집으로요.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_refugee_ep1, CHAR_004_ref, LOC_003_wide

### SC_274 | 37:22–37:30 | LOC_002 (LOC_002_westwall) | CHAR_001, CHAR_104 | — | PROPS: PROP_015 | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: wide on the west wall, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide on the west wall, slow pull-out. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_002_detail: On a rectangular protruding bastion of the west wall of the Goguryeo fortress: dry-stacked grey granite parapet with arrow slits, a black three-legged crow banner on a tall bamboo pole, and beyond the wall an ocean of grey felt Sui tents with red and yellow banners covering the trampled yellow plain to the horizon under a pale silver sky. Action: The captain stands alone on a protruding bastion of the west wall, a Goguryeo arrow in his hand, before an ocean of grey Sui tents spreading to the horizon under a silver sky; a hundred meters along the wall on another bastion a small figure in a grey cloak — the fortress commander — looks out the same way. Light: Flat silver morning light under a pale grey sky, cold wind, yellow dust. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (8 s): slow pull-out until the two figures are two distant dots on the long wall. Sound: wind, drums very far.
ACTION_START: captain on the bastion, commander further along
ACTION_END: two dots on the wall
NARRATION_KO: 성 안에는 스무 날 치 곡식과 백 수레가 있었습니다. 성 밖에는 백만이 있었습니다. 성벽 위에서 두 사람은 같은 것을 보았습니다. 끝이 없는 천막이었습니다.
DIALOGUE_KO: 
SOUND: gió, trống rất xa.
CONTINUITY: Kết P11. Open loop. Không tableau đôi (decisions).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_104_ref, PROP_015_ref, LOC_002_detail


## [Phần 12] 그 천둥을 가져오라 (37:30–40:00) · chiếu vua, hành doanh 양제, end card

### SC_275 | 37:30–37:40 | LOC_002 (LOC_002_hall) | CHAR_104, CHAR_001, CHAR_105, PYONGYANG_COURIER | — | PROPS: PROP_013 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide interior, slow push to the bamboo tube
IMAGE_PROMPT: Still for ken-burns: wide interior, slow push to the bamboo tube. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. Goguryeo courier around 25, lean build, road-dusty face, black topknot under a cloth headband, light leather lamellar vest over a dark brown hemp jacket, wide trousers, straw sandals, holding a black lacquered bamboo tube with red silk cord. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_002_interior: Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze. Action: Inside the dark timber hall at night: a road-dusty Goguryeo courier kneels in the center of the floor holding up a black lacquered bamboo tube in both hands; the fortress commander sits at the low black table; the captain stands beside a red pillar with the Goguryeo officer at his side; clay oil lamps, the leather map on its frame. Light: Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in to the bamboo tube in the courier's raised hands. Sound: lamp flames, the kneeling man's breath.
ACTION_START: wide hall
ACTION_END: tight on the tube
NARRATION_KO: 그날 저녁, 평양의 전령이 요동성 대청에 무릎을 꿇었습니다. 전령은 평양에서 열흘을 달려왔습니다. 글은 짧았습니다. 전령은 성주 앞에서만 글을 꺼냈습니다.
DIALOGUE_KO: 
SOUND: lửa đèn, hơi thở người quỳ.
CONTINUITY: 4 người trong khung (không ai nói). Đại sảnh = LOC_002_interior.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, CHAR_001_ref, CHAR_105_ref, PROP_013_ref, LOC_002_interior
AI_RISK: 4 người nội thất → wide, mỗi người 1 dấu hiệu

### SC_276 | 37:40–37:48 | LOC_002 (LOC_002_hall) | CHAR_104 | — | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Medium shot over the low table, static
IMAGE_PROMPT: Medium shot over the low table, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_002_interior: Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze. Action: The fortress commander takes the bamboo tube, opens its cap, draws out a pale yellow silk scroll on a black lacquered rod and unrolls it on the low black table — columns of soft unreadable brush calligraphy and a square red seal impression at the end; he reads, lips motionless; oil lamp light. Light: Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: cap off, scroll drawn out, unrolled across the table, his eyes move down the columns, lips still. Sound: silk, the wooden rod rolling.
ACTION_START: opening the tube
ACTION_END: scroll open, reading
NARRATION_KO: 영양왕 고원. 고구려의 스물여섯 번째 왕이었습니다. 수나라를 두 번 맞은 왕이었습니다. 598년에 한 번, 그리고 지금.
DIALOGUE_KO: 
SOUND: lụa, trục gỗ lăn.
CONTINUITY: PROP_013 chiếu chỉ (calligraphy mờ, ấn son).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, PROP_013_ref, LOC_002_interior
AI_RISK: chữ trên chiếu → 'soft unreadable brush calligraphy'

### SC_277 | 37:48–37:58 | LOC_002 (LOC_002_hall) | — | — | PROPS: PROP_013 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up on the silk scroll, slow vertical drift down the columns
IMAGE_PROMPT: Still for ken-burns: close-up on the silk scroll, slow vertical drift down the columns. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_002_interior: Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze. Action: Close on the pale yellow silk edict under oil lamp light: columns of black brush calligraphy rendered soft and unreadable, a large square red seal impression, the black lacquered rod with bronze end caps at the edge. Light: Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow vertical drift down the columns to the red seal. The king's voice reads (character voice-over, not narrator). Sound: lamp flames.
ACTION_START: top of the scroll
ACTION_END: red seal
NARRATION_KO: 글은 짧았습니다. 짧은 글일수록 무거웠습니다. 왕은 요동성에 사람을 보내지 않았습니다. 글만 보냈습니다.
DIALOGUE_KO: 영양왕: 요동성은 죽어도 지키라. 이것이 과인의 뜻이다.
SOUND: lửa đèn.
CONTINUITY: Giọng 영양왕 = VO nhân vật. Không chữ đọc được.
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_013_ref, LOC_002_interior
AI_RISK: chữ → mờ, không ký tự thật; chữ Hán/dịch = subtitle edit

### SC_278 | 37:58–38:08 | LOC_006 (LOC_006_hall) | CHAR_102 | — | PROPS: PROP_013 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium portrait, slow push to the face
IMAGE_PROMPT: Still for ken-burns: medium portrait, slow push to the face. @CHAR_102_ref: Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. Seated on a red-lacquered wooden throne, hands on knees, edict scroll on a low table. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The Goguryeo king seated on his throne in the Pyongyang hall at night, a brush and a length of silk on the low table before him, oil lamps; his heavy-lidded face still and calculating, the long thin black beard on his chest, white silk crown with gold fittings. Light: Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in to the king's face. The king's voice continues (character voice-over). Sound: lamp flames, silence.
ACTION_START: king seated, table before him
ACTION_END: tight on the face
NARRATION_KO: 항복은 없다. 수나라 황제가 받는 것은 항복뿐이었기 때문입니다. 598년 수 문제의 삼십만은 요하에서 물러났습니다. 이번 황제는 그 아들이었습니다.
DIALOGUE_KO: 영양왕: 항복은 없다. 성과 함께 죽으라.
SOUND: lửa đèn, im.
CONTINUITY: 영양왕 1 still (P-34). LOC_006_interior. Không giống người thật.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_102_ref, PROP_013_ref, LOC_006_interior

### SC_279 | 38:08–38:16 | LOC_002 (LOC_002_hall) | CHAR_104, CHAR_001 | — | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Medium two-shot across the table, static
IMAGE_PROMPT: Medium two-shot across the table, static. @CHAR_104_ref: 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_002_interior: Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze. Action: The fortress commander rolls the silk scroll closed slowly, sets it on the low table, and raises his eyes to the captain standing by the red pillar; oil lamp light on the grey-streaked beard. Light: Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the scroll rolls closed, is set down, his eyes come up to the captain and he speaks one line. Sound: silk rolling, one line of Korean dialogue.
ACTION_START: rolling the scroll
ACTION_END: eyes on the captain, line spoken
NARRATION_KO: 성과 함께. 성주는 그 말에 이 부대를 넣었습니다. 쇠수레는 이제 성의 것이었습니다. 적어도 성주의 셈으로는.
DIALOGUE_KO: 고정수: 왕명이오. 이 성과 함께… 그대들도.
SOUND: lụa cuộn.
CONTINUITY: '왕명이오. 이 성과 함께… 그대들도.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_104_ref, CHAR_001_ref, PROP_013_ref, LOC_002_interior

### SC_280 | 38:16–38:24 | LOC_002 (LOC_002_hall) | CHAR_001, CHAR_105 | — | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Medium shot, slow push-in to the captain's face
IMAGE_PROMPT: Medium shot, slow push-in to the captain's face. @CHAR_001_ref: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. @CHAR_105_ref: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_002_interior: Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze. Action: The captain says nothing: his eyes go to the rolled scroll on the table, to the Goguryeo officer beside him who is watching him, back to the fortress commander; total silence; oil lamp light on the compass at his throat. Light: Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in: eyes to the scroll, to the officer, back; no words; the push ends tight on his face. Sound: lamp flames, silence.
ACTION_START: captain by the pillar
ACTION_END: tight on his silent face
NARRATION_KO: 한승우는 대답하지 않았습니다. 그 대답은 아직 그의 것이 아니었습니다. 그는 아흔네 명의 것이었습니다.
DIALOGUE_KO: 
SOUND: lửa đèn, im.
CONTINUITY: Không trả lời.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_ref, CHAR_105_ref, PROP_013_ref, LOC_002_interior

### SC_281 | 38:24–38:34 | LOC_004 (LOC_004_pavilion_ext) | SUI_EUNUCH | — | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide exterior at night, slow push to the silk doorway  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide exterior at night, slow push to the silk doorway. Sui court eunuch in a plain grey-blue silk robe and black gauze cap, clean-shaven, head bowed. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_004_wide: The Sui emperor's traveling court on the west bank of the Liao River at night: a huge pavilion tent with a golden silk roof and red pillars raised on a wooden dais, yellow and red silk drapes, rows of burning torches on tall poles, hundreds of eunuchs in grey-blue silk robes lining the approach, red and yellow banners, an ocean of grey felt tents with campfires to the horizon. Action: Night amid the sea of Sui tents on the west bank: a great pavilion tent with a golden silk roof and red pillars on a dais, yellow and red silk drapes at its entrance, rows of torches, hundreds of eunuchs in grey-blue silk robes lining the approach with heads bowed; red and yellow banners. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in to the drapes of the entrance. Sound: night drums, silk stirring in wind.
ACTION_START: wide pavilion and torches
ACTION_END: tight on the silk doorway
NARRATION_KO: 요하 서안. 황제의 행영이었습니다. 육합성은 아직 세워지기 전이었습니다. 하지만 이미 비단과 금이 벌판 위에 있었습니다. 행영 하나가 웬만한 성보다 컸습니다.
DIALOGUE_KO: 
SOUND: trống đêm, lụa lay gió.
CONTINUITY: Hành doanh 양제 (chưa phải 육합성) — sub-lock riêng, không tường lắp ghép.
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_021_ref, LOC_004_wide
AI_RISK: hàng trăm hoạn quan → hàng đầu cúi, xa, không mặt

### SC_282 | 38:34–38:42 | LOC_004 (LOC_004_pavilion_int) | CHAR_205, SUI_VANGUARD_GENERAL | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot low on the red carpet, static
IMAGE_PROMPT: Medium two-shot low on the red carpet, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Chinese man in his mid-50s, heavy broad build, wide fleshy face with thick black brows, long black beard streaked grey to mid-chest, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest, gilt-hilted straight sword. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: Inside the golden pavilion the bareheaded Xianbei commander kneels on the red carpet below the dais, yellow dust still on his leather armor, and sets the wrecked grey quadcopter down before him; beside him the Sui vanguard general with the black-grey beard kneels and presses his forehead to the floor; silk lanterns. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the drone is set on the carpet; the general beside him bows to the floor and speaks one line into the carpet. Sound: silk, lantern flames, a forehead touching the carpet, one line of Korean dialogue.
ACTION_START: setting the drone down
ACTION_END: general's forehead on the floor, line spoken
NARRATION_KO: 총관은 사과부터 했습니다. 황제 앞에서 부하의 말은 곧 자신의 목이었습니다. 요술이라 웃던 사람이었습니다. 황제 앞에서는 웃지 않았습니다.
DIALOGUE_KO: 수 전군총관: 폐하, 황공하오나 보셔야 할 것입니다.
SOUND: lụa, lửa, tiếng trán chạm thảm.
CONTINUITY: Bụi vàng còn nguyên (đi 45 km). Không áo choàng da sói (lock).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, EXTRA_sui_vanguard_general_ref, UAV_001_ref, LOC_004_detail

### SC_283 | 38:42–38:50 | LOC_004 (LOC_004_pavilion_int) | CHAR_201, SUI_EUNUCH | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the kneeling man's position up at the throne, static
IMAGE_PROMPT: Low angle from the kneeling man's position up at the throne, static. @CHAR_201_robe_only_ep3: Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques. Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged. Sui court eunuch in a plain grey-blue silk robe and black gauze cap, clean-shaven, head bowed. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: From the floor looking up: the Sui emperor sits on the red-and-gold carved throne in his yellow silk robe without armor, tall black crown, a round silk fan in one hand, looking down at the strange object on the carpet with cold curiosity and no surprise; he lifts the fan slightly and a eunuch in grey-blue silk steps forward to carry the drone up the dais steps on a tray. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the emperor looks down, the fan lifts a little, the eunuch comes forward and carries the drone up the steps on a tray. Sound: silk, soft eunuch footsteps.
ACTION_START: emperor looking down, fan still
ACTION_END: eunuch carrying the drone up the steps
NARRATION_KO: 수 양제 양광. 놀라는 법이 없는 사람이었습니다. 백만을 움직인 사람을 부서진 쇠새 하나가 놀라게 할 수는 없었습니다.
DIALOGUE_KO: 
SOUND: lụa, bước chân hoạn quan.
CONTINUITY: CHAR_201 = robe_only (không giáp). Quạt lụa tròn.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_201_robe_only_ep3, UAV_001_ref, LOC_004_detail

### SC_284 | 38:50–38:58 | LOC_004 (LOC_004_pavilion_int) | CHAR_201, SUI_EUNUCH | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the emperor's hand and face, static
IMAGE_PROMPT: Close-up on the emperor's hand and face, static. @CHAR_201_robe_only_ep3: Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques. Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged. Sui court eunuch in a plain grey-blue silk robe and black gauze cap, clean-shaven, head bowed. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: Close: the emperor's long fingers with a jade ring touch the broken orange-tipped propeller of the drone on a tray under a silk lantern and turn it slightly; the eunuch's hands holding the tray tremble; half-lidded eyes, thin goatee. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the ringed fingers turn the propeller, the tray trembles, he asks one line without looking up. Sound: plastic creaking faintly, lantern, one line of Korean dialogue.
ACTION_START: fingers reaching the propeller
ACTION_END: propeller turned, question asked
NARRATION_KO: 황제의 첫 질문은 소유였습니다. 누구의 것인가. 황제에게 세상의 물건은 둘뿐이었습니다. 짐의 것과, 아직 짐의 것이 아닌 것.
DIALOGUE_KO: 수 양제: 이것이 고구려의 것인가.
SOUND: nhựa gãy kêu khẽ, lửa.
CONTINUITY: '이것이 고구려의 것인가.'
CHAIN_FROM: SC_283
CUT_HALF: no
REFS: CHAR_201_robe_only_ep3, UAV_001_ref, LOC_004_detail
AI_RISK: tay cận đeo nhẫn → 1 tay, 1 vật

### SC_285 | 38:58–39:06 | LOC_004 (LOC_004_pavilion_int) | CHAR_205 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up, slight high angle, static
IMAGE_PROMPT: Medium close-up, slight high angle, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: The Xianbei commander raises his head for the first time — dried blood at his left ear, the long scar, eyes straight — and answers in short firm sentences; red carpet, lantern light. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the head comes up, eyes straight ahead, one firm line. Sound: lantern flames, one line of Korean dialogue.
ACTION_START: head down
ACTION_END: head up, line delivered
NARRATION_KO: 탁발흠은 본 대로 말했습니다. 삼족오가 아니면 고구려도 아니었습니다. 고구려의 것이 아니면 빼앗아도 되는 것이었습니다.
DIALOGUE_KO: 탁발흠: 고구려의 것이 아닙니다. 삼족오 깃발이 아니었습니다.
SOUND: lửa.
CONTINUITY: '고구려의 것이 아닙니다. 삼족오 깃발이 아니었습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, LOC_004_detail

### SC_286 | 39:06–39:14 | LOC_004 (LOC_004_pavilion_int) | CHAR_205 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: Close on the Xianbei commander's scarred face in lantern light: he speaks one sentence neither high nor low — the words of a man who stood on a hill and counted. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: one measured line, eyes unmoving. Sound: silence, one line of Korean dialogue.
ACTION_START: silent
ACTION_END: line delivered
NARRATION_KO: 
DIALOGUE_KO: 탁발흠: 저들은 손에 천둥을 쥐고 있습니다.
SOUND: im.
CONTINUITY: Direct quote #5a: '저들은 손에 천둥을 쥐고 있습니다.'
CHAIN_FROM: SC_285
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, LOC_004_detail

### SC_287 | 39:14–39:22 | LOC_004 (LOC_004_pavilion_int) | CHAR_201 | UAV_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_201_robe_only_ep3: Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques. Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: The Sui emperor lifts the broken propeller from the tray, holds it up before a silk lantern and turns it once through the light, then lowers his eyes to the kneeling man below the dais; yellow silk robe, black crown. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the propeller rises into the lantern light, turns once, his eyes drop to the kneeling man, one line. Sound: lantern, silk, one line of Korean dialogue.
ACTION_START: lifting the propeller
ACTION_END: eyes down on the kneeling man, line spoken
NARRATION_KO: 
DIALOGUE_KO: 수 양제: 그럼 그 천둥을 가져오라.
SOUND: lửa, lụa.
CONTINUITY: Direct quote #5b: '그럼 그 천둥을 가져오라.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_201_robe_only_ep3, UAV_001_ref, LOC_004_detail

### SC_288 | 39:22–39:32 | LOC_004 (LOC_004_pavilion_int) | CHAR_205, CHAR_201 | UAV_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium from the side, slow push to the drone
IMAGE_PROMPT: Still for ken-burns: medium from the side, slow push to the drone. @CHAR_205_survivor_ep1: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. @CHAR_201_robe_only_ep3: Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques. Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged. @UAV_001_ref: Small dark graphite-grey military reconnaissance quadcopter drone, four folding arms with orange-tipped propellers, short landing legs, spherical three-axis gimbal camera under the belly, tiny status LEDs, small numeral on one arm and a tiny Korean flag sticker on the body. Setting @LOC_004_detail: Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack. Action: From the side: the Xianbei commander bows until his forehead touches the red carpet; the wrecked drone lies between him and the dais steps; the emperor on the throne above, and the throne's shadow falls long across the kneeling man; silk lanterns. Light: Night interior, rich golden silk-lantern light, deep shadows. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in to the drone on the carpet. The emperor's voice off-screen gives the name. Sound: distant night drums, silk.
ACTION_START: wide: kneeling man, drone, throne
ACTION_END: tight on the drone
NARRATION_KO: 그날 밤, 부대에 이름이 붙었습니다. 황제가 지은 이름이었습니다. 이름이 붙은 부대는 쫓기는 부대였습니다.
DIALOGUE_KO: 수 양제: 뇌군이라 하라.
SOUND: trống đêm xa, lụa.
CONTINUITY: '뇌군이라 하라.' — 양제 tự đặt tên (decisions).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_survivor_ep1, CHAR_201_robe_only_ep3, UAV_001_ref, LOC_004_detail

### SC_289 | 39:32–39:42 | LOC_004 (LOC_004_pavilion_ext) | — | VEH_205, WPN_201 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: very high aerial at night, very slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: very high aerial at night, very slow pull-out. @VEH_205_ref: Sui pontoon bridge of flat-bottomed wooden boats moored side by side with hemp rope and iron chain, plank deck four meters wide, wooden mooring stakes, crossing a wide brown river. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_004_wide: The Sui emperor's traveling court on the west bank of the Liao River at night: a huge pavilion tent with a golden silk roof and red pillars raised on a wooden dais, yellow and red silk drapes, rows of burning torches on tall poles, hundreds of eunuchs in grey-blue silk robes lining the approach, red and yellow banners, an ocean of grey felt tents with campfires to the horizon. Action: Very high aerial at night: the golden pavilion is one bright point in a sea of Sui campfires stretching to every horizon; the black river and its three pontoon bridges glitter with torches; far on the east bank a dark mass — the fortress. Light: Night from high above, tens of thousands of orange campfires on a black plain, thin moonlight. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): very slow pull-out. Sound: drums, wind from high above.
ACTION_START: pavilion bright at center
ACTION_END: pulled out, fires to the horizon, fortress a dark mass
NARRATION_KO: 113만이 성 하나를 에워쌌습니다. 그리고 이제, 94명을 찾고 있었습니다. 요동성 포위는 넉 달을 갈 것이었습니다. 그 넉 달의 첫날 밤이었습니다.
DIALOGUE_KO: 
SOUND: trống, gió trên cao.
CONTINUITY: 113만 vs 94.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_205_ref, WPN_201_ref, LOC_004_wide

### SC_290 | 39:42–39:52 | LOC_003 (LOC_003_k2) | ROK_SOLDIER | VEH_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide at night, slow push to the gun barrel
IMAGE_PROMPT: Still for ken-burns: medium-wide at night, slow push to the gun barrel. ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Setting @LOC_003_wide: The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond. Action: The K2 tank under camouflage netting in the dark valley, a thin moon on its clean gun barrel, a small helmeted sentry standing by the track with his rifle slung; silence. Light: Night, thin cold moonlight, deep blue-black shadows. Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: KEN-BURNS (10 s): slow push in along the clean barrel. Sound: wind, silence.
ACTION_START: tank and sentry
ACTION_END: tight on the barrel
NARRATION_KO: 전차는 아직 한 번도 울지 않았습니다. 스물두 발. 삼백사십 킬로. 아흔네 명. 요동성의 여름은 이 숫자들로 시작되었습니다.
DIALOGUE_KO: 
SOUND: gió, im.
CONTINUITY: Kết hình: 22 viên, 370 km, 94 người.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, LOC_003_wide

### SC_291 | 39:52–40:00 | LOC_003 (LOC_003_k2) | — | — | PROPS: — | TYPE: still_kenburns | 8s
SHOT: END CARD — black frame, white title text centered (added in edit)
IMAGE_PROMPT: — (EDIT ONLY: end card đen + chữ ở khâu edit, không tạo ảnh AI)
VIDEO_PROMPT: EDIT ONLY: black frame 8 s, white centered title 「살수 612 · 2화 요동성」 added in edit; Sui drums echo 3 s into the black, then absolute silence.
ACTION_START: black
ACTION_END: black
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: tiếng trống Tùy còn vọng 3 s trong đen, rồi im tuyệt đối.
CONTINUITY: Không tạo ảnh AI. Chữ ở edit.
CHAIN_FROM: —
CUT_HALF: no
REFS: —
AI_RISK: chữ → không tạo ảnh; end card ở edit
