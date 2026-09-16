# 살수 612 — 2화 「요동성」 대본 v1

> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (237 video8s + 50 still_kenburns) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer
> **Nguồn:** outline_ep2.md (khung 12 phần — chuẩn), SCRIPT_BRIEF.md v1, series_foundation.md §7 (2화) + §8/§8b, story_bible.md §1 (612 4–6월 [史]) + quy tắc 시호, character_bible.md (LOCKED — giọng), resource_ledger.md v2 (lệch → outline), location/vehicle/prop bible, logs/decisions.md, full_script_ep1.md v3 (nối giọng/callback).
> **Quy ước ghi (giống 1화 v3):** `N:` = narration tiếng Hàn (격식체, giọng nam trầm). Trong SC có cả `N:` và thoại, editor quyết thứ tự đọc (mặc định: N dẫn vào → TRƯỚC thoại; N bình luận → SAU thoại). `TÊN:` = thoại tiếng Hàn. `[ACTION-VI]` = hành động nhìn thấy được (tiếng Việt, cho veo-prompt-engineer). `[SOUND]` = âm thanh gợi ý. `[COMBAT]` = SC có giao chiến/hỏa lực/bị tấn công (để đếm tỷ lệ combat — mới ở 2화, theo brief). `2-BEAT` trong [ACTION-VI] = 1 SC 8 s gồm 2 shot (cắt ở edit hoặc 2 clip ngắn) — chỉ dùng ở hook và trận. `[NARRATOR IM LẶNG]` / `[MID-ROLL]` / `[END CARD]` theo outline.
> **ID:** CHAR_/LOC_/VEH_/UAV_/EQP_/WPN_/PROP_ theo bible. Nhân vật phụ không ID (ghi tên vai): 소년 척후 (~17, từ 1화), 고구려 초병, 수 공성총관 (tướng chỉ huy công thành Tùy — không tên, không phải 전군총관 1화), 수 전령 (kỵ sứ), 통역 (thông ngôn Tùy), 선비 부장 (phó của 탁발흠), 고구려 농부 (tù binh), 전차장 / 포수 / 조종수 (kíp K2, không tên), 사수 (cối), K3 사수, 2소대 PZF 사수, 초병 (lính Hàn).
> **Ghi chú LOC:** hành doanh 양제 bên 요하 (P2, cách thành 100리) dùng identity LOC_004_YUKHAPSEONG dạng "lều vàng" như 1화 P12; từ P7 (5월) là 육합성 thật (dựng một đêm, chu vi 8리 [史]). Đài quan sát của 양제 phía nam thành (P10, 6월 11 [史]) ghi `LOC_004_YUKHAPSEONG (đài quan sát nam thành)`. Bệnh xá trong thành = nhà gỗ cạnh tường (LOC_002 interior). Dốc đất + 치 đông-nam = LOC_002 (치 동남).
> **Quy ước ngôn ngữ (P-11):** trên màn hình mọi phe nói tiếng Hàn. Goguryeo ↔ đại đội hiểu nhau. Tùy ↔ đại đội không đối thoại trực tiếp trong tập này (탁발흠 hỏi cung nông dân Goguryeo qua 통역). Người đương thời KHÔNG dùng 시호 (영양왕/수 양제): Goguryeo nói "대왕/황제", Tùy nói "폐하"; chỉ narrator dùng 시호. Narrator thì quá khứ "-였습니다/-했습니다", trừ câu mở địa danh ("612년 4월. 요동성.").
> **Từ đúng thời đã dùng:** 전령 (không 기사) · 나각 (không 나팔) · 황공하오나 · 공성총관/전군총관 phân biệt · Goguryeo gọi cối là "우는 쇠" (callback 을보 1화 "쇠가 우는 소리군"), K2 là "쇠수레", drone "쇠새".
> **Chữ Hangul trên xe:** không vẽ bằng AI (decisions #1) — script mô tả bình thường, overlay ở edit.
> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi "X일째/이틀 뒤/간밤에/보름 뒤" trong narration rà theo bảng này; D = ngày kể từ sáng đầu tiên trên đất Goguryeo, 1화 D1–D5):**
>
> | Ngày | Buổi | SC | Sự kiện |
> |---|---|---|---|
> | D25 (4월 중순, "이 땅에 온 지 삼 주") | 새벽 sương | SC_001–012 | 팔륜누차 xuất hiện trong sương — không phải 20, là 40; hầm đang đào [史] |
> | D25 | 오전–낮 | SC_013–025 | đợt xung phong đầu bằng 운제 (tháp chưa vào vị trí) → **cờ hàng giả thứ 3** [史 kế xin hàng] → Tùy dừng, 전령 phi về hành doanh 양제 bên 요하 (100리) |
> | D25 | 저녁–밤 | SC_026–033 | vá tường dưới đuốc (dân + lính + 을보 + 한승우); 전령 tới lều vàng |
> | D26 | 새벽 | SC_034 | cờ trắng vẫn treo, tường đã vá |
> | D26 | 아침 | SC_035–042 | kiểm kê thung lũng: 22 · 140/140/200 · 110 · 18 · 3 · 전차 360 · 발전기 30일; 천둥 3 chạy trên chốt sắt 을보 |
> | D26 | 낮 | SC_043–048 | bệnh xá trong thành (nỏ Tùy bắn vào chớp cửa); 소년 척후 sốt; kháng sinh 13→12 = 60 % |
> | D26 | 저녁 | SC_049–052 | người áo choàng đen trong bóng tường (을지문덕 vào bằng đường bí mật, đại đội chưa biết) · MID-ROLL 1 |
> | D27 | 새벽 | SC_053–054 | trả lời của hoàng đế tới (2 ngày đi-về); tường đã vá, cờ đã hạ |
> | D27 | 낮 | SC_055–072 | **1차 공성** (tháp + 운제 + 충차 vào 옹성 nam) · PZF 1 phát (18→17) · đại quân Tùy lần đầu thấy "sấm" |
> | D27 | 밤 | SC_073–077 | Tùy phủ đất ướt lên xe húc mới; 박기철 ghi 17; người áo choàng đếm ngón tay |
> | D28 | 아침 | SC_078–085 | đại sảnh: 을지문덕 lộ diện — "쇠수레는 며칠이나 달릴 수 있소?" · thử: ít đạn nhất |
> | D28 | 오후 | SC_086–097 | cối 10 viên (2 đăng ký + 8) → 2 tháp cháy từ tầng trên · "열 발에 둘" · cối 110→100 |
> | D28 | 밤 | SC_098–099 | Tùy kéo tháp lùi 6리 (~2,5 km), phủ chiếu đất ướt, đóng thêm |
> | D29 | 새벽 | SC_100–103 | "탑이 다시 마흔입니다" · MID-ROLL 2 · aerial 40 tháp phủ đất |
> | D29 | 저녁 | SC_104–105 | 서아 quàng khăn olive cho 아리; 아리 dạy 태오 chữ trên đất |
> | D29 | 밤 | SC_106–127 | đại sảnh: quân cờ / "명령은 못 받습니다, 임무는 받겠습니다" / bữa ăn / "왕의 것도 아닙니다" · tên lửa Tùy bắn vào thành (mini-combat) · tin 황제 sắp tới · "황제를 죽이면…" · Tùy đói trên đường [史] · thỏa hiệp · "오래 쓸 데" |
> | D33 (4월 하순) | 낮 | SC_128–130 | ENEMY POV: 탁발흠 hỏi cung nông dân Goguryeo qua 통역 → "검은 물" |
> | D33 | 밤 | SC_131–133 | 탁발흠 đi bộ theo vết bánh 천둥 3 (bến suối 1화) lên sườn → thấy đường mòn, thung lũng, 2 phuy; không đánh — đợi lệnh hoàng đế |
> | D45 (5월 초) [史 5월] | 새벽 | SC_134 | **육합성** dựng trong một đêm, chu vi 8리, cách tường tây 2 km |
> | D45 | 낮 | SC_135–138 | 양제 hỏi "뇌군은 어디 있느냐" → 탁발흠 xin đánh "thứ xe uống" → "오늘 밤은 네 것이다" |
> | D45 | 밤 (khô, gió) | SC_139–151 | **HỎA CÔNG**: 6 kính đêm gác; nồi lửa xuống đường mòn; tên lửa → lưới → phuy #1 nổ (narrator im 30 s) → 박기철 tay không lăn phuy #2 → 천둥 4 cháy, 40mm nổ dây chuyền, drone #2 cháy; 백성민 hạ 3 kẻ đột nhập; K2 dưới lưới ướt không sao |
> | D46 | 새벽 | SC_152–156 | MID-ROLL 3 · xác 천둥 4 · "K21 두 대. 드럼 하나. 드론 둘." · "항생제, 없습니다." · 을보 rổ thuốc |
> | D46 | 아침 | SC_157–173 | **2차 공성** (nhỏ) — Goguryeo tự giữ, đại đội không bắn · 을지문덕 rời tường xuống thung lũng giữa trận, chạm K2, hỏi số · "전차 시동 한 번이 드론 열 번" · tin 양제 gom quân riêng · "쇠수레를 쓰시오. 열 발만." |
> | D47–D69 (5월 중순–6월 초) | ngày/đêm | SC_174–193 | Tùy phủ đất mọi tháp, đóng thêm, hầm tiến; tháo tường trong sau 치 đông-nam, đắp dốc 3 ngày; mở rộng lỗ châu mai; mốc đá 100/200/300 bước; Tiên Ti dò lửa lần 2 — 오태민 40mm đuổi (mini-combat); 오태민 nhận giữ thung lũng; "청천강까지 며칠이오?" |
> | D70 (6월 10) | 밤 | SC_194–198 | tháp Tùy tiến vào 1 km; đài quan sát dựng phía nam; K2 rời thung lũng sau ~2 tháng đứng yên, leo dốc (MID-ROLL 4 rồi SC_198) |
> | D71 (6월 11) [史] | 새벽–해질녘 | SC_199–249 | **3차 공성**: 양제 trên đài nam thành [史 6월 11] · cờ trắng #4 — tháp không dừng · cối 40 (100→60) · K2 10 viên (22→12) · nỏ tập trung vào khe · hầm sập 80 m tường → lỗ hổng · PZF 5 (17→12) · 고정수 giáo dài · 해모루 xuất kích cổng bắc · 오태민 trái lệnh đưa 천둥 2 ra cổng bắc (40mm −60 → 220) · "그건 여기 것이 아니오" |
> | D71 | 밤 | SC_250–255 | vá lỗ hổng bằng đá của dốc; xác trên tường; tên Tùy quấy rối tổ vá (mini); lính bỏng không cầm được súng; "포탄 열두 발. 박격포 예순. PZF 열둘. 40밀리 이백이십." · 전차 310 |
> | D72–D74 (6월 중순) | 밤 | SC_256–263 | 육합성: 우중문 · 우문술 · 9군 30만 5천 · 백 일치 군량 [史] · "뇌군도 남쪽으로 갈 것이다. 탁발흠은 따라붙어라." |
> | D75 | 밤 | SC_264–287 | 을지문덕 vẽ đường trên đất ở lỗ hổng: "성은 버티오. 문제는 평양이오." · 9 quân chảy về đông dưới trăng · thung lũng: que đo dầu · "400km, 전차 한 대 몫" · 탁발흠 "막지 않는다. 뒤를 밟는다." · END CARD |

---

## [Phần 1] 안개 속의 탑 — 「안개 속의 탑」 / Chuyện không thể xảy ra  (0:00–1:30)
> Tóm tắt VI: Bình minh sương dày trên tường nam 요동성. 소년 척후 (1화) gác trên 치, nghe tiếng cót két đều từ trong sương. Sương hé: một bánh gỗ khổng lồ, rồi tháp da trâu ướt cao hơn tường — tháp thứ hai, thứ ba. Cậu đánh trống; một mũi nỏ từ tháp cắm vào giá trống. 한승우 + 백성민 chạy lên: "탑이… 몇 개입니까?" — "스물. 아니, 더." Narrator vào 0:48: 612년 4월, 팔륜누차 · 충차 · 운제, và hầm dưới đất. 고정수: "탑이 담보다 높소." Sương tan: bốn mươi.
> Chức năng: ACTION-HOOK · Tài nguyên: — · Foreshadow: "땅 밑 굴" (P10 hầm sập tường), da trâu ướt (P5) · Open loop cuối phần: "탑은 스물이 아니었습니다. 마흔이었습니다."
> Ràng buộc: 0:00–0:30 KHÔNG narrator (narrator vào 0:48 bằng "612년 4월. 요동성."); 0–30 s = 6 shot (SC_001 2-BEAT · SC_002 · SC_003 2-BEAT · SC_004). Nguy hiểm: 0:03 (tiếng cót két), 0:24 (mũi nỏ).

### SC_001 · LOC_002_YODONGSEONG (tường nam, 치) · 소년 척후 · — · video8s · 0:00–0:08
[ACTION-VI] 2-BEAT (3 s + 5 s): (a) 0:00–0:03 màn đen, chỉ một tiếng gỗ cót két rất đều, xa, lặp lại; (b) 0:03–0:08 sương trắng đặc trên mặt tường đá granite, cận nghiêng mặt 소년 척후 (áo gai, mũ da, cung trên lưng) đang quay tai về phía tiếng động, hơi thở trắng. Máy tĩnh.
[SOUND] cót két gỗ nặng đều nhịp, gió nhẹ, không nhạc.

### SC_002 · LOC_002_YODONGSEONG (tường nam) · 소년 척후, 고구려 초병 · — · video8s · 0:08–0:16
[ACTION-VI] Cậu bé đi dọc lan can đá trong sương, tay lần theo lỗ châu mai, tới chỗ một lính gác Goguryeo ngủ gục bên chum nước; cậu lắc vai anh ta, chỉ ra ngoài sương — tiếng cót két nay nhiều lớp, gần hơn.
[SOUND] cót két thành nhiều lớp chồng nhau, giáp va đá, tiếng người tỉnh giấc.
소년 척후: 일어나시오. 소리가… 여럿이오.

### SC_003 · LOC_002_YODONGSEONG (ngoài tường nam, trong sương) · — · VEH_201 · video8s · 0:16–0:24
[ACTION-VI] 2-BEAT (4 s + 4 s): (a) trong sương, một bánh gỗ đặc đường kính hơn người xoay chậm, bùn dính vành, hàng chục bàn chân trần đẩy càng phía sau; (b) máy ngước từ bánh lên: khối gỗ bọc da trâu ướt đen bóng dựng lên qua sương, cao mãi — đỉnh tháp có cờ đỏ nhô CAO HƠN lan can tường đá phía trước máy.
[SOUND] bánh gỗ nghiến đất, dây gai kẽo kẹt, tiếng thở của hàng trăm người đẩy.

### SC_004 · LOC_002_YODONGSEONG (tường nam, 치) · 소년 척후, 고구려 초병 · PROP_017 · video8s · 0:24–0:32
[ACTION-VI] Cậu bé lao tới trống da lớn trên giá gỗ, vung dùi đánh hai tiếng — đúng lúc một mũi nỏ Tùy từ trong sương cắm "퍽" vào cột giá trống cách tay cậu một gang, rung tít. Lính gác Goguryeo bên cạnh gào lên, chỉ ra sương.
[SOUND] trống hai tiếng nặng, mũi nỏ cắm gỗ, tiếng gào, rồi trống Tùy nổi lên từ xa đáp lại.
[COMBAT]
고구려 초병: 탑이다! 탑이 왔다!

### SC_005 · LOC_002_YODONGSEONG (bậc thang lên tường nam) · CHAR_001, CHAR_006 · PROP_006 · video8s · 0:32–0:40
[ACTION-VI] 한승우 và 백성민 chạy lên bậc đá hai bậc một, mũ cài dây trong lúc chạy, ống nhòm trên ngực 백성민 đập vào giáp; hai người tới lan can, 백성민 giơ ống nhòm ngay. 한승우 hỏi không quay đầu.
[SOUND] giày trên đá, giáp, trống Tùy mỗi lúc một nhiều hướng.
한승우: 탑이… 몇 개입니까?

### SC_006 · LOC_002_YODONGSEONG (tường nam, qua ống nhòm) · CHAR_006 · PROP_006, VEH_201 · video8s · 0:40–0:48
[ACTION-VI] POV ống nhòm: sương loãng dần theo gió — một tháp, hai, rồi hàng tháp da đen nối nhau ra xa, cái sau chỉ còn là bóng; phía dưới mỗi tháp là hàng người đẩy như kiến. 백성민 hạ ống nhòm, giọng phẳng.
[SOUND] gió cuốn sương, trống, tiếng người đẩy vọng lên.
백성민: 스물. 아니, 더.

### SC_007 · LOC_002_YODONGSEONG (aerial, đồng bằng nam-tây) · — · VEH_201, VEH_202, VEH_203 · still_kenburns · 0:48–0:54
[ACTION-VI] Ảnh aerial cao: biển sương phủ đồng bằng phía nam-tây thành; đỉnh các tháp gỗ nhô lên khỏi sương như đảo, hàng dài; cờ đỏ; mặt trời đỏ thấp. Ken-burns kéo ra chậm.
[SOUND] trống Tùy khắp đồng bằng, gió trên cao.
N: 612년 4월. 요동성. 수 양제의 공성 무기가 요동성 앞에 도착했습니다. 요하를 건넌 지 스무 날 남짓이었습니다.

### SC_008 · LOC_002_YODONGSEONG (bản vẽ — ken-burns) · — · VEH_201 · still_kenburns · 0:54–1:00
[ACTION-VI] Ảnh: bản vẽ mực nâu trên lụa cũ kiểu binh thư — tháp công thành tám bánh, bốn tầng, cầu bập bênh trên đỉnh, da trâu bọc mặt trước, hàng người đẩy. Ken-burns trượt từ bánh lên cầu.
[SOUND] trống nền xa, bút lông.
N: 팔륜누차. 바퀴가 여덟, 층이 넷. 성벽보다 높았습니다. 앞면은 젖은 소가죽으로 덮었습니다. 불화살이 붙지 않게 하기 위해서였습니다.

### SC_009 · LOC_002_YODONGSEONG (bản vẽ — ken-burns) · — · VEH_202, VEH_203 · still_kenburns · 1:00–1:06
[ACTION-VI] Ảnh: bản vẽ tiếp — xe phá cổng mái mai rùa (충차), xe thang gập (운제); bên dưới mặt đất vẽ cắt ngang một đường hầm có cột chống gỗ chạy về phía chân tường. Ken-burns đi từ mặt đất xuống hầm.
[SOUND] bút lông, rồi tiếng cuốc rất khẽ dưới đất.
N: 충차, 운제. 그리고 땅 밑으로는 굴이 파이고 있었습니다. 위에서 보이는 것만이 공성이 아니었습니다.

### SC_010 · LOC_002_YODONGSEONG (dưới đồng bằng — hầm Tùy) · lính Tùy đào hầm · WPN_201 · video8s · 1:06–1:14
[ACTION-VI] Trong hầm đất thấp: đèn dầu treo cột chống gỗ, lính Tùy cởi trần cuốc đất, chuyền giỏ về sau; nước rỉ vách; một cột gỗ mới được nêm vào. Máy thấp, tracking theo giỏ đất.
[SOUND] cuốc, thở, gỗ nêm, nước nhỏ giọt; trống trên mặt đất nghe ù.
N: 굴은 밤에만 팠습니다. 흙은 자루에 담아 멀리 버렸습니다. 성 위에서는 아무것도 보이지 않았습니다. 그것이 굴의 목적이었습니다.

### SC_011 · LOC_002_YODONGSEONG (tường nam) · CHAR_104, CHAR_001 · — · video8s · 1:14–1:22
[ACTION-VI] 고정수 lên tường, mũ trụ ĐỘI trên đầu lần đầu, áo choàng xám, chùm chìa khóa; ông nhìn hàng tháp, rồi nhìn lên đỉnh tháp gần nhất — cao hơn lan can chỗ ông đứng một đầu người; ông quay sang 한승우.
[SOUND] trống, gió, chìa khóa.
N: 성주는 담의 높이를 알았습니다. 서른 자였습니다. 탑은 그보다 높았습니다. 담이 높다는 것은 이제 아무 뜻도 없었습니다.
고정수: 탑이 성벽보다 높소.

### SC_012 · LOC_002_YODONGSEONG (tường nam, wide) · CHAR_001, CHAR_104, CHAR_006, lính Goguryeo · VEH_201 · video8s · 1:22–1:30
[ACTION-VI] Wide từ trên tường qua vai ba người: gió xé sương hẳn — hàng tháp da đen kéo dài hết tầm mắt vòng theo mặt nam và tây thành, trống, cờ đỏ, phía sau là biển lều. Lính Goguryeo dọc tường đứng im. Máy tĩnh.
[SOUND] gió mạnh, trống dồn, rồi im một nhịp.
N: 안개가 걷혔습니다. 탑은 스물이 아니었습니다. 마흔이었습니다.

[Kết thúc Phần 1]

## [Phần 2] 항복 깃발의 비밀 — 「항복 깃발의 비밀」 / Họ đang ở đâu  (1:30–4:30)
> Tóm tắt VI: Aerial: vòng vây khép, rừng bị đốn đóng tháp, miệng hầm phía nam-tây; thung lũng LOC_003 đã bị trinh sát Tiên Ti thấy từ 1화 nhưng 20 ngày không ai tới — vì sao, chưa ai biết. Narrator kể lệnh thật của 양제 (mọi tiến thoái phải tấu; Goguryeo xin hàng thì phải nhận). Đợt xung phong đầu bằng 운제 tới chân tường; một đoạn tường cũ nứt; 고정수 ra lệnh dựng cờ trắng — tướng Tùy phất tay dừng, 전령 phi về tây 100리. 한승우: "말객님, 이게… 몇 번째입니까?" 해모루: "세 번째요." 오태민 qua radio đòi đánh; 한승우 không cho — bắn là lộ kế. Đêm: dân + lính + 을보 + 한승우 vá tường dưới đuốc. Tướng Tùy nhìn đuốc, biết, nhưng không được động. 해모루: "황제가 눈치채면 끝이오." 소년 척후 ho khi khiêng đá (foreshadow sốt). Bình minh: cờ trắng vẫn treo trên tường đã vá.
> Chức năng: DISCOVERY · Combat: SC_015–019 (xung phong + cờ) · Tài nguyên giảm: thời gian ("황제가 눈치채면 끝이오") · Quyết định lịch sử: 고정수 dựng cờ hàng giả [史] · Open loop: "네 번째 항복 깃발이 오르는 날, 황제는 요동성 앞에 와 있을 것이었습니다."

### SC_013 · LOC_002_YODONGSEONG (aerial ban ngày, toàn vòng vây) · — · WPN_201, VEH_201 · still_kenburns · 1:30–1:40
[ACTION-VI] Ảnh aerial rất cao, sương đã tan: 요동성 trên gò giữa đồng vàng; lều trại Tùy phủ kín tây, nam, bắc tới chân trời; vạt rừng phía tây-nam bị đốn trọc, gốc cây trắng lốp, bãi đóng tháp; dọc phía nam-tây, những đống đất mới đổ thành hàng (miệng hầm). Phía đông: dải đồi sồi thưa — thung lũng nhỏ dưới tán cây, không một bóng địch. Ken-burns từ thành kéo ra tới rừng trọc.
[SOUND] gió trên cao, trống nhiều hướng, tiếng búa rất xa.
N: 이 땅에 온 지 삼 주였습니다. 포위는 스무 날째였습니다. 수나라는 숲 하나를 베어 탑을 만들었습니다. 성 뒤 골짜기는 지난달 밤 선비 척후에게 들켰습니다. 그 뒤로 스무 날, 아무도 오지 않았습니다. 이유는 아직 아무도 몰랐습니다.

### SC_014 · LOC_004_YUKHAPSEONG (hành doanh 양제 bên 요하 — lều vàng, ken-burns) · CHAR_201 · PROP_021 · still_kenburns · 1:40–1:50
[ACTION-VI] Ảnh: lều-điện lụa vàng bên bờ sông Liêu ban ngày, cờ Tùy, hàng hoạn quan; trên bậc, 양제 áo vàng thổ ngồi, một quan quỳ dâng thẻ. Ken-burns đẩy chậm vào thẻ.
[SOUND] lụa gió, trống xa.
N: 황제는 요하 서안에 있었습니다. 성에서 백 리였습니다. 황제의 명령은 둘이었습니다. 나아가고 물러서는 것은 모두 짐에게 아뢰라. 고구려가 항복을 청하면 받아들이고, 치지 말라. 이 두 줄이 요동성을 지키고 있었습니다.

### SC_015 · LOC_002_YODONGSEONG (ngoài tường nam, hào) · lính Tùy · VEH_203, WPN_201 · video8s · 1:50–1:58
[ACTION-VI] Giữa buổi sáng: sóng bộ binh Tùy khiên gỗ chạy qua bãi cỏ nát tới hào đã lấp bằng bao đất và bó củi thành đường đắp, khiêng thang gập 운제; phía sau xa, các tháp vẫn bò chậm chưa tới. Aerial thấp theo hàng đầu.
[SOUND] hô đồng thanh, khiên va, ván đập nước.
[COMBAT]
N: 해자는 흙 자루로 메워져 있었습니다. 탑이 자리를 잡기 전에 사다리가 먼저 왔습니다. 탑은 하루에 오 리를 갔습니다. 사다리는 사람의 걸음이었습니다.

### SC_016 · LOC_002_YODONGSEONG (mặt tường nam) · lính Goguryeo · WPN_101 · video8s · 1:58–2:06
[ACTION-VI] Trên tường: cung thủ Goguryeo bắn xuống hào; đá tảng lăn qua lan can; nồi nước sôi hắt xuống một thang vừa dựng — thang bị đẩy đổ bằng sào chạc. Không cận thương vong.
[SOUND] dây cung hàng loạt, đá đập thang, nước sôi xèo, thét dưới hào.
[COMBAT]
N: 고구려는 이백 년 동안 이 성을 지켜 온 사람들이었습니다. 돌과 물과 화살. 그것이 그들의 순서였습니다.

### SC_017 · LOC_002_YODONGSEONG (đoạn tường cũ phía tây-nam) · lính Goguryeo · — · video8s · 2:06–2:14
[ACTION-VI] Một đoạn tường cũ gần góc tây-nam rùng lên khi hai thang cùng đập vào: vài tảng đá xếp khan trượt rơi khỏi mặt ngoài, để lộ kẽ hở rộng bằng bàn tay chạy dọc xuống; lính Goguryeo trên đó lùi lại nhìn xuống chân. Cận kẽ nứt.
[SOUND] đá lăn, tiếng lính gọi nhau hoảng.
[COMBAT]
N: 담에는 약한 곳이 있었습니다. 이백 년 된 돌이었습니다. 수나라는 그곳을 알고 있었습니다. 사다리는 그곳에 몰렸습니다.

### SC_018 · LOC_002_YODONGSEONG (tường nam, 치) · CHAR_104, lính Goguryeo · — · video8s · 2:14–2:22
[ACTION-VI] 고정수 nhìn kẽ nứt, nhìn thang Tùy đã chạm lan can, nhìn về phía tây nơi hành doanh hoàng đế; ông không do dự — quay lại, ra hiệu cho một lính cầm giáo có buộc sẵn tấm vải trắng cuộn. Cận mặt ông rồi bàn tay ra hiệu.
[SOUND] thét, thang gỗ, gió.
[COMBAT]
N: 성주는 담을 보지 않았습니다. 서쪽을 보았습니다. 황제의 두 줄 명령을 그는 외우고 있었습니다.
고정수: 깃발을 올려라.

### SC_019 · LOC_002_YODONGSEONG (치 và chân tường) · 수 공성총관, lính Tùy · WPN_201, VEH_203 · video8s · 2:22–2:30
[ACTION-VI] Tấm vải trắng dựng lên trên 치; dưới thang, lính Tùy đang leo ngẩng lên nhìn; tướng công thành Tùy giáp 명광개 trên ngựa phía sau hào giơ cao tay — trống ngừng giữa nhịp; lính trên thang khựng, rồi leo xuống. Máy từ chân tường ngước lên cờ.
[SOUND] trống ngừng đột ngột, thang gỗ kêu, tiếng hô "멈춰라" lan dần.
[COMBAT]
N: 흰 천 하나가 올라갔습니다. 만 명이 멈췄습니다. 황제의 명령이 그렇게 시켰습니다.

### SC_020 · LOC_002_YODONGSEONG (tường nam, cách 치 vài chục mét) · CHAR_001, CHAR_105 · — · video8s · 2:30–2:38
[ACTION-VI] 한승우 đứng bên 해모루 ở lan can, ống nhòm hạ, nhìn hàng nghìn lính Tùy quay lưng rút khỏi hào — không hiểu; ông quay sang 해모루, giọng thấp.
[SOUND] lính Tùy rút, ván kéo, gió.
N: 한승우는 항복을 본 적이 없었습니다. 항복하는 성이 이렇게 조용할 리 없었습니다. 그는 물었습니다.
한승우: 말객님, 이게… 몇 번째입니까?

### SC_021 · LOC_002_YODONGSEONG (tường nam) · CHAR_105 · — · video8s · 2:38–2:46
[ACTION-VI] 해모루 không nhìn ông — nhìn tướng Tùy đang gọi người viết thư; nói như nói chuyện thời tiết, khóe miệng hơi nhếch.
[SOUND] gió, xa xa tiếng ngựa.
N: 해모루에게 이것은 새로운 일이 아니었습니다. 성이 늘 하던 일이었습니다.
해모루: 세 번째요. 황제가 대답할 때까지 저들은 못 움직이오.

### SC_022 · LOC_002_YODONGSEONG (phía Tùy, sau hào) · 수 공성총관, 수 전령, quan viết · WPN_201 · video8s · 2:46–2:54
[ACTION-VI] Tướng công thành Tùy đọc cho quan viết trên thẻ lụa; ấn triện; ống thư trao cho kỵ sứ — người này quay ngựa phi về tây qua biển lều, bụi bốc thành vệt. Tracking theo kỵ sứ.
[SOUND] ngựa phi, lụa, tiếng tướng gầm sau lưng.
N: 총관은 글을 썼습니다. 고구려가 항복을 청한다. 전령은 서쪽으로 백 리를 달렸습니다. 하루 길이었습니다. 답이 오는 데 또 하루였습니다.

### SC_023 · LOC_002_YODONGSEONG (aerial, đồng bằng tây) · 수 전령 · WPN_201 · still_kenburns · 2:54–3:04
[ACTION-VI] Ảnh aerial: một vệt bụi nhỏ xíu của kỵ sứ chạy xuyên biển lều Tùy về phía sông Liêu lấp lánh ở chân trời; hàng vạn người đứng yên hai bên. Ken-burns theo vệt bụi.
[SOUND] gió trên cao, một tiếng ngựa nhỏ.
N: 백만 대군이 사람 하나를 기다렸습니다. 황제가 모든 것을 직접 정했기 때문입니다. 그것이 수나라의 힘이었고, 그날은 수나라의 약점이었습니다. 요동성은 그 약점을 세 번째 쓰고 있었습니다.

### SC_024 · LOC_003_CHEONDUNG_BASE (chốt quan sát trên gò tây thung) · CHAR_002 · PROP_006, EQP_002 · video8s · 3:04–3:12
[ACTION-VI] Chốt quan sát trên gò tây thung lũng (lính gác nằm bên): 오태민 tay áo xắn, ống nhòm dán mắt về phía tường nam xa; ông thấy hàng lính Tùy quay lưng rút khỏi hào; bấm tổ hợp radio, giọng to.
[SOUND] PTT, gió lùa khe.
N: 골짜기 위 언덕에서 오태민도 그것을 보았습니다. 그에게 등을 돌린 적은 과녁이었습니다.
오태민: 천둥 지휘, 여기는 천둥 2. 지금 치면 끝납니다.

### SC_025 · LOC_002_YODONGSEONG (tường nam) · CHAR_001 · EQP_002 · video8s · 3:12–3:20
[ACTION-VI] 한승우 nhìn xuống sân trong: lính Goguryeo đã bắt đầu khiêng đá về phía đoạn tường nứt trước cả khi lính Tùy rút hết; ông hiểu; bấm radio, ngắn.
[SOUND] PTT, đá lăn dưới sân.
N: 한승우는 그제야 보았습니다. 총이 울리면 흰 천은 거짓이 됩니다. 거짓이 되면 담은 고쳐지지 않습니다. 이 사람들은 머리로 이기고 있었습니다. 총 없이도.
한승우: 천둥 2, 여기는 천둥 지휘. 안 친다. 지켜봐.

### SC_026 · LOC_002_YODONGSEONG (chân tường trong, đoạn nứt — hoàng hôn sang đêm) · dân Goguryeo, lính, CHAR_107 · PROP_016 · video8s · 3:20–3:28
[ACTION-VI] Đuốc thắp dọc chân tường trong; đàn ông khiêng đá tảng bằng cáng gỗ, đàn bà đội giỏ đất, lính Goguryeo cởi giáp xếp đá; 아리 (khăn gai, túi thuốc) bê giỏ đá nhỏ len giữa dòng người. Tracking ngang.
[SOUND] đá đặt lên đá, thở, gọi nhau, đuốc cháy.
N: 해가 지자 성이 움직였습니다. 군사만이 아니었습니다. 삼천 명의 피난민이 돌을 날랐습니다. 지난달 동문으로 들어온 사람들이었습니다.

### SC_027 · LOC_002_YODONGSEONG (đoạn tường nứt, giàn gỗ) · CHAR_106, thợ đá Goguryeo · PROP_019 · video8s · 3:28–3:36
[ACTION-VI] 을보 (chân còn tập tễnh, tạp dề da) đứng trên giàn gỗ thấp, búa nhỏ gõ vào tảng đá vừa đặt, nghe tiếng, lắc đầu, chỉ xuống hàng dưới — thợ đá tháo ra xếp lại từ dưới.
[SOUND] búa gõ đá "딱, 딱", gỗ giàn kêu.
N: 을보는 대장장이였습니다. 하지만 요동성에서 돌을 모르는 사람은 없었습니다. 담은 이 성의 밥이었습니다.
을보: 돌은 아래부터야. 위부터 쌓으면 다 무너져.

### SC_028 · LOC_002_YODONGSEONG (đoạn tường nứt) · CHAR_001, lính Goguryeo · PROP_011 · video8s · 3:36–3:44
[ACTION-VI] 한승우 tháo găng, cùng một lính Goguryeo giáp lamellar nâng chung một tảng đá lên giàn — vai áo camo có miếng vá 태극기 sát vai giáp sắt; hai người đặt đá, không nhìn nhau, quay lại lấy tảng tiếp. Máy trung, tĩnh.
[SOUND] đá, thở, đuốc.
N: 한승우는 돌을 들었습니다. 그는 이 성에 지혜를 가져온 사람이 아니었습니다. 이 성은 그가 오기 전에도 지혜로웠습니다. 그가 가져온 것은 어깨 둘이었습니다. 그날 밤은 그것으로 충분했습니다.

### SC_029 · LOC_002_YODONGSEONG (mặt ngoài tường, đêm — ken-burns) · — · PROP_016 · still_kenburns · 3:44–3:54
[ACTION-VI] Ảnh: mặt ngoài tường đá dưới ánh đuốc — đoạn vá mới màu đá sáng xếp khít giữa đá cũ đen rêu, thành một vệt dọc nhạt; trên tường, cờ trắng vẫn cắm. Ken-burns đẩy chậm vào vệt đá mới.
[SOUND] đuốc, gió, xa xa trống Tùy im.
N: 역사는 이 일을 기록했습니다. 요동성은 무너질 때마다 항복을 청했고, 답이 오기 전에 담을 고쳤습니다. 한 번이 아니었습니다. 여러 번이었습니다. 흰 천 하나가 돌 백 개의 값을 했습니다.

### SC_030 · LOC_002_YODONGSEONG (trại Tùy đêm, sau hào) · 수 공성총관 · WPN_201 · video8s · 3:54–4:02
[ACTION-VI] Tướng công thành Tùy đứng trước lều, nhìn hàng đuốc lấp lóa dọc mặt tường Goguryeo và bóng người khiêng đá; hàm bạnh; sau lưng ông, lính ngồi ôm giáo chờ. Ông không ra lệnh gì.
[SOUND] đuốc xa, lính ho, ngựa.
N: 총관은 알았습니다. 항복하는 자는 밤에 담을 고치지 않습니다. 그래도 그는 움직일 수 없었습니다. 황제의 글이 아직 오지 않았습니다.
수 공성총관: 저 불빛은 항복하는 자의 불빛이 아니다.

### SC_031 · LOC_002_YODONGSEONG (chân tường trong) · CHAR_105, CHAR_001 · — · video8s · 4:02–4:10
[ACTION-VI] 해모루 và 한승우 đi dọc chân tường (walk-and-talk), qua hàng người khiêng đá; 해모루 ngẩng nhìn cờ trắng trên tường rồi nói nhỏ, không đùa nữa.
[SOUND] bước chân, đá, đuốc.
N: 세 번은 통했습니다. 네 번째는 아무도 장담하지 못했습니다.
해모루: 황제가 눈치채면 끝이오.

### SC_032 · LOC_002_YODONGSEONG (chân tường trong) · 소년 척후, CHAR_004 · — · video8s · 4:10–4:18
[ACTION-VI] 소년 척후 khiêng cáng đá cùng một lính, đặt xuống, ho khan, lấy tay áo lau mồ hôi dù đêm lạnh; 서아 đi ngang với túi quân y, dừng một nhịp nhìn cậu, rồi bị lính gọi đi băng người khác. Cận trán cậu ướt mồ hôi.
[SOUND] ho, đá, gọi "의녀!".
N: 소년 척후는 삼 주 전 화살을 돌려받은 아이였습니다. 지금은 성벽 위의 군사였습니다. 그날 밤 그는 땀을 흘렸습니다. 밤은 추웠습니다.

### SC_033 · LOC_004_YUKHAPSEONG (lều vàng bên 요하, đêm — ken-burns) · 수 전령, CHAR_201 · PROP_021 · still_kenburns · 4:18–4:24
[ACTION-VI] Ảnh: trong lều vàng đêm, kỵ sứ bụi đường quỳ dâng ống thư; hoạn quan bưng lên bậc; 양제 không cúi nhìn, quạt tròn che nửa mặt. Ken-burns đẩy vào ống thư.
[SOUND] lụa, lửa đèn lồng.
N: 전령은 그날 밤 황제의 발치에 닿았습니다. 황제는 글을 읽고 한마디만 했습니다. 받으라. 그 한마디가 돌아오는 동안 담은 완성될 것이었습니다.

### SC_034 · LOC_002_YODONGSEONG (치 tường nam, bình minh — ken-burns) · — · — · still_kenburns · 4:24–4:30
[ACTION-VI] Ảnh: bình minh xám, cờ trắng còn treo trên 치, bên dưới là đoạn tường mới vá màu sáng; đồng bằng phía trước: tháp Tùy đứng im, lính ngồi. Ken-burns kéo ra từ cờ.
[SOUND] gió, chim sớm.
N: 네 번째 항복 깃발이 오르는 날, 황제는 요동성 앞에 와 있을 것이었습니다.

[Kết thúc Phần 2]

## [Phần 3] 발전기 연료 30일 — 「발전기 연료 30일」 / Kiểm kê  (4:30–7:00)
> Tóm tắt VI: Sáng D26, thung lũng sau ba tuần. 박기철 đọc bảng (walk-and-talk dọc hàng xe): K2 22 · 40mm 140/140/200 · cối 110 · PZF 18 · drone 3 · 전차 360 (시동 점검 10 km) · 장갑차 7할 · 드럼 2 · 발전기 = 드론 15회; 태오: "삼십 일". 천둥 3 chạy thử trên chốt sắt của 을보: "돈다. 내 쇠가 돈다." Lính tiêu chảy — 을보: đun nước. Trong thành: bệnh xá nhà gỗ cạnh tường, nỏ Tùy bắn vào chớp cửa; thương binh Goguryeo bỏng tên lửa, nhiễm trùng; 소년 척후 sốt cao — 서아 tiêm kháng sinh; 한승우 thấy ở cửa, không cản: "항생제, 예순 퍼센트. 열두 개입니다." 을보 đưa thanh sắt + chốt dự phòng: "쇠는 쇠요." Hoàng hôn: người áo choàng đen trong bóng tường, 해모루 cúi rất sâu; 한승우 hỏi — 해모루: "성주께서 내일 부르실 것이오."
> Chức năng: DECISION · Combat mini: SC_043 (nỏ vào bệnh xá) · Tài nguyên nói thành lời: "전차 삼백육십", "드론 열다섯 번 → 삼십 일", "드론 셋", "항생제 예순 퍼센트, 열두 개" · Open loop: "그날 저녁, 비밀 통로로 한 사람이 성에 들어왔습니다. 그는 쇠수레를 보러 온 것이 아니었습니다." → [MID-ROLL 1 · 7:00]

### SC_035 · LOC_003_CHEONDUNG_BASE (bình minh — ken-burns) · — · VEH_001, VEH_002, VEH_003, VEH_004 · still_kenburns · 4:30–4:40
[ACTION-VI] Ảnh: thung lũng sáng xám: K2 dưới lưới đã bạc màu, ba K21 hàng ngang (천둥 3 có chốt sắt thô ở bánh thứ ba), hai K511 và K151 sát sườn tây, hai phuy dầu sau bao cát cách xe 30 m; lều olive cạnh lều gai nâu; bảng gỗ ghi số treo ở lều chỉ huy, chữ phấn bị mưa loang. Ken-burns từ bảng ra toàn cảnh.
[SOUND] chim, gió khe, máy phát K151 không chạy — im.
N: 스물여섯째 아침이었습니다. 삼 주 동안 늘어난 것은 없었습니다. 줄어든 것만 있었습니다. 박기철은 매일 아침 같은 판을 읽었습니다. 읽는 것이 그의 기도였습니다.

### SC_036 · LOC_003_CHEONDUNG_BASE (hàng xe) · CHAR_003, CHAR_001 · VEH_001, VEH_002 · video8s · 4:40–4:48
[ACTION-VI] Walk-and-talk: 박기철 sổ bìa xanh trong tay, đi dọc hàng xe với 한승우 (vừa từ thành về, bụi đá trên vai); ông gõ ngón tay lên hông tháp K2 khi đọc số đầu, rồi lên hông từng K21.
[SOUND] bước trên đất trần, giấy, gõ thép.
N: 전차는 한 발도 쏘지 않았습니다. 장갑차 둘은 지난달 벌판과 동쪽 길에서 예순 발씩 썼습니다. 숫자는 그대로였습니다.
박기철: 포탄 스물두 발. 40밀리, 백사십, 백사십, 이백.

### SC_037 · LOC_003_CHEONDUNG_BASE (hố cối trên gò) · CHAR_003, CHAR_001, tổ cối · WPN_002, WPN_005 · video8s · 4:48–4:56
[ACTION-VI] Hai người lên gò tới hố cối: thùng đạn cối xếp có đánh dấu phấn, hai ống PZF-3 dựng dưới poncho; 박기철 đếm bằng ngón tay theo thùng, không nhìn sổ.
[SOUND] gió trên gò, nắp thùng đạn.
N: 지난달 여울에서 열 발이 나갔습니다. 문 앞에서 아직 한 발도 나가지 않았습니다. 판처파우스트는 상자째 그대로였습니다.
박기철: 박격포 백십. PZF 열여덟. 드론 셋.

### SC_038 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_003 · VEH_001 · video8s · 4:56–5:04
[ACTION-VI] 박기철 quay lại K2, rút que đo dầu dài ra khỏi nắp thùng dầu, giơ lên ánh sáng: vệt ướt cao gần đỉnh; ông lau que bằng giẻ đỏ, nói con số như báo giờ.
[SOUND] que kim loại, giẻ, gió.
N: 삼백칠십이 삼백육십이 되어 있었습니다. 싸우지 않아도 기계는 먹었습니다. 일주일에 한 번, 시동만 걸어도 그랬습니다.
박기철: 전차 삼백육십. 시동 점검으로 열 킬로 먹었습니다.

### SC_039 · LOC_003_CHEONDUNG_BASE (ụ bao cát phuy, cách xe 30 bước) · CHAR_003, CHAR_001 · VEH_003, PROP_007 · video8s · 5:04–5:12
[ACTION-VI] Hai người tới ụ bao cát cách hàng xe ba mươi bước: hai phuy xanh olive tam giác đỏ đứng sau bao cát; 박기철 gõ nắm tay lên từng phuy — tiếng đặc; rồi chỉ về máy phát nhỏ trên K151 và can 20 L bên cạnh xe.
[SOUND] gõ phuy "둥, 둥" đặc, gió.
N: 드럼 둘은 손대지 않았습니다. 박기철은 통을 수레에서 삼십 걸음 떼어 두었습니다. 발전기 기름은 따로였습니다. 그것은 드론과 야시경과 무전기의 밥이었습니다.
박기철: 드럼 둘. 발전기 기름은 드론 열다섯 번입니다.

### SC_040 · LOC_003_CHEONDUNG_BASE (bên K151) · CHAR_005, CHAR_003 · VEH_004, UAV_001 · video8s · 5:12–5:20
[ACTION-VI] 태오 ngồi trên bậc K151, dây sạc chưa cắm, drone #2 và #3 đặt trên nắp ca-pô, chiếc #4 trong hộp; cậu tính trên ngón tay, ngẩng lên nói với 박기철; 박기철 gật một cái.
[SOUND] dây cáp, gió.
N: 이틀에 한 번 날리면 서른 날이었습니다. 서른 날 뒤에는 하늘의 눈이 감길 것이었습니다. 태오는 그 셈을 매일 했습니다.
장태오: 열다섯 번이면… 삼십 일입니다.

### SC_041 · LOC_003_CHEONDUNG_BASE (bãi trống) · CHAR_106, CHAR_003 · VEH_002, PROP_019 · video8s · 5:20–5:28
[ACTION-VI] 천둥 3 lăn chậm 20 m trên đất trần, 박기철 nhô nửa người ở cửa lái; 을보 đi bộ sát bánh thứ ba, bàn tay áp lên váy xích nghe rung, mắt trái nheo; ông gõ búa nhỏ hai cái lên chốt sắt thô khi xe dừng — gật.
[SOUND] động cơ K21 ga nhỏ, xích, búa gõ.
N: 천둥 3호는 고구려 쇠로 굴렀습니다. 삼 주째였습니다. 을보는 매일 그 바퀴 소리를 들으러 왔습니다.
을보: 돈다. 내 쇠가 돈다.

### SC_042 · LOC_003_CHEONDUNG_BASE (bếp Goguryeo, rìa lều) · CHAR_106, 초병 (lính Hàn), CHAR_004 · — · video8s · 5:28–5:36
[ACTION-VI] Một lính Hàn ngồi bệt bên bếp đá, mặt tái, ôm bụng; 서아 đưa gói muối bù nước; 을보 đi qua, chỉ cây búa về phía suối rồi về chum đất đang sôi trên bếp, quát nhẹ.
[SOUND] lửa, nước sôi, tiếng lính rên.
N: 이 땅의 물은 이 땅의 배에만 익숙했습니다. 삼 주 만에 여덟 명이 배를 앓았습니다. 약은 필요 없었습니다. 불이 필요했습니다.
을보: 물은 끓여서 마시게. 낯선 배는 이 물을 몰라.

### SC_043 · LOC_002_YODONGSEONG (bệnh xá — nhà gỗ cạnh tường trong) · CHAR_004, CHAR_107, thương binh Goguryeo · PROP_009 · video8s · 5:36–5:44
[ACTION-VI] Trong nhà gỗ tối, sàn trải chiếu: hàng thương binh Goguryeo nằm — vai bỏng đen vì tên lửa, cẳng tay sưng tím nhiễm trùng; 서아 hai tay áo máu tới khuỷu, đèn đội đầu; 아리 cầm chậu. Bỗng hai mũi nỏ Tùy xuyên chớp cửa gỗ cắm vào cột trong nhà — thương binh giật mình; 서아 không ngẩng lên, tiếp tục cắt băng.
[SOUND] nỏ xuyên gỗ "탁, 탁", rên, kéo cắt.
[COMBAT]
N: 성 안의 병실은 담에서 스무 걸음이었습니다. 수나라 쇠뇌는 담을 넘어왔습니다. 서아는 셋째 날부터 고개를 들지 않았습니다.

### SC_044 · LOC_002_YODONGSEONG (bệnh xá) · 소년 척후, CHAR_004, CHAR_107 · — · video8s · 5:44–5:52
[ACTION-VI] 소년 척후 nằm co trên chiếu, run từng cơn, cẳng tay bỏng đỏ sưng mọng, môi khô; 아리 quỳ bên, tay đặt lên trán cậu rồi rụt lại; 서아 tới, đặt mu bàn tay lên cổ cậu.
[SOUND] răng va, thở gấp.
N: 사흘 전 불화살이 그의 팔을 스쳤습니다. 상처는 작았습니다. 열은 크게 왔습니다. 이 시대에 그 열은 죽음의 이름이었습니다.
아리: 언니, 이 애 열이 불 같아요.

### SC_045 · LOC_002_YODONGSEONG (bệnh xá) · CHAR_004, CHAR_001 · PROP_009 · video8s · 5:52–6:00
[ACTION-VI] 서아 mở ba lô quân y, ngăn kháng sinh: mười ba lọ nhỏ xếp hàng — cô đếm bằng đầu ngón tay, rút một lọ, xé ống tiêm. Ngẩng lên: 한승우 đứng trong khung cửa, bụi đá, nhìn lọ thuốc trong tay cô. Một nhịp. Ông không nói gì, quay đi. Cô cúi xuống tiêm.
[SOUND] xé bao ống tiêm, lửa đèn, tiếng nỏ xa.
N: 열세 개였습니다. 아흔네 명의 몫이었습니다. 한승우는 문 앞에 서 있었습니다. 그는 말리지 않았습니다. 말리지 않는 것도 결정이었습니다.

### SC_046 · LOC_002_YODONGSEONG (bệnh xá) · CHAR_004 · PROP_009 · video8s · 6:00–6:08
[ACTION-VI] Cận: kim vào cánh tay cậu bé, 서아 ấn pít-tông chậm; rút kim, dán băng; cô nói vào khoảng trống nơi 한승우 vừa đứng, không ngẩng lên, giọng đều như 박기철 đọc sổ.
[SOUND] băng dính, thở của cậu bé dịu lại.
N: 그녀는 숫자를 말하는 사람이 되어 있었습니다. 박기철이 기름을 읽듯, 서아는 병을 읽었습니다.
윤서아: 항생제, 예순 퍼센트. 열두 개입니다.

### SC_047 · LOC_002_YODONGSEONG (bệnh xá — ken-burns) · 소년 척후, CHAR_004 · — · still_kenburns · 6:08–6:18
[ACTION-VI] Ảnh cận: bàn tay găng nitrile dính máu của 서아 đặt trên trán cậu bé đã nhắm mắt; ánh đèn đội đầu; phía sau mờ, hàng thương binh Goguryeo. Ken-burns đẩy chậm vào hai gương mặt.
[SOUND] thở đều, đèn, xa xa trống Tùy.
N: 삼 주 동안 다섯 병이 고구려 사람에게 갔습니다. 오늘이 여섯 번째였습니다. 서아는 그 셈을 숨기지 않았습니다. 우리 사람과 조상 사이에서 그녀는 매번 아픈 쪽을 골랐습니다. 열두 개. 다음 스무 명의 화살이면 끝이었습니다.

### SC_048 · LOC_003_CHEONDUNG_BASE (bên 천둥 3) · CHAR_106, CHAR_003 · VEH_002, PROP_019 · video8s · 6:18–6:26
[ACTION-VI] Chiều: 을보 đặt lên váy xích 천둥 3 một thanh sắt bẩy dài rèn tay còn ám khói và hai chốt dự phòng; 박기철 (tay dính dầu) cầm lên ướm, gật; 을보 nói câu cũ, nửa đùa; 박기철 chỉ gật, hai bàn tay dầu chắp lại một nhịp.
[SOUND] sắt đặt lên thép, gió.
N: 여분이 생겼습니다. 이 시대의 여분이었습니다. 두 대장장이는 이제 서로의 말을 조금 알았습니다.
을보: 쇠는 쇠요, 쇠쟁이.

### SC_049 · LOC_002_YODONGSEONG (sân trong, chân tường — hoàng hôn) · CHAR_101 (áo choàng, không lộ mặt), CHAR_105, CHAR_001, CHAR_004 · — · video8s · 6:26–6:34
[ACTION-VI] Hoàng hôn hổ phách qua bụi: dưới bóng tường trong, một người áo choàng len đen trùm kín, mũ trùm, gấu áo bụi đường, đứng im nhìn lên 치 nơi cờ trắng đã hạ — không nhìn gì khác. 해모루 từ cổng bước vào, thấy người ấy, dừng lại và cúi rất sâu, lâu. 한승우 và 서아 đi ngang sân với túi quân y, thấy cái cúi đầu ấy; 한승우 chậm bước.
[SOUND] gió, cờ, giáp 해모루 khi cúi.
N: 해모루는 아무에게도 그렇게 절하지 않았습니다. 성주에게도 그러지 않았습니다. 한승우는 그것을 보았습니다.

### SC_050 · LOC_002_YODONGSEONG (sân trong) · CHAR_001, CHAR_105 · — · video8s · 6:34–6:42
[ACTION-VI] Người áo choàng đã đi khuất sau góc tường; 한승우 tới bên 해모루 đang thẳng người dậy, hỏi khẽ, mắt vẫn nhìn theo góc tường.
[SOUND] bước chân xa dần, gió.
N: 질문은 짧았습니다. 그는 이름을 물은 것이 아니었습니다. 왜 저렇게 절하는가를 물은 것이었습니다.
한승우: 말객님, 저분은 누구십니까?

### SC_051 · LOC_002_YODONGSEONG (sân trong) · CHAR_105 · — · video8s · 6:42–6:50
[ACTION-VI] 해모루 nhìn ông một nhịp — lần đầu không nhếch mép; trả lời rồi đi trước về phía dinh, không đợi.
[SOUND] giáp, bước chân trên đất nện.
N: 해모루는 이름을 말하지 않았습니다. 이름을 말할 자리가 따로 있었습니다.
해모루: 성주께서 내일 부르실 것이오. 그때 아시오.

### SC_052 · LOC_002_YODONGSEONG (dọc tường trong, hoàng hôn — ken-burns) · CHAR_101 (áo choàng, lưng), CHAR_105 · — · still_kenburns · 6:50–7:00
[ACTION-VI] Ảnh: người áo choàng đen đi dọc chân tường trong về phía dinh thành chủ, lưng quay về máy, mũ trùm; 해모루 theo sau hai bước; bóng hai người đổ dài trên đá; xa, tháp chùa gỗ ba tầng. Ken-burns kéo ra chậm.
[SOUND] gió, cờ, trống Tùy xa.
N: 그날 저녁, 비밀 통로로 한 사람이 성에 들어왔습니다. 그는 쇠수레를 보러 온 것이 아니었습니다.

[MID-ROLL 1 · 7:00]

[Kết thúc Phần 3]

## [Phần 4] 충차와 한 발 — 「충차와 한 발」 / Cuộc chạm trán đầu tiên  (7:00–10:30)
> Tóm tắt VI: Sau mid-roll: bàn tay người áo choàng chạm đá tường lúc bình minh D27. 전령 về: "받으라" — nhưng tường đã vá, cờ đã hạ; tướng Tùy: "받을 항복이 없다." 1차 공성 thuần cổ 90 s: tháp áp tường, tên lửa không bén da ướt, cầu bập bênh hạ, giao chiến trên mặt tường, 고정수 cầm giáo, nước sôi. 오태민 xin ra — 한승우: "대기. 성이 막고 있다." 충차 húc 옹성 nam, then cổng nứt; 고정수 sai gọi 한승우. PZF-3 từ lỗ châu mai 치 cách 60 m — xe húc nổ tung, tổ phá cổng tan; quân Tùy quanh cổng lùi — lần đầu đại quân Tùy thấy "sấm". Tướng Tùy nhìn thấy khói ở 치. Người áo choàng trên tường cách hai 치: một ngón tay giơ lên. Chiều: Tùy rút; lệnh phủ da + đất ướt lên xe húc mới. 박기철: "열여덟에서 열일곱." 고정수: "그 한 발이 몇 개나 남았소?"
> Chức năng: THREAT + CONTACT · Combat: SC_055–070, SC_072 · Tài nguyên: PZF 18→17 · Enemy adaptation: đất ướt hai lớp lên xe húc · Quyết định lịch sử: 수 공성총관 tự đổi cách bọc xe · Open loop: "성 안의 누군가가 그 한 발을 세고 있었습니다."

### SC_053 · LOC_002_YODONGSEONG (tường trong, bình minh — ken-burns) · CHAR_101 (tay) · — · still_kenburns · 7:00–7:10
[ACTION-VI] Ảnh cận: một bàn tay gầy, gân nổi, ngón trỏ có vết chai dây cung, đặt lên tảng đá granite xám của tường — bên cạnh là tay áo len đen bụi đường; ánh bình minh xiên. Không mặt. Ken-burns đẩy rất chậm vào bàn tay. Không thoại.
[SOUND] gió sớm, chim, xa xa vó ngựa một con.
N: 스물일곱째 새벽. 손 하나가 담을 만졌습니다. 담은 차가웠고, 새로 쌓은 돌은 아직 젖어 있었습니다.

### SC_054 · LOC_002_YODONGSEONG (trại Tùy sau hào, bình minh) · 수 공성총관, 수 전령 · WPN_201 · video8s · 7:10–7:18
[ACTION-VI] Kỵ sứ bụi trắng nhảy xuống ngựa, dâng ống thư; tướng công thành mở, đọc một chữ, ngẩng lên nhìn thành: đoạn tường nứt hôm kia nay là vệt đá sáng phẳng lì, cờ trắng trên 치 đã không còn. Ông vò thẻ lụa trong nắm tay.
[SOUND] ngựa thở, lụa vò, trống bắt đầu nổi.
N: 답은 이틀 만에 왔습니다. 받으라. 담은 이미 서 있었고, 흰 천은 내려가 있었습니다.
수 공성총관: 받으라 하셨다. 헌데 받을 항복이 없다.

### SC_055 · LOC_002_YODONGSEONG (đồng bằng nam, tháp tiến) · lính Tùy · VEH_201 · video8s · 7:18–7:26
[ACTION-VI] Trống dồn: các tháp tám bánh lăn về phía tường — hàng trăm người đẩy càng, bò kéo dây phía trước, da trâu ướt bốc hơi trong nắng sớm; hào đã lấp bằng bao đất thành đường đắp rộng. Aerial thấp lướt ngang hàng tháp.
[SOUND] trống, dây gai, bánh gỗ, bò rống.
[COMBAT]
N: 탑을 앞세운 첫 공성이 시작되었습니다. 흰 천은 더 이상 통하지 않았습니다. 적어도 오늘은.

### SC_056 · LOC_002_YODONGSEONG (mặt tường nam) · CHAR_104, cung thủ Goguryeo · WPN_101, PROP_016 · video8s · 7:26–7:34
[ACTION-VI] Cung thủ Goguryeo bắn tên quấn vải cháy vào mặt tháp — tên cắm vào da trâu ướt, xèo khói, tắt; 고정수 (mũ đội) đứng sau lan can nhìn khói tắt, hàm nghiến.
[SOUND] dây cung, tên lửa rít, xèo tắt.
[COMBAT]
N: 젖은 가죽은 불을 먹었습니다. 불화살 백 개가 연기 백 줄이 되었습니다. 수나라는 요동성의 첫 번째 답을 미리 알고 왔습니다.

### SC_057 · LOC_002_YODONGSEONG (mặt tường nam, tháp áp tường) · lính Tùy, lính Goguryeo · VEH_201 · video8s · 7:34–7:42
[ACTION-VI] Tháp chạm chân tường; cầu bập bênh trên đỉnh đổ sập xuống lan can đá "쾅"; lính Tùy khiên tròn ào qua cầu; giáo Goguryeo đón ở lan can — cận chiến trên mặt tường hẹp, người ngã xuống hai phía. Wide trung, không gore.
[SOUND] cầu gỗ đập đá, khiên, giáo, thét.
[COMBAT]
N: 다리가 내려왔습니다. 담 위는 이제 벌판이었습니다. 창 하나 길이의 벌판이었습니다.

### SC_058 · LOC_002_YODONGSEONG (mặt tường nam) · CHAR_104 · — · video8s · 7:42–7:50
[ACTION-VI] 고정수 tự cầm giáo dài, tấn thẳng vào ngực khiên một lính Tùy đang bước xuống cầu, đẩy ngược hắn lên cầu; tia lửa từ đuốc gãy bén vào áo choàng xám của ông — ông không để ý, giáo lại đâm. Cận nửa người.
[SOUND] giáo va khiên, thở, lửa bén vải.
[COMBAT]
N: 성주는 뒤에 서지 않았습니다. 요동성에서 성주는 첫 번째 창이었습니다. 그것이 이 성이 이백 년을 버틴 방식이었습니다.

### SC_059 · LOC_002_YODONGSEONG (mặt tường nam, cạnh tháp) · lính Goguryeo · VEH_203 · video8s · 7:50–7:58
[ACTION-VI] Nồi nước sôi lớn do bốn người nghiêng đổ qua lan can xuống một thang mây đầy lính; thang rung, người rơi; đá tảng ném theo — thang gãy đôi. Low-angle từ ngoài tường.
[SOUND] nước sôi trút, thét, gỗ gãy.
[COMBAT]
N: 물은 화살보다 쌌습니다. 성 안에는 우물이 셋 있었습니다.

### SC_060 · LOC_003_CHEONDUNG_BASE (nóc 천둥 2) · CHAR_002 · VEH_002, EQP_002 · video8s · 7:58–8:06
[ACTION-VI] Thung lũng: trống và tiếng thét vọng qua đồi; 오태민 đứng thẳng trên nóc 천둥 2, tổ lái đã ngồi vào ghế, động cơ chưa nổ; ông bấm radio, giọng căng.
[SOUND] trống vọng, PTT.
[COMBAT]
N: 골짜기에서는 소리만 들렸습니다. 소리는 오태민을 늘 앞으로 밀었습니다.
오태민: 천둥 지휘, 여기는 천둥 2. 지원 나갑니까?

### SC_061 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001, CHAR_105 · EQP_002 · video8s · 8:06–8:14
[ACTION-VI] 한승우 trên 치 đông-nam với 해모루, ống nhòm nhìn dọc mặt tường nam nơi giao chiến cách 300 m — giáo Goguryeo đang đẩy lính Tùy lùi lên cầu; ông hạ ống nhòm, bấm radio.
[SOUND] PTT, giao chiến xa.
[COMBAT]
N: 담은 막고 있었습니다. 한승우는 그것을 셌습니다. 총이 나가면 총은 다시 들어오지 않습니다.
한승우: 천둥 2, 여기는 천둥 지휘. 대기. 성이 막고 있다.

### SC_062 · LOC_002_YODONGSEONG (đường đắp vào cổng nam 옹성) · lính Tùy · VEH_202 · video8s · 8:14–8:22
[ACTION-VI] Xe phá cổng mái mai rùa bọc da đen lăn lên đường đắp qua hào về phía vòm 옹성 nam; tên Goguryeo cắm vào mái da, đá lăn trượt xuống; bên trong mái, bốn mươi đôi chân đẩy. Tracking theo xe.
[SOUND] bánh gỗ, tên cắm da, hô đẩy trong mái.
[COMBAT]
N: 충차였습니다. 쇠머리를 단 통나무가 가죽 지붕 밑에서 왔습니다. 화살도 돌도 지붕 위로 미끄러졌습니다. 문은 담보다 약했습니다.

### SC_063 · LOC_002_YODONGSEONG (trong 옹성, sau cổng) · lính Goguryeo · — · video8s · 8:22–8:30
[ACTION-VI] Trong vòm 옹성: cánh cổng gỗ bọc sắt rung "쿵" mỗi nhịp húc, bụi rơi từ vòm, then ngang gỗ nứt một đường dài; lính Goguryeo chống thêm cây gỗ vào cổng, đá chèn chân. Cận then nứt.
[SOUND] húc nặng lặp nhịp, gỗ nứt, thở.
[COMBAT]
N: 옹성 안쪽에서 문은 북처럼 울었습니다. 빗장은 참나무 한 아름이었습니다. 그것이 갈라지고 있었습니다.

### SC_064 · LOC_002_YODONGSEONG (tháp cổng nam) · CHAR_104, lính chạy tin · — · video8s · 8:30–8:38
[ACTION-VI] 고정수 (áo choàng cháy thủng một lỗ, khói) trên tháp cổng nhìn xuống then cổng nứt dài thêm; ông nắm vai một lính trẻ, chỉ về phía 치 đông-nam.
[SOUND] húc, bụi, giọng khàn.
[COMBAT]
N: 담은 성주의 것이었습니다. 문은 이제 아니었습니다. 성주는 그것을 인정했습니다.
고정수: 한 대장을 불러라. 지금.

### SC_065 · LOC_002_YODONGSEONG (mặt tường, chạy về cổng nam) · CHAR_001, CHAR_006, 2소대 PZF 사수 · WPN_005 · video8s · 8:38–8:46
[ACTION-VI] 한승우 chạy dọc mặt tường về phía cổng nam, sau ông 백성민 và một lính 2소대 vác ống PZF-3 xanh trên vai; lính Goguryeo nép vào lan can nhường lối; tên Tùy rít qua đầu.
[SOUND] giày trên đá, tên rít, thở.
[COMBAT]
N: 문에서 육십 미터. 치 하나가 문을 내려다보고 있었습니다.

### SC_066 · LOC_002_YODONGSEONG (치 cạnh cổng nam) · CHAR_006, PZF 사수, cung thủ Goguryeo · WPN_005 · video8s · 8:46–8:54
[ACTION-VI] Trên 치: xạ thủ quỳ, đặt ống PZF lên vai nhắm qua lỗ châu mai xuống xe húc; 백성민 quay lại, tay đẩy ngực hai cung thủ Goguryeo đang đứng sau ống, chỉ vào đuôi ống rồi ra hiệu lùi — họ không hiểu nhưng lùi.
[SOUND] PZF khóa cò, giáp, giao chiến xa.
[COMBAT]
N: 뒤로 나가는 불을 이 시대는 몰랐습니다. 백성민은 손으로 설명했습니다.
백성민: 물러서시오. 뒤가 탑니다.

### SC_067 · LOC_002_YODONGSEONG (치 cạnh cổng nam) · CHAR_001, PZF 사수 · WPN_005 · video8s · 8:54–9:02
[ACTION-VI] 한승우 khom sau xạ thủ, nhìn qua lỗ châu mai: mái da đen của xe húc lắc theo nhịp 8 m dưới chân tường; ông đặt tay lên vai xạ thủ.
[SOUND] húc cổng dội lên, thở.
[COMBAT]
N: 열여덟 발 중 하나였습니다. 한승우는 그 하나를 문에 쓰기로 했습니다.
한승우: 한 발이다. 한 발에 끝내.

### SC_068 · LOC_002_YODONGSEONG (치 → xe húc, wide) · — · WPN_005, VEH_202 · video8s · 9:02–9:10
[ACTION-VI] PZF phụt: luồng hậu tống thổi bụi đá tung khỏi 치, vệt khói cắm thẳng xuống mái xe húc — mái da và gỗ bung lên thành mảnh, cây phá cổng đầu sắt gãy rời, bụi trùm đường đắp. Wide từ trên tường.
[SOUND] "쾅" khô, mảnh gỗ rơi rào rào, rồi im lạ.
[COMBAT]
N: 육십 미터. 한 발. 그것으로 충분했습니다.

### SC_069 · LOC_002_YODONGSEONG (đường đắp trước cổng nam) · lính Tùy · VEH_202 · video8s · 9:10–9:18
[ACTION-VI] Lính Tùy sống sót bò ra khỏi xác xe húc cháy, ngã dúi; quanh cổng, hàng khiên Tùy lùi từng bước, đầu ngẩng nhìn lên 치 còn khói; một sĩ quan Tùy giơ đao ra lệnh dừng mà không ai nghe. Wide trung.
[SOUND] lửa, rên, hàng khiên lùi lạo xạo.
[COMBAT]
N: 지난달 동쪽 길에서 천둥을 본 것은 선비 기병 이천이었습니다. 오늘은 수나라 본군 만 명이 보았습니다. 소문이 아니었습니다. 문 앞에서였습니다.

### SC_070 · LOC_002_YODONGSEONG (sau hào, tướng Tùy) · 수 공성총관 · WPN_201 · video8s · 9:18–9:26
[ACTION-VI] Tướng công thành trên ngựa giật cương, ngựa xoay; ông không nhìn xe húc cháy — nhìn lên 치 nơi khói xám còn bay ra từ lỗ châu mai; ông giơ roi chỉ đúng chỗ ấy cho sĩ quan bên cạnh.
[SOUND] ngựa hí, gió, lửa xa.
[COMBAT]
N: 총관은 불을 보지 않았습니다. 연기가 나온 구멍을 보았습니다. 그도 배우는 사람이었습니다.

### SC_071 · LOC_002_YODONGSEONG (tường nam, cách 치 hai 치) · CHAR_101 (áo choàng) · — · video8s · 9:26–9:34
[ACTION-VI] Trên mặt tường, cách hai 치, người áo choàng đen đứng nép lan can giữa lính Goguryeo, mũ trùm; máy trượt xuống bàn tay phải buông dọc thân — ngón trỏ giơ lên, giữ. Không mặt.
[SOUND] giao chiến tan dần, gió.
N: 담 위의 누군가는 문을 보지 않았습니다. 연기도 보지 않았습니다. 그는 손가락 하나를 폈습니다.

### SC_072 · LOC_002_YODONGSEONG (mặt tường nam, chiều) · lính Goguryeo, lính Tùy · VEH_201, VEH_203 · video8s · 9:34–9:42
[ACTION-VI] Chiều muộn: cầu bập bênh cuối bị sào Goguryeo đẩy bật lên; trống Tùy đổi nhịp — lính Tùy khiêng thang lùi qua hào, tháp bị kéo ngược chậm chạp; trên tường, lính Goguryeo ngồi sụp xuống lan can, không reo. Wide.
[SOUND] trống rút, thang kéo, thở dốc.
[COMBAT]
N: 첫 번째 공성은 해와 함께 끝났습니다. 탑 하나가 담에 닿았고, 문 하나가 갈라졌습니다. 성은 섰습니다. 값은 나중에 셀 것이었습니다.

### SC_073 · LOC_002_YODONGSEONG (bãi đóng xe Tùy, hoàng hôn) · 수 공성총관, thợ Tùy · VEH_202 · video8s · 9:42–9:50
[ACTION-VI] Bãi thợ: khung xe húc mới đang đóng; tướng công thành đi vòng quanh, đá chân vào mái da, quay sang thợ cả, ra lệnh; thợ nhìn nhau rồi chạy đi lấy giỏ.
[SOUND] búa, gỗ, giọng tướng.
N: 그는 원인을 몰랐습니다. 하지만 답을 몰라도 대비는 할 수 있었습니다. 수나라는 큰 나라였습니다. 큰 나라는 빨리 배웠습니다.
수 공성총관: 다음 충차엔 젖은 흙을 덮어라. 두 겹으로.

### SC_074 · LOC_002_YODONGSEONG (bãi thợ Tùy, đêm — ken-burns) · thợ Tùy · VEH_202 · still_kenburns · 9:50–10:02
[ACTION-VI] Ảnh: đêm, đuốc; hàng chục thợ Tùy xúc bùn ướt từ hào đổ lên mái xe húc mới đã phủ chiếu rơm, đắp thành lớp dày; xa hơn, các tháp cũng đang được phủ. Ken-burns trượt từ xe húc ra hàng tháp.
[SOUND] xẻng, bùn, hô lệnh đêm.
N: 그날 밤 수나라는 흙을 팠습니다. 가죽 위에 거적을 깔고, 거적 위에 진흙을 얹었습니다. 불에도, 그리고 아직 이름을 모르는 것에도 대비하기 위해서였습니다. 성 안의 한 발이 성 밖의 흙 만 삽이 되었습니다.

### SC_075 · LOC_003_CHEONDUNG_BASE (lều chỉ huy, bảng đếm) · CHAR_003, PZF 사수 · WPN_005 · video8s · 10:02–10:10
[ACTION-VI] Đêm, đèn đỏ: xạ thủ 2소대 dựng ống PZF rỗng vào giá; 박기철 lấy phấn xóa số 18 trên bảng gỗ, viết 17; nói với xạ thủ mà như nói với bảng.
[SOUND] phấn trên gỗ, ống rỗng chạm giá.
N: 열일곱. 박기철에게 그 한 발은 값이 쌌습니다. 수레 하나에 한 발. 문 하나에 한 발. 그는 그 계산을 좋아했습니다.
박기철: 열여덟에서 열일곱. 한 발에 수레 하나.

### SC_076 · LOC_002_YODONGSEONG (mặt tường nam, đêm) · CHAR_104, CHAR_001 · — · video8s · 10:10–10:18
[ACTION-VI] Walk-and-talk: 고정수 (băng vải quấn trán dưới khăn, áo choàng thủng) và 한승우 đi dọc mặt tường qua chỗ cầu bập bênh để lại vết vỡ trên lan can; dưới chân tường, xác xe húc còn cháy âm ỉ. 고정수 dừng, nhìn xuống, hỏi không nhìn ông.
[SOUND] bước chân, lửa âm ỉ dưới tường.
N: 성주는 고맙다고 하지 않았습니다. 지난달과 같았습니다. 그는 묻는 사람이었습니다.
고정수: 한 발로 문을 지켰소. 그 한 발이 몇 개나 남았소?

### SC_077 · LOC_002_YODONGSEONG (치 tường nam, đêm — ken-burns) · CHAR_101 (bóng áo choàng) · VEH_202 · still_kenburns · 10:18–10:30
[ACTION-VI] Ảnh: đêm, bóng người áo choàng đứng một mình trên 치, một tay đặt lên lan can đá, mũ trùm; xa dưới đường đắp, xác xe húc là đốm lửa nhỏ; đồng bằng phía sau là biển lửa trại Tùy. Ken-burns đẩy chậm từ biển lửa vào bóng người.
[SOUND] gió, lửa xa, im.
N: 한승우는 대답하지 않았습니다. 열일곱이라는 숫자는 아직 그의 것이었습니다. 하지만 그 숫자를 세는 사람은 그만이 아니었습니다. 성 안의 누군가가 그 한 발을 세고 있었습니다.

[Kết thúc Phần 4]

## [Phần 5] 열 발에 둘 — 「열 발에 둘」 / Chứng minh sức mạnh  (10:30–14:00)
> Tóm tắt VI: Sáng D28, đại sảnh: 고정수 ĐỨNG; người áo choàng nay mặc giáp trơn không lông chỏm ngồi dưới ghế thành chủ. Câu đầu khi đại đội bước vào: "쇠수레는 며칠이나 달릴 수 있소?" 박기철: "달리면 닷새. 안 움직이면 한 달." Ông hỏi tiếp "우는 쇠" (cối): "백십 발입니다. 백이십 발로 왔습니다." 고정수 mới xưng tên: 대장군 을지문덕. 한승우 biết cái tên ấy. Thử: "저 탑들을 가장 적은 화살로 부수시오." 오태민: K2, mỗi tháp 1 viên. 한승우 chọn cối — rẻ, bắn từ sau đồi, K2 vẫn giấu. Cối đăng ký 2 viên (백성민 chỉnh từ tường), 을보: "탑은 속에서 타. 꼭대기를 쳐." 8 viên → 2 tháp cháy từ tầng trên. 을지문덕 đếm to: "열 발에 둘. 그럼 스무 개엔 백 발이오. 마흔이면 이백 발. 그대들은 백십 발이라 했소." 박기철: "이제 백 발입니다." 오태민: "전차면 두 발입니다." Đêm: Tùy kéo tháp lùi 6리, phủ chiếu đất ướt, đóng thêm. Bình minh D29: "탑이 다시 마흔입니다." 을지문덕: "쇠는 세면 줄고, 나무는 베면 는다."
> Chức năng: BATTLE nhỏ / DEMO · Combat: SC_086–092 · Tài nguyên nói thành lời: cối 110→100 ("백십 발", "이제 백 발"), "닷새 / 한 달" · Quyết định lịch sử: 을지문덕 thử bằng "ít đạn nhất"; 수 공성총관 lùi ngoài tầm + phủ đất + nhân bản tháp · Open loop: "쇠는 세면 줄고, 나무는 베면 는다." → [MID-ROLL 2 · 14:00]

### SC_078 · LOC_002_YODONGSEONG (đại sảnh dinh thành chủ, sáng) · CHAR_101, CHAR_104, CHAR_001, CHAR_003, CHAR_002, CHAR_105 · — · video8s · 10:30–10:38
[ACTION-VI] Đại sảnh gỗ, nắng xiên qua cửa lưới: 고정수 ĐỨNG cạnh ghế thành chủ trống; dưới ghế, trên chiếu, một người ngồi — giáp lamellar trơn không lông chỏm, râu bạc ngắn, ống đựng thư ở thắt lưng; 해모루 đứng sau ông. 한승우, 박기철, 오태민 bước vào, chưa kịp cúi chào — người ấy hỏi ngay, không ngẩng nhìn hết mặt họ.
[SOUND] sàn gỗ, giáp, gió qua cửa.
N: 그는 이름을 말하지 않았습니다. 어디서 왔는지도 묻지 않았습니다. 첫 질문은 쇠수레였습니다. 정확히는, 쇠수레의 날수였습니다.
을지문덕: 쇠수레는 며칠이나 달릴 수 있소?

### SC_079 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_003, CHAR_001 · — · video8s · 10:38–10:46
[ACTION-VI] 박기철 liếc 한승우 — 한승우 gật một li; 박기철 trả lời, tay vô thức sờ giẻ đỏ ở thắt lưng như sờ que đo dầu.
[SOUND] im, gió.
N: 박기철은 그 답을 매일 아침 준비해 두고 있었습니다. 묻는 사람이 없었을 뿐입니다. 한 달은 발전기의 수였습니다. 전차가 아니라 부대의 눈과 귀의 수였습니다.
박기철: 달리면 닷새. 안 움직이면 한 달.

### SC_080 · LOC_002_YODONGSEONG (đại sảnh → hiên) · CHAR_101 · — · video8s · 10:46–10:54
[ACTION-VI] Người ấy gật một cái, đứng dậy — cao gầy, lưng thẳng — đi ra hiên gỗ nhìn qua sân về phía tường nam nơi tiếng "퉁" cối tập hôm trước còn trong trí; ông hỏi câu thứ hai với lưng quay về họ.
[SOUND] sàn gỗ, cờ 삼족오 lay ngoài hiên.
N: 그는 놀라지 않았습니다. 궁금해하지도 않았습니다. 그는 셌습니다.
을지문덕: 그 우는 쇠는 몇 발이나 남았소?

### SC_081 · LOC_002_YODONGSEONG (hiên dinh) · CHAR_003 · — · video8s · 10:54–11:02
[ACTION-VI] 박기철 bước ra hiên theo, đứng cách ông hai bước, đáp không cần mở sổ; 오태민 sau lưng nhíu mày vì ông trả lời người lạ mọi thứ.
[SOUND] gió, xa xa búa Tùy.
N: 백십. 지난달 여울에서 열 발이 줄어든 수였습니다. 박기철은 숨기지 않았습니다.
박기철: 백십 발입니다. 백이십 발로 왔습니다.

### SC_082 · LOC_002_YODONGSEONG (hiên dinh) · CHAR_104, CHAR_001 · — · video8s · 11:02–11:10
[ACTION-VI] 고정수 bước tới bên cạnh, cúi đầu về phía người ấy rồi nói với 한승우 — lần đầu dùng 합쇼 với ai đó trước mặt đại đội. 한승우 nghe tên: lưng thẳng lên, cằm hạ xuống nửa tấc — như trước quốc kỳ. 오태민 nhìn 한승우, không hiểu vì sao.
[SOUND] gió, cờ.
N: 한승우는 그 이름을 알았습니다. 대한민국 사람이면 누구나 알았습니다. 천사백 년 뒤의 교과서에 있는 이름이었습니다. 그 이름이 두 걸음 앞에 서 있었습니다.
고정수: 대장군 을지문덕이시오. 대왕의 명으로 오셨소.

### SC_083 · LOC_002_YODONGSEONG (hiên dinh) · CHAR_101, CHAR_001 · — · video8s · 11:10–11:18
[ACTION-VI] 을지문덕 không nhận cái cúi đầu; ông giơ tay chỉ qua mái nhà về phía nam — nơi 38 tháp đứng cách tường một dặm rưỡi — rồi nhìn thẳng 한승우 lần đầu.
[SOUND] gió, trống Tùy xa.
N: 그는 인사를 받지 않았습니다. 시험을 냈습니다.
을지문덕: 저 탑들을 가장 적은 화살로 부수시오.

### SC_084 · LOC_002_YODONGSEONG (mặt tường nam — walk-and-talk) · CHAR_002, CHAR_001 · — · video8s · 11:18–11:26
[ACTION-VI] Ba người đại đội đi nhanh dọc mặt tường về 치 đông-nam; 오태민 đi sát 한승우, tay chém không khí về phía hàng tháp cách 1,5 km.
[SOUND] giày trên đá, gió.
N: 오태민의 답은 이번에도 하나였습니다. 그리고 이번에는 그 답이 틀리지 않았습니다.
오태민: 전차입니다. 탑 하나에 한 발.

### SC_085 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001, CHAR_003 · — · video8s · 11:26–11:34
[ACTION-VI] 한승우 dừng ở 치, nhìn hàng tháp, rồi quay đầu nhìn về dải đồi phía đông nơi thung lũng nằm khuất; ông nói với 박기철 nhưng mắt vẫn ở đồi.
[SOUND] gió, cờ.
N: 전차 한 발은 탑 하나였습니다. 그리고 전차 한 발은 전차의 자리였습니다. 골짜기가 드러나면 다음 밤은 없었습니다. 박격포는 언덕 뒤에서 울었습니다.
한승우: 박격포. 전차는 숨긴 채로 간다.

### SC_086 · LOC_003_CHEONDUNG_BASE (hố cối) · 사수, tổ cối · WPN_002 · video8s · 11:34–11:42
[ACTION-VI] Chiều: hố cối trên gò; xạ thủ đọc bảng tính, chỉnh góc nòng cao — tầm xa nhất; tổ viên nâng đạn; radio đặt trên bao cát.
[SOUND] chỉnh ốc nòng, radio rè.
[COMBAT]
N: 골짜기에서 탑까지는 이천 미터가 넘었습니다. 박격포는 언덕 너머를 볼 수 없었습니다. 눈은 담 위에 있었습니다.
사수: 1번 포, 사격 제원 입력. 두 발.

### SC_087 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_006 · PROP_006, EQP_002 · video8s · 11:42–11:50
[ACTION-VI] Trên 치: hai cột đất bùng lên cách chân tháp gần nhất vài chục mét, lệch trái; 백성민 ống nhòm, bấm radio, giọng điện tín.
[SOUND] hai tiếng nổ xa dội, PTT.
[COMBAT]
N: 첫 두 발은 겨냥이었습니다. 눈은 담 위에, 손은 골짜기에 있었습니다.
백성민: 포반, 여기는 고지. 우로 오십, 증가 백.

### SC_088 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_106, CHAR_001 · — · video8s · 11:50–11:58
[ACTION-VI] 을보 (lên tường theo xem, tạp dề da) nắm tay áo 한승우 kéo, chỉ lên đỉnh tháp — sàn trên, nơi gỗ khô không có da bọc — rồi chỉ vào bụng mình.
[SOUND] gió, tiếng 을보 khàn.
[COMBAT]
N: 을보는 탑을 만드는 사람은 아니었습니다. 하지만 나무를 아는 사람이었습니다. 가죽은 밖에 있었습니다. 마른 나무는 안에 있었습니다.
을보: 탑은 속에서 타. 꼭대기를 쳐, 대장 양반.

### SC_089 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001 · EQP_002 · video8s · 11:58–12:06
[ACTION-VI] 한승우 nhìn đỉnh tháp một nhịp, bấm radio.
[SOUND] PTT, gió.
[COMBAT]
N: 여덟 발. 대장장이의 말이 포격 제원이 되었습니다.
한승우: 포반, 여기는 천둥 지휘. 탑 꼭대기. 여덟 발.

### SC_090 · LOC_003_CHEONDUNG_BASE (hố cối) · tổ cối · WPN_002 · video8s · 12:06–12:14
[ACTION-VI] Hai khẩu cối bắn liên tiếp — bốn viên mỗi khẩu, chớp cam, xạ thủ thả đạn không nhìn, vỏ hộp đạn rỗng ném ra sau.
[SOUND] "퉁, 퉁, 퉁, 퉁" dồn.
[COMBAT]
N: 여덟 발. 지난달 여울에서 쓴 것과 같은 수였습니다.

### SC_091 · LOC_002_YODONGSEONG (hàng tháp, tầng trên) · lính Tùy · VEH_201 · video8s · 12:14–12:22
[ACTION-VI] Đạn cối nổ trên sàn tầng ba, tầng bốn của hai tháp gần nhau: gỗ khô vỡ tung, một tấm da tuột rơi; trong lòng tháp, lửa bén vào thang gỗ khô; lính Tùy tầng dưới nhảy ra. Trung cảnh từ tường.
[SOUND] nổ trên cao, gỗ vỡ, lửa bén, thét.
[COMBAT]
N: 가죽은 젖어 있었습니다. 사다리는 말라 있었습니다. 불은 안에서 시작되었습니다. 을보의 말대로였습니다.

### SC_092 · LOC_002_YODONGSEONG (hàng tháp, wide) · lính Tùy, lính Goguryeo · VEH_201 · video8s · 12:22–12:30
[ACTION-VI] Hai tháp cháy từ đỉnh xuống như hai bó đuốc khổng lồ giữa hàng tháp; người đẩy tản ra; máy lia từ tháp về mặt tường: lính Goguryeo bắt đầu giơ giáo — và dừng ở một người không reo, đang giơ bàn tay lên trước mặt. Wide → pan.
[SOUND] lửa lớn, gỗ gãy, reo hò bắt đầu rồi chìm vào gió.
[COMBAT]
N: 담 위가 환호했습니다. 을지문덕은 아니었습니다.

### SC_093 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101 · — · video8s · 12:30–12:38
[ACTION-VI] 을지문덕 (giáp trơn, không lông) đứng ở lan can 치 nhìn hai tháp cháy, không cười; ông giơ bàn tay, gập từng ngón, đếm to cho những người quanh nghe.
[SOUND] lửa xa, reo hò, giọng ông đều.
[COMBAT]
N: 그는 불을 오래 보지 않았습니다. 그는 손가락을 폈습니다.
을지문덕: 열 발에 둘. 그럼 스무 개엔 백 발이오.

### SC_094 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101, CHAR_003 · — · video8s · 12:38–12:46
[ACTION-VI] Ông tiếp, bàn tay thứ hai mở ra; rồi quay đầu nhìn 박기철 đang đứng sau 한승우.
[SOUND] gió, lửa.
N: 그는 셈을 끝까지 했습니다. 탑 마흔과 우는 쇠 백십. 답은 모자란다였습니다.
을지문덕: 마흔이면 이백 발. 그대들은 백십 발이라 했소.

### SC_095 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_003, CHAR_101 · — · video8s · 12:46–12:54
[ACTION-VI] 박기철 (một nhịp, rồi như sửa sổ): trả lời. Khóe miệng 을지문덕 nhích một li — lần đầu. 한승우 nhìn hai người.
[SOUND] gió, reo hò tắt dần.
N: 두 사람이 세고 있었습니다. 하나는 기름과 탄약을, 하나는 날과 나무를. 을지문덕은 박기철보다 빨랐습니다. 박기철은 정확했습니다.
박기철: 이제 백 발입니다.

### SC_096 · LOC_002_YODONGSEONG (치 đông-nam, lan can) · CHAR_002, CHAR_001 · — · video8s · 12:54–13:02
[ACTION-VI] 오태민 tựa lan can bên 한승우, nói khẽ, mắt ở hai tháp cháy — không phải cãi, chỉ ghi lại.
[SOUND] lửa xa, gió.
N: 오태민도 틀리지 않았습니다. 그것이 문제였습니다. 맞는 답이 둘일 때, 값이 정합니다.
오태민: 전차면 두 발입니다. 두 발.

### SC_097 · LOC_002_YODONGSEONG (hàng tháp, hoàng hôn — ken-burns) · — · VEH_201 · still_kenburns · 13:02–13:12
[ACTION-VI] Ảnh: hoàng hôn, hai khung tháp cháy đen còn bốc khói giữa hàng ba mươi tám tháp nguyên vẹn; bóng tháp đổ dài về phía thành. Ken-burns kéo ra từ hai xác tháp ra toàn hàng.
[SOUND] lửa tàn, gió chiều, trống Tùy nhịp chậm.
N: 그날의 셈은 이랬습니다. 열 발에 탑 둘. 남은 탑 서른여덟. 남은 우는 쇠 백 발. 한승우는 이겼습니다. 을지문덕은 아직 아무 말도 하지 않았습니다.

### SC_098 · LOC_002_YODONGSEONG (đồng bằng nam, đêm) · 수 공성총관, lính Tùy · VEH_201 · video8s · 13:12–13:20
[ACTION-VI] Đêm: hàng nghìn người kéo dây thừng, bò gồng — các tháp lùi ngược từng thước dưới đuốc; tướng công thành đứng bên một cột mốc gỗ mới cắm, tay cầm dây đo, ra lệnh.
[SOUND] dây thừng, bò, bánh gỗ lùi, giọng tướng.
N: 수나라는 그날 밤 탑을 뒤로 끌었습니다. 우는 쇠가 닿은 자리에서 여섯 리. 닿지 않는 자리까지였습니다.
수 공성총관: 성에서 여섯 리 밖으로 물려라. 흙을 덮어라.

### SC_099 · LOC_002_YODONGSEONG (bãi tháp Tùy, đêm) · thợ Tùy · VEH_201 · video8s · 13:20–13:28
[ACTION-VI] Thợ Tùy trải chiếu rơm ngâm bùn lên đỉnh và mặt tháp, đắp đất ướt; cạnh đó, khung tháp mới dựng từ gỗ rừng vừa đốn, búa gõ suốt đêm. Tracking ngang.
[SOUND] búa, bùn, đuốc.
N: 젖은 흙은 불도 막고 쇳덩이도 받았습니다. 그리고 숲은 아직 남아 있었습니다. 탑 둘이 탄 자리에 탑 둘이 올라갔습니다.

### SC_100 · LOC_002_YODONGSEONG (aerial bình minh — ken-burns) · — · VEH_201 · still_kenburns · 13:28–13:40
[ACTION-VI] Ảnh aerial bình minh D29: bốn mươi bóng tháp màu đất xếp hàng cách thành xa hơn hẳn hôm trước, mặt trước phủ chiếu bùn; giữa thành và tháp là dải cỏ nát rộng; trại Tùy phía sau. Ken-burns trượt dọc hàng tháp.
[SOUND] gió trên cao, chim, trống buổi sáng.
N: 스물아홉째 새벽. 탑은 멀어졌고, 색이 바뀌었고, 수가 돌아왔습니다. 쇠 한 발은 돌아오지 않았습니다. 나무는 돌아왔습니다.

### SC_101 · LOC_002_YODONGSEONG (치 đông-nam, bình minh) · CHAR_006 · PROP_006 · video8s · 13:40–13:48
[ACTION-VI] 백성민 ống nhòm, đếm bằng môi không tiếng, hạ ống nhòm; báo 한승우 đứng bên với giọng không đổi.
[SOUND] gió, ống nhòm.
N: 하룻밤이었습니다. 지난 저녁의 서른여덟이 마흔이 되어 있었습니다.
백성민: 탑이 다시 마흔입니다.

### SC_102 · LOC_002_YODONGSEONG (치 đông-nam, bình minh — ken-burns) · CHAR_101 · — · still_kenburns · 13:48–14:00
[ACTION-VI] Ảnh: 을지문덕 nghiêng mặt ở lan can 치 trong ánh bình minh, nhìn hàng bốn mươi tháp màu đất; lính Goguryeo và lính Hàn mờ phía sau. Ken-burns đẩy chậm vào mắt ông. Giọng ông ngoài hình.
[SOUND] gió, im.
N: 그가 처음으로 자기 생각을 말했습니다. 쇠수레에 대한 말이 아니었습니다. 이 전쟁 전체에 대한 말이었습니다.
을지문덕: 쇠는 세면 줄고, 나무는 베면 는다.

[MID-ROLL 2 · 14:00]

[Kết thúc Phần 5]

## [Phần 6] 황제를 죽이면 — 「황제를 죽이면」 / Liên minh không dễ  (14:00–17:30)
> Tóm tắt VI: Sau mid-roll: aerial 40 tháp phủ đất (không thoại). Chiều tối D29: 서아 học 을보 sắc thuốc bên bếp, tháo khăn olive quàng cho 아리; 아리 dạy 태오 vạch dấu thợ rèn của 을보 trên đất bên giếng. Đêm, đại sảnh: 을지문덕 — xe sắt phải là một quân cờ: "혼자 움직이는 말은 판을 망치오." 한승우: "명령은 못 받습니다. 임무는 받겠습니다." Ông không cãi — hỏi: "오늘 저녁은 무엇을 먹었소?" Im lặng (bát kê). 고정수: chiếu vua nói họ thuộc về thành. 한승우: "우리 것이 아닙니다. 그렇다고 왕의 것도 아닙니다." Tên lửa Tùy bắn qua tường vào thành — dân dập lửa, 태오 múc nước bằng mũ, cung thủ Goguryeo bắn trả (mini-combat). 해모루 báo hoàng đế sắp tới thành. 오태민: dùng K2 bắn hành doanh. 을지문덕: "황제를 죽이면 백만이 돌아가겠소, 아니면 백만이 미치겠소?" Tin trinh sát: Tùy trên đường đang đói — tiếp vận 탁군–요하 sụp, xe bò đi không về [史 수서]. Thỏa hiệp: nhiệm vụ qua 해모루, K2 do 한승우 quyết. 박기철 tưới nước lưới K2 (thói quen). 을지문덕 với 해모루: "저들은 오래 못 버티오. 그러니 오래 쓸 데를 찾아야 하오." Ngón tay ông dừng trên bản đồ ở một con sông phía nam.
> Chức năng: POLITICS · Combat mini: SC_113–115 · Tài nguyên: — (đòn bẩy bữa ăn) · Quyết định lịch sử: 을지문덕 từ chối đánh hoàng đế, đặt cơ chế "nhiệm vụ qua 해모루" · Open loop: "저들은 오래 못 버티오. 그러니 오래 쓸 데를 찾아야 하오."

### SC_103 · LOC_002_YODONGSEONG (aerial ban ngày — ken-burns) · — · VEH_201 · still_kenburns · 14:00–14:10
[ACTION-VI] Ảnh aerial: bốn mươi tháp phủ chiếu bùn màu đất xếp hàng cách thành 2,5 km, chiếu bùn khô nứt trong nắng; giữa các tháp, khung tháp mới trần gỗ; bãi rừng trọc phía sau. Ken-burns trượt chậm. Không thoại.
[SOUND] gió, búa xa, trống nhịp chậm.
N: 흙을 뒤집어쓴 탑 마흔이 이천오백 미터 밖에 섰습니다. 우는 쇠가 닿지 않는 거리였습니다. 수나라는 하루 만에 답을 냈습니다. 답은 흙과 거리와 나무였습니다.

### SC_104 · LOC_003_CHEONDUNG_BASE (bếp Goguryeo, chiều tối) · CHAR_004, CHAR_106, CHAR_107 · — · video8s · 14:10–14:18
[ACTION-VI] Bếp đá ngoài lều gai: 을보 khuấy nồi đất sắc thuốc, chỉ vào từng nắm rễ; 서아 (tay áo khô máu, tóc xổ) ghi vào sổ nhỏ; 아리 ngồi bên rùng mình vì gió khe — 서아 tháo khăn quân đội olive ở cổ mình, quàng và thắt quanh cổ 아리, siết nút. 아리 sờ khăn.
[SOUND] lửa, nồi sôi, gió.
N: 서아는 약초 이름을 외웠습니다. 을보는 값을 받지 않았습니다. 대신 손녀에게 목도리 하나가 생겼습니다. 이 땅에 없는 색이었습니다.
아리: 언니… 이거 언니 건데요.

### SC_105 · LOC_002_YODONGSEONG (sân giếng trong thành, chiều tối) · CHAR_107, CHAR_005 · — · video8s · 14:18–14:26
[ACTION-VI] Bên giếng đá: 아리 (khăn olive) dùng que vạch lên đất nện dấu thợ rèn của ông cô — ký hiệu 을보 khắc lên mọi lưỡi sắt — rồi vạch tên mình; 태오 quỳ, copy méo xẹo; cô bé cười, xóa bằng bàn chân, vẽ lại; drone #3 trong hộp bên cạnh cậu.
[SOUND] que trên đất, cười khẽ, gàu giếng.
N: 을보가 가르친 글자였습니다. 대장장이는 쇠에 이름을 새겼습니다. 태오는 스물한 살이었습니다. 이 땅의 글자를 배우는 첫 번째 대한민국 군인이었습니다. 선생은 열다섯 살이었습니다.
아리: 오라버니, 그건 삐뚤어요. 다시요.

### SC_106 · LOC_002_YODONGSEONG (đại sảnh, đêm) · CHAR_101, CHAR_001, CHAR_002, CHAR_104, CHAR_105, CHAR_003 · — · video8s · 14:26–14:34
[ACTION-VI] Đêm, đèn dầu: bản đồ da trên bàn thấp; 을지문덕 ngồi, đặt lên bản đồ một quân cờ gỗ nhỏ ở chỗ thung lũng phía đông thành; 한승우 ngồi đối diện; 고정수, 해모루, 박기철, 오태민 quanh bàn — 오태민 đứng.
[SOUND] quân cờ đặt xuống gỗ, lửa đèn.
N: 그날 밤 을지문덕은 판을 폈습니다. 판 위에는 성 하나, 골짜기 하나, 그리고 말 하나가 있었습니다. 말은 쇠수레였습니다.
을지문덕: 혼자 움직이는 말은 판을 망치오.

### SC_107 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_001 · — · video8s · 14:34–14:42
[ACTION-VI] 한승우 nhìn quân cờ, không chạm; ngẩng lên, giọng thấp, 하십시오체 nhưng không lùi.
[SOUND] lửa đèn.
N: 한승우는 명령이라는 말을 골랐습니다. 아흔네 명은 대한민국의 군인이었습니다. 그것은 바꿀 수 없었습니다. 임무는 달랐습니다.
한승우: 명령은 못 받습니다. 임무는 받겠습니다.

### SC_108 · LOC_002_YODONGSEONG (sân giếng, đêm) · CHAR_005, CHAR_107 · — · video8s · 14:42–14:50
[ACTION-VI] Insert: sân giếng dưới đèn lồng — chữ vạch trên đất nện còn đó; 태오 ngồi bậc giếng lau kính drone, 아리 gà gật tựa cột với khăn olive; một lính Goguryeo vác bó tên đi ngang, ngoái nhìn cái hộp lạ. Không thoại.
[SOUND] dế, giáp xa, gió.
N: 대청 밖에서는 아무도 판을 몰랐습니다. 그들은 글자와 쇠새와 잠을 나눴습니다.

### SC_109 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_101 · — · video8s · 14:50–14:58
[ACTION-VI] 을지문덕 không cãi; ông cầm bát gốm kê nguội trên bàn cạnh khuỷu tay 한승우, đẩy nhẹ về phía ông, hỏi bằng giọng bình thản nhất tối nay.
[SOUND] bát gốm trượt trên gỗ.
N: 그는 명령과 임무를 가르지 않았습니다. 다른 것을 물었습니다. 저녁이었습니다.
을지문덕: 그대들, 오늘 저녁은 무엇을 먹었소?

### SC_110 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_003, CHAR_002, CHAR_001 · — · video8s · 14:58–15:06
[ACTION-VI] Im lặng. Cận: bát kê Goguryeo, thìa gỗ; 박기철 nhìn xuống hai bàn tay; 오태민 siết hàm; 한승우 không rời mắt khỏi bát. Không ai trả lời.
[SOUND] lửa đèn, một tiếng dế.
N: 삼 주 동안 아흔네 명은 고구려의 조를 먹었습니다. 전투식량은 스무 날 전에 끝났습니다. 대답은 필요 없었습니다. 먹이는 자가 판의 주인이었습니다. 을지문덕은 그것을 굳이 말하지 않았습니다.

### SC_111 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_104 · PROP_013 · video8s · 15:06–15:14
[ACTION-VI] 고정수 đặt ống tre đen chứa chiếu chỉ lên bàn (chiếu 1화), tay đặt lên ống; nói với 한승우, không nặng lời nhưng chắc.
[SOUND] ống tre trên gỗ.
N: 성주는 지난달의 글을 꺼냈습니다. 성과 함께 죽으라. 그 글에 성주는 이 부대를 넣어 두었습니다.
고정수: 대왕의 글은 그대들도 성의 것이라 하오.

### SC_112 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_001 · PROP_013 · video8s · 15:14–15:22
[ACTION-VI] 한승우 nhìn ống tre, rồi nhìn 을지문덕 — trả lời câu của 고정수 nhưng nói với người ngồi đối diện.
[SOUND] lửa đèn.
N: 그것은 그날 밤 가장 위험한 문장이었습니다. 왕의 것이 아니라는 말은 이 시대에 없는 말이었습니다.
한승우: 우리 것이 아닙니다. 그렇다고 왕의 것도 아닙니다.

### SC_113 · LOC_002_YODONGSEONG (tường nam → mái kho, đêm) · — · PROP_016 · video8s · 15:22–15:30
[ACTION-VI] Cắt: đêm trên tường nam — một mũi tên lửa vẽ đường cong đỏ qua lan can, rơi xuống mái rơm một nhà kho nhỏ cạnh kho lương; lửa bén mái. Tiếp hai, ba mũi nữa cắm sân. Low-angle từ sân.
[SOUND] tên lửa rít, rơm bén lửa, tiếng hô "불이야!".
[COMBAT]
N: 그날 밤부터 수나라는 밤마다 불화살을 넘겼습니다. 성을 태우기 위해서가 아니었습니다. 성이 자지 못하게 하기 위해서였습니다.

### SC_114 · LOC_002_YODONGSEONG (sân kho lương, đêm) · dân Goguryeo, CHAR_005, CHAR_107 · — · video8s · 15:30–15:38
[ACTION-VI] Dân và lính chuyền chum nước lên mái kho cháy; 태오 múc nước giếng bằng mũ sắt hắt lên mái; 아리 kéo một đứa bé khỏi tàn lửa rơi; một mũi tên lửa nữa cắm xuống sân cách họ ba bước. Tracking.
[SOUND] nước, lửa, thét, tên cắm đất.
[COMBAT]
N: 물은 우물 셋에서 왔습니다. 손은 삼천 명에게서 왔습니다. 밤마다 그랬습니다.

### SC_115 · LOC_002_YODONGSEONG (tường nam, đêm) · cung thủ Goguryeo · WPN_101 · video8s · 15:38–15:46
[ACTION-VI] Trên tường: cung thủ Goguryeo bắn trả vào bóng tối phía hào nơi vài chấm lửa lóe — một cung thủ trúng tên ngã vào lan can, đồng đội kéo xuống; tên lửa Tùy thưa dần. Wide trung.
[SOUND] dây cung, tên rít hai chiều, rên.
[COMBAT]
N: 매일 밤 두세 명이 담에서 내려왔습니다. 화살은 병실로 갔습니다. 병실은 서아의 것이었습니다.

### SC_116 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_105, CHAR_101 · — · video8s · 15:46–15:54
[ACTION-VI] 해모루 bước vào từ ngoài, khói bám giáp, cúi báo với 을지문덕 — tin từ trinh sát vừa về bằng đường bí mật.
[SOUND] cửa gỗ, giáp, khói.
N: 소식은 산길로 왔습니다. 을지문덕이 들어온 길이었습니다.
해모루: 장군, 황제가 성 앞으로 온답니다. 보름 안입니다.

### SC_117 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_002 · — · video8s · 15:54–16:02
[ACTION-VI] 오태민 bước tới bàn, ngón tay đặt xuống bản đồ phía tây thành — chỗ hoàng đế sẽ đóng; nói với 한승우 nhưng đủ to cho cả sảnh.
[SOUND] ngón tay gõ da.
N: 오태민은 지도 위에서 가장 큰 것을 찾았습니다. 그것이 그의 방식이었습니다.
오태민: 그럼 전차로 황제 행영을 칩니다. 한 발이면 됩니다.

### SC_118 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_101 · — · video8s · 16:02–16:10
[ACTION-VI] 을지문덕 nhìn ngón tay 오태민 trên bản đồ, không gạt ra; ngẩng lên nhìn thẳng anh, hỏi chậm, từng chữ.
[SOUND] lửa đèn, im.
N: 그는 화를 내지 않았습니다. 셈을 물었습니다. 백만이라는 수를 어느 쪽으로 움직일 것인가.
을지문덕: 황제를 죽이면 백만이 돌아가겠소, 아니면 백만이 미치겠소?

### SC_119 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_002, CHAR_001, CHAR_101 · — · video8s · 16:10–16:18
[ACTION-VI] 오태민 mở miệng — không có câu trả lời; rút ngón tay khỏi bản đồ. 한승우 nhìn bản đồ: ngón tay 을지문덕 gõ nhẹ lên con đường từ 요하 tới thành. Cận bàn tay gõ.
[SOUND] gõ da ba nhịp.
N: 한승우는 대답을 알았습니다. 그가 두려워하던 것이 바로 그것이었습니다. 역사가 이긴 싸움을 총 한 발로 망치는 것. 을지문덕은 그 두려움을 한 문장으로 말했습니다.

### SC_120 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_101 · — · video8s · 16:18–16:26
[ACTION-VI] 을지문덕 lấy từ ống thư ở thắt lưng một thẻ tre nhỏ, đặt lên đường từ 요하 trên bản đồ; nói tin trinh sát như đọc thời tiết.
[SOUND] thẻ tre trên da.
N: 그가 가진 것은 쇠수레가 아니었습니다. 눈이었습니다. 요하에서 성까지의 길에 그의 눈이 있었습니다.
을지문덕: 저들은 길에서 굶고 있소. 탁군의 쌀이 사람을 못 따라오오.

### SC_121 · LOC_001_YOHA (đường tiếp vận 탁군→요하, ban ngày — ken-burns) · dân phu Tùy · WPN_201 · still_kenburns · 16:26–16:36
[ACTION-VI] Ảnh: đường tiếp vận từ 탁군 tới 요하 — xe bò gãy trục nằm nghiêng bên đường, bò chết trương, dân phu gục bên bánh xe, bao gạo rách vãi xuống bùn; hàng xe phía sau kẹt dài tới chân trời; sĩ quan cưỡi ngựa quất roi. Ken-burns trượt dọc hàng xe gãy.
[SOUND] bánh xe gãy, bò rống, roi, gió bụi.
N: 역사는 그 길을 기록했습니다. 탁군에서 요하까지, 수레와 소는 갔고 돌아오지 않았습니다. 쌀은 길 위에서 사람보다 먼저 죽었습니다. 백만을 먹이는 길이 백만보다 먼저 지쳤습니다.

### SC_122 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_101, CHAR_105 · — · video8s · 16:36–16:44
[ACTION-VI] 을지문덕 gạt thẻ tre và quân cờ sang một bên, đặt ra thỏa hiệp: bàn tay chỉ 해모루, rồi chỉ 한승우.
[SOUND] quân cờ trượt.
N: 판은 그의 것이었습니다. 말은 한승우의 것이었습니다. 그 사이에 해모루가 섰습니다.
을지문덕: 임무는 해모루가 전하오. 쇠수레는 한 대장이 정하시오.

### SC_123 · LOC_002_YODONGSEONG (đại sảnh) · CHAR_001, CHAR_003, CHAR_002 · — · video8s · 16:44–16:52
[ACTION-VI] 한승우 gật; 박기철 thở ra; 오태민 quay lưng ra cửa trước, không chào. 한승우 đứng dậy.
[SOUND] sàn gỗ, cửa.
N: 그날 밤 이긴 사람은 없었습니다. 진 사람도 없었습니다. 판과 말이 각자의 주인을 가졌을 뿐입니다.
한승우: 그렇게 하겠습니다.

### SC_124 · LOC_003_CHEONDUNG_BASE (bãi xe, đêm) · CHAR_003, 초병 (lính Hàn) · VEH_001, PROP_007 · video8s · 16:52–17:00
[ACTION-VI] Thung lũng đêm: 박기철 (về từ thành) đi vòng qua hai phuy sau bao cát, đá thử bao cát; tới K2 — xách chum đất múc nước suối tưới lên lưới ngụy trang phủ xe, kỹ từng mép; đưa chum cho lính gác.
[SOUND] nước lên lưới, gió khô lùa khe.
N: 지난달 여울에서 그물이 탔습니다. 박기철은 그것을 잊지 않았습니다. 그의 버릇은 그날 밤부터였습니다.
박기철: 불티는 그물부터 먹는다. 전차 그물은 적셔.

### SC_125 · LOC_002_YODONGSEONG (thành đêm — ken-burns) · — · PROP_016 · still_kenburns · 17:00–17:10
[ACTION-VI] Ảnh: thành ban đêm nhìn từ tháp chùa gỗ — mái kho nhỏ cháy đen còn khói cạnh kho lương, đuốc dọc tường, biển lửa trại Tùy bên ngoài vòng quanh. Ken-burns kéo ra.
[SOUND] khói, đuốc, trống xa.
N: 성은 그날 밤도 자지 못했습니다. 밖에는 백만이 있었고, 안에는 조 한 그릇과 아흔네 명이 있었습니다.

### SC_126 · LOC_002_YODONGSEONG (đại sảnh, vắng) · CHAR_101, CHAR_105 · — · video8s · 17:10–17:18
[ACTION-VI] Đại sảnh chỉ còn hai người; 을지문덕 cuộn bản đồ chậm, nói với 해모루 đang thu đèn — không nhìn anh.
[SOUND] da cuộn, đèn.
N: 문이 닫힌 뒤 을지문덕은 다른 말을 했습니다. 쇠수레에 대한 것이었습니다. 해모루만 들었습니다.
을지문덕: 저들은 오래 못 버티오. 그러니 오래 쓸 데를 찾아야 하오.

### SC_127 · LOC_002_YODONGSEONG (đại sảnh, bản đồ — ken-burns) · CHAR_101 (tay) · — · still_kenburns · 17:18–17:30
[ACTION-VI] Ảnh cận: bản đồ da mở lại một góc dưới đèn — ngón tay gầy của 을지문덕 dừng ở một đường sông vẽ mực xa về phía nam, chưa có chữ; phía trên là thành và biển ký hiệu địch. Ken-burns đẩy chậm vào ngón tay trên sông.
[SOUND] đèn, im.
N: 오래 쓸 데. 그 말에는 아직 이름이 없었습니다. 지도 위에는 강 하나가 있었습니다. 성에서 아득히 남쪽이었습니다. 그는 그날 밤 그 강을 보고 있었습니다.

[Kết thúc Phần 6]

## [Phần 7] 검은 물이 탄다 — 「검은 물이 탄다」 / Kẻ địch thích nghi  (17:30–21:00)
> Tóm tắt VI: (a) ENEMY POV, D33: 탁발흠 hỏi cung nông dân Goguryeo bị bắt (qua 통역): xe sắt uống "검은 물" từ thùng tròn — ông ta thấy trên đường đông tháng trước. 탁발흠: "말은 풀을 먹고, 쇠수레는 검은 물을 마신다." Lệnh: tìm thùng, không tìm xe. Đêm: ông đi bộ lên con đường mòn đã biết từ 1화 (trinh sát của ông bị bắn ở đó) → lần này chỉ nhìn hai phuy sau bao cát — không đánh, thuộc chỗ thùng; ông đợi hoàng đế cho phép (12 ngày) — trả lời open loop P2 "vì sao 20 ngày không ai tới". (b) 5월, D45: 육합성 dựng trong một đêm, chu vi 8리 [史]. 양제: "뇌군은 어디 있느냐." 탁발흠: đánh thứ xe uống, không đánh xe. 양제: "오늘 밤은 네 것이다. 검은 물을 태워라." (c) Đêm khô gió: 6 kính đêm gác; Tiên Ti đi bộ xuống đường mòn với nồi lửa; tên lửa vào lưới → phuy #1 nổ (NARRATOR IM 32 s) → 박기철 tay không lăn phuy #2, 오태민 đẩy cùng (tay áo cháy) → 천둥 4 cháy, 40mm nổ dây chuyền, drone #2 trong hộp cháy; 백성민 hạ 3 kẻ vác nồi lửa gần K2; K2 dưới lưới ướt không sao. 탁발흠 trên sườn: "검은 물이 탄다. 그럼 쇠수레도 탄다."
> Chức năng: THREAT (turning point) · Combat: SC_139–150 · Tài nguyên: K21 3→2 · phuy 2→1 · drone 3→2 · 40mm −200 · 2 bỏng nặng + 박기철 bỏng tay · Enemy adaptation: "nước đen", đường mòn, đánh lúc kính đêm ít · Quyết định lịch sử: 양제 giao đêm cho 탁발흠 · Payoff: đuốc dính lưới (1화), "검은 통" (1화 SC_251), lưới ướt K2 (P6) · Open loop: "검은 물이 탄다. 그럼 쇠수레도 탄다." → [MID-ROLL 3 · 21:00]

### SC_128 · LOC_001_YOHA (trại tiền quân Tùy bờ đông, ban ngày) · CHAR_205, 고구려 농부, 통역 · VEH_206 · video8s · 17:30–17:38
[ACTION-VI] D33, trại Tiên Ti rìa đại doanh: một nông dân Goguryeo bị trói quỳ trên đất, mặt bầm; 탁발흠 ngồi xổm ngang tầm mắt ông ta, không đánh; một thông ngôn Tùy áo xám cúi bên. Nông dân nói, tay bị trói cố vẽ hình tròn trong không khí.
[SOUND] ngựa, gió, giọng thông ngôn nhắc lại.
N: 나흘 뒤. 탁발흠은 성 밖에서 나물을 캐던 농부 하나를 잡았습니다. 때리지 않았습니다. 물었습니다. 지난달 동쪽 길에서 무엇을 보았는가.
고구려 농부: 쇠수레가… 둥근 통에서 검은 물을 마셨소.

### SC_129 · LOC_001_YOHA (trại Tiên Ti) · CHAR_205 · — · video8s · 17:38–17:46
[ACTION-VI] 탁발흠 đứng dậy, nhìn về phía đông nơi dải đồi sau thành mờ trong bụi; nói với chính mình, chậm, như ghi vào đá.
[SOUND] gió, ngựa gặm cỏ.
N: 그는 지난달 문 앞에서 검은 통을 보았습니다. 그때는 그것이 무엇인지 몰랐습니다. 이제 알았습니다.
탁발흠: 말은 풀을 먹고, 쇠수레는 검은 물을 마신다.

### SC_130 · LOC_001_YOHA (trại Tiên Ti) · CHAR_205, 선비 부장 · VEH_206 · video8s · 17:46–17:54
[ACTION-VI] 탁발흠 quay sang phó tướng (mũ lông, giáp da), ra lệnh ngắn; phó tướng nhìn về phía thành như định hỏi "xe?", ông lắc đầu.
[SOUND] gió, dây cương.
N: 황제는 쇠수레를 가져오라 했습니다. 탁발흠은 다른 것을 찾기로 했습니다.
탁발흠: 검은 통이 어디 있는지 찾는다. 수레는 나중이다.

### SC_131 · LOC_003_CHEONDUNG_BASE (bờ bắc bến suối, đêm) · CHAR_205, 3 trinh sát Tiên Ti · VEH_206 · video8s · 17:54–18:02
[ACTION-VI] Đêm không trăng: 탁발흠 đi bộ, không ngựa, ba trinh sát theo; ông đi thẳng lên sườn đồi theo con đường đã biết — không lần vết, không dừng; ngang qua vệt bùn khô ở bờ bắc bến suối (rãnh xích, vết móng bò 1화) ông chỉ liếc một cái. Low-angle, tracking.
[SOUND] nước suối, côn trùng, ngón tay trên đất khô.
N: 지난달 그는 이 길로 척후를 내려보냈습니다. 화살 하나가 쇠수레의 그물에 박혔습니다. 그때는 무엇을 쳐야 하는지 몰랐습니다.

### SC_132 · LOC_003_CHEONDUNG_BASE (sườn đồi, rìa bụi sồi — POV) · CHAR_205 · VEH_001, VEH_002, VEH_003, PROP_007 · video8s · 18:02–18:10
[ACTION-VI] POV qua bụi sồi từ sườn đồi: dưới thung lũng đêm, bóng lưới ngụy trang, chấm đèn đỏ lều chỉ huy, hàng xe; và cách hàng xe ba mươi bước, sau bao cát, hai khối tròn — đúng hình ông ta vẽ. Máy giữ, rồi hai ngón tay 탁발흠 vào khung: đếm hai.
[SOUND] gió trong lá, máy phát K151 ro ro rất nhỏ.
N: 골짜기는 그대로였습니다. 그물, 붉은 빛, 그리고 둥근 통이 둘. 이번에는 그는 통만 보았습니다.

### SC_133 · LOC_003_CHEONDUNG_BASE (sườn đồi) · CHAR_205, trinh sát Tiên Ti · — · video8s · 18:10–18:18
[ACTION-VI] 탁발흠 trong bóng tối: một trinh sát rút dao ra hiệu xuống — ông chặn cổ tay hắn, lắc đầu; nhìn hai phuy sau bao cát một lần dài, rồi trườn ngược lên đỉnh. Cận mặt, sẹo.
[SOUND] dao vào vỏ, lá, thở.
N: 그는 그날 밤 아무것도 하지 않았습니다. 셋으로는 부족했고, 황제의 허락이 없었습니다. 수나라에서는 황제 없이 불도 못 놓았습니다. 스무 날 동안 그가 오지 않은 이유였습니다. 그는 통의 자리를 외웠습니다. 그리고 열이틀을 기다렸습니다.

### SC_134 · LOC_004_YUKHAPSEONG (aerial bình minh — ken-burns) · — · PROP_021 · still_kenburns · 18:18–18:30
[ACTION-VI] Ảnh aerial bình minh D45: trên đồng vàng cách tường tây thành 2 km, một tòa thành vuông mới toanh — tường vải sơn giả gạch xám căng trên khung gỗ, lầu canh đỏ son bốn góc, giữa là điện mái lụa vàng trên bục — mọc giữa biển lều, sương sớm; trên tường 요동성, hàng lính Goguryeo đứng nhìn. Ken-burns kéo ra từ điện vàng.
[SOUND] trống lớn, kèn, gió trên cao.
N: 5월. 황제가 왔습니다. 하룻밤 사이에 성 하나가 벌판에 섰습니다. 육합성. 둘레 여덟 리, 나무 틀에 천을 씌운 성이었습니다. 역사는 이것을 기록했습니다. 고구려 군사들은 담 위에서 그것을 보았습니다. 하룻밤에 성을 세우는 나라와 싸우고 있었습니다.

### SC_135 · LOC_004_YUKHAPSEONG (điện vàng, ban ngày) · CHAR_201, 수 공성총관, CHAR_205 · — · video8s · 18:30–18:38
[ACTION-VI] Trong điện: nắng qua rèm lụa thành sọc; 양제 trên ngai, giáp mạ vàng, bụi bám gấu áo vàng, quạt tròn tay trái, mặt cáu; tướng công thành quỳ trước bậc, 탁발흠 quỳ sau hai bước. 양제 hỏi không nhìn ai.
[SOUND] lụa, lư hương, ngoài xa trống.
N: 황제는 성을 묻지 않았습니다. 성은 두 달째 그 자리에 있었습니다. 그는 새 것을 물었습니다.
수 양제: 뇌군은 어디 있느냐.

### SC_136 · LOC_004_YUKHAPSEONG (điện vàng) · 수 공성총관 · — · video8s · 18:38–18:46
[ACTION-VI] Tướng công thành cúi sát sàn, trả lời; tay chỉ ngược ra sau về phía 탁발흠 mà không quay đầu.
[SOUND] trán chạm sàn gỗ.
N: 총관은 골짜기를 가 본 적이 없었습니다. 가 본 사람은 뒤에 무릎 꿇고 있었습니다.
수 공성총관: 성 뒤 골짜기에 숨어 있습니다. 탁발 낭장이 지난달부터 지켜봤습니다.

### SC_137 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_205 · — · video8s · 18:46–18:54
[ACTION-VI] 탁발흠 ngẩng đầu — mũi tên Goguryeo trên dây da cổ, sẹo thái dương; ông nói ngắn, chắc, 합쇼체.
[SOUND] lụa gió.
N: 황제는 쇠수레를 가져오라 했습니다. 탁발흠은 다른 것을 청했습니다. 그것은 명령을 거스르는 것이었습니다. 그는 그래도 말했습니다.
탁발흠: 폐하, 쇠수레를 치지 않겠습니다. 쇠수레가 마시는 것을 치겠습니다.

### SC_138 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_201 · — · video8s · 18:54–19:02
[ACTION-VI] 양제 quạt dừng; ông nhìn 탁발흠 lần đầu, tò mò lạnh như nhìn cánh quạt drone tháng trước; rồi khẽ nghiêng quạt về phía cửa — ban đêm cho hắn.
[SOUND] quạt lụa, lư hương.
N: 황제는 이 선비 사람을 기억했습니다. 쇠새를 가져온 자였습니다. 그는 명령을 바꾸지 않았습니다. 하룻밤만 빌려주었습니다.
수 양제: 그럼 오늘 밤은 네 것이다. 검은 물을 태워라.

### SC_139 · LOC_003_CHEONDUNG_BASE (gò bắc, đêm) · CHAR_006 · EQP_001 · video8s · 19:02–19:10
[ACTION-VI] Đêm khô, gió giật từng cơn lùa khe; 백성민 nằm trên gò bắc, kính đêm — POV xanh lục: đường mòn trống, bụi sồi lay; cận mặt anh dưới kính, rồi cận tay anh chỉnh kính. Sáu chấm sáng kính đêm rải quanh thung. Dưới bãi xe, 태오 khép cửa đuôi 천둥 4 — hộp drone #2 đặt trong khoang lính cho kín khô.
[SOUND] gió giật, lá khô, kính đêm rít, cửa đuôi K21 khép.
[COMBAT]
N: 그날 밤 야시경은 여섯이었습니다. 건전지를 아끼는 밤이었습니다. 바람은 서쪽에서 불었고, 골짜기는 말라 있었습니다. 불이 좋아하는 밤이었습니다.

### SC_140 · LOC_003_CHEONDUNG_BASE (đường mòn, sườn đồi) · CHAR_205, kỵ Tiên Ti đi bộ · PROP_016 · video8s · 19:10–19:18
[ACTION-VI] Trên đường mòn tối: Tiên Ti đi bộ thành hàng, giáp da, cung; mỗi người thứ ba ôm một nồi đất có nắp — khe nắp hắt ánh than đỏ lên cằm; 탁발흠 đi đầu, tay giơ ra sau ra hiệu ngồi xuống. Không đuốc. Tracking thấp.
[SOUND] than trong nồi lách tách, dép da trên đá, gió.
[COMBAT]
N: 그들은 말을 두고 왔습니다. 횃불도 두고 왔습니다. 불은 항아리 안에 있었습니다. 야시경은 항아리 안을 볼 수 없었습니다.

### SC_141 · LOC_003_CHEONDUNG_BASE (rìa sườn, trên bãi xe) · cung thủ Tiên Ti · PROP_016 · video8s · 19:18–19:26
[ACTION-VI] Mười cung thủ Tiên Ti mở nắp nồi, châm đầu tên quấn vải dầu vào than, giương cung thấp — thả đồng loạt: mười vệt lửa bay vòng cung thấp qua bụi sồi xuống hàng xe tải và bao cát; tên cắm vào lưới ngụy trang trên K511 #2 và lưới phủ bao cát phuy. Wide từ trên.
[SOUND] dây cung, tên lửa rít, lưới bén "화르륵".
[COMBAT]
N: 그물이었습니다. 달포 전 여울에서 배운 것이었습니다. 쇠는 안 타도 그물은 탔습니다.

### SC_142 · LOC_003_CHEONDUNG_BASE (bãi phuy) · CHAR_003, 초병 · PROP_007, VEH_003 · video8s · 19:26–19:34
[ACTION-VI] Lưới trên bao cát bùng cháy, lửa liếm lên hai phuy; một cán tên cháy nằm vắt ngang nắp vặn phuy ngoài; 박기철 lao từ lều chỉ huy ra, chân trần một bên, gào; lính gác bắn vào bóng tối sườn đồi.
[SOUND] lửa, K2C1 loạt ngắn, tiếng gào.
[COMBAT]
N: 박기철은 이 순간을 알고 있었습니다. 그래서 통을 수레에서 삼십 걸음 떼어 두었습니다. 삼십 걸음. 그것이 그가 산 값이었습니다.
박기철: 불! 드럼!

[NARRATOR IM LẶNG — 19:34 → 20:06]

### SC_143 · LOC_003_CHEONDUNG_BASE (bãi phuy, wide) · — · PROP_007 · video8s · 19:34–19:42
[ACTION-VI] Phuy ngoài nổ: cột lửa cam đỏ dựng cao mười mét, sóng nhiệt đẩy lưới cháy bay, bao cát văng; mọi người trong khung nằm rạp; ánh lửa hắt lên cả hai sườn thung lũng và tán sồi. Wide thấp, máy rung. Không narration.
[SOUND] "쾅" trầm, lửa gầm, tai ù.
[COMBAT]

### SC_144 · LOC_003_CHEONDUNG_BASE (bãi phuy) · CHAR_003, CHAR_002 · PROP_007 · video8s · 19:42–19:50
[ACTION-VI] 박기철 chạy VÀO vùng sáng, ôm phuy thứ hai đang đứng bên vũng lửa, ngả nó xuống bằng vai, lăn bằng hai bàn tay trần trên đất nóng ra xa — tay áo bốc khói; 오태민 lao tới đẩy cùng, tay áo phải bén lửa, anh đập vào đùi dập. Hai người lăn phuy qua ranh sáng-tối. Tracking sát. Không narration.
[SOUND] phuy lăn ầm ầm, lửa, thở gắt, da cháy xèo.
[COMBAT]

### SC_145 · LOC_003_CHEONDUNG_BASE (천둥 4) · kíp 천둥 4 · VEH_002 · video8s · 19:50–19:58
[ACTION-VI] 천둥 4 đậu sát thùng K511 #2: lưới cháy trên xe tải đổ sang, can dầu phụ trên thùng xe tải bục — lửa tràn qua hông xuống gầm 천둥 4, lưới ngụy trang trên nóc bốc thành mảng, lửa chui vào khe lưới thoát khí động cơ; ba người kíp xe bật nắp nóc nhảy ra, một người lăn trên đất dập lửa trên lưng. Không narration.
[SOUND] lửa, kim loại kêu, thét.
[COMBAT]

### SC_146 · LOC_003_CHEONDUNG_BASE (천둥 4, wide) · đại đội nằm rạp · VEH_002, UAV_001 · video8s · 19:58–20:06
[ACTION-VI] Đạn 40mm trong 천둥 4 nổ dây chuyền: chớp trắng liên tiếp qua nắp nóc mở, mảnh và tracer phụt lên trời thành chùm; qua cửa đuôi bung ra, khoang lính rực lửa — hộp drone bên trong cháy; cả bãi nằm sát đất, tay ôm đầu. Wide. Không narration.
[SOUND] "탕탕탕" dồn dập không dứt, mảnh rơi thép.
[COMBAT]

### SC_147 · LOC_003_CHEONDUNG_BASE (bên K2, tối) · CHAR_006, 3 Tiên Ti · VEH_001, WPN_001 · video8s · 20:06–20:14
[ACTION-VI] Phía K2 đậu riêng rìa tối: ba Tiên Ti ôm nồi lửa trườn tới lưới xe; 백성민 từ sau gò lao xuống — máy ở sau lưng anh, kẻ đầu đổ khỏi khung không thấy lưỡi dao chạm da, kẻ thứ hai quay lại nhận loạt ngắn K2C1 ở cự ly hai mét, kẻ thứ ba đánh rơi nồi bỏ chạy lên sườn — loạt thứ hai hạ hắn giữa dốc, than tung tóe. Cận, nhanh.
[SOUND] dao, loạt ngắn, nồi vỡ, than rơi.
[COMBAT]
N: 셋이 전차로 갔습니다. 백성민은 그것을 처음부터 보고 있었습니다. 셋 다 돌아가지 못했습니다.

### SC_148 · LOC_003_CHEONDUNG_BASE (K2 dưới lưới) · CHAR_003 · VEH_001 · video8s · 20:14–20:22
[ACTION-VI] Than rơi lên lưới ngụy trang K2 — xèo, tắt, khói trắng; lưới ướt đẫm. 박기철 (tay đỏ phồng, run) tới đập bàn tay lên lưới ướt — rồi rụt lại vì đau; đứng thở nhìn xe nguyên vẹn.
[SOUND] than tắt trong nước, thở, lửa xa.
[COMBAT]
N: 전차는 젖은 그물 밑에 있었습니다. 박기철의 버릇이었습니다. 버릇 하나가 전차 한 대를 남겼습니다.

### SC_149 · LOC_003_CHEONDUNG_BASE (gần 천둥 4) · CHAR_005, CHAR_004 · VEH_002, UAV_001 · video8s · 20:22–20:30
[ACTION-VI] 태오 bật dậy chạy về phía cửa đuôi 천둥 4 nơi khoang lính đang cháy — 서아 nhào tới ôm ngang người kéo ngã xuống đất đúng lúc hộp drone bên trong nổ bung; cậu gào tên máy. Cận hai người trên đất, lửa hắt.
[SOUND] hộp nhựa nổ, gào, lửa.
[COMBAT]
N: 드론 둘이 남았습니다. 셋째는 상자 안에서 탔습니다. 태오는 한 대를 이름으로 불렀습니다.
장태오: 2호기! 2호기가 안에…

### SC_150 · LOC_003_CHEONDUNG_BASE (sườn đồi) · CHAR_205 · — · video8s · 20:30–20:38
[ACTION-VI] 탁발흠 trên sườn đồi giữa bụi sồi nhìn xuống thung lũng ngập lửa cam: một xe sắt cháy, một cột lửa phuy, người chạy; mặt ông sáng lửa, hai bàn tay đặt trên đầu gối; ông nói câu học được, rồi giơ tay — rút.
[SOUND] lửa xa, gió, giọng thấp.
[COMBAT]
N: 그는 오래 보지 않았습니다. 볼 것은 다 보았습니다.
탁발흠: 검은 물이 탄다. 그럼 쇠수레도 탄다.

### SC_151 · LOC_003_CHEONDUNG_BASE (đêm, wide — ken-burns) · — · VEH_002, VEH_001, PROP_007 · still_kenburns · 20:38–20:50
[ACTION-VI] Ảnh: thung lũng đêm ngập sáng cam — 천둥 4 là khối lửa đen, vũng dầu cháy, hố cháy nơi phuy nổ; phuy thứ hai nằm nghiêng xa trong tối; ở rìa, K2 dưới lưới ướt bóng nước; người nhỏ xíu chạy với chum. Ken-burns kéo ra chậm.
[SOUND] lửa, tiếng người xa, 40mm còn nổ lẻ.
N: 그날 밤의 셈은 이랬습니다. 장갑차 셋에서 둘. 드럼 둘에서 하나. 드론 셋에서 둘. 40밀리 이백 발이 하늘로 갔습니다. 총 한 발 맞지 않고 잃은 것이었습니다.

### SC_152 · LOC_003_CHEONDUNG_BASE (bình minh — ken-burns) · CHAR_003, CHAR_004 · VEH_002 · still_kenburns · 20:50–21:00
[ACTION-VI] Ảnh: bình minh xám, 박기철 ngồi trên thùng đạn, hai bàn tay ngâm trong xô nước, lông mày trái cháy xém, mặt bồ hóng; 서아 quỳ băng; sau lưng họ, xác 천둥 4 đen bốc khói. Ken-burns đẩy vào hai bàn tay trong nước.
[SOUND] nước, khói, chim sớm.
N: 처음으로 싸움 밖에서 쇠를 잃었습니다. 적은 쇠수레를 치지 않았습니다. 쇠수레를 먹이는 것을 쳤습니다. 탁발흠은 그날 밤 이름 하나를 더 배웠습니다. 검은 물.

[MID-ROLL 3 · 21:00]

[Kết thúc Phần 7]

## [Phần 8] 항생제, 없습니다 — 「항생제, 없습니다」 / Tài nguyên bắt đầu cạn  (21:00–24:00)
> Tóm tắt VI: Sau mid-roll: xác 천둥 4 đen khói lúc bình minh D46 (không thoại). 박기철 tay băng đọc bảng 태오 viết hộ: "K21 두 대. 드럼 하나. 드론 둘. 40mm 이백 발 날아갔습니다." 서아 sau đêm băng 2 lính bỏng + 15 lính Goguryeo, lộn ngược túi thuốc: "항생제, 없습니다. 이제부턴 이 사람들 약초입니다." 을보 mang rổ thuốc: "쓰다. 쓴 만큼 듣는다." Trống: 2차 공성 — Tùy đánh tường tưởng 뇌군 đã què; 오태민 xin ra; 을지문덕 giáp đủ bộ đi VÀO thung lũng giữa trận: "성은 성이 막소. 나는 쇠수레를 보러 왔소." Ông đứng cạnh K2 lần đầu, chạm giáp một lần, không bình luận; hỏi số: "쇠수레는 몇 번 울 수 있소?" — "스물두 발. 기름은 삼백육십." — "한 발에 탑 하나입니다." Tường Goguryeo tự đẩy lui đợt hai. 오태민: dùng K2 phá vây ngay; 박기철: "전차 시동 한 번이 드론 열 번입니다." 을지문덕: hoàng đế đang gom quân riêng để vòng qua thành — chưa biết bao nhiêu. Điều kiện: "다음 공성 때 쇠수레를 쓰시오. 열 발만." 한승우: không phá vây, giữ dầu, K2 mười viên. Bàn tay ông trên tháp pháo (ken-burns). "열 발. 그 이상은 안 되오. 그다음엔 저들이 어디로 갈지 보이오."
> Chức năng: DECISION · Combat: SC_157, 158, 165 (2차 공성 — Goguryeo tự giữ) · Tài nguyên nói thành lời: "K21 두 대. 드럼 하나. 드론 둘. 40mm 이백 발" · "항생제, 없습니다" · "스물두 발. 기름은 삼백육십" · "열 발" · Quyết định lịch sử: 을지문덕 rời tường giữa trận để xem xe; đặt giới hạn 10 viên · Open loop: "열 발. 그 이상은 안 되오. 그다음엔 저들이 어디로 갈지 보이오."

### SC_153 · LOC_003_CHEONDUNG_BASE (bình minh — ken-burns) · — · VEH_002, PROP_007 · still_kenburns · 21:00–21:12
[ACTION-VI] Ảnh: bình minh xám lạnh: xác 천둥 4 đen kịt, tháp pháo lệch, nắp nóc há, khói trắng mỏng bốc thẳng vì gió đã lặng; hố cháy nơi phuy nổ, bao cát tung; tro phủ cỏ, lều, lưới. Ken-burns đẩy chậm vào nắp nóc há. Không thoại.
[SOUND] khói, kim loại nguội kêu tách, chim.
N: 새벽. 천둥 4호는 검은 뼈였습니다. 어제까지 아홉 명을 태우던 쇠집이었습니다. 기름 한 통이 그것을 태웠습니다. 기름은 목숨이었고, 그래서 불이기도 했습니다.

### SC_154 · LOC_003_CHEONDUNG_BASE (lều chỉ huy, bảng đếm) · CHAR_003, CHAR_005, CHAR_001 · — · video8s · 21:12–21:20
[ACTION-VI] 박기철 hai tay băng trắng đến cổ tay, lông mày cháy, đứng trước bảng gỗ; 태오 cầm phấn viết hộ theo lời ông; 한승우 đứng nghe, bụi tro trên mũ. 박기철 đọc từng dòng khi 태오 viết.
[SOUND] phấn, gió lặng, khói.
N: 박기철은 손으로 쓸 수 없었습니다. 입으로 읽었습니다. 판은 태오가 썼습니다. 숫자는 하룻밤에 이만큼 바뀌었습니다.
박기철: K21 두 대. 드럼 하나. 드론 둘. 40mm 이백 발 날아갔습니다.

### SC_155 · LOC_003_CHEONDUNG_BASE (lều quân y) · CHAR_004, thương binh · PROP_009 · video8s · 21:20–21:28
[ACTION-VI] Lều quân y: hai lính Hàn bỏng nằm băng kín cánh tay và cổ; ngoài cửa lều, hàng thương binh Goguryeo chờ; 서아 tay áo máu tới khuỷu, mũ tháo, cầm ba lô quân y dốc ngược — vài gói băng rơi, không một lọ. Cô nhìn 한승우 ở cửa lều.
[SOUND] ba lô rỗng lắc, rên.
N: 밤새 서아는 화상 둘과 고구려 열다섯을 묶었습니다. 열두 병은 스무 날 동안 밤마다 줄었습니다. 마지막 병은 그 밤에 나갔습니다.
윤서아: 항생제, 없습니다. 이제부턴 이 사람들 약초입니다.

### SC_156 · LOC_003_CHEONDUNG_BASE (lều quân y) · CHAR_106, CHAR_107, CHAR_004 · — · video8s · 21:28–21:36
[ACTION-VI] 을보 bước vào với rổ tre đầy rễ và lá, 아리 (khăn olive) bê nồi đất sắc sẵn; ông đặt rổ xuống cạnh ba lô rỗng, nhìn 서아, nói cộc.
[SOUND] rổ tre, nồi đất.
N: 을보의 약은 쓰고, 느리고, 이 땅의 것이었습니다. 이제 그것뿐이었습니다.
을보: 쓰다. 쓴 만큼 듣는다.

### SC_157 · LOC_003_CHEONDUNG_BASE (bên 천둥 2) · CHAR_002 · VEH_002, EQP_002 · video8s · 21:36–21:44
[ACTION-VI] Trống Tùy nổi từ phía thành, dồn dập hơn mọi sáng; 오태민 (tay áo phải cháy xém, mặt bồ hóng) nhảy lên nóc 천둥 2, tay ấn tai nghe, gào về phía 한승우 ở lều chỉ huy.
[SOUND] trống vọng qua đồi, PTT.
[COMBAT]
N: 수나라는 새벽을 기다리지 않았습니다. 뇌군이 절뚝거리는 아침에 담을 쳤습니다.
오태민: 중대장님, 성이 공격받습니다. 나가겠습니다.

### SC_158 · LOC_002_YODONGSEONG (mặt tường nam) · CHAR_104, lính Goguryeo · VEH_203, VEH_201 · video8s · 21:44–21:52
[ACTION-VI] Tường nam: thang mây và một tháp phủ đất áp tường; 고정수 (băng trán) dẫn lính đẩy thang bằng sào chạc, nước sôi trút, đá lăn; cầu tháp hạ xuống — giáo Goguryeo đón, không một lính Hàn trong khung. Wide trung.
[SOUND] trống, thang gãy, giáo, thét.
[COMBAT]
N: 두 번째 공성이었습니다. 담 위에는 고구려뿐이었습니다. 담은 총 없이 싸우는 법을 이백 년 알고 있었습니다.

### SC_159 · LOC_003_CHEONDUNG_BASE (cửa thung, đường mòn) · CHAR_101, CHAR_105, CHAR_002 · — · video8s · 21:52–22:00
[ACTION-VI] Từ đường mòn, 을지문덕 đi bộ VÀO thung lũng — giáp đủ bộ, lông chỏm đen cao với hai lông trắng, 해모루 theo sau — trong khi trống và tiếng thét dội sau lưng ông; 오태민 trên nóc xe sững người. 을지문덕 không nhìn về phía thành.
[SOUND] trống xa, giáp, bước chân trên tro.
[COMBAT]
N: 담이 공격받는 아침에 대장군은 담을 떠났습니다. 그는 담을 믿었습니다. 그가 보러 온 것은 다른 것이었습니다.
을지문덕: 성은 성이 막소. 나는 쇠수레를 보러 왔소.

### SC_160 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_101, CHAR_003, CHAR_001 · VEH_001 · video8s · 22:00–22:08
[ACTION-VI] 을지문덕 đứng trước K2 lần đầu — lưới đã kéo lên, thép ba màu, nòng dài; ông đặt bàn tay lên tấm giáp trước tháp một lần, giữ hai giây, bỏ xuống; đi vòng quanh xe, nhìn xích, nhìn nòng; không nói gì. 박기철 (tay băng) và 한승우 đứng chờ.
[SOUND] giáp ông, bước chân trên đất trần, trống xa.
N: 그는 쇠수레가 무엇인지 묻지 않았습니다. 손을 한 번 얹었습니다. 그리고 셈을 물었습니다.

### SC_161 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_101, CHAR_003 · VEH_001 · video8s · 22:08–22:16
[ACTION-VI] 을지문덕 dừng trước nòng pháo, nhìn vào miệng nòng sạch chưa một vệt bồ hóng; hỏi 박기철 không quay đầu.
[SOUND] gió, trống.
N: 우는 쇠는 몇 발이냐고 물었던 사람이었습니다. 쇠수레에는 다른 말을 썼습니다. 운다는 것이었습니다.
을지문덕: 쇠수레는 몇 번 울 수 있소?

### SC_162 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_003 · VEH_001 · video8s · 22:16–22:24
[ACTION-VI] 박기철 giơ hai bàn tay băng như định đếm ngón, không đếm được, nói số thẳng; ánh mắt rời nòng sang que đo dầu cắm ở nắp thùng dầu.
[SOUND] băng cọ, gió.
N: 박기철은 모든 것을 말했습니다. 숨길 이유가 없었습니다. 그 사람은 어차피 세고 있었습니다.
박기철: 스물두 발. 기름은 삼백오십.

### SC_163 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_101 · VEH_001 · video8s · 22:24–22:32
[ACTION-VI] 을지문덕 quay nhìn về phía dải đồi che thành, nơi tiếng trống dội lại; đặt ngón tay lên hông tháp pháo, hỏi tiếp.
[SOUND] trống, ngón tay trên thép.
N: 그는 세 번째 셈으로 갔습니다. 한 발의 값이었습니다.
을지문덕: 한 번 울면 저 탑이 몇 개 무너지오?

### SC_164 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_003, CHAR_001 · VEH_001 · video8s · 22:32–22:40
[ACTION-VI] 박기철 trả lời; 한승우 bên cạnh nhìn 을지문덕 — ông đang tính, môi mấp máy: hai mươi hai và bốn mươi.
[SOUND] gió.
N: 스물둘과 마흔. 그는 그 두 숫자를 나란히 놓았습니다. 답은 하나였습니다. 스물둘로는 마흔을 못 부순다. 그는 이미 다른 셈을 하고 있었습니다.
박기철: 한 발에 탑 하나입니다.

### SC_165 · LOC_002_YODONGSEONG (mặt tường nam) · lính Goguryeo, 소년 척후, lính Tùy · VEH_203 · video8s · 22:40–22:48
[ACTION-VI] Tường nam: thang cuối bị đẩy đổ; trống Tùy đổi nhịp rút; lính Tùy khiêng thang lùi qua hào; trên tường, 소년 척후 — gầy đi, cánh tay còn băng — chuyền bó tên cho cung thủ; lính Goguryeo ngồi thở, không reo. Wide.
[SOUND] trống rút, thở, tên xếp.
[COMBAT]
N: 두 번째 공성은 한나절로 끝났습니다. 담이 혼자 막았습니다. 화살을 나르는 아이의 열은 보름 전에 내렸습니다. 열두 병 중 한 병의 값이었습니다.

### SC_166 · LOC_003_CHEONDUNG_BASE (bên K2 → 천둥 2) · CHAR_002, CHAR_001 · VEH_001, VEH_002 · video8s · 22:48–22:56
[ACTION-VI] 오태민 nhảy xuống khỏi 천둥 2, đi thẳng tới 한승우 bên K2, chỉ tay lên đường mòn rồi chỉ về hướng tây — xuyên vòng vây; giọng to, mặt còn bồ hóng.
[SOUND] giày trên tro, gió.
N: 오태민에게 어젯밤은 답이었습니다. 앉아서 기다리면 다음 불이 온다. 그는 움직이자고 했습니다.
오태민: 전차로 포위를 뚫습니다. 지금이 기회입니다.

### SC_167 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_003 · VEH_001 · video8s · 22:56–23:04
[ACTION-VI] 박기철 giơ một bàn tay băng chặn giữa 오태민 và xe — không cao giọng; ông gõ bàn tay băng lên nắp thùng dầu.
[SOUND] băng trên thép, gió.
N: 요동성에 온 첫날 밤, 그는 말했습니다. 드론 한 번 충전에 경유 이 리터. 전차 시동 한 번은 그 열 배였습니다. 그 셈은 그의 몸에 붙어 있었습니다.
박기철: 전차 시동 한 번이 드론 열 번입니다.

### SC_168 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_101 · VEH_001 · video8s · 23:04–23:12
[ACTION-VI] 을지문덕 chen vào bằng tin — không bằng lệnh; ông nhìn về hướng tây nơi 육합성 nằm sau đồi, nói cho cả ba người.
[SOUND] gió, trống đã tắt.
N: 산길로 온 소식은 하나 더 있었습니다. 황제의 눈이 성에서 떨어지고 있었습니다.
을지문덕: 황제가 성을 돌아갈 군사를 모으고 있소. 수는 모르오.

### SC_169 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_101, CHAR_001 · VEH_001 · video8s · 23:12–23:20
[ACTION-VI] 을지문덕 gõ hai ngón tay lên váy xích K2 — không đặt tay — rồi nói với 한승우 điều kiện, mắt vào mắt.
[SOUND] tay trên thép, gió.
N: 그는 쇠수레를 쓰라고 했습니다. 그리고 수를 정했습니다. 판의 주인이 말의 걸음을 정했습니다.
을지문덕: 다음 공성 때 쇠수레를 쓰시오. 열 발만.

### SC_170 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_001, CHAR_002, CHAR_003 · VEH_001 · video8s · 23:20–23:28
[ACTION-VI] 한승우 nhìn xác 천둥 4 sau vai 오태민, nhìn que đo dầu, nhìn 을지문덕; quyết — nói với hai người của mình, ngắn.
[SOUND] gió, khói.
N: 한승우는 조상의 수를 받았습니다. 스물두 발 중 열 발. 그는 처음으로 남의 셈을 자기 것으로 삼았습니다.
한승우: 포위는 안 뚫는다. 기름은 지킨다. 전차는 열 발.

### SC_171 · LOC_003_CHEONDUNG_BASE (K2, cận — ken-burns) · CHAR_101 (tay) · VEH_001, VEH_002 · still_kenburns · 23:28–23:38
[ACTION-VI] Ảnh cận: bàn tay gầy của 을지문덕 đặt trên góc tháp pháo K2 ba màu; nền mờ: xác 천둥 4 đen. Ken-burns kéo ra từ bàn tay tới xác xe.
[SOUND] gió, im.
N: 그는 오늘 쇠수레를 한 번 만졌습니다. 다음은 강가에서일 것이었습니다. 그는 그것을 아직 몰랐습니다.

### SC_172 · LOC_003_CHEONDUNG_BASE (bảng đếm — ken-burns) · — · — · still_kenburns · 23:38–23:48
[ACTION-VI] Ảnh cận: bảng gỗ chữ phấn nét trẻ (태오): K21 2 · 드럼 1 · 드론 2 · 항생제 0 · 포탄 22 — và ở góc, một số "10" khoanh tròn hai vòng. Ken-burns đẩy vào số 10.
[SOUND] gió, tro.
N: 판 위에 새 숫자가 하나 붙었습니다. 열. 줄어드는 숫자가 아니라 정해진 숫자였습니다. 이 부대가 받은 첫 번째 한계였습니다.

### SC_173 · LOC_003_CHEONDUNG_BASE (đường mòn lên đồi — ken-burns) · CHAR_101, CHAR_105 · — · still_kenburns · 23:48–24:00
[ACTION-VI] Ảnh: 을지문덕 và 해모루 đi ngược đường mòn lên đồi giữa bụi sồi, lưng quay về thung lũng còn khói; lông chỏm hai lông trắng nổi trên nền lá. Ken-burns theo hai người lên dốc. Giọng 을지문덕 ngoài hình.
[SOUND] bước chân trên lá, gió, giọng ông xa.
N: 그는 열 발 뒤를 이미 보고 있었습니다. 성이 아니라 황제가 어디로 가는가를.
을지문덕: 열 발. 그 이상은 안 되오. 그다음엔 저들이 어디로 갈지 보이오.

[Kết thúc Phần 8]

## [Phần 9] 치 위의 전차 — 「치 위의 전차」 / Kế hoạch lớn  (24:00–27:30)
> Tóm tắt VI: Một tháng (5월 중순–6월 초): tháp phủ đất, đóng thêm, hầm tiến — cối vô hiệu → phải đánh tại tường. 박기철 + 을보: tháo tường trong sau 치 đông-nam, đắp dốc đất cho K2 leo, mở rộng một lỗ châu mai. 고정수: "내 성벽을 헐자는 것이오? 조상이 쌓은 돌이오." 을지문덕: "조상은 돌을 지키라고 쌓지 않았소. 사람을 지키라고 쌓았소." Ba ngày đắp dốc; 박기철 nhăn: "경사 이십 도. 오르는 데 기름 십 킬로 몫입니다." Kế: cờ trắng lần 4 khi tháp cách 100 bước — nếu hoàng đế giữ lệnh → tháp dừng → cối 40 viên; nếu không → K2 mười viên. Mốc đá 100/200/300 bước thay đạn đăng ký. Kế rút: đêm sau trận rời thung lũng theo đường mòn (탁발흠 biết đường — red herring). Tiên Ti dò lửa lần 2 — 오태민 40mm đuổi (mini). 오태민 nhận giữ thung lũng với 2 K21, nổi giận. 을지문덕 hỏi nhỏ 박기철: "청천강까지 며칠이오?" — 박기철 không hiểu vì sao. Đêm 6월 10: tháp tiến vào 1 km, đài quan sát dựng phía nam; K2 rời thung lũng sau hai tháng, tới chân dốc. 고정수 cầm cờ trắng gấp: "황제는 자신의 명령을 지킬까요?"
> Chức năng: PLAN · Combat mini: SC_187–188 · Tài nguyên: dầu K2 "십 킬로 몫" (dốc) · Quyết định lịch sử: 을지문덕 gạt 고정수, đặt kế trên tâm lý hoàng đế · Red herring: 탁발흠 sẽ chặn đường mòn? (P12: theo đuôi) · Open loop: "황제는 자신의 명령을 지킬까요?" → [MID-ROLL 4 · 27:30]

### SC_174 · LOC_002_YODONGSEONG (aerial ban ngày — ken-burns) · — · VEH_201 · still_kenburns · 24:00–24:12
[ACTION-VI] Ảnh aerial: hàng tháp phủ đất nay đông hơn hẳn, kéo dài vòng theo tây, nam và một cụm phía đông-nam; đống đất hầm phía nam-tây đã dài như đê; giữa tháp và thành, dải cỏ nát; trên thành, hai lá cờ 삼족오. Ken-burns trượt dọc hàng tháp về cụm đông-nam.
[SOUND] búa xa, trống nhịp chậm, gió.
N: 한 달이 지났습니다. 5월이 6월이 되었습니다. 탑은 모두 흙을 입었고, 수는 마흔을 넘었습니다. 우는 쇠는 흙 앞에서 소용이 없었습니다. 탑은 담까지 올 것이었습니다. 그렇다면 싸움은 담에서였습니다.

### SC_175 · LOC_002_YODONGSEONG (sau 치 đông-nam, trong thành) · CHAR_003, CHAR_001, CHAR_106 · — · video8s · 24:12–24:20
[ACTION-VI] Bên trong thành, sau 치 đông-nam: 박기철 (tay còn băng mỏng) bước đo từ chân tường trong ra sân, ngẩng nhìn mặt tường trong cao ngang hai người che khuất lỗ châu mai của 치; 한승우 và 을보 đứng nhìn theo bước ông.
[SOUND] bước chân đếm, gió.
N: 치 뒤에는 안쪽 담이 있었습니다. 전차는 담 너머를 볼 수 없었습니다. 박기철은 담을 걸음으로 쟀습니다.
박기철: 안쪽 벽을 헐고 흙을 쌓으면… 오릅니다.

### SC_176 · LOC_002_YODONGSEONG (tường trong sau 치) · CHAR_106 · PROP_019 · video8s · 24:20–24:28
[ACTION-VI] 을보 căng sợi dây đo lên mặt tường trong, gõ búa nhỏ vào từng hàng đá từ trên xuống, nghe tiếng; dừng ở hàng thứ mười, gõ hai lần.
[SOUND] búa gõ đá, dây.
N: 지난달 을보는 돌은 아래부터 쌓는다고 했습니다. 헐 때는 반대였습니다.
을보: 이 돌은 뺄 수 있어. 위에서부터 열 줄.

### SC_177 · LOC_002_YODONGSEONG (sau 치 đông-nam) · CHAR_104, CHAR_003 · — · video8s · 24:28–24:36
[ACTION-VI] 고정수 tới, thấy sợi dây đo trên tường trong và 을보 với búa; ông đặt bàn tay lên đá, quay lại nhìn 박기철 và 한승우, giọng cứng.
[SOUND] chìa khóa, gió.
N: 성주에게 담은 곡식보다 오래된 것이었습니다. 그는 처음으로 아니라고 했습니다.
고정수: 내 성벽을 헐자는 것이오? 조상이 쌓은 돌이오.

### SC_178 · LOC_002_YODONGSEONG (sau 치 đông-nam) · CHAR_101, CHAR_104 · — · video8s · 24:36–24:44
[ACTION-VI] 을지문덕 từ bậc thang 치 bước xuống — ông đã ở trên đó nhìn — đi ngang qua 고정수, đặt tay lên vai ông một cái, nói không cao giọng, rồi chỉ 을보 bắt đầu.
[SOUND] bước chân trên bậc đá, tay trên giáp.
N: 대장군은 성주를 꾸짖지 않았습니다. 담이 무엇을 위한 것인지 말했습니다.
을지문덕: 조상은 돌을 지키라고 쌓지 않았소. 사람을 지키라고 쌓았소.

### SC_179 · LOC_002_YODONGSEONG (từ mặt tường nhìn xuống: công trường sau 치 + cổng đông phía sau — ken-burns) · thợ đá Goguryeo, lính Hàn, CHAR_005, CHAR_106 · PROP_019 · still_kenburns · 24:44–24:56
[ACTION-VI] Ảnh: công trường sau 치 — thợ đá Goguryeo cạy từng hàng đá tường trong bằng thanh bẩy sắt của 을보, lính Hàn và dân đổ giỏ đất thành dốc thoai thoải lên chân 치; 태오 vác giỏ; trên 치, hai thợ đục rộng một lỗ châu mai thành khe vuông; ở hậu cảnh, vòm cổng đông nhỏ có giàn gỗ — thợ đá đục rộng hai bên vách vòm, đá mới lộ màu trắng; 을보 đứng giữa, chỉ hai hướng. Ken-burns trượt từ hàng đá tháo ra qua khe đục tới vòm cổng trắng.
[SOUND] bẩy đá, giỏ đất đổ, đục.
N: 사흘이 걸렸습니다. 열 줄의 돌이 내려왔고, 흙 삼천 짐이 올라갔습니다. 치의 총안 하나가 쇠수레의 눈 크기로 넓어졌습니다. 동문도 반 미터 넓어졌습니다. 두 달 전의 그 반 미터였습니다. 천사백 년 전의 담이 오늘의 쇠를 위해 몸을 바꿨습니다.

### SC_180 · LOC_002_YODONGSEONG (dốc đất sau 치) · CHAR_003 · — · video8s · 24:56–25:04
[ACTION-VI] 박기철 đi lên dốc đất mới đắp với cây gậy đo, dừng giữa dốc, ngoái nhìn xuống chân dốc rồi lên 치; mặt nhăn như nếm thuốc 을보.
[SOUND] đất mới dưới giày, gió.
N: 흙은 공짜였습니다. 오르는 것은 아니었습니다. 박기철은 언덕을 기름으로 쟀습니다.
박기철: 경사 이십 도. 오르는 데 기름 십 킬로 몫입니다.

### SC_181 · LOC_002_YODONGSEONG (đại sảnh, ban ngày) · CHAR_101, CHAR_104, CHAR_001 · — · video8s · 25:04–25:12
[ACTION-VI] Đại sảnh: bản đồ da; 을지문덕 đặt lên bản đồ trước tường một viên sỏi trắng — cách tường một đốt ngón tay; 고정수 gật; 한승우 nhìn viên sỏi.
[SOUND] sỏi trên da.
N: 네 번째 흰 천의 자리는 백 걸음이었습니다. 계획은 황제의 머릿속에 있었습니다. 황제가 제 명령을 지키는가, 버리는가.
을지문덕: 탑이 백 걸음에 오면 깃발을 올리오.

### SC_182 · LOC_002_YODONGSEONG (vòm cổng đông đang đục rộng, walk-and-talk) · CHAR_105, CHAR_001, thợ đá · — · video8s · 25:12–25:20
[ACTION-VI] 해모루 và 한승우 đi qua vòm cổng đông nhỏ đang được đục rộng — thợ đá Goguryeo đứng trên giàn đục vách vòm, bụi đá rơi, đá mới trắng hai bên; 해모루 nói tiếp kế, cúi tránh giàn; 한승우 đi sát vách, tay lướt trên đá vừa đục.
[SOUND] bước chân, gió, đục xa.
N: 흰 천이 통하면 탑은 백 걸음에서 설 것이었습니다. 선 탑은 과녁이었습니다. 우는 쇠는 그때 울 것이었습니다.
해모루: 황제가 제 명령을 지키면 탑은 서오. 그럼 우는 쇠 마흔 발이오.

### SC_183 · LOC_002_YODONGSEONG (vòm cổng đông) · CHAR_001, CHAR_106 · — · video8s · 25:20–25:28
[ACTION-VI] 한승우 dừng dưới vòm, ướm sải tay hai vách vừa đục — rộng hơn hôm 1화 một gang mỗi bên; 을보 trên giàn gõ búa xuống vách, nheo mắt nhìn ông; 한승우 nói vế còn lại — vế của mình.
[SOUND] gió, cờ.
N: 두 갈래였습니다. 어느 쪽이든 마흔 발이거나 열 발이었습니다. 그 이상은 없었습니다. 그리고 문은 이제 반 미터 넓었습니다.
한승우: 지키지 않으면, 전차입니다. 열 발.

### SC_184 · LOC_002_YODONGSEONG (bãi cỏ phía nam trước 치 đông-nam, đêm — ken-burns) · CHAR_006, lính Goguryeo · — · still_kenburns · 25:28–25:38
[ACTION-VI] Ảnh: đêm, 백성민 và bốn lính Goguryeo trên bãi cỏ nát phía nam trước 치 đông-nam đặt những tảng đá quét vôi trắng thành hàng — 100, 200, 300 bước từ chân tường — dưới ánh đuốc che tay; trên tường, cung thủ canh. Ken-burns từ mốc gần ra mốc xa.
[SOUND] đá đặt cỏ, đuốc, dế.
N: 우는 쇠는 백 발이었습니다. 겨냥에 쓸 발은 없었습니다. 그래서 돌로 쟀습니다. 흰 돌 하나가 백 걸음이었습니다. 화살 대신 돌이 표적을 등록했습니다.

### SC_185 · LOC_003_CHEONDUNG_BASE (cửa thung, đường mòn) · CHAR_001, CHAR_003, CHAR_006 · — · video8s · 25:38–25:46
[ACTION-VI] Cửa thung: 한승우 chỉ gậy lên đường mòn đi qua bụi sồi lên đồi; 박기철 và 백성민 nhìn theo; 백성민 nhìn lâu hơn — đó là đường 탁발흠 đã xuống.
[SOUND] gió trong lá, gậy trên đất.
N: 싸움 다음 날 밤, 골짜기를 뜬다. 길은 하나였습니다. 탁발흠이 내려온 길이었습니다. 그도 그 길을 알았습니다.
한승우: 전투 다음 날 밤, 산길로 골짜기를 뜬다.

### SC_186 · LOC_003_CHEONDUNG_BASE (đỉnh đồi phía địch, hoàng hôn) · CHAR_205, 선비 부장 · VEH_206 · video8s · 25:46–25:54
[ACTION-VI] Hoàng hôn: 탁발흠 và phó tướng nằm sau tảng đá trên đỉnh đồi nhìn xuống cửa thung và đường mòn; phó tướng chỉ xuống lối mòn, đề nghị; 탁발흠 không trả lời — nhìn đường mòn, rồi nhìn xa hơn về phía nam.
[SOUND] gió, ngựa buộc xa.
N: 탁발흠은 골짜기의 문을 알았습니다. 문을 막는 것은 쉬웠습니다. 그는 대답하지 않았습니다.
선비 부장: 낭장, 길목에 기병을 두겠습니다.

### SC_187 · LOC_003_CHEONDUNG_BASE (nóc 천둥 2, đêm) · CHAR_002, 포수 · VEH_002 · video8s · 25:54–26:02
[ACTION-VI] Đêm: 오태민 cúi vào cửa nóc 천둥 2, mắt dán kính nhiệt tháp pháo — màn hình: bốn chấm nóng bò xuống sườn theo đường mòn, một chấm sáng hơn (nồi lửa); ông ra lệnh nội bộ xe.
[SOUND] kính nhiệt bíp, intercom.
[COMBAT]
N: 두 번째 불은 왔습니다. 이번에는 열이 먼저 보였습니다. 골짜기는 어젯밤부터 밤새 깨어 있었습니다.
오태민: 포수, 능선 열한 시. 점사.

### SC_188 · LOC_003_CHEONDUNG_BASE (sườn đồi, đêm) · Tiên Ti · VEH_002, PROP_016 · video8s · 26:02–26:10
[ACTION-VI] Loạt 40mm nổ trên sườn — đất và lá tung, một nồi lửa vỡ bung than đỏ thành hoa; bốn bóng người tản ngược lên đồi, một người lết. Wide từ thung nhìn lên.
[SOUND] 40mm ba phát, nồi vỡ, tiếng hét.
[COMBAT]
N: 넷이 왔고, 셋이 돌아갔습니다. 불은 항아리째 깨졌습니다.

### SC_189 · LOC_003_CHEONDUNG_BASE (bên 천둥 2, sáng) · CHAR_002, CHAR_001 · VEH_002 · video8s · 26:10–26:18
[ACTION-VI] Sáng: 한승우 đứng bên 천둥 2, chỉ hai K21 rồi chỉ đường mòn — giao thung lũng; 오태민 nghe, mặt đỏ, bước tới một bước.
[SOUND] gió, xích lạnh.
N: 어젯밤이 오태민의 자리를 정했습니다. 그는 그 자리를 원하지 않았습니다.
오태민: 골짜기를 지키란 말씀입니까? 전차 옆은 제 자리입니다.

### SC_190 · LOC_003_CHEONDUNG_BASE (bên 천둥 2) · CHAR_001 · VEH_002 · video8s · 26:18–26:26
[ACTION-VI] 한승우 không lùi, không cao giọng; ngón tay chỉ lên sườn đồi nơi đêm qua nồi lửa vỡ.
[SOUND] gió.
N: 한승우는 이유를 말했습니다. 요하에서는 말하지 않았습니다. 그것이 달라진 점이었습니다.
한승우: 골짜기는 두 번째 불이 온다. 그걸 막는 게 네 자리다.

### SC_191 · LOC_003_CHEONDUNG_BASE (bên 천둥 2) · CHAR_002 · VEH_002 · video8s · 26:26–26:34
[ACTION-VI] 오태민 đập lòng bàn tay lên hông 천둥 2 — tiếng thép đục; đứng thở; rồi kéo kính bảo hộ xuống mắt, quay đi kiểm tra xích. Không thoại.
[SOUND] tay đập thép, thở, xích.
N: 오태민은 따랐습니다. 이번에는. 요하의 여울에서 그는 세 시간을 따랐습니다. 이번에는 며칠이 될지 아무도 몰랐습니다.

### SC_192 · LOC_002_YODONGSEONG (chân dốc đất, chiều) · CHAR_101, CHAR_003 · — · video8s · 26:34–26:42
[ACTION-VI] Chân dốc đất: 을지문덕 đi ngang qua 박기철 đang kiểm tra độ chặt của đất bằng gót giày; ông dừng một bước, hỏi nhỏ, chỉ cho 박기철 nghe, rồi đi tiếp lên bậc 치.
[SOUND] gót giày trên đất, bước chân xa dần.
N: 질문은 스쳐 가듯 왔습니다. 그의 질문은 늘 그렇게 왔습니다.
을지문덕: 청천강까지 며칠이오?

### SC_193 · LOC_002_YODONGSEONG (chân dốc đất) · CHAR_003 · — · video8s · 26:42–26:50
[ACTION-VI] 박기철 ngẩng lên — 을지문덕 đã lên nửa bậc thang; ông hỏi với theo, không có câu trả lời; đứng đó với gót giày dính đất, nhìn lưng ông đi khuất.
[SOUND] gió, bậc đá.
N: 청천강. 박기철은 그 강을 몰랐습니다. 남쪽 어디였습니다. 왜 그 강인지 그는 아직 몰랐습니다. 아는 사람은 담 위로 올라가고 있었습니다.
박기철: …청천강 말입니까? 왜 청천강을…

### SC_194 · LOC_002_YODONGSEONG (aerial đêm 6월 10 — ken-burns) · — · VEH_201, PROP_021 · still_kenburns · 26:50–27:02
[ACTION-VI] Ảnh aerial đêm: hàng tháp phủ đất đã tiến vào cách thành một cây số, hàng nghìn đèn lồng; phía tây, 육합성 sáng vàng; phía nam thành, một đài gỗ cao mới dựng với lọng vàng, đuốc quanh chân đài; thành tối, chỉ vài đuốc trên tường. Ken-burns từ đài vàng kéo ra toàn cảnh.
[SOUND] trống đêm nhiều lớp, gió trên cao.
N: 6월 10일 밤. 탑이 천 미터까지 왔습니다. 성 남쪽에 높은 대가 섰습니다. 황제의 자리였습니다. 역사는 다음 날을 기록했습니다. 6월 11일, 황제가 요동성 남쪽에 서서 장수들을 꾸짖었습니다. 그날이 내일이었습니다.

### SC_195 · LOC_002_YODONGSEONG (vòm cổng đông đã đục rộng, đêm) · CHAR_003, kíp K2, lính Goguryeo · VEH_001 · video8s · 27:02–27:10
[ACTION-VI] Đêm: K2 chui qua vòm cổng đông vừa đục — váy xích cách vách đá mới trắng hai ngón tay, bụi đá rơi trên nóc, động cơ gầm trầm dội trong vòm; 박기철 đi lùi trước mũi xe với đèn pin che tay, tay kia ra hiệu từng tấc; lính Goguryeo cầm đuốc nép sát vách. Máy từ trong thành nhìn ra vòm.
[SOUND] động cơ K2 dội trong vòm đá, xích trên đá, bụi đá rơi trên thép, đuốc.
N: 두 달 만이었습니다. 문은 반 미터 넓어져 있었습니다. 을보의 돌이었습니다. 두 달 동안 골짜기의 돌이던 것이, 오늘 밤 다시 쇠수레였습니다.

### SC_196 · LOC_002_YODONGSEONG (chân dốc đất sau 치, đêm) · CHAR_003, CHAR_106, kíp K2 · VEH_001 · video8s · 27:10–27:18
[ACTION-VI] K2 dừng ở chân dốc đất, mũi hướng lên 치, đuốc hai hàng dọc dốc; 을보 đứng trên dốc giơ tay ra hiệu chờ; 박기철 gõ hai cái lên váy xích rồi giơ ngón cái. Lính Goguryeo hai bên nhìn khối thép dưới đuốc, không ai nói. Không thoại.
[SOUND] động cơ chờ, đuốc, giáp.
N: 언덕 아래에 전차가 섰습니다. 언덕 위에는 치와 넓힌 총안이 있었습니다. 열 발이 올라갈 자리였습니다.

### SC_197 · LOC_002_YODONGSEONG (치 đông-nam, đêm — ken-burns) · CHAR_104 · PROP_021 · still_kenburns · 27:18–27:30
[ACTION-VI] Ảnh: 고정수 (băng trán) đứng trên 치 đêm, hai tay cầm tấm vải trắng gấp vuông, nhìn về phía nam nơi lọng vàng trên đài quan sát sáng đuốc; sau lưng ông, đỉnh nòng pháo K2 chưa lên tới khe. Ken-burns từ tấm vải trắng qua vai ông tới lọng vàng.
[SOUND] gió, trống Tùy đêm, đuốc.
N: 흰 천은 네 번째였습니다. 세 번은 통했습니다. 네 번째는 황제가 백 리 밖이 아니라 오 리 밖에 있었습니다. 황제는 자신의 명령을 지킬까요?

[MID-ROLL 4 · 27:30]

[Kết thúc Phần 9]

## [Phần 10] 제3차 공성전 — 「제3차 공성전」 / Trận đánh quyết định  (27:30–34:30) — 6 phase
> Tóm tắt VI: Phase 1 (27:30–28:42) — sau mid-roll: K2 leo dốc đất lên 치 trong đêm, đuốc hai bên (không thoại). Bình minh 6월 11 [史]: 40+ tháp + 충차 + 운제; 양제 trên đài nam thành, lọng vàng: "짐이 왔다." K2 sau 치, 태극기 cạnh 삼족오. Mốc đá 100 bước — 고정수: "올려라." Tháp không dừng; kỵ sứ Tùy hét: "폐하께서 항복을 받지 말라 하셨다!" — "황제가 눈치챘소." Phase 2 (28:42–30:02) — cối 40 viên: chiếu đất hứng, 3 tháp cháy, 37 tới; thang, cận chiến tường nam thuần cổ; 양제 nhìn ba tháp cháy; đông: 3 tháp cách 200 bước — 을지문덕: "이제 쇠수레요." Phase 3 (30:02–31:30) — viên 1: tháp vỡ đôi, cả đại quân ngừng một giây; 양제 giật vai; viên 2–6: tháp 300 m, 충차; tướng Tùy: "저 구멍이다! 쇠뇌를 저 구멍에 모아라!" Phase 4 (31:30–33:00, NARRATOR IM) — nỏ tập trung vào khe, lính Goguryeo bên K2 trúng; hầm sập 80 m tường bắc → lỗ hổng → bộ binh Tùy tràn; K3 không che nổi hai nơi, nòng đỏ; PZF ×2 vào 운제, ×3 vào tháp áp lỗ hổng; K2 viên 7–10. Phase 5 (33:00–34:04) — 고정수 dẫn giáo dài vào lỗ hổng; 해모루 xuất kích cổng bắc; 오태민 bỏ thung lũng đưa 천둥 2 ra cổng bắc bắn 40mm sườn tổ đẩy tháp (trái lệnh lần 2, đúng lúc); lỗ hổng giữ được; "얼마나 남았소?" — "열두 발입니다." — "그럼 이제 내려가시오. 그건 여기 것이 아니오." Phase 6 (34:04–34:30) — hoàng hôn, Tùy lùi, tháp cháy rải đồng; 양제 rời đài không nói; K2 lùi xuống dốc, 박기철 tay băng đi cạnh, tường Goguryeo reo.
> Chức năng: BATTLE · Combat: SC_199–249 · Tài nguyên: K2 22→12 · cối 100→60 · PZF 17→12 · 40mm −60 (220) · K3 −1.200 · 4 thương binh · Quyết định lịch sử: 양제 bỏ lệnh nhận hàng của chính mình; 고정수 dẫn giáo; 을지문덕 rút K2 khi còn 12 · Enemy adaptation: nỏ vào khe; hầm · Payoff: hầm (P1), cờ trắng (P2), "열 발" (P8), mốc đá (P9) · Open loop: "성은 버텼습니다. 황제는 그날 밤 다른 지도를 펼쳤습니다."
> [NARRATOR IM LẶNG] 31:30–33:00. Sau mid-roll 4: SC_198 K2 leo dốc, không thoại.

### — Phase 1 · 탑이 오다, 흰 천 / Tháp tiến, cờ trắng (27:30–28:42) —

### SC_198 · LOC_002_YODONGSEONG (dốc đất sau 치 đông-nam, đêm) · kíp K2, CHAR_003, CHAR_106 · VEH_001 · video8s · 27:30–27:38
[ACTION-VI] K2 leo dốc đất: xích cắn đất mới, đất trượt hai bên, mũi xe ngóc lên trời đêm rồi hạ xuống khi tới mặt 치; đuốc hai hàng dọc dốc sáng lên thân xe ba màu; 을보 đứng trên 치 giơ tay dừng; 박기철 đi bộ bên xích. Low-angle từ chân dốc. Không thoại, không narration.
[SOUND] động cơ gầm lên dốc, xích nghiến đất, đuốc.

### SC_199 · LOC_002_YODONGSEONG (aerial bình minh) · — · VEH_201, VEH_202, VEH_203 · video8s · 27:38–27:46
[ACTION-VI] Aerial bình minh: từ ba mặt, hàng tháp phủ đất lăn về thành, xe húc phủ bùn trên đường đắp, thang mây thành rừng; trống hàng trăm cái; cỏ nát thành bụi vàng. Máy lướt cao.
[SOUND] trống dồn ba mặt, bánh gỗ, hô đồng thanh.
[COMBAT]
N: 6월 11일. 세 번째 공성이었습니다. 탑은 마흔이 넘었고, 모두 흙을 입었습니다.

### SC_200 · LOC_004_YUKHAPSEONG (đài quan sát nam thành) · CHAR_201, tướng Tùy · PROP_021 · video8s · 27:46–27:54
[ACTION-VI] Đài gỗ cao phía nam thành: 양제 dưới lọng vàng, giáp mạ vàng, quạt tròn; hàng tướng Tùy quỳ dưới bậc đài; ông nhìn thành, nói với hàng tướng mà không hạ mắt xuống họ.
[SOUND] lọng lụa gió, giáp tướng quỳ, trống.
[COMBAT]
N: 역사는 이날을 기록했습니다. 황제가 성 남쪽에 서서 장수들을 꾸짖었습니다. 그대들은 짐이 겁쟁이라 여기는가. 그는 보러 왔습니다.
수 양제: 짐이 왔다. 그대들이 무엇을 하는지, 짐이 보겠다.

### SC_201 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001, CHAR_101, CHAR_104, 전차장 · VEH_001, PROP_011, PROP_012 · video8s · 27:54–28:02
[ACTION-VI] Trên 치: tháp pháo K2 nhô sau lan can đá, nòng thò qua khe đục; 전차장 nửa người trên cupola; 한승우 bên xe với radio, vai áo 태극기 cạnh cột cờ 삼족오 cắm ở góc 치; 을지문덕 giáp đủ bộ, lông chỏm, đứng ở lan can; 고정수 cầm giáo có vải trắng cuộn. Cung thủ Goguryeo đã lùi khỏi 치 theo tay 박기철 vẫy. Máy low-angle từ sân lên.
[SOUND] động cơ K2 chờ nhỏ, cờ, trống.
[COMBAT]
N: 치 위에 쇠수레가 있었습니다. 돌 담과 쇠 사이에 두 깃발이 있었습니다. 열 발이 그 사이에 있었습니다.

### SC_202 · LOC_002_YODONGSEONG (치 đông-nam, lan can) · CHAR_006 · PROP_006 · video8s · 28:02–28:10
[ACTION-VI] 백성민 ống nhòm: ba tháp phía đông-nam lăn qua mốc đá trắng xa nhất, rồi mốc giữa; bánh tháp lăn đè lên mốc 100 bước. Ông hạ ống nhòm, nói không đổi giọng.
[SOUND] bánh gỗ, trống gần.
[COMBAT]
N: 흰 돌 하나가 바퀴 밑에 들어갔습니다.
백성민: 백 걸음.

### SC_203 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_104 · — · video8s · 28:10–28:18
[ACTION-VI] 고정수 tự dựng ngọn giáo lên, vải trắng bung ra trong gió trên đầu 치; ông nhìn về đài vàng phía nam, không nhìn tháp.
[SOUND] vải bung gió, trống.
[COMBAT]
N: 네 번째 흰 천이었습니다. 이번에는 황제가 보고 있었습니다.
고정수: 올려라.

### SC_204 · LOC_002_YODONGSEONG (bãi đông-nam trước 치) · 수 전령, lính Tùy · VEH_201 · video8s · 28:18–28:26
[ACTION-VI] Các tháp… không dừng. Một kỵ sứ Tùy phi dọc hàng người đẩy, giơ cờ lệnh đỏ, hét lệnh của hoàng đế cho từng tổ; người đẩy cúi đầu đẩy mạnh hơn. Tracking theo kỵ sứ.
[SOUND] vó ngựa, hét lặp lại, bánh gỗ không ngừng.
[COMBAT]
N: 황제의 새 명령은 벌판을 달렸습니다. 지난 명령보다 빨랐습니다.
수 전령: 폐하께서 항복을 받지 말라 하셨다!

### SC_205 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_104, CHAR_101 · — · video8s · 28:26–28:34
[ACTION-VI] 고정수 hạ ngọn giáo, vải trắng rũ xuống đá; ông nói với 한승우 bên cạnh, không quay đầu — sự thật, không ngạc nhiên; 을지문덕 phía sau nghe.
[SOUND] vải rơi trên đá, trống.
[COMBAT]
N: 황제는 제 명령을 버렸습니다. 세 번 속은 사람이 네 번째에는 속지 않았습니다.
고정수: 황제가 눈치챘소.

### SC_206 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101, CHAR_001 · EQP_002 · video8s · 28:34–28:42
[ACTION-VI] 을지문덕 gật một cái như đã đoán; nói với 한승우 hai chữ đầu của kế B; 한승우 giơ radio.
[SOUND] PTT, trống.
[COMBAT]
N: 계획은 두 갈래였습니다. 첫 갈래가 닫혔습니다. 그는 둘째 갈래를 열었습니다.
을지문덕: 우는 쇠부터. 마흔 발.

### — Phase 2 · 우는 쇠가 흙을 만나다 / Cối vô hiệu (28:42–30:02) —

### SC_207 · LOC_003_CHEONDUNG_BASE (hố cối) · 사수, tổ cối · WPN_002 · video8s · 28:42–28:50
[ACTION-VI] Hố cối: xạ thủ hô lệnh; hai khẩu cối bắn liên tục, tổ viên thả đạn theo nhịp, thùng đạn cối mở xếp hàng, vỏ hộp bay; nòng nóng bốc hơi.
[SOUND] "퉁" dồn dập không ngớt, thùng đạn.
[COMBAT]
N: 마흔 발. 백 발 중 마흔이었습니다. 표적은 흰 돌이었습니다.
사수: 1번, 2번, 표석 백. 스무 발씩.

### SC_208 · LOC_002_YODONGSEONG (đỉnh tháp phủ đất) · lính Tùy · VEH_201 · video8s · 28:50–28:58
[ACTION-VI] Đạn cối nổ trên đỉnh tháp: chiếu bùn ướt bung lên, bùn văng như mưa, vài thanh gỗ gãy — nhưng tháp vẫn lăn; lính Tùy tầng dưới lau bùn khỏi mặt. Trung cảnh từ tường.
[SOUND] nổ bị bùn nuốt "퍽", bùn rơi, bánh gỗ vẫn lăn.
[COMBAT]
N: 흙이 쇠를 먹었습니다. 두 달 전 탑 둘을 태운 것과 같은 쇠였습니다. 이번에는 진흙만 튀었습니다.

### SC_209 · LOC_002_YODONGSEONG (hàng tháp, wide) · — · VEH_201 · video8s · 28:58–29:06
[ACTION-VI] Ba tháp mất chiếu bùn ở đỉnh bén lửa từ tầng trên, cháy dọc xuống — còn lại vẫn tiến qua khói của ba tháp cháy. Wide từ tường.
[SOUND] lửa, trống không ngớt.
[COMBAT]
N: 셋. 마흔 발에 셋이었습니다. 서른일곱이 왔습니다.

### SC_210 · LOC_002_YODONGSEONG (mặt tường nam) · lính Goguryeo, lính Tùy · WPN_101, VEH_203 · video8s · 29:06–29:14
[ACTION-VI] Tường nam: thang mây dựng dày dọc tường, cung Goguryeo bắn xuống, đá lăn, nước sôi; lính Tùy khiên tròn leo lên như kiến. Low-angle từ hào.
[SOUND] dây cung, thang gỗ, thét.
[COMBAT]
N: 남쪽 담은 옛 방식으로 싸웠습니다. 돌과 물과 화살.

### SC_211 · LOC_002_YODONGSEONG (mặt tường nam) · lính Goguryeo · — · video8s · 29:14–29:22
[ACTION-VI] Bốn lính Goguryeo dùng sào chạc đẩy một thang đầy người bật khỏi tường; một lính Tùy đã lên tới lan can bị giáo hất ngược xuống. Trung cảnh, không gore.
[SOUND] sào gỗ, thang đổ, giáp rơi.
[COMBAT]
N: 사다리 하나에 스무 명이 있었습니다. 장대 하나가 스무 명을 떨어뜨렸습니다.

### SC_212 · LOC_002_YODONGSEONG (mặt tường nam, tháp áp tường) · CHAR_104, lính hai bên · VEH_201 · video8s · 29:22–29:30
[ACTION-VI] Cầu tháp phủ bùn hạ xuống lan can tường nam; 고정수 (băng trán) cầm giáo đón ở đầu cầu cùng hàng giáo; lính Tùy ào qua cầu, hai bên đâm nhau trên mặt tường hẹp. Cận trung.
[SOUND] cầu đập đá, giáo, thét.
[COMBAT]
N: 성주는 이번에도 첫 번째 창이었습니다.

### SC_213 · LOC_004_YUKHAPSEONG (đài quan sát nam thành) · CHAR_201 · PROP_021 · video8s · 29:30–29:38
[ACTION-VI] Trên đài: 양제 nhìn ba cột khói tháp cháy giữa hàng tháp; quạt vẫn phe phẩy; tướng bên cạnh cúi báo số; ông không đổi sắc mặt.
[SOUND] lọng gió, trống xa.
[COMBAT]
N: 마흔 중 셋. 황제는 그 셈을 들었습니다. 셋은 그에게 아무것도 아니었습니다.

### SC_214 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_006 · PROP_006 · video8s · 29:38–29:46
[ACTION-VI] 백성민 ống nhòm về phía đông-nam: ba tháp phủ đất qua mốc 300 bước đang tới mốc 200; xa hơn về phía nam, xe húc phủ bùn bò lên đường đắp cổng nam 옹성. Báo.
[SOUND] bánh gỗ gần, PTT.
[COMBAT]
N: 동남쪽이었습니다. 쇠수레가 보는 쪽이었습니다.
백성민: 동남쪽, 탑 셋. 이백 걸음.

### SC_215 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101, CHAR_001 · VEH_001 · video8s · 29:46–29:54
[ACTION-VI] 을지문덕 nhìn ba tháp, rồi quay sang 한승우 — hai chữ, và bàn tay ông mở ra: mười ngón.
[SOUND] trống gần, gió.
[COMBAT]
N: 흰 천이 실패했고, 우는 쇠가 실패했습니다. 남은 것은 열 발이었습니다.
을지문덕: 이제 쇠수레요.

### SC_216 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001 · EQP_002, VEH_001 · video8s · 29:54–30:02
[ACTION-VI] 한승우 bấm radio nội bộ với K2 cách ông ba bước — tiếng ông vào tai nghe kíp xe; ông nhìn tháp đầu tiên qua khe.
[SOUND] PTT, động cơ K2 tăng ga.
[COMBAT]
N: 쇠수레는 세 걸음 옆에 있었습니다. 목소리는 무전으로 갔습니다. 그것이 규칙이었습니다.
한승우: 천둥 1, 여기는 천둥 지휘. 동남쪽 첫 번째 탑. 한 발.

### — Phase 3 · 돌을 지나는 천둥 / Sấm qua đá (30:02–31:30) —

### SC_217 · LOC_002_YODONGSEONG (trong K2) · 전차장, 포수 · VEH_001 · video8s · 30:02–30:10
[ACTION-VI] Trong tháp pháo: màn hình nhiệt của 포수 — khối tháp phủ đất, hình chữ thập; bộ đếm "잔탄 22" sáng góc màn hình; 전차장 đáp radio rồi hạ lệnh.
[SOUND] intercom, quạt tháp pháo, máy nạp đạn kêu.
[COMBAT]
N: 스물두 발이 처음으로 하나가 될 참이었습니다.
전차장: 천둥 지휘, 여기는 천둥 1. 목표 확인. 발사.

### SC_218 · LOC_002_YODONGSEONG (치 đông-nam, wide) · — · VEH_001 · video8s · 30:10–30:18
[ACTION-VI] K2 bắn qua khe đục: chớp lửa dài ra khỏi nòng, sóng chấn thổi bụi đá và cỏ khô bay khỏi mặt 치, cờ 삼족오 giật ngang; lính Goguryeo dọc tường ôm tai. Wide từ tường nam nhìn sang.
[SOUND] "쾅" xé, dội nhiều lần qua đồng bằng, tai ù.
[COMBAT]
N: 돌 담이 천둥을 냈습니다.

### SC_219 · LOC_002_YODONGSEONG (tháp thứ nhất phía đông) · lính Tùy · VEH_201 · video8s · 30:18–30:26
[ACTION-VI] Tháp phủ đất thứ nhất vỡ đôi ở tầng giữa — chiếu bùn, gỗ, người bung ra hai phía; nửa trên đổ nghiêng xuống đám người đẩy; bụi đất trùm. Trung cảnh từ tường.
[SOUND] gỗ vỡ tan, đổ, thét bị bụi nuốt.
[COMBAT]
N: 첫 번째 탑은 흙째 갈라졌습니다. 흙은 우는 쇠를 막았습니다. 이것은 막지 못했습니다.

### SC_220 · LOC_002_YODONGSEONG (đồng bằng, wide) · đại quân Tùy · WPN_201, VEH_201 · video8s · 30:26–30:34
[ACTION-VI] Wide: cả cánh đồng Tùy — người đẩy tháp, hàng khiên, tay trống — khựng lại một giây: trống ngừng, đầu ngẩng về phía tiếng nổ; rồi trống nổi lại, rời rạc. Aerial trung.
[SOUND] im một giây trọn, rồi trống lộn xộn.
[COMBAT]
N: 한 순간, 백만이 멈췄습니다. 두 달 전 문 앞의 만 명이 아니었습니다. 벌판 전체였습니다.

### SC_221 · LOC_004_YUKHAPSEONG (đài quan sát nam thành) · CHAR_201 · PROP_021 · video8s · 30:34–30:42
[ACTION-VI] Đài: 양제 — vai giật một cái khi tiếng nổ dội tới; quạt dừng giữa chừng; các tướng dưới đài ngước nhìn ông; ông không nhìn lại ai, mắt ở cột bụi phía đông. Trung cảnh, không cận mặt lâu. Không thoại.
[SOUND] tiếng nổ dội tới muộn, lọng lụa, im.
[COMBAT]
N: 황제도 들었습니다. 두 달 반 전 탁발흠이 말한 천둥이었습니다. 이번에는 귀로였습니다.

### SC_222 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001, 전차장 · VEH_001, EQP_002 · video8s · 30:42–30:50
[ACTION-VI] 한승우 nhìn qua khe: tháp thứ hai vẫn lăn qua bụi; 전차장 trên cupola nhìn ông; ông bấm radio, giọng không đổi. Bộ đếm trong xe (insert nhanh): 21.
[SOUND] PTT, máy nạp đạn.
[COMBAT]
N: 스물하나. 한승우는 그 수를 말하지 않았습니다. 다음 탑을 말했습니다.
한승우: 천둥 1, 두 번째 탑. 계속.

### SC_223 · LOC_002_YODONGSEONG (hai tháp phía đông-nam, 300 m) · lính Tùy · VEH_201 · video8s · 30:50–30:58
[ACTION-VI] Hai phát nối nhau: tháp thứ hai bung tầng trên; tháp thứ ba lãnh đạn ở chân, nghiêng chậm rồi đổ tựa vào mặt tường nam gần góc đông-nam, cầu bập bênh gãy treo lủng lẳng. Wide từ tường.
[SOUND] hai "쾅", gỗ đổ tựa đá, dây gai đứt.
[COMBAT]
N: 둘, 셋. 탑 하나는 담에 기대어 죽었습니다.

### SC_224 · LOC_002_YODONGSEONG (đường đắp cổng nam 옹성) · lính Tùy · VEH_202 · video8s · 30:58–31:06
[ACTION-VI] Xe húc phủ bùn hai lớp lăn trên đường đắp cổng nam 옹성 — trong tầm nòng từ 치 đông-nam; phát thứ tư: mái bùn và gỗ bốc lên trọn khối, xe đứng khựng, cây phá cổng đầu sắt cắm xuống đất. Trung cảnh.
[SOUND] "쾅", bùn và gỗ rơi.
[COMBAT]
N: 넷. 흙 두 겹은 한 발의 값을 못 했습니다.

### SC_225 · LOC_002_YODONGSEONG (chân dốc đất, trong thành) · CHAR_003 · VEH_001 · video8s · 31:06–31:14
[ACTION-VI] Chân dốc đất: 박기철 đứng nhìn lên đuôi K2 trên 치, hai tiếng nổ nữa dội xuống — ông gập ngón tay băng, đếm thành tiếng; sau ông, dân Goguryeo trong sân bịt tai.
[SOUND] hai "쾅" dội trong sân, ngón tay băng.
[COMBAT]
N: 다섯, 여섯. 박기철은 언덕 아래에서 셌습니다. 위에서는 을지문덕이 셌습니다.
박기철: 여섯.

### SC_226 · LOC_002_YODONGSEONG (sau hào phía đông-nam, tướng Tùy) · 수 공성총관, nỏ thủ Tùy · WPN_201 · video8s · 31:14–31:22
[ACTION-VI] Tướng công thành trên ngựa phía đông-nam, thấy khói xám tuôn ra từ một khe vuông trên 치 sau mỗi tiếng; ông đứng lên bàn đạp, đao chỉ thẳng khe, quát hàng nỏ thủ đang nấp sau khiên lớn.
[SOUND] quát, nỏ lên dây hàng loạt.
[COMBAT]
N: 총관은 두 달 전과 같은 것을 보았습니다. 구멍. 이번에는 답이 있었습니다.
수 공성총관: 저 구멍이다! 쇠뇌를 저 구멍에 모아라!

### SC_227 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101, lính Goguryeo · VEH_001 · video8s · 31:22–31:30
[ACTION-VI] Trên 치 và tường đông: lính Goguryeo giơ giáo reo vang khi tháp thứ ba nằm tựa tường; 을지문덕 không reo — ông nhìn xuống hàng nỏ Tùy đang dàn thành khối trước hào, hàm siết. Cận ông, nền reo hò.
[SOUND] reo hò, nỏ lên dây xa.
[COMBAT]
N: 담은 환호했습니다. 을지문덕은 환호하지 않았습니다. 그는 쇠뇌를 보고 있었습니다.

[NARRATOR IM LẶNG — 31:30 → 33:00]

### — Phase 4 · 실수 / Sai sót — NARRATOR IM (31:30–33:00) —

### SC_228 · LOC_002_YODONGSEONG (치 đông-nam, khe đục) · lính Goguryeo, 전차장 · VEH_001 · video8s · 31:30–31:38
[ACTION-VI] Loạt nỏ Tùy tập trung: hàng trăm mũi nỏ đập vào mặt 치 và khe đục — tia lửa trên giáp trước K2, đá vụn bắn; một lính Goguryeo đứng cạnh xích xe trúng mũi nỏ vào vai, ngã ngồi; 전차장 rụt xuống, nắp cupola sập. Cận trung.
[SOUND] nỏ đập đá và thép như mưa đá, tiếng ngã.
[COMBAT]

### SC_229 · LOC_002_YODONGSEONG (trong K2) · 전차장, 포수 · VEH_001 · video8s · 31:38–31:46
[ACTION-VI] Trong xe: mũi nỏ gõ lên vỏ như mưa đá, 포수 rụt vai khi một mũi đập ngay trước kính ngắm; màn hình nhiệt rung; 전차장 ấn tai nghe, mắt vào màn hình bên: 16. Không thoại.
[SOUND] gõ thép dồn dập, quạt, thở.
[COMBAT]

### SC_230 · LOC_002_YODONGSEONG (dưới tường nam — hầm Tùy) · lính Tùy đào hầm · WPN_201 · video8s · 31:46–31:54
[ACTION-VI] Trong hầm dưới chân tường: lính Tùy tưới dầu lên cột chống gỗ, châm lửa, chạy ngược ra; cột cháy, kêu răng rắc; đất trên trần hầm bắt đầu đổ. Máy thấp, tracking ra ngoài.
[SOUND] lửa trong hầm, gỗ nứt, đất đổ.
[COMBAT]

### SC_231 · LOC_002_YODONGSEONG (tường nam, 80 m tây 치 đông-nam) · lính Goguryeo · — · video8s · 31:54–32:02
[ACTION-VI] Đoạn tường nam cách 치 đông-nam 80 m về phía tây chùng xuống như thở ra — rồi mặt ngoài đổ sập ra phía hào trong tiếng gầm, đá xếp khan tuôn thành thác, bụi trùm; lính Goguryeo trên đó rơi theo đá. Wide từ 치 nhìn dọc tường.
[SOUND] đá đổ như sấm, bụi, thét.
[COMBAT]

### SC_232 · LOC_002_YODONGSEONG (lỗ hổng, từ ngoài) · bộ binh Tùy · WPN_201, VEH_203 · video8s · 32:02–32:10
[ACTION-VI] Bộ binh Tùy khiên tròn ào qua hào lên đống đá đổ vào lỗ hổng còn mù bụi; thang mây kéo theo; cờ đỏ cắm lên đống đá. Aerial thấp.
[SOUND] hô xung phong, đá lăn dưới chân.
[COMBAT]

### SC_233 · LOC_002_YODONGSEONG (mặt tường nam giữa 치 và lỗ hổng) · K3 사수, phụ xạ thủ · WPN_003 · video8s · 32:10–32:18
[ACTION-VI] Trên mặt tường giữa 치 và lỗ hổng: tổ K3 bắn dài xuống đống đá — tracer quét ngang đám khiên; phụ xạ thủ kéo dây đạn; nòng K3 đỏ rực qua khe tản nhiệt; xạ thủ hét về phía sau. Phía tường tây xa, khẩu K3 kia vẫn bận thang.
[SOUND] K3 quét dài, dây đạn, hét.
[COMBAT]
K3 사수: 총열 교환!

### SC_234 · LOC_002_YODONGSEONG (tường đông trên lỗ hổng) · 2소대 PZF 사수 ×2 · WPN_005, VEH_203 · video8s · 32:18–32:26
[ACTION-VI] Hai lính 2소대 quỳ ở lan can, hai ống PZF phụt gần như cùng lúc xuống xe thang mây đang dựng thang lên mép lỗ hổng — xe thang nổ bung, thang gãy đôi rơi lên đám khiên. Trung cảnh.
[SOUND] hai "쾅", gỗ, thét.
[COMBAT]

### SC_235 · LOC_002_YODONGSEONG (lỗ hổng — ken-burns) · lính Goguryeo, lính Hàn, lính Tùy · PROP_011 · still_kenburns · 32:26–32:36
[ACTION-VI] Ảnh: trong bụi trắng của lỗ hổng, hàng giáo Goguryeo và khiên Tùy chạm nhau trên đống đá; ở tiền cảnh, một vai áo camo có 태극기 sát một vai giáp lamellar, hai người cùng tì vào một tảng đá. Ken-burns đẩy chậm vào hai bờ vai. Không thoại, không narration.
[SOUND] giáo, khiên, thở, bụi.
[COMBAT]

### SC_236 · LOC_002_YODONGSEONG (tường đông trên lỗ hổng) · 2소대 PZF 사수 ×3 · WPN_005, VEH_201 · video8s · 32:36–32:44
[ACTION-VI] Một tháp phủ đất đã lăn tới sát lỗ hổng, cầu bập bênh sắp hạ; ba ống PZF từ lan can phụt liên tiếp vào tầng giữa — tháp bốc lửa từ trong, cầu rơi trước khi chạm tường. Wide.
[SOUND] ba "쾅" nối nhau, lửa, cầu rơi.
[COMBAT]

### SC_237 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001 · EQP_002, VEH_001 · video8s · 32:44–32:52
[ACTION-VI] 한승우 nép sau lan can 치 dưới mưa nỏ, ngẩng nhìn dọc tường về cụm hai tháp và xe thang đang dồn vào lỗ hổng; bấm radio, mặt bụi đá — câu vừa dứt, nòng K2 bên ông xoay về phía tây và hai phát nối nhau (viên 7–8) dội xuống cụm tháp, bụi 치 bay. 
[SOUND] nỏ đập đá, PTT, hai "쾅" cách nhau sáu giây, máy nạp đạn.
[COMBAT]
한승우: 천둥 1, 무너진 벽 앞 탑. 네 발.

### SC_238 · LOC_002_YODONGSEONG (cụm tháp trước lỗ hổng) · lính Tùy · VEH_001, VEH_201 · video8s · 32:52–33:00
[ACTION-VI] 2-BEAT (4 s + 4 s): (a) wide — viên 9 và 10 cách nhau sáu giây: tháp phủ đất thứ hai vỡ, xe thang tan, đống đá trước lỗ hổng bốc thành cột đất, bộ binh Tùy tản ngược xuống hào; (b) insert trong xe — bộ đếm "잔탄 12", 포수 buông tay khỏi cò.
[SOUND] hai "쾅", đất đá, trống Tùy rối, máy nạp đạn im.
[COMBAT]

### — Phase 5 · 고구려가 메우다 / Goguryeo gánh (33:00–34:04) —

### SC_239 · LOC_002_YODONGSEONG (lỗ hổng, trong thành) · CHAR_104, bộ binh giáo Goguryeo · — · video8s · 33:00–33:08
[ACTION-VI] 고정수 nhảy xuống bậc thang tường đông sát lỗ hổng, giáo dài trong tay, áo choàng cháy; ông quát, hàng giáo dài Goguryeo dựng thành tường thứ hai ngay trong lỗ hổng, mũi giáo hạ ngang. Low-angle từ đống đá.
[SOUND] giáo hạ đồng loạt, quát, đá.
[COMBAT]
N: 열 발은 끝났습니다. 구멍은 아직 열려 있었습니다. 구멍을 메우는 것은 이 성의 것이었습니다.
고정수: 창을 세워라! 한 걸음도 안 된다!

### SC_240 · LOC_002_YODONGSEONG (cổng bắc) · CHAR_105, kỵ Goguryeo · VEH_101, PROP_018 · video8s · 33:08–33:16
[ACTION-VI] Cổng bắc mở: 해모루 thổi tù và một hồi, dẫn ba trăm kỵ binh giáp ngựa lao ra, vòng theo chân tường đông — mặt không có địch — xuống góc đông-nam, đánh vào sườn tổ người đẩy tháp bên ngoài lỗ hổng, giáo dài hạ ngang. Aerial thấp theo đầu đoàn.
[SOUND] tù và, vó ngựa như sấm, giáp.
[COMBAT]
N: 해모루의 삼백 기가 북문으로 나갔습니다. 적이 없는 동쪽을 돌아, 탑을 미는 자들의 옆구리로.

### SC_241 · LOC_003_CHEONDUNG_BASE (nóc 천둥 2) · CHAR_002 · VEH_002 · video8s · 33:16–33:24
[ACTION-VI] Thung lũng: 오태민 trên nóc 천둥 2 nghe tù và và tiếng đá đổ dội qua đồi; ông nhìn 천둥 3 (giữ lại), nhìn đường mòn — rồi chui xuống cửa nóc, lệnh nội bộ xe. Xe nổ máy vọt lên đường mòn.
[SOUND] tù và xa, intercom, động cơ gầm.
[COMBAT]
N: 오태민은 골짜기를 맡았습니다. 골짜기는 조용했고, 북문은 아니었습니다. 그는 두 번째로 명령을 어겼습니다.
오태민: 조종수, 북문. 말객 옆에 선다.

### SC_242 · LOC_002_YODONGSEONG (góc đông-nam ngoài tường, bãi tháp) · CHAR_002, kỵ Goguryeo · VEH_002, VEH_101, VEH_201 · video8s · 33:24–33:32
[ACTION-VI] 천둥 2 vọt ra cạnh đoàn kỵ Goguryeo đang đâm vào sườn đám người đẩy tháp; tháp pháo 40mm xoay, bắn loạt dài vào chân hai tháp còn lại phía tây lỗ hổng — người đẩy tản, tháp đứng chết; kỵ Goguryeo phi qua khoảng trống. Tracking ngang.
[SOUND] 40mm loạt dài, vó ngựa, giáo.
[COMBAT]
N: 오 분 뒤, 천둥 2가 동남쪽 모퉁이로 나왔습니다. 예순 발. 어긴 명령이 제때 왔습니다. 그것이 문제였습니다.

### SC_243 · LOC_002_YODONGSEONG (lỗ hổng) · CHAR_104, giáo Goguryeo, lính Tùy · — · video8s · 33:32–33:40
[ACTION-VI] Trong lỗ hổng: hàng giáo Goguryeo tiến từng bước lên đống đá, đẩy hàng khiên Tùy lùi xuống hào; khói PZF còn bay; 고정수 ở hàng đầu, giáo gãy, rút kiếm ngắn. Trung cảnh.
[SOUND] giáo, khiên lùi lạo xạo, thở.
[COMBAT]
N: 구멍은 창으로 막혔습니다. 총으로 막힌 것이 아니었습니다.

### SC_244 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101, CHAR_001 · VEH_001 · video8s · 33:40–33:48
[ACTION-VI] Trên 치, nỏ đã thưa; 을지문덕 đứng thẳng bên xích K2, không nhìn trận — nhìn 한승우; hỏi hai chữ.
[SOUND] trận xa dần, gió.
[COMBAT]
N: 그는 담 아래를 보지 않았습니다. 수를 물었습니다. 늘 그랬습니다.
을지문덕: 얼마나 남았소?

### SC_245 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_001 · VEH_001 · video8s · 33:48–33:56
[ACTION-VI] 한승우 nhìn 전차장 giơ hai bàn tay lên khỏi cupola — mười ngón, rồi hai ngón; ông trả lời.
[SOUND] gió, trận xa.
[COMBAT]
N: 약속한 열이었습니다. 하나도 더 쓰지 않았습니다.
한승우: 열두 발입니다.

### SC_246 · LOC_002_YODONGSEONG (치 đông-nam) · CHAR_101 · VEH_001 · video8s · 33:56–34:04
[ACTION-VI] 을지문덕 đặt bàn tay lên váy xích K2 — lần thứ hai trong đời — rồi chỉ xuống dốc đất; nói với 한승우 trong khi trận vẫn còn ở lỗ hổng.
[SOUND] tay trên thép, giáo xa.
[COMBAT]
N: 그는 이기고 있는 쇠수레를 내렸습니다. 열두 발은 다른 곳의 것이었습니다.
을지문덕: 그럼 이제 내려가시오. 그건 여기 것이 아니오.

### SC_247 · LOC_002_YODONGSEONG (đồng bằng hoàng hôn — ken-burns) · — · VEH_201, WPN_201 · still_kenburns · 34:04–34:14
[ACTION-VI] Ảnh: hoàng hôn hổ phách qua bụi: tháp cháy rải khắp đồng phía nam và đông-nam, một tháp đổ tựa tường nam gần góc, xe húc đen trên đường đắp cổng nam; cột quân Tùy lùi về phía biển lều; kỵ Goguryeo quay về cổng bắc. Ken-burns kéo ra rất chậm.
[SOUND] lửa, trống rút, vó ngựa về.
[COMBAT]
N: 해가 졌습니다. 세 번째 공성이 끝났습니다. 탑 아홉이 벌판에서 탔습니다. 담 하나가 무너졌고, 창으로 막혔습니다. 성은 섰습니다.

### — Phase 6 · 다른 지도 / Kết (34:14–34:30) —

### SC_248 · LOC_004_YUKHAPSEONG (đài quan sát nam thành, hoàng hôn) · CHAR_201, tướng Tùy · PROP_021 · video8s · 34:14–34:22
[ACTION-VI] Đài: 양제 gập quạt, đứng dậy, bước xuống bậc đài giữa hàng tướng quỳ rạp — không một lời; lọng vàng theo sau; ông không nhìn về phía thành. Trung cảnh từ dưới.
[SOUND] lọng, giáp tướng, im.
[COMBAT]
N: 황제는 아무 말도 하지 않았습니다. 그는 오늘 천둥을 귀로 들었습니다. 말은 그날 밤 육합성에서 나올 것이었습니다.

### SC_249 · LOC_002_YODONGSEONG (dốc đất sau 치, hoàng hôn) · CHAR_003, kíp K2 · VEH_001 · video8s · 34:22–34:30
[ACTION-VI] K2 lùi xuống dốc đất từng thước, nòng đen bồ hóng, mũi nỏ gãy cắm trên giá đồ; 박기철 tay băng đi lùi bên xích, tay ra hiệu; từ trên tường dội xuống tiếng reo của lính Goguryeo, kíp xe mặt đen không reo. Low-angle từ chân dốc.
[SOUND] xích trên đất, reo hò trên tường, động cơ.
[COMBAT]
N: 성은 버텼습니다. 황제는 그날 밤 다른 지도를 펼쳤습니다.

[Kết thúc Phần 10]

## [Phần 11] 성은 버티오, 문제는 평양이오 — 「성은 버티오, 문제는 평양이오」 / Chiến thắng có giá  (34:30–37:30)
> Tóm tắt VI: Đêm 6월 11: lỗ hổng vá bằng chính đá của dốc đất — thành "ăn" dốc; xác lính Goguryeo xếp trên tường dưới vải. 을보: "이 돌은 성 돌이야. 제자리로 간다." Tên Tùy từ tối bắn quấy tổ vá — 소년 척후 bắn trả (mini). Lính bỏng nặng sống nhờ thuốc 을보 nhưng ngón tay không nắm được súng. 박기철: "포탄 열두 발. 박격포 예순. PZF 열둘. 40밀리 이백이십." · "전차, 어제 하루 오십 킬로 몫 먹었습니다. 삼백십." 육합성 [史]: 우중문 (hiếu chiến) và 우문술 (thận trọng) lần đầu: "평양이 떨어지면 요동은 저절로 떨어집니다." — "백 일치 군량을 누가 집니까?" — 양제: "아홉 군. 삼십만 오천. 평양으로 가라." + "뇌군도 남쪽으로 갈 것이다. 탁발흠은 따라붙어라." Ở lỗ hổng, 을지문덕 vẽ đường trên đất bằng que: 요동 — 압록 — 평양: "성은 버티오. 문제는 평양이오." — "나와 같이 남쪽으로 가시오." Aerial: 9 quân chảy về đông dưới trăng; 소년 척후 trên tường nhìn dòng đen. "삼십만 오천 명이 동쪽으로 떠났습니다. 그들의 등에는 백 일치 쌀이 있었습니다. — 아직은."
> Chức năng: CONSEQUENCE · Combat mini: SC_252 · Tài nguyên nói thành lời: "포탄 열두 발 · 박격포 예순 · PZF 열둘 · 40밀리 이백이십 · 전차 삼백십" · lính không cầm súng được · Quyết định lịch sử: 양제 chuẩn 9 quân 30만 5천 [史]; 우중문/우문술 tranh luận [史]; 을지문덕 đổi nhiệm vụ giữ → đi · Open loop: "삼십만 오천 명이 동쪽으로 떠났습니다. 그들의 등에는 백 일치 쌀이 있었습니다. — 아직은."

### SC_250 · LOC_002_YODONGSEONG (lỗ hổng tường nam, đêm — ken-burns) · dân, lính Goguryeo · PROP_016 · still_kenburns · 34:30–34:40
[ACTION-VI] Ảnh: đêm, đuốc; lỗ hổng 80 m đang được xếp lại bằng những tảng đá tháo từ tường trong — dân và lính chuyền tay từ dốc đất tới lỗ hổng; dốc đất đã bị đào lở một bên; trên mặt tường phía trên, một hàng xác lính Goguryeo dưới vải gai, giáo dựng đầu mỗi người. Ken-burns từ hàng vải gai xuống dòng người chuyền đá.
[SOUND] đá, đuốc, không tiếng người.
N: 그날 밤 성은 언덕을 먹었습니다. 쇠수레가 오른 흙 언덕의 돌이 구멍으로 갔습니다. 담 위에는 마흔 명이 천 밑에 누웠습니다. 성이 낸 값이었습니다. 총이 낸 값은 따로 있었습니다.

### SC_251 · LOC_002_YODONGSEONG (lỗ hổng) · CHAR_106, CHAR_005, thợ đá · PROP_019 · video8s · 34:40–34:48
[ACTION-VI] 을보 trên đống đá, búa gõ chỉ chỗ; 태오 và một thợ đá Goguryeo khiêng một tảng đá từ dốc tới, đặt vào hàng; 을보 vỗ tảng đá như vỗ ngựa.
[SOUND] búa, đá đặt, thở.
N: 을보는 달포 전에 뺀 돌을 오늘 밤 다시 쌓았습니다. 열 줄이 내려왔고, 열 줄이 올라갔습니다.
을보: 이 돌은 성 돌이야. 제자리로 간다.

### SC_252 · LOC_002_YODONGSEONG (mặt tường trên lỗ hổng, đêm) · 소년 척후, cung thủ Goguryeo · WPN_101 · video8s · 34:48–34:56
[ACTION-VI] Từ bóng tối ngoài hào, tên Tùy bay tới cắm quanh đuốc của tổ vá — một đuốc rơi; trên tường, 소년 척후 (tay còn băng) giương cung bắn trả vào chỗ lóe lửa, cung thủ Goguryeo bắn theo một loạt; tên Tùy im. Low-angle.
[SOUND] tên rít hai chiều, đuốc rơi, dây cung.
[COMBAT]
N: 수나라는 밤에도 화살을 보냈습니다. 담을 고치지 못하게 하려는 것이었습니다. 화살을 나르던 아이가 그날 밤 처음 활을 당겼습니다.

### SC_253 · LOC_003_CHEONDUNG_BASE (lều quân y) · CHAR_004, lính bỏng · WPN_001 · video8s · 34:56–35:04
[ACTION-VI] Lều quân y: lính bỏng nặng ngồi dậy, cánh tay băng kín tới vai, cố nắm báng súng K2C1 dựng bên cáng — ngón tay không khép lại được; 서아 nhẹ nhàng gỡ khẩu súng ra, đặt xuống, giọng 해요.
[SOUND] băng cọ, súng đặt xuống.
N: 을보의 약은 들었습니다. 두 사람은 살았습니다. 손가락은 아직 아니었습니다. 살아 있으나 총을 못 드는 사람이 둘 생겼습니다. 오늘 담에서 넷이 더 다쳤습니다.
윤서아: 살았어요. 총은… 나중에요.

### SC_254 · LOC_003_CHEONDUNG_BASE (hàng xe, đêm) · CHAR_003, CHAR_001 · VEH_001, VEH_002 · video8s · 35:04–35:12
[ACTION-VI] Walk-and-talk dọc hàng xe dưới đèn đỏ: K2 nòng đen, 천둥 2 và 3, xác 천둥 4 phía sau; 박기철 (tay băng) đọc số cho 한승우 không cần sổ — sổ 태오 cầm đi sau.
[SOUND] bước trên tro, đèn đỏ ro ro.
N: 박기철은 오늘도 줄어든 것만 읽었습니다. K3는 천이백 발이 나갔습니다. 늘어난 것은 없었습니다.
박기철: 포탄 열두 발. 박격포 예순. PZF 열둘. 40밀리 이백이십.

### SC_255 · LOC_003_CHEONDUNG_BASE (bên K2) · CHAR_003 · VEH_001 · video8s · 35:12–35:20
[ACTION-VI] 박기철 dừng ở K2, rút que đo dầu bằng hai bàn tay băng vụng về, giơ lên đèn: vệt ướt thấp hơn lần trước rõ rệt; ông nhìn que rồi mới nói.
[SOUND] que kim loại, đèn.
N: 불이 난 뒤로 점검 시동은 끊었습니다. 오늘은 언덕을 오르고, 하루 종일 시동을 켜 두었습니다. 쏘지 않는 시간에도 기름은 갔습니다.
박기철: 전차, 오늘 하루 오십 킬로 몫 먹었습니다. 삼백.

### SC_256 · LOC_004_YUKHAPSEONG (육합성 đêm — ken-burns) · — · PROP_021 · still_kenburns · 35:20–35:30
[ACTION-VI] Ảnh: 육합성 ban đêm từ trên cao — tường vải giả gạch, lầu canh đỏ, điện vàng sáng đèn lồng giữa biển lửa trại; đường từ cổng nam ra bãi tháp cháy còn đỏ. Ken-burns đẩy vào điện vàng.
[SOUND] trống đêm, gió.
N: 그날 밤 육합성에서 회의가 열렸습니다. 요동성에 대한 회의가 아니었습니다. 요동성을 두고 가는 회의였습니다.

### SC_257 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_201, CHAR_202, CHAR_203, CHAR_205 · — · video8s · 35:30–35:38
[ACTION-VI] Trong điện: 양제 trên ngai, áo lụa không giáp; dưới bậc, hai tướng quỳ — 우중문 (giáp 명광개 hai gương ngực, râu trắng dài, áo choàng đỏ) và 우문술 (giáp sẫm không trang trí, râu xám ngắn, thẻ tre trong tay); bản đồ lụa lớn trải giữa: 평양 ở góc xa. 탁발흠 quỳ sát rèm phía sau. Máy trung, low-angle.
[SOUND] lụa, lư hương.
N: 우중문. 우문술. 역사가 이름을 남긴 두 장군이었습니다. 하나는 치자고 했고, 하나는 세자고 했습니다.

### SC_258 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_202 · — · video8s · 35:38–35:46
[ACTION-VI] 우중문 ngẩng đầu, bàn tay đập lên bản đồ lụa ở 평양, giọng gầm trong điện.
[SOUND] tay đập lụa, giọng vang.
N: 우중문의 셈은 성이 아니라 나라였습니다. 머리를 치면 손발은 따라온다는 셈이었습니다.
우중문: 평양이 떨어지면 요동은 저절로 떨어집니다.

### SC_259 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_203 · — · video8s · 35:46–35:54
[ACTION-VI] 우문술 không ngẩng cao, giơ thẻ tre — dòng số lương — hỏi bằng giọng khô, thận trọng.
[SOUND] thẻ tre, im.
N: 우문술은 셈을 하는 사람이었습니다. 이 전쟁에서 셈을 하는 사람은 늘 소수였습니다.
우문술: 백 일치 군량을 누가 집니까?

### SC_260 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_202, CHAR_203 · — · video8s · 35:54–36:02
[ACTION-VI] 우중문 quay đầu nhìn 우문술, mỉa; tay ông vạch một đường ngắn trên lụa từ 압록 tới 평양.
[SOUND] móng tay trên lụa.
N: 사흘. 그 수는 지도 위의 수였습니다. 땅 위의 수는 아니었습니다.
우중문: 평양은 압록에서 사흘 거리요. 사흘이면 끝나오.

### SC_261 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_201 · — · video8s · 36:02–36:10
[ACTION-VI] 양제 nhìn bản đồ, không nhìn hai tướng; quạt gập chỉ xuống 평양 — quyết.
[SOUND] quạt chạm lụa.
N: 황제는 오늘 낮의 천둥을 말하지 않았습니다. 넉 달 동안 못 깬 성도 말하지 않았습니다. 그는 다른 성을 골랐습니다. 역사는 이 결정을 기록했습니다. 아홉 군, 삼십만 오천.
수 양제: 아홉 군. 삼십만 오천. 평양으로 가라.

### SC_262 · LOC_004_YUKHAPSEONG (điện vàng) · CHAR_201, CHAR_205 · — · video8s · 36:10–36:18
[ACTION-VI] 양제 quay quạt về phía rèm sau — nơi 탁발흠 quỳ; nói không cao giọng; 탁발흠 chạm trán xuống sàn.
[SOUND] lụa, trán chạm sàn.
N: 황제는 뇌군을 잊지 않았습니다. 성을 두고 가면서도 그것은 두고 가지 않았습니다.
수 양제: 뇌군도 남쪽으로 갈 것이다. 탁발흠은 따라붙어라.

### SC_263 · LOC_001_YOHA (bãi tập kết 9 quân, đêm — ken-burns) · lính Tùy · WPN_201, PROP_022 · still_kenburns · 36:18–36:28
[ACTION-VI] Ảnh: đêm, đuốc hàng dặm: lính Tùy xếp hàng nhận bao gạo lớn, mỗi người cõng bao lên lưng đã có giáp, giáo, lều cuộn — lưng còng xuống; sĩ quan đếm bằng thẻ. Ken-burns trượt theo hàng người.
[SOUND] bao gạo lên lưng, thẻ tre, hô số.
N: 역사는 그 무게를 적었습니다. 한 사람에 백 일치 양식. 세 섬이 넘었습니다. 아홉 군이 압록수 서쪽에 모였습니다. 그들은 요동성을 등 뒤에 두고 갈 것이었습니다.

### SC_264 · LOC_002_YODONGSEONG (lỗ hổng, trong thành, đêm) · CHAR_101, CHAR_001 · — · video8s · 36:28–36:36
[ACTION-VI] 을지문덕 ngồi trên một tảng đá của dốc đất chưa kịp chuyển, que trong tay vạch trên đất nện ba chấm và một đường: 요동 — 압록 — 평양; 한승우 ngồi xổm đối diện, mũi tên trong túi ngực; sau lưng họ, dòng người chuyền đá vẫn đi.
[SOUND] que trên đất, đá xa.
N: 그는 담 위에서 말하지 않았습니다. 구멍 앞에서, 땅에 선을 그으며 말했습니다.
을지문덕: 성은 버티오. 문제는 평양이오.

### SC_265 · LOC_002_YODONGSEONG (lỗ hổng, trong thành) · CHAR_101 · — · video8s · 36:36–36:44
[ACTION-VI] Que dừng ở chấm cuối; 을지문덕 ngẩng lên nhìn 한승우, nói câu thứ hai — không phải lệnh, không phải xin.
[SOUND] que, gió.
N: 임무는 바뀌었습니다. 지키는 것에서 가는 것으로.
을지문덕: 나와 같이 남쪽으로 가시오.

### SC_266 · LOC_002_YODONGSEONG (lỗ hổng, trong thành) · CHAR_001 · PROP_015 · video8s · 36:44–36:52
[ACTION-VI] 한승우 nhìn đường vạch trên đất — ba chấm, đường dài; tay phải chạm vào mũi tên trong túi ngực; không trả lời — nhìn về phía thung lũng tối sau tường. Máy đẩy chậm vào mặt.
[SOUND] gió, đá xa.
N: 한승우는 대답하지 않았습니다. 그의 머릿속에는 숫자 하나가 있었습니다. 박기철의 숫자였습니다. 삼백.

### SC_267 · LOC_002_YODONGSEONG (aerial đêm trăng — ken-burns) · — · WPN_201 · still_kenburns · 36:52–37:02
[ACTION-VI] Ảnh aerial đêm trăng: từ biển lều phía tây, chín cột quân đen kịt chảy về phía đông vòng qua phía nam thành như một dòng sông tối dưới trăng, đuốc thưa; thành là một hòn đảo im. Ken-burns kéo ra rất chậm.
[SOUND] bước chân vạn người rất xa, gió trên cao.
N: 며칠 뒤 밤, 아홉 군이 움직였습니다. 요동성을 돌아 동쪽으로였습니다. 성은 처음으로 지나가는 군대를 보았습니다.

### SC_268 · LOC_002_YODONGSEONG (tường đông, đêm) · 소년 척후, CHAR_105 · — · video8s · 37:02–37:10
[ACTION-VI] Trên tường đông: 소년 척후 một mình ở lan can, cung trên lưng, nhìn dòng đen chảy qua phía nam thành dưới trăng; 해모루 lên bậc, đặt tay lên vai cậu, đứng cùng một nhịp rồi kéo cậu xuống. Không thoại.
[SOUND] gió, bước chân xa của đại quân.
N: 아이는 석 달 전 백만이라 했습니다. 오늘 밤 그 백만의 삼십만이 성을 지나갔습니다. 어디로 가는지 아이는 몰랐습니다. 대장군은 알았습니다.

### SC_269 · LOC_001_YOHA (đường về đông, đêm — ken-burns) · lính Tùy · PROP_022 · still_kenburns · 37:10–37:20
[ACTION-VI] Ảnh: đêm trên đường hành quân, một lính Tùy tụt lại, lén tháo dây bao gạo, trút một phần vào rãnh bên đường, lấp lá; hàng người phía trước còng lưng đi tiếp. Ken-burns đẩy vào bàn tay trút gạo.
[SOUND] gạo đổ khẽ, bước chân.
N: 무게는 첫날 밤부터 등을 눌렀습니다. 버리면 목이 달아났습니다. 그래도 몇 줌이 길가에 떨어졌습니다. 아무도 보지 않는 곳에서였습니다.

### SC_270 · LOC_004_YUKHAPSEONG (cổng 육합성, đêm — ken-burns) · CHAR_205, kỵ Tiên Ti · VEH_206 · still_kenburns · 37:20–37:30
[ACTION-VI] Ảnh: cổng đỏ 육합성 ban đêm, 탁발흠 dẫn một toán kỵ Tiên Ti nhỏ ra cổng, không theo cột quân — rẽ về phía đông-nam nơi dải đồi tối sau thành; ở thắt lưng ông, một băng đạn rỗng lạ mắt nhặt dưới chân tường hôm trước. Ken-burns theo toán kỵ ra khỏi cổng.
[SOUND] vó ngựa ít, gió.
N: 탁발흠은 아홉 군을 따라가지 않았습니다. 그는 다른 것을 따라갈 것이었습니다. 삼십만 오천 명이 동쪽으로 떠났습니다. 그들의 등에는 백 일치 쌀이 있었습니다. — 아직은.

[Kết thúc Phần 11]

## [Phần 12] 400km — 「400km」 / Lịch sử rẽ hướng  (37:30–40:00)
> Tóm tắt VI: Thung lũng đêm D75. 박기철 xếp que đo dầu từng xe lên nắp động cơ K2; vạch đường trên đất bằng cán búa: 요동성 — 압록수 — 청천강; bước đo. "전차에 삼백. 나머지 다 짜면 사백." — "여기서 청천강까지 400km. 연료는 전차 한 대 몫뿐입니다." 한승우 nhìn bốn xe còn lại. 오태민: "그럼 나머지는요?" Không ai trả lời. 을보 đặt tay lên chốt sắt bánh 천둥 3. 서아 xếp thuốc 을보 vào ba lô quân y rỗng, 아리 khăn olive. 한승우 với mũi tên: "…전차 한 대 몫." Aerial: chín cột đen về đông; xa nhất, một toán kỵ Tiên Ti rẽ về núi — 탁발흠: "막지 않는다. 뒤를 밟는다." K2 dưới lưới, nòng đen. End card 「살수 612 · 3화 남하」.
> Chức năng: DECISION-OPEN · Tài nguyên nói thành lời: "전차에 삼백 · 사백 · 전차 한 대 몫" · Enemy adaptation: 탁발흠 không chặn — theo đuôi · Open loop tập: "여기서 청천강까지 400km. 연료는 전차 한 대 몫뿐입니다."

### SC_271 · LOC_003_CHEONDUNG_BASE (đêm — ken-burns) · — · VEH_001, VEH_002, VEH_003, VEH_004, PROP_007 · still_kenburns · 37:30–37:40
[ACTION-VI] Ảnh: thung lũng đêm trăng: K2 nòng đen dưới lưới kéo hé, 천둥 2 và 천둥 3 (chốt sắt bánh), hai K511, K151 — và xác 천둥 4 đen ở rìa; sau bao cát mới, MỘT phuy đứng lẻ. Ken-burns từ phuy lẻ ra hàng xe.
[SOUND] gió khe, dế, không máy phát.
N: 골짜기에는 아직 쇠가 많았습니다. 전차 하나, 장갑차 둘, 트럭 둘, 지휘차 하나. 그리고 드럼 하나. 문제는 쇠가 아니었습니다. 쇠를 먹일 것이었습니다.

### SC_272 · LOC_003_CHEONDUNG_BASE (nắp động cơ K2) · CHAR_003 · VEH_001 · video8s · 37:40–37:48
[ACTION-VI] 박기철 (tay băng) đặt lên nắp động cơ K2 một hàng que đo dầu — sáu que, mỗi que buộc mẩu giẻ đánh dấu, vệt ướt cao thấp khác nhau; ông xếp chúng thẳng hàng như xếp đũa. Cận tay và que.
[SOUND] que kim loại trên thép, gió.
N: 여섯 개의 막대였습니다. 여섯 대의 기름이었습니다. 박기철은 그것을 한 줄로 놓았습니다. 한 줄로 놓으면 답이 보였습니다.

### SC_273 · LOC_003_CHEONDUNG_BASE (đất trần trước K2) · CHAR_003, CHAR_001, CHAR_002 · VEH_001 · video8s · 37:48–37:56
[ACTION-VI] 박기철 quỳ, cán búa vạch lên đất một đường dài với ba chấm — chấm đầu, chấm giữa, chấm cuối — rồi cầm từng que đo trên nắp K2 giơ lên: que K21 khô gần hết, que xe tải ướt nửa, que phuy; đặt xuống theo hàng; 한승우 và 오태민 đứng nhìn; đèn pin che tay chiếu xuống que.
[SOUND] cán búa trên đất, bước chân, gió.
N: 요동성. 압록수. 청천강. 을지문덕이 물은 강이었습니다. 박기철은 이제 왜 물었는지 알았습니다. 두 달 동안 장갑차는 밤마다 시동으로 기름을 태웠습니다.
박기철: 장갑차는 바닥, 트럭은 반, 드럼 하나. 다 짜면 사백.

### SC_274 · LOC_003_CHEONDUNG_BASE (đất trần trước K2) · CHAR_003 · VEH_001 · video8s · 37:56–38:04
[ACTION-VI] 박기철 đứng ở chấm cuối đường vạch, quay lại nhìn 한승우 qua khoảng đất, nói con số như đã nói mọi con số — không cao, không thấp.
[SOUND] gió, im.
N: 그 문장은 두 달 동안 준비된 것이었습니다. 막대 여섯 개와 땅 위의 선 하나로.
박기철: 여기서 청천강까지 400km. 연료는 전차 한 대 몫뿐입니다.

### SC_275 · LOC_003_CHEONDUNG_BASE (hàng xe) · CHAR_001 · VEH_002, VEH_003, VEH_004 · video8s · 38:04–38:12
[ACTION-VI] 한승우 quay đầu chậm nhìn từng xe dưới lưới — 천둥 2, 천둥 3, hai xe tải, xe chỉ huy — rồi nhìn K2. Máy theo ánh mắt ông từ xe này sang xe kia.
[SOUND] gió, lưới sột soạt.
N: 나머지 다섯 대는 그 셈에 없었습니다. 한승우는 다섯 대를 하나씩 보았습니다. 지난 두 달의 집이었습니다.

### SC_276 · LOC_003_CHEONDUNG_BASE (hàng xe) · CHAR_002 · VEH_002 · video8s · 38:12–38:20
[ACTION-VI] 오태민 (tay áo cháy) bước tới đặt bàn tay lên hông 천둥 2 — xe anh đã đưa ra cổng bắc — hỏi, không to.
[SOUND] tay trên thép.
N: 오태민이 물었습니다. 화를 내지 않고 물은 것은 처음이었습니다.
오태민: 그럼 나머지는요?

### SC_277 · LOC_003_CHEONDUNG_BASE (hàng xe) · CHAR_003, CHAR_001, CHAR_106 · VEH_002, PROP_007 · video8s · 38:20–38:28
[ACTION-VI] Không ai trả lời. 박기철 nhìn phuy lẻ sau bao cát; 한승우 nhìn xuống đường vạch trên đất; xa hơn, 을보 đứng bên 천둥 3, bàn tay già đặt lên chốt sắt bánh xe do chính ông rèn — ông nghe câu hỏi, mắt trái nheo. Wide.
[SOUND] gió, dế, im.
N: 아무도 대답하지 않았습니다. 대답은 이미 땅 위에 그어져 있었습니다.

### SC_278 · LOC_003_CHEONDUNG_BASE (bánh 천둥 3 — ken-burns) · CHAR_106 (tay) · VEH_002, PROP_019 · still_kenburns · 38:28–38:38
[ACTION-VI] Ảnh cận: bàn tay chai sần của 을보 trên chốt sắt rèn tay chốt vào bánh chịu nặng thép công nghiệp; vết búa thô, dầu, bụi. Ken-burns đẩy vào chỗ sắt cổ gặp thép.
[SOUND] gió, im.
N: 을보는 그 바퀴를 두 달 동안 매일 만졌습니다. 고구려 쇠로 굴러온 바퀴였습니다. 그 바퀴가 사백 킬로를 못 간다는 것을 그는 방금 들었습니다. 쇠는 쇠였습니다. 기름은 아니었습니다.

### SC_279 · LOC_003_CHEONDUNG_BASE (lều quân y) · CHAR_004, CHAR_107 · PROP_009 · video8s · 38:38–38:46
[ACTION-VI] Lều quân y: 서아 xếp rễ khô và lá thuốc của 을보 bọc vải vào ngăn ba lô quân y rỗng — nơi từng có mười ba lọ; 아리 (khăn olive) đưa từng gói; hai người không nói. Cận tay.
[SOUND] vải gói, lá khô.
N: 항생제 자리에 약초가 들어갔습니다. 서아의 가방은 이제 이 땅의 가방이었습니다. 이름을 외운 풀이 스물이었습니다.

### SC_280 · LOC_003_CHEONDUNG_BASE (bên K2, đêm) · CHAR_001 · VEH_001, PROP_015 · video8s · 38:46–38:54
[ACTION-VI] 한승우 một mình bên xích K2, rút mũi tên Goguryeo từ túi ngực, xoay trong tay, nhìn về phía nam nơi đường vạch trên đất trỏ tới; nói khẽ với chính mình.
[SOUND] gió, cán tên trong tay.
N: 두 달 전 그는 아흔네 명을 데리고 돌아가겠다고 했습니다. 오늘 밤 그 아흔네 명은 사백 킬로 남쪽을 보고 있었습니다. 돌아가는 길이 아니었습니다.
한승우: …전차 한 대 몫.

### SC_281 · LOC_002_YODONGSEONG (aerial đêm trăng — ken-burns) · — · WPN_201 · still_kenburns · 38:54–39:04
[ACTION-VI] Ảnh aerial rất cao: chín cột quân đen kịt bò về đông dưới trăng, đuốc thưa như hạt; thành nhỏ phía sau; phía trước xa là sông Áp Lục ánh bạc. Ken-burns kéo theo hướng đông.
[SOUND] gió trên cao, bước chân vạn người rất mơ hồ.
N: 삼십만 오천 명이 압록수로 갔습니다. 역사는 그 뒤를 알고 있었습니다. 숫자 하나로. 그 숫자는 아직 오지 않은 일이었습니다. 한 달 하고도 보름 뒤였습니다.

### SC_282 · LOC_002_YODONGSEONG (aerial đêm, rìa cột quân — ken-burns) · CHAR_205, kỵ Tiên Ti · VEH_206 · still_kenburns · 39:04–39:14
[ACTION-VI] Ảnh aerial: ở rìa xa nhất của cột quân, một toán kỵ nhỏ — chấm đen vài chục — tách khỏi dòng, rẽ ngang về phía dải đồi tối sau thành thay vì đi đông. Ken-burns đẩy vào toán kỵ.
[SOUND] vó ngựa ít, gió.
N: 가장 끝에서 기병 한 무리가 길을 벗어났습니다. 동쪽이 아니었습니다. 산이었습니다.

### SC_283 · LOC_003_CHEONDUNG_BASE (ngã ba chân đồi, đêm) · CHAR_205, 선비 부장 · VEH_206 · video8s · 39:14–39:22
[ACTION-VI] Chân đồi, ngã ba: phó tướng chỉ về miệng đường mòn vào thung lũng — nơi có thể chặn; 탁발흠 xoay băng đạn rỗng lạ ở thắt lưng, nhìn đường mòn, rồi nhìn về phía nam — quyết định.
[SOUND] ngựa thở, dây da, gió.
N: 길목은 하나였습니다. 막을 수 있었습니다. 그는 막지 않기로 했습니다. 막는 자는 쇠수레의 앞에 섭니다. 그는 한 번도 앞에 선 적이 없었습니다.
탁발흠: 막지 않는다. 뒤를 밟는다.

### SC_284 · LOC_003_CHEONDUNG_BASE (sườn đồi nam, rìa, đêm — ken-burns) · CHAR_205, kỵ Tiên Ti · VEH_206 · still_kenburns · 39:22–39:32
[ACTION-VI] Ảnh: toán kỵ Tiên Ti đi hàng một dọc sườn đồi tối về phía nam, không đuốc; 탁발흠 dẫn đầu, mũ lông cáo, bím tóc, mũi tên trên dây cổ; xa dưới, thung lũng có một chấm đỏ lều chỉ huy. Ken-burns theo hàng kỵ về phía nam.
[SOUND] vó ngựa nhẹ, gió.
N: 탁발흠은 명령을 받았습니다. 따라붙어라. 그는 명령을 제 방식으로 읽었습니다. 앞을 막는 자는 한 번 싸웁니다. 뒤를 밟는 자는 골라서 싸웁니다. 그는 고르기로 했습니다.

### SC_285 · LOC_003_CHEONDUNG_BASE (K2 đêm — ken-burns) · — · VEH_001 · still_kenburns · 39:32–39:42
[ACTION-VI] Ảnh: K2 dưới lưới ngụy trang trong thung lũng đêm, trăng mỏng trên nòng pháo đen bồ hóng — không còn sạch như hai tháng trước; mũi nỏ gãy cắm trên giá đồ; lính gác nhỏ bên xích. Ken-burns đẩy chậm vào nòng đen.
[SOUND] gió, im.
N: 두 달 전 전차는 한 번도 울지 않았습니다. 이제 열 번 울었습니다. 열두 발. 삼백 킬로. 아흔네 명. 그리고 사백 킬로의 남쪽. 이 숫자들이 다음 길이었습니다.

### SC_286 · LOC_002_YODONGSEONG (tường nam gần góc đông-nam, đêm — ken-burns) · — · PROP_012 · still_kenburns · 39:42–39:51
[ACTION-VI] Ảnh: tường nam đêm, gần góc đông-nam: lỗ hổng đã xếp kín bằng đá sáng màu của dốc đất, cờ 삼족오 cắm trên đó; 치 đông-nam trống, khe đục rộng còn đen bồ hóng; thành im. Ken-burns kéo ra từ khe đục tới lá cờ.
[SOUND] cờ đập gió, im.
N: 요동성은 그해 여름 끝까지 섰습니다. 성은 버텼습니다. 문제는 남쪽이었습니다.

### SC_287 · [END CARD] · — · — · still_kenburns · 39:51–40:00
[ACTION-VI] Đen. Chữ trắng giữa khung: 「살수 612 · 3화 남하」. Không hình khác.
[SOUND] tiếng xích K2 lăn trên đất vọng 3 s trong đen, rồi im tuyệt đối.

[END CARD]

[Kết thúc Phần 12]


---

## 부록 — THỐNG KÊ & TỰ KIỂM (ngoài phần kịch bản · script-writer · 2026-09-16 · 2화 v1)

### A. Thống kê (script đếm tự động `logs/scratch/script-writer-ep2/count.py`: SC theo header `### SC_`, narration = dòng `N:`, thoại = dòng `TÊN:`; 어절 tách theo khoảng trắng; combat = SC có tag `[COMBAT]`)
| Phần | Phút (outline) | SC | video8s | still_kenburns | Giây | Dòng N | 어절 N | Câu thoại | 어절 thoại | Combat (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–1:30 | 12 | 9 | 3 | 90 | 6 | 83 | 5 | 15 | 8 |
| 2 | 1:30–4:30 | 22 | 16 | 6 | 180 | 22 | 371 | 8 | 45 | 40 |
| 3 | 4:30–7:00 | 18 | 15 | 3 | 150 | 18 | 281 | 12 | 65 | 8 |
| 4 | 7:00–10:30 | 25 | 22 | 3 | 210 | 25 | 343 | 9 | 57 | 136 |
| 5 | 10:30–14:00 | 25 | 22 | 3 | 210 | 25 | 315 | 19 | 110 | 64 |
| 6 | 14:00–17:30 | 25 | 21 | 4 | 210 | 25 | 369 | 15 | 94 | 24 |
| 7 | 17:30–21:00 | 25 | 22 | 3 | 210 | 21 | 329 | 10 | 59 | 96 |
| 8 | 21:00–24:00 | 21 | 17 | 4 | 180 | 21 | 306 | 15 | 100 | 32 |
| 9 | 24:00–27:30 | 24 | 19 | 5 | 210 | 24 | 356 | 15 | 99 | 16 |
| 10 | 27:30–34:30 | 52 | 50 | 2 | 420 | 40 | 390 | 21 | 98 | 412 |
| 11 | 34:30–37:30 | 21 | 15 | 6 | 180 | 21 | 322 | 11 | 62 | 8 |
| 12 | 37:30–40:00 | 17 | 9 | 8 | 150 | 16 | 270 | 5 | 24 | 0 |
| **Tổng** | 0:00–40:00 | **287** | **237** | **50** | **2400** (= 40:00) | **264** | **3735** | **145** | **828** | **844 s = 35,2 %** |

- Narration **3.735 어절** / 264 dòng N / 862 câu — **0 câu >15 어절**; SC có N: 264/287 (phủ 2.213 s ≈ 92 % runtime theo SC — mỗi dòng N ngắn 1–4 câu, thời lượng đọc ước ~25 phút ≈ 62 % runtime; tương đương 1화 v3 3.828 어절).
- Thoại **145 câu / 828 어절**, dài nhất 12 어절 (SC_182), **0 câu >12**, **0 SC có >1 câu thoại**. Phân bổ: 을지문덕 27 · 박기철 22 · 한승우 20 · 오태민 11 · 고정수 10 · 을보 8 · 백성민 6 · 수 공성총관 6 · 해모루 5 · 탁발흠 5 · 수 양제 5 · 아리 3 · 윤서아 3 · 장태오 2 · 사수 2 · 우중문 2 · phụ 8 → hiện đại 45 % / Goguryeo 40 % / Tùy 15 %.
- **Combat 844 s = 35,2 %** (brief ≥30 %). 11 cụm `[COMBAT]` / ≥5 khối thật: P2 xung phong + cờ (SC_015–019, 40 s) · P4 1차 공성 + PZF (SC_055–070, 072; 136 s) · P5 cối 10 viên (SC_086–093, 64 s) · P7 hỏa công (SC_139–150, 96 s) · P10 3차 공성 (SC_199–249, 412 s) + mini: P1 mũi nỏ (SC_004) · P3 nỏ vào bệnh xá (SC_043) · P6 tên lửa đêm vào thành (SC_113–115, 24 s) · P8 2차 공성 Goguryeo tự giữ (SC_157–159, 165; 32 s) · P9 Tiên Ti dò lửa lần 2 (SC_187–188, 16 s) · P11 tên quấy tổ vá (SC_252). Khoảng không action dài nhất trong thân tập: 15:46→19:02 (3:16); sau P10: 34:56→40:00 là aftermath (5:04, chấp nhận theo cấu trúc P11–P12).
- Vùng im narrator: 0:00–0:48 (narrator vào 0:48 "612년 4월. 요동성.") · **19:34–20:06** (P7 phuy nổ, SC_143–146, 32 s — theo outline "30 s") · **31:30–33:00** (P10 Phase 4, SC_228–238, 90 s). Sau mỗi mid-roll: 1 SC không thoại (SC_053 tay chạm đá · SC_103 aerial 40 tháp phủ đất · SC_153 xác 천둥 4 · SC_198 K2 leo dốc). 30 s đầu: **6 shot** (SC_001 2-BEAT · SC_002 · SC_003 2-BEAT · SC_004), 0 narrator.
- Mid-roll: 7:00 · 14:00 · 21:00 · 27:30 (đúng outline; không chen climax). Shot trung bình 8,36 s (2.400/287); trong P10 8,08 s (52 SC/420 s) → veo-stage cắt 2-beat ~15 clip như 1화.

### B. Tự kiểm (7 mục)
1. **ID trong bible:** CHAR_001–006, 101, 104, 105, 106, 107, 201, 202, 203, 205 ✓ (CHAR_102 chỉ qua chiếu 1화 PROP_013 — không xuất hiện, đúng bible 2화; CHAR_103/204 chưa dùng) · LOC_001/002/003/004/008 ✓ · VEH_001–004, 101, 201, 202, 203, 206 ✓ · UAV_001, EQP_001/002 ✓ · WPN_001/002/003/005/101/201 ✓ (WPN_004 K6, WPN_006 K4 không dùng — ghi proposals) · PROP_006/007/009/011/012/013/015/016/017/018/019/021/022 ✓. Nhân vật phụ không ID: 소년 척후, 고구려 초병, 수 공성총관, 수 전령, 통역, 고구려 농부, 선비 부장, 전차장/포수/조종수, 사수, K3 사수, 2소대 PZF 사수, 초병.
2. **Thời gian khớp outline:** 12/12 phần đúng mốc phút (0 s lệch); tổng 40:00; không đứt quãng; mọi video8s = 8 s, still 6–12 s (50 still: 6 s ×3, 8 s ×1, 9 s ×2, 10 s ×32, 12 s ×12). Bảng ngày/đêm ở header (D25→D75, 4월 중순→6월 중순; [史] 5월 육합성, 6월 11 양제 nam thành, 6월 9군 30만 5천). Mọi "지난달/두 달 전/석 달 전/보름/열이틀/사흘/하룻밤" rà theo bảng.
3. **Direct quotes nguyên văn (outline):** (1) SC_078 "쇠수레는 며칠이나 달릴 수 있소?" · (2) SC_093 "열 발에 둘. 그럼 스무 개엔 백 발이오." · (3) SC_118 "황제를 죽이면 백만이 돌아가겠소, 아니면 백만이 미치겠소?" · (4) SC_129 "말은 풀을 먹고, 쇠수레는 검은 물을 마신다." · (5) SC_274 "여기서 청천강까지 400km. 연료는 전차 한 대 몫뿐입니다." · (+) SC_155 "항생제, 없습니다. 이제부턴 이 사람들 약초입니다." · SC_264 "성은 버티오. 문제는 평양이오." ✓. **12/12 open loop cuối phần đúng câu outline** (SC_012 · 034 · 052 · 077 · 102 · 126 · 150 · 173 · 197 · 249 · 270 · 274). Câu outline khác giữ nguyên văn: "달리면 닷새. 안 움직이면 한 달." SC_079 · "저 탑들을 가장 적은 화살로 부수시오." SC_083 · "탑이 다시 마흔입니다." SC_101 · "혼자 움직이는 말은 판을 망치오." SC_106 · "명령은 못 받습니다. 임무는 받겠습니다." SC_107 · "그대들, 오늘 저녁은 무엇을 먹었소?" SC_109 · "우리 것이 아닙니다. 그렇다고 왕의 것도 아닙니다." SC_112 · "K21 두 대. 드럼 하나. 드론 둘. 40mm 이백 발 날아갔습니다." SC_154 · "전차 시동 한 번이 드론 열 번입니다." SC_167 · "쇠수레를 쓰시오. 열 발만." SC_169 · "청천강까지 며칠이오?" SC_192 · "폐하께서 항복을 받지 말라 하셨다!" SC_204 · "황제가 눈치챘소." SC_205 · "얼마나 남았소?/열두 발입니다./그럼 이제 내려가시오. 그건 여기 것이 아니오." SC_244–246 · "백 일치 군량을 누가 집니까?" SC_259 · "평양이 떨어지면 요동은 저절로 떨어집니다." SC_258 · "뇌군도 남쪽으로 갈 것이다. 탁발흠은 따라붙어라." SC_262 · "나와 같이 남쪽으로 가시오." SC_265 · "그럼 나머지는요?" SC_276 · "세 번째요. 황제가 대답할 때까지 저들은 못 움직이오." SC_021 · "황제가 눈치채면 끝이오." SC_031. **Câu outline đã điều chỉnh** (xem C): "그대들은 백이십 발이라 했소" → "백십 발이라 했소" · "이게… 몇 번째요?" → "말객님, 이게… 몇 번째입니까?" · 을보 "탑은 속에서 타오 — 꼭대기를 치시오" → 반말.
4. **0–30 s không narration:** ✓ (SC_001–004 chỉ SFX + 2 câu thoại; 0:32–0:48 thêm 2 câu thoại; narrator 0:48).
5. **≤12 어절/câu thoại:** 0 vi phạm (145 câu). Narration ≤15 어절/câu: 0 vi phạm (862 câu). Không dùng "그러나 그들은 몰랐습니다". Radio protocol: mọi câu gọi có "[người nghe], 여기는 [người gọi]" (SC_024, 025, 060, 061, 087, 089, 216, 217); lệnh nội bộ xe dùng "포수/조종수" (SC_187, 241); không tự gọi callsign xe mình.
6. **Ràng buộc nội dung:** 을지문덕 xuất hiện lần đầu, đến bằng đường bí mật (SC_049–052), **không kinh ngạc**, câu đầu là số (SC_078) · thử "ít đạn nhất" (SC_083) · K2 22→12 (10 viên: SC_218, 223 ×2, 224, 225 ×2, 238 ×4; bộ đếm 22→21→…→12) · cối 110→100 (SC_086–090) →60 (SC_207) · PZF 18→17 (SC_068) →12 (SC_234 ×2, 236 ×3) · 40mm 480→280 (cháy 200, SC_146/151) →220 (SC_242 −60) · drone 3→2 (SC_149) · K21 3→2 (천둥 4, SC_145–146) · phuy 2→1 (SC_143–144) · kháng sinh 90 %→60 %→0 (SC_045–046, 155) · 아리 nhận khăn olive (SC_104) · 을보 chốt sắt bánh 천둥 3 (SC_041, 278) · 탁발흠 "검은 물" → hỏa công → "검은 물이 탄다" (SC_129, 150) · 양제 9군 30만 5천 [史] (SC_261) · "성은 버티오. 문제는 평양이오." (SC_264) · 400 km (SC_274) · nối 1화: "뇌군" do 양제 gọi (SC_135, 262), mũi tên trong túi ngực 한승우 (SC_266, 280), 고정수 mở cổng → nay dựng cờ hàng (SC_018), chiếu "성과 함께 죽으라" (SC_111), 을보 "쇠는 쇠요/쇠쟁이" (SC_048), K2 chưa bắn ở 1화 (SC_036, 285), "검은 통" 탁발흠 thấy ở cổng 1화 (SC_129) · 0 KIA đại đội (2 bỏng nặng + 4 thương P10 + 박기철 bỏng tay; SC_253) · không nhắc Bắc Triều Tiên, chỉ "이 땅" (SC_013, 042, 105, 156, 279) · P-11: Tùy ↔ đại đội không nói trực tiếp (탁발흠 hỏi nông dân qua 통역, SC_128) · 시호: người đương thời chỉ "황제/폐하/대왕" (SC_082, 111 "대왕"; SC_205 "황제"); narrator dùng "수 양제" (SC_007).
7. **Anti-copy:** không tên/thoại/trình tự kênh tham chiếu; trình tự tập = tháp trong sương → kế hàng giả [史] → kiểm kê + người áo choàng → PZF xe húc → tướng thử "ít đạn nhất", làm tính → "황제를 죽이면" → hỏa công đốt K21 → 항생제 0, tướng rời tường xem xe → tháo tường đặt xe → 양제 bỏ lệnh, hầm, K2 10 viên, rút xe khi đang thắng → 9 quân → 400 km. Kết: 탁발흠 rẽ núi (SC_283–284) → K2 nòng đen (SC_285) → tường vá (SC_286) → card — KHÔNG "2 chỉ huy trên tường → lều địch → card"; câu "성은 버티오" nói khi ngồi trên đá dốc ở lỗ hổng, vẽ đường trên đất (SC_264), không phải tableau trên tường.

### C. Nhật ký diễn giải ngoài outline (để coordinator/QC rà)
1. **"백이십 발이라 했소" → "백십 발이라 했소"** (SC_094): sau 1화 cối còn 110; 박기철 nói "백십 발입니다. 백이십 발로 왔습니다." (SC_081) rồi đáp lại "이제 백 발입니다." (SC_095) — hai người đếm đối đáp. Quote bắt buộc #2 giữ nguyên văn.
2. Register theo bible: 한승우 với 해모루 하십시오체 → "말객님, 이게… 몇 번째입니까?" (SC_020); 을보 반말 → "탑은 속에서 타. 꼭대기를 쳐, 대장 양반." (SC_088); 고정수 "황제가 눈치챘소" nói với 한승우 (을지문덕 ở sau nghe) vì bible cho 고정수 dùng 합쇼 với 을지문덕 (SC_205).
3. **P2 "đợt tấn công đầu"** = bộ binh + 운제 khi tháp chưa vào vị trí (SC_015–019) — để P1 (tháp vừa tới trong sương) và P4 (1차 공성 với tháp + 충차) không trùng; cờ hàng #3 vẫn đúng chỗ.
4. **Thêm "2차 공성" ở P8** (SC_157–159, 165): Goguryeo tự giữ, đại đội không bắn; 을지문덕 rời tường xuống thung lũng giữa trận ("성은 성이 막소") — để đủ "3 đợt" (foundation §7) và cho quyết định lịch sử nhìn thấy được. Bỏ được bằng cách đổi 4 SC thành cảnh tĩnh nếu user muốn bám outline.
5. **탁발흠 tìm đường mòn D33 rồi đợi 12 ngày** đến khi 양제 tới cho phép (SC_133): echo lệnh "mọi việc phải tấu" của P2 — Tùy chậm vì hệ thống; outline chỉ ghi (a)(b)(c) không nêu khoảng chờ.
6. **Mốc đá trắng 100/200/300 bước** thay đạn đăng ký (SC_184, 202) — giữ cối đúng 100→60 mà vẫn có "đăng ký".
7. **Băng đạn K2C1 rỗng của 탁발흠** (bible "2화+"): nhặt dưới chân tường sau 3차 공성 (SC_270, 283), không phải đêm hỏa công (hắn không xuống thung lũng).
8. **Mini-combat thêm** (không có trong outline, theo brief ≥5 khối/không >4 phút): SC_004 mũi nỏ vào giá trống (hook), SC_043 nỏ vào chớp cửa bệnh xá, SC_113–115 tên lửa đêm vào thành (lý do 서아 hết thuốc dần), SC_187–188 Tiên Ti dò lửa lần 2 bị 40mm đuổi (lý do 오태민 phải giữ thung lũng), SC_252 tên quấy tổ vá — 소년 척후 bắn mũi đầu.
9. **소년 척후 sống** (SC_165, 252, 268) — payoff lọ kháng sinh; xuất hiện thay tableau tường ở cuối P11.
10. **Đường cong dầu K2:** 370 (1화) → 360 "시동 점검 열 킬로" (SC_038) → 310 "언덕 + 하루 시동, 오십 킬로 몫" (SC_255) → "삼백" (SC_273, làm tròn) · tổng gom mọi xe + 1 phuy = "사백" (SC_273) → ledger 2화 "~300 trong K2 †" và "400 딱" 3화 ✓. Máy phát K151: "드론 열다섯 번 = 삼십 일" (SC_039–040).
11. **Kháng sinh:** 20 lọ = 100 % (1화 "스무 개") → 18 (90 %, 1화) → 13 → 12 = 60 % (SC_045–046) → 0 (SC_155: 20 đêm tên lửa + đêm hỏa công). 서아 dùng 6 lọ cho Goguryeo trong 3 tuần (SC_047).
12. **40mm cháy 200** = toàn bộ đạn trên 천둥 4 (SC_146/151) → 280 → cổng bắc −60 (천둥 2) → 220 (SC_254) ✓ ledger. **K3 −1.200** nói trong N (SC_254). K6/K4 không dùng trong tập (K6 trên xe ở thung lũng; K2 có K6 cupola nhưng không bắn — đề xuất giữ kho).
13. **양제 [史] 6월 11** lời mắng tướng → thoại paraphrase "짐이 왔다. 그대들이 무엇을 하는지, 짐이 보겠다." (SC_200) + N nêu ý "겁쟁이".
14. **Tuổi tường "이백 년"** (Goguryeo chiếm Liêu Đông ~404 → ~208 năm; SC_016/017/058/158) thay "삼백 년" — cần world-designer xác nhận.
15. **Tháp "마흔"** là số kịch của outline (sử chỉ ghi nhiều 팔륜누차); narrator dùng "마흔이 넘었습니다" ở P9–P10 sau khi Tùy đóng thêm.
16. Phase 6 P10: "1 shot tường reo + 1 shot K2 lùi" gộp thành SC_249 (reo = âm xa, đúng quy tắc 1 SC = 1 địa điểm).
17. 을지문덕 chạm K2 **2 lần** (SC_160, 246) + N "마지막은 강가에서" (SC_171) — foreshadow 5화; bible 5화 nên ghi "lần thứ ba".
18. 육합성 + hỏa công cùng ngày D45 (5월 초); 3차 공성 D71 = 6월 11 [史]; hội đồng 9군 D72–74; 9 quân đi D75 — narrator "며칠 뒤 밤" (SC_267).

### D. Quote đắt (KO / VI) — ứng viên title/thumbnail/hook
1. 을지문덕 SC_078: **"쇠수레는 며칠이나 달릴 수 있소?"** / "Xe sắt chạy được mấy ngày?"
2. 을지문덕 SC_093: **"열 발에 둘. 그럼 스무 개엔 백 발이오."** / "Mười viên hạ hai. Vậy hai mươi tháp là trăm viên."
3. 을지문덕 SC_118: **"황제를 죽이면 백만이 돌아가겠소, 아니면 백만이 미치겠소?"** / "Giết Hoàng đế thì trăm vạn về nhà, hay trăm vạn phát điên?"
4. 탁발흠 SC_129: **"말은 풀을 먹고, 쇠수레는 검은 물을 마신다."** / "Ngựa ăn cỏ, xe sắt uống nước đen."
5. 박기철 SC_274: **"여기서 청천강까지 400km. 연료는 전차 한 대 몫뿐입니다."** / "Từ đây tới Thanh Xuyên giang 400 km. Dầu chỉ đủ một xe tăng."
6. 윤서아 SC_155: **"항생제, 없습니다. 이제부턴 이 사람들 약초입니다."** / "Kháng sinh, hết rồi. Từ giờ là thuốc cỏ của người ở đây."
7. 을지문덕 SC_264: **"성은 버티오. 문제는 평양이오."** / "Thành thì trụ được. Vấn đề là Bình Nhưỡng."
8. 을지문덕 SC_246: **"그럼 이제 내려가시오. 그건 여기 것이 아니오."** / "Vậy giờ xuống đi. Thứ ấy không thuộc về nơi này."
9. 을지문덕 SC_178: **"조상은 돌을 지키라고 쌓지 않았소. 사람을 지키라고 쌓았소."** / "Tổ tiên xây tường không phải để giữ đá. Để giữ người."
10. 을지문덕 SC_102: **"쇠는 세면 줄고, 나무는 베면 는다."** / "Sắt đếm thì vơi, gỗ chặt thì đầy."
11. 탁발흠 SC_150: **"검은 물이 탄다. 그럼 쇠수레도 탄다."** / "Nước đen cháy được. Vậy xe sắt cũng cháy được."
12. 박기철 SC_167: **"전차 시동 한 번이 드론 열 번입니다."** / "Một lần nổ máy xe tăng bằng mười lần bay drone."
13. 을지문덕 SC_159: **"성은 성이 막소. 나는 쇠수레를 보러 왔소."** / "Thành thì thành tự giữ. Tôi đến để xem xe sắt."
14. 한승우 SC_112: **"우리 것이 아닙니다. 그렇다고 왕의 것도 아닙니다."** / "Không phải của chúng tôi. Nhưng cũng không phải của vua."
15. 탁발흠 SC_283: **"막지 않는다. 뒤를 밟는다."** / "Không chặn. Bám đuôi."

### E. Tự chấm 18 chỉ số `docs/benchmark_vs_reference.md` — 2화 (script v1; không sửa file benchmark)
| # | Chỉ số | Mục tiêu | 2화 | Kết |
|---|---|---|---|---|
| 1 | Giây đầu có nguy hiểm/câu hỏi | ≤0:10 | **0:03** tiếng cót két trong màn đen; 0:24 mũi nỏ cắm giá trống | ✅ |
| 2 | Shot trong 30 s đầu | ≥5 | **6** (SC_001 2-BEAT · 002 · 003 2-BEAT · 004) | ✅ (gốc 13 ❌) |
| 3 | Narrator 30 s đầu | 0 | **0** — vào 0:48 "612년 4월. 요동성." | ✅ |
| 4 | Giao tranh đầu | ≤7:00 | Nguy cơ 0:24 (nỏ); xung phong 1:50 (SC_015); đại đội bóp cò **9:02** (PZF, SC_068; 1화: 12:14) | ✅ giao tranh; ⚠️ đại đội bắn sau 7:00 (do kế cờ hàng giả P2) |
| 5 | Combat/runtime | ≥35 % (brief ≥30 %) | **844 s = 35,2 %**, 11 cụm / 5 khối thật + 6 mini (1화 v3: 30,2 %) | ✅ sát mục tiêu (gốc 45 % ❌) |
| 6 | Khoảng cách beat retention tối đa | ≤4' | Action: 3:16 (15:46→19:02); beat bất kỳ (số/quyết định/địch học): ≤1:30 | ✅ |
| 7 | Con số tài nguyên nói thành lời | ≥6 | **~36 câu thoại có số** (22발·140/140/200·110·18·3·360·10km·15회/30일·13→12/60 %·17·닷새/한 달·110/120·10/2/100/200·100·38→40·6리·2대/1/2/200·22/360·1탑·10발·20도/10km·40발·100걸음·60·12·60/12/220·50km/310·9군/305,000·100일·300/400·400km) + N | ✅ |
| 8 | Enemy POV | ≥5 cảnh, địch có tên & học | **~45 SC** (lều vàng ×3 · trại Tùy ×8 · 탁발흠 ×12 · 육합성 ×12 · đài 양제 ×5 · aerial địch ×5). 탁발흠 học 3 (검은 물 · 그물·항아리 · 뒤를 밟는다), 공성총관 học 2 (흙 hai lớp · nỏ vào khe), 양제 học 1 (bỏ lệnh nhận hàng) | ✅ |
| 9 | Nhân vật lịch sử quyết định | ≥3 | Người thật: 을지문덕 ×7 (thử · từ chối đánh hoàng đế · rời tường xem xe · giới hạn 10 · phá tường trong · rút K2 · đi nam), 양제 ×4 (giao đêm · bỏ lệnh · 9군 · 따라붙어라), 우중문/우문술 ×1 · hư cấu: 고정수 ×4, 탁발흠 ×3 | ✅ (1화: 2 người thật → 2화: 4) |
| 10 | Số câu thoại | 120–160 | **145** | ✅ |
| 11 | Thoại >12 어절 | 0 | **0** | ✅ |
| 12 | Quote đắt | ≥5 | **15** (mục D) | ✅ |
| 13 | Shot trung bình | 8–10 s | **8,36 s**; P10 8,08 s → veo-stage 2-beat | ✅ / ❌ gốc 4 s trong trận |
| 14 | Kết mở | có + hạt series | 400 km + 5 xe không đi được + 탁발흠 bám đuôi + K21 천둥 3 "chốt sắt" (SC_278 = xe sẽ rơi vào tay Tùy 3화) + end card 3화 | ✅ |
| 15 | Mid-roll sau open loop nhỏ | 4 | 7:00 · 14:00 · 21:00 · 27:30, mỗi điểm sau open loop + 1 SC không thoại | ✅ |
| 16 | Yếu tố riêng | hậu cần · bỏ xe · để địch đi qua · địch có tên | Que đo dầu xếp hàng (SC_272) · bảng đếm "10" khoanh (SC_172) · "그럼 나머지는요?" (bỏ xe, gieo 3화) · 9 quân đi qua thành, thành đứng nhìn (SC_267–268, gieo 4화) · 탁발흠 학 3 bài · kế hàng giả [史] của tổ tiên thắng bằng đầu | ✅ 6/6 |
| 17 | Lỗi lịch sử cứng | 0 | Tự kiểm 0: lệnh 2 dòng 양제 [史] · 육합성 1 đêm/8리 [史] · 6월 11 nam thành mắng tướng [史] · 9군 30만 5천 [史] · 100일/3석 [史] · 2.700 [史] · 우중문 낙랑도/우문술 부여도 (không nêu đạo, chỉ vai) · 시호 0 vi phạm. Mềm: "탑 마흔", "이백 년" tường, "여섯 리" — hư cấu có lý | ✅ / ⚠️ 3 số mềm |
| 18 | Trình tự giống kênh gốc | KHÔNG | Không: tháp sương → hàng giả → người lạ đếm → PZF → thử ít đạn → giết hoàng đế? → đốt dầu → thuốc 0 → phá tường tổ tiên → rút xe khi thắng → 9 quân → 400 km. Kết không phải "2 chỉ huy trên tường → lều địch → card" | ✅ |

**Kết luận tự chấm 2화:** HƠN 1화 ở #4 (9:02 vs 12:14), #5 (35,2 % vs 30,2 %), #9 (4 người thật vs 2), #2 (6 vs 4→6), #16 (6/6). Còn THUA kênh gốc: #4 đại đội bắn sau 7:00 (cấu trúc hàng giả), #5 (45 %), #13 shot trong trận 8 s.

### F. Điểm cần user quyết (chi tiết trong logs/proposals.md P-38…P-45)
- "탑 마흔" (số kịch, sử không ghi số) — giữ hay "수십"?
- 2차 공성 do Goguryeo tự giữ (P8, thêm ngoài outline) — giữ (khuyến nghị) hay bỏ?
- "이백 년" tuổi tường Liêu Đông — world-designer xác nhận.
- 고정수 "황제가 눈치챘소" (하오) nói với 한승우 thay vì với 을지문덕 — chấp nhận?
- 서아 3 câu / 태오 2 câu — có cần thêm để cân giọng?
