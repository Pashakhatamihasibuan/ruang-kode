"""Membuat src/js/track-so.js: soal latihan tambahan untuk jalur yang ditulis tangan.
Isi soal ada di tools/gen/soal_*.py (kamus SOAL: nama konstanta modul -> {judul pelajaran: [soal]}).
Jalankan: python3 tools/gen/soal.py"""
import glob, importlib, json, os, re, subprocess, sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
root = here.parent.parent
OK = re.compile(r'<(?!/?(?:code|b|i|em|strong|br)\b)')
aman = lambda x: OK.sub('&lt;', x)

semua = {}
for f in sorted(glob.glob(str(here / 'soal_*.py'))):
    mod = importlib.import_module(Path(f).stem)
    for nama, isi in mod.SOAL.items():
        d = semua.setdefault(nama, {})
        for judul, daftar in isi.items():
            d.setdefault(judul, []).extend({**s, 'q': aman(s['q']), 'h': aman(s['h'])} for s in daftar)

nama = sorted(semua)
js = ('/* ===================== SOAL LATIHAN TAMBAHAN =====================\n'
      '   Dibuat oleh tools/gen/soal.py dari tools/gen/soal_*.py. Jangan diedit langsung.\n'
      '   Soal ditempel ke pelajaran berdasarkan judulnya. */\n'
      'const SO_TAMBAHAN=' + json.dumps(semua, ensure_ascii=False) + ';\n'
      '[' + ','.join(f'["{n}",{n}]' for n in nama) + '].forEach(([n,M])=>M.forEach(m=>m.lessons.forEach(l=>{'
      'const s=l.t&&SO_TAMBAHAN[n][l.t];if(s)l.so=(l.so||[]).concat(s)})));\n')
(root / 'src/js/track-so.js').write_text(js)

# periksa: setiap judul harus cocok dengan satu pelajaran
cek = ("const fs=require('fs');let s='';for(const f of process.argv.slice(1))s+=fs.readFileSync(f,'utf8')+'\\n;\\n';"
       "s=s.replace(/^(const|let) /gm,'var ');eval(s);const miss=[];"
       "for(const [n,d] of Object.entries(SO_TAMBAHAN)){const T=new Set(eval(n).flatMap(m=>m.lessons.map(l=>l.t)));"
       "for(const t of Object.keys(d))if(!T.has(t))miss.push(n+': '+t)}console.log(miss.length?'TIDAK COCOK:\\n'+miss.join('\\n'):'semua judul cocok')")
files = [str(root / 'src/js' / f) for f in ['data.js', 'lang-only.js'] + [x.strip('" ') for x in re.search(r'TRACK_JS = \[(.*?)\]', (root / 'build.py').read_text(), re.S).group(1).replace('\n', '').split(',')]]
print(subprocess.run(['node', '-e', cek, *files], capture_output=True, text=True).stdout.strip() or 'node gagal')
n = sum(len(v) for d in semua.values() for v in d.values())
print(f'{n} soal untuk {len(semua)} jalur')
