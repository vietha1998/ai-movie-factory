# G-LABS AUTOMATION WEBHOOK — API REFERENCE (rút gọn từ WEBHOOK_INTEGRATION.vi.md, 2026-09-16)
Nguồn: https://github.com/duckmartians/G-Labs-Automation/blob/main/WEBHOOK_INTEGRATION.vi.md

## Yêu cầu
- G-Labs app đang mở, tab Webhook bật, license **MAX**. Base mặc định `http://127.0.0.1:8765`.
- Google account đăng nhập + enabled trong app (Flow/Veo). 4K & `veo_31_lite_relaxed` cần **ULTRA**.
- Key: header `X-API-Key: <key>` (lưu tại `config/glabs.env`).
- **Không có webhook callback** — chỉ polling. Task mất khi restart app → tải kết quả ngay trong phiên.

## Endpoints
| Method | Path | Auth |
|---|---|---|
| GET | /api/health | — |
| POST | /api/image/generate | ✓ |
| POST | /api/video/generate | ✓ |
| POST | /api/upscale/generate | ✓ |
| POST | /api/grok/generate · /api/meta/generate · /api/openai/generate | ✓ |
| GET | /api/status/{task_id} · /api/result/{task_id} · /api/tasks | ✓ |
| GET | /api/files/{filename} | — |

## IMAGE — POST /api/image/generate
```json
{"prompt":"...", "model":"nano_banana_pro|nano_banana_2|nano_banana_2_lite",
 "aspect_ratio":"16:9|9:16|1:1|3:4|4:3",
 "reference_images":[ "data:image/png;base64,...", {"path":"/abs/x.png","name":"hero","category":"subject"} ],
 "upscale":["2K","4K"]}
```
- Tối đa 10 ref. `@name` trong prompt tham chiếu ref theo `name` (substring, không phân biệt hoa thường).
- Object `{"path": ...}` chỉ dùng khi client cùng máy với G-Labs (ta cùng máy → dùng path, tiết kiệm băng thông).

## VIDEO — POST /api/video/generate
```json
{"prompt":"...", "model":"veo_31_fast|veo_31_lite|veo_31_quality|veo_31_lite_relaxed|omni_flash",
 "aspect_ratio":"16:9", "mode":"text_to_video|start_image|start_end_image|components",
 "reference_images":[...max 3 (Veo) / 7 (omni_flash)...],
 "resolution":["720p"|"1080p"|"4K"], "video_length":8, "voice":"aoede (components only)"}
```
- Pipeline dùng: `mode: "start_image"` (ảnh scene đã QC làm frame đầu) + `video_length: 8` + `1080p`.
- `components` + `@name` cho consistency nhân vật khi không có ảnh scene.

## UPSCALE — POST /api/upscale/generate
`{"image_path":"/abs/x.png","scale":4,"model":"upscayl-standard-4x"}` — tuần tự, 1 GPU.

## Job flow
1. POST → 202 `{"task_id","status":"pending","poll_url"}`
2. GET /api/status/{id} mỗi 3–5s → `pending|running|completed|failed`
3. completed → `results: ["http://127.0.0.1:8765/api/files/xxx.png"]` → GET tải về.
4. failed → `error_code`: 429 quota (đợi & retry) · 403 session hết hạn · 400 policy/invalid · 500 upstream · 0 validation/timeout.

## Giới hạn
- Body ≤ 50MB. ~5 task song song/account (image/video). Upscale tuần tự.
- HTTP 403 "Webhook requires MAX plan" nếu license không đủ.
