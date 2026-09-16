#!/usr/bin/env python3
"""Đồng bộ narration_ko / dialogue_ko trong 04_veo/scenes_epN.json từ full_script_epN.md (nguồn sự thật).
Dùng sau mỗi lần sửa chữ kịch bản mà không đổi SC. Cũng cập nhật scene_list_epN.md (dòng NARRATION/DIALOGUE).
Usage: python3 tools/sync_narration.py projects/SALSU_612 1
"""
import re, sys, json, pathlib
proj, ep = pathlib.Path(sys.argv[1]), sys.argv[2]
script = (proj/"02_script"/f"full_script_ep{ep}.md").read_text()
def parse(txt):
    out = {}
    for blk in re.split(r"\n(?=### SC_\d{3})", txt):
        m = re.match(r"### (SC_\d{3})", blk)
        if not m: continue
        N, D = [], []
        for line in blk.splitlines():
            if line.startswith("N:"):
                N.append(line[2:].strip())
            elif re.match(r"^[가-힣A-Za-z_ ()·0-9]{1,20}:\s", line) and not line.startswith(("[", "#", ">", "N:")):
                D.append(line.strip())
        out[m.group(1)] = (" ".join(N).strip(), "\n".join(D).strip())
    return out
sc = parse(script)
jp = proj/"04_veo"/f"scenes_ep{ep}.json"
changed = 0
if jp.exists():
    data = json.loads(jp.read_text())
    for rec in data:
        n, d = sc.get(rec["id"], (None, None))
        if n is None: continue
        if rec.get("narration_ko","") != n or rec.get("dialogue_ko","") != d:
            rec["narration_ko"], rec["dialogue_ko"] = n, d; changed += 1
    jp.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    print(f"scenes_ep{ep}.json: {changed} SC cập nhật")
lp = proj/"04_veo"/f"scene_list_ep{ep}.md"
if lp.exists():
    txt = lp.read_text(); c2 = 0
    def repl(m):
        global c2
        sid = m.group(1); n, d = sc.get(sid, (None, None))
        body = m.group(0)
        if n is None: return body
        new = re.sub(r"(NARRATION \(KO\):)[^\n]*", lambda x: x.group(1)+" "+n, body)
        new = re.sub(r"(DIALOGUE \(KO\):)[^\n]*", lambda x: x.group(1)+" "+d.replace("\n"," / "), new)
        if new != body: c2 += 1
        return new
    txt = re.sub(r"### (SC_\d{3}).*?(?=\n### SC_|\Z)", repl, txt, flags=re.S)
    lp.write_text(txt); (pathlib.Path("output")/f"ep{ep}"/"kich_ban"/"scene_list.md").write_text(txt)
    print(f"scene_list_ep{ep}.md: {c2} SC cập nhật (+ output copy)")
