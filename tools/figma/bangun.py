"""Membangun semua kit desain Figma menjadi ZIP di /desain (dilayani Vercel) + thumbnail untuk pelajaran.
Jalankan: python3 tools/figma/bangun.py   (butuh node + playwright untuk PNG pratinjau)"""
import json, os, pathlib, shutil, subprocess, sys, tempfile, zipfile
sys.path.insert(0, os.path.dirname(__file__))
import svgkit
from svgkit import Tema, IKON, GAYA
import kopikita as KK
import kk_papan as KP
import proyek as PJ
import proyek_data as D
import prototipe

AKAR = pathlib.Path(__file__).resolve().parents[2]
OUT = AKAR / 'desain'
THUMB = pathlib.Path(__file__).resolve().parent / 'thumbs'
TMP = pathlib.Path(tempfile.gettempdir()) / 'rk-desain'
URL = 'https://ruang-kode-nine.vercel.app/desain/'


# ------------------------------------------------------------------ token DTCG 2025.10
def _warna(h):
    h = h.lstrip('#')[:6]
    return {'$type': 'color', '$value': {'colorSpace': 'srgb', 'components': [round(int(h[i:i + 2], 16) / 255, 4) for i in (0, 2, 4)], 'hex': '#' + h.upper()}}


def _dim(v):
    return {'$type': 'dimension', '$value': {'value': v, 'unit': 'px'}}


def dtcg(token, gaya):
    T = Tema('hi', **{**token, 'gaya': gaya})
    t = T.t
    peta = {'action': {'primary': 'primer', 'primary-strong': 'primer2'}, 'accent': {'default': 'aksen'},
            'bg': {'canvas': 'latar', 'surface': 'permukaan', 'subtle': 'lembut'}, 'text': {'primary': 'teks', 'secondary': 'teks2'},
            'border': {'default': 'garis'}, 'feedback': {'success': 'sukses', 'danger': 'bahaya', 'warning': 'peringatan', 'info': 'info'}}
    prim = {k: _warna(t[k]) for k in ('primer', 'primer2', 'aksen', 'latar', 'permukaan', 'lembut', 'teks', 'teks2', 'garis', 'sukses', 'bahaya', 'peringatan', 'info')}
    sem = {g: {n: {'$type': 'color', '$value': '{color.brand.' + k + '}'} for n, k in isi.items()} for g, isi in peta.items()}
    return {
        '$description': f'Token {token["nama"]} · gaya {GAYA[gaya]["label"]} · format DTCG 2025.10 (impor lewat Tokens Studio atau plugin Variables Import).',
        'color': {'brand': prim, **sem},
        'space': {str(v): _dim(v) for v in (4, 8, 12, 16, 24, 32, 48, 64)},
        'radius': {'sm': _dim(6), 'md': _dim(10), 'lg': _dim(T.r), 'full': _dim(999)},
        'font': {'family': {'heading': {'$type': 'fontFamily', '$value': [T.fj, 'system-ui', 'sans-serif']},
                            'body': {'$type': 'fontFamily', '$value': [T.fb, 'system-ui', 'sans-serif']}},
                 'weight': {'regular': {'$type': 'fontWeight', '$value': 400}, 'semibold': {'$type': 'fontWeight', '$value': 600}, 'bold': {'$type': 'fontWeight', '$value': 700}}},
        'typography': {nm: {'$type': 'typography', '$value': {'fontFamily': '{font.family.' + ('heading' if nm.startswith(('display', 'heading')) else 'body') + '}',
                                                                'fontSize': _dim(sz)['$value'], 'fontWeight': wt, 'lineHeight': lh / sz, 'letterSpacing': {'value': 0, 'unit': 'px'}}}
                       for nm, sz, wt, lh in [('display', 40, 800, 48), ('heading-1', 28, 800, 36), ('heading-2', 22, 700, 30), ('heading-3', 18, 700, 26),
                                              ('body-lg', 17, 400, 26), ('body-md', 15, 400, 22), ('label', 14, 600, 20), ('caption', 12, 500, 16)]},
        'motion': {'duration': {k: {'$type': 'duration', '$value': {'value': v, 'unit': 'ms'}} for k, v in (('fast', 100), ('base', 200), ('slow', 300), ('emphasis', 400))},
                   'easing': {'standard': {'$type': 'cubicBezier', '$value': [0.2, 0, 0, 1]}, 'out': {'$type': 'cubicBezier', '$value': [0, 0, 0.2, 1]},
                              'spring': {'$type': 'cubicBezier', '$value': [0.34, 1.56, 0.64, 1]}}},
    }


# ------------------------------------------------------------------ dokumen
FONT_GAYA = lambda g: ['Plus Jakarta Sans'] + GAYA[g].get('fonts', [])


def readme(judul, gaya_list, isi_folder, catatan=''):
    fonts = sorted({f for g in gaya_list for f in FONT_GAYA(g)})
    return f'''# {judul}

Kit desain dari Ruang Kode. Semua file SVG bisa diimpor ke Figma dengan nama layer dan teks yang tetap bisa diedit.

## Isi folder
{isi_folder}

## Langkah impor ke Figma
1. Ekstrak ZIP ini.
2. Pasang font gratis dari Google Fonts: {", ".join(fonts)}. Tanpa font ini Figma memakai font pengganti dan teks akan bergeser.
3. Buka file Figma baru, lalu seret (drag) file `.svg` ke kanvas. Bisa juga lewat menu **File > Place image** atau `Ctrl/Cmd + Shift + K`.
4. Setiap SVG masuk sebagai satu grup. Klik kanan grup itu, pilih **Frame selection** (`Ctrl/Cmd + Alt + G`), lalu beri nama frame sesuai nama file.
5. Nama layer sudah rapi (misalnya `Tombol/Pesan sekarang`, `Input/Nomor HP`, `Ikon/cart`). Lepas grup yang perlu diedit dengan **Ungroup** (`Ctrl/Cmd + Shift + G`).
6. Latihan design system: pilih satu tombol, tekan **Create component** (`Ctrl/Cmd + Alt + K`). Gabungkan state-nya menjadi **Variant** (default, hover, tekan, fokus, nonaktif, memuat).
7. Ubah frame bertumpuk (kartu, daftar, navbar) menjadi **Auto layout** (`Shift + A`) supaya responsif. SVG tidak membawa auto layout, jadi ini bagian dari latihanmu.
8. Token: impor `tokens.json` (format DTCG 2025.10) lewat plugin **Tokens Studio** atau **Variables Import**, lalu hubungkan warna ke Variables.
9. Prototype: buka `prototype/index.html` di browser untuk melihat alur dan animasinya. Tiru di Figma lewat tab **Prototype**: tarik sambungan dari tombol ke frame tujuan, pilih **Smart Animate** dengan durasi dan easing yang sama.
10. Slicing: pakai **Dev Mode** untuk melihat ukuran, warna, dan tipografi. Ekspor ikon dari folder `aset/ikon` (SVG) atau dari layer `Ikon/*`.

## Standar yang dipakai (2026-2030)
- WCAG 2.2 AA: kontras teks >= 4,5:1, target sentuh 48x48 (minimal 24x24), fokus terlihat dan tidak tertutup.
- Token format DTCG 2025.10 (primitif > semantik), siap multi-tema.
- Grid 4/8 pt, tipografi rasio 1,2, motion 100-400 ms dengan dukungan `prefers-reduced-motion`.
- Pola lokal Indonesia: QRIS, OTP/passkey, format Rp dan tanggal DD/MM/YYYY, persetujuan data terpisah (UU PDP).
{catatan}
Lisensi: bebas dipakai untuk belajar dan portofolio. Sebutkan "kit desain Ruang Kode" bila dipublikasikan.
'''


def brief_md(spec):
    gaya = GAYA[spec['gaya']]['label']
    return f'''# Brief: {spec["judul"]}

**Brand:** {spec["token"]["nama"]} · **Platform:** {"Aplikasi HP (390x844)" if spec["platform"] == "hp" else ("Web (1440)" if spec["platform"] == "web" else "Papan desain")} · **Gaya visual:** {gaya} · **Skala:** proyek {spec["tipe"]}

{spec["brief"]}

## Yang harus kamu hasilkan
- Slicing / implementasi yang sama dengan desain hi-fi (selisih maksimal 2px di breakpoint utama).
- Semua state: default, hover, fokus, tekan, nonaktif, memuat, kosong, error.
- Responsif: 360, 768, 1024, 1440 (web) atau 360-430 lebar HP.
- Aksesibilitas WCAG 2.2 AA (cek dengan axe + keyboard).
- Animasi sesuai `prototype/index.html` dan tetap nyaman dengan `prefers-reduced-motion`.

## Kriteria penerimaan
1. Warna, radius, dan tipografi diambil dari `tokens.json`, bukan nilai lepas.
2. Lighthouse Performance dan Accessibility >= 90 di HP.
3. Tidak ada teks di dalam gambar; ikon punya label aksesibel.
4. Tulis studi kasus singkat untuk portofolio: masalah, keputusan desain, hasil.

## Variasi gaya
Folder `variasi-gaya/` berisi layar pertama dalam gaya lain. Struktur sama, hanya token yang berubah. Coba ganti token di kode slicing-mu untuk membuktikan tema bisa diganti tanpa mengubah komponen.
'''


# ------------------------------------------------------------------ util
def tulis(dasar, rel, isi):
    p = dasar / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(isi, bytes):
        p.write_bytes(isi)
    else:
        p.write_text(isi, encoding='utf-8')
    return p


def ikon_svg(nama):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">'
            f'<path id="{nama}" d="{IKON[nama]}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>\n')


def png_batch(daftar):
    if not daftar:
        return
    f = TMP / 'daftar.json'
    f.write_text(json.dumps([[str(a), str(b), s] for a, b, s in daftar]))
    subprocess.run(['node', str(pathlib.Path(__file__).parent / 'render_png.js'), str(f)], check=True, timeout=1800)


def kemas(dasar, nama_zip):
    OUT.mkdir(exist_ok=True)
    z = OUT / nama_zip
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(dasar.rglob('*')):
            if p.is_file():
                zf.write(p, f'{dasar.name}/{p.relative_to(dasar)}')
    return z


def thumb(png, nama, lebar=300):
    from PIL import Image
    THUMB.mkdir(exist_ok=True)
    im = Image.open(png).convert('RGB')
    h = int(im.height * lebar / im.width)
    im = im.resize((lebar, h), Image.LANCZOS)
    if h > lebar * 2.2:
        im = im.crop((0, 0, lebar, int(lebar * 2.2)))
    im.save(THUMB / f'{nama}.webp', 'WEBP', quality=72)


# ------------------------------------------------------------------ kit studi kasus Kopi Kita
def kit_kopikita():
    nama = 'kopi-kita-studi-kasus'
    d = TMP / nama
    shutil.rmtree(d, ignore_errors=True)
    KK.GAYA_AKTIF[0] = 'modern'
    pngs = []
    def simpan(rel, svg, png=True, skala=1):
        p = tulis(d, rel, svg)
        if png:
            q = d / 'png' / (rel.replace('/', '__').replace('.svg', '.png'))
            q.parent.mkdir(parents=True, exist_ok=True)
            pngs.append((p, q, skala))
    for n, f in [('01-persona', KP.persona), ('02-empathy-map', KP.empathy), ('03-journey-map', KP.journey), ('04-problem-statement', KP.masalah)]:
        simpan(f'01-riset/{n}.svg', f().svg(), skala=0.5)
    for n, f in [('01-sitemap', KP.sitemap), ('02-user-flow', KP.userflow)]:
        simpan(f'02-struktur/{n}.svg', f().svg(), skala=0.5)
    nama_hp = ['01-masuk', '02-beranda', '03-menu', '04-detail-produk', '05-keranjang', '06-pembayaran', '07-berhasil']
    nama_state = ['02b-beranda-memuat', '05b-keranjang-kosong', '06b-pembayaran-gagal']
    for fid, folder in (('lo', '03-wireframe-lofi'), ('mid', '04-midfi'), ('hi', '05-hifi')):
        for n, f in zip(nama_hp, KK.LAYAR_HP):
            simpan(f'{folder}/hp/{n}.svg', f(fid).svg(), png=(fid == 'hi'))
        for n, f in zip(nama_state, KK.STATE_HP):
            simpan(f'{folder}/hp/state/{n}.svg', f(fid).svg(), png=(fid == 'hi'))
        simpan(f'{folder}/web/landing-desktop-1440.svg', KK.landing(fid).svg(), png=(fid == 'hi'), skala=0.5)
        simpan(f'{folder}/web/landing-hp-390.svg', KK.landing_hp(fid).svg(), png=(fid == 'hi'))
    simpan('05-hifi/eksplorasi-8-gaya.svg', KP.eksplorasi_gaya().svg(), skala=0.5)
    simpan('05-hifi/peta-interaksi-motion.svg', KP.motion().svg(), skala=0.5)
    for g in [g for g in GAYA if g not in ('wireframe', 'modern', 'manga')]:
        KK.GAYA_AKTIF[0] = g
        simpan(f'05-hifi/variasi-gaya/{g}/02-beranda.svg', KK.beranda('hi').svg(), png=False)
        simpan(f'05-hifi/variasi-gaya/{g}/04-detail-produk.svg', KK.detail('hi').svg(), png=False)
    KK.GAYA_AKTIF[0] = 'modern'
    simpan('06-design-system/01-fondasi.svg', KP.ds_fondasi(KK.TOKEN_KK).svg(), skala=0.5)
    simpan('06-design-system/02-komponen-dan-state.svg', KP.ds_komponen(KK.TOKEN_KK).svg(), skala=0.5)
    tulis(d, '06-design-system/tokens.json', json.dumps(dtcg(KK.TOKEN_KK, 'modern'), indent=2, ensure_ascii=False))
    for g in ('gelap', 'brutal', 'kaca'):
        tulis(d, f'06-design-system/tokens-gaya-{g}.json', json.dumps(dtcg(KK.TOKEN_KK, g), indent=2, ensure_ascii=False))
    simpan('07-handoff/01-redline.svg', KP.redline().svg(), skala=0.5)
    simpan('07-handoff/02-daftar-aset.svg', KP.aset().svg(), skala=0.5)
    for k in IKON:
        tulis(d, f'aset/ikon/{k}.svg', ikon_svg(k))
    # prototype
    lay = []
    trans = [('dissolve', 0, '-', 'Buka aplikasi')] + [(('dissolve' if 'Dissolve' in a else 'instant' if a.startswith('Instant') else 'smart' if a.startswith('Smart Animate (') else 'spring' if 'Spring' in a else 'push'), dur, ez, pm)
                                                      for (_, _, pm, a, dur, ez) in KP.INTERAKSI[:6]]
    for (n, f), (tr, dur, ez, pm) in zip(zip(nama_hp, KK.LAYAR_HP), trans):
        lay.append(dict(nama=n[3:].replace('-', ' ').capitalize(), svg=f('hi').svg(), trans=tr, dur=dur, ease=ez, pemicu=pm, label=prototipe.TRANSISI.get(tr, tr)))
    tulis(d, 'prototype/index.html', prototipe.html('Kopi Kita (pesan ulang)', lay, 'hp', KK.TOKEN_KK['primer']))
    isi = '''- `01-riset/` persona, empathy map, journey map, problem statement
- `02-struktur/` sitemap dan user flow
- `03-wireframe-lofi/`, `04-midfi/`, `05-hifi/` 7 layar HP + 3 state (memuat, kosong, gagal) + landing page desktop & HP
- `05-hifi/eksplorasi-8-gaya.svg` dan `variasi-gaya/` satu layout dalam 8 gaya visual
- `05-hifi/peta-interaksi-motion.svg` sambungan prototype, durasi, easing, mikro-interaksi
- `06-design-system/` fondasi, komponen dengan semua state, `tokens.json` (DTCG) + token gaya alternatif
- `07-handoff/` redline dan daftar aset
- `prototype/index.html` prototype klik-through dengan animasi
- `aset/ikon/` 55 ikon SVG 24px
- `png/` pratinjau'''
    tulis(d, 'README.md', readme('Studi kasus Kopi Kita: dari riset sampai design system', ['modern', 'brutal', 'kaca', 'm3', 'gelap', 'clay', 'editorial', 'retro'], isi))
    png_batch(pngs)
    thumb(d / 'png' / '05-hifi__hp__02-beranda.png', nama)
    for n in ('01-riset__01-persona', '02-struktur__02-user-flow', '06-design-system__02-komponen-dan-state', '07-handoff__01-redline', '05-hifi__eksplorasi-8-gaya', '05-hifi__peta-interaksi-motion', '05-hifi__web__landing-desktop-1440'):
        thumb(d / 'png' / f'{n}.png', f'{nama}--{n.split("__")[-1]}', 360)
    return kemas(d, f'{nama}.zip')


# ------------------------------------------------------------------ kit proyek
def kit_proyek(spec):
    nama = spec['id']
    d = TMP / nama
    shutil.rmtree(d, ignore_errors=True)
    pngs = []
    pertama = None
    for fid, folder in (('hi', 'hifi'), ('lo', 'wireframe-lofi')):
        for slug, svg in PJ.render_layar(spec, fid):
            p = tulis(d, f'{folder}/{slug}.svg', svg)
            if fid == 'hi':
                q = d / 'png' / f'{slug}.png'
                q.parent.mkdir(parents=True, exist_ok=True)
                pngs.append((p, q, 1 if spec['platform'] == 'hp' else 0.5))
                pertama = pertama or q
    if spec.get('varian_gelap'):
        for slug, svg in PJ.render_layar(spec, 'hi', 'gelap'):
            tulis(d, f'hifi/mode-gelap/{slug}.svg', svg)
    for slug, svg in PJ.render_papan(spec):
        p = tulis(d, f'papan/{slug}.svg', svg)
        q = d / 'png' / f'{slug}.png'
        q.parent.mkdir(parents=True, exist_ok=True)
        pngs.append((p, q, 0.5))
        pertama = pertama or q
    if spec.get('layar'):
        alt = [g for g in ('modern', 'brutal', 'kaca', 'm3', 'gelap', 'clay', 'editorial', 'retro') if g != spec['gaya']]
        mulai = sum(ord(c) for c in nama) % len(alt)
        for g in (alt[mulai], alt[(mulai + 3) % len(alt)], alt[(mulai + 5) % len(alt)]):
            slug, svg = PJ.render_layar(spec, 'hi', g)[0]
            tulis(d, f'variasi-gaya/{g}-{slug}.svg', svg)
        lay = []
        for k, (slug, svg) in enumerate(PJ.render_layar(spec, 'hi')):
            lay.append(dict(nama=slug[3:].replace('-', ' ').capitalize(), svg=svg, trans='push' if k else 'dissolve', dur=250 if k else 0, ease='ease-out', label='Push dari kanan' if k else ''))
        tulis(d, 'prototype/index.html', prototipe.html(spec['token']['nama'], lay, 'hp' if spec['platform'] == 'hp' else 'web', spec['token']['primer']))
    tulis(d, 'tokens.json', json.dumps(dtcg(spec['token'], spec['gaya']), indent=2, ensure_ascii=False))
    pakai = set()
    for f in d.rglob('*.svg'):
        t = f.read_text()
        pakai |= {k for k in IKON if f'id="Ikon/{k}"' in t}
    for k in sorted(pakai):
        tulis(d, f'aset/ikon/{k}.svg', ikon_svg(k))
    tulis(d, 'BRIEF.md', brief_md(spec))
    isi = '\n'.join(x for x in [
        '- `BRIEF.md` masalah, yang harus dihasilkan, dan kriteria penerimaan',
        '- `hifi/` desain final siap slicing' if spec.get('layar') else '',
        '- `hifi/mode-gelap/` versi mode gelap' if spec.get('varian_gelap') else '',
        '- `wireframe-lofi/` wireframe untuk latihan menyusun struktur' if spec.get('layar') else '',
        '- `papan/` papan design system / riset' if spec.get('papan') else '',
        '- `variasi-gaya/` layar pertama dalam 3 gaya visual lain' if spec.get('layar') else '',
        '- `prototype/index.html` prototype klik-through + demo mikro-interaksi' if spec.get('layar') else '',
        '- `tokens.json` token DTCG 2025.10', '- `aset/ikon/` ikon SVG yang dipakai', '- `png/` pratinjau'] if x)
    gaya_semua = [spec['gaya'], 'modern', 'brutal', 'kaca', 'm3', 'gelap', 'clay', 'editorial', 'retro']
    tulis(d, 'README.md', readme(f'Kit desain: {spec["judul"]} ({spec["token"]["nama"]})', gaya_semua, isi))
    png_batch(pngs)
    if pertama:
        thumb(pertama, nama)
    return kemas(d, f'{nama}.zip')


def main(hanya=None):
    TMP.mkdir(parents=True, exist_ok=True)
    katalog = []
    if not hanya or 'kopi' in hanya:
        z = kit_kopikita()
        katalog.append(dict(id='kopi-kita-studi-kasus', judul='Studi kasus Kopi Kita', url=URL + z.name, kb=z.stat().st_size // 1024))
    for spec in D.SEMUA:
        if hanya and not any(h in spec['id'] for h in hanya):
            continue
        z = kit_proyek(spec)
        katalog.append(dict(id=spec['id'], judul=spec['judul'], gaya=GAYA[spec['gaya']]['label'], url=URL + z.name, kb=z.stat().st_size // 1024))
        print(spec['id'], z.stat().st_size // 1024, 'KB', flush=True)
    lama = {}
    kp = OUT / 'katalog.json'
    if kp.exists() and hanya:
        lama = {k['id']: k for k in json.loads(kp.read_text())}
    for k in katalog:
        lama[k['id']] = k
    kp.write_text(json.dumps(list(lama.values()), indent=1, ensure_ascii=False))
    print('selesai', len(katalog))


if __name__ == '__main__':
    main(sys.argv[1:] or None)
