import re, sys
from collections import Counter
path = sys.argv[1] if len(sys.argv)>1 else "/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep2.md"
txt = open(path, encoding="utf-8").read()
main = txt.split("\n## 부록")[0]
blocks = re.split(r'(?m)^### (SC_\d{3})', main)
scs=[]
part=None
for i in range(1,len(blocks),2):
    sid=blocks[i]; body=blocks[i+1]
    header=body.split('\n',1)[0]
    m=re.search(r'(\d+):(\d+)–(\d+):(\d+)',header)
    t0=int(m.group(1))*60+int(m.group(2)); t1=int(m.group(3))*60+int(m.group(4))
    kind='video' if 'video8s' in header else 'still'
    body_main=body.split('\n[Kết thúc')[0]
    lines=body_main.split('\n')
    narr=[l[2:].strip() for l in lines if l.startswith('N:')]
    dlg=[(l.split(':',1)[0],l.split(':',1)[1].strip()) for l in lines if re.match(r'^[^\[\sN#>][^:]{0,30}:',l) and not l.startswith('N:')]
    action=' '.join(l for l in lines if l.startswith('[ACTION-VI]'))
    combat = '[COMBAT]' in body_main
    scs.append(dict(id=sid,t0=t0,t1=t1,kind=kind,narr=narr,dlg=dlg,action=action,header=header,combat=combat))
# parts
parts=re.findall(r'(?m)^## \[Phần (\d+)\].*?\((\d+):(\d+)–(\d+):(\d+)\)',main)
print("SC total",len(scs),"video",sum(1 for s in scs if s['kind']=='video'),"still",sum(1 for s in scs if s['kind']=='still'))
prev=0;gaps=[]
for s in scs:
    if s['t0']!=prev: gaps.append((s['id'],prev,s['t0']))
    prev=s['t1']
print("gaps",gaps,"end",prev)
bad=[(s['id'],s['t1']-s['t0']) for s in scs if (s['kind']=='video' and s['t1']-s['t0']!=8) or (s['kind']=='still' and not 6<=s['t1']-s['t0']<=12)]
print("bad durations",bad)
print("SC<30s",[s['id'] for s in scs if s['t0']<30],"N<30s",[s['id'] for s in scs if s['t0']<30 and s['narr']])
alld=[(s['id'],w,l) for s in scs for w,l in s['dlg']]
print("dialogue lines",len(alld))
print("dlg>12",[(sid,w,l,len(l.split())) for sid,w,l in alld if len(l.split())>12])
multi=[(s['id'],len(s['dlg'])) for s in scs if len(s['dlg'])>1]
print("SC with >1 dlg",multi)
alln=[(s['id'],l) for s in scs for l in s['narr']]
nw=sum(len(l.split()) for _,l in alln)
nsent=[]
for sid,l in alln:
    for sent in re.split(r'(?<=[.!?])\s+',l):
        if sent.strip(): nsent.append((sid,sent.strip()))
print("N lines",len(alln),"N sentences",len(nsent),"N eojeol",nw)
print("N>15",[(sid,s,len(s.split())) for sid,s in nsent if len(s.split())>15])
print("SC with N",sum(1 for s in scs if s['narr']),"coverage sec",sum(s['t1']-s['t0'] for s in scs if s['narr']))
comb=sum(s['t1']-s['t0'] for s in scs if s['combat'])
print("combat sec",comb,round(comb/2400*100,1),"%")
print("speakers",Counter(w for _,w,_ in alld))
dw=sum(len(l.split()) for _,_,l in alld); print("dlg eojeol",dw)
# per part
import itertools
pstats=[]
for pn,a,b,c,d in parts:
    a0=int(a)*60+int(b); b0=int(c)*60+int(d)
    ss=[s for s in scs if a0<=s['t0']<b0]
    pstats.append((pn,f"{a}:{b}–{c}:{d}",len(ss),sum(1 for s in ss if s['kind']=='video'),sum(1 for s in ss if s['kind']=='still'),sum(s['t1']-s['t0'] for s in ss),sum(len(s['narr']) for s in ss),sum(len(l.split()) for s in ss for l in s['narr']),sum(len(s['dlg']) for s in ss),sum(len(l.split()) for s in ss for _,l in s['dlg']),sum(s['t1']-s['t0'] for s in ss if s['combat'])))
for p in pstats: print(p)
