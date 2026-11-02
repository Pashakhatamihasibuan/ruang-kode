"""Menjalankan jawaban soal SQL di mesin SQL situs dan menyimpan keluarannya ke soal_sql_out.json."""
import sys,json,subprocess,re,os
G=os.path.dirname(os.path.abspath(__file__))+'/';sys.path.insert(0,G)
src=open(G+'soal_sql.py').read()
code=src.split('# keluaran hasil')[0]
ns={};exec(compile(code,'soal_sql','exec'),ns)
items=[]
for t,L in ns['SQL'].items():
  for i,s in enumerate(L):
    if s.get('out')=='RUN': items.append({'sql':s['a'],'k':f'{t}#{i}'})
r=json.loads(subprocess.run(['node',G+'sql_jalankan.js'],input=json.dumps(items),capture_output=True,text=True).stdout)
out={it['k']:(x['out'] if x['ok'] else 'Galat: '+x['err']) for it,x in zip(items,r)}
json.dump(out,open(G+'soal_sql_out.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'keluaran')
