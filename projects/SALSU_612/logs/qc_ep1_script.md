# QC — 1화 「요하」 full_script_ep1.md (v1, 291 SC, 40:00) · qc-reviewer · 2026-09-16

> Đối chiếu: series_foundation §4–§10 · outline_ep1 · story_bible §1/§5/§9 · character_bible (giọng từng nhân vật) · resource_ledger v2 · decisions P-20…P-35 · channel style §4/§10/§11/§17/§19b/§20 · templates/01 §IX–XIV/§XVII · templates/06.
> Bỏ qua lỗi "narration thưa" (P-26, đang sửa song song). Tham chiếu bằng SC ID; số thời gian theo header SC.
> Tổng: **BLOCK 1 · FIX 18 · NOTE 27**. Không sửa full_script. Các FIX chạm outline/ledger (★) cần coordinator quyết → ghi proposals.

## 0. Kết luận nhanh
- Script **khớp outline 12/12 phần, 0 s lệch**, 5 quote nguyên văn, K2 không bắn, drone 4→3, 0 KIA, 탁발흠 sống, kết "가져오라" — ràng buộc cứng đạt.
- **Ba lỗi nặng nhất:** (1) SC_006/012 gắn VEH_206 (kỵ Tiên Ti) ở ngày 1 khi cầu phao chưa nối — mâu thuẫn timeline nội tại (BLOCK). (2) Đồng hồ dầu: "이틀에 육십 킬로" (SC_261) trong khi K2 chỉ chạy 1 đêm 30 km và tắt máy đêm trận — số không có nguồn (FIX★). (3) Thời điểm đại quân Tùy: SC_153 "대군보다 이틀 빨랐습니다" nhưng SC_155/200 (đêm 4) và SC_263 (sáng 5) đã cho thấy vòng vây khép kín hàng vạn lều (FIX).
- **Benchmark thua kênh gốc rõ nhất:** tỷ lệ combat ~22–23 % (mục tiêu ≥35 %, kênh gốc 45 %); đại đội bóp cò lần đầu ở 12:14 (kênh gốc 0:52–1:36); chỉ 3 khối action (spec S40 ≥6); 30 s đầu 4 shot (kênh gốc 13, mục tiêu ≥5); shot trong trận toàn 8 s (kênh gốc 4 s).

---
## 1. BẢNG LỖI

| Mức | SC / dòng | Vấn đề | Đề xuất sửa cụ thể |
|---|---|---|---|
| **BLOCK** | SC_006 (header `VEH_206`), SC_012 | **Kỵ Tiên Ti trên bờ đông ngày 1.** SC_006 gắn ID VEH_206 (선비 기병 của 탁발흠) cho vệt bụi 3 km lúc 0:40, nhưng theo chính script cầu phao thất bại ngày 1 (SC_053–059) và "이틀 뒤… 수나라 기병이 올라왔습니다" (SC_078). Ngày 1 chỉ có kỵ Goguryeo (해모루 thu quân; cậu bé척후; 20 vết móng SC_033) ở bờ đông. Nếu veo-stage đính ref Tiên Ti → hình sai timeline. | Đổi ID SC_006 → `VEH_101` (kỵ Goguryeo, cờ 삼족오 không nhìn rõ vì xa) hoặc ghi `기병 미상 (xa, chỉ bụi)`; SC_012 giữ "vệt bụi" không ID. Thêm ở SC_040 [ACTION] 한승우 nhìn về hướng bụi "phía đông-nam" (không phải tây) để drone bay tây vẫn hợp lý. |
| FIX★ | SC_261 (+ SC_145, SC_187, SC_262) | **"연료는… 이틀에 육십 킬로 썼습니다"** không có nguồn: K2 chỉ di chuyển 1 đêm (SC_145 "삼십 킬로"), đêm trận "시동 끕니다" (SC_187), sạc drone dùng máy phát K151 (SC_156) nên K2 không nổ máy. 30 km còn lại biến mất. Quote ★ của outline P11/ledger nhưng script không chứng minh được. | (A) Đổi SC_261: **"연료는… 하룻밤에 삼십 킬로. 전차 몫으로 삼백칠십입니다."** (7 어절) và cập nhật ledger 1화 cuối = ~370 (ghi proposals). (B) Nếu giữ 60: thêm 1 SC ở P5/P6 (sau SC_103) — sau khi lộ diện, 한승우 dời cả căn cứ 30 km về đông trước hoàng hôn ("쏜 자리에서 잔다는 건 없다") → K2 chạy 30 km ngày 3 + 30 km đêm 3. Đề nghị (A). |
| FIX | SC_153 N ↔ SC_150, SC_155, SC_200, SC_263 | **Thời điểm đại quân.** SC_153 (ngày 4): "대군보다 이틀 빨랐습니다" nhưng SC_150 (sáng 4) trại Tùy "mọc như nấm", SC_155/200 (đêm 4) "hàng vạn đốm lửa vòng cung khép dần", SC_263 (sáng 5) "포위는 하룻밤 사이에 닫혔습니다". Đại quân đã ở đó ngày 4. | SC_153 N: **"탁발흠은 이천 기와 함께 동쪽으로 돌았습니다. 본대보다 하루 빨랐습니다. 그는 길을 막는 법을 알았습니다."** Thêm 1 câu N ở SC_155 (narration pass): "하루에 한 군씩, 불빛이 늘어났습니다." — khớp sử 24군 cách nhau 1 ngày, giải thích lửa tăng dần. |
| FIX | SC_174 N | "이 땅에서의 **사흘째** 밤" — đếm theo script: sáng 1 tới (SC_022) → đêm 1 → (ngày 2) → ngày 3 P5 ("이틀 뒤", SC_078) → đêm 3 hành quân vào thành (P6–P7) → sáng 4 (SC_145) → **đêm 4 = P8/P10**. | **"이 땅에서의 나흘째 밤이었습니다."** |
| FIX | SC_245 N | "성을 지키라는 **왕명**이었습니다. 성주는 문을 열었습니다." — chiếu vua chỉ đến ở P12 (SC_275–278). Nói "왕명" ở P10 làm hỏng reveal chiếu "성과 함께 죽으라" và mâu thuẫn "성주는 읽기 전에 내용을 알았습니다" (SC_271). | **"성문을 닫는 것이 성주의 첫째 임무였습니다. 성주는 문을 열었습니다."** (Quyết định trái lệnh thường trực, không phải trái chiếu — chiếu đến sau càng nặng hơn.) |
| FIX★ | SC_115 (+ SC_114, SC_117) | **"영양왕 이십삼 년이오"** — 영양왕 là **시호** (tên thụy) đặt sau khi vua băng; người đương thời 612 không thể gọi vua đang sống là 영양왕. Khán giả 50+ xem 사극 biết lỗi này (lỗi kinh điển). Quote nằm trong outline/foundation §7 → cần coordinator. | Đổi cách lộ năm — 한승우 **tự suy ra** (hay hơn kênh gốc, xem §3 #2): SC_114 한승우 (nhẩm với 박기철): **"수나라, 백만, 요동성… 육백십이년입니다."** · SC_115 해모루 (nhíu mày): **"대왕 즉위 스물세 해째요."** · SC_116 giữ "육백십이년… 살수." · SC_117 N (narrator được phép dùng 시호): "영양왕 23년, 서기 612년. 대한민국 군인이라면 누구나 배운 해입니다." Ghi proposals (đổi quote outline P6). |
| FIX | SC_078 (+ SC_077, SC_079) | **Nén thời gian quá tay:** cầu nối lại "이틀 뒤" (SC_077) = ngày 3; nhưng "bình minh xám ngày thứ ba" (SC_078) kỵ Tùy đã vượt sông, đốt làng, đuổi dân cách bờ 15 km+. Trong 1 rạng sáng không kịp. | SC_078 [ACTION] "Chiều ngày thứ ba, nắng bạc xiên"; N: **"이틀 뒤 오후. 다리가 놓인 지 반나절, 수나라 기병이 동안으로 올라왔습니다."** P6 hoàng hôn cùng ngày càng hợp. Thêm 1 câu [史] ở SC_077 N (narration pass): "고구려군 만 명이 물가에서 무너졌고, 남은 이들은 요동성으로 물러났습니다." — giải thích vì sao 해모루 chỉ còn 300 kỵ "thu quân". |
| FIX | SC_090, SC_222 (đăng ký radio) | 오태민 đang **ở trên 천둥 2** mà gọi "**천둥 2**, 기병 선두 전방 오십. 점사." — theo thủ tục vô tuyến, gọi tên trước là gọi *người khác*; tự gọi xe mình là sai (cựu binh 50+ nhận ra). SC_222 tương tự: trong 천둥 3 nói "천둥 3, 전진". | SC_090: **"포수, 선두 전방 오십. 점사."** (nội bộ xe). SC_222: **"조종수, 전진. 여울 건너 측면 친다."** (6 어절 — thêm ý đồ "đánh sườn" để sai lầm có logic). SC_223 한승우 "천둥 3, 정지! 오 중위, 정지!" đúng, giữ. |
| FIX | SC_186 (해모루) | "성주**께서는** 보병 오백으로 문을 **지키오**." — dùng 께서 (kính) mà đuôi không có -시-; "수레가 올 때만 **여시오**" nghe như ra lệnh cho người nghe mở cổng. | **"성주께서 보병 오백으로 문을 지키실 것이오. 수레가 올 때만 여실 것이오."** (11 어절) |
| FIX | SC_270, SC_275 N, header P12 "기사(사자)" | "**기사**가 왔습니다" — với khán giả hiện đại "기사" = tài xế/bài báo; từ đúng thời là 전령/사자/파발. | SC_270 해모루: **"성주, 평양에서 전령이 왔습니다."** · SC_275 N: "평양의 **전령**이 요동성 대청에 무릎을 꿇었습니다." · đổi nhãn vai → 전령. |
| FIX | SC_252 | **Một SC hai địa điểm** ("Trên tường: lính Goguryeo reo… Cắt: cửa thung — 오태민…") — không quay bằng 1 clip 8 s. | Tách: SC_252a (still 4 s hoặc gộp vào SC_253 ken-burns): lính Goguryeo trên tường giơ giáo; SC_252b video 8 s: 오태민 thở bên 천둥 3. Hoặc bỏ nửa "reo" (SC_253 đã có cổng đóng) và giữ 8 s cho 오태민 — N vẫn nói "고구려는 환호했습니다" (âm thanh reo xa). |
| FIX | SC_265 | 한승우 đi qua **cổng đông**, rút tên khỏi gỗ cổng, rồi **lên tường tây** trong 8 s — hai đầu thành. | SC_265 chỉ giữ hành động rút tên ở cổng đông (đủ cho payoff PROP_015); SC_266 mở bằng 한승우 bước lên bậc tường tây (ghi trong [ACTION] SC_266). |
| FIX | SC_178 ↔ SC_203/212/215/222 (địa hình trận) | "동쪽 길은 **여울을 건너오**" → đường đông đi qua bến suối; nhưng kỵ vào bến "북에서 남" (ngang đường), đoàn xe từ 4 km (SC_194) tới 2 km cách cổng (SC_215) mà không thấy qua bến đang bị pháo; 오태민 "여울 건넌다" để cứu xe bò lại đi *ra xa* đoàn xe. Sa bàn (SC_180) sẽ được veo-stage vẽ theo lời này → rối. | SC_178 해모루: **"여울은 북쪽에서 길로 오는 유일한 길목이오. 돌바닥이고 양쪽은 진창이오."** (9 어절) — bến = lối duy nhất từ bắc xuống đường; red herring P9 (địch vòng gò bắc) tự khớp; SC_222 thêm "측면 친다" (xem trên) → 오태민 vượt bến để đánh sườn cánh kỵ đang chém đuôi đoàn xe từ phía bắc. |
| FIX | SC_189 ↔ P5 (SC_079–103), SC_237, SC_249 | **을보 và "우리 마을 수레":** làng 을보 là làng ven 요하 đã cháy, đoàn dân ấy đã vào thành đêm 3 (SC_142 "hàng dân đợi sau đoàn xe"). Đoàn 3.000 + xe lương là làng **phía đông** → "마지막 수레는 우리 마을 것이야" không khớp. Thêm nữa: 을보 (66 tuổi, chân băng) ở xe cuối (SC_217, 29:30) → bến suối quát bò kéo K21 (SC_237, 32:10) → lại trên xe cuối qua cổng (SC_249, 33:48): di chuyển 2 km × 2 trong 4 phút phim. | SC_189: **"마지막 수레는 내 아우네 것이야. 내가 타고 가겠네."** (8 어절 — em trai ở làng đông, hợp lý). SC_237: bỏ 을보, dùng "dân đánh xe bò Goguryeo" (không ID) quát bò; 을보 chỉ ở xe cuối (SC_217 → SC_249). |
| FIX | SC_219 | 한승우: "박격포는 수레 전방으로." — cối chưa đăng ký mục tiêu trên đường đông, đêm, gần 3.000 dân; và **không có SC nào cối bắn về đó** (tổng cối −8 đúng ledger 110). Lệnh không có payoff. | **"천둥 2, 3 위치 고수. 백 중사, 후미 계속 보고."** (10 어절). Nếu muốn giữ cối: thêm 1 SC cối chuyển làn 2 viên (110→108) — phải sửa ledger, không khuyên. |
| FIX | SC_161–SC_167 (7 SC liên tiếp, 21:48–22:44) | **"Đứng nói" 56 s trong lều**: 7 SC tĩnh quanh bàn gấp, chỉ mặt + thoại. Vượt quy tắc ≤2 SC nói liên tiếp; kênh gốc không bao giờ để 1 phút không hình động. (Các cụm khác: SC_109–123 P6 15 SC đàm phán — có chuyển động nhưng vẫn dài; SC_284–287 4 SC lều 양제 — chấp nhận.) | Cắt đôi: SC_161–163 (lều) → chèn SC_168 (phát kính đêm, không thoại) → SC_164–167. Cho SC_165 thành walk-and-talk: 오태민 bước ra khỏi lều, chỉ thẳng K2 dưới lưới, **vỗ váy xích** (đối xứng cử chỉ 박기철 SC_083/187); SC_166 한승우 nói từ cửa lều. P6: chèn 2 SC không thoại giữa SC_115–SC_118 (kỵ Goguryeo trên gò hạ cung khi 을보 gào; 서아 băng lại chân 을보 giữa khoảng trống). |
| FIX | SC_078, SC_015, SC_182 (logic pin drone) | SC_015 "4 viên pin dán số 1/2/3/4" + SC_182 "2호기… pin số 2 và 3, hai lần bay **hợp 24 phút**" ⇒ pin tháo rời được và có dự trữ; vậy ngày 3 drone #1 "배터리 십이 분" (không sạc 2 ngày vì "giữ dầu" — mà 1 lần sạc chỉ 2 L, SC_156) là giới hạn giả. | SC_078 태오: **"1호기, 배터리 십이 분. 새 건전지는 아낍니다."** (7) · SC_182: **"2호기, 두 번 비행. 열두 분씩만 씁니다."** (6) · Thêm N ở SC_051 (narration pass): "발전기는 돌리지 않았습니다. 소리는 십 리를 갔습니다." → lý do không sạc ngày 1–2 = **tiếng máy phát** khi kỵ binh lạ cách 3 km, không phải 2 lít dầu. |
| FIX | 0:00–0:30 (SC_001–004) | Chỉ **4 shot trong 30 s đầu** (mục tiêu ≥5; kênh gốc 13). SC_001 có 2 s đen + 6 s tên. | Tách SC_001 → (a) 3 s đen + gió, (b) 5 s tên; chèn 1 insert 4 s "giày chiến đấu trên cỏ vàng, 태극기 patch rung gió" trước SC_003 → 6 shot/30 s, không đổi tổng thời gian (rút SC_003 còn 6 s). |
| FIX | Cấu trúc action (P4 32 s · P5 80 s · P8 16 s · P10 402 s) | Combat ≈ **530 s / 2.400 = 22 %** (S40 ≥35 %; ≥6 khối action). Chỉ 3 khối thật + 1 mini. Khoảng 14:00–27:30 (13,5 phút) **không có giao tranh**. | Thêm 2 khối nhỏ **không đổi số SC** (đổi still → video, đổi nội dung SC hiện có): (i) P7 SC_136–137/144: đêm hành quân — trinh sát Tiên Ti bám đuôi đoàn xe, 백성민 thấy qua kính đêm, kỵ 해모루 đuổi (3 SC, không thoại) — hợp "탁발흠 học"; (ii) P8 SC_174–176: trinh sát địch dò thung lũng đêm, một mũi tên cắm vào lưới K2 (PROP_015 "tên gãy cắm lưới K2" đã có trong prop_bible), lính gác kính đêm hạ 1 tên (2 SC). (iii) P4: SC_054/059 still → video có giao chiến (+20 s combat sử). Xem §3 #1. |
| NOTE | SC_018 (오태민) | "가정, **북에서** 삼십만 남하" — kịch bản diễn tập ám chỉ Bắc Triều Tiên (foundation §8: chỉ "이 땅"). Là câu outline; cho 50+ không phản cảm nhưng vi phạm nguyên tắc tự đặt. | **"가정, 적 삼십만 남하… 반나절이면 끝납니다."** — giữ mỉa mai. |
| NOTE | SC_132 (탁발흠) | "쇠수레가 **셋**" — hắn chỉ thấy 2 K21 xuất kích (천둥 2, 3); K2 và 천둥 4 dưới lưới cách 3 km. Outline ghi "3대, 검은 통" nhưng script không có SC hắn nhìn thấy căn cứ/phuy dầu → foreshadow hỏa công 2화 (outline P5) **bị rơi**. | "쇠수레가 **둘**, 사람은 백 남짓입니다." · Trả foreshadow: SC_247 đổi K511 #1 → **K511 #2 (xe chở phuy)** để SC_251 cái nhìn cuối của 탁발흠 bắt được "검은 통" trên thùng xe (thêm 1 câu [ACTION]). |
| NOTE | SC_058 N ↔ SC_131–134, SC_282 "수 선봉장" | "선봉장 맥철장이… 죽었습니다" (7:42) rồi P7/P12 lại có "수 선봉장" còn sống → khán giả có thể tưởng cùng người. (맥철장 sử là 좌둔위대장군, tự xin đi đầu — gọi 선봉장 chấp nhận được.) | Đổi nhãn vai P7/P12 → **"수 전군총관"** hoặc "수 기병총관"; SC_130 N "선봉 진영" → "전군 진영". |
| NOTE | SC_077 N (lịch sử) | Thiếu [史] quan trọng: lần vượt sông thứ hai Goguryeo **mất ~1만**, rút vào 요동성 (story_bible §1). Script chỉ nói "이번엔 길이가 맞았습니다". Không sai, nhưng bỏ lỡ cái giá của tổ tiên (chủ đề 50+) và lý do 해모루 "thu quân". | Thêm 1 câu N (đã ghi ở FIX SC_078). |
| NOTE | SC_022 ↔ SC_011–012, SC_024 | Sáng P2 (SC_022) "sương bám trên **lưới ngụy trang**" nhưng lệnh phủ lưới mới ở SC_011 (P1). Trình tự P1 (hook) ↔ P2-sáng mơ hồ; 백성민 "중대장님. 나와 보셔야겠습니다" (2:56) sau khi 한승우 đã đứng nóc xe nhìn chân trời (0:16). | SC_022 bỏ "lưới ngụy trang" (xe trần, sương trên giáp) → P2-sáng = trước P1; SC_024 백성민: **"중대장님. 도로가… 끊겨 있습니다."** (báo phát hiện cụ thể). |
| NOTE | SC_145 (박기철) | "**오늘 밤에** 전차 삼십 킬로 썼습니다" nói lúc **bình minh** → tiếng Hàn tự nhiên là "간밤에". Quote outline, sửa 1 từ. | **"간밤에 전차 삼십 킬로 썼습니다."** |
| NOTE | Narrator (SC_007–010 hiện tại; SC_011+ quá khứ; SC_027 lẫn "향합니다… 떠났습니다") | Thì narrator không nhất quán (story_bible §9 ghi "thì hiện tại"; script chủ yếu quá khứ). Không lỗi nặng nhưng TTS/nhịp lệch. | Chốt quy ước: **quá khứ** cho chuyện, **hiện tại** chỉ cho câu "định vị" mở phần ("612년 정월. 탁군."). Sửa SC_027: "…요하로 향했습니다." — giao narration pass. |
| NOTE | SC_259 | N "항생제는 스무 개에서 열여덟 개" + 서아 "항생제는 아직 아흔 퍼센트입니다" — narrator nói điều thoại nói ngay sau (templates/06 §8). | Bỏ vế N về kháng sinh, giữ "돌아오지 않는 숫자였습니다" gắn vào "부상 여섯". |
| NOTE | SC_066 (소년) | "수나라… 수나라**요**?" (đuôi 해요) lệch với 하오체 của cậu ở SC_067/071/110 ("백만이오/요동성이오/저 사람이오"). | **"수나라… 수나라 사람이오?"** |
| NOTE | SC_166 (한승우) | "전차는 그물 밑에 **있는다**" — dạng gượng. | **"전차는 그물 밑에 둔다. 두 번 말 안 한다."** |
| NOTE | SC_282 (수 선봉장) | "폐하, **무례하오나** 보셔야 할 것입니다" — công thức triều đình là "황공하오나/외람되오나". | **"폐하, 황공하오나 보셔야 할 것입니다."** |
| NOTE | SC_288 N | "이름 없던 부대에 이름이 붙었습니다. 뇌군." — **không ai nói chữ 뇌군** trên màn hình; narrator đặt tên thay 양제. Đòn bẩy 3 (nhân vật lịch sử quyết) bị narrator lấy mất. | Thêm giọng 양제 (off) trên still SC_288: **"뇌군이라 하라."** (2 어절) rồi N rút còn "그날 밤, 부대에 이름이 붙었습니다." — câu dùng được cho title/thumbnail 2화. |
| NOTE (anti-copy) | SC_266–274 → SC_281–288 → SC_291 | Khung kết giống style §17 tập series kênh gốc: (a) hai chỉ huy trên tường nhìn địch → (b) lều địch, chỉ huy ra lệnh → (c) black card. Ta khác ở chỗ chèn đại sảnh chiếu vua (SC_275–280) và kết bằng K2 (SC_290), thoại khác hẳn → **không BLOCK**, nhưng tableau "2 chỉ huy trên tường" (SC_154, SC_274 lặp 2 lần) là hình hiệu của kênh gốc. | Chuyển 2 câu của 고정수 (SC_266–267) vào **kho lương**: ông đếm bao thóc bằng thẻ tre khi nói ("hậu cần là nhân vật"); tường tây chỉ giữ SC_269 (2 lá cờ) + SC_274 đổi thành 한승우 **một mình** với mũi tên trong tay. Bỏ hẳn tableau đôi. |
| NOTE (anti-copy) | SC_114 | "지금이… 몇 년입니까?" = beat "Năm nào?" ở cùng vị trí cấu trúc (gặp quan địa phương) của S15 kênh gốc. Không copy chữ, nhưng cùng cơ chế. | Dùng phương án suy luận ở FIX SC_115 — 한승우 tự tính ra 612, 해모루 chỉ xác nhận. Vừa tránh trùng, vừa sửa 시호. |
| NOTE (realism) | SC_044–SC_050, LOC_001 "cách sông ~15 km" | Quadcopter pin 30 phút bay >10 km ("십 킬로… 아직 풀") tới sông, giữ link video ở 15 km rồi quay về với 18 phút pin: tốc độ ~75 km/h + link 15 km là biên trên của drone quân sự cỡ nhỏ. Người 50+ ít soi; lính chuyên nghiệp có. | Hạ khoảng cách: LOC_001 ghi "~8–10 km", SC_044 **"팔 킬로… 아직 풀입니다."** (không đổi số pin). |
| NOTE (realism) | SC_086 → SC_094 | "팔백 미터, 정지 사격" rồi SC_094 1소대 đã ở xe bò lật, 2 lính trúng tên (SC_099) — thiếu lệnh tiến sau khi kỵ vỡ. | SC_093 hoặc SC_094 [SOUND] radio 오태민: "수레로 전진!" (2 어절) — hoặc 1 câu N (narration pass). |
| NOTE | SC_233 (사수 천둥 2) | "40밀리 **마지막** 탄띠!" trong khi tổng 40mm cuối tập còn 480 (SC_260). Là băng cuối *trên xe* (đạn dự trữ ở thùng tại căn cứ). | **"40밀리, 즉응탄 마지막입니다!"** — 5 어절, đúng thuật ngữ. |
| NOTE | SC_149–150 (고정수) ↔ rule SC_162 | "저 수레가 못 들어오면 **가을까지 못 버티오**" → hàm ý không có đại đội, 요동성 thất thủ (sử: thành giữ được suốt hè). Mâu thuẫn ngầm với "역사가 이미 이겼다" và story_bible §3 "1화 lệch nhỏ về sử". | Đổi cái giá sang **người**, không phải kho: **"저 수레가 못 들어오면 삼천이 성 밖에서 죽소."** (7 어절). 3.000 dân không có trong sử → đại đội cứu người mà không "sửa" lịch sử. |
| NOTE | P10 (SC_202–251) toàn 8 s | Outline P10 hứa "shot 4–6 s trong trận"; script 52 SC × 8 s → nhịp trận chậm gấp đôi kênh gốc (4 s). | Veo-stage: cắt đôi ~15 clip 8 s thành 2×4 s (hard cut trong cùng clip: cận → wide). Không đổi SC. Ghi vào veo prompt "two-beat cut". |
| NOTE | SC_019 (한승우) | "천둥 지휘. 한탄강 여울 확보 후 대기한다." — thiếu định danh người gọi/người nghe. | **"전 소대, 여기는 천둥 지휘. 한탄강 여울 확보 후 대기한다."** (11 어절) |
| NOTE | SC_185 (해모루) | "신호는 **나팔**이오" — prop là 나각 (tù và sừng, PROP_018). | "신호는 **나각**이오." (hoặc "뿔나팔"). |
| NOTE | SC_035, SC_168 | Hàng lính xếp hàng (SC_035 wide OK; SC_168 trung cảnh phát kính đêm) — cẩn thận "đám đông cận cảnh" (foundation §9). | SC_168: quay từ sau lưng hàng người, chỉ mặt 태오 rõ. |
| NOTE | SC_002/SC_061 ↔ vehicle_bible VEH_003 | Lốp K511 #2 thủng tên, vehicle_bible ghi "thay lốp dự phòng — cảnh đầu"; script không có beat thay lốp mà xe vẫn hành quân đêm 3. | Thêm [ACTION] ở SC_035 hoặc SC_126: "K511 #2 lốp dự phòng còn mới, lốp thủng buộc trên thùng" (không thoại). |
| NOTE (bible lệch, không phải lỗi script) | vehicle_bible dòng 285 "tên cắm lốp — 해모루 bắn", dòng 416 "을보 chốt sắt tạm **2화**"; prop_bible PROP_019 chỉ tập 3–5 | Script + outline + P-28: cậu bé 척후 là chủ mũi tên; 을보 chốt sắt ở **1화** P11 (SC_256–258); thanh sắt 1화 ≠ thanh bẩy PROP_019 (3화). | world-designer sửa vehicle_bible 2 dòng; prop_bible thêm PROP_019a "쇠못/축핀 rèn tay 1화". |
| NOTE | SC_013, SC_087, SC_126 | "K2 '천둥 1'", "천둥 2 và 3" — decisions #1: chữ Hangul trên xe **không vẽ bằng AI**, overlay ở edit. Script mô tả bình thường (đúng), nhắc veo-prompt không đưa Hangul vào prompt. | Ghi chú cho veo-prompt-engineer. |
| NOTE | §8b xưng hô chưa dùng | 을보 → 박기철 "쇠쟁이" (§8b) chưa xuất hiện dù hai người gặp ở SC_256–257. | SC_256 을보 thêm gọi trước quote: giữ "쇠는 쇠요." nguyên văn; SC_257 sau 박기철 → 1 SC nhỏ hoặc [SOUND] 을보 (off): "쇠쟁이." — gieo nickname cho 2–5화. |
| NOTE | SC_102 / SC_132 / SC_285 | 탁발흠 "máu chảy từ tai trái" → derived state chưa có trong character_bible (chỉ có sẹo thái dương trái). | character-designer thêm derived state "dried blood left ear (1화 P5–P12)". |

---
## 2. BẢNG RETENTION (beat theo phút)

Ký hiệu: ACTION · REVEAL · SỐ GIẢM · QUYẾT ĐỊNH · ĐỊCH THÍCH NGHI · XUNG ĐỘT · THREAT · OPEN LOOP · CHI PHÍ. Cột cuối = khoảng cách tới beat trước.

| Phút | SC | Loại | Beat | Δ |
|---|---|---|---|---|
| 0:02 | SC_001 | REVEAL | Mũi tên cắm lốp K511 | — |
| 0:24 | SC_004 | SỐ GIẢM | "위성 0개" | 0:22 |
| 0:32 | SC_005 | THREAT | "11시 방향 사람" — vệt bụi kỵ binh 3 km | 0:08 |
| 0:48 | SC_007 | REVEAL sử | 612 정월 탁군 · 113만 3천 8백 · 24군 | 0:16 |
| 1:14 | SC_011 | QUYẾT ĐỊNH | "전 차량, 위장망. 지금." | 0:26 |
| 1:38 | SC_014 | SỐ GIẢM | Flashback "연료 한 통" | 0:24 |
| 2:26 | SC_020 | ACTION-lite | Sét khô, la bàn quay, đèn tắt | 0:48 |
| 2:48 | SC_023 | REVEAL | Đường nhựa cắt sau 50 m | 0:22 |
| 3:12 | SC_026 | SỐ GIẢM | Radio chỉ nội bộ 10 km | 0:24 |
| 3:20 | SC_027 | REVEAL sử | 24군 · dân phu ×2 · 960리 | 0:08 |
| 4:22 | SC_034 | REVEAL | "편자가 없습니다" | 1:02 |
| 4:38 | SC_036 | SỐ GIẢM | "포탄 스물두 발" | 0:16 |
| 5:06 | SC_039 | SỐ GIẢM | "식량 사흘, 물 이틀" | 0:28 |
| 5:14 | SC_040 | QUYẾT ĐỊNH | Ở hay đi → drone bay tây | 0:08 |
| 6:02 | SC_046 | REVEAL | Cầu phao đang đẩy sang | 0:48 |
| 6:10 | SC_047 | REVEAL | Trại Tùy không thấy điểm cuối | 0:08 |
| 6:36 | SC_050 | SỐ GIẢM | "배터리 십팔 분" | 0:26 |
| 7:18 | SC_055 | ACTION (sử) | Goguryeo bắn xuống cầu ngắn 3 m | 0:42 |
| 7:42 | SC_058 | REVEAL sử | 맥철장 chết, cầu kéo về | 0:24 |
| 8:24 | SC_063 | THREAT | Cậu bé giương cung | 0:42 |
| 8:56 | SC_067 | REVEAL | "백만. 백만이오." | 0:32 |
| 9:30 | SC_071 | ACTION-lite | K21 nổ máy, cậu bé bỏ chạy | 0:34 |
| 10:04 | SC_075 | XUNG ĐỘT | 오태민: "왜 보내십니까?" | 0:34 |
| 10:20 | SC_077 | THREAT | Cầu nối lại, Tùy tràn bờ đông | 0:16 |
| 10:38 | SC_079 | THREAT | Dân chạy nạn 300, làng cháy | 0:18 |
| 10:46 | SC_080 | THREAT | 200 kỵ Tiên Ti cắt đầu | 0:08 |
| 11:02 | SC_082 | XUNG ĐỘT | Đòi K2 / "나가면 들킵니다. 기름도요." | 0:16 |
| 11:26 | SC_085 | QUYẾT ĐỊNH | "쏜다. 대신 전차는 안 나간다." | 0:24 |
| 11:42 | SC_087 | ACTION | 2 K21 xuất kích (narrator im 80 s) | 0:16 |
| 12:14 | SC_091 | ACTION | 40mm điểm xạ, đội hình vỡ | 0:32 |
| 12:30 | SC_093 | ĐỊCH THÍCH NGHI | 탁발흠 không chạy, lên đồi | 0:16 |
| 13:02 | SC_097 | ACTION / SỐ GIẢM | Drone #1 bị tên bắn rơi (4→3) | 0:32 |
| 13:18 | SC_099 | CHI PHÍ | 2 lính trúng tên | 0:16 |
| 13:44 | SC_102 | ĐỊCH THÍCH NGHI | 탁발흠 nhặt xác drone | 0:26 |
| 14:08 | SC_105 | THREAT | 300 kỵ Goguryeo trên gò | 0:24 |
| 14:34 | SC_108 | REVERSAL | "이들이 우릴 살렸소!" | 0:26 |
| 14:58 | SC_111 | REVEAL | "어느 성의 군사요?" / "성이 없습니다" | 0:24 |
| 15:30 | SC_115 | REVEAL | Năm → "육백십이년… 살수" | 0:32 |
| 16:18 | SC_121 | SỐ GIẢM | "식량 이틀 치" | 0:48 |
| 16:34 | SC_123 | QUYẾT ĐỊNH | Đi trong đêm, K2 cuối hàng | 0:16 |
| 17:06 | SC_127 | OPEN LOOP | "말보다 빠르오?" | 0:32 |
| 17:40 | SC_131 | ENEMY POV | Xác drone trước tướng Tùy | 0:34 |
| 17:56 | SC_133 | ĐỊCH THÍCH NGHI | 2.000 kỵ + "쌀 한 톨" | 0:16 |
| 18:38 | SC_138 | VẤN ĐỀ MỚI | K2 không lọt cổng | 0:42 |
| 19:10 | SC_142 | QUYẾT ĐỊNH | 고정수: thung lũng + 10 con tin | 0:32 |
| 19:36 | SC_145 | SỐ GIẢM | "전차 삼십 킬로" | 0:26 |
| 19:44 | SC_146 | THREAT | Đường đông bị cắt 2 ngày; 3.000 dân | 0:08 |
| 20:10 | SC_149 | SỐ | Kho lương 20 ngày | 0:26 |
| 20:26 | SC_151 | QUYẾT ĐỊNH | Nhiệm vụ: giữ đường đông một đêm | 0:16 |
| 20:42 | SC_153 | ĐỊCH | 탁발흠 2.000 kỵ vòng đông | 0:16 |
| 21:08 | SC_156 | SỐ GIẢM | "충전 한 번 = 경유 2리터" | 0:26 |
| 21:16 | SC_157 | SỐ GIẢM | "건전지 나흘치" | 0:08 |
| 21:24 | SC_158 | SỐ GIẢM | Kháng sinh 90 % | 0:08 |
| 21:56 | SC_162 | REVEAL / RULE | "역사가 이미 이겼다" | 0:32 |
| 22:04 | SC_163 | XUNG ĐỘT | "역사책이 우리 94명을 지켜줍니까?" | 0:08 |
| 22:28 | SC_166 | QUYẾT ĐỊNH | K2 ở lại lần 2 | 0:24 |
| 23:02 | SC_170 | ACTION-lite | Cối đăng ký 2 viên (120→118) | 0:34 |
| 23:50 | SC_176 | OPEN LOOP | 12 kính đêm → 6 | 0:48 |
| 24:00 | SC_177 | PLAN (yếu) | Sa bàn đất | 0:10 |
| 24:58 | SC_184 | FORESHADOW (yếu) | 오태민 gật miễn cưỡng; N "ba giờ" | 0:58 |
| 25:40 | SC_189 | QUYẾT ĐỊNH nhỏ | 을보 xin theo xe cuối | 0:42 |
| 26:30 | SC_195 | THREAT | Kỵ binh tập kết sau gò bắc | 0:50 |
| 26:54 | SC_198 | SỐ GIẢM | Drone #2: 24 → 12 phút | 0:24 |
| 27:12 | SC_200 | THREAT (hình) | Hàng vạn đốm lửa | 0:18 |
| 27:38 | SC_203 | ACTION | 400 kỵ lội bến — cối 8 viên | 0:26 |
| 28:34 | SC_210 | ĐỊCH THÍCH NGHI | 탁발흠 xòe 3 ngón | 0:56 |
| 28:50 | SC_212 | REVERSAL | 2 cánh vòng gò bắc → xe bò | 0:16 |
| 29:22 | SC_216 | ACTION | Kỵ chém đoàn xe | 0:32 |
| 30:10 | SC_222 | SAI SÓT | 오태민 phá lệnh | 0:48 |
| 30:34 | SC_225 | CHI PHÍ | 천둥 3 kẹt bùn | 0:24 |
| 30:42 | SC_226 | ĐỊCH THÍCH NGHI | Đuốc lên lưới — 탁발흠 học | 0:08 |
| 31:14 | SC_230 | SỐ GIẢM | Kính đêm 백성민 tắt | 0:32 |
| 31:38 | SC_233 | SỐ GIẢM | 40mm băng cuối | 0:24 |
| 31:46 | SC_234 | ACTION | Tù và — 300 kỵ lao xuống | 0:08 |
| 32:18 | SC_238 | REVERSAL | Bò + kỵ Goguryeo kéo K21 | 0:32 |
| 33:08 | SC_244 | QUYẾT ĐỊNH (sử-vai) | 고정수 mở cổng, 500 giáo | 0:50 |
| 33:56 | SC_250 | PAYOFF | Xe cuối qua cổng, cổng đóng | 0:48 |
| 34:04 | SC_251 | ĐỊCH | 탁발흠 rút lần 2, vẫn nhìn | 0:08 |
| 34:40 | SC_255 | CHI PHÍ | Trục cong, không phụ tùng | 0:36 |
| 34:48 | SC_256 | REVERSAL | "쇠는 쇠요" | 0:08 |
| 35:14 | SC_259 | SỐ GIẢM | Kháng sinh 20→18; 6 thương | 0:26 |
| 35:22 | SC_260 | SỐ GIẢM | 40mm 480 · cối 110 · pin 3 ngày | 0:08 |
| 35:30 | SC_261 | SỐ GIẢM | "이틀에 육십 킬로" | 0:08 |
| 35:46 | SC_263 | THREAT | Vòng vây khép | 0:16 |
| 36:14 | SC_266 | POLITICS | 고정수 hai câu "cái giá" | 0:28 |
| 36:48 | SC_270 | OPEN LOOP | Sứ giả từ 평양 | 0:34 |
| 37:04 | SC_272 | ĐỊCH | 탁발흠 mang drone đi tây | 0:16 |
| 37:48 | SC_277 | REVEAL | Chiếu vua "성과 함께 죽으라" | 0:44 |
| 38:08 | SC_279 | THREAT | "…그대들도." | 0:20 |
| 38:34 | SC_282 | ENEMY POV | Drone trước 양제 | 0:26 |
| 39:06 | SC_286 | OPEN LOOP | "손에 천둥을" / "가져오라" | 0:32 |
| 39:32 | SC_289 | OPEN LOOP | 113만 đang tìm 94 người | 0:26 |

**Kết quả:** 93 beat / 40 phút (≈1 beat / 26 s). Khoảng cách lớn nhất tính mọi beat = **1:02** (3:20 → 4:22, đoạn ken-burns sử + bốc đất). Nếu chỉ tính beat MẠNH (action/reveal/số/quyết định/địch thích nghi/threat) → gap lớn nhất **2:40 (23:50 → 26:30, P9 sa bàn)** — vẫn ≤4 phút mục tiêu, ngang kênh gốc (2–3 phút). Vùng yếu thứ hai: 1:38 → 2:26 (giới thiệu 5 nhân vật flashback, 48 s không nguy hiểm — chấp nhận vì mở series).
**Thiếu hụt về LOẠI beat:** 14:00 → 27:30 không có ACTION thật (13,5 phút) — retention giữ bằng reveal/số/politics, nhưng kênh gốc không bao giờ để 13 phút không bắn. → §3 #1.

---
## 3. ≤10 ĐỀ XUẤT "HAY HƠN KÊNH GỐC" (xếp theo tác động; đòn bẩy: ①địch có tên ②hậu cần đếm ngược ③nhân vật lịch sử là bộ não ④chi phí thật ⑤open loop mỗi phần)

| # | SC | Sửa gì | Vì sao (đòn bẩy) |
|---|---|---|---|
| 1 | P7 SC_136/137/144 · P8 SC_174–176 · P4 SC_054/059 | **Nâng combat 22 % → ~30 % không thêm SC:** (i) hành quân đêm P7: trinh sát Tiên Ti bám đuôi, 백성민 thấy qua kính đêm, 해모루 phái 10 kỵ đuổi — 3 clip không thoại; (ii) đêm P8: trinh sát địch dò thung lũng, 1 mũi tên cắm lưới K2 (prop đã có), lính gác kính đêm hạ 1 tên — 2 clip; (iii) P4 đổi 2 still sử thành video giao chiến. | Kênh gốc 45 % combat; ta 22 %. 13,5 phút giữa (14:00–27:30) không có tiếng súng là điểm rơi retention lớn nhất. (i) còn cho thấy 탁발흠 **đã bám theo từ đêm 3** → ① địch học liên tục. |
| 2 | SC_114–117 | 한승우 **tự suy ra năm**: "수나라, 백만, 요동성… 육백십이년입니다." → 해모루 chỉ xác nhận "대왕 즉위 스물세 해째요." | Kênh gốc: lính hỏi "năm nào?" và được trả lời. Ta: lính Hàn *biết sử của mình* — vừa là niềm tự hào 50+, vừa sửa lỗi 시호 (FIX), vừa tránh beat trùng S15. ③ |
| 3 | SC_288 (+SC_287) | 양제 nói **"뇌군이라 하라."** (giọng off trên still) — tên do Hoàng đế đặt, không do narrator. | ③ nhân vật lịch sử ra quyết định có thể nhìn thấy; câu 2 어절 làm được thumbnail/title 2화 ("황제가 이름을 붙였다: 뇌군"). |
| 4 | SC_001–004 | 30 s đầu 4 → 6 shot (tách SC_001, chèn insert 4 s giày/태극기 trên cỏ vàng). | Kênh gốc 13 shot/30 s là "hook không giải thích"; ta chỉ 4. Mật độ hình = retention 30 s đầu = CTR→AVD. |
| 5 | SC_266–267, SC_274 | 고정수 nói 2 câu "cái giá" **trong kho lương** khi đếm bao thóc bằng thẻ tre; tường tây chỉ giữ ảnh 2 lá cờ; SC_274 = 한승우 một mình. Đồng thời SC_150 đổi thành "삼천이 성 밖에서 죽소". | ② hậu cần là nhân vật (kho = đồng hồ của Goguryeo, đối xứng sổ 박기철); xóa tableau "2 chỉ huy trên tường" giống §17 kênh gốc; giữ "역사가 이미 이겼다" không bị mâu thuẫn. |
| 6 | SC_161–167 | Cãi trong lều → chẻ đôi bằng SC_168; 오태민 nói "전차를 내보내면…" khi bước ra **vỗ váy xích K2** (đối xứng 박기철 SC_083/187). | Kênh gốc không có 1 phút đứng nói. Xung đột chỉ huy được *nhìn thấy* bằng cùng một cử chỉ trên cùng chiếc xe — hai cách yêu K2. ④ |
| 7 | SC_242 / SC_251 | 탁발흠 **áp dụng bài học ngay**: SC_242 hắn chỉ cung về 천둥 2 ở cửa thung: "그물을 태워라." (2 어절) → 3 tên lửa cắm lưới 천둥 2, lính giật lưới; SC_251 cái nhìn cuối bắt "검은 통" trên K511 #2. | ① địch có tên *thích nghi trong cùng trận* chứ không chờ tập sau; gieo hỏa công 2화 bằng hình, không bằng narrator. |
| 8 | SC_212–213 | Drone #2 **hết pin giữa Phase 2**: 태오 "2호기, 이 분 남았습니다… 신호 끊깁니다" → mù đúng lúc 오태민 phá lệnh (SC_222). | ② đồng hồ tài nguyên đổ chuông trong climax; sai lầm của 오태민 xảy ra khi *không còn mắt trên trời* → hợp lý hơn, cái giá của "bay 2 lần × 12 phút" được trả ngay. |
| 9 | SC_109–123 | Chèn 2 beat không thoại (kỵ Goguryeo hạ cung khi 을보 gào; 서아 băng chân 을보 giữa khoảng trống) + 해모루 gõ chuôi kiếm lên giáp K21: **"쇠가 맞소."** trước khi hỏi "어디서 왔소". | ③ người lịch sử **thử** trước khi tin (foundation §4 을지문덕 "thử họ trước khi tin" — 해모루 học từ thầy); phá 2 phút shot-reverse-shot. |
| 10 | P10 veo-stage | Cắt đôi ~15 clip 8 s thành 2×4 s (cận→wide) trong Phase 1–3; giữ 8 s ở Phase 4 (narrator im, bò kéo xe) để tương phản nhịp. | Kênh gốc shot 4 s trong trận; ta 8 s đều → trận 7 phút cảm giác dài. Không đổi SC/thời gian. |

---
## 4. Địa lý (kiểm theo trình tự di chuyển)
탁군 (Bắc Kinh) → 요하 tây→đông ✓ · căn cứ ngày 1 = thảo nguyên bờ đông cách sông ~15 km (LOC_001 identity) ✓ (khuyến nghị ~8–10 km, xem NOTE drone) · hành quân đêm 3 về đông ~30 km tới 요동성 ✓ (요양 thật cách điểm vượt sông 40–60 km — hợp) · thung lũng cách cổng đông 2 km ✓ · đường đông từ các làng đông ✓ · sứ giả từ 평양 (đông-nam) ✓ · 탁발흠 về tây qua biển lều tới hành doanh bên 요하 trong 1 ngày (~45 km) ✓ · 육합성 chưa dựng (5월) ✓. Không địa danh thật nào bị đặt sai trình tự.

## 5. Điểm cần coordinator quyết (★)
1. SC_261 dầu: phương án (A) "하룻밤에 삼십 킬로 / 삼백칠십" + sửa ledger, hay (B) thêm beat dời căn cứ 30 km ngày 3.
2. SC_115 "영양왕 23년" → đổi sang suy luận của 한승우 + "대왕 즉위 스물세 해째" (đổi quote outline P6; giữ 5 quote đắt khác).
3. Có chấp nhận nâng combat bằng 2 khối mini (P7/P8) không đổi số SC (đề xuất §3 #1)? Ảnh hưởng ledger: +0 đạn nếu chỉ dùng kính đêm/tên; +1 lính gác bắn 3 viên K2C1 (không cần ghi).
