"""Prototype HTML klik-through (tanpa dependensi) + demo mikro-interaksi. Dibuka langsung di browser dari ZIP."""
import json

TRANSISI = {'dissolve': 'Dissolve', 'push': 'Push dari kanan', 'smart': 'Smart Animate', 'spring': 'Smart Animate + Spring', 'instant': 'Instant', 'overlay': 'Overlay'}


def html(judul, layar, platform='hp', warna='#8A4B2A', mikro=True):
    """layar: [{nama, svg, trans, dur, ease, pemicu}] — trans dipakai saat MASUK ke layar itu."""
    data = json.dumps([{k: v for k, v in l.items()} for l in layar], ensure_ascii=False)
    lebar = 390 if platform == 'hp' else 1440
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prototype {judul}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;700&family=Sora:wght@400;600;700&family=Roboto+Flex:wght@400;700;800&family=Outfit:wght@400;600;700&family=Nunito:wght@400;700;800&family=Fraunces:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap">
<style>
:root{{--aksen:{warna};--bg:#111114;--fg:#F4F4F6;--muted:#A4A4AE;--kartu:#1C1C21}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 'Plus Jakarta Sans',system-ui,sans-serif}}
header{{padding:20px max(16px,4vw);display:flex;gap:16px;align-items:center;flex-wrap:wrap;justify-content:space-between}}
h1{{font-size:20px;margin:0}} .muted{{color:var(--muted)}}
main{{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:24px;padding:0 max(16px,4vw) 40px}}
@media (max-width:900px){{main{{grid-template-columns:1fr}}}}
.panggung{{display:flex;justify-content:center;align-items:flex-start;min-width:0}}
.hp{{width:min({lebar}px,100%);aspect-ratio:{'390/844' if platform == 'hp' else 'auto'};position:relative;overflow:hidden;border-radius:{'44px' if platform == 'hp' else '12px'};
  box-shadow:0 0 0 10px #2A2A30,0 30px 80px #0008;background:#000;cursor:pointer}}
.hp .lyr{{position:absolute;inset:0;will-change:transform,opacity}} .hp .lyr svg{{width:100%;height:auto;display:block}}
{'.hp{aspect-ratio:auto;height:80vh;overflow:auto}.hp .lyr{position:absolute;inset:0 0 auto 0}' if platform != 'hp' else ''}
aside{{background:var(--kartu);border-radius:16px;padding:20px;align-self:start}}
.btn{{font:600 14px inherit;font-family:inherit;border:0;border-radius:999px;padding:10px 18px;background:var(--aksen);color:#fff;cursor:pointer;min-height:44px}}
.btn.g{{background:transparent;color:var(--fg);box-shadow:inset 0 0 0 1.5px #4A4A52}}
.btn:focus-visible{{outline:3px solid #8AB4F8;outline-offset:2px}} .btn:active{{transform:scale(.97);transition:transform .1s ease-out}}
ol{{padding-left:20px;margin:8px 0}} li{{padding:4px 0;cursor:pointer}} li.on{{color:#fff;font-weight:700}} li:not(.on){{color:var(--muted)}}
.spek{{background:#26262C;border-radius:12px;padding:12px;margin:12px 0;font-size:13px}} code{{font-family:'Space Mono',monospace;font-size:12px}}
/* transisi */
@keyframes masukKanan{{from{{transform:translateX(100%)}}to{{transform:none}}}}
@keyframes keluarKiri{{to{{transform:translateX(-30%);opacity:.6}}}}
@keyframes larut{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes zoom{{from{{transform:scale(.86);opacity:0;border-radius:24px}}to{{transform:none;opacity:1}}}}
@keyframes pegas{{0%{{transform:scale(.8);opacity:0}}60%{{transform:scale(1.03);opacity:1}}100%{{transform:none}}}}
/* mikro-interaksi */
.demo{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;padding:0 max(16px,4vw) 48px}}
.d{{background:var(--kartu);border-radius:16px;padding:20px;min-height:170px;display:flex;flex-direction:column;gap:12px}}
.d h3{{margin:0;font-size:15px}} .d p{{margin:0;font-size:13px;color:var(--muted)}}
.skel{{height:14px;border-radius:7px;background:linear-gradient(90deg,#2A2A30 25%,#3A3A42 50%,#2A2A30 75%);background-size:200% 100%;animation:shimmer 1.2s linear infinite}}
@keyframes shimmer{{to{{background-position:-200% 0}}}}
.badge{{display:inline-grid;place-items:center;min-width:24px;height:24px;border-radius:12px;background:#E5484D;color:#fff;font-weight:700;font-size:12px}}
.bounce{{animation:pegas .3s cubic-bezier(.34,1.56,.64,1)}}
.toast{{position:relative;background:#2B2724;border-radius:12px;padding:12px 16px;transform:translateY(16px);opacity:0;transition:transform .2s ease-out,opacity .2s ease-out}}
.toast.on{{transform:none;opacity:1}}
.cek path{{stroke-dasharray:40;stroke-dashoffset:40}} .cek.on path{{animation:gambar .4s ease-out forwards}} .cek.on{{animation:pegas .4s cubic-bezier(.34,1.56,.64,1)}}
@keyframes gambar{{to{{stroke-dashoffset:0}}}}
@media (prefers-reduced-motion:reduce){{*,*::before,*::after{{animation-duration:.01ms!important;transition-duration:.01ms!important}}}}
</style></head><body>
<header><div><h1>Prototype: {judul}</h1><div class="muted">Klik layar atau tekan → untuk lanjut, ← untuk kembali. Animasi mengikuti spesifikasi motion di kit.</div></div>
<div style="display:flex;gap:8px"><button class="btn g" id="kembali">← Kembali</button><button class="btn" id="lanjut">Lanjut →</button></div></header>
<main><div class="panggung"><div class="hp" id="hp" role="button" tabindex="0" aria-label="Layar prototype, klik untuk lanjut"></div></div>
<aside><div class="muted" style="font-size:13px">ALUR</div><ol id="alur"></ol><div class="spek" id="spek"></div>
<p class="muted" style="font-size:13px">Di Figma: tab Prototype, tarik sambungan dari tombol ke frame tujuan, pilih animasi dan durasi yang sama seperti di atas.</p></aside></main>
{_mikro() if mikro else ''}
<script>
const L={data};let i=0;const hp=document.getElementById('hp'),alur=document.getElementById('alur'),spek=document.getElementById('spek');
const anim={{dissolve:'larut',push:'masukKanan',smart:'zoom',spring:'pegas',overlay:'larut',instant:''}};
L.forEach((l,k)=>{{const li=document.createElement('li');li.textContent=l.nama;li.onclick=()=>ke(k,k>i?1:-1);alur.appendChild(li)}});
function ke(n,arah){{if(n<0||n>=L.length)return;const l=L[n];const baru=document.createElement('div');baru.className='lyr';baru.innerHTML=l.svg;
 const lama=hp.querySelector('.lyr');const a=arah>0?anim[l.trans||'push']:'larut';const d=(arah>0?l.dur:200)||1;
 if(a)baru.style.animation=`${{a}} ${{d}}ms ${{arah>0&&l.ease&&!l.ease.startsWith('spring')?l.ease:'cubic-bezier(.34,1.56,.64,1)'}} both`;
 if(lama&&a==='masukKanan')lama.style.animation=`keluarKiri ${{d}}ms ease-out both`;
 hp.appendChild(baru);setTimeout(()=>{{hp.querySelectorAll('.lyr').forEach(x=>{{if(x!==baru)x.remove()}})}},d+20);
 i=n;[...alur.children].forEach((c,k)=>c.className=k===i?'on':'');
 spek.innerHTML=n===0?'<b>Layar awal</b>':`<b>${{L[n-1].nama}} → ${{l.nama}}</b><br>Pemicu: ${{l.pemicu||'Tap CTA utama'}}<br>Animasi: ${{l.label||l.trans}}<br>Durasi: <code>${{l.dur||0}} ms</code> · Easing: <code>${{l.ease||'ease-out'}}</code>`;}}
document.getElementById('lanjut').onclick=()=>ke(i+1,1);document.getElementById('kembali').onclick=()=>ke(i-1,-1);
hp.onclick=()=>ke(i+1,1);hp.onkeydown=e=>{{if(e.key==='Enter'||e.key===' '){{e.preventDefault();ke(i+1,1)}}}};
document.onkeydown=e=>{{if(e.key==='ArrowRight')ke(i+1,1);if(e.key==='ArrowLeft')ke(i-1,-1)}};ke(0,1);
document.querySelectorAll('[data-ulang]').forEach(b=>b.onclick=()=>{{const t=document.getElementById(b.dataset.ulang);
 if(t.id==='bdg'){{t.textContent=+t.textContent+1;t.classList.remove('bounce');void t.offsetWidth;t.classList.add('bounce')}}
 else{{t.classList.remove('on');void t.offsetWidth;t.classList.add('on');if(t.id==='tst')setTimeout(()=>t.classList.remove('on'),4000)}}}});
</script></body></html>'''


def _mikro():
    return '''<h2 style="padding:0 max(16px,4vw);font-size:18px">Mikro-interaksi (CSS, hormati prefers-reduced-motion)</h2>
<section class="demo">
<div class="d"><h3>Tombol tekan</h3><p>scale 0.97 · 100ms ease-out</p><button class="btn">Tekan saya</button></div>
<div class="d"><h3>Tambah ke keranjang</h3><p>badge +1 · 300ms spring</p><div style="display:flex;gap:12px;align-items:center"><button class="btn" data-ulang="bdg">Tambah</button><span>Keranjang <span class="badge" id="bdg">2</span></span></div></div>
<div class="d"><h3>Skeleton memuat</h3><p>shimmer · 1200ms linear · loop</p><div class="skel" style="width:80%"></div><div class="skel" style="width:60%"></div><div class="skel" style="width:40%"></div></div>
<div class="d"><h3>Toast</h3><p>slide up 16px + fade · 200ms · hilang 4 detik</p><button class="btn g" data-ulang="tst">Tampilkan toast</button><div class="toast" id="tst">✓ Ditambahkan ke keranjang</div></div>
<div class="d"><h3>Centang berhasil</h3><p>stroke draw 400ms + spring</p><button class="btn g" data-ulang="cek">Putar</button>
<svg class="cek on" id="cek" width="64" height="64" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#1E7A4C"/><path d="M18 33l9 9 19-20" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</section>'''
