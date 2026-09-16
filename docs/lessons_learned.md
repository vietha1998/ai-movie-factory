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

## 2026-09-16 · QC 1화 script v1 (qc-reviewer · projects/SALSU_612/logs/qc_ep1_script.md)
| # | Điều học được | Đã sửa ở / cần sửa ở |
|---|---|---|
| L-11 | **Timeline nội tại phải có bảng "ngày/đêm thứ mấy" trong script**: 1화 lệch 3 chỗ (kỵ Tiên Ti bờ đông ngày 1 khi cầu chưa nối; "사흘째 밤" thực ra là đêm 4; đại quân "이틀 빨랐다" nhưng vòng vây đã khép đêm 4). Outline chỉ ghi phút phim, không ghi ngày truyện. | script-writer.md: thêm bắt buộc "bảng D-day/đêm theo SC" ở phụ lục; outline template thêm cột "ngày truyện". |
| L-12 | **Số ★ của outline/ledger phải có SC chứng minh**: "이틀에 60km" (K2 chỉ chạy 1 đêm, đêm trận tắt máy) và pin drone "12 phút" (có pin rời) là số đúng bảng nhưng không có nguồn hình. Script-writer đã chép số, chưa dựng hành động sinh ra số. | resource_ledger: thêm cột "SC sinh ra số"; qc-reviewer soi "số có SC nguồn?" thay vì chỉ "số khớp bảng". |
| L-13 | **시호 (tên thụy) không được đặt vào miệng người đương thời** — "영양왕 23년" trong outline/foundation là lỗi 사극 kinh điển với khán giả 50+. Cách hay hơn: lính Hàn tự suy ra năm từ dữ kiện (수나라 + 백만 + 요동성 = 612), người Goguryeo chỉ nói "대왕 즉위 스물세 해째". | foundation §8 thêm dòng "vua đang sống: 대왕/전하/금상, không dùng 시호"; story_bible §5.5. |
| L-14 | **Combat 40' không tự đủ**: outline 12 phần theo template chỉ sinh 3 khối action (22 %) vì P6–P9 toàn chính trị/kế hoạch → 13,5 phút không tiếng súng. Phải chèn "combat mini" (trinh sát địch bám đuôi, tên cắm lưới) vào P7/P8 ngay từ outline, và shot trong trận phải 4–6 s như đã hứa (script để 8 s đều). | templates/06 §1 thêm "mỗi phần ≥1 SC có hỏa lực/đe dọa vật lý"; veo-prompt: cắt đôi clip trận. |
| L-15 | **Thủ tục vô tuyến ROK**: nhân vật không tự gọi callsign xe mình ("천둥 2, …" khi đang ở 천둥 2); dùng "포수/조종수" cho nội bộ xe. Từ thời đại: "기사" → 전령/사자; "께서 + 하오" phải có -시-. Khán giả 50+ có nhiều cựu binh và người xem 사극 — hai nhóm soi hai lỗi này. | character_bible §"Giọng" thêm 3 dòng quy tắc radio; script-writer checklist đăng ký. |
