import re,sys,collections
p='02_script/full_script_ep5.md'
txt=open(p,encoding='utf-8').read()
lines=txt.split('\n')
# parse parts and SCs
part=None; scs=[]; cur=None
part_re=re.compile(r'^## \[Phần (\d+)\]')
sc_re=re.compile(r'^### (SC_(\d+)) · (.*?) · (video8s|still_kenburns) · (\d+):(\d+)–(\d+):(\d+)\s*$')
for ln in lines:
    m=part_re.match(ln)
    if m: part=int(m.group(1)); continue
    m=sc_re.match(ln)
    if m:
        t1=int(m.group(5))*60+int(m.group(6)); t2=int(m.group(7))*60+int(m.group(8))
        cur={'id':m.group(1),'num':int(m.group(2)),'part':part,'type':m.group(4),'t1':t1,'t2':t2,'dur':t2-t1,'N':[],'D':[],'hdr':m.group(3)}
        scs.append(cur); continue
    if ln.startswith('### SC_'):
        print('UNPARSED SC HEADER:',ln)
    if cur is None: continue
    if ln.startswith('N:'):
        cur['N'].append(ln[2:].strip())
    elif re.match(r'^[가-힣A-Za-z0-9 ]+: ',ln) and not ln.startswith('[') :
        cur['D'].append(ln)
# checks
errs=[]
prev=None
for s in scs:
    if prev and s['t1']!=prev['t2']: errs.append(f"gap {prev['id']} {prev['t2']} -> {s['id']} {s['t1']}")
    if s['type']=='video8s' and s['dur']!=8: errs.append(f"{s['id']} video dur {s['dur']}")
    if s['type']=='still_kenburns' and not (6<=s['dur']<=12): errs.append(f"{s['id']} still dur {s['dur']}")
    if len(s['D'])>1: errs.append(f"{s['id']} has {len(s['D'])} dialogue lines")
    prev=s
nums=[s['num'] for s in scs]
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]+1: errs.append(f"numbering jump {nums[i-1]}->{nums[i]}")
def eojeol(t): return len(t.split())
# narration sentences
def sentences(t):
    t=re.sub(r'\([^)]*\)','',t)
    return [x.strip() for x in re.split(r'(?<=[.?!])\s+',t) if x.strip()]
nviol=[]; dviol=[]
per=collections.defaultdict(lambda: dict(sc=0,v=0,s=0,sec=0,nl=0,nw=0,ns=0,dl=0,dw=0))
speakers=collections.Counter()
for s in scs:
    P=per[s['part']]; P['sc']+=1; P['sec']+=s['dur']
    if s['type']=='video8s': P['v']+=1
    else: P['s']+=1
    for n in s['N']:
        P['nl']+=1; P['nw']+=eojeol(n)
        for st in sentences(n):
            P['ns']+=1
            if eojeol(st)>15: nviol.append((s['id'],eojeol(st),st))
    for d in s['D']:
        sp,_,body=d.partition(': ')
        body2=re.sub(r'\([^)]*\)','',body).strip()
        P['dl']+=1; P['dw']+=eojeol(body2); speakers[sp.strip()]+=1
        if eojeol(body2)>12: dviol.append((s['id'],eojeol(body2),body2))
tot=dict(sc=0,v=0,s=0,sec=0,nl=0,nw=0,ns=0,dl=0,dw=0)
print("| Phần | SC | video | still | Giây | Dòng N | Câu N | 어절 N | Câu thoại | 어절 thoại |")
for k in sorted(per):
    P=per[k]
    for kk in tot: tot[kk]+=P[kk]
    print(f"| {k} | {P['sc']} | {P['v']} | {P['s']} | {P['sec']} | {P['nl']} | {P['ns']} | {P['nw']} | {P['dl']} | {P['dw']} |")
print(f"| Tổng | {tot['sc']} | {tot['v']} | {tot['s']} | {tot['sec']} | {tot['nl']} | {tot['ns']} | {tot['nw']} | {tot['dl']} | {tot['dw']} |")
print("ERRORS:",len(errs)); [print(' ',e) for e in errs]
print("N >15:",len(nviol)); [print(' ',v) for v in nviol]
print("D >12:",len(dviol)); [print(' ',v) for v in dviol]
print("Speakers:",speakers.most_common())
# narration silence check 0-30s
for s in scs:
    if s['t1']<32 and s['N']: print("N in first 30s:",s['id'])
# combat ranges
combat_ranges=[(17,18),(46,47),(69,71),(76,100),(114,114),(121,122),(127,147),(169,169),(190,190),(200,250)]
cs=0
for a,b in combat_ranges:
    for s in scs:
        if a<=s['num']<=b: cs+=s['dur']
print("combat sec",cs, f"{cs/tot['sec']*100:.1f}%")
# 2-BEAT counts
print("2-BEAT:",txt.count('2-BEAT'))
