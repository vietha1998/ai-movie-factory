import re,sys,collections
p=sys.argv[1]
txt=open(p,encoding='utf-8').read()
# split parts
parts=re.split(r'\n## \[Phần (\d+)\]',txt)
# parts[0]=header, then (num, body) pairs
def tsec(t):
    m,s=t.split(':'); return int(m)*60+int(s)
sc_re=re.compile(r'^### (SC_\d+) · (.+?) · (.+?) · (.+?) · (video8s|still_kenburns) · (\d+:\d+)–(\d+:\d+)\s*$',re.M)
allsc=[]
rows=[]
prev_end=0
issues=[]
combat_ranges={ # SC numbers counted as combat/contact
 1:range(1,10),2:range(13,16),3:range(39,41),4:list(range(53,54))+list(range(62,75)),5:range(76,93),6:range(116,118),7:range(130,148),8:range(162,163),9:list(range(181,182))+list(range(189,190)),10:range(207,246),11:range(260,262),12:range(272,273)}
combat_set=set()
for k,v in combat_ranges.items(): combat_set.update(v)
totN_words=0; totD=0; totD_words=0; totNlines=0; totN_sent=0
viol_N=[]; viol_D=[]
combat_total=0
for i in range(1,len(parts),2):
    pn=int(parts[i]); body=parts[i+1]
    scs=list(sc_re.finditer(body))
    n_sc=len(scs); nv=sum(1 for m in scs if m.group(5)=='video8s'); ns=n_sc-nv
    secs=0; combat=0
    for j,m in enumerate(scs):
        t1,t2=tsec(m.group(6)),tsec(m.group(7)); d=t2-t1; secs+=d
        num=int(m.group(1)[3:])
        if t1!=prev_end: issues.append(f'{m.group(1)}: t1 {m.group(6)} != prev end {prev_end//60}:{prev_end%60:02d}')
        prev_end=t2
        if m.group(5)=='video8s' and d!=8: issues.append(f'{m.group(1)}: video {d}s')
        if m.group(5)=='still_kenburns' and not (6<=d<=12): issues.append(f'{m.group(1)}: still {d}s')
        if num in combat_set: combat+=d
        # body of SC
        start=m.end(); end=scs[j+1].start() if j+1<len(scs) else len(body)
        sb=body[start:end]
        Ns=re.findall(r'^N: (.+)$',sb,re.M)
        Ds=re.findall(r'^([가-힣A-Za-z ()의를]+?): (.+)$',sb,re.M)
        Ds=[(a,b) for a,b in Ds if a!='N']
        nlines=len(Ns)
        if nlines>1: issues.append(f'{m.group(1)}: {nlines} N lines')
        for n in Ns:
            totN_words+=len(n.split())
            for sent in re.split(r'(?<=[.!?])\s+',n.strip()):
                if not sent: continue
                totN_sent+=1
                w=len(sent.split())
                if w>15: viol_N.append((m.group(1),w,sent))
        totNlines+=nlines
        if len(Ds)>2: issues.append(f'{m.group(1)}: {len(Ds)} dialogue lines')
        for a,b in Ds:
            totD+=1; w=len(b.split()); totD_words+=w
            if w>12: viol_D.append((m.group(1),a,w,b))
        allsc.append((pn,m.group(1),m.group(5),d,nlines,len(Ds)))
    combat_total+=combat
    rows.append((pn,n_sc,nv,ns,secs,combat))
print("| Phần | SC | video8s | still | Giây | Combat s |")
for r in rows: print("| %d | %d | %d | %d | %d | %d |"%r)
T=[sum(r[k] for r in rows) for k in range(1,6)]
print("TOTAL SC %d video %d still %d secs %d combat %d (%.1f%%)"%(T[0],T[1],T[2],T[3],T[4],100*T[4]/T[3]))
print("N lines",totNlines,"N sentences",totN_sent,"N 어절",totN_words)
print("Dialogue lines",totD,"어절",totD_words)
print("viol N >15:",len(viol_N)); [print(v) for v in viol_N]
print("viol D >12:",len(viol_D)); [print(v) for v in viol_D]
print("issues:",len(issues)); [print(i) for i in issues]
# per-part N words & dialogue
per=collections.defaultdict(lambda:[0,0,0,0])
for i in range(1,len(parts),2):
    pn=int(parts[i]); body=parts[i+1]
    Ns=re.findall(r'^N: (.+)$',body,re.M); Ds=[l for l in re.findall(r'^([가-힣A-Za-z ()의를]+?): (.+)$',body,re.M) if l[0]!='N']
    per[pn]=[len(Ns),sum(len(n.split()) for n in Ns),len(Ds),sum(len(d[1].split()) for d in Ds)]
print("| Phần | Câu N (dòng) | 어절 N | Câu thoại | 어절 thoại |")
for pn in sorted(per): print("| %d | %d | %d | %d | %d |"%(pn,*per[pn]))
# speakers
spk=collections.Counter()
for i in range(1,len(parts),2):
    for a,b in re.findall(r'^([가-힣A-Za-z ()의를]+?): (.+)$',parts[i+1],re.M):
        if a!='N': spk[a]+=1
print(spk.most_common())
