"""Pembantu proyek berpenyelesaian: setiap jalur karier punya 6 proyek mini dan 4 proyek besar.
Setiap proyek: masalah, fitur wajib, langkah penyelesaian, dan kode penyelesaian lengkap."""
import html, re
from rb_lib import C, M, q, jalan


def polos(t):
    """Tabel ditampilkan sebagai teks biasa: buang tag HTML dan kembalikan entitas."""
    return html.unescape(re.sub(r'<[^>]+>', '', t))


def _body(masalah, wajib, langkah, extra=None):
    b = [f'<b>Masalah.</b> {masalah}',
         '<b>Fitur wajib:</b><br>' + '<br>'.join(f'{i+1}. {w}' for i, w in enumerate(wajib)),
         '<b>Penyelesaian langkah demi langkah:</b><br>' + '<br>'.join(f'{i+1}. {s}' for i, s in enumerate(langkah))]
    if extra:
        b.append(extra)
    return b


def MINI(no, nama, masalah, wajib, langkah, code, lang, out=None, run=False, cek=None, kunci=None):
    """Proyek mini. run=True: kode Python dijalankan saat generate agar keluarannya pasti cocok."""
    if run:
        out = jalan(code)
    tantangan = f'<b>Kembangkan sendiri:</b> {kunci}' if kunci else None
    return C(f'Mini {no}: {nama}', _body(masalah, wajib, langkah, tantangan), code, out, lang,
             tb=[{'c': 'Fitur wajib dan cara penyelesaiannya', 'h': ['Fitur', 'Penyelesaian'], 'r': [[polos(w), polos(s)] for w, s in zip(wajib, langkah)]}],
             pts=[f'Proyek mini: {nama}.', polos(wajib[0]), 'Kode penyelesaian lengkap ada di bawah; ketik ulang, jangan disalin.'],
             qs=[cek] if cek else None)


def BESAR(no, nama, masalah, wajib, stack, arsitektur, langkah, code, lang, out=None, cek=None, standar=None):
    """Proyek besar berskala industri: kode berisi berkas-berkas inti penyelesaiannya."""
    extra = f'<b>Standar industri yang dinilai:</b> {standar}' if standar else None
    return C(f'Besar {no}: {nama}', _body(masalah, wajib, langkah, extra), code, out, lang,
             tb=[{'c': f'Arsitektur dan stack ({stack})', 'h': ['Bagian', 'Isi'], 'r': [[polos(c) for c in r] for r in arsitektur]}],
             pts=[f'Proyek besar: {nama}.', f'Stack: {stack}.', 'Berkas inti penyelesaian ada di bawah; sisanya mengikuti pola yang sama.'],
             qs=[cek] if cek else None)


def JALUR_M(nama, lvl, d, nodes, mini, besar):
    return M(f'Proyek {nama}: 6 mini + 4 besar', lvl, d, nodes, mini + besar)
