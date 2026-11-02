"""Membuat src/js/track-mobile.js (Dart, Flutter, Kotlin, Compose, KMP) dan src/js/track-cssfw.js (Tailwind, Bootstrap).
Jalankan: python3 tools/gen/mobile.py"""
import json, sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
root = here.parent.parent

from mobile_dart import DART, FLUTTER
from mobile_kotlin import KOTLIN, COMPOSE, KMP
from cssfw import TW, BS
from mobile_dart_x import DART_SO, DART_QX, DART_MORE
from mobile_flutter_x import FLUTTER_SO, FLUTTER_QX, FLUTTER_MORE
from mobile_kotlin_x import KOTLIN_SO, KOTLIN_QX, KOTLIN_MORE, COMPOSE_SO, COMPOSE_QX, COMPOSE_MORE, KMP_SO, KMP_QX, KMP_MORE
from cssfw_x import TW_SO, TW_QX, TW_MORE, BS_SO, BS_QX, BS_MORE


import re
OK = re.compile(r'<(?!/?(?:code|b|i|em|strong|br)\b)')
aman = lambda x: OK.sub('&lt;', x)


def rapikan(mods):
    """Teks yang tampil sebagai HTML: '<' yang bukan tag yang diizinkan ditulis sebagai &lt;."""
    for m in mods:
        for l in m['lessons']:
            l['b'] = [aman(x) for x in l['b']]
            if 'pts' in l: l['pts'] = [aman(x) for x in l['pts']]
            for x in l.get('so', []):
                x['q'], x['h'] = aman(x['q']), aman(x['h'])
            if 'q' in l: l['q'] = [[aman(a), [aman(o) for o in b], c, aman(d)] for a, b, c, d in l['q']]
            if 'task' in l: l['task']['q'] = aman(l['task']['q'])


def gabung(nama, mods, so, qx, more):
    judul = {l['t']: l for m in mods for l in m['lessons']}
    for kamus, kunci in ((so, 'so'), (qx, 'q')):
        for t, isi in kamus.items():
            if t not in judul:
                raise SystemExit(f'{nama}: pelajaran "{t}" tidak ditemukan')
            judul[t].setdefault(kunci, []).extend(isi)
    out = mods + more
    rapikan(out)
    n = sum(len(m['lessons']) for m in out)
    s = sum(len(l.get('so', [])) for m in out for l in m['lessons'])
    print(f'{nama}: {len(out)} modul, {n} pelajaran, {s} soal latihan')
    return out


J = lambda v: json.dumps(v, ensure_ascii=False)
T = {
    'DART': gabung('dart', DART, DART_SO, DART_QX, DART_MORE),
    'FLUTTER': gabung('flutter', FLUTTER, FLUTTER_SO, FLUTTER_QX, FLUTTER_MORE),
    'KOTLIN': gabung('kotlin', KOTLIN, KOTLIN_SO, KOTLIN_QX, KOTLIN_MORE),
    'COMPOSE': gabung('compose', COMPOSE, COMPOSE_SO, COMPOSE_QX, COMPOSE_MORE),
    'KMP': gabung('kmp', KMP, KMP_SO, KMP_QX, KMP_MORE),
    'TW': gabung('tw', TW, TW_SO, TW_QX, TW_MORE),
    'BS': gabung('bs', BS, BS_SO, BS_QX, BS_MORE),
}

head = '/* ===================== {} =====================\n   Dibuat oleh tools/gen/mobile.py dari tools/gen/{}. Jangan diedit langsung. */\n'
mob = head.format('JALUR DART, FLUTTER, KOTLIN, JETPACK COMPOSE, KMP', 'mobile_*.py') + ''.join(
    f'const {k}_MODULES={J(T[k])};\n' for k in ('DART', 'FLUTTER', 'KOTLIN', 'COMPOSE', 'KMP'))
css = head.format('JALUR TAILWIND CSS & BOOTSTRAP 5', 'cssfw*.py') + ''.join(
    f'const {k}_MODULES={J(T[k])};\n' for k in ('TW', 'BS'))
(root / 'src/js/track-mobile.js').write_text(mob)
(root / 'src/js/track-cssfw.js').write_text(css)
