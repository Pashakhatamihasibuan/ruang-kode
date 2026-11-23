"""Pustaka kecil untuk menulis papan desain SVG yang rapi saat diimpor ke Figma.

Aturan agar hasil impor enak dipakai:
- setiap bagian dibungkus <g id="Nama layer"> sehingga muncul sebagai grup bernama di panel Layers;
- teks ditulis sebagai <text> asli (bisa diedit), font Google "Plus Jakarta Sans" yang tersedia di Figma;
- tidak ada filter, mask, atau gambar raster: semuanya vektor, jadi bisa diekspor ulang dalam ukuran apa pun.
"""
from contextlib import contextmanager
from xml.sax.saxutils import escape

FONT = 'Plus Jakarta Sans'
# faktor lebar rata-rata per huruf (x ukuran font), diukur kasar per keluarga font
LEBAR_FONT = {'Dela Gothic One': 0.74, 'Space Grotesk': 0.58, 'Sora': 0.62, 'Roboto Flex': 0.54, 'Outfit': 0.54,
              'Nunito': 0.56, 'Fraunces': 0.56, 'Space Mono': 0.62}
_AKTIF = [None]   # tema terakhir yang dibuat; dibaca Svg() untuk font isi & latar gradasi


def esc(s):
    return escape(str(s), {'"': '&quot;'})


def lebar_teks(s, size, weight=400, fam=None):
    """Perkiraan lebar teks (px) untuk tata letak; cukup akurat untuk Plus Jakarta Sans."""
    f = 0.60 if weight >= 600 else 0.56
    if fam and fam != FONT: f = LEBAR_FONT.get(fam, 0.62) + (0.03 if weight >= 600 else 0)
    sempit = sum(1 for c in str(s) if c in 'il.,:;|!\'ftrj1 ')
    lebar = sum(1 for c in str(s) if c in 'mwMW@%')
    return size * (f * len(str(s)) - 0.25 * sempit + 0.3 * lebar)


def bungkus(teks, maks, size, weight=400, fam=None):
    baris, cur = [], ''
    for kata in str(teks).split():
        coba = (cur + ' ' + kata).strip()
        if cur and lebar_teks(coba, size, weight, fam) > maks:
            baris.append(cur)
            cur = kata
        else:
            cur = coba
    if cur:
        baris.append(cur)
    return baris


# ---------------------------------------------------------------- gaya visual
def campur(a, b, k):
    """Campur warna a ke b sebanyak k (0..1)."""
    a, b = a.lstrip('#')[:6], b.lstrip('#')[:6]
    c = [round(int(a[i:i + 2], 16) * (1 - k) + int(b[i:i + 2], 16) * k) for i in (0, 2, 4)]
    return '#' + ''.join(f'{v:02X}' for v in c)


def _m3(t):
    """Material 3: permukaan tonal turunan warna primer."""
    p = t['primer']
    t.update(latar=campur(p, '#FFFFFF', 0.95), permukaan=campur(p, '#FFFFFF', 0.9), lembut=campur(p, '#FFFFFF', 0.8),
             garis=campur(p, '#FFFFFF', 0.65))


def _editorial(t):
    t.update(latar='#F7F3EC', permukaan='#FFFDF8', lembut='#EFE8DC')


def _gelap(t):
    """Mode gelap: latar & permukaan gelap, teks terang, aksen tetap dari brand."""
    t.update(latar='#121212', permukaan='#1E1E1E', lembut='#2A2A2A', teks='#F2F2F2', teks2='#B5B5B5', garis='#3A3A3A')
    t['primer'] = t.get('primer_gelap') or campur(t['primer'], '#FFFFFF', 0.62)
    t['primer2'] = campur(t['primer2'], '#FFFFFF', 0.2)


def _kaca(t):
    t['latar_gradasi'] = (campur(t['primer'], '#FFFFFF', 0.7), campur(t['aksen'], '#FFFFFF', 0.55), campur(t['primer2'], '#FFFFFF', 0.75))
    t.update(permukaan='#FFFFFFB8', lembut='#FFFFFF73', garis='#FFFFFFCC')


def _clay(t):
    t.update(latar='#F4EFFA' if 'latar_clay' not in t else t['latar_clay'], garis='#00000000')


GAYA = {
    'wireframe': dict(),
    'modern':    dict(label='Modern minimal', bayang='lembut', fonts=[]),
    'brutal':    dict(label='Neo-brutalism', tinta=True, sw=2.5, bayang='blok', radius=6, fj='Space Grotesk', fonts=['Space Grotesk']),
    'kaca':      dict(label='Liquid Glass', kaca=True, bayang='lembut', radius=22, fj='Sora', wj=600, ubah=_kaca, fonts=['Sora']),
    'm3':        dict(label='Material 3 Expressive', radius=28, ubah=_m3, fj='Roboto Flex', wj=800, fb='Roboto Flex', fonts=['Roboto Flex']),
    'gelap':     dict(label='Dark mode', bayang=None, radius=14, ubah=_gelap, fj='Outfit', fonts=['Outfit']),
    'clay':      dict(label='Claymorphism', bayang='clay', radius=26, fj='Nunito', wj=800, fb='Nunito', ubah=_clay, fonts=['Nunito']),
    'editorial': dict(label='Editorial', radius=2, tinta=True, sw=1, ubah=_editorial, fj='Fraunces', wj=600, fonts=['Fraunces']),
    'retro':     dict(label='Retro Y2K', tinta=True, sw=2, bayang='blok', radius=12, fj='Space Mono', wj=700, fonts=['Space Mono']),
    'manga':     dict(label='Manga', tinta=True, komik=True, sw=2.5, bayang='blok', fj='Dela Gothic One', wj=400, fonts=['Dela Gothic One']),
}


# ---------------------------------------------------------------- tema
class Tema:
    """Token warna satu proyek. fid: 'lo' (wireframe), 'mid' (abu-abu, konten asli), 'hi' (final)."""
    def __init__(self, fid='hi', **t):
        base = dict(primer='#8A4B2A', primer2='#6B3A20', aksen='#E9B872', latar='#FBF7F2', permukaan='#FFFFFF',
                    teks='#2B2724', teks2='#6B625B', garis='#E8DFD5', sukses='#1E7A4C', bahaya='#B3261E',
                    peringatan='#9A6700', info='#1F5FA8', lembut='#F3E9DF', radius=12, nama='Kopi Kita')
        base.update(t)
        self.fid = fid
        self.t = base
        if fid != 'hi':
            abu = dict(primer='#3A3A3A', primer2='#222222', aksen='#9E9E9E', latar='#F4F4F4', permukaan='#FFFFFF',
                       teks='#222222', teks2='#6E6E6E', garis='#D6D6D6', sukses='#555555', bahaya='#555555',
                       peringatan='#555555', info='#555555', lembut='#E6E6E6')
            if fid == 'lo':
                abu.update(primer='#FFFFFF', primer2='#444444', latar='#FFFFFF', lembut='#EDEDED', garis='#9A9A9A', teks='#555555', teks2='#9A9A9A')
            self.t.update(abu)
        g = GAYA[base.get('gaya', 'modern')] if fid == 'hi' else GAYA['wireframe']
        self.gaya = base.get('gaya', 'modern') if fid == 'hi' else 'wireframe'
        if fid == 'hi':
            self.t.update(g.get('warna', {}))
            if callable(g.get('ubah')):
                g['ubah'](self.t)
        r0 = g.get('radius', base['radius'])
        self.r = r0 if fid == 'hi' else (8 if fid == 'mid' else 4)
        self.tinta = g.get('tinta', False)      # garis tinta tebal (brutalism, manga, retro)
        self.komik = g.get('komik', False)      # dekorasi manga: screentone, garis kecepatan, balon kata
        self.bayang = g.get('bayang')           # None | 'blok' | 'lembut' | 'clay'
        self.kaca = g.get('kaca', False)        # permukaan tembus pandang (Liquid Glass/glassmorphism)
        self.sw = g.get('sw', 1)
        self.fj = g.get('fj', FONT)             # font judul
        self.wj = g.get('wj', 700)              # ketebalan judul
        self.fb = g.get('fb', FONT)             # font isi
        self.manga = self.tinta                 # nama lama, dipakai komponen
        if self.tinta:
            self.t['garis'] = g.get('tinta_warna', '#121212')
        _AKTIF[0] = self

    def __getattr__(self, k):
        t = self.__dict__.get('t', {})
        if k in t:
            return t[k]
        raise AttributeError(k)

    @property
    def lo(self):
        return self.fid == 'lo'

    @property
    def hi(self):
        return self.fid == 'hi'

    def di_atas(self, warna):
        """Warna teks di atas warna isi (putih untuk isi gelap)."""
        h = warna.lstrip('#')
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        lin = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return '#FFFFFF' if 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b) < 0.45 else '#1A1A1A'


# ---------------------------------------------------------------- ikon (24x24, garis 2px)
IKON = {
    'home': 'M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z',
    'search': 'M11 4a7 7 0 1 1 0 14 7 7 0 0 1 0-14zM20 20l-4-4',
    'cart': 'M3 4h2l2.4 11h10.2L20 8H6.2M9 20a1 1 0 1 0 0-.01M17 20a1 1 0 1 0 0-.01',
    'bag': 'M5 8h14l-1 12H6zM9 8V6a3 3 0 0 1 6 0v2',
    'user': 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21a8 8 0 0 1 16 0',
    'heart': 'M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z',
    'plus': 'M12 5v14M5 12h14',
    'minus': 'M5 12h14',
    'back': 'M15 5l-7 7 7 7',
    'next': 'M9 5l7 7-7 7',
    'down': 'M6 9l6 6 6-6',
    'close': 'M6 6l12 12M18 6 6 18',
    'check': 'M5 12.5l4.5 4.5L19 7',
    'star': 'M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z',
    'clock': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM12 7v5l3 2',
    'pin': 'M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21zM12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
    'menu': 'M4 7h16M4 12h16M4 17h16',
    'bell': 'M6 16V11a6 6 0 0 1 12 0v5l2 2H4zM10 21h4',
    'filter': 'M4 6h16M7 12h10M10 18h4',
    'cup': 'M5 8h11v6a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5zM16 10h1.5a2.5 2.5 0 0 1 0 5H16M8 3v2M11 3v2',
    'receipt': 'M6 3h12v18l-3-2-3 2-3-2-3 2zM9 8h6M9 12h6M9 16h3',
    'card': 'M3 6h18v12H3zM3 10h18M7 15h4',
    'qr': 'M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h2v2h-2zM18 18h2v2h-2zM14 18h2v2h-2zM18 14h2v2h-2z',
    'wallet': 'M4 7h15a1 1 0 0 1 1 1v11H4zM4 7V5h12v2M16 13h2',
    'info': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM12 11v6M12 7.5v.5',
    'alert': 'M12 3 2 20h20zM12 10v5M12 17.5v.5',
    'chat': 'M4 5h16v11H9l-5 4z',
    'send': 'M4 12 20 4l-6 16-3-7z',
    'mic': 'M12 3a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM5 11a7 7 0 0 0 14 0M12 18v3',
    'chart': 'M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-3',
    'doc': 'M6 3h9l4 4v14H6zM14 3v5h5M9 13h7M9 17h5',
    'calendar': 'M4 6h16v15H4zM4 10h16M8 3v4M16 3v4',
    'eye': 'M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z',
    'lock': 'M6 11h12v10H6zM8 11V8a4 4 0 0 1 8 0v3',
    'phone': 'M7 3h10v18H7zM11 18h2',
    'mail': 'M3 6h18v12H3zM3 7l9 6 9-6',
    'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z',
    'list': 'M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01',
    'settings': 'M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1',
    'logout': 'M10 4H5v16h5M14 8l4 4-4 4M18 12H9',
    'upload': 'M12 16V4M7 9l5-5 5 5M4 20h16',
    'download': 'M12 4v12M7 11l5 5 5-5M4 20h16',
    'map': 'M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v14M15 6v14',
    'bike': 'M6 17a3 3 0 1 0 0-.01M18 17a3 3 0 1 0 0-.01M6 17l4-7h5l3 7M12 10 10 6H8',
    'pill': 'M8.5 15.5 15.5 8.5a3.5 3.5 0 1 0-5-5l-7 7a3.5 3.5 0 1 0 5 5zM7 7l7 7',
    'sparkle': 'M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6',
    'trash': 'M4 7h16M10 11v6M14 11v6M6 7l1 14h10l1-14M9 7V4h6v3',
    'edit': 'M4 20h4L19 9l-4-4L4 16zM14 6l4 4',
    'share': 'M18 8a3 3 0 1 0 0-.01M6 12a3 3 0 1 0 0-.01M18 16a3 3 0 1 0 0-.01M8.7 10.7l6.6-3.4M8.7 13.3l6.6 3.4',
    'globe': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18',
    'shield': 'M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z',
    'refresh': 'M20 11a8 8 0 1 0-2.3 5.7M20 4v7h-7',
}


# ---------------------------------------------------------------- kanvas
def _warna(attr, c):
    """Ubah #RRGGBBAA jadi warna + opacity terpisah (lebih aman untuk impor Figma)."""
    if isinstance(c, str) and c.startswith('#') and len(c) == 9:
        a = int(c[7:9], 16) / 255
        return f' {attr}="{c[:7]}" {attr}-opacity="{a:.2f}"'
    return f' {attr}="{c}"'


class Svg:
    def __init__(self, w, h, nama, latar='#FFFFFF'):
        self.w, self.h, self.nama, self.latar = w, h, nama, latar
        self.isi = []
        self.d = 0
        T = _AKTIF[0]
        self.font = T.fb if T else FONT
        self.gradasi = T.t.get('latar_gradasi') if T else None   # latar gradasi gaya kaca

    def _add(self, s):
        self.isi.append('  ' * (self.d + 1) + s)

    @contextmanager
    def g(self, nama, tx=0, ty=0):
        tr = f' transform="translate({tx} {ty})"' if (tx or ty) else ''
        self._add(f'<g id="{esc(nama)}"{tr}>')
        self.d += 1
        yield self
        self.d -= 1
        self._add('</g>')

    def rect(self, x, y, w, h, fill='none', r=0, stroke=None, sw=1, nama=None, dash=None, op=None):
        a = f'<rect x="{x:g}" y="{y:g}" width="{max(w, 0):g}" height="{max(h, 0):g}"'
        if r: a += f' rx="{r:g}"'
        a += _warna('fill', fill)
        if stroke: a += _warna('stroke', stroke) + f' stroke-width="{sw:g}"'
        if dash: a += f' stroke-dasharray="{dash}"'
        if op is not None: a += f' opacity="{op:g}"'
        if nama: a += f' id="{esc(nama)}"'
        self._add(a + '/>')

    def circle(self, cx, cy, r, fill='none', stroke=None, sw=1, nama=None):
        a = f'<circle cx="{cx:g}" cy="{cy:g}" r="{r:g}"' + _warna('fill', fill)
        if stroke: a += _warna('stroke', stroke) + f' stroke-width="{sw:g}"'
        if nama: a += f' id="{esc(nama)}"'
        self._add(a + '/>')

    def line(self, x1, y1, x2, y2, stroke='#000', sw=1, dash=None, nama=None):
        a = f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}"' + _warna('stroke', stroke) + f' stroke-width="{sw:g}"'
        if dash: a += f' stroke-dasharray="{dash}"'
        if nama: a += f' id="{esc(nama)}"'
        self._add(a + '/>')

    def path(self, d, fill='none', stroke=None, sw=1, nama=None, tx=0, ty=0, scale=1):
        a = f'<path d="{d}"' + _warna('fill', fill)
        if stroke: a += _warna('stroke', stroke) + f' stroke-width="{sw:g}" stroke-linecap="round" stroke-linejoin="round"'
        if tx or ty or scale != 1: a += f' transform="translate({tx:g} {ty:g}) scale({scale:g})"'
        if nama: a += f' id="{esc(nama)}"'
        self._add(a + '/>')

    def text(self, x, y, s, size=14, weight=400, fill='#222', anchor='start', nama=None, ls=None, lh=None, maks=None, italic=False, fam=None):
        """y = baseline baris pertama. maks: bungkus otomatis ke beberapa baris (tspan)."""
        baris = bungkus(s, maks, size, weight, fam) if maks else str(s).split('\n')
        lh = lh or round(size * 1.45)
        a = f'<text x="{x:g}" y="{y:g}" font-family="{fam or self.font}" font-size="{size:g}" font-weight="{weight}"' + _warna('fill', fill)
        if anchor != 'start': a += f' text-anchor="{anchor}"'
        if ls: a += f' letter-spacing="{ls:g}"'
        if italic: a += ' font-style="italic"'
        a += f' id="{esc(nama or str(s)[:40])}">'
        if len(baris) == 1:
            self._add(a + esc(baris[0]) + '</text>')
        else:
            self._add(a + ''.join(f'<tspan x="{x:g}" dy="{0 if i == 0 else lh}">{esc(b)}</tspan>' for i, b in enumerate(baris)) + '</text>')
        return len(baris) * lh

    def ikon(self, nama, x, y, size=24, warna='#222', sw=2):
        self.path(IKON[nama], stroke=warna, sw=sw * 24 / size if size != 24 else sw, nama=f'Ikon/{nama}', tx=x, ty=y, scale=size / 24)

    def svg(self):
        defs, isi_latar = getattr(self, 'defs_extra', ''), self.latar
        if self.gradasi:
            gid = 'gradasi-' + format(__import__('zlib').crc32(self.nama.encode()), 'x')
            stop = ''.join(f'<stop offset="{i / (len(self.gradasi) - 1):g}" stop-color="{c}"/>' for i, c in enumerate(self.gradasi))
            defs += f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">{stop}</linearGradient>'
            isi_latar = f'url(#{gid})'
        defs = f'  <defs>{defs}</defs>\n' if defs else ''
        kepala = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" fill="none">\n' + defs +
                  f'  <g id="{esc(self.nama)}">\n    <rect id="Latar" width="{self.w}" height="{self.h}" fill="{isi_latar}"/>\n')
        return kepala + '\n'.join('  ' + s for s in self.isi) + '\n  </g>\n</svg>\n'
