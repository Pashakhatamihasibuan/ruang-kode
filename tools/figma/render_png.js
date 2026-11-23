// node render_png.js daftar.json  -> daftar: [[svg, png, skala], ...]. Font diambil dari Google Fonts.
const {chromium} = require('playwright'); const fs = require('fs');
const daftar = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const fam = ['Plus Jakarta Sans:wght@400;500;600;700;800', 'Space Grotesk:wght@400;500;600;700', 'Sora:wght@400;500;600;700;800', 'Roboto Flex:wght@400;500;600;700;800',
  'Outfit:wght@400;500;600;700;800', 'Nunito:wght@400;500;600;700;800', 'Fraunces:wght@400;500;600;700;800', 'Space Mono:wght@400;700', 'Dela Gothic One'];
const link = 'https://fonts.googleapis.com/css2?' + fam.map(f => 'family=' + f.replace(/ /g, '+')).join('&') + '&display=block';
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.setContent(`<html><head><link rel="stylesheet" href="${link}"><style>body{margin:0}</style></head><body><div id="w"></div>
  <span style="font-family:'Plus Jakarta Sans'">a</span><span style="font-family:'Space Grotesk'">a</span><span style="font-family:Sora">a</span><span style="font-family:'Roboto Flex'">a</span><span style="font-family:Outfit">a</span><span style="font-family:Nunito">a</span><span style="font-family:Fraunces">a</span><span style="font-family:'Space Mono'">a</span><span style="font-family:'Dela Gothic One'">a</span></body></html>`, {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  for (const [svg, png, sk] of daftar) {
    const isi = fs.readFileSync(svg, 'utf8');
    const m = isi.match(/width="(\d+)" height="(\d+)"/);
    const w = +m[1], h = +m[2];
    await p.setViewportSize({width: Math.ceil(w * sk), height: Math.ceil(h * sk)});
    await p.evaluate(([isi, sk]) => { const d = document.getElementById('w'); d.innerHTML = isi; const s = d.querySelector('svg'); s.setAttribute('width', s.getAttribute('width') * sk); s.setAttribute('height', s.getAttribute('height') * sk); s.style.display = 'block'; }, [isi, sk]);
    await p.evaluate(() => document.fonts.ready);
    await p.locator('#w svg').screenshot({path: png});
  }
  await b.close();
})();
