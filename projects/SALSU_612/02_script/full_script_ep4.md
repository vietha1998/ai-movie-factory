# 살수 612 — 4화 「평양」 대본 v1

> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (238 video8s + 49 still_kenburns 8–12 s) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer
> **Nguồn:** outline_ep4.md (khung 12 phần — chuẩn), series_foundation.md (§7 4화, §8, §8b), story_bible.md ([史] 내호아·고건무·7 trận·thơ·방진; quy tắc 시호), character_bible.md (LOCKED), location_bible.md (LOC_006 + interior, LOC_007), prop_bible.md (PROP_013/014/016/017/018/020/022), vehicle_bible.md, resource_ledger.md (lệch → outline), logs/decisions.md, full_script_ep1.md v3 (chuẩn định dạng/giọng), SCRIPT_BRIEF.md.
> **Quy ước ghi:** `N:` = narration tiếng Hàn (격식체, giọng nam trầm, thì quá khứ "-였습니다/-했습니다"; câu mở địa danh có thể "612년 7월. 패수."). Trong SC có cả `N:` và thoại, thứ tự đọc do editor quyết (mặc định: N bình luận → đọc SAU thoại; N dẫn vào → đọc TRƯỚC). `TÊN:` = thoại tiếng Hàn. `[ACTION-VI]` = hành động nhìn thấy được (tiếng Việt, cho veo-prompt-engineer). `[SOUND]` = âm thanh gợi ý. `2-BEAT` = 1 SC 8 s gồm 2 shot (chỉ ở hook/trận). `[NARRATOR IM LẶNG]` / `[MID-ROLL]` / `[END CARD]` theo outline.
> **ID:** CHAR_/LOC_/VEH_/UAV_/EQP_/WPN_/PROP_ theo bible. Nhân vật phụ không ID (ghi tên vai): 주법상 (부총관 thủy quân Tùy — tên sử, 1 SC), 사자 (sứ Goguryeo mang thơ), 전령 (Tùy, kỵ mã), 통역 (thông ngôn Goguryeo bị bắt), 수 초병, 선비 기병, 고구려 장교, 마을 아낙들, 포수/탄약수 K2, 부상병 (2소대), 초병 (đại đội), 사수 (cối), 수 장교.
> **Ghi chú LOC:** Đảo lau thứ nhất (2 km trên bãi cạn) và đảo lau thứ hai (3 km thượng lưu) đều là sub-location của LOC_007_SALSU, ghi `LOC_007_SALSU (đảo lau 1 / đảo lau 2 / bãi cạn / bờ nam trại hậu quân)`. Trại 우중문 cách 평양 30리 dựa núi ghi `LOC_008_GOGURYEO_VILLAGE (đồi phía bắc 평양, trại Tùy 30리)` — identity địa hình đồi xanh mưa; không cần LOC mới. Nội điện 평양 = `LOC_006_PYONGYANG (nội điện)` theo REF_PROMPT_EN_INTERIOR.
> **Quy ước ngôn ngữ (P-11):** trên màn hình mọi phe nói tiếng Hàn. Goguryeo ↔ đại đội hiểu nhau. Tùy ↔ 태오 chỉ qua 통역 Goguryeo bị bắt (SC_128). 해모루 đọc thư vua cho 한승우 (Hán văn → tiếng Hàn). Người đương thời KHÔNG dùng 시호 (영양왕 / 수 양제): Goguryeo nói 대왕·전하·과인; Tùy nói 폐하. Narrator được dùng 시호.
> **Con số (nguồn: outline_ep4 + ledger):** 92명 hiện diện (93 sống, 태오 bị bắt) → 91 · K2 8 → 6 · dầu K2 ~20 km (chuẩn đường núi) · cối 50 → 30 · PZF 9 → 6 · kính đêm 10, pin 30% → 20% · radio 50% → 40% · drone 0 · kháng sinh 0 · morphine 10 → 8 · K3 −800 · K6 −40 · súng trường 탄창 넷/người.
>
> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi "X일째/이틀 뒤/간밤에/사흘째 밤" trong narration rà theo bảng này):**
>
> | Ngày | Buổi | SC | Sự kiện |
> |---|---|---|---|
> | D−6 … D−1 | — [史] | SC_013–017 (montage) | 을지문덕 mỗi ngày 7 trận giả thua, dụ 30만 5천 về phía 살수 |
> | D−3 | chiều | (3화 P12) | đại đội tới bãi bắc 살수; lệnh "숨으시오"; mưa bắt đầu |
> | D−2 … D−1 | — | (narrator P2) | K2 trát bùn, đảo lau 1; các bà làng bờ bắc mang cơm; 아리 đi cắt lau với các bà |
> | D1 | rạng sáng | SC_001–011 | 30만 5천 bắt đầu qua bãi cạn; đại đội nằm trong lau sát đường lội |
> | D1 | ngày [史] | SC_012, SC_018–019 | đại quân qua sông cả ngày lẫn đêm; hạm đội 내호아 vào 패수, cách 평양 60리 |
> | D1 | chiều–tối | SC_020–025 | đảo lau 1: không lửa, cơm nguội, thuốc sắc nguội |
> | D2 | rạng sáng | SC_026–030 | 아리 theo các bà cắt lau — trại hậu quân Tùy bờ nam (5천 + đoàn xe, 탁발흠 giữ bãi cạn) |
> | D2 | ngày–tối | SC_031–050 | 백성민 đếm ngày thứ hai; kiểm kê; que nước; 아리 báo cũi |
> | D2 | ngày [史] | SC_052–060 | 내호아 đổ bộ; 주법상 can; 4만; 고건무 bỏ trống 나곽, giấu quân trong chùa |
> | D2 | đêm | SC_061–075 | 탁발흠 đeo kính đêm dò đầm; chốt gác; đánh dao; 탁발흠 bị chém tay, chạy thoát |
> | D3 | ngày [史] | SC_076–093 | 4만 vào 나곽; cửa chùa mở; 내호아 thoát thân; 고건무 đuổi tới thuyền; 내호아 rút ra 해포 |
> | D3 | đêm | SC_101–111 | nội điện 평양: 영양왕·고건무·을지문덕; vua viết một dòng; 해모루 phi đêm về 살수 |
> | D4 | sáng–ngày | SC_112–125 | 해모루 tới đảo lau 1; 한승우 đọc thư; mâu thuẫn; kỵ Tiên Ti bắn tên dò lau |
> | D4 | chiều–đêm | SC_126–148 | cũi 태오 ra bờ; trống + đuốc lùa về bãi cạn; cối 20, PZF 3, K2 2 viên; 2 người ngã; trượt về đảo lau 2 |
> | D5 | rạng sáng | SC_152–172 | đảo lau 2: "여섯 발"; người bị tên bụng; 탁발흠 đếm vỏ đạn ở đảo lau 1; quyết cứu 태오 |
> | D5 | chiều–tối [史] | SC_094–100, SC_149–151 | 30만 tới trại 30리 dựa núi; tin 내호아 (cách 2 ngày) và 전령 "천둥" cùng tới 우중문; 을지문덕 nhận báo của 해모루: "좋소. 서두르게 하시오." |
> | D6 | ngày [史] | SC_173–185 | thơ 여수장우중문시; sứ giả; 우문술 quyết rút, 방진 |
> | D6 | tối | SC_186–197 | 해모루 về đảo lau 2: thơ, kế cứu, lệnh "반이 건널 때까지" |
> | D7 | rạng sáng | SC_198–249 | sương; cứu 태오; chó sủa; kính đêm mù; nghi binh 해모루; K6 một loạt |
> | D7 | ngày [史] | SC_260–261, SC_271–273 | 방진 rút về bắc, kỵ Goguryeo đánh bốn mặt |
> | D7 | đêm (đêm thứ ba sau D4) | SC_250–252 | người bị tên bụng chết vì nhiễm trùng |
> | D8 | sáng | SC_253–259, SC_277–282 | chôn trong lau; 91명; que "어제보다 한 뼘" |
> | D8 | ngày | SC_262–267, SC_283–286 | 탁발흠 quỳ trước 우중문 giữa đường rút; 우문술 "살수까지 이틀" |

---

## [Phần 1] 콜드 오픈 — 「숨 쉬는 것도 작게」 / Chuyện không thể xảy ra  (0:00–1:30)
> Tóm tắt VI: Rạng sáng D1, bãi lau bờ bắc 살수, mưa nhỏ. Cận mặt 오태민 trong bùn; cách mặt 30 cm phía trên, móng ngựa Tùy dẫm xuống nước. Hàng nghìn bàn chân lội qua. Một lính Tùy tạt vào lau tiểu cách mặt 백성민 2 m. Tay 한승우 đè lên báng súng 오태민: "쏘지 마. 숨 쉬는 것도 작게." Narrator vào 0:32. Bánh kê rơi trôi qua tay 서아 — quân đói. K2 là một mô bùn phủ lau, kỵ binh Tùy đi sát váy xích. Aerial: cột quân không thấy điểm cuối.
> Chức năng: ACTION-HOOK · Tài nguyên: "92명" (narrator) · Open loop cuối phần: "누구도 방아쇠를 당기지 않았습니다. 을지문덕이 그렇게 명령했기 때문입니다."
> Ràng buộc: 0:00–0:30 KHÔNG narrator (narrator vào 0:32). 0–30 s = 6 shot (SC_001 2-BEAT · SC_002 · SC_003 2-BEAT · SC_004).

### SC_001 · LOC_007_SALSU (bãi lau sát đường lội, bờ bắc) · CHAR_002 · — · video8s · 0:00–0:08
[ACTION-VI] 2-BEAT (veo-stage tạo 2 clip 3 s + 5 s hoặc 1 clip 8 s cắt đôi ở edit): (a) 0:00–0:03 màn đen; chỉ có tiếng nước bị khuấy bởi hàng nghìn bàn chân và móng ngựa; (b) 0:03–0:08 cận cực gần mặt 오태민 nằm nghiêng trong bùn giữa gốc lau: một mắt mở, bùn khô nứt trên gò má, mưa bám lông mi; đúng lúc đó một móng ngựa Tùy dẫm xuống nước cách mặt anh 30 cm, bùn bắn lên má. Máy tĩnh, không rung.
[SOUND] nước khuấy liên tục, móng ngựa, tiếng thở bị nén. Không nhạc.

### SC_002 · LOC_007_SALSU (bãi lau) · — · WPN_201 · video8s · 0:08–0:16
[ACTION-VI] Low-angle từ tầm mắt người nằm: chân lính Tùy lội qua nước nâu ngang bắp chân — dép rơm rách, ống quần vải ướt, khiên gỗ kéo lê, hàng nối hàng không dứt; phía trên cao, ngọn lau che gần hết trời xám. Máy tĩnh, tiêu cự nông.
[SOUND] bì bõm dồn dập, gỗ khiên va nhau, một tiếng ho, không ai nói.

### SC_003 · LOC_007_SALSU (bãi lau) · CHAR_006 · WPN_201 · video8s · 0:16–0:24
[ACTION-VI] 2-BEAT (4 s + 4 s): (a) cận mặt 백성민 bôi bùn đen chỉ hở mắt, mũ boonie ướt, dao găm cầm ngược trong tay phải áp xuống bùn; (b) một lính Tùy tách khỏi hàng, bước vào mép lau cách anh 2 m, quay lưng, cởi dây quần, tiểu vào lau — hơi nước bốc lên trong mưa; 백성민 không chớp mắt.
[SOUND] tiếng nước tiểu vào lau, lính Tùy thở phào, hàng quân vẫn lội phía sau.

### SC_004 · LOC_007_SALSU (bãi lau) · CHAR_001, CHAR_002 · WPN_001 · video8s · 0:24–0:32
[ACTION-VI] Cận hai bàn tay: ngón trỏ 오태민 đã nằm trong vòng cò khẩu K2C1; bàn tay 한승우 (găng rách, la bàn lủng lẳng chạm bùn) đè lên báng súng, ấn xuống chậm và chắc. Máy nâng lên mặt 한승우 sát tai 오태민, môi gần như không động.
[SOUND] mưa, hàng quân lội, thì thầm sát mic.
한승우: 쏘지 마. 숨 쉬는 것도 작게.

### SC_005 · LOC_007_SALSU (aerial bãi lau bờ bắc) · — · WPN_201 · video8s · 0:32–0:40
[ACTION-VI] Aerial trung-cao: bãi lau xanh xám rộng hàng trăm mét bên bờ bắc; xuyên qua nó, một vệt người và ngựa đi thành hàng dài từ mép nước lên bờ — vệt kéo tới đường chân trời phía nam qua sông; trong lau không thấy gì khác. Máy trượt chậm theo vệt quân.
[SOUND] gió trên cao, tiếng lội dội lên mơ hồ.
N: 612년 7월. 수나라 별동대 30만 5천이 살수를 건넜습니다. 그 갈대밭에는 92명의 대한민국 군인이 엎드려 있었습니다.

### SC_006 · LOC_007_SALSU (bãi lau) · CHAR_006 · WPN_201 · video8s · 0:40–0:48
[ACTION-VI] Lính Tùy thắt lại dây quần, đá một gốc lau cho vui, quay lại nhìn thẳng vào bụi lau chỗ 백성민 nằm — một nhịp — rồi lội trở lại hàng. Máy tĩnh trên mắt 백성민; con mắt không đổi.
[SOUND] dép rơm trên bùn, dây quần, hàng quân.
N: 두 걸음이었습니다. 두 걸음 안에 사람이 엎드려 있었습니다. 수나라 병사는 갈대만 보았습니다. 갈대는 그들의 것이 아니었습니다.

### SC_007 · LOC_007_SALSU (bãi lau) · CHAR_002 · WPN_001 · video8s · 0:48–0:56
[ACTION-VI] Cận mặt 오태민: hàm nghiến, mạch cổ đập nhìn thấy được, môi nứt rớm máu; ngón trỏ rút khỏi vòng cò từng milimét; bàn tay 한승우 vẫn không rời báng súng. Máy tĩnh.
[SOUND] mưa, thở nén, hàng quân.
N: 오태민에게 이것은 가장 어려운 명령이었습니다. 총이 있는데 쏘지 않는 것. 손가락 하나를 움직이지 않는 데 그의 전부가 들어갔습니다.

### SC_008 · LOC_007_SALSU (bãi lau, mép nước) · CHAR_004 · WPN_201 · video8s · 0:56–1:04
[ACTION-VI] Cận mặt nước nâu ngang tay 서아 đang nằm nửa người dưới nước: hàng chân lội qua; một chiếc dép rơm đứt trôi; rồi một bánh kê ép mốc rơi từ túi ai đó, nổi lềnh bềnh, chạm nhẹ vào ngón tay cô rồi trôi đi. Cô không rút tay.
[SOUND] nước, một tiếng chửi khẽ xa (lính Tùy), bánh kê chạm nước.
N: 그들은 백 일치 군량을 압록수에 묻고 왔습니다. 남은 것은 곰팡이 핀 떡 몇 개였습니다. 배고픈 군대가 92명의 머리 위를 지나갔습니다.

### SC_009 · LOC_007_SALSU (bãi lau, vị trí K2) · CHAR_001 · VEH_001, VEH_206 · video8s · 1:04–1:12
[ACTION-VI] Mắt 한승우 (mũ tháo, tóc bết bùn) liếc về phía sau 50 m: một mô bùn phủ lau cao ngang đầu người — nòng pháo bọc lau nằm thấp — K2. Đúng lúc đó một kỵ binh Tiên Ti mũ lông cưỡi ngựa đi sát mô bùn, ngựa hít hít lớp lau, rồi đi tiếp. Máy đẩy nhẹ từ mắt ông sang mô bùn.
[SOUND] vó ngựa trên bùn mềm, ngựa khịt mũi, mưa.
N: 오십 미터 뒤에 전차가 있었습니다. 진흙과 갈대 밑에서 쇠는 숨을 쉬지 않았습니다. 말은 쇠 냄새를 맡지 못했습니다. 젖은 진흙이 냄새를 덮었습니다.

### SC_010 · LOC_007_SALSU (aerial cao, bãi cạn) · — · WPN_201 · still_kenburns · 1:12–1:21
[ACTION-VI] Ảnh aerial rất cao: sông 살수 rộng 800 m xám bạc, mô cát dài, và một dải người đen đặc đi từ bờ bắc qua bãi cạn sang bờ nam — cả hai đầu dải đều khuất ngoài khung, cờ đỏ li ti; bãi lau bờ bắc là một mảng xanh xám tĩnh lặng. Ken-burns kéo ra rất chậm.
[SOUND] gió trên cao, mưa, xa xa tiếng trống hành quân đều đều.
N: 아홉 군. 30만 5천. 살수는 얕았습니다. 무릎까지였습니다. 그래서 그들은 걸어서 건넜습니다. 건너는 데 하루 낮과 하룻밤이 걸렸습니다.

### SC_011 · LOC_007_SALSU (bãi lau) · CHAR_002 · WPN_001 · still_kenburns · 1:21–1:30
[ACTION-VI] Ảnh cận: bàn tay 오태민 mở ra trên bùn cạnh khẩu súng, ngón trỏ duỗi thẳng, cách xa vòng cò; trên mu bàn tay, vết móng ngựa in nước. Ken-burns đẩy chậm vào ngón trỏ.
[SOUND] mưa, hàng quân nhỏ dần.
N: 누구도 방아쇠를 당기지 않았습니다. 을지문덕이 그렇게 명령했기 때문입니다.

[Kết thúc Phần 1]

## [Phần 2] 발견 — 「하루 일곱 번」 / Họ đang ở đâu  (1:30–4:30)
> Tóm tắt VI: Aerial 9 quân xuôi nam. Montage [史] những ngày trước D1: 을지문덕 trên đồi, kỵ Goguryeo xông — vỡ — chạy, ×7 mỗi ngày; Tùy càng thắng càng xa lương; 우중문 hét "평양은 사흘 거리다". Track (a) mở: biển — hạm đội 내호아 vào 패수, cách 평양 60리; 내호아 muốn tới trước 우중문. Đảo lau 1 cách bãi cạn 2 km: không lửa, cơm nguội từ các bà làng bờ bắc; K2 trát bùn ướt (ý 박기철 — payoff hỏa công 2화); 을보 gọi K2 "진흙 소"; 서아 học thuốc sắc nguội. D2 rạng sáng: 아리 theo các bà cắt lau qua nhánh sông — trại hậu quân Tùy bờ nam (5천 + đoàn xe; 탁발흠 được giao giữ bãi cạn: đường về); 아리 nhìn thấy trại, thứ gì đó phủ vải dưới gốc cây; 탁발흠 nhìn xuyên qua các bà về phía lau. Chiều 아리 về.
> Chức năng: DISCOVERY · Tài nguyên: không lửa = cơm nguội, thuốc nguội · Open loop cuối phần: "아리는 매일 아침 갈대를 베러 나갔습니다. 그리고 매일 저녁, 적의 진영을 보고 돌아왔습니다."
> Mini-combat [史]: SC_013–015 (kỵ Goguryeo xông–vỡ–chạy).

### SC_012 · LOC_007_SALSU (aerial, bờ nam → đồi phía nam) · — · WPN_201, PROP_021 · still_kenburns · 1:30–1:40
[ACTION-VI] Ảnh aerial: từ bờ nam 살수, chín cột quân Tùy tỏa thành chín vệt bụi-bùn xuôi về phía nam qua đồi xanh ướt, mỗi cột dưới một cụm cờ đỏ; giữa các cột, đất trống. Ken-burns trượt từ sông về phía nam.
[SOUND] trống Tùy nhiều lớp xa, mưa.
N: 부여도, 낙랑도, 그리고 일곱 길. 아홉 군은 살수 남쪽에서 다시 아홉 갈래로 갈라졌습니다. 목적지는 하나였습니다. 평양. 남은 거리는 이백 리였습니다.

### SC_013 · LOC_008_GOGURYEO_VILLAGE (đồi xanh mưa, ngày trước D1) · CHAR_101, CHAR_105 · VEH_101, PROP_012 · video8s · 1:40–1:48
[ACTION-VI] Montage [史] những ngày trước: 을지문덕 trên lưng ngựa ở đỉnh đồi cỏ ướt, chỏm lông đen hai lông trắng rủ nước, áo choàng ướt; bên ông 해모루 cầm tù và; dưới đồi, cột tiền quân Tùy dài dằng dặc trên đường lầy. Ông giơ hai ngón tay. Máy tĩnh, đẩy nhẹ.
[SOUND] mưa, ngựa giậm, trống Tùy xa.
N: 살수를 건너기 전 엿새 동안, 을지문덕은 하루에 일곱 번 싸웠습니다. 그리고 일곱 번 다 졌습니다. 지는 것은 그의 명령이었습니다.

### SC_014 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ dưới đồi) · CHAR_105 · VEH_101, WPN_101, WPN_201 · video8s · 1:48–1:56
[ACTION-VI] 300 kỵ Goguryeo của 해모루 lao xuống dốc, cung bắn một loạt vào sườn cột quân Tùy — vài lính Tùy ngã, hàng khiên dựng lên; kỵ binh vòng sát rồi ghì cương. Tracking ngang, wide, không cận thương vong.
[SOUND] vó ngựa dồn, dây cung hàng loạt, tiếng hô Tùy.
N: 공격은 진짜였습니다. 화살도 진짜였습니다. 다만 끝까지 가지 않았습니다.

### SC_015 · LOC_008_GOGURYEO_VILLAGE (đồng cỏ) · CHAR_105 · VEH_101, PROP_012, WPN_201 · video8s · 1:56–2:04
[ACTION-VI] Kỵ Goguryeo "vỡ": quay ngựa tháo chạy tán loạn lên đồi, một lá cờ 삼족오 rơi xuống bùn — cố ý; lính Tùy reo, tiền quân bỏ hàng đuổi theo; một sĩ quan Tùy nhặt cờ giơ lên. Máy trung, theo cờ rơi.
[SOUND] reo hò Tùy, vó ngựa xa dần, cờ đập bùn.
N: 깃발 하나를 버리면 수나라 군은 십 리를 더 왔습니다. 십 리는 곧 하루치 밥이었습니다. 을지문덕은 깃발로 밥을 샀습니다.

### SC_016 · LOC_008_GOGURYEO_VILLAGE (sườn đồi, chiều) · CHAR_105 · PROP_018 · still_kenburns · 2:04–2:14
[ACTION-VI] Ảnh cận: 해모루 ngồi trên đá, dao nhỏ khắc vạch thứ bảy lên cán tù và bằng sừng đen — sáu vạch cũ, một vạch mới; tay dính bùn, mắt trũng. Ken-burns đẩy vào vạch thứ bảy.
[SOUND] dao cạo sừng, mưa, ngựa thở.
N: 하루 일곱 번. 해모루는 나각 손잡이에 일곱 줄을 새겼습니다. 다음 날 아침이면 다시 처음부터였습니다. 그렇게 엿새, 마흔두 번을 졌습니다. 삼국사기는 이렇게 적었습니다. 하루에 일곱 번 싸워 일곱 번 다 이겼다고. 수나라 쪽에서 본 문장이었습니다.

### SC_017 · LOC_008_GOGURYEO_VILLAGE (đường lầy, cột quân Tùy) · CHAR_202 · WPN_201, PROP_021 · video8s · 2:14–2:22
[ACTION-VI] 우중문 (giáp 명광개 hai gương ngực ướt bóng, râu trắng dài, áo choàng đỏ nặng nước) cưỡi ngựa dọc cột quân, gươm chỉ về nam, hét; hai bên đường, lính Tùy nhai vỏ cây, một người ngồi gục bị bạn kéo dậy. Tracking ngang theo ngựa.
[SOUND] ngựa, hét khàn, mưa, chân lội bùn.
N: 우중문은 이기고 있었습니다. 적어도 그렇게 믿었습니다. 그의 병사들은 나무껍질을 씹으며 이기고 있었습니다.
우중문: 평양은 사흘 거리다! 사흘이면 끝난다!

### SC_018 · LOC_006_PYONGYANG (cửa biển 패수, aerial) · — · VEH_204, PROP_021 · still_kenburns · 2:22–2:32
[ACTION-VI] HARD CUT. Ảnh aerial biển xám: hàng trăm 누선 Tùy — thân gỗ nâu đỏ, lầu gỗ hai ba tầng, buồm nâu — nối nhau từ khơi vào cửa sông rộng, cờ đỏ-vàng ướt; mưa mù chân trời. Ken-burns kéo từ khơi vào cửa sông.
[SOUND] sóng, mái chèo hàng loạt, trống thủy quân.
N: 같은 무렵, 바다. 내호아의 수군이 패수 하구에 들어왔습니다. 동래에서 배로 떠난 강회의 군사들이었습니다. 평양까지 육십 리. 배로 반나절이었습니다.

### SC_019 · LOC_006_PYONGYANG (boong 누선 kỳ hạm) · CHAR_204 · VEH_204 · video8s · 2:32–2:40
[ACTION-VI] 내호아 (mũ sắt vành rộng, áo choàng dầu bóng nước, sống mũi dẹt) đứng mũi thuyền, tay nắm lan can ướt, nhìn lên thượng nguồn; quay lại quát thủy thủ chèo. Low-angle, mưa tạt.
[SOUND] mái chèo, trống nhịp nhanh hơn, mưa, gỗ kêu.
N: 내호아는 우중문을 기다리지 않을 생각이었습니다. 평양을 먼저 밟는 자가 공을 가져갈 것이었습니다.
내호아: 노를 더 저어라. 우중문보다 먼저 간다.

### SC_020 · LOC_007_SALSU (đảo lau 1, chiều D1) · lính Hàn, CHAR_004 · PROP_020, PROP_010 · video8s · 2:40–2:48
[ACTION-VI] HARD CUT về đảo lau: một gò đất thấp giữa bãi lau ngập nước, lính Hàn nằm dưới mái lau bó tạm, mặt bôi bùn, súng bọc vải; 서아 đi khom giữa họ, phát từng nắm cơm kê nguội gói lá; không khói, không lửa. Tracking thấp theo cô.
[SOUND] mưa trên lau, nhai, tiếng lội rất xa (cột quân vẫn qua sông).
N: 여울에서 이 킬로. 갈대 사이에 낮은 섬 하나가 있었습니다. 삼 일 전부터 92명은 거기 있었습니다. 불은 피우지 않았습니다. 연기 한 줄이면 삼십만이 돌아볼 것이었습니다.

### SC_021 · LOC_007_SALSU (đảo lau 1, K2) · CHAR_003, 2 lính · VEH_001, PROP_020 · video8s · 2:48–2:56
[ACTION-VI] K2 giữa lau: 박기철 (mũ lưỡi trai ướt nhẹp, râu muối tiêu) và hai lính vốc bùn ướt từ xô, trát từng lớp lên váy xích và tháp pháo; bùn dính vào lưới lau đã cắm; tay ông vỗ bùn như vỗ lưng bò. Máy trung.
[SOUND] bùn nhão, tay vỗ thép qua bùn, mưa.
N: 진흙은 박기철의 생각이었습니다. 요동성에서 그는 기름이 타는 것을 보았습니다. 그때 손을 데었습니다. 젖은 진흙은 불화살을 받아도 타지 않았습니다.
박기철: 젖은 흙은 안 탑니다. 두 번은 안 당합니다.

### SC_022 · LOC_007_SALSU (đảo lau 1, K2) · CHAR_106 · VEH_001 · video8s · 2:56–3:04
[ACTION-VI] 을보 (tạp dề da, búa nhỏ ở thắt lưng) đứng cạnh nòng pháo, hai bàn tay già gân guốc miết bùn dọc bao nhiệt nòng như vuốt cổ ngựa, nheo mắt trái, cười một bên mép.
[SOUND] bùn, mưa, tiếng cười khẽ.
N: 을보는 쇠를 만지고 나서야 사람을 믿는 노인이었습니다. 이제 그는 진흙까지 만졌습니다.
을보: 쇠쟁이, 이놈이 이제 진흙 소가 됐구먼.

### SC_023 · LOC_007_SALSU (mép đảo lau 1, phía làng) · 마을 아낙들, lính Hàn · PROP_020 · still_kenburns · 3:04–3:14
[ACTION-VI] Ảnh: năm bà làng Goguryeo áo vải gai, khăn đầu, váy xếp ly buộc gối, gánh rổ đậy lá qua đường lau ngập nước tới mép đảo; một lính Hàn trẻ cúi đầu nhận rổ; phía sau, mái tranh làng bờ bắc lấp ló. Ken-burns trượt từ rổ lên mặt bà cụ.
[SOUND] nước, tiếng bà cụ nói nhỏ không rõ chữ, mưa.
N: 북쪽 기슭 마을의 아낙들이었습니다. 매일 저녁 찬 조밥과 삶은 나물이 왔습니다. 갈대를 베러 가는 길이라고 하면 아무도 묻지 않았습니다. 이천 년 뒤의 군대는 이 땅의 어머니들이 먹였습니다.

### SC_024 · LOC_007_SALSU (đảo lau 1, góc thuốc) · CHAR_004, CHAR_106 · PROP_009 · video8s · 3:14–3:22
[ACTION-VI] 서아 (tóc tết bím Goguryeo, băng chữ thập sờn) ngồi xổm trước bát gỗ, giã rễ cây bằng đá trong nước lạnh; 을보 ngồi đối diện nhìn tay cô. Cô ngẩng lên hỏi.
[SOUND] đá giã, nước, mưa.
서아: 불 없이 달인 약도 약이 됩니까?

### SC_025 · LOC_007_SALSU (đảo lau 1, góc thuốc) · CHAR_106, CHAR_004 · — · video8s · 3:22–3:30
[ACTION-VI] 을보 nhúng ngón tay vào bát, nếm, nhăn mặt, rồi đẩy bát về phía cô; giọng 반말 người già.
[SOUND] mưa, bát gỗ trượt.
N: 항생제는 두 달 전에 끝났습니다. 남은 것은 이 노인의 풀뿐이었습니다. 서아는 풀 이름을 약 이름처럼 외웠습니다.
을보: 찬 약은 반 약이지. 없는 것보단 낫고.

### SC_026 · LOC_007_SALSU (đường lau, rạng sáng D2) · CHAR_107, 마을 아낙들 · PROP_020 · video8s · 3:30–3:38
[ACTION-VI] Rạng sáng xám: 아리 (hai bím buộc chỉ đỏ giấu dưới khăn, khăn olive quấn bụng giấu trong váy, liềm trong tay, rổ trên lưng) đi giữa năm bà làng theo lối lau ngập nước về phía sông; các bà nói chuyện bình thường, 아리 im. Tracking từ sau.
[SOUND] nước tới đùi, liềm chạm rổ, tiếng các bà.
N: 다음 날 새벽부터 아리는 아낙들과 함께 나갔습니다. 아리의 어머니는 이 강가 마을 사람이었습니다. 아리는 갈대 베는 법을 알았습니다. 그리고 갈대가 어디까지 이어지는지도 알았습니다.

### SC_027 · LOC_007_SALSU (mép đảo lau 1) · CHAR_006, CHAR_001 · PROP_006 · video8s · 3:38–3:46
[ACTION-VI] 백성민 nằm ở mép đảo, ống nhòm dõi theo bóng các bà và 아리 nhỏ dần trong lau; hạ ống nhòm, nói không quay đầu; 한승우 nằm cạnh, mũ tháo.
[SOUND] mưa, ống nhòm chạm áo.
N: 백성민은 아리를 내보낸 것이 누구의 생각인지 묻지 않았습니다. 아리 자신의 생각이었습니다. 열다섯 살의 생각이었습니다.
백성민: 저 아이는 갈대를 베러 가는 게 아닙니다.

### SC_028 · LOC_007_SALSU (mô cát, nhìn sang trại hậu quân bờ nam) · 마을 아낙들, CHAR_107 · WPN_201, PROP_021 · still_kenburns · 3:46–3:56
[ACTION-VI] Ảnh wide từ mô cát giữa sông: các bà cúi cắt lau ở tiền cảnh; qua một nhánh nước hẹp, bờ nam: trại Tùy — hàng lều da, xe bò chở hòm, ngựa buộc dây, một lính gác dựa giáo nhìn các bà rồi quay đi. Ken-burns kéo từ liềm tới trại.
[SOUND] liềm cắt lau, tiếng trại xa, bò rống.
N: 삼십만이 남쪽으로 갔습니다. 그러나 다 간 것은 아니었습니다. 우중문은 여울에 오천을 남겼습니다. 수레와 남은 짐을 지키는 후군이었습니다. 돌아올 길이었기 때문입니다. 그 후군을 탁발흠이 맡았습니다.

### SC_029 · LOC_007_SALSU (mô cát) · CHAR_107 · PROP_020 · video8s · 3:56–4:04
[ACTION-VI] Cận 아리 cắt lau, mắt ngước dưới chân mày không ngẩng đầu: lính gác; dây ngựa; dưới một gốc liễu trong trại, một khối vuông phủ vải ướt — không rõ là gì. Cô cúi xuống cắt tiếp, tay run.
[SOUND] liềm, mưa, tiếng trại.
N: 아리는 얼굴을 들지 않았습니다. 눈만 들었습니다. 그것도 어머니에게 배운 것이었습니다.

### SC_030 · LOC_007_SALSU (bờ nam, mép trại hậu quân) · CHAR_205 · EQP_001, VEH_206 · video8s · 4:04–4:12
[ACTION-VI] 탁발흠 đi bộ dọc mép trại, mũ vành lông cáo, kính nhìn đêm lật ngược trên mũ (ban ngày), áo choàng da ướt; liếc qua các bà cắt lau không quá một nhịp, rồi mắt dừng lâu ở bãi lau bờ bắc xa xa. Máy đẩy chậm vào mắt.
[SOUND] trại, mưa, ngựa.
N: 탁발흠은 아낙들을 보지 않았습니다. 아낙들 너머를 보았습니다. 그의 눈은 며칠째 저 갈대밭에 가 있었습니다. 저 안 어딘가에 천둥이 있었습니다.

### SC_031 · LOC_007_SALSU (đảo lau 1, chiều D2) · CHAR_107, CHAR_004 · PROP_020 · video8s · 4:12–4:20
[ACTION-VI] Chiều: 아리 về tới đảo, thả bó lau nặng xuống, hai bàn tay xước máu; 서아 chạy tới đỡ; 아리 ngồi thụp, thở dốc, không nói ngay. Máy trung.
[SOUND] bó lau đổ, thở, mưa.
N: 저녁마다 아리는 갈대 한 짐과 함께 돌아왔습니다. 갈대는 핑계였습니다. 진짜 짐은 눈 안에 있었습니다.

### SC_032 · LOC_007_SALSU (đảo lau 1) · CHAR_107 · PROP_020 · still_kenburns · 4:20–4:30
[ACTION-VI] Ảnh cận: 아리 ngồi bên bó lau, khăn olive lộ một góc, hai bàn tay xước đặt trên đầu gối, mắt nhìn về hướng sông. Ken-burns đẩy chậm vào mắt.
[SOUND] mưa, lau cọ.
N: 아리는 매일 아침 갈대를 베러 나갔습니다. 그리고 매일 저녁, 적의 진영을 보고 돌아왔습니다.

[Kết thúc Phần 2]

## [Phần 3] 재고 조사 — 「우린 이제 장님입니다」 / Kiểm kê  (4:30–7:00)
> Tóm tắt VI: Chiều tối D2. Sổ 박기철 (KB số): 92 · K2 8 · 연료 20km · 박격포 50 · PZF 9 · 야시경 10 (30%) · 무전기 50% · 드론 0. Chỗ 태오 từng ngồi trống — "우린 이제 장님입니다." Mini-contact: hai lính Tùy lạc hàng vào mép đảo tìm củi, cách lính Hàn 3 m — không ai cử động. 백성민 với máy đếm tay: "하루 종일 셌습니다. 끝이 없습니다.". Aerial đuôi cột quân: đoàn xe + hậu quân dựng trại bờ nam. Que nước: "하루에 한 뼘씩". 을보: "이 강은 한 번 화나면 사흘 만에 어른 키를 넘소." 아리 về, thì thầm với 서아: cũi tre trong trại, cậu bé mặc đồ như họ. 서아 nhìn 한승우.
> Chức năng: DECISION · Tài nguyên nói thành lời: "아흔두 명" · "여덟 발" · "이십 킬로" · "박격포 오십" · "PZF 아홉" · "야시경 열 개, 배터리 삼십" · "무전기 오십 퍼센트" · "드론, 영" · Open loop cuối phần: "강 건너 우리 안에 앉은 소년은 그들과 같은 옷을 입고 있었습니다."
> Sau mid-roll 1 (7:00): SC_051 cận cũi tre trong mưa, không thoại.

### SC_033 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_003 · PROP_001 · still_kenburns · 4:30–4:40
[ACTION-VI] Ảnh cận: trang sổ bìa xanh ướt mép của 박기철, bút chì, các dòng chữ và số viết tay (brush-less, chữ Hangul mô tả bình thường, số Ả Rập): 92 · 8 · 20km · 50 · 9 · 10 (30%) · 50% · 0; một giọt mưa làm nhòe số 0 cuối. Ken-burns trượt từ trên xuống dưới cột số.
[SOUND] mưa trên lau, bút chì.
N: 이틀째 저녁. 박기철은 같은 숫자를 다시 셌습니다. 숫자는 세지 않으면 줄어도 모르는 법이었습니다. 이 수첩은 이 부대의 은행이었습니다. 은행에 들어오는 돈은 없었습니다.

### SC_034 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_003, CHAR_001 · PROP_001 · video8s · 4:40–4:48
[ACTION-VI] 박기철 đọc sổ, giọng thấp, mỗi số nói một lần rồi lặp bằng môi; 한승우 ngồi đối diện, mũ tháo, nghe không ngắt. Máy tĩnh, hai mặt trong khung.
[SOUND] mưa, giấy ướt.
박기철: 아흔두 명. 포탄 여덟 발. 연료 이십 킬로.

### SC_035 · LOC_007_SALSU (đảo lau 1, đống khí tài) · lính Hàn · WPN_002, WPN_005, EQP_001 · video8s · 4:48–4:56
[ACTION-VI] Insert: bàn tay lính lật nắp hòm đạn cối ướt đếm bằng ngón; sáu ống PZF-3 xếp dưới tấm poncho; túi pin AA và mười kính đêm cuộn trong vải dầu. Máy cận, lia chậm.
[SOUND] nắp hòm, pin lách cách, mưa.
N: 연료 이십 킬로는 산길 기준이었습니다. 평지라면 조금 더 갔습니다. 박기철은 늘 적은 쪽으로 셌습니다. 많은 쪽으로 세다가 죽는 사람을 그는 알았습니다.

### SC_036 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_003 · PROP_001 · video8s · 4:56–5:04
[ACTION-VI] 박기철 tiếp, ngón tay dò từng dòng; mưa nhỏ từ mái lau xuống vai ông.
[SOUND] mưa, giấy.
박기철: 박격포 오십. PZF 아홉. 야시경 열 개, 배터리 삼십.

### SC_037 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_003 · EQP_002 · video8s · 5:04–5:12
[ACTION-VI] 박기철 gõ bút chì lên máy radio PRC-999K đặt cạnh, màn hình pin nhỏ; đọc; rồi bút chì dừng ở dòng cuối, ông không đọc tiếp. Cận tay và sổ.
[SOUND] bút gõ nhựa, mưa.
N: 무전기는 전차에서 충전했습니다. 전차는 기름으로 충전했습니다. 모든 숫자는 결국 한 숫자로 이어졌습니다. 이십 킬로.
박기철: 무전기 오십 퍼센트. 드론…

### SC_038 · LOC_007_SALSU (đảo lau 1, chỗ trống bên K2) · CHAR_003 · VEH_001 · video8s · 5:12–5:20
[ACTION-VI] 박기철 ngẩng lên nhìn chỗ đất trống cạnh váy xích K2 — nơi trước đây hộp drone và tấm bạt của 태오 luôn đặt; giờ chỉ có bùn và một vết lõm. Máy từ mắt ông sang chỗ trống.
[SOUND] mưa, im.
N: 그 자리에는 늘 소년이 앉아 있었습니다. 하늘의 눈을 무릎에 놓고. 이제 자리만 남았습니다.
박기철: 드론, 영. …우린 이제 장님입니다.

### SC_039 · LOC_007_SALSU (mép đảo lau 1, phía sông) · CHAR_006, 초병 · PROP_006, WPN_201 · video8s · 5:20–5:28
[ACTION-VI] 백성민 nằm sấp ở mép đảo, ống nhòm và máy đếm tay bấm tách-tách; cách anh 3 m, hai lính Tùy lạc hàng (áo vải, giáo cầm ngược) lội vào mép lau, bẻ lau khô làm củi, nói chuyện; một lính Hàn nằm ngay dưới chân họ, chỉ có mắt động. Máy tĩnh, tiêu cự nông từ mắt lính Hàn.
[SOUND] lau gãy, tiếng Tùy lầm bầm, máy đếm ngừng.
N: 낙오병 둘이 마른 갈대를 꺾으러 들어왔습니다. 세 걸음 안에 총이 셋 있었습니다. 아무도 쏘지 않았습니다. 백성민의 손가락도 세는 것을 멈췄습니다.

### SC_040 · LOC_007_SALSU (mép đảo lau 1) · CHAR_006, CHAR_001 · PROP_006 · video8s · 5:28–5:36
[ACTION-VI] Hai lính Tùy ôm bó lau khô đi khuất; 백성민 bò lùi về chỗ 한승우, chìa máy đếm tay — con số ba chữ số đã quay vòng nhiều lần; giọng phẳng.
[SOUND] bò trên bùn, máy đếm, mưa.
N: 사람을 세는 기계는 천에서 다시 영으로 돌아갔습니다. 백성민은 그것을 몇 번이나 돌렸는지 종이에 적었습니다. 어제도, 오늘도. 종이가 젖어서 숫자가 번졌습니다.
백성민: 하루 종일 셌습니다. 끝이 없습니다.

### SC_041 · LOC_007_SALSU (aerial đuôi cột quân, bờ nam) · — · WPN_201, PROP_021 · still_kenburns · 5:36–5:46
[ACTION-VI] Ảnh aerial: đuôi cột quân — đoàn xe bò chở hòm, ngựa thồ, lính Tùy áo vải — dừng lại trên bờ nam ngay sau bãi cạn, lều da dựng thành vòng quanh xe; phía nam xa, cột quân chính đã khuất; bờ bắc, bãi lau tĩnh. Ken-burns kéo từ đoàn xe ra toàn cảnh.
[SOUND] bò, gỗ xe, trống ngừng.
N: 꼬리는 남쪽으로 가지 않았습니다. 여울 남쪽 기슭에 멈춰 진을 쳤습니다. 후군 오천과 수레였습니다. 그 수레 사이 어딘가에 대나무 우리가 하나 있었습니다. 아직 아무도 그것을 보지 못했습니다.

### SC_042 · LOC_007_SALSU (mép nước đảo lau 1) · CHAR_003 · — · video8s · 5:46–5:54
[ACTION-VI] 박기철 lội tới gối ở mép đảo, cắm một cọc gỗ đã khắc vạch xuống đáy cát, ấn chắc; mặt nước chạm vạch thứ hai từ dưới; ông nhìn cọc, nhìn trời. Máy thấp ngang mặt nước.
[SOUND] cọc cắm cát, nước chảy, mưa.
N: 하늘의 눈이 없으니 강이 시계가 되었습니다. 박기철은 나무 막대에 눈금을 새겨 물에 꽂았습니다. 기름과 탄약처럼, 물도 셀 수 있었습니다.

### SC_043 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_003, CHAR_001 · — · video8s · 5:54–6:02
[ACTION-VI] 박기철 về dưới mái lau, vắt ống quần, nói với 한승우 đang lau súng; giơ bàn tay xòe làm cỡ.
[SOUND] vắt vải, mưa.
박기철: 하루에 한 뼘씩 오릅니다.

### SC_044 · LOC_007_SALSU (mép nước, cạnh cọc) · CHAR_106 · — · video8s · 6:02–6:10
[ACTION-VI] 을보 ngồi xổm bên cọc, thọc cả bàn tay xuống dòng nước, cảm dòng chảy, nheo mắt trái nhìn thượng nguồn nơi mây đen đè xuống núi; nói không quay lại (하오체 với sĩ quan — miễn cưỡng).
[SOUND] nước qua tay, sấm rất xa.
N: 을보는 강가 마을에서 자란 사람이 아니었습니다. 그러나 대장장이는 물을 알았습니다. 쇠를 식히는 물이 어디서 오는지 알았습니다.
을보: 이 강은 한 번 화나면 사흘 만에 어른 키를 넘소.

### SC_045 · LOC_007_SALSU (mép nước) · CHAR_001 · PROP_015 · video8s · 6:10–6:18
[ACTION-VI] 한승우 đứng phía sau nhìn cọc — vạch thứ hai — rồi ngẩng nhìn mây đen thượng nguồn; bàn tay phải theo thói quen chạm túi ngực nơi cán mũi tên Goguryeo lộ ra. Máy đẩy chậm.
[SOUND] mưa dày hơn, sấm xa.
N: 물이 오르면 여울은 사라집니다. 여울이 사라지면 삼십만은 돌아갈 길이 없어집니다. 한승우는 아직 그 셈을 하지 않았습니다. 을지문덕은 이미 했습니다.

### SC_046 · LOC_007_SALSU (đảo lau 1, hoàng hôn D2) · CHAR_107, CHAR_004 · PROP_020 · video8s · 6:18–6:26
[ACTION-VI] Hoàng hôn xám: 아리 về với bó lau, mặt trắng bệch, không thả bó xuống chỗ thường lệ mà đi thẳng tới 서아 đang cuộn băng, kéo tay áo cô ra sau bụi lau. Tracking theo hai người.
[SOUND] lau, mưa, thở gấp.
N: 그날 저녁 아리는 갈대를 내려놓지 않았습니다. 먼저 사람을 찾았습니다.

### SC_047 · LOC_007_SALSU (đảo lau 1, sau bụi lau) · CHAR_107, CHAR_004 · — · video8s · 6:26–6:34
[ACTION-VI] Hai người ngồi sát, 아리 thì thầm sát tai 서아, mắt mở to; 서아 nghe, tay ngừng cuộn băng.
[SOUND] thì thầm, mưa.
아리: 언니, 강 건너에 우리가 있어요. 대나무 우리요.

### SC_048 · LOC_007_SALSU (đảo lau 1, sau bụi lau) · CHAR_107, CHAR_004 · — · video8s · 6:34–6:42
[ACTION-VI] 서아 nắm chặt cánh tay 아리; 아리 kéo tay áo mình lên chỉ vào hoa văn rằn ri trên vai 서아 rồi nói tiếp; nước mắt không rơi, chỉ đọng.
[SOUND] thì thầm, mưa.
아리: 그 안에 오라버니 같은 사람이… 같은 옷이에요.

### SC_049 · LOC_007_SALSU (đảo lau 1) · CHAR_004 · — · video8s · 6:42–6:50
[ACTION-VI] 서아 đứng dậy khỏi bụi lau, quay người tìm 한승우 qua đầu những người nằm; máy theo hướng mắt cô: 한승우 ở đầu kia đảo bên cọc nước ngẩng lên đúng lúc. Không thoại.
[SOUND] mưa, lau.
N: 서아는 곧바로 말하러 가지 않았습니다. 먼저 얼굴을 보았습니다. 말보다 얼굴이 먼저 건너갔습니다.

### SC_050 · LOC_007_SALSU (đảo lau 1, bên cọc nước) · CHAR_001 · — · still_kenburns · 6:50–7:00
[ACTION-VI] Ảnh cận: mặt 한승우 dưới mưa, mắt hướng về 서아 ngoài khung — đã đọc được điều cô chưa nói; sau lưng ông, cọc nước và dòng sông xám; ken-burns đẩy rất chậm vào mắt.
[SOUND] mưa, sông.
N: 강 건너 우리 안에 앉은 소년은 그들과 같은 옷을 입고 있었습니다.

[MID-ROLL 1 · 7:00]

[Kết thúc Phần 3]

## [Phần 4] 첫 접촉 — 「밤눈을 가진 자」 / Cuộc chạm trán đầu tiên  (7:00–10:30)
> Tóm tắt VI: Sau mid-roll: cận cũi tre trong mưa, không thoại. (a) [史] D2 패수: 내호아 đổ bộ, thắng một chạm trán nhỏ ở bãi; 주법상 xin đợi bộ binh; 내호아: "평양은 비었소. 사만이면 남소." — chọn 4만 tinh binh. 고건무 trên tháp cổng: lệnh bỏ trống 나곽, để chúng vào tới chợ; chợ trống, vò rượu để lại làm mồi; quân Goguryeo vào chùa, cửa đóng, ngồi trong tối. (b) Salsu đêm D2: POV kính đêm xanh của 탁발흠; hắn đi bộ với 20 kỵ vào đầm; chốt gác đại đội chỉ bật 4 kính (pin 30%); 백성민 ra thay ca; hai Tiên Ti dò trúng chốt; đánh dao trong nước, không phát súng; 탁발흠 lao vào, bị chém cẳng tay, chạy thoát — kính đêm phát sáng xanh bập bềnh xa dần: "야시경입니다. 우리 겁니다." 탁발흠 rút ra bài học: "찾았다. 갈대밭 안이다."
> Chức năng: THREAT + CONTACT · Tài nguyên: kính đêm dùng 4 chiếc (pin 30→20% sau đêm) · Enemy adaptation: săn đêm bằng kính, đi bộ trong đầm · Open loop cuối phần: "그날 밤, 갈대밭에서 처음으로 적이 그들보다 멀리 봤습니다."

### SC_051 · LOC_007_SALSU (trại hậu quân bờ nam, gốc liễu) · CHAR_005 · — · video8s · 7:00–7:08
[ACTION-VI] Cận cũi tre dưới gốc liễu trong mưa: nan tre buộc dây da, mái vải ướt; bên trong, một bóng người co ro quay lưng, áo rằn ri rách, vai phải một mảng vải bị xé — chỗ miếng vá 태극기 từng ở. Máy đẩy rất chậm vào mảng vải xé. Không thoại, không narrator.
[SOUND] mưa trên vải, dây da kêu, trại xa.

### SC_052 · LOC_006_PYONGYANG (aerial bờ bắc 패수 dưới thành) · — · VEH_204, PROP_021 · still_kenburns · 7:08–7:18
[ACTION-VI] Ảnh aerial mưa: thành 평양 trên đồi thấp, tường đá xám dài có 치, mái cổng ngói đen; dưới thành, sông 패수 rộng 500 m xám xanh, hàng chục 누선 áp bãi bờ bắc, thuyền phẳng chở lính đổ vào bãi cát; cờ đỏ. Ken-burns từ thuyền lên thành.
[SOUND] mái chèo, trống thủy quân, mưa.
N: 612년 7월. 패수. 내호아의 배가 평양성 아래 닿았습니다. 성벽 위에서는 삼족오가 비에 젖은 채 내려다보았습니다.

### SC_053 · LOC_006_PYONGYANG (bãi đổ bộ) · 수군 Tùy, quân Goguryeo · VEH_204, WPN_201 · video8s · 7:18–7:26
[ACTION-VI] Bãi cát: lính thủy Tùy nhảy khỏi thuyền phẳng, khiên dựng, đao rút; một toán quân Goguryeo nhỏ từ bờ dốc bắn tên rồi rút lui lên phía cổng thủy; lính Tùy reo, đuổi vài bước rồi dừng. Wide, không cận thương vong.
[SOUND] dây cung, đao, reo Tùy, sóng.
N: 첫 싸움은 작았습니다. 고구려 군은 몇 번 쏘고 물러났습니다. 내호아는 그것을 승리라 불렀습니다. 고구려는 그것을 초대라 불렀습니다.

### SC_054 · LOC_006_PYONGYANG (bãi đổ bộ, dưới lọng) · CHAR_204, 주법상 · VEH_204 · video8s · 7:26–7:34
[ACTION-VI] 내호아 đứng dưới lọng dầu, mũ vành rộng nhỏ nước; 주법상 (부총관, giáp sẫm, mặt gầy) tiến lên một bước, cúi đầu, nói thấp — hợp lễ, cẩn trọng.
[SOUND] mưa trên lọng, trại.
N: 부총관 주법상은 뭍의 군대를 기다리자고 했습니다. 우중문의 삼십만이 오면 함께 치자는 것이었습니다. 옳은 말이었습니다. 옳은 말은 늦게 오는 법이었습니다.
주법상: 총관, 뭍의 군사가 올 때까지 기다리십시오.

### SC_055 · LOC_006_PYONGYANG (bãi đổ bộ, dưới lọng) · CHAR_204 · — · video8s · 7:34–7:42
[ACTION-VI] 내호아 cười to, vỗ gương ngực, chỉ tay lên thành trên đồi — cổng ngoại thành mở toang, không bóng người trên tường ngoài; giọng thô.
[SOUND] cười, mưa, trống.
내호아: 평양은 비었소. 사만이면 남소.

### SC_056 · LOC_006_PYONGYANG (bãi đổ bộ) · 4만 tinh binh Tùy · WPN_201, PROP_021 · video8s · 7:42–7:50
[ACTION-VI] 4만 lính tinh nhuệ xếp hàng trên bãi cát: giáp 명광개 ướt bóng, đao, khiên, cờ đỏ; hàng nối hàng dọc bờ sông; sĩ quan cưỡi ngựa dọc hàng. Aerial trung, không thấy điểm cuối.
[SOUND] giáp va, trống, mưa.
N: 사만. 강회에서 데려온 가장 좋은 병사들이었습니다. 내호아는 그들을 성으로 보냈습니다. 배는 강에 남겨 두었습니다. 그것이 두 번째 실수였습니다. 첫 번째는 주법상의 말을 듣지 않은 것이었습니다.

### SC_057 · LOC_006_PYONGYANG (tháp cổng ngoại thành) · CHAR_103 · PROP_012 · still_kenburns · 7:50–8:00
[ACTION-VI] Ảnh: 고건무 (chỏm bờm ngựa đỏ ngắn, râu quai nón, khiên tròn trên lưng) đứng trên tháp cổng gỗ hai tầng, tay đặt lên lan can ướt, nhìn xuống bãi sông đầy thuyền và giáp bạc; sau lưng ông, cờ 삼족오 ướt sũng. Ken-burns đẩy vào mặt ông.
[SOUND] mưa trên ngói, trống Tùy vọng lên.
N: 성 위에서 고건무가 내려다보았습니다. 대왕의 아우였습니다. 평양의 방어는 그의 것이었습니다. 그는 사만을 세지 않았습니다. 사만이 걸어올 길을 세었습니다.

### SC_058 · LOC_006_PYONGYANG (tháp cổng, sân dưới) · CHAR_103, 고구려 장교 · — · video8s · 8:00–8:08
[ACTION-VI] 고건무 xuống cầu thang gỗ, đi ngang hàng sĩ quan đang chờ, không dừng, nói (하게체 với thuộc hạ) — walk-and-talk; sĩ quan chạy theo.
[SOUND] giày trên gỗ, mưa, giáp.
N: 나곽. 평양의 바깥 성이었습니다. 시장과 절과 백성의 집이 그 안에 있었습니다. 고건무는 그것을 다 내주기로 했습니다.
고건무: 나곽을 비워라. 시장까지 들어오게 두라.

### SC_059 · LOC_006_PYONGYANG (phố chợ ngoại thành) · quân Goguryeo · — · video8s · 8:08–8:16
[ACTION-VI] Tracking qua phố chợ đang bị bỏ trống có chủ ý: lính Goguryeo khiêng hòm cuối cùng lên dốc nội thành; một sạp để nguyên lụa; một lính đặt vò rượu đầy lên sạp rồi đi; cửa nhà mở toang. Mưa.
[SOUND] bước chân rút, vò rượu đặt gỗ, mưa.
N: 비단은 남겨 두었습니다. 술독도 남겨 두었습니다. 배고픈 군대가 비단과 술을 보면 대열이 풀리는 법이었습니다. 고건무는 적의 배를 미끼로 썼습니다.

### SC_060 · LOC_006_PYONGYANG (chùa gỗ trống, trong) · CHAR_103, quân Goguryeo · — · video8s · 8:16–8:24
[ACTION-VI] Trong chùa gỗ: lính Goguryeo giáp lamellar lần lượt bước vào, ngồi xuống giữa các cột gỗ dày, sát nhau, giáo dựng; tượng Phật gỗ mờ vàng; 고건무 vào cuối cùng, tự tay khép cửa gỗ ba gian, ngồi xuống với khiên. Ánh sáng tắt dần theo cửa.
[SOUND] cửa gỗ nặng, giáp ngồi, mưa bên ngoài nhỏ dần.
N: 절은 비어 있었습니다. 승려들은 내성으로 올라갔습니다. 빈 절에 오백이 들어갔습니다. 그리고 문을 닫았습니다.

### SC_061 · LOC_006_PYONGYANG (chùa, trong tối) · quân Goguryeo · — · still_kenburns · 8:24–8:34
[ACTION-VI] Ảnh: trong chùa tối, hàng chục mũ trụ sắt lấp lánh nhạt dưới ánh sáng lọt khe cửa; một ngọn đèn dầu bị bàn tay che tắt; tượng Phật trên cao nhìn xuống. Ken-burns đẩy chậm vào khe sáng cửa.
[SOUND] hơi thở nhiều người nén, mưa qua cửa, một tiếng giáp khẽ.
N: 부처 아래서 오백 명이 숨을 죽였습니다. 밖에서 사만이 오고 있었습니다. 기다리는 쪽이 이기는 법이었습니다. 적어도 이 성에서는.

### SC_062 · LOC_007_SALSU (đầm lau bờ bắc, đêm D2 — POV kính đêm) · CHAR_205 · EQP_001 · video8s · 8:34–8:42
[ACTION-VI] HARD CUT: POV kính nhìn đêm xanh lục nhiễu hạt: lau sậy sáng nhạt, nước đen, mưa thành vệt; ở giữa khung, một bóng người lội thấp — rồi bóng dừng. Không thoại.
[SOUND] kính đêm rít nhẹ, nước, mưa.
N: 같은 밤, 살수. 탁발흠은 밤을 보고 있었습니다. 석문령에서 빼앗은 눈이었습니다.

### SC_063 · LOC_007_SALSU (đầm lau bờ bắc) · CHAR_205, 선비 기병 · EQP_001, VEH_206 · video8s · 8:42–8:50
[ACTION-VI] 탁발흠 đi bộ, kính đêm hạ xuống mắt dưới mũ lông cáo, cung trên tay, nước tới đùi; sau lưng, 20 kỵ Tiên Ti đi bộ không ngựa, giãn thành hàng đôi, cung giương; mưa. Tracking từ bên hông, rất tối, chỉ thấy viền người.
[SOUND] lội chậm, mưa, không ai nói.
N: 말은 남쪽 기슭에 두고 왔습니다. 말은 물에서 소리를 냅니다. 그는 스무 명을 데리고 걸어서 갈대로 들어왔습니다. 짐승을 찾는 사냥꾼처럼.

### SC_064 · LOC_007_SALSU (chốt gác đại đội, mép đầm) · 초병 ×2 · EQP_001, WPN_001 · video8s · 8:50–8:58
[ACTION-VI] Chốt gác: hai lính Hàn trong hố lau, một người đeo kính đêm (đèn pin báo pin nhấp nháy đỏ), người kia không; súng bọc vải, dao găm cắm trước mặt; mưa. Cận.
[SOUND] mưa, kính đêm rít, nhấp nháy.
N: 야시경은 넷만 켰습니다. 배터리는 삼십 퍼센트였습니다. 나머지 눈은 다 감았습니다. 이 밤에 이 부대는 넷의 눈으로 보았습니다.

### SC_065 · LOC_007_SALSU (đường lau tới chốt) · CHAR_006 · WPN_001 · video8s · 8:58–9:06
[ACTION-VI] 백성민 bò thấp theo lối lau tới chốt để thay ca, dao găm trong tay, súng trên lưng bọc vải, không kính đêm; anh dừng, nghiêng đầu — nghe gì đó trong mưa. Cận.
[SOUND] mưa, một tiếng lội lệch nhịp rất xa.
N: 백성민은 야시경 없이 갔습니다. 배터리를 아끼려는 것이었습니다. 그는 눈 대신 귀로 걸었습니다.

### SC_066 · LOC_007_SALSU (đầm lau — POV kính đêm 탁발흠) · CHAR_205 · EQP_001 · video8s · 9:06–9:14
[ACTION-VI] POV xanh lục: ba hình người sáng nhạt trong lau cách 30 m — hai ngồi, một đang bò tới; 탁발흠 giơ nắm tay — hàng người sau lưng hắn khựng lại, cúi xuống. Thì thầm.
[SOUND] kính rít, mưa.
탁발흠: 셋. 소리 없이.

### SC_067 · LOC_007_SALSU (chốt gác) · 초병, CHAR_006 · EQP_001 · video8s · 9:14–9:22
[ACTION-VI] Lính gác đeo kính đêm quay đầu — trong ống kính của anh, hai bóng lom khom cách 15 m trong lau; anh đông cứng, tay trái vươn ra sau gõ hai cái lên giày 백성민 vừa bò tới. 백성민 ngừng thở. Cận hai người, tối.
[SOUND] mưa, hai tiếng gõ giày, im.
N: 두 번 두드리는 것. 적이 보인다는 뜻이었습니다. 소리를 내지 말라는 뜻이었습니다.

### SC_068 · LOC_007_SALSU (chốt gác) · CHAR_006, 초병, 선비 기병 ×2 · — · video8s · 9:22–9:30
[ACTION-VI] Hai Tiên Ti lao thấp qua lau tới hố; 백성민 bật dậy đón kẻ thứ nhất — hai người ngã xuống nước, dao găm và đao chuôi vòng khóa nhau dưới mặt nước nâu; lính gác thứ hai ôm chân kẻ thứ hai kéo ngã. Không tiếng súng. Máy thấp, nước bắn.
[SOUND] nước quật, thở gằn, kim loại chạm, mưa — không tiếng súng.
N: 총은 없었습니다. 총소리 하나면 오천이 깨어날 것이었습니다. 이 싸움은 칼과 물로 해야 했습니다.

### SC_069 · LOC_007_SALSU (chốt gác) · 초병 ×2, 선비 기병 · WPN_001 · video8s · 9:30–9:38
[ACTION-VI] Lính gác không kính đêm dùng báng súng bọc vải nện xuống; dây cung Tiên Ti bị cắt bật lên; lính gác kính đêm bị bóp cổ — 백성민 từ dưới nước kéo kẻ đó ra sau; nước sủi. Không cận vết thương.
[SOUND] báng súng, dây cung đứt, nước, mưa.

### SC_070 · LOC_007_SALSU (chốt gác) · CHAR_205, CHAR_006 · EQP_001 · video8s · 9:38–9:46
[ACTION-VI] 탁발흠 tự lao vào từ bên trái, đao chuôi vòng vung; 백성민 xoay người, dao găm rạch ngang cẳng tay trái hắn; 탁발흠 giật lùi, kính đêm lệch trên mắt, mũ lông rơi xuống nước rồi hắn vớt lại. Cận, tối, chỉ ánh xanh nhỏ của kính.
[SOUND] đao rít, dao rạch da, thở rít qua răng, mưa.
N: 탁발흠은 부하 뒤에 서지 않았습니다. 그것이 그가 살아남은 방식이었습니다. 이번에는 그것이 그를 다치게 했습니다.

### SC_071 · LOC_007_SALSU (chốt gác) · CHAR_205, 초병 · EQP_001, WPN_001 · video8s · 9:46–9:54
[ACTION-VI] 탁발흠 quay lưng lao qua lau về phía nam, nước bắn; lính gác không kính giật vải khỏi khẩu K2C1, nâng súng — bàn tay 백성민 từ dưới nước đập nòng súng xuống bùn. Máy trung.
[SOUND] lội chạy xa dần, vải giật, nòng súng đập bùn.
백성민: 쏘지 마.

### SC_072 · LOC_007_SALSU (chốt gác, sau giao tranh) · CHAR_006, 초병 ×2 · — · video8s · 9:54–10:02
[ACTION-VI] Hai xác Tiên Ti nổi úp trong nước lau; lính gác thứ hai ôm cánh tay chảy máu; 백성민 quỳ trong nước tới ngực, thở, quay đầu về hướng bóng chạy. Máy thấp ngang mặt nước.
[SOUND] thở, nước lặng dần, mưa.
N: 둘이 갈대 밑에 남았습니다. 한 사람이 달아났습니다. 달아난 사람이 우두머리였습니다.

### SC_073 · LOC_007_SALSU (chốt gác, nhìn về nam) · CHAR_006 · EQP_001 · video8s · 10:02–10:10
[ACTION-VI] POV 백성민 (mắt thường, đêm đen): trong bóng tối phía nam, một đốm sáng xanh lục nhỏ xíu — mắt kính đêm — nhấp nhô xa dần rồi tắt sau lau. Cận mặt 백성민 rồi đốm sáng.
[SOUND] mưa, lội rất xa.
백성민: 야시경입니다. 우리 겁니다.

### SC_074 · LOC_007_SALSU (bờ nam, chỗ buộc ngựa) · CHAR_205, 선비 기병 · EQP_001, VEH_206 · video8s · 10:10–10:18
[ACTION-VI] 탁발흠 về tới chỗ ngựa, xé vạt áo băng cẳng tay, tháo kính đêm khỏi mũ, cầm nó trước mặt, thở; rồi cười không thành tiếng — hắn đã tìm được thứ cần tìm. Nói với phó của hắn (반말 cộc).
[SOUND] vải xé, ngựa, mưa.
N: 그는 팔을 잃지 않았습니다. 대신 위치를 얻었습니다. 정확한 위치는 아직 아니었습니다. 그러나 갈대밭 안이라는 것은 확실했습니다.
탁발흠: 찾았다. 갈대밭 안이다. 어디쯤인지는 내일 밤에.

### SC_075 · LOC_007_SALSU (đầm lau, aerial đêm) · — · EQP_001 · still_kenburns · 10:18–10:30
[ACTION-VI] Ảnh aerial đêm mưa: bãi lau đen mênh mông, sông xám bạc mờ; ở góc khung phía nam, một đốm xanh lục nhỏ như con đom đóm đang di chuyển về trại có vài đuốc. Ken-burns kéo ra rất chậm.
[SOUND] mưa, gió trên cao.
N: 그날 밤, 갈대밭에서 처음으로 적이 그들보다 멀리 봤습니다.

[Kết thúc Phần 4]

## [Phần 5] 빈 절 — 「빈 절」 / Chứng minh sức mạnh  (10:30–14:00) — GOGURYEO CHỨNG MINH, ĐẠI ĐỘI KHÔNG CÓ MẶT
> Tóm tắt VI: [史] D3, 평양 ngoại thành: 4만 quân Tùy tràn qua cổng thủy vào 나곽 trống — vỡ hàng, cướp lụa, uống rượu; 내호아 "내 성이다. 마음껏 가져가라." Ngõ hẹp im lặng. Khe cửa chùa: 고건무 chờ tới khi đội hình tan hẳn — "지금이다. 문을 열어라." [NARRATOR IM LẶNG 11:20–12:08]: cửa chùa bật mở, 500 tràn ra; lính vác lụa bị chém; ngõ hẹp; cung thủ trên mái; 내호아 "물러나라! 배로!"; chạy về sông, thuyền quá tải lật; narrator: "4만 중 수천 명만 배로 돌아갔습니다." 내호아 thoát trên ngựa không yên; 고건무: "배까지 쫓아라." Thuyền đổ bộ cháy; 고건무 đi qua chợ: "평양은 고구려 사람이 지키오." 내호아 rút ra 해포. Cắt: trại 우중문 30리 dựa núi (D5, "이틀 뒤"): tin thua; 우문술: "장군. 이제 돌아가야 하오." 우중문 nhìn 평양 xa, không đáp; lính luộc dây da.
> Chức năng: BATTLE (sử thuần) · Tài nguyên (địch): 4만 → vài nghìn · Open loop cuối phần: "내호아는 배로 돌아갔습니다. 우중문의 30만은 이제 혼자였습니다."
> Sau mid-roll 2 (14:00): SC_101 aerial trại Tùy dựa núi, khói bếp thưa, không thoại.

### SC_076 · LOC_006_PYONGYANG (aerial cổng thủy ngoại thành) · 4만 Tùy · WPN_201, PROP_021 · still_kenburns · 10:30–10:40
[ACTION-VI] Ảnh aerial mưa: cổng thủy ngoại thành mở toang, dòng giáp bạc và cờ đỏ chảy từ bãi sông qua cổng vào phố; trong phố, dòng người tỏa ra các ngõ như nước tràn; tường nội thành trên đồi đóng kín. Ken-burns từ cổng vào phố.
[SOUND] trống Tùy, reo, mưa.
N: 사흘째 아침. 사만이 나곽으로 들어갔습니다. 문은 열려 있었고, 성벽 위에는 아무도 없었습니다. 내호아는 그것을 항복이라 읽었습니다.

### SC_077 · LOC_006_PYONGYANG (phố chợ) · lính Tùy · WPN_201 · video8s · 10:40–10:48
[ACTION-VI] Lính Tùy đá cửa nhà dân, lôi lụa ra sạp, một người vác nguyên cây lụa lên vai; hai người giành vò rượu, tu ừng ực; một sĩ quan cưỡi ngựa hét giữ hàng — không ai nghe. Tracking qua phố.
[SOUND] cửa gãy, gốm vỡ, cười, sĩ quan hét bị át.
N: 배고픈 병사에게 빈 시장은 명령보다 컸습니다. 대열은 시장 골목마다 한 줄씩 풀렸습니다. 고건무가 원한 그대로였습니다.

### SC_078 · LOC_006_PYONGYANG (phố chợ, đầu phố) · CHAR_204 · WPN_201 · video8s · 10:48–10:56
[ACTION-VI] 내호아 cưỡi ngựa vào đầu phố, thấy lính cướp phá; không quát — cười to, giơ đao chỉ vòng quanh phố.
[SOUND] cười, ngựa, gốm vỡ.
N: 내호아는 대열을 세우지 않았습니다. 그도 시장을 보았습니다.
내호아: 내 성이다. 마음껏 가져가라.

### SC_079 · LOC_006_PYONGYANG (ngõ hẹp cạnh chùa) · lính Tùy · — · video8s · 10:56–11:04
[ACTION-VI] Một lính Tùy vác lụa rẽ vào ngõ hẹp giữa hai dãy nhà gỗ; ngõ vắng ngắt, mưa nhỏ giọt từ mái; anh ta dừng — cảm thấy lạ — nhìn cánh cửa chùa gỗ ba gian đóng kín cuối ngõ; rồi nhún vai đi tiếp. Máy từ sau lưng.
[SOUND] mưa nhỏ giọt, bước chân một người, im.
N: 골목은 너무 조용했습니다. 조용함을 이상하게 여긴 병사도 있었습니다. 그러나 비단이 더 무거웠습니다.

### SC_080 · LOC_006_PYONGYANG (chùa, khe cửa) · CHAR_103 · — · video8s · 11:04–11:12
[ACTION-VI] Trong chùa tối: mắt 고건무 áp vào khe cửa — ngoài kia phố chợ đầy lính Tùy rải rác, không hàng lối, ngựa sĩ quan bị bỏ; sau lưng ông, 500 người đứng dậy không tiếng động, giáo hạ ngang. Cận mắt.
[SOUND] hơi thở, giáp khẽ, ngoài cửa tiếng cướp phá.
N: 고건무는 기다렸습니다. 사만이 다 들어올 때까지. 대열이 완전히 풀릴 때까지. 기다림은 그의 병법이었습니다.

### SC_081 · LOC_006_PYONGYANG (chùa, trước cửa) · CHAR_103 · — · video8s · 11:12–11:20
[ACTION-VI] 고건무 đứng thẳng, khiên tròn lên tay trái, giáo tay phải, quay lại nhìn 500 người trong tối một nhịp; rồi quay ra cửa, nói thấp (하게체).
[SOUND] khiên chạm giáp, im.
고건무: 지금이다. 문을 열어라.

[NARRATOR IM LẶNG — 11:20 → 12:08]

### SC_082 · LOC_006_PYONGYANG (cửa chùa → phố) · quân Goguryeo, CHAR_103 · — · video8s · 11:20–11:28
[ACTION-VI] Cửa chùa ba gian bật tung ra ngoài; 500 quân Goguryeo tràn ra thành mũi nêm giáo dựng, 고건무 ở mũi; mưa hắt; lính Tùy trong phố ngoảnh lại, lụa rơi. Wide từ giữa phố.
[SOUND] cửa gỗ nện, hàng trăm giày trên đá, tiếng hô Goguryeo ngắn.

### SC_083 · LOC_006_PYONGYANG (phố chợ) · quân Goguryeo, lính Tùy · WPN_201 · video8s · 11:28–11:36
[ACTION-VI] Lính Tùy tay lụa tay rượu bị mũi nêm cuốn — người bỏ chạy, người vấp lụa ngã, người cố rút đao quá muộn; không hàng ngũ nào để chống. Wide, không gore.
[SOUND] giáo, gốm vỡ, thét, mưa.

### SC_084 · LOC_006_PYONGYANG (ngõ hẹp) · CHAR_103, 수 장교 · — · video8s · 11:36–11:44
[ACTION-VI] Ngõ hẹp: 고건무 đâm giáo, chặn đao bằng khiên; một sĩ quan Tùy cưỡi ngựa cố tập hợp lính — ngựa bị giáo dọa dựng lên, hất ông ta xuống. Máy trung, sát.
[SOUND] khiên gỗ, ngựa hí, giáo.

### SC_085 · LOC_006_PYONGYANG (ngõ hẹp, mái nhà) · cung thủ Goguryeo, lính Tùy · WPN_101 · video8s · 11:44–11:52
[ACTION-VI] Trên mái ngói hai bên ngõ, cung thủ Goguryeo bật dậy bắn xuống dòng lính Tùy chen nhau trong ngõ; lính Tùy đạp lên nhau lùi về phía cổng thủy. Low-angle từ ngõ lên mái.
[SOUND] dây cung liên tiếp, giày trượt trên đá ướt, thét.

### SC_086 · LOC_006_PYONGYANG (đầu phố, cổng thủy) · CHAR_204 · WPN_201 · video8s · 11:52–12:00
[ACTION-VI] 내호아 trên ngựa gần cổng thủy, thấy lính mình chạy về phía ông, lụa bỏ đầy phố; mặt ông đổi từ cười sang trắng; gào.
[SOUND] ngựa, thét, mưa, cung xa.
내호아: 시장이 왜 이리 조용… 물러나라! 배로!

### SC_087 · LOC_006_PYONGYANG (cổng thủy → bãi sông) · lính Tùy, kỵ Goguryeo · VEH_101 · video8s · 12:00–12:08
[ACTION-VI] Dòng lính Tùy chen qua cổng thủy ra bãi cát; từ hai ngõ bên, kỵ binh Goguryeo 개마무사 lao ra cắt ngang dòng người; lụa và đao rơi khắp bãi. Aerial trung.
[SOUND] vó ngựa, giáp, thét, sóng.

### SC_088 · LOC_006_PYONGYANG (bãi sông, thuyền) · lính Tùy · VEH_204 · video8s · 12:08–12:16
[ACTION-VI] Bãi: lính lội ra thuyền phẳng, bám mạn; thuyền quá tải nghiêng, lật; cung thủ Goguryeo trên bờ bắn xuống nước; 누선 lớn ngoài xa hạ buồm chèo lùi. Wide.
[SOUND] thuyền lật, nước, dây cung, trống thủy quân rối loạn.
N: 4만 중 수천 명만 배로 돌아갔습니다. 나머지는 시장과 골목과 강가에 남았습니다. 삼국사기는 그날을 한 줄로 적었습니다. 고구려의 매복이 있었다고.

### SC_089 · LOC_006_PYONGYANG (bãi sông) · CHAR_204 · VEH_204 · video8s · 12:16–12:24
[ACTION-VI] 내호아 bị ngựa hất xuống bãi, mũ vành móp; ông chộp dây cương một con ngựa không yên bỏ chạy, nhảy lên, thúc xuống nước về phía 누선 gần nhất; áo choàng dầu cháy một góc từ đuốc rơi. Tracking theo ngựa xuống nước.
[SOUND] ngựa, nước, lửa nhỏ, thét sau lưng.
N: 내호아는 안장 없는 말로 강에 들어갔습니다. 배까지 닿았습니다. 그의 사만은 닿지 못했습니다.

### SC_090 · LOC_006_PYONGYANG (cổng thủy) · CHAR_103 · — · video8s · 12:24–12:32
[ACTION-VI] 고건무 đứng dưới vòm cổng thủy, mũ tháo, tóc ướt, máu trên cẳng tay, khiên nứt một mảnh; nhìn ra bãi sông đầy người và thuyền lật; giọng phẳng (하게체 với sĩ quan bên cạnh).
[SOUND] mưa, thét xa, sóng.
N: 이기는 것은 절반이었습니다. 나머지 절반은 쫓는 것이었습니다. 고건무는 배까지 쫓게 했습니다.
고건무: 배까지 쫓아라.

### SC_091 · LOC_006_PYONGYANG (sông, thuyền cháy) · — · VEH_204, PROP_021 · still_kenburns · 12:32–12:42
[ACTION-VI] Ảnh: thuyền đổ bộ cháy trên nước xám, khói đen trộn mưa; 누선 lớn chèo lùi ra giữa sông, cờ đỏ rũ; trên bãi, cờ Tùy gãy cắm nghiêng trong cát. Ken-burns kéo ra từ ngọn lửa tới sông.
[SOUND] lửa, gỗ nổ, chèo xa, mưa.
N: 배가 탔습니다. 강회의 배였습니다. 동래에서 여기까지 온 배였습니다. 내호아는 그날 밤 강을 내려가 바다로 나갔습니다.

### SC_092 · LOC_006_PYONGYANG (phố chợ, sau trận) · CHAR_103 · PROP_021 · video8s · 12:42–12:50
[ACTION-VI] 고건무 đi bộ qua phố chợ tan hoang: xác lính Tùy phủ vải (không cận), lụa ngâm bùn, vò rượu vỡ; ông cúi nhặt một lá cờ Tùy ướt, nhìn, thả xuống; nói với sĩ quan đi sau (하오체 — lời nói cho cả thành nghe).
[SOUND] mưa, giày trên gốm vỡ, cờ ướt rơi.
N: 그는 사만을 오백으로 깼습니다. 쇠수레도, 천둥도 없이. 평양은 그렇게 지켜졌습니다.
고건무: 평양은 고구려 사람이 지키오.

### SC_093 · LOC_006_PYONGYANG (해포, vịnh biển — aerial) · — · VEH_204 · still_kenburns · 12:50–13:00
[ACTION-VI] Ảnh aerial: một vịnh biển xám, hàng chục 누선 neo san sát, buồm cuộn, thuyền vơi người, mưa mù; không có bờ Goguryeo nào gần. Ken-burns kéo ra tới biển.
[SOUND] sóng, mưa, gỗ thuyền kêu.
N: 해포. 내호아는 거기서 멈췄습니다. 다시는 강을 거슬러 오르지 않았습니다. 우중문을 만나러 가지도 않았습니다. 수나라의 물길은 그날로 끊겼습니다.

### SC_094 · LOC_008_GOGURYEO_VILLAGE (đồi phía bắc 평양, trại Tùy 30리 — lều 우중문) · 전령, CHAR_202, CHAR_203 · PROP_021 · video8s · 13:00–13:08
[ACTION-VI] Lều lớn dựa sườn núi, mưa gõ mái da; một 전령 Tùy bùn tới ngực quỳ, hai tay dâng thẻ tre; 우중문 ngồi ghế gấp, 우문술 đứng bên, thẻ tre trong tay. Máy trung.
[SOUND] mưa trên da lều, thở của người quỳ.
N: 그 소식은 이틀 뒤 우중문에게 닿았습니다. 삼십만은 그때 평양에서 삼십 리 떨어진 산기슭에 진을 치고 있었습니다. 다섯 날을 걸어온 길이었습니다.

### SC_095 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202 · — · video8s · 13:08–13:16
[ACTION-VI] 우중문 đọc thẻ tre, mặt đỏ dần lên tới thái dương, râu trắng rung; ngẩng lên nhìn 전령, giọng gầm.
[SOUND] thẻ tre siết, mưa.
우중문: 내호아가 배로 도망쳤다고?

### SC_096 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_203 · — · video8s · 13:16–13:24
[ACTION-VI] 우문술 (giáp sẫm, râu xám ngắn, cổ lông ướt) không nhìn 우중문 — nhìn thẻ tre của mình: các vạch lương; rồi nói, chậm, 하오체 khô.
[SOUND] mưa, thẻ tre.
N: 우문술은 열흘 전부터 같은 말을 했습니다. 이번에는 숫자가 그의 편이었습니다.
우문술: 장군. 이제 돌아가야 하오.

### SC_097 · LOC_008_GOGURYEO_VILLAGE (cửa lều, nhìn về nam) · CHAR_202 · — · video8s · 13:24–13:32
[ACTION-VI] 우중문 đứng dậy, vén rèm lều, nhìn về nam: qua mưa, xa xa trên một đồi thấp, tường thành 평양 xám mờ như một nét vẽ. Máy từ sau vai ông.
[SOUND] mưa, trại ướt.
N: 삼십 리. 십이 킬로였습니다. 보이는 거리였습니다. 그리고 닿을 수 없는 거리였습니다. 배가 없었고, 밥이 없었습니다.

### SC_098 · LOC_008_GOGURYEO_VILLAGE (trại Tùy, bếp) · lính Tùy · — · video8s · 13:32–13:40
[ACTION-VI] Insert: lính Tùy quanh nồi đất — luộc dây da giáp và yên ngựa cắt nhỏ; một người vớt miếng da nhai; mưa tắt lửa, người khác che bằng khiên.
[SOUND] lửa xèo, nhai da, mưa.
N: 병사들은 가죽끈을 삶았습니다. 안장을 잘라 먹었습니다. 삼십만이 그렇게 먹고 있었습니다.

### SC_099 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202, CHAR_203 · — · video8s · 13:40–13:48
[ACTION-VI] 우중문 quay vào, bóp nát thẻ tre trong tay, không trả lời 우문술; ngồi xuống ghế, nhìn tấm bản đồ da trên bàn — 평양 gần, 살수 xa sau lưng. 우문술 chờ.
[SOUND] thẻ tre gãy, mưa.
N: 우중문은 대답하지 않았습니다. 돌아간다는 말은 그의 입에서 나올 수 없었습니다. 황제 앞에서 큰소리를 친 사람이었기 때문입니다.

### SC_100 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202 · — · still_kenburns · 13:48–14:00
[ACTION-VI] Ảnh cận: mặt 우중문 dưới đèn dầu, râu trắng ướt, hai gương ngực lấm bùn, mắt nhìn bản đồ; bàn tay nắm thẻ tre gãy. Ken-burns đẩy rất chậm vào mắt.
[SOUND] mưa, đèn dầu.
N: 내호아는 배로 돌아갔습니다. 우중문의 30만은 이제 혼자였습니다.

[MID-ROLL 2 · 14:00]

[Kết thúc Phần 5]

## [Phần 6] 누구의 군대인가 — 「누구의 군대인가」 / Liên minh không dễ  (14:00–17:30)
> Tóm tắt VI: Sau mid-roll: aerial trại Tùy dựa núi, khói bếp thưa, không thoại. (a) D3 đêm, nội điện 평양: 고건무 vào với mặt lem khói; 영양왕 (áo choàng đen khoác long bào) với 을지문덕 về thành một đêm. Vua hỏi 뇌군 ở đâu — "살수 갈대밭". Tay vua trên bản đồ. "전쟁이 끝나면 저들은 누구의 군대인가?" 고건무: giải tán, thu vũ khí. 을지문덕: "지금은 그들이 필요합니다. 그다음은 그다음에." Vua viết một dòng, 해모루 mang đi, phi đêm 80 km. (b) D4 sáng, đảo lau 1: 해모루 đọc thư cho 한승우: "그 뒤에 그대들은 누구의 군대인가?" — 한승우 gấp vào áo, cạnh mũi tên. Mini-contact: kỵ Tiên Ti trên mô cát bắn tên dò vào lau, tên cắm cách mặt lính 1 m — không ai động. Mâu thuẫn: 오태민 "태오는 저기 우리에 있고, 우리는 진흙에 누워 있습니다." 한승우 lặp rule; 오태민 "역사책이 우리 94명을 지켜줍니까? 이제 92명입니다." 박기철 trên xích K2: "이십 킬로. 그게 우리 편입니다." 서아: 아리 thấy 태오 bị đánh vào chân. Im lặng. 해모루 nhìn.
> Chức năng: POLITICS · Tài nguyên: "92명" nói thành lời lần 2 · Open loop cuối phần: "왕은 답을 기다렸습니다. 한승우는 답을 쓰지 않았습니다."

### SC_101 · LOC_008_GOGURYEO_VILLAGE (aerial trại Tùy 30리 dựa núi) · — · PROP_021 · still_kenburns · 14:00–14:10
[ACTION-VI] Ảnh aerial mưa: trại Tùy khổng lồ dựa vào sườn núi xanh, lều da xám nối tới chân đồi, chỉ vài chục cột khói bếp mỏng lẻ tẻ giữa hàng vạn lều — quá ít cho 30만; cờ đỏ rũ. Ken-burns kéo ra chậm. Không thoại, không narrator.
[SOUND] mưa, gió trên cao, trống trại thưa.

### SC_102 · LOC_006_PYONGYANG (nội điện — hành lang mưa, đêm D3) · CHAR_103, lính gác · — · video8s · 14:10–14:18
[ACTION-VI] Đêm, hành lang gỗ nội điện, mưa xối sân đá; 고건무 đi nhanh, mũ cắp nách, mặt lem khói, cẳng tay băng vải, khiên nứt để lại cho lính gác ở cửa; cửa gỗ chạm mở ra ánh đèn dầu. Tracking theo ông.
[SOUND] mưa sân đá, giày trên gỗ, cửa.
N: 같은 날 밤. 고건무는 갑옷을 벗지 않고 내전으로 들어갔습니다. 대왕이 기다리고 있었습니다. 그리고 또 한 사람이 있었습니다.

### SC_103 · LOC_006_PYONGYANG (nội điện) · CHAR_102, CHAR_101, CHAR_103 · PROP_012 · video8s · 14:18–14:26
[ACTION-VI] Đại điện: cột son, ngai đen viền vàng, cờ 삼족오 lớn sau ngai; 영양왕 (백라관, long bào đỏ thẫm, áo choàng đen khoác ngoài) ngồi; bên trái dưới bậc, 을지문덕 ngồi trên chiếu trước bàn thấp, giáp ướt, tóc bạc; 고건무 quỳ một gối chào. Wide đối xứng.
[SOUND] đèn dầu, mưa ngoài hiên, giáp.
N: 을지문덕이었습니다. 들에서 하룻밤만 성으로 들어온 것이었습니다. 삼십만은 삼십 리 밖에 있었습니다. 삼십 리는 그에게 하룻밤 거리였습니다.

### SC_104 · LOC_006_PYONGYANG (nội điện) · CHAR_102 · — · video8s · 14:26–14:34
[ACTION-VI] 영양왕 không hỏi về trận vừa thắng — nhìn 을지문덕, giọng chậm, mỗi chữ một cân nhắc.
[SOUND] đèn dầu.
N: 대왕은 오늘의 승리를 묻지 않았습니다. 다른 것을 물었습니다.
영양왕: 대장군. 그 뇌군은 지금 어디 있는가?

### SC_105 · LOC_006_PYONGYANG (nội điện) · CHAR_101 · — · video8s · 14:34–14:42
[ACTION-VI] 을지문덕 không ngẩng cao; trả lời ngắn, 합쇼체, mắt vẫn trên bàn thấp.
[SOUND] mưa.
을지문덕: 살수 갈대밭에 있습니다. 삼십만이 그 위로 지나갔습니다.

### SC_106 · LOC_006_PYONGYANG (nội điện, bàn thấp) · CHAR_102 · PROP_001 · video8s · 14:42–14:50
[ACTION-VI] Insert: bàn thấp có bản đồ da vẽ mực; ngón tay vua (nhẫn vàng nhỏ) đặt lên nét sông phía bắc, trượt chậm xuống 평양, dừng; đèn dầu run. Không thoại.
[SOUND] ngón tay trên da, đèn.
N: 살수에서 평양까지 손가락 한 마디였습니다. 그 한 마디 안에 삼십만과 92명이 있었습니다. 대왕은 92명을 세고 있었습니다.

### SC_107 · LOC_006_PYONGYANG (nội điện) · CHAR_102 · — · video8s · 14:50–14:58
[ACTION-VI] 영양왕 ngẩng lên, nhìn hai người, hỏi câu ông đã nghĩ từ lâu.
[SOUND] đèn, mưa.
영양왕: 전쟁이 끝나면 저들은 누구의 군대인가?

### SC_108 · LOC_006_PYONGYANG (nội điện) · CHAR_103 · — · video8s · 14:58–15:06
[ACTION-VI] 고건무 đứng dậy, bước tới bàn thấp, đặt bàn tay băng vải lên bản đồ chỗ 살수 — walk-and-talk; 합쇼체 với vua, thẳng, cộc.
[SOUND] giày, da bản đồ.
N: 고건무는 오늘 사만을 오백으로 깼습니다. 그에게 쇠수레는 필요 없었습니다. 필요 없는 것은 위험한 것이었습니다.
고건무: 흩어 보내고 쇠를 거두어야 합니다, 전하.

### SC_109 · LOC_006_PYONGYANG (nội điện) · CHAR_101 · — · video8s · 15:06–15:14
[ACTION-VI] 을지문덕 vẫn ngồi; ngón tay ông gõ hai lần lên bàn — không lên bản đồ; nói không nhìn ai, sắc, ngắn.
[SOUND] ngón gõ gỗ, đèn.
N: 을지문덕은 다음을 말하지 않았습니다. 그는 늘 지금만 말했습니다. 지금은 삼십만이 돌아올 길 위에 있었습니다.
을지문덕: 지금은 그들이 필요합니다. 그다음은 그다음에.

### SC_110 · LOC_006_PYONGYANG (nội điện) · CHAR_102, CHAR_105 · PROP_013 · video8s · 15:14–15:22
[ACTION-VI] 영양왕 cầm bút lông, viết một cột chữ ngắn trên lụa vàng nhạt, thổi khô, cuộn; 해모루 (bùn tới đùi, radio kẹp trên giáp) quỳ ở ngưỡng cửa nhận lụa bằng hai tay. Máy từ bút tới cửa.
[SOUND] bút lông, lụa, mưa cửa mở.
N: 대왕은 한 줄을 썼습니다. 답이 아니라 물음이었습니다. 해모루가 그것을 받았습니다. 그는 밤새 달릴 것이었습니다.
영양왕: 한 대장에게 전하라. 답은 네가 듣고 오라.

### SC_111 · LOC_006_PYONGYANG (đường ven sông đêm mưa, rời 평양) · CHAR_105 · VEH_101 · still_kenburns · 15:22–15:34
[ACTION-VI] Ảnh: 해모루 phi ngựa trong đêm mưa trên đường đất ven sông, áo choàng bay, một kỵ hộ tống phía sau dắt ngựa thay; đèn thành 평양 nhỏ dần sau lưng. Ken-burns trượt theo hướng bắc.
[SOUND] vó ngựa trên bùn, mưa, thở ngựa.
N: 평양에서 살수까지 이백 리. 말을 두 번 바꿨습니다. 해모루는 이 길을 이레 사이에 세 번 달릴 것이었습니다. 왕과 장군과 갈대밭 사이를 잇는 것은 이 사람 하나였습니다.

### SC_112 · LOC_007_SALSU (đảo lau 1, sáng D4) · CHAR_105, lính Hàn · PROP_020 · video8s · 15:34–15:42
[ACTION-VI] Sáng xám: 해모루 lội tới đảo lau từ phía làng, ngựa để lại, bùn tới đùi, mắt trũng; hai lính gác hạ súng khi nhận ra lông trắng trên mũ; anh gật, đi thẳng vào. Tracking.
[SOUND] nước, lau, chim nước.
N: 넷째 날 아침. 해모루는 걸어서 섬으로 들어왔습니다. 말은 마을에 두었습니다. 그는 이 부대의 규칙을 알았습니다. 소리 내는 것은 들어오지 못했습니다.

### SC_113 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_105, CHAR_001 · PROP_013 · video8s · 15:42–15:50
[ACTION-VI] 해모루 ngồi xuống trước 한승우, rút cuộn lụa từ trong giáp (ướt mép), đưa hai tay; 하오체.
[SOUND] lụa, mưa nhỏ.
해모루: 대왕의 글이오. 답을 기다리시오.

### SC_114 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_105, CHAR_001 · PROP_013 · video8s · 15:50–15:58
[ACTION-VI] Cận lụa mở trên hai bàn tay bùn của 한승우: một cột chữ Hán brush calligraphy; ông không đọc được — nhìn 해모루; 해모루 đọc thành tiếng Hàn, chậm.
[SOUND] lụa, mưa.
N: 한승우는 한문을 읽지 못했습니다. 해모루가 읽어 주었습니다. 이천 년 전의 왕이 이천 년 뒤의 군인에게 물었습니다.
해모루: "그 뒤에 그대들은 누구의 군대인가?"

### SC_115 · LOC_007_SALSU (đảo lau 1, dưới mái lau) · CHAR_001 · PROP_013, PROP_015 · video8s · 15:58–16:06
[ACTION-VI] 한승우 không trả lời; gấp lụa làm tư, chậm, nhét vào túi ngực áo giáp — cạnh cán mũi tên Goguryeo; cài nắp túi. 해모루 nhìn tay ông, không hỏi lại. Cận tay.
[SOUND] lụa gấp, khóa túi, mưa.
N: 그는 답 대신 글을 접었습니다. 화살 옆에 넣었습니다. 요동성 동문에서 뽑은 화살이었습니다. 이 부대가 이 땅에 남긴 첫날의 것이었습니다.

### SC_116 · LOC_007_SALSU (mép đảo lau 1, nhìn ra mô cát) · 선비 기병 ×2, lính Hàn · VEH_206, WPN_101 · video8s · 16:06–16:14
[ACTION-VI] Trên mô cát cách 300 m, hai kỵ Tiên Ti ghìm ngựa, giương cung bắn mù vào bãi lau — ba mũi tên rít qua ngọn lau; một mũi cắm phập xuống bùn cách mặt lính Hàn đang nằm đúng một mét. Anh không động. Máy từ mắt anh lên mũi tên rung.
[SOUND] dây cung xa, tên rít qua lau, cắm bùn.
N: 그날 아침부터 탁발흠은 낚시를 시작했습니다. 갈대에 화살을 던지고 무엇이 튀어나오는지 보는 것이었습니다. 총소리 하나면 그는 위치를 얻을 것이었습니다.

### SC_117 · LOC_007_SALSU (mép đảo lau 1) · CHAR_006, lính Hàn · VEH_206 · video8s · 16:14–16:22
[ACTION-VI] 백성민 nằm cách đó 5 m, bàn tay xòe ép xuống bùn — ký hiệu "không động"; hai kỵ Tiên Ti nhìn lau một lúc, quay ngựa về nam. Mũi tên vẫn rung trước mặt lính.
[SOUND] lau, vó ngựa xa dần, mưa.
N: 아무것도 튀어나오지 않았습니다. 기병 둘이 돌아갔습니다. 화살은 그 자리에 남았습니다. 아무도 뽑지 않았습니다.

### SC_118 · LOC_007_SALSU (đảo lau 1, lối bùn) · CHAR_002, CHAR_001 · — · video8s · 16:22–16:30
[ACTION-VI] 오태민 đi sau 한승우 dọc lối bùn giữa lau (walk-and-talk, khom người), tay áo rách hẳn, cẳng tay bầm; giọng thấp nhưng từng chữ nặng.
[SOUND] bùn, lau, mưa.
오태민: 태오는 저기 우리에 있고, 우리는 진흙에 누워 있습니다.

### SC_119 · LOC_007_SALSU (đảo lau 1, lối bùn) · CHAR_001, CHAR_002 · — · video8s · 16:30–16:38
[ACTION-VI] 한승우 dừng, quay lại, mặt sát 오태민; nói câu ông đã nói ở 요동성 — lần này chậm hơn.
[SOUND] mưa.
N: 요동성에서 한 말이었습니다. 그때는 규칙이었습니다. 지금은 변명처럼 들렸습니다. 그도 알았습니다.
한승우: 이 싸움은 역사가 이미 이겼다. 우리는 망치지만 않으면 된다.

### SC_120 · LOC_007_SALSU (đảo lau 1, lối bùn) · CHAR_002 · — · video8s · 16:38–16:46
[ACTION-VI] 오태민 không lùi; câu hỏi cũ, thêm một con số mới.
[SOUND] mưa, lau.
오태민: 역사책이 우리 94명을 지켜줍니까? 이제 92명입니다.

### SC_121 · LOC_007_SALSU (đảo lau 1, K2) · CHAR_003 · VEH_001, PROP_001 · video8s · 16:46–16:54
[ACTION-VI] Insert: 박기철 ngồi trên váy xích K2 phủ bùn, sổ mở trên đùi, không ngẩng lên; nói với hai người đang đứng cách 3 m — đứng về phía 한승우 theo cách của ông.
[SOUND] bút chì, mưa trên bùn xe.
N: 박기철은 편을 들지 않았습니다. 숫자를 들었습니다. 이십 킬로는 전차를 우리에까지 데려가지 못했습니다.
박기철: 이십 킬로. 그게 우리 편입니다.

### SC_122 · LOC_007_SALSU (đảo lau 1, lối bùn) · CHAR_004, CHAR_002 · — · video8s · 16:54–17:02
[ACTION-VI] 서아 tới, đứng giữa hai người, không nhìn ai — nói với cả hai, 다나까 ngắn; 오태민 quay phắt sang cô.
[SOUND] mưa.
서아: 아리가 봤습니다. 태오 발을, 몽둥이로 때렸답니다.

### SC_123 · LOC_007_SALSU (đảo lau 1, lối bùn) · CHAR_001, CHAR_002 · — · video8s · 17:02–17:10
[ACTION-VI] Im lặng: 오태민 quay lưng đi về phía mép sông; 한승우 đứng nhìn theo, rồi nhìn xuống dòng nước dâng qua lau; mưa dày. Máy tĩnh, hai người xa nhau dần trong khung.
[SOUND] mưa, lau, nước.
N: 아무도 더 말하지 않았습니다. 말이 끝난 자리에 숫자만 남았습니다. 92명. 이십 킬로. 여덟 발. 그리고 강 건너 하나.

### SC_124 · LOC_007_SALSU (đảo lau 1, mép) · CHAR_105 · EQP_002 · video8s · 17:10–17:18
[ACTION-VI] 해모루 ngồi ở mép đảo, radio trên giáp, nhìn ba người Hàn Quốc tản ra ba hướng; anh xoay xoay tù và trong tay — bảy vạch khắc trên cán. Cận mặt.
[SOUND] mưa, sừng chạm giáp.
N: 해모루는 이 다툼을 알았습니다. 모든 군대에 있는 다툼이었습니다. 쓰려는 사람과 아끼려는 사람. 그는 왕에게 무엇을 전해야 할지 아직 몰랐습니다.

### SC_125 · LOC_007_SALSU (đảo lau 1) · CHAR_001 · PROP_013, PROP_015 · still_kenburns · 17:18–17:30
[ACTION-VI] Ảnh cận: túi ngực áo giáp 한승우 dưới mưa — góc lụa vàng nhạt lộ ra cạnh cán mũi tên xám, giọt nước lăn trên vải rằn ri; ken-burns đẩy rất chậm vào góc lụa.
[SOUND] mưa.
N: 왕은 답을 기다렸습니다. 한승우는 답을 쓰지 않았습니다.

[Kết thúc Phần 6]

## [Phần 7] 북과 횃불 — 「북과 횃불」 / Kẻ địch thích nghi  (17:30–21:00)
> Tóm tắt VI: Chiều D4: 탁발흠 cho khiêng cũi 태오 ra bờ nam trong tầm nhìn — mồi; 백성민 rồi 오태민 nhìn qua ống nhòm; 탁발흠 hỏi 태오 qua 통역 — "모릅니다"; bài học nói thành lời: "젖은 갈대는 안 탄다. 그럼 몰아낸다. 짐승처럼." Đêm: 200 đuốc, trống trên xe bò; kính đêm dẫn hắn theo vết chốt gác; vòng đuốc từ đông và nam lùa đại đội về phía bãi cạn — nơi 500 cung thủ quỳ chờ; 한승우 giữ im tới khi tên rơi mù, một người trúng vai → "박격포, 횃불 선. 스무 발." Cối, K3, PZF ×3 vào bè đuốc; vòng vây chưa vỡ, một người ngã (tên vào cổ). [NARRATOR IM LẶNG 19:39–20:11] K2 hai viên vào khối đuốc cửa bãi cạn — sấm giữa đêm mưa; kính đêm 탁발흠 lóa trắng. Hậu quân Tùy nghe. Đại đội trượt 3 km thượng lưu về đảo lau 2 với một xác và một người tên vào bụng. 전령 phi về nam: "뒤에서 천둥이 울렸습니다. 뇌군이 우리 뒤에 있습니다." 우중문 tái mặt. 을지문덕 (D5, đồi bắc 평양) nhận báo của 해모루: "좋소. 서두르게 하시오."
> Chức năng: THREAT (turning point) · Tài nguyên: **K2 8→6** · cối 50→30 · PZF 9→6 · K3 −800 · 2 thương vong · Enemy adaptation: mồi + trống/đuốc lùa, nhắm cửa bãi cạn · Payoff: lau ướt (P2) · Open loop cuối phần: "뒤에서 천둥이 울렸다. 뇌군이 우리 뒤에 있다."
> Sau mid-roll 3 (21:00): SC_152 bình minh đảo lau 2, mưa, xác bọc poncho, không thoại.

### SC_126 · LOC_007_SALSU (bờ nam, bãi cát trước trại hậu quân, chiều D4) · CHAR_005, 선비 기병 · — · video8s · 17:30–17:38
[ACTION-VI] Bốn lính Tiên Ti khiêng cũi tre ra khỏi trại, đặt xuống bãi cát ngay mép nước bờ nam, chỗ nhìn thẳng sang bãi lau bờ bắc; trong cũi 태오 ngồi co, chân trần, bàn chân phải sưng tím; áo rằn ri rách, không mũ, không giáp. Wide từ phía sông.
[SOUND] cũi đặt cát, dây da, mưa, sông.
N: 넷째 날 오후. 탁발흠은 우리를 강가로 옮겼습니다. 갈대밭에서 보이는 자리였습니다. 그는 낚시를 계속했습니다. 이번 미끼는 사람이었습니다.

### SC_127 · LOC_007_SALSU (mép đảo lau 1) · CHAR_006, CHAR_002 · PROP_006 · video8s · 17:38–17:46
[ACTION-VI] 백성민 nhìn qua ống nhòm — hạ xuống, mặt không đổi; 오태민 nằm cạnh giật ống nhòm, nhìn: 태오 trong cũi ngẩng mặt về phía lau như biết có ai đang nhìn; ngón tay 오태민 trắng bệch trên ống nhòm.
[SOUND] mưa, ống nhòm chạm mũ.
N: 이 킬로 밖에서도 얼굴이 보였습니다. 스물한 살의 얼굴이었습니다.
오태민: 미끼인 거 압니다. 그래도 저건 태오입니다.

### SC_128 · LOC_007_SALSU (bờ nam, cạnh cũi) · CHAR_205, 통역, CHAR_005 · EQP_001 · video8s · 17:46–17:54
[ACTION-VI] 탁발흠 ngồi xổm trước cũi, cẳng tay trái băng vải, kính đêm trên mũ; bên cạnh, 통역 Goguryeo bị trói tay trước, tóc rối, dịch lời hắn sang tiếng Hàn (quy ước P-11); 태오 nhìn xuống cát, trả lời một từ. Máy qua nan tre.
[SOUND] mưa, nan tre, giọng khàn.
통역: 갈대밭에 네 편이 있느냐고 묻는다.
장태오: 모릅니다.

### SC_129 · LOC_007_SALSU (bờ nam, cạnh cũi) · CHAR_205, 선비 기병 (phó) · EQP_001 · video8s · 17:54–18:02
[ACTION-VI] 탁발흠 đứng dậy, nhìn sang bãi lau bờ bắc rất lâu; bốc một nắm lau ướt trên cát, bóp — nước chảy; ném xuống; nói với phó (반말 cộc) — bài học của đêm 요동성.
[SOUND] lau ướt, mưa, trại.
N: 요동성에서 그는 기름을 태웠습니다. 여기는 태울 것이 없었습니다. 그래서 그는 다른 것을 골랐습니다. 몰이였습니다. 초원에서 늑대를 잡던 방식이었습니다.
탁발흠: 젖은 갈대는 안 탄다. 그럼 몰아낸다. 짐승처럼.

### SC_130 · LOC_007_SALSU (bờ nam, trại hậu quân, đêm D4) · lính Tùy, 선비 기병 · PROP_016, PROP_017 · still_kenburns · 18:02–18:11
[ACTION-VI] Ảnh đêm: hàng trăm đuốc được châm dọc bờ nam thành dải lửa; trống lớn Tùy đặt trên xe bò, hai người đánh; kỵ Tiên Ti cầm đuốc lội xuống nước thành hàng cong. Ken-burns trượt dọc dải lửa.
[SOUND] trống Tùy nặng, lửa đuốc, ngựa.
N: 이백 개의 횃불. 수레 위의 북. 동쪽과 남쪽에서 반달처럼 조여 서쪽 여울로 몹니다. 여울 어귀에는 궁수 오백이 무릎을 꿇고 기다립니다. 늑대가 몰려 나오는 자리였습니다.

### SC_131 · LOC_007_SALSU (đầm lau bờ bắc — POV kính đêm) · CHAR_205 · EQP_001 · video8s · 18:11–18:19
[ACTION-VI] POV xanh lục: 탁발흠 lội theo lối lau bị dẫm nát — vết bùn, một chiếc găng đen Hàn Quốc rơi sáng nhạt trên lau; hắn nhặt, ngửi, đi tiếp; sau hắn, 20 người đi bộ không đuốc. 
[SOUND] kính rít, lội, mưa, trống xa sau lưng.
N: 횃불은 미끼고 북은 소리였습니다. 진짜 사냥꾼은 어둠 속에서 걸었습니다. 이틀 전 밤의 길이 그를 섬으로 데려갔습니다.

### SC_132 · LOC_007_SALSU (đảo lau 1, đêm) · 초병, CHAR_001 · WPN_001 · video8s · 18:19–18:27
[ACTION-VI] Lính gác trên đảo ngẩng đầu — tiếng trống từ đông; rồi một hàng đốm lửa hiện lên trong lau cách 800 m, cong dần; 한승우 bật dậy khỏi mái lau, mũ chưa đội, nhìn dải lửa.
[SOUND] trống dội qua nước, lửa xa, lau.
N: 북소리는 동쪽에서 왔습니다. 그리고 남쪽에서도 왔습니다. 오지 않는 쪽은 서쪽뿐이었습니다. 서쪽은 여울이었습니다.

### SC_133 · LOC_007_SALSU (đảo lau 1, trên mô bùn K2) · CHAR_001, CHAR_006 · VEH_001 · video8s · 18:27–18:35
[ACTION-VI] 한승우 và 백성민 đứng trên nóc K2 phủ bùn nhìn ra: dải đuốc cong từ đông và nam như một cánh tay ôm, trống dồn, khoảng trống duy nhất mở về phía tây — bãi cạn. 백성민 nói không quay đầu.
[SOUND] trống hai hướng, lửa, mưa.
백성민: 몰이입니다. 여울로 몰고 있습니다.

### SC_134 · LOC_007_SALSU (cửa bãi cạn, mô cát — phía địch) · cung thủ Tùy · WPN_201 · video8s · 18:35–18:43
[ACTION-VI] Insert: trên mô cát cửa bãi cạn, trong tối, hàng trăm cung thủ Tùy quỳ thành ba hàng, cung giương, một sĩ quan Tiên Ti đi sau lưng họ với đuốc che tay; họ nhìn về bãi lau đang bị lùa. Máy thấp ngang cung.
[SOUND] dây cung căng, mưa, trống xa.
N: 여울 어귀. 오백 개의 활이 갈대밭 쪽을 향했습니다. 몰이가 끝나는 자리였습니다. 탁발흠은 갈대를 태우는 대신 갈대에서 나오는 것을 쏘기로 했습니다.

### SC_135 · LOC_007_SALSU (đảo lau 1) · CHAR_001 · EQP_002 · video8s · 18:43–18:51
[ACTION-VI] 한승우 bấm tổ hợp radio, giọng thấp — ra lệnh giữ im; sau lưng ông lính đã vào hố chiến đấu trong lau, súng rút vải. Cận.
[SOUND] PTT, trống gần hơn, mưa.
N: 그는 아직 침묵을 지키려 했습니다. 을지문덕의 명령이었습니다. 삼십만이 돌아올 때까지 여기 없는 것처럼 있으라는 것이었습니다.
한승우: 전 소대, 여기는 천둥 지휘. 위치 고수. 아직 쏘지 않는다.

### SC_136 · LOC_007_SALSU (đảo lau 1, hố chiến đấu) · lính Hàn, CHAR_002 · WPN_003 · video8s · 18:51–18:59
[ACTION-VI] Đuốc còn 300 m; từ dải lửa, tên bắn mù vào lau rơi lác đác quanh hố; một lính trúng tên vào vai, gập người không kêu; 오태민 ôm khẩu K3 (khẩu của người chết ở 석문령) nhìn về phía 한승우, không bắn — chờ. Máy trung.
[SOUND] tên rơi lau, rên nén, trống, lửa.
N: 침묵에는 값이 있었습니다. 어깨에 화살 하나. 그 값은 아직 낼 만했습니다. 다음 값은 아니었습니다.

### SC_137 · LOC_007_SALSU (đảo lau 1) · CHAR_001 · EQP_002 · video8s · 18:59–19:07
[ACTION-VI] 한승우 nhìn dải đuốc, nhìn khoảng trống phía bãi cạn, nhìn người trúng tên; bấm radio — quyết định phá im lặng. Cận mặt.
[SOUND] PTT, trống dồn.
N: 침묵을 깨는 것도 결정이었습니다. 그는 몰이꾼을 먼저 치기로 했습니다. 여울로 나가는 것은 죽음이었기 때문입니다.
한승우: 박격포, 횃불 선. 스무 발.

### SC_138 · LOC_007_SALSU (đảo lau 1, hố cối) · 사수, tổ cối · WPN_002 · video8s · 19:07–19:15
[ACTION-VI] Hố cối trong bùn: hai khẩu 81mm, xạ thủ thả đạn không nhìn, đạn nối đạn; chớp cam trong lau; tổ đếm to. Cận tay và nòng.
[SOUND] "퉁, 퉁, 퉁" dồn dập, mưa.
사수: 여덟… 아홉… 열!

### SC_139 · LOC_007_SALSU (dải đuốc phía đông) · lính Tùy, 선비 기병 · PROP_016, PROP_017 · video8s · 19:15–19:23
[ACTION-VI] Đạn cối nổ dọc dải đuốc — nước và bùn bùng lên, đuốc văng xuống nước tắt, trống trên xe bò đổ nghiêng; từ đảo, K3 quét tracer thành dải sáng đỏ ngang lau; 오태민 bắn K3, mặt sáng lửa. Wide.
[SOUND] cối nổ liên tiếp, K3 dài, trống ngừng một bên, ngựa hí.

### SC_140 · LOC_007_SALSU (nhánh nước phía nam đảo) · 선비 기병, xạ thủ PZF · PROP_016, WPN_005 · video8s · 19:23–19:31
[ACTION-VI] Từ nam, ba bè lau chở đuốc và cung thủ Tiên Ti đẩy qua nhánh nước về phía đảo; xạ thủ PZF quỳ trong lau bắn — quả thứ nhất, thứ hai, thứ ba: bè nổ tung, lửa trên mặt nước. Máy từ sau vai xạ thủ.
[SOUND] PZF phụt, nổ trên nước, lửa, thét.
N: PZF 셋. 뗏목 셋. 남쪽 고리가 끊어졌습니다.

### SC_141 · LOC_007_SALSU (đảo lau 1, hố chiến đấu) · lính Hàn, CHAR_001 · WPN_001 · video8s · 19:31–19:39
[ACTION-VI] Nhưng phía đông-bắc dải đuốc vẫn khép lại, tên bay dày; một lính Hàn trong hố ngã ngửa — mũi tên cắm cổ, tay bạn kéo anh xuống (không cận); 한승우 nhìn về cửa bãi cạn: khối đuốc lớn nhất đang tụ ở đó — hàm của bẫy. Máy trung.
[SOUND] tên dày, ngã, thở gấp, trống đông.
N: 동쪽 고리는 끊기지 않았습니다. 한 사람이 목에 화살을 맞았습니다. 그리고 여울 어귀의 횃불 무리는 움직이지 않았습니다. 기다리는 쪽이었습니다.

[NARRATOR IM LẶNG — 19:39 → 20:11]

### SC_142 · LOC_007_SALSU (đảo lau 1) · CHAR_001 · EQP_002, VEH_001 · video8s · 19:39–19:47
[ACTION-VI] 한승우 quỳ sau mô bùn K2, tay trên radio, mắt vào khối đuốc cửa bãi cạn; nói ngắn — lệnh cho xe.
[SOUND] PTT, trống, tên rít.
한승우: 천둥 1, 여기는 천둥 지휘. 여울 어귀 횃불 무리. 두 발.

### SC_143 · LOC_007_SALSU (K2 dưới bùn) · 포수 · VEH_001 · video8s · 19:47–19:55
[ACTION-VI] Tháp pháo K2 xoay dưới lớp bùn và lau — bùn nứt, lau rơi khỏi nòng; trong xe, kính ngắm nhiệt: một khối trắng nóng đông đặc trên mô cát cửa bãi cạn; tay pháo thủ trên cần. Không thoại.
[SOUND] mô-tơ tháp pháo rít, bùn rơi, máy nạp đạn tự động "쿵".

### SC_144 · LOC_007_SALSU (đảo lau 1 → cửa bãi cạn) · — · VEH_001, WPN_201 · video8s · 19:55–20:03
[ACTION-VI] K2 khai hỏa — chớp lửa xé đêm mưa trắng một khoảnh khắc, lau quanh xe rạp; viên đạn nổ giữa mô cát cửa bãi cạn: cột nước-cát-đuốc bốc lên, cung thủ văng xuống nước. Wide từ đảo nhìn ra. Không thoại.
[SOUND] tiếng pháo 120mm — sấm dội khắp thung lũng sông, dội lại từ đồi nam.

### SC_145 · LOC_007_SALSU (cửa bãi cạn) · cung thủ Tùy · WPN_201, PROP_016 · video8s · 20:03–20:11
[ACTION-VI] Viên thứ hai nổ lệch trái: khối cung thủ vỡ, người chạy tán loạn xuống nước, đuốc rơi tắt hàng loạt; trống trên mọi hướng ngừng cùng lúc. Aerial trung.
[SOUND] pháo thứ hai, nổ, nước, thét, trống ngừng — rồi chỉ còn mưa.

### SC_146 · LOC_007_SALSU (bờ nam, mép trại hậu quân) · CHAR_205, lính Tùy · EQP_001 · video8s · 20:11–20:19
[ACTION-VI] Bờ nam: lính Tùy trong trại đứng chết lặng, bò bứt dây chạy; 탁발흠 trong lau bờ bắc giật kính đêm khỏi mắt — ống kính lóa trắng vì chớp pháo — hắn dụi mắt, nhìn về cửa bãi cạn bằng mắt thường: chỉ còn lửa nhỏ trên nước. Cận.
[SOUND] mưa, bò chạy, lửa nhỏ.
N: 삼십만의 뒤가 그 소리를 들었습니다. 요동성에서 열 번, 석문령에서 네 번 울린 소리였습니다. 살수에서 두 번. 탁발흠은 그것을 셌습니다. 그의 밤눈은 그 빛에 잠시 멀었습니다.

### SC_147 · LOC_007_SALSU (lối lau ngập, thượng lưu, đêm) · lính Hàn, CHAR_004 · VEH_001, PROP_020 · video8s · 20:19–20:27
[ACTION-VI] Đại đội rút theo lối lau ngập về thượng lưu: hai lính khiêng một xác bọc poncho; 서아 đi cạnh cáng lau chở người trúng tên vào bụng, tay giữ mũi tên không cho lắc; phía sau, K2 bò rất chậm không đèn, lau trên nóc lắc lư. Tracking từ trước.
[SOUND] lội, cáng lau, động cơ K2 ở vòng tua thấp, mưa.
N: 그들은 침묵을 잃었습니다. 대신 밤을 얻었습니다. 삼 킬로 상류에 두 번째 갈대 섬이 있었습니다. 한 사람은 판초에 싸여 갔고, 한 사람은 배에 화살을 꽂은 채 갔습니다.

### SC_148 · LOC_008_GOGURYEO_VILLAGE (đường lầy về nam, đêm) · 전령 · VEH_206 · video8s · 20:27–20:35
[ACTION-VI] Một 전령 Tùy phi ngựa trên đường lầy về nam trong mưa đêm, đuốc trong tay tắt, ngựa sủi bọt; qua một cột quân đang ngủ ven đường. Tracking.
[SOUND] vó ngựa, mưa, ngựa thở.
N: 전령이 남으로 달렸습니다. 이백 리. 그가 가진 것은 한 문장이었습니다.

### SC_149 · LOC_008_GOGURYEO_VILLAGE (lều 우중문, trại 30리, đêm D5) · 전령, CHAR_202 · — · video8s · 20:35–20:43
[ACTION-VI] 전령 quỳ, bùn tới ngực, thở không ra hơi, trước ghế 우중문; 우문술 ở mép khung. Cận 전령.
[SOUND] thở dốc, mưa trên lều.
전령: 뒤에서 천둥이 울렸습니다. 뇌군이 우리 뒤에 있습니다.

### SC_150 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202, CHAR_203 · PROP_001 · video8s · 20:43–20:51
[ACTION-VI] 우중문 tái mặt; đứng dậy tới bản đồ da, ngón tay run đặt lên 살수 — sau lưng ông; 우문술 nhìn ngón tay ấy, không nói. Máy cận bản đồ và hai bàn tay.
[SOUND] mưa, thở.
N: 우중문의 손가락이 살수에 놓였습니다. 그의 뒤였습니다. 앞에는 평양이 있었고, 뒤에는 천둥이 있었습니다. 밥은 어디에도 없었습니다.

### SC_151 · LOC_008_GOGURYEO_VILLAGE (đồi bắc 평양, trại Goguryeo, rạng sáng D5) · CHAR_101, CHAR_105 · PROP_018 · still_kenburns · 20:51–21:00
[ACTION-VI] Ảnh: rạng sáng mưa trên một đồi xanh; 을지문덕 đứng dưới mái lều bạt, giáp ướt; trước ông, 해모루 quỳ một gối, bùn tới ngực, vừa xuống ngựa, đang báo; phía sau, kỵ binh Goguryeo yên ngựa sẵn. Ken-burns đẩy vào mặt 을지문덕 — một nét cười rất nhỏ. Giọng ông ngoài hình.
[SOUND] mưa, ngựa, gió.
N: 을지문덕에게 그 소리는 하루 늦게 닿았습니다. 말 탄 사람의 입으로. 그는 화내지 않았습니다. 뒤에서 천둥이 울렸다. 뇌군이 우리 뒤에 있다. 그 문장은 우중문에게는 공포였고, 그에게는 채찍이었습니다.
을지문덕: 좋소. 서두르게 하시오.

[MID-ROLL 3 · 21:00]

[Kết thúc Phần 7]

## [Phần 8] 여섯 발, 이게 답니다 — 「여섯 발, 이게 답니다」 / Tài nguyên bắt đầu cạn  (21:00–24:00)
> Tóm tắt VI: Sau mid-roll: bình minh D5, đảo lau 2, mưa, xác bọc poncho, không thoại. Màn hình trưởng xe "잔탄 06". 박기철: "여섯 발. 이게 답니다." PZF 여섯 · 박격포 서른 · 탄창 넷 · 무전기 사십 · 연료 "산길 기준 이십 그대로" (3 km đường bằng). 서아 với người bị tên vào bụng: morphine, không kháng sinh; 을보 sắc thuốc lạnh — "뱃속 화살은 못 내리네"; sổ 서아: 항생제 0 · 모르핀 9. ENEMY: 탁발흠 đi trên đảo lau 1 bỏ trống, nhặt vỏ đạn 120 mm, đếm "열 번, 네 번, 그리고 두 번. 열여섯" — "천둥도 센다. 언젠가는 마른다." Mini: 백성민 hạ một trinh sát Tiên Ti bám vết xích K2 bằng dao. Kế: 아리 vẽ đường lau của các bà tới chỗ lấy nước; 백성민 "안개 걷히기 전에 갑니다. 셋만. 총은 놓고."; 오태민 nghe. 한승우 quyết: "쏠 순 없어도 보낼 순 있다." 오태민 xin đi — "넌 북쪽 여울을 지켜." — nhận, lần đầu không cãi. 을보 đưa áo nông dân.
> Chức năng: DECISION · Tài nguyên nói thành lời: "여섯 발" · "PZF 여섯" · "박격포 서른" · "탄창 넷" · "무전기 사십" · "모르핀 아홉" · Open loop cuối phần: "여섯 발은 쓰지 않기로 했습니다. 대신 칼 한 자루와 소녀 하나를 보내기로 했습니다."

### SC_152 · LOC_007_SALSU (đảo lau 2, bình minh D5) · — · PROP_020 · still_kenburns · 21:00–21:10
[ACTION-VI] Ảnh: bình minh xám trên đảo lau thứ hai — gò cát thấp giữa lau cao, mưa; ở tiền cảnh, một xác bọc poncho olive buộc dây đặt trên lau gãy, giày chiến đấu lộ ra; phía sau, K2 là mô bùn mới, lau chưa kịp cắm. Ken-burns kéo ra chậm. Không thoại, không narrator.
[SOUND] mưa, chim nước, im.

### SC_153 · LOC_007_SALSU (đảo lau 2, khoang trưởng xe K2) · CHAR_003 · VEH_001 · video8s · 21:10–21:18
[ACTION-VI] Insert: trong tháp K2, màn hình trưởng xe sáng xanh lạnh: bộ đếm đạn "잔탄 06"; bên cạnh, "위성 0개" vẫn hiện; bàn tay 박기철 đặt lên viền màn hình. Cận.
[SOUND] quạt điện tử, mưa trên nóc.
N: 다섯째 날 새벽. 전차는 여섯이라고 말했습니다. 기계는 거짓말을 하지 않았습니다. 사람이 그것을 소리 내어 읽어야 했습니다.

### SC_154 · LOC_007_SALSU (đảo lau 2, cạnh K2) · CHAR_003, CHAR_001 · VEH_001 · video8s · 21:18–21:26
[ACTION-VI] 박기철 chui ra khỏi cửa tháp, ngồi trên nóc bùn, nhìn xuống 한승우 đứng dưới; hai mặt đều bùn; nói chậm, ngắt nhịp.
[SOUND] mưa, bùn.
박기철: 여섯 발. 이게 답니다.

### SC_155 · LOC_007_SALSU (đảo lau 2, đống khí tài) · CHAR_003 · WPN_005, WPN_002, WPN_001 · video8s · 21:26–21:34
[ACTION-VI] 박기철 trèo xuống, đi dọc đống khí tài phủ poncho (walk-and-talk): tay chạm sáu ống PZF, ba hòm cối, hàng băng đạn xếp theo người; đọc như đếm hàng trong kho.
[SOUND] ống PZF gõ nhau, mưa.
박기철: PZF 여섯. 박격포 서른. 소총은 탄창 넷씩.

### SC_156 · LOC_007_SALSU (đảo lau 2, cạnh K2) · CHAR_003, CHAR_001 · EQP_002, VEH_001 · video8s · 21:34–21:42
[ACTION-VI] 박기철 quay lại, gõ ngón tay lên máy radio rồi lên váy xích K2; 한승우 nghe, gật một cái.
[SOUND] ngón gõ nhựa, gõ thép qua bùn.
N: 간밤에 삼 킬로를 움직였습니다. 평지였습니다. 산길로 센 이십은 아직 이십이었습니다. 박기철은 그렇게 셈했습니다. 적은 쪽으로 세는 사람의 셈이었습니다.
박기철: 무전기 사십 퍼센트. 연료는 산길 기준 이십, 그대로입니다.

### SC_157 · LOC_007_SALSU (đảo lau 2, mái lau cứu thương) · CHAR_004, 부상병 · PROP_009 · video8s · 21:42–21:50
[ACTION-VI] Dưới mái lau: người lính trúng tên vào bụng nằm ngửa, cán tên đã cắt ngắn, băng ép quanh, mặt trắng mồ hôi; 서아 ấn ống morphine tự tiêm vào đùi anh, giữ tay anh; mắt cô nhìn băng đang thấm. Cận.
[SOUND] mưa, thở gấp, ống tiêm bấm.
N: 배에 박힌 화살은 뽑지 않았습니다. 뽑으면 피가 났고, 두면 열이 났습니다. 항생제는 두 달 전에 끝났습니다. 서아에게 남은 것은 모르핀과 시간이었습니다.

### SC_158 · LOC_007_SALSU (đảo lau 2, mái lau cứu thương) · CHAR_106, CHAR_004 · — · video8s · 21:50–21:58
[ACTION-VI] 을보 tới, đặt bát gỗ thuốc lạnh bên cạnh, nhìn người bệnh một nhịp, rồi nhìn 서아 — nói thật, không dịu.
[SOUND] bát gỗ đặt, mưa.
을보: 이건 열을 내리지. 뱃속 화살은… 못 내리네.

### SC_159 · LOC_007_SALSU (đảo lau 2, mái lau cứu thương) · CHAR_004 · PROP_009 · still_kenburns · 21:58–22:08
[ACTION-VI] Ảnh cận: sổ tay y tế của 서아 ướt mép, chữ bút chì: 항생제 0 · 모르핀 9 · 붕대…; bàn tay cô cầm bút dừng trên số 9; phía sau nhòe, bát thuốc lạnh. Ken-burns đẩy vào số 0.
[SOUND] mưa, thở của người bệnh.
N: 서아는 알았습니다. 항생제 없는 배의 상처가 어디로 가는지. 이틀, 길면 사흘. 그녀는 그것을 수첩에 적지 않았습니다. 대신 모르핀을 아홉이라 적었습니다.

### SC_160 · LOC_007_SALSU (đảo lau 1 bỏ trống, sáng D5 — phía địch) · CHAR_205, 선비 기병 · VEH_001 (vết) · video8s · 22:08–22:16
[ACTION-VI] 탁발흠 đi bộ trên đảo lau 1 bỏ trống: hố cối, lau rạp, một vết xích K2 in sâu trong bùn; hắn cúi nhặt một vỏ đạn 120 mm đen bồ hóng, nặng, xoay trong tay; đếm bằng ngón. Cận vỏ đạn và mặt.
[SOUND] mưa, thép chạm bùn, lính Tiên Ti lục lọi xa.
N: 아침이 되자 탁발흠은 빈 섬을 걸었습니다. 그는 늘 싸움 뒤에 그 자리를 걸었습니다. 요동성에서도, 석문령에서도.
탁발흠: 열 번, 네 번, 그리고 두 번. 열여섯이다.

### SC_161 · LOC_007_SALSU (đảo lau 1 bỏ trống) · CHAR_205 · — · video8s · 22:16–22:24
[ACTION-VI] 탁발흠 thả vỏ đạn xuống bùn, ngẩng nhìn thượng lưu theo vết xích; nói với chính mình (반말) — bài học thứ hai của tập.
[SOUND] vỏ đạn rơi bùn, mưa.
N: 그는 천둥이 몇 번 남았는지 몰랐습니다. 다만 하나를 알았습니다. 세어지는 것은 끝이 있는 법이었습니다.
탁발흠: 천둥도 센다. 언젠가는 마른다.

### SC_162 · LOC_007_SALSU (mép đảo lau 2, thượng lưu) · CHAR_006 · WPN_001 · video8s · 22:24–22:32
[ACTION-VI] 백성민 trở về từ mép lau phía hạ lưu, lau lưỡi dao vào ống quần, không nói; sau lưng anh, trong lau, một mũ lông cáo Tiên Ti nổi úp trên nước. Máy theo anh.
[SOUND] lau, nước, mưa.
N: 척후 하나가 전차 자국을 따라 상류로 올라왔습니다. 백성민이 갈대에서 기다렸습니다. 세 번째 적이 갈대 밑에 묻혔습니다. 총소리 없이.

### SC_163 · LOC_007_SALSU (đảo lau 2, bàn cát) · CHAR_107, CHAR_001, CHAR_006 · PROP_020 · video8s · 22:32–22:40
[ACTION-VI] Bàn cát: 아리 quỳ, dùng cọng lau vạch lên bùn ướt: đảo — nhánh nước — mô cát — đường lau — một vòng tròn (chỗ lấy nước của trại); 한승우 và 백성민 nhìn; 을보 đứng sau lưng cháu. Máy từ trên xuống bàn cát.
[SOUND] cọng lau vạch bùn, mưa.
N: 아리는 아낙들의 길을 그렸습니다. 아낙들만 아는 길이었습니다. 그 길의 끝에 적의 물 긷는 자리가 있었습니다. 우리는 그 옆으로 옮겨졌습니다.
아리: 물 긷는 데예요. 새벽엔 졸아요, 지키는 사람들.

### SC_164 · LOC_007_SALSU (đảo lau 2, bàn cát) · CHAR_006, CHAR_001 · — · video8s · 22:40–22:48
[ACTION-VI] 백성민 đặt dao găm lên bàn cát cạnh vòng tròn; rút băng đạn khỏi súng đặt sang bên — không mang súng; nhìn 한승우.
[SOUND] dao đặt bùn, băng đạn tháo.
백성민: 안개 걷히기 전에 갑니다. 셋만. 총은 놓고.

### SC_165 · LOC_007_SALSU (đảo lau 2, hố K3) · CHAR_002 · WPN_003 · video8s · 22:48–22:56
[ACTION-VI] Insert: 오태민 ngồi trong hố lau cách bàn cát 3 m, lau khẩu K3 bằng giẻ, không nhìn lên — nghe hết. Cận tay và mặt nghiêng.
[SOUND] giẻ trên thép, mưa, giọng bàn cát nhỏ.
N: 선택은 둘이었습니다. 셋을 보내고 하나를 데려오는 것. 아니면 아흔둘이 다 숨는 것. 셋이 잡히면 위치도 잡히는 것이었습니다.

### SC_166 · LOC_007_SALSU (đảo lau 2, bàn cát) · CHAR_001 · VEH_001 · video8s · 22:56–23:04
[ACTION-VI] 한승우 nhìn K2 (mô bùn), nhìn mái lau cứu thương, nhìn dòng sông; rồi cúi xuống bàn cát, đặt ngón tay lên vòng tròn.
[SOUND] mưa.
N: 세 번째 결정이었습니다. 첫째는 침묵, 둘째는 두 발. 이번에는 탄약을 아끼고 사람을 보내는 것이었습니다.
한승우: 쏠 순 없어도 보낼 순 있다.

### SC_167 · LOC_007_SALSU (đảo lau 2, hố K3 → bàn cát) · CHAR_002 · WPN_003 · video8s · 23:04–23:12
[ACTION-VI] 오태민 đứng dậy khỏi hố, K3 trên vai, bước tới bàn cát; xin đi — ngắn.
[SOUND] giày trên bùn.
오태민: 제가 가겠습니다.

### SC_168 · LOC_007_SALSU (đảo lau 2, bàn cát) · CHAR_001, CHAR_002 · — · video8s · 23:12–23:20
[ACTION-VI] 한승우 không từ chối ngay — chỉ tay về phía bắc, nơi lau mở ra bãi cạn phía thượng lưu của đảo; giao cho anh thứ quan trọng hơn.
[SOUND] mưa.
N: 그는 오태민에게 가장 중요한 자리를 주었습니다. 셋이 돌아올 길이었습니다. 그리고 그 뒤에 올 것의 길이기도 했습니다.
한승우: 넌 북쪽 여울을 지켜.

### SC_169 · LOC_007_SALSU (đảo lau 2, hướng bãi bắc) · CHAR_002 · WPN_003 · video8s · 23:20–23:28
[ACTION-VI] 오태민 nhìn 한승우 một nhịp, gật một cái — không cãi; quay đi, vác K3 lội về phía mép bắc, lau khép lại sau lưng. Tracking.
[SOUND] lội, lau, mưa.
N: 오태민은 처음으로 묻지 않았습니다. 왜냐고도, 어째서냐고도. 그는 북쪽 여울로 갔습니다.

### SC_170 · LOC_007_SALSU (đảo lau 2, bên 을보) · CHAR_106, CHAR_006 · PROP_020 · video8s · 23:28–23:36
[ACTION-VI] 을보 lôi từ bọc vải ba bộ áo 저고리 vải gai và ba đôi dép rơm, ném cho 백성민; nheo mắt nhìn khuôn mặt góc cạnh của anh.
[SOUND] vải ném, dép rơm, mưa.
을보: 이 옷 입으면 우리 사람 같겠구먼. 얼굴만 빼고.

### SC_171 · LOC_007_SALSU (đảo lau 2) · — · PROP_020 · still_kenburns · 23:36–23:48
[ACTION-VI] Ảnh cận: trên lau gãy, ba bộ áo vải gai xếp, ba đôi dép rơm, một dao găm Hàn Quốc và hai dao Goguryeo, một dải vải tối để bịt đầu, một nắm bùn đen; mưa lấm tấm. Ken-burns trượt ngang.
[SOUND] mưa.
N: 총도, 야시경도, 무전기도 가져가지 않기로 했습니다. 이천 년 전의 옷과 칼과 안개. 그것이 이번 작전의 전부였습니다. 이천 년 뒤의 군대가 가장 오래된 방법을 골랐습니다.

### SC_172 · LOC_007_SALSU (đảo lau 2, mép nước) · CHAR_107 · — · still_kenburns · 23:48–24:00
[ACTION-VI] Ảnh: 아리 ngồi ở mép nước rạng sáng, khăn olive quàng vai, nhìn sang bờ nam qua sương mỏng bắt đầu lên; hai bàn tay xước chắp trên gối. Ken-burns đẩy chậm vào mặt.
[SOUND] mưa nhỏ dần, sông.
N: 여섯 발은 쓰지 않기로 했습니다. 대신 칼 한 자루와 소녀 하나를 보내기로 했습니다.

[Kết thúc Phần 8]

## [Phần 9] 여수장우중문시 — 「여수장우중문시」 / Kế hoạch lớn  (24:00–27:30)
> Tóm tắt VI: (a) [史] D6: 을지문덕 trong lều viết thơ trên lụa ngà, buộc quanh mũi tên, giao 사자: "읽을 줄 안다면 알아들을 것이오." Sứ vào trại Tùy giữa lính gầy. 우중문 mở — đọc thành tiếng; KB chữ Hán + narrator đọc dịch Hàn 4 câu. 우중문 cười một tiếng — rồi lạnh: "이 시가… 나를 비웃는 것이냐?" 사자: "군사를 돌리면 왕을 모시고 행재소에 조회하겠소." Mini-combat: 300 kỵ 해모루 đánh toán lính Tùy đi kiếm ăn ngoài trại rồi rút; 우문술 nhìn bụi, vào lều: "군사는 지쳤고 평양은 험하오. 돌아가오. 방진으로." 우중문 bóp nát lụa rồi nhặt lại. Aerial trại: vẽ 방진 trên bùn. (b) D6 tối, đảo lau 2: 해모루 kể thơ, đọc câu cuối; 한승우: "태오가 외웠던 시다." Insert: 태오 trong cũi môi mấp máy. (c) Kế cứu: 을보 "물이 오르면 안개가 오오. 내일 새벽이오."; 아리: gió + chó; 백성민 thử dao; 해모루: thổi 나각 ở 2리 đông. (d) Lệnh 을지문덕 (VO trên still) "돌아올 것이오. 사흘 안에. 여울 북쪽을 지키시오." — 해모루 nhắc câu cuối: "반이 건널 때까지 아무것도 하지 마시오." 한승우: "어느 쪽 반입니까?" — 해모루 nhún vai.
> Chức năng: PLAN · Tài nguyên: — (K6, PZF không dùng) · Payoff: thơ 3화 P2 · sương ↔ kính đêm (P10) · Open loop cuối phần: "반이 건널 때까지. 을지문덕은 그 반이 어느 쪽 반인지 말하지 않았습니다."
> Sau mid-roll 4 (27:30): SC_198 sương trắng phủ sông lúc rạng đông, không thoại.

### SC_173 · LOC_008_GOGURYEO_VILLAGE (lều 을지문덕, đồi bắc 평양, đêm D5→D6) · CHAR_101 · PROP_014 · still_kenburns · 24:00–24:10
[ACTION-VI] Ảnh: trong lều bạt đêm mưa, 을지문덕 không mũ, tóc bạc búi, giáp cởi để cạnh, ngồi trước bàn thấp, bút lông trên lụa trắng ngà khổ nhỏ; đèn dầu; bốn cột chữ ngắn đang thành hình (brush calligraphy, không cần rõ chữ). Ken-burns đẩy vào tay cầm bút.
[SOUND] mưa trên bạt, bút lông, đèn.
N: 여섯째 날. 일곱 번 지고, 사만을 깨고, 천둥을 두 번 듣고 나서 을지문덕은 붓을 들었습니다. 그는 칼 대신 시를 보내기로 했습니다. 다섯 글자 넉 줄이었습니다.

### SC_174 · LOC_008_GOGURYEO_VILLAGE (lều 을지문덕) · CHAR_101, 사자 · PROP_014, PROP_015 · video8s · 24:10–24:18
[ACTION-VI] 을지문덕 cuộn lụa quanh cán một mũi tên Goguryeo, buộc dây gai hai vòng, đưa cho 사자 (áo bào, không giáp, cờ trắng cuộn); nói ngắn, mỉa nhẹ (하게체 với thuộc hạ).
[SOUND] dây gai siết, lụa, mưa.
N: 화살에 묶어 보냈습니다. 화살로 보내는 글은 답을 요구하는 글이었습니다.
을지문덕: 우중문에게 전하게. 읽을 줄 안다면 알아들을 것이네.

### SC_175 · LOC_008_GOGURYEO_VILLAGE (trại Tùy 30리, cổng trại) · 사자, lính Tùy · PROP_021 · video8s · 24:18–24:26
[ACTION-VI] 사자 Goguryeo cưỡi ngựa dưới cờ trắng đi chậm qua cổng trại Tùy, hai bên là lính Tùy gầy gò dựa giáo nhìn theo — mắt trũng, má hóp; một người ngã khi cố đứng thẳng. Tracking theo sứ.
[SOUND] ngựa, mưa, trại im lặng bất thường.
N: 사자는 무기를 보지 않았습니다. 을지문덕이 그랬던 것처럼, 얼굴을 보았습니다. 얼굴은 열흘 전보다 더 깊었습니다.

### SC_176 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202, CHAR_203 · PROP_014 · video8s · 24:26–24:34
[ACTION-VI] 우중문 ngồi ghế gấp, tháo dây gai khỏi mũi tên, mở lụa; 우문술 đứng sau vai nhìn xuống; đèn dầu; 우중문 đọc thành tiếng hai câu đầu bằng âm Hán — giọng khinh khỉnh.
[SOUND] lụa mở, đèn, mưa.
N: 다섯 글자 넉 줄. 우중문은 소리 내어 읽었습니다. 처음에는 웃으려고 읽었습니다.
우중문: 신책구천문, 묘산궁지리…

### SC_177 · LOC_008_GOGURYEO_VILLAGE (lều 우중문 — cận lụa) · — · PROP_014 · still_kenburns · 24:34–24:44
[ACTION-VI] Ảnh cận lụa ngà dưới đèn dầu: hai cột chữ đầu (brush calligraphy). EDIT: chữ Hán hiện overlay đúng nguyên văn 「神策究天文 / 妙算窮地理」 + phụ đề Hàn (decisions #6). Ken-burns trượt dọc cột thứ nhất sang cột thứ hai.
[SOUND] đèn, mưa.
N: 신책구천문. 신묘한 계책은 천문을 꿰뚫었고. 묘산궁지리. 오묘한 계산은 지리를 다하였네.

### SC_178 · LOC_008_GOGURYEO_VILLAGE (lều 우중문 — cận lụa) · — · PROP_014 · still_kenburns · 24:44–24:54
[ACTION-VI] Ảnh cận lụa: hai cột chữ sau; EDIT overlay 「戰勝功既高 / 知足願云止」 + phụ đề Hàn. Ken-burns trượt sang cột cuối, dừng ở chữ cuối.
[SOUND] đèn, mưa; tiếng thở của 우중문 ngoài hình.
N: 전승공기고. 싸움에 이겨 공이 이미 높으니. 지족원운지. 족함을 알고 그만두기를 바라노라. 여수장우중문시. 이 땅에 남은 가장 오래된 시였습니다.

### SC_179 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202 · PROP_014 · video8s · 24:54–25:02
[ACTION-VI] 우중문 bật cười một tiếng khô — rồi tiếng cười tắt; mặt đỏ dần từ cổ lên thái dương, râu trắng rung; ông nhìn lụa lần nữa, giọng thấp xuống.
[SOUND] cười cụt, đèn, mưa.
N: 일곱 번 이겼다는 말이었습니다. 그러니 이제 그만두라는 말이었습니다. 이긴 자에게 보내는 항복 권고였습니다.
우중문: 이 시가… 나를 비웃는 것이냐?

### SC_180 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · 사자 · — · video8s · 25:02–25:10
[ACTION-VI] 사자 quỳ một gối, không cúi đầu quá thấp, nói câu đã được dặn — trang trọng, không sợ (하오체 ngoại giao).
[SOUND] mưa, đèn.
N: 사자는 두 번째 글을 입으로 전했습니다. 글보다 부드럽고, 글보다 무거운 말이었습니다.
사자: 군사를 돌리면 왕을 모시고 행재소에 조회하겠소.

### SC_181 · LOC_008_GOGURYEO_VILLAGE (đồng ngoài trại Tùy) · CHAR_105, lính Tùy · VEH_101, WPN_101 · video8s · 25:10–25:18
[ACTION-VI] Mini-combat: ngoài trại, một toán lính Tùy đào củ trong ruộng bỏ hoang; 300 kỵ 해모루 từ đồi lao xuống, bắn một loạt, cắt qua toán lính, rồi quay ngựa biến vào mưa; lính Tùy còn lại chạy về trại tay không. Wide.
[SOUND] vó ngựa, dây cung, thét, mưa.
N: 사자가 안에 있는 동안에도 밖에서는 싸웠습니다. 매일 그랬습니다. 밥을 찾으러 나가는 자는 돌아오지 못했습니다.

### SC_182 · LOC_008_GOGURYEO_VILLAGE (mép trại Tùy) · CHAR_203 · — · video8s · 25:18–25:26
[ACTION-VI] 우문술 đứng ở mép trại nhìn bụi kỵ binh tan trong mưa, thẻ tre trong tay, đếm vạch; rồi quay người đi về lều — walk. Tracking.
[SOUND] mưa, trại, thẻ tre.
N: 우문술은 세었습니다. 열흘, 이레, 닷새. 오늘 아침 그의 대쪽에는 사흘이 적혀 있었습니다. 사흘치 밥으로 평양은 무너지지 않았습니다.

### SC_183 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_203, CHAR_202 · — · video8s · 25:26–25:34
[ACTION-VI] 우문술 vào lều, đặt thẻ tre lên bàn trước mặt 우중문, đứng thẳng; quyết định nói thành lời — 하오체 khô, không cao giọng.
[SOUND] thẻ tre đặt bàn, mưa.
N: 사흘 전에는 권했습니다. 이번에는 정했습니다. 우문술은 부총관이었지만, 이 순간 군은 그의 것이었습니다.
우문술: 군사는 지쳤고 평양은 험하오. 돌아가오. 방진으로.

### SC_184 · LOC_008_GOGURYEO_VILLAGE (lều 우중문) · CHAR_202 · PROP_014 · video8s · 25:34–25:42
[ACTION-VI] 우중문 bóp nát cuộn lụa trong nắm tay, ném xuống sàn lều; nhìn nó; rồi cúi nhặt lại, vuốt phẳng, nhét vào áo. Cận tay.
[SOUND] lụa vò, rơi, nhặt, mưa.
N: 우중문은 시를 버렸다가 다시 주웠습니다. 그는 답장을 썼습니다. 꾸짖는 글이었습니다. 그러나 군은 돌아섰습니다. 삼국사기는 그 답장을 적지 않았습니다. 시만 적었습니다.

### SC_185 · LOC_008_GOGURYEO_VILLAGE (aerial trại Tùy, hoàng hôn D6) · lính Tùy · PROP_021 · still_kenburns · 25:42–25:52
[ACTION-VI] Ảnh aerial hoàng hôn mưa: trong trại, sĩ quan Tùy dùng gậy vạch một ô vuông khổng lồ lên bùn, lính xếp thành cạnh vuông tập đội hình, xe bò kéo vào giữa; cờ hạ. Ken-burns kéo ra.
[SOUND] trống lệnh chậm, mưa, bò.
N: 방진. 사방을 막고 가운데에 수레를 넣는 진이었습니다. 쫓기는 군대의 진이었습니다. 내일 새벽, 삼십만은 왔던 길로 돌아갈 것이었습니다. 살수로.

### SC_186 · LOC_007_SALSU (đảo lau 2, tối D6) · CHAR_105, CHAR_001, CHAR_006 · EQP_002 · video8s · 25:52–26:00
[ACTION-VI] Tối: 해모루 ngồi xuống bên 한승우 và 백성민 dưới mái lau, bùn tới đùi, tháo radio đặt xuống, uống nước từ bầu; kể — 하오체.
[SOUND] bầu nước, mưa nhỏ, lau.
N: 그날 저녁, 해모루가 세 번째로 갈대밭에 왔습니다. 이번에는 시를 가지고 왔습니다.
해모루: 장군께서 우중문에게 시를 보내셨소. 넉 줄이오.

### SC_187 · LOC_007_SALSU (đảo lau 2, dưới mái lau) · CHAR_105 · — · video8s · 26:00–26:08
[ACTION-VI] 해모루 đọc câu cuối bằng tiếng Hàn, chậm, như người thuộc lòng; nhìn phản ứng của người đối diện.
[SOUND] mưa.
해모루: 족함을 알고 그만두기를 바라노라.

### SC_188 · LOC_007_SALSU (đảo lau 2, dưới mái lau) · CHAR_001 · — · video8s · 26:08–26:16
[ACTION-VI] Mặt 한승우 — nhận ra: câu thơ này ông đã nghe trên đường nam hạ, từ miệng một cậu lính 21 tuổi; ông nói khẽ, gần như với mình.
[SOUND] mưa, lau.
N: 남하하는 길에서 한 소년이 이 시를 외웠습니다. 시험에 나온 시라고 했습니다. 그때 한승우는 듣기만 했습니다.
한승우: 태오가 외웠던 시다.

### SC_189 · LOC_007_SALSU (trại hậu quân bờ nam, chỗ lấy nước, tối) · CHAR_005 · — · video8s · 26:16–26:24
[ACTION-VI] Insert: cũi tre đặt lại gần chỗ lấy nước trong trại (bên hố nước, gốc cây, hai lính gác, một con chó nằm); 태오 co người, môi mấp máy không thành tiếng — bốn câu năm chữ; mắt nhìn sương bắt đầu lên trên mặt nước. Cận qua nan tre.
[SOUND] mưa, chó thở, môi mấp máy.
N: 그 시를 외운 아이는 강 건너 우리 안에 있었습니다. 시험은 이미 오래전에 끝났습니다. 시는 끝나지 않았습니다.

### SC_190 · LOC_007_SALSU (đảo lau 2, mép nước) · CHAR_106, CHAR_001 · — · video8s · 26:24–26:32
[ACTION-VI] 을보 ngồi xổm ở mép nước, cọng lau chỉ mặt sông — sương mỏng đã bò trên mặt nước ấm hơn không khí; nói không ngẩng lên (하오체 miễn cưỡng).
[SOUND] sông, sương, ếch.
N: 비가 그치고 물이 오르면 강은 김을 냅니다. 을보는 그것을 대장간 물통에서 배웠습니다. 뜨거운 쇠를 담근 물이 그랬습니다.
을보: 물이 오르면 안개가 오오. 내일 새벽이오.

### SC_191 · LOC_007_SALSU (đảo lau 2, bàn cát) · CHAR_107, CHAR_006 · PROP_020 · video8s · 26:32–26:40
[ACTION-VI] 아리 quỳ bên bàn cát, ngón tay vạch lại đường: lau — mô cát — nhánh nước — vòng tròn; rồi liếm ngón tay giơ lên thử gió; nói với 백성민.
[SOUND] bùn, gió nhẹ, mưa tạnh.
N: 개가 있었습니다. 개는 안개를 보지 못하지만 냄새를 맡습니다. 아리는 바람까지 계산했습니다.
아리: 개들이 있어요. 바람이 우리 쪽이면 못 맡아요.

### SC_192 · LOC_007_SALSU (đảo lau 2) · CHAR_006, 2 lính · PROP_020 · video8s · 26:40–26:48
[ACTION-VI] 백성민 thử lưỡi dao găm vào cọng lau — đứt ngọt; đưa hai dao Goguryeo cho hai lính đi cùng (áo vải gai đã mặc), chỉ vào cổ tay mình rồi vào cổ họng — cách dùng. Không thoại.
[SOUND] lau đứt, dao trao tay.
N: 둘은 백성민이 골랐습니다. 사냥꾼 집 아들과 어부 집 아들이었습니다. 물을 아는 사람들이었습니다.

### SC_193 · LOC_007_SALSU (đảo lau 2, dưới mái lau) · CHAR_105 · PROP_018 · video8s · 26:48–26:56
[ACTION-VI] 해모루 nhấc tù và có bảy vạch, chỉ về đông; walk-and-talk ra mép đảo cùng 한승우 (ngoài khung tiếng).
[SOUND] sừng chạm giáp, lau.
N: 나각은 고구려의 무전기였습니다. 삼백 기와 나각 하나. 그것이 해모루가 이 작전에 내놓은 것이었습니다.
해모루: 나는 동쪽 이 리에서 나각을 불겠소. 그러면 놈들이 돌아보오.

### SC_194 · LOC_008_GOGURYEO_VILLAGE (đồi mưa, 을지문덕 — ảnh hồi tưởng lời dặn) · CHAR_101 · — · still_kenburns · 26:56–27:04
[ACTION-VI] Ảnh: 을지문덕 trên đồi mưa nhìn về bắc, 해모루 đứng bên cầm cương; mưa xiên. Giọng 을지문덕 ngoài hình (lời ông dặn 해모루 trước khi đi). Ken-burns đẩy chậm vào mặt.
[SOUND] mưa, gió.
을지문덕: 돌아올 것이오. 사흘 안에. 여울 북쪽을 지키시오.

### SC_195 · LOC_007_SALSU (đảo lau 2, mép đảo) · CHAR_105, CHAR_001 · — · video8s · 27:04–27:12
[ACTION-VI] 해모루 hạ giọng, nhắc nguyên văn câu cuối của 장군, mắt nhìn thẳng 한승우 — chữ nào cũng chậm.
[SOUND] sông, sương.
N: 을지문덕이 처음으로 계획을 말했습니다. 한 문장이었습니다. 그 한 문장이 살수의 전부였습니다.
해모루: 반이 건널 때까지 아무것도 하지 마시오.

### SC_196 · LOC_007_SALSU (đảo lau 2, mép đảo) · CHAR_001, CHAR_105 · — · video8s · 27:12–27:20
[ACTION-VI] 한승우 hỏi; 해모루 nhún vai — một cái nhún nhẹ, rồi nhìn ra sông. Máy hai người.
[SOUND] sương, sông.
N: 해모루는 어깨만 으쓱했습니다. 장군은 그 말을 하지 않았습니다. 그는 늘 지금만 말했습니다.
한승우: 어느 쪽 반입니까?

### SC_197 · LOC_007_SALSU (mép nước, cọc — tối D6) · — · — · still_kenburns · 27:20–27:30
[ACTION-VI] Ảnh: cọc gỗ khắc vạch cắm ở mép nước trong ánh sáng cuối ngày, nước đã lên tới vạch thứ tư; sương bắt đầu phủ mặt sông; mưa tạnh. Ken-burns đẩy vào vạch thứ tư.
[SOUND] sông, sương, im.
N: 반이 건널 때까지. 을지문덕은 그 반이 어느 쪽 반인지 말하지 않았습니다.

[MID-ROLL 4 · 27:30]

[Kết thúc Phần 9]

## [Phần 10] 안개 속의 칼 — 「안개 속의 칼」 / Trận đánh quyết định  (27:30–34:30) — 6 phase
> Tóm tắt VI: Phase 1 Sương (27:30–28:44): sau mid-roll, sương trắng phủ sông; các bà với rổ, 아리 dẫn; 백성민 + 2 áo nông dân, dao dưới áo; 오태민 ở bãi bắc với K3 + K6; 한승우 trong cửa tháp K2: "사격 금지"; 해모루 2리 đông; lính gác Tùy vẫy các bà qua. Phase 2 Chỗ lấy nước (28:44–29:40): hai lính Tiên Ti gác ngủ gật, chó ngủ; dao; cũi mở; 태오 không đi được — 백성민 cõng; mảng vải xé chỗ 태극기. Phase 3 Sai sót (29:40–31:24): chó tỉnh — sủa; tù và Tùy; 탁발흠 bật dậy giơ kính đêm — trắng lóa trong sương và ánh ngày; giật xuống treo cổ: "안개엔 눈이 없다. 귀로 잡는다."; 오태민 radio "대기합니다"; 한승우 "대기."; 해모루 giơ tù và. Phase 4 NARRATOR IM (31:24–33:00): tù và Goguryeo, 300 kỵ đánh sườn đông trại; 아리 kéo cả nhóm vào đường lau; một Tiên Ti bám kịp trong nước — 백성민 hạ dưới nước; 아리 hét — bịt miệng; 탁발흠 chọn hướng sông; kỵ Tiên Ti xuống nước đuổi; 아리 ra mô cát bắc. Phase 5 Goguryeo gánh (33:00–33:56): 20 kỵ của 해모루 lội ra kéo lên ngựa; 오태민 K6 một loạt xuống nước trước mũi ngựa đuổi; 탁발흠 dừng; K2 không bắn; 탁발흠 đá cũi trống, nhặt chốt gỗ bị cắt — học. Phase 6 Kết (33:56–34:30): 태오 đặt xuống đảo; 서아 xem chân; 한승우 quỳ: "죄송합니다… 드론을…" — "살아 있잖아." Không reo hò; 아리 run, 을보 ôm cháu.
> Chức năng: BATTLE (cứu người không tiếng súng của đại đội, trừ 1 loạt K6) · Tài nguyên: K6 −40 · K2 0 viên dùng · Enemy adaptation: 탁발흠 bỏ kính xuống cổ, săn bằng tai; nhặt chốt cắt · Open loop cuối phần: "태오는 돌아왔습니다. 드론과 쇠수레는 이미 서쪽으로 보름째 가고 있었습니다."
> [NARRATOR IM LẶNG] 31:24–33:00.

### — Phase 1 · 안개 / Sương (27:30–28:44) —

### SC_198 · LOC_007_SALSU (sông, rạng đông D7) · — · — · still_kenburns · 27:30–27:40
[ACTION-VI] Ảnh: rạng đông, sương trắng đặc phủ kín mặt sông 살수, chỉ ngọn lau nhô lên như đảo, không thấy bờ nam; ánh sáng trắng phẳng. Ken-burns kéo ra rất chậm. Không thoại, không narrator.
[SOUND] sông rất nhỏ, chim nước một tiếng, im.

### SC_199 · LOC_007_SALSU (đường lau, rạng đông) · CHAR_107, 마을 아낙들 · PROP_020 · video8s · 27:40–27:48
[ACTION-VI] Sáu bà làng với rổ và liềm đi vào sương theo lối lau ngập, 아리 đi đầu, bím giấu dưới khăn tối, mặt bôi bùn nhạt, váy vén buộc gối, chân trần; không ai nói. Tracking từ sau, sương nuốt dần.
[SOUND] nước tới đùi, rổ tre, sương ẩm.
N: 이레째 새벽. 을보의 말대로 안개가 왔습니다. 아낙들은 여느 날처럼 나갔습니다. 다만 오늘은 아리가 앞장섰습니다.

### SC_200 · LOC_007_SALSU (đường lau) · CHAR_006, 2 lính · PROP_020 · video8s · 27:48–27:56
[ACTION-VI] Sau các bà 10 m: 백성민 và hai lính trong áo 저고리 vải gai, khăn tối bịt đầu, mặt bôi bùn đen chỉ hở mắt, dép rơm, tay không; dao găm ép trong ống tay áo. Cận đi ngang.
[SOUND] nước, vải gai ướt.
N: 세 사람은 총을 두고 왔습니다. 야시경도, 무전기도. 가진 것은 칼 셋과 안개였습니다. 그리고 열다섯 살의 길이었습니다.

### SC_201 · LOC_007_SALSU (bãi bắc thượng lưu, hố lau) · CHAR_002 · WPN_003, WPN_004 · video8s · 27:56–28:04
[ACTION-VI] 오태민 trong hố lau ở mép bãi bắc, K3 trước mặt, K6 trên giá ba chân bên cạnh phủ poncho, kính bảo hộ trên mũ; nhìn vào sương trắng không thấy gì. Cận.
[SOUND] sương nhỏ giọt từ lau, im.
N: 북쪽 여울. 오태민의 자리였습니다. 셋이 돌아올 문이었습니다. 그는 안개 속에서 아무것도 보지 못했습니다. 듣기만 했습니다.

### SC_202 · LOC_007_SALSU (đảo lau 2, cửa tháp K2) · CHAR_001 · VEH_001, EQP_002 · video8s · 28:04–28:12
[ACTION-VI] 한승우 nửa người trong cửa tháp K2 dưới lau, tai nghe, mũ tháo; bấm radio thì thầm — lệnh cho toàn đội.
[SOUND] PTT, quạt điện tử nhỏ, sương.
한승우: 천둥 1 이하 전원, 여기는 천둥 지휘. 사격 금지.

### SC_203 · LOC_007_SALSU (bãi đông, 2리 — kỵ Goguryeo trong sương) · CHAR_105 · VEH_101, PROP_018 · video8s · 28:12–28:20
[ACTION-VI] 2리 phía đông: 300 kỵ Goguryeo đứng im trong sương trên bãi cỏ, ngựa thở ra khói; 해모루 phía trước, tù và nâng ngang ngực — chưa thổi; radio trên giáp. Máy trung, sương.
[SOUND] ngựa thở, giáp khẽ, sương.
N: 동쪽 이 리. 삼백 기가 안개 속에 서 있었습니다. 해모루의 나각은 아직 입에 닿지 않았습니다. 그것은 마지막에 부는 것이었습니다.

### SC_204 · LOC_007_SALSU (nhánh nước tới bờ nam) · 마을 아낙들, CHAR_006 · PROP_020 · video8s · 28:20–28:28
[ACTION-VI] Các bà lội nhánh nước tới thắt lưng, rổ đội đầu; 백성민 và hai lính lẫn giữa họ, cúi thấp như người già; sương nuốt bờ sau lưng. Máy ngang mặt nước.
[SOUND] nước, rổ, thở.
N: 초병은 아낙들만 보았습니다. 이레째 같은 아낙들이었습니다. 같은 것은 보이지 않는 법이었습니다.

### SC_205 · LOC_007_SALSU (bờ nam, chốt gác Tùy) · 수 초병 · WPN_201 · video8s · 28:28–28:36
[ACTION-VI] Lính gác Tùy ngồi dựa giáo dưới tấm da, mắt nửa nhắm; thấy bóng các bà trong sương, vẫy tay uể oải cho qua, kéo áo che gáy ngủ tiếp. Không thoại.
[SOUND] sương, ngáy, rổ đi qua.

### SC_206 · LOC_007_SALSU (mép trại hậu quân, lối lau) · CHAR_107, CHAR_006 · PROP_020 · video8s · 28:36–28:44
[ACTION-VI] 아리 không quay đầu — hất cằm về phía trước: qua sương, hố nước và gốc cây cách 50 m, bóng cũi; cô đi tiếp với các bà về bãi lau; ba người tách sang trái, tan vào lau. Máy theo ba người.
[SOUND] lau khép, nước.
N: 여기서 길이 갈렸습니다. 아낙들은 갈대로, 셋은 물로. 아리는 뒤돌아보지 않았습니다. 뒤돌아보는 것은 어머니에게 배우지 않았습니다.

### — Phase 2 · 물 긷는 자리 / Chỗ lấy nước (28:44–29:40) —

### SC_207 · LOC_007_SALSU (chỗ lấy nước, trại hậu quân) · 선비 기병 ×2, CHAR_005 · — · video8s · 28:44–28:52
[ACTION-VI] Chỗ lấy nước: hố nước kè đá, hai lính Tiên Ti gác ngồi gục dưới mái da, cung trên gối; con chó nâu ngủ cuộn cạnh tro bếp; cũi tre dưới gốc cây; 태오 trong cũi tỉnh, mắt mở nhìn sương. Wide thấp.
[SOUND] ngáy, chó thở, nước rỉ.
N: 새벽에는 졸았습니다. 아리의 말 그대로였습니다. 개도 졸았습니다. 아직은.

### SC_208 · LOC_007_SALSU (chỗ lấy nước, mép hố) · CHAR_006 · — · video8s · 28:52–29:00
[ACTION-VI] 백성민 nổi lên ở mép hố nước, chỉ mắt và mũi trên mặt nước, bò lên kè đá không một tiếng; dao rút khỏi ống tay; một lính gác cựa mình. Cận, sương.
[SOUND] nước rỉ rất nhỏ, kè đá, cựa mình.

### SC_209 · LOC_007_SALSU (chỗ lấy nước) · CHAR_006, 2 lính, 선비 기병 ×2 · — · video8s · 29:00–29:08
[ACTION-VI] Dao: lính gác thứ nhất gục xuống trong tay 백성민 không kịp mở mắt (không cận vết); lính Hàn thứ hai khóa cổ lính gác thứ hai từ sau lưng, kéo xuống sau tấm da; ba giây; sương. Máy trung, không gore.
[SOUND] vải sột soạt, một tiếng thở hắt, im.

### SC_210 · LOC_007_SALSU (chỗ lấy nước, cũi) · CHAR_006, CHAR_005 · — · video8s · 29:08–29:16
[ACTION-VI] Cận khóa cũi: dây da và chốt gỗ; dao 백성민 cắt dây, bẩy chốt; 태오 nhìn khuôn mặt bùn đen chỉ hở mắt — miệng mở định gọi; ngón tay bùn của 백성민 ấn lên môi cậu.
[SOUND] dây da đứt, chốt gỗ, thở.
N: 열아흐레 만이었습니다. 태오는 그 눈을 알아보았습니다. 눈밖에 보이는 것이 없었지만 알아보았습니다.

### SC_211 · LOC_007_SALSU (chỗ lấy nước, cũi) · CHAR_005, CHAR_006 · — · video8s · 29:16–29:24
[ACTION-VI] 태오 bò ra khỏi cũi, cố đứng — bàn chân phải sưng tím đen, khuỵu xuống; 백성민 đỡ kịp; cậu cắn tay mình để không kêu. Cận chân và mặt.
[SOUND] thở nén, cát.
N: 발은 몽둥이로 맞은 뒤 부어 있었습니다. 걸을 수 없었습니다. 계획에 없던 것이었습니다. 계획에 없는 것은 늘 있었습니다.

### SC_212 · LOC_007_SALSU (chỗ lấy nước) · CHAR_006, CHAR_005, 2 lính · — · video8s · 29:24–29:32
[ACTION-VI] 백성민 quỳ, xốc 태오 lên lưng; lính thứ hai buộc hai cổ tay 태오 quanh cổ 백성민 bằng dải vải; mắt 백성민 dừng ở vai phải 태오 — mảng vải xé trống chỗ 태극기; anh không nói. Máy trung.
[SOUND] vải buộc, thở.
N: 어깨의 태극기는 없었습니다. 탁발흠이 뜯어 갔습니다. 백성민은 그 자리를 한 번 보고 걸음을 옮겼습니다.

### SC_213 · LOC_007_SALSU (chỗ lấy nước → mép nước) · CHAR_006 (cõng CHAR_005), 2 lính · — · video8s · 29:32–29:40
[ACTION-VI] Ba người khom lưng xuống mép hố nước, 백성민 cõng 태오 lội xuống; sau lưng họ, bên đống tro, tai con chó dựng lên — cận tai chó, mũi hít.
[SOUND] nước, chó hít, sương.

### — Phase 3 · 실수 / Sai sót (29:40–31:24) —

### SC_214 · LOC_007_SALSU (mép lau, các bà) · CHAR_107, 마을 아낙들 · PROP_020 · video8s · 29:40–29:48
[ACTION-VI] 아리 giữa các bà ở mép lau, liềm trong tay, nhìn về hố nước qua sương — thấy con chó đứng dậy, quay đầu về phía nước; bàn tay cô siết cán liềm trắng bệch. Cận.
[SOUND] sương, liềm, tim đập (subjective).
N: 바람이 바뀌었습니다. 새벽 강바람은 늘 그랬습니다. 아리가 계산하지 못한 하나였습니다.

### SC_215 · LOC_007_SALSU (chỗ lấy nước) · chó, 수 초병 · — · video8s · 29:48–29:56
[ACTION-VI] Con chó sủa — dữ dội, tiếng vang trong sương; lao tới mép hố nước; một lính gác Tùy ở lối vào trại giật mình, nâng tù và bằng ốc lên thổi. Máy trung.
[SOUND] chó sủa dội, tù và Tùy khàn dài.
N: 실수는 개였습니다. 사람은 속일 수 있었습니다. 개는 속일 수 없었습니다.

### SC_216 · LOC_007_SALSU (lều 탁발흠, trại hậu quân) · CHAR_205 · EQP_001 · video8s · 29:56–30:04
[ACTION-VI] 탁발흠 bật dậy khỏi đệm da trong lều, tay chộp kính đêm treo ở cột lều, chân trần lao ra cửa lều trong sương trắng. Tracking nhanh.
[SOUND] chó sủa, tù và, lều bạt.
N: 탁발흠은 눈부터 잡았습니다. 밤이면 그 눈은 낮이었습니다. 지금은 새벽이었고, 안개였습니다.

### SC_217 · LOC_007_SALSU (trại hậu quân — POV kính đêm) · CHAR_205 · EQP_001 · video8s · 30:04–30:12
[ACTION-VI] POV kính đêm: trắng — toàn màn hình lóa trắng nhiễu, ánh ngày và sương làm ống kính mù; hắn quay đầu — trắng; quay lại — trắng. Không thoại.
[SOUND] kính rít cao, chó sủa xa, tù và.

### SC_218 · LOC_007_SALSU (trại hậu quân, trước lều) · CHAR_205 · EQP_001 · video8s · 30:12–30:20
[ACTION-VI] 탁발흠 giật kính khỏi mắt, để nó rơi xuống treo lủng lẳng trên dây quanh cổ; nhắm mắt lại; nghiêng đầu — lắng nghe; rồi mở mắt; nói với chính mình (반말) — bài học thứ ba.
[SOUND] kính đập ngực, thở, tiếng nước xa.
N: 밤눈은 밤에만 눈이었습니다. 안개 앞에서 이천 년 뒤의 물건은 장님이 되었습니다. 그는 그것을 오 초 만에 배웠습니다.
탁발흠: 안개엔 눈이 없다. 귀로 잡는다.

### SC_219 · LOC_007_SALSU (trại hậu quân) · CHAR_205, 선비 기병 · VEH_206 · video8s · 30:20–30:28
[ACTION-VI] Kỵ Tiên Ti chạy ra khỏi lều với cung, chân trần; 탁발흠 giơ tay chỉ về hố nước — nơi có tiếng nước khuấy — không chỉ về phía chó; ngựa tháo dây. Máy trung.
[SOUND] chân chạy, dây cung, ngựa, tiếng nước xa.
N: 그는 개가 짖는 곳을 가리키지 않았습니다. 물소리가 나는 곳을 가리켰습니다. 귀는 안개를 뚫었습니다.

### SC_220 · LOC_007_SALSU (chỗ lấy nước) · 선비 기병 · — · video8s · 30:28–30:36
[ACTION-VI] Kỵ Tiên Ti tới hố nước: hai lính gác nằm sau tấm da, cũi mở, chốt gỗ cắt ngọt trên cát; họ tỏa xuống nước đi bộ, cung giương, vào sương. Wide.
[SOUND] cát, nước, tiếng gọi nhau ngắn.
N: 우리는 비어 있었습니다. 자물쇠는 칼로 잘려 있었습니다. 그들은 물로 들어갔습니다. 안개가 그들도 삼켰습니다.

### SC_221 · LOC_007_SALSU (nhánh nước, sương) · CHAR_006 (cõng CHAR_005), 2 lính · — · video8s · 30:36–30:44
[ACTION-VI] 백성민 cõng 태오 lội tới thắt lưng trong sương, hai lính hai bên đẩy nước cho anh; sau lưng, tiếng hô và tiếng lội của kẻ đuổi; 태오 cắn răng, tay siết cổ 백성민. Máy trước mặt.
[SOUND] lội, thở, sau lưng tiếng đuổi.
N: 물은 무릎이 아니었습니다. 이레 동안 허리까지 올라와 있었습니다. 업힌 사람과 업은 사람에게 그것은 두 배로 무거웠습니다.

### SC_222 · LOC_007_SALSU (nhánh nước) · CHAR_107, CHAR_006 · — · video8s · 30:44–30:52
[ACTION-VI] 아리 tách khỏi các bà, lội ào tới, vượt lên trước 백성민 — dẫn; phía xa, các bà tản vào lau như đã dặn (họ chỉ đi cắt lau). Máy trung.
[SOUND] nước, lau, tiếng đuổi.
N: 아낙들은 흩어졌습니다. 갈대를 베러 왔을 뿐이었습니다. 아리는 앞으로 나갔습니다. 여기서부터는 그녀의 길이었습니다.

### SC_223 · LOC_007_SALSU (bãi bắc, hố lau) · CHAR_002 · WPN_004, EQP_002 · video8s · 30:52–31:00
[ACTION-VI] 오태민 nghe tù và và chó qua sương từ bờ nam, bàn tay đặt lên tay cầm K6, ngón cái trên khóa an toàn; bấm radio, giọng nén.
[SOUND] tù và xa, chó, PTT.
오태민: 천둥 지휘, 여기는 1소대. 남안 소란. 대기합니다.

### SC_224 · LOC_007_SALSU (đảo lau 2, cửa tháp K2) · CHAR_001 · VEH_001, EQP_002 · video8s · 31:00–31:08
[ACTION-VI] 한승우 trong cửa tháp nhắm mắt lắng nghe — tù và, chó, nước; mở mắt; radio một chữ.
[SOUND] PTT, sương.
N: 대기. 이 부대가 지난 이레 동안 가장 많이 한 일이었습니다.
한승우: 대기.

### SC_225 · LOC_007_SALSU (bãi đông 2리) · CHAR_105 · PROP_018, VEH_101 · video8s · 31:08–31:16
[ACTION-VI] 해모루 nghe tù và Tùy từ trại; nâng tù và sừng đen lên môi; 300 kỵ sau lưng siết cương. Cận môi và sừng.
[SOUND] tù và Tùy xa, ngựa, hít hơi.
N: 그때 동쪽에서.

### SC_226 · LOC_007_SALSU (bãi đông → trại) · CHAR_105, kỵ Goguryeo · VEH_101, PROP_018, PROP_012 · video8s · 31:16–31:24
[ACTION-VI] Tù và Goguryeo — một hồi dài trầm; 300 kỵ bật ra khỏi sương thành hàng ngang lao về sườn đông trại hậu quân, cờ 삼족오 ướt bay. Wide thấp.
[SOUND] tù và Goguryeo dài, vó ngựa dồn, hô.
N: 해모루의 나각이 울렸습니다. 그 순간부터 갈대밭에는 말이 없었습니다.

[NARRATOR IM LẶNG — 31:24 → 33:00]

### — Phase 4 · 갈대의 길 / Đường lau (31:24–33:00) —

### SC_227 · LOC_007_SALSU (trại hậu quân, sườn đông) · lính Tùy, 선비 기병 · WPN_201, VEH_101 · video8s · 31:24–31:32
[ACTION-VI] Trại: lính Tùy đổ về phía đông, khiên dựng vội; tên Goguryeo bay vào từ sương; kỵ Tiên Ti đang xuống nước ngoảnh lại — một nửa quay về trại, một nửa vẫn lội. Wide.
[SOUND] tù và Goguryeo, dây cung, hô, nước.

### SC_228 · LOC_007_SALSU (nhánh nước → đường lau) · CHAR_107, CHAR_006 (cõng CHAR_005), 2 lính · PROP_020 · video8s · 31:32–31:40
[ACTION-VI] 아리 rẽ lau ở một chỗ nhìn như bức tường lau kín — mở ra một lối hẹp ngập nước chỉ vừa một người; cô chui vào; 백성민 cúi thấp với 태오 trên lưng theo sau; lau khép lại.
[SOUND] lau cọ, nước, thở.

### SC_229 · LOC_007_SALSU (nhánh nước, sương) · 선비 기병 · WPN_101 · video8s · 31:40–31:48
[ACTION-VI] Một kỵ Tiên Ti đi bộ tới thắt lưng theo vệt nước động, cung giương, mắt theo gợn sóng dẫn vào bức tường lau; hắn dừng trước lối hẹp, nghiêng đầu nghe. Cận.
[SOUND] nước lặng, dây cung căng, thở.

### SC_230 · LOC_007_SALSU (đường lau, trong) · CHAR_006, CHAR_005, lính · — · video8s · 31:48–31:56
[ACTION-VI] Trong lối lau: 백성민 chuyển 태오 sang lưng lính thứ hai bằng một cái xoay vai, ra hiệu đi tiếp; anh quay lại, hít sâu, chìm xuống nước không một gợn.
[SOUND] vải, hít, nước khép.

### SC_231 · LOC_007_SALSU (cửa lối lau) · 선비 기병, CHAR_006 · — · video8s · 31:56–32:04
[ACTION-VI] Kỵ Tiên Ti bước vào lối lau — nước trước mặt hắn bùng lên: 백성민 từ dưới nước, dao; hai người quay tròn dưới mặt nước, chỉ thấy lưng, tay, sóng; rồi mặt nước lặng, một cánh tay Tiên Ti chìm. Máy ngang mặt nước, không cận.
[SOUND] nước quật, thở gằn, im.

### SC_232 · LOC_007_SALSU (đường lau) · CHAR_107, CHAR_006 · — · video8s · 32:04–32:12
[ACTION-VI] 아리 quay lại đúng lúc thấy nước đổi màu nâu đỏ — miệng cô mở, tiếng hét bật ra; 백성민 trồi lên ngay trước mặt, bàn tay bùn đen chụp lên miệng cô; mắt cô mở to trên bàn tay.
[SOUND] tiếng hét cụt, nước, thở.

### SC_233 · LOC_007_SALSU (đường lau) · CHAR_006, CHAR_107 · — · video8s · 32:12–32:20
[ACTION-VI] Cận hai đôi mắt: 백성민 lắc đầu một lần, chậm; 아리 nhìn anh — gật; anh bỏ tay; cô lau miệng bằng mu bàn tay, quay người dẫn tiếp. Không thoại.
[SOUND] sương, thở đều lại, nước.

### SC_234 · LOC_007_SALSU (đường lau) · CHAR_107, CHAR_006, lính (cõng CHAR_005) · PROP_020 · video8s · 32:20–32:28
[ACTION-VI] Bốn người trong lối lau hẹp, nước tới ngực, lau hai bên như tường; phía sau, tiếng lội đuổi loạn xạ nhưng đi lệch hướng; mặt 태오 gục trên vai lính, mắt mở nhìn ngọn lau trôi qua. Tracking từ trước.
[SOUND] lau, nước, tiếng đuổi lệch xa.

### SC_235 · LOC_007_SALSU (trại hậu quân, sườn đông) · CHAR_205, kỵ Goguryeo · VEH_101, EQP_001 · video8s · 32:28–32:36
[ACTION-VI] 탁발흠 đứng giữa trại — bên đông kỵ Goguryeo bắn rồi vòng, lều đổ; bên sông tiếng nước; hắn nhìn đông, nhìn sông; chỉ tay về sông — hắn chọn con mồi nhỏ, không chọn trận lớn; kỵ Tiên Ti dắt ngựa xuống nước theo hắn.
[SOUND] dây cung đông, hô, ngựa xuống nước.

### SC_236 · LOC_007_SALSU (bãi bắc, hố lau) · CHAR_002 · WPN_004 · video8s · 32:36–32:44
[ACTION-VI] 오태민 thấy trong sương ở nhánh nước phía nam mô cát: bóng ngựa và người — kỵ Tiên Ti cưỡi ngựa lội ngang nước, cung trên tay, đang lần theo lối lau từ ngoài; anh kéo poncho khỏi K6. Cận.
[SOUND] ngựa lội xa, poncho, khóa an toàn.

### SC_237 · LOC_007_SALSU (bãi bắc, hố lau) · CHAR_002 · WPN_004 · video8s · 32:44–32:52
[ACTION-VI] Ngón tay 오태민 đặt lên cò K6; anh quay đầu về phía đảo lau 2 cách 200 m — chỉ có sương trắng, không thấy K2, không thấy 한승우; quay lại nhìn xuống sông. Cận mặt.
[SOUND] sương, ngựa lội, thở.

### SC_238 · LOC_007_SALSU (cửa ra lối lau, mô cát bắc) · CHAR_107, CHAR_006, lính (cõng CHAR_005), 선비 기병 · PROP_020, VEH_206 · video8s · 32:52–33:00
[ACTION-VI] 아리 bật ra khỏi tường lau lên mô cát bắc, ngã, bò dậy; 백성민 và lính cõng 태오 theo sau; trước mặt: 100 m nước trống tới bờ bắc; sau lưng, ba kỵ Tiên Ti cưỡi ngựa đã vòng qua đầu lau, đang lội tới, cách 80 m. Wide từ bờ bắc.
[SOUND] cát, nước, vó ngựa trong nước.

### — Phase 5 · 고구려가 업다 / Goguryeo gánh (33:00–33:56) —

### SC_239 · LOC_007_SALSU (nhánh nước bờ bắc, phía đông) · kỵ Goguryeo · VEH_101 · video8s · 33:00–33:08
[ACTION-VI] Từ mép lau phía đông bờ bắc, 20 kỵ Goguryeo lao xuống nước về phía mô cát — không cờ, không tù và, chỉ ngựa và giáo; nước bắn thành tường. Tracking ngang.
[SOUND] vó ngựa trong nước, giáp.
N: 해모루는 삼백을 둘로 나눴습니다. 이백팔십은 동쪽으로, 스물은 여기로. 스물은 소리를 내지 않았습니다.

### SC_240 · LOC_007_SALSU (mô cát bắc) · kỵ Goguryeo, CHAR_005, CHAR_107, CHAR_006 · VEH_101 · video8s · 33:08–33:16
[ACTION-VI] Kỵ Goguryeo tới mô cát: một người kéo 태오 vắt ngang yên; người khác xốc 아리 lên sau lưng; 백성민 nắm bàn đạp một con ngựa, hai lính nắm đuôi; ngựa quay đầu về bờ bắc. Máy trung, nhanh.
[SOUND] ngựa hí, giáp, nước, thở.
N: 이천 년 전의 말이 이천 년 뒤의 병사를 업었습니다. 석문령에서 한 번 그랬습니다. 살수에서 다시 그랬습니다.

### SC_241 · LOC_007_SALSU (nhánh nước, giữa mô cát và bờ bắc) · 선비 기병 ×3, CHAR_002 · VEH_206, WPN_004 · video8s · 33:16–33:24
[ACTION-VI] Ba kỵ Tiên Ti cách 80 m giương cung trong nước; từ hố lau bờ bắc, K6 nổ một loạt dài — mặt nước bùng lên thành một hàng cột nước ngay trước mũi ba con ngựa; ngựa dựng đứng, hất kỵ sĩ xuống nước. Wide.
[SOUND] K6 12.7 gầm một loạt, nước bùng, ngựa hí.
N: 한 번. 마흔 발. 살수에서 나는 마지막 총소리였습니다. 그다음 총소리는 삼십만 앞에서 날 것이었습니다.

### SC_242 · LOC_007_SALSU (mô cát nam, mép sương) · CHAR_205 · EQP_001, VEH_206 · video8s · 33:24–33:32
[ACTION-VI] 탁발흠 ghìm ngựa ở mép mô cát nam, kính đêm treo ngực, nhìn ba kỵ sĩ ướt sũng bò về; nhìn bờ bắc nơi khói súng tan trong sương; giơ tay — không đuổi nữa. Cận.
[SOUND] ngựa, nước, im sau loạt súng.
N: 탁발흠은 쫓지 않았습니다. 마흔 발이 어디서 왔는지 그는 들었습니다. 북쪽 여울. 그는 그 자리를 기억했습니다.

### SC_243 · LOC_007_SALSU (đảo lau 2, cửa tháp K2) · CHAR_001 · VEH_001 · video8s · 33:32–33:40
[ACTION-VI] 한승우 trong cửa tháp K2: bàn tay trên nắp công tắc khai hỏa của trưởng xe — không mở; ông rút tay về, đặt lên mép tháp bùn; nòng pháo vẫn bọc lau. Cận tay và mặt.
[SOUND] quạt điện tử, súng xa đã tắt, sương.
N: 전차는 쏘지 않았습니다. 여섯 발은 여섯 발로 남았습니다. 한승우는 손을 거두었습니다. 그것도 결정이었습니다.

### SC_244 · LOC_007_SALSU (bờ bắc, mép lau) · kỵ Goguryeo, CHAR_005, CHAR_107, CHAR_006, CHAR_002 · VEH_101, WPN_004 · video8s · 33:40–33:48
[ACTION-VI] Ngựa Goguryeo lên bờ bắc, lao vào lau; 오태민 hạ nòng K6 còn bốc khói, đứng dậy trong hố, nhìn 태오 vắt trên yên đi ngang qua — hai mắt gặp nhau một nhịp. Máy trung.
[SOUND] ngựa lên bùn, thép nóng xèo trong mưa nhỏ, thở.
N: 북쪽 여울이 열렸다가 닫혔습니다. 오태민이 지킨 문이었습니다. 문은 제 몫을 했습니다.

### SC_245 · LOC_007_SALSU (chỗ lấy nước, trại hậu quân) · CHAR_205 · — · video8s · 33:48–33:56
[ACTION-VI] 탁발흠 đi bộ tới cũi trống, đá nó một cái — nan tre gãy; cúi nhặt chốt gỗ bị cắt ngọt trên cát, nhìn vết dao: một nhát, thẳng; nhìn ra sương phía bắc. Cận chốt và mặt.
[SOUND] tre gãy, gỗ trên tay, sương.
N: 그는 화내지 않았습니다. 배웠습니다. 칼 한 자루가 안개 속에서 야시경을 이겼습니다. 그는 그 칼자국을 오래 보았습니다.

### — Phase 6 · 살아 있잖아 / Kết (33:56–34:30) —

### SC_246 · LOC_007_SALSU (đảo lau 2, mái lau cứu thương) · CHAR_005, CHAR_004, CHAR_106 · PROP_009 · video8s · 33:56–34:04
[ACTION-VI] 태오 được đặt nằm trên lau; 서아 quỳ, kéo cắt dải vải bẩn quanh bàn chân sưng đen của cậu; 을보 giữ đèn lồng không thắp — chỉ soi bằng ánh sáng ban ngày qua lau; xung quanh, lính đứng im. Máy trung.
[SOUND] kéo cắt vải, thở, im.
N: 태오가 갈대 위에 놓였습니다. 아무도 소리를 내지 않았습니다. 이 부대는 이제 소리 내는 법을 잊고 있었습니다.

### SC_247 · LOC_007_SALSU (đảo lau 2, mái lau cứu thương) · CHAR_001, CHAR_005 · — · video8s · 34:04–34:12
[ACTION-VI] 한승우 quỳ xuống bên đầu 태오; cậu ngẩng mặt, môi nứt, mắt đỏ; nói không hết câu.
[SOUND] thở, lau.
장태오: 죄송합니다… 드론을…

### SC_248 · LOC_007_SALSU (đảo lau 2, mái lau cứu thương) · CHAR_001, CHAR_005 · — · video8s · 34:12–34:20
[ACTION-VI] Bàn tay bùn của 한승우 đặt lên đầu 태오 — tóc cắt nham nhở của tù binh; ông nói một câu, không nhìn ai khác.
[SOUND] im.
N: 열아흐레 전 한승우는 이 소년에게 살아 있으라고 했습니다. 소년은 그 말을 지켰습니다.
한승우: 살아 있잖아.

### SC_249 · LOC_007_SALSU (đảo lau 2) · CHAR_107, CHAR_106 · — · still_kenburns · 34:20–34:30
[ACTION-VI] Ảnh: 아리 ngồi trên lau, hai tay ôm gối, run không dứt, khăn olive ướt; 을보 quỳ sau lưng ôm lấy cháu, cằm đặt lên đầu cô; phía sau nhòe, lính Hàn đứng im, không ai reo. Ken-burns đẩy chậm vào hai ông cháu.
[SOUND] mưa bắt đầu lại, sông.
N: 태오는 돌아왔습니다. 드론과 쇠수레는 이미 서쪽으로 보름째 가고 있었습니다.

[Kết thúc Phần 10]

