# 살수 612 — 1화 「요하」 대본 v3.1 (TTS-trimmed)

> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 291 (233 video8s + 58 still_kenburns) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer
> **v3.1 (TTS-trimmed):** narration cắt gọn theo tools/tts_budget.py — 0 SC vượt (video8s ≤22 어절 N+thoại, still ≤45), 108,5 어절/phút; thoại/SC/thời gian/open loop/quotes/vùng im không đổi.
> **v3 (QC-fixed, 2026-09-16):** áp dụng logs/qc_ep1_script.md (1 BLOCK + 18 FIX + NOTE ≤1 dòng) theo decisions.md mục "sau QC 1화 script → v3". Xem nhật ký thay đổi ở phụ lục C.
> **Nguồn:** outline_ep1.md (khung 12 phần — chuẩn), series_foundation.md, story_bible.md, character_bible.md (LOCKED), resource_ledger.md (nơi lệch → outline), location/vehicle/prop bible.
> **Quy ước ghi:** `N:` = narration tiếng Hàn (격식체, giọng nam trầm). Trong SC có cả `N:` và thoại, thứ tự đọc do editor quyết (mặc định: N bình luận về câu thoại → đọc SAU thoại; N dẫn vào → đọc TRƯỚC). `TÊN:` = thoại tiếng Hàn. `[ACTION-VI]` = hành động nhìn thấy được (tiếng Việt, cho veo-prompt-engineer). `[SOUND]` = âm thanh gợi ý. `(tiếp)` = narration nối từ SC trước, không đọc lại. `[NARRATOR IM LẶNG]` / `[MID-ROLL]` / `[END CARD]` theo outline.
> **ID:** CHAR_/LOC_/VEH_/UAV_/EQP_/WPN_/PROP_ theo bible. Nhân vật phụ không ID (ghi tên vai): 소년 척후 (~17), 수 전군총관 (tướng tiền quân Tùy — không phải 맥철장), 전령 (평양), 무전병, 초병, 사수, 조종수, 수 환관, dân đánh xe.
> **Ghi chú LOC:** 탁군 (P1) và hành doanh 양제 bên 요하 (P12) dùng identity LOC_004_YUKHAPSEONG theo location_bible (1화: chiếu xuất quân · 탁발흠 quỳ báo). Flashback 철원 (P2) chưa có LOC trong bible → ghi `LOC_FLASHBACK_CHEORWON` (đề xuất, xem proposals).
> **Quy ước ngôn ngữ (P-11):** trên màn hình mọi phe nói tiếng Hàn. Goguryeo ↔ đại đội hiểu nhau. Tùy ↔ đại đội không đối thoại trực tiếp trong tập này.
> **Quy ước v3:** `2-BEAT` trong [ACTION-VI] = 1 SC 8 s gồm 2 shot (veo-stage tạo 2 clip ngắn hoặc cắt đôi ở edit) — chỉ dùng ở hook và trận. Người đương thời KHÔNG dùng 시호 (영양왕); chỉ narrator được dùng. Narrator: thì quá khứ "-였습니다/-했습니다" cho toàn tập, trừ câu mở địa danh ("612년 정월. 탁군.").
> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi "X일째/이틀 뒤" trong narration rà theo bảng này):**
>
> | Ngày | Buổi | SC | Sự kiện |
> |---|---|---|---|
> | D0 | đêm (철원, flashback) | SC_013–021 | huấn luyện, bão điện khô |
> | D1 | sáng sớm | SC_022–034 | đường nhựa cắt, radio chỉ nội bộ, bốc đất, vết móng không đóng sắt (xe chưa phủ lưới — TRƯỚC P1) |
> | D1 | sáng | SC_001–012 | mũi tên trong lốp, 위성 0, vệt bụi đông-nam = kỵ Goguryeo thu quân (기병 미상), lệnh phủ lưới |
> | D1 | sáng–trưa | SC_035–052 | kiểm kê; drone bay tây 8 km thấy cầu phao đang đẩy; không nổ máy phát (tiếng động) |
> | D1 | trưa [史] | SC_053–060 | cầu phao ngắn 1장, Goguryeo thắng, 맥철장·전사웅·맹차 chết, cầu kéo về |
> | D1 | chiều | SC_061–076 | 백성민 trả mũi tên; cậu bé 척후 chạy về 요동성 |
> | D2 | — | (SC_077 N) | Tùy nối cầu |
> | D3 | sáng [史] | SC_077 | cầu nối lại đủ dài; Goguryeo mất ~1만, rút vào 요동성 |
> | D3 | chiều | SC_078–103 | kỵ Tiên Ti vượt sông đuổi dân; drone #1 pin 12 phút (không sạc); trận nhỏ; drone rơi |
> | D3 | hoàng hôn | SC_104–129 | 300 kỵ 해모루; "대왕 재위 이십삼 년"; quyết đi trong đêm |
> | D3 | đêm | SC_130–134 | trại tiền quân Tùy bờ đông: 2.000 kỵ cho 탁발흠 |
> | D3 | đêm | SC_135–144 | hành quân 30 km; trinh sát Tiên Ti bám đuôi (mini-combat); 요동성; đường mòn vào thung lũng (trinh sát thấy đường mòn) |
> | D4 | sáng | SC_145–152 | "간밤에 삼십 킬로"; đường đông bị cắt ngay đêm nay; nhiệm vụ một đêm |
> | D4 | ban ngày | SC_153–154 | 탁발흠 2.000 kỵ vòng đông — trước 본대 1 ngày; 본대 (mỗi ngày 1 quân) bắt đầu tới trước thành |
> | D4 | đêm (밤 4 = "나흘째 밤") | SC_155–201 | sạc/kính đêm/quyết định; 탁발흠 dò thung lũng — tên cắm lưới K2; kế hoạch; trinh sát bị hạ trên gò |
> | D4 | đêm | SC_202–253 | trận đường đông (P10) |
> | D5 | bình minh–sáng | SC_254–274 | cái giá; kho lương; tường tây |
> | D5 | tối | SC_275–280 | 전령 từ 평양 (đi 10 ngày — vua ra lệnh khi biết Tùy tập kết bờ tây) |
> | D5 | đêm | SC_281–290 | hành doanh 양제 bên 요하 (탁발흠 đi ~45 km trong ngày D5) |

---

## [Phần 1] 콜드 오픈 — 「있을 수 없는 아침」 / Chuyện không thể xảy ra  (0:00–1:30)
> Tóm tắt VI: Sáng xám trên thảo nguyên cỏ vàng. Một mũi tên cắm vào lốp xe tải K511. GPS "위성 0/0". Lính gác thấy vệt bụi kỵ binh 3 km. Hard cut 0:48: 탁군 — chiếu xuất quân, 113만 3천 8백, 24군. Cắt về: 한승우 lệnh phủ lưới ngụy trang.
> Chức năng: ACTION-HOOK · Tài nguyên: "위성 0개" · Open loop cuối phần: "그 113만이 향하는 길 위에, 94명의 대한민국 군인이 서 있었습니다."
> Ràng buộc: 0:00–0:30 KHÔNG narrator (narrator vào 0:48 bằng địa danh + năm).

### SC_001 · LOC_003_CHEONDUNG_BASE (thảo nguyên, chưa đặt tên) · — · VEH_003 · video8s · 0:00–0:08
[ACTION-VI] 2-BEAT (veo-stage tạo 2 clip 3 s + 5 s hoặc 1 clip 8 s cắt đôi ở edit): (a) 0:00–0:03 màn đen, chỉ tiếng gió; (b) 0:03–0:08 cận lốp trước phải xe tải K511 #2 — một mũi tên Goguryeo (PROP_015, đầu tam giác có ngạnh) cắm ngập nửa thân, lông vũ xám rung trong gió; cỏ vàng khô phía sau lốp. Máy tĩnh, đẩy chậm vào cán tên.
[SOUND] gió liên tục, cỏ khô cọ vào nhau, bạt xe đập nhẹ. Không nhạc.

### SC_002 · LOC_003_CHEONDUNG_BASE · CHAR_003 · VEH_003 · video8s · 0:08–0:16
[ACTION-VI] Bàn tay đeo găng dính dầu của 박기철 vào khung, chạm cán tên, lắc thử — cắm chắc. Ngón tay vuốt lông vũ. Máy ngước lên mặt ông: mũ lưỡi trai, thái dương muối tiêu, không cười.
[SOUND] gió; tiếng cao su kêu khẽ khi lắc tên.
박기철: 타이어에… 화살입니다.

### SC_003 · LOC_003_CHEONDUNG_BASE · CHAR_001 · — · video8s · 0:16–0:24
[ACTION-VI] 2-BEAT (4 s + 4 s): (a) insert — giày chiến đấu bước qua cỏ vàng khô, máy ngang mắt cá, pan nhanh lên vai áo: miếng vá 태극기 rung trong gió; (b) 한승우 đứng trên nóc K151, ống nhòm hạ ngang ngực, nhìn chân trời — cỏ vàng đến tận cùng, không cột điện, không dãy núi 철원, chỉ trời xám bạc; la bàn đeo dây cổ đung đưa.
[SOUND] cỏ khô dưới giày; gió mạnh hơn, ống nhòm chạm áo giáp.

### SC_004 · LOC_003_CHEONDUNG_BASE · CHAR_002, CHAR_005 · VEH_004 · video8s · 0:24–0:32
[ACTION-VI] Trong K151: 오태민 gõ ngón tay lên màn hình định vị, gõ lại, gõ mạnh. Cận màn hình: "위성 0/0". 태오 ngồi ghế sau, controller drone trên ngực, nhìn màn hình rồi nhìn 오태민.
[SOUND] tiếng gõ nhựa, quạt máy K151 ro ro.
장태오: 위성 0개입니다. 하나도 안 잡힙니다.

### SC_005 · LOC_003_CHEONDUNG_BASE · 초병 · VEH_002 · video8s · 0:32–0:40
[ACTION-VI] Lính gác trên nóc K21 천둥 2, ống nhòm dán mắt, tay trái giơ lên ra hiệu ngừng. Máy over-the-shoulder từ sau lưng anh nhìn ra thảo nguyên.
[SOUND] gió; tiếng ống nhòm chỉnh nét.
초병: 11시 방향… 사람입니다.

### SC_006 · LOC_001_YOHA (thảo nguyên bờ đông, cách sông ~10 km) · — · VEH_101 (기병 미상 — xa, chỉ thấy bụi; KHÔNG đính ref Tiên Ti) · video8s · 0:40–0:48
[ACTION-VI] Aerial wide rất cao: thảo nguyên vàng lượn sóng; ở xa ~3 km về phía đông-nam, một vệt bụi dài bốc lên theo hàng — kỵ binh, chỉ là chấm đen chuyển động dưới bụi, không nhận ra cờ hay giáp (kỵ Goguryeo đang thu quân sau trận cầu phao). Máy giữ tĩnh, không zoom.
[SOUND] gió trên cao, xa xa tiếng vó ngựa mơ hồ.

### SC_007 · LOC_004_YUKHAPSEONG (탁군 — sân điểm binh, identity Tùy) · — · WPN_201 · still_kenburns · 0:48–0:54
[ACTION-VI] HARD CUT. Ảnh: sân điểm binh 탁군 sáng chói, hàng vạn lính Tùy giáp 명광개 xếp ô vuông tới chân trời, trống lớn sơn đỏ hai bên, cờ đỏ-vàng. Ken-burns kéo ra chậm từ trống → toàn cảnh.
[SOUND] một hồi trống Tùy nặng, vang.
N: 612년 정월. 탁군. 오늘날의 베이징 근처입니다.

### SC_008 · LOC_004_YUKHAPSEONG (탁군) · 수 환관 · — · still_kenburns · 0:54–1:00
[ACTION-VI] Ảnh: cuộn chiếu lụa vàng mở ra trên tay quan đọc chiếu (brush calligraphy, không chữ rõ), phía sau là biển giáp bạc. Ken-burns cuộn dọc theo cột chữ.
[SOUND] giọng đọc chiếu xa, ù, trống ngừng.
N: 수 양제가 조서를 읽습니다. 전투 병력 113만 3천 8백. 세상은 이백만이라 불렀습니다.

### SC_009 · LOC_004_YUKHAPSEONG (탁군, đường xuất quân) · — · WPN_201 · still_kenburns · 1:00–1:06
[ACTION-VI] Ảnh: đường lớn xuyên đồng, 24 lá cờ quân đoàn nối nhau xa dần đến chân trời, mỗi quân một khối bụi. Ken-burns trượt ngang theo hàng cờ.
[SOUND] trống và kèn xa, nhiều lớp chồng nhau.
N: 24군이 하루에 한 군씩, 40리 간격으로 떠납니다. 다 떠나는 데 사십 일이 걸립니다. 길 위의 군대만으로 나라 하나 크기였습니다.

### SC_010 · LOC_004_YUKHAPSEONG (탁군, đài duyệt binh) · CHAR_201 · — · video8s · 1:06–1:14
[ACTION-VI] Low-angle: 수 양제 đứng trên đài gỗ sơn son, 통천관 đen viền vàng, áo vàng thổ, sạch tuyệt đối giữa bụi. Ông không nhìn quân — nhìn về phía đông. Máy đẩy chậm vào mặt.
[SOUND] gió lay tua cờ; trống nền rất xa.
N: 목표는 하나. 고구려였습니다. 황제는 직접 요동으로 갈 것이었습니다.

### SC_011 · LOC_003_CHEONDUNG_BASE · CHAR_001, CHAR_003 · VEH_004 · video8s · 1:14–1:22
[ACTION-VI] HARD CUT về: 한승우 hạ ống nhòm, nhìn xuống 박기철 đang đứng cạnh lốp có mũi tên. Hai người nhìn nhau một nhịp. 한승우 quay sang tổ hợp radio trên vai.
[SOUND] gió; tiếng bấm PTT.
N: 하늘에 위성은 없었습니다. 땅 위에는 화살이 있었습니다.
한승우: 전 차량, 위장망. 지금.

### SC_012 · LOC_003_CHEONDUNG_BASE · đại đội (không mặt) · VEH_001, VEH_002, VEH_003, VEH_004 · video8s · 1:22–1:30
[ACTION-VI] Wide từ gò thấp: lính kéo lưới ngụy trang phủ K2 và ba K21; đoàn xe nhỏ xíu giữa biển cỏ vàng; phía xa đông-nam, vệt bụi (기병 미상) vẫn đang di chuyển ngang đường chân trời. Máy tĩnh.
[SOUND] lưới ngụy trang sột soạt, lệnh nhỏ, gió.
N: 그 조서는 두 달 전의 일이었습니다. 그 113만이 향하는 길 위에, 94명의 대한민국 군인이 서 있었습니다.

[Kết thúc Phần 1]

## [Phần 2] 발견 — 「여기가 어디인가」 / Họ đang ở đâu  (1:30–4:30)
> Tóm tắt VI: Flashback đêm trước ở 철원 (không title card, chỉ ánh sáng xanh xám lạnh): đoàn xe, 박기철 đo dầu, 태오 bay thử drone, 서아 đếm thuốc, 백성민 đọc vết, 오태민 đọc kịch bản "30만 남하", 한승우 lệnh giữ bến 한탄강. Bão điện khô, la bàn quay, màn hình nhiễu, đèn tắt. Sáng: đường nhựa bị cắt, không vệt máy bay, radio chỉ nội bộ. Intercut sử: 24군, dân phu, cờ 960리. 한승우 bốc nắm đất. 백성민: vết móng ngựa không đóng sắt.
> Chức năng: DISCOVERY · Tài nguyên: radio chỉ nội bộ 5–10 km; nhắc "연료 한 통", "항생제 스무 개" · Open loop cuối phần: "말발굽 자국인데… 편자가 없습니다."

### SC_013 · LOC_FLASHBACK_CHEORWON (đêm, đường đất đóng băng — đề xuất, chưa có trong bible) · đại đội · VEH_001, VEH_002, VEH_003, VEH_004 · video8s · 1:30–1:38
[ACTION-VI] Ánh sáng xanh xám lạnh, không title card. Đoàn xe nổ máy trên đường đất đóng băng giữa đồi thông: K2 "천둥 1" dẫn đầu, 3 K21, 2 K511, K151 khóa đuôi; đèn pha xuyên hơi thở lính. Tracking ngang theo đoàn.
[SOUND] động cơ diesel nặng, xích nghiến băng, gió đêm.
N: 그 전날 밤. 철원, 겨울 훈련장이었습니다. 여단 훈련 사흘째, 실탄은 제한 수량이었습니다. 기계화보병중대 하나에 전차 한 대가 붙은 편성이었습니다.

### SC_014 · LOC_FLASHBACK_CHEORWON · CHAR_003 · VEH_001 · video8s · 1:38–1:46
[ACTION-VI] 박기철 rút que đo dầu khỏi K2 dưới đèn pin che tay, soi vạch, lau que bằng giẻ đỏ ở thắt lưng, ghi số vào sổ bìa xanh bằng bút chì. Cận mặt càu nhàu.
[SOUND] kim loại chạm, bút chì trên giấy, động cơ nền.
N: 훈련은 사흘. 연료는 그 사흘을 위한 것이었습니다. 박기철은 숫자를 두 번 말하는 버릇이 있었습니다.
박기철: 연료, 한 통입니다. 딱 한 통.

### SC_015 · LOC_FLASHBACK_CHEORWON · CHAR_005 · UAV_001 · video8s · 1:46–1:54
[ACTION-VI] 태오 đứng sau K151, controller sáng xanh hắt lên mặt búng sữa; drone #1 (đèn LED đỏ-xanh) bay lên khỏi lòng bàn tay, treo trên đầu, camera gimbal xoay. Bốn viên pin dán số 1/2/3/4 trên túi giáp.
[SOUND] tiếng rotor drone vo ve, bíp controller.
N: 장태오 일병, 스물한 살. 중대에서 가장 어린 병사였습니다. 드론 넷과 배터리 여덟 개가 그의 재산이었습니다.
장태오: 1호기 이상 무. 배터리 백 퍼센트입니다.

### SC_016 · LOC_FLASHBACK_CHEORWON · CHAR_004 · — · video8s · 1:54–2:02
[ACTION-VI] Trong thùng K511 #1 dưới đèn đỏ: 서아 mở túi quân y, đếm lọ kháng sinh xếp thành hàng trên nắp thùng đạn, ghi vào sổ; băng chữ thập đỏ trên tay trái. Máy tĩnh, cận tay và mặt.
[SOUND] nắp nhựa lách cách, đèn đỏ ù nhẹ.
N: 윤서아 하사, 의무병. 이 가방 하나가 아흔네 명의 병원이었습니다.
윤서아: 항생제 스무 개, 모르핀 서른 개. 이상 없습니다.

### SC_017 · LOC_FLASHBACK_CHEORWON · CHAR_006 · — · video8s · 2:02–2:10
[ACTION-VI] 백성민 mũ boonie, quỳ một gối bên bìa rừng, đèn pin đỏ soi vết chân hươu trên đất đóng băng; ngón tay chạm mép vết, ngẩng lên nhìn vào rừng tối.
[SOUND] im lặng rừng, cành gãy xa.
N: 백성민 중사, 강원도 산골 사냥꾼의 아들. 땅을 읽는 사람이었습니다. 그는 하루 전 발자국과 한 시간 전 발자국을 구별했습니다.
백성민: 고라니. 한 시간 전.

### SC_018 · LOC_FLASHBACK_CHEORWON · CHAR_002 · VEH_004 · video8s · 2:10–2:18
[ACTION-VI] 오태민 dựa cửa K151, đọc kịch bản diễn tập trên tablet, cười khẩy một bên mép, tay áo xắn dù trời rét, kính bảo hộ gác trên mũ.
[SOUND] tablet bíp, gió.
N: 오태민 중위, 부중대장. 화력이 답이라고 믿는 사람이었습니다. 그날 밤까지는 농담이었습니다. 훈련 시나리오는 늘 과장되어 있었습니다.
오태민: 가정, 적 삼십만 남하… 반나절이면 끝납니다.

### SC_019 · LOC_FLASHBACK_CHEORWON · CHAR_001 · VEH_004 · video8s · 2:18–2:26
[ACTION-VI] 한승우 trải bản đồ giấy Cheorwon trên mui K151, đèn pin đỏ, ngón tay dừng ở một khúc sông; bấm tổ hợp radio.
[SOUND] giấy bản đồ, tiếng PTT.
N: 한승우 대위, 중대장. 아흔네 명의 목숨을 맡은 사람이었습니다.
한승우: 전 소대, 여기는 천둥 지휘. 한탄강 여울 확보 후 대기한다.

### SC_020 · LOC_FLASHBACK_CHEORWON · CHAR_001 · — · video8s · 2:26–2:34
[ACTION-VI] Sét không mưa xé ngang trời đen trên đồi — sét khô, không tiếng sấm đúng nhịp. Cận: la bàn lensatic trên ngực 한승우 — kim quay loạn, quay, quay. 한승우 nhìn xuống la bàn, không nói.
[SOUND] tiếng rít tĩnh điện tăng dần, tóc gáy, không sấm.
N: 비는 없었습니다. 나침반은 십 초 동안 돌았습니다. 그 십 초를 설명할 사람은 이후에도 없었습니다.

### SC_021 · LOC_FLASHBACK_CHEORWON · CHAR_005, CHAR_002 · VEH_004, VEH_001 · video8s · 2:34–2:42
[ACTION-VI] Mọi màn hình trong K151 và trên controller của 태오 nhiễu trắng; đèn pha K2 rồi từng xe tắt lần lượt như bị thổi; khung hình chìm vào đen hoàn toàn 2 s cuối.
[SOUND] rít tĩnh điện đạt đỉnh → cắt im tuyệt đối.
N: 그것이 철원의 마지막 밤이었습니다. 다음 아침은 다른 세기의 아침이었습니다.
장태오: 화면이 전부… 나갔습니다!

### SC_022 · LOC_003_CHEONDUNG_BASE · — · VEH_001, VEH_002 · still_kenburns · 2:42–2:48
[ACTION-VI] Từ đen mở ra bình minh xám bạc: ảnh wide đoàn xe đứng im giữa cỏ vàng đến chân trời, sương bám trên giáp xe trần (chưa phủ lưới — trước P1), không núi, không cây. Ken-burns kéo ra rất chậm.
[SOUND] gió lạnh, một con chim đồng kêu.
N: 아침이었습니다. 아무 소리도 나지 않았습니다. 차 소리도, 비행기 소리도. 오직 바람이었습니다. 군인들은 그 침묵을 먼저 들었습니다.

### SC_023 · LOC_003_CHEONDUNG_BASE · CHAR_006 · — · video8s · 2:48–2:56
[ACTION-VI] POV 백성민 (gác ca sáng): đường nhựa dưới chân chạy thẳng 50 m rồi kết thúc như bị dao cắt — mép nhựa gọn, bên kia là cỏ vàng khô cao đến gối rạp theo gió. Máy đi bộ chậm tới mép cắt, dừng.
[SOUND] giày trên nhựa → im khi tới mép; gió.
N: 도로는 오십 미터 앞에서 끝났습니다. 그 너머는 다른 땅이었습니다. 백성민은 그 선을 넘지 않았습니다. 아직은.

### SC_024 · LOC_003_CHEONDUNG_BASE · CHAR_006 · EQP_002 · video8s · 2:56–3:04
[ACTION-VI] 백성민 ngẩng lên: trời xám mênh mông, không một vệt máy bay. Anh nhìn đồng hồ, nhìn trời lần nữa, rồi bấm radio kẹp vai, giọng không đổi.
[SOUND] gió; tiếng PTT.
N: 백성민은 하늘을 먼저 보았습니다. 비행운이 없는 하늘은 처음이었습니다. 그가 아는 하늘에는 언제나 무언가 날고 있었습니다.
백성민: 중대장님. 도로가… 끊겨 있습니다.

### SC_025 · LOC_003_CHEONDUNG_BASE · CHAR_001 · VEH_004, EQP_002 · video8s · 3:04–3:12
[ACTION-VI] 한승우 ngồi ghế trước K151, tổ hợp radio xe áp tai, mắt nhìn màn hình LCD chỉ hiện dòng kênh. Ông bấm, nói, thả — trả về tiếng rít trắng.
[SOUND] rít trắng radio kéo dài sau câu nói.
N: 여단 지휘소는 십 킬로 밖에 있어야 했습니다. 응답은 없었습니다. 기계는 멀쩡했습니다. 없는 것은 상대편이었습니다.
한승우: 여단 지휘소, 여기는 천둥 지휘. 감명도?

### SC_026 · LOC_003_CHEONDUNG_BASE · 무전병, CHAR_001 · VEH_004 · video8s · 3:12–3:20
[ACTION-VI] Nhân viên radio ở ghế sau xoay núm kênh liên tục, lắc đầu nhìn 한승우. 한승우 đặt tổ hợp xuống chậm, nhìn ra ngoài kính chắn.
[SOUND] núm xoay lách cách, rít trắng, gió ngoài xe.
N: 무전은 중대 안에서만 들렸습니다. 세상이 십 킬로로 줄어든 것이었습니다.
무전병: 중대 내부만 됩니다. 십 킬로 밖은 아무것도 없습니다.

### SC_027 · LOC_001_YOHA (đường tiến quân Tùy, ken-burns lịch sử) · — · WPN_201 · still_kenburns · 3:20–3:30
[ACTION-VI] Ảnh: cột quân Tùy giáp bạc, khiên đỏ, đi trên đường đất rộng qua đồng cỏ, bụi vàng cuộn, cờ đỏ-vàng nghiêng cùng hướng gió. Ken-burns đẩy chậm dọc hàng quân.
[SOUND] bước chân hàng vạn người, trống nhịp hành quân.
N: 같은 봄. 수나라 24군이 차례로 요하로 향했습니다. 한 군이 떠나면 다음 군이 하루 뒤에 떠났습니다. 좌군 열둘, 우군 열둘이었습니다. 황제가 요동에 닿기까지 두 달이 걸렸습니다.

### SC_028 · LOC_001_YOHA (kênh đào & dân phu, ken-burns lịch sử) · — · — · still_kenburns · 3:30–3:40
[ACTION-VI] Ảnh: dân phu áo gai kéo xe lương hai bánh nối đuôi vô tận; phía sau, kênh đào chật thuyền chở thóc phủ vải. Ken-burns trượt ngang.
[SOUND] bánh xe gỗ, tiếng thở, roi.
N: 군량을 나르는 민부가 병사의 두 배였습니다. 운하는 곡식 배로 막혔습니다. 병사와 민부를 합치면 삼백만이 넘었습니다. 이 원정은 싸우기 전에 먼저 먹어 치웠습니다.

### SC_029 · LOC_001_YOHA (cờ trải đến chân trời, ken-burns lịch sử) · — · WPN_201 · still_kenburns · 3:40–3:50
[ACTION-VI] Ảnh aerial: một dải cờ và bụi chạy từ tiền cảnh đến tận chân trời, không thấy điểm cuối; mặt trời bạc sau mây. Ken-burns kéo ra.
[SOUND] trống của nhiều quân đoàn chồng nhau, lệch nhịp.
N: 깃발은 960리에 이어졌습니다. 앞뒤 군의 북소리가 서로 들렸습니다. 이런 규모의 원정은 그 전에도, 그 후에도 없었습니다. 그리고 그 끝은 아무도 보지 못했습니다.

### SC_030 · LOC_003_CHEONDUNG_BASE · CHAR_001 · — · video8s · 3:50–3:58
[ACTION-VI] HARD CUT về: 한승우 quỳ một gối ngoài mép đường nhựa, bốc một nắm đất lẫn cỏ vàng khô, bóp trong găng, để rơi qua kẽ tay, nhìn chân trời. Không nói. Máy đẩy chậm từ tay lên mặt.
[SOUND] gió, đất khô rơi.
N: 이 풀은 철원의 풀이 아니었습니다. 그는 그것만은 알았습니다. 나머지는 알 필요가 없다고 정했습니다. 그것이 그가 지휘하는 방식이었습니다.

### SC_031 · LOC_003_CHEONDUNG_BASE · CHAR_002, CHAR_001 · — · video8s · 3:58–4:06
[ACTION-VI] 오태민 đi tới sau lưng, dừng, nhìn cùng hướng, giọng nhỏ lần đầu tiên. 한승우 không quay lại, chỉ đứng dậy, phủi găng.
[SOUND] giày trên cỏ khô, gió.
N: 누군가는 먼저 말해야 했습니다. 한승우는 대답하지 않았습니다. 말하면 사실이 되기 때문이었습니다.
오태민: 중대장님, 여기… 철원이 아닙니다.

### SC_032 · LOC_003_CHEONDUNG_BASE · — · VEH_001, VEH_002, VEH_003, VEH_004 · still_kenburns · 4:06–4:14
[ACTION-VI] Ảnh aerial rất cao: đoàn xe dưới lưới ngụy trang là một vệt nhỏ giữa cỏ vàng vô tận, đoạn đường nhựa 50 m nằm lạc lõng như mảnh băng dính trên thảm. Ken-burns kéo ra thêm.
[SOUND] gió trên cao.
N: 아무도 그 말을 입에 올리지 않았습니다. 대신, 땅을 읽었습니다. 군인은 이유보다 위치를 먼저 묻습니다. 위치는 곧 알게 될 것이었습니다.

### SC_033 · LOC_003_CHEONDUNG_BASE · CHAR_006, CHAR_001 · — · video8s · 4:14–4:22
[ACTION-VI] 백성민 đi trước lần theo một hàng vết trên đất cứng ven đường cỏ, 한승우 theo sau; 백성민 dừng, ngồi xổm, chỉ ngón tay xuống mà không nói. 한승우 ngồi xuống cạnh.
[SOUND] cỏ khô, gió, hai người thở.
N: 그날 아침 백성민이 읽은 것은 발자국이었습니다. 말 스무 필. 두 시간 전. 발자국은 걷지 않고 달렸습니다. 급한 자의 것이었습니다.

### SC_034 · LOC_003_CHEONDUNG_BASE · CHAR_006 · — · video8s · 4:22–4:30
[ACTION-VI] Cận: vết móng ngựa in sâu trên đất bùn cứng — hình móng tròn tự nhiên, không viền sắt, không đinh. Bàn tay 백성민 đặt cạnh làm thước. Máy giữ tĩnh, rồi ngước lên mặt anh.
[SOUND] gió, im.
백성민: 말발굽 자국인데… 편자가 없습니다.

[Kết thúc Phần 2]

## [Phần 3] 재고 조사 — 「재고 조사」 / Kiểm kê  (4:30–7:00)
> Tóm tắt VI: Bãi cỏ trũng, xe phủ lưới. 박기철 đọc sổ: 94명, 22 viên K2, 40mm 600, cối 120, PZF 18, drone 4, dầu 1 bình + 2 phuy, lương 3 ngày, nước 2 ngày. 한승우: ở hay đi → cho drone #1 bay về hướng vệt bụi. Màn hình: cỏ, rồi sông Liêu, cầu phao đang được đẩy sang, doanh trại tới chân trời. Pin 30 → 18. 태오: "끝이 안 보입니다." 오태민 lần đầu im.
> Chức năng: DECISION (đồng hồ) · Tài nguyên nói thành lời: "포탄 스물두 발", "식량 사흘", "배터리 십팔 분" · Open loop: "강 건너에 있는 건 군대가 아니었습니다. 나라 하나가 움직이고 있었습니다." → câu hỏi trước mid-roll: "그게 무엇이든, 이쪽으로 오고 있었습니다."

### SC_035 · LOC_003_CHEONDUNG_BASE · CHAR_003, đại đội · VEH_001, VEH_002, VEH_003 · video8s · 4:30–4:38
[ACTION-VI] Wide tĩnh: hàng xe dưới lưới ngụy trang xanh-nâu trong bãi cỏ trũng — K511 #2 đã thay lốp dự phòng, lốp thủng buộc trên thùng; trước xe, lính xếp hàng ngang. 박기철 đứng trước hàng, sổ bìa xanh mở, đọc to không ngẩng lên.
[SOUND] gió lùa qua lưới, giấy lật.
N: 아흔네 명. 그 숫자가 이 이야기의 시작이었습니다. 다섯 달 뒤까지 매일 다시 세어질 숫자였습니다.
박기철: 현재 인원 아흔네 명. 전원 이상 없습니다.

### SC_036 · LOC_003_CHEONDUNG_BASE · CHAR_003 · VEH_001 · video8s · 4:38–4:46
[ACTION-VI] 박기철 xoay người, bút chì chỉ vào tháp pháo K2 dưới lưới rồi chỉ vào sổ; cận mặt ông, không cảm xúc.
[SOUND] gió, bút gõ lên bìa sổ.
N: 훈련 적재량이었습니다. 실전용이 아니었습니다. 실전이라면 두 배를 실었을 것입니다.
박기철: 포탄 스물두 발. 그게 전부입니다.

### SC_037 · LOC_003_CHEONDUNG_BASE · — · WPN_002, WPN_005, UAV_001 · still_kenburns · 4:46–4:56
[ACTION-VI] Ảnh cận trang sổ bìa xanh viết tay bút chì: các dòng số xếp cột (40mm ×3, 박격포, PZF, 드론) — chữ số Ả Rập rõ, chữ Hàn chỉ gợi nét. Ken-burns trượt dọc trang từ trên xuống.
[SOUND] gió nhỏ, giấy.
N: 40밀리 600발. 박격포탄 120발. 판처파우스트 18발. 드론 넷, 한 대에 30분. 여기서 하나도 늘지 않을 숫자들이었습니다. 박기철은 이 페이지를 매일 밤 다시 썼습니다.

### SC_038 · LOC_003_CHEONDUNG_BASE · — · VEH_001, VEH_003 · still_kenburns · 4:56–5:06
[ACTION-VI] Ảnh: hai phuy dầu 200 L xếp cạnh bao cát, phía sau là K2 dưới lưới và thùng xe tải chở thùng đạn; ánh sáng xám lạnh. Ken-burns đẩy chậm vào hai phuy.
[SOUND] gió, bạt xe đập.
N: 연료는 전차 한 통과 드럼 두 개. 물 이틀. 항생제 한 가방. 전차 한 통은 사백 킬로였습니다. 그 사백 킬로가 이 부대의 수명이었습니다.

### SC_039 · LOC_003_CHEONDUNG_BASE · CHAR_003 · — · video8s · 5:06–5:14
[ACTION-VI] 박기철 gập sổ, nhét vào túi ngực, nhìn thẳng hàng lính rồi nhìn 한승우 đứng bên cạnh.
[SOUND] sổ gập, gió.
N: 그것이 이 부대의 전 재산이었습니다. 박기철은 숫자 앞에 형용사를 붙이지 않았습니다.
박기철: 식량 사흘, 물 이틀. 들어오는 건 없습니다.

### SC_040 · LOC_003_CHEONDUNG_BASE · CHAR_001, CHAR_002, CHAR_003, CHAR_006 · VEH_004 · video8s · 5:14–5:22
[ACTION-VI] Bốn người quanh mui K151; bản đồ giấy Cheorwon trải ra vô dụng, gió lật góc. 한승우 chắp hai tay sau lưng, nhìn về phía đông-nam nơi vệt bụi sáng nay đã tan, rồi quay đầu về phía tây.
[SOUND] bản đồ phần phật, gió.
N: 머무르면 안전했습니다. 사흘 동안만. 움직이면 위험했습니다. 하지만 알 수 있었습니다.
한승우: 선택은 둘이다. 여기 있거나, 움직이거나.

### SC_041 · LOC_003_CHEONDUNG_BASE · CHAR_002, CHAR_003 · VEH_004 · video8s · 5:22–5:30
[ACTION-VI] 오태민 đập tay lên mui xe, chỉ về phía tây; 박기철 bên cạnh lắc đầu rất nhẹ, mắt không rời bản đồ.
[SOUND] tay đập tôn xe, gió.
N: 오태민은 먼지 쪽을 가리켰습니다. 그에게 모르는 것은 곧 적이었습니다. 모르는 것과 싸울 수는 없었습니다.
오태민: 움직입니다. 먼지 난 쪽으로 밀고 갑니다.

### SC_042 · LOC_003_CHEONDUNG_BASE · CHAR_001, CHAR_005 · UAV_001 · video8s · 5:30–5:38
[ACTION-VI] 한승우 quay sang 태오 đang đứng cách vài bước ôm hộp drone; ánh mắt ra lệnh trước khi lời nói. 태오 đứng thẳng người.
[SOUND] gió, hộp drone mở khóa.
N: 먼지는 동남쪽으로, 발자국은 서쪽에서 왔습니다. 한승우는 발자국이 온 곳을 먼저 보았습니다. 사람 대신 드론이었습니다.
한승우: 장 일병. 1호기, 서쪽. 낮게 말고 높게.

### SC_043 · LOC_003_CHEONDUNG_BASE · CHAR_005 · UAV_001 · video8s · 5:38–5:46
[ACTION-VI] Drone #1 bốc lên khỏi lòng bàn tay 태오, xuyên qua khe lưới ngụy trang, lên cao khỏi bãi cỏ; 태오 ngẩng theo, tay trên cần điều khiển. Low-angle.
[SOUND] rotor vo ve mạnh rồi nhỏ dần theo độ cao.
N: 하늘 위의 눈. 이 부대가 가진 가장 귀한 것이었습니다. 이 시대에는 하늘에서 보는 자가 없었습니다.
장태오: 1호기 이륙. 배터리 삼십 분.

### SC_044 · LOC_003_CHEONDUNG_BASE · CHAR_005, CHAR_001, CHAR_002 · UAV_001 · video8s · 5:46–5:54
[ACTION-VI] Cận màn hình controller trong tay 태오: cỏ vàng lướt qua liên tục từ trên cao, chỉ cỏ và bóng mây; quanh màn hình, mấy cái đầu chụm lại, mũ chạm mũ.
[SOUND] tiếng rotor nhỏ qua loa controller, thở.
N: 팔 킬로. 그 사이에 마을 하나, 길 하나 없었습니다. 철원이라면 팔 킬로 안에 도로 셋, 마을 둘이 있었습니다.
장태오: 팔 킬로… 아직 풀입니다.

### SC_045 · LOC_001_YOHA · — · VEH_205 · still_kenburns · 5:54–6:02
[ACTION-VI] Ảnh màn hình drone (góc nhìn thẳng xuống, viền HUD mờ): mép trên khung hình, một dải sông rộng nâu đục hiện ra giữa cỏ vàng. Ken-burns tilt lên rất chậm về phía sông.
[SOUND] rotor qua loa, một tiếng "어…" nhỏ ngoài hình.
N: 요하였습니다. 고구려와 수나라의 경계였습니다. 폭 오백 미터, 흙탕물의 강이었습니다. 이 강을 건너는 것이 원정의 첫 관문이었습니다. 고구려는 이 강을 이백 년 동안 지켜 왔습니다.

### SC_046 · LOC_001_YOHA · CHAR_005 · VEH_205, WPN_201 · video8s · 6:02–6:10
[ACTION-VI] Màn hình drone: ba dải cầu phao thuyền gỗ đang được hàng nghìn người đẩy từ bờ tây sang; trên cầu, lính Tùy xếp hàng dài; bụi và khói. 태오 (ngoài hình) thở gấp. Máy cận màn hình rồi lên mặt 태오.
[SOUND] rotor, tiếng nuốt nước bọt.
N: 수나라 공부상서 우문개가 세운 다리였습니다. 셋이었습니다.
장태오: 다리… 다리를 놓고 있습니다.

### SC_047 · LOC_001_YOHA · — · VEH_205, WPN_201 · still_kenburns · 6:10–6:20
[ACTION-VI] Ảnh aerial từ drone: bờ tây sông Liêu — lều trại xám xếp ô đến tận chân trời, nghìn cột khói bếp, cờ đỏ-vàng, bãi ngựa; bờ đông cỏ vàng trống. Ken-burns kéo ra rất chậm, không thấy điểm cuối trại.
[SOUND] rotor qua loa; im lặng người.
N: 탁군을 떠난 지 두 달. 24군이 요하 서안에 모여 있었습니다. 강 하나가 고구려와 그들 사이에 있었습니다. 천막의 수를 세는 것은 의미가 없었습니다.

### SC_048 · LOC_003_CHEONDUNG_BASE · CHAR_005 · UAV_001 · video8s · 6:20–6:28
[ACTION-VI] Cận mặt 태오, ánh màn hình xanh xám hắt lên, mắt không chớp; môi run.
[SOUND] rotor qua loa, gió.
N: 끝이 없다는 말은 과장이 아니었습니다. 화면이 닿는 곳까지가 전부 진영이었습니다. 사람의 눈으로는 끝을 볼 수 없는 진영이었습니다.
장태오: 끝이… 안 보입니다.

### SC_049 · LOC_003_CHEONDUNG_BASE · CHAR_002, CHAR_003 · UAV_001 · video8s · 6:28–6:36
[ACTION-VI] 오태민 nhìn màn hình, lần đầu tiên im — cằm siết, kính bảo hộ trên mũ phản chiếu màn hình. 박기철 không nhìn màn hình; ông nhìn 오태민. Máy tĩnh, hai mặt trong khung.
[SOUND] rotor, gió, không ai nói.
N: 삼십만이면 반나절이라던 사람이었습니다. 화면 속 숫자는 그 세 배를 넘었습니다. 그는 셈을 다시 하고 있었습니다.

### SC_050 · LOC_003_CHEONDUNG_BASE · CHAR_005, CHAR_001 · UAV_001 · video8s · 6:36–6:44
[ACTION-VI] Cận góc màn hình controller: chỉ số pin nhảy 19 → 18. 태오 ngẩng nhìn 한승우; 한승우 gật một cái. 태오 đẩy cần — hình ảnh trên màn hình quay đầu về đông.
[SOUND] bíp cảnh báo pin, rotor.
N: 배터리 십팔 분. 돌아올 거리를 빼면 볼 수 있는 시간은 끝났습니다. 여섯 분은 돌아오는 값이었습니다.
장태오: 배터리 십팔 분. 복귀시킵니까?

### SC_051 · LOC_003_CHEONDUNG_BASE · CHAR_001 · UAV_001 · still_kenburns · 6:44–6:52
[ACTION-VI] Ảnh: 한승우 nhìn xuống màn hình đã tối, bóng ông và bóng lính phản chiếu trên mặt kính; sau lưng là K2 dưới lưới, máy phát K151 im, nắp đậy. Ken-burns đẩy vào mặt kính.
[SOUND] gió, xa xa vọng trống Tùy — gần như tưởng tượng.
N: 그는 숫자를 세지 않았습니다. 발전기도 돌리지 않았습니다. 소리는 십 리를 갔습니다. 강 건너에 있는 건 군대가 아니었습니다. 나라 하나가 움직이고 있었습니다.

### SC_052 · LOC_003_CHEONDUNG_BASE · — · UAV_001 · still_kenburns · 6:52–7:00
[ACTION-VI] Ảnh: drone #1 nhỏ như hạt bụi bay về phía máy trên nền trời xám bạc; dưới là thảo nguyên vàng; xa nơi chân trời tây, một dải bụi mỏng. Ken-burns đẩy vào chân trời.
[SOUND] rotor xa dần, gió.
N: 드론은 돌아왔습니다. 배터리 여섯 분이 남아 있었습니다. 그게 무엇이든, 이쪽으로 오고 있었습니다. 이제 그들에게 필요한 것은 총이 아니라 시간이었습니다.

[MID-ROLL 1 · 7:00]

[Kết thúc Phần 3]

## [Phần 4] 첫 접촉 — 「첫 접촉」 / Cuộc chạm trán đầu tiên  (7:00–10:30)
> Tóm tắt VI: (a) LỊCH SỬ thuần: cầu phao đẩy sang ngắn hơn bờ 1장; quân Goguryeo từ bờ cao xông xuống; lính Tùy nhảy xuống nước, thua; 맥철장 chết; cầu kéo về. (b) HIỆN ĐẠI: 백성민 rút mũi tên khỏi lốp, lần theo vết móng tới khe cạn → cậu bé trinh sát Goguryeo (~17) giương cung run tay. 백성민 đặt súng xuống, trả mũi tên. Cậu bé: "수나라?" → chỉ tây: "백만." 한승우 tới; cậu nhìn 태극기 không biết. K21 nổ máy → cậu ngã, chạy về đông.
> Chức năng: THREAT (sử) + CONTACT · Tài nguyên: — · Combat (sử): SC_054–059 video + SC_077 · Payoff: trả mũi tên (P1) · Open loop: "다리는 이틀 뒤 다시 놓였습니다. 이번엔 길이가 맞았습니다."
> Sau mid-roll 1: SC_053 aerial cầu phao 8 s, không thoại, không narration.

### SC_053 · LOC_001_YOHA · quân Goguryeo, lính Tùy · VEH_205, WPN_101, WPN_201 · video8s · 7:00–7:08
[ACTION-VI] Aerial wide chậm: ba cầu phao thuyền gỗ đang được đẩy từ bờ tây sang bờ đông sông Liêu, hàng nghìn lính Tùy dồn trên ván cầu, cờ đỏ; từ bờ đông cao, những mũi tên thăm dò đầu tiên của Goguryeo rơi xuống nước quanh đầu cầu, khiên đỏ giơ lên. Không thoại, không narration.
[SOUND] trống Tùy nhịp chậm, tiếng hò đẩy cầu, tên rơi nước.

### SC_054 · LOC_001_YOHA · lính Tùy, quân Goguryeo · VEH_205, WPN_101, WPN_201 · video8s · 7:08–7:16
[ACTION-VI] Đầu cầu phao dừng giữa nước, cách bờ đông cao dốc một khoảng nước đục; lính Tùy dồn ở mép ván — từ bờ cao, loạt tên đầu tiên cắm xuống ván cầu, người ngã xuống nước, khiên đỏ giơ lên muộn. Máy từ trên cầu nhìn về bờ.
[SOUND] nước, tên cắm gỗ, la hét, trống ngừng.
N: 다리는 동쪽 기슭보다 한 장, 세 미터가 짧았습니다. 그 세 미터가 첫 번째 싸움을 결정했습니다. 다리를 놓은 사람은 강폭을 잘못 쟀습니다.

### SC_055 · LOC_001_YOHA · quân Goguryeo · WPN_101 · video8s · 7:16–7:24
[ACTION-VI] Trên bờ đông cao: hàng lính Goguryeo giáp lamellar sắt, mũ chỏm lông, cờ 삼족오 đen — đứng dậy khỏi cỏ vàng, cung 맥궁 giương đồng loạt, bắn xuống. Low-angle từ mép nước.
[SOUND] dây cung bật hàng loạt, tên rít.
N: 고구려군은 높은 기슭에서 기다리고 있었습니다. 수나라가 강을 재는 동안 그들은 기슭을 골랐습니다. 기슭이 곧 성벽이었습니다.

### SC_056 · LOC_001_YOHA · lính Tùy · VEH_205, WPN_201 · video8s · 7:24–7:32
[ACTION-VI] Lính Tùy nhảy từ đầu cầu xuống nước ngang ngực, khiên đỏ giơ trên đầu, lội về bờ; tên cắm vào khiên, vào nước; người ngã kéo theo người sau. Tracking ngang.
[SOUND] nước bắn, khiên gỗ chịu tên, la hét.
N: 먼저 물에 들어간 쪽이 불리했습니다. 갑옷은 젖으면 두 배로 무거웠습니다. 고구려는 그것을 알고 물가에서 기다렸습니다.

### SC_057 · LOC_001_YOHA · quân Goguryeo, lính Tùy · WPN_101 · video8s · 7:32–7:40
[ACTION-VI] Mép nước: lính Goguryeo từ trên bùn cao đâm giáo xuống; lính Tùy trượt trên bùn dốc, không lên nổi, giáp ướt nặng. Cận trung, không gore.
[SOUND] giáo chạm giáp, bùn, tiếng thở.
N: 물속에서 싸운 쪽이 졌습니다. 진흙 기슭은 오르는 자에게 벽이었습니다. 이기려면 기슭에 서 있어야 했습니다.

### SC_058 · LOC_001_YOHA · 맥철장 (tướng Tùy), lính Tùy · VEH_205 · video8s · 7:40–7:48
[ACTION-VI] Một tướng Tùy giáp 명광개 hai gương ngực, áo choàng đỏ, mũ chỏm tua — khuỵu xuống ở mép ván cầu; hai lính kéo ông về, áo choàng trôi trên nước. Máy từ trên cầu nhìn xuống.
[SOUND] la hét, nước, trống Tùy vang lên gấp gáp rồi tắt.
N: 선봉장 맥철장이 그 물가에서 죽었습니다. 황제의 장수가 강 하나를 건너지 못한 것입니다.

### SC_059 · LOC_001_YOHA · lính Tùy, quân Goguryeo · VEH_205, WPN_101 · video8s · 7:48–7:56
[ACTION-VI] Ba cầu phao bị kéo ngược về bờ tây, dây neo căng; lính Tùy còn trên ván bám dây bò lùi, tên Goguryeo vẫn rít theo cắm xuống ván và nước; mặt sông đầy khiên đỏ trôi. Wide từ bờ đông, hàng Goguryeo tiền cảnh.
[SOUND] dây thừng nghiến, tên rơi nước, nước.
N: 전사웅, 맹차 두 장수도 함께 죽었습니다. 수나라는 다리를 도로 끌어갔습니다. 첫 도하는 실패였습니다. 다리는 그날 밤 다시 만들어지기 시작했습니다.

### SC_060 · LOC_001_YOHA · kỵ Goguryeo, lính Tùy · VEH_101, WPN_101, WPN_201 · video8s · 7:56–8:04
[ACTION-VI] Kỵ binh Goguryeo giáp ngựa lao xuống bãi bùn truy đuổi lính Tùy còn lội ngược về đầu cầu đang bị kéo; từ bờ tây, cung nỏ Tùy bắn trả, tên cắm quanh vó ngựa; kỵ Goguryeo ghì cương ở mép nước, không đuổi thêm. Tracking ngang thấp. Không cận thương vong.
[SOUND] vó ngựa trên bùn, nỏ Tùy bật, tên cắm bùn, tù và thu quân.
N: 고구려는 이겼습니다. 그날은. 강 건너의 숫자는 하나도 줄지 않았습니다. 이틀 뒤, 다리는 다시 올 것이었습니다.

### SC_061 · LOC_003_CHEONDUNG_BASE · CHAR_006 · VEH_003 · video8s · 8:04–8:12
[ACTION-VI] HARD CUT: 백성민 quỳ bên lốp K511 #2, nắm cán mũi tên bằng hai tay, rút một nhát — lốp xì hơi dài. Anh nhìn đầu tên tam giác có ngạnh, nhét mũi tên vào dây giáp ngực.
[SOUND] lốp xì, gió.
N: 화살에는 주인이 있었습니다. 백성민은 그 주인을 찾으러 갔습니다. 셋만 데리고, 총은 어깨에 멘 채였습니다.

### SC_062 · LOC_003_CHEONDUNG_BASE (rìa đông, cỏ → khe cạn) · CHAR_006 + 2 lính trinh sát · — · video8s · 8:12–8:20
[ACTION-VI] 백성민 đi khom dẫn hai lính trinh sát theo hàng vết móng ngựa qua cỏ vàng cao đến gối, xuống một khe cạn đáy đá cuội. Tay ra hiệu dừng — ngồi. Tracking phía sau.
[SOUND] cỏ khô, đá cuội lăn, gió.
N: 발자국은 동쪽으로, 마른 개울까지 이어졌습니다. 말 한 필. 편자는 없었습니다. 백성민은 발자국의 주인이 혼자라고 판단했습니다.

### SC_063 · LOC_003_CHEONDUNG_BASE (khe cạn) · CHAR_006, 소년 척후 · WPN_101 · video8s · 8:20–8:28
[ACTION-VI] Over-the-shoulder từ sau vai 백성민: cách 10 m trong khe đá, một cậu bé ~17 tuổi, áo 저고리 gai nâu, khăn 건 trên đầu, cung 맥궁 giương hết cỡ — mũi tên chĩa thẳng, hai tay run thấy rõ.
[SOUND] dây cung kêu căng, thở gấp của cậu bé, gió trên khe.
N: 열일곱쯤 된 소년이었습니다. 요동성의 척후였습니다. 어제 타이어에 화살을 쏜 것도 그였습니다.

### SC_064 · LOC_003_CHEONDUNG_BASE (khe cạn) · CHAR_006 + 2 lính · WPN_001 · video8s · 8:28–8:36
[ACTION-VI] 백성민 chậm rãi hạ K2C1 xuống đá, hai lòng bàn tay mở ra hai bên, lùi nửa bước; tay trái ra hiệu sau lưng — hai lính hạ nòng súng xuống đất. Cậu bé vẫn giương cung.
[SOUND] báng súng chạm đá, gió.
N: 이 땅에서 처음 만난 사람이었습니다. 총을 겨눌 수는 없었습니다. 백성민은 그렇게 배웠습니다. 사냥꾼은 처음 보는 것을 쏘지 않는 법이었습니다.

### SC_065 · LOC_003_CHEONDUNG_BASE (khe cạn) · CHAR_006, 소년 척후 · PROP_015 · video8s · 8:36–8:44
[ACTION-VI] 백성민 rút mũi tên từ giáp ngực, chìa ra bằng hai tay, đuôi tên hướng về cậu bé, đầu tên về phía mình; đặt xuống phiến đá giữa hai người, lùi lại.
[SOUND] mũi tên chạm đá, gió.
N: 화살을 돌려주는 것. 그가 아는 유일한 인사였습니다. 소년은 그 인사를 알아들었습니다.
백성민: 네 화살이다. 돌려준다.

### SC_066 · LOC_003_CHEONDUNG_BASE (khe cạn) · 소년 척후 · PROP_015 · video8s · 8:44–8:52
[ACTION-VI] Cận cậu bé: mắt nhìn mũi tên trên đá, nhìn lên vai áo 백성민 — miếng vải nhỏ đỏ-xanh (태극기) — cung hạ dần từng chút, giọng vỡ.
[SOUND] dây cung chùng, thở.
N: 소년에게 세상은 둘뿐이었습니다. 고구려와 수나라. 이들은 둘 다 아니었습니다.
소년 척후: 수나라… 수나라 사람이오?

### SC_067 · LOC_003_CHEONDUNG_BASE (khe cạn) · CHAR_006, 소년 척후 · — · video8s · 8:52–9:00
[ACTION-VI] 백성민 lắc đầu chậm, một lần. Cậu bé cúi nhặt mũi tên, rồi giơ tay chỉ về phía tây — bàn tay vẫn run; nói như người vừa chạy suốt đêm.
[SOUND] gió, tiếng nuốt.
N: 백만. 소년이 서쪽에서 본 것은 그것이었습니다. 그는 그 숫자를 성에 전하러 가는 길이었습니다.
소년 척후: 백만. 백만이오.

### SC_068 · LOC_003_CHEONDUNG_BASE (khe cạn) · 소년 척후 · PROP_015 · still_kenburns · 9:00–9:10
[ACTION-VI] Ảnh cận cậu bé: mặt lấm bụi vàng, mắt to, mũi tên nhận lại nắm chặt trong tay, phía sau là vách khe đá xám. Ken-burns đẩy vào mắt.
[SOUND] gió, im.
N: 백만. 소년은 그 수를 세어 본 적이 없었습니다. 들었을 뿐입니다. 하지만 그 말은 정확했습니다. 백만은 이백만이 아니었지만, 소년에게는 같은 말이었습니다.

### SC_069 · LOC_003_CHEONDUNG_BASE (mép khe) · CHAR_001, 소년 척후 + 2 lính · — · video8s · 9:10–9:18
[ACTION-VI] 한승우 cùng hai lính đi tới mép khe phía trên, dừng lại nhìn xuống. Cậu bé ngước lên: mắt dừng ở lá cờ 태극기 trên vai 한승우 — không nhận ra, ánh mắt trống, rồi nhìn xuống nòng súng.
[SOUND] cỏ, gió, đá lăn.
N: 태극기. 소년이 알 리 없는 깃발이었습니다. 천 년도 더 뒤에 생길 깃발이었습니다.

### SC_070 · LOC_003_CHEONDUNG_BASE (khe cạn) · CHAR_001, 소년 척후 · — · video8s · 9:18–9:26
[ACTION-VI] 한승우 trượt xuống khe, quỳ một gối ngang tầm mắt cậu bé, chỉ ngực mình, lắc đầu, rồi chỉ về đông; nói chậm, từng chữ.
[SOUND] gió, im.
N: 한승우는 첫 질문으로 성을 물었습니다. 이유가 아니라 위치였습니다. 이유를 물으면 답이 없었습니다. 위치를 물으면 답이 있었습니다.
한승우: 우리는 수나라가 아닙니다. 성은 어디입니까?

### SC_071 · LOC_003_CHEONDUNG_BASE (khe cạn) · 소년 척후, CHAR_001 · VEH_002 · video8s · 9:26–9:34
[ACTION-VI] Cậu bé giơ tay chỉ về đông, môi mấp máy "요동…" — đúng lúc từ sau gò cỏ, K21 천둥 2 nổ máy, tiếng gầm diesel dội xuống khe, tháp pháo nhô lên khỏi cỏ.
[SOUND] động cơ K21 nổ đột ngột, dội vách đá.
N: 요동성. 소년의 입에서 처음 나온 지명이었습니다. 요동의 심장. 백만이 노리는 첫 번째 성이었습니다.
소년 척후: 요동… 요동성이오.

### SC_072 · LOC_003_CHEONDUNG_BASE (khe cạn) · 소년 척후, CHAR_006 · VEH_002 · video8s · 9:34–9:42
[ACTION-VI] Cậu bé ngã ngồi, bò lùi trên đá cuội, mắt dán vào tháp pháo K21 trên gò; 백성민 giơ tay mở "không sao" — nhưng cậu đã lật người dậy.
[SOUND] đá cuội, động cơ nền, thở gấp.
N: 쇠로 된 집이 울었습니다. 소년에게는 그렇게 보였습니다. 그 소리는 그가 아는 어떤 짐승의 것도 아니었습니다.

### SC_073 · LOC_003_CHEONDUNG_BASE (cỏ phía đông) · 소년 척후, CHAR_001 + 2 lính · — · video8s · 9:42–9:50
[ACTION-VI] Cậu bé chạy về phía đông qua cỏ vàng, cung trên lưng, mũi tên vẫn nắm trong tay; hai lính định lao theo — 한승우 giơ thẳng cánh tay chặn, không nói. Wide.
[SOUND] cỏ khô bị đạp, thở, gió.
N: 한승우는 소년을 보냈습니다. 그가 달려가는 곳에 성이 있을 것이었습니다. 잡아 두면 얻는 것은 적 하나뿐이었습니다.

### SC_074 · LOC_003_CHEONDUNG_BASE (đồng cỏ) · 소년 척후 · — · still_kenburns · 9:50–10:00
[ACTION-VI] Ảnh: bóng cậu bé nhỏ dần trên biển cỏ vàng, bóng đổ dài, chân trời đông xám. Ken-burns theo hướng chạy.
[SOUND] gió.
N: 소년은 성으로 달렸습니다. 보고할 말은 하나였습니다. 쇠로 된 집. 그 말은 그날 저녁 말객의 귀에 들어갔습니다. 쇠로 된 집. 말객은 그 말을 두 번 되물었습니다.

### SC_075 · LOC_003_CHEONDUNG_BASE · CHAR_002, CHAR_001 · VEH_002 · video8s · 10:00–10:08
[ACTION-VI] 오태민 đứng trên nóc K21, kính bảo hộ gác mũ, hai tay chống hông, gào xuống. 한승우 dưới cỏ ngước lên, mặt không đổi.
[SOUND] động cơ K21 tắt, gió.
N: 오태민은 포로를 원했습니다. 한승우는 길잡이를 원했습니다. 두 사람은 같은 소년에게서 다른 것을 보았습니다.
오태민: 왜 보내십니까? 잡았어야 합니다!

### SC_076 · LOC_003_CHEONDUNG_BASE · CHAR_001, CHAR_006 · — · video8s · 10:08–10:16
[ACTION-VI] 한승우 không đáp 오태민; quay sang 백성민 đang nhặt lại K2C1, chỉ về hướng đông. 백성민 gật, rút sổ nhỏ ghi phương vị.
[SOUND] gió, bút.
N: 방향은 동쪽. 성은 그쪽에 있었습니다. 백만은 반대쪽이었습니다. 이제 이 부대에게도 방향이 생겼습니다.
한승우: 백 중사. 소년이 간 방향, 기록해.

### SC_077 · LOC_001_YOHA · quân Goguryeo, quân Tùy · VEH_205, WPN_201, VEH_101 · still_kenburns · 10:16–10:26
[ACTION-VI] Ảnh aerial: ba cầu phao nối dài chạm hẳn bờ đông; quân Tùy tràn sang thành hàng; trên bờ, hàng lính Goguryeo vỡ dưới mưa tên và kỵ binh Tùy, kỵ Goguryeo rút về đông trong bụi vàng. Ken-burns kéo ra.
[SOUND] trống Tùy dồn dập, vó ngựa, tù và Goguryeo thu quân.
N: 그 사이 요하에서는 두 번째 도하가 준비되고 있었습니다. 다리는 이틀 뒤 다시 놓였습니다. 이번엔 길이가 맞았습니다. 고구려군 만 명이 물가에서 무너졌고, 남은 이들은 요동성으로 물러났습니다.

[Kết thúc Phần 4]

## [Phần 5] 첫 방아쇠 — 「첫 방아쇠」 / Chứng minh sức mạnh  (10:30–14:00) — HỘI TỤ 2 TRACK
> Tóm tắt VI: Chiều ngày thứ ba (cầu nối lại sáng cùng ngày). Drone #1 (pin 12 phút, không sạc vì tránh tiếng máy phát) thấy 3 km đông-nam: đoàn dân chạy nạn ~300 người, xe bò — và 200 kỵ Tiên Ti của 탁발흠 vòng cắt đầu. 아리 kéo 을보 khỏi xe bò lật. 오태민 đòi K2; 박기철: lộ diện + dầu; 서아 im. 한승우: "쏜다. 대신 전차는 안 나간다." 2 K21 + 1소대 xuất kích 800 m; 40mm điểm xạ trước mũi kỵ binh, ngựa điên, đội hình vỡ; 탁발흠 mất ~40, vòng lên đồi. Cứu 을보 + 아리. Drone sà 40 m bám 탁발흠 → cung thủ bắn trúng cánh quạt. 2 lính trúng tên. 탁발흠 nhặt xác drone, nhìn K21 — đang học.
> Chức năng: BATTLE nhỏ · Tài nguyên: drone 4→3 · 40mm −60 · 2 thương binh · Open loop: "탁발흠은 도망치지 않았습니다. 언덕에서, 그는 세고 있었습니다." · [NARRATOR IM LẶNG] 11:54–13:14.

### SC_078 · LOC_003_CHEONDUNG_BASE · CHAR_005 · UAV_001 · video8s · 10:26–10:34
[ACTION-VI] Chiều ngày thứ ba, nắng bạc xiên qua bụi. Drone #1 treo thấp trên bãi trũng rồi bốc lên; 태오 dưới lưới ngụy trang, controller sáng; góc màn hình pin hiện 12; bốn viên pin dự trữ dán số vẫn nguyên trên giáp.
[SOUND] rotor, gió.
N: 이틀 뒤 오후. 다리가 놓인 지 반나절, 수나라 기병이 동안으로 올라왔습니다.
장태오: 1호기, 배터리 십이 분. 새 건전지는 아낍니다.

### SC_079 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ đông-nam, đoàn dân chạy nạn) · CHAR_005 · UAV_001 · video8s · 10:34–10:42
[ACTION-VI] Màn hình drone: cách 3 km, một đoàn người đi bộ dài trên cỏ vàng — bọc hành lý, xe bò hai bánh, trẻ con; phía sau rất xa, khói đen của làng cháy. Máy cận màn hình, ngón tay 태오 run trên cần.
[SOUND] rotor qua loa.
N: 요하 동쪽 마을들은 불탔습니다. 사람들은 성으로 걸었습니다. 성까지는 이틀 길이었습니다.
장태오: 피난민입니다. 삼백쯤… 소달구지도 있습니다.

### SC_080 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_005 · UAV_001, VEH_206 · video8s · 10:42–10:50
[ACTION-VI] Màn hình drone lia sang phải: 200 kỵ binh nhẹ — mũ lông, cung, ngựa lùn — chạy thành vòng cung rộng qua cỏ, cắt lên phía trước đầu đoàn dân; bụi thành dải.
[SOUND] rotor; tiếng thở gấp của 태오.
N: 이백 기. 피난민의 앞을 끊는 데는 충분한 수였습니다. 선비 기병은 앞을 끊고, 옆을 돌고, 뒤에서 쏩니다.
장태오: 기병… 이백. 앞을 끊고 있습니다.

### SC_081 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_004, CHAR_005; trên màn hình: CHAR_106, CHAR_107 · UAV_001 · video8s · 10:50–10:58
[ACTION-VI] Màn hình drone zoom: một xe bò lật nghiêng; cô gái hai bím tóc buộc chỉ đỏ (아리) kéo ông lão bọc hành lý sau lưng (을보) ra khỏi càng xe, ông lết một chân. 서아 nhìn qua vai 태오, tay đưa lên miệng.
[SOUND] rotor; tiếng thét rất nhỏ qua loa.
N: 선비족 기병이었습니다. 수나라의 눈이자 사냥개였습니다. 정면으로 싸우지 않고, 돌아서 끊는 자들이었습니다.

### SC_082 · LOC_003_CHEONDUNG_BASE · CHAR_002, CHAR_001 · VEH_004, VEH_001 · video8s · 10:58–11:06
[ACTION-VI] Cạnh K151: 오태민 chỉ thẳng tay về K2 dưới lưới, mặt đỏ, giọng to. 한승우 đứng im nhìn màn hình controller trong tay 태오.
[SOUND] gió, rotor qua loa.
N: 오태민에게 답은 늘 하나였습니다. 가장 큰 것을 쓰는 것. 그것은 사실이기도 했습니다.
오태민: 전차 내보냅니다. 한 발이면 다 흩어집니다.

### SC_083 · LOC_003_CHEONDUNG_BASE · CHAR_003 · VEH_001 · video8s · 11:06–11:14
[ACTION-VI] 박기철 đứng dựa váy xích K2, tay đặt lên tấm giáp như giữ nó lại, nói chậm, không to.
[SOUND] gió.
N: 박기철에게도 답은 하나였습니다. 기름은 목숨이었습니다. 전차 한 발은 시동 한 번이었고, 시동은 곧 노출이었습니다.
박기철: 나가면 들킵니다. 기름도요.

### SC_084 · LOC_003_CHEONDUNG_BASE · CHAR_004, CHAR_001 · UAV_001 · video8s · 11:14–11:22
[ACTION-VI] 서아 không nói — nhìn màn hình rồi ngẩng nhìn 한승우. 한승우 nhìn màn hình: cô gái vẫn đang kéo ông lão, kỵ binh đã cách đoàn dân một quãng ngắn. Máy đẩy chậm vào mặt 한승우.
[SOUND] rotor qua loa, tiếng thét mơ hồ, gió.
N: 아흔네 명을 데리고 돌아가는 것. 그것이 한승우의 임무였습니다. 화면 속 삼백 명은 임무에 없었습니다.

### SC_085 · LOC_003_CHEONDUNG_BASE · CHAR_001 · — · video8s · 11:22–11:30
[ACTION-VI] Cận 한승우: mắt rời màn hình, nhìn 오태민, rồi 박기철. Câu nói ngắn, không cao giọng.
[SOUND] gió ngừng một nhịp.
한승우: 쏜다. 대신 전차는 안 나간다.

### SC_086 · LOC_003_CHEONDUNG_BASE · CHAR_001 · EQP_002 · video8s · 11:30–11:38
[ACTION-VI] 한승우 bấm tổ hợp radio vai trái, mắt vẫn nhìn về phía đông-nam; sau lưng ông, lính 1소대 đã chạy về phía K21.
[SOUND] PTT, giày chạy trên cỏ.
N: 전차는 남았습니다. 쏘되, 가장 큰 것은 숨긴다. 그것이 첫 결정의 모양이었습니다.
한승우: 천둥 2, 3. 1소대 탑승. 팔백 미터, 정지 사격.

### SC_087 · LOC_003_CHEONDUNG_BASE · CHAR_003, 1소대 · VEH_002, VEH_001 · video8s · 11:38–11:46
[ACTION-VI] K21 천둥 2 và 3 xé lưới ngụy trang lao lên khỏi bãi trũng, cửa đuôi đang khép, lính cuối nhảy vào; K2 vẫn nằm dưới lưới; 박기철 đứng cạnh K2 nhìn theo hai xe. Wide.
[SOUND] hai động cơ K21 gầm, xích nghiến cỏ.
N: 한승우의 첫 번째 결정이었습니다. 그 결과는 이 부대를 끝까지 따라갈 것이었습니다.

[NARRATOR IM LẶNG — 11:54 → 13:14]

### SC_088 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_002 · VEH_002 · video8s · 11:46–11:54
[ACTION-VI] Hai K21 chạy song song qua cỏ vàng, bụi bốc sau đuôi; 오태민 nhô nửa người trên nóc 천둥 2, kính bảo hộ kéo xuống mắt; tháp 40mm xoay về phải. Tracking ngang thấp.
[SOUND] động cơ, xích, gió lùa.
N: 팔백 미터. 화살이 닿지 않는 거리였습니다.

### SC_089 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_205 · VEH_206 · video8s · 11:54–12:02
[ACTION-VI] Phía kỵ binh: 탁발흠 — sẹo thái dương trái, mũ vành lông cáo, áo choàng da sói xám, bím tóc dày — dẫn đầu, cung trong tay, ngựa phi; ông ngoái nhìn đầu đoàn dân, giơ cung ra hiệu vòng chặn. Tracking bên hông.
[SOUND] vó ngựa dồn, tiếng hú của kỵ binh.

### SC_090 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_002 · VEH_002 · video8s · 12:02–12:10
[ACTION-VI] K21 천둥 2 phanh gấp trên gò thấp, bụi trùm; 오태민 cúi vào cửa nóc, tay ấn tai nghe intercom, mắt nhìn qua ống nhòm về đầu kỵ binh cách 800 m — lệnh nội bộ xe cho pháo thủ.
[SOUND] phanh, xích dừng, PTT.
오태민: 포수, 선두 전방 오십. 점사.

### SC_091 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · — · VEH_002, VEH_206 · video8s · 12:10–12:18
[ACTION-VI] Wide: pháo 40mm bắn loạt ngắn — đất bùng lên thành cột 50 m trước mũi hàng kỵ binh dẫn đầu; ngựa dựng đứng, kỵ sĩ văng, hàng sau đâm vào hàng trước. Không cận thương vong.
[SOUND] 40mm nổ đanh ba phát, đất văng, ngựa hí.

### SC_092 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_002 · VEH_002, VEH_206 · video8s · 12:18–12:26
[ACTION-VI] Đội hình kỵ binh vỡ thành từng cụm quay cuồng, ngựa điên chạy ngược; từ nóc hai K21, xạ thủ K3 quét tracer thành dải sáng ngang cỏ; bụi phủ tất cả. Aerial trung; 오태민 (off, radio) ra lệnh tiến.
[SOUND] K3 quét dài, 40mm loạt thứ hai, ngựa, PTT.
오태민: 수레로 전진!

### SC_093 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ, chân đồi) · CHAR_205 · VEH_206 · video8s · 12:26–12:34
[ACTION-VI] 탁발흠 ghì cương, ngựa dựng — ông không nhìn trời, nhìn thẳng vào hai khối xe trên gò; hét một lệnh, quất ngựa vòng lên sườn đồi bên phải. Kỵ binh còn lại theo ông thành dòng.
[SOUND] ngựa hí, lệnh hét khàn, K3 xa.
탁발흠: 흩어져라! 언덕으로!

### SC_094 · LOC_008_GOGURYEO_VILLAGE (đoàn dân) · CHAR_004, CHAR_106, CHAR_107, 1소대 · VEH_002 · video8s · 12:34–12:42
[ACTION-VI] Lính 1소대 chạy tới xe bò lật, tỏa ra thành vòng; 서아 quỳ xuống bên chân 을보 đang chảy máu, kéo cắt băng; 아리 nắm tay áo cô, nói gấp.
[SOUND] giày trên cỏ, kéo cắt vải, tiếng khóc trẻ con xa.
아리: 할아버지 다리요! 피가 안 멈춰요!

### SC_095 · LOC_008_GOGURYEO_VILLAGE (đoàn dân) · CHAR_004, CHAR_106 · — · still_kenburns · 12:42–12:52
[ACTION-VI] Ảnh cận: hai bàn tay găng nitrile của 서아 dính máu siết băng ép quanh bắp chân 을보; bàn tay già gân guốc của ông đặt lên tay cô. Ken-burns đẩy chậm. Không thoại.
[SOUND] gió, thở, xa xa động cơ K21.

### SC_096 · LOC_003_CHEONDUNG_BASE · CHAR_005 · UAV_001 · video8s · 12:52–13:00
[ACTION-VI] 태오 dưới lưới: màn hình drone theo dòng kỵ binh lên sườn đồi; cậu đẩy cần — hình ảnh hạ thấp dần, cỏ lớn lên trong khung, chỉ số độ cao giảm. Cận mặt và màn hình.
[SOUND] rotor, bíp độ cao.
장태오: 저 놈이 우두머리입니다. 따라갑니다.

### SC_097 · LOC_008_GOGURYEO_VILLAGE (sườn đồi) · CHAR_205, cung thủ Tiên Ti · VEH_206, UAV_001 · video8s · 13:00–13:08
[ACTION-VI] Sườn đồi: 탁발흠 ngẩng lên — một vật vo ve bay thấp 40 m trên đầu; ông chỉ tay; cung thủ bên cạnh giương cung, ngắm, thả. Low-angle theo mũi tên bay lên.
[SOUND] rotor gần, dây cung bật, tên rít.

### SC_098 · LOC_003_CHEONDUNG_BASE · CHAR_005 · UAV_001 · video8s · 13:08–13:16
[ACTION-VI] Màn hình drone: hình xoay tít, một mảnh cánh quạt gãy lướt qua ống kính, cỏ lao lên → nhiễu → đen. 태오 bấm cần liên tục vô ích.
[SOUND] rotor rít lệch, tín hiệu đứt, bíp mất kết nối.
장태오: 1호기… 신호 끊겼습니다.

### SC_099 · LOC_008_GOGURYEO_VILLAGE (đoàn dân) · CHAR_004, 2 lính bị thương · VEH_002 · video8s · 13:16–13:24
[ACTION-VI] Sau đuôi K21 천둥 3: hai lính được kéo vào khuất — một mũi tên xuyên cẳng tay, một cắm đùi; 서아 buộc garô, mặt bình tĩnh. Máy trung, không cận vết thương.
[SOUND] tên rơi lác đác quanh xe, rên, lệnh "올려!".
N: 총이 있어도, 화살은 여전히 피를 냈습니다. 방탄복은 가슴만 가렸습니다.

### SC_100 · LOC_008_GOGURYEO_VILLAGE (đoàn dân) · CHAR_106, CHAR_107, 1소대 · VEH_002 · video8s · 13:24–13:32
[ACTION-VI] 을보 được một lính dìu tới cửa đuôi K21 mở, 아리 ôm giỏ theo sát; một mũi tên bay tới đập "캉" vào giáp xe cạnh vai ông — ông không né, dừng lại, đặt bàn tay lên tấm giáp thép, vuốt như vuốt cổ ngựa, nheo mắt trái, rồi mới bước lên. Lính bên cạnh bắn trả một loạt ngắn về sườn đồi.
[SOUND] tên đập thép, K2C1 loạt ngắn, động cơ xe chờ, bàn tay trên thép.
N: 을보 영감, 요동성의 대장장이. 쇠를 만지는 것은 그의 인사였습니다. 그는 쇠를 만지고 나서야 사람을 믿었습니다.
을보: 이 쇠는… 우리 쇠가 아니야.

### SC_101 · LOC_008_GOGURYEO_VILLAGE (sườn đồi) · CHAR_205, cung thủ Tiên Ti · VEH_206, VEH_002 · still_kenburns · 13:32–13:42
[ACTION-VI] Ảnh wide: sườn đồi cỏ vàng, 탁발흠 đã xuống ngựa đứng giữa đám kỵ binh còn lại; theo tay ông chỉ, một hàng cung thủ Tiên Ti giương cung bắn một loạt thử về hai K21 đang quay đầu về đông — chùm tên rơi cắm xuống cỏ, hụt xa trước xe; dưới đồng, ngựa mất chủ chạy tán loạn, bụi tan dần. Ken-burns từ chùm tên cắm cỏ kéo ra tới 탁발흠.
[SOUND] dây cung hàng loạt, tên rơi cỏ xa, gió, ngựa hí.
N: 탁발흠은 기병 마흔을 잃었습니다. 그는 물러나지 않았습니다. 화살 한 줄을 쏘게 했습니다. 닿지 않았습니다. 그것도 배움이었습니다. 살아남은 백육십 기는 언덕 위에서 쉬었습니다.

### SC_102 · LOC_008_GOGURYEO_VILLAGE (sườn đồi) · CHAR_205 · UAV_001 · video8s · 13:42–13:50
[ACTION-VI] 탁발흠 đi bộ tới chỗ cỏ rạp, cúi xuống nhấc xác drone #1 lên bằng một cánh tay gãy, xoay nó trước mặt; máu chảy một vệt từ tai trái. Ông ngẩng lên nhìn về hai K21 — mặt không sợ, mắt đang ghi.
[SOUND] nhựa gãy kêu, gió.
N: 그는 이름을 붙이지 않았습니다. 먼저 살펴보았습니다. 요술이라 부르는 자는 배우지 못하는 법이었습니다.

### SC_103 · LOC_008_GOGURYEO_VILLAGE (sườn đồi) · CHAR_205 · UAV_001, VEH_002 · still_kenburns · 13:50–14:00
[ACTION-VI] Ảnh: 탁발흠 là chấm nhỏ trên đồi, tay cầm drone; dưới đồng, đoàn dân chạy nạn nối lại hàng đi về đông, hai K21 đi kèm hai bên, bụi. Ken-burns đẩy chậm vào 탁발흠.
[SOUND] gió.
N: 쇠수레 둘. 사람은 백 남짓. 탁발흠은 도망치지 않았습니다. 언덕에서, 그는 세고 있었습니다.

[MID-ROLL 2 · 14:00]

[Kết thúc Phần 5]

## [Phần 6] 어느 성의 군사요 — 「어느 성의 군사요」 / Liên minh không dễ  (14:00–17:30)
> Tóm tắt VI: Hoàng hôn. 300 kỵ binh Goguryeo của 해모루 dàn trên gò, cậu bé trinh sát chỉ tay. Đại đội dàn K21, nòng hạ. 을보 lết ra giữa: "이들이 우릴 살렸소!" 해모루 xuống ngựa, nhìn 태극기: "삼족오가 아니오. 그대들은 어느 성의 군사요?" 한승우: "성이… 없습니다." Năm: 한승우 TỰ SUY "수나라… 백만… 요동성. 육백십이 년." → 해모루 xác nhận bằng lịch đương thời "대왕 재위 이십삼 년이오." (không dùng 시호) → "육백십이년… 살수". Mặc cả: vào thành (bị vây) hay đi tây (오태민); "식량 이틀" quyết thay họ. Điều kiện: đi ngay trong đêm. 백성민 ↔ 해모루 nhìn nhau.
> Chức năng: POLITICS · Tài nguyên nói thành lời: "식량 이틀 치" · Open loop: "한승우는 이 전쟁의 결말을 알고 있었습니다. 문제는, 자신들이 그 결말에 없다는 것이었습니다."
> Sau mid-roll 2: SC_104 cận xác drone trong tay 탁발흠 8 s, không thoại.

### SC_104 · LOC_008_GOGURYEO_VILLAGE (sườn đồi) · CHAR_205 · UAV_001 · video8s · 14:00–14:08
[ACTION-VI] Cận: xác drone #1 trong bàn tay 탁발흠 xoay chậm — cánh quạt gãy, một cánh tay cong, đèn LED tắt, tem 태극기 nhỏ trên thân; nền trời hoàng hôn cam xám. Không thoại, không narration.
[SOUND] gió, nhựa gãy kêu khẽ.

### SC_105 · LOC_003_CHEONDUNG_BASE (gò phía đông, hoàng hôn) · CHAR_105, 소년 척후 · VEH_101 · still_kenburns · 14:08–14:18
[ACTION-VI] Ảnh: trên gò cỏ vàng ngược sáng hoàng hôn, 300 kỵ binh Goguryeo dàn hàng — giáp lamellar, ngựa mặc giáp, chỏm lông đỏ, cờ 삼족오; ở giữa, 해모루 (không râu, một lông trắng trên mũ) trên ngựa; cậu bé trinh sát đứng bên cạnh chỉ tay xuống. Ken-burns kéo ra dọc hàng kỵ.
[SOUND] ngựa thở, giáp lách cách, gió chiều.
N: 해 질 무렵, 삼백 기가 언덕에 섰습니다. 소년이 길을 안내했습니다. 쇠로 된 집이라는 말을 확인하러 온 것이었습니다. 삼백 기 앞에 선 것은 쇠수레 셋과 아흔네 명이었습니다.

### SC_106 · LOC_003_CHEONDUNG_BASE (dưới gò) · CHAR_002, đại đội · VEH_002 · video8s · 14:18–14:26
[ACTION-VI] Dưới gò: ba K21 dàn ngang, nòng 40mm hạ thấp, lính nấp sau xe; 오태민 trên nóc 천둥 2 áp tai nghe, mắt không rời hàng kỵ binh. Over-the-shoulder từ sau 오태민 nhìn lên gò.
[SOUND] động cơ chờ, PTT.
N: 삼백 기, 사거리 안. 오태민의 셈은 늘 그렇게 시작했습니다. 그에게 사거리 안은 곧 표적이었습니다.
오태민: 중대장님, 삼백입니다. 사거리 안입니다.

### SC_107 · LOC_003_CHEONDUNG_BASE (dưới gò) · CHAR_001 · VEH_002, EQP_002 · video8s · 14:26–14:34
[ACTION-VI] 한승우 đứng trước mũi 천둥 3, giữa khoảng trống, tay trái giữ tổ hợp radio, tay phải giơ ngang ra sau ra hiệu cho các xe; nòng 40mm phía sau ông hạ thêm.
[SOUND] PTT, tháp pháo quay hạ.
N: 한승우의 셈은 달랐습니다. 이들은 서쪽의 그들이 아니었습니다. 쏘지 않는 것이 그날 두 번째 결정이었습니다.
한승우: 전 차량, 포신 내려. 사격 금지.

### SC_108 · LOC_003_CHEONDUNG_BASE (khoảng trống giữa hai bên) · CHAR_106 · — · video8s · 14:34–14:42
[ACTION-VI] 을보 chân băng trắng lết ra khoảng trống giữa hai hàng, bọc hành lý vẫn trên lưng, giơ hai tay lên phía gò, gào bằng giọng khàn của ông già không sợ ai.
[SOUND] gió, tiếng gào vang.
N: 을보 영감이 먼저 나섰습니다. 예순여섯 살 노인에게 두 군대 사이는 무섭지 않았습니다. 이들이 손녀를 살렸기 때문입니다.
을보: 이들이 우릴 살렸소!

### SC_109 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_105 · VEH_101 · video8s · 14:42–14:50
[ACTION-VI] 해모루 xuống ngựa, ném cương cho lính, đi bộ xuống dốc một mình — tay không chạm chuôi kiếm — dừng cách 한승우 ba bước; mắt ông dừng ở lá cờ 태극기 trên vai áo 한승우. Máy đẩy chậm.
[SOUND] giày da trên cỏ, giáp lách cách.
N: 해모루 말객. 을지문덕 장군의 사람이었습니다. 칼보다 질문을 먼저 꺼내는 사람이었습니다. 그는 이날 처음으로 답이 없는 질문을 하게 됩니다.

### SC_110 · LOC_003_CHEONDUNG_BASE (khoảng trống) · 소년 척후, CHAR_105, CHAR_006 · — · video8s · 14:50–14:58
[ACTION-VI] Cậu bé trinh sát chạy xuống theo, đứng sau 해모루, giơ tay chỉ 백성민 đang đứng cạnh K21 — mũi tên của cậu vẫn cầm trong tay.
[SOUND] gió, thở gấp.
N: 소년은 약속을 지켰습니다. 그것이 첫 번째 신용이었습니다. 화살을 돌려준 자는 적이 아니었습니다. 소년의 법이었습니다.
소년 척후: 저 사람이오. 화살을 돌려준 사람.

### SC_111 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_105, CHAR_001 · — · video8s · 14:58–15:06
[ACTION-VI] Cận 해모루: mắt từ 태극기 lên mặt 한승우, giọng đều, không thù không thân.
[SOUND] gió.
해모루: 삼족오가 아니오. 그대들은 어느 성의 군사요?

### SC_112 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_001 · — · video8s · 15:06–15:14
[ACTION-VI] Cận 한승우: một nhịp im — ông nhìn xuống hàng xe, nhìn lại 해모루; trả lời thật.
[SOUND] gió, xa xa ngựa hí.
N: 성이 없다. 이 시대에 그것은 군대가 아니라는 뜻이었습니다. 성이 없는 자는 어디에도 속하지 않는 자였습니다.
한승우: 성이… 없습니다.

### SC_113 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_105 · VEH_002 · video8s · 15:14–15:22
[ACTION-VI] 해모루 liếc dọc thân K21, tấm phao gấp, nòng 40mm, rồi quay lại nhìn thẳng 한승우; hỏi như thẩm vấn nhưng không lớn tiếng.
[SOUND] giáp lách cách.
N: 해모루는 쇠수레보다 사람을 먼저 보았습니다. 어디서 왔는지가 무엇을 가졌는지보다 중요했습니다. 그가 을지문덕에게 보고할 것도 그것이었습니다.
해모루: 그대들은 어디서 왔소?

### SC_114 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_001 · — · video8s · 15:22–15:30
[ACTION-VI] 한승우 không trả lời câu hỏi — mắt ông đi từ hàng kỵ binh giáp lamellar, sang cờ 삼족오, sang phía tây nơi cậu bé đã chỉ; môi ông nhẩm từng chữ như cộng một phép tính, rồi nói ra kết quả — và câu ấy làm 해모루 nhíu mày.
[SOUND] gió, thì thầm.
N: 한승우는 대답 대신 셈을 했습니다. 수나라, 백만, 요동성. 학교에서 배운 세 단어였습니다. 세 단어가 가리키는 해는 하나뿐이었습니다.
한승우: 수나라… 백만… 요동성. 육백십이 년.

### SC_115 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_105 · — · video8s · 15:30–15:38
[ACTION-VI] 해모루 nhíu mày — con số kia không có nghĩa với ông; ông trả lời bằng lịch của mình, chậm, rõ từng chữ, như sửa cho người nói sai.
[SOUND] gió.
N: 해모루는 이 땅의 달력으로 답했습니다. 왕의 이름이 아니라, 왕의 햇수였습니다. 그것이 확인이었습니다.
해모루: 대왕 재위 이십삼 년이오.

### SC_116 · LOC_003_CHEONDUNG_BASE (bên K21) · CHAR_001, CHAR_003 · VEH_002 · video8s · 15:38–15:46
[ACTION-VI] 한승우 quay nửa người về 박기철 đứng sát sau, nói rất nhỏ như tự nói; 박기철 nhìn ông — chưa hiểu, rồi mặt ông đổi.
[SOUND] gió, tiếng thì thầm.
N: 재위 이십삼 년. 한승우의 셈과 같은 해였습니다. 초등학교 교과서의 두 단어가 눈앞에 있었습니다.
한승우: 육백십이년… 살수.

### SC_117 · LOC_003_CHEONDUNG_BASE · CHAR_001 · — · still_kenburns · 15:46–15:54
[ACTION-VI] Ảnh cận 한승우 nhìn xuống la bàn trên ngực, phía sau mờ là hàng kỵ binh trên gò ngược sáng. Ken-burns đẩy vào la bàn.
[SOUND] gió.
N: 영양왕 23년, 서기 612년. 대한민국 군인이라면 누구나 배운 해였습니다. 살수대첩의 해. 을지문덕, 삼십만 오천, 살아 돌아간 자 이천칠백. 결말을 아는 것과 그 안에서 사는 것은 다른 일이었습니다.

### SC_118 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_105 · VEH_002 · video8s · 15:54–16:02
[ACTION-VI] 해모루 chỉ tay về hàng K21, rồi về phía đông nơi thành ở, giọng như đã quyết thay họ.
[SOUND] gió.
N: 해모루의 제안은 명령에 가까웠습니다. 성주의 판단, 그것이 이 땅의 법이었습니다.
해모루: 쇠수레를 요동성으로 들이시오. 성주께서 판단하실 것이오.

### SC_119 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_001 · — · video8s · 16:02–16:10
[ACTION-VI] 한승우 lắc đầu một lần, chậm; hai tay chắp sau lưng.
[SOUND] gió.
N: 한승우는 성을 알았습니다. 성은 지키는 곳이지, 나가는 곳이 아니었습니다. 전차에게 성벽은 보호가 아니라 감옥이었습니다.
한승우: 성 안은 안 됩니다. 갇힙니다.

### SC_120 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_002 · VEH_002 · video8s · 16:10–16:18
[ACTION-VI] 오태민 nhảy xuống khỏi nóc K21, bước tới cạnh 한승우, chỉ về tây — nơi mặt trời đang lặn.
[SOUND] giày đập đất.
N: 오태민은 다리를 원했습니다. 다리를 끊으면 백만이 강 저쪽에 묶인다고 믿었습니다. 다리는 셋이었고, 이미 기병이 건너 있었습니다.
오태민: 서쪽으로 갑니다. 다리를 끊으면 끝입니다.

### SC_121 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_003 · — · video8s · 16:18–16:26
[ACTION-VI] 박기철 không nhìn ai, mở sổ bìa xanh, đọc một dòng, gập lại. Câu nói đặt dấu chấm cho cuộc cãi.
[SOUND] sổ gập.
N: 이틀. 어느 쪽으로 가든 사흘째는 굶는 것이었습니다. 박기철의 숫자는 늘 논쟁을 끝냈습니다.
박기철: 식량 이틀 치입니다. 이틀.

### SC_122 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_105 · — · video8s · 16:26–16:34
[ACTION-VI] 해모루 nhìn 박기철 — ông hiểu con số dù không hiểu "식량" kiểu nào; quay lại 한승우, chỉ về đồng bằng phía tây đang tối.
[SOUND] gió, kỵ binh trên gò chuyển động.
N: 곡식은 성에 있었습니다. 벌판은 내일이면 수나라의 것이었습니다. 해모루는 협박하지 않았습니다. 시간을 말했을 뿐입니다.
해모루: 곡식은 성에 있소. 단, 오늘 밤 안에 떠나야 하오.

### SC_123 · LOC_003_CHEONDUNG_BASE (khoảng trống) · CHAR_001, CHAR_002, CHAR_003 · VEH_002 · video8s · 16:34–16:42
[ACTION-VI] 한승우 nhìn 오태민 (cằm siết), 박기철 (gật nhẹ), rồi ngoảnh về hướng đông; ra lệnh ngắn.
[SOUND] gió.
N: 결정은 배가 내렸습니다. 한승우는 그것을 알면서 명령했습니다. 전차를 맨 뒤에 둔 것은 기름 때문이었습니다. 먼지 때문이기도 했습니다.
한승우: 밤에 이동한다. 전차는 맨 뒤.

### SC_124 · LOC_003_CHEONDUNG_BASE (bên K21) · CHAR_006, CHAR_105 · VEH_002 · video8s · 16:42–16:50
[ACTION-VI] 백성민 đứng cạnh xích K21, mũ boonie, sơn mặt hai vệt; 해모루 đi ngang qua, dừng nửa bước, nhìn anh — hai người lính trinh sát nhận ra nhau; 해모루 gật rất nhẹ; 백성민 gật lại. Không thoại.
[SOUND] giáp lách cách, gió.
N: 말은 필요 없었습니다. 척후는 척후를 알아보는 법이었습니다. 두 사람은 이후 넉 달을 같은 길에서 보내게 됩니다.

### SC_125 · LOC_003_CHEONDUNG_BASE (cửa đuôi K21) · CHAR_106, CHAR_001, CHAR_107 · VEH_002 · video8s · 16:50–16:58
[ACTION-VI] 을보 lết về cửa đuôi K21 nơi 아리 đang đứng ôm giỏ; ngang qua 한승우, ông nói không ngoảnh lại, giọng ông già nói với người trẻ.
[SOUND] chân lết trên cỏ.
N: 을보 영감은 성주를 알았습니다. 이 땅에서 그보다 좋은 소개장은 없었습니다.
을보: 대장 양반, 성주는 내가 아는 사람이야.

### SC_126 · LOC_003_CHEONDUNG_BASE · đại đội, kỵ binh Goguryeo · VEH_001, VEH_002, VEH_003, VEH_004, VEH_101 · still_kenburns · 16:58–17:06
[ACTION-VI] Ảnh wide: mặt trời chạm chân trời; kỵ binh Goguryeo xếp thành hàng dẫn đầu, phía sau đoàn xe hiện đại đã cuộn lưới, K2 đi cuối; bụi vàng ngược sáng. Ken-burns trượt ngang.
[SOUND] vó ngựa chậm, động cơ nổ máy lần lượt.
N: 삼백 기가 앞장섰습니다. 쇠수레 일곱 대가 뒤를 따랐습니다. 요동성까지 삼십 킬로. 전차에게는 기름 삼십 킬로였습니다. 밤길 삼십 킬로. 고구려 기병에게는 익숙한 길이었습니다.

### SC_127 · LOC_003_CHEONDUNG_BASE · CHAR_105, CHAR_001 · VEH_101, VEH_002 · video8s · 17:06–17:14
[ACTION-VI] 해모루 đã lên ngựa, ghì cương quay lại nhìn K21 lần nữa — tò mò thắng nghi ngờ; hỏi 한승우 đang bước lên K151.
[SOUND] ngựa dậm chân, động cơ.
N: 해모루는 쇠수레의 속도를 물었습니다. 한승우는 기름을 생각했습니다. 말보다 빠른 것은 확실했습니다. 말보다 오래 달리지는 못했습니다.
해모루: 한 대장. 저 쇠수레, 말보다 빠르오?

### SC_128 · LOC_003_CHEONDUNG_BASE · CHAR_001 · VEH_004, PROP_001 · video8s · 17:14–17:22
[ACTION-VI] 한승우 không trả lời; ngồi vào K151, mở bản đồ giấy Cheorwon, nhìn một giây, gấp lại nhét túi. Cận la bàn trên ngực: kim đứng yên, chỉ bắc.
[SOUND] giấy gấp, động cơ.
N: 철원의 지도는 이제 종이일 뿐이었습니다. 나침반만이 아직 쓸모가 있었습니다. 그것은 철원에서 가져온 것 중 유일하게 쓸모 있는 것이었습니다.

### SC_129 · LOC_003_CHEONDUNG_BASE · — · VEH_001, VEH_101 · still_kenburns · 17:22–17:30
[ACTION-VI] Ảnh: đoàn xe và kỵ binh thành một hàng dài đi vào bóng tối phía đông, chỉ còn vệt trời cam mỏng sau lưng. Ken-burns đẩy chậm theo hàng.
[SOUND] xích, vó ngựa, gió đêm.
N: 612년 봄. 살수까지는 넉 달이 남아 있었습니다. 한승우는 이 전쟁의 결말을 알고 있었습니다. 문제는, 자신들이 그 결말에 없다는 것이었습니다.

[Kết thúc Phần 6]

## [Phần 7] 쇠집은 문을 못 지난다 — 「쇠집은 문을 못 지난다」 / Kẻ địch thích nghi  (17:30–21:00)
> Tóm tắt VI: (a) ENEMY POV: trại tiền quân Tùy bờ đông — 탁발흠 đặt xác drone trước 전군총관; tướng cười "고구려 요술" nhưng giao 2.000 kỵ, lệnh khóa phía đông 요동성: "쌀 한 톨도". (b) Đêm hành quân 30 km: MINI-COMBAT — 백성민 thấy qua kính đêm 6 kỵ Tiên Ti bám đuôi; 해모루 phái 10 kỵ đuổi, tên cắm bạt K511; tới 요동성 — tường đá, 치, đuốc. Cổng 옹성 hẹp: K2 không lọt (박기철 đo bước). 고정수: "쇠수레를 성 안에 들이시오." 한승우: xe tăng trong thành = quan tài → thung lũng sau thành. 고정수 đồng ý với điều kiện: 한승우 + 10 người ngủ trong thành. Trên đường mòn vào thung lũng: 3 trinh sát Tiên Ti lộ, bị đuổi (chúng đã thấy đường mòn). Sáng: 박기철 "간밤에 전차 30km"; 백성민: đường đông bị cắt ngay đêm nay, 3.000 dân + xe lương. 고정수 giao nhiệm vụ: giữ đường đông một đêm.
> Chức năng: THREAT · Tài nguyên nói thành lời: "간밤에 전차 삼십 킬로 썼습니다" · Combat: SC_135–136, SC_144 (mini) · Enemy adaptation: 2.000 kỵ + lệnh khóa lương · Open loop: "성주는 쌀을 원했습니다. 탁발흠도 같은 것을 원했습니다."

### SC_130 · LOC_001_YOHA (trại tiền quân Tùy bờ đông, đêm) · — · WPN_201, PROP_016 · still_kenburns · 17:30–17:40
[ACTION-VI] Ảnh: trại Tùy đêm trên bờ đông sông Liêu — hàng lều xám, đuốc thành hàng, cờ đỏ-vàng, một lều tướng lớn giữa; xa xa cầu phao lấp lánh đuốc. Ken-burns đẩy vào lều tướng.
[SOUND] trống đêm, ngựa, lửa.
N: 같은 밤. 요하 동안, 수나라 전군 진영이었습니다. 대군이 오기 전에 길을 여는 부대였습니다. 그들은 대군보다 먼저 보고, 먼저 죽는 자들이었습니다.

### SC_131 · LOC_001_YOHA (lều 전군총관) · CHAR_205, 수 전군총관 · UAV_001 · video8s · 17:40–17:48
[ACTION-VI] Trong lều dưới đèn lồng: 탁발흠 đặt xác drone lên bàn thấp trước 전군총관 — giáp 명광개, râu dài, áo choàng đỏ. Tướng nhấc cánh quạt gãy lên bằng hai ngón, cười thành tiếng.
[SOUND] lửa đèn, tiếng cười.
N: 총관은 웃었습니다. 웃는 자는 보고를 반만 들었습니다. 선비 낭장의 말을 한족 장수가 다 믿을 리 없었습니다.
수 전군총관: 고구려 요술이로군.

### SC_132 · LOC_001_YOHA (lều 전군총관) · CHAR_205 · UAV_001 · video8s · 17:48–17:56
[ACTION-VI] 탁발흠 quỳ một gối, máu khô ở tai trái, mũ lông cầm tay; nói ngắn như báo cáo kỹ thuật, không ngẩng đầu.
[SOUND] lửa, giáp.
N: 탁발흠은 숫자로 보고했습니다. 요술이라는 말은 쓰지 않았습니다. 본 것만 말하는 것. 그것이 그가 살아남는 방식이었습니다.
탁발흠: 요술이 아닙니다. 쇠수레가 둘, 사람은 백 남짓입니다.

### SC_133 · LOC_001_YOHA (lều 전군총관) · 수 전군총관, CHAR_205 · UAV_001 · video8s · 17:56–18:04
[ACTION-VI] 전군총관 ném cánh quạt xuống bàn, đứng dậy, kéo tấm bản đồ lụa — chỉ vào phía đông 요동성; giọng lệnh.
[SOUND] cánh quạt rơi trên gỗ, lụa.
N: 이천 기. 총관에게는 작은 값이었습니다. 성을 치는 것은 대군의 일, 굶기는 것은 기병의 일이었습니다.
수 전군총관: 기병 이천을 주겠다. 요동성 동쪽을 막아라.

### SC_134 · LOC_001_YOHA (lều 전군총관) · 수 전군총관, CHAR_205 · UAV_001 · video8s · 18:04–18:12
[ACTION-VI] Cận 전군총관: ngón tay ấn lên bản đồ ở con đường phía đông, mắt vào 탁발흠. Cuối clip, 탁발흠 cúi nhặt lại cánh quạt gãy, xoay giữa hai ngón tay — nhìn nó, không nhìn tướng.
[SOUND] lửa, nhựa xoay.
N: 성을 무너뜨리는 것은 사다리가 아니라 굶주림이었습니다. 탁발흠은 믿을 필요가 없었습니다. 더 볼 필요가 있었을 뿐입니다.
수 전군총관: 동쪽에서 쌀 한 톨도 못 들어가게 하라.

### SC_135 · LOC_002_YODONGSEONG (đồng cỏ đêm, đường về thành) · CHAR_006 · VEH_001, EQP_001, VEH_206 · video8s · 18:12–18:20
[ACTION-VI] HARD CUT: đêm hành quân. POV kính đêm 백성민 từ nóc K2 đi cuối đoàn — màn xanh lục: phía sau 400 m, năm sáu bóng kỵ binh cúi thấp trên yên bám theo đoàn, không cờ, không chỏm lông; khi đoàn chậm lại, họ chậm lại. Tay anh nâng lên bấm radio.
[SOUND] xích K2 chậm, gió, rít kính đêm, PTT.
N: 요동성까지 삼십 킬로. 뒤에서 여섯 기가 따라오고 있었습니다. 삼족오 깃발은 없었습니다. 탁발흠은 사람을 잃고도 눈을 잃지 않았습니다.

### SC_136 · LOC_002_YODONGSEONG (đồng cỏ đêm) · CHAR_105, CHAR_006, kỵ Goguryeo · VEH_101, VEH_206, VEH_003, WPN_101 · video8s · 18:20–18:28
[ACTION-VI] 해모루 phi ngựa ngược hàng tới cuối đoàn, nhìn theo tay 백성민 chỉ vào bóng tối, giơ tay — mười kỵ binh Goguryeo tách hàng quay ngựa lao về sau; trong tối, bóng kỵ Tiên Ti tản ra ba hướng, một mũi tên bắn ngược cắm vào bạt K511 đi cuối. Tracking từ nóc K2.
[SOUND] vó ngựa lao đi, dây cung xa, tên cắm bạt, tiếng hú ngắn tắt trong gió.
N: 해모루는 열 기를 돌려보냈습니다. 선비 척후는 싸우지 않았습니다. 흩어졌다가, 다시 모일 것이었습니다. 그것이 그들의 방식이었습니다.

### SC_137 · LOC_002_YODONGSEONG (cổng nam 옹성) · lính Goguryeo, lính Hàn · VEH_002 · still_kenburns · 18:28–18:38
[ACTION-VI] Ảnh low-angle: K21 dừng trước khoang cổng 옹성 vòm đá bán nguyệt dưới tường đá granite xám có 치 nhô, đuốc trên tường soi xuống; lính Goguryeo giáp lamellar cúi nhìn xuống xe sắt; lính Hàn dưới đất ngước nhìn tường. Ken-burns tilt từ xe lên tường.
[SOUND] lửa đuốc, thì thầm trên tường, động cơ chờ.
N: 요동성. 돌을 쌓아 올린 성벽 둘레 이 킬로, 높이 십 미터. 요동의 모든 길이 이 성을 지났습니다. 성벽 위의 병사들은 처음으로 쇠로 된 집을 보았습니다. 그들은 두려워하지 않았습니다. 궁금해했습니다. 문은 그 집보다 좁았습니다.

### SC_138 · LOC_002_YODONGSEONG (khoang 옹성) · CHAR_003 · VEH_001 · video8s · 18:38–18:46
[ACTION-VI] 박기철 đi bộ đo bằng bước chân qua khoang cổng đá hẹp, môi đếm khẽ; tới cánh cổng bọc sắt thì dừng, giang tay chạm hai bên vách, quay lại nhìn K2 đứng ngoài — lắc đầu.
[SOUND] bước chân vang trong vòm đá.
N: 옹성의 문은 사람과 말을 위한 것이었습니다. 오십 톤짜리 쇠수레를 위한 문은 세상에 없었습니다.
박기철: 전차는 안 들어갑니다. 반 미터 모자랍니다.

### SC_139 · LOC_002_YODONGSEONG (tháp cổng) · CHAR_104 · PROP_016 · video8s · 18:46–18:54
[ACTION-VI] Trên tháp cổng gỗ: 고정수 — râu rậm muối tiêu, áo choàng len xám, chùm chìa khóa sắt ở thắt lưng, mũ cầm tay — nhìn xuống đoàn xe, đuốc hai bên. Low-angle từ dưới.
[SOUND] lửa đuốc, gió.
N: 고정수 성주. 병사보다 백성을 먼저 세는 사람이었습니다. 이 성의 백성 절반이 아직 성 밖에 있었습니다.
고정수: 쇠수레를 성 안에 들이시오.

### SC_140 · LOC_002_YODONGSEONG (trước cổng) · CHAR_001 · VEH_001 · video8s · 18:54–19:02
[ACTION-VI] 한승우 đứng trước mũi K2, ngước lên tháp cổng, 하십시오체 rõ ràng; tay chỉ vào khoang cổng hẹp rồi vào xe.
[SOUND] gió, lửa.
N: 성 안의 전차는 움직일 수 없는 전차였습니다. 움직이지 못하는 전차는 과녁이었습니다.
한승우: 성주님. 성 안에 갇힌 전차는 관입니다.

### SC_141 · LOC_002_YODONGSEONG (trước cổng) · CHAR_105 · VEH_101 · video8s · 19:02–19:10
[ACTION-VI] 해모루 trên ngựa cạnh 한승우, ngẩng lên tháp cổng, giọng kính nhưng nhanh — người liên lạc thực địa đề xuất.
[SOUND] ngựa, gió.
N: 해모루가 길을 냈습니다. 그는 이미 이 부대의 쓸모를 계산하고 있었습니다.
해모루: 성 뒤에 골짜기가 있습니다. 산길로 통합니다.

### SC_142 · LOC_002_YODONGSEONG (tháp cổng) · CHAR_104 · — · video8s · 19:10–19:18
[ACTION-VI] 고정수 im, tay nắm chùm chìa khóa; nhìn K2, nhìn 한승우, nhìn hàng dân đang đợi sau đoàn xe; quyết.
[SOUND] chìa khóa lách cách.
N: 성주는 조건을 걸었습니다. 이 땅에서 신뢰는 사람을 맡기는 것이었습니다.
고정수: 좋소. 대신 한 대장과 열 명은 성 안에서 자시오.

### SC_143 · LOC_002_YODONGSEONG (trước cổng) · CHAR_001, CHAR_002 · VEH_001 · video8s · 19:18–19:26
[ACTION-VI] 한승우 nhìn sang 오태민 (mặt bất bình, lắc đầu nhẹ), rồi ngẩng lên gật với 고정수.
[SOUND] gió.
N: 열 명은 인질이었습니다. 신뢰는 그렇게 시작되었습니다. 오태민은 그 열 명에 들지 않았습니다. 한승우가 뺐습니다.
한승우: 알겠습니다. 열 명은 제가 고릅니다.

### SC_144 · LOC_003_CHEONDUNG_BASE (đường mòn vào thung lũng, đêm) · CHAR_105, kỵ Goguryeo, kỵ Tiên Ti · VEH_003, VEH_101, VEH_206 · video8s · 19:26–19:34
[ACTION-VI] Đoàn xe rẽ theo đường mòn ven đồi sồi vào thung lũng; trên sườn đồi phía trên, ba bóng kỵ Tiên Ti lộ ra dưới trăng; kỵ Goguryeo của 해모루 hú lên xông lên dốc; hai mũi tên cắm vào thùng K511 đi cuối; bóng Tiên Ti quay ngựa biến vào rừng sồi. Wide thấp từ đường mòn.
[SOUND] hú, vó ngựa lên dốc, tên cắm gỗ, cành gãy.
N: 골짜기는 동문에서 2킬로였습니다. 산길 하나로만 통했습니다. 그날 밤부터 그곳이 천둥 기지였습니다. 그리고 그 산길을, 선비 척후 셋이 보고 갔습니다.

### SC_145 · LOC_003_CHEONDUNG_BASE (bình minh) · CHAR_003, CHAR_001 · VEH_001 · video8s · 19:34–19:42
[ACTION-VI] Sương sớm: 박기철 rút que đo dầu K2, soi, lau giẻ đỏ, ghi sổ; 한승우 đi bộ từ hướng thành về, sương trên vai. 박기철 nói không ngẩng lên.
[SOUND] chim sớm, kim loại, bút chì.
N: 삼십 킬로. 사백 킬로 중 삼십이 하룻밤에 사라졌습니다. 삼백칠십 킬로. 박기철은 그 숫자를 새 페이지에 적었습니다.
박기철: 간밤에 전차 삼십 킬로 썼습니다.

### SC_146 · LOC_003_CHEONDUNG_BASE (bình minh) · CHAR_006, CHAR_001 · — · video8s · 19:42–19:50
[ACTION-VI] 백성민 từ gò trở về, mũ boonie đẫm sương, quỳ xuống vẽ lên đất bằng đầu dao: một đường, một vòng chặn; nói kiểu điện tín.
[SOUND] dao vạch đất.
N: 동쪽 길. 성으로 들어오는 마지막 길이었습니다. 길이 끊기면 성은 섬이 되는 것이었습니다.
백성민: 동쪽 길, 오늘 밤이면 끊깁니다. 기병 천 이상.

### SC_147 · LOC_003_CHEONDUNG_BASE (bình minh) · CHAR_006 · — · video8s · 19:50–19:58
[ACTION-VI] 백성민 vẽ thêm một hàng chấm dài trên "con đường" — người và xe; ngẩng lên nhìn 한승우.
[SOUND] dao vạch đất, gió.
N: 삼천 명. 곡식 수레. 백성민의 보고에는 형용사가 없었습니다. 형용사는 셈을 흐리기 때문이었습니다.
백성민: 길 위에 피난민 삼천. 곡식 수레도 있습니다.

### SC_148 · LOC_002_YODONGSEONG (đường đông, aerial) · dân chạy nạn · — · still_kenburns · 19:58–20:08
[ACTION-VI] Ảnh aerial cao: con đường đất chạy qua đồng cỏ vàng tới cổng đông thành; trên đường, đoàn người và xe bò chở thóc kéo dài; phía bắc rất xa, một dải bụi mỏng của kỵ binh. Ken-burns kéo ra.
[SOUND] gió trên cao, xa xa tiếng bò.
N: 동쪽 마을들이 곡식을 싣고 성으로 오고 있었습니다. 삼천 명이었습니다. 성이 버틸 여름이 그 수레 위에 있었습니다. 수레는 백 대. 사람은 걸었고, 소는 끌었습니다.

### SC_149 · LOC_002_YODONGSEONG (tường đông) · CHAR_104, CHAR_001 · — · video8s · 20:08–20:16
[ACTION-VI] Trên tường đá phía đông: 고정수 và 한승우 đứng cạnh một 치, nhìn xuống đường đông; 고정수 cầm thẻ tre kiểm kho, gõ lên đá.
[SOUND] gió trên tường, thẻ tre.
N: 스무 날. 성주는 창고를 날짜로 셌습니다. 박기철이 기름을 세는 방식이었습니다.
고정수: 창고에 곡식이 스무 날 치요. 스무 날.

### SC_150 · LOC_002_YODONGSEONG (tường đông) · CHAR_104 · — · video8s · 20:16–20:24
[ACTION-VI] 고정수 chỉ tay xuống đoàn xe bò xa trên đường đông, rồi chỉ về phía tây nơi trại Tùy đang mọc lên như nấm.
[SOUND] gió.
N: 성주가 세는 것은 곳간만이 아니었습니다. 문 밖의 삼천도 그의 셈에 있었습니다.
고정수: 저 수레가 못 들어오면 삼천이 성 밖에서 죽소.

### SC_151 · LOC_002_YODONGSEONG (tường đông) · CHAR_104, CHAR_001 · — · video8s · 20:24–20:32
[ACTION-VI] 고정수 quay hẳn người nhìn thẳng 한승우 — không xin, không ra lệnh; giao việc như giao chìa khóa.
[SOUND] gió.
N: 부탁이 아니었습니다. 성주는 이 부대의 쓸모를 정한 것이었습니다. 쇠수레는 성 밖에서 쓸모가 있어야 했습니다.
고정수: 동쪽 길을 하룻밤만 지켜 주시오.

### SC_152 · LOC_002_YODONGSEONG (tường đông) · CHAR_001 · — · video8s · 20:32–20:40
[ACTION-VI] 한승우 nhìn xuống đường đông, nhìn về thung lũng nơi xe ẩn; im một nhịp dài; gật.
[SOUND] gió, tù và xa trong thành.
N: 하룻밤. 한승우가 이 땅에 내건 첫 번째 약속이었습니다. 약속은 짧았습니다. 그래서 지킬 수 있었습니다.
한승우: 하룻밤. 그 이상은 없습니다.

### SC_153 · LOC_001_YOHA (đồng cỏ phía bắc thành) · CHAR_205 · VEH_206 · still_kenburns · 20:40–20:50
[ACTION-VI] Ảnh: 탁발흠 dẫn 2.000 kỵ binh Tiên Ti băng chéo đồng cỏ về phía đông — cờ đuôi ngựa đen, mũ lông, bụi dài như dòng sông. Ken-burns trượt ngang theo hướng chạy.
[SOUND] vó ngựa ngàn con, gió.
N: 탁발흠은 이천 기와 함께 동쪽으로 돌았습니다. 본대보다 하루 빨랐습니다. 그는 길을 막는 법을 알았습니다. 이천 기는 성 하나를 굶기기에 충분한 수였습니다.

### SC_154 · LOC_002_YODONGSEONG (tường đông) · CHAR_104, CHAR_001 · — · still_kenburns · 20:50–21:00
[ACTION-VI] Ảnh: bóng hai người trên tường đông — áo choàng xám và quân phục camo — nhìn cùng một hướng xuống con đường; cỏ vàng, trời xám. Ken-burns đẩy chậm vào hai bóng.
[SOUND] gió.
N: 두 사람은 같은 수레를 보고 있었습니다. 성주는 쌀을 원했습니다. 탁발흠도 같은 것을 원했습니다.

[MID-ROLL 3 · 21:00]

[Kết thúc Phần 7]

## [Phần 8] 건전지 나흘 — 「건전지 나흘」 / Tài nguyên bắt đầu cạn  (21:00–24:00)
> Tóm tắt VI: Đêm ở LOC_003. 박기철 sạc drone từ K151: "한 번 충전, 경유 2리터"; 12 kính đêm: "건전지 나흘치". 서아: kháng sinh 90%. Bát cháo kê đầu tiên. Trong lều đỏ (xen 3 insert: ngoài lều thay pin · tay trên bản đồ vẽ tay dừng ở "살수" · 탁발흠 trên gò bắc nhìn vệt đèn đỏ), 한승우 nói rule với 오태민 + 박기철: "이 싸움은 역사가 이미 이겼다…"; 오태민: "역사책이 우리 94명을 지켜줍니까?" — rồi bước ra vỗ váy xích K2. Quyết: kính đêm dùng hết, K2 ở lại (lần 2), cối đăng ký bến suối — bắn thử 2 viên; 을보: "쇠가 우는 소리군." MINI-COMBAT cuối phần: trinh sát Tiên Ti dò thung lũng, một mũi tên cắm lưới K2, lính gác bắn 3 phát.
> Chức năng: DECISION · Tài nguyên nói thành lời: "경유 2리터", "나흘치", "아흔 퍼센트", cối 120→118 · Open loop: "그날 밤 열두 개의 야시경이 켜졌습니다. 다음 날 밤엔 여섯 개만 켤 수 있었습니다."
> Sau mid-roll 3: SC_155 aerial đêm vòng lửa trại Tùy, không thoại.

### SC_155 · LOC_002_YODONGSEONG (aerial đêm) · — · — · video8s · 21:00–21:08
[ACTION-VI] Aerial đêm rất cao: 요동성 là khối tối giữa đồng; phía tây và nam, hàng vạn đốm lửa trại Tùy xếp thành vòng cung khép dần; phía đông còn tối. Máy lướt chậm. Không thoại.
[SOUND] gió đêm, trống Tùy rất xa, tù và Goguryeo đáp lại.
N: 하루에 한 군씩, 불빛이 늘어났습니다.

### SC_156 · LOC_003_CHEONDUNG_BASE (đêm) · CHAR_003 · VEH_004, UAV_001 · video8s · 21:08–21:16
[ACTION-VI] 박기철 cắm dây sạc drone #2 vào máy phát điện nhỏ sau K151 đang kêu ro ro; ông nhìn đồng hồ dầu máy phát, ghi vào sổ dưới đèn pin đỏ.
[SOUND] máy phát ro ro, bút chì.
N: 충전은 곧 연료였습니다. 연료는 곧 거리였습니다. 드론 한 번에 전차 육백 미터가 사라졌습니다.
박기철: 드론 한 번 충전, 경유 2리터.

### SC_157 · LOC_003_CHEONDUNG_BASE (lều chỉ huy) · CHAR_003, CHAR_001 · EQP_001 · video8s · 21:16–21:24
[ACTION-VI] Bàn gấp trong lều đèn đỏ: 12 kính đêm PVS-11K xếp hai hàng, pin AA xếp cạnh thành cột; 박기철 đếm bằng bút chì; 한승우 đứng nhìn, tay chắp sau lưng.
[SOUND] pin lách cách, máy phát ngoài lều.
N: 야시경은 건전지를 먹었습니다. 건전지는 충전할 수 없는 것이었습니다. 열두 개를 켜면 나흘, 여섯 개를 켜면 여드레였습니다.
박기철: 오늘 밤 다 쓰면, 건전지는 나흘치입니다.

### SC_158 · LOC_003_CHEONDUNG_BASE (trạm y tế) · CHAR_004, lính bị thương · PROP_009 · video8s · 21:24–21:32
[ACTION-VI] 서아 thay băng cho lính bị tên xuyên cẳng tay, tiêm một mũi; đặt lọ kháng sinh rỗng sang một bên, đếm số còn lại trong túi quân y bằng ngón tay.
[SOUND] băng xé, lọ chạm.
N: 스무 개 중 열여덟 개. 화살 하나가 항생제 하나였습니다. 그 셈이 앞으로의 셈이었습니다.
윤서아: 항생제, 아흔 퍼센트 남았습니다. 두 명분 썼습니다.

### SC_159 · LOC_003_CHEONDUNG_BASE (trạm y tế) · CHAR_107, CHAR_004 · — · video8s · 21:32–21:40
[ACTION-VI] 아리 ngồi xổm bên cạnh, rút từ túi vải nhỏ ở thắt lưng một nắm lá khô, chìa cho 서아, chỉ vào vết thương của lính; 서아 cầm lá lên ngửi, nhìn cô bé.
[SOUND] lá khô, gió lùa lều.
N: 아리, 열다섯 살. 그 풀의 이름을 서아는 몰랐습니다. 이 시대의 약은 풀이었습니다.
아리: 언니, 이 풀은 피를 멎게 해요.

### SC_160 · LOC_003_CHEONDUNG_BASE (bếp) · lính Hàn · — · still_kenburns · 21:40–21:48
[ACTION-VI] Ảnh cận: bát gỗ Goguryeo đựng cháo kê vàng trong bàn tay găng đen của lính Hàn, thìa quân đội; nồi đất trên bếp đá; phía sau vài lính nhăn mặt nhưng vẫn húp. Ken-burns đẩy vào bát.
[SOUND] lửa, thìa chạm gỗ.
N: 첫 고구려 밥이었습니다. 조죽 한 그릇. 아무도 남기지 않았습니다. 이 밥부터 이 부대는 고구려에 빚을 졌습니다. 빚은 갚아야 했습니다. 어떤 방식으로든.

### SC_161 · LOC_003_CHEONDUNG_BASE (ngoài lều chỉ huy, đêm) · CHAR_001, CHAR_002, CHAR_003, lính · VEH_004, EQP_001 · video8s · 21:48–21:56
[ACTION-VI] Ngoài lều chỉ huy dưới đèn đỏ: hai lính ngồi trên thùng đạn thay pin AA cho kính đêm, máy phát K151 ro ro sau lưng; 한승우, 오태민, 박기철 đi ngang qua họ, vén cửa lều vào. Máy tĩnh, ba người khuất vào lều. Không thoại.
[SOUND] máy phát, pin lách cách, cửa lều.
N: 세 사람이 지휘 천막으로 들어갔습니다. 지금부터 할 이야기는 세 사람만의 것이었습니다. 나머지 아흔한 명에게는 무거운 것이었습니다.

### SC_162 · LOC_003_CHEONDUNG_BASE (lều chỉ huy) · CHAR_001 · — · video8s · 21:56–22:04
[ACTION-VI] Lều đèn đỏ: 한승우 kéo cửa lều khép, quay lại bàn gấp có bản đồ vẽ tay, hạ giọng; nói chậm, mắt nhìn 오태민 rồi 박기철.
[SOUND] khóa lều, máy phát rất xa.
한승우: 이 싸움은 역사가 이미 이겼다. 우리는 망치지만 않으면 된다.

### SC_163 · LOC_003_CHEONDUNG_BASE (lều chỉ huy) · CHAR_002 · — · video8s · 22:04–22:12
[ACTION-VI] 오태민 chống hai tay lên bàn, nghiêng người tới, không cao giọng nhưng từng chữ nặng.
[SOUND] bàn gấp kêu.
N: 역사는 고구려의 승리를 적었습니다. 그 책에 아흔네 명은 없었습니다. 한승우는 답이 없었습니다.
오태민: 역사책이 우리 94명을 지켜줍니까?

### SC_164 · LOC_003_CHEONDUNG_BASE (lều chỉ huy) · CHAR_001 · PROP_001 · video8s · 22:12–22:20
[ACTION-VI] Cận: bàn tay 한승우 trên bản đồ vẽ tay bằng bút chì — một con sông ngoằn ngoèo (요하), một ô vuông (요동성), mũi tên về đông-nam, và ở mép giấy một khúc sông khác chỉ có một chữ nguệch ngoạc; ngón tay ông dừng ở đó. Đèn đỏ. Không thoại.
[SOUND] im, máy phát rất xa, giấy.
N: 손으로 그린 지도였습니다. 요하, 요동성, 그리고 아직 가 보지 않은 강 하나. 살수. 그 강까지 사백 킬로였습니다. 전차 한 통이었습니다.

### SC_165 · LOC_003_CHEONDUNG_BASE (lều → K2) · CHAR_002 · VEH_001 · video8s · 22:20–22:28
[ACTION-VI] 오태민 vén cửa lều bước ra, đi thẳng tới K2 dưới lưới, vỗ hai cái lên váy xích — đúng chỗ 박기철 vẫn vỗ — rồi quay lại nhìn về cửa lều. Tracking theo anh.
[SOUND] cửa lều, giày trên đất, tay vỗ thép.
N: 두 번째 요구였습니다. 같은 쇠를 같은 손짓으로 두드리는 두 사람이 있었습니다. 아끼는 쪽과 쓰는 쪽이었습니다.
오태민: 전차를 내보내면 야시경은 필요 없습니다.

### SC_166 · LOC_003_CHEONDUNG_BASE (cửa lều chỉ huy) · CHAR_001 · VEH_001 · video8s · 22:28–22:36
[ACTION-VI] 한승우 đứng ở cửa lều, ánh đỏ sau lưng, nhìn 오태민 bên K2 không chớp; giọng thấp hơn nữa.
[SOUND] gió, máy phát.
N: 스물두 발과 사백 킬로. 한승우는 그것을 마지막을 위해 남겼습니다. 마지막이 언제인지는 그도 몰랐습니다.
한승우: 전차는 그물 밑에 둔다. 두 번 말 안 한다.

### SC_167 · LOC_003_CHEONDUNG_BASE (lều chỉ huy) · CHAR_001, CHAR_003 · EQP_001 · video8s · 22:36–22:44
[ACTION-VI] 한승우 quay vào lều, đẩy hộp kính đêm trên bàn về phía 박기철; quyết định thứ hai.
[SOUND] kính đêm trượt trên bàn.
N: 볼 수 있으면 살 수 있었습니다. 건전지 나흘치가 그 값이었습니다.
한승우: 야시경 열두 개, 전부 켠다. 오늘 밤은 봐야 한다.

### SC_168 · LOC_003_CHEONDUNG_BASE (ngoài lều) · CHAR_003, CHAR_005, lính · EQP_001 · video8s · 22:44–22:52
[ACTION-VI] Máy từ sau lưng hàng người (không cận mặt đám đông): 박기철 phát kính đêm cho từng người, ghi tên vào sổ; 태오 nhận chiếc cuối cùng, quay lại — mặt cậu rõ — gắn lên cần mũ, bật thử: mắt trái sáng xanh lục. Không thoại.
[SOUND] cần gập kim loại, bút chì, tiếng "딸깍" bật kính.
N: 야시경 열두 개. 이 부대가 밤을 보는 눈이었습니다. 박격포 백이십. 40밀리 오백사십. 드론 셋. 쓰는 것은 줄어들고, 채워지는 것은 없었습니다.

### SC_169 · LOC_003_CHEONDUNG_BASE (gò bắc, phía địch, đêm) · CHAR_205 · VEH_206 · still_kenburns · 22:52–23:02
[ACTION-VI] Ảnh: đêm, trên sườn gò phía bắc cách thung lũng ~1 km, 탁발흠 đứng cạnh ngựa giữa vài kỵ binh, nhìn xuống — dưới kia, một khe tối có vệt đỏ rất mờ lọt qua lưới (đèn lều chỉ huy). Ken-burns đẩy chậm vào vệt đỏ.
[SOUND] gió đêm, ngựa thở, xa xa tiếng máy phát mơ hồ.
N: 같은 시각, 북쪽 능선. 탁발흠은 골짜기에서 새는 붉은 빛을 보고 있었습니다. 낮에는 길을 막고, 밤에는 쇠수레를 찾았습니다. 그는 척후 셋을 내려보냈습니다.

### SC_170 · LOC_003_CHEONDUNG_BASE (hố cối trên gò) · CHAR_003, tổ cối · WPN_002 · video8s · 23:02–23:10
[ACTION-VI] Gò nhỏ phía nam: hai khẩu cối 81mm trong hố bao cát; 박기철 chỉ hướng bến suối phía đông bằng ngón tay và la bàn; xạ thủ chỉnh tay quay tầm, thả viên đạn vào nòng.
[SOUND] tay quay, đạn trượt nòng.
N: 표적을 미리 등록하면 밤에도 맞출 수 있었습니다. 대신 두 발이 들었습니다.
사수: 박격포 1번, 개울 여울 제원. 두 발 사격.

### SC_171 · LOC_003_CHEONDUNG_BASE (gò cối → bến suối xa) · tổ cối · WPN_002 · video8s · 23:10–23:18
[ACTION-VI] Cối bắn hai phát — chớp lửa trong hố, rồi từ gò nhìn ra: hai cột đất bùng lên ở bến suối tối cách xa, sáng lóa một giây. Wide.
[SOUND] cối "퉁, 퉁", 4 giây im, hai tiếng nổ dội về.
N: 여울에 표적을 등록했습니다. 박격포탄 두 발. 이제 백십팔 발이었습니다.

### SC_172 · LOC_003_CHEONDUNG_BASE (bếp đá) · CHAR_106, CHAR_107, CHAR_004 · — · video8s · 23:18–23:26
[ACTION-VI] Bên bếp đá: 을보 ngồi, chân băng duỗi, không bịt tai khi tiếng nổ dội tới; ông ngẩng lên hướng tiếng, nheo mắt trái, gật gù.
[SOUND] dư âm nổ, lửa bếp.
N: 을보는 귀를 막지 않았습니다. 대장장이는 쇠 소리를 압니다. 그는 그 소리에서 쇠의 두께를 들었습니다.
을보: 쇠가 우는 소리군.

### SC_173 · LOC_003_CHEONDUNG_BASE (bếp đá) · CHAR_107, CHAR_004 · — · video8s · 23:26–23:34
[ACTION-VI] 아리 hai tay bịt tai, hạ xuống, nhìn 서아; 서아 mỉm cười chạm vai cô bé.
[SOUND] lửa bếp, gió.
N: 아리의 질문에 서아는 답이 없었습니다. 매일 날지, 아무도 몰랐습니다. 열다섯 살에게 이 소리는 어제까지 없던 것이었습니다.
아리: 언니, 저 소리… 매일 나요?

### SC_174 · LOC_003_CHEONDUNG_BASE (mép thung, gác đêm) · 초병 · EQP_001, EQP_002, WPN_001 · video8s · 23:34–23:42
[ACTION-VI] Lính gác ở mép thung lũng đội kính đêm — POV xanh lục: trên gò bắc, ba bóng người bò sát đất nhìn xuống thung, một người giương cung. Anh bấm radio nhỏ, tay kia gạt chốt an toàn.
[SOUND] rít kính đêm, PTT, chốt an toàn, gió.
N: 나흘째 밤. 골짜기 북쪽 능선에 셋이 엎드려 있었습니다. 그들도 보고 있었습니다.

### SC_175 · LOC_003_CHEONDUNG_BASE (K2 dưới lưới) · CHAR_003, 초병 · VEH_001, WPN_001, PROP_015 · video8s · 23:42–23:50
[ACTION-VI] Một mũi tên rít xuống cắm vào lưới ngụy trang trên nóc K2, ngay trên đầu 박기철 đang ngủ dựa xích — ông bật dậy; từ mép thung, lính gác bắn ba phát K2C1 về gò bắc, chớp lửa đầu nòng; ba bóng người biến mất. Wide thấp.
[SOUND] tên rít, cắm lưới, ba phát súng đơn, tiếng "북쪽 능선!" ngoài hình.
N: 화살 하나가 전차의 그물에 박혔습니다. 총성 세 발. 능선은 비었습니다. 탁발흠의 척후는 골짜기를 찾았습니다.

### SC_176 · LOC_003_CHEONDUNG_BASE (K2 dưới lưới) · CHAR_003, CHAR_001 · VEH_001, PROP_015 · still_kenburns · 23:50–24:00
[ACTION-VI] Ảnh: đèn pin che tay soi mũi tên gãy cắm trong lưới ngụy trang trên nóc K2; bàn tay 박기철 giữ cán tên; 한승우 đứng bên, mắt về gò bắc tối. Ken-burns đẩy vào mũi tên.
[SOUND] gió, im.
N: 건전지는 열두 개씩, 나흘. 그 다음은 없었습니다. 그날 밤 열두 개의 야시경이 켜졌습니다. 다음 날 밤엔 여섯 개만 켤 수 있었습니다.

[Kết thúc Phần 8]

## [Phần 9] 동쪽 길, 하룻밤 — 「동쪽 길, 하룻밤」 / Kế hoạch lớn  (24:00–27:30)
> Tóm tắt VI: Sa bàn bằng đất do 해모루 vẽ, 한승우 thêm ký hiệu. Địa hình: đường đông qua bến suối cạn (đá, bùn hai bờ) → cửa thung → cổng đông có 2 치. Kế 7 điểm: 백성민 + 6 kính đêm trên gò báo hướng; drone #2 bay 2 lần × 12 phút; K21 천둥 2/3 ở cửa thung, KHÔNG đuổi; cối đã đăng ký bến suối; 해모루 300 kỵ + cung thủ trên 2 치; 고정수 500 bộ binh trong cổng — chỉ mở khi xe bò đến; K2 dưới lưới, tắt máy. 오태민 gật miễn cưỡng. 을보 xin theo xe bò cuối. 아리 ở lại với 서아. Drone bay lần 1: xe bò 4 km, kỵ binh tập kết sau gò bắc. 한승우 nhìn xuống đồng bằng: hàng vạn đốm lửa.
> Chức năng: PLAN · Tài nguyên: drone #2 giới hạn 24 → 12 phút · Red herring: cả kế đặt trên giả định địch đánh vào xe · Open loop: "계획은 완벽했습니다. 적이 그 계획대로 와 준다면."

### SC_177 · LOC_003_CHEONDUNG_BASE (trước lều chỉ huy, đêm) · CHAR_105, CHAR_001 · — · video8s · 24:00–24:08
[ACTION-VI] Dưới đèn pin che tay: 해모루 quỳ vẽ lên đất bằng đầu dao — một con đường, một bến suối, cửa thung, thành với hai ô vuông (치); 한승우 cắm que gỗ làm ký hiệu vào các điểm.
[SOUND] dao vạch đất, que cắm.
N: 계획은 흙 위에서 세워졌습니다. 고구려 말객과 대한민국 대위가 같은 흙을 그렸습니다. 한쪽은 흙을 알았고, 한쪽은 총을 알았습니다.

### SC_178 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_105 · — · video8s · 24:08–24:16
[ACTION-VI] 해모루 chỉ que vào bến suối phía bắc con đường đông trên sa bàn, vạch hai vệt hai bên — bùn; gõ đầu dao xuống lòng suối — đá.
[SOUND] dao gõ đất.
N: 여울. 북쪽에서 길로 내려오는 유일한 길목이었습니다. 적도 그리로 올 것이라고 모두 생각했습니다.
해모루: 여울은 북쪽에서 길로 오는 유일한 길목이오. 돌바닥이고 양쪽은 진창이오.

### SC_179 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_001, CHAR_105 · — · video8s · 24:16–24:24
[ACTION-VI] 한승우 đặt hai viên sỏi lên hai ô vuông ở cổng đông; 해모루 nhìn, gật một cái.
[SOUND] sỏi đặt xuống đất.
N: 치. 성벽에서 튀어나온 돌 망루. 고구려 성의 특징이었습니다. 문 앞을 양쪽에서 쏠 수 있었습니다.
한승우: 동문 치 두 곳. 궁수는 여기.

### SC_180 · LOC_003_CHEONDUNG_BASE (sa bàn) · — · — · still_kenburns · 24:24–24:34
[ACTION-VI] Ảnh top-down sa bàn đất: đường vạch, que, sỏi, một vỏ đạn 40mm đặt ở cửa thung làm K21, nắp lọ làm drone; đèn pin đỏ viền. Ken-burns trượt từ bến suối tới cổng.
[SOUND] gió, im.
N: 여울, 골짜기 입구, 동문. 세 곳이 계획의 전부였습니다. 적이 여울로 온다면 세 곳이면 충분했습니다. 계획은 적이 어디로 오느냐에 달려 있었습니다.

### SC_181 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_001, CHAR_006 · EQP_001 · video8s · 24:34–24:42
[ACTION-VI] 한승우 chỉ que lên gò cao phía trên bến suối, nhìn 백성민 đang đội kính đêm gập trên mũ boonie; 백성민 gật, không nói.
[SOUND] cần kính đêm gập.
N: 여섯 명과 야시경 여섯 개. 싸우지 않는 눈이 가장 오래 보는 법이었습니다.
한승우: 백 중사, 여섯 명. 고지에서 방향만 보고한다.

### SC_182 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_005 · UAV_001 · video8s · 24:42–24:50
[ACTION-VI] 태오 ôm drone #2 đã sạc, hai viên pin dán số 2 và 3 trên giáp; nói khi 한승우 chỉ vào nắp lọ trên sa bàn.
[SOUND] gió.
N: 이십사 분. 밤새 지켜야 할 길에 하늘 눈은 이십사 분뿐이었습니다. 태오는 그것을 둘로 나눴습니다.
장태오: 2호기, 두 번 비행. 열두 분씩만 씁니다.

### SC_183 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_001, CHAR_002 · — · video8s · 24:50–24:58
[ACTION-VI] 한승우 đặt vỏ đạn 40mm vào cửa thung trên sa bàn, giữ tay lên đó, nhìn 오태민.
[SOUND] đồng chạm đất.
N: 안 쫓는다. 이 계획에서 가장 어려운 명령이었습니다. 오태민은 그 자리를 견디는 법을 배운 적이 없었습니다.
한승우: 천둥 2, 3은 골짜기 입구. 안 쫓는다.

### SC_184 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_002 · — · video8s · 24:58–25:06
[ACTION-VI] Cận 오태민: hàm siết, mắt trên vỏ đạn 40mm; một nhịp dài; gật miễn cưỡng.
[SOUND] gió.
N: 그는 약속했습니다. 그 약속은 세 시간을 갔습니다.
오태민: …안 쫓습니다.

### SC_185 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_105 · PROP_018 · video8s · 25:06–25:14
[ACTION-VI] 해모루 vạch một vòng trên gò trên bến suối, chạm tay vào tù và sừng đen đeo hông.
[SOUND] dao vạch, tù và chạm giáp.
N: 나각 한 번. 삼백 기는 한 번만 쓸 수 있었습니다. 부는 때는 해모루가 정했습니다.
해모루: 삼백 기는 여울 위 언덕에 숨소. 신호는 나각이오.

### SC_186 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_105 · — · video8s · 25:14–25:22
[ACTION-VI] 해모루 chỉ que vào cổng đông, nói thay thành chủ đang ở trong thành.
[SOUND] gió.
N: 문이 열리는 순간 성은 벌판이 되었습니다. 그래서 오백을 문 안에 세웠습니다.
해모루: 성주께서 보병 오백으로 문을 지키실 것이오. 수레가 올 때만 여실 것이오.

### SC_187 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_003 · VEH_001 · video8s · 25:22–25:30
[ACTION-VI] 박기철 đứng cạnh K2 dưới lưới, vỗ hai cái lên váy xích như vỗ vai ngựa; nhìn về sa bàn.
[SOUND] tay vỗ thép.
N: 시동을 끈 전차. 기름을 아끼는 가장 확실한 방법이었습니다. 박기철에게 시동 소리는 곧 기름 냄새였습니다.
박기철: 전차는 그물 밑. 시동 끕니다.

### SC_188 · LOC_003_CHEONDUNG_BASE (K2 đêm) · CHAR_003 · VEH_001 · still_kenburns · 25:30–25:40
[ACTION-VI] Ảnh: K2 dưới lưới trong tối, trăng mỏng ánh trên nòng pháo; 박기철 ngồi dựa xích, sổ trên gối. Ken-burns đẩy chậm vào nòng.
[SOUND] gió, im.
N: 스물두 발은 그대로였습니다. 이 밤에도 전차는 울지 않을 것이었습니다. 박기철은 그 옆에서 잤습니다. 자식 옆에서 자는 아비처럼.

### SC_189 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_106, CHAR_001 · — · video8s · 25:40–25:48
[ACTION-VI] 을보 chân băng lết tới, bọc hành lý đã buộc lại sau lưng, búa nhỏ ở thắt lưng; nói với 한승우 như nói với cháu.
[SOUND] chân lết, gió.
N: 마지막 수레는 을보의 아우네 것이었습니다. 남은 피붙이가 그 수레 위에 있었습니다.
을보: 마지막 수레는 내 아우네 것이야. 내가 타고 가겠네.

### SC_190 · LOC_003_CHEONDUNG_BASE (sa bàn) · CHAR_001, CHAR_004, CHAR_006 · — · video8s · 25:48–25:56
[ACTION-VI] 한승우 nhìn 을보, nhìn sang 서아 — cô lắc đầu nhẹ (chân ông); nhưng 을보 đã quay lưng đi. 한승우 nói với 백성민 đứng gần.
[SOUND] gió.
N: 한승우는 말리지 않았습니다. 이 땅의 노인에게 명령할 권한은 그에게 없었습니다.
한승우: 백 중사, 영감님 수레 뒤에 둘 붙여.

### SC_191 · LOC_003_CHEONDUNG_BASE (bên lều) · CHAR_107, CHAR_106 · — · video8s · 25:56–26:04
[ACTION-VI] 아리 chạy tới níu tay áo 을보; ông gỡ tay cô bé, đặt bàn tay ấy vào tay 서아 vừa tới, lắc đầu, không nói.
[SOUND] vải gai, thở.
N: 아리에게 마을에서 남은 것은 할아버지 하나였습니다. 그 하나가 수레로 갔습니다. 열다섯 살의 세상은 하룻밤 사이에 노인 하나로 줄었습니다.
아리: 할아버지, 저도 가요.

### SC_192 · LOC_003_CHEONDUNG_BASE (bên lều) · CHAR_004, CHAR_107 · — · video8s · 26:04–26:12
[ACTION-VI] 서아 kéo 아리 vào, quàng tay qua vai cô bé, nhìn theo lưng 을보 khuất vào bóng tối.
[SOUND] gió, tiếng nấc nhỏ.
N: 서아에게 아리는 첫 번째 환자가 아니라 첫 번째 동생이었습니다. 동생은 환자보다 어려웠습니다.
윤서아: 아리는 나랑 여기 있어요.

### SC_193 · LOC_003_CHEONDUNG_BASE (gò trên bến suối, đêm) · CHAR_006, CHAR_105, kỵ binh Goguryeo · VEH_101, EQP_001 · still_kenburns · 26:12–26:22
[ACTION-VI] Ảnh: kỵ binh Goguryeo dắt ngựa mặc giáp lên gò trong bóng tối, chỏm lông đỏ; bên cạnh, 백성민 và tổ trinh sát đội kính đêm — ống kính lóe xanh mờ. Ken-burns trượt ngang.
[SOUND] vó ngựa êm, giáp, cần kính đêm gập.
N: 고구려 기병과 야시경이 같은 언덕에 올랐습니다. 이런 밤은 처음이었습니다. 천사백 년의 거리가 언덕 하나에 있었습니다. 누구도 그 거리를 말하지 않았습니다.

### SC_194 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_005 · UAV_001 · video8s · 26:22–26:30
[ACTION-VI] 태오 bên K21 천둥 2, drone #2 lần bay 1: màn hình nhiệt xanh-trắng — đoàn xe bò dài, người và bò là những chấm sáng, đang tới trên đường đông.
[SOUND] rotor qua loa.
N: 사 킬로. 수레의 걸음으로 한 시간이었습니다. 한 시간 뒤면 여울이었습니다. 계획대로라면.
장태오: 수레 행렬, 사 킬로. 앞은 아직 조용합니다.

### SC_195 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_005 · UAV_001 · video8s · 26:30–26:38
[ACTION-VI] Màn hình nhiệt lia sang bắc: sau gò bắc, một mảng chấm nóng dày đặc, xếp hàng — kỵ binh tập kết. 태오 nuốt nước bọt.
[SOUND] rotor, bíp.
N: 수백. 여울이 아니라 북쪽 언덕 뒤였습니다. 계획은 여울이었습니다. 태오는 그것을 보고했습니다. 아무도 계획을 바꾸지 않았습니다.
장태오: 북쪽 언덕 뒤… 기병 집결. 수백입니다.

### SC_196 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_105, CHAR_001 · UAV_001 · video8s · 26:38–26:46
[ACTION-VI] 해모루 ghé nhìn màn hình qua vai 태오 — lần đầu thấy "쇠새" nhìn đêm; ông quay sang 한승우, tò mò thật sự.
[SOUND] rotor qua loa, giáp.
N: 해모루는 두려워하지 않았습니다. 그는 물었습니다. 그것이 그와 수나라 총관의 차이였습니다. 두려움 없이 묻는 자가 가장 빨리 배웁니다.
해모루: 그 쇠새가 밤에도 보오?

### SC_197 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_001 · UAV_001 · video8s · 26:46–26:54
[ACTION-VI] 한승우 nhìn màn hình rồi nhìn 해모루, trả lời ngắn; giơ tay ra hiệu 태오 cho drone về.
[SOUND] rotor.
N: 밤에 더 잘 본다. 해모루는 그 말을 기억했습니다. 그는 배운 것을 잊지 않는 사람이었습니다.
한승우: 밤에 더 잘 봅니다.

### SC_198 · LOC_003_CHEONDUNG_BASE (gò trên bến suối, đêm) · CHAR_006 · EQP_001, VEH_206 · still_kenburns · 26:54–27:04
[ACTION-VI] Ảnh POV kính đêm 백성민 (xanh lục, nhiễu hạt): trên sườn gò cách 30 m, một bóng trinh sát Tiên Ti bò sát cỏ về phía tổ trinh sát, cung trên lưng; sáu vệt sáng mờ của tổ 백성민 nằm im hai bên. Ken-burns đẩy chậm vào bóng người bò.
[SOUND] gió, cỏ khô rất khẽ, rít kính đêm.
N: 첫 비행이 끝났습니다. 남은 것은 열두 분이었습니다. 그 열두 분을 쓰기도 전에, 언덕 위로 누군가 기어오고 있었습니다.

### SC_199 · LOC_003_CHEONDUNG_BASE (gò trên bến suối, đêm) · CHAR_006, trinh sát Tiên Ti · EQP_001 · video8s · 27:04–27:12
[ACTION-VI] 백성민 nằm im trong cỏ, kính đêm gập lên, dao lưỡi cố định rút khỏi giáp không tiếng; bóng trinh sát Tiên Ti bò ngang qua cách một sải tay — bàn tay 백성민 chụp lên miệng gã, kéo xuống cỏ; máy cắt sang mặt lính bên cạnh nhắm mắt lại. Không cận lưỡi dao, không máu.
[SOUND] cỏ đè, một tiếng thở bị chặn, rồi gió.
N: 언덕 위에서 첫 번째 피가 흘렀습니다. 소리는 나지 않았습니다. 탁발흠은 그 척후를 다시 보지 못했습니다.

### SC_200 · LOC_003_CHEONDUNG_BASE (mép thung phía tây) · CHAR_001 · — · video8s · 27:12–27:20
[ACTION-VI] 한승우 leo lên mép thung lũng phía tây, dừng lại: dưới kia, đồng bằng đêm phủ hàng vạn đốm lửa trại Tùy đến chân trời. Máy từ sau lưng, kéo rộng.
[SOUND] gió, trống Tùy xa nhiều lớp.
N: 불빛 하나가 천막 하나였습니다. 그는 세다가 그만두었습니다. 백만은 셀 수 없는 숫자였습니다. 그래서 그는 아흔네 명만 셌습니다.

### SC_201 · LOC_003_CHEONDUNG_BASE (mép thung phía tây) · CHAR_001 · — · still_kenburns · 27:20–27:30
[ACTION-VI] Ảnh: bóng 한승우 tiền cảnh, đồng bằng đêm đầy đốm lửa như sao rơi xuống đất. Ken-burns kéo ra chậm.
[SOUND] gió, trống xa.
N: 불빛 아래 백만이 잠들어 있었습니다. 그중 이천은 깨어 있었습니다. 계획은 완벽했습니다. 적이 그 계획대로 와 준다면.

[MID-ROLL 4 · 27:30]

[Kết thúc Phần 9]

## [Phần 10] 동문 야전 — 「동문 야전」 / Trận đánh quyết định  (27:30–34:30) — 6 phase
> Tóm tắt VI: Phase 1 phục kích bến suối: 400 kỵ lội bến, cối 8 viên đúng đăng ký, K3 từ gò, đội đầu vỡ; "안 쫓는다". Phase 2 địch đổi hướng: drone thấy 탁발흠 chia 3 — 1 cánh ghìm K21 bằng tên lửa, 2 cánh vòng gò bắc đánh thẳng đoàn xe bò. Phase 3 sai sót: 오태민 phá lệnh, 천둥 3 lao qua bến → kẹt bùn bờ đối diện; đuốc ném lên xe, lửa dính lưới (탁발흠 ghi nhớ). Phase 4 (narrator im): pin kính đêm 백성민 tắt; 40mm 천둥 2 còn 1 băng; 해모루 dẫn 300 kỵ xuống, dây thừng — bò dân + kỵ Goguryeo kéo K21 khỏi bùn; cung thủ trên 치 bắn trùm. Phase 5: 고정수 mở cổng, dẫn 500 giáo ra đón (trái lệnh); K3/K6 che hai sườn. Phase 6: xe bò cuối (을보) qua cổng; cổng đóng; 탁발흠 rút, nhìn lại K21 được bò kéo. Goguryeo reo; lính Hàn không.
> Chức năng: BATTLE · Tài nguyên: cối −8 (110) · 40mm −60 (480) · K3 −600 · pin kính đêm cạn · 4 thương binh mới (tổng 6) · 천둥 3 hỏng bánh chịu nặng · Enemy adaptation: nhắm xe bò; đuốc lên lưới; giữ khoảng cách · Open loop: "삼천 명이 성으로 들어갔습니다. 문은 닫혔습니다. 이제 나갈 길도 닫힌 것입니다."
> [NARRATOR IM LẶNG] 31:30–33:00. Sau mid-roll 4: SC_202 POV kính đêm xanh lục, không thoại.

### — Phase 1 · 여울 매복 / Phục kích bến suối (27:30–28:42) —

### SC_202 · LOC_003_CHEONDUNG_BASE (gò trên bến suối) · CHAR_006 · EQP_001, VEH_206 · video8s · 27:30–27:38
[ACTION-VI] POV kính đêm 백성민: màn xanh lục nhiễu hạt — bến suối đá cuội sáng nhạt, hai bờ bùn tối; từ phía bắc, hàng kỵ binh Tiên Ti lội xuống nước thành hàng dài, chấm sáng chuyển động. Không thoại, không narration.
[SOUND] gió, tiếng nước rất xa, kính đêm rít nhẹ.

### SC_203 · LOC_003_CHEONDUNG_BASE (gò) · CHAR_006 · EQP_001, EQP_002 · video8s · 27:38–27:46
[ACTION-VI] 백성민 nằm sấp trong cỏ, kính đêm trên mắt trái, tay bấm radio; giọng điện tín, không đổi nhịp.
[SOUND] PTT, gió.
N: 사백. 이천 중 사백이었습니다.
백성민: 고지. 기병 사백, 여울 진입. 북에서 남.

### SC_204 · LOC_003_CHEONDUNG_BASE (hố cối) · tổ cối · WPN_002 · video8s · 27:46–27:54
[ACTION-VI] Hố cối: xạ thủ nhìn thẻ đăng ký mục tiêu, gật với tổ bên; hai người nâng đạn sẵn.
[SOUND] đạn cối lách cách.
사수: 박격포, 여울 제원 사격. 여덟 발.

### SC_205 · LOC_003_CHEONDUNG_BASE (hố cối) · tổ cối · WPN_002 · video8s · 27:54–28:02
[ACTION-VI] Hai khẩu cối bắn liên tiếp — chớp lửa cam trong hố bao cát, bốn lần mỗi khẩu, xạ thủ thả đạn không nhìn.
[SOUND] "퉁, 퉁, 퉁" dồn dập.
N: 등록된 표적이었습니다. 조준은 필요 없었습니다.

### SC_206 · LOC_003_CHEONDUNG_BASE (bến suối, qua kính đêm) · kỵ Tiên Ti · VEH_206 · video8s · 28:02–28:10
[ACTION-VI] Góc từ gò qua kính đêm xanh: đạn cối rơi giữa hàng kỵ binh đang lội — cột nước và đá cuội bùng lên, ngựa ngã trong nước, hàng đầu vỡ tán về hai phía. Không cận thương vong.
[SOUND] tám tiếng nổ dội qua nước, ngựa hí.
N: 선두는 물속에서 멈췄습니다. 물속에서 멈춘 기병은 과녁이었습니다.

### SC_207 · LOC_003_CHEONDUNG_BASE (gò) · tổ trinh sát · WPN_003 · video8s · 28:10–28:18
[ACTION-VI] K3 từ gò bắn tracer thành dải sáng xiên xuống bến; kỵ binh trong nước quay ngựa ngược lên bờ bắc.
[SOUND] K3 quét dài, nước.

### SC_208 · LOC_003_CHEONDUNG_BASE (cửa thung, K151) · CHAR_001 · VEH_004, EQP_002 · video8s · 28:18–28:26
[ACTION-VI] 한승우 đứng cạnh K151 ở cửa thung, tổ hợp radio áp tai, mắt trên bến suối đang lóe lửa xa.
[SOUND] PTT, nổ xa.
N: 쫓지 않는 것. 계획의 첫 번째 시험이었습니다.
한승우: 천둥 2, 접촉. 안 쫓는다.

### SC_209 · LOC_003_CHEONDUNG_BASE (cửa thung) · — · VEH_002 · video8s · 28:26–28:34
[ACTION-VI] 천둥 2 từ cửa thung bắn 40mm loạt ngắn về bến — đất bùng ở mép nước phía bắc, chặn đường lên; xe không nhúc nhích khỏi vị trí.
[SOUND] 40mm ba phát, dội.

### SC_210 · LOC_003_CHEONDUNG_BASE (gò bắc, phía địch) · CHAR_205 · VEH_206 · video8s · 28:34–28:42
[ACTION-VI] 탁발흠 trên gò bắc, phía sau đội hình, nhìn xuống bến đang chớp lửa — mặt không đổi; ông giơ cánh tay lên, xòe ba ngón. Kỵ binh quanh ông tách thành ba dòng trong tối.
[SOUND] nổ xa, vó ngựa tách hướng.
N: 탁발흠은 사백을 보냈습니다. 자신은 가지 않았습니다.

### — Phase 2 · 적이 방향을 바꾸다 / Địch đổi hướng (28:42–30:02) —

### SC_211 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_005 · UAV_001 · video8s · 28:42–28:50
[ACTION-VI] 태오 bên 천둥 2, drone #2 lần bay 2: màn hình nhiệt — khối chấm nóng trên gò bắc tách làm ba. Cậu gào vào radio.
[SOUND] rotor qua loa, PTT.
N: 탁발흠은 첫 파도로 여울을 샀습니다. 그 값으로 이쪽의 눈을 여울에 묶었습니다.
장태오: 기병… 셋으로 갈라집니다!

### SC_212 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_005 · UAV_001 · video8s · 28:50–28:58
[ACTION-VI] Màn hình nhiệt: một cánh dừng xa bến, chấm lửa nhỏ bay về phía cửa thung (tên lửa); hai cánh lớn vòng qua gò bắc về phía đường đông. Ngón tay 태오 chỉ lên màn hình.
[SOUND] rotor, bíp.
N: 두 무리. 천 기 이상이 수레로 향했습니다.
장태오: 두 무리가 북쪽 언덕을 돕니다. 수레 쪽입니다!

### SC_213 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_002 · VEH_002, PROP_016 · video8s · 28:58–29:06
[ACTION-VI] Tên quấn vải cháy cắm xuống cỏ trước mũi 천둥 3, lửa nhỏ lan; 오태민 gạt kính đêm lên vì chói, nhìn về bến — không thấy kẻ bắn. Không thoại.
[SOUND] tên lửa rít, cỏ cháy lép bép.
N: 불화살은 맞히기 위한 것이 아니었습니다. 붙들어 두기 위한 것이었습니다.

### SC_214 · LOC_003_CHEONDUNG_BASE (gò bắc, đêm) · CHAR_205 · VEH_206 · video8s · 29:06–29:14
[ACTION-VI] 탁발흠 dẫn cánh chính phi vòng qua sườn gò bắc trong bóng tối, cung trên tay, không đuốc; đoàn kỵ chảy như nước qua cỏ. Tracking ngang.
[SOUND] vó ngựa dồn, không tiếng hô.
N: 그는 쇠수레를 노리지 않았습니다. 총관의 명령은 쌀이었습니다. 그는 명령을 정확히 읽었습니다.

### SC_215 · LOC_002_YODONGSEONG (đường đông, dốc lên cổng) · dân chạy nạn · — · video8s · 29:14–29:22
[ACTION-VI] Đường đông: đoàn xe bò chở thóc lên dốc về cổng đông, dân đi bộ hai bên, vài đuốc; từ bóng tối phía bắc, tiếng vó ngựa — người ngoảnh lại, bò dừng.
[SOUND] bánh xe gỗ, vó ngựa tới gần, tiếng thét đầu tiên.
N: 삼천 명이 문에서 이 킬로 떨어져 있었습니다.

### SC_216 · LOC_002_YODONGSEONG (đường đông) · kỵ Tiên Ti, dân · VEH_206 · video8s · 29:22–29:30
[ACTION-VI] Kỵ Tiên Ti xông vào đuôi đoàn xe: đao chém dây ách, một xe lật, bao thóc đổ tràn; dân chạy tán loạn lên dốc. Wide, không gore.
[SOUND] đao, bò rống, thóc đổ, thét.
N: 수레가 먼저였습니다. 사람은 나중이었습니다. 그것이 명령이었습니다.

### SC_217 · LOC_002_YODONGSEONG (đường đông, xe cuối) · CHAR_106, 2 lính Hàn · — · video8s · 29:30–29:38
[ACTION-VI] 을보 trên càng xe cuối, tay nắm búa nhỏ, quát bò đi tiếp; hai lính Hàn đi kèm quỳ bắn về phía bóng kỵ binh bằng loạt ngắn.
[SOUND] K2C1 loạt ngắn, bò, búa gõ càng.
N: 을보의 수레는 맨 뒤였습니다. 맨 뒤가 가장 먼저 닿는 자리였습니다.

### SC_218 · LOC_003_CHEONDUNG_BASE (gò) · CHAR_006 · EQP_002 · video8s · 29:38–29:46
[ACTION-VI] 백성민 xoay kính đêm về hướng đường đông, thấy lửa đuốc lộn xộn ở đuôi đoàn xe; bấm radio, giọng vẫn phẳng.
[SOUND] PTT, gió.
N: 미끼. 백성민이 그 말을 쓴 것은 처음이었습니다.
백성민: 수레 후미 피격. 기병 이백 이상. 여울은 미끼입니다.

### SC_219 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_001 · VEH_004 · video8s · 29:46–29:54
[ACTION-VI] 한승우 nghe radio, cúi nhìn sa bàn đất dưới chân — kế đã lệch; ông nhìn về đường đông, rồi bấm radio.
[SOUND] PTT, nổ xa.
N: 계획은 여울에 있었습니다. 적은 수레에 있었습니다. 한승우는 계획을 버리지 않았습니다.
한승우: 천둥 2, 3 위치 고수. 백 중사, 후미 계속 보고.

### SC_220 · LOC_003_CHEONDUNG_BASE (gò trên bến) · CHAR_105 · VEH_101, PROP_018 · video8s · 29:54–30:02
[ACTION-VI] 해모루 trên ngựa giữa 300 kỵ binh trong bóng gò, tù và nắm trong tay, nhìn về đuôi đoàn xe cháy đuốc; chưa thổi — chờ. Cận mặt ông, không râu, mắt sáng.
[SOUND] ngựa dậm, giáp, thét xa.
N: 해모루는 기다렸습니다. 삼백 기는 한 번만 쓸 수 있었습니다.

### — Phase 3 · 실수 / Sai sót (30:02–31:30) —

### SC_221 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_002 · VEH_002, EQP_001 · video8s · 30:02–30:10
[ACTION-VI] 오태민 qua kính đêm: xe bò bị chém, người ngã trên dốc; hàm ông siết, tay đập mạnh lên nắp xe.
[SOUND] tay đập thép, thét xa qua kính.
N: 오태민이 보는 것은 수레가 아니었습니다. 죽어 가는 사람이었습니다.

### SC_222 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_002 · VEH_002, EQP_002 · video8s · 30:10–30:18
[ACTION-VI] 오태민 chui vào cửa nóc 천둥 3, đập vai lái xe, lệnh nội bộ xe — ngược lại lệnh của 한승우: vượt bến để đánh vào sườn cánh kỵ đang chém đuôi đoàn xe từ phía bắc.
[SOUND] intercom, động cơ nổ.
N: 안 쫓는다는 약속은 세 시간을 갔습니다.
오태민: 조종수, 전진. 여울 건너 측면 친다.

### SC_223 · LOC_003_CHEONDUNG_BASE (cửa thung, K151) · CHAR_001 · VEH_004, EQP_002 · video8s · 30:18–30:26
[ACTION-VI] 한승우 thấy 천둥 3 bật đèn lái đêm rời cửa thung; ông gào vào tổ hợp — lần đầu tiên cao giọng trong tập.
[SOUND] PTT, xích nghiến.
N: 무전은 닿았습니다. 명령은 닿지 않았습니다.
한승우: 천둥 3, 정지! 오 중위, 정지!

### SC_224 · LOC_003_CHEONDUNG_BASE (bến suối) · — · VEH_002 · video8s · 30:26–30:34
[ACTION-VI] 천둥 3 lao xuống bến suối, nước bắn hai bên, xích nghiến đá cuội, đèn tắt; xe qua bến, mũi ngóc lên bờ đối diện. Wide thấp.
[SOUND] động cơ gầm, nước, đá.
N: 천둥 3호가 골짜기 입구를 떠났습니다. 명령은 그 반대였습니다.

### SC_225 · LOC_003_CHEONDUNG_BASE (bờ bắc bến suối) · 조종수 · VEH_002 · video8s · 30:34–30:42
[ACTION-VI] Bờ đối diện toàn bùn: xích quay không, bùn văng thành vòi, xe lún nghiêng, mũi cắm bùn, đuôi chổng lên. Cận xích quay.
[SOUND] xích quay tít, bùn, động cơ rú.
N: 돌바닥은 여울까지였습니다. 그 너머는 해모루가 말한 진창이었습니다.
조종수: 빠졌습니다! 궤도가 헛돕니다!

### SC_226 · LOC_003_CHEONDUNG_BASE (bờ bắc bến suối) · kỵ Tiên Ti · VEH_206, VEH_002, PROP_016 · video8s · 30:42–30:50
[ACTION-VI] Từ bóng tối, kỵ Tiên Ti phi ngang xe ném đuốc lên nóc — đuốc lăn trên tấm lưới ngụy trang còn buộc trên xe; lửa bén, lan theo lưới.
[SOUND] vó ngựa, đuốc rơi thép, lửa bắt.
N: 그들은 쇠를 뚫을 수 없었습니다. 그래서 불을 던졌습니다.

### SC_227 · LOC_003_CHEONDUNG_BASE (bờ bắc, cách 100 m) · CHAR_205 · VEH_206 · video8s · 30:50–30:58
[ACTION-VI] 탁발흠 ghì ngựa cách xe 100 m, nhìn lửa bám vào lưới trên nóc xe sắt — mắt ghi nhớ; cung hạ xuống, không bắn. Cận mặt, lửa phản chiếu.
[SOUND] lửa xa, ngựa thở.
N: 탁발흠은 배웠습니다. 불은 쇠에 붙지 않았지만, 그물에는 붙었습니다.

### SC_228 · LOC_003_CHEONDUNG_BASE (trong 천둥 3) · CHAR_002, lính 1소대 · VEH_002 · video8s · 30:58–31:06
[ACTION-VI] Khoang lính đèn đỏ: khói lọt vào, lính ho; 오태민 kéo cần hạ cửa đuôi — cửa mở nửa chừng rồi kẹt vào bùn; tên gõ lên giáp xe từ ngoài.
[SOUND] ho, thép rít, tên gõ.
N: 문이 막힌 쇠집 안에 아홉 명이 있었습니다.
오태민: 후방 램프 막혔다! 위로!

### SC_229 · LOC_003_CHEONDUNG_BASE (bờ bắc) · lính 1소대 · VEH_002, VEH_206 · video8s · 31:06–31:14
[ACTION-VI] Tháp 40mm 천둥 3 xoay bắn loạt ngắn quanh xe — kỵ Tiên Ti tản ra xa hơn nhưng không đi; cửa nóc mở, hai lính nhô lên bắn ra, khói lưới cháy phủ.
[SOUND] 40mm, K2C1, lửa.
N: 기관포는 적을 쫓았습니다. 진창은 쫓지 못했습니다.

### SC_230 · LOC_003_CHEONDUNG_BASE (gò) · CHAR_006 · EQP_001 · video8s · 31:14–31:22
[ACTION-VI] Kính đêm của 백성민 nhấp nháy, xanh lục tối dần — đen. Anh không chửi; tháo khối pin trong bóng tối bằng đầu ngón tay, mắt trần nhìn ra bến suối chỉ còn ánh lửa.
[SOUND] pin lách cách, thở.
N: 야시경 하나가 꺼졌습니다. 건전지였습니다.

### SC_231 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_001 · VEH_004, EQP_002 · video8s · 31:22–31:30
[ACTION-VI] 한승우 đứng thẳng cạnh K151, tổ hợp radio; nhìn lửa cháy trên xe bên kia bến; lệnh cho xe còn lại.
[SOUND] PTT, lửa xa.
N: 천둥 2호는 남았습니다. 명령은 이번엔 지켜졌습니다.
한승우: 천둥 2, 여울 앞 사격 지원. 건너지 마라.

[NARRATOR IM LẶNG — 31:30 → 33:00]

### — Phase 4 · 고구려가 끌어내다 / Goguryeo gánh — NARRATOR IM (31:30–33:00) —

### SC_232 · LOC_003_CHEONDUNG_BASE (gò) · CHAR_006 · EQP_001 · video8s · 31:30–31:38
[ACTION-VI] 백성민 lắp khối pin mới vào kính đêm bằng cảm giác ngón tay; kính sáng lại xanh lục — bến suối: 천둥 3 cháy lưới, vòng kỵ binh Tiên Ti xoay quanh ngoài tầm. Không thoại.
[SOUND] "딸깍", rít kính đêm, lửa xa.

### SC_233 · LOC_003_CHEONDUNG_BASE (cửa thung) · 사수 천둥 2 · VEH_002 · video8s · 31:38–31:46
[ACTION-VI] Trong tháp 천둥 2: xạ thủ kéo băng đạn 40mm cuối trên xe vào máng, nhìn hộp rỗng dưới chân.
[SOUND] băng đạn lách cách, động cơ.
사수: 40밀리, 즉응탄 마지막입니다!

### SC_234 · LOC_003_CHEONDUNG_BASE (gò trên bến) · CHAR_105, kỵ Goguryeo · VEH_101, PROP_018 · video8s · 31:46–31:54
[ACTION-VI] 해모루 giơ tù và sừng đen, thổi một hồi dài; 300 kỵ binh Goguryeo từ gò lao xuống bến — giáp ngựa lấp lánh dưới ánh lửa, giáo dài hạ ngang, chỏm lông đỏ. Aerial thấp theo đầu đoàn.
[SOUND] tù và trầm dài, vó ngựa như sấm, giáp.

### SC_235 · LOC_003_CHEONDUNG_BASE (bờ bắc bến) · kỵ Goguryeo, kỵ Tiên Ti · VEH_101, VEH_206 · video8s · 31:54–32:02
[ACTION-VI] Kỵ Goguryeo giáp nặng đâm vào cánh Tiên Ti quanh xe kẹt; Tiên Ti không đón — tản ra hai bên thành hình quạt, bắn tên ngược lại khi chạy. Wide trung.
[SOUND] giáo chạm giáp, ngựa hí, tên rít.

### SC_236 · LOC_003_CHEONDUNG_BASE (bờ bắc, bên 천둥 3) · CHAR_105, kỵ Goguryeo · VEH_101, VEH_002 · video8s · 32:02–32:10
[ACTION-VI] 해모루 nhảy xuống ngựa bên xe kẹt, ném cuộn dây thừng lên móc kéo trước mũi K21; hai kỵ binh móc đầu dây vào yên ngựa, ngựa gồng.
[SOUND] dây thừng, thép, ngựa thở.

### SC_237 · LOC_003_CHEONDUNG_BASE (bờ bắc) · dân đánh xe Goguryeo · VEH_002 · video8s · 32:10–32:18
[ACTION-VI] Bốn con bò được dân dắt ngược từ đoàn xe tới, ách buộc vào dây; một người đánh xe Goguryeo áo gai quát bò, vụt roi lên mông con đầu.
[SOUND] bò rống, ách gỗ, quát, roi.

### SC_238 · LOC_003_CHEONDUNG_BASE (bờ bắc) · — · VEH_002, VEH_101 · video8s · 32:18–32:26
[ACTION-VI] Cận: dây thừng căng như dây đàn, bò gồng cổ, ngựa mặc giáp gò lưng, kỵ binh kéo dây bằng tay; xích K21 quay chậm — bám — bùn nứt một vệt dài. Máy tĩnh trên dây và xích.
[SOUND] dây rít, bùn nứt, thở của người và thú.

### SC_239 · LOC_002_YODONGSEONG (치 cổng đông) · cung thủ Goguryeo · WPN_101 · video8s · 32:26–32:34
[ACTION-VI] Trên hai 치 cổng đông: cung thủ Goguryeo giương cung đồng loạt, bắn trùm — mưa tên cắm thành hàng rào giữa kỵ Tiên Ti và đoàn xe bò trên dốc. Low-angle từ đường lên.
[SOUND] dây cung hàng trăm, tên rơi như mưa đá.

### SC_240 · LOC_003_CHEONDUNG_BASE (bờ bắc) · CHAR_002, CHAR_105 · VEH_002 · video8s · 32:34–32:42
[ACTION-VI] 천둥 3 trồi lên khỏi bùn, lính giật lưới cháy khỏi nóc ném xuống nước; 오태민 nhô người trên nóc, mặt đen khói, nhìn xuống 해모루 đứng bên xe cầm dây — 해모루 nhìn lên, không nói. Máy giữ hai mặt.
[SOUND] xích bám đá, lưới cháy xèo trong nước.

### SC_241 · LOC_003_CHEONDUNG_BASE (bờ bắc) · kỵ Goguryeo, dân · VEH_002, VEH_101 · still_kenburns · 32:42–32:52
[ACTION-VI] Ảnh: xe sắt lấm bùn được bốn con bò kéo lên dốc, kỵ binh giáp lamellar đi hai bên dây, lửa lưới còn cháy phía sau, đuốc. Ken-burns đẩy chậm theo dây kéo. Không narration.
[SOUND] dây, bò, xích, lửa.

### SC_242 · LOC_003_CHEONDUNG_BASE (gò bắc) · CHAR_205 · VEH_206 · video8s · 32:52–33:00
[ACTION-VI] 탁발흠 thấy xe sắt được kéo ra — không tiếc, không nhìn lâu; ông giơ cung chỉ về đuôi đoàn xe bò trên dốc — dồn tất cả về đó. Kỵ binh quanh ông đổi hướng theo cung. Không thoại.
[SOUND] vó ngựa dồn về một hướng.

### — Phase 5 · 성주의 결정 / Quyết định của 고정수 (33:00–33:56) —

### SC_243 · LOC_002_YODONGSEONG (tường cổng đông) · CHAR_104 · — · video8s · 33:00–33:08
[ACTION-VI] 고정수 trên tường cổng đông nhìn xuống: đoàn xe còn cách cổng 200 m, đuôi đoàn bị kỵ Tiên Ti dồn ép, đuốc rơi; sau lưng ông, 500 bộ binh giáo dài đứng im trong sân cổng.
[SOUND] thét dưới dốc, giáp bộ binh.
N: 수레는 문에서 이백 미터였습니다. 이백 미터를 지켜 줄 것은 성 안에만 있었습니다.

### SC_244 · LOC_002_YODONGSEONG (bậc thang tường) · CHAR_104 · — · video8s · 33:08–33:16
[ACTION-VI] 고정수 chạy xuống bậc đá, giật chùm chìa khóa ở thắt lưng ném cho lính cổng, rút kiếm ngắn lần đầu; quát.
[SOUND] chìa khóa, kiếm rút, giày trên đá.
N: 성문을 닫는 것이 성주의 첫째 임무였습니다. 그는 그 임무를 알았습니다.
고정수: 문을 열어라! 창병 오백, 나를 따르라!

### SC_245 · LOC_002_YODONGSEONG (cổng đông) · CHAR_104, bộ binh Goguryeo · — · video8s · 33:16–33:24
[ACTION-VI] Hai cánh cổng gỗ bọc sắt mở; 고정수 áo choàng xám dẫn 500 bộ binh giáo dài xông ra thành hàng, đuốc hai bên, xuống dốc đón đoàn xe. Wide từ trên tường.
[SOUND] then cổng, giáo, tiếng hô "가자!".
N: 성주는 문을 열었습니다. 그의 백성이 문 밖에 있었기 때문입니다. 왕의 글은 아직 오지 않았습니다.

### SC_246 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_001 · VEH_004, EQP_002 · video8s · 33:24–33:32
[ACTION-VI] 한승우 thấy cổng mở qua ống nhòm; đổi hỏa lực bằng một câu radio.
[SOUND] PTT.
N: 한승우는 계획을 바꿨습니다. 이제 중심은 창이었습니다.
한승우: K3, K6 전부 동문 양옆. 창병 측면 엄호.

### SC_247 · LOC_002_YODONGSEONG (dưới cổng đông) · xạ thủ K6 · VEH_003, VEH_004, WPN_004 · video8s · 33:32–33:40
[ACTION-VI] K511 #2 (thùng chở hai phuy dầu, tam giác đỏ trên bạt) và K151 lăn tới chân dốc; hai khẩu K6 trên nóc bắn dải tracer 12.7 qua hai bên hàng giáo Goguryeo — kỵ Tiên Ti ở sườn tản ra xa.
[SOUND] K6 nặng "둥둥둥", tracer.
N: 창과 총이 같은 문 앞에 섰습니다.

### SC_248 · LOC_002_YODONGSEONG (dốc cổng đông) · bộ binh Goguryeo, kỵ Tiên Ti · VEH_206 · video8s · 33:40–33:48
[ACTION-VI] Khối giáo Goguryeo tiến xuống dốc thành hàng kín, giáo hạ ngang, đón đoàn xe vào giữa; kỵ Tiên Ti không đánh thẳng — vòng ra ngoài tầm giáo, bắn tên lẻ. Aerial thấp.
[SOUND] giáo, bước chân đều, tên lẻ.
N: 선비 기병은 창을 정면으로 받지 않았습니다. 그것이 그들의 방식이었습니다.

### SC_249 · LOC_002_YODONGSEONG (xe cuối) · CHAR_106 · — · video8s · 33:48–33:56
[ACTION-VI] 을보 trên càng xe cuối, bò lao qua khe giữa hai hàng giáo; một mũi tên cắm vào thùng xe cách ông một gang — ông không cúi, chỉ quất bò.
[SOUND] tên cắm gỗ, bánh xe, bò.
N: 을보는 몸을 낮추지 않았습니다. 예순여섯 해를 산 사람의 고집이었습니다.

### — Phase 6 · 문이 닫히다 / Kết (33:56–34:30) —

### SC_250 · LOC_002_YODONGSEONG (cổng đông) · CHAR_104, CHAR_106 · — · video8s · 33:56–34:04
[ACTION-VI] Xe bò cuối lăn qua cổng; 고정수 đi sau cùng bước vào; hai cánh cổng đóng lại sau lưng ông — và từ ngoài, ba mũi tên cắm vào gỗ cổng. Máy từ trong nhìn ra khe cổng đang khép.
[SOUND] then cổng hạ, tên cắm gỗ.
N: 곡식 백 수레. 요동성이 여름을 버틸 양이었습니다.

### SC_251 · LOC_002_YODONGSEONG (ngoài tầm cổng, tối) · CHAR_205 · VEH_206, VEH_002, VEH_003 · video8s · 34:04–34:12
[ACTION-VI] 탁발흠 dừng ngựa ngoài tầm tên, giơ tay: rút. Kỵ binh tan vào tối. Ông quay đầu nhìn lần cuối — bên bến suối, xe sắt lấm bùn đang được bò kéo lên dốc; gần chân dốc cổng, thùng xe tải mở bạt lộ hai phuy đen tròn dưới đuốc. Cận mặt ông, rồi máy theo ánh mắt dừng ở hai phuy.
[SOUND] vó ngựa rút xa, dây bò xa.
N: 탁발흠은 다시 물러났습니다. 두 번째였습니다. 그는 두 번 다 보고 있었습니다. 마지막으로 본 것은 수레 위의 검은 통이었습니다.

### SC_252 · LOC_003_CHEONDUNG_BASE (cửa thung) · CHAR_002, lính Hàn · VEH_002 · video8s · 34:12–34:20
[ACTION-VI] Cửa thung: 오태민 đứng thở bên 천둥 3 lấm bùn, kính bảo hộ vỡ một mắt, tay chống lên xe, nhìn về phía cổng đông xa — từ đó vọng tới tiếng reo của lính Goguryeo trên tường; lính Hàn quanh anh không reo, ngồi bệt xuống cỏ. Máy tĩnh.
[SOUND] reo hò rất xa; gần: thở, kim loại nguội kêu tách.
N: 고구려는 환호했습니다. 천둥 중대는 아니었습니다. 이긴 것은 그들의 총이 아니었습니다.

### SC_253 · LOC_002_YODONGSEONG (cổng đông, đêm) · — · PROP_016 · still_kenburns · 34:20–34:30
[ACTION-VI] Ảnh: cổng đông đóng kín, tên cắm dày trên gỗ bọc sắt, đuốc hai bên; phía xa, thung lũng tối. Ken-burns đẩy chậm vào then cổng.
[SOUND] gió, đuốc, im.
N: 삼천 명이 성으로 들어갔습니다. 문은 닫혔습니다. 이제 나갈 길도 닫힌 것입니다.

[Kết thúc Phần 10]

## [Phần 11] 쇠는 쇠요 — 「쇠는 쇠요」 / Chiến thắng có giá  (34:30–37:30)
> Tóm tắt VI: Bình minh xám. 천둥 3 tháo bánh chịu nặng, 박기철 dưới gầm; 을보 tới với búa và thanh sắt rèn đêm qua: đo, gõ: "쇠는 쇠요" — chốt tạm bằng sắt Goguryeo; 을보 gọi ông là "쇠쟁이". 서아 băng 6 thương binh. 박기철 báo số: 40mm 480, cối 110, pin 3 ngày, dầu "간밤에 삼십 킬로. 남은 건 삼백칠십." Aerial: vòng vây khép kín — thung lũng nằm bên trong. 한승우 rút mũi tên ở cổng đông, vào KHO LƯƠNG gặp 고정수 đang đếm bao thóc bằng thẻ tre: "그대들이 없었으면 쌀은 못 들어왔소. 그대들이 있어서 저들도 여기 온 것이오." 전령 từ 평양 tới. 한승우 một mình trên tường tây.
> Chức năng: CONSEQUENCE · Tài nguyên nói thành lời: "간밤에 삼십 킬로. 남은 건 삼백칠십", "아흔 퍼센트", 40mm/cối/pin · Open loop: "성벽 위에서 두 사람은 같은 것을 보았습니다. 끝이 없는 천막이었습니다."

### SC_254 · LOC_003_CHEONDUNG_BASE (bình minh) · — · VEH_002 · still_kenburns · 34:30–34:40
[ACTION-VI] Ảnh: bình minh xám lạnh trong thung lũng; 천둥 3 lấm bùn đến nóc, lưới cháy đen rách; một bánh chịu nặng tháo ra nằm trên cỏ, dụng cụ rải quanh. Ken-burns đẩy chậm vào bánh xe.
[SOUND] chim sớm, gió, kim loại lạnh.
N: 새벽. 천둥 3호는 바퀴 하나를 잃었습니다. 바퀴는 여섯 개 중 하나였습니다. 부품은 이 시대에 없었습니다. 있는 것은 대장간뿐이었습니다.

### SC_255 · LOC_003_CHEONDUNG_BASE · CHAR_003, CHAR_005 · VEH_002 · video8s · 34:40–34:48
[ACTION-VI] 박기철 nằm ngửa dưới gầm 천둥 3, tay bùn, kìm đa năng; 태오 quỳ đưa dụng cụ, drone #2 đặt cạnh trên cỏ. 박기철 nói từ dưới gầm.
[SOUND] kìm, thép, thở.
N: 휜 축. 철원이라면 반나절 일이었습니다. 여기서는 불가능한 일이었습니다. 부품 없는 기계는 이 시대의 돌과 같았습니다.
박기철: 지지륜 축이 휘었습니다. 부품은 없습니다.

### SC_256 · LOC_003_CHEONDUNG_BASE · CHAR_106, CHAR_003 · VEH_002, PROP_019 · video8s · 34:48–34:56
[ACTION-VI] 을보 lết tới, chân băng, tay cầm búa nhỏ và một thanh sắt rèn tay còn ám khói lò đêm qua; ông ướm thanh sắt lên trục, gõ hai cái, nheo mắt trái, gật.
[SOUND] búa gõ sắt, tiếng "쨍".
N: 을보는 밤새 쇠를 두드렸습니다. 다친 다리로, 남의 쇠를 위해서였습니다. 대장장이는 쇠에 주인을 묻지 않았습니다.
을보: 쇠는 쇠요.

### SC_257 · LOC_003_CHEONDUNG_BASE · CHAR_003, CHAR_106 · VEH_002, PROP_019 · video8s · 34:56–35:04
[ACTION-VI] 박기철 chui ra, cầm thanh sắt, ướm vào chốt xích, xoay, nhìn 을보; hai người thợ hai thời đại gật nhau — không cần thêm lời.
[SOUND] sắt chạm sắt.
N: 두 대장장이는 서로의 말을 몰라도 됐습니다. 쇠가 말을 대신했습니다.
박기철: 영감님, 이거… 되겠습니다.

### SC_258 · LOC_003_CHEONDUNG_BASE · CHAR_106 (off) · VEH_002, PROP_019 · still_kenburns · 35:04–35:14
[ACTION-VI] Ảnh cận: thanh sắt rèn tay có vết búa thô chốt tạm vào mắt xích thép công nghiệp mài nhẵn; bùn khô, dây thép quấn. Ken-burns đẩy vào chỗ nối. Giọng 을보 ngoài hình gọi 박기철 bằng cái tên từ nay sẽ dính với ông.
[SOUND] gió, im; tiếng gọi khàn ngoài hình.
N: 고구려 대장간의 쇠가 쇠수레의 발을 붙들었습니다. 천사백 년 된 방식이 오늘의 기계를 고쳤습니다. 이 부대는 이제 고구려 없이는 굴러가지 못했습니다. 그리고 박기철에게는 새 이름이 생겼습니다.
을보: 쇠쟁이.

### SC_259 · LOC_003_CHEONDUNG_BASE (trạm y tế) · CHAR_004, thương binh · PROP_009 · video8s · 35:14–35:22
[ACTION-VI] Sáu thương binh ngồi hàng trên thùng đạn; 서아 băng vết tên ở vai người cuối, đếm lọ kháng sinh trong túi bằng ngón tay, ghi sổ.
[SOUND] băng, lọ.
N: 부상 여섯. 돌아오지 않는 숫자였습니다. 화살이 스무 개면 항생제는 끝이었습니다.
윤서아: 부상 여섯. 항생제는 아직 아흔 퍼센트입니다.

### SC_260 · LOC_003_CHEONDUNG_BASE (bên K151) · CHAR_003, CHAR_001 · VEH_004 · video8s · 35:22–35:30
[ACTION-VI] 박기철 lau tay giẻ đỏ, mở sổ bìa xanh đọc cho 한승우 đang đứng tựa K151; giọng đều như đọc đơn hàng.
[SOUND] giấy, gió.
N: 사백팔십, 백십, 사흘치. 숫자는 하룻밤에 이만큼 줄었습니다. 박기철은 줄어드는 숫자만 읽었습니다. 늘어나는 숫자는 없었습니다.
박기철: 40밀리 사백팔십. 박격포 백십. 야시경 건전지 사흘치.

### SC_261 · LOC_003_CHEONDUNG_BASE (bên K151) · CHAR_003 · VEH_001 · video8s · 35:30–35:38
[ACTION-VI] 박기철 lật trang, dừng ở dòng cuối; nhìn về K2 dưới lưới rồi mới nói.
[SOUND] giấy lật.
N: 삼백칠십. 박기철은 남은 것부터 말하는 사람이 되어 가고 있었습니다. 싸우지 않아도 기름은 줄었습니다. 움직이는 것만으로도.
박기철: 간밤에 삼십 킬로. 남은 건 삼백칠십.

### SC_262 · LOC_003_CHEONDUNG_BASE · CHAR_001 · VEH_001 · video8s · 35:38–35:46
[ACTION-VI] 한승우 nhìn K2 dưới lưới — nòng pháo sạch, chưa một vệt bồ hóng, mũi tên gãy đêm qua vẫn cắm trên lưới; ông nói khẽ như ghi vào sổ của chính mình.
[SOUND] gió.
N: 스물두 발은 그대로였습니다. 하지만 삼백칠십은 사백이 아니었습니다. 스물두 발을 아끼는 값은 매일 기름으로 치르고 있었습니다.
한승우: 전차는 한 발도 안 쐈다.

### SC_263 · LOC_002_YODONGSEONG (aerial ban ngày) · — · WPN_201 · still_kenburns · 35:46–35:56
[ACTION-VI] Ảnh aerial cao: 요동성 giữa đồng; lều trại Tùy phủ kín đồng bằng phía tây, nam và nay cả phía bắc; thung lũng nhỏ phía đông với vệt lưới ngụy trang nằm gọn bên trong vòng. Ken-burns kéo ra.
[SOUND] gió trên cao, trống Tùy nhiều hướng.
N: 포위는 하룻밤 사이에 닫혔습니다. 골짜기는 그 안에 있었습니다. 들어올 수는 있어도 나갈 수는 없는 자리였습니다. 포위된 것은 성이 아니라 이 부대였습니다. 성은 늘 포위될 준비가 되어 있었습니다.

### SC_264 · LOC_002_YODONGSEONG (ngoài thành phía tây) · lính Tùy · WPN_201 · still_kenburns · 35:56–36:06
[ACTION-VI] Ảnh: quân Tùy đào hào, dựng tháp canh gỗ, khung tháp công thành bằng gỗ đang được lắp trên đồng cỏ; hàng vạn người làm việc dưới trời xám. Ken-burns trượt ngang.
[SOUND] búa, gỗ, hô lệnh xa.
N: 수나라는 이 성을 여러 달 에워쌀 것이었습니다. 요동성이 버티는 동안, 백만 대군은 여기 묶여 있었습니다. 성 안에는 스무 날 치 곡식에 백 수레가 더해졌습니다. 그것이 하룻밤의 값이었습니다.

### SC_265 · LOC_002_YODONGSEONG (cổng đông, trong thành) · CHAR_001 · PROP_015 · video8s · 36:06–36:14
[ACTION-VI] 한승우 đi qua cổng đông vào thành, ngang tấm gỗ cổng cắm dày tên; ông rút một mũi tên ra, nhìn đầu tam giác có ngạnh, cất vào túi ngực; rồi đi theo trục đường đất nện về phía kho lương. Không thoại.
[SOUND] tên rút khỏi gỗ, giày trên đất nện, tiếng dỡ hàng xa.
N: 그는 화살 하나를 가졌습니다. 이 땅이 그에게 준 첫 번째 것이었습니다. 화살은 이 땅의 말이었습니다. 그는 아직 그 말을 배우는 중이었습니다.

### SC_266 · LOC_002_YODONGSEONG (kho lương — kho gỗ nâng sàn) · CHAR_104, CHAR_001, dân · — · video8s · 36:14–36:22
[ACTION-VI] Kho lương: dân khiêng bao thóc từ xe bò vào kho gỗ nâng sàn; 고정수 đứng ở cửa kho với thẻ tre kiểm kho, đếm từng bao đi qua bằng cách gõ thẻ; 한승우 bước vào khung cửa. 고정수 không quay lại, nói mặt nghiêm, không cảm ơn.
[SOUND] bao thóc đặt xuống sàn gỗ, thẻ tre gõ, tiếng dân.
N: 성주의 첫 마디는 감사가 아니었습니다. 사실이었습니다. 성주는 빚을 말했습니다. 갚아야 할 쪽은 성이었습니다.
고정수: 그대들이 없었으면 쌀은 못 들어왔소.

### SC_267 · LOC_002_YODONGSEONG (kho lương) · CHAR_104 · — · video8s · 36:22–36:30
[ACTION-VI] 고정수 gõ thẻ tre lên bao thóc cuối, quay đầu nhìn 한승우 lần đầu; câu thứ hai nặng hơn câu đầu.
[SOUND] thẻ tre, bao thóc.
N: 두 번째 마디도 사실이었습니다. 쇠수레가 오지 않았다면 이천 기도 오지 않았을 것입니다.
고정수: 그대들이 있어서 저들도 여기 온 것이오.

### SC_268 · LOC_002_YODONGSEONG (kho lương) · CHAR_001 · PROP_015 · video8s · 36:30–36:38
[ACTION-VI] 한승우 im trong khung cửa kho; sau lưng ông dân vẫn khiêng bao; bàn tay phải chạm vào mũi tên trong túi ngực, dừng ở đó. Máy đẩy chậm vào mặt.
[SOUND] bao thóc, thẻ tre, trống Tùy xa ngoài tường.
N: 감사는 없었습니다. 계산이 있었습니다. 한승우도 계산하고 있었습니다. 그의 계산에는 아흔네 명이 있었습니다. 두 계산은 아직 같은 답을 내지 않았습니다.

### SC_269 · LOC_002_YODONGSEONG (tường tây) · CHAR_001 · PROP_011, PROP_012 · still_kenburns · 36:38–36:48
[ACTION-VI] Ảnh cận: miếng vá 태극기 trên vai áo camo của 한승우, ngay cạnh lá cờ 삼족오 đen cắm trên tường đá granite xám. Ken-burns kéo ra chậm.
[SOUND] cờ đập gió.
N: 성벽 위에 두 개의 깃발이 나란히 섰습니다. 서로 알지 못하는 깃발이었습니다. 하나는 이 땅의 옛 깃발이었고, 하나는 이 땅의 먼 훗날 깃발이었습니다.

### SC_270 · LOC_002_YODONGSEONG (kho lương) · CHAR_105, CHAR_104 · — · video8s · 36:48–36:56
[ACTION-VI] 해모루 bước vào kho, bụi đường, cúi đầu với thành chủ, giọng 합쇼체 ngắn.
[SOUND] giáp, giày trên sàn gỗ.
N: 평양. 왕이 있는 곳이었습니다. 왕의 글은 요동까지 열흘이 걸렸습니다. 그래도 명령은 왕의 것이었습니다.
해모루: 성주, 평양에서 전령이 왔습니다.

### SC_271 · LOC_002_YODONGSEONG (kho lương → tường tây) · CHAR_104 · — · video8s · 36:56–37:04
[ACTION-VI] 고정수 đặt thẻ tre xuống bao thóc, nhìn hàng bao chưa đếm xong; đi ra khỏi kho, dừng ở chân bậc thang tường tây, ngước nhìn lên nơi tiếng trống Tùy vọng qua — rồi rẽ về dinh. Không thoại.
[SOUND] chìa khóa, thẻ tre, trống xa.
N: 왕의 글이었습니다. 성주는 읽기 전에 내용을 알았습니다. 왕의 글은 언제나 하나였습니다. 지키라. 곳간 셈은 끝나지 않았습니다.

### SC_272 · LOC_001_YOHA (trại Tùy ban ngày) · CHAR_205 · VEH_206, UAV_001 · still_kenburns · 37:04–37:14
[ACTION-VI] Ảnh: 탁발흠 buộc xác drone lên sau yên ngựa bằng dây da, mấy kỵ binh tùy tùng đã lên ngựa, đường về tây qua biển lều. Ken-burns trượt theo hướng tây.
[SOUND] dây da, ngựa, trại ồn.
N: 같은 아침, 탁발흠은 서쪽으로 말을 몰았습니다. 안장에는 쇠새가 묶여 있었습니다. 그는 황제에게 직접 보고할 수 있는 몇 안 되는 사람이었습니다.

### SC_273 · LOC_003_CHEONDUNG_BASE (mép thung) · CHAR_107, CHAR_004 · — · video8s · 37:14–37:22
[ACTION-VI] 아리 và 서아 ngồi trên mép thung nhìn về thành đá và biển lều xa; 아리 hỏi không nhìn cô; 서아 không trả lời, chỉ nắm tay cô bé chặt hơn.
[SOUND] gió, cỏ.
N: 돌아갈 길은 없었습니다. 서아는 그 말을 하지 않았습니다. 거짓말도 하지 않았습니다.
아리: 언니, 돌아갈 수 있어요? 언니네 집으로요.

### SC_274 · LOC_002_YODONGSEONG (tường tây) · CHAR_001 · PROP_015 · still_kenburns · 37:22–37:30
[ACTION-VI] Ảnh: 한승우 một mình trên 치 tường tây, mũi tên Goguryeo trong tay, trước biển lều xám trải đến chân trời dưới trời bạc; xa dọc tường, ở một 치 khác cách trăm mét, bóng nhỏ áo choàng xám của 고정수 vừa lên nhìn cùng hướng trước khi về dinh. Ken-burns kéo ra tới khi cả hai thành hai chấm cách xa nhau trên tường.
[SOUND] gió, trống rất xa.
N: 성 안에는 스무 날 치 곡식과 백 수레가 있었습니다. 성 밖에는 백만이 있었습니다. 성벽 위에서 두 사람은 같은 것을 보았습니다. 끝이 없는 천막이었습니다.

[Kết thúc Phần 11]

## [Phần 12] 그 천둥을 가져오라 — 「그 천둥을 가져오라」 / Lịch sử rẽ hướng  (37:30–40:00)
> Tóm tắt VI: (a) Đại sảnh gỗ 요동성: 전령 từ 평양 quỳ, dâng chiếu 영양왕 (xuất hiện bằng chữ + giọng đọc): giữ thành, không hàng, "성과 함께 죽으라". 고정수 đọc xong nhìn 한승우: "왕명이오. 이 성과 함께… 그대들도." 한승우 không trả lời. (b) Hành doanh 양제 bên 요하 (lều vàng, chưa phải 육합성): 탁발흠 quỳ, đặt xác drone lên thảm; 선봉장 xin lỗi thay; 양제 tò mò lạnh. 탁발흠: "저들은 손에 천둥을 쥐고 있습니다." 양제: "그럼 그 천둥을 가져오라." (c) End card.
> Chức năng: POLITICS + OPEN LOOP · Tài nguyên: — (đồng hồ: thành đã bị vây) · Enemy adaptation: Tùy có vật chứng + lệnh săn · Open loop tập: quote 5.

### SC_275 · LOC_002_YODONGSEONG (đại sảnh dinh thành chủ, đêm) · 전령, CHAR_104, CHAR_001, CHAR_105 · PROP_013 · still_kenburns · 37:30–37:40
[ACTION-VI] Ảnh: đại sảnh gỗ tối, cột tròn sơn son bạc màu, đèn dầu đất nung, bản đồ da trên khung; giữa sàn, 전령 bụi đường quỳ, hai tay nâng ống tre sơn đen; 고정수 ngồi bàn thấp, 한승우 đứng bên cột, 해모루 cạnh ông. Ken-burns đẩy vào ống tre.
[SOUND] lửa đèn, hơi thở người quỳ.
N: 그날 저녁, 평양의 전령이 요동성 대청에 무릎을 꿇었습니다. 전령은 평양에서 열흘을 달려왔습니다. 글은 짧았습니다. 전령은 성주 앞에서만 글을 꺼냈습니다.

### SC_276 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_104 · PROP_013 · video8s · 37:40–37:48
[ACTION-VI] 고정수 nhận ống tre, mở nắp, rút cuộn lụa vàng nhạt trên trục gỗ đen, trải ra trên bàn thấp — cột chữ Hán, ấn son đỏ vuông ở cuối. Ông đọc, môi không động.
[SOUND] lụa, trục gỗ lăn.
N: 영양왕 고원. 고구려의 스물여섯 번째 왕이었습니다. 수나라를 두 번 맞은 왕이었습니다. 598년에 한 번, 그리고 지금.

### SC_277 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_102 (giọng) · PROP_013 · still_kenburns · 37:48–37:58
[ACTION-VI] Ảnh cận chiếu lụa dưới đèn dầu: cột chữ brush calligraphy, ấn son đỏ. Ken-burns trượt dọc cột chữ từ trên xuống. Giọng vua đọc chiếu (voice-over nhân vật, không phải narrator).
[SOUND] lửa đèn.
N: 글은 짧았습니다. 짧은 글일수록 무거웠습니다. 왕은 요동성에 사람을 보내지 않았습니다. 글만 보냈습니다.
영양왕: 요동성은 죽어도 지키라. 이것이 과인의 뜻이다.

### SC_278 · LOC_006_PYONGYANG (điện đêm — ken-burns chân dung) · CHAR_102 · — · still_kenburns · 37:58–38:08
[ACTION-VI] Ảnh: 영양왕 trong điện 평양 đêm — 백라관 lụa trắng viền vàng, long bào đỏ thẫm, ngồi trước bàn thấp có bút lông và lụa, đèn dầu; mặt tĩnh, tính toán. Ken-burns đẩy chậm vào mặt. Giọng vua tiếp.
[SOUND] lửa đèn, im.
N: 항복은 없다. 수나라 황제가 받는 것은 항복뿐이었기 때문입니다. 598년 수 문제의 삼십만은 요하에서 물러났습니다. 이번 황제는 그 아들이었습니다.
영양왕: 항복은 없다. 성과 함께 죽으라.

### SC_279 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_104, CHAR_001 · PROP_013 · video8s · 38:08–38:16
[ACTION-VI] 고정수 cuộn chiếu lại chậm, đặt lên bàn, ngẩng lên nhìn thẳng 한승우 đứng bên cột.
[SOUND] lụa cuộn.
N: 성과 함께. 성주는 그 말에 이 부대를 넣었습니다. 쇠수레는 이제 성의 것이었습니다. 적어도 성주의 셈으로는.
고정수: 왕명이오. 이 성과 함께… 그대들도.

### SC_280 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_001, CHAR_105 · — · video8s · 38:16–38:24
[ACTION-VI] 한승우 không trả lời: nhìn cuộn chiếu, nhìn 해모루 (đang quan sát ông), nhìn lại 고정수; im hoàn toàn. Máy đẩy chậm vào mặt ông.
[SOUND] lửa đèn, im.
N: 한승우는 대답하지 않았습니다. 그 대답은 아직 그의 것이 아니었습니다. 그는 아흔네 명의 것이었습니다.

### SC_281 · LOC_004_YUKHAPSEONG (hành doanh 양제 bên 요하, đêm — lều vàng, chưa phải 육합성) · 수 환관 · PROP_021 · still_kenburns · 38:24–38:34
[ACTION-VI] Ảnh: giữa biển lều Tùy đêm, một lều-điện lớn mái lụa vàng, rèm lụa vàng-đỏ, hàng đuốc, hàng trăm hoạn quan áo lụa đứng hai bên lối vào. Ken-burns đẩy vào cửa rèm.
[SOUND] trống đêm, lụa lay gió.
N: 요하 서안. 황제의 행영이었습니다. 육합성은 아직 세워지기 전이었습니다. 하지만 이미 비단과 금이 벌판 위에 있었습니다. 행영 하나가 웬만한 성보다 컸습니다.

### SC_282 · LOC_004_YUKHAPSEONG (trong lều vàng) · CHAR_205, 수 전군총관 · UAV_001 · video8s · 38:34–38:42
[ACTION-VI] Trong lều: 탁발흠 quỳ, bụi vàng còn nguyên trên áo choàng da sói, đặt xác drone lên thảm đỏ dưới bậc ngai; 전군총관 quỳ bên, cúi đầu sát sàn.
[SOUND] lụa, lửa, tiếng trán chạm thảm.
N: 총관은 사과부터 했습니다. 황제 앞에서 부하의 말은 곧 자신의 목이었습니다. 요술이라 웃던 사람이었습니다. 황제 앞에서는 웃지 않았습니다.
수 전군총관: 폐하, 황공하오나 보셔야 할 것입니다.

### SC_283 · LOC_004_YUKHAPSEONG (lều vàng) · CHAR_201 · UAV_001 · video8s · 38:42–38:50
[ACTION-VI] 양제 trên ngai sơn son thếp vàng, quạt tròn lụa trong tay, 통천관 đen; nhìn xuống vật lạ trên thảm — không kinh ngạc, chỉ tò mò lạnh; ông khẽ giơ quạt — hoạn quan bưng drone lên bậc. Low-angle từ chỗ 탁발흠 quỳ.
[SOUND] lụa, bước chân hoạn quan.
N: 수 양제 양광. 놀라는 법이 없는 사람이었습니다. 백만을 움직인 사람을 부서진 쇠새 하나가 놀라게 할 수는 없었습니다.

### SC_284 · LOC_004_YUKHAPSEONG (lều vàng) · CHAR_201 · UAV_001 · video8s · 38:50–38:58
[ACTION-VI] Cận 양제: ngón tay đeo nhẫn ngọc chạm cánh quạt gãy dưới đèn lồng, xoay nhẹ; hoạn quan bưng khay run tay.
[SOUND] nhựa gãy kêu khẽ, lửa.
N: 황제의 첫 질문은 소유였습니다. 누구의 것인가. 황제에게 세상의 물건은 둘뿐이었습니다. 짐의 것과, 아직 짐의 것이 아닌 것.
수 양제: 이것이 고구려의 것인가.

### SC_285 · LOC_004_YUKHAPSEONG (lều vàng) · CHAR_205 · — · video8s · 38:58–39:06
[ACTION-VI] 탁발흠 ngẩng đầu lần đầu — máu khô ở tai trái, sẹo, mắt thẳng — 합쇼체 ngắn, chắc.
[SOUND] lửa.
N: 탁발흠은 본 대로 말했습니다. 삼족오가 아니면 고구려도 아니었습니다. 고구려의 것이 아니면 빼앗아도 되는 것이었습니다.
탁발흠: 고구려의 것이 아닙니다. 삼족오 깃발이 아니었습니다.

### SC_286 · LOC_004_YUKHAPSEONG (lều vàng) · CHAR_205 · — · video8s · 39:06–39:14
[ACTION-VI] Cận 탁발흠: giọng không cao, không thấp — lời của người đã đứng trên đồi và đếm.
[SOUND] im.
탁발흠: 저들은 손에 천둥을 쥐고 있습니다.

### SC_287 · LOC_004_YUKHAPSEONG (lều vàng) · CHAR_201 · UAV_001 · video8s · 39:14–39:22
[ACTION-VI] 양제 cầm cánh quạt gãy lên khỏi khay, giơ trước đèn lồng xoay một vòng, rồi hạ mắt xuống 탁발흠.
[SOUND] lửa, lụa.
수 양제: 그럼 그 천둥을 가져오라.

### SC_288 · LOC_004_YUKHAPSEONG (lều vàng) · CHAR_205, CHAR_201 · UAV_001 · still_kenburns · 39:22–39:32
[ACTION-VI] Ảnh: 탁발흠 cúi đầu chạm thảm, xác drone nằm giữa ông và bậc ngai, bóng ngai đổ dài lên người ông. Ken-burns đẩy chậm vào drone. Giọng 양제 ngoài hình đặt tên.
[SOUND] trống đêm xa, lụa.
N: 그날 밤, 부대에 이름이 붙었습니다. 황제가 지은 이름이었습니다. 이름이 붙은 부대는 쫓기는 부대였습니다.
수 양제: 뇌군이라 하라.

### SC_289 · LOC_004_YUKHAPSEONG (aerial đêm) · — · VEH_205, WPN_201 · still_kenburns · 39:32–39:42
[ACTION-VI] Ảnh aerial đêm: lều vàng là một đốm sáng giữa biển lửa trại Tùy đến chân trời; sông Liêu và ba cầu phao lấp lánh đuốc; bờ đông xa, một khối tối — 요동성. Ken-burns kéo ra rất chậm.
[SOUND] trống, gió trên cao.
N: 113만이 성 하나를 에워쌌습니다. 그리고 이제, 94명을 찾고 있었습니다. 요동성 포위는 넉 달을 갈 것이었습니다. 그 넉 달의 첫날 밤이었습니다.

### SC_290 · LOC_003_CHEONDUNG_BASE (đêm) · — · VEH_001 · still_kenburns · 39:42–39:52
[ACTION-VI] Ảnh: K2 dưới lưới ngụy trang trong thung lũng đêm, trăng mỏng trên nòng pháo sạch, lính gác nhỏ bên xích. Ken-burns đẩy chậm vào nòng pháo.
[SOUND] gió, im.
N: 전차는 아직 한 번도 울지 않았습니다. 스물두 발. 삼백사십 킬로. 아흔네 명. 요동성의 여름은 이 숫자들로 시작되었습니다.

### SC_291 · [END CARD] · — · — · still_kenburns · 39:52–40:00
[ACTION-VI] Đen. Chữ trắng giữa khung: 「살수 612 · 2화 요동성」. Không hình khác.
[SOUND] tiếng trống Tùy còn vọng 3 s trong đen, rồi im tuyệt đối.

[END CARD]

[Kết thúc Phần 12]


---

## 부록 — THỐNG KÊ & TỰ KIỂM (ngoài phần kịch bản · script-writer · 2026-09-16 · cập nhật v2 narration-dense)

### A. Thống kê (script đếm tự động: SC theo header `### SC_`, narration = dòng `N:`, thoại = dòng `TÊN:`; 어절 tách theo khoảng trắng)
| Phần | Phút (outline) | SC | video8s | still_kenburns | Giây | Câu N | 어절 N | Câu thoại | 어절 thoại |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–1:30 | 12 | 9 | 3 | 90 | 6 | 68 | 4 | 14 |
| 2 | 1:30–4:30 | 22 | 17 | 5 | 180 | 21 | 325 | 12 | 69 |
| 3 | 4:30–7:00 | 18 | 12 | 6 | 150 | 18 | 290 | 11 | 57 |
| 4 | 7:00–10:30 | 25 | 22 | 3 | 206 | 24 | 369 | 7 | 25 |
| 5 | 10:30–14:00 | 26 | 23 | 3 | 214 | 15 | 186 | 14 | 65 |
| 6 | 14:00–17:30 | 26 | 22 | 4 | 210 | 24 | 383 | 18 | 86 |
| 7 | 17:30–21:00 | 25 | 20 | 5 | 210 | 25 | 382 | 17 | 102 |
| 8 | 21:00–24:00 | 22 | 19 | 3 | 180 | 21 | 303 | 12 | 77 |
| 9 | 24:00–27:30 | 25 | 20 | 5 | 210 | 25 | 360 | 17 | 105 |
| 10 | 27:30–34:30 | 52 | 50 | 2 | 420 | 37 | 301 | 15 | 90 |
| 11 | 34:30–37:30 | 21 | 14 | 7 | 180 | 21 | 359 | 12 | 56 |
| 12 | 37:30–40:00 | 17 | 9 | 8 | 150 | 14 | 228 | 9 | 41 |
| **Tổng** | 0:00–40:00 | **291** | **237** | **54** | **2400** (= 40:00) | **251** | **3554** | **148** | **787** |
| **Combat (giây / %)** | — | — | — | — | **726 s = 30.2 %** | P4 74 · P5 148 · P7 24 · P8 42 · P9 18 · P10 420 | | | |
| **TTS (tools/tts_budget.py)** | — | — | — | — | — | **4.341 어절 (N+thoại) = 108,5 어절/phút** · SC vượt ngưỡng = **0** (video8s ≤22, still ≤45) | | | |

- **v3.1 (TTS-trimmed):** narration **3.554 어절** (v3: 3.831 → cắt 277 어절 ở 39 SC vượt ngân sách đọc; 251 dòng N, 0 câu >15 어절) · thoại 148 câu / 789 어절 (v1: 147). Định nghĩa combat: SC có giao chiến / hỏa lực / truy đuổi / bị tấn công (kể cả trận sử P4 và trinh sát bị hạ) — **726 s = 30.2 %** (v1 ≈ 22 %). Khối action: P4 sử (SC_053–060, 077) · P5 (079–081, 087–101) · P7 mini (135–136, 144) · P8 mini (170–171, 174–176) · P9 mini (198–199) · P10 (202–253) = 6 khối.
- Vùng im narrator: 0:00–0:48 (narrator vào 0:48 "612년 정월. 탁군.") · 11:54–13:14 (P5 giao tranh) · 31:30–33:00 (P10 Phase 4). Sau mỗi mid-roll: 1 SC không thoại (SC_053, SC_104, SC_155, SC_202). 30 s đầu: 6 shot (SC_001 2-beat · SC_002 · SC_003 2-beat · SC_004).
- Mid-roll: 7:00 · 14:00 · 21:00 · 27:30 (đúng outline; không chen climax).

### B. Tự kiểm
1. **ID trong bible:** CHAR_001–006, 102, 104, 105, 106, 107, 201, 205 ✓ · LOC_001/002/003/004/006/008 ✓ · VEH_001–004, 101, 205, 206 ✓ · UAV_001, EQP_001/002 ✓ · WPN_001–005, 101, 201 ✓ · PROP_001/009/011/012/013/015/016/018/019/021 ✓. **Ngoại lệ:** `LOC_FLASHBACK_CHEORWON` (P2, SC_013–021) — flashback đêm 철원 chưa có trong location_bible → ghi proposals. Nhân vật phụ không ID: 소년 척후, 수 전군총관, 전령, 무전병, 초병, 사수, 조종수, 수 환관, 맥철장 (tên sử, 1 shot).
2. **Thời gian khớp outline:** 12/12 phần trong ±30 s (P4 kết 10:26 vì 2 still sử → video combat; P5 bù bằng 2 still 10 s → mid-roll 2 vẫn 14:00); tổng 40:00; không đứt quãng; mọi video8s = 8 s, still 6–10 s. Bảng ngày/đêm ở header.
3. **5 direct quotes nguyên văn:** (1) SC_085 · (2) SC_034 · (3) SC_111 · (4) SC_162 · (5a) SC_286 · (5b) SC_287 ✓ (quote năm P6 đổi theo decisions: "대왕 재위 이십삼 년이오" SC_115). 12 open loop cuối phần đúng câu outline ✓. Các câu outline khác: "나가면 들킵니다. 기름도요." SC_083 · "끝이… 안 보입니다." SC_048 · "대왕 재위 이십삼 년이오." SC_115 · "성이… 없습니다." SC_112 · "쇠수레를 성 안에 들이시오." SC_139 · "동쪽에서 쌀 한 톨도…" SC_134 · "간밤에 전차 삼십 킬로 썼습니다." SC_145 · "드론 한 번 충전, 경유 2리터." SC_156 · "나흘치" SC_157 · "역사책이 우리 94명을 지켜줍니까?" SC_163 · "쇠가 우는 소리군." SC_172 · "천둥 2, 접촉. 안 쫓는다." SC_208 · "그는 쇠수레를 노리지 않았습니다." SC_214 · "쇠는 쇠요." SC_256 · "간밤에 삼십 킬로. 남은 건 삼백칠십." SC_261 · 고정수 hai câu SC_266–267 (kho lương) · "왕명이오. 이 성과 함께… 그대들도." SC_279 ✓.
4. **0–30 s không narration:** ✓ (SC_001–004 chỉ SFX + 2 câu thoại).
5. **≤12 어절/câu thoại:** 0 vi phạm (147 câu). Narration ≤15 어절/câu: 0 vi phạm (~860 câu, v2). Không dùng "그러나 그들은 몰랐습니다".
6. **Ràng buộc nội dung:** K2 không bắn (SC_262, SC_290 nói thành lời) · drone 4→3 (SC_098, SC_175) · hội tụ 2 track 12:00–14:00 (SC_089–103) · 0 KIA, 6 thương (SC_259) · 탁발흠 sống, đặt tên "뇌군" (SC_288) · chiếu "성과 함께 죽으라" (SC_278) · kết "그럼 그 천둥을 가져오라" (SC_287) · 을지문덕 chỉ được nhắc tên (SC_109), chưa xuất hiện · không nhắc Bắc Triều Tiên, chỉ "이 땅" (SC_064, SC_174, SC_265) · không khẩu hiệu.
7. **Anti-copy:** không dùng tên/thoại/trình tự kênh tham chiếu; trình tự tập = tên cắm lốp → sử cầu phao → trinh sát nhí → bắn vì dân, giấu xe tăng → "어느 성의 군사요" → xe không lọt cổng → giữ đường đông → địch nhắm xe bò, K21 kẹt bùn, bò kéo xe → 고정수 mở cổng → chiếu vua → 양제 "가져오라".

### C. Nhật ký v3 (QC-fixed) — áp dụng logs/qc_ep1_script.md theo decisions.md
- **BLOCK** SC_006/012: VEH_206 → VEH_101 "기병 미상" (bụi đông-nam = kỵ Goguryeo thu quân); SC_040 한승우 nhìn đông-nam rồi quay tây; SC_042 N giải thích drone bay tây (vết móng từ tây).
- **FIX★ dầu** SC_261: "간밤에 삼십 킬로. 남은 건 삼백칠십." — đồng bộ SC_145 (간밤에), SC_187 (시동 끕니다), SC_262 (삼백칠십). Ledger K2 cuối 1화 = 370.
- **FIX★ năm** SC_114–117: bỏ "몇 년입니까" + 시호; 한승우 tự suy "수나라… 백만… 요동성. 육백십이 년." → 해모루 "대왕 재위 이십삼 년이오." → "육백십이년… 살수."; narrator SC_117 dùng "영양왕 23년, 서기 612년".
- **FIX timeline** SC_153 "본대보다 하루 빨랐습니다" · SC_155 N "하루에 한 군씩, 불빛이 늘어났습니다" · SC_174 "나흘째 밤" · SC_244/245 bỏ "왕명" (thành "성문을 닫는 것이 성주의 첫째 임무… 왕의 글은 아직 오지 않았습니다") · SC_077 thêm [史] Goguryeo mất 1만 rút vào thành · SC_078 "이틀 뒤 오후… 반나절" · SC_146 "오늘 밤이면 끊깁니다" · bảng ngày/đêm ở header.
- **FIX radio** SC_090 "포수, 선두 전방 오십. 점사." · SC_222 "조종수, 전진. 여울 건너 측면 친다." · SC_019 "전 소대, 여기는 천둥 지휘…".
- **FIX** SC_186 (지키실 것이오/여실 것이오) · SC_270/275 전령 · SC_252 một địa điểm (reo hò = âm xa) · SC_265 chỉ rút tên ở cổng đông · SC_178 bến = lối duy nhất từ bắc xuống đường · SC_189 "내 아우네 것" + SC_237 bỏ 을보 · SC_219 bỏ lệnh cối ("백 중사, 후미 계속 보고") · SC_161–167 xen 3 insert (161 ngoài lều thay pin · 164 tay trên bản đồ "살수" · 169 탁발흠 trên gò bắc) + SC_165 walk-and-talk vỗ váy xích K2 · SC_078/182 pin drone ("새 건전지는 아낍니다" / "열두 분씩만") + SC_051 lý do không sạc = tiếng máy phát · 0–30 s: SC_001/003 2-BEAT → 6 shot.
- **Combat** (không đổi số SC): P4 SC_053/054/059/060 → video giao chiến sử · P7 SC_135–136 (trinh sát bám đuôi, 해모루 phái 10 kỵ) + SC_144 (đường mòn) · P8 SC_169 (탁발흠 nhìn thung) → SC_174–176 (dò thung, tên cắm lưới K2, 3 phát súng) · P9 SC_198–199 (trinh sát bị 백성민 hạ bằng dao) · SC_100 tên đập giáp · SC_101 탁발흠 cho bắn loạt thử — hụt (학). Kết quả: xem dòng Combat trong bảng A.
- **Hay-hơn** SC_288: 양제 "뇌군이라 하라." (narrator không đặt tên) · SC_266–267 → kho lương (고정수 đếm bao thóc bằng thẻ tre), SC_274 = 한승우 một mình + 고정수 ở 치 khác cách trăm mét (không tableau đôi) · SC_150 "삼천이 성 밖에서 죽소" · SC_247/251 K511 #2 + "검은 통" (foreshadow hỏa công 2화) · SC_258 을보 gọi "쇠쟁이".
- **NOTE ≤1 dòng đã sửa:** 간밤에 · 나각 · 황공하오나 · 전령 · SC_066 하오체 · SC_166 "둔다" · SC_233 "즉응탄" · SC_259 bỏ vế N trùng thoại · SC_018 "적 삼십만" · SC_022 bỏ lưới (trước P1) + SC_024 "도로가… 끊겨 있습니다" · SC_044 "팔 킬로" · SC_092 "수레로 전진!" · SC_132 "쇠수레가 둘" · SC_035 lốp dự phòng · SC_168 máy sau lưng hàng người · 선봉장 → 전군총관 (P7/P12) · thì narrator quá khứ (gnomic → "-는 법이었습니다").
- **Không làm (NOTE cấu trúc lớn, theo decisions):** drone #2 hết pin giữa Phase 2 (QC §3 #8) · 탁발흠 "그물을 태워라" trong Phase 4 (#7) · 해모루 "쇠가 맞소" + 2 beat P6 (#9) · cắt đôi clip P10 (#10 — giao veo-stage) · bible lệch (world-designer/character-designer).
