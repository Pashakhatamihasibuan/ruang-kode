"""Kode final standar industri untuk proyek slicing: dibangkitkan dari spesifikasi desain yang sama dengan kit Figma
(tools/figma/proyek_data.py), sehingga hasil kodenya sama susunan, isi, dan tokennya dengan desain di ZIP.
- web_final(spec): HTML semantik + CSS (token, base, komponen, mobile-first + breakpoint) + JS + tooling + test.
- flutter_final(spec): proyek Flutter (tema dari token, layar, widget, test) yang lolos `flutter analyze`."""
import html as _h
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'figma'))
from svgkit import Tema, FONT  # noqa: E402

e = _h.escape


def palet(spec):
    T = Tema('hi', **spec['token'], gaya=spec['gaya'])
    return T


def slug(s):
    s = s.lower()
    for a, b in (('à', 'a'), ('é', 'e')):
        s = s.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


# ====================================================================== WEB
IKON = {  # ikon SVG 24px (garis) yang dipakai blok web; aria-hidden karena selalu didampingi teks
    'sparkle': 'M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z', 'edit': 'M4 20h4L19 9l-4-4L4 16zM14 6l4 4',
    'globe': 'M12 3a9 9 0 100 18 9 9 0 000-18zM3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18', 'send': 'M4 12l16-8-6 16-2-6z',
    'receipt': 'M6 3h12v18l-3-2-3 2-3-2-3 2zM9 8h6M9 12h6', 'chart': 'M4 20V10M10 20V4M16 20v-7M22 20H2', 'star': 'M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z',
    'user': 'M12 12a4 4 0 100-8 4 4 0 000 8zM4 21a8 8 0 0116 0', 'alert': 'M12 3l10 18H2zM12 10v4M12 17v.5', 'info': 'M12 3a9 9 0 100 18 9 9 0 000-18zM12 11v6M12 7v.5',
    'mail': 'M3 6h18v12H3zM3 7l9 6 9-6', 'phone': 'M6 3h4l2 5-3 2a11 11 0 005 5l2-3 5 2v4a2 2 0 01-2 2A17 17 0 014 5a2 2 0 012-2',
    'doc': 'M6 3h9l4 4v14H6zM14 3v5h5M9 13h6M9 17h6', 'search': 'M11 4a7 7 0 100 14 7 7 0 000-14zM20 20l-4-4',
    'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z', 'list': 'M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01',
    'calendar': 'M4 5h16v16H4zM4 9h16M8 3v4M16 3v4', 'settings': 'M12 9a3 3 0 100 6 3 3 0 000-6zM12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2',
    'bag': 'M5 8h14l-1 13H6zM9 8V6a3 3 0 016 0v2', 'bike': 'M5 17a3 3 0 100-6 3 3 0 000 6zM19 17a3 3 0 100-6 3 3 0 000 6zM5 14l4-7h5l5 7M9 7l3 7',
    'chat': 'M4 5h16v11H9l-5 4z', 'wallet': 'M3 7h18v12H3zM3 7l13-4v4M16 13h2', 'refresh': 'M20 11a8 8 0 10-2 6M20 4v7h-7',
    'cart': 'M3 4h2l2 12h12l2-8H6M9 20h.01M18 20h.01', 'pin': 'M12 21s-7-6-7-12a7 7 0 0114 0c0 6-7 12-7 12zM12 11a2 2 0 100-4 2 2 0 000 4z',
    'heart': 'M12 20s-8-5-8-11a4 4 0 018-1 4 4 0 018 1c0 6-8 11-8 11z', 'home': 'M3 11l9-7 9 7v9H3zM9 20v-6h6v6', 'menu': 'M4 7h16M4 12h16M4 17h16',
    'x': 'M6 6l12 12M18 6L6 18', 'cup': 'M5 8h12v5a6 6 0 01-12 0zM17 9h2a2 2 0 010 4h-2',
}


def ik(n, cls='ik'):
    d = IKON.get(n, IKON['sparkle'])
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="{d}"/></svg>'


def _id(t):
    return slug(t)[:40] or 'bagian'


def wb_navbar(d, sp):
    menu = ''.join(f'<li><a href="#{_id(m)}">{e(m)}</a></li>' for m in d['menu'])
    return (f'<header class="navbar">\n  <div class="wadah navbar__isi">\n    <a class="logo" href="./">{ik(d.get("logo_ikon", "sparkle"))}<span>{e(sp["token"]["nama"])}</span></a>\n'
            f'    <button class="navbar__toggle" type="button" aria-expanded="false" aria-controls="menu-utama">{ik("menu")}<span class="sr">Buka menu</span></button>\n'
            f'    <nav id="menu-utama" class="navbar__menu" aria-label="Utama">\n      <ul>{menu}</ul>\n      <a class="tombol tombol--primer" href="#kontak">{e(d["cta"])}</a>\n    </nav>\n  </div>\n</header>')


def wb_topbar(d, sp):
    tb = f'\n  <button class="tombol tombol--primer" type="button">{e(d["cta"])}</button>' if d.get('cta') else ''
    return f'<header class="topbar">\n  <div class="topbar__judul"><h1>{e(d["jd"])}</h1><p>{e(d.get("sub", ""))}</p></div>{tb}\n</header>'


def wb_hero(d, sp):
    return (f'<section class="hero" aria-labelledby="hero-judul">\n  <div class="wadah hero__isi">\n    <div class="hero__teks">\n'
            f'      <p class="lencana">{e(d.get("badge_teks", ""))}</p>\n      <h1 id="hero-judul">{e(d["jd"])}</h1>\n      <p class="hero__sub">{e(d["sub"])}</p>\n'
            f'      <div class="aksi"><a class="tombol tombol--primer" href="#{_id("koleksi")}">{e(d["cta1"])}</a><a class="tombol tombol--garis" href="#cara">{e(d.get("cta2", ""))}</a></div>\n'
            + (f'      <p class="bukti">{ik("star")} {e(d["bukti"])}</p>\n' if d.get('bukti') else '')
            + f'    </div>\n    <div class="hero__media" role="img" aria-label="Ilustrasi {e(sp["token"]["nama"])}" style="--warna:{d.get("warna", sp["token"]["primer"])}">{ik(d.get("ikon", "sparkle"), "ik ik--besar")}</div>\n  </div>\n</section>')


def wb_fitur(d, sp):
    li = ''.join(f'\n      <li class="fitur__item">{ik(i)}<h3>{e(j)}</h3><p>{e(t)}</p></li>' for i, j, t in d['items'])
    return f'<section class="bagian" id="{_id(d["jd"])}" aria-labelledby="h-{_id(d["jd"])}">\n  <div class="wadah">\n    <h2 id="h-{_id(d["jd"])}">{e(d["jd"])}</h2>\n    <ul class="fitur" role="list">{li}\n    </ul>\n  </div>\n</section>'


def wb_kartu(d, sp):
    out = []
    for n, sub, harga, w, i, badge in d['items']:
        out.append(f'\n      <li>\n        <article class="kartu">\n          <div class="kartu__media" style="--warna:{w}" role="img" aria-label="Foto {e(n)}">{ik(i, "ik ik--besar")}'
                   + (f'<span class="lencana lencana--di-atas">{e(badge)}</span>' if badge else '') +
                   f'</div>\n          <h3 class="kartu__judul">{e(n)}</h3>\n          <p class="kartu__sub">{e(sub)}</p>\n          <p class="kartu__harga">{e(harga)}</p>\n'
                   f'          <button class="tombol tombol--primer tombol--penuh" type="button" data-tambah="{e(n)}">Tambah ke keranjang</button>\n        </article>\n      </li>')
    return f'<section class="bagian" id="{_id(d["jd"])}" aria-labelledby="h-{_id(d["jd"])}">\n  <div class="wadah">\n    <h2 id="h-{_id(d["jd"])}">{e(d["jd"])}</h2>\n    <ul class="grid-kartu" role="list">{"".join(out)}\n    </ul>\n  </div>\n</section>'


def wb_testimoni(d, sp):
    li = ''.join(f'\n      <li><figure class="testimoni"><blockquote>“{e(t)}”</blockquote><figcaption><b>{e(n)}</b><span>{e(r)}</span></figcaption></figure></li>' for n, r, t in d['items'])
    return f'<section class="bagian bagian--lembut" aria-label="Testimoni">\n  <div class="wadah">\n    <h2>Kata mereka</h2>\n    <ul class="grid-testimoni" role="list">{li}\n    </ul>\n  </div>\n</section>'


def wb_cta(d, sp):
    return (f'<section class="cta" id="kontak" aria-labelledby="cta-judul">\n  <div class="wadah cta__isi">\n    <div><h2 id="cta-judul">{e(d["jd"])}</h2><p>{e(d["sub"])}</p></div>\n'
            f'    <a class="tombol tombol--aksen" href="https://wa.me/6281234567890" rel="noopener">{e(d["cta"])}</a>\n  </div>\n</section>')


def wb_footer(d, sp):
    kol = ''.join(f'\n      <nav aria-label="{e(j)}"><h3>{e(j)}</h3><ul>' + ''.join(f'<li><a href="#">{e(x)}</a></li>' for x in xs) + '</ul></nav>' for j, xs in d['kolom'])
    return (f'<footer class="kaki">\n  <div class="wadah kaki__isi">\n    <div class="kaki__merek"><a class="logo" href="./">{ik("sparkle")}<span>{e(sp["token"]["nama"])}</span></a><p>{e(sp["brief"].split(".")[0])}.</p></div>{kol}\n  </div>\n'
            f'  <p class="wadah kaki__hak">{e(d["hak"])}</p>\n</footer>')


def _field(i, f):
    label, nilai, ph, st, pesan, ikon = f
    fid = f'f-{i}-{slug(label)}'
    jenis = 'email' if 'mail' in label.lower() else 'tel' if 'whatsapp' in label.lower() or 'hp' in label.lower() else 'text'
    angka = ' inputmode="numeric"' if re.search(r'\d', nilai or '') and jenis == 'text' else ''
    err = st == 'error'
    bantuan = f'<p class="field__pesan{" field__pesan--error" if err else ""}" id="{fid}-pesan">{e(pesan)}</p>' if pesan else f'<p class="field__pesan" id="{fid}-pesan" hidden></p>'
    return (f'\n        <div class="field{" field--error" if err else ""}">\n          <label for="{fid}">{e(label)}</label>\n          <div class="field__kotak">{ik(ikon or "edit")}'
            f'<input id="{fid}" name="{slug(label)}" type="{jenis}"{angka} value="{e(nilai or "")}" placeholder="{e(ph or "")}" required aria-describedby="{fid}-pesan"{" aria-invalid=\"true\"" if err else ""}></div>\n          {bantuan}\n        </div>')


def wb_form(d, sp):
    fs = ''.join(_field(i, f) for i, f in enumerate(d['fields']))
    samping = ''
    if d.get('samping'):
        j, rows = d['samping']
        samping = f'\n    <aside class="ringkasan" aria-labelledby="ringkasan-judul"><h2 id="ringkasan-judul">{e(j)}</h2><ul>' + ''.join(f'<li>{e(r)}</li>' for r in rows) + '</ul></aside>'
    return (f'<section class="bagian" aria-labelledby="form-judul">\n  <div class="wadah form-tata">\n    <form class="form" novalidate data-validasi>\n      <h1 id="form-judul">{e(d["jd"])}</h1>\n      <p class="form__sub">{e(d.get("sub", ""))}</p>{fs}\n'
            f'      <button class="tombol tombol--primer tombol--penuh" type="submit">{e(d["cta"])}</button>\n      <p class="form__status" role="status" aria-live="polite"></p>\n    </form>{samping}\n  </div>\n</section>')


def wb_statistik(d, sp):
    li = ''.join(f'\n      <div class="stat">{ik(i)}<dt>{e(lb)}</dt><dd>{e(v)}' + (f' <span class="stat__ubah{" stat__ubah--turun" if u.startswith("-") else ""}">{e(u)}</span>' if u else '') + '</dd></div>' for lb, v, u, i in d['items'])
    return f'<section class="bagian bagian--rapat" aria-label="Ringkasan angka">\n  <div class="wadah">\n    <dl class="grid-stat">{li}\n    </dl>\n  </div>\n</section>'


def wb_grafik(d, sp):
    data, lab = d['data'], d['label']
    lo, hi = min(data), max(data)
    lo = lo - (hi - lo) * 0.25 if hi > lo else 0
    w, h = 600, 220
    bw = w / len(data)
    bar = ''.join(f'<rect x="{i * bw + bw * .18:.1f}" y="{h - (v - lo) / (hi - lo or 1) * (h - 20):.1f}" width="{bw * .64:.1f}" height="{(v - lo) / (hi - lo or 1) * (h - 20):.1f}" rx="4"><title>{e(lab[i])}: {v}</title></rect>' for i, v in enumerate(data))
    lbl = ''.join(f'<text x="{i * bw + bw / 2:.1f}" y="{h + 18}">{e(lab[i])}</text>' for i in range(len(data)))
    tabel = '<div class="sr"><table><caption>' + e(d['jd']) + '</caption><tr>' + ''.join(f'<th scope="col">{e(x)}</th>' for x in lab) + '</tr><tr>' + ''.join(f'<td>{v}</td>' for v in data) + '</tr></table></div>'
    return (f'<section class="bagian bagian--rapat" aria-labelledby="g-{_id(d["jd"])}">\n  <div class="wadah">\n    <figure class="grafik">\n      <figcaption id="g-{_id(d["jd"])}">{e(d["jd"])}</figcaption>\n'
            f'      <svg viewBox="0 0 {w} {h + 24}" role="img" aria-labelledby="g-{_id(d["jd"])}" preserveAspectRatio="none">{bar}{lbl}</svg>\n      {tabel}\n    </figure>\n  </div>\n</section>')


def wb_tabel(d, sp):
    th = ''.join(f'<th scope="col">{e(k)}</th>' for k in d['kolom'])
    sk = d.get('status_kol')
    rows = ''
    for r in d['baris']:
        cells = ''.join((f'<th scope="row">{e(c)}</th>' if i == 0 else (f'<td><span class="status status--{slug(c)}">{e(c)}</span></td>' if sk is not None and i == sk else f'<td>{e(c)}</td>')) for i, c in enumerate(r))
        rows += f'\n          <tr>{cells}</tr>'
    return (f'<section class="bagian bagian--rapat" aria-labelledby="t-{_id(d["jd"])}">\n  <div class="wadah">\n    <h2 id="t-{_id(d["jd"])}">{e(d["jd"])}</h2>\n'
            f'    <div class="tabel-gulir" tabindex="0" role="region" aria-labelledby="t-{_id(d["jd"])}">\n      <table class="tabel">\n        <thead><tr>{th}</tr></thead>\n        <tbody>{rows}\n        </tbody>\n      </table>\n    </div>\n  </div>\n</section>')


def wb_kanban(d, sp):
    kols = []
    for j, kartu in d['kolom']:
        ks = ''.join(f'\n          <li class="tugas" tabindex="0" draggable="true" data-id="{slug(t)}" aria-describedby="petunjuk-kanban"><span class="label label--{slug(lb)}">{e(lb)}</span><p>{e(t)}</p><span class="avatar" aria-label="Penanggung jawab {e(a)}">{e(a)}</span></li>' for t, lb, a in kartu)
        kols.append(f'\n      <section class="kolom" aria-labelledby="k-{slug(j)}" data-kolom="{slug(j)}">\n        <h2 id="k-{slug(j)}">{e(j)} <span class="hitung">{len(kartu)}</span></h2>\n        <ul class="kolom__isi" role="list">{ks}\n        </ul>\n      </section>')
    return (f'<div class="kanban-wadah">\n  <p id="petunjuk-kanban" class="sr">Pilih kartu lalu tekan panah kiri atau kanan untuk memindahkan ke kolom lain.</p>\n  <div class="kanban">{"".join(kols)}\n  </div>\n  <p class="sr" role="status" aria-live="polite" id="kanban-status"></p>\n</div>')


def wb_langkah(d, sp):
    li = ''.join(f'\n      <li class="langkah__item"><span class="langkah__no" aria-hidden="true">{i + 1}</span><h3>{e(j)}</h3><p>{e(t)}</p></li>' for i, (j, t) in enumerate(d['items']))
    return f'<section class="bagian" id="cara" aria-labelledby="h-cara">\n  <div class="wadah">\n    <h2 id="h-cara">{e(d["jd"])}</h2>\n    <ol class="langkah">{li}\n    </ol>\n  </div>\n</section>'


def wb_chat(d, sp):
    ps = ''
    for p in d['pesan']:
        siapa, teks = p[0], p[1]
        sumber = p[2] if len(p) > 2 else None
        ps += (f'\n      <li class="pesan pesan--{siapa}"><p class="pesan__nama sr">{"Kamu" if siapa == "saya" else "Asisten"}</p><div class="pesan__isi"><p>{e(teks)}</p>'
               + (f'<p class="pesan__sumber">Sumber: {e(", ".join(sumber) if isinstance(sumber, (list, tuple)) else sumber)}</p>' if sumber else '') + '</div></li>')
    return (f'<section class="chat" aria-label="Percakapan">\n  <ol class="chat__log" aria-live="polite">{ps}\n  </ol>\n  <form class="chat__form" data-chat>\n    <label for="tanya" class="sr">Tulis pertanyaan</label>\n'
            f'    <textarea id="tanya" rows="1" placeholder="Tanya apa saja tentang materi…" required></textarea>\n    <button class="tombol tombol--primer" type="submit">{ik("send")}<span class="sr">Kirim</span></button>\n  </form>\n</section>')


def wb_spasi(d, sp):
    return ''


WEB = {k[3:]: v for k, v in globals().items() if k.startswith('wb_')}

CSS_KOMPONEN = '''/* ===== Navbar ===== */
.navbar { position: sticky; top: 0; z-index: 10; background: var(--permukaan); border-bottom: var(--garis-tebal) solid var(--garis); }
.navbar__isi { display: flex; align-items: center; justify-content: space-between; gap: var(--ruang-3); min-height: 64px; }
.logo { display: inline-flex; align-items: center; gap: var(--ruang-1); font: var(--berat-judul) 1.25rem/1 var(--font-judul); color: var(--primer); text-decoration: none; }
.navbar__toggle { display: inline-grid; place-items: center; width: 48px; height: 48px; border: 0; border-radius: var(--radius-kecil); background: transparent; color: var(--teks); cursor: pointer; }
.navbar__menu { display: none; position: absolute; inset: 64px 0 auto; padding: var(--ruang-2) var(--ruang-tepi) var(--ruang-3); background: var(--permukaan); border-bottom: 1px solid var(--garis); box-shadow: var(--bayang); }
.navbar__menu[data-terbuka] { display: grid; gap: var(--ruang-2); }
.navbar__menu ul { display: grid; gap: var(--ruang-1); margin: 0; padding: 0; list-style: none; }
.navbar__menu a:not(.tombol) { display: block; padding: 12px 0; color: var(--teks-2); text-decoration: none; font-weight: 500; }
.navbar__menu a:not(.tombol):hover { color: var(--primer); }

/* ===== Topbar (aplikasi) ===== */
.topbar { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--ruang-2); padding: var(--ruang-3) var(--ruang-tepi); border-bottom: 1px solid var(--garis); background: var(--permukaan); }
.topbar h1 { font-size: clamp(1.25rem, 2vw + 1rem, 1.75rem); }
.topbar p { color: var(--teks-2); }

/* ===== Hero ===== */
.hero { padding-block: var(--ruang-5); }
.hero__isi { display: grid; gap: var(--ruang-4); align-items: center; }
.hero h1 { font-size: clamp(2rem, 5vw + 1rem, 3.5rem); line-height: 1.1; margin-block: var(--ruang-2); text-wrap: balance; }
.hero__sub { font-size: 1.125rem; color: var(--teks-2); max-width: 52ch; }
.aksi { display: flex; flex-wrap: wrap; gap: var(--ruang-2); margin-top: var(--ruang-3); }
.bukti { display: flex; align-items: center; gap: var(--ruang-1); margin-top: var(--ruang-3); color: var(--teks-2); font-size: .9rem; }
.bukti .ik { color: var(--aksen); fill: currentColor; }
.hero__media { aspect-ratio: 4 / 3; border-radius: var(--radius-besar); display: grid; place-items: center; color: #fff;
  background: radial-gradient(circle at 30% 30%, color-mix(in srgb, var(--warna) 70%, #fff), var(--warna)); box-shadow: var(--bayang); }

/* ===== Bagian umum ===== */
.bagian { padding-block: var(--ruang-5); }
.bagian--rapat { padding-block: var(--ruang-3); }
.bagian--lembut { background: var(--lembut); }
.bagian h2 { font-size: clamp(1.5rem, 2vw + 1rem, 2.25rem); margin-bottom: var(--ruang-4); }
.lencana { display: inline-block; font: 700 .75rem/1 var(--font-isi); letter-spacing: .08em; text-transform: uppercase; color: var(--primer); }
.lencana--di-atas { position: absolute; top: var(--ruang-1); left: var(--ruang-1); padding: 6px 10px; border-radius: 999px; background: var(--aksen); color: var(--di-atas-aksen); }

/* ===== Fitur ===== */
.fitur { display: grid; gap: var(--ruang-3); margin: 0; padding: 0; list-style: none; }
.fitur__item { display: grid; align-content: start; gap: var(--ruang-1); padding: var(--ruang-3); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); box-shadow: var(--bayang); }
.fitur__item .ik { width: 32px; height: 32px; color: var(--primer); }
.fitur__item p { color: var(--teks-2); }

/* ===== Kartu produk ===== */
.grid-kartu { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 240px), 1fr)); gap: var(--ruang-3); margin: 0; padding: 0; list-style: none; }
.kartu { height: 100%; display: flex; flex-direction: column; gap: var(--ruang-1); padding: var(--ruang-2); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); box-shadow: var(--bayang); }
.kartu__media { position: relative; aspect-ratio: 1; border-radius: var(--radius-kecil); display: grid; place-items: center; color: #fff; background: var(--warna); margin-bottom: var(--ruang-1); }
.kartu__judul { font-size: 1.125rem; }
.kartu__sub { color: var(--teks-2); font-size: .9rem; }
.kartu__harga { font-weight: 800; font-size: 1.125rem; margin-bottom: var(--ruang-1); font-variant-numeric: tabular-nums; }
.kartu .tombol { margin-top: auto; }

/* ===== Testimoni ===== */
.grid-testimoni { display: grid; gap: var(--ruang-3); margin: 0; padding: 0; list-style: none; }
.testimoni { margin: 0; height: 100%; display: grid; align-content: space-between; gap: var(--ruang-2); padding: var(--ruang-3); background: var(--permukaan); border-radius: var(--radius); border: var(--garis-tebal) solid var(--garis); }
.testimoni blockquote { margin: 0; font-size: 1.05rem; }
.testimoni figcaption { display: grid; color: var(--teks-2); font-size: .9rem; }
.testimoni b { color: var(--teks); }

/* ===== CTA ===== */
.cta { padding-block: var(--ruang-5); background: var(--primer-2); color: #fff; }
.cta__isi { display: grid; gap: var(--ruang-3); align-items: center; }
.cta h2 { font-size: clamp(1.5rem, 2vw + 1rem, 2.25rem); color: inherit; }
.cta p { opacity: .85; }

/* ===== Footer ===== */
.kaki { padding-block: var(--ruang-5) var(--ruang-3); background: var(--permukaan); border-top: 1px solid var(--garis); }
.kaki__isi { display: grid; gap: var(--ruang-4); }
.kaki h3 { font-size: .95rem; margin-bottom: var(--ruang-1); }
.kaki ul { margin: 0; padding: 0; list-style: none; display: grid; gap: 4px; }
.kaki a:not(.logo) { color: var(--teks-2); text-decoration: none; display: inline-block; padding-block: 6px; }
.kaki a:not(.logo):hover { color: var(--primer); text-decoration: underline; }
.kaki__merek p { color: var(--teks-2); margin-top: var(--ruang-1); max-width: 36ch; }
.kaki__hak { margin-top: var(--ruang-4); padding-top: var(--ruang-2); border-top: 1px solid var(--garis); color: var(--teks-2); font-size: .85rem; }

/* ===== Form ===== */
.form-tata { display: grid; gap: var(--ruang-4); align-items: start; }
.form { display: grid; gap: var(--ruang-3); padding: var(--ruang-4) var(--ruang-3); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius-besar); box-shadow: var(--bayang); }
.form h1 { font-size: clamp(1.5rem, 2vw + 1rem, 2rem); }
.form__sub { color: var(--teks-2); margin-top: calc(var(--ruang-2) * -1); }
.field { display: grid; gap: 6px; }
.field label { font-weight: 600; }
.field__kotak { display: flex; align-items: center; gap: var(--ruang-1); min-height: 52px; padding-inline: var(--ruang-2); background: var(--permukaan); border: 1.5px solid var(--garis-input); border-radius: var(--radius-kecil); }
.field__kotak:focus-within { border-color: var(--primer); box-shadow: 0 0 0 3px color-mix(in srgb, var(--primer) 25%, transparent); }
.field__kotak .ik { color: var(--teks-2); flex: none; }
.field input { flex: 1; min-width: 0; height: 48px; border: 0; background: transparent; font: inherit; color: var(--teks); outline: none; }
.field__pesan { font-size: .85rem; color: var(--teks-2); }
.field--error .field__kotak { border-color: var(--bahaya); }
.field__pesan--error, .field--error .field__pesan { color: var(--bahaya); }
.form__status:empty { display: none; }
.form__status { padding: var(--ruang-2); border-radius: var(--radius-kecil); background: color-mix(in srgb, var(--sukses) 12%, var(--permukaan)); color: var(--sukses); font-weight: 600; }
.ringkasan { padding: var(--ruang-3); background: var(--lembut); border-radius: var(--radius); }
.ringkasan h2 { font-size: 1.125rem; margin-bottom: var(--ruang-2); }
.ringkasan ul { margin: 0; padding-left: 1.1em; display: grid; gap: var(--ruang-1); color: var(--teks-2); }

/* ===== Statistik ===== */
.grid-stat { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--ruang-2); margin: 0; }
.stat { display: grid; gap: 4px; padding: var(--ruang-2) var(--ruang-3); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); box-shadow: var(--bayang); }
.stat .ik { color: var(--primer); }
.stat dt { color: var(--teks-2); font-size: .85rem; }
.stat dd { margin: 0; font: var(--berat-judul) 1.5rem/1.2 var(--font-judul); font-variant-numeric: tabular-nums; }
.stat__ubah { font: 600 .8rem var(--font-isi); color: var(--sukses); }
.stat__ubah--turun { color: var(--bahaya); }

/* ===== Grafik ===== */
.grafik { margin: 0; padding: var(--ruang-3); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); }
.grafik figcaption { font-weight: 700; margin-bottom: var(--ruang-2); }
.grafik svg { width: 100%; height: 220px; display: block; overflow: visible; }
.grafik rect { fill: var(--primer); }
.grafik rect:hover { fill: var(--aksen); }
.grafik text { font: 12px var(--font-isi); fill: var(--teks-2); text-anchor: middle; }

/* ===== Tabel ===== */
.tabel-gulir { overflow-x: auto; border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); background: var(--permukaan); }
.tabel { width: 100%; border-collapse: collapse; min-width: 560px; font-variant-numeric: tabular-nums; }
.tabel th, .tabel td { padding: 14px var(--ruang-2); text-align: left; border-bottom: 1px solid var(--garis); }
.tabel thead th { font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; color: var(--teks-2); background: var(--lembut); }
.tabel tbody tr:hover { background: color-mix(in srgb, var(--primer) 6%, transparent); }
.status { display: inline-block; padding: 4px 10px; border-radius: 999px; font-size: .8rem; font-weight: 700; background: var(--lembut); }

/* ===== Kanban ===== */
.kanban { display: grid; grid-auto-flow: column; grid-auto-columns: min(85%, 300px); gap: var(--ruang-2); overflow-x: auto; padding: var(--ruang-3) var(--ruang-tepi); scroll-snap-type: x mandatory; }
.kolom { scroll-snap-align: start; padding: var(--ruang-2); background: var(--lembut); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); }
.kolom h2 { display: flex; justify-content: space-between; font-size: 1rem; margin-bottom: var(--ruang-2); }
.hitung { min-width: 28px; padding: 2px 8px; border-radius: 999px; background: var(--permukaan); text-align: center; font-size: .85rem; }
.kolom__isi { display: grid; gap: var(--ruang-1); margin: 0; padding: 0; list-style: none; min-height: 80px; }
.kolom[data-target] .kolom__isi { outline: 2px dashed var(--primer); outline-offset: 4px; }
.tugas { display: grid; gap: var(--ruang-1); grid-template-columns: 1fr auto; padding: var(--ruang-2); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius-kecil); box-shadow: var(--bayang); cursor: grab; }
.tugas p { grid-column: 1 / -1; font-weight: 600; }
.tugas[aria-grabbed="true"] { opacity: .5; }
.label { justify-self: start; padding: 2px 8px; border-radius: 6px; font-size: .75rem; font-weight: 700; background: var(--aksen); color: var(--di-atas-aksen); }
.label--bug { background: var(--bahaya); color: #fff; }
.avatar { width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; font-size: .75rem; font-weight: 700; background: var(--primer); color: var(--di-atas-primer); }

/* ===== Langkah ===== */
.langkah { display: grid; gap: var(--ruang-3); margin: 0; padding: 0; list-style: none; counter-reset: l; }
.langkah__item { display: grid; align-content: start; gap: var(--ruang-1); padding: var(--ruang-3); background: var(--permukaan); border-radius: var(--radius); border: var(--garis-tebal) solid var(--garis); }
.langkah__no { width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; font-weight: 800; background: var(--primer); color: var(--di-atas-primer); }
.langkah__item p { color: var(--teks-2); }

/* ===== Chat ===== */
.chat { display: grid; grid-template-rows: 1fr auto; min-height: 70vh; max-width: 860px; margin-inline: auto; padding: var(--ruang-3) var(--ruang-tepi); gap: var(--ruang-2); }
.chat__log { display: grid; align-content: start; gap: var(--ruang-2); margin: 0; padding: 0; list-style: none; }
.pesan { display: flex; }
.pesan--saya { justify-content: flex-end; }
.pesan__isi { max-width: min(80ch, 85%); padding: var(--ruang-2); border-radius: var(--radius); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); }
.pesan--saya .pesan__isi { background: var(--primer); color: var(--di-atas-primer); border-color: transparent; }
.pesan__sumber { margin-top: var(--ruang-1); font-size: .8rem; color: var(--teks-2); }
.chat__form { position: sticky; bottom: var(--ruang-2); display: flex; gap: var(--ruang-1); padding: var(--ruang-1); background: var(--permukaan); border: var(--garis-tebal) solid var(--garis); border-radius: var(--radius); box-shadow: var(--bayang); }
.chat__form textarea { flex: 1; min-height: 48px; resize: none; border: 0; padding: 12px; font: inherit; background: transparent; color: var(--teks); }

/* ===== Tata letak aplikasi dengan sidebar ===== */
.app { min-height: 100vh; }
.sidebar { display: none; }
.tabbar { position: sticky; bottom: 0; z-index: 5; display: flex; justify-content: space-around; padding-bottom: env(safe-area-inset-bottom, 0px); background: var(--permukaan); border-top: 1px solid var(--garis); }
.tabbar a { display: grid; justify-items: center; gap: 2px; min-width: 64px; padding: 8px 4px; font-size: .75rem; color: var(--teks-2); text-decoration: none; }
.tabbar a[aria-current="page"] { color: var(--primer); font-weight: 700; }

/* =========================================================================
   TABLET dan DESKTOP (≥ 768 px): susunan mengikuti frame web di kit desain
   ========================================================================= */
@media (min-width: 768px) {
  .navbar__toggle { display: none; }
  .navbar__menu, .navbar__menu[data-terbuka] { display: flex; position: static; align-items: center; gap: var(--ruang-4); padding: 0; background: none; border: 0; box-shadow: none; }
  .navbar__menu ul { display: flex; gap: var(--ruang-3); }
  .navbar__menu a:not(.tombol) { padding: 8px 0; }
  .hero__isi { grid-template-columns: 1.1fr 1fr; gap: var(--ruang-5); }
  .fitur { grid-template-columns: repeat(3, 1fr); }
  .grid-testimoni { grid-template-columns: repeat(3, 1fr); }
  .cta__isi { grid-template-columns: 1fr auto; }
  .kaki__isi { grid-template-columns: 2fr repeat(3, 1fr); }
  .form-tata { grid-template-columns: minmax(0, 2fr) minmax(260px, 1fr); }
  .ringkasan { position: sticky; top: 88px; }
  .grid-stat { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .langkah { grid-template-columns: repeat(3, 1fr); }
  .kanban { grid-auto-flow: initial; grid-template-columns: repeat(4, minmax(0, 1fr)); overflow: visible; padding-inline: var(--ruang-tepi); }
  .app { display: grid; grid-template-columns: 248px minmax(0, 1fr); }
  .sidebar { display: flex; flex-direction: column; gap: var(--ruang-1); position: sticky; top: 0; height: 100vh; padding: var(--ruang-3) var(--ruang-2); background: var(--permukaan); border-right: var(--garis-tebal) solid var(--garis); }
  .sidebar a:not(.logo) { display: flex; align-items: center; gap: var(--ruang-2); min-height: 44px; padding: 0 var(--ruang-2); border-radius: var(--radius-kecil); color: var(--teks-2); text-decoration: none; font-weight: 500; }
  .sidebar a[aria-current="page"] { background: var(--lembut); color: var(--primer); font-weight: 700; }
  .sidebar .logo { margin-bottom: var(--ruang-3); padding-inline: var(--ruang-2); }
  .tabbar { display: none; }
}
@media (min-width: 1200px) {
  .hero { padding-block: 96px; }
  .bagian { padding-block: 80px; }
}
'''


def css_token(T, spec):
    t = T.t
    keras = T.tinta
    bay = {'blok': f'4px 4px 0 {t["teks"] if keras else "#0002"}', 'lembut': '0 1px 2px #0000000f, 0 8px 24px #0000000d',
           'clay': 'inset -4px -4px 10px #0000000f, inset 4px 4px 10px #ffffffb3, 0 10px 24px #00000014'}.get(T.bayang, 'none')
    on = T.di_atas
    fj = T.fj if T.fj else FONT
    fb = T.fb if T.fb else FONT
    latar = t['latar']
    if T.kaca and t.get('latar_gradasi'):
        g = t['latar_gradasi']
        latar_img = f'linear-gradient(160deg, {g[0]}, {g[-1]})'
    else:
        latar_img = 'none'
    return f'''/* Token desain "{spec['token']['nama']}" · gaya {spec['gaya']} — sama dengan tokens.json di kit Figma.
   Primitive dan semantic dijadikan satu lapis agar ringkas; komponen hanya memakai var(--…). */
:root {{
  --primer: {t['primer']};
  --primer-2: {t['primer2']};
  --aksen: {t['aksen']};
  --latar: {latar};
  --latar-gambar: {latar_img};
  --permukaan: {t['permukaan']};
  --lembut: {t['lembut']};
  --teks: {t['teks']};
  --teks-2: {t['teks2']};
  --garis: {t['garis']};
  --garis-input: {t['garis'] if keras else t['teks2']};
  --sukses: {t['sukses']};
  --bahaya: {t['bahaya']};
  --di-atas-primer: {on(t['primer'])};
  --di-atas-aksen: {on(t['aksen'])};

  --font-judul: "{fj}", system-ui, sans-serif;
  --font-isi: "{fb}", system-ui, sans-serif;
  --berat-judul: {T.wj};

  --radius: {T.r}px;
  --radius-kecil: {max(2, round(T.r * .6))}px;
  --radius-besar: {round(T.r * 1.4)}px;
  --garis-tebal: {2 if keras else 1}px;
  --bayang: {bay};

  --ruang-1: 8px; --ruang-2: 16px; --ruang-3: 24px; --ruang-4: 32px; --ruang-5: 56px;
  --ruang-tepi: max(16px, env(safe-area-inset-left, 0px));
  --lebar-isi: 1200px;
  --durasi: 200ms; --kurva: cubic-bezier(.2, 0, 0, 1);
}}
'''


CSS_DASAR = '''/* Reset modern + tipografi + utilitas. */
*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 80px; }
body { min-height: 100vh; font: 400 1rem/1.6 var(--font-isi); color: var(--teks); background: var(--latar) var(--latar-gambar) fixed; -webkit-font-smoothing: antialiased; }
h1, h2, h3 { font-family: var(--font-judul); font-weight: var(--berat-judul); line-height: 1.2; text-wrap: balance; }
img, svg { display: block; max-width: 100%; }
.ik { width: 24px; height: 24px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex: none; }
.ik--besar { width: 64px; height: 64px; stroke-width: 1.5; }
button, input, textarea, select { font: inherit; }
a { color: var(--primer); }
.wadah { width: 100%; max-width: calc(var(--lebar-isi) + 2 * var(--ruang-tepi)); margin-inline: auto; padding-inline: var(--ruang-tepi); }
.sr { position: absolute !important; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.lewati { position: absolute; left: var(--ruang-2); top: -100px; z-index: 100; padding: 12px 16px; background: var(--teks); color: var(--latar); border-radius: var(--radius-kecil); }
.lewati:focus { top: var(--ruang-2); }

/* Tombol: target sentuh minimal 48 px (WCAG 2.5.8 + Material) */
.tombol { display: inline-flex; align-items: center; justify-content: center; gap: var(--ruang-1); min-height: 48px; padding: 0 var(--ruang-3);
  border: var(--garis-tebal) solid transparent; border-radius: var(--radius-kecil); font-weight: 700; text-decoration: none; cursor: pointer;
  transition: transform var(--durasi) var(--kurva), filter var(--durasi) var(--kurva), background-color var(--durasi); }
.tombol--primer { background: var(--primer); color: var(--di-atas-primer); }
.tombol--aksen { background: var(--aksen); color: var(--di-atas-aksen); }
.tombol--garis { background: transparent; color: var(--primer); border-color: var(--primer); }
.tombol--penuh { width: 100%; }
.tombol:hover { filter: brightness(1.08); }
.tombol:active { transform: scale(.97); }
.tombol:disabled { opacity: .5; cursor: not-allowed; }

:where(a, button, input, textarea, select, [tabindex]):focus-visible { outline: 3px solid var(--aksen); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
'''

JS_MAIN = '''// Interaksi halaman. Tanpa framework: setiap fitur hanya aktif jika elemennya ada di halaman.
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];

// 1. Menu navigasi di HP (tombol ☰) — dapat dibuka/tutup dengan keyboard, Esc menutup.
const toggle = $('.navbar__toggle');
const menu = $('#menu-utama');
if (toggle && menu) {
  const atur = (buka) => {
    toggle.setAttribute('aria-expanded', String(buka));
    menu.toggleAttribute('data-terbuka', buka);
    $('.sr', toggle).textContent = buka ? 'Tutup menu' : 'Buka menu';
  };
  toggle.addEventListener('click', () => atur(toggle.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') { atur(false); toggle.focus(); } });
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) atur(false); });
}

// 2. Validasi form: pesan muncul di bawah field, fokus ke field pertama yang salah.
const ATURAN = {
  email: (v) => /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v) || 'Format email belum lengkap, contoh: nama@mail.com',
  tel: (v) => /^(\\+62|0)8\\d{7,12}$/.test(v.replace(/[\\s-]/g, '')) || 'Nomor HP diawali 08 atau +628, 10-14 digit',
  text: (v) => v.trim().length > 0 || 'Wajib diisi',
};
for (const form of $$('[data-validasi]')) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    let pertamaSalah = null;
    for (const input of $$('input[required]', form)) {
      const hasil = (ATURAN[input.type] || ATURAN.text)(input.value);
      const salah = hasil !== true;
      const field = input.closest('.field');
      const pesan = $('.field__pesan', field);
      field.classList.toggle('field--error', salah);
      input.toggleAttribute('aria-invalid', salah);
      if (salah) { pesan.hidden = false; pesan.textContent = hasil; pertamaSalah ??= input; }
    }
    const status = $('.form__status', form);
    if (pertamaSalah) { pertamaSalah.focus(); status.textContent = ''; return; }
    status.textContent = 'Berhasil disimpan.';
  });
}

// 3. Tombol "Tambah ke keranjang": umpan balik untuk pembaca layar dan visual.
for (const btn of $$('[data-tambah]')) {
  btn.addEventListener('click', () => {
    btn.textContent = 'Ditambahkan ✓';
    btn.disabled = true;
    setTimeout(() => { btn.textContent = 'Tambah ke keranjang'; btn.disabled = false; }, 1500);
  });
}

// 4. Kanban: seret-lepas DAN alternatif keyboard (WCAG 2.2 · 2.5.7 Dragging Movements).
const kolom = $$('.kolom');
if (kolom.length) {
  const status = $('#kanban-status');
  const hitung = () => kolom.forEach((k) => { $('.hitung', k).textContent = $$('.tugas', k).length; });
  const pindah = (tugas, ke) => {
    $('.kolom__isi', ke).append(tugas);
    hitung();
    status.textContent = `Dipindah ke ${$('h2', ke).firstChild.textContent.trim()}`;
  };
  for (const t of $$('.tugas')) {
    t.addEventListener('dragstart', (e) => { e.dataTransfer.setData('text/plain', t.dataset.id); t.setAttribute('aria-grabbed', 'true'); });
    t.addEventListener('dragend', () => t.removeAttribute('aria-grabbed'));
    t.addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      e.preventDefault();
      const i = kolom.indexOf(t.closest('.kolom')) + (e.key === 'ArrowRight' ? 1 : -1);
      if (kolom[i]) { pindah(t, kolom[i]); t.focus(); }
    });
  }
  for (const k of kolom) {
    k.addEventListener('dragover', (e) => { e.preventDefault(); k.setAttribute('data-target', ''); });
    k.addEventListener('dragleave', () => k.removeAttribute('data-target'));
    k.addEventListener('drop', (e) => {
      e.preventDefault(); k.removeAttribute('data-target');
      const t = $(`.tugas[data-id="${e.dataTransfer.getData('text/plain')}"]`);
      if (t) pindah(t, k);
    });
  }
}

// 5. Chat: kirim dengan Enter, Shift+Enter untuk baris baru; jawaban dari API ditampilkan bertahap.
const chat = $('[data-chat]');
if (chat) {
  const log = $('.chat__log');
  const area = $('textarea', chat);
  const tambah = (siapa, teks) => {
    const li = document.createElement('li');
    li.className = `pesan pesan--${siapa}`;
    li.innerHTML = '<div class="pesan__isi"><p></p></div>';
    $('p', li).textContent = teks; // textContent: aman dari XSS
    log.append(li);
    li.scrollIntoView({ block: 'end', behavior: 'smooth' });
  };
  area.addEventListener('keydown', (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); chat.requestSubmit(); } });
  chat.addEventListener('submit', async (e) => {
    e.preventDefault();
    const teks = area.value.trim();
    if (!teks) return;
    tambah('saya', teks);
    area.value = '';
    // Ganti dengan panggilan API backend: const r = await fetch('/api/tanya', { method: 'POST', body: JSON.stringify({ teks }) });
    tambah('ai', 'Sedang mencari di materi kelasmu…');
  });
}
'''


def _sidebar(spec, aktif_layar):
    sb = spec.get('sidebar')
    if not sb:
        return '', ''
    items, aktif = sb
    side = (f'<aside class="sidebar" aria-label="Navigasi aplikasi">\n    <a class="logo" href="./">{ik("sparkle")}<span>{e(spec["token"]["nama"])}</span></a>\n'
            + ''.join(f'    <a href="#"{" aria-current=\"page\"" if i == aktif else ""}>{ik(ic)}<span>{e(n)}</span></a>\n' for i, (ic, n) in enumerate(items)) + '  </aside>')
    tab = ('<nav class="tabbar" aria-label="Navigasi aplikasi">' + ''.join(f'<a href="#"{" aria-current=\"page\"" if i == aktif else ""}>{ik(ic)}<span>{e(n)}</span></a>' for i, (ic, n) in enumerate(items[:4])) + '</nav>')
    return side, tab


def halaman_web(spec, layar):
    nama, bloks = layar[0], layar[1]
    blok_html = [WEB[j](d, spec) for j, d in bloks]
    kepala = [b for (j, _), b in zip(bloks, blok_html) if j in ('navbar',)]
    kaki = [b for (j, _), b in zip(bloks, blok_html) if j == 'footer']
    isi = [b for (j, _), b in zip(bloks, blok_html) if j not in ('navbar', 'footer') and b]
    ind = lambda s, n: '\n'.join((' ' * n + x) if x else x for x in s.split('\n'))
    side, tab = _sidebar(spec, nama)
    main = '<main id="isi">\n' + '\n'.join(ind(b, 2) for b in isi) + '\n</main>'
    if side:
        badan = f'<div class="app">\n  {side}\n  <div class="app__isi">\n{ind(main, 4)}\n    {tab}\n  </div>\n</div>'
    else:
        badan = '\n'.join(kepala + [main] + kaki)
    return nama, badan


def _font_link(T):
    fams = sorted({T.fj or FONT, T.fb or FONT})
    q = '&'.join('family=' + f.replace(' ', '+') + ':wght@400;500;600;700;800' if f not in ('Space Mono', 'Dela Gothic One') else 'family=' + f.replace(' ', '+') + (':wght@400;700' if f == 'Space Mono' else '') for f in fams)
    return f'https://fonts.googleapis.com/css2?{q}&display=swap'


def web_final(spec):
    T = palet(spec)
    nama_proyek = slug(spec['token']['nama'])
    halaman = []
    for i, lay in enumerate(spec['layar']):
        nm, badan = halaman_web(spec, lay)
        fn = 'index.html' if i == 0 else slug(nm) + '.html'
        halaman.append((fn, nm, badan))
    tok = css_token(T, spec)
    font = _font_link(T)
    deskripsi = spec['brief'].split('.')[0] + '.'

    def dok(nm, badan, css_inline=None, js_inline=None):
        css = f'<style>\n{css_inline}</style>' if css_inline else '<link rel="stylesheet" href="css/tokens.css">\n  <link rel="stylesheet" href="css/base.css">\n  <link rel="stylesheet" href="css/komponen.css">'
        js = f'<script>\n{js_inline}</script>' if js_inline else '<script type="module" src="js/main.js"></script>'
        return (f'<!doctype html>\n<html lang="id">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                f'  <title>{e(nm)} · {e(spec["token"]["nama"])}</title>\n  <meta name="description" content="{e(deskripsi)}">\n  <meta name="theme-color" content="{T.t["primer"]}">\n'
                f'  <meta property="og:title" content="{e(spec["token"]["nama"])}">\n  <meta property="og:description" content="{e(deskripsi)}">\n'
                f'  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link rel="stylesheet" href="{font}">\n  {css}\n  {js if not js_inline else ""}\n</head>\n<body>\n'
                f'  <a class="lewati" href="#isi">Lewati ke konten utama</a>\n' + '\n'.join('  ' + x if x else x for x in badan.split('\n')) + (f'\n  {js}' if js_inline else '') + '\n</body>\n</html>\n')

    files = [(fn, 'html', dok(nm, b)) for fn, nm, b in halaman]
    files += [('css/tokens.css', 'css', tok), ('css/base.css', 'css', CSS_DASAR), ('css/komponen.css', 'css', CSS_KOMPONEN), ('js/main.js', 'js', JS_MAIN)]
    files += [('tests/tampilan.spec.js', 'js', TEST_WEB.replace('@@HAL@@', json.dumps([f for f, _, _ in halaman]))),
              ('package.json', 'json', json.dumps({'name': nama_proyek, 'private': True, 'type': 'module', 'scripts': {
                  'dev': 'vite', 'build': 'vite build', 'preview': 'vite preview', 'lint': 'html-validate "*.html" && stylelint "css/**/*.css" && eslint js',
                  'test': 'playwright test', 'test:update': 'playwright test --update-snapshots'},
                  'devDependencies': {'vite': '^6.0.0', '@playwright/test': '^1.49.0', '@axe-core/playwright': '^4.10.0', 'html-validate': '^9.0.0',
                                      'stylelint': '^16.10.0', 'stylelint-config-standard': '^36.0.0', 'eslint': '^9.15.0', '@eslint/js': '^9.15.0'}}, indent=2) + '\n'),
              ('.stylelintrc.json', 'json', '{ "extends": "stylelint-config-standard", "rules": { "selector-class-pattern": null, "custom-property-pattern": null } }\n'),
              ('eslint.config.js', 'js', "import js from '@eslint/js';\nexport default [js.configs.recommended, { languageOptions: { globals: { document: 'readonly', window: 'readonly', setTimeout: 'readonly' } } }];\n"),
              ('playwright.config.js', 'js', PW_CONFIG),
              ('.github/workflows/ci.yml', 'yaml', CI_WEB),
              ('README.md', 'markdown', README_WEB.format(nama=spec['token']['nama'], judul=spec['judul'], gaya=spec['gaya'], hal=', '.join(f'`{f}` ({n})' for f, n, _ in halaman)))]
    tree = TREE_WEB.format(nama=nama_proyek, hal=''.join(f'├── {f:<24}# {n}\n' for f, n, _ in halaman))
    prev = dok(halaman[0][1], halaman[0][2], tok + CSS_DASAR + CSS_KOMPONEN, JS_MAIN).replace(f'  <link rel="stylesheet" href="{font}">\n', f'  <link rel="stylesheet" href="{font}">\n')
    return dict(files=files, tree=tree, prev=prev, vp=1280,
                run='npm install\nnpx playwright install chromium\nnpm run dev          # buka http://localhost:5173\nnpm run lint         # validasi HTML, CSS, JS\nnpm test             # uji tampilan 360/768/1440 + aksesibilitas axe',
                n=f'Kode final ini dibangkitkan dari spesifikasi yang sama dengan kit Figma <b>{e(spec["judul"])}</b>, jadi isi, urutan blok, dan tokennya cocok dengan desain. Tekan tombol lebar layar di pratinjau untuk membandingkan dengan frame desain.',
                cek=CEK_WEB)


TREE_WEB = '''{nama}/
{hal}├── css/
│   ├── tokens.css          # token dari tokens.json (warna, font, radius, jarak)
│   ├── base.css            # reset, tipografi, tombol, fokus, reduced motion
│   └── komponen.css        # setiap blok desain; mobile-first + @media 768/1200
├── js/
│   └── main.js             # menu HP, validasi form, kanban keyboard, chat
├── tests/
│   └── tampilan.spec.js    # screenshot 360/768/1440 + uji aksesibilitas axe
├── .github/workflows/ci.yml
├── eslint.config.js · .stylelintrc.json · playwright.config.js
├── package.json
└── README.md'''

TEST_WEB = '''import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const HALAMAN = @@HAL@@;
const LEBAR = [360, 768, 1440];

for (const hal of HALAMAN) {
  for (const lebar of LEBAR) {
    test(`${hal} @ ${lebar}px sesuai desain`, async ({ page }) => {
      await page.setViewportSize({ width: lebar, height: 900 });
      await page.goto('/' + hal);
      // Tidak boleh ada scroll horizontal di lebar mana pun.
      const lebarDok = await page.evaluate(() => document.documentElement.scrollWidth);
      expect(lebarDok).toBeLessThanOrEqual(lebar);
      // Bandingkan dengan tangkapan acuan (buat sekali dengan npm run test:update setelah desainer setuju).
      await expect(page).toHaveScreenshot(`${hal}-${lebar}.png`, { fullPage: true, maxDiffPixelRatio: 0.01 });
    });
  }

  test(`${hal} lolos aksesibilitas WCAG 2.2 AA`, async ({ page }) => {
    await page.goto('/' + hal);
    const hasil = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag22aa']).analyze();
    expect(hasil.violations).toEqual([]);
  });
}

test('menu HP bisa dibuka dengan keyboard', async ({ page }) => {
  await page.setViewportSize({ width: 360, height: 800 });
  await page.goto('/');
  const tombol = page.locator('.navbar__toggle');
  test.skip(!(await tombol.count()), 'halaman ini tidak memakai navbar');
  await tombol.focus();
  await page.keyboard.press('Enter');
  await expect(tombol).toHaveAttribute('aria-expanded', 'true');
  await page.keyboard.press('Escape');
  await expect(tombol).toHaveAttribute('aria-expanded', 'false');
});
'''

PW_CONFIG = '''import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: 'tests',
  use: { baseURL: 'http://localhost:4173' },
  webServer: { command: 'npm run build && npm run preview -- --port 4173', port: 4173, reuseExistingServer: !process.env.CI },
});
'''

CI_WEB = '''name: CI
on: [push, pull_request]
jobs:
  cek:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run lint
      - run: npx playwright install --with-deps chromium
      - run: npm test
'''

README_WEB = '''# {nama} · {judul}

Hasil slicing dari kit Figma Ruang Kode (gaya **{gaya}**). Halaman: {hal}.

## Menjalankan
```bash
npm install
npm run dev      # http://localhost:5173
npm run lint     # html-validate + stylelint + eslint
npm test         # Playwright: tampilan 360/768/1440 + axe WCAG 2.2 AA
```

## Keputusan teknis
- **Token** di `css/tokens.css` sama dengan `tokens.json` di kit; komponen hanya memakai `var(--…)`.
- **Mobile-first**: gaya dasar untuk 360 px, `@media (min-width: 768px)` untuk susunan web, `1200px` untuk ukuran lebar.
- **Aksesibilitas**: landmark lengkap, satu `h1`, tautan lewati konten, fokus terlihat, target 48 px, alternatif keyboard untuk seret-lepas.
- **Tanpa framework** agar ringan; bisa dipindah ke React/Vue per blok (setiap `<section>` = satu komponen).

## Perbedaan yang disengaja dari desain
- State hover/fokus/aktif ditambahkan karena tidak digambar di frame statis.
- Foto produk memakai blok warna; ganti dengan `<img>` WebP/AVIF `loading="lazy"` + `width`/`height`.
'''

CEK_WEB = [
    ['Kesetiaan desain', 'Urutan blok, teks, warna, radius, dan jarak sama dengan frame web dan versi HP-nya'],
    ['Token', 'Tidak ada kode warna atau angka ajaib di komponen; semua lewat var(--…) dari tokens.css'],
    ['HTML semantik', 'header/nav/main/section/footer, satu h1, heading berurutan, list untuk daftar, table + th scope untuk tabel'],
    ['Responsif', 'Mobile-first; tidak ada scroll horizontal dari 320 sampai 1920 px; isi maks 1200 di tengah'],
    ['Aksesibilitas', 'Label untuk setiap input, aria-invalid + pesan error terhubung, fokus terlihat, target 48 px, lolos axe'],
    ['Interaksi', 'Menu HP bisa dibuka keyboard dan ditutup Esc; seret-lepas punya alternatif tombol panah'],
    ['Keamanan', 'Teks dari pengguna dimasukkan dengan textContent, bukan innerHTML; tautan luar rel="noopener"'],
    ['Performa', 'CSS dan JS terpisah dan di-cache; font display=swap; gambar asli diberi ukuran dan lazy'],
    ['Kualitas kode', 'Lolos html-validate, stylelint, eslint; penamaan kelas konsisten (blok__elemen--varian)'],
    ['Pengujian', 'Uji tampilan 3 lebar + axe berjalan di CI pada setiap push'],
]


# ====================================================================== FLUTTER
IKON_M = {'plus': 'add', 'minus': 'remove', 'chart': 'bar_chart', 'settings': 'settings_outlined', 'cup': 'local_cafe_outlined', 'wallet': 'account_balance_wallet_outlined',
          'bike': 'two_wheeler', 'home': 'home_outlined', 'list': 'receipt_long_outlined', 'user': 'person_outline', 'search': 'search', 'heart': 'favorite_border',
          'bag': 'shopping_bag_outlined', 'sparkle': 'auto_awesome', 'star': 'star_outline', 'pill': 'medication_outlined', 'calendar': 'calendar_month_outlined',
          'edit': 'edit_outlined', 'close': 'close', 'back': 'arrow_back', 'bell': 'notifications_none', 'refresh': 'currency_exchange', 'receipt': 'receipt_long_outlined',
          'pin': 'place_outlined', 'grid': 'grid_view', 'cart': 'shopping_cart_outlined', 'doc': 'description_outlined', 'chat': 'chat_bubble_outline',
          'alert': 'warning_amber', 'info': 'info_outline', 'globe': 'public', 'mail': 'mail_outline', 'phone': 'phone_outlined', 'send': 'send', 'filter': 'tune',
          'clock': 'schedule', 'check': 'check', 'more': 'more_vert', 'share': 'share_outlined', 'x': 'close', 'menu': 'menu'}


def mi(n):
    return 'Icons.' + IKON_M.get(n, 'circle_outlined')


def ds(t):
    t = str(t).replace('\\', '\\\\').replace("'", "\\'").replace('$', '\\$')
    return f"'{t}'"


def dc(h):
    return f'Color(0xFF{h.lstrip("#").upper()[:6]})'


def kelas(nama):
    return 'Layar' + ''.join(w.capitalize() for w in re.sub(r'[^A-Za-z0-9 ]', ' ', nama).split())


def fb_appbar(d):
    kiri = d.get('kiri', 'back')
    kanan = d.get('kanan') or ()
    acts = ', '.join(f"IconButton(onPressed: () {{}}, tooltip: {ds(k)}, icon: const Icon({mi(k)}))" for k in kanan)
    return ('appbar', f"AppBar(\n        leading: IconButton(onPressed: () => Navigator.maybePop(context), tooltip: {ds('Tutup' if kiri == 'close' else 'Kembali')}, icon: const Icon({mi(kiri)})),\n"
                      f"        title: const Text({ds(d['judul_teks'])}),\n" + (f"        actions: [{acts}],\n" if acts else '') + "      )")


def fb(jenis, d):
    """Satu blok desain -> satu ekspresi widget Dart (const)."""
    if jenis == 'sapaan':
        return f"Sapaan(nama: {ds(d['nama'])}, sub: {ds(d['sub'])})"
    if jenis == 'saldo':
        aksi = ', '.join(f"AksiCepat({mi(i)}, {ds(t)})" for i, t in d['aksi'])
        return f"KartuSaldo(label: {ds(d['label'])}, nilai: {ds(d['nilai'])}, sub: {ds(d['sub'])}, aksi: [{aksi}])"
    if jenis == 'bagian':
        return f"JudulBagian({ds(d['teks'])}" + (f", tautan: {ds(d['link'])}" if d.get('link') else '') + ')'
    if jenis == 'list':
        it = ',\n              '.join(f"ItemDaftar(judul: {ds(a)}, sub: {ds(b)}, kanan: {ds(c)}, warna: {dc(w)}, ikon: {mi(i)})" for a, b, c, w, i in d['items'])
        return f"DaftarItem(items: [\n              {it},\n            ])"
    if jenis == 'judul':
        return f"JudulLayar({ds(d['teks'])}" + (f", sub: {ds(d['sub'])}" if d.get('sub') else '') + (', besar: true' if d.get('besar') else '') + ')'
    if jenis == 'cari':
        return f"KotakCari(petunjuk: {ds(d['placeholder'])}" + (', filter: false' if d.get('filter') is False else '') + ')'
    if jenis == 'chips':
        return f"BarisChip(items: [{', '.join(ds(x) for x in d['items'])}])"
    if jenis == 'banner':
        return f"BannerInfo(judul: {ds(d['jd'])}, sub: {ds(d['sub'])}, label: {ds(d.get('label', ''))}, ikon: {mi(d.get('ikon', 'sparkle'))})"
    if jenis == 'grid':
        it = ',\n              '.join(f"Produk(nama: {ds(a)}, sub: {ds(b)}, harga: {ds(c)}, warna: {dc(w)}, ikon: {mi(i)}" + (f", lencana: {ds(bg)}" if bg else '') + ')' for a, b, c, w, i, bg in d['items'])
        return f"GridProduk(items: [\n              {it},\n            ])"
    if jenis == 'form':
        it = []
        for lb, nilai, ph, st, pesan, ikon in d['fields']:
            x = f"Isian(label: {ds(lb)}, ikon: {mi(ikon or 'edit')}"
            if nilai:
                x += f", nilai: {ds(nilai)}"
            if ph:
                x += f", petunjuk: {ds(ph)}"
            if st == 'error' and pesan:
                x += f", galat: {ds(pesan)}"
            elif pesan:
                x += f", bantuan: {ds(pesan)}"
            it.append(x + ')')
        return "FormIsian(isian: [\n              " + ',\n              '.join(it) + ",\n            ])"
    if jenis == 'langkah':
        return f"IndikatorLangkah(langkah: [{', '.join(ds(x) for x in d['langkah'])}], aktif: {d.get('aktif', 0)})"
    if jenis == 'peta':
        return f"PetaRute(tinggi: {d.get('h', 300)}, label: {ds(d.get('label', 'Peta'))})"
    if jenis == 'chat':
        it = ', '.join(f"Pesan(dariSaya: {'true' if a == 'saya' else 'false'}, teks: {ds(b)})" for a, b in d['pesan'])
        return f"Percakapan(pesan: [{it}])"
    if jenis == 'masukan_chat':
        return None
    if jenis == 'ringkas':
        it = ', '.join(f"({ds(a)}, {ds(b)})" for a, b in d['baris'])
        tot = f", total: ({ds(d['total'][0])}, {ds(d['total'][1])})" if d.get('total') else ''
        return f"KartuRingkas(baris: [{it}]{tot})"
    if jenis == 'grafik':
        return f"GrafikBatang(judul: {ds(d['jd'])}, data: [{', '.join(str(float(v)) for v in d['data'])}], label: [{', '.join(ds(x) for x in d['label'])}])"
    if jenis == 'slot':
        return f"PilihSlot(judul: {ds(d['jd'])}, slot: [{', '.join(ds(x) for x in d['slot'])}], awal: {d.get('aktif', 0)})"
    if jenis == 'segmen':
        return f"PilihSegmen(opsi: [{', '.join(ds(x) for x in d['opsi'])}])"
    if jenis == 'kosong':
        return f"KeadaanKosong(ikon: {mi(d.get('ikon', 'search'))}, judul: {ds(d['jd'])}, sub: {ds(d['sub'])}, aksi: {ds(d['cta'])})"
    if jenis == 'spasi':
        return f"SizedBox(height: {d.get('h', 16)})"
    raise KeyError(jenis)


def layar_dart(spec, lay, idx):
    nama, bloks = lay[0], lay[1]
    opsi = lay[2] if len(lay) > 2 else {}
    kls = kelas(nama)
    appbar = None
    anak = []
    chat_input = False
    for j, d in bloks:
        if j == 'appbar':
            appbar = fb_appbar(d)[1]
            continue
        if j == 'masukan_chat':
            chat_input = True
            continue
        anak.append(fb(j, d))
    bawah = ''
    if opsi.get('nav'):
        it = ', '.join(f"({mi(i)}, {ds(t)})" for i, t in opsi['nav'])
        bawah = f"      bottomNavigationBar: const NavBawah(item: [{it}], awal: {opsi.get('aktif', 0)}),\n"
    elif opsi.get('bawah'):
        b = opsi['bawah']
        x = f"label: {ds(b['label'])}"
        if b.get('label2'):
            x += f", label2: {ds(b['label2'])}"
        if b.get('info'):
            x += f", info: ({ds(b['info'][0])}, {ds(b['info'][1])})"
        bawah = f"      bottomNavigationBar: const AksiBawah({x}),\n"
    elif chat_input:
        bawah = "      bottomNavigationBar: const MasukanChat(),\n"
    rute = "/" if idx == 0 else "/" + slug(nama)
    isi = ',\n            SizedBox(height: 16),\n'.join('            ' + a for a in anak)
    kode = (f"import 'package:flutter/material.dart';\n\nimport '../widgets/blok.dart';\n\n/// Layar \"{nama}\" — sesuai frame \"{nama}\" di kit Figma {spec['token']['nama']}.\n"
            f"class {kls} extends StatelessWidget {{\n  const {kls}({{super.key}});\n\n  static const rute = '{rute}';\n\n  @override\n  Widget build(BuildContext context) {{\n    return Scaffold(\n"
            + (f"      appBar: {appbar},\n" if appbar else '')
            + "      body: SafeArea(\n        child: ListView(\n          padding: const EdgeInsets.fromLTRB(16, 8, 16, 24),\n          children: const [\n"
            + isi + ",\n          ],\n        ),\n      ),\n" + bawah + "    );\n  }\n}\n")
    return slug(nama).replace('-', '_'), kls, rute, kode


BLOK_DART = r"""import 'package:flutter/material.dart';

/// Pustaka widget yang dipakai semua layar. Setiap widget = satu komponen di halaman Komponen kit Figma.
/// Warna, radius, dan huruf diambil dari Theme (lib/tema.dart), bukan ditulis langsung di sini.

// ---------------------------------------------------------------- data
class ItemDaftar {
  const ItemDaftar({required this.judul, required this.sub, required this.kanan, required this.warna, required this.ikon});
  final String judul, sub, kanan;
  final Color warna;
  final IconData ikon;
}

class Produk {
  const Produk({required this.nama, required this.sub, required this.harga, required this.warna, required this.ikon, this.lencana});
  final String nama, sub, harga;
  final Color warna;
  final IconData ikon;
  final String? lencana;
}

class AksiCepat {
  const AksiCepat(this.ikon, this.label);
  final IconData ikon;
  final String label;
}

class Isian {
  const Isian({required this.label, required this.ikon, this.nilai, this.petunjuk, this.galat, this.bantuan});
  final String label;
  final IconData ikon;
  final String? nilai, petunjuk, galat, bantuan;
}

class Pesan {
  const Pesan({required this.dariSaya, required this.teks});
  final bool dariSaya;
  final String teks;
}

// ---------------------------------------------------------------- header
class Sapaan extends StatelessWidget {
  const Sapaan({super.key, required this.nama, required this.sub});
  final String nama, sub;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    final awal = nama.replaceAll(RegExp(r'^(Halo|Hai|Mau ke mana),?\s*'), '').trim();
    return Row(children: [
      CircleAvatar(radius: 22, child: Text(awal.isEmpty ? '?' : awal[0])),
      const SizedBox(width: 12),
      Expanded(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(sub, style: t.bodySmall),
          Text(nama, style: t.titleLarge, maxLines: 1, overflow: TextOverflow.ellipsis),
        ]),
      ),
      IconButton.outlined(onPressed: () {}, tooltip: 'Notifikasi', icon: const Icon(Icons.notifications_none)),
    ]);
  }
}

class JudulLayar extends StatelessWidget {
  const JudulLayar(this.teks, {super.key, this.sub, this.besar = false});
  final String teks;
  final String? sub;
  final bool besar;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(teks, style: besar ? t.headlineMedium : t.titleLarge),
      if (sub != null) ...[const SizedBox(height: 4), Text(sub!, style: t.bodyMedium?.copyWith(color: Theme.of(context).colorScheme.onSurfaceVariant))],
    ]);
  }
}

class JudulBagian extends StatelessWidget {
  const JudulBagian(this.teks, {super.key, this.tautan});
  final String teks;
  final String? tautan;

  @override
  Widget build(BuildContext context) {
    return Row(children: [
      Expanded(child: Text(teks, style: Theme.of(context).textTheme.titleMedium)),
      if (tautan != null) TextButton(onPressed: () {}, child: Text(tautan!)),
    ]);
  }
}

// ---------------------------------------------------------------- kartu
class KartuSaldo extends StatelessWidget {
  const KartuSaldo({super.key, required this.label, required this.nilai, required this.sub, required this.aksi});
  final String label, nilai, sub;
  final List<AksiCepat> aksi;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    final t = Theme.of(context).textTheme;
    return Card(
      color: c.primary,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(label, style: t.bodyMedium?.copyWith(color: c.onPrimary.withValues(alpha: .85))),
          const SizedBox(height: 4),
          Text(nilai, style: t.headlineMedium?.copyWith(color: c.onPrimary, fontFeatures: const [FontFeature.tabularFigures()])),
          const SizedBox(height: 4),
          Text(sub, style: t.bodySmall?.copyWith(color: c.onPrimary.withValues(alpha: .85))),
          const SizedBox(height: 16),
          Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
            for (final a in aksi)
              Column(children: [
                IconButton.filledTonal(onPressed: () {}, tooltip: a.label, icon: Icon(a.ikon)),
                Text(a.label, style: t.labelSmall?.copyWith(color: c.onPrimary)),
              ]),
          ]),
        ]),
      ),
    );
  }
}

class DaftarItem extends StatelessWidget {
  const DaftarItem({super.key, required this.items});
  final List<ItemDaftar> items;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    return Card(
      child: Column(children: [
        for (final (i, it) in items.indexed) ...[
          if (i > 0) const Divider(height: 1, indent: 72),
          ListTile(
            minVerticalPadding: 12,
            leading: CircleAvatar(backgroundColor: it.warna.withValues(alpha: .14), child: Icon(it.ikon, color: it.warna)),
            title: Text(it.judul, style: const TextStyle(fontWeight: FontWeight.w700)),
            subtitle: Text(it.sub),
            trailing: Text(
              it.kanan,
              style: TextStyle(
                fontWeight: FontWeight.w700,
                fontFeatures: const [FontFeature.tabularFigures()],
                color: it.kanan.startsWith('+') ? Colors.green.shade700 : c.onSurface,
              ),
            ),
            onTap: () {},
          ),
        ],
      ]),
    );
  }
}

class BannerInfo extends StatelessWidget {
  const BannerInfo({super.key, required this.judul, required this.sub, required this.label, required this.ikon});
  final String judul, sub, label;
  final IconData ikon;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    final t = Theme.of(context).textTheme;
    return Card(
      color: c.primaryContainer,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Row(children: [
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              if (label.isNotEmpty) Text(label, style: t.labelMedium?.copyWith(color: c.primary, letterSpacing: 1)),
              const SizedBox(height: 4),
              Text(judul, style: t.titleLarge?.copyWith(color: c.onPrimaryContainer)),
              const SizedBox(height: 4),
              Text(sub, style: t.bodyMedium?.copyWith(color: c.onPrimaryContainer)),
            ]),
          ),
          const SizedBox(width: 12),
          Icon(ikon, size: 48, color: c.primary),
        ]),
      ),
    );
  }
}

class KartuRingkas extends StatelessWidget {
  const KartuRingkas({super.key, required this.baris, this.total});
  final List<(String, String)> baris;
  final (String, String)? total;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    Widget row((String, String) r, {bool tebal = false}) => Padding(
          padding: const EdgeInsets.symmetric(vertical: 6),
          child: Row(children: [
            Expanded(child: Text(r.$1, style: tebal ? t.titleMedium : t.bodyMedium)),
            Text(r.$2, style: (tebal ? t.titleMedium : t.bodyMedium)?.copyWith(fontWeight: FontWeight.w700)),
          ]),
        );
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(children: [
          for (final r in baris) row(r),
          if (total != null) ...[const Divider(), row(total!, tebal: true)],
        ]),
      ),
    );
  }
}

// ---------------------------------------------------------------- produk
class GridProduk extends StatelessWidget {
  const GridProduk({super.key, required this.items});
  final List<Produk> items;

  @override
  Widget build(BuildContext context) {
    // LayoutBuilder: 2 kolom di HP, 3-4 kolom di tablet (layout adaptif).
    return LayoutBuilder(builder: (context, box) {
      final kolom = box.maxWidth >= 840 ? 4 : box.maxWidth >= 600 ? 3 : 2;
      return GridView.count(
        crossAxisCount: kolom,
        shrinkWrap: true,
        physics: const NeverScrollableScrollPhysics(),
        mainAxisSpacing: 12,
        crossAxisSpacing: 12,
        childAspectRatio: .62,
        children: [for (final p in items) KartuProduk(p)],
      );
    });
  }
}

class KartuProduk extends StatelessWidget {
  const KartuProduk(this.p, {super.key});
  final Produk p;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    return Card(
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: () {},
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          AspectRatio(
            aspectRatio: 1,
            child: Stack(children: [
              Positioned.fill(child: ColoredBox(color: p.warna, child: Icon(p.ikon, size: 48, color: Colors.white))),
              if (p.lencana != null)
                Positioned(left: 8, top: 8, child: Chip(label: Text(p.lencana!), visualDensity: VisualDensity.compact)),
            ]),
          ),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(p.nama, style: t.titleSmall, maxLines: 2, overflow: TextOverflow.ellipsis),
              Text(p.sub, style: t.bodySmall, maxLines: 1, overflow: TextOverflow.ellipsis),
              const SizedBox(height: 4),
              Text(p.harga, style: t.titleMedium?.copyWith(fontWeight: FontWeight.w800)),
            ]),
          ),
        ]),
      ),
    );
  }
}

// ---------------------------------------------------------------- input
class KotakCari extends StatelessWidget {
  const KotakCari({super.key, required this.petunjuk, this.filter = true});
  final String petunjuk;
  final bool filter;

  @override
  Widget build(BuildContext context) {
    return SearchBar(
      hintText: petunjuk,
      leading: const Icon(Icons.search),
      trailing: [if (filter) IconButton(onPressed: () {}, tooltip: 'Filter', icon: const Icon(Icons.tune))],
      elevation: const WidgetStatePropertyAll(0),
    );
  }
}

class BarisChip extends StatefulWidget {
  const BarisChip({super.key, required this.items});
  final List<String> items;

  @override
  State<BarisChip> createState() => _BarisChipState();
}

class _BarisChipState extends State<BarisChip> {
  int dipilih = 0;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(children: [
        for (final (i, x) in widget.items.indexed)
          Padding(
            padding: const EdgeInsets.only(right: 8),
            child: FilterChip(label: Text(x), selected: i == dipilih, onSelected: (_) => setState(() => dipilih = i)),
          ),
      ]),
    );
  }
}

class PilihSlot extends StatefulWidget {
  const PilihSlot({super.key, required this.judul, required this.slot, this.awal = 0});
  final String judul;
  final List<String> slot;
  final int awal;

  @override
  State<PilihSlot> createState() => _PilihSlotState();
}

class _PilihSlotState extends State<PilihSlot> {
  late int dipilih = widget.awal;

  @override
  Widget build(BuildContext context) {
    return Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(widget.judul, style: Theme.of(context).textTheme.titleMedium),
      const SizedBox(height: 8),
      Wrap(spacing: 8, runSpacing: 8, children: [
        for (final (i, s) in widget.slot.indexed)
          ChoiceChip(label: Text(s), selected: i == dipilih, onSelected: (_) => setState(() => dipilih = i)),
      ]),
    ]);
  }
}

class PilihSegmen extends StatefulWidget {
  const PilihSegmen({super.key, required this.opsi});
  final List<String> opsi;

  @override
  State<PilihSegmen> createState() => _PilihSegmenState();
}

class _PilihSegmenState extends State<PilihSegmen> {
  int dipilih = 0;

  @override
  Widget build(BuildContext context) {
    return SegmentedButton<int>(
      segments: [for (final (i, o) in widget.opsi.indexed) ButtonSegment(value: i, label: Text(o))],
      selected: {dipilih},
      onSelectionChanged: (s) => setState(() => dipilih = s.first),
    );
  }
}

class FormIsian extends StatelessWidget {
  const FormIsian({super.key, required this.isian});
  final List<Isian> isian;

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      for (final (i, f) in isian.indexed) ...[
        if (i > 0) const SizedBox(height: 16),
        TextFormField(
          initialValue: f.nilai,
          textInputAction: i == isian.length - 1 ? TextInputAction.done : TextInputAction.next,
          keyboardType: RegExp(r'Jumlah|Rp|nomor|kurs', caseSensitive: false).hasMatch(f.label + (f.nilai ?? '')) ? TextInputType.number : TextInputType.text,
          decoration: InputDecoration(
            labelText: f.label,
            hintText: f.petunjuk,
            prefixIcon: Icon(f.ikon),
            errorText: f.galat,
            helperText: f.bantuan,
          ),
        ),
      ],
    ]);
  }
}

// ---------------------------------------------------------------- status & visual
class IndikatorLangkah extends StatelessWidget {
  const IndikatorLangkah({super.key, required this.langkah, required this.aktif});
  final List<String> langkah;
  final int aktif;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    return Semantics(
      label: 'Langkah ${aktif + 1} dari ${langkah.length}: ${langkah[aktif]}',
      child: ExcludeSemantics(
        child: Row(children: [
          for (final (i, l) in langkah.indexed) ...[
            if (i > 0) Expanded(child: Divider(thickness: 2, color: i <= aktif ? c.primary : c.outlineVariant)),
            Column(mainAxisSize: MainAxisSize.min, children: [
              CircleAvatar(
                radius: 14,
                backgroundColor: i <= aktif ? c.primary : c.surfaceContainerHighest,
                foregroundColor: i <= aktif ? c.onPrimary : c.onSurfaceVariant,
                child: i < aktif ? const Icon(Icons.check, size: 16) : Text('${i + 1}', style: const TextStyle(fontSize: 12)),
              ),
              const SizedBox(height: 4),
              Text(l, style: Theme.of(context).textTheme.labelSmall),
            ]),
          ],
        ]),
      ),
    );
  }
}

class GrafikBatang extends StatelessWidget {
  const GrafikBatang({super.key, required this.judul, required this.data, required this.label});
  final String judul;
  final List<double> data;
  final List<String> label;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(judul, style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 12),
          Semantics(
            label: '$judul: ${[for (var i = 0; i < data.length; i++) '${label[i]} ${data[i]}'].join(', ')}',
            child: SizedBox(height: 160, width: double.infinity, child: CustomPaint(painter: _Batang(data, c.primary))),
          ),
          const SizedBox(height: 6),
          Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [for (final l in label) Text(l, style: Theme.of(context).textTheme.labelSmall)]),
        ]),
      ),
    );
  }
}

class _Batang extends CustomPainter {
  _Batang(this.data, this.warna);
  final List<double> data;
  final Color warna;

  @override
  void paint(Canvas canvas, Size size) {
    final maks = data.reduce((a, b) => a > b ? a : b);
    final min = data.reduce((a, b) => a < b ? a : b);
    // Rentang sempit (mis. kurs): sumbu dimulai sedikit di bawah nilai terkecil agar perbedaan terlihat.
    final dasar = maks - min < maks * .1 ? min - (maks - min) * .5 : 0.0;
    final lebar = size.width / data.length;
    final cat = Paint()..color = warna;
    for (var i = 0; i < data.length; i++) {
      final h = (data[i] - dasar) / (maks - dasar) * size.height;
      canvas.drawRRect(
        RRect.fromRectAndRadius(Rect.fromLTWH(i * lebar + lebar * .2, size.height - h, lebar * .6, h), const Radius.circular(4)),
        cat,
      );
    }
  }

  @override
  bool shouldRepaint(_Batang old) => old.data != data || old.warna != warna;
}

class PetaRute extends StatelessWidget {
  const PetaRute({super.key, required this.tinggi, required this.label});
  final double tinggi;
  final String label;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    // Ganti dengan GoogleMap / flutter_map; placeholder ini menjaga tata letak sama dengan desain.
    return Semantics(
      label: label,
      child: ClipRRect(
        borderRadius: BorderRadius.circular(16),
        child: Container(
          height: tinggi,
          color: c.surfaceContainerHighest,
          alignment: Alignment.center,
          child: Icon(Icons.place, size: 48, color: c.primary),
        ),
      ),
    );
  }
}

class KeadaanKosong extends StatelessWidget {
  const KeadaanKosong({super.key, required this.ikon, required this.judul, required this.sub, required this.aksi});
  final IconData ikon;
  final String judul, sub, aksi;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 32),
      child: Column(children: [
        Icon(ikon, size: 64, color: Theme.of(context).colorScheme.primary),
        const SizedBox(height: 16),
        Text(judul, style: t.titleLarge, textAlign: TextAlign.center),
        const SizedBox(height: 8),
        Text(sub, style: t.bodyMedium, textAlign: TextAlign.center),
        const SizedBox(height: 24),
        FilledButton(onPressed: () {}, child: Text(aksi)),
      ]),
    );
  }
}

class Percakapan extends StatelessWidget {
  const Percakapan({super.key, required this.pesan});
  final List<Pesan> pesan;

  @override
  Widget build(BuildContext context) {
    final c = Theme.of(context).colorScheme;
    return Column(children: [
      for (final p in pesan)
        Align(
          alignment: p.dariSaya ? Alignment.centerRight : Alignment.centerLeft,
          child: Container(
            margin: const EdgeInsets.only(bottom: 8),
            padding: const EdgeInsets.all(12),
            constraints: const BoxConstraints(maxWidth: 300),
            decoration: BoxDecoration(
              color: p.dariSaya ? c.primary : c.surfaceContainerHighest,
              borderRadius: BorderRadius.circular(16),
            ),
            child: Text(p.teks, style: TextStyle(color: p.dariSaya ? c.onPrimary : c.onSurface)),
          ),
        ),
    ]);
  }
}

// ---------------------------------------------------------------- bawah layar
class NavBawah extends StatefulWidget {
  const NavBawah({super.key, required this.item, this.awal = 0});
  final List<(IconData, String)> item;
  final int awal;

  @override
  State<NavBawah> createState() => _NavBawahState();
}

class _NavBawahState extends State<NavBawah> {
  late int aktif = widget.awal;

  @override
  Widget build(BuildContext context) {
    return NavigationBar(
      selectedIndex: aktif,
      onDestinationSelected: (i) => setState(() => aktif = i),
      destinations: [for (final (ik, l) in widget.item) NavigationDestination(icon: Icon(ik), label: l)],
    );
  }
}

class AksiBawah extends StatelessWidget {
  const AksiBawah({super.key, required this.label, this.label2, this.info});
  final String label;
  final String? label2;
  final (String, String)? info;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.fromLTRB(16, 12, 16, 12),
        child: Row(children: [
          if (info != null)
            Expanded(
              child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(info!.$1, style: t.bodySmall),
                Text(info!.$2, style: t.titleLarge?.copyWith(fontWeight: FontWeight.w800)),
              ]),
            ),
          if (label2 != null) ...[
            Expanded(child: OutlinedButton(onPressed: () {}, child: Text(label2!))),
            const SizedBox(width: 12),
          ],
          Expanded(child: FilledButton(onPressed: () {}, child: Text(label))),
        ]),
      ),
    );
  }
}

class MasukanChat extends StatelessWidget {
  const MasukanChat({super.key});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Padding(
        // viewInsets: kolom naik saat keyboard muncul.
        padding: EdgeInsets.fromLTRB(16, 8, 8, 8 + MediaQuery.viewInsetsOf(context).bottom),
        child: Row(children: [
          const Expanded(
            child: TextField(
              minLines: 1,
              maxLines: 4,
              textInputAction: TextInputAction.send,
              decoration: InputDecoration(hintText: 'Tanya soal keuanganmu…'),
            ),
          ),
          const SizedBox(width: 8),
          IconButton.filled(onPressed: () {}, tooltip: 'Kirim', icon: const Icon(Icons.send)),
        ]),
      ),
    );
  }
}
"""


def tema_dart(spec):
    T = palet(spec)
    t = T.t
    gelap = spec['gaya'] == 'gelap'
    fj, fb = (T.fj or FONT), (T.fb or FONT)
    return f"""import 'package:flutter/material.dart';

/// Tema dari tokens.json kit "{spec['token']['nama']}" (gaya {spec['gaya']}).
/// Semua widget membaca warna/huruf/radius dari sini — tidak ada Color(0x..) di layar.
class Token {{
  static const primer = {dc(t['primer'])};
  static const primer2 = {dc(t['primer2'])};
  static const aksen = {dc(t['aksen'])};
  static const latar = {dc(t['latar'])};
  static const permukaan = {dc(t['permukaan'])};
  static const teks = {dc(t['teks'])};
  static const teks2 = {dc(t['teks2'])};
  static const garis = {dc(t['garis'])};
  static const bahaya = {dc(t['bahaya'])};
  static const radius = {float(T.r)};
  static const fontJudul = '{fj}';
  static const fontIsi = '{fb}';
}}

ThemeData buatTema() {{
  final skema = ColorScheme.fromSeed(
    seedColor: Token.primer,
    brightness: Brightness.{'dark' if gelap else 'light'},
  ).copyWith(
    primary: Token.primer,
    secondary: Token.aksen,
    surface: Token.latar,
    onSurface: Token.teks,
    onSurfaceVariant: Token.teks2,
    outline: Token.garis,
    error: Token.bahaya,
  );
  final bentuk = RoundedRectangleBorder(borderRadius: BorderRadius.circular(Token.radius));
  final dasar = ThemeData(useMaterial3: true, colorScheme: skema, fontFamily: Token.fontIsi);
  return dasar.copyWith(
    scaffoldBackgroundColor: Token.latar,
    textTheme: dasar.textTheme.copyWith(
      headlineMedium: dasar.textTheme.headlineMedium?.copyWith(fontFamily: Token.fontJudul, fontWeight: FontWeight.w{min(900, max(400, T.wj // 100 * 100))}),
      titleLarge: dasar.textTheme.titleLarge?.copyWith(fontFamily: Token.fontJudul, fontWeight: FontWeight.w{min(900, max(400, T.wj // 100 * 100))}),
    ),
    cardTheme: CardThemeData(
      elevation: 0,
      color: Token.permukaan,
      margin: EdgeInsets.zero,
      shape: bentuk.copyWith(side: const BorderSide(color: Token.garis{', width: 2' if T.tinta else ''})),
    ),
    filledButtonTheme: FilledButtonThemeData(style: FilledButton.styleFrom(minimumSize: const Size(64, 52), shape: bentuk)),
    outlinedButtonTheme: OutlinedButtonThemeData(style: OutlinedButton.styleFrom(minimumSize: const Size(64, 52), shape: bentuk)),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: Token.permukaan,
      border: OutlineInputBorder(borderRadius: BorderRadius.circular(Token.radius)),
    ),
    navigationBarTheme: const NavigationBarThemeData(backgroundColor: Token.permukaan),
  );
}}
"""


def flutter_final(spec):
    paket = slug(spec['token']['nama']).replace('-', '_')
    lay = [layar_dart(spec, l, i) for i, l in enumerate(spec['layar'])]
    imp = '\n'.join(f"import 'layar/{f}.dart';" for f, _, _, _ in lay)
    rute = '\n'.join(f"        {k}.rute: (_) => const {k}()," for _, k, _, _ in lay)
    main = f"""import 'package:flutter/material.dart';

{imp}
import 'tema.dart';

void main() => runApp(const Aplikasi());

class Aplikasi extends StatelessWidget {{
  const Aplikasi({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: '{spec['token']['nama']}',
      debugShowCheckedModeBanner: false,
      theme: buatTema(),
      initialRoute: {lay[0][1]}.rute,
      routes: {{
{rute}
      }},
    );
  }}
}}
"""
    teks_uji = []
    for (f, k, r, _), l in zip(lay, spec['layar']):
        kunci = next((d.get('jd') or d.get('teks') or d.get('label') or d.get('nama') for j, d in l[1] if isinstance(d, dict) and (d.get('jd') or d.get('teks') or d.get('label') or d.get('nama'))), None)
        teks_uji.append((f, k, kunci))
    tes = "import 'package:flutter/material.dart';\nimport 'package:flutter_test/flutter_test.dart';\n\n" + '\n'.join(f"import 'package:{paket}/layar/{f}.dart';" for f, _, _ in teks_uji) + f"\nimport 'package:{paket}/tema.dart';\n\n" + \
        "Future<void> pasang(WidgetTester t, Widget layar, {double lebar = 360}) async {\n  t.view.physicalSize = Size(lebar * 3, 800 * 3); // 360 × 800 dp pada 3x, sama dengan frame desain\n  t.view.devicePixelRatio = 3;\n  addTearDown(t.view.reset);\n  await t.pumpWidget(MaterialApp(theme: buatTema(), home: layar));\n}\n\nvoid main() {\n" + \
        ''.join(f"""  group('{k}', () {{
    testWidgets('menampilkan isi utama sesuai desain', (t) async {{
      await pasang(t, const {k}());
      {"expect(find.text(" + ds(kunci) + "), findsWidgets);" if kunci else "expect(find.byType(Scaffold), findsOneWidget);"}
    }});
    testWidgets('tidak overflow di HP kecil 320 dp dan tablet 800 dp', (t) async {{
      for (final lebar in [320.0, 800.0]) {{
        await pasang(t, const {k}(), lebar: lebar);
        expect(t.takeException(), isNull);
      }}
    }});
    testWidgets('lolos pedoman aksesibilitas', (t) async {{
      final h = t.ensureSemantics();
      await pasang(t, const {k}());
      await expectLater(t, meetsGuideline(androidTapTargetGuideline));
      await expectLater(t, meetsGuideline(labeledTapTargetGuideline));
      await expectLater(t, meetsGuideline(textContrastGuideline));
      h.dispose();
    }});
    testWidgets('golden 360 × 800', (t) async {{
      await pasang(t, const {k}());
      await expectLater(find.byType({k}), matchesGoldenFile('goldens/{f}.png'));
    }}, tags: 'golden');
  }});
""" for f, k, kunci in teks_uji) + "}\n"
    pub = f"""name: {paket}
description: Hasil slicing kit Figma "{spec['judul']}" (Ruang Kode).
publish_to: none
version: 1.0.0+1

environment:
  sdk: ^3.6.0
  flutter: ">=3.27.0"

dependencies:
  flutter:
    sdk: flutter
  google_fonts: ^6.2.1

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^5.0.0

flutter:
  uses-material-design: true
"""
    ana = """include: package:flutter_lints/flutter.yaml

analyzer:
  language:
    strict-casts: true
    strict-raw-types: true

linter:
  rules:
    - prefer_const_constructors
    - prefer_const_literals_to_create_immutables
    - prefer_final_locals
    - require_trailing_commas
    - always_declare_return_types
    - avoid_print
"""
    ci = """name: CI
on: [push, pull_request]
jobs:
  cek:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with: { channel: stable, cache: true }
      - run: flutter pub get
      - run: dart format --output=none --set-exit-if-changed .
      - run: flutter analyze
      - run: flutter test --exclude-tags golden
"""
    files = [('lib/main.dart', 'dart', main), ('lib/tema.dart', 'dart', tema_dart(spec))]
    files += [(f'lib/layar/{f}.dart', 'dart', kode) for f, _, _, kode in lay]
    files += [('lib/widgets/blok.dart', 'dart', BLOK_DART), ('test/layar_test.dart', 'dart', tes), ('pubspec.yaml', 'yaml', pub),
              ('analysis_options.yaml', 'yaml', ana), ('.github/workflows/ci.yml', 'yaml', ci),
              ('README.md', 'markdown', f"# {spec['token']['nama']} · {spec['judul']}\n\nHasil slicing kit Figma Ruang Kode (gaya **{spec['gaya']}**) ke Flutter + Material 3.\n\n"
               "```bash\nflutter pub get\nflutter run                      # emulator 360 × 800 dp\nflutter analyze                  # lint\nflutter test --exclude-tags golden\nflutter test --update-goldens    # buat acuan golden setelah desainer setuju\n```\n\n"
               "## Keputusan teknis\n- Token di `lib/tema.dart` sama dengan `tokens.json`; layar tidak menulis warna langsung.\n"
               "- Satu file per layar (`lib/layar/`), komponen bersama di `lib/widgets/blok.dart`.\n- Target sentuh ≥ 48 dp, tooltip untuk ikon, Semantics untuk grafik dan peta.\n"
               "- Font: tambahkan berkas font ke `assets/fonts` atau pakai `google_fonts` (`GoogleFonts.config.allowRuntimeFetching = false` untuk produksi).\n")]
    tree = f"{paket}/\n├── lib/\n│   ├── main.dart              # MaterialApp + rute\n│   ├── tema.dart              # ThemeData dari tokens.json\n│   ├── layar/\n" + \
        ''.join(f"│   │   ├── {f + '.dart':<26}# {l[0]}\n" for (f, _, _, _), l in zip(lay, spec['layar'])) + \
        "│   └── widgets/\n│       └── blok.dart          # komponen: kartu, daftar, form, grafik, navigasi\n├── test/\n│   └── layar_test.dart        # isi, overflow 320/800 dp, aksesibilitas, golden\n" + \
        "├── .github/workflows/ci.yml   # format, analyze, test\n├── analysis_options.yaml\n├── pubspec.yaml\n└── README.md"
    return dict(files=files, tree=tree, run='flutter create . --platforms=android,ios   # sekali, membuat folder platform\nflutter pub get\nflutter run\nflutter analyze\nflutter test --exclude-tags golden',
                n=f'Kode final ini dibangkitkan dari spesifikasi yang sama dengan kit Figma <b>{e(spec["judul"])}</b>: setiap blok di frame menjadi satu widget di <code>lib/widgets/blok.dart</code>, dan token menjadi <code>ThemeData</code>. Bandingkan hasil <code>flutter run</code> dengan gambar pratinjau kit di atas.',
                cek=CEK_FLUTTER)


CEK_FLUTTER = [
    ['Kesetiaan desain', 'Urutan widget, teks, warna, radius, dan jarak sama dengan frame 360 × 800 dp'],
    ['Tema', 'Warna dan huruf hanya dari ThemeData/ColorScheme; tidak ada Color(0x..) di file layar'],
    ['Struktur', 'Satu file per layar, komponen dipakai ulang di widgets/, data dipisah dari tampilan'],
    ['Const dan rebuild', 'Widget statis memakai const; state lokal sekecil mungkin (StatefulWidget hanya untuk chip, segmen, navigasi)'],
    ['Responsif', 'Tidak overflow di 320 dp, huruf 200%, dan tablet; grid adaptif dengan LayoutBuilder'],
    ['Aksesibilitas', 'Target sentuh 48 dp, tooltip/semanticsLabel untuk ikon, Semantics untuk grafik dan peta, kontras AA'],
    ['Safe area dan keyboard', 'SafeArea di body dan tombol bawah; input chat naik dengan viewInsets'],
    ['Kualitas kode', 'dart format bersih, flutter analyze tanpa peringatan (flutter_lints)'],
    ['Pengujian', 'Widget test untuk isi, overflow, pedoman aksesibilitas, dan golden test; berjalan di CI'],
]
