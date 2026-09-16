# BENCHMARK — SO VỚI KÊNH GỐC (@actionchannelai) VÀ VƯỢT LÊN
Mục tiêu: mỗi tập của ta phải ĐO ĐƯỢC là bằng hoặc hơn video top của kênh gốc trên từng chỉ số, không chỉ "cảm thấy hay".
Nguồn số kênh gốc: `channel_reference/actionchannelai_style.md` (Jinju 268K · Steel Platoon Ep1 201K · Haengju 199K).

## Bảng chỉ số (điền cho từng tập — QC reviewer chấm, người điều phối duyệt)
| # | Chỉ số | Kênh gốc (8–15') | Mục tiêu của ta (40') | Cách đo | Tập 1 | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Giây đầu tiên có nguy hiểm/câu hỏi | ≤ 0:10 (comms cut / paratroopers) | ≤ 0:10 | SC đầu có tên nguy cơ | **0:02** (SC_001 mũi tên cắm lốp; 0:32 lính gác thấy kỵ binh) | ✅ ĐẠT. Vật lạc thời + nguy cơ trước 0:10, không giải thích. |
| 2 | Số shot trong 30 s đầu | 13 | ≥ 5 (S40 hook 0–1:30 ≈ 11–12 SC) | đếm SC 0:00–0:30 | **4** (SC_001–004; 12 SC trong 0–1:30) | ❌ THUA mục tiêu ≥5 và kênh gốc 13. Sửa rẻ: tách SC_001, chèn insert 4 s → 6 (qc_ep1 FIX). |
| 3 | Narrator trong 30 s đầu | 0 | 0 | grep N: trước 0:30 | **0** — narrator vào 0:48 (SC_007 "612년 정월. 탁군.") | ✅ ĐẠT. |
| 4 | Lần giao tranh đầu | 1:36 (Jinju) · 0:52 (Haengju) | ≤ 7:00 (P4) | thời điểm SC đầu có muzzle flash/tên bắn | Sử (Goguryeo vs Tùy ở cầu phao): **7:18** (SC_055) · Đại đội bóp cò: **12:14** (SC_091) | ⚠️ Biên: 7:18 lệch mục tiêu ≤7:00 18 s; ❌ THUA kênh gốc (0:52–1:36) và đại đội chỉ bắn ở 12:14. Cấu trúc outline khóa; bù bằng combat mini P7/P8 (qc §3 #1). |
| 5 | Tỷ lệ combat/runtime | ~45% | ≥ 35% (40' có chính trị/hậu cần) | tổng giây SC có chiến đấu ÷ tổng | **≈22–23 %** (P4 32 s · P5 80 s · P8 16 s · P10 402 s = ~530 s / 2.400) | ❌ THUA mục tiêu ≥35 % và kênh gốc 45 %. Chỉ 3 khối action thật (spec S40 ≥6); 14:00–27:30 không có giao tranh. Đề xuất nâng ~30 % không đổi số SC (qc §3 #1). |
| 6 | Khoảng cách tối đa giữa 2 beat retention | ~2–3 phút | ≤ 4 phút | list beat (action/reveal/số giảm/quyết định/địch thích nghi) | Mọi beat: **1:02** (3:20→4:22) · Beat mạnh: **2:40** (23:50→26:30, P9 sa bàn) | ✅ ĐẠT ≤4'; ngang kênh gốc. 93 beat / 40' (≈1/26 s). Vùng yếu: P9 kế hoạch, 1:38–2:26 giới thiệu nhân vật. |
| 7 | Con số tài nguyên nói thành lời | ~1–2/video | ≥ 6/tập (≥1 mỗi 7') | grep thoại có số | **~26 câu thoại có số tài nguyên** (위성 0 · 연료 한 통 · 항생제 20/모르핀 30 · 94명 · 포탄 22 · 식량 3/물 2 · 배터리 30/18/12 · 식량 이틀 · 30km · 2리터 · 나흘치 · 90% · 야시경 12 · 24분 · 480/110/사흘치 · 60km…) + 8 câu N có số | ✅ HƠN xa (mục tiêu ≥6). Lưu ý 1 số không có nguồn: "이틀에 60km" (FIX★). |
| 8 | Góc nhìn địch (enemy POV) | 2–3 cảnh | ≥ 5 cảnh, địch CÓ TÊN & THÍCH NGHI | đếm SC LOC_004/CHAR_2xx | **32 SC** enemy POV / ~8 cảnh (탁군 ×4 still · 탁발흠 đồi ×7 · lều 선봉장 ×5 · 2.000 kỵ ×1 · P10 ×4 · P11 ×1 · lều 양제 ×9). Địch có tên: 탁발흠 thích nghi 4 lần (quan sát, nhặt drone, nhắm xe bò, học lửa-lưới) | ✅ HƠN (mục tiêu ≥5). Cải thiện: cho hắn *áp dụng* bài học trong cùng trận (qc §3 #7); BLOCK SC_006 gắn nhầm VEH_206 ngày 1. |
| 9 | Nhân vật lịch sử ra quyết định | 1–2 quyết định | ≥ 3 quyết định thay đổi plot | list | **5** nếu tính nhân vật Goguryeo hư cấu: 해모루 (dẫn vào thành; chờ tù và), 고정수 (thung lũng+con tin; giao nhiệm vụ; mở cổng), 선봉장 (2.000 kỵ), 영양왕 (chiếu), 양제 (가져오라). Nhân vật **sử thật** quyết: **2** (양제, 영양왕) | ✅ ĐẠT theo cách đếm outline (≥3) · ⚠️ chỉ 2 người thật; 을지문덕 giữ cho 2화. Nâng: 양제 tự đặt tên "뇌군" (qc §3 #3). |
| 10 | Số câu thoại | 60–70 (8') | 120–160 (40') | đếm | **147** câu thoại (한승우 33 · 태오 18 · 박기철 17 · 오태민 13 · 해모루 12 · 고정수 9 · 백성민 8 · 을보 6 · 아리 5 · 서아 4 · 탁발흠 4 · 선봉장 4 · 양제 2 · 영양왕 2 · phụ 8) | ✅ ĐẠT (120–160). Phân bổ ≈ hiện đại 66 % / Goguryeo 25 % / Tùy 9 % — Tùy hơi ít so với kênh gốc 20 %. |
| 11 | Thoại > 12 어절 | — | 0 | script | **0** / 147 (dài nhất 11 어절) | ✅ ĐẠT. Lỗi đăng ký nhỏ: SC_186 kính ngữ, SC_090/222 tự gọi callsign xe mình, SC_270 "기사", SC_066/166/282 (qc bảng). |
| 12 | Câu "quote đắt" (dùng được cho title/thumbnail) | 1–2 | ≥ 5 | list | **≥9**: "쏜다. 대신 전차는 안 나간다" · "편자가 없습니다" · "어느 성의 군사요" · "역사가 이미 이겼다" · "손에 천둥을 쥐고"/"그 천둥을 가져오라" · "성 안에 갇힌 전차는 관입니다" · "그대들이 있어서 저들도 여기 온 것이오" · "전차는 한 발도 안 쐈다" · "쇠가 우는 소리군" · N "고구려는 이겼습니다. 그날은." | ✅ HƠN (≥5). Thêm ứng viên nếu duyệt: 양제 "뇌군이라 하라". |
| 13 | Shot trung bình | ~4 s | 8–10 s (clip 8 s + still 6–10 s) | tổng giây ÷ SC | **8,25 s** (2.400 s / 291 SC; video 233×8 s, still 40×10 s + 14×8 s + 4×6 s) · Trong trận P10: **8,1 s** (52 SC/420 s) | ✅ ĐẠT khung 8–10 s · ❌ THUA kênh gốc trong trận (4 s): outline hứa 4–6 s nhưng script toàn 8 s → veo-stage cắt đôi ~15 clip (qc §3 #10). |
| 14 | Kết mở (open loop) | có, 30 s cuối + end card | có + gieo hạt series 2 | P12 | Có: P12 chiếu vua + "가져오라" + N "113만이… 94명을 찾고 있었습니다" + K2 "아직 한 번도 울지 않았습니다" + end card 2화; 12/12 phần kết open loop đúng câu outline | ✅ ĐẠT. Hạt series 2 chưa cần ở 1화 (gieo 5화 P12). |
| 15 | Mid-roll đặt sau open loop nhỏ | — | 4 điểm (7/14/21/27:30) | [MID-ROLL] | **4** đúng 7:00 · 14:00 · 21:00 · 27:30; mỗi điểm sau open loop + 1 SC không thoại sau mid-roll (SC_053/104/155/202) | ✅ ĐẠT. |
| 16 | Yếu tố kênh gốc KHÔNG có mà ta có | — | hậu cần là nhân vật · hành trình bỏ xe · "để địch đi qua" · địch có tên | check | Hậu cần: 박기철 đọc số 6 lần, bảng đếm treo lều (SC_169/198) ✓ · K2 không lọt cổng + không bắn ✓ · bò + kỵ Goguryeo kéo K21 ✓ · địch có tên nhặt drone ✓ · cậu bé trinh sát/trả mũi tên ✓ · "để địch đi qua"/bỏ xe: chưa (3–4화) | ✅ ĐẠT — 5/6 yếu tố riêng có mặt ở tập 1. |
| 17 | Lỗi lịch sử cứng (năm/tên/kết quả gốc) | 0 | 0 | qc | **0 lỗi cứng** (113만 3천 8백 · 24군/40리/960리/40일 · 우문개 3 cầu · 1장 · 맥철장/전사웅/맹차 · nối cầu 2 ngày · 영양왕 = vua 26 · 육합성 chưa dựng). **1 lỗi mềm:** người đương thời gọi vua đang sống bằng 시호 "영양왕" (SC_115). Bỏ sót [史]: Goguryeo mất 1만 ở lần vượt 2. | ⚠️ FIX★ SC_115 (đề xuất 한승우 tự suy ra 612). Địa lý theo trình tự: đúng. |
| 18 | Trình tự giống kênh gốc | — | KHÔNG (gặp tướng→trình diễn súng→kinh ngạc→tăng→trận→rút) | qc | KHÔNG giống trình tự cấm. Trình tự thật: tên cắm lốp → sử cầu phao → trinh sát nhí → bắn vì dân, giấu K2 → "어느 성" → xe không lọt cổng → giữ đường đông → địch nhắm xe bò, bò kéo xe → 고정수 mở cổng → chiếu vua → "가져오라". K2 0 viên. | ✅ ĐẠT · ⚠️ 2 NOTE anti-copy: khung kết (2 chỉ huy trên tường → lều địch ra lệnh → card) trùng skeleton §17; beat "몇 년입니까" trùng S15 — cả hai có phương án sửa rẻ (qc §3 #2, #5). |

### Kết luận chấm Tập 1 (script v1 · qc-reviewer 2026-09-16)
- **THUA kênh gốc / mục tiêu:** #2 shot 30 s đầu (4 < 5, gốc 13) · #4 giao tranh đầu (đại đội 12:14, gốc ≤1:36) · **#5 combat 22 % (mục tiêu 35 %, gốc 45 %)** · #13 shot trong trận 8 s (gốc 4 s).
- **Biên/mềm:** #9 chỉ 2 nhân vật sử thật quyết định · #17 1 lỗi 시호 · #18 khung kết gần §17.
- **HƠN kênh gốc:** #7 số tài nguyên (26 vs 1–2) · #8 enemy POV có tên & học (32 SC vs 2–3) · #12 quote (≥9 vs 1–2) · #14/#15/#16 ✓.
- Chi tiết + đề xuất: `projects/SALSU_612/logs/qc_ep1_script.md`.

## "Hay hơn kênh gốc" — 5 đòn bẩy cố định
1. **Địch thông minh có tên** (kênh gốc: địch vô danh, chỉ hoảng loạn) → 탁발흠 học sau mỗi trận.
2. **Hậu cần là đồng hồ đếm ngược nói thành lời** (kênh gốc: đạn vô hạn ngầm định).
3. **Nhân vật lịch sử là bộ não của trận quyết định** (kênh gốc: tướng giải thích rồi giao súng).
4. **Chi phí cảm xúc có thật** (thương vong, bỏ xe, xe cháy) nhưng không giết nhân vật có tên (khán giả 50+ cần điểm tựa).
5. **Mọi phần kết bằng open loop** (kênh gốc chỉ có ở cuối video).

## Điểm mạnh kênh gốc PHẢI giữ (không được kém hơn)
- Hook không giải thích · aerial "không thấy điểm cuối" · contrast trong cùng khung hình · thumbnail số · series có tên · nhịp thoại ngắn.
