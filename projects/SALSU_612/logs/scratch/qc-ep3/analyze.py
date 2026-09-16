import re, json, collections
p="/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep3.md"
txt=open(p,encoding="utf-8").read()
# stop at appendix
body=txt.split("## 부록")[0]
hdr=re.compile(r"^### (SC_\d{3})(?: · (.*?))? · (video8s|still_kenburns) · (\d+):(\d\d)–(\d+):(\d\d)",re.M)
scs=[]
for m in hdr.finditer(body):
    sid=m.group(1); kind=m.group(3)
    t1=int(m.group(4))*60+int(m.group(5)); t2=int(m.group(6))*60+int(m.group(7))
    scs.append(dict(id=sid,kind=kind,t1=t1,t2=t2,dur=t2-t1,start=m.start()))
# END CARD header differs
m=re.search(r"^### (SC_287) · \[END CARD\] · — · — · (still_kenburns) · (\d+):(\d\d)–(\d+):(\d\d)",body,re.M)
if m:
    t1=int(m.group(3))*60+int(m.group(4)); t2=int(m.group(5))*60+int(m.group(6))
    scs.append(dict(id="SC_287",kind="still_kenburns",t1=t1,t2=t2,dur=t2-t1,start=m.start()))
seen=set(); scs=[x for x in scs if not (x["id"] in seen or seen.add(x["id"]))]
scs.sort(key=lambda s:s["start"])
print("SC:",len(scs),"video8s:",sum(1 for s in scs if s["kind"]=="video8s"),"still:",sum(1 for s in scs if s["kind"]!="video8s"))
print("total sec:",sum(s["dur"] for s in scs), "first t1",scs[0]["t1"],"last t2",scs[-1]["t2"])
# gaps/overlaps
gaps=[(scs[i]["id"],scs[i+1]["id"],scs[i+1]["t1"]-scs[i]["t2"]) for i in range(len(scs)-1) if scs[i+1]["t1"]!=scs[i]["t2"]]
print("gaps:",gaps)
print("video not 8s:",[(s["id"],s["dur"]) for s in scs if s["kind"]=="video8s" and s["dur"]!=8])
print("still durs:",collections.Counter(s["dur"] for s in scs if s["kind"]!="video8s"))
# per SC text
for i,s in enumerate(scs):
    end=scs[i+1]["start"] if i+1<len(scs) else len(body)
    s["text"]=body[s["start"]:end]
# dialogue & narration
dlg=[];nar=[]
for s in scs:
    for line in s["text"].splitlines():
        if line.startswith("N: "):
            nar.append((s["id"],line[3:].strip()))
        elif re.match(r"^[^\[\]#>\-\s][^:]{0,30}: ",line) and not line.startswith("N:"):
            name,_,t=line.partition(": ")
            dlg.append((s["id"],name.strip(),t.strip()))
print("dialogue lines:",len(dlg))
by=collections.Counter(n for _,n,_ in dlg)
print(by.most_common())
mx=sorted(((len(t.split()),i,n,t) for i,n,t in dlg),reverse=True)[:5]
print("longest dlg:",mx)
print(">12 어절:",[(i,n,t) for i,n,t in dlg if len(t.split())>12])
multi=collections.Counter(i for i,_,_ in dlg)
print("SC with >1 dialogue:",[k for k,v in multi.items() if v>1])
print("N lines:",len(nar),"N 어절:",sum(len(t.split()) for _,t in nar))
sent=[]
for i,t in nar:
    for st in re.split(r"(?<=[.!?…])\s+",t):
        st=st.strip()
        if st: sent.append((i,st))
print("N sentences:",len(sent),">15 어절:",[(i,s) for i,s in sent if len(s.split())>15])
print("dlg 어절:",sum(len(t.split()) for _,_,t in dlg))
# narrator before 0:30
print("first N:",[ (i,t[:30]) for i,t in nar[:2]], "SC t1:",[s["t1"] for s in scs if s["id"]==nar[0][0]])
# SC without N
noN=[s["id"] for s in scs if not any(i==s["id"] for i,_ in nar)]
print("SC without N:",len(noN),noN)
# combat classification (QC's own list: pure = fire/attack/chase physically on screen)
pure=set("""SC_003 SC_004 SC_010 SC_020 SC_021 SC_022 SC_044 SC_067 SC_068 SC_069 SC_070 SC_071 SC_083 SC_084 SC_085 SC_086 SC_087 SC_088 SC_089 SC_090 SC_091 SC_092 SC_115 SC_116 SC_137 SC_138 SC_139 SC_152 SC_153 SC_187""".split())
for n in range(207,242): pure.add(f"SC_{n:03d}")
block=set(pure)|set("SC_007 SC_066 SC_082 SC_093 SC_094 SC_117 SC_154 SC_188".split())
for n in range(198,250): block.add(f"SC_{n:03d}")
ps=sum(s["dur"] for s in scs if s["id"] in pure); bs=sum(s["dur"] for s in scs if s["id"] in block)
print("combat pure s:",ps,round(ps/2400*100,1),"%  block s:",bs,round(bs/2400*100,1),"%")
# longest gap between pure-combat SCs
pc=[s for s in scs if s["id"] in pure]
g=max(((pc[i+1]["t1"]-pc[i]["t2"]),pc[i]["id"],pc[i+1]["id"]) for i in range(len(pc)-1))
print("max gap pure combat:",g, "before first:",pc[0]["t1"],"after last:",2400-pc[-1]["t2"])
# number counts in dialogue
numre=re.compile(r"\d|백|천|만|십|열|스물|서른|마흔|쉰|예순|일곱|여덟|아홉|하나|둘|셋|넷|다섯|여섯|한 |두 |세 |네 |닷새|이틀|사흘|나흘|킬로|미터|분|퍼센트|%|발|개|명|기 |섬|리 ")
nd=[(i,n,t) for i,n,t in dlg if numre.search(t)]
print("dialogue with numbers:",len(nd))
for x in nd: print("  ",x)
# enemy POV SCs: CHAR_2xx or 수 / 선비 in header line
epov=[s["id"] for s in scs if re.search(r"CHAR_20\d|수 |선비|kỵ Tiên Ti|kỵ Tùy|유사룡|우중문|우문술|탁발흠",(s["text"].splitlines() or [""])[0])]
print("enemy POV SC count:",len(epov))
# tense check: N sentences ending in present
pres=[(i,s) for i,s in sent if re.search(r"(습니다|입니다)\.?$",s) and not re.search(r"(었|았|였|겠)습니다\.?$",s)]
print("N present-tense sentences:",len(pres))
for x in pres: print("  ",x)
json.dump(dict(scs=[{k:v for k,v in s.items() if k!='text'} for s in scs]),open("/Users/admin/phim han quoc/projects/SALSU_612/logs/scratch/qc-ep3/scs.json","w"),ensure_ascii=False,indent=0)
