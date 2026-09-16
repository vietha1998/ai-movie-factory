#!/usr/bin/env python3
"""Đo mật độ đọc TTS trong full_script_epN.md: 어절 (N + thoại) mỗi SC so với ngân sách
(video8s ≤22, still ≤45; toàn tập ≤115 어절/phút). In bảng SC vượt ngưỡng."""
import re, sys, pathlib
def analyze(path, limit_v=22, limit_s=45):
    txt = pathlib.Path(path).read_text()
    scs = re.split(r"\n(?=### SC_\d{3})", txt)
    rows, total_w, total_s, viol = [], 0, 0, []
    for blk in scs:
        m = re.match(r"### (SC_\d{3})[^\n]*?·\s*(video8s|still_kenburns)[^\n]*?·\s*(\d+):(\d+)–(\d+):(\d+)", blk)
        if not m: continue
        sid, typ = m.group(1), m.group(2)
        t1 = int(m.group(3))*60+int(m.group(4)); t2 = int(m.group(5))*60+int(m.group(6)); sec = max(t2-t1, 1)
        words = 0
        for line in blk.splitlines():
            if line.startswith("N:") or re.match(r"^[가-힣A-Za-z_ ]{1,12}:\s", line) and not line.startswith(("[", "#", ">")):
                if line.startswith("[") : continue
                body = line.split(":",1)[1].strip()
                body = re.sub(r"\(.*?\)", "", body)
                if "(tiếp)" in line or body in ("", "(tiếp)"): continue
                words += len(body.split())
        total_w += words; total_s += sec
        lim = limit_v if typ == "video8s" else limit_s
        if sec > 8 and typ == "video8s": lim = int(limit_v * sec / 8)
        if typ == "still_kenburns": lim = int(limit_s * sec / 12) if sec < 12 else limit_s
        if words > lim: viol.append((sid, typ, sec, words, lim))
    wpm = total_w / (total_s/60) if total_s else 0
    return total_w, total_s, wpm, viol
if __name__ == "__main__":
    for p in sys.argv[1:]:
        w, s, wpm, viol = analyze(p)
        print(f"{pathlib.Path(p).name}: {w} 어절 / {s//60}:{s%60:02d} → {wpm:.1f} 어절/phút · vượt ngưỡng: {len(viol)} SC")
        for v in viol[:8]: print("   ", v)
        if len(viol) > 8: print("    ...")
