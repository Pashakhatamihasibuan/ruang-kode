"""Pratinjau visual hasil kode Flutter/Compose (HTML tiruan layar Material 3), dipakai di pelajaran slicing mobile.
Setiap fungsi mengembalikan dokumen HTML lengkap untuk iframe srcdoc (tanpa skrip)."""

TEMA = {
    'kopi': dict(primary='#8A4B2A', onp='#FFFFFF', surface='#FBF7F2', onsurf='#2B2724', var='#6B625B', outline='#C9BBAE', field='#FFFFFF', err='#B3261E', cont='#F1E6DC'),
    'default': dict(primary='#6750A4', onp='#FFFFFF', surface='#FEF7FF', onsurf='#1D1B20', var='#49454F', outline='#79747E', field='#FEF7FF', err='#B3261E', cont='#EADDFF'),
    'gelap': dict(primary='#FFB68F', onp='#522300', surface='#1A1310', onsurf='#F0DFD7', var='#D7C2B8', outline='#A08D84', field='#231A16', err='#FFB4AB', cont='#3A2A22'),
}

CSS = '''*{box-sizing:border-box}html,body{margin:0;height:100%}
body{font:calc(14px*var(--fs)) / 1.43 Roboto,"Segoe UI",system-ui,sans-serif;background:var(--surface);color:var(--onsurf);display:flex;flex-direction:column;overflow:hidden}
.st{height:28px;flex:none;display:flex;justify-content:space-between;align-items:center;padding:0 20px;font:500 12px system-ui;color:var(--onsurf)}
.sc{flex:1;overflow:hidden;position:relative}
.isi{padding:24px;display:flex;flex-direction:column;max-width:480px;margin:0 auto}
.logo{width:48px;height:48px;border-radius:12px;background:var(--primary);color:var(--onp);display:grid;place-items:center;font-weight:800;font-size:16px}
h1{margin:24px 0 4px;font-size:calc(24px*var(--fs));line-height:1.33;font-weight:700}
.sub{margin:0 0 32px;color:var(--var)}
.tf{position:relative;height:56px;border:1px solid var(--outline);border-radius:12px;background:var(--field);display:flex;align-items:center;padding:0 16px;font-size:calc(16px*var(--fs))}
.tf label{position:absolute;left:12px;top:-9px;padding:0 4px;background:var(--field);font-size:calc(12px*var(--fs));color:var(--var)}
.tf.ph label{position:static;padding:0;background:none;font-size:inherit}
.tf.fokus{border:2px solid var(--primary)}.tf.fokus label{color:var(--primary)}
.tf.err{border:2px solid var(--err)}.tf.err label{color:var(--err)}
.tf .ik{margin-left:auto;width:24px;height:24px;display:grid;place-items:center;color:var(--var)}
.help{margin:4px 16px 0;font-size:calc(12px*var(--fs));color:var(--err)}
.gap16{height:16px}.gap8{height:8px}.gap24{height:24px}
.lupa{align-self:flex-end;color:var(--primary);font-weight:500;padding:10px 12px;margin-right:-12px}
.fb{height:48px;border-radius:12px;background:var(--primary);color:var(--onp);display:grid;place-items:center;font-weight:600;font-size:calc(14px*var(--fs))}
.fb.off{background:color-mix(in srgb,var(--onsurf) 12%,transparent);color:color-mix(in srgb,var(--onsurf) 38%,transparent)}
.ob{height:48px;border-radius:12px;border:1px solid var(--outline);display:grid;place-items:center;font-weight:600;color:var(--primary)}
.atau{text-align:center;color:var(--var);margin:16px 0}
.spin{width:20px;height:20px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent}
.ph-blok{height:236px;border:2px dashed var(--outline);border-radius:12px;display:grid;place-items:center;color:var(--var);font:500 12px ui-monospace,monospace;text-align:center;padding:8px}
.snack{position:absolute;left:12px;right:12px;bottom:16px;background:#322F35;color:#F5EFF7;border-radius:4px;padding:14px 16px;font-size:14px;box-shadow:0 3px 6px #0004}
.kb{flex:none;height:300px;background:#E8E2E8;display:grid;grid-template-rows:repeat(4,1fr);gap:8px;padding:10px 6px 30px}
.kb div{display:flex;gap:6px;justify-content:center}.kb span{flex:0 1 32px;background:#fff;border-radius:6px;height:100%}
.kb .done{flex:0 1 64px;background:var(--primary)}
.nav{flex:none;height:24px;display:grid;place-items:center}.nav i{width:108px;height:4px;border-radius:2px;background:var(--onsurf);opacity:.5}
.ovl [data-b]{position:relative;outline:2px dashed #F24E1E;outline-offset:2px}
.ovl [data-b]::after{content:attr(data-b);position:absolute;right:-4px;top:-4px;background:#F24E1E;color:#fff;font:600 9px/1 system-ui;padding:3px 4px;border-radius:0 3px 0 3px;white-space:nowrap;z-index:2}
.ovl .tf label{z-index:1}
.rl{position:absolute;left:24px;font:600 9px/1 system-ui;color:#fff;background:#7B61FF;padding:2px 4px;border-radius:3px}
'''


def _ikon_mata(lihat):
    return '◉' if not lihat else '◎'


def masuk(tema='kopi', tahap='form', email='rina@contoh.id', sandi='••••••••', fokus=None, err_email=None,
          memuat=False, snack=None, lihat=False, keyboard=False, fs=1.0, w=360, h=760, overlay=False, scroll=0):
    t = TEMA[tema]
    var = ';'.join(f'--{k}:{v}' for k, v in t.items()) + f';--fs:{fs}'
    kepala = '<div data-b="Header: logo 48 · judul · sub"><div class="logo">KK</div><h1>Masuk</h1><p class="sub">Pesan kopi favoritmu lebih cepat.</p></div>'
    if tahap == 'kerangka':
        form = '<div class="ph-blok">FormMasuk()<br>dibuat di Langkah 4</div>'
    else:
        e_cls = 'err' if err_email else ('fokus' if fokus == 'email' else '')
        s_cls = 'fokus' if fokus == 'sandi' else ''
        e_isi = f'<label>Email</label>{email}' if email else '<label>Email</label>'
        if not email and fokus != 'email':
            e_isi, e_cls = '<label>Email</label>', e_cls + ' ph'
        form = (f'<div class="tf {e_cls}" data-b="TextField email 56">{e_isi}' + ('<span class="ik" style="color:var(--err)">!</span>' if err_email else '') + '</div>'
                + (f'<p class="help">{err_email}</p>' if err_email else '')
                + '<div class="gap16"></div>'
                + f'<div class="tf {s_cls}" data-b="TextField sandi 56"><label>Kata sandi</label>{"kopi2026" if lihat else sandi}<span class="ik">{_ikon_mata(lihat)}</span></div>'
                + '<div class="gap8"></div><span class="lupa" data-b="TextButton">Lupa kata sandi?</span><div class="gap24"></div>'
                + ('<div class="fb off"><span class="spin"></span></div>' if memuat else '<div class="fb" data-b="FilledButton 48">Masuk</div>')
                + '<p class="atau" data-b="Teks atau">atau</p><div class="ob" data-b="OutlinedButton 48">Lanjut dengan Google</div>'
                + '<p style="text-align:center;margin:24px 0 0" data-b="Row daftar">Belum punya akun? <b style="color:var(--primary)">Daftar</b></p>')
    ov = '<span class="rl" style="top:2px">padding 24 · SingleChildScrollView</span>' if overlay else ''
    st = 'transform:translateY(-%dpx)' % scroll if scroll else ''
    tubuh = (f'<div class="st"><span>09.41</span><span>▲ ◼ 87%</span></div><div class="sc"><div class="isi" style="position:relative;{st}">{kepala}{form}{ov}</div>'
             + (f'<div class="snack">{snack}</div>' if snack else '') + '</div>'
             + ('<div class="kb">' + ''.join('<div>' + '<span></span>' * n + ('<span class="done"></span>' if i == 3 else '') + '</div>' for i, n in enumerate([10, 9, 7, 5])) + '</div>' if keyboard else '')
             + '<div class="nav"><i></i></div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>:root{{{var}}}{CSS}</style></head><body class="{"ovl" if overlay else ""}">{tubuh}</body></html>'


def s(t, d, w=360, h=760):
    return {'t': t, 'd': d, 'w': w, 'h': h}
