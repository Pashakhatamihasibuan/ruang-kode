"""Studi kasus Kopi Kita: aplikasi pemesanan kopi (HP) + landing page (web).
Setiap layar ditulis sekali lalu dirender dalam tiga fidelitas: lo (wireframe), mid, hi (final, gaya bisa diganti: modern, brutal, kaca, m3, gelap, clay, editorial, retro)."""
from svgkit import Svg, Tema, lebar_teks
from komponen import (HP_W, HP_H, para, judul, tombol, masukan, gambar, chip, badge, status_bar, appbar, nav_bawah,
                      stepper, segmen, radio, kartu_produk, baris_list, skeleton, dialog, toast, avatar, langkah_status,
                      navbar_web, footer_web, bayangan, screentone, garis_cepat, gelembung)

TOKEN_KK = dict(primer='#8A4B2A', primer2='#5C2F17', aksen='#FFD23F', latar='#FFFCF5', permukaan='#FFFFFF', teks='#121212',
                teks2='#55504B', garis='#E3D9CE', sukses='#1E7A4C', bahaya='#C8102E', peringatan='#9A6700', info='#1F5FA8',
                lembut='#F6ECDD', radius=14, nama='Kopi Kita', gaya='modern')

MENU = [('Es Kopi Susu Aren', 'Espresso, susu segar, gula aren', 'Rp24.000', '#A66A43', 'Terlaris'),
        ('Kopi Gayo V60', 'Manual brew, notes jeruk & cokelat', 'Rp32.000', '#6E4A33', None),
        ('Caffè Latte', 'Double shot, susu oat tersedia', 'Rp28.000', '#C49A6C', None),
        ('Matcha Latte', 'Matcha Uji, susu segar', 'Rp30.000', '#6F8F4E', 'Baru')]
NAV = [('home', 'Beranda'), ('cup', 'Menu'), ('receipt', 'Pesanan'), ('user', 'Akun')]


GAYA_AKTIF = ['modern']


def T_(fid):
    return Tema(fid, **{**TOKEN_KK, 'gaya': GAYA_AKTIF[0]})


# ================================================================== layar HP
def masuk(fid):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/01 Masuk ({fid})', T.latar)
    status_bar(s, T)
    with s.g('Header'):
        if T.komik:
            garis_cepat(s, 195, 190, 70, 260, 32, '#12121222', 2)
        s.circle(195, 190, 52, T.primer if not T.lo else '#EEE', stroke=T.garis if (T.manga or T.lo) else None, sw=T.sw)
        s.ikon('cup', 167, 162, 56, T.di_atas(T.primer) if not T.lo else '#555', 2)
        judul(s, T, 195, 296, 'Masuk ke Kopi Kita', 26, anchor='middle')
        para(s, T, 195, 328, 'Pesan sebelum sampai, ambil tanpa antre.', 15, 400, T.teks2, anchor='middle')
    y = 372
    y += masukan(s, T, 24, y, 342, 'Nomor HP', '', '0812 3456 7890', ikon='phone', pesan='Kami kirim kode OTP lewat WhatsApp atau SMS')
    tombol(s, T, 24, y + 24, 342, 52, 'Kirim kode OTP')
    with s.g('Pemisah'):
        s.line(24, y + 112, 160, y + 112, T.garis, 1)
        para(s, T, 195, y + 117, 'atau', 13, 500, T.teks2, anchor='middle')
        s.line(230, y + 112, 366, y + 112, T.garis, 1)
    tombol(s, T, 24, y + 140, 342, 52, 'Masuk dengan passkey', 'garis', ikon='lock')
    tombol(s, T, 24, y + 204, 342, 52, 'Lanjut dengan Google', 'garis', ikon='globe')
    para(s, T, 195, 780, 'Dengan masuk, kamu menyetujui Syarat & Ketentuan.', 12, 400, T.teks2, anchor='middle')
    para(s, T, 195, 800, 'Persetujuan data diminta terpisah (UU PDP).', 12, 400, T.teks2, anchor='middle')
    return s


def beranda(fid, memuat=False):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/02 Beranda{" - memuat" if memuat else ""} ({fid})', T.latar)
    status_bar(s, T)
    with s.g('Header'):
        avatar(s, T, 44, 84, 20, 'R')
        para(s, T, 76, 78, 'Selamat pagi,', 13, 400, T.teks2)
        judul(s, T, 76, 100, 'Rina', 18)
        s.circle(346, 84, 20, T.permukaan, stroke=T.garis, sw=T.sw)
        s.ikon('bell', 334, 72, 24, T.teks)
        s.circle(358, 72, 5, T.bahaya if T.hi else '#777')
    with s.g('Pilih outlet'):
        s.rect(24, 124, 342, 52, T.lembut, r=T.r, stroke=T.garis if T.manga else None, sw=T.sw)
        s.ikon('pin', 38, 138, 24, T.primer2 if T.hi else T.teks)
        para(s, T, 72, 146, 'Ambil di outlet', 11, 500, T.teks2)
        s.text(72, 165, 'Gatot Subroto · 1,2 km', 14, 700, T.teks, nama='Outlet')
        s.ikon('down', 334, 138, 20, T.teks)
    with s.g('Pencarian'):
        s.rect(24, 192, 342, 48, T.permukaan, r=24, stroke=T.garis, sw=T.sw)
        s.ikon('search', 40, 204, 22, T.teks2)
        para(s, T, 74, 221, 'Cari kopi, teh, atau roti', 14, 400, T.teks2)
    if memuat:
        with s.g('Skeleton'):
            skeleton(s, 24, 260, 342, 132, T.r)
            for i in range(4): skeleton(s, 24 + i * 86, 412, 74, 34, 17)
            for i in range(2):
                skeleton(s, 24 + i * 179, 470, 163, 146, T.r)
                skeleton(s, 24 + i * 179, 628, 120, 14, 6)
                skeleton(s, 24 + i * 179, 650, 80, 12, 6)
        nav_bawah(s, T, NAV, 0)
        return s
    with s.g('Banner promo'):
        bayangan(s, T, 24, 256, 342, 136, T.r, 5)
        s.rect(24, 256, 342, 136, T.primer if not T.lo else '#EEE', r=T.r, stroke=T.garis if (T.manga or T.lo) else None, sw=T.sw, nama='Latar banner')
        if T.komik:
            garis_cepat(s, 330, 324, 40, 200, 26, '#FFFFFF33', 2)
            screentone(s, 230, 262, 130, 124, 9, 1.6, '#FFFFFF', 0.3)
        wb = T.di_atas(T.primer) if not T.lo else '#333'
        if T.hi: badge(s, T, 44, 276, 'PROMO PAGI', 'aksen')
        judul(s, T, 44, 330, 'Diskon 30% sebelum 08.00', 20, warna=wb, maks=190)
        para(s, T, 44, 376, 'Berlaku untuk semua es kopi', 12, 500, wb)
        gambar(s, T, 248, 276, 100, 96, '#5C2F17', 'Foto promo', r=T.r - 4)
    with s.g('Kategori'):
        x = 24
        for i, (c, ik) in enumerate([('Semua', None), ('Kopi', 'cup'), ('Non-kopi', None), ('Roti', None)]):
            x += chip(s, T, x, 408, c, i == 0) + 8
    with s.g('Section favorit'):
        judul(s, T, 24, 474, 'Favorit pagi ini', 18)
        para(s, T, 366, 474, 'Lihat semua', 13, 700, T.primer if T.hi else T.teks, anchor='end')
        for i, (n, info, h, w, lb) in enumerate(MENU[:2]):
            kartu_produk(s, T, 24 + i * 179, 490, 163, n, info.split(',')[0], h, w, favorit=i == 0, label=lb if T.hi else None)
    nav_bawah(s, T, NAV, 0)
    return s


def menu(fid):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/03 Menu ({fid})', T.latar)
    status_bar(s, T)
    appbar(s, T, 'Menu', None, ('search',))
    with s.g('Tab kategori'):
        x = 24
        for i, c in enumerate(['Kopi', 'Non-kopi', 'Roti', 'Merchandise']):
            x += chip(s, T, x, 108, c, i == 0) + 8
    with s.g('Daftar menu'):
        judul(s, T, 24, 180, 'Kopi', 18)
        para(s, T, 366, 180, '8 menu', 13, 500, T.teks2, anchor='end')
        for i, (n, sub, h, w, lb) in enumerate(MENU + MENU[:1]):
            baris_list(s, T, 24, 200 + i * 104, 342, n if i < 4 else 'Americano', sub if i < 4 else 'Double shot, air panas', h if i < 4 else 'Rp22.000', w)
            if i < 4: s.line(24, 290 + i * 104, 366, 290 + i * 104, T.garis if not T.manga else '#12121222', 1)
    with s.g('Bar keranjang mengambang'):
        bayangan(s, T, 24, 664, 342, 60, T.r, 4)
        s.rect(24, 664, 342, 60, T.primer2 if not T.lo else '#DDD', r=T.r, stroke=T.garis if T.manga else None, sw=T.sw)
        wb = '#FFFFFF' if not T.lo else '#333'
        s.ikon('bag', 42, 682, 24, wb)
        s.text(76, 690, '2 item', 14, 700, wb, nama='Jumlah item')
        s.text(76, 708, 'Ambil 07.45', 12, 400, wb, nama='Waktu ambil')
        s.text(348, 700, 'Rp56.000', 16, 800, wb, 'end', nama='Total')
    nav_bawah(s, T, NAV, 1)
    return s


def detail(fid):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/04 Detail produk ({fid})', T.latar)
    gambar(s, T, 0, 0, HP_W, 330, '#A66A43', 'Foto Es Kopi Susu Aren', r=0)
    status_bar(s, T, gelap=T.hi)
    with s.g('Tombol atas'):
        for x, ik in ((16, 'back'), (330, 'heart')):
            s.circle(x + 22, 72, 22, '#FFFFFF', stroke=T.garis if (T.manga or T.lo) else None, sw=T.sw)
            s.ikon(ik, x + 10, 60, 24, T.teks)
    with s.g('Lembar detail', 0, 300):
        s.rect(0, 0, HP_W, 544, T.latar, r=24, stroke=T.garis if T.manga else None, sw=T.sw, nama='Latar lembar')
        if T.hi: badge(s, T, 24, 24, 'TERLARIS', 'aksen')
        judul(s, T, 24, 80, 'Es Kopi Susu Aren', 24)
        s.text(366, 80, 'Rp24.000', 18, 800, T.primer2 if T.hi else T.teks, 'end', nama='Harga')
        with s.g('Rating'):
            s.ikon('star', 24, 92, 18, '#E0A100' if T.hi else T.teks2)
            para(s, T, 48, 106, '4,9 (1.284 ulasan) · 180 kkal', 13, 500, T.teks2)
        para(s, T, 24, 136, 'Espresso blend Gayo-Toraja, susu segar, dan gula aren cair dari Garut. Manis yang pas untuk pagi.', 14, 400, T.teks2, maks=342)
        judul(s, T, 24, 200, 'Ukuran', 15)
        segmen(s, T, 24, 212, 342, ['Regular', 'Large +5rb'], 0)
        judul(s, T, 24, 286, 'Tingkat manis', 15)
        x = 24
        for i, c in enumerate(['Normal', 'Kurang', 'Tanpa gula']):
            x += chip(s, T, x, 298, c, i == 1) + 8
        judul(s, T, 24, 364, 'Catatan', 15)
        with s.g('Input catatan'):
            s.rect(24, 376, 342, 44, T.permukaan, r=10, stroke=T.garis, sw=T.sw)
            para(s, T, 40, 404, 'Contoh: es dipisah', 14, 400, T.teks2)
        s.line(0, 444, HP_W, 444, T.garis if not T.manga else '#12121222', 1)
        stepper(s, T, 24, 466, 1)
        tombol(s, T, 144, 460, 222, 48, 'Tambah · Rp24.000')
    return s


def keranjang(fid, kosong=False):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/05 Keranjang{" - kosong" if kosong else ""} ({fid})', T.latar)
    status_bar(s, T)
    appbar(s, T, 'Keranjang', 'back')
    if kosong:
        with s.g('Empty state'):
            if T.komik: garis_cepat(s, 195, 300, 70, 190, 30, '#12121222', 2)
            s.circle(195, 300, 64, T.lembut, stroke=T.garis if T.manga else None, sw=T.sw)
            s.ikon('bag', 159, 264, 72, T.primer2 if T.hi else T.teks2, 2)
            if T.komik: gelembung(s, T, 236, 196, 120, 44, 'bawah-kiri')
            if T.komik: s.text(296, 224, 'Kosong!', 15, 400, T.teks, 'middle', nama='Teks balon', fam=T.fj)
            judul(s, T, 195, 410, 'Keranjangmu masih kosong', 20, anchor='middle')
            para(s, T, 195, 440, 'Pilih kopi favoritmu dan pesan sebelum', 14, 400, T.teks2, anchor='middle')
            para(s, T, 195, 460, 'berangkat. Ambil tanpa antre.', 14, 400, T.teks2, anchor='middle')
            tombol(s, T, 95, 492, 200, 48, 'Lihat menu')
        return s
    with s.g('Item'):
        for i, (n, sub, h, w, lb) in enumerate(MENU[:2]):
            baris_list(s, T, 24, 120 + i * 108, 342, n, 'Regular · kurang manis' if i == 0 else 'Hot · tanpa catatan', h, w, aksi='stepper')
        s.line(24, 334, 366, 334, T.garis, 1)
    with s.g('Waktu ambil'):
        judul(s, T, 24, 368, 'Waktu ambil', 16)
        x = 24
        for i, c in enumerate(['Secepatnya (10 mnt)', '07.45', '08.00']):
            x += chip(s, T, x, 382, c, i == 1, ikon='clock' if i == 0 else None) + 8
    with s.g('Ringkasan'):
        s.rect(24, 440, 342, 156, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw)
        for i, (k, v) in enumerate([('Subtotal', 'Rp56.000'), ('Promo pagi 30%', '-Rp7.200'), ('Biaya layanan', 'Rp1.000')]):
            para(s, T, 40, 474 + i * 28, k, 14, 400, T.teks2)
            s.text(350, 474 + i * 28, v, 14, 600, T.sukses if (i == 1 and T.hi) else T.teks, 'end', nama=k)
        s.line(40, 552, 350, 552, T.garis if not T.manga else '#12121233', 1, dash='4 4')
        judul(s, T, 40, 580, 'Total', 16)
        s.text(350, 580, 'Rp49.800', 18, 800, T.teks, 'end', nama='Total')
    with s.g('CTA bawah', 0, 720):
        s.rect(0, 0, HP_W, 124, T.permukaan, stroke=T.garis if T.manga else None, sw=T.sw)
        tombol(s, T, 24, 20, 342, 52, 'Lanjut ke pembayaran')
    return s


def bayar(fid, gagal=False):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/06 Pembayaran{" - gagal" if gagal else ""} ({fid})', T.latar)
    status_bar(s, T)
    appbar(s, T, 'Pembayaran', 'back')
    with s.g('Metode bayar'):
        judul(s, T, 24, 130, 'Pilih metode', 16)
        for i, (n, sub, ik) in enumerate([('QRIS', 'Semua e-wallet & m-banking', 'qr'), ('GoPay', 'Saldo Rp120.500', 'wallet'),
                                          ('OVO', 'Hubungkan akun', 'wallet'), ('Kartu debit/kredit', 'Visa, Mastercard, GPN', 'card')]):
            radio(s, T, 24, 146 + i * 76, 342, n, sub, i == 0, ik)
    with s.g('Info'):
        s.rect(24, 462, 342, 64, T.lembut, r=T.r)
        s.ikon('shield', 38, 482, 24, T.sukses if T.hi else T.teks)
        para(s, T, 72, 490, 'Pembayaran diproses oleh mitra berizin', 13, 600, T.teks)
        para(s, T, 72, 510, 'Bank Indonesia. Data kartu tidak disimpan.', 12, 400, T.teks2)
    with s.g('CTA bawah', 0, 700):
        s.rect(0, 0, HP_W, 144, T.permukaan, stroke=T.garis if T.manga else None, sw=T.sw)
        para(s, T, 24, 36, 'Total bayar', 13, 400, T.teks2)
        s.text(24, 62, 'Rp49.800', 22, 800, T.teks, nama='Total')
        tombol(s, T, 184, 20, 182, 52, 'Bayar sekarang')
    if gagal:
        s.rect(0, 0, HP_W, HP_H, '#12121299', nama='Scrim')
        dialog(s, T, 32, 300, 326, 'Pembayaran gagal', 'Saldo tidak cukup. Coba metode lain.', 'Pilih metode lain', 'Coba lagi')
    return s


def berhasil(fid):
    T = T_(fid); s = Svg(HP_W, HP_H, f'HP/07 Pesanan berhasil ({fid})', T.latar)
    status_bar(s, T)
    with s.g('Hero sukses'):
        if T.komik:
            garis_cepat(s, 195, 190, 80, 300, 40, '#12121226', 2)
        s.circle(195, 190, 58, T.sukses if not T.lo else '#EEE', stroke=T.garis if (T.manga or T.lo) else None, sw=T.sw)
        s.ikon('check', 159, 154, 72, '#FFFFFF' if not T.lo else '#555', 2)
        if T.komik:
            gelembung(s, T, 246, 96, 124, 46, 'bawah-kiri')
            s.text(308, 125, 'Yosh!', 16, 400, T.teks, 'middle', nama='Teks balon', fam=T.fj)
        judul(s, T, 195, 300, 'Pesanan diterima!', 26, anchor='middle')
        para(s, T, 195, 330, 'Barista mulai menyiapkan kopimu.', 15, 400, T.teks2, anchor='middle')
    with s.g('Kartu antrean'):
        bayangan(s, T, 24, 360, 342, 150, T.r, 5)
        s.rect(24, 360, 342, 150, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw)
        para(s, T, 195, 392, 'Nomor ambil', 13, 500, T.teks2, anchor='middle')
        judul(s, T, 195, 448, 'A-27', 48, anchor='middle', warna=T.primer2 if T.hi else T.teks)
        para(s, T, 195, 488, 'Siap sekitar 07.45 · Outlet Gatot Subroto', 13, 500, T.teks2, anchor='middle')
    langkah_status(s, T, 40, 540, 310, ['Diterima', 'Disiapkan', 'Siap', 'Diambil'], 0)
    tombol(s, T, 24, 690, 342, 52, 'Lacak pesanan')
    tombol(s, T, 24, 752, 342, 44, 'Kembali ke beranda', 'teks')
    return s


LAYAR_HP = [masuk, beranda, menu, detail, keranjang, bayar, berhasil]
STATE_HP = [lambda f: beranda(f, memuat=True), lambda f: keranjang(f, kosong=True), lambda f: bayar(f, gagal=True)]


# ================================================================== landing page web
def landing(fid, w=1440):
    T = T_(fid)
    H = 3320
    s = Svg(w, H, f'Web/Landing page desktop ({fid})', T.latar)
    navbar_web(s, T, w, ['Beranda', 'Menu', 'Cara pesan', 'Outlet', 'Langganan'], 'Pesan sekarang')
    with s.g('Hero', 0, 80):
        if T.komik:
            garis_cepat(s, 1040, 330, 180, 760, 48, '#1212121F', 2.5)
        if T.hi: badge(s, T, 120, 104, 'ROASTERY MEDAN SEJAK 2019', 'aksen')
        judul(s, T, 120, 210, 'Kopi Nusantara, dipanggang setiap minggu', 60, maks=600)
        para(s, T, 120, 400, 'Pesan dari aplikasi sebelum berangkat, ambil di outlet tanpa antre. Biji pilihan dari Gayo, Toraja, dan Kintamani.', 20, 400, T.teks2, maks=540, lh=32)
        tombol(s, T, 120, 486, 200, 56, 'Lihat menu')
        tombol(s, T, 336, 486, 200, 56, 'Unduh aplikasi', 'garis', ikon='download')
        with s.g('Bukti sosial'):
            for i in range(3):
                avatar(s, T, 140 + i * 30, 600, 20, 'RBD'[i], ['#F6C28B', '#E9B872', '#D9A066'][i] if T.hi else None)
            para(s, T, 216, 596, '4,9 dari 12.000+ pelanggan', 15, 700, T.teks)
            para(s, T, 216, 618, 'Rating rata-rata di App Store dan Google Play', 13, 400, T.teks2)
        bayangan(s, T, 760, 40, 560, 600, 28, 8)
        gambar(s, T, 760, 40, 560, 600, '#8A4B2A', 'Foto hero: es kopi susu aren', r=28)
        if T.komik:
            gelembung(s, T, 700, 470, 230, 70, 'bawah-kanan', 'Balon testimoni')
            s.text(815, 512, 'Ga pakai antre!', 18, 400, T.teks, 'middle', nama='Teks balon', fam=T.fj)
    with s.g('Keunggulan', 0, 820):
        s.rect(0, 0, w, 360, T.lembut if not T.lo else '#F7F7F7', nama='Latar section')
        judul(s, T, w / 2, 96, 'Kenapa pesan di Kopi Kita?', 36, anchor='middle')
        for i, (ik, jd, isi) in enumerate([('clock', 'Ambil tanpa antre', 'Pesan dari kantor, kopi siap saat kamu tiba. Rata-rata hemat 12 menit.'),
                                           ('cup', 'Biji segar mingguan', 'Dipanggang di Medan setiap Senin, tidak lebih dari 14 hari di rak.'),
                                           ('qr', 'Bayar sekali sentuh', 'QRIS, e-wallet, dan kartu. Struk digital langsung masuk aplikasi.')]):
            x = 120 + i * 412
            with s.g(f'Fitur/{jd}'):
                bayangan(s, T, x, 140, 376, 176, T.r, 5)
                s.rect(x, 140, 376, 176, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw)
                s.circle(x + 52, 196, 28, T.aksen if T.hi else '#E0E0E0', stroke=T.garis if T.manga else None, sw=T.sw)
                s.ikon(ik, x + 38, 182, 28, T.teks)
                judul(s, T, x + 100, 204, jd, 20)
                para(s, T, x + 32, 260, isi, 15, 400, T.teks2, maks=312, lh=24)
    with s.g('Menu favorit', 0, 1180):
        judul(s, T, 120, 120, 'Menu favorit minggu ini', 36)
        para(s, T, w - 120, 120, 'Lihat semua menu', 16, 700, T.primer if T.hi else T.teks, anchor='end')
        for i, (n, info, h, wr, lb) in enumerate(MENU[:4]):
            kartu_produk(s, T, 120 + i * 306, 160, 282, n, info, h, wr, label=lb if T.hi else None)
    with s.g('Cara pesan', 0, 1700):
        judul(s, T, w / 2, 100, 'Pesan dalam 3 langkah', 36, anchor='middle')
        for i, (jd, isi) in enumerate([('Pilih menu', 'Atur ukuran, tingkat manis, dan catatan.'), ('Bayar', 'QRIS atau e-wallet, aman dan cepat.'), ('Ambil', 'Tunjukkan nomor ambil di outlet.')]):
            x = 120 + i * 412
            with s.g(f'Langkah {i + 1}'):
                s.circle(x + 188, 200, 44, T.primer if not T.lo else '#EEE', stroke=T.garis if (T.manga or T.lo) else None, sw=T.sw)
                judul(s, T, x + 188, 216, str(i + 1), 36, anchor='middle', warna=T.di_atas(T.primer) if not T.lo else '#444')
                judul(s, T, x + 188, 290, jd, 22, anchor='middle')
                para(s, T, x + 188, 322, isi, 15, 400, T.teks2, anchor='middle')
                if i < 2: s.line(x + 250, 200, x + 538, 200, T.garis, 2 if T.manga else 1, dash='6 8')
    with s.g('Testimoni', 0, 2100):
        s.rect(0, 0, w, 420, T.lembut if not T.lo else '#F7F7F7')
        judul(s, T, w / 2, 96, 'Kata pelanggan', 36, anchor='middle')
        for i, (nm, kt, ps) in enumerate([('Rina, Medan', 'Pesan dari lift, turun langsung ambil. Tidak telat absen lagi.', 'R'),
                                          ('Budi, Binjai', 'Kopi Gayo V60-nya konsisten enak. Struk digital memudahkan reimburse.', 'B'),
                                          ('Dewi, Medan', 'Fitur pilih tingkat manis itu penting buat saya. Mantap!', 'D')]):
            x = 120 + i * 412
            with s.g(f'Testimoni/{nm}'):
                if T.komik:
                    gelembung(s, T, x, 140, 376, 150, 'bawah-kiri')
                else:
                    s.rect(x, 140, 376, 150, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw)
                para(s, T, x + 28, 186, kt, 16, 400, T.teks, maks=320, lh=26)
                avatar(s, T, x + 48, 340, 22, ps)
                s.text(x + 82, 346, nm, 15, 700, T.teks, nama='Nama')
    with s.g('CTA aplikasi', 0, 2560):
        bayangan(s, T, 120, 0, w - 240, 260, 28, 8)
        s.rect(120, 0, w - 240, 260, T.primer2 if not T.lo else '#EEE', r=28, stroke=T.garis if (T.manga or T.lo) else None, sw=T.sw)
        if T.komik:
            screentone(s, 900, 10, 400, 240, 12, 2, '#FFFFFF', 0.25)
        wb = '#FFFFFF' if not T.lo else '#333'
        judul(s, T, 200, 110, 'Unduh aplikasinya, dapat diskon 30%', 36, warna=wb, maks=640)
        para(s, T, 200, 200, 'Untuk 3 pesanan pertama. Tersedia di Android dan iOS.', 17, 400, wb)
        tombol(s, T, w - 480, 104, 280, 56, 'Unduh di Google Play', 'garis', ikon='download')
    footer_web(s, T, w, H - 280, [('Produk', ['Menu', 'Biji kopi', 'Langganan']), ('Perusahaan', ['Tentang', 'Karier', 'Outlet']), ('Bantuan', ['FAQ', 'Kontak', 'Kebijakan privasi'])],
               '© 2026 Kopi Kita · Jl. Gatot Subroto 12, Medan')
    return s


def landing_hp(fid='hi'):
    T = T_(fid); s = Svg(HP_W, 1900, f'Web/Landing page mobile ({fid})', T.latar)
    with s.g('Navbar'):
        s.rect(0, 0, HP_W, 64, T.permukaan, stroke=T.garis if T.manga else None, sw=T.sw)
        s.circle(36, 32, 16, T.primer)
        s.ikon('cup', 26, 22, 20, '#FFFFFF')
        judul(s, T, 60, 39, 'Kopi Kita', 18)
        s.ikon('menu', 342, 20, 24, T.teks)
    with s.g('Hero', 0, 64):
        if T.komik: garis_cepat(s, 195, 420, 80, 420, 36, '#1212121A', 2)
        if T.hi: badge(s, T, 20, 32, 'ROASTERY MEDAN SEJAK 2019', 'aksen')
        judul(s, T, 20, 104, 'Kopi Nusantara, dipanggang setiap minggu', 32, maks=340)
        para(s, T, 20, 254, 'Pesan sebelum berangkat, ambil tanpa antre.', 16, 400, T.teks2, maks=340)
        tombol(s, T, 20, 290, 350, 52, 'Lihat menu')
        tombol(s, T, 20, 354, 350, 52, 'Unduh aplikasi', 'garis', ikon='download')
        bayangan(s, T, 20, 432, 350, 300, 20, 6)
        gambar(s, T, 20, 432, 350, 300, '#8A4B2A', 'Foto hero', r=20)
    with s.g('Keunggulan', 0, 840):
        judul(s, T, 20, 40, 'Kenapa Kopi Kita?', 26)
        for i, (ik, jd, isi) in enumerate([('clock', 'Ambil tanpa antre', 'Hemat rata-rata 12 menit.'), ('cup', 'Biji segar mingguan', 'Dipanggang setiap Senin.'), ('qr', 'Bayar sekali sentuh', 'QRIS, e-wallet, kartu.')]):
            y = 64 + i * 100
            with s.g(f'Fitur/{jd}'):
                bayangan(s, T, 20, y, 350, 84, T.r, 4)
                s.rect(20, y, 350, 84, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw)
                s.circle(60, y + 42, 22, T.aksen, stroke=T.garis if T.manga else None, sw=T.sw)
                s.ikon(ik, 48, y + 30, 24, T.teks)
                s.text(96, y + 38, jd, 16, 700, T.teks, nama='Judul')
                para(s, T, 96, y + 60, isi, 13, 400, T.teks2)
    with s.g('Menu favorit', 0, 1220):
        judul(s, T, 20, 40, 'Menu favorit', 26)
        for i, (n, info, h, wr, lb) in enumerate(MENU[:2]):
            kartu_produk(s, T, 20 + i * 179, 64, 171, n, info.split(',')[0], h, wr, label=lb)
    footer = Tema('hi', **TOKEN_KK)
    with s.g('Footer', 0, 1620):
        s.rect(0, 0, HP_W, 280, '#2B2724' if not T.manga else T.garis)
        s.text(20, 56, 'Kopi Kita', 20, 400, '#FFFFFF', nama='Brand', fam=T.fj)
        for i, t in enumerate(['Menu', 'Outlet', 'Langganan', 'Kebijakan privasi']):
            s.text(20, 100 + i * 30, t, 14, 400, '#CFC6BE', nama=t)
        s.text(20, 250, '© 2026 Kopi Kita', 12, 400, '#CFC6BE', nama='Hak cipta')
    return s
