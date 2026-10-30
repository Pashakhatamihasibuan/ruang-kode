# Helper: emit JS module arrays from python dicts, running code to fill `out`.
import json, subprocess, sys, textwrap
def run(code):
    r=subprocess.run([sys.executable,'-I','-c',code],capture_output=True,text=True,timeout=60)
    if r.returncode!=0: raise SystemExit('ERROR running:\n'+code+'\n'+r.stderr)
    return r.stdout.rstrip('\n')
def js(v):
    return json.dumps(v,ensure_ascii=False)
def emit(name,header,mods):
    out=[header,f'const {name}=[']
    for m in mods:
        for l in m['lessons']:
            if l.get('k')=='c' and l.get('exec'):
                l['out']=run(l['code']); del l['exec']
        out.append(js(m)+',')
    out.append('];')
    return '\n'.join(out)+'\n'
