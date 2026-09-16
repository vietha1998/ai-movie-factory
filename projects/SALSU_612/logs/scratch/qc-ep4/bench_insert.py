import re
path = "/Users/admin/phim han quoc/docs/benchmark_vs_reference.md"
txt = open(path, encoding="utf-8").read()
vals = {
 "1": "**0:03** (SC_001b móng ngựa Tùy cách mặt 30 cm; 0:16 lính Tùy tiểu cách 백성민 2 m) ✅",
 "2": "**6** (SC_001 2-BEAT · 002 · 003 2-BEAT · 004) ✅ mục tiêu · ❌ gốc 13",
 "3": "**0** — narrator vào 0:32 \"612년 7월.\" ✅",
 "4": "Contact/threat **0:03** · [史] 1:48 (SC_014) · đại đội đánh dao **9:22** (SC_068) · **đại đội bóp cò 19:07** (cối, SC_138) — muộn nhất 4 tập, có chủ ý \"tập im lặng\" ⚠️ thua gốc theo nghĩa hỏa lực",
 "5": "Khối theo script-writer **36,9 %** (885 s, gồm P1/P3 \"địch đi qua/lạc vào\" 88 s) · QC: khối có vũ khí **~33 %** (793 s) · **thuần ~16 %** (384 s: P2 24 · P4 40 · P5 64 · P6 16 · P7 80 · P9 8 · P10 136 · P11/12 16) ❌ gốc 45 %; ✅ S40 ≥30 % (khối)",
 "6": "Mọi beat: **0:44** (27:20→28:04) · beat mạnh: **1:06** (2:32→3:38) · ~150 beat/40' ✅",
 "7": "**~23 câu thoại / ~35 con số** (92·8·20km·50·9·10/30 %·50 %·드론 0·한 뼘·배터리 삼십·94/92·이십 킬로·스무 발·두 발·여섯 발·PZF 6·박격포 30·탄창 넷·무전기 40·모르핀 하나·열여섯·사흘·91·야시경 20·이틀·어제보다 한 뼘) + màn hình \"잔탄 06\" ×2 ✅ hơn xa",
 "8": "**~88 SC** enemy POV / ~16 cảnh (탁발흠 ×10 cảnh · 내호아 ×4 · 우중문/우문술 ×5). 탁발흠 **4 bài học nói thành lời** (SC_074/129/161/218) + nhặt chốt (245) + xin cánh sườn (263) ✅ hơn",
 "9": "**14 quyết định / 6 người thật**: 고건무 3 (nhường 나곽·mở cửa·đuổi tới thuyền) · 내호아 1 (gạt 주법상) · 영양왕 2 (hỏi·viết) · 을지문덕 6 (7 trận·\"그다음\"·\"서두르게\"·thơ·\"반\"·\"살수로\") · 우문술 2 (방진·\"좁히시오\") · 우중문 1 (\"네 죄를 잊겠다\") ✅ hơn",
 "10": "**147** (한승우 13 · 박기철 12 · 해모루 10 · 탁발흠 10 · 백성민 9 · 을지문덕/서아/아리/고건무/오태민 7 · 을보 6 · 우중문/우문술/태오 5 · 내호아 4 · 영양왕 3 · phụ 30) — hiện đại 41 % / Goguryeo 33 % / Tùy 26 % ✅",
 "11": "**0** / 147 (dài nhất 11) ✅ · đăng ký: SC_246 서아 해요체 trước 중대장 (FIX), SC_130 N thì hiện tại (FIX)",
 "12": "**≥16** (\"쏘지 마. 숨 쉬는 것도 작게\" · \"우린 이제 장님입니다\" · \"야시경입니다. 우리 겁니다\" · \"평양은 고구려 사람이 지키오\" · \"누구의 군대인가\" · \"젖은 갈대는 안 탄다. 몰아낸다\" · \"좋소. 서두르게 하시오\" · \"여섯 발. 이게 답니다\" · \"천둥도 센다. 언젠가는 마른다\" · \"쏠 순 없어도 보낼 순 있다\" · \"반이 건널 때까지\" · \"어느 쪽 반입니까?\" · \"안개엔 눈이 없다. 귀로 잡는다\" · \"살아 있잖아\" · \"물은 오르고, 포탄은 여섯 발\") ✅",
 "13": "**8,36 s** (2.400/287; still 10 s ×34, 12 s ×8) · P10 **8,08 s**, **0 2-BEAT trong trận** (chỉ 2 ở hook; 3화 có 3 ở P10) ❌ gốc 4 s → qc §3 #1",
 "14": "12/12 open loop đúng outline · kết tập \"30만이 살수로… 포탄은 여섯 발\" + hạt 5화 (여울 북쪽 · \"반\" · 탁발흠 đếm 16 · nước +1 뼘/ngày) + hạt series 2 (천둥 3 + drone về 요동 SC_259) ✅",
 "15": "**4** đúng 7:00 · 14:00 · 21:00 · 27:30; sau mỗi điểm 1 SC không thoại (SC_051 cũi · 101 trại · 152 xác · 198 sương) ✅",
 "16": "6/6: hậu cần là nhân vật (sổ ×3, cọc nước, \"물\" ghi dưới 기름) ✓ · **\"để 30 vạn đi qua\" ✓ (P1)** · địch có tên & học ×4 ✓ · tổ tiên thắng không cần đại đội (빈 절) ✓ · cứu người bằng sương-dao-đường lau, K2 không bắn ✓ · chết vì hết thuốc ✓ · công nghệ đổi phe mù sương ✓ ✅",
 "17": "**0 lỗi cứng** (내호아 4만 · 주법상 · 나곽 · 500 결사대 · 해포 · 7 trận/ngày + 삼국사기 nhìn từ Tùy · 30리 산 · 60리 패수 · thơ 4 câu nguyên văn + âm Hán + dịch · sứ \"행재소 조회\" · 우중문 답장 không chép · 방진 · 사면 초격). **Mềm:** \"이천 년\" ×11 (sai số năm, 1/2/3/5화 dùng 천사백 — FIX) · \"부총관\" cho 우문술 (SC_183) · \"삼국사기 한 줄\" (SC_088) · 내호아 6월→7월 nén [推] · 시호 0 vi phạm ⚠️ FIX 이천 년",
 "18": "KHÔNG. Trình tự: móng ngựa trên mặt → 7 trận giả thua → \"장님\"/cũi → kính đêm trong tay địch, dao → 빈 절 (tổ tiên thắng) → thư vua → trống-đuốc, 2 viên → \"여섯 발\" → thơ + \"반\" → sương-dao-đường lau → chết vì sốt, 탁발흠 quỳ → cọc nước + 오태민 một mình + mưa. Không demo súng, không xe tăng cứu tinh, không tableau kết §17 (NOTE nhẹ: SC_274 2 chỉ huy trên gò giữa P12) ✅",
}
out=[]
for line in txt.split('\n'):
    if line.startswith('| # | Chỉ số |'):
        line = line.replace('| Tập 1 | Ghi chú |', '| Tập 1 | Tập 4 | Ghi chú |')
    elif line.startswith('|---|---|---|---|---|---|---|'):
        line = '|---|---|---|---|---|---|---|---|'
    else:
        m = re.match(r'^\| (\d+) \| ', line)
        if m and m.group(1) in vals:
            cells = line.split(' | ')
            # cells: ['| #', 'Chỉ số', 'gốc', 'mục tiêu', 'cách đo', 'Tập 1', 'Ghi chú |']
            assert len(cells)==7, (m.group(1), len(cells))
            cells.insert(6, vals[m.group(1)])
            line = ' | '.join(cells)
    out.append(line)
txt2='\n'.join(out)
marker = '## "Hay hơn kênh gốc" — 5 đòn bẩy cố định'
concl = '''### Kết luận chấm Tập 4 (script v1 · qc-reviewer 2026-09-16)
- **THUA kênh gốc / mục tiêu:** **#5 combat thuần ~16 % / khối 33–37 %** (gốc 45 %) · **#4 đại đội bóp cò 19:07** (gốc ≤1:36; dao 9:22) — cả hai là hệ quả thiết kế "tập im lặng" (đại đội nằm im để 30만 đi qua) · **#13 P10 8,08 s, 0 2-BEAT** (gốc 4 s) · #2 6 shot/30 s (gốc 13, đạt mục tiêu ≥5).
- **Biên/mềm:** #17 "이천 년" ×11 (số năm sai, lệch 4 tập khác — FIX) · #11 2 lỗi đăng ký nhỏ · #18 SC_274 tableau gò.
- **HƠN kênh gốc:** #6 beat dày nhất 4 tập (1 beat/16 s, gap ≤1:06) · #7 ~35 số · #8 4 bài học địch nói thành lời · #9 14 quyết định/6 người thật · #12 ≥16 quote · #16 6/6 yếu tố riêng (lần đầu có "để 30 vạn đi qua").
- **Đo đếm:** #5 nên ghi 2 số (khối/thuần) từ tập này — cách đếm "khối" của script-writer gộp 72 s địch đi qua trên đầu (P1) và 16 s lính lạc (P3) vào combat.
- Chi tiết + đề xuất: `projects/SALSU_612/logs/qc_ep4_script.md`.

'''
assert marker in txt2
txt2 = txt2.replace(marker, concl + marker)
open(path,'w',encoding='utf-8').write(txt2)
print("ok")
