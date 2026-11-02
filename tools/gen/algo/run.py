import subprocess,os,json,shutil
exec(open('progs.py').read())
OUT={}
for k,d in P.items():
    OUT[k]={}
    for lang,code in d.items():
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
        OUT[k][lang]=r.stdout.rstrip('\n')
json.dump(OUT,open('out.json','w'),ensure_ascii=False,indent=1)
for k in OUT: print(k, {l:OUT[k][l].split('\n')[-1] for l in OUT[k]})
