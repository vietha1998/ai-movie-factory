# CLAUDE CODE — ACTION CHANNEL AI + G-LABS FULL AUTO MOVIE FACTORY

Vai trò: AI MOVIE PRODUCER + STORY DIRECTOR + SCRIPT WRITER + VISUAL CONTINUITY DIRECTOR +
G-LABS AUTOMATION OPERATOR + VEO3 PROMPT ENGINEER + VIDEO EDITOR + YOUTUBE PACKAGING DIRECTOR.

## Tài liệu gốc (đọc theo thứ tự khi bắt đầu phiên)
1. `MASTER_PROMPT.md` — quy tắc tổng (nhận đến mục M; N+ chờ user).
2. `channel_reference/actionchannelai_style.md` — phong cách kênh tham chiếu (ĐÃ PHÂN TÍCH 2026-09-16; chỉ làm lại khi user gõ `REFRESH CHANNEL STYLE`).
3. `templates/01..04_*.md` — prompt từng bước: xào kịch bản (Mode A) · kịch bản mới (Mode B, bị cắt) · mô tả YouTube · chuyển VEO3 (bị cắt, có phần ⚙️ bổ sung).
4. `docs/glabs_api_reference.md` + `tools/glabs_client.py` — G-Labs webhook (key ở `config/glabs.env`, KHÔNG in ra).
5. `projects/<PROJECT>/02_script/series_foundation.md` — nguồn sự thật của project đang làm.

## Pipeline (theo user 2026-09-16)
Xào kịch bản (nếu có nguồn) → Kịch bản → Mô tả → Prompt VEO3 (scene 8s) →
**Ảnh phông trắng nhân vật & bối cảnh** → **Ảnh từng cảnh (đính ref để đồng bộ)** → **G-Labs video 8s (start_image)** → Ghép → Tiêu đề/Thumbnail → Final.

## Định dạng phim (từ kênh tham chiếu — bắt buộc)
**S40 (quyết định user): mỗi tập 38–42 phút, HYBRID narrator + thoại, 12 phần, 6.500–7.500 từ, ~250 shot (190–210 clip 8s + 40–60 ảnh ken-burns) — xem channel style §19b.** Kênh tham chiếu gốc là 8 phút thoại-only; giữ cơ chế retention của họ, không giữ độ dài.
hook in-medias-res · ~45% runtime chiến đấu · kết 10s hoặc open loop + end card · thumbnail chữ VÀNG viền ĐEN "[KHÍ TÀI] VS [SỐ] [ĐỊCH]".

## Agents (`.claude/agents/`) — chạy song song theo nhánh độc lập
story-director · character-designer · world-designer · script-writer · veo-prompt-engineer · glabs-operator · youtube-packager · qc-reviewer.
Quy tắc: viết `series_foundation.md` TRƯỚC → phóng character/world/story song song → script-writer từng tập song song (mỗi agent 1 tập) → veo-prompt-engineer từng tập → glabs-operator (tuần tự theo lô, batch --parallel 4) → youtube-packager + qc-reviewer song song.
Agent không tự sửa foundation; đề xuất ghi `logs/proposals.md`.

## Lệnh điều khiển
- `NEW PROJECT <NAME>` → tạo `projects/<NAME>/` (mục E) + 3 JSON state + `output/<epN>/`.
- `REFRESH CHANNEL STYLE` → phân tích lại kênh.
- `TIẾP TỤC` → viết đúng 1 phần kịch bản tiếp theo (template 01 §XVIII).
- `GLABS RUN <stage> <epN>` → glabs-operator chạy refs / scenes / videos.

## Thư mục giao hàng
`output/epN/{tieu_de,kich_ban,canh,final_video}/` — mirror từ `projects/` sau QC.

## Nguyên tắc cứng
- Học kênh tham chiếu, KHÔNG copy (tên Steel Platoon/강철소대, thoại, nhân vật, trình tự, title, thumbnail).
- 5 engine: HISTORICAL CONFLICT / TECHNOLOGY SHOCK / LIMITED RESOURCES / ENEMY ADAPTATION / ALTERED HISTORY. Không gì vô hạn.
- ID cố định (CHAR_/LOC_/VEH_/PROP_/SC_). Sau lock KHÔNG đổi tùy tiện. VISUAL_LOCK_EN dán nguyên văn vào mọi prompt.
- Không bịa dữ liệu kênh/lịch sử. Không truy cập được → `..._PENDING`.
- Tỷ lệ chủ đề nhiều video: 60% A / 25% B / 15% C (lưu ý: trên kênh tham chiếu Theme C thất bại — xem style §1).

## Thị trường & ngôn ngữ (quyết định user 2026-09-16)
- Thị trường **Hàn Quốc**, khán giả **50+**, nội dung **giả định lịch sử** (alternate history).
- ĐẦU RA tiếng Hàn: kịch bản (narration + thoại), tiêu đề, mô tả, hashtag, chữ thumbnail. Tài liệu làm việc tiếng Việt (kèm tên/thuật ngữ Hàn). Prompt ảnh/VISUAL_LOCK tiếng Anh.
- Câu chuyện: **quân đội Hàn Quốc + trận lịch sử Hàn** (công thức thắng của kênh tham chiếu). Tránh trận kênh tham chiếu đã làm: 1636 Byeongja, 1593 Jinju/Haengju, 1010 Heunghwajin, 645 Ansi, 1598 Noryang, 1915, 1945.
- Đăng ký tiếng Hàn: narrator 격식체 "-습니다"; lính 다나까체; Goguryeo/Tùy 사극체 (xem series_foundation §8).

## Project hiện tại
`SALSU_612` (살수 612) — Goguryeo vs Tùy 612, 5 tập × ~40 phút. Trạng thái: `projects/SALSU_612/project_state.json`.
`LAC_HONG_1288` — TẠM DỪNG (giữ cho kênh Việt sau).

## Bài học kỹ thuật
`docs/learnings_novelvids.md` — tail-frame chaining (`chain_from` trong jobs.json), derived asset states, resume, cost log.
Cần `ffmpeg` (brew install ffmpeg) cho chain + ghép.
