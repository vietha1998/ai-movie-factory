import re, sys, collections
p = "/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep2.md"
txt = open(p, encoding="utf-8").read()
# cut appendix
body = txt.split("## 부록")[0]
sc_re = re.compile(r"^### (SC_\d+) · (.+?) · (.+?) · (.+?) · (video8s|still_kenburns) · (\d+):(\d+)–(\d+):(\d+)\s*$", re.M)
scs = []
for m in sc_re.finditer(body):
    sid, loc, chars, vehs, kind, m1, s1, m2, s2 = m.groups()
    t1 = int(m1)*60+int(s1); t2 = int(m2)*60+int(s2)
    scs.append(dict(id=sid, loc=loc, chars=chars, vehs=vehs, kind=kind, t1=t1, t2=t2, start=m.start()))
# attach bodies
for i, s in enumerate(scs):
    end = scs[i+1]["start"] if i+1 < len(scs) else len(body)
    s["body"] = body[s["start"]:end]
print("SC:", len(scs), "video:", sum(1 for s in scs if s["kind"]=="video8s"), "still:", sum(1 for s in scs if s["kind"]=="still_kenburns"))
print("total sec:", sum(s["t2"]-s["t1"] for s in scs), "last t2:", scs[-1]["t2"])
# durations check
bad = [(s["id"], s["t2"]-s["t1"]) for s in scs if s["kind"]=="video8s" and s["t2"]-s["t1"]!=8]
print("video != 8s:", bad)
# gaps
gaps = [(scs[i]["id"], scs[i+1]["id"]) for i in range(len(scs)-1) if scs[i]["t2"]!=scs[i+1]["t1"]]
print("gaps:", gaps)
# end card handling
# combat
combat = [s for s in scs if "[COMBAT]" in s["body"]]
csec = sum(s["t2"]-s["t1"] for s in combat)
print("combat SC:", len(combat), "sec:", csec, "pct:", round(csec/2400*100,1))
# narration
N_lines = re.findall(r"^N: (.+)$", body, re.M)
n_eojeol = sum(len(l.split()) for l in N_lines)
n_sent = sum(len([x for x in re.split(r"[.?!]\s*", l) if x.strip()]) for l in N_lines)
print("N lines:", len(N_lines), "eojeol:", n_eojeol, "sentences:", n_sent)
long_n = []
for l in N_lines:
    for sent in re.split(r"(?<=[.?!])\s+", l):
        if len(sent.split())>15: long_n.append(sent)
print("N sentences >15 eojeol:", len(long_n), long_n[:5])
# dialogue
D = re.findall(r"^([^\n:\[#>]+?): (.+)$", body, re.M)
D = [(a,b) for a,b in D if a.strip()!="N" and not a.startswith("[")]
print("dialogue lines:", len(D), "eojeol:", sum(len(b.split()) for a,b in D))
long_d = [(a,b,len(b.split())) for a,b in D if len(b.split())>12]
print(">12:", long_d)
cnt = collections.Counter(a.strip() for a,b in D)
print(cnt.most_common())
# SC with >1 dialogue line
for s in scs:
    dl = [l for l in s["body"].splitlines() if re.match(r"^[^\n:\[#>]+?: ", l) and not l.startswith("N:")]
    if len(dl)>1: print("multi-dialogue", s["id"], len(dl))
# first 30s
print("first30:", [(s["id"], s["t1"], s["t2"], "2-BEAT" in s["body"]) for s in scs if s["t1"]<30])
# narrator before 30s
print("N before 30s:", [s["id"] for s in scs if s["t1"]<30 and "\nN:" in s["body"]])
# first N
for s in scs:
    if "\nN:" in s["body"]:
        print("first N at", s["id"], s["t1"]); break
# enemy POV: LOC_004 or CHAR_2xx or Tùy chars
enemy = [s for s in scs if ("LOC_004" in s["loc"]) or re.search(r"CHAR_2\d\d", s["chars"]) or re.search(r"수 공성총관|수 전령|lính Tùy|thợ Tùy|Tiên Ti|nỏ thủ Tùy|tướng Tùy|đại quân Tùy|bộ binh Tùy|lính Tùy đào hầm|통역|선비", s["chars"])]
print("enemy POV SC:", len(enemy))
# per part combat
parts = re.split(r"^## \[Phần (\d+)\]", body, flags=re.M)
# numbers in dialogue
numre = re.compile(r"(\d|하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|열|스물|서른|마흔|쉰|예순|일흔|여든|아흔|백|천|만|킬로|퍼센트|리\b|발|대|병|개|번|일\b|날|주|달|시간|분|미터|걸음)")
nd = [(a,b) for a,b in D if numre.search(b)]
print("dialogue with numbers:", len(nd))
for a,b in nd: print("  ", a, "|", b)
