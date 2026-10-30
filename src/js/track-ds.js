/* ===================== JALUR DESIGN SYSTEM =====================
   Mengikuti roadmap.sh/design-system: dasar, membuat dari nol atau dari desain yang ada,
   bahasa desain, token, komponen inti, dokumentasi, tooling, dan tata kelola. */
const DS_MODULES=[
{t:'Memahami design system',lvl:'Pemula',d:'Apa itu design system, bedanya dengan pustaka komponen, dan kapan tim membutuhkannya.',
 nodes:['What is a Design System?','Need of Design System','Design System vs Component Library','Component Library','What is Atomic Design','Terminology','Design System Examples'],
 lessons:[
  {k:'c',t:'Design system, pustaka komponen & atomic design',nodes:['What is a Design System?','Design System vs Component Library','What is Atomic Design','Terminology'],lang:'text',run:false,
   b:['<b>Design system</b> adalah satu sumber kebenaran untuk membangun produk: prinsip, bahasa visual, <b>design token</b>, komponen di Figma dan di kode, pedoman penggunaan, serta proses kontribusi. <b>Pustaka komponen</b> hanyalah satu bagiannya, yaitu kode tombol, input, modal, dan seterusnya.',
      '<b>Atomic design</b> (Brad Frost) menyusun antarmuka dari kecil ke besar: <b>atom</b> (label, ikon, input), <b>molekul</b> (kolom pencarian = input + tombol), <b>organisme</b> (header), <b>template</b> (kerangka halaman), dan <b>halaman</b> (template berisi data nyata).',
      'Contoh terbuka yang layak dipelajari: Material Design (Google), Carbon (IBM), Polaris (Shopify), Primer (GitHub), dan Atlassian Design System.'],
   code:`Design system
├─ Prinsip & bahasa desain   "Jelas lebih dulu, baru indah"
├─ Token                     color.action.primary, space.200
├─ Komponen                  Button, TextField, Modal (Figma + kode)
├─ Pola                      Form pendaftaran, empty state
├─ Pedoman                   kapan dipakai, kapan tidak, contoh benar/salah
└─ Tata kelola               kontribusi, versi, changelog`,
   pts:['Design system ⊃ pustaka komponen.','Atom → molekul → organisme → template → halaman.','Pelajari sistem terbuka: Material, Carbon, Polaris, Primer.'],
   q:[['Kolom pencarian (input + tombol) dalam atomic design adalah?',['Molekul','Atom','Template'],0,'Gabungan beberapa atom dengan satu fungsi.'],
      ['Mana yang BUKAN bagian pustaka komponen saja?',['Pedoman tone of voice','Kode tombol','Kode modal'],0,'Tone of voice adalah bagian bahasa desain.']]},
  {k:'c',t:'Kapan tim butuh design system?',nodes:['Need of Design System','Design System Examples'],lang:'text',run:false,
   b:['Tanda-tanda tim butuh design system: ada 14 warna biru yang sedikit berbeda, tiga versi tombol utama, desainer dan developer berdebat soal jarak setiap rilis, dan halaman baru selalu dibuat dari nol.',
      'Manfaatnya: konsistensi, kecepatan membangun fitur, aksesibilitas yang dibangun sekali lalu dipakai di mana-mana, dan bahasa bersama antara desain dan kode.',
      'Biayanya nyata: perlu tim atau waktu khusus untuk merawatnya. Untuk satu produk kecil dengan dua orang, cukup mulai dari token dan beberapa komponen.'],
   code:`Hasil audit visual aplikasi "Celengan"
Warna biru unik         : 14
Ukuran huruf berbeda    : 23
Varian tombol utama     : 6
Radius sudut            : 2px, 4px, 6px, 8px, 10px, 12px
→ target setelah sistem : 1 biru aksi, 7 ukuran huruf, 1 tombol, 3 radius`,
   pts:['Inkonsistensi dan kerja berulang = sinyal butuh sistem.','Manfaat: konsistensi, kecepatan, aksesibilitas.','Mulai kecil: token + komponen paling sering dipakai.'],
   q:[['Langkah awal paling masuk akal untuk tim kecil?',['Token dan beberapa komponen inti','Situs dokumentasi lengkap','Tim design system 10 orang'],0,'Mulai dari yang memberi dampak terbesar.']]}
 ]},
{t:'Membangun dari desain yang ada',lvl:'Menengah',d:'Audit visual, memetakan proses, dan memilih jalur dari nol atau dari produk yang sudah berjalan.',
 nodes:['Making a Design System','Making it from Scratch','Making it from Existing Design','Performing a Visual Audit','Identify Existing Design Process','Existing Design Analysis','Stakeholders Involved in Building','Pilot'],
 lessons:[
  {k:'c',t:'Audit visual & pilot',nodes:['Performing a Visual Audit','Making it from Existing Design','Existing Design Analysis','Pilot','Making it from Scratch','Stakeholders Involved in Building'],lang:'text',run:false,
   b:['<b>Audit visual</b>: kumpulkan tangkapan layar setiap tombol, input, warna, ikon, dan ukuran huruf dari seluruh produk, lalu kelompokkan. Hasilnya bukti konkret untuk meyakinkan pemangku kepentingan.',
      'Dari nol cocok untuk produk baru; dari desain yang ada cocok untuk produk berjalan, karena komponen diambil dari pola yang paling sering dipakai lalu dirapikan.',
      'Jalankan <b>pilot</b> di satu fitur (misalnya halaman profil) sebelum menyebar. Libatkan desainer, developer, PM, penulis UX, dan QA sejak awal.'],
   code:`Rencana 8 minggu
Mg 1-2  audit visual + wawancara 6 desainer & developer
Mg 3-4  token warna, tipografi, jarak; tombol & input
Mg 5-6  pilot di halaman Profil, ukur waktu pengerjaan
Mg 7    dokumentasi + sesi demo
Mg 8    keputusan perluasan`,
   pts:['Audit visual = bukti inkonsistensi.','Dari produk berjalan: rapikan pola yang paling sering muncul.','Pilot di satu fitur sebelum skala penuh.'],
   q:[['Kenapa pilot dijalankan di satu fitur dulu?',['Menguji sistem dengan risiko kecil sebelum diperluas','Agar lebih mahal','Karena aturan Figma'],0,'Masalah ditemukan lebih awal dan murah.']]}
 ]},
{t:'Bahasa desain',lvl:'Menengah',d:'Prinsip, tone of voice, dan pedoman penulisan yang membuat produk terasa satu suara.',
 nodes:['Design Language','Creating Design Language','Design Principles','Vision','Tone of Voice','Writing Guidelines','Microcopy Guidelines','Terminology','Regional Requirements'],
 lessons:[
  {k:'c',t:'Prinsip desain & tone of voice',nodes:['Design Principles','Vision','Tone of Voice','Writing Guidelines','Microcopy Guidelines','Regional Requirements'],lang:'text',run:false,
   b:['Prinsip desain yang berguna membantu memutuskan saat ada dua pilihan bagus. "Sederhana dan indah" terlalu umum; "Tunjukkan total biaya sebelum pengguna berkomitmen" bisa dipakai menolak sebuah desain.',
      '<b>Tone of voice</b> menetapkan cara produk berbicara: sapaan (kamu atau Anda), tingkat formal, dan cara menyampaikan kabar buruk. Nada boleh menyesuaikan situasi, suara tetap sama.',
      'Pedoman <b>microcopy</b>: tombol memakai kata kerja spesifik, pesan error menjelaskan apa yang salah dan cara memperbaikinya, tanpa menyalahkan. Format lokal Indonesia: Rp 1.250.000, 30/10/2026, +62.'],
   code:`Prinsip "Celengan"
1. Uang orang itu serius: tunjukkan angka pasti, jangan kira-kira.
2. Satu langkah, satu keputusan.
3. Bahasa teman, bukan bahasa bank.

Error
✗ "Transaksi gagal. Kode E-402."
✓ "Saldo GoPay kurang Rp 12.000. Isi saldo atau pilih metode lain."`,
   pts:['Prinsip harus bisa dipakai untuk menolak desain.','Suara tetap, nada menyesuaikan situasi.','Error: apa yang salah + cara memperbaiki.'],
   q:[['Prinsip desain mana yang paling bisa dipakai?',['Tampilkan total biaya sebelum pengguna menekan Bayar','Desain harus indah','Pengguna nomor satu'],0,'Spesifik dan bisa diuji.']]}
 ]},
{t:'Design token & fondasi visual',lvl:'Menengah',d:'Warna, tipografi, jarak, dan mode gelap sebagai token yang mengalir dari Figma ke kode.',
 nodes:['Defining Design Tokens','Token','Naming','Color','Functional Colors','Dark Mode','Typography','Readability','Spaces','Sizes','Units','Grid','Breakpoints','Responsiveness','Accessibility'],
 lessons:[
  {k:'c',t:'Token: primitif, semantik, komponen',nodes:['Defining Design Tokens','Token','Naming'],lang:'json',run:false,viz:'tokens',
   b:['<b>Design token</b> adalah keputusan desain yang diberi nama: warna, ukuran huruf, jarak, radius, bayangan, durasi animasi. Token disimpan sekali, lalu diekspor ke CSS, Android, iOS, dan Figma.',
      'Susun tiga lapis. <b>Primitif</b>: nilai mentah (<code>teal.700 = #0F766E</code>). <b>Semantik</b>: peran (<code>color.action.primary → teal.700</code>). <b>Komponen</b>: pemakaian spesifik (<code>button.primary.bg → color.action.primary</code>). Komponen hanya boleh merujuk token semantik atau komponen.',
      'Format pertukaran yang kini dipakai banyak alat adalah spesifikasi <b>DTCG</b> (Design Tokens Community Group), versi stabil 2025.10. Lihat visualisasi: ganti tema dan perhatikan hanya lapis primitif yang berubah.'],
   code:`{
  "teal":  { "700": { "$type": "color", "$value": "#0F766E" },
             "300": { "$type": "color", "$value": "#5EEAD4" } },
  "color": {
    "action": { "primary": { "$value": "{teal.700}" } },
    "text":   { "default": { "$value": "{gray.900}" } }
  },
  "button": {
    "primary": { "bg": { "$value": "{color.action.primary}" } }
  }
}`,
   pts:['Token = keputusan desain bernama.','Primitif → semantik → komponen.','Nama menurut peran: color.text.default, bukan gray900.','Format DTCG untuk pertukaran antar alat.'],
   q:[['Nama token mana yang semantik?',['color.action.primary','blue500','#0F766E'],0,'Menjelaskan peran, bukan nilai.'],
      ['Saat membuat tema gelap, lapis mana yang berubah paling banyak?',['Pemetaan semantik ke primitif','Nama komponen','Kode React'],0,'Peran sama, nilai berbeda.']]},
  {k:'c',t:'Warna fungsional & kontras',nodes:['Color','Functional Colors','Accessibility','Readability'],lang:'text',run:false,viz:'contrast',
   b:['Palet sistem dibagi menjadi warna <b>merek</b>, <b>netral</b> (teks, garis, latar), dan <b>fungsional</b>: sukses, peringatan, bahaya, info. Setiap warna punya skala 50-900 agar tersedia varian untuk latar, garis, dan teks.',
      'WCAG 2.2 AA mensyaratkan kontras teks normal minimal <b>4,5:1</b>, teks besar dan komponen UI minimal <b>3:1</b>. Coba visualisasi: pilih warna teks dan latar, lihat rasionya.',
      'Jangan mengandalkan warna saja. Pesan error memakai ikon dan teks, grafik memakai label atau pola, bukan hanya merah dan hijau.'],
   code:`Pasangan teks / latar             Rasio   AA teks normal
#1C1B19 / #FFFFFF                  17,4    lulus
#0F766E / #FFFFFF                   5,5    lulus
#5EEAD4 / #FFFFFF                   1,6    gagal → pakai untuk dekorasi saja
#B91C1C / #FEF2F2                   5,9    lulus (pesan error)`,
   pts:['Merek, netral, fungsional; skala 50-900.','Kontras AA: 4,5:1 teks normal, 3:1 teks besar & komponen.','Jangan hanya warna untuk menyampaikan makna.'],
   q:[['Teks biasa dengan kontras 3,2:1 terhadap latar?',['Gagal AA untuk teks normal','Lulus AA','Lulus AAA'],0,'Teks normal butuh 4,5:1.']]},
  {k:'c',t:'Skala tipografi & jarak',nodes:['Typography','Readability','Spaces','Sizes','Units','Grid','Breakpoints','Responsiveness'],lang:'css',run:false,viz:'typescale',
   b:['Skala tipografi dibuat dengan rasio, misalnya 1,25 (major third): 16 → 20 → 25 → 31 → 39. Dengan skala, ukuran huruf tidak dipilih acak per layar. Lihat visualisasi dan coba rasio lain.',
      'Teks isi 16px dengan line-height 1,5 dan panjang baris 45-80 karakter. Gunakan <code>rem</code> agar menghormati pengaturan ukuran huruf pengguna.',
      'Jarak memakai skala 4 atau 8: <code>space.100 = 8px</code>, <code>space.200 = 16px</code>, dan seterusnya. Grid 4 kolom di ponsel, 8 di tablet, 12 di desktop; breakpoint umum 600, 1024, 1440.'],
   code:`:root{
  --font-size-100: .8rem;   /* 12.8px keterangan */
  --font-size-200: 1rem;    /* 16px  isi        */
  --font-size-300: 1.25rem; /* 20px            */
  --font-size-400: 1.563rem;/* 25px  judul kecil */
  --font-size-500: 1.953rem;/* 31px  judul      */
  --space-050: .25rem; --space-100: .5rem;
  --space-200: 1rem;   --space-300: 1.5rem; --space-400: 2rem;
}`,
   pts:['Skala tipografi dengan rasio tetap.','Isi 16px, line-height 1,5, 45-80 karakter.','Jarak skala 4/8; ukuran dalam rem.'],
   q:[['Kenapa memakai rem untuk ukuran huruf?',['Mengikuti pengaturan ukuran huruf pengguna','Lebih cepat dirender','Wajib di Figma'],0,'Pengguna yang memperbesar huruf tetap terlayani.']]},
  {k:'w',t:'Mode gelap dengan token CSS',nodes:['Dark Mode','Color'],
   b:['Mode gelap bukan sekadar membalik warna. Latar gelap memakai abu-abu sangat gelap (bukan hitam murni) agar bayangan dan lapisan masih terlihat, dan warna aksen dibuat sedikit lebih terang agar kontras tetap cukup.',
      'Karena komponen hanya merujuk token semantik, tema gelap cukup mendefinisikan ulang token di satu tempat. Tidak ada komponen yang perlu diubah.',
      'Tugas: tambahkan nilai <code>--color-bg</code> untuk tema gelap di blok <code>[data-theme=dark]</code> (sudah disiapkan) lalu tekan tombol Ganti tema di pratinjau.'],
   html:`<div class="kartu">
  <p class="label">Saldo tabungan</p>
  <p class="angka">Rp 2.400.000</p>
  <button class="utama" onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme==='dark' ? '' : 'dark'">Ganti tema</button>
</div>`,
   css:`:root{
  --color-bg:#F6F7F5; --color-surface:#FFFFFF; --color-text:#1C1B19;
  --color-muted:#5B6360; --color-action:#0F766E; --color-on-action:#FFFFFF;
}
[data-theme=dark]{
  --color-surface:#1D201F; --color-text:#ECEDEA;
  --color-muted:#A3AAA6; --color-action:#5EEAD4; --color-on-action:#06201D;
}
body{background:var(--color-bg);color:var(--color-text);font:16px/1.5 system-ui,sans-serif;padding:24px;transition:background .2s}
.kartu{background:var(--color-surface);border-radius:16px;padding:24px;max-width:300px;display:grid;gap:8px}
.label{margin:0;color:var(--color-muted);font-size:14px}
.angka{margin:0;font-size:28px;font-weight:700}
.utama{min-height:44px;border:0;border-radius:12px;background:var(--color-action);color:var(--color-on-action);font:600 16px system-ui}`,
   task:{q:'Lengkapi tema gelap: definisikan --color-bg di blok [data-theme=dark] (misalnya #121413).',test:"(()=>{document.documentElement.dataset.theme='dark';const v=getComputedStyle(document.documentElement).getPropertyValue('--color-bg').trim().toLowerCase();document.documentElement.dataset.theme='';return v!=='#f6f7f5'&&v!==''})()",hint:'Tambahkan --color-bg:#121413; di dalam blok [data-theme=dark].'},
   pts:['Gelap = abu-abu sangat gelap, bukan hitam murni.','Aksen dibuat lebih terang di tema gelap.','Ganti token semantik di satu tempat.'],
   q:[['Kenapa latar mode gelap jarang memakai #000000?',['Bayangan dan lapisan jadi tidak terlihat dan kontras berlebihan','Karena dilarang browser','Agar hemat baterai'],0,'Abu-abu gelap memberi ruang untuk elevasi.']]}
 ]},
{t:'Komponen inti',lvl:'Lanjutan',d:'Membangun tombol, input, dan komponen lain lengkap dengan state, varian, dan aksesibilitas.',
 nodes:['Creating Core Components','Component','Button','Input Text','Input Checkbox','Input Radio','Input Switch','Select','Modal','Toast','Tooltip','Tabs','Card','Badge','Avatar','Loading Indicator','Icon','Accessibility Testing'],
 lessons:[
  {k:'w',t:'Komponen tombol lengkap dengan state',nodes:['Creating Core Components','Button','Component','Loading Indicator','Accessibility'],
   b:['Komponen sistem harus menangani semua <b>state</b>: default, hover, fokus keyboard, ditekan, nonaktif, dan memuat. State yang terlupa adalah sumber bug tampilan paling umum.',
      'Varian (primary, secondary, danger) dan ukuran (sm, md, lg) dibuat lewat kelas atau prop, bukan dengan menyalin komponen. Target sentuh minimal 44px, dan saat memuat tombol diberi <code>aria-busy</code> serta tetap memiliki label yang terbaca.',
      'Tugas: lengkapi state fokus keyboard dengan <code>:focus-visible</code> yang memakai outline 3px, lalu tekan Tab di pratinjau untuk mencobanya.'],
   html:`<div class="baris">
  <button class="btn btn--primary">Simpan</button>
  <button class="btn btn--secondary">Batal</button>
  <button class="btn btn--danger">Hapus akun</button>
  <button class="btn btn--primary" disabled>Nonaktif</button>
  <button class="btn btn--primary" aria-busy="true"><span class="putar" aria-hidden="true"></span>Menyimpan…</button>
</div>`,
   css:`:root{--action:#0F766E;--danger:#B91C1C;--line:#C9CFCC;--r:12px}
body{font:16px/1.5 system-ui,sans-serif;padding:24px}
.baris{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 18px;border-radius:var(--r);border:1px solid transparent;font:600 15px system-ui;cursor:pointer;transition:transform .1s,filter .15s}
.btn--primary{background:var(--action);color:#fff}
.btn--secondary{background:#fff;color:#1C1B19;border-color:var(--line)}
.btn--danger{background:var(--danger);color:#fff}
.btn:hover{filter:brightness(1.08)}
.btn:active{transform:scale(.97)}
.btn:disabled{opacity:.45;cursor:not-allowed;filter:none}
.btn[aria-busy=true]{cursor:progress}
.putar{width:14px;height:14px;border-radius:50%;border:2px solid #fff6;border-top-color:#fff;animation:p .8s linear infinite}
@keyframes p{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.putar{animation-duration:3s}}`,
   task:{q:'Tambahkan aturan .btn:focus-visible dengan outline 3px agar fokus keyboard terlihat.',test:"[...document.styleSheets].some(s=>[...s.cssRules].some(r=>r.selectorText&&r.selectorText.includes(':focus-visible')&&/3px/.test(r.style.outline||r.style.outlineWidth)))",hint:'.btn:focus-visible{outline:3px solid #1C1B19;outline-offset:2px}'},
   pts:['State: default, hover, focus, active, disabled, loading.','Varian & ukuran lewat kelas/prop.','Target sentuh ≥ 44px; fokus selalu terlihat.'],
   q:[['Kenapa memakai :focus-visible, bukan :focus?',['Outline hanya muncul untuk navigasi keyboard, tidak saat diklik mouse','Lebih cepat','Wajib di Safari'],0,'Pengguna mouse tidak terganggu, pengguna keyboard tetap terbantu.']]},
  {k:'c',t:'Anatomi komponen form & umpan balik',nodes:['Input Text','Input Checkbox','Input Radio','Input Switch','Select','Modal','Toast','Tooltip','Tabs','Card','Badge','Avatar','Icon','Accessibility Testing'],lang:'html',run:false,
   b:['Kolom isian sistem selalu punya <b>label</b> yang terlihat (bukan hanya placeholder), teks bantuan opsional, dan pesan error yang terhubung lewat <code>aria-describedby</code>. Switch dipakai untuk pengaturan yang langsung berlaku; checkbox untuk pilihan yang dikirim bersama form.',
      'Komponen umpan balik dibedakan menurut tingkat gangguan: <b>toast</b> untuk konfirmasi ringan yang hilang sendiri, <b>banner</b> untuk informasi penting di halaman, <b>modal</b> untuk keputusan yang menghentikan alur. Modal harus menjebak fokus di dalamnya dan bisa ditutup dengan Esc.',
      'Setiap komponen diuji aksesibilitasnya: keyboard, pembaca layar, kontras, dan zoom 200%. Alat otomatis seperti axe menemukan sekitar sepertiga masalah; sisanya perlu diuji manual.'],
   code:`<div class="field">
  <label for="nominal">Nominal setoran</label>
  <input id="nominal" inputmode="numeric" aria-describedby="nominal-bantu nominal-err" aria-invalid="true">
  <p id="nominal-bantu" class="bantu">Minimal Rp 10.000</p>
  <p id="nominal-err" class="err">Nominal kurang dari Rp 10.000.</p>
</div>

<dialog id="konfirmasi" aria-labelledby="k-judul">
  <h2 id="k-judul">Hentikan autodebet?</h2>
  <p>Setoran tanggal 25 tidak akan dipotong.</p>
  <button>Hentikan</button> <button autofocus>Batal</button>
</dialog>`,
   pts:['Label terlihat + bantuan + error via aria-describedby.','Toast < banner < modal dalam tingkat gangguan.','Modal: fokus terjebak, Esc menutup.','Uji keyboard, pembaca layar, kontras, zoom.'],
   q:[['Komponen yang tepat untuk "Setoran berhasil disimpan"?',['Toast','Modal','Tooltip'],0,'Konfirmasi ringan tidak perlu menghentikan alur.']]}
 ]},
{t:'Dokumentasi, tooling & tata kelola',lvl:'Profesional',d:'Membuat sistem dipakai dan dirawat: dokumentasi, Storybook, versi, kontribusi, dan metrik.',
 nodes:['Documentation','Usage Guidance','Placement Guidance','Component Catalog','Tooling','Design Editor','Plugins','Version Control','Semantic Versioning','Release Strategy','Contribution Guidelines','Governance','Component Analytics','Communication Channel','Roadmap'],
 lessons:[
  {k:'c',t:'Dokumentasi & katalog komponen',nodes:['Documentation','Usage Guidance','Placement Guidance','Component Catalog','Tooling','Design Editor','Plugins'],lang:'text',run:false,
   b:['Dokumentasi yang dipakai menjawab tiga pertanyaan per komponen: <b>kapan dipakai</b>, <b>kapan tidak</b>, dan <b>bagaimana</b> (props, contoh kode, contoh benar dan salah).',
      '<b>Storybook</b> adalah katalog komponen standar di sisi kode: setiap state dijadikan "story" yang bisa diuji visual dan aksesibilitasnya. Di sisi desain, pustaka Figma dengan variabel dan Code Connect menghubungkan komponen Figma ke kodenya.',
      'Token disinkronkan otomatis dengan alat seperti Tokens Studio atau Style Dictionary agar Figma dan kode tidak pernah berbeda.'],
   code:`Button
Kapan dipakai   : memicu aksi di halaman ini (simpan, bayar)
Kapan tidak     : pindah halaman → pakai Link
Varian          : primary (1 per layar), secondary, danger
Ukuran          : sm 36px, md 44px (default), lg 52px
Aksesibilitas   : label teks wajib; ikon saja → aria-label
✓ "Bayar Rp 128.000"     ✗ "Klik di sini"`,
   pts:['Dokumentasi: kapan, kapan tidak, bagaimana.','Storybook untuk katalog dan uji visual.','Sinkronkan token Figma dan kode otomatis.'],
   q:[['Tombol yang membuka halaman lain sebaiknya diganti dengan?',['Link','Button primary','Toast'],0,'Navigasi memakai elemen link.']]},
  {k:'c',t:'Versi, kontribusi & metrik adopsi',nodes:['Version Control','Semantic Versioning','Release Strategy','Contribution Guidelines','Governance','Component Analytics','Communication Channel','Roadmap'],lang:'text',run:false,
   b:['Rilis memakai <b>semantic versioning</b>: MAJOR.MINOR.PATCH. Perubahan yang merusak pemakai lama (mengganti nama prop) menaikkan MAJOR, fitur baru yang aman menaikkan MINOR, perbaikan bug menaikkan PATCH. Selalu sertakan changelog dan panduan migrasi.',
      'Model tata kelola yang umum: tim inti kecil merawat sistem, tim produk berkontribusi lewat proses jelas (usulan → review desain → review kode → dokumentasi).',
      'Ukur keberhasilan: persentase layar yang memakai komponen sistem, jumlah komponen lokal yang menyalin sistem, waktu membangun fitur, dan jumlah bug aksesibilitas.'],
   code:`CHANGELOG
3.0.0  BREAKING  Button: prop "type" diganti "variant" (lihat migrasi)
2.4.0  feat      TextField: dukungan prefix "Rp"
2.3.1  fix       Modal: fokus kembali ke pemicu saat ditutup

Adopsi kuartal ini
Layar memakai komponen sistem : 64% → 81%
Komponen tombol lokal         : 11 → 3`,
   pts:['SemVer: MAJOR merusak, MINOR fitur, PATCH perbaikan.','Proses kontribusi yang jelas.','Ukur adopsi dan dampaknya.'],
   q:[['Mengganti nama prop yang dipakai banyak tim menaikkan versi?',['MAJOR','MINOR','PATCH'],0,'Perubahan merusak kompatibilitas.']]}
 ]},
{t:'Proyek akhir',lvl:'Profesional',d:'Bangun design system mini dari audit sampai dokumentasi.',nodes:['Project'],
 lessons:[
  {k:'proj',t:'Design system mini "Celengan"',stack:'Figma + CSS + Storybook',
   brief:'Rapikan aplikasi tabungan fiktif yang tumbuh tanpa aturan menjadi design system mini: token tiga lapis, lima komponen inti dengan semua state, mode gelap, dan dokumentasi.',
   feats:['Audit visual dengan jumlah warna, ukuran huruf, dan varian tombol sebelum-sesudah','Token primitif, semantik, komponen dalam format DTCG','Mode gelap hanya dengan mengganti token semantik','Komponen Button, TextField, Checkbox, Modal, Toast dengan semua state','Kontras semua pasangan teks lulus WCAG 2.2 AA','Halaman dokumentasi: kapan dipakai, kapan tidak, contoh benar/salah','Changelog dengan semantic versioning','Pilot di satu layar dan catatan hasilnya'],
   steps:['Audit dan tentukan token.','Bangun komponen di Figma dan CSS.','Uji kontras dan keyboard.','Tulis dokumentasi, rilis v1.0.0.'],
   files:[['tokens.json','json',`{
  "teal": { "700": { "$type": "color", "$value": "#0F766E" }, "300": { "$type": "color", "$value": "#5EEAD4" } },
  "gray": { "50": { "$type": "color", "$value": "#F6F7F5" }, "900": { "$type": "color", "$value": "#1C1B19" } },
  "color": {
    "bg":     { "$value": "{gray.50}" },
    "text":   { "default": { "$value": "{gray.900}" } },
    "action": { "primary": { "$value": "{teal.700}" } }
  },
  "space": { "100": { "$type": "dimension", "$value": "8px" }, "200": { "$type": "dimension", "$value": "16px" } },
  "button": { "primary": { "bg": { "$value": "{color.action.primary}" }, "radius": { "$value": "12px" } } }
}`]]}
 ]}
];
