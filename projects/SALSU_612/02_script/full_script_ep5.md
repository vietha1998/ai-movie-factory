# 살수 612 — 5화 「살수」 (最終話) 대본 v2.2 (TTS-trimmed · 박기철 tên đùi trái theo bible)

> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 289 (249 video8s + 40 still_kenburns) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer
> **v2.1 (TTS-trimmed, 2026-09-16):** pass "TTS budget" (`tools/tts_budget.py`: video8s ≤22 어절 N+thoại · still ≤45 (10 s → 37) · toàn tập ≤115 어절/phút) — cắt gọn NARRATION ở 51 SC (không chạm thoại/SC/thời gian/open loop/quotes/vùng im/2-BEAT): 0 SC vượt · 4.190 어절 (N 3.601 + thoại 593) = 104,8 어절/phút · narration 3.601 ≥ 3.500. Chi tiết phụ lục F.
> **v2 (QC-fixed, 2026-09-16):** áp dụng logs/qc_ep5_script.md (1 BLOCK + 16 FIX + 19 NOTE ≤1 dòng + 4 đề xuất hay-hơn đã duyệt) theo decisions.md mục "sau QC 5화 → v2". Xem nhật ký thay đổi ở phụ lục E. **ID mới dùng trong tập (chờ world-designer thêm bible + lock):** `VEH_207` = kỵ binh/ngựa chiến Tùy (tướng trên ngựa Hán, giáp 명광개 — thay VEH_205 ở 21 SC; VEH_205 = cầu phao 요하 chỉ còn ở SC_273) · `PROP_024` = 붉은 신호기 (cờ đỏ hiệu lệnh 을지문덕, lụa đỏ trơn cán tre, cuộn dây gai — không phải cờ Tùy PROP_021) · `PROP_025` = 소이수류탄 (lựu đạn nhiệt nhôm xám, nhãn mờ, vòng kéo — không phải hộp đạn PROP_008). Giáo dài 삭 ghi `VEH_101 (giáo 삭 của 개마무사)`; cung Tiên Ti ghi `VEH_206 (cung Tiên Ti)`. **SC_169 đứng trước SC_165** trong dòng thời gian (dời theo QC, giữ ID). Veo: KHÔNG đính `@VEH_205` ở LOC_007.
> **Nguồn:** outline_ep5.md (khung 12 phần — chuẩn; 6 phase P10; quyết định cuối đã chốt), series_foundation.md §7 5화 + §8b, story_bible.md (§1 [史] Salsu: nửa quân qua sông · 신세웅 chết · 450리 · 2.700 · KHÔNG dùng đập nước — mưa dầm; §3 rẽ: 우중문 bị bắt sống; §8 quyết định 2/3/9), character_bible (LOCKED), location_bible LOC_007 3 pha thời tiết + LOC_006 nội điện, vehicle_bible K2 5화, prop_bible (PROP_018 tù và 3 hồi · PROP_023 biển 천둥 3 · PROP_011 patch), resource_ledger (lệch → outline), logs/decisions.md (P-02 · P-05 · P-18 · tù và 3 hồi = hiệu lệnh), SCRIPT_BRIEF.md (checklist 1화).
> **Quy ước ghi (giống 1화 v3):** `N:` = narration tiếng Hàn (격식체, giọng nam trầm, thì quá khứ "-였습니다/-했습니다"; câu mở địa danh "612년 7월. 살수." và câu nhìn từ hiện tại "역사는 … 기록합니다" được dùng hiện tại). Trong SC có cả `N:` và thoại, thứ tự đọc do editor quyết (mặc định: N dẫn vào → đọc TRƯỚC; N bình luận → đọc SAU). `TÊN:` = thoại tiếng Hàn. `[ACTION-VI]` = hành động nhìn thấy được (tiếng Việt, cho veo-prompt-engineer). `[SOUND]` = âm thanh gợi ý. `2-BEAT` = 1 SC 8 s gồm 2 shot (chỉ ở hook và trận). `[NARRATOR IM LẶNG]` / `[MID-ROLL]` / `[END CARD]` theo outline.
> **ID:** CHAR_/LOC_/VEH_/UAV_/EQP_/WPN_/PROP_ theo bible. Nhân vật phụ không ID (ghi tên vai): 기수 (lính cầm cờ), 나각수 (người thổi tù và), 척후 선비 (trinh sát Tiên Ti), 사수 (xạ thủ cối/K3), 조종수 (lái xe K2 phối thuộc), 포수, 고구려 부장 (phó của 해모루 ở mô cát thượng lưu), 고구려 전령, 고구려 기병 장교, 고구려 궁수 장교, 수 부장, 수 전령, 수 환관, 마을 여인, 소달구지꾼 (người đánh xe bò Tùy), 병사. **수 후군 장수** = tướng hậu quân Tùy (EXTRA giáp 명광개 mũ tua đỏ, không ref riêng — decisions P-44); tên sử 신세웅 chỉ vang lên 1 lần ở SC_091 (narrator, cái chết [史]).
> **Ghi chú LOC:** toàn bộ P1–P10 + nửa đầu P11 + đầu P12 tại LOC_007_SALSU (3 pha: **bình minh xám** P1–P2 → **mưa dầm** P3–P9 → **nắng xé mây** P10 Phase 6–P11). Sub-địa hình LOC_007 dùng trong tập (khớp location_bible "Layout"): **갈대밭/bãi lau bờ bắc** (đại đội) · **여울 목/cổ họng bãi** = lối duy nhất từ bãi cạn lên bờ bắc, khe rộng ~60 m giữa bãi lau (tây) và bờ bùn dốc (đông), cách mép lau 300 m · **강 가운데 모래톱/mô cát giữa sông** (cờ 우중문 — mục tiêu 6 viên) · **작은 모래톱/mô cát nhỏ** cạnh cổ họng, cách K2 30 m (P10 Phase 3–5) · **상류 모래톱 길/mô cát thượng lưu** 1,5 km về đông = đường lội bí mật của Goguryeo, nước tới bụng ngựa (300 kỵ 해모루 + 백성민) · **북쪽 모래벌/bãi cát bắc** sau lau → đồi thấp bắc (2.000 kỵ 탁발흠) · **남쪽 언덕/gò nam** (을지문덕, cờ đỏ, 나각). LOC_004_YUKHAPSEONG (P11: 양제 nhận tin, bên 요동성). LOC_006_PYONGYANG nội điện (P12).
> **Quy ước ngôn ngữ (P-11):** trên màn hình mọi phe nói tiếng Hàn. Goguryeo ↔ đại đội hiểu nhau. Tùy ↔ đại đội KHÔNG đối thoại trực tiếp trong tập (탁발흠 ↔ 한승우 chỉ nhìn nhau). 을지문덕 ↔ 우중문 nói trực tiếp (을지문덕 thạo Hán văn — story_bible §5.2). Người đương thời KHÔNG dùng 시호 (영양왕/양제): Goguryeo "대왕/전하/과인", Tùy "폐하/짐"; narrator được dùng.
> **Radio:** callsign đại đội 5화 — "천둥 지휘" (한승우; 태오 trực máy) · "1소대" (오태민, tuyến bắc) · "수색" (백성민, mô cát thượng lưu) · 박기철 gọi "박 상사" · 해모루 giữ 1 máy từ 3화 (pin chết D−3 → P6 ông phi ngựa vào lau). Gọi "[người nghe], 여기는 [người gọi]". Pin máy chính: 4화 kết 40 % → **15 % (P1 — 4 đêm trực máy D−3→D1, SC_010 "나흘 밤을 켜 둔 값")** → 10 % (P6) → 5 % (P8) → chết (P9) → cờ tay + 나각.
> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi "간밤에/이레/마흔 날/이듬해" trong narration rà theo bảng này):**
>
> | Ngày | Buổi | SC | Sự kiện |
> |---|---|---|---|
> | **Nối 4화** | — | — | **5화 D1 = 4화 D12** (30만 qua sông nam D1 → 7 trận/ngày → rút D7 → "닷새" tới 살수). Nước: 4화 D1 무릎 → D8 허리 → 5화 D−1 배 → D1 가슴 (SC_012/044). Radio 40 % (4화 kết) → 15 % (4 đêm trực máy). 천둥 3 tới 육합성 từ 3화 D22 (= 15 ngày trước D+5). |
> | D−3 | — | (SC_025/103 N) | radio 해모루 chết; 백성민 bắt đầu đọc mô cát thượng lưu |
> | D−2 | đêm | (SC_057 N) | K2 trượt 3 km từ đảo lau thứ hai (4화) xuống bãi lau cửa bãi bắc, cách cổng họng 300 m — vết xích trong bùn (→ P4); 박기철 đo 300 m bằng chân hôm sau (SC_021) |
> | D−1 | đêm (flashback ngắn) | SC_027–028 | 해모루 giải thích "마개" bằng nút bầu |
> | **D1** (612 7월 하순, ngày quyết định) | rạng đông xám, mưa nhỏ | SC_001–011 | chân lính Tùy đầu tiên xuống bãi cạn; "여섯"; cờ đỏ cuộn |
> | D1 | rạng đông → sáng sớm | SC_012–031 | bàn cờ; 방진 [史] tới mép nước bờ nam, kỵ Goguryeo bám bốn mặt [史]; 우중문 quyết đứng giữa sông với cờ |
> | D1 | sáng sớm | SC_032–049 | kiểm kê cuối; 한승우 phát băng đạn; 을보 "가슴까지"; hậu quân Tùy đã giao tranh ở bờ nam |
> | D1 | sáng (mưa dày lên) | SC_050–075 | tiền quân 우문술 qua cổng họng, đi cách lau 200 m; 척후 thấy vết xích; trung quân 우중문 xuống nước — cờ ra mô cát; **[史] nửa quân qua sông**; cờ đỏ, tên lửa, trống |
> | D1 | giữa sáng | SC_076–101 | 나각 3 hồi; 6 viên; cối 30; PZF 6; kỵ hai bờ vào hậu quân; **[史] 신세웅 chết**; tiền quân quay lại; 탁발흠 đếm |
> | D1 | sáng muộn | SC_102–126 | lệnh "không lùi"; 우문술 "뚫어라"; 2.000 kỵ từ đồi bắc |
> | D1 | gần trưa | SC_127–152 | kỵ Tiên Ti xông lau (ngựa bịt tai 3화); K6 câm; K5 15 viên; lái xe trúng tên; 91→86 |
> | D1 | trưa | SC_153–174 | băng cuối; radio 5 %; quyết định "전차를 여울에 박는다" |
> | D1 | đầu chiều | SC_175–199 | kế 300 m; radio chết → 나각/cờ tay; 을지문덕 lệnh đánh đuôi |
> | D1 | chiều (mưa → nắng xé mây) | SC_200–251 | trận 6 phase: K2 xuống cổ họng, đốt; 탁발흠 chết trên nóc xe; **우중문 bị bắt sống** (rẽ sử); 86→80 |
> | D1 | chiều muộn, nắng | SC_252–265 | 80 người; 서아 với 해모루; 을지문덕 xuống mô cát; 경례; bát nước cho 우중문 |
> | D1→D2 | đêm → sáng | (SC_257 N) | 해모루 thở đến sáng |
> | D1→D2 [史] | một ngày một đêm | SC_252 (video + N) | tàn quân chạy 450리 tới 압록수; kỵ Goguryeo truy kích; 왕인공 chặn hậu |
> | D+5 | 육합성 bên 요동성, mưa | SC_266–272 | tin thảm bại tới 양제; xiềng 우문술; xe bò 천둥 3 **đã đứng trong trại 15 ngày** (tới 3화 D22, "스무 날" kéo từ 요동성 골짜기) — 양제 không chạm cho tới hôm nay; "내년" |
> | D+8 | 평양 nội điện, đêm mưa | SC_276–280 | hội đồng 뇌군; "내년에 또 올 것이오"; vua không quyết |
> | D+10 | 살수, nắng, nước rút | SC_281–284 | biển 천둥 3 lên xác K2; "이제 우리는 뭡니까?" |
> | cuối 7월 [史] | 요하 / đường về tây, mưa | SC_273 · SC_286–289 | Tùy rút khỏi 요동; xe bò kéo K21 về 낙양; [END CARD] |
> | 613 · 614 · 618 [史] | — | SC_274–275 N | xâm lược lần 2, 3; 우문화급 giết 양제 |

---

## [Phần 1] 여섯 — 「여섯」 / Chuyện không thể xảy ra  (0:00–1:30)
> Tóm tắt VI: Rạng đông xám, mưa nhỏ trên 살수. Bàn chân lính Tùy đầu tiên bước xuống bãi cạn — nước lên ngang ngực, khiên giơ trên đầu. 한승우 trong cửa tháp K2 trát bùn dưới lau thì thầm "여섯." Gò nam: lá cờ đỏ cuộn bên 을지문덕 — chưa mở. 0:32 narrator: "612년 7월…" — tên trận được gọi ra: 살수대첩. 91 người trong lau; 6 viên; 을지문덕 chưa ra hiệu.
> Chức năng: ACTION-HOOK · Tài nguyên nói thành lời: "여섯" · "91명" · "배터리 십오 퍼센트" · Open loop: "여섯 발. 을지문덕은 아직 신호를 보내지 않았습니다."
> Ràng buộc: 0:00–0:32 KHÔNG narrator (narrator vào 0:32 bằng năm + địa danh); 0–30 s = 6 shot (SC_001 2-BEAT · SC_002 · SC_003 2-BEAT · SC_004).

### SC_001 · LOC_007_SALSU (mép nước bờ nam, bãi cạn) · 수 보병 (không mặt) · WPN_201 · video8s · 0:00–0:08
[ACTION-VI] 2-BEAT: (a) 0:00–0:03 màn đen; chỉ tiếng mưa nhỏ rơi trên mặt sông và tiếng bước chân rất nhiều người trên đất ướt, xa; (b) 0:03–0:08 cận sát mặt nước xám rạng đông: một bàn chân đi giày cỏ, ống quần vải ướt, bước xuống nước — vòng sóng lan, một cọc gỗ đánh dấu đường lội nghiêng bên cạnh; phía sau, thêm nhiều chân bước xuống. Máy ngang mặt nước, tĩnh.
[SOUND] mưa nhỏ trên nước, bước chân hàng vạn người trên đất ướt (xa, đều), nước bị khuấy.

### SC_002 · LOC_007_SALSU (bãi cạn, nhìn từ mặt nước) · 수 보병 · WPN_201, PROP_021 · video8s · 0:08–0:16
[ACTION-VI] 2-BEAT: (a) 0:08–0:12 cận chân — hàng chân lính Tùy lội xuống nước đục, ống quần vải rách, bùn tan theo mỗi bước; (b) 0:12–0:16 low-angle từ mặt nước: hàng lính Tùy lội ra — nước lên tới ngực, một mái khiên tròn giơ trên đầu che mưa, giáo dựng đứng, cờ đỏ ướt rũ ở tiền cảnh; chỉ một khuôn mặt gần ống kính rõ (gầy, mắt trũng), còn lại là khiên và giáo kéo ngược về bờ nam không thấy điểm cuối trong mưa xám. Máy trôi chậm ngang.
[SOUND] nước ngang ngực khua nặng, thở dốc, khiên chạm nhau, mưa.

### SC_003 · LOC_007_SALSU (bãi lau bờ bắc, K2 dưới lau) · CHAR_001 · VEH_001 · video8s · 0:16–0:24
[ACTION-VI] 2-BEAT: (a) 0:16–0:20 cận mắt 한승우 trong cửa tháp K2 hé mở — tháp pháo trát bùn khô xám, lau sậy cắm dày trên nóc, mưa chảy dọc vành mũ, la bàn dây cổ dính bùn; (b) 0:20–0:24 bàn tay găng của ông đặt trên vành cửa, ngón trỏ gõ nhẹ sáu lần lên thép, môi mấp máy một chữ.
[SOUND] mưa trên thép bị bùn phủ (tiếng đục), lau cọ, thở.
한승우: (thì thầm) 여섯.

### SC_004 · LOC_007_SALSU (gò nam) · CHAR_101, 기수 · PROP_024 (붉은 신호기 — cờ đỏ hiệu lệnh 을지문덕), WPN_101 · video8s · 0:24–0:32
[ACTION-VI] 2-BEAT: (a) 0:24–0:28 cận lá cờ đỏ lớn cuộn chặt quanh cán tre trong tay lính cầm cờ, dây gai buộc chưa cởi, mưa chảy dọc lụa; (b) 0:28–0:32 gò nam trong mưa xám: 을지문덕 đứng bất động — giáp ướt, chỏm lông đen + hai lông trắng rủ nước, kiếm 환두대도 rút cầm thấp; dưới gò, dòng người Tùy lội ra sông nhỏ như kiến. Máy đẩy chậm vào mặt ông.
[SOUND] mưa, gió trên gò, tiếng dòng quân xa như sóng.

### SC_005 · LOC_007_SALSU (aerial, bờ nam) · — · WPN_201, PROP_021 · still_kenburns · 0:32–0:40
[ACTION-VI] Ảnh aerial rất cao, xám: khối 방진 khổng lồ hình vuông méo bò tới mép nước bờ nam — đầu khối đã xuống sông, thân khối trải ngược lên đồng cỏ xanh ướt, đuôi mất trong mưa; cờ đỏ ướt như vệt máu loang. Ken-burns kéo ra chậm.
[SOUND] một hồi trống Tùy nặng, xa; mưa.
N: 612년 7월. 살수. 수나라 별동대 30만 5천이 살수로 돌아왔습니다. 평양 삼십 리 앞에서 돌아선 군대였습니다. 굶은 채 닷새를 걸어온 군대였습니다.

### SC_006 · LOC_007_SALSU (bãi cạn) · 수 보병, 수 기병 · WPN_201, VEH_207 · video8s · 0:40–0:48
[ACTION-VI] Wide thấp từ mô cát: hàng nghìn lính Tùy dàn ngang lội qua bãi cạn, ngựa bơi cổ ngẩng, xe ngựa gỗ lắc trên bè lau; nước xám bạc gợn mưa; hai bờ đồi thấp im lìm. Máy tĩnh.
[SOUND] hàng nghìn bước chân trong nước, ngựa thở, bè gỗ kẽo kẹt.
N: 역사는 이날을 살수대첩이라 기록합니다. 기록은 짧습니다. 절반이 건넜을 때 쳤다. 그 한 줄이 전부입니다.

### SC_007 · LOC_007_SALSU (bãi lau bờ bắc, hố chiến đấu) · 천둥 중대 (không mặt), CHAR_005 · WPN_001, EQP_002 · video8s · 0:48–0:56
[ACTION-VI] Tracking thấp dọc bãi lau: một hàng lính Hàn nằm trong hố cát có bao cát, súng K2C1 gác trên lau gập, mũ bọc lau, mặt bôi bùn — 태극기 rách trên vai vẫn thấy màu; cuối hàng, 태오 đội mũ trụ sắt Goguryeo, chân nẹp tre, tổ hợp radio trên tấm poncho. Không ai động.
[SOUND] mưa trên lau, thở nén, radio rè rất nhỏ.
N: 그러나 그날 아침, 갈대밭에는 역사에 없는 91명이 있었습니다. 넉 달 전에는 94명이었습니다. 그들은 이 강의 이름을 학교에서 배웠습니다. 그 강물이 발밑에 있었습니다.

### SC_008 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001, EQP_002 · video8s · 0:56–1:04
[ACTION-VI] 박기철 ngồi ép sát váy xích K2 dưới lau, mũ lưỡi trai ướt, tai nghe radio, sổ tay bọc túi nilon; qua cửa nạp đạn hé mở, màn hình bộ đếm đạn trong tháp hắt sáng xanh: "잔탄 06". Ông không nhìn sổ — nhìn màn hình.
[SOUND] mưa, quạt điện tử trong xe rất nhỏ, PTT.
N: 포탄 여섯 발. 넉 달 동안 열여섯 발을 썼습니다. 언제 쓸지는 아직이었습니다.
박기철: (thì thầm, radio) 천둥 지휘, 여기는 박 상사. 잔탄 여섯. 이상 없음.

### SC_009 · LOC_007_SALSU (tuyến bắc bãi lau) · CHAR_002 · WPN_003 · video8s · 1:04–1:12
[ACTION-VI] 오태민 trong hố cát ở rìa bắc bãi lau, khẩu K3 (băng dính vải ghi tên người chết trên báng — không rõ chữ) đặt trên bao cát; kính bảo hộ còn gác trên mũ, băng bắp tay trái (tên sượt đêm cứu 태오, 4화); ống nhòm nhỏ nhìn qua khe lau: cách 200 m, đầu cột quân Tùy đang bò lên khỏi cổng họng bãi, khiên dựng. Ông hạ ống nhòm, bấm radio, giọng thì thầm.
[SOUND] mưa, PTT, tiếng đoàn quân xa.
N: 오태민은 북쪽 선을 맡았습니다. 어깨에는 석문령에서 죽은 사수의 기관총이 있었습니다. 삼십만을 보내는 것은 두 번째였습니다.
오태민: (thì thầm, radio) 천둥 지휘, 여기는 1소대. 선두가 물에서 나옵니다.

### SC_010 · LOC_007_SALSU (bãi lau, radio) · CHAR_005 · EQP_002 · video8s · 1:12–1:20
[ACTION-VI] Cận 태오 dưới vành mũ trụ sắt Goguryeo quá rộng, mắt trái còn vết bầm mờ; ngón tay lau nước mưa khỏi màn hình nhỏ của tổ hợp radio: vạch pin còn một vạch ngắn; cậu nói vào mic mà không nhìn.
[SOUND] mưa trên sắt mũ trụ (tiếng khác mũ nhựa), PTT.
N: 하늘의 눈은 없었습니다. 드론은 없었습니다. 남은 것은 무전기 한 대와 두 눈이었습니다. 나흘 밤을 켜 둔 값이었습니다.
장태오: (thì thầm) 무전기, 십오 퍼센트. 날마다 말라갑니다.

### SC_011 · LOC_007_SALSU (aerial, bãi cạn) · — · WPN_201, PROP_021 · still_kenburns · 1:20–1:30
[ACTION-VI] Ảnh aerial xám: dòng quân Tùy kéo dài từ bờ nam ra giữa sông như một sợi dây tối; đầu dây chạm bờ bắc; mô cát giữa sông còn trống; hai bên bờ, đồi thấp xanh và bãi lau im — không một chuyển động lạ. Ken-burns đẩy rất chậm vào mô cát giữa sông.
[SOUND] mưa, dòng quân như sóng xa, một tiếng nhạc trầm kéo dài.
N: 반. 을지문덕이 말한 것은 그 한 글자였습니다. 그 반이 어느 쪽 반인지, 갈대밭은 아직 몰랐습니다. 여섯 발. 을지문덕은 아직 신호를 보내지 않았습니다.

[Kết thúc Phần 1]

## [Phần 2] 마개 — 「마개」 / Họ đang ở đâu  (1:30–4:30)
> Tóm tắt VI: Bàn cờ (KB bản đồ lụa vẽ tay + aerial thật): bãi cạn rộng 400 m, mô cát giữa sông, cổng họng bãi bờ bắc rộng 60 m, hai bờ đồi thấp — kỵ Goguryeo giấu trong đồi hai bờ; 을지문덕 gò nam; 방진 khổng lồ [史]: 우문술 tiền quân, 우중문 trung quân với cờ (quyết đứng giữa sông), 신세웅 hậu quân — đã bị kỵ Goguryeo bám bốn mặt suốt đường rút [史]. Kế của 을지문덕: đánh khi "nửa" — nửa dưới nước. Đại đội: cửa ra bãi bắc = nút chai; 오태민 tuyến bắc; 백성민 với 300 kỵ 해모루 ở mô cát thượng lưu; 서아 trạm cứu thương; 태오 mũ trụ sắt trực radio; 을보, 아리 với phụ nữ làng. Flashback đêm trước: 해모루 giải thích "마개" bằng nút bầu rượu. 한승우 hiểu nửa nào.
> Chức năng: DISCOVERY · Tài nguyên: — (radio 해모루 không trả lời) · Mini-combat [史] SC_017–018 (kỵ Goguryeo bám 방진) · Open loop: "을지문덕의 계획에서 그들이 맡은 것은 단 하나였습니다. 마개."

### SC_012 · LOC_007_SALSU (KB bản đồ lụa Goguryeo) · — · PROP_001 (bản đồ lụa 을지문덕) · still_kenburns · 1:30–1:42
[ACTION-VI] Ảnh: bản đồ lụa vẽ mực (brush, không chữ đọc được): một dải sông uốn cong, vạch cọc đánh dấu đường lội, dải mô cát giữa sông, bãi lau bờ bắc tô nét dày, đồi hai bên bờ vẽ hình vảy; góc bản đồ, một chấm son đỏ ở khe bờ bắc. Ken-burns trượt từ bờ nam qua sông lên chấm đỏ.
[SOUND] mưa xa, giấy lụa, nhạc trầm.
N: 살수. 오늘의 청천강입니다. 폭 팔백 미터. 열이틀 전 삼십만이 남으로 건널 때는 무릎이었습니다. 나흘 전에는 허리였습니다. 그 사이 상류에 비가 내렸습니다. 을보 영감이 말한 대로였습니다. 화나면 사흘에 어른 키를 넘는 강이었습니다.

### SC_013 · LOC_007_SALSU (aerial, toàn bãi cạn) · — · WPN_201 · video8s · 1:42–1:50
[ACTION-VI] Aerial thật, rạng đông xám: bãi cạn 400 m với hàng cọc gỗ, mô cát giữa sông dài như lưỡi, bờ bắc chìm trong bãi lau xanh xám rộng hàng trăm mét; ở mép bắc, một khe hở giữa bãi lau và bờ bùn dốc — cổng họng; bờ nam đồi thấp xanh; đầu 방진 đã tràn xuống nước. Máy trôi chậm từ nam lên bắc.
[SOUND] gió trên cao, mưa, dòng quân xa.
N: 건널 수 있는 길은 하나였습니다. 사백 미터의 여울, 그리고 북쪽 기슭의 좁은 목. 목은 육십 걸음 폭이었습니다. 삼십만이 육십 걸음으로 나와야 했습니다.

### SC_014 · LOC_007_SALSU (KB bản đồ, ba khối quân) · — · PROP_021 · still_kenburns · 1:50–2:02
[ACTION-VI] Ảnh: bản đồ lụa với ba khối vuông vẽ mực đỏ nối đuôi: khối đầu đã chạm sông, khối giữa có một lá cờ nhỏ vẽ trên, khối cuối trên đồng bờ nam; quanh khối cuối, các mũi tên mực đen vẽ vòng (kỵ Goguryeo). Ken-burns từ khối đầu lùi về khối cuối.
[SOUND] mưa, nhạc trầm.
N: 방진. 네모진 행군이었습니다. 앞은 우문술, 가운데는 우중문, 뒤는 후군이었습니다. 평양에서 여기까지 닷새였습니다. 닷새 내내 고구려 기병이 네 면을 물어뜯었습니다. 역사는 그것도 기록했습니다. 사면에서 치되, 결전은 하지 않았다.

### SC_015 · LOC_007_SALSU (mép nước bờ nam, tiền quân) · CHAR_203 · VEH_207, WPN_201 · video8s · 2:02–2:10
[ACTION-VI] 우문술 trên ngựa xám ướt ở mép nước bờ nam — giáp sẫm không trang trí, cổ lông ướt bết, mặt xám mệt; ông nhìn hàng cọc gỗ nghiêng trong nước, rồi nhìn lính đang lưỡng lự, giơ tay chỉ ra sông. Máy trung, hơi thấp.
[SOUND] mưa, ngựa giậm nước, tiếng quan hô xa.
N: 우문술은 물을 먼저 보았습니다. 어제보다 높았습니다. 그는 알았지만 멈출 수 없었습니다. 뒤에서 고구려가 오고 있었습니다.
우문술: 선봉부터 건너라. 수레는 버려라.

### SC_016 · LOC_007_SALSU (bờ nam, trung quân) · CHAR_202, 기수 · VEH_207, PROP_021 · video8s · 2:10–2:18
[ACTION-VI] 우중문 trên ngựa đen giữa trung quân — hai gương ngực 명광개 mờ nước, râu trắng dài ướt, áo choàng đỏ nặng mưa; bên ông, lính cầm cờ đại quân đỏ viền vàng; ông nhìn ra mô cát giữa sông, đặt tay lên cán cờ. Máy đẩy chậm.
[SOUND] mưa trên gương ngực, cờ ướt đập cán.
N: 우중문은 강 가운데를 보았습니다. 깃발이 뒤에 서는 것을 그는 허락하지 않았습니다. 삼십만이 깃발을 보고 건너야 했습니다.
우중문: 깃발은 내 곁에 둔다. 강 가운데서도.

### SC_017 · LOC_007_SALSU (đồng bờ nam, sườn 방진) · 고구려 기병, 수 보병 · VEH_101, WPN_101, WPN_201 · video8s · 2:18–2:26
[ACTION-VI] Wide trung: một cánh kỵ Goguryeo giáp ngựa từ đồi nam lao xuống sườn khối 방진 — bắn một loạt tên rồi ngoặt đi trước khi chạm khiên; hàng khiên Tùy khép lại, giáo tua tủa, vài người ngã; kỵ binh đã vòng lại lên đồi. Không cận thương vong.
[SOUND] vó ngựa giáp, dây cung hàng loạt, tên cắm khiên, hô.
N: 결전은 아직이었습니다. 물어뜯고, 물러나고, 다시 물어뜯었습니다. 그것이 닷새 동안의 방식이었습니다.
고구려 기병 장교: 돌아라! 언덕으로!

### SC_018 · LOC_007_SALSU (đồng bờ nam, hậu quân) · 수 후군 장수, 수 보병 · VEH_207, WPN_201 · video8s · 2:26–2:34
[ACTION-VI] Hậu quân: một tướng Tùy giáp 명광개 mũ tua đỏ (수 후군 장수 — EXTRA, không ref riêng) trên ngựa quay lại, quát hàng sau dựng khiên về phía đồi; tên cắm xuống bùn quanh móng ngựa; lính hậu quân gầy, chân bùn, quay mặt về đồi thay vì về sông. Máy trung.
[SOUND] lệnh quát, khiên dựng, tên rơi bùn, ngựa.
N: 뒤는 늘 뒤였습니다. 후군은 강을 등지고 언덕을 보았습니다. 강을 건너려면 먼저 언덕을 막아야 했습니다.
수 후군 장수: 방패를 언덕으로! 강은 나중이다!

### SC_019 · LOC_007_SALSU (KB gò nam) · CHAR_101, 나각수, 궁수 · PROP_018, PROP_024, WPN_101 · still_kenburns · 2:34–2:46
[ACTION-VI] Ảnh wide: gò nam trong mưa — 을지문덕 đứng giữa, cờ đỏ cuộn bên trái, người thổi tù và sừng đen bên phải, một hàng cung thủ với tên quấn vải dầu chưa châm; phía sau gò, hàng kỵ Goguryeo giáp ngựa đứng im dưới mưa như tượng. Ken-burns đẩy chậm vào tù và.
[SOUND] mưa, giáp ướt, im.
N: 을지문덕의 계획은 한 줄이었습니다. 반이 건넜을 때 친다. 그 한 줄을 위해 그는 하루에 일곱 번 졌습니다. 평양 앞에서 물러났고, 시를 보냈고, 항복을 말했습니다. 모두 이 아침을 위해서였습니다. 신호는 붉은 깃발과 나각 세 번이었습니다.

### SC_020 · LOC_007_SALSU (gò nam) · CHAR_101, 기수 · PROP_024 · video8s · 2:46–2:54
[ACTION-VI] 을지문덕 quay đầu nói với lính cầm cờ — không nhìn anh ta, mắt vẫn trên sông; lính cờ gật, siết dây cờ. Cận hai người, mưa.
[SOUND] mưa, giáp, giọng thấp.
N: 깃발이 펴지는 순간은 정해져 있었습니다. 가운데 군이 물에 드는 순간. 물속의 군대는 뛰지 못했습니다.
을지문덕: 깃발은 가운데 군이 물에 들거든 펴게.

### SC_021 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_003 · VEH_001, PROP_006 · video8s · 2:54–3:02
[ACTION-VI] 한승우 nửa người trong cửa tháp K2, ống nhòm nhìn qua khe lau về cổng họng bãi — hàng cọc gỗ, đầu cột quân Tùy đang bò lên khỏi nước; 박기철 đứng dưới đất bên váy xích, ngước lên nói nhỏ, tay vỗ nhẹ lên tấm giáp bùn.
[SOUND] mưa, ống nhòm, tay trên bùn khô.
N: 갈대밭에서 여울 목까지는 삼백 미터였습니다. 아직은 그저 거리였습니다. 전차의 마지막 거리가 될 것이었습니다.
박기철: 여울 목까지 삼백 미터입니다. 발로 쟀습니다.

### SC_022 · LOC_007_SALSU (tuyến bắc bãi lau) · CHAR_002, 사수 · WPN_003, WPN_004 · video8s · 3:02–3:10
[ACTION-VI] Tuyến bắc: hố cát bao cát nối nhau dọc rìa bãi lau, K6 trên giá ba chân phủ lau ở góc, xạ thủ K3 nằm; 오태민 lấy khăn lau nước mưa khỏi băng dính ghi tên trên báng K3 người chết, gấp khăn, bỏ túi ngực. Máy cận tay rồi lên mặt.
[SOUND] mưa, vải lau thép, lau sậy.
N: 북쪽 선. 갈대밭이 끝나고 모래벌이 시작되는 곳이었습니다. 적이 뭍에서 온다면 여기로 올 것이었습니다. 오태민은 양쪽 다 준비했습니다.
오태민: K6는 북쪽. 나머진 내가 본다.

### SC_023 · LOC_007_SALSU (K2 dưới lau, KB) · — · VEH_001, PROP_020 · still_kenburns · 3:10–3:20
[ACTION-VI] Ảnh: K2 dưới rạng đông xám — thân xe trát bùn khô từng lớp, lau sậy cắm dày trên nóc và giá đồ, nòng pháo hạ thấp phủ lau, chỉ một góc 태극기 nhỏ hé dưới bùn; quanh xe, hố cối và giá K6 phủ lau. Ken-burns đẩy chậm vào nòng pháo.
[SOUND] mưa trên lau.
N: 전차는 넉 달 동안 사백 킬로를 달렸습니다. 요동성에서 여기까지, 산길로. 이제 남은 기름은 이십 킬로였습니다. 산길 기준, 박기철의 셈이었습니다. 움직이는 전차가 아니었습니다. 진흙을 바른 쇠 요새였습니다. 여섯 발을 쏘고 나면 그마저도 아니었습니다.

### SC_024 · LOC_007_SALSU (trạm cứu thương trong lau) · CHAR_004, CHAR_107, CHAR_106, 마을 여인 · PROP_009, PROP_019 · video8s · 3:20–3:28
[ACTION-VI] Sâu trong bãi lau: 서아 (mũ đội, bím tóc Goguryeo ướt, băng chữ thập rách góc) xếp băng ép trên tấm chiếu lau; 아리 (khăn olive) đặt bát thuốc giã bên cạnh; ba phụ nữ làng trải chiếu lau thành hàng; 을보 ngồi mài đầu thanh sắt vào đá, tạp dề da ướt. Máy trung.
[SOUND] mưa, chày giã, sắt mài đá.
N: 갈대밭 깊은 곳은 의무실이었습니다. 항생제는 석 달 전에 끝났습니다. 대신 을보 영감의 풀과 마을 여인들의 손이 있었습니다.
아리: 언니, 풀은 다 찧어 놨어요.

### SC_025 · LOC_007_SALSU (bãi lau, radio) · CHAR_005 · EQP_002 · video8s · 3:28–3:36
[ACTION-VI] 태오 áp tổ hợp radio vào tai dưới mũ trụ sắt, bấm PTT hai lần, chờ — chỉ rè; cậu nhìn về hướng đông (thượng lưu), rồi ghi một vạch vào bùn bằng ngón tay.
[SOUND] PTT, rè, mưa.
N: 해모루의 무전기는 사흘째 대답이 없었습니다. 건전지는 충전할 곳이 없었습니다. 말하는 돌은 돌로 돌아가고 있었습니다.
장태오: 말객님 무전기, 응답 없습니다.

### SC_026 · LOC_007_SALSU (mô cát thượng lưu, chân đồi bắc) · CHAR_006, CHAR_105, 고구려 부장 · VEH_101, WPN_001 · video8s · 3:36–3:44
[ACTION-VI] 1,5 km về đông: dưới đường chân đồi bắc, 300 kỵ Goguryeo giáp ngựa đứng im trong lau thấp, chỏm lông đỏ rủ nước; 백성민 trên lưng ngựa hạt dẻ Goguryeo — boonie ướt, khăn ngụy trang, K2C1 đeo chéo — nhìn dải mô cát nối bờ bắc với giữa sông; 해모루 bên cạnh, radio trên giáp, tay ấn máy — im. Máy trung, hai người.
[SOUND] mưa, ngựa thở, nước chảy qua mô cát.
N: 상류 모래톱. 고구려만 아는 길이었습니다. 백성민은 사흘 동안 발로 읽었습니다. 강원도 산에서 배운 눈이었습니다.
백성민: 모래톱 길, 말 배까지 옵니다. 갈 수 있습니다.

### SC_027 · LOC_007_SALSU (bãi lau, đêm trước — flashback) · CHAR_105, CHAR_001 · PROP_020 · video8s · 3:44–3:52
[ACTION-VI] [FLASHBACK 간밤] Đêm trong lau, không lửa, mưa nhỏ; 해모루 ngồi xổm đối diện 한승우, rút nút gỗ khỏi miệng bầu nước bằng vỏ bầu khô, giơ cái nút nhỏ giữa hai ngón tay. Cận hai mặt dưới ánh xanh mờ.
[SOUND] nút bầu "뽁", mưa, im.
N: 간밤. 해모루가 장군의 말을 전했습니다. 그는 병법을 설명하지 않았습니다. 물병 하나면 충분했습니다.
해모루: 마개요. 병이 아무리 커도 마개가 막으면 못 나오오.

### SC_028 · LOC_007_SALSU (bãi lau, đêm trước — flashback) · CHAR_001, CHAR_105 · — · video8s · 3:52–4:00
[ACTION-VI] [FLASHBACK 간밤] 한승우 cầm cái nút gỗ, xoay trong ngón tay — nhỏ, sứt, đen nước; ông không đưa lại, bỏ vào túi ngực cạnh mũi tên cũ (PROP_015). 해모루 nhìn động tác đó, gật.
[SOUND] mưa, vải túi.
N: 마개는 작았습니다. 병은 삼십만이었습니다. 한승우는 그 마개를 돌려주지 않았습니다.
한승우: 마개는… 작군요.

### SC_029 · LOC_007_SALSU (KB bản đồ, chấm đỏ) · — · PROP_001 · still_kenburns · 4:00–4:10
[ACTION-VI] Ảnh: cận bản đồ lụa — chấm son đỏ ở khe bờ bắc, quanh chấm là nét lau vẽ dày; một ngón tay già (을지문덕, không mặt) đặt lên chấm đỏ. Ken-burns đẩy vào ngón tay.
[SOUND] mưa, lụa.
N: 을지문덕은 삼십만을 물에 넣을 수 있었습니다. 물에서 못 나오게 하는 것은 다른 일이었습니다. 목을 막는 것. 그 일에 그는 가장 작은 조각을 놓았습니다. 아흔한 명과 쇠수레 하나였습니다.

### SC_030 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_003 · VEH_001, PROP_006 · video8s · 4:10–4:18
[ACTION-VI] Trở lại rạng đông: qua khe lau, những chiếc khiên đầu tiên của tiền quân Tùy bò lên khỏi cổng họng bãi, cách 300 m, nước chảy khỏi ống quần; 한승우 hạ ống nhòm, nhìn xuống 박기철, nói rất nhỏ.
[SOUND] mưa, đoàn quân lên bờ (xa), ống nhòm.
N: 그는 이제 알았습니다. 나온 자는 뛸 수 있었습니다. 물속에 있는 자는 뛸 수 없었습니다.
한승우: 물속의 반이다. 나온 반이 아니라.

### SC_031 · LOC_007_SALSU (aerial) · — · WPN_201, PROP_021 · still_kenburns · 4:18–4:30
[ACTION-VI] Ảnh aerial: cột quân Tùy đầu đã lên bờ bắc, thân cột nằm dọc bãi cạn, đuôi còn trên đồng bờ nam; bãi lau bờ bắc nằm sát bên cột như một bàn tay mở; gò nam có một chấm đỏ nhỏ (cờ cuộn). Ken-burns kéo ra rất chậm.
[SOUND] mưa, nhạc trầm, dòng quân xa.
N: 병은 강이었습니다. 물은 을지문덕이 막았습니다. 언덕은 고구려 기병이 막았습니다. 을지문덕의 계획에서 그들이 맡은 것은 단 하나였습니다. 마개.

[Kết thúc Phần 2]

## [Phần 3] 탄창 넷 — 「탄창 넷」 / Kiểm kê  (4:30–7:00)
> Tóm tắt VI: 박기철 (tay lành, giọng khàn) đọc bảng đếm lần cuối trên thân K2 trước cả đại đội ngồi xổm trong lau: 포탄 여섯 · 연료 이십 킬로 · 박격포 서른 · PZF 여섯 · K6 두 정 사백 발씩 · K3 여섯 정 삼백 발씩 · 소총 1인당 탄창 넷 · 항생제 없음 · 모르핀 여덟 · 식량 하루 · 91명 — "다 쓰면 끝입니다. 다음은 없습니다." + K5 của 한승우 15 viên. 한승우 tự tay phát băng đạn cho từng người (không thoại). 오태민 nhận băng, nhìn khẩu K3 của người chết. 을보 lội ra cắm que: "가슴까지 왔소." Bờ nam: hậu quân Tùy (수 후군 장수) đã giao tranh với kỵ Goguryeo [史]. Narrator: 30만 5천.
> Chức năng: DECISION (đếm cuối) · Tài nguyên nói thành lời: toàn bảng + "권총 열다섯 발" · Mini-combat [史] SC_046–047 · Open loop: "탄창 넷. 그것이 21세기가 남긴 전부였습니다." → [MID-ROLL 1 · 7:00].

### SC_032 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, 천둥 중대 · VEH_001, PROP_008 · video8s · 4:30–4:38
[ACTION-VI] 박기철 ngồi trên váy xích K2 dưới lau, sổ tay bọc nilon trên đùi, giọng khàn; trước mặt, gần chín mươi người ngồi xổm trong lau thành nửa vòng, mũ bọc lau, mặt bùn, mưa; không ai nhìn sổ — nhìn ông. Máy trung từ sau vai ông.
[SOUND] mưa trên lau, im, giọng khàn.
N: 마지막 점호였습니다. 넉 달 동안 밤마다 다시 쓴 숫자였습니다. 오늘은 다시 쓸 일이 없을 것이었습니다.
박기철: 포탄 여섯. 연료 이십 킬로.

### SC_033 · LOC_007_SALSU (hố cối trong lau) · 사수, 탄약수 · WPN_002 · video8s · 4:38–4:46
[ACTION-VI] Insert: hố cối — hai xạ thủ đặt từng viên đạn cối 81mm lên tấm poncho thành ba hàng mười; đế cối lún cát, chân càng cong; bên cạnh, sáu ống PZF-3 xếp dựa bao cát, nắp còn dán băng keo. Giọng 박기철 ngoài hình.
[SOUND] đạn cối chạm nhau, mưa trên poncho.
N: 서른 발. 요동성에서 백이십 발로 시작한 숫자였습니다.
박기철: (off) 박격포 서른. 판처파우스트 여섯.

### SC_034 · LOC_007_SALSU (tuyến bắc, giá K6) · 사수 · WPN_004, WPN_003 · video8s · 4:46–4:54
[ACTION-VI] Insert: K6 trên giá ba chân, xạ thủ đếm dây đạn 12.7 xếp trong hộp thiếc; hố bên, xạ thủ K3 trải dây đạn 5.56 lên lau khô, đếm bằng ngón tay. Giọng 박기철 ngoài hình.
[SOUND] dây đạn kim loại, mưa.
N: 사백과 삼백. 요동성 성벽에서는 하룻밤에 쓰던 양이었습니다.
박기철: (off) K6 두 정, 사백 발씩. K3 여섯 정, 삼백 발씩.

### SC_035 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001 · video8s · 4:54–5:02
[ACTION-VI] Cận 박기철: ông gấp một ngón, hai ngón, ba, bốn — giơ bàn tay bốn ngón lên cho cả hàng thấy; mưa chảy từ vành mũ lưỡi trai xuống mu bàn tay.
[SOUND] mưa, im.
N: 넷. 철원에서는 한 사람에 여덟이었습니다. 넉 달 동안 절반이 갔습니다.
박기철: 소총, 일인당 탄창 넷.

### SC_036 · LOC_007_SALSU (KB sổ tay) · — · PROP_008 · still_kenburns · 5:02–5:12
[ACTION-VI] Ảnh cận: trang sổ tay ướt mép, bút chì — một cột số viết tay dọc trang, gạch xóa nhiều lần, con số cuối mỗi dòng nhỏ dần; góc trang, một vết dầu và một vết máu cũ. Ken-burns trượt dọc cột số từ trên xuống. (Chữ không cần đọc được.)
[SOUND] mưa, giấy.
N: 이 공책은 3월 요하에서 시작되었습니다. 첫 장에는 스물두 발, 사백 킬로, 아흔넷이 적혀 있었습니다. 마지막 장에는 지울 것이 거의 남지 않았습니다. 이 부대의 넉 달은 이 공책 한 권이었습니다.

### SC_037 · LOC_007_SALSU (trạm cứu thương, rìa) · CHAR_004, CHAR_003 (giọng) · PROP_009 · video8s · 5:12–5:20
[ACTION-VI] 서아 ngồi ở rìa nửa vòng, túi quân y mở trên đùi — tám ống morphine xếp trong ngăn, ngăn kháng sinh trống; cô ngẩng lên khi nghe số của mình, gật một cái. Giọng 박기철 ngoài hình.
[SOUND] mưa, khóa túi.
N: 그 세 글자는 석 달 동안 변하지 않았습니다. 여덟은 여덟 사람의 마지막 밤을 위한 숫자였습니다.
박기철: (off) 항생제 없음. 모르핀 여덟. 식량 하루.

### SC_038 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, 천둥 중대 · VEH_001 · video8s · 5:20–5:28
[ACTION-VI] 박기철 ngẩng khỏi sổ, nhìn từng khuôn mặt trong nửa vòng — chậm, từ trái sang phải; máy theo mắt ông lướt qua các mặt bùn; ông nói con số cuối.
[SOUND] mưa, im.
N: 아흔넷으로 왔습니다. 석문령에 하나를 묻었습니다. 살수에 둘을 묻었습니다. 그 숫자를 그는 형용사 없이 읽었습니다.
박기철: 아흔한 명.

### SC_039 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001 · video8s · 5:28–5:36
[ACTION-VI] 박기철 đóng sổ, nhét vào túi ngực, vỗ lên túi một cái; nói câu cuối không cao giọng, rồi tụt xuống khỏi váy xích.
[SOUND] sổ đóng, mưa, giày chạm cát.
N: 다음이 없다는 말은 위협이 아니었습니다. 산수였습니다. 박기철의 산수는 넉 달 동안 한 번도 틀리지 않았습니다.
박기철: 다 쓰면 끝입니다. 다음은 없습니다.

### SC_040 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, CHAR_001 · WPN_001 (K5 trong bao) · video8s · 5:36–5:44
[ACTION-VI] 박기철 đi ngang qua 한승우 đang đứng dựa xích xe, liếc xuống bao súng ngắn K5 ở đùi ông, nói khô không cười; 한승우 đặt tay lên bao súng, khóe miệng nhếch một chút.
[SOUND] mưa, dây bao súng.
N: 그는 지휘관의 권총까지 세었습니다. 정비반장에게 숫자에 예외는 없었습니다.
박기철: 중대장님 권총은 열다섯 발입니다. 그것도 셌습니다.

### SC_041 · LOC_007_SALSU (bãi lau, hàng lính) · CHAR_001, 천둥 중대 · WPN_001, PROP_008 · video8s · 5:44–5:52
[ACTION-VI] 한승우 đi dọc hàng người ngồi xổm, hộp đạn mở trên tay trái, tay phải đặt từng băng đạn vào lòng bàn tay mỗi người — bốn băng, đếm bằng ngón cái; người nhận nhìn ông, không ai nói. Tracking chậm theo tay.
[SOUND] băng đạn chạm lòng bàn tay, mưa, thở.
N: 그는 탄창을 직접 나눠 주었습니다. 소대장에게 맡길 수도 있었습니다. 그는 한 사람씩 손에 쥐여 주었습니다. 이 탄창이 마지막이라는 말을, 그는 손으로 했습니다.

### SC_042 · LOC_007_SALSU (bãi lau, hàng lính) · CHAR_001, CHAR_005 · WPN_001 · video8s · 5:52–6:00
[ACTION-VI] 한승우 quỳ xuống trước 태오 — mũ trụ sắt Goguryeo lệch trên đầu cậu; ông đặt bốn băng vào tay cậu, rồi chỉnh lại quai da mũ trụ dưới cằm cậu bằng hai tay, siết. 태오 ngồi im. Không thoại.
[SOUND] da quai mũ, mưa trên sắt.
N: 장태오는 걷지 못했습니다. 철모는 석문령에서 돌아왔지만 투구를 잃은 사수에게 갔습니다. 야시경은 돌아오지 않았습니다. 천사백 년 전의 투구가 스물한 살의 머리에 맞았습니다.

### SC_043 · LOC_007_SALSU (tuyến bắc) · CHAR_001, CHAR_002 · WPN_001, WPN_003 · video8s · 6:00–6:08
[ACTION-VI] 오태민 đứng dậy nhận băng đạn từ 한승우 — hai người ngang mặt; 오태민 nhận, không nhìn băng đạn — nhìn xuống khẩu K3 dựa bao cát cạnh chân, băng dính tên trên báng; 한승우 theo mắt anh, không nói, đi tiếp.
[SOUND] mưa, băng đạn vào túi.
N: 석문령의 사수는 이름이 있었습니다. 오태민은 그 이름을 총에 붙여 두었습니다. 넉 달 전 그는 화력을 믿었습니다. 이제 그는 화력이 무엇을 남기는지 알았습니다.

### SC_044 · LOC_007_SALSU (mép nước rìa bãi lau, nhánh sông) · CHAR_106 · PROP_019, PROP_020 · video8s · 6:08–6:16
[ACTION-VI] 을보 xắn quần, lội ra nhánh sông sau bãi lau với một que gỗ có khắc vạch — nước lên dần, tới đùi, tới bụng, tới ngực ông; ông cắm que xuống đáy cát, ngoảnh lại gào nhỏ về phía lau. Máy từ bờ.
[SOUND] nước khua, que cắm cát, giọng già.
N: 을보 영감이 물을 쟀습니다. 나흘 전에는 허리였습니다. 어제는 배였습니다. 강은 화가 나 있었습니다. 그가 예언한 대로였습니다.
을보: 가슴까지 왔소.

### SC_045 · LOC_007_SALSU (bãi lau, K2) · CHAR_106, CHAR_003 · VEH_001 · video8s · 6:16–6:24
[ACTION-VI] 을보 lên bờ, quần áo ướt sũng, đi thẳng tới K2, đặt bàn tay già lên tấm giáp bùn, nheo mắt trái nhìn 박기철; 박기철 đang siết dây lau trên nóc, nhìn xuống, không trả lời.
[SOUND] mưa, dây thừng, bàn tay trên bùn khô.
N: 쇠는 헤엄치지 못했습니다. 대장장이는 그것을 알았습니다. 정비반장도 알았습니다. 두 사람 다 말하지 않았습니다.
을보: 쇠쟁이, 물이 이놈 배까지 오면 어쩌려고.

### SC_046 · LOC_007_SALSU (bờ nam, đuôi 방진) · 고구려 기병, 수 보병 · VEH_101, WPN_101, WPN_201 · video8s · 6:24–6:32
[ACTION-VI] Bờ nam: hậu quân Tùy dồn ứ ở mép nước, hàng sau chưa xuống được vì hàng trước chậm; từ đồi, một cánh kỵ Goguryeo giáp ngựa lao thẳng vào đuôi khối — lần này không ngoặt, giáo dài hạ ngang chọc vào hàng khiên; khiên vỡ, người ngã xuống nước nông. Wide trung, không cận thương vong.
[SOUND] vó ngựa giáp, giáo chạm khiên, hô, nước.
N: 뒤에서는 이미 싸움이 시작되어 있었습니다. 후군은 강에 들어가려 했고, 고구려 기병은 그것을 막았습니다. 뒤가 물에 들어가지 못하면 앞은 물에서 나올 수 없었습니다.

### SC_047 · LOC_007_SALSU (bờ nam, hậu quân) · 수 후군 장수, 수 보병 · VEH_207, WPN_201, PROP_021 · video8s · 6:32–6:40
[ACTION-VI] 수 후군 장수 trên ngựa giữa hàng khiên hậu quân ở mép nước, kiếm chỉ về đồi, hàng khiên khép lại; lính hậu quân vừa dựng khiên vừa bước giật lùi xuống nước — nước lên tới thắt lưng họ khi còn quay mặt về đồi. Máy trung, thấp.
[SOUND] lệnh quát, khiên, nước, tên rơi.
N: 30만 5천. 그 숫자가 사백 미터 폭의 여울 위에 늘어서 있었습니다. 앞은 뭍이었고, 가운데는 물이었고, 뒤는 싸움이었습니다.
수 후군 장수: 방패! 물러서지 마라!

### SC_048 · LOC_007_SALSU (aerial) · — · WPN_201, VEH_101 · still_kenburns · 6:40–6:50
[ACTION-VI] Ảnh aerial cao: đầu cột quân ở bờ bắc, thân cột dày đặc trên bãi cạn, đuôi khối 방진 trên đồng bờ nam có những vệt kỵ binh Goguryeo cắm vào như răng; mưa che mờ phía xa. Ken-burns kéo ra chậm.
[SOUND] mưa, dòng quân, trống xa.
N: 을지문덕은 물속의 반을 기다렸습니다. 아직 반이 아니었습니다. 두 시간이 더 필요했습니다. 갈대밭의 아흔한 명은 그 두 시간을 탄창 넷과 함께 기다렸습니다.

### SC_049 · LOC_007_SALSU (aerial, 방진 chạm mép nước) · — · WPN_201, PROP_021 · still_kenburns · 6:50–7:00
[ACTION-VI] Ảnh aerial thấp hơn: khối 방진 đầy đủ chạm mép nước bờ nam — hàng khiên đầu tiên của trung quân bước xuống sông, lá cờ lớn của 우중문 ở giữa khối bắt đầu di chuyển về phía nước. Không thoại. Ken-burns đẩy chậm vào lá cờ.
[SOUND] mưa, một hồi trống Tùy, im dần.
N: 탄창 넷. 그것이 21세기가 남긴 전부였습니다.

[MID-ROLL 1 · 7:00]

[Kết thúc Phần 3]

## [Phần 4] 붉은 깃발 — 「붉은 깃발」 / Cuộc chạm trán đầu tiên  (7:00–10:30)
> Tóm tắt VI: Tiền quân Tùy lội qua — hàng nghìn, khiên trên đầu, ngựa bơi; lên bãi bắc qua cổng họng, đi qua cách lau 200 m; 오태민 (radio thì thầm): "지금입니다." 한승우: "아직." Một 척후 Tiên Ti thấy vết xích K2 trong bùn → phi về; 탁발흠 gật — hắn đợi sẵn và nói thành lời bài học: "천둥은 셀 수 있다. 다 세면 들어간다." Trung quân xuống nước — cờ 우중문 ra mô cát giữa sông (quyết định đứng giữa sông); 방진 méo trong nước [史]. Gò nam: 을지문덕 giơ tay — cờ đỏ mở; tên lửa; trống ba bề; kỵ Goguryeo từ đồi hai bờ đổ vào hậu quân [史]. Trong lau: chưa có 나각 — 한승우 chờ.
> Chức năng: THREAT + CONTACT · Tài nguyên: — · Enemy adaptation: 탁발흠 xác nhận vị trí K2 qua vết xích; "đếm sấm" · Payoff: "반이 건널 때까지" (4화) · Combat: SC_069–071 · Open loop: "붉은 깃발이 올랐습니다. 절반이 물속에 있었습니다."
> Sau mid-roll 1: SC_050 hình mạnh, không thoại.

### SC_050 · LOC_007_SALSU (bãi cạn, từ trong lau) · 수 보병 · WPN_201 · video8s · 7:00–7:08
[ACTION-VI] POV thấp từ trong lau qua khe lá: tiền quân Tùy lội ngang bãi cạn — khiên tròn giơ trên đầu thành một mái khiên dài, giáo dựng như rừng, nước tới ngực, mưa nặng hạt hơn; ngựa bơi giữa hàng người, cổ ngẩng. Không thoại.
[SOUND] mưa nặng hạt, nước khua nặng, khiên chạm, thở của hàng nghìn người.
N: 비가 굵어졌습니다. 강은 그 비를 받아 다시 한 뼘 올랐습니다.

### SC_051 · LOC_007_SALSU (cổng họng bãi bờ bắc) · 수 보병 · WPN_201, PROP_021 · video8s · 7:08–7:16
[ACTION-VI] Cổng họng bãi: khe rộng 60 m giữa bãi lau và bờ bùn dốc — lính Tùy bò lên khỏi nước, quần áo chảy nước, khiên kéo lê, có người ngã vào bùn và được kéo dậy; cột người qua khe rồi tỏa ra bãi cát bắc về phía con đường lên đồi. Máy từ rìa lau, ngang tầm mắt, cách 200 m.
[SOUND] bùn, thở dốc, khiên lê cát, mưa.
N: 목을 지나면 뭍이었습니다. 뭍에 오른 자는 살았습니다. 앞의 오만은 그렇게 살았습니다. 갈대밭에서 이백 미터였습니다.

### SC_052 · LOC_007_SALSU (bờ bắc, trên cổng họng) · CHAR_203 · VEH_207, WPN_201 · video8s · 7:16–7:24
[ACTION-VI] 우문술 dắt ngựa xám lên khỏi bùn ở cổng họng, mũ đội, áo choàng ướt nặng; lên tới gờ cát ông dừng, quay nhìn xuống bãi cạn — trung quân bắt đầu xuống nước phía bờ nam; ông nhìn rồi nhìn bãi lau bên trái, một nhịp, rồi quay đi. Máy trung.
[SOUND] mưa, ngựa thở, giáp ướt.
N: 우문술은 뭍에 올랐습니다. 그는 갈대밭을 한 번 보았습니다. 갈대는 갈대였습니다. 그는 강을 더 오래 보았습니다.
우문술: 선봉은 멈추지 마라. 언덕까지 간다.

### SC_053 · LOC_007_SALSU (tuyến bắc) · CHAR_002 · WPN_003, EQP_002 · video8s · 7:24–7:32
[ACTION-VI] 오태민 trong hố cát, mặt ép sát bao cát, mắt trên hàng người Tùy đang tỏa ra bãi cát bắc cách 200 m — nhiều tới mức không thấy cát; ngón tay trên PTT, giọng thì thầm khản.
[SOUND] mưa, PTT, tiếng đoàn quân gần.
N: 오만 명이 총구 앞을 지나갔습니다. 열이틀 전에도 이 강가에서 삼십만을 보냈습니다. 오늘은 쏘기로 했습니다. 아직 아니었을 뿐입니다.
오태민: (thì thầm, radio) 천둥 지휘, 여기는 1소대. 지금입니다.

### SC_054 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · VEH_001, EQP_002 · video8s · 7:32–7:40
[ACTION-VI] Cận 한승우 trong cửa tháp: mắt không rời cổng họng, ngón tay bấm PTT trên tổ hợp vai, một chữ. Mưa chảy qua mặt.
[SOUND] PTT, mưa trên bùn khô.
한승우: (radio) 아직.

### SC_055 · LOC_007_SALSU (KB, POV mặt đất) · 수 보병 (chân) · WPN_201 · still_kenburns · 7:40–7:48
[ACTION-VI] Ảnh POV sát mặt cát từ trong lau: một rừng chân — giày cỏ rách, ống quần ướt, mũi giáo lê cát, khiên kéo — đi ngang qua cách ống kính vài mét, mờ dần vào mưa. Ken-burns trượt ngang theo bước chân.
[SOUND] hàng vạn bước chân trên cát ướt, mưa.
N: 넉 달 전, 요하에서 그들은 이 군대를 처음 보았습니다. 끝이 안 보인다고 태오가 말했습니다. 오늘은 끝이 보였습니다. 강 건너 남쪽 언덕 아래였습니다.

### SC_056 · LOC_007_SALSU (bãi lau, radio) · CHAR_005 · EQP_002 · video8s · 7:48–7:56
[ACTION-VI] 태오 trong hố với mũ trụ sắt, tổ hợp radio kề miệng, giọng thì thầm truyền lệnh cho toàn tuyến; tay kia đặt lên báng K2C1 gác trên miệng hố.
[SOUND] PTT, mưa trên sắt.
N: 명령은 한 단어였습니다. 그 단어가 갈대밭 전체로 퍼졌습니다.
장태오: (thì thầm, radio) 전 소대, 여기는 천둥 지휘. 사격 금지. 대기.

### SC_057 · LOC_007_SALSU (bãi cát bắc, rìa lau phía đông) · 척후 선비 · VEH_206 · video8s · 7:56–8:04
[ACTION-VI] Bãi cát bắc: hai kỵ trinh sát Tiên Ti (giáp da, mũ lông) đi chậm dọc rìa đông bãi lau, cách cột quân Tùy; một người xuống ngựa, cúi xem mặt bùn — hai vệt xích rộng in sâu, mưa chưa xóa hết, chạy từ bãi cát vào trong lau. Anh ta ngẩng nhìn vào lau.
[SOUND] mưa, vó ngựa chậm, bùn dưới gối.
N: 이틀 전 밤, 전차는 상류 갈대섬에서 삼 킬로를 내려왔습니다. 여울 목에서 삼백 미터. 자국은 이틀 비에도 지워지지 않았습니다.
척후 선비: …바퀴 자국이다.

### SC_058 · LOC_007_SALSU (tuyến bắc, hố phía đông) · 사수, CHAR_002 · WPN_001 · video8s · 8:04–8:12
[ACTION-VI] Trong hố ở góc đông tuyến bắc: một lính Hàn đã ngắm thẳng vào lưng tên trinh sát cách 60 m, ngón tay đặt lên cò; bàn tay 오태민 từ bên cạnh ấn nòng súng xuống bao cát — chậm, chắc; hai người nhìn nhau. Không thoại.
[SOUND] mưa, hơi thở nén, nòng chạm bao cát.

### SC_059 · LOC_007_SALSU (bãi cát bắc) · 척후 선비 · VEH_206 · video8s · 8:12–8:20
[ACTION-VI] Tên trinh sát nhảy lên ngựa, quay đầu, phi nước đại về phía đồi bắc qua bãi cát, bùn văng; người thứ hai theo sau. Máy tracking ngang, thấp.
[SOUND] vó ngựa dồn, mưa.
N: 한 발이면 그를 멈출 수 있었습니다. 한 발이면 아흔한 명이 들켰습니다. 척후는 달렸습니다. 갈대밭은 그를 보냈습니다.

### SC_060 · LOC_007_SALSU (chân đồi bắc) · CHAR_205, 척후 선비 · VEH_206, EQP_001 · video8s · 8:20–8:28
[ACTION-VI] Chân đồi bắc, trong mưa: 탁발흠 trên ngựa lùn, mũ vành lông cáo ướt, sẹo thái dương, kính nhìn đêm vỡ mặt kính treo bằng dây da trước ngực, cẳng tay phải quấn băng vải đen bẩn (vết dao 백성민 đêm cứu 태오); sau ông, hàng kỵ Tiên Ti đứng im trong lau thấp tới tận sườn đồi; trinh sát phi tới, nói gấp; ông không đổi mặt, gật một cái.
[SOUND] mưa, ngựa thở, giọng trinh sát.
N: 그는 놀라지 않았습니다. 열흘 전 밤, 이 강가의 갈대를 야시경으로 보았습니다. 그들은 갈대를 떠나지 않는 자들이었습니다.
탁발흠: 안다. 검은 소는 거기 있다.

### SC_061 · LOC_007_SALSU (chân đồi bắc) · CHAR_205, 선비 기병 · VEH_206 · video8s · 8:28–8:36
[ACTION-VI] 탁발흠 quay sang hai thủ lĩnh nhỏ bên cạnh, giơ bàn tay xòe năm ngón rồi nắm lại từng ngón — như đếm; nói ngắn. Kỵ binh sau lưng vẫn im; tai ngựa nhét vải trắng lộ dưới mưa.
[SOUND] mưa, giáp da, giọng khô.
N: 요동성에서 열 번, 석문령에서 네 번, 열흘 전 밤에 두 번. 천둥이 마르고 있었습니다.
탁발흠: 기다려라. 천둥은 셀 수 있다. 다 세면 들어간다.

### SC_062 · LOC_007_SALSU (bãi cạn, trung quân) · CHAR_202, 기수, 수 보병 · VEH_207, PROP_021 · video8s · 8:36–8:44
[ACTION-VI] Trung quân xuống nước: khối vuông méo dần khi các hàng lội ở tốc độ khác nhau — hàng ngoài chậm, hàng trong dồn; 우중문 trên ngựa đen giữa khối, cờ đại quân bên cạnh, nước lên bụng ngựa. Aerial thấp.
[SOUND] nước, hô giữ hàng, cờ ướt.
N: 가운데 군이 물에 들었습니다. 네모는 물속에서 네모로 남지 못했습니다. 물은 줄을 흐트러뜨렸습니다. 흐트러진 군대는 느렸습니다. 느린 군대는 물속에 오래 있었습니다.

### SC_063 · LOC_007_SALSU (mô cát giữa sông) · CHAR_202, 기수 · VEH_207, PROP_021 · video8s · 8:44–8:52
[ACTION-VI] Ngựa 우중문 leo lên mô cát giữa sông — dải cát nổi vừa đủ cho vài trăm người; ông ghìm cương, chỉ xuống cát; lính cầm cờ cắm cán cờ đỏ xuống cát, cờ ướt rũ rồi bung ra trong gió. Quanh mô cát, nước ngập tới ngực người. Máy trung, thấp.
[SOUND] cán cờ cắm cát, cờ bung, nước.
N: 강 가운데 모래톱. 삼십만이 볼 수 있는 높은 곳이었습니다. 깃발이 보이면 군대는 건넜습니다. 깃발이 넘어지면, 군대도 넘어질 것이었습니다.
우중문: 여기 선다. 깃발을 세워라.

### SC_064 · LOC_007_SALSU (mô cát giữa sông) · CHAR_202 · VEH_207 · video8s · 8:52–9:00
[ACTION-VI] Cận: chân ngựa 우중문 trên mép mô cát — nước xám đục xoáy qua móng, dâng lên mắt cá rồi lên ống chân ngựa trong lúc máy quay; ngựa giậm, bất an; bàn tay ông siết cương, mắt nhìn xuống nước.
[SOUND] nước xoáy, ngựa giậm, mưa.
N: 물은 서 있는 동안에도 올랐습니다. 상류의 비가 이제 여기 닿고 있었습니다. 을지문덕이 막은 것이 아니었습니다. 하늘이 막은 것이었습니다.

### SC_065 · LOC_007_SALSU (aerial) · — · WPN_201, PROP_021 · still_kenburns · 9:00–9:10
[ACTION-VI] Ảnh aerial cao: cột quân — đầu đã trải lên bãi cát bắc và con đường lên đồi, giữa là khối trung quân dày đặc trong nước quanh mô cát có chấm cờ đỏ, đuôi hậu quân còn ở mép bờ nam trong khói bụi giao tranh nhỏ. Ken-burns đẩy chậm vào khối giữa.
[SOUND] mưa, dòng quân, trống xa.
N: 절반. 앞은 뭍에, 뒤는 물가에, 가운데는 물속에 있었습니다. 을지문덕이 기다린 그림이었습니다. 하루 일곱 번 져서 그린 그림이었습니다.

### SC_066 · LOC_007_SALSU (gò nam) · CHAR_101, 기수 · PROP_024 · video8s · 9:10–9:18
[ACTION-VI] Gò nam: 을지문덕 giơ bàn tay phải lên ngang vai, không nhìn ai; lính cầm cờ cắt dây — lá cờ đỏ bung ra hết chiều dài trong mưa, rực trên nền trời xám. Low-angle từ chân gò.
[SOUND] dây cắt, cờ bung "펄럭", mưa.
N: 을지문덕은 손을 들었습니다. 말은 하지 않았습니다.

### SC_067 · LOC_007_SALSU (gò nam, hàng cung thủ) · 궁수 · WPN_101, PROP_016 · video8s · 9:18–9:26
[ACTION-VI] Hàng cung thủ Goguryeo châm tên quấn vải dầu vào chậu than, giương cung cùng lúc, thả — một loạt tên lửa vẽ vòng cung cam qua bầu trời mưa xám về phía sông. Low-angle theo tên bay. Không thoại.
[SOUND] dây cung hàng loạt, lửa rít trong mưa.
고구려 궁수 장교: 불화살, 쏴라!

### SC_068 · LOC_007_SALSU (đồi hai bờ, trống) · 고구려 고수 · PROP_017 · video8s · 9:26–9:34
[ACTION-VI] Gò nam: hàng trống trận Goguryeo — dùi giáng xuống mặt da ướt, nước bắn; máy pan từ dùi trống lên trời xám rồi xuống sông: xa bên kia sông, trên đồi bờ bắc phía đông, một vệt cờ 삼족오 và khói tín hiệu — trống bên ấy đáp lại (nghe, không thấy rõ).
[SOUND] ba dàn trống dội vào nhau, vang qua sông.
N: 북이 세 방향에서 울렸습니다. 남쪽 언덕, 동쪽 언덕, 강 건너 북쪽 언덕. 수나라 군대는 그 순간 깨달았습니다. 고구려는 강 양쪽에 다 있었습니다.

### SC_069 · LOC_007_SALSU (bờ nam, hậu quân) · 고구려 기병, 수 보병 · VEH_101, WPN_201 · video8s · 9:34–9:42
[ACTION-VI] Từ đồi nam, kỵ Goguryeo giáp ngựa đổ xuống thành dòng dài, giáo hạ, đâm thẳng vào hậu quân đang dồn ở mép nước; hàng khiên Tùy vỡ ở hai chỗ; ngựa giáp lao vào nước nông. Wide trung, không cận thương vong.
[SOUND] vó ngựa như sấm, giáo chạm khiên, hô, nước.
N: 이번에는 물러나지 않았습니다. 하루에 일곱 번 물러났던 기병이었습니다. 여덟 번째는 결전이었습니다.
고구려 기병 장교: 밀어라! 물까지!

### SC_070 · LOC_007_SALSU (bờ nam, mép nước) · 수 후군 장수, 수 보병 · VEH_207, WPN_201 · video8s · 9:42–9:50
[ACTION-VI] 수 후군 장수 trên ngựa quát hàng khiên khép lại, kiếm vung; tên Goguryeo cắm dày lên khiên và bùn; lính hậu quân lùi xuống nước tới thắt lưng, khiên vẫn hướng về đồi. Máy trung.
[SOUND] lệnh quát, tên cắm khiên, nước, ngựa hí.
N: 후군 장수는 물러서지 않았습니다. 후군이 무너지면 물속의 가운데 군은 등을 내주는 것이었습니다.
수 후군 장수: 방패 세워라! 강을 등져라!

### SC_071 · LOC_007_SALSU (đồi bờ bắc phía đông) · 고구려 기병 · VEH_101, PROP_012 · video8s · 9:50–9:58
[ACTION-VI] Đồi thấp bờ bắc phía đông cổng họng: một hàng kỵ Goguryeo giáp ngựa hiện lên trên đường đỉnh đồi trong mưa, cờ 삼족오 đen trên nền vàng, chỏm lông đỏ; họ đứng im nhìn xuống tiền quân Tùy đang tỏa trên bãi cát bắc. Low-angle từ bãi cát.
[SOUND] mưa, giáp, trống bắc gần hơn.
N: 북쪽 언덕에도 고구려가 있었습니다. 뭍에 오른 오만은 뭍에서도 안전하지 않았습니다.

### SC_072 · LOC_007_SALSU (bãi cát bắc) · CHAR_203 · VEH_207 · video8s · 9:58–10:06
[ACTION-VI] 우문술 trên ngựa giữa tiền quân trên bãi cát bắc, quay đầu nhìn đồi đông bờ bắc, rồi quay nhìn qua sông về gò nam có cờ đỏ; mặt xám; ông nói với phó tướng bên cạnh, giọng thấp không hoảng.
[SOUND] mưa, trống hai bờ, ngựa.
N: 우문술은 세었습니다. 그는 늘 세는 사람이었습니다. 군량을 세었고, 날을 세었고, 이제 언덕을 세었습니다.
우문술: 양쪽이다. 고구려가 양쪽 언덕에 있다.

### SC_073 · LOC_007_SALSU (trạm cứu thương trong lau) · CHAR_107, CHAR_004, 마을 여인 · PROP_009 · video8s · 10:06–10:14
[ACTION-VI] Trong lau: 아리 ngồi bó gối, hai tay bịt tai dưới tiếng trống ba bề; một phụ nữ làng kéo cô vào lòng; 서아 bên cạnh vẫn tay siết từng garô sẵn lên cẳng tay mình thử độ chặt, mắt không rời việc. Máy cận hai người.
[SOUND] trống dội qua sông, mưa trên lau, thở.
N: 북소리는 갈대밭까지 왔습니다. 서아는 지혈대를 하나씩 조였습니다. 곧 쓸 것이었습니다. 몇 개나 쓸지는 몰랐습니다.
아리: 언니, 북소리가 세 군데예요.

### SC_074 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_003 · VEH_001 · video8s · 10:14–10:22
[ACTION-VI] 한승우 nửa người trong cửa tháp, tay trái giơ lên — bàn tay mở, ra hiệu "chờ" cho 박기철 và tổ cối bên dưới; ông nghiêng đầu nghe — trống, tên lửa, hô — không có tiếng tù và; 박기철 dưới đất ngước lên, nói nhỏ.
[SOUND] trống xa, mưa, im giữa hai người.
N: 깃발은 올랐습니다. 북도 울렸습니다. 그러나 그의 신호는 나각이었습니다. 세 번. 그는 손을 내리지 않았습니다.
박기철: 나각은 아직입니다.

### SC_075 · LOC_007_SALSU (KB gò nam, cờ đỏ) · CHAR_101 (xa) · PROP_024 · still_kenburns · 10:22–10:30
[ACTION-VI] Ảnh: gò nam trong mưa — lá cờ đỏ dài bung hết trên nền mây xám, dưới cờ là bóng 을지문덕 nhỏ; dưới gò, sông đầy người và ngựa, cột khói tên lửa mỏng. Ken-burns đẩy chậm vào cờ.
[SOUND] cờ đập gió, mưa, trống.
N: 붉은 깃발이 올랐습니다. 절반이 물속에 있었습니다.

[Kết thúc Phần 4]

## [Phần 5] 여섯, 다섯, 넷 — 「여섯, 다섯, 넷」 / Chứng minh sức mạnh  (10:30–14:00)
> Tóm tắt VI: 나각 ba hồi từ gò nam — hiệu lệnh của 을지문덕. Radio 박기철: "여섯." — K2 khai hỏa vào cụm cờ trên mô cát giữa sông. "다섯… 넷… 셋… 둘… 하나." Sáu tiếng nổ, sáu con số, không lời nào khác (narrator im 10:38–12:30). Cối 30 viên vào cổng họng bãi; PZF 6 vào bè chở xe ngựa; kỵ Goguryeo hai bờ đổ vào hậu quân — 신세웅 ngã [史]. 박기철: "다 썼습니다." Vấn đề mới: tiền quân trên bãi bắc quay lại mở đường xuống sông — thẳng vào nút chai. Trên đồi bắc, 탁발흠 đếm ngón tay: "여섯. …그리고 조용하다."
> Chức năng: BATTLE (đòn của đại đội) · Tài nguyên nói thành lời: "여섯…하나", "다 썼습니다", "박격포, 탄 없음" · K2 6→0 · cối 30→0 · PZF 6→0 · Enemy adaptation: đếm — biết xe câm · Combat: SC_076–100 · Open loop: 탁발흠 "여섯. 그리고 조용하다." → [MID-ROLL 2 · 14:00].
> [NARRATOR IM LẶNG] 10:38 → 12:30 (SC_077–090).

### SC_076 · LOC_007_SALSU (gò nam) · CHAR_101, 나각수 · PROP_018 · video8s · 10:30–10:38
[ACTION-VI] Gò nam: 을지문덕 hạ tay đã giơ, quay đầu nhìn người thổi tù và; người ấy nâng tù và sừng đen lên miệng, ngực phồng — thổi: một hồi trầm dài, ngắt, hồi hai, ngắt, hồi ba. Cận tù và rồi mặt 을지문덕 — không đổi.
[SOUND] tù và trầm ba hồi, vang qua sông; trống ngừng một nhịp.
N: 나각이 세 번 울렸습니다. 그것이 신호였습니다.

[NARRATOR IM LẶNG — 10:38 → 12:30]

### SC_077 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · VEH_001 · video8s · 10:38–10:46
[ACTION-VI] 한승우 trong cửa tháp nghe hồi thứ ba — bàn tay trái đang giơ chém xuống một nhát; ông tụt vào tháp, nắp cửa khép còn hé; qua khe, ánh màn hình xanh trên mặt ông; môi động — lệnh nội bộ không nghe được. Không thoại.
[SOUND] tù và tắt, nắp cửa sắt, mưa, tiếng quạt tháp pháo xoay rất nhỏ.

### SC_078 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001, EQP_002 · video8s · 10:46–10:54
[ACTION-VI] 2-BEAT: (a) 10:46–10:50 박기철 quỳ sát váy xích, một tay bịt tai, tay kia bấm PTT, nói một chữ; (b) 10:50–10:54 K2 khai hỏa — chớp lửa xé qua bãi lau, lau rạp thành vòng, bùn trên tháp văng, sóng xung kích làm mưa ngừng một nhịp. Máy thấp từ sau lưng 박기철.
[SOUND] PTT; tiếng pháo 120mm xé, dội qua sông, lau rạp.
박기철: (radio) 여섯.

### SC_079 · LOC_007_SALSU (mô cát giữa sông) · CHAR_202, 기수, 수 기병 · VEH_207, PROP_021 · video8s · 10:54–11:02
[ACTION-VI] Mô cát giữa sông: viên đạn nổ giữa cụm cờ — cát và nước bốc thành cột, ngựa tung, cờ đỏ bay lên rồi rơi xuống nước, người văng; quanh mô cát, hàng nghìn khiên trong nước cùng quay đầu về cột nước. Wide trung, không cận thương vong.
[SOUND] nổ, cát rơi lộp độp xuống nước, ngựa hí, tiếng người gào dội.

### SC_080 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001, EQP_002 · video8s · 11:02–11:10
[ACTION-VI] 2-BEAT: (a) 박기철, tai bịt, PTT — một chữ; (b) K2 khai hỏa viên thứ hai — máy cận nòng pháo: lửa, khói, bùn trên nòng rụng.
[SOUND] PTT; pháo; vỏ đạn nhôm bật trong tháp.
박기철: (radio) 다섯.

### SC_081 · LOC_007_SALSU (mô cát giữa sông) · CHAR_202, 기수 · VEH_207, PROP_021 · video8s · 11:10–11:18
[ACTION-VI] Viên thứ hai nổ ở đầu mô cát: cán cờ gãy đôi, cờ đỏ chìm; ngựa đen của 우중문 dựng lên, hất ông xuống nước ngang ngực; ông nổi lên, áo choàng đỏ rách nửa, một gương ngực móp, bíu vào cán cờ gãy. Máy trung, ngang mặt nước.
[SOUND] nổ, nước dội, ngựa, thở sặc nước.

### SC_082 · LOC_007_SALSU (trong tháp K2) · CHAR_001, 포수 · VEH_001 · video8s · 11:18–11:26
[ACTION-VI] 2-BEAT: (a) trong tháp: 한승우 dán mắt vào thị kính trưởng xe, ánh sáng xanh; góc màn hình bộ đếm đạn nhảy "04" → "03"; pháo thủ bên dưới bóp cò; (b) 박기철 bên ngoài, PTT, một chữ, đúng lúc pháo nổ lần ba. (Hai địa điểm là trong/ngoài cùng một xe — coi là một LOC.)
[SOUND] máy nạp đạn tự động "철컹", pháo, PTT.
박기철: (radio) 넷.

### SC_083 · LOC_007_SALSU (bãi cạn, trung quân) · 수 보병 · WPN_201 · video8s · 11:26–11:34
[ACTION-VI] Trung quân trong nước ngang ngực: cột nước thứ ba bốc lên giữa khối; khiên bị buông trôi, người xô nhau về hai phía, có người chìm dưới người khác; đội hình vuông tan thành đám. Aerial thấp, không cận thương vong.
[SOUND] nổ, nước, hàng nghìn tiếng gào dội, không lệnh.

### SC_084 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001, EQP_002 · video8s · 11:34–11:42
[ACTION-VI] 2-BEAT: (a) 박기철 — PTT — một chữ; máy cận mặt ông, mưa và bùn rung trên mũ lưỡi trai mỗi phát; (b) K2 khai hỏa viên thứ tư; lau quanh xe đã rạp hết, xe lộ ra giữa bãi lau như một khối đá đen.
[SOUND] PTT; pháo; lau khô cháy lép bép quanh nòng.
박기철: (radio) 셋.

### SC_085 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001, EQP_002 · video8s · 11:42–11:50
[ACTION-VI] 2-BEAT: (a) 박기철 — PTT — một chữ; (b) K2 khai hỏa viên thứ năm; máy từ phía sau xe: chớp lửa chiếu sáng cả bãi cạn đầy người trong một nhịp.
[SOUND] PTT; pháo; mưa quay lại ngay sau tiếng dội.
박기철: (radio) 둘.

### SC_086 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, CHAR_001 · VEH_001, EQP_002 · video8s · 11:50–11:58
[ACTION-VI] 2-BEAT: (a) 박기철 — PTT — chữ cuối; (b) trong tháp: mặt 한승우 sáng trắng một nhịp bởi chớp lửa qua thị kính; bộ đếm nhảy "01" → "00"; tay ông rời khỏi thị kính. Máy cận mặt.
[SOUND] PTT; pháo lần sáu; "철컹" của máy nạp không còn gì để nạp; im.
박기철: (radio) 하나.

### SC_087 · LOC_007_SALSU (mô cát giữa sông) · 수 보병, 수 기병 · WPN_201, PROP_021 · video8s · 11:58–12:06
[ACTION-VI] Mô cát giữa sông sau sáu phát: khói xám bay là mặt nước, cát lở, không còn lá cờ nào đứng; ngựa không chủ lội vòng; quanh mô cát, khối trung quân chỉ còn là một biển đầu người và khiên trôi, không hàng lối. Aerial thấp, chậm.
[SOUND] khói xì trong mưa, nước, ngựa hí xa, không lệnh.

### SC_088 · LOC_007_SALSU (hố cối trong lau) · 사수, 탄약수 · WPN_002 · video8s · 12:06–12:14
[ACTION-VI] Hố cối: xạ thủ hô một lệnh, hai khẩu cối bắt đầu bắn liên tiếp — tay thả đạn không nhìn, viên nối viên; ba hàng đạn trên poncho vơi nhanh; đế cối lún thêm vào cát.
[SOUND] "퉁, 퉁, 퉁" dồn dập, đạn cối chạm ống.
사수: 박격포, 여울 목. 서른 발, 전량.

### SC_089 · LOC_007_SALSU (cổng họng bãi) · 수 보병 · WPN_201 · video8s · 12:14–12:22
[ACTION-VI] Cổng họng bãi: đạn cối rơi liên tiếp xuống khe cát và mép nước — cột cát, cột nước nối nhau; những toán tiền quân còn đang leo lên hoặc đứng quanh khe dạt ra hai phía, chạy lên bãi cát bắc; khe trống, đầy hố. Máy từ rìa lau.
[SOUND] ba mươi tiếng nổ nối nhau, cát rơi, gào.

### SC_090 · LOC_007_SALSU (rìa lau, mép nước) · PZF 사수 ×3 · WPN_005 · video8s · 12:22–12:30
[ACTION-VI] Rìa lau sát nước: ba xạ thủ PZF quỳ, ống trên vai, bắn — luồng lửa sau ống thổi lau bay; giữa sông, ba chiếc bè lau chở xe ngựa và hòm gỗ nổ tung, bè lật, ngựa kéo bè giãy trong nước; xạ thủ đổi ống, bắn tiếp — sáu luồng lửa, sáu chiếc bè. Wide từ sau lưng.
[SOUND] PZF "쾅" ×6, bè gỗ vỡ, nước, ngựa.

### SC_091 · LOC_007_SALSU (bờ nam, mép nước) · 수 후군 장수 (신세웅 — tên sử, 1 lần), 고구려 기병, 수 보병 · VEH_101, VEH_207, WPN_101 · video8s · 12:30–12:38
[ACTION-VI] Mép nước bờ nam: kỵ Goguryeo giáp ngựa từ đồi nam và một cánh từ đồi đông lội xuống nước nông, đâm vào hậu quân từ hai phía; 수 후군 장수 (신세웅) trên ngựa giữa hàng khiên vỡ — một mũi giáo dài quét qua, ông ngã khỏi yên xuống nước, mũ tua đỏ trôi. Wide trung, không cận.
[SOUND] vó ngựa trong nước, giáo, khiên vỡ, gào.
N: 우둔위장군 신세웅이 물가에서 죽었습니다. 역사가 이름을 적은 죽음이었습니다. 뒤가 무너졌습니다. 물속의 가운데는 이제 앞도 뒤도 없었습니다.

### SC_092 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001, EQP_002 · video8s · 12:38–12:46
[ACTION-VI] 박기철 tháo tai nghe khỏi đầu, cầm trên tay, nhìn nòng pháo đang bốc khói trắng trong mưa; ông bấm PTT lần cuối, nói ba chữ, rồi để tai nghe rơi xuống bùn cạnh gối.
[SOUND] PTT, mưa, khói xì trên nòng nóng.
N: 스물두 발. 요동성에서 열, 석문령에서 넷, 갈대밭에서 둘, 그리고 오늘 여섯. 넉 달의 산수가 끝났습니다.
박기철: (radio) 다 썼습니다.

### SC_093 · LOC_007_SALSU (bãi lau, K2) · — · VEH_001 · video8s · 12:46–12:54
[ACTION-VI] Cận nòng pháo K2: khói trắng cuộn ra khỏi miệng nòng, mưa rơi lên thép nóng xì thành hơi; bùn trên nòng nứt và rụng từng mảng; qua cửa tháp mở, màn hình bộ đếm: "잔탄 00". Máy tĩnh, đẩy rất chậm.
[SOUND] hơi nước xì, mưa, quạt điện tử.
N: 천둥은 다시 울지 않을 것이었습니다. 이제 이 쇠는 대포가 아니었습니다. 오십오 톤의 무게였습니다. 그것이 무슨 뜻인지는 아직 아무도 몰랐습니다.

### SC_094 · LOC_007_SALSU (bãi cát bắc, đường lên đồi) · CHAR_203, 수 보병 · VEH_207, WPN_201 · video8s · 12:54–13:02
[ACTION-VI] Bãi cát bắc: tiền quân đang đi lên con đường về đồi bắc — hàng người dừng, quay đầu nhìn xuống sông đang bốc khói; 우문술 ghìm ngựa, quay ngựa lại hướng cổng họng; phó tướng gào lệnh; hàng người bắt đầu quay ngược. Wide trung.
[SOUND] lệnh gào, hàng người xoay, giáp, mưa.
N: 가운데 군이 물속에서 죽어 가고 있었습니다. 우문술은 늘 살아 있는 자만 데려가겠다고 했습니다. 살아 있는 자가 물속에 있었습니다.
우문술: 돌아선다! 목을 다시 열어라!

### SC_095 · LOC_007_SALSU (bãi cát bắc) · 수 보병 · WPN_201, PROP_021 · video8s · 13:02–13:10
[ACTION-VI] Aerial thấp: hàng vạn lính tiền quân từ bãi cát bắc đổ ngược về phía cổng họng bãi thành dòng — khiên dựng, giáo hạ, cờ đỏ dồn về khe; dòng người chảy thẳng qua bãi cát về phía bãi lau nơi khói cối còn bốc. Máy theo dòng.
[SOUND] hàng vạn bước chân trên cát, hô, mưa.
N: 오만이 돌아섰습니다. 목을 다시 열기 위해서였습니다. 목은 갈대밭 옆에 있었습니다. 마개 쪽이었습니다.

### SC_096 · LOC_007_SALSU (tuyến bắc bãi lau) · CHAR_002, 사수 · WPN_003, EQP_002 · video8s · 13:10–13:18
[ACTION-VI] Tuyến bắc: 오태민 trong hố nghe 태오 truyền — quay người nhìn ngược qua bãi lau về hướng cổng họng: qua lau thưa, dòng tiền quân Tùy đang đổ ngược về khe; xạ thủ K3 bên cạnh xoay nòng từ hướng bắc sang hướng sông; 오태민 bấm PTT.
[SOUND] giày trên cát ướt, PTT, tiếng dòng quân gần.
N: 적은 이제 강에서 왔습니다. 북쪽 선이 남쪽 선이 되었습니다.
오태민: (radio) 천둥 지휘, 여기는 1소대. 선봉이 돌아옵니다.

### SC_097 · LOC_007_SALSU (hố cối) · 사수 · WPN_002 · video8s · 13:18–13:26
[ACTION-VI] Hố cối: poncho trống, ba mươi ống đạn rỗng lăn trên cát; xạ thủ ngồi thụp, hai tay còn run, ngẩng lên gào về phía K2; khẩu cối nóng bốc hơi dưới mưa.
[SOUND] ống đạn lăn, mưa xì trên nòng, giọng khản.
N: 박격포 서른 발은 일 분 만에 끝났습니다. 넉 달을 아낀 숫자였습니다.
사수: 박격포, 탄 없음!

### SC_098 · LOC_007_SALSU (mô cát giữa sông) · CHAR_202 · PROP_021 · video8s · 13:26–13:34
[ACTION-VI] 우중문 đứng trong nước ngang ngực cạnh mô cát lở, hai tay ôm cán cờ gãy, mảnh lụa đỏ rách quấn quanh cánh tay; quanh ông, lính trung quân trôi qua không nhìn ông; tóc râu bết bùn; ông nhìn về bờ bắc — khói và một khe trống. Máy trung, ngang nước.
[SOUND] nước, tiếng người trôi qua, mưa.
N: 우중문은 깃발 없이 서 있었습니다. 삼십만은 이제 깃발을 보지 않았습니다. 물을 보았습니다. 물은 가슴까지였습니다.
우중문: 깃발… 깃발을 세워라.

### SC_099 · LOC_007_SALSU (chân đồi bắc) · CHAR_205 · VEH_206, EQP_001 · video8s · 13:34–13:42
[ACTION-VI] Chân đồi bắc: 탁발흠 trên ngựa, tay trái giơ trước mặt — sáu ngón đã gấp (một bàn tay nắm, bàn kia gập một ngón); ông giữ bàn tay đó trước mắt, nghe: chỉ mưa và tiếng gào dưới sông, không tiếng pháo. Kỵ binh sau lưng vẫn im.
[SOUND] mưa, gào xa, im — không pháo.
N: 그는 손가락으로 세었습니다. 여섯 번 울렸습니다. 일곱 번째는 오지 않았습니다.

### SC_100 · LOC_007_SALSU (chân đồi bắc) · CHAR_205 · VEH_206, EQP_001 · video8s · 13:42–13:50
[ACTION-VI] Cận 탁발흠: ông hạ bàn tay, nhìn xuống bãi lau xa nơi khói cối tan dần; kính đêm vỡ trên ngực lắc nhẹ theo nhịp ngựa; giọng khô, nói với chính mình nhiều hơn với lính.
[SOUND] mưa, im.
탁발흠: 여섯. …그리고 조용하다.

### SC_101 · LOC_007_SALSU (KB từ đồi bắc) · CHAR_205 (xa), 선비 기병 · VEH_206, WPN_201 · still_kenburns · 13:50–14:00
[ACTION-VI] Ảnh wide từ đồi bắc: bãi cát bắc với dòng tiền quân Tùy đổ ngược về cổng họng bãi, bãi lau bốc khói, sông đầy người; tiền cảnh: hàng kỵ Tiên Ti đứng im trong lau thấp, 탁발흠 phía trước. Ken-burns đẩy từ hàng kỵ qua vai ông xuống bãi lau.
[SOUND] mưa, dòng quân, một nhịp trống xa.
N: 그는 스물두 번을 셀 필요가 없었습니다. 조용해진 것으로 충분했습니다. 넉 달 동안 배운 것이 이 한 번의 침묵을 위한 것이었습니다.

[MID-ROLL 2 · 14:00]

[Kết thúc Phần 5]

## [Phần 6] 한 명도 북으로 — 「한 명도 북으로」 / Liên minh không dễ  (14:00–17:30)
> Tóm tắt VI: 해모루 (radio chết) phi ngựa dọc bờ bắc từ mô cát thượng lưu vào lau, 100 bộ binh giáo dài chạy theo, mang lệnh 을지문덕: giữ cửa bãi, không lùi — "한 명도 북으로 올라오지 못하게 하시오." 오태민: 2.000 kỵ 탁발흠 đang xuống từ đồi bắc — phải lùi; câu hỏi: người của ai chết cho kế của ai. 한승우 quyết: giữ. Gò nam: 을지문덕 thấy bụi kỵ Tiên Ti — không chia quân ("마개는 저들이오. 우리는 물을 치오."). Bãi bắc: 우문술 nhìn lau: "뇌군이다. 저놈들이 여울을 막고 있다. 뚫어라." — tiền quân ép vào rìa nam bãi lau (mini-combat). 오태민: "빈 전차가 뭘 합니까?" 박기철: "오십오 톤입니다." 해모루 ở lại thay vì về gò. 태오: radio 해모루 chết, máy chính 10 %.
> Chức năng: POLITICS (trận tiếp diễn ở nền) · Tài nguyên: radio 10 % · Quyết định sử: 을지문덕 không chia quân; 우문술 "뚫어라"; 해모루 ở lại · Combat: SC_114, SC_121–122 · Open loop: "우문술은 여울을 뚫으라 했습니다. 탁발흠은 북쪽에서 왔습니다. 두 방향에서."
> Sau mid-roll 2: SC_102 nòng K2 bốc khói, mưa rơi lên thép, không thoại.

### SC_102 · LOC_007_SALSU (bãi lau, K2) · — · VEH_001 · video8s · 14:00–14:08
[ACTION-VI] Cận nòng pháo K2 trong mưa: khói mỏng còn rỉ ra khỏi miệng nòng, giọt mưa chạm thép nóng xì thành hơi trắng, lau rạp quanh xe còn cháy âm ỉ vài chỗ; xa xa qua khe lau, dòng tiền quân Tùy đổ về. Không thoại.
[SOUND] mưa xì trên thép, lau cháy lép bép, dòng quân xa.
N: 여섯 발 뒤의 갈대밭은 조용했습니다. 조용한 것은 이쪽뿐이었습니다.

### SC_103 · LOC_007_SALSU (bờ bắc phía đông bãi lau) · CHAR_105, 고구려 보병 · VEH_101 (giáo 삭), EQP_002 · video8s · 14:08–14:16
[ACTION-VI] Tracking: 해모루 phi ngựa hạt dẻ dọc mép nước bờ bắc từ hướng đông, giáp nhẹ ướt, một lông trắng gãy, radio kẹp trên giáp ngực lắc; sau ông, một trăm bộ binh Goguryeo giáo dài 4 m chạy thành hàng trong mưa; đoàn rẽ vào bãi lau qua lối lau rạp. Máy ngang, thấp.
[SOUND] vó ngựa trên cát ướt, giáo chạm nhau, chạy, mưa.
N: 해모루가 왔습니다. 말하는 돌은 사흘 전에 죽었습니다. 말을 타고 왔습니다. 삼백 기는 상류 모래톱에 두고, 창병 백 명만 데려왔습니다.
해모루: 창병, 갈대로 들어가라!

### SC_104 · LOC_007_SALSU (bãi lau, K2) · CHAR_105, CHAR_001 · VEH_001 · video8s · 14:16–14:24
[ACTION-VI] 해모루 nhảy xuống ngựa cạnh K2, ngựa thở dốc; 한승우 tụt từ tháp xuống váy xích rồi xuống đất — hai người đứng đối mặt trong mưa, bùn tới thắt lưng cả hai. 해모루 nói ngay, không chào.
[SOUND] ngựa thở, giày trên xích, mưa.
N: 을지문덕의 명령은 셋이었습니다. 지키라. 물러서지 말라. 그리고 마지막 하나.
해모루: 장군의 명이오. 여울 목을 지키시오. 물러서지 마시오.

### SC_105 · LOC_007_SALSU (bãi lau, K2) · CHAR_105 · — · video8s · 14:24–14:32
[ACTION-VI] Cận 해모루: mặt diều hâu ướt, mắt nhanh nhìn thẳng; ông chỉ tay về cổng họng bãi rồi vòng tay lên hướng bắc — một cử chỉ khép; giọng thấp, rõ.
[SOUND] mưa, giọng.
해모루: 한 명도 북으로 올라오지 못하게 하시오.

### SC_106 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_001 · WPN_003 · video8s · 14:32–14:40
[ACTION-VI] 오태민 chạy tới từ tuyến bắc, K3 trên vai, bùn tới đùi, thở gấp, chỉ ngược tay về đồi bắc; sau lưng anh qua khe lau, trên sườn đồi bắc xa, một vệt tối đang chảy xuống — kỵ binh.
[SOUND] thở gấp, mưa, vó ngựa rất xa như sấm nhỏ.
N: 척후가 먼저 보았습니다. 북쪽 언덕이 움직였습니다. 이천 기. 열흘 전 밤 갈대밭을 야시경으로 본 자의 기병이었습니다.
오태민: 북쪽에서 기병 이천. 탁발흠입니다. 물러나야 합니다.

### SC_107 · LOC_007_SALSU (KB bản đồ, hai mũi tên) · — · PROP_001 · still_kenburns · 14:40–14:50
[ACTION-VI] Ảnh: bản đồ lụa cận bãi lau bờ bắc — hai mũi tên mực đỏ vẽ tay: một từ bãi cát bắc (trên) đâm xuống bãi lau, một từ bãi cạn (dưới) đâm lên cổng họng; bãi lau kẹp giữa như một chiếc lá bị hai ngón tay bóp. Ken-burns đẩy vào bãi lau.
[SOUND] mưa, nhạc trầm.
N: 마개는 병 안에 있어야 했습니다. 이제 병 안에서 오만이 밀어 올리고, 병 밖에서 이천이 내리눌렀습니다. 마개는 양쪽에서 눌렸습니다. 을지문덕의 계획에 그 부분은 없었습니다.

### SC_108 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_001 · — · video8s · 14:50–14:58
[ACTION-VI] 오태민 đứng sát 한승우, giọng không to nhưng gằn; anh không nhìn 해모루 đang đứng cách hai bước — nhìn thẳng 중대장; mưa chảy trên băng bắp tay.
[SOUND] mưa, giọng gằn.
N: 넉 달 동안 한 번도 사라지지 않은 질문이었습니다. 누구의 계획에 누구의 사람이 죽는가. 오태민은 이번에도 물었습니다.
오태민: 장군 계획입니다. 죽는 건 우리 애들입니다.

### SC_109 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_002 · VEH_001 · video8s · 14:58–15:06
[ACTION-VI] 한승우 không trả lời câu hỏi — nhìn 오태민 một nhịp, rồi nhìn cổng họng bãi qua khe lau, rồi nói; tay ông đặt lên xích xe như 박기철 vẫn làm. 오태민 nghe, quai hàm bạnh, không cãi tiếp.
[SOUND] mưa, tay trên thép bùn.
N: 그는 대답하지 않았습니다. 결정만 했습니다. 넉 달 전 요하에서처럼, 짧게.
한승우: 지킨다. 여울 목은 안 내준다.

### SC_110 · LOC_007_SALSU (rìa nam bãi lau) · 천둥 중대, CHAR_106 · PROP_019, PROP_020 · video8s · 15:06–15:14
[ACTION-VI] Insert: lính Hàn kéo bao cát từ hố cối trống sang rìa nam bãi lau hướng cổng họng, đặt thành gờ thấp; 을보 ngồi giữa, thanh sắt trong tay, vót đầu những cây lau to thành cọc nhọn, đóng xiên xuống cát trước gờ. Máy trung, tay và cát.
[SOUND] bao cát, sắt vót lau, mưa.
N: 갈대밭이 양쪽을 향해 돌아앉았습니다. 남쪽에는 모래주머니, 북쪽에는 기관총. 을보 영감은 갈대로 말뚝을 깎았습니다. 쇠가 없으면 갈대라도 쇠였습니다.
을보: 갈대도 깎으면 창이지.

### SC_111 · LOC_007_SALSU (KB gò nam) · CHAR_101, 고구려 부장 · PROP_024 · still_kenburns · 15:14–15:24
[ACTION-VI] Ảnh: gò nam — 을지문덕 đứng dưới cờ đỏ, một phó tướng chỉ tay qua sông về đồi bắc nơi vệt bụi kỵ Tiên Ti đang chảy xuống; 을지문덕 không quay đầu theo tay chỉ — mắt vẫn trên khối trung quân trong nước. Ken-burns từ đồi bắc xa kéo về mặt ông.
[SOUND] mưa, trống, giọng ngoài hình.
N: 남쪽 언덕에서도 그 이천 기가 보였습니다. 부장은 기병을 나누자고 했습니다. 을지문덕은 나누지 않았습니다. 마개가 버티는 동안 물을 치는 것. 그것이 그의 몫이었습니다.
을지문덕: (off) 마개는 저들이오. 우리는 물을 치오.

### SC_112 · LOC_007_SALSU (bãi cát bắc, trên cổng họng) · CHAR_203 · VEH_207, WPN_201 · video8s · 15:24–15:32
[ACTION-VI] 우문술 trên ngựa ở gờ cát trên cổng họng, tiền quân dồn quanh; ông nhìn bãi lau bên trái — khói cối tan, lau rạp lộ một khối đen (K2); mặt ông đổi — lần đầu trong tập. Máy đẩy vào mặt.
[SOUND] mưa, dòng quân, ngựa.
N: 우문술은 갈대밭을 다시 보았습니다. 이번에는 오래 보았습니다. 검은 것이 보였습니다. 넉 달 동안 소문으로만 듣던 것이었습니다.
우문술: 뇌군이다. 저놈들이 여울을 막고 있다.

### SC_113 · LOC_007_SALSU (bãi cát bắc) · CHAR_203, 수 보병 · VEH_207, WPN_201 · video8s · 15:32–15:40
[ACTION-VI] 우문술 rút kiếm, chỉ mũi kiếm về bãi lau — không gào, chỉ nói một chữ; phó tướng gào lại lệnh cho hàng khiên; hàng khiên tiền quân xoay mặt về bãi lau. Low-angle.
[SOUND] kiếm rút, lệnh gào lan, khiên xoay.
N: 우문술은 늘 물러나자고 한 사람이었습니다. 오늘 그는 처음으로 뚫으라고 했습니다. 물러날 길이 갈대밭 옆에 있었기 때문입니다.
우문술: 뚫어라.

### SC_114 · LOC_007_SALSU (bãi cát bắc → rìa nam bãi lau) · 수 보병 · WPN_201, PROP_021 · video8s · 15:40–15:48
[ACTION-VI] Wide: hàng khiên tiền quân Tùy — nghìn người, khiên tròn dựng trước ngực, giáo hạ — bắt đầu tiến ngang bãi cát về phía rìa nam bãi lau và cổng họng; cung thủ Tùy phía sau bắn loạt tên cầu vồng vào bãi lau. Tên cắm xuống lau và bao cát. Máy từ trong lau.
[SOUND] bước chân đồng loạt, tên rít, tên cắm bao cát, mưa.
N: 오만 중 천 명이 먼저 왔습니다. 방패를 세우고, 걸어서. 뇌군을 넉 달 동안 쫓은 군대는 이제 뇌군에게 걸어왔습니다.
수 부장: 방패 앞으로! 걸어라!

### SC_115 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_003 · VEH_001 · video8s · 15:48–15:56
[ACTION-VI] 오태민 quay lại K2, vỗ mạnh vào tấm giáp bùn — bùn rụng; anh nhìn 박기철 đang siết lại lau trên nóc; giọng vừa gằn vừa hỏi thật.
[SOUND] bùn rụng, mưa.
N: 대포 없는 전차. 오태민에게 그것은 쇠로 만든 천막이었습니다.
오태민: 빈 전차가 뭘 합니까?

### SC_116 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, CHAR_002 · VEH_001 · video8s · 15:56–16:04
[ACTION-VI] 박기철 trên nóc xe, ngừng tay, nhìn xuống 오태민; ông đặt bàn tay lên tháp pháo, vỗ hai cái như vỗ cổ ngựa, nói ba chữ không giải thích, rồi tiếp tục siết lau.
[SOUND] tay trên thép, dây thừng, mưa.
N: 박기철은 다르게 세었습니다. 그에게 전차는 대포가 아니었습니다.
박기철: 오십오 톤입니다.

### SC_117 · LOC_007_SALSU (bãi lau, mép đông) · CHAR_105, 고구려 전령 · VEH_101 · video8s · 16:04–16:12
[ACTION-VI] 해모루 kéo một kỵ binh trẻ của mình lại, nắm dây cương ngựa anh ta, chỉ về hướng đông (mô cát thượng lưu) rồi qua sông về gò nam; anh lính gật, quay ngựa phi đi. 해모루 không lên ngựa mình.
[SOUND] cương da, vó ngựa đi xa, mưa.
N: 그는 전령을 보냈습니다. 자신은 가지 않았습니다. 그것은 장군의 명령에 없는 결정이었습니다.
해모루: 너는 장군께 가라. 나는 여기 남는다.

### SC_118 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_105 · VEH_001 · video8s · 16:12–16:20
[ACTION-VI] 한승우 bước tới 해모루 đang cởi bao cung khỏi yên ngựa để mang lên vai; ông nói với giọng kính trọng nhưng rõ là muốn ông ta đi; 해모루 vẫn cởi bao cung.
[SOUND] da yên, cung chạm giáp, mưa.
N: 한승우는 그를 돌려보내려 했습니다. 장군의 부장이 마개와 함께 죽을 이유는 없었습니다.
한승우: 말객님은 언덕으로 돌아가셔야 합니다.

### SC_119 · LOC_007_SALSU (bãi lau, K2) · CHAR_105, CHAR_001 · WPN_101 · video8s · 16:20–16:28
[ACTION-VI] 해모루 đeo cung lên lưng, đứng thẳng đối diện 한승우, đặt tay lên vai ông một cái — cử chỉ Goguryeo ngắn; nói, không cười. 백성민 không có ở đây — ông nhìn về hướng đông một nhịp.
[SOUND] mưa, giáp.
N: 그는 넉 달 동안 이 부대와 걸었습니다. 요하에서 살수까지. 이제 그는 그들 편에 서기로 했습니다.
해모루: 마개는 혼자 서는 게 아니오. 나도 남소.

### SC_120 · LOC_007_SALSU (bãi lau, radio) · CHAR_005 · EQP_002 · video8s · 16:28–16:36
[ACTION-VI] 태오 trong hố, tổ hợp radio trên đùi; cậu nhìn radio chết trên giáp 해모루 (đèn tắt), rồi nhìn màn hình máy mình — vạch pin ngắn hơn lúc sáng; nói không thì thầm nữa — trận đã bắt đầu.
[SOUND] PTT, rè, mưa trên sắt.
N: 무전기 두 대 중 한 대가 죽었습니다. 이 부대의 목소리는 그만큼 남아 있었습니다.
장태오: 말객님 무전기는 죽었습니다. 우린 십 퍼센트.

### SC_121 · LOC_007_SALSU (rìa nam bãi lau) · 사수 ×2, 수 보병 · WPN_003, WPN_201 · video8s · 16:36–16:44
[ACTION-VI] Rìa nam: hàng khiên Tùy đã tới cách gờ bao cát 150 m; hai K3 khai hỏa loạt ngắn — tracer xiên qua mưa, khiên gỗ vỡ, hàng đầu đổ; hàng sau dẫm lên, tiếp tục; xạ thủ đổi dây đạn bằng tay run. Máy từ sau lưng xạ thủ.
[SOUND] K3 loạt ngắn, khiên vỡ, gào, mưa.
N: 백오십 미터. 총이 아직 말을 하는 거리였습니다.
사수: 백오십! 쏜다!

### SC_122 · LOC_007_SALSU (bãi cát trước rìa nam) · 수 보병 · WPN_201 · video8s · 16:44–16:52
[ACTION-VI] Hàng khiên Tùy dừng, lùi về gờ cát cách 200 m, để lại khiên và người trên cát; cung thủ Tùy từ sau gờ bắn loạt tên cao vào bãi lau; tên rơi như mưa thứ hai xuống lau, cắm vào bao cát, vào nóc K2. Wide.
[SOUND] tên rít hàng loạt, cắm lau, cắm thép, mưa.
N: 그들은 물러났습니다. 그리고 화살을 보냈습니다. 화살은 총알보다 느렸지만 셀 수 없이 많았습니다. 총알은 셀 수 있었습니다.

### SC_123 · LOC_007_SALSU (KB sườn đồi bắc) · CHAR_205, 선비 기병 · VEH_206 · still_kenburns · 16:52–17:02
[ACTION-VI] Ảnh: sườn đồi bắc trong mưa — hai nghìn kỵ Tiên Ti đổ xuống bãi cát bắc thành ba dòng dài, giáp da sẫm nước, cung trên lưng, đao trong tay; hàng đầu đã tới rìa bãi cát; cận góc ảnh: tai một con ngựa nhét vải trắng. Ken-burns từ tai ngựa kéo ra toàn dòng.
[SOUND] vó ngựa như sấm gần, mưa.
N: 이천 기가 언덕을 내려왔습니다. 석문령에서 그들은 말의 귀를 막았습니다. 총소리에 놀라지 않는 말이었습니다. 넉 달 동안 배운 것을 그들은 다 가지고 왔습니다.

### SC_124 · LOC_007_SALSU (bãi cát bắc) · CHAR_205 · VEH_206, EQP_001 · video8s · 17:02–17:10
[ACTION-VI] Tracking bên hông: 탁발흠 phi đầu dòng kỵ, mũ lông cáo, bím tóc, kính đêm vỡ đập lên ngực theo nhịp; ông không rút cung — rút đao chuôi vòng; mắt trên bãi lau đang bốc khói trước mặt.
[SOUND] vó ngựa dồn, đao rút, mưa.
N: 그는 활을 꺼내지 않았습니다. 칼을 꺼냈습니다. 오늘은 돌아서 쏘는 날이 아니었습니다.

### SC_125 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · VEH_001, PROP_006 · video8s · 17:10–17:18
[ACTION-VI] 한승우 đứng trên nóc K2 giữa lau rạp, ống nhòm — quay về bắc: dòng kỵ Tiên Ti; quay về nam: hàng khiên Tùy dưới gờ cát và biển người trong nước; ông hạ ống nhòm, hai hướng, một nhịp thở.
[SOUND] mưa, vó ngựa từ bắc, tên rít từ nam.
N: 북쪽에서 이천, 남쪽에서 오만. 가운데에 아흔한 명과 창병 백 명. 그리고 대포 없는 전차 하나.

### SC_126 · LOC_007_SALSU (aerial bãi lau) · — · VEH_206, WPN_201 · still_kenburns · 17:18–17:30
[ACTION-VI] Ảnh aerial: bãi lau bờ bắc như một chiếc lá xanh xám giữa hai gọng kìm — phía bắc, ba dòng kỵ binh đang khép vào; phía nam, hàng khiên đỏ dưới gờ cát và bãi cạn đầy người; giữa lá, một khối đen nhỏ (K2) và những vệt khói. Ken-burns kéo ra rất chậm.
[SOUND] mưa, vó ngựa, trống, nhạc trầm.
N: 우문술은 여울을 뚫으라 했습니다. 탁발흠은 북쪽에서 왔습니다. 두 방향에서.

[Kết thúc Phần 6]

## [Phần 7] 쇠수레가 벙어리가 됐다 — 「쇠수레가 벙어리가 됐다」 / Kẻ địch thích nghi  (17:30–21:00)
> Tóm tắt VI: 탁발흠 (kính đêm vỡ treo cổ): "쇠수레가 벙어리가 됐다. 지금이다." 2.000 kỵ Tiên Ti ngựa bịt tai (3화) xông vào bãi lau từ bắc — K3 không làm ngựa lồng; cận 50 m; tuyến trái 오태민 cong; nòng K3 đỏ; tổ K6 bị tràn — K6 câm (narrator im 18:18–18:50); 을보 hất một kỵ binh bằng thanh sắt; 박기철 xuống xe cầm súng trường; 한승우 bắn hết 15 viên K5 ở 10 m; lái xe K2 trúng tên (cửa mở); 5 lính ngã (91→86). 해모루 + 100 giáo dài dựng tuyến chặn ngựa. Từ phía sông, tiền quân ép cổng họng. 탁발흠 không đánh thẳng vào xe — vòng ra, đợi. 오태민: "탄창 둘 남았습니다."
> Chức năng: THREAT (turning point — địch giáp lá cà quy mô lớn) · Tài nguyên: 91→86 · K6 câm · K5 15→0 · 탄창 넷→둘 · Enemy adaptation: bịt tai ngựa (3화) trả; đếm đạn (P5) trả; đánh lúc câm; không đánh thẳng · Combat: SC_127–147 · Open loop: "왼쪽이 무너지고 있었습니다. 소총 탄창은 둘이 남았습니다." → [MID-ROLL 3 · 21:00].
> [NARRATOR IM LẶNG] 18:18 → 18:50 (SC_133–136).

### SC_127 · LOC_007_SALSU (bãi cát bắc, trước rìa lau) · CHAR_205, 선비 기병 · VEH_206, EQP_001 · video8s · 17:30–17:38
[ACTION-VI] 탁발흠 ghìm ngựa cách rìa bãi lau 300 m, hai nghìn kỵ dàn ngang sau lưng trên bãi cát trong mưa; ông giơ đao chỉ vào bãi lau — chỗ khối đen K2 lộ giữa lau rạp — nói với hàng kỵ, giọng khô, không gào.
[SOUND] mưa, ngựa giậm, giáp da, giọng.
N: 넉 달 동안 그는 쇠수레를 피해 다녔습니다. 오늘 처음으로 그는 쇠수레를 향해 갔습니다.
탁발흠: 쇠수레가 벙어리가 됐다. 지금이다.

### SC_128 · LOC_007_SALSU (bãi cát bắc) · 선비 기병 · VEH_206 · video8s · 17:38–17:46
[ACTION-VI] 2-BEAT: (a) cận tai ngựa Tiên Ti — vải trắng nhét chặt, dây da buộc qua trán; (b) hai nghìn kỵ xuất phát cùng lúc — bùn cát văng, đao giơ, không tiếng hú, chỉ vó ngựa. Tracking thấp theo hàng đầu.
[SOUND] vó ngựa như sấm rền, mưa.

### SC_129 · LOC_007_SALSU (tuyến bắc bãi lau) · 사수 ×2 · WPN_003 · video8s · 17:46–17:54
[ACTION-VI] Tuyến bắc: hai K3 khai hỏa từ hố — tracer quét ngang bãi cát, ngựa hàng đầu ngã, kỵ sĩ văng; nhưng hàng sau không tản, không dựng — nhảy qua ngựa ngã, tiếp tục thẳng; khoảng cách 150 m → 100 m trong shot. Máy từ sau lưng xạ thủ.
[SOUND] K3 quét dài, ngựa ngã, vó không ngừng.
N: 넉 달 전 요하에서 말은 총소리에 미쳤습니다. 오늘 말의 귀에는 천이 있었습니다. 총은 말을 멈추지 못했습니다.
사수: 말이… 말이 안 놀랍니다!

### SC_130 · LOC_007_SALSU (tuyến bắc, rìa lau) · 선비 기병, 천둥 중대 · VEH_206, WPN_001 · video8s · 17:54–18:02
[ACTION-VI] 50 m: kỵ Tiên Ti hàng đầu phi thẳng vào rìa lau — ngựa nhảy qua hố cát, đao chém xuống; tên bắn ở cự ly gần từ trên yên; một lính Hàn trong hố trúng tên vào cổ ngã ngửa (không cận); lính bên cạnh bắn điểm xạ lên bụng ngựa. Máy ngang hố, rung.
[SOUND] ngựa nhảy, đao, tên rít gần, K2C1 điểm xạ, gào.
N: 오십 미터. 쏘는 것보다 맞는 것이 빠른 거리였습니다.

### SC_131 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005 · WPN_001, EQP_002 · video8s · 18:02–18:10
[ACTION-VI] 태오 ngồi trong hố, chân nẹp duỗi thẳng, mũ trụ sắt Goguryeo lệch, K2C1 tì lên miệng hố bắn từng phát vào bóng ngựa lướt qua lau trước mặt; vỏ đạn rơi lên radio; cậu không rời cò.
[SOUND] K2C1 phát một, vỏ đạn rơi lên nhựa, mưa trên sắt.
N: 장태오는 걷지 못했습니다. 쏠 수는 있었습니다. 넉 달 전 그는 하늘을 보는 병사였습니다. 오늘은 땅에서 쏘는 병사였습니다.
장태오: 왼쪽! 왼쪽으로 옵니다!

### SC_132 · LOC_007_SALSU (tuyến trái, tuyến bắc) · CHAR_002 · WPN_003 · video8s · 18:10–18:18
[ACTION-VI] 오태민 đứng thẳng khỏi hố, K3 của người chết kẹp hông, bắn dài vào cụm kỵ đang lách vào lau bên trái; nòng K3 đỏ ửng dưới mưa, hơi bốc; kính bảo hộ trên mũ vỡ văng mất; anh gào không ra chữ. Máy cận nửa người.
[SOUND] K3 dài, nòng xì, gào, ngựa.
N: 왼쪽이 휘었습니다. 오태민은 휘는 쪽으로 갔습니다. 늘 그랬습니다.

[NARRATOR IM LẶNG — 18:18 → 18:50]

### SC_133 · LOC_007_SALSU (góc tuyến bắc, giá K6) · 사수 K6 ×2, 선비 기병 · WPN_004, VEH_206 · video8s · 18:18–18:26
[ACTION-VI] Góc bắc: tổ K6 trên giá ba chân đang bắn — ba kỵ Tiên Ti vòng qua sườn lau, ập vào từ bên hông; đao chém xuống xạ thủ (không cận), giá ba chân đổ nghiêng, nòng K6 chúi xuống cát, dây đạn tuột; ngựa dẫm qua. Không thoại, không narration.
[SOUND] K6 ngắt giữa loạt, giá đổ, ngựa, đao, mưa.

### SC_134 · LOC_007_SALSU (tuyến trái) · 천둥 중대, 선비 기병 · WPN_001, VEH_206 · video8s · 18:26–18:34
[ACTION-VI] Tuyến trái cong: lính Hàn lùi khom qua lau về phía K2, lưỡi lê đã cắm, bắn từng phát ngược lại; kỵ Tiên Ti xuống ngựa đuổi trong lau — cận chiến, đao gặp lưỡi lê, không gore. Tracking lùi theo hàng lính.
[SOUND] lau gãy, đao chạm lưỡi lê, phát một, thở.

### SC_135 · LOC_007_SALSU (bãi lau, gần trạm cứu thương) · CHAR_106, 선비 기병 · PROP_019, VEH_206 · video8s · 18:34–18:42
[ACTION-VI] Một kỵ Tiên Ti phi xuyên lau về phía trạm cứu thương; từ sau bụi lau, 을보 đứng dậy, thanh sắt cầm ngang hai tay, vung một nhát vào ngực kỵ sĩ — người rơi khỏi yên xuống bùn; ngựa chạy tiếp; ông già đứng thở, tạp dề da ướt, mắt trái nheo. Máy trung.
[SOUND] sắt chạm giáp da, người rơi bùn, ngựa, thở già.

### SC_136 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, 천둥 중대 (bị thương) · VEH_001, WPN_001 · video8s · 18:42–18:50
[ACTION-VI] 박기철 tụt khỏi nóc K2, quỳ bên một lính trúng tên đang tựa xích xe, rút khẩu K2C1 khỏi tay anh ta, kéo khóa nòng, bắn từng phát vào bóng đao lướt qua lau cách 20 m; mũ lưỡi trai rơi — ông không nhặt. Máy thấp bên xích.
[SOUND] khóa nòng, phát một, mưa, rên.

### SC_137 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, 선비 기병 · VEH_001, WPN_001 (K5) · video8s · 18:50–18:58
[ACTION-VI] 한승우 đứng dưới đất bên mũi K2 — một kỵ Tiên Ti xuống ngựa lao tới qua lau cách 10 m, đao giơ; ông rút K5 khỏi bao đùi, hai tay, bắn ba phát — người ngã (không cận); người thứ hai từ bên trái — bắn tiếp. Máy cận vai, rung.
[SOUND] K5 đanh từng phát, đao rơi, mưa.
N: 십 미터. 권총의 거리였습니다. 넉 달 동안 한 번도 꺼내지 않은 총이었습니다.

### SC_138 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · WPN_001 (K5) · video8s · 18:58–19:06
[ACTION-VI] Cận hai tay 한승우 cầm K5: bắn — bắn — khóa nòng bật về sau, đứng lại, ổ trống; ông bấm chốt, băng đạn rỗng rơi xuống bùn cạnh giày; ông nhìn khẩu súng rỗng một nhịp rồi nhét vào bao.
[SOUND] hai phát cuối, khóa nòng khóa, băng đạn rơi bùn.
N: 열다섯 발. 박기철이 아침에 센 숫자였습니다. 그 숫자도 이제 영이었습니다.

### SC_139 · LOC_007_SALSU (bãi lau, K2 mũi xe) · 조종수 · VEH_001 · video8s · 19:06–19:14
[ACTION-VI] Cửa lái xe K2 mở — người lái phối thuộc nhô nửa người lên khỏi cửa để nhìn ra bãi lau (kính tiềm vọng đầy bùn); một mũi tên từ trong lau cắm vào vai phải anh — anh gục xuống miệng cửa, tay còn bám mép. Máy trung từ bên hông xe.
[SOUND] tên cắm, thở hắt, thép.
N: 조종수는 밖을 보려고 문을 열었습니다. 잠망경은 진흙에 덮여 있었습니다. 화살은 열린 문을 기다렸습니다.

### SC_140 · LOC_007_SALSU (bãi lau, K2 mũi xe) · CHAR_003, 조종수 · VEH_001 · video8s · 19:14–19:22
[ACTION-VI] 박기철 lao tới, luồn tay dưới nách người lái, kéo anh khỏi cửa xuống đất sau váy xích; cận mũi tên cắm vai phải, máu loang áo; 박기철 gào về phía trạm cứu thương, tay đè lên vết thương. Không cận máu quá mức.
[SOUND] kéo người, gào "의무병!", mưa.
N: 전차를 몰 수 있는 사람은 이제 둘이었습니다. 다친 조종수, 그리고 정비반장.
박기철: 의무병! 조종수 맞았다!

### SC_141 · LOC_007_SALSU (rìa nam bãi lau, cổng họng) · 사수 K3, 수 보병 · WPN_003, WPN_201 · video8s · 19:22–19:30
[ACTION-VI] Rìa nam cùng lúc: hàng khiên tiền quân Tùy lại tiến qua bãi cát về gờ bao cát — gần hơn, 100 m; K3 hướng nam bắn từng loạt ngắn, dây đạn còn một đoạn; khiên đổ, khiên khác lấp vào. Máy từ hố.
[SOUND] K3 ngắn, khiên, bước chân đồng loạt, tên.
N: 남쪽도 왔습니다. 방패는 총알을 막지 못했습니다. 그러나 방패는 많았고 총알은 적었습니다.
사수: 남쪽도 옵니다! 백 미터!

### SC_142 · LOC_007_SALSU (rìa bắc bãi lau) · CHAR_105, 고구려 보병 · VEH_101 (giáo 삭 của 개마무사), VEH_206 · video8s · 19:30–19:38
[ACTION-VI] Rìa bắc: 해모루 gào một lệnh Goguryeo — một trăm bộ binh Goguryeo từ trong lau bước lên thành hàng, giáo dài 4 m hạ ngang, đuôi giáo cắm cát; kỵ Tiên Ti lao tới — ngựa dựng trước rừng mũi giáo, quay ngang; hàng giáo bước tới một bước. Wide trung.
[SOUND] lệnh Goguryeo, giáo cắm cát, ngựa dựng, đao chạm giáo.
N: 창은 천 년 동안 말을 세워 왔습니다. 총이 못 세운 말을 창이 세웠습니다. 창병 백 명이 이천 기 앞에 섰습니다.
해모루: 창, 앞으로!

### SC_143 · LOC_007_SALSU (tuyến trái) · CHAR_002, 사수 · WPN_003 · video8s · 19:38–19:46
[ACTION-VI] 오태민 quỳ sau bụi lau, K3 mở nắp — xạ thủ bên cạnh đưa dây đạn cuối cùng từ hộp thiếc rỗng; 오태민 lắp, đóng nắp, nhìn hộp rỗng, đá nó sang bên. Máy cận tay.
[SOUND] nắp K3, dây đạn, hộp thiếc rỗng lăn.
N: 삼백 발씩 여섯 정. 아침의 숫자였습니다. 오태민의 총에는 마지막 띠가 걸렸습니다.

### SC_144 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005 · EQP_002 · video8s · 19:46–19:54
[ACTION-VI] 태오 buông súng, vớ tổ hợp radio dính bùn, bấm PTT, gào qua tiếng đao ngựa; mũ trụ sắt tụt xuống lông mày.
[SOUND] PTT, gào, ngựa, mưa.
N: 상류 모래톱의 삼백 기는 아직 움직이지 않았습니다. 한승우가 부르지 않았기 때문입니다.
장태오: (radio) 수색, 여기는 천둥 지휘. 대기. 아직입니다.

### SC_145 · LOC_007_SALSU (mô cát thượng lưu) · CHAR_006, 고구려 부장 · VEH_101, EQP_002 · video8s · 19:54–20:02
[ACTION-VI] Mô cát thượng lưu: 300 kỵ Goguryeo đã lên yên, giáo dựng, ngựa giậm; phó tướng Goguryeo nhìn 백성민 chờ; 백성민 trên ngựa nghe radio, mắt về phía tây nơi khói bốc trên bãi lau, hạ radio, lắc đầu một cái.
[SOUND] radio rè, ngựa giậm, mưa, súng xa.
N: 백성민은 기다렸습니다. 기다리는 것은 그가 가장 잘하는 일이었습니다.
백성민: 아직입니다. 기다립니다.

### SC_146 · LOC_007_SALSU (tuyến trái, trong lau) · CHAR_205, 천둥 중대 · VEH_206, EQP_001 · video8s · 20:02–20:10
[ACTION-VI] 탁발흠 xuống ngựa trong lau, mũ lông cáo mất, bím tóc xổ, bùn tới đùi, đao dính máu; ông chém một lính Hàn đang lùi (không cận), rồi dừng — nhìn qua lau về K2: cửa đóng, im, tên cắm đầy nóc. Máy cận mặt ông — bình tĩnh dữ.
[SOUND] đao, lau gãy, thở, im nhìn.
N: 그는 이제 검은 소에서 오십 미터에 있었습니다. 넉 달 만에 가장 가까운 거리였습니다. 그는 서두르지 않았습니다.

### SC_147 · LOC_007_SALSU (tuyến trái, rìa lau) · CHAR_205, 선비 기병 · VEH_206 · video8s · 20:10–20:18
[ACTION-VI] 탁발흠 huýt sáo hai tiếng sắc; kỵ Tiên Ti trong lau lùi ra bãi cát, lên ngựa, tản rộng thành hình quạt ngoài tầm lưỡi lê — không rút hẳn, không xông; hàng giáo Goguryeo và tuyến Hàn thở dốc nhìn theo. Wide trung.
[SOUND] huýt sáo, vó ngựa lùi, mưa, thở.
N: 그는 직진하지 않았습니다. 선비족은 직진하는 법이 없었습니다. 그는 갈대밭이 스스로 비기를 기다렸습니다. 총알이 마르는 것을 그는 넉 달 동안 보았습니다.

### SC_148 · LOC_007_SALSU (bãi lau, giữa) · CHAR_004, 천둥 중대 (thương vong) · PROP_009 · video8s · 20:18–20:26
[ACTION-VI] Bãi lau sau đợt xung phong: năm hình người nằm trong lau rạp, hai đã được phủ poncho, ba đang được kéo về trạm; 서아 bò tới người gần nhất, mũ đội, bím tóc ướt, băng chữ thập rách; mưa. Máy tracking chậm qua từng người, không cận mặt người chết.
[SOUND] mưa, rên, lau, gọi nhỏ "여기!".
N: 다섯이 쓰러졌습니다. 아흔하나에서 여든여섯이었습니다. 화살이었습니다. 방탄복은 가슴만 가렸습니다. 넉 달 전 요하에서 배운 것을 살수가 다시 가르쳤습니다.

### SC_149 · LOC_007_SALSU (trạm cứu thương) · CHAR_004, CHAR_107, 천둥 중대 (bị thương) · PROP_009 · video8s · 20:26–20:34
[ACTION-VI] 서아 quỳ bên lính trúng tên vào đùi, hai tay siết garô, máu tới khuỷu; 아리 đè hai chân anh ta, mặt ngoảnh đi; túi quân y mở — tám ống morphine vẫn nguyên trong ngăn; 서아 nói với người bị thương, giọng dứt khoát.
[SOUND] garô siết, rên, mưa trên lau.
N: 모르핀 여덟. 서아는 아직 하나도 꺼내지 않았습니다. 여덟은 오늘 밤을 위한 숫자였습니다.
윤서아: 모르핀 아낍니다. 참으십시오.

### SC_150 · LOC_007_SALSU (tuyến trái) · CHAR_002 · WPN_001 · video8s · 20:34–20:42
[ACTION-VI] 오태민 đứng dựa lau, tay sờ các túi băng đạn trên áo giáp — túi, túi, túi rỗng, hai băng còn; anh rút ra cầm hai băng trên tay, nhìn về phía K2 nơi 한승우 đứng, giơ hai băng lên. Máy cận tay rồi mặt.
[SOUND] vải túi, băng đạn chạm nhau, mưa.
N: 한 번의 돌격이었습니다.
오태민: 탄창 둘 남았습니다.

### SC_151 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · WPN_001 · video8s · 20:42–20:50
[ACTION-VI] Cận 한승우: tay phải cài nắp bao súng K5 rỗng; tay trái cúi nhặt khẩu K2C1 của người lính bị thương tựa xích xe, kéo khóa nòng — có đạn; ông ngước nhìn hai băng 오태민 giơ, gật. Mưa trên mũ.
[SOUND] khóa nòng, bao súng, mưa.
N: 지휘관은 권총이 없었습니다. 부하의 소총을 들었습니다. 그 소총에는 탄창이 하나였습니다. 나머지는 이미 나뉘어 있었습니다.

### SC_152 · LOC_007_SALSU (aerial bãi lau) · — · VEH_206, WPN_201, VEH_001 · still_kenburns · 20:50–21:00
[ACTION-VI] Ảnh aerial: bãi lau bị ép — cánh trái (tây-bắc) lau rạp thành vệt lớn, kỵ Tiên Ti dàn hình quạt ngoài rìa; phía nam, hàng khiên đỏ dưới gờ cát; giữa lau, K2 đen tên cắm như lông nhím, khói mỏng; mưa. Ken-burns đẩy chậm vào cánh trái.
[SOUND] mưa, ngựa, trống xa, nhạc trầm.
N: 왼쪽이 무너지고 있었습니다. 소총 탄창은 둘이 남았습니다.

[MID-ROLL 3 · 21:00]

[Kết thúc Phần 7]

## [Phần 8] 마개는 우리다 — 「마개는 우리다」 / Tài nguyên bắt đầu cạn  (21:00–24:00)
> Tóm tắt VI: "마지막 탄창" chuyền tay — lính chia đạn từ băng này sang băng kia. Kính đêm vô dụng ban ngày. 태오: "무전기 오 퍼센트." Thứ cuối cùng: động cơ K2 — 20 km dầu, 55 tấn, 0 viên. 오태민: đưa K2 lên mô cát làm lô cốt. Không ai nói "chạy". 박기철: "연료 이십 킬로. 여울까지 삼백 미터. 남는 건 다 태워도 됩니다." 한승우 nhìn cổng họng: tiền quân dồn trên gờ, trung quân chìm dưới — tay chạm lựu đạn nhiệt nhôm (3화): "전차를 여울에 박는다. 마개는 우리다." — nút chai theo nghĩa đen, không để "천둥" rơi vào tay 탁발흠. 박기철 (lái xe bị thương): "제가 몹니다. 십 년 몰았습니다." — tháo biển 천둥 3 khỏi ba lô, bỏ túi ngực. 오태민: "북안은 제가 맡습니다. 한 명도 못 건넙니다." 을보: "쇠는 물에 가라앉지. 그게 쇠야."
> Chức năng: DECISION · Tài nguyên nói thành lời: "탄창 둘" · "무전기 오 퍼센트" · "이십 킬로 / 삼백 미터" · Quyết định cuối của 한승우 (outline/decisions P-03) · Payoff: lựu đạn 3화 · "55톤" P6 · nút bầu P2 · Mini-combat: SC_169 (v2: dời vào giữa SC_164 và SC_165 — K3 nam tắt giữa lúc quyết định; giữ ID) · Open loop: "그는 전차를 버리기로 했습니다. 버리는 방법이 문제였습니다."
> Sau mid-roll 3: SC_153 cận băng đạn rỗng rơi xuống bùn, không thoại.

### SC_153 · LOC_007_SALSU (bãi lau, tuyến trái) · — · WPN_001 · video8s · 21:00–21:08
[ACTION-VI] Cận sát đất: một băng đạn K2C1 rỗng rơi từ trên xuống, cắm nghiêng vào bùn cạnh ba băng rỗng khác; mưa gõ lên nhôm; một bàn tay bùn vào khung nhặt lên, lắc — rỗng — thả lại. Không thoại.
[SOUND] băng đạn rơi bùn, mưa gõ nhôm, tay.
N: 탄창은 비면 쇳조각이었습니다. 이 시대의 쇳조각이었습니다.

### SC_154 · LOC_007_SALSU (bãi lau, tuyến trái) · 천둥 중대 ×2 · WPN_001 · video8s · 21:08–21:16
[ACTION-VI] Hai lính quỳ đối diện trong lau: một người tháo từng viên khỏi băng của mình bằng ngón cái, đếm, đưa cho người kia nhét vào băng gần rỗng; người kia đếm lại bằng môi; băng đầy trả về; hai người gật nhau. Máy cận hai đôi tay.
[SOUND] viên đạn "딸깍" vào băng, mưa, đếm thì thầm.
N: 마지막 탄창은 나누는 것이었습니다. 서른 발이 두 사람의 열다섯 발이 되었습니다. 아무도 명령하지 않았습니다. 넉 달 동안 이렇게 살았습니다.
병사: 열다섯. 너도 열다섯.

### SC_155 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005 · EQP_002 · video8s · 21:16–21:24
[ACTION-VI] 태오 lau bùn khỏi màn hình radio bằng ngón cái — vạch pin chỉ còn một chấm; cậu nhìn về K2, nói to đủ nghe, không qua radio.
[SOUND] mưa trên sắt mũ, rè.
N: 말 몇 마디의 값이었습니다. 이 부대의 21세기는 그만큼 남았습니다.
장태오: 무전기 오 퍼센트.

### SC_156 · LOC_007_SALSU (bãi lau, tuyến trái) · CHAR_003 · EQP_001 · video8s · 21:24–21:32
[ACTION-VI] 박기철 (không mũ, tóc muối tiêu ướt) nhặt chiếc kính nhìn đêm gãy mount từ mũ một lính đã phủ poncho; bật — không sáng; ông giơ lên trời mưa xám, nhìn qua — đen; đặt lại lên poncho, không ném. Máy cận.
[SOUND] công tắc nhựa, mưa.
N: 야시경 열 개. 낮에는 장님이었고 밤에는 건전지가 없었습니다. 그것은 이제 유리와 플라스틱이었습니다.

### SC_157 · LOC_007_SALSU (KB K2 dưới lau) · — · VEH_001 · still_kenburns · 21:32–21:42
[ACTION-VI] Ảnh: K2 giữa bãi lau rạp trong mưa — tên cắm đầy nóc và giá đồ như lông nhím, bùn nứt trên tháp, nòng pháo hạ thấp, cửa lái xe còn mở với vệt máu trên mép; xe to, đen, im. Ken-burns đẩy rất chậm từ toàn xe vào cửa lái.
[SOUND] mưa, im.
N: 남은 것은 하나였습니다. 엔진. 기름 이십 킬로, 무게 오십오 톤, 포탄 영. 넉 달 동안 이 쇠는 대포였습니다. 오늘 오후 이 쇠는 그냥 쇠였습니다. 그 쇠로 무엇을 할지가 이 부대의 마지막 결정이었습니다.

### SC_158 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_001 · VEH_001 · video8s · 21:42–21:50
[ACTION-VI] 오태민 quỳ bên K2 với 한승우 và 박기철 dưới tấm giáp bùn — ba cái mũ (một mũ lưỡi trai mất) chụm; 오태민 chỉ tay về mô cát nhỏ cạnh cổng họng cách 300 m, rồi vẽ một vòng tròn trên cát.
[SOUND] mưa, cát, ngựa xa.
N: 첫 번째 안은 오태민의 것이었습니다. 도망치자는 말은 아무도 하지 않았습니다. 도망칠 곳이 없었기 때문만은 아니었습니다.
오태민: 전차를 모래톱에 올립니다. 토치카로 씁니다.

### SC_159 · LOC_007_SALSU (bãi lau, K2) · CHAR_003 · VEH_001 · video8s · 21:50–21:58
[ACTION-VI] 박기철 gõ ngón tay lên váy xích như gõ bình xăng, nói chậm, ngắt nhịp, lặp số như thói quen; mắt ông nhìn cổng họng qua khe lau rồi nhìn 한승우.
[SOUND] ngón tay gõ thép, mưa.
N: 박기철은 기름부터 말했습니다. 늘 그랬습니다. 그는 한 번만 말했습니다.
박기철: 연료 이십 킬로. 여울까지 삼백 미터. 남는 건 다 태워도 됩니다.

### SC_160 · LOC_007_SALSU (bãi lau, K2 — nhìn ra cổng họng) · CHAR_001 · PROP_006 · video8s · 21:58–22:06
[ACTION-VI] 한승우 đứng dậy, ống nhòm qua khe lau: cổng họng bãi — trên gờ cát, tiền quân Tùy dồn dày đặc chờ lệnh; dưới khe, nước ngang ngực đầy trung quân đang cố bò lên; khe rộng 60 m giữa hai khối ấy còn trống. Ông hạ ống nhòm, nhìn K2, nhìn lại khe. Máy theo mắt.
[SOUND] mưa, gào từ sông, dòng quân trên gờ.
N: 목은 육십 걸음이었습니다. 위에는 오만이 내려오려 했고, 아래에는 십만이 올라오려 했습니다. 그 사이를 막을 것이 하나 있었습니다. 오십오 톤의 쇠.

### SC_161 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · PROP_025 (소이수류탄 — lựu đạn nhiệt nhôm) · video8s · 22:06–22:14
[ACTION-VI] Cận tay 한승우 mở túi ngực áo giáp: quả lựu đạn nhiệt nhôm xám (nhãn mờ) ông đã cầm ở Liêu Đông thành đêm bỏ xe (3화) — nằm cạnh cái nút bầu gỗ và mũi tên cũ; ngón tay ông chạm vào ba thứ theo thứ tự, dừng ở quả lựu đạn.
[SOUND] khóa túi, mưa, thở.
N: 한 달 전 요동성 골짜기에서 그는 이 수류탄을 들고 서 있었습니다. 천둥 3호 앞에서. 그는 던지지 못했습니다. 두 번 실수하지 않을 것이었습니다.

### SC_162 · LOC_007_SALSU (bãi lau, K2) · CHAR_105, CHAR_001 · VEH_001 · video8s · 22:14–22:22
[ACTION-VI] 해모루 đứng bên, cung trên lưng, theo dõi tay 한승우 trên quả lựu đạn rồi nhìn K2; ông là người Goguryeo duy nhất từng thấy ông này đốt xe của mình; hỏi thẳng, không ngạc nhiên.
[SOUND] mưa, giáp.
N: 해모루는 요동성 골짜기에서 장갑차가 타는 것을 보았습니다. 그는 이 사람이 무엇을 하려는지 먼저 알았습니다.
해모루: 쇠수레를 버리려는 것이오?

### SC_163 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · VEH_001 · video8s · 22:22–22:30
[ACTION-VI] 한승우 đóng túi ngực, đặt bàn tay lên tấm giáp mũi K2, nhìn thẳng cổng họng bãi qua khe lau — nói không cao giọng, rõ từng chữ; sau lưng ông, 오태민 và 박기철 nghe.
[SOUND] mưa, tay trên thép, im.
한승우: 전차를 여울에 박는다. 마개는 우리다.

### SC_164 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_003 · VEH_001 · video8s · 22:30–22:38
[ACTION-VI] 오태민 há miệng — không ra chữ; anh nhìn K2 từ mũi tới đuôi như nhìn một người; 박기철 bên cạnh gật chậm một cái, rồi gật cái nữa — người đã hiểu từ lúc nói "오십오 톤". Máy hai mặt.
[SOUND] mưa, im, ngựa xa.
N: 오십오 톤을 목에 박으면 오만은 내려오지 못하고 십만은 올라오지 못했습니다. 그리고 천둥은 탁발흠의 손에 들어가지 않았습니다. 네 번째 결정이었습니다.
오태민: …전차를요?

### SC_169 · LOC_007_SALSU (rìa nam bãi lau) · 사수 K3, 수 보병 · WPN_003, WPN_201 · video8s · 22:38–22:46
[ACTION-VI] Rìa nam: hàng khiên Tùy lại thử — chạy khom qua bãi cát về gờ bao cát; K3 hướng nam bắn loạt cuối — dây đạn hết giữa loạt, xạ thủ mở nắp: trống; khiên Tùy dừng ở 80 m, chần chừ, rồi lùi vì hàng giáo Goguryeo bước ra bên cạnh K3. Máy từ hố.
[SOUND] K3 ngắt, nắp mở, hô Goguryeo, khiên lùi.
N: 남쪽 기관총이 마지막 띠를 다 썼습니다. 방패는 팔십 미터에서 멈췄습니다. 총이 아니라 창 때문이었습니다.

### SC_165 · LOC_007_SALSU (KB nút bầu) · CHAR_001 (tay) · — · still_kenburns · 22:46–22:56
[ACTION-VI] Ảnh cận: lòng bàn tay găng bùn của 한승우 mở ra — cái nút gỗ nhỏ, sứt, đen nước, nằm giữa lòng tay; sau bàn tay, mờ, khối K2. Ken-burns đẩy rất chậm vào cái nút.
[SOUND] mưa, nhạc trầm.
N: 병이 아무리 커도 마개가 막으면 못 나온다. 해모루가 간밤에 한 말이었습니다. 마개는 작아야 했습니다. 마개는 병 안에 들어가야 했습니다. 그리고 마개는 병에서 나오지 않는 법이었습니다.

### SC_166 · LOC_007_SALSU (bãi lau, K2) · CHAR_003, CHAR_001 · VEH_001 · video8s · 22:56–23:04
[ACTION-VI] 박기철 đứng dậy khỏi chỗ ngồi, không nhìn ai, nhìn cửa lái xe còn mở có vệt máu; nói hai câu ngắn, giọng khàn, lặp số theo thói quen; rồi nhìn 한승우.
[SOUND] mưa, giọng khàn.
N: 조종수는 화살에 맞았습니다. 전차를 몰 수 있는 사람은 하나 남았습니다.
박기철: 제가 몹니다. 십 년 몰았습니다.

### SC_167 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_003 · VEH_001 · video8s · 23:04–23:12
[ACTION-VI] 한승우 nhìn 박기철 một lúc lâu hơn mọi lần trong tập — rồi gật một cái; 박기철 gật lại; không bắt tay. Máy hai mặt, mưa giữa hai người.
[SOUND] mưa, im.
N: 넉 달 동안 이 쇠를 살려 온 사람이었습니다. 기름을 세고, 축을 갈고, 진흙을 발랐습니다. 이 쇠를 묻는 일도 그의 몫이었습니다. 그것이 옳았습니다.

### SC_168 · LOC_007_SALSU (bãi lau, K2 mũi xe) · CHAR_003 · VEH_001, PROP_023 · video8s · 23:12–23:20
[ACTION-VI] 박기철 tháo ba lô, cởi dây dù buộc tấm biển thép nhỏ PROP_023 (chỉ số "3" sơn trắng trầy, mép cháy sém — không vẽ chữ Hangul, overlay ở edit nếu cần) khỏi ba lô, lau bùn bằng ngón cái, nhét vào túi ngực áo giáp; rồi bám mép cửa lái xe, trèo lên. Cận tay và biển tên.
[SOUND] dây dù, thép nhỏ, mưa, giày trên xích.
N: 요동성 골짜기에서 그는 이 이름표를 떼어 왔습니다. 두고 온 장갑차의 것이었습니다. 그는 한 달 동안 그것을 등에 지고 다녔습니다. 오늘은 가슴에 넣었습니다.

### SC_170 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_001 · WPN_003 · video8s · 23:20–23:28
[ACTION-VI] 오태민 đứng thẳng trước 한승우, K3 người chết trên vai, hai băng đạn cuối trong túi ngực; anh không xin đi cùng xe — nói câu của tuyến bắc, giọng thấp lần đầu trong series.
[SOUND] mưa, giáp.
N: 넉 달 전 요하에서 그는 전차를 내보내자고 했습니다. 오늘 그는 전차를 보내는 쪽에 섰습니다.
오태민: 북안은 제가 맡습니다. 한 명도 못 건넙니다.

### SC_171 · LOC_007_SALSU (trạm cứu thương) · CHAR_004, CHAR_107, 마을 여인 · PROP_009, PROP_020 · video8s · 23:28–23:36
[ACTION-VI] Trạm cứu thương: 서아 ra hiệu bằng tay — hai phụ nữ làng nâng hai đầu chiếu lau có thương binh; 아리 ôm túi quân y trước ngực; đoàn chuyển sâu về phía tây bãi lau, xa cổng họng; 서아 đi cuối, ngoái nhìn K2. Máy tracking.
[SOUND] chiếu lau, rên, mưa, bước chân.
N: 의무실이 움직였습니다. 전차가 갈 길에서 먼 쪽으로. 스무 명의 부상자와 여덟 개의 모르핀이 갈대 위에서 옮겨졌습니다.
윤서아: 서쪽으로. 전차에서 먼 쪽으로.

### SC_172 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005, 고구려 전령 · EQP_002, VEH_101 · video8s · 23:36–23:44
[ACTION-VI] 태오 bấm PTT gọi — rè — gọi lại — rè; cậu buông tổ hợp, ngẩng nhìn một kỵ binh Goguryeo trẻ (người 해모루 giữ lại) đang ngồi trên ngựa cạnh hố chờ lệnh; hai người trẻ nhìn nhau qua mưa — một mũ trụ sắt, một chỏm lông đỏ.
[SOUND] PTT, rè dài, ngựa thở.
N: 무전기는 대답하지 않았습니다. 말 탄 전령은 대답했습니다. 천사백 년 전의 통신이 다시 유일한 통신이 되었습니다.
장태오: 장군께… 마개가 내려간다고 전해 주십시오.

### SC_173 · LOC_007_SALSU (bãi lau, K2) · CHAR_106 · VEH_001 · video8s · 23:44–23:52
[ACTION-VI] 을보 đi tới K2, tạp dề da ướt, thanh sắt cắm xuống cát bên chân; ông đặt hai bàn tay lên tấm giáp mũi xe, vuốt như vuốt cổ ngựa — như ngày đầu ở Liêu Đông; nheo mắt trái, nói với cái xe hơn với người.
[SOUND] tay trên thép bùn, mưa.
N: 대장장이는 쇠에게 인사했습니다. 넉 달 전 요하에서 처음 만진 쇠와 같은 쇠였습니다. 그는 쇠가 어디로 가는지 알았습니다.
을보: 쇠는 물에 가라앉지. 그게 쇠야.

### SC_174 · LOC_007_SALSU (bãi lau, K2 — wide) · CHAR_003 (trong cửa lái) · VEH_001 · still_kenburns · 23:52–24:00
[ACTION-VI] Ảnh wide: K2 giữa bãi lau rạp, tên cắm nóc, mưa; cửa lái xe mở — nửa đầu 박기철 trong đó, tóc muối tiêu ướt; quanh xe, lính Hàn và bộ binh Goguryeo quỳ trong lau, ai cũng nhìn xe. Ken-burns đẩy chậm vào cửa lái.
[SOUND] mưa, im, ngựa xa.
N: 그는 전차를 버리기로 했습니다. 버리는 방법이 문제였습니다.

[Kết thúc Phần 8]

## [Phần 9] 300미터 — 「300미터」 / Kế hoạch lớn  (24:00–27:30)
> Tóm tắt VI: Kế cuối vẽ trên cát (radio 5 % → chết → cờ tay + 나각 해모루): (1) 박기철 lái K2 từ lau 300 m ra cổng họng bãi, 한승우 trong tháp với lựu đạn; (2) 백성민 dẫn 300 kỵ 해모루 qua mô cát thượng lưu đánh lưng 탁발흠 — lệnh cuối qua radio trước khi máy chết; (3) 오태민 giữ tuyến bắc với băng cuối + K3 cuối + 100 giáo dài Goguryeo (해모루 để lại; "창은 말을 세우오. 그대들 쇠는 사람을 세우시오."); 박기철 nói giới hạn lội của K2 ("도하 준비 없이 일 점 이 미터"); (4) 서아 dời trạm; (5) 태오 — không đi được — hố chiến đấu với súng và radio chết; kỵ Goguryeo mang tin tới gò: 을지문덕 quyết "쇠수레가 목을 막으면 우리는 꼬리를 치오. 전군." Nước ngang ngực — Tùy không chạy nổi [史]; 우중문: "물이… 물이 왜 이렇게 빠른가." Vai K2: chặn lối lên bãi bắc để tiền quân không xuống, trung quân không lên.
> Chức năng: PLAN · Tài nguyên: radio 5 % → chết (cờ tay/나각 — không còn hiện đại); "K3 탄 떨어졌습니다" · Quyết định sử: 을지문덕 lệnh toàn quân đánh đuôi khi nút chai xuống · Mini-combat: SC_190 · Open loop: "300미터. 전차가 마지막으로 달릴 거리였습니다." → [MID-ROLL 4 · 27:30].

### SC_175 · LOC_007_SALSU (bãi lau, K2) · CHAR_001, CHAR_105, CHAR_002, CHAR_003 · VEH_001 · video8s · 24:00–24:08
[ACTION-VI] 한승우 quỳ, vạch lên cát ướt bằng một cán tên gãy: một vệt dài (bãi lau), một khe (cổng họng), một ô vuông nhỏ (K2) kéo từ vệt tới khe; 해모루, 오태민, 박기철 quỳ quanh; ông chọc cán tên vào khe.
[SOUND] cán tên cào cát, mưa, giọng thấp.
N: 계획은 모래 위에 그려졌습니다. 지도도, 화면도 없었습니다. 삼백 미터, 목, 쇠. 세 개의 선이었습니다.
한승우: 박 상사, 삼백 미터. 여울 목에 세운다.

### SC_176 · LOC_007_SALSU (KB sơ đồ trên cát) · — · — · still_kenburns · 24:08–24:18
[ACTION-VI] Ảnh cận từ trên xuống: sơ đồ vạch trên cát ướt — vệt lau, khe cổng họng, ô K2 với mũi tên tới khe; phía đông vệt lau, một đường vòng (mô cát thượng lưu) với mũi tên cong đâm vào lưng một hàng chấm (kỵ Tiên Ti); phía bắc vệt lau, một hàng vạch ngắn (giáo). Ken-burns từ ô K2 theo mũi tên tới khe rồi lên đường vòng.
[SOUND] mưa, nhạc trầm.
N: 다섯 가지였습니다. 전차는 목으로. 삼백 기는 상류 모래톱을 돌아 탁발흠의 등으로. 오태민은 창병 백 명과 북쪽에. 의무실은 서쪽 갈대로. 장군에게는 말 탄 전령 하나. 여든여섯 명의 계획은 쉰다섯 살 노인의 계획 안에 있었습니다. 계획은 강 안에 있었습니다.

### SC_177 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005 · EQP_002 · video8s · 24:18–24:26
[ACTION-VI] 태오 bấm PTT, nói rõ từng chữ — lệnh cuối cùng 한승우 giao cho radio; tay kia che mic khỏi mưa; mũ trụ sắt đẩy lên trán.
[SOUND] PTT, mưa trên sắt, giọng rõ.
N: 마지막 오 퍼센트는 한 문장을 위해 남겨 두었습니다. 상류 모래톱으로 가는 문장이었습니다.
장태오: (radio) 수색, 여기는 천둥 지휘. 모래톱 길로. 탁발흠 뒤를 치십시오.

### SC_178 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005 · EQP_002 · video8s · 24:26–24:34
[ACTION-VI] Cận màn hình radio: vạch pin cuối nhấp nháy, rồi màn hình tối; đèn LED tắt; 태오 bấm PTT — không tiếng rè nữa, chỉ tiếng mưa; cậu đặt tổ hợp xuống bùn, không nhìn nó nữa.
[SOUND] LED "틱", im — chỉ mưa.
N: 무전기가 죽었습니다. 요하에서 살수까지 넉 달을 산 기계였습니다. 이 부대의 마지막 21세기가 진흙 위에 놓였습니다. 대답은 듣지 못했습니다.

### SC_179 · LOC_007_SALSU (mô cát thượng lưu) · CHAR_006, 고구려 부장 · VEH_101, EQP_002 · video8s · 24:34–24:42
[ACTION-VI] 백성민 trên ngựa, radio áp tai: câu lệnh tới — cậu đáp "알겠—" và máy rè rồi câm; cậu nhìn radio một nhịp, nhét vào áo giáp, quay sang phó tướng Goguryeo, giơ tay chỉ dải mô cát; phó tướng gật, nâng tù và nhỏ.
[SOUND] rè, im, tù và nhỏ một hồi, ngựa giậm.
N: 백성민은 대답을 끝내지 못했습니다. 대답은 필요 없었습니다. 명령은 들었습니다.
백성민: 모래톱 길로 갑니다. 지금.

### SC_180 · LOC_007_SALSU (bãi lau, K2) · CHAR_105, CHAR_001 · PROP_018, PROP_012 (cờ hiệu nhỏ) · video8s · 24:42–24:50
[ACTION-VI] 해모루 tháo tù và sừng đen khỏi hông, vỗ lên nó; rồi rút lá cờ hiệu nhỏ 삼족오 sau lưng đưa cho 한승우; giải thích bằng ngón tay: một, hai; 한승우 nhận cờ, cắm vào dây áo giáp.
[SOUND] sừng chạm giáp, cờ nhỏ, mưa.
N: 무전기 대신 나각과 깃발이었습니다. 이 부대는 이제 612년의 방식으로 말했습니다.
해모루: 나각 한 번은 가고, 두 번은 서는 것이오.

### SC_181 · LOC_007_SALSU (tuyến bắc) · CHAR_002, 고구려 보병, 천둥 중대 · VEH_101 (giáo 삭 của 개마무사), WPN_001 · video8s · 24:50–24:58
[ACTION-VI] Tuyến bắc: 오태민 đi dọc rìa lau, kéo từng bộ binh Goguryeo giáo dài xen vào giữa hai lính Hàn trong hố — giáo, súng, giáo, súng; một lính Goguryeo giáp lamellar và một lính Hàn áo camo rách quỳ sát vai nhau nhìn ra bãi cát. Tracking chậm.
[SOUND] giáo cắm cát, giáp, mưa, lệnh ngắn.
N: 창 하나, 총 하나. 천사백 년이 한 구덩이에 나란히 앉았습니다. 총에는 탄창 둘, 창에는 끝이 없었습니다.
오태민: 여기. 총 옆에 서시오.

### SC_182 · LOC_007_SALSU (tuyến bắc) · CHAR_105, CHAR_002 · VEH_101 (giáo 삭), WPN_003 · video8s · 24:58–25:06
[ACTION-VI] 해모루 tới bên 오태민 ở rìa lau, đặt tay lên cán một cây giáo cắm cát, chỉ mũi giáo về bãi cát rồi chỉ khẩu K3 của 오태민; nói ngắn — 하오체; 오태민 gật, lần đầu không gượng.
[SOUND] mưa, giáp.
N: 해모루는 창을 설명하지 않았습니다. 역할을 나누었을 뿐입니다.
해모루: 창은 말을 세우오. 그대들 쇠는 사람을 세우시오.

### SC_183 · LOC_007_SALSU (tuyến bắc) · CHAR_002, 천둥 중대 · WPN_001 · video8s · 25:06–25:14
[ACTION-VI] 오태민 quỳ giữa hố, quay lại nhìn hàng lính của mình dọc rìa lau, giơ hai ngón tay rồi một ngón; giọng trầm, 반말 với lính mình.
[SOUND] mưa, giáp, im.
N: 그는 화력으로 밀자던 사람이었습니다. 오늘 그는 한 발씩 세라고 했습니다.
오태민: 탄창 둘. 한 발에 하나다.

### SC_184 · LOC_007_SALSU (KB gò nam, điện tin) · CHAR_101, 고구려 전령 · VEH_101, PROP_024 · still_kenburns · 25:14–25:24
[ACTION-VI] Ảnh: gò nam — kỵ binh trẻ của 해모루 quỳ một gối trước 을지문덕, ngựa ướt sũng thở dốc sau lưng (đã lội mô cát thượng lưu rồi vòng qua sông); 을지문덕 cúi nghe, kiếm thấp; phó tướng bên cạnh; dưới gò, sông đầy người. Ken-burns từ người lính quỳ lên mặt ông.
[SOUND] mưa, ngựa thở, trống.
N: 전령이 상류 모래톱을 돌아 남쪽 언덕에 닿았습니다. 반 시간이 걸렸습니다. 말은 짧았습니다. 쇠수레가 목으로 내려간다. 을지문덕은 그 말을 두 번 묻지 않았습니다.

### SC_185 · LOC_007_SALSU (gò nam) · CHAR_101, 고구려 부장 · VEH_101, PROP_018 · video8s · 25:24–25:32
[ACTION-VI] 을지문덕 đứng thẳng, quay sang phó tướng và người thổi tù và; nói với giọng thấp sắc — quyết định; phó tướng chạy về hàng kỵ binh phía sau gò; người thổi tù và nâng sừng. Máy cận rồi mở rộng.
[SOUND] giáp, giọng, tù và bắt đầu.
N: 마개가 목으로 내려가면 병 안의 물은 갇힐 것이었습니다. 그는 남은 기병을 다 보내기로 했습니다.
을지문덕: 쇠수레가 목을 막으면 우리는 꼬리를 치오. 전군.

### SC_186 · LOC_007_SALSU (bãi lau phía tây) · CHAR_004, CHAR_107, 마을 여인, 천둥 중대 (thương) · PROP_009 · video8s · 25:32–25:40
[ACTION-VI] Bãi lau phía tây, xa cổng họng: các chiếu lau đặt xuống cát cao hơn; 서아 đi từng chiếu kiểm tra garô; 아리 quỳ cho một thương binh uống nước bằng bầu; phụ nữ làng dựng lau che mưa. Máy trung.
[SOUND] mưa, rên, lau dựng.
N: 의무실은 서쪽으로 이백 걸음 옮겨졌습니다. 전차가 가는 길에서 가장 먼 갈대였습니다. 서아는 지혈대를 하나씩 다시 조였습니다.

### SC_187 · LOC_007_SALSU (bãi lau, hố 태오) · CHAR_005 · WPN_001, EQP_002 · video8s · 25:40–25:48
[ACTION-VI] 태오 kéo mình ngồi thẳng trong hố, radio chết bên chân, K2C1 gác miệng hố hướng bắc; mũ trụ sắt Goguryeo chỉnh lại; một lính bên cạnh định kéo cậu về trạm cứu thương — cậu lắc đầu, nói.
[SOUND] mưa trên sắt, khóa nòng.
N: 장태오는 옮겨지지 않기로 했습니다. 걷지 못하는 병사도 볼 수는 있었습니다. 넉 달 전 그는 하늘의 눈이었습니다.
장태오: 제가 봅니다. 제가 눈입니다.

### SC_188 · LOC_007_SALSU (bãi lau, K2 đuôi xe) · CHAR_003, CHAR_106 · VEH_001 · video8s · 25:48–25:56
[ACTION-VI] 박기철 mở tấm nắp kiểm tra ở hông đuôi K2, chỉ cho 을보 một van xả nhiên liệu nhỏ có tay vặn; 을보 cúi nhìn, ngửi mùi dầu, nheo mắt trái; 박기철 đóng nắp lại, gật với ông già.
[SOUND] nắp thép, mưa, mùi dầu (im).
N: 검은 물. 요동성에서 붙은 이름이었습니다. 을보 영감도, 탁발흠도 같은 이름을 썼습니다. 그 물은 강에 쏟아질 것이었습니다.
을보: 여길 열면 검은 물이 다 새는구먼.

### SC_189 · LOC_007_SALSU (trong tháp K2) · CHAR_001 · VEH_001, PROP_025 · video8s · 25:56–26:04
[ACTION-VI] Trong tháp: 한승우 ngồi ghế trưởng xe, cầm quả lựu đạn nhiệt nhôm đặt thử lên khay nạp đạn trống của máy nạp tự động — bộ đếm "00" sáng xanh bên cạnh; ông kiểm tra chốt, rồi lấy lại, cài vào dây áo giáp ngực chỗ một tay với tới được; nhìn lên cửa tháp còn mở có mưa rơi vào.
[SOUND] lựu đạn chạm khay thép, quạt điện tử, mưa rơi vào tháp.
N: 포탄이 있던 자리는 비어 있었습니다. 이 전차의 마지막 탄은 그의 가슴에 있었습니다. 적을 향한 탄이 아니었습니다.

### SC_190 · LOC_007_SALSU (rìa nam bãi lau) · 사수 K3, 수 보병 · WPN_003, WPN_201 · video8s · 26:04–26:12
[ACTION-VI] Rìa nam: hàng khiên Tùy bò lên tới mép gờ cổng họng, cách bao cát 60 m, cung thủ sau khiên bắn thẳng; xạ thủ K3 thứ hai bóp cò — ngắt; mở nắp — trống; anh gào về phía K2; hàng giáo Goguryeo bước ra chắn trước hố. Máy từ hố, rung.
[SOUND] K3 ngắt, nắp mở, gào, tên cắm bao cát, giáo.
N: 남쪽에서 마지막 기관총이 침묵했습니다. 목까지 육십 미터였습니다.
사수: K3 탄 떨어졌습니다!

### SC_191 · LOC_007_SALSU (bãi cạn, trung quân) · 수 보병 · WPN_201 · video8s · 26:12–26:20
[ACTION-VI] Bãi cạn: trung quân Tùy trong nước ngang ngực cố lội về phía cổng họng — bước rất chậm, khiên bỏ, giáo bỏ, hai tay đẩy nước; người phía sau dồn lên người phía trước; ai ngã không đứng dậy. Aerial thấp, không cận.
[SOUND] nước nặng, thở, gào không lời.
N: 가슴까지 오는 물에서 사람은 뛰지 못했습니다. 걷지도 못했습니다. 헤엄치기에는 얕았고, 걷기에는 깊었습니다. 을지문덕이 기다린 물이었습니다. 하늘이 열흘 동안 채운 물이었습니다.

### SC_192 · LOC_007_SALSU (mô cát giữa sông) · CHAR_202, 수 기병 · PROP_021 · video8s · 26:20–26:28
[ACTION-VI] 우중문 bên mô cát đã lở gần hết, nước lên tới cổ áo choàng rách, cán cờ gãy trong tay; một kỵ sĩ Tùy dắt tới con ngựa không yên; ông nhìn dòng nước xoáy quanh ngực, nói — không với ai.
[SOUND] nước xoáy, ngựa thở, mưa.
N: 우중문은 물을 보았습니다. 평양은 사흘 거리라던 사람이었습니다. 시를 받고 웃던 사람이었습니다. 이제 그는 물이 왜 빠른지를 물었습니다.
우중문: 물이… 물이 왜 이렇게 빠른가.

### SC_193 · LOC_007_SALSU (KB aerial toàn bàn cờ) · — · WPN_201, VEH_101, VEH_206 · still_kenburns · 26:28–26:40
[ACTION-VI] Ảnh aerial cao, mưa: bờ nam — kỵ Goguryeo đang đổ hết xuống hậu quân ở mép nước; bãi cạn — khối trung quân dày đặc, mô cát lở; cổng họng — tiền quân dồn trên gờ; bãi lau — khối đen nhỏ; bãi cát bắc — kỵ Tiên Ti hình quạt; xa về đông — dải mô cát thượng lưu với một hàng chấm nhỏ bắt đầu lội. Ken-burns kéo rất chậm từ gò nam qua sông tới dải mô cát thượng lưu.
[SOUND] mưa, trống, nhạc trầm dâng.
N: 을지문덕의 계획은 강 전체에서 돌아가고 있었습니다. 남쪽에서 기병이 꼬리를 치고, 물이 가운데를 잡고, 언덕이 양쪽을 막았습니다. 그 계획에서 비어 있는 곳이 하나였습니다. 북쪽 기슭의 육십 걸음. 그 육십 걸음은 이제 여든여섯 명이 아니라 쇠 하나가 막을 것이었습니다.

### SC_194 · LOC_007_SALSU (bãi lau, K2) · CHAR_105, CHAR_001 · PROP_018 · video8s · 26:40–26:48
[ACTION-VI] 해모루 và 한승우 đứng đối diện bên xích K2; 해모루 nắm cẳng tay 한승우 kiểu Goguryeo — bàn tay trên cẳng tay; tù và trên hông ông; ông nói, rồi buông, quay về tuyến bắc với hàng giáo.
[SOUND] giáp da, mưa, giọng.
N: 두 사람은 약속을 하나 했습니다. 마개가 서면 나각 세 번. 아침에 장군이 쓴 신호였습니다.
해모루: 한 대장. 마개가 서면 내가 나각을 불겠소.

### SC_195 · LOC_007_SALSU (bãi lau, K2) · CHAR_001 · — · video8s · 26:48–26:56
[ACTION-VI] 한승우 một mình bên mũi K2: rút cái nút bầu gỗ khỏi túi ngực, nhìn nó trong lòng bàn tay dưới mưa, rồi cất lại — không vào túi, mà nhét vào khe giữa hai tấm giáp mũi xe. Cận tay.
[SOUND] gỗ vào khe thép, mưa.
N: 그는 마개를 전차에 꽂았습니다. 병에 들어가는 것은 마개였습니다. 사람이 아니었습니다. 그것이 이 계획의 마지막 조건이었습니다.

### SC_196 · LOC_007_SALSU (bãi lau, K2) · CHAR_002, CHAR_001 · WPN_003 · video8s · 26:56–27:04
[ACTION-VI] 오태민 tới, K3 trên vai, đứng nghiêm trước 한승우 đang bám mép tháp chuẩn bị trèo; anh không chào tay — nói một câu, giọng lính; 한승우 gật, trèo lên tháp.
[SOUND] giày trên xích, mưa, giọng.
N: 다녀오라는 말은 돌아온다는 뜻이었습니다. 오태민은 그 말을 골랐습니다.
오태민: 중대장님. 다녀오십시오.

### SC_197 · LOC_007_SALSU (khoang lái K2) · CHAR_003 · VEH_001 · video8s · 27:04–27:12
[ACTION-VI] Khoang lái K2 nằm ngả: 박기철 tay trên cần lái kiểu yoke, tóc muối tiêu ướt dán trán, mắt qua kính tiềm vọng đã được lau — bãi lau rạp, cổng họng xa, nước xám ngang ngực người ở khe; ngón tay ông đặt lên nút khởi động, không bấm — nói với chính mình, đợi. Cận tay và mặt.
[SOUND] mưa trên thân xe (tiếng trong), thở, im.
N: 삼백 미터. 십 년 동안 수천 킬로를 몰았습니다. 마지막 삼백 미터는 한 번뿐이었습니다.
박기철: 도하 준비 없이 일 점 이 미터. 가슴이면 아슬아슬합니다.

### SC_198 · LOC_007_SALSU (bãi lau, tháp K2) · CHAR_001, 천둥 중대, 고구려 보병 · VEH_001 · video8s · 27:12–27:20
[ACTION-VI] 한승우 đứng trong cửa tháp, nhìn xuống bãi lau: lính Hàn trong hố, bộ binh Goguryeo với giáo, 태오 mũ trụ sắt, 을보 với thanh sắt — mặt nào cũng ngước lên xe; ông không nói gì; kéo nắp cửa tháp xuống một nửa. Máy từ dưới lên rồi từ trong tháp ra.
[SOUND] nắp sắt, mưa, im.
N: 그는 말을 하지 않았습니다. 넉 달 동안 그는 연설을 한 번도 하지 않았습니다. 오늘도 하지 않았습니다. 뚜껑을 반쯤 닫았습니다.

### SC_199 · LOC_007_SALSU (cửa tháp K2, cận) · CHAR_001 (tay) · VEH_001 · still_kenburns · 27:20–27:30
[ACTION-VI] Ảnh cận: nắp cửa tháp K2 hạ xuống còn hé một khe; qua khe, một con mắt; mưa chảy trên vành thép bùn; lau cắm trên nóc rung. Ken-burns đẩy chậm vào khe cửa.
[SOUND] mưa, nhạc trầm ngừng.
N: 300미터. 전차가 마지막으로 달릴 거리였습니다.

[MID-ROLL 4 · 27:30]

[Kết thúc Phần 9]

## [Phần 10] 살수 — 「살수」 / Trận đánh quyết định  (27:30–34:30) — 6 phase
> Tóm tắt VI: Phase 1 (300 m): K2 lao khỏi lau, nòng rỗng quay — tiền quân Tùy dạt (tin), 탁발흠 không; xuống nước, tới cổng họng — **nước qua lưới hút gió, động cơ sặc tắt trước khi 박기철 chạm nút** ("물이 껐습니다" — giới hạn 1,2 m ông nói ở P9); xích lún; mở van dầu — dầu loang; **해모루 thổi 나각 ba hồi → gò nam 을지문덕 hạ kiếm, toàn quân kỵ xuống** (2-BEAT SC_208/211). Phase 2 (kẻ săn): 탁발흠 thấy "천둥" một mình giữa sông — bỏ trận, dẫn 500 kỵ xuống nước lấy xe; tên cắm chi chít. Phase 3 (sai sót — **sai lầm thật của 한승우**: đếm người trước lửa, như suốt 4 tháng): hai người bỏ xe dưới tên; 박기철 trúng tên vào chân; 한승우 kéo ông lên mô cát nhỏ — lựu đạn còn trên ngực → quay lại xe dưới mưa tên, thả nhiệt nhôm vào khóa nòng; khói trắng; giọt sắt lỏng rơi xuống vệt dầu — dầu trên nước bén lửa. Phase 4 (NARRATOR IM 31:30–33:22): 백성민 + 300 kỵ 해모루 vượt mô cát thượng lưu đánh lưng 탁발흠; 해모루 dẫn 50 giáo ra kẹp — **trúng tên dưới xương đòn trái** (theo character_bible), ngã ở mép nước; giữa sông ngựa 우중문 ngã — kỵ Goguryeo kéo ông lên khỏi nước, trói (bắt sống); trung quân giẫm nhau; tiền quân bãi bắc tan — 우문술 hạ kiếm để họ chạy; 오태민 tuyến giáo + súng rỗng đứng vững. Phase 5 (nóc xe): 탁발흠 leo lên nóc K2 cháy — bên trong lửa trắng, không có gì để lấy; giương cung vào 한승우 cách 30 m — **tay phải băng cũ (vết dao 백성민 4화) run, chậm nửa nhịp**; 한승우 bóp cò — cạch — 박기철: "탄창 비었습니다." — từ bờ lau, mũi tên của 해모루 nửa chết; 탁발흠 rơi xuống sông; 태극기 của 태오 tuột khỏi thắt lưng hắn, trôi. Phase 6: nắng xé mây; K2 cháy lún cát, nước tràn giáp; Tùy vỡ mọi hướng; giáo Goguryeo + súng rỗng Hàn đứng cạnh nhau; Goguryeo reo, đại đội không.
> Chức năng: BATTLE · Tài nguyên: tất cả → 0 · 86→80 · 박기철 chân · 해모루 hấp hối · K2 chìm · Enemy adaptation: 탁발흠 chọn xe thay trận — cái học cuối thành cái chết · Payoff: "천둥을 가져오라" (1화) · 태극기 3화 · nút bầu · 을보 nước · Quyết định sử: 우문술 để tiền quân chạy · Combat: SC_200–250 · Open loop: "전차는 모래 속으로 가라앉았습니다. 강은 다시 흐르기 시작했습니다."
> [NARRATOR IM LẶNG] 31:30 → 33:22 (SC_230–243); narrator 1 câu ở SC_244 rồi im tới SC_250. Sau mid-roll 4: SC_200 K2 nổ máy, bùn trượt khỏi giáp, không thoại.

### — Phase 1 · 300미터 / 300 m (27:30–28:42) —

### SC_200 · LOC_007_SALSU (bãi lau, K2) · — · VEH_001 · video8s · 27:30–27:38
[ACTION-VI] Cận hông K2: động cơ nổ — thân xe rùng một cái, bùn khô trên giáp nứt và trượt xuống thành mảng, lau cắm trên nóc rung rồi rụng, khói xám phụt từ lưới thoát khí đuôi; mưa bắn ngược. Không thoại.
[SOUND] động cơ 1.500 mã lực gầm lên từ im lặng, bùn rơi, lau rụng.

### SC_201 · LOC_007_SALSU (bãi lau → bãi cát) · CHAR_002 (xa), 천둥 중대 · VEH_001 · video8s · 27:38–27:46
[ACTION-VI] K2 lao ra khỏi bãi lau — lau rạp thành đường, tên cắm nóc gãy rụng; tháp pháo xoay chậm sang phải rồi sang trái, nòng rỗng quét ngang bãi cát; từ hố, 오태민 và lính Hàn, bộ binh Goguryeo ngẩng nhìn theo. Wide thấp từ phía sau xe.
[SOUND] xích nghiến cát, động cơ, lau gãy.
N: 삼백 미터가 시작되었습니다. 나가는 전차는 빈 대포를 좌우로 돌렸습니다. 쏠 수 없었습니다. 그러나 보이는 것은 대포였습니다.

### SC_202 · LOC_007_SALSU (gờ cát trên cổng họng) · 수 보병 · WPN_201, PROP_021 · video8s · 27:46–27:54
[ACTION-VI] Gờ cát trên cổng họng: tiền quân Tùy dày đặc nhìn thấy khối đen gầm rú từ bãi lau chạy thẳng về phía họ, nòng pháo quay — hàng khiên vỡ, người dạt sang hai bên, có người bỏ khiên chạy ngược lên bãi cát; một tướng nhỏ gào giữ hàng, không ai nghe. Wide.
[SOUND] gào hoảng, khiên rơi, chạy, động cơ dội.
N: 수나라 병사들은 그것이 비었다는 것을 몰랐습니다. 요동성에서 그것이 우는 것을 들은 자들이었습니다. 그들은 길을 열었습니다. 검은 소가 지나가도록.
수 부장: 검은 소다! 비켜라!

### SC_203 · LOC_007_SALSU (bãi cát bắc) · CHAR_205 · VEH_206, EQP_001 · video8s · 27:54–28:02
[ACTION-VI] 탁발흠 trên ngựa ở bãi cát bắc, mũ mất, bím tóc xổ, kính đêm vỡ trên ngực; ông nhìn K2 chạy ngang bãi cát cách 200 m — không quay ngựa, không lùi; mắt theo nòng pháo quay — môi mím: ông biết. Cận.
[SOUND] động cơ xa dần, mưa, ngựa.
N: 탁발흠은 알았습니다. 그는 여섯을 세었습니다. 그가 본 것은 대포가 아니라 무게였습니다. 그리고 그 무게가 어디로 가는지를 보았습니다.

### SC_204 · LOC_007_SALSU (bãi cát, 300 m) · CHAR_003 (trong xe) · VEH_001 · video8s · 28:02–28:10
[ACTION-VI] 2-BEAT: (a) khoang lái: 박기철 hai tay trên yoke, mắt qua kính tiềm vọng — bãi cát, cổng họng lớn dần; (b) ngoài: K2 chạy hết tốc trên cát ướt, xích hất bùn thành hai cánh, tên Tùy từ gờ cát bay tới đập vào giáp bật ra như mưa đá. Tracking ngang.
[SOUND] động cơ, xích, tên đập thép "캉캉".
N: 박기철은 십 년 만에 가장 빨리 몰았습니다. 삼백 미터는 삼십 초였습니다.
박기철: 가자, 이놈아.

### SC_205 · LOC_007_SALSU (cổng họng bãi, mép nước) · — · VEH_001 · video8s · 28:10–28:18
[ACTION-VI] K2 lao xuống khe cổng họng — mũi xe cắm xuống nước, sóng bùn nâu dựng lên hai bên cao hơn tháp, nước tràn qua mũi; xe chậm lại trong nước ngang ngực người, xích khuấy cát. Low-angle từ mặt nước.
[SOUND] nước dội, động cơ gằn xuống, xích trong cát.
N: 오십오 톤이 물에 들어갔습니다. 물은 전차의 허리까지 왔습니다. 그 물이 사람의 가슴이었습니다.

### SC_206 · LOC_007_SALSU (cổng họng bãi, giữa khe) · CHAR_003 (trong xe) · VEH_001 · video8s · 28:18–28:26
[ACTION-VI] K2 tới giữa khe — thân xe chắn ngang 60 m còn lại cùng bờ bùn dốc phía đông; nước dâng qua lưới hút gió đuôi xe — động cơ sặc, khựng, tắt trước khi ngón tay 박기철 chạm nút; xích quay thêm nửa vòng rồi lún vào cát, xe nghiêng nhẹ; trong khoang lái, kim đồng hồ rơi; im. Máy trong/ngoài (cùng xe).
[SOUND] động cơ sặc nước rồi tắt, thép nguội kêu "틱틱", nước chảy qua xích, mưa — đột ngột nghe rõ mưa.
N: 기름 이십 킬로 중 삼백 미터를 썼습니다. 남은 기름은 태울 것이었습니다. 목은 막혔습니다. 강이 먼저 막았습니다.
박기철: (intercom) 물이 껐습니다. 여울 목. 정지.

### SC_207 · LOC_007_SALSU (trong K2, đuôi khoang) · CHAR_003 · VEH_001 · video8s · 28:26–28:34
[ACTION-VI] 2-BEAT: (a) 박기철 với tay ra sau ghế lái, vặn tay van xả nhiên liệu — nặng — vặn tiếp, dầu chảy ra ngoài qua đáy xe; (b) ngoài: mặt nước quanh đuôi K2 loang một vệt dầu óng nhiều màu, trôi theo dòng xuống cổng họng, qua những cái đầu người trong nước. Cận tay, rồi mặt nước.
[SOUND] van rít, dầu chảy vào nước, mưa.
N: 검은 물이 강으로 나갔습니다. 넉 달 동안 목숨처럼 세던 기름이었습니다. 이제 그것은 불이 될 것이었습니다.

### SC_208 · LOC_007_SALSU (rìa lau → aerial cổng họng) · CHAR_105 · PROP_018, VEH_001, WPN_201 · video8s · 28:34–28:42
[ACTION-VI] 2-BEAT: (a) 28:34–28:38 rìa bãi lau: 해모루 đứng thẳng khỏi hố, nâng tù và sừng đen lên miệng — thổi ba hồi trầm, ngắt rõ, vang qua sông; (b) 28:38–28:42 aerial thẳng xuống: khe cổng họng bị chặn bởi khối K2 đen nằm ngang trong nước; phía dưới khe (sông), hàng vạn đầu người trong nước ngang ngực dồn về khối đen và dừng; phía trên khe (bãi cát), tiền quân dồn lại nhìn xuống, không xuống được; giữa hai biển người — một khối sắt. Máy tĩnh, đẩy chậm.
[SOUND] tù và ba hồi vang qua sông; mưa, gào từ hai phía, im giữa.
N: 마개였습니다. 아래의 십만은 올라오지 못했습니다. 위의 오만은 내려가지 못했습니다. 을지문덕이 그린 병에 마개가 꽂혔습니다. 마개는 쇠였습니다.

### — Phase 2 · 사냥꾼 / Kẻ săn (28:42–29:54) —

### SC_209 · LOC_007_SALSU (bãi cát bắc) · CHAR_205 · VEH_206, EQP_001 · video8s · 28:42–28:50
[ACTION-VI] 탁발흠 giục ngựa lên gờ cát phía đông, nhìn xuống cổng họng: khối đen nằm một mình giữa nước, không lính Hàn nào quanh nó, chỉ nước và người Tùy chết đuối; mắt ông sáng lên lần đầu trong tập; tay siết đao.
[SOUND] mưa, ngựa, gào xa.
N: 넉 달 동안 그는 이 쇠를 쫓았습니다. 황제가 가져오라 한 것이었습니다. 우중문이 죄를 잊겠다고 한 값이었습니다. 이제 그것이 물 가운데 혼자 있었습니다.

### SC_210 · LOC_007_SALSU (bờ bùn dốc phía đông cổng họng) · CHAR_205, 선비 기병 · VEH_206 · video8s · 28:50–28:58
[ACTION-VI] 탁발흠 quay ngựa khỏi bãi lau — bỏ tuyến giáo Goguryeo và tuyến Hàn sau lưng — giơ đao, năm trăm kỵ tách khỏi hình quạt theo ông, phi xuống bờ bùn dốc phía đông cổng họng, lao thẳng xuống nước về phía K2; ngựa lội tới bụng, tới ngực. Tracking từ trên bờ.
[SOUND] vó ngựa xuống dốc bùn, nước dội, hô Tiên Ti.
N: 그는 전투를 버렸습니다. 갈대밭도, 창병도, 오만의 선봉도 버렸습니다. 오백 기를 데리고 물로 들어갔습니다. 쇠수레 하나를 위해서였습니다.

### SC_211 · LOC_007_SALSU (gò nam → tuyến bắc bãi lau) · CHAR_101, CHAR_002 · PROP_024, VEH_101, WPN_003 · video8s · 28:58–29:06
[ACTION-VI] 2-BEAT: (a) 28:58–29:02 gò nam: 을지문덕 nghe hồi tù và thứ ba từ bờ bắc — hạ kiếm đang cầm thấp xuống một nhát; sau gò, hàng kỵ Goguryeo còn lại lao xuống dốc về phía sông (không thoại); (b) 29:02–29:06 tuyến bắc: 오태민 sau bụi lau thấy hình quạt kỵ Tiên Ti tách ra — áp lực trước mặt giảm hẳn, chỉ còn ~1.500 đứng xa; anh đứng thẳng, gào cho cả tuyến, chỉ K3 về hướng cổng họng.
[SOUND] tù và hồi ba tắt, vó ngựa đổ dốc; gào, mưa, vó ngựa Tiên Ti xa dần.
N: 남쪽 언덕이 신호를 받았습니다. 북쪽 선은 갑자기 가벼워졌습니다. 사냥꾼이 사냥감을 바꾸었기 때문입니다.
오태민: 탁발흠이 빠집니다! 전차로 갑니다!

### SC_212 · LOC_007_SALSU (cổng họng, K2) · 선비 기병 · VEH_001, VEH_206 (cung Tiên Ti) · video8s · 29:06–29:14
[ACTION-VI] Kỵ Tiên Ti trong nước tới ngực ngựa vây quanh K2, cung giương — tên bắn thẳng vào xe từ mọi phía ở cự ly 20 m: cắm vào lưới thoát khí, vào giá đồ, đập vào tháp bật ra; tên cắm dày lên nóc như lông nhím trong vài giây. Máy tĩnh ngang tháp.
[SOUND] hàng trăm mũi tên cắm thép và bật thép, nước, ngựa.

### SC_213 · LOC_007_SALSU (trong tháp K2) · CHAR_001 · VEH_001, PROP_025 · video8s · 29:14–29:22
[ACTION-VI] Trong tháp: tiếng tên đập lên nóc như mưa đá trên mái tôn; 한승우 ngồi ghế trưởng xe, nhìn bộ đếm "00", nhìn cửa tháp đóng, tay đặt lên quả lựu đạn trên ngực — chưa rút; ông nhìn qua kính tiềm vọng: mặt kỵ binh Tiên Ti cách 5 m. Cận mặt.
[SOUND] tên trên thép dồn dập (tiếng trong), thở, quạt.
N: 안에서는 우박 소리였습니다. 그는 아직 뽑지 않았습니다. 태우기 전에 나가야 했습니다. 나가려면 문을 열어야 했습니다. 문 밖에는 화살이 있었습니다.

### SC_214 · LOC_007_SALSU (gờ cát trên cổng họng) · CHAR_203, 수 보병 · VEH_207, WPN_201 · video8s · 29:22–29:30
[ACTION-VI] Gờ cát: 우문술 nhìn xuống K2 chắn khe — ông phất tay cho một toán lính thử vòng qua đầu xe: họ bước xuống bờ bùn dốc phía đông, trượt, rơi xuống nước ngang ngực, không lên lại được; toán khác thử qua bãi lau phía tây — giáo Goguryeo chờ. Ông hạ tay. Máy trung.
[SOUND] lệnh, bùn trượt, nước, giáo cắm.
N: 우문술은 돌아갈 길을 찾았습니다. 동쪽은 진흙 벼랑이었고 서쪽은 창이었습니다. 가운데는 쇠였습니다. 육십 걸음은 이제 영 걸음이었습니다.

### SC_215 · LOC_007_SALSU (cổng họng, K2) · 선비 기병, CHAR_003 (trong xe) · VEH_001, VEH_206 · video8s · 29:30–29:38
[ACTION-VI] 2-BEAT: (a) kỵ Tiên Ti xuống ngựa trong nước ngang ngực, bám váy xích trèo lên hông K2, đao gõ lên nóc tìm cửa; (b) khoang lái: 박기철 kéo nắp cửa lái xuống, khóa chốt — tối; tiếng đao gõ thép ngay trên đầu.
[SOUND] đao gõ thép, nắp khóa, thở trong tối.

### SC_216 · LOC_007_SALSU (trong tháp K2) · CHAR_001, CHAR_003 (giọng intercom) · VEH_001 · video8s · 29:38–29:46
[ACTION-VI] 한승우 bấm intercom, nói với khoang lái; tay kia đã nắm tay nắm cửa tháp; ông nhìn quả lựu đạn trên ngực một nhịp, rồi nhìn nắp cửa — quyết: ra trước, đốt sau — vì 박기철 phải ra được cửa lái phía trước dưới nòng pháo.
[SOUND] intercom "틱", đao gõ nóc, thở.
N: 그는 순서를 정했습니다. 사람 먼저. 조종수 문은 앞에 있었습니다. 그가 먼저 나가야 박기철이 나올 수 있었습니다.
한승우: (intercom) 박 상사, 나간다. 지금.

### SC_217 · LOC_007_SALSU (cổng họng, nóc K2) · 선비 기병 · VEH_001, VEH_206 · video8s · 29:46–29:54
[ACTION-VI] Cận nóc K2: tên cắm dày như lông nhím quanh cửa tháp, mưa chảy qua cán tên; một kỵ Tiên Ti đứng trên nóc, hai tay nắm đao bổ xuống nắp cửa tháp — tiếng chuông rền; anh ta bổ tiếp. Máy thấp trên nóc.
[SOUND] đao bổ thép "쾅", chuông rền, mưa.
N: 문을 열면 칼이 있었습니다. 열지 않으면 불이 없었습니다. 둘 다 죽는 길이었습니다. 하나만 고를 수 있었습니다.

### — Phase 3 · 실수 / Sai sót (29:54–31:30) —

### SC_218 · LOC_007_SALSU (nóc K2) · CHAR_001, 선비 기병 · VEH_001, WPN_001 · video8s · 29:54–30:02
[ACTION-VI] 2-BEAT: (a) nắp cửa tháp bật lên — 한승우 nhô lên với khẩu K2C1 trong tay, bắn một phát vào kỵ sĩ đang giơ đao trên nóc — người rơi khỏi nóc xuống nước (không cận); (b) cùng lúc cửa lái xe phía trước bật mở — 박기철 nhô đầu. Máy thấp trên nóc, rung.
[SOUND] nắp bật, K2C1 một phát, người rơi nước, tên rít.

### SC_219 · LOC_007_SALSU (mũi K2, mặt nước) · CHAR_003 · VEH_001 · video8s · 30:02–30:10
[ACTION-VI] 박기철 lăn khỏi cửa lái, trượt xuống mặt giáp mũi xe nghiêng về phía mô cát nhỏ — một mũi tên từ bên hông cắm vào đùi trái ông giữa lúc trượt; ông rơi xuống nước ngang ngực, chìm rồi ngoi lên, ôm chân. Máy ngang nước.
[SOUND] tên cắm, người rơi nước, sặc.
N: 화살은 다리를 골랐습니다. 방탄복은 가슴만 가렸습니다. 넉 달 동안 변하지 않은 사실이었습니다.

### SC_220 · LOC_007_SALSU (cổng họng, mặt nước) · CHAR_001, CHAR_003 · VEH_001 · video8s · 30:10–30:18
[ACTION-VI] 2-BEAT (jump cut): (a) 30:10–30:14 한승우 nhảy từ tháp xuống nước cạnh 박기철, súng đeo chéo, nắm cổ áo giáp ông kéo — nước tới ngực cả hai, tên cắm xuống nước quanh, dầu loang trên mặt nước; (b) 30:14–30:18 nửa quãng: hai người còn 15 m tới mô cát nhỏ, 박기철 đạp chân lành, mặt trắng, tên vẫn rơi. Máy ngang nước, rung.
[SOUND] nước, tên cắm nước "푹", thở, tên đập thép sau lưng.
N: 삼십 미터. 작은 모래톱까지였습니다. 가슴까지 오는 물에서 삼십 미터는 삼백 미터였습니다.
한승우: 박 상사! 잡아!

### SC_221 · LOC_007_SALSU (mô cát nhỏ cạnh cổng họng) · CHAR_001, CHAR_003 · — · video8s · 30:18–30:26
[ACTION-VI] 한승우 đẩy 박기철 lên bờ mô cát nhỏ — dải cát dài chục mét với một con ngựa Tùy chết nằm ngang; ông lăn 박기철 vào sau xác ngựa; rồi quay đầu nhìn về K2 cách 30 m — cửa tháp mở, khói chưa có, kỵ Tiên Ti đang trèo lên nóc. Máy thấp trên cát.
[SOUND] cát, thở, tên cắm xác ngựa "툭", mưa.
N: 그는 돌아보았습니다. 전차는 아직 타지 않았습니다. 뚜껑은 열려 있었습니다. 수류탄은 그의 가슴에 있었습니다.

### SC_222 · LOC_007_SALSU (mô cát nhỏ) · CHAR_001, CHAR_003 · PROP_025 · video8s · 30:26–30:34
[ACTION-VI] Cận: tay 한승우 chạm quả lựu đạn trên ngực; 박기철 nằm sau xác ngựa nhìn ông, lắc đầu — "đừng"; 한승우 tháo súng đưa cho 박기철, tháo mũ, đặt lên cát, đứng dậy. Hai mặt.
[SOUND] mưa, súng đặt cát, thở.
N: 그것이 그의 실수였습니다. 불보다 사람을 먼저 세었습니다. 넉 달 동안 그랬습니다. 그래서 그는 돌아갔습니다.
박기철: 가지 마십시오.

### SC_223 · LOC_007_SALSU (cổng họng, mặt nước) · CHAR_001, 선비 기병 · VEH_001, VEH_206 · video8s · 30:34–30:42
[ACTION-VI] 2-BEAT (jump cut): (a) 30:34–30:38 한승우 lội ngược về K2 dưới tên — nước ngang ngực, hai tay rẽ dầu trên mặt nước, tên cắm xuống nước hai bên; (b) 30:38–30:42 sát xe: một kỵ Tiên Ti trên ngựa trong nước chắn trước — ông lặn xuống dưới bụng ngựa, ngoi lên bên váy xích, bám lên. Tracking ngang nước, rung.
[SOUND] nước, tên, ngựa hí, thở sặc.
N: 그는 화살 속으로 돌아갔습니다. 넉 달 동안 그는 돌아가자고만 했습니다. 아흔네 명을 데리고. 오늘은 혼자 돌아갔습니다. 쇠를 향해서.

### SC_224 · LOC_007_SALSU (nóc K2, trong tháp) · CHAR_001, 선비 기병 · VEH_001, PROP_025 · video8s · 30:42–30:50
[ACTION-VI] 2-BEAT: (a) 한승우 trèo lên nóc — một kỵ Tiên Ti trên nóc quay lại, đao giơ — ông húc cả người vào anh ta, hai người văng xuống nước bên kia, ông ngoi lên bám lại; (b) ông chúi đầu vào cửa tháp mở, rút chốt lựu đạn nhiệt nhôm, thả vào khay nạp đạn hở của máy nạp — rơi vào khoang đạn. Máy rung, cận.
[SOUND] đao trượt, người rơi nước, chốt rút, lựu đạn lăn trên thép.

### SC_225 · LOC_007_SALSU (nóc K2) · CHAR_001 · VEH_001 · video8s · 30:50–30:58
[ACTION-VI] Khói trắng dày phụt lên từ cửa tháp như một cột — ánh trắng chói bên trong; 한승우 lăn khỏi nóc xuống phía mô cát nhỏ, rơi xuống nước; kỵ Tiên Ti trên hông xe nhảy xuống nước vì khói. Máy thấp, ngược sáng.
[SOUND] nhiệt nhôm rít như hàn, khói xì, người rơi nước.
N: 물이 끄지 못하는 불이었습니다. 쇠를 녹이는 불이었습니다. 선비족은 그런 불을 본 적이 없었습니다.

### SC_226 · LOC_007_SALSU (mô cát nhỏ) · CHAR_001, CHAR_003 · WPN_001 · video8s · 30:58–31:06
[ACTION-VI] 한승우 bò lên mô cát, ướt sũng, không mũ, kéo mình vào sau xác ngựa cạnh 박기철; 박기철 đưa lại khẩu súng, nói qua răng nghiến — mũi tên vẫn cắm bắp chân, ống quần đẫm máu.
[SOUND] cát, thở, mưa, khói xì sau lưng.
N: 두 사람은 죽은 말 뒤에 있었습니다. 삼십 미터 앞에서 전차가 안에서부터 타기 시작했습니다.
박기철: 다리입니다. 뼈는 아닙니다.

### SC_227 · LOC_007_SALSU (cổng họng, K2 cháy) · — · VEH_001 · video8s · 31:06–31:14
[ACTION-VI] K2 giữa khe: cửa tháp phun khói trắng và lửa trắng-vàng, tháp pháo đỏ dần ở mép; từ khe nắp nạp đạn, một giọt sắt lỏng trắng chói chảy xuống váy xích, rơi xuống vệt dầu sát thân xe — dầu bén lửa ngay cạnh thép nóng, lửa chạy trên mặt nước thành vòng quanh xe rồi trôi xuôi theo dòng qua cổng họng, cháy trên đầu những người Tùy trong nước (không cận). Wide.
[SOUND] lửa bùng trên nước, gào, nhiệt nhôm rít.
N: 쇳물 한 방울이 기름 위에 떨어졌습니다. 검은 물이 탔습니다. 물 위에서, 사람들 사이에서. 넉 달 동안 이십 킬로를 아낀 값이었습니다.

### SC_228 · LOC_007_SALSU (cổng họng, mép vòng lửa) · CHAR_205, 선비 기병 · VEH_206, EQP_001 · video8s · 31:14–31:22
[ACTION-VI] Kỵ Tiên Ti trong nước lùi khỏi vòng lửa, ngựa hí, có người bỏ ngựa lội về bờ bùn; 탁발흠 trên ngựa ở mép lửa — ngựa dựng, ông ghì cương, mắt trên chiếc xe đang cháy — không lùi. Kính đêm vỡ phản ánh lửa. Cận.
[SOUND] ngựa hí, lửa trên nước, mưa xì trong lửa.
N: 넉 달 동안 한 번도 물러서지 않았습니다. 요하에서 마흔을 잃고도 언덕에서 세었던 사람이었습니다. 아직 그 안에 무엇이 있는지 보지 못했습니다.

### SC_229 · LOC_007_SALSU (mô cát nhỏ) · CHAR_001 · WPN_001 · video8s · 31:22–31:30
[ACTION-VI] 한승우 tì súng lên xác ngựa, bắn từng phát vào kỵ Tiên Ti trong nước đang vòng lại phía mô cát — một, hai, ba phát, người ngã (không cận); ông đếm bằng môi; băng đạn trong súng là băng cuối của người lính bị thương. Cận vai và mặt.
[SOUND] K2C1 phát một, vỏ đạn rơi cát, nước, lửa.
N: 그는 세면서 쐈습니다. 박기철이 넉 달 동안 가르친 습관이었습니다. 마지막 탄창이었습니다.

[NARRATOR IM LẶNG — 31:30 → 33:22]

### — Phase 4 · 조상의 창 / Tổ tiên gánh — NARRATOR IM (31:30–33:22) —

### SC_230 · LOC_007_SALSU (mô cát thượng lưu, nhánh sông) · CHAR_006, 고구려 기병 · VEH_101, WPN_001 · video8s · 31:30–31:38
[ACTION-VI] Dải mô cát thượng lưu: 백성민 trên ngựa đi đầu, nước tới bụng ngựa, đọc mặt nước — chỗ gợn nông, chỗ tối sâu — giơ tay rẽ trái; sau lưng, 300 kỵ Goguryeo giáp ngựa nối hàng một lội theo đúng vệt của anh, giáo dựng, chỏm lông đỏ rủ. Aerial thấp theo hàng.
[SOUND] nước qua bụng ngựa, giáp, mưa, thở ngựa.

### SC_231 · LOC_007_SALSU (bãi cát bắc, phía đông) · CHAR_006, 고구려 부장, 고구려 기병 · VEH_101, PROP_018 · video8s · 31:38–31:46
[ACTION-VI] Hàng kỵ lên khỏi nhánh sông lên bãi cát bắc — sau lưng hình quạt kỵ Tiên Ti còn lại đang quay mặt về bãi lau; phó tướng Goguryeo thổi tù và một hồi; 300 kỵ dàn ngang thành hàng, giáo hạ; 백성민 giục ngựa lên cùng hàng, K2C1 trên ngực không bắn — tay cầm giáo mượn. Wide.
[SOUND] tù và một hồi, giáo hạ đồng loạt, vó ngựa bắt đầu.
고구려 부장: 쳐라!

### SC_232 · LOC_007_SALSU (bãi cát bắc) · 고구려 기병, 선비 기병 · VEH_101, VEH_206 · video8s · 31:46–31:54
[ACTION-VI] Kỵ Goguryeo giáp ngựa đâm vào lưng hình quạt Tiên Ti — ngựa giáp húc ngựa da, giáo 4 m xuyên qua trước khi đao chạm; hàng Tiên Ti vỡ, tản sang hai bên, có toán phi về bãi lau — vào hàng giáo; có toán phi xuống nước. Wide trung, không gore.
[SOUND] giáp va giáp, giáo, ngựa hí, đao.

### SC_233 · LOC_007_SALSU (rìa bắc bãi lau, mép nước) · CHAR_105, 고구려 보병 · VEH_101 (giáo 삭 của 개마무사), PROP_018 · video8s · 31:54–32:02
[ACTION-VI] 해모루 rút đao, gào một tiếng — nửa hàng giáo Goguryeo (năm mươi người, nửa còn lại ở lại trong hố với tuyến 오태민) bước ra khỏi bãi lau thành hàng ngang, tiến xuống mép nước phía đông để khép gọng kìm với kỵ binh; 해모루 đi đầu, chân trong nước nông, cung trên lưng, tù và hông. Tracking.
[SOUND] lệnh Goguryeo, giáo bước đều, nước nông.
해모루: 창병, 물가로!

### SC_234 · LOC_007_SALSU (mép nước phía đông bãi lau) · CHAR_105, 선비 기병 · VEH_206, WPN_101 · video8s · 32:02–32:10
[ACTION-VI] Một kỵ xạ Tiên Ti thoát khỏi hàng giáo phi dọc mép nước, xoay người trên yên bắn ở 15 m — mũi tên cắm dưới xương đòn trái 해모루 giữa lúc ông quay người; ông ngã ngửa xuống mép nước, mũ trụ rơi lăn xuống nước, tóc xổ, tay còn nắm đao, cán tên dựng trên ngực; kỵ sĩ phi tiếp và bị giáo Goguryeo hạ phía sau. Máy trung, không cận vết thương.
[SOUND] dây cung bật, tên cắm giáp, người ngã nước, mũ lăn, ngựa.

### SC_235 · LOC_007_SALSU (bãi cát bắc) · CHAR_006 · VEH_101 · video8s · 32:10–32:18
[ACTION-VI] 백성민 trên ngựa giữa hàng kỵ đang xé qua hình quạt Tiên Ti — thấy 해모루 ngã ở mép nước cách 50 m; anh ghìm cương một nhịp — hàng kỵ sau đẩy tới — anh không dừng được, giục ngựa tiếp, quay đầu nhìn lại. Cận mặt trên ngựa.
[SOUND] vó ngựa, giáp, thở, mưa.

### SC_236 · LOC_007_SALSU (giữa sông, gần mô cát lở) · CHAR_202, 수 기병 · VEH_207 · video8s · 32:18–32:26
[ACTION-VI] Giữa sông: con ngựa không yên chở 우중문 bước hụt xuống hố cát lở — ngã nghiêng; ông văng xuống nước, chìm; cán cờ gãy nổi lên trước; áo choàng đỏ rách lập lờ dưới mặt nước. Máy ngang nước.
[SOUND] ngựa ngã nước, sặc, dòng chảy.

### SC_237 · LOC_007_SALSU (giữa sông) · CHAR_202, 고구려 기병 · VEH_101, VEH_207 · video8s · 32:26–32:34
[ACTION-VI] Ba kỵ Goguryeo từ bờ nam lội tới trong nước ngang bụng ngựa — một người cúi túm áo choàng đỏ kéo lên: 우중문 ngoi lên sặc nước, râu bết bùn, gương ngực móp; hai người khác vòng dây thừng qua hai tay ông, trói quặt, kéo ông ngược về bờ nam như kéo một cái bao. Máy ngang nước.
[SOUND] nước, dây thừng, sặc, giáp.

### SC_238 · LOC_007_SALSU (bãi cạn, trung quân) · 수 보병 · WPN_201 · video8s · 32:34–32:42
[ACTION-VI] Trung quân trong nước ngang ngực: người giẫm lên người để ngoi lên, khiên trôi, giáo trôi, lửa dầu chạy trên mặt nước phía cổng họng; không ai còn quay về hướng nào. Aerial thấp, chậm, không cận.
[SOUND] gào không lời, nước, lửa xa.

### SC_239 · LOC_007_SALSU (gờ cát trên cổng họng) · CHAR_203, 수 보병 · VEH_207, WPN_201 · video8s · 32:42–32:50
[ACTION-VI] Gờ cát: tiền quân Tùy nhìn xuống — trung quân chìm, cổng họng cháy; hàng người bắt đầu quay lưng, bỏ khiên, chạy lên bãi cát bắc về phía đường lên đồi; 우문술 trên ngựa giơ kiếm định giữ — rồi hạ kiếm xuống, quay ngựa theo họ. Cận rồi wide.
[SOUND] khiên rơi, chạy, mưa, kiếm hạ.
우문술: …가게 두어라.

### SC_240 · LOC_007_SALSU (tuyến bắc bãi lau) · CHAR_002, 고구려 보병, 천둥 중대 · VEH_101 (giáo 삭), WPN_001, VEH_206 · video8s · 32:50–32:58
[ACTION-VI] Tuyến bắc: tàn kỵ Tiên Ti bị dồn từ sau lao vào hàng giáo — ngựa dựng trước rừng giáo, kỵ sĩ rơi; giữa hai cây giáo, một lính Hàn bắn một phát; giáo Goguryeo và lưỡi lê Hàn cạnh nhau trong cùng khung. Máy ngang hàng.
[SOUND] giáo, ngựa dựng, phát một, đao.

### SC_241 · LOC_007_SALSU (tuyến bắc) · CHAR_002 · WPN_003, WPN_001 · video8s · 32:58–33:06
[ACTION-VI] 오태민 bóp cò K3 — ngắt: dây đạn hết; anh vứt K3 xuống cát, rút khẩu K2C1 sau lưng, bắn — một phát — khóa nòng đứng: hết; anh tháo lưỡi lê khỏi thắt lưng, cắm lên nòng bằng một động tác, đứng thẳng vào hàng giáo. Cận.
[SOUND] K3 ngắt, K2C1 khóa nòng, lưỡi lê "철컥", mưa.

### SC_242 · LOC_007_SALSU (bãi lau phía tây → mép nước đông) · CHAR_004, CHAR_107 · PROP_009 · video8s · 33:06–33:14
[ACTION-VI] 서아 chạy khom dọc bãi lau về mép nước phía đông, túi quân y đập hông, mũ đội, bím tóc ướt; 아리 chạy sau, khăn olive; hai người băng qua lau rạp, qua xác ngựa — phía trước là mép nước đông, một hình người nằm (tới nơi = SC_243). Tracking.
[SOUND] chạy trên cát ướt, lau, thở, mưa.
아리: 언니! 말객님이 저기…!

### SC_243 · LOC_007_SALSU (mép nước đông, 해모루) · CHAR_004, CHAR_105 · PROP_009, WPN_101 · video8s · 33:14–33:22
[ACTION-VI] 서아 quỳ, hai tay ép quanh cán mũi tên dưới xương đòn trái 해모루 — không rút — máu loang áo xanh lá thành đen; ông mở mắt, nhìn qua vai cô về phía cổng họng: chiếc xe cháy trắng cách 40 m và một bóng người trên nóc nó; tay phải ông mò ra sau lưng — bao cung; ông kéo cung ra trước ngực; 서아 lắc đầu. Cận hai người.
[SOUND] mưa, thở rít, dây cung chạm giáp, lửa xa.
윤서아: 말객님, 안 됩니다.

### — Phase 5 · 쇠 위에서 / Trên nóc xe (33:22–34:10) —

### SC_244 · LOC_007_SALSU (cổng họng, K2 cháy) · CHAR_205 · VEH_001, VEH_206, EQP_001 · video8s · 33:22–33:30
[ACTION-VI] 탁발흠 giục ngựa xuyên qua mép vòng lửa trên nước — ngựa hí, lông cháy sém — tới hông K2; ông đứng lên yên, bám giá đồ, đu lên nóc xe đang cháy; ngựa quay đầu lồng đi. Ông đứng trên nóc giữa khói trắng, đao trong tay, bím tóc, kính đêm vỡ trên ngực. Low-angle từ mặt nước.
[SOUND] lửa, ngựa hí, giày da trên thép nóng, khói rít.
N: 그는 마침내 천둥 위에 섰습니다.

### SC_245 · LOC_007_SALSU (nóc K2) · CHAR_205, CHAR_001 (xa) · VEH_001, EQP_001, VEH_206 (cung Tiên Ti) · video8s · 33:30–33:38
[ACTION-VI] 2-BEAT: (a) 탁발흠 cúi nhìn vào cửa tháp mở — bên trong là lửa trắng chói và kim loại chảy, không có gì để lấy; kính đêm vỡ trên ngực ông phản ánh ánh trắng; (b) ông đứng thẳng, quay đầu — thấy 한승우 trên mô cát nhỏ cách 30 m sau xác ngựa; ông vứt đao, kéo cung khỏi lưng, rút tên, giương — bàn tay phải kéo dây, cẳng tay băng cũ đen bẩn run, dây cung tới má chậm nửa nhịp. Cận rồi trung.
[SOUND] lửa rít, thép chảy nhỏ giọt, dây cung căng.

### SC_246 · LOC_007_SALSU (mô cát nhỏ) · CHAR_001 · WPN_001 · video8s · 33:38–33:46
[ACTION-VI] 한승우 quỳ sau xác ngựa, súng lên vai, ngắm người trên nóc xe cháy — bóp cò: "철컥" — khóa nòng đã đứng sau từ phát trước; ông nhìn khẩu súng một nhịp rất ngắn; mưa trên tóc ướt không mũ. Cận.
[SOUND] "철컥" khô, lửa xa, mưa — im.

### SC_247 · LOC_007_SALSU (mô cát nhỏ) · CHAR_003, CHAR_001 · WPN_001 · video8s · 33:46–33:54
[ACTION-VI] 박기철 nằm nghiêng sau xác ngựa cạnh ông, mắt trên khóa nòng đứng, nói bình thản như đọc sổ; 한승우 không hạ súng. Hai mặt sát nhau, mưa.
[SOUND] mưa, lửa, dây cung xa căng thêm.
박기철: 탄창 비었습니다.

### SC_248 · LOC_007_SALSU (mép nước đông) · CHAR_105, CHAR_004 · WPN_101 · video8s · 33:54–34:02
[ACTION-VI] 해모루 nửa ngồi trong hai cánh tay 서아 đỡ sau lưng, cán tên vẫn cắm dưới xương đòn trái, cung giương bằng cả người còn lại — cánh tay trái giữ cung run, dây cung tới má, mắt trên nóc xe cháy 40 m; 서아 giữ vai ông không nói; ông thả dây. Cận hai người, tên bay ra khỏi khung.
[SOUND] dây cung "팅", thở hắt, mưa.

### SC_249 · LOC_007_SALSU (nóc K2 → mặt nước) · CHAR_205 · VEH_001, PROP_011 (patch 태극기 của 태오) · video8s · 34:02–34:10
[ACTION-VI] 2-BEAT: (a) mũi tên cắm vào ngực 탁발흠 giữa lúc dây cung của ông đang căng — tên của ông bay chệch lên trời; ông lùi một bước trên nóc xe cháy, ngã ngửa khỏi nóc xuống sông, kính đêm vỡ kéo theo; (b) trên mặt nước loang dầu, một miếng vải nhỏ đỏ-xanh-đen-trắng tuột khỏi thắt lưng da chìm dần của ông, nổi lên, trôi theo dòng qua thân xe, qua những cái đầu người, về phía hạ lưu. Cận mặt nước.
[SOUND] tên cắm, người rơi nước, lửa, nước chảy — rồi rất xa, tiếng reo Goguryeo bắt đầu.

### — Phase 6 · 해가 찢고 나오다 / Nắng xé mây (34:10–34:30) —

### SC_250 · LOC_007_SALSU (bãi bắc, wide) · CHAR_002, 고구려 보병, 천둥 중대, 고구려 기병 · VEH_101 (giáo 삭), WPN_001 · video8s · 34:10–34:18
[ACTION-VI] Mây xám rách — những cột nắng vàng chiếu xuống sông: bãi cạn đầy người Tùy chạy tán loạn về mọi hướng, kỵ Goguryeo giáp ngựa phi qua bãi cạn lấp lánh nước; bờ bắc: hàng giáo Goguryeo và hàng lính Hàn súng rỗng cắm lưỡi lê đứng cạnh nhau trên rìa lau — 오태민 giữa hàng, K3 dưới chân; kỵ Goguryeo giơ giáo reo; lính Hàn đứng im. Wide, máy trôi chậm.
[SOUND] reo Goguryeo lan qua sông, tù và nhiều hồi, mưa ngừng — nước nhỏ giọt.
N: 해가 구름을 찢고 나왔습니다. 고구려가 환호했습니다. 갈대밭의 여든 명은 환호하지 않았습니다. 그들은 서 있었습니다.

### SC_251 · LOC_007_SALSU (aerial cổng họng, K2) · — · VEH_001 · still_kenburns · 34:18–34:30
[ACTION-VI] Ảnh aerial dưới cột nắng: K2 đen sém giữa khe cổng họng — tháp pháo cháy đỏ, khói trắng, thân xe lún nghiêng vào cát, nước nâu tràn qua váy xích và bắt đầu chảy qua nóc thân; quanh xe, cờ Tùy gãy trôi, khiên trôi; vòng lửa dầu tắt dần. Ken-burns đẩy rất chậm vào nước tràn qua giáp.
[SOUND] nước chảy qua thép, lửa tàn, reo xa, nhạc trầm.
N: 전차는 모래 속으로 가라앉았습니다. 강은 다시 흐르기 시작했습니다.

[Kết thúc Phần 10]

## [Phần 11] 2천 7백 — 「2천 7백」 / Chiến thắng có giá  (34:30–37:30)
> Tóm tắt VI: Narrator trở lại trên **video [史] kỵ Goguryeo truy kích tàn quân tới 압록수, 왕인공 chặn hậu** (SC_252, +8 s combat): "30만 5천 명 중 2천 7백 명이 요동성으로 돌아갔습니다. 하루 낮 하루 밤에 450리를 달아났습니다." (내호아 nghe tin rút). Bãi bắc dưới nắng: 80 người đứng/nằm, 20 thương; 한승우 gỡ patch 태극기 của đồng đội tử trận bỏ túi; 서아 với 해모루 (tên đã rút, băng chéo vai trái–ngực) — thảo dược 을보 + morphine cuối: "말객님, 눈 뜨세요. 보세요, 저예요." — "마개는… 아직 서 있소?" — ông thở đến sáng; 박기철 giữ được chân, chống giáo Goguryeo làm nạng. K2: thân đen giữa sông. 을지문덕 xuống mô cát, nhìn chiếc xe ông từng chạm ở Liêu Đông thành — không nói; với 한승우: "쇠수레가 여울을 막았소. 그대들이 마개였소." Đại đội 경례 tự phát — ông không hiểu động tác, gật một cái. 우중문 bị dẫn tới, ướt sũng; 을지문덕 đưa bát nước: "족함을 알라 했소. 물 한 그릇이 족함이오." Cắt 요동 — 육합성 (D+5): 양제 nhận tin; xiềng 우문술 [史]; "우중문은 어디 있는가." — "고구려 손에 있습니다. 살아서."; xe bò 천둥 3 + hộp drone **đã đứng trong sân trại 15 ngày, ông chưa từng chạm**; hôm nay ông ra mưa, chạm giáp K21 lần đầu: "…내년."
> Chức năng: CONSEQUENCE · Tài nguyên nói thành lời: "여든 명" · "2천 7백" · "붕대 마지막" · Payoff: 을지문덕 chạm K2 (2화) · 우중문 bị bắt sống = rẽ timeline · Quyết định sử: 을지문덕 tha nước · 양제 "내년" · Open loop: "황제는 쇠수레를 만졌습니다. 그리고 한마디 했습니다. 내년."

### SC_252 · LOC_005_AMNOK (bờ nam 압록수, tàn quân chạy — [史] 450리) · 고구려 기병, 수 보병 · VEH_101, WPN_101, WPN_201, PROP_021 · video8s · 34:30–34:38
[ACTION-VI] Hôm sau, bờ nam 압록수 dưới mưa lất phất: tàn quân Tùy — không khiên, không cờ, chân trần — chạy tán loạn về phía sông; từ sau lưng, kỵ Goguryeo giáp ngựa truy kích qua đồng, giáo hạ, bắn tên khi phi; ở mép nước, một hàng khiên Tùy nhỏ (천수장군 왕인공) quay lại chặn để những người khác lội qua. Aerial thấp, không cận thương vong.
[SOUND] vó ngựa, tên rít, gào, nước, mưa nhỏ.
N: 30만 5천 명 중 2천 7백 명이 요동성으로 돌아갔습니다. 하루 낮 하루 밤에 450리를 달아났습니다. 역사의 숫자는 바뀌지 않았습니다. 2천 7백.

### SC_253 · LOC_007_SALSU (bãi bắc, nắng) · 천둥 중대, 고구려 보병 · WPN_001, PROP_020 · video8s · 34:38–34:46
[ACTION-VI] Bãi bắc dưới cột nắng, bùn khô dần xám: lính Hàn ngồi, đứng, nằm trên lau rạp — súng rỗng cắm lưỡi lê dựng bên cạnh; bộ binh Goguryeo ngồi lẫn; những tấm poncho phủ thành hàng ở rìa; hơi nước bốc từ áo ướt. Tracking chậm dọc hàng.
[SOUND] nước nhỏ giọt, thở, chim sông, xa xa reo.
N: 여든 명. 아침에는 아흔하나였습니다. 열하나가 갈대 위에 누웠습니다. 스물다섯은 다쳤습니다. 서 있는 사람은 쉰 남짓이었습니다. 총은 다 비어 있었습니다.

### SC_254 · LOC_007_SALSU (bãi bắc, hàng poncho) · CHAR_001 · PROP_011 · video8s · 34:46–34:54
[ACTION-VI] 한승우 (không mũ, tóc ướt, bùn khô tới thắt lưng, máu người khác ngang ngực giáp) quỳ bên một tấm poncho, lật mép — vai áo camo lộ ra; ông gỡ miếng 태극기 rách nửa khỏi Velcro, gấp, bỏ vào túi ngực; kéo poncho lại. Cận tay.
[SOUND] Velcro, vải, nắng — im.
N: 그는 죽은 병사의 어깨에서 태극기를 떼었습니다. 열하나. 요하에서 살수까지 열넷이었습니다. 그는 그 열넷을 모두 주머니에 넣어 왔습니다.

### SC_255 · LOC_007_SALSU (mép nước đông, 해모루) · CHAR_004, CHAR_105 · PROP_009 · video8s · 34:54–35:02
[ACTION-VI] 해모루 nằm ngửa trên chiếu lau, giáp đã cởi, mũi tên đã rút nằm trên cát, băng trắng quấn chéo qua vai trái và ngực; 서아 quỳ, một tay giữ bát thuốc giã của 을보, tay kia cầm ống morphine — ống đầu tiên trong tập — tiêm vào đùi ông; cô cúi sát mặt ông, gọi. Máu tới khuỷu tay cô.
[SOUND] ống tiêm, thở rít, nắng — chim.
N: 여덟 개 중 첫 번째였습니다. 서아는 그것을 고구려 사람에게 썼습니다. 석 달 전 요동성에서 항생제를 쓴 것처럼.
윤서아: 말객님, 눈 뜨세요. 보세요, 저예요.

### SC_256 · LOC_007_SALSU (mép nước đông, 해모루) · CHAR_105, CHAR_004 · — · video8s · 35:02–35:10
[ACTION-VI] 해모루 mở mắt — chậm; mắt không tìm 서아, tìm cổng họng bãi; ông thấy khối đen cháy sém giữa nước; môi động, giọng thều thào.
[SOUND] thở, nước xa.
N: 그는 눈을 떴습니다. 먼저 본 것은 여울 목이었습니다.
해모루: 마개는… 아직 서 있소?

### SC_257 · LOC_007_SALSU (mép nước đông, 해모루) · CHAR_107, CHAR_004 · PROP_009 · video8s · 35:10–35:18
[ACTION-VI] 아리 quỳ bên, tay run mở túi quân y — ngăn băng chỉ còn một cuộn; cô đưa cuộn cuối cho 서아; 서아 nhận, không ngẩng lên, cuốn qua ngực 해모루. Cận hai đôi tay.
[SOUND] băng gạc, thở, chim.
N: 그다음은 을보 영감의 풀과 마을 여인들의 천이었습니다. 해모루는 그날 밤을 넘겼습니다. 아침까지 숨을 쉬었습니다. 서아가 밤새 곁에 앉아 있었습니다.
아리: 언니, 붕대 마지막이에요.

### SC_258 · LOC_007_SALSU (bãi bắc) · CHAR_003, CHAR_004 (xa) · VEH_101 (giáo 삭 gãy làm nạng) · video8s · 35:18–35:26
[ACTION-VI] 박기철 ngồi trên lau rạp, đùi trái băng trắng, mũi tên đã rút nằm trên cát; ông chống một cây giáo Goguryeo gãy đứng dậy, thử đặt chân, nhăn — đứng được; 서아 ở xa gật một cái; ông nhìn ra sông, nói khô.
[SOUND] giáo chống cát, thở, nắng.
N: 다리는 남았습니다. 뼈는 무사했습니다. 그는 고구려 창을 지팡이로 삼았습니다.
박기철: 다리는 붙어 있습니다. 전차는 없습니다.

### SC_259 · LOC_007_SALSU (K2 giữa sông, KB) · — · VEH_001 · still_kenburns · 35:26–35:38
[ACTION-VI] Ảnh: dưới nắng chiều xiên, K2 đen sém giữa khe cổng họng — tháp pháo cháy đen, nghiêng 10°, xích phải chìm cát, nước nâu chảy qua nóc thân, tên gãy cắm nóc; quanh xe, cờ Tùy gãy mắc vào xích, khiên trôi; hơi nước bốc từ thép. Ken-burns đẩy chậm vào tháp.
[SOUND] nước chảy qua thép, gió, chim sông.
N: 전차는 강 가운데 검게 서 있었습니다. 넉 달 동안 사백 킬로를 달린 쇠였습니다. 스물두 발을 울린 쇠였습니다. 이제 그것은 이 시대의 것이었습니다. 물과 모래가 그것을 가져갔습니다.

### SC_260 · LOC_007_SALSU (mô cát nhỏ cạnh cổng họng) · CHAR_101, 고구려 부장 · VEH_101, VEH_001 · video8s · 35:38–35:46
[ACTION-VI] Ngựa 을지문덕 bước lên mô cát nhỏ từ bãi cạn đã vãn người (đã qua sông); ông xuống ngựa — giáp ướt, chỏm lông nặng nước, bùn tới cẳng; ông đứng nhìn chiếc xe cháy cách 30 m; không nói; không chạm — chỉ nhìn, lâu. Máy sau lưng ông rồi vòng ra mặt.
[SOUND] nước chảy, thép nguội kêu "틱", gió.
N: 을지문덕이 모래톱에 내려섰습니다. 석 달 전 요동성 골짜기에서 이 쇠를 한 번 만졌습니다. 며칠이나 달릴 수 있는지 물었습니다. 오늘 그는 대답을 보았습니다.

### SC_261 · LOC_007_SALSU (mô cát nhỏ) · CHAR_101, CHAR_001 · — · video8s · 35:46–35:54
[ACTION-VI] 한승우 lội lên mô cát, đứng trước 을지문덕 — không mũ, ướt, bùn; hai người cách hai bước; 을지문덕 quay khỏi chiếc xe, nhìn ông, nói — 하오체, ngắn, không cười; sau lưng họ, khói mỏng từ tháp pháo.
[SOUND] nước, gió, giọng.
N: 장군은 병법을 말하지 않았습니다. 감사도 말하지 않았습니다. 사실만 말했습니다.
을지문덕: 쇠수레가 여울을 막았소. 그대들이 마개였소.

### SC_262 · LOC_007_SALSU (mô cát nhỏ / bãi bắc) · CHAR_101, CHAR_001, CHAR_002, 천둥 중대 · — · video8s · 35:54–36:02
[ACTION-VI] 한승우 đứng nghiêm, tay phải lên vành mắt — chào; sau lưng ông trên bãi bắc, 오태민 đứng dậy chào, rồi từng người — người ngồi cũng nhấc tay — cả hàng lính Hàn trong nắng; 을지문덕 nhìn động tác lạ, không hiểu, không hỏi — gật một cái. Wide từ sau lưng ông nhìn ra hàng người.
[SOUND] gió, im, nước.
N: 아무도 명령하지 않았습니다. 여든 명이 천사백 년 전의 장군에게 경례했습니다. 그는 그 동작을 몰랐습니다. 묻지 않았습니다. 한 번 고개를 끄덕였습니다. 그것으로 충분했습니다.

### SC_263 · LOC_007_SALSU (mô cát nhỏ) · CHAR_101, CHAR_202, 고구려 기병 · VEH_101, PROP_021 · video8s · 36:02–36:10
[ACTION-VI] Ba kỵ Goguryeo dẫn 우중문 lội lên mô cát — tay trói sau lưng, ướt sũng, râu bùn, áo choàng rách nửa, một gương ngực móp; họ ấn ông quỳ xuống cát trước 을지문덕; 을지문덕 nhận một bát gốm nước từ phó tướng, cúi xuống, đưa bát tới môi ông ta. Máy trung.
[SOUND] dây trói, nước trong bát, gió.
N: 역사에서 우중문은 달아났습니다. 옥에 갇혔다가 병들어 죽었습니다. 오늘 그는 달아나지 못했습니다. 물이 가슴까지 왔기 때문입니다. 을지문덕은 그에게 물을 주었습니다. 그것도 그의 결정이었습니다.

### SC_264 · LOC_007_SALSU (mô cát nhỏ) · CHAR_101, CHAR_202 · — · video8s · 36:10–36:18
[ACTION-VI] 우중문 uống — nước chảy xuống râu bùn; 을지문덕 giữ bát tới khi cạn, rút bát về, đứng thẳng, nhìn xuống ông ta — nói câu mỉa ngầm, giọng phẳng. 우중문 ngẩng nhìn ông — mặt trống rỗng.
[SOUND] uống, bát gốm, gió.
N: 시는 넉 줄이었습니다. 마지막 줄은 족함을 알라는 것이었습니다. 을지문덕은 그 줄을 다시 읽어 주었습니다.
을지문덕: 족함을 알라 했소. 물 한 그릇이 족함이오.

### SC_265 · LOC_007_SALSU (bãi bắc, mép nước) · CHAR_106 · VEH_001 (xa) · video8s · 36:18–36:26
[ACTION-VI] 을보 đứng ở mép nước bãi bắc, tạp dề da khô dần, thanh sắt cắm cát; ông nhìn chiếc xe cháy giữa khe — tay giơ ra như muốn chạm, nhưng cách 100 m nước; ông hạ tay, nheo mắt trái, đứng đó. Máy sau lưng, xe nhỏ trong khung.
[SOUND] nước, gió, chim.
N: 대장장이는 쇠를 만지지 못했습니다. 물이 사이에 있었습니다. 그는 오래 서 있었습니다. 쇠는 쇠였습니다. 가라앉은 쇠도 쇠였습니다.
을보: …쇠는 쇠지.

### SC_266 · LOC_004_YUKHAPSEONG (bên 요동성, mưa, KB) · — · PROP_021 · still_kenburns · 36:26–36:38
[ACTION-VI] Ảnh: 육합성 — tường gỗ-vải lắp ghép, lầu vàng, cờ Tùy đỏ-vàng ướt rũ dưới mưa dầm; trước cổng, một hàng kỵ sứ ướt sũng xuống ngựa; xa, tường đá xám 요동성 vẫn đứng. Ken-burns đẩy từ 요동성 về cổng 육합성.
[SOUND] mưa, trống Tùy chậm, ngựa.
N: 닷새 뒤. 요동성 앞 육합성. 넉 달 동안 성 하나를 깨지 못한 황제에게 소식이 닿았습니다. 별동대 30만 5천 중 2천 7백. 후군 장수 전사. 우중문 실종.

### SC_267 · LOC_004_YUKHAPSEONG (điện trong 육합성) · CHAR_201, CHAR_203, 수 환관 · — · video8s · 36:38–36:46
[ACTION-VI] Trong điện: 양제 đứng bất động giữa sàn — 통천관 hơi lệch, áo vàng thổ, mặt trắng bệch, tay phải bóp nát một tờ tấu; trước ông, 우문술 quỳ, cổ và tay đeo xiềng sắt, giáp bùn khô, râu xám; hoạn quan hai bên cúi sát sàn. Low-angle từ chỗ 우문술.
[SOUND] xiềng, giấy nhàu, lửa đèn, mưa ngoài.
N: 황제는 장군들을 쇠사슬로 묶었습니다. 역사가 기록한 대로였습니다. 우문술은 살아 돌아왔기에 묶였습니다. 황제는 소리를 지르지 않았습니다. 종이를 쥔 손만 하얗게 되었습니다.

### SC_268 · LOC_004_YUKHAPSEONG (điện) · CHAR_201 · — · video8s · 36:46–36:54
[ACTION-VI] Cận 양제: mắt mở lớn không chớp, giọng chậm, từng chữ, lạnh — câu hỏi duy nhất.
[SOUND] lửa đèn, mưa.
N: 황제가 물은 것은 숫자가 아니었습니다. 이름이었습니다.
수 양제: 우중문은 어디 있는가.

### SC_269 · LOC_004_YUKHAPSEONG (điện) · CHAR_203, CHAR_201 · — · video8s · 36:54–37:02
[ACTION-VI] 우문술 ngẩng đầu trong xiềng, nhìn thẳng lên — người thận trọng cả đời nói câu thật cuối; 양제 trên cao nghe, mặt không đổi, tờ tấu trong tay rơi xuống sàn.
[SOUND] xiềng, giấy rơi, im.
N: 살아서. 두 글자가 황제를 아프게 했습니다. 적의 손에 산 장군은 잊을 수 없었습니다. 역사에 없던 일이었습니다.
우문술: …고구려 손에 있습니다. 살아서.

### SC_270 · LOC_004_YUKHAPSEONG (sân trại, mưa, KB) · 소달구지꾼, 선비 기병 · VEH_002 (천둥 3 bị thu), UAV_001 (hộp) · still_kenburns · 37:02–37:12
[ACTION-VI] Ảnh: sân trại trước điện trong mưa — một cỗ xe gỗ khổng lồ đã đứng đó nhiều ngày, bánh xe lún bùn đọng nước, chở khối xe bọc thép phủ vải dầu bám bùn khô (một góc váy xích và bánh chịu nặng lộ ra, vệt sơn trắng hình mũi tên trên cửa đuôi), cờ Tùy cắm trên vải rũ nước; bò đã tháo ách; hai lính gác ướt; bên xe, một hộp sơn mài đen trên tay hoạn quan. Ken-burns từ hộp sơn mài kéo ra toàn xe.
[SOUND] mưa trên vải dầu, bò rống xa, lính gác.
N: 수레는 보름 전에 닿아 있었습니다. 요동성 골짜기에서 스무 날을 끌려온 것이었습니다. 탁발흠이 보낸 장갑차 천둥 3호였습니다. 황제는 그것을 만지지 않았습니다. 살수의 소식을 먼저 기다렸습니다. 그리고 옻칠한 상자 안에 쇠새 한 마리. 보낸 사람은 살수에 있었습니다. 물속에.

### SC_271 · LOC_004_YUKHAPSEONG (sân trại, mưa) · CHAR_201, 수 환관 · VEH_002 · video8s · 37:12–37:20
[ACTION-VI] 양제 bước ra khỏi điện xuống sân trong mưa — hoạn quan che lọng không kịp; ông đi tới cỗ xe, kéo góc vải dầu — tấm giáp thép K21 xanh-nâu ướt lộ ra; ông đặt bàn tay đeo nhẫn ngọc lên thép, giữ; nói một chữ, không nhìn ai.
[SOUND] mưa trên thép, vải dầu, lọng, im.
N: 넉 달 전 그는 부서진 쇠새를 만졌습니다. 이 쇠수레는 보름 동안 만지지 않았습니다. 오늘 만졌습니다. 그의 첫 질문은 늘 소유였습니다.
수 양제: …내년.

### SC_272 · LOC_004_YUKHAPSEONG (sân trại, KB) · CHAR_201 (tay) · VEH_002 · still_kenburns · 37:20–37:30
[ACTION-VI] Ảnh cận: bàn tay đeo nhẫn ngọc của 양제 trên tấm giáp K21 ướt mưa, giọt nước chảy quanh ngón tay; tay áo vàng thổ đẫm nước; nền mờ: cờ Tùy. Ken-burns đẩy rất chậm vào bàn tay.
[SOUND] mưa trên thép, nhạc trầm.
N: 황제는 쇠수레를 만졌습니다. 그리고 한마디 했습니다. 내년.

[Kết thúc Phần 11]

## [Phần 12] 이제 우리는 뭡니까 — 「이제 우리는 뭡니까」 / Lịch sử rẽ hướng  (37:30–40:00)
> Tóm tắt VI: Narrator: Tùy rút khỏi 요동 cuối 7월; 613 lại đến; 614 lại đến; 618 Tùy sụp — "우문술의 아들 우문화급이 황제를 죽였습니다." [史]. 평양 nội điện đêm mưa (D+8): 영양왕, 고건무, 을지문덕 — số phận 뇌군: 고건무: thu vũ khí — "쇠를 거두면 저들은 여든 명의 농부입니다." (nối câu 4화 của ông "쇠를 거두어야 합니다"; quote outline "총" → "쇠" theo decisions); vua: "이겼다. 그런데 과인은 무엇을 얻었는가."; 을지문덕 nhìn ra cửa mở, mưa trên 대동강: "내년에 또 올 것이오."; vua không quyết — "내년에 다시 묻겠다." Salsu nắng (D+10), nước rút: 박기철 chống nạng đặt biển 천둥 3 lên xác K2, ngồi trên thân xe với sổ tay; 한승우 nhìn xe; 오태민, 태오 trên ngựa, 서아, 백성민, 을보, 아리 phía sau: "이제 우리는 뭡니까?" — không ai trả lời. Narrator đọc câu cuối bài thơ: 知足願云止. Hình cuối: xe bò kéo K21 về tây trong mưa, hộp sơn mài đựng drone trên đùi người đánh xe. End card 「살수 612 — 끝」 → 「다음: 613」.
> Chức năng: OPEN (series 2 「613」 — decisions P-18: 3 dây: công nghệ về 낙양 · 뇌군 thuộc về ai · 613) · Tài nguyên: 0 mọi thứ — "여든 명의 농부" · Quyết định sử: 영양왕 hoãn (không quyết = quyết định nhìn thấy được) · Anti-copy: không tableau "2 chỉ huy trên tường → lều địch → card"; kết bằng câu hỏi của đại đội + hình xe bò · Open loop series: "내년에 또 올 것이오." — "이제 우리는 뭡니까?"

### SC_273 · LOC_001_YOHA (KB, Tùy rút qua cầu phao trong mưa) · — · VEH_205, PROP_021 · still_kenburns · 37:30–37:40
[ACTION-VI] Ảnh aerial mưa: ba cầu phao trên 요하 — dòng quân Tùy đi ngược về tây, cờ rũ, xe lương trống; bờ đông, 요동성 đá xám đứng nguyên với cờ 삼족오; lều Tùy đang được dỡ thành từng mảng trống trên đồng. Ken-burns từ 요동성 kéo về cầu phao.
[SOUND] mưa, bánh xe gỗ, trống chậm.
N: 7월 말, 황제는 전군을 돌렸습니다. 남은 대군이 요하를 건너 돌아갔습니다. 요동성은 넉 달을 버텼습니다. 성은 한 번도 열리지 않았습니다.

### SC_274 · LOC_002_YODONGSEONG (KB 613, tháp công thành) · — · VEH_201, PROP_021 · still_kenburns · 37:40–37:50
[ACTION-VI] Ảnh: 요동성 dưới nắng hè khác — tháp công thành 8 bánh cao hơn tường đang hạ cầu xuống mặt tường, lính Tùy trèo thang mây dưới mưa tên và đá từ 치, một ụ đất khổng lồ đắp sát tường; cờ Tùy mới; góc ảnh xa: một đoàn quân Tùy rút vội trong đêm, đuốc tắt. Ken-burns từ tháp công thành sang đoàn quân rút.
[SOUND] búa, trống, rồi im.
N: 이듬해 613년, 그는 다시 왔습니다. 팔륜누차와 어량대도로 요동성을 다시 쳤습니다. 그해 여름, 후방에서 양현감이 반란을 일으켰습니다. 황제는 밤에 몰래 물러났습니다. 역사에 있는 그대로입니다.

### SC_275 · LOC_004_YUKHAPSEONG (KB 618, 강도 — điện Tùy cuối) · — · PROP_021 · still_kenburns · 37:50–38:00
[ACTION-VI] Ảnh: một điện Tùy phương nam về đêm — cột son, rèm lụa vàng đứt, đèn lồng đổ, cửa mở toang, giáp lính đứng chật cửa, một tấm áo vàng thổ bỏ lại trên sàn. Ken-burns đẩy chậm vào tấm áo. Không mặt người.
[SOUND] gió đêm, rèm lụa, một tiếng kim loại.
N: 614년, 세 번째로 왔습니다. 고구려는 이름뿐인 화의를 주었습니다. 618년, 강도에서 우문술의 아들 우문화급이 황제를 죽였습니다. 수나라는 그렇게 끝났습니다. 살수에서 육 년 뒤였습니다.

### SC_276 · LOC_006_PYONGYANG (nội điện, đêm mưa) · CHAR_102, CHAR_103, CHAR_101 · PROP_012 · video8s · 38:00–38:08
[ACTION-VI] Nội điện 평양 đêm: cột son, ngai đen viền vàng trên bậc thấp, cờ 삼족오 lớn sau ngai, đèn dầu; 영양왕 ngồi — 백라관, long bào đỏ thẫm, không đổi trang phục, mặt không cười; dưới bậc, 고건무 (giáp sạch, không mũ) đứng, 을지문덕 (조우관, áo lụa đỏ nâu) đứng cách một bước; cửa lớn mở ra hiên mưa. 고건무 nói với vua, tay chỉ về phía bắc.
[SOUND] mưa trên ngói, lửa đèn, giọng.
N: 여드레 뒤. 평양. 왕은 이긴 전쟁 앞에서 다른 것을 물었습니다. 보름 전 해모루 편에 보낸 질문이었습니다.
고건무: 쇠를 거두면 저들은 여든 명의 농부입니다.

### SC_277 · LOC_006_PYONGYANG (nội điện) · CHAR_102 · — · video8s · 38:08–38:16
[ACTION-VI] Cận 영양왕 trên ngai: hai tay trên gối, râu cằm dài mảnh, mắt tính toán; ông nói chậm, mỗi câu một cân nhắc — không với ai cụ thể.
[SOUND] lửa đèn, mưa.
N: 30만 5천이 2천 7백이 되었습니다. 그의 땅에는 총 든 여든 명이 있었습니다. 어느 성의 군사도 아닌 자들이었습니다.
영양왕: 이겼다. 그런데 과인은 무엇을 얻었는가.

### SC_278 · LOC_006_PYONGYANG (nội điện, cửa mở) · CHAR_101 · — · video8s · 38:16–38:24
[ACTION-VI] 을지문덕 không trả lời vua ngay — quay người, bước tới khung cửa mở, nhìn ra hiên: mưa đêm trên sân đá, xa dưới đồi là 대동강 xám đen; ông nói với cơn mưa hơn với điện; sau lưng, vua và 고건무 nhìn lưng ông.
[SOUND] mưa to hơn ở cửa, gió.
N: 을지문덕은 문 쪽으로 갔습니다.
을지문덕: 내년에 또 올 것이오.

### SC_279 · LOC_006_PYONGYANG (nội điện) · CHAR_102, CHAR_103 · — · video8s · 38:24–38:32
[ACTION-VI] 영양왕 nghe câu đó, nhìn lưng 을지문덕, rồi nhìn 고건무 đang chờ lệnh thu vũ khí; ông đặt tay lên tay vịn ngai, không đứng dậy; nói — hoãn, không quyết; 고건무 mím môi, cúi đầu.
[SOUND] lửa đèn, mưa, tay trên gỗ.
N: 왕은 결정하지 않았습니다. 그것도 결정이었습니다. 두면 누구의 군대인지 모를 여든 명이었습니다.
영양왕: 그 군사들은… 내년에 다시 묻겠다.

### SC_280 · LOC_006_PYONGYANG (KB cửa điện mở, hiên mưa) · — · — · still_kenburns · 38:32–38:40
[ACTION-VI] Ảnh: từ trong điện nhìn ra khung cửa gỗ mở — hiên đá ướt, mưa xiên qua ánh đèn, sân trống, xa là bóng tường thành và sông; không người trong khung. Ken-burns đẩy chậm ra cửa.
[SOUND] mưa, gió.
N: 그 군사들은 평양에 오지 않았습니다. 왕도 살수에 가지 않았습니다. 두 사람은 끝내 만나지 않았습니다. 사이에 해모루가 있었고, 해모루는 아직 누워 있었습니다.

### SC_281 · LOC_007_SALSU (cổng họng bãi, nắng, nước rút) · CHAR_001 · VEH_001 · video8s · 38:40–38:48
[ACTION-VI] Salsu mấy ngày sau, nắng: nước đã rút — bãi cát lộ rộng, cổng họng chỉ còn một lạch nông; K2 nằm nghiêng 10° trong cát, thân đen sém, nửa thân chìm bùn khô nứt, nòng hạ, nắp cupola mở, tên gãy cắm nóc, 태극기 nhỏ hé dưới bùn; 한승우 đứng trên cát, mũ cầm tay, tóc khô, bùn xám khô trên áo, nhìn xe. Máy sau lưng ông, rồi ngang.
[SOUND] gió, chim sông, nước lạch nhỏ.
N: 열흘 뒤. 물이 빠졌습니다. 강은 다시 무릎이었습니다. 을보 영감의 말대로 화가 풀린 강이었습니다. 이제 아무도 전차를 가져갈 수 없었습니다.

### SC_282 · LOC_007_SALSU (xác K2) · CHAR_003 · VEH_001, PROP_023 · video8s · 38:48–38:56
[ACTION-VI] 박기철 chống nạng (cây giáo Goguryeo gãy) lết lên thân K2 nghiêng, ngồi xuống mép tháp cháy đen, đặt tấm biển thép nhỏ PROP_023 (số "3" trắng) xuống cạnh số "1" trắng còn hé dưới bùn khô — hai số cạnh nhau (không vẽ chữ Hangul); ông mở sổ tay bọc nilon trên đùi, bút chì, nhìn trang cuối, viết một chữ số, nói khô. Cận tay rồi mặt.
[SOUND] nạng trên thép, thép nhỏ đặt lên thép, giấy, gió.
N: 박기철은 이름표를 올려놓았습니다. 장갑차의 이름을 가라앉은 전차 위에. 천둥 1호와 천둥 3호가 나란히 있었습니다. 공책의 마지막 장을 펼쳤습니다.
박기철: 영입니다. 전부 영.

### SC_283 · LOC_007_SALSU (bãi cát, trước xác K2) · CHAR_001, CHAR_002, CHAR_005, CHAR_004, CHAR_006, CHAR_106, CHAR_107 · VEH_001, VEH_101 · video8s · 38:56–39:04
[ACTION-VI] Wide: 한승우 đứng trước xác K2; phía sau ông một hàng: 오태민 (băng bắp tay, không kính bảo hộ), 태오 trên lưng ngựa Goguryeo với mũ trụ sắt trong tay, 서아 (bím tóc, băng chữ thập rách), 백성민 (boonie, dắt ngựa), 을보 (thanh sắt), 아리 (khăn olive); nắng, gió; 한승우 không quay lại, hỏi — không to.
[SOUND] gió, ngựa thở, chim.
한승우: 이제 우리는 뭡니까?

### SC_284 · LOC_007_SALSU (bãi cát, hàng người) · CHAR_002, CHAR_005, CHAR_004, CHAR_006, CHAR_106, CHAR_107 · VEH_001 · video8s · 39:04–39:12
[ACTION-VI] Máy lướt chậm qua từng mặt trong hàng: 오태민 nhìn xe, quai hàm bạnh; 태오 nhìn mũ trụ trong tay; 서아 nhìn về phía lau nơi 해모루 nằm; 백성민 nhìn dòng nước; 아리 nhìn 서아; 을보 bước lên, đặt bàn tay lên tấm giáp cháy của K2 — vuốt một cái. Không ai trả lời. Gió.
[SOUND] gió, tay già trên thép, im.
N: 아무도 대답하지 않았습니다. 총 없는 군인. 성 없는 군사. 왕이 아직 묻지 않은 여든 명. 그 답은 내년의 것이었습니다.

### SC_285 · LOC_006_PYONGYANG (KB cuộn thơ) · — · PROP_014 · still_kenburns · 39:12–39:22
[ACTION-VI] Ảnh cận: cuộn lụa bài thơ 여수장우중문시 mở trên bàn thấp dưới đèn dầu — bốn cột chữ Hán brush calligraphy, mực đã khô, mép lụa sờn; ngón tay già đặt dưới cột chữ cuối. Ken-burns trượt dọc cột chữ cuối. (Edit: overlay subtitle 知足願云止 + dịch Hàn khi narrator đọc.)
[SOUND] lụa, lửa đèn, nhạc trầm.
N: 知足願云止. 족함을 알고 그만두기를 바라노라. 을지문덕이 우중문에게 보낸 마지막 줄이었습니다. 수나라는 족함을 몰랐습니다. 613년에도, 614년에도. 그리고 618년에 끝났습니다.

### SC_286 · LOC_001_YOHA (KB đường về tây, mưa) · 소달구지꾼, 선비 기병 · VEH_002 (천둥 3 bị thu), UAV_001 (hộp) · still_kenburns · 39:22–39:34
[ACTION-VI] Ảnh wide: con đường đất lầy về tây trong mưa xám, đồng cỏ vàng ướt — bốn mươi con bò kéo cỗ xe khổng lồ chở khối bọc thép phủ vải dầu, cờ Tùy nhỏ trên vải; kỵ Tiên Ti hộ tống thưa thớt; cỗ xe nhỏ dần về chân trời tây. Ken-burns kéo ra rất chậm.
[SOUND] mưa, bánh xe gỗ, bò rống xa.
N: 그리고 서쪽으로 가는 수레가 하나 있었습니다. 낙양까지 삼천 리. 안에는 기름 없는 쇠수레 한 대. 수나라는 그것을 열어 볼 것이었습니다. 무엇을 배울지는 아직 아무도 몰랐습니다.

### SC_287 · LOC_001_YOHA (cỗ xe, cận) · 소달구지꾼 · UAV_001 (hộp sơn mài) · video8s · 39:34–39:42
[ACTION-VI] Cận: trên đùi người đánh xe bò Tùy áo vải ướt, một hộp sơn mài đen bóng mưa, nắp buộc dây lụa vàng; bàn tay chai của anh ta đặt lên nắp hộp, ngón cái vô thức xoa lớp sơn; mưa gõ trên nắp; anh ta nhìn xuống hộp một cái, rồi nhìn đường. Máy tĩnh.
[SOUND] mưa trên sơn mài, bánh xe, bò.
N: 옻칠한 상자 안에 쇠새가 잠들어 있었습니다. 건전지는 죽었습니다. 날개는 남았습니다. 낙양까지 남은 길은 아직 멀었습니다.

### SC_288 · [END CARD] · — · — · still_kenburns · 39:42–39:52
[ACTION-VI] Đen. Chữ trắng giữa khung: 「살수 612 — 끝」. Không hình khác.
[SOUND] mưa trên nắp hộp còn vọng 3 s trong đen, rồi im.

### SC_289 · [END CARD] · — · — · still_kenburns · 39:52–40:00
[ACTION-VI] Đen. Chữ trắng nhỏ hơn, giữa khung: 「다음: 613」. Không hình khác.
[SOUND] im tuyệt đối; giây cuối: một hồi tù và Goguryeo rất xa.

[END CARD]

[Kết thúc Phần 12]


---

## 부록 — THỐNG KÊ & TỰ KIỂM (ngoài phần kịch bản · script-writer · 2026-09-16 · 5화 v2.1 TTS-trimmed)

### A. Thống kê (script đếm tự động `logs/scratch/script-writer-ep5/stats.py`: SC theo header `### SC_`, narration = dòng `N:`, thoại = dòng `TÊN:`; 어절 tách theo khoảng trắng; câu N tách theo dấu chấm)
| Phần | Phút (outline) | SC | video8s | still_kenburns | Giây | Dòng N | Câu N | 어절 N | Câu thoại | 어절 thoại |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–1:30 | 11 | 9 | 2 | 90 | 7 | 28 | 122 | 4 | 22 |
| 2 | 1:30–4:30 | 20 | 14 | 6 | 180 | 20 | 85 | 369 | 13 | 65 |
| 3 | 4:30–7:00 | 18 | 15 | 3 | 150 | 18 | 58 | 280 | 11 | 53 |
| 4 | 7:00–10:30 | 26 | 23 | 3 | 210 | 23 | 76 | 331 | 14 | 57 |
| 5 | 10:30–14:00 | 26 | 25 | 1 | 210 | 11 | 34 | 150 | 13 | 33 |
| 6 | 14:00–17:30 | 25 | 21 | 4 | 210 | 24 | 76 | 335 | 18 | 81 |
| 7 | 17:30–21:00 | 26 | 25 | 1 | 210 | 21 | 60 | 258 | 10 | 34 |
| 8 | 21:00–24:00 | 22 | 19 | 3 | 180 | 21 | 67 | 339 | 12 | 57 |
| 9 | 24:00–27:30 | 25 | 21 | 4 | 210 | 25 | 84 | 389 | 15 | 87 |
| 10 | 27:30–34:30 | 52 | 51 | 1 | 420 | 28 | 98 | 410 | 14 | 39 |
| 11 | 34:30–37:30 | 21 | 17 | 4 | 180 | 21 | 90 | 372 | 10 | 39 |
| 12 | 37:30–40:00 | 17 | 9 | 8 | 150 | 14 | 58 | 249 | 6 | 26 |
| **Tổng** | 0:00–40:00 | **289** | **249** | **40** | **2400** (= 40:00) | **233** | **814** | **3601** | **140** | **593** |
| **Combat KHỐI (giây / %)** | — | — | — | — | **880 s = 36,7 %** | P2 sử 16 · P3 sử 16 · P4 24 · P5 200 · P6 24 · P7 168 · P8 8 · P9 8 · P10 408 · P11 sử 8 | | | |
| **Combat THUẦN (giây / %)** | — | — | — | — | **648 s = 27,0 %** | chỉ SC có giao chiến/hỏa lực/truy đuổi nhìn thấy (loại SC đếm, nhìn, radio, phản ứng bên trong khối) | | | |

- **Câu vi phạm:** thoại >12 어절: **0**/140 (dài nhất 11) · narration >15 어절/câu: **0**/814 · **TTS budget (tools/tts_budget.py): 0 SC vượt (video8s ≤22, still 10 s ≤37) · 4.194 어절 / 40:00 = 104,8 어절/phút (≤115)** · SC có >1 câu thoại: 0 · lỗi nối thời gian: 0 · video8s ≠ 8 s: 0 · still ngoài 6–12 s: 0.
- **Phân bổ thoại:** 박기철 30 · 오태민 15 · 해모루 13 · 한승우 11 · 태오 10 · 우문술 8 · 을지문덕 6 · 을보 6 · 사수 6 · 우중문 4 · 아리 4 · 탁발흠 4 · 서아 4 · 수 후군 장수 3 · 백성민 3 · 양제 2 · 영양왕 2 · 고건무 1 · phụ 8 → hiện đại 59 % / Goguryeo 24 % / Tùy 17 %.
- **Khối action (10):** SC_017–018 [史] kỵ Goguryeo bám 방진 · SC_046–047 [史] hậu quân giao tranh bờ nam · SC_069–071 kỵ hai bờ vào hậu quân · SC_076–100 (6 viên, cối, PZF, 신세웅) · SC_114 + 121–122 tiền quân ép rìa nam · SC_127–147 kỵ Tiên Ti xông lau · SC_169 (v2: đứng giữa SC_164–165) · SC_190 · SC_200–250 (6 phase) · **SC_252 [史] truy kích 압록수 (v2, +8 s)**. Khoảng không action dài nhất trong thân tập: 2:34→6:24 (3:50). Sau 34:38 là aftermath (P11–P12) — còn 1 still sử 613 (SC_274) có hình giao chiến (decisions P-47: chấp nhận).
- **Vùng im narrator:** 0:00–0:32 (narrator vào 0:32 "612년 7월. 살수.") · **10:38–12:30** (SC_077–090, 112 s) · **18:18–18:50** (SC_133–136, 32 s) · **31:30–33:22** (SC_230–243, 112 s) + Phase 5 chỉ 1 câu N ở 33:22 rồi im tới 34:10. Sau mỗi mid-roll: 1 SC không thoại (SC_050 · SC_102 · SC_153 · SC_200). 30 s đầu: **8 shot** (v2: SC_001 2-BEAT · SC_002 2-BEAT · SC_003 2-BEAT · SC_004 2-BEAT). 2-BEAT dùng 25 lần, chỉ ở hook + trận (P1 ×4, P5 ×6, P7 ×1, P10 ×14 — v2 thêm SC_208/211/220/223).
- Mid-roll: 7:00 · 14:00 · 21:00 · 27:30 (đúng outline; không mid-roll 5 — decisions P-46).

### B. Tự kiểm 7 mục
1. **ID trong bible:** CHAR_001–006, 101, 102, 103, 105, 106, 107, 201, 202, 203, 205 ✓ · LOC_001/002/004/005/006/007 ✓ · VEH_001/002/101/205 (chỉ SC_273)/206 ✓ · UAV_001 (hộp) · EQP_001/002 ✓ · WPN_001/002/003/004/005/101/201 ✓ · PROP_001/006/008/009/011/012/014/017/018/019/020/021/023 ✓. **ID mới (v2, chờ bible + lock — proposals P-50):** `VEH_207` kỵ binh/ngựa chiến Tùy (21 SC) · `PROP_024` 붉은 신호기 (8 SC) · `PROP_025` 소이수류탄 (5 SC). Ghi kèm không ID: giáo 삭 → `VEH_101 (giáo 삭 của 개마무사)`, cung Tiên Ti → `VEH_206 (cung Tiên Ti)`, nút bầu gỗ (P-43 → PROP mới), cờ hiệu nhỏ 해모루 (PROP_012 biến thể). 수 후군 장수 = EXTRA (P-44); tên 신세웅 1 lần (SC_091 N). Nhân vật phụ không ID: xem header.
2. **Thời gian khớp outline:** 12/12 phần đúng mốc phút, tổng 40:00, không đứt quãng; P10 6 phase: 27:30–28:42 · 28:42–29:54 · 29:54–31:30 · 31:30–33:22 · 33:22–34:10 · 34:10–34:30. v2: SC_169 dời vào 22:38–22:46 (SC_165–168 lùi 8 s tới 23:20, giữ ID); SC_252 video 8 s (34:30–34:38), SC_259 và SC_266 still 12 s để P11 vẫn kết 37:30. Bảng ngày/đêm ở header nối 4화 (**5화 D1 = 4화 D12**; nước 무릎 → 허리 → 배 → 가슴; radio 40 % → 15 % sau 4 đêm; 천둥 3 tới 육합성 3화 D22).
3. **5 direct quotes nguyên văn:** (1) 박기철 "여섯… 다섯… 넷… 셋… 둘… 하나." SC_078/080/082/084/085/086 + "다 썼습니다." SC_092 · (2) 탁발흠 "쇠수레가 벙어리가 됐다. 지금이다." SC_127 · (3) 한승우 "전차를 여울에 박는다. 마개는 우리다." SC_163 · (4) 을지문덕 "쇠수레가 여울을 막았소. 그대들이 마개였소." SC_261 · (5) 을지문덕 "내년에 또 올 것이오." SC_278 — 한승우 "이제 우리는 뭡니까?" SC_283 ✓. Phụ: 박기철 "탄창 비었습니다." SC_247 · N "30만 5천 명 중 2천 7백 명이 요동성으로 돌아갔습니다." SC_252 · 양제 "…내년." SC_271 · 탁발흠 "여섯. …그리고 조용하다." SC_100 · 우문술 "뇌군이다. 저놈들이 여울을 막고 있다." SC_112 + "뚫어라." SC_113 · 해모루 "한 명도 북으로 올라오지 못하게 하시오." SC_105 · 오태민 "빈 전차가 뭘 합니까?" SC_115 · 박기철 "오십오 톤입니다." SC_116 · "연료 이십 킬로. 여울까지 삼백 미터. 남는 건 다 태워도 됩니다." SC_159 · "제가 몹니다. 십 년 몰았습니다." SC_166 · **고건무 "쇠를 거두면 저들은 여든 명의 농부입니다." SC_276 (v2 — quote outline P12 "총이 없으면" đổi theo decisions, ghi proposals)** · 을보 "가슴까지 왔소." SC_044 · v2 thêm: 박기철 "도하 준비 없이 일 점 이 미터. 가슴이면 아슬아슬합니다." SC_197 → "물이 껐습니다. 여울 목. 정지." SC_206 · 해모루 "창은 말을 세우오. 그대들 쇠는 사람을 세우시오." SC_182. 12 open loop cuối phần đúng câu outline ✓ (P5 = câu 탁발흠).
4. **0–30 s không narration:** ✓ (SC_001–004, 8 shot, chỉ SFX + 1 chữ thì thầm "여섯").
5. **≤12 어절/câu thoại:** 0 vi phạm. Narration ≤15 어절/câu: 0 vi phạm. Không dùng "그러나 그들은 몰랐습니다". Narrator không giải thích công nghệ (v2: bỏ "삼천 도"). Narrator không nói trước/lặp thoại (v2: SC_116/120/150/155/206/278 sửa).
6. **Ràng buộc nội dung:** K2 đúng 6 viên đầu tập (SC_008) → 0 (SC_086/092/093) · Salsu là kế 을지문덕, đại đội là nút chai (SC_019/029/031/208/261) · **나각 3 hồi trả trọn: 을지문덕 (P5) → 해모루 (SC_208) → 을지문덕 hạ kiếm (SC_211)** · 우중문 bị bắt sống, không giết (SC_236–237, 263–264; narrator nói rõ sử gốc — SC_263 "옥에 갇혔다가 병들어 죽었습니다") · 우문술 sống, để tiền quân chạy (SC_239), bị xiềng [史] (SC_267) · 탁발흠 chết trên nóc K2 cháy bởi tên 해모루 đúng lúc "탄창 비었습니다" (SC_247–249); tay phải băng (4화) run — chậm nửa nhịp (SC_245) · 오태민 giữ bờ bắc (SC_170, 240–241, 250) · 백성민 dẫn 300 kỵ qua mô cát (SC_230–231) · 서아 cứu 해모루 — **tên dưới xương đòn trái, băng chéo ngực (theo bible)** (SC_234/243/248/255) · 박기철 đếm cuối, lái xe, nói giới hạn 1,2 m (SC_197), **sông tắt máy** (SC_206), tên vào chân, chống nạng, không mất chân (SC_219, 258, 282 — P-05) · **Phase 3 là sai lầm thật của 한승우** (SC_216/222 "불보다 사람을 먼저 세었습니다") · K2 sắt vụn chìm bùn (SC_251, 259, 281) + biển 천둥 3 (SC_282) · 94→80 (SC_148 91→86 · SC_253 80) · 0 drone (SC_010) · không nhân vật có tên chết · 태오 mũ trụ Goguryeo — mũ Hàn về từ 석문령 nhưng đưa cho xạ thủ mất mũ, kính không về (SC_042, decisions 4화 phương án B), trực radio, sau đó trên ngựa (SC_007, 283) · 해모루 radio chết D−3 → ông phi ngựa vào (SC_025, 103, 120) · kính đêm vỡ treo cổ 탁발흠 → rơi sông cùng hắn (SC_060, 249) · 태극기 của 태오 trôi (SC_249) · nút bầu (SC_027–028, 165, 195) · lựu đạn nhiệt nhôm 3화 = PROP_025 (SC_161, 224) · ngựa bịt tai 3화 (SC_128–129) · 을지문덕 chạm K2 2화 → hôm nay không chạm (SC_260) · 양제 có 천둥 3 trong sân 15 ngày không chạm → chạm khi tin thảm bại tới (SC_270–271) · 영양왕 không gặp 한승우 (SC_280 nói thành lời) · K21 + drone về 낙양 (SC_286–287) · 양제 "내년" (SC_271) · [END CARD] 「살수 612 — 끝」 → 「다음: 613」 · không dùng đập nước — mưa dầm + nước lên (SC_012, 064, 191) · không nhắc Bắc Triều Tiên, không khẩu hiệu · 시호: 0 lần trong thoại người đương thời · "총" trong miệng Goguryeo: 0 (v2) · P-11: Tùy ↔ đại đội không đối thoại; 을지문덕 ↔ 우중문 trực tiếp (thạo Hán văn).
7. **Anti-copy:** trình tự tập = chờ → đếm cuối → 5만 đi qua mũi súng → cờ đỏ → 6 con số → chính trị giữa trận → kỵ binh xông được vào súng máy → hết đạn → quyết định chôn xe → xe xuống sông làm vật cản, sông tắt máy → kẻ săn chết trên xe bởi tên → 2.700 (truy kích [史]) → 경례 → 양제 chạm K21 → "내년" → hội đồng vua hoãn → "뭡니까" → xe bò. Không tableau "2 chỉ huy trên tường → lều địch → card" (QC xác nhận: hai beat §17 có mặt nhưng đảo thứ tự, trong điện, chèn câu hỏi đại đội, hình cuối = công nghệ rò rỉ). Xe tăng không thắng trận — bị chôn để tổ tiên thắng.

### C. Nhật ký diễn giải ngoài outline (v1, giữ; QC đã rà — mục 6 đã đổi theo decisions)
1. **Địa hình LOC_007 chi tiết hóa:** cổng họng bãi rộng 60 m giữa bãi lau (tây) và bờ bùn dốc (đông); K2 cách cổng họng 300 m (SC_021); mô cát nhỏ cách K2 30 m (Phase 3–5); mô cát thượng lưu 1,5 km về đông, nước tới bụng ngựa (SC_026); **v2:** K2 trượt 3 km từ đảo lau thứ hai (4화) xuống bãi lau cửa bãi **hai đêm trước** (SC_057) — vết xích còn trong bùn. → proposals P-41.
2. **Radio 해모루 chết D−3** (SC_025 "사흘째") → ông phi ngựa vào lau (P6); câu 태오 outline "장군 쪽 무전 안 잡힙니다. 배터리 10%." viết thành "말객님 무전기는 죽었습니다. 우린 십 퍼센트." (SC_120). Pin máy chính: 40 % (4화) → 15 % (SC_010, "나흘 밤을 켜 둔 값") → 10 % → 5 % (SC_155) → chết (SC_178) → 나각/cờ tay (SC_180).
3. **해모루 mang 100 giáo dài** vào lau (SC_103), 300 kỵ ở lại với 백성민 + 고구려 부장; Phase 4 dẫn 50 giáo ra mép nước (SC_233), 50 ở lại tuyến 오태민 (SC_240).
4. **"Sai sót" Phase 3 = sai lầm thật của 한승우** (v2): ông đếm người trước lửa (SC_216 "그는 순서를 정했습니다. 사람 먼저."), 박기철 trúng tên khi trượt khỏi mũi xe → kéo lên mô cát → **quay lại xe dưới tên** để thả nhiệt nhôm (SC_222 "그것이 그의 실수였습니다…"). Lựu đạn cài trên ngực áo giáp từ P9 (SC_189).
5. **탁발흠 giữ cung trên lưng** suốt P7–P10 (SC_124) để có cung giương trên nóc xe (SC_245) — decisions P-39 DUYỆT; v2 thêm băng cẳng tay **phải** (vết dao 백성민 4화 v2) ở SC_060/245.
6. **Vết thương 해모루** — v2 theo BIBLE: mũi tên dưới xương đòn trái (kỵ xạ Tiên Ti bắn 15 m — "người bị tên bắn tên"), băng chéo vai–ngực ở P11.
7. **Quyết định sử thêm** (cùng chiều sử): 을지문덕 không chia kỵ (SC_111); lệnh toàn quân đánh đuôi khi nút chai xuống (SC_185) — **v2 có cò thật: 나각 3 hồi của 해모루 → ông hạ kiếm (SC_208/211)**; 우문술 hạ kiếm để tiền quân chạy (SC_239); 영양왕 hoãn thành lời (SC_279); 우중문 đứng giữa sông với cờ (SC_016/063).
8. **K5 열다섯** nói thành lời ở P3 bởi 박기철 (SC_040) + narrator SC_138.
9. **Mini-combat [史] P2/P3** (kỵ Goguryeo bám 방진 bốn mặt; hậu quân giao tranh mép nước); **v2: SC_252 video [史] truy kích tới 압록수, 왕인공 chặn hậu** (P-47 DUYỆT).
10. **Morphine:** ống đầu tiên dùng cho 해모루 (SC_255 "여덟 개 중 첫 번째"), số còn lại dùng trong đêm cho ~25 thương binh (SC_253 v2 "스물다섯") → ledger cuối 5화 = 0; K6: tổ bị tràn, súng đổ, đạn còn nằm trong bùn (SC_133).
11. **Thoại phụ thêm** (140 câu): 고구려 기병 장교 ×2, 수 부장 ×2, 척후 선비, 고구려 궁수 장교, 고구려 부장, 병사, 수 후군 장수 ×3.
12. **Timeline epilogue (v2 nối 3화/4화):** 육합성 D+5 (tin đi 450리 + 요동 ~3 ngày; 천둥 3 đã tới từ 3화 D22 — "보름 전", kéo "스무 날" từ 요동성 골짜기), 평양 D+8 ("보름 전" câu hỏi của vua = 4화 D3), 살수 D+10 (nước rút), Tùy rút cuối 7월 [史] ("남은 대군").
13. **을지문덕 "내년에 또 올 것이오"** từ khung cửa điện 평양 nhìn ra mưa/대동강 (gộp outline + foundation).
14. **Narrator P11 nêu 왕인공 chặn hậu, 내호아 rút** [史] — 1 câu mỗi tên; v2 SC_263 우중문 sử gốc "옥에 갇혔다가 병들어 죽었습니다" (수서: chết ở nhà sau khi được thả vì bệnh — story_bible §3 cần sửa cùng câu).
15. **Số viết bằng chữ Hàn trong thoại** (이십 킬로, 삼백 미터, 오십오 톤, 십 퍼센트, 일 점 이 미터) để TTS đọc đúng; narrator giữ số Ả Rập kiểu 1화.
16. **Chữ trên prop:** biển tên 천둥 3 chỉ số "3" (PROP_023), số "1" trên K2 — không vẽ Hangul; bài thơ hiện subtitle 知足願云止 + dịch Hàn ở edit (SC_285).
17. **Post-mid-roll:** SC_050 (khiên trên đầu, mưa dày) — hình mạnh, không thoại.

### D. Tự chấm 18 chỉ số benchmark (docs/benchmark_vs_reference.md) — 5화 v2
| # | Chỉ số | Mục tiêu | 5화 v2 | Kết luận |
|---|---|---|---|---|
| 1 | Giây đầu có nguy hiểm/câu hỏi | ≤ 0:10 | **0:03** chân lính Tùy xuống nước; 0:20 "여섯" | ✅ |
| 2 | Shot trong 30 s đầu | ≥ 5 | **8** (4 SC 2-BEAT — v2) | ✅ (gốc 13 — vẫn thua gốc) |
| 3 | Narrator 30 s đầu | 0 | **0** (vào 0:32) | ✅ |
| 4 | Lần giao tranh đầu | ≤ 7:00 | Sử: **2:18** (SC_017) · đại đội bóp cò: **10:46** (SC_078) | ✅ sử · ⚠️ đại đội 10:46 (cố ý theo kế "nửa"; veo/edit giữ nhịp bằng contact/threat P4) |
| 5 | Combat/runtime (2 số) | ≥ 35 % | **KHỐI 36,7 %** (880 s, 10 khối) · **THUẦN 27,0 %** (648 s) | ✅ khối (gốc 45 %) · ⚠️ thuần <35 % — ghi 2 số theo decisions 4화 |
| 6 | Khoảng cách tối đa 2 beat retention | ≤ 4' | Beat mạnh ~2:00; không action dài nhất trong thân: 3:50 (2:34→6:24); aftermath 34:38→40:00 có 1 still sử | ✅ |
| 7 | Con số tài nguyên nói thành lời | ≥ 6 | **≥ 34 câu thoại có số** (v1 + "일 점 이 미터", "십오 퍼센트… 날마다") + N: 2천 7백 · 450리 · 여든 · 열넷 · 스물다섯 | ✅ HƠN xa |
| 8 | Enemy POV | ≥ 5 cảnh, địch có tên & học | **~45 SC**; 탁발흠 nói bài học 3 lần (SC_061/100/127), áp dụng: bịt tai (128), không đánh thẳng (147), chọn xe thay trận (210) → chết vì bài học cuối; v2: giá của 4화 (tay phải băng) trả đúng lúc chết (SC_245); 양제 kiên nhẫn 15 ngày không chạm xe (SC_270) | ✅ HƠN |
| 9 | Nhân vật lịch sử ra quyết định | ≥ 3 | **13** / 5 người thật: 을지문덕 6 (v2: hạ kiếm trên tín hiệu nút chai SC_211) · 우문술 3 · 우중문 2 · 영양왕 1 · 양제 1 | ✅ HƠN |
| 10 | Số câu thoại | 120–160 | **140** (hiện đại 59 % · Goguryeo 24 % · Tùy 17 %) | ✅ |
| 11 | Thoại > 12 어절 | 0 | **0** | ✅ |
| 12 | Quote đắt | ≥ 5 | **≥ 14** (mục B.3; v2 thêm "물이 껐습니다", "그대들 쇠는 사람을 세우시오") | ✅ HƠN |
| 13 | Shot trung bình | 8–10 s | **8,3 s** (2400/289); P10: 8,1 s danh nghĩa, 14 SC 2-BEAT → ~6,9 s hiệu dụng | ✅ khung · ❌ gốc 4 s trong trận (veo-stage two-beat thêm ~12 clip Phase 1–3 — QC NOTE) |
| 14 | Kết mở | có + gieo series 2 | 12/12 open loop; series 2 「613」 3 dây (SC_270/286/287 · SC_276–280 · "내년" ×3); end card 「다음: 613」 | ✅ |
| 15 | Mid-roll sau open loop | 4 | 7:00 · 14:00 · 21:00 · 27:30, mỗi điểm sau open loop + 1 SC không thoại | ✅ |
| 16 | Yếu tố riêng | hậu cần · bỏ xe · để địch đi qua · địch có tên | 6/6 (v2: giới hạn K2 nói thành lời rồi trả ngay — sông tắt máy) | ✅ |
| 17 | Lỗi lịch sử cứng | 0 | **0**; v2 sửa 2 lỗi mềm (우중문 chết ở nhà sau ngục; "113만 về" → "남은 대군"); 시호 0; điểm rẽ [虛] narrator nói rõ (SC_263, 269) | ✅ |
| 18 | Trình tự giống kênh gốc | KHÔNG | KHÔNG (mục B.7; QC xác nhận không BLOCK) | ✅ |

**Kết luận tự chấm v2:** thua gốc ở #2 (8 < 13), #13 (8 s vs 4 s trong trận — giao veo-stage), #5 combat thuần 27 % (khối 36,7 % đạt); biên ở #4 (đại đội bóp cò 10:46 — cố ý); hơn gốc ở #7/#8/#9/#12/#14/#16.

### E. Nhật ký v2 (QC-fixed) — áp dụng logs/qc_ep5_script.md theo decisions.md "sau QC 5화 → v2"
- **BLOCK ID:** `VEH_205` (cầu phao) → `VEH_207` (kỵ binh/ngựa chiến Tùy) ở 21 header (SC_006/015/016/018/047/052/062/063/064/070/072/079/081/091/094/112/113/214/236/237/239); giữ VEH_205 chỉ ở SC_273. Cờ đỏ hiệu lệnh → `PROP_024` (SC_004/019/020/066/075/111/184 + SC_211). Lựu đạn nhiệt nhôm → `PROP_025` (SC_161/189/213/222/224). Giáo 삭 → `VEH_101 (giáo 삭…)` (SC_103/142/181/182/211/233/240/250/258); cung Tiên Ti → `VEH_206 (cung Tiên Ti)` (SC_212/245).
- **FIX 해모루 (bible):** SC_234 (kỵ xạ bắn 15 m — tên dưới xương đòn trái) · SC_243 (ép quanh cán tên, không rút) · SC_248 (cán tên vẫn cắm, tay trái giữ cung run) · SC_255 (tên đã rút, băng chéo vai trái–ngực). Lái xe K2 → "vai phải" (SC_139/140).
- **FIX 신세웅 → "수 후군 장수"** (nhãn thoại SC_018/047/070; header 4 SC; N SC_014/018/070/266); tên giữ 1 lần SC_091.
- **FIX nối 4화:** SC_012 "열이틀 전 … 무릎 / 나흘 전 허리" · SC_044 "나흘 전에는 허리" · SC_191 "열흘 동안" · SC_053 "열이틀 전에도 … 이 강가에서" · SC_276 "보름 전" · SC_057 "이틀 전 밤 … 삼 킬로 … 여울 목에서 삼백 미터" · SC_023 "산길 기준, 박기철의 셈이었습니다" (dầu phương án A) · SC_161 "한 달 전 … 천둥 3호는 지금 요동의 황제 앞에" · SC_168 "한 달 동안" · SC_270 N + [ACTION] (xe đã tới 15 ngày, "스무 날", 양제 không chạm) · SC_271 "보름 동안 만지지 않았습니다. 오늘 만졌습니다." · SC_010 N "나흘 밤을 켜 둔 값" + 태오 "무전기, 십오 퍼센트. 날마다 말라갑니다." · SC_042 N mũ 태오 theo decisions 4화 (mũ Hàn về, kính không; mũ đưa cho xạ thủ) · header bảng ngày: dòng "Nối 4화", D−3/D−2/D−1, D+5.
- **FIX "총" → "쇠":** SC_182 해모루 "그대들 쇠는 사람을 세우시오" · SC_276 고건무 "쇠를 거두면 저들은 여든 명의 농부입니다" (quote outline P12 → proposals).
- **FIX narrator:** SC_225 bỏ "삼천 도" (nhìn từ mắt Tiên Ti) · SC_116/120/150/155/206/278 bỏ câu nói trước/lặp thoại · SC_263 우중문 "옥에 갇혔다가 병들어 죽었습니다" · SC_273 "남은 대군이".
- **FIX hình:** SC_242 kết trước khi tới 해모루 · SC_220/223 2-BEAT jump cut (30 m nước ngang ngực) · SC_260 bắt đầu trên mô cát · SC_169 dời vào giữa SC_164–165 (22:38–22:46; SC_165–168 lùi 8 s; giữ ID) · SC_252 KB → video [史] truy kích 압록수 (SC_259/266 still 12 s bù 4 s).
- **Hay-hơn đã duyệt:** #1 SC_216/222 Phase 3 = sai lầm thật ("불보다 사람을 먼저 세었습니다") · #2 SC_197 박기철 "도하 준비 없이 일 점 이 미터…" → SC_206 nước qua lưới hút gió, động cơ sặc tắt, "물이 껐습니다. 여울 목. 정지."; "가자, 이놈아" dời sang SC_204 · #3 SC_208/211 2-BEAT 나각 3 hồi → 을지문덕 hạ kiếm · #4 SC_270–271 양제 15 ngày không chạm xe · #5 SC_252 video · #7 SC_060/245 băng tay phải 탁발흠 run · #8 SC_002/004 2-BEAT (8 shot/30 s) · #9 SC_169 dời.
- **NOTE ≤1 dòng:** SC_130 "쏘는 것보다 맞는 것이 빠른 거리" · SC_015 "수레는 버려라" · SC_060 N "이 강가의 갈대… 갈대를 떠나지 않는 자들" · SC_151 "탄창이 하나… 나머지는 이미 나뉘어" · SC_253 "스물다섯은 다쳤습니다" · SC_204 "삼십 초" · SC_227 giọt sắt lỏng + N "쇳물 한 방울이 기름 위에" · SC_009 "(tên sượt đêm cứu 태오, 4화)" · header ghi chú veo (VEH_205, two-beat Phase 1–3).
- **Không làm (ngoài phạm vi script):** 4화 SC_283–284 "이틀 뒤" → "며칠 뒤" (script-writer 4화) · bible/ledger v3 (character-designer/world-designer): VEH_207 · PROP_024 · PROP_025 · PROP nút bầu · `CHAR_205_final_ep5` bow slung · `CHAR_105_wounded_ep5` mốc P10 Phase 4 → P12 · story_bible §3 우중문 · ledger 5화 cuối (P-40).

### F. Nhật ký v2.1 (TTS-trimmed) — pass "TTS budget"
- Công cụ: `python3 tools/tts_budget.py projects/SALSU_612/02_script/full_script_ep5.md` — v2: 4.517 어절 / 112,9 어절/phút, **51 SC vượt** (nặng nhất SC_252 44, SC_164 40, SC_270 42/37, SC_197 33, SC_009 33, SC_060 33). v2.1: **0 SC vượt · 4.194 어절 / 104,8 어절/phút**; narration 3.924 → **3.601 어절** (−323, vẫn ≥ 3.500); thoại 140 câu / 593 어절 không đổi.
- Chỉ cắt NARRATION trong 51 SC (SC_007/008/009/010/013/016/020/021/022/026/030/032/037/042/053/057/060/061/063/068/094/103/108/119/129/142/154/158/159/161/164/170/176/180/185/188/197/209/228/252/257/260/263/269/270/271/276/277/279/281/282). Không đổi SC, thời gian, thoại, 12 open loop, quotes, vùng im narrator, 2-BEAT, mid-roll.
- Nguyên tắc cắt: bỏ câu narrator lặp/nói trước thoại trong cùng SC (SC_021 "발로 쟀습니다" · SC_037 "항생제 없음/모르핀 여덟" · SC_129 "말은 놀라지 않았습니다" · SC_257 "붕대는 마지막" · SC_277 "왕은 이겼습니다" · SC_271 "한마디를 했습니다"), bỏ câu mô tả điều hình ảnh đã cho (SC_094 "앞의 오만은 뭍에", SC_158 phương án 오태민, SC_228 "타는 쇠를 보았습니다", SC_281 "모래 속에 반쯤"), bỏ vế bình luận thứ hai (SC_164 câu "요하에서 백성을 위해…", SC_170 "자기 자리를 말했습니다", SC_180 "배우는 데 넉 달", SC_185 "갇힌 물을 치는 것").
- **Nội dung [史] rút khỏi narration (giữ trong [ACTION] hoặc phụ lục):** SC_252 — 왕인공 chặn hậu (còn trong [ACTION-VI] "hàng khiên Tùy nhỏ (천수장군 왕인공)"), 내호아 rút về biển (bỏ hẳn — story_bible §1 có; nếu QC muốn giữ, thêm 4 어절 "내호아는 배를 돌렸습니다" ở SC_266 N còn dư 2 어절 → không đủ); SC_060 "우중문에게 청한 자리였습니다. 여울 북쪽." (đã có ở 4화 P11); SC_061 "갈수록 적었습니다"; SC_270 "소 마흔 마리, 선비 기병 이백" (còn trong [ACTION] SC_286).
- Con số nói thành lời vẫn ≥ 34 câu thoại có số; "2천 7백" ×2 trong SC_252 N; K5/6 viên/30/PZF/băng đạn/5 %/20 km/300 m/55 t/1,2 m nguyên vẹn.
