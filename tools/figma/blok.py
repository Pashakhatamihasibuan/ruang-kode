"""Pustaka blok layar untuk kit proyek. Setiap layar = daftar blok berurutan; satu fungsi menggambar satu blok
dan mengembalikan tingginya. Layar HP 390x844, layar web lebar 1440 (atau 1280 untuk dashboard) dengan tinggi otomatis."""
from svgkit import Svg, Tema, lebar_teks, campur
from komponen import (HP_W, HP_H, para, judul, tombol, masukan, gambar, chip, badge, status_bar, appbar, nav_bawah,
                      stepper, segmen, radio, kartu_produk, baris_list, skeleton, dialog, toast, avatar, langkah_status,
                      bayangan)


def _kartu(s, T, x, y, w, h, nama='Kartu', isi=None):
    bayangan(s, T, x, y, w, h, T.r, 4)
    s.rect(x, y, w, h, isi or T.permukaan, r=T.r, stroke=T.garis, sw=T.sw, nama=nama)


# ================================================================== blok HP (x 24..366)
def h_appbar(s, T, y, judul_teks, kiri='back', kanan=()):
    appbar(s, T, judul_teks, kiri, tuple(kanan), y=y)
    return 56


def h_sapaan(s, T, y, nama, sub, ikon='bell', inisial=None):
    with s.g('Header sapaan', 0, y):
        avatar(s, T, 44, 28, 20, inisial or nama[0])
        para(s, T, 76, 22, sub, 13, 400, T.teks2)
        judul(s, T, 76, 44, nama, 18)
        s.circle(346, 28, 20, T.permukaan, stroke=T.garis, sw=T.sw)
        s.ikon(ikon, 334, 16, 24, T.teks)
    return 68


def h_judul(s, T, y, teks, sub=None, besar=False):
    with s.g(f'Judul/{teks[:24]}', 0, y):
        judul(s, T, 24, 26 if besar else 22, teks, 26 if besar else 18, maks=342)
        if sub:
            para(s, T, 24, 52 if besar else 44, sub, 14, 400, T.teks2, maks=342)
    return (64 if besar else 34) + (24 if sub else 0)


def h_bagian(s, T, y, teks, link='Lihat semua'):
    with s.g(f'Bagian/{teks}', 0, y):
        judul(s, T, 24, 20, teks, 17)
        if link:
            para(s, T, 366, 20, link, 13, 700, T.primer if T.hi else T.teks, anchor='end')
    return 36


def h_saldo(s, T, y, label, nilai, sub=None, aksi=(('send', 'Kirim'), ('download', 'Isi'), ('qr', 'Bayar'), ('chart', 'Laporan'))):
    with s.g('Kartu ringkasan', 0, y):
        bayangan(s, T, 24, 0, 342, 176, T.r, 5)
        isi = T.primer if not T.lo else '#EEE'
        s.rect(24, 0, 342, 176, isi, r=T.r, stroke=T.garis if (T.tinta or T.lo) else None, sw=T.sw, nama='Latar kartu')
        wt = T.di_atas(isi) if not T.lo else '#444'
        para(s, T, 44, 34, label, 13, 500, wt)
        s.text(44, 72, nilai, 28, 800, wt, nama='Nilai', fam=T.fj if T.hi else None)
        if sub:
            para(s, T, 44, 96, sub, 12, 500, wt)
        for i, (ik, lb) in enumerate(aksi):
            cx = 64 + i * 82
            s.circle(cx, 132, 18, '#FFFFFF33' if not T.lo else '#DDD')
            s.ikon(ik, cx - 10, 122, 20, wt)
            para(s, T, cx, 166, lb, 11, 600, wt, anchor='middle')
    return 192


def h_cari(s, T, y, placeholder='Cari', filter=True):
    with s.g('Pencarian', 0, y):
        s.rect(24, 0, 342 - (56 if filter else 0), 48, T.permukaan, r=min(T.r, 24), stroke=T.garis, sw=T.sw)
        s.ikon('search', 40, 12, 24, T.teks2)
        para(s, T, 74, 30, placeholder, 14, 400, T.teks2)
        if filter:
            s.rect(318, 0, 48, 48, T.lembut, r=min(T.r, 24), stroke=T.garis if T.tinta else None, sw=T.sw)
            s.ikon('filter', 330, 12, 24, T.teks)
    return 64


def h_chips(s, T, y, items, aktif=0):
    with s.g('Filter chip', 0, y):
        x = 24
        for i, c in enumerate(items):
            if x > 330: break
            x += chip(s, T, x, 0, c, i == aktif) + 8
    return 50


def h_banner(s, T, y, jd, sub, ikon='sparkle', label=None):
    with s.g('Banner', 0, y):
        bayangan(s, T, 24, 0, 342, 120, T.r, 5)
        isi = T.lembut if not T.lo else '#EEE'
        s.rect(24, 0, 342, 120, isi, r=T.r, stroke=T.garis if (T.tinta or T.lo) else None, sw=T.sw)
        if label and T.hi: badge(s, T, 44, 18, label, 'aksen')
        judul(s, T, 44, 64 if label else 48, jd, 18, maks=220)
        para(s, T, 44, 92 if label else 76, sub, 12, 400, T.teks2, maks=220)
        s.circle(316, 60, 34, T.aksen if T.hi else '#DDD')
        s.ikon(ikon, 296, 40, 40, T.di_atas(T.aksen) if T.hi else '#555')
    return 136


def h_list(s, T, y, items, gaya='ikon'):
    """items: (judul, sub, kanan, warna, ikon). gaya 'ikon' (ikon dalam lingkaran) atau 'foto'."""
    with s.g('Daftar', 0, y):
        yy = 0
        for i, (jd, sub, kanan, warna, ik) in enumerate(items):
            with s.g(f'Baris/{jd}'):
                if gaya == 'foto':
                    gambar(s, T, 24, yy, 64, 64, warna, 'Foto', f'ikon:{ik}', r=T.r - 2)
                else:
                    s.rect(24, yy + 6, 52, 52, campur(warna, '#FFFFFF', 0.82) if T.hi else '#EEE', r=min(T.r, 26))
                    s.ikon(ik, 38, yy + 20, 24, warna if T.hi else '#555')
                s.text(96, yy + 28, jd, 15, 700, T.teks, nama='Judul')
                para(s, T, 96, yy + 50, sub, 12, 400, T.teks2, maks=180)
                if kanan:
                    warna_k = T.sukses if kanan.startswith('+') and T.hi else (T.bahaya if kanan.startswith('-') and T.hi else T.teks)
                    s.text(366, yy + 38, kanan, 15, 700, warna_k, 'end', nama='Nilai')
                if i < len(items) - 1:
                    s.line(96, yy + 74, 366, yy + 74, T.garis if not T.tinta else T.garis + '33', 1)
            yy += 82
    return yy + 4


def h_grid(s, T, y, items):
    """Grid produk 2 kolom. items: (nama, info, harga, warna, ikon, label)."""
    with s.g('Grid produk', 0, y):
        tinggi = 0
        for i, (n, info, h, w, ik, lb) in enumerate(items[:4]):
            x = 24 + (i % 2) * 179
            yy = (i // 2) * 268
            with s.g(f'Kartu/{n}'):
                bayangan(s, T, x, yy, 163, 252, T.r, 4)
                s.rect(x, yy, 163, 252, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw)
                gambar(s, T, x + 8, yy + 8, 147, 132, w, 'Foto ' + n, f'ikon:{ik}', r=T.r - 4)
                if lb and T.hi: badge(s, T, x + 16, yy + 16, lb, 'aksen')
                s.text(x + 12, yy + 164, n, 14, 700, T.teks, nama='Nama', maks=139)
                para(s, T, x + 12, yy + 204, info, 12, 400, T.teks2, maks=139)
                s.text(x + 12, yy + 236, h, 15, 800, T.primer2 if T.hi else T.teks, nama='Harga')
            tinggi = yy + 268
    return tinggi


def h_form(s, T, y, fields, cta=None, cta2=None):
    """fields: (label, nilai, placeholder, state, pesan, ikon)."""
    with s.g('Formulir', 0, y):
        yy = 0
        for lb, nil, ph, st, ps, ik in fields:
            yy += masukan(s, T, 24, yy, 342, lb, nil, ph, st, ps, ik) + 14
        if cta:
            tombol(s, T, 24, yy + 6, 342, 52, cta)
            yy += 66
        if cta2:
            tombol(s, T, 24, yy + 4, 342, 48, cta2, 'garis')
            yy += 60
    return yy + 8


def h_langkah(s, T, y, langkah, aktif):
    with s.g('Langkah', 0, y):
        langkah_status(s, T, 24, 0, 342, langkah, aktif)
    return 68


def h_peta(s, T, y, h=300, label='Lokasi'):
    with s.g('Peta', 0, y):
        gambar(s, T, 0, 0, HP_W, h, '#7FA88B' if T.hi else '#CCC', label, 'peta', r=0)
    return h


def h_chat(s, T, y, pesan, h=520):
    """pesan: (siapa, teks); siapa 'saya' di kanan, lainnya di kiri."""
    with s.g('Percakapan', 0, y):
        yy = 8
        for siapa, t in pesan:
            from svgkit import bungkus
            baris = bungkus(t, 236, 14)
            bh = len(baris) * 20 + 24
            lw = min(max(lebar_teks(b, 14) for b in baris) + 28, 264)
            kanan = siapa == 'saya'
            x = 366 - lw if kanan else 24 + (0 if siapa == '' else 0)
            isi = (T.primer if kanan else T.permukaan) if not T.lo else ('#E0E0E0' if kanan else '#FFF')
            s.rect(x, yy, lw, bh, isi, r=min(T.r + 4, 18), stroke=None if kanan else T.garis, sw=T.sw, nama=f'Balon/{siapa or "lawan"}')
            s.text(x + 14, yy + 26, t, 14, 400, T.di_atas(isi) if (kanan and not T.lo) else T.teks, maks=236, lh=20, nama='Pesan')
            yy += bh + 12
            if yy > h - 40: break
    return h


def h_masukan_chat(s, T, y, placeholder='Tulis pesan'):
    with s.g('Input pesan', 0, y):
        s.rect(24, 0, 286, 48, T.permukaan, r=24, stroke=T.garis, sw=T.sw)
        para(s, T, 44, 30, placeholder, 14, 400, T.teks2)
        s.circle(342, 24, 24, T.primer if not T.lo else '#DDD')
        s.ikon('send', 330, 12, 24, T.di_atas(T.primer) if not T.lo else '#444')
    return 60


def h_ringkas(s, T, y, baris, total=None):
    """Kartu ringkasan biaya/detail: baris (label, nilai)."""
    tinggi = 32 + len(baris) * 30 + (48 if total else 0)
    with s.g('Ringkasan', 0, y):
        _kartu(s, T, 24, 0, 342, tinggi)
        for i, (k, v) in enumerate(baris):
            para(s, T, 44, 36 + i * 30, k, 14, 400, T.teks2)
            s.text(346, 36 + i * 30, v, 14, 600, T.teks, 'end', nama=k)
        if total:
            yy = 36 + len(baris) * 30
            s.line(44, yy - 8, 346, yy - 8, T.garis, 1, dash='4 4')
            judul(s, T, 44, yy + 22, total[0], 16)
            s.text(346, yy + 22, total[1], 18, 800, T.teks, 'end', nama='Total')
    return tinggi + 16


def h_grafik(s, T, y, jd, data, label=None):
    with s.g('Grafik', 0, y):
        _kartu(s, T, 24, 0, 342, 200)
        judul(s, T, 44, 34, jd, 15)
        mx, mn = max(data), min(data)
        lo = mn - (mx - mn) * 0.6 if (mx - mn) / mx < 0.2 else 0   # rentang sempit: sumbu tidak dari nol (beri label)
        bw = 260 / len(data)
        for i, v in enumerate(data):
            h = 110 * (v - lo) / (mx - lo)
            s.rect(56 + i * bw, 170 - h, bw * 0.6, h, (T.primer if i == len(data) - 1 else campur(T.primer, '#FFFFFF', 0.6)) if T.hi else '#CCC', r=4, nama=f'Batang {i + 1}')
        if label:
            for i, l in enumerate(label):
                para(s, T, 56 + i * bw + bw * 0.3, 190, l, 10, 500, T.teks2, anchor='middle')
    return 216


def h_slot(s, T, y, jd, slot, aktif=0):
    with s.g('Slot waktu', 0, y):
        judul(s, T, 24, 18, jd, 15)
        for i, t in enumerate(slot[:8]):
            x, yy = 24 + (i % 4) * 87, 32 + (i // 4) * 50
            on = i == aktif
            s.rect(x, yy, 79, 40, (T.primer if on else T.permukaan) if not T.lo else ('#DDD' if on else '#FFF'), r=min(T.r, 12), stroke=None if on else T.garis, sw=T.sw)
            s.text(x + 39.5, yy + 25, t, 13, 700 if on else 500, T.di_atas(T.primer) if (on and not T.lo) else T.teks, 'middle', nama=f'Slot/{t}')
    return 32 + ((len(slot[:8]) + 3) // 4) * 50 + 8


def h_segmen(s, T, y, opsi, aktif=0):
    segmen(s, T, 24, y, 342, opsi, aktif)
    return 56


def h_tombol_bawah(s, T, label, label2=None, info=None):
    with s.g('CTA bawah', 0, HP_H - 112):
        s.rect(0, 0, HP_W, 112, T.permukaan, stroke=T.garis if T.tinta else None, sw=T.sw)
        s.line(0, 0, HP_W, 0, T.garis, 1)
        if info:
            para(s, T, 24, 30, info[0], 12, 400, T.teks2)
            s.text(24, 56, info[1], 18, 800, T.teks, nama='Nilai')
            tombol(s, T, 186, 18, 180, 52, label)
        elif label2:
            tombol(s, T, 24, 18, 160, 52, label2, 'garis')
            tombol(s, T, 196, 18, 170, 52, label)
        else:
            tombol(s, T, 24, 18, 342, 52, label)
        s.rect(HP_W / 2 - 67, 99, 134, 5, T.teks, r=2.5, nama='Home indicator')


def h_kosong(s, T, y, ikon, jd, sub, cta=None):
    with s.g('Empty state', 0, y):
        s.circle(195, 70, 64, T.lembut, stroke=T.garis if T.tinta else None, sw=T.sw)
        s.ikon(ikon, 159, 34, 72, T.primer2 if T.hi else T.teks2, 2)
        judul(s, T, 195, 180, jd, 20, anchor='middle')
        para(s, T, 195, 208, sub, 14, 400, T.teks2, anchor='middle', maks=300)
        if cta:
            tombol(s, T, 95, 250, 200, 48, cta)
    return 320


def h_spasi(s, T, y, h=16):
    return h


BLOK_HP = {k[2:]: v for k, v in globals().items() if k.startswith('h_') and k != 'h_tombol_bawah'}


def layar_hp(T, nama, bloks, nav=None, aktif=0, bawah=None, y0=56):
    s = Svg(HP_W, HP_H, nama, T.latar)
    status_bar(s, T)
    y = y0 - 12
    for b in bloks:
        jenis, kw = b[0], (b[1] if len(b) > 1 else {})
        y += BLOK_HP[jenis](s, T, y, **kw) + 8
    if nav:
        nav_bawah(s, T, nav, aktif)
    elif bawah:
        h_tombol_bawah(s, T, **bawah)
    return s


# ================================================================== blok web
def w_navbar(s, T, y, w, x0, menu, cta, logo_ikon='sparkle'):
    with s.g('Navbar', 0, y):
        s.rect(0, 0, w, 80, T.permukaan, nama='Latar navbar')
        s.line(0, 80, w, 80, T.garis, 1)
        s.circle(x0 + 18, 40, 18, T.primer if not T.lo else '#DDD')
        s.ikon(logo_ikon, x0 + 7, 29, 22, T.di_atas(T.primer) if not T.lo else '#444')
        s.text(x0 + 46, 47, T.nama, 20, 800, T.teks, nama='Nama brand', fam=T.fj if T.hi else None)
        x = w / 2 - sum(lebar_teks(m, 15, 500) + 36 for m in menu) / 2 + 30
        for i, m in enumerate(menu):
            s.text(x, 46, m, 15, 600 if i == 0 else 500, T.teks if i == 0 else T.teks2, nama=f'Menu/{m}')
            x += lebar_teks(m, 15, 500) + 36
        tombol(s, T, w - x0 - 170, 18, 170, 44, cta)
    return 80


def w_hero(s, T, y, w, x0, badge_teks, jd, sub, cta1, cta2=None, warna=None, ikon='sparkle', bukti=None):
    with s.g('Hero', 0, y):
        if T.hi and badge_teks: badge(s, T, x0, 96, badge_teks, 'aksen')
        tinggi = judul(s, T, x0, 196, jd, 56, maks=600)
        yy = 196 + tinggi
        yy += para(s, T, x0, yy + 10, sub, 19, 400, T.teks2, maks=540, lh=30)
        tombol(s, T, x0, yy + 36, 200, 56, cta1)
        if cta2: tombol(s, T, x0 + 216, yy + 36, 200, 56, cta2, 'garis')
        if bukti:
            para(s, T, x0, yy + 140, bukti, 14, 600, T.teks2, maks=540)
        bayangan(s, T, w - x0 - 560, 40, 560, 520, 28, 8)
        gambar(s, T, w - x0 - 560, 40, 560, 520, warna or T.primer, 'Ilustrasi hero', f'ikon:{ikon}', r=28)
    return 620


def w_fitur(s, T, y, w, x0, jd, items, latar=True):
    n = len(items)
    with s.g(f'Section/{jd}', 0, y):
        if latar: s.rect(0, 0, w, 380, T.lembut if not T.lo else '#F7F7F7', nama='Latar section')
        judul(s, T, w / 2, 90, jd, 36, anchor='middle')
        cw = (w - 2 * x0 - (n - 1) * 24) / n
        for i, (ik, t, isi) in enumerate(items):
            x = x0 + i * (cw + 24)
            with s.g(f'Fitur/{t}'):
                _kartu(s, T, x, 136, cw, 196)
                s.circle(x + 52, 192, 28, T.aksen if T.hi else '#E0E0E0', stroke=T.garis if T.tinta else None, sw=T.sw)
                s.ikon(ik, x + 38, 178, 28, T.di_atas(T.aksen) if T.hi else T.teks)
                judul(s, T, x + 28, 262, t, 20, maks=cw - 56)
                para(s, T, x + 28, 292, isi, 15, 400, T.teks2, maks=cw - 56, lh=23)
    return 380


def w_kartu(s, T, y, w, x0, jd, items, link='Lihat semua'):
    """items: (nama, info, harga, warna, ikon, label)."""
    n = min(len(items), 4)
    cw = (w - 2 * x0 - (n - 1) * 24) / n
    with s.g(f'Section/{jd}', 0, y):
        judul(s, T, x0, 80, jd, 32)
        if link: para(s, T, w - x0, 80, link, 16, 700, T.primer if T.hi else T.teks, anchor='end')
        for i, (nm, info, h, wr, ik, lb) in enumerate(items[:n]):
            x = x0 + i * (cw + 24)
            with s.g(f'Kartu/{nm}'):
                _kartu(s, T, x, 120, cw, 380)
                gambar(s, T, x + 10, 130, cw - 20, 220, wr, 'Foto ' + nm, f'ikon:{ik}', r=T.r - 4)
                if lb and T.hi: badge(s, T, x + 24, 144, lb, 'aksen')
                s.text(x + 20, 386, nm, 18, 700, T.teks, nama='Nama', maks=cw - 40)
                para(s, T, x + 20, 414, info, 14, 400, T.teks2, maks=cw - 40)
                s.text(x + 20, 476, h, 20, 800, T.primer2 if T.hi else T.teks, nama='Harga')
                tombol(s, T, x + cw - 120, 448, 100, 40, 'Tambah', 'sekunder')
    return 540


def w_langkah(s, T, y, w, x0, jd, items):
    n = len(items)
    cw = (w - 2 * x0) / n
    with s.g(f'Section/{jd}', 0, y):
        judul(s, T, w / 2, 90, jd, 36, anchor='middle')
        for i, (t, isi) in enumerate(items):
            cx = x0 + cw * i + cw / 2
            s.circle(cx, 180, 40, T.primer if not T.lo else '#EEE', stroke=T.garis if (T.tinta or T.lo) else None, sw=T.sw)
            s.text(cx, 194, str(i + 1), 36, 800, T.di_atas(T.primer) if not T.lo else '#444', 'middle', nama='Nomor', fam=T.fj if T.hi else None)
            if i < n - 1: s.line(cx + 56, 180, cx + cw - 56, 180, T.garis, 2, dash='6 8')
            judul(s, T, cx, 262, t, 22, anchor='middle')
            para(s, T, cx, 294, isi, 15, 400, T.teks2, anchor='middle', maks=cw - 60)
    return 360


def w_statistik(s, T, y, w, x0, items):
    """items: (label, nilai, delta, ikon)."""
    n = len(items)
    cw = (w - x0 - 40 - (n - 1) * 20) / n
    with s.g('KPI', 0, y):
        for i, (lb, v, d, ik) in enumerate(items):
            x = x0 + i * (cw + 20)
            with s.g(f'KPI/{lb}'):
                _kartu(s, T, x, 0, cw, 132)
                s.rect(x + 20, 20, 40, 40, T.lembut, r=10)
                s.ikon(ik, x + 28, 28, 24, T.primer if T.hi else T.teks)
                para(s, T, x + 76, 46, lb, 14, 500, T.teks2)
                s.text(x + 20, 104, v, 28, 800, T.teks, nama='Nilai', fam=T.fj if T.hi else None)
                if d:
                    naik = d.startswith('+')
                    s.text(x + cw - 20, 104, d, 14, 700, (T.sukses if naik else T.bahaya) if T.hi else T.teks2, 'end', nama='Perubahan')
    return 152


def w_grafik(s, T, y, w, x0, jd, data, lebar=None, label=None, garis=True):
    lw = lebar or (w - x0 - 40)
    with s.g(f'Grafik/{jd}', x0, y):
        _kartu(s, T, 0, 0, lw, 320)
        judul(s, T, 24, 40, jd, 18)
        mx, mn = max(data), min(data)
        lo = mn - (mx - mn) * 0.6 if (mx - mn) / mx < 0.2 else 0
        gx, gw, gy, gh = 48, lw - 80, 80, 190
        for k in range(5):
            s.line(gx, gy + gh * k / 4, gx + gw, gy + gh * k / 4, T.garis if not T.tinta else T.garis + '22', 1)
        pts = [(gx + gw * i / (len(data) - 1), gy + gh - gh * (v - lo) / (mx - lo)) for i, v in enumerate(data)]
        if garis:
            s.path('M' + 'L'.join(f'{a:.1f} {b:.1f}' for a, b in pts) + f'L{gx + gw} {gy + gh}L{gx} {gy + gh}Z', fill=(T.primer + '22') if T.hi else '#EEEEEE', nama='Area')
            s.path('M' + 'L'.join(f'{a:.1f} {b:.1f}' for a, b in pts), stroke=T.primer if T.hi else '#666', sw=3, nama='Garis')
        else:
            bw = gw / len(data)
            for i, v in enumerate(data):
                h = gh * (v - lo) / (mx - lo)
                s.rect(gx + i * bw + bw * 0.2, gy + gh - h, bw * 0.6, h, T.primer if T.hi else '#BBB', r=4, nama=f'Batang {i + 1}')
        if label:
            for i, l in enumerate(label):
                para(s, T, gx + gw * i / max(len(label) - 1, 1), 300, l, 12, 500, T.teks2, anchor='middle')
    return 340


def w_tabel(s, T, y, w, x0, jd, kolom, baris, lebar=None, status_kol=None):
    lw = lebar or (w - x0 - 40)
    with s.g(f'Tabel/{jd}', x0, y):
        tinggi = 72 + 48 + len(baris) * 56
        _kartu(s, T, 0, 0, lw, tinggi)
        judul(s, T, 24, 44, jd, 18)
        cw = (lw - 48) / len(kolom)
        s.rect(1, 72, lw - 2, 48, T.lembut, nama='Kepala tabel')
        for j, k in enumerate(kolom):
            s.text(24 + j * cw, 102, k, 13, 700, T.teks2, nama=f'Kolom/{k}')
        for i, r in enumerate(baris):
            yy = 120 + i * 56
            s.line(0, yy, lw, yy, T.garis if not T.tinta else T.garis + '33', 1)
            for j, v in enumerate(r):
                if status_kol is not None and j == status_kol:
                    jn = {'Selesai': 'sukses', 'Lunas': 'sukses', 'Aktif': 'sukses', 'Proses': 'peringatan', 'Menunggu': 'peringatan', 'Gagal': 'bahaya', 'Terlambat': 'bahaya'}.get(v, 'info')
                    badge(s, T, 24 + j * cw, yy + 17, v, jn)
                else:
                    para(s, T, 24 + j * cw, yy + 34, v, 14, 600 if j == 0 else 400, T.teks)
    return tinggi + 20


def w_form(s, T, y, w, x0, jd, sub, fields, cta, samping=None):
    with s.g(f'Form/{jd}', 0, y):
        lw = 560
        fx = x0 if samping else (w - lw) / 2
        judul(s, T, fx, 60, jd, 32)
        para(s, T, fx, 96, sub, 16, 400, T.teks2, maks=lw)
        yy = 130
        for lb, nil, ph, st, ps, ik in fields:
            yy += masukan(s, T, fx, yy, lw, lb, nil, ph, st, ps, ik) + 16
        tombol(s, T, fx, yy + 8, lw, 56, cta)
        if samping:
            bx = x0 + lw + 80
            _kartu(s, T, bx, 40, w - bx - x0, yy - 20, isi=T.lembut)
            judul(s, T, bx + 40, 100, samping[0], 24)
            yb = 140
            for t in samping[1]:
                s.ikon('check', bx + 40, yb - 18, 22, T.sukses if T.hi else T.teks)
                yb += para(s, T, bx + 74, yb, t, 16, 400, T.teks, maks=w - bx - x0 - 120) + 16
    return yy + 100


def w_testimoni(s, T, y, w, x0, items):
    n = len(items)
    cw = (w - 2 * x0 - (n - 1) * 24) / n
    with s.g('Testimoni', 0, y):
        judul(s, T, w / 2, 80, 'Kata mereka', 36, anchor='middle')
        for i, (nm, peran, isi) in enumerate(items):
            x = x0 + i * (cw + 24)
            _kartu(s, T, x, 120, cw, 240)
            for k in range(5): s.ikon('star', x + 28 + k * 22, 144, 18, '#E0A100' if T.hi else T.teks2)
            para(s, T, x + 28, 200, f'"{isi}"', 16, 500, T.teks, maks=cw - 56, lh=25)
            avatar(s, T, x + 48, 316, 20, nm[0])
            s.text(x + 78, 312, nm, 15, 700, T.teks, nama='Nama')
            para(s, T, x + 78, 332, peran, 13, 400, T.teks2)
    return 400


def w_cta(s, T, y, w, x0, jd, sub, cta):
    with s.g('CTA', 0, y):
        bayangan(s, T, x0, 20, w - 2 * x0, 240, 28, 8)
        isi = T.primer2 if not T.lo else '#EEE'
        s.rect(x0, 20, w - 2 * x0, 240, isi, r=28, stroke=T.garis if (T.tinta or T.lo) else None, sw=T.sw)
        wt = T.di_atas(isi) if not T.lo else '#444'
        s.text(x0 + 64, 110, jd, 36, 800, wt, nama='Judul CTA', fam=T.fj if T.hi else None)
        para(s, T, x0 + 64, 150, sub, 17, 400, wt, maks=700)
        tombol(s, T, w - x0 - 64 - 220, 112, 220, 56, cta, 'sekunder')
    return 300


def w_footer(s, T, y, w, x0, kolom, hak):
    with s.g('Footer', 0, y):
        isi = '#1C1B1F' if T.hi else ('#3A3A3A' if T.fid == 'mid' else '#F0F0F0')
        s.rect(0, 0, w, 260, isi, nama='Latar footer')
        wt = '#FFFFFF' if not T.lo else '#444'
        w2 = '#C9C5CF' if not T.lo else '#888'
        s.text(x0, 70, T.nama, 22, 800, wt, nama='Brand')
        x = x0 + 400
        for jd, isi_k in kolom:
            s.text(x, 70, jd, 14, 700, wt, nama=f'Kolom/{jd}')
            for i, t in enumerate(isi_k):
                para(s, T, x, 102 + i * 28, t, 14, 400, w2)
            x += 240
        s.line(x0, 200, w - x0, 200, '#FFFFFF22' if not T.lo else '#CCC', 1)
        para(s, T, x0, 234, hak, 13, 400, w2)
    return 260


def w_kanban(s, T, y, w, x0, kolom):
    n = len(kolom)
    cw = (w - x0 - 40 - (n - 1) * 20) / n
    with s.g('Papan kanban', 0, y):
        tinggi = 0
        for i, (nm, kartu_k) in enumerate(kolom):
            x = x0 + i * (cw + 20)
            h = 64 + len(kartu_k) * 116
            tinggi = max(tinggi, h)
            with s.g(f'Kolom/{nm}'):
                s.rect(x, 0, cw, h, T.lembut, r=T.r, nama='Latar kolom')
                judul(s, T, x + 20, 38, f'{nm} · {len(kartu_k)}', 16)
                for j, (t, tag, org) in enumerate(kartu_k):
                    ky = 60 + j * 116
                    _kartu(s, T, x + 12, ky, cw - 24, 104)
                    badge(s, T, x + 28, ky + 14, tag, {'Bug': 'bahaya', 'Desain': 'aksen', 'Fitur': 'info'}.get(tag, 'sukses'))
                    para(s, T, x + 28, ky + 62, t, 14, 600, T.teks, maks=cw - 100)
                    avatar(s, T, x + cw - 48, ky + 76, 14, org)
        if T.hi:
            with s.g('Fokus keyboard'):
                s.rect(x0 + 12 - 3, 60 - 3, cw - 24 + 6, 110, 'none', r=T.r + 3, stroke=T.info, sw=3)
    return tinggi + 20


def w_chat(s, T, y, w, x0, pesan, lebar=None):
    lw = lebar or 760
    cx = x0 if lebar else (w - lw) / 2
    with s.g('Percakapan', cx, y):
        yy = 0
        from svgkit import bungkus
        for siapa, t, sumber in pesan:
            baris = bungkus(t, lw - 200, 16)
            bh = len(baris) * 26 + 32 + (40 if sumber else 0)
            kanan = siapa == 'saya'
            bw = min(max(lebar_teks(b, 16) for b in baris) + 40, lw - 160) if kanan else lw - 120
            x = lw - bw if kanan else 56
            if not kanan:
                s.circle(20, yy + 20, 20, T.primer if not T.lo else '#DDD')
                s.ikon('sparkle', 9, yy + 9, 22, T.di_atas(T.primer) if not T.lo else '#444')
            isi = (T.lembut if kanan else T.permukaan) if not T.lo else '#F2F2F2'
            s.rect(x, yy, bw, bh, isi, r=T.r + 4, stroke=None if kanan else T.garis, sw=T.sw)
            s.text(x + 20, yy + 32, t, 16, 400, T.teks, maks=lw - 200, lh=26, nama='Pesan')
            if sumber:
                sx = x + 20
                for sb in sumber:
                    sw_ = lebar_teks(sb, 12, 600) + 34
                    s.rect(sx, yy + bh - 44, sw_, 28, T.lembut, r=14)
                    s.ikon('doc', sx + 8, yy + bh - 38, 16, T.primer if T.hi else T.teks)
                    s.text(sx + 28, yy + bh - 25, sb, 12, 600, T.teks, nama=f'Sumber/{sb}')
                    sx += sw_ + 8
            yy += bh + 20
        s.rect(0, yy + 10, lw, 64, T.permukaan, r=32, stroke=T.garis, sw=T.sw, nama='Input pertanyaan')
        para(s, T, 28, yy + 48, 'Tanya apa saja tentang materi ini...', 16, 400, T.teks2)
        s.circle(lw - 32, yy + 42, 22, T.primer if not T.lo else '#DDD')
        s.ikon('send', lw - 44, yy + 30, 24, T.di_atas(T.primer) if not T.lo else '#444')
    return yy + 100


def w_spasi(s, T, y, w, x0, h=40):
    return h


BLOK_WEB = {k[2:]: v for k, v in globals().items() if k.startswith('w_')}


def _ukur(T, w, x0, bloks):
    s = Svg(w, 10, 'ukur', T.latar)
    y = 0
    for b in bloks:
        y += BLOK_WEB[b[0]](s, T, y, w, x0, **(b[1] if len(b) > 1 else {}))
    return y


def layar_web(T, nama, bloks, w=1440, x0=120, sidebar=None):
    """sidebar: (menu[(ikon, label)], aktif) untuk tata letak dashboard: konten digeser ke kanan 280px."""
    if sidebar:
        x0 = 312
    h = max(_ukur(T, w, x0, bloks), 900 if sidebar else 0)
    s = Svg(w, h, nama, T.latar)
    if sidebar:
        menu, aktif = sidebar
        with s.g('Sidebar'):
            s.rect(0, 0, 272, h, T.permukaan, nama='Latar sidebar')
            s.line(272, 0, 272, h, T.garis, 1)
            s.circle(48, 48, 18, T.primer if not T.lo else '#DDD')
            s.text(76, 55, T.nama, 18, 800, T.teks, nama='Brand', fam=T.fj if T.hi else None)
            for i, (ik, lb) in enumerate(menu):
                yy = 112 + i * 52
                if i == aktif:
                    s.rect(16, yy, 240, 44, T.lembut if not T.lo else '#EEE', r=min(T.r, 12), nama='Menu aktif')
                s.ikon(ik, 32, yy + 10, 24, T.primer if (i == aktif and T.hi) else T.teks2)
                s.text(68, yy + 28, lb, 15, 700 if i == aktif else 500, T.teks if i == aktif else T.teks2, nama=f'Menu/{lb}')
    y = 0
    for b in bloks:
        y += BLOK_WEB[b[0]](s, T, y, w, x0, **(b[1] if len(b) > 1 else {}))
    return s


def w_topbar(s, T, y, w, x0, jd, sub=None, cta=None):
    with s.g('Top bar', 0, y):
        judul(s, T, x0, 56, jd, 28)
        if sub: para(s, T, x0, 84, sub, 14, 400, T.teks2)
        s.rect(w - 40 - 520, 28, 320, 44, T.permukaan, r=min(T.r, 22), stroke=T.garis, sw=T.sw)
        s.ikon('search', w - 40 - 504, 38, 22, T.teks2)
        para(s, T, w - 40 - 472, 56, 'Cari...', 14, 400, T.teks2)
        if cta:
            tombol(s, T, w - 40 - 184, 28, 184, 44, cta, ikon='plus')
        else:
            s.circle(w - 40 - 160, 50, 20, T.permukaan, stroke=T.garis, sw=T.sw)
            s.ikon('bell', w - 40 - 172, 38, 24, T.teks)
            avatar(s, T, w - 40 - 100, 50, 20, 'A')
    return 112


BLOK_WEB['topbar'] = w_topbar
