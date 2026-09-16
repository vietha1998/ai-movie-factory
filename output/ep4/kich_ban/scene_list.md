# 살수 612 — 4화 「평양」 · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep4.md` v2.1 (287 SC · 40:00 · 239 video8s + 48 still) · `continuity_master.json` (LOCKED) · character/location/vehicle/prop bible · template 04 §C–§H · decisions.md (sau QC 4화 → v2; sau QC 5화: VEH_207) · 04_veo/VEO_BRIEF.md.
> Format §C như 1화. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit.
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (`@CHAR_001_reeds_ep4`, `@CHAR_205_night_hunt_ep4`, `@LOC_007_island_ep4`) — tag = đúng `name` trong `reference_images`. VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json; derived state ✔ = câu nguyên văn character_bible (ref biến thể đính thay ref gốc); trạng thái trong tập (`*_ep4` do veo đặt theo bảng "Trạng thái theo tập" 4화) đính ref gần nhất — xem ep4_asset_usage.md §1. Không tên riêng; không chữ trong ảnh: sổ 박기철/sổ 서아/màn hình trưởng xe/bài thơ/end card → `OVERLAY (edit)`; Hangul trên xe KHÔNG vẽ (decisions #1); 태극기 vai PHẢI (P-38).
> **Hai track 4화:** (a) LOC_006_PYONGYANG (cửa biển 패수 → bãi đổ bộ → phố chợ/chùa trống/ngõ → cổng thủy → nội điện 평양 = REF_PROMPT_EN_INTERIOR) + LOC_008 4화 (đồi xanh mưa bắc 평양, trại Tùy 30리 dựa núi, lều 우중문, 방진 đường rút — KHÔNG dùng lock làng núi LOC_008); (b) LOC_007_SALSU (bãi lau sát đường lội → đảo lau 1 → đầm đêm/chốt gác → bờ nam trại hậu quân + cũi → cửa bãi cạn → đảo lau 2 → sương D7 → bãi bắc/cọc). Sub-lock cố định trong `logs/scratch/veo-ep4/build.py` SUBLOC → `02_script/sublocks_ep4.md`.
> **Mưa dầm toàn tập** (tháng 7): mọi Light = mưa/sương; nước tới gối (D1) → đùi (D2–D4) → thắt lưng (D7) → ngực trong lối lau (P10) — ghi trong Action. Lính Hàn: mũ tháo/bọc lưới + lau, mặt bùn, râu 1 tuần, áo vá vải nâu (WEAR §0.3). K2 = mô bùn phủ lau (VEH_STATE `VEH_001_mud`), chỉ 2 phát đêm D4.
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói (ngoại lệ SC_128 통역+태오 — 2 beat trong clip, decisions), 1 chuyển động camera. `CUT_HALF: yes` = hook 0–30 s + khối trận/contact (P2 013–015, P3 039–040, P4 053/062–074, P5 076–092, P6 116–117, P7 130–147, P8 162, P9 181, P10 207–245, P11–12 260–261/272) → edit cắt 2 shot 4 s. `2-BEAT` ×12 (SC_001/003 hook · 139/140/143/144 P7 · 209/215/226/231/240/241 P10): beat A/B ghi trong VIDEO_PROMPT; beat là góc máy khác → `INSERT_CLIP` tách riêng (3–4 s). Đại quân = aerial wide (⚑ AERIAL/QUALITY → veo_31_quality; ảnh nano_banana_pro + upscale 2K).
> **CHAIN_FROM:** chỉ khi SC trước là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (`--chain`). Không chain quá 3 clip liên tiếp.
> **POV kính đêm** (SC_062/066/131/217): prompt "monochrome green night-vision view", không HUD; SC_217 = trắng lóa. **Màn hình trưởng xe** (SC_143b/144/145/153/279): "cold blue screen with a small blank readout" — số 잔탄 08→07→06 và 위성 0개 = OVERLAY ở edit.
> **LOCK_PENDING:** `VEH_207` (kỵ Tùy trên ngựa — decisions sau QC 5화) chưa có trong continuity_master → lock tạm theo proposals P-50/vehicle_bible §0.4 (build.py LOCK_PENDING); ref `VEH_207_ref` trong ref_jobs_ep4_extra.json. Thay lock nguyên văn khi world-designer khóa.
> **Style tag (§D, cuối mọi image prompt):** `photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`
> **Negative (§E, ghi 1 lần):** `cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, modern buildings in historical scene, anachronistic clothing`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.


**Tổng:** 287 SC · 239 video8s · 48 still_kenburns · 2400 s · chain_from: 49 · cut_half: 105 · aerial/quality: 34 · insert_clip: 9 · overlay: 11 · lock_pending: 11

---


## [Phần 1] 콜드 오픈 — 「숨 쉬는 것도 작게」 (0:00–1:30) · hook, không narrator 0–32 s · D1 rạng sáng bãi lau

### SC_001 | 0:00–0:08 | LOC_007 (LOC_007_reeds_ford) | CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Extreme close-up at ground level, static camera, no shake (keyframe = beat B)
IMAGE_PROMPT: Extreme close-up at ground level, static camera, no shake (keyframe = beat B). @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The tall lieutenant lies on his side in grey-brown mud between reed stalks, one eye open and fixed, dried mud cracked across his cheekbone, rain clinging to his eyelashes; thirty centimeters above his face the wet hoof of a horse comes down into calf-deep brown water, mud spattering onto his cheek; only the eye, the mud and the hoof in frame. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–3 s): frame held on pure black, only the sound of thousands of feet and hooves churning water. Beat B (3–8 s): cut to the extreme close-up — the open eye does not blink, rain beads on the lashes, a horse's hoof drops into the water a hand's width above the face and mud spatters the cheek; the eye stays fixed; camera absolutely static. Sound: continuous churning water, hooves, one compressed breath, no music.
ACTION_START: black frame → eye open in mud, hoof rising out of frame
ACTION_END: hoof planted in the water beside the face, mud on the cheek, eye unblinking
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: nước khuấy liên tục, móng ngựa, tiếng thở bị nén. Không nhạc.
CONTINUITY: Mở tập. D1 rạng sáng, nước ngang bắp chân ở bãi lau sát đường lội. 오태민: mũ tháo (reeds_ep4). Beat A = 3 s đen làm ở edit.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, LOC_007_detail
AI_RISK: cận mắt + móng ngựa → 1 mắt, 1 móng, máy tĩnh; không thấy toàn thân ngựa (né deformed legs)

### SC_002 | 0:08–0:16 | LOC_007 (LOC_007_reeds_ford) | SUI_FEET | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle at the eye level of a man lying in the reeds, static, shallow focus
IMAGE_PROMPT: Low angle at the eye level of a man lying in the reeds, static, shallow focus. the legs and feet of Sui foot soldiers wading past, torn straw sandals, wet cloth leggings, wooden shield rims dragging in the water, no faces. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: From ground level: the legs of Sui foot soldiers wade past through calf-deep brown water — torn straw sandals, wet cloth leggings, the rims of red rectangular wooden shields dragging in the water — rank after rank without end; above them the reed tops close off almost all of the grey sky; no faces. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera static at ground level: legs and shield rims wade past left to right in an endless stream, water churning, a straw sandal slipping; the reed tops above sway; no faces enter frame. Sound: dense splashing, wooden shields knocking together, one cough, no voices, no music.
ACTION_START: first legs entering from the left, water calm
ACTION_END: stream of legs still passing, water churned brown
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: bì bõm dồn dập, gỗ khiên va nhau, một tiếng ho, không ai nói.
CONTINUITY: Máy = mắt lính nằm. Không mặt địch. WPN_201 = lính Tùy (chỉ chân/khiên).
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, LOC_007_detail
AI_RISK: đám đông chân → chỉ chân + khiên, tiêu cự nông, không mặt

### SC_003 | 0:16–0:24 | LOC_007 (LOC_007_reeds_ford) | CHAR_006, SUI_SOLDIER_BACK | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the scout's mud-blackened face at ground level, static (keyframe = beat A with the soldier's back entering behind)
IMAGE_PROMPT: Close-up on the scout's mud-blackened face at ground level, static (keyframe = beat A with the soldier's back entering behind). @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a single Sui foot soldier in a wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, straw sandals, seen from behind. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The staff sergeant lies flat in the reeds, face blackened with wet mud so that only his eyes show, soaked boonie hat, the reversed knife in his right hand pressed down into the mud; two meters behind him, out of focus, a single Sui soldier has stepped out of the column into the edge of the reeds with his back turned, loosening his trouser cord. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): static close-up on the mud-blackened face, eyes open, rain on the hat brim, the knife hand still. Beat B (4–8 s): behind him a Sui soldier's back settles two meters away, steam rising into the rain as he urinates into the reeds; the scout does not blink. Sound: urine hitting reeds, the soldier's relieved sigh, the column still wading behind, no music.
ACTION_START: scout's face still, soldier's back stepping into the reeds
ACTION_END: soldier urinating with back turned, scout unblinking
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: tiếng nước tiểu vào lau, lính Tùy thở phào, hàng quân vẫn lội phía sau.
CONTINUITY: 2-BEAT trong 1 clip (máy tĩnh, beat B là hành động nền). 백성민 mặt bùn đen (mudface_ep4), mũ boonie ướt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, WPN_201_ref, LOC_007_detail
AI_RISK: lính Tùy cận → quay lưng, out-focus; hơi nước thay chi tiết

### SC_004 | 0:24–0:32 | LOC_007 (LOC_007_reeds_ford) | CHAR_001, CHAR_002 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Extreme close-up on two hands and a rifle in the mud, static, then a slow tilt up to two faces
IMAGE_PROMPT: Extreme close-up on two hands and a rifle in the mud, static, then a slow tilt up to two faces. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: Close on the lieutenant's index finger already inside the trigger guard of a black assault rifle lying in the mud; the captain's hand in a torn glove comes down over the rifle stock and presses it slowly and firmly into the mud, his lensatic compass on its cord dangling and touching the mud; camera tilts up to the captain's mud-smeared face pressed close to the lieutenant's ear, lips barely moving. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up: the gloved hand covers the rifle stock and presses it down into the mud slowly and firmly, the compass on its cord swings and touches the mud; camera tilts up to the captain's face beside the lieutenant's ear, lips barely moving with one whispered line. Sound: rain, the column wading close by, a whisper right against the microphone.
ACTION_START: finger in the trigger guard, gloved hand descending
ACTION_END: rifle pressed into the mud, captain's lips at the lieutenant's ear
NARRATION_KO: 
DIALOGUE_KO: 한승우: 쏘지 마. 숨 쉬는 것도 작게.
SOUND: mưa, hàng quân lội, thì thầm sát mic.
CONTINUITY: '쏘지 마. 숨 쉬는 것도 작게.' — 1 câu thoại. La bàn chạm bùn (identifier 한승우). Găng rách. Súng K2C1 (WPN_001) không bọc vải ở đây.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, CHAR_002_reeds_ep4, WPN_001_ref, LOC_007_detail
AI_RISK: tay cận + súng → 2 bàn tay, chuyển động chậm, súng nằm im

### SC_005 | 0:32–0:40 | LOC_007 (LOC_007_aerial) | — | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-high aerial, slow lateral drift along the column  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Medium-high aerial, slow lateral drift along the column. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_007_wide: Wide shallow Cheongcheon River eight hundred meters across in July monsoon rain: long wet grey-brown sandbars, a line of wooden ford-marker stakes crossing the shallows, the north bank buried in dense two-meter grey-green reed beds stretching hundreds of meters, the south bank rising into low green hills, brown water, river mist, heavy grey cloud, no trees on the sandbars. Action: From above: a grey-green reed bed hundreds of meters wide on the north bank, and cutting through it a long dark line of men and horses walking in file from the water's edge up onto the bank — the line runs back across the wide grey river and vanishes toward the southern horizon; nothing else moves in the reeds. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera drifts slowly along the line of tiny figures from the reed bed toward the river, the column creeping forward beneath; rain veils the far bank; nothing in the reeds moves. Sound: high wind, rain, the faint massed splashing of thousands of feet rising from below.
ACTION_START: column entering the reed bed from the water
ACTION_END: camera over the river, column stretching to the southern horizon
NARRATION_KO: 612년 7월. 수나라 별동대 30만 5천이 살수를 건넜습니다. 그 갈대밭에는 92명의 대한민국 군인이 엎드려 있었습니다.
DIALOGUE_KO: 
SOUND: gió trên cao, tiếng lội dội lên mơ hồ.
CONTINUITY: Narrator vào 0:32. Aerial đại quân — chấm người, không chi tiết.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, LOC_007_wide
AI_RISK: đại quân → aerial trung-cao, người là chấm

### SC_006 | 0:40–0:48 | LOC_007 (LOC_007_reeds_ford) | CHAR_006, SUI_SOLDIER_BACK | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the scout's eyes at ground level, static, soldier out of focus behind
IMAGE_PROMPT: Close-up on the scout's eyes at ground level, static, soldier out of focus behind. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a single Sui foot soldier in a wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, straw sandals, seen from behind. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The scout's mud-blackened face fills the lower frame, eyes open and unmoving; behind him, out of focus, the Sui soldier retying his trouser cord kicks a reed stalk for fun, then turns and looks straight at the clump of reeds where the scout lies — one beat — then wades back to the column. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up on the unblinking eyes: behind, the out-of-focus soldier ties his cord, kicks a reed, turns to look straight toward the camera for one long beat, mutters one line, then turns away and wades off; the eyes never change. Sound: straw sandals on mud, the cord, one muttered Korean line, the column wading.
ACTION_START: eyes open, soldier tying cord behind
ACTION_END: soldier wading away out of focus, eyes unchanged
NARRATION_KO: 두 걸음이었습니다. 두 걸음 안에 사람이 엎드려 있었습니다. 수나라 병사는 갈대만 보았습니다. 갈대는 그들의 것이 아니었습니다.
DIALOGUE_KO: 수 병사: 빌어먹을 비.
SOUND: dép rơm trên bùn, dây quần, hàng quân.
CONTINUITY: Kế SC_003 cùng vị trí. Lính Tùy nói '빌어먹을 비.' — mặt out-focus, không cận.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, WPN_201_ref, LOC_007_detail
AI_RISK: mặt lính Tùy → out-focus sâu, quay đi ngay

### SC_007 | 0:48–0:56 | LOC_007 (LOC_007_reeds_ford) | CHAR_002 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the lieutenant's face and hand, static
IMAGE_PROMPT: Close-up on the lieutenant's face and hand, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The lieutenant's face in the mud: jaw clenched, a pulse visible in his neck, split lip beading blood; his index finger draws back out of the trigger guard millimeter by millimeter while the captain's gloved hand stays flat on the rifle stock at the edge of frame. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the jaw works, the neck pulse beats, the finger slides out of the trigger guard by millimeters and straightens along the rifle; the gloved hand at the frame edge never lifts. Sound: rain, a compressed breath through the nose, the column wading.
ACTION_START: finger inside the trigger guard, jaw clenched
ACTION_END: finger straight along the rifle, hand still on the stock
NARRATION_KO: 오태민에게 이것은 가장 어려운 명령이었습니다. 총이 있는데 쏘지 않는 것. 손가락 하나를 움직이지 않는 데 그의 전부가 들어갔습니다.
DIALOGUE_KO: 
SOUND: mưa, thở nén, hàng quân.
CONTINUITY: Kế SC_004. Môi nứt rớm máu (reeds_ep4). Tay 한승우 chỉ là găng ở mép khung.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_001_ref, LOC_007_detail
AI_RISK: ngón tay cận trên cò → chuyển động chậm, 1 ngón, súng tĩnh

### SC_008 | 0:56–1:04 | LOC_007 (LOC_007_reeds_ford) | CHAR_004, SUI_FEET | WPN_201 | PROPS: PROP_010 | TYPE: video8s | 8s
SHOT: Close-up at water level, static, shallow focus on the hand
IMAGE_PROMPT: Close-up at water level, static, shallow focus on the hand. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. the legs and feet of Sui foot soldiers wading past, torn straw sandals, wet cloth leggings, wooden shield rims dragging in the water, no faces. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_010_ref: South Korean army combat ration: square olive-brown plastic pouches, a flameless heating bag steaming, plastic spoon, compressed biscuit, instant coffee sachet; later a Goguryeo clay bowl of millet. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The medic lies half submerged at the edge of the reeds, only her braided head and one hand above the brown water; legs of Sui soldiers wade past close by; a broken straw sandal floats by, then a mouldy pressed millet cake drops from someone's bag, bobs, touches her fingertips and drifts on; her hand does not move. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static at water level: legs wade past, a broken sandal floats through, a small mouldy millet cake drops into the water, bobs against the still fingertips and drifts away; the hand never moves. Sound: water, a distant muttered curse, the cake plopping into the water.
ACTION_START: hand still in the water, legs passing
ACTION_END: millet cake drifting away past the fingertips
NARRATION_KO: 그들은 백 일치 군량을 압록수에 묻고 왔습니다. 남은 것은 곰팡이 핀 떡 몇 개였습니다. 배고픈 군대가 92명의 머리 위를 지나갔습니다.
DIALOGUE_KO: 
SOUND: nước, một tiếng chửi khẽ xa (lính Tùy), bánh kê chạm nước.
CONTINUITY: PROP_010 = bánh kê Tùy mốc (chỉ bánh nổi, không bao bì hiện đại). 서아 bím Goguryeo (braid_ep4).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, WPN_201_ref, PROP_010_ref, LOC_007_detail
AI_RISK: chân địch + tay → tiêu cự nông, 1 bàn tay, chân out-focus

### SC_009 | 1:04–1:12 | LOC_007 (LOC_007_reeds_ford) | CHAR_001, XIANBEI_RIDER | VEH_001, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the captain's eyes, slow push past him to the mud mound fifty meters behind
IMAGE_PROMPT: Close-up on the captain's eyes, slow push past him to the mud mound fifty meters behind. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The captain, helmet off and hair matted with mud, lies in the reeds and glances back over his shoulder: fifty meters behind, a head-high mound of wet mud stuck with reeds rises among the reed beds with a reed-wrapped barrel lying low along it; a single Xianbei rider in a fox-fur cap walks his stocky horse right along the mound, the horse sniffing at the reed layer, then moves on. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera pushes slowly from the captain's eyes past his shoulder toward the mud mound: the rider's horse walks along the mound, lowers its head and sniffs the reed layer, snorts, and walks on; the reeds on the mound do not move. Sound: hooves in soft mud, the horse snorting, rain.
ACTION_START: captain's eyes glancing back, rider approaching the mound
ACTION_END: rider passing beyond the mound, horse's head up
NARRATION_KO: 오십 미터 뒤에 전차가 있었습니다. 진흙과 갈대 밑에서 쇠는 숨을 쉬지 않았습니다. 말은 쇠 냄새를 맡지 못했습니다. 젖은 진흙이 냄새를 덮었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa trên bùn mềm, ngựa khịt mũi, mưa.
CONTINUITY: K2 = mô bùn phủ lau (VEH_001_mud). 1 kỵ Tiên Ti cận mô bùn (VEH_206). 한승우 mũ tháo.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, VEH_001_ref, VEH_206_ref, LOC_007_detail
AI_RISK: ngựa + xe → 1 ngựa, xe là mô bùn (không chi tiết thép)

### SC_010 | 1:12–1:21 | LOC_007 (LOC_007_aerial) | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 9s
SHOT: Still for ken-burns: very high aerial, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: very high aerial, slow pull-out. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_007_wide: Wide shallow Cheongcheon River eight hundred meters across in July monsoon rain: long wet grey-brown sandbars, a line of wooden ford-marker stakes crossing the shallows, the north bank buried in dense two-meter grey-green reed beds stretching hundreds of meters, the south bank rising into low green hills, brown water, river mist, heavy grey cloud, no trees on the sandbars. Action: From very high above in rain: the silver-grey river eight hundred meters wide with a long sandbar, and a dense black ribbon of people walking from the north bank across the shallows to the south bank, both ends of the ribbon cut off by the frame edges, tiny red banner dots along it; the reed bed on the north bank a still grey-green patch. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow pull-out from the black ribbon of people on the ford to the whole grey river and reed beds. Sound: high wind, rain, a faint steady march drum far off.
ACTION_START: tight on the ribbon of people on the ford
ACTION_END: wide on river, sandbar and still reed bed
NARRATION_KO: 아홉 군. 30만 5천. 살수는 얕았습니다. 무릎까지였습니다. 그래서 그들은 걸어서 건넜습니다. 건너는 데 하루 낮과 하룻밤이 걸렸습니다.
DIALOGUE_KO: 
SOUND: gió trên cao, mưa, xa xa tiếng trống hành quân đều đều.
CONTINUITY: Still 9 s. Đại quân = chấm đen. Cờ Tùy = chấm đỏ.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_007_wide
AI_RISK: đại quân → aerial rất cao, không chi tiết

### SC_011 | 1:21–1:30 | LOC_007 (LOC_007_reeds_ford) | CHAR_002 | WPN_001 | PROPS: — | TYPE: still_kenburns | 9s
SHOT: Still for ken-burns: extreme close-up on an open hand in the mud, slow push-in to the index finger
IMAGE_PROMPT: Still for ken-burns: extreme close-up on an open hand in the mud, slow push-in to the index finger. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_detail: Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops. Action: The lieutenant's open hand lies in the mud beside the black rifle, index finger stretched straight and well away from the trigger guard; on the back of the hand the wet print of a horse's hoof; rain pocks the mud around it; no face. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in from the hand and rifle to the straight index finger and the hoofprint. Sound: rain, the column fading.
ACTION_START: hand open beside the rifle
ACTION_END: tight on the index finger and hoofprint
NARRATION_KO: 누구도 방아쇠를 당기지 않았습니다. 을지문덕이 그렇게 명령했기 때문입니다.
DIALOGUE_KO: 
SOUND: mưa, hàng quân nhỏ dần.
CONTINUITY: Still 9 s. Kết P1. Không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_001_ref, LOC_007_detail
AI_RISK: tay cận → 1 bàn tay mở, tĩnh


## [Phần 2] 발견 — 「하루 일곱 번」 (1:30–4:30) · [史] 7 trận giả thua · hạm đội 내호아 vào 패수 · đảo lau 1 · 아리 cắt lau

### SC_012 | 1:30–1:40 | LOC_007 (LOC_007_south_hills) | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial over the south bank, slow slide from the river southward  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial over the south bank, slow slide from the river southward. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_007_wide: From above the south bank of the shallow river in July monsoon rain: low green hills rolling south under low grey cloud, muddy roads fanning out through wet grass and scrub, the wide grey river and its sandbars behind, rain. Action: From high above: from the south bank of the grey river nine dark columns of Sui soldiers fan out into nine muddy trails heading south over wet green hills, each column under a small cluster of red banners, empty wet ground between the columns, low grey cloud. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide from the river bank southward along the nine diverging columns. Sound: layered Sui marching drums far off, rain.
ACTION_START: river bank with columns leaving the water
ACTION_END: nine trails fanning south over the hills
NARRATION_KO: 부여도, 낙랑도, 그리고 일곱 길. 아홉 군은 살수 남쪽에서 다시 아홉 갈래로 갈라졌습니다. 목적지는 하나였습니다. 평양. 남은 거리는 이백 리였습니다.
DIALOGUE_KO: 
SOUND: trống Tùy nhiều lớp xa, mưa.
CONTINUITY: Still 10 s. 9 quân = 9 vệt. Aerial.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_007_wide
AI_RISK: đại quân → aerial cao, cột là vệt

### SC_013 | 1:40–1:48 | LOC_008 (LOC_008_hilltop) | CHAR_101, CHAR_105 | VEH_101 | PROPS: PROP_012, PROP_018 | TYPE: video8s | 8s
SHOT: Medium shot from the side on the hill crest, static with a slight push-in
IMAGE_PROMPT: Medium shot from the side on the hill crest, static with a slight push-in. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_008_hills_rain_ep4: The crest of a green hill in monsoon rain: wet grass and scrub, low grey cloud, and below in the valley a muddy road filled with an endless column of Sui soldiers under wet red and yellow banners. Action: Montage of the days before: the silver-bearded Goguryeo general sits his armored horse on the wet crest of a green hill, plume feathers dripping, cloak soaked; beside him the young officer with the single white feather holds the black horn; below in the valley an endless Sui column fills the muddy road; the general raises two fingers. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium shot with a slight push-in: rain runs off the plume, the horse shifts, the general looks down at the column and raises two fingers, says one short line; the officer beside him lifts the horn. Sound: rain, horses stamping, Sui drums far below, one line of Korean dialogue.
ACTION_START: both mounted on the crest, hands on reins
ACTION_END: general's two fingers raised, officer lifting the horn
NARRATION_KO: 살수를 건너기 전 열흘 동안, 을지문덕은 하루에 일곱 번 싸웠습니다. 그리고 일곱 번 다 졌습니다. 지는 것은 그의 명령이었습니다.
DIALOGUE_KO: 을지문덕: 일곱 번째. 가게.
SOUND: mưa, ngựa giậm, trống Tùy xa.
CONTINUITY: [史] montage ngày trước D1 (D−6…D−1). 을지문덕 giáp mưa (rain_ep4, ref salsu_rain_ep5). 해모루 radio kẹp giáp (radio_ep3) — có từ 3화. Tù và 7 vạch (PROP_018).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_101_salsu_rain_ep5, CHAR_105_radio_ep3, VEH_101_ref, PROP_012_ref, PROP_018_ref, LOC_008_hills_rain_ep4
AI_RISK: 2 kỵ sĩ + ngựa giáp → máy ngang, ngựa đứng yên

### SC_014 | 1:48–1:56 | LOC_008 (LOC_008_road_column) | CHAR_105, GOG_CAVALRYMEN | VEH_101, WPN_101, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide lateral tracking shot at slope height, no close-ups  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide lateral tracking shot at slope height, no close-ups. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_008_hills_rain_ep4: A muddy dirt road through low green hills in monsoon rain, 612 AD: mud churned to soup by countless feet, wet grass and scrub on both sides, low grey cloud, an endless column of Sui infantry with wet red and yellow banners filling the road to the horizon. Action: Three hundred Goguryeo cavalry led by the young officer with the white feather pour down the wet green slope, loose a volley of arrows into the flank of the Sui column on the muddy road — a few Sui soldiers drop, a wall of red shields goes up — then the riders wheel close along the column and haul on their reins; rain. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Wide tracking shot moving with the charge: riders sweep down the slope, bows release together, red shields rise along the column, the riders wheel and rein in; one shouted line. Sound: massed hooves, a volley of bowstrings, Sui shouting, rain.
ACTION_START: cavalry cresting the slope
ACTION_END: cavalry wheeling along the column, reins hauled
NARRATION_KO: 공격은 진짜였습니다. 화살도 진짜였습니다. 다만 끝까지 가지 않았습니다.
DIALOGUE_KO: 해모루: 쏘고 돌아선다!
SOUND: vó ngựa dồn, dây cung hàng loạt, tiếng hô Tùy.
CONTINUITY: [史] trận 1/7. Wide, không cận thương vong. 해모루 hô '쏘고 돌아선다!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_radio_ep3, VEH_101_ref, WPN_101_ref, WPN_201_ref, LOC_008_hills_rain_ep4
AI_RISK: kỵ số đông + cung → wide tracking, bùn/mưa che chân ngựa

### SC_015 | 1:56–2:04 | LOC_008 (LOC_008_road_column) | CHAR_105, GOG_CAVALRYMEN, SUI_OFFICER | VEH_101, WPN_201 | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Medium shot, camera following the falling banner
IMAGE_PROMPT: Medium shot, camera following the falling banner. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, straight sword, face weathered and shouting. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_008_hills_rain_ep4: A muddy dirt road through low green hills in monsoon rain, 612 AD: mud churned to soup by countless feet, wet grass and scrub on both sides, low grey cloud, an endless column of Sui infantry with wet red and yellow banners filling the road to the horizon. Action: The Goguryeo cavalry break and flee in disorder back up the hill, and a tall yellow banner with a black three-legged crow drops into the mud on purpose; Sui soldiers cheer and the vanguard breaks ranks to chase; a Sui officer in mingguang armor snatches up the muddy banner and raises it overhead. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera follows the banner as it falls from a rider's hand into the mud, riders scattering uphill beyond it; Sui soldiers run past cheering, an officer lifts the muddy banner high. Sound: Sui cheering, hooves fading, the wet banner slapping mud.
ACTION_START: banner falling from the rider's hand
ACTION_END: Sui officer holding the muddy banner overhead
NARRATION_KO: 깃발 하나를 버리면 수나라 군은 십 리를 더 왔습니다. 십 리는 곧 하루치 밥이었습니다. 을지문덕은 깃발로 밥을 샀습니다.
DIALOGUE_KO: 
SOUND: reo hò Tùy, vó ngựa xa dần, cờ đập bùn.
CONTINUITY: [史] cờ rơi cố ý. Cờ 삼족오 = PROP_012.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_radio_ep3, VEH_101_ref, WPN_201_ref, PROP_012_ref, LOC_008_hills_rain_ep4
AI_RISK: đám đông đuổi → theo cờ, người phụ out-focus

### SC_016 | 2:04–2:14 | LOC_008 (LOC_008_hillside_rock) | CHAR_105 | — | PROPS: PROP_018 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up on hands carving a horn, slow push-in to the seventh notch
IMAGE_PROMPT: Still for ken-burns: close-up on hands carving a horn, slow push-in to the seventh notch. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_008_hills_rain_ep4: A wet grey rock on a green hillside in monsoon rain, wet grass, scrub, horses standing with heads down in the rain behind, low grey cloud. Action: The young officer with the white feather sits on a wet rock in the rain, a small knife carving a seventh short notch into the black horn's handle beside six older notches; mud on his hands, hollow tired eyes above, the modern radio clipped to his chest armor. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in from the hands and horn to the fresh seventh notch. Sound: knife scraping horn, rain, a horse breathing.
ACTION_START: knife on the horn, seven notches
ACTION_END: tight on the seventh notch
NARRATION_KO: 하루 일곱 번. 해모루는 나각 손잡이에 일곱 줄을 새겼습니다. 다음 날 아침이면 다시 처음부터였습니다. 그렇게 열흘, 일흔 번을 졌습니다. 삼국사기는 이렇게 적었습니다. 하루에 일곱 번 싸워 일곱 번 다 이겼다고. 수나라 쪽에서 본 문장이었습니다.
DIALOGUE_KO: 
SOUND: dao cạo sừng, mưa, ngựa thở.
CONTINUITY: Still 10 s. Tù và 7 vạch (PROP_018 — cần ref PROP_018_ref). Radio trên giáp.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, PROP_018_ref, LOC_008_hills_rain_ep4
AI_RISK: tay + dao cận → tĩnh, 2 bàn tay, dao nhỏ

### SC_017 | 2:14–2:22 | LOC_008 (LOC_008_road_column) | CHAR_202, SUI_SOLDIERS_STARVING | VEH_207, WPN_201 | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Lateral tracking shot at rider height along the column
IMAGE_PROMPT: Lateral tracking shot at rider height along the column. @CHAR_202_ref: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Armor and breast mirrors streaming with rain, red cloak heavy with water, white beard dripping, mud splashed to the thighs. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_hills_rain_ep4: A muddy dirt road through low green hills in monsoon rain, 612 AD: mud churned to soup by countless feet, wet grass and scrub on both sides, low grey cloud, an endless column of Sui infantry with wet red and yellow banners filling the road to the horizon. Action: The white-bearded Sui general in mingguang armor with both breast mirrors streaming rain rides along the muddy column on a tall warhorse, sword pointed south, shouting hoarsely; on both sides of the road gaunt soldiers chew strips of tree bark, one man sits slumped in the mud until a comrade hauls him up. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with the horse along the column: the general points his sword south and shouts one line, rain streaming off his beard; soldiers on the roadside chew bark, one slumped man is hauled up as the horse passes. Sound: hooves, a hoarse shout, rain, feet in mud.
ACTION_START: general riding into frame, sword rising
ACTION_END: sword pointed south, slumped soldier hauled upright behind
NARRATION_KO: 우중문은 이기고 있었습니다. 적어도 그렇게 믿었습니다. 그의 병사들은 나무껍질을 씹으며 이기고 있었습니다.
DIALOGUE_KO: 우중문: 평양은 사흘 거리다! 사흘이면 끝난다!
SOUND: ngựa, hét khàn, mưa, chân lội bùn.
CONTINUITY: '평양은 사흘 거리다! 사흘이면 끝난다!' Ngựa Tùy = VEH_207 (LOCK_PENDING). 우중문 giáp mưa (rain_ep4).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_ref, VEH_207_ref, WPN_201_ref, PROP_021_ref, LOC_008_hills_rain_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)
AI_RISK: tướng trên ngựa + đám đông → tracking ngang, lính phụ out-focus quay đi

### SC_018 | 2:22–2:32 | LOC_006 (LOC_006_estuary) | — | VEH_204 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial over grey sea, slow pull from open water into the river mouth  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial over grey sea, slow pull from open water into the river mouth. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_006_wide: Grey sea and a wide river mouth in monsoon rain: low grey waves, mist hiding the horizon, flat marshy shores, rain. Action: Hard cut: from high above a grey sea in rain, hundreds of Sui tower warships with dark red-brown hulls, two- and three-story wooden deckhouses and square brown sails file from the open sea into a wide river mouth, red and yellow banners hanging wet, mist hiding the horizon. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull from the open-sea end of the fleet into the river mouth. Sound: waves, massed oars, naval drums.
ACTION_START: fleet at sea
ACTION_END: lead ships entering the river mouth
NARRATION_KO: 같은 무렵, 바다. 내호아의 수군이 패수 하구에 들어왔습니다. 동래에서 배로 떠난 강회의 군사들이었습니다. 평양까지 육십 리. 배로 반나절이었습니다.
DIALOGUE_KO: 
SOUND: sóng, mái chèo hàng loạt, trống thủy quân.
CONTINUITY: Still 10 s. HARD CUT sang track (a). 누선 = VEH_204.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_204_ref, PROP_021_ref, LOC_006_wide
AI_RISK: hàng trăm thuyền → aerial cao, thuyền là hình khối

### SC_019 | 2:32–2:40 | LOC_006 (LOC_006_warship_bow) | CHAR_204 | VEH_204 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the deck looking up at the admiral at the bow, static, rain driving across
IMAGE_PROMPT: Low angle from the deck looking up at the admiral at the bow, static, rain driving across. @CHAR_204_ref: Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. River spray on the oiled cloak and helmet, wet beard, confident grin, dao drawn. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. Setting @VEH_204_ref: The bow deck of a Sui tower warship under way on a wide grey river in rain: wet dark red-brown planking, a carved beast head at the prow, wooden railings, rows of oars rising and falling below, wooden deckhouses behind, grey water and misty banks. Action: The Sui admiral in the wide-brimmed iron helmet and oiled cloak stands at the bow with one hand gripping the wet railing, flattened nose lifted toward the upstream mist, spray on his beard; he turns his head to bark at the rowers below. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the admiral stares upstream, rain driving across the frame, then turns and barks one line down at the oar decks; the oars quicken. Sound: oars, the drum beating faster, rain, timbers creaking, one line of Korean dialogue.
ACTION_START: admiral facing upstream, hand on the railing
ACTION_END: admiral turned toward the rowers, mouth open
NARRATION_KO: 내호아는 우중문을 기다리지 않을 생각이었습니다. 평양을 먼저 밟는 자가 공을 가져갈 것이었습니다.
DIALOGUE_KO: 내호아: 노를 더 저어라. 우중문보다 먼저 간다.
SOUND: mái chèo, trống nhịp nhanh hơn, mưa, gỗ kêu.
CONTINUITY: '노를 더 저어라. 우중문보다 먼저 간다.' Landing state (grin, dao drawn) — ref CHAR_204_ref.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_204_ref, VEH_204_ref
AI_RISK: thuyền + người → máy tĩnh, 1 nhân vật, thuyền là boong

### SC_020 | 2:40–2:48 | LOC_007 (LOC_007_island1) | CHAR_004, ROK_SOLDIERS | — | PROPS: PROP_020, PROP_010 | TYPE: video8s | 8s
SHOT: Low tracking shot following the medic between the shelters
IMAGE_PROMPT: Low tracking shot following the medic between the shelters. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. @PROP_010_ref: South Korean army combat ration: square olive-brown plastic pouches, a flameless heating bag steaming, plastic spoon, compressed biscuit, instant coffee sachet; later a Goguryeo clay bowl of millet. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: Hard cut back to the reed island: soldiers lie under low roofs of bundled reeds, faces mud-smeared, rifles wrapped in cloth; the medic with the Goguryeo braid moves stooped among them handing each man a fist-sized ball of cold millet wrapped in a leaf; no smoke, no fire anywhere. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Low tracking shot behind the stooped medic: she hands a leaf-wrapped rice ball to one soldier, then the next, rain dripping through the reed roofs; she says one quiet line. Sound: rain on reeds, chewing, a very faint distant wading far off, one line of Korean dialogue.
ACTION_START: medic stooped with rice balls, first soldier reaching
ACTION_END: medic moving on to the next shelter
NARRATION_KO: 여울에서 이 킬로. 갈대 사이의 낮은 섬이었습니다. 92명은 거기 있었습니다. 연기 한 줄이면 삼십만이 돌아볼 것이었습니다.
DIALOGUE_KO: 서아: 식은 밥입니다. 다 드십시오.
SOUND: mưa trên lau, nhai, tiếng lội rất xa (cột quân vẫn qua sông).
CONTINUITY: '식은 밥입니다. 다 드십시오.' PROP_010 4화 = nắm cơm kê nguội gói lá (không bao bì). Lính phụ mặt bùn, quay đi.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, PROP_010_ref, LOC_007_island_ep4
AI_RISK: nhiều lính → thấp, out-focus, mặt khuất

### SC_021 | 2:48–2:56 | LOC_007 (LOC_007_island1_k2) | CHAR_003, ROK_SOLDIERS | VEH_001 | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The stocky sergeant in the dripping patrol cap and two soldiers scoop wet mud from wooden buckets and slap it in layers onto the tank's side skirt and turret, the mud clinging to reed bundles already stuck into it; the sergeant pats the mud flat with his palm like a man patting an ox. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium shot: handfuls of wet mud slap onto the skirt and turret, the sergeant smooths and pats it flat with his palm, says one line without looking up. Sound: wet mud slapping, palms on mud over steel, rain, one line of Korean dialogue.
ACTION_START: hands scooping mud from buckets
ACTION_END: sergeant patting the mud flat on the turret
NARRATION_KO: 진흙은 박기철의 생각이었습니다. 요동성에서 그는 기름이 타는 것을 보았습니다. 젖은 진흙은 불화살에도 타지 않았습니다.
DIALOGUE_KO: 박기철: 젖은 흙은 안 탑니다. 두 번은 안 당합니다.
SOUND: bùn nhão, tay vỗ thép qua bùn, mưa.
CONTINUITY: '젖은 흙은 안 탑니다. 두 번은 안 당합니다.' K2 phủ bùn (VEH_001_mud). 2 lính phụ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, VEH_001_ref, LOC_007_island_ep4
AI_RISK: tay + xe → 3 người, chuyển động đơn giản

### SC_022 | 2:56–3:04 | LOC_007 (LOC_007_island1_k2) | CHAR_106 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up beside the gun barrel, static
IMAGE_PROMPT: Medium close-up beside the gun barrel, static. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The old blacksmith in the leather apron stands beside the reed-wrapped gun barrel, both huge veined hands smoothing mud along the barrel's thermal sleeve as if stroking a horse's neck, left eye squinting, a one-sided grin. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the old hands stroke mud along the barrel, he squints, grins with one side of his mouth and says one line. Sound: mud, rain, a soft chuckle, one line of Korean dialogue.
ACTION_START: hands on the barrel, face neutral
ACTION_END: one-sided grin, hands resting on the mud
NARRATION_KO: 을보는 쇠를 만지고 나서야 사람을 믿는 노인이었습니다. 이제 그는 진흙까지 만졌습니다.
DIALOGUE_KO: 을보: 쇠쟁이, 이놈이 이제 진흙 소가 됐구먼.
SOUND: bùn, mưa, tiếng cười khẽ.
CONTINUITY: '쇠쟁이, 이놈이 이제 진흙 소가 됐구먼.' 을보 ướt mưa (reeds_ep4). Búa nhỏ ở thắt lưng (lock).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_ref, VEH_001_ref, LOC_007_island_ep4
AI_RISK: tay già cận → chuyển động chậm, 2 bàn tay

### SC_023 | 3:04–3:14 | LOC_007 (LOC_007_island_edge) | VILLAGE_WOMEN, ROK_SOLDIER | — | PROPS: PROP_020 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide at the island's edge, slow slide from a basket up to the old woman's face
IMAGE_PROMPT: Still for ken-burns: medium-wide at the island's edge, slow slide from a basket up to the old woman's face. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, helmet wrapped in netting stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: Five Goguryeo village women in hemp jackets and head wraps, skirts tied at the knees, carry leaf-covered baskets on shoulder poles through the flooded reed path to the island's edge; a young ROK soldier with his face turned down takes a basket with a bow of his head; far behind, the thatched roofs of a riverside village show through the reeds. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide from the basket in the soldier's hands up to the lined face of the oldest woman. Sound: water, the old woman's quiet indistinct words, rain.
ACTION_START: basket being handed over
ACTION_END: tight on the old woman's face
NARRATION_KO: 북쪽 기슭 마을의 아낙들이었습니다. 매일 저녁 찬 조밥과 삶은 나물이 왔습니다. 갈대를 베러 가는 길이라고 하면 아무도 묻지 않았습니다. 천사백 년 뒤의 군대는 이 땅의 어머니들이 먹였습니다.
DIALOGUE_KO: 마을 아낙: 갈대 베러 왔소. 늘 그렇듯.
SOUND: nước, tiếng bà cụ nói nhỏ không rõ chữ, mưa.
CONTINUITY: Still 10 s. 마을 아낙 nói '갈대 베러 왔소. 늘 그렇듯.' Cần ref EXTRA_village_women_ref.
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_village_women_ref, LOC_007_island_ep4
AI_RISK: nhiều người → still, lính quay mặt xuống

### SC_024 | 3:14–3:22 | LOC_007 (LOC_007_shelter) | CHAR_004, CHAR_106 | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium two-shot under the reed roof, static
IMAGE_PROMPT: Medium two-shot under the reed roof, static. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The medic with the Goguryeo braid and the worn red-cross armband squats before a wooden bowl, grinding a root with a stone in cold water; the old blacksmith squats opposite watching her hands; she looks up and asks him a question. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the stone grinds the root in the water, the old man watches the hands, she looks up and asks one line. Sound: stone grinding, water, rain, one line of Korean dialogue.
ACTION_START: medic grinding, old man watching
ACTION_END: medic looking up at the old man
NARRATION_KO: 불이 없으니 약도 찬물로 우렸습니다. 서아는 그것이 약이 되는지 몰랐습니다. 물어볼 사람은 이 노인뿐이었습니다.
DIALOGUE_KO: 서아: 불 없이 달인 약도 약이 됩니까?
SOUND: đá giã, nước, mưa.
CONTINUITY: '불 없이 달인 약도 약이 됩니까?' Túi y tế PROP_009 cạnh.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, CHAR_106_ref, PROP_009_ref, LOC_007_island_ep4

### SC_025 | 3:22–3:30 | LOC_007 (LOC_007_shelter) | CHAR_106, CHAR_004 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot under the reed roof, static (same setup)
IMAGE_PROMPT: Medium two-shot under the reed roof, static (same setup). @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The old blacksmith dips a finger into the wooden bowl, tastes, grimaces, then pushes the bowl back across the mud toward the medic with a grunted verdict. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: finger into the bowl, taste, grimace, the bowl pushed back across the mud, one gruff line. Sound: rain, the wooden bowl sliding, one line of Korean dialogue.
ACTION_START: finger dipping into the bowl
ACTION_END: bowl pushed back to the medic
NARRATION_KO: 항생제는 요동성에서 끝났습니다. 남은 것은 이 노인의 풀뿐이었습니다. 서아는 풀 이름을 약 이름처럼 외웠습니다.
DIALOGUE_KO: 을보: 찬 약은 반 약이지. 없는 것보단 낫고.
SOUND: mưa, bát gỗ trượt.
CONTINUITY: '찬 약은 반 약이지. 없는 것보단 낫고.' Nối SC_024.
CHAIN_FROM: SC_024
CUT_HALF: no
REFS: CHAR_106_ref, CHAR_004_braid_ep4, LOC_007_island_ep4

### SC_026 | 3:30–3:38 | LOC_007 (LOC_007_reed_path) | CHAR_107, VILLAGE_WOMEN | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Tracking shot from behind along the flooded reed path
IMAGE_PROMPT: Tracking shot from behind along the flooded reed path. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: Grey dawn: the girl, braids hidden under a hemp head cloth, a sickle in her hand and a basket on her back, wades thigh-deep along the reed path in the middle of five village women heading toward the river; the women chat as on any morning, the girl silent. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking from behind: the group wades away along the reed path, water to their thighs, sickles knocking baskets, the women talking; one woman says a line to the girl, who lowers her head. Sound: water, sickles on baskets, women's voices, one line of Korean dialogue.
ACTION_START: group entering the reed path
ACTION_END: group deeper in the reeds, girl's head lowered
NARRATION_KO: 다음 날 새벽부터 아리는 아낙들과 나갔습니다. 아리의 어머니는 이 강가 마을 사람이었습니다. 아리는 갈대가 어디까지 이어지는지 알았습니다.
DIALOGUE_KO: 마을 아낙: 아가, 고개 숙이고 걸어라.
SOUND: nước tới đùi, liềm chạm rổ, tiếng các bà.
CONTINUITY: D2 rạng sáng. 아리 reedcutter_ep4 (khăn olive giấu trong váy). '아가, 고개 숙이고 걸어라.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, EXTRA_village_women_ref, LOC_007_detail
AI_RISK: 6 người → từ sau lưng

### SC_027 | 3:38–3:46 | LOC_007 (LOC_007_island_edge) | CHAR_006, CHAR_001 | — | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Medium close-up at ground level on two prone men, static
IMAGE_PROMPT: Medium close-up at ground level on two prone men, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The scout in the soaked boonie hat lies at the island's edge with binoculars following the shrinking figures of the women in the reeds; he lowers the binoculars and speaks without turning; the captain lies beside him, helmet off, hair matted. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the binoculars track slowly, lower, the scout speaks one line without turning his head; the captain beside him does not answer. Sound: rain, binoculars tapping wet fabric, one line of Korean dialogue.
ACTION_START: binoculars up, tracking
ACTION_END: binoculars lowered, line delivered
NARRATION_KO: 백성민은 아리를 내보낸 것이 누구의 생각인지 묻지 않았습니다. 아리 자신의 생각이었습니다. 열다섯 살의 생각이었습니다.
DIALOGUE_KO: 백성민: 저 아이는 갈대를 베러 가는 게 아닙니다.
SOUND: mưa, ống nhòm chạm áo.
CONTINUITY: '저 아이는 갈대를 베러 가는 게 아닙니다.' 백성민 reeds_ep4 (mũ boonie, không sơn mặt).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_ref, CHAR_001_reeds_ep4, PROP_006_ref, LOC_007_island_ep4

### SC_028 | 3:46–3:56 | LOC_007 (LOC_007_sandbar_mid) | CHAR_107, VILLAGE_WOMEN, SUI_SENTRY | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide from the sandbar, slow pull from a sickle to the camp
IMAGE_PROMPT: Still for ken-burns: wide from the sandbar, slow pull from a sickle to the camp. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. a Sui sentry in a wet grey-blue padded coat and pointed iron helmet, spear leaning beside him, face half hidden, dozing. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_007_south_camp_ep4: A wet grey-brown sandbar in the shallow river with tall reeds growing along its edge, and across a narrow channel of brown water the south bank: a Sui rear-guard camp of grey felt and dark hide tents, two-wheeled ox carts loaded with chests, tethered horses, a large willow tree, red and yellow banners hanging wet, steady rain, low green hills behind. Action: In the foreground the village women and the girl bend to cut reeds on the sandbar; across a narrow channel of brown water on the south bank the Sui rear-guard camp: rows of hide tents, ox carts loaded with chests, tethered horses; a sentry leaning on his spear glances at the women and looks away. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull from the sickle cutting reeds in the foreground out to the camp across the channel. Sound: sickles cutting reeds, distant camp noise, an ox lowing.
ACTION_START: tight on the sickle
ACTION_END: wide on the camp across the channel
NARRATION_KO: 삼십만이 남쪽으로 갔습니다. 그러나 다 간 것은 아니었습니다. 우중문은 여울에 오천을 남겼습니다. 수레와 남은 짐을 지키는 후군이었습니다. 돌아올 길이었기 때문입니다. 그 후군을 탁발흠이 맡았습니다.
DIALOGUE_KO: 
SOUND: liềm cắt lau, tiếng trại xa, bò rống.
CONTINUITY: Still 10 s. Trại hậu quân 5천 (ref LOC_007_south_camp_ep4).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, EXTRA_village_women_ref, WPN_201_ref, PROP_021_ref, LOC_007_south_camp_ep4
AI_RISK: trại + người → still wide

### SC_029 | 3:56–4:04 | LOC_007 (LOC_007_sandbar_mid) | CHAR_107 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Close-up on the girl cutting reeds, static, shallow focus
IMAGE_PROMPT: Close-up on the girl cutting reeds, static, shallow focus. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_south_camp_ep4: A wet grey-brown sandbar in the shallow river with tall reeds growing along its edge, and across a narrow channel of brown water the south bank: a Sui rear-guard camp of grey felt and dark hide tents, two-wheeled ox carts loaded with chests, tethered horses, a large willow tree, red and yellow banners hanging wet, steady rain, low green hills behind. Action: The girl cuts reeds with the sickle without raising her head, only her eyes lifting under her brows: beyond her, out of focus, the sentry, the horse lines, and under a willow inside the camp a square shape covered with wet cloth; she bends and cuts again, her hands trembling. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the sickle cuts, the eyes lift under the brows and hold on the blurred shape under the willow, then drop; she cuts again, hands trembling. Sound: sickle, rain, camp noise far off.
ACTION_START: eyes down, sickle cutting
ACTION_END: eyes down again, hands trembling on the sickle
NARRATION_KO: 아리는 얼굴을 들지 않았습니다. 눈만 들었습니다. 그것도 어머니에게 배운 것이었습니다.
DIALOGUE_KO: 
SOUND: liềm, mưa, tiếng trại.
CONTINUITY: Khối phủ vải = cũi (chưa rõ). Nền out-focus.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, LOC_007_south_camp_ep4
AI_RISK: liềm + tay → chuyển động cắt đơn giản

### SC_030 | 4:04–4:12 | LOC_007 (LOC_007_south_shore) | CHAR_205 | EQP_001, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot walking along the camp's edge, slow push-in to the eyes
IMAGE_PROMPT: Medium shot walking along the camp's edge, slow push-in to the eyes. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. A modern night-vision monocular device mounted on the front of the fox-fur cap, an empty black rifle magazine hanging from the belt, rain-darkened leather armor, mud on boots. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_007_south_camp_ep4: The sandy south shore of the shallow river in front of the Sui rear-guard camp, July monsoon: wet grey sand at the water's edge, the wide grey river and the dark reed beds of the north bank beyond, grey felt tents and ox carts behind, rain. Action: The Xianbei commander with the long scar walks along the sandy edge of the camp, the night-vision device flipped up on the front of his fox-fur cap in daylight, wet leather cloak; his glance slides over the reed-cutting women for less than a beat, then his eyes fix far across the river on the reed beds of the north bank and stay there. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in as he walks: the glance flicks over the women and away, the eyes lock on the far reed beds and hold; he says one short line to someone off frame. Sound: camp noise, rain, horses, one line of Korean dialogue.
ACTION_START: walking, glance on the women
ACTION_END: stopped, eyes fixed on the far reed beds
NARRATION_KO: 탁발흠은 아낙들을 보지 않았습니다. 아낙들 너머를 보았습니다. 그의 눈은 며칠째 저 갈대밭에 가 있었습니다. 저 안 어딘가에 천둥이 있었습니다.
DIALOGUE_KO: 탁발흠: 아낙들은 두어라.
SOUND: trại, mưa, ngựa.
CONTINUITY: '아낙들은 두어라.' Kính đêm lật lên trên mũ ban ngày (nvg_ep3 ✔). Tay chưa bị chém.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, EQP_001_ref, VEH_206_ref, LOC_007_south_camp_ep4

### SC_031 | 4:12–4:20 | LOC_007 (LOC_007_island1) | CHAR_107, CHAR_004 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: Evening: the girl reaches the island and drops a heavy bundle of cut reeds from her back, both hands scratched and bleeding; the medic hurries to catch her arm; the girl sinks into a squat, breathing hard, saying nothing yet. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the bundle thuds down, the medic steadies her, the girl sinks to a squat, chest heaving, mouth closed. Sound: reeds thudding, gasping breath, rain.
ACTION_START: girl dropping the bundle
ACTION_END: girl squatting, medic holding her arm
NARRATION_KO: 저녁마다 아리는 갈대 한 짐과 함께 돌아왔습니다. 갈대는 핑계였습니다. 진짜 짐은 눈 안에 있었습니다.
DIALOGUE_KO: 
SOUND: bó lau đổ, thở, mưa.
CONTINUITY: Chiều D2. Tay 아리 xước máu.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_004_braid_ep4, LOC_007_island_ep4

### SC_032 | 4:20–4:30 | LOC_007 (LOC_007_island1) | CHAR_107 | — | PROPS: PROP_020 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up, slow push-in to the eyes
IMAGE_PROMPT: Still for ken-burns: close-up, slow push-in to the eyes. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The girl sits beside the reed bundle, a corner of the olive scarf showing at her waist, scratched hands resting on her knees, eyes fixed toward the river. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in from the hands on the knees to the eyes. Sound: rain, reeds rubbing.
ACTION_START: girl seated, hands on knees
ACTION_END: tight on the eyes
NARRATION_KO: 아리는 매일 아침 갈대를 베러 나갔습니다. 그리고 매일 저녁, 적의 진영을 보고 돌아왔습니다.
DIALOGUE_KO: 
SOUND: mưa, lau cọ.
CONTINUITY: Still 10 s. Kết P2.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, LOC_007_island_ep4


## [Phần 3] 재고 조사 — 「우린 이제 장님입니다」 (4:30–7:00) · sổ 박기철 · lính Tùy lạc hàng · cọc nước · cũi · MID-ROLL 1 @7:00

### SC_033 | 4:30–4:40 | LOC_007 (LOC_007_shelter) | CHAR_003 | — | PROPS: PROP_001 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: extreme close-up on a notebook page, slow slide down a column of pencil figures
IMAGE_PROMPT: Still for ken-burns: extreme close-up on a notebook page, slow slide down a column of pencil figures. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: A page of a small green field notebook with rain-swollen edges held on a knee, a pencil resting on it: a column of blurred pencil lines and figures, one raindrop spreading the last figure into a grey smudge; no readable characters. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide from the top of the pencil column down to the smudged last line. Sound: rain on reeds, a pencil.
ACTION_START: top of the notebook page
ACTION_END: bottom of the column, raindrop smudge
NARRATION_KO: 이틀째 저녁. 박기철은 같은 숫자를 다시 셌습니다. 숫자는 세지 않으면 줄어도 모르는 법이었습니다. 이 수첩은 이 부대의 은행이었습니다. 은행에 들어오는 돈은 없었습니다.
DIALOGUE_KO: 
SOUND: mưa trên lau, bút chì.
CONTINUITY: Still 10 s. Số thật OVERLAY ở edit: 92 · 8 · 20km · 50 · 9 · 10 (30%) · 50% · 0. Ảnh chỉ 'blurred pencil'.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, PROP_001_ref, LOC_007_island_ep4
OVERLAY (edit): 92 · 8 · 20km · 50 · 9 · 10 (30%) · 50% · 0 (cột số sổ 박기철, giọt mưa nhòe số 0)
AI_RISK: chữ trong ảnh → blurred pencil lines, không ký tự; số OVERLAY

### SC_034 | 4:40–4:48 | LOC_007 (LOC_007_shelter) | CHAR_003, CHAR_001 | — | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Two-shot under the reed roof, static, both faces in frame
IMAGE_PROMPT: Two-shot under the reed roof, static, both faces in frame. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The stocky sergeant reads from the small notebook in a low voice, each figure spoken once and then repeated with his lips only; the captain sits opposite, helmet off, listening without interrupting. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the sergeant reads one line in a low voice, lips repeating silently after; the captain listens without moving. Sound: rain, wet paper, one line of Korean dialogue.
ACTION_START: sergeant looking at the notebook
ACTION_END: sergeant's lips repeating silently, captain still
NARRATION_KO: 박기철은 숫자를 두 번 말하는 사람이었습니다. 이 섬에서는 한 번만 말했습니다. 소리가 아까웠습니다.
DIALOGUE_KO: 박기철: 아흔두 명. 포탄 여덟 발. 연료 이십 킬로.
SOUND: mưa, giấy ướt.
CONTINUITY: '아흔두 명. 포탄 여덟 발. 연료 이십 킬로.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, CHAR_001_reeds_ep4, PROP_001_ref, LOC_007_island_ep4

### SC_035 | 4:48–4:56 | LOC_007 (LOC_007_island1) | ROK_SOLDIER | WPN_002, WPN_005, EQP_001 | PROPS: PROP_008 | TYPE: video8s | 8s
SHOT: Insert: close-up, slow pan across the stacked equipment
IMAGE_PROMPT: Insert: close-up, slow pan across the stacked equipment. a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, helmet wrapped in netting stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. @WPN_005_ref: Panzerfaust 3 shoulder-fired anti-tank launcher, long dark olive tube with a large black conical warhead protruding from the front, detachable sight and trigger unit on the left side, shoulder rest. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @PROP_008_ref: olive-green steel ammunition cans with hinged latched lids and carry handles, a wooden crate of 81mm mortar bombs in green plastic tubes, and a single one-meter 120mm tank round with a copper-brown semi-combustible case and black projectile. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: A soldier's hand lifts the lid of a wet mortar-bomb crate and counts the finned bombs with a finger; beside it nine anti-tank launcher tubes stacked under a poncho; a bag of small batteries and ten night-vision monoculars rolled in oilcloth. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow pan across: the lid lifts, a finger counts bombs, the pan continues over the nine launcher tubes to the batteries and the rolled night-vision devices. Sound: crate lid, batteries clicking, rain.
ACTION_START: hand on the crate lid
ACTION_END: pan resting on the rolled night-vision devices
NARRATION_KO: 연료 이십 킬로는 산길 기준이었습니다. 평지라면 조금 더 갔습니다. 박기철은 늘 적은 쪽으로 셌습니다. 많은 쪽으로 세다가 죽는 사람을 그는 알았습니다.
DIALOGUE_KO: 
SOUND: nắp hòm, pin lách cách, mưa.
CONTINUITY: 9 ống PZF, 10 kính đêm, hòm đạn cối (PROP_008). Không mặt.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_002_ref, WPN_005_ref, EQP_001_ref, PROP_008_ref, LOC_007_island_ep4
AI_RISK: nhiều vật thể nhỏ → pan chậm, không chữ

### SC_036 | 4:56–5:04 | LOC_007 (LOC_007_shelter) | CHAR_003 | — | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Close-up on the sergeant and the notebook, static
IMAGE_PROMPT: Close-up on the sergeant and the notebook, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The sergeant continues, his finger tracing line by line down the notebook page, rain dripping from the reed roof onto his shoulder. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the finger moves down the page, drops fall on his shoulder, he reads one line. Sound: rain, paper, one line of Korean dialogue.
ACTION_START: finger at the top of the page
ACTION_END: finger lower on the page
NARRATION_KO: 포탄 여덟에 박격포 오십. 요동성의 절반도 안 되는 숫자였습니다. 그것으로 삼십만을 상대해야 했습니다.
DIALOGUE_KO: 박기철: 박격포 오십. PZF 아홉. 야시경 열 개, 배터리 삼십.
SOUND: mưa, giấy.
CONTINUITY: '박격포 오십. PZF 아홉. 야시경 열 개, 배터리 삼십.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, PROP_001_ref, LOC_007_island_ep4

### SC_037 | 5:04–5:12 | LOC_007 (LOC_007_shelter) | CHAR_003 | EQP_002 | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Close-up on the hand, pencil and radio, static
IMAGE_PROMPT: Close-up on the hand, pencil and radio, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The sergeant taps his pencil on the olive backpack radio set beside him, its small panel dark; he reads; then the pencil stops at the last line of the notebook and he does not read on. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the pencil taps the radio twice, he reads one line, the pencil stops on the last line and stays. Sound: pencil on plastic, rain, one line of Korean dialogue that trails off.
ACTION_START: pencil tapping the radio
ACTION_END: pencil frozen on the last line
NARRATION_KO: 무전기는 전차에서 충전했습니다. 전차는 기름으로 충전했습니다. 모든 숫자는 결국 한 숫자로 이어졌습니다. 이십 킬로.
DIALOGUE_KO: 박기철: 무전기 오십 퍼센트. 드론…
SOUND: bút gõ nhựa, mưa.
CONTINUITY: '무전기 오십 퍼센트. 드론…' Màn hình radio tối (không chữ).
CHAIN_FROM: SC_036
CUT_HALF: no
REFS: CHAR_003_rain_ep3, EQP_002_ref, PROP_001_ref, LOC_007_island_ep4

### SC_038 | 5:12–5:20 | LOC_007 (LOC_007_island1_k2) | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the sergeant's eyes, slow pan to an empty patch of mud beside the tank
IMAGE_PROMPT: Close-up on the sergeant's eyes, slow pan to an empty patch of mud beside the tank. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The sergeant lifts his head and looks at a bare patch of mud beside the tank's mud-caked skirt — where a drone case and a tarp always used to sit; now only mud and a shallow rectangular dent. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow pan from the sergeant's eyes to the empty patch of mud with its rectangular dent; he says one line, the last words almost inaudible. Sound: rain, silence, one line of Korean dialogue.
ACTION_START: sergeant's eyes lifting
ACTION_END: empty mud with the dent
NARRATION_KO: 그 자리에는 늘 소년이 앉아 있었습니다. 하늘의 눈을 무릎에 놓고. 이제 자리만 남았습니다.
DIALOGUE_KO: 박기철: 드론, 영. …우린 이제 장님입니다.
SOUND: mưa, im.
CONTINUITY: '드론, 영. …우린 이제 장님입니다.' Chỗ trống của 태오.
CHAIN_FROM: SC_037
CUT_HALF: no
REFS: CHAR_003_rain_ep3, VEH_001_ref, LOC_007_island_ep4

### SC_039 | 5:20–5:28 | LOC_007 (LOC_007_island_edge) | CHAR_006, SUI_STRAGGLERS, ROK_SOLDIER | WPN_201 | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Static, shallow focus from the eye level of a soldier lying in the reeds
IMAGE_PROMPT: Static, shallow focus from the eye level of a soldier lying in the reeds. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. two Sui stragglers in wet grey-blue padded coats and pointed iron helmets, spears carried reversed, faces turned away. a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, helmet wrapped in netting stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The scout lies prone at the island's edge with binoculars and a hand tally counter; three meters away two Sui stragglers with spears carried reversed wade into the reed edge, snapping dry reeds for firewood and muttering; a ROK soldier lies directly beneath their feet, only his eyes moving. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static shallow-focus shot: the two stragglers snap reeds and mutter, a boot sinks into the mud a hand from the prone soldier's face, the eyes move, nothing else; the counter in the scout's hand stops clicking. Sound: reeds snapping, muttering, the counter stops, rain.
ACTION_START: stragglers wading in, counter clicking
ACTION_END: stragglers gathering reeds, counter silent
NARRATION_KO: 낙오병 둘이 마른 갈대를 꺾으러 들어왔습니다. 세 걸음 안에 총이 셋 있었습니다. 아무도 쏘지 않았습니다. 백성민의 손가락도 세는 것을 멈췄습니다.
DIALOGUE_KO: 
SOUND: lau gãy, tiếng Tùy lầm bầm, máy đếm ngừng.
CONTINUITY: Mini-contact. Lính Tùy quay đi, không mặt. Máy đếm tay (không chữ).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, WPN_201_ref, PROP_006_ref, LOC_007_island_ep4
AI_RISK: địch sát nhân vật → tiêu cự nông, địch out-focus

### SC_040 | 5:28–5:36 | LOC_007 (LOC_007_island_edge) | CHAR_006, CHAR_001, SUI_STRAGGLERS | — | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Medium shot at ground level, static
IMAGE_PROMPT: Medium shot at ground level, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. two Sui stragglers in wet grey-blue padded coats and pointed iron helmets, spears carried reversed, faces turned away. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The two stragglers wade away with armfuls of dry reeds; the scout crawls backward through the mud to the captain and holds out the hand tally counter, its four-digit wheels having rolled over many times; his voice flat. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the stragglers recede, the scout crawls back and holds the counter out to the captain, says one flat line. Sound: crawling through mud, the counter, rain, one line of Korean dialogue.
ACTION_START: stragglers leaving, scout starting to crawl
ACTION_END: counter held out to the captain
NARRATION_KO: 사람을 세는 기계는 만에서 다시 영으로 돌아갔습니다. 백성민은 몇 번 돌렸는지 종이에 적었습니다. 젖은 종이에서 숫자가 번졌습니다.
DIALOGUE_KO: 백성민: 하루 종일 셌습니다. 끝이 없습니다.
SOUND: bò trên bùn, máy đếm, mưa.
CONTINUITY: '하루 종일 셌습니다. 끝이 없습니다.' Máy đếm: không cận số (né chữ).
CHAIN_FROM: SC_039
CUT_HALF: yes
REFS: CHAR_006_ref, CHAR_001_reeds_ep4, WPN_201_ref, PROP_006_ref, LOC_007_island_ep4
AI_RISK: số trên máy đếm → không cận mặt số

### SC_041 | 5:36–5:46 | LOC_007 (LOC_007_south_camp) | OXEN_CARTS | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial over the south bank, slow pull from the carts to the whole shore  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial over the south bank, slow pull from the carts to the whole shore. two-wheeled wooden ox carts loaded with rope-bound chests, oxen under wooden yokes. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_007_south_camp_ep4: The Sui rear-guard camp on the south bank of the shallow river, July monsoon: rows of grey felt and dark hide tents, two-wheeled ox carts loaded with chests, oxen and tethered horses, cooking fires smoking under hide awnings, a large willow tree dripping rain, red and yellow banners hanging wet, the sandy shore and the grey river beyond, low green hills behind. Action: From above: the tail of the great column — ox carts loaded with chests, pack horses, soldiers in padded coats — has stopped on the south bank just past the ford, hide tents going up in a ring around the carts; far south the main column has vanished; across the water the reed beds of the north bank lie still. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out from the ring of carts to the whole south shore and the still reed beds across the water. Sound: oxen, cart timbers, the drums stopping.
ACTION_START: tight on the carts and tents
ACTION_END: wide on shore, river and reed beds
NARRATION_KO: 꼬리는 남쪽으로 가지 않았습니다. 여울 남쪽 기슭에 멈춰 진을 쳤습니다. 후군 오천과 수레였습니다. 그 수레 사이 어딘가에 대나무 우리가 하나 있었습니다. 아직 아무도 그것을 보지 못했습니다.
DIALOGUE_KO: 
SOUND: bò, gỗ xe, trống ngừng.
CONTINUITY: Still 10 s. Hậu quân 5천 dựng trại. Cũi chưa thấy.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_007_south_camp_ep4
AI_RISK: trại + đoàn xe → aerial

### SC_042 | 5:46–5:54 | LOC_007 (LOC_007_stake) | CHAR_003 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle at water level, static
IMAGE_PROMPT: Low angle at water level, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The sergeant wades knee-deep at the island's edge and drives a wooden stake carved with horizontal notches into the sandy bottom, pressing it firm; the brown water touches the second notch from the bottom; he looks at the stake, then up at the sky. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static at water level: the stake is pushed down and pressed firm, water lapping the second notch; he studies it, then lifts his face to the rain. Sound: stake into sand, running water, rain.
ACTION_START: stake in hand above the water
ACTION_END: stake planted, sergeant looking up
NARRATION_KO: 하늘의 눈이 없으니 강이 시계가 되었습니다. 박기철은 이번에는 눈금을 새긴 막대를 꽂았습니다. 기름과 탄약처럼, 물도 셀 수 있었습니다.
DIALOGUE_KO: 
SOUND: cọc cắm cát, nước chảy, mưa.
CONTINUITY: Cọc vạch: nước ở vạch 2 (D2). 3화 dùng cành cây → 'lần này' cọc khắc.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, LOC_007_detail

### SC_043 | 5:54–6:02 | LOC_007 (LOC_007_shelter) | CHAR_003, CHAR_001 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot under the reed roof, static
IMAGE_PROMPT: Medium two-shot under the reed roof, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The sergeant sits back under the reed roof wringing water from his trouser leg and speaks to the captain, who is wiping down a cloth-wrapped rifle; the sergeant holds up one spread hand as a measure. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: trouser leg wrung out, one line spoken, the spread hand held up as a measure; the captain's wiping hand pauses. Sound: cloth wrung, rain, one line of Korean dialogue.
ACTION_START: sergeant wringing his trouser leg
ACTION_END: spread hand held up, captain paused
NARRATION_KO: 한 뼘. 어른 손으로 한 뼘이었습니다. 박기철은 그것을 수첩에 물이라는 항목으로 적었습니다. 기름 밑에, 탄약 밑에.
DIALOGUE_KO: 박기철: 하루에 한 뼘씩 오릅니다.
SOUND: vắt vải, mưa.
CONTINUITY: '하루에 한 뼘씩 오릅니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, CHAR_001_reeds_ep4, WPN_001_ref, LOC_007_island_ep4

### SC_044 | 6:02–6:10 | LOC_007 (LOC_007_stake) | CHAR_106 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up at the water's edge, static
IMAGE_PROMPT: Medium close-up at the water's edge, static. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The old blacksmith squats beside the notched stake, one whole hand thrust into the running brown water feeling the current, left eye squinting upstream where black cloud presses down on the hills; he speaks without turning. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the hand in the current, the squint upstream at the black cloud, one line spoken without turning. Sound: water over the hand, very distant thunder, one line of Korean dialogue.
ACTION_START: hand entering the water
ACTION_END: hand in the current, eyes upstream
NARRATION_KO: 을보는 강가 사람이 아니었습니다. 그러나 대장장이는 물을 알았습니다. 쇠를 식히는 물이었습니다.
DIALOGUE_KO: 을보: 이 강은 한 번 화나면 사흘 만에 어른 키를 넘소.
SOUND: nước qua tay, sấm rất xa.
CONTINUITY: '이 강은 한 번 화나면 사흘 만에 어른 키를 넘소.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_ref, LOC_007_detail

### SC_045 | 6:10–6:18 | LOC_007 (LOC_007_stake) | CHAR_001 | — | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium shot from behind and beside the captain, slow push-in
IMAGE_PROMPT: Medium shot from behind and beside the captain, slow push-in. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The captain stands behind looking at the stake — water at the second notch — then lifts his eyes to the black cloud upstream; his right hand rises by habit to his chest pocket where the bamboo shaft of a Goguryeo arrow shows above the flap. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow push-in: eyes from the stake to the cloud, the hand rising to touch the arrow shaft at the chest pocket, one line spoken. Sound: rain thickening, distant thunder, one line of Korean dialogue.
ACTION_START: captain looking at the stake
ACTION_END: hand on the chest pocket, eyes on the cloud
NARRATION_KO: 물이 오르면 여울은 사라집니다. 그러면 삼십만은 돌아갈 길이 없어집니다. 한승우는 그 셈을 하지 않았습니다. 을지문덕은 이미 했습니다.
DIALOGUE_KO: 한승우: 하루에 한 뼘. 적어 둬.
SOUND: mưa dày hơn, sấm xa.
CONTINUITY: '하루에 한 뼘. 적어 둬.' Mũi tên túi ngực = PROP_015 (từ 1화).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, PROP_015_ref, LOC_007_detail

### SC_046 | 6:18–6:26 | LOC_007 (LOC_007_island1) | CHAR_107, CHAR_004 | — | PROPS: PROP_020, PROP_009 | TYPE: video8s | 8s
SHOT: Tracking shot following the two
IMAGE_PROMPT: Tracking shot following the two. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: Grey dusk: the girl returns with a reed bundle, face bloodless, and instead of dropping it in the usual place walks straight to the medic who is rolling a bandage, grips her sleeve and pulls her behind a clump of reeds. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking: the girl crosses the island with the bundle, seizes the medic's sleeve, pulls her behind the reeds; the bandage roll drops. Sound: reeds, rain, quick breathing.
ACTION_START: girl entering with the bundle
ACTION_END: both disappearing behind the reeds
NARRATION_KO: 그날 저녁 아리는 갈대를 내려놓지 않았습니다. 먼저 사람을 찾았습니다.
DIALOGUE_KO: 
SOUND: lau, mưa, thở gấp.
CONTINUITY: Hoàng hôn D2. Mặt 아리 trắng bệch.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_004_braid_ep4, PROP_009_ref, LOC_007_island_ep4

### SC_047 | 6:26–6:34 | LOC_007 (LOC_007_island1) | CHAR_107, CHAR_004 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close two-shot behind the reeds, static
IMAGE_PROMPT: Close two-shot behind the reeds, static. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The two sit pressed together behind the reeds; the girl whispers right into the medic's ear, eyes wide; the medic listens, her bandage-rolling hands going still. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close two-shot: the whisper at the ear, the wide eyes, the medic's hands stopping on the bandage; one whispered line. Sound: whisper, rain, one line of Korean dialogue.
ACTION_START: girl leaning in to whisper
ACTION_END: medic's hands still, girl's eyes wide
NARRATION_KO: 우리. 아리는 그 말을 먼저 했습니다. 안에 든 것은 그다음이었습니다.
DIALOGUE_KO: 아리: 언니, 강 건너에 우리가 있어요. 대나무 우리요.
SOUND: thì thầm, mưa.
CONTINUITY: '언니, 강 건너에 우리가 있어요. 대나무 우리요.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_004_braid_ep4, LOC_007_island_ep4

### SC_048 | 6:34–6:42 | LOC_007 (LOC_007_island1) | CHAR_107, CHAR_004 | — | PROPS: PROP_011 | TYPE: video8s | 8s
SHOT: Close two-shot behind the reeds, static (same setup)
IMAGE_PROMPT: Close two-shot behind the reeds, static (same setup). @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. @PROP_011_ref: small full-color embroidered South Korean Taegukgi flag patch, red and blue taeguk circle with four black trigrams on white, about seven by four centimeters, on the right upper sleeve of a digital-camouflage uniform. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The medic grips the girl's arm; the girl pulls up her own sleeve and points at the digital camouflage pattern on the medic's shoulder, then speaks; tears stand in her eyes without falling. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the grip on the arm, the girl's finger touching the camouflage on the shoulder, one whispered line, tears standing unshed. Sound: whisper, rain, one line of Korean dialogue.
ACTION_START: medic gripping the girl's arm
ACTION_END: girl's finger on the camouflage sleeve, tears standing
NARRATION_KO: 
DIALOGUE_KO: 아리: 그 안에 오라버니 같은 사람이… 같은 옷이에요.
SOUND: thì thầm, mưa.
CONTINUITY: '그 안에 오라버니 같은 사람이… 같은 옷이에요.' Chỉ vào hoa văn rằn ri (patch 태극기 vai phải theo lock).
CHAIN_FROM: SC_047
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_004_braid_ep4, PROP_011_ref, LOC_007_island_ep4

### SC_049 | 6:42–6:50 | LOC_007 (LOC_007_island1) | CHAR_004, CHAR_001, ROK_SOLDIERS | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, camera following her eyeline across the island
IMAGE_PROMPT: Medium shot, camera following her eyeline across the island. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The medic stands up from behind the reeds and turns, searching over the heads of the lying soldiers; camera follows her eyeline to the far end of the island where the captain, beside the water stake, lifts his head at that exact moment; no words. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera follows the medic's turn and eyeline across the prone soldiers to the captain at the far end lifting his head; the two hold each other's look. Sound: rain, reeds, no dialogue.
ACTION_START: medic standing up behind the reeds
ACTION_END: captain at the far end, head lifted, looking back
NARRATION_KO: 서아는 곧바로 말하러 가지 않았습니다. 먼저 얼굴을 보았습니다. 말보다 얼굴이 먼저 건너갔습니다.
DIALOGUE_KO: 
SOUND: mưa, lau.
CONTINUITY: Không thoại. 한승우 ở đầu kia đảo (nhỏ trong khung) — header script chỉ ghi CHAR_004, veo thêm lock CHAR_001 để không drift.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, CHAR_001_reeds_ep4, LOC_007_island_ep4
AI_RISK: nhiều lính nền → nằm, out-focus

### SC_050 | 6:50–7:00 | LOC_007 (LOC_007_stake) | CHAR_001 | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up, very slow push-in to the eyes
IMAGE_PROMPT: Still for ken-burns: close-up, very slow push-in to the eyes. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The captain's mud-smeared face in the rain, eyes directed at someone off frame — already understanding what has not been said; behind him the notched stake and the grey river. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow push-in to the eyes. Sound: rain, the river.
ACTION_START: face with stake and river behind
ACTION_END: tight on the eyes
NARRATION_KO: 강 건너 우리 안에 앉은 소년은 그들과 같은 옷을 입고 있었습니다.
DIALOGUE_KO: 
SOUND: mưa, sông.
CONTINUITY: Still 10 s. Kết P3 → MID-ROLL 1 @7:00.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, LOC_007_detail


## [Phần 4] 첫 접촉 — 「밤눈을 가진 자」 (7:00–10:30) · [史] 내호아 đổ bộ, 고건무 bỏ trống 나곽 · đêm D2 đánh dao trong lau

### SC_051 | 7:00–7:08 | LOC_007 (LOC_007_cage) | CHAR_005 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the bamboo cage, very slow push-in to a torn patch of cloth
IMAGE_PROMPT: Close-up on the bamboo cage, very slow push-in to a torn patch of cloth. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. Setting @LOC_007_south_camp_ep4: Under a dripping willow tree at the edge of the Sui rear-guard camp on the south bank: a man-sized cage of bamboo poles lashed with leather thongs under a sagging wet cloth roof, wet sand and mud, grey felt tents and ox carts behind, steady rain. Action: A bamboo cage under a dripping willow in rain: poles lashed with leather thongs, a sagging wet cloth roof; inside, a huddled figure with his back turned in a torn camouflage uniform, hair hacked short, and on his right shoulder a ragged bare patch where a flag patch has been torn away; no face. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Very slow push-in on the cage through the rain to the torn bare patch on the right shoulder; the figure does not move; no dialogue, no narration. Sound: rain on the cloth roof, leather thongs creaking, the camp far off.
ACTION_START: cage in the rain, figure's back
ACTION_END: tight on the torn patch on the shoulder
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: mưa trên vải, dây da kêu, trại xa.
CONTINUITY: Sau mid-roll 1: không thoại. 태오 quay lưng (cage_ep4). Mảng vải xé = chỗ 태극기 vai PHẢI.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_captive_ep3, LOC_007_south_camp_ep4
AI_RISK: nhân vật quay lưng → không mặt (né drift)

### SC_052 | 7:08–7:18 | LOC_006 | — | VEH_204 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial in rain, slow pull from the ships up to the fortress  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial in rain, slow pull from the ships up to the fortress. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_006_wide: Goguryeo capital fortress on low hills above a wide grey-green river in monsoon rain: long dry-stacked grey granite walls with bastions, tiled timber gate towers, an outer town of empty wooden houses with rain-dark tiled and thatched roofs, an empty wooden Buddhist temple with a five-story stone pagoda, palace halls with red pillars on the hill, black three-legged crow banners. Action: From above in rain: the Goguryeo capital on low hills with long grey granite walls and dark tiled gate towers; below it the wide grey-green river five hundred meters across, dozens of tower warships pressed against the north-bank beach, flat-bottomed boats unloading soldiers onto the sand, red banners. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull from the landing boats on the beach up to the walls and gate towers on the hill. Sound: oars, naval drums, rain.
ACTION_START: tight on the beach and ships
ACTION_END: wide on the fortress above the river
NARRATION_KO: 612년 7월. 패수. 내호아의 배가 평양성 아래 닿았습니다. 성벽 위에서는 삼족오가 비에 젖은 채 내려다보았습니다.
DIALOGUE_KO: 
SOUND: mái chèo, trống thủy quân, mưa.
CONTINUITY: Still 10 s. LOC_006 lock gốc (bible). Track (a) D2.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_204_ref, PROP_021_ref, LOC_006_wide
AI_RISK: hạm đội + thành → aerial

### SC_053 | 7:18–7:26 | LOC_006 (LOC_006_landing) | SUI_MARINES, GOG_ARCHERS, SUI_OFFICER | VEH_204, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide shot on the beach, static, no close-ups of casualties  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide shot on the beach, static, no close-ups of casualties. Sui marines in wet black lacquered leather lamellar armor with iron chest plates, wide-brimmed iron helmets, round shields and broad dao, faces turned away. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, straight sword, face weathered and shouting. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_006_wide: The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud. Action: Sui marines leap from flat-bottomed boats onto the wet sand, round shields up and broad dao drawn; a small party of Goguryeo archers on the sloping bank looses a volley and falls back uphill toward the water gate; the marines cheer, chase a few steps, and halt. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: marines pour off the boats, a volley comes from the bank, the archers retreat uphill, the marines cheer and chase a few steps then stop; a Sui officer shouts one line. Sound: bowstrings, dao, Sui cheering, waves, one line of Korean dialogue.
ACTION_START: marines jumping from the boats
ACTION_END: marines halted on the sand, archers gone uphill
NARRATION_KO: 첫 싸움은 작았습니다. 고구려 군은 몇 번 쏘고 물러났습니다. 내호아는 그것을 승리라 불렀습니다. 고구려는 그것을 초대라 불렀습니다.
DIALOGUE_KO: 수 장교: 달아난다! 쫓아라!
SOUND: dây cung, đao, reo Tùy, sóng.
CONTINUITY: [史] chạm trán nhỏ. '달아난다! 쫓아라!' Wide, không gore.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, VEH_204_ref, WPN_201_ref, LOC_006_wide
AI_RISK: đám đông đổ bộ → wide tĩnh

### SC_054 | 7:26–7:34 | LOC_006 (LOC_006_landing) | CHAR_204, SUI_NAVAL_DEPUTY | VEH_204 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot under an oiled canopy, static
IMAGE_PROMPT: Medium two-shot under an oiled canopy, static. @CHAR_204_ref: Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. River spray on the oiled cloak and helmet, wet beard, confident grin, dao drawn. Sui naval deputy commander around 45, thin face with a sparse black beard, dark lacquered leather lamellar armor with iron chest plates, wide-brimmed iron naval helmet, oiled cloak, head bowed. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. Setting @LOC_006_wide: The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud. Action: The Sui admiral stands under an oiled-cloth canopy on the beach, rain dripping from the wide brim of his helmet; the thin-faced naval deputy in dark lacquered armor steps forward one pace, bows his head and speaks low and carefully. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the deputy steps forward, bows, speaks one careful line; the admiral's face does not change. Sound: rain on the canopy, the camp, one line of Korean dialogue.
ACTION_START: deputy standing back
ACTION_END: deputy one pace forward, head bowed
NARRATION_KO: 부총관 주법상은 뭍의 군대를 기다리자고 했습니다. 옳은 말이었습니다. 옳은 말은 늦게 오는 법이었습니다.
DIALOGUE_KO: 주법상: 총관, 뭍의 군사가 올 때까지 기다리십시오.
SOUND: mưa trên lọng, trại.
CONTINUITY: 주법상 = EXTRAS SUI_NAVAL_DEPUTY (1 SC, không ref). '총관, 뭍의 군사가 올 때까지 기다리십시오.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_204_ref, VEH_204_ref, LOC_006_wide

### SC_055 | 7:34–7:42 | LOC_006 (LOC_006_landing) | CHAR_204 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot under the canopy, static (same setup)
IMAGE_PROMPT: Medium shot under the canopy, static (same setup). @CHAR_204_ref: Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. River spray on the oiled cloak and helmet, wet beard, confident grin, dao drawn. Setting @LOC_006_wide: The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud. Action: The admiral laughs loudly, slaps the iron plate on his chest and points up at the fortress on the hill — the outer gate standing wide open, not one figure on the outer wall; his voice coarse. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: a loud laugh, the slap on the chest plate, the arm flung up toward the open gate, one coarse line. Sound: laughter, rain, drums, one line of Korean dialogue.
ACTION_START: admiral beginning to laugh
ACTION_END: arm pointing at the fortress
NARRATION_KO: 그는 성벽 위의 빈자리를 보았습니다. 빈자리는 항복이거나 함정이었습니다. 그는 앞의 것을 골랐습니다.
DIALOGUE_KO: 내호아: 평양은 비었소. 사만이면 남소.
SOUND: cười, mưa, trống.
CONTINUITY: '평양은 비었소. 사만이면 남소.' Cổng ngoại thành mở, tường trống (thấy xa).
CHAIN_FROM: SC_054
CUT_HALF: no
REFS: CHAR_204_ref, LOC_006_wide

### SC_056 | 7:42–7:50 | LOC_006 (LOC_006_landing) | SUI_OFFICER_MOUNTED | VEH_207, WPN_201 | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Medium-high aerial along the ranks, slow drift, no end to the ranks in frame  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Medium-high aerial along the ranks, slow drift, no end to the ranks in frame. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, on a tall warhorse with a high wooden saddle and red saddle cloth. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_006_wide: The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud. Action: Forty thousand picked soldiers form ranks on the sand along the river: wet mingguang armor shining, dao and shields, red banners; rank behind rank along the shore beyond the frame; an officer on a tall warhorse rides along the front rank. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow aerial drift along the ranks: the mounted officer rides the front rank, the ranks stretch beyond both frame edges; one shouted line. Sound: armor clashing, drums, rain, one line of Korean dialogue.
ACTION_START: ranks forming, officer riding in
ACTION_END: officer mid-rank, ranks endless
NARRATION_KO: 사만. 강회에서 데려온 가장 좋은 병사들이었습니다. 내호아는 그들을 성으로 보내고 배는 강에 남겼습니다. 두 번째 실수였습니다. 첫 번째는 주법상이었습니다.
DIALOGUE_KO: 수 장교: 사만, 성으로!
SOUND: giáp va, trống, mưa.
CONTINUITY: '사만, 성으로!' Aerial trung. VEH_207 (LOCK_PENDING) cho sĩ quan trên ngựa.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_207_ref, WPN_201_ref, PROP_021_ref, LOC_006_wide
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)
AI_RISK: 4만 → aerial, không cận

### SC_057 | 7:50–8:00 | LOC_006 (LOC_006_gate_tower) | CHAR_103 | — | PROPS: PROP_012 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium shot on the gate tower, slow push-in to the face
IMAGE_PROMPT: Still for ken-burns: medium shot on the gate tower, slow push-in to the face. @CHAR_103_ref: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Armor and blue jacket dark with rain, water running from the red crest, round shield slung on the back, mud on the boots. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_006_wide: On the two-story timber gate tower of the outer wall of the Goguryeo capital in rain: wet dark tiled roof, wooden railing, dry-stacked grey granite wall below, a black three-legged crow banner hanging wet, the sandy riverbank and the grey-green river with warships far below, rain. Action: The Goguryeo commander with the short red horsehair crest and chinstrap beard stands on the two-story timber gate tower, round shield slung on his back, one hand on the wet railing, looking down at the beach full of boats and shining armor; behind him a soaked yellow banner with a black three-legged crow. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in from the tower to the commander's face. Sound: rain on tiles, Sui drums rising from below.
ACTION_START: commander on the tower, beach below
ACTION_END: tight on his face
NARRATION_KO: 성 위에서 고건무가 내려다보았습니다. 대왕의 아우였습니다. 평양의 방어는 그의 것이었습니다. 그는 사만을 세지 않았습니다. 사만이 걸어올 길을 세었습니다.
DIALOGUE_KO: 
SOUND: mưa trên ngói, trống Tùy vọng lên.
CONTINUITY: Still 10 s. 고건무 trước trận (rain_ep4, ref CHAR_103_ref).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_103_ref, PROP_012_ref, LOC_006_wide

### SC_058 | 8:00–8:08 | LOC_006 (LOC_006_gate_yard) | CHAR_103, GOG_OFFICER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Walk-and-talk tracking shot down the wooden stair
IMAGE_PROMPT: Walk-and-talk tracking shot down the wooden stair. @CHAR_103_ref: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Armor and blue jacket dark with rain, water running from the red crest, round shield slung on the back, mud on the boots. a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain. Setting @LOC_006_wide: The packed-earth yard inside the outer gate of the Goguryeo capital in rain: a wooden stair climbing to the timber gate tower, dry-stacked grey granite walls, wooden houses with rain-dark tiled roofs beyond, puddles, grey light. Action: The commander comes down the wooden stair from the gate tower and walks past a line of waiting Goguryeo officers without stopping, giving an order as he goes; one officer hurries after him through the puddles. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with him down the stair and past the officers: one order given without stopping, an officer running to catch up. Sound: boots on wet wood, rain, armor, one line of Korean dialogue.
ACTION_START: commander at the top of the stair
ACTION_END: commander crossing the yard, officer following
NARRATION_KO: 나곽. 평양의 바깥 성이었습니다. 시장과 절과 백성의 집이 그 안에 있었습니다. 고건무는 그것을 다 내주기로 했습니다.
DIALOGUE_KO: 고건무: 나곽을 비워라. 시장까지 들어오게 두라.
SOUND: giày trên gỗ, mưa, giáp.
CONTINUITY: '나곽을 비워라. 시장까지 들어오게 두라.' Sĩ quan phụ = GOG_OFFICER (WPN_102_ref).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_103_ref, WPN_102_ref, LOC_006_wide

### SC_059 | 8:08–8:16 | LOC_006 (LOC_006_market) | GOG_INFANTRY, GOG_OFFICER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot along the market street
IMAGE_PROMPT: Tracking shot along the market street. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain. Setting @LOC_006_market_ep4: An empty market street in the outer town of the Goguryeo capital in monsoon rain, 612 AD: wooden houses with rain-dark grey tiled and thatched roofs, wooden market stalls left standing with bolts of silk and clay wine jars, doors open, an abandoned ox cart, a stone-paved street running uphill toward a closed inner-wall gate, puddles, grey wet light. Action: Goguryeo soldiers carry the last chest up the sloping street toward the inner town; one stall is left with its bolts of silk untouched; a soldier sets a full clay wine jar on a stall counter and walks on; house doors stand open; rain. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking along the street: the chest carried uphill, the wine jar set down on the counter, the soldier walking away, doors gaping; an officer calls one line. Sound: retreating footsteps, the jar set on wood, rain, one line of Korean dialogue.
ACTION_START: soldiers carrying the chest
ACTION_END: wine jar alone on the counter, street emptying
NARRATION_KO: 비단은 남겨 두었습니다. 술독도 남겨 두었습니다. 배고픈 군대가 비단과 술을 보면 대열이 풀리는 법이었습니다. 고건무는 적의 배를 미끼로 썼습니다.
DIALOGUE_KO: 고구려 장교: 술독은 두라 하셨다.
SOUND: bước chân rút, vò rượu đặt gỗ, mưa.
CONTINUITY: '술독은 두라 하셨다.' Chợ trống có chủ ý (ref LOC_006_market_ep4).
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_102_ref, LOC_006_market_ep4
AI_RISK: phố + lính → tracking, mặt quay đi

### SC_060 | 8:16–8:24 | LOC_006 (LOC_006_temple_int) | CHAR_103, GOG_INFANTRY | — | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from the back of the hall toward the doors, static, light dying as the doors close
IMAGE_PROMPT: Wide from the back of the hall toward the doors, static, light dying as the doors close. @CHAR_103_ref: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Armor and blue jacket dark with rain, water running from the red crest, round shield slung on the back, mud on the boots. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Setting @LOC_006_detail: Inside an empty Goguryeo wooden Buddhist temple hall in rain, 612 AD: thick wooden pillars, a dim gilded wooden Buddha statue, bronze incense burner, a bronze bell, scattered offerings, latticed wooden doors closed with only thin lines of grey light through the cracks, deep shadow. Action: Inside the wooden temple hall: Goguryeo soldiers in iron lamellar file in and sit down shoulder to shoulder between thick pillars, spears upright; a dim gilded Buddha above; the commander enters last with his shield and gives an order; two soldiers swing the three-bay doors shut and a hand cups out the last oil lamp; he sits. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the last men sit, the commander enters and speaks one line, the doors swing shut cutting the grey light to a slit, a hand snuffs the lamp, darkness. Sound: heavy wooden doors, armor settling, rain fading outside, one line of Korean dialogue.
ACTION_START: soldiers seated, doors open, commander entering
ACTION_END: doors shut, lamp out, dark
NARRATION_KO: 절은 비어 있었습니다. 승려들은 내성으로 올라갔습니다. 빈 절에 오백이 들어갔습니다. 그리고 문을 닫았습니다.
DIALOGUE_KO: 고건무: 문을 닫아라. 불을 꺼라.
SOUND: cửa gỗ nặng, giáp ngồi, mưa bên ngoài nhỏ dần.
CONTINUITY: '문을 닫아라. 불을 꺼라.' 500 người → wide, hàng mũ trụ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_103_ref, WPN_102_ref, LOC_006_detail
AI_RISK: đám đông trong nhà → wide tĩnh, người ngồi thấp, tối dần

### SC_061 | 8:24–8:34 | LOC_006 (LOC_006_temple_int) | GOG_INFANTRY | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: from inside the dark hall, slow push-in to the slit of light at the doors
IMAGE_PROMPT: Still for ken-burns: from inside the dark hall, slow push-in to the slit of light at the doors. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Setting @LOC_006_detail: Inside an empty Goguryeo wooden Buddhist temple hall in rain, 612 AD: thick wooden pillars, a dim gilded wooden Buddha statue, bronze incense burner, a bronze bell, scattered offerings, latticed wooden doors closed with only thin lines of grey light through the cracks, deep shadow. Action: In the dark temple: dozens of iron helmets catch a faint sheen from the thin line of grey light through the door crack; a snuffed oil lamp still smoking under a cupped hand; the Buddha statue looking down from above. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in from the rows of dim helmets to the slit of light at the doors. Sound: many held breaths, rain through the door, one soft clink of armor.
ACTION_START: rows of helmets in the dark
ACTION_END: tight on the slit of light
NARRATION_KO: 부처 아래서 오백 명이 숨을 죽였습니다. 밖에서 사만이 오고 있었습니다. 기다리는 쪽이 이기는 법이었습니다. 적어도 이 성에서는.
DIALOGUE_KO: 
SOUND: hơi thở nhiều người nén, mưa qua cửa, một tiếng giáp khẽ.
CONTINUITY: Still 10 s. Light: tối, chỉ khe cửa.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_102_ref, LOC_006_detail

### SC_062 | 8:34–8:42 | LOC_007 (LOC_007_marsh_night) | — | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV, monochrome green, static
IMAGE_PROMPT: Night-vision POV, monochrome green, static. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_marsh_night_ep4: The flooded reed marsh of the north bank at night in rain: black water thigh-deep, walls of tall grey-green reeds dripping, no torches, no moon, a faint grey sheen on the water surface, rain streaking the darkness. Action: Hard cut: a monochrome green night-vision view with heavy grain — pale glowing reeds, black water, rain as streaks; in the center of the view a single human figure wading low through the reeds — then the figure stops; no HUD, no text. Light: Monochrome green night-vision view with heavy grain and rain streaks, black sky, pale green highlights on wet reeds and warm bodies. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static green POV: the wading figure moves through the reeds, then freezes; grain crawls, rain streaks; no dialogue. Sound: night-vision whine, water, rain.
ACTION_START: figure wading
ACTION_END: figure frozen in the reeds
NARRATION_KO: 같은 밤, 살수. 탁발흠은 밤을 보고 있었습니다. 석문령에서 빼앗은 눈이었습니다.
DIALOGUE_KO: 
SOUND: kính đêm rít nhẹ, nước, mưa.
CONTINUITY: POV kính đêm 탁발흠 (không thấy hắn — chars=[]). D2 đêm. EQP_001 lock dán để nhắc thiết bị.
CHAIN_FROM: —
CUT_HALF: yes
REFS: EQP_001_ref, LOC_007_marsh_night_ep4
AI_RISK: POV kính đêm → mono green, không HUD

### SC_063 | 8:42–8:50 | LOC_007 (LOC_007_marsh_night) | CHAR_205, XIANBEI_RIDERS_FOOT | EQP_001, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Lateral tracking shot at hip height, very dark, figures only as rimmed silhouettes
IMAGE_PROMPT: Lateral tracking shot at hip height, very dark, figures only as rimmed silhouettes. @CHAR_205_night_hunt_ep4: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, a fresh cut on the right forearm. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_007_marsh_night_ep4: The flooded reed marsh of the north bank at night in rain: black water thigh-deep, walls of tall grey-green reeds dripping, no torches, no moon, a faint grey sheen on the water surface, rain streaking the darkness. Action: The Xianbei commander wades thigh-deep through black water, the night-vision monocular down over his right eye under the fox-fur cap, bow in hand; behind him twenty riders on foot without horses, spread in a loose double file, bows drawn; rain; only the edges of the figures catch the faint sheen of the water. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Very dark lateral tracking: the file wades slowly, rimmed by the water's sheen, nobody speaks. Sound: slow wading, rain, no voices.
ACTION_START: commander leading into frame
ACTION_END: file crossing the frame in the reeds
NARRATION_KO: 말은 남쪽 기슭에 두고 왔습니다. 말은 물에서 소리를 냅니다. 그는 스무 명을 데리고 걸어서 갈대로 들어왔습니다. 짐승을 찾는 사냥꾼처럼.
DIALOGUE_KO: 
SOUND: lội chậm, mưa, không ai nói.
CONTINUITY: night_hunt_ep4 ✔ (vết cắt cẳng tay phải trong state — chưa bị chém: chấp nhận vì rất tối; ghi risk). Ngựa để bờ nam.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_night_hunt_ep4, EQP_001_ref, VEH_206_ref, LOC_007_marsh_night_ep4
AI_RISK: đám đông đêm → viền người, rất tối; state có 'fresh cut' trước SC_070 → QC bỏ qua trong tối

### SC_064 | 8:50–8:58 | LOC_007 (LOC_007_outpost) | ROK_SENTRY_NVG, ROK_SENTRY_PLAIN | EQP_001, WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close two-shot in the reed hole, static
IMAGE_PROMPT: Close two-shot in the reed hole, static. a ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, a night-vision monocular flipped down over the left eye, a tiny red battery light blinking on it, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: Two ROK sentries crouch in a reed hole: one wears a night-vision monocular down over his eye with a tiny red battery light blinking on it, the other has none; rifles wrapped in cloth, a fixed-blade knife stuck in the mud before them; rain; faces mud-smeared and mostly hidden. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close two-shot: the red light blinks, the sentry with the device whispers one line, the other does not move. Sound: rain, the device whining, a whisper, one line of Korean dialogue.
ACTION_START: both crouched, red light blinking
ACTION_END: whisper delivered, unchanged
NARRATION_KO: 야시경은 넷만 켰습니다. 배터리는 삼십 퍼센트였습니다. 나머지 눈은 다 감았습니다. 이 밤에 이 부대는 넷의 눈으로 보았습니다.
DIALOGUE_KO: 초병: 배터리… 삼십.
SOUND: mưa, kính đêm rít, nhấp nháy.
CONTINUITY: '배터리… 삼십.' Lính không mặt (bùn + tối). 4 kính bật.
CHAIN_FROM: —
CUT_HALF: yes
REFS: EQP_001_ref, WPN_001_ref, LOC_007_marsh_night_ep4
AI_RISK: mặt lính phụ → bùn + tối

### SC_065 | 8:58–9:06 | LOC_007 (LOC_007_reed_path) | CHAR_006 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up crawling at water level, static
IMAGE_PROMPT: Close-up crawling at water level, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: The scout crawls low along the reed path toward the outpost to relieve the watch, knife in hand, cloth-wrapped rifle on his back, no night-vision device, face blackened with mud; he stops and tilts his head — listening to something in the rain. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: he crawls into frame, stops, tilts his head, holds utterly still. Sound: rain, one far-off splash out of rhythm.
ACTION_START: crawling into frame
ACTION_END: stopped, head tilted
NARRATION_KO: 백성민은 야시경 없이 갔습니다. 배터리를 아끼려는 것이었습니다. 그는 눈 대신 귀로 걸었습니다.
DIALOGUE_KO: 
SOUND: mưa, một tiếng lội lệch nhịp rất xa.
CONTINUITY: Đêm D2, không kính đêm. mudface_ep4 (mũ boonie, mặt bùn đen).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, WPN_001_ref, LOC_007_detail

### SC_066 | 9:06–9:14 | LOC_007 (LOC_007_marsh_night) | — | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV, monochrome green, static
IMAGE_PROMPT: Night-vision POV, monochrome green, static. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_marsh_night_ep4: The flooded reed marsh of the north bank at night in rain: black water thigh-deep, walls of tall grey-green reeds dripping, no torches, no moon, a faint grey sheen on the water surface, rain streaking the darkness. Action: Green night-vision view: three pale glowing human shapes in the reeds thirty meters ahead — two crouched, one crawling toward them; at the bottom edge of the view a raised fist in silhouette; no HUD, no text. Light: Monochrome green night-vision view with heavy grain and rain streaks, black sky, pale green highlights on wet reeds and warm bodies. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static green POV: the three shapes hold, the crawling one still moving; a fist rises into the bottom of frame; one whispered line. Sound: night-vision whine, rain, one whispered line of Korean dialogue.
ACTION_START: three shapes, crawling one moving
ACTION_END: fist raised in frame
NARRATION_KO: 그는 셋을 보았습니다. 셋 뒤에 아흔이 있다는 것은 아직 몰랐습니다.
DIALOGUE_KO: 탁발흠: 셋. 소리 없이.
SOUND: kính rít, mưa.
CONTINUITY: '셋. 소리 없이.' POV 탁발흠 — chars=[].
CHAIN_FROM: —
CUT_HALF: yes
REFS: EQP_001_ref, LOC_007_marsh_night_ep4
AI_RISK: POV kính đêm → mono green, hình khối

### SC_067 | 9:14–9:22 | LOC_007 (LOC_007_outpost) | CHAR_006, ROK_SENTRY_NVG | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close two-shot in the dark, static
IMAGE_PROMPT: Close two-shot in the dark, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, a night-vision monocular flipped down over the left eye, a tiny red battery light blinking on it, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: The sentry with the night-vision device turns his head toward the reeds and freezes; his left hand reaches back and taps twice on the boot of the scout who has just crawled up behind him; the scout stops breathing. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the sentry's head turns and locks, the hand reaches back, two taps on the boot, both men rigid. Sound: rain, two taps on a boot, silence.
ACTION_START: sentry turning his head
ACTION_END: hand on the boot after two taps, both frozen
NARRATION_KO: 두 번 두드리는 것. 적이 보인다는 뜻이었습니다. 소리를 내지 말라는 뜻이었습니다.
DIALOGUE_KO: 
SOUND: mưa, hai tiếng gõ giày, im.
CONTINUITY: Gõ 2 cái = có địch. Không thoại.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, EQP_001_ref, LOC_007_marsh_night_ep4

### SC_068 | 9:22–9:30 | LOC_007 (LOC_007_outpost) | CHAR_006, ROK_SENTRY_PLAIN, XIANBEI_RIDERS_FOOT | — | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle at water level, static, water spraying
IMAGE_PROMPT: Low angle at water level, static, water spraying. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: Two Xianbei warriors burst low through the reeds into the hole; the scout springs up to meet the first and both go down into the black water, a knife and a ring-pommel saber locked together under the churning surface, only backs and arms showing; the second sentry wraps the other attacker's legs and drags him down; no gunfire. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the two attackers burst in, the scout rises and tackles the first into the water, bodies rolling half submerged, the second attacker dragged down by his legs; water sprays the lens; no shot fired. Sound: water thrashing, grunting, metal on metal, rain — no gunfire.
ACTION_START: attackers bursting through the reeds
ACTION_END: two pairs struggling half under water
NARRATION_KO: 총은 없었습니다. 총소리 하나면 오천이 깨어날 것이었습니다. 이 싸움은 칼과 물로 해야 했습니다.
DIALOGUE_KO: 
SOUND: nước quật, thở gằn, kim loại chạm, mưa — không tiếng súng.
CONTINUITY: Đánh dao dưới nước: chỉ lưng/tay/nước, không vết thương.
CHAIN_FROM: SC_067
CUT_HALF: yes
REFS: CHAR_006_ref, VEH_206_ref, LOC_007_marsh_night_ep4
AI_RISK: cận chiến 4 người → nửa dưới nước, chỉ lưng và tay, nước bắn che

### SC_069 | 9:30–9:38 | LOC_007 (LOC_007_outpost) | CHAR_006, ROK_SENTRY_PLAIN, ROK_SENTRY_NVG, XIANBEI_RIDER | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle at water level, static (same setup)
IMAGE_PROMPT: Low angle at water level, static (same setup). @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. a ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, a night-vision monocular flipped down over the left eye, a tiny red battery light blinking on it, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: The sentry without the device brings a cloth-wrapped rifle butt down hard; a cut bowstring whips up; the sentry with the device is being choked from behind — the scout rises out of the water and hauls the choking attacker backward off him; the water boils; no wounds shown. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the rifle butt drops, a bowstring snaps up, the scout surges out of the water and drags the attacker off the choking sentry backward into the reeds; water churns. Sound: rifle butt thud, bowstring snapping, water, rain.
ACTION_START: rifle butt raised, sentry being choked
ACTION_END: attacker hauled backward into the water by the scout
NARRATION_KO: 야시경이 있는 쪽은 적이었습니다. 이 밤은 뒤집혀 있었습니다.
DIALOGUE_KO: 
SOUND: báng súng, dây cung đứt, nước, mưa.
CONTINUITY: Báng súng bọc vải (không bắn). Không cận vết thương.
CHAIN_FROM: SC_068
CUT_HALF: yes
REFS: CHAR_006_ref, VEH_206_ref, WPN_001_ref, LOC_007_marsh_night_ep4
AI_RISK: cận chiến → nửa dưới nước, nước sủi

### SC_070 | 9:38–9:46 | LOC_007 (LOC_007_outpost) | CHAR_205, CHAR_006 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up in near darkness, static, only the small green glow of the device
IMAGE_PROMPT: Close-up in near darkness, static, only the small green glow of the device. @CHAR_205_night_hunt_ep4: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, a fresh cut on the right forearm. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: The Xianbei commander himself lunges in from the left with his ring-pommel saber; the scout twists and his knife slashes across the commander's right forearm — the saber arm; the commander jerks back, the night-vision device knocked askew over his eye, his fox-fur cap falling into the water and floating away. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up in near darkness: the saber sweeps in from the left, the scout twists, the knife slashes the sword forearm, the commander recoils, the device tilts on his face, the cap drops into the water and drifts off; a hiss through teeth. Sound: saber cutting air, knife on skin, a hiss through clenched teeth, rain.
ACTION_START: saber lunging in from the left
ACTION_END: commander recoiled, cap floating away, device askew
NARRATION_KO: 탁발흠은 부하 뒤에 서지 않았습니다. 그것이 그가 살아남은 방식이었습니다. 이번에는 그것이 그를 다치게 했습니다.
DIALOGUE_KO: 
SOUND: đao rít, dao rạch da, thở rít qua răng, mưa.
CONTINUITY: Cẳng tay PHẢI bị chém (night_hunt_ep4 ✔ 'fresh cut on the right forearm'). Mũ lông trôi — không vớt.
CHAIN_FROM: SC_069
CUT_HALF: yes
REFS: CHAR_205_night_hunt_ep4, CHAR_006_ref, EQP_001_ref, LOC_007_marsh_night_ep4
AI_RISK: dao cận + 2 người → rất tối, chớp xanh nhỏ, không máu cận

### SC_071 | 9:46–9:54 | LOC_007 (LOC_007_outpost) | CHAR_205, CHAR_006, ROK_SENTRY_PLAIN | EQP_001, WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_night_hunt_ep4: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dripping, night-vision monocular knocked askew over the right eye, wet dark cloak over the armor, mud on the knees, a fresh cut on the right forearm, turning to flee. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: The bareheaded commander turns and plunges away south through the reeds, water spraying; the sentry rips the cloth off his rifle and raises it — the scout's hand shoots up out of the water and slams the muzzle down into the mud. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium: the commander crashes away through the reeds, the sentry tears the cloth off and raises the rifle, a hand from the water slaps the barrel down into the mud; one whispered line. Sound: wading fading fast, cloth ripping, the barrel hitting mud, one whispered line of Korean dialogue.
ACTION_START: commander turning to flee, rifle still wrapped
ACTION_END: rifle muzzle in the mud under the scout's hand, commander gone
NARRATION_KO: 총은 다시 덮였습니다. 밤의 규칙은 지켜졌습니다. 그 값은 달아난 사람 하나였습니다.
DIALOGUE_KO: 백성민: 쏘지 마.
SOUND: lội chạy xa dần, vải giật, nòng súng đập bùn.
CONTINUITY: '쏘지 마.' 탁발흠 đầu trần chạy (capless_night_ep4).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_night_hunt_ep4, CHAR_006_ref, EQP_001_ref, WPN_001_ref, LOC_007_marsh_night_ep4
AI_RISK: súng nâng → không cận cò, tay đập nòng

### SC_072 | 9:54–10:02 | LOC_007 (LOC_007_outpost) | CHAR_006, ROK_SENTRY_PLAIN, ROK_SENTRY_NVG | — | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle at water level, static
IMAGE_PROMPT: Low angle at water level, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. a ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, a night-vision monocular flipped down over the left eye, a tiny red battery light blinking on it, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. Setting @LOC_007_marsh_night_ep4: A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light. Action: Two Xianbei bodies float face down in the reed water; the second sentry clutches a bleeding arm; the scout kneels chest-deep in the water, breathing hard, head turned south after the fleeing shape. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static at water level: the water settles, the sentry holds his arm, the scout breathes and stares south; the sentry says one line. Sound: breathing, water calming, rain, one line of Korean dialogue.
ACTION_START: water still churning, scout rising
ACTION_END: scout kneeling still, staring south
NARRATION_KO: 둘이 갈대 밑에 남았습니다. 한 사람이 달아났습니다. 달아난 사람이 우두머리였습니다.
DIALOGUE_KO: 초병: 중사님, 팔이…
SOUND: thở, nước lặng dần, mưa.
CONTINUITY: '중사님, 팔이…' Xác nổi úp (không mặt).
CHAIN_FROM: SC_071
CUT_HALF: yes
REFS: CHAR_006_ref, LOC_007_marsh_night_ep4
AI_RISK: xác → nổi úp, tối

### SC_073 | 10:02–10:10 | LOC_007 (LOC_007_marsh_night) | CHAR_006 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the scout's face, then rack to a tiny green point far off in the dark
IMAGE_PROMPT: Close-up on the scout's face, then rack to a tiny green point far off in the dark. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_marsh_night_ep4: The flooded reed marsh of the north bank at night in rain: black water thigh-deep, walls of tall grey-green reeds dripping, no torches, no moon, a faint grey sheen on the water surface, rain streaking the darkness. Action: The scout's mud-black face, eyes fixed south; beyond him in the black rain a single tiny green point of light — the eyepiece glow of a night-vision device — bobs away and winks out behind the reeds. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Close on the face, then focus racks past him to the tiny green point bobbing away in the dark until it vanishes; one line spoken. Sound: rain, distant wading, one line of Korean dialogue.
ACTION_START: scout's face, green point far off
ACTION_END: green point gone, face in the dark
NARRATION_KO: 
DIALOGUE_KO: 백성민: 야시경입니다. 우리 겁니다.
SOUND: mưa, lội rất xa.
CONTINUITY: '야시경입니다. 우리 겁니다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, EQP_001_ref, LOC_007_marsh_night_ep4

### SC_074 | 10:10–10:18 | LOC_007 (LOC_007_south_horses) | CHAR_205, XIANBEI_DEPUTY | EQP_001, VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up at the horse lines, static
IMAGE_PROMPT: Medium close-up at the horse lines, static. @CHAR_205_night_hunt_ep4: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap lost, braid exposed and dripping, wet dark cloak over the armor, mud to the thighs, a fresh cut on the right forearm, the night-vision monocular held in one hand on its strap. a Xianbei deputy around 30 in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, a thin black mustache, listening. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_007_south_camp_ep4: The horse lines at the edge of the Sui rear-guard camp on the south bank at night in rain: short stocky steppe horses tethered to a rope line, wet sand, dark tents and a few guttering torches behind, the black river beyond. Action: The bareheaded commander reaches the horses, tears a strip from his tunic hem and binds his right forearm, unslings the night-vision device and holds it up before his face, breathing hard; then a soundless laugh; he speaks to his deputy. Light: Night in rain, warm orange torchlight against blue-black darkness, fire reflected in wet surfaces. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the strip torn and wound around the forearm, the device lifted and stared at, breath slowing, a silent laugh, one curt line to the deputy. Sound: cloth tearing, horses, rain, one line of Korean dialogue.
ACTION_START: binding the forearm
ACTION_END: device held up, laughing without sound
NARRATION_KO: 그는 팔을 잃지 않았습니다. 대신 위치를 얻었습니다. 정확한 위치는 아직 아니었습니다. 그러나 갈대밭 안이라는 것은 확실했습니다.
DIALOGUE_KO: 탁발흠: 찾았다. 갈대밭 안이다. 어디쯤인지는 다음 밤에.
SOUND: vải xé, ngựa, mưa.
CONTINUITY: '찾았다. 갈대밭 안이다. 어디쯤인지는 다음 밤에.' Đầu trần (bareheaded_ep4). Băng cẳng tay PHẢI.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_night_hunt_ep4, EQP_001_ref, VEH_206_ref, LOC_007_south_camp_ep4

### SC_075 | 10:18–10:30 | LOC_007 (LOC_007_aerial_night) | — | EQP_001 | PROPS: — | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: high aerial at night in rain, very slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial at night in rain, very slow pull-out. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_wide: The wide shallow river at night in rain seen from high above: black water with a faint grey sheen, pale sandbars, the vast dark reed beds of the north bank, low black hills on the south bank with a few scattered orange torch points, no moon. Action: From high above at night in rain: the vast black reed beds, the river a dim grey-silver band; at the southern corner of the frame one tiny green point like a firefly moves toward a camp marked by a few orange torches. Light: Night from high above in rain, black land and grey water, a few scattered orange torch points. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow pull-out from the green point to the whole dark river. Sound: rain, high wind.
ACTION_START: tight on the green point near the torches
ACTION_END: wide on the black reed beds and river
NARRATION_KO: 그날 밤, 갈대밭에서 처음으로 적이 그들보다 멀리 봤습니다.
DIALOGUE_KO: 
SOUND: mưa, gió trên cao.
CONTINUITY: Still 12 s. Kết P4.
CHAIN_FROM: —
CUT_HALF: no
REFS: EQP_001_ref, LOC_007_wide
AI_RISK: aerial đêm → tối, điểm sáng nhỏ


## [Phần 5] 빈 절 (10:30–14:00) · [史] 4만 vào 나곽, cửa chùa mở · narrator im 11:20–12:08 · trại 우중문 30리 · MID-ROLL 2 @14:00

### SC_076 | 10:30–10:40 | LOC_006 (LOC_006_water_gate) | — | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial in rain, slow slide from the gate into the streets  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial in rain, slow slide from the gate into the streets. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_006_wide: The water gate of the outer wall of the Goguryeo capital in rain: a stone gate passage through dry-stacked grey granite walls with a timber gate tower above, two-leaf iron-sheathed wooden doors standing open, the stone-paved market street inside, and outside the gate the sandy riverbank sloping down to the wide grey-green river with warships. Action: From above in rain: the water gate of the outer wall stands wide open and a river of shining wet armor and red banners pours from the beach through the gate into the streets, spreading into every lane like water; on the hill the inner wall stays shut. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide from the open water gate along the flood of soldiers into the market streets. Sound: Sui drums, cheering, rain.
ACTION_START: gate and beach
ACTION_END: streets filling with soldiers
NARRATION_KO: 사흘째 아침. 사만이 나곽으로 들어갔습니다. 문은 열려 있었고, 성벽 위에는 아무도 없었습니다. 내호아는 그것을 항복이라 읽었습니다.
DIALOGUE_KO: 
SOUND: trống Tùy, reo, mưa.
CONTINUITY: Still 10 s. D3 sáng. 4만 vào 나곽.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, PROP_021_ref, LOC_006_wide
AI_RISK: đại quân → aerial

### SC_077 | 10:40–10:48 | LOC_006 (LOC_006_market) | SUI_SOLDIERS_LOOTING, SUI_OFFICER_MOUNTED | VEH_207, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot through the market street
IMAGE_PROMPT: Tracking shot through the market street. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, on a tall warhorse with a high wooden saddle and red saddle cloth. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_006_market_ep4: An empty market street in the outer town of the Goguryeo capital in monsoon rain, 612 AD: wooden houses with rain-dark grey tiled and thatched roofs, wooden market stalls left standing with bolts of silk and clay wine jars, doors open, an abandoned ox cart, a stone-paved street running uphill toward a closed inner-wall gate, puddles, grey wet light. Action: Sui soldiers kick in house doors and drag bolts of silk onto the stalls, one man carrying a whole roll of silk on his shoulder; two fight over a clay wine jar and gulp from it; a mounted officer shouts to hold ranks and nobody listens; rain. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking through the chaos: doors kicked, silk dragged out, the jar fought over and gulped, the mounted officer shouting one line that is drowned out. Sound: doors breaking, pottery shattering, laughter, one shouted line of Korean dialogue swallowed by noise.
ACTION_START: soldiers kicking a door
ACTION_END: officer shouting unheard amid looters
NARRATION_KO: 배고픈 병사에게 빈 시장은 명령보다 컸습니다. 대열은 시장 골목마다 한 줄씩 풀렸습니다. 고건무가 원한 그대로였습니다.
DIALOGUE_KO: 수 장교: 대열을 지켜라! 대열!
SOUND: cửa gãy, gốm vỡ, cười, sĩ quan hét bị át.
CONTINUITY: '대열을 지켜라! 대열!' Mặt lính quay đi. VEH_207 cho sĩ quan cưỡi ngựa.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_207_ref, WPN_201_ref, LOC_006_market_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)
AI_RISK: đám đông cướp phá → tracking, mặt quay đi, out-focus

### SC_078 | 10:48–10:56 | LOC_006 (LOC_006_market) | CHAR_204, SUI_SOLDIERS_LOOTING | VEH_207 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the head of the street, static, low angle on the rider
IMAGE_PROMPT: Medium shot at the head of the street, static, low angle on the rider. @CHAR_204_ref: Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. River spray on the oiled cloak and helmet, wet beard, confident grin, dao drawn. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. Setting @LOC_006_market_ep4: An empty market street in the outer town of the Goguryeo capital in monsoon rain, 612 AD: wooden houses with rain-dark grey tiled and thatched roofs, wooden market stalls left standing with bolts of silk and clay wine jars, doors open, an abandoned ox cart, a stone-paved street running uphill toward a closed inner-wall gate, puddles, grey wet light. Action: The Sui admiral rides into the head of the market street on a tall warhorse and sees his men looting; instead of shouting he laughs aloud and sweeps his broad dao around the street in a wide gesture. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the horse walks in, the admiral looks, laughs, sweeps the dao around the street and calls one line. Sound: laughter, the horse, pottery breaking, one line of Korean dialogue.
ACTION_START: admiral riding in, looking
ACTION_END: dao swept wide, laughing
NARRATION_KO: 내호아는 대열을 세우지 않았습니다. 그도 시장을 보았습니다.
DIALOGUE_KO: 내호아: 내 성이다. 마음껏 가져가라.
SOUND: cười, ngựa, gốm vỡ.
CONTINUITY: '내 성이다. 마음껏 가져가라.' Landing state (grin, dao drawn). VEH_207 LOCK_PENDING.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_204_ref, WPN_201_ref, VEH_207_ref, LOC_006_market_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)

### SC_079 | 10:56–11:04 | LOC_006 (LOC_006_alley) | SUI_SOLDIER_BACK | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot from behind the soldier, static
IMAGE_PROMPT: Medium shot from behind the soldier, static. a single Sui foot soldier in a wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, straw sandals, seen from behind. Setting @LOC_006_market_ep4: A narrow alley between two rows of wooden houses in the outer town of the Goguryeo capital in rain: wet stone paving, rain dripping from grey tiled eaves, wooden walls, and at the end of the alley the closed three-bay wooden doors of a temple hall, grey light. Action: A single Sui soldier with a bolt of silk on his shoulder turns into a narrow alley between wooden houses; the alley is dead quiet, rain dripping from the eaves; he stops — something feels wrong — and looks at the closed three-bay wooden doors of the temple at the end of the alley; then shrugs and walks on. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static from behind: he walks in with the silk, stops, stares at the closed temple doors, shrugs, walks on. Sound: rain dripping, one man's footsteps, silence.
ACTION_START: soldier entering the alley
ACTION_END: soldier walking on toward the doors
NARRATION_KO: 골목은 너무 조용했습니다. 조용함을 이상하게 여긴 병사도 있었습니다. 그러나 비단이 더 무거웠습니다.
DIALOGUE_KO: 
SOUND: mưa nhỏ giọt, bước chân một người, im.
CONTINUITY: Từ sau lưng, không mặt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, LOC_006_market_ep4

### SC_080 | 11:04–11:12 | LOC_006 (LOC_006_temple_int) | CHAR_103, GOG_INFANTRY | — | PROPS: — | TYPE: video8s | 8s
SHOT: Extreme close-up on an eye at the door crack, static
IMAGE_PROMPT: Extreme close-up on an eye at the door crack, static. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Blood on the spear blade and right forearm, smoke smudges on face and armor, sweat, one plank of the round shield split, red crest frayed, teeth clenched mid-battle. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Setting @LOC_006_detail: Inside an empty Goguryeo wooden Buddhist temple hall in rain, 612 AD: thick wooden pillars, a dim gilded wooden Buddha statue, bronze incense burner, a bronze bell, scattered offerings, latticed wooden doors closed with only thin lines of grey light through the cracks, deep shadow. Action: In the dark temple the commander's eye is pressed to the crack of the door: outside, the market street scattered with Sui soldiers, no ranks, an officer's horse abandoned; behind him in the dark five hundred men rise to their feet without a sound, spears lowering level. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up on the eye at the crack, the bright slit of street beyond it; behind, out of focus, dark shapes rise and spears come level without a sound. Sound: breathing, a whisper of armor, looting noise through the door.
ACTION_START: eye at the crack, men seated behind
ACTION_END: men standing behind, spears level
NARRATION_KO: 고건무는 기다렸습니다. 사만이 다 들어올 때까지. 대열이 완전히 풀릴 때까지. 기다림은 그의 병법이었습니다.
DIALOGUE_KO: 
SOUND: hơi thở, giáp khẽ, ngoài cửa tiếng cướp phá.
CONTINUITY: ambush_ep4 ✔ từ đây (máu trên giáo/cẳng tay có thể chưa có — tối, chấp nhận). 500 người = hình khối tối.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_103_ambush_ep4, WPN_102_ref, LOC_006_detail
AI_RISK: đám đông tối → out-focus, hình khối

### SC_081 | 11:12–11:20 | LOC_006 (LOC_006_temple_int) | CHAR_103, GOG_INFANTRY | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot inside the doors, static
IMAGE_PROMPT: Medium shot inside the doors, static. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Blood on the spear blade and right forearm, smoke smudges on face and armor, sweat, one plank of the round shield split, red crest frayed, teeth clenched mid-battle. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Setting @LOC_006_detail: Inside an empty Goguryeo wooden Buddhist temple hall in rain, 612 AD: thick wooden pillars, a dim gilded wooden Buddha statue, bronze incense burner, a bronze bell, scattered offerings, latticed wooden doors closed with only thin lines of grey light through the cracks, deep shadow. Action: The commander straightens, round shield up on his left arm, spear in his right hand, turns to look back one beat at the five hundred standing in the dark, then faces the doors and speaks low. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: shield up, the look back, the turn to the doors, one low line. Sound: shield knocking armor, silence, one line of Korean dialogue.
ACTION_START: commander straightening, shield rising
ACTION_END: facing the doors, line spoken
NARRATION_KO: 문을 여는 것. 이 성의 첫 번째 명령이었습니다. 전날 닫으라 한 사람이 열라 했습니다.
DIALOGUE_KO: 고건무: 지금이다. 문을 열어라.
SOUND: khiên chạm giáp, im.
CONTINUITY: '지금이다. 문을 열어라.' → NARRATOR IM 11:20–12:08.
CHAIN_FROM: SC_080
CUT_HALF: yes
REFS: CHAR_103_ambush_ep4, WPN_102_ref, LOC_006_detail

### SC_082 | 11:20–11:28 | LOC_006 (LOC_006_temple_doors) | CHAR_103, GOG_INFANTRY, SUI_SOLDIERS_LOOTING | — | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from the middle of the street facing the temple, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide from the middle of the street facing the temple, static. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Blood on the spear blade and right forearm, smoke smudges on face and armor, sweat, one plank of the round shield split, red crest frayed, teeth clenched mid-battle. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. Setting @LOC_006_detail: The three-bay wooden doors of an empty Goguryeo temple hall opening onto a rain-soaked market street with abandoned stalls, bolts of silk, clay wine jars and an abandoned ox cart, wooden houses with rain-dark tiled roofs, grey wet light. Action: The three-bay temple doors burst outward and five hundred Goguryeo soldiers pour out in a wedge, spears leveled, the commander at the point; rain slants across; Sui soldiers in the street turn, silk dropping from their arms. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the doors slam open, the wedge pours out with the commander at its tip, looters turn and drop their silk. Sound: doors slamming, hundreds of boots on wet stone, one short Goguryeo war cry.
ACTION_START: doors closed, street with looters
ACTION_END: wedge in the street, silk falling
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: cửa gỗ nện, hàng trăm giày trên đá, tiếng hô Goguryeo ngắn.
CONTINUITY: Narrator im. Wide, đám đông.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_103_ambush_ep4, WPN_102_ref, WPN_201_ref, LOC_006_detail
AI_RISK: đám đông → wide tĩnh

### SC_083 | 11:28–11:36 | LOC_006 (LOC_006_market) | GOG_INFANTRY, SUI_SOLDIERS_LOOTING, GOG_OFFICER | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static, no gore
IMAGE_PROMPT: Wide, static, no gore. Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_006_market_ep4: An empty market street in the outer town of the Goguryeo capital in monsoon rain, 612 AD: wooden houses with rain-dark grey tiled and thatched roofs, wooden market stalls left standing with bolts of silk and clay wine jars, doors open, an abandoned ox cart, a stone-paved street running uphill toward a closed inner-wall gate, puddles, grey wet light. Action: Sui soldiers with silk and wine in their hands are swept up by the wedge — some run, some trip over silk and fall, some fumble for their dao too late; no rank anywhere to resist; a Goguryeo officer shouts to drive them into the lanes. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the wedge rolls through the street, looters scatter, trip, fall; one Goguryeo officer shouts a line. Sound: spears, pottery shattering, screams, rain, one line of Korean dialogue.
ACTION_START: wedge meeting the looters
ACTION_END: looters scattering into the lanes
NARRATION_KO: 
DIALOGUE_KO: 고구려 장교: 골목으로 몰아라!
SOUND: giáo, gốm vỡ, thét, mưa.
CONTINUITY: '골목으로 몰아라!' Không gore.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, WPN_201_ref, LOC_006_market_ep4
AI_RISK: đám đông → wide, không cận

### SC_084 | 11:36–11:44 | LOC_006 (LOC_006_alley) | CHAR_103, SUI_OFFICER_MOUNTED | VEH_207 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot in the narrow alley, static, close
IMAGE_PROMPT: Medium shot in the narrow alley, static, close. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Blood on the spear blade and right forearm, smoke smudges on face and armor, sweat, one plank of the round shield split, red crest frayed, teeth clenched mid-battle. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, on a tall warhorse with a high wooden saddle and red saddle cloth. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. Setting @LOC_006_market_ep4: A narrow alley between two rows of wooden houses in the outer town of the Goguryeo capital in rain: wet stone paving, rain dripping from grey tiled eaves, wooden walls, and at the end of the alley the closed three-bay wooden doors of a temple hall, grey light. Action: In the narrow alley the commander thrusts his spear and takes a dao cut on his round shield; a Sui officer on a tall warhorse tries to rally men — the horse shies from the spears, rears and throws him. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium: spear thrust, dao on shield, the horse rears and throws its rider; no dialogue. Sound: wooden shield, a horse screaming, spear.
ACTION_START: commander thrusting, officer mounted
ACTION_END: officer thrown, horse rearing
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: khiên gỗ, ngựa hí, giáo.
CONTINUITY: Khiên nứt một mảnh (ambush state). VEH_207.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_103_ambush_ep4, WPN_201_ref, VEH_207_ref, LOC_006_market_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)
AI_RISK: ngựa dựng + cận chiến → 1 ngựa, máy tĩnh

### SC_085 | 11:44–11:52 | LOC_006 (LOC_006_rooftops) | GOG_ARCHERS, SUI_SOLDIERS_LOOTING | WPN_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the alley up to the rooftops, static
IMAGE_PROMPT: Low angle from the alley up to the rooftops, static. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. Setting @LOC_006_market_ep4: Wet grey tiled rooftops of wooden houses on both sides of a narrow stone-paved alley in the outer town of the Goguryeo capital, rain, grey sky. Action: On the wet tiled roofs on both sides of the alley Goguryeo archers spring up and shoot down into the stream of Sui soldiers jammed in the alley; the soldiers trample one another falling back toward the water gate. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: archers rise on the roofs and loose arrow after arrow downward, the crowd below shoving back. Sound: bowstrings in rapid succession, boots slipping on wet stone, screams.
ACTION_START: archers rising on the roofs
ACTION_END: archers shooting, crowd below pushing back
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: dây cung liên tiếp, giày trượt trên đá ướt, thét.
CONTINUITY: Cung thủ trên mái. Wide-ish low angle.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_102_ref, WPN_201_ref, WPN_101_ref, LOC_006_market_ep4
AI_RISK: cung thủ số đông → low angle, hình dáng trên mái

### SC_086 | 11:52–12:00 | LOC_006 (LOC_006_water_gate) | CHAR_204, SUI_SOLDIERS_LOOTING | VEH_207, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot on the mounted admiral near the gate, static
IMAGE_PROMPT: Medium shot on the mounted admiral near the gate, static. @CHAR_204_ambush_ep4: Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. Blood on the dao blade, smoke smudges, helmet brim dented, cloak scorched at the hem, sweat and panic in the eyes, mid-run. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_006_wide: The water gate of the outer wall of the Goguryeo capital in rain: a stone gate passage through dry-stacked grey granite walls with a timber gate tower above, two-leaf iron-sheathed wooden doors standing open, the stone-paved market street inside, and outside the gate the sandy riverbank sloping down to the wide grey-green river with warships. Action: The admiral on his warhorse near the water gate sees his own men running toward him, silk strewn across the street behind them; his face changes from a grin to grey; he screams. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium: the men come running toward him, the grin drains from his face, he screams one line, the horse wheeling. Sound: the horse, screams, rain, distant bowstrings, one line of Korean dialogue.
ACTION_START: admiral grinning, men beginning to run
ACTION_END: admiral grey-faced, screaming, horse wheeling
NARRATION_KO: 
DIALOGUE_KO: 내호아: 시장이 왜 이리 조용… 물러나라! 배로!
SOUND: ngựa, thét, mưa, cung xa.
CONTINUITY: '시장이 왜 이리 조용… 물러나라! 배로!' ambush_ep4 ✔.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_204_ambush_ep4, VEH_207_ref, WPN_201_ref, LOC_006_wide
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)

### SC_087 | 12:00–12:08 | LOC_006 (LOC_006_water_gate) | SUI_SOLDIERS_LOOTING, GOG_CAVALRYMEN | VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-high aerial over the gate and beach, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Medium-high aerial over the gate and beach, static. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_006_wide: The water gate of the outer wall of the Goguryeo capital in rain: a stone gate passage through dry-stacked grey granite walls with a timber gate tower above, two-leaf iron-sheathed wooden doors standing open, the stone-paved market street inside, and outside the gate the sandy riverbank sloping down to the wide grey-green river with warships. Action: A stream of Sui soldiers jams through the water gate onto the sandy beach; from two side lanes Goguryeo armored cavalry burst out and cut across the stream; silk and dao litter the sand. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static aerial: the crowd squeezes through the gate, cavalry cut across it from the lanes, silk scattering on the sand. Sound: hooves, armor, screams, waves.
ACTION_START: crowd in the gate, lanes empty
ACTION_END: cavalry cutting across the beach
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: vó ngựa, giáp, thét, sóng.
CONTINUITY: [史]. Aerial trung.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, VEH_101_ref, LOC_006_wide
AI_RISK: đám đông + kỵ → aerial

### SC_088 | 12:08–12:16 | LOC_006 (LOC_006_landing) | SUI_SOLDIERS_LOOTING, GOG_ARCHERS | VEH_204 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from the beach toward the water, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide from the beach toward the water, static. Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets. Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. Setting @LOC_006_wide: The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud. Action: Soldiers wade out and cling to the sides of flat-bottomed boats; an overloaded boat tips and capsizes; Goguryeo archers on the bank shoot into the water; far out the big tower warships lower sail and back oars. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the boat tips and goes over, archers shoot from the bank, the warships back away. Sound: a boat capsizing, water, bowstrings, naval drums in confusion.
ACTION_START: soldiers clinging to the boat
ACTION_END: boat capsized, warships backing off
NARRATION_KO: 4만 중 수천 명만 배로 돌아갔습니다. 나머지는 시장과 골목과 강가에 남았습니다.
DIALOGUE_KO: 
SOUND: thuyền lật, nước, dây cung, trống thủy quân rối loạn.
CONTINUITY: Narrator quay lại 12:08. Wide.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, WPN_102_ref, VEH_204_ref, LOC_006_wide
AI_RISK: đám đông + thuyền → wide

### SC_089 | 12:16–12:24 | LOC_006 (LOC_006_landing) | CHAR_204 | VEH_204 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot with the horse down into the water
IMAGE_PROMPT: Tracking shot with the horse down into the water. @CHAR_204_ambush_ep4: Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. Blood on the dao blade, smoke smudges, helmet brim dented, cloak scorched at the hem, sweat and panic in the eyes, mid-run. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. Setting @LOC_006_wide: The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud. Action: The admiral is thrown onto the sand, his helmet brim dented; he snatches the reins of a saddleless horse bolting past, hauls himself onto its bare back and drives it into the river toward the nearest tower warship. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking: he hits the sand, grabs the passing horse's reins, scrambles up bareback and rides it into the water toward the warship. Sound: the horse, water, screams behind.
ACTION_START: admiral on the sand, horse bolting past
ACTION_END: riding bareback into the river
NARRATION_KO: 내호아는 안장 없는 말로 강에 들어갔습니다. 배까지 닿았습니다. 그의 사만은 닿지 못했습니다.
DIALOGUE_KO: 
SOUND: ngựa, nước, thét sau lưng.
CONTINUITY: ambush_ep4 ✔ (áo cháy ở gấu — QC ep4 bỏ 'áo cháy' trong script; ref đã có, chấp nhận). Ngựa không yên (không VEH_207 lock — ngựa trần).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_204_ambush_ep4, VEH_204_ref, LOC_006_wide
AI_RISK: người leo ngựa → tracking, chuyển động 1 người 1 ngựa

### SC_090 | 12:24–12:32 | LOC_006 (LOC_006_water_gate) | CHAR_103, GOG_OFFICER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot under the gate arch, static
IMAGE_PROMPT: Medium shot under the gate arch, static. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Helmet removed and held at the side, black topknot loosened, smoke-smudged face, calm. a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain. Setting @LOC_006_wide: The water gate of the outer wall of the Goguryeo capital in rain: a stone gate passage through dry-stacked grey granite walls with a timber gate tower above, two-leaf iron-sheathed wooden doors standing open, the stone-paved market street inside, and outside the gate the sandy riverbank sloping down to the wide grey-green river with warships. Action: The commander stands under the arch of the water gate, helmet off and hair wet, blood on his forearm, his round shield split, looking out at the beach of men and capsized boats; he speaks flatly to the officer beside him. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he looks out at the beach, then gives one flat line to the officer beside him, who runs. Sound: rain, distant screams, waves, one line of Korean dialogue.
ACTION_START: commander looking at the beach
ACTION_END: officer running off, commander still
NARRATION_KO: 이기는 것은 절반이었습니다. 나머지 절반은 쫓는 것이었습니다. 고건무는 배까지 쫓게 했습니다.
DIALOGUE_KO: 고건무: 배까지 쫓아라.
SOUND: mưa, thét xa, sóng.
CONTINUITY: '배까지 쫓아라.' helmet_off (ref ambush_ep4). Máu cẳng tay, khiên nứt.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_103_ambush_ep4, WPN_102_ref, LOC_006_wide

### SC_091 | 12:32–12:42 | LOC_006 (LOC_006_river_burning) | — | VEH_204 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide from the flames out to the river, slow pull  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide from the flames out to the river, slow pull. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_006_wide: The wide grey-green river below the Goguryeo capital in rain: flat-bottomed landing boats burning on the water with black smoke mixing into rain, tower warships rowing backward toward midstream with red banners drooping, broken red banners leaning in the wet sand of the beach. Action: Landing boats burn on the grey water, black smoke mixing with rain; a large tower warship rows backward to midstream, red banners drooping; on the beach a broken Sui banner leans in the wet sand. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull from the burning boat to the whole river. Sound: fire, timber cracking, distant oars, rain.
ACTION_START: tight on the burning boat
ACTION_END: wide on river, warship, broken banner
NARRATION_KO: 배가 탔습니다. 강회의 배였습니다. 동래에서 여기까지 온 배였습니다. 내호아는 그날 밤 강을 내려가 바다로 나갔습니다.
DIALOGUE_KO: 
SOUND: lửa, gỗ nổ, chèo xa, mưa.
CONTINUITY: Still 10 s. Thuyền cháy.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_204_ref, PROP_021_ref, LOC_006_wide

### SC_092 | 12:42–12:50 | LOC_006 (LOC_006_market) | CHAR_103, GOG_OFFICER | — | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Tracking shot walking through the wrecked market, no close-ups of bodies
IMAGE_PROMPT: Tracking shot walking through the wrecked market, no close-ups of bodies. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Helmet removed and held at the side, black topknot loosened, smoke-smudged face, calm. a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_006_market_ep4: An empty market street in the outer town of the Goguryeo capital in monsoon rain, 612 AD: wooden houses with rain-dark grey tiled and thatched roofs, wooden market stalls left standing with bolts of silk and clay wine jars, doors open, an abandoned ox cart, a stone-paved street running uphill toward a closed inner-wall gate, puddles, grey wet light. Action: The commander walks through the wrecked market street: cloth-covered dead at the edges of frame, silk trampled in mud, broken wine jars; he stoops, picks up a wet Sui banner, looks at it, lets it fall, and speaks to the officer walking behind him. Light: Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with him through the street: the stoop, the banner lifted and dropped, one line spoken to the officer behind. Sound: rain, boots on broken pottery, the wet banner falling, one line of Korean dialogue.
ACTION_START: commander walking in
ACTION_END: banner dropped, line spoken
NARRATION_KO: 그는 사만을 오백으로 깼습니다. 쇠수레도, 천둥도 없이. 평양은 그렇게 지켜졌습니다.
DIALOGUE_KO: 고건무: 평양은 고구려 사람이 지키오.
SOUND: mưa, giày trên gốm vỡ, cờ ướt rơi.
CONTINUITY: '평양은 고구려 사람이 지키오.' Xác phủ vải ở mép khung.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_103_ambush_ep4, WPN_102_ref, PROP_021_ref, LOC_006_market_ep4
AI_RISK: xác → phủ vải, mép khung

### SC_093 | 12:50–13:00 | LOC_006 (LOC_006_haepo) | — | VEH_204 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial over a grey bay, slow pull-out to open sea  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial over a grey bay, slow pull-out to open sea. @VEH_204_ref: Sui dynasty tower warship, long dark red-brown wooden hull about forty meters, two to three stories of wooden deckhouses with railings, square brown sail, rows of oars on both sides, carved beast head at the prow, red and yellow banners. Setting @LOC_006_wide: A grey sea bay in monsoon rain: dozens of tower warships anchored close together with sails furled, low grey waves, mist hiding the horizon, no shore nearby. Action: A grey sea bay in rain: dozens of tower warships anchored close together, sails furled, decks half empty, mist hiding the horizon, no shore nearby. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out from the anchored ships to the grey sea. Sound: waves, rain, ship timbers creaking.
ACTION_START: tight on the anchored ships
ACTION_END: wide on the bay
NARRATION_KO: 해포. 내호아는 거기서 멈췄습니다. 다시는 강을 거슬러 오르지 않았습니다. 우중문을 만나러 가지도 않았습니다. 수나라의 물길은 그날로 끊겼습니다.
DIALOGUE_KO: 
SOUND: sóng, mưa, gỗ thuyền kêu.
CONTINUITY: Still 10 s. 해포.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_204_ref, LOC_006_wide

### SC_094 | 13:00–13:08 | LOC_008 (LOC_008_sui_tent) | CHAR_202, CHAR_203, SUI_COURIER | — | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Medium shot inside the tent, static
IMAGE_PROMPT: Medium shot inside the tent, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. a Sui mounted courier around 25, mud to the chest, wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, exhausted gasping face. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: Inside the hide tent on the mountainside, rain drumming on the roof: a Sui courier plastered with mud to the chest kneels and holds up a bundle of bamboo slips in both hands; the white-bearded general sits in a folding camp chair, helmet off, the grey-bearded deputy standing beside him with his own bamboo slips. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the courier kneels and lifts the slips, speaks one line; the general does not yet take them; the deputy watches. Sound: rain on the hide roof, the kneeling man's breathing, one line of Korean dialogue.
ACTION_START: courier kneeling, slips raised
ACTION_END: slips held up, general about to take them
NARRATION_KO: 그 소식은 이틀 뒤 우중문에게 닿았습니다. 삼십만은 그때 평양에서 삼십 리 떨어진 산기슭에 있었습니다. 다섯 날을 걸어온 길이었습니다.
DIALOGUE_KO: 전령: 장군, 패수에서 온 글입니다.
SOUND: mưa trên da lều, thở của người quỳ.
CONTINUITY: D5 (tin 내호아 tới sau 2 ngày). '장군, 패수에서 온 글입니다.' 우중문 tent_plain (không cầm lụa). 우문술 giáp theo script (rain_ep4, không dùng tent_ep4 no-armor).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, CHAR_203_ref, EXTRA_sui_courier_ref, PROP_021_ref, LOC_008_sui_tent_ep4

### SC_095 | 13:08–13:16 | LOC_008 (LOC_008_sui_tent) | CHAR_202, SUI_COURIER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the general, static
IMAGE_PROMPT: Close-up on the general, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. a Sui mounted courier around 25, mud to the chest, wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, exhausted gasping face. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The general reads the bamboo slips; the flush climbs his face from the neck to the temples, his white beard trembling; he lifts his eyes to the courier and growls. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: reading, the flush rising, the beard trembling, eyes lifting, one growled line. Sound: bamboo slips creaking in his grip, rain, one line of Korean dialogue.
ACTION_START: eyes on the slips
ACTION_END: eyes on the courier, face red
NARRATION_KO: 사만 중 수천. 그 숫자가 대쪽에 적혀 있었습니다. 수군은 이제 없는 것과 같았습니다.
DIALOGUE_KO: 우중문: 내호아가 배로 도망쳤다고?
SOUND: thẻ tre siết, mưa.
CONTINUITY: '내호아가 배로 도망쳤다고?'
CHAIN_FROM: SC_094
CUT_HALF: no
REFS: CHAR_202_tent_ep4, EXTRA_sui_courier_ref, LOC_008_sui_tent_ep4

### SC_096 | 13:16–13:24 | LOC_008 (LOC_008_sui_tent) | CHAR_203 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up on the deputy, static
IMAGE_PROMPT: Medium close-up on the deputy, static. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The grey-bearded deputy in his dark plain cuirass and wet fur collar does not look at the general — he looks at his own bamboo slips scored with tally marks; then he speaks, slowly and dry. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: eyes on the tally marks, then one slow dry line. Sound: rain, bamboo slips, one line of Korean dialogue.
ACTION_START: looking at the slips
ACTION_END: line spoken, eyes still down
NARRATION_KO: 우문술은 보름 전부터 같은 말을 했습니다. 이번에는 숫자가 그의 편이었습니다.
DIALOGUE_KO: 우문술: 장군. 이제 돌아가야 하오.
SOUND: mưa, thẻ tre.
CONTINUITY: '장군. 이제 돌아가야 하오.' Thẻ tre: vạch, không chữ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_203_ref, LOC_008_sui_tent_ep4
AI_RISK: chữ trên thẻ tre → chỉ vạch

### SC_097 | 13:24–13:32 | LOC_008 (LOC_008_sui_tent_door) | CHAR_202 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Over-the-shoulder from behind the general at the tent door, static
IMAGE_PROMPT: Over-the-shoulder from behind the general at the tent door, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. Setting @LOC_008_sui_tent_ep4: The doorway of a Sui general's campaign tent with the hide flap held open: rain falling on a vast camp of grey felt tents on a green mountainside, and far to the south across the rain a low hill with the faint grey line of a fortress wall, low grey cloud. Action: The general stands and lifts the hide flap: through the rain, far to the south on a low hill, the grey wall of the Goguryeo capital shows as faintly as a brush line. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static over the shoulder: the flap lifts, the rain, the faint grey line of the wall far off; he does not move. Sound: rain, the wet camp.
ACTION_START: flap rising
ACTION_END: general still, wall faint in the distance
NARRATION_KO: 삼십 리. 십이 킬로였습니다. 보이는 거리였습니다. 그리고 닿을 수 없는 거리였습니다. 배가 없었고, 밥이 없었습니다.
DIALOGUE_KO: 
SOUND: mưa, trại ướt.
CONTINUITY: 30리 = thấy được, không tới được.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, LOC_008_sui_tent_ep4

### SC_098 | 13:32–13:40 | LOC_008 (LOC_008_sui_camp_cook) | SUI_SOLDIERS_STARVING | — | PROPS: — | TYPE: video8s | 8s
SHOT: Insert: close-up on the pot, static
IMAGE_PROMPT: Insert: close-up on the pot, static. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. Setting @LOC_008_sui_camp_ep4: A cooking fire in the Sui camp in rain: a clay pot on stones over a smoking fire sheltered by a red rectangular wooden shield, mud, grey felt tents behind. Action: Sui soldiers crouch around a clay pot boiling strips of leather cut from armor lacing and a saddle; one fishes out a strip and chews; rain hisses into the fire and another man holds a red wooden shield over it. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close on the pot: a strip fished out and chewed, rain hissing, the shield held over the fire; one line muttered. Sound: fire hissing, chewing leather, rain, one line of Korean dialogue.
ACTION_START: pot boiling, hands reaching
ACTION_END: shield over the fire, man chewing
NARRATION_KO: 병사들은 가죽끈을 삶았습니다. 안장을 잘라 먹었습니다. 삼십만이 그렇게 먹고 있었습니다.
DIALOGUE_KO: 수 병사: 이게 마지막 안장이다.
SOUND: lửa xèo, nhai da, mưa.
CONTINUITY: '이게 마지막 안장이다.' Mặt lính quay đi.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, LOC_008_sui_camp_ep4
AI_RISK: mặt lính phụ → cận nồi, mặt out-focus

### SC_099 | 13:40–13:48 | LOC_008 (LOC_008_sui_tent) | CHAR_202, CHAR_203 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at the table, static
IMAGE_PROMPT: Medium shot at the table, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The general turns back inside, crushes the bamboo slips in his fist without answering, sits, and stares at the leather map on the table — the capital close, the river far behind; the deputy waits. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the slips crushed, the general sits and stares at the map, the deputy waits; no dialogue. Sound: bamboo cracking, rain.
ACTION_START: general turning in with the slips
ACTION_END: seated, staring at the map, slips crushed
NARRATION_KO: 우중문은 대답하지 않았습니다. 돌아간다는 말은 그의 입에서 나올 수 없었습니다. 황제 앞에서 큰소리를 친 사람이었기 때문입니다.
DIALOGUE_KO: 
SOUND: thẻ tre gãy, mưa.
CONTINUITY: Header script ghi PROP_001 (bản đồ Hàn) — sai vật: đây là bản đồ da Tùy → KHÔNG dán lock PROP_001, mô tả trong action.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, CHAR_203_ref, LOC_008_sui_tent_ep4

### SC_100 | 13:48–14:00 | LOC_008 (LOC_008_sui_tent) | CHAR_202 | — | PROPS: — | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: close-up under the oil lamp, very slow push-in to the eyes
IMAGE_PROMPT: Still for ken-burns: close-up under the oil lamp, very slow push-in to the eyes. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The general's face under the oil lamp, wet white beard, mud on the two breast mirrors, eyes on the map, the crushed bamboo slips in his fist. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow push-in to the eyes. Sound: rain, the lamp.
ACTION_START: face and fist
ACTION_END: tight on the eyes
NARRATION_KO: 내호아는 배로 돌아갔습니다. 우중문의 30만은 이제 혼자였습니다.
DIALOGUE_KO: 
SOUND: mưa, đèn dầu.
CONTINUITY: Still 12 s. Kết P5 → MID-ROLL 2 @14:00.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, LOC_008_sui_tent_ep4


## [Phần 6] 누구의 군대인가 (14:00–17:30) · nội điện 평양 đêm D3 · thư vua → 해모루 → 한승우 · tên dò lau · mâu thuẫn

### SC_101 | 14:00–14:10 | LOC_008 (LOC_008_sui_camp_mountain) | — | — | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial in rain, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial in rain, slow pull-out. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_sui_camp_ep4: A vast Sui camp pitched against the foot of a green forested mountain in monsoon rain, 612 AD: countless grey felt and hemp tents in ragged rows across wet trampled grass and mud, only a few thin threads of cooking smoke, red and yellow banners hanging limp, wooden watchtowers, horse lines, low grey cloud on the mountain. Action: From above in rain: a vast Sui camp against a green mountainside, grey hide tents to the foot of the hills, only a few dozen thin threads of cooking smoke among tens of thousands of tents, red banners hanging limp. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out over the camp; no dialogue, no narration. Sound: rain, high wind, sparse camp drums.
ACTION_START: tight on the tents and thin smoke
ACTION_END: wide on the camp against the mountain
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: mưa, gió trên cao, trống trại thưa.
CONTINUITY: Still 10 s. Sau mid-roll 2: không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_021_ref, LOC_008_sui_camp_ep4

### SC_102 | 14:10–14:18 | LOC_006 (LOC_006_hall_corridor) | CHAR_103, GOG_GUARDS, GOG_OFFICER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot along the veranda
IMAGE_PROMPT: Tracking shot along the veranda. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Helmet carried under one arm, black topknot loosened, smoke smudges on face and armor, right forearm wrapped in a cloth bandage, no shield, wet armor. Goguryeo palace guards in iron lamellar armor holding long spears, faces shadowed under iron helmets. a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain. Setting @LOC_006_interior: A covered wooden veranda of the palace at the Goguryeo capital at night in monsoon rain: thick round pillars lacquered deep red, dark wooden floor, rain pouring onto a stone courtyard beside it, carved wooden doors opening onto warm oil-lamp light, guards' torches. Action: Night on the palace veranda, rain pouring onto the stone courtyard: the commander strides along with his helmet under his arm, smoke-smudged face, forearm bandaged, hands his split shield to a guard at the door; the carved doors open onto oil-lamp light. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with him along the veranda: the shield handed off, the doors opening to warm light; an officer announces him with one line. Sound: rain on stone, boots on wood, the door, one line of Korean dialogue.
ACTION_START: commander striding along the veranda
ACTION_END: doors opening, commander stepping in
NARRATION_KO: 빈 절이 열린 날 밤. 고건무는 갑옷을 벗지 않고 내전으로 들어갔습니다. 대왕이 기다리고 있었습니다. 그리고 또 한 사람이 있었습니다.
DIALOGUE_KO: 고구려 장교: 고건무 장군 드십니다.
SOUND: mưa sân đá, giày trên gỗ, cửa.
CONTINUITY: D3 đêm (sau trận). '고건무 장군 드십니다.' council_ep4 (mũ cắp nách, băng tay).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_103_ambush_ep4, WPN_102_ref, LOC_006_interior

### SC_103 | 14:18–14:26 | LOC_006 (LOC_006_hall) | CHAR_102, CHAR_101, CHAR_103 | — | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Symmetrical wide shot of the hall, static
IMAGE_PROMPT: Symmetrical wide shot of the hall, static. @CHAR_102_wall_night_ep4: Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Helmet carried under one arm, black topknot loosened, smoke smudges on face and armor, right forearm wrapped in a cloth bandage, no shield, wet armor. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The audience hall: red pillars, the black throne, the great three-legged-crow banner behind; the king in the white silk crown and crimson robe with a black cloak over it sits the throne; below the dais to the left the silver-bearded general sits on a mat before a low table in wet armor; the commander drops to one knee in salute. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static symmetrical wide: the commander enters and kneels on one knee, speaks one line; the king and the general do not move. Sound: oil lamps, rain beyond the veranda, armor, one line of Korean dialogue.
ACTION_START: commander entering
ACTION_END: commander on one knee, line spoken
NARRATION_KO: 을지문덕이었습니다. 들에서 하룻밤만 성으로 들어온 것이었습니다. 삼십만은 아직 이틀 거리에 있었습니다. 그는 늘 그들보다 반나절 앞에 있었습니다.
DIALOGUE_KO: 고건무: 전하, 나곽을 되찾았습니다.
SOUND: đèn dầu, mưa ngoài hiên, giáp.
CONTINUITY: '전하, 나곽을 되찾았습니다.' 3 nhân vật có ID (wide). 을지문덕 ngồi chiếu (rain_ep4).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_102_wall_night_ep4, CHAR_101_salsu_rain_ep5, CHAR_103_ambush_ep4, PROP_012_ref, LOC_006_interior
AI_RISK: 3 nhân vật → wide đối xứng, mặt nhỏ

### SC_104 | 14:26–14:34 | LOC_006 (LOC_006_hall) | CHAR_102 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up on the king, static
IMAGE_PROMPT: Medium close-up on the king, static. @CHAR_102_wall_night_ep4: Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The king does not ask about the victory — he looks toward the general and speaks slowly, weighing every word. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static medium close-up: the king turns his eyes, speaks one slow line. Sound: oil lamps, one line of Korean dialogue.
ACTION_START: king looking down
ACTION_END: king looking toward the general, line spoken
NARRATION_KO: 대왕은 오늘의 승리를 묻지 않았습니다. 다른 것을 물었습니다.
DIALOGUE_KO: 영양왕: 대장군. 그 뇌군은 지금 어디 있는가?
SOUND: đèn dầu.
CONTINUITY: '대장군. 그 뇌군은 지금 어디 있는가?' hall_ep4 (ngồi, ref wall_night_ep4).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_102_wall_night_ep4, LOC_006_interior

### SC_105 | 14:34–14:42 | LOC_006 (LOC_006_hall) | CHAR_101 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up on the general, static
IMAGE_PROMPT: Medium close-up on the general, static. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The silver-bearded general does not raise his head high; he answers shortly, eyes still on the low table. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: one short answer, eyes on the table. Sound: rain, one line of Korean dialogue.
ACTION_START: eyes on the table
ACTION_END: eyes on the table, answer given
NARRATION_KO: 그 위로. 을지문덕은 그렇게 말했습니다. 그 아래에 있었다는 말이기도 했습니다.
DIALOGUE_KO: 을지문덕: 살수 갈대밭에 있습니다. 삼십만이 그 위로 지나갔습니다.
SOUND: mưa.
CONTINUITY: '살수 갈대밭에 있습니다. 삼십만이 그 위로 지나갔습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_salsu_rain_ep5, LOC_006_interior

### SC_106 | 14:42–14:50 | LOC_006 (LOC_006_hall) | CHAR_102 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Insert: extreme close-up on the map and the king's finger, static
IMAGE_PROMPT: Insert: extreme close-up on the map and the king's finger, static. @CHAR_102_wall_night_ep4: Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: A low table with a leather map painted in ink; the king's finger with a small gold ring settles on the line of a river to the north, slides slowly down to the capital, and stops; the oil lamp flame trembles; no words. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up: the ringed finger slides from the river line to the capital and stops; the lamp trembles. Sound: fingertip on leather, the lamp.
ACTION_START: finger on the river line
ACTION_END: finger stopped at the capital
NARRATION_KO: 살수에서 평양까지 손가락 한 마디였습니다. 그 한 마디 안에 삼십만과 92명이 있었습니다. 대왕은 92명을 세고 있었습니다.
DIALOGUE_KO: 
SOUND: ngón tay trên da, đèn.
CONTINUITY: Không thoại. Bản đồ da Goguryeo (không PROP_001).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_102_wall_night_ep4, LOC_006_interior
AI_RISK: bản đồ có chữ → 'painted in ink', không ký tự

### SC_107 | 14:50–14:58 | LOC_006 (LOC_006_hall) | CHAR_102 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up on the king, static
IMAGE_PROMPT: Medium close-up on the king, static. @CHAR_102_wall_night_ep4: Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The king lifts his head, looks at the two men before him and asks the question he has long been thinking. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the head lifts, the eyes travel between the two men, one line. Sound: lamp, rain, one line of Korean dialogue.
ACTION_START: king looking at the map
ACTION_END: king looking up, question asked
NARRATION_KO: 이기는 것은 대장군의 일이었습니다. 이긴 뒤의 일은 왕의 일이었습니다. 왕은 이긴 뒤를 먼저 물었습니다.
DIALOGUE_KO: 영양왕: 전쟁이 끝나면 저들은 누구의 군대인가?
SOUND: đèn, mưa.
CONTINUITY: '전쟁이 끝나면 저들은 누구의 군대인가?'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_102_wall_night_ep4, LOC_006_interior

### SC_108 | 14:58–15:06 | LOC_006 (LOC_006_hall) | CHAR_103 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Walk-and-talk medium shot to the low table, static camera
IMAGE_PROMPT: Walk-and-talk medium shot to the low table, static camera. @CHAR_103_ambush_ep4: Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Helmet carried under one arm, black topknot loosened, smoke smudges on face and armor, right forearm wrapped in a cloth bandage, no shield, wet armor. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The commander rises, steps to the low table and lays his bandaged hand flat on the map where the river runs; he speaks to the king straight and blunt. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he rises, steps to the table, the bandaged hand comes down on the map, one blunt line. Sound: boots on wood, leather map, one line of Korean dialogue.
ACTION_START: commander rising
ACTION_END: bandaged hand on the map, line spoken
NARRATION_KO: 고건무는 오늘 사만을 오백으로 깼습니다. 그에게 쇠수레는 필요 없었습니다. 필요 없는 것은 위험한 것이었습니다.
DIALOGUE_KO: 고건무: 흩어 보내고 쇠를 거두어야 합니다, 전하.
SOUND: giày, da bản đồ.
CONTINUITY: '흩어 보내고 쇠를 거두어야 합니다, 전하.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_103_ambush_ep4, LOC_006_interior

### SC_109 | 15:06–15:14 | LOC_006 (LOC_006_hall) | CHAR_101 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the general's hand and face, static
IMAGE_PROMPT: Close-up on the general's hand and face, static. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The general stays seated; his finger taps twice on the table — not on the map; he speaks without looking at anyone, sharp and short. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: two taps on the wood, one sharp short line, eyes on nobody. Sound: fingertip on wood, lamp, one line of Korean dialogue.
ACTION_START: finger raised
ACTION_END: finger resting after two taps, line spoken
NARRATION_KO: 을지문덕은 다음을 말하지 않았습니다. 그는 늘 지금만 말했습니다. 지금은 삼십만이 돌아올 길 위에 있었습니다.
DIALOGUE_KO: 을지문덕: 지금은 그들이 필요합니다. 그다음은 그다음에.
SOUND: ngón gõ gỗ, đèn.
CONTINUITY: '지금은 그들이 필요합니다. 그다음은 그다음에.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_salsu_rain_ep5, LOC_006_interior

### SC_110 | 15:14–15:22 | LOC_006 (LOC_006_hall) | CHAR_102, CHAR_105 | — | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Slow pan from the brush to the doorway
IMAGE_PROMPT: Slow pan from the brush to the doorway. @CHAR_102_wall_night_ep4: Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_006_interior: Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside. Action: The king writes a short column of characters with a brush on pale yellow silk, blows it dry and rolls it; at the open doorway the young officer with the white feather, mud to the thighs, the radio clipped to his armor, kneels and receives the silk in both hands. Light: Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow pan from the brush moving on the silk to the doorway where the kneeling officer takes the rolled silk in both hands; the king speaks one line. Sound: brush on silk, silk rolling, rain through the open door, one line of Korean dialogue.
ACTION_START: brush on the silk
ACTION_END: officer at the door holding the silk
NARRATION_KO: 대왕은 한 줄을 썼습니다. 답이 아니라 물음이었습니다. 해모루가 그것을 받았습니다. 그는 밤새 달릴 것이었습니다.
DIALOGUE_KO: 영양왕: 한 대장에게 전하라. 답은 네가 듣고 오라.
SOUND: bút lông, lụa, mưa cửa mở.
CONTINUITY: '한 대장에게 전하라. 답은 네가 듣고 오라.' Chữ = brush calligraphy, không ký tự thật. PROP_013 lock = chiếu chỉ (dùng nguyên văn, cuộn lụa vàng).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_102_wall_night_ep4, CHAR_105_radio_ep3, PROP_013_ref, LOC_006_interior
AI_RISK: chữ trên lụa → 'short column of brush calligraphy', không đọc được

### SC_111 | 15:22–15:34 | LOC_006 (LOC_006_river_road_night) | CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: — | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: wide on the night road, slow slide northward
IMAGE_PROMPT: Still for ken-burns: wide on the night road, slow slide northward. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_006_wide: A dirt road along the wide grey-green river at night in rain, 612 AD: mud and puddles, willows dripping, the torch-lit walls and gate towers of the Goguryeo capital shrinking in the distance behind, black hills, no other light. Action: The young officer gallops along the muddy river road in the rain at night, cloak flying, one escort rider behind leading a spare horse; the torch-lit walls of the capital shrinking behind them. Light: Night in rain, warm orange torchlight against blue-black darkness, fire reflected in wet surfaces. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide north along the road ahead of the riders. Sound: hooves in mud, rain, horses breathing.
ACTION_START: riders with the lit walls behind
ACTION_END: road ahead into darkness
NARRATION_KO: 평양에서 살수까지 이백 리. 말을 두 번 바꿨습니다. 해모루는 이 길을 이레 사이에 세 번 달릴 것이었습니다. 왕과 장군과 갈대밭 사이를 잇는 것은 이 사람 하나였습니다.
DIALOGUE_KO: 
SOUND: vó ngựa trên bùn, mưa, thở ngựa.
CONTINUITY: Still 12 s. 200리 đêm, 2 lần đổi ngựa.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, VEH_101_ref, LOC_006_wide
AI_RISK: ngựa phi đêm → still

### SC_112 | 15:34–15:42 | LOC_007 (LOC_007_island_edge) | CHAR_105, ROK_SOLDIERS | WPN_001 | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Tracking shot as he wades in
IMAGE_PROMPT: Tracking shot as he wades in. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: Grey morning: the young Goguryeo officer with the single white feather wades onto the reed island from the village side, mud to the thighs, eyes sunken, radio on his chest armor; two mud-faced sentries lower their cloth-wrapped rifles as they recognise the white feather; he nods and walks straight in. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking: he wades up out of the reeds, the sentries lower their rifles, one whispers a line, he nods and passes between them. Sound: water, reeds, a water bird, one whispered line of Korean dialogue.
ACTION_START: officer wading toward the island
ACTION_END: officer passing between the sentries
NARRATION_KO: 넷째 날 아침. 해모루는 걸어서 섬으로 들어왔습니다. 말은 마을에 두었습니다. 그는 이 부대의 규칙을 알았습니다. 소리 내는 것은 들어오지 못했습니다.
DIALOGUE_KO: 초병: 말객님.
SOUND: nước, lau, chim nước.
CONTINUITY: D4 sáng. '말객님.' Ngựa để ở làng.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, WPN_001_ref, LOC_007_island_ep4

### SC_113 | 15:42–15:50 | LOC_007 (LOC_007_shelter) | CHAR_105, CHAR_001 | — | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Medium two-shot under the reed roof, static
IMAGE_PROMPT: Medium two-shot under the reed roof, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The officer sits down before the captain, draws a rolled pale yellow silk from inside his armor — its edge wet — and holds it out with both hands. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the silk drawn from the armor, held out in both hands, one line spoken. Sound: silk, light rain, one line of Korean dialogue.
ACTION_START: officer sitting, hand inside the armor
ACTION_END: silk held out in both hands
NARRATION_KO: 이번 글은 대나무 통에 담겨 오지 않았습니다. 갑옷 속에 넣어 왔습니다. 급한 글이 아니라 무거운 글이었습니다.
DIALOGUE_KO: 해모루: 대왕의 글이오. 답을 기다리시오.
SOUND: lụa, mưa nhỏ.
CONTINUITY: '대왕의 글이오. 답을 기다리시오.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, CHAR_001_reeds_ep4, PROP_013_ref, LOC_007_island_ep4

### SC_114 | 15:50–15:58 | LOC_007 (LOC_007_shelter) | CHAR_105, CHAR_001 | — | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Close-up on the silk in the captain's hands, static, faces above out of focus
IMAGE_PROMPT: Close-up on the silk in the captain's hands, static, faces above out of focus. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The silk unrolled on the captain's mud-stained palms: a single column of brush calligraphy; he cannot read it — he looks up at the officer; the officer reads it aloud slowly in Korean. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up on the silk and hands: the captain's eyes lift off frame, the officer's voice reads one slow line. Sound: silk, rain, one line of Korean dialogue.
ACTION_START: silk unrolled on the palms
ACTION_END: captain looking up, line read
NARRATION_KO: 한승우는 한문을 읽지 못했습니다. 해모루가 읽어 주었습니다. 천사백 년 전의 왕이 천사백 년 뒤의 군인에게 물었습니다.
DIALOGUE_KO: 해모루: "그 뒤에 그대들은 누구의 군대인가?"
SOUND: lụa, mưa.
CONTINUITY: '"그 뒤에 그대들은 누구의 군대인가?"' Chữ = brush calligraphy không đọc được (OVERLAY không cần — narrator đọc).
CHAIN_FROM: SC_113
CUT_HALF: no
REFS: CHAR_105_radio_ep3, CHAR_001_reeds_ep4, PROP_013_ref, LOC_007_island_ep4
AI_RISK: chữ trên lụa → không ký tự thật

### SC_115 | 15:58–16:06 | LOC_007 (LOC_007_shelter) | CHAR_001 | — | PROPS: PROP_013, PROP_015 | TYPE: video8s | 8s
SHOT: Close-up on hands, static
IMAGE_PROMPT: Close-up on hands, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The captain says nothing; he folds the silk in four, slowly, and slides it into the chest pocket of his body armor beside the bamboo shaft of the Goguryeo arrow, then closes the pocket flap; the officer's eyes on his hands, not asking. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the silk folded twice, slid into the pocket beside the arrow shaft, the flap pressed shut. Sound: silk folding, the pocket flap, rain.
ACTION_START: silk open in the hands
ACTION_END: pocket flap closed over silk and arrow
NARRATION_KO: 그는 답 대신 글을 접었습니다. 화살 옆에 넣었습니다. 요동성 동문에서 뽑은 화살이었습니다. 이 부대가 이 땅에 남긴 첫날의 것이었습니다.
DIALOGUE_KO: 
SOUND: lụa gấp, khóa túi, mưa.
CONTINUITY: Lụa gấp tư cạnh mũi tên (PROP_015).
CHAIN_FROM: SC_114
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, PROP_013_ref, PROP_015_ref, LOC_007_island_ep4

### SC_116 | 16:06–16:14 | LOC_007 (LOC_007_island_edge) | XIANBEI_RIDER, ROK_SOLDIER | VEH_206, WPN_101 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: From the eye of a prone soldier, tilt up to a quivering arrow
IMAGE_PROMPT: From the eye of a prone soldier, tilt up to a quivering arrow. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, helmet wrapped in netting stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: On the sandbar three hundred meters out two Xianbei riders rein in and shoot blind into the reed bed — three arrows hiss through the reed tops; one thuds into the mud exactly one meter from the face of a ROK soldier lying flat; he does not move; the arrow quivers. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera at the soldier's eye: arrows hiss overhead, one thuds into the mud a meter away, camera tilts up along the quivering shaft; the soldier does not move. Sound: distant bowstrings, arrows through reeds, the thud into mud.
ACTION_START: soldier's eye, riders far out
ACTION_END: arrow quivering in the mud
NARRATION_KO: 그날 아침부터 탁발흠은 낚시를 시작했습니다. 갈대에 화살을 던지고 무엇이 튀어나오는지 보는 것이었습니다. 총소리 하나면 그는 위치를 얻을 것이었습니다.
DIALOGUE_KO: 
SOUND: dây cung xa, tên rít qua lau, cắm bùn.
CONTINUITY: Mini-contact '낚시'. 2 kỵ Tiên Ti xa trên mô cát. PROP_015 lock = tên Goguryeo (dùng như 'tên' chung — tên Tiên Ti tương tự; chấp nhận).
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, WPN_101_ref, PROP_015_ref, LOC_007_island_ep4
AI_RISK: tên cắm cận + lính → 1 mũi tên, người bất động

### SC_117 | 16:14–16:22 | LOC_007 (LOC_007_island_edge) | CHAR_006, XIANBEI_RIDER, ROK_SOLDIER | VEH_206 | PROPS: PROP_015 | TYPE: video8s | 8s
SHOT: Medium shot at ground level, static
IMAGE_PROMPT: Medium shot at ground level, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, helmet wrapped in netting stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The scout lies five meters away, one hand spread flat and pressed into the mud — the signal not to move; out on the sandbar the two riders study the reeds a while, then turn their horses south; the arrow still quivers in front of the soldier's face. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the flat hand in the mud, the riders far out turning away, the arrow still trembling; nobody moves. Sound: reeds, hooves fading, rain.
ACTION_START: riders watching, hand flat
ACTION_END: riders turning south, arrow left in the mud
NARRATION_KO: 아무것도 튀어나오지 않았습니다. 기병 둘이 돌아갔습니다. 화살은 그 자리에 남았습니다. 아무도 뽑지 않았습니다.
DIALOGUE_KO: 
SOUND: lau, vó ngựa xa dần, mưa.
CONTINUITY: Không ai rút mũi tên.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, VEH_206_ref, PROP_015_ref, LOC_007_island_ep4

### SC_118 | 16:22–16:30 | LOC_007 (LOC_007_reed_path) | CHAR_002, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Walk-and-talk tracking shot from ahead, both stooped
IMAGE_PROMPT: Walk-and-talk tracking shot from ahead, both stooped. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: The lieutenant follows the captain stooped along the muddy path between reeds, both sleeves torn off, forearms bruised; he speaks low but every word heavy. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking from ahead: the two walk stooped, the lieutenant speaks one heavy line to the captain's back. Sound: mud, reeds, rain, one line of Korean dialogue.
ACTION_START: two walking, lieutenant behind
ACTION_END: line delivered, captain slowing
NARRATION_KO: 오태민은 사흘을 참았습니다. 우리 이야기를 들은 뒤로는 하루도 참기 어려웠습니다. 그의 말은 틀리지 않았습니다.
DIALOGUE_KO: 오태민: 태오는 저기 우리에 있고, 우리는 진흙에 누워 있습니다.
SOUND: bùn, lau, mưa.
CONTINUITY: '태오는 저기 우리에 있고, 우리는 진흙에 누워 있습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, CHAR_001_reeds_ep4, LOC_007_detail

### SC_119 | 16:30–16:38 | LOC_007 (LOC_007_reed_path) | CHAR_001, CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close two-shot, static
IMAGE_PROMPT: Close two-shot, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: The captain stops and turns, face close to the lieutenant's; he repeats the sentence he once said at the fortress — slower this time. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close two-shot: the turn, the faces close, one slow line. Sound: rain, one line of Korean dialogue.
ACTION_START: captain turning
ACTION_END: faces close, line spoken
NARRATION_KO: 요동성에서 한 말이었습니다. 그때는 규칙이었습니다. 지금은 변명처럼 들렸습니다. 그도 알았습니다.
DIALOGUE_KO: 한승우: 이 싸움은 역사가 이미 이겼다. 우리는 망치지만 않으면 된다.
SOUND: mưa.
CONTINUITY: '이 싸움은 역사가 이미 이겼다. 우리는 망치지만 않으면 된다.'
CHAIN_FROM: SC_118
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_002_reeds_ep4, LOC_007_detail

### SC_120 | 16:38–16:46 | LOC_007 (LOC_007_reed_path) | CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the lieutenant, static
IMAGE_PROMPT: Close-up on the lieutenant, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: The lieutenant does not step back; the old question, with a new number in it. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: he holds his ground, one line. Sound: rain, reeds, one line of Korean dialogue.
ACTION_START: lieutenant facing the captain
ACTION_END: line spoken, jaw set
NARRATION_KO: 요동성에서는 아흔넷이었습니다. 지금은 아흔둘이었습니다. 그 둘이 오태민의 새 논거였습니다.
DIALOGUE_KO: 오태민: 역사책이 우리 94명을 지켜줍니까? 이제 92명입니다.
SOUND: mưa, lau.
CONTINUITY: '역사책이 우리 94명을 지켜줍니까? 이제 92명입니다.'
CHAIN_FROM: SC_119
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, LOC_007_detail

### SC_121 | 16:46–16:54 | LOC_007 (LOC_007_island1_k2) | CHAR_003 | VEH_001 | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Insert: medium shot, static
IMAGE_PROMPT: Insert: medium shot, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The sergeant sits on the mud-caked side skirt of the tank with the small notebook open on his knee, not looking up, and speaks toward two men standing three meters away off frame. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: pencil moving, he speaks one line without lifting his head. Sound: pencil, rain on the mud over steel, one line of Korean dialogue.
ACTION_START: sergeant writing
ACTION_END: line spoken, still writing
NARRATION_KO: 박기철은 편을 들지 않았습니다. 숫자를 들었습니다. 이십 킬로는 전차를 우리에까지 데려가지 못했습니다.
DIALOGUE_KO: 박기철: 이십 킬로. 그게 우리 편입니다.
SOUND: bút chì, mưa trên bùn xe.
CONTINUITY: '이십 킬로. 그게 우리 편입니다.' PROP_001 = sổ/bản đồ Hàn (lock có bản đồ; sổ ghi trong action).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, VEH_001_ref, PROP_001_ref, LOC_007_island_ep4

### SC_122 | 16:54–17:02 | LOC_007 (LOC_007_reed_path) | CHAR_004, CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: The medic arrives and stands between the two men without looking at either, speaking to both in short clipped words; the lieutenant's head snaps toward her. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: she steps in between, speaks one clipped line to the air, the lieutenant's head whips toward her. Sound: rain, one line of Korean dialogue.
ACTION_START: medic stepping in
ACTION_END: lieutenant staring at her
NARRATION_KO: 서아는 편을 들지 않았습니다. 본 것을 말했습니다. 본 것은 편보다 무거웠습니다.
DIALOGUE_KO: 서아: 아리가 봤습니다. 태오 발을, 몽둥이로 때렸답니다.
SOUND: mưa.
CONTINUITY: '아리가 봤습니다. 태오 발을, 몽둥이로 때렸답니다.' 한승우 ngoài khung (chỉ 2 nhân vật).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, CHAR_002_reeds_ep4, LOC_007_detail

### SC_123 | 17:02–17:10 | LOC_007 (LOC_007_reed_path) | CHAR_001, CHAR_002 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static, the two figures drawing apart in the frame
IMAGE_PROMPT: Wide, static, the two figures drawing apart in the frame. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: Silence: the lieutenant turns and walks away toward the river's edge; the captain stands watching him go, then looks down at the brown water rising through the reeds; heavy rain. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the lieutenant walks off, the captain watches, then looks down at the water; the two figures far apart; no dialogue. Sound: rain, reeds, water.
ACTION_START: two men close
ACTION_END: lieutenant far off, captain looking at the water
NARRATION_KO: 아무도 더 말하지 않았습니다. 말이 끝난 자리에 숫자만 남았습니다. 92명. 이십 킬로. 여덟 발. 그리고 강 건너 하나.
DIALOGUE_KO: 
SOUND: mưa, lau, nước.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_122
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_002_reeds_ep4, LOC_007_detail

### SC_124 | 17:10–17:18 | LOC_007 (LOC_007_island_edge) | CHAR_105 | EQP_002 | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Close-up on the officer's face and hands, static
IMAGE_PROMPT: Close-up on the officer's face and hands, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The young officer sits at the island's edge, the radio on his armor, watching the three modern soldiers scatter in three directions; he turns the black horn over in his hands — seven notches carved on its handle. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the eyes follow three figures off frame, the horn turns slowly in his hands showing the seven notches. Sound: rain, horn against armor.
ACTION_START: watching, horn still
ACTION_END: horn turned, notches showing
NARRATION_KO: 해모루는 이 다툼을 알았습니다. 모든 군대에 있는 다툼이었습니다. 쓰려는 사람과 아끼려는 사람. 그는 왕에게 무엇을 전해야 할지 아직 몰랐습니다.
DIALOGUE_KO: 
SOUND: mưa, sừng chạm giáp.
CONTINUITY: Tù và 7 vạch (PROP_018_ref). EQP_002 = radio trên giáp.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, EQP_002_ref, PROP_018_ref, LOC_007_island_ep4

### SC_125 | 17:18–17:30 | LOC_007 (LOC_007_island1) | CHAR_001 | — | PROPS: PROP_013, PROP_015 | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: extreme close-up on the chest pocket, very slow push-in
IMAGE_PROMPT: Still for ken-burns: extreme close-up on the chest pocket, very slow push-in. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The chest pocket of the captain's body armor in the rain: a corner of pale yellow silk showing beside the grey shaft of the arrow, a raindrop rolling down the digital camouflage; no face. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow push-in to the corner of silk. Sound: rain.
ACTION_START: pocket with silk and arrow
ACTION_END: tight on the silk corner
NARRATION_KO: 왕은 답을 기다렸습니다. 한승우는 답을 쓰지 않았습니다.
DIALOGUE_KO: 
SOUND: mưa.
CONTINUITY: Still 12 s. Kết P6.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, PROP_013_ref, PROP_015_ref, LOC_007_island_ep4


## [Phần 7] 북과 횃불 (17:30–21:00) · cũi mồi · 200 đuốc lùa về bãi cạn · cối 20, PZF 3, K2 2 viên · narrator im 19:39–20:11 · MID-ROLL 3 @21:00

### SC_126 | 17:30–17:38 | LOC_007 (LOC_007_south_shore) | CHAR_005, XIANBEI_RIDERS_FOOT | — | PROPS: — | TYPE: video8s | 8s
SHOT: Wide from the water toward the shore, static
IMAGE_PROMPT: Wide from the water toward the shore, static. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. Setting @LOC_007_south_camp_ep4: The sandy south shore of the shallow river in front of the Sui rear-guard camp, July monsoon: wet grey sand at the water's edge, the wide grey river and the dark reed beds of the north bank beyond, grey felt tents and ox carts behind, rain. Action: Four Xianbei warriors carry the bamboo cage out of the camp and set it on the wet sand at the water's edge in full view of the reed beds across the river; inside, the boy prisoner sits huddled, barefoot, his right foot swollen dark purple, torn camouflage, no helmet, no armor. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide from the water: the cage carried out and set down on the sand, the bearers step back; one of them says a line. Sound: cage on sand, leather thongs, rain, the river, one line of Korean dialogue.
ACTION_START: cage being carried out
ACTION_END: cage set at the water's edge, bearers stepping back
NARRATION_KO: 넷째 날 오후. 해모루는 답 없이 마을로 돌아갔습니다. 탁발흠은 우리를 갈대밭에서 보이는 강가로 옮겼습니다. 낚시는 계속됐습니다. 이번 미끼는 사람이었습니다.
DIALOGUE_KO: 선비 기병: 여기 놔라. 보이게.
SOUND: cũi đặt cát, dây da, mưa, sông.
CONTINUITY: '여기 놔라. 보이게.' 태오 cage_ep4.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_captive_ep3, VEH_206_ref, LOC_007_south_camp_ep4
AI_RISK: 4 người khiêng → wide, mặt quay đi

### SC_127 | 17:38–17:46 | LOC_007 (LOC_007_island_edge) | CHAR_006, CHAR_002 | — | PROPS: PROP_006 | TYPE: video8s | 8s
SHOT: Close two-shot at ground level, static
IMAGE_PROMPT: Close two-shot at ground level, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @PROP_006_ref: black rubber-armored 7x50 military binoculars with a neck strap and flip lens caps, dusty. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The scout looks through the binoculars, lowers them, face unchanged; the lieutenant beside him snatches the binoculars and looks: far across the water the caged figure lifts his face toward the reeds as if he knows someone is watching; the lieutenant's knuckles go white on the binoculars. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close two-shot: binoculars lowered, snatched, raised; the knuckles whiten; one line spoken through clenched teeth. Sound: rain, binoculars knocking a hat brim, one line of Korean dialogue.
ACTION_START: scout looking through binoculars
ACTION_END: lieutenant gripping the binoculars, knuckles white
NARRATION_KO: 이 킬로 밖에서도 누군지 보였습니다. 얼굴은 안 보여도 알았습니다.
DIALOGUE_KO: 오태민: 미끼인 거 압니다. 그래도 저건 태오입니다.
SOUND: mưa, ống nhòm chạm mũ.
CONTINUITY: '미끼인 거 압니다. 그래도 저건 태오입니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_ref, CHAR_002_reeds_ep4, PROP_006_ref, LOC_007_island_ep4

### SC_128 | 17:46–17:54 | LOC_007 (LOC_007_cage) | CHAR_205, CHAR_005, GOG_INTERPRETER | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot through the bamboo bars, static (2 beats: interpreter speaks, boy answers)
IMAGE_PROMPT: Medium shot through the bamboo bars, static (2 beats: interpreter speaks, boy answers). @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. A modern night-vision monocular device mounted on the front of a fox-fur cap, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud on boots. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. a captured Goguryeo interpreter around 30, thin build, hair loose and tangled, torn brown hemp jacket, hands bound in front with hemp rope, bruised face. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_south_camp_ep4: Under a dripping willow tree at the edge of the Sui rear-guard camp on the south bank: a man-sized cage of bamboo poles lashed with leather thongs under a sagging wet cloth roof, wet sand and mud, grey felt tents and ox carts behind, steady rain. Action: The Xianbei commander squats before the cage, right forearm bandaged, the night-vision device mounted on a new fox-fur cap; beside him a captured Goguryeo interpreter with bound hands and tangled hair translates his words; inside the cage the boy looks down at the sand and answers with one word. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static through the bars: beat A (0–4 s) the interpreter turns to the cage and speaks one line; beat B (4–8 s) the boy keeps his eyes on the sand and answers one word; the commander does not move. Sound: rain, bamboo creaking, a hoarse voice, two short lines of Korean dialogue.
ACTION_START: commander squatting, interpreter turning to the cage
ACTION_END: boy's one-word answer, eyes on the sand
NARRATION_KO: 탁발흠은 소년의 말을 믿지 않았습니다. 믿을 필요도 없었습니다. 소년은 대답이 아니라 미끼였습니다.
DIALOGUE_KO: 통역: 갈대밭에 네 편이 있느냐고 묻는다. / 장태오: 모릅니다.
SOUND: mưa, nan tre, giọng khàn.
CONTINUITY: Ngoại lệ 2 người nói (decisions): 통역 '갈대밭에 네 편이 있느냐고 묻는다.' / 태오 '모릅니다.' 탁발흠 bandaged_day_ep4 (mũ lông mới, kính trên mũ).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, CHAR_005_captive_ep3, EQP_001_ref, LOC_007_south_camp_ep4
AI_RISK: 3 người + song → máy qua nan tre, tĩnh

### SC_129 | 17:54–18:02 | LOC_007 (LOC_007_south_shore) | CHAR_205, XIANBEI_DEPUTY | EQP_001 | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. A modern night-vision monocular device mounted on the front of a fox-fur cap, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud on boots. a Xianbei deputy around 30 in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, a thin black mustache, listening. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_south_camp_ep4: The sandy south shore of the shallow river in front of the Sui rear-guard camp, July monsoon: wet grey sand at the water's edge, the wide grey river and the dark reed beds of the north bank beyond, grey felt tents and ox carts behind, rain. Action: The commander stands and stares a long time across the river at the reed beds; he scoops a handful of wet reeds off the sand, squeezes — water runs out — and throws it down; he speaks to his deputy. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the long stare, the reeds squeezed until water runs, thrown down, one line to the deputy. Sound: wet reeds, rain, camp noise, one line of Korean dialogue.
ACTION_START: standing, staring across the river
ACTION_END: reeds thrown down, line spoken
NARRATION_KO: 요동성에서 그는 기름을 태웠습니다. 여기는 태울 것이 없었습니다. 그래서 몰이를 골랐습니다. 초원에서 늑대를 잡던 방식이었습니다.
DIALOGUE_KO: 탁발흠: 젖은 갈대는 안 탄다. 그럼 몰아낸다. 짐승처럼.
SOUND: lau ướt, mưa, trại.
CONTINUITY: '젖은 갈대는 안 탄다. 그럼 몰아낸다. 짐승처럼.'
CHAIN_FROM: SC_128
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, VEH_206_ref, EQP_001_ref, LOC_007_south_camp_ep4

### SC_130 | 18:02–18:11 | LOC_007 (LOC_007_south_shore) | SUI_TORCHBEARERS, XIANBEI_RIDERS_FOOT | VEH_206 | PROPS: PROP_016, PROP_017 | TYPE: still_kenburns | 9s
SHOT: Still for ken-burns: wide on the night shore, slow slide along the line of fire  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: wide on the night shore, slow slide along the line of fire. Sui conscript laborers in wet hemp jackets and head cloths wading with burning torches, faces hidden by fire glare. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. @PROP_017_ref: Goguryeo war drum one meter across, faded red lacquered wooden body with bronze studs and hide heads on an X-shaped wooden stand; Sui war drum larger, bright red with gold patterns in a red lacquered frame. Setting @LOC_007_south_camp_ep4: The sandy south shore of the shallow river in front of the Sui rear-guard camp, July monsoon: wet grey sand at the water's edge, the wide grey river and the dark reed beds of the north bank beyond, grey felt tents and ox carts behind, rain. Action: Night: hundreds of torches are lit along the south shore into a ribbon of fire; a great red Sui war drum on an ox cart beaten by two men; Xianbei riders with torches wade down into the water in a curving line. Light: Night in rain, warm orange torchlight against blue-black darkness, fire reflected in wet surfaces. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide along the ribbon of torches. Sound: heavy Sui drum, torch fire, horses.
ACTION_START: drum cart and torches
ACTION_END: torch line curving into the water
NARRATION_KO: 이백 개의 횃불. 수레 위의 북. 동쪽과 남쪽에서 반달처럼 조여 서쪽 여울로 몰았습니다. 여울 어귀에는 궁수 오백이 무릎을 꿇고 기다렸습니다. 늑대가 몰려 나오는 자리였습니다.
DIALOGUE_KO: 
SOUND: trống Tùy nặng, lửa đuốc, ngựa.
CONTINUITY: Still 9 s. 200 đuốc, trống trên xe bò.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, PROP_017_ref, LOC_007_south_camp_ep4
AI_RISK: đám đông đuốc → still wide

### SC_131 | 18:11–18:19 | LOC_007 (LOC_007_reed_path) | — | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV, monochrome green, slow forward movement
IMAGE_PROMPT: Night-vision POV, monochrome green, slow forward movement. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_detail: A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain. Action: Green night-vision view moving forward along a trampled reed path — flattened stalks, a mud trail, and lying pale on the reeds a dropped black modern glove; a hand reaches into the view, picks the glove up, lifts it toward the lens; behind, dim shapes of men follow without torches; no HUD. Light: Monochrome green night-vision view with heavy grain and rain streaks, black sky, pale green highlights on wet reeds and warm bodies. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow forward POV: the trampled path, the glove picked up and lifted close, then the view moves on; no dialogue. Sound: night-vision whine, wading, rain, distant drums behind.
ACTION_START: trail ahead, glove on the reeds
ACTION_END: glove lifted, moving on
NARRATION_KO: 횃불은 미끼고 북은 소리였습니다. 진짜 사냥꾼은 어둠 속에서 걸었습니다. 이틀 전 밤의 길이 그를 섬으로 데려갔습니다.
DIALOGUE_KO: 
SOUND: kính rít, lội, mưa, trống xa sau lưng.
CONTINUITY: POV 탁발흠 (không thấy hắn — chars=[]). Găng đen Hàn rơi.
CHAIN_FROM: —
CUT_HALF: yes
REFS: EQP_001_ref, LOC_007_detail
AI_RISK: POV kính đêm → mono green; 1 bàn tay + găng

### SC_132 | 18:19–18:27 | LOC_007 (LOC_007_island1) | CHAR_001, ROK_SENTRY_PLAIN | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static, torch line far in the background
IMAGE_PROMPT: Medium shot, static, torch line far in the background. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: A sentry on the island lifts his head — drums from the east; then a line of tiny fire points appears in the reeds eight hundred meters away, slowly curving; the captain springs up from under a reed roof, helmet not on, staring at the line of fire. Light: Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the sentry's head lifts, the far fire points appear and curve, the captain rises from the shelter and stares; the sentry calls one line. Sound: drums carrying over water, distant fire, reeds, one line of Korean dialogue.
ACTION_START: sentry lifting his head
ACTION_END: captain standing, torch line curving far off
NARRATION_KO: 북소리는 동쪽에서 왔습니다. 그리고 남쪽에서도 왔습니다. 오지 않는 쪽은 서쪽뿐이었습니다. 서쪽은 여울이었습니다.
DIALOGUE_KO: 초병: 북소리… 동쪽입니다!
SOUND: trống dội qua nước, lửa xa, lau.
CONTINUITY: '북소리… 동쪽입니다!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, WPN_001_ref, LOC_007_island_ep4

### SC_133 | 18:27–18:35 | LOC_007 (LOC_007_island1_k2) | CHAR_001, CHAR_006 | VEH_001 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium two-shot on top of the mud mound, static, fire lines behind
IMAGE_PROMPT: Medium two-shot on top of the mud mound, static, fire lines behind. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The captain and the scout stand on top of the mud-caked tank looking out: two curving lines of torches close in from east and south like an embracing arm, drums beating, the only gap open to the west — toward the ford; the scout speaks without turning his head. Light: Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the two torch lines creep closer behind them, drums from two directions, the scout speaks one line without turning. Sound: drums from two sides, distant fire, rain, one line of Korean dialogue.
ACTION_START: two men on the mound, lines far
ACTION_END: lines closer, line spoken
NARRATION_KO: 몰이. 백성민의 아버지도 그렇게 멧돼지를 잡았습니다. 소리로 몰고, 길목에서 잡았습니다. 이번에는 그들이 멧돼지였습니다.
DIALOGUE_KO: 백성민: 몰이입니다. 여울로 몰고 있습니다.
SOUND: trống hai hướng, lửa, mưa.
CONTINUITY: '몰이입니다. 여울로 몰고 있습니다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, CHAR_006_ref, VEH_001_ref, LOC_007_island_ep4

### SC_134 | 18:35–18:43 | LOC_007 (LOC_007_ford_mouth) | SUI_ARCHERS, XIANBEI_OFFICER_TORCH | WPN_201 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Wide, backlit by torches behind the ranks, static — only silhouettes and bows  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide, backlit by torches behind the ranks, static — only silhouettes and bows. hundreds of Sui archers in grey-blue padded coats and pointed iron helmets kneeling in three ranks with drawn bows, seen only as backlit silhouettes. a Xianbei officer in brown leather lamellar armor and a fur-trimmed leather cap walking behind the ranks with a torch shielded by his hand. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_007_wide: The sandbar at the mouth of the ford on the south side of the shallow river at night in rain: wet grey sand, brown water on both sides, a line of wooden ford-marker stakes, the dark reed beds of the north bank across the water, torchlight glowing far off to the east. Action: On the sandbar at the mouth of the ford, in the dark, hundreds of Sui archers kneel in three ranks with bows drawn, seen only as silhouettes rimmed by torchlight from behind; a Xianbei officer walks behind them with a torch shielded by his hand, the only face lit; all bows point toward the reed beds being driven. Light: Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static backlit wide: the kneeling ranks hold, bows drawn, the officer walks along behind them with his shielded torch and calls one line. Sound: bowstrings creaking, rain, distant drums, one line of Korean dialogue.
ACTION_START: ranks kneeling, officer entering
ACTION_END: officer mid-rank, bows still drawn
NARRATION_KO: 여울 어귀. 오백 개의 활이 갈대밭 쪽을 향했습니다. 몰이가 끝나는 자리였습니다. 탁발흠은 갈대를 태우는 대신 나오는 것을 쏘기로 했습니다.
DIALOGUE_KO: 수 장교: 나오면 쏜다. 기다려.
SOUND: dây cung căng, mưa, trống xa.
CONTINUITY: '나오면 쏜다. 기다려.' Ngược sáng, không cận đám đông.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, WPN_201_ref, LOC_007_wide
AI_RISK: 500 cung thủ → ngược sáng, viền người

### SC_135 | 18:43–18:51 | LOC_007 (LOC_007_island1) | CHAR_001, ROK_SOLDIERS | EQP_002, WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the captain with the handset, static
IMAGE_PROMPT: Close-up on the captain with the handset, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The captain presses the radio handset and speaks low — the order to hold and stay silent; behind him soldiers slide into fighting holes among the reeds, pulling the cloth off their rifles. Light: Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the push-to-talk pressed, one low line; behind, out of focus, men slide into holes and unwrap rifles. Sound: push-to-talk click, drums closer, rain, one line of Korean dialogue.
ACTION_START: handset rising
ACTION_END: handset pressed, order given
NARRATION_KO: 그는 아직 침묵을 지키려 했습니다. 을지문덕의 명령이었습니다. 여기 없는 것처럼 있으라는 것이었습니다.
DIALOGUE_KO: 한승우: 전 소대, 여기는 천둥 지휘. 위치 고수. 아직 쏘지 않는다.
SOUND: PTT, trống gần hơn, mưa.
CONTINUITY: '전 소대, 여기는 천둥 지휘. 위치 고수. 아직 쏘지 않는다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, EQP_002_ref, WPN_001_ref, LOC_007_island_ep4

### SC_136 | 18:51–18:59 | LOC_007 (LOC_007_island1) | CHAR_002, ROK_SOLDIERS | WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot in the fighting holes, static
IMAGE_PROMPT: Medium shot in the fighting holes, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The torch line three hundred meters off; from it, arrows shot blind into the reeds drop scattered around the holes; a soldier takes an arrow in the shoulder and folds without a sound; the lieutenant hugs a light machine gun and looks toward the captain, not firing — waiting. Light: Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: arrows drop into the reeds, one soldier folds silently with a shaft in his shoulder, the lieutenant looks back and shouts one line. Sound: arrows falling in reeds, a stifled groan, drums, fire, one shouted line of Korean dialogue.
ACTION_START: arrows dropping, lieutenant on the gun
ACTION_END: soldier folded, lieutenant looking back
NARRATION_KO: 침묵에는 값이 있었습니다. 어깨에 화살 하나. 그 값은 아직 낼 만했습니다. 다음 값은 아니었습니다.
DIALOGUE_KO: 오태민: 중대장님!
SOUND: tên rơi lau, rên nén, trống, lửa.
CONTINUITY: '중대장님!' K3 = súng của người chết 석문령 (3화).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, WPN_003_ref, LOC_007_island_ep4
AI_RISK: tên trúng người → không cận vết

### SC_137 | 18:59–19:07 | LOC_007 (LOC_007_island1) | CHAR_001 | EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the captain's face, static
IMAGE_PROMPT: Close-up on the captain's face, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: The captain looks at the torch line, at the gap toward the ford, at the wounded man; presses the handset — the decision to break the silence. Light: Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes to the fire, to the gap, to the wounded; the handset pressed, one line. Sound: push-to-talk click, drums pounding, one line of Korean dialogue.
ACTION_START: eyes moving
ACTION_END: handset pressed, order given
NARRATION_KO: 침묵을 깨는 것도 결정이었습니다. 그는 몰이꾼을 먼저 치기로 했습니다. 여울로 나가는 것은 죽음이었기 때문입니다.
DIALOGUE_KO: 한승우: 박격포, 횃불 선. 스무 발.
SOUND: PTT, trống dồn.
CONTINUITY: '박격포, 횃불 선. 스무 발.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, EQP_002_ref, LOC_007_island_ep4

### SC_138 | 19:07–19:15 | LOC_007 (LOC_007_island1) | ROK_MORTAR_CREW | WPN_002 | PROPS: PROP_008 | TYPE: video8s | 8s
SHOT: Close on hands and tubes in the mortar pit, static
IMAGE_PROMPT: Close on hands and tubes in the mortar pit, static. ROK mortar crew in soaked mud-smeared granite-pattern digital camo uniforms and netted helmets, faces down under helmet brims, dropping finned bombs into the tubes. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. @PROP_008_ref: olive-green steel ammunition cans with hinged latched lids and carry handles, a wooden crate of 81mm mortar bombs in green plastic tubes, and a single one-meter 120mm tank round with a copper-brown semi-combustible case and black projectile. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: In a mud pit two 81mm mortars: the gunners drop bomb after bomb into the tubes without looking, orange flashes lighting the reeds, the crew counting aloud. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close on the tubes: bombs dropped and fired in fast rhythm, flashes, a crewman counting one line aloud. Sound: hollow mortar thumps in rapid rhythm, rain, one line of Korean dialogue.
ACTION_START: first bomb dropping
ACTION_END: tenth round leaving the tube
NARRATION_KO: 스무 발. 남은 오십의 절반에 가까웠습니다. 박기철은 그 숫자를 듣고 눈을 감았습니다.
DIALOGUE_KO: 사수: 여덟… 아홉… 열!
SOUND: "퉁, 퉁, 퉁" dồn dập, mưa.
CONTINUITY: '여덟… 아홉… 열!' Cối 50→30.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_002_ref, PROP_008_ref, LOC_007_island_ep4
AI_RISK: lặp chuyển động → nhịp đơn giản, tay không cận

### SC_139 | 19:15–19:23 | LOC_007 (LOC_007_island_edge) | CHAR_002, SUI_TORCHBEARERS | WPN_003 | PROPS: PROP_016, PROP_017 | TYPE: video8s | 8s
SHOT: Wide from the island toward the eastern torch line, static (keyframe = beat B)
IMAGE_PROMPT: Wide from the island toward the eastern torch line, static (keyframe = beat B). @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. Sui conscript laborers in wet hemp jackets and head cloths wading with burning torches, faces hidden by fire glare. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. @PROP_017_ref: Goguryeo war drum one meter across, faded red lacquered wooden body with bronze studs and hide heads on an X-shaped wooden stand; Sui war drum larger, bright red with gold patterns in a red lacquered frame. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: From the island: a long red line of tracer fire from a light machine gun rakes across the reeds toward the torch line; the lieutenant fires the machine gun from a hole, face lit by the muzzle flame, shouting. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): insert — mortar bursts along the torch line, torches into the water, the drum cart tipping. Beat B (4–8 s): wide from the island — a red line of tracers rakes across the reeds, the lieutenant firing with his face lit, shouting one line. Sound: mortar bursts, a long machine-gun burst, the drum stopping on one side, horses, one shouted line of Korean dialogue.
ACTION_START: bursts on the torch line (insert) / lieutenant on the gun
ACTION_END: tracers raking, lieutenant shouting
NARRATION_KO: 횃불은 물에 떨어지면 꺼졌습니다. 북은 뒤집히면 울지 않았습니다. 동쪽 고리가 흔들렸습니다.
DIALOGUE_KO: 오태민: 횃불 선! 계속!
SOUND: cối nổ liên tiếp, K3 dài, trống ngừng một bên, ngựa hí.
CONTINUITY: 2-BEAT (4+4). '횃불 선! 계속!' K3 −800.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, WPN_003_ref, PROP_017_ref, LOC_007_island_ep4
AI_RISK: 2 beat khác góc → insert riêng 4 s; tracer = vệt sáng, không cận súng
INSERT_CLIP (4 s, tách riêng): Beat A insert, 4 s, close on the eastern torch line at night in rain: mortar bombs burst along the line of torches in the flooded reeds, water and mud geysering up, torches flung into the water and going out, a great red war drum on an ox cart tipping over; no faces. Sound: rapid mortar bursts, drum toppling, horses screaming.

### SC_140 | 19:23–19:31 | LOC_007 (LOC_007_channel_south) | ROK_PZF_GUNNERS, XIANBEI_RIDERS_FOOT | WPN_005 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Over the shoulder of a kneeling gunner, static
IMAGE_PROMPT: Over the shoulder of a kneeling gunner, static. two ROK soldiers kneeling in the reeds with shoulder-fired anti-tank launchers, faces hidden under netted helmets, a third soldier crouched behind them with a spare launcher tube. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @WPN_005_ref: Panzerfaust 3 shoulder-fired anti-tank launcher, long dark olive tube with a large black conical warhead protruding from the front, detachable sight and trigger unit on the left side, shoulder rest. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_007_marsh_night_ep4: A channel of open black water south of the reed island at night in rain, walls of tall reeds on both sides, bundled-reed rafts drifting on the water carrying burning torches, orange fire reflected in the water. Action: From behind the shoulder of a kneeling gunner: across the channel three bundled-reed rafts loaded with torches and Xianbei archers push toward the island; two gunners fire their anti-tank launchers almost together — two rafts blow apart; the loader pulls the spent tube off the first gunner's sight unit and clicks a new tube on. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): two launchers fire almost together, two rafts erupt in fire on the water. Beat B (4–8 s): the loader swaps a fresh tube onto the first gunner's sight unit; the third round leaves the tube as the clip ends and the third raft bursts into flame. One shouted line. Sound: launcher whoosh, explosions on water, fire, screams, one shouted line of Korean dialogue.
ACTION_START: two gunners aimed at the rafts
ACTION_END: third round fired, third raft burning
NARRATION_KO: PZF 셋. 뗏목 셋. 남쪽 고리가 끊어졌습니다.
DIALOGUE_KO: 사수: 뗏목, 좌측! 발사!
SOUND: PZF phụt, nổ trên nước, lửa, thét.
CONTINUITY: 2-BEAT trong 1 clip (cùng góc sau vai). '뗏목, 좌측! 발사!' PZF 9→6.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, WPN_005_ref, LOC_007_marsh_night_ep4
AI_RISK: PZF + nổ → sau vai, chỉ ống và chớp lửa

### SC_141 | 19:31–19:39 | LOC_007 (LOC_007_island1) | CHAR_001, ROK_SOLDIERS, ROK_WOUNDED | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot in the holes, static
IMAGE_PROMPT: Medium shot in the holes, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_island_ep4: A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke. Action: To the north-east the torch line still closes, arrows falling thick; a soldier in a hole falls backward with a shaft in his neck and a comrade drags him down out of sight; three meters away another soldier doubles over clutching his belly, an arrow shaft between his hands; the captain looks toward the ford mouth where the largest mass of torches waits without moving. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: arrows fall, one man falls back and is dragged down, another doubles over with a shaft between his hands, the captain's head turns toward the far mass of torches. Sound: thick arrow fall, a fall, gasping, drums from the east.
ACTION_START: arrows falling, men in the holes
ACTION_END: captain looking toward the ford mouth
NARRATION_KO: 동쪽 고리는 끊기지 않았습니다. 한 사람이 목에, 한 사람이 배에 화살을 맞았습니다. 여울 어귀의 횃불 무리는 움직이지 않았습니다. 기다리는 쪽이었습니다.
DIALOGUE_KO: 
SOUND: tên dày, ngã, thở gấp, trống đông.
CONTINUITY: Người trúng tên bụng = ROK_WOUNDED (mặt tròn ~22, cần ref). Không cận vết. → NARRATOR IM 19:39–20:11.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, EXTRA_rok_wounded_ref, WPN_001_ref, LOC_007_island_ep4
AI_RISK: 2 người trúng tên → không cận vết thương, người kéo xuống khuất

### SC_142 | 19:39–19:47 | LOC_007 (LOC_007_island1_k2) | CHAR_001 | EQP_002, VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up behind the mud mound, static
IMAGE_PROMPT: Close-up behind the mud mound, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The captain kneels behind the mud-caked tank, hand on the radio handset, eyes on the mass of torches at the ford mouth; he speaks short — the order to the tank. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: handset pressed, one short order, eyes never leaving the far torches. Sound: push-to-talk click, drums, arrows hissing, one line of Korean dialogue.
ACTION_START: kneeling, hand on the handset
ACTION_END: order given
NARRATION_KO: 
DIALOGUE_KO: 한승우: 천둥 1, 여기는 천둥 지휘. 여울 어귀 횃불 무리. 두 발.
SOUND: PTT, trống, tên rít.
CONTINUITY: '천둥 1, 여기는 천둥 지휘. 여울 어귀 횃불 무리. 두 발.' Narrator im.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, EQP_002_ref, VEH_001_ref, LOC_007_island_ep4

### SC_143 | 19:47–19:55 | LOC_007 (LOC_007_island1_k2) | — | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot on the turret, static (keyframe = beat A)
IMAGE_PROMPT: Medium shot on the turret, static (keyframe = beat A). @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds, mud cracking off the turret ring, reed bundles sliding off the gun barrel, no lights. Setting @LOC_007_island_ep4: Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain. Action: The tank's turret turns under its layer of mud and reeds — mud cracking and dropping away, reed bundles sliding off the barrel; a thermal-sight view: a dense white-hot mass on the sandbar at the ford mouth. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): the turret rotates under the mud, crust cracking off, reeds sliding from the barrel; a thermal view shows a white-hot mass on the sandbar. Beat B (4–8 s): insert — close on the commander's screen with a blank readout and the gunner's hand on the handle; one line. Sound: turret motor whine, mud falling, the autoloader's clunk, one line of Korean dialogue.
ACTION_START: turret starting to turn under the mud
ACTION_END: turret on target, reeds off the barrel / screen with blank readout
NARRATION_KO: 
DIALOGUE_KO: 포수: 표적 확인. 장전 완료.
SOUND: mô-tơ tháp pháo rít, bùn rơi, máy nạp đạn tự động "쿵".
CONTINUITY: 2-BEAT (4+4). '표적 확인. 장전 완료.' [OVERLAY] '잔탄 08' lên ô trống màn hình ở beat B.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_001_ref, LOC_007_island_ep4
OVERLAY (edit): 잔탄 08 (màn hình trưởng xe, beat B — ô readout trống trong ảnh)
AI_RISK: chữ màn hình → 'small blank readout box', số OVERLAY; tháp pháo lộ khỏi bùn = 1 chuyển động
INSERT_CLIP (4 s, tách riêng): Beat B insert, 4 s, extreme close-up inside the turret at night: the commander's cold blue screen showing a small blank readout box with no readable characters, the gunner's gloved hand resting on the control handle; screen glow on the hand. Sound: cooling fans, the autoloader's heavy clunk, one line of Korean dialogue.

### SC_144 | 19:55–20:03 | LOC_007 (LOC_007_island_edge) | — | VEH_001, WPN_201 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Wide from the island across the water to the ford mouth, static (keyframe = beat B)  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide from the island across the water to the ford mouth, static (keyframe = beat B). @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds, mud cracking off the turret ring, reed bundles sliding off the gun barrel, no lights. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: From the island edge across the black water: the shell bursts in the middle of the sandbar at the ford mouth — a column of water, sand and torches thrown up, archers flung into the water, fire scattering. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–3 s): insert — the muzzle flash. Beat B (3–8 s): wide from the island — the burst on the sandbar, the column of water and torches rising and falling, fire scattering on the water; no dialogue. Sound: the 120mm report, the burst echoing back from the southern hills, rain.
ACTION_START: muzzle flash (insert) / far torch mass intact
ACTION_END: burst column falling, torches scattered
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: tiếng pháo 120mm — sấm dội khắp thung lũng sông, dội lại từ đồi nam.
CONTINUITY: 2-BEAT (3+5). [OVERLAY] '잔탄 07' góc khung cuối beat B. Không thoại.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_001_ref, WPN_201_ref, LOC_007_island_ep4
OVERLAY (edit): 잔탄 07 (nháy ở góc khung cuối beat B)
AI_RISK: nổ + đám đông → wide xa, cột nước che chi tiết
INSERT_CLIP (3 s, tách riêng): Beat A insert, 3 s, close on the tank's gun muzzle at night in rain: the 120mm gun fires — a white-orange flash tears the wet night open for one instant, reeds around the tank flattening in the blast, mud and water flung outward. Sound: the 120mm gun — thunder rolling across the river valley.

### SC_145 | 20:03–20:11 | LOC_007 (LOC_007_ford_mouth) | SUI_ARCHERS, SUI_TORCHBEARERS | WPN_201 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Medium-high aerial over the ford mouth, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Medium-high aerial over the ford mouth, static. hundreds of Sui archers in grey-blue padded coats and pointed iron helmets kneeling in three ranks with drawn bows, seen only as backlit silhouettes. Sui conscript laborers in wet hemp jackets and head cloths wading with burning torches, faces hidden by fire glare. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_007_wide: The sandbar at the mouth of the ford on the south side of the shallow river at night in rain: wet grey sand, brown water on both sides, a line of wooden ford-marker stakes, the dark reed beds of the north bank across the water, torchlight glowing far off to the east. Action: The second shell bursts left of the first: the block of archers breaks and men run in every direction into the water, torches dropping and dying in dozens; at the eastern edge of frame the other torch line also breaks — laborers flinging their torches into the water and fleeing toward the south shore; every drum stops at once. Light: Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static aerial: the second burst, the block scattering into the water, torches dying, the eastern line breaking and running; the drums stop and only rain remains. Sound: the second report, the burst, water, screams, drums stopping — then rain alone.
ACTION_START: second burst
ACTION_END: torches dying, men fleeing, silence
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: pháo thứ hai, nổ, nước, thét, trống ngừng — rồi chỉ còn mưa.
CONTINUITY: [OVERLAY] kết clip: cận màn hình trưởng xe '잔탄 06' nháy — edit chèn từ insert SC_143 (cùng ảnh, số khác). Narrator im.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, LOC_007_wide
OVERLAY (edit): 잔탄 06 (nháy — kết clip, dùng lại ảnh màn hình insert SC_143)
AI_RISK: đám đông vỡ → aerial

### SC_146 | 20:11–20:19 | LOC_007 (LOC_007_marsh_night) | CHAR_205, XIANBEI_RIDERS_FOOT | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up in the dark reeds, static
IMAGE_PROMPT: Close-up in the dark reeds, static. @CHAR_205_night_hunt_ep4: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, the right forearm wrapped in a grey cloth bandage. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_marsh_night_ep4: The flooded reed marsh of the north bank at night in rain: black water thigh-deep, walls of tall grey-green reeds dripping, no torches, no moon, a faint grey sheen on the water surface, rain streaking the darkness. Action: In the north-bank reeds the Xianbei commander rips the night-vision device from his eye — its lens flared white by the gun flash — rubs his eyes and looks toward the ford mouth with his naked eyes: only small fires on the water; around him twenty men stand dead still in the water; far off on the south shore the camp torches mill in confusion. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the device torn off and held away, eyes rubbed, the naked stare toward the far small fires; the men around him frozen; no dialogue. Sound: rain, oxen bellowing across the river, small fires.
ACTION_START: device on the eye, flash fading
ACTION_END: device in hand, staring, men frozen
NARRATION_KO: 삼십만의 뒤가 그 소리를 들었습니다. 요동성에서 열 번, 석문령에서 네 번 울린 소리였습니다. 살수에서 두 번. 탁발흠은 셌습니다. 밤눈은 잠시 멀었습니다.
DIALOGUE_KO: 
SOUND: mưa, bò rống xa qua sông, lửa nhỏ.
CONTINUITY: Kính đêm lóa trắng. bandaged_night_ep4 (băng tay phải).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_night_hunt_ep4, VEH_206_ref, EQP_001_ref, LOC_007_marsh_night_ep4

### SC_147 | 20:19–20:27 | LOC_007 (LOC_007_retreat_path) | CHAR_004, ROK_SOLDIERS, ROK_WOUNDED | VEH_001 | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Tracking shot from ahead along the flooded reed path
IMAGE_PROMPT: Tracking shot from ahead along the flooded reed path. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_marsh_night_ep4: A flooded reed path upstream from the reed island at night in rain: brown water waist-deep between walls of tall reeds, trampled stalks, no light except the faint grey sheen of the water, rain. Action: The company withdraws upstream through waist-deep water: two soldiers carry a body wrapped in an olive poncho; the medic wades beside a reed litter carrying the man with the arrow in his belly, one hand steadying the shaft; behind them the mud-caked tank creeps without lights, reeds on its top swaying. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking from ahead: the poncho-wrapped body, the litter with the medic's hand on the shaft, the dark tank creeping behind; the medic says one line to the bearers. Sound: wading, the litter, an engine at low idle, rain, one line of Korean dialogue.
ACTION_START: column entering the path
ACTION_END: column passing, tank behind
NARRATION_KO: 그들은 침묵을 잃고 밤을 얻었습니다. 동쪽 고리는 소리 하나에 풀렸습니다. 그 틈으로 삼 킬로 상류의 두 번째 섬으로 갔습니다.
DIALOGUE_KO: 서아: 흔들지 마세요. 천천히.
SOUND: lội, cáng lau, động cơ K2 ở vòng tua thấp, mưa.
CONTINUITY: '흔들지 마세요. 천천히.' 1 xác poncho + 1 người tên bụng (ROK_WOUNDED). K2 bò không đèn.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_004_braid_ep4, EXTRA_rok_wounded_ref, VEH_001_ref, LOC_007_marsh_night_ep4
AI_RISK: nhiều người + xe trong nước → tracking chậm, xe là khối tối

### SC_148 | 20:27–20:35 | LOC_008 (LOC_008_mud_road_night) | SUI_COURIER | VEH_207 | PROPS: PROP_016 | TYPE: video8s | 8s
SHOT: Tracking shot with the rider
IMAGE_PROMPT: Tracking shot with the rider. a Sui mounted courier around 25, mud to the chest, wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, exhausted gasping face. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. wooden torch with a hemp-wrapped pitch-soaked head burning yellow-orange with black smoke; fire arrows with oil-soaked cloth bound behind the head. Setting @LOC_008_hills_rain_ep4: A muddy road through low green hills at night in rain: mud and puddles, wet scrub, a column of Sui soldiers sleeping in the mud along the roadside under wet cloaks, no light except a guttering torch. Action: A Sui courier gallops south on a muddy road in the night rain, the torch in his hand gone out, his horse lathered in foam, past a column of soldiers sleeping in the mud along the roadside. Light: Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with the galloping horse past the sleeping column, the dead torch in the rider's fist. Sound: hooves, rain, the horse's ragged breathing.
ACTION_START: rider entering at a gallop
ACTION_END: rider passing the sleeping column
NARRATION_KO: 전령이 남으로 달렸습니다. 이백 리. 그가 가진 것은 한 문장이었습니다. 북쪽 마을에서 해모루도 그 소리를 들었습니다. 그는 남으로 달렸습니다.
DIALOGUE_KO: 
SOUND: vó ngựa, mưa, ngựa thở.
CONTINUITY: Header script ghi VEH_206 (Tiên Ti) — nhưng 전령 là Tùy → veo dùng VEH_207 (LOCK_PENDING) theo brief. Cần ref EXTRA_sui_courier_ref.
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_sui_courier_ref, VEH_207_ref, LOC_008_hills_rain_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)

### SC_149 | 20:35–20:43 | LOC_008 (LOC_008_sui_tent) | CHAR_202, SUI_COURIER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the kneeling courier, static, the general at the frame edge
IMAGE_PROMPT: Close-up on the kneeling courier, static, the general at the frame edge. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. a Sui mounted courier around 25, mud to the chest, wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, exhausted gasping face. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The courier kneels plastered with mud to the chest, gasping, before the general's camp chair; the deputy at the edge of frame; the courier forces out his message. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up on the courier gasping out one line; the general's hand grips the chair arm at the frame edge. Sound: ragged breathing, rain on the tent, one line of Korean dialogue.
ACTION_START: courier kneeling, gasping
ACTION_END: message delivered, head bowed
NARRATION_KO: 
DIALOGUE_KO: 전령: 뒤에서 천둥이 울렸습니다. 뇌군이 우리 뒤에 있습니다.
SOUND: thở dốc, mưa trên lều.
CONTINUITY: '뒤에서 천둥이 울렸습니다. 뇌군이 우리 뒤에 있습니다.' D5 đêm. 우문술 ở mép (không đính lock — chỉ mép khung).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, EXTRA_sui_courier_ref, LOC_008_sui_tent_ep4

### SC_150 | 20:43–20:51 | LOC_008 (LOC_008_sui_tent) | CHAR_202, CHAR_203 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the leather map and two hands, static
IMAGE_PROMPT: Close-up on the leather map and two hands, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The general's face drains; he stands, goes to the leather map and sets a trembling finger on the river behind him; the deputy's eyes go to that finger and he says nothing. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close on the map: the trembling finger comes down on the river, the deputy's hand rests still beside the map; no dialogue. Sound: rain, breathing.
ACTION_START: map empty, finger approaching
ACTION_END: finger on the river, trembling
NARRATION_KO: 우중문의 손가락이 살수에 놓였습니다. 그의 뒤였습니다. 앞에는 평양이 있었고, 뒤에는 천둥이 있었습니다. 밥은 어디에도 없었습니다.
DIALOGUE_KO: 
SOUND: mưa, thở.
CONTINUITY: Bản đồ da Tùy (mực), không chữ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, CHAR_203_ref, LOC_008_sui_tent_ep4
AI_RISK: bản đồ → 'painted in ink', không ký tự

### SC_151 | 20:51–21:00 | LOC_008 (LOC_008_gog_camp_hill) | CHAR_101, CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_018 | TYPE: still_kenburns | 9s
SHOT: Still for ken-burns: medium shot under the awning, slow push-in to the general's face
IMAGE_PROMPT: Still for ken-burns: medium shot under the awning, slow push-in to the general's face. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_008_hills_rain_ep4: A Goguryeo field camp on a green hill in monsoon rain: hemp tents with wooden poles, a large tent with an awning of oiled cloth, black three-legged crow banners hanging wet, saddled horses in iron lamellar barding waiting in the rain, wet grass, low grey cloud. Action: Grey dawn rain on a green hill: the silver-bearded general stands under an oiled-cloth awning in wet armor; before him the young officer kneels on one knee, mud to the chest, just off his horse, reporting; behind, Goguryeo cavalry wait saddled; on the general's face the smallest trace of a smile. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in from the two men to the general's face and the trace of a smile; his line is heard over the still. Sound: rain, horses, wind, one line of Korean dialogue.
ACTION_START: officer kneeling, general standing
ACTION_END: tight on the general's face
NARRATION_KO: 을지문덕에게 그 소리는 하루 늦게 닿았습니다. 말 탄 사람의 입으로. 그는 화내지 않았습니다. 뒤에서 천둥이 울렸다. 뇌군이 우리 뒤에 있다. 그 문장은 우중문에게는 공포였고, 그에게는 채찍이었습니다.
DIALOGUE_KO: 을지문덕: 좋소. 서두르게 하시오.
SOUND: mưa, ngựa, gió.
CONTINUITY: Still 9 s. '좋소. 서두르게 하시오.' → MID-ROLL 3 @21:00.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_salsu_rain_ep5, CHAR_105_radio_ep3, VEH_101_ref, PROP_018_ref, LOC_008_hills_rain_ep4


## [Phần 8] 여섯 발, 이게 답니다 (21:00–24:00) · đảo lau 2 · 잔탄 06 · 탁발흠 đếm vỏ đạn · kế cứu 태오

### SC_152 | 21:00–21:10 | LOC_007 (LOC_007_island2) | — | VEH_001 | PROPS: PROP_020 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium-wide, slow pull-out
IMAGE_PROMPT: Still for ken-burns: medium-wide, slow pull-out. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: Grey dawn on the second reed island — a low sand mound among tall reeds, rain; in the foreground a body wrapped in an olive poncho and tied with cord lies on broken reeds, combat boots showing; behind it the tank is a fresh mound of mud, reeds not yet planted over it. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out from the wrapped body to the island and the fresh mud mound; no dialogue, no narration. Sound: rain, a water bird, silence.
ACTION_START: tight on the poncho-wrapped body
ACTION_END: wide on the island
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: mưa, chim nước, im.
CONTINUITY: Still 10 s. Sau mid-roll 3: không thoại. Đảo lau 2 (sub-lock island2).
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, LOC_007_island_ep4

### SC_153 | 21:10–21:18 | LOC_007 (LOC_007_island2_k2) | CHAR_003 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Insert: extreme close-up inside the turret, static
IMAGE_PROMPT: Insert: extreme close-up inside the turret, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: Inside the tank turret the commander's screen glows cold blue: two small blank readout boxes with no readable characters; the sergeant's torn-gloved hand rests on the edge of the screen. Light: Night inside the turret, cold blue-white glow of a screen on hands and metal, deep black shadows. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up: the screen glow, the hand resting on its edge, nothing moves. Sound: cooling fans, rain on the hull above.
ACTION_START: hand on the screen edge
ACTION_END: hand on the screen edge
NARRATION_KO: 다섯째 날 새벽. 전차는 여섯이라고 말했습니다. 기계는 거짓말을 하지 않았습니다. 사람이 그것을 소리 내어 읽어야 했습니다.
DIALOGUE_KO: 
SOUND: quạt điện tử, mưa trên nóc.
CONTINUITY: [OVERLAY] '잔탄 06' + '위성 0개' vào 2 ô trống. Xe vẫn là mô bùn ngoài (VEH_001_mud để nhắc).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, VEH_001_ref, LOC_007_island_ep4
OVERLAY (edit): 잔탄 06 · 위성 0개 (hai ô readout trống trên màn hình trưởng xe)
AI_RISK: chữ màn hình → ô trống, số OVERLAY

### SC_154 | 21:18–21:26 | LOC_007 (LOC_007_island2_k2) | CHAR_003, CHAR_001 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle two-shot, static
IMAGE_PROMPT: Low angle two-shot, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The sergeant climbs out of the turret hatch and sits on the muddy top of the tank looking down at the captain standing below; both faces muddy; he speaks slowly, in pieces. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the sergeant emerges, sits on the mud, looks down, speaks one line in pieces. Sound: rain, mud, one line of Korean dialogue.
ACTION_START: sergeant climbing out of the hatch
ACTION_END: seated on the mud, line spoken
NARRATION_KO: 여덟에서 여섯. 두 발의 값은 밤 하나였습니다. 그리고 사람 둘이었습니다.
DIALOGUE_KO: 박기철: 여섯 발. 이게 답니다.
SOUND: mưa, bùn.
CONTINUITY: '여섯 발. 이게 답니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, CHAR_001_reeds_ep4, VEH_001_ref, LOC_007_island_ep4

### SC_155 | 21:26–21:34 | LOC_007 (LOC_007_island2) | CHAR_003 | WPN_005, WPN_002, WPN_001 | PROPS: PROP_008 | TYPE: video8s | 8s
SHOT: Walk-and-talk tracking shot along the equipment under ponchos
IMAGE_PROMPT: Walk-and-talk tracking shot along the equipment under ponchos. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @WPN_005_ref: Panzerfaust 3 shoulder-fired anti-tank launcher, long dark olive tube with a large black conical warhead protruding from the front, detachable sight and trigger unit on the left side, shoulder rest. @WPN_002_ref: 81mm KM187 mortar, dark olive tube on a bipod with traversing handwheels, round aluminum baseplate, small optical sight, finned mortar bombs in green plastic tubes beside it. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. @PROP_008_ref: olive-green steel ammunition cans with hinged latched lids and carry handles, a wooden crate of 81mm mortar bombs in green plastic tubes, and a single one-meter 120mm tank round with a copper-brown semi-combustible case and black projectile. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: The sergeant climbs down and walks along the equipment stacked under ponchos, his hand touching six launcher tubes, three mortar crates, rows of rifle magazines laid out by man, reading them off like a storekeeper. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with him along the stacks: the hand touches the tubes, the crates, the magazines, one line read off. Sound: launcher tubes knocking together, rain, one line of Korean dialogue.
ACTION_START: sergeant at the launcher tubes
ACTION_END: sergeant at the magazines
NARRATION_KO: 박격포는 오십에서 서른. PZF는 아홉에서 여섯. 이 섬에 오면서 준 것은 없고 쓴 것만 있었습니다.
DIALOGUE_KO: 박기철: PZF 여섯. 박격포 서른. 소총은 탄창 넷씩.
SOUND: ống PZF gõ nhau, mưa.
CONTINUITY: 'PZF 여섯. 박격포 서른. 소총은 탄창 넷씩.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, WPN_005_ref, WPN_002_ref, WPN_001_ref, PROP_008_ref, LOC_007_island_ep4

### SC_156 | 21:34–21:42 | LOC_007 (LOC_007_island2_k2) | CHAR_003, CHAR_001 | EQP_002, VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The sergeant turns back, taps a finger on the backpack radio and then on the mud over the tank's side skirt; the captain listens and gives one nod. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: a tap on the radio, a tap on the muddy skirt, one line; the captain nods once. Sound: finger on plastic, on mud over steel, rain, one line of Korean dialogue.
ACTION_START: sergeant turning back
ACTION_END: captain's single nod
NARRATION_KO: 간밤에 삼 킬로를 움직였습니다. 평지였습니다. 산길로 센 이십은 이십이었습니다. 적은 쪽으로 세는 사람의 셈이었습니다.
DIALOGUE_KO: 박기철: 무전기 사십 퍼센트. 연료는 산길 기준 이십, 그대로입니다.
SOUND: ngón gõ nhựa, gõ thép qua bùn.
CONTINUITY: '무전기 사십 퍼센트. 연료는 산길 기준 이십, 그대로입니다.'
CHAIN_FROM: SC_155
CUT_HALF: no
REFS: CHAR_003_rain_ep3, CHAR_001_reeds_ep4, EQP_002_ref, VEH_001_ref, LOC_007_island_ep4

### SC_157 | 21:42–21:50 | LOC_007 (LOC_007_aid) | CHAR_004, ROK_WOUNDED | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Close-up under the reed roof, static
IMAGE_PROMPT: Close-up under the reed roof, static. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: Under the reed roof the wounded soldier lies on his back, the arrow shaft cut short and a pressure bandage around his belly, face white with sweat; the medic presses a morphine autoinjector into his thigh and holds his hand, her eyes on the bandage darkening. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the autoinjector pressed, the hand held, the eyes on the bandage, one soft line. Sound: rain, quick shallow breathing, the injector click, one line of Korean dialogue.
ACTION_START: injector at the thigh
ACTION_END: hand held, eyes on the bandage
NARRATION_KO: 배에 박힌 화살은 뽑지 않았습니다. 뽑으면 피가 났고, 두면 열이 났습니다. 항생제는 없었습니다. 남은 것은 모르핀과 시간이었습니다.
DIALOGUE_KO: 서아: 모르핀 하나. 참아요.
SOUND: mưa, thở gấp, ống tiêm bấm.
CONTINUITY: '모르핀 하나. 참아요.' Morphine 10→9. ROK_WOUNDED (ref).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, EXTRA_rok_wounded_ref, PROP_009_ref, LOC_007_island_ep4
AI_RISK: vết thương → băng ép + cán tên ngắn, không máu cận

### SC_158 | 21:50–21:58 | LOC_007 (LOC_007_aid) | CHAR_106, CHAR_004, ROK_WOUNDED | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot under the reed roof, static
IMAGE_PROMPT: Medium shot under the reed roof, static. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: The old blacksmith comes in, sets a wooden bowl of cold herb liquid beside the wounded man, looks at him one beat, then at the medic — and tells her the truth, not gently. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the bowl set down, the look at the wounded man, the look at the medic, one blunt line. Sound: wooden bowl on mud, rain, one line of Korean dialogue.
ACTION_START: old man entering with the bowl
ACTION_END: line spoken to the medic
NARRATION_KO: 을보는 거짓말을 하지 않는 노인이었습니다. 쇠에게도, 사람에게도.
DIALOGUE_KO: 을보: 이건 열을 내리지. 뱃속 화살은… 못 내리네.
SOUND: bát gỗ đặt, mưa.
CONTINUITY: '이건 열을 내리지. 뱃속 화살은… 못 내리네.'
CHAIN_FROM: SC_157
CUT_HALF: no
REFS: CHAR_106_ref, CHAR_004_braid_ep4, EXTRA_rok_wounded_ref, LOC_007_island_ep4

### SC_159 | 21:58–22:08 | LOC_007 (LOC_007_aid) | CHAR_004 | — | PROPS: PROP_009 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: extreme close-up on the medic's notebook, slow push-in
IMAGE_PROMPT: Still for ken-burns: extreme close-up on the medic's notebook, slow push-in. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: A small medical notebook with rain-swollen edges, blurred pencil lines; the medic's hand holds the pencil stopped over the last line; behind, out of focus, the bowl of cold herb liquid. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the pencil stopped on the last line. Sound: rain, the wounded man's breathing.
ACTION_START: notebook and hand
ACTION_END: tight on the pencil tip
NARRATION_KO: 서아는 알았습니다. 항생제 없는 배의 상처가 어디로 가는지. 이틀, 길면 사흘. 그녀는 그것을 수첩에 적지 않았습니다. 대신 모르핀을 아홉이라 적었습니다.
DIALOGUE_KO: 
SOUND: mưa, thở của người bệnh.
CONTINUITY: Still 10 s. [OVERLAY] '항생제 0 · 모르핀 9 · 붕대…' — ảnh chỉ nét chì mờ.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, PROP_009_ref, LOC_007_island_ep4
OVERLAY (edit): 항생제 0 · 모르핀 9 · 붕대… (sổ y tế 서아; ken-burns đẩy vào số 0)
AI_RISK: chữ → blurred pencil, OVERLAY

### SC_160 | 22:08–22:16 | LOC_007 (LOC_007_island1_abandoned) | CHAR_205, XIANBEI_RIDERS_FOOT | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the shell base and the face, static
IMAGE_PROMPT: Close-up on the shell base and the face, static. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. A modern night-vision monocular device mounted on the front of a fox-fur cap, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud on boots. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_island_ep4: The abandoned reed island by grey morning light in rain: empty reed shelters collapsing, trampled and flattened reeds, an empty sandbagged mortar pit, a deep pair of tank track ruts filled with brown water leading away into the reeds, no fire. Action: The Xianbei commander walks the abandoned first island: an empty mortar pit, flattened reeds, deep tank track ruts in the mud; he stoops and picks up the base of a spent 120mm case — a steel ring as wide as his hand, black with soot — and turns it on his fingers, counting on the others; his men rummage far behind. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the steel ring lifted from the mud and turned on the fingers, the other hand counting, one line. Sound: rain, steel against mud, distant rummaging, one line of Korean dialogue.
ACTION_START: stooping to the shell base in the mud
ACTION_END: ring turning on the fingers, line spoken
NARRATION_KO: 아침이 되자 탁발흠은 빈 섬을 걸었습니다. 늘 싸움 뒤에 그 자리를 걸었습니다. 요동성에서도, 석문령에서도.
DIALOGUE_KO: 탁발흠: 열 번, 네 번, 그리고 두 번. 열여섯이다.
SOUND: mưa, thép chạm bùn, lính Tiên Ti lục lọi xa.
CONTINUITY: '열 번, 네 번, 그리고 두 번. 열여섯이다.' Header ghi VEH_001 (vết) — xe đã đi: KHÔNG dán lock VEH_001, chỉ vết xích trong action.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, VEH_206_ref, EQP_001_ref, LOC_007_island_ep4
AI_RISK: vỏ đạn 120mm cận → 'steel ring as wide as his hand, black with soot', không chữ

### SC_161 | 22:16–22:24 | LOC_007 (LOC_007_island1_abandoned) | CHAR_205 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. A modern night-vision monocular device mounted on the front of a fox-fur cap, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud on boots. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_island_ep4: The abandoned reed island by grey morning light in rain: empty reed shelters collapsing, trampled and flattened reeds, an empty sandbagged mortar pit, a deep pair of tank track ruts filled with brown water leading away into the reeds, no fire. Action: The commander drops the shell base into the mud and lifts his eyes upstream along the track ruts; he speaks to himself. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the ring drops, the eyes lift upstream, one line spoken to himself. Sound: the ring in mud, rain, one line of Korean dialogue.
ACTION_START: ring dropping
ACTION_END: looking upstream
NARRATION_KO: 그는 천둥이 몇 번 남았는지 몰랐습니다. 다만 하나를 알았습니다. 세어지는 것은 끝이 있는 법이었습니다.
DIALOGUE_KO: 탁발흠: 천둥도 센다. 언젠가는 마른다.
SOUND: vỏ đạn rơi bùn, mưa.
CONTINUITY: '천둥도 센다. 언젠가는 마른다.'
CHAIN_FROM: SC_160
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, EQP_001_ref, LOC_007_island_ep4

### SC_162 | 22:24–22:32 | LOC_007 (LOC_007_island_edge) | CHAR_006 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot following him from the downstream reeds, camera panning with him
IMAGE_PROMPT: Medium shot following him from the downstream reeds, camera panning with him. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The scout comes back from the downstream edge of the reeds wiping his knife blade on his trouser leg, saying nothing; behind him in the reeds a fox-fur cap floats upside down on the water. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Pan with him as he walks in wiping the blade, the cap floating behind; he says one line. Sound: reeds, water, rain, one line of Korean dialogue.
ACTION_START: scout emerging from the reeds
ACTION_END: scout past camera, cap floating behind
NARRATION_KO: 척후 하나가 전차 자국을 따라 상류로 올라왔습니다. 백성민이 갈대에서 기다렸습니다. 세 번째 적이 갈대 밑에 묻혔습니다. 총소리 없이.
DIALOGUE_KO: 백성민: 척후 하나. 자국 따라왔습니다.
SOUND: lau, nước, mưa.
CONTINUITY: '척후 하나. 자국 따라왔습니다.' Đảo lau 2 mép hạ lưu.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_ref, WPN_001_ref, LOC_007_island_ep4

### SC_163 | 22:32–22:40 | LOC_007 (LOC_007_sandtable) | CHAR_107, CHAR_001, CHAR_006 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Top-down shot onto the mud sand table, static
IMAGE_PROMPT: Top-down shot onto the mud sand table, static. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain. Action: From above: the girl kneels and draws with a reed stalk in wet mud — an island, a channel, a sandbar, a reed path, and a circle for the camp's water point; the captain and the scout watch from either side; the old man's sandals at the frame edge behind her. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static top-down: the reed stalk draws the island, channel, sandbar, path, then the circle; the girl says one line. Sound: reed on mud, rain, one line of Korean dialogue.
ACTION_START: stalk starting the drawing
ACTION_END: circle drawn, line spoken
NARRATION_KO: 아리는 아낙들만 아는 길을 그렸습니다. 길 끝에 적의 물 긷는 자리와 우리가 있었습니다.
DIALOGUE_KO: 아리: 물 긷는 데예요. 새벽엔 졸아요, 지키는 사람들.
SOUND: cọng lau vạch bùn, mưa.
CONTINUITY: '물 긷는 데예요. 새벽엔 졸아요, 지키는 사람들.' 을보 chỉ là dép ở mép (không lock).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_001_reeds_ep4, CHAR_006_ref, LOC_007_island_ep4
AI_RISK: 3 nhân vật → top-down, chỉ tay và bàn cát

### SC_164 | 22:40–22:48 | LOC_007 (LOC_007_sandtable) | CHAR_006, CHAR_001 | WPN_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot over the sand table, static
IMAGE_PROMPT: Medium shot over the sand table, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @WPN_001_ref: South Korean K2C1 assault rifle, black, quad Picatinny rail handguard, side-folding skeleton stock, 30-round steel magazine, small red-dot sight, two-point sling. Setting @LOC_007_island_ep4: A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain. Action: The scout lays his fixed-blade knife on the mud beside the circle; pulls the magazine from his rifle and sets rifle and magazine aside — not taking the gun; looks at the captain. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: knife laid by the circle, magazine pulled, rifle set aside, the look at the captain, one line. Sound: knife on mud, magazine release, rain, one line of Korean dialogue.
ACTION_START: knife going down beside the circle
ACTION_END: rifle set aside, looking at the captain
NARRATION_KO: 총을 놓고 가는 것. 백성민에게는 어려운 일이 아니었습니다. 그는 총보다 칼을 먼저 배운 사람이었습니다.
DIALOGUE_KO: 백성민: 안개 걷히기 전에 갑니다. 셋만. 총은 놓고.
SOUND: dao đặt bùn, băng đạn tháo.
CONTINUITY: '안개 걷히기 전에 갑니다. 셋만. 총은 놓고.'
CHAIN_FROM: SC_163
CUT_HALF: no
REFS: CHAR_006_ref, CHAR_001_reeds_ep4, WPN_001_ref, LOC_007_island_ep4
AI_RISK: tháo băng đạn → tay đơn giản, súng không chĩa

### SC_165 | 22:48–22:56 | LOC_007 (LOC_007_island2) | CHAR_002 | WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Insert: close-up on hands and a profile, static
IMAGE_PROMPT: Insert: close-up on hands and a profile, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: The lieutenant sits in a reed hole three meters from the sand table wiping the light machine gun with a rag, not looking up — hearing everything; profile of his face. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the rag moves along the gun, the profile does not lift. Sound: rag on steel, rain, low voices from the sand table.
ACTION_START: rag on the gun
ACTION_END: rag on the gun, head still down
NARRATION_KO: 선택은 둘이었습니다. 셋을 보내고 하나를 데려오는 것. 아니면 아흔둘이 다 숨는 것. 셋이 잡히면 위치도 잡히는 것이었습니다.
DIALOGUE_KO: 
SOUND: giẻ trên thép, mưa, giọng bàn cát nhỏ.
CONTINUITY: Insert.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_003_ref, LOC_007_island_ep4

### SC_166 | 22:56–23:04 | LOC_007 (LOC_007_sandtable) | CHAR_001 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static, then a tilt down to the sand table
IMAGE_PROMPT: Medium shot, static, then a tilt down to the sand table. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain. Action: The captain looks at the mud mound of the tank, at the aid shelter, at the river; then bends to the sand table and sets his finger on the circle. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static then tilt: the three looks, the bend, the finger on the circle, one line. Sound: rain, one line of Korean dialogue.
ACTION_START: captain looking at the tank
ACTION_END: finger on the circle
NARRATION_KO: 세 번째 결정이었습니다. 첫째는 침묵, 둘째는 두 발. 이번에는 탄약을 아끼고 사람을 보내는 것이었습니다.
DIALOGUE_KO: 한승우: 쏠 순 없어도 보낼 순 있다.
SOUND: mưa.
CONTINUITY: '쏠 순 없어도 보낼 순 있다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, VEH_001_ref, LOC_007_island_ep4

### SC_167 | 23:04–23:12 | LOC_007 (LOC_007_sandtable) | CHAR_002 | WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_007_island_ep4: A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain. Action: The lieutenant rises from his hole with the machine gun on his shoulder and steps to the sand table; he asks — short. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he rises, steps in, one short line. Sound: boots in mud, one line of Korean dialogue.
ACTION_START: rising from the hole
ACTION_END: at the sand table, line spoken
NARRATION_KO: 그는 셋 중 하나가 되고 싶었습니다. 진흙에 누워 있는 것은 이제 그만이었습니다.
DIALOGUE_KO: 오태민: 제가 가겠습니다.
SOUND: giày trên bùn.
CONTINUITY: '제가 가겠습니다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_003_ref, LOC_007_island_ep4

### SC_168 | 23:12–23:20 | LOC_007 (LOC_007_sandtable) | CHAR_001, CHAR_002 | WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_007_island_ep4: A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain. Action: The captain does not refuse at once — he points north, where the reeds open onto the ford upstream of the island, and gives him the thing that matters more. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the arm points north, one line. Sound: rain, one line of Korean dialogue.
ACTION_START: captain facing the lieutenant
ACTION_END: arm pointing north, line spoken
NARRATION_KO: 그는 오태민에게 가장 중요한 자리를 주었습니다. 셋이 돌아올 길이었습니다. 그리고 그 뒤에 올 것의 길이기도 했습니다.
DIALOGUE_KO: 한승우: 넌 북쪽 여울을 지켜.
SOUND: mưa.
CONTINUITY: '넌 북쪽 여울을 지켜.'
CHAIN_FROM: SC_167
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_002_reeds_ep4, WPN_003_ref, LOC_007_island_ep4

### SC_169 | 23:20–23:28 | LOC_007 (LOC_007_island2) | CHAR_002 | WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot following him into the reeds
IMAGE_PROMPT: Tracking shot following him into the reeds. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: The lieutenant looks at the captain one beat, nods once — no argument; turns and wades north with the machine gun on his shoulder, the reeds closing behind him. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking: the beat, the single nod, the turn, wading away until the reeds close. Sound: wading, reeds, rain.
ACTION_START: lieutenant facing the captain
ACTION_END: reeds closing behind him
NARRATION_KO: 오태민은 처음으로 묻지 않았습니다. 왜냐고도, 어째서냐고도. 그는 북쪽 여울로 갔습니다.
DIALOGUE_KO: 
SOUND: lội, lau, mưa.
CONTINUITY: Không cãi lần đầu.
CHAIN_FROM: SC_168
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_003_ref, LOC_007_island_ep4

### SC_170 | 23:28–23:36 | LOC_007 (LOC_007_island2) | CHAR_106, CHAR_006 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: The old blacksmith pulls three coarse hemp jackets and three pairs of straw sandals from a cloth bundle and tosses them to the scout, squinting at the scout's sharp angular face. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the jackets and sandals tossed over, the squint, one line. Sound: cloth thrown, straw sandals, rain, one line of Korean dialogue.
ACTION_START: old man opening the bundle
ACTION_END: scout holding the jackets, old man squinting
NARRATION_KO: 옷은 마을 아낙들의 남편 것이었습니다. 남편들은 요동으로 갔습니다. 옷만 남아 있었습니다.
DIALOGUE_KO: 을보: 이 옷 입으면 우리 사람 같겠구먼. 얼굴만 빼고.
SOUND: vải ném, dép rơm, mưa.
CONTINUITY: '이 옷 입으면 우리 사람 같겠구먼. 얼굴만 빼고.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_ref, CHAR_006_ref, LOC_007_island_ep4

### SC_171 | 23:36–23:48 | LOC_007 (LOC_007_island2) | — | — | PROPS: PROP_020 | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: close-up flat lay on broken reeds, slow lateral slide
IMAGE_PROMPT: Still for ken-burns: close-up flat lay on broken reeds, slow lateral slide. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: Laid out on broken reeds: three folded hemp jackets, three pairs of straw sandals, one modern fixed-blade knife and two Goguryeo knives, a strip of dark cloth for the head, a fistful of black mud; rain speckling everything. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow lateral slide across the laid-out items. Sound: rain.
ACTION_START: jackets and sandals
ACTION_END: knives, cloth and mud
NARRATION_KO: 총도, 야시경도, 무전기도 가져가지 않기로 했습니다. 천사백 년 전의 옷과 칼과 안개. 그것이 이번 작전의 전부였습니다. 천사백 년 뒤의 군대가 가장 오래된 방법을 골랐습니다.
DIALOGUE_KO: 
SOUND: mưa.
CONTINUITY: Still 12 s.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_007_island_ep4

### SC_172 | 23:48–24:00 | LOC_007 (LOC_007_island_edge) | CHAR_107 | — | PROPS: — | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: medium close-up, slow push-in to the face
IMAGE_PROMPT: Still for ken-burns: medium close-up, slow push-in to the face. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The girl sits at the water's edge at grey dawn, the olive scarf around her shoulders, scratched hands clasped on her knees, looking across at the south bank through thin mist beginning to rise. Light: Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to her face. Sound: rain thinning, the river.
ACTION_START: girl seated at the water's edge
ACTION_END: tight on the face
NARRATION_KO: 여섯 발은 쓰지 않기로 했습니다. 대신 칼 한 자루와 소녀 하나를 보내기로 했습니다.
DIALOGUE_KO: 
SOUND: mưa nhỏ dần, sông.
CONTINUITY: Still 12 s. Kết P8.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, LOC_007_island_ep4


## [Phần 9] 여수장우중문시 (24:00–27:30) · [史] thơ → 우중문 · 방진 · 해모루 kể thơ · kế sương · 「반이 건널 때까지」 · MID-ROLL 4 @27:30

### SC_173 | 24:00–24:10 | LOC_008 (LOC_008_gog_tent) | CHAR_101 | — | PROPS: PROP_014 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium close-up, slow push-in to the hand with the brush
IMAGE_PROMPT: Still for ken-burns: medium close-up, slow push-in to the hand with the brush. @CHAR_101_ref: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Helmet removed, gray topknot exposed, cloak over shoulders, brush in hand. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. Setting: Interior of a Goguryeo commander's field tent at night in rain: oiled hemp walls, rain drumming on the cloth, a low wooden table, a clay oil lamp, a set of iron lamellar armor laid beside the table, a black three-legged crow banner, reed mats. Action: Night in the tent, rain on the cloth: the silver-bearded general, helmet off, grey topknot, armor laid beside him, sits before a low table with a brush over a small ivory silk sheet under an oil lamp; four short columns of brush calligraphy taking shape. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the hand holding the brush over the silk. Sound: rain on cloth, the brush, the lamp.
ACTION_START: general at the table
ACTION_END: tight on the brush hand
NARRATION_KO: 여섯째 날. 일곱 번 지고, 사만을 깨고, 천둥이 두 번 울렸다는 말을 듣고 나서 을지문덕은 붓을 들었습니다. 그는 칼 대신 시를 보내기로 했습니다. 다섯 글자 넉 줄이었습니다.
DIALOGUE_KO: 
SOUND: mưa trên bạt, bút lông, đèn.
CONTINUITY: Still 10 s. D5→D6 đêm. helmet_off_tent (ref CHAR_101_ref). PROP_014 lock (thơ nhỏ lụa ngà).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_ref, PROP_014_ref
AI_RISK: chữ → brush calligraphy không rõ ký tự

### SC_174 | 24:10–24:18 | LOC_008 (LOC_008_gog_tent) | CHAR_101, GOG_ENVOY | — | PROPS: PROP_014, PROP_015 | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_101_ref: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Helmet removed, gray topknot exposed, cloak over shoulders, brush in hand. Goguryeo envoy around 40, lean build, black topknot under a black silk court cap, dark red-brown silk robe with a black border, no armor, a rolled white cloth flag on a short pole, calm face. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. @PROP_015_ref: Goguryeo arrow: eighty-centimeter bamboo shaft, barbed triangular iron head, grey three-vane feather fletching bound with sinew, notched nock. Setting: Interior of a Goguryeo commander's field tent at night in rain: oiled hemp walls, rain drumming on the cloth, a low wooden table, a clay oil lamp, a set of iron lamellar armor laid beside the table, a black three-legged crow banner, reed mats. Action: The general rolls the silk around the shaft of a Goguryeo arrow, ties it with two turns of hemp cord, and hands it to the envoy in the silk robe with the rolled white flag; a short, faintly mocking instruction. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: silk rolled on the arrow, cord tied twice, handed over with one line. Sound: cord tightening, silk, rain, one line of Korean dialogue.
ACTION_START: rolling the silk on the arrow
ACTION_END: envoy holding the arrow, line spoken
NARRATION_KO: 화살에 묶어 보냈습니다. 화살로 보내는 글은 답을 요구하는 글이었습니다.
DIALOGUE_KO: 을지문덕: 우중문에게 전하게. 읽을 줄 안다면 알아들을 것이네.
SOUND: dây gai siết, lụa, mưa.
CONTINUITY: '우중문에게 전하게. 읽을 줄 안다면 알아들을 것이네.' 사자 = GOG_ENVOY (ref EXTRA_gog_envoy_ref).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_ref, EXTRA_gog_envoy_ref, PROP_014_ref, PROP_015_ref

### SC_175 | 24:18–24:26 | LOC_008 (LOC_008_sui_camp_gate) | GOG_ENVOY, SUI_SOLDIERS_STARVING | — | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Tracking shot with the envoy through the gate
IMAGE_PROMPT: Tracking shot with the envoy through the gate. Goguryeo envoy around 40, lean build, black topknot under a black silk court cap, dark red-brown silk robe with a black border, no armor, a rolled white cloth flag on a short pole, calm face. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_sui_camp_ep4: The gate of the Sui camp in monsoon rain: a gap in a low earth bank with a wooden barrier, mud churned to soup, rows of grey felt tents beyond, wet red and yellow banners on black lacquered poles, exhausted soldiers leaning on spears. Action: The Goguryeo envoy rides slowly through the Sui camp gate under a white flag on a plain horse; on both sides gaunt Sui soldiers lean on their spears and watch him — sunken eyes, hollow cheeks; one man falls as he tries to stand straight. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with the envoy: the starving soldiers watch, one falls trying to stand; a sentry shouts one line. Sound: the horse, rain, an unnatural silence in the camp, one shouted line of Korean dialogue.
ACTION_START: envoy entering the gate
ACTION_END: envoy inside, soldiers watching
NARRATION_KO: 사자는 무기를 보지 않았습니다. 을지문덕이 그랬던 것처럼, 얼굴을 보았습니다. 얼굴은 보름 전보다 더 깊었습니다.
DIALOGUE_KO: 수 초병: 고구려 사자다! 길을 비켜라!
SOUND: ngựa, mưa, trại im lặng bất thường.
CONTINUITY: '고구려 사자다! 길을 비켜라!' Ngựa trần (không VEH lock).
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_gog_envoy_ref, WPN_201_ref, PROP_021_ref, LOC_008_sui_camp_ep4
AI_RISK: lính gầy → mặt quay đi, out-focus

### SC_176 | 24:26–24:34 | LOC_008 (LOC_008_sui_tent) | CHAR_202, CHAR_203 | — | PROPS: PROP_014 | TYPE: video8s | 8s
SHOT: Medium two-shot at the camp chair, static
IMAGE_PROMPT: Medium two-shot at the camp chair, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, holding a small silk scroll, face flushed red with anger, lamplight warmth on the beard. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The white-bearded general in the camp chair unties the hemp cord from the arrow and unrolls the small ivory silk; the grey-bearded deputy looks down over his shoulder; under the oil lamp the general reads the first two lines aloud in a sneering voice. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: cord untied, silk unrolled, one line read aloud with a sneer, the deputy looking down. Sound: silk, the lamp, rain, one line of Korean dialogue.
ACTION_START: untying the cord
ACTION_END: silk open, reading aloud
NARRATION_KO: 다섯 글자 넉 줄. 우중문은 소리 내어 읽었습니다. 처음에는 웃으려고 읽었습니다.
DIALOGUE_KO: 우중문: 신책구천문, 묘산궁지리…
SOUND: lụa mở, đèn, mưa.
CONTINUITY: '신책구천문, 묘산궁지리…' tent_ep4 ✔ (cầm lụa).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, CHAR_203_ref, PROP_014_ref, LOC_008_sui_tent_ep4

### SC_177 | 24:34–24:44 | LOC_008 (LOC_008_sui_tent) | — | — | PROPS: PROP_014 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: extreme close-up on the silk under the lamp, slow slide from the first column to the second
IMAGE_PROMPT: Still for ken-burns: extreme close-up on the silk under the lamp, slow slide from the first column to the second. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The small ivory silk under the oil lamp: two columns of brush calligraphy, the strokes soft and unreadable, hemp cord and the arrow shaft beside it. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide along the first column to the second. Sound: the lamp, rain.
ACTION_START: first column
ACTION_END: second column
NARRATION_KO: 신책구천문. 신묘한 계책은 천문을 꿰뚫었고. 묘산궁지리. 오묘한 계산은 지리를 다하였네.
DIALOGUE_KO: 
SOUND: đèn, mưa.
CONTINUITY: Still 10 s. [OVERLAY] 「神策究天文 / 妙算窮地理」 + phụ đề Hàn (decisions #6).
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_014_ref, LOC_008_sui_tent_ep4
OVERLAY (edit): 神策究天文 / 妙算窮地理 + phụ đề Hàn 「신책구천문 · 묘산궁지리」
AI_RISK: chữ → nét bút mềm không đọc được; chữ thật OVERLAY

### SC_178 | 24:44–24:54 | LOC_008 (LOC_008_sui_tent) | — | — | PROPS: PROP_014 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: extreme close-up on the silk, slow slide to the last column, stopping on the last character
IMAGE_PROMPT: Still for ken-burns: extreme close-up on the silk, slow slide to the last column, stopping on the last character. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The same small ivory silk under the lamp: the last two columns of soft brush calligraphy, the final stroke at the bottom. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide to the last column, stopping on the last character. Sound: the lamp, rain, a man's breathing off frame.
ACTION_START: third column
ACTION_END: last character
NARRATION_KO: 전승공기고. 싸움에 이겨 공이 이미 높으니. 지족원운지. 족함을 알고 그만두기를 바라노라. 여수장우중문시. 이 땅에 남은 가장 오래된 시였습니다.
DIALOGUE_KO: 
SOUND: đèn, mưa; tiếng thở của 우중문 ngoài hình.
CONTINUITY: Still 10 s. [OVERLAY] 「戰勝功既高 / 知足願云止」 + phụ đề Hàn.
CHAIN_FROM: —
CUT_HALF: no
REFS: PROP_014_ref, LOC_008_sui_tent_ep4
OVERLAY (edit): 戰勝功既高 / 知足願云止 + phụ đề Hàn 「전승공기고 · 지족원운지」
AI_RISK: chữ → OVERLAY

### SC_179 | 24:54–25:02 | LOC_008 (LOC_008_sui_tent) | CHAR_202 | — | PROPS: PROP_014 | TYPE: video8s | 8s
SHOT: Close-up on the general, static
IMAGE_PROMPT: Close-up on the general, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, holding a small silk scroll, face flushed red with anger, lamplight warmth on the beard. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The general barks one dry laugh — and the laugh dies; the flush climbs from his neck to his temples, the white beard trembling; he looks at the silk again and his voice drops low. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: one dry laugh cut short, the flush rising, the second look at the silk, one low line. Sound: a short laugh, the lamp, rain, one line of Korean dialogue.
ACTION_START: laughing
ACTION_END: face red, low line
NARRATION_KO: 일곱 번 이겼다는 말이었습니다. 그러니 이제 그만두라는 말이었습니다. 이긴 자에게 보내는 항복 권고였습니다.
DIALOGUE_KO: 우중문: 이 시가… 나를 비웃는 것이냐?
SOUND: cười cụt, đèn, mưa.
CONTINUITY: '이 시가… 나를 비웃는 것이냐?'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_202_tent_ep4, PROP_014_ref, LOC_008_sui_tent_ep4

### SC_180 | 25:02–25:10 | LOC_008 (LOC_008_sui_tent) | GOG_ENVOY | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot on the kneeling envoy, static
IMAGE_PROMPT: Medium shot on the kneeling envoy, static. Goguryeo envoy around 40, lean build, black topknot under a black silk court cap, dark red-brown silk robe with a black border, no armor, a rolled white cloth flag on a short pole, calm face. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The Goguryeo envoy kneels on one knee without bowing too low and delivers the words he was told to say — formal, unafraid. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: one formal line delivered on one knee, head level. Sound: rain, the lamp, one line of Korean dialogue.
ACTION_START: envoy kneeling
ACTION_END: line delivered
NARRATION_KO: 사자는 두 번째 글을 입으로 전했습니다. 글보다 부드럽고, 글보다 무거운 말이었습니다.
DIALOGUE_KO: 사자: 군사를 돌리면 왕을 모시고 행재소에 조회하겠소.
SOUND: mưa, đèn.
CONTINUITY: '군사를 돌리면 왕을 모시고 행재소에 조회하겠소.'
CHAIN_FROM: —
CUT_HALF: no
REFS: EXTRA_gog_envoy_ref, LOC_008_sui_tent_ep4

### SC_181 | 25:10–25:18 | LOC_008 (LOC_008_fields) | CHAR_105, GOG_CAVALRYMEN, SUI_SOLDIERS_STARVING | VEH_101, WPN_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. Setting @LOC_008_hills_rain_ep4: Abandoned terraced fields below the Sui camp in monsoon rain: overgrown wet millet plots, mud, low green hills, grey cloud. Action: Outside the camp a party of Sui soldiers dig roots in an abandoned field; three hundred Goguryeo cavalry led by the officer with the white feather sweep down from the hill, loose one volley, cut through the party and vanish into the rain; the survivors run back to the camp empty-handed. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the diggers, the cavalry sweeping down and through, gone into the rain, survivors running. Sound: hooves, one volley of bowstrings, shouts, rain.
ACTION_START: soldiers digging, hill empty
ACTION_END: cavalry gone, survivors running
NARRATION_KO: 사자가 안에 있는 동안에도 밖에서는 싸웠습니다. 매일 그랬습니다. 밥을 찾으러 나가는 자는 돌아오지 못했습니다.
DIALOGUE_KO: 
SOUND: vó ngựa, dây cung, thét, mưa.
CONTINUITY: Mini-combat [史]. Wide.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_radio_ep3, WPN_201_ref, VEH_101_ref, WPN_101_ref, LOC_008_hills_rain_ep4
AI_RISK: kỵ số đông → wide

### SC_182 | 25:18–25:26 | LOC_008 (LOC_008_sui_camp_edge) | CHAR_203 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot as he turns and walks
IMAGE_PROMPT: Tracking shot as he turns and walks. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. Setting @LOC_008_sui_camp_ep4: The edge of the Sui camp in rain looking out over wet green fields and low hills, grey felt tents behind, an earth bank, mud, low grey cloud. Action: The grey-bearded deputy stands at the camp's edge watching the cavalry's dust dissolve in the rain, bamboo slips in his hand, counting the tally marks; then he turns and walks back toward the tent. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking: the watch, the count on the slips, one word, the turn and walk. Sound: rain, camp, bamboo slips, one word of Korean dialogue.
ACTION_START: standing at the edge, looking out
ACTION_END: walking back toward the tent
NARRATION_KO: 우문술은 세었습니다. 열흘, 이레, 닷새. 오늘 아침 그의 대쪽에는 사흘이 적혀 있었습니다. 사흘치 밥으로 평양은 무너지지 않았습니다.
DIALOGUE_KO: 우문술: 사흘.
SOUND: mưa, trại, thẻ tre.
CONTINUITY: '사흘.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_203_ref, LOC_008_sui_camp_ep4

### SC_183 | 25:26–25:34 | LOC_008 (LOC_008_sui_tent) | CHAR_203, CHAR_202 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, holding a small silk scroll, face flushed red with anger, lamplight warmth on the beard. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The deputy enters, lays his bamboo slips on the table before the general, and stands straight; the decision said aloud — dry, not raised. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: slips laid on the table, he straightens, one dry line. Sound: bamboo on lacquered wood, rain, one line of Korean dialogue.
ACTION_START: deputy entering with the slips
ACTION_END: standing straight, line spoken
NARRATION_KO: 사흘 전에는 권했습니다. 이번에는 정했습니다. 우문술은 우중문 아래 있었지만, 이 순간 군은 그의 것이었습니다.
DIALOGUE_KO: 우문술: 군사는 지쳤고 평양은 험하오. 돌아가오. 방진으로.
SOUND: thẻ tre đặt bàn, mưa.
CONTINUITY: '군사는 지쳤고 평양은 험하오. 돌아가오. 방진으로.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_203_ref, CHAR_202_tent_ep4, LOC_008_sui_tent_ep4

### SC_184 | 25:34–25:42 | LOC_008 (LOC_008_sui_tent) | CHAR_202 | — | PROPS: PROP_014 | TYPE: video8s | 8s
SHOT: Close-up on hands, static
IMAGE_PROMPT: Close-up on hands, static. @CHAR_202_tent_ep4: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, holding a small silk scroll, face flushed red with anger, lamplight warmth on the beard. @PROP_014_ref: small ivory silk scroll about thirty by forty centimeters with four short columns of black brush calligraphy, no seal, tied with hemp cord around a Goguryeo arrow shaft. Setting @LOC_008_sui_tent_ep4: Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats. Action: The general crushes the rolled silk in his fist and flings it onto the tent floor; looks at it; then bends, picks it up, smooths it flat, and tucks it inside his armor. Light: Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: silk crushed and thrown, the look, picked up, smoothed, tucked away. Sound: silk crumpling, falling, rain.
ACTION_START: silk crushed in the fist
ACTION_END: silk tucked into the armor
NARRATION_KO: 우중문은 시를 버렸다가 다시 주웠습니다. 그는 답장을 썼습니다. 꾸짖는 글이었습니다. 그러나 군은 돌아섰습니다. 삼국사기는 그 답장을 적지 않았습니다. 시만 적었습니다.
DIALOGUE_KO: 
SOUND: lụa vò, rơi, nhặt, mưa.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_183
CUT_HALF: no
REFS: CHAR_202_tent_ep4, PROP_014_ref, LOC_008_sui_tent_ep4

### SC_185 | 25:42–25:52 | LOC_008 (LOC_008_sui_camp_mountain) | SUI_OFFICER, SUI_SOLDIERS_STARVING, OXEN_CARTS | WPN_201 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial at rainy dusk, slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial at rainy dusk, slow pull-out. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, straight sword, face weathered and shouting. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. two-wheeled wooden ox carts loaded with rope-bound chests, oxen under wooden yokes. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_sui_camp_ep4: A vast Sui camp pitched against the foot of a green forested mountain in monsoon rain, 612 AD: countless grey felt and hemp tents in ragged rows across wet trampled grass and mud, only a few thin threads of cooking smoke, red and yellow banners hanging limp, wooden watchtowers, horse lines, low grey cloud on the mountain. Action: From above at dusk in rain: inside the camp Sui officers scratch an enormous square into the mud with poles, soldiers form up along its sides practising the formation, ox carts drawn into the middle; banners being lowered. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out over the square taking shape. Sound: slow command drums, rain, oxen.
ACTION_START: tight on the square lines in the mud
ACTION_END: wide on the camp
NARRATION_KO: 방진. 사방을 막고 가운데에 수레를 넣는 진이었습니다. 쫓기는 군대의 진이었습니다. 내일 새벽, 삼십만은 왔던 길로 돌아갈 것이었습니다. 살수로.
DIALOGUE_KO: 
SOUND: trống lệnh chậm, mưa, bò.
CONTINUITY: Still 10 s. 방진.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, PROP_021_ref, LOC_008_sui_camp_ep4

### SC_186 | 25:52–26:00 | LOC_007 (LOC_007_shelter) | CHAR_105, CHAR_001, CHAR_006 | EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium three-shot under the reed roof, static
IMAGE_PROMPT: Medium three-shot under the reed roof, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: Evening: the young officer sits down beside the captain and the scout under the reed roof, mud to the thighs, unclips the radio and sets it down, drinks from a gourd; he tells them. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static three-shot: he sits, sets the radio down, drinks from the gourd, one line. Sound: gourd, light rain, reeds, one line of Korean dialogue.
ACTION_START: officer sitting down
ACTION_END: gourd lowered, line spoken
NARRATION_KO: 그날 저녁, 해모루가 세 번째로 갈대밭에 왔습니다. 이번에는 시를 가지고 왔습니다.
DIALOGUE_KO: 해모루: 장군께서 우중문에게 시를 보내셨소. 넉 줄이오.
SOUND: bầu nước, mưa nhỏ, lau.
CONTINUITY: '장군께서 우중문에게 시를 보내셨소. 넉 줄이오.' Tối D6, đảo lau 2.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, CHAR_001_reeds_ep4, CHAR_006_ref, EQP_002_ref, LOC_007_island_ep4
AI_RISK: 3 nhân vật → tĩnh, khung rộng vừa

### SC_187 | 26:00–26:08 | LOC_007 (LOC_007_shelter) | CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the officer, static
IMAGE_PROMPT: Close-up on the officer, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The officer recites the last line in Korean, slowly, like a man who knows it by heart, watching the face across from him. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: one slow line recited, eyes on the listener. Sound: rain, one line of Korean dialogue.
ACTION_START: officer beginning
ACTION_END: line finished, watching
NARRATION_KO: 해모루는 넉 줄을 다 외웠습니다. 마지막 줄만 소리 내어 읽었습니다. 그 줄이 전부였습니다.
DIALOGUE_KO: 해모루: 족함을 알고 그만두기를 바라노라.
SOUND: mưa.
CONTINUITY: '족함을 알고 그만두기를 바라노라.'
CHAIN_FROM: SC_186
CUT_HALF: no
REFS: CHAR_105_radio_ep3, LOC_007_island_ep4

### SC_188 | 26:08–26:16 | LOC_007 (LOC_007_shelter) | CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the captain, static
IMAGE_PROMPT: Close-up on the captain, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The captain's face — recognition: he heard this line on the road south from a twenty-one-year-old soldier; he says it softly, almost to himself. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the recognition dawning, one soft line. Sound: rain, reeds, one line of Korean dialogue.
ACTION_START: listening
ACTION_END: soft line spoken
NARRATION_KO: 남하하는 길에서 한 소년이 이 시를 외웠습니다. 시험에 나온 시라고 했습니다. 그때 한승우는 듣기만 했습니다.
DIALOGUE_KO: 한승우: 태오가 외웠던 시다.
SOUND: mưa, lau.
CONTINUITY: '태오가 외웠던 시다.'
CHAIN_FROM: SC_187
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, LOC_007_island_ep4

### SC_189 | 26:16–26:24 | LOC_007 (LOC_007_water_point) | CHAR_005, XIANBEI_GUARDS_2, DOG | — | PROPS: — | TYPE: video8s | 8s
SHOT: Insert: close-up through the bamboo bars, static
IMAGE_PROMPT: Insert: close-up through the bamboo bars, static. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two Xianbei guards in brown leather lamellar armor and fur-trimmed leather caps slumped asleep under a hide awning with bows across their knees. a lean brown short-haired camp dog. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: The cage now set beside the camp's water point — a stone-lined pool, a tree, two guards, a brown dog lying by cold ashes; the boy curled inside, lips moving without sound — four lines of five syllables — his eyes on the mist beginning to rise from the water. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static through the bars: the lips move silently, the eyes on the rising mist; the dog breathes. Sound: rain, the dog breathing, lips moving, one whispered line of Korean dialogue.
ACTION_START: boy curled, lips still
ACTION_END: lips moving, mist rising
NARRATION_KO: 그 시를 외운 아이는 강 건너 우리 안에 있었습니다. 시험은 이미 오래전에 끝났습니다. 시는 끝나지 않았습니다.
DIALOGUE_KO: 장태오: (속삭임) 지족원운지…
SOUND: mưa, chó thở, môi mấp máy.
CONTINUITY: '(속삭임) 지족원운지…' Light: tối D6, sương bắt đầu (mưa tạnh dần).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_captive_ep3, VEH_206_ref, LOC_007_south_camp_ep4

### SC_190 | 26:24–26:32 | LOC_007 (LOC_007_island_edge) | CHAR_106, CHAR_001 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot at the water's edge, static
IMAGE_PROMPT: Medium two-shot at the water's edge, static. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The old blacksmith squats at the water's edge pointing a reed stalk at the river — thin mist already creeping over water warmer than the air; he speaks without looking up. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the reed stalk pointing at the mist on the water, one line without looking up. Sound: river, frogs, mist, one line of Korean dialogue.
ACTION_START: reed stalk pointing
ACTION_END: line spoken, mist creeping
NARRATION_KO: 비가 그치고 물이 오르면 강은 김을 냈습니다. 을보는 그것을 대장간 물통에서 배웠습니다. 뜨거운 쇠를 담근 물이었습니다.
DIALOGUE_KO: 을보: 물이 오르면 안개가 오오. 내일 새벽이오.
SOUND: sông, sương, ếch.
CONTINUITY: '물이 오르면 안개가 오오. 내일 새벽이오.' Mưa tạnh, sương lên.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_106_ref, CHAR_001_reeds_ep4, LOC_007_island_ep4

### SC_191 | 26:32–26:40 | LOC_007 (LOC_007_sandtable) | CHAR_107, CHAR_006 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium two-shot over the sand table, static
IMAGE_PROMPT: Medium two-shot over the sand table, static. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain. Action: The girl kneels at the sand table retracing the route with her finger — reeds, sandbar, channel, circle; then licks her finger and holds it up to test the wind; speaks to the scout. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the finger retraces the route, is licked and raised, one line. Sound: mud, a light breeze, one line of Korean dialogue.
ACTION_START: finger on the route
ACTION_END: wet finger raised, line spoken
NARRATION_KO: 개가 있었습니다. 개는 안개를 보지 못하지만 냄새를 맡습니다. 아리는 바람까지 계산했습니다.
DIALOGUE_KO: 아리: 개들이 있어요. 바람이 우리 쪽이면 못 맡아요.
SOUND: bùn, gió nhẹ, mưa tạnh.
CONTINUITY: '개들이 있어요. 바람이 우리 쪽이면 못 맡아요.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_006_ref, LOC_007_island_ep4

### SC_192 | 26:40–26:48 | LOC_007 (LOC_007_island2) | CHAR_006, ROK_RAIDERS_2 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_006_ref: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: The scout tests his knife blade on a reed stalk — it parts cleanly; he hands two Goguryeo knives to the two soldiers going with him, already in hemp jackets, and points at his own wrist, then his throat — how it is done. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: reed cut clean, two knives handed over, the gesture at wrist and throat, two words. Sound: reed parting, knives changing hands, one short line of Korean dialogue.
ACTION_START: knife on the reed
ACTION_END: gesture at the throat
NARRATION_KO: 둘은 백성민이 골랐습니다. 사냥꾼 집 아들과 어부 집 아들이었습니다. 물을 아는 사람들이었습니다.
DIALOGUE_KO: 백성민: 목. 한 번에.
SOUND: lau đứt, dao trao tay.
CONTINUITY: '목. 한 번에.' 2 lính = ROK_RAIDERS_2 (mặt bùn đen).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_ref, LOC_007_island_ep4
AI_RISK: dao + cử chỉ cổ → chậm, không chạm da

### SC_193 | 26:48–26:56 | LOC_007 (LOC_007_shelter) | CHAR_105 | — | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Walk-and-talk medium shot, camera panning as he rises
IMAGE_PROMPT: Walk-and-talk medium shot, camera panning as he rises. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The officer lifts the black horn with its seven notches and points east; rises and walks out toward the island's edge, speaking to the captain off frame. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Pan as he lifts the horn, points east, rises and walks, one line to someone off frame. Sound: horn on armor, reeds, one line of Korean dialogue.
ACTION_START: horn lifted, pointing east
ACTION_END: walking out of the shelter
NARRATION_KO: 나각은 고구려의 무전기였습니다. 삼백 기와 나각 하나. 그것이 해모루가 이 작전에 내놓은 것이었습니다.
DIALOGUE_KO: 해모루: 나는 동쪽 이 리에서 나각을 불겠소. 그러면 놈들이 돌아보오.
SOUND: sừng chạm giáp, lau.
CONTINUITY: '나는 동쪽 이 리에서 나각을 불겠소. 그러면 놈들이 돌아보오.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, PROP_018_ref, LOC_007_island_ep4

### SC_194 | 26:56–27:04 | LOC_008 (LOC_008_hills_rain) | CHAR_101, CHAR_105 | VEH_101 | PROPS: — | TYPE: still_kenburns | 8s
SHOT: Still for ken-burns: medium shot on the hill, slow push-in to the general's face
IMAGE_PROMPT: Still for ken-burns: medium shot on the hill, slow push-in to the general's face. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_008_hills_rain_ep4: Low green hills north of the Goguryeo capital in July monsoon rain, 612 AD: wet grass and scrub on rolling slopes, a muddy dirt road winding through the valley below churned by countless feet and hooves, low grey cloud on the ridges, mist in the folds, no buildings. Action: Memory image: the silver-bearded general stands on a rain-swept green hill looking north, the young officer beside him holding the reins of two armored horses; rain driving sideways. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the general's face; his voice over the still. Sound: rain, wind, one line of Korean dialogue.
ACTION_START: two men on the hill
ACTION_END: tight on the general's face
NARRATION_KO: 
DIALOGUE_KO: 을지문덕: 돌아올 것이오. 사흘 안에. 여울 북쪽을 지키시오.
SOUND: mưa, gió.
CONTINUITY: Still 8 s. VO 을지문덕: '돌아올 것이오. 사흘 안에. 여울 북쪽을 지키시오.' (lời dặn trước khi 해모루 đi).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_salsu_rain_ep5, CHAR_105_radio_ep3, VEH_101_ref, LOC_008_hills_rain_ep4

### SC_195 | 27:04–27:12 | LOC_007 (LOC_007_island_edge) | CHAR_105, CHAR_001 | — | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Walk-and-talk medium shot to the water's edge, static camera
IMAGE_PROMPT: Walk-and-talk medium shot to the water's edge, static camera. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The officer steps down to the water's edge, crouches and rinses the horn in the river, speaking as he crouches — the general's last sentence, every word slow; the captain stands behind him. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: he steps down, crouches, rinses the horn, one slow line word by word; the captain stands behind. Sound: river, mist, one line of Korean dialogue.
ACTION_START: officer stepping to the water
ACTION_END: crouched, horn in the water, line finished
NARRATION_KO: 을지문덕이 처음으로 계획을 말했습니다. 한 문장이었습니다. 그 한 문장이 살수의 전부였습니다.
DIALOGUE_KO: 해모루: 반이 건널 때까지 아무것도 하지 마시오.
SOUND: sông, sương.
CONTINUITY: '반이 건널 때까지 아무것도 하지 마시오.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, CHAR_001_reeds_ep4, PROP_018_ref, LOC_007_island_ep4

### SC_196 | 27:12–27:20 | LOC_007 (LOC_007_island_edge) | CHAR_001, CHAR_105 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Setting @LOC_007_island_ep4: The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water. Action: The captain asks; the officer gives a small shrug and looks out at the river. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: one question, a small shrug, eyes to the river. Sound: mist, river, one line of Korean dialogue.
ACTION_START: captain asking
ACTION_END: officer shrugging, looking at the river
NARRATION_KO: 해모루는 어깨만 으쓱했습니다. 장군은 그 말을 하지 않았습니다. 그는 늘 지금만 말했습니다.
DIALOGUE_KO: 한승우: 어느 쪽 반입니까?
SOUND: sương, sông.
CONTINUITY: '어느 쪽 반입니까?'
CHAIN_FROM: SC_195
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_105_radio_ep3, LOC_007_island_ep4

### SC_197 | 27:20–27:30 | LOC_007 (LOC_007_stake) | — | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up on the notched stake, slow push-in to the sixth notch
IMAGE_PROMPT: Still for ken-burns: close-up on the notched stake, slow push-in to the sixth notch. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The notched wooden stake at the water's edge in the last light: the water has risen to the sixth notch; mist beginning to cover the river; the rain has stopped. Light: Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the sixth notch at the waterline. Sound: river, mist, silence.
ACTION_START: stake with water at the sixth notch
ACTION_END: tight on the sixth notch
NARRATION_KO: 반이 건널 때까지. 을지문덕은 그 반이 어느 쪽 반인지 말하지 않았습니다.
DIALOGUE_KO: 
SOUND: sông, sương, im.
CONTINUITY: Still 10 s. Cọc mới ở đảo lau 2 (박기철 cắm lại — nước vạch 6). Kết P9 → MID-ROLL 4 @27:30.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_007_detail


## [Phần 10] 안개 속의 칼 (27:30–34:30) · 6 phase · narrator im 31:24–33:00 · CUT_HALF toàn khối

### SC_198 | 27:30–27:40 | LOC_007 (LOC_007_river_fog) | — | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: wide, very slow pull-out
IMAGE_PROMPT: Still for ken-burns: wide, very slow pull-out. Setting @LOC_007_fog_ep4: The wide shallow river at dawn buried in dense white fog: only the tops of the tall reeds rising from the whiteness like islands, the water surface a pale mirror fading into white a few meters out, no far bank visible, flat shadowless white light. Action: Dawn: dense white fog lies on the whole river, only the tops of the tall reeds rising from it like islands, no south bank visible, flat white light. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow pull-out; no dialogue, no narration. Sound: the river very faint, one water bird, silence.
ACTION_START: reed tops in white fog
ACTION_END: wide white river
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: sông rất nhỏ, chim nước một tiếng, im.
CONTINUITY: Still 10 s. Sau mid-roll 4: không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_007_fog_ep4

### SC_199 | 27:40–27:48 | LOC_007 (LOC_007_reed_path_fog) | CHAR_107, VILLAGE_WOMEN | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Tracking shot from behind, the fog swallowing them
IMAGE_PROMPT: Tracking shot from behind, the fog swallowing them. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: Six village women with baskets and sickles wade into the fog along the flooded reed path, the girl leading — braids under a dark cloth, pale mud on her cheeks, skirt tied at the knees, bare feet; nobody speaks. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking from behind as the file wades into the fog and fades; one woman murmurs a line. Sound: thigh-deep water, bamboo baskets, damp fog, one line of Korean dialogue.
ACTION_START: file entering the fog
ACTION_END: file fading into white
NARRATION_KO: 이레째 새벽. 을보의 말대로 안개가 왔습니다. 아낙들은 여느 날처럼 나갔습니다. 다만 오늘은 아리가 앞장섰습니다.
DIALOGUE_KO: 마을 아낙: 오늘은 안개가 깊구먼.
SOUND: nước tới đùi, rổ tre, sương ẩm.
CONTINUITY: '오늘은 안개가 깊구먼.' 아리 fog_trail_ep4 (không đèn lồng).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_night_trail_ep4, EXTRA_village_women_ref, LOC_007_fog_ep4
AI_RISK: 7 người → từ sau, sương che

### SC_200 | 27:48–27:56 | LOC_007 (LOC_007_reed_path_fog) | CHAR_006, ROK_RAIDERS_2 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Close lateral shot as they pass, static
IMAGE_PROMPT: Close lateral shot as they pass, static. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: Ten meters behind the women: the scout and two soldiers in coarse hemp jackets, dark cloths over their heads, faces blackened with mud except the eyes, straw sandals, hands empty — knives pressed inside their sleeves; wading past through the fog. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static lateral close: the three wade past stooped through the fog, hands empty, eyes only. Sound: water, wet hemp cloth.
ACTION_START: three entering frame
ACTION_END: three leaving frame into the fog
NARRATION_KO: 세 사람은 총을 두고 왔습니다. 야시경도, 무전기도. 가진 것은 칼 셋과 안개였습니다. 그리고 열다섯 살의 길이었습니다.
DIALOGUE_KO: 
SOUND: nước, vải gai ướt.
CONTINUITY: raid_hemp_ep4 (night_raid ✔ + áo gai, khăn đầu). Không súng.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_night_raid_ep4, LOC_007_fog_ep4

### SC_201 | 27:56–28:04 | LOC_007 (LOC_007_north_ford) | CHAR_002 | WPN_003, WPN_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up in the reed hole, static
IMAGE_PROMPT: Close-up in the reed hole, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The lieutenant in a reed hole at the edge of the north shore, helmet off, tactical goggles pushed up on his forehead, the light machine gun before him and a heavy machine gun on a tripod beside him under a poncho; he stares into white fog and sees nothing. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: he stares into the white, listening, fog dripping from the reeds; nothing moves. Sound: fog dripping from reeds, silence.
ACTION_START: staring into fog
ACTION_END: staring, unchanged
NARRATION_KO: 북쪽 여울. 오태민의 자리였습니다. 셋이 돌아올 문이었습니다. 그는 안개 속에서 아무것도 보지 못했습니다. 듣기만 했습니다.
DIALOGUE_KO: 
SOUND: sương nhỏ giọt từ lau, im.
CONTINUITY: K6 trên giá ba chân phủ poncho (WPN_004). Kính bảo hộ đẩy lên trán (mũ tháo).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_003_ref, WPN_004_ref, LOC_007_detail

### SC_202 | 28:04–28:12 | LOC_007 (LOC_007_island2_k2) | CHAR_001 | VEH_001, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium close-up on the turret hatch, static
IMAGE_PROMPT: Medium close-up on the turret hatch, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The captain half out of the tank's turret hatch under its reed cover, headset on, helmet off; he presses the radio and whispers the order to the whole company. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the handset pressed, one whispered line. Sound: push-to-talk click, faint electronics, fog.
ACTION_START: captain in the hatch
ACTION_END: order whispered
NARRATION_KO: 사격 금지. 이 섬에서 가장 많이 들은 명령이었습니다. 오늘은 명령이 세 사람의 목숨이었습니다.
DIALOGUE_KO: 한승우: 천둥 1 이하 전원, 여기는 천둥 지휘. 사격 금지.
SOUND: PTT, quạt điện tử nhỏ, sương.
CONTINUITY: '천둥 1 이하 전원, 여기는 천둥 지휘. 사격 금지.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, VEH_001_ref, EQP_002_ref, LOC_007_island_ep4

### SC_203 | 28:12–28:20 | LOC_007 (LOC_007_east_meadow_fog) | CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Medium shot in the fog, static
IMAGE_PROMPT: Medium shot in the fog, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_007_fog_ep4: A flat grassy meadow on the north bank east of the reed beds in dense white dawn fog: wet green grass, the shapes of horses and riders fading into whiteness, no horizon, flat white light. Action: Two li to the east: three hundred Goguryeo cavalry stand motionless in the fog on wet grass, horses breathing steam; the officer with the white feather in front, the black horn held level at his chest — not yet raised; radio on his armor. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: horses breathe steam, nothing moves, the horn held at the chest; one word. Sound: horses breathing, a faint clink of armor, fog, one word of Korean dialogue.
ACTION_START: cavalry motionless in fog
ACTION_END: horn still at the chest, word spoken
NARRATION_KO: 동쪽 이 리. 삼백 기가 안개 속에 서 있었습니다. 해모루의 나각은 아직 입에 닿지 않았습니다. 그것은 마지막에 부는 것이었습니다.
DIALOGUE_KO: 해모루: 아직이다.
SOUND: ngựa thở, giáp khẽ, sương.
CONTINUITY: '아직이다.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, VEH_101_ref, PROP_018_ref, LOC_007_fog_ep4
AI_RISK: 300 kỵ → sương che, hình khối

### SC_204 | 28:20–28:28 | LOC_007 (LOC_007_channel_fog) | CHAR_006, VILLAGE_WOMEN, ROK_RAIDERS_2 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Camera at water level, static
IMAGE_PROMPT: Camera at water level, static. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A channel of open brown water between the south shore and the reed beds in dense white dawn fog: waist-deep water, a wall of tall reeds fading into whiteness on one side, wet sand on the other, no far bank visible. Action: The women wade the channel waist-deep with baskets balanced on their heads; the scout and the two soldiers mixed among them, stooped low like old men; the fog swallows the bank behind. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static at water level: the group wades past, baskets on heads, the three disguised men stooped among them. Sound: water, baskets, breathing.
ACTION_START: group entering the channel
ACTION_END: group crossing, fog behind
NARRATION_KO: 초병은 아낙들만 보았습니다. 엿새째 같은 아낙들이었습니다. 같은 것은 보이지 않는 법이었습니다.
DIALOGUE_KO: 
SOUND: nước, rổ, thở.
CONTINUITY: Nước tới thắt lưng.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_006_night_raid_ep4, EXTRA_village_women_ref, LOC_007_fog_ep4
AI_RISK: 9 người → ngang mặt nước, sương

### SC_205 | 28:28–28:36 | LOC_007 (LOC_007_south_sentry_fog) | SUI_SENTRY | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. a Sui sentry in a wet grey-blue padded coat and pointed iron helmet, spear leaning beside him, face half hidden, dozing. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_007_south_camp_ep4: A Sui sentry post at the water's edge of the rear-guard camp in dense white dawn fog: a hide awning on poles, a spear leaning against it, wet sand, grey felt tents fading into whiteness behind. Action: A Sui sentry sits against his spear under a hide awning, eyes half shut; he sees the shapes of the women in the fog, waves them through lazily, pulls his coat over his neck and settles back to sleep. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: eyes half open, a lazy wave, the coat pulled up, one mumbled line. Sound: fog, snoring, baskets passing, one mumbled line of Korean dialogue.
ACTION_START: sentry dozing
ACTION_END: sentry settled back asleep
NARRATION_KO: 엿새 동안 같은 얼굴이 같은 시간에 지나갔습니다. 초병은 그것을 풍경으로 보았습니다. 풍경은 검사하지 않는 법이었습니다.
DIALOGUE_KO: 수 초병: 가라, 가.
SOUND: sương, ngáy, rổ đi qua.
CONTINUITY: '가라, 가.'
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, LOC_007_south_camp_ep4

### SC_206 | 28:36–28:44 | LOC_007 (LOC_007_camp_fog) | CHAR_107, CHAR_006, VILLAGE_WOMEN, ROK_RAIDERS_2 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Tracking shot following the three as they split off
IMAGE_PROMPT: Tracking shot following the three as they split off. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_south_camp_ep4: Inside the Sui rear-guard camp in dense white dawn fog: grey felt and dark hide tents fading into whiteness, ox carts, tethered horses, wet sand and mud, flat white light. Action: The girl does not turn her head — a tilt of her chin forward: through the fog fifty meters off, the water pool, a tree, the shape of the cage; she walks on with the women toward the reed beds; the three men split left and dissolve into the reeds. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking: the chin tilt, the women walking on, the three peeling off into the reeds and gone. Sound: reeds closing, water.
ACTION_START: girl's chin lifting toward the cage
ACTION_END: three men vanishing into the reeds
NARRATION_KO: 여기서 길이 갈렸습니다. 아낙들은 갈대로, 셋은 물로. 아리는 뒤돌아보지 않았습니다. 뒤돌아보는 것은 어머니에게 배우지 않았습니다.
DIALOGUE_KO: 
SOUND: lau khép, nước.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, EXTRA_village_women_ref, LOC_007_south_camp_ep4

### SC_207 | 28:44–28:52 | LOC_007 (LOC_007_water_point) | CHAR_005, XIANBEI_GUARDS_2, DOG | — | PROPS: — | TYPE: video8s | 8s
SHOT: Low wide, static
IMAGE_PROMPT: Low wide, static. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two Xianbei guards in brown leather lamellar armor and fur-trimmed leather caps slumped asleep under a hide awning with bows across their knees. a lean brown short-haired camp dog. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: The water point: a stone-lined pool, two Xianbei guards slumped asleep under a hide awning with bows on their knees, a brown dog curled asleep by cold ashes, the bamboo cage under the tree; inside, the boy awake, eyes open on the fog. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low wide: nothing moves but the dog's breathing and the boy's eyes. Sound: snoring, the dog breathing, water trickling.
ACTION_START: all still
ACTION_END: all still, boy's eyes on the fog
NARRATION_KO: 새벽에는 졸았습니다. 아리의 말 그대로였습니다. 개도 졸았습니다. 아직은.
DIALOGUE_KO: 
SOUND: ngáy, chó thở, nước rỉ.
CONTINUITY: Phase 2. Cũi cạnh hố nước (sub-lock water_point).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_005_captive_ep3, VEH_206_ref, LOC_007_south_camp_ep4

### SC_208 | 28:52–29:00 | LOC_007 (LOC_007_water_point) | CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up at the pool's edge, static, fog
IMAGE_PROMPT: Close-up at the pool's edge, static, fog. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: The scout surfaces at the edge of the pool — only eyes and nose above the water — and climbs onto the stone rim without a sound; the knife slides out of his sleeve; one of the guards stirs. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the face rises from the water, the body slides onto the stones, the knife appears, a guard stirs off frame. Sound: a faint trickle, stone, a sleeper shifting.
ACTION_START: eyes above the water
ACTION_END: on the rim, knife out
NARRATION_KO: 사냥꾼의 아들은 물에서도 조용했습니다. 강원도 산골의 개울이 그를 그렇게 키웠습니다.
DIALOGUE_KO: 
SOUND: nước rỉ rất nhỏ, kè đá, cựa mình.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_207
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, LOC_007_south_camp_ep4

### SC_209 | 29:00–29:08 | LOC_007 (LOC_007_water_point) | CHAR_006, ROK_RAIDERS_2, XIANBEI_GUARDS_2 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium-wide under the awning, static (keyframe = beat B)
IMAGE_PROMPT: Medium-wide under the awning, static (keyframe = beat B). @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. two Xianbei guards in brown leather lamellar armor and fur-trimmed leather caps slumped asleep under a hide awning with bows across their knees. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: Under the hide awning: the second disguised soldier locks the second guard's neck from behind and pulls him down behind the hide sheet; the scout lowers the first guard to the ground; three seconds; fog; no blood. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): insert — the first guard slumps into the scout's arms. Beat B (4–8 s): medium-wide — the second guard is locked from behind and pulled down behind the hide; the scout lowers the first; stillness. Sound: rustling, a short exhalation, silence.
ACTION_START: guard slumping (insert) / second guard being locked
ACTION_END: both guards down, three men still
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: vải sột soạt, một tiếng thở hắt, im.
CONTINUITY: 2-BEAT (4+4), narrator vẫn nói. Không gore.
CHAIN_FROM: SC_208
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, VEH_206_ref, LOC_007_south_camp_ep4
AI_RISK: giết lính gác → không lưỡi dao, không vết, 'slumps'
INSERT_CLIP (4 s, tách riêng): Beat A insert, 4 s, close-up in fog: the first sleeping guard slumps forward into the arms of the mud-faced scout in a hemp jacket without ever opening his eyes; no blade visible, no wound. Sound: cloth rustling, one short exhalation, silence.

### SC_210 | 29:08–29:16 | LOC_007 (LOC_007_cage) | CHAR_006, CHAR_005 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the cage lock, then tilt to the faces
IMAGE_PROMPT: Close-up on the cage lock, then tilt to the faces. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. Setting @LOC_007_south_camp_ep4: Under a dripping willow tree at the edge of the Sui rear-guard camp on the south bank: a man-sized cage of bamboo poles lashed with leather thongs under a sagging wet cloth roof, wet sand and mud, grey felt tents and ox carts behind, steady rain. Action: Close on the cage lock: leather thongs and a wooden pin; the scout's knife cuts the thongs and levers the pin out; the boy inside stares at the mud-black face with only eyes — his mouth opens to call out; a muddy finger presses against his lips. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Close on the lock: thongs cut, pin levered out; tilt up as the boy's mouth opens and the muddy finger comes to his lips. Sound: leather parting, the wooden pin, breathing.
ACTION_START: knife on the thongs
ACTION_END: finger on the boy's lips
NARRATION_KO: 열이틀 만이었습니다. 태오는 그 눈을 알아보았습니다. 눈밖에 보이는 것이 없었지만 알아보았습니다.
DIALOGUE_KO: 
SOUND: dây da đứt, chốt gỗ, thở.
CONTINUITY: Chốt gỗ bị cắt ngọt (탁발흠 nhặt ở SC_245).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_south_camp_ep4

### SC_211 | 29:16–29:24 | LOC_007 (LOC_007_cage) | CHAR_005, CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the foot and the face, static
IMAGE_PROMPT: Close-up on the foot and the face, static. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. Setting @LOC_007_south_camp_ep4: Under a dripping willow tree at the edge of the Sui rear-guard camp on the south bank: a man-sized cage of bamboo poles lashed with leather thongs under a sagging wet cloth roof, wet sand and mud, grey felt tents and ox carts behind, steady rain. Action: The boy crawls out of the cage, tries to stand — his right foot swollen black-purple — and buckles; the scout catches him; the boy bites his own hand to keep from crying out. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: crawling out, the try to stand, the buckle, caught, the hand bitten; one whispered word. Sound: strangled breathing, sand, one whispered word of Korean dialogue.
ACTION_START: crawling out of the cage
ACTION_END: held up by the scout, hand in his teeth
NARRATION_KO: 발은 몽둥이로 맞은 뒤 부어 있었습니다. 걸을 수 없었습니다. 계획에 없던 것이었습니다. 계획에 없는 것은 늘 있었습니다.
DIALOGUE_KO: 장태오: (속삭임) 발이…
SOUND: thở nén, cát.
CONTINUITY: '(속삭임) 발이…' Chân phải sưng tím.
CHAIN_FROM: SC_210
CUT_HALF: yes
REFS: CHAR_005_captive_ep3, CHAR_006_night_raid_ep4, LOC_007_south_camp_ep4

### SC_212 | 29:24–29:32 | LOC_007 (LOC_007_cage) | CHAR_006, CHAR_005, ROK_RAIDERS_2 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. Setting @LOC_007_south_camp_ep4: Under a dripping willow tree at the edge of the Sui rear-guard camp on the south bank: a man-sized cage of bamboo poles lashed with leather thongs under a sagging wet cloth roof, wet sand and mud, grey felt tents and ox carts behind, steady rain. Action: The scout kneels and hoists the boy onto his back; the second soldier binds the boy's wrists together around the scout's neck with a strip of cloth; the scout's eyes stop on the boy's right shoulder — the ragged bare patch where the flag was — and he says nothing. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the hoist onto the back, the wrists bound at the neck, the eyes resting on the torn shoulder, moving on. Sound: cloth tying, breathing.
ACTION_START: scout kneeling, boy being lifted
ACTION_END: boy on his back, wrists bound, eyes on the shoulder
NARRATION_KO: 어깨의 태극기는 없었습니다. 탁발흠이 뜯어 갔습니다. 백성민은 그 자리를 한 번 보고 걸음을 옮겼습니다.
DIALOGUE_KO: 
SOUND: vải buộc, thở.
CONTINUITY: Mảng vải xé vai PHẢI (chỗ 태극기).
CHAIN_FROM: SC_211
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_south_camp_ep4

### SC_213 | 29:32–29:40 | LOC_007 (LOC_007_water_point) | CHAR_006, CHAR_005, ROK_RAIDERS_2, DOG | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static, then rack focus to the dog's ear
IMAGE_PROMPT: Medium shot, static, then rack focus to the dog's ear. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. a lean brown short-haired camp dog. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: The three men stoop down to the pool's edge, the scout carrying the boy on his back wading in; behind them by the cold ashes the dog's ear lifts — close on the ear, the nose twitching. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the men wade into the pool; focus racks to the dog's ear lifting, the nose sniffing. Sound: water, the dog sniffing, fog.
ACTION_START: men entering the water, dog asleep
ACTION_END: dog's ear up, nose twitching
NARRATION_KO: 개는 사람보다 먼저 깼습니다. 코가 먼저였고, 귀가 그다음이었습니다.
DIALOGUE_KO: 
SOUND: nước, chó hít, sương.
CONTINUITY: Kết Phase 2.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_south_camp_ep4

### SC_214 | 29:40–29:48 | LOC_007 (LOC_007_reed_path_fog) | CHAR_107, VILLAGE_WOMEN | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Close-up on the girl, static
IMAGE_PROMPT: Close-up on the girl, static. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: The girl among the women at the reed edge, sickle in hand, looks back through the fog toward the water point — the dog is standing, its head turned toward the water; her hand tightens white on the sickle handle. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the look back, the dog's shape standing in the fog, the hand whitening on the sickle. Sound: fog, the sickle, a heartbeat.
ACTION_START: girl looking back
ACTION_END: hand white on the sickle
NARRATION_KO: 바람이 바뀌었습니다. 새벽 강바람은 늘 그랬습니다. 아리가 계산하지 못한 하나였습니다.
DIALOGUE_KO: 
SOUND: sương, liềm, tim đập (subjective).
CONTINUITY: Gió đổi.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_107_night_trail_ep4, EXTRA_village_women_ref, LOC_007_fog_ep4

### SC_215 | 29:48–29:56 | LOC_007 (LOC_007_water_point) | DOG, SUI_SENTRY | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide on the camp entrance in fog, static (keyframe = beat B)
IMAGE_PROMPT: Wide on the camp entrance in fog, static (keyframe = beat B). a lean brown short-haired camp dog. a Sui sentry in a wet grey-blue padded coat and pointed iron helmet, spear leaning beside him, face half hidden, dozing. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: A Sui sentry at the camp entrance jerks awake at the barking, lifts a conch-shell horn to his mouth and blows. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–3 s): insert — the dog's muzzle barking and lunging. Beat B (3–8 s): the sentry jerks awake, lifts the conch horn and blows a long hoarse note, shouting one line. Sound: barking, a long hoarse conch note, one shouted line of Korean dialogue.
ACTION_START: dog barking (insert) / sentry asleep
ACTION_END: sentry blowing the conch
NARRATION_KO: 실수는 개였습니다. 사람은 속일 수 있었습니다. 개는 속일 수 없었습니다.
DIALOGUE_KO: 수 초병: 적이다!
SOUND: chó sủa dội, tù và Tùy khàn dài.
CONTINUITY: 2-BEAT (3+5). '적이다!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, LOC_007_south_camp_ep4
INSERT_CLIP (3 s, tách riêng): Beat A insert, 3 s, extreme close-up on a brown dog's muzzle in fog: it barks furiously, the sound ringing in the whiteness, and lunges toward the edge of the water. Sound: violent barking echoing in fog.

### SC_216 | 29:56–30:04 | LOC_007 (LOC_007_tent_tuoba) | CHAR_205 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Fast tracking shot out of the tent
IMAGE_PROMPT: Fast tracking shot out of the tent. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_south_camp_ep4: Inside a small felt tent in the Sui rear-guard camp: a leather sleeping pad, a wooden tent pole hung with a bow and quiver, dim grey fog light through the open flap. Action: The Xianbei commander springs off his leather sleeping pad, snatches the night-vision device hanging from the tent pole, and runs barefoot out through the flap into white fog. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Fast tracking: up off the pad, the device grabbed from the pole, out through the flap into whiteness. Sound: barking, the conch horn, tent cloth.
ACTION_START: rising from the pad
ACTION_END: out of the tent into fog
NARRATION_KO: 탁발흠은 눈부터 잡았습니다. 밤이면 그 눈은 낮이었습니다. 지금은 새벽이었고, 안개였습니다.
DIALOGUE_KO: 
SOUND: chó sủa, tù và, lều bạt.
CONTINUITY: fog_ep4 (không mũ, chân trần, kính trên dây cổ — ở đây cầm tay).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, EQP_001_ref, LOC_007_south_camp_ep4

### SC_217 | 30:04–30:12 | LOC_007 (LOC_007_camp_fog) | — | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Night-vision POV blown out to white, static
IMAGE_PROMPT: Night-vision POV blown out to white, static. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_south_camp_ep4: Inside the Sui rear-guard camp in dense white dawn fog: grey felt and dark hide tents fading into whiteness, ox carts, tethered horses, wet sand and mud, flat white light. Action: A night-vision view — pure white: the whole view flared white with grain, daylight and fog blinding the tube; the view swings one way — white; back — white; no shapes at all. Light: A night-vision view blown out to pure white with grain and faint scan noise, no shapes visible. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: POV: white, a swing left — white, a swing back — white, grain crawling; no dialogue. Sound: a high night-vision whine, barking far off, the conch horn.
ACTION_START: white
ACTION_END: white
NARRATION_KO: 밤을 낮으로 만드는 눈은 낮을 견디지 못했습니다. 안개와 새벽빛이 그 안을 하얗게 채웠습니다. 석문령의 전리품이 처음으로 쓸모없어졌습니다.
DIALOGUE_KO: 
SOUND: kính rít cao, chó sủa xa, tù và.
CONTINUITY: Kính đêm mù trong sương + ánh ngày.
CHAIN_FROM: —
CUT_HALF: yes
REFS: EQP_001_ref, LOC_007_south_camp_ep4
AI_RISK: khung trắng → chấp nhận ảnh gần trống, hạt nhiễu

### SC_218 | 30:12–30:20 | LOC_007 (LOC_007_camp_fog) | CHAR_205 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_south_camp_ep4: Inside the Sui rear-guard camp in dense white dawn fog: grey felt and dark hide tents fading into whiteness, ox carts, tethered horses, wet sand and mud, flat white light. Action: The commander tears the device from his eye and lets it fall to hang on its cord against his chest; closes his eyes; tilts his head — listening; opens his eyes; speaks to himself. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the device dropped to the chest, eyes closed, head tilted, eyes open, one line. Sound: the device knocking his chest, breathing, distant water, one line of Korean dialogue.
ACTION_START: device at the eye
ACTION_END: eyes open, line spoken
NARRATION_KO: 밤눈은 밤에만 눈이었습니다. 안개 앞에서 천사백 년 뒤의 물건은 장님이 되었습니다. 그는 그것을 오 초 만에 배웠습니다.
DIALOGUE_KO: 탁발흠: 안개엔 눈이 없다. 귀로 잡는다.
SOUND: kính đập ngực, thở, tiếng nước xa.
CONTINUITY: '안개엔 눈이 없다. 귀로 잡는다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, EQP_001_ref, LOC_007_south_camp_ep4

### SC_219 | 30:20–30:28 | LOC_007 (LOC_007_camp_fog) | CHAR_205, XIANBEI_RIDERS_FOOT | VEH_206, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_south_camp_ep4: Inside the Sui rear-guard camp in dense white dawn fog: grey felt and dark hide tents fading into whiteness, ox carts, tethered horses, wet sand and mud, flat white light. Action: Xianbei riders run barefoot from the tents with bows; the commander flings his arm toward the water point — where water is being churned — not toward the barking dog; horses being untied. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: men run out with bows, the arm flung toward the water, one shouted line, horses untied. Sound: running feet, bowstrings, horses, distant splashing, one line of Korean dialogue.
ACTION_START: men running out
ACTION_END: arm pointing toward the water
NARRATION_KO: 그는 개가 짖는 곳을 가리키지 않았습니다. 물소리가 나는 곳을 가리켰습니다. 귀는 안개를 뚫었습니다.
DIALOGUE_KO: 탁발흠: 물소리다. 저쪽!
SOUND: chân chạy, dây cung, ngựa, tiếng nước xa.
CONTINUITY: '물소리다. 저쪽!'
CHAIN_FROM: SC_218
CUT_HALF: yes
REFS: CHAR_205_ref, VEH_206_ref, EQP_001_ref, LOC_007_south_camp_ep4

### SC_220 | 30:28–30:36 | LOC_007 (LOC_007_water_point) | XIANBEI_RIDERS_FOOT | VEH_206 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static
IMAGE_PROMPT: Wide, static. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: Xianbei riders reach the water point: the two guards lying behind the hide sheet, the cage open, its wooden pin cut clean on the sand; they spread out into the water on foot with bows drawn and the fog takes them. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the riders arrive, see the open cage, spread into the water, vanish into fog; one shouts a line. Sound: sand, water, short calls, one line of Korean dialogue.
ACTION_START: riders arriving
ACTION_END: riders gone into the fog
NARRATION_KO: 우리는 비어 있었습니다. 자물쇠는 칼로 잘려 있었습니다. 그들은 물로 들어갔습니다. 안개가 그들도 삼켰습니다.
DIALOGUE_KO: 선비 기병: 우리가 비었다!
SOUND: cát, nước, tiếng gọi nhau ngắn.
CONTINUITY: '우리가 비었다!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, LOC_007_south_camp_ep4

### SC_221 | 30:36–30:44 | LOC_007 (LOC_007_channel_fog) | CHAR_006, CHAR_005, ROK_RAIDERS_2 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot from the front, camera moving backward with them
IMAGE_PROMPT: Medium shot from the front, camera moving backward with them. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. Setting @LOC_007_fog_ep4: A channel of open brown water between the south shore and the reed beds in dense white dawn fog: waist-deep water, a wall of tall reeds fading into whiteness on one side, wet sand on the other, no far bank visible. Action: The scout wades waist-deep through fog with the boy on his back, the two soldiers on either side pushing the water aside for him; behind, shouts and splashing of pursuers; the boy's teeth clenched, arms tight around the scout's neck. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Camera backing ahead of them: wading hard, the two soldiers breaking water, the boy clinging; pursuit sounds behind; one line. Sound: wading, breathing, pursuit splashing behind, one line of Korean dialogue.
ACTION_START: three men wading toward camera
ACTION_END: closer, boy's arms tight
NARRATION_KO: 물은 무릎이 아니었습니다. 이레 동안 허리까지 올라와 있었습니다. 업힌 사람과 업은 사람에게 그것은 두 배로 무거웠습니다.
DIALOGUE_KO: 백성민: 잡아. 놓지 마.
SOUND: lội, thở, sau lưng tiếng đuổi.
CONTINUITY: '잡아. 놓지 마.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_fog_ep4

### SC_222 | 30:44–30:52 | LOC_007 (LOC_007_channel_fog) | CHAR_107, CHAR_006, VILLAGE_WOMEN | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles. Setting @LOC_007_fog_ep4: A channel of open brown water between the south shore and the reed beds in dense white dawn fog: waist-deep water, a wall of tall reeds fading into whiteness on one side, wet sand on the other, no far bank visible. Action: The girl breaks from the women and splashes ahead past the scout to lead; far off the women scatter into the reeds as arranged, only reed-cutters; she whispers. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the girl splashes past to the front, the women scattering into the reeds far off, one whispered line. Sound: water, reeds, pursuit, one whispered line of Korean dialogue.
ACTION_START: girl breaking from the women
ACTION_END: girl ahead of the scout
NARRATION_KO: 아낙들은 흩어졌습니다. 갈대를 베러 왔을 뿐이었습니다. 아리는 앞으로 나갔습니다. 여기서부터는 그녀의 길이었습니다.
DIALOGUE_KO: 아리: (속삭임) 이쪽이에요.
SOUND: nước, lau, tiếng đuổi.
CONTINUITY: '(속삭임) 이쪽이에요.' 태오 trên lưng (không thêm lock — khuất).
CHAIN_FROM: SC_221
CUT_HALF: yes
REFS: CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, EXTRA_village_women_ref, LOC_007_fog_ep4

### SC_223 | 30:52–31:00 | LOC_007 (LOC_007_north_ford) | CHAR_002 | WPN_004, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the hand and the handset, static
IMAGE_PROMPT: Close-up on the hand and the handset, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The lieutenant hears the conch and the dog through the fog from the south bank; his hand rests on the heavy machine gun's grip, thumb on the safety; he presses the radio, voice pressed flat. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: hand on the grip, thumb on the safety, the handset pressed, one flat line. Sound: distant conch, barking, push-to-talk click, one line of Korean dialogue.
ACTION_START: hand on the grip
ACTION_END: handset pressed
NARRATION_KO: 북쪽 여울에서는 아무것도 보이지 않았습니다. 오태민은 소리로 싸움을 읽었습니다. 개, 나각, 그리고 물.
DIALOGUE_KO: 오태민: 천둥 지휘, 여기는 1소대. 남안 소란. 대기합니다.
SOUND: tù và xa, chó, PTT.
CONTINUITY: '천둥 지휘, 여기는 1소대. 남안 소란. 대기합니다.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, WPN_004_ref, EQP_002_ref, LOC_007_detail
AI_RISK: tay trên súng → không cận cò, ngón cái trên khóa

### SC_224 | 31:00–31:08 | LOC_007 (LOC_007_island2_k2) | CHAR_001 | VEH_001, EQP_002 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up in the hatch, static
IMAGE_PROMPT: Close-up in the hatch, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The captain in the hatch closes his eyes and listens — the conch, the dog, the water; opens them; one word into the radio. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes closed, listening, opened, one word. Sound: push-to-talk click, fog, one word of Korean dialogue.
ACTION_START: eyes closed
ACTION_END: eyes open, word spoken
NARRATION_KO: 대기. 이 부대가 지난 이레 동안 가장 많이 한 일이었습니다.
DIALOGUE_KO: 한승우: 대기.
SOUND: PTT, sương.
CONTINUITY: '대기.'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, VEH_001_ref, EQP_002_ref, LOC_007_island_ep4

### SC_225 | 31:08–31:16 | LOC_007 (LOC_007_east_meadow_fog) | CHAR_105, GOG_CAVALRYMEN | VEH_101, EQP_002 | PROPS: PROP_018 | TYPE: video8s | 8s
SHOT: Close-up on the radio, the lips and the horn, static
IMAGE_PROMPT: Close-up on the radio, the lips and the horn, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. Setting @LOC_007_fog_ep4: A flat grassy meadow on the north bank east of the reed beds in dense white dawn fog: wet green grass, the shapes of horses and riders fading into whiteness, no horizon, flat white light. Action: The officer hears the Sui conch from the camp; he presses the modern radio clipped to his armor and speaks one line into it; then lifts the black horn with seven notches to his lips; behind him three hundred riders gather their reins. Light: Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the radio pressed, one line, the horn raised to the lips, a deep breath; reins tightening behind. Sound: distant conch, push-to-talk click, horses, an intake of breath, one line of Korean dialogue.
ACTION_START: radio pressed
ACTION_END: horn at the lips, breath drawn
NARRATION_KO: 그때 동쪽에서.
DIALOGUE_KO: 해모루: 한 대장, 여기는 해모루. 나각 부오.
SOUND: tù và Tùy xa, PTT, ngựa, hít hơi.
CONTINUITY: '한 대장, 여기는 해모루. 나각 부오.' (decisions #3).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_radio_ep3, VEH_101_ref, EQP_002_ref, PROP_018_ref, LOC_007_fog_ep4

### SC_226 | 31:16–31:24 | LOC_007 (LOC_007_east_meadow_fog) | CHAR_105, GOG_CAVALRYMEN | VEH_101 | PROPS: PROP_018, PROP_012 | TYPE: video8s | 8s
SHOT: Low wide as the cavalry burst from the fog, static (keyframe = beat B)  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Low wide as the cavalry burst from the fog, static (keyframe = beat B). @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_018_ref: curved black water-buffalo horn trumpet about fifty centimeters long with a bronze mouthpiece and a leather shoulder cord. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_007_fog_ep4: A flat grassy meadow on the north bank east of the reed beds in dense white dawn fog: wet green grass, the shapes of horses and riders fading into whiteness, no horizon, flat white light. Action: Three hundred Goguryeo cavalry burst out of the white fog in a broad line charging toward the eastern flank of the camp, wet yellow banners with the black crow streaming, the officer with the white feather leading. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–3 s): insert — lips on the horn, one long note. Beat B (3–8 s): low wide — the line of cavalry erupts from the fog toward camera and thunders past. Sound: the horn's long note, massed hooves, a war cry.
ACTION_START: horn note (insert) / fog empty
ACTION_END: cavalry line thundering past
NARRATION_KO: 해모루의 나각이 울렸습니다. 그 순간부터 갈대밭에는 말이 없었습니다.
DIALOGUE_KO: 
SOUND: tù và Goguryeo dài, vó ngựa dồn, hô.
CONTINUITY: 2-BEAT (3+5). → NARRATOR IM 31:24–33:00.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_105_radio_ep3, VEH_101_ref, PROP_018_ref, PROP_012_ref, LOC_007_fog_ep4
AI_RISK: 300 kỵ → low wide, sương che, nước bùn
INSERT_CLIP (3 s, tách riêng): Beat A insert, 3 s, extreme close-up in fog: lips on the bronze mouthpiece of a black buffalo-horn trumpet, one long deep note. Sound: a long low horn call rolling through fog.

### SC_227 | 31:24–31:32 | LOC_007 (LOC_007_camp_east_fog) | SUI_SOLDIERS_STARVING, XIANBEI_RIDERS_FOOT, GOG_CAVALRYMEN | WPN_201, VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide, static. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_007_south_camp_ep4: The east side of the Sui rear-guard camp in dense white dawn fog: grey felt tents, ox carts, a rough wall of red rectangular shields being raised, arrows flying out of the whiteness, wet grass and mud. Action: The camp: Sui soldiers pour toward the east side raising shields in haste; Goguryeo arrows fly in out of the fog; Xianbei riders wading into the water turn back — half return to the camp, half keep wading. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: shields going up, arrows out of the fog, riders in the water splitting. Sound: the Goguryeo horn, bowstrings, shouting, water.
ACTION_START: soldiers running east
ACTION_END: shield wall up, riders split
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: tù và Goguryeo, dây cung, hô, nước.
CONTINUITY: Narrator im.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, WPN_201_ref, VEH_101_ref, LOC_007_south_camp_ep4
AI_RISK: đám đông → wide

### SC_228 | 31:32–31:40 | LOC_007 (LOC_007_reed_path_fog) | CHAR_107, CHAR_006, CHAR_005, ROK_RAIDERS_2 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Medium shot at the reed wall, static
IMAGE_PROMPT: Medium shot at the reed wall, static. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: The girl parts the reeds at a place that looks like a solid wall — a hidden passage of flooded water just wide enough for one; she slips in; the scout stoops with the boy on his back and follows; the reeds close. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the reeds parted, the girl in, the scout stooping through with the boy, the two soldiers after, the reeds swinging shut. Sound: reeds rubbing, water, breathing.
ACTION_START: girl parting the reed wall
ACTION_END: reeds closing behind the last man
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: lau cọ, nước, thở.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_fog_ep4
AI_RISK: 3 nhân vật + 2 phụ → cửa lau hẹp, lần lượt

### SC_229 | 31:40–31:48 | LOC_007 (LOC_007_channel_fog) | XIANBEI_RIDER | WPN_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. Setting @LOC_007_fog_ep4: A channel of open brown water between the south shore and the reed beds in dense white dawn fog: waist-deep water, a wall of tall reeds fading into whiteness on one side, wet sand on the other, no far bank visible. Action: A single Xianbei rider on foot, waist-deep, follows the ripples with his bow drawn, eyes tracing the moving water to the reed wall; he stops before the hidden opening and tilts his head to listen. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the bow drawn, eyes on the ripples, the stop before the reed wall, head tilted. Sound: water settling, a bowstring creaking, breathing.
ACTION_START: rider following the ripples
ACTION_END: rider stopped at the reed wall
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: nước lặng, dây cung căng, thở.
CONTINUITY: Header ghi WPN_101 (cung Goguryeo) — thực là cung Tiên Ti (VEH_206); dán WPN_101 theo header, ref VEH_206 thêm.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, WPN_101_ref, LOC_007_fog_ep4

### SC_230 | 31:48–31:56 | LOC_007 (LOC_007_reed_path_fog) | CHAR_006, CHAR_005, ROK_RAIDERS_2 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot in the passage, static
IMAGE_PROMPT: Medium shot in the passage, static. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: Inside the reed passage the scout shifts the boy onto the second soldier's back with one turn of the shoulders, signs them to go on; he turns back, draws a deep breath, and sinks under the water without a ripple. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the boy passed to the other back, a hand sign, the scout turns, breathes, sinks without a ripple. Sound: cloth, an intake of breath, water closing.
ACTION_START: boy being transferred
ACTION_END: water closing over the scout
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: vải, hít, nước khép.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_fog_ep4

### SC_231 | 31:56–32:04 | LOC_007 (LOC_007_channel_fog) | CHAR_006, XIANBEI_RIDER | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up at water level, static (keyframe = beat A)
IMAGE_PROMPT: Close-up at water level, static (keyframe = beat A). @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. Setting @LOC_007_fog_ep4: A channel of open brown water between the south shore and the reed beds in dense white dawn fog: waist-deep water, a wall of tall reeds fading into whiteness on one side, wet sand on the other, no far bank visible. Action: At water level: the Xianbei rider steps into the reed passage — the water in front of him erupts as the scout comes up from beneath with the knife; the two turn over and over half under the brown water, only backs, arms and churned water visible; no wound shown. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): the rider steps in, the water erupts, two bodies rolling half submerged, backs and arms only. Beat B (4–8 s): insert — the water stills, one leather-clad arm sinks. Sound: water thrashing, a strangled breath, then silence.
ACTION_START: rider stepping into the passage
ACTION_END: water still, arm sinking (insert)
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: nước quật, thở gằn, im.
CONTINUITY: 2-BEAT (4+4). Không cận vết thương.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, VEH_206_ref, LOC_007_fog_ep4
AI_RISK: đánh dao dưới nước → chỉ lưng/tay/nước, không máu
INSERT_CLIP (4 s, tách riêng): Beat B insert, 4 s, wide at the mouth of the reed passage in thinning fog: the churned brown water goes still, ripples spreading out, and one arm in brown leather lamellar sinks below the surface; nothing else moves. Sound: water settling, silence.

### SC_232 | 32:04–32:12 | LOC_007 (LOC_007_reed_path_fog) | CHAR_107, CHAR_006 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close two-shot, static
IMAGE_PROMPT: Close two-shot, static. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: The girl turns back just as the water behind her clouds reddish-brown — her mouth opens, a scream starting; the scout surfaces right in front of her and a mud-black hand clamps over her mouth; her eyes huge above the hand. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close two-shot: the turn, the mouth opening, the scout surfacing, the hand over her mouth, the eyes huge. Sound: a cut-off scream, water, breathing.
ACTION_START: girl turning, mouth opening
ACTION_END: hand over her mouth, eyes wide
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: tiếng hét cụt, nước, thở.
CONTINUITY: Nước đổi màu (nhẹ), không cận.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, LOC_007_fog_ep4

### SC_233 | 32:12–32:20 | LOC_007 (LOC_007_reed_path_fog) | CHAR_006, CHAR_107 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Extreme close-up on two pairs of eyes, static
IMAGE_PROMPT: Extreme close-up on two pairs of eyes, static. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: Two pairs of eyes: the scout shakes his head once, slowly; the girl looks at him — nods; he takes his hand away; she wipes her mouth with the back of her hand, turns and leads on; no words. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static extreme close-up: the slow headshake, the nod, the hand withdrawn, the mouth wiped, she turns away. Sound: fog, breathing steadying, water.
ACTION_START: hand on her mouth
ACTION_END: girl turning to lead
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: sương, thở đều lại, nước.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_232
CUT_HALF: yes
REFS: CHAR_006_night_raid_ep4, CHAR_107_night_trail_ep4, LOC_007_fog_ep4

### SC_234 | 32:20–32:28 | LOC_007 (LOC_007_reed_path_fog) | CHAR_107, CHAR_006, CHAR_005, ROK_RAIDERS_2 | — | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Tracking shot from ahead in the narrow passage
IMAGE_PROMPT: Tracking shot from ahead in the narrow passage. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light. Action: Four in the narrow reed passage, water to the chest, reeds like walls on both sides; behind them the pursuers' splashing goes off in the wrong direction; the boy's face rests on a soldier's shoulder, eyes open, watching the reed tops drift past. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking from ahead: the file wades chest-deep, pursuit sounds veering away behind, the boy's open eyes on the reed tops. Sound: reeds, water, pursuit fading off to one side.
ACTION_START: file wading toward camera
ACTION_END: file passing, pursuit fading
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: lau, nước, tiếng đuổi lệch xa.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_233
CUT_HALF: yes
REFS: CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, LOC_007_fog_ep4

### SC_235 | 32:28–32:36 | LOC_007 (LOC_007_camp_east_fog) | CHAR_205, XIANBEI_RIDERS_FOOT, GOG_CAVALRYMEN | VEH_101, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_south_camp_ep4: The east side of the Sui rear-guard camp in dense white dawn fog: grey felt tents, ox carts, a rough wall of red rectangular shields being raised, arrows flying out of the whiteness, wet grass and mud. Action: The commander stands in the middle of the camp — to the east Goguryeo cavalry shoot and wheel, tents going down; from the river, the sound of water; he looks east, looks toward the river; points to the river — choosing the small prey over the big fight; his riders lead horses down into the water after him. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the look east, the look to the river, the arm pointing at the river, one shouted line, horses led into the water. Sound: bowstrings east, shouting, horses into water, one line of Korean dialogue.
ACTION_START: commander looking east
ACTION_END: arm pointing at the river, horses moving
NARRATION_KO: 
DIALOGUE_KO: 탁발흠: 강이다. 강으로!
SOUND: dây cung đông, hô, ngựa xuống nước.
CONTINUITY: '강이다. 강으로!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, VEH_206_ref, VEH_101_ref, EQP_001_ref, LOC_007_south_camp_ep4

### SC_236 | 32:36–32:44 | LOC_007 (LOC_007_north_ford) | CHAR_002 | WPN_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up in the reed hole, static
IMAGE_PROMPT: Close-up in the reed hole, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The lieutenant sees through thinning fog on the channel south of the sandbar: shapes of horses and men — Xianbei riders on horseback wading across the water, bows in hand, following the reed passage from outside; he drags the poncho off the heavy machine gun. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the shapes in the fog, the poncho dragged off the gun, the safety clicked. Sound: horses wading far off, the poncho, a safety catch.
ACTION_START: staring at the shapes
ACTION_END: poncho off the gun
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: ngựa lội xa, poncho, khóa an toàn.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, WPN_004_ref, LOC_007_detail

### SC_237 | 32:44–32:52 | LOC_007 (LOC_007_north_ford) | CHAR_002 | WPN_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the lieutenant's face, static
IMAGE_PROMPT: Close-up on the lieutenant's face, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The lieutenant's finger rests on the heavy machine gun's trigger; he turns his head toward the second island two hundred meters off — only white fog, no tank, no captain; turns back and looks down at the river. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the finger on the trigger, the head turning to white fog, turning back, the look down at the river. Sound: fog, horses wading, breathing.
ACTION_START: looking toward the island
ACTION_END: looking down at the river
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: sương, ngựa lội, thở.
CONTINUITY: Không thoại. Ngón tay trên cò K6 (không cận ngón — cận mặt).
CHAIN_FROM: SC_236
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, WPN_004_ref, LOC_007_detail
AI_RISK: ngón tay trên cò → cận mặt, tay mờ mép khung

### SC_238 | 32:52–33:00 | LOC_007 (LOC_007_sandbar_north_fog) | CHAR_107, CHAR_006, CHAR_005, ROK_RAIDERS_2, XIANBEI_RIDER | VEH_206 | PROPS: PROP_020 | TYPE: video8s | 8s
SHOT: Wide from the north bank, static
IMAGE_PROMPT: Wide from the north bank, static. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_fog_ep4: A low wet sandbar on the north side of the shallow river in thinning dawn fog: grey sand, a wall of tall reeds behind it, a hundred meters of open brown water to the reed beds of the north bank, fog lifting in ribbons. Action: The girl bursts out of the reed wall onto the north sandbar, falls, scrambles up; the scout and the soldier carrying the boy follow; ahead of them a hundred meters of open water to the north bank; behind, three Xianbei riders on horseback have rounded the end of the reeds and come wading eighty meters off. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide from the north bank: the group tumbles out onto the sandbar, three riders wading toward them from behind. Sound: sand, water, hooves in water.
ACTION_START: girl bursting out, falling
ACTION_END: group on the sandbar, riders closing behind
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: cát, nước, vó ngựa trong nước.
CONTINUITY: Kết Phase 4. 3 kỵ (VEH_206).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, CHAR_005_captive_ep3, VEH_206_ref, LOC_007_fog_ep4
AI_RISK: nhiều người + ngựa → wide xa

### SC_239 | 33:00–33:08 | LOC_007 (LOC_007_channel_north_fog) | GOG_CAVALRYMEN | VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Lateral tracking shot at water level  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Lateral tracking shot at water level. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_007_fog_ep4: The channel of brown water between the north sandbar and the reed beds of the north bank in thinning dawn fog: waist-deep water, tall reeds on the north side, fog lifting, rain beginning. Action: From the reed edge on the north bank twenty Goguryeo armored cavalry plunge into the water toward the sandbar — no banner, no horn, only horses and lances; water thrown up in a wall. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Lateral tracking: the riders plunge in, water rising in a wall beside them. Sound: hooves in water, armor.
ACTION_START: riders entering the water
ACTION_END: riders mid-channel, water flying
NARRATION_KO: 해모루는 삼백을 둘로 나눴습니다. 이백팔십은 동쪽으로, 스물은 여기로. 스물은 소리를 내지 않았습니다.
DIALOGUE_KO: 
SOUND: vó ngựa trong nước, giáp.
CONTINUITY: Narrator quay lại 33:00. 20 kỵ.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_101_ref, LOC_007_fog_ep4
AI_RISK: kỵ số đông → tracking, nước che chân ngựa

### SC_240 | 33:08–33:16 | LOC_007 (LOC_007_sandbar_north_fog) | CHAR_005, CHAR_107, CHAR_006, GOG_CAVALRYMEN, ROK_RAIDERS_2 | VEH_101 | PROPS: — | TYPE: video8s | 8s
SHOT: Fast wide on the sandbar, static (keyframe = beat B)
IMAGE_PROMPT: Fast wide on the sandbar, static (keyframe = beat B). @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_006_night_raid_ep4: 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. Setting @LOC_007_fog_ep4: A low wet sandbar on the north side of the shallow river in thinning dawn fog: grey sand, a wall of tall reeds behind it, a hundred meters of open brown water to the reed beds of the north bank, fog lifting in ribbons. Action: Fast wide: the scout seizes the stirrup of one horse, the two soldiers grab another's tail; the horses swing around toward the north bank; a rider shouts. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–4 s): insert — the boy hauled across a saddle, the girl swung up behind a rider. Beat B (4–8 s): fast wide — the scout on a stirrup, the soldiers on a tail, horses swinging north; one shouted line. Sound: horses screaming, armor, water, one shouted line of Korean dialogue.
ACTION_START: boy hauled up (insert) / group on the sandbar
ACTION_END: horses turning north with everyone attached
NARRATION_KO: 천사백 년 전의 말이 천사백 년 뒤의 병사를 업었습니다. 석문령에서 한 번 그랬습니다. 살수에서 다시 그랬습니다.
DIALOGUE_KO: 고구려 기병: 올려!
SOUND: ngựa hí, giáp, nước, thở.
CONTINUITY: 2-BEAT (4+4). '올려!'
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_005_captive_ep3, CHAR_107_night_trail_ep4, CHAR_006_night_raid_ep4, VEH_101_ref, LOC_007_fog_ep4
AI_RISK: nhiều người + ngựa → wide nhanh; insert cận 2 người
INSERT_CLIP (4 s, tách riêng): Beat A insert, 4 s, close-up on the sandbar: an armored Goguryeo gauntlet hauls a thin boy in a torn camouflage uniform up across a saddle; a girl in a hemp jacket with a dark head cloth is swung up behind another rider. Sound: horses, armor, a gasp.

### SC_241 | 33:16–33:24 | LOC_007 (LOC_007_channel_north_fog) | XIANBEI_RIDER | VEH_206, WPN_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide over the channel, static (keyframe = beat B)  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide over the channel, static (keyframe = beat B). a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. Setting @LOC_007_fog_ep4: The channel of brown water between the north sandbar and the reed beds of the north bank in thinning dawn fog: waist-deep water, tall reeds on the north side, fog lifting, rain beginning. Action: Wide: a row of water columns erupts across the channel directly in front of three Xianbei horses eighty meters out; the horses rear straight up and throw their riders into the water. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Beat A (0–3 s): insert — the muzzle flaming, casings flying. Beat B (3–8 s): wide — the row of water columns erupts before the three horses, they rear and throw their riders. Sound: the heavy gun's roar, water bursting, horses screaming.
ACTION_START: muzzle burst (insert) / horses wading
ACTION_END: horses rearing, riders in the water
NARRATION_KO: 한 번. 마흔 발. 살수에서 나는 마지막 총소리였습니다. 그다음 총소리는 삼십만 앞에서 날 것이었습니다.
DIALOGUE_KO: 
SOUND: K6 12.7 gầm một loạt, nước bùng, ngựa hí.
CONTINUITY: 2-BEAT (3+5). K6 −40. Header ghi CHAR_002 nhưng keyframe wide không thấy anh (chỉ nòng K6 ở insert) → không dán lock (né AI chèn người vào wide).
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_206_ref, WPN_004_ref, LOC_007_fog_ep4
AI_RISK: ngựa dựng ×3 → wide xa, cột nước che
INSERT_CLIP (3 s, tách riêng): Beat A insert, 3 s, close on the muzzle of a heavy machine gun in a reed hole on the north bank: a long burst, muzzle flame flickering, spent brass casings flying. Sound: a heavy machine gun roaring one long burst.

### SC_242 | 33:24–33:32 | LOC_007 (LOC_007_sandbar_north_fog) | CHAR_205, XIANBEI_RIDER | VEH_206, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the mounted commander, static
IMAGE_PROMPT: Close-up on the mounted commander, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_007_fog_ep4: A low wet sandbar on the north side of the shallow river in thinning dawn fog: grey sand, a wall of tall reeds behind it, a hundred meters of open brown water to the reed beds of the north bank, fog lifting in ribbons. Action: The commander reins in on a horse at the edge of the south sandbar, the night-vision device hanging on his chest, watching his three soaked riders crawl back; looks at the north bank where gun smoke dissolves into fog; raises one hand — no more pursuit. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: reins hauled, the look at the crawling riders, the look at the smoke, the hand raised. Sound: the horse, water, silence after gunfire.
ACTION_START: reining in
ACTION_END: hand raised
NARRATION_KO: 탁발흠은 쫓지 않았습니다. 마흔 발이 어디서 왔는지 그는 들었습니다. 북쪽 여울. 그는 그 자리를 기억했습니다.
DIALOGUE_KO: 
SOUND: ngựa, nước, im sau loạt súng.
CONTINUITY: Không thoại. Mô cát nam (sub-lock sandbar_north_fog dùng chung — mép sương).
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, VEH_206_ref, EQP_001_ref, LOC_007_fog_ep4

### SC_243 | 33:32–33:40 | LOC_007 (LOC_007_island2_k2) | CHAR_001 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the hand and face in the hatch, static
IMAGE_PROMPT: Close-up on the hand and face in the hatch, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The captain in the turret hatch: his hand rests on the guarded cover of the commander's firing switch — not lifted; he draws the hand back and lays it on the muddy hatch rim; the gun barrel still wrapped in reeds. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the hand on the switch cover, withdrawn, laid on the mud; the face still. Sound: electronics hum, distant gunfire already gone, fog.
ACTION_START: hand on the switch cover
ACTION_END: hand on the hatch rim
NARRATION_KO: 전차는 쏘지 않았습니다. 여섯 발은 여섯 발로 남았습니다. 한승우는 손을 거두었습니다. 그것도 결정이었습니다.
DIALOGUE_KO: 
SOUND: quạt điện tử, súng xa đã tắt, sương.
CONTINUITY: Không thoại. K2 không bắn.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_001_reeds_ep4, VEH_001_ref, LOC_007_island_ep4
AI_RISK: công tắc → không chữ, nắp che

### SC_244 | 33:40–33:48 | LOC_007 (LOC_007_north_ford) | CHAR_002, CHAR_005, GOG_CAVALRYMEN | VEH_101, WPN_004 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @WPN_004_ref: K6 12.7mm heavy machine gun, long boxy steel receiver, thick perforated barrel jacket, twin spade grips, wide 12.7mm ammunition belt, mounted on a heavy olive tripod. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The Goguryeo horses come up onto the north bank and plunge into the reeds; the lieutenant lowers the still-smoking heavy machine gun and stands up in his hole, watching the boy slung across a saddle go past — their eyes meet for one beat. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: horses up the bank, the gun lowered, the lieutenant standing, the boy on the saddle passing, the eyes meeting. Sound: horses on mud, hot steel hissing in light rain, breathing.
ACTION_START: horses coming up the bank
ACTION_END: boy passing, eyes meeting
NARRATION_KO: 북쪽 여울이 열렸다가 닫혔습니다. 오태민이 지킨 문이었습니다. 문은 제 몫을 했습니다.
DIALOGUE_KO: 
SOUND: ngựa lên bùn, thép nóng xèo trong mưa nhỏ, thở.
CONTINUITY: Không thoại. Mưa nhỏ bắt đầu lại.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_002_reeds_ep4, CHAR_005_captive_ep3, VEH_101_ref, WPN_004_ref, LOC_007_detail

### SC_245 | 33:48–33:56 | LOC_007 (LOC_007_water_point) | CHAR_205 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the pin and the face, static
IMAGE_PROMPT: Close-up on the pin and the face, static. @CHAR_205_ref: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face. Setting @LOC_007_south_camp_ep4: The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog. Action: The commander walks to the empty cage and kicks it — bamboo cracks; he stoops and picks up the wooden pin from the sand, cut clean — one straight stroke; looks at the cut a long moment, then out at the fog to the north. Light: Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the kick, the pin lifted, the cut studied, the look north. Sound: bamboo cracking, wood in the hand, fog.
ACTION_START: kicking the cage
ACTION_END: pin in hand, looking north
NARRATION_KO: 그는 화내지 않았습니다. 배웠습니다. 칼 한 자루가 안개 속에서 야시경을 이겼습니다. 그는 그 칼자국을 오래 보았습니다.
DIALOGUE_KO: 
SOUND: tre gãy, gỗ trên tay, sương.
CONTINUITY: Không thoại. Bài học thứ 4.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_205_ref, LOC_007_south_camp_ep4

### SC_246 | 33:56–34:04 | LOC_007 (LOC_007_aid) | CHAR_005, CHAR_004, CHAR_106, ROK_SOLDIERS | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Medium shot under the reed roof, static
IMAGE_PROMPT: Medium shot under the reed roof, static. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: The boy laid on the reeds; the medic kneels and cuts the filthy cloth from his swollen black foot with shears; the old blacksmith holds an unlit lantern aside, useless — only daylight through the reeds; soldiers stand silent around. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the shears cut the cloth, the old man holds the unlit lantern, the medic says one clipped line. Sound: shears, breathing, silence, one line of Korean dialogue.
ACTION_START: medic beginning to cut the cloth
ACTION_END: foot bared, line spoken
NARRATION_KO: 태오가 갈대 위에 놓였습니다. 아무도 소리를 내지 않았습니다. 이 부대는 이제 소리 내는 법을 잊고 있었습니다.
DIALOGUE_KO: 서아: 부러졌습니다. 모르핀은 안 씁니다.
SOUND: kéo cắt vải, thở, im.
CONTINUITY: '부러졌습니다. 모르핀은 안 씁니다.' 태오 vẫn cage_ep4 (chưa áo gai).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_captive_ep3, CHAR_004_braid_ep4, CHAR_106_ref, PROP_009_ref, LOC_007_island_ep4
AI_RISK: 3 nhân vật + lính → tĩnh, lính nền mờ

### SC_247 | 34:04–34:12 | LOC_007 (LOC_007_aid) | CHAR_001, CHAR_005 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close two-shot, static
IMAGE_PROMPT: Close two-shot, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: The captain kneels at the boy's head; the boy lifts his face, split lip, red eyes, and cannot finish his sentence. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close two-shot: the face lifted, one broken line that trails away. Sound: breathing, reeds, one line of Korean dialogue.
ACTION_START: captain kneeling
ACTION_END: boy's face lifted, words failing
NARRATION_KO: 드론. 그가 잃은 것은 그것이었습니다. 그는 자신을 잃은 것으로 세지 않았습니다.
DIALOGUE_KO: 장태오: 죄송합니다… 드론을…
SOUND: thở, lau.
CONTINUITY: '죄송합니다… 드론을…'
CHAIN_FROM: SC_246
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_005_captive_ep3, LOC_007_island_ep4

### SC_248 | 34:12–34:20 | LOC_007 (LOC_007_aid) | CHAR_001, CHAR_005 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the hands, static
IMAGE_PROMPT: Close-up on the hands, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: The captain's muddy hand rests on the boy's hacked-short hair; with the other hand he sets down on the reeds beside the boy's head a ROK ballistic helmet with an empty night-vision mount on its front — the boy's own helmet, carried since the pass; he says one line, looking at no one else. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: hand on the hair, the helmet with the empty mount set down beside the head, one line. Sound: silence, one line of Korean dialogue.
ACTION_START: hand on the hair
ACTION_END: helmet set down, line spoken
NARRATION_KO: 보름 전 한승우는 이 소년에게 살아 있으라고 했습니다. 소년은 그 말을 지켰습니다.
DIALOGUE_KO: 한승우: 살아 있잖아.
SOUND: im.
CONTINUITY: '살아 있잖아.' Mũ Hàn trống ngàm kính (phương án B, decisions QC 4화) — KHÔNG dán lock EQP_001 (không có kính).
CHAIN_FROM: SC_247
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_005_captive_ep3, LOC_007_island_ep4
AI_RISK: mũ trống ngàm → 'empty night-vision mount', không thiết bị

### SC_249 | 34:20–34:30 | LOC_007 (LOC_007_island2) | CHAR_107, CHAR_106, ROK_SOLDIERS | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium shot, slow push-in to the two
IMAGE_PROMPT: Still for ken-burns: medium shot, slow push-in to the two. @CHAR_107_night_trail_ep4: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: The girl sits on the reeds hugging her knees, shaking without stopping, the olive scarf soaked; the old blacksmith kneels behind her holding her, his chin on her head; behind them, blurred, soldiers stand silent — no cheering. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the girl and the old man. Sound: rain beginning again, the river.
ACTION_START: girl and old man, soldiers behind
ACTION_END: tight on the two
NARRATION_KO: 태오는 돌아왔습니다. 드론과 쇠수레는 이미 서쪽으로 열흘째 가고 있었습니다.
DIALOGUE_KO: 
SOUND: mưa bắt đầu lại, sông.
CONTINUITY: Still 10 s. Kết P10.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_107_night_trail_ep4, CHAR_106_ref, LOC_007_island_ep4


## [Phần 11] 여울 북쪽 (34:30–37:30) · chết vì nhiễm trùng · 91명 · mũ trụ Goguryeo · 방진 rút · 탁발흠 quỳ

### SC_250 | 34:30–34:40 | LOC_007 (LOC_007_aid) | CHAR_004, ROK_WOUNDED | — | PROPS: PROP_009 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: close-up under the reed roof in red light, slow push-in to the hand on the wrist
IMAGE_PROMPT: Still for ken-burns: close-up under the reed roof in red light, slow push-in to the hand on the wrist. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: Night under the reed roof, a red flashlight shielded by a hand: the wounded soldier lies with a yellow sweating face and cracked lips; the medic sits beside him, a wet cloth on his forehead, her other hand on his wrist counting the pulse. Light: Night, dim red flashlight light shielded by a hand on faces and hands, deep black shadows beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the hand on the wrist. Sound: rain, shallow rapid breathing.
ACTION_START: medic and wounded man in red light
ACTION_END: tight on the hand on the wrist
NARRATION_KO: 사흘째 밤이었습니다. 열은 배에서 시작해 온몸으로 갔습니다. 서아는 그것을 알면서 앉아 있었습니다.
DIALOGUE_KO: 
SOUND: mưa, thở nông và nhanh.
CONTINUITY: Still 10 s. Đêm D7 (đêm thứ 3). ROK_WOUNDED.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, EXTRA_rok_wounded_ref, PROP_009_ref, LOC_007_island_ep4

### SC_251 | 34:40–34:48 | LOC_007 (LOC_007_aid) | CHAR_004, ROK_WOUNDED | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Close-up, static, red light
IMAGE_PROMPT: Close-up, static, red light. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: The medic presses a morphine autoinjector into his thigh; his hand closes on hers; she does not pull away; she speaks softly. Light: Night, dim red flashlight light shielded by a hand on faces and hands, deep black shadows beyond. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the injector, his hand closing on hers, held, one soft line. Sound: the injector click, breathing, rain, one line of Korean dialogue.
ACTION_START: injector at the thigh
ACTION_END: hands held, line spoken
NARRATION_KO: 모르핀 하나. 그것이 그녀가 줄 수 있는 전부였습니다. 그리고 손 하나.
DIALOGUE_KO: 서아: 괜찮아요. 자요. 제가 있어요.
SOUND: ống tiêm, thở, mưa.
CONTINUITY: '괜찮아요. 자요. 제가 있어요.' Morphine 9→8.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_004_braid_ep4, EXTRA_rok_wounded_ref, PROP_009_ref, LOC_007_island_ep4

### SC_252 | 34:48–34:56 | LOC_007 (LOC_007_aid) | CHAR_004, ROK_WOUNDED | — | PROPS: PROP_009 | TYPE: video8s | 8s
SHOT: Close-up, static, near dark
IMAGE_PROMPT: Close-up, static, near dark. @CHAR_004_braid_ep4: 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat. @PROP_009_ref: olive-green medic shoulder bag with a small red cross patch and many zipped pockets, spilling rolled bandages, an orange tourniquet, trauma shears, morphine autoinjectors and an empty white plastic antibiotic bottle, a small brown hemp pouch of dried Goguryeo herbs tied to the strap. Setting @LOC_007_island_ep4: The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view. Action: Before dawn: his chest stops rising; the medic stays as she is for a while, hand on his wrist; then she reaches over and closes his eyes, and writes the time in her notebook. Light: The dark before dawn, faint blue-grey light, rain, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up in near darkness: the chest still, the long pause, the hand closing the eyes, the pencil moving. Sound: rain; the breathing gone; a pencil.
ACTION_START: hand on the wrist, chest still
ACTION_END: eyes closed, pencil on the notebook
NARRATION_KO: 사흘째 밤이 끝나기 전에 그는 갔습니다. 화살이 아니라 열이 데려갔습니다. 천사백 년 뒤의 약이 없어서였습니다.
DIALOGUE_KO: 
SOUND: mưa; tiếng thở không còn; bút chì.
CONTINUITY: Không thoại. Chữ trong sổ không thấy (tối).
CHAIN_FROM: SC_251
CUT_HALF: no
REFS: CHAR_004_braid_ep4, EXTRA_rok_wounded_ref, PROP_009_ref, LOC_007_island_ep4
AI_RISK: người chết → mặt yên, không chi tiết

### SC_253 | 34:56–35:04 | LOC_007 (LOC_007_island2) | CHAR_105, CHAR_001, ROK_SOLDIERS, GOG_CAVALRYMEN | — | PROPS: PROP_019, PROP_020 | TYPE: video8s | 8s
SHOT: Medium shot at the grave, static
IMAGE_PROMPT: Medium shot at the grave, static. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @PROP_019_ref: hand-forged iron pry bar one point two meters long with a flattened end and a hooked end showing hammer marks, and a modern folding entrenching shovel re-handled with a new oak shaft and a hand-forged iron collar. bundles of wet two-meter grey-green river reeds with pale silver feathered plumes, tied with cord, used as camouflage on helmets and tank. Setting @LOC_007_island_ep4: A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke. Action: Grey morning, light rain: a shallow sand grave among the reeds, the poncho-wrapped body lowered in; ROK soldiers and two Goguryeo cavalrymen fill it together by hand and with the oak-handled entrenching shovel; the young officer takes off his helmet and bows his head in the Goguryeo manner; the captain stands at the head of the grave. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the body lowered, sand pushed in by hands and the shovel, the officer bareheaded and bowing, one line from him. Sound: sand falling, rain, silence, one line of Korean dialogue.
ACTION_START: body being lowered
ACTION_END: grave half filled, officer bowing
NARRATION_KO: 갈대 사이에 묻었습니다. 석문령에서 하나, 여기서 둘. 천사백 년 뒤의 사람들을 이 땅의 사람들이 함께 덮었습니다.
DIALOGUE_KO: 해모루: 이 땅에 눕는 것이오. 편히 가시오.
SOUND: cát đổ, mưa, im.
CONTINUITY: '이 땅에 눕는 것이오. 편히 가시오.' PROP_019 = xẻng cán sồi. 2 kỵ Goguryeo xuống ngựa (không VEH_101 — người).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_105_radio_ep3, CHAR_001_reeds_ep4, PROP_019_ref, LOC_007_island_ep4
AI_RISK: nhiều người → tĩnh, mặt lính cúi

### SC_254 | 35:04–35:12 | LOC_007 (LOC_007_shelter) | CHAR_003 | — | PROPS: PROP_001 | TYPE: video8s | 8s
SHOT: Close-up on the notebook and pencil, static
IMAGE_PROMPT: Close-up on the notebook and pencil, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. @PROP_001_ref: folded South Korean army topographic paper map with brown contour lines, pale green forest areas and a black grid, red and blue grease-pencil marks, its back side covered in charcoal sketches of a river, a fortress and a route, creased, dusty, later mud-stained. Setting @LOC_007_island_ep4: Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light. Action: The sergeant opens the wet notebook and draws a pencil line through a figure, writing a new one beside it; on the line below another figure struck through and replaced; he reads it under his breath like a prayer. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the pencil strikes through, writes beside, strikes through below, one line murmured. Sound: pencil, rain, one line of Korean dialogue.
ACTION_START: pencil on the first figure
ACTION_END: second figure replaced, line murmured
NARRATION_KO: 아흔넷으로 왔습니다. 이제 아흔하나였습니다. 박기철은 그 숫자를 두 번 말하지 않았습니다. 한 번으로 충분했습니다.
DIALOGUE_KO: 박기철: 아흔한 명. 야시경 배터리 이십. 무전기 삼십.
SOUND: bút chì, mưa.
CONTINUITY: '아흔한 명. 야시경 배터리 이십. 무전기 삼십.' [OVERLAY] 92→91, 30→20 (số thật ở edit; ảnh nét chì mờ).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, PROP_001_ref, LOC_007_island_ep4
OVERLAY (edit): 92 → 91 · 30 → 20 (gạch số cũ, viết số mới cạnh — sổ 박기철)
AI_RISK: chữ → blurred pencil, OVERLAY

### SC_255 | 35:12–35:20 | LOC_007 (LOC_007_island2_k2) | CHAR_005, CHAR_105 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot beside the tank's skirt, static
IMAGE_PROMPT: Medium two-shot beside the tank's skirt, static. @CHAR_005_captive_ep3: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, straw sandals, no helmet, exhausted relief. @CHAR_105_radio_ep3: 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The boy sits against the mud-caked skirt of the tank, right leg splinted with reed bundles and bandage, a coarse hemp jacket open over his torn camouflage; beside his thigh a ROK ballistic helmet with an empty night-vision mount; the young officer holds a Goguryeo iron helmet of vertical riveted plates without a plume and lowers it onto the boy's head, adjusting the chin strap; the boy's hand rises to touch the iron rim. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: the iron helmet lowered onto the head, the strap adjusted, the boy's fingers touching the rim, one line from the officer. Sound: iron, leather strap, rain, one line of Korean dialogue.
ACTION_START: officer holding the iron helmet above the boy's head
ACTION_END: helmet on, boy touching the rim
NARRATION_KO: 빈 철모는 한승우가 석문령에서 가지고 왔습니다. 해모루가 먼저 육백십이 년의 쇠를 씌웠습니다. 태오는 벗지 않았습니다.
DIALOGUE_KO: 해모루: 머리는 쇠로 덮는 법이오. 어느 해 것이든.
SOUND: sắt chạm, quai da, mưa.
CONTINUITY: '머리는 쇠로 덮는 법이오. 어느 해 것이든.' Mũ Hàn trống ngàm bên đùi (phương án B). rescued_ep4 + nẹp chân (action).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_captive_ep3, CHAR_105_radio_ep3, VEH_001_ref, LOC_007_island_ep4
AI_RISK: 2 mũ trong khung → mũ Hàn 'empty mount', mũ sắt 'no plume'

### SC_256 | 35:20–35:28 | LOC_007 (LOC_007_island2_k2) | CHAR_107, CHAR_005 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. @CHAR_005_goguryeo_helmet_ep5: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The girl sits down beside the boy in the iron helmet, looks at the helmet, then asks him the question she asked on the road south. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: she sits, looks at the helmet, one question. Sound: rain, reeds, one line of Korean dialogue.
ACTION_START: girl sitting down
ACTION_END: question asked
NARRATION_KO: 남하하는 길에서 아리는 그 시의 뜻을 물었습니다. 그때 태오는 나중에 알게 된다고 했습니다. 나중이 왔습니다.
DIALOGUE_KO: 아리: 오라버니, 그 시… 무슨 뜻이에요?
SOUND: mưa, lau.
CONTINUITY: '오라버니, 그 시… 무슨 뜻이에요?' 태오 helmet_ep4 (ref goguryeo_helmet_ep5).
CHAIN_FROM: SC_255
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_005_goguryeo_helmet_ep5, VEH_001_ref, LOC_007_island_ep4

### SC_257 | 35:28–35:36 | LOC_007 (LOC_007_island2_k2) | CHAR_005 | VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the boy, static
IMAGE_PROMPT: Close-up on the boy, static. @CHAR_005_goguryeo_helmet_ep5: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The boy looks at the river through the reeds and answers slowly — not in an exam voice anymore. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: eyes on the river, one slow line. Sound: river, one line of Korean dialogue.
ACTION_START: looking at the river
ACTION_END: answer given
NARRATION_KO: 시험에서는 이 뜻을 쓰면 점수를 받았습니다. 여기서는 점수가 없었습니다.
DIALOGUE_KO: 장태오: 이만하면 됐으니 그만두라는 뜻이야.
SOUND: sông.
CONTINUITY: '이만하면 됐으니 그만두라는 뜻이야.'
CHAIN_FROM: SC_256
CUT_HALF: no
REFS: CHAR_005_goguryeo_helmet_ep5, VEH_001_ref, LOC_007_island_ep4

### SC_258 | 35:36–35:44 | LOC_007 (LOC_007_island2_k2) | CHAR_107, CHAR_005 | EQP_002, VEH_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium two-shot, static
IMAGE_PROMPT: Medium two-shot, static. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. @CHAR_005_goguryeo_helmet_ep5: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The girl asks again; the boy does not answer — he reaches for the radio handset hanging on the tank's track, sets it on his thigh, and looks south. Light: Grey morning in light rain, flat cold grey-green light, thin mist on the water. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static two-shot: her question, no answer, the handset taken down and set on the thigh, the look south. Sound: faint radio static, rain, one line of Korean dialogue.
ACTION_START: girl asking
ACTION_END: handset on the boy's thigh, looking south
NARRATION_KO: 책에는 그렇게 씌어 있었습니다. 그들은 그만두고 돌아갔다고. 태오는 그 말을 하지 않았습니다. 책은 그가 여기 있는 것을 몰랐습니다.
DIALOGUE_KO: 아리: 그만둘까요, 그 사람들?
SOUND: radio nhiễu nhỏ, mưa.
CONTINUITY: '그만둘까요, 그 사람들?' Radio = việc mới của 태오.
CHAIN_FROM: SC_257
CUT_HALF: no
REFS: CHAR_107_scarf_ep2, CHAR_005_goguryeo_helmet_ep5, EQP_002_ref, VEH_001_ref, LOC_007_island_ep4

### SC_259 | 35:44–35:54 | LOC_008 (LOC_008_road_west) | XIANBEI_RIDER, OXEN_CARTS | VEH_002, VEH_206 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: high aerial in rain, slow slide along the train  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: high aerial in rain, slow slide along the train. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. two-wheeled wooden ox carts loaded with rope-bound chests, oxen under wooden yokes. @VEH_002_captured: South Korean K21 infantry fighting vehicle, angular boxy hull with steep sloped front, small two-man turret offset right with a short 40mm autocannon, folded flotation panels along the hull sides, six road wheels per side, rear troop ramp, three-tone green-brown-black camouflage, small white numeral and a small Korean flag on the turret side. Under a lashed-down cover of dark hides on a heavy wooden ox cart drawn by many oxen, only the boxy shape and one road wheel showing. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_008_hills_rain_ep4: A muddy road winding west between low green hills in monsoon rain, 612 AD, seen from above: a long train of two-wheeled ox carts, mud, wet scrub, low grey cloud. Action: From above in rain: a long train of ox carts on a muddy road winding west between low green hills; in the middle a huge shape under lashed dark hides on a heavy cart drawn by many oxen, a wooden crate roped beside it; two hundred Xianbei riders escorting. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide along the train to the covered shape. Sound: oxen, wooden wheels, rain.
ACTION_START: head of the train
ACTION_END: the covered shape and crate
NARRATION_KO: 같은 시각, 서쪽 삼백 킬로. 소 마흔 마리가 끄는 수레 위에 쇠수레 하나와 상자 하나가 있었습니다. 요동으로, 그리고 황제에게로 가는 길이었습니다. 역사에 없던 짐이었습니다.
DIALOGUE_KO: 
SOUND: bò, bánh xe gỗ, mưa.
CONTINUITY: Still 10 s. 천둥 3 phủ bạt (VEH_002_captured ref) + hộp drone. 300 km về tây.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_002_captured, VEH_206_ref, LOC_008_hills_rain_ep4
AI_RISK: xe dưới bạt → chỉ khối phủ da

### SC_260 | 35:54–36:02 | LOC_008 (LOC_008_square) | GOG_CAVALRYMEN, SUI_SOLDIERS_STARVING | WPN_201, VEH_101 | PROPS: PROP_021 | TYPE: video8s | 8s
SHOT: Medium-high aerial, static  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Medium-high aerial, static. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_hills_rain_ep4: A muddy road through low green hills in monsoon rain: an enormous square formation of Sui infantry crawling north along it, four sides of red rectangular shields and long spears, ox carts in the center, wet red and yellow banners, mud churned to soup, low grey cloud. Action: An enormous square of Sui infantry crawls north along the muddy road: four sides of red shields and spears, ox carts in the center; Goguryeo cavalry sweep down from a hill, shoot into a flank and wheel away; here and there a side of the square dents inward. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static aerial: the square crawls, cavalry sweep in, loose, wheel away, a side of the square dents and reforms. Sound: slow Sui drums, bowstrings, shouts, rain.
ACTION_START: square crawling, cavalry on the hill
ACTION_END: cavalry wheeling away, side dented
NARRATION_KO: 방진은 살수로 향했습니다. 고구려 군은 네 방향에서 쳤습니다. 치고 물러나고, 치고 물러났습니다. 삼국사기의 문장 그대로였습니다.
DIALOGUE_KO: 
SOUND: trống Tùy chậm, dây cung, hô, mưa.
CONTINUITY: [史] 방진. Aerial.
CHAIN_FROM: —
CUT_HALF: yes
REFS: WPN_201_ref, VEH_101_ref, PROP_021_ref, LOC_008_hills_rain_ep4
AI_RISK: đại quân → aerial

### SC_261 | 36:02–36:10 | LOC_008 (LOC_008_square_inside) | CHAR_202, CHAR_203, SUI_SOLDIERS_STARVING, OXEN_CARTS | VEH_207, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Lateral tracking shot inside the square
IMAGE_PROMPT: Lateral tracking shot inside the square. @CHAR_202_ref: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Armor and breast mirrors streaming with rain, red cloak heavy with water, white beard dripping, mud splashed to the thighs. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. two-wheeled wooden ox carts loaded with rope-bound chests, oxen under wooden yokes. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_008_hills_rain_ep4: Inside the marching square of Sui infantry on a muddy road in rain: walls of soldiers with red rectangular shields and spears on every side, ox carts creaking through mud in the center, exhausted men, wet banners, low grey sky. Action: Inside the square: the white-bearded general rides in the center with the grey-bearded deputy beside him on tall warhorses; Goguryeo arrows drop a few meters off; a Sui soldier walking beside an ox cart buckles from hunger, is hauled up by the man behind, then left where he falls. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking inside the square: arrows dropping nearby, the soldier buckling, hauled up, left; the deputy says one line without turning. Sound: arrows in mud, horses, dragging feet, rain, one line of Korean dialogue.
ACTION_START: two generals riding, soldier walking
ACTION_END: soldier left behind, generals riding on
NARRATION_KO: 진 안에서 사람이 쓰러졌습니다. 화살이 아니라 배가 쓰러뜨렸습니다. 방진은 쓰러진 사람을 두고 갔습니다. 멈추면 진이 아니었습니다.
DIALOGUE_KO: 우문술: 두고 가시오.
SOUND: tên rơi, ngựa, chân lê, mưa.
CONTINUITY: '두고 가시오.' VEH_207 (LOCK_PENDING) cho 2 tướng trên ngựa.
CHAIN_FROM: —
CUT_HALF: yes
REFS: CHAR_202_ref, CHAR_203_ref, VEH_207_ref, WPN_201_ref, LOC_008_hills_rain_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)
AI_RISK: 2 tướng + đám đông → tracking ngang, lính phụ out-focus

### SC_262 | 36:10–36:18 | LOC_008 (LOC_008_square_head) | CHAR_205, CHAR_202 | VEH_206, VEH_207, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle from the kneeling man's level, static
IMAGE_PROMPT: Low angle from the kneeling man's level, static. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs. @CHAR_202_ref: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Armor and breast mirrors streaming with rain, red cloak heavy with water, white beard dripping, mud splashed to the thighs. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_008_hills_rain_ep4: The muddy road at the head of the marching Sui square in rain: churned mud, wet green hills, the front rank of red shields and spears behind, low grey cloud. Action: The Xianbei commander gallops in from the north, mud to his horse's chest, dismounts and kneels straight-backed in the mud before the general's tall warhorse; right forearm bandaged, the night-vision device hanging on his chest; the general reins in and looks down. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the gallop in, the dismount, the kneel in the mud, the general looking down; no dialogue. Sound: the horse pulling up, mud, rain.
ACTION_START: commander galloping in
ACTION_END: commander kneeling, general looking down
NARRATION_KO: 탁발흠은 얼굴을 잃었습니다. 미끼를 잃었고, 부하들을 갈대에 묻었고, 우리를 비웠습니다. 그가 가진 것은 하나였습니다. 자리였습니다.
DIALOGUE_KO: 
SOUND: ngựa dừng, bùn, mưa.
CONTINUITY: retreat_ep4 (mũ lông, kính trên ngực, băng tay phải). 2 ngựa: VEH_206 + VEH_207.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, CHAR_202_ref, VEH_206_ref, VEH_207_ref, EQP_001_ref, LOC_008_hills_rain_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)
AI_RISK: 2 ngựa + 2 người → low angle, tĩnh

### SC_263 | 36:18–36:26 | LOC_008 (LOC_008_square_head) | CHAR_205 | EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the kneeling commander, static
IMAGE_PROMPT: Close-up on the kneeling commander, static. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_008_hills_rain_ep4: The muddy road at the head of the marching Sui square in rain: churned mud, wet green hills, the front rank of red shields and spears behind, low grey cloud. Action: The commander lifts his face — rain running down the long scar — and lays his hand on the night-vision device on his chest as on an oath; he speaks short and formal. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the face lifted, rain on the scar, the hand on the device, one formal line. Sound: rain, one line of Korean dialogue.
ACTION_START: face down
ACTION_END: face up, hand on the device, line spoken
NARRATION_KO: 그는 위치를 팔았습니다. 그것이 그가 가진 유일한 값이었습니다. 우중문은 그 값을 알았습니다.
DIALOGUE_KO: 탁발흠: 천둥은 여울 북쪽에 있습니다. 제가 가져오겠습니다.
SOUND: mưa.
CONTINUITY: '천둥은 여울 북쪽에 있습니다. 제가 가져오겠습니다.'
CHAIN_FROM: SC_262
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, EQP_001_ref, LOC_008_hills_rain_ep4

### SC_264 | 36:26–36:34 | LOC_008 (LOC_008_square_head) | CHAR_202 | VEH_207 | PROPS: — | TYPE: video8s | 8s
SHOT: Low angle close-up on the mounted general, static
IMAGE_PROMPT: Low angle close-up on the mounted general, static. @CHAR_202_ref: Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Armor and breast mirrors streaming with rain, red cloak heavy with water, white beard dripping, mud splashed to the thighs. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. Setting @LOC_008_hills_rain_ep4: The muddy road at the head of the marching Sui square in rain: churned mud, wet green hills, the front rank of red shields and spears behind, low grey cloud. Action: The general looks down a long time — at the kneeling man, at the strange device on his chest, at the muddy road north; then speaks without raising his voice. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static low angle: the long look, the eyes moving north, one quiet line. Sound: rain, the horse breathing, one line of Korean dialogue.
ACTION_START: looking down
ACTION_END: line spoken
NARRATION_KO: 우중문에게 뇌군은 뒤에서 울린 천둥이었습니다. 그것을 가져오면 평양의 실패를 덮을 수 있었습니다. 황제 앞에서.
DIALOGUE_KO: 우중문: 천둥을 가져오면 네 죄를 잊겠다.
SOUND: mưa, ngựa thở.
CONTINUITY: '천둥을 가져오면 네 죄를 잊겠다.'
CHAIN_FROM: SC_263
CUT_HALF: no
REFS: CHAR_202_ref, VEH_207_ref, LOC_008_hills_rain_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)

### SC_265 | 36:34–36:42 | LOC_008 (LOC_008_square_head) | CHAR_203, SUI_OFFICER_MOUNTED | VEH_207 | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot, static
IMAGE_PROMPT: Medium shot, static. @CHAR_203_ref: Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes. a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, on a tall warhorse with a high wooden saddle and red saddle cloth. @VEH_207_ref: Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants. Setting @LOC_008_hills_rain_ep4: The muddy road at the head of the marching Sui square in rain: churned mud, wet green hills, the front rank of red shields and spears behind, low grey cloud. Action: The deputy turns in the saddle to the officer beside him and gives a dry order, tapping his bamboo slips on the saddle; the officer gallops off along the side of the square. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static: the turn in the saddle, the slips tapping the saddle, one dry line, the officer galloping off. Sound: bamboo on leather, hooves, rain, one line of Korean dialogue.
ACTION_START: deputy turning to the officer
ACTION_END: officer galloping away
NARRATION_KO: 우문술은 뒤를 보지 않았습니다. 그의 눈은 살수에 있었습니다. 이틀. 그 이틀 안에 비는 그치지 않을 것이었습니다.
DIALOGUE_KO: 우문술: 방진을 좁히시오. 살수까지 이틀이오.
SOUND: thẻ tre gõ yên, ngựa phi.
CONTINUITY: '방진을 좁히시오. 살수까지 이틀이오.'
CHAIN_FROM: SC_264
CUT_HALF: no
REFS: CHAR_203_ref, WPN_201_ref, VEH_207_ref, LOC_008_hills_rain_ep4
LOCK_PENDING: VEH_207 (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)

### SC_266 | 36:42–36:50 | LOC_008 (LOC_008_square_head) | CHAR_205, XIANBEI_RIDER, SUI_SOLDIERS_STARVING | VEH_206, EQP_001 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot with the riders
IMAGE_PROMPT: Tracking shot with the riders. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_008_hills_rain_ep4: The muddy road at the head of the marching Sui square in rain: churned mud, wet green hills, the front rank of red shields and spears behind, low grey cloud. Action: The commander swings up onto his horse and leads his Xianbei riders galloping ahead of the square northward; they pass a Sui soldier sitting at the roadside chewing grass; the commander does not look. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking with the riders past the square's front and the grass-chewing soldier. Sound: hooves, rain, chewing.
ACTION_START: commander mounting
ACTION_END: riders past the soldier, heading north
NARRATION_KO: 그에게는 이제 명령과 이유가 있었습니다. 명령은 우중문의 것이었고, 이유는 그의 것이었습니다. 둘 다 여울 북쪽을 가리켰습니다.
DIALOGUE_KO: 
SOUND: vó ngựa, mưa, nhai cỏ.
CONTINUITY: Không thoại.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, WPN_201_ref, VEH_206_ref, EQP_001_ref, LOC_008_hills_rain_ep4

### SC_267 | 36:50–37:02 | LOC_008 (LOC_008_hills_rain) | CHAR_205 | EQP_001, VEH_206 | PROPS: — | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: medium close-up on the rider, slow push-in to the device on his chest
IMAGE_PROMPT: Still for ken-burns: medium close-up on the rider, slow push-in to the device on his chest. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. Setting @LOC_008_hills_rain_ep4: Low green hills north of the Goguryeo capital in July monsoon rain, 612 AD: wet grass and scrub on rolling slopes, a muddy dirt road winding through the valley below churned by countless feet and hooves, low grey cloud on the ridges, mist in the folds, no buildings. Action: The commander rides north in the rain, the night-vision device on his chest beaded with water, right forearm bandaged, braid wet; behind him the far side of the great square. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the device on his chest. Sound: rain, hooves.
ACTION_START: rider with the square behind
ACTION_END: tight on the device
NARRATION_KO: 그는 야시경의 건전지를 셀 줄 몰랐습니다. 그 눈이 며칠이나 더 밤을 볼지 그는 몰랐습니다. 갈대밭의 박기철은 자기 것을 알았습니다. 이십. 그 둘도 같은 건전지였습니다.
DIALOGUE_KO: 
SOUND: mưa, vó ngựa.
CONTINUITY: Still 12 s.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, EQP_001_ref, VEH_206_ref, LOC_008_hills_rain_ep4

### SC_268 | 37:02–37:10 | LOC_007 (LOC_007_island2_k2) | CHAR_001 | VEH_001 | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Close-up, static
IMAGE_PROMPT: Close-up, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: Afternoon: the captain sits on the tank's muddy skirt, draws the folded pale yellow silk from his chest pocket and opens it — one column of brush calligraphy; he looks at it a long time though he cannot read it. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the silk drawn out, unfolded, the long look. Sound: silk, light rain.
ACTION_START: silk coming out of the pocket
ACTION_END: silk open, eyes on it
NARRATION_KO: 왕의 글은 닷새째 그의 가슴에 있었습니다. 누구의 군대인가. 그는 이 강가에 두 사람을 묻었습니다. 그들은 누구의 군대로 묻혔는지 그도 몰랐습니다.
DIALOGUE_KO: 
SOUND: lụa, mưa nhỏ.
CONTINUITY: Chiều D8.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, VEH_001_ref, PROP_013_ref, LOC_007_island_ep4
AI_RISK: chữ → brush calligraphy

### SC_269 | 37:10–37:18 | LOC_007 (LOC_007_island2_k2) | CHAR_001, CHAR_005 | EQP_002, VEH_001 | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: Wide two-shot, static, the two five meters apart
IMAGE_PROMPT: Wide two-shot, static, the two five meters apart. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_005_goguryeo_helmet_ep5: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The captain folds the silk and buttons the pocket; lifts his head to the boy in the Goguryeo iron helmet sitting by the radio five meters away, the handset on his thigh; the two look at each other and say nothing. Light: Flat grey afternoon light in steady rain, low cloud, wet grey-green tones. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide two-shot: silk folded away, the look across five meters, held; no dialogue. Sound: silk, faint radio static, rain.
ACTION_START: captain folding the silk
ACTION_END: two men looking at each other
NARRATION_KO: 답은 아직 쓰지 않았습니다. 그러나 답의 반은 저기 앉아 있었습니다. 고구려의 쇠를 쓰고, 천사백 년 뒤의 돌을 무릎에 놓고.
DIALOGUE_KO: 
SOUND: lụa, radio nhiễu nhỏ, mưa.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_268
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_005_goguryeo_helmet_ep5, EQP_002_ref, VEH_001_ref, PROP_013_ref, LOC_007_island_ep4

### SC_270 | 37:18–37:30 | LOC_007 (LOC_007_stake) | — | VEH_001 | PROPS: — | TYPE: still_kenburns | 12s
SHOT: Still for ken-burns: wide at grey dusk, slow pull-out
IMAGE_PROMPT: Still for ken-burns: wide at grey dusk, slow pull-out. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: Grey dusk on the north bank: the notched stake leans in water risen almost to its top notch, the reeds half drowned, and far off the dim mud mound of the tank; no people. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out from the stake to the drowned reed bank. Sound: river, rain, silence.
ACTION_START: tight on the stake, water at the top notch
ACTION_END: wide on the bank and the far mound
NARRATION_KO: 탁발흠은 이제 뇌군이 어디 있는지 정확히 알았습니다. 여울 북쪽.
DIALOGUE_KO: 
SOUND: sông, mưa, im.
CONTINUITY: Still 12 s. Kết P11. Nước gần ngập vạch trên cùng.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, LOC_007_detail
AI_RISK: xe xa → 'dim mud mound', không chi tiết


## [Phần 12] 물은 오르고, 포탄은 여섯 발 (37:30–40:00) · 방진 về bắc · cọc nước · 잔탄 06 · 오태민 một mình · end card

### SC_271 | 37:30–37:40 | LOC_008 (LOC_008_square) | GOG_CAVALRYMEN | WPN_201, VEH_101 | PROPS: PROP_021 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: very high aerial in rain, slow pull-out to the northern horizon  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: very high aerial in rain, slow pull-out to the northern horizon. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_021_ref: Sui army banner: tall red silk rectangle with a yellow border and black tassels on a black lacquered pole with bronze finial; imperial banner: yellow silk with an embroidered coiled dragon and red tassels. Setting @LOC_008_hills_rain_ep4: A muddy road through low green hills in monsoon rain: an enormous square formation of Sui infantry crawling north along it, four sides of red rectangular shields and long spears, ox carts in the center, wet red and yellow banners, mud churned to soup, low grey cloud. Action: From very high above in rain: a huge dark square — tens of thousands of men — crawls north over green hills on a muddy road, its corners bent; around it smaller streaks of cavalry cling to all four sides like dogs around an ox. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow pull-out to the northern horizon. Sound: slow Sui drums very far, rain, high wind.
ACTION_START: tight on the square
ACTION_END: wide to the northern hills
NARRATION_KO: 삼십만이 돌아섰습니다. 평양에서 삼십 리, 손가락 한 마디 앞에서. 왔던 길이 돌아가는 길이 되었습니다. 그 길 끝에 강이 있었습니다.
DIALOGUE_KO: 
SOUND: trống Tùy chậm rất xa, mưa, gió trên cao.
CONTINUITY: Still 10 s.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, VEH_101_ref, PROP_021_ref, LOC_008_hills_rain_ep4

### SC_272 | 37:40–37:48 | LOC_008 (LOC_008_square) | GOG_CAVALRYMEN, SUI_SOLDIERS_STARVING | VEH_101, WPN_101, WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static, rain  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Wide, static, rain. Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @WPN_101_ref: Goguryeo short composite reflex bow of horn, wood and sinew wrapped in dark cherry bark, arrows with iron willow-leaf and barbed triangular heads and grey three-vane fletching, a wooden crossbow with a bronze trigger on the wall. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_008_hills_rain_ep4: A muddy road through low green hills in monsoon rain: an enormous square formation of Sui infantry crawling north along it, four sides of red rectangular shields and long spears, ox carts in the center, wet red and yellow banners, mud churned to soup, low grey cloud. Action: Goguryeo cavalry sweep down and loose a volley into a side of the square, wheeling away before the Sui crossbows come up; a few red shields fall, the side closes again; over and over. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: the sweep, the volley, the wheel away, the crossbows late, shields falling, the side closing. Sound: bowstrings, late crossbow strings, shouts, rain.
ACTION_START: cavalry sweeping in
ACTION_END: cavalry gone, side closed
NARRATION_KO: 을지문덕은 사방에서 쳤습니다. 삼국사기는 이렇게 적었습니다. 싸우면서 갔다고. 그 문장 안에 며칠이 들어 있었습니다.
DIALOGUE_KO: 
SOUND: dây cung, nỏ Tùy muộn, hô, mưa.
CONTINUITY: [史] Wide.
CHAIN_FROM: —
CUT_HALF: yes
REFS: VEH_101_ref, WPN_101_ref, WPN_201_ref, LOC_008_hills_rain_ep4
AI_RISK: kỵ số đông → wide

### SC_273 | 37:48–37:56 | LOC_008 (LOC_008_square_inside) | SUI_SOLDIERS_STARVING, OXEN_CARTS | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: Tracking shot against the direction of march
IMAGE_PROMPT: Tracking shot against the direction of march. gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away. two-wheeled wooden ox carts loaded with rope-bound chests, oxen under wooden yokes. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_008_hills_rain_ep4: Inside the marching square of Sui infantry on a muddy road in rain: walls of soldiers with red rectangular shields and spears on every side, ox carts creaking through mud in the center, exhausted men, wet banners, low grey sky. Action: Inside the square: soldiers drag their spears, an ox cart with a broken axle left in the middle of the road, the men behind flowing around it; rain pouring. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Tracking against the flow: dragging spears, the broken cart passed on both sides. Sound: dragging feet, a broken wheel, rain.
ACTION_START: soldiers approaching
ACTION_END: broken cart passed
NARRATION_KO: 진 안에는 밥이 없었습니다. 수레는 비어 있었습니다. 그래도 진은 움직였습니다. 움직이는 것 말고는 할 수 있는 것이 없었습니다.
DIALOGUE_KO: 
SOUND: chân lê, bánh xe gãy, mưa.
CONTINUITY: Mặt lính quay đi.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, LOC_008_hills_rain_ep4
AI_RISK: đám đông → tracking, mặt khuất

### SC_274 | 37:56–38:06 | LOC_008 (LOC_008_knoll) | CHAR_101, GOG_FLAGBEARER | VEH_101 | PROPS: PROP_012 | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium shot on the knoll, slow push-in to the general's face
IMAGE_PROMPT: Still for ken-burns: medium shot on the knoll, slow push-in to the general's face. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. a mounted Goguryeo flag bearer in iron lamellar armor carrying a tall wet yellow silk banner with a black three-legged crow. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_008_hills_rain_ep4: The top of a green knoll in monsoon rain: wet grass, low grey cloud, and far below in the valley a dark square of tens of thousands of soldiers crawling north along a muddy road. Action: The silver-bearded general alone on his armored horse on the top of a knoll in rain, plume drooping; behind him only a flag bearer with the wet crow banner; far below, the dark square crawls north. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the general's face; no dialogue. Sound: rain, wind, the wet banner slapping.
ACTION_START: general on the knoll, square below
ACTION_END: tight on the face
NARRATION_KO: 을지문덕은 말하지 않았습니다. 이틀 전에 그는 시를 보냈습니다. 시는 답을 받았습니다. 삼십만이 돌아서는 것으로.
DIALOGUE_KO: 
SOUND: mưa, gió, cờ ướt đập.
CONTINUITY: Still 10 s. 해모루 KHÔNG ở gò (QC: anh ở 살수 D8).
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_salsu_rain_ep5, VEH_101_ref, PROP_012_ref, LOC_008_hills_rain_ep4

### SC_275 | 38:06–38:14 | LOC_008 (LOC_008_knoll) | CHAR_101, GOG_FLAGBEARER | VEH_101 | PROPS: PROP_012 | TYPE: video8s | 8s
SHOT: Close-up on the eyes, then the camera follows the horse turning
IMAGE_PROMPT: Close-up on the eyes, then the camera follows the horse turning. @CHAR_101_salsu_rain_ep5: Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard. a mounted Goguryeo flag bearer in iron lamellar armor carrying a tall wet yellow silk banner with a black three-legged crow. @VEH_101_ref: Goguryeo cataphract: horse fully armored in dull iron lamellar barding from neck to rump with an iron face mask, rider in full iron lamellar armor with arm and shin guards, iron helmet with a red plume, four-meter lance, sword at the waist, black three-legged crow pennant on a yellow field. @PROP_012_ref: Goguryeo banner: tall rectangular earthy yellow silk flag with a black three-legged crow inside a black sun circle, black tassel fringe, on a long bamboo pole topped with a tuft of feathers. Setting @LOC_008_hills_rain_ep4: The top of a green knoll in monsoon rain: wet grass, low grey cloud, and far below in the valley a dark square of tens of thousands of soldiers crawling north along a muddy road. Action: Close on the general's eyes watching the square; the smallest nod; he pulls the reins and turns his horse north — toward the river; the flag bearer follows. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Close-up on the eyes, the small nod, the horse turned north, camera following the turn; one word. Sound: reins, the horse, rain, one word of Korean dialogue.
ACTION_START: eyes on the square
ACTION_END: horse turned north
NARRATION_KO: 역사는 이 강을 살수라 부릅니다. 그때 그 강은 그저 물이 오르는 강이었습니다.
DIALOGUE_KO: 을지문덕: 살수로.
SOUND: cương, ngựa, mưa.
CONTINUITY: '살수로.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_101_salsu_rain_ep5, VEH_101_ref, PROP_012_ref, LOC_008_hills_rain_ep4

### SC_276 | 38:14–38:24 | LOC_007 (LOC_007_aerial) | — | — | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: aerial in rain, slow slide along the line of stakes  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: aerial in rain, slow slide along the line of stakes. Setting @LOC_007_wide: Wide shallow Cheongcheon River eight hundred meters across in July monsoon rain: long wet grey-brown sandbars, a line of wooden ford-marker stakes crossing the shallows, the north bank buried in dense two-meter grey-green reed beds stretching hundreds of meters, the south bank rising into low green hills, brown water, river mist, heavy grey cloud, no trees on the sandbars. Action: From above in rain: the river swollen and brown, the mid-river sandbar shrunk to a single strip, the line of wooden ford stakes drowned to their tops, the north-bank reeds half submerged. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow slide along the drowned line of stakes. Sound: rain on the river, water running harder.
ACTION_START: stakes at one end
ACTION_END: stakes at the other end, reeds half drowned
NARRATION_KO: 살수. 이레 전에는 무릎이었습니다. 지금은 허리였습니다. 물은 매일 올랐습니다. 어떤 날은 한 뼘, 어떤 날은 반 뼘. 비는 매일 왔습니다.
DIALOGUE_KO: 
SOUND: mưa trên sông, nước chảy mạnh hơn.
CONTINUITY: Still 10 s. Nước từ gối → thắt lưng.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_007_wide

### SC_277 | 38:24–38:32 | LOC_007 (LOC_007_stake) | CHAR_003 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Medium shot at water level, static
IMAGE_PROMPT: Medium shot at water level, static. @CHAR_003_rain_ep3: 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The sergeant wades waist-deep out to the stake — the water past yesterday's notch; he draws his knife and cuts a new notch at the waterline, eyes the gap to the old one, and measures it with his spread hand. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static at water level: the knife cutting the notch, the gap measured with a spread hand, one line. Sound: knife scraping wood, water, rain, one line of Korean dialogue.
ACTION_START: wading to the stake
ACTION_END: hand spread against the stake, line spoken
NARRATION_KO: 한 뼘. 어제도 한 뼘이었습니다. 박기철은 두 눈금 사이를 손으로 쟀습니다. 손은 자보다 정확하지 않았지만 매일 같았습니다.
DIALOGUE_KO: 박기철: 어제보다 한 뼘.
SOUND: dao cạo gỗ, nước, mưa.
CONTINUITY: '어제보다 한 뼘.'
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_003_rain_ep3, LOC_007_detail

### SC_278 | 38:32–38:40 | LOC_007 (LOC_007_stake) | CHAR_106 | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the bank, static
IMAGE_PROMPT: Close-up on the bank, static. @CHAR_106_ref: 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold. Setting @LOC_007_detail: The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud. Action: The old blacksmith squats on the bank behind the sergeant, one hand thrust into the water, left eye squinting upstream at black cloud pressing on the hills; says nothing; pulls the hand out and shakes it. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: the hand in the water, the squint upstream, the hand pulled out and shaken; no dialogue. Sound: water over the hand, distant thunder.
ACTION_START: hand in the water
ACTION_END: hand shaken dry
NARRATION_KO: 을보는 말하지 않았습니다. 사흘이라는 말은 이미 했습니다. 두 번 말하는 것은 대장장이의 법이 아니었습니다.
DIALOGUE_KO: 
SOUND: nước qua tay, sấm xa.
CONTINUITY: Không thoại. 박기철 ở nền (không thêm lock — chỉ lưng xa).
CHAIN_FROM: SC_277
CUT_HALF: no
REFS: CHAR_106_ref, LOC_007_detail

### SC_279 | 38:40–38:50 | LOC_007 (LOC_007_island2_k2) | — | VEH_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium shot on the mud mound, slow push-in to the glowing crack of the hatch
IMAGE_PROMPT: Still for ken-burns: medium shot on the mud mound, slow push-in to the glowing crack of the hatch. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The tank's mud mound under the reeds in rain — only the reed-wrapped barrel and a corner of the side skirt recognisable; through the half-open hatch a cold blue screen glow with a small blank readout. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the blue glow in the hatch. Sound: rain on mud, a faint electronic fan.
ACTION_START: mud mound
ACTION_END: tight on the blue glow
NARRATION_KO: 여섯. 전차는 그 숫자를 매일 밤 켜 두었습니다. 요동성에서 스물둘이었습니다. 살수에서 여섯이었습니다. 다음은 없었습니다.
DIALOGUE_KO: 
SOUND: mưa trên bùn, quạt điện tử rất nhỏ.
CONTINUITY: Still 10 s. [OVERLAY] '잔탄 06' trong khe sáng.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, LOC_007_island_ep4
OVERLAY (edit): 잔탄 06 (màn hình trưởng xe qua cửa tháp hé)
AI_RISK: chữ → blank readout, OVERLAY

### SC_280 | 38:50–38:58 | LOC_007 (LOC_007_north_ford) | CHAR_002 | WPN_003 | PROPS: — | TYPE: video8s | 8s
SHOT: Wide, static, the figure small between water and reeds
IMAGE_PROMPT: Wide, static, the figure small between water and reeds. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The lieutenant stands alone at the edge of the north shore in the rain, helmet off, the light machine gun slung across his back, goggles on his forehead beaded with water, looking across the rising river at the south bank; motionless. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static wide: rain, the river rising, the small figure does not move. Sound: rain, the river.
ACTION_START: figure standing
ACTION_END: figure standing
NARRATION_KO: 오태민은 북쪽 여울에 서 있었습니다. 한승우가 준 자리였습니다. 그는 그 자리가 무엇을 위한 자리인지 이제 알았습니다.
DIALOGUE_KO: 
SOUND: mưa, sông.
CONTINUITY: Không thoại. Kính bảo hộ trên trán.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_002_reeds_ep4, WPN_003_ref, LOC_007_detail

### SC_281 | 38:58–39:06 | LOC_007 (LOC_007_north_ford) | CHAR_001, CHAR_002 | WPN_003 | PROPS: PROP_013 | TYPE: video8s | 8s
SHOT: From behind the captain, both men in frame, static
IMAGE_PROMPT: From behind the captain, both men in frame, static. @CHAR_001_reeds_ep4: 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. @CHAR_002_reeds_ep4: 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. @WPN_003_ref: South Korean K3 5.56mm light machine gun, black, long barrel with carrying handle, folding bipod, green 200-round plastic belt box under the receiver, fixed stock. @PROP_013_ref: royal edict on pale yellow silk rolled on a black lacquered wooden rod with bronze end caps, columns of black brush calligraphy, a large square red seal impression at the end, carried in a black lacquered bamboo tube with red silk cord. Setting @LOC_007_detail: The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist. Action: The captain stands thirty meters behind the lieutenant at the edge of the reeds and does not go closer; his hand touches the chest pocket with the silk and the arrow; he looks at the lieutenant's back, then at the river. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static from behind the captain: the hand on the pocket, the look at the other man's back, the look at the river; no dialogue. Sound: rain, reeds.
ACTION_START: captain behind, lieutenant far ahead
ACTION_END: captain's eyes on the river
NARRATION_KO: 두 사람은 같은 강을 보았습니다. 서로 다른 것을 보았습니다. 한 사람은 태오를, 한 사람은 왕의 물음을. 강은 둘 다 상관하지 않았습니다.
DIALOGUE_KO: 
SOUND: mưa, lau.
CONTINUITY: Không thoại.
CHAIN_FROM: SC_280
CUT_HALF: no
REFS: CHAR_001_reeds_ep4, CHAR_002_reeds_ep4, WPN_003_ref, PROP_013_ref, LOC_007_detail

### SC_282 | 39:06–39:16 | LOC_007 (LOC_007_island2_k2) | CHAR_005, CHAR_107 | EQP_002, VEH_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium two-shot, slow push-in to the iron helmet
IMAGE_PROMPT: Still for ken-burns: medium two-shot, slow push-in to the iron helmet. @CHAR_005_goguryeo_helmet_ep5: 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief. @CHAR_107_scarf_ep2: 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. @EQP_002_ref: PRC-999K military VHF backpack radio, dark olive metal box with rotary knobs and a small LCD panel, long black whip antenna, coiled-cord handset, backpack frame. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_island_ep4: Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain. Action: The boy in the Goguryeo iron helmet, hemp jacket over his camouflage, leg splinted, holds the radio handset level with his mouth; the girl sits beside him in the olive scarf, her head resting against the tank's mud-caked track. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the iron helmet. Sound: faint radio static, rain.
ACTION_START: two by the track
ACTION_END: tight on the iron helmet
NARRATION_KO: 태오는 무전을 맡았습니다. 걸을 수 없는 사람이 할 수 있는 일이었습니다. 하늘의 눈은 잃었지만 귀는 남았습니다. 그 돌로 고구려 말객이 나각을 알렸습니다. 이제 그 돌은 태오의 무릎에 있었습니다.
DIALOGUE_KO: 
SOUND: radio nhiễu nhỏ, mưa.
CONTINUITY: Still 10 s.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_005_goguryeo_helmet_ep5, CHAR_107_scarf_ep2, EQP_002_ref, VEH_001_ref, LOC_007_island_ep4

### SC_283 | 39:16–39:24 | LOC_008 (LOC_008_aerial_north) | — | WPN_201 | PROPS: — | TYPE: video8s | 8s
SHOT: High aerial, slow drift from the square to the silver band  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: High aerial, slow drift from the square to the silver band. @WPN_201_ref: Sui dynasty infantry in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, straight swords, archers in grey-blue padded coats, red and yellow banners. Setting @LOC_008_hills_rain_ep4: From high above in rain: low green hills rolling north under grey cloud, a muddy road, and beyond the last hills a silver band of a wide river, mist. Action: From high above: the head of the great square reaches a range of low hills to the north; beyond the hills, through rain mist, a silver band — the river. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Slow aerial drift from the head of the square forward over the hills to the silver band of the river. Sound: wind, rain, drums very far.
ACTION_START: head of the square at the hills
ACTION_END: silver band of the river ahead
NARRATION_KO: 며칠. 우문술은 그렇게 말했습니다. 비가 며칠 더 오면 여울은 여울이 아닐 것이었습니다.
DIALOGUE_KO: 
SOUND: gió, mưa, trống rất xa.
CONTINUITY: Aerial video.
CHAIN_FROM: —
CUT_HALF: no
REFS: WPN_201_ref, LOC_008_hills_rain_ep4

### SC_284 | 39:24–39:34 | LOC_008 (LOC_008_hills_rain) | CHAR_205, XIANBEI_RIDER | VEH_206, EQP_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: medium close-up on the rider, slow push-in to the eyes
IMAGE_PROMPT: Still for ken-burns: medium close-up on the rider, slow push-in to the eyes. @CHAR_205_nvg_ep3: 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs. a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber. @VEH_206_ref: Xianbei steppe light cavalry: short stocky steppe horses with thick manes and no armor, riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, soft boots, composite bows and hip quivers, short curved sabers, coiled lassos, black horse-tail standards on poles. @EQP_001_ref: PVS-11K monocular night vision device, short black cylindrical tube with a round objective lens and rubber eyecup, flip-up metal helmet mount, small battery pack. Setting @LOC_008_hills_rain_ep4: Low green hills north of the Goguryeo capital in July monsoon rain, 612 AD: wet grass and scrub on rolling slopes, a muddy dirt road winding through the valley below churned by countless feet and hooves, low grey cloud on the ridges, mist in the folds, no buildings. Action: The commander rides at the head of his Xianbei riders northward in rain, the night-vision device on his chest, eyes fixed ahead; behind him a file of riders in wet fur caps. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: slow push-in to the eyes. Sound: hooves, rain.
ACTION_START: rider with the file behind
ACTION_END: tight on the eyes
NARRATION_KO: 앞에는 탁발흠이 있었습니다. 그는 여울 북쪽을 알았습니다. 여울 북쪽은 아직 그를 몰랐습니다. 며칠 뒤면 알게 될 것이었습니다.
DIALOGUE_KO: 
SOUND: vó ngựa, mưa.
CONTINUITY: Still 10 s.
CHAIN_FROM: —
CUT_HALF: no
REFS: CHAR_205_nvg_ep3, VEH_206_ref, EQP_001_ref, LOC_008_hills_rain_ep4

### SC_285 | 39:34–39:42 | LOC_007 (LOC_007_river_surface) | — | — | PROPS: — | TYPE: video8s | 8s
SHOT: Close-up on the water surface, static
IMAGE_PROMPT: Close-up on the water surface, static. Setting @LOC_007_detail: Close on the surface of the shallow river in heavy monsoon rain: brown water pocked by dense raindrops, a wooden stake almost submerged, tall reeds leaning with the current, no far bank. Action: Heavy rain hammering brown water, a wooden stake almost submerged, reeds leaning with the current; no people. Light: Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Static close-up: rain pocking the water, the current pulling at the reeds, the stake's top barely showing; nothing else. Sound: dense rain, fast water.
ACTION_START: stake top above the water
ACTION_END: stake top barely above the water
NARRATION_KO: 물은 매일 올랐습니다. 아무도 그것을 막지 않았습니다. 막을 필요가 없었습니다.
DIALOGUE_KO: 
SOUND: mưa dồn, nước chảy xiết.
CONTINUITY: Không người.
CHAIN_FROM: —
CUT_HALF: no
REFS: LOC_007_detail

### SC_286 | 39:42–39:52 | LOC_007 (LOC_007_aerial) | — | VEH_001 | PROPS: — | TYPE: still_kenburns | 10s
SHOT: Still for ken-burns: aerial at rainy dusk, very slow pull-out  · ⚑ AERIAL/QUALITY
IMAGE_PROMPT: Still for ken-burns: aerial at rainy dusk, very slow pull-out. @VEH_001_ref: South Korean K2 Black Panther main battle tank, low angular wedge-shaped turret, long 120mm gun with bore evacuator, six twin road wheels per side under thick side skirts, six smoke launchers each side, three-tone green-brown-black camouflage, small white numeral 1 and a small Korean flag on the turret side, black whip antennas. Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible. Setting @LOC_007_wide: Wide shallow Cheongcheon River eight hundred meters across in July monsoon rain: long wet grey-brown sandbars, a line of wooden ford-marker stakes crossing the shallows, the north bank buried in dense two-meter grey-green reed beds stretching hundreds of meters, the south bank rising into low green hills, brown water, river mist, heavy grey cloud, no trees on the sandbars. Action: From above at dusk in rain: the north bank — reeds half drowned, the dim mud mound of the tank, tiny figures of people among the reeds, the wooden stake in the water; to the south, dark hills; the river a sheet of grey silver in ripples. Light: Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps. photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look
VIDEO_PROMPT: Ken-burns: very slow pull-out. Sound: rain, river, wind.
ACTION_START: tight on the reed bank and the mound
ACTION_END: wide on river and dark hills
NARRATION_KO: 30만이 살수로 돌아오고 있었습니다. 물은 오르고, 포탄은 여섯 발이었습니다.
DIALOGUE_KO: 
SOUND: mưa, sông, gió.
CONTINUITY: Still 10 s.
CHAIN_FROM: —
CUT_HALF: no
REFS: VEH_001_ref, LOC_007_wide
AI_RISK: xe xa → 'dim mud mound'

### SC_287 | 39:52–40:00 | LOC_007 (LOC_007_aerial) | — | — | PROPS: — | TYPE: still_kenburns | 8s
SHOT: END CARD — black frame, white title text centered (added in edit)
IMAGE_PROMPT: — (EDIT ONLY: end card đen + chữ ở khâu edit, không tạo ảnh AI)
VIDEO_PROMPT: EDIT ONLY: black frame 8 s, white centered title 「살수 612 · 5화 살수 (最終話)」 added in edit; rain continues 3 s into the black, then absolute silence.
ACTION_START: black
ACTION_END: black
NARRATION_KO: 
DIALOGUE_KO: 
SOUND: mưa còn 3 s trong đen, rồi im tuyệt đối.
CONTINUITY: Không tạo ảnh AI. Chữ ở edit.
CHAIN_FROM: —
CUT_HALF: no
REFS: —
OVERLAY (edit): 살수 612 · 5화 살수 (最終話) — end card trắng trên đen
AI_RISK: chữ → không tạo ảnh; end card ở edit
