/* ===================== JALUR UX DESIGN =====================
   Mengikuti roadmap.sh/ux-design: perilaku manusia, model perubahan perilaku,
   memahami produk, riset, desain konseptual, prototyping, dan mengukur dampak. */
const UX_MODULES=[
{t:'Cara manusia mengambil keputusan',lvl:'Pemula',d:'Dasar psikologi yang menjelaskan kenapa pengguna bertindak, ragu, atau pergi.',
 nodes:['Human Decision Making','Behavioral Science','Behavioral Economics','Dual Process Theory','Nudge Theory','Persuasive Technology'],
 lessons:[
  {k:'c',t:'Dua sistem berpikir',nodes:['Human Decision Making','Dual Process Theory'],lang:'text',run:false,
   b:['Psikolog Daniel Kahneman membagi cara berpikir menjadi dua. <b>Sistem 1</b> cepat, otomatis, dan intuitif: mengenali ikon keranjang, menekan tombol berwarna mencolok. <b>Sistem 2</b> lambat dan butuh usaha: membandingkan tiga paket asuransi.',
      'Hampir semua interaksi di aplikasi dijalankan Sistem 1. Pengguna memindai, bukan membaca. Kalau sebuah layar memaksa Sistem 2 bekerja tanpa alasan (istilah teknis, pilihan terlalu banyak, ikon tanpa label) mereka lelah lalu pergi.',
      'Tugas desainer: jadikan langkah rutin bisa dijalankan Sistem 1, dan bangunkan Sistem 2 hanya saat keputusan memang penting, misalnya konfirmasi transfer Rp 5.000.000.'],
   code:`Layar transfer e-wallet

Sistem 1 (otomatis)            Sistem 2 (sadar)
- pilih kontak terakhir        - cek ulang nama penerima
- nominal cepat 50rb/100rb     - baca biaya admin
- tombol "Lanjut" besar        - masukkan PIN

Rancang agar kolom kiri tanpa pikir,
dan kolom kanan cukup jelas untuk diperiksa.`,
   pts:['Sistem 1: cepat, otomatis; Sistem 2: lambat, butuh usaha.','Pengguna memindai, tidak membaca.','Kurangi beban Sistem 2 pada langkah rutin.','Bangunkan Sistem 2 untuk keputusan berisiko.'],
   q:[['Ikon tanpa label pada menu utama membebani?',['Sistem 2, karena pengguna harus menebak','Sistem 1 saja','Tidak membebani apa pun'],0,'Menebak arti ikon butuh usaha sadar.'],
      ['Kapan desain sebaiknya sengaja memperlambat pengguna?',['Sebelum transfer uang besar','Saat membuka beranda','Saat menggulir daftar produk'],0,'Keputusan berisiko layak diperiksa dengan sadar.']]},
  {k:'c',t:'Ekonomi perilaku & nudge',nodes:['Behavioral Economics','Nudge Theory','Persuasive Technology','Behavioral Science'],lang:'text',run:false,
   b:['Ekonomi perilaku menunjukkan manusia tidak selalu rasional. Beberapa bias yang paling sering muncul di produk digital: <b>loss aversion</b> (kehilangan terasa dua kali lebih berat daripada mendapat), <b>default effect</b> (orang cenderung menerima pilihan bawaan), <b>social proof</b> (ikut apa yang dilakukan banyak orang), dan <b>anchoring</b> (angka pertama memengaruhi penilaian berikutnya).',
      '<b>Nudge</b> (Thaler & Sunstein) adalah cara menyusun pilihan agar orang lebih mudah memilih yang baik untuk dirinya, tanpa melarang pilihan lain. Contoh: menabung otomatis aktif secara default, tetapi bisa dimatikan dengan satu ketukan.',
      'Garis tipisnya: nudge membantu pengguna mencapai tujuan <b>mereka</b>. Jika dipakai untuk menjebak (centang otomatis langganan, tombol batal disembunyikan) itu <b>dark pattern</b>, merusak kepercayaan, dan di Indonesia dapat melanggar UU Perlindungan Data Pribadi.'],
   code:`Nudge yang etis                    Dark pattern
- tabungan otomatis 10% (bisa off)  - langganan dicentang otomatis
- "1.240 orang membeli minggu ini"  - "tersisa 1!" yang palsu
- pengingat bayar tagihan H-3       - tombol batal abu-abu kecil
- harga total ditampilkan di awal   - biaya muncul di langkah akhir`,
   pts:['Bias umum: loss aversion, default, social proof, anchoring.','Nudge = arsitektur pilihan, tidak melarang.','Ukuran etis: membantu tujuan pengguna, bukan menjebak.'],
   q:[['Mengaktifkan tabungan otomatis secara default memanfaatkan?',['Default effect','Anchoring','Loss aversion'],0,'Orang cenderung mempertahankan pilihan bawaan.'],
      ['Mana yang termasuk dark pattern?',['Biaya admin baru muncul di langkah pembayaran terakhir','Menampilkan ulasan pembeli','Pengingat jatuh tempo'],0,'Menyembunyikan biaya menyesatkan pengguna.']]}
 ]},
{t:'Model perilaku',lvl:'Pemula',d:'Model Fogg, Hook, dan cue-routine-reward untuk merancang kebiasaan.',
 nodes:["BJ Fogg's Behavior Model","BJ Fogg's Behavior Grid","Nir Eyal's Hook Model",'Cue Routine Reward Model','Make or Change Habits','Behavior Design'],
 lessons:[
  {k:'c',t:'Model perilaku Fogg: B = MAP',nodes:["BJ Fogg's Behavior Model","BJ Fogg's Behavior Grid",'Behavior Design'],lang:'text',run:false,viz:'fogg',
   b:['BJ Fogg dari Stanford merumuskan: perilaku terjadi saat <b>Motivation</b> (motivasi), <b>Ability</b> (kemampuan atau kemudahan), dan <b>Prompt</b> (pemicu) hadir pada saat yang sama. Tanpa pemicu, orang yang termotivasi pun tidak bertindak.',
      'Motivasi naik-turun dan sulit dikendalikan. Kemudahan jauh lebih bisa dirancang: kurangi langkah, waktu, biaya, usaha fisik, usaha berpikir, dan hal yang terasa aneh secara sosial.',
      'Coba visualisasi di atas: geser motivasi dan kemudahan. Titik di atas garis aksi berarti pemicu akan berhasil; di bawahnya, pemicu hanya mengganggu.'],
   code:`Masalah: pengguna tidak melengkapi profil (8 kolom)

Motivasi  : rendah ("untuk apa?")
Kemudahan : rendah (8 kolom, unggah KTP)
Pemicu    : banner di beranda

Perbaikan:
+ motivasi : "Lengkapi profil, dapat ongkir gratis"
+ kemudahan: 3 kolom dulu, sisanya nanti
+ pemicu   : tepat setelah checkout pertama`,
   pts:['B = M A P: motivasi, kemampuan, pemicu sekaligus.','Kemudahan lebih mudah dirancang daripada motivasi.','Pemicu di bawah garis aksi hanya mengganggu.'],
   q:[['Pengguna sangat ingin, tetapi formulir terlalu rumit. Faktor mana yang lemah?',['Ability (kemudahan)','Motivation','Prompt'],0,'Perbaiki dengan mengurangi langkah.'],
      ['Menurut Fogg, apa yang paling mudah diubah desainer?',['Kemudahan','Motivasi','Kepribadian pengguna'],0,'Motivasi berfluktuasi; kemudahan bisa dirancang.']]},
  {k:'c',t:'Hook model & kebiasaan',nodes:["Nir Eyal's Hook Model",'Cue Routine Reward Model','Make or Change Habits'],lang:'text',run:false,viz:'hook',
   b:['Nir Eyal menggambarkan produk pembentuk kebiasaan sebagai siklus empat langkah: <b>Trigger</b> (pemicu eksternal seperti notifikasi, lalu internal seperti rasa bosan), <b>Action</b> (tindakan paling sederhana), <b>Variable reward</b> (hadiah yang tidak selalu sama), dan <b>Investment</b> (pengguna menaruh sesuatu: data, konten, pengikut) yang membuat pemicu berikutnya lebih kuat.',
      'Model Charles Duhigg lebih sederhana: <b>cue → routine → reward</b>. Untuk mengganti kebiasaan buruk, pertahankan cue dan reward, ganti routine-nya.',
      'Pertanyaan etis yang perlu diajukan tim: apakah kebiasaan ini meningkatkan hidup pengguna, dan apakah kami sendiri mau memakainya? Aplikasi belajar bahasa yang membentuk kebiasaan 10 menit sehari berbeda dengan feed tanpa ujung.'],
   code:`Aplikasi belajar 10 menit sehari

Trigger   : notifikasi jam 19.00 → lama-lama "waktunya belajar"
Action    : satu ketukan "Lanjut pelajaran"
Reward    : kuis acak, poin, kadang lencana kejutan
Investment: streak 12 hari, catatan pribadi, kelas yang diikuti`,
   pts:['Hook: trigger, action, variable reward, investment.','Cue-routine-reward: ganti routine untuk ganti kebiasaan.','Uji etis: apakah kebiasaan ini baik untuk pengguna?'],
   q:[['Streak belajar 30 hari termasuk tahap?',['Investment','Trigger','Action'],0,'Pengguna menaruh sesuatu yang sayang ditinggalkan.'],
      ['Kenapa hadiah dibuat bervariasi?',['Ketidakpastian membuat orang penasaran kembali','Agar lebih murah','Agar mudah diukur'],0,'Variable reward memicu rasa ingin tahu.']]}
 ]},
{t:'Strategi perubahan perilaku',lvl:'Menengah',d:'Taktik konkret yang dipakai produk untuk membantu pengguna bertindak.',
 nodes:['Behavior Change Strategies','Make it Easy to Understand and Complete','Default Everything','Lessen the Burden of Action / Info','Make Progress Visible to User','Deploy Social Proof','Leverage Loss Aversion','Reminders / Planning Prompts','Gamification','Goal Trackers','Avoid Choice Overload','Avoid Cognitive Overhead','Make it Clear Where to Act','Call to Action'],
 lessons:[
  {k:'c',t:'Kurangi beban: default, sedikit pilihan, aksi jelas',nodes:['Default Everything','Lessen the Burden of Action / Info','Avoid Choice Overload','Avoid Cognitive Overhead','Make it Clear Where to Act','Call to Action','Make it Easy to Understand and Complete'],lang:'text',run:false,
   b:['<b>Hick\'s law</b>: semakin banyak pilihan, semakin lama orang memutuskan. Tampilkan 3 paket, bukan 9; tandai satu sebagai "paling banyak dipilih".',
      'Isi <b>default</b> yang masuk akal: kota dari riwayat, metode bayar terakhir, jumlah 1. Setiap kolom yang terisi otomatis adalah satu keputusan yang tidak perlu diambil.',
      'Satu layar, satu <b>aksi utama</b>. Tombol utama memakai kata kerja spesifik ("Bayar Rp 128.000", bukan "Kirim"), kontras tinggi, dan berada di zona jempol pada ponsel. Aksi sekunder tampil lebih tenang.'],
   code:`Sebelum                          Sesudah
[Simpan] [Kirim] [Lanjut] [Batal]  Ringkasan pesanan
9 metode pembayaran                 Metode: GoPay (terakhir dipakai) ▸ ubah
Kota: (kosong)                      Kota: Bandung (dari alamat)
                                    [ Bayar Rp 128.000 ]   ← satu aksi utama
                                    Kembali ke keranjang   ← aksi sekunder`,
   pts:['Batasi pilihan; tandai rekomendasi.','Default cerdas mengurangi keputusan.','Satu aksi utama per layar dengan kata kerja spesifik.'],
   q:[['Label tombol mana yang paling baik untuk halaman pembayaran?',['Bayar Rp 128.000','Submit','OK'],0,'Spesifik dan memperjelas akibatnya.'],
      ['Hick\'s law menyarankan?',['Kurangi jumlah pilihan','Perbesar semua tombol','Tambah animasi'],0,'Waktu keputusan naik seiring jumlah pilihan.']]},
  {k:'c',t:'Progres, bukti sosial & pengingat',nodes:['Make Progress Visible to User','Make Progress Meaningful to Reward User','Deploy Social Proof','Leverage Loss Aversion','Reminders / Planning Prompts','Goal Trackers','Gamification','Elicit Implementation Intentions'],lang:'text',run:false,
   b:['Progres yang terlihat mendorong orang menyelesaikan (<b>goal gradient effect</b>): "Langkah 2 dari 3", bilah kelengkapan profil 70%. Mulai dari sedikit terisi (misalnya otomatis 1 dari 5) agar terasa sudah berjalan.',
      '<b>Bukti sosial</b> yang jujur ("4,8 dari 2.310 ulasan", "dipakai 12 kampus") mengurangi ragu. <b>Loss aversion</b> bisa dipakai secara etis: "Streak 14 harimu berakhir malam ini".',
      'Pengingat paling efektif bila pengguna sendiri menentukan kapan dan di mana (<b>implementation intention</b>): "Saya akan belajar setelah makan malam, jam 19.30".'],
   code:`Onboarding aplikasi tabungan

[■■■□□] Langkah 3 dari 5: Pilih target
"68% penabung memilih target Dana Darurat"
Target: Dana Darurat  Rp 6.000.000
Kapan kamu menabung?  [ Setiap gajian, tgl 25 ▾ ]
                      → pengingat dikirim tgl 25 pukul 09.00`,
   pts:['Tampilkan progres; mulai tidak dari nol.','Bukti sosial harus nyata dan spesifik.','Biarkan pengguna menentukan waktu pengingat.'],
   q:[['Menampilkan "Langkah 3 dari 5" memanfaatkan?',['Goal gradient effect','Anchoring','Default effect'],0,'Orang makin termotivasi saat tujuan terlihat dekat.']]}
 ]},
{t:'Memahami produk & bisnis',lvl:'Menengah',d:'Alat strategi untuk menghubungkan masalah pengguna dengan tujuan bisnis.',
 nodes:['Understanding the Product','Business Model Canvas','Lean Canvas','SWOT Analysis','Five Forces Model','Competitor Analysis','Target Outcome','Target Actor','Target Action'],
 lessons:[
  {k:'c',t:'Outcome, aktor, dan aksi',nodes:['Target Outcome','Target Actor','Target Action','Understanding the Product'],lang:'text',run:false,
   b:['Sebelum menggambar layar, tulis tiga hal. <b>Outcome</b>: perubahan nyata yang dicari (pengguna punya dana darurat 3 bulan). <b>Aktor</b>: siapa yang harus berubah (karyawan muda gaji UMR di kota besar). <b>Aksi</b>: perilaku spesifik yang bisa diamati (menyisihkan Rp 300.000 setiap gajian).',
      'Aksi yang baik itu konkret, terukur, dan memang dikuasai pengguna. "Lebih sadar finansial" bukan aksi; "mengaktifkan autodebet di tanggal gajian" adalah aksi.',
      'Hubungkan dengan metrik produk: persentase pengguna baru yang mengaktifkan autodebet dalam 7 hari.'],
   code:`Problem statement
Karyawan muda (aktor) kesulitan menabung rutin (aksi)
karena uang habis sebelum sempat disisihkan,
sehingga tidak punya dana darurat (outcome).

Metrik utama : % pengguna baru aktifkan autodebet ≤ 7 hari
Metrik jaga  : tingkat pembatalan autodebet bulan pertama`,
   pts:['Outcome → aktor → aksi, baru kemudian layar.','Aksi harus konkret dan terukur.','Pasang metrik utama dan metrik penjaga.'],
   q:[['Mana yang merupakan aksi target yang baik?',['Mengaktifkan autodebet Rp300.000 tiap gajian','Menjadi lebih bijak','Menyukai aplikasi'],0,'Konkret dan bisa diamati.']]},
  {k:'c',t:'Kanvas bisnis, SWOT & kompetitor',nodes:['Business Model Canvas','Lean Canvas','SWOT Analysis','Five Forces Model','Competitor Analysis'],lang:'text',run:false,
   b:['<b>Lean Canvas</b> merangkum produk dalam satu halaman: masalah, segmen pelanggan, proposisi nilai unik, solusi, saluran, sumber pendapatan, struktur biaya, metrik kunci, dan keunggulan yang sulit ditiru. Business Model Canvas mirip, lebih cocok untuk bisnis yang sudah berjalan.',
      '<b>SWOT</b> memetakan kekuatan dan kelemahan internal serta peluang dan ancaman eksternal. <b>Five Forces</b> Porter menilai tekanan pasar: pesaing, pendatang baru, produk pengganti, daya tawar pembeli, dan pemasok.',
      '<b>Analisis kompetitor</b> untuk UX: coba alur kunci di 3-5 produk (lokal dan global), catat pola yang dipakai, langkah yang membingungkan, dan celah yang bisa diisi. Ambil pelajaran, jangan menyalin.'],
   code:`Analisis alur "buka tabungan" (jumlah langkah, waktu)
Produk A : 7 langkah, 4 menit, wajib unggah KTP di awal
Produk B : 4 langkah, 2 menit, KTP setelah saldo > Rp 2 juta
Produk C : 5 langkah, 3 menit, target tabungan dipilih di awal

Celah: belum ada yang mengaitkan tabungan dengan tanggal gajian.`,
   pts:['Lean Canvas: satu halaman model bisnis.','SWOT: internal (S, W) dan eksternal (O, T).','Bandingkan alur kunci kompetitor, cari celah.'],
   q:[['Dalam SWOT, regulasi baru yang menyulitkan termasuk?',['Threat','Weakness','Strength'],0,'Faktor eksternal yang merugikan.']]}
 ]},
{t:'Riset & persona',lvl:'Menengah',d:'Mengenal pengguna lewat riset, persona, user story, dan peta pengalaman.',
 nodes:['Create User Personas','User Stories','Customer Experience Map by Mel Edwards','Simple Flowchart','Conceptual Design'],
 lessons:[
  {k:'c',t:'Persona berbasis data',nodes:['Create User Personas'],lang:'text',run:false,
   b:['<b>Persona</b> adalah gambaran pengguna yang disusun dari riset nyata (wawancara, survei, analitik), bukan dari imajinasi tim. Isinya: tujuan, konteks, perilaku, hambatan, dan kutipan asli.',
      'Wawancara 5-8 orang per segmen biasanya cukup untuk menemukan pola. Tanyakan perilaku nyata ("Ceritakan terakhir kali kamu...") alih-alih opini hipotetis ("Apakah kamu akan memakai...?").',
      'Persona yang baik membantu tim memutuskan; persona yang buruk hanya berisi hobi dan foto stok.'],
   code:`Persona: Rina, 24, staf admin di Bekasi (dari 7 wawancara)
Tujuan    : punya dana darurat sebelum menikah tahun depan
Konteks   : gaji tgl 25, Android entry-level, kuota terbatas
Perilaku  : cek e-wallet 5x sehari, menabung "kalau sisa"
Hambatan  : "Uangnya keburu kepakai buat ongkos dan jajan."
Kebutuhan : disisihkan otomatis sebelum sempat dipakai`,
   pts:['Persona dari data riset, bukan karangan.','Tanya perilaku masa lalu, bukan opini masa depan.','Fokus pada tujuan, konteks, hambatan.'],
   q:[['Pertanyaan wawancara yang lebih baik?',['Ceritakan terakhir kali kamu mencoba menabung','Apakah kamu suka fitur tabungan?','Kamu akan pakai aplikasi ini?'],0,'Cerita nyata lebih dapat dipercaya daripada opini.']]},
  {k:'c',t:'User story & peta pengalaman',nodes:['User Stories','Customer Experience Map by Mel Edwards','Simple Flowchart'],lang:'text',run:false,
   b:['<b>User story</b> menuliskan kebutuhan dari sudut pengguna: <i>Sebagai [peran], saya ingin [aksi], agar [manfaat]</i>, dilengkapi kriteria penerimaan yang bisa diuji.',
      '<b>Peta pengalaman</b> (customer journey) menyusun tahap pengguna dari sadar sampai loyal: apa yang dilakukan, dipikirkan, dirasakan, dan di mana titik sakitnya. Peluang desain biasanya muncul di titik emosi terendah.',
      '<b>Flowchart</b> sederhana menunjukkan langkah, keputusan, dan cabang error sebelum layar digambar.'],
   code:`User story
Sebagai karyawan bergaji bulanan, saya ingin tabungan
terpotong otomatis di tanggal gajian, agar tidak lupa.

Kriteria penerimaan
- bisa memilih tanggal 1-31 dan nominal minimal Rp 10.000
- jika saldo kurang, autodebet dicoba ulang besok, ada notifikasi
- autodebet bisa dijeda tanpa menghubungi CS

Flow: Beranda → Target → Nominal → Tanggal → [Saldo cukup?] → Sukses / Coba ulang`,
   pts:['User story: peran, aksi, manfaat + kriteria penerimaan.','Journey map: tahap, aksi, pikiran, emosi, peluang.','Flowchart memperlihatkan cabang error.'],
   q:[['Bagian mana yang membuat user story bisa diuji?',['Kriteria penerimaan','Nama persona','Warna tombol'],0,'Kriteria menjelaskan kapan cerita dianggap selesai.']]}
 ]},
{t:'Prototyping & pola tata letak',lvl:'Menengah',d:'Dari sketsa ke prototipe, aturan tata letak yang baik, dan alat desain.',
 nodes:['Prototyping','Good Layout Rules','Make UI Professional and Beautiful','Figma','Sketch','Adobe XD','Balsamiq','UX Best Practices'],
 lessons:[
  {k:'w',t:'Aturan tata letak yang baik',nodes:['Good Layout Rules','Make UI Professional and Beautiful','UX Best Practices'],
   b:['Kebanyakan layar terasa "berantakan" karena empat hal: jarak tidak konsisten, terlalu banyak gaya huruf, perataan tidak sejajar, dan tidak ada hierarki. Pakai skala jarak kelipatan 8 (8, 16, 24, 32), maksimal dua ukuran teks per kartu, dan satu garis rata kiri.',
      'Hukum <b>proximity</b> Gestalt: elemen yang berdekatan dianggap satu kelompok. Jarak di dalam kartu harus lebih kecil daripada jarak antarkartu.',
      'Ubah kode di bawah: rapikan jarak dengan variabel <code>--s</code> dan lihat pratinjaunya. Tugas: beri tombol kelas <code>utama</code> agar menjadi aksi utama.'],
   html:`<div class="kartu">
  <p class="label">Target tabungan</p>
  <h2>Dana Darurat</h2>
  <p class="angka">Rp 2.400.000 <span>dari Rp 6.000.000</span></p>
  <div class="bar"><i style="width:40%"></i></div>
  <button>Tambah setoran</button>
</div>`,
   css:`:root{--s:8px;--aksen:#0f766e}
body{font:16px/1.5 system-ui,sans-serif;padding:calc(var(--s)*3);background:#f6f7f5}
.kartu{background:#fff;border-radius:16px;padding:calc(var(--s)*3);max-width:320px;display:grid;gap:calc(var(--s)*1.5);box-shadow:0 1px 3px rgb(0 0 0/.08)}
.label{margin:0;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:#5b6360}
h2{margin:0;font-size:22px}
.angka{margin:0;font-weight:600}.angka span{font-weight:400;color:#5b6360}
.bar{height:8px;border-radius:8px;background:#e3e7e4}.bar i{display:block;height:100%;border-radius:8px;background:var(--aksen)}
button{min-height:48px;border-radius:12px;border:1px solid #c9cfcc;background:#fff;font:inherit}
button.utama{background:var(--aksen);color:#fff;border-color:transparent;font-weight:600}`,
   task:{q:'Jadikan tombol "Tambah setoran" sebagai aksi utama dengan menambahkan kelas utama.',test:"!!document.querySelector('button.utama')",hint:'Ubah <button> menjadi <button class="utama">.'},
   pts:['Jarak kelipatan 8, konsisten.','Proximity: jarak dalam kelompok < jarak antarkelompok.','Satu aksi utama yang menonjol.'],
   q:[['Menurut prinsip proximity, jarak di dalam kartu sebaiknya?',['Lebih kecil daripada jarak antarkartu','Sama dengan jarak antarkartu','Lebih besar'],0,'Agar isi kartu terbaca sebagai satu kelompok.']]},
  {k:'c',t:'Fidelity prototipe & alat desain',nodes:['Prototyping','Figma','Sketch','Adobe XD','Balsamiq'],lang:'text',run:false,
   b:['Pilih <b>fidelity</b> sesuai pertanyaan yang ingin dijawab. Sketsa kertas dan wireframe abu-abu (Balsamiq) untuk struktur dan alur; prototipe klik di Figma untuk menguji tugas; prototipe kode untuk interaksi rumit seperti drag atau animasi.',
      '<b>Figma</b> kini menjadi standar industri karena berbasis browser dan kolaboratif: komponen, variabel (token), auto layout, dan mode prototipe. Sketch masih dipakai di Mac; Adobe XD sudah tidak dikembangkan lagi.',
      'Uji prototipe sedini mungkin. Lima partisipan biasanya menemukan sebagian besar masalah besar pada satu alur.'],
   code:`Pertanyaan                         Fidelity
"Apakah urutan langkahnya masuk akal?"   sketsa / wireframe
"Bisakah pengguna menyelesaikan tugas?"  prototipe klik Figma
"Apakah gestur geser terasa wajar?"      prototipe kode`,
   pts:['Fidelity mengikuti pertanyaan riset.','Figma: komponen, variabel, auto layout, prototipe.','Uji dini dengan 5 partisipan per alur.'],
   q:[['Untuk menguji urutan langkah onboarding, fidelity yang cukup?',['Wireframe sederhana','Prototipe kode lengkap','Desain final dengan animasi'],0,'Struktur bisa diuji tanpa warna dan detail.']]}
 ]},
{t:'Mengukur dampak',lvl:'Lanjutan',d:'A/B test, uji multivariat, dan cara membaca hasilnya dengan benar.',
 nodes:['Measuring the Impact','Incremental A/B Testing','Multivariate Testing','Gather Lessons, Prioritize & Integrate'],
 lessons:[
  {k:'c',t:'A/B test yang benar',nodes:['Incremental A/B Testing','Measuring the Impact'],lang:'text',run:false,viz:'abtest',
   b:['<b>A/B test</b> membagi pengguna secara acak ke versi A (kontrol) dan B (perubahan), lalu membandingkan satu metrik utama. Tentukan hipotesis, metrik, dan ukuran sampel <b>sebelum</b> tes dimulai.',
      'Perbedaan kecil bisa muncul karena kebetulan. Uji statistik memberi <b>p-value</b>: peluang melihat perbedaan sebesar itu jika sebenarnya tidak ada efek. Konvensi umum: p &lt; 0,05. Jangan berhenti lebih awal hanya karena grafik sedang terlihat bagus.',
      'Coba visualisasi di atas: ubah jumlah pengunjung dan konversi tiap versi, lalu lihat apakah selisihnya signifikan.'],
   code:`Hipotesis : tombol "Bayar Rp 128.000" menaikkan konversi
            dibanding "Lanjut", karena total terlihat jelas.
Metrik    : % sesi checkout yang selesai bayar
Sampel    : 2 x 4.000 sesi (dihitung sebelum mulai)
Hasil     : A 11,2%  B 12,9%  selisih +1,7 poin, p = 0,02
Keputusan : rilis B, pantau tingkat pembatalan 2 minggu`,
   pts:['Hipotesis, metrik, sampel ditentukan di awal.','Acak pengguna; ubah satu hal.','p < 0,05 umum dipakai; jangan mengintip lalu berhenti.'],
   q:[['Kenapa tes tidak boleh dihentikan saat grafik sedang bagus?',['Peluang hasil kebetulan meningkat','Server lelah','Agar biaya turun'],0,'Mengintip berulang menaikkan false positive.'],
      ['Multivariate test berbeda dari A/B karena?',['Menguji kombinasi beberapa elemen sekaligus','Hanya untuk aplikasi mobile','Tidak memakai acak'],0,'Butuh trafik jauh lebih besar.']]}
 ]},
{t:'Proyek akhir',lvl:'Lanjutan',d:'Rancang ulang alur nyata dengan model perilaku dan ukur dampaknya.',nodes:['Project'],
 lessons:[
  {k:'proj',t:'Rancang ulang onboarding aplikasi tabungan',stack:'Riset + Figma + HTML/CSS',
   brief:'Aplikasi tabungan fiktif "Celengan" kehilangan 62% pengguna baru sebelum setoran pertama. Rancang ulang onboarding agar lebih banyak pengguna mengaktifkan autodebet dalam 7 hari.',
   feats:['Problem statement dengan outcome, aktor, dan aksi','Persona dari minimal 5 wawancara singkat','Peta perjalanan dengan titik emosi terendah','Analisis Fogg (motivasi, kemudahan, pemicu) untuk setiap langkah','Wireframe 3 alternatif dan alasan memilih satu','Prototipe klik 5 layar dengan state error dan kosong','Uji usability 5 orang dan daftar temuan dengan tingkat keparahan','Rencana A/B test: hipotesis, metrik, ukuran sampel'],
   steps:['Wawancara dan susun persona.','Petakan alur lama, cari titik putus.','Sketsa tiga pendekatan.','Bangun prototipe, uji, perbaiki.','Tulis rencana A/B test.'],
   files:[['rencana-ab.md','text',`Hipotesis: memilih target tabungan di langkah pertama
menaikkan aktivasi autodebet karena tujuan terasa nyata.

Kontrol (A): daftar → KTP → saldo → autodebet
Varian  (B): pilih target → nominal → autodebet → KTP nanti

Metrik utama : % pengguna baru aktifkan autodebet ≤ 7 hari
Metrik jaga  : % autodebet dibatalkan bulan pertama
Sampel       : 2 x 3.500 pengguna baru, durasi 14 hari
Kriteria     : rilis B jika naik ≥ 3 poin dan p < 0,05`]]}
 ]}
];
