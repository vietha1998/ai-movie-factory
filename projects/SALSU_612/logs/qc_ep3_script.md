# QC — 3화 「남하」 full_script_ep3.md (v1, 287 SC, 40:00) · qc-reviewer · 2026-09-16

> Đối chiếu: QC_BRIEF v1 · SCRIPT_BRIEF v1 (checklist 1화) · series_foundation §4/§5/§7/§8/§8b/§9/§10 · outline_ep3 · story_bible §1 (612 6월 [史]) + quy tắc 시호 · character_bible (giọng, derived 3화) · location_bible LOC_005/008/009 · vehicle_bible · resource_ledger v2 · decisions (mục 3화: PZF 2+1, 천둥 3 không vượt 압록, 양제 1 SC, timeline D1–D17 chuẩn) · proposals P-38…P-51 (ep3) · channel style §4/§10/§11/§17/§19b/§20 · **full_script_ep2 v1 header + phụ lục** (nối tiếp: K2 12 · dầu K2 "삼백"/gom "사백" · cối 60 · PZF 12 · 40mm 220 · drone 2 · K21 2 (천둥 2, 3) · phuy 1 · kháng sinh 0 · quân số 94 · 을지문덕 đã gặp · lệnh nam hạ).
> Đếm thật từ file (`logs/scratch/qc-ep3/analyze.py`): **287 SC (241 video8s + 46 still 8/10/12 s) = 2.400 s, 0 khoảng trống** · thoại **138 câu / 674 어절**, dài nhất 11 어절, 0 SC >1 câu · narration **251 dòng / 1.015 câu / 4.421 어절**, 0 câu >15 · narrator vào **0:32** · 0–30 s **6 shot** · combat **724 s khối = 30,2 %** (script tự đếm 740) / **520 s thuần = 21,7 %** · mid-roll 7:00/14:00/21:00/27:30 + SC không thoại sau mỗi điểm ✓ · 12/12 open loop đúng câu outline ✓ · 5/5 DIRECT QUOTES nguyên văn ✓.
> Tổng: **BLOCK 1 · FIX 20 (3 ★ cần coordinator/outline) · NOTE 25**. Không sửa full_script.

## 0. Kết luận nhanh
- Nối tiếp 2화 **đúng hết số đầu tập**: PZF 12→10 (SC_006 "남은 것은 열 발"), K2 12 (SC_056/227), cối 60→50, 40mm 220 = 160 nổ trong 천둥 2 + 60 trong 천둥 3, drone 2→1→0, phuy 1 lên đuôi K2, kháng sinh 0 (SC_119), 94 người (SC_012), 해모루 chưa có radio tới P6, 탁발흠 "뒤를 밟는다" → SC_007 "이틀 전 산으로". Ràng buộc cứng outline đạt: 천둥 3 nguyên vẹn → 탁발흠 · 태오 bị bắt + drone + 2 kính · 1 KIA không tên · K2 12→8 · "산 채로 잡아라" · kết "숨으시오".
- **Ba lỗi nặng nhất:** (1) **BLOCK SC_130** — bài học then chốt của 탁발흠 ("새는 수레에 앉아 밥을 먹고, 밤눈을 가진 자들은 그때 가만히 있소") được narrator gắn vào "3 ngày quan sát bên kia 압록수" — cảnh không tồn tại: đại đội tới 압록 D9, 탁발흠 tới đuôi cột quân D10, drone không hề sạc trên K2 ở 압록, K2 giấu dưới thông bờ nam. Chỗ hắn thực sự thấy là **thung lũng 요동성 (2화, 12 ngày rình)** → đổi 1 câu N + 1 dòng [ACTION]. (2) **FIX★ SC_070/078** — 우중문 nghe loạt K6 và "báo là sấm Goguryeo": ông ta đã ngồi trong 육합성 nghe 양제 nói "뇌군도 남쪽으로 갈 것이다" (2화 SC_262); ai-biết-gì lệch; sửa thành 우중문 *nhận ra* 뇌군 ở bờ bên kia → động cơ vượt sông mạnh hơn (đòn bẩy ①). (3) **FIX SC_015/034/042** — tốc độ & dầu không khớp nhau: "hàng ngày 30리, bằng đại quân" nhưng đại quân tới 압록 300 km ở D9 (≈70리/ngày); "400km 딱" nói ở D3 sau khi đã chạy 30 km trong khi 2화 gom được "사백".
- **Benchmark:** hơn kênh gốc ở #7 (≈30 câu thoại có số), #8 (≈60 SC địch, 탁발흠 học 7 lần), #9 (5 người sử thật ra 10 quyết định), #12 (≥14 quote), #16 (6/6 kể cả "để 30 vạn đi qua"). **Thua:** #5 combat 30,2 % khối / 21,7 % thuần (gốc 45 %, mục tiêu 35 %); #6 **4:32 không có phát súng/mũi tên nào (21:26→25:58)** — chỉ có beat "30 cung giương trên 3 척후" (23:36) đỡ; #13 shot trận 8,08 s (gốc 4 s); #2 6 shot/30 s (gốc 13).
- **Rủi ro sản xuất:** narration + thoại = **5.095 어절 / 40' = 127 어절/phút** (2화: 114; TTS Hàn tự nhiên 100–120); P7 159, P3/P8/P9 151; 154/287 SC >2,2 어절/s, đỉnh SC_162/130/056/137 (35 어절 trong 8 s ≈ 17 s đọc). Editor không nhét được → FIX cắt ~570 어절.

---
## 1. BẢNG LỖI

| Mức | SC / dòng | Vấn đề | Đề xuất sửa cụ thể |
|---|---|---|---|
| **BLOCK** | SC_130 (N + [ACTION]) · tóm tắt P7 · SC_143 N | **Bài học then chốt của địch dựa trên cảnh không có.** N: "압록수에서 그는 강 건너를 사흘 동안 보았습니다. 쇠새가 쇠수레 등에 내려앉으면 한참을 있었습니다… 그때 밤눈을 가진 자들은 수레 곁을 떠나지 않았습니다." Theo chính script: đại đội tới 압록 rạng sáng D9 (SC_051–052), 탁발흠 ở **đuôi cột quân bờ tây** tới D10 (SC_096 "맨 끝"), drone chỉ bay 1 lần từ tay 태오 (SC_053/072), **không sạc trên K2** ở 압록 (K2 tắt máy dưới thông, SC_056/069), 3 ngày quan sát không tồn tại. Veo-stage sẽ phải dựng cảnh không có. Chỗ hắn thấy thật là **thung lũng 요동성, 12 ngày rình (2화 D33–D45)**: drone sạc "trên lưng xe" (K151/máy phát), 6 kính đêm gác cạnh xe. | [ACTION] SC_130: "…nhìn về phía **tây — nơi 요동성, nơi hắn đã nằm 12 ngày trên sườn nhìn xuống thung lũng**"; N: **"요동성 골짜기 위에서 그는 열이틀을 보았습니다. 쇠새가 수레 등에 내려앉으면 한참을 있었습니다. 밥을 먹는 것이었습니다. 그때 밤눈을 가진 자들은 수레 곁을 떠나지 않았습니다."** Thoại giữ nguyên. SC_143 N: "탁발흠이 **요동성 골짜기에서** 본 것이 바로 이것이었습니다." Tóm tắt P7: "Hắn đã thấy ở 요동성". |
| FIX★ | SC_070 N · SC_078 N (+ outline P4 "Enemy adaptation: — Tùy chưa biết") | **Ai biết gì lệch giữa 2화 và 3화.** 2화 SC_262: 양제 nói trước 우중문/우문술 "뇌군도 남쪽으로 갈 것이다. 탁발흠은 따라붙어라." Vậy 우중문 biết (a) có 뇌군, (b) nó đi nam. 3화 SC_070: kỵ Tùy báo K6 là "고구려의 천둥" và N/tóm tắt P4 nói "Tùy chưa biết đại đội ở đây". "천둥" chính là tên hiệu địch đặt cho đại đội (1화 P12) → 우중문 không thể không nhận ra. SC_129 (D10 đêm) lại có "수나라 총관은 뇌군이 어디로 갔는지 물었습니다" — tự mâu thuẫn trong tập. | Cho địch **nhận ra** (hay hơn kênh gốc: địch có mục tiêu tên): SC_070 N: **"육십 발이 물에 들어갔습니다. 수나라 기병은 총을 몰랐습니다. 그러나 천둥이라는 말은 알았습니다. 뇌군이 강 건너에 있다고, 그들은 그날 저녁 보고했습니다."** SC_078 N thêm 1 câu: **"우중문에게는 이유가 하나 더 있었습니다. 황제가 찾는 천둥이 강 건너에 있었습니다."** → quyết định vượt sông của 우중문 có thêm động cơ [虚] hợp sử (story_bible 4화 "우중문 sợ tiếng K2"). Đổi outline P4 dòng "Enemy adaptation" → "Tùy biết 뇌군 ở bờ nam; chưa biết ở đâu". |
| FIX★ | SC_034 · SC_042 N (+ ledger K2 dầu 2화/3화) | **Dầu 400 ở D3 sau khi đã chạy 30 km.** 2화 SC_273 "전차에 삼백. 나머지 다 짜면 사백" (D75). 3화 D1–D3 K2 bò 30 km đường núi (SC_015, SC_042 "사백 킬로 중 삼십을 온 참"), rồi 박기철 nói "산길로 400km, 딱" (D3). Hoặc gom được >400, hoặc còn 370. Câu N SC_042 nói cả hai ("400 trong đó đã đi 30" = còn 370) nhưng P-50 và toàn bộ hạch toán sau (−300 −3 −~80 → ~20 cho 4화 "연료 20km") tính từ **400 tại D3**. | Giữ 400 tại D3 (để 4화 "20km" đứng vững) và sửa 1 câu N SC_042: bỏ "사백 킬로 중 삼십을 온 참이었습니다" → **"골짜기에서 여기까지 삼십 킬로. 전차는 그 삼십을 사람 걸음으로 왔습니다. 남은 기름은 사백, 딱이었습니다."** Ledger ghi: gom thực tế ≈ 430 km-tương-đương (2화 "다 짜면 사백" là ước tính của 박기철 trước khi hút). Phương án B (không khuyên): "산길로 삼백칠십. 딱." + đổi 압록 = 270 km, "하루 오십". |
| FIX★ | SC_015 N (+ SC_012, SC_097) | **Tốc độ hai cột.** SC_015: "하루에 삼십 리. 벌판의 대군과 같은 속도였습니다." Nhưng đại quân đi D-1 và tới bờ tây 압록 (300 km theo SC_042) ở D9 → ≈27 km/ngày ≈ **70리**, đúng bằng tốc độ bò kéo 천둥 3 "하루에 칠십 리… 대열을 따라왔습니다" (SC_097). Đại đội đi bộ 12 km/ngày chỉ bằng **nửa** đại quân — đó mới là lý do phải đổi ngựa (P3). | SC_015 N: **"하루에 삼십 리. 벌판의 대군은 그 두 배를 갔습니다. 짐은 무거웠고, 매는 더 무서웠습니다."** (3 câu ≤15). Ghi story_bible: tốc độ 9군 ≈ 70리/ngày (300 km/11 ngày). |
| FIX | SC_005 N | "**넉 달** 만에 처음으로" — đại đội tới đất Goguryeo 3월 하순 (2화 header: D25 = 4월 중순); 3화 D1 = 2화 D77 ≈ 6월 17 → chưa tới 3 tháng. | **"석 달 만에 처음으로, 이 부대는 적이 아니라 자기 것을 태우고 있었습니다."** (SC_132 "넉 달째" của 양제 tính từ 3월 vây thành → chấp nhận.) |
| FIX | SC_022 [ACTION] ↔ SC_046 N | 해모루 "cười khẽ" ở SC_022 (D2) nhưng SC_046 N: "해모루가 **처음으로** 웃었습니다. 요동성에서도, 벌판에서도 웃지 않던 사람이었습니다." (D4). Lời hứa "lần đầu trong ba tập" là beat đắt — bị chính SC_022 phá. | SC_022 [ACTION]: "vệt máu trên lưỡi đao, **gật một cái**, quay ngựa đi không nói." |
| FIX | SC_039 N | "을보는 **이 쇠수레**의 바퀴에 쇠못을 박은 사람이었습니다. 그가 고친 장갑차는 골짜기에 남았습니다. 그 사실을 그는 아직 몰랐습니다." — ông đang gõ lên K2 (không phải xe ông chốt); và ông **có mặt** lúc 천둥 3 bị bỏ lại (SC_010), nên "chưa biết" sai. | **"을보는 골짜기에 남은 장갑차의 바퀴에 쇠못을 박은 사람이었습니다. 그 장갑차가 누구 손에 들어갈지, 그는 아직 몰랐습니다."** — gieo SC_096 ("우리 찹니다") cho cả ông. |
| FIX (sử mềm) | SC_054 N | "남은 것마저 강에 던졌습니다… **수나라 역사책은 이 장면도 적어 두었습니다.**" — 삼국사기/수서 chỉ ghi **chôn dưới lều** (掘坑埋之) và "tới giữa đường lương gần hết"; "ném xuống 압록수" là dựng thêm của foundation/outline ([虚] chấp nhận), nhưng gắn "sử ghi" vào là overclaim — khán giả 50+ đọc 삼국사기 sẽ soi. | **"역사책이 적은 것은 묻은 것이었습니다. 던진 것은 적지 않았습니다. 강은 흔적을 남기지 않습니다."** |
| FIX (sử mềm) | SC_099 N · SC_268 N · SC_275 N | **"하루 일곱 번"** là 4화 P2 (story_bible: sau khi vượt 압록, trước khi vượt 살수 — montage 7 trận/ngày). 3화 đã: SC_099 "그 일곱 번의 첫 번째가 이 강가였습니다" (D10), SC_268 "을지문덕은 그들 앞에서 하루에 일곱 번 졌습니다. 일곱 번 다 뜻대로 졌습니다." (D16, thì quá khứ = đã xong), SC_275 "그 사이에 세 번 더 졌습니다" (D17) → 4화 kể lại lần nữa thành lặp; và 7+3 ≠ 7. Thêm: SC_099 "삼국사기는 이렇게 **적습니다**" vs SC_055 "적었습니다". | SC_099: **"삼국사기는 이렇게 적었습니다. 하루에 일곱 번 싸워 일곱 번 졌다. 그 일곱 번은 아직 오지 않았습니다. 이 강가는 그 첫 연습이었습니다."** SC_268: **"을지문덕은 그들 앞에서 지기 시작했습니다. 하루에 일곱 번 지는 날이 올 것이었습니다."** SC_275 giữ "세 번 더 졌습니다" (đếm riêng trước 7 trận). |
| FIX (timeline) | SC_109 N · SC_116 N · SC_118 N · SC_192 N · SC_262 N | 5 mốc tương đối lệch bảng ngày/đêm header: (a) SC_109 "**사흘 전부터** 두 사람은 말 없이도 통했습니다" — 백성민 được 해모루 gọi tên từ D4 (SC_047), P6 là D11 = 7 ngày; (b) SC_116 "이것도 **사흘 사이에** 배운 것" — bài "không dùng súng" học D2 (SC_022) → 9 ngày; (c) SC_118 "박기철은 **이틀 뒤에야** 계기판에서 읽게 됩니다" — rò nước là D12 = hôm sau; (d) SC_192 "그 세 바늘은 **이틀을** 버틸 것이었습니다" + SC_262 "**사흘 전에** 세 바늘로 꿰맨 깃발" — khâu D14 chiều, giật D15 đêm = ~30 giờ. | (a) **"말을 바꿔 탄 날부터 두 사람은 말 없이도 통했습니다."** (b) **"이것도 산길에서 배운 것이었습니다."** (c) **"그날 밤 그가 읽은 것을, 박기철은 이튿날 계기판에서 읽었습니다."** (d) SC_192 **"그 세 바늘은 하루를 버틸 것이었습니다."** · SC_262 **"어제 세 바늘로 꿰맨 깃발이었습니다."** → script-writer chạy grep mọi "X일/이틀/사흘/닷새/전/뒤" đối chiếu bảng D trước khi nộp (lessons L-18). |
| FIX (timeline/hướng) | SC_170 [ACTION] + N (↔ SC_145–147, SC_177) | Phân ngựa trên đường dê lúc **trưa D12** "반나절 전" được giải là của 3 척후 해모루 ("보냈소. 셋이오" — đã gửi). Nhưng SC_170 (**đêm D12**) cho 3 척후 "dắt ngựa đi chậm **lên** dốc" → họ chưa lên trước trưa, phân ngựa trưa không thể là của họ; D13 họ "về báo không có ai" (SC_177) → phải là lượt **xuống/về**. | [ACTION] SC_170: "ba 척후 Goguryeo dắt ngựa **đi xuống dốc, trên đường về**, cung đeo lưng, thở phào"; N: **"해모루의 척후 셋이 염소 길을 내려왔습니다. 위에는 아무도 없었다고, 그들은 믿었습니다. 그들 머리 위에 활 서른 개가 있었습니다. 탁발흠은 손을 내렸습니다."** (câu "죽은 척후는…" giữ). |
| FIX (đăng ký) | SC_111 한승우 | "이걸로 부르**시오**." — 하오체; character_bible 한승우: với Goguryeo **하십시오체** (tiền lệ 2화 P-43: "말객님, 이게… 몇 번째입니까?"). Câu outline nhưng không thuộc 5 DIRECT QUOTES. | **"이걸로 부르십시오."** (SC_159 "장군은… 부르셨다" — đúng, giữ.) |
| FIX (đăng ký) | SC_066 우중문 | "사람을 보내**시오**. 더 할 말이 있다 하**시오**." — nói với sĩ quan kỵ binh quỳ nhận lệnh; bible: 하오체 với tướng ngang hàng, thuộc hạ → 하라체. | **"사람을 보내라. 더 할 말이 있다 하라."** (SC_060 "…오지 않았는가", SC_085 "을지 놈이 왔다! 쫓아라!" đúng, giữ.) |
| FIX (số/đơn vị) | SC_112 N · SC_256 N · SC_274 N | Radio "닿는 거리는 **십 리**" = 4 km; 1화 SC_026 "10 km", foundation EQP_002 5–10 km; narrator dùng km ở mọi chỗ khác ("삼백 킬로", "십이 킬로"). | SC_112 **"닿는 거리는 십 킬로. 산이 막으면 그보다 짧았습니다."** · SC_256 **"말하는 돌은 십 킬로까지 닿았습니다. 십 킬로 뒤에 그는 다시 혼자였습니다."** · SC_274 **"십 킬로 안이었습니다."** |
| FIX (số có nguồn) | SC_162 N + 태오 | "**충전 한 번 남았습니다**" — khán giả vừa được dạy "1 lần sạc = 600 m" và còn ~100 km sau 압록 → 160 lần sạc; "còn một lần" đọc như **kho** thì sai, phải là **ngân sách** 한승우 cấp. N hiện tại "그 드론을 채울 전기는 한 번" không nói ai quyết. | N: **"숫자는 이랬습니다. 드론 하나. 한승우가 그 드론에 허락한 전기는 한 번. 나머지 기름은 살수까지의 길이었습니다. 야시경 열두 개, 전지 사십 퍼센트. 기름을 아끼느라 반만 채운 전지였습니다."** 태오: **"드론 하나. 허락된 충전 한 번. 야시경 배터리 40%."** (7 어절; ledger 3화 ★ giữ ý). |
| FIX (realism/cựu binh) | SC_182 N · SC_183 N + 박기철 · SC_215 N + 박기철 (SC_143 giữ) | Tiền đề trận: "잠든 전차는 쏘지 못합니다. 시동에는 시간이 걸립니다" / "시동을 걸면 밥은 끊깁니다" / "충전 중입니다! 이 분!". **APU của K2 tồn tại chính để nuôi pháo/điều khiển hỏa lực khi tắt máy**; nổ máy chính không cắt sạc mà sạc mạnh hơn; K2 nổ máy < 1 phút. Khán giả 50+ có cựu binh tăng-thiết giáp. Ràng buộc kịch (xe "ngủ" 40 phút) vẫn giữ được nếu **cột nó vào dây**: 7 kính + drone + 4 radio cắm vào ổ đuôi xe, dây chằng qua sân; giật dây sớm = mất chu kỳ sạc; tháp không xoay khi ổ ngoài đang kéo tải. | SC_182 N: "…그 마흔 분 동안 전차는 시동을 끄고 보조동력만 돌립니다. **포탑은 줄에 묶입니다.**" · SC_183 N: **"줄에 묶인 전차는 쏘지 못합니다. 줄을 뽑고 포탑을 살리는 데 시간이 걸립니다. 박기철은 그 시간을 알았습니다."** 박기철: **"마흔 분. 그 사이 전차는 줄에 묶입니다."** · SC_215 N: **"이 분. 야시경 일곱 개가 아직 밥을 먹고 있었습니다. 줄을 뽑으면 밥은 끊깁니다. 박기철은 이 분을 달라고 했습니다. 이 분은 그날 밤 가장 비싼 시간이었습니다."** 박기철: **"충전 중입니다! 줄 뽑는 데 이 분!"** (SC_226 "줄을 뽑았습니다 → 됐다! 시동!" đã khớp). vehicle_bible K2 thêm dòng "engine off + APU: pháo/FCS vẫn dùng được; cấm dùng lý do 'ngủ = không bắn'". |
| FIX (hình) | SC_139 [ACTION] | 8 s chứa: K2 lết lên làng + 2 척후 trên gờ bắn 2 tên lửa + tên cắm cành thông + 아리 giật khăn dập lửa liên tiếp + 을보 quát + lính bắn loạt lên gờ + 1 bóng ngã + bóng kia biến. Không quay được 1 clip. | 2-BEAT: (a) 0–4 s low-angle: hai mũi tên lửa rít từ gờ đá, một mũi cắm vào cành thông trên nóc K2, nhựa thông bén lửa; (b) 4–8 s cận đuôi xe: 아리 giật khăn olive đập lửa, 을보 quát "아리야! 내려와!". Loạt K2C1 + bóng ngã → [SOUND] off-screen; N giữ. (SC_010 tương tự: K2 ra khe + tên cắm bùn + loạt bắn + chạy → 2-BEAT.) |
| FIX (hình) | SC_105–108, SC_110–113 (lều 을지문덕, 14:22–15:58) | Hai cụm **4 SC liên tiếp đứng nói** trong lều (chỉ 1 insert tay SC_104, 1 insert ngoài lều SC_109 ở giữa) — checklist ≤2. | Không đổi số SC: SC_103 을지문덕 **đặt một quân cờ đen lên bản đồ ở 살수** khi nói; SC_107 오태민 bước tới bản đồ, ngón tay ấn lên cột quân Tùy (walk-in); dời SC_109 (백성민 ra cổng) vào **giữa SC_106 và SC_107**; SC_113 을지문덕 **đặt quân cờ thứ hai cạnh quân đầu** — hình hóa N "그의 판에 말이 하나 더 놓였습니다". |
| FIX (bible) | SC_262 N | "그는 요하에서 화살촉을 목에 걸었습니다. 이번에는 깃발이었습니다." — character_bible: đầu mũi tên Goguryeo trên dây da là **chiến lợi phẩm cũ** (trước 1화); thứ hắn nhặt của đại đội là **băng đạn K2C1 rỗng treo thắt lưng (2화+)** — đã có trong derived state `CHAR_205_nvg_ep3`. | **"그는 요동성에서 빈 탄창을 허리에 찼습니다. 이번에는 깃발이었습니다. 그것은 이 이야기의 마지막 강까지 그의 품에 있을 것이었습니다."** |
| FIX (sản xuất — mật độ đọc) | Toàn tập; đỉnh: SC_162, 130, 056, 137, 133, 182, 063, 077, 121, 171, 018, 043, 097, 107, 117, 161, 177, 181, 215, 262, 007, 139, 157, 159, 014 | N + thoại = **5.095 어절 / 40' = 127 어절/phút** (2화 114 · 1화 v3 ~115; TTS Hàn giọng documentary 100–120). Theo phần: P7 **159**, P3/P8/P9 **151**, P2 148, P4/P6 139. 154/287 SC >2,2 어절/s; 25 SC ≥3,4 어절/s = 27–36 어절 trong clip 8 s (≈14–17 s đọc). Editor phải tràn N sang SC kế → rối "N trước/sau thoại". | Cắt N còn **≤3.850 어절** (−~570), giữ thoại: quy tắc mỗi video8s **≤2 câu N khi có thoại, ≤3 câu khi không**; cắt câu N thứ 3–5 ở 25 SC trên (danh sách + số liệu trong `logs/scratch/qc-ep3/`); ưu tiên P7 (−120), P9 (−100), P3/P8 (−80 mỗi phần), P2 (−60). Không đổi SC/thời gian/thoại. |
| FIX (radio) | SC_007 백성민 | "산길에 횃불. 선비 기병. 열 분 안에 옵니다." — báo cáo qua radio không danh gọi (checklist: "[người nghe], 여기는 [người gọi]"); là câu outline → giữ nguyên nội dung sau danh gọi. | **"지휘, 여기는 수색. 산길에 횃불. 선비 기병. 열 분 안에 옵니다."** (11 어절) |
| NOTE (realism) | SC_079 N (↔ SC_085) | "30만 5천 명이 압록수를 건넜습니다… **하루 종일 걸렸습니다**" — 305.000 người lội ngang ngực qua một bãi cạn trong 1 ngày ≈ 3,5 người/giây liên tục 24 h. | **"선봉은 하루 만에 건넜습니다. 아홉 군이 다 건너는 데는 사흘이 걸렸습니다."** — cũng hợp SC_085 (우중문 còn ở bờ tây lúc trận giả thua). |
| NOTE (hậu cần/hình) | SC_010, SC_033, SC_048, SC_194 → P10 | Phuy 200 L (đầy) nằm trên buồng động cơ K2 suốt tới trận đèo — tên lửa cắm cành thông nóc xe (SC_139), đêm đèo cung bắn trùm; không ai đổ phuy vào bình. Ledger ghi phuy = 0 cuối 3화. | SC_173 [ACTION] thêm: "phuy rỗng nằm nghiêng cạnh lò rèn"; 박기철 (SC_174) thêm 1 câu tùy chọn: **"드럼 비웠습니다. 이제 전차 배 속뿐입니다."** (6 어절) → đuôi xe P9–P10 chỉ còn hộp đạn/K6/cối. |
| NOTE (realism) | SC_017 N | "**반년 전에** 대학 시험을 봤습니다" — 태오 21 tuổi, 일병; 수능 lúc 18–19. | **"삼 년 전에 대학 시험을 봤습니다."** (hoặc "고등학교 때 외운 시"). |
| NOTE (hình) | SC_057 (KB) | "Ken-burns trượt theo **hàng mặt lính**" — foundation §9 "không cận cảnh đám đông". | Trung cảnh tracking, chỉ 2–3 khuôn mặt nét gần 을지문덕, hàng sau mờ. |
| NOTE (sử/nhãn) | SC_059 N ↔ SC_076 N | "우중문, 별동대 **총사령**" rồi "**두 총사령**이 마주 앉았습니다". Sử: 양제 lệnh các quân nghe 우중문 định đoạt (仲文有計畫 令諸軍諮稟節度) nhưng 우문술 đồng cấp. | SC_059: **"우중문. 아홉 군을 이끄는 두 총사령 중 하나. 황제는 결정을 그에게 맡겼습니다."** |
| NOTE (nối 2화) | P2 (SC_012–015) | 2화 SC_253: **2 lính bỏng nặng không cầm được súng** + 4 thương P10; 3화 hành quân 400 km không nhắc họ đi bằng gì. | SC_015 [ACTION] thêm: "hai lính băng kín tay đi giữa hàng, súng do người khác vác" (D2–D3), từ D4 lên ngựa như mọi người. |
| NOTE (logic địch) | SC_128–129 N | 탁발흠 (Tiên Ti, đất Liêu) biết "đường xe duy nhất phía nam 압록" — nguồn? 2화 hắn đã hỏi cung nông dân Goguryeo (SC_128 2화). | Thêm 1 câu N SC_128: **"남쪽 길은 요동성 앞에서 잡은 농부에게 미리 물어 두었습니다."** |
| NOTE (logic địch) | SC_007 ↔ SC_097 | D1 đêm hắn bám theo đại đội vào núi (10 phút sau lưng); D2–D10 lại đi cùng 40 bò kéo K21 trên đồng bằng. Chưa có câu nào nói hắn **chọn** bỏ dấu đại đội. Cộng thêm 70리 × 9 ngày ≈ 250 km < 300 km tới 압록 (SC_042). | SC_097 N thêm: **"그는 부대를 쫓지 않았습니다. 뇌군은 어차피 압록수로 올 것이었습니다."** · "하루에 칠십 리" → "하루에 팔십 리" hoặc chấp nhận làm tròn. |
| NOTE (realism) | SC_142 N · SC_173 [ACTION] | Vá ống cao su làm mát bằng "구리판… 송진과 **쇠못**으로 붙일 것" — đóng đinh sắt vào ống cao su chịu áp. | **"구리 관을 만들어 끼우고, 송진을 먹인 가죽끈으로 조일 것이었습니다."**; SC_173 "đóng chốt sắt" → "quấn dây da tẩm nhựa thông". |
| NOTE (logic) | SC_149 N | Hoàng hôn D12, K2 tắt máy (chỉ APU) mà hắn thấy "흰 연기. 쇠수레가 내는 연기" từ 5 km. Hơi nước chỉ có lúc leo dốc buổi sáng. | Hắn thấy **xe đứng bất động cạnh kho thóc, khói lò rèn không dứt** → N: "그가 본 것은 서 있는 쇠수레와 꺼지지 않는 대장간 연기였습니다." Câu "물을 마시고 있다" giữ (suy luận). |
| NOTE (thì) | ~29 câu N hiện tại (SC_035, 060, 065, 083, 116, 128, 155, 170, 176, 181…) · SC_121 | Đa số là châm ngôn ("죽은 척후는 돌아가지 않습니다") — chấp nhận theo quy ước 1화 v3. Lệch: SC_121 "그 길은 **다음 이야기에서** 사람 하나를 살립니다" (meta, hiện tại). | SC_121: **"그 길은 다음 이야기에서 사람 하나를 살릴 것이었습니다."** hoặc bỏ câu. |
| NOTE (radio) | SC_234 태오 | "**본부**, 본부… 잡혔—" — callsign trước đó "천둥 지휘" (SC_202/220). Là câu outline (+); hoảng loạn thì chấp nhận. | Nếu story-director đồng ý: "지휘, 지휘… 잡혔—". |
| NOTE (giọng N) | SC_251 N | "이름은 여기 적지 않**겠습니다**" — narrator ngôi thứ nhất/thì tương lai, lệch giọng documentary 격식체. | **"이름은 여기 적지 않습니다. 스물세 살. 강원도 어느 마을의 아들이었습니다."** |
| NOTE (foundation) | SC_132 (양제 1 SC) | Foundation §4: 양제 xuất hiện 1–2화, 5화; P-47 OPEN. QC ủng hộ giữ: nhân vật sử ra lệnh nhìn thấy được (đòn bẩy ③), 1 SC không phá cấu trúc. | Coordinator ghi foundation §4: "3화: 1 SC 육합성". |
| NOTE (ledger) | SC_003/006 (PZF 2 vào 천둥 2) · P-38 OPEN | Ledger/outline gốc: đốt xe bằng dầu + lựu đạn, PZF ×3 ở đèo; script theo brief user 2+1. Hình hook mạnh, nhưng PZF là tài nguyên series (5화 cần 6) và 천둥 2 đã rút cạn dầu — cửa đuôi mở + lựu đạn nhiệt nhôm là đủ. | Coordinator quyết P-38. Nếu giữ 2 quả: thêm phản ứng 1 câu cho 박기철 ở SC_003 [SOUND] off: "두 발…" để cái giá được nói ra. |
| NOTE (hình) | SC_124 (KB) | "ken-burns kết hợp **fade** đèn tắt" = 2 trạng thái trong 1 still. | Veo-stage: 2 still 5 s (đèn sáng → đèn tắt) hoặc video8s. |
| NOTE (veo-stage) | Toàn P4–P7 [ACTION]/header | Bờ 압록: script gọi phía Tùy "**bờ tây**", phía Goguryeo "**bờ nam**" (không đối nhau); location_bible LOC_005 dùng **bờ bắc (Tùy) / bờ nam (ta)**. | Thống nhất theo bible: "bờ bắc/bờ nam" trong ~20 header/[ACTION] (SC_054, 057, 067, 085, 096–101, 126–133, 264). |
| NOTE (hình) | SC_112 | 8 s: cầm radio, xoay, áp tai như vỏ ốc, 한승우 lấy lại, kẹp lên giáp, bấm PTT, 해모루 giật, cười — 7 động tác. | Cắt "xoay trong tay"; giữ áp tai → kẹp → PTT "칙" → cười. |
| NOTE (nhịp trận) | P10 (52 SC, 8,08 s; 2-BEAT chỉ 3 lần) | Kênh gốc 4 s/shot trong trận; outline hứa 4–6 s. | Veo-stage: đánh dấu 2-BEAT thêm ~12 clip Phase 2–4 (SC_208, 210, 211, 212, 216, 217, 221, 223, 225, 229, 231, 236) → shot hiệu dụng ~6 s. |
| NOTE (thống kê) | Phụ lục A | Script tự đếm combat khối 740 s; QC đếm 724 s (SC_198–206 setup tính vào khối là hào phóng); thuần 520 s ✓ khớp. SC/N/thoại ✓ khớp. | Ghi cả hai số trong benchmark; đặt chuẩn đếm "khối" = từ SC đe dọa vật lý đầu tiên đến SC hỏa lực cuối. |
| NOTE (retention) | 21:26 → 25:58 | **4:32 không có phát súng/mũi tên** (sau SC_153 tới SC_187); chỉ có beat đe dọa SC_170 (23:36, cung giương không bắn). Brief: không có khoảng >4′ không action. | Xem §3 #1 (biến SC_178 thành chạm trán của 소년 척후 — không tăng SC). |
| NOTE (payoff) | SC_168 (소년 척후 đi đông) | Gửi đi, không bao giờ về/không có hậu quả. | Gộp vào §3 #1. |
| NOTE (đăng ký, OK) | SC_146 백성민 "해모루, 여기는 수색" | Gọi tên trần — bible cho phép từ 3화 ("chỉ '해모루' được phép"); callsign do 해모루 tự xưng (SC_137). Không lỗi. | — |
| NOTE (sử, OK) | SC_267 우중문 "평양은 사흘 거리요" | Khoác lác (thật ~200 km); script-writer đã ghi. | Có thể thêm N: "사흘. 그의 셈이었습니다." |
| NOTE (bible) | Prop/derived cần ghi sau 3화 (P-49 đã liệt kê) | + mũ trống 태오 ở tay 한승우 (SC_245/248/285) · K3 KIA trên vai 오태민 · khăn 아리 cháy sém · miếng đồng K2 · mộ đá + mũ úp (LOC_009 aftermath) · **2 quân cờ trên bản đồ** nếu duyệt FIX lều · patch 태극기 trong áo giáp 탁발흠. | character/prop/vehicle-designer. |

---
## 2. BẢNG RETENTION (beat theo phút)

Ký hiệu: ACTION · REVEAL · SỐ · QUYẾT ĐỊNH · ĐỊCH (POV/thích nghi) · XUNG ĐỘT · THREAT · OPEN LOOP · CHI PHÍ · QUOTE. Δ = khoảng cách tới beat trước.

| Phút | SC | Loại | Beat | Δ |
|---|---|---|---|---|
| 0:03 | SC_001 | REVEAL | Dầu chảy vào can, lửa cam sau lưng | — |
| 0:16 | SC_003 | ACTION | 2 xe tải + K151 cháy; PZF vào xe mình | 0:13 |
| 0:24 | SC_004 | CHI PHÍ | 40mm nổ dây chuyền; tháo biển "3" | 0:08 |
| 0:40 | SC_006 | SỐ/XUNG ĐỘT | PZF 12→10; "정말 버립니까?" | 0:16 |
| 0:48 | SC_007 | THREAT | Đuốc Tiên Ti, 10 phút | 0:08 |
| 0:56 | SC_008 | QUYẾT ĐỊNH | "출발" — lựu đạn về túi | 0:08 |
| 1:04 | SC_009 | REVEAL sử | 30만 5천 · 백 일치 · 세 섬 | 0:08 |
| 1:14 | SC_010 | ACTION-lite | Tên cắm bùn sau gót | 0:10 |
| 1:22 | SC_011 | OPEN LOOP | "천둥 3호는 불타지 않았습니다" | 0:08 |
| 1:30 | SC_012 | REVEAL | Hai cột song song 20리 | 0:08 |
| 1:54 | SC_014 | REVEAL sử | Lính gục dưới 3석 | 0:24 |
| 2:10 | SC_016 | SỐ | "사백 킬로를 이 발로" | 0:16 |
| 2:18 | SC_017 | FORESHADOW | 4 câu thơ | 0:08 |
| 2:42 | SC_020 | THREAT | Kỵ Tùy thấy bụi K2 | 0:24 |
| 2:50 | SC_021 | ACTION | 30 kỵ 해모루 chặn khe | 0:08 |
| 2:58 | SC_022 | XUNG ĐỘT | "쏘지 마" — cấm #1 | 0:08 |
| 3:14 | SC_024 | REVEAL | Đào dưới lều (POV kính đêm) | 0:16 |
| 3:22 | SC_025 | QUOTE | "밥을 묻고 있습니다" | 0:08 |
| 3:56 | SC_029 | REVEAL | Điểm yếu = bụng | 0:34 |
| 4:12 | SC_031 | QUYẾT ĐỊNH | "안 친다. 압록수로 간다" | 0:16 |
| 4:40 | SC_034 | SỐ | "400km 딱" | 0:28 |
| 4:48 | SC_035 | SỐ GIẢM | Drone 2→1 (pin phồng) | 0:08 |
| 4:56 | SC_036 | QUOTE/SỐ | "600미터" | 0:08 |
| 5:12 | SC_038 | SỐ | "입이 둘" | 0:16 |
| 5:36 | SC_041 | CLOCK | "닷새" | 0:24 |
| 5:52 | SC_043 | QUYẾT ĐỊNH | Kỵ Goguryeo nhường ngựa | 0:16 |
| 6:00 | SC_044 | ACTION-lite | Lính đào ngũ bị quật | 0:08 |
| 6:16 | SC_046 | RELIEF | 오태민 rơi ngựa, 해모루 cười | 0:16 |
| 6:32 | SC_048 | SỐ | "전차가 노새" | 0:16 |
| 6:50 | SC_050 | OPEN LOOP | "닷새…" → MID-ROLL 1 | 0:18 |
| 7:12 | SC_052 | THREAT | "장군께서 직접 가시오" | 0:22 |
| 7:20 | SC_053 | SỐ | Drone cuối, 30 phút | 0:08 |
| 7:28 | SC_054 | REVEAL | Ném lương xuống sông | 0:08 |
| 7:36 | SC_055 | REVEAL sử | Cờ trắng — 詐降 | 0:08 |
| 7:44 | SC_056 | PLAN/SỐ | "정문에 네 발" | 0:08 |
| 8:02 | SC_058 | REVEAL | Nhai vỏ cây | 0:18 |
| 8:10 | SC_059 | THREAT | Mật chỉ bắt | 0:08 |
| 8:34 | SC_062 | THREAT | "붙잡으라는 밀지가 있소" | 0:24 |
| 8:42 | SC_063 | QUYẾT ĐỊNH sử | 유사룡 can | 0:08 |
| 9:06 | SC_066 | THREAT | 우중문 hối, đuổi | 0:24 |
| 9:14 | SC_067 | ACTION | 50 kỵ đuổi | 0:08 |
| 9:30 | SC_069 | QUYẾT ĐỊNH | "물에다 쏴" | 0:16 |
| 9:38 | SC_070 | ACTION | K6 xuống nước | 0:08 |
| 9:46 | SC_071 | PAYOFF sử | Không ngoảnh lại | 0:08 |
| 9:54 | SC_072 | SỐ GIẢM | Pin 30→14 | 0:08 |
| 10:12 | SC_074 | QUOTE | "굶는 군대는 이기게 두면 되오" | 0:18 |
| 10:30 | SC_076 | ĐỊCH | "군량이 없소" | 0:18 |
| 10:38 | SC_077 | ĐỊCH XUNG ĐỘT | Câu mắng [史] | 0:08 |
| 10:46 | SC_078 | QUYẾT ĐỊNH sử | 우문술 nhượng | 0:08 |
| 11:14 | SC_081 | QUOTE | "지되, 죽지는 마시오" | 0:28 |
| 11:22 | SC_082 | SỐ | Cối 10 viên | 0:08 |
| 11:30 | SC_083 | ACTION | 300 kỵ xung phong | 0:08 |
| 11:38 | SC_084 | CHI PHÍ | 1 kỵ Goguryeo ngã | 0:08 |
| 11:54 | SC_086 | REVERSAL | Cờ rơi cố ý | 0:16 |
| 12:10 | SC_088 | ACTION | Cối 10 viên (narrator im) | 0:16 |
| 12:34 | SC_091 | XUNG ĐỘT | "안 쏜다. 지는 중이다" — cấm #2 | 0:24 |
| 12:42 | SC_092 | ĐỊCH THÍCH NGHI | Giãn đội hình | 0:08 |
| 12:58 | SC_094 | SỐ GIẢM | 60→50 | 0:16 |
| 13:14 | SC_096 | REVEAL | "저건… 우리 찹니다" | 0:16 |
| 13:22 | SC_097 | ĐỊCH | 탁발흠 bên xe | 0:08 |
| 13:30 | SC_098 | SỐ | 60 viên 40mm trong xe | 0:08 |
| 13:48 | SC_100 | OPEN LOOP | Bò kéo K21 → MID-ROLL 2 | 0:18 |
| 14:22 | SC_103 | QUYẾT ĐỊNH sử | "살수로 먼저 가시오" | 0:34 |
| 14:38 | SC_105 | XUNG ĐỘT | "왜 거깁니까?" | 0:16 |
| 14:46 | SC_106 | OPEN LOOP | "이유는 그때 말하겠소" | 0:08 |
| 14:54 | SC_107 | XUNG ĐỘT | Cấm #3 | 0:08 |
| 15:02 | SC_108 | QUOTE | "이기고 있다고 믿어야 하오" | 0:08 |
| 15:18 | SC_110 | REVEAL | 해모루 cũng không biết | 0:16 |
| 15:26 | SC_111 | QUYẾT ĐỊNH | Trao radio (tin) | 0:08 |
| 15:34 | SC_112 | RELIEF | "말하는 돌이오?" | 0:08 |
| 15:58 | SC_115 | THREAT | 2 척후 Tùy | 0:24 |
| 16:06 | SC_116 | ACTION | Tên + dao, không súng | 0:08 |
| 16:14 | SC_117 | RED HERRING | "남쪽" | 0:08 |
| 16:22 | SC_118 | FORESHADOW | "이 쇠가 땀을 흘리네" | 0:08 |
| 16:38 | SC_120 | FORESHADOW | Mẹ 아리 quê 살수 | 0:16 |
| 16:54 | SC_122 | EMOTION | "왜 여기 있습니까?" | 0:16 |
| 17:02 | SC_123 | QUOTE | "몰라. 그래서 살아 있어야 해" | 0:08 |
| 17:20 | SC_125 | OPEN LOOP | "살수." | 0:18 |
| 17:30 | SC_126 | ĐỊCH | 탁발흠 chui vào 천둥 3 | 0:10 |
| 17:46 | SC_128 | ĐỊCH THÍCH NGHI | Bản đồ bùn → 석문령 | 0:16 |
| 17:56 | SC_129 | QUOTE | "쇠수레는 산을 못 넘소" | 0:08 |
| 18:04 | SC_130 | ĐỊCH THÍCH NGHI | Đánh lúc "chim ăn" | 0:08 |
| 18:12 | SC_131 | ĐỊCH THÍCH NGHI | Bịt tai ngựa | 0:08 |
| 18:20 | SC_132 | QUYẾT ĐỊNH sử | "산 채로 잡아라" | 0:08 |
| 18:28 | SC_133 | THREAT | 2.000 kỵ lên yên | 0:08 |
| 18:36 | SC_134 | PROBLEM | Rò nước làm mát | 0:08 |
| 18:44 | SC_135 | SỐ | "이틀은 세워야" | 0:08 |
| 18:52 | SC_136 | REVERSAL | "구리로 때우면 되지" | 0:08 |
| 19:00 | SC_137 | ACTION | Hậu vệ vs 척후; radio 해모루 | 0:08 |
| 19:16 | SC_139 | ACTION | Tên lửa lên nóc K2, 아리 dập | 0:16 |
| 19:32 | SC_141 | REVEAL | 석문령 lộ diện; "이틀" | 0:16 |
| 19:52 | SC_143 | FORESHADOW | "전차가 서야 얘가 밥을" | 0:20 |
| 20:00 | SC_144 | CLOCK | Cột Tùy 2 ngày | 0:08 |
| 20:08 | SC_145 | THREAT | Phân ngựa đường dê | 0:08 |
| 20:24 | SC_147 | RED HERRING | "보냈소. 셋이오" | 0:16 |
| 20:32 | SC_148 | SỐ | "전차 삼 킬로" | 0:08 |
| 20:40 | SC_149 | ĐỊCH | 탁발흠 nhìn làng | 0:08 |
| 20:48 | SC_150 | OPEN LOOP | "물을 마시고 있다" → MID-ROLL 3 | 0:08 |
| 21:10 | SC_152 | ACTION | Kỵ Tùy cướp ruộng | 0:22 |
| 21:18 | SC_153 | ACTION | 오태민 bắn đuổi | 0:08 |
| 21:26 | SC_154 | REVEAL | "굶은 겁니다" | 0:08 |
| 21:34 | SC_155 | DILEMMA | Vá hay bỏ | 0:08 |
| 21:50 | SC_157 | QUOTE | "소총 아흔 자루" | 0:16 |
| 22:06 | SC_159 | REVEAL | "무게가 필요해" | 0:16 |
| 22:14 | SC_160 | QUYẾT ĐỊNH | "고친다. 고개는 밤에" | 0:08 |
| 22:30 | SC_162 | SỐ | "충전 한 번 / 40%" | 0:16 |
| 22:38 | SC_163 | CHARACTER | "두 시간입니다. 명령입니다" | 0:08 |
| 23:28 | SC_169 | THREAT | Sương — kính đêm mù | 0:50 |
| 23:36 | SC_170 | THREAT | 30 cung trên 3 척후 | 0:08 |
| 23:44 | SC_171 | ĐỊCH THÍCH NGHI | "보내라. 아무도 없다고" | 0:08 |
| 23:52 | SC_172 | OPEN LOOP | Cùng nhìn một con đèo | 0:08 |
| 24:00 | SC_173 | REVERSAL | Vá xong | 0:08 |
| 24:18 | SC_175 | PLAN | Bàn cát | 0:18 |
| 24:36 | SC_177 | IRONY | Mũi tên cắm sai | 0:18 |
| 24:44 | SC_178 | THREAT | Mắt Tiên Ti trên vách | 0:08 |
| 25:00 | SC_180 | SỐ | "십 분. 마지막 비행" | 0:16 |
| 25:16 | SC_182 | SỐ | "마흔 분" | 0:16 |
| 25:24 | SC_183 | FORESHADOW | "전차는 잠듭니다" | 0:08 |
| 25:40 | SC_185 | QUYẾT ĐỊNH | "너는 전차 옆이다" | 0:16 |
| 25:58 | SC_187 | ACTION | 5 척후 cửa nam | 0:18 |
| 26:14 | SC_189 | IRONY | "역시 남쪽이다" | 0:16 |
| 26:22 | SC_190 | QUOTE | "너무 높다" | 0:08 |
| 26:38 | SC_192 | FORESHADOW | Khâu 태극기 | 0:16 |
| 26:46 | SC_193 | SETUP | "돌아올 몫 남겨" | 0:08 |
| 27:10 | SC_196 | REVEAL | Ải đá 598 | 0:24 |
| 27:20 | SC_197 | OPEN LOOP | "마흔 분…" → MID-ROLL 4 | 0:10 |
| 27:40 | SC_199 | CLOCK | Tắt máy | 0:20 |
| 28:04 | SC_202 | SỐ | Drone lên, 10 phút | 0:24 |
| 28:12 | SC_203 | IRONY | Đường dê trống | 0:08 |
| 28:36 | SC_206 | THREAT | Nhiệt không thấy sau vách | 0:24 |
| 28:44 | SC_207 | ACTION | Mũi tên đầu | 0:08 |
| 28:52 | SC_208 | ACTION | 2.000 đuốc | 0:08 |
| 29:08 | SC_210 | ACTION | 3 K3 | 0:16 |
| 29:16 | SC_211 | ĐỊCH THÍCH NGHI | Ngựa không hoảng | 0:08 |
| 29:32 | SC_213 | ĐỊCH THÍCH NGHI | Hắn nhìn mỏm đá | 0:16 |
| 29:48 | SC_215 | SỐ | "이 분!" | 0:16 |
| 29:56 | SC_216 | REVERSAL | Không vào K2 — lên mỏm | 0:08 |
| 30:04 | SC_217 | THREAT | Dây từ đỉnh vách | 0:08 |
| 30:12 | SC_218 | REVEAL | "목표는 태오다!" | 0:08 |
| 30:20 | SC_219 | IMAGE | Thấy chính mình bị vây | 0:08 |
| 30:44 | SC_222 | QUYẾT ĐỊNH | "백 중사, 바위로!" | 0:24 |
| 31:00 | SC_224 | ĐỊCH | "나는 위로 간다" | 0:16 |
| 31:16 | SC_226 | SỐ | 5 đầy, 2 còn 40 % | 0:16 |
| 31:32 | SC_228 | ACTION | K2 bắn (narrator im) | 0:16 |
| 31:48 | SC_230 | SỐ GIẢM | Đá lở; "잔탄 08" | 0:16 |
| 32:04 | SC_232 | SAI SÓT | Đá lở chặn lối lên mỏm | 0:16 |
| 32:12 | SC_233 | CHI PHÍ | KIA #1 | 0:08 |
| 32:20 | SC_234 | CHI PHÍ | "잡혔—" | 0:08 |
| 32:36 | SC_236 | SỐ GIẢM | PZF 10→9 | 0:16 |
| 32:44 | SC_237 | SỐ GIẢM | Kính đêm 백성민 tắt | 0:08 |
| 32:52 | SC_238 | SỐ GIẢM | Drone tự hạ — bị nhặt | 0:08 |
| 33:00 | SC_239 | ACTION | 해모루 bỏ nam, đánh cửa đông | 0:08 |
| 33:08 | SC_240 | ACTION | 개마무사 phá 200 kỵ | 0:08 |
| 33:16 | SC_241 | GROWTH | 오태민 không đuổi | 0:08 |
| 33:24 | SC_242 | CHI PHÍ | 6 thương | 0:08 |
| 33:40 | SC_244 | CHI PHÍ | Mỏm trống, mũ trống | 0:16 |
| 33:48 | SC_245 | REPORT | "태오… 없습니다. 사수 전사" | 0:08 |
| 34:04 | SC_247 | ĐỊCH | 탁발흠 với 태오 vắt yên | 0:16 |
| 34:20 | SC_249 | OPEN LOOP | "92명…" | 0:16 |
| 34:30 | SC_250 | CHI PHÍ | Chôn kiểu Goguryeo | 0:10 |
| 34:48 | SC_252 | XUNG ĐỘT | "그 이틀이 태오입니다" | 0:18 |
| 35:12 | SC_255 | SỐ | "야시경 열 개. 드론, 없습니다" | 0:24 |
| 35:30 | SC_257 | ĐỊCH THÍCH NGHI | Kính đêm lên mũ lông | 0:18 |
| 35:38 | SC_258 | IMAGE | POV xanh của địch | 0:08 |
| 35:46 | SC_259 | QUOTE | "밤이… 낮이 되었다" | 0:08 |
| 36:02 | SC_261 | CHARACTER | "모릅니다" | 0:16 |
| 36:10 | SC_262 | FORESHADOW | Giật 태극기 | 0:08 |
| 36:18 | SC_263 | QUYẾT ĐỊNH | "눈은 내가 갖는다" | 0:08 |
| 36:26 | SC_264 | ALTERED | K21 về tây | 0:08 |
| 36:36 | SC_265 | ĐỊCH | "뇌군은 살수로" | 0:10 |
| 36:52 | SC_267 | QUYẾT ĐỊNH sử | "건너오" | 0:16 |
| 37:10 | SC_269 | EMOTION | 태오 nhìn về nam | 0:18 |
| 37:20 | SC_270 | OPEN LOOP | "야시경은 보내지 않았습니다" | 0:10 |
| 37:30 | SC_271 | REVEAL | 살수 | 0:10 |
| 37:50 | SC_273 | PAYOFF | 아리 tìm lối lau | 0:20 |
| 38:06 | SC_275 | ARRIVAL | 해모루 2 đêm phi | 0:16 |
| 38:14 | SC_276 | OPEN LOOP | "숨으시오. 30만이 지나가게 두시오" | 0:08 |
| 38:32 | SC_278 | XUNG ĐỘT | "태오가 저기 있는데?!" | 0:18 |
| 38:48 | SC_280 | CLOCK | "물이 오르고 있습니다" | 0:16 |
| 39:04 | SC_282 | CLOCK | "사흘" | 0:16 |
| 39:22 | SC_284 | THREAT | 탁발흠 đang tới, kính đêm trên mũ | 0:18 |
| 39:32 | SC_285 | THEME | Sử không có 92 người | 0:10 |
| 39:42 | SC_286 | OPEN LOOP | Nước qua vạch dao | 0:10 |

**Kết quả:** ~175 beat / 40′ (≈1 beat / 14 s) — dày hơn 1화 (93). Khoảng cách lớn nhất tính mọi beat = **0:50** (22:38 → 23:28, ngủ/lò rèn). Beat MẠNH (action/reveal/số/quyết định/địch/threat): gap lớn nhất ≈ **1:00** (22:30 → 23:28). → #6 ✅.
**Thiếu hụt về LOẠI beat:** (1) **21:26 → 25:58 = 4:32 không có phát súng/mũi tên** (chỉ SC_170 cung giương không bắn ở 23:36) — vượt quy tắc brief ">4′ không action"; (2) 34:30 → 40:00 aftermath không action (5:30) — theo cấu trúc P11–P12, chấp nhận như 2화, có SC_284 (탁발흠 đang tới) đỡ; (3) 0:32–2:42 không có địch hiện diện thật (chỉ đuốc xa) — hook dựa vào "đốt xe mình", đủ mạnh.

---
## 3. ≤10 ĐỀ XUẤT "HAY HƠN KÊNH GỐC" (theo tác động; đòn bẩy: ①địch có tên ②hậu cần đếm ngược ③nhân vật lịch sử là bộ não ④chi phí thật ⑤open loop mỗi phần)

| # | SC | Sửa gì | Vì sao (đòn bẩy) |
|---|---|---|---|
| 1 | SC_168 + SC_178 (không tăng SC) | **Lấp lỗ 4:32 không action bằng 소년 척후:** SC_168 백성민 gửi cậu bé đi đông (giữ). SC_178 (insert 2 척후 Tiên Ti nhìn xuống bàn cát) → **rạng sáng D14 trên đường đông, cậu bé chạm 2 척후 Tiên Ti**: 2 mũi tên, cậu phi thoát, một mũi cắm yên ngựa (8 s, 2-BEAT). Rồi ở SC_189 (đã có 백성민 gật) cậu về báo "동쪽 길에 척후 둘" → 백성민/한승우 đọc là **척후của cột Tùy phía bắc** → red herring giữ nguyên, thậm chí mạnh hơn ("địch ở bắc + nam, không phải tây-bắc"). | Kênh gốc không bao giờ để 4′ không mũi tên. Cậu bé 1화 (mũi tên cắm lốp) có beat thứ hai xuyên series; 탁발흠's 척후 lộ mặt mà đại đội vẫn đoán sai — ①⑤. Combat +8 s, không đổi ledger. |
| 2 | SC_070 / SC_078 (FIX★) | 우중문 **nhận ra 뇌군** qua tiếng K6 → "황제가 찾는 천둥이 강 건너에 있었습니다" là lý do thứ hai ông ta ép 우문술 vượt sông. | Kênh gốc: địch vô danh, chỉ hoảng. Ta: tổng chỉ huy sử thật ra quyết định vượt sông **vì mục tiêu có tên** — ①③; gieo 4화 "우중문 sợ tiếng K2 cắt đường" (story_bible). |
| 3 | SC_143 · SC_180 · SC_202 · SC_238 (theo ledger "30→14→10→0") | **Drone bay 10 trên 14 phút còn lại, không sạc đầy ở D12:** SC_143 đổi thành sạc pin **kính đêm** (không phải drone); SC_180 [ACTION] "màn hình: 14"; SC_202 "pin 14 → hẹn 10"; 박기철 "돌아올 몫 남겨" (SC_193) → drone **tự quay về mỏm với 4 phút cuối** (SC_238) — và bị nhặt *vì* 태오 để dành pin quay về. | ② đồng hồ tài nguyên đổ chuông trong climax; ④ chi phí có mỉa mai bi kịch (nghe lời 박기철 = mất drone vào tay địch); xóa cảm giác "sạc hai lần mà bảo còn một lần". Không đổi SC. |
| 4 | SC_231 hoặc SC_247 (+1 câu thoại 1 어절) | **탁발흠 đếm sấm:** sau viên thứ tư, trên vách hắn giơ 4 ngón cho 부장: **"넷."** — nối 4화 P-45 ("열 번, 네 번, 그리고 두 번. 열여섯이다") và 5화 "스물두 번 울렸습니다". | ① địch học *bằng số* như 박기철 — hai người đếm ở hai phe; kênh gốc không có. Chi phí 0. |
| 5 | SC_257 N (+1 câu) | **"밤눈도 밥을 먹는다는 것을, 그는 아직 몰랐습니다."** — hạt giống cho 4화 "야시경 30%→20%" và 5화 "kính vỡ treo cổ". | ②① — công nghệ đổi phe *có hạn dùng*; khán giả biết điều địch không biết → open loop ngầm cho 2 tập. |
| 6 | SC_250 (+1 câu 해모루, 6 어절) | Tang lễ Goguryeo hiện chỉ narrator. Cho **해모루 nói trên mộ**: **"이 땅에 묻히면 이 땅 사람이오."** rồi cúi đầu — lính Hàn cúi theo. | ③④ — tổ tiên *nói* với hậu duệ; câu dùng được cho title/thumbnail 3화 ("이 땅에 묻히면 이 땅 사람이오"); khán giả 50+: điểm cảm xúc mạnh nhất tập, không khẩu hiệu. |
| 7 | SC_182–183 · SC_215 (FIX APU) | Đổi tiền đề "xe ngủ không bắn được" thành **"xe bị cột vào dây"** (7 kính + drone + 4 radio cắm ổ đuôi xe, dây chằng qua sân; giật sớm = mất chu kỳ). 박기철: "마흔 분. 그 사이 전차는 줄에 묶입니다." / "충전 중입니다! 줄 뽑는 데 이 분!" | Giữ nguyên kịch tính, bịt lỗ kỹ thuật mà cựu binh tăng-thiết giáp 50+ sẽ soi (APU sinh ra để bắn khi tắt máy). ② hậu cần là *sợi dây nhìn thấy được* (hình dây chằng trên đá xếp khan 7 thế kỷ — contrast đúng foundation §9). |
| 8 | SC_173–174 (+1 câu 박기철) | **Đổ phuy vào bình trước đèo, bỏ phuy ở lò rèn**: "드럼 비웠습니다. 이제 전차 배 속뿐입니다." | ② mốc "phuy = 0" nói thành lời (ledger); bỏ 200 L diesel trên buồng động cơ dưới tên lửa (SC_139) và trong trận đèo — realism; hình phuy rỗng nằm nghiêng cạnh lò = "bỏ dần" (foundation §10 điểm riêng). |
| 9 | SC_103 · SC_107 · SC_109 · SC_113 (FIX lều) | **Quân cờ trên bản đồ**: 을지문덕 đặt quân cờ đen ở 살수 khi ra lệnh; 오태민 ấn ngón tay lên cột quân Tùy; radio kêu → ông đặt quân thứ hai cạnh quân đầu. Dời SC_109 vào giữa. | ③ "그의 판에 말이 하나 더 놓였습니다" thành hình thay vì narrator; phá 2 cụm 4 SC đứng nói; nối 2화 "혼자 움직이는 말은 판을 망치오". |
| 10 | P10 veo-stage (SC_208/210/211/212/216/217/221/223/225/229/231/236) | Đánh dấu 2-BEAT thêm 12 clip → shot hiệu dụng ~6 s trong Phase 2–4; giữ 8 s ở Phase 5 (개마무사, cõng thương binh) để tương phản. | Kênh gốc 4 s/shot trận; ta 8,08 s. Không đổi SC/thời gian. |

---
## 4. Địa lý (kiểm theo trình tự di chuyển)
요동성 (요양) → đường núi đông-nam → 압록수 (bến vượt phía tây Uiju) ~300 km theo script (thật 230–280 km đường; hợp) ✓ · 육합성 ở 요동 → lệnh tới bờ tây 압록 "삼백 킬로를 닷새에" (60 km/ngày ngựa trạm) ✓ · 9 quân vượt 압록 rồi nam tiến theo đồng bằng ven biển; đại đội vào núi phía đông — "hai cột song song" hợp lý ✓ · sơn thành "cách 압록 1 ngày về nam" ✓ · **석문령 [虚]** phía nam 압록, trước 살수 (decisions) ✓ — script mô tả đúng 4 cửa/mỏm/ải theo location_bible ✓ · 압록 → 살수 ~100 km (2 ngày sau đèo) — thật 의주→안주 ~110 km ✓ · 살수 = 청천강, "평양에서 북쪽으로 팔십 킬로" (thật ~70–80) ✓ · 천둥 3 về tây "요동성까지 삼백 킬로, 열흘이 넘는 길" rồi 낙양 ✓ · 해모루 phi 2 đêm từ đèo tới 살수 ✓. **Không địa danh thật nào đặt sai trình tự.** Lệch nhỏ: bò kéo 70리 × 9 ngày ≈ 250 km < 300 km (NOTE SC_097); "bờ tây/bờ nam" cần thống nhất "bờ bắc/bờ nam" theo bible.

## 5. Điểm cần coordinator quyết (★)
1. **SC_070/078** — cho 우중문 nhận ra 뇌군 qua "천둥" (đổi outline P4 dòng Enemy adaptation) — khuyến nghị CÓ.
2. **SC_042 dầu** — giữ "400 tại D3" (sửa 1 câu N, ledger ghi gom ≈430) hay đổi thành 370 + 압록 270 km (sửa 5 câu) — khuyến nghị phương án 1.
3. **SC_015 tốc độ** — đại quân 70리/ngày (ghi story_bible), đại đội 30리 = nửa — chỉ đổi 1 câu N.
4. Đề xuất §3 #1 (소년 척후 chạm 척후 Tiên Ti, không tăng SC) và #3 (drone 14→10, không sạc ở D12) — cả hai không đụng ledger/outline; #6 (câu 해모루 trên mộ) thêm 1 thoại.
5. P-38 PZF 2+1 (đang OPEN) và P-47 양제 1 SC — QC không phản đối; ghi foundation nếu giữ.
6. Cắt narration −570 어절 (FIX sản xuất) — giao script-writer pass "narration-trim" trước veo-stage.
