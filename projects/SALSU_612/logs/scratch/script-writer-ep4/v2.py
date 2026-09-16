import re,sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
cnt=0
def R(old,new,count=1):
    global s,cnt
    n=s.count(old)
    assert n>=1, "NOT FOUND: "+old[:80]
    if count=='all': s=s.replace(old,new); cnt+=n
    else:
        assert n==count, f"count {n}!={count}: "+old[:80]
        s=s.replace(old,new); cnt+=1

# ---------- HEADER ----------
R("# 살수 612 — 4화 「평양」 대본 v1","# 살수 612 — 4화 「평양」 대본 v2 (QC-fixed)")
R("> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (239 video8s + 48 still_kenburns 8–12 s) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer",
"> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (239 video8s + 48 still_kenburns 8–12 s) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer\n> **v2 (QC-fixed, 2026-09-16):** áp dụng logs/qc_ep4_script.md (1 BLOCK phương án B + 16 FIX + NOTE ≤1 dòng + đề xuất #1/#2/#3) theo decisions.md mục \"sau QC 4화 → v2\". Không đổi số SC / thời gian / SC ID / open loop / quotes / mid-roll. Nhật ký thay đổi ở phụ lục C-v2. Quy ước mới: `2-BEAT` được đánh dấu trong [ACTION-VI] ở 8 SC trận (P7/P10); `[OVERLAY]` = chữ hiện ở khâu edit (bộ đếm 잔탄 08→07→06).")
R("> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi \"X일째/이틀 뒤/간밤에/사흘째 밤\" trong narration rà theo bảng này):**",
"> **BẢNG NGÀY/ĐÊM (đếm theo SC — mọi \"X일째/이틀 뒤/간밤에/사흘째 밤\" trong narration rà theo bảng này). Mốc chéo: 4화 D1 = 3화 D20 (3화 tới 살수 = D17 = 4화 D−3); 태오 bị bắt 3화 D14 đêm → 4화 D7 = 12 ngày (\"열이틀\"); 천둥 3 + drone rời bờ tây 압록 3화 D16 → 4화 D7 = 10 ngày (\"열흘째\"):**")
R("> | D8 | ngày | SC_262–267, SC_283–286 | 탁발흠 quỳ trước 우중문 giữa đường rút; 우문술 \"살수까지 이틀\" |",
"> | D8 | ngày [史] | SC_262–267, SC_271–276, SC_283–286 | 방진 rút về bắc, kỵ Goguryeo đánh bốn mặt; 을지문덕 trên gò \"살수로\"; 탁발흠 quỳ trước 우중문 giữa đường rút; 우문술 \"살수까지 이틀\" |")

# ---------- FIX 1: 이천 년 → 천사백 년 ----------
R("이천 년","천사백 년",'all')

# ---------- FIX 2: SC_103 ----------
R("N: 을지문덕이었습니다. 들에서 하룻밤만 성으로 들어온 것이었습니다. 삼십만은 삼십 리 밖에 있었습니다. 삼십 리는 그에게 하룻밤 거리였습니다.",
  "N: 을지문덕이었습니다. 들에서 하룻밤만 성으로 들어온 것이었습니다. 삼십만은 아직 이틀 거리에 있었습니다. 그는 늘 그들보다 반나절 앞에 있었습니다.")
# ---------- FIX 3: SC_081 ----------
R("이틀 전에 닫으라 한 사람이 열라 했습니다.","전날 닫으라 한 사람이 열라 했습니다.")
# ---------- FIX 4: timeline ----------
R("N: 태오는 돌아왔습니다. 드론과 쇠수레는 이미 서쪽으로 보름째 가고 있었습니다.","N: 태오는 돌아왔습니다. 드론과 쇠수레는 이미 서쪽으로 열흘째 가고 있었습니다.")
R("N: 보름 남짓 만이었습니다. 태오는 그 눈을 알아보았습니다.","N: 열이틀 만이었습니다. 태오는 그 눈을 알아보았습니다.")
# ---------- FIX 5: cẳng tay phải ----------
R("dao găm rạch ngang cẳng tay trái hắn; 탁발흠 giật lùi, kính đêm lệch trên mắt, mũ lông rơi xuống nước rồi hắn vớt lại.",
  "dao găm rạch ngang cẳng tay phải hắn — tay cầm đao; 탁발흠 giật lùi, kính đêm lệch trên mắt, mũ lông rơi xuống nước trôi đi.")
R("[ACTION-VI] 탁발흠 về tới chỗ ngựa, xé vạt áo băng cẳng tay, tháo kính đêm khỏi mũ,",
  "[ACTION-VI] 탁발흠 về tới chỗ ngựa, đầu trần, xé vạt áo băng cẳng tay phải, tháo kính đêm khỏi dây đeo,")
R("[ACTION-VI] 탁발흠 ngồi xổm trước cũi, cẳng tay trái băng vải, kính đêm trên mũ;","[ACTION-VI] 탁발흠 ngồi xổm trước cũi, cẳng tay phải băng vải, kính đêm trên mũ lông cáo mới;")
R("quỳ thẳng trong bùn trước ngựa 우중문; cẳng tay băng, kính đêm treo trước ngực.","quỳ thẳng trong bùn trước ngựa 우중문; cẳng tay phải băng, kính đêm treo trước ngực.")
R("kính đêm treo ngực đọng nước, cẳng tay băng, bím tóc ướt;","kính đêm treo ngực đọng nước, cẳng tay phải băng, bím tóc ướt;")
R("탁발흠 lao vào, bị chém cẳng tay, chạy thoát","탁발흠 lao vào, bị chém cẳng tay phải, chạy thoát")
R("bị 백성민 chém cẳng tay (khớp derived state \"vết cắt cẳng tay\" trong character_bible)","bị 백성민 chém cẳng tay phải (khớp derived state \"a fresh cut on the right forearm\" trong character_bible)")
# ---------- FIX 6: vòng đuốc đông ----------
R("[ACTION-VI] Viên thứ hai nổ lệch trái: khối cung thủ vỡ, người chạy tán loạn xuống nước, đuốc rơi tắt hàng loạt; trống trên mọi hướng ngừng cùng lúc. Aerial trung.",
  "[ACTION-VI] Viên thứ hai nổ lệch trái: khối cung thủ vỡ, người chạy tán loạn xuống nước, đuốc rơi tắt hàng loạt; ở rìa khung phía đông, dải đuốc kia cũng vỡ — người cầm đuốc là dân phu Tùy, ném đuốc xuống nước bỏ chạy về bờ nam; trống trên mọi hướng ngừng cùng lúc. Aerial trung. [OVERLAY] kết clip: cận màn hình trưởng xe, bộ đếm nháy \"잔탄 06\".")
R("N: 그들은 침묵을 잃었습니다. 대신 밤을 얻었습니다. 삼 킬로 상류에 두 번째 갈대 섬이 있었습니다.",
  "N: 그들은 침묵을 잃었습니다. 대신 밤을 얻었습니다. 동쪽 고리는 소리 하나에 풀렸습니다. 그 틈으로 그들은 상류로 갔습니다. 삼 킬로 상류에 두 번째 갈대 섬이 있었습니다.")
# ---------- FIX 7: người trúng tên bụng ----------
R("một lính Hàn trong hố ngã ngửa — mũi tên cắm cổ, tay bạn kéo anh xuống (không cận); 한승우 nhìn về cửa bãi cạn",
  "một lính Hàn trong hố ngã ngửa — mũi tên cắm cổ, tay bạn kéo anh xuống (không cận); cách đó 3 m một người khác gập người ôm bụng, cán tên lộ giữa hai bàn tay; 한승우 nhìn về cửa bãi cạn")
R("N: 동쪽 고리는 끊기지 않았습니다. 한 사람이 목에 화살을 맞았습니다. 그리고 여울 어귀의 횃불 무리는 움직이지 않았습니다. 기다리는 쪽이었습니다.",
  "N: 동쪽 고리는 끊기지 않았습니다. 한 사람이 목에, 한 사람이 배에 화살을 맞았습니다. 여울 어귀의 횃불 무리는 움직이지 않았습니다. 기다리는 쪽이었습니다.")
# ---------- FIX 8: PZF 2 xạ thủ ----------
R("[ACTION-VI] Từ nam, ba bè lau chở đuốc và cung thủ Tiên Ti đẩy qua nhánh nước về phía đảo; xạ thủ PZF quỳ trong lau bắn — quả thứ nhất, thứ hai, thứ ba: bè nổ tung, lửa trên mặt nước. Máy từ sau vai xạ thủ.",
  "[ACTION-VI] 2-BEAT (4 s + 4 s): (a) từ nam, ba bè lau chở đuốc và cung thủ Tiên Ti đẩy qua nhánh nước về phía đảo; hai xạ thủ PZF quỳ cạnh nhau trong lau bắn gần như cùng lúc — hai bè nổ tung; (b) phụ nạp tháo ống rỗng, lắp ống mới vào cụm ngắm của xạ thủ thứ nhất — quả thứ ba rời nòng khi clip kết, bè thứ ba bốc lửa trên mặt nước. Máy từ sau vai xạ thủ.")
# ---------- FIX 9: SC_035 ----------
R("sáu ống PZF-3 xếp dưới tấm poncho;","chín ống PZF-3 xếp dưới tấm poncho;")
# ---------- FIX 10: cọc ----------
R("nước đã lên tới vạch thứ tư; sương bắt đầu phủ mặt sông; mưa tạnh. Ken-burns đẩy vào vạch thứ tư.","nước đã lên tới vạch thứ sáu; sương bắt đầu phủ mặt sông; mưa tạnh. Ken-burns đẩy vào vạch thứ sáu.")
R("[ACTION-VI] Ảnh: hoàng hôn xám trên bãi bắc — cọc gỗ nghiêng trong nước đã dâng, lau ngập,","[ACTION-VI] Ảnh: hoàng hôn xám trên bãi bắc — cọc gỗ nghiêng trong nước đã dâng gần ngập tới vạch trên cùng, lau ngập,")
# ---------- FIX 11: 해모루 rời đảo đêm D4 ----------
R("N: 넷째 날 오후. 탁발흠은 우리를 강가로 옮겼습니다. 갈대밭에서 보이는 자리였습니다.","N: 넷째 날 오후. 해모루는 답 없이 마을로 돌아갔습니다. 탁발흠은 우리를 강가로 옮겼습니다. 갈대밭에서 보이는 자리였습니다.")
R("N: 전령이 남으로 달렸습니다. 이백 리. 그가 가진 것은 한 문장이었습니다.","N: 전령이 남으로 달렸습니다. 이백 리. 그가 가진 것은 한 문장이었습니다. 북쪽 마을에서 해모루도 그 소리를 들었습니다. 그는 남으로 달렸습니다.")
# ---------- FIX 12: SC_173 ----------
R("N: 여섯째 날. 일곱 번 지고, 사만을 깨고, 천둥을 두 번 듣고 나서 을지문덕은 붓을 들었습니다.","N: 여섯째 날. 일곱 번 지고, 사만을 깨고, 천둥이 두 번 울렸다는 말을 듣고 나서 을지문덕은 붓을 들었습니다.")
# ---------- FIX 13: SC_118 ----------
R("N: 오태민은 사흘을 참았습니다. 강가에서 우리를 본 뒤로는 하루도 참기 어려웠습니다.","N: 오태민은 사흘을 참았습니다. 강 건너 우리 이야기를 들은 뒤로는 하루도 참기 어려웠습니다.")
# ---------- FIX 14: SC_074 ----------
R("탁발흠: 찾았다. 갈대밭 안이다. 어디쯤인지는 내일 밤에.","탁발흠: 찾았다. 갈대밭 안이다. 어디쯤인지는 다음 밤에.")
# ---------- FIX 15: SC_246 ----------
R("서아: 부러졌어요. 모르핀은 안 써요.","서아: 부러졌습니다. 모르핀은 안 씁니다.")
R("SC_246 \"모르핀은 안 써요\"","SC_246 \"모르핀은 안 씁니다\"")
# ---------- FIX 16: SC_130 tense ----------
R("동쪽과 남쪽에서 반달처럼 조여 서쪽 여울로 몹니다. 여울 어귀에는 궁수 오백이 무릎을 꿇고 기다립니다.","동쪽과 남쪽에서 반달처럼 조여 서쪽 여울로 몰았습니다. 여울 어귀에는 궁수 오백이 무릎을 꿇고 기다렸습니다.")

# ---------- NOTES ≤1 dòng ----------
R("우문술은 부총관이었지만, 이 순간 군은 그의 것이었습니다.","우문술은 우중문 아래 있었지만, 이 순간 군은 그의 것이었습니다.")
R("N: 4만 중 수천 명만 배로 돌아갔습니다. 나머지는 시장과 골목과 강가에 남았습니다. 삼국사기는 그날을 한 줄로 적었습니다. 고구려의 매복이 있었다고.","N: 4만 중 수천 명만 배로 돌아갔습니다. 나머지는 시장과 골목과 강가에 남았습니다.")
R("N: 항생제는 두 달 전에 끝났습니다. 남은 것은 이 노인의 풀뿐이었습니다.","N: 항생제는 요동성에서 끝났습니다. 남은 것은 이 노인의 풀뿐이었습니다.")
R("N: 사흘째 밤이었습니다. 열은 배에서 시작해 온몸으로 갔습니다. 항생제는 두 달 전에 끝났습니다. 서아는 그것을 알면서 앉아 있었습니다.","N: 사흘째 밤이었습니다. 열은 배에서 시작해 온몸으로 갔습니다. 서아는 그것을 알면서 앉아 있었습니다.")
R("N: 살수를 건너기 전 엿새 동안, 을지문덕은 하루에 일곱 번 싸웠습니다.","N: 살수를 건너기 전 열흘 동안, 을지문덕은 하루에 일곱 번 싸웠습니다.")
R("그렇게 엿새, 마흔두 번을 졌습니다.","그렇게 열흘, 일흔 번을 졌습니다.")
R("N: 우문술은 열흘 전부터 같은 말을 했습니다.","N: 우문술은 보름 전부터 같은 말을 했습니다.")
R("얼굴은 열흘 전보다 더 깊었습니다.","얼굴은 보름 전보다 더 깊었습니다.")
R("박기철: 아흔한 명. 야시경 배터리 이십.","박기철: 아흔한 명. 야시경 배터리 이십. 무전기 삼십.")
R("N: 이 킬로 밖에서도 얼굴이 보였습니다. 스물한 살의 얼굴이었습니다.","N: 이 킬로 밖에서도 누군지 보였습니다. 얼굴은 안 보여도 알았습니다.")
R("hắn cúi nhặt một vỏ đạn 120 mm đen bồ hóng, nặng, xoay trong tay; đếm bằng ngón.","hắn cúi nhặt đế vỏ đạn 120 mm — vành thép to bằng bàn tay, đen bồ hóng — xoay trên ngón tay; đếm bằng ngón.")
R("N: 살수. 이레 전에는 무릎이었습니다. 지금은 허리였습니다. 물은 매일 올랐습니다. 비는 매일 왔습니다.","N: 살수. 이레 전에는 무릎이었습니다. 지금은 허리였습니다. 물은 매일 올랐습니다. 어떤 날은 한 뼘, 어떤 날은 반 뼘. 비는 매일 왔습니다.")
R("[ACTION-VI] Insert: trên mô cát cửa bãi cạn, trong tối, hàng trăm cung thủ Tùy quỳ thành ba hàng, cung giương, một sĩ quan Tiên Ti đi sau lưng họ với đuốc che tay; họ nhìn về bãi lau đang bị lùa. Máy thấp ngang cung.",
  "[ACTION-VI] Insert: trên mô cát cửa bãi cạn, trong tối, hàng trăm cung thủ Tùy quỳ thành ba hàng, cung giương — wide ngược sáng đuốc từ sau lưng hàng cung, chỉ thấy viền người và cung; một sĩ quan Tiên Ti đi sau lưng họ với đuốc che tay là người duy nhất rõ mặt; họ nhìn về bãi lau đang bị lùa.")
R("thúc xuống nước về phía 누선 gần nhất; áo choàng dầu cháy một góc từ đuốc rơi. Tracking theo ngựa xuống nước.","thúc xuống nước về phía 누선 gần nhất. Tracking theo ngựa xuống nước.")
R("[SOUND] ngựa, nước, lửa nhỏ, thét sau lưng.\nN: 내호아는 안장 없는 말로","[SOUND] ngựa, nước, thét sau lưng.\nN: 내호아는 안장 없는 말로")
R("[ACTION-VI] 해모루 hạ giọng, nhắc nguyên văn câu cuối của 장군, mắt nhìn thẳng 한승우 — chữ nào cũng chậm.","[ACTION-VI] 해모루 bước xuống mép nước, cúi rửa tù và trong dòng sông, nói khi đang cúi — nhắc nguyên văn câu cuối của 장군, chữ nào cũng chậm; 한승우 đứng phía sau. Walk-and-talk.")
R("[ACTION-VI] Ảnh: 을지문덕 trên ngựa ở đỉnh gò, giáp ướt, chỏm lông rủ; 해모루 bên cạnh, kỵ binh và cờ 삼족오 phía sau; dưới gò xa, hình vuông tối bò về bắc.","[ACTION-VI] Ảnh: 을지문덕 một mình trên ngựa ở đỉnh gò, giáp ướt, chỏm lông rủ; sau lưng chỉ có lính cờ với lá 삼족오 ướt; dưới gò xa, hình vuông tối bò về bắc.")
R("### SC_274 · LOC_008_GOGURYEO_VILLAGE (gò cao, mưa) · CHAR_101, CHAR_105 · VEH_101, PROP_012","### SC_274 · LOC_008_GOGURYEO_VILLAGE (gò cao, mưa) · CHAR_101 · VEH_101, PROP_012")
R("ông kéo cương quay ngựa về bắc — về phía con sông. 해모루 theo. Máy theo ngựa quay.","ông kéo cương quay ngựa về bắc — về phía con sông; lính cờ theo. Máy theo ngựa quay.")
R("아리: 이쪽이에요!","아리: (속삭임) 이쪽이에요.")
R("고건무 vào cuối cùng, tự tay khép cửa gỗ ba gian, ngồi xuống với khiên. Ánh sáng tắt dần theo cửa.","고건무 vào cuối cùng, ra lệnh; hai lính khép cửa gỗ ba gian theo lệnh, một bàn tay che tắt đèn; ông ngồi xuống với khiên. Ánh sáng tắt dần theo cửa.")
R("박기철은 나무 막대에 눈금을 새겨 물에 꽂았습니다.","박기철은 이번에는 눈금을 새긴 막대를 꽂았습니다.")
R("갈대밭의 박기철은 알았습니다. 이십.","갈대밭의 박기철은 자기 것을 알았습니다. 이십. 그 둘도 같은 건전지였습니다.")
R("chìa máy đếm tay — con số ba chữ số đã quay vòng nhiều lần;","chìa máy đếm tay — con số bốn chữ số đã quay vòng nhiều lần;")
R("N: 사람을 세는 기계는 천에서 다시 영으로 돌아갔습니다.","N: 사람을 세는 기계는 만에서 다시 영으로 돌아갔습니다.")

# ---------- BLOCK B: mũ 태오 ----------
R("[ACTION-VI] Bàn tay bùn của 한승우 đặt lên đầu 태오 — tóc cắt nham nhở của tù binh; ông nói một câu, không nhìn ai khác.",
  "[ACTION-VI] Bàn tay bùn của 한승우 đặt lên đầu 태오 — tóc cắt nham nhở của tù binh; tay kia ông đặt xuống lau cạnh đầu cậu chiếc mũ trống ngàm kính đêm của 태오 — mũ 한승우 mang từ 석문령; ông nói một câu, không nhìn ai khác.")
R("N: 석문령에서 잃은 철모는 돌아오지 않았습니다. 해모루가 다른 것을 씌웠습니다. 육백십이 년의 쇠였습니다. 태오는 그것을 벗지 않았습니다.",
  "N: 석문령의 빈 철모는 한승우가 가지고 왔습니다. 눈이 없는 철모였습니다. 해모루가 먼저 다른 것을 씌웠습니다. 육백십이 년의 쇠였습니다. 태오는 그것을 벗지 않았습니다.")
R("[ACTION-VI] 태오 ngồi dựa váy xích K2, chân phải nẹp lau và băng, áo 저고리 vải gai khoác ngoài áo rằn ri; 해모루 đến,",
  "[ACTION-VI] 태오 ngồi dựa váy xích K2, chân phải nẹp lau và băng, áo 저고리 vải gai khoác ngoài áo rằn ri; chiếc mũ Hàn trống ngàm kính đặt bên đùi cậu; 해모루 đến,")

# ---------- Đề xuất #1: 2-BEAT ----------
R("[ACTION-VI] Đạn cối nổ dọc dải đuốc — nước và bùn bùng lên, đuốc văng xuống nước tắt, trống trên xe bò đổ nghiêng; từ đảo, K3 quét tracer thành dải sáng đỏ ngang lau; 오태민 bắn K3, mặt sáng lửa. Wide.",
  "[ACTION-VI] 2-BEAT (4 s + 4 s): (a) cận — đạn cối nổ dọc dải đuốc, nước và bùn bùng lên, đuốc văng xuống nước tắt, trống trên xe bò đổ nghiêng; (b) wide từ đảo — K3 quét tracer thành dải sáng đỏ ngang lau; 오태민 bắn K3, mặt sáng lửa.")
R("[ACTION-VI] Tháp pháo K2 xoay dưới lớp bùn và lau — bùn nứt, lau rơi khỏi nòng; trong xe, kính ngắm nhiệt: một khối trắng nóng đông đặc trên mô cát cửa bãi cạn; tay pháo thủ trên cần.",
  "[ACTION-VI] 2-BEAT (4 s + 4 s): (a) tháp pháo K2 xoay dưới lớp bùn và lau — bùn nứt, lau rơi khỏi nòng; kính ngắm nhiệt: một khối trắng nóng đông đặc trên mô cát cửa bãi cạn; (b) cận màn hình trưởng xe: bộ đếm \"잔탄 08\" — [OVERLAY] chữ hiện ở edit; tay pháo thủ trên cần.")
R("[ACTION-VI] K2 khai hỏa — chớp lửa xé đêm mưa trắng một khoảnh khắc, lau quanh xe rạp; viên đạn nổ giữa mô cát cửa bãi cạn: cột nước-cát-đuốc bốc lên, cung thủ văng xuống nước. Wide từ đảo nhìn ra. Không thoại.",
  "[ACTION-VI] 2-BEAT (3 s + 5 s): (a) cận nòng K2 khai hỏa — chớp lửa xé đêm mưa trắng một khoảnh khắc, lau quanh xe rạp; (b) wide từ đảo nhìn ra — viên đạn nổ giữa mô cát cửa bãi cạn: cột nước-cát-đuốc bốc lên, cung thủ văng xuống nước. [OVERLAY] góc khung cuối beat (b): bộ đếm nháy \"잔탄 07\". Không thoại.")
R("[ACTION-VI] Dao: lính gác thứ nhất gục xuống trong tay 백성민 không kịp mở mắt (không cận vết); lính Hàn thứ hai khóa cổ lính gác thứ hai từ sau lưng, kéo xuống sau tấm da; ba giây; sương. Máy trung, không gore.",
  "[ACTION-VI] 2-BEAT (4 s + 4 s): (a) cận — lính gác thứ nhất gục xuống trong tay 백성민 không kịp mở mắt (không cận vết); (b) wide trung — lính Hàn thứ hai khóa cổ lính gác thứ hai từ sau lưng, kéo xuống sau tấm da; ba giây; sương. Không gore.")
R("[ACTION-VI] Con chó sủa — dữ dội, tiếng vang trong sương; lao tới mép hố nước; một lính gác Tùy ở lối vào trại giật mình, nâng tù và bằng ốc lên thổi. Máy trung.",
  "[ACTION-VI] 2-BEAT (3 s + 5 s): (a) cận mõm chó — sủa dữ dội, tiếng vang trong sương, lao tới mép hố nước; (b) wide — một lính gác Tùy ở lối vào trại giật mình, nâng tù và bằng ốc lên thổi.")
R("[ACTION-VI] Tù và Goguryeo — một hồi dài trầm; 300 kỵ bật ra khỏi sương thành hàng ngang lao về sườn đông trại hậu quân, cờ 삼족오 ướt bay. Wide thấp.",
  "[ACTION-VI] 2-BEAT (3 s + 5 s): (a) cận môi 해모루 trên tù và sừng đen — một hồi dài trầm; (b) wide thấp — 300 kỵ bật ra khỏi sương thành hàng ngang lao về sườn đông trại hậu quân, cờ 삼족오 ướt bay.")
R("[ACTION-VI] Kỵ Tiên Ti bước vào lối lau — nước trước mặt hắn bùng lên: 백성민 từ dưới nước, dao; hai người quay tròn dưới mặt nước, chỉ thấy lưng, tay, sóng; rồi mặt nước lặng, một cánh tay Tiên Ti chìm. Máy ngang mặt nước, không cận.",
  "[ACTION-VI] 2-BEAT (4 s + 4 s): (a) cận mặt nước ngang tầm — kỵ Tiên Ti bước vào lối lau, nước trước mặt hắn bùng lên: 백성민 từ dưới nước, dao; hai người quay tròn dưới mặt nước, chỉ thấy lưng, tay, sóng; (b) wide — mặt nước lặng dần, một cánh tay Tiên Ti chìm. Không cận vết thương.")
R("[ACTION-VI] Kỵ Goguryeo tới mô cát: một người kéo 태오 vắt ngang yên; người khác xốc 아리 lên sau lưng; 백성민 nắm bàn đạp một con ngựa, hai lính nắm đuôi; ngựa quay đầu về bờ bắc. Máy trung, nhanh.",
  "[ACTION-VI] 2-BEAT (4 s + 4 s): (a) cận — bàn tay giáp Goguryeo kéo 태오 vắt ngang yên, 아리 bị xốc lên sau lưng một kỵ sĩ; (b) wide nhanh — 백성민 nắm bàn đạp một con ngựa, hai lính nắm đuôi; ngựa quay đầu về bờ bắc.")
R("[ACTION-VI] Ba kỵ Tiên Ti cách 80 m giương cung trong nước; từ hố lau bờ bắc, K6 nổ một loạt dài — mặt nước bùng lên thành một hàng cột nước ngay trước mũi ba con ngựa; ngựa dựng đứng, hất kỵ sĩ xuống nước. Wide.",
  "[ACTION-VI] 2-BEAT (3 s + 5 s): (a) cận nòng K6 trong hố lau bờ bắc nháy lửa — một loạt dài, vỏ đạn văng; (b) wide — mặt nước bùng lên thành một hàng cột nước ngay trước mũi ba con ngựa Tiên Ti cách 80 m; ngựa dựng đứng, hất kỵ sĩ xuống nước.")

# ---------- Đề xuất #3: 해모루 radio ----------
R("[ACTION-VI] 해모루 nghe tù và Tùy từ trại; nâng tù và sừng đen lên môi; 300 kỵ sau lưng siết cương. Cận môi và sừng.\n[SOUND] tù và Tùy xa, ngựa, hít hơi.\nN: 그때 동쪽에서.",
  "[ACTION-VI] 해모루 nghe tù và Tùy từ trại; bấm tổ hợp radio kẹp trên giáp, nói một câu vào \"말하는 돌\"; rồi nâng tù và sừng đen lên môi; 300 kỵ sau lưng siết cương. Cận radio, môi và sừng.\n[SOUND] tù và Tùy xa, PTT, ngựa, hít hơi.\nN: 그때 동쪽에서.\n해모루: 한 대장, 여기는 해모루. 나각 부오.")
R("N: 태오는 무전을 맡았습니다. 걸을 수 없는 사람이 할 수 있는 일이었습니다. 하늘의 눈은 잃었지만 귀는 남았습니다.",
  "N: 태오는 무전을 맡았습니다. 걸을 수 없는 사람이 할 수 있는 일이었습니다. 하늘의 눈은 잃었지만 귀는 남았습니다. 그 돌로 고구려 말객이 나각을 알렸습니다. 이제 그 돌은 태오의 무릎에 있었습니다.")

# ---------- Appendix references ----------
R("2. **Open loop P10:** \"드론과 **쇠수레**는 이미 서쪽으로 **보름째**\" (outline: 야시경 · 열흘째) — vì 3화 P11 khóa \"야시경은 보내지 않았습니다\" và 탁발흠 đang dùng kính; mốc thời gian ~15 ngày từ 석문령 (đồng bộ \"보름 남짓 만\" SC_210, \"보름 전\" SC_248).",
  "2. **Open loop P10:** \"드론과 **쇠수레**는 이미 서쪽으로 **열흘째**\" (outline: 야시경) — vì 3화 P11 khóa \"야시경은 보내지 않았습니다\" và 탁발흠 đang dùng kính; \"열흘째\" giữ theo outline/bảng ngày 3화 (v2); SC_210 \"열이틀 만\" (bị bắt 3화 D14 → 4화 D7), SC_248 \"보름 전\" (3화 D11 \"살아 있어야 해\").")
open(p,'w',encoding='utf-8').write(s)
print("edits applied:",cnt)
