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

## 2026-09-16 · QC 4화 script v1 (qc-reviewer · projects/SALSU_612/logs/qc_ep4_script.md)
| # | Điều học được | Đã sửa ở / cần sửa ở |
|---|---|---|
| L-16 | **Prop/state do script-writer "diễn giải ngoài outline" ở tập N phải vào bible TRƯỚC khi viết tập N+1.** 3화 v1 cho 한승우 cầm mũ trống của 태오 (4 SC, ghi P-49) nhưng bible/§8b vẫn "mũ mất" → 4화 và 5화 (viết song song theo bible) nói mũ không về → BLOCK xuyên tập. Chạy script song song 5 tập = mọi "nhật ký diễn giải" của tập trước là nguồn sự thật chưa được gom. | Quy trình: sau mỗi script v1, coordinator gom mục D "nhật ký diễn giải" + P-4x prop vào prop/character_bible (bản "delta") trước khi tập sau bắt đầu; qc-reviewer thêm mục "prop state nối tiếp" đọc phụ lục D tập trước. |
| L-17 | **Công thức narrator lặp toàn series phải có "từ điển series".** 1/2/3/5화 dùng "천사백 년 전/뒤", 4화 dùng "이천 년" ×11 — sai số (612→2026 = 1.414) và lệch giọng series; QC 1화 không bắt được vì chỉ soi 1 tập. | SCRIPT_BRIEF thêm bảng "công thức lặp": 천사백 년 · 말하는 돌 · 쇠새 · 쇠수레 · 하늘의 눈 · 이 땅; script-writer grep tập trước trước khi nộp; qc-reviewer grep chéo 5 tập cho các cụm số năm. |
| L-18 | **Bảng ngày/đêm (L-11) chưa đủ khi mốc nằm ở tập trước:** "보름째/보름 남짓/열흘 전" trong 4화 đều tính sai vì không có dòng quy đổi "4화 D1 = 3화 D20"; script-writer thậm chí sửa "열흘째" (đúng) của outline thành "보름째" (sai). | Header bảng ngày/đêm bắt buộc có dòng "D1 tập này = D? tập trước"; mọi từ chỉ khoảng thời gian tới sự kiện tập trước phải ghi phép tính trong scratch. |
| L-19 | **Trái/phải và chi tiết derived state EN phải chép nguyên từ bible vào [ACTION]** — 4화 "cẳng tay trái" vs derived "right forearm" (ref đã sinh); cùng loại với 5화 P-38 (vết thương 해모루). Lỗi này rẻ ở script, đắt ở veo-stage. | script-writer checklist: trước khi viết trạng thái bị thương/đeo kính/đội mũ → mở dòng derived_state của nhân vật, chép EN; qc-reviewer soi "trái/phải/mắt nào" theo bible. |
| L-20 | **"Tập im lặng" cần metric riêng:** benchmark #4/#5 đo "bóp cò/combat" nên 4화 (thiết kế không nổ súng tới 19:07) thua gốc dù retention beat dày nhất 4 tập (1 beat/16 s). Cách đếm combat của script-writer (khối, gộp "địch đi qua trên đầu") cho 36,9 %, đếm thuần chỉ 16 % — hai cách lệch >2×. | benchmark: #4 thêm cột "contact vật lý ≤2 m"; #5 ghi 2 số khối/thuần theo định nghĩa phụ lục 3화 (SC có giao chiến/hỏa lực đang diễn ra vs khối kèm setup/aftermath) để các tập so được với nhau. |
