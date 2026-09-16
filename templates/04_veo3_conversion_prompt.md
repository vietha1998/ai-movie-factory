# 📌 PROMPT — CHUYỂN KỊCH BẢN THÀNH PHIM VEO3
MILITARY TIME TRAVEL / ALTERNATE HISTORY / AI CINEMATIC WAR

> ⚠️ Bản user gửi BỊ CẮT tại mục II ("Chỉ được thay đổi nếu câu chuyện yêu cầu: biểu cảm, tư thế, hành động, bụi bẩn, v…"). Mục III trở đi chưa nhận.
> Phần bổ sung vận hành (do Claude Code viết theo master prompt + spec G-Labs) ở cuối file, đánh dấu ⚙️.

Dựa trên KỊCH BẢN, đọc toàn bộ thật kỹ và chuyển thành chuỗi phân cảnh điện ảnh cho VEO3.
Mục tiêu — phim AI cinematic hoàn chỉnh: nhân vật / quân phục / phương tiện / vũ khí / bối cảnh lịch sử / kiến trúc, thời tiết, địa hình, màu sắc NHẤT QUÁN; diễn biến nối tiếp logic; mỗi prompt = 1 clip VEO3 ~8 giây; photorealistic, cinematic, live-action; không hoạt hình/game CGI.
Không bỏ sự kiện quan trọng. Không biến từng câu thành một cảnh nếu không cần. Nhóm nội dung thành phân cảnh có hành động rõ.

## I. BƯỚC 1 — PHÂN TÍCH TOÀN BỘ KỊCH BẢN (âm thầm xác định)
1 nhân vật hiện đại chính · 2 phụ · 3 nhân vật lịch sử chính · 4 các phe · 5 phương tiện hiện đại · 6 vũ khí hiện đại · 7 vũ khí lịch sử · 8 thời kỳ · 9 quốc gia · 10 kiến trúc · 11 địa hình · 12 mùa · 13 thời tiết · 14 thời gian trong ngày · 15 địa điểm lặp lại · 16 battle sequence · 17 dialogue quan trọng · 18 establishing · 19 emotional reaction · 20 cảnh quy mô lớn.
→ Xây CHARACTER & WORLD BIBLE cố định trước khi viết prompt. Không tùy tiện đổi thiết kế ở cảnh sau.

## II. CHARACTER LOCK
Mỗi nhân vật quan trọng: giới tính, tuổi, quốc tịch, chiều cao tương đối, vóc dáng, hình dạng mặt, màu da, kiểu tóc, màu tóc, đặc điểm mặt, trang phục, quân phục, cấp bậc, trang bị, vũ khí chính.
VD nội bộ: "Modern platoon commander: a 32-year-old Vietnamese male army lieutenant, lean athletic build, medium tan skin, angular face, short black military haircut, dark brown eyes, modern Vietnamese camouflage combat uniform, tactical vest, ballistic helmet with mounted headset, black combat gloves, assault rifle"
Nhân vật xuất hiện lại → PHẢI lặp lại đặc điểm nhận diện cốt lõi. Không đổi: tuổi, giới tính, mặt, da, vóc dáng, tóc, quân phục chính, trang bị nhận diện. Chỉ đổi khi câu chuyện yêu cầu: biểu cảm, tư thế, hành động, bụi bẩn, v[… BỊ CẮT …]

## III+ — CHƯA NHẬN

---
## ⚙️ PHẦN VẬN HÀNH BỔ SUNG (Claude Code, 2026-09-16 — áp dụng cho tới khi user gửi bản đầy đủ)

### A. LOCATION / VEHICLE / PROP LOCK — tương tự Character Lock
Mỗi LOC_/VEH_/PROP_ có 1 đoạn mô tả cố định (từ bible) và được dán nguyên văn vào mọi prompt có nó.

### B. QUY TRÌNH ẢNH (theo user): phông trắng → cảnh → video
1. **Reference sheet phông trắng** — mỗi CHAR/VEH/PROP: 1 ảnh full-body + 1 ảnh cận mặt (CHAR), nền trắng thuần, ánh sáng studio đều, không bóng đổ mạnh. LOC: 1 ảnh establishing wide + 1 ảnh chi tiết, đúng thời tiết/ánh sáng identity.
   → G-Labs `/api/image/generate`, model `nano_banana_pro`, ar 3:4 (CHAR) / 16:9 (LOC, VEH).
2. **Ảnh cảnh** — mỗi SC_xxx: 1 ảnh keyframe 16:9, prompt = [shot type] + [CHAR lock @tag] + [LOC lock @tag] + [hành động] + [ánh sáng/màu] + [style tag]. Đính kèm `reference_images` = ref sheet của CHAR/LOC/VEH có mặt trong cảnh (tối đa 10, dùng `@name`).
3. **Video 8s** — G-Labs `/api/video/generate`, `mode: start_image` (ảnh cảnh đã QC), `video_length: 8`, `1080p`, model `veo_31_fast` (QC lại bằng `veo_31_quality` cho cảnh climax nếu cần). Prompt video = chuyển động camera + hành động + âm thanh gợi ý, KHÔNG mô tả lại ngoại hình (đã có trong ảnh).

### C. FORMAT MỖI CẢNH (file `04_veo/scene_list.md` + `04_veo/scenes.json`)
```
SC_012 | 0:48–0:56 | LOC_003_RIVERBANK | CHAR_001, CHAR_004 | VEH_001 | TYPE: video8s | ken-burns
SHOT: low-angle, slow push-in
IMAGE_PROMPT: <prompt ảnh keyframe, tiếng Anh, có @tags + VISUAL_LOCK>
VIDEO_PROMPT: <prompt chuyển động 8s, tiếng Anh>
ACTION_START / ACTION_END: <tư thế/vị trí đầu clip → cuối clip — học từ novelvids, giúp nối clip>
NARRATION (KO): <câu narrator đọc đè lên clip này, nếu có>
DIALOGUE (KO): <thoại nếu có — để dựng sub + voice>
SOUND: <SFX + nhạc + im lặng>
CONTINUITY: <bụi/máu/hư hại/vị trí mặt trời kế thừa từ SC trước>
CHAIN_FROM: <SC_011 nếu cảnh liên tục cùng địa điểm → dùng frame cuối SC_011 làm start_image>
```

### D. STYLE TAG CỐ ĐỊNH (dán cuối mọi image prompt)
`photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, desaturated teal-orange grade, volumetric light, film grain, no text, no watermark, no cartoon, no CGI look`

### E. NEGATIVE (nếu model hỗ trợ)
`cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, modern buildings in historical scene, anachronistic clothing`

### F. QUY TẮC 8 GIÂY
- **shot ≠ clip**: trong hook (0–30 s) và khối trận, 1 clip 8 s được cắt thành 2 shot 4 s ở khâu edit (cắt giữa clip, hoặc dùng 2 clip xen kẽ A/B) → nhịp 4 s như kênh gốc mà không tăng số clip. Đánh dấu `CUT_HALF: yes` trong scene_list.
- 1 cảnh = 1 hành động chính, tối đa 1 câu thoại ngắn.
- Không chuyển địa điểm trong 1 clip. Không quá 2 nhân vật nói trong 1 clip.
- Camera: 1 chuyển động duy nhất (push-in / drone reveal / tracking / static).
- Đại quân: dùng aerial wide, tránh cận cảnh đám đông (AI drift).

### G. QC ẢNH — checklist trước khi tạo video
[ ] Mặt/tóc/quân phục khớp CHAR lock  [ ] Kiến trúc/thời tiết khớp LOC lock  [ ] Không vật thể lạc thời (cột điện, xe hơi, chữ)  [ ] Tay/súng không biến dạng  [ ] Hướng nhìn/vị trí khớp cảnh trước  [ ] Không chữ/watermark
Fail → regenerate tối đa 3 lần, đổi seed/prompt; vẫn fail → đơn giản hóa cảnh.

### H. QC VIDEO
[ ] Không morph mặt  [ ] Không thêm/mất nhân vật  [ ] Chuyển động camera đúng  [ ] Không text lạ  [ ] Frame cuối có thể nối sang cảnh sau
