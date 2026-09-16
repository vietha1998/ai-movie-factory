# QC — 5화 「살수」(最終話) full_script_ep5.md (v1, 289 SC, 40:00) · qc-reviewer · 2026-09-16

> Đối chiếu: QC_BRIEF · series_foundation §4–§10 · outline_ep5 (12 phần, 6 phase P10) · story_bible §1/§3/§5/§8/§9 + quy tắc 시호 · character_bible (LOCKED; giọng; derived 5화) · location_bible LOC_007 · vehicle_bible · prop_bible · resource_ledger v2 · decisions.md (mục "sau script-writer 5화": P-38 해모루 theo BIBLE · P-39 bow slung · P-42 289 SC · P-44 신세웅 → "수 장군" · P-46 không mid-roll 5 · P-47) · proposals P-38…P-49 · channel style §4/§10/§11/§17/§19b/§20 · SCRIPT_BRIEF checklist · **nối tiếp 4화 v1** (header bảng ngày/đêm D1–D8 + phụ lục; cuối 4화: K2 6 · cối 30 · PZF 6 · kính đêm 20 % · radio 40 % · morphine 8 · 91명 · 태오 mũ trụ Goguryeo · 탁발흠 bị chém cẳng tay TRÁI (SC_442 ep4) + kính đêm treo ngực · 30만 quay về 살수 · nước **허리** (ep4 SC_276 "이레 전 무릎 → 지금 허리") · 우문술 "살수까지 이틀") · 3화 header D1–D17 (천둥 3 gửi về tây D16, không vượt 압록 — decisions P-40 ep3).
> Đếm độc lập bằng `logs/scratch/qc-ep5/analyze.py`: **289 SC (248 video8s · 41 still 8–12 s) · 2.400 s · 139 câu thoại (dài nhất 11 어절, 0 SC có 2 câu) · narration 3.891 어절, 0 câu >15 · 0 narrator trước 0:32 · 2-BEAT ×19** — khớp phụ lục A của script-writer.
> Tổng: **BLOCK 1 · FIX 16 · NOTE 19**. Không sửa full_script. FIX chạm outline/ledger/bible đánh ★ → coordinator quyết (mục 5).

## 0. Kết luận nhanh
- **Ràng buộc cứng ĐẠT:** K2 đúng 6 → 0 (SC_008 "잔탄 06" → SC_086 "00" → SC_092 "다 썼습니다"), cối 30 → 0, PZF 6 → 0, 91 → 86 → 80, radio 15 → 10 → 5 → chết → 나각/cờ, K5 15 viên nói thành lời (SC_040) và bắn hết (SC_137–138), nhiệt nhôm 3화 trả (SC_161/189/224), biển 천둥 3 đặt lên xác K2 (SC_282), 탁발흠 giữ cung trên lưng (SC_123/124/245 — P-39), **우중문 bị bắt sống** và narrator nói rõ sử gốc ông chạy thoát (SC_236–237/263/269), 2.700 [史] (SC_252/266/277), **không đập nước** — script nói thẳng "을지문덕이 막은 것이 아니었습니다. 하늘이 막은 것이었습니다" (SC_064/191), không nhân vật có tên (phe ta) chết, 영양왕–한승우 không gặp và narrator nói thành lời (SC_280), series 2 「613」 gieo 3 dây + end card 「다음: 613」, không mid-roll 5, 12/12 open loop đúng câu outline, 5 quote nguyên văn.
- **Ba lỗi nặng nhất:** (1) **BLOCK — VEH_205 (cầu phao 요하) gắn cho ngựa/kỵ Tùy ở 21 SC** (SC_006/015/016/018/047/052/062/063/064/070/072/079/081/091/094/112/113/214/236/237/239): veo-stage sẽ đính ref cầu phao vào 우중문/우문술 trên ngựa → hình sai. (2) **Vết thương 해모루 viết theo outline (giáo vào sườn phải) trong khi decisions P-38 đã chốt theo BIBLE** (mũi tên dưới xương đòn trái, ref `CHAR_105_wounded_ep5` đã có) → 3 câu [ACTION] SC_234/243/255 (+1 chạm SC_248) phải sửa. (3) **Đồng hồ nước/ngày tự mâu thuẫn**: SC_012 "이레 전까지는 무릎" ↔ SC_044 "사흘 전에는 무릎, 어제는 배" ↔ 4화 kết "지금은 허리" (D8) ↔ SC_060 "열흘 전 밤" ↔ SC_053 "보름 전"; cộng SC_057 "간밤에 삼백 미터 / 갈대섬 → 여울 목 옆" (4화 kết ở đảo lau 2 cách 3 km; script lại nói 3 ngày ở đây) và SC_161/168/270 "두 달 / 마흔 날" (bảng ngày 3화–5화 chỉ ra ~30 ngày; xe bò 천둥 3 đã tới 육합성 ~2 tuần trước).
- **Kiểm đặc biệt (user):** (a) *6 phase có "sai sót" thật không?* — **KHÔNG.** Phase 3 「실수」 là *biến cố* (tên trúng chân 박기철 khi trượt khỏi mũi xe) + hệ quả của thứ tự "먼저 사람, 그다음 불" mà narrator khen là đúng (SC_216 "순서는 정해져 있었습니다"); không ai *quyết định sai*. Sửa rẻ: 1 câu N ở SC_221/222 gọi thẳng đó là sai lầm của 한승우 (đếm người trước lửa — đúng tính cách, và trả giá bằng chuyến quay lại dưới tên) — xem §3 #1. (b) *Narrator im ở đỉnh?* — **ĐẠT**: 10:38–12:30 (112 s, 6 con số + cối + PZF), 18:18–18:50 (K6 bị tràn), **31:30–33:22 (112 s, Phase 4)** + Phase 5 chỉ 1 câu N (SC_244) rồi im tới 34:10. (c) *Kết giống tableau §17?* — **KHÔNG BLOCK**: thứ tự kết = 육합성 양제 "내년" (P11) → điện 평양 3 người "내년에 또 올 것이오"/vua hoãn (P12) → đại đội "이제 우리는 뭡니까" → thơ → **xe bò K21 về tây** → card. Hai beat "địch thề quay lại" (b) và "thắng nhưng địch sẽ trở lại" (a) của §17 đều có, nhưng ĐẢO thứ tự, ở trong điện chứ không trên tường, chèn câu hỏi của đại đội, và hình cuối là công nghệ rò rỉ chứ không phải tướng địch gầm lệnh → khác skeleton. (d) K5 15 viên ✓ · nhiệt nhôm ✓ (nhưng N SC_225 "삼천 도" sai số + vi phạm "narrator không giải thích công nghệ") · biển 천둥 3 lên xác K2 ✓ (SC_282, cạnh số "1").
- **Benchmark thua kênh gốc:** #2 shot 30 s đầu **6** (gốc 13; đạt mục tiêu ≥5) · #13 shot trong trận **8 s danh nghĩa / ~7 s hiệu dụng** (gốc 4 s) · #5 combat **36,3 %** (đạt ≥35 %, gốc 45 %) · #4 đại đội bóp cò **10:46** (gốc ≤1:36; cố ý theo kế "nửa" — tập thứ 2 liên tiếp đại đội im >10 phút, cần veo/edit giữ nhịp bằng contact/threat).

---
## 1. BẢNG LỖI

| Mức | SC / dòng | Vấn đề | Đề xuất sửa cụ thể |
|---|---|---|---|
| **BLOCK** (ID/lock) | 21 SC: SC_006, 015, 016, 018, 047, 052, 062, 063, 064, 070, 072, 079, 081, 091, 094, 112, 113, 214, 236, 237, 239 (SC_006 header "수 기병 · VEH_205") | **VEH_205 = 요하 부교 (cầu phao Tùy — vehicle_bible dòng 347)** nhưng script dùng VEH_205 làm ID cho *ngựa/kỵ binh Tùy* (우문술 trên ngựa xám, 우중문 ngựa đen, 신세웅, 수 기병). 3화/4화 không dùng VEH_205 cho kỵ Tùy. Veo-stage đính ref cầu phao vào tướng Tùy trên ngựa → hình sai toàn P2/P4/P10. Chỉ SC_273 (cầu phao 요하) dùng đúng. | Xóa `VEH_205` khỏi 21 header trên (giữ SC_273). Nếu cần ref cho kỵ/ngựa tướng Tùy → proposals: **VEH_207 「수 장군 기마」** (ngựa chiến Tùy yên cao, giáp ngựa lụa đỏ, cho 우중문/우문술) — hoặc ghi "수 기병 (không ID, dùng WPN_201 + PROP_021)". Ghi chú cho veo-prompt-engineer: KHÔNG đính `@VEH_205` ở LOC_007. |
| FIX (decisions P-38) | **SC_234, SC_243, SC_255** [ACTION] (+ chạm SC_248) | **Vết thương 해모루 = giáo ngắn vào sườn phải** (theo outline Phase 4) — decisions đã chốt **theo BIBLE: mũi tên cắm dưới xương đòn trái** (`CHAR_105_wounded_ep5`: "arrow shaft embedded below the left collarbone… helmet gone, topknot loosened"; `CHAR_105_bandaged_ep5`: "white bandage wrapped diagonally across the bare chest and shoulder"). Script: SC_234 "giáo ngắn hạ — đâm vào sườn phải", SC_243 "hai tay đè lên sườn phải", SC_248 "sườn đẫm máu", SC_255 "sườn phải băng ép". | **SC_234 [ACTION]:** "Một kỵ xạ Tiên Ti thoát khỏi hàng giáo phi dọc mép nước, xoay người trên yên bắn ở 15 m — **mũi tên cắm dưới xương đòn trái 해모루** giữa lúc ông quay người; ông ngã ngửa xuống mép nước, mũ trụ rơi lăn xuống nước, tóc xổ, tay còn nắm đao, **cán tên dựng trên ngực**; kỵ sĩ phi tiếp và bị giáo Goguryeo hạ phía sau. Máy trung, không cận vết thương." · **SC_243 [ACTION]:** "서아 quỳ, hai tay ép quanh **cán mũi tên dưới xương đòn trái** 해모루 — không rút — máu loang áo xanh lá thành đen; ông mở mắt, nhìn qua vai cô về phía cổng họng… tay phải mò ra sau lưng — bao cung…" · **SC_248 [ACTION]:** "…**cán tên vẫn cắm dưới xương đòn trái**, cung giương bằng cả người còn lại — **cánh tay trái giữ cung run**, dây cung tới má…" (hình mạnh hơn giáo-sườn: người bị tên bắn tên). · **SC_255 [ACTION]:** "해모루 nằm ngửa trên chiếu lau, giáp đã cởi, **mũi tên đã rút nằm trên cát, băng trắng quấn chéo qua vai trái và ngực**; 서아 quỳ…". Thoại/SC/thời gian không đổi. Đồng thời SC_139–140: vết thương **lái xe K2** đang viết "cắm dưới xương đòn" — đổi thành "vai phải" để hình "tên dưới xương đòn trái" là của riêng 해모루. |
| FIX (decisions P-44) | SC_018, 047, 070 (nhãn thoại "신세웅:"), N SC_014/018/070/091/266, header dòng 6 | Decision: **신세웅 → "수 장군" generic + 1 dòng narrator gọi tên (không ref riêng)**. Script cho ông **3 câu thoại dưới nhãn 신세웅** và narrator gọi tên **5 lần** (SC_014, 018, 070, 091, 266); header ghi "3 shot" nhưng ông có mặt 4 SC + 2 N. | Nhãn thoại → **"수 후군 장수:"** (3 câu giữ nguyên). N SC_014: "앞은 우문술, 가운데는 우중문, 뒤는 후군이었습니다." · N SC_018: "뒤는 늘 뒤였습니다. 후군은 강을 등지고 언덕을 보았습니다." · N SC_070: "후군 장수는 물러서지 않았습니다. 후군이 무너지면 물속의 가운데 군은 등을 내주는 것이었습니다." · **Giữ tên ở SC_091 (cái chết [史])** — đúng 1 dòng, mạnh hơn vì tên chỉ vang lên khi ông chết. · SC_266 (tấu lên 양제): đề nghị "후군 장수 전사. 우중문 실종." (coordinator quyết giữ tên lần 2 hay không — mục 5). Veo: 1 EXTRA "수 장군 giáp 명광개 mũ tua đỏ" không cần CHAR_206. |
| FIX (ID) | SC_004, 019, 020, 066, 075, 111, 184 (`PROP_021 (cờ đỏ hiệu Goguryeo)`) | **PROP_021 = 수나라 깃발 (cờ Tùy đỏ viền vàng)**. Lá cờ đỏ hiệu lệnh của 을지문덕 trên gò nam (cuộn → mở = tín hiệu "nửa") không có PROP; gắn PROP_021 → veo đính cờ Tùy lên gò Goguryeo. | Tạo **PROP_024 「붉은 신호기」** (decisions đã dự kiến PROP_024 gom sau QC): "large plain red silk signal banner on a bamboo pole, rolled and tied with hemp cord, no emblem" — thêm vào 7 header; giữ PROP_021 chỉ cho cờ Tùy trong khung. |
| FIX (ID) | SC_161, 189, 213, 222, 224 (`PROP_008`) | **PROP_008 = 탄약통 (hộp đạn)**; script dùng cho **lựu đạn nhiệt nhôm** (3화 P1 cũng không có ID). Cận SC_161/189/224 là hero-prop của quyết định cuối → ref sai. | Tạo **PROP_025 「소이수류탄 (thermite)」**: "grey cylindrical incendiary grenade, faded stencil, pull ring, olive canvas strap" — 5 header + nhắc 3화 P1. (SC_032/036/041 PROP_008 đúng — hộp đạn/sổ.) |
| FIX (nối tiếp 4화 + nội tại) | SC_012 N · SC_044 N · SC_191 N · SC_053 N · SC_276 N · header bảng ngày | **Đồng hồ nước & đếm ngày lệch nhau:** 4화 kết (D8) "이레 전에는 무릎, 지금은 허리"; 5화 D1 = 4화 **D12** (SC_060 "열흘 전 밤" = đêm săn D2 ✓; "닷새" từ 평양 = rút D7 ✓). Nhưng SC_012 "이레 전까지는 무릎" (7 ngày trước = D5, khi nước đã quá gối) · SC_044 "**사흘 전에는 무릎**이었습니다. 어제는 배" (3 ngày trước = D9 — 4화 D8 đã 허리) · SC_191 "이레 동안 채운 물" · SC_053 "**보름 전**에도 그는 이 자리에서 삼십만을 보냈습니다" (11 ngày, và lúc đó họ ở đảo lau 1 cách 2 km) · SC_276 "**한 달 전** 해모루 편에 보낸 질문" (4화 D3 → 5화 D+8 = 17 ngày). | SC_012: "**열흘 전까지는** 그랬습니다. **열흘 동안** 상류에 비가 내렸습니다." · SC_044: "**사흘 전에는 허리였습니다.** 어제는 배였습니다." (무릎→허리→배→가슴 nối 4화) · SC_191: "하늘이 **열흘 동안** 채운 물이었습니다." · SC_053: "**열흘 전에도** 그는 **이 강가에서** 삼십만을 보냈습니다." · SC_276: "**보름 전** 해모루 편에 보낸 질문이었습니다." · Header: thêm dòng "**D1 = 4화 D12** (rút D7 + 닷새); nước: 4화 D1 무릎 → D8 허리 → 5화 D−1 배 → D1 가슴". (Ngoài phạm vi: 4화 SC_283–284 N khẳng định "이틀 뒤" theo lời 우문술 — 5화 đúng hơn với "닷새"; script-writer 4화 nên đổi thành "며칠 뒤".) |
| FIX★ (nối tiếp 4화 · ledger) | SC_057 N · header D0 · SC_021/032 | **K2 di chuyển:** 4화 kết K2 ở **đảo lau 2, 3 km thượng lưu** (ep4 SC_279); 5화 SC_057 N: "**간밤에** 전차는 **삼백 미터**를 움직였습니다. 갈대섬에서 **여울 목 옆으로**" — (a) 3 km chứ không 300 m; (b) "đêm qua" mâu thuẫn SC_025/026/103 "사흘째/사흘 동안/사흘 전" (đại đội đã ở cửa bãi 3 ngày); (c) "ở cạnh cổng họng" mâu thuẫn SC_021 "여울 목까지 삼백 미터"; (d) dầu: 3 km đường bằng mà P3 vẫn "연료 이십 킬로" (ledger 4화 đã làm tròn 1 lần "산길 기준"). | SC_057 N: "**사흘 전 밤**, 전차는 상류 갈대섬에서 **삼 킬로**를 내려왔습니다. 여울 목에서 삼백 미터. 자국은 사흘 비에도 지워지지 않았습니다. 오십오 톤은 자국을 남기는 법이었습니다." · Header D0 → **D−3** (trượt xuống cửa bãi; 백성민 đọc mô cát 3 ngày; radio 해모루 chết D−3). · Dầu — phương án **(A)** giữ "이십 킬로" + thêm 4 어절 ở SC_023 N: "…이십 킬로였습니다. **산길 기준, 박기철의 셈이었습니다.**" (nối 4화 C.6); **(B)** đổi "십칠 킬로" ở SC_032/023/157/159/206 — chạm quote ★ outline "연료 20km". Đề nghị (A). |
| FIX (nối tiếp 3화/4화) | SC_161 N · SC_168 N · **SC_270 N** · header D+5 · proposals P-49 | **Thời gian 천둥 3 & lựu đạn:** bảng ngày 3화 D1 (đêm bỏ xe, cầm lựu đạn) → 5화 D1 = 3화 D31 ≈ **một tháng**, script nói "**두 달 전**" (SC_161) / "두 달 동안" (SC_168). SC_270: xe bò 천둥 3 "**같은 날 오후** 수레가 닿았습니다. 압록수 남쪽에서 **마흔 날**" — 3화 P11/decisions P-40: 천둥 3 **không vượt 압록**, gửi về tây từ bờ tây 압록 ở 3화 D16 với bò 70리/ngày → tới 요동 (~400리) khoảng 3화 D22 = **4화 D3**; đến 5화 D+5 (= 3화 D36) đã ở 육합성 ~2 tuần; tổng đường cũng chỉ 20 ngày, không 40. P-49 tính 10 km/ngày từ *nam* 압록 là sai tiền đề. | SC_161: "**한 달 전** 요동성 골짜기에서…" · SC_168: "그는 **한 달 동안** 그것을 등에 지고 다녔습니다." · **SC_270 N:** "수레는 **보름 전에** 닿아 있었습니다. 소 마흔 마리, 선비 기병 이백. 탁발흠이 보낸 장갑차 천둥 3호였습니다. **황제는 그것을 만지지 않았습니다. 살수의 소식을 먼저 기다렸습니다.** 그리고 옻칠한 상자 안에 쇠새 한 마리. 보낸 사람은 살수에 있었습니다. 물속에." → SC_271 "오늘은 쇠수레를 만졌습니다" càng nặng (xem §3 #4). Header D+5 bỏ "마흔 날". |
| FIX★ (đăng ký · nối 1–4화) | SC_182 (해모루) · **SC_276 (고건무 — quote outline P12)** | **"총"** trong miệng người Goguryeo: 4 tập trước phe Goguryeo chỉ dùng từ "쇠" (쇠수레 · 쇠새 · "그 우는 쇠는 몇 발이나 남았소" 2화 · 4화 고건무 "**쇠를 거두어야 합니다**"). 5화: 해모루 "창은 말을 세우오. **총**은 사람을 세우시오." · 고건무 "**총이 없으면** 저들은 여든 명의 농부입니다." — 총(銃) là từ đời Cao Ly–Triều Tiên; khán giả 50+ xem 사극 bắt ngay; phá quy ước từ vựng series. | SC_182: **"창은 말을 세우오. 그대들 쇠는 사람을 세우시오."** (8 어절) · SC_276: **"쇠를 거두면 저들은 여든 명의 농부입니다."** (6 어절 — nối đúng câu 4화 của chính ông). Ghi proposals đổi quote outline P12 (★). |
| FIX (logic kế · payoff rơi) | SC_194 ↔ SC_185 ↔ Phase 1–2 (SC_205–211) | 해모루 hứa: "**마개가 서면 내가 나각을 불겠소**" (SC_194); 을지문덕 ra điều kiện: "**쇠수레가 목을 막으면** 우리는 꼬리를 치오. 전군." (SC_185). K2 dừng ở cổng họng 28:18 (SC_206) — **không SC nào 해모루 thổi 3 hồi, không SC nào gò nam nhận tín hiệu**; tù và duy nhất sau đó là 고구려 부장 thổi 1 hồi cho kỵ (SC_231). Kế của tổ tiên mất cái cò của nó. | SC_208 → **2-BEAT**: (a) 28:34–28:38 rìa lau: 해모루 nâng tù và — **ba hồi** (âm vang qua sông); (b) 28:38–28:42 aerial K2 chắn khe (giữ N). · SC_211 → 2-BEAT: (a) gò nam: 을지문덕 nghe hồi thứ ba, **hạ kiếm** — hàng kỵ sau gò lao xuống (không thoại); (b) tuyến bắc 오태민 "탁발흠이 빠집니다!". Không tăng SC. |
| FIX (story_bible §9) | SC_225 N | "테르밋은 **삼천 도**로 탔습니다…" — (a) narrator **giải thích công nghệ** (bible §9: "Narrator không bao giờ giải thích công nghệ cho khán giả… Công nghệ được hiểu qua mắt Goguryeo/Tùy"); (b) số sai (thermite ~2.500 °C). | **"물이 끄지 못하는 불이었습니다. 쇠를 녹이는 불이었습니다. 선비족은 그런 불을 본 적이 없었습니다."** (nhìn từ mắt địch; SC_228 đã tiếp "그는 타는 쇠를 보았습니다"). |
| FIX (sử mềm) | SC_263 N (+ story_bible §3 "chết trong ngục 613") | "역사에서 우중문은 달아났습니다. 그리고 **황제의 옥에서 죽었습니다.**" — 수서·우중문전: bị hạ ngục, ưu phẫn phát bệnh, **được thả khi bệnh nặng, chết ở nhà** (卒於家). Cách nói "chết trong ngục" là sai mềm; khán giả 50+ đọc sử có thể bắt. | "…그리고 **옥에 갇혔다가 병들어 죽었습니다.**" — story_bible §3 sửa cùng câu. |
| FIX (hình: hành động >8 s / 1 SC 2 chỗ) | SC_242 · SC_220 · SC_223 · SC_260 | SC_242: 서아/아리 **chạy 200 bước qua bãi lau** (SC_186 "이백 걸음") **và tới chỗ 해모루** trong 8 s. SC_220/223: kéo/lội **30 m nước ngang ngực** mỗi chiều trong 8 s — chính N nói "삼십 미터는 삼백 미터였습니다". SC_260: 을지문덕 **lội ngựa qua bãi cạn 800 m** rồi xuống mô cát trong 8 s. | SC_242 [ACTION] kết ở "băng qua lau rạp, qua xác ngựa — phía trước là mép nước đông" (tới nơi = SC_243). · SC_220/223 ghi **2-BEAT** với nhảy thời gian: (a) xuất phát dưới tên (b) tới nơi (jump cut, đúng phong cách 4 s kênh gốc). · SC_260 [ACTION] bắt đầu từ "ngựa 을지문덕 bước lên mô cát nhỏ, ông xuống ngựa" (đã qua sông). |
| FIX (templates/06 §8 — narrator lặp/nói trước thoại) | SC_120 · SC_150 · SC_155 · SC_206 · SC_116 · SC_278 | N nói đúng con số/ý mà thoại nói ngay sau: SC_120 N "남은 한 대는 십 퍼센트였습니다" + 태오 "우린 십 퍼센트" · SC_150 N "넷이 둘이 되었습니다" + 오태민 "탄창 둘 남았습니다" · SC_155 N "오 퍼센트" + 태오 "무전기 오 퍼센트" · SC_206 N "그는 시동을 껐습니다" + 박기철 "시동 끕니다" · SC_116 N "무게였습니다" cướp reveal "오십오 톤입니다" · SC_278 N "늘 다음 해를 먼저 보는 사람" cướp "내년에 또 올 것이오". | SC_120 N: "무전기 두 대 중 한 대가 죽었습니다. 이 부대의 목소리는 그만큼 남아 있었습니다." · SC_150 N: "한 번의 돌격이었습니다." · SC_155 N: "말 몇 마디의 값이었습니다. 이 부대의 21세기는 그만큼 남았습니다." · SC_206 N: "기름 이십 킬로 중 삼백 미터를 썼습니다. 남은 기름은 태울 것이었습니다. 목은 막혔습니다." · SC_116 N: "박기철은 다르게 세었습니다. 그에게 전차는 대포가 아니었습니다." · SC_278 N: "을지문덕은 문 쪽으로 갔습니다." |
| FIX (nối 4화 — pin radio) | SC_010 (+ header "15 %") | 4화 kết radio **40 %** (ep4 SC_156/phụ lục C.17); 5화 mở "십오 퍼센트" — rơi 25 điểm không có nguồn (bài học L-12: số phải có SC sinh ra số). | Thêm ở SC_010 N: "…남은 것은 무전기 한 대와 두 눈이었습니다. **나흘 밤을 켜 둔 값이었습니다.**" (radio trực đêm 4 đêm D−3→D1 — tự khớp bảng ngày). |
| FIX (sử mềm) | SC_273 N | "**113만이** 요하를 건너 돌아갔습니다." — 113만 3천 8백 là quân số **xuất phát**; sau 요동 4 tháng + 30만 5천 mất, không thể 113만 về; sử không ghi số về. | "**남은 대군이** 요하를 건너 돌아갔습니다." |
| FIX (hình: đứng nói) | SC_158–167 (10 SC, 80 s quanh K2) | Hội đồng quanh xe: 158 (vẽ vòng) · 159 (gõ xích) · 160 (ống nhòm) · 161 (túi ngực) · **162–163–164** (3 SC đứng nói) · 165 KB · **166–167** (2 SC đứng nói) · 168 (trèo xe). Dài hơn quy tắc ≤2 SC nói liên tiếp; mini-combat SC_169 (K3 nam hết đạn) nằm *sau* cả cụm. | **Dời SC_169 vào giữa SC_164 và SC_165** (giữ nội dung, đổi mốc giờ 22:38–22:46; các SC sau lùi 8 s tới 23:20 rồi khớp lại) → tiếng K3 tắt giữa lúc quyết định; 오태민 "…전차를요?" → cắt ngay sang súng nam câm → 165 KB nút bầu. Không tăng SC. |
| NOTE (thiết kế — kiểm đặc biệt) | Phase 3 「실수」 SC_216–226 | Không có *sai lầm* nào của phe ta — chỉ biến cố (tên vào chân) và thứ tự đã định. Đối chiếu 1화 (오태민 phá lệnh) / 3화 / 4화: "sai sót" của ta luôn là quyết định. | Xem §3 #1: 1 câu N ở SC_222 (thay "두고 올 수는 없었습니다…"): **"그것이 그의 실수였습니다. 불보다 사람을 먼저 세었습니다. 넉 달 동안 그랬습니다. 그래서 그는 돌아갔습니다."** — sai lầm đúng tính cách ("94명 전원"), trả giá bằng chuyến quay lại dưới tên. |
| NOTE (realism · khí tài) | SC_205–206 (+ SC_188/197) | K2 lội nước **không chuẩn bị ~1,2 m**; script cho xe chạy trong nước "ngang ngực người" (~1,3–1,4 m) rồi 박기철 tắt máy. Biên; nhưng đây là con số 박기철 *phải* biết và là "giới hạn của công nghệ" (story_bible §5.3) chưa được nói thành lời. | Thêm 1 câu 박기철 ở SC_188 (với 을보) hoặc SC_197: **"도하 준비 없이 일 점 이 미터. 가슴이면 아슬아슬합니다."** (7 어절). Tùy chọn mạnh hơn: SC_206 — động cơ **sặc nước tắt** trước khi ông kịp tắt ("물이 껐습니다") → sông là người tắt máy (xem §3 #2). |
| NOTE (realism) | SC_204 N | "삼백 미터는 **이십 초**였습니다" = 54 km/h trên cát ướt từ đứng yên — quá nhanh cho K2 (0→32 km/h ~7 s). | "**삼십 초**였습니다." |
| NOTE (realism) | SC_227 [ACTION]/N | Dầu diesel loang trên nước lạnh + mưa **rất khó bén lửa** từ "một mảnh cháy rơi" (điểm chớp cháy >52 °C); cựu binh 50+ biết. | Cho **"녹은 쇳물 한 방울"** (nhiệt nhôm phun sắt lỏng) rơi xuống vệt dầu ngay sát thân xe — vòng lửa bám quanh xe rồi trôi; N: "쇳물이 기름 위에 떨어졌습니다. 검은 물이 탔습니다." Giữ hình, thêm nguyên nhân. |
| NOTE (từ ngữ) | SC_130 N | "오십 미터. **화살이 총알보다 빠른 거리**였습니다." — vật lý sai, ý thơ khó hiểu. | "오십 미터. **쏘는 것보다 맞는 것이 빠른 거리**였습니다." |
| NOTE (đăng ký/từ đa nghĩa) | SC_015 (우문술) | "선봉부터 건너라. **짐은 버려라.**" — "짐" (hành lý) trùng âm "짐" (trẫm) mà 양제 dùng cùng tập; nghe TTS dễ hiểu thành "bỏ trẫm". | "선봉부터 건너라. **짐짝은 버려라.**" hoặc "**수레는** 버려라." |
| NOTE (nối 4화 · derived state) | SC_060, 124, 203, 244–245 (탁발흠) ↔ ep4 SC_442/464/781 · character_bible `CHAR_205_night_hunt_ep4` | 4화: 백성민 rạch **cẳng tay TRÁI** 탁발흠, băng vải (ep4 SC_442/464/781/1551 "cẳng tay trái băng"); bible derived ep4 ghi "**right** forearm"; 5화 (10 ngày sau) không nhắc băng/sẹo. | SC_060 [ACTION] thêm "cẳng tay trái quấn băng vải đen bẩn"; SC_245 (giương cung): "cánh tay trái cầm cung — băng cũ — run" → lý do vật lý 한승우 còn kịp sống tới mũi tên 해모루 (xem §3 #7). character-designer sửa `night_hunt_ep4` "right" → "left forearm". |
| NOTE (ai biết gì) | SC_060 N | "열흘 전 밤, 그는 **그 갈대밭**을 야시경으로 보았습니다" — đêm đó hắn dò **đảo lau 1** cách 2 km thượng lưu, không phải bãi lau cửa bãi này. | "열흘 전 밤, 그는 **이 강가의 갈대**를 야시경으로 보았습니다. **그들은 갈대를 떠나지 않는 자들이었습니다.**" |
| NOTE (số có nguồn) | SC_151 N ↔ SC_229 N | SC_151: súng của lính bị thương "그 소총에도 **탄창은 둘**이었습니다"; SC_229: 한승우 "**마지막 탄창**이었습니다" — băng thứ hai biến mất (SC_218 bắn 1, SC_229 bắn 3). | SC_151 N: "그 소총에는 **탄창이 하나**였습니다. 나머지는 이미 나뉘어 있었습니다." (nối SC_154 chia đạn). |
| NOTE (số) | SC_253 N | "여든 명… 스무 명은 다쳤습니다. 서 있는 사람은 **쉰 남짓**" — 80 − 20 = 60; trừ 태오/박기철 vẫn ~58. | "**예순 남짓**" hoặc "**스물다섯**은 다쳤습니다" (SC_171 đã có 20 thương *trước* P10, sau P10 phải nhiều hơn). |
| NOTE (hình §9 đám đông) | SC_002 | Low-angle hàng lính Tùy lội nước "mặt gầy, mắt trũng" — cận đám đông (foundation §9: đại quân = aerial, không cận đám đông). | Giữ khiên/giáo/cờ ở tiền cảnh, mặt chỉ 1 người rõ; hoặc 2-BEAT (a) chân (b) khiên trên đầu — cũng nâng #2 lên 7–8 shot/30 s. |
| NOTE (ID vũ khí) | SC_142, 181, 231–233, 240, 258 (`WPN_101 (giáo dài 삭)`) · SC_245 (`WPN_101 (cung Tiên Ti)`) | WPN_101 = cung 맥궁 & nỏ Goguryeo; giáo 삭 4 m và cung Tiên Ti không có ID. | Giáo dài: ghi "VEH_101 (giáo 삭 của 개마무사)" hoặc PROP mới; cung Tiên Ti: "VEH_206 (cung)". Ghi chú veo. |
| NOTE (header ≠ thân) | Header dòng 9 "해모루 … pin chết sáng P6" · dòng D0 | Thân: SC_025 "사흘째 대답이 없었습니다", SC_103 "말하는 돌은 사흘 전에 죽었습니다". Header nói chết sáng P6. | Header: "pin chết D−3 → P6 ông phi ngựa vào lau". D0 → D−3 (FIX SC_057). |
| NOTE (nối 4화 · derived state) | SC_009 (오태민 "băng bắp tay trái") | Bible 5화: "băng quấn bắp tay trái (tên sượt)" — script có băng từ 0:00 nhưng 4화 chỉ có "cẳng tay bầm"; không SC nào sinh ra vết tên sượt. | Hoặc chấp nhận (bị thương đêm 4화 P10 ngoài hình) — thêm 3 chữ ở SC_009 [ACTION] "băng bắp tay trái (tên sượt đêm cứu 태오)"; hoặc để SC_132 (P7) là lúc tên sượt → derived state đúng "5화". |
| NOTE (anti-copy §17) | P11 SC_266–272 → P12 SC_276–280 → SC_286–288 | Hai beat của §17 có mặt: 양제 thề "내년" (lều địch ra lệnh) và điện 평양 "내년에 또 올 것이오" (thắng nhưng địch sẽ trở lại). Khác: đảo thứ tự, trong điện, chèn "뭡니까", hình cuối = xe bò công nghệ. Không BLOCK. | Giữ. Để chắc: SC_279 đã kết điện bằng **vua hoãn** (không phải câu "địch sẽ quay lại") ✓; đừng để edit thêm shot 2 tướng nhìn sông ở P12. |
| NOTE (retention aftermath) | 34:30–40:00 (5:30 không action; P-47) | Chỉ SC_274 (still 613) có hình giao chiến; 3 still sử liên tiếp 37:30–38:00. | DUYỆT phương án P-47 nhưng đặt ở **SC_252** thay vì SC_273: đổi KB bản đồ 450리 thành video 8 s "kỵ Goguryeo truy kích tàn quân ở 압록수 · 왕인공 chặn hậu" [史] (+8 s combat, N giữ nguyên). |
| NOTE (0–30 s) | SC_001–004 | 6 shot/30 s (gốc 13). | 2-BEAT thêm ở SC_002 (chân → khiên trên đầu) và SC_004 (cờ cuộn → mặt 을지문덕) → **8 shot**, không đổi thời gian. |
| NOTE (P10 nhịp) | SC_200–229 (Phase 1–3, 30 SC × 8 s; 5 SC 2-BEAT) | Shot hiệu dụng ~7 s; kênh gốc 4 s trong trận. | Veo-stage: two-beat thêm ~12 clip Phase 1–3 (SC_201/202/205/207/210/212/214/217/219/223/225/227) → Phase 1–3 ≈ 5,5 s; giữ 8 s ở Phase 4 im lặng (tương phản). |
| NOTE (quy ước P-11) | SC_264 (을지문덕 ↔ 우중문 trực tiếp) | Đúng bible §5.2 (을지문덕 thạo Hán văn). Chỉ nhắc veo/edit: không phụ đề "dịch"; 2 người nói tiếng Hàn theo quy ước. | — |
| NOTE (nhân vật phụ) | SC_202 "수 부장: 검은 소다! 비켜라!" | "검은 소" là tên 탁발흠 đặt (bible); lính Tùy dùng chung được (đã nghe K2 ở 요동) — chấp nhận, nhưng nên có 1 lần lính Tùy gọi thế ở 2화 để tên lan. | Ghi chú cho 2화 (ngoài phạm vi). |
| NOTE (bible lệch) | character_bible `CHAR_205_final_ep5` "bow discarded" · `CHAR_105_wounded_ep5` "P9–P12" (thực tế P10 Phase 4 32:02 → P12) · `CHAR_002` 5화 "kính bảo hộ mất" ✓ SC_132 · `CHAR_003` 5화 "ngồi trên thân K2 với sổ tay" ✓ SC_282 | Bible cần cập nhật theo P-39 (bow slung) và mốc phần của 해모루. | character-designer (gom v3). |

---
## 2. BẢNG RETENTION (beat theo phút — mốc t1 của SC)

Ký hiệu: ACTION · REVEAL · SỐ (tài nguyên nói thành lời) · QUYẾT (quyết định) · SỬ-QUYẾT (nhân vật lịch sử quyết) · ĐỊCH (địch thích nghi/POV) · XUNG ĐỘT · THREAT · CHI PHÍ · PAYOFF · OPEN LOOP. Δ = cách beat trước.

| Phút | SC | Loại | Beat | Δ |
|---|---|---|---|---|
| 0:03 | 001 | THREAT | Chân lính Tùy đầu tiên xuống bãi cạn | — |
| 0:20 | 003 | SỐ | "여섯" (gõ 6 lần lên thép) | 0:17 |
| 0:24 | 004 | REVEAL | Cờ đỏ cuộn bên 을지문덕 — chưa mở | 0:04 |
| 0:32 | 005 | REVEAL sử | 30만 5천 quay về; 닷새 đói | 0:08 |
| 0:40 | 006 | REVEAL sử | "절반이 건넜을 때 쳤다" | 0:08 |
| 0:48 | 007 | SỐ | 91/94; "학교에서 배운 강" | 0:08 |
| 0:56 | 008 | SỐ | "잔탄 06" — radio "잔탄 여섯" | 0:08 |
| 1:04 | 009 | THREAT | "선두가 물에서 나옵니다" | 0:08 |
| 1:12 | 010 | SỐ | Radio 15 % | 0:08 |
| 1:20 | 011 | OPEN LOOP | "반" — nửa nào? tín hiệu chưa | 0:08 |
| 1:30 | 012 | SỐ/THREAT | Nước: 무릎 → (이레) | 0:10 |
| 1:42 | 013 | REVEAL | Cổng họng 60 걸음 — 30만 phải qua đó | 0:12 |
| 1:50 | 014 | REVEAL sử | 방진 3 khối; kỵ bám 4 mặt | 0:08 |
| 2:02 | 015 | SỬ-QUYẾT | 우문술 "짐은 버려라" | 0:12 |
| 2:10 | 016 | SỬ-QUYẾT | 우중문: cờ đứng giữa sông | 0:08 |
| 2:18 | 017 | ACTION [史] | Kỵ Goguryeo cắn sườn 방진 | 0:08 |
| 2:34 | 019 | REVEAL | Kế: cờ đỏ + 나각 3 | 0:16 |
| 2:46 | 020 | SỬ-QUYẾT | 을지문덕: "가운데 군이 물에 들거든" | 0:12 |
| 2:54 | 021 | SỐ | "여울 목까지 삼백 미터" | 0:08 |
| 3:10 | 023 | SỐ | 400 km đã chạy · 20 km còn | 0:16 |
| 3:28 | 025 | SỐ GIẢM | Radio 해모루 chết 3 ngày | 0:18 |
| 3:36 | 026 | REVEAL | Mô cát thượng lưu — "말 배까지" | 0:08 |
| 3:44 | 027 | REVEAL | "마개" — nút bầu | 0:08 |
| 4:00 | 029 | REVEAL | 91 + 1 xe = mảnh nhỏ nhất của kế | 0:16 |
| 4:10 | 030 | REVEAL | "물속의 반이다" | 0:10 |
| 4:18 | 031 | OPEN LOOP | "마개." | 0:08 |
| 4:30–5:28 | 032–038 | SỐ ×7 | 6 · 20 km · 30 · PZF 6 · 400/300 · 탄창 넷 · morphine 8 · 식량 하루 · 91 | ≤0:10 |
| 5:28 | 039 | QUYẾT | "다 쓰면 끝입니다. 다음은 없습니다." | 0:08 |
| 5:36 | 040 | SỐ | K5 15 viên | 0:08 |
| 5:44 | 041 | CHI PHÍ (cảm xúc) | Phát băng đạn tận tay | 0:08 |
| 6:08 | 044 | THREAT/SỐ | "가슴까지 왔소" | 0:24 |
| 6:16 | 045 | FORESHADOW | "쇠는 헤엄치지 못했습니다" | 0:08 |
| 6:24 | 046 | ACTION [史] | Kỵ Goguryeo đâm đuôi 방진 | 0:08 |
| 6:40 | 048 | SỐ | "두 시간이 더 필요했습니다" | 0:16 |
| 6:50 | 049 | OPEN LOOP → mid-roll 1 | "탄창 넷…21세기가 남긴 전부" | 0:10 |
| 7:00 | 050 | THREAT | Nước lên thêm 한 뼘 | 0:10 |
| 7:08 | 051 | THREAT | 5만 lên bờ cách lau 200 m | 0:08 |
| 7:16 | 052 | ĐỊCH POV | 우문술 nhìn lau một nhịp | 0:08 |
| 7:24 | 053 | XUNG ĐỘT | "지금입니다." | 0:08 |
| 7:32 | 054 | QUYẾT | "아직." | 0:08 |
| 7:56 | 057 | ĐỊCH | 척후 thấy vết xích | 0:24 |
| 8:04 | 058 | TENSION | Nòng súng bị ấn xuống | 0:08 |
| 8:20 | 060 | ĐỊCH | "안다. 검은 소는 거기 있다." | 0:16 |
| 8:28 | 061 | ĐỊCH học | "천둥은 셀 수 있다. 다 세면 들어간다." | 0:08 |
| 8:36 | 062 | REVEAL | 방진 méo trong nước | 0:08 |
| 8:44 | 063 | SỬ-QUYẾT | 우중문 "여기 선다. 깃발을 세워라." | 0:08 |
| 8:52 | 064 | THREAT | Nước lên trong lúc đứng — "하늘이 막은" | 0:08 |
| 9:00 | 065 | REVEAL | "절반." | 0:08 |
| 9:10 | 066 | SỬ-QUYẾT | Cờ đỏ mở | 0:10 |
| 9:18 | 067 | ACTION | Tên lửa | 0:08 |
| 9:26 | 068 | REVEAL | Trống 3 bề — Goguryeo ở cả hai bờ | 0:08 |
| 9:34 | 069 | ACTION [史] | Kỵ vào hậu quân — "여덟 번째는 결전" | 0:08 |
| 9:50 | 071 | THREAT | Kỵ Goguryeo trên đồi bắc | 0:16 |
| 9:58 | 072 | ĐỊCH POV | 우문술 "양쪽이다" | 0:08 |
| 10:14 | 074 | TENSION | "나각은 아직입니다" | 0:16 |
| 10:22 | 075 | OPEN LOOP | "절반이 물속에" | 0:08 |
| 10:30 | 076 | SIGNAL | 나각 3 hồi | 0:08 |
| 10:46–11:50 | 078–086 | ACTION ×6 | "여섯…하나" — 6 phát, cờ tung, 우중문 xuống nước | ≤0:16 |
| 12:06 | 088 | ACTION | Cối 30 viên | 0:16 |
| 12:22 | 090 | ACTION | PZF 6 → 6 bè | 0:16 |
| 12:30 | 091 | [史] CHI PHÍ địch | 신세웅 chết | 0:08 |
| 12:38 | 092 | SỐ | "다 썼습니다." (22 = 10+4+2+6) | 0:08 |
| 12:54 | 094 | REVERSAL | 우문술 quay 5만 lại | 0:16 |
| 13:02 | 095 | THREAT | 5만 đổ về nút chai | 0:08 |
| 13:18 | 097 | SỐ | "박격포, 탄 없음!" | 0:16 |
| 13:34 | 099 | ĐỊCH | 탁발흠 đếm 6 ngón — "일곱 번째는 오지 않았습니다" | 0:16 |
| 13:42 | 100 | OPEN LOOP → mid-roll 2 | "여섯. …그리고 조용하다." | 0:08 |
| 14:08 | 103 | REVEAL | 해모루 phi vào + 100 giáo | 0:26 |
| 14:16 | 104–105 | LỆNH | "지키시오. 물러서지 마시오." / "한 명도 북으로" | 0:08 |
| 14:32 | 106 | THREAT | 2.000 kỵ từ đồi bắc | 0:16 |
| 14:40 | 107 | REVEAL | Hai gọng kìm — "계획에 그 부분은 없었습니다" | 0:08 |
| 14:50 | 108 | XUNG ĐỘT | "장군 계획입니다. 죽는 건 우리 애들입니다." | 0:10 |
| 14:58 | 109 | QUYẾT | "지킨다." | 0:08 |
| 15:14 | 111 | SỬ-QUYẾT | 을지문덕 không chia quân | 0:16 |
| 15:24 | 112 | ĐỊCH POV | 우문술 thấy 뇌군 | 0:10 |
| 15:32 | 113 | SỬ-QUYẾT | "뚫어라." | 0:08 |
| 15:40 | 114 | ACTION | 1.000 khiên tiến, tên rơi | 0:08 |
| 15:48 | 115 | XUNG ĐỘT | "빈 전차가 뭘 합니까?" | 0:08 |
| 15:56 | 116 | FORESHADOW | "오십오 톤입니다." | 0:08 |
| 16:20 | 119 | QUYẾT | 해모루 ở lại | 0:24 |
| 16:28 | 120 | SỐ | Radio 10 % | 0:08 |
| 16:36 | 121 | ACTION | K3 150 m | 0:08 |
| 16:52 | 123 | THREAT/ĐỊCH | 2.000 kỵ, tai ngựa bịt | 0:16 |
| 17:10 | 125 | SỐ | 2.000 / 5만 / 91 + 100 | 0:18 |
| 17:18 | 126 | OPEN LOOP | "두 방향에서." | 0:08 |
| 17:30 | 127 | ĐỊCH | "쇠수레가 벙어리가 됐다. 지금이다." | 0:12 |
| 17:46 | 129 | ĐỊCH học trả | Ngựa không hoảng | 0:16 |
| 17:54 | 130 | CHI PHÍ | Lính trúng tên cổ | 0:08 |
| 18:18 | 133 | CHI PHÍ (im) | K6 bị tràn | 0:24 |
| 18:34 | 135 | REVERSAL | 을보 hất kỵ sĩ bằng thanh sắt | 0:16 |
| 18:50 | 137 | ACTION | K5 ở 10 m | 0:16 |
| 18:58 | 138 | SỐ | K5 15 → 0 | 0:08 |
| 19:06 | 139 | CHI PHÍ | Lái xe trúng tên | 0:08 |
| 19:22 | 141 | THREAT | Nam 100 m | 0:16 |
| 19:30 | 142 | REVERSAL | Giáo Goguryeo dựng ngựa | 0:08 |
| 19:38 | 143 | SỐ | K3 băng cuối | 0:08 |
| 19:46 | 144 | QUYẾT | "수색, 대기. 아직입니다." | 0:08 |
| 20:02 | 146 | ĐỊCH | 탁발흠 cách xe 50 m — không vội | 0:16 |
| 20:10 | 147 | ĐỊCH học | Không xông thẳng — đợi lau tự cạn | 0:08 |
| 20:18 | 148 | CHI PHÍ | 91 → 86 | 0:08 |
| 20:26 | 149 | SỐ | Morphine 8 chưa dùng | 0:08 |
| 20:34 | 150 | SỐ | "탄창 둘 남았습니다." | 0:08 |
| 20:50 | 152 | OPEN LOOP → mid-roll 3 | "왼쪽이 무너지고… 탄창은 둘" | 0:16 |
| 21:08 | 154 | SỐ | Chia đạn 15/15 | 0:18 |
| 21:16 | 155 | SỐ | Radio 5 % | 0:08 |
| 21:24 | 156 | SỐ | Kính đêm = thủy tinh + nhựa | 0:08 |
| 21:32 | 157 | SỐ | 20 km · 55 t · 0 viên | 0:08 |
| 21:42 | 158 | PLAN A | 토치카 | 0:10 |
| 21:50 | 159 | SỐ | "이십 킬로. 삼백 미터. 다 태워도 됩니다." | 0:08 |
| 21:58 | 160 | REVEAL | Khe 60 걸음 giữa 5만 và 10만 | 0:08 |
| 22:06 | 161 | PAYOFF | Lựu đạn 3화 + nút bầu + mũi tên | 0:08 |
| 22:22 | 163 | QUYẾT | "전차를 여울에 박는다. 마개는 우리다." | 0:16 |
| 22:48 | 166 | QUYẾT | "제가 몹니다. 십 년 몰았습니다." | 0:26 |
| 23:04 | 168 | PROP | Biển 천둥 3 vào túi ngực | 0:16 |
| 23:12 | 169 | ACTION/SỐ | K3 nam hết; giáo chặn | 0:08 |
| 23:20 | 170 | QUYẾT | "북안은 제가 맡습니다." | 0:08 |
| 23:44 | 173 | FORESHADOW | "쇠는 물에 가라앉지." | 0:24 |
| 23:52 | 174 | OPEN LOOP | "버리는 방법이 문제였습니다." | 0:08 |
| 24:00 | 175 | PLAN | Vẽ trên cát: 300 m · 목 · 쇠 | 0:08 |
| 24:18 | 177 | SỐ | 5 % cuối cho một câu | 0:18 |
| 24:26 | 178 | SỐ GIẢM | Radio chết | 0:08 |
| 24:34 | 179 | ACTION-lite | "모래톱 길로 갑니다. 지금." | 0:08 |
| 24:42 | 180 | REVEAL | 나각 + cờ thay radio | 0:08 |
| 25:06 | 183 | SỐ | "탄창 둘. 한 발에 하나다." | 0:24 |
| 25:24 | 185 | SỬ-QUYẾT | "쇠수레가 목을 막으면 우리는 꼬리를 치오. 전군." | 0:18 |
| 25:40 | 187 | QUYẾT | 태오 "제가 눈입니다." | 0:16 |
| 25:48 | 188 | REVEAL | Van dầu — "검은 물" | 0:08 |
| 26:04 | 190 | ACTION/SỐ | "K3 탄 떨어졌습니다!" | 0:16 |
| 26:12 | 191 | THREAT | Nước ngực — không chạy được | 0:08 |
| 26:20 | 192 | ĐỊCH POV | 우중문 "물이 왜 이렇게 빠른가" | 0:08 |
| 26:40 | 194 | PROMISE | "마개가 서면 나각을 불겠소" | 0:20 |
| 26:48 | 195 | PAYOFF | Nút bầu cắm vào xe | 0:08 |
| 26:56 | 196 | CẢM XÚC | "다녀오십시오." | 0:08 |
| 27:04 | 197 | QUYẾT | "가자, 이놈아." | 0:08 |
| 27:20 | 199 | OPEN LOOP → mid-roll 4 | "300미터." | 0:16 |
| 27:30 | 200 | ACTION | K2 nổ máy | 0:10 |
| 27:46 | 202 | REVERSAL | Tùy dạt — "검은 소다!" | 0:16 |
| 27:54 | 203 | ĐỊCH | 탁발흠 biết nòng rỗng | 0:08 |
| 28:10 | 205 | ACTION | 55 t xuống nước | 0:16 |
| 28:18 | 206 | SỐ | "시동 끕니다" — 300 m của 20 km | 0:08 |
| 28:26 | 207 | THREAT | Dầu loang | 0:08 |
| 28:34 | 208 | REVEAL | "마개는 쇠였습니다." | 0:08 |
| 28:50 | 210 | ĐỊCH | Bỏ trận — 500 kỵ xuống nước | 0:16 |
| 29:06 | 212 | THREAT | Tên phủ xe | 0:16 |
| 29:22 | 214 | SỬ-QUYẾT | 우문술 thử vòng — "육십 걸음은 영 걸음" | 0:16 |
| 29:30 | 215 | THREAT | Đao gõ nóc | 0:08 |
| 29:38 | 216 | QUYẾT | "박 상사, 나간다. 지금." | 0:08 |
| 29:54 | 218 | ACTION | Bật nắp, 1 phát | 0:16 |
| 30:02 | 219 | CHI PHÍ | Tên vào chân 박기철 | 0:08 |
| 30:26 | 222 | QUYẾT | Quay lại xe — "가지 마십시오." | 0:24 |
| 30:42 | 224 | ACTION | Nhiệt nhôm vào khoang đạn | 0:16 |
| 31:06 | 227 | ACTION | Lửa trên nước | 0:24 |
| 31:14 | 228 | ĐỊCH | Không lùi | 0:08 |
| 31:22 | 229 | SỐ | "마지막 탄창" | 0:08 |
| 31:30 | 230 | ACTION (im) | 300 kỵ lội mô cát — 백성민 dẫn | 0:08 |
| 31:46 | 232 | ACTION | Đánh lưng Tiên Ti | 0:16 |
| 32:02 | 234 | CHI PHÍ | 해모루 ngã | 0:16 |
| 32:18 | 236 | [史→虛] | 우중문 ngã ngựa | 0:16 |
| 32:26 | 237 | REVERSAL sử | Bắt sống | 0:08 |
| 32:42 | 239 | SỬ-QUYẾT | 우문술 "…가게 두어라." | 0:16 |
| 32:58 | 241 | SỐ | Súng hết → lưỡi lê | 0:16 |
| 33:14 | 243 | THREAT | 해모루 kéo cung — "안 됩니다" | 0:16 |
| 33:22 | 244 | PAYOFF | "그는 마침내 천둥 위에 섰습니다." | 0:08 |
| 33:30 | 245 | THREAT | Trong xe: lửa trắng, không gì để lấy — giương cung | 0:08 |
| 33:38 | 246 | CHI PHÍ | "철컥" | 0:08 |
| 33:46 | 247 | SỐ (quote) | "탄창 비었습니다." | 0:08 |
| 33:54 | 248 | ACTION | Mũi tên 해모루 | 0:08 |
| 34:02 | 249 | PAYOFF | 탁발흠 rơi; 태극기 태오 trôi | 0:08 |
| 34:10 | 250 | KẾT | Nắng xé mây; Goguryeo reo, đại đội không | 0:08 |
| 34:18 | 251 | OPEN LOOP | "강은 다시 흐르기 시작했습니다." | 0:08 |
| 34:30 | 252 | [史] SỐ | 2.700 · 450리 · 왕인공 · 내호아 | 0:12 |
| 34:42 | 253 | SỐ | 80 · 11 nằm · 20 thương | 0:12 |
| 34:50 | 254 | CHI PHÍ | 14 miếng 태극기 trong túi | 0:08 |
| 34:58 | 255 | SỐ | Morphine 8 → ống đầu tiên cho 해모루 | 0:08 |
| 35:06 | 256 | PAYOFF | "마개는… 아직 서 있소?" | 0:08 |
| 35:14 | 257 | SỐ | "붕대 마지막이에요." | 0:08 |
| 35:22 | 258 | CHI PHÍ | "다리는 붙어 있습니다. 전차는 없습니다." | 0:08 |
| 35:40 | 260 | PAYOFF 2화 | 을지문덕 không chạm — "대답을 보았습니다" | 0:18 |
| 35:48 | 261 | QUOTE | "그대들이 마개였소." | 0:08 |
| 35:56 | 262 | CẢM XÚC | 경례 — ông gật một cái | 0:08 |
| 36:04 | 263 | REVEAL rẽ sử | "역사에서 우중문은 달아났습니다. 오늘은…" | 0:08 |
| 36:12 | 264 | SỬ-QUYẾT | Bát nước — "족함을 알라 했소" | 0:08 |
| 36:28 | 266 | [史] | Tin tới 육합성 | 0:16 |
| 36:38 | 267 | [史] | Xiềng 우문술 | 0:10 |
| 36:54 | 269 | REVEAL | "…고구려 손에 있습니다. 살아서." | 0:16 |
| 37:02 | 270 | ĐỊCH/công nghệ | K21 + hộp drone ở 육합성 | 0:08 |
| 37:12 | 271 | SỬ-QUYẾT | 양제 chạm K21: "…내년." | 0:10 |
| 37:20 | 272 | OPEN LOOP | "내년." | 0:08 |
| 37:30–37:50 | 273–275 | [史] ×3 | Rút cuối 7월 · 613 양현감 · 618 우문화급 | ≤0:10 |
| 38:00 | 276 | POLITICS | "여든 명의 농부" | 0:10 |
| 38:08 | 277 | XUNG ĐỘT | "과인은 무엇을 얻었는가." | 0:08 |
| 38:16 | 278 | OPEN LOOP series | "내년에 또 올 것이오." | 0:08 |
| 38:24 | 279 | SỬ-QUYẾT (hoãn) | "내년에 다시 묻겠다." | 0:08 |
| 38:32 | 280 | REVEAL | Hai người không bao giờ gặp | 0:08 |
| 38:40 | 281 | REVEAL | Nước rút — xe nửa chìm cát | 0:08 |
| 38:48 | 282 | SỐ/PAYOFF | Biển 천둥 3 cạnh số 1 — "영입니다. 전부 영." | 0:08 |
| 38:56 | 283 | OPEN LOOP | "이제 우리는 뭡니까?" | 0:08 |
| 39:12 | 285 | PAYOFF thơ | 知足願云止 | 0:16 |
| 39:22 | 286 | OPEN LOOP series 2 | Xe bò về 낙양 3.000리 | 0:10 |
| 39:34 | 287 | OPEN LOOP | Hộp sơn mài — "날개는 남았습니다" | 0:12 |
| 39:52 | 289 | END | 「다음: 613」 + 1 hồi tù và | 0:18 |

**Kết quả:** ~170 beat / 40 phút (≈1 beat/14 s). **Khoảng cách lớn nhất mọi beat: 0:26** (22:22 → 22:48 và 14:08 khoảng trước) — dưới xa mục tiêu ≤4' và ngang kênh gốc. **Không action** dài nhất trong thân tập **3:50 (2:34 → 6:24, P2–P3 bàn cờ + kiểm kê)** — ≤4' nhưng sát biên; **aftermath 34:30 → 40:00 (5:30) không action** — chấp nhận theo P-47 nhưng nên đổi SC_252 thành video truy kích 압록 [史] (+8 s). Vùng mềm thứ hai: 37:30–38:00 ba still sử liên tiếp (30 s narration thuần) — chấp nhận cho khán giả 50+ (đọc sử), giữ nhịp ken-burns nhanh.

---
## 3. ≤10 ĐỀ XUẤT "HAY HƠN KÊNH GỐC" (xếp theo tác động; đòn bẩy: ①địch có tên ②hậu cần đếm ngược ③nhân vật lịch sử là bộ não ④chi phí thật ⑤open loop)

| # | SC | Sửa gì | Vì sao (đòn bẩy) |
|---|---|---|---|
| 1 | SC_222 (+SC_216) | **Biến Phase 3 thành SAI SÓT thật của 한승우:** N SC_222 → "그것이 그의 실수였습니다. 불보다 사람을 먼저 세었습니다. 넉 달 동안 그랬습니다. 그래서 그는 돌아갔습니다." SC_216 N bỏ "순서는 정해져 있었습니다" → "그는 순서를 정했습니다. 사람 먼저." | ④ Cái giá gắn vào *quyết định*, không vào vận rủi; đúng tính cách "94명 전원" (1화) → tập cuối chính điểm mạnh của ông suýt giết ông. Kênh gốc không có climax mà lỗi của phe ta có tên. |
| 2 | SC_188/197 + SC_206 | **Nước tắt máy, không phải người:** 박기철 nói giới hạn lội "도하 준비 없이 일 점 이 미터. 가슴이면 아슬아슬합니다." (P9) → Phase 1: K2 tới cổ họng, nước qua hút gió — **động cơ sặc, tắt** trước khi ông kịp bấm; 박기철 (intercom): "물이 껐습니다. 여울 목. 정지." | ② Giới hạn thật của K2 (story_bible §5.3) nói thành lời rồi trả ngay; sông = tướng (đúng "không đập nước": trời + sông thắng, không phải công nghệ). Vẫn giữ "300 m của 20 km". |
| 3 | SC_208 + SC_211 (2-BEAT) | **Trả 나각 3 hồi:** 해모루 thổi ba hồi khi K2 chắn khe → gò nam 을지문덕 **hạ kiếm** → kỵ Goguryeo toàn quân xuống (SC_185 có điều kiện, nay có cò). | ③ Bộ não lịch sử bấm nút *trên tín hiệu của đại đội* — hai kế lồng nhau nhìn thấy được; 5 s không thoại, không tăng SC. (Hiện tại là FIX vì payoff rơi.) |
| 4 | SC_270–271 | **양제 và cái xe đã ở đó 15 ngày:** xe bò 천둥 3 tới 육합성 từ trước (đúng bảng ngày 3화); ông **không chạm** — chờ "천둥 thật"; hôm nay tin thảm bại tới, ông đi ra mưa, chạm K21 lần đầu: "…내년." | ① Địch có tên & kiên nhẫn, không chỉ nổi giận; ⑤ series 2 mở bằng hành động (chạm) sau 15 ngày kìm. Sửa lỗi timeline "마흔 날" cùng lúc. |
| 5 | SC_252 | KB bản đồ 450리 → **video 8 s [史]**: kỵ Goguryeo truy kích tàn quân tới 압록수, 왕인공 chặn hậu; N giữ nguyên. | ④/③ Tổ tiên hoàn tất chiến thắng bằng chính họ (chủ đề 50+ #2); +8 s combat lấp 5:30 aftermath (P-47). |
| 6 | SC_182 · SC_276 | "그대들 쇠는 사람을 세우시오." / "**쇠를 거두면** 저들은 여든 명의 농부입니다." | Từ vựng "쇠" xuyên 5 tập = độ tin 사극 cho khán giả 50+; câu 고건무 5화 nối thẳng câu 4화 của ông ("쇠를 거두어야 합니다") → nhân vật nhất quán. (FIX★) |
| 7 | SC_060 · SC_245 | **Băng cẳng tay trái 탁발흠** (4화 백성민 chém) hiện ở SC_060; trên nóc xe SC_245 "cánh tay trái cầm cung — băng cũ — **run**" → mũi tên hắn chậm nửa nhịp = nửa nhịp 해모루 cần. | ① Mỗi bài học của địch có giá thật và giá ấy trả đúng lúc chết (4화 P4 → 5화 P10). Không thoại, 1 câu [ACTION]. |
| 8 | SC_002 · SC_004 | 2-BEAT: SC_002 (a) chân trong nước (b) mái khiên trên đầu; SC_004 (a) cờ cuộn, dây chưa cởi (b) mặt 을지문덕 → **8 shot/30 s**. | Hook không giải thích của kênh gốc là mật độ hình (13/30 s); ta 6 → 8 rẻ nhất có thể; đồng thời bỏ cận đám đông (§9). |
| 9 | SC_169 → giữa SC_164–165 | Tiếng K3 nam **tắt giữa hội đồng** quanh xe (sau "…전차를요?"), rồi mới tới KB nút bầu. | ② Đồng hồ tài nguyên đổ chuông *trong lúc* quyết định — phá cụm 80 s đứng nói; kênh gốc không bao giờ để 1 phút không hình động. |
| 10 | P10 Phase 1–3 (veo) | Two-beat thêm ~12 clip (SC_201/202/205/207/210/212/214/217/219/223/225/227) → shot hiệu dụng ~5,5 s; giữ 8 s trong Phase 4 im lặng. | Kênh gốc 4 s trong trận (#13); tương phản nhịp Phase 1–3 nhanh / Phase 4 chậm-im làm tổ tiên gánh phần cuối "nặng" hơn. Không đổi SC. |

---
## 4. Địa lý (kiểm theo trình tự di chuyển)
30만 5천 rút từ trại 30리 bắc **평양** → đi **bắc** → tới **살수 (청천강)** từ **bờ nam**, vượt sang **bờ bắc** ✓ (script: 방진 chạm mép nước bờ nam SC_005/049, lên bãi bắc qua cổng họng SC_051) · 을지문덕 theo sau từ 평양 → **gò nam** ✓ · kỵ Goguryeo có ở đồi bờ bắc phía đông (SC_071) — đi qua **mô cát thượng lưu 1,5 km về đông** (đường Goguryeo) ✓ · 탁발흠 2.000 kỵ ở **đồi bắc "từ hôm qua"** — hắn dẫn đầu cột về bắc (4화 SC_284) và xin "여울 북쪽" (4화 SC_263) → kỵ qua ford trước bộ ✓ (chấp nhận; 4화 còn hậu quân 5천 giữ bãi cạn bờ nam — 5화 không nhắc, không mâu thuẫn) · tàn quân chạy **450리 lên 압록수** (bắc) ✓, bản đồ SC_252 "살수 dưới, 압록수 trên" ✓ · tin tới **육합성 bên 요동성** (tây-bắc) sau 5 ngày ✓ · 천둥 3 từ **bờ tây 압록** (3화 P-40) về 요동 → **đã tới trước 5화** (FIX SC_270) · **평양** (nam) — 대동강 nhìn từ điện ✓ · 낙양 "삼천 리" về tây ✓ · 내호아 rút ra biển 해포 ✓ · 613 요동성, 614 비사성 (chỉ narrator), 618 강도 ✓. **Không địa danh thật nào sai trình tự.** Sub-địa hình LOC_007 (cổng họng 60 m · mô cát nhỏ 30 m · mô cát thượng lưu 1,5 km · bãi cát bắc → đồi) nhất quán trong 269 SC; cần world-designer ghi vào location_bible (P-41).

## 5. Điểm cần coordinator quyết (★)
1. **VEH_205 (BLOCK):** xóa khỏi 21 header + có tạo VEH_207 「수 장군 기마」 không (vehicle_bible + 1 ref job)?
2. **SC_057 dầu:** (A) giữ "이십 킬로" + 4 어절 "산길 기준, 박기철의 셈이었습니다" (đề nghị) hay (B) "십칠 킬로" ở 5 SC (đổi quote ★ outline P3/P8).
3. **"총" → "쇠"** ở SC_276 (quote outline P12 "총이 없으면…") — đề nghị "쇠를 거두면 저들은 여든 명의 농부입니다."
4. **신세웅:** giữ tên ở SC_091 (chết, [史]) + có giữ lần 2 ở SC_266 (tấu lên 양제) không? Decision P-44 nói 1 dòng.
5. **Phase 3 "sai sót"** (§3 #1) và **nước tắt máy** (§3 #2): sửa 2–3 câu N/thoại — có duyệt cho vòng v2 không?
6. **SC_252 → video truy kích 압록 [史]** (P-47, §3 #5): +8 s combat trong aftermath, không đổi SC.
7. Bible/ledger v3 gom sau QC 5 tập: PROP_024 (붉은 신호기) · PROP_025 (thermite) · PROP nút bầu (P-43) · `CHAR_205_night_hunt_ep4` "right" → "left forearm" · `CHAR_205_final_ep5` bow slung (P-39) · story_bible §3 우중문 "옥에 갇혔다가 병들어 죽음" · ledger 5화 cuối theo P-40.
