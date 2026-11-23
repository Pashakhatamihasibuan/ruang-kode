"""Papan tahap 1-2 (riset, struktur), 6 (design system), 7 (handoff) dan motion untuk studi kasus Kopi Kita."""
from papan import (papan, kartu, teks, daftar, sticky, panah, simpul, swatch, kontras, ukuran, tempel,
                   TINTA, ABU, GARIS, STICKY)
from svgkit import Svg, Tema, lebar_teks, campur
import komponen as K
import kopikita as KK

W = 1920


# ------------------------------------------------------------------ tahap 1: riset
def persona():
    s = papan('01 Riset/Persona', W, 1180, 'TAHAP 1 · RISET', 'Persona: Rina, karyawan yang dikejar jam masuk',
              'Disusun dari 8 wawancara pelanggan outlet Gatot Subroto dan 214 respons survei (Okt 2026). Bukan karangan: setiap poin punya kutipan.')
    with s.g('Profil'):
        kartu(s, 64, 230, 520, 880, None)
        s.circle(324, 360, 84, '#FFE0C7', nama='Foto profil')
        s.circle(324, 340, 34, '#C98B5E'); s.path('M262 430a62 50 0 0 1 124 0z', fill='#C98B5E')
        s.text(324, 490, 'Rina Hutapea, 27', 26, 800, TINTA, 'middle', nama='Nama persona')
        s.text(324, 520, 'Staf keuangan · Medan · Android', 16, 400, ABU, 'middle', nama='Peran')
        y = 570
        for k, v in [('Masuk kantor', '08.00, absen sidik jari'), ('Rutinitas', 'Beli kopi 4x seminggu, 07.30-07.50'),
                     ('Perangkat', 'Android kelas menengah, kuota 25 GB'), ('Bayar', 'QRIS dan e-wallet, jarang tunai'),
                     ('Literasi digital', 'Tinggi, terbiasa aplikasi ojol')]:
            s.text(104, y, k, 14, 700, ABU, nama=f'Label/{k}')
            s.text(104, y + 24, v, 16, 500, TINTA, nama=f'Isi/{k}')
            y += 66
        s.rect(104, 920, 440, 150, '#FFF6E5', r=12, nama='Kutipan')
        teks(s, 128, 956, '"Saya sering batal beli karena antrean panjang. Kalau telat absen, potong uang makan."', 17, 600, TINTA, maks=392)
    kol = [('Tujuan', '#1E7A4C', ['Kopi siap saat tiba di outlet, tanpa menunggu', 'Tahu pasti kapan pesanan jadi', 'Pesanan sama setiap hari bisa diulang 1 ketukan']),
           ('Frustrasi', '#C8102E', ['Antre 8-15 menit di jam sibuk 07.30-08.00', 'Pesanan salah (kurang manis jadi normal)', 'Aplikasi lain minta daftar panjang sebelum pesan']),
           ('Perilaku', '#1F5FA8', ['Memesan sambil di angkot/ojol, satu tangan', 'Membandingkan promo pagi antar-kedai', 'Jarang membaca teks panjang, mengandalkan ikon + label']),
           ('Kebutuhan desain', '#8A4B2A', ['Pesan ulang dari Beranda dalam 2 ketukan', 'Status pesanan + estimasi menit yang jujur', 'Target sentuh 48dp, kontras AA, zona jempol'])]
    for i, (jd, wr, isi) in enumerate(kol):
        x, y = 616 + (i % 2) * 632, 230 + (i // 2) * 290
        yy = kartu(s, x, y, 608, 270, jd, aksen=wr)
        daftar(s, x + 28, yy + 20, isi, 540, 17, titik=wr, jarak=18)
    yy = kartu(s, 616, 810, 1240, 300, 'Skenario: Senin, 07.25 di ojol', aksen='#9A6700')
    teks(s, 644, yy + 24, 'Rina baru berangkat dari rumah, 20 menit ke kantor. Ia ingin es kopi susu aren kurang manis yang sama seperti kemarin, '
         'siap tepat saat ojol berhenti di depan outlet Gatot Subroto. Tangannya satu memegang ponsel, satu memegang tas. '
         'Sinyal kadang turun ke 3G di jalan Sisingamangaraja.', 18, 400, TINTA, maks=1180, lh=30)
    teks(s, 644, yy + 170, 'Pertanyaan riset berikutnya: berapa menit sebelum tiba Rina mau memesan? Apakah ia mau membayar di muka?', 16, 600, ABU, maks=1180)
    return s


def empathy():
    s = papan('01 Riset/Empathy map', W, 1080, 'TAHAP 1 · RISET', 'Empathy map: Rina di jam 07.30',
              'Apa yang Rina katakan, pikirkan, lakukan, dan rasakan saat ingin membeli kopi sebelum masuk kantor.')
    kuad = [('Katakan', ['"Antrenya panjang banget."', '"Bisa dipisah esnya, Kak?"', '"Kok sudah 10 menit belum jadi?"']),
            ('Pikirkan', ['Takut telat absen', 'Apakah promo pagi masih berlaku?', 'Lebih baik pesan dari jalan']),
            ('Lakukan', ['Cek jam berkali-kali', 'Pesan sambil naik ojol', 'Screenshot struk untuk reimburse']),
            ('Rasakan', ['Cemas di 10 menit terakhir', 'Lega saat nama dipanggil', 'Kesal kalau pesanan salah'])]
    for i, (jd, isi) in enumerate(kuad):
        x, y = 64 + (i % 2) * 904, 230 + (i // 2) * 410
        kartu(s, x, y, 880, 390, jd)
        for j, t in enumerate(isi):
            sticky(s, x + 24 + j * 280, y + 80, 260, 150, t, STICKY[(i + j) % len(STICKY)], size=16)
    with s.g('Pusat'):
        s.circle(W / 2, 640, 70, TINTA)
        s.text(W / 2, 646, 'Rina', 22, 800, '#FFFFFF', 'middle')
    return s


def journey():
    s = papan('01 Riset/Journey map', W, 1140, 'TAHAP 1 · RISET', 'Journey map: dari ingin kopi sampai kopi di tangan',
              'Tahap, aksi, pikiran, emosi, pain point, dan peluang. Kurva emosi dari wawancara (skala -2 sampai +2).')
    tahap = ['Ingin kopi', 'Pilih tempat', 'Pesan', 'Bayar', 'Menunggu', 'Ambil']
    baris = [('Aksi', ['Bangun, cek jadwal', 'Bandingkan promo', 'Pilih menu, atur manis', 'QRIS/e-wallet', 'Pantau status', 'Tunjukkan nomor']),
             ('Pikiran', ['Sempat nggak ya?', 'Mana yang dekat kantor?', 'Pesanan kemarin apa?', 'Aman nggak?', 'Kapan jadi?', 'Ini punyaku?']),
             ('Pain point', ['-', 'Promo tidak jelas', 'Form panjang, harus daftar', 'Gagal bayar, saldo terpotong', 'Tidak ada estimasi', 'Antre di kasir lagi']),
             ('Peluang', ['Notifikasi promo pagi', 'Outlet terdekat otomatis', 'Pesan ulang 1 ketukan', 'Retry aman + status jelas', 'Estimasi menit live', 'Loker/rak ambil'])]
    x0, cw = 260, 268
    for i, t in enumerate(tahap):
        with s.g(f'Tahap/{t}'):
            s.rect(x0 + i * cw, 230, cw - 12, 52, TINTA, r=10)
            s.text(x0 + i * cw + (cw - 12) / 2, 263, f'{i + 1}. {t}', 16, 700, '#FFFFFF', 'middle')
    y = 300
    for jb, isi in baris:
        with s.g(f'Baris/{jb}'):
            s.text(64, y + 40, jb, 16, 800, TINTA)
            for i, t in enumerate(isi):
                warna = {'Pain point': '#FFE1E1', 'Peluang': '#DDF5E3'}.get(jb, '#FFFFFF')
                s.rect(x0 + i * cw, y, cw - 12, 96, warna, r=10, stroke=GARIS)
                teks(s, x0 + i * cw + 16, y + 32, t, 15, 500, TINTA, maks=cw - 44)
        y += 112
    with s.g('Kurva emosi', 0, y + 20):
        s.text(64, 80, 'Emosi', 16, 800, TINTA)
        s.line(x0, 90, x0 + cw * 6 - 12, 90, GARIS, 1, dash='4 4')
        nilai = [1, 0, -1, -2, -1.5, 1.5]
        titik = [(x0 + i * cw + (cw - 12) / 2, 90 - v * 34) for i, v in enumerate(nilai)]
        s.path('M' + ' L'.join(f'{a:.0f} {b:.0f}' for a, b in titik), stroke='#8A4B2A', sw=3, nama='Kurva')
        for (a, b), v in zip(titik, nilai):
            s.circle(a, b, 9, '#1E7A4C' if v > 0 else ('#C8102E' if v < 0 else '#9A6700'))
    return s


def masalah():
    s = papan('01 Riset/Problem statement', W, 900, 'TAHAP 1 · RISET', 'Problem statement, HMW, dan metrik',
              'Ringkasan riset menjadi satu masalah yang bisa diuji.')
    yy = kartu(s, 64, 230, 1792, 200, 'Problem statement', '#FFF6E5', aksen='#8A4B2A')
    teks(s, 92, yy + 30, 'Karyawan yang membeli kopi sebelum jam 08.00 kesulitan mendapatkan pesanan tepat waktu karena antrean dan tidak ada estimasi siap, sehingga 31% responden pernah batal membeli dan 18% pernah telat absen.', 22, 600, TINTA, maks=1720, lh=34)
    for i, (jd, isi) in enumerate([('How might we', ['HMW membuat kopi siap tepat saat Rina tiba?', 'HMW membuat pesan ulang secepat 2 ketukan?', 'HMW membuat gagal bayar tidak menakutkan?']),
                                   ('Metrik utama (HEART)', ['Task success pesan ulang >= 95%', 'Waktu pesan < 30 detik (median)', 'Batal di checkout turun dari 22% ke 10%']),
                                   ('Asumsi yang diuji', ['Pengguna mau memilih jam ambil', 'Estimasi menit menurunkan kecemasan', 'Passkey/OTP cukup tanpa password'])]):
        x = 64 + i * 604
        yy = kartu(s, x, 470, 580, 360, jd)
        daftar(s, x + 28, yy + 24, isi, 520, 18, jarak=20)
    return s


# ------------------------------------------------------------------ tahap 2: struktur
def sitemap():
    s = papan('02 Struktur/Sitemap', W, 1000, 'TAHAP 2 · STRUKTUR', 'Sitemap dan arsitektur informasi',
              'Navigasi bawah 4 tab (Beranda, Menu, Pesanan, Akun). Diuji dengan tree testing 20 peserta: 90% menemukan "ubah tingkat manis" di Detail produk.')
    simpul(s, 860, 240, 200, 56, 'Aplikasi Kopi Kita', 'terminal')
    tab = [('Beranda', ['Promo pagi', 'Pesan ulang', 'Pilih outlet', 'Notifikasi']), ('Menu', ['Kategori', 'Cari', 'Detail produk', 'Favorit']),
           ('Pesanan', ['Keranjang', 'Pembayaran', 'Status & nomor ambil', 'Riwayat & struk']), ('Akun', ['Profil', 'Metode bayar', 'Privasi & persetujuan data', 'Bantuan'])]
    for i, (t, anak) in enumerate(tab):
        x = 120 + i * 440
        panah(s, 960, 296, x + 110, 380, ABU, 1.5, nama=f'Garis/{t}')
        simpul(s, x, 380, 220, 56, t, warna='#FFE9A8')
        for j, a in enumerate(anak):
            panah(s, x + 20, 436 + j * 84 + 0, x + 40, 476 + j * 84, GARIS, 1.5, nama=f'Garis/{a}')
            simpul(s, x + 40, 456 + j * 84, 240, 52, a)
    teks(s, 64, 900, 'Masuk (OTP/passkey) hanya diminta saat checkout pertama, bukan di awal: pengguna bisa menjelajah menu tanpa akun.', 16, 500, ABU, maks=1792)
    return s


def userflow():
    s = papan('02 Struktur/User flow', W, 980, 'TAHAP 2 · STRUKTUR', 'User flow: pesan ulang sebelum berangkat',
              'Jalur utama (happy path) dan cabang: belum masuk, stok habis, gagal bayar. Setiap kotak adalah satu layar di tahap 3-5.')
    n = [('Buka aplikasi', 'terminal', 64, 300), ('Beranda: kartu Pesan ulang', 'layar', 300, 290), ('Sudah masuk?', 'keputusan', 600, 270),
         ('Masuk: OTP / passkey', 'layar', 600, 470), ('Keranjang + jam ambil', 'layar', 880, 290), ('Stok ada?', 'keputusan', 1160, 270),
         ('Pembayaran QRIS / e-wallet', 'layar', 1440, 290), ('Berhasil? ', 'keputusan', 1440, 470), ('Status + nomor ambil', 'layar', 1700, 290),
         ('Ganti menu serupa', 'layar', 1160, 640), ('Gagal: coba lagi / metode lain', 'layar', 1440, 680)]
    pos = {}
    for t, j, x, y in n:
        w, h = (200, 120) if j == 'keputusan' else (200, 80)
        simpul(s, x, y, w, h, t, j, warna='#DDF5E3' if t.startswith('Status') else None)
        pos[t] = (x, y, w, h)
    def kanan(a): x, y, w, h = pos[a]; return x + w, y + h / 2
    def kiri(a): x, y, w, h = pos[a]; return x, y + h / 2
    def bawah(a): x, y, w, h = pos[a]; return x + w / 2, y + h
    def atas(a): x, y, w, h = pos[a]; return x + w / 2, y
    for a, b, lb, f1, f2 in [('Buka aplikasi', 'Beranda: kartu Pesan ulang', None, kanan, kiri), ('Beranda: kartu Pesan ulang', 'Sudah masuk?', None, kanan, kiri),
                             ('Sudah masuk?', 'Keranjang + jam ambil', 'Ya', kanan, kiri), ('Sudah masuk?', 'Masuk: OTP / passkey', 'Belum', bawah, atas),
                             ('Keranjang + jam ambil', 'Stok ada?', None, kanan, kiri), ('Stok ada?', 'Pembayaran QRIS / e-wallet', 'Ya', kanan, kiri),
                             ('Stok ada?', 'Ganti menu serupa', 'Habis', bawah, atas), ('Pembayaran QRIS / e-wallet', 'Berhasil? ', None, bawah, atas),
                             ('Berhasil? ', 'Gagal: coba lagi / metode lain', 'Tidak', bawah, atas)]:
        (x1, y1), (x2, y2) = f1(a), f2(b)
        panah(s, x1, y1, x2, y2, TINTA, 2, lb, nama=f'Alur/{a} ke {b}')
    x1, y1 = kanan('Berhasil? '); panah(s, x1, y1, 1800, 370, '#1E7A4C', 2, 'Ya', nama='Alur/berhasil')
    x1, y1 = kanan('Masuk: OTP / passkey'); panah(s, x1, y1, 980, 370, TINTA, 2, nama='Alur/kembali ke keranjang', dash='6 6')
    teks(s, 64, 900, 'Garis putus-putus: kembali ke alur utama setelah cabang selesai. Target: 2 ketukan dari Beranda ke Pembayaran untuk pengguna yang sudah masuk.', 16, 500, ABU, maks=1792)
    return s


# ------------------------------------------------------------------ tahap 6: design system
def ds_fondasi(token, nama='Kopi Kita'):
    T = Tema('hi', **token)
    s = papan('06 Design system/Fondasi', W, 1680, 'TAHAP 6 · DESIGN SYSTEM', f'Fondasi {nama}: warna, tipografi, spasi, radius, elevasi',
              'Token primitif dan semantik. Nama token sama persis dengan tokens.json (format DTCG 2025.10) agar bisa diimpor ke Figma Variables / Tokens Studio.')
    peran = [('primer', 'color.action.primary', 'Tombol utama, tautan'), ('primer2', 'color.action.primary-strong', 'Tekan, teks harga'),
             ('aksen', 'color.accent', 'Badge, sorotan'), ('latar', 'color.bg.canvas', 'Latar layar'), ('permukaan', 'color.bg.surface', 'Kartu, lembar'),
             ('lembut', 'color.bg.subtle', 'Chip, area input'), ('teks', 'color.text.primary', 'Teks utama'), ('teks2', 'color.text.secondary', 'Teks pendukung'),
             ('garis', 'color.border.default', 'Garis, pemisah'), ('sukses', 'color.feedback.success', 'Berhasil'), ('bahaya', 'color.feedback.danger', 'Error, hapus'),
             ('peringatan', 'color.feedback.warning', 'Peringatan'), ('info', 'color.feedback.info', 'Info')]
    with s.g('Warna'):
        s.text(64, 260, 'Warna semantik', 22, 800, TINTA)
        for i, (k, tok, pr) in enumerate(peran):
            x, y = 64 + (i % 9) * 200, 290 + (i // 9) * 220
            v = T.t[k][:7]
            swatch(s, x, y, tok, v, pr, 180)
            if k in ('primer', 'primer2', 'sukses', 'bahaya', 'teks', 'teks2', 'info'):
                c = kontras(v, '#FFFFFF') if k != 'teks2' else kontras(v, T.latar)
                s.text(x + 12, y + 30, f'{c:.1f}:1', 13, 700, T.di_atas(v), nama='Rasio kontras')
                s.text(x + 12, y + 50, 'AA' if c >= 4.5 else ('AA besar' if c >= 3 else 'Gagal'), 12, 600, T.di_atas(v), nama='Status WCAG')
    with s.g('Tipografi', 0, 760):
        s.text(64, 0, 'Skala tipografi (rasio 1,2 · basis 16)', 22, 800, TINTA)
        skala = [('display', 40, 800, 48), ('heading.1', 28, 800, 36), ('heading.2', 22, 700, 30), ('heading.3', 18, 700, 26),
                 ('body.lg', 17, 400, 26), ('body.md', 15, 400, 22), ('label', 14, 600, 20), ('caption', 12, 500, 16)]
        y = 50
        for nm, sz, wt, lh in skala:
            fam = T.fj if nm in ('display', 'heading.1', 'heading.2') else T.fb
            s.text(64, y + sz, 'Kopi Nusantara siap tanpa antre', sz, wt if fam == T.fb else T.wj, TINTA, nama=f'Contoh/{nm}', fam=fam)
            s.text(760, y + sz, f'typography.{nm} · {fam} {sz}/{lh} · {wt}', 14, 500, ABU, nama=f'Spek/{nm}')
            y += lh + 22
    with s.g('Spasi', 1500, 760):
        s.text(0, 0, 'Spasi (grid 4/8)', 22, 800, TINTA)
        for i, v in enumerate([4, 8, 12, 16, 24, 32, 48, 64]):
            s.rect(0, 30 + i * 46, v * 4, 30, '#E5484D33', r=4, stroke='#E5484D')
            s.text(v * 4 + 16, 51 + i * 46, f'space.{v} = {v}px', 14, 600, TINTA)
    with s.g('Radius & elevasi', 0, 1340):
        s.text(64, 0, 'Radius', 22, 800, TINTA)
        for i, (nm, r) in enumerate([('sm', 6), ('md', 10), ('lg', T.r), ('full', 999)]):
            s.rect(64 + i * 150, 30, 120, 120, T.lembut, r=min(r, 60), stroke=T.primer, sw=2)
            s.text(64 + i * 150, 176, f'radius.{nm} = {r if r < 999 else "999"}', 13, 600, TINTA)
        s.text(760, 0, 'Elevasi (di Figma: Effects > Drop shadow)', 22, 800, TINTA)
        for i, (nm, sp) in enumerate([('0', 'tanpa bayangan'), ('1', 'y2 blur4 #0000000F'), ('2', 'y6 blur16 #00000014'), ('3', 'y12 blur32 #0000001F')]):
            x = 760 + i * 270
            for k in range(i):
                s.rect(x + 2, 30 + 2 + k * 3, 220, 120, '#00000010', r=16)
            s.rect(x, 30, 220, 120, '#FFFFFF', r=16, stroke=GARIS)
            s.text(x, 176, f'elevation.{nm} · {sp}', 13, 600, TINTA)
    return s


def ds_komponen(token, nama='Kopi Kita'):
    T = Tema('hi', **token)
    s = papan('06 Design system/Komponen', W, 1900, 'TAHAP 6 · DESIGN SYSTEM', f'Komponen {nama} dan semua state-nya',
              'Setiap baris adalah satu komponen; setiap kolom satu state. Di Figma, jadikan Component Set dengan properti Variant=state.')
    s.font = T.fb
    states = ['default', 'hover', 'tekan', 'fokus', 'nonaktif', 'memuat']
    y = 250
    with s.g('Tombol'):
        s.text(64, y, 'Tombol (tinggi 48, min. lebar 88, target sentuh 48)', 20, 800, TINTA)
        for i, st in enumerate(states):
            s.text(300 + i * 260, y + 40, st, 13, 700, ABU)
        for j, v in enumerate(['primer', 'sekunder', 'garis', 'teks', 'bahaya']):
            s.text(64, y + 92 + j * 72, v, 15, 700, TINTA)
            for i, st in enumerate(states):
                K.tombol(s, T, 300 + i * 260, y + 62 + j * 72, 210, 48, 'Pesan sekarang' if v != 'bahaya' else 'Hapus item', v, state=st)
    y = 740
    with s.g('Input'):
        s.text(64, y, 'Input teks (label selalu tampil, pesan error terhubung ke field)', 20, 800, TINTA)
        for i, (st, nil, ps) in enumerate([('default', '', None), ('fokus', '0812', None), ('terisi', '0812 3456 7890', None),
                                           ('error', '0812 34', 'Nomor HP minimal 10 digit'), ('nonaktif', '', None)]):
            K.masukan(s, T, 64 + i * 360, y + 30, 330, 'Nomor HP', nil, '0812 3456 7890', st, ps, ikon='phone')
            s.text(64 + i * 360, y + 150, st, 13, 700, ABU)
    y = 960
    with s.g('Seleksi'):
        s.text(64, y, 'Chip, segmen, radio, stepper, badge', 20, 800, TINTA)
        x = 64
        for i, c in enumerate(['Semua', 'Kopi', 'Non-kopi']):
            x += K.chip(s, T, x, y + 30, c, i == 0) + 10
        K.segmen(s, T, 420, y + 26, 320, ['Regular', 'Large'], 0)
        K.radio(s, T, 780, y + 20, 340, 'QRIS', 'Semua e-wallet & m-banking', True, 'qr')
        K.radio(s, T, 1150, y + 20, 340, 'Kartu debit/kredit', 'Visa, Mastercard, GPN', False, 'card')
        K.stepper(s, T, 1520, y + 34, 2)
        x = 64
        for jn in ['info', 'sukses', 'bahaya', 'peringatan', 'aksen']:
            x += K.badge(s, T, x, y + 110, jn.upper(), jn) + 12
    y = 1140
    with s.g('Kartu & daftar'):
        s.text(64, y, 'Kartu produk, baris daftar, skeleton (state memuat)', 20, 800, TINTA)
        K.kartu_produk(s, T, 64, y + 30, 200, 'Es Kopi Susu Aren', 'Espresso', 'Rp24.000', '#A66A43', label='Terlaris')
        K.kartu_produk(s, T, 290, y + 30, 200, 'Kopi Gayo V60', 'Manual brew', 'Rp32.000', '#6E4A33', favorit=True)
        with s.g('Kartu memuat'):
            K.skeleton(s, 516, y + 30, 200, 160, 14); K.skeleton(s, 516, y + 206, 150, 16); K.skeleton(s, 516, y + 234, 100, 14); K.skeleton(s, 516, y + 270, 90, 20)
        K.baris_list(s, T, 760, y + 30, 420, 'Caffè Latte', 'Hot · susu oat', 'Rp28.000', '#C49A6C', 'plus')
        K.baris_list(s, T, 760, y + 140, 420, 'Matcha Latte', 'Regular · kurang manis', 'Rp30.000', '#6F8F4E', 'stepper')
    y = 1500
    with s.g('Umpan balik & navigasi'):
        s.text(64, y, 'Dialog, toast, navigasi bawah, app bar', 20, 800, TINTA)
        K.dialog(s, T, 64, y + 30, 340, 'Pembayaran gagal', 'Saldo tidak terpotong. Coba lagi atau pilih metode lain.', 'Coba lagi', 'Ganti metode')
        K.toast(s, T, 440, y + 40, 340, 'Ditambahkan ke keranjang', 'sukses')
        K.toast(s, T, 440, y + 110, 340, 'Koneksi terputus, mencoba lagi', 'bahaya')
        with s.g('Nav bawah', 820, y + 30 - (K.HP_H - 84)):
            K.nav_bawah(s, T, KK.NAV, 0)
        with s.g('App bar', 1240, y - 14):
            K.appbar(s, T, 'Keranjang', 'back', ('share',), w=K.HP_W, y=44)
    return s


# ------------------------------------------------------------------ tahap 7: handoff
def redline():
    s = papan('07 Handoff/Redline layar HP', W, 1180, 'TAHAP 7 · HANDOFF', 'Redline: Beranda dan Detail produk',
              'Ukuran dalam px (1x, setara dp/pt). Garis merah = jarak, label biru = token. Di Figma, developer bisa juga memakai Dev Mode untuk nilai yang sama.')
    tempel(s, KK.beranda('hi').svg(), 140, 260, 1, 'Layar/Beranda')
    tempel(s, KK.detail('hi').svg(), 1100, 260, 1, 'Layar/Detail')
    ox, oy = 140, 260
    ukuran(s, ox, oy + 150, ox + 24, oy + 150, '24')
    ukuran(s, ox + 24, oy + 400, ox + 366, oy + 400, '342')
    ukuran(s, ox + 380, oy + 124, ox + 380, oy + 176, '52')
    ukuran(s, ox + 380, oy + 192, ox + 380, oy + 240, '48')
    ukuran(s, ox + 380, oy + 256, ox + 380, oy + 392, '136')
    ukuran(s, ox + 24, oy + 244, ox + 24, oy + 256, '16')
    for i, (tx, ty, lb) in enumerate([(ox - 120, oy + 150, 'radius.lg 14'), (ox - 120, oy + 230, 'bg.surface'), (ox - 120, oy + 330, 'action.primary'),
                                      (ox - 120, oy + 480, 'heading.3 18/26'), (ox - 120, oy + 800, 'nav 84 + safe area')]):
        s.rect(tx, ty - 14, 112, 22, '#1F5FA8', r=4)
        s.text(tx + 56, ty + 1, lb, 11, 700, '#FFFFFF', 'middle', nama=f'Token/{lb}')
    ox = 1100
    ukuran(s, ox, oy + 330, ox, oy + 300, '30 tumpang', nama='Redline/tumpang lembar')
    ukuran(s, ox + 144, oy + 830, ox + 366, oy + 830, '222')
    ukuran(s, ox + 380, oy + 760, ox + 380, oy + 808, '48')
    with s.g('Catatan', 560, 300):
        kartu(s, 0, 0, 480, 780, 'Catatan implementasi')
        daftar(s, 28, 90, ['Lembar detail tumpang 30px di atas foto, radius atas 24.', 'Semua target sentuh >= 48x48 (WCAG 2.5.8 AA min. 24).',
                           'Teks harga memakai angka tabular (font-variant-numeric: tabular-nums).', 'Nav bawah mengikuti safe area bawah (env(safe-area-inset-bottom)).',
                           'Fokus keyboard: cincin 3px color.focus, tidak tertutup app bar (WCAG 2.4.11).', 'Skeleton tampil jika data > 300ms; jangan tampilkan spinner penuh layar.',
                           'Format harga: Rp24.000 (titik ribuan, tanpa spasi).'], 420, 16, jarak=16)
    return s


def aset():
    s = papan('07 Handoff/Daftar aset', W, 900, 'TAHAP 7 · HANDOFF', 'Daftar aset ekspor',
              'Semua ikon ada di folder aset/ikon sebagai SVG 24x24 garis 2px. Foto produk adalah placeholder: ganti dengan foto asli 4:3, WebP/AVIF.')
    baris = [('Ikon (55)', 'aset/ikon/*.svg', 'SVG', '24x24, stroke 2, currentColor', 'Ekspor dari layer Ikon/*'),
             ('Logo', 'aset/logo.svg', 'SVG', 'Tinggi 36 di navbar', 'Gunakan versi putih di footer'),
             ('Foto produk', 'aset/foto-produk-*.svg', 'WebP/AVIF', '4:3, 800x600 @2x', 'Placeholder vektor di kit'),
             ('Ilustrasi empty state', 'aset/kosong-keranjang.svg', 'SVG', '144x144', 'Teks alt: "Keranjang kosong"'),
             ('Ikon aplikasi', '-', 'PNG', '1024 (iOS), 512 adaptive (Android)', 'Buat dari logo, zona aman 66%'),
             ('Pratinjau layar', 'png/*.png', 'PNG', '1x, untuk dokumentasi', 'Bukan aset produksi')]
    kol = [('Aset', 64), ('Lokasi di ZIP', 400), ('Format', 820), ('Ukuran', 1020), ('Catatan', 1420)]
    with s.g('Tabel aset'):
        s.rect(64, 240, 1792, 56, TINTA, r=10)
        for k, x in kol:
            s.text(x + 20, 275, k, 15, 700, '#FFFFFF')
        for i, b in enumerate(baris):
            y = 296 + i * 72
            s.rect(64, y, 1792, 72, '#FFFFFF' if i % 2 else '#FAFAFB', stroke=GARIS)
            for (k, x), v in zip(kol, b):
                s.text(x + 20, y + 44, v, 15, 500 if k != 'Aset' else 700, TINTA, nama=f'{k}/{v[:20]}')
    return s


# ------------------------------------------------------------------ animasi & prototype
INTERAKSI = [  # (dari, ke, pemicu, animasi, durasi, easing)
    ('01 Masuk', '02 Beranda', 'Tap "Kirim kode OTP" > OTP valid', 'Dissolve', 200, 'ease-out'),
    ('02 Beranda', '03 Menu', 'Tap tab Menu', 'Instant (tab tidak dianimasikan)', 0, '-'),
    ('03 Menu', '04 Detail', 'Tap kartu produk', 'Smart Animate (foto membesar)', 300, 'ease-in-out'),
    ('04 Detail', '05 Keranjang', 'Tap "Tambah"', 'Move in dari kanan', 250, 'ease-out'),
    ('05 Keranjang', '06 Pembayaran', 'Tap "Lanjut ke pembayaran"', 'Push dari kanan', 250, 'ease-out'),
    ('06 Pembayaran', '07 Berhasil', 'Tap "Bayar" > sukses', 'Smart Animate + Spring', 400, 'spring (mass 1, stiffness 300, damping 26)'),
    ('06 Pembayaran', 'Gagal bayar', 'Tap "Bayar" > gagal', 'Overlay dialog, dissolve', 200, 'ease-out'),
]
MIKRO = [('Tombol tekan', 'scale 0.97, 100ms ease-out', 'Umpan balik sentuh'),
         ('Tambah ke keranjang', 'badge keranjang +1 bounce, 300ms spring', 'Konfirmasi tanpa pindah layar'),
         ('Skeleton memuat', 'shimmer kiri ke kanan, 1200ms linear, loop', 'Status sistem terlihat'),
         ('Toast', 'slide up 16px + fade, 200ms; hilang setelah 4 detik', 'Tidak menutupi CTA'),
         ('Centang berhasil', 'stroke draw 400ms + scale 0.8 ke 1 spring', 'Peak-end rule: akhir yang menyenangkan'),
         ('Reduced motion', 'semua animasi jadi dissolve 0-100ms', 'Hormati prefers-reduced-motion')]


def motion():
    s = papan('05b Prototype/Peta interaksi & motion', W, 1530, 'TAHAP 5 · PROTOTYPE & ANIMASI', 'Peta interaksi dan spesifikasi motion',
              'Sambungkan frame di Figma (tab Prototype) persis seperti tabel ini. Durasi 150-400ms; gunakan Smart Animate jika layer bernama sama di kedua frame.')
    skala = 0.36
    layar = [KK.masuk, KK.beranda, KK.menu, KK.detail, KK.keranjang, KK.bayar, KK.berhasil]
    for i, f in enumerate(layar):
        x = 64 + i * 262
        tempel(s, f('hi').svg(), x, 250, skala, f'Frame/{i + 1:02d}')
        s.rect(x, 250, 390 * skala, 844 * skala, 'none', r=8, stroke=GARIS, sw=1)
        if i < 6:
            panah(s, x + 390 * skala + 6, 250 + 150, x + 262 - 6, 250 + 150, '#8A4B2A', 2, nama=f'Sambungan/{i + 1}')
    with s.g('Tabel interaksi', 0, 600):
        s.rect(64, 0, 1792, 52, TINTA, r=10)
        kol = [('Dari', 0), ('Ke', 200), ('Pemicu', 400), ('Animasi', 820), ('Durasi', 1220), ('Easing', 1360)]
        for k, x in kol:
            s.text(84 + x, 33, k, 14, 700, '#FFFFFF')
        for i, r in enumerate(INTERAKSI):
            y = 52 + i * 56
            s.rect(64, y, 1792, 56, '#FFFFFF' if i % 2 else '#FAFAFB', stroke=GARIS)
            for (k, x), v in zip(kol, r):
                s.text(84 + x, y + 35, f'{v} ms' if k == 'Durasi' and v else str(v), 14, 500, TINTA, nama=f'{k}/{str(v)[:20]}')
    with s.g('Mikro-interaksi', 0, 1110):
        s.text(64, 0, 'Mikro-interaksi', 22, 800, TINTA)
        for i, (n, spek, why) in enumerate(MIKRO):
            x, y = 64 + (i % 3) * 604, 30 + (i // 3) * 170
            kartu(s, x, y, 580, 150, n, aksen='#8A4B2A')
            teks(s, x + 28, y + 86, spek, 15, 600, TINTA, maks=530)
            teks(s, x + 28, y + 118, why, 14, 400, ABU, maks=530)
    return s


def eksplorasi_gaya():
    """Satu layar dalam 8 gaya visual: menunjukkan token (bukan layout) yang mengubah gaya."""
    import svgkit
    s = papan('05 Eksplorasi gaya/Beranda 8 gaya', W, 1360, 'TAHAP 5 · EKSPLORASI', 'Satu layout, delapan gaya visual',
              'Struktur dan konten sama; yang berubah hanya token (warna, radius, font, garis, bayangan). Pilih satu gaya untuk produk, lalu kunci di design system.')
    gaya = [g for g in svgkit.GAYA if g not in ('wireframe', 'manga')]
    for i, g in enumerate(gaya):
        KK.GAYA_AKTIF[0] = g
        x, y = 64 + (i % 4) * 460, 240 + (i // 4) * 540
        tempel(s, KK.beranda('hi').svg(), x, y, 0.55, f'Gaya/{g}')
        s.text(x, y + 490, svgkit.GAYA[g]['label'], 18, 800, TINTA, nama=f'Label/{g}')
        s.text(x, y + 514, f'gaya="{g}"', 13, 500, ABU, nama=f'Kode/{g}')
    KK.GAYA_AKTIF[0] = 'modern'
    return s
