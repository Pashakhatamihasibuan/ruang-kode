"""Pendalaman materi: istilah dunia kerja dan contoh tambahan per pelajaran.
Sumber: tools/deep/<jalur>.py berisi K (kunci jalur) dan D = {judul pelajaran: {...}}.
  ist: [(istilah, arti), ...]
  cx : [dict(t=judul, b=penjelasan, code=..., lang='python', run=True|False, out=None)]
Contoh Python dengan run=True dijalankan agar keluarannya pasti cocok. Hasil: src/js/deep.json."""
import importlib.util, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/gen'))
from rb_lib import jalan

out = {}
for f in sorted((ROOT / 'tools/deep').glob('*.py')):
    spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    jal = out.setdefault(m.K, {})
    for judul, d in m.D.items():
        e = {}
        if d.get('ist'):
            e['ist'] = [list(x) for x in d['ist']]
        cx = []
        for c in d.get('cx', []):
            c = dict(c); lang = c.get('lang', 'python')
            if c.pop('run', lang == 'python') and lang == 'python':
                c['out'] = jalan(c['code'])
            c['lang'] = lang
            cx.append({k: v for k, v in c.items() if v is not None})
        if cx:
            e['cx'] = cx
        jal[judul] = e
    print(f'{m.K}: {len(m.D)} pelajaran diperdalam, {sum(len(d.get("ist", [])) for d in m.D.values())} istilah, '
          f'{sum(len(d.get("cx", [])) for d in m.D.values())} contoh tambahan')
(ROOT / 'src/js/deep.json').write_text(json.dumps(out, ensure_ascii=False, separators=(',', ':')))
