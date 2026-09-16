import re,sys,json
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
if '\n## 부록' in s: s=s[:s.index('\n## 부록')]
blocks=re.split(r'(?=^### SC_)',s,flags=re.M)[1:]
rows=[]
for b in blocks:
    m=re.match(r'### SC_(\d+) · .*? · (video8s|still_kenburns) · (\d+:\d+)–(\d+:\d+)',b)
    sid,typ,t1,t2=m.groups()
    n=' '.join(re.findall(r'^N: (.*)$',b,re.M))
    nw=len(n.split())
    dw=0
    for l in b.split('\n'):
        mm=re.match(r'^([^\[#>\s][^:]{0,30}): (.+)$',l)
        if mm and mm.group(1)!='N': dw+=len(mm.group(2).split())
    lim=22 if typ=='video8s' else 45
    rows.append((sid,typ,nw,dw,nw+dw,lim))
over=[r for r in rows if r[4]>r[5]]
print('over:',len(over),'total excess:',sum(r[4]-r[5] for r in over))
for r in over: print(r[0],r[1][:5],'N',r[2],'D',r[3],'tot',r[4],'lim',r[5],'excess',r[4]-r[5])
json.dump(rows,open(sys.argv[2],'w'))
