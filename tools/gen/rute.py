"""Membuat src/js/track-rute.js: jalur tambahan (UI Design, Slicing Website, Slicing Mobile, dan jalur roadmap baru).
Jalankan: python3 tools/gen/rute.py   (CEK=berkas.json untuk menulis data uji tantangan)"""
import json, sys, re
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
root = here.parent.parent

OK = re.compile(r'<(?!/?(?:code|b|i|em|strong|br)\b)')
aman = lambda x: OK.sub('&lt;', x)

JALUR = []  # (KONSTANTA, modul, soal)
from uidesign import UI, UI_SO
JALUR.append(('UI', UI, UI_SO))
try:
    from slicing import SLW, SLW_SO, SLM, SLM_SO
    JALUR += [('SLW', SLW, SLW_SO), ('SLM', SLM, SLM_SO)]
except ImportError:
    pass
try:
    from roadmap_baru import BARU
    JALUR += BARU
except ImportError:
    pass

cek = {}
out = []
for nama, mods, so in JALUR:
    judul = {l['t']: l for m in mods for l in m['lessons']}
    assert len(judul) == sum(len(m['lessons']) for m in mods), nama + ': judul ganda'
    for t, isi in so.items():
        if t not in judul:
            raise SystemExit(f'{nama}: pelajaran "{t}" tidak ditemukan')
        judul[t].setdefault('so', []).extend(isi)
    for mi, m in enumerate(mods):
        for li, l in enumerate(m['lessons']):
            if 'cek' in l:
                cek[f'{nama}|{mi}|{li}'] = {'t': l['t'], 'html': l['html'], 'css': l.get('css', ''), 'test': l['task']['test'], 'cek': l.pop('cek')}
            l['b'] = [aman(x) for x in l['b']]
            if 'pts' in l: l['pts'] = [aman(x) for x in l['pts']]
            for x in l.get('so', []): x['q'], x['h'] = aman(x['q']), aman(x['h'])
            if 'q' in l: l['q'] = [[aman(a), [aman(o) for o in b], c, aman(d)] for a, b, c, d in l['q']]
            if 'task' in l: l['task']['q'] = aman(l['task']['q'])
    n = sum(len(m['lessons']) for m in mods)
    s = sum(len(l.get('so', [])) for m in mods for l in m['lessons'])
    print(f'{nama}: {len(mods)} modul, {n} pelajaran, {s} soal')
    out.append(f'const {nama}_MODULES={json.dumps(mods, ensure_ascii=False)};\n')

(root / 'src/js/track-rute.js').write_text('/* ===================== JALUR TAMBAHAN =====================\n   Dibuat oleh tools/gen/rute.py. Jangan diedit langsung. */\n' + ''.join(out))
import os
if os.environ.get('CEK'): Path(os.environ['CEK']).write_text(json.dumps(cek, ensure_ascii=False))
print('cek', len(cek))
