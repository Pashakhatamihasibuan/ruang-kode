/* ===================== JALUR CSS =====================
   Mengikuti roadmap.sh/css. Kebanyakan pelajaran jenis w (editor + pratinjau). */
const CSS_MODULES=[
{t:'Dasar CSS',lvl:'Pemula',d:'Anatomi aturan CSS, selector, dan cara browser memilih aturan yang menang.',
 nodes:['CSS Basics','CSS Rules','Selector','Declaration','Properties and Values','Comments','Simple Selectors','Element Selectors','Class Selectors','ID Selectors','Universal Selector','Grouping Selectors'],
 lessons:[
  {k:'w',t:'Aturan, selector & deklarasi',nodes:['CSS Rules','Selector','Declaration','Properties and Values','Comments'],
   b:['CSS (Cascading Style Sheets) mengatur tampilan HTML. Satu <b>aturan</b> terdiri dari <b>selector</b> (elemen mana) dan blok <b>deklarasi</b> di dalam kurung kurawal. Setiap deklarasi adalah pasangan <code>properti: nilai;</code>.',
      'Contoh: <code>h1 { color: #B4532A; font-size: 32px; }</code> berarti "semua h1 berwarna terakota dan berukuran 32 piksel". Komentar ditulis <code>/* ... */</code>.',
      'Ubah nilai di panel CSS dan lihat hasilnya langsung.'],
   html:`<h1>Toko Nusantara</h1>
<p>Kopi, teh, dan camilan pilihan.</p>
<p class="promo">Promo: gratis ongkir!</p>`,
   css:`/* aturan untuk semua h1 */
h1 {
  color: #B4532A;
  font-family: Georgia, serif;
}
p {
  color: #444;
  line-height: 1.6;
}
.promo {
  background: #FBE7A8;
  padding: 6px 10px;
}`,
   task:{q:'Buat semua paragraf berukuran huruf <code>18px</code>.',test:`getComputedStyle(document.querySelector('p')).fontSize==='18px'`,hint:'Tambahkan font-size: 18px; di aturan p.'},
   pts:['Aturan = selector + { deklarasi }.','Deklarasi = properti: nilai; dan diakhiri titik koma.','Komentar CSS: /* ... */.'],
   q:[['Bagian mana yang menentukan elemen sasaran?',['Selector','Properti','Nilai'],0,'Selector memilih elemen.']]},
  {k:'w',t:'Selector sederhana',nodes:['Simple Selectors','Element Selectors','Class Selectors','ID Selectors','Universal Selector','Grouping Selectors'],
   b:['Selector elemen memilih berdasarkan nama tag (<code>p</code>), selector class memakai titik (<code>.harga</code>), selector id memakai pagar (<code>#keranjang</code>), dan <code>*</code> memilih semua elemen.',
      'Beberapa selector bisa digabung dengan koma agar berbagi gaya: <code>h1, h2, h3 { ... }</code>. Selector juga bisa digabung tanpa spasi untuk syarat ganda: <code>p.promo</code> berarti paragraf yang punya class promo.',
      'Kebiasaan baik: utamakan class. Hindari id untuk gaya, karena id sangat kuat dan sulit ditimpa.'],
   html:`<h2>Keranjang</h2>
<p class="item">Kopi Gayo <span class="harga">Rp85.000</span></p>
<p class="item habis">Rendang Kaleng <span class="harga">Rp75.000</span></p>
<p id="total">Total: Rp85.000</p>`,
   css:`* { box-sizing: border-box; }
h2, #total { font-family: Georgia, serif; }
.item { padding: 6px; border-bottom: 1px solid #ddd; }
.harga { float: right; font-weight: 600; }
p.habis { color: #999; text-decoration: line-through; }
#total { font-size: 20px; }`,
   task:{q:'Buat semua elemen dengan class <code>harga</code> berwarna hijau <code>rgb(47, 122, 82)</code>.',test:`getComputedStyle(document.querySelector('.harga')).color==='rgb(47, 122, 82)'`,hint:'.harga { color: #2F7A52; }'},
   pts:['.class, #id, tag, dan * adalah selector sederhana.','Koma mengelompokkan selector.','Utamakan class untuk gaya.'],
   q:[['Selector untuk class "menu"?',['.menu','#menu','menu'],0,'Titik untuk class.'],
      ['p.promo memilih?',['Paragraf yang punya class promo','Semua p dan semua .promo','Elemen promo di dalam p'],0,'Tanpa spasi berarti syarat ganda pada elemen yang sama.']]},
  {k:'w',t:'Cascade & specificity',nodes:['Cascading Order','CSS Specificity'],viz:'specificity',
   b:['Kalau dua aturan mengatur properti yang sama, siapa yang menang? Browser memeriksa berurutan: <b>pentingnya</b> (!important), lalu <b>specificity</b> (kekuatan selector), lalu <b>urutan</b> (yang ditulis belakangan menang).',
      'Specificity dihitung sebagai tiga angka (a, b, c): a = jumlah id, b = jumlah class, atribut, dan pseudo-class, c = jumlah elemen dan pseudo-element. Bandingkan dari kiri: (1,0,0) mengalahkan (0,9,9).',
      'Gaya inline mengalahkan semuanya kecuali !important. Hindari !important; jika butuh, biasanya selectormu terlalu rumit.'],
   html:`<p id="info" class="pesan penting">Warna apa saya?</p>`,
   css:`p { color: gray; }               /* (0,0,1) */
.pesan { color: green; }         /* (0,1,0) */
p.pesan.penting { color: blue; } /* (0,2,1) menang dari .pesan */
.pesan { color: orange; }        /* (0,1,0) kalah walau ditulis belakangan */`,
   task:{q:'Tanpa menghapus aturan yang ada, buat paragraf berwarna merah <code>rgb(255, 0, 0)</code> dengan selector id.',test:`getComputedStyle(document.querySelector('p')).color==='rgb(255, 0, 0)'`,hint:'#info { color: red; } punya specificity (1,0,0).'},
   pts:['Urutan penentuan: !important, specificity, lalu urutan tulis.','Specificity (id, class, elemen) dibandingkan dari kiri.','Inline style sangat kuat; hindari !important.'],
   q:[['Mana yang menang: #menu a atau .nav .menu a?',['#menu a (1,0,1)','.nav .menu a (0,2,1)','Yang ditulis terakhir'],0,'Satu id mengalahkan berapa pun class.']]}
 ]},
{t:'Box model & ukuran',lvl:'Pemula',d:'Setiap elemen adalah kotak: isi, padding, border, dan margin. Pahami unit ukuran.',
 nodes:['Box Model','Width and Height','Margin','Padding','Border','Outline','CSS Units','Absolute vs. Relative Units','Units with Functions','CSS Functions'],
 lessons:[
  {k:'w',t:'Box model',nodes:['Box Model','Margin','Padding','Border','Outline','Width and Height'],viz:'boxmodel',
   b:['Setiap elemen digambar sebagai kotak berlapis: <b>content</b> (isi), <b>padding</b> (jarak di dalam), <b>border</b> (garis tepi), dan <b>margin</b> (jarak ke elemen lain).',
      'Secara bawaan, <code>width</code> hanya mengukur isi, jadi padding dan border menambah lebar total. Dengan <code>box-sizing: border-box</code>, width sudah termasuk padding dan border. Hampir semua proyek modern memasang <code>*{box-sizing:border-box}</code>.',
      'Margin vertikal dua blok yang bersebelahan bisa <b>runtuh</b> (collapse) menjadi satu, diambil yang terbesar. <code>outline</code> mirip border tapi tidak memakan ruang, sering dipakai untuk penanda fokus.'],
   html:`<div class="kotak a">content-box: lebar 200 + padding + border</div>
<div class="kotak b">border-box: lebar tepat 200</div>`,
   css:`.kotak { width: 200px; padding: 20px; border: 6px solid #2E5E8C; margin: 12px 0; background: #E9EFF5; font: 13px sans-serif; }
.a { box-sizing: content-box; }
.b { box-sizing: border-box; }`,
   task:{q:'Ubah kotak <code>.a</code> agar lebar totalnya juga tepat 200px.',test:`document.querySelector('.a').getBoundingClientRect().width===200`,hint:'Ganti box-sizing .a menjadi border-box.'},
   pts:['Lapisan kotak: content, padding, border, margin.','border-box: width sudah termasuk padding dan border.','Margin vertikal bisa runtuh.','outline tidak memakan ruang.'],
   q:[['width 200px, padding 20px, border 5px, content-box. Lebar total?',['250px','200px','225px'],0,'200 + 2×20 + 2×5 = 250.'],
      ['Yang memberi jarak di dalam border?',['padding','margin','outline'],0,'Padding ada di antara isi dan border.']]},
  {k:'w',t:'Unit ukuran',nodes:['CSS Units','Absolute vs. Relative Units','Units with Functions','CSS Functions'],
   b:['<b>px</b> adalah unit absolut. Unit relatif menyesuaikan konteks: <code>%</code> (persen dari induk), <code>em</code> (dari ukuran huruf elemen itu), <code>rem</code> (dari ukuran huruf root, biasanya 16px), <code>vw</code>/<code>vh</code> (persen lebar/tinggi layar), dan <code>ch</code> (lebar karakter "0").',
      'Pakai <b>rem</b> untuk ukuran huruf agar menghormati pengaturan ukuran huruf pengguna. Fungsi <code>calc()</code> mencampur unit (<code>calc(100% - 2rem)</code>), <code>min()</code>/<code>max()</code> memilih nilai, dan <code>clamp(min, ideal, max)</code> membuat ukuran fleksibel dengan batas.'],
   html:`<div class="wadah">
  <h2>Judul fleksibel</h2>
  <p class="baca">Paragraf ini dibatasi sekitar 45 karakter per baris agar nyaman dibaca, apa pun lebar layarnya.</p>
  <div class="bar"></div>
</div>`,
   css:`html { font-size: 16px; }
h2 { font-size: clamp(1.25rem, 4vw, 2.5rem); }
.baca { max-width: 45ch; font-size: 1rem; }
.bar { width: calc(100% - 2rem); height: .5rem; background: #2F7A52; border-radius: 1em; }`,
   pts:['rem untuk ukuran huruf, menghormati pengaturan pengguna.','% dan vw untuk lebar fleksibel.','calc() mencampur unit, clamp() membatasi ukuran fleksibel.','ch cocok untuk membatasi panjang baris.'],
   q:[['1.5rem bila root 16px?',['24px','16px','1.5px'],0,'1.5 × 16 = 24.'],
      ['clamp(1rem, 4vw, 2rem) berarti?',['4vw, tapi tidak kurang dari 1rem dan tidak lebih dari 2rem','Selalu 4vw','Rata-rata ketiganya'],0,'clamp menjaga nilai di antara batas bawah dan atas.']]}
 ]},
{t:'Warna, latar & tipografi',lvl:'Pemula',d:'Menulis warna, latar, gradien, bayangan, dan mengatur huruf yang nyaman dibaca.',
 nodes:['Color','Named Colors','Hex Colors','RGB Colors in CSS','rgba and hsla Colors','HSL Colors','Background','Background Color','Background Image','Background Gradient','Background Position','Background Attachment','Box Shadows','Opacity','Text Styling','Font Families','Font Size','Font Weight','Font Style','Font Variant','Font Shorthand','Line Height','Text Alignment','Text Decoration','Text Transform','Text Spacing','Text Shadows','Google Fonts'],
 lessons:[
  {k:'w',t:'Warna & latar',nodes:['Color','Named Colors','Hex Colors','RGB Colors in CSS','rgba and hsla Colors','HSL Colors','Background','Background Gradient','Box Shadows','Opacity'],
   b:['Warna bisa ditulis dengan nama (<code>tomato</code>), hex (<code>#B4532A</code>), <code>rgb(180 83 42)</code>, atau <code>hsl(18 62% 44%)</code>. HSL paling mudah diatur manusia: hue (0–360 derajat roda warna), saturation, lightness. Tambahkan alpha untuk transparansi: <code>rgb(0 0 0 / 50%)</code>.',
      'Properti <code>background</code> bisa berisi warna, gambar, atau gradien seperti <code>linear-gradient(135deg, #B4532A, #2E5E8C)</code>. <code>box-shadow</code> memberi bayangan dan <code>opacity</code> membuat seluruh elemen transparan.',
      'Pastikan kontras teks dengan latar cukup: minimal 4.5:1 untuk teks biasa.'],
   html:`<div class="kartu">
  <h3>Promo Oktober</h3>
  <p>Diskon 20% semua kopi.</p>
</div>
<div class="label">hsl(18 62% 44%)</div>`,
   css:`.kartu {
  background: linear-gradient(135deg, hsl(18 62% 44%), hsl(208 50% 36%));
  color: white;
  padding: 16px 20px;
  border-radius: 14px;
  box-shadow: 0 10px 24px rgb(0 0 0 / 25%);
  font-family: sans-serif;
}
.label { margin-top: 12px; display: inline-block; padding: 4px 10px; border-radius: 99px; background: hsl(18 62% 44% / 15%); color: hsl(18 62% 34%); font: 12px monospace; }`,
   task:{q:'Ubah sudut gradien kartu menjadi <code>90deg</code>.',test:`getComputedStyle(document.querySelector('.kartu')).backgroundImage.includes('90deg')`,hint:'linear-gradient(90deg, ...)'},
   pts:['Hex, rgb, dan hsl menulis warna yang sama dengan cara berbeda.','HSL mudah diubah: geser lightness untuk versi terang/gelap.','Gradien ditulis di background-image.','Kontras teks minimal 4.5:1.'],
   q:[['Pada hsl(), angka pertama menyatakan?',['Hue (sudut warna)','Kecerahan','Transparansi'],0,'Hue 0–360 derajat pada roda warna.']]},
  {k:'w',t:'Tipografi',nodes:['Text Styling','Font Families','Font Size','Font Weight','Font Style','Font Shorthand','Line Height','Text Alignment','Text Decoration','Text Transform','Text Spacing','Text Shadows','Google Fonts'],
   b:['<code>font-family</code> berisi daftar huruf cadangan: <code>font-family: "Inter", system-ui, sans-serif</code>. Jika Inter gagal dimuat, browser memakai berikutnya. Google Fonts menyediakan ratusan huruf gratis lewat tag link.',
      'Untuk keterbacaan: ukuran dasar 16px atau lebih, <code>line-height</code> 1.5–1.7 untuk paragraf, dan panjang baris 45–75 karakter. Tebal diatur <code>font-weight</code> (400 normal, 600 semi tebal, 700 tebal).',
      'Properti teks lain: <code>text-align</code>, <code>text-decoration</code>, <code>text-transform: uppercase</code>, <code>letter-spacing</code>, dan <code>text-shadow</code>.'],
   html:`<p class="eyebrow">Cerita kopi</p>
<h1>Dari kebun Gayo ke cangkirmu</h1>
<p class="isi">Kopi Gayo tumbuh di ketinggian 1.200 meter di Aceh Tengah. Petani memetik buah merah satu per satu, lalu mengolahnya dengan proses giling basah yang membuat rasanya bersih dan seimbang.</p>`,
   css:`body { font-family: system-ui, sans-serif; color: #1C1B19; }
.eyebrow { text-transform: uppercase; letter-spacing: .12em; font-size: .75rem; font-weight: 600; color: #6E6B64; }
h1 { font: 400 2rem/1.1 Georgia, serif; margin: .2em 0 .5em; }
.isi { font-size: 1rem; line-height: 1.7; max-width: 60ch; }`,
   task:{q:'Ubah line-height paragraf <code>.isi</code> menjadi <code>2</code>.',test:`parseFloat(getComputedStyle(document.querySelector('.isi')).lineHeight)/parseFloat(getComputedStyle(document.querySelector('.isi')).fontSize)===2`,hint:'.isi { line-height: 2; }'},
   pts:['Selalu tulis font cadangan di font-family.','Paragraf nyaman: 16px+, line-height 1.5–1.7, 45–75 karakter.','Shorthand font: gaya tebal ukuran/line-height keluarga.'],
   q:[['Line-height paragraf yang nyaman?',['1.5–1.7','0.8','3'],0,'Ruang antarbaris membantu mata pindah baris.']]}
 ]},
{t:'Display & posisi',lvl:'Menengah',d:'Bagaimana elemen mengalir di halaman, cara memindahkannya, dan lapisan tumpukan.',
 nodes:['Display','Block Display','Inline Display','Inline-Block','Display: None','Visibility','Flow Layout','Position','Static Positioning','Relative Positioning','Absolute Positioning','Fixed Positioning','Sticky Positioning','Z-Index and Stacking Context','Floating Elements'],
 lessons:[
  {k:'w',t:'Display & alur normal',nodes:['Display','Block Display','Inline Display','Inline-Block','Display: None','Visibility','Flow Layout','Floating Elements'],
   b:['Dalam <b>alur normal</b>, elemen <b>block</b> (div, p, h1) mengambil satu baris penuh dan tersusun ke bawah, sedangkan elemen <b>inline</b> (span, a, strong) mengalir di dalam baris seperti kata. Elemen inline tidak bisa diberi width/height.',
      '<code>inline-block</code> mengalir seperti inline tapi bisa diberi ukuran. <code>display: none</code> menghapus elemen dari tata letak, sedangkan <code>visibility: hidden</code> menyembunyikan tapi tetap memakan ruang.',
      '<code>float</code> dulu dipakai untuk tata letak, kini hanya untuk membuat teks mengalir di sekitar gambar. Untuk tata letak, pakai flexbox atau grid.'],
   html:`<div class="blok">blok 1</div><div class="blok">blok 2</div>
<p>Teks dengan <span class="in">inline</span> dan <span class="ib">inline-block</span> di dalam baris.</p>
<p>Kotak <span class="hilang">A</span> display none, kotak <span class="sembunyi">B</span> visibility hidden.</p>`,
   css:`.blok{background:#E9EFF5;margin:4px 0;padding:4px}
.in{background:#FBE7A8;width:200px}
.ib{display:inline-block;width:120px;background:#E7F2EB;text-align:center}
.hilang{display:none}.sembunyi{visibility:hidden;background:#ccc}`,
   pts:['block satu baris penuh, inline mengalir dalam baris.','inline-block: dalam baris tapi bisa diberi ukuran.','display:none menghapus, visibility:hidden menyisakan ruang.'],
   q:[['Elemen yang tetap memakan ruang walau tak terlihat?',['visibility: hidden','display: none','opacity tidak berpengaruh'],0,'Ruangnya tetap ada.']]},
  {k:'w',t:'Position & z-index',nodes:['Position','Static Positioning','Relative Positioning','Absolute Positioning','Fixed Positioning','Sticky Positioning','Z-Index and Stacking Context'],
   b:['<code>position</code> menentukan cara elemen ditempatkan. <b>static</b> (bawaan) mengikuti alur. <b>relative</b> bergeser dari posisi aslinya dan menjadi patokan bagi anak absolute. <b>absolute</b> keluar dari alur dan diposisikan terhadap leluhur terdekat yang non-static.',
      '<b>fixed</b> menempel pada layar (misalnya tombol chat), <b>sticky</b> mengikuti alur lalu menempel saat digulir (misalnya header tabel).',
      '<code>z-index</code> mengatur elemen mana di atas, tapi hanya berlaku di dalam <b>stacking context</b> yang sama. Elemen dengan opacity kurang dari 1, transform, atau position + z-index membuat stacking context baru.'],
   html:`<div class="kartu">
  <span class="badge">BARU</span>
  <h3>Madu Hutan</h3>
  <p>Gulir panel ini untuk melihat sticky.</p>
  <div class="gulir"><div class="judul">Ulasan</div><p>Enak!</p><p>Kental.</p><p>Asli.</p><p>Mantap.</p></div>
</div>`,
   css:`.kartu{position:relative;border:1px solid #ddd;border-radius:12px;padding:12px;font:14px sans-serif;width:260px}
.badge{position:absolute;top:-10px;right:12px;background:#B23A2E;color:#fff;font-size:11px;padding:2px 8px;border-radius:99px}
.gulir{height:90px;overflow:auto;border:1px solid #eee}
.judul{position:sticky;top:0;background:#F2F1EC;font-weight:600;padding:2px 6px}`,
   task:{q:'Pindahkan badge ke pojok kiri atas kartu (gunakan <code>left</code>).',test:`(()=>{const b=document.querySelector('.badge').getBoundingClientRect(),k=document.querySelector('.kartu').getBoundingClientRect();return b.left-k.left<40})()`,hint:'Ganti right:12px menjadi left:12px.'},
   pts:['relative menjadi patokan anak absolute.','absolute keluar dari alur normal.','fixed menempel di layar, sticky menempel saat digulir.','z-index hanya bersaing di stacking context yang sama.'],
   q:[['Absolute diposisikan terhadap?',['Leluhur terdekat yang non-static','Selalu body','Elemen sebelumnya'],0,'Biasanya induk diberi position: relative.']]}
 ]},
{t:'Flexbox & Grid',lvl:'Menengah',d:'Dua alat tata letak modern: flexbox untuk satu arah, grid untuk dua arah.',
 nodes:['Flexbox','Grid Layout','Multicolumn Layout'],
 lessons:[
  {k:'w',t:'Flexbox',nodes:['Flexbox'],viz:'flexbox',
   b:['Flexbox menata elemen dalam <b>satu arah</b>: baris atau kolom. Pasang <code>display: flex</code> pada induk; anak-anaknya menjadi flex item.',
      '<code>justify-content</code> mengatur posisi di sumbu utama (start, center, space-between), <code>align-items</code> di sumbu silang, <code>gap</code> memberi jarak, dan <code>flex-wrap: wrap</code> mengizinkan pindah baris.',
      'Pada item, <code>flex: 1</code> berarti "ambil sisa ruang". Mainkan pengatur di visual, lalu coba di editor.'],
   html:`<nav class="bar">
  <strong>Toko Nusantara</strong>
  <div class="menu"><a href="#">Produk</a><a href="#">Promo</a><a href="#">Kontak</a></div>
  <button>Keranjang (2)</button>
</nav>`,
   css:`.bar { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 10px 14px; background: #F2F1EC; border-radius: 12px; font: 14px sans-serif; flex-wrap: wrap; }
.menu { display: flex; gap: 12px; }
.menu a { color: #1C1B19; }`,
   task:{q:'Buat menu link tersusun vertikal (kolom).',test:`getComputedStyle(document.querySelector('.menu')).flexDirection==='column'`,hint:'.menu { flex-direction: column; }'},
   pts:['display:flex pada induk.','justify-content = sumbu utama, align-items = sumbu silang.','gap untuk jarak, flex-wrap untuk pindah baris.','flex:1 mengambil sisa ruang.'],
   q:[['Menaruh item tepat di tengah horizontal dan vertikal?',['justify-content:center; align-items:center','text-align:center saja','margin:auto pada induk'],0,'Keduanya untuk dua sumbu.']]},
  {k:'w',t:'Grid',nodes:['Grid Layout','Multicolumn Layout'],viz:'grid',
   b:['Grid menata dalam <b>dua arah</b> sekaligus: baris dan kolom. <code>grid-template-columns: repeat(3, 1fr)</code> membuat tiga kolom sama lebar; <code>fr</code> berarti bagian dari sisa ruang.',
      'Pola paling berguna untuk kartu produk: <code>repeat(auto-fill, minmax(160px, 1fr))</code>. Kolom otomatis bertambah atau berkurang sesuai lebar layar, tanpa media query.',
      'Item bisa membentang dengan <code>grid-column: span 2</code>, atau ditempatkan dengan nama area lewat <code>grid-template-areas</code>.'],
   html:`<div class="galeri">
  <div class="besar">Kopi Gayo</div><div>Teh Melati</div><div>Keripik</div>
  <div>Mete</div><div>Sambal</div><div>Madu</div>
</div>`,
   css:`.galeri { display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 10px; font: 13px sans-serif; }
.galeri div { background: #E9EFF5; border-radius: 10px; padding: 18px 10px; text-align: center; }
.galeri .besar { grid-column: span 2; background: #F6ECE5; }`,
   task:{q:'Buat kotak "Kopi Gayo" juga membentang 2 baris.',test:`getComputedStyle(document.querySelector('.besar')).gridRowEnd.includes('span 2')`,hint:'.besar { grid-row: span 2; }'},
   pts:['Grid untuk dua arah, flexbox untuk satu arah.','fr = bagian dari sisa ruang.','repeat(auto-fill, minmax(…, 1fr)) membuat galeri responsif.','span membentangkan item.'],
   q:[['Unit grid untuk "bagian dari sisa ruang"?',['fr','%','px'],0,'fr = fraction.']]}
 ]},
{t:'Responsif',lvl:'Menengah',d:'Satu situs yang nyaman di ponsel, tablet, dan desktop.',
 nodes:['Media Queries','Container Queries','Responsive Typography','Images and Filters'],
 lessons:[
  {k:'w',t:'Media query & mobile-first',nodes:['Media Queries','Responsive Typography'],
   b:['Mayoritas pengguna internet Indonesia membuka situs dari ponsel. Pendekatan <b>mobile-first</b>: tulis gaya untuk layar kecil dulu, lalu tambahkan <code>@media (min-width: 640px) { ... }</code> untuk layar yang lebih lebar.',
      'Media query juga bisa memeriksa preferensi pengguna: <code>prefers-color-scheme: dark</code> untuk mode gelap dan <code>prefers-reduced-motion</code> untuk mengurangi animasi.',
      'Ubah lebar pratinjau dengan tombol di atasnya untuk melihat tata letak berubah.'],
   html:`<div class="tata"><aside>Filter</aside><main>Daftar produk</main></div>`,
   css:`.tata { display: grid; gap: 10px; font: 14px sans-serif; }
.tata > * { background: #E9EFF5; padding: 14px; border-radius: 10px; }
/* layar lebar: dua kolom */
@media (min-width: 480px) {
  .tata { grid-template-columns: 140px 1fr; }
}
@media (prefers-color-scheme: dark) {
  .tata > * { background: #1A2330; color: #ECEAE4; }
}`,
   pts:['Mobile-first: gaya dasar untuk ponsel, min-width untuk layar lebar.','Media query bisa memeriksa tema gelap dan preferensi animasi.','Selalu pasang meta viewport di HTML.'],
   q:[['Mobile-first memakai media query?',['min-width','max-width','orientation saja'],0,'Gaya bertambah saat layar melebar.']]},
  {k:'w',t:'Container query',nodes:['Container Queries','Images and Filters'],
   b:['Media query melihat lebar <b>layar</b>. Container query melihat lebar <b>wadah</b> komponen, sehingga kartu yang sama bisa tampil berbeda di sidebar sempit dan di area utama yang lebar.',
      'Tandai wadah dengan <code>container-type: inline-size</code>, lalu tulis <code>@container (min-width: 300px) { ... }</code>. Gambar responsif cukup diberi <code>max-width: 100%</code> dan <code>height: auto</code>; <code>object-fit: cover</code> memotong gambar agar pas tanpa gepeng.'],
   html:`<div class="sempit wadah"><div class="kartu"><div class="img"></div><p>Kopi Gayo<br><b>Rp85.000</b></p></div></div>
<div class="lebar wadah"><div class="kartu"><div class="img"></div><p>Kopi Gayo<br><b>Rp85.000</b></p></div></div>`,
   css:`.wadah { container-type: inline-size; margin-bottom: 10px; font: 13px sans-serif; }
.sempit { width: 180px; } .lebar { width: 100%; max-width: 420px; }
.kartu { display: grid; gap: 8px; border: 1px solid #ddd; border-radius: 10px; padding: 8px; }
.img { background: linear-gradient(135deg,#B4532A,#2E5E8C); aspect-ratio: 16/9; border-radius: 6px; }
@container (min-width: 300px) {
  .kartu { grid-template-columns: 120px 1fr; align-items: center; }
}`,
   pts:['Container query melihat lebar wadah, bukan layar.','container-type: inline-size menandai wadah.','max-width:100% dan object-fit menjaga gambar tetap rapi.'],
   q:[['Kapan container query lebih cocok dari media query?',['Komponen dipakai di wadah berbeda lebar','Untuk mode gelap','Untuk mencetak'],0,'Komponen menyesuaikan tempatnya.']]}
 ]},
{t:'Selector lanjutan, transisi & animasi',lvl:'Lanjutan',d:'Combinator, pseudo-class, pseudo-element, transform, transisi, dan keyframes.',
 nodes:['Combinator Selectors','Descendant Combinator','Child Combinator','Next Sibling Combinator','Subsequent Sibling Combinator','Attribute Selectors','Pseudo-Classes','Pseudo-Elements','Transforms','Transitions','Keyframe Animations','Lists','Tables','Direction'],
 lessons:[
  {k:'w',t:'Combinator & pseudo',nodes:['Combinator Selectors','Descendant Combinator','Child Combinator','Next Sibling Combinator','Subsequent Sibling Combinator','Attribute Selectors','Pseudo-Classes','Pseudo-Elements'],
   b:['Combinator memilih berdasarkan hubungan: <code>nav a</code> (keturunan), <code>ul &gt; li</code> (anak langsung), <code>h2 + p</code> (saudara tepat setelahnya), <code>h2 ~ p</code> (semua saudara setelahnya). Selector atribut: <code>a[href^="https"]</code>, <code>input[type="email"]</code>.',
      '<b>Pseudo-class</b> memilih keadaan: <code>:hover</code>, <code>:focus-visible</code>, <code>:checked</code>, <code>:nth-child(2n)</code>, <code>:not(.aktif)</code>, <code>:has(img)</code>. <b>Pseudo-element</b> menata bagian elemen: <code>::before</code>, <code>::after</code>, <code>::first-letter</code>, <code>::placeholder</code>.'],
   html:`<ul class="daftar">
  <li>Kopi Gayo</li><li class="habis">Rendang Kaleng</li><li>Teh Melati</li><li>Keripik</li>
</ul>
<a href="https://roadmap.sh">Tautan luar</a> · <a href="#bawah">Tautan dalam</a>`,
   css:`.daftar > li { padding: 6px; font: 14px sans-serif; }
.daftar > li:nth-child(even) { background: #F2F1EC; }
.daftar li:not(.habis):hover { background: #FBE7A8; }
.habis::after { content: " (habis)"; color: #B23A2E; font-size: 12px; }
a[href^="https"]::after { content: " ↗"; }`,
   task:{q:'Buat baris pertama daftar bercetak tebal memakai <code>:first-child</code>.',test:`getComputedStyle(document.querySelector('.daftar li')).fontWeight>=600`,hint:'.daftar > li:first-child { font-weight: 700; }'},
   pts:['spasi = keturunan, > = anak langsung, + = saudara berikutnya, ~ = semua saudara berikutnya.','Pseudo-class untuk keadaan, pseudo-element untuk bagian.',':has() memilih induk berdasarkan isinya.'],
   q:[['Selector untuk baris genap?',[':nth-child(even)',':even',':nth(2)'],0,'Atau :nth-child(2n).']]},
  {k:'w',t:'Transform, transisi & animasi',nodes:['Transforms','Transitions','Keyframe Animations'],
   b:['<code>transform</code> menggeser (<code>translate</code>), memutar (<code>rotate</code>), dan mengubah skala (<code>scale</code>) tanpa mengganggu tata letak elemen lain.',
      '<code>transition</code> menghaluskan perubahan nilai, misalnya saat hover: <code>transition: transform .2s ease</code>. <code>@keyframes</code> membuat animasi bertahap yang bisa berulang.',
      'Animasikan <code>transform</code> dan <code>opacity</code> saja bila bisa, karena paling ringan untuk browser. Hormati <code>prefers-reduced-motion</code>.'],
   html:`<button class="tombol">Arahkan kursor</button>
<div class="loader" aria-label="Memuat"></div>`,
   css:`.tombol { padding: 10px 18px; border: 0; border-radius: 99px; background: #1C1B19; color: #fff; transition: transform .2s ease, box-shadow .2s; }
.tombol:hover { transform: translateY(-3px) scale(1.04); box-shadow: 0 8px 18px rgb(0 0 0 / 25%); }
.loader { width: 28px; height: 28px; margin-top: 16px; border: 3px solid #ddd; border-top-color: #2E5E8C; border-radius: 50%; animation: putar 1s linear infinite; }
@keyframes putar { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .loader { animation-duration: 3s; } }`,
   pts:['transform tidak menggeser elemen lain.','transition untuk perubahan halus, keyframes untuk animasi bertahap.','Animasikan transform dan opacity.','Hormati prefers-reduced-motion.'],
   q:[['Properti yang paling ringan dianimasikan?',['transform dan opacity','width dan height','margin'],0,'Keduanya tidak memicu hitung ulang tata letak.']]}
 ]},
{t:'Arsitektur CSS & alat',lvl:'Lanjutan',d:'Variabel, penamaan BEM, preprocessor, CSS modules, dan performa.',
 nodes:['CSS Variables','BEM','Sass','PostCSS','CSS Modules','CSS-in-JS','Performance','Accessibility'],
 lessons:[
  {k:'w',t:'Variabel CSS & tema',nodes:['CSS Variables'],
   b:['<b>Custom property</b> (variabel CSS) ditulis <code>--nama: nilai</code> dan dipakai dengan <code>var(--nama)</code>. Berbeda dengan variabel Sass, variabel CSS hidup di browser: bisa diubah oleh media query, oleh class, atau oleh JavaScript.',
      'Ini dasar dari tema terang-gelap dan design token. Tulis semua warna di <code>:root</code>, lalu ganti nilainya untuk tema gelap.'],
   html:`<div class="kartu"><h3>Mode tema</h3><p>Klik tombol untuk ganti tema.</p>
<button onclick="document.documentElement.classList.toggle('gelap')">Ganti tema</button></div>`,
   css:`:root { --bg: #FAFAF7; --teks: #1C1B19; --aksen: #B4532A; --radius: 12px; }
:root.gelap { --bg: #181816; --teks: #ECEAE4; --aksen: #E39A73; }
body { background: var(--bg); color: var(--teks); font-family: sans-serif; transition: background .3s; }
.kartu { border: 2px solid var(--aksen); border-radius: var(--radius); padding: 12px 16px; }
button { background: var(--aksen); color: var(--bg); border: 0; padding: 6px 14px; border-radius: 99px; }`,
   task:{q:'Ganti <code>--radius</code> menjadi <code>0px</code> agar kartu bersudut tajam.',test:`getComputedStyle(document.querySelector('.kartu')).borderTopLeftRadius==='0px'`,hint:':root { --radius: 0px; }'},
   pts:['--nama untuk mendefinisikan, var(--nama) untuk memakai.','Variabel CSS bisa diubah saat halaman berjalan.','Dasar tema gelap dan design token.'],
   q:[['Cara memakai variabel --aksen?',['var(--aksen)','$aksen','@aksen'],0,'Fungsi var() membaca custom property.']]},
  {k:'c',t:'BEM, Sass, CSS Modules & performa',nodes:['BEM','Sass','PostCSS','CSS Modules','CSS-in-JS','Performance'],lang:'scss',run:false,
   b:['Di proyek besar, nama class mudah bentrok. <b>BEM</b> (Block__Element--Modifier) memberi aturan penamaan: <code>.kartu</code>, <code>.kartu__judul</code>, <code>.kartu--promo</code>. Specificity tetap rendah dan maksud setiap class jelas.',
      '<b>Sass</b> menambah fitur seperti nesting, mixin, dan fungsi, lalu dikompilasi menjadi CSS biasa. <b>PostCSS</b> memproses CSS dengan plugin, misalnya menambahkan prefix browser otomatis. <b>CSS Modules</b> dan <b>CSS-in-JS</b> membuat nama class unik per komponen secara otomatis.',
      'Untuk performa: kirim CSS sekecil mungkin, hapus aturan yang tidak dipakai, dan muat CSS kritis lebih awal karena CSS menghambat tampilnya halaman.'],
   code:`// Sass dengan penamaan BEM
$aksen: #B4532A;

@mixin kartu-dasar {
  border-radius: 12px;
  padding: 16px;
}

.kartu {
  @include kartu-dasar;
  border: 1px solid #ddd;

  &__judul { font-weight: 600; }        // .kartu__judul
  &--promo { border-color: $aksen; }    // .kartu--promo
}`,
   pts:['BEM: blok__elemen--modifier.','Sass dikompilasi menjadi CSS biasa.','CSS Modules membuat nama class unik otomatis.','CSS menghambat tampil halaman: jaga tetap ramping.'],
   q:[['Dalam BEM, .tombol--besar adalah?',['Modifier dari blok tombol','Elemen anak tombol','Blok baru'],0,'Dua tanda hubung untuk modifier.']]}
 ]},
{t:'Proyek akhir CSS',lvl:'Lanjutan',d:'Tata halaman landing responsif dengan tema terang-gelap.',nodes:[],
 lessons:[
  {k:'proj',t:'Landing page toko responsif',stack:'HTML + CSS',
   brief:'Tata ulang halaman produk Toko Nusantara menjadi landing page yang rapi di ponsel dan desktop, dengan tema terang-gelap memakai variabel CSS.',
   feats:['Variabel CSS untuk warna, radius, dan jarak di :root','Tema gelap otomatis lewat prefers-color-scheme','Header dengan flexbox: logo kiri, menu kanan, pindah baris di ponsel','Galeri produk dengan grid auto-fill minmax','Kartu produk dengan penamaan BEM dan efek hover memakai transform','Tipografi: clamp untuk judul, panjang baris maksimal 65ch','Fokus keyboard terlihat (:focus-visible)','Tidak ada scroll horizontal di lebar 360px'],
   steps:['Tulis HTML semantik terlebih dahulu.','Definisikan variabel di :root, lalu versi gelapnya.','Bangun header (flex) dan galeri (grid).','Uji di 360px, 768px, dan 1280px.'],
   files:[['gaya.css','css',`:root{--bg:#FAFAF7;--teks:#1C1B19;--redup:#6E6B64;--aksen:#B4532A;--kartu:#fff;--garis:#E7E5DF;--r:14px}
@media (prefers-color-scheme:dark){:root{--bg:#111110;--teks:#ECEAE4;--redup:#9C988F;--aksen:#E39A73;--kartu:#181816;--garis:#2A2925}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--teks);font:16px/1.6 system-ui,sans-serif}
.header{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:12px;padding:16px max(16px,4vw);border-bottom:1px solid var(--garis)}
.header__menu{display:flex;gap:16px}
.header__menu a{color:var(--teks);text-decoration:none}
.hero{padding:48px max(16px,4vw)}
.hero__judul{font:400 clamp(2rem,6vw,3.5rem)/1.05 Georgia,serif;max-width:18ch;margin:0}
.hero__teks{color:var(--redup);max-width:65ch}
.galeri{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;padding:0 max(16px,4vw) 48px}
.kartu{background:var(--kartu);border:1px solid var(--garis);border-radius:var(--r);padding:16px;transition:transform .2s,box-shadow .2s}
.kartu:hover{transform:translateY(-4px);box-shadow:0 12px 28px rgb(0 0 0/.12)}
.kartu__harga{color:var(--aksen);font-weight:600}
.kartu--promo{border-color:var(--aksen)}
a:focus-visible,button:focus-visible{outline:3px solid var(--aksen);outline-offset:2px}`],
   ['index.html','html',`<header class="header">
  <strong>Toko Nusantara</strong>
  <nav class="header__menu"><a href="#produk">Produk</a><a href="#kontak">Kontak</a></nav>
</header>
<main>
  <section class="hero">
    <h1 class="hero__judul">Rasa Nusantara, diantar ke rumahmu</h1>
    <p class="hero__teks">Kopi, teh, dan camilan dari petani lokal.</p>
  </section>
  <section class="galeri" id="produk">
    <article class="kartu kartu--promo"><h2>Kopi Gayo</h2><p class="kartu__harga">Rp85.000</p></article>
    <article class="kartu"><h2>Teh Melati</h2><p class="kartu__harga">Rp25.000</p></article>
    <article class="kartu"><h2>Madu Hutan</h2><p class="kartu__harga">Rp120.000</p></article>
  </section>
</main>`]],
   preview:true}
 ]}
];
