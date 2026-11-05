"""Membuat src/css/tema-jalur.css: warna setiap jalur diselaraskan di ruang warna OKLCH.
Rona (hue) asli tiap jalur dipertahankan; kecerahan dan kepekatan disamakan agar semua
jalur terasa satu keluarga, dengan kontras teks >= 4.5:1 di mode terang dan gelap.
Jalankan: python3 tools/gen/tema.py"""
import re, math
from pathlib import Path
root = Path(__file__).resolve().parents[2]
v4 = (root / 'src/css/v4.css').read_text()

def srgb2lin(c): return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4
def lin2srgb(c): return 12.92 * c if c <= .0031308 else 1.055 * c ** (1 / 2.4) - .055
def hex2oklch(h):
    r, g, b = (srgb2lin(int(h[i:i + 2], 16) / 255) for i in (1, 3, 5))
    l = (.4122214708 * r + .5363325363 * g + .0514459929 * b) ** (1 / 3)
    m = (.2119034982 * r + .6806995451 * g + .1073969566 * b) ** (1 / 3)
    s = (.0883024619 * r + .2817188376 * g + .6299787005 * b) ** (1 / 3)
    L = .2104542553 * l + .7936177850 * m - .0040720468 * s
    A = 1.9779984951 * l - 2.4285922050 * m + .4505937099 * s
    B = .0259040371 * l + .7827717662 * m - .8086757660 * s
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360
def oklch2hex(L, C, H):
    while True:
        a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
        l = (L + .3963377774 * a + .2158037573 * b) ** 3
        m = (L - .1055613458 * a - .0638541728 * b) ** 3
        s = (L - .0894841775 * a - 1.2914855480 * b) ** 3
        rgb = [4.0767416621 * l - 3.3077115913 * m + .2309699292 * s,
               -1.2684380046 * l + 2.6097574011 * m - .3413193965 * s,
               -.0041960863 * l - .7034186147 * m + 1.7076147010 * s]
        if all(-1e-4 <= c <= 1.0001 for c in rgb) or C < .005:
            return '#' + ''.join(f'{round(max(0, min(1, lin2srgb(max(0, c)))) * 255):02X}' for c in rgb)
        C -= .004
def lum(h): return sum(w * srgb2lin(int(h[i:i + 2], 16) / 255) for w, i in ((.2126, 1), (.7152, 3), (.0722, 5)))
def kontras(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)

# warna terang tiap jalur dari blok :root pertama yang menyebut --c-*
terang = {}
for blok in re.findall(r'(?m)^:root\{([^}]*--c-[^}]*)\}', v4):
    for k, v in re.findall(r'--c-([a-z0-9]+):(#[0-9A-Fa-f]{6})', blok):
        terang.setdefault(k, v)
PERMUKAAN_T, PERMUKAAN_G = '#FFFFFF', '#171A21'
out_t, out_g = [], []
for k, v in sorted(terang.items()):
    L, C, H = hex2oklch(v)
    if C < .03: ct, cg = oklch2hex(.40, .02, H), oklch2hex(.86, .02, H)  # jalur netral (mis. Next.js)
    else: ct, cg = oklch2hex(.50, .125, H), oklch2hex(.80, .105, H)
    assert kontras(ct, PERMUKAAN_T) >= 4.5 and kontras(cg, PERMUKAAN_G) >= 4.5, (k, ct, cg)
    out_t.append(f'--c-{k}:{ct}'); out_g.append(f'--c-{k}:{cg}')
css = ('/* Dibuat oleh tools/gen/tema.py. Warna jalur diselaraskan (OKLCH L .50 / .80). Jangan diedit langsung. */\n'
       ':root{' + ';'.join(out_t) + '}\n'
       '@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){' + ';'.join(out_g) + '}}\n'
       ':root[data-theme="dark"]{' + ';'.join(out_g) + '}\n')
(root / 'src/css/tema-jalur.css').write_text(css)
print(len(terang), 'jalur')
