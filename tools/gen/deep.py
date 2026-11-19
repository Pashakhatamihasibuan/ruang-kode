"""Pendalaman materi: istilah dunia kerja dan contoh tambahan per pelajaran.
Sumber: tools/deep/<berkas>.py berisi K (kunci jalur) dan D = {judul pelajaran: {...}}.
Beberapa berkas boleh memakai K yang sama; isinya digabung.
  ist: [(istilah, arti), ...]
  cx : [dict(t=judul, b=penjelasan, code=..., lang='python'|'java'|'sql'|..., run=True|False, out=None, setup=None)]
Contoh dengan run=True dijalankan agar keluarannya pasti cocok:
  python -> exec; java -> `java Main.java` (JDK 21); sql -> SQLite di memori (setup dijalankan dulu, tidak ditampilkan).
Keluaran disimpan di cache (tools/deep/.cache.json) berdasarkan hash kode. Hasil: src/js/deep.json."""
import hashlib, importlib.util, json, pathlib, sqlite3, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/gen'))
from rb_lib import jalan

CACHE_F = ROOT / 'tools/deep/.cache.json'
CACHE = json.loads(CACHE_F.read_text()) if CACHE_F.exists() else {}


def jalan_java(code):
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / 'Main.java'
        p.write_text(code)
        r = subprocess.run(['java', p.name], cwd=d, capture_output=True, text=True, timeout=60)
        err = '\n'.join(l for l in r.stderr.splitlines() if 'JAVA_TOOL_OPTIONS' not in l)
        if r.returncode != 0 and 'Exception' not in err:
            raise RuntimeError(f'Java gagal:\n{err}\n---\n{code}')
        out = r.stdout.rstrip('\n')
        if r.returncode != 0:  # contoh yang sengaja melempar exception: tampilkan baris pertamanya
            out = (out + '\n' if out else '') + err.splitlines()[0]
        return out


def _tabel(cur):
    kol = [c[0] for c in cur.description]
    rows = [['NULL' if v is None else str(v) for v in r] for r in cur.fetchall()]
    w = [max([len(k)] + [len(r[i]) for r in rows]) for i, k in enumerate(kol)]
    garis = '-+-'.join('-' * x for x in w)
    fmt = lambda r: ' | '.join(v.ljust(w[i]) for i, v in enumerate(r))
    return '\n'.join([fmt(kol), garis] + [fmt(r) for r in rows] + [f'({len(rows)} baris)'])


def jalan_sql(code, setup=''):
    con = sqlite3.connect(':memory:', isolation_level=None)
    if setup:
        con.executescript(setup)
    hasil, buf = [], ''
    for baris in code.splitlines(keepends=True):
        buf += baris
        if sqlite3.complete_statement(buf):
            s = buf.strip(); buf = ''
            cur = con.execute(s)
            if cur.description:
                hasil.append(_tabel(cur))
            else:
                inti = '\n'.join(l for l in s.splitlines() if not l.strip().startswith('--')).strip()
                if inti.upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                    hasil.append(f'{cur.rowcount} baris terpengaruh')
    return '\n\n'.join(hasil)


def jalankan(c):
    lang = c.get('lang', 'python')
    key = hashlib.sha1((lang + '\0' + c.get('setup', '') + '\0' + c['code']).encode()).hexdigest()
    if key not in CACHE:
        if lang == 'python':
            CACHE[key] = jalan(c['code'])
        elif lang == 'java':
            CACHE[key] = jalan_java(c['code'])
        elif lang == 'sql':
            CACHE[key] = jalan_sql(c['code'], c.get('setup', ''))
    return CACHE[key]


out, kerja = {}, []
for f in sorted((ROOT / 'tools/deep').glob('*.py')):
    spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    jal = out.setdefault(m.K, {})
    for judul, d in m.D.items():
        e = {}
        if d.get('ist'):
            e['ist'] = [list(x) for x in d['ist']]
        cx = []
        for c in d.get('cx', []):
            c = dict(c); lang = c.setdefault('lang', 'python')
            if c.pop('run', lang in ('python', 'java', 'sql')) and lang in ('python', 'java', 'sql'):
                kerja.append(c)
            cx.append(c)
        if cx:
            e['cx'] = cx
        jal[judul] = e
    print(f'{f.stem} ({m.K}): {len(m.D)} pelajaran, {sum(len(d.get("ist", [])) for d in m.D.values())} istilah, '
          f'{sum(len(d.get("cx", [])) for d in m.D.values())} contoh')

# Python dijalankan berurutan (redirect_stdout tidak aman antar thread); Java paralel.
for c in kerja:
    if c['lang'] != 'java':
        c['out'] = jalankan(c)
with ThreadPoolExecutor(6) as ex:
    js = [c for c in kerja if c['lang'] == 'java']
    for c, o in zip(js, ex.map(jalankan, js)):
        c['out'] = o
CACHE_F.write_text(json.dumps(CACHE, ensure_ascii=False))
for jal in out.values():
    for e in jal.values():
        e['cx'] = [{k: v for k, v in c.items() if v is not None and v != ''} for c in e.get('cx', [])] or None
        if e['cx'] is None:
            del e['cx']
(ROOT / 'src/js/deep.json').write_text(json.dumps(out, ensure_ascii=False, separators=(',', ':')))
print('total:', {k: len(v) for k, v in out.items()})
