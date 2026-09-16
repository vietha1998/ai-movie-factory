# BÀI HỌC TỪ github.com/vietcanhvn/novelvids (đọc 2026-09-16)
Repo: nền tảng Trung Quốc biến tiểu thuyết → phim ngắn AI (FastAPI + Vue, Seedream/Seedance/MiniMax/Wan, ffmpeg). License CC BY-NC.
Không dùng code (stack khác, license phi thương mại). Áp dụng KỸ THUẬT:

| # | Kỹ thuật của novelvids | Áp dụng vào xưởng của ta | Trạng thái |
|---|---|---|---|
| 1 | **Tail-frame continuity**: ffmpeg trích frame cuối clip N → làm first-frame clip N+1 (tự động trong batch) | `tools/glabs_client.py` thêm `extract_last_frame()` + cờ `--chain` trong batch video: nếu scene có `chain_from: SC_prev` → dùng frame cuối SC_prev làm `start_image` (Veo `start_image`) hoặc `start_end_image` (start = tail, end = keyframe cảnh). Dùng cho cảnh liên tục cùng địa điểm. | ✅ đã thêm |
| 2 | `@{asset_name}` binding trong prompt để model không nhầm nhân vật | G-Labs hỗ trợ `@name` với `reference_images[].name` → mọi image prompt dùng `@CHAR_001` `@LOC_002` | ✅ trong template 04 |
| 3 | Asset có **derived forms** (trang phục, tuổi, trạng thái) + lịch sử phiên bản, chọn "current" | `DERIVED_STATES` trong character bible (dusty_ep2, muddy_ep5…) → ref sheet riêng; `production_manifest.json.asset_versions{asset: {current, history[]}}` | ✅ manifest có trường; agent character xuất DERIVED_STATES |
| 4 | Prompt cảnh cô lập hoàn toàn: thời gian, môi trường, vị trí, action start/stop, âm thanh | scenes_epN.json thêm `action_start`, `action_end`, `sound` bên cạnh image/video prompt | ✅ template 04 §C (cập nhật) |
| 5 | Task reconciliation loop (30 s, batch 50) — trình duyệt đóng vẫn chạy | G-Labs mất task khi restart → ta lưu task_id vào `glabs_results.jsonl` ngay khi 202 và tải ngay khi completed; thêm lệnh `resume` quét jobs chưa có file để chạy lại | ✅ đã thêm `resume` |
| 6 | Log chi phí mỗi task (token/giây, giá) | `glabs_results.jsonl` thêm `model`, `resolution`, `seconds`, `elapsed_s` → tổng hợp chi phí/tập | ✅ đã thêm |
| 7 | Thư viện giọng theo nhân vật (voice timbre) | `08_audio/voices.json`: map CHAR_ID → giọng TTS Hàn (narrator riêng); chọn TTS sau (blocker) | ⏳ chờ chọn TTS |
| 8 | Remake pipeline: PySceneDetect tách shot video đối thủ để học nhịp | MODE A (video đối thủ): tùy chọn tách shot bằng ffmpeg scene detect để đo shot length — không cần ngay | ⏳ optional |
| 9 | Ghép chương bằng ffmpeg concat theo thứ tự shot | `tools/assemble.py` (concat + ken-burns ảnh tĩnh + sub cứng KO + mix narrator/thoại/SFX/nhạc) | ⏳ viết ở giai đoạn edit |
| 10 | Infinite canvas + version switch UI | Không cần — ta dùng file + manifest | — |
