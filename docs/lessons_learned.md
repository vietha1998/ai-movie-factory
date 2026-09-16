# LESSONS LEARNED — cập nhật sau MỖI sản phẩm (bắt buộc, xem CLAUDE.md "Quy trình sau deliverable")
Format: ngày · sản phẩm · lỗi/điều học được · sửa ở đâu (template/agent/foundation/tool).

## 2026-09-16 · Giai đoạn tiền kỳ SALSU_612 (foundation → bible → outline)
| # | Điều học được | Đã sửa ở |
|---|---|---|
| L-01 | Phải chốt **thị trường + ngôn ngữ + khán giả + độ dài** TRƯỚC khi viết foundation — đổi sau làm mất 3 agent (LAC_HONG_1288). | CLAUDE.md: checklist "NEW PROJECT" hỏi 4 câu này nếu chưa có. |
| L-02 | Foundation trước, agent sau, mỗi agent 1 nhánh file riêng → không mâu thuẫn. Nhưng agent chạy song song **ghi đè scratchpad chung** (world vs character build script). | .claude/agents/*: scratch riêng `logs/scratch/<agent>/`. |
| L-03 | Tên địa danh THẬT phải kiểm tra vị trí địa lý so với trình tự outline (청석령 nằm bắc Áp Lục nhưng outline đặt sau Áp Lục) → dùng tên hư cấu [虚] khi trình tự truyện cần. | story_bible quy tắc: mọi địa danh thật phải ghi tọa độ tương đối + ngày; nếu lệch → [虚]. qc-reviewer thêm mục "địa lý". |
| L-04 | Story-director và world-designer chạy song song sinh **số liệu lệch** (K2 −10/−4 vs −12/−2). Chốt: OUTLINE là chuẩn, ledger theo sau. | CLAUDE.md thứ tự ưu tiên nguồn: foundation > outline > ledger > bible. |
| L-05 | Agent hỏi nhiều quyết định nhỏ → người điều phối quyết ngay theo "routine judgment", ghi `logs/decisions.md`; chỉ hỏi user khi đổi thị trường/câu chuyện/format. | decisions.md là file bắt buộc của project. |
| L-06 | Kênh gốc **không narrator** nhưng format 40' cần narrator → hybrid; giữ luật "0–30 s không narrator, narrator im ở đỉnh trận". | channel style §19b, templates/06 §8. |
| L-07 | Kênh gốc: nội dung KHÔNG phải lịch sử của khán giả → thất bại (2–29K). Chọn trận của chính dân tộc khán giả. | CLAUDE.md thị trường. |
| L-08 | Git: không có gh/SSH → user phải nhập token vào ô ẩn → lỗi. SSH key + public key dán trên web = 1 lần, sạch. | README: hướng dẫn SSH. |
| L-09 | User dán mật khẩu/token vào chat → nhắc thu hồi, không dùng, không lưu; dọn history. | — |
| L-10 | Agent không được chạm `project_state.json` → coordinator cập nhật sau mỗi agent; tốt, giữ. | agents. |
