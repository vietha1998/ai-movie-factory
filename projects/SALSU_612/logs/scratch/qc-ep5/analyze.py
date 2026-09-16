import re, json, collections
p="/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep5.md"
txt=open(p,encoding="utf-8").read()
# stop at appendix
body=txt.split("## 부록")[0]
hdr=re.compile(r"^### (SC_\d+) · (.*?) · (.*?) · (.*?) · (video8s|still_kenburns) · (\d+):(\d+)–(\d+):(\d+)\s*$",re.M)
scs=[]
for m in hdr.finditer(body):
    sid,loc,chars,ids,kind,m1,s1,m2,s2=m.groups()
    t1=int(m1)*60+int(s1); t2=int(m2)*60+int(s2)
    scs.append(dict(id=sid,loc=loc,chars=chars,ids=ids,kind=kind,t1=t1,t2=t2,start=m.end()))
# also END CARD headers
ec=re.findall(r"^### (SC_\d+) · \[END CARD\] · — · — · still_kenburns · (\d+):(\d+)–(\d+):(\d+)",body,re.M)
for sid,m1,s1,m2,s2 in ec:
    scs.append(dict(id=sid,loc="END",chars="",ids="",kind="still_kenburns",t1=int(m1)*60+int(s1),t2=int(m2)*60+int(s2),start=body.find("### "+sid)))
scs.sort(key=lambda x:x["start"])
print("SC count",len(scs), "video",sum(1 for s in scs if s["kind"]=="video8s"),"still",sum(1 for s in scs if s["kind"]=="still_kenburns"))
# continuity
bad=[(scs[i]["id"],scs[i]["t2"],scs[i+1]["t1"]) for i in range(len(scs)-1) if scs[i]["t2"]!=scs[i+1]["t1"]]
print("time gaps",bad)
print("total sec",scs[-1]["t2"])
durs=collections.Counter((s["kind"],s["t2"]-s["t1"]) for s in scs)
print("durations",durs)
# blocks text
for i,s in enumerate(scs):
    end=scs[i+1]["start"] if i+1<len(scs) else len(body)
    s["text"]=body[s["start"]:end]
# narration & dialogue
dlg=[];nar=[]
for s in scs:
    for line in s["text"].splitlines():
        if line.startswith("N:"):
            nar.append((s["id"],line[2:].strip()))
        m=re.match(r"^([^\[\s#>\-][^:]{0,30}):\s(.+)$",line)
        if m and not line.startswith("N:") and not line.startswith("[") :
            name=m.group(1).strip()
            if name.startswith("SC_") or "ACTION" in name or "SOUND" in name: continue
            dlg.append((s["id"],name,m.group(2).strip()))
print("dialogue lines",len(dlg))
spk=collections.Counter(n for _,n,_ in dlg)
print(spk.most_common())
def eojeol(t):
    t=re.sub(r"\(.*?\)","",t)
    return len(t.split())
long=[(i,n,t,eojeol(t)) for i,n,t in dlg if eojeol(t)>12]
print("dialog >12:",long)
mx=max(eojeol(t) for _,_,t in dlg); print("max dialog eojeol",mx)
# narration eojeol total + sentences >15
tot=0;longn=[]
for i,t in nar:
    tot+=len(t.split())
    for sent in re.split(r"(?<=[.?!])\s+",t):
        if len(sent.split())>15: longn.append((i,sent))
print("narration eojeol",tot,"sentences>15",longn)
# narrator before 0:30
print("N before 32s:",[i for i,t in nar if next(s for s in scs if s["id"]==i)["t1"]<32])
# SC with >1 dialogue line
c=collections.Counter(i for i,_,_ in dlg)
print(">1 dlg per SC",[(k,v) for k,v in c.items() if v>1])
# 2-BEAT count
print("2-BEAT",body.count("2-BEAT"))
# keyword checks
for kw in ["신세웅","영양왕","양제","북한","그러나 그들은","VEH_205","께서"]:
    print(kw, [s["id"] for s in scs if kw in s["text"]])
# dialogue lines containing 시호
print("dlg with 영양왕/양제:",[(i,n,t) for i,n,t in dlg if ("영양왕" in t or "양제" in t)])
# enemy POV: SCs with CHAR_2 or 수 / 선비 in chars
en=[s["id"] for s in scs if re.search(r"CHAR_2|수 |선비|탁발흠|우중문|우문술|양제",s["chars"])]
print("enemy POV SCs",len(en))
# LOC counts
print(collections.Counter(s["loc"].split(" ")[0] for s in scs))
json.dump([{k:v for k,v in s.items() if k!="text"} for s in scs],open("/Users/admin/phim han quoc/projects/SALSU_612/logs/scratch/qc-ep5/scs.json","w"),ensure_ascii=False,indent=0)
