import re,io,sys
p="/Users/admin/phim han quoc/docs/benchmark_vs_reference.md"
s=open(p,encoding="utf-8").read()
if "Tập 5" in s.split("\n")[5] or "| Tập 5" in s:
    print("Tập 5 already present — abort"); sys.exit(1)
T5={
"h":"Tập 5 (script v1 · qc 2026-09-16 · đếm thật từ file)",
1:"**0:03** (SC_001 chân lính Tùy đầu tiên xuống bãi cạn — nguy cơ không giải thích; 0:20 \"여섯\") ✅",
2:"**6** (SC_001 2-BEAT · 002 · 003 2-BEAT · 004) ✅ ≥5 · ❌ gốc 13 → 2-BEAT thêm SC_002/004 = 8 (qc §3 #8)",
3:"**0** — narrator vào 0:32 \"612년 7월. 살수.\" ✅",
4:"Nguy cơ **0:03** · sử (kỵ Goguryeo cắn 방진) **2:18** (SC_017) · đại đội bóp cò **10:46** (SC_078, viên K2 #1) ✅ sử · ⚠️ đại đội >10' — cố ý theo kế \"nửa\" (tập thứ 2 liên tiếp sau 4화 19:07)",
5:"**872 s = 36,3 %** (9 khối: P2/P3 [史] mini · P4 · P5 200 s · P6 · P7 168 s · P8/P9 mini · P10 408 s liên tục) ✅ ≥35 % · ❌ gốc 45 %. Không action dài nhất trong thân 3:50 (2:34→6:24); aftermath 34:30→40:00 5:30 (P-47 → đổi SC_252 thành video truy kích 압록 [史])",
6:"Mọi beat: **0:26** · ~170 beat/40' (1/14 s) ✅ hơn gốc (2–3'). Vùng mềm: 37:30–38:00 ba still sử liên tiếp",
7:"**≥32 câu thoại có số** (잔탄 여섯 · 15 % · bảng P3 11 mục · 권총 열다섯 · 여섯…하나 · 다 썼습니다 · 탄 없음 · 이천 · 십 퍼센트 · 백오십 · 오 퍼센트 · 이십 킬로/삼백 미터 · 오십오 톤 · 탄창 둘 · 십 년 · K3 탄 떨어졌습니다 · 탄창 비었습니다 · 붕대 마지막 · 여든 명 · 영) + N (2천 7백 · 450리 · 열넷 · 스물두 발) ✅ HƠN xa. ⚠️ 2 số thiếu nguồn: radio 40→15 % (SC_010), K2 \"20 km\" sau 3 km di chuyển (SC_057 — FIX★)",
8:"**88 SC có địch trong khung / ~45 SC enemy POV có tên** (탁발흠 17 · 우문술/우중문/후군 ~20 · 양제 7). 탁발흠 nói 3 bài học (SC_061 \"천둥은 셀 수 있다\" · SC_100 \"조용하다\" · SC_127 \"벙어리\") + áp dụng 4 (vết xích, tai ngựa, không xông thẳng, chọn xe thay trận) → chết vì bài học cuối ✅ HƠN. ❌ BLOCK ID: VEH_205 (cầu phao) gắn cho kỵ Tùy 21 SC",
9:"**14 quyết định / 5 người thật:** 을지문덕 ×6 (SC_020 mốc cờ · 066 cờ · 076 나각 · 111 không chia quân · 185 전군 · 263–264 bát nước) · 우문술 ×5 (015 · 094 quay lại · 113 뚫어라 · 214 tìm đường · 239 가게 두어라) · 우중문 ×1 (016/063 cờ giữa sông) · 영양왕 ×1 (279 hoãn) · 양제 ×1 (271 내년) ✅ HƠN xa. ⚠️ 나각 3 hồi (cò của SC_185) chưa có SC trả (FIX)",
10:"**139** (박기철 29 · 오태민 15 · 해모루 13 · 한승우 11 · 태오 10 · 우문술 8 · 을지문덕 6 · 을보 6 · 사수 6 · 우중문/아리/탁발흠/서아 4 · 후군 장수 3 · 백성민 3 · 양제/영양왕 2 · 고건무 1 · phụ 8) ≈ hiện đại 59 % / Goguryeo 24 % / Tùy 17 % ✅",
11:"**0**/139 (dài nhất 11 어절) ✅. Đăng ký: ❌ \"총\" trong miệng Goguryeo ×2 (SC_182/276 — series dùng \"쇠\"); \"짐은 버려라\" đa nghĩa (SC_015); 시호 0 vi phạm",
12:"**≥14**: \"여섯…하나. 다 썼습니다\" · \"쇠수레가 벙어리가 됐다. 지금이다\" · \"전차를 여울에 박는다. 마개는 우리다\" · \"오십오 톤입니다\" · \"제가 몹니다. 십 년 몰았습니다\" · \"탄창 비었습니다\" · \"그대들이 마개였소\" · \"족함을 알라 했소. 물 한 그릇이 족함이오\" · \"…고구려 손에 있습니다. 살아서\" · \"…내년\" · \"내년에 또 올 것이오\" · \"이제 우리는 뭡니까\" · \"영입니다. 전부 영\" · \"다녀오십시오\" ✅ HƠN",
13:"**8,3 s** (2.400/289); P10 8,1 s danh nghĩa, **~7,0 s hiệu dụng** (10 SC 2-BEAT) ✅ khung · ❌ gốc 4 s → veo two-beat thêm ~12 clip Phase 1–3 (qc §3 #10)",
14:"12/12 open loop đúng câu outline; series 2 「613」 3 dây: K21+drone về 낙양 (SC_270/286/287) · 뇌군 thuộc về ai (276–280) · \"내년\" ×3; end card 「다음: 613」 ✅",
15:"**4** đúng 7:00 · 14:00 · 21:00 · 27:30, mỗi điểm sau open loop + 1 SC không thoại (SC_050/102/153/200); không mid-roll 5 (P-46) ✅",
16:"6/6: hậu cần (박기철 đếm 8 lần, sổ SC_036/282, \"영입니다\") · bỏ xe (K2 chôn ở cổng họng) · \"5만 đi qua mũi súng\" (SC_053) · địch có tên chết trên xe · tổ tiên là bộ não (을지문덕 ×6) · người Hàn dẫn tổ tiên qua sông (SC_230) · 경례 (SC_262) ✅",
17:"**0 lỗi cứng** ([史] 30만 5천 · nửa quân qua sông · 신세웅 · 450리 일주야 · 2.700 · 왕인공 · 내호아 rút · xiềng tướng · rút cuối 7월 · 613 양현감 · 614 · 618 우문화급 · 知足願云止; điểm rẽ 우중문 bị bắt sống được narrator nói rõ SC_263). **Mềm ×2:** \"우중문 옥에서 죽었습니다\" (sử: thả khi bệnh, chết ở nhà — SC_263) · \"113만이 요하를 건너 돌아갔습니다\" (SC_273). 시호 0. Địa lý đúng trình tự",
18:"KHÔNG giống trình tự cấm: chờ → đếm cuối → 5만 qua mũi súng → cờ đỏ → 6 con số → chính trị giữa trận → kỵ xông được vào súng máy → hết đạn → chôn xe → kẻ săn chết trên xe bởi tên → 2.700 → 경례 → 양제 chạm K21 → điện 평양 → \"뭡니까\" → xe bò. ⚠️ Hai beat §17 (địch thề \"내년\" / \"내년에 또 올 것이오\") có mặt nhưng đảo thứ tự, trong điện, kết bằng xe bò công nghệ → không tableau ✅",
}
lines=s.split("\n")
out=[];row=0
for ln in lines:
    if ln.startswith("| # | Chỉ số |"):
        cells=ln.split("|"); cells.insert(len(cells)-2," "+T5["h"]+" "); ln="|".join(cells)
    elif ln.startswith("|---|---|") and row==0:
        cells=ln.split("|"); cells.insert(len(cells)-2,"---"); ln="|".join(cells); row=1
    else:
        m=re.match(r"^\| (\d{1,2}) \| ",ln)
        if m and 1<=int(m.group(1))<=18 and row==1:
            n=int(m.group(1)); cells=ln.split("|"); cells.insert(len(cells)-2," "+T5[n]+" "); ln="|".join(cells)
    out.append(ln)
s2="\n".join(out)
concl='''### Kết luận chấm Tập 5 (script v1 · qc-reviewer 2026-09-16 · đếm thật từ file)
- **THUA kênh gốc:** #2 shot 30 s đầu **6** (gốc 13; đạt ≥5) · #13 shot trong trận **~7 s hiệu dụng** (gốc 4 s) · #5 combat **36,3 %** (đạt ≥35 %, gốc 45 %) · #4 đại đội bóp cò **10:46** (gốc ≤1:36 — cố ý theo kế "nửa"; tập thứ 2 liên tiếp đại đội im >10').
- **BLOCK/FIX ảnh hưởng chỉ số:** #8 **BLOCK** VEH_205 (cầu phao) gắn cho kỵ Tùy 21 SC · #9 나각 3 hồi (cò của 을지문덕 SC_185) không có SC trả · #7 hai số thiếu nguồn (radio 40→15 %; K2 "20 km" sau 3 km) · #11 "총" ×2 trong miệng Goguryeo · #17 hai câu sử mềm · vết thương 해모루 trái decisions P-38 (giáo sườn ↔ tên dưới xương đòn trái) · 신세웅 trái P-44 (3 thoại + 5 N gọi tên) · đồng hồ nước/ngày lệch 4화 (이레/사흘/보름 vs D12).
- **HƠN kênh gốc / hơn 1–4화:** #6 gap mọi beat **0:26** (~170 beat) · #7 ≥32 câu số · #8 3 bài học + 4 áp dụng của 탁발흠 · #9 **14 quyết định/5 người thật** · #12 ≥14 quote · #14 series 2 đủ 3 dây · #16 6/6 + 경례.
- **Kiểm đặc biệt:** 6 phase P10 — **không có "sai sót" thật** (Phase 3 là biến cố; sửa 1 câu N → sai lầm "sống người trước lửa" của 한승우, qc §3 #1) · narrator im 10:38–12:30 và 31:30–33:22 (112 s ×2) ✅ · kết không phải tableau §17 ✅ · K5 15 viên ✅ · nhiệt nhôm ✅ (N SC_225 "삼천 도" = narrator giải thích công nghệ + sai số → FIX) · biển 천둥 3 lên xác K2 ✅.
- **Nối tiếp 4화 v1:** đúng K2 6 · cối 30 · PZF 6 · morphine 8 · 91명 · 태오 mũ trụ · 탁발흠 kính đêm (vỡ) · 30만 quay về ✓; **lệch:** nước (4화 kết 허리, 5화 SC_044 "사흘 전 무릎") · K2 vị trí (4화 đảo lau 2 cách 3 km vs 5화 "간밤에 삼백 미터") · radio 40→15 % · 탁발흠 cẳng tay trái băng (4화) không hiện · 천둥 3 "마흔 날" (thực ~20 ngày, đã tới 육합성 từ 4화 D3).
- Chi tiết + đề xuất: `projects/SALSU_612/logs/qc_ep5_script.md`.

'''
marker='## "Hay hơn kênh gốc" — 5 đòn bẩy cố định'
assert marker in s2
s2=s2.replace(marker,concl+marker,1)
open(p,"w",encoding="utf-8").write(s2)
print("patched; header now:",s2.split("\n")[5][:200])
