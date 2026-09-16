import re, json
from collections import Counter
path = "/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep4.md"
txt = open(path, encoding="utf-8").read()
main = txt.split('\n## 부록')[0]
blocks = re.split(r'(?m)^### (SC_\d{3})', main)
scs = []
for i in range(1, len(blocks), 2):
    sid = blocks[i]; body = blocks[i+1]
    header = body.split('\n',1)[0]
    m = re.search(r'(\d+):(\d+)–(\d+):(\d+)', header)
    t0 = int(m.group(1))*60+int(m.group(2)); t1 = int(m.group(3))*60+int(m.group(4))
    kind = 'video' if 'video8s' in header else 'still'
    parts = header.split(' · ')
    loc = parts[1].strip() if len(parts)>1 else ''
    chars = parts[2].strip() if len(parts)>2 else ''
    props = parts[3].strip() if len(parts)>3 else ''
    body_main = body.split('\n[Kết thúc')[0].split('\n## [Phần')[0]
    lines = body_main.split('\n')
    narr = [l[2:].strip() for l in lines if l.startswith('N:')]
    dlg = [(l.split(':',1)[0], l.split(':',1)[1].strip()) for l in lines if re.match(r'^[^\[\sN#>][^:]{0,30}:', l) and not l.startswith('[') and not l.startswith('N:')]
    action = ' '.join(l for l in lines if l.startswith('[ACTION-VI]'))
    scs.append(dict(id=sid,t0=t0,t1=t1,kind=kind,loc=loc,chars=chars,props=props,narr=narr,dlg=dlg,action=action,header=header))
print("total SC", len(scs), "video", sum(1 for s in scs if s['kind']=='video'), "still", sum(1 for s in scs if s['kind']=='still'))
prev=0; gaps=[]
for s in scs:
    if s['t0']!=prev: gaps.append((s['id'],prev,s['t0']))
    prev=s['t1']
print("time gaps:", gaps, "end", prev)
print("SC in 0-30s:", [s['id'] for s in scs if s['t0']<30])
print("N before 30s:", [s['id'] for s in scs if s['t0']<30 and s['narr']])
print("first N:", next((s['id'],s['t0']) for s in scs if s['narr']))
alld=[(s['id'],who,l) for s in scs for who,l in s['dlg']]
print("dialogue lines:", len(alld))
long=[(sid,who,l,len(l.split())) for sid,who,l in alld if len(l.split())>12]
print("dlg >12 eojeol:", long)
print("dlg max:", max(len(l.split()) for _,_,l in alld))
multi=[(s['id'],len(s['dlg'])) for s in scs if len(s['dlg'])>1]
print("SC with >1 dlg:", multi)
alln=[(s['id'],l) for s in scs for l in s['narr']]
nsent=[]
for sid,l in alln:
    for sent in re.split(r'(?<=[.!?])\s+', l):
        if sent.strip(): nsent.append((sid,sent.strip()))
print("narr lines:", len(alln), "sentences:", len(nsent), "eojeol:", sum(len(l.split()) for _,l in alln))
print("narr >15:", [(sid,s,len(s.split())) for sid,s in nsent if len(s.split())>15])
print("dlg eojeol total:", sum(len(l.split()) for _,_,l in alld))
numre=re.compile(r'[0-9]|하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|열|스물|서른|마흔|쉰|백|천|만|이틀|사흘|나흘|하루|퍼센트|킬로|미터|리터|분\b|발\b|개\b|명\b|치\b|뼘')
numd=[(sid,who,l) for sid,who,l in alld if numre.search(l)]
print("dlg with number:", len(numd))
for x in numd: print("  ",x)
enemy=[s['id'] for s in scs if re.search(r'CHAR_20\d', s['header']) or re.search(r'탁발흠|선비|수 |Tùy|우중문|내호아|lính Tùy|4만|전령|주법상|cung thủ Tùy|통역', s['chars'])]
print("enemy POV SC:", len(enemy))
c=Counter(who for _,who,_ in alld); print(c)
print("avg shot:", 2400/len(scs))
print("still durations:", Counter(s['t1']-s['t0'] for s in scs if s['kind']=='still'))
print("video durations:", Counter(s['t1']-s['t0'] for s in scs if s['kind']=='video'))
# talking runs: consecutive video SC with dialogue whose action has no movement keyword
move=re.compile(r'chạy|lao|bắn|phi|nổ|lội|kéo|leo|đi |bước|xuống|lên |ném|rút|mở|đóng|quay|tracking|Tracking|aerial|Aerial|wide|Wide|walk|đứng dậy|trèo|bò ')
run=[];cur=[]
for s in scs:
    if s['dlg'] and not move.search(s['action']):
        cur.append(s['id'])
    else:
        if len(cur)>=3: run.append(cur)
        cur=[]
if len(cur)>=3: run.append(cur)
print("talking runs >=3:", run)
# locate per part
parts=re.findall(r'(?m)^## \[Phần (\d+)\].*?\((\d+):(\d+)–(\d+):(\d+)\)', main)
print(parts)
# 2-BEAT usage
print("2-BEAT SC:", [s['id'] for s in scs if '2-BEAT' in s['action']])
# 시호 check in dialogue
print("시호 in dlg:", [(sid,who,l) for sid,who,l in alld if re.search(r'영양왕|양제', l)])
# 해모루 radio use
print("radio lines:", [(sid,who,l) for sid,who,l in alld if '여기는' in l])
json.dump(scs, open("/Users/admin/phim han quoc/projects/SALSU_612/logs/scratch/qc-ep4/scs.json","w",encoding="utf-8"), ensure_ascii=False, indent=0)
