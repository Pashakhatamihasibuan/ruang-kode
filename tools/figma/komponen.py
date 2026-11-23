"""Komponen UI yang sadar fidelitas: tampil sebagai kotak wireframe (lo), abu-abu (mid), atau final (hi)."""
from svgkit import Svg, Tema, lebar_teks, bungkus

HP_W, HP_H = 390, 844


def para(s, T, x, y, teks, size=14, weight=400, warna=None, maks=None, lh=None, nama=None, anchor='start', paksa=False):
    """Teks isi. Di wireframe lo-fi, teks kecil diganti bar abu-abu (konten belum final)."""
    warna = warna or T.teks
    lh = lh or round(size * 1.45)
    if T.lo and size <= 15 and not paksa:
        baris = bungkus(teks, maks, size, weight) if maks else str(teks).split('\n')
        with s.g(nama or 'Teks (placeholder)'):
            for i, b in enumerate(baris):
                w = min(lebar_teks(b, size, weight), maks or 9999)
                bx = x - w if anchor == 'end' else (x - w / 2 if anchor == 'middle' else x)
                s.rect(bx, y - size * 0.75 + i * lh, w, size * 0.7, '#D9D9D9', r=2)
        return len(baris) * lh
    return s.text(x, y, teks, size, weight, warna, anchor, nama=nama, maks=maks, lh=lh)


def judul(s, T, x, y, teks, size=20, weight=700, warna=None, maks=None, anchor='start', nama=None):
    if T.hi:
        weight = T.wj if weight >= 700 else weight
    return s.text(x, y, teks, size, weight, warna or T.teks, anchor, nama=nama or f'Judul/{teks[:30]}', maks=maks, lh=round(size * 1.3), fam=T.fj)


def bayangan(s, T, x, y, w, h, r, d=4):
    """Bayangan sesuai gaya: blok tinta (brutalism/retro/manga), lembut (modern/kaca), atau clay.
    Dibuat dari bentuk biasa (bukan filter) agar utuh saat diimpor ke Figma; di Figma bisa diganti Drop shadow."""
    if not T.hi or not T.bayang:
        return
    if T.bayang == 'blok':
        s.rect(x + d, y + d, w, h, T.garis, r=r, nama='Bayangan blok')
    elif T.bayang == 'lembut':
        with s.g('Bayangan lembut'):
            s.rect(x, y + 2, w, h, '#0000000F', r=r)
            s.rect(x + 2, y + d + 2, w - 4, h, '#0000000A', r=r)
    elif T.bayang == 'clay':
        with s.g('Bayangan clay'):
            s.rect(x + 2, y + d + 4, w - 4, h, T.primer + '33', r=r)


def screentone(s, x, y, w, h, jarak=10, r=1.6, warna='#121212', op=0.18, nama='Screentone'):
    """Titik halftone khas manga, digambar sebagai lingkaran vektor agar tetap utuh di Figma."""
    with s.g(nama):
        baris = 0
        yy = y
        while yy < y + h:
            xx = x + (jarak / 2 if baris % 2 else 0)
            while xx < x + w:
                s.circle(xx, yy, r, warna + format(int(op * 255), '02X'))
                xx += jarak
            yy += jarak * 0.87
            baris += 1


def garis_cepat(s, cx, cy, r1, r2, n=28, warna='#121212', sw=2, nama='Garis kecepatan'):
    """Speed lines/focus lines manga yang memusat ke satu titik."""
    import math
    with s.g(nama):
        for i in range(n):
            a = 2 * math.pi * i / n + (0.05 if i % 2 else 0)
            rr = r1 + (i % 3) * 12
            s.line(cx + rr * math.cos(a), cy + rr * math.sin(a), cx + r2 * math.cos(a), cy + r2 * math.sin(a), warna, sw if i % 3 else sw * 1.6)


def gelembung(s, T, x, y, w, h, ekor='bawah-kiri', nama='Gelembung dialog'):
    """Balon kata manga: kotak membulat dengan ekor."""
    with s.g(nama):
        r = min(h / 2, 22)
        ex = x + 28 if 'kiri' in ekor else x + w - 44
        d = (f'M{x + r:g} {y:g}H{x + w - r:g}A{r:g} {r:g} 0 0 1 {x + w:g} {y + r:g}V{y + h - r:g}A{r:g} {r:g} 0 0 1 {x + w - r:g} {y + h:g}'
             f'H{ex + 22:g}L{ex + 6:g} {y + h + 16:g}L{ex + 8:g} {y + h:g}H{x + r:g}A{r:g} {r:g} 0 0 1 {x:g} {y + h - r:g}V{y + r:g}A{r:g} {r:g} 0 0 1 {x + r:g} {y:g}Z')
        s.path(d, fill=T.permukaan, stroke=T.garis if T.manga else T.garis, sw=T.sw if T.manga else 1)


def tombol(s, T, x, y, w, h, label, varian='primer', ikon=None, nama=None, state='default'):
    with s.g(nama or f'Tombol/{label}'):
        if T.lo:
            fill, stroke, tw = ('#E0E0E0', '#777', '#333') if varian == 'primer' else ('#FFFFFF', '#999', '#555')
            if varian == 'teks': fill, stroke = 'none', None
        else:
            isi = {'primer': T.primer, 'sekunder': T.lembut, 'garis': T.permukaan, 'teks': 'none', 'bahaya': T.bahaya}[varian]
            if state == 'hover' and varian == 'primer': isi = T.primer2
            if state == 'tekan' and varian == 'primer': isi = T.primer2
            fill = isi
            stroke = T.primer if varian == 'garis' else None
            tw = T.di_atas(isi) if varian in ('primer', 'bahaya') else (T.primer if varian in ('garis', 'teks') else T.primer2)
            if state == 'nonaktif':
                fill, stroke, tw = (T.garis, None, T.teks2) if varian != 'teks' else ('none', None, T.teks2)
        if T.manga and varian in ('primer', 'garis', 'bahaya') and state not in ('nonaktif', 'tekan'):
            bayangan(s, T, x, y, w, h, min(T.r, h / 2), 3)
        if T.manga and varian != 'teks':
            stroke = T.garis
        s.rect(x, y, w, h, fill, r=min(T.r, h / 2), stroke=stroke, sw=T.sw if T.manga else (1.5 if varian == 'garis' else 1), nama='Latar tombol')
        if state == 'fokus' and not T.lo:
            s.rect(x - 3, y - 3, w + 6, h + 6, 'none', r=min(T.r, h / 2) + 3, stroke=T.info, sw=2, nama='Cincin fokus')
        size = 15 if h >= 44 else 13
        tl = lebar_teks(label, size, 600) + (26 if ikon else 0)
        tx = x + (w - tl) / 2
        if ikon:
            s.ikon(ikon, tx, y + (h - 18) / 2, 18, tw)
            tx += 26
        s.text(tx, y + h / 2 + size * 0.36, label, size, 600, tw, nama='Label')
        if state == 'memuat' and not T.lo:
            s.circle(x + w - 24, y + h / 2, 7, 'none', stroke=tw, sw=2, nama='Spinner')


def masukan(s, T, x, y, w, label, nilai='', placeholder='', state='default', pesan=None, ikon=None, kanan=None, nama=None, h=48):
    with s.g(nama or f'Input/{label}'):
        s.text(x, y + 13, label, 13, 600, T.teks, nama='Label') if not T.lo else para(s, T, x, y + 13, label, 13, 600, paksa=True)
        by = y + 22
        warna_garis = {'default': T.garis, 'fokus': T.primer, 'error': T.bahaya, 'nonaktif': T.garis, 'terisi': T.garis}[state]
        if T.lo: warna_garis = '#999'
        if T.manga and state == 'default': warna_garis = T.garis
        s.rect(x, by, w, h, T.lembut if state == 'nonaktif' else T.permukaan, r=min(T.r, 10), stroke=warna_garis, sw=max(T.sw, 2 if state in ('fokus', 'error') else 1), nama='Kotak input')
        tx = x + 14
        if ikon:
            s.ikon(ikon, tx, by + (h - 20) / 2, 20, T.teks2)
            tx += 30
        isi = nilai or placeholder
        if isi:
            s.text(tx, by + h / 2 + 5, isi, 15, 400, T.teks if nilai else T.teks2, nama='Nilai' if nilai else 'Placeholder')
        if state == 'fokus' and not T.lo:
            cx = tx + lebar_teks(nilai, 15) + 2
            s.line(cx, by + 14, cx, by + h - 14, T.primer, 1.5, nama='Kursor')
        if kanan:
            s.ikon(kanan, x + w - 34, by + (h - 20) / 2, 20, T.teks2)
        if pesan:
            warna = T.bahaya if state == 'error' else T.teks2
            if state == 'error' and not T.lo:
                s.ikon('alert', x, by + h + 6, 16, warna)
                s.text(x + 22, by + h + 19, pesan, 12, 500, warna, nama='Pesan error')
            else:
                para(s, T, x, by + h + 19, pesan, 12, 400, warna, nama='Pesan bantuan')
    return 22 + h + (26 if pesan else 0)


def gambar(s, T, x, y, w, h, warna='#B07A52', label='Foto', jenis='kopi', r=None, nama=None):
    r = T.r if r is None else r
    with s.g(nama or f'Gambar/{label}'):
        if T.lo:
            s.rect(x, y, w, h, '#F2F2F2', r=r, stroke='#999', nama='Bingkai')
            s.line(x, y, x + w, y + h, '#BBB', 1)
            s.line(x + w, y, x, y + h, '#BBB', 1)
            return
        if T.fid == 'mid':
            s.rect(x, y, w, h, '#D4D4D4', r=r, nama='Bingkai')
            s.text(x + w / 2, y + h / 2 + 4, label, 12, 500, '#6E6E6E', 'middle', nama='Keterangan')
            return
        s.rect(x, y, w, h, warna, r=r, stroke=T.garis if T.manga else None, sw=T.sw, nama='Latar foto')
        if T.komik:
            screentone(s, x + 6, y + 6, w * 0.45, h * 0.4, 9, 1.4, '#FFFFFF', 0.35)
        m = min(w, h)
        cx, cy = x + w / 2, y + h / 2
        terang = '#FFFFFF'
        if jenis.startswith('ikon:'):
            k = m * 0.42
            s.circle(cx, cy, k * 0.85, '#FFFFFF33', nama='Lingkar')
            s.ikon(jenis[5:], cx - k / 2, cy - k / 2, k, '#FFFFFF', 2)
        elif jenis == 'kopi':
            k = m * 0.42
            s.rect(cx - w / 2, y + h * 0.72, w, h * 0.28, '#00000014', r=0, nama='Meja')
            s.path(f'M{cx - k / 2:g} {cy - k * 0.35:g}h{k:g}v{k * 0.5:g}a{k * 0.5:g} {k * 0.45:g} 0 0 1-{k:g} 0z', fill='#FFFFFFE6', nama='Cangkir')
            s.path(f'M{cx + k / 2:g} {cy - k * 0.2:g}h{k * 0.12:g}a{k * 0.16:g} {k * 0.16:g} 0 0 1 0 {k * 0.32:g}h-{k * 0.12:g}', stroke='#FFFFFFE6', sw=max(2, k * 0.06), nama='Gagang')
            s.rect(cx - k * 0.42, cy - k * 0.35, k * 0.84, k * 0.1, '#5A3420', r=k * 0.05, nama='Permukaan kopi')
            for i, dx in enumerate((-0.18, 0.0, 0.18)):
                s.path(f'M{cx + k * dx:g} {cy - k * 0.5:g}c{k * 0.08:g} -{k * 0.1:g} -{k * 0.08:g} -{k * 0.18:g} 0 -{k * 0.3:g}', stroke='#FFFFFF99', sw=max(1.5, k * 0.035), nama=f'Uap {i + 1}')
        elif jenis == 'orang':
            s.circle(cx, cy - m * 0.12, m * 0.18, '#FFFFFFCC', nama='Kepala')
            s.path(f'M{cx - m * 0.32:g} {y + h:g}a{m * 0.32:g} {m * 0.3:g} 0 0 1 {m * 0.64:g} 0z', fill='#FFFFFFCC', nama='Badan')
        elif jenis == 'peta':
            for i in range(1, 4):
                s.line(x, y + h * i / 4, x + w, y + h * (i / 4) + 18, '#FFFFFF80', 6)
                s.line(x + w * i / 4, y, x + w * i / 4 - 20, y + h, '#FFFFFF80', 6)
            s.path(f'M{cx:g} {cy + 16:g}s-14-12.4-14-23a14 14 0 0 1 28 0c0 10.6-14 23-14 23z', fill='#B3261E', nama='Penanda')
            s.circle(cx, cy - 7, 5, '#FFFFFF')
        else:
            s.circle(x + w * 0.3, y + h * 0.32, m * 0.09, '#FFFFFFAA', nama='Matahari')
            s.path(f'M{x:g} {y + h:g}L{x + w * 0.38:g} {y + h * 0.45:g}L{x + w * 0.62:g} {y + h * 0.75:g}L{x + w * 0.78:g} {y + h * 0.58:g}L{x + w:g} {y + h:g}z', fill='#FFFFFF66', nama='Bukit')


def chip(s, T, x, y, label, aktif=False, ikon=None, nama=None):
    w = lebar_teks(label, 13, 600) + 28 + (22 if ikon else 0)
    with s.g(nama or f'Chip/{label}'):
        if T.lo:
            s.rect(x, y, w, 34, '#E0E0E0' if aktif else '#FFF', r=17, stroke='#999')
        else:
            s.rect(x, y, w, 34, T.primer if aktif else T.permukaan, r=17, stroke=None if aktif else T.garis)
        tx = x + 14
        warna = (T.di_atas(T.primer) if aktif and not T.lo else T.teks)
        if ikon:
            s.ikon(ikon, tx, y + 8, 18, warna)
            tx += 22
        s.text(tx, y + 22, label, 13, 600, warna, nama='Label')
    return w


def badge(s, T, x, y, label, jenis='info', nama=None):
    warna = {'info': (T.lembut, T.primer2), 'sukses': ('#E3F4EA', T.sukses), 'bahaya': ('#FBE5E3', T.bahaya),
             'peringatan': ('#FFF3D6', T.peringatan), 'aksen': (T.aksen, T.di_atas(T.aksen))}[jenis]
    if not T.hi: warna = ('#E6E6E6', '#444')
    w = lebar_teks(label, 11, 700) + 16
    with s.g(nama or f'Badge/{label}'):
        s.rect(x, y, w, 22, warna[0], r=11)
        s.text(x + 8, y + 15, label, 11, 700, warna[1], nama='Label')
    return w


def status_bar(s, T, w=HP_W, gelap=False):
    warna = '#FFFFFF' if gelap else T.teks
    with s.g('Status bar'):
        s.text(28, 32, '9:41', 15, 600, warna, nama='Jam')
        s.rect(w - 70, 22, 18, 11, warna, r=2, nama='Sinyal')
        s.rect(w - 46, 21, 24, 12, 'none', r=3, stroke=warna, sw=1.2, nama='Baterai')
        s.rect(w - 44, 23, 17, 8, warna, r=1.5)


def appbar(s, T, judul_teks, kiri='back', kanan=(), w=HP_W, y=44):
    with s.g('App bar'):
        if kiri:
            s.ikon(kiri, 16, y + 14, 24, T.teks)
        s.text(w / 2, y + 32, judul_teks, 17, 700, T.teks, 'middle', nama='Judul')
        for i, ik in enumerate(kanan):
            s.ikon(ik, w - 40 - i * 36, y + 14, 24, T.teks)
    return y + 52


def nav_bawah(s, T, items, aktif=0, w=HP_W, h=HP_H):
    tinggi = 84
    with s.g('Bottom navigation', 0, h - tinggi):
        s.rect(0, 0, w, tinggi, T.permukaan, nama='Latar')
        s.line(0, 0, w, 0, T.garis, 1)
        lw = w / len(items)
        for i, (ik, lb) in enumerate(items):
            warna = T.primer if (i == aktif and T.hi) else (T.teks if i == aktif else T.teks2)
            with s.g(f'Tab/{lb}'):
                s.ikon(ik, lw * i + lw / 2 - 12, 10, 24, warna)
                s.text(lw * i + lw / 2, 50, lb, 11, 700 if i == aktif else 500, warna, 'middle', nama='Label')
        s.rect(w / 2 - 67, tinggi - 13, 134, 5, T.teks, r=2.5, nama='Home indicator')


def stepper(s, T, x, y, n, nama='Stepper jumlah'):
    with s.g(nama):
        s.rect(x, y, 104, 36, T.permukaan, r=18, stroke=T.garis, sw=T.sw)
        s.ikon('minus', x + 8, y + 8, 20, T.teks)
        s.text(x + 52, y + 24, str(n), 15, 700, T.teks, 'middle', nama='Jumlah')
        s.circle(x + 86, y + 18, 14, T.primer if not T.lo else '#E0E0E0')
        s.ikon('plus', x + 77, y + 9, 18, T.di_atas(T.primer) if not T.lo else '#333')


def segmen(s, T, x, y, w, opsi, aktif=0, nama='Segmented control'):
    with s.g(nama):
        s.rect(x, y, w, 40, T.lembut, r=min(T.r, 20))
        sw = (w - 8) / len(opsi)
        for i, o in enumerate(opsi):
            if i == aktif:
                s.rect(x + 4 + i * sw, y + 4, sw, 32, T.permukaan, r=min(T.r - 2, 16), stroke=T.garis if T.lo else None, nama='Terpilih')
            s.text(x + 4 + i * sw + sw / 2, y + 25, o, 13, 700 if i == aktif else 500, T.teks if i == aktif else T.teks2, 'middle', nama=f'Opsi/{o}')


def radio(s, T, x, y, w, label, sub='', pilih=False, ikon=None, nama=None):
    with s.g(nama or f'Opsi/{label}'):
        if pilih: bayangan(s, T, x, y, w, 64, T.r, 3)
        s.rect(x, y, w, 64, T.lembut if (pilih and T.manga) else T.permukaan, r=T.r, stroke=T.garis if T.manga else (T.primer if (pilih and not T.lo) else T.garis), sw=T.sw if T.manga else (2 if pilih else 1))
        tx = x + 16
        if ikon:
            s.rect(tx, y + 14, 36, 36, T.lembut, r=8)
            s.ikon(ikon, tx + 6, y + 20, 24, T.primer2 if T.hi else T.teks)
            tx += 50
        s.text(tx, y + 29, label, 15, 600, T.teks, nama='Label')
        if sub:
            para(s, T, tx, y + 48, sub, 12, 400, T.teks2)
        s.circle(x + w - 28, y + 32, 10, T.permukaan, stroke=T.primer if (pilih and not T.lo) else T.teks2, sw=2)
        if pilih:
            s.circle(x + w - 28, y + 32, 5, T.primer if not T.lo else '#555')


def kartu_produk(s, T, x, y, w, nama, info, harga, warna, favorit=False, label=None):
    h = w * 0.9
    with s.g(f'Kartu produk/{nama}'):
        bayangan(s, T, x, y, w, h + 104, T.r)
        s.rect(x, y, w, h + 104, T.permukaan, r=T.r, stroke=T.garis, sw=T.sw, nama='Latar kartu')
        gambar(s, T, x + 8, y + 8, w - 16, h - 8, warna, 'Foto ' + nama, r=T.r - 4)
        if label:
            badge(s, T, x + 16, y + 16, label, 'aksen')
        if favorit:
            s.circle(x + w - 28, y + 28, 15, '#FFFFFFE6')
            s.ikon('heart', x + w - 38, y + 18, 20, T.bahaya if T.hi else T.teks)
        s.text(x + 12, y + h + 24, nama, 15, 700, T.teks, nama='Nama produk')
        para(s, T, x + 12, y + h + 44, info, 12, 400, T.teks2, nama='Info')
        s.text(x + 12, y + h + 82, harga, 15, 700, T.primer2 if T.hi else T.teks, nama='Harga')
        s.circle(x + w - 26, y + h + 76, 16, T.primer if not T.lo else '#E0E0E0', nama='Tombol tambah')
        s.ikon('plus', x + w - 36, y + h + 66, 20, T.di_atas(T.primer) if not T.lo else '#333')
    return h + 104


def baris_list(s, T, x, y, w, nama, sub, harga, warna, aksi='plus'):
    with s.g(f'Item/{nama}'):
        gambar(s, T, x, y, 76, 76, warna, 'Foto', r=T.r - 2)
        s.text(x + 90, y + 22, nama, 15, 700, T.teks, nama='Nama')
        para(s, T, x + 90, y + 42, sub, 12, 400, T.teks2, maks=w - 160)
        s.text(x + 90, y + 70, harga, 15, 700, T.primer2 if T.hi else T.teks, nama='Harga')
        if aksi == 'plus':
            s.circle(x + w - 18, y + 58, 16, T.primer if not T.lo else '#E0E0E0', nama='Tombol tambah')
            s.ikon('plus', x + w - 28, y + 48, 20, T.di_atas(T.primer) if not T.lo else '#333')
        elif aksi == 'stepper':
            stepper(s, T, x + w - 104, y + 40, 1)
    return 76


def skeleton(s, x, y, w, h, r=8, nama='Skeleton'):
    s.rect(x, y, w, h, '#ECE6E0', r=r, nama=nama)


def dialog(s, T, x, y, w, judul_teks, isi, aksi1, aksi2=None, ikon='alert', warna_ikon=None):
    with s.g('Dialog'):
        s.rect(x, y, w, 0, T.permukaan)
        tinggi = 236 if aksi2 else 190
        bayangan(s, T, x, y, w, tinggi, T.r + 4, 6)
        s.rect(x, y, w, tinggi, T.permukaan, r=T.r + 4, stroke=T.garis if T.manga else None, sw=T.sw, nama='Latar dialog')
        s.circle(x + w / 2, y + 40, 22, '#FBE5E3' if T.hi else T.lembut)
        s.ikon(ikon, x + w / 2 - 12, y + 28, 24, warna_ikon or (T.bahaya if T.hi else T.teks))
        s.text(x + w / 2, y + 88, judul_teks, 17, 700, T.teks, 'middle', nama='Judul')
        para(s, T, x + w / 2, y + 112, isi, 13, 400, T.teks2, anchor='middle')
        tombol(s, T, x + 20, y + 132, w - 40, 44, aksi1)
        if aksi2:
            tombol(s, T, x + 20, y + 184, w - 40, 40, aksi2, 'teks')


def toast(s, T, x, y, w, teks, jenis='sukses'):
    with s.g(f'Toast/{jenis}'):
        s.rect(x, y, w, 52, '#2B2724' if T.hi else '#333', r=T.r)
        s.ikon('check' if jenis == 'sukses' else 'alert', x + 16, y + 14, 24, '#8BD7A8' if (T.hi and jenis == 'sukses') else '#FFFFFF')
        s.text(x + 52, y + 31, teks, 14, 500, '#FFFFFF', nama='Pesan')


def avatar(s, T, cx, cy, r, inisial, warna=None):
    with s.g(f'Avatar/{inisial}'):
        s.circle(cx, cy, r, warna or (T.aksen if T.hi else '#D0D0D0'))
        s.text(cx, cy + r * 0.36, inisial, r * 0.9, 700, T.teks, 'middle', nama='Inisial')


def langkah_status(s, T, x, y, w, langkah, aktif):
    with s.g('Status pesanan'):
        n = len(langkah)
        dx = (w - 24) / (n - 1)
        s.line(x + 12, y + 12, x + 12 + dx * (n - 1), y + 12, T.garis, 3)
        s.line(x + 12, y + 12, x + 12 + dx * aktif, y + 12, T.sukses if T.hi else T.teks, 3)
        for i, lb in enumerate(langkah):
            cx = x + 12 + dx * i
            selesai = i <= aktif
            s.circle(cx, y + 12, 12, (T.sukses if T.hi else T.teks) if selesai else T.permukaan, stroke=None if selesai else T.garis, sw=2)
            if selesai:
                s.ikon('check', cx - 8, y + 4, 16, '#FFFFFF')
            s.text(cx, y + 44, lb, 11, 600 if i == aktif else 500, T.teks if selesai else T.teks2, 'middle', nama=f'Langkah/{lb}')


def kerangka_hp(nama, T, latar=None):
    s = Svg(HP_W, HP_H, nama, latar or T.latar)
    return s


# ---------------------------------------------------------------- web
def navbar_web(s, T, w, menu, cta, logo=None, y=0):
    with s.g('Navbar', 0, y):
        s.rect(0, 0, w, 80, T.permukaan, nama='Latar navbar')
        s.line(0, 80, w, 80, T.garis, 1)
        with s.g('Logo'):
            s.circle(120 + 18, 40, 18, T.primer if not T.lo else '#DDD')
            s.ikon('cup', 120 + 7, 29, 22, T.di_atas(T.primer) if not T.lo else '#444')
            s.text(120 + 46, 47, logo or T.nama, 20, 800, T.teks, nama='Nama brand')
        x = w / 2 - sum(lebar_teks(m, 15, 500) + 40 for m in menu) / 2 + 40
        with s.g('Menu'):
            for i, m in enumerate(menu):
                s.text(x, 46, m, 15, 600 if i == 0 else 500, T.teks if i == 0 else T.teks2, nama=f'Menu/{m}')
                x += lebar_teks(m, 15, 500) + 40
        tombol(s, T, w - 120 - 150, 18, 150, 44, cta)


def footer_web(s, T, w, y, kolom, hak):
    with s.g('Footer', 0, y):
        s.rect(0, 0, w, 280, '#2B2724' if T.hi else ('#3A3A3A' if T.fid == 'mid' else '#F0F0F0'), nama='Latar footer')
        warna = '#FFFFFF' if not T.lo else '#444'
        warna2 = '#CFC6BE' if T.hi else ('#BBBBBB' if T.fid == 'mid' else '#888')
        s.text(120, 72, T.nama, 22, 800, warna, nama='Brand')
        para(s, T, 120, 104, 'Roastery lokal dari Medan. Biji kopi Nusantara pilihan, dipanggang setiap minggu.', 14, 400, warna2, maks=300)
        x = 520
        for jud, isi in kolom:
            with s.g(f'Kolom/{jud}'):
                s.text(x, 72, jud, 14, 700, warna, nama='Judul kolom')
                for i, t in enumerate(isi):
                    para(s, T, x, 104 + i * 30, t, 14, 400, warna2)
            x += 220
        s.line(120, 216, w - 120, 216, '#FFFFFF22' if not T.lo else '#CCC', 1)
        para(s, T, 120, 250, hak, 13, 400, warna2)
