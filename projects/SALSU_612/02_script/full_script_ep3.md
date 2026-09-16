# 살수 612 — 3화 「남하」 대본 v2 (QC-fixed)

> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (241 video8s + 46 still_kenburns) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer
> **v2 (QC-fixed, 2026-09-16):** áp dụng logs/qc_ep3_script.md (1 BLOCK + 20 FIX + NOTE ≤1 dòng) theo decisions.md mục "sau QC 3화 → v2" + SCRIPT_BRIEF "Ngân sách đọc TTS" (video8s ≤22 어절 N+thoại · still ≤45 · toàn tập ≤115 어절/phút). Không đổi SC ID/thời gian/open loop/quotes/mid-roll (trừ đảo thứ tự nội bộ SC_107–109 trong lều). Xem nhật ký v2 ở phụ lục E.
> **Nguồn:** SCRIPT_BRIEF.md · outline_ep3.md (khung 12 phần — chuẩn) · series_foundation.md (§7 3화, §8, §8b) · story_bible.md (timeline [史] 612 6월: chôn lương · 을지문덕 giả hàng · 우문술/우중문 · vượt 압록) · character_bible.md · location_bible.md (LOC_005_AMNOK, LOC_008, **LOC_009_SEOKMUN_PASS 석문령 [虛]**, LOC_007) · vehicle/prop bible (PROP_022 lương chôn, PROP_023 biển "천둥 3") · resource_ledger.md (lệch → outline) · logs/decisions.md · full_script_ep1.md v3 (chuẩn giọng/định dạng).
> **Quy ước ghi:** `N:` = narration tiếng Hàn (격식체, giọng nam trầm, thì quá khứ "-였습니다/-했습니다"; câu mở địa danh "612년 6월. 압록수."). Trong SC có cả `N:` và thoại: N bình luận → đọc SAU thoại; N dẫn vào → đọc TRƯỚC (editor quyết). `TÊN:` = thoại tiếng Hàn (≤12 어절/dòng). `[ACTION-VI]` = hành động nhìn thấy được (tiếng Việt, cho veo-prompt-engineer). `[SOUND]` = âm thanh gợi ý. `2-BEAT` = 1 SC 8 s gồm 2 shot (chỉ ở hook/trận). `[NARRATOR IM LẶNG]` / `[MID-ROLL]` / `[END CARD]` theo outline.
> **ID:** CHAR_/LOC_/VEH_/UAV_/EQP_/WPN_/PROP_ theo bible. Nhân vật phụ không ID (ghi tên vai): 소년 척후 (~17, từ 1화, đi theo 해모루), 유사룡 (위무사 Tùy — [史], 1 cảnh), 수 전령, 수 기병 사자, 수 총관 (tướng tiền quân 9 quân), 수 낙오병 (lính đào ngũ), 고구려 통역 포로 (thông ngôn Goguryeo bị Tùy bắt), PZF 사수, 박격포 사수, K3 사수 (KIA — không tên), 조종수/포수 K2, 무전병, 선비 부장 (phó của 탁발흠).
> **Quy ước ngôn ngữ (P-11):** trên màn hình mọi phe nói tiếng Hàn. Goguryeo ↔ đại đội hiểu nhau. **Tùy ↔ Goguryeo: 을지문덕 biết Hán văn — trong trại Tùy ông không nói, ông VIẾT (필담); 해모루 nghe rồi dịch thầm cho ông** ([ACTION-VI] ghi rõ). **Tùy ↔ đại đội: không hiểu nhau** — 탁발흠 hỏi 태오 qua 고구려 통역 포로 (P11). Loạt K6 xuống nước (P4): kỵ Tùy báo "천둥" → 우중문 nhận ra 뇌군 ở bờ nam (đã nghe tên ở 육합성 2화) — động cơ vượt sông.
> **Quy tắc 시호:** người đương thời không gọi 영양왕/수 양제 bằng tên thụy — dùng 대왕·전하·재위 N년 / 폐하·황상. Narrator được dùng. Lính Hàn nói với nhau được dùng ("을지문덕 장군" là tên thật, không phải 시호).
> **Tên xe (§8b + ledger):** 천둥 4 cháy 2화 · **천둥 2 bị phá ở P1 (2 quả PZF + dầu)** · **천둥 3 nguyên vẹn → 탁발흠** (biển tên đã tháo, PROP_023). Outline P1 ghi tiêu đề "불타지 않은 4호" → sửa thành **3호** cho khớp open loop "천둥 3호는 불타지 않았습니다" (xem proposals).
> **Số liệu khóa (outline/ledger):** xe 7→1 · K2 12→**8** (4 viên vào vách 석문령) · dầu K2 "산길로 400km, 딱" · cối 60→**50** · PZF 12→**9** (2 phá 천둥 2 + 1 cụm đuốc — theo brief; outline P10 ×3 → proposals) · 40mm 220→0 (160 nổ trong 천둥 2, ~60 nằm trong 천둥 3) · K6 −60 (P4) · drone 2→1 (pin phồng)→0 (bị bắt) · kính đêm 12→**10** · quân số 94→**93** (1 KIA không tên) + 태오 bị bắt = 92 hiện diện.
>
> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi "X일째/이틀 뒤/사흘 만에" trong narration rà theo bảng này):**
>
> | Ngày | Buổi | SC | Sự kiện |
> |---|---|---|---|
> | D1 | đêm | SC_001–011 | LOC_003 (thung lũng sau 요동성): rút dầu; PZF ×2 → 천둥 2; K511 ×2 + K151 cháy; tháo biển "천둥 3"; đuốc 탁발흠 10 phút; xuất phát. (9 quân Tùy đã đi về đông 2 đêm trước — 2화 P11) |
> | D2 | ngày | SC_012–022 | Hai cột song song cách 20리 (đại quân ~70리/ngày, đại đội 30리); kỵ Tùy cánh sườn bị 30 kỵ 해모루 chặn (mini-combat) |
> | D2 | đêm | SC_023–032 | Từ sườn núi thấy lính Tùy đào hố chôn lương dưới lều [史] |
> | D3 | đêm | SC_033–048 | Trạm dừng (LOC_003 Dạng B): "400km 딱" (gom ≈430 ở 2화, đã chạy 30 km) · drone 2→1 · "600미터" · "입이 둘" · lệnh 을지문덕 "닷새" · lính Tùy đào ngũ lạc vào trại · đổi ngựa |
> | D4–D8 | | SC_049–050 | 5 ngày trên ngựa Goguryeo, ~60 km/ngày, mưa |
> | D9 | sáng–chiều [史] | SC_051–075 | 압록수: lính Tùy chôn nốt lương bên bờ; 을지문덕 giả hàng vào trại 우중문; được thả; kỵ sứ đuổi; K6 xuống nước; ông không ngoảnh lại |
> | D10 | sáng [史] | SC_076–078 | 우문술 muốn lui, 우중문 mắng, 우문술 nhượng |
> | D10 | ngày [史] | SC_079–100 | 9 quân vượt 압록수; trận giả thua thứ nhất (300 kỵ + cối 10 viên); 태오 thấy 천둥 3 bị 40 bò kéo ở bờ bắc |
> | D10 | đêm | SC_126–131 | ENEMY (chiếu ở P7, sau P6): 탁발흠 chui vào 천둥 3 bờ bắc; bản đồ bùn → 석문령 (hỏi nông dân 2화); bài học "chim ăn / mắt đêm đứng yên" từ 12 ngày rình thung lũng 요동성 (2화); bịt tai ngựa |
> | D11 | ngày–đêm | SC_101–125 | Đại đội đi 1 ngày về nam; đêm: sơn thành LOC_008 — lều 을지문덕 "살수"; radio cho 해모루; 백성민 chặn 2 척후 Tùy phía nam |
> | D11 | rạng sáng | SC_132–133 | 육합성 (5 ngày trước, 요동): 양제 "산 채로 잡아라" → 전령 tới 탁발흠 bờ bắc 압록; 2.000 kỵ lên đường |
> | D12 | ngày | SC_134–150 | K2 rò nước làm mát trên dốc; hậu vệ 해모루 vs 척후; tên lửa lên nóc K2; làng dưới chân 석문령; 을보 nung đồng; phân ngựa đường dê; 해모루 gửi 3 척후; "3 km"; 탁발흠 nhìn làng từ gờ núi |
> | D12 | chiều tối–đêm | SC_151–172 | Kỵ Tùy cướp ruộng; quyết vá; "허락된 충전 한 번 / 40%"; ngủ sau 3 đêm; 을보 gò đồng; 3 척후 해모루 (đi từ sáng D12) xuống đường dê dưới cung Tiên Ti — 탁발흠 thả |
> | D13 | ngày–đêm | (N SC_173/177) | Vá tiếp; 3 척후 về báo "không có ai" |
> | D14 | rạng sáng–chiều | SC_173–197 | "사흘째 새벽" thử máy, đổ nốt phuy; 소년 척후 chạm 2 척후 Tiên Ti đường đông; bàn cát; 해모루 chiếm cửa nam, đuổi 5 척후; "너무 높다"; lên đèo lúc hoàng hôn |
> | D14 | đêm | SC_198–238 | Trận đèo 석문령 (phase 1–4) |
> | D15 | rạng đông–sáng | SC_239–256 | Phase 5–6; chôn KIA kiểu Goguryeo; 해모루 tách về với 을지문덕 |
> | D15 | đêm | SC_257–263 | ENEMY: 탁발흠 đeo kính đêm; hỏi cung 태오 qua thông ngôn Goguryeo; lệnh gửi 천둥 3 + drone về tây |
> | D16 | ngày | SC_264–268 | 천둥 3 quay về tây (200 kỵ); 우중문 nhận tin "뇌군은 살수로"; tiến [史] |
> | D16 | đêm | SC_269–270 | 태오 ở trại Tiên Ti; 탁발흠 đi đêm bằng kính đêm |
> | D17 | chiều mưa | SC_271–287 | 살수 bãi bắc: 해모루 (đi 2 đêm) mang lệnh "숨으시오"; "사흘 뒤" 30만 tới; nước lên |

---

## [Phần 1] 불타지 않은 3호 — 「불타지 않은 3호」 / Chuyện không thể xảy ra  (0:00–1:30)
> Tóm tắt VI: Đêm, thung lũng sau 요동성. Ống xi-phông, dầu chảy vào can, 박기철 (tay còn băng bỏng từ 2화) đếm to từng lít. Sau lưng: 2 K511 + K151 cháy. Xạ thủ PZF bắn 2 quả vào 천둥 2 — 40mm nổ dây chuyền. 박기철 tháo biển "3" khỏi 천둥 3 (PROP_023). 한승우 đứng trước 천둥 3, lựu đạn nhiệt nhôm trong tay. 오태민: "정말 버립니까?" Radio 백성민: đuốc Tiên Ti, 10 phút. 한승우: "출발." — lựu đạn vẫn trong tay. Aerial: 30만 5천 đi về 압록수. Tên bay vào bùn sau lưng người cuối. 천둥 3 đứng nguyên trong mưa.
> Chức năng: ACTION-HOOK · Tài nguyên: xe 7→1 · PZF 12→10 · 40mm 220→~60 (nằm trong 천둥 3) · Open loop: "천둥 3호는 불타지 않았습니다."
> Ràng buộc: 0:00–0:32 KHÔNG narrator (narrator vào 0:32 bằng địa danh + năm). 0–30 s = 6 shot (SC_001 2-beat · SC_002 · SC_003 2-beat · SC_004).

### SC_001 · LOC_003_CHEONDUNG_BASE (thung lũng, đêm) · CHAR_003 · VEH_002 (천둥 3) · video8s · 0:00–0:08
[ACTION-VI] 2-BEAT: (a) 0:00–0:03 màn đen, chỉ tiếng chất lỏng chảy ồng ộc vào thùng; (b) 0:03–0:08 cận: ống xi-phông cao su cắm vào cổ bình dầu K21 천둥 3, dầu diesel chảy thành dòng vào can 20 L; bàn tay 박기철 quấn băng trắng bẩn (bỏng 2화) giữ ống; ánh cam rung từ phía sau khung.
[SOUND] dầu chảy, kim loại can rung, xa xa lửa cháy gầm nhẹ. Không nhạc.

### SC_002 · LOC_003_CHEONDUNG_BASE · CHAR_003 · VEH_002 (천둥 3) · video8s · 0:08–0:16
[ACTION-VI] 박기철 quỳ cạnh can, mắt nhìn vạch mức, môi đếm; mũ lưỡi trai, thái dương muối tiêu; sau lưng ông, ngoài nét, lửa cam liếm bạt xe tải. Máy tĩnh, đẩy chậm vào miệng ông.
[SOUND] dầu chảy chậm dần, lửa xa, gió.
박기철: …백팔십. 백구십.

### SC_003 · LOC_003_CHEONDUNG_BASE · PZF 사수, CHAR_002 · VEH_002 (천둥 2), VEH_003, VEH_004, WPN_005 · video8s · 0:16–0:24
[ACTION-VI] 2-BEAT: (a) 0:16–0:20 wide: hai xe tải K511 và K151 đang cháy trong khe thung lũng, lửa cam soi vách đá, lính là bóng đen đi ngang; (b) 0:20–0:24 xạ thủ PZF quỳ cách 천둥 2 (đã rút cạn dầu, cửa đuôi mở) 40 m, ống phóng trên vai; 오태민 đứng sau giơ tay — hạ tay. Chớp lửa đuôi ống.
[SOUND] lửa cháy, rồi tiếng phóng PZF "펑" khô, tiếng nổ dội vách; giọng 박기철 off-screen, khàn.
박기철: 두 발…

### SC_004 · LOC_003_CHEONDUNG_BASE · CHAR_003 · VEH_002 (천둥 2 cháy, 천둥 3), PROP_023 · video8s · 0:24–0:32
[ACTION-VI] Tiền cảnh: 천둥 2 bùng lửa, tiếng đạn 40mm nổ lốp bốp trong thân xe, một tia lửa văng cao. Hậu cảnh gần máy: 박기철 quay lưng với đám cháy, tay cầm cờ lê tháo hai bu-lông biển tên thép nhỏ trên hông 천둥 3 (biển sơn olive, số "3" trắng trầy) — bu-lông cuối rơi, ông nhét biển vào ba lô, không ngoảnh lại.
[SOUND] 40mm nổ dây chuyền ngắt quãng, cờ lê kêu, lửa.

### SC_005 · LOC_003_CHEONDUNG_BASE · CHAR_001 · VEH_002 (천둥 3) · video8s · 0:32–0:40
[ACTION-VI] 한승우 đứng trước mũi 천둥 3 — xe còn nguyên, lưới ngụy trang đã gỡ, bánh chịu nặng thứ ba bên phải có chốt sắt thô của 을보; trong tay ông một lựu đạn nhiệt nhôm, ngón cái đặt trên chốt; áo choàng vải gai nâu Goguryeo trùm ngoài giáp (고정수 tặng). Lửa cam từ 천둥 2 hắt lên nửa mặt. Máy đẩy chậm.
[SOUND] lửa, 40mm nổ thưa dần, gió.
N: 612년 6월. 요동성 동쪽 골짜기였습니다. 석 달 만에 처음으로, 이 부대는 적이 아니라 자기 것을 태우고 있었습니다.

### SC_006 · LOC_003_CHEONDUNG_BASE · CHAR_002 · VEH_002 (천둥 3) · video8s · 0:40–0:48
[ACTION-VI] 오태민 bước tới cạnh 한승우, kính bảo hộ trên mũ ám khói, nhìn 천둥 3 rồi nhìn quả lựu đạn trong tay chỉ huy. Giọng thấp, không phải cãi — là hỏi thật.
[SOUND] lửa, bước chân trên đá.
N: 판처파우스트 두 발이 방금 아군 장갑차를 뚫었습니다. 남은 것은 열 발이었습니다. 적을 향해 쓸 열 발이었습니다.
오태민: 정말 버립니까?

### SC_007 · LOC_003_CHEONDUNG_BASE (sườn núi phía tây, đêm) · CHAR_006 · EQP_001, EQP_002, VEH_206 (xa — đuốc) · video8s · 0:48–0:56
[ACTION-VI] 백성민 nằm sấp trên gờ đá cao trên thung lũng, kính đêm gạt lên vì ánh lửa quá chói; nhìn bằng mắt thường về phía tây: trên đường mòn núi, một chuỗi đuốc cam đang bò xuống — dài, không đếm được. Ông bấm radio, giọng phẳng.
[SOUND] PTT, gió trên cao, lửa xa dưới thung.
N: 탁발흠은 이틀 전 산으로 꺾어 들어갔습니다. 대군이 아니라 이 부대를 따라왔습니다.
백성민: 지휘, 여기는 수색. 산길에 횃불. 선비 기병. 열 분 안에 옵니다.

### SC_008 · LOC_003_CHEONDUNG_BASE · CHAR_001 · VEH_002 (천둥 3) · video8s · 0:56–1:04
[ACTION-VI] 한승우 nhìn 천둥 3 một nhịp dài — nhìn xuống quả lựu đạn — ngón cái rời chốt. Ông quay đi, nói một từ, nhét lựu đạn vào túi ngực áo choàng. Sau lưng ông, lính bắt đầu chạy về phía K2.
[SOUND] chốt lựu đạn không rút; giày chạy; lửa.
N: 태우는 데도 시간이 필요했습니다. 열 분은 그 시간이 아니었습니다. 수류탄은 주머니로 돌아갔습니다. 그 수류탄은 이 이야기의 끝까지 그 주머니에 있을 것이었습니다.
한승우: 출발.

### SC_009 · LOC_001_YOHA (đồng bằng phía đông 요동성, aerial đêm) · — · WPN_201, PROP_021 · still_kenburns · 1:04–1:14
[ACTION-VI] Ảnh aerial đêm rất cao: đồng bằng đen, một dải lửa trại kéo dài từ chân trời này sang chân trời kia như dòng sông lửa — 9 quân đoàn Tùy đang trên đường đông; cờ đỏ chỉ là chấm. Ken-burns kéo ra rất chậm.
[SOUND] trống Tùy rất xa, gió trên cao.
N: 같은 밤, 동쪽 벌판. 수나라 별동대 아홉 군, 30만 5천 명이 압록수로 향했습니다. 병사 한 명당 백 일치 군량. 무게 세 섬. 사람이 질 수 있는 무게가 아니었습니다.

### SC_010 · LOC_003_CHEONDUNG_BASE (cửa thung, đêm) · đại đội, CHAR_106, CHAR_107 · VEH_001, VEH_101, VEH_206 (xa) · video8s · 1:14–1:22
[ACTION-VI] 2-BEAT: (a) 1:14–1:18 K2 bò ra khỏi thung lũng, can dầu và một phuy 200 L buộc dây trên đuôi tháp, cành thông phủ nóc; hàng lính đi bộ hai bên, 을보 chống gậy, 아리 quàng khăn olive nắm tay áo ông; kỵ Goguryeo của 해모루 chờ ở cửa thung; (b) 1:18–1:22 cận gót người cuối hàng: hai mũi tên từ bóng tối sườn tây cắm "픽, 픽" vào bùn; anh ta quay lại bắn một loạt ngắn lên sườn núi rồi chạy tiếp.
[SOUND] xích K2, tên cắm bùn, K2C1 loạt ngắn, ngựa hí xa.
N: 수레 일곱 대로 왔습니다. 한 대가 떠났습니다. 나머지는 골짜기에 남았습니다. 사람은 둘이 더 따라왔습니다. 대장장이와 그 손녀였습니다.

### SC_011 · LOC_003_CHEONDUNG_BASE (bãi xe, đêm) · — · VEH_002 (천둥 3 nguyên; 천둥 2 cháy) · still_kenburns · 1:22–1:30
[ACTION-VI] Ảnh: 천둥 3 đứng một mình dưới tán sồi, cửa đuôi mở, ghế trống, giáp ướt phản chiếu lửa cam từ xác 천둥 2 cháy phía sau; hạt mưa đầu tiên lấm tấm trên nóc; trên hông xe, hai lỗ bu-lông trống nơi biển tên từng ở. Ken-burns đẩy chậm vào hai lỗ bu-lông.
[SOUND] lửa xa, mưa bắt đầu lộp độp trên thép.
N: 천둥 3호는 불타지 않았습니다.

[Kết thúc Phần 1]

## [Phần 2] 밥을 묻는 군대 — 「밥을 묻는 군대」 / Họ đang ở đâu  (1:30–4:30)
> Tóm tắt VI: Ngày D2. Aerial split: đồng bằng — 30만 5천 đen kịt; núi — 94 người + 을보/아리 đi bộ, 300 kỵ 해모루, xe bò chở K6/cối/đạn, K2 bò sau. Narrator: 9 đạo quân, mỗi lính 100 ngày lương, lệnh "vứt lương = chém". 서아 băng chân phồng rộp. 태오 đọc 4 câu thơ thuộc lòng từ kỳ thi; 아리 hỏi nghĩa; "나중에 알게 돼"; 한승우 nghe, không nói. Mini-combat: kỵ Tùy cánh sườn thấy bụi K2 — 30 kỵ 해모루 chặn trong khe; 오태민 bị cấm bắn lần 1. Đêm D2: từ sườn núi, ống nhòm thấy hàng nghìn lính Tùy đào dưới lều — 백성민: "저건 참호가 아닙니다. 밥을 묻고 있습니다." [史]
> Chức năng: DISCOVERY · Tài nguyên: giày/chân (400 km) · Enemy: điểm yếu của 30만 là bụng · Open loop: "그들은 백 일치 쌀을 땅에 묻었습니다. 아직 압록수도 건너기 전이었습니다."

### SC_012 · LOC_008_GOGURYEO_VILLAGE (dãy núi phía nam đồng bằng, aerial ngày) · — · VEH_001, VEH_101, WPN_201 · still_kenburns · 1:30–1:42
[ACTION-VI] Ảnh aerial rất cao, ngày xám mưa phùn: bên trái khung, đồng bằng — một cột đen khổng lồ của quân Tùy chảy về đông, không thấy đầu, không thấy đuôi; bên phải, dãy núi xanh — một sợi chỉ nhỏ trên đường núi: người đi bộ, kỵ binh, mấy xe bò, và một chấm vuông sẫm ở cuối là K2. Giữa hai cột là 20리 đồi thấp. Ken-burns trượt từ cột lớn sang sợi chỉ nhỏ.
[SOUND] gió trên cao, xa xa trống Tùy.
N: 이튿날 낮. 두 줄이 나란히 동쪽으로 갔습니다. 벌판에는 30만 5천 명. 산에는 아흔네 명과 기병 삼백. 두 줄 사이는 이십 리였습니다. 서로 보이지 않는 거리였고, 서로 잊을 수 없는 거리였습니다.

### SC_013 · LOC_001_YOHA (đường quân Tùy, đồng bằng) · — · WPN_201, PROP_021 · still_kenburns · 1:42–1:54
[ACTION-VI] Ảnh: đường lớn đồng bằng lầy mưa, hàng cờ đỏ-vàng của từng đạo quân nối nhau xa dần; lính Tùy cúi gập dưới bao gai, giáo, lều cuộn; bùn đến bắp chân. Ken-burns trượt ngang theo hàng cờ.
[SOUND] chân bùn, cờ ướt đập, trống.
N: 아홉 군이었습니다. 우문술의 부여도군, 우중문의 낙랑도군, 신세웅의 현도도군. 그 밖에 여섯 군이 더 있었습니다. 목표는 하나, 평양이었습니다. 요동성은 뒤에 두고 가는 것이었습니다.

### SC_014 · LOC_001_YOHA (đường quân Tùy) · 수 병사 · WPN_201, PROP_022 · video8s · 1:54–2:02
[ACTION-VI] Cận một lính Tùy trẻ: bao lương gai buộc chéo ngực, giáp da, giáo, lều cuộn, khiên — tổng cộng cao hơn đầu; anh ta trượt chân trong bùn, quỳ xuống, đứng dậy không nổi; lính sau lưng đẩy qua. Một sĩ quan cưỡi ngựa quát, roi giơ lên.
[SOUND] bùn, thở dốc, roi, tiếng quát.
N: 한 사람 몫이 세 섬이었습니다. 쌀과 갑옷, 창, 천막, 옷. 황제의 명령은 하나. 군량을 버리는 자는 목을 벤다. 사람들은 다른 방법을 찾았습니다.

### SC_015 · LOC_008_GOGURYEO_VILLAGE (đường núi, ngày mưa phùn) · đại đội, CHAR_106, CHAR_107 · VEH_001, VEH_101 · video8s · 2:02–2:10
[ACTION-VI] Tracking ngược trước đoàn: lính Hàn đi bộ hai hàng, áo sẫm nước, bùn tới gối, râu ba ngày; hai lính băng kín tay (bỏng 2화) đi giữa hàng, súng do người khác vác; 을보 chống gậy, cuộn dụng cụ trên lưng; 아리 khăn olive ướt, bím tóc dính má; sau họ hai xe bò chở hộp đạn xanh olive, hai khẩu K6, ống cối; kỵ Goguryeo đi bộ dắt ngựa bên cạnh; K2 cuối cùng bò chậm, xích nghiền đá.
[SOUND] mưa, giày lội bùn, bánh xe bò kẽo kẹt, xích K2 xa.
N: 산길은 수레가 갈 수 있는 유일한 길이었습니다. 하루에 삼십 리. 벌판의 대군은 그 두 배를 갔습니다. 짐은 무거웠고, 매는 더 무서웠습니다.

### SC_016 · LOC_008_GOGURYEO_VILLAGE (bên đường, gốc thông) · CHAR_004, 병사 · PROP_009 · video8s · 2:10–2:18
[ACTION-VI] Nghỉ ngắn: 서아 quỳ, kéo giày một lính ra — gót chân phồng rộp vỡ, máu loãng; cô cắt băng, dán, nói nhanh; lính nhăn mặt; túi vải thảo dược nhỏ buộc thắt lưng cô lắc theo tay.
[SOUND] mưa trên lá, kéo cắt băng.
N: 사백 킬로였습니다. 전차에게는 기름의 문제였습니다. 사람에게는 발의 문제였습니다.
윤서아: 사백 킬로를 이 발로 갑니다. 물집은 지금 잡아야 합니다.

### SC_017 · LOC_008_GOGURYEO_VILLAGE (đường núi) · CHAR_005, CHAR_107 · UAV_001 (hộp), PROP_014 (đọc thuộc) · video8s · 2:18–2:26
[ACTION-VI] 태오 đi cạnh 아리, hộp drone cứng trên lưng, controller trên ngực; cậu đọc bốn câu như đọc bảng cửu chương, mắt nhìn đường; 아리 ngước nhìn cậu. (Editor: subtitle 4 câu chữ Hán 神策究天文 / 妙算窮地理 / 戰勝功既高 / 知足願云止 + âm Hàn khi cậu đọc.)
[SOUND] mưa, bước chân.
N: 장태오, 스물한 살. 삼 년 전에 대학 시험을 봤습니다. 시험에 나온 시 한 수를 아직 외우고 있었습니다.
장태오: 신책구천문, 묘산궁지리, 전승공기고, 지족원운지.

### SC_018 · LOC_008_GOGURYEO_VILLAGE (đường núi) · CHAR_107, CHAR_005 · — · video8s · 2:26–2:34
[ACTION-VI] 아리 nghiêng đầu, hỏi bằng giọng trẻ con tò mò; 태오 nhìn xuống cô, hơi lúng túng, nhìn về phía trước — nơi 한승우 đang đi cách hai hàng.
[SOUND] mưa, bước chân.
N: 그 시는 아직 쓰이지 않은 시였습니다. 이 땅의 장군이 한 달 뒤 적장에게 보낼 시였습니다. 소년은 결말을 알았습니다.
아리: 그게 무슨 말이에요, 오라버니?

### SC_019 · LOC_008_GOGURYEO_VILLAGE (đường núi) · CHAR_005, CHAR_001 · — · video8s · 2:34–2:42
[ACTION-VI] 태오 trả lời ngắn, cười gượng; máy rack focus qua vai cậu lên 한승우 đi phía trước — ông nghe được, bước không đổi, không quay lại; bàn tay ông chạm túi ngực nơi có quả lựu đạn.
[SOUND] mưa, bước chân, xích K2 xa.
N: 한승우도 들었습니다. 그는 말하지 않았습니다. 이 싸움은 역사가 이미 이겼다. 문제는 그 역사에 아흔네 명의 자리가 없다는 것이었습니다.
장태오: 나중에 알게 돼.

### SC_020 · LOC_008_GOGURYEO_VILLAGE (gờ đồi phía bắc đường, ngày) · CHAR_001, CHAR_002 · PROP_006, VEH_101, WPN_201 (kỵ Tùy) · video8s · 2:42–2:50
[ACTION-VI] 한승우 dừng trên gờ đồi, ống nhòm; POV ống nhòm: dưới sườn đồi thấp cách 2 km, một toán kỵ binh Tùy ~40 (giáp sắt, cờ đỏ nhỏ — không phải Tiên Ti) đang dừng ngựa, một tên chỉ tay về phía đám bụi xích K2; từ khe bên trái, 30 kỵ Goguryeo của 해모루 phóng ra cắt ngang. 오태민 bên cạnh giương súng lên vai.
[SOUND] gió, vó ngựa xa, ống nhòm.
N: 벌판의 대군에게도 눈이 있었습니다. 옆구리를 도는 기병이었습니다. 해모루는 그것을 알았습니다. 그래서 삼십 기를 언덕 사이에 두었습니다.

### SC_021 · LOC_008_GOGURYEO_VILLAGE (khe đồi, ngày) · CHAR_105, kỵ Goguryeo, kỵ Tùy · VEH_101, WPN_101 · video8s · 2:50–2:58
[ACTION-VI] Trong khe: kỵ Goguryeo giáp lamellar lao vào sườn toán kỵ Tùy — cung bắn khi phi, hai kỵ Tùy ngã ngựa, đao chạm giáp; toán Tùy quay đầu chạy về đồng bằng, bỏ lại ngựa mất chủ; 해모루 dẫn đầu, tù và ở hông, không đuổi quá gờ đồi. Wide, không cận thương vong.
[SOUND] vó ngựa dồn, dây cung, đao chạm sắt, ngựa hí.
N: 싸움은 짧았습니다. 산 쪽 언덕은 고구려 기병의 땅이었습니다. 수나라 기병이 본 것은 먼지뿐이었습니다. 먼지는 보고할 것이 못 되었습니다.

### SC_022 · LOC_008_GOGURYEO_VILLAGE (gờ đồi) · CHAR_002, CHAR_001 · WPN_001 · video8s · 2:58–3:06
[ACTION-VI] 오태민 vẫn ngắm qua kính súng về phía khe; 한승우 đặt tay lên nòng, ấn xuống. 해모루 phi lên gờ, vệt máu trên lưỡi đao, gật một cái, quay ngựa đi không nói.
[SOUND] gió, vó ngựa tới gần rồi đi.
N: 총소리는 이십 리를 갑니다. 화살 소리는 백 걸음을 갑니다. 오태민이 첫 번째로 금지당한 날이었습니다.
한승우: 쏘지 마. 해 말객이 막는다.

### SC_023 · LOC_008_GOGURYEO_VILLAGE (sườn núi nhìn xuống đồng bằng, đêm D2) · CHAR_001, CHAR_006, CHAR_105 · PROP_006 · video8s · 3:06–3:14
[ACTION-VI] Đêm, mưa tạnh, mây thấp. Ba người nằm sấp trên gờ đá: 한승우 với ống nhòm, 백성민 với kính đêm (bật), 해모루 mắt thường; dưới xa, đồng bằng đầy đốm lửa trại Tùy đến chân trời — hàng nghìn lều xám ướt.
[SOUND] gió, trống đêm Tùy rất xa, tiếng kính đêm rít nhẹ.
N: 그날 밤 부대는 산등성이에 멈췄습니다. 드론은 띄우지 않았습니다. 드론 한 번은 기름이었습니다. 이십 리 아래, 30만의 불이 있었습니다.

### SC_024 · LOC_001_YOHA (trại Tùy, đêm — POV kính đêm) · 수 병사 · PROP_022, EQP_001 · video8s · 3:14–3:22
[ACTION-VI] POV kính đêm xanh lục: giữa các hàng lều, những bóng người cúi khom — không phải đứng gác — đang đào bằng xẻng gỗ và tay; bao gai được hạ xuống hố nông ngay dưới mép lều; đất lấp lại; hai người kéo tấm lều che lên trên. Hàng chục cụm như vậy trong khung.
[SOUND] kính đêm rít, gió; xa xa tiếng xẻng nhỏ.
N: 천막 밑에서 사람들이 움직였습니다. 보초가 아니었습니다. 보초는 서 있습니다. 이들은 엎드려 있었습니다.

### SC_025 · LOC_008_GOGURYEO_VILLAGE (gờ đá) · CHAR_006 · EQP_001 · video8s · 3:22–3:30
[ACTION-VI] 백성민 hạ kính đêm, nhìn 한승우; giọng điện tín nhưng có một nhịp ngừng ở giữa — hiếm với ông.
[SOUND] gió, kính đêm tắt "틱".
백성민: 저건 참호가 아닙니다. 밥을 묻고 있습니다.

### SC_026 · LOC_008_GOGURYEO_VILLAGE (gờ đá) · CHAR_105, CHAR_001 · — · video8s · 3:30–3:38
[ACTION-VI] 해모루 quay hẳn người sang 백성민, mặt không tin; rồi nhìn xuống đồng bằng, không cần kính cũng thấy các đốm đen cúi khom; ông nói chậm, từng chữ.
[SOUND] gió.
N: 해모루는 고구려 사람이었습니다. 고구려에서 쌀은 성 하나와 같았습니다. 쌀을 묻는다는 말은 그의 말에 없는 말이었습니다.
해모루: 백 일치 쌀을… 땅에 묻는단 말이오?

### SC_027 · LOC_001_YOHA (trại Tùy, mép lều — cận) · — · PROP_022 · still_kenburns · 3:38–3:48
[ACTION-VI] Ảnh cận: hố nông đất ướt cạnh chân lều gai xám, bao lương ~40 kg buộc miệng nằm nửa chìm, kê vàng vãi trên bùn, một xẻng gỗ, dấu chân đầy nước mưa; góc khung: bàn chân trần lính Tùy nứt nẻ. Ken-burns đẩy chậm vào bao gai.
[SOUND] mưa nhỏ, xa xa tiếng ai ho.
N: 황제는 군량을 버리는 자를 베라 했습니다. 그래서 병사들은 버리지 않았습니다. 묻었습니다. 벤 것은 사람이 아니라 백 일이었습니다. 이 일은 수나라 역사책에 그대로 적혀 있습니다.

### SC_028 · LOC_001_YOHA (trại Tùy, hàng lều, đêm) · 수 장교, 수 병사 · PROP_016, PROP_022 · video8s · 3:48–3:56
[ACTION-VI] Một sĩ quan Tùy cầm đèn lồng đi dọc hàng lều; lính đang đào dừng tay, phủ rơm lên hố, đứng nghiêm; sĩ quan nhìn xuống rơm, nhìn lính, nâng đèn — rồi đi tiếp không nói. Tracking chậm theo đèn.
[SOUND] mưa, đèn lồng cọt kẹt, thở.
N: 장교들은 보았습니다. 보지 않은 척했습니다. 벨 목은 하나였고, 묻는 손은 만 개였습니다. 규율도 그날 밤 천막 밑에 묻혔습니다.

### SC_029 · LOC_008_GOGURYEO_VILLAGE (gờ đá) · CHAR_001 · PROP_006 · video8s · 3:56–4:04
[ACTION-VI] 한승우 hạ ống nhòm, nhìn vào khoảng tối trước mặt; máy đẩy chậm vào mặt ông; sau lưng, 해모루 vẫn nhìn xuống đồng bằng.
[SOUND] gió, trống xa.
N: 요동성에서 을지문덕이 한 말이 있었습니다. 저들은 오래 못 버티오. 한승우는 갑옷 이야기인 줄 알았습니다. 배 이야기였습니다.

### SC_030 · LOC_008_GOGURYEO_VILLAGE (gờ đá, phía sau) · CHAR_002, CHAR_001 · WPN_002 (xa, xe bò) · video8s · 4:04–4:12
[ACTION-VI] 오태민 bò lên gờ, đã nhìn thấy; ông chỉ tay xuống đồng bằng rồi chỉ về phía xe bò chở ống cối trong bóng tối sau lưng — ý rõ ràng không cần lời; rồi nói.
[SOUND] gió, đá lăn nhỏ dưới khuỷu tay.
N: 오태민에게 이것은 기회였습니다. 밥을 버리는 군대는 반은 진 군대였습니다. 마저 치는 것이 병법이었습니다. 그의 병법으로는.
오태민: 지금 쳐야 합니다. 밥을 버리는 놈들입니다.

### SC_031 · LOC_008_GOGURYEO_VILLAGE (gờ đá) · CHAR_001 · — · video8s · 4:12–4:20
[ACTION-VI] 한승우 không nhìn 오태민; nhìn xuống đồng bằng, nói thấp; rồi trượt xuống khỏi gờ đá về phía trại. 해모루 đưa mắt theo ông — đang đánh giá.
[SOUND] gió, đá.
N: 한승우의 병법은 달랐습니다. 아직 이름이 없는 병법이었습니다. 이름은 압록수에서 을지문덕이 붙여줄 것이었습니다.
한승우: 안 친다. 우리는 압록수로 간다.

### SC_032 · LOC_001_YOHA (aerial đêm, đồng bằng + dãy núi) · — · WPN_201 · still_kenburns · 4:20–4:30
[ACTION-VI] Ảnh aerial đêm: biển lửa trại Tùy đến chân trời; sát mép khung phải, dãy núi đen câm, không một đốm lửa — nơi đại đội đang nằm. Ken-burns kéo ra chậm.
[SOUND] trống xa, gió.
N: 그들은 백 일치 쌀을 땅에 묻었습니다. 아직 압록수도 건너기 전이었습니다.

[Kết thúc Phần 2]

## [Phần 3] 드론 한 번, 전차 600미터 — 「드론 한 번, 전차 600미터」 / Kiểm kê  (4:30–7:00)
> Tóm tắt VI: Đêm D3, trạm dừng trong khe núi. 박기철 đọc que dầu: "산길로 400km, 딱." Drone: pin chiếc thứ hai phồng vì sức nóng đêm cháy — chết hẳn → còn 1. Sạc chỉ còn từ APU của K2: "드론 한 번 충전이 전차 600미터입니다." Kính đêm 12, radio — tất cả nối vào một bình dầu. Lương: kê 해모루 cấp; "입이 둘 더 늘었습니다" — 을보 đáp trả. Kỵ sứ Goguryeo mang lệnh 을지문덕: "hạ nhãn" phải ở 압록수 trong 5 ngày → 60 km/ngày → lính Hàn cưỡi ngựa Goguryeo, kỵ binh Goguryeo đi bộ. Mini: lính Tùy đào ngũ lạc vào trại — gầy, nhai vỏ cây. 오태민 lên ngựa vụng — 해모루 bật cười. 백성민 làm quen ngựa (1 shot). K2 thành "con la" chở đạn + 을보/아리.
> Chức năng: DECISION · Tài nguyên nói thành lời: "400km 딱" · "드론 하나" · "600미터" · "닷새" · "입이 둘" · Open loop: "닷새. 을지문덕은 압록수에서 무엇을 하려는지 말하지 않았습니다." → [MID-ROLL 1 · 7:00]

### SC_033 · LOC_003_CHEONDUNG_BASE (Dạng B — khe núi có suối, đêm D3, mưa) · — · VEH_001 · still_kenburns · 4:30–4:40
[ACTION-VI] Ảnh: K2 dưới cành thông chặt phủ nóc trong khe đá hẹp có suối, phuy 200 L và can dầu buộc đuôi tháp, một lều chỉ huy olive + vài poncho căng giữa thân thông, đèn đỏ mờ trong lều, mưa rả rích, sương chảy qua khe. Ken-burns đẩy chậm vào đèn đỏ.
[SOUND] mưa trên poncho, suối, APU rì rì rất nhỏ.
N: 사흘째 밤. 골짜기에서 떠난 뒤로 두 밤을 자지 못했습니다. 기지는 이제 움직이는 것이었습니다. 천막 하나, 전차 한 대.

### SC_034 · LOC_003_CHEONDUNG_BASE (đuôi K2) · CHAR_003 · VEH_001, PROP_007 · video8s · 4:40–4:48
[ACTION-VI] 박기철 rút que đo dầu dài khỏi cổ bình K2, soi đèn pin che tay lên vạch ướt; bên cạnh, bảng gỗ ghi số bằng bút dạ treo ở giá đồ; ông gõ que lên bảng, nói với 한승우 đứng cạnh (chỉ thấy vai áo choàng).
[SOUND] mưa, que đo kêu, đèn pin bật.
N: 장갑차 둘, 트럭 둘, 지휘차 하나. 다섯 대의 기름이 한 대에 들어갔습니다. 그 숫자가 이 부대의 남은 길이었습니다.
박기철: 산길로 400km, 딱.

### SC_035 · LOC_003_CHEONDUNG_BASE (dưới poncho) · CHAR_005 · UAV_001 · video8s · 4:48–4:56
[ACTION-VI] 태오 mở hộp cứng olive: hai drone xám; cậu nhấc pin của chiếc thứ hai — vỏ pin phồng cong như gối, dây chảy; cậu ấn nút — không đèn; đặt xuống rất nhẹ như đặt vật đã chết.
[SOUND] mưa trên poncho, nút bấm không kêu.
N: 두 번째 기체의 전지는 그날 밤 불 옆에 있었습니다. 열은 전지를 부풀렸습니다. 드론 넷으로 왔습니다. 이제 하나였습니다.
장태오: 배터리가 부풀었습니다. 죽었습니다.

### SC_036 · LOC_003_CHEONDUNG_BASE (đuôi K2) · CHAR_003, CHAR_005 · VEH_001, UAV_001 · video8s · 4:56–5:04
[ACTION-VI] 박기철 cắm dây sạc từ ổ điện phụ trên đuôi K2 vào pin drone cuối; đèn sạc đỏ sáng; APU sau tháp rít lên một tông; ông nhìn 태오, giơ ngón tay lên như thầy giáo.
[SOUND] APU tăng tông, đèn sạc "띡".
N: 지휘차는 골짜기에서 탔습니다. 발전기도 같이 탔습니다. 이제 전기는 전차에서만 나왔습니다. 전차의 보조동력은 기름을 먹었습니다.
박기철: 드론 한 번 충전이 전차 600미터입니다.

### SC_037 · LOC_003_CHEONDUNG_BASE (đuôi K2) · CHAR_003 · EQP_001, EQP_002, VEH_001 · video8s · 5:04–5:12
[ACTION-VI] Cận: trên tấm bạt dưới đuôi K2, 12 kính đêm xếp hàng, 4 radio cầm tay, pin AA, tablet — tất cả nối dây về một ổ chia trên đuôi xe như con bạch tuộc; bàn tay băng của 박기철 gõ lên ổ chia.
[SOUND] mưa, APU.
N: 야시경 열둘. 무전기. 태블릿. 전부 한 줄로 이어져 있었습니다. 그 줄의 끝은 기름통이었습니다.
박기철: 전부 이 한 통에서 나갑니다.

### SC_038 · LOC_003_CHEONDUNG_BASE (bếp đá, dưới poncho) · CHAR_106, CHAR_107, CHAR_003 · — · video8s · 5:12–5:20
[ACTION-VI] 을보 và 아리 ngồi bên bếp đá, bát cháo kê Goguryeo bốc khói; lính Hàn ăn cùng bằng ca sắt; 박기철 đứng với bảng số, nhìn hai ông cháu, nói không ác ý — chỉ là người đếm.
[SOUND] mưa, thìa chạm bát, lửa nhỏ.
N: 전투식량은 요동성에서 끝났습니다. 밥은 해모루의 기병이 가져온 조였습니다. 조는 셀 수 있었습니다. 입도 셀 수 있었습니다.
박기철: 입이 둘 더 늘었습니다.

### SC_039 · LOC_003_CHEONDUNG_BASE (bếp đá) · CHAR_106 · VEH_001 · video8s · 5:20–5:28
[ACTION-VI] 을보 không ngẩng lên, húp cháo xong mới nói; rồi ông đưa tay gõ hai lần lên váy xích K2 sau lưng như gõ lên vai bò; mắt trái nheo. 아리 cười khúc khích.
[SOUND] gõ thép, lửa.
N: 골짜기에 남은 장갑차의 바퀴에 쇠못을 박은 사람이 을보였습니다. 그 장갑차가 누구 손에 갈지, 그는 아직 몰랐습니다.
을보: 쇠쟁이, 이 쇠는 내가 봐야 굴러가.

### SC_040 · LOC_003_CHEONDUNG_BASE (cửa khe, đêm) · CHAR_105, 고구려 전령 · VEH_101 · video8s · 5:28–5:36
[ACTION-VI] Một kỵ sĩ Goguryeo ướt sũng phi vào khe, xuống ngựa, quỳ một gối, dâng thẻ tre buộc dây; 해모루 mở, đọc dưới đèn lồng; mặt ông thay đổi.
[SOUND] vó ngựa, thẻ tre lách cách, mưa.
N: 을지문덕은 사흘 전에 앞서 떠났습니다. 기병 오백과 함께 더 빠른 길로 갔습니다. 편지는 짧았습니다. 그의 편지는 늘 짧았습니다.

### SC_041 · LOC_003_CHEONDUNG_BASE (đuôi K2) · CHAR_105, CHAR_001 · — · video8s · 5:36–5:44
[ACTION-VI] 해모루 đến trước 한승우, thẻ tre trong tay, nói thẳng; ánh đèn đỏ lều hắt lên chỏm lông trắng ướt trên mũ.
[SOUND] mưa.
N: 하늘 눈. 해모루는 드론을 그렇게 불렀습니다. 을지문덕은 그 눈을 압록수에서 쓰려 했습니다.
해모루: 하늘 눈은 닷새 안에 압록수에 있어야 하오.

### SC_042 · LOC_003_CHEONDUNG_BASE (lều chỉ huy, đèn đỏ) · CHAR_001 · PROP_001 · video8s · 5:44–5:52
[ACTION-VI] Trong lều: 한승우 cúi trên bản đồ giấy quân sự, ngón tay đo bằng dây dù từ điểm đánh dấu tới sông Áp Lục; ông nhẩm, gõ ngón tay xuống bàn thép ba lần.
[SOUND] mưa trên vải lều, giấy.
N: 압록수까지 삼백 킬로. 닷새면 하루 육십 킬로였습니다. 골짜기에서 여기까지 삼십 킬로를 사흘에 왔습니다.
한승우: 하루 육십 킬로. 걸어선 못 간다.

### SC_043 · LOC_003_CHEONDUNG_BASE (cửa khe) · CHAR_105, CHAR_001 · VEH_101 · video8s · 5:52–6:00
[ACTION-VI] 해모루 đứng ở cửa khe, sau lưng là hàng ngựa hạt dẻ của kỵ binh đang được dắt tới, yên còn ướt; ông nói với 한승우 không do dự — như đã quyết trước khi hỏi.
[SOUND] ngựa thở, dây cương.
N: 고구려 기병은 말에서 내리지 않는 사람들이었습니다. 그날 밤 해모루는 내렸습니다. 말 삼백이 아흔네 명에게 갔습니다.
해모루: 말은 천둥 군사가 타시오. 우리는 걷겠소.

### SC_044 · LOC_003_CHEONDUNG_BASE (rìa trại, đêm — POV kính đêm) · CHAR_006, 수 낙오병 · EQP_001, WPN_001 · video8s · 6:00–6:08
[ACTION-VI] POV kính đêm xanh: một bóng người loạng choạng bước qua suối vào khe, không giáp, tay không; cắt sang: 백성민 từ sau gốc thông lao ra, quật ngã, đầu gối đè lưng, dao kề cổ; lính gác thứ hai chĩa súng. Bóng người không chống cự — chỉ khóc.
[SOUND] nước suối văng, thân người ngã, dao rút, tiếng khóc nghẹn.
N: 자정 무렵 개울에서 사람이 왔습니다. 적이 아니었습니다. 적이었던 사람이었습니다.

### SC_045 · LOC_003_CHEONDUNG_BASE (bếp đá) · 수 낙오병, CHAR_105, CHAR_001 · — · video8s · 6:08–6:16
[ACTION-VI] Lính Tùy đào ngũ quỳ bên bếp: má hóp, môi nứt, áo vải rách, đang nhai một mẩu vỏ cây; 해모루 ngồi xổm hỏi bằng Hán ngữ (quy ước: trên màn hình chỉ nghe anh ta lí nhí, không rõ lời), rồi quay sang 한승우 dịch. 서아 đưa ca cháo — anh ta nhìn ca cháo như nhìn vàng.
[SOUND] lửa, nhai vỏ cây, lí nhí.
N: 사흘 전에 군량을 묻고, 이틀 전에 대열에서 빠졌습니다. 밥 냄새가 나는 쪽으로 왔을 뿐이었습니다.
해모루: 군량을 묻고 도망친 자요. 이런 자가 천은 되오.

### SC_046 · LOC_003_CHEONDUNG_BASE (cửa khe, rạng sáng D4) · CHAR_002, CHAR_105 · VEH_101 · video8s · 6:16–6:24
[ACTION-VI] 오태민 đặt chân vào bàn đạp da, nhảy lên — ngựa hạt dẻ xoay ngang, ông trượt xuống, thử lại, lên được nhưng ngồi lệch, súng vướng yên; 해모루 đứng cạnh giữ cương, bật cười thành tiếng — lần đầu tiên trong ba tập; kỵ binh quanh ông cũng cười.
[SOUND] ngựa hí, da yên kêu, tiếng cười.
N: 해모루가 소리 내어 웃었습니다. 말이 사람을 가르치는 데는 하루가 걸립니다. 그들에게는 하루가 없었습니다.

### SC_047 · LOC_003_CHEONDUNG_BASE (cửa khe, rạng sáng) · CHAR_006, CHAR_105 · VEH_101 · video8s · 6:24–6:32
[ACTION-VI] 백성민 đứng trước một con ngựa xám không yên, không nhìn thẳng vào mắt nó, đưa mu bàn tay cho nó ngửi, thổi nhẹ vào mũi nó; ngựa cúi đầu; ông vuốt cổ, nhảy lên lưng trần một động tác gọn. 해모루 ngừng cười, nhìn — gật một cái rất nhỏ.
[SOUND] ngựa thở phì, mưa nhỏ.
N: 백성민은 강원도 산골 사냥꾼의 아들이었습니다. 말은 그의 손을 알아보았습니다. 그날부터 해모루는 그를 이름으로 불렀습니다.

### SC_048 · LOC_003_CHEONDUNG_BASE (đuôi K2, rạng sáng) · CHAR_003, CHAR_106, CHAR_107 · VEH_001, WPN_004, WPN_002 · video8s · 6:32–6:40
[ACTION-VI] Đuôi K2: hộp đạn xanh olive và hai khẩu K6 buộc dây chằng trên lưới thoát khí, ống cối cột dọc giá đồ; 을보 và 아리 ngồi trên nóc buồng động cơ giữa can dầu, chân thò xuống; 박기철 siết dây chằng cuối, vỗ lên giáp xe.
[SOUND] dây chằng siết, xích K2 nổ máy ấm.
N: 소달구지는 하루 육십 킬로를 못 갑니다. 그래서 짐은 전차 등에 올라갔습니다. 55톤이 짐말이 되었습니다.
박기철: 전차가 노새가 됐습니다.

### SC_049 · LOC_008_GOGURYEO_VILLAGE (đường núi, ngày mưa — montage) · đại đội, CHAR_105 · VEH_101, VEH_001 · still_kenburns · 6:40–6:50
[ACTION-VI] Ảnh: đoàn lính Hàn cưỡi ngựa Goguryeo hai hàng trên đường núi mưa, áo choàng gai trùm giáp, súng vắt ngang yên; kỵ binh Goguryeo giáp lamellar đi bộ dắt ngựa dự bị bên cạnh; K2 chở đầy đồ bò ở giữa đoàn. Ken-burns trượt ngang theo đoàn.
[SOUND] vó ngựa, mưa, xích.
N: 닷새였습니다. 하루 육십 킬로. 밤에도 갔습니다. 고구려 기병이 자기 말을 남에게 내주고 걷는 것을, 이 땅의 역사는 본 적이 없었습니다.

### SC_050 · LOC_008_GOGURYEO_VILLAGE (đường núi, chiều mưa — montage) · — · VEH_001 · still_kenburns · 6:50–7:00
[ACTION-VI] Ảnh: khúc cua đường núi ướt, mây thấp phủ đỉnh, K2 là khối sẫm giữa hàng ngựa, bùn bắn lên nửa thân; xa phía đông-nam, một vệt xanh lục sẫm giữa hai dãy núi — sông Áp Lục lần đầu hé. Ken-burns đẩy chậm về vệt sông.
[SOUND] mưa, xích xa.
N: 닷새. 을지문덕은 압록수에서 무엇을 하려는지 말하지 않았습니다.

[MID-ROLL 1 · 7:00]

[Kết thúc Phần 3]

## [Phần 4] 거짓 항복 — 「거짓 항복」 / Cuộc chạm trán đầu tiên  (7:00–10:30)
> Tóm tắt VI: D9, 압록수. Đồi bờ nam trên bến vượt; 9 quân tập kết bờ bắc, lính chôn nốt lương còn lại bên bờ [史: chôn]. Drone cuối cất cánh (30 phút): thấy toán nhỏ dưới cờ trắng đi vào trại Tùy — 을지문덕 không giáp, áo lụa + 조우관, tay không; 해모루 đi cùng. Kế dự phòng: ông bị bắt → K2 4 viên vào cổng trại. Trong trại (P-11: 을지문덕 không nói — viết; 해모루 dịch thầm): 우중문 muốn bắt theo mật lệnh; 유사룡 can; 을지문덕 nhìn mặt lính, gầy, nhai vỏ cây. Được thả. 우중문 hối, sai kỵ sứ đuổi "더 할 말이 있소!" — ông không ngoảnh lại. 50 kỵ đuổi sát bến — 백성민 + K6: một loạt xuống mặt nước trước mũi ngựa; toán đuổi dừng; ông lội qua sông. K2 không bắn. Trên đồi: "저들은 굶고 있소. 굶는 군대는 이기게 두면 되오."
> Chức năng: THREAT + CONTACT · Tài nguyên: drone pin 30→14 · K6 −60 · Enemy: Tùy nhận ra 뇌군 ở bờ nam qua "sấm" (우중문 đã nghe ở 육합성 2화) — chưa biết ở đâu · Payoff 2화 "저들은 오래 못 버티오" · Open loop: "그는 적진에서 무기를 보지 않았습니다. 병사들의 얼굴을 봤습니다."

### SC_051 · LOC_005_AMNOK (aerial, sáng sương mưa) · — · WPN_201, PROP_021 · still_kenburns · 7:00–7:12
[ACTION-VI] Ảnh aerial: sông Áp Lục xanh lục sẫm chảy xiết giữa hai dãy núi đá xám phủ thông; bãi cuội rộng nơi nước cạn; bờ bắc — bãi bồi phủ kín lều Tùy xiêu vẹo, khói ướt, cờ đỏ; bờ nam — rừng thông dốc, không một bóng người. Mây thấp, mưa phùn. Ken-burns kéo ra rất chậm. Không thoại.
[SOUND] nước sông, mưa, trống Tùy mơ hồ bên kia.
N: 닷새 뒤. 압록수.

### SC_052 · LOC_005_AMNOK (đồi bờ nam, rạng sáng) · CHAR_105, CHAR_001 · VEH_101 · video8s · 7:12–7:20
[ACTION-VI] Rạng sáng trong rừng thông ướt: 해모루 đã cởi giáp, mặc áo vải dài nâu, không đao, không cung — chỉ radio chưa có (P6 mới nhận); ông nói với 한승우 đang đứng dưới tán cây; phía sau, một bóng người mảnh cao áo lụa đỏ nâu, 조우관 hai lông trắng, đang đợi ở mép rừng — 을지문덕, tay không, lưng quay lại máy.
[SOUND] mưa trên lá thông, nước sông xa.
N: 그날 아침 을지문덕은 갑옷을 벗었습니다. 비단옷과 조우관. 칼도 없었습니다. 항복할 생각은 없었습니다. 볼 생각이었습니다.
해모루: 장군께서 직접 가시오. 나도 가오.

### SC_053 · LOC_005_AMNOK (đồi bờ nam, mỏm đá) · CHAR_005 · UAV_001 · video8s · 7:20–7:28
[ACTION-VI] 태오 trên mỏm đá dưới tán thông, drone cuối cất cánh khỏi lòng bàn tay, biến vào mưa phùn; màn hình controller: pin 30; cậu nói với radio vai.
[SOUND] rotor nhỏ dần trong mưa, PTT.
N: 마지막 드론이었습니다. 전지 삼십 분. 이것이 을지문덕이 닷새를 달리게 한 이유였습니다. 하늘 눈은 강 건너를 봐야 했습니다.
장태오: 마지막 기체. 배터리 삼십 분.

### SC_054 · LOC_005_AMNOK (bờ bắc — màn hình drone) · 수 병사 · PROP_022, WPN_201 · video8s · 7:28–7:36
[ACTION-VI] Màn hình drone (góc cao, mưa lấm ống kính): bờ bắc — dọc mép trại, hàng trăm lính Tùy đào hố nông trong bùn, hạ bao gai xuống, lấp đất, dẫm lên; kê vàng vãi quanh miệng hố; phía sau, trại lều xiêu vẹo kéo dài đến khuất trong mưa. Ngón tay 태오 run trên cần.
[SOUND] rotor qua loa, mưa.
N: 압록수에 이르렀을 때, 백 일치 군량은 거의 남아 있지 않았습니다. 남은 것마저 강가에 묻었습니다. 강을 건너려면 몸이 가벼워야 했습니다.

### SC_055 · LOC_005_AMNOK (bến vượt — màn hình drone) · CHAR_101, CHAR_105 (trên màn hình), CHAR_005 · UAV_001 · video8s · 7:36–7:44
[ACTION-VI] Màn hình drone zoom: trên bãi cuội, một toán 6 người đi bộ về phía trại Tùy — dẫn đầu một người áo lụa đỏ nâu, 조우관, tay không; cạnh ông một người áo nâu (해모루) cầm cờ trắng trên sào tre; lính Tùy gác ở mép trại giương giáo rồi hạ. 태오 nhìn màn hình, thì thầm.
[SOUND] rotor qua loa, PTT.
N: 삼국사기는 이렇게 적었습니다. 을지문덕은 왕명을 받아 거짓 항복으로 적진에 들어가 허실을 보았다. 그날이 그날이었습니다.
장태오: 백기… 장군님입니다.

### SC_056 · LOC_005_AMNOK (đồi bờ nam, mỏm đá) · CHAR_001, CHAR_006, 소년 척후 · EQP_002, WPN_004, VEH_001 (xa) · video8s · 7:44–7:52
[ACTION-VI] Trên mỏm đá: 한승우 ống nhòm nhìn xuống bến; 백성민 nằm sau khẩu K6 trên giá ba chân, băng đạn nạp sẵn; 소년 척후 (17 tuổi, từ 1화, nay đi theo 해모루) ngồi xổm cạnh, cung trên đùi; sau lưng họ, K2 dưới tán thông, nòng hướng sông, máy tắt. 한승우 bấm radio.
[SOUND] mưa, PTT, băng K6 lách cách.
N: 계획은 하나였습니다. 장군이 붙잡히면 전차가 정문에 네 발. 한승우는 쓰고 싶지 않았습니다.
한승우: 천둥 1, 여기는 천둥 지휘. 장군이 잡히면 정문에 네 발.

### SC_057 · LOC_005_AMNOK (cổng trại Tùy, bờ bắc) · CHAR_101, CHAR_105, 수 병사 · WPN_201, PROP_021 · still_kenburns · 7:52–8:02
[ACTION-VI] Ảnh: lối đi bùn giữa hai hàng lính Tùy đứng dọc — giáp da rách, mặt hóp, mắt trũng, nhiều người tựa giáo cho khỏi ngã; giữa lối, 을지문덕 áo lụa đi chậm, hai tay buông, đầu hơi nghiêng nhìn từng mặt; 해모루 nửa bước sau, cờ trắng. Trung cảnh: chỉ 2–3 khuôn mặt lính gần ông nét, hàng sau mờ. Ken-burns đẩy chậm theo bước ông.
[SOUND] mưa, giáo cắm bùn, tiếng ho.
N: 그는 병영으로 걸어 들어갔습니다. 창을 세지 않았습니다. 깃발도 세지 않았습니다. 그가 본 것은 얼굴이었습니다. 얼굴은 거짓말을 못 했습니다.

### SC_058 · LOC_005_AMNOK (trại Tùy, lối đi) · CHAR_101, 수 병사 · — · video8s · 8:02–8:10
[ACTION-VI] Cận theo mắt 을지문덕: một lính Tùy trẻ đứng gác đang lén nhai mẩu vỏ cây, thấy ông nhìn thì giấu vào tay; người bên cạnh gò má hõm, môi nứt; ông không đổi nét mặt, chỉ chớp mắt một lần. Rack focus từ mặt lính sang mặt ông.
[SOUND] mưa, nhai khẽ.
N: 나무껍질이었습니다. 백 일치 군량을 받은 군대가 나무를 씹고 있었습니다. 을지문덕은 그 순간 셈을 끝냈습니다. 나머지는 확인이었습니다.

### SC_059 · LOC_005_AMNOK (lều 우중문, trại Tùy) · CHAR_202, CHAR_203, CHAR_101, CHAR_105 · PROP_021 · video8s · 8:10–8:18
[ACTION-VI] Lều lớn, sàn ván ướt: 우중문 ngồi ghế gấp, 명광개 hai gương ngực, râu trắng dài, áo choàng đỏ; 우문술 đứng bên, giáp sẫm không trang trí, thẻ tre trong tay; hai hàng vệ sĩ. 을지문덕 bước vào, dừng giữa lều, cúi đầu vừa phải — không quỳ; 해모루 sau vai ông.
[SOUND] mưa trên mái lều, giáp vệ sĩ.
N: 우중문. 아홉 군을 이끄는 두 총사령 중 하나. 황제는 결정을 그에게 맡겼습니다. 그의 품에는 밀지가 있었습니다. 을지문덕이 오면 붙잡으라.

### SC_060 · LOC_005_AMNOK (lều 우중문) · CHAR_202, CHAR_105, CHAR_101 · — · video8s · 8:18–8:26
[ACTION-VI] 우중문 hỏi bằng giọng gầm, không đứng dậy; 해모루 nghiêng đầu sát tai 을지문덕, môi mấp máy dịch thầm (P-11: quy ước — Tùy nói Hán ngữ, 해모루 dịch; trên màn hình khán giả nghe tiếng Hàn); 을지문덕 không nhìn 우중문 — nhìn cái bàn có bút và lụa.
[SOUND] mưa, giọng gầm, tiếng thì thầm.
N: 을지문덕은 한문을 읽고 썼습니다. 말은 해모루가 옮겼습니다. 적장 앞에서 그는 한 마디도 소리 내지 않을 작정이었습니다.
우중문: 고구려 왕은 어찌 오지 않았는가.

### SC_061 · LOC_005_AMNOK (lều 우중문) · CHAR_101 · — · video8s · 8:26–8:34
[ACTION-VI] 을지문덕 bước tới bàn thấp, cầm bút lông, chấm mực, viết một hàng chữ ngắn trên lụa (brush calligraphy, không chữ rõ), đặt bút xuống ngay ngắn; một hoạn quan bưng tấm lụa tới 우중문. Cận bàn tay ông — không run.
[SOUND] bút chạm lụa, mưa.
N: 필담이었습니다. 붓으로 하는 대화. 왕은 성에 계시다. 신이 대신 왔다. 항복이라는 글자는 쓰지 않았습니다. 옷이 대신 말했습니다.

### SC_062 · LOC_005_AMNOK (lều 우중문) · CHAR_202, CHAR_203 · — · video8s · 8:34–8:42
[ACTION-VI] 우중문 đọc lụa, mặt đỏ dần; ông nghiêng sang 우문술, nói nhỏ nhưng khán giả nghe — tay đặt lên ngực áo nơi có mật chỉ. 우문술 không đáp, nhìn về phía cửa lều.
[SOUND] lụa, mưa, giáp vệ sĩ động.
N: 우중문은 밀지를 떠올렸습니다. 붙잡으면 공이었습니다. 놓치면 책임이었습니다. 그의 손은 이미 가슴으로 갔습니다.
우중문: 붙잡으라는 밀지가 있소.

### SC_063 · LOC_005_AMNOK (lều 우중문) · 유사룡, CHAR_202 · — · video8s · 8:42–8:50
[ACTION-VI] Một quan văn Tùy áo xanh sẫm, mũ sa đen — 유사룡, 위무사 — bước ra từ hàng bên, chắp tay, nói với 우중문 giọng đều, không run; 우중문 nhìn ông ta rất lâu.
[SOUND] mưa.
N: 위무사 유사룡. 황제가 항복을 받으라고 보낸 문관이었습니다. 그 한 마디가 30만 5천 명의 운명을 갈랐습니다.
유사룡: 항복하러 온 자를 잡으면 누가 다시 오겠습니까.

### SC_064 · LOC_005_AMNOK (lều 우중문) · CHAR_202, CHAR_101 · — · video8s · 8:50–8:58
[ACTION-VI] 우중문 phẩy tay — vệ sĩ lùi lại; 을지문덕 cúi đầu vừa phải lần nữa, quay người; 해모루 cụp cờ trắng theo. 우중문 nhìn tấm lụa trên tay, không nhìn người đi ra.
[SOUND] mưa, bước chân trên ván.
N: 을지문덕은 풀려났습니다. 병영에 있었던 시간은 차 한 잔 식을 시간이었습니다. 그 시간에 그는 필요한 것을 다 보았습니다.

### SC_065 · LOC_005_AMNOK (trại Tùy, lối đi ra) · CHAR_101, CHAR_105 · — · video8s · 8:58–9:06
[ACTION-VI] Hai người đi ra giữa hàng lính, bước đều, không nhanh; 을지문덕 nói không quay đầu, môi gần như không động; 해모루 gật rất nhỏ. Tracking phía trước họ.
[SOUND] mưa, giáo, bùn.
N: 걸음은 느렸습니다. 도망치는 사람은 뛰지 않습니다. 을지문덕은 한 가지를 미리 정해 두었습니다. 무슨 일이 있어도 뒤를 보지 않는다.
을지문덕: 돌아보지 말게.

### SC_066 · LOC_005_AMNOK (lều 우중문) · CHAR_202, 수 기병 사자 · — · video8s · 9:06–9:14
[ACTION-VI] 우중문 đứng bật dậy, tấm lụa rơi; ông đập tay lên bàn, gọi một sĩ quan kỵ binh vào; sĩ quan quỳ nhận lệnh, chạy ra.
[SOUND] ghế đổ, lụa rơi, giáp chạy.
N: 문이 닫히자 우중문은 후회했습니다. 밀지는 밀지였습니다. 그는 사람을 보냈습니다. 이것도 역사책 그대로입니다.
우중문: 사람을 보내라. 더 할 말이 있다 하라.

### SC_067 · LOC_005_AMNOK (bãi cuội bờ bắc) · 수 기병 사자, kỵ Tùy, CHAR_101, CHAR_105 · WPN_201 · video8s · 9:14–9:22
[ACTION-VI] 50 kỵ Tùy phóng ra khỏi cổng trại, sĩ quan dẫn đầu gào về phía toán người đang đi ra bãi cuội; 을지문덕 và 해모루 đi tiếp, lưng thẳng, không quay đầu; toán 4 lính Goguryeo đi sau bắt đầu nhìn lại — 해모루 giơ tay ra hiệu không.
[SOUND] vó ngựa dồn trên cuội, tiếng gọi, mưa.
N: 뒤에서 부르는 소리가 났습니다. 돌아보는 순간, 항복하러 온 사람은 도망치는 사람이 됩니다. 그는 끝까지 항복하러 온 사람이었습니다.
수 기병 사자: 더 할 말이 있소! 멈추시오!

### SC_068 · LOC_005_AMNOK (đồi bờ nam — màn hình drone) · CHAR_005 · UAV_001 · video8s · 9:22–9:30
[ACTION-VI] Màn hình drone: từ trên cao, 50 chấm kỵ binh thu hẹp khoảng cách với 6 chấm người trên bãi cuội trắng; mép nước xanh ngay trước toán người. 태오 gào vào radio, pin trên góc màn hình: 19.
[SOUND] rotor qua loa, PTT.
N: 하늘 눈이 처음으로 제 일을 했습니다. 거리를 재는 일이었습니다.
장태오: 기병 오십. 장군까지 이백 미터.

### SC_069 · LOC_005_AMNOK (mỏm đá bờ nam) · CHAR_001, CHAR_006 · WPN_004 · video8s · 9:30–9:38
[ACTION-VI] 백성민 tì vai vào K6, mắt trên thước ngắm, ngón tay đặt lên cò; 한승우 đứng thấp sau ông, ống nhòm, nói không cao giọng; sau lưng, K2 vẫn tắt máy.
[SOUND] mưa, K6 lên đạn "철컥".
N: 사람을 쏘면 을지문덕은 도망친 사람이 됩니다. 물을 쏘면 그는 여전히 걸어가는 사람입니다. 한승우는 그 차이를 알았습니다.
한승우: 물에다 쏴. 사람은 안 맞힌다.

### SC_070 · LOC_005_AMNOK (bãi cạn) · CHAR_006 (off), kỵ Tùy, 수 기병 사자 · WPN_004, WPN_201 · video8s · 9:38–9:46
[ACTION-VI] 2-BEAT: (a) 9:38–9:42 K6 nổ dài từ mỏm đá — một hàng cột nước trắng bùng lên ngang bãi cạn ngay trước mũi hàng kỵ binh Tùy, cuội văng; (b) 9:42–9:46 ngựa dựng đứng, kỵ sĩ ghì cương, hàng đầu dồn vào hàng sau; sĩ quan Tùy trợn mắt nhìn mặt nước đang sôi — không thấy ai bắn.
[SOUND] K6 12.7 nổ dài, nước bùng, ngựa hí, cuội rơi.
N: 육십 발이 물에 들어갔습니다. 수나라 기병은 총을 몰랐습니다. 그러나 천둥이라는 말은 알았습니다. 뇌군이 강 건너에 있다고, 그들은 그날 저녁 보고했습니다.

### SC_071 · LOC_005_AMNOK (bãi cạn) · CHAR_101, CHAR_105 · — · video8s · 9:46–9:54
[ACTION-VI] 을지문덕 lội qua bãi cạn, nước đến gối, áo lụa sẫm nước, 조우관 vẫn ngay ngắn, không quay đầu; 해모루 sau ông, cũng không quay đầu; sau lưng họ, kỵ Tùy đứng yên ở mép nước như bị đóng đinh. Tracking phía trước, thấp sát mặt nước.
[SOUND] nước, mưa, ngựa hí xa.
N: 을지문덕은 압록수를 건너 돌아왔습니다. 삼국사기의 문장은 짧습니다. 돌아보지 않고 압록수를 건넜다. 그 짧은 문장 뒤에 이 강이 있었습니다.

### SC_072 · LOC_005_AMNOK (mỏm đá bờ nam) · CHAR_005 · UAV_001 · video8s · 9:54–10:02
[ACTION-VI] Drone hạ xuống lòng bàn tay 태오, rotor ngừng; cậu nhìn màn hình pin: 14; lấy vải lau nước mưa trên ống kính, cẩn thận như lau kính người già.
[SOUND] rotor dừng, mưa.
N: 삼십 분이 십사 분이 되었습니다. 다음 충전은 전차 육백 미터였습니다. 그 육백 미터는 아직 어디에 쓸지 정해지지 않았습니다.
장태오: 배터리 십사 분 남았습니다.

### SC_073 · LOC_005_AMNOK (sườn đồi bờ nam, rừng thông) · CHAR_101, CHAR_105, CHAR_001 · — · still_kenburns · 10:02–10:12
[ACTION-VI] Ảnh: 을지문덕 leo sườn thông ướt lên mỏm đá, áo lụa dính người, hai lông trắng trên mũ rũ nước; 해모루 sau; trên mỏm, 한승우 đứng chờ, áo choàng gai, không chào — chỉ đứng thẳng. Ken-burns đẩy chậm lên mặt 을지문덕.
[SOUND] mưa, cành thông.
N: 그는 언덕에 올랐습니다. 전차는 한 발도 쏘지 않았습니다. 그는 그것도 보았습니다. 그가 한 대장에게 한 말은 한 마디였습니다.

### SC_074 · LOC_005_AMNOK (mỏm đá) · CHAR_101 · — · video8s · 10:12–10:20
[ACTION-VI] Cận 을지문덕: nước mưa chảy trên râu bạc ngắn, mắt bình thản; ông nói với 한승우 ngoài khung — không giải thích thêm; nói xong ông nhìn về bờ bắc.
[SOUND] mưa, im.
을지문덕: 저들은 굶고 있소. 굶는 군대는 이기게 두면 되오.

### SC_075 · LOC_005_AMNOK (aerial mưa) · — · WPN_201 · still_kenburns · 10:20–10:30
[ACTION-VI] Ảnh aerial: trại Tùy bờ bắc trong mưa, 50 kỵ binh quay về cổng thành một vệt nhỏ; sông xanh; bờ nam rừng thông không thấy gì. Ken-burns kéo ra chậm.
[SOUND] mưa, trống xa.
N: 그는 적진에서 무기를 보지 않았습니다. 병사들의 얼굴을 봤습니다.

[Kết thúc Phần 4]

## [Phần 5] 지는 것도 병법이오 — 「지는 것도 병법이오」 / Chứng minh sức mạnh  (10:30–14:00)
> Tóm tắt VI: D10. ENEMY POV [史]: 우문술 "군량이 없소. 돌아가야 하오." — 우중문 "장군은 십만 군을 가지고 소적을 못 깨고 무슨 낯으로 폐하를 뵙겠소?" — 우문술 nhượng. 9 quân vượt 압록수. Trận giả thua đầu tiên: 300 kỵ 해모루 xung phong rồi "vỡ"; cối 10 viên từ sườn núi vào đội đuổi. Lệnh 을지문덕: "지되, 죽지는 마시오. 지는 것도 병법이오." Vấn đề mới: (1) tiền quân Tùy học tầm cối → giãn đội hình; (2) 태오 ống nhòm nhìn đuôi cột quân bờ bắc: 천둥 3 bị 40 con bò kéo dưới cờ Tùy — "저건… 우리 찹니다." 탁발흠 cưỡi ngựa bên xe.
> Chức năng: BATTLE nhỏ / DEMO · Tài nguyên: cối 60→50 · 1 kỵ Goguryeo chết, 3 bị thương · Enemy adaptation: giãn đội hình ngoài tầm cối · [NARRATOR IM LẶNG] 12:02–13:02 · Open loop: "그들의 장갑차가 적의 깃발 아래서 소 마흔 마리에 끌려오고 있었습니다." → [MID-ROLL 2 · 14:00]

### SC_076 · LOC_005_AMNOK (lều 우문술, trại Tùy, sáng D10) · CHAR_203, CHAR_202 · — · video8s · 10:30–10:38
[ACTION-VI] Lều 우문술: bàn thấp đầy thẻ tre ướt; 우문술 giáp sẫm, râu xám ngắn, đặt một bó thẻ tre xuống bàn trước 우중문 đang đứng; ông nói chậm, từng chữ, mắt không rời 우중문.
[SOUND] mưa trên lều, thẻ tre.
N: 이튿날 아침. 두 총사령이 마주 앉았습니다. 우문술은 셈을 하는 사람이었습니다. 군량은 열흘 치도 남지 않았습니다.
우문술: 군량이 없소. 돌아가야 하오.

### SC_077 · LOC_005_AMNOK (lều 우문술) · CHAR_202 · — · video8s · 10:38–10:46
[ACTION-VI] 우중문 đập bó thẻ tre xuống sàn ván, râu trắng rung; ông cúi sát mặt 우문술, nói câu mắng nổi tiếng — giọng gầm, không hét.
[SOUND] thẻ tre vãi, mưa.
N: 우중문의 셈에는 황제가 있었습니다. 이 말은 수서에 그대로 남아 있습니다.
우중문: 장군은 십만 군을 가지고 소적을 못 깨고 무슨 낯으로 폐하를 뵙겠소?

### SC_078 · LOC_005_AMNOK (lều 우문술) · CHAR_203 · — · video8s · 10:46–10:54
[ACTION-VI] 우문술 nhìn bó thẻ tre dưới sàn rất lâu; ông không nhặt; đứng dậy, cầm mũ sắt, cúi đầu một cái ngắn về phía 우중문 — nhượng bộ không lời — đi ra.
[SOUND] mũ sắt, ván sàn, mưa.
N: 우문술은 물러섰습니다. 우중문에게는 이유가 하나 더 있었습니다. 황제가 찾는 천둥이 강 건너에 있었습니다. 아홉 군은 군량 없이 강을 건너기로 했습니다.

### SC_079 · LOC_005_AMNOK (bãi cạn, aerial, ngày mưa) · — · WPN_201, PROP_021 · still_kenburns · 10:54–11:06
[ACTION-VI] Ảnh aerial: hàng chục cột quân Tùy lội qua bãi cạn Áp Lục, nước đến ngực, giáo và cờ đỏ dựng thành rừng trên mặt nước xanh; bờ bắc vẫn đen kịt người chờ đến lượt; bờ nam — bãi cuội trống, rừng thông. Ken-burns trượt ngang theo dòng người. Không thoại.
[SOUND] nước, hàng vạn bước chân, trống, nạo bạt.
N: 선봉은 하루 만에 건넜습니다. 아홉 군이 다 건너는 데는 사흘이 걸렸습니다. 가슴까지 오는 물이었습니다. 건너는 동안 아무도 막지 않았습니다. 을지문덕이 막지 말라고 했기 때문입니다. 이 결정이 살수까지 가는 첫걸음이었습니다.

### SC_080 · LOC_005_AMNOK (đồi bờ nam, rừng thông) · CHAR_101, CHAR_105, CHAR_001 · VEH_101 · video8s · 11:06–11:14
[ACTION-VI] Trong rừng thông: 을지문덕 đã mặc lại giáp lamellar, đứng cạnh ngựa; 해모루 giáp, tù và ở hông; 한승우 áo choàng gai. 을지문덕 chỉ bằng hai ngón tay: xuống bãi, rồi lên sườn núi bên phải nơi hố cối. Câu lệnh ngắn, không giải thích.
[SOUND] mưa, ngựa, xa xa nước.
N: 그날 오후 을지문덕은 첫 번째 싸움을 짰습니다. 이기는 싸움이 아니었습니다. 잘 지는 싸움이었습니다.
을지문덕: 삼백 기가 치고 무너지오. 그대들은 산에서 열 발만.

### SC_081 · LOC_005_AMNOK (rừng thông) · CHAR_101, CHAR_105, CHAR_001 · — · video8s · 11:14–11:22
[ACTION-VI] 을지문덕 nhìn 해모루, rồi nhìn 한승우 — hai người, một câu; ông lên ngựa. Cận mặt ông khi nói, rồi cắt sang mặt 해모루 và 한승우 nghe.
[SOUND] yên ngựa, mưa.
을지문덕: 지되, 죽지는 마시오. 지는 것도 병법이오.

### SC_082 · LOC_005_AMNOK (hố cối trên sườn núi bờ nam) · 박격포 사수, tổ cối · WPN_002 · video8s · 11:22–11:30
[ACTION-VI] Hố cối đào vội trong rừng thông, hai ống cối dựng, đạn xếp thành hàng: đúng 10 viên, 5 mỗi khẩu; 사수 đếm bằng ngón tay, gật với 한승우 (off); một lính lấy tay che mưa cho đạn.
[SOUND] đạn cối lách cách, mưa.
N: 박격포탄은 육십 발이었습니다. 요동성에서 쉰 발을 썼습니다. 열 발이면 지는 싸움을 진짜처럼 보이게 할 수 있었습니다.
박격포 사수: 박격포, 열 발. 열 발뿐입니다.

### SC_083 · LOC_005_AMNOK (bãi cuội bờ nam) · CHAR_105, kỵ Goguryeo, 수 선봉 · VEH_101, WPN_201, PROP_018 · video8s · 11:30–11:38
[ACTION-VI] Tiền quân Tùy đã lên bờ nam, đang xếp hàng ướt sũng trên bãi cuội; từ rừng thông, tù và Goguryeo rúc — 300 kỵ 해모루 đổ xuống sườn dốc thành mũi nhọn, giáp lamellar, cung giương, cờ 삼족오. Wide, aerial trung.
[SOUND] tù và, vó ngựa dồn xuống dốc, tiếng hô.
N: 해모루의 삼백이 내려갔습니다. 진짜로 쳤습니다. 지는 싸움도 처음은 진짜여야 했습니다. 그렇지 않으면 적은 쫓지 않습니다.

### SC_084 · LOC_005_AMNOK (bãi cuội) · kỵ Goguryeo, 수 선봉 · VEH_101, WPN_201, WPN_101 · video8s · 11:38–11:46
[ACTION-VI] Va chạm: kỵ Goguryeo bắn cung khi phi, xé vào mép hàng Tùy còn ướt; giáo Tùy dựng lên; một kỵ Goguryeo trúng tên rơi khỏi ngựa xuống cuội; đồng đội phi vòng qua. Wide, không cận thương vong.
[SOUND] dây cung hàng loạt, giáo chạm giáp, ngựa hí, thét.
N: 첫 부딪침에서 고구려 기병 하나가 떨어졌습니다. 지는 싸움에도 값은 있었습니다. 을지문덕은 그 값을 알고 시켰습니다.

### SC_085 · LOC_005_AMNOK (bờ bắc, mép nước) · CHAR_202 · WPN_201, PROP_021 · video8s · 11:46–11:54
[ACTION-VI] 우중문 trên ngựa ở mép nước bờ bắc, áo choàng đỏ ướt, nhìn qua sông thấy kỵ Goguryeo đang quần thảo tiền quân; ông rút kiếm chỉ sang bờ nam, gào.
[SOUND] tiếng gào, trống nổi, nước.
N: 우중문은 강 건너에서 그것을 보았습니다. 을지문덕의 기병이었습니다. 어제 놓친 사람이 다시 나타난 것이었습니다.
우중문: 을지 놈이 왔다! 쫓아라!

### SC_086 · LOC_005_AMNOK (bãi cuội) · CHAR_105, kỵ Goguryeo · VEH_101, PROP_012, PROP_018 · video8s · 11:54–12:02
[ACTION-VI] 해모루 nâng tù và rúc hai hồi ngắn; kỵ Goguryeo đồng loạt quay ngựa — nhưng quay lộn xộn, tản mác, một người "rơi" cờ 삼족오 xuống cuội và không nhặt; cả đoàn "chạy" lên sườn núi phía đông-nam thành từng cụm rời rạc.
[SOUND] tù và hai hồi, vó ngựa tán loạn, cờ đổ.
N: 두 번 부는 나각은 무너지라는 뜻이었습니다. 깃발은 일부러 떨어뜨렸습니다. 쫓는 자에게 깃발만큼 좋은 미끼는 없었습니다.

[NARRATOR IM LẶNG — 12:02 → 13:02]

### SC_087 · LOC_005_AMNOK (bãi cạn + bãi cuội) · 수 선봉, 수 총관 · WPN_201, PROP_021 · video8s · 12:02–12:10
[ACTION-VI] Tiền quân Tùy reo hò, tràn lên bãi cuội đuổi theo; hàng nghìn người từ bãi cạn lội gấp vào bờ nam, hàng ngũ vỡ thành đám đông chạy; một tướng Tùy (총관) trên ngựa vung giáo thúc. Aerial trung — "không thấy điểm cuối" phía sau.
[SOUND] reo hò, nước, giáp chạy trên cuội.

### SC_088 · LOC_005_AMNOK (hố cối) · tổ cối · WPN_002 · video8s · 12:10–12:18
[ACTION-VI] Hố cối: hai khẩu bắn liên tiếp — chớp cam trong mưa, 사수 thả đạn không nhìn, đếm bằng môi; 5 viên mỗi khẩu; đạn xếp hàng cạn dần đến viên cuối.
[SOUND] "퉁, 퉁, 퉁" dồn dập, mưa.

### SC_089 · LOC_005_AMNOK (bãi cuội, mép nước) · 수 선봉 · WPN_201 · video8s · 12:18–12:26
[ACTION-VI] Đạn cối rơi vào đám đông đang tràn lên mép bờ nam — cột cuội và nước bùng lên giữa đội hình, người ngã hàng loạt, cờ đổ; đám đông khựng, tách ra hai bên vết nổ; nhưng phía sau vẫn tràn lên. Wide, không gore.
[SOUND] mười tiếng nổ dội qua nước, thét, ngựa.

### SC_090 · LOC_005_AMNOK (rừng thông sườn núi) · CHAR_107, CHAR_004 · — · video8s · 12:26–12:34
[ACTION-VI] Sau gốc thông: 아리 ngồi bó gối, hai tay bịt tai, mắt nhắm; 서아 ôm vai cô, mắt mở nhìn về phía bãi cuội đang chớp lửa; khăn olive trên cổ 아리 ướt sũng. Không thoại.
[SOUND] nổ xa dội qua rừng, mưa trên lá, thở.

### SC_091 · LOC_005_AMNOK (gờ đá, K3) · CHAR_002, CHAR_001 · WPN_003 · video8s · 12:34–12:42
[ACTION-VI] 오태민 nằm sau khẩu K3 trên gờ đá, báng đã tì vai, ngón tay vào cò — dưới kia đám đông Tùy đang lên bờ trong tầm; 한승우 quỳ sau ông, đặt tay lên nắp hộp tiếp đạn, nói thấp. 오태민 nghiến răng, không bắn.
[SOUND] nổ xa, mưa, thở gấp.
한승우: 안 쏜다. 지는 중이다.

### SC_092 · LOC_005_AMNOK (bãi cuội) · 수 총관, 수 선봉 · WPN_201 · video8s · 12:42–12:50
[ACTION-VI] Tướng Tùy trên ngựa hét, vung giáo sang hai bên: đám đông tản rộng ra hai cánh, bỏ đường giữa nơi hố cối vừa cày; đội hình từ khối đặc thành hình quạt thưa, tiếp tục tiến lên sườn núi theo dấu kỵ Goguryeo — chậm hơn, xa hơn.
[SOUND] hô lệnh, giáp chạy, mưa.

### SC_093 · LOC_005_AMNOK (rừng thông sườn đông-nam) · CHAR_105, kỵ Goguryeo · VEH_101 · video8s · 12:50–12:58
[ACTION-VI] Kỵ Goguryeo gom lại trong rừng thông trên cao, ngựa thở dốc; một người bị tên ở đùi được đỡ xuống; 해모루 phi tới chỗ 한승우, mặt ướt mưa và mồ hôi, nói câu ngắn — nửa hỏi, nửa cười.
[SOUND] ngựa thở, mưa, xa xa reo hò Tùy.
해모루: 졌소. 잘 졌소?

### SC_094 · LOC_005_AMNOK (gờ đá) · CHAR_001, CHAR_003 · WPN_002 · video8s · 12:58–13:06
[ACTION-VI] 한승우 nhìn xuống bãi cuội qua ống nhòm: đám Tùy đã tản thành hình quạt ngoài tầm cối; ông hạ ống nhòm; bên cạnh, 박기철 gạch một vạch trên bảng gỗ: 60 → 50.
[SOUND] mưa, bút dạ trên gỗ.
N: 적은 배웠습니다. 열 발이 떨어진 자리를 피해 옆으로 퍼졌습니다. 박격포는 이제 쉰 발이었습니다. 배우는 적을 상대로, 쉰 발은 많지 않았습니다.

### SC_095 · LOC_005_AMNOK (mỏm đá bờ nam) · CHAR_005 · PROP_006 · video8s · 13:06–13:14
[ACTION-VI] 태오 với ống nhòm nhìn không phải bãi cuội — nhìn xa qua sông, về đuôi cột quân trên bờ bắc: cậu chỉnh nét, khựng, chỉnh lại; miệng há ra. Máy đẩy vào mặt cậu.
[SOUND] mưa, ống nhòm chỉnh nét.
N: 이기고 지는 것과 상관없는 것을, 그날 장태오가 보았습니다. 강 건너 대열의 맨 끝이었습니다.

### SC_096 · LOC_005_AMNOK (bờ bắc, đuôi cột quân — POV ống nhòm) · CHAR_205 · VEH_002 (천둥 3), VEH_206, PROP_021 · video8s · 13:14–13:22
[ACTION-VI] POV ống nhòm rung: bờ bắc, sau hàng cờ Tùy cuối cùng, một khối vuông xanh-nâu quen thuộc lăn chậm trên đường lầy — K21 천둥 3, xích quay theo dây kéo, trước mũi xe hai hàng bò — 40 con — ách gỗ, người đánh bò; kỵ Tiên Ti hộ tống hai bên. Trên hông xe: hai lỗ bu-lông trống.
[SOUND] mưa; qua ống nhòm chỉ có gió.
장태오: 저건… 우리 찹니다.

### SC_097 · LOC_005_AMNOK (bờ bắc — POV ống nhòm) · CHAR_205 · VEH_002 (천둥 3), VEH_206 · video8s · 13:22–13:30
[ACTION-VI] POV ống nhòm zoom sát: 탁발흠 cưỡi ngựa vàng nâu đi sát hông K21, mũ vành lông cáo, bím tóc, một tay đặt lên tấm giáp xe như đặt lên cổ con vật mới bắt; hắn ngẩng nhìn về phía núi bờ nam — đúng hướng ống nhòm.
[SOUND] gió trong ống nhòm.
N: 탁발흠이었습니다. 골짜기에서 타지 않은 장갑차를 그가 가져갔습니다. 소 마흔 마리, 하루 팔십 리. 그는 부대를 쫓지 않았습니다. 뇌군은 어차피 압록수로 올 것이었습니다.

### SC_098 · LOC_005_AMNOK (mỏm đá) · CHAR_003, CHAR_005 · PROP_006, PROP_023 · video8s · 13:30–13:38
[ACTION-VI] 박기철 lấy ống nhòm từ tay 태오, nhìn một lúc lâu, hạ xuống; tay ông đưa ra sau, chạm vào biển thép "3" buộc trên quai ba lô — chỉ chạm, không nói; 태오 nhìn ông.
[SOUND] mưa, ống nhòm hạ.
N: 박기철은 아무 말도 하지 않았습니다. 그가 뗀 명판은 등에 있었습니다. 명판 없는 장갑차 안에는 40밀리 포탄 예순 발이 그대로 있었습니다.

### SC_099 · LOC_005_AMNOK (sườn núi bờ nam, mưa) · CHAR_101 · VEH_101 · still_kenburns · 13:38–13:48
[ACTION-VI] Ảnh: 을지문덕 trên ngựa giữa rừng thông cao, giáp ướt, nhìn xuống bãi cạn nơi quân Tùy vẫn đang tràn qua sông không dứt; sau lưng ông, kỵ binh sắp hàng lại im lặng. Ken-burns đẩy chậm vào mặt ông.
[SOUND] mưa, xa xa nước và trống.
N: 첫 번째 패배였습니다. 앞으로 더 여러 번 질 것이었습니다. 을지문덕은 만족한 얼굴이 아니었습니다. 세는 얼굴이었습니다.

### SC_100 · LOC_005_AMNOK (bờ bắc, đường lầy — cận) · CHAR_205 · VEH_002 (천둥 3), VEH_206, PROP_021 · still_kenburns · 13:48–14:00
[ACTION-VI] Ảnh: mưa; K21 천둥 3 lăn trên đường lầy, dây kéo căng về phía hai hàng bò, kỵ Tiên Ti đi kèm, cờ Tùy đỏ trên nóc xe cắm vào giá đồ; bùn dính nửa thân. Ken-burns đẩy chậm vào bánh xích đang quay theo bò.
[SOUND] bò rống, dây kéo kẽo kẹt, xích lăn, mưa.
N: 그들의 장갑차가 적의 깃발 아래서 소 마흔 마리에 끌려오고 있었습니다.

[MID-ROLL 2 · 14:00]

[Kết thúc Phần 5]

## [Phần 6] 이유는 그때 말하겠소 — 「이유는 그때 말하겠소」 / Liên minh không dễ  (14:00–17:30)
> Tóm tắt VI: Đêm D11, sơn thành nhỏ một ngày đường phía nam 압록 (LOC_008). Lều 을지문덕: lệnh không giải thích — "살수로 먼저 가시오. 갈대밭 북쪽 여울. 거기서 기다리시오." 한승우: "왜 거깁니까?" — "이유는 그때 말하겠소." 오태민 đòi đánh xe lương địch — bị cấm lần 3: "저들은 이기고 있다고 믿어야 하오." 해모루 thú nhận có lệnh không được nói kế. 한승우 quyết TIN — nhận vị trí; trao 해모루 một radio PRC-999K kẹp lên giáp: "이걸로 부르시오." — "말하는 돌이오?" 을지문덕 viết thư cho vua. Mini-combat: 백성민 + 2 kỵ Goguryeo chặn 2 척후 Tùy trên đường phía NAM (red herring). 을보 sờ K2: "이 쇠가 땀을 흘리네." 서아 rửa vết thương kỵ binh bằng thuốc 을보; 아리 kể mẹ quê làng ven 살수 — biết đường lau sậy. Đêm, radio: 태오 "우리는 왜 여기 있습니까?" — "몰라. 그래서 살아 있어야 해."
> Chức năng: POLITICS · Tài nguyên: — (kháng sinh 0 nhắc lại) · Foreshadow: 아리 lau sậy (4화) · "살아 있어야 해" (P10) · K2 "땀" (P7) · Open loop: "을지문덕은 계획을 말하지 않았습니다. 다만 강 이름을 말했습니다. 살수."

### SC_101 · LOC_005_AMNOK (bờ bắc, đường lầy — cận) · — · VEH_002 (천둥 3), VEH_206 · still_kenburns · 14:00–14:10
[ACTION-VI] Ảnh cận thấp sát đất: bánh xích K21 lăn chậm theo dây kéo, bùn ép qua guốc xích, móng bò và chân kỵ Tiên Ti đi ngang phía trước; mưa lấm ống kính. Ken-burns đẩy chậm. Không thoại.
[SOUND] xích lăn nặng, bò rống, dây kéo, mưa.
N: 쇠수레는 소를 따라갔습니다. 하루에 팔십 리. 팔십 리씩, 그것은 황제의 것이 되어 가고 있었습니다.

### SC_102 · LOC_008_GOGURYEO_VILLAGE (sơn thành trên đỉnh đồi, đêm mưa) · — · VEH_001, PROP_012, PROP_016 · still_kenburns · 14:10–14:22
[ACTION-VI] Ảnh: sơn thành Goguryeo nhỏ trên đỉnh đồi — tường đá xếp khan thấp 3–4 m, một cổng gỗ, tháp canh, đuốc dưới mái che; bên trong, K2 đậu cạnh kho thóc nâng sàn; một lều vải gai lớn có cờ 삼족오 ướt; ngựa buộc hàng dài. Ken-burns đẩy vào lều có cờ.
[SOUND] mưa, đuốc, ngựa.
N: 이튿날 밤, 압록수에서 하루 거리 남쪽. 작은 산성이었습니다. 을지문덕의 천막이 거기 있었습니다. 천둥 중대가 그 천막에 불려 간 것은 두 번째였습니다. 첫 번째는 요동성이었습니다.

### SC_103 · LOC_008_GOGURYEO_VILLAGE (lều 을지문덕) · CHAR_101, CHAR_001, CHAR_105 · PROP_001 (bản đồ da Goguryeo) · video8s · 14:22–14:30
[ACTION-VI] Trong lều: đèn dầu, bản đồ da trải trên rương gỗ; 을지문덕 ngồi, giáp cởi vai, áo 저고리; 한승우 đứng, 해모루 bên cột; 을지문덕 nói không ngẩng lên khỏi bản đồ — lệnh, không phải thảo luận; khi nói, ông đặt một quân cờ gỗ đen lên vạch sông ở 살수.
[SOUND] mưa trên vải, đèn dầu.
N: 을지문덕은 설명하는 사람이 아니었습니다. 요동성에서도 그랬습니다. 그는 숫자를 묻고, 자리를 정했습니다.
을지문덕: 살수로 먼저 가시오. 갈대밭 북쪽 여울. 거기서 기다리시오.

### SC_104 · LOC_008_GOGURYEO_VILLAGE (lều — insert bản đồ) · CHAR_101 (tay) · PROP_001 · video8s · 14:30–14:38
[ACTION-VI] Cận: ngón tay gân guốc của 을지문덕 trên bản đồ da — đi từ vạch sông Áp Lục xuống một vạch sông khác ngoằn ngoèo, dừng ở một điểm phình rộng có nét vẽ lau sậy; bên cạnh, ngón tay 한승우 đặt xuống cách đó một gang — nơi Bình Nhưỡng.
[SOUND] da bản đồ, mưa.
N: 살수. 오늘날의 청천강입니다. 평양에서 북쪽으로 팔십 킬로. 그 자리는 이 부대의 마지막 자리가 될 것이었습니다. 아직 아무도 몰랐습니다.

### SC_105 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_001 · — · video8s · 14:38–14:46
[ACTION-VI] 한승우 nhìn bản đồ, rồi nhìn thẳng 을지문덕; câu hỏi ngắn, kính trọng nhưng không lùi.
[SOUND] mưa, đèn.
N: 한승우는 살수를 알았습니다. 학교에서 배운 이름이었습니다. 배운 것은 결과뿐이었습니다. 왜 거기인지는 배우지 않았습니다.
한승우: 왜 거깁니까?

### SC_106 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_101 · — · video8s · 14:46–14:54
[ACTION-VI] 을지문덕 ngẩng lên lần đầu, nhìn 한승우 — không khó chịu, không giải thích; một câu, rồi cúi lại bản đồ.
[SOUND] đèn dầu lép bép.
을지문덕: 이유는 그때 말하겠소.

### SC_107 · LOC_008_GOGURYEO_VILLAGE (ngoài lều, sân sơn thành đêm) · CHAR_006, 2 kỵ Goguryeo · EQP_001, VEH_101 · video8s · 14:54–15:02
[ACTION-VI] Ngoài lều: 백성민 kéo kính đêm xuống mắt, hai kỵ Goguryeo dắt ngựa theo ông ra cổng gỗ; lính gác Goguryeo mở then; ba bóng người biến vào mưa. Máy đứng ở cửa lều nhìn ra.
[SOUND] then gỗ, mưa, vó ngựa nhỏ dần.
N: 산성 아래 길에 수나라 척후가 있었습니다. 백성민이 나갔습니다. 해모루의 기병 둘이 따랐습니다. 말을 바꿔 탄 날부터 둘은 말 없이도 통했습니다.

### SC_108 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_002 · — · video8s · 15:02–15:10
[ACTION-VI] Walk-in: 오태민 từ cửa lều bước thẳng tới rương bản đồ, ngón tay ấn xuống vạch cột quân Tùy phía bắc, giọng to hơn cần thiết; 해모루 quay đầu nhìn ông; 한승우 không cản.
[SOUND] mưa.
N: 세 번째였습니다. 산길에서 한 번, 압록수에서 한 번. 틀린 말은 아니었습니다. 때가 틀렸을 뿐이었습니다.
오태민: 지금 쳐야 합니다. 저들은 굶고 있습니다.

### SC_109 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_101 · — · video8s · 15:10–15:18
[ACTION-VI] 을지문덕 không nhìn 오태민; nói với bản đồ; nhưng câu nói dành cho cả lều. 오태민 há miệng — đóng lại.
[SOUND] đèn, mưa.
N: 을지문덕의 셈은 이랬습니다. 굶는 군대는 이기면 더 깊이 들어옵니다. 지면 돌아갑니다. 돌아가면 다시 옵니다.
을지문덕: 저들은 이기고 있다고 믿어야 하오.

### SC_110 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_105, CHAR_001 · — · video8s · 15:18–15:26
[ACTION-VI] 해모루 bước khỏi cột, đến gần 한승우, nói nhỏ như thú nhận — mắt liếc 을지문덕 đang cúi trên bản đồ, người không tỏ ra nghe.
[SOUND] mưa, đèn.
N: 해모루도 다 알지 못했습니다. 을지문덕은 부하에게도 계책을 나누어 주지 않았습니다. 새는 것은 사람이었기 때문입니다.
해모루: 계책은… 말하지 말라는 명이오. 나도 다는 모르오.

### SC_111 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_001, CHAR_105 · EQP_002 · video8s · 15:26–15:34
[ACTION-VI] 한승우 im một nhịp; rồi ông tháo máy radio cầm tay khỏi ngực giáp — khối olive có ăng-ten ngắn — đưa cho 해모루 bằng hai tay. 해모루 nhìn nó, không nhận ngay.
[SOUND] khóa nhựa mở, mưa.
N: 한승우는 믿기로 했습니다. 이유를 모르고 명령을 받은 것은 처음이었습니다. 상대가 을지문덕이었기 때문입니다. 그는 그 믿음에 물건 하나를 얹었습니다.
한승우: 이걸로 부르십시오.

### SC_112 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_105, CHAR_001 · EQP_002 · video8s · 15:34–15:42
[ACTION-VI] 해모루 cầm radio, đưa lên tai như vỏ ốc; 한승우 lấy lại, kẹp nó vào dây buộc giáp ngực của 해모루, bấm PTT — radio kêu "칙"; 해모루 giật nhẹ, rồi cười.
[SOUND] PTT "칙", tiếng cười ngắn.
N: 무전기 하나가 고구려 갑옷에 달렸습니다. 그날부터 이 무전기는 두 시대를 잇는 줄이었습니다. 닿는 거리는 십 킬로. 산이 막으면 그보다 짧았습니다.
해모루: 말하는 돌이오?

### SC_113 · LOC_008_GOGURYEO_VILLAGE (lều) · CHAR_101 · — · video8s · 15:42–15:50
[ACTION-VI] 을지문덕 ngẩng lên đúng lúc radio kêu; nhìn khối olive trên giáp 해모루 — không hỏi nó là gì; nhìn 한승우 — rồi cúi lại bản đồ, đặt quân cờ đen thứ hai sát cạnh quân đầu ở 살수. Máy đẩy nhẹ.
[SOUND] mưa, đèn.
N: 을지문덕은 묻지 않았습니다. 그는 그것도 셌습니다. 말하는 돌 하나, 십 킬로. 그의 판에 말이 하나 더 놓였습니다.

### SC_114 · LOC_008_GOGURYEO_VILLAGE (lều, sau khi mọi người ra) · CHAR_101 · PROP_013 (lụa, bút) · video8s · 15:50–15:58
[ACTION-VI] Lều trống; 을지문덕 một mình, kéo tấm lụa, chấm bút, viết chậm — cột chữ brush calligraphy; đèn dầu soi nửa mặt; ống đựng thư da ở thắt lưng mở nắp.
[SOUND] bút trên lụa, mưa.
N: 그날 밤 그는 편지를 썼습니다. 받는 사람은 평양의 대왕이었습니다. 적은 굶는다. 적은 건넜다. 신은 살수로 간다. 왕에게도 계책의 전부는 적지 않았습니다.

### SC_115 · LOC_008_GOGURYEO_VILLAGE (đường mòn dưới sơn thành, đêm — POV kính đêm) · CHAR_006, 수 척후 · EQP_001, VEH_101 · video8s · 15:58–16:06
[ACTION-VI] POV kính đêm xanh: đường mòn đất dưới chân đồi, mưa; hai bóng người Tùy dắt ngựa đi chậm, cúi nhìn dấu xích K2 trên bùn; một tên ngẩng lên nhìn về phía nam đường. Sau lùm cây, 백성민 nằm; hai kỵ Goguryeo giương cung trong tối.
[SOUND] kính đêm rít, mưa, vó ngựa dắt.
N: 척후 둘이었습니다. 그들은 쇠수레의 자국을 보고 있었습니다. 자국은 남쪽으로 이어졌습니다.

### SC_116 · LOC_008_GOGURYEO_VILLAGE (đường mòn, đêm) · CHAR_006, kỵ Goguryeo, 수 척후 · WPN_101, VEH_101 · video8s · 16:06–16:14
[ACTION-VI] Hai mũi tên Goguryeo từ tối — tên thứ nhất ngã; tên thứ hai quay chạy, 백성민 từ lùm cây lao ra quật xuống bùn, dao kề cổ; kỵ Goguryeo bắt hai con ngựa. Nhanh, không tiếng súng.
[SOUND] dây cung, thân ngã, bùn, ngựa giật.
N: 총은 쓰지 않았습니다. 총소리는 산성을 알립니다. 화살은 알리지 않습니다. 이것도 산길에서 배운 것이었습니다.

### SC_117 · LOC_008_GOGURYEO_VILLAGE (cổng sơn thành) · CHAR_006, CHAR_105, CHAR_001 · EQP_001 · video8s · 16:14–16:22
[ACTION-VI] 백성민 quay vào cổng, mưa và bùn khắp người, kính đêm gạt lên; báo với 한승우 và 해모루 đứng dưới mái đuốc; 해모루 gật — "남쪽" — nhìn về phía nam trong mưa.
[SOUND] mưa, đuốc.
N: 남쪽. 그 말이 모두의 머리에 박혔습니다. 위험은 남쪽에서 올 것이었습니다. 반만 맞는 생각이었습니다.
백성민: 수나라 척후 둘. 남쪽 길을 보고 있었습니다.

### SC_118 · LOC_008_GOGURYEO_VILLAGE (sân sơn thành, cạnh K2, đêm) · CHAR_106, CHAR_003 · VEH_001 · video8s · 16:22–16:30
[ACTION-VI] 을보 chống gậy đi vòng quanh K2 dưới mưa như đi quanh con bò mua mới; ông đặt lòng bàn tay lên lưới thoát khí sau tháp — rút tay lại, xoa hai ngón: ẩm, nhờn; ông nói với 박기철 đang đứng cạnh, nheo mắt trái. 박기철 cau mày, sờ theo.
[SOUND] mưa trên thép, gậy gõ.
N: 을보는 쇠를 손으로 읽는 사람이었습니다. 그날 밤 그가 읽은 것을, 박기철은 이튿날 계기판에서 읽었습니다.
을보: 이 쇠가 땀을 흘리네.

### SC_119 · LOC_008_GOGURYEO_VILLAGE (mái che kho thóc, đêm) · CHAR_004, CHAR_107, kỵ Goguryeo bị thương · PROP_009 · video8s · 16:30–16:38
[ACTION-VI] Dưới mái kho thóc: kỵ Goguryeo bị tên ở đùi (từ P5) nằm trên chiếu; 서아 rửa vết thương bằng nước thuốc màu nâu từ bát đất — thuốc 을보 sắc; 아리 quỳ cạnh đưa vải, đọc tên cây thuốc; 서아 lặp lại theo.
[SOUND] mưa, nước, tiếng thì thầm tên cây.
N: 항생제는 요동성에서 끝났습니다. 이제 약은 을보가 달인 물이었습니다. 스물네 살 의무병이 이 땅의 약초를 배우고 있었습니다.

### SC_120 · LOC_008_GOGURYEO_VILLAGE (mái che kho thóc) · CHAR_107, CHAR_004 · — · video8s · 16:38–16:46
[ACTION-VI] 아리 vừa vắt vải vừa nói, giọng nhẹ như kể chuyện nhà; 서아 ngừng tay nhìn cô.
[SOUND] mưa, vải vắt.
N: 살수. 아리는 그 이름을 지도에서 배우지 않았습니다. 어머니의 고향이었습니다.
아리: 어머니 고향이 살수예요. 갈대밭 옆이요.

### SC_121 · LOC_008_GOGURYEO_VILLAGE (mái che kho thóc) · CHAR_004, CHAR_107 · — · video8s · 16:46–16:54
[ACTION-VI] 서아 cười mệt, nói nhỏ; 아리 gật mạnh — bím tóc ướt văng nước; sau lưng hai cô, ở góc khung, 태오 đi ngang với radio trực đêm.
[SOUND] mưa.
N: 갈대밭에는 갈대를 베는 사람만 아는 길이 있습니다. 그 길이 다음 이야기에서 사람 하나를 살릴 것이었습니다.
윤서아: 그 길, 나중에 나한테도 가르쳐 줘.

### SC_122 · LOC_008_GOGURYEO_VILLAGE (tường sơn thành, chòi canh, đêm) · CHAR_005 · EQP_002 · video8s · 16:54–17:02
[ACTION-VI] 태오 trực radio trên tường đá dưới mái chòi canh, poncho trùm, mưa chảy dọc mép; cậu bấm PTT gọi 한승우 (đang ở tường bên kia) — không phải báo cáo, là câu hỏi; giọng trẻ, thấp.
[SOUND] mưa, PTT.
N: 자정. 무전기에 보고가 아닌 말이 올라왔습니다. 스물한 살이 서른네 살에게 묻는 말이었습니다.
장태오: 중대장님… 우리는 왜 여기 있습니까?

### SC_123 · LOC_008_GOGURYEO_VILLAGE (tường sơn thành, phía tây, đêm) · CHAR_001 · EQP_002 · video8s · 17:02–17:10
[ACTION-VI] 한승우 đứng một mình ở góc tường phía tây, radio áp tai, nhìn xuống thung lũng đen; ông im lâu hơn bình thường trước khi trả lời; tay kia đặt lên túi ngực có lựu đạn.
[SOUND] mưa, PTT.
N: 한승우는 대답을 갖고 있지 않았습니다. 없는 것을 있는 척하지 않았습니다. 그것이 아흔네 명을 여기까지 데려온 방식이었습니다.
한승우: 몰라. 그래서 살아 있어야 해.

### SC_124 · LOC_008_GOGURYEO_VILLAGE (lều 을지문덕, ngoài, đêm) · — · PROP_012 · still_kenburns · 17:10–17:20
[ACTION-VI] Ảnh: lều vải gai có cờ 삼족오 ướt trong mưa đêm, ánh đèn dầu vàng hắt qua vải — rồi đèn tắt, lều thành khối đen (veo-stage: 2 still 5 s sáng → tắt, hoặc 1 video8s). Ken-burns đẩy chậm vào cửa lều.
[SOUND] mưa, đèn tắt.
N: 을지문덕의 등불은 자정에 꺼졌습니다. 그는 잤습니다. 계책을 가진 사람은 잘 수 있었습니다. 계책을 모르는 사람들은 그 밤에 잘 자지 못했습니다.

### SC_125 · LOC_008_GOGURYEO_VILLAGE (aerial sơn thành đêm mưa) · — · VEH_001 · still_kenburns · 17:20–17:30
[ACTION-VI] Ảnh aerial: sơn thành nhỏ tối trên đỉnh đồi giữa mưa, hai đuốc cổng, K2 là khối sẫm cạnh kho thóc; xa phía bắc, dưới thung lũng, một dải lửa trại Tùy mờ. Ken-burns kéo ra chậm.
[SOUND] mưa, gió.
N: 을지문덕은 계획을 말하지 않았습니다. 다만 강 이름을 말했습니다. 살수.

[Kết thúc Phần 6]

## [Phần 7] 쇠수레는 산을 못 넘는다 — 「쇠수레는 산을 못 넘는다」 / Kẻ địch thích nghi  (17:30–21:00)
> Tóm tắt VI: (a) ENEMY POV, bờ bắc 압록, đêm D10: 탁발흠 chui vào 천둥 3 — ngửi dầu, sờ giá đỡ drone, cầm một viên 40mm. Bản đồ vẽ trong bùn: xe sắt không qua núi → chỉ một con đường: 석문령. "쇠수레는 산을 못 넘소. 길로 가오." Hắn đã thấy ở thung lũng 요동성 (2화, 12 ngày rình): "새는 수레에 앉아 밥을 먹고, 밤눈을 가진 자들은 그때 가만히 있소." → đánh lúc xe ngủ, chim ăn. Lính nhét vải vào tai ngựa, tập với trống. Lệnh 양제 từ 육합성: "천둥을 산 채로 잡아라." → 2.000 kỵ. (b) D12: K2 rò nước làm mát trên dốc, đồng hồ đỏ; 박기철: dừng 2 ngày — 을보: "쇠는 쇠요. 구리로 때우면 되지." Hậu vệ 해모루 đuổi 척후 Tùy; 2 척후 sót bắn tên lửa vào cành thông trên nóc K2 — 아리 dập bằng khăn olive (khăn cháy sém). Làng dưới chân đèo. 백성민: cột Tùy cách 2 ngày phía sau (천둥 3 ở lại bờ bắc 압록 với 200 kỵ); đường dê tây-bắc có phân ngựa mới — 해모루 xác nhận có gửi 3 척후 → hiểu sai. 박기철: "이틀 서 있으면 전차 삼 킬로가 날아갑니다."
> Chức năng: THREAT (turning point) · Tài nguyên: dầu −3 km (APU 2 ngày) · Enemy adaptation: đoán đường từ vật lý xe · đánh lúc sạc · bịt tai ngựa · lệnh bắt sống · Red herring: phân ngựa = 해모루 척후 · Open loop: 탁발흠 "쇠수레가 멈췄다. 물을 마시고 있다." → [MID-ROLL 3 · 21:00]

### SC_126 · LOC_005_AMNOK (bờ bắc, bãi lầy cạnh đường, đêm D10) · CHAR_205 · VEH_002 (천둥 3), VEH_206 · video8s · 17:30–17:38
[ACTION-VI] Đêm mưa tạnh, đuốc; 천둥 3 đậu bên đường lầy, bò đã tháo ách; 탁발흠 trèo lên nóc xe bằng động tác leo ngựa, mở nắp cửa nóc, cúi đầu vào trong, hít — mùi dầu; hắn nhăn mũi rồi chui hẳn xuống. Kỵ Tiên Ti cầm đuốc đứng quanh, không ai dám lên.
[SOUND] nắp thép, đuốc, bò xa.
N: 강을 건넌 날 밤, 강 북쪽. 탁발흠은 쇠수레 안으로 들어갔습니다. 열흘 동안 그는 겉만 보았습니다. 이제 속을 볼 차례였습니다.

### SC_127 · LOC_005_AMNOK (trong K21 천둥 3, đêm) · CHAR_205 · VEH_002 · video8s · 17:38–17:46
[ACTION-VI] Trong khoang K21 tối, đuốc từ cửa nóc chiếu xuống: 탁발흠 sờ ghế, sờ giá đỡ trống nơi từng đặt hộp drone (khung kim loại có dây chằng), rồi rút một viên đạn 40mm từ giá — nặng, lạnh, bóng — xoay trước đuốc; hắn ngửi nó, đặt lại đúng chỗ.
[SOUND] kim loại, thở, đuốc.
N: 안에는 40밀리 포탄 예순 발이 남아 있었습니다. 그는 그것이 무엇인지 몰랐습니다. 모르는 것은 건드리지 않는다. 그것이 그가 살아남은 방식이었습니다.

### SC_128 · LOC_005_AMNOK (bờ bắc, bên đống lửa — bản đồ trong bùn) · CHAR_205, 선비 부장 · — · still_kenburns · 17:46–17:56
[ACTION-VI] Ảnh: bên đống lửa, mặt bùn phẳng bị vạch bằng mũi đao: một vạch ngang là sông Áp Lục; phía nam, hai dãy gạch chéo là núi; giữa hai dãy, một đường duy nhất ngoằn ngoèo — mũi đao dừng ở chỗ hẹp nhất; bàn tay 탁발흠 đặt một viên sỏi lên chỗ đó. Ken-burns đẩy vào viên sỏi.
[SOUND] lửa, mũi đao trên bùn.
N: 그는 산을 알았습니다. 쇠수레는 논을 못 갑니다. 나무다리를 못 건넙니다. 산을 못 넘습니다. 남쪽 길은 요동성 앞에서 잡은 농부에게 미리 물어 두었습니다. 압록수 남쪽에서 쇠수레가 갈 길은 하나뿐이었습니다. 석문령. 돌문 고개였습니다.

### SC_129 · LOC_005_AMNOK (bờ bắc, bên đống lửa) · CHAR_205, 수 총관 사자 · — · video8s · 17:56–18:04
[ACTION-VI] Một sĩ quan Tùy (sứ của 총관 tiền quân, giáp sắt) đứng bên lửa nghe; 탁발흠 ngồi xổm, mũi đao gõ lên viên sỏi, nói bằng giọng người giải thích cho kẻ chậm hiểu.
[SOUND] lửa, đao gõ sỏi.
N: 수나라 총관은 뇌군이 어디로 갔는지 물었습니다. 탁발흠은 지도를 보지 않았습니다. 쇠수레를 보았습니다.
탁발흠: 쇠수레는 산을 못 넘소. 길로 가오.

### SC_130 · LOC_005_AMNOK (bờ bắc, bên đống lửa) · CHAR_205 · — · video8s · 18:04–18:12
[ACTION-VI] 탁발흠 ngẩng lên, nhìn về phía tây — nơi 요동성, nơi hắn đã nằm 12 ngày trên sườn núi nhìn xuống thung lũng xe sắt; hắn nói câu thứ hai chậm hơn, như đọc lại điều đã ghi trong đầu. Sĩ quan Tùy không hiểu; 부장 của hắn hiểu.
[SOUND] lửa, nước sông xa.
N: 요동성 골짜기 위에서 열이틀을 본 것이었습니다. 쇠새는 수레 등에서 밥을 먹었습니다.
탁발흠: 새는 수레에 앉아 밥을 먹고, 밤눈을 가진 자들은 그때 가만히 있소.

### SC_131 · LOC_005_AMNOK (bãi ngựa Tiên Ti, đêm) · kỵ Tiên Ti, CHAR_205 · VEH_206, PROP_017 · video8s · 18:12–18:20
[ACTION-VI] Bãi ngựa: kỵ Tiên Ti nhét cuộn vải dạ nhỏ vào tai từng con ngựa, buộc dây qua má; một người gõ trống trận Tùy ngay cạnh mõm ngựa — con ngựa giật lần một, lần hai, rồi đứng yên nhai cỏ; 탁발흠 đứng nhìn, gật.
[SOUND] trống gõ dồn, ngựa phì, vải.
N: 요하에서 그의 말들은 천둥소리에 미쳤습니다. 세 번째는 없어야 했습니다. 귀를 막은 말은 천둥을 듣지 못합니다. 듣지 못하는 말은 달립니다.

### SC_132 · LOC_004_YUKHAPSEONG (육합성, lầu vàng — 요동성) · CHAR_201, 수 전령 · UAV_001 (xác drone #1), PROP_021 · video8s · 18:20–18:28
[ACTION-VI] Trong lầu 육합성: 양제 không giáp, áo lụa vàng thổ, 통천관, cầm xác drone #1 (từ 1화) lên ngang mắt xoay xem; dưới bậc, một 전령 quỳ, ống thư tre; ông nói không nhìn xuống — nhìn cánh quạt gãy.
[SOUND] lụa, cánh quạt nhựa kêu, mưa trên mái.
N: 닷새 전, 요동성 앞 육합성. 넉 달째였습니다. 황제의 손에는 부서진 쇠새가 있었습니다. 그는 온전한 것을 원했습니다.
수 양제: 천둥을 산 채로 잡아라.

### SC_133 · LOC_005_AMNOK (bờ bắc, bãi ngựa, rạng sáng D11) · 수 전령, CHAR_205 · VEH_206, PROP_021 · video8s · 18:28–18:36
[ACTION-VI] Rạng sáng: 전령 Tùy bụi đường quỳ dâng ống thư cho 탁발흠; hắn mở, nhìn chữ (không đọc to), cuộn lại nhét vào áo; sau lưng hắn, bãi ngựa Tiên Ti trải rộng — hai nghìn kỵ đang lên yên, tai ngựa buộc vải.
[SOUND] vó ngựa hàng loạt, dây cương, gió sớm.
N: 명령은 삼백 킬로를 닷새에 왔습니다. 산 채로. 죽이면 천둥은 없어집니다. 탁발흠에게 이천 기가 주어졌습니다. 이번에는 사람을 노릴 생각이었습니다.

### SC_134 · LOC_009_SEOKMUN_PASS (đường dốc chân đèo, ngày D12, mưa phùn) · CHAR_003, 조종수 · VEH_001 · video8s · 18:36–18:44
[ACTION-VI] K2 bò lên dốc đá ướt; cận màn hình lái: vạch nhiệt độ động cơ đỏ, đèn cảnh báo nháy; hơi nước trắng phụt từ lưới thoát khí sau tháp; 박기철 chạy bên hông xe, đập tay lên giáp, hét; xe khựng, dừng, hơi nước trùm.
[SOUND] động cơ gầm rồi tụt, cảnh báo bíp, hơi nước xì, tay đập thép.
N: 을보가 땀이라 부른 것은 냉각수였습니다. 오르막에서 새는 것이 터졌습니다. 55톤은 물이 없으면 달리지 못합니다.
박기철: 세워! 세워!

### SC_135 · LOC_009_SEOKMUN_PASS (chân đèo) · CHAR_003, CHAR_001 · VEH_001 · video8s · 18:44–18:52
[ACTION-VI] 박기철 leo lên đuôi xe, mở tấm lưới buồng động cơ — hơi nước phà vào mặt, ông quay đi ho; cận: ống cao su nứt dọc, nước làm mát phun thành tia mỏng lên tấm tản nhiệt; ông đóng lại, nhảy xuống, nói với 한승우 đang đi tới; tay băng dính dầu mới.
[SOUND] hơi nước, lưới thép, ho.
N: 박기철은 숫자로 말하는 사람이었습니다. 이번 숫자는 날이었습니다.
박기철: 냉각수입니다. 이틀은 세워야 합니다.

### SC_136 · LOC_009_SEOKMUN_PASS (chân đèo) · CHAR_106, CHAR_003 · VEH_001, PROP_019 · video8s · 18:52–19:00
[ACTION-VI] 을보 chống gậy leo lên đuôi xe không cần ai đỡ, dí mũi vào hơi nước, sờ ống nứt bằng đầu ngón tay chai; ông rút từ cuộn dụng cụ một mảnh đồng mỏng cũ, gõ lên ống — nói với 박기철 kiểu người thợ nói với người thợ.
[SOUND] đồng gõ cao su, hơi nước.
N: 요동성에서 을보는 쇠는 쇠요, 라고 말했습니다. 그때는 바퀴였습니다. 이번에는 물길이었습니다.
을보: 쇠는 쇠요. 구리로 때우면 되지.

### SC_137 · LOC_009_SEOKMUN_PASS (đường phía sau đoàn, ngày) · CHAR_105, kỵ Goguryeo, 수 척후 · VEH_101, WPN_201, EQP_002 · video8s · 19:00–19:08
[ACTION-VI] Cách đoàn 1 km về phía bắc trên đường núi: 30 kỵ hậu vệ Goguryeo của 해모루 gặp ~20 kỵ Tùy đang dò theo vết xích; hai bên bắn cung khi phi; 해모루 ghì cương, tay trái lóng ngóng ấn PTT trên máy radio ở ngực, gào át tiếng ngựa.
[SOUND] dây cung, vó ngựa, PTT, gió.
N: 대열 뒤로 수나라 척후가 붙었습니다. 해모루가 처음으로 말하는 돌을 썼습니다. 돌은 속삭여도 들립니다.
해모루: 한 대장, 여기는 해모루! 뒤에 척후! 내가 막소!

### SC_138 · LOC_009_SEOKMUN_PASS (đường phía sau đoàn) · kỵ Goguryeo, 수 척후 · VEH_101, WPN_201 · video8s · 19:08–19:16
[ACTION-VI] Kỵ Goguryeo giáp lamellar xông thẳng, kỵ Tùy nhẹ hơn quay đầu; một kỵ Tùy bị kéo khỏi yên bằng dây thòng lọng của kỵ Goguryeo; số còn lại chạy ngược đường xuống; 해모루 dừng ở khúc cua, không đuổi. Wide.
[SOUND] ngựa, thòng lọng, thét ngắn, gió.
N: 척후는 돌아갔습니다. 돌아간 척후는 보고를 합니다. 쇠수레가 고개 밑에 섰다. 그 보고는 그날 저녁 탁발흠에게 닿았습니다.

### SC_139 · LOC_009_SEOKMUN_PASS (đường lên làng, gờ đá bên trên, ngày) · CHAR_107, CHAR_106, 수 척후, 병사 · VEH_001, WPN_201, WPN_001 · video8s · 19:16–19:24
[ACTION-VI] 2-BEAT: (a) 19:16–19:20 low-angle từ đường: hai mũi tên quấn vải cháy rít xuống từ gờ đá bên trên (2 척후 Tùy còn sót), một mũi cắm vào cành thông phủ nóc K2 đang lết lên dốc, nhựa thông bén lửa; (b) 19:20–19:24 cận đuôi xe: 아리 giật khăn olive khỏi cổ đập lửa liên tiếp, 을보 quát; khăn cháy sém một góc, lửa tắt.
[SOUND] tên lửa rít, lửa bén cành, khăn đập, quát; off-screen: K2C1 loạt ngắn lên gờ, một tiếng ngã.
N: 척후 둘이 남아 있었습니다. 요동성에서 배운 것을 썼습니다. 쇠수레는 탄다. 열다섯 살 소녀가 그 불을 껐습니다. 의무병이 준 수건으로.
을보: 아리야! 내려와!

### SC_140 · LOC_008_GOGURYEO_VILLAGE (làng dưới chân đèo, ngày mưa) · đại đội, dân làng · VEH_001 · video8s · 19:24–19:32
[ACTION-VI] K2 bò với tốc độ người đi bộ vào làng núi — nhà gỗ mái vỏ cây chèn đá, kho thóc nâng sàn; hơi nước vẫn rỉ; dân làng đứng ở cửa nhìn, trẻ con núp sau cột; lính Hàn đi bộ hai bên xe, ngựa Goguryeo theo sau. Tracking phía trước.
[SOUND] xích chậm, hơi nước, chó sủa, mưa.
N: 고개 밑에 마을이 있었습니다. 열다섯 집. 마을 사람들은 도망치지 않았습니다. 삼족오 깃발이 같이 왔기 때문입니다.

### SC_141 · LOC_008_GOGURYEO_VILLAGE (wide từ ruộng bậc thang ngước lên) · — · VEH_001 · still_kenburns · 19:32–19:44
[ACTION-VI] Ảnh: từ ruộng kê non ngước lên làng: K2 đậu cạnh kho thóc nâng sàn, cành thông phủ nóc; khói bếp lam; trên cao, sau làng, con đường đất ngoằn ngoèo bò lên một khe giữa hai vách đá xám-xanh chìm trong mây — 석문령. Ken-burns đẩy chậm lên khe đèo.
[SOUND] mưa, gió, xa xa búa rèn.
N: 마을 위가 석문령이었습니다. 두 벼랑 사이의 안장 같은 고개. 남쪽으로 가는 수레 길은 그 고개뿐이었습니다. 이틀. 쇠수레는 그 밑에서 이틀을 서 있어야 했습니다.

### SC_142 · LOC_008_GOGURYEO_VILLAGE (lò rèn làng, chiều) · CHAR_106, CHAR_003 · PROP_019 · video8s · 19:44–19:52
[ACTION-VI] Lò rèn làng: 을보 kéo bễ da, lò đất cháy cam, tấm đồng mỏng nung đỏ trong kìm; 박기철 cầm đoạn ống nứt và tấm tản nhiệt tháo ra, xoay cho ông xem; 을보 gật, đặt đồng lên đe, búa nhỏ gõ — tia lửa.
[SOUND] bễ, búa gõ đồng, lửa.
N: 7세기의 대장간이 21세기의 물길을 고치고 있었습니다. 구리 관을 만들어 끼우고, 송진을 먹인 가죽끈으로 조일 것이었습니다. 을보의 손은 빨랐습니다.

### SC_143 · LOC_008_GOGURYEO_VILLAGE (cạnh kho thóc, K2) · CHAR_005 · VEH_001, UAV_001 · video8s · 19:52–20:00
[ACTION-VI] 태오 cắm dây sạc một hàng pin kính đêm vào ổ đuôi K2; hộp drone đóng nắp bên cạnh — không sạc; APU rì rì sau tháp dù động cơ chính tắt; cậu ngồi xổm nhìn đèn sạc đỏ, nói với 박기철 đi ngang (chỉ thấy chân).
[SOUND] APU, đèn sạc.
N: 전차가 서 있는 동안 보조동력은 돌았습니다. 탁발흠이 요동성 골짜기에서 본 것이 바로 이것이었습니다.
장태오: 전차가 서야 얘가 밥을 먹습니다.

### SC_144 · LOC_009_SEOKMUN_PASS (gờ núi phía bắc làng, chiều) · CHAR_006 · PROP_006 · video8s · 20:00–20:08
[ACTION-VI] 백성민 nằm trên gờ đá cao phía bắc, ống nhòm về phía bắc: POV — rất xa dưới thung lũng, cột quân Tùy đen như dòng nước chậm, cờ đỏ rũ mưa; không thấy đầu đuôi. Ông hạ ống nhòm, nhìn trời tính.
[SOUND] gió, ống nhòm.
N: 수나라 대열은 이틀 뒤에 있었습니다. 소가 끄는 쇠수레는 강 북쪽에 남았습니다. 고치는 데 이틀. 오는 데 이틀.

### SC_145 · LOC_009_SEOKMUN_PASS (đường dê tây-bắc, chiều) · CHAR_006 · — · video8s · 20:08–20:16
[ACTION-VI] Đường dê: lối mòn rộng 1 m bám vách đá xám-xanh, dốc; 백성민 ngồi xổm, lấy que gạt một đống phân ngựa — còn ướt bên trong, hơi bốc nhẹ; ông nhìn lên đường dê ngoằn ngoèo mất hút vào mây, rồi nhìn xuống về phía nam.
[SOUND] gió, que gạt.
N: 북서쪽 염소 길. 사람 하나가 겨우 지나는 길이었습니다. 거기에 말똥이 있었습니다.
백성민: 말똥. 반나절.

### SC_146 · LOC_009_SEOKMUN_PASS (đường dê) · CHAR_006 · EQP_002 · video8s · 20:16–20:24
[ACTION-VI] 백성민 bấm radio, giọng phẳng; ông vẫn nhìn đống phân — nghi ngờ đang tìm chỗ bám.
[SOUND] PTT, gió.
N: 그는 물었습니다. 답이 반만 맞았을 뿐입니다.
백성민: 해모루, 여기는 수색. 북서쪽 염소 길에 척후 보냈습니까?

### SC_147 · LOC_009_SEOKMUN_PASS (đường xe dưới làng) · CHAR_105 · EQP_002, VEH_101 · video8s · 20:24–20:32
[ACTION-VI] 해모루 trên ngựa ở khúc đường dưới làng, cúi đầu nói vào máy radio trên ngực — lần này không hét, gần như thì thầm, thử nghiệm; ông ngẩng nhìn lên vách tây-bắc nơi đường dê bò lên.
[SOUND] PTT, mưa nhỏ.
N: 해모루는 셋을 보냈습니다. 그래서 말똥은 해모루의 것이었습니다. 백성민은 그렇게 결론을 내렸습니다. 그것만은 아니었습니다.
해모루: 보냈소. 셋이오.

### SC_148 · LOC_008_GOGURYEO_VILLAGE (cạnh K2, hoàng hôn) · CHAR_003, CHAR_001 · VEH_001 · video8s · 20:32–20:40
[ACTION-VI] Hoàng hôn xám: APU K2 vẫn chạy; 박기철 gạch lên bảng gỗ một con số nhỏ, đưa cho 한승우 xem; sau lưng, dây sạc chạy từ đuôi xe vào hiên nhà gỗ nơi kính đêm xếp hàng.
[SOUND] APU, bút dạ.
N: 서 있어도 기름은 줄었습니다. 보조동력은 낮에도 밤에도 돌았습니다. 이틀치 전기를 박기철은 거리로 바꿔 적었습니다.
박기철: 이틀 서 있으면 전차 삼 킬로가 날아갑니다.

### SC_149 · LOC_009_SEOKMUN_PASS (gờ núi xa phía đông-bắc, hoàng hôn) · CHAR_205, 선비 부장 · VEH_206 · video8s · 20:40–20:48
[ACTION-VI] Trên một gờ núi xa cách làng 5 km, hoàng hôn hổ phách nhạt qua mây: 탁발흠 nằm sấp sau tảng đá, 부장 bên cạnh; hắn nhìn xuống thung lũng — làng nhỏ, một chấm sẫm bất động cạnh kho thóc, và sợi khói lò rèn bốc lên không dứt từ mái che bên suối. Hắn nheo mắt.
[SOUND] gió trên cao.
N: 척후의 보고는 정확했습니다. 탁발흠은 직접 보러 왔습니다. 그가 본 것은 서 있는 쇠수레와 꺼지지 않는 대장간 연기였습니다.

### SC_150 · LOC_009_SEOKMUN_PASS (gờ núi xa, hoàng hôn — cận) · CHAR_205 · — · still_kenburns · 20:48–21:00
[ACTION-VI] Ảnh cận: mặt 탁발흠 sau tảng đá — sẹo thái dương, mắt hẹp, mũ lông cáo ướt; ánh hoàng hôn cuối trên gò má; phía sau, mờ, hàng kỵ binh nằm rạp. Ken-burns đẩy rất chậm vào mắt hắn.
[SOUND] gió, im.
탁발흠: 쇠수레가 멈췄다. 물을 마시고 있다.

[MID-ROLL 3 · 21:00]

[Kết thúc Phần 7]

## [Phần 8] 전차냐, 시간이냐 — 「전차냐, 시간이냐」 / Tài nguyên bắt đầu cạn  (21:00–24:00)
> Tóm tắt VI: D12 chiều tối–đêm, làng dưới đèo. Mini-combat: 10 kỵ Tùy 척후 cướp kê ở ruộng bậc thang — 1소대 đuổi bằng loạt ngắn; bao kê rơi lại nửa rỗng: "굶은 겁니다." Lựa chọn: vá K2 (2 ngày, bị đuổi kịp) hay bỏ K2 đi bộ. 오태민: "전차 없이도 싸울 수 있습니다." 박기철: "이 전차가 없으면 우리는 그냥 소총 아흔 자루입니다." 한승우: 을지문덕 gọi "쇠수레" tới bãi cạn — cần khối lượng → vá; qua đèo ban đêm; sạc trên đèo. 태오: "드론 하나. 충전 한 번 남았습니다. 야시경 배터리 40%." 서아 ép 한승우 ngủ 2 giờ — lần đầu sau 3 đêm. 백성민 nhìn đường dê qua kính đêm: sương — không thấy. 을보 gõ đồng suốt đêm. ENEMY: 3 척후 Goguryeo của 해모루 đi qua ngay dưới 30 cung Tiên Ti trên đường dê — 탁발흠 hạ cung: "보내라. 아무도 없다고 하게 두어라." (để họ về báo "không có ai" → red herring được chính địch nuôi).
> Chức năng: DECISION · Tài nguyên nói thành lời: "충전 한 번" · "40%" · Open loop: "그들은 고개에서 배터리를 충전하기로 했습니다. 탁발흠도 같은 고개를 보고 있었습니다."

### SC_151 · LOC_009_SEOKMUN_PASS (bãi ngựa Tiên Ti trong rừng, tối) · kỵ Tiên Ti · VEH_206, PROP_017 · still_kenburns · 21:00–21:10
[ACTION-VI] Ảnh cận: tai một con ngựa thảo nguyên nhét cuộn vải dạ, dây buộc qua má ướt; sau tai, mờ, một bàn tay Tiên Ti gõ trống da nhỏ; mắt ngựa bình thản. Ken-burns đẩy chậm vào cuộn vải. Không thoại.
[SOUND] trống gõ đều, ngựa nhai, mưa nhỏ.
N: 이천 마리의 귀가 막혔습니다.

### SC_152 · LOC_008_GOGURYEO_VILLAGE (ruộng bậc thang dưới làng, chạng vạng D12) · 수 척후 기병, dân làng · WPN_201, PROP_022 · video8s · 21:10–21:18
[ACTION-VI] Chạng vạng: 10 kỵ Tùy nhẹ phóng vào ruộng kê non dưới làng, nhảy xuống, vơ kê, phá cửa một kho thóc nhỏ ở mép ruộng, quẳng bao lên yên; dân làng trên cao la hét; một con chó lao ra bị đá.
[SOUND] ngựa, ván kho vỡ, la hét, chó.
N: 저녁에 수나라 척후가 마을 밭에 들어왔습니다. 정찰이 아니었습니다. 밥이었습니다.

### SC_153 · LOC_008_GOGURYEO_VILLAGE (mép làng nhìn xuống ruộng) · CHAR_002, 1소대 · WPN_001 · video8s · 21:18–21:26
[ACTION-VI] 오태민 dẫn 1소대 chạy ra mép làng, quỳ bắn loạt ngắn xuống ruộng — đất bùng quanh chân ngựa; kỵ Tùy nhảy lên ngựa phóng đi, bao kê rơi rải trên bờ ruộng; một con ngựa ngã, kỵ sĩ bị đồng đội kéo lên yên chạy. Không cận thương vong.
[SOUND] K2C1 loạt ngắn dội vách, ngựa hí, tiếng hô.
N: 총소리가 골짜기에 울렸습니다. 숨길 것은 이미 없었습니다. 척후는 이미 쇠수레를 보았습니다.

### SC_154 · LOC_008_GOGURYEO_VILLAGE (bờ ruộng) · CHAR_002 · PROP_022 · video8s · 21:26–21:34
[ACTION-VI] 오태민 xuống bờ ruộng nhặt một bao gai rơi — nhẹ, lép; ông dốc ngược: vài nắm kê non chưa chín rơi ra; ông nhìn theo hướng kỵ Tùy chạy, nói với lính bên cạnh.
[SOUND] kê rơi, gió chiều.
N: 자루는 반도 차지 않았습니다. 익지도 않은 조였습니다. 오태민은 처음으로 적을 불쌍하다고 생각했습니다.
오태민: 밭을 털고 갑니다. 굶은 겁니다.

### SC_155 · LOC_008_GOGURYEO_VILLAGE (lò rèn, đêm) · CHAR_001, CHAR_002, CHAR_003 · VEH_001 (nền) · video8s · 21:34–21:42
[ACTION-VI] Đêm, dưới mái lò rèn: 한승우, 오태민, 박기철 đứng quanh tấm tản nhiệt tháo ra đặt trên đe; ánh lò cam; ngoài mưa, K2 tối đen cạnh kho thóc, APU rì rì. Ba người, ba hướng nhìn.
[SOUND] lò, mưa, APU xa.
N: 선택은 둘이었습니다. 전차를 고친다. 그러면 뒤가 따라잡습니다. 전차를 버린다. 그러면 살수에 제때 닿습니다. 둘 다 맞는 답이었습니다.

### SC_156 · LOC_008_GOGURYEO_VILLAGE (lò rèn) · CHAR_002 · — · video8s · 21:42–21:50
[ACTION-VI] 오태민 nói trước, tay chỉ ra ngoài mưa về phía nam — không giận, là người tính đường; kính bảo hộ trên mũ đọng nước.
[SOUND] lò, mưa.
N: 오태민의 답은 걷는 것이었습니다. 처음으로 그는 가장 큰 것을 버리자고 했습니다. 그것은 성장이었습니다. 틀린 성장이었습니다.
오태민: 전차 없이도 싸울 수 있습니다.

### SC_157 · LOC_008_GOGURYEO_VILLAGE (lò rèn) · CHAR_003 · — · video8s · 21:50–21:58
[ACTION-VI] 박기철 không cãi to; ông đặt bàn tay băng lên tấm tản nhiệt còn ấm, nói chậm, ngắt nhịp — người đếm nói ra con số cuối cùng của mình.
[SOUND] lò, tay trên kim loại.
N: 박기철의 답은 숫자였습니다. 아흔 자루. 전차 한 대가 그 숫자를 다른 것으로 만들었습니다.
박기철: 이 전차가 없으면 우리는 그냥 소총 아흔 자루입니다.

### SC_158 · LOC_008_GOGURYEO_VILLAGE (lò rèn — insert) · CHAR_106 (tay) · PROP_019 · video8s · 21:58–22:06
[ACTION-VI] Cận: bàn tay chai sạn của 을보 giữ kìm, tấm đồng đỏ trên đe, búa nhỏ gõ nhịp đều — tia lửa bay qua khung; mép đồng cong dần theo hình ống. Không mặt người.
[SOUND] búa gõ đồng đều như đồng hồ.
N: 세 사람이 말하는 동안 네 번째 사람은 두드렸습니다. 쇠는 기다리는 사람의 것이 아니었습니다.

### SC_159 · LOC_008_GOGURYEO_VILLAGE (lò rèn) · CHAR_001 · — · video8s · 22:06–22:14
[ACTION-VI] 한승우 nhìn ra ngoài mưa về phía K2; nói không nhìn ai; tay vô thức chạm túi ngực.
[SOUND] mưa, lò.
N: 갈대밭 북쪽 여울. 을지문덕은 사람을 부르지 않았습니다. 쇠수레를 불렀습니다. 이유는 무게였습니다.
한승우: 장군은 쇠수레를 여울로 부르셨다. 무게가 필요해.

### SC_160 · LOC_008_GOGURYEO_VILLAGE (lò rèn) · CHAR_001, CHAR_002, CHAR_003 · — · video8s · 22:14–22:22
[ACTION-VI] Walk-and-talk: 한승우 bước ra khỏi mái lò rèn vào mưa, đi về phía K2, nói hai câu ngắn không quay lại; 오태민 và 박기철 theo sau; 오태민 cắn môi gật; 박기철 cầm theo tấm tản nhiệt.
[SOUND] lò, mưa.
N: 두 번째 결정이었습니다. 요동 벌판에서 그는 쏘기로 했습니다. 여기서 그는 고치기로 했습니다. 두 번째 값은 첫 번째보다 비쌌습니다.
한승우: 고친다. 고개는 밤에 넘는다.

### SC_161 · LOC_008_GOGURYEO_VILLAGE (lò rèn) · CHAR_003 · — · video8s · 22:22–22:30
[ACTION-VI] Walk-and-talk tiếp: tới đuôi K2 dưới mưa, 박기철 đặt tấm tản nhiệt lên giáp xe, nói ra hậu quả — không phản đối, chỉ nói cho đủ; ông nhìn về phía hiên nhà nơi kính đêm đang sạc, dây sạc chạy qua sân.
[SOUND] lò, APU xa.
N: 밤에 넘으려면 야시경이, 야시경에는 전기가, 전기에는 서 있는 전차가 필요했습니다. 하나가 하나를 끌고 왔습니다.
박기철: 그럼 충전은 고개 위에서 해야 합니다.

### SC_162 · LOC_008_GOGURYEO_VILLAGE (hiên nhà gỗ, dây sạc) · CHAR_005 · UAV_001, EQP_001 · video8s · 22:30–22:38
[ACTION-VI] 태오 ngồi ở hiên, tablet trên đùi hiện cột pin; kính đêm xếp hàng bên cạnh, đèn sạc đỏ; cậu đọc số cho 한승우 đang bước tới — như đọc bảng điểm.
[SOUND] mưa trên mái, đèn sạc.
N: 드론 하나. 한승우가 허락한 충전은 한 번. 나머지 기름은 살수까지의 길이었습니다.
장태오: 드론 하나. 허락된 충전 한 번. 야시경 배터리 40%.

### SC_163 · LOC_008_GOGURYEO_VILLAGE (hiên nhà gỗ) · CHAR_004, CHAR_001 · — · video8s · 22:38–22:46
[ACTION-VI] 서아 chặn 한승우 ở bậc hiên, đưa hai ngón tay lên — hai giờ; giọng 다나까 nhưng là giọng người có quyền y tế; 한승우 định lách qua, dừng.
[SOUND] mưa.
N: 의무병에게는 지휘관을 재울 권한이 있었습니다. 윤서아가 그 권한을 쓴 것은 처음이었습니다.
윤서아: 두 시간입니다. 명령입니다, 중대장님.

### SC_164 · LOC_008_GOGURYEO_VILLAGE (sàn kho thóc nâng, đêm) · CHAR_001 · — · video8s · 22:46–22:54
[ACTION-VI] 한승우 nằm xuống sàn ván kho thóc, poncho kéo tới ngực, mũ đặt cạnh đầu, la bàn trên dây cổ trượt sang bên; ông nhìn trần gỗ một lúc — mắt nhắm. Máy tĩnh trên cao.
[SOUND] mưa trên mái vỏ cây, APU rất xa.
N: 사흘 만에 처음으로 그는 누웠습니다. 잠은 오지 않을 것 같았습니다. 삼십 초 뒤에 왔습니다.

### SC_165 · LOC_008_GOGURYEO_VILLAGE (nhà gỗ, sàn 구들 ấm, đêm) · 병사, CHAR_107, CHAR_005 · — · video8s · 22:54–23:02
[ACTION-VI] Trong nhà gỗ: lính Hàn nằm chen trên sàn đất ấm (구들), súng dựa tường, giày cởi; 아리 rón rén phủ tấm vải gai lên 태오 đang ngủ ngồi dựa cột, controller vẫn trên ngực; cậu không tỉnh.
[SOUND] thở đều, mưa, lửa bếp nhỏ.
N: 병사들은 고구려의 구들 위에서 잤습니다. 천사백 년 뒤에도 이 땅 사람들은 같은 방식으로 방을 데울 것이었습니다.

### SC_166 · LOC_008_GOGURYEO_VILLAGE (làng đêm, wide) · — · VEH_001 · still_kenburns · 23:02–23:12
[ACTION-VI] Ảnh: làng núi trong đêm mưa, mọi nhà tối; chỉ một đốm cam — lò rèn — hắt lên mái vỏ cây và lên hông K2 đậu gần; tiếng búa. Ken-burns đẩy chậm vào lò.
[SOUND] búa gõ đồng đều, mưa.
N: 마을에서 불이 켜진 곳은 한 곳뿐이었습니다. 대장간이었습니다. 그 불은 밤새 꺼지지 않았습니다.

### SC_167 · LOC_008_GOGURYEO_VILLAGE (lò rèn, khuya) · CHAR_106, CHAR_003 · PROP_019 · video8s · 23:12–23:20
[ACTION-VI] Cận hai bàn tay già gõ đồng, mồ hôi trên trán 을보; bên cạnh, 박기철 ngồi giữ đèn pin soi, đầu gật xuống ngủ rồi giật lên, đèn lệch — 을보 không nói, chỉ hắng giọng; đèn thẳng lại.
[SOUND] búa, đèn pin va kìm, hắng giọng.
N: 예순여섯 살과 마흔두 살. 한 사람은 쇠를 두드리고, 한 사람은 불을 비췄습니다. 쇠쟁이들에게 말은 필요 없었습니다.

### SC_168 · LOC_008_GOGURYEO_VILLAGE (cổng làng, đêm) · CHAR_006, 소년 척후 · VEH_101 · video8s · 23:20–23:28
[ACTION-VI] Cổng rào gỗ: 백성민 vỗ vai 소년 척후 đang lên ngựa, chỉ về phía đông — con đường xe lên đèo; cậu bé gật, phi vào mưa không đuốc.
[SOUND] vó ngựa nhỏ dần, mưa.
N: 백성민은 새벽마다 동쪽 길로 소년을 보냈습니다. 남쪽은 해모루가, 북쪽은 대열이 이틀 뒤. 네 번째 방향은 길이 아니었습니다.

### SC_169 · LOC_008_GOGURYEO_VILLAGE (tường sơn thành nhỏ trên làng, đêm — POV kính đêm) · CHAR_006 · EQP_001 · video8s · 23:28–23:36
[ACTION-VI] 백성민 trên tường đá, kính đêm hạ xuống mắt, quay về vách tây-bắc; POV xanh lục: sương dày chảy qua khe đèo, hình ảnh nhòe thành khối sáng đục, không thấy đường dê; ông gạt kính lên, nhìn bằng mắt thường — đen.
[SOUND] kính đêm rít, gió, sương.
N: 야시경은 안개를 보지 못합니다. 안개 속에서 밤눈은 눈이 아니었습니다. 그 밤 염소 길은 안개 속에 있었습니다.
백성민: 안개. 안 보입니다.

### SC_170 · LOC_009_SEOKMUN_PASS (đường dê tây-bắc, đêm sương) · 3 고구려 척후, kỵ Tiên Ti, CHAR_205 · VEH_101, VEH_206, WPN_101 · video8s · 23:36–23:44
[ACTION-VI] Đường dê trong sương đêm: ba 척후 Goguryeo của 해모루 dắt ngựa đi xuống dốc trên đường về, cung đeo lưng, thở phào; máy ngước lên: trên gờ đá ngay phía trên đầu họ, hàng chục kỵ Tiên Ti nằm rạp, cung đã giương, mũi tên chĩa xuống ba cái gáy; 탁발흠 nằm giữa, giơ bàn tay lên — chậm — hạ xuống: hạ cung. Ba người Goguryeo đi qua, không hay biết.
[SOUND] đá dưới móng ngựa, dây cung căng rồi chùng, sương, im.
N: 해모루의 척후 셋이 염소 길을 내려왔습니다. 위에는 아무도 없었다고, 그들은 믿었습니다. 그들 머리 위에 활 서른 개가 있었습니다. 탁발흠은 손을 내렸습니다.

### SC_171 · LOC_009_SEOKMUN_PASS (gờ đá trên đường dê, đêm) · CHAR_205, 선비 부장 · VEH_206 · video8s · 23:44–23:52
[ACTION-VI] 탁발흠 nằm rạp trên gờ đá, nhìn theo ba bóng Goguryeo khuất trong sương phía trên; 부장 bên cạnh vẫn giữ cung, quay sang hắn không hiểu; hắn nói cộc, mắt không rời đường dê; sau lưng, không một đốm lửa.
[SOUND] gió, sương, ngựa thở rất xa.
N: 죽은 척후는 돌아가지 않습니다. 돌아가지 않는 척후는 의심을 남깁니다. 쇠수레가 일어나는 밤, 그는 이 길로 내려갈 것이었습니다.
탁발흠: 보내라. 아무도 없다고 하게 두어라.

### SC_172 · LOC_008_GOGURYEO_VILLAGE (từ làng ngước lên đèo, đêm) · — · — · still_kenburns · 23:52–24:00
[ACTION-VI] Ảnh: từ mái làng ngước lên: hai vách đá xám-xanh của 석문령 đen sẫm trên nền mây đêm, khe yên ngựa giữa hai vách ngậm sương trắng; không ánh sáng nào trên đó. Ken-burns đẩy chậm vào khe.
[SOUND] gió qua khe, xa xa búa rèn.
N: 그들은 고개에서 배터리를 충전하기로 했습니다. 탁발흠도 같은 고개를 보고 있었습니다.

[Kết thúc Phần 8]

## [Phần 9] 석문령, 마흔 분 — 「석문령, 마흔 분」 / Kế hoạch lớn  (24:00–27:30)
> Tóm tắt VI: D14. K2 vá xong — "새지 않습니다." Bàn cát bằng bùn cạnh kho thóc: 석문령 — yên ngựa hẹp, vách hai bên, đường dê tây-bắc (백성민 cắm mũi tên Goguryeo = "해모루 척후" — sai), mỏm đá 200 m đông-nam. Kế: qua đèo đêm; 12 kính đêm (pin 40%) đi đầu với 백성민; drone bay 10 phút cuối trên yên; 태오 lên mỏm đá giữ tín hiệu với 1 xạ thủ K3 + 2 lính súng trường; K2 sau cùng với xe cối; 해모루 chặn phía nam; dừng 40 phút trên yên để APU sạc. 오태민 đòi đi đầu — "너는 전차 옆이다." Rạng sáng: 소년 척후 chạm 2 척후 Tiên Ti trên đường đông (tên cắm yên) → 백성민 đọc là 척후 của cột Tùy phía sau. Mini: 해모루 đuổi 5 척후 Tùy ở cửa nam → "역시 남쪽이다." Chân đèo: 한승우 nhìn mỏm: "너무 높다." — 태오: "신호는 높아야 잡힙니다." 서아 khâu lại patch 태극기 lỏng trên vai 태오. 박기철: "배터리 다 쓰지 마라." Hoàng hôn: đoàn bò lên yên.
> Chức năng: PLAN · Tài nguyên: drone lần bay cuối · Red herring: hướng nam · Open loop: "고개 위에서 마흔 분. 그동안 전차는 잠들고, 드론은 밥을 먹어야 했습니다." → [MID-ROLL 4 · 27:30]

### SC_173 · LOC_008_GOGURYEO_VILLAGE (đuôi K2, rạng sáng D14) · CHAR_003, CHAR_106 · VEH_001, PROP_019 · still_kenburns · 24:00–24:10
[ACTION-VI] Ảnh: nắp buồng động cơ K2 mở, bên trong một đoạn ống đồng đỏ gò cong lồng vào ống cũ, quấn dây da tẩm nhựa thông đen siết chặt; bàn tay băng của 박기철 và bàn tay già của 을보 cùng đặt trên đó; 을보 dốc bát nước lên mối nối — không rỉ; góc khung: phuy 200 L rỗng nằm nghiêng cạnh lò rèn. Ken-burns đẩy vào mối đồng.
[SOUND] nước đổ lên kim loại, chim sớm.
N: 이틀이 지났습니다. 사흘째 새벽, 구리가 물길을 막았습니다. 고구려의 구리와 송진, 대한민국의 냉각수. 을보는 그것을 자기 쇠라고 불렀습니다.

### SC_174 · LOC_008_GOGURYEO_VILLAGE (cạnh K2) · CHAR_003, 조종수 · VEH_001 · video8s · 24:10–24:18
[ACTION-VI] K2 nổ máy — tiếng gầm dội vách núi, chim vụt bay; 박기철 đứng sau đuôi xe nhìn lưới thoát khí: không hơi trắng; ông nhìn màn hình lái qua vai 조종수: vạch nhiệt xanh; gõ hai lần lên giáp.
[SOUND] động cơ K2 gầm ổn định, chim, tay gõ thép.
N: 시동을 걸었습니다. 흰 연기는 나지 않았습니다. 그 55톤이 이제 고개를 넘어야 했습니다.
박기철: 새지 않습니다. 드럼은 비웠습니다. 갑니다.

### SC_175 · LOC_008_GOGURYEO_VILLAGE (sân cạnh kho thóc — bàn cát bùn) · CHAR_001, CHAR_006, CHAR_105, CHAR_005, CHAR_002 (tay/chân) · PROP_015 (mũi tên Goguryeo cắm bàn cát) · still_kenburns · 24:18–24:28
[ACTION-VI] Ảnh: bàn cát đắp bằng bùn trên tấm ván: hai gờ bùn cao là hai vách, giữa là yên ngựa hẹp có một vệt lõm là đường xe; một hòn đá dài dựng đứng ở góc đông-nam là mỏm đá; một que tre cắm chéo vách tây-bắc là đường dê; nhiều đôi giày và một đôi dép rơm (해모루) quanh ván. Ken-burns trượt từ que tre sang hòn đá dựng.
[SOUND] mưa nhỏ, tiếng nói trầm.
N: 석문령. 안장처럼 좁은 고개. 양쪽은 삼십에서 육십 미터 벼랑. 남쪽으로 내려가는 길, 동쪽에서 올라오는 길. 북서쪽 벼랑에 염소 길. 동남쪽에 이백 미터 바위.

### SC_176 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_001 · — · video8s · 24:28–24:36
[ACTION-VI] 한승우 quỳ một gối bên bàn cát, que tre trong tay chỉ đường xe qua yên; ông nói ngắn, nhìn từng người: 백성민, 해모루, 태오, 오태민.
[SOUND] que tre trên bùn, mưa.
N: 계획은 밤이었습니다. 낮에 넘으면 벼랑 위에서 다 보입니다. 밤에는 야시경을 가진 쪽만 봅니다.
한승우: 고개는 밤에 넘는다. 야시경 열둘이 앞장선다.

### SC_177 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_006 · PROP_015 · video8s · 24:36–24:44
[ACTION-VI] 백성민 rút một mũi tên Goguryeo (đầu tam giác) cắm xuống bùn ngay chỗ que tre đường dê — dấu "척후 Goguryeo ở đó"; rồi ông chỉ que sang phía nam bàn cát; giọng phẳng.
[SOUND] mũi tên cắm bùn.
N: 화살은 해모루의 척후라는 뜻이었습니다. 척후 셋은 아무도 없다고 했습니다. 그날 밤 잘못 꽂힌 유일한 화살이었습니다.
백성민: 염소 길은 해모루 척후입니다. 남쪽이 문제입니다.

### SC_178 · LOC_009_SEOKMUN_PASS (đường xe phía đông dưới đèo, rạng sáng D14) · 소년 척후, 2 척후 Tiên Ti · VEH_101, VEH_206, WPN_101 · video8s · 24:44–24:52
[ACTION-VI] 2-BEAT: (a) 24:44–24:48 소년 척후 phi chậm trên đường xe phía đông trong sương sớm; từ rừng thông bên đường, hai kỵ Tiên Ti mũ lông lao ra; (b) 24:48–24:52 hai mũi tên — một rít qua tai, một cắm "턱" vào yên ngựa sau đùi cậu; cậu rạp người xuống cổ ngựa, quay đầu phi ngược về làng, mất hút trong sương. Không thoại.
[SOUND] vó ngựa, dây cung, tên cắm gỗ yên, tiếng hú ngắn.
N: 같은 새벽, 동쪽 길. 소년 척후가 선비 기병 둘을 만났습니다. 화살 둘. 하나는 안장에 박혔습니다. 소년은 돌아서 달렸습니다.

### SC_179 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_105 · EQP_002 · video8s · 24:52–25:00
[ACTION-VI] 해모루 ngồi xổm kiểu kỵ binh, radio trên ngực giáp; ông đặt bàn tay úp lên phía nam bàn cát như đậy nắp; nhìn 한승우.
[SOUND] mưa.
N: 남쪽 입구는 해모루의 삼백이 맡았습니다. 적이 온 곳에서 적이 옵니다. 대개는 그렇습니다.
해모루: 남쪽 입구는 내가 막소. 척후는 남에서 오오.

### SC_180 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_005 · UAV_001 · video8s · 25:00–25:08
[ACTION-VI] 태오 đặt hộp drone xuống cạnh bàn cát, mở nắp: chiếc cuối; cậu bật controller — màn hình pin: 14; cậu giơ một ngón tay — một lần bay.
[SOUND] khóa hộp, mưa.
N: 마지막 비행이었습니다. 전지 열네 분 중 십 분. 그 십 분 동안 고개 전체가 보일 것이었습니다.
장태오: 십 분. 마지막 비행입니다.

### SC_181 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_005, CHAR_001 · — · video8s · 25:08–25:16
[ACTION-VI] 태오 chỉ vào hòn đá dựng ở góc bàn cát — mỏm đá; ngón tay cậu gõ lên đỉnh hòn đá; 한승우 nhìn hòn đá, không nói.
[SOUND] ngón tay gõ đá.
N: 드론과 조종기 사이에는 보이지 않는 줄이 있습니다. 그 줄은 바위에 막힙니다. 높은 곳에 서면 줄이 이어집니다.
장태오: 저 바위 위에서 신호를 잡겠습니다.

### SC_182 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_001 · — · video8s · 25:16–25:24
[ACTION-VI] 한승우 đặt một hòn sỏi vuông ở cuối yên đèo — K2 — và một hòn nhỏ sau nó — xe cối; giơ bàn tay xòe rồi nắm — bốn mươi.
[SOUND] sỏi trên bùn.
N: 그동안 전차는 시동을 끄고 보조동력만 돌립니다. 열과 소리를 숨기기 위해서였습니다. 포탑은 줄에 묶입니다.
한승우: 고개 위에서 마흔 분. 전차는 맨 뒤, 박격포 수레와.

### SC_183 · LOC_008_GOGURYEO_VILLAGE (cạnh K2, đuôi xe) · CHAR_003 · VEH_001 · video8s · 25:24–25:32
[ACTION-VI] Cắt sang đuôi K2 cách bàn cát 20 m: 박기철 mở nắp ổ điện phụ, thử công tắc APU — rít lên rồi tắt; ông nói câu bổ sung về phía bàn cát — không phản đối, chỉ ghi nhận rủi ro; tay vỗ lên giáp xe.
[SOUND] mưa.
N: 줄에 묶인 전차는 쏘지 못합니다. 줄을 뽑는 데 시간이 걸립니다. 박기철은 그 시간을 알았습니다.
박기철: 마흔 분. 그 사이 전차는 줄에 묶입니다.

### SC_184 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_002 · — · video8s · 25:32–25:40
[ACTION-VI] 오태민 bước tới, chỉ vào đầu yên đèo phía tây — muốn đi đầu với đội kính đêm; giọng chắc.
[SOUND] mưa.
N: 오태민은 늘 앞을 원했습니다. 요하에서, 요동성 북문에서. 앞은 그의 자리였습니다. 이번에는 아니었습니다.
오태민: 제가 앞에 서겠습니다.

### SC_185 · LOC_008_GOGURYEO_VILLAGE (bàn cát) · CHAR_001, CHAR_002 · — · video8s · 25:40–25:48
[ACTION-VI] 한승우 không ngẩng lên, chỉ que tre vào hòn sỏi vuông rồi ba chấm bên trái nó — K3; 오태민 im, gật một cái cứng.
[SOUND] que tre.
N: 전차 옆. 가장 큰 것을 지키는 자리였습니다. 오태민에게는 물러나는 것이었고, 한승우에게는 가장 무거운 것을 맡기는 것이었습니다.
한승우: 너는 전차 옆이다. K3 셋.

### SC_186 · LOC_008_GOGURYEO_VILLAGE (hông K2 — phấn vẽ) · CHAR_001 (tay) · VEH_001 · still_kenburns · 25:48–25:58
[ACTION-VI] Ảnh cận: hông tháp K2, phấn trắng vẽ sơ đồ trên giáp ướt — hai đường cong (vách), một đường giữa (yên), chấm và mũi tên (không chữ đọc được); bàn tay 한승우 cầm viên phấn; giọt mưa làm phấn chảy một vệt. Ken-burns trượt theo sơ đồ.
[SOUND] phấn trên thép, mưa.
N: 야시경은 백성민과 앞에. 장태오는 바위 위에, K3 사수와 소총수 둘이 같이. 해모루는 남쪽. 전차는 맨 뒤. 마흔 분. 모든 눈이 남쪽을 보고 있었습니다.

### SC_187 · LOC_009_SEOKMUN_PASS (cửa nam đèo, đường xuống phía nam, trưa D14) · CHAR_105, kỵ Goguryeo, 수 척후 · VEH_101, WPN_201, WPN_101 · video8s · 25:58–26:06
[ACTION-VI] Trưa: 해모루 đã đưa 300 kỵ qua đèo trước để chiếm cửa nam; trên con đường đổ xuống phía nam, 5 kỵ Tùy 척후 đang bò lên gặp hàng kỵ Goguryeo — tên bay, 2 ngã, 3 quay chạy; kỵ Goguryeo đuổi một quãng ngắn. Wide.
[SOUND] dây cung, ngựa, tiếng hô, gió qua đèo.
N: 해모루는 정오에 먼저 고개를 넘어 남쪽 입구에 섰습니다. 거기서 수나라 척후 다섯을 만났습니다. 또 남쪽이었습니다.

### SC_188 · LOC_009_SEOKMUN_PASS (cửa nam) · CHAR_105 · EQP_002, VEH_101 · video8s · 26:06–26:14
[ACTION-VI] 해모루 ghì ngựa, cúi xuống radio trên ngực — lần này giọng thì thầm, đã học; sau lưng, kỵ binh kéo hai con ngựa Tùy về.
[SOUND] PTT, gió.
N: 해모루는 이제 돌에 속삭였습니다. 그의 보고는 정확했습니다. 정확한 보고가 틀린 결론을 굳혔습니다.
해모루: 한 대장, 여기는 해모루. 남쪽에 척후 다섯. 쫓았소.

### SC_189 · LOC_008_GOGURYEO_VILLAGE (cạnh K2, trưa) · CHAR_001, CHAR_006 · EQP_002 · video8s · 26:14–26:22
[ACTION-VI] 소년 척후 phi vào sân, ngựa sùi bọt, xoay yên cho 백성민 xem mũi tên cắm ở yên, giơ hai ngón tay chỉ về đông; 백성민 rút mũi tên, nhìn, gật với 한승우 — kỵ Tiên Ti đi theo đại quân, cột quân ở phía bắc-đông; 한승우 vừa nghe xong radio 해모루, nói hai chữ rồi ra hiệu đoàn chuẩn bị; sau lưng, lính chằng đồ lên K2.
[SOUND] PTT, dây chằng, ngựa.
N: 동쪽 길에 척후 둘. 안장에 박힌 화살이 증거였습니다. 백성민은 그것을 뒤따르는 대열의 척후로 읽었습니다. 북서쪽만 비어 있었습니다.
한승우: 역시 남쪽이다.

### SC_190 · LOC_009_SEOKMUN_PASS (chân đèo phía đông, chiều) · CHAR_001, CHAR_005 · — · video8s · 26:22–26:30
[ACTION-VI] Chiều mưa phùn, đoàn dừng ở chân đèo: 한승우 ngửa cổ nhìn lên — máy low-angle theo mắt ông: vách đá xám-xanh ướt, thông đỏ vặn xoắn, và trên cao 200 m, mỏm đá đỉnh phẳng nhô ra khỏi mây. 태오 đứng cạnh cũng nhìn lên.
[SOUND] gió qua khe, mưa.
N: 바위는 지도에서보다 높았습니다. 이백 미터. 스물한 살이 올라가야 할 높이였습니다.
한승우: 너무 높다.

### SC_191 · LOC_009_SEOKMUN_PASS (chân đèo) · CHAR_005 · UAV_001 (hộp) · video8s · 26:30–26:38
[ACTION-VI] 태오 vẫn ngước nhìn mỏm, siết quai hộp drone, trả lời không nhìn 한승우 — không cãi, chỉ nói điều cậu biết chắc.
[SOUND] gió, quai hộp.
N: 신호는 높아야 잡힙니다. 높은 곳은 멀고, 먼 곳은 위험합니다. 드론 하나를 살리는 자리가 사람 하나를 가장 먼 곳에 두었습니다.
장태오: 신호는 높아야 잡힙니다.

### SC_192 · LOC_009_SEOKMUN_PASS (chân đèo) · CHAR_004, CHAR_005 · PROP_011 · video8s · 26:38–26:46
[ACTION-VI] 서아 kéo vai 태오 lại: miếng patch 태극기 trên vai phải cậu bong một góc; cô rút kim chỉ từ túi quân y, khâu ba mũi nhanh, cắn chỉ; 태오 đứng yên như trẻ con.
[SOUND] chỉ, mưa.
N: 어깨의 태극기가 떨어지려 하고 있었습니다. 윤서아가 세 바늘로 꿰맸습니다. 그 세 바늘은 하루를 버틸 것이었습니다.
윤서아: 떨어지겠다. 잠깐.

### SC_193 · LOC_009_SEOKMUN_PASS (chân đèo, cạnh K2) · CHAR_003, CHAR_005 · VEH_001, UAV_001 · video8s · 26:46–26:54
[ACTION-VI] 박기철 kéo 태오 lại bằng quai hộp drone, nói vào tai cậu nửa đùa nửa lệnh; gõ hai ngón lên nắp hộp.
[SOUND] xích K2 chờ, mưa.
N: 박기철은 전지를 걱정했습니다. 그는 늘 물건을 걱정했습니다. 그것이 그가 사람을 걱정하는 방식이었습니다.
박기철: 야, 태오. 배터리 다 쓰지 마라. 돌아올 몫 남겨.

### SC_194 · LOC_009_SEOKMUN_PASS (chân đèo, đuôi K2) · CHAR_107, CHAR_005 · VEH_001 · video8s · 26:54–27:02
[ACTION-VI] 아리 đã ngồi trên đuôi K2 giữa hộp đạn, chân đung đưa; cô gọi với xuống 태오 đang đi về đội leo mỏm; cậu ngoái lại cười, gõ lên hộp drone hai cái.
[SOUND] mưa, xích.
N: 열다섯 살에게 스물한 살은 그런 사람이었습니다.
아리: 오라버니, 높은 데 조심해요.

### SC_195 · LOC_009_SEOKMUN_PASS (đuôi K2) · CHAR_106, CHAR_003 · VEH_001 · video8s · 27:02–27:10
[ACTION-VI] 을보 leo lên đuôi K2 ngồi cạnh 아리, đặt lòng bàn tay lên tấm lưới buồng động cơ trên chỗ vá đồng — ấm, khô; ông gõ hai cái, nói với 박기철 đang đi bên xe.
[SOUND] xích, tay trên thép.
N: 구리는 뜨거웠습니다. 새지 않았습니다. 을보가 믿는 것은 손이었습니다.
을보: 구리가 버티겠지.

### SC_196 · LOC_009_SEOKMUN_PASS (aerial hoàng hôn) · — · — · still_kenburns · 27:10–27:20
[ACTION-VI] Ảnh aerial hoàng hôn: yên đèo 석문령 nhỏ giữa hai vách đá xám-xanh, ải đá Goguryeo bỏ hoang thấp chắn ngang yên với khoảng hở 5 m, vọng gác tròn đổ ở đầu bắc; đỉnh vách ngậm ánh hổ phách nhạt, yên đã tối, sương chảy qua khe; đường xe ngoằn ngoèo từ chân đèo phía đông bò lên. Ken-burns đẩy chậm vào khoảng hở ải đá.
[SOUND] gió qua khe.
N: 고개 위에는 옛 고구려 관문이 있었습니다. 598년 전쟁 뒤에 버려진 돌담이었습니다. 담 가운데 다섯 걸음 틈. 쇠수레가 겨우 지나는 틈이었습니다.

### SC_197 · LOC_009_SEOKMUN_PASS (đường lên đèo, hoàng hôn) · đại đội, CHAR_105 (xa) · VEH_001, VEH_101 · still_kenburns · 27:20–27:30
[ACTION-VI] Ảnh: đoàn người và ngựa bò lên đường dốc trong ánh hoàng hôn cuối — đội kính đêm đi đầu là bóng nhỏ, hàng lính đi bộ, xe cối do ngựa kéo, K2 sau cùng với 을보/아리 trên đuôi; mây thấp đè xuống yên. Ken-burns trượt lên theo đoàn. Không thoại.
[SOUND] xích, vó ngựa, gió.
N: 고개 위에서 마흔 분. 그동안 전차는 잠들고, 드론은 밥을 먹어야 했습니다.

[MID-ROLL 4 · 27:30]

[Kết thúc Phần 9]

## [Phần 10] 고개의 밤 — 「고개의 밤」 / Trận đánh quyết định  (27:30–34:30) — 6 phase
> Tóm tắt VI: Phase 1 yên đèo: K2 tắt máy (giấu nhiệt/tiếng), APU, dây sạc — tháp "bị cột vào dây"; 태오 lên mỏm với 1 xạ thủ K3 + 2 lính súng trường; drone 10 phút; 80 người trong tối; 해모루 "남쪽 조용하오". Phase 2 tây-bắc: tên cắm váy xích K2; đuốc bừng dọc vách; 2.000 kỵ 탁발흠 đổ xuống đường dê; ngựa bịt tai không hoảng trước K3; 80 người bắn vào đuốc; "박 상사, 시동!" — "충전 중입니다! 이 분!". Phase 3 mục tiêu thật: kỵ Tiên Ti không lao vào K2 — lao lên chân mỏm, đồng bọn từ đỉnh vách thả dây xuống mỏm; 백성민: "목표는 태오다!"; drone quay về mỏm — 태오 thấy chính mình bị vây trên màn hình; 한승우 cử 백성민 + 2 lính lên mỏm; 탁발흠: "쇠수레를 붙들어라. 나는 위로 간다." Phase 4 NARRATOR IM 31:32–33:00: K2 nổ máy, 4 viên vào vách → đá lở bịt cửa tây-bắc — chặn viện binh 탁발흠 nhưng cũng chặn đường 백성민; xạ thủ K3 trúng tên — KIA đầu tiên; "본부, 본부… 잡혔—"; PZF ×1 vào cụm đuốc; kính đêm 백성민 tắt; drone hết 10 phút tự quay về mỏm bằng 4 phút để dành — tay Tiên Ti nhặt; 탁발흠 đếm "넷." Phase 5: 해모루 quay kỵ từ nam phá cửa đông; kỵ Goguryeo cõng thương binh; qua yên lúc rạng đông; 백성민 tới mỏm: hộp drone mất, 2 kính đêm mất, 태오 mất, xác xạ thủ. Phase 6: 오태민 nhặt K3 người chết; vách xa: 탁발흠 trên ngựa, 태오 vắt ngang yên; hắn nhìn — quay đi. Không reo hò.
> Chức năng: BATTLE · Tài nguyên: K2 12→8 · PZF 10→9 · kính đêm 12→10 · drone 1→0 · 94→93 (+1 bị bắt) · K3 −1.000 · Enemy adaptation: đường dê, ngựa bịt tai, nhắm mắt/người điều khiển thay vì xe · Payoff: phân ngựa (P7), "너무 높다" (P9), "살아 있어야 해" (P6, đảo) · Open loop: "94명으로 왔습니다. 이제 92명이 걷고, 한 명이 묻히고, 한 명이 끌려갔습니다."
> [NARRATOR IM LẶNG] 31:32–33:00. Sau mid-roll 4: SC_198 aerial hoàng hôn, không thoại. Veo-stage: đánh dấu 2-BEAT thêm ~12 clip Phase 2–4 (SC_208/210/211/212/216/217/221/223/225/229/231/236) → shot hiệu dụng ~6 s; giữ 8 s ở Phase 5.

### — Phase 1 · 고개 위 / Yên đèo (27:30–28:44) —

### SC_198 · LOC_009_SEOKMUN_PASS (aerial, hoàng hôn cuối) · đại đội · VEH_001, VEH_101 · still_kenburns · 27:30–27:40
[ACTION-VI] Ảnh aerial: ánh hổ phách cuối tắt trên đỉnh vách; dưới yên đèo đã tối, K2 bò qua khúc cua cuối lên yên, hàng người và ngựa trải dài phía trước; ải đá thấp chắn ngang yên, khoảng hở 5 m ngay trước mũi xe; sương trắng chảy từ khe tây-bắc xuống. Ken-burns đẩy chậm vào khoảng hở. Không thoại.
[SOUND] xích K2 dội vách, gió qua khe, vó ngựa.
N: 해가 졌습니다. 고개 위는 이미 밤이었습니다.

### SC_199 · LOC_009_SEOKMUN_PASS (yên đèo, khoảng hở ải đá) · CHAR_003, 조종수 · VEH_001 · video8s · 27:40–27:48
[ACTION-VI] K2 dừng đúng trong khoảng hở ải đá, mũi hướng nam; động cơ tắt — im đột ngột; APU sau tháp rít lên một tông đều; 박기철 đứng cạnh xích, nhìn đồng hồ đeo tay, nói vào radio.
[SOUND] động cơ tắt, APU rì rì, gió.
N: 전차는 잠들었습니다. 열도 소리도 숨겼습니다. 보조동력만 깨어 있었습니다. 지금부터 마흔 분.
박기철: 시동 끕니다. 보조동력 가동.

### SC_200 · LOC_009_SEOKMUN_PASS (đuôi K2) · CHAR_003, 무전병 · VEH_001, EQP_001, EQP_002, UAV_001 · video8s · 27:48–27:56
[ACTION-VI] Dây sạc từ đuôi K2 chạy trên đá xếp khan cổ tới một tấm bạt: 7 kính đêm đang sạc, đèn đỏ hàng dài (5 chiếc đang dùng: 백성민 + 2 lính đi đầu + 태오 + xạ thủ K3 trên mỏm); 4 radio (drone đang bay bằng pin 14 phút — không sạc); 무전병 cắm nốt dây cuối; 박기철 bấm đồng hồ.
[SOUND] đèn sạc "띡, 띡", APU.
N: 21세기의 줄이 7세기의 돌담 위를 지나갔습니다. 야시경, 무전기. 모두 한 통에서 밥을 먹었습니다.
박기철: 마흔 분. 지금부터.

### SC_201 · LOC_009_SEOKMUN_PASS (đường dốc lên mỏm đá, chạng vạng) · CHAR_005, K3 사수, 2 병사 · UAV_001, WPN_003, EQP_001 · video8s · 27:56–28:04
[ACTION-VI] Đường mòn đá dốc bám vách đông-nam lên mỏm: 태오 đi trước với hộp drone trên lưng, kính đêm gắn trên mũ, dây thừng buộc ngang người; sau cậu, K3 사수 vác súng máy (kính đêm trên mũ), hai lính súng trường không kính chốt sau; đá vụn lăn; xa dưới, yên đèo là những chấm đỏ nhỏ của đèn sạc.
[SOUND] đá lăn, thở, dây thừng.
N: 이백 미터. 넷이 올라갔습니다. 조종병 하나, K3 사수 하나, 소총수 둘. 위에서 보면 고개 전체가 손바닥 같을 것이었습니다.

### SC_202 · LOC_009_SEOKMUN_PASS (đỉnh mỏm đá, đêm) · CHAR_005 · UAV_001, EQP_002 · video8s · 28:04–28:12
[ACTION-VI] Đỉnh mỏm phẳng 10×10 m: 태오 quỳ, drone cất cánh khỏi tay biến vào đêm; màn hình controller: pin 14 → cậu đặt hẹn bay 10, để dành 4 phút quay về (lời 박기철); K3 사수 đặt súng hướng xuống con đường vừa leo; 태오 bấm radio.
[SOUND] rotor nhỏ dần, PTT, gió trên cao.
N: 마지막 비행이 시작되었습니다. 열네 분 중 십 분. 고개는 조용했습니다.
장태오: 천둥 지휘, 여기는 바위. 드론 이륙, 십 분.

### SC_203 · LOC_009_SEOKMUN_PASS (yên đèo — POV kính đêm) · CHAR_006 · EQP_001, VEH_001 · video8s · 28:12–28:20
[ACTION-VI] POV kính đêm 백성민 xanh lục nhiễu hạt: yên đèo trơ đá, ải đá xếp khan, khối K2 trong khoảng hở, hàng người ngồi tựa tường sáng nhạt; ông xoay sang trái — vách tây-bắc đen đặc, sương mỏng hơn lúc chiều, đường dê là vệt xám mờ, trống. Không thoại.
[SOUND] kính đêm rít, gió, APU xa.
N: 백성민은 북서쪽을 보았습니다. 안개는 저녁보다 엷었습니다. 염소 길이 보였습니다. 비어 있었습니다. 그는 남쪽으로 눈을 돌렸습니다.

### SC_204 · LOC_009_SEOKMUN_PASS (yên đèo, dọc ải đá) · đại đội, CHAR_002, CHAR_106, CHAR_107, CHAR_004 · VEH_001, WPN_003 · video8s · 28:20–28:28
[ACTION-VI] Wide thấp trong tối (chỉ đèn sạc đỏ và mây sáng nhạt): 80 người ngồi dọc chân ải đá, súng trên đùi, không ai nói; 오태민 sau khẩu K3 trên đống đá phía tây với hai khẩu K3 nữa cách 20 m; 을보 và 아리 ngồi giữa hai xích K2 dưới gầm; 서아 với túi quân y bên bánh xe.
[SOUND] gió, APU, xa xa tiếng ngựa.
N: 여든 명이 어둠 속에 앉았습니다. 총은 무릎 위에. 눈은 남쪽에. 아무도 말하지 않았습니다. 기다리는 것은 싸움이 아니라 전기였습니다.

### SC_205 · LOC_009_SEOKMUN_PASS (cửa nam đèo, đêm) · CHAR_105 · EQP_002, VEH_101 · video8s · 28:28–28:36
[ACTION-VI] Cửa nam: 해모루 trên ngựa giữa hàng kỵ binh im lặng, nhìn xuống con đường đổ về nam; ông cúi đầu thì thầm vào radio.
[SOUND] PTT, ngựa thở, gió.
해모루: 한 대장, 여기는 해모루. 남쪽 조용하오.

### SC_206 · LOC_009_SEOKMUN_PASS (mỏm đá — màn hình drone) · CHAR_005 · UAV_001 · video8s · 28:36–28:44
[ACTION-VI] Màn hình drone nhiệt: từ trên cao, yên đèo là vệt xám, K2 là khối trắng nóng, 80 chấm ấm dọc tường; 태오 lia sang vách tây-bắc: đường dê xám, không chấm nóng; lia bắc — trống; đồng hồ bay: 8:40 còn lại. Cận ngón tay cậu và màn hình.
[SOUND] rotor qua loa, bíp.
N: 팔 분 사십 초. 하늘 눈은 아무것도 보지 못했습니다. 보이지 않는 것은 없는 것이 아니었습니다. 벼랑 뒤는 열에 잡히지 않았습니다.

### — Phase 2 · 북서쪽 / Tây-bắc (28:44–29:56) —

### SC_207 · LOC_009_SEOKMUN_PASS (yên đèo, hông K2) · CHAR_003 · VEH_001, PROP_015 · video8s · 28:44–28:52
[ACTION-VI] Một mũi tên từ bóng tối bay tới cắm "캉" vào váy xích K2 ngay cạnh đầu 박기철 — lông vũ rung; ông khựng, nhìn mũi tên, nhìn lên vách tây-bắc; cả hàng người dọc tường ngẩng đầu cùng lúc.
[SOUND] tên đập thép, im, gió.
N: 첫 화살은 북서쪽에서 왔습니다.

### SC_208 · LOC_009_SEOKMUN_PASS (vách tây-bắc, đêm) · kỵ Tiên Ti · VEH_206, PROP_016, PROP_017 · video8s · 28:52–29:00
[ACTION-VI] Vách tây-bắc đen: một đuốc bừng lên trên đường dê — rồi mười, rồi hàng trăm, nối nhau thành chuỗi lửa ngoằn ngoèo từ đỉnh vách xuống; trống da nổi dồn dập; sương ánh cam. Low-angle từ yên.
[SOUND] trống dồn, đuốc bùng, tiếng hú.
N: 염소 길이 불로 그려졌습니다. 이천 개의 횃불이었습니다. 말똥의 주인이 나타났습니다.

### SC_209 · LOC_009_SEOKMUN_PASS (yên đèo) · CHAR_006 · EQP_001, EQP_002, VEH_206 · video8s · 29:00–29:08
[ACTION-VI] 백성민 đứng bật dậy, kính đêm dán mắt — POV xanh lục: chuỗi đuốc lóa trắng, dưới đuốc là ngựa và người đổ xuống đường dê thành dòng; ông gào vào radio — lần đầu ông gào.
[SOUND] PTT, trống, hú.
백성민: 북서! 염소 길! 기병!

### SC_210 · LOC_009_SEOKMUN_PASS (đống đá phía tây yên) · CHAR_002, xạ thủ K3 · WPN_003, VEH_206 · video8s · 29:08–29:16
[ACTION-VI] 오태민 kéo cò K3 — tracer đỏ quét thành dải lên vách tây-bắc vào chuỗi đuốc; hai khẩu K3 bên cạnh nổ theo; đuốc trên đường dê rơi, lăn; nhưng dòng lửa vẫn chảy xuống.
[SOUND] ba khẩu K3 quét dài, dội vách, đuốc rơi.
N: 요하에서 총소리는 말을 미치게 했습니다. 요동성에서도 그랬습니다. 이번에는 아니었습니다.

### SC_211 · LOC_009_SEOKMUN_PASS (chân đường dê, mép yên) · kỵ Tiên Ti · VEH_206, PROP_016 · video8s · 29:16–29:24
[ACTION-VI] Cận ngựa Tiên Ti lao xuống đoạn cuối đường dê vào yên đèo: tai buộc vải, mắt mở, không dựng, không hí; kỵ sĩ rạp trên yên, cung giương; tracer bay qua đầu — ngựa không đổi bước; hàng sau nối hàng trước đổ vào yên như nước vỡ bờ.
[SOUND] vó ngựa dồn, tracer rít, trống.
N: 귀를 막은 말은 천둥을 듣지 못했습니다. 듣지 못하는 말은 달렸습니다. 탁발흠은 요하에서 배운 것을 석문령에서 썼습니다.

### SC_212 · LOC_009_SEOKMUN_PASS (dọc ải đá) · đại đội · WPN_001, VEH_206 · video8s · 29:24–29:32
[ACTION-VI] 80 người quỳ sau ải đá bắn vào đuốc — chớp lửa đầu nòng liên tiếp dọc tường; trên vách, đuốc tắt từng cụm; nhưng trong bóng tối dưới vách, tiếng vó ngựa vẫn đổ; tên từ tối rơi xuống yên cắm vào đá, một mũi cắm vào bao cát cạnh mặt lính.
[SOUND] K2C1 hàng loạt, tên cắm, trống.
N: 횃불을 쏘면 횃불이 꺼졌습니다. 꺼진 횃불 밑에서 말은 계속 왔습니다. 야시경을 가진 사람은 셋이었습니다. 나머지는 빛을 쏘았습니다.

### SC_213 · LOC_009_SEOKMUN_PASS (đường dê, đoạn trên) · CHAR_205, 선비 부장 · VEH_206, PROP_016 · video8s · 29:32–29:40
[ACTION-VI] Đoạn trên đường dê: 탁발흠 ghì ngựa dừng bên vách, không đuốc, để dòng kỵ binh chảy qua; hắn ngẩng lên — không nhìn K2 dưới yên — nhìn mỏm đá đông-nam đối diện, nơi một đốm sáng nhỏ (màn hình controller) nhấp nháy; hắn giơ tay chỉ mỏm cho 부장.
[SOUND] vó ngựa chảy qua, trống, gió.
N: 탁발흠은 쇠수레를 보지 않았습니다. 그는 바위를 보았습니다. 바위 위에 작은 빛이 있었습니다. 쇠새를 부리는 자의 빛이었습니다.

### SC_214 · LOC_009_SEOKMUN_PASS (hông K2) · CHAR_001 · VEH_001, EQP_002 · video8s · 29:40–29:48
[ACTION-VI] 한승우 chạy tới hông K2, đập tay lên giáp, gào với 박기철 đang ở đuôi xe giữa mớ dây sạc; tên cắm xuống đá quanh chân ông.
[SOUND] tay đập thép, tên cắm, K3 xa.
한승우: 박 상사, 시동!

### SC_215 · LOC_009_SEOKMUN_PASS (đuôi K2) · CHAR_003 · VEH_001, EQP_001 · video8s · 29:48–29:56
[ACTION-VI] 박기철 quỳ giữa dây sạc, nhìn đồng hồ, nhìn hàng kính đêm đèn đỏ chưa xanh; ông gào lại — hai ngón tay giơ lên; tay kia đã cầm sẵn đầu dây để giật.
[SOUND] APU, đèn sạc, K3, trống.
N: 이 분. 야시경 일곱 개가 아직 밥을 먹고 있었습니다. 그날 밤 가장 비싼 이 분이었습니다.
박기철: 충전 중입니다! 줄 뽑는 데 이 분!

### — Phase 3 · 진짜 목표 / Mục tiêu thật (29:56–31:32) —

### SC_216 · LOC_009_SEOKMUN_PASS (yên đèo, chân mỏm đá) · kỵ Tiên Ti · VEH_206 · video8s · 29:56–30:04
[ACTION-VI] Kỵ Tiên Ti tràn vào yên — nhưng dòng chính không quay về phía K2 và ải đá; họ phóng chéo qua yên tới chân mỏm đá đông-nam, nhảy khỏi ngựa, bám đá leo lên con đường mòn 태오 vừa đi; ngựa mất chủ chạy tán loạn giữa yên.
[SOUND] vó ngựa, giày da trên đá, hú.
N: 그들은 쇠수레로 오지 않았습니다. 돌담으로도 오지 않았습니다. 바위로 갔습니다.

### SC_217 · LOC_009_SEOKMUN_PASS (đỉnh vách trên mỏm đá) · kỵ Tiên Ti (đi bộ) · VEH_206 · video8s · 30:04–30:12
[ACTION-VI] Trên đỉnh vách phía trên mỏm đá — nơi đường dê có nhánh vòng lên — hàng chục bóng Tiên Ti đi bộ, không đuốc, thả dây thừng xuống mặt mỏm; một người trượt xuống dây đầu tiên. High-angle từ đỉnh vách nhìn xuống mỏm nhỏ sáng nhạt.
[SOUND] dây thừng, gió trên cao, xa xa súng.
N: 염소 길은 하나가 아니었습니다. 위로 갈라진 가지가 있었습니다. 그 가지는 바위 위 벼랑으로 이어졌습니다. 탁발흠은 이틀 전 밤에 그 가지를 걸어보았습니다.

### SC_218 · LOC_009_SEOKMUN_PASS (yên đèo) · CHAR_006 · EQP_001 · video8s · 30:12–30:20
[ACTION-VI] 백성민 xoay kính đêm về mỏm đá — POV xanh: bóng người bám vách leo lên từ dưới, bóng người tụt dây từ trên; ông gào — không vào radio, gào bằng cổ họng cho cả yên nghe.
[SOUND] gào, K3, trống.
백성민: 목표는 태오다!

### SC_219 · LOC_009_SEOKMUN_PASS (mỏm đá — màn hình drone) · CHAR_005 · UAV_001 · video8s · 30:20–30:28
[ACTION-VI] Màn hình drone nhiệt: 태오 kéo drone quay về mỏm — hình ảnh từ trên cao: một mặt phẳng nhỏ với 4 chấm nóng (chính họ), và quanh mặt phẳng, từ dưới lên và từ trên xuống, hàng chục chấm nóng đang bám vào. Cận mặt 태오 trong ánh màn hình: cậu đang nhìn chính mình bị vây.
[SOUND] rotor qua loa, thở gấp, gió.
N: 장태오는 화면에서 자신을 보았습니다. 작은 점 넷. 그 둘레로 올라오는 점들. 하늘 눈이 마지막으로 본 것은 자기 주인이었습니다.

### SC_220 · LOC_009_SEOKMUN_PASS (mỏm đá) · CHAR_005 · EQP_002 · video8s · 30:28–30:36
[ACTION-VI] 태오 bấm radio, giọng vỡ nhưng còn giữ được mẫu câu; tay kia vẫn giữ cần drone; K3 사수 sau lưng cậu đang xoay súng về mép mỏm.
[SOUND] PTT, K3 lên đạn.
장태오: 천둥 지휘, 여기는 바위. 올라옵니다. 사방입니다.

### SC_221 · LOC_009_SEOKMUN_PASS (mỏm đá, mép nam) · K3 사수 · WPN_003, VEH_206 · video8s · 30:36–30:44
[ACTION-VI] K3 사수 nằm ở mép mỏm bắn xuống con đường mòn — chớp lửa đầu nòng soi mặt đá và những bóng Tiên Ti bám vách rơi ngược; hai lính súng trường bắn lên phía đỉnh vách nơi dây thừng buông xuống; tên cắm quanh họ.
[SOUND] K3 dội đá, tên cắm, thét.
N: K3 사수는 스물세 살이었습니다. 그는 길을 막았습니다. 아래에서 오는 길이었습니다. 위에서 오는 길은 총 하나로 막을 수 없었습니다.

### SC_222 · LOC_009_SEOKMUN_PASS (hông K2) · CHAR_001, CHAR_006 · EQP_002 · video8s · 30:44–30:52
[ACTION-VI] 한승우 nắm vai 백성민, chỉ về mỏm đá, hét; 백성민 gật, vẫy hai lính có kính đêm bên cạnh; ba người lao đi.
[SOUND] hét, K3, trống, tên.
N: 한승우는 전차 곁을 떠나지 않았습니다. 그는 갈 수 있는 사람을 보냈습니다. 밤눈을 가진 셋이었습니다.
한승우: 백 중사, 바위로! 둘 데려가!

### SC_223 · LOC_009_SEOKMUN_PASS (yên đèo, chạy qua) · CHAR_006, 2 병사 · EQP_001, WPN_001 · video8s · 30:52–31:00
[ACTION-VI] Ba người chạy chéo qua yên trong tối giữa ngựa mất chủ và tên rơi; một lính trúng tên ở cánh tay, loạng choạng, chạy tiếp; 백성민 dẫn đầu, kính đêm trên mắt, tới chân đường mòn lên mỏm. Tracking bên hông, rung.
[SOUND] chạy trên đá, tên, ngựa hí, thở.
N: 이백 미터 아래에서 이백 미터 위로. 걸어서 이십 분. 뛰어서 십 분. 그들에게는 십 분이 없었습니다.

### SC_224 · LOC_009_SEOKMUN_PASS (đường dê, đoạn trên) · CHAR_205, 선비 부장 · VEH_206 · video8s · 31:00–31:08
[ACTION-VI] 탁발흠 nhảy khỏi ngựa trên đường dê, ném cương cho 부장, nói cộc hai câu; hắn bám vách rẽ lên nhánh trên về phía đỉnh vách mỏm đá, cung trên lưng.
[SOUND] cương ngựa, đá, gió.
N: 그는 스스로 올라갔습니다. 늘 그랬습니다. 요하에서 언덕에 올라 세었고, 골짜기에서 벼랑에 올라 보았습니다. 이번에는 잡으러 올라갔습니다.
탁발흠: 쇠수레를 붙들어라. 나는 위로 간다.

### SC_225 · LOC_009_SEOKMUN_PASS (dọc ải đá) · CHAR_004, 병사 bị thương · PROP_009 · video8s · 31:08–31:16
[ACTION-VI] Cung thủ Tiên Ti trên vách bắn trùm xuống yên; một lính bên ải đá trúng tên ở vai ngã ngửa; 서아 bò tới, kéo anh ta sau tường đá, kéo cắt áo, băng — mặt không đổi, tên cắm xuống đá cạnh cô.
[SOUND] tên hàng loạt, kéo cắt, rên.
N: 벼랑 위의 활은 돌담을 넘어왔습니다. 방탄복은 가슴을 가렸습니다. 어깨와 팔은 가리지 못했습니다. 요하에서 배운 것을 그날 밤 다시 배웠습니다.

### SC_226 · LOC_009_SEOKMUN_PASS (đuôi K2) · CHAR_003 · VEH_001, EQP_001 · video8s · 31:16–31:24
[ACTION-VI] 박기철 nhìn đồng hồ — hết hai phút; ông giật cả bó dây sạc khỏi ổ đuôi xe bằng một động tác, đập tay lên nắp ổ điện, gào vào cửa lái; kính đêm trên bạt: 5 đèn xanh, 2 đèn đỏ.
[SOUND] dây giật, nắp đập, gào.
N: 일곱 개 중 다섯 개가 찼습니다. 나머지 둘은 사십 퍼센트로 밤을 넘겨야 했습니다. 박기철은 줄을 뽑았습니다.
박기철: 됐다! 시동!

### SC_227 · LOC_009_SEOKMUN_PASS (K2 trong khoảng hở ải đá) · CHAR_001, 조종수 · VEH_001, EQP_002 · video8s · 31:24–31:32
[ACTION-VI] K2 nổ máy — tiếng gầm trùm cả yên đèo, khói phụt từ đuôi; tháp pháo xoay chậm sang trái, nòng nâng lên hướng vách tây-bắc nơi chuỗi đuốc vẫn chảy xuống đường dê; 한승우 đứng sát hông xe, radio áp miệng.
[SOUND] động cơ K2 gầm, tháp pháo xoay, trống.
N: 전차가 깨어났습니다. 남은 포탄은 열두 발이었습니다.
한승우: 천둥 1, 염소 길 위 벼랑. 네 발.

[NARRATOR IM LẶNG — 31:32 → 33:00]

### — Phase 4 · 실수와 자원 / Sai sót & tài nguyên (31:32–33:00) — NARRATOR IM —

### SC_228 · LOC_009_SEOKMUN_PASS (K2 — bắn) · 포수 · VEH_001 · video8s · 31:32–31:40
[ACTION-VI] 2-BEAT: (a) 31:32–31:36 cận trong xe: màn hình pháo thủ hồng ngoại — vách đá trắng nóng phía trên miệng đường dê, chữ thập ngắm; bộ đếm "잔탄 12"; tay bóp cò; (b) 31:36–31:40 ngoài: K2 khai hỏa — chớp lửa đầu nòng trùm cả yên đèo trong một phần giây, sóng xung kích thổi bụi, đá; vách tây-bắc lóe.
[SOUND] 120mm nổ đanh, dội vách ba lần, tai ù.

### SC_229 · LOC_009_SEOKMUN_PASS (vách tây-bắc) · — · VEH_001 (off), VEH_206 · video8s · 31:40–31:48
[ACTION-VI] 2-BEAT: (a) viên hai — vách đá phía trên miệng đường dê vỡ toác, đá tảng bung ra lăn xuống; (b) viên ba — cả một mảng vách nứt, bụi trắng phun, đuốc trên đường dê chao đảo, ngựa và người trên đoạn dưới ngoái lên.
[SOUND] hai tiếng 120mm, đá vỡ, gầm.

### SC_230 · LOC_009_SEOKMUN_PASS (vách tây-bắc — đá lở) · kỵ Tiên Ti · VEH_206, PROP_016 · video8s · 31:48–31:56
[ACTION-VI] Viên bốn — mảng vách sụp: một thác đá xám-xanh đổ xuống lấp miệng đường dê, đuốc bị chôn tắt hàng loạt, bụi bốc cam trong ánh đuốc còn lại, tiếng gầm kéo dài; đống đá cao dần thành bức tường 6 m. Insert 2 s: bộ đếm trong xe "잔탄 08".
[SOUND] 120mm, đá lở kéo dài, đuốc tắt, ngựa hí.

### SC_231 · LOC_009_SEOKMUN_PASS (đường dê phía trên đá lở) · kỵ Tiên Ti · VEH_206, PROP_016 · video8s · 31:56–32:04
[ACTION-VI] Trên đường dê, phía trên đống đá: hàng trăm đuốc dồn cục, ngựa quay ngang, không xuống được; dưới yên, số kỵ Tiên Ti đã vào (vài trăm) ngoái lại nhìn đường về bị bịt — họ bị cắt. Cận: 탁발흠 trên nhánh trên, quay sang 부장, giơ bốn ngón tay — đếm sấm. High-angle.
[SOUND] hú, ngựa, đá lăn rải rác.
탁발흠: 넷.

### SC_232 · LOC_009_SEOKMUN_PASS (đường mòn lên mỏm, đoạn dưới) · CHAR_006, 2 병사 · EQP_001 · video8s · 32:04–32:12
[ACTION-VI] 백성민 leo đường mòn — bỗng đá tảng từ rìa đá lở văng qua, đập nát đoạn đường mòn ngay trước mặt ông, bụi trùm; ông ngã ngửa vào lính sau; trước mặt: đống đá vụn chắn lối lên mỏm. Ông gào tên cậu bé lên vách.
[SOUND] đá đập, bụi, gào.
백성민: 태오!

### SC_233 · LOC_009_SEOKMUN_PASS (đỉnh mỏm đá) · K3 사수, CHAR_005 · WPN_003 · video8s · 32:12–32:20
[ACTION-VI] Trên mỏm: K3 사수 quỳ bắn lên đỉnh vách — hai mũi tên từ trên cắm vào vai và ngực trên áo giáp mép hở; anh ngã nghiêng lên mặt đá, khẩu K3 trượt khỏi tay; 태오 quay lại thấy, rời cần drone. Không cận vết thương.
[SOUND] tên cắm, thân ngã, K3 im.

### SC_234 · LOC_009_SEOKMUN_PASS (đỉnh mỏm đá) · CHAR_005, kỵ Tiên Ti (đi bộ) · EQP_002 · video8s · 32:20–32:28
[ACTION-VI] 태오 bấm radio, câu nói đứt giữa chừng — bàn tay Tiên Ti từ sau túm cổ áo, một cánh tay khác đập vào tay cầm radio; radio rơi xuống đá, đèn còn sáng; cậu bị kéo ngửa ra sau khỏi khung.
[SOUND] PTT, tiếng kéo, radio rơi, im.
장태오: 본부, 본부… 잡혔—

### SC_235 · LOC_009_SEOKMUN_PASS (hông K2) · CHAR_001 · EQP_002 · video8s · 32:28–32:36
[ACTION-VI] Cận 한승우: radio áp tai, nghe — im; ông bấm PTT, mở miệng, không nói được gì; bấm lần nữa; xung quanh chớp lửa và tiếng gầm nhưng máy chỉ giữ mặt ông. Không thoại.
[SOUND] PTT hai lần, nhiễu, im giữa tiếng trận xa.

### SC_236 · LOC_009_SEOKMUN_PASS (ải đá, phía tây) · PZF 사수, CHAR_002 · WPN_005, VEH_206 · video8s · 32:36–32:44
[ACTION-VI] 오태민 vỗ vai xạ thủ PZF bên cạnh, chỉ lên cụm đuốc cung thủ đông nhất trên vách; xạ thủ quỳ, ống trên vai — phóng; quả đạn vạch sáng lên vách, nổ giữa cụm đuốc — đuốc văng, đá vụn.
[SOUND] PZF "펑", nổ dội, đuốc rơi.

### SC_237 · LOC_009_SEOKMUN_PASS (đường mòn, chân đá lở) · CHAR_006 · EQP_001 · video8s · 32:44–32:52
[ACTION-VI] POV kính đêm 백성민 xanh lục — hình ảnh chớp, tối dần, một vệt nhiễu, rồi đen; cắt ra ngoài: ông giật kính khỏi mũ, ném vào ngực áo, bám đá bằng tay trần leo vòng qua mép đống đá lở trong tối.
[SOUND] kính đêm tắt "틱", đá, thở.

### SC_238 · LOC_009_SEOKMUN_PASS (đỉnh mỏm đá) · kỵ Tiên Ti, CHAR_005 (bị kéo) · UAV_001 · video8s · 32:52–33:00
[ACTION-VI] Trên mỏm, đuốc Tiên Ti đã bật: drone tự hạ xuống từ đêm — hết 10 phút bay, nó tự quay về bằng 4 phút pin 태오 để dành, không ai điều khiển — đèn nhấp nháy, đáp đúng chỗ nó cất cánh; một bàn tay Tiên Ti đeo vòng đồng chộp lấy nó khi rotor còn quay; góc khung: 태오 bị hai người kéo bằng dây lên phía đỉnh vách, mũ và áo giáp đã bị lột, chỉ còn áo quân phục.
[SOUND] rotor hạ, tay chộp, dây thừng, đuốc.

### — Phase 5 · 고구려가 짊어지다 / Goguryeo gánh (33:00–33:56) —

### SC_239 · LOC_009_SEOKMUN_PASS (cửa nam đèo) · CHAR_105 · EQP_002, VEH_101, PROP_018 · video8s · 33:00–33:08
[ACTION-VI] 해모루 trên ngựa ở cửa nam, tay đè radio trên ngực, mặt nghiêng nghe; ông rút tù và, rúc ba hồi, quay ngựa — 300 kỵ quay theo ông ngược lên yên rồi vòng về cửa đông.
[SOUND] PTT, tù và ba hồi, vó ngựa dồn.
N: 남쪽은 조용했습니다. 해모루는 남쪽을 버렸습니다. 말하는 돌이 동쪽 문이 막혔다고 했습니다.
해모루: 한 대장, 여기는 해모루. 동문을 치오!

### SC_240 · LOC_009_SEOKMUN_PASS (cửa đông đèo, đêm) · kỵ Goguryeo, kỵ Tiên Ti · VEH_101, VEH_206, PROP_012 · video8s · 33:08–33:16
[ACTION-VI] Cửa đông — nơi một toán Tiên Ti đã vòng xuống chặn đường xe phía sau đại đội: 300 kỵ Goguryeo giáp lamellar đâm thẳng vào sườn họ, cờ 삼족오, giáo dài; kỵ Tiên Ti nhẹ vỡ, chạy lên scree. Wide.
[SOUND] va chạm, giáo, ngựa, tù và.
N: 동쪽 문은 선비 기병 이백이 막고 있었습니다. 개마무사 삼백이 그 이백을 옆에서 쳤습니다. 이 땅의 기병이 이 땅의 고개를 열었습니다.

### SC_241 · LOC_009_SEOKMUN_PASS (yên đèo, scree phía bắc) · kỵ Tiên Ti, đại đội, kỵ Goguryeo · VEH_206, VEH_001 · video8s · 33:16–33:24
[ACTION-VI] Kỵ Tiên Ti còn trong yên — bị đá lở cắt đường về, K2 và 80 người trước mặt, kỵ Goguryeo từ đông tới — bỏ ngựa leo lên sườn scree phía bắc trong tối, đá lăn; vài người trượt ngã; K3 quét theo sườn dốc rồi ngừng — 오태민 giơ tay ngừng bắn.
[SOUND] đá lăn, K3 loạt ngắn rồi im, ngựa mất chủ.
N: 고개 안에 남은 선비 기병은 벼랑을 기어 올라갔습니다. 오태민은 쫓지 않았습니다. 쫓지 않는 것을 그는 이제 알았습니다.

### SC_242 · LOC_009_SEOKMUN_PASS (dọc ải đá, tảng sáng) · kỵ Goguryeo, CHAR_004, thương binh · VEH_101, PROP_009 · video8s · 33:24–33:32
[ACTION-VI] Trời tảng sáng xám: kỵ Goguryeo xuống ngựa, cúi nhấc lính Hàn bị thương lên yên — người trúng tên vai, người trúng tên tay; 서아 đỡ chân một người lên, siết garô lần cuối; kỵ sĩ Goguryeo dắt ngựa đi bộ.
[SOUND] ngựa, rên nhẹ, mưa bắt đầu.
N: 다친 사람은 여섯이었습니다. 고구려 기병이 그들을 말에 태웠습니다. 기병은 걸었습니다. 사흘째 밤에도 그랬고, 이 밤에도 그랬습니다.

### SC_243 · LOC_009_SEOKMUN_PASS (khoảng hở ải đá, rạng đông) · đại đội, CHAR_106, CHAR_107 · VEH_001 · video8s · 33:32–33:40
[ACTION-VI] Rạng đông xám, mưa: K2 bò qua khoảng hở ải đá về phía nam, đuôi xe chở 을보 ôm 아리, hai ông cháu nhìn ngược lại mỏm đá; hàng người đi sau, đầu cúi; đống đá lở khổng lồ bên trái khung còn bốc bụi.
[SOUND] xích, mưa, gió.
N: 해가 뜨기 전에 전차는 고개를 넘었습니다. 남쪽으로. 살수로. 뒤에 남은 것을 세는 일은 아직이었습니다.

### SC_244 · LOC_009_SEOKMUN_PASS (đỉnh mỏm đá, rạng đông) · CHAR_006, K3 사수 (xác) · WPN_003, EQP_001 (mount trống) · video8s · 33:40–33:48
[ACTION-VI] 백성민 nhô lên mép mỏm, tay trầy máu; mặt mỏm: đuốc tắt, dây thừng buông từ đỉnh vách, hộp drone không còn, controller không còn; xác K3 사수 nằm nghiêng, khẩu K3 bên cạnh; mũ 태오 lăn ở góc — ngàm gắn kính đêm trên mũ trống; ông đứng thở.
[SOUND] mưa, gió, thở.
N: 바위 위에는 아무것도 없었습니다. 드론도, 조종기도, 야시경 둘도, 장태오도. 있는 것은 사수와 그의 총, 그리고 빈 철모 하나였습니다.

### SC_245 · LOC_009_SEOKMUN_PASS (đỉnh mỏm đá) · CHAR_006 · EQP_002 · video8s · 33:48–33:56
[ACTION-VI] 백성민 nhặt mũ 태오, xoay nhìn ngàm trống, cầm radio rơi trên đá (đèn vẫn sáng); ông bấm, nói bằng giọng điện tín — nhưng ngắt một lần ở giữa.
[SOUND] PTT, mưa.
백성민: 천둥 지휘, 여기는 수색. 태오… 없습니다. 사수 전사.

### — Phase 6 · 새벽 / Kết (33:56–34:30) —

### SC_246 · LOC_009_SEOKMUN_PASS (yên đèo phía nam, bình minh xám) · CHAR_002, kỵ Goguryeo · WPN_003 · video8s · 33:56–34:04
[ACTION-VI] Kỵ Goguryeo đưa xác K3 사수 bọc poncho xuống ngựa đặt lên nền đất bằng phía nam yên; bên cạnh, khẩu K3 dính máu; 오태민 đứng nhìn một lúc, cúi xuống nhặt khẩu K3, lau bằng tay áo, đeo lên vai cạnh súng mình. Máy đẩy chậm vào mặt ông.
[SOUND] mưa, dây súng.
N: 오태민은 그 총을 들었습니다. 그는 그 총을 살수까지 가져갈 것이었습니다.

### SC_247 · LOC_009_SEOKMUN_PASS (đỉnh vách xa, bình minh) · CHAR_205, CHAR_005 (bị bắt), kỵ Tiên Ti · VEH_206, UAV_001 (hộp) · video8s · 34:04–34:12
[ACTION-VI] Trên đỉnh vách xa phía tây-bắc, ngược sáng bình minh xám: 탁발흠 trên ngựa, mũ lông cáo; vắt ngang yên trước hắn — 태오, tay trói sau lưng, không mũ, không giáp, không giày; một kỵ sĩ bên cạnh ôm hộp drone olive. Hắn nhìn xuống yên đèo — nhìn K2, nhìn đống đá — rồi quay ngựa, biến sau đỉnh. Static, xa.
[SOUND] gió, mưa.
N: 벼랑 위에 그가 있었습니다. 안장 위에 장태오가 있었습니다. 탁발흠은 아래를 한 번 보았습니다. 그리고 돌아섰습니다. 그는 원하는 것을 가졌습니다.

### SC_248 · LOC_009_SEOKMUN_PASS (yên đèo phía nam) · CHAR_001 · EQP_002 · video8s · 34:12–34:20
[ACTION-VI] 한승우 ngẩng nhìn đỉnh vách nơi bóng ngựa vừa khuất; radio còn trong tay; ông không nói, không ra lệnh; 백성민 xuống tới cạnh ông, đưa chiếc mũ trống; ông cầm, nhìn ngàm kính đêm trống; xung quanh không một tiếng reo. Máy tĩnh.
[SOUND] mưa, xích K2 xa, im.
N: 아무도 소리치지 않았습니다. 고개는 넘었습니다. 이긴 것이었습니다. 그렇게 부르는 사람은 없었습니다.

### SC_249 · LOC_009_SEOKMUN_PASS (aerial bình minh mưa) · đại đội · VEH_001, VEH_101 · still_kenburns · 34:20–34:30
[ACTION-VI] Ảnh aerial: yên đèo trong mưa xám, đống đá lở 6 m bịt cửa tây-bắc, ải đá, xác ngựa, tên gãy, đuốc tắt; phía nam, một cột nhỏ — người, ngựa, K2 — bò xuống dốc về phía nam; trên mỏm đá, một chấm người đứng một mình. Ken-burns kéo ra rất chậm.
[SOUND] mưa, gió.
N: 94명으로 왔습니다. 이제 92명이 걷고, 한 명이 묻히고, 한 명이 끌려갔습니다.

[Kết thúc Phần 10]

## [Phần 11] 밤이 낮이 되었다 — 「밤이 낮이 되었다」 / Chiến thắng có giá  (34:30–37:30)
> Tóm tắt VI: Sáng D15 trên đèo. Xác bọc poncho, chôn kiểu Goguryeo — gò đất, vòng đá cuội, phiến đá dựng; kỵ binh 해모루 cúi đầu — tổ tiên chôn hậu duệ. 오태민: "전차 고치느라 이틀 잃었습니다. 그 이틀이 태오입니다." — "안다." 박기철 không nói, lau miếng đồng; đọc số: "야시경 열 개. 드론, 없습니다." 해모루 tách về với 을지문덕. ENEMY POV đêm D15: 탁발흠 đeo kính đêm lên mũ lông — POV xanh lục — "밤이… 낮이 되었다." Thông ngôn Goguryeo bị bắt hỏi 태오; "모릅니다." 탁발흠 gỡ 태극기 trên vai 태오, cất. Gửi 천둥 3 + drone về tây cho 양제 với 200 kỵ; giữ 2 kính đêm + 태오. D16: 우중문 nhận tin "뇌군은 살수로 갑니다." 우문술: "그럼 우린 왜 건너는 거요?" 우중문: tiến [史].
> Chức năng: CONSEQUENCE · Tài nguyên nói thành lời: "야시경 열 개" · "드론, 없습니다" · Enemy: công nghệ đổi phe · Foreshadow: 태극기 của 태오 trong tay 탁발흠 (5화) · kính đêm → 4화 săn đêm · "밤눈도 밥을 먹는다" → pin kính đêm 4–5화 · Open loop: "탁발흠은 드론을 서쪽으로 보냈습니다. 야시경은 보내지 않았습니다."

### SC_250 · LOC_009_SEOKMUN_PASS (nền đất bằng phía nam yên, sáng mưa) · đại đội, CHAR_105, kỵ Goguryeo, CHAR_106 · VEH_101, PROP_012 · video8s · 34:30–34:38
[ACTION-VI] Nền đất nhỏ phía nam yên đèo: xác bọc poncho olive đã hạ xuống hố nông; kỵ Goguryeo xếp đá cuội thành vòng quanh gò đất theo cách của họ, không ai bảo; 을보 dựng một phiến đá xanh đứng ở đầu mộ; 해모루 và kỵ binh cúi đầu; lính Hàn đứng hàng ngang, mũ cầm tay.
[SOUND] mưa, đá xếp, im.
N: 고구려 사람들이 묻었습니다. 흙을 돋우고, 냇돌로 둘러 세우고, 머리맡에 돌을 세웠습니다. 그들의 방식이었습니다. 천사백 년 전의 조상이 천사백 년 뒤의 자손을 묻었습니다.

### SC_251 · LOC_009_SEOKMUN_PASS (mộ — cận) · — · PROP_011 (mũ) · still_kenburns · 34:38–34:48
[ACTION-VI] Ảnh cận: gò đất mới, vòng đá cuội xám, phiến đá xanh dựng; trên gò, chiếc mũ chiến đấu bọc vải camo úp xuống, patch 태극기 nhỏ trên mũ ướt mưa; một mũi tên Goguryeo cắm cạnh mộ do kỵ binh để lại. Ken-burns đẩy chậm vào 태극기.
[SOUND] mưa.
N: 이름은 여기 적지 않습니다. 스물세 살. 강원도 어느 마을의 아들이었습니다. 그는 이 땅에 묻힌 첫 번째 사람이었습니다. 이 땅은 그때도 이 땅이었습니다.

### SC_252 · LOC_009_SEOKMUN_PASS (đường xuống phía nam, cạnh K2) · CHAR_002, CHAR_001 · VEH_001, WPN_003 · video8s · 34:48–34:56
[ACTION-VI] Walk-and-talk xuống dốc: 오태민 đi cạnh 한승우, khẩu K3 người chết trên vai cạnh súng mình; ông nói không nhìn 한승우 — không phải buộc tội, là nói ra con số.
[SOUND] mưa, giày trên đá, xích K2 phía sau.
N: 오태민은 셈을 했습니다. 처음으로 그의 셈은 화력이 아니었습니다. 시간이었습니다.
오태민: 전차 고치느라 이틀 잃었습니다. 그 이틀이 태오입니다.

### SC_253 · LOC_009_SEOKMUN_PASS (đường xuống) · CHAR_001 · — · video8s · 34:56–35:04
[ACTION-VI] 한승우 đi tiếp, một từ; mắt nhìn đường; tay phải cầm chiếc mũ trống của 태오 bên hông, ngón cái miết vào ngàm kính đêm.
[SOUND] mưa, giày.
N: 그는 변명하지 않았습니다. 전차를 고친 것은 그의 결정이었습니다. 그 결정의 값을 그는 알았습니다. 아는 것과 갚는 것은 다른 일이었습니다.
한승우: 안다.

### SC_254 · LOC_009_SEOKMUN_PASS (đuôi K2, đang bò) · CHAR_003 · VEH_001, PROP_023 · video8s · 35:04–35:12
[ACTION-VI] 박기철 đi sau đuôi K2 đang bò, tay cầm giẻ đỏ lau tấm lưới buồng động cơ trên chỗ vá đồng — lau đi lau lại một chỗ đã sạch; biển "3" trên quai ba lô đung đưa; ông không nói gì.
[SOUND] xích, giẻ trên thép, mưa.
N: 박기철은 말이 없었습니다. 그는 구리를 닦았습니다. 이틀 동안 두드린 구리였습니다. 그 구리 값이 무엇이었는지, 그도 알았습니다.

### SC_255 · LOC_009_SEOKMUN_PASS (điểm dừng ngắn, chân đèo phía nam) · CHAR_003, CHAR_001 · EQP_001, UAV_001 (hộp trống) · video8s · 35:12–35:20
[ACTION-VI] Dừng ngắn dưới chân đèo: 박기철 với bảng gỗ, gạch hai dòng, đọc cho 한승우 — giọng đếm, nhưng chậm hơn thường; trên tấm bạt: 10 kính đêm, chỗ trống nơi từng đặt hộp drone.
[SOUND] bút dạ, mưa.
N: 숫자는 줄었습니다. 야시경 열둘이 열이 되었습니다. 드론은 없었습니다. 하늘 눈은 감겼습니다. 이 부대는 이제 땅에서만 보았습니다.
박기철: 야시경 열 개. 드론, 없습니다.

### SC_256 · LOC_009_SEOKMUN_PASS (đường nam dưới đèo, wide mưa) · đại đội, CHAR_105 · VEH_001, VEH_101, EQP_002 · still_kenburns · 35:20–35:30
[ACTION-VI] Ảnh: ngã ba đường dưới đèo trong mưa: cột đại đội + K2 đi tiếp về nam; 300 kỵ 해모루 rẽ ngược lên phía bắc-đông, 해모루 ở giữa ngoái lại, radio trên ngực; hai cột tách nhau như chữ Y. Ken-burns kéo ra.
[SOUND] mưa, vó ngựa xa dần, xích.
N: 고개 밑에서 해모루는 갈라졌습니다. 그는 을지문덕에게 돌아가야 했습니다. 지는 싸움이 기다리고 있었습니다. 말하는 돌은 십 킬로까지 닿았습니다. 십 킬로 뒤에 그는 다시 혼자였습니다.

### SC_257 · LOC_009_SEOKMUN_PASS (trại Tiên Ti trên cao nguyên phía tây-bắc đèo, đêm D15) · CHAR_205, 선비 부장 · EQP_001 · video8s · 35:30–35:38
[ACTION-VI] Đêm, lửa trại nhỏ: 탁발흠 ngồi, cầm kính đêm PVS-11K trong tay — vật nhỏ đen có thị kính; 부장 chỉ vào ngàm trên chiếc mũ Hàn thu được, giải thích cách nó gắn; 탁발흠 nhìn mũ, nhìn kính, rồi lấy dây da buộc kính lên vành trước mũ lông cáo của mình, ngay trên mắt phải.
[SOUND] lửa, dây da.
N: 탁발흠은 밤눈을 손에 넣었습니다. 하나는 조종병의 것, 하나는 사수의 것. 석문령에서 그는 밤을 배웠습니다. 밤눈도 밥을 먹는다는 것을, 그는 아직 몰랐습니다.

### SC_258 · LOC_009_SEOKMUN_PASS (trại Tiên Ti — POV kính đêm 탁발흠) · kỵ Tiên Ti, CHAR_005 · EQP_001 · video8s · 35:38–35:46
[ACTION-VI] POV kính đêm xanh lục nhiễu hạt — lần đầu từ mắt địch: trại tối bỗng sáng như ngày: từng khuôn mặt Tiên Ti quanh lửa, ngựa buộc tai vải, và ở gốc thông, 태오 ngồi trói tay sau lưng, mắt trái sưng, môi rách, chỉ còn áo quân phục rách và tất; cậu ngẩng lên nhìn thẳng vào ống kính — vào hắn.
[SOUND] kính đêm rít, lửa, im.
N: 그는 처음으로 밤을 보았습니다. 초록으로 빛나는 밤이었습니다. 그 밤 속에서 포로가 그를 보고 있었습니다.

### SC_259 · LOC_009_SEOKMUN_PASS (trại Tiên Ti) · CHAR_205 · EQP_001 · video8s · 35:46–35:54
[ACTION-VI] Cận 탁발흠: kính đêm trên mũ lông, ánh lửa cam trên sẹo, mắt trái mở nhìn lửa, mắt phải sau kính; hắn nói rất khẽ — không phải với ai.
[SOUND] lửa, im.
탁발흠: 밤이… 낮이 되었다.

### SC_260 · LOC_009_SEOKMUN_PASS (trại Tiên Ti, gốc thông) · 고구려 통역 포로, CHAR_005, CHAR_205 · — · video8s · 35:54–36:02
[ACTION-VI] Một tù binh Goguryeo — áo vải rách, mặt bầm, tay trói — bị đẩy tới ngồi xổm trước 태오; 탁발흠 đứng sau nói một câu Tiên Ti/Hán ngữ (quy ước: khán giả không nghe rõ lời); tù binh Goguryeo quay sang 태오, nói tiếng Goguryeo — 태오 hiểu (quy ước Goguryeo ↔ đại đội).
[SOUND] lửa, thì thầm, tiếng nói khàn.
N: 탁발흠은 말을 걸 수 없었습니다. 고구려 말은 이상하게도 이 젊은이에게 통했습니다. 그것을 그는 요동성에서부터 보아 왔습니다.
고구려 통역 포로: 이 쇠새… 누가 날리느냐 묻소.

### SC_261 · LOC_009_SEOKMUN_PASS (trại Tiên Ti, gốc thông) · CHAR_005 · — · video8s · 36:02–36:10
[ACTION-VI] 태오 nhìn tù binh Goguryeo, nhìn hộp drone olive đặt cạnh lửa, nhìn lên 탁발흠 — rồi cúi đầu, nói một từ; mắt sưng, môi rách nhưng giọng đều.
[SOUND] lửa.
N: 장태오는 하나만 말하기로 했습니다. 모릅니다. 그는 그 말을 앞으로 백 번 할 것이었습니다.
장태오: 모릅니다.

### SC_262 · LOC_009_SEOKMUN_PASS (trại Tiên Ti, gốc thông) · CHAR_205, CHAR_005 · PROP_011 · video8s · 36:10–36:18
[ACTION-VI] 탁발흠 ngồi xổm xuống ngang mặt 태오, không đánh; hắn nhìn vai phải cậu — patch 태극기 nhỏ (ba mũi chỉ 서아 khâu); hắn nắm mép patch, giật — chỉ đứt, patch rời ra; hắn xoay nó trước lửa, gấp lại, nhét vào trong áo giáp da ngực. 태오 nhìn theo bàn tay hắn.
[SOUND] chỉ đứt, lửa, thở.
N: 어깨의 깃발이 뜯겼습니다. 어제 세 바늘로 꿰맨 깃발이었습니다. 요동성에서 그는 빈 탄창을 허리에 찼습니다. 이번에는 깃발이었습니다. 마지막 강까지 그의 품에 있을 것이었습니다.

### SC_263 · LOC_009_SEOKMUN_PASS (trại Tiên Ti) · CHAR_205, 선비 부장 · UAV_001 (hộp), EQP_001 · video8s · 36:18–36:26
[ACTION-VI] 탁발흠 đứng dậy, đá nhẹ hộp drone về phía 부장, chỉ về tây; tay kia vỗ lên kính đêm trên mũ; giọng cộc.
[SOUND] hộp trượt trên đất, lửa.
N: 황제의 명은 산 채로였습니다. 쇠수레와 쇠새는 서쪽으로, 이백 기가 호송할 것이었습니다. 밤눈과 포로는 미끼였고, 눈이었습니다.
탁발흠: 수레와 새는 황제께. 눈은 내가 갖는다.

### SC_264 · LOC_005_AMNOK (đường lầy phía bắc, ngày mưa D16) · kỵ Tiên Ti · VEH_002 (천둥 3), VEH_206, UAV_001 (hộp) · still_kenburns · 36:26–36:36
[ACTION-VI] Ảnh: 40 con bò kéo K21 천둥 3 quay đầu về tây trên đường lầy, 200 kỵ Tiên Ti hộ tống hai bên, hộp drone olive buộc trên lưng một con ngựa, mưa; xa phía đông-nam, cột quân Tùy vẫn đi ngược hướng. Ken-burns trượt theo hướng tây.
[SOUND] bò rống, dây kéo, mưa.
N: 장갑차는 서쪽으로 돌아섰습니다. 요동성까지 삼백 킬로, 하루 팔십 리. 열흘이 넘는 길이었습니다. 그 뒤에는 낙양까지 더 먼 길이 있었습니다.

### SC_265 · LOC_005_AMNOK (lều 우중문, trại Tùy trên đường nam, D16) · CHAR_202, 수 기병 사자 · PROP_021 · video8s · 36:36–36:44
[ACTION-VI] Lều 우중문 dựng vội bên đường lầy: 우중문 áo choàng đỏ ướt, mũ tháo, râu trắng dính mưa; kỵ sứ của 탁발흠 quỳ báo; 우문술 đứng bên với thẻ tre.
[SOUND] mưa trên lều, giáp.
N: 탁발흠의 보고가 우중문에게 닿았습니다. 뇌군의 행방이었습니다.
수 기병 사자: 뇌군은 살수로 갑니다.

### SC_266 · LOC_005_AMNOK (lều 우중문) · CHAR_203 · — · video8s · 36:44–36:52
[ACTION-VI] 우문술 đặt thẻ tre xuống, nhìn 우중문; câu hỏi khô, không lớn tiếng — người tính toán hỏi người hiếu chiến.
[SOUND] thẻ tre, mưa.
N: 우문술은 같은 말을 다르게 했습니다. 군량이 없다는 말을. 이번에는 질문이었습니다.
우문술: 그럼 우린 왜 건너는 거요?

### SC_267 · LOC_005_AMNOK (lều 우중문) · CHAR_202 · — · video8s · 36:52–37:00
[ACTION-VI] 우중문 đội mũ sắt lại, đứng dậy, kéo rèm lều nhìn ra mưa về phía đông-nam — nói không quay lại.
[SOUND] rèm lều, mưa, trống xa.
N: 우중문은 나아갔습니다. 역사책의 한 줄입니다. 그 한 줄이 30만 5천 명을 살수로 데려갔습니다.
우중문: 건너오. 평양은 사흘 거리요.

### SC_268 · LOC_005_AMNOK (aerial mưa, đường nam) · — · WPN_201, PROP_021 · still_kenburns · 37:00–37:10
[ACTION-VI] Ảnh aerial: cột quân Tùy đen chảy về đông-nam qua thung lũng xanh mưa, không thấy đầu đuôi; cờ đỏ rũ nước; hai bên đường, bao gai vứt rải rác. Ken-burns trượt theo cột.
[SOUND] mưa, hàng vạn bước chân, trống.
N: 아홉 군이 남쪽으로 갔습니다. 을지문덕은 그들 앞에서 지기 시작했습니다. 이기는 군대는 멈추지 않습니다. 굶어도 멈추지 않습니다.

### SC_269 · LOC_009_SEOKMUN_PASS (trại Tiên Ti, đêm — cận 태오) · CHAR_005 · — · still_kenburns · 37:10–37:20
[ACTION-VI] Ảnh cận: 태오 ngồi trói ở gốc thông trong đêm mưa, tay sau lưng, áo quân phục rách, vai phải một khoảng vải sẫm hình chữ nhật nơi patch 태극기 từng ở; mắt mở, nhìn về phía nam. Ken-burns đẩy chậm vào khoảng vải trống trên vai.
[SOUND] mưa, lửa xa.
N: 이 이야기에는 이제 저쪽에 있는 사람이 하나 있었습니다. 스물한 살. 시를 외우는 사람. 그는 남쪽을 보고 있었습니다. 남쪽에 살수가 있었습니다.

### SC_270 · LOC_009_SEOKMUN_PASS (đường mòn, đêm mưa) · CHAR_205, kỵ Tiên Ti · VEH_206, EQP_001 · still_kenburns · 37:20–37:30
[ACTION-VI] Ảnh: 탁발흠 cưỡi ngựa dẫn hàng kỵ binh trên đường mòn đêm, không đuốc — kính đêm hạ xuống mắt phải dưới mũ lông cáo, ánh xanh mờ từ thị kính; sau lưng, một ngựa chở 태오 nằm vắt; hàng kỵ đi trong tối như ban ngày. Ken-burns đẩy vào kính đêm.
[SOUND] vó ngựa êm, mưa, không tiếng người.
N: 탁발흠은 드론을 서쪽으로 보냈습니다. 야시경은 보내지 않았습니다.

[Kết thúc Phần 11]

## [Phần 12] 30만이 지나가게 두시오 — 「30만이 지나가게 두시오」 / Lịch sử rẽ hướng  (37:30–40:00)
> Tóm tắt VI: D17 chiều, 살수 (청천강) lần đầu: sông rộng nông, mô cát, lau sậy cao quá đầu; mưa bắt đầu. Đại đội tới bãi bắc; K2 chui vào lau. 아리: "여기예요. 어머니가 갈대 베던 데." Radio: "한 대장, 여기는 해모루." — 해모루 phi tới với thẻ tre lệnh 을지문덕 (VO trên ảnh ông giữa trận giả thua): "숨으시오. 30만이 지나가게 두시오." 오태민: "지나가게 둡니까? 태오가 저기 있는데?!" 한승우 nhìn sông rất lâu. 박기철 cắm que: "물이 오르고 있습니다." 을보: "비가 오래 가겠구먼." 해모루: "사흘 뒤면 저들이 여기 오오." Narrator: 3 ngày. End card 「살수 612 · 4화 평양」.
> Chức năng: POLITICS-OPEN · Tài nguyên: thời gian 3 ngày · nước lên · Turning point: nhiệm vụ 4화 = không làm gì · Open loop tập: "숨으시오. 30만이 지나가게 두시오."

### SC_271 · LOC_007_SALSU (aerial, chiều mưa bắt đầu) · — · — · still_kenburns · 37:30–37:42
[ACTION-VI] Ảnh aerial: sông rộng ~800 m nhưng nông, mô cát xám nâu ướt nổi thành dải, hàng cọc gỗ đánh dấu đường lội; bờ bắc chìm trong bãi lau xanh xám cao 2–3 m trải hàng trăm mét; bờ nam đồi thấp xanh; mây thấp, hạt mưa đầu lấm mặt nước. Ken-burns kéo ra rất chậm. Không thoại.
[SOUND] mưa bắt đầu, gió qua lau, nước chảy nhẹ.
N: 이틀 뒤. 살수. 오늘의 청천강입니다. 넓고 얕은 강. 모래톱과 갈대. 그 이름을 이 부대의 모든 사람이 학교에서 배웠습니다. 강은 배운 것보다 조용했습니다.

### SC_272 · LOC_007_SALSU (bãi bắc, mép lau) · CHAR_003, đại đội · VEH_001, PROP_020 · video8s · 37:42–37:50
[ACTION-VI] K2 bò từ đường xuống bãi cát ướt, 박기철 đi trước vẫy tay dẫn vào bãi lau; lau cao ngập nóc xe, rẽ ra rồi khép lại sau đuôi xe — xe biến mất; hàng lính theo sau, lau nuốt từng người.
[SOUND] xích trên cát, lau gãy, mưa.
N: 사백 킬로였습니다. 요동성 골짜기에서 여기까지. 전차는 왔습니다. 아흔두 명이 왔습니다. 대장장이와 손녀가 왔습니다. 갈대가 그들을 삼켰습니다.

### SC_273 · LOC_007_SALSU (trong bãi lau) · CHAR_107, CHAR_004 · PROP_020 · video8s · 37:50–37:58
[ACTION-VI] Trong lau: 아리 đi trước 서아, tay vạch lau, chân tìm một lối mòn hẹp chỉ mình cô thấy — nền cát cứng dưới lau; cô dừng, ngồi xổm sờ một gốc lau bị cắt cũ, ngẩng lên cười.
[SOUND] lau, mưa, chim nước.
N: 아리는 길을 찾았습니다. 갈대를 베던 사람들의 길이었습니다. 지도에는 없는 길이었습니다.
아리: 여기예요. 어머니가 갈대 베던 데.

### SC_274 · LOC_007_SALSU (mép lau, bãi cát) · CHAR_001 · EQP_002 · video8s · 37:58–38:06
[ACTION-VI] 한승우 đứng ở mép lau nhìn sông; radio trên ngực "칙" — giọng 해모루 nhiễu (thoại qua radio, không thấy mặt 해모루); ông chộp tổ hợp, áp tai; mặt đổi.
[SOUND] PTT, giọng nhiễu qua radio, mưa.
N: 말하는 돌이 살아났습니다. 십 킬로 안이었습니다.
해모루: 한 대장, 여기는 해모루. 곧 닿소.

### SC_275 · LOC_007_SALSU (bãi cát bờ bắc) · CHAR_105, kỵ Goguryeo, CHAR_001 · VEH_101, EQP_002 · video8s · 38:06–38:14
[ACTION-VI] 해모루 phi dọc bãi cát với 10 kỵ, ngựa sùi bọt, bùn tới ngực ngựa; ông nhảy xuống trước 한승우, thở dốc, rút từ ngực áo giáp một thẻ tre buộc dây đỏ, đưa bằng hai tay.
[SOUND] vó ngựa trên cát, thở, mưa.
N: 해모루는 이틀 밤을 달려왔습니다. 을지문덕은 그 사이에 세 번 더 졌습니다. 편지는 여느 때처럼 짧았습니다.

### SC_276 · LOC_008_GOGURYEO_VILLAGE (thung lũng phía bắc — trận giả thua, ngày mưa) · CHAR_101, CHAR_105 · VEH_101, PROP_012 · still_kenburns · 38:14–38:24
[ACTION-VI] Ảnh: giữa một trận giả thua — kỵ Goguryeo "tan vỡ" qua thung lũng mưa, cờ 삼족오 nghiêng, cột quân Tùy đen phía sau — 을지문덕 trên ngựa ở gò, giáp ướt, đang nói với 해모루 vừa ghì ngựa bên cạnh; mặt ông bình thản như đang nói về thời tiết. Ken-burns đẩy chậm vào mặt ông. Giọng ông ngoài hình (voice-over nhân vật).
[SOUND] xa xa trận, mưa; giọng 을지문덕 rõ.
N: 을지문덕은 이렇게 말했습니다.
을지문덕: 숨으시오. 30만이 지나가게 두시오.

### SC_277 · LOC_007_SALSU (bãi cát) · CHAR_105, CHAR_001 · — · video8s · 38:24–38:32
[ACTION-VI] 한승우 mở thẻ tre — vài chữ Hán khắc; 해모루 nói thêm câu cuối, không giải thích, mắt nhìn thẳng; sau lưng ông, kỵ binh đang cho ngựa uống nước sông.
[SOUND] thẻ tre, mưa.
N: 그것이 전부였습니다. 이유는 그때 말하겠소. 그때는 아직 오지 않았습니다.
해모루: 장군의 명이오. 한 자도 더 없소.

### SC_278 · LOC_007_SALSU (bãi cát) · CHAR_002 · WPN_003 · video8s · 38:32–38:40
[ACTION-VI] 오태민 bước tới, khẩu K3 người chết vẫn trên vai, chỉ tay về phía bắc — nơi 30만 và 태오 đang tới; giọng vỡ, không còn 다나까 đầy đủ.
[SOUND] mưa, dây súng.
N: 오태민에게 이 명령은 네 번째 금지였습니다. 이번에는 다른 것이 걸려 있었습니다. 사람이었습니다.
오태민: 지나가게 둡니까? 태오가 저기 있는데?!

### SC_279 · LOC_007_SALSU (mép nước) · CHAR_001 · — · video8s · 38:40–38:48
[ACTION-VI] 한승우 không trả lời; ông đi tới mép nước, đứng nhìn sông rất lâu — mô cát, cọc gỗ, mưa lấm mặt nước; máy đẩy rất chậm vào lưng ông, rồi vòng sang mặt: mắt không chớp. Không thoại.
[SOUND] mưa trên nước, gió qua lau, im.
N: 한승우는 강을 오래 보았습니다. 요동 벌판에서는 쏘기로, 고개 밑에서는 고치기로 했습니다. 이번에는 아무것도 하지 않아야 했습니다. 그것이 가장 어려운 결정이었습니다.

### SC_280 · LOC_007_SALSU (mép nước, bãi cát) · CHAR_003 · — · video8s · 38:48–38:56
[ACTION-VI] 박기철 cắm một cành cây thẳng xuống cát ở mép nước, rút dao khắc một vạch ngang mực nước hiện tại; ông ngồi xổm nhìn vạch; nước liếm lên đúng vạch — rồi hơi quá.
[SOUND] dao khắc gỗ, nước.
N: 박기철은 새로운 것을 세기 시작했습니다. 기름도 포탄도 아니었습니다. 물이었습니다.
박기철: 물이 오르고 있습니다.

### SC_281 · LOC_007_SALSU (bãi cát, cạnh lau) · CHAR_106 · — · video8s · 38:56–39:04
[ACTION-VI] 을보 chống gậy, ngửa mặt lên trời xám, hứng mưa vào lòng bàn tay chai, ngửi gió; nheo mắt trái nhìn thượng nguồn; nói với không ai.
[SOUND] mưa, gió.
N: 을보는 이 땅의 비를 예순여섯 번 보았습니다. 칠월의 비는 오래 갑니다. 강은 오래 오르는 비를 따라 오릅니다.
을보: 비가 오래 가겠구먼.

### SC_282 · LOC_007_SALSU (bãi cát) · CHAR_105, CHAR_001 · VEH_101, EQP_002 · video8s · 39:04–39:12
[ACTION-VI] 해모루 lên ngựa, ghì cương quay đầu về bắc, nói câu cuối với 한승우; ông vỗ lên radio trên ngực — rồi phi đi, 10 kỵ theo, cát văng.
[SOUND] ngựa, cát, mưa.
N: 해모루는 돌아갔습니다. 을지문덕에게. 지는 싸움으로.
해모루: 사흘이오. 사흘 뒤면 저들이 여기 오오.

### SC_283 · LOC_007_SALSU (aerial bãi lau bờ bắc, mưa) · — · VEH_001 (không thấy) · still_kenburns · 39:12–39:22
[ACTION-VI] Ảnh aerial: bãi lau bờ bắc rộng hàng trăm mét trong mưa — không thấy xe, không thấy người, chỉ một vệt lau hơi ngả nơi K2 đã đi vào; sông xám; bờ nam đồi xanh trống. Ken-burns kéo ra chậm.
[SOUND] mưa, gió qua lau.
N: 사흘. 30만 5천 명이 사흘 뒤에 이 강에 올 것이었습니다. 이기면서 올 것이었습니다. 굶으면서 올 것이었습니다. 갈대밭 속에서 아흔두 명이 그것을 기다려야 했습니다. 싸우지 않고.

### SC_284 · LOC_008_GOGURYEO_VILLAGE (đường nam, aerial mưa) · CHAR_205 (nhỏ), CHAR_005 · WPN_201, VEH_206, EQP_001 · still_kenburns · 39:22–39:32
[ACTION-VI] Ảnh aerial: cột quân Tùy đen chảy về nam qua thung lũng mưa; đi trước cột, tách riêng, một toán kỵ Tiên Ti — người dẫn đầu đội mũ lông có vật đen trên vành; sau hắn một ngựa chở người nằm vắt. Ken-burns đẩy chậm vào toán kỵ dẫn đầu.
[SOUND] mưa, trống xa, vó ngựa.
N: 대군 앞에 탁발흠이 있었습니다. 그의 모자에는 밤눈이 있었습니다. 그의 안장 뒤에는 장태오가 있었습니다. 그는 갈대밭을 향해 오고 있었습니다.

### SC_285 · LOC_007_SALSU (mép nước, chiều muộn) · CHAR_001 · — · still_kenburns · 39:32–39:42
[ACTION-VI] Ảnh: 한승우 một mình ở mép nước, áo choàng gai ướt, mũ trống của 태오 cầm ở tay trái; trước ông, cành cây của 박기철 cắm trên cát, nước đã lên qua vạch dao một ngón tay; sau lưng, bãi lau câm. Ken-burns đẩy chậm từ ông xuống cành cây.
[SOUND] mưa trên nước.
N: 그가 아는 역사는 이 강에서 이겼습니다. 그 역사에 아흔두 명은 없었습니다. 장태오도 없었습니다. 그는 그 역사를 망치지 않기로 했습니다. 그것이 무엇을 뜻하는지, 그는 이제 알았습니다.

### SC_286 · LOC_007_SALSU (cành cây đo nước — cận) · — · — · still_kenburns · 39:42–39:52
[ACTION-VI] Ảnh cận: cành cây cắm trên cát, vạch dao trắng, nước nâu đục dâng qua vạch, bọt mưa; bên cạnh, dấu giày chiến đấu đang đầy nước. Ken-burns đẩy rất chậm vào vạch dao.
[SOUND] mưa, nước lên, im.
N: 그날 밤부터 이 부대의 임무는 싸우지 않는 것이었습니다. 물은 오르고 있었습니다.

### SC_287 · [END CARD] · — · — · still_kenburns · 39:52–40:00
[ACTION-VI] Đen. Chữ trắng giữa khung: 「살수 612 · 4화 평양」. Không hình khác.
[SOUND] mưa còn vọng 3 s trong đen, rồi im tuyệt đối.

[END CARD]

[Kết thúc Phần 12]


---

## 부록 — THỐNG KÊ & TỰ KIỂM (ngoài phần kịch bản · script-writer · 2026-09-16 · v1)

### A. Thống kê (script đếm tự động `logs/scratch/script-writer-ep3/stats.py`: SC theo header `### SC_`, narration = dòng `N:`, thoại = dòng `TÊN:`; 어절 tách theo khoảng trắng; combat KHỐI = SC giao chiến/hỏa lực/truy đuổi/bị tấn công + SC setup/aftermath liền kề trong cùng khối — cách đếm của ep1 v3; combat THUẦN = chỉ SC có giao chiến/hỏa lực đang diễn ra)
| Phần | SC | video8s | still | Giây | Dòng N | Câu N | 어절 N | Câu thoại | 어절 thoại | Combat khối (s) | Combat thuần (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 11 | 9 | 2 | 90 | 7 | 25 | 123 | 4 | 13 | 32 | 24 |
| 2 | 21 | 17 | 4 | 180 | 20 | 87 | 396 | 9 | 48 | 24 | 24 |
| 3 | 18 | 15 | 3 | 150 | 18 | 74 | 321 | 11 | 57 | 16 | 8 |
| 4 | 25 | 21 | 4 | 210 | 24 | 97 | 415 | 14 | 73 | 48 | 40 |
| 5 | 25 | 22 | 3 | 210 | 16 | 65 | 302 | 9 | 48 | 96 | 64 |
| 6 | 25 | 21 | 4 | 210 | 24 | 93 | 421 | 14 | 67 | 32 | 16 |
| 7 | 25 | 22 | 3 | 210 | 24 | 117 | 486 | 14 | 71 | 24 | 24 |
| 8 | 22 | 19 | 3 | 180 | 22 | 87 | 399 | 10 | 55 | 24 | 16 |
| 9 | 25 | 20 | 5 | 210 | 25 | 102 | 443 | 18 | 86 | 24 | 8 |
| 10 | 52 | 50 | 2 | 420 | 35 | 125 | 530 | 17 | 78 | 420 | 296 |
| 11 | 21 | 15 | 6 | 180 | 20 | 84 | 357 | 10 | 40 | 0 | 0 |
| 12 | 17 | 10 | 7 | 150 | 16 | 59 | 227 | 8 | 38 | 0 | 0 |
| **Tổng** | **287** | **241** | **46** | **2400** (= 40:00) | **251** | **1015** | **4420** | **138** | **674** | **740 s = 30,8 %** | **520 s = 21,7 %** |

- Khối combat (9 khối): P1 SC_003–004/007/010 (PZF vào xe mình, đuốc, tên) · P2 SC_020–022 (kỵ Tùy sườn vs 30 kỵ 해모루) · P3 SC_044–045 (lính đào ngũ) · P4 SC_066–071 (kỵ sứ đuổi, K6 xuống nước) · P5 SC_083–094 (giả thua, cối 10 viên) · P6 SC_109/115–117 (chặn 2 척후 nam) · P7 SC_137–139 (hậu vệ, tên lửa lên nóc K2) · P8 SC_152–154 (cướp ruộng) · P9 SC_187–189 (cửa nam) · P10 SC_198–249 (trận đèo). Khoảng cách dài nhất giữa 2 beat action: 21:26 → 23:36 (2:10, P8 — 3 척후 dưới cung Tiên Ti).
- Vùng im narrator: 0:00–0:32 (narrator vào 0:32 "612년 6월. 요동성 동쪽 골짜기였습니다.") · 12:02–13:02 (P5 giả thua) · 31:32–33:00 (P10 Phase 4). Sau mỗi mid-roll: 1 SC không thoại (SC_051, SC_101, SC_151, SC_198). 30 s đầu: 6 shot (SC_001 2-beat · SC_002 · SC_003 2-beat · SC_004). 2-BEAT dùng 6 lần (hook 2, P4 K6 1, P10 3).
- Mid-roll: 7:00 · 14:00 · 21:00 · 27:30 (đúng outline; không chen climax).
- Thoại theo người: 한승우 21 · 박기철 20 · 태오 18 · 해모루 17 · 백성민 11 · 오태민 8 · 을지문덕 8 · 탁발흠 7 · 을보 6 · 우중문 6 · 서아 4 · 아리 4 · 수 기병 사자 2 · 우문술 2 · 유사룡 1 · 박격포 사수 1 · 양제 1 · 고구려 통역 포로 1 = 138 (hiện đại 62 % / Goguryeo 27 % / Tùy 11 %).

### B. Tự kiểm 7 mục
1. **ID trong bible:** CHAR_001–006, 101, 105, 106, 107, 201, 202, 203, 205 ✓ · LOC_001/003/004/005/007/008/009 ✓ · VEH_001/002/003/004/101/206 ✓ · UAV_001, EQP_001/002 ✓ · WPN_001/002/003/004/005/101/201 ✓ · PROP_001/006/007/009/011/012/013/014/015/016/017/018/019/020/021/022/023 ✓. Nhân vật phụ không ID: 소년 척후, 유사룡 [史], 수 전령, 수 기병 사자, 수 총관 사자, 수 낙오병, 수 척후, 고구려 전령, 고구려 통역 포로, PZF 사수, 박격포 사수, K3 사수 (KIA), 조종수/포수, 무전병, 선비 부장, dân làng.
2. **Thời gian khớp outline:** 12/12 phần đúng mốc phút (0 lệch); tổng 40:00; không đứt quãng (script kiểm tra t1 = t2 trước); mọi video8s = 8 s, still 8–12 s. Bảng ngày/đêm D1–D17 ở header — mọi "이튿날/사흘째/이틀 뒤/닷새/사흘 만에" rà theo bảng.
3. **5 direct quotes nguyên văn:** (1) SC_025 "저건 참호가 아닙니다. 밥을 묻고 있습니다." · (2) SC_036 "드론 한 번 충전이 전차 600미터입니다." · (3) SC_074 "저들은 굶고 있소. 굶는 군대는 이기게 두면 되오." · (4) SC_081 "지되, 죽지는 마시오. 지는 것도 병법이오." · (5) SC_276 "숨으시오. 30만이 지나가게 두시오." ✓ · thêm: 양제 SC_132 "천둥을 산 채로 잡아라." · 태오 SC_234 "본부, 본부… 잡혔—" · 탁발흠 SC_259 "밤이… 낮이 되었다." · SC_129 "쇠수레는 산을 못 넘소. 길로 가오." · SC_130 "새는 수레에 앉아 밥을 먹고…" · SC_150 "쇠수레가 멈췄다. 물을 마시고 있다." · 박기철 SC_034 "산길로 400km, 딱." · SC_157 "이 전차가 없으면 우리는 그냥 소총 아흔 자루입니다." · SC_038 "입이 둘 더 늘었습니다." · 을지문덕 SC_103/106/108 · 한승우 SC_123 "몰라. 그래서 살아 있어야 해." · 오태민 SC_252/278 · 백성민 SC_218 "목표는 태오다!" · 한승우/태오 SC_190–191 "너무 높다." / "신호는 높아야 잡힙니다." · 박기철 SC_280 "물이 오르고 있습니다." ✓. 12 open loop cuối phần đúng câu outline: SC_011 · 032 · 050 · 075 · 100 · 125 · 150 · 172 · 197 · 249 · 270 · 276 (+ N kết SC_286).
4. **0–30 s không narration:** ✓ (SC_001–004 chỉ SFX + 1 câu đếm của 박기철).
5. **≤12 어절/câu thoại:** 0 vi phạm (138 dòng, dài nhất 11 어절 — SC_077 우중문 [史]). Narration ≤15 어절/câu: 0 vi phạm (1015 câu). Không dùng "그러나 그들은 몰랐습니다". Thì quá khứ thống nhất, trừ câu mở địa danh ("612년 6월." / "닷새 뒤. 압록수." / "이틀 뒤. 살수.").
6. **Ràng buộc nội dung:** xe 7→1 (SC_010 N) · 천둥 3 nguyên vẹn, biển tên tháo (SC_004, 011) · PZF 12→10 (SC_003/006) →9 (SC_236) · 40mm 160 nổ trong 천둥 2 (SC_004), 60 trong 천둥 3 (SC_098/127) · K2 12→8 (SC_227 "열두 발", bộ đếm SC_228→230 "08") · dầu "400km 딱" (SC_034), "600미터" (SC_036), "삼 킬로" (SC_148) · drone 2→1 (SC_035) →0 (SC_238; SC_255 "드론, 없습니다") · kính đêm 12→10 (SC_244/255/257) · cối 60→50 (SC_082/094) · K6 −60 (SC_070) · 94→93 + 1 bị bắt (SC_249) · 을보+아리 nam hạ, "입이 둘" (SC_038) · 해모루 nhận radio (SC_111–112; dùng SC_137/147/187/205/239/274) · 을지문덕 giả hàng không giáp, áo lụa + 조우관, tay không, 해모루 đi cùng, đại đội yểm hộ drone cuối, K2 không bắn (SC_052–074) · P-11: 을지문덕 viết (필담), 해모루 dịch thầm (SC_060–061); 탁발흠 ↔ 태오 qua 고구려 통역 포로 (SC_260) · 우중문/우문술 [史] (SC_076–078, 265–267) · 양제 "산 채로" (SC_132) · 탁발흠 đeo kính đêm lên mũ lông (SC_257–259) · 태극기 của 태오 (SC_191 khâu → SC_262 giật) · 백성민 làm quen ngựa (SC_047) · 1 KIA không tên, chôn kiểu Goguryeo (SC_233, 250–251) · kết "숨으시오" (SC_276) · không nhắc Bắc Triều Tiên (chỉ "이 땅" ×7) · không khẩu hiệu · 시호: 0 lần trong thoại người đương thời (nhãn "수 양제:" là tên vai như ep1).
7. **Anti-copy:** trình tự tập = PZF vào xe mình → hai cột song song/chôn lương → "600미터"/đổi ngựa → 필담 trong trại địch, K6 xuống nước → giả thua có chủ đích, xe mình bị bò kéo → lệnh một tên sông → địch đoán đường từ vật lý xe, K2 rò nước → "소총 아흔 자루" → bàn cát nhìn nam, địch nhìn từ vách → K2 bắn 4 viên vào đá, địch nhắm mắt không nhắm xe → chôn trên đèo, kính đêm đổi phe → "để 30 vạn đi qua". Không "tướng giải thích rồi giao súng", không xe tăng cứu tinh, không tableau đôi trên tường + lều địch + card.

### C. Benchmark 18 chỉ số (tự chấm theo docs/benchmark_vs_reference.md — QC reviewer chấm lại)
| # | Chỉ số | Mục tiêu | 3화 | Chấm |
|---|---|---|---|---|
| 1 | Giây đầu có nguy hiểm/câu hỏi | ≤ 0:10 | **0:03** (rút dầu dưới ánh lửa, 0:16 xe mình cháy, 0:20 PZF vào xe mình) | ✅ |
| 2 | Shot trong 30 s đầu | ≥ 5 | **6** (2 SC 2-beat) | ✅ (gốc 13) |
| 3 | Narrator trong 30 s đầu | 0 | **0** — vào 0:32 | ✅ |
| 4 | Giao tranh đầu | ≤ 7:00 | Hỏa lực: **0:20** (PZF, SC_003) · đại đội bắn về phía địch: **1:14** (SC_010) · kỵ chạm kỵ: **2:50** (SC_021) · địch chạm đại đội: **9:38** (K6, SC_070) | ✅ (ep1: 12:14) |
| 5 | Combat/runtime | ≥ 35 % (S40 ≥ 30 %) | **30,8 %** khối (740 s, 9 khối) · 21,7 % thuần | ⚠️ đạt S40 ≥30 %, dưới mục tiêu 35 % và kênh gốc 45 % — P6/P11/P12 là chính trị/hậu quả theo outline |
| 6 | Khoảng cách tối đa 2 beat retention | ≤ 4′ | action: **2:14** (23:44→25:58) · mọi beat (số/quyết định/địch/reveal): ≤ 1:30 | ✅ |
| 7 | Con số tài nguyên nói thành lời | ≥ 6 | **≥ 24** câu thoại có số (백팔십/백구십 · 400km 딱 · 600미터 · 한 통 · 입이 둘 · 닷새 · 육십 킬로 · 삼십 분 · 네 발 · 오십/이백 미터 · 십사 분 · 열 발 ×2 · 삼백 기 · 이틀 · 삼 킬로 · 드론 하나/충전 한 번/40% · 두 시간 · 십 분 · 마흔 분 ×3 · 야시경 열둘 · 이 분 · 열 개 · 셋 · 다섯 · 사흘) + ~20 câu N có số | ✅ |
| 8 | Enemy POV | ≥ 5 cảnh, địch có tên & học | **~62 SC** / 14 cảnh (P1 đuốc · P2 chôn lương ×2 · P4 trại 우중문 · P5 우문술/우중문, bờ tây K21 · P7 탁발흠 K21, bản đồ bùn, bịt tai, 육합성, gờ núi · P8 tai ngựa, thả척후 · P9 insert vách · P10 ×8 · P11 trại Tiên Ti, lều 우중문 ×2). 탁발흠 học/áp dụng **7**: đoán đường từ vật lý xe · đánh lúc xe sạc · bịt tai ngựa · nhánh trên đường dê · thả척후 để nuôi tin sai · nhắm mắt/người điều khiển thay vì xe · giữ kính đêm, gửi xe. Nói thành lời: SC_129/130/150/171/224/263 | ✅ |
| 9 | Nhân vật lịch sử ra quyết định | ≥ 3 | Sử thật: 을지문덕 **5** (giả hàng · không ngoảnh lại · "지되 죽지 마시오" · Salsu không giải thích · "숨으시오") · 우중문 2 (đuổi/tiến) · 우문술 1 (nhượng) · 유사룡 1 (can) · 양제 1 (산 채로) = **10 / 5 người thật**; hư cấu: 해모루 3 (đổi ngựa · bỏ nam phá cửa đông · thả radio), 탁발흠 7 | ✅ |
| 10 | Số câu thoại | 120–160 | **138** | ✅ |
| 11 | Thoại > 12 어절 | 0 | **0** | ✅ |
| 12 | Quote đắt | ≥ 5 | **≥ 14** (mục B.3) | ✅ |
| 13 | Shot trung bình | 8–10 s | **8,36 s** (2400/287) · P10 **8,08 s** (+3 SC 2-beat → ~7,6 s hiệu dụng) | ✅ khung · ❌ gốc 4 s trong trận → veo-stage cắt đôi thêm ~12 clip P10 |
| 14 | Kết mở | có + hạt series | 12/12 open loop · kết tập = lệnh "không làm gì" + nước lên + 태오 bên kia · hạt series 2: K21 + drone về tây (SC_264) | ✅ |
| 15 | Mid-roll sau open loop nhỏ | 4 | 7:00 / 14:00 / 21:00 / 27:30, sau mỗi điểm 1 SC không thoại | ✅ |
| 16 | Yếu tố riêng | hậu cần · bỏ xe · để địch đi qua · địch có tên | Bỏ xe ✓ (P1) · hậu cần nói thành lời 8 lần (박기철), "전차가 노새" ✓ · địch có tên học 7 lần ✓ · **"để 30 vạn đi qua" ✓ (P12)** · tổ tiên chôn hậu duệ ✓ · 필담 ✓ · công nghệ đổi phe (kính đêm trên mũ lông) ✓ | ✅ 6/6 |
| 17 | Lỗi lịch sử cứng | 0 | **0** (9 quân/3 tên đạo đúng · 100일/3석 · lệnh chém · 詐降 · mật lệnh bắt · 유사룡 · "더 할 말" · không ngoảnh lại · 우문술/우중문 câu mắng · 7 trận). Hư cấu ghi rõ [虛]: 석문령, sơn thành, làng, K21 bị thu, nội dung 필담. Mềm: 우중문 "평양은 사흘 거리요" (câu mẫu bible — khoác lác của nhân vật) | ✅ |
| 18 | Trình tự giống kênh gốc | KHÔNG | Không (mục B.7); kết = lệnh ẩn, không trận thắng | ✅ |

**Kết luận tự chấm:** thua kênh gốc ở #5 (30,8 % vs 45 %) và #13 (8 s vs 4 s trong trận); ngang/hơn ở 16/18. Đề xuất nâng #5 nếu user muốn: đổi 2 SC thoại P6 (SC_113–114) thành mini-combat kỵ Goguryeo hạ 척후 thứ 3 → +16 s (31,5 %), hoặc giữ nguyên vì P6 theo outline là POLITICS.

### D. Nhật ký diễn giải ngoài outline (script-writer quyết — user/story-director đảo được)
1. **PZF 12→9 = 2 quả phá 천둥 2 (P1) + 1 quả cụm đuốc (P10)** theo brief user ("2 quả phá xe mình"); outline P10 ghi "PZF ×3" và ledger ghi "đốt xe bằng dầu + lựu đạn, không tốn PZF". Tổng cuối tập vẫn 9. → proposals P-38.
2. **Tiêu đề P1 "불타지 않은 4호" → "3호"** (천둥 4 đã cháy 2화; open loop outline là "천둥 3호").
3. **천둥 3 KHÔNG qua 압록수**: ở lại bờ tây với 200 kỵ, bò 70리/ngày (để tới 압록 trong 10 ngày); P7 백성민 chỉ thấy cột Tùy 2 ngày phía sau (outline: "천둥 3 và cột Tùy"); P11 gửi về tây từ bờ tây.
4. **5 ngày trên ngựa**: K6/cối/đạn buộc lên đuôi K2 ("전차가 노새가 됐습니다"), 을보/아리 ngồi trên buồng động cơ — xe bò không theo kịp 60 km/ngày.
5. **Trận giả thua P5** diễn ra ở bờ nam ngay sau khi tiền quân Tùy lên bờ (không phải giữa sông); 1 kỵ Goguryeo chết, 3 bị thương — "값" của việc thua.
6. **P-11 trong trại Tùy**: 을지문덕 không nói — viết (필담), 해모루 dịch thầm; nội dung lụa do narrator kể ("왕은 성에 계시다. 신이 대신 왔다.") — hư cấu.
7. **Mini-combat thêm** (outline chỉ có P4/P5/P10): P2 kỵ Tùy sườn vs 30 kỵ 해모루 · P3 lính Tùy đào ngũ lạc vào trại (mang thông tin "chôn lương") · P6 백성민 chặn 2 척후 nam (nuôi red herring) · P7 hậu vệ 해모루 + tên lửa lên nóc K2 (아리 dập bằng khăn olive — khăn cháy sém, prop) · P8 kỵ Tùy cướp ruộng ("굶은 겁니다") · P9 해모루 đuổi 5 척후 cửa nam. Bỏ: cảnh 서아 học thảo dược với phụ nữ làng (P7) và 소년 척후 về báo (P9).
8. **Red herring do địch nuôi**: 탁발흠 thả 3 척후 của 해모루 trên đường dê để họ về báo "không có ai" (SC_170–171) + insert 2 척후 Tiên Ti nhìn xuống bàn cát (SC_178). Outline chỉ có "phân ngựa hiểu sai".
9. **Mỏm đá**: 2 người đi cùng 태오 là súng trường không kính (outline "2 lính kính đêm") để 2 kính mất = của 태오 + xạ thủ K3 (SC_257 nói rõ). Tiên Ti lên mỏm bằng dây từ đỉnh vách (nhánh trên đường dê) + leo từ chân; drone tự hạ (return-to-home) về mỏm → bị nhặt (SC_238).
10. **Kính đêm trên đèo**: 3 dùng (백성민 + 2 đi đầu) + 2 trên mỏm, 7 sạc; sau 2 phút sạc dở: 5 đầy, 2 còn 40 % (SC_226) — nối 4화 "30 %".
11. **해모루 tách về với 을지문덕 sau đèo (D15)** rồi phi 2 đêm tới 살수 (D17) với thẻ tre; quote "숨으시오" do 을지문덕 nói qua still + voice-over (SC_276) vì ông không có mặt ở 살수 — tránh 해모루 "đọc hộ" quote 5.
12. **양제 xuất hiện 1 SC (SC_132, 육합성, cầm xác drone #1)** — foundation §4 ghi 양제 tập 1–2/5 nhưng character_bible 3화 có trạng thái "xem drone/kính đêm bị bắt" → dùng cho lệnh "산 채로" thay vì lệnh chuyển tiếp qua narrator.
13. **Timeline**: P6 (lều 을지문덕) = đêm D11 (sơn thành cách 압록 1 ngày, không thể cùng đêm D10) → P7–P12 lệch +1 ngày; bảng ngày/đêm ở header là chuẩn (D17 tới 살수; "사흘 뒤" 30만 tới = D20 → 4화 P1).
14. **Thêm chi tiết nối tập**: 을지문덕 viết thư cho vua (SC_114) · 서아 khâu 3 mũi patch 태극기 của 태오 (SC_191) → 탁발흠 giật (SC_262) · 한승우 giữ mũ trống của 태오 (SC_245/248/285) · 오태민 mang K3 người chết (SC_246/252/278) · 을보 "이 쇠가 땀을 흘리네" (SC_118) báo trước rò nước · 오태민 bị cấm 4 lần (P2/P5/P6/P12).
15. **Số km**: 요동 골짜기 → 압록 300 km (5 ngày × 60), 압록 → 살수 ~100 km (2 ngày sau đèo) ≈ 400 km; xe bò/bộ 30리 (12 km)/ngày trước khi đổi ngựa.
16. **Ledger đề xuất sửa** (world-designer): K6 cuối 3화 = 900 ✓ (−60 P4, −40 gác) · K3 −1.000 (P10) ✓ · 40mm: 160 nổ trong 천둥 2 + ~60 trong 천둥 3 ✓ · kỵ Goguryeo: −1 chết P5 (không trong ledger) · khăn olive 아리 cháy sém (prop) · mũ 태오 (không kính) do 한승우 giữ (prop mới) · K3 của KIA do 오태민 mang (prop) · 을보 miếng đồng vá K2 (vehicle_bible damage state 3화).
