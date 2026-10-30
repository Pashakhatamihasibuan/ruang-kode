/* ===================== PELAJARAN TAMBAHAN JALUR BARU =====================
   Dibuat oleh tools/gen/more.py. Setiap pelajaran ditambahkan di akhir modul yang dituju,
   sehingga alamat pelajaran lama (jalur-modul-urutan) tidak bergeser. */
(()=>{
const MORE=[
{
"track": "ux",
"module": "Cara manusia mengambil keputusan",
"lesson": {
"k": "c",
"t": "Hukum UX: Hick, Fitts, Jakob & Miller",
"nodes": [
"Human Decision Making",
"Behavioral Science"
],
"lang": "text",
"b": [
"Beberapa temuan psikologi sering dipakai sebagai \"hukum\" desain. <b>Hukum Hick</b>: makin banyak pilihan, makin lama orang memutuskan. Karena itu menu utama aplikasi yang baik hanya punya 4 sampai 5 tujuan, dan sisanya disimpan di menu \"Lainnya\".",
"<b>Hukum Fitts</b>: target yang besar dan dekat lebih cepat disentuh. Tombol utama di HP diletakkan di jangkauan jempol bagian bawah, dengan area sentuh minimal 44 sampai 48 piksel. <b>Hukum Jakob</b>: pengguna menghabiskan sebagian besar waktunya di aplikasi lain, jadi mereka berharap aplikasimu bekerja seperti yang sudah mereka kenal. Ikon keranjang di kanan atas bukan kebetulan.",
"<b>Hukum Miller</b> sering dikutip sebagai \"7 ± 2 item\", tetapi pelajaran yang lebih berguna adalah <b>chunking</b>: kelompokkan informasi. Nomor <code>081234567890</code> lebih mudah diperiksa sebagai <code>0812-3456-7890</code>. Hukum ini alat bantu berpikir, bukan aturan mutlak; tetap uji dengan pengguna."
],
"pts": [
"Hick: pilihan lebih sedikit, keputusan lebih cepat.",
"Fitts: target penting dibuat besar dan mudah dijangkau.",
"Jakob: ikuti pola yang sudah dikenal pengguna.",
"Miller: kelompokkan informasi (chunking)."
],
"q": [
[
"Menampilkan 3 metode bayar populer dan menyembunyikan sisanya menerapkan?",
[
"Hukum Hick",
"Hukum Fitts",
"Hukum Jakob"
],
0,
"Lebih sedikit pilihan di awal mempercepat keputusan."
],
[
"Kenapa tombol utama di HP sebaiknya besar dan di bawah?",
[
"Hukum Fitts: target besar dan dekat lebih cepat disentuh",
"Agar terlihat modern",
"Hukum Miller"
],
0,
"Ukuran dan jarak menentukan kecepatan menyentuh target."
]
],
"code": "Ulasan cepat layar checkout dengan empat hukum\n\nHick   : 9 metode bayar ditampilkan sekaligus\n         -> tampilkan 3 yang paling sering dipakai, sisanya \"Lihat semua\"\nFitts  : tombol \"Bayar\" kecil di pojok kanan atas\n         -> tombol lebar di bawah, dalam jangkauan jempol\nJakob  : ikon keranjang di kiri bawah, tidak seperti aplikasi lain\n         -> pindahkan ke posisi yang sudah dikenal pengguna\nMiller : nomor virtual account 16 digit tanpa jeda\n         -> 8808 1234 5678 9012 + tombol Salin",
"run": false
}
},
{
"track": "ux",
"module": "Riset & persona",
"lesson": {
"k": "c",
"t": "Wawancara pengguna yang tidak mengarahkan",
"nodes": [
"User Research",
"Interviews"
],
"lang": "text",
"b": [
"Wawancara pengguna bertujuan memahami <b>perilaku nyata</b>, bukan mengumpulkan pendapat tentang fitur. Pertanyaan \"Apakah kamu mau fitur X?\" hampir selalu dijawab \"mau\", padahal belum tentu dipakai. Tanyakan apa yang terakhir kali mereka lakukan.",
"Hindari pertanyaan yang mengarahkan (\"Fitur ini memudahkan, kan?\") dan pertanyaan hipotetis (\"Apakah kamu akan...\"). Gunakan pertanyaan terbuka: \"Ceritakan terakhir kali kamu...\", lalu gali dengan \"Kenapa?\" dan \"Lalu apa yang terjadi?\". Diam beberapa detik juga teknik yang ampuh: orang cenderung melanjutkan cerita.",
"Lima sampai delapan wawancara per segmen biasanya cukup untuk melihat pola. Rekam (dengan izin), tulis kutipan apa adanya, lalu kelompokkan temuan dengan affinity mapping. Minta persetujuan tertulis dan simpan data pribadi sesuai UU PDP."
],
"pts": [
"Tanyakan perilaku masa lalu, bukan pendapat atau rencana.",
"Hindari pertanyaan yang mengarahkan.",
"Gali dengan \"kenapa\" dan biarkan hening sejenak.",
"5 sampai 8 wawancara per segmen untuk melihat pola."
],
"q": [
[
"Pertanyaan mana yang paling baik?",
[
"Ceritakan terakhir kali kamu membayar tagihan listrik.",
"Apakah kamu akan memakai fitur bayar otomatis?",
"Fitur kami membantu, kan?"
],
0,
"Pertanyaan tentang kejadian nyata menghasilkan data perilaku."
],
[
"Kenapa \"Apakah kamu mau fitur X?\" berbahaya?",
[
"Orang cenderung menjawab mau walau tidak akan memakainya",
"Pertanyaannya terlalu panjang",
"Melanggar UU PDP"
],
0,
"Pendapat tentang masa depan tidak memprediksi perilaku."
]
],
"code": "Kurang baik (mengarahkan / hipotetis)     Lebih baik (perilaku nyata)\n- \"Kamu suka fitur tabungan otomatis?\"    - \"Ceritakan terakhir kali kamu menabung.\"\n- \"Aplikasi kami mudah dipakai, kan?\"     - \"Bagian mana yang membuatmu berhenti sejenak?\"\n- \"Apakah kamu akan membayar Rp20 ribu?\"  - \"Layanan apa yang kamu bayar bulan lalu? Kenapa?\"\n- \"Kenapa tidak pakai fitur filter?\"      - \"Bagaimana biasanya kamu mencari barang?\"\n\nPenutup wawancara:\n\"Ada hal yang belum saya tanyakan tapi menurutmu penting?\"",
"run": false
}
},
{
"track": "ux",
"module": "Prototyping & pola tata letak",
"lesson": {
"k": "c",
"t": "Usability test & 10 heuristik Nielsen",
"nodes": [
"Prototyping",
"Usability Testing"
],
"lang": "text",
"b": [
"<b>Usability test</b> meminta pengguna menyelesaikan tugas nyata dengan prototipe sambil berpikir keras, sementara kamu mengamati tanpa membantu. Model Nielsen-Landauer memperkirakan 5 peserta menemukan sekitar 85% masalah di satu alur. Lebih baik tiga putaran kecil yang diselingi perbaikan daripada satu tes besar.",
"Sebelum tes dengan pengguna, ulas layar sendiri dengan <b>10 heuristik Nielsen</b>, antara lain: tampilkan status sistem, gunakan bahasa pengguna, beri kendali untuk membatalkan, konsisten, cegah error, lebih baik mengenali daripada mengingat, dan bantu pengguna pulih dari error.",
"Catat setiap temuan dengan tingkat keparahan 0 sampai 4. Perbaiki yang 3 dan 4 lebih dulu. Ukur juga keberhasilan tugas, waktu, dan kepuasan (misalnya skor SEQ satu pertanyaan setelah tiap tugas)."
],
"pts": [
"Beri skenario tugas, bukan instruksi klik.",
"5 peserta per putaran, ulangi setelah perbaikan.",
"Ulas dulu dengan 10 heuristik Nielsen.",
"Beri tingkat keparahan 0 sampai 4."
],
"q": [
[
"Apa yang sebaiknya dilakukan fasilitator saat peserta bingung?",
[
"Mengamati dan bertanya apa yang dipikirkan, tanpa memberi jawaban",
"Langsung menunjukkan tombolnya",
"Menghentikan tes"
],
0,
"Kebingungan itu sendiri adalah temuan."
],
[
"Pesan \"Error 402\" tanpa penjelasan melanggar heuristik?",
[
"Bantu pengguna mengenali dan pulih dari error",
"Estetika minimalis",
"Fleksibilitas"
],
0,
"Pesan error harus menjelaskan masalah dan solusinya."
]
],
"code": "Skenario tugas (bukan instruksi klik)\n\"Kamu ingin mengirim Rp150.000 ke adikmu, Rina. Silakan lakukan.\"\n\nLembar temuan\n#  Heuristik yang dilanggar       Temuan                               Keparahan\n1  Status sistem                  Tidak ada tanda transfer diproses    3\n2  Bahasa pengguna                Label \"Beneficiary\" membingungkan    2\n3  Pulih dari error               \"Error 402\" tanpa penjelasan         4\n4  Mengenali, bukan mengingat     Harus mengetik ulang no. rekening    3",
"run": false
}
},
{
"track": "ux",
"module": "Mengukur dampak",
"lesson": {
"k": "c",
"t": "Metrik HEART & North Star",
"nodes": [
"Measuring Impact",
"Metrics"
],
"lang": "text",
"b": [
"Desain yang baik harus terlihat dampaknya. Kerangka <b>HEART</b> dari Google membagi metrik pengalaman menjadi lima: <b>Happiness</b> (kepuasan), <b>Engagement</b> (seberapa sering dan dalam), <b>Adoption</b> (pengguna baru suatu fitur), <b>Retention</b> (yang kembali), dan <b>Task success</b> (berhasil, cepat, tanpa error).",
"Untuk setiap kategori, tulis <b>Goal</b> (tujuan), <b>Signal</b> (perilaku yang menandakan tujuan tercapai), dan <b>Metric</b> (angka yang bisa dihitung). Tidak semua kategori harus dipakai; pilih yang relevan dengan fitur.",
"<b>North Star metric</b> adalah satu angka yang paling mencerminkan nilai yang diterima pengguna, misalnya \"jumlah pesanan yang sampai tepat waktu per minggu\" untuk aplikasi kurir. Metrik ini menyatukan tim dan mencegah mengejar angka semu seperti jumlah unduhan."
],
"pts": [
"HEART: Happiness, Engagement, Adoption, Retention, Task success.",
"Turunkan Goal → Signal → Metric.",
"North Star mencerminkan nilai bagi pengguna.",
"Hindari metrik semu seperti jumlah unduhan."
],
"q": [
[
"\"% pengguna yang masih memakai fitur setelah 30 hari\" termasuk kategori?",
[
"Retention",
"Adoption",
"Happiness"
],
0,
"Retention mengukur yang kembali dan bertahan."
],
[
"Mana yang paling cocok jadi North Star aplikasi kurir?",
[
"Paket terkirim tepat waktu per minggu",
"Jumlah unduhan aplikasi",
"Jumlah halaman yang dilihat"
],
0,
"North Star harus mencerminkan nilai yang diterima pengguna."
]
],
"code": "Fitur: pembayaran tagihan otomatis\n\nKategori      Goal                         Signal                           Metric\nAdoption      Pengguna mencoba fitur       Mengaktifkan bayar otomatis      % pengguna aktif yang mengaktifkan / minggu\nTask success  Pembayaran lancar            Tagihan terbayar tanpa gagal     % pembayaran berhasil\nRetention     Fitur tetap dipakai          Tidak mematikan dalam 30 hari    % masih aktif setelah 30 hari\nHappiness     Merasa tenang                Skor survei singkat              rata-rata CSAT 1-5\n\nNorth Star: jumlah tagihan yang terbayar tepat waktu per bulan",
"run": false
}
},
{
"track": "ds",
"module": "Bahasa desain",
"lesson": {
"k": "c",
"t": "Ikon, ilustrasi & motion yang konsisten",
"nodes": [
"Design Language",
"Iconography"
],
"lang": "css",
"b": [
"Bahasa desain tidak berhenti di warna dan huruf. <b>Ikon</b> perlu satu gaya: ukuran grid sama (misalnya 24×24), ketebalan garis sama, sudut sama. Mencampur ikon garis dan ikon terisi dari pustaka berbeda langsung terlihat tidak rapi.",
"<b>Ilustrasi</b> perlu aturan palet, proporsi tokoh, dan kapan dipakai (biasanya empty state dan onboarding, bukan di setiap layar). <b>Motion</b> juga bagian bahasa: durasi standar (misalnya 150 ms untuk hover, 250 ms untuk panel), kurva easing, dan arah gerak yang sama.",
"Semua ini dibakukan sebagai token dan pedoman. Hormati <code>prefers-reduced-motion</code> agar pengguna yang sensitif terhadap gerakan tidak terganggu."
],
"pts": [
"Ikon: satu grid, satu ketebalan garis, satu gaya.",
"Ilustrasi punya aturan kapan dipakai.",
"Motion dibakukan sebagai token durasi dan easing.",
"Hormati prefers-reduced-motion."
],
"q": [
[
"Kenapa mencampur ikon dari beberapa pustaka bermasalah?",
[
"Ketebalan garis dan gayanya berbeda sehingga terlihat tidak konsisten",
"Ukuran file terlalu besar",
"Ikon tidak bisa diwarnai"
],
0,
"Konsistensi visual adalah inti bahasa desain."
],
[
"Apa fungsi token durasi motion?",
[
"Menyamakan kecepatan animasi di semua komponen",
"Mempercepat situs",
"Mengganti warna"
],
0,
"Durasi yang sama membuat gerak terasa satu sistem."
]
],
"code": ":root {\n  --icon-size-sm: 16px;\n  --icon-size-md: 24px;\n  --icon-stroke: 1.75;\n\n  --motion-duration-fast: 150ms;   /* hover, fokus */\n  --motion-duration-base: 250ms;   /* panel, dropdown */\n  --motion-easing-standard: cubic-bezier(.2, 0, 0, 1);\n}\n\n@media (prefers-reduced-motion: reduce) {\n  :root { --motion-duration-fast: 0ms; --motion-duration-base: 0ms; }\n}\n\n.dropdown { transition: opacity var(--motion-duration-base) var(--motion-easing-standard); }",
"run": false
}
},
{
"track": "ds",
"module": "Komponen inti",
"lesson": {
"k": "c",
"t": "Memilih komponen umpan balik: toast, banner, modal",
"nodes": [
"Components",
"Feedback"
],
"lang": "html",
"b": [
"Design system yang matang tidak hanya menyediakan komponen, tetapi juga menjelaskan <b>kapan</b> setiap komponen dipakai. Tiga komponen umpan balik yang sering tertukar adalah toast, banner, dan modal.",
"<b>Toast</b> untuk konfirmasi ringan yang tidak butuh tindakan (\"Alamat disimpan\"), hilang sendiri, dan diumumkan lewat <code>role=\"status\"</code>. <b>Banner</b> untuk informasi yang tetap relevan selama pengguna di halaman itu (\"Koneksi terputus\"). <b>Modal</b> hanya untuk keputusan yang harus dijawab sebelum lanjut, karena memblokir seluruh halaman.",
"Modal yang baik memindahkan fokus ke dalamnya, mengunci fokus selama terbuka, bisa ditutup dengan Esc, dan mengembalikan fokus ke tombol pemicunya. Elemen <code>&lt;dialog&gt;</code> dengan <code>showModal()</code> memberi sebagian besar perilaku ini secara bawaan."
],
"pts": [
"Toast: konfirmasi ringan, hilang sendiri, role=status.",
"Banner: informasi yang tetap relevan di halaman.",
"Modal: hanya untuk keputusan yang memblokir.",
"Modal mengelola fokus dan bisa ditutup dengan Esc."
],
"q": [
[
"\"Pesanan berhasil disimpan\" paling cocok ditampilkan sebagai?",
[
"Toast",
"Modal",
"Halaman baru"
],
0,
"Konfirmasi ringan tidak perlu memblokir pengguna."
],
[
"Kapan modal tepat dipakai?",
[
"Saat pengguna harus memutuskan sebelum lanjut, misalnya konfirmasi hapus",
"Untuk setiap pesan sukses",
"Untuk iklan"
],
0,
"Modal memblokir, jadi pakai hanya untuk keputusan penting."
]
],
"code": "<!-- Toast: konfirmasi ringan, tidak memblokir -->\n<div class=\"toast\" role=\"status\">Alamat disimpan</div>\n\n<!-- Banner: informasi selama di halaman ini -->\n<div class=\"banner banner--warning\" role=\"alert\">\n  Koneksi terputus. Perubahan akan dikirim saat online kembali.\n</div>\n\n<!-- Modal: keputusan yang harus dijawab -->\n<dialog id=\"hapus\" aria-labelledby=\"hapus-judul\">\n  <h2 id=\"hapus-judul\">Hapus alamat \"Rumah\"?</h2>\n  <p>Alamat ini tidak bisa dikembalikan.</p>\n  <button value=\"batal\">Batal</button>\n  <button value=\"hapus\" class=\"danger\">Hapus alamat</button>\n</dialog>",
"run": false
}
},
{
"track": "ds",
"module": "Design token & fondasi visual",
"lesson": {
"k": "c",
"t": "Token lintas platform: format DTCG",
"nodes": [
"Design Tokens",
"Tooling"
],
"lang": "json",
"b": [
"Token yang hanya hidup di Figma atau hanya di CSS akan cepat berbeda. Solusinya: simpan token di satu berkas sumber, lalu <b>hasilkan</b> CSS, kode Android, dan iOS darinya.",
"Format yang kini dipakai banyak alat adalah format <b>DTCG</b> (Design Tokens Community Group, W3C). Versi stabil pertamanya, 2025.10, dirilis Oktober 2025. Setiap token punya <code>$value</code> dan <code>$type</code>, dan token bisa merujuk token lain dengan kurung kurawal.",
"Alat seperti Style Dictionary atau Tokens Studio membaca berkas ini dan menulis variabel CSS, berkas Kotlin, Swift, dan lainnya. Perubahan warna brand cukup di satu tempat, lalu semua platform ikut berubah lewat pipeline build."
],
"pts": [
"Satu sumber token, banyak keluaran platform.",
"DTCG: $value, $type, dan rujukan {token.lain}.",
"Style Dictionary / Tokens Studio menghasilkan kode.",
"Perubahan brand cukup di satu berkas."
],
"q": [
[
"Apa arti \"$value\": \"{color.blue.600}\"?",
[
"Token ini merujuk nilai token color.blue.600",
"Warnanya biru tua tetap",
"Komentar"
],
0,
"Kurung kurawal adalah rujukan antartoken."
],
[
"Keuntungan utama berkas token tunggal?",
[
"Web, Android, dan iOS memakai nilai yang sama",
"Desainer tidak perlu Figma",
"Situs lebih cepat"
],
0,
"Satu sumber mencegah nilai berbeda di tiap platform."
]
],
"code": "{\n  \"color\": {\n    \"blue\": {\n      \"600\": { \"$value\": \"#2563EB\", \"$type\": \"color\" }\n    },\n    \"action\": {\n      \"primary\": { \"$value\": \"{color.blue.600}\", \"$type\": \"color\",\n                   \"$description\": \"Latar tombol utama\" }\n    }\n  },\n  \"space\": {\n    \"md\": { \"$value\": \"16px\", \"$type\": \"dimension\" }\n  }\n}\n\n/* hasil build untuk web */\n:root {\n  --color-blue-600: #2563EB;\n  --color-action-primary: var(--color-blue-600);\n  --space-md: 16px;\n}",
"run": false
}
},
{
"track": "ds",
"module": "Dokumentasi, tooling & tata kelola",
"lesson": {
"k": "c",
"t": "Aksesibilitas bawaan komponen (WCAG 2.2)",
"nodes": [
"Accessibility",
"Documentation"
],
"lang": "text",
"b": [
"Design system adalah tempat paling efektif untuk aksesibilitas: perbaiki sekali di komponen, seluruh produk ikut benar. Jadikan <b>WCAG 2.2 level AA</b> sebagai standar minimum setiap komponen.",
"Beberapa kriteria baru WCAG 2.2 yang langsung berdampak ke komponen: <b>2.4.11 Focus Not Obscured</b> (elemen yang difokus tidak tertutup header lengket atau banner), <b>2.5.7 Dragging Movements</b> (slider dan daftar yang bisa diseret harus punya alternatif tanpa seret), dan <b>2.5.8 Target Size</b> (target minimal 24×24 piksel; untuk kenyamanan sentuh tetap rancang 44×44).",
"Tuliskan di dokumentasi setiap komponen: perilaku keyboard, atribut ARIA yang dipakai, kontras warna setiap state, dan contoh salah-benar. Uji dengan keyboard dan pembaca layar, karena alat otomatis hanya menangkap sebagian masalah."
],
"pts": [
"Perbaiki aksesibilitas sekali di komponen.",
"WCAG 2.2 AA sebagai standar minimum.",
"Dokumentasikan keyboard, ARIA, kontras, ukuran.",
"Uji manual; alat otomatis tidak cukup."
],
"q": [
[
"Kriteria WCAG 2.2 mana yang terkait header lengket yang menutupi elemen fokus?",
[
"2.4.11 Focus Not Obscured",
"2.5.8 Target Size",
"1.4.3 Contrast"
],
0,
"Elemen yang difokus tidak boleh tertutup sepenuhnya."
],
[
"Slider yang hanya bisa diseret melanggar?",
[
"2.5.7 Dragging Movements",
"3.3.8 Accessible Authentication",
"Tidak melanggar apa pun"
],
0,
"Harus ada alternatif satu ketukan, misalnya tombol + dan −."
]
],
"code": "Dokumentasi komponen: Tombol\n\nKeyboard     Tab untuk fokus, Enter / Spasi untuk menekan\nFokus        Garis 2px var(--color-focus), kontras >= 3:1 terhadap latar\nUkuran       Tinggi minimal 44px (target WCAG 2.5.8 minimal 24px)\nKontras      Teks >= 4.5:1 di semua state (default, hover, disabled diberi label)\nARIA         aria-pressed untuk tombol toggle; aria-busy saat memuat\nJangan       Pakai <div onclick>; ikon tanpa aria-label",
"run": false
}
},
{
"track": "git",
"module": "Branch & merge",
"lesson": {
"k": "c",
"t": "Strategi cabang: GitHub Flow & trunk-based",
"nodes": [
"Branching Basics",
"Collaboration"
],
"lang": "bash",
"b": [
"Tim perlu kesepakatan cara memakai cabang. <b>GitHub Flow</b> paling sederhana: <code>main</code> selalu siap rilis; setiap pekerjaan dibuat di cabang pendek, dibuka pull request, ditinjau, lalu digabung dan dirilis.",
"<b>Trunk-based development</b> lebih ekstrem: cabang hidup paling lama sehari atau dua hari, dan fitur yang belum selesai disembunyikan dengan <b>feature flag</b>. Cocok untuk tim yang rilis berkali-kali sehari dengan tes otomatis yang kuat.",
"<b>Git Flow</b> memakai cabang <code>develop</code>, <code>release/*</code>, dan <code>hotfix/*</code>. Masih dipakai untuk produk dengan jadwal rilis berversi (misalnya aplikasi desktop), tetapi terlalu berat untuk kebanyakan aplikasi web. Apa pun pilihannya, beri nama cabang yang jelas."
],
"pts": [
"GitHub Flow: main selalu siap rilis, cabang pendek + PR.",
"Trunk-based: cabang 1-2 hari + feature flag.",
"Git Flow: untuk rilis berversi, lebih berat.",
"Nama cabang: jenis/ringkasan."
],
"q": [
[
"Ciri utama trunk-based development?",
[
"Cabang sangat pendek dan fitur belum jadi disembunyikan dengan feature flag",
"Cabang develop yang berumur panjang",
"Tidak memakai pull request sama sekali"
],
0,
"Integrasi sering mengurangi konflik besar."
],
[
"Dalam GitHub Flow, kondisi cabang main seharusnya?",
[
"Selalu siap dirilis",
"Berisi kode percobaan",
"Hanya diubah sebulan sekali"
],
0,
"Semua perubahan masuk lewat PR yang sudah ditinjau."
]
],
"code": "# GitHub Flow sehari-hari\ngit switch main\ngit pull\ngit switch -c fitur/filter-harga      # nama cabang: jenis/ringkasan\n# ... ubah kode, commit kecil-kecil ...\ngit push -u origin fitur/filter-harga\ngh pr create --fill                   # buka pull request\n# setelah disetujui dan digabung:\ngit switch main && git pull\ngit branch -d fitur/filter-harga",
"run": false
}
},
{
"track": "git",
"module": "Penggunaan dasar Git",
"lesson": {
"k": "c",
"t": "Tag & rilis dengan semantic versioning",
"nodes": [
"git tag",
"Releases"
],
"lang": "bash",
"b": [
"<b>Tag</b> memberi nama tetap pada satu commit, biasanya untuk menandai rilis. Berbeda dengan cabang, tag tidak bergerak. Pakai <b>annotated tag</b> (<code>-a</code>) agar tercatat siapa dan kapan membuatnya.",
"Penomoran yang paling umum adalah <b>Semantic Versioning</b>: <code>MAYOR.MINOR.PATCH</code>. Naikkan PATCH untuk perbaikan bug, MINOR untuk fitur baru yang tetap kompatibel, dan MAYOR untuk perubahan yang merusak kompatibilitas. Versi <code>0.x</code> berarti API belum stabil.",
"Tag harus di-push secara eksplisit. Di GitHub, tag bisa dijadikan <b>Release</b> dengan catatan perubahan; GitHub dapat membuat catatan rilis otomatis dari judul pull request."
],
"pts": [
"Tag menandai satu commit secara tetap.",
"Annotated tag (-a) mencatat pembuat dan pesan.",
"SemVer: MAYOR.MINOR.PATCH.",
"Tag perlu di-push: git push origin v1.4.0."
],
"q": [
[
"Menambah fitur baru yang tetap kompatibel dari 2.3.1 menjadi?",
[
"2.4.0",
"3.0.0",
"2.3.2"
],
0,
"Fitur kompatibel menaikkan MINOR dan PATCH kembali ke 0."
],
[
"Apakah git push biasa mengirim tag?",
[
"Tidak, tag di-push secara eksplisit",
"Ya, selalu",
"Hanya tag ringan"
],
0,
"Gunakan git push origin nama-tag atau --tags."
]
],
"code": "git log --oneline -3\ngit tag -a v1.4.0 -m \"Fitur filter harga\"\ngit push origin v1.4.0\ngit tag --list \"v1.*\"\ngit show v1.4.0 --stat\n\n# contoh urutan versi\n# 1.3.2 -> 1.3.3   perbaikan bug total keranjang      (PATCH)\n# 1.3.3 -> 1.4.0   fitur filter harga                 (MINOR)\n# 1.4.0 -> 2.0.0   format API /pesanan diubah         (MAYOR)",
"run": false
}
},
{
"track": "git",
"module": "Lebih jauh dengan GitHub",
"lesson": {
"k": "c",
"t": "git bisect: mencari commit penyebab bug",
"nodes": [
"git bisect",
"Debugging"
],
"lang": "bash",
"b": [
"Fitur kemarin masih jalan, hari ini rusak, dan di antaranya ada 60 commit. <b><code>git bisect</code></b> mencari commit penyebabnya dengan <b>pencarian biner</b>: Git memilih commit di tengah, kamu menandai baik atau buruk, lalu rentangnya dibelah dua lagi.",
"Untuk 60 commit hanya perlu sekitar 6 langkah, karena 2<sup>6</sup> = 64. Kalau ada tes atau skrip yang bisa memeriksa bug secara otomatis, <code>git bisect run</code> menjalankan semuanya tanpa campur tangan.",
"Setelah ketemu, jangan lupa <code>git bisect reset</code> untuk kembali ke cabang semula. Ini salah satu perintah Git yang jarang diketahui pemula, padahal bisa menghemat berjam-jam."
],
"pts": [
"bisect memakai pencarian biner pada riwayat.",
"n commit butuh sekitar log2(n) langkah.",
"git bisect run untuk pemeriksaan otomatis.",
"Akhiri dengan git bisect reset."
],
"q": [
[
"Berapa langkah kira-kira untuk mencari di antara 1.000 commit?",
[
"Sekitar 10",
"Sekitar 500",
"1.000"
],
0,
"2^10 = 1.024, jadi sekitar 10 langkah."
],
[
"Apa fungsi git bisect run?",
[
"Menjalankan skrip tes di setiap langkah secara otomatis",
"Menghapus commit rusak",
"Mendorong perbaikan ke remote"
],
0,
"Kode keluar skrip menentukan baik atau buruk."
]
],
"code": "git bisect start\ngit bisect bad                 # commit sekarang rusak\ngit bisect good v1.3.0         # versi ini masih benar\n# Git berpindah ke commit di tengah; uji, lalu tandai:\ngit bisect good                # atau: git bisect bad\n# ... ulangi sampai Git menulis:\n# a1b2c3d is the first bad commit\n\n# otomatis dengan tes:\ngit bisect run npm test -- keranjang.test.js\ngit bisect reset               # kembali ke cabang semula",
"run": false
}
},
{
"track": "css",
"module": "Warna, latar & tipografi",
"lesson": {
"k": "c",
"t": "Warna modern: oklch, color-mix & light-dark",
"nodes": [
"Colors",
"Modern CSS"
],
"lang": "css",
"b": [
"Selain heksa dan <code>rgb()</code>, CSS modern punya <b><code>oklch()</code></b>: <i>lightness</i>, <i>chroma</i> (kepekatan), dan <i>hue</i>. Keunggulannya, perubahan lightness terasa merata di mata manusia, sehingga membuat skala warna 100 sampai 900 jauh lebih mudah.",
"<b><code>color-mix()</code></b> mencampur dua warna langsung di CSS, misalnya membuat latar lembut dari warna brand tanpa menambah token baru. <b><code>light-dark()</code></b> memilih nilai untuk tema terang atau gelap sesuai <code>color-scheme</code>.",
"Ketiganya didukung browser modern sejak 2023 sampai 2024. Untuk browser lama, tulis nilai cadangan heksa di baris sebelumnya; browser akan memakai baris terakhir yang dipahaminya."
],
"pts": [
"oklch: lightness, chroma, hue; skala warna lebih merata.",
"color-mix() mencampur warna di CSS.",
"light-dark() memilih nilai sesuai tema.",
"Beri nilai cadangan untuk browser lama."
],
"q": [
[
"Apa kelebihan oklch untuk membuat skala warna?",
[
"Perubahan lightness terasa merata di mata",
"Ukuran file lebih kecil",
"Hanya bisa warna abu-abu"
],
0,
"oklch dirancang mengikuti persepsi manusia."
],
[
"light-dark(#000, #fff) bekerja berdasarkan?",
[
"color-scheme yang aktif",
"Lebar layar",
"Jam di perangkat"
],
0,
"Nilai dipilih sesuai skema warna terang atau gelap."
]
],
"code": ":root {\n  color-scheme: light dark;\n  --brand: oklch(55% 0.15 255);                  /* biru */\n  --brand-soft: color-mix(in oklch, var(--brand) 15%, white);\n  --teks: light-dark(#152033, #E4EAF2);\n  --latar: light-dark(#F2F4F8, #0C121B);\n}\n\n.tombol {\n  background: #255DA2;          /* cadangan untuk browser lama */\n  background: var(--brand);\n}\n.tombol:hover { background: oklch(from var(--brand) calc(l - 0.08) c h); }\n.badge { background: var(--brand-soft); color: var(--brand); }",
"run": false
}
},
{
"track": "css",
"module": "Selector lanjutan, transisi & animasi",
"lesson": {
"k": "c",
"t": ":has(): selector induk & nesting",
"nodes": [
"Pseudo-classes",
"Modern CSS"
],
"lang": "css",
"b": [
"Selama bertahun-tahun CSS tidak bisa memilih elemen <b>berdasarkan isinya</b>. <code>:has()</code> mengubah itu: <code>.kartu:has(img)</code> memilih kartu yang berisi gambar, dan <code>form:has(:invalid)</code> memilih form yang masih punya isian salah.",
"Ini membuat banyak JavaScript kecil tidak diperlukan lagi, misalnya menandai label saat checkbox di dalamnya dicentang. Hati-hati memakai <code>:has()</code> pada elemen yang sangat umum seperti <code>body</code>, karena browser harus memeriksa ulang saat isinya berubah.",
"CSS kini juga mendukung <b>nesting</b> tanpa Sass: aturan untuk anak elemen ditulis di dalam blok induknya, dan <code>&amp;</code> merujuk induk itu sendiri."
],
"pts": [
":has() memilih elemen berdasarkan isinya.",
"Mengganti JavaScript kecil untuk status visual.",
"Hindari :has() pada elemen sangat umum.",
"Nesting bawaan dengan & tanpa Sass."
],
"q": [
[
"Selector untuk kartu yang berisi gambar?",
[
".kartu:has(img)",
".kartu img",
"img .kartu"
],
0,
".kartu img memilih gambarnya, bukan kartunya."
],
[
"Dalam nesting CSS, & merujuk ke?",
[
"Selector induk",
"Elemen berikutnya",
"Elemen html"
],
0,
"& menggantikan selector blok induknya."
]
],
"code": "/* kartu dengan gambar memakai tata letak dua kolom */\n.kartu:has(img) { display: grid; grid-template-columns: 120px 1fr; gap: 12px; }\n\n/* tombol kirim redup selama ada isian yang salah */\nform:has(:invalid) button[type=\"submit\"] { opacity: .5; }\n\n/* label ikut tersorot saat pilihannya dicentang */\n.pilihan:has(input:checked) { border-color: var(--brand); background: var(--brand-soft); }\n\n/* nesting bawaan CSS */\n.menu {\n  display: flex;\n  & a { padding: 8px 12px; }\n  & a:hover { text-decoration: underline; }\n}",
"run": false
}
},
{
"track": "css",
"module": "Responsif",
"lesson": {
"k": "c",
"t": "Gambar responsif, aspect-ratio & object-fit",
"nodes": [
"Responsive Design",
"Images"
],
"lang": "html",
"b": [
"Gambar sering menjadi bagian terberat halaman. <code>srcset</code> dan <code>sizes</code> memberi browser beberapa ukuran sehingga HP tidak mengunduh gambar selebar desktop. <code>&lt;picture&gt;</code> menambahkan format modern seperti AVIF dan WebP dengan cadangan JPEG.",
"<code>aspect-ratio</code> menjaga proporsi kotak, misalnya 16/9 untuk video atau 1/1 untuk foto produk, bahkan sebelum gambar dimuat, sehingga tata letak tidak bergeser (CLS). <code>object-fit: cover</code> mengisi kotak tanpa membuat gambar gepeng.",
"Gabungkan dengan <code>loading=\"lazy\"</code> untuk gambar di bawah layar, tetapi jangan untuk gambar utama di atas layar, karena justru memperlambat LCP."
],
"pts": [
"srcset + sizes: browser memilih ukuran yang pas.",
"picture untuk AVIF/WebP dengan cadangan.",
"aspect-ratio mencegah tata letak bergeser.",
"Jangan lazy-load gambar utama di atas layar."
],
"q": [
[
"Apa guna sizes=\"(min-width: 768px) 33vw, 100vw\"?",
[
"Memberi tahu browser lebar gambar di layar agar memilih file yang tepat",
"Mengubah ukuran gambar di server",
"Memotong gambar"
],
0,
"Browser memakai sizes untuk memilih kandidat srcset."
],
[
"object-fit: cover membuat gambar?",
[
"Mengisi kotak tanpa gepeng, sebagian bisa terpotong",
"Selalu terlihat utuh dengan ruang kosong",
"Menjadi hitam putih"
],
0,
"cover mempertahankan proporsi sambil memenuhi kotak."
]
],
"code": "<picture>\n  <source type=\"image/avif\" srcset=\"kopi-400.avif 400w, kopi-800.avif 800w\">\n  <source type=\"image/webp\" srcset=\"kopi-400.webp 400w, kopi-800.webp 800w\">\n  <img src=\"kopi-800.jpg\" alt=\"Kopi Gayo dalam kemasan 250 gram\"\n       srcset=\"kopi-400.jpg 400w, kopi-800.jpg 800w\"\n       sizes=\"(min-width: 768px) 33vw, 100vw\"\n       width=\"800\" height=\"800\" loading=\"lazy\">\n</picture>\n\n<style>\n.foto-produk {\n  width: 100%;\n  aspect-ratio: 1 / 1;\n  object-fit: cover;\n  border-radius: 12px;\n}\n</style>",
"run": false
}
},
{
"track": "da",
"module": "Statistik deskriptif",
"lesson": {
"k": "c",
"t": "Persentil, kuartil & median",
"nodes": [
"Descriptive Statistics",
"Percentiles"
],
"lang": "python",
"b": [
"Rata-rata mudah tertarik oleh nilai ekstrem. Satu transaksi grosir Rp2,1 juta di antara transaksi ratusan ribu membuat rata-rata terlihat jauh lebih tinggi dari kebanyakan pembeli. <b>Median</b> (nilai tengah) lebih tahan terhadap outlier.",
"<b>Persentil</b> ke-p adalah nilai yang berada di atas p% data. Kuartil adalah persentil 25 (Q1), 50 (median), dan 75 (Q3). Jarak Q3 - Q1 disebut <b>IQR</b>, dipakai di box plot dan untuk mendeteksi outlier.",
"Di laporan bisnis, persentil sering lebih jujur daripada rata-rata. Contoh: \"90% pesanan sampai dalam 2 hari\" (P90) lebih bermakna untuk pelanggan daripada \"rata-rata pengiriman 1,4 hari\"."
],
"pts": [
"Median tahan terhadap outlier, rata-rata tidak.",
"Kuartil: Q1 (P25), median (P50), Q3 (P75).",
"IQR = Q3 - Q1.",
"Persentil seperti P90 cocok untuk janji layanan."
],
"q": [
[
"Data gaji karyawan dengan beberapa direktur bergaji sangat tinggi paling baik diringkas dengan?",
[
"Median",
"Rata-rata",
"Nilai maksimum"
],
0,
"Median tidak terdorong nilai ekstrem."
],
[
"\"P90 waktu kirim = 2 hari\" artinya?",
[
"90% pesanan sampai dalam 2 hari atau kurang",
"Rata-rata waktu kirim 2 hari",
"90 pesanan terlambat"
],
0,
"Persentil ke-90 membatasi 90% data."
]
],
"code": "import pandas as pd\npenjualan = pd.Series([120, 95, 130, 88, 2100, 101, 115, 99, 140, 105], name=\"omzet_ribu\")\nprint(\"rata-rata :\", penjualan.mean())\nprint(\"median    :\", penjualan.median())\nprint(\"Q1, Q3    :\", penjualan.quantile(0.25), penjualan.quantile(0.75))\nprint(\"P90       :\", round(penjualan.quantile(0.9), 1))",
"out": "rata-rata : 309.3\nmedian    : 110.0\nQ1, Q3    : 99.5 127.5\nP90       : 336.0"
}
},
{
"track": "da",
"module": "Membersihkan & mentransformasi data",
"lesson": {
"k": "c",
"t": "Menstandarkan data kotor dengan pandas",
"nodes": [
"Data Cleaning",
"Standardization"
],
"lang": "python",
"b": [
"Data dari formulir hampir selalu kotor: \"medan\", \"MEDAN \", dan \"Kota Medan\" adalah kota yang sama. Nomor HP ditulis \"0812-...\", \"+62812...\", atau dengan spasi. Kalau tidak distandarkan, hasil <code>groupby</code> akan terpecah.",
"Langkahnya: rapikan spasi dan huruf (<code>str.strip</code>, <code>str.title</code>), buang awalan yang tidak perlu dengan <code>str.replace</code> dan regex, lalu petakan variasi ke nilai baku dengan <code>replace</code> atau kamus.",
"Simpan aturan pembersihan sebagai fungsi agar bisa dijalankan ulang untuk data bulan berikutnya. Selalu bandingkan jumlah baris sebelum dan sesudah, dan catat nilai yang tidak bisa dibakukan."
],
"pts": [
"Rapikan spasi dan huruf sebelum mengelompokkan.",
"Regex untuk membuang karakter bukan angka.",
"Bakukan awalan seperti 0 / 62 menjadi +62.",
"Jadikan aturan pembersihan fungsi yang bisa diulang."
],
"q": [
[
"Kenapa \"medan\" dan \"MEDAN \" harus disamakan sebelum groupby?",
[
"Agar tidak dihitung sebagai dua kota berbeda",
"Agar file lebih kecil",
"Karena pandas tidak bisa membaca huruf kecil"
],
0,
"Nilai yang berbeda tulisan dianggap kategori berbeda."
],
[
"Apa fungsi str.replace(r\"\\D\", \"\", regex=True)?",
[
"Menghapus semua karakter yang bukan angka",
"Menghapus semua angka",
"Mengganti huruf D"
],
0,
"\\D cocok dengan karakter non-digit."
]
],
"code": "import pandas as pd\ndf = pd.DataFrame({\n    \"kota\": [\"medan\", \"MEDAN \", \"Kota Medan\", \"bandung\", \" Bandung\"],\n    \"hp\": [\"0812-3456-7890\", \"+62 812 3456 7891\", \"081234567892\", \"62812-3456-7893\", \"0812 3456 7894\"],\n})\ndf[\"kota\"] = df[\"kota\"].str.strip().str.title().str.replace(r\"^Kota \", \"\", regex=True)\ndf[\"hp\"] = df[\"hp\"].str.replace(r\"\\D\", \"\", regex=True).str.replace(r\"^(62|0)\", \"+62\", regex=True)\nprint(df.to_string(index=False))\nprint(df[\"kota\"].value_counts().to_dict())",
"out": "   kota             hp\n  Medan +6281234567890\n  Medan +6281234567891\n  Medan +6281234567892\nBandung +6281234567893\nBandung +6281234567894\n{'Medan': 3, 'Bandung': 2}"
}
},
{
"track": "da",
"module": "Visualisasi & alat BI",
"lesson": {
"k": "c",
"t": "Dari temuan ke rekomendasi",
"nodes": [
"Storytelling",
"Communication"
],
"lang": "text",
"b": [
"Analisis belum selesai sampai ada keputusan. Struktur yang sering dipakai analis: <b>Apa yang terjadi</b> (temuan dengan angka), <b>Kenapa penting</b> (dampak ke bisnis), dan <b>Apa yang disarankan</b> (tindakan yang bisa diuji).",
"Mulai dari kesimpulan, bukan proses. Manajer yang sibuk membaca kalimat pertama dan judul grafik. Judul grafik sebaiknya berupa kalimat temuan, misalnya \"Pembeli baru turun 18% sejak ongkir naik\", bukan \"Grafik pembeli per bulan\".",
"Sebutkan juga keterbatasan data dan tingkat keyakinanmu. Rekomendasi yang jujur tentang ketidakpastian lebih dipercaya daripada yang terdengar pasti tetapi keliru."
],
"pts": [
"Temuan → dampak → rekomendasi.",
"Mulai dari kesimpulan.",
"Judul grafik berupa kalimat temuan.",
"Sebutkan keterbatasan data."
],
"q": [
[
"Judul grafik yang paling baik?",
[
"Pembeli baru turun 18% sejak ongkir naik",
"Grafik pembeli per bulan",
"Data Mei"
],
0,
"Judul berupa temuan langsung menyampaikan pesan."
],
[
"Rekomendasi yang baik sebaiknya?",
[
"Spesifik dan bisa diuji, misalnya A/B test 2 minggu",
"Umum seperti \"tingkatkan penjualan\"",
"Tidak perlu ada"
],
0,
"Tindakan yang bisa diuji memudahkan keputusan."
]
],
"code": "Ringkasan untuk manajer (satu slide)\n\nJudul  : Pembeli baru turun 18% sejak ongkir minimum naik 1 Mei\nTemuan : Pembeli baru/minggu: 1.240 (April) -> 1.017 (Mei).\n         Penurunan terbesar di luar Jawa (-31%); pelanggan lama stabil (-2%).\nDampak : Bila berlanjut, omzet pelanggan baru berkurang ±Rp96 juta/bulan.\nSaran  : Uji A/B ongkir gratis untuk pesanan pertama di luar Jawa selama 2 minggu.\nCatatan: Mei punya libur panjang; bandingkan juga dengan Mei tahun lalu.",
"run": false
}
},
{
"track": "bi",
"module": "Metrik & KPI",
"lesson": {
"k": "c",
"t": "Leading vs lagging indicator",
"nodes": [
"KPIs",
"Metrics"
],
"lang": "text",
"b": [
"<b>Lagging indicator</b> mengukur hasil yang sudah terjadi: omzet bulan lalu, churn kuartal ini. Angkanya pasti, tetapi terlambat untuk diubah. <b>Leading indicator</b> bergerak lebih dulu dan memberi sinyal awal: jumlah keranjang dibuat, pengunjung yang menambahkan alamat, tiket keluhan minggu ini.",
"Dashboard yang baik memasangkan keduanya. Misalnya churn (lagging) ditemani jumlah pelanggan yang tidak login 14 hari (leading). Tim bisa bertindak, seperti mengirim pengingat, sebelum pelanggan benar-benar pergi.",
"Leading indicator perlu dibuktikan: periksa apakah perubahannya memang mendahului perubahan lagging indicator dengan data historis, bukan sekadar terdengar masuk akal."
],
"pts": [
"Lagging: hasil, pasti tetapi terlambat.",
"Leading: sinyal awal yang bisa ditindaklanjuti.",
"Pasangkan keduanya di dashboard.",
"Buktikan hubungan leading → lagging dengan data."
],
"q": [
[
"Mana yang leading indicator untuk churn?",
[
"Pelanggan yang tidak login 14 hari",
"Jumlah pelanggan yang berhenti bulan lalu",
"Omzet tahunan"
],
0,
"Ketidakaktifan muncul sebelum pelanggan berhenti."
],
[
"Kenapa leading indicator berguna?",
[
"Memberi waktu untuk bertindak sebelum hasil buruk terjadi",
"Lebih mudah dihitung",
"Selalu akurat"
],
0,
"Nilainya ada pada kesempatan untuk mengubah hasil."
]
],
"code": "KPI hasil (lagging)          Sinyal awal (leading)                         Tindakan\nOmzet bulanan                Keranjang dibuat per hari                     promo keranjang terbengkalai\nChurn pelanggan              Tidak login >= 14 hari                         kirim pengingat + voucher\nRating toko                  Pesanan terlambat dikirim > 2 hari             eskalasi ke gudang\nPelanggan baru               Pengunjung yang mendaftar akun                 perbaiki formulir daftar",
"run": false
}
},
{
"track": "bi",
"module": "SQL untuk BI",
"lesson": {
"k": "c",
"t": "Running total & perubahan bulan ke bulan",
"nodes": [
"Window Functions",
"Time Series"
],
"lang": "sql",
"b": [
"Dua pertanyaan yang hampir selalu muncul di laporan: \"berapa omzet kumulatif sampai bulan ini?\" dan \"naik atau turun berapa persen dibanding bulan lalu?\". Keduanya dijawab dengan <b>window function</b> tanpa subquery.",
"<code>SUM(...) OVER (ORDER BY bulan)</code> menjumlahkan dari baris pertama sampai baris saat ini, sehingga menghasilkan running total. <code>LAG(...) OVER (ORDER BY bulan)</code> mengambil nilai baris sebelumnya, lalu persentase perubahan dihitung dari keduanya.",
"Bungkus pembaginya dengan <code>NULLIF</code> agar bulan pertama atau bulan dengan omzet 0 tidak memicu pembagian dengan nol. Query di bawah dijalankan pada database skema bintang yang sama dengan pelajaran BI lainnya."
],
"pts": [
"SUM() OVER (ORDER BY ...) menghasilkan running total.",
"LAG() mengambil nilai periode sebelumnya.",
"NULLIF mencegah pembagian dengan nol.",
"CTE memisahkan agregasi dan perhitungan window."
],
"q": [
[
"Fungsi untuk mengambil omzet bulan sebelumnya?",
[
"LAG(omzet) OVER (ORDER BY bulan)",
"LEAD(omzet) OVER (ORDER BY bulan)",
"MAX(omzet)"
],
0,
"LAG melihat ke baris sebelumnya, LEAD ke baris berikutnya."
],
[
"Kenapa ubah_persen bulan pertama bernilai NULL?",
[
"Tidak ada bulan sebelumnya, jadi LAG menghasilkan NULL",
"Query salah",
"Omzetnya nol"
],
0,
"Operasi dengan NULL menghasilkan NULL."
]
],
"code": "WITH bulanan AS (\n  SELECT t.bulan, SUM(f.jumlah * f.harga) AS omzet\n  FROM fakta_penjualan f\n  JOIN dim_tanggal t ON t.tanggal_id = f.tanggal_id\n  GROUP BY t.bulan\n)\nSELECT bulan, omzet,\n       SUM(omzet) OVER (ORDER BY bulan) AS kumulatif,\n       ROUND(100.0 * (omzet - LAG(omzet) OVER (ORDER BY bulan))\n             / NULLIF(LAG(omzet) OVER (ORDER BY bulan), 0), 1) AS ubah_persen\nFROM bulanan\nORDER BY bulan;",
"out": "bulan | omzet    | kumulatif | ubah_persen\n------+----------+-----------+------------\n1     | 16780000 | 16780000  | NULL\n2     | 21550000 | 38330000  | 28.4\n3     | 24870000 | 63200000  | 15.4\n4     | 18300000 | 81500000  | -26.4\n5     | 22700000 | 104200000 | 24\n6     | 21750000 | 125950000 | -4.2"
}
},
{
"track": "bi",
"module": "Visualisasi & dashboard",
"lesson": {
"k": "c",
"t": "Warna, urutan & angka di dashboard",
"nodes": [
"Dashboard Design",
"Data Visualization"
],
"lang": "text",
"b": [
"Warna di dashboard punya tugas, bukan hiasan. Pakai satu warna netral untuk data biasa dan satu warna aksen untuk yang perlu diperhatikan. Merah dan hijau sebaiknya hanya untuk makna buruk dan baik, dan selalu ditemani tanda atau teks, karena sebagian orang buta warna merah-hijau.",
"Urutkan batang dari besar ke kecil kecuali kategorinya punya urutan alami (bulan, tingkat pendidikan). Mulai sumbu batang dari nol. Tampilkan angka dengan satuan yang mudah dibaca: \"Rp1,2 M\" lebih cepat dipahami daripada \"1.234.567.890\".",
"Letakkan KPI terpenting di kiri atas, karena mata pembaca mulai dari sana. Setiap KPI sebaiknya punya pembanding (target, periode lalu) agar angkanya bermakna."
],
"pts": [
"Satu warna netral + satu aksen.",
"Merah/hijau selalu ditemani tanda atau teks.",
"Urutkan batang dari besar ke kecil.",
"KPI utama di kiri atas dengan pembanding."
],
"q": [
[
"Kapan batang TIDAK diurutkan dari besar ke kecil?",
[
"Saat kategori punya urutan alami seperti bulan",
"Saat ada lebih dari 3 batang",
"Tidak pernah"
],
0,
"Urutan alami lebih mudah dipahami."
],
[
"Kenapa KPI perlu pembanding?",
[
"Agar terlihat apakah angka itu baik atau buruk",
"Agar dashboard penuh",
"Agar warnanya cocok"
],
0,
"Angka tunggal tanpa konteks sulit ditafsirkan."
]
],
"code": "Tata letak dashboard penjualan mingguan\n\n+--------------------------------------------------------------+\n| Omzet  Rp1,24 M  ▲ 8% vs minggu lalu | Pesanan 3.412 ▼ 2%    |\n| Target Rp1,30 M  (95%)               | Rata-rata Rp363 rb    |\n+------------------------------+-------------------------------+\n| Omzet per kota (urut besar)  | Tren 12 minggu (garis)        |\n| Medan     ███████████ 412 jt | menyorot minggu ini           |\n| Bandung   ████████    301 jt |                               |\n| Makassar  █████       198 jt |                               |\n+------------------------------+-------------------------------+\nWarna: abu-abu untuk data, biru untuk sorotan, merah hanya untuk di bawah target",
"run": false
}
},
{
"track": "fe0",
"module": "JavaScript dasar",
"lesson": {
"k": "c",
"t": "Perulangan: for, for...of & while",
"nodes": [
"Loops"
],
"lang": "js",
"b": [
"Perulangan menjalankan kode berulang kali. <code>for</code> klasik cocok saat kamu butuh nomor urut. <code>for...of</code> membaca isi array satu per satu dan lebih jarang salah karena tidak ada indeks yang perlu dijaga.",
"<code>while</code> dipakai saat jumlah putaran belum diketahui, misalnya menabung sampai target tercapai. Pastikan kondisinya suatu saat menjadi salah, kalau tidak program berputar selamanya.",
"<code>break</code> menghentikan perulangan, dan <code>continue</code> melompat ke putaran berikutnya. Untuk mengolah array menjadi array baru, method seperti <code>map</code> dan <code>filter</code> biasanya lebih rapi."
],
"pts": [
"for: saat butuh nomor urut.",
"for...of: membaca isi array tanpa indeks.",
"while: saat jumlah putaran belum diketahui.",
"break berhenti, continue melompat."
],
"q": [
[
"Perulangan yang paling cocok untuk \"menabung sampai target\"?",
[
"while",
"for...of",
"Tidak perlu perulangan"
],
0,
"Jumlah putarannya tergantung kapan target tercapai."
],
[
"Apa yang dilakukan continue?",
[
"Melompat ke putaran berikutnya",
"Menghentikan perulangan",
"Mengulang dari awal"
],
0,
"Sisa kode di putaran itu dilewati."
]
],
"code": "const keranjang = [\"kopi\", \"teh\", \"gula\"];\n\nfor (let i = 0; i < keranjang.length; i++) {\n  console.log(`${i + 1}. ${keranjang[i]}`);\n}\n\nfor (const barang of keranjang) {\n  if (barang === \"teh\") continue;\n  console.log(\"dikemas:\", barang);\n}\n\nlet tabungan = 0;\nlet minggu = 0;\nwhile (tabungan < 100_000) {\n  tabungan += 30_000;\n  minggu++;\n}\nconsole.log(`Target tercapai di minggu ke-${minggu}: Rp${tabungan}`);",
"out": "1. kopi\n2. teh\n3. gula\ndikemas: kopi\ndikemas: gula\nTarget tercapai di minggu ke-4: Rp120000"
}
},
{
"track": "fe0",
"module": "JavaScript dasar",
"lesson": {
"k": "c",
"t": "Menangani error dengan try...catch",
"nodes": [
"Error Handling"
],
"lang": "js",
"b": [
"Program bisa gagal karena hal di luar kendali: data JSON rusak, koneksi putus, atau masukan pengguna salah. Tanpa penanganan, satu error menghentikan seluruh skrip dan halaman bisa macet.",
"<code>try</code> membungkus kode yang mungkin gagal, <code>catch</code> menerima objek error, dan <code>finally</code> selalu dijalankan, cocok untuk mematikan indikator memuat. Kamu juga bisa melempar error sendiri dengan <code>throw new Error(\"pesan\")</code> saat data tidak masuk akal.",
"Tampilkan pesan yang dimengerti pengguna (\"Data gagal dimuat, coba lagi\"), dan simpan detail teknisnya di <code>console.error</code> untuk developer."
],
"pts": [
"try membungkus kode yang mungkin gagal.",
"catch menerima objek error (err.message).",
"finally selalu dijalankan.",
"throw untuk data yang tidak masuk akal."
],
"q": [
[
"Kapan blok finally dijalankan?",
[
"Selalu, baik terjadi error maupun tidak",
"Hanya jika terjadi error",
"Hanya jika tidak terjadi error"
],
0,
"finally cocok untuk membersihkan keadaan."
],
[
"Apa yang dicetak err.message untuk throw new Error(\"stok habis\")?",
[
"stok habis",
"Error",
"undefined"
],
0,
"message berisi teks yang diberikan saat membuat error."
]
],
"code": "function bacaKeranjang(teks) {\n  try {\n    const data = JSON.parse(teks);\n    if (!Array.isArray(data)) throw new Error(\"format keranjang salah\");\n    return data;\n  } catch (err) {\n    console.log(\"Gagal membaca keranjang:\", err.message);\n    return [];\n  } finally {\n    console.log(\"selesai memeriksa\");\n  }\n}\n\nconsole.log(bacaKeranjang('[\"kopi\",\"teh\"]'));\nconsole.log(bacaKeranjang(\"{rusak\"));\nconsole.log(bacaKeranjang('{\"kopi\": 1}'));",
"out": "selesai memeriksa\n[ 'kopi', 'teh' ]\nGagal membaca keranjang: Expected property name or '}' in JSON at position 1 (line 1 column 2)\nselesai memeriksa\n[]\nGagal membaca keranjang: format keranjang salah\nselesai memeriksa\n[]"
}
},
{
"track": "fe0",
"module": "JavaScript dasar",
"lesson": {
"k": "c",
"t": "Modul: import & export",
"nodes": [
"Modules"
],
"lang": "js",
"b": [
"Saat kode bertambah, satu berkas besar sulit dirawat. <b>Modul</b> memecahnya: setiap berkas punya tanggung jawab sendiri dan hanya membagikan yang perlu dengan <code>export</code>.",
"Ada dua jenis ekspor. <b>Named export</b> (<code>export function hitungTotal</code>) diimpor dengan nama yang sama di dalam kurung kurawal. <b>Default export</b> hanya satu per berkas dan boleh diberi nama apa saja saat diimpor.",
"Di browser, muat berkas utama dengan <code>&lt;script type=\"module\"&gt;</code>. Modul otomatis berjalan dalam mode ketat, variabelnya tidak bocor ke global, dan dijalankan setelah HTML selesai dibaca."
],
"pts": [
"export membagikan fungsi atau nilai dari berkas.",
"Named export diimpor dengan { nama }.",
"Default export satu per berkas, nama bebas.",
"Browser: <code>&lt;script type=\"module\"&gt;</code>."
],
"q": [
[
"Cara mengimpor named export rupiah?",
[
"import { rupiah } from \"./rupiah.js\"",
"import rupiah from \"./rupiah.js\"",
"require rupiah"
],
0,
"Named export memakai kurung kurawal dan nama yang sama."
],
[
"Berapa default export yang boleh ada di satu berkas?",
[
"Satu",
"Tidak terbatas",
"Dua"
],
0,
"Default export hanya satu per modul."
]
],
"code": "// berkas: rupiah.js\nexport function rupiah(angka) {\n  return \"Rp\" + angka.toLocaleString(\"id-ID\");\n}\nexport const PPN = 0.11;\n\n// berkas: keranjang.js\nimport { rupiah, PPN } from \"./rupiah.js\";\nexport default function total(barang) {\n  const sub = barang.reduce((t, b) => t + b.harga * b.qty, 0);\n  return rupiah(Math.round(sub * (1 + PPN)));\n}\n\n// berkas: main.js\nimport hitungTotal from \"./keranjang.js\";\nconsole.log(hitungTotal([{ harga: 85_000, qty: 2 }]));  // Rp188.700\n\n<!-- index.html -->\n<script type=\"module\" src=\"main.js\"></script>",
"run": false
}
},
{
"track": "ts",
"module": "Generics",
"lesson": {
"k": "c",
"t": "Constraint generik & tipe bawaan",
"nodes": [
"Generic Constraints",
"Generics"
],
"lang": "ts",
"b": [
"Generik tanpa batasan menerima tipe apa saja, sehingga TypeScript tidak tahu properti apa yang tersedia. <b>Constraint</b> dengan <code>extends</code> membatasinya: <code>&lt;T extends { harga: number }&gt;</code> berarti T boleh tipe apa pun asal punya properti <code>harga</code>.",
"<code>keyof</code> bisa dipakai sebagai constraint juga. <code>&lt;T, K extends keyof T&gt;</code> memastikan nama properti yang dikirim benar-benar ada pada objek, dan tipe hasilnya <code>T[K]</code> ikut tepat.",
"Parameter generik juga boleh punya <b>tipe bawaan</b> seperti <code>&lt;T = string&gt;</code>, dipakai saat pemanggil tidak menyebut tipenya dan TypeScript tidak bisa menebaknya."
],
"pts": [
"T extends {...} membatasi tipe yang diterima.",
"K extends keyof T menjamin nama properti valid.",
"T[K] memberi tipe hasil yang tepat.",
"Tipe bawaan: <code>&lt;T = string&gt;</code>."
],
"q": [
[
"Apa arti <code>&lt;T extends { harga: number }&gt;</code>?",
[
"T boleh tipe apa saja yang punya properti harga bertipe number",
"T harus number",
"T adalah salinan harga"
],
0,
"extends di generik berarti batasan."
],
[
"Kenapa ambil(teratas, \"warna\") ditolak?",
[
"\"warna\" bukan keyof tipe teratas",
"Fungsi tidak menerima string",
"teratas bernilai null"
],
0,
"K dibatasi pada nama properti yang ada."
]
],
"code": "function termahal<T extends { harga: number }>(daftar: T[]): T {\n  return daftar.reduce((a, b) => (b.harga > a.harga ? b : a));\n}\n\nfunction ambil<T, K extends keyof T>(obj: T, kunci: K): T[K] {\n  return obj[kunci];\n}\n\ntype Respons<T = string> = { ok: boolean; data: T };\n\nconst produk = [\n  { nama: \"Kopi Gayo\", harga: 85_000, stok: 40 },\n  { nama: \"Madu Hutan\", harga: 120_000, stok: 15 },\n];\nconst teratas = termahal(produk);\nconsole.log(teratas.nama);          // tipe teratas: { nama, harga, stok }\nconsole.log(ambil(teratas, \"stok\")); // ambil(teratas, \"warna\") ditolak compiler\nconst r: Respons = { ok: true, data: \"tersimpan\" };\nconsole.log(r.data.toUpperCase());",
"out": "Madu Hutan\n15\nTERSIMPAN"
}
},
{
"track": "ts",
"module": "Narrowing & assertion",
"lesson": {
"k": "c",
"t": "Validasi data dari API dengan type predicate",
"nodes": [
"Type Predicates",
"Narrowing"
],
"lang": "ts",
"b": [
"Data dari <code>fetch</code> atau <code>JSON.parse</code> tidak punya jaminan bentuk. Menulis <code>as Produk</code> hanya menenangkan compiler, bukan memeriksa data. Kalau server mengirim bentuk lain, error baru muncul jauh di bagian lain program.",
"<b>Type predicate</b> adalah fungsi yang mengembalikan <code>x is Produk</code>. Di dalamnya kamu memeriksa data sungguhan; di luar, TypeScript memakai hasilnya untuk mempersempit tipe. Gabungkan dengan <code>filter</code> untuk menyaring data yang valid saja.",
"Untuk skema besar, pustaka seperti Zod atau Valibot menulis pemeriksaan sekaligus tipe dari satu definisi."
],
"pts": [
"as Tipe tidak memeriksa data.",
"Type predicate: fungsi yang mengembalikan x is Tipe.",
"filter(isTipe) menyaring dan mempersempit tipe.",
"Skema besar: Zod atau Valibot."
],
"q": [
[
"Apa beda as Produk dan type predicate isProduk?",
[
"as tidak memeriksa apa pun; isProduk memeriksa data saat program berjalan",
"Keduanya sama",
"as lebih aman"
],
0,
"Assertion hanya berlaku saat kompilasi."
],
[
"Kenapa {\"nama\":\"Teh\",\"harga\":\"25rb\"} tidak lolos?",
[
"harga bertipe string, bukan number",
"nama terlalu pendek",
"JSON tidak valid"
],
0,
"Pemeriksaan typeof harga === number gagal."
]
],
"code": "type Produk = { nama: string; harga: number };\n\nfunction isProduk(x: unknown): x is Produk {\n  return typeof x === \"object\" && x !== null\n    && typeof (x as Produk).nama === \"string\"\n    && typeof (x as Produk).harga === \"number\";\n}\n\nconst dariServer: unknown = JSON.parse(\n  '[{\"nama\":\"Kopi\",\"harga\":85000},{\"nama\":\"Teh\",\"harga\":\"25rb\"},null]'\n);\nconst daftar = Array.isArray(dariServer) ? dariServer.filter(isProduk) : [];\nconsole.log(daftar.length, \"produk valid\");\nfor (const p of daftar) console.log(p.nama, p.harga * 2);",
"out": "1 produk valid\nKopi 170000"
}
},
{
"track": "ts",
"module": "Fungsi",
"lesson": {
"k": "c",
"t": "Fungsi orde tinggi & callback bertipe",
"nodes": [
"Function Types",
"Callbacks"
],
"lang": "ts",
"b": [
"Fungsi di TypeScript bisa diterima dan dikembalikan seperti nilai lain. Fungsi yang menerima atau mengembalikan fungsi disebut <b>fungsi orde tinggi</b>. Tipe fungsi ditulis seperti <code>(harga: number) =&gt; number</code>.",
"Memberi nama pada tipe fungsi dengan <code>type</code> membuat kode lebih mudah dibaca, misalnya <code>type Aturan = (harga: number) =&gt; number</code>. Fungsi yang mengembalikan fungsi lain sering dipakai untuk membuat aturan yang bisa dikonfigurasi, seperti diskon dengan persentase tertentu.",
"Saat callback dikirim ke <code>map</code> atau <code>filter</code>, TypeScript menebak tipe parameternya dari array, jadi kamu jarang perlu menuliskannya."
],
"pts": [
"Tipe fungsi: (param: Tipe) => Hasil.",
"Beri nama tipe fungsi dengan type.",
"Fungsi bisa mengembalikan fungsi yang sudah dikonfigurasi.",
"Tipe parameter callback ditebak dari konteks."
],
"q": [
[
"Kenapa dua pemanggilan terapkan menghasilkan angka berbeda?",
[
"Urutan aturan berbeda: diskon sebelum atau sesudah ongkir",
"Ada bug di reduce",
"Angka acak"
],
0,
"Diskon dari 115.000 berbeda dengan diskon dari 100.000."
],
[
"Tipe dari diskon(10)?",
[
"Aturan, yaitu (harga: number) => number",
"number",
"string"
],
0,
"diskon mengembalikan fungsi."
]
],
"code": "type Aturan = (harga: number) => number;\n\nconst diskon = (persen: number): Aturan => (harga) => harga * (1 - persen / 100);\nconst ongkir = (biaya: number): Aturan => (harga) => harga + biaya;\n\nfunction terapkan(harga: number, ...aturan: Aturan[]): number {\n  return aturan.reduce((h, f) => f(h), harga);\n}\n\nconsole.log(terapkan(100_000, diskon(10), ongkir(15_000)));\nconsole.log(terapkan(100_000, ongkir(15_000), diskon(10)));\nconst hargaAkhir = [50_000, 80_000].map(diskon(20));\nconsole.log(hargaAkhir);",
"out": "105000\n103500\n[ 40000, 64000 ]"
}
},
{
"track": "react",
"module": "Data dari server",
"lesson": {
"k": "c",
"t": "Empat keadaan data: memuat, error, kosong, ada",
"nodes": [
"Data Fetching",
"UI States"
],
"lang": "jsx",
"b": [
"Komponen yang mengambil data punya setidaknya empat keadaan: <b>memuat</b>, <b>error</b>, <b>kosong</b>, dan <b>ada data</b>. Pemula sering hanya menulis keadaan terakhir, sehingga pengguna melihat layar putih saat koneksi lambat atau saat belum ada data.",
"Tangani keempatnya secara eksplisit dan berurutan. Gunakan skeleton yang menyerupai bentuk isi agar layar tidak meloncat, pesan error yang bisa ditindaklanjuti dengan tombol coba lagi, dan empty state yang mengajak bertindak.",
"Pustaka seperti TanStack Query sudah menyediakan <code>isPending</code>, <code>isError</code>, dan <code>refetch</code>, sehingga kamu tinggal menampilkan setiap keadaan."
],
"pts": [
"Empat keadaan: memuat, error, kosong, ada data.",
"Skeleton mencegah layar meloncat.",
"Error disertai tombol coba lagi.",
"Empty state mengajak bertindak."
],
"q": [
[
"Apa yang terlihat pengguna jika keadaan memuat tidak ditangani?",
[
"Layar kosong atau error karena data belum ada",
"Data lama",
"Tidak ada bedanya"
],
0,
"Komponen mencoba merender data yang belum tersedia."
],
[
"Empty state yang baik berisi?",
[
"Penjelasan singkat dan aksi berikutnya",
"Teks \"null\"",
"Halaman putih"
],
0,
"Empty state adalah kesempatan mengarahkan pengguna."
]
],
"code": "function DaftarPesanan() {\n  const { data, isPending, isError, refetch } = useQuery({\n    queryKey: [\"pesanan\"],\n    queryFn: () => fetch(\"/api/pesanan\").then((r) => r.json()),\n  });\n\n  if (isPending) return <SkeletonList baris={3} />;\n  if (isError) return (\n    <div role=\"alert\">\n      Pesanan gagal dimuat. <button onClick={() => refetch()}>Coba lagi</button>\n    </div>\n  );\n  if (data.length === 0) return (\n    <EmptyState judul=\"Belum ada pesanan\" aksi={<a href=\"/katalog\">Mulai belanja</a>} />\n  );\n  return <ul>{data.map((p) => <li key={p.id}>{p.nomor}</li>)}</ul>;\n}",
"run": false
}
},
{
"track": "react",
"module": "Hooks",
"lesson": {
"k": "c",
"t": "useTransition & useDeferredValue: tetap responsif",
"nodes": [
"Concurrent Features",
"Hooks"
],
"lang": "jsx",
"b": [
"Saat pengguna mengetik di kotak pencarian yang menyaring ribuan produk, setiap ketukan memicu render berat dan input terasa tersendat. React 18 menyediakan dua hook untuk menandai pembaruan yang <b>tidak mendesak</b>.",
"<code>useDeferredValue(nilai)</code> mengembalikan versi nilai yang boleh tertinggal. Input tetap memakai nilai terbaru dan selalu responsif, sementara daftar berat memakai nilai yang ditunda. <code>useTransition</code> melakukan hal serupa untuk pembaruan state yang kamu picu sendiri, dan memberi <code>isPending</code> untuk indikator.",
"Ini bukan debounce: React tetap merender secepat mungkin, tetapi bisa menghentikan render lama jika ada ketukan baru. Ukur dulu dengan React DevTools Profiler sebelum menambahkan optimasi."
],
"pts": [
"useDeferredValue: nilai yang boleh tertinggal.",
"Input tetap responsif, daftar berat menyusul.",
"useTransition untuk pembaruan state tidak mendesak.",
"Ukur dengan Profiler sebelum mengoptimasi."
],
"q": [
[
"Kenapa input memakai kata dan daftar memakai kataTunda?",
[
"Agar input selalu responsif sementara daftar berat boleh tertinggal",
"Agar daftar lebih cepat dari input",
"Tidak ada alasan"
],
0,
"Pembaruan input diprioritaskan."
],
[
"Apa beda useDeferredValue dengan debounce?",
[
"Tidak ada jeda waktu tetap; React merender secepatnya dan bisa membatalkan render lama",
"Sama persis",
"useDeferredValue selalu menunggu 300 ms"
],
0,
"React yang mengatur prioritasnya."
]
],
"code": "function CariProduk({ semuaProduk }) {\n  const [kata, setKata] = useState(\"\");\n  const kataTunda = useDeferredValue(kata);\n  const hasil = useMemo(\n    () => semuaProduk.filter((p) => p.nama.toLowerCase().includes(kataTunda.toLowerCase())),\n    [semuaProduk, kataTunda]\n  );\n  const usang = kata !== kataTunda;\n\n  return (\n    <>\n      <input value={kata} onChange={(e) => setKata(e.target.value)} placeholder=\"Cari produk\" />\n      <ul style={{ opacity: usang ? 0.6 : 1 }}>\n        {hasil.map((p) => <li key={p.id}>{p.nama}</li>)}\n      </ul>\n    </>\n  );\n}",
"run": false
}
},
{
"track": "react",
"module": "Pola komponen",
"lesson": {
"k": "c",
"t": "Memecah komponen: kapan & bagaimana",
"nodes": [
"Component Design",
"Composition"
],
"lang": "jsx",
"b": [
"Komponen 400 baris yang mengambil data, mengatur form, dan menggambar tabel sulit diuji dan diubah. Pecah komponen saat ada bagian yang <b>dipakai ulang</b>, punya <b>tanggung jawab berbeda</b>, atau punya <b>state sendiri</b> yang tidak perlu diketahui induknya.",
"Pola yang sering dipakai: komponen induk mengurus data dan state, komponen anak hanya menerima props dan menampilkan. Komponen anak seperti ini mudah diuji dan bisa dipakai di Storybook.",
"Jangan memecah terlalu dini. Tiga baris JSX yang hanya muncul sekali tidak perlu menjadi komponen sendiri. Simpan state sedekat mungkin dengan komponen yang memakainya, dan naikkan hanya saat dua komponen saudara membutuhkannya."
],
"pts": [
"Pecah saat dipakai ulang, beda tanggung jawab, atau punya state sendiri.",
"Induk mengurus data, anak menampilkan.",
"Logika ke custom hook dan fungsi murni.",
"Jangan memecah terlalu dini; state sedekat mungkin."
],
"q": [
[
"Di mana sebaiknya state input kupon disimpan?",
[
"Di KotakKupon, karena hanya dipakai di sana",
"Di komponen paling atas aplikasi",
"Di localStorage"
],
0,
"State disimpan sedekat mungkin dengan pemakainya."
],
[
"Keuntungan memindahkan hitungTotal ke fungsi murni?",
[
"Bisa diuji tanpa merender komponen",
"Membuat aplikasi lebih berwarna",
"Wajib di React"
],
0,
"Fungsi murni mudah diuji dan dipakai ulang."
]
],
"code": "// Sebelum: satu komponen mengurus semuanya\nfunction HalamanKeranjang() { /* fetch, state kupon, tabel, ringkasan, tombol bayar ... 300 baris */ }\n\n// Sesudah: induk mengurus data, anak menampilkan\nfunction HalamanKeranjang() {\n  const { barang, ubahJumlah, hapus } = useKeranjang();   // custom hook\n  const total = hitungTotal(barang);                      // fungsi murni, mudah diuji\n  return (\n    <main>\n      <TabelKeranjang barang={barang} onUbah={ubahJumlah} onHapus={hapus} />\n      <KotakKupon />                                       {/* state kupon tinggal di sini */}\n      <Ringkasan total={total} />\n    </main>\n  );\n}",
"run": false
}
},
{
"track": "html",
"module": "Teks & pengelompokan",
"lesson": {
"k": "c",
"t": "details, summary & dialog: interaksi tanpa JavaScript",
"nodes": [
"Interactive Elements"
],
"lang": "html",
"b": [
"Beberapa interaksi umum sudah disediakan HTML. <code>&lt;details&gt;</code> dan <code>&lt;summary&gt;</code> membuat bagian yang bisa dibuka-tutup, misalnya FAQ, lengkap dengan dukungan keyboard dan pembaca layar. Atribut <code>name</code> yang sama pada beberapa details membuatnya saling menutup seperti akordeon.",
"<code>&lt;dialog&gt;</code> membuat jendela modal. Dibuka dengan <code>showModal()</code>, ia otomatis berada di atas halaman, menutup dengan tombol Esc, dan menahan fokus di dalamnya. Form dengan <code>method=\"dialog\"</code> di dalamnya menutup dialog saat dikirim.",
"Atribut <code>popover</code> (didukung browser utama sejak 2024) membuat menu atau tooltip yang ditutup saat klik di luar, tanpa satu baris JavaScript pun."
],
"pts": [
"details/summary: buka-tutup bawaan, aksesibel.",
"name yang sama: akordeon.",
"dialog + showModal(): modal dengan Esc dan fokus.",
"popover: menu yang ditutup saat klik di luar."
],
"q": [
[
"Elemen untuk FAQ yang bisa dibuka-tutup tanpa JavaScript?",
[
"details dan summary",
"div dan span",
"section"
],
0,
"details menyediakan perilaku buka-tutup."
],
[
"Apa yang terjadi saat form method=\"dialog\" dikirim?",
[
"Dialog tertutup",
"Halaman dimuat ulang",
"Data dikirim ke server"
],
0,
"method=dialog menutup dialog induknya."
]
],
"code": "<h2>Pertanyaan umum</h2>\n<details name=\"faq\" open>\n  <summary>Berapa lama pengiriman?</summary>\n  <p>2 sampai 4 hari kerja untuk Pulau Jawa.</p>\n</details>\n<details name=\"faq\">\n  <summary>Bisa bayar di tempat (COD)?</summary>\n  <p>Bisa untuk pesanan di bawah Rp1.000.000.</p>\n</details>\n\n<button popovertarget=\"menu-akun\">Akun ▾</button>\n<div id=\"menu-akun\" popover>\n  <a href=\"/pesanan\">Pesanan saya</a><br>\n  <a href=\"/keluar\">Keluar</a>\n</div>\n\n<button onclick=\"konfirmasi.showModal()\">Batalkan pesanan</button>\n<dialog id=\"konfirmasi\">\n  <form method=\"dialog\">\n    <p>Yakin membatalkan pesanan #1024?</p>\n    <button value=\"tidak\">Kembali</button>\n    <button value=\"ya\">Ya, batalkan</button>\n  </form>\n</dialog>",
"run": false
}
},
{
"track": "html",
"module": "Form",
"lesson": {
"k": "c",
"t": "Tipe input modern & datalist",
"nodes": [
"Input Types",
"Forms"
],
"lang": "html",
"b": [
"Memilih <code>type</code> yang tepat memberi banyak hal gratis. <code>type=\"email\"</code> memeriksa format email, <code>type=\"tel\"</code> menampilkan papan angka telepon di HP, <code>type=\"date\"</code> memberi pemilih tanggal, dan <code>type=\"range\"</code> membuat slider.",
"<code>inputmode</code> mengatur keyboard tanpa mengubah validasi, misalnya <code>inputmode=\"numeric\"</code> untuk kode OTP. <code>autocomplete</code> membantu browser dan pengelola kata sandi mengisi otomatis, misalnya <code>autocomplete=\"one-time-code\"</code> untuk OTP dari SMS.",
"<code>&lt;datalist&gt;</code> memberi saran sambil tetap mengizinkan isian bebas, cocok untuk nama kota. Untuk daftar yang wajib dipilih, tetap pakai <code>&lt;select&gt;</code>."
],
"pts": [
"type yang tepat memberi validasi dan keyboard yang sesuai.",
"inputmode mengatur keyboard tanpa validasi.",
"autocomplete=one-time-code untuk OTP.",
"datalist: saran dengan isian bebas."
],
"q": [
[
"Atribut agar HP menampilkan keyboard angka untuk OTP?",
[
"inputmode=\"numeric\"",
"type=\"text\"",
"size=\"6\""
],
0,
"inputmode menentukan jenis keyboard virtual."
],
[
"Beda datalist dan select?",
[
"datalist memberi saran tetapi isian bebas tetap boleh",
"Sama saja",
"select mengizinkan isian bebas"
],
0,
"select hanya menerima pilihan yang tersedia."
]
],
"code": "<form>\n  <label for=\"email\">Email</label>\n  <input id=\"email\" type=\"email\" autocomplete=\"email\" required>\n\n  <label for=\"otp\">Kode OTP</label>\n  <input id=\"otp\" inputmode=\"numeric\" autocomplete=\"one-time-code\" pattern=\"[0-9]{6}\" maxlength=\"6\">\n\n  <label for=\"kirim\">Tanggal kirim</label>\n  <input id=\"kirim\" type=\"date\" min=\"2026-11-01\">\n\n  <label for=\"budget\">Budget maksimal: <output id=\"nilai\">500000</output></label>\n  <input id=\"budget\" type=\"range\" min=\"50000\" max=\"2000000\" step=\"50000\" value=\"500000\"\n         oninput=\"nilai.value = this.value\">\n\n  <label for=\"kota\">Kota</label>\n  <input id=\"kota\" list=\"daftar-kota\" autocomplete=\"address-level2\">\n  <datalist id=\"daftar-kota\">\n    <option value=\"Medan\"><option value=\"Bandung\"><option value=\"Makassar\">\n  </datalist>\n</form>",
"run": false
}
},
{
"track": "html",
"module": "Aksesibilitas, SEO & performa",
"lesson": {
"k": "c",
"t": "Open Graph & data terstruktur",
"nodes": [
"SEO",
"Meta Tags"
],
"lang": "html",
"b": [
"Saat link dibagikan di WhatsApp atau media sosial, yang muncul adalah judul, deskripsi, dan gambar dari tag <b>Open Graph</b> (<code>og:title</code>, <code>og:description</code>, <code>og:image</code>). Tanpa tag ini, pratinjau link sering kosong atau mengambil teks acak.",
"<b>Data terstruktur</b> dengan format JSON-LD dan kosakata schema.org menjelaskan isi halaman kepada mesin pencari: ini produk dengan harga sekian, ini artikel oleh penulis tertentu, ini kursus. Google memakainya untuk hasil penelusuran yang lebih kaya.",
"Tambahkan juga <code>&lt;link rel=\"canonical\"&gt;</code> agar halaman yang bisa diakses lewat beberapa URL dianggap satu halaman. Periksa hasilnya dengan Rich Results Test dari Google."
],
"pts": [
"Open Graph mengatur pratinjau saat link dibagikan.",
"og:image ideal 1200×630 piksel.",
"JSON-LD + schema.org menjelaskan isi ke mesin pencari.",
"canonical menyatukan URL ganda."
],
"q": [
[
"Tag yang menentukan gambar pratinjau link di WhatsApp?",
[
"og:image",
"img alt",
"favicon"
],
0,
"Aplikasi chat membaca tag Open Graph."
],
[
"Apa fungsi link rel=\"canonical\"?",
[
"Menunjuk URL utama agar halaman ganda dianggap satu",
"Mempercepat halaman",
"Menambah gambar"
],
0,
"Mesin pencari menggabungkan sinyal ke URL kanonis."
]
],
"code": "<head>\n  <title>Kopi Gayo 250 g · Toko Nusantara</title>\n  <meta name=\"description\" content=\"Kopi arabika Gayo sangrai medium, 250 gram. Dikirim dari Aceh.\">\n  <link rel=\"canonical\" href=\"https://toko.contoh.id/produk/kopi-gayo\">\n\n  <meta property=\"og:type\" content=\"product\">\n  <meta property=\"og:title\" content=\"Kopi Gayo 250 g\">\n  <meta property=\"og:description\" content=\"Arabika Gayo sangrai medium. Rp85.000\">\n  <meta property=\"og:image\" content=\"https://toko.contoh.id/img/kopi-gayo-1200x630.jpg\">\n\n  <script type=\"application/ld+json\">\n  {\n    \"@context\": \"https://schema.org\",\n    \"@type\": \"Product\",\n    \"name\": \"Kopi Gayo 250 g\",\n    \"offers\": { \"@type\": \"Offer\", \"price\": 85000, \"priceCurrency\": \"IDR\",\n                \"availability\": \"https://schema.org/InStock\" }\n  }\n  </script>\n</head>",
"run": false
}
},
{
"track": "pda",
"module": "Transformasi & penggabungan",
"lesson": {
"k": "c",
"t": "Rantai transformasi dengan assign & pipe",
"nodes": [
"Method Chaining",
"Data Transformation"
],
"lang": "python",
"b": [
"Kode analisis sering penuh variabel sementara: <code>df2</code>, <code>df3</code>, <code>df_final</code>. <b>Method chaining</b> menyusun langkah-langkah sebagai satu rangkaian yang dibaca dari atas ke bawah, dibungkus tanda kurung.",
"<code>assign</code> menambah kolom baru tanpa mengubah DataFrame asli, dan bisa menerima lambda yang merujuk kolom hasil langkah sebelumnya. <code>query</code> menyaring dengan teks yang mudah dibaca, dan <code>pipe</code> menyisipkan fungsi buatan sendiri ke dalam rantai.",
"Rantai yang terlalu panjang juga sulit dibaca. Pecah menjadi fungsi bernama bila lebih dari 6 sampai 8 langkah."
],
"pts": [
"Method chaining: langkah dibaca dari atas ke bawah.",
"assign menambah kolom tanpa mengubah aslinya.",
"query untuk filter yang mudah dibaca.",
"pipe menyisipkan fungsi sendiri."
],
"q": [
[
"Kenapa assign memakai lambda d: d[\"harga\"] * d[\"qty\"]?",
[
"Agar merujuk DataFrame pada langkah itu di dalam rantai",
"Karena assign tidak menerima angka",
"Agar lebih lambat"
],
0,
"Lambda menerima DataFrame hasil langkah sebelumnya."
],
[
"Fungsi untuk menyisipkan fungsi buatan sendiri ke rantai?",
[
"pipe",
"apply",
"map"
],
0,
"pipe(f, ...) memanggil f(df, ...)."
]
],
"code": "import pandas as pd\npesanan = pd.DataFrame({\n    \"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\", \"Medan\"],\n    \"harga\": [85000, 25000, 25000, 85000, 85000, 18000],\n    \"qty\": [2, 4, 1, 3, 1, 5],\n})\n\ndef tandai_besar(df, batas):\n    return df.assign(besar=df[\"total\"] >= batas)\n\nringkas = (\n    pesanan\n    .assign(total=lambda d: d[\"harga\"] * d[\"qty\"])\n    .query(\"qty >= 2\")\n    .pipe(tandai_besar, batas=150_000)\n    .groupby(\"kota\", as_index=False)[\"total\"].sum()\n    .sort_values(\"total\", ascending=False)\n)\nprint(ringkas.to_string(index=False))",
"out": "   kota  total\n  Medan 260000\n  Ambon 255000\nBandung 100000"
}
},
{
"track": "pda",
"module": "Statistik & EDA",
"lesson": {
"k": "c",
"t": "Deret waktu: resample & rolling",
"nodes": [
"Time Series",
"Resampling"
],
"lang": "python",
"b": [
"Data transaksi harian sering perlu diringkas per minggu atau per bulan. Jadikan kolom tanggal sebagai indeks, lalu <code>resample(\"W\")</code> atau <code>resample(\"ME\")</code> mengelompokkan berdasarkan periode waktu, mirip <code>groupby</code> untuk tanggal.",
"<code>rolling(3)</code> membuat jendela bergeser, misalnya rata-rata 3 hari terakhir. Rata-rata bergerak menghaluskan naik-turun harian sehingga tren lebih mudah terlihat. Tiga baris pertama bernilai kosong karena jendelanya belum penuh, kecuali kamu menetapkan <code>min_periods</code>.",
"<code>pct_change()</code> menghitung perubahan persen dari periode sebelumnya, berguna untuk melihat pertumbuhan."
],
"pts": [
"Tanggal sebagai indeks, lalu resample per periode.",
"rolling(n) untuk jendela bergeser.",
"Rata-rata bergerak menghaluskan data harian.",
"pct_change() untuk pertumbuhan."
],
"q": [
[
"Kenapa rolling(3).mean() menghasilkan NaN di dua baris pertama?",
[
"Jendela 3 hari belum penuh",
"Datanya salah",
"pandas tidak bisa menghitung"
],
0,
"Atur min_periods jika ingin tetap dihitung."
],
[
"resample(\"W\").sum() menghasilkan?",
[
"Jumlah omzet per minggu",
"Rata-rata harian",
"Jumlah baris"
],
0,
"resample mengelompokkan berdasarkan periode waktu."
]
],
"code": "import pandas as pd\ndf = pd.DataFrame({\"tanggal\": pd.date_range(\"2024-01-01\", periods=10, freq=\"D\"), \"omzet\": [120, 95, 130, 88, 150, 101, 115, 99, 140, 105]})\nharian = df.set_index(\"tanggal\")[\"omzet\"]\nprint(harian.resample(\"W\").sum().to_string())\nprint(harian.rolling(3).mean().round(1).tolist())\nprint((harian.pct_change() * 100).round(1).head(4).tolist())",
"out": "tanggal\n2024-01-07    799\n2024-01-14    344\nFreq: W-SUN\n[nan, nan, 115.0, 104.3, 122.7, 113.0, 122.0, 105.0, 118.0, 114.7]\n[nan, -20.8, 36.8, -32.3]"
}
},
{
"track": "pda",
"module": "Dasar Python untuk data",
"lesson": {
"k": "c",
"t": "Membaca file besar per potongan",
"nodes": [
"File I/O",
"Memory"
],
"lang": "python",
"b": [
"File CSV berukuran beberapa gigabyte bisa melebihi memori laptop. <code>pd.read_csv(..., chunksize=n)</code> membaca file per potongan n baris, sehingga kamu bisa mengolah lalu membuang setiap potongan.",
"Polanya: hitung ringkasan per potongan, simpan di list, lalu gabungkan di akhir. Untuk jumlah dan hitungan, menjumlahkan hasil per potongan memberi hasil yang sama dengan membaca seluruh file.",
"Hemat memori juga dengan <code>usecols</code> (hanya kolom yang perlu) dan <code>dtype</code> yang tepat, misalnya <code>category</code> untuk kolom kota yang nilainya berulang. Untuk data yang sangat besar, pertimbangkan Polars atau DuckDB."
],
"pts": [
"chunksize membaca file per potongan.",
"Ringkas per potongan, gabungkan di akhir.",
"usecols dan dtype menghemat memori.",
"Data sangat besar: Polars atau DuckDB."
],
"q": [
[
"Kenapa hasil penjumlahan per potongan tetap benar?",
[
"Jumlah dari jumlah-jumlah bagian sama dengan jumlah total",
"pandas menyimpan seluruh file diam-diam",
"Kebetulan saja"
],
0,
"Penjumlahan bisa dipecah lalu digabung."
],
[
"Ringkasan mana yang TIDAK bisa digabung dengan menjumlahkan hasil per potongan?",
[
"Median",
"Jumlah",
"Hitungan baris"
],
0,
"Median butuh melihat semua nilai sekaligus."
]
],
"code": "import pandas as pd, io\ncsv = \"kota,total\\n\" + \"\\n\".join(f\"{k},{t}\" for k, t in\n       [(\"Medan\", 120), (\"Bandung\", 90), (\"Medan\", 45), (\"Ambon\", 70), (\"Bandung\", 30), (\"Medan\", 60), (\"Ambon\", 25)])\n\nbagian = []\nfor potongan in pd.read_csv(io.StringIO(csv), chunksize=3, usecols=[\"kota\", \"total\"]):\n    print(\"potongan\", len(potongan), \"baris\")\n    bagian.append(potongan.groupby(\"kota\")[\"total\"].sum())\n\nhasil = pd.concat(bagian).groupby(level=0).sum()\nprint(hasil.to_dict())",
"out": "potongan 3 baris\npotongan 3 baris\npotongan 1 baris\n{'Ambon': 95, 'Bandung': 120, 'Medan': 225}"
}
},
{
"track": "de",
"module": "Ingestion & pipeline",
"lesson": {
"k": "c",
"t": "Kontrak data & validasi skema",
"nodes": [
"Data Quality",
"Schema Validation"
],
"lang": "python",
"b": [
"Pipeline sering rusak bukan karena kodenya, tetapi karena data sumber berubah diam-diam: kolom berganti nama, angka dikirim sebagai teks, nilai kosong muncul. <b>Kontrak data</b> adalah kesepakatan tertulis antara tim penghasil dan pemakai data tentang skema, arti kolom, dan aturan kualitasnya.",
"Kontrak itu diperiksa otomatis di awal pipeline. Baris yang melanggar dipisahkan ke tabel karantina beserta alasannya, bukan diam-diam dibuang atau dibiarkan merusak laporan.",
"Alat yang sering dipakai: Great Expectations, Soda, atau dbt tests. Contoh di bawah menulis pemeriksaan sederhana dengan Python biasa agar idenya terlihat jelas."
],
"pts": [
"Kontrak data: skema, arti, dan aturan kualitas yang disepakati.",
"Periksa di awal pipeline.",
"Baris salah ke karantina beserta alasannya.",
"Alat: Great Expectations, Soda, dbt tests."
],
"q": [
[
"Apa yang sebaiknya dilakukan pada baris yang melanggar kontrak?",
[
"Pisahkan ke karantina dengan alasannya",
"Buang diam-diam",
"Biarkan masuk ke laporan"
],
0,
"Karantina menjaga laporan tetap benar dan masalah bisa ditelusuri."
],
[
"Kenapa pesanan 4 masuk karantina?",
[
"Kolom total tidak ada",
"Kota tidak valid",
"id negatif"
],
0,
"Kolom wajib yang hilang melanggar kontrak."
]
],
"code": "KONTRAK = {\n    \"id_pesanan\": lambda v: isinstance(v, int) and v > 0,\n    \"kota\": lambda v: isinstance(v, str) and v.strip() != \"\",\n    \"total\": lambda v: isinstance(v, (int, float)) and v >= 0,\n}\n\nmasuk = [\n    {\"id_pesanan\": 1, \"kota\": \"Medan\", \"total\": 120000},\n    {\"id_pesanan\": 2, \"kota\": \"\", \"total\": 90000},\n    {\"id_pesanan\": 3, \"kota\": \"Ambon\", \"total\": \"45rb\"},\n    {\"id_pesanan\": 4, \"kota\": \"Bandung\"},\n]\n\nlolos, karantina = [], []\nfor baris in masuk:\n    salah = [k for k, cek in KONTRAK.items() if k not in baris or not cek(baris[k])]\n    (karantina if salah else lolos).append((baris[\"id_pesanan\"], salah))\n\nprint(\"lolos    :\", [i for i, _ in lolos])\nprint(\"karantina:\", karantina)",
"out": "lolos    : [1]\nkarantina: [(2, ['kota']), (3, ['total']), (4, ['total'])]"
}
},
{
"track": "de",
"module": "Pemodelan & arsitektur penyimpanan",
"lesson": {
"k": "c",
"t": "Format kolom & partisi: Parquet",
"nodes": [
"File Formats",
"Partitioning"
],
"lang": "text",
"b": [
"CSV mudah dibaca manusia, tetapi lambat dan boros untuk analitik: setiap kueri harus membaca seluruh baris, dan tipe datanya hilang. <b>Parquet</b> menyimpan data per kolom dengan kompresi dan skema, sehingga kueri yang hanya butuh dua kolom cukup membaca dua kolom itu.",
"<b>Partisi</b> membagi data ke folder berdasarkan kolom yang sering difilter, biasanya tanggal: <code>tahun=2024/bulan=05/</code>. Mesin kueri seperti Spark, DuckDB, atau BigQuery melewati folder yang tidak relevan (partition pruning).",
"Hati-hati dengan terlalu banyak partisi kecil: ribuan file berukuran beberapa kilobyte justru memperlambat. Targetkan file sekitar 128 MB sampai 1 GB, dan pilih kolom partisi dengan jumlah nilai yang wajar."
],
"pts": [
"Parquet: per kolom, terkompresi, menyimpan skema.",
"Kueri hanya membaca kolom yang dibutuhkan.",
"Partisi per tanggal memungkinkan partition pruning.",
"Hindari terlalu banyak file kecil."
],
"q": [
[
"Kenapa Parquet lebih cepat dari CSV untuk SELECT dua kolom?",
[
"Data disimpan per kolom, jadi kolom lain tidak dibaca",
"Parquet berisi lebih sedikit baris",
"CSV tidak bisa dibaca DuckDB"
],
0,
"Penyimpanan kolom membaca hanya yang diperlukan."
],
[
"Apa itu partition pruning?",
[
"Melewati folder partisi yang tidak cocok dengan filter",
"Menghapus partisi lama",
"Mengompresi file"
],
0,
"Mesin kueri tidak membaca data yang pasti tidak relevan."
]
],
"code": "# menulis data penjualan sebagai Parquet berpartisi (pandas + pyarrow)\ndf.to_parquet(\"gudang/penjualan\", partition_cols=[\"tahun\", \"bulan\"], index=False)\n\n# struktur yang dihasilkan\ngudang/penjualan/\n  tahun=2024/bulan=4/part-0.parquet\n  tahun=2024/bulan=5/part-0.parquet\n  tahun=2024/bulan=6/part-0.parquet\n\n-- DuckDB hanya membaca folder bulan=5 dan dua kolom\nSELECT kota, SUM(total) AS omzet\nFROM read_parquet('gudang/penjualan/*/*/*.parquet', hive_partitioning = true)\nWHERE tahun = 2024 AND bulan = 5\nGROUP BY kota;",
"run": false
}
},
{
"track": "de",
"module": "Kualitas, tata kelola & keamanan",
"lesson": {
"k": "c",
"t": "Lineage & katalog data",
"nodes": [
"Data Governance",
"Data Lineage"
],
"lang": "text",
"b": [
"Saat angka di dashboard terlihat aneh, pertanyaan pertama adalah: dari mana angka ini berasal? <b>Data lineage</b> mencatat alur data dari sumber, melalui setiap transformasi, sampai ke laporan. Dengan lineage, tim bisa menelusuri penyebab masalah dan tahu laporan mana yang terdampak sebelum mengubah sebuah tabel.",
"<b>Katalog data</b> adalah \"perpustakaan\" untuk tabel: deskripsi kolom, pemilik, tingkat sensitivitas (misalnya data pribadi menurut UU PDP), jadwal pembaruan, dan lineage-nya. Contoh alat: DataHub, OpenMetadata, dan katalog bawaan platform cloud.",
"dbt otomatis membuat lineage dari referensi <code>ref()</code> di model SQL-nya, sehingga dokumentasi tidak tertinggal dari kode."
],
"pts": [
"Lineage: jejak data dari sumber ke laporan.",
"Analisis dampak sebelum mengubah tabel.",
"Katalog: deskripsi, pemilik, sensitivitas, jadwal.",
"dbt membuat lineage dari ref()."
],
"q": [
[
"Manfaat lineage saat tabel staging akan diubah?",
[
"Mengetahui laporan mana yang terdampak",
"Membuat tabel lebih cepat",
"Mengenkripsi data"
],
0,
"Lineage menunjukkan semua turunan sebuah tabel."
],
[
"Informasi apa yang sebaiknya ada di katalog data?",
[
"Pemilik, deskripsi kolom, sensitivitas, jadwal pembaruan",
"Kata sandi database",
"Isi seluruh tabel"
],
0,
"Katalog membantu orang menemukan dan memahami data."
]
],
"code": "Lineage untuk KPI \"Omzet bersih\"\n\naplikasi_kasir.transaksi  (sumber, PostgreSQL)\n        |  ingest harian 02.00 (Airbyte)\n        v\nmentah.transaksi          (gudang, apa adanya)\n        |  dbt: stg_transaksi  (bersihkan tipe, buang uji coba)\n        v\nstaging.stg_transaksi\n        |  dbt: fct_penjualan  (join produk, hitung diskon)\n        v\nmart.fct_penjualan  --->  Dashboard \"Penjualan Mingguan\"\n                     --->  Laporan keuangan bulanan\n\nKatalog: fct_penjualan · pemilik: tim data komersial · berisi data pribadi: tidak\n         diperbarui: harian 03.00 · uji: unik(id_transaksi), not_null(total)",
"run": false
}
},
{
"track": "fe",
"module": "JavaScript",
"lesson": {
"k": "c",
"t": "Closure: fungsi yang mengingat",
"nodes": [
"Closures",
"Scope"
],
"lang": "js",
"b": [
"<b>Closure</b> terjadi saat fungsi dibuat di dalam fungsi lain dan tetap bisa memakai variabel fungsi luar, bahkan setelah fungsi luar selesai dijalankan. Variabel itu \"terkunci\" bersama fungsinya.",
"Closure dipakai di mana-mana: event handler yang mengingat id produk, fungsi pabrik seperti <code>buatPenghitung()</code>, sampai hook React. Ia juga cara sederhana membuat data privat, karena variabel di dalamnya tidak bisa diubah dari luar kecuali lewat fungsi yang disediakan.",
"Jebakan klasik: <code>var</code> di dalam loop berbagi satu variabel untuk semua putaran, sehingga semua callback melihat nilai terakhir. <code>let</code> membuat variabel baru di setiap putaran."
],
"pts": [
"Closure: fungsi membawa variabel lingkup luarnya.",
"Dipakai untuk handler, pabrik fungsi, data privat.",
"var di loop berbagi satu variabel.",
"let membuat variabel baru per putaran."
],
"q": [
[
"Kenapa k.isi bernilai undefined?",
[
"isi adalah variabel di dalam closure, bukan properti objek",
"Keranjang kosong",
"Ada error"
],
0,
"Variabel closure bersifat privat."
],
[
"Kenapa pakaiVar menghasilkan [3, 3, 3]?",
[
"Semua fungsi berbagi satu variabel i yang akhirnya bernilai 3",
"Karena map salah",
"var selalu bernilai 3"
],
0,
"var tidak membuat variabel baru per putaran."
]
],
"code": "function buatKeranjang() {\n  let isi = [];                       // privat, tidak bisa diakses langsung\n  return {\n    tambah(barang) { isi.push(barang); return isi.length; },\n    lihat() { return [...isi]; },\n  };\n}\nconst k = buatKeranjang();\nk.tambah(\"kopi\");\nk.tambah(\"teh\");\nconsole.log(k.lihat(), k.isi);\n\nconst pakaiVar = [], pakaiLet = [];\nfor (var i = 0; i < 3; i++) pakaiVar.push(() => i);\nfor (let j = 0; j < 3; j++) pakaiLet.push(() => j);\nconsole.log(pakaiVar.map((f) => f()), pakaiLet.map((f) => f()));",
"out": "[ 'kopi', 'teh' ] undefined\n[ 3, 3, 3 ] [ 0, 1, 2 ]"
}
},
{
"track": "fe",
"module": "Performa & aksesibilitas",
"lesson": {
"k": "c",
"t": "Debounce & throttle",
"nodes": [
"Performance",
"Events"
],
"lang": "js",
"b": [
"Event seperti <code>input</code>, <code>scroll</code>, dan <code>resize</code> bisa terpicu puluhan kali per detik. Kalau setiap event memanggil API pencarian, server kebanjiran dan hasilnya datang tidak berurutan.",
"<b>Debounce</b> menunggu sampai event berhenti selama jeda tertentu, lalu menjalankan fungsi sekali. Cocok untuk kotak pencarian: kirim permintaan 300 ms setelah pengguna berhenti mengetik. <b>Throttle</b> menjalankan fungsi paling banyak sekali per selang waktu, cocok untuk scroll atau menyimpan posisi.",
"Contoh di bawah mensimulasikan 5 ketukan cepat lalu jeda. Debounce hanya mencari sekali dengan kata terakhir."
],
"pts": [
"Debounce: jalankan sekali setelah event berhenti.",
"Throttle: paling banyak sekali per selang waktu.",
"Pencarian: debounce ±300 ms.",
"Scroll/resize: throttle atau requestAnimationFrame."
],
"q": [
[
"Teknik untuk kotak pencarian yang memanggil API?",
[
"Debounce",
"Throttle 0 ms",
"Panggil setiap ketukan"
],
0,
"Permintaan dikirim setelah pengguna berhenti mengetik."
],
[
"Kenapa clearTimeout dipanggil di setiap event?",
[
"Membatalkan jadwal sebelumnya agar hanya event terakhir yang dijalankan",
"Mempercepat timer",
"Menghapus event listener"
],
0,
"Itulah inti debounce."
]
],
"code": "function debounce(fn, ms) {\n  let t;\n  return (...args) => {\n    clearTimeout(t);\n    t = setTimeout(() => fn(...args), ms);\n  };\n}\n\nconst panggilan = [];\nconst cari = debounce((kata) => {\n  panggilan.push(kata);\n  console.log(\"cari ke server:\", kata);\n}, 300);\n\n[\"k\", \"ko\", \"kop\", \"kopi\", \"kopi g\"].forEach((kata, i) => setTimeout(() => cari(kata), i * 50));\nsetTimeout(() => console.log(\"jumlah panggilan:\", panggilan.length), 700);",
"out": "cari ke server: kopi g\njumlah panggilan: 1"
}
}
];
const M={html:HTML_MODULES,css:CSS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES,react:REACT_MODULES,ts:TS_MODULES,git:GIT_MODULES,pda:PDA_MODULES,da:DA_MODULES,bi:BI_MODULES,de:DE_MODULES,ux:UX_MODULES,ds:DS_MODULES};
for(const {track,module,lesson} of MORE){const m=(M[track]||[]).find(x=>x.t===module);
  if(!m)throw new Error('more: modul tidak ditemukan: '+track+' / '+module);m.lessons.push(lesson)}
})();
