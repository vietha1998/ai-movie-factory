import re, sys, json
path = "/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep1.md"
txt = open(path, encoding="utf-8").read()
# split into SC blocks
blocks = re.split(r'(?m)^### (SC_\d{3})', txt)
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
    dlg = [(l.split(':',1)[0], l.split(':',1)[1].strip()) for l in lines if re.match(r'^[^\[\sN][^:]{0,30}:', l) and not l.startswith('[') and not l.startswith('N:')]
    action = ' '.join(l for l in lines if l.startswith('[ACTION-VI]'))
    scs.append(dict(id=sid,t0=t0,t1=t1,kind=kind,loc=loc,chars=chars,props=props,narr=narr,dlg=dlg,action=action,header=header))
print("total SC", len(scs))
# time continuity
prev=0; gaps=[]
for s in scs:
    if s['t0']!=prev: gaps.append((s['id'],prev,s['t0']))
    prev=s['t1']
print("time gaps:", gaps, "end", prev)
# 0-30s
print("SC in 0-30s:", [s['id'] for s in scs if s['t0']<30])
print("N before 30s:", [s['id'] for s in scs if s['t0']<30 and s['narr']])
print("first N:", next((s['id'],s['t0']) for s in scs if s['narr']))
# dialogue stats
alld=[(s['id'],who,l) for s in scs for who,l in s['dlg']]
print("dialogue lines:", len(alld))
long=[(sid,who,l,len(l.split())) for sid,who,l in alld if len(l.split())>12]
print("dlg >12 eojeol:", long)
alln=[(s['id'],l) for s in scs for l in s['narr']]
# split narration into sentences
nsent=[]
for sid,l in alln:
    for sent in re.split(r'(?<=[.!?])\s+', l):
        if sent.strip(): nsent.append((sid,sent.strip()))
print("narr sentences:", len(nsent), "words:", sum(len(l.split()) for _,l in alln))
print("narr >15:", [(sid,s,len(s.split())) for sid,s in nsent if len(s.split())>15])
# dialogue w/ number
numre=re.compile(r'[0-9]|하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|열|스물|서른|마흔|쉰|백|천|만|이틀|사흘|나흘|하루|퍼센트|킬로|미터|리터|분\b|발\b|개\b|명\b|치\b')
numd=[(sid,who,l) for sid,who,l in alld if numre.search(l)]
print("dlg with number:", len(numd))
for x in numd: print("  ",x)
# enemy POV
enemy=[s['id'] for s in scs if re.search(r'CHAR_20\d|LOC_004', s['header']) or '탁발흠' in s['chars'] or '선봉장' in s['chars'] or '양제' in s['chars']]
print("enemy POV SC:", len(enemy), enemy)
# combat seconds: define by keyword in action
combatkw=re.compile(r'bắn|nổ|tracer|cối|40mm|K3|K6|tên rít|tên cắm|mũi tên bay|đuốc|kỵ .*xông|giáo|chém|cháy|lao|đâm|cung .*giương|thả|xung|tản ra|lửa')
combat=[s for s in scs if combatkw.search(s['action']) and s['t0']>=420]
# manual ranges instead
ranges=[(7*60+18,8*60+8),(11*60+42,13*60+34),(23*60+2,23*60+18),(27*60+30,34*60+12)]
tot=sum(b-a for a,b in ranges); print("combat sec (manual ranges):", tot, tot/2400)
# per speaker count
from collections import Counter
c=Counter(who for _,who,_ in alld); print(c)
# avg shot
print("avg shot:", 2400/len(scs))
# still durations
print("still durations:", Counter(s['t1']-s['t0'] for s in scs if s['kind']=='still'))
print("video durations:", Counter(s['t1']-s['t0'] for s in scs if s['kind']=='video'))
# consecutive talking-head SCs: video SCs with dialogue and no movement keywords
talk=re.compile(r'đứng|ngồi|quỳ|cận|Cận')
move=re.compile(r'chạy|lao|bắn|phi|nổ|lội|kéo|leo|đi |bước|xuống|lên |ném|rút|mở|đóng|quay|tracking|Tracking|aerial|Aerial|wide|Wide')
run=[];cur=[]
for s in scs:
    if s['dlg'] and not move.search(s['action']):
        cur.append(s['id'])
    else:
        if len(cur)>=3: run.append(cur)
        cur=[]
if len(cur)>=3: run.append(cur)
print("talking runs >=3:", run)
# multi-location SC
print("multi-loc SC:", [s['id'] for s in scs if '→' in s['loc']])
# SC with >2 speakers
print(">1 dlg per SC:", [s['id'] for s in scs if len(s['dlg'])>1])
json.dump(scs, open("/Users/admin/phim han quoc/projects/SALSU_612/logs/scratch/qc-reviewer/scs.json","w"), ensure_ascii=False, indent=0)
