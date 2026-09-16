# QC — 4화 「평양」 full_script_ep4.md (v1, 287 SC, 40:00) · qc-reviewer · 2026-09-16

> Đối chiếu: series_foundation §4/§5/§7 4화/§8/§8b · outline_ep4 · story_bible §1 [史] (내호아·고건무·7 trận·thơ·방진) / §3 / §5.3 / quy tắc 시호 · character_bible (giọng + derived states 4화) · location_bible LOC_006/007/008 · vehicle_bible K2 4화 · prop_bible · resource_ledger v2 · decisions (mục "sau script-writer 4화 v1" P-38…P-52) · proposals P-38…P-52 (ep4) · **full_script_ep3.md header + phụ lục** (nối tiếp: K2 8 · dầu "400 딱" gần hết → ~20 km "산길 기준" · cối 50 · PZF 9 · 40mm 0 · drone 0 · kính đêm 10 · 93 sống/92 hiện diện + 태오 bị bắt · 천둥 3 ở bờ tây 압록 · 해모루 có radio · 을보/아리 đi cùng · tới 살수 = D17 (3화) = D−3 (4화)) · full_script_ep5.md header (radio, mũ 태오, D0) · channel style §4/§10/§11/§17/§19b/§20 · SCRIPT_BRIEF checklist · qc_ep1_script.md (mẫu).
> Đếm thật bằng `logs/scratch/qc-ep4/analyze.py`: 287 SC (239 video8s + 48 still 8–12 s) · 0 lỗ hổng thời gian · 147 câu thoại (dài nhất 11 어절, 0 câu >12) · 251 dòng N / 861 câu / 3.716 어절 (0 câu >15) · narrator vào 0:32 · 0–30 s 4 SC = 6 shot (2 × 2-BEAT) · 1 SC có 2 câu thoại (SC_128, đã duyệt) · 0 시호 trong thoại người đương thời.
> Tổng: **BLOCK 1 · FIX 16 · NOTE 22**. Không sửa full_script. Mục ★ = chạm outline/bible/tập khác → coordinator quyết (mục 5).

## 0. Kết luận nhanh
- Script **khớp outline 12/12 phần, 0 s lệch**, 5 quote nguyên văn + bài thơ 4 câu Hán đúng nguyên văn/âm Hán/dịch outline, K2 bắn đúng 2 → "여섯 발"/"잔탄 06", cối 50→30, PZF 9→6, 92→91, kính 30→20 %, radio 50→40 %, 영양왕 không gặp 한승우, 시호 0 vi phạm, [史] 내호아/주법상/고건무/빈 절/해포/30리/방진/사자 "행재소" đều đúng, decisions P-38/40/41/43 được áp dụng đúng. Nối tiếp 3화 đúng số ở mọi dòng tài nguyên. Radio protocol 4/4 câu đúng. Đây là bản v1 sạch nhất trong 4 tập về số liệu.
- **Ba lỗi nặng nhất:** (1) **Mũ 태오** — 3화 v1 cho 백성민 nhặt mũ trống ngàm kính của 태오 và 한승우 cầm suốt P10–P12 (3화 SC_245/248/285, P-49 prop list); 4화 SC_255 N nói "석문령에서 잃은 철모는 돌아오지 않았습니다" và 5화 (dòng 282) nói "그의 철모는 선비족이 가져갔습니다" → mâu thuẫn prop xuyên tập, veo-stage sẽ dựng sai (BLOCK★). (2) **"이천 년" ×11** (SC_023/114/171/218/240/252/253/269): 612→2026 = 1.414 năm; 1·2·3·5화 đều dùng "천사백 년" — narrator sai số và lệch series (FIX, sửa 8 câu). (3) **Timeline D3 vs D5**: SC_103 N "삼십만은 삼십 리 밖에 있었습니다" ở đêm D3 trong khi bảng ngày/đêm + SC_094 cho 30만 tới trại 30리 ngày D5 (FIX); cùng nhóm: SC_081 "이틀 전에 닫으라" (thực là hôm trước), SC_249/210 "보름째/보름 남짓" (theo bảng 3화 D16→4화 D7 = **10 ngày**, outline gốc "열흘째" mới đúng).
- **Benchmark thua kênh gốc rõ nhất:** #5 combat **thuần ~16 %** (khối có vũ khí ~33 %, khối theo cách đếm script-writer 36,9 %) vs gốc 45 %; #4 đại đội bóp cò lần đầu **19:07** (gốc ≤1:36) — có chủ ý "tập im lặng" nhưng là muộn nhất 4 tập; #13 shot trong trận **8,08 s, 0 2-BEAT ở P10** (gốc 4 s; 3화 có 3 2-BEAT trong P10); #2 30 s đầu 6 shot (gốc 13).

---
## 1. BẢNG LỖI

| Mức | SC / dòng | Vấn đề | Đề xuất sửa cụ thể |
|---|---|---|---|
| **BLOCK★** | SC_255 N (+ SC_248, 3화 SC_245/248/278/285, 5화 dòng 282, §8b, character_bible CHAR_005) | **Mũ 태오 mâu thuẫn xuyên tập.** 3화 v1: 백성민 nhặt "mũ 태오 — ngàm kính đêm trống" (SC_245), đưa 한승우 (SC_248), 한승우 cầm bên hông cả P11–P12 (SC_278 "ngón cái miết vào ngàm", SC_285 "mũ trống của 태오 cầm ở tay trái"); P-49 ghi thành prop. 4화 SC_255 N: "석문령에서 잃은 철모는 돌아오지 않았습니다"; 5화 dòng 282: "그의 철모는 선비족이 가져갔습니다"; §8b/bible: "mũ + giáp bị lột, không thu hồi". Ba nguồn nói mũ mất, một nguồn (3화, hình ảnh mạnh ×4) nói mũ ở trong tay 한승우. | **(B – khuyến nghị, 2 SC 4화 + 1 câu 5화):** SC_248 [ACTION] thêm: *"chiếc mũ trống ngàm kính của 태오 — 한승우 mang từ 석문령 — đặt xuống lau cạnh đầu cậu"* (payoff prop 3화, không thêm thoại). SC_255 N: **"석문령의 빈 철모는 한승우가 가지고 왔습니다. 눈이 없는 철모였습니다. 해모루가 먼저 다른 것을 씌웠습니다. 육백십이 년의 쇠였습니다. 태오는 그것을 벗지 않았습니다."** 5화 dòng 282 → "그의 철모는 눈을 잃었습니다. 대신 고구려 병사의 쇠투구를 썼습니다." **(A):** 3화 v2 bỏ beat nhặt mũ (4 SC) — mất hình "mũ trống" đã dùng 4 lần. |
| FIX | SC_023, SC_114 (×2), SC_171 (×2), SC_218, SC_240 (×2), SC_252, SC_253, SC_269 — 11 lần | **"이천 년 전/뒤"**: 612→2026 = 1.414 năm; 1화 (SC "천사백 년의 거리"), 2화, 3화 ("천사백 년 전의 조상이 천사백 년 뒤의 자손을 묻었습니다"), 5화 (×4) đều dùng **천사백 년**. Khán giả 50+ thuộc "1.400년 전 살수대첩". | Thay toàn bộ **이천 년 → 천사백 년**. VD SC_114: "천사백 년 전의 왕이 천사백 년 뒤의 군인에게 물었습니다." · SC_240: "천사백 년 전의 말이 천사백 년 뒤의 병사를 업었습니다." · SC_253: "이 땅에 묻힌 천사백 년 뒤의 사람들이었습니다." (số 어절 không đổi). |
| FIX | SC_103 N ↔ bảng ngày (D3) ↔ SC_094 (D5) | "삼십만은 삼십 리 밖에 있었습니다. 삼십 리는 그에게 하룻밤 거리였습니다." nói ở **đêm D3**; nhưng header + SC_094 N ("다섯 날을 걸어온 길") đặt 30만 tới trại 30리 ngày **D5**. Đêm D3 họ còn cách 평양 ~2 ngày đường. | SC_103 N: **"을지문덕이었습니다. 들에서 하룻밤만 성으로 들어온 것이었습니다. 삼십만은 아직 이틀 거리에 있었습니다. 그는 늘 그들보다 반나절 앞에 있었습니다."** |
| FIX | SC_081 N | "**이틀 전에** 닫으라 한 사람이 열라 했습니다" — cửa chùa đóng SC_060 (D2), mở SC_076–081 (D3 sáng) = hôm trước. | **"전날 닫으라 한 사람이 열라 했습니다."** |
| FIX | SC_249 N (open loop P10), SC_210 N, phụ lục C.2 (P-39) | **"보름째" / "보름 남짓"** không khớp bảng ngày: 천둥 3 + drone rời bờ tây 압록 ngày **D16 (3화)**; 4화 D1 = 3화 D20 → 4화 D7 = 3화 D26 → **10 ngày** ("열흘째" của outline đúng). 태오 bị bắt 3화 D14 đêm → 4화 D7 = **12 ngày** ("열이틀"). SC_248 "보름 전" (3화 D11 "살아 있어야 해" → 15 ngày) thì đúng. | SC_249 N: **"태오는 돌아왔습니다. 드론과 쇠수레는 이미 서쪽으로 열흘째 가고 있었습니다."** (giữ "쇠수레" của P-39, trả "열흘째" cho outline). SC_210 N: **"열이틀 만이었습니다."** Header thêm dòng "4화 D1 = 3화 D20" để tập sau tính mốc chéo. |
| FIX★ | SC_070, SC_074, SC_128, SC_262, SC_267 + tóm tắt P4 (5 chỗ) ↔ character_bible CHAR_205_night_hunt_ep4 | Script: 백성민 rạch **cẳng tay trái** 탁발흠, băng tay trái. Bible derived state (đã có ref ✔): "a fresh cut on the **right** forearm". Cùng loại lỗi 5화 P-38 (vết thương 해모루) — decisions đã chọn **theo bible vì ref đã có**. | Đổi 5 chỗ "cẳng tay trái" → **"cẳng tay phải"** (hợp lý hơn: hắn vung đao tay phải, 백성민 rạch tay cầm đao). Nếu coordinator muốn giữ "trái" → character-designer sửa derived + ref. |
| FIX | SC_130–147 (địa lý trận đêm) | Vòng đuốc từ **đông và nam** lùa về **tây = bãi cạn**; SC_141 "동쪽 고리는 끊기지 않았습니다"; K2 chỉ bắn vào cửa bãi cạn (tây). Sau đó đại đội "trượt **3 km thượng lưu**" (SC_147) = đi về **đông**, xuyên qua vòng đuốc đông còn nguyên. Không có SC nào cho thấy vòng đông tan. Sa bàn veo-stage sẽ rối (bài học 1화 SC_178). | SC_145 [ACTION] thêm: *"dải đuốc phía đông cũng vỡ — người cầm đuốc là dân phu Tùy, ném đuốc xuống nước bỏ chạy về bờ nam"*. SC_147 N thêm 1 câu: **"동쪽 고리는 소리 하나에 풀렸습니다. 그 틈으로 그들은 상류로 갔습니다."** (2 câu ≤15 어절). |
| FIX | SC_136, SC_141, SC_147, SC_157 | **Người trúng tên vào bụng không có SC bị bắn.** SC_136: tên vào **vai**; SC_141: tên vào **cổ** (chết); SC_147 bỗng có "người trúng tên vào bụng" trên cáng. Outline: 2 ngã (1 chết tại chỗ, 1 tên bụng). | SC_141 [ACTION]: *"một lính ngã ngửa — mũi tên cắm cổ; cách đó 3 m một người khác gập người ôm bụng, cán tên lộ giữa hai bàn tay"*; N: **"동쪽 고리는 끊기지 않았습니다. 한 사람이 목에, 한 사람이 배에 화살을 맞았습니다. 여울 어귀의 횃불 무리는 움직이지 않았습니다."** (giữ người trúng vai SC_136 = thương binh thứ 3, hợp "사람 둘" SC_154 vì vai nhẹ). |
| FIX | SC_140 (realism) | "xạ thủ PZF quỳ … quả thứ nhất, thứ hai, thứ ba" — PZF-3 phải tháo ống cũ, lắp ống mới vào cụm ngắm; 1 người không bắn 3 quả trong 8 s. Cựu binh 50+ biết. | [ACTION]: *"**ba** xạ thủ PZF quỳ cạnh nhau trong lau, ba quả gần như cùng lúc — bè nổ tung"*; 사수 "뗏목, 좌측! 발사!" giữ; N "PZF 셋. 뗏목 셋." giữ. |
| FIX | SC_035 [ACTION] ↔ SC_036 thoại | Insert "**sáu** ống PZF-3" trong khi 박기철 đọc "PZF **아홉**" (mỗi quả = 1 ống). Veo sẽ vẽ 6. | *"**chín** ống PZF-3 xếp dưới tấm poncho"*. (SC_155 "sáu ống" đúng vì đã bắn 3.) |
| FIX | SC_197 [ACTION] ↔ SC_042/043 | Cọc nước: D2 "chạm vạch thứ **hai**", "하루에 한 뼘씩" → D6 phải là vạch **sáu**; script ghi "vạch thứ **tư**". Khán giả theo dõi cọc (đồng hồ của tập) sẽ thấy lệch. | SC_197: *"nước đã lên tới vạch thứ **sáu**"*; SC_270 (D8) nếu vẽ cọc → vạch 8/"gần ngập". |
| FIX | SC_125 → SC_151 (해모루 ở đâu đêm D4?) | 해모루 có mặt trên đảo lau 1 tới 17:18 (SC_124). Trận trống-đuốc đêm D4 không nhắc anh; rạng D5 anh đã báo 을지문덕 cách 80 km "말 탄 사람의 입으로" (P-38). Không SC nào cho anh rời đảo hoặc nghe tiếng pháo. | SC_126 N mở: **"넷째 날 오후. 해모루는 답 없이 마을로 돌아갔습니다. 탁발흠은 우리를 강가로 옮겼습니다…"** · SC_148 N thêm: **"북쪽 마을에서 해모루도 그 소리를 들었습니다. 그는 남으로 달렸습니다."** → P-38 có nguồn hình. |
| FIX | SC_173 N ↔ P-38 | "천둥을 두 번 **듣고** 나서 을지문덕은 붓을 들었습니다" — P-38 (đã duyệt) nói ông **không nghe** trực tiếp, chỉ nhận báo cáo. | **"일곱 번 지고, 사만을 깨고, 천둥이 두 번 울렸다는 말을 듣고 나서 을지문덕은 붓을 들었습니다."** |
| FIX | SC_118 N ↔ SC_127 | "**강가에서 우리를 본 뒤로는** 하루도 참기 어려웠습니다" (D4 sáng) — 오태민 chỉ **thấy** cũi qua ống nhòm ở SC_127 (D4 chiều, sau đó). Đến lúc này anh chỉ **nghe** qua 서아/아리. | **"오태민은 사흘을 참았습니다. 강 건너 우리 이야기를 들은 뒤로는 하루도 참기 어려웠습니다."** |
| FIX | SC_074 (탁발흠) ↔ bảng ngày | "어디쯤인지는 **내일 밤에**." — đêm D3 không có gì ở Salsu (D3 = 빈 절 + hội đồng); hắn đến đêm D4. | **"찾았다. 갈대밭 안이다. 어디쯤인지는 다음 밤에."** (hoặc thêm 1 câu N ở SC_116: "사흘째 밤, 그는 오지 않았습니다. 비가 너무 컸습니다."). |
| FIX | SC_246 (서아) | "부러졌어요. 모르핀은 안 써요." nói khi 한승우 quỳ ngay cạnh và lính đứng quanh — bible: 서아 다나까 với đồng đội, 해요체 chỉ với dân/아리/thương binh khi riêng tư. SC_122 cô dùng 다나까 với 오태민. | **"부러졌습니다. 모르핀은 안 씁니다."** (nếu muốn giữ dịu: nhìn 태오 nói "부러졌어. 모르핀은 안 써." — 반말 chị em như "태오야"). |
| FIX (thì) | SC_130 N | "동쪽과 남쪽에서 반달처럼 조여 서쪽 여울로 **몹니다**. 여울 어귀에는 궁수 오백이 무릎을 꿇고 **기다립니다**." — hiện tại giữa narration quá khứ (quy ước header). | **"…서쪽 여울로 몰았습니다. 여울 어귀에는 궁수 오백이 무릎을 꿇고 기다렸습니다."** |
| NOTE [史] mềm | SC_183 N | "우문술은 **부총관**이었지만" — 우문술 là 좌익위대장군/부여도군 총관, một trong 9 총관; 양제 chỉ lệnh "諸軍諮稟仲文". "부총관" là chức thật (đã dùng cho 주법상 SC_054) → khán giả soi sử thấy sai chức. | **"우문술은 우중문 아래 있었지만, 이 순간 군은 그의 것이었습니다."** |
| NOTE [史] mềm | SC_088 N (P-51) | "삼국사기는 그날을 **한 줄로** 적었습니다" — đoạn 내호아 trong 삼국사기 dài nhiều câu (4만 → 수천, đuổi tới thuyền, 해포). Tu từ sai sự thật. | Bỏ 2 câu cuối, giữ "4만 중 수천 명만 배로 돌아갔습니다. 나머지는 시장과 골목과 강가에 남았습니다." (P-51 đã đề nghị). |
| NOTE | SC_025, SC_157, SC_250 | "항생제는 두 달 전에 끝났습니다" lặp **3 lần** nguyên văn. | Giữ SC_157 (đúng lúc cần); SC_025 → "항생제는 요동성에서 끝났습니다."; SC_250 bỏ câu (đã có "서아는 그것을 알면서"). |
| NOTE | SC_016 N ↔ 3화 bảng ngày | "살수를 건너기 전 **엿새** 동안 … 마흔두 번" — 3화 trận giả thua thứ nhất D10 (압록), 30만 tới 살수 D20 → 10 ngày. Không sai sử (삼국사기 không ghi số ngày) nhưng lệch bảng ngày 3화. | "살수를 건너기 전 **열흘** 동안…" và SC_016 "그렇게 열흘, 일흔 번을 졌습니다" — hoặc giữ 엿새 nếu coi 4 ngày đầu chưa đủ 7 trận/ngày (thêm "마지막 엿새"). |
| NOTE | SC_096, SC_175 | "열흘 전부터 같은 말을" / "얼굴은 열흘 전보다" — 우문술 đòi lui ở 압록 = 3화 D10 → 4화 D5 = 14 ngày; 을지문덕 thấy mặt lính Tùy = 3화 D9 → 4화 D6 = 16 ngày. | Cả hai → **"보름 전"**. |
| NOTE (ledger chéo) | SC_156 "무전기 사십" (D5) ↔ 5화 P1 "배터리 십오 퍼센트" (D10) | D2→D5: 50→40 (~3 %/ngày); D5→D10: 40→15 (5 %/ngày) — chấp nhận được (đêm cứu, gác), nhưng ledger cuối 4화 nên ghi **40 % (D5) / ~30 % (D8)** để 5화 không nhảy. | SC_254 박기철 thêm 2 어절: "아흔한 명. 야시경 배터리 이십. **무전기 삼십.**" (7 어절) → world-designer ghi ledger 30 %. |
| NOTE (realism) | SC_127 N | "이 킬로 밖에서도 **얼굴이** 보였습니다" — ống nhòm 7× ở 2 km mưa: nhận ra người/quân phục, không thấy mặt. | **"이 킬로 밖에서도 누군지 보였습니다. 얼굴은 안 보여도 알았습니다."** |
| NOTE (realism) | SC_160 [ACTION] | "vỏ đạn 120 mm đen bồ hóng, **nặng**" — đạn K2 (K276/K277) vỏ bán cháy, chỉ còn **đế kim loại** cỡ bàn tay. 2·3화 ledger đã ghi "vỏ đạn 120 mm lính Tùy nhặt" → thống nhất mô tả. | *"đế vỏ đạn 120 mm — vành thép to bằng bàn tay, đen bồ hóng"*; 탁발흠 xoay trên ngón tay — hợp "đếm bằng ngón". |
| NOTE (realism) | SC_221 N ↔ SC_043/SC_276 | "하루에 한 뼘" (≈20 cm) × 6 ngày = 1,2 m: gối → quá ngực; script nói "허리" (D7–D8) rồi 5화 D10 "가슴". Số học lệch nhẹ (bible/outline-level, không phải lỗi script). | Giữ "한 뼘" (quote outline); SC_276 N có thể nói "물은 매일 올랐습니다. 어떤 날은 한 뼘, 어떤 날은 반 뼘." để khán giả không nhẩm. |
| NOTE (hình) | SC_134 | "hàng trăm cung thủ Tùy quỳ… **máy thấp ngang cung**" = cận đám đông (foundation §9 cấm). | Wide ngược sáng đuốc từ sau lưng hàng cung; chỉ 1 sĩ quan Tiên Ti rõ mặt. |
| NOTE (hình >8 s) | SC_070 · SC_089 | SC_070: lao vào, bị rạch, kính lệch, mũ rơi xuống nước, **vớt lại** — quá 8 s. SC_089: bị hất, chộp ngựa, nhảy lên, xuống nước, áo cháy — 5 hành động. | SC_070 bỏ "vớt lại" (mũ trôi; SC_074 hắn đội mũ khác/đầu trần → derived state "cap lost" đã có ở 1화). SC_089: bỏ "áo choàng cháy"; giữ hất–chộp–xuống nước. |
| NOTE (đứng nói) | SC_194–196 (3 SC liên tiếp tĩnh: still VO + 2 video mặt) | Vượt quy tắc ≤2 SC nói liên tiếp (nhẹ: SC_194 là still). | SC_195 thành walk: 해모루 nói khi bước xuống mép nước, cúi rửa tù và; SC_196 giữ. |
| NOTE (anti-copy nhẹ) | SC_274 | "2 chỉ huy trên gò nhìn địch" (을지문덕 + 해모루) — hình hiệu §17 kênh gốc, dù không ở vị trí kết. | 해모루 không trên gò — ông đang ở bãi lau (SC_253 sáng D8, 80 km); SC_274 chỉ 을지문덕 + cờ; N giữ. Cũng sửa lỗi địa lý nhỏ (해모루 sáng D8 chôn người ở 살수, chiều cùng ngày trên gò cách 50–80 km). |
| NOTE | SC_222 (아리) | "이쪽이에요!" hét khi kỵ Tiên Ti đang đuổi trong sương — lộ vị trí; Phase 4 cô hét mới bị bịt miệng. | "(속삭임) 이쪽이에요." |
| NOTE | SC_060 | 고건무 "tự tay khép cửa" rồi nói "문을 닫아라. 불을 꺼라." | [ACTION]: hai lính khép cửa theo lệnh; ông ngồi xuống với khiên. |
| NOTE | SC_042 N | "박기철은 나무 막대에 눈금을 새겨 물에 꽂았습니다" như lần đầu — 3화 SC_280 ông đã cắm cành cây khắc vạch ở bãi bắc. | **"박기철은 이번에는 눈금을 새긴 막대를 꽂았습니다."** (nối 3화). |
| NOTE | SC_267 N | "갈대밭의 박기철은 알았습니다. 이십." — 20 % là pin kính của đại đội, không phải 2 kính 탁발흠 giữ (rời khỏi kho từ 3화 D14). Tu từ hơi gượng. | "갈대밭의 박기철은 자기 것을 알았습니다. 이십. 그 둘도 같은 건전지였습니다." |
| NOTE | SC_040 | Máy đếm tay "ba chữ số quay vòng" — máy đếm tay tiêu chuẩn 4 chữ số (9999). | "bốn chữ số"; N "만에서 다시 영으로". |
| NOTE (bible lệch, không phải lỗi script) | character_bible CHAR_102_wall_night_ep4 (P4/P12, đứng trên tường) · CHAR_005_rescued_ep4 "no helmet" · CHAR_107_night_trail_ep4 "paper lantern" | Script: vua ngồi nội điện P6 (đúng P-34/REF interior); 태오 đội mũ trụ từ P11 (P-46); đèn lồng do 을보 cầm (SC_246), 아리 cầm liềm. | character-designer: derived vua → "seated, black cloak, brush"; 태오 → "Goguryeo iron helmet from 4화 P11"; 아리 bỏ lantern. |
| NOTE (bảng ngày) | Header ↔ SC_271–276 | Bảng ngày không liệt kê SC_271–276 (방진 rút, 을지문덕 trên gò) — là D8. | Thêm dòng "D8 ngày [史] SC_271–276". |
| NOTE (radio 해모루) | SC_110/124/186/203 | 해모루 đeo radio 4 lần, **không dùng lần nào** trong 4화 (3화 dùng 7 lần, "말하는 돌"). P10 phối hợp tù và với đại đội hoàn toàn bằng… không gì cả. | Xem §3 #3 (1 câu radio ở SC_225). |
| NOTE (SC_128) | 2 câu thoại/1 SC | Đã duyệt (decisions); veo tách 2 beat. | — |

---
## 2. BẢNG RETENTION (beat theo phút)

Ký hiệu: ACTION · REVEAL · SỐ (tài nguyên nói/hiện) · QUYẾT ĐỊNH · ĐỊCH THÍCH NGHI · XUNG ĐỘT · THREAT · OPEN LOOP · CHI PHÍ · [史]. Δ = khoảng cách tới beat trước.

| Phút | SC | Loại | Beat | Δ |
|---|---|---|---|---|
| 0:03 | SC_001 | THREAT | Móng ngựa Tùy cách mặt 오태민 30 cm | — |
| 0:16 | SC_003 | THREAT | Lính Tùy tiểu cách 백성민 2 m | 0:13 |
| 0:24 | SC_004 | QUYẾT ĐỊNH | "쏘지 마. 숨 쉬는 것도 작게." | 0:08 |
| 0:32 | SC_005 | REVEAL/SỐ | 30만 5천 qua sông · 92명 | 0:08 |
| 0:40 | SC_006 | THREAT | Lính Tùy nhìn thẳng bụi lau | 0:08 |
| 0:56 | SC_008 | REVEAL | Bánh kê mốc — quân đói (nối 3화) | 0:16 |
| 1:04 | SC_009 | THREAT | Ngựa Tiên Ti hít mô bùn K2 | 0:08 |
| 1:12 | SC_010 | [史] | Sông tới gối, qua 1 ngày 1 đêm | 0:08 |
| 1:21 | SC_011 | OPEN LOOP | "을지문덕이 그렇게 명령했기 때문입니다" | 0:09 |
| 1:40 | SC_013 | ACTION [史] | 7 trận giả thua | 0:19 |
| 2:04 | SC_016 | REVEAL | 42 lần thua / 삼국사기 nhìn từ phía Tùy | 0:24 |
| 2:14 | SC_017 | ĐỊCH | 우중문 "평양은 사흘 거리다" | 0:10 |
| 2:22 | SC_018 | [史] | Hạm đội 내호아 vào 패수 | 0:08 |
| 2:32 | SC_019 | QUYẾT ĐỊNH (địch) | 내호아 "우중문보다 먼저" | 0:10 |
| 2:48 | SC_021 | PAYOFF/SỐ | K2 trát bùn — "두 번은 안 당합니다" | 0:16 |
| 3:04 | SC_023 | REVEAL | Các bà làng nuôi đại đội | 0:16 |
| 3:38 | SC_027 | REVEAL | "저 아이는 갈대를 베러 가는 게 아닙니다" | 0:34 |
| 3:46 | SC_028 | THREAT | Hậu quân 5천 + 탁발흠 giữ bãi cạn | 0:08 |
| 4:04 | SC_030 | ĐỊCH | 탁발흠 nhìn xuyên các bà về bãi lau | 0:18 |
| 4:20 | SC_032 | OPEN LOOP | 아리 mỗi chiều về "đã thấy trại địch" | 0:16 |
| 4:40 | SC_034 | SỐ | 92 · 8 viên · 20 km | 0:20 |
| 4:56 | SC_036 | SỐ | 박격포 50 · PZF 9 · 야시경 10/30 % | 0:16 |
| 5:12 | SC_038 | SỐ | "드론, 영. 우린 이제 장님입니다" | 0:16 |
| 5:20 | SC_039 | THREAT | 2 lính Tùy lạc hàng cách 3 m | 0:08 |
| 5:36 | SC_040 | SỐ | "하루 종일 셌습니다. 끝이 없습니다" | 0:16 |
| 5:46 | SC_041 | REVEAL | Cũi tre trong đoàn xe | 0:10 |
| 5:54 | SC_043 | SỐ | "하루에 한 뼘씩" | 0:08 |
| 6:02 | SC_044 | QUOTE | 을보 "사흘 만에 어른 키" | 0:08 |
| 6:26 | SC_047 | REVEAL | "대나무 우리요" | 0:24 |
| 6:50 | SC_050 | OPEN LOOP | Cậu bé trong cũi mặc đồ như họ | 0:24 |
| 7:00 | SC_051 | REVEAL | Cận cũi, mảng vải xé chỗ 태극기 | 0:10 |
| 7:26 | SC_054 | [史] | 주법상 can | 0:26 |
| 7:34 | SC_055 | QUYẾT ĐỊNH (địch) | "평양은 비었소. 사만이면 남소" | 0:08 |
| 8:00 | SC_058 | QUYẾT ĐỊNH [史] | 고건무 bỏ trống 나곽 | 0:26 |
| 8:16 | SC_060 | REVEAL | 500 vào chùa, đóng cửa | 0:16 |
| 8:34 | SC_062 | ĐỊCH POV | Kính đêm xanh của 탁발흠 | 0:18 |
| 9:06 | SC_066 | THREAT | "셋. 소리 없이" | 0:32 |
| 9:22 | SC_068 | ACTION | Đánh dao trong nước | 0:16 |
| 9:38 | SC_070 | ACTION/CHI PHÍ (địch) | 탁발흠 bị rạch tay | 0:16 |
| 9:46 | SC_071 | QUYẾT ĐỊNH | 백성민 đập nòng súng xuống bùn | 0:08 |
| 10:02 | SC_073 | REVEAL | "야시경입니다. 우리 겁니다" | 0:16 |
| 10:10 | SC_074 | ĐỊCH THÍCH NGHI | "찾았다. 갈대밭 안이다" | 0:08 |
| 10:18 | SC_075 | OPEN LOOP | Địch nhìn xa hơn họ | 0:08 |
| 10:30 | SC_076 | [史] | 4만 vào 나곽 | 0:12 |
| 10:48 | SC_078 | ĐỊCH | 내호아 "마음껏 가져가라" | 0:18 |
| 11:12 | SC_081 | QUYẾT ĐỊNH [史] | "지금이다. 문을 열어라" | 0:24 |
| 11:20 | SC_082 | ACTION (narrator im) | Cửa chùa bật, 500 tràn ra | 0:08 |
| 11:52 | SC_086 | REVERSAL | 내호아 "물러나라! 배로!" | 0:32 |
| 12:08 | SC_088 | SỐ [史] | 4만 → 수천 | 0:16 |
| 12:24 | SC_090 | QUYẾT ĐỊNH [史] | "배까지 쫓아라" | 0:16 |
| 12:42 | SC_092 | QUOTE | "평양은 고구려 사람이 지키오" | 0:18 |
| 12:50 | SC_093 | [史] | 해포 — thủy quân hết | 0:08 |
| 13:00 | SC_094 | ĐỊCH | Tin bại tới 우중문 | 0:10 |
| 13:16 | SC_096 | XUNG ĐỘT (địch) | 우문술 "이제 돌아가야 하오" | 0:16 |
| 13:32 | SC_098 | SỐ (địch) | Luộc yên ngựa | 0:16 |
| 13:48 | SC_100 | OPEN LOOP | 30만 "이제 혼자" | 0:16 |
| 14:10 | SC_102 | POLITICS | 고건무 vào nội điện mặt khói | 0:22 |
| 14:26 | SC_104 | REVEAL | Vua hỏi 뇌군 ở đâu | 0:16 |
| 14:50 | SC_107 | QUOTE | "누구의 군대인가" | 0:24 |
| 14:58 | SC_108 | XUNG ĐỘT | 고건무: giải tán, thu sắt | 0:08 |
| 15:06 | SC_109 | QUYẾT ĐỊNH | 을지문덕 "그다음은 그다음에" | 0:08 |
| 15:14 | SC_110 | QUYẾT ĐỊNH | Vua viết một dòng | 0:08 |
| 15:50 | SC_114 | REVEAL | 해모루 đọc thư vua | 0:36 |
| 16:06 | SC_116 | THREAT | Tên dò cắm cách mặt 1 m | 0:16 |
| 16:22 | SC_118 | XUNG ĐỘT | "태오는 저기 우리에 있고…" | 0:16 |
| 16:38 | SC_120 | XUNG ĐỘT/SỐ | "94명 … 이제 92명" | 0:16 |
| 16:46 | SC_121 | SỐ | "이십 킬로. 그게 우리 편" | 0:08 |
| 16:54 | SC_122 | REVEAL | 태오 bị đánh chân | 0:08 |
| 17:18 | SC_125 | OPEN LOOP | 한승우 không viết | 0:24 |
| 17:30 | SC_126 | THREAT | Cũi làm mồi ra bờ sông | 0:12 |
| 17:38 | SC_127 | XUNG ĐỘT | 오태민 thấy 태오 | 0:08 |
| 17:54 | SC_129 | ĐỊCH THÍCH NGHI | "젖은 갈대는 안 탄다. 몰아낸다" | 0:16 |
| 18:02 | SC_130 | THREAT | 200 đuốc, trống trên xe bò | 0:08 |
| 18:19 | SC_132 | THREAT | Trống từ đông và nam | 0:17 |
| 18:27 | SC_133 | REVEAL | "몰이입니다. 여울로" | 0:08 |
| 18:35 | SC_134 | THREAT | 500 cung chờ cửa bãi cạn | 0:08 |
| 18:51 | SC_136 | CHI PHÍ | Tên vào vai | 0:16 |
| 18:59 | SC_137 | QUYẾT ĐỊNH | Phá im lặng: "스무 발" | 0:08 |
| 19:07 | SC_138 | ACTION/SỐ | Cối 20 viên | 0:08 |
| 19:23 | SC_140 | ACTION/SỐ | PZF ×3 vào bè | 0:16 |
| 19:31 | SC_141 | CHI PHÍ | Tên vào cổ — chết tại chỗ | 0:08 |
| 19:39 | SC_142 | QUYẾT ĐỊNH | "천둥 1 … 두 발" | 0:08 |
| 19:55 | SC_144 | ACTION | K2 khai hỏa — sấm đêm mưa | 0:16 |
| 20:11 | SC_146 | ĐỊCH | 탁발흠 lóa kính, đếm 16 | 0:16 |
| 20:19 | SC_147 | CHI PHÍ | Rút 3 km với 1 xác + 1 tên bụng | 0:08 |
| 20:35 | SC_149 | OPEN LOOP | "뇌군이 우리 뒤에 있습니다" | 0:16 |
| 20:51 | SC_151 | QUYẾT ĐỊNH | 을지문덕 "서두르게 하시오" | 0:16 |
| 21:00 | SC_152 | CHI PHÍ | Xác bọc poncho | 0:09 |
| 21:10 | SC_153 | SỐ | "잔탄 06" | 0:10 |
| 21:18 | SC_154 | SỐ | "여섯 발. 이게 답니다" | 0:08 |
| 21:26 | SC_155 | SỐ | PZF 6 · 박격포 30 · 탄창 4 | 0:08 |
| 21:34 | SC_156 | SỐ | 무전기 40 · 연료 20 | 0:08 |
| 21:42 | SC_157 | CHI PHÍ/SỐ | Tên bụng, morphine, 0 kháng sinh | 0:08 |
| 21:58 | SC_159 | SỐ | 항생제 0 · 모르핀 9 · "이틀, 길면 사흘" | 0:16 |
| 22:08 | SC_160 | ĐỊCH | 탁발흠 đếm vỏ đạn "열여섯" | 0:10 |
| 22:16 | SC_161 | ĐỊCH THÍCH NGHI | "천둥도 센다. 언젠가는 마른다" | 0:08 |
| 22:24 | SC_162 | ACTION | 백성민 hạ trinh sát bám vết xích | 0:08 |
| 22:40 | SC_164 | QUYẾT ĐỊNH | "셋만. 총은 놓고" | 0:16 |
| 22:56 | SC_166 | QUYẾT ĐỊNH | "쏠 순 없어도 보낼 순 있다" | 0:16 |
| 23:12 | SC_168 | QUYẾT ĐỊNH | "넌 북쪽 여울을 지켜" | 0:16 |
| 23:28 | SC_170 | HUMOR | 을보 "얼굴만 빼고" | 0:16 |
| 23:48 | SC_172 | OPEN LOOP | Dao + cô bé thay 6 viên | 0:20 |
| 24:00 | SC_173 | [史] | 을지문덕 cầm bút | 0:12 |
| 24:26 | SC_176 | [史] | 우중문 đọc "신책구천문…" | 0:26 |
| 24:44 | SC_178 | REVEAL | "지족원운지" — thơ trọn vẹn | 0:18 |
| 24:54 | SC_179 | ĐỊCH | "나를 비웃는 것이냐?" | 0:10 |
| 25:02 | SC_180 | [史] | Sứ: "행재소에 조회하겠소" | 0:08 |
| 25:10 | SC_181 | ACTION | 300 kỵ 해모루 đánh toán kiếm ăn | 0:08 |
| 25:18 | SC_182 | SỐ (địch) | "사흘" | 0:08 |
| 25:26 | SC_183 | QUYẾT ĐỊNH [史] | 우문술: rút, 방진 | 0:08 |
| 25:42 | SC_185 | REVEAL | 방진 vẽ trên bùn — "살수로" | 0:16 |
| 25:52 | SC_186 | REVEAL | 해모루 mang thơ tới | 0:10 |
| 26:08 | SC_188 | PAYOFF | "태오가 외웠던 시다" | 0:16 |
| 26:16 | SC_189 | EMOTION | 태오 trong cũi thì thầm thơ | 0:08 |
| 26:24 | SC_190 | PLAN/SỐ | "내일 새벽" sương | 0:08 |
| 26:56 | SC_194 | QUYẾT ĐỊNH | 을지문덕 "사흘 안에. 여울 북쪽" | 0:32 |
| 27:04 | SC_195 | QUOTE | "반이 건널 때까지" | 0:08 |
| 27:12 | SC_196 | OPEN | "어느 쪽 반입니까?" | 0:08 |
| 27:20 | SC_197 | OPEN LOOP | 을지문덕 không nói nửa nào | 0:08 |
| 28:04 | SC_202 | QUYẾT ĐỊNH | "사격 금지" | 0:44 |
| 28:28 | SC_205 | THREAT | Lính gác vẫy qua | 0:24 |
| 28:44 | SC_207 | THREAT | Chó ngủ — "아직은" | 0:16 |
| 29:00 | SC_209 | ACTION | Dao, 2 lính gác | 0:16 |
| 29:16 | SC_211 | SAI SÓT | 태오 không đi được | 0:16 |
| 29:32 | SC_213 | THREAT | Tai chó dựng | 0:16 |
| 29:48 | SC_215 | ACTION | Chó sủa, tù và Tùy | 0:16 |
| 30:04 | SC_217 | REVERSAL | Kính đêm mù trắng | 0:16 |
| 30:12 | SC_218 | ĐỊCH THÍCH NGHI | "안개엔 눈이 없다. 귀로 잡는다" | 0:08 |
| 30:20 | SC_219 | THREAT | "물소리다. 저쪽!" | 0:08 |
| 30:36 | SC_221 | CHI PHÍ | Nước tới thắt lưng, cõng người | 0:16 |
| 31:00 | SC_224 | QUYẾT ĐỊNH | "대기." | 0:24 |
| 31:16 | SC_226 | ACTION | Tù và Goguryeo, 300 kỵ | 0:16 |
| 31:32 | SC_228 | REVEAL | Đường lau chỉ phụ nữ biết | 0:16 |
| 31:56 | SC_231 | ACTION | Dao dưới nước | 0:24 |
| 32:04 | SC_232 | SAI SÓT | 아리 hét — bịt miệng | 0:08 |
| 32:28 | SC_235 | ĐỊCH | 탁발흠 chọn sông | 0:24 |
| 32:52 | SC_238 | THREAT | 3 kỵ cách 80 m | 0:24 |
| 33:00 | SC_239 | REVERSAL | 20 kỵ không cờ | 0:08 |
| 33:16 | SC_241 | ACTION/SỐ | K6 một loạt — "마흔 발" | 0:16 |
| 33:24 | SC_242 | ĐỊCH | 탁발흠 nhớ "북쪽 여울" | 0:08 |
| 33:32 | SC_243 | QUYẾT ĐỊNH | K2 không bắn | 0:08 |
| 33:48 | SC_245 | ĐỊCH THÍCH NGHI | Nhặt chốt gỗ bị cắt | 0:16 |
| 34:04 | SC_247 | EMOTION | "죄송합니다… 드론을…" | 0:16 |
| 34:12 | SC_248 | PAYOFF | "살아 있잖아" | 0:08 |
| 34:20 | SC_249 | OPEN LOOP | Drone + xe đi tây | 0:08 |
| 34:40 | SC_251 | SỐ/CHI PHÍ | Morphine cuối → 8 | 0:20 |
| 34:48 | SC_252 | CHI PHÍ | Chết vì sốt | 0:08 |
| 35:04 | SC_254 | SỐ | "아흔한 명. 야시경 배터리 이십" | 0:16 |
| 35:12 | SC_255 | REVEAL | Mũ trụ Goguryeo | 0:08 |
| 35:28 | SC_257 | PAYOFF | Nghĩa bài thơ | 0:16 |
| 35:44 | SC_259 | REVEAL | Xe bò chở 천둥 3 về tây | 0:16 |
| 35:54 | SC_260 | ACTION [史] | 방진 bị đánh bốn mặt | 0:10 |
| 36:18 | SC_263 | ĐỊCH | "천둥은 여울 북쪽에 있습니다" | 0:24 |
| 36:26 | SC_264 | QUYẾT ĐỊNH [史-vai] | "네 죄를 잊겠다" | 0:08 |
| 36:34 | SC_265 | QUYẾT ĐỊNH | "살수까지 이틀" | 0:08 |
| 37:02 | SC_268 | POLITICS | Thư vua ngày thứ 5 | 0:28 |
| 37:18 | SC_270 | OPEN LOOP | 탁발흠 biết chính xác | 0:16 |
| 37:30 | SC_271 | REVEAL | 30만 quay đầu | 0:12 |
| 38:06 | SC_275 | QUYẾT ĐỊNH | 을지문덕 "살수로" | 0:36 |
| 38:24 | SC_277 | SỐ | "어제보다 한 뼘" | 0:18 |
| 38:40 | SC_279 | SỐ | "여섯" trên màn hình | 0:16 |
| 38:50 | SC_280 | EMOTION | 오태민 một mình ở bãi bắc | 0:10 |
| 39:24 | SC_284 | THREAT | 탁발흠 dẫn đầu về bắc | 0:34 |
| 39:42 | SC_286 | OPEN LOOP | "물은 오르고, 포탄은 여섯 발" | 0:18 |

**Kết quả:** ~150 beat / 40 phút (≈1 beat / 16 s). Khoảng cách lớn nhất tính mọi beat = **0:44** (27:20 → 28:04, sương + xâm nhập Phase 1 — đúng chỗ cần nín thở). Beat MẠNH (action/reveal/số/quyết định/địch thích nghi/threat): gap lớn nhất **1:06** (2:32 → 3:38, các bà làng + thuốc nguội) — ✅ ≤4', ngang/hơn kênh gốc (2–3'). Vùng "chỉ có beat mềm": 26:16–26:56 (kế cứu — 4 SC PLAN) và 37:02–37:30 (thư vua). Loại beat: ACTION thật của **đại đội** chỉ 3 cụm (9:22 dao · 19:07–20:11 cối/PZF/K2 · 29:00–33:24 cứu) — phần còn lại là threat/sử/địch, đúng thiết kế "tập im lặng" nhưng là lý do #4/#5 thua gốc.

---
## 3. ≤10 ĐỀ XUẤT "HAY HƠN KÊNH GỐC" (xếp theo tác động; đòn bẩy: ①địch có tên ②hậu cần đếm ngược ③nhân vật lịch sử là bộ não ④chi phí thật ⑤open loop mỗi phần)

| # | SC | Sửa gì | Vì sao (đòn bẩy) |
|---|---|---|---|
| 1 | P10 SC_209, 215, 226, 231, 240, 241 (+ P7 SC_139, 144) | **2-BEAT ×6–8 trong trận** (cận → wide trong cùng clip 8 s): dao/chó sủa/tù và/dao dưới nước/kéo lên ngựa/K6. 4화 có 0 2-BEAT ở P10 (3화 có 3). Không đổi SC/thời gian. | #13: kênh gốc 4 s/shot trong trận, ta 8,08 s. Cứu người trong sương là khối 7 phút dài nhất series không có tiếng súng — cần nhịp cắt để không "trôi". |
| 2 | SC_143 → SC_145 | **Bộ đếm "잔탄 08 → 07 → 06"** hiện trên màn hình trưởng xe đúng lúc 2 phát nổ (như 3화 SC_228–230 "12→08"): SC_143 2-BEAT (kính ngắm nhiệt → "08"), SC_145 kết bằng cận "06" nháy. | ② đồng hồ tài nguyên đổ chuông *trong* climax thay vì sáng hôm sau; nối thẳng tới thumbnail "포탄 6발". Kênh gốc: đạn vô hạn ngầm định. |
| 3 | SC_225 (+ SC_282) | 해모루 bấm radio trước khi thổi tù và: **"한 대장, 여기는 해모루. 나각 부오."** (5 어절) → rồi tù và. 4화 anh đeo radio 4 lần không dùng; 3화 gọi nó "말하는 돌". Trả luôn cho SC_282 (태오 trực máy: tiếng đầu tiên cậu nghe ở vị trí mới là giọng Goguryeo). | ③ + "công nghệ trong tay tổ tiên" (yếu tố riêng #16): đài hiện đại ra lệnh cho tù và 612. 1 câu, 0 SC mới. |
| 4 | SC_263 (+ SC_160–161) | 탁발흠 bán cho 우중문 không chỉ vị trí mà **con số**: sau "천둥은 여울 북쪽에 있습니다." thêm SC_263b (hoặc đổi SC_266 thành thoại): **"천둥은 열여섯 번 울었습니다. 남은 것은 셀 수 있습니다."** (9 어절). | ① địch có tên *dùng* bài học trong cùng tập (QC 1화 §3 #7); cho 우중문 lý do duy lý để tin — và 5화 "스물둘" có tiền đề. |
| 5 | SC_039–040 | Lính Tùy lạc hàng **dẫm lên bàn tay** lính Hàn đang nằm (không phải chỉ đứng cách 3 m) — anh không rút tay; N "세 걸음 안에 총이 셋" → "발밑에 손이 하나 있었습니다. 손은 움직이지 않았습니다." | #4: 4:30–7:00 không có contact thật; kênh gốc không để 12 phút không "chạm". Vật lý hơn, rẻ hơn mọi cách nâng combat. |
| 6 | SC_251 | Người sắp chết nói **một câu** (≤4 어절) trước khi 서아 "괜찮아요": VD **"…춥습니다, 하사님."** Không tên (giữ P-05), nhưng có giọng. | ④ chi phí thật: 2 KIA của tập đều câm; kênh gốc không bao giờ cho lính vô danh chết có tiếng. Khán giả 50+ là nhóm nhớ cái chết "vì không có thuốc". |
| 7 | SC_128 | 통역 dịch thêm 1 nhịp cho thấy 탁발흠 **tò mò kỹ thuật** (bible): sau "모릅니다", hắn không hỏi tiếp — chỉ tay lên trời rồi làm động tác cánh quạt bằng ngón; 태오 nhìn xuống cát. Không thêm thoại. | ① "kẻ thù nghiên cứu" (foundation §4) — 4화 hắn chỉ săn, chưa "học máy"; 1 cử chỉ 3 s gieo K21/drone về 낙양 (series 2). |
| 8 | SC_023 (still) | Trong khung các bà gánh rổ, **bờ nam xa có 2 kỵ Tiên Ti** đứng nhìn sang (chấm nhỏ). N thêm: "강 건너에서 누군가 그것을 보았습니다." | Lấp gap beat mạnh 2:32→3:38 (dài nhất tập); nối với SC_030 탁발흠 "아낙들은 두어라" — hắn *đã* thấy từ đầu. ① |
| 9 | SC_274–275 | Bỏ 해모루 khỏi gò (anh ở 살수 sáng D8); 을지문덕 **một mình** + cờ; thay cái gật bằng hành động: ông rút thẻ tre khắc **"半"** (반) đưa kỵ sứ — "살수로." | ③ nhân vật lịch sử ra quyết định *nhìn thấy được* thay vì gật; xóa tableau §17; sửa địa lý 해모루 (mục 1 NOTE). Chữ 半 = thumbnail 5화. |
| 10 | SC_268–269 | 한승우 mở thư vua lần 3 — thêm 1 cử chỉ: ông **rút bút chì của 박기철**, đặt lên lụa… rồi không viết, cài lại. | ⑤ open loop chính trị "누구의 군대인가" thành hành động dở dang (kênh gốc chỉ có open loop bằng lời); nối 5화 P12 "이제 우리는 뭡니까?". |

---
## 4. Địa lý (kiểm theo trình tự di chuyển)
살수 (청천강) bãi bắc → 30만 lội bãi cạn nam tiến ✓ · 9 quân tách 9 hướng, 평양 cách 200리 (~80 km) ✓ (SC_012, SC_111 nhất quán) · 패수 = 대동강, hạm đội cách 평양 60리 ✓ [史] · 나곽/내성 평양 ✓ · 해포 (vịnh biển) ✓ [史] · trại 30리 dựa núi bắc 평양 ✓ [史] · 해모루 평양↔살수 80 km/đêm với 2 lần đổi ngựa ✓ (khả thi) · 전령 Tùy 80 km từ bãi cạn tới trại D5 ✓ · hậu quân 5천 bờ nam bãi cạn [推] (P-41) ✓ · đảo lau 1 cách bãi cạn 2 km về **đông** (thượng lưu), đảo lau 2 thêm 3 km thượng lưu ✓ — **nhưng** vòng đuốc "đông + nam lùa về tây" rồi rút "thượng lưu" = đi xuyên vòng đông chưa vỡ → FIX (mục 1) · 해모루 300 kỵ "동쪽 이 리" bờ nam ✓ · mô cát bắc cách bờ bắc 100 m, 오태민 "북쪽 여울" cách đảo 2 200 m ✓ · 방진 từ trại 30리 về bắc, D8 "살수까지 이틀" → 5화 D10 ✓ · 천둥 3 "서쪽 삼백 킬로" (bờ tây 압록 + 10 ngày × ~12 km) ✓ xấp xỉ · 을지문덕 gò nhìn 방진 D8 rồi "살수로" ✓ (해모루 cùng gò = lệch, NOTE). Không địa danh thật nào bị đặt sai trình tự; thời điểm 내호아 nén từ 6월 [史] vào 7월 (story_bible cho "6–7월") — [推] chấp nhận.

## 5. Điểm cần coordinator quyết (★)
1. **Mũ 태오** (BLOCK): chọn (B) sửa 4화 SC_248/255 + 5화 dòng 282, giữ beat 3화 — hay (A) 3화 v2 bỏ 4 SC nhặt/cầm mũ. QC khuyến nghị **(B)**.
2. **Cẳng tay 탁발흠 trái → phải** theo bible/ref (như tiền lệ P-38 5화), hay sửa bible.
3. **"보름째" → "열흘째"** (SC_249) và "열이틀" (SC_210): đảo một phần P-39 — outline gốc đúng theo bảng ngày; giữ "쇠수레".
4. **Combat metric**: benchmark #5 nên ghi 2 số (khối / thuần) như phụ lục 3화; theo "khối" 4화 đạt 33–37 %, theo "thuần" chỉ 16 % — quyết định có coi "địch đi qua trên đầu 72 s" là combat không.
5. Đề xuất #3 (radio 해모루) và #4 (탁발흠 bán con số) chạm bible giọng nhân vật nhẹ — DUYỆT/không.
