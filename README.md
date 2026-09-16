# AI Movie Factory — Military Time Travel (thị trường Hàn Quốc)

Xưởng sản xuất video YouTube AI cinematic: quân đội hiện đại xuyên không về trận đánh lịch sử.
Vận hành bằng Claude Code + G-Labs Automation (Veo/Nano Banana). Đọc `CLAUDE.md` để biết toàn bộ quy tắc.

## Cài đặt trên máy mới (Mac / Windows)
1. Cài Python 3.9+ (Windows: python.org, tick "Add to PATH").
2. Clone repo, rồi trong thư mục dự án:
   ```bash
   python3 tools/setup_ffmpeg.py        # Windows: py tools\setup_ffmpeg.py
   ```
   → tải ffmpeg tĩnh vào `tools/bin/` (không cần Homebrew/choco).
3. Tạo `config/glabs.env` (KHÔNG có trong git) với nội dung:
   ```
   GLABS_BASE_URL=http://127.0.0.1:8765
   GLABS_API_KEY=<key trong app G-Labs, tab Webhook>
   GLABS_IMAGE_MODEL=nano_banana_pro
   GLABS_VIDEO_MODEL=veo_31_fast
   GLABS_VIDEO_RESOLUTION=1080p
   GLABS_POLL_SECONDS=4
   GLABS_TIMEOUT_SECONDS=900
   ```
4. Mở app G-Labs → tab Webhook → bật server. Kiểm tra:
   ```bash
   python3 tools/glabs_client.py health
   ```

## Cấu trúc
- `MASTER_PROMPT.md` — quy tắc tổng · `templates/` — prompt từng bước · `channel_reference/` — phân tích kênh tham chiếu
- `projects/<PROJECT>/` — pipeline đầy đủ 00_input → 12_final · `output/epN/` — thư mục giao hàng theo tập
- `tools/glabs_client.py` — client G-Labs (image/video/upscale/batch/resume/chain) · `docs/` — API + bài học
- `.claude/agents/` — 8 agent chuyên trách chạy song song

## Media
Ảnh/video sinh ra không commit (xem `.gitignore`). Sao lưu riêng `projects/*/0[5-9]_*`, `12_final`, `output/*/canh`, `output/*/final_video`.
