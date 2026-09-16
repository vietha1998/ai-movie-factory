# SCRIPT BRIEF — 살수 612 (áp dụng cho MỌI tập · v1 · 2026-09-16, đúc kết từ QC 1화)

## Đọc bắt buộc (theo thứ tự)
1. `series_foundation.md` (§4 nhân vật · §5 tài nguyên · §7 arc tập · §8 + §8b ngôn ngữ/xưng hô · §10 anti-copy)
2. `outline_epN.md` — KHUNG 12 PHẦN BẮT BUỘC (phút ±30 s, LOC/CHAR, tài nguyên giảm, open loop, quotes, mid-roll)
3. `story_bible.md` (timeline [史]/[推]/[傳]/[虚], quy tắc 시호) · `character_bible.md` (giọng từng nhân vật, câu mẫu) · `location_bible.md` · `vehicle_bible.md` · `resource_ledger.md` (lệch → OUTLINE là chuẩn) · `logs/decisions.md`
4. `full_script_ep1.md` v3 — **chuẩn định dạng & giọng**; đọc header + Phần 1, 5, 10, 12 + phụ lục thống kê để bắt nhịp. Tập sau phải nối giọng/callback với tập trước qua outline.
5. `channel_reference/actionchannelai_style.md` §4/§19b/§20 · `templates/06_longform_retention_addendum.md` · `docs/benchmark_vs_reference.md` (18 chỉ số — tự chấm trước khi nộp)

## Spec S40 (cứng)
38–42 phút · 12 phần theo outline · 250–290 SC (video8s 8 s + still_kenburns 6–12 s) · narration KO 격식체 **≥3.500 어절** (≤15 어절/câu) phủ ~70% · thoại 120–160 câu (≤12 어절, ≤1 câu/SC) · 0–30 s KHÔNG narrator · 1–2 vùng narrator im ở đỉnh trận (60–90 s) · [MID-ROLL] sau open loop nhỏ · [END CARD] · **combat ≥30% runtime, ≥5 khối** (mini-combat 20–40 s ở các phần chính trị/hậu cần để không có khoảng >4 phút không action) · **0–30 s ≥5 shot** (dùng 2-BEAT trong clip nếu cần).

## Ngân sách đọc TTS (cứng — từ QC 3화)
- video8s: N + thoại **≤22 어절**/SC · still 6–12 s: **≤45 어절** · toàn tập **≤115 어절/phút** (narration+thoại). Script-writer in bảng SC vượt ngưỡng ở phụ lục và phải = 0.

## Định dạng (giống ep1 v3)
Header: runtime · tổng shot · mid-roll · **BẢNG NGÀY/ĐÊM** (ngày N · buổi · SC từ–đến · sự kiện [史] cùng ngày) — mọi câu "X일째/이틀 뒤/간밤에" phải khớp bảng.
`## [Phần X] tên KO / VI (phút)` + tóm tắt VI + chức năng/tài nguyên/open loop → `### SC_nnn · LOC · CHAR · VEH · video8s|still_kenburns · t1–t2` + `[ACTION-VI]` + `[SOUND]` + `N:` + `TÊN: thoại` → `[Kết thúc Phần X]`. Cuối file: bảng thống kê tự đếm (SC, video/still, giây, câu thoại, 어절 N, **combat giây/%**, câu vi phạm) + tự kiểm 7 mục + nhật ký diễn giải ngoài outline.

## Checklist lỗi đã gặp ở 1화 — KHÔNG lặp
- [ ] Địch/khí tài xuất hiện đúng thời điểm địa lý-timeline (kỵ Tiên Ti chỉ sau khi cầu phao nối; quân Tùy ở đâu ngày nào theo story_bible).
- [ ] **시호**: người đương thời không nói 영양왕/수 양제; dùng 대왕·전하·재위 N년 / 폐하·황상. Narrator và lính Hàn (nói với nhau) được dùng.
- [ ] Mọi con số tài nguyên nói ra phải có NGUỒN trong ledger/SC trước (dầu, đạn, pin, thuốc) — không "이틀에 육십 킬로" vô căn.
- [ ] Không "đứng nói" >2 SC liên tiếp → xen insert (tay/bản đồ/ngoài lều/địch quan sát) hoặc walk-and-talk.
- [ ] 1 SC = 1 địa điểm, ≤2 người nói; không hành động cần >8 s (đi qua cổng đông rồi lên tường tây).
- [ ] Radio protocol: gọi "[người nghe], 여기는 [người gọi]"; không tự gọi callsign xe mình.
- [ ] Từ đúng thời: 전령/사자 (không 기사), 나각 (không 나팔), 황공하오나 (không 무례하오나), 전군총관/선봉장 phân biệt người.
- [ ] Narrator không nói trước điều thoại sắp reveal, không lặp điều thoại vừa nói, thì quá khứ "-였습니다/-했습니다" thống nhất (câu mở địa danh có thể "N년 M월. 지명.").
- [ ] Nhân vật lịch sử RA QUYẾT ĐỊNH nhìn thấy được (양제 "뇌군이라 하라" là mẫu) — narrator không quyết thay.
- [ ] Không tableau "2 chỉ huy trên tường nhìn địch → lều địch → end card" giống kênh gốc §17; kết bằng hành động khác.
- [ ] Không nhắc Bắc Triều Tiên trực tiếp ("적", "이 땅"); không khẩu hiệu.
- [ ] Quy ước thông ngôn P-11: Tùy ↔ lính Hàn không hiểu nhau trực tiếp.
- [ ] Chữ Hangul trên xe không vẽ bằng AI (mô tả bình thường, edit overlay).

## Đòn bẩy "hay hơn kênh gốc" phải có mỗi tập
địch có tên & học (탁발흠 rút ra 1 bài học/tập, nói thành lời) · ≥6 con số tài nguyên nói thành lời · nhân vật lịch sử là bộ não (≥3 quyết định) · chi phí thật (xe/người/đạn) · open loop cuối MỖI phần · ≥5 quote đắt (KO+VI) ghi cuối file.

## Ghi file
Append từng phần (12 lần), không ghi một lần. Copy sang `output/epN/kich_ban/full_script.md`. Đề xuất đổi foundation/outline → `logs/proposals.md` (không tự đổi). Scratch: `logs/scratch/script-writer-epN/`. Không chạm file tập khác, state, ledger (ghi đề xuất số cần sửa ledger vào proposals).
