"""Merender satu kit proyek (dari proyek_data) menjadi kumpulan berkas SVG: hi-fi, wireframe lo-fi, dan papan."""
import svgkit
from svgkit import Tema
from blok import layar_hp, layar_web
import papan as PP
import kk_papan as KP


def tema(spec, fid, gaya=None):
    return Tema(fid, **{**spec['token'], 'gaya': gaya or spec['gaya']})


def render_layar(spec, fid, gaya=None):
    """Mengembalikan [(nama_berkas, svg_str)] untuk semua layar spec pada fidelitas fid."""
    hasil = []
    for i, item in enumerate(spec.get('layar', [])):
        nama, bloks = item[0], item[1]
        opsi = item[2] if len(item) > 2 else {}
        T = tema(spec, fid, gaya)
        label = f'{"HP" if spec["platform"] == "hp" else "Web"}/{i + 1:02d} {nama} ({fid}{", " + gaya if gaya else ""})'
        if spec['platform'] == 'hp':
            s = layar_hp(T, label, bloks, **opsi)
        else:
            s = layar_web(T, label, bloks, sidebar=spec.get('sidebar'))
        slug = f'{i + 1:02d}-' + nama.lower().replace(' ', '-')
        hasil.append((slug, s.svg()))
    return hasil


def kartu_sort(spec):
    s = PP.papan('Riset/Kartu card sorting', 1920, 1240, 'RISET · CARD SORTING', 'Kartu konten untuk card sorting terbuka',
                 '30 kartu. Minta 15 peserta mengelompokkan dan memberi nama kelompok. Analisis matriks kemiripan, lalu susun sitemap.')
    isi = ['Lacak pesanan', 'Kembalikan barang', 'Voucher saya', 'Alamat tersimpan', 'Metode pembayaran', 'Riwayat belanja', 'Wishlist', 'Ulasan saya',
           'Pusat bantuan', 'Chat penjual', 'Promo hari ini', 'Flash sale', 'Kategori elektronik', 'Kategori fesyen', 'Toko favorit', 'Notifikasi',
           'Pengaturan privasi', 'Ubah kata sandi / passkey', 'Bahasa', 'Poin & koin', 'Langganan bulanan', 'Gratis ongkir', 'Bandingkan produk',
           'Ukuran & panduan', 'Faktur pajak', 'Keamanan akun', 'Undang teman', 'Jadi penjual', 'Syarat & ketentuan', 'Hapus akun']
    for i, t in enumerate(isi):
        x, y = 64 + (i % 6) * 300, 240 + (i // 6) * 190
        PP.sticky(s, x, y, 276, 160, f'{i + 1}. {t}', PP.STICKY[i % len(PP.STICKY)], size=18)
    return s


def papan_multibrand(spec):
    s = PP.papan('Design system/Satu komponen, tiga brand', 1920, 900, 'DESIGN SYSTEM · MULTI-BRAND', 'Satu komponen, tiga brand',
                 'Komponen sama persis; hanya token semantik yang berganti. Di Figma: Variables dengan mode per brand.')
    import komponen as K
    for i, tk in enumerate([spec['token']] + spec.get('brand_lain', [])):
        T = Tema('hi', **{**tk, 'gaya': 'modern'})
        x = 64 + i * 620
        PP.kartu(s, x, 240, 592, 600, tk['nama'])
        K.tombol(s, T, x + 28, 320, 260, 48, 'Bayar sekarang')
        K.tombol(s, T, x + 300, 320, 260, 48, 'Batal', 'garis')
        K.masukan(s, T, x + 28, 396, 532, 'Email', 'nama@contoh.id', '', 'fokus', ikon='mail')
        xx = x + 28
        for j, c in enumerate(['Semua', 'Promo', 'Baru']):
            xx += K.chip(s, T, xx, 490, c, j == 0) + 8
        K.badge(s, T, x + 28, 548, 'AKTIF', 'sukses'); K.badge(s, T, x + 100, 548, 'BARU', 'aksen')
        K.radio(s, T, x + 28, 590, 532, 'QRIS', 'Semua e-wallet', True, 'qr')
        K.toast(s, T, x + 28, 676, 532, 'Pembayaran berhasil', 'sukses')
    return s


def render_papan(spec):
    out = []
    for p in spec.get('papan', []):
        if p == 'fondasi':
            out.append(('papan-fondasi', KP.ds_fondasi(spec['token'], spec['token']['nama']).svg()))
            for tk in spec.get('brand_lain', []):
                out.append((f'papan-fondasi-{tk["nama"].lower().replace(" ", "-")}', KP.ds_fondasi(tk, tk['nama']).svg()))
        elif p == 'komponen':
            out.append(('papan-komponen', KP.ds_komponen(spec['token'], spec['token']['nama']).svg()))
        elif p == 'kartu_sort':
            out.append(('papan-kartu-card-sorting', kartu_sort(spec).svg()))
        elif p == 'multibrand':
            out.append(('papan-multi-brand', papan_multibrand(spec).svg()))
    return out
