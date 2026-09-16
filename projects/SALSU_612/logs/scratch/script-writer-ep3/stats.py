import re,sys
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
# cut appendix if exists
if '\n## 부록' in s: s=s[:s.index('\n## 부록')]
parts=re.split(r'\n## \[Phần (\d+)\]',s)
# parts[0]=header, then num, body...
def tosec(t):
    m,se=t.split(':'); return int(m)*60+int(se)
rows=[]; tot={'sc':0,'v':0,'st':0,'sec':0,'n':0,'nw':0,'d':0,'dw':0}
viol=[]; nviol=[]
prev_end=None; gaps=[]
combat_blocks={1:['003','004','007','010'],2:['020','021','022'],3:['044','045'],4:['066','067','068','069','070','071'],5:['083','084','085','086','087','088','089','090','091','092','093','094'],6:['109','115','116','117'],7:['137','138','139'],8:['152','153','154'],9:['187','188','189'],10:['%03d'%i for i in range(198,250)],11:[],12:[]}
strict={1:['003','004','010'],2:['020','021','022'],3:['044'],4:['067','068','069','070','071'],5:['083','084','086','087','088','089','091','092'],6:['115','116'],7:['137','138','139'],8:['152','153'],9:['187'],10:['%03d'%i for i in range(207,244)],11:[],12:[]}
combat_tot=0; strict_tot=0
speakers={}
for i in range(1,len(parts),2):
    num=int(parts[i]); body=parts[i+1]
    scs=re.findall(r'### SC_(\d+) · (.*?) · (video8s|still_kenburns) · (\d+:\d+)–(\d+:\d+)',body)
    sc=len(scs); v=sum(1 for x in scs if x[2]=='video8s'); st=sc-v
    sec=0
    for sid,_,typ,t1,t2 in scs:
        d=tosec(t2)-tosec(t1); sec+=d
        if typ=='video8s' and d!=8: viol.append(f'SC_{sid} video {d}s')
        if typ=='still_kenburns' and not (6<=d<=12): viol.append(f'SC_{sid} still {d}s')
        if prev_end is not None and tosec(t1)!=prev_end: gaps.append(f'SC_{sid} starts {t1} prev end {prev_end//60}:{prev_end%60:02d}')
        prev_end=tosec(t2)
    # narration
    nlines=re.findall(r'^N: (.*)$',body,re.M)
    nw=sum(len(l.split()) for l in nlines)
    nsent=0
    for l in nlines:
        for sent in re.split(r'(?<=[.!?])\s+',l.strip()):
            if not sent: continue
            nsent+=1
            w=len(sent.split())
            if w>15: nviol.append(f'P{num}: {w}어절: {sent}')
    # dialogue: lines "NAME: text" not starting with N:, [ , #, >
    dl=[]
    for l in body.split('\n'):
        m=re.match(r'^([^\[#>\s][^:]{0,30}): (.+)$',l)
        if m and m.group(1)!='N' and not l.startswith('[') :
            dl.append((m.group(1),m.group(2)))
    d=len(dl); dw=sum(len(t.split()) for _,t in dl)
    for name,t in dl:
        speakers[name]=speakers.get(name,0)+1
        if len(t.split())>12: viol.append(f'P{num} {name}: {len(t.split())}어절: {t}')
    cb=sum(tosec(t2)-tosec(t1) for sid,_,typ,t1,t2 in scs if sid in combat_blocks[num])
    cs=sum(tosec(t2)-tosec(t1) for sid,_,typ,t1,t2 in scs if sid in strict[num])
    combat_tot+=cb; strict_tot+=cs
    rows.append((num,sc,v,st,sec,len(nlines),nsent,nw,d,dw,cb,cs))
    for k,val in zip(['sc','v','st','sec','n','nw','d','dw'],[sc,v,st,sec,len(nlines),nw,d,dw]): tot[k]+=val
print('| Phần | SC | video8s | still | Giây | Dòng N | Câu N | 어절 N | Câu thoại | 어절 thoại | Combat khối (s) | Combat thuần (s) |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for r in rows: print('| '+' | '.join(str(x) for x in r)+' |')
print('| Tổng |',tot['sc'],'|',tot['v'],'|',tot['st'],'|',tot['sec'],'|',tot['n'],'|',sum(r[6] for r in rows),'|',tot['nw'],'|',tot['d'],'|',tot['dw'],'|',combat_tot,f'({combat_tot/tot["sec"]*100:.1f}%)','|',strict_tot,f'({strict_tot/tot["sec"]*100:.1f}%)','|')
print('VIOL dialogue/duration:',viol)
print('VIOL narration >15:',len(nviol)); [print(' ',x) for x in nviol]
print('GAPS:',gaps)
print('speakers:',sorted(speakers.items(),key=lambda x:-x[1]))
