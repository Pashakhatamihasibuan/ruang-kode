"""Papan dokumentasi (riset, struktur, design system, handoff, motion) sebagai SVG berlayer.
Semua papan memakai tata letak yang sama: judul tahap di kiri atas, isi dalam kartu."""
import math
from svgkit import Svg, Tema, lebar_teks, bungkus, campur

TINTA = '#1B1B1F'
ABU = '#5F5F68'
GARIS = '#DADAE0'
LATAR = '#F5F5F7'
STICKY = ['#FFE9A8', '#CDEBFF', '#D9F5D0', '#FFD6E0', '#E6DDFF', '#FFE0C7']


def papan(nama, w, h, tahap, judul, sub):
    s = Svg(w, h, nama, LATAR)
    s.font = 'Plus Jakarta Sans'
    s.gradasi = None
    with s.g('Kepala papan'):
        s.rect(64, 56, lebar_teks(tahap, 13, 700) + 28, 30, TINTA, r=15, nama='Label tahap')
        s.text(78, 76, tahap, 13, 700, '#FFFFFF', nama='Teks tahap')
        s.text(64, 140, judul, 44, 800, TINTA, nama='Judul papan')
        s.text(64, 180, sub, 18, 400, ABU, nama='Subjudul papan', maks=w - 128)
    return s


def kartu(s, x, y, w, h, judul=None, warna='#FFFFFF', nama=None, garis=GARIS, aksen=None):
    with s.g(nama or f'Kartu/{judul or ""}'):
        s.rect(x, y, w, h, warna, r=16, stroke=garis, sw=1, nama='Latar kartu')
        if aksen:
            s.rect(x, y, 6, h, aksen, r=3, nama='Aksen')
        if judul:
            s.text(x + 24, y + 38, judul, 18, 700, TINTA, nama='Judul kartu')
    return y + 56


def teks(s, x, y, isi, size=15, weight=400, warna=TINTA, maks=None, lh=None, nama=None):
    return s.text(x, y, isi, size, weight, warna, nama=nama, maks=maks, lh=lh or round(size * 1.5))


def daftar(s, x, y, butir, maks, size=15, warna=TINTA, titik=TINTA, jarak=8):
    """Daftar berpoin; mengembalikan y setelah butir terakhir."""
    for b in butir:
        s.circle(x + 4, y - size * 0.32, 3, titik)
        y += teks(s, x + 18, y, b, size, 400, warna, maks=maks - 18) + jarak
    return y


def sticky(s, x, y, w, h, isi, warna, nama=None, size=14):
    with s.g(nama or f'Sticky/{isi[:24]}'):
        s.rect(x, y, w, h, warna, r=4, nama='Kertas')
        s.rect(x, y + h - 6, w, 6, '#0000000D', r=0, nama='Lipatan')
        s.text(x + 14, y + 28, isi, size, 500, TINTA, maks=w - 28, lh=round(size * 1.45), nama='Isi')


def panah(s, x1, y1, x2, y2, warna=TINTA, sw=2, label=None, nama='Panah', dash=None):
    with s.g(nama):
        s.line(x1, y1, x2, y2, warna, sw, dash=dash)
        a = math.atan2(y2 - y1, x2 - x1)
        p = [(x2, y2), (x2 - 11 * math.cos(a - 0.45), y2 - 11 * math.sin(a - 0.45)), (x2 - 11 * math.cos(a + 0.45), y2 - 11 * math.sin(a + 0.45))]
        s.path('M' + 'L'.join(f'{px:.1f} {py:.1f}' for px, py in p) + 'Z', fill=warna, nama='Kepala panah')
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            lw = lebar_teks(label, 12, 600) + 16
            s.rect(mx - lw / 2, my - 13, lw, 24, '#FFFFFF', r=12, stroke=GARIS)
            s.text(mx, my + 4, label, 12, 600, ABU, 'middle', nama='Label panah')


def simpul(s, x, y, w, h, isi, jenis='layar', warna=None, nama=None):
    """Simpul diagram alur: layar (kotak), keputusan (belah ketupat), mulai/selesai (kapsul)."""
    with s.g(nama or f'Simpul/{isi[:30]}'):
        if jenis == 'keputusan':
            cx, cy = x + w / 2, y + h / 2
            s.path(f'M{cx:g} {y:g}L{x + w:g} {cy:g}L{cx:g} {y + h:g}L{x:g} {cy:g}Z', fill=warna or '#FFF4D6', stroke=TINTA, sw=1.5, nama='Bentuk')
        elif jenis == 'terminal':
            s.rect(x, y, w, h, warna or TINTA, r=h / 2, nama='Bentuk')
        else:
            s.rect(x, y, w, h, warna or '#FFFFFF', r=10, stroke=TINTA, sw=1.5, nama='Bentuk')
        baris = bungkus(isi, w - 24, 14, 600)
        y0 = y + h / 2 - (len(baris) - 1) * 10 + 5
        s.text(x + w / 2, y0, isi, 14, 600, '#FFFFFF' if jenis == 'terminal' else TINTA, 'middle', maks=w - 24, lh=20, nama='Label')


def swatch(s, x, y, nama_token, nilai, peran=None, w=168):
    with s.g(f'Swatch/{nama_token}'):
        s.rect(x, y, w, 96, nilai, r=12, stroke=GARIS, nama='Warna')
        s.text(x, y + 122, nama_token, 13, 700, TINTA, nama='Nama token')
        s.text(x, y + 142, nilai.upper(), 13, 400, ABU, nama='Nilai')
        if peran:
            s.text(x, y + 162, peran, 12, 400, ABU, nama='Peran', maks=w)


def kontras(a, b):
    def lum(h):
        h = h.lstrip('#')
        r, g, bb = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(bb)
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def ukuran(s, x1, y1, x2, y2, label, warna='#E5484D', nama=None):
    """Garis ukur redline (horizontal atau vertikal) dengan label nilai."""
    with s.g(nama or f'Redline/{label}'):
        s.line(x1, y1, x2, y2, warna, 1)
        if y1 == y2:
            s.line(x1, y1 - 5, x1, y1 + 5, warna, 1); s.line(x2, y2 - 5, x2, y2 + 5, warna, 1)
            mx, my = (x1 + x2) / 2, y1
        else:
            s.line(x1 - 5, y1, x1 + 5, y1, warna, 1); s.line(x2 - 5, y2, x2 + 5, y2, warna, 1)
            mx, my = x1, (y1 + y2) / 2
        lw = lebar_teks(label, 11, 700) + 10
        s.rect(mx - lw / 2, my - 9, lw, 18, warna, r=4, nama='Label')
        s.text(mx, my + 4, label, 11, 700, '#FFFFFF', 'middle', nama='Nilai')


def tempel(s, svg_lain, x, y, skala=1.0, nama=None):
    """Sisipkan SVG layar lain (isi <g> akarnya) sebagai grup, untuk papan yang memuat layar."""
    i = svg_lain.index('<g id=')
    j = svg_lain.rindex('</g>')
    isi = svg_lain[i:j + 4]
    tr = f'translate({x:g} {y:g})' + (f' scale({skala:g})' if skala != 1 else '')
    s._add(f'<g id="{nama or "Layar"}" transform="{tr}">')
    s._add(isi)
    s._add('</g>')
    # gradasi latar milik layar ditempel (jika ada) disalin ke defs papan
    if '<defs>' in svg_lain:
        d = svg_lain[svg_lain.index('<defs>') + 6:svg_lain.index('</defs>')]
        s.defs_extra = getattr(s, 'defs_extra', '') + d
