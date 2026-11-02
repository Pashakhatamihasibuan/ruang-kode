import subprocess,os,json
exec(open('soal.py').read())
OUT={}
for k,L in Q.items():
    OUT[k]=[]
    for s in L:
        o={}
        for lang,code in s['a'].items():
            os.makedirs('w',exist_ok=True)
            if lang=='java':
                open('w/Main.java','w').write(code); subprocess.run(['javac','w/Main.java'],check=True)
                r=subprocess.run(['java','-cp','w','Main'],capture_output=True,text=True)
            elif lang=='python':
                open('w/m.py','w').write(code); r=subprocess.run(['python3','w/m.py'],capture_output=True,text=True)
            elif lang=='js':
                open('w/m.js','w').write(code); r=subprocess.run(['node','w/m.js'],capture_output=True,text=True)
            else:
                open('w/m.ts','w').write(code); r=subprocess.run(['node','--experimental-strip-types','--no-warnings','w/m.ts'],capture_output=True,text=True)
            if r.returncode: print(k,lang,r.stderr); raise SystemExit
            o[lang]=r.stdout.rstrip('\n')
        OUT[k].append(o)
        print(k,{l:o[l].replace('\n',' | ')[:60] for l in o})
json.dump(OUT,open('soalout.json','w'),ensure_ascii=False,indent=1)
