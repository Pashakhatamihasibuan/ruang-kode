/* ===================== LATIHAN ALGORITMA PER BAHASA =====================
   Dibuat oleh tools/gen/algo/gen.py (jalankan dari folder itu). Modul ditambahkan di AKHIR jalur agar alamat pelajaran lama tidak bergeser.
   Semua kode dan keluaran sudah dijalankan (Java 21, Python 3, Node 22). */
(()=>{
const ALGO={
"java": {
"t": "Format keluaran dan latihan algoritma",
"lvl": "Menengah",
"d": "Format specifier, Fibonacci, bubble sort, FizzBuzz, bilangan prima, palindrom, dan binary search di Java, dengan alasan memilih for, while, do-while, atau for-each.",
"nodes": [
"Loops",
"Arrays"
],
"lessons": [
{
"k": "c",
"t": "Format specifier: merapikan keluaran",
"nodes": [
"Basic Syntax"
],
"lang": "java",
"b": [
"<b>Format specifier</b> adalah kode kecil yang mengatur <b>bagaimana sebuah nilai ditampilkan</b>: berapa angka di belakang koma, selebar apa kolomnya, rata kiri atau kanan, diberi nol di depan, atau diberi pemisah ribuan. Nilainya tidak berubah, hanya tampilannya. Hampir semua program nyata membutuhkannya: struk belanja, laporan nilai, nomor invoice, dan log server.",
"Polanya mirip di semua bahasa: <b>[perataan][lebar][.presisi][tipe]</b>. Contoh <code>%-10s</code> berarti teks rata kiri selebar 10, <code>%8.2f</code> berarti desimal 2 angka dalam kolom selebar 8, dan <code>%05d</code> berarti bilangan bulat selebar 5 yang diisi nol di depan.",
"Di Java, pakai <code>System.out.printf(...)</code> untuk langsung mencetak, atau <code>String.format(...)</code> untuk menghasilkan teks (misalnya kode invoice). <code>%n</code> adalah baris baru yang benar di semua sistem operasi, dan <code>%%</code> mencetak tanda persen. Jumlah dan tipe argumen harus cocok: <code>%d</code> dengan nilai double akan error <code>IllegalFormatConversionException</code> saat program berjalan.",
"Pemisah ribuan <code>%,d</code> mengikuti <b>lokal</b> komputer. Untuk format Indonesia (titik sebagai pemisah ribuan) tulis <code>String.format(Locale.forLanguageTag(\"id-ID\"), \"%,d\", 7500000)</code>, yang menghasilkan 7.500.000.",
"Contoh terakhir di kode adalah <b>struk belanja</b>: format di dalam loop membuat setiap baris punya lebar kolom yang sama, sehingga angka tersusun rapi ke kanan. Ini pola yang akan sering kamu pakai di soal-soal berikutnya."
],
"tb": [
{
"c": "Format specifier di berbagai bahasa",
"h": [
"Tujuan",
"Java / C (printf)",
"Python (f-string)",
"JavaScript / TypeScript"
],
"r": [
[
"Teks",
"%s",
"{x}",
"${x}"
],
[
"Bilangan bulat",
"%d",
"{x:d}",
"${x}"
],
[
"Desimal 2 angka",
"%.2f",
"{x:.2f}",
"x.toFixed(2)"
],
[
"Lebar 8, rata kanan",
"%8s",
"{x:>8}",
"String(x).padStart(8)"
],
[
"Lebar 8, rata kiri",
"%-8s",
"{x:<8}",
"String(x).padEnd(8)"
],
[
"Isi nol di depan",
"%05d",
"{x:05d}",
"String(x).padStart(5, \"0\")"
],
[
"Pemisah ribuan",
"%,d",
"{x:,}",
"x.toLocaleString(\"id-ID\")"
],
[
"Persen",
"%.0f%%",
"{x:.0%}",
"(x * 100).toFixed(0) + \"%\""
],
[
"Heksadesimal",
"%x",
"{x:x}",
"x.toString(16)"
],
[
"Notasi ilmiah",
"%.3e",
"{x:.3e}",
"x.toExponential(3)"
],
[
"Baris baru",
"%n atau \\n",
"\\n",
"\\n"
]
]
},
{
"c": "Yang paling sering dipakai di industri",
"h": [
"Kebutuhan",
"Pilihan umum",
"Alasan"
],
"r": [
[
"Menyusun teks di kode baru",
"f-string (Python), template literal (JS/TS), String.format atau formatted() (Java)",
"Paling mudah dibaca dan dirawat"
],
[
"Angka dan uang ke pengguna",
"Format berbasis lokal: Intl.NumberFormat, Locale id-ID, Babel",
"Titik, koma, dan simbol Rp mengikuti aturan negara"
],
[
"Laporan dan struk berkolom",
"Lebar + perataan: %-12s, %10.2f, padEnd/padStart",
"Kolom tetap lurus berapa pun panjang datanya"
],
[
"Kode dokumen dan antrean",
"Isi nol: %04d, {n:04d}",
"INV-0007 lebih mudah diurutkan dan dicari"
],
[
"Logging",
"Placeholder %s atau {}: logger.info(\"user %s\", id)",
"Teks hanya disusun jika log benar-benar dicetak"
],
[
"Tanggal",
"ISO 8601 (2026-11-02) atau pola yyyy-MM-dd",
"Standar internasional dan mudah diurutkan"
]
]
}
],
"code": "public class Main {\n    public static void main(String[] args) {\n        String nama = \"Rina\";\n        int umur = 20;\n        double ipk = 3.4567;\n        // %s teks, %d bilangan bulat, %.2f desimal 2 angka, %n baris baru\n        System.out.printf(\"Nama: %s, umur %d, IPK %.2f%n\", nama, umur, ipk);\n\n        // lebar kolom: angka positif = rata kanan, tanda minus = rata kiri\n        System.out.printf(\"[%8s] [%-8s] [%5d] [%05d]%n\", nama, nama, umur, umur);\n\n        // pemisah ribuan, persen, basis lain, notasi ilmiah, boolean, karakter\n        System.out.printf(\"Gaji %,d | diskon 15%% | hex %x | oktal %o%n\", 7500000, 255, 8);\n        System.out.printf(\"%.3e | %b | %c%n\", 123456.789, umur > 17, 'A');\n\n        // String.format menghasilkan teks, tidak langsung mencetak\n        String kode = String.format(\"INV-%04d\", 7);\n        System.out.println(kode);\n\n        // struk belanja: format di dalam loop membuat kolom rapi\n        String[] barang = {\"Kopi susu\", \"Roti bakar\", \"Air mineral\"};\n        int[] harga = {18000, 22500, 5000};\n        int total = 0;\n        System.out.printf(\"%-12s %10s%n\", \"Barang\", \"Harga\");\n        for (int i = 0; i < barang.length; i++) {\n            System.out.printf(\"%-12s %,10d%n\", barang[i], harga[i]);\n            total += harga[i];\n        }\n        System.out.printf(\"%-12s %,10d%n\", \"TOTAL\", total);\n    }\n}",
"out": "Nama: Rina, umur 20, IPK 3.46\n[    Rina] [Rina    ] [   20] [00020]\nGaji 7,500,000 | diskon 15% | hex ff | oktal 10\n1.235e+05 | true | A\nINV-0007\nBarang            Harga\nKopi susu        18,000\nRoti bakar       22,500\nAir mineral       5,000\nTOTAL            45,500",
"pts": [
"Pola umum: [perataan][lebar][.presisi][tipe].",
"Lebar + perataan membuat kolom laporan lurus.",
"Untuk angka ke pengguna, pakai format lokal (id-ID).",
"Kode baru: f-string, template literal, atau String.format."
],
"q": [
[
"Apa arti format %-10s?",
[
"Teks rata kanan selebar 10",
"Teks rata kiri selebar 10",
"10 karakter pertama saja"
],
1,
"Tanda minus berarti rata kiri, angka 10 adalah lebar kolom minimum."
],
[
"Format apa yang menampilkan 7 sebagai 007?",
[
"%.3d atau {x:.3}",
"%03d atau {x:03d}",
"%3d atau {x:3}"
],
1,
"Angka 0 di depan lebar berarti isi nol. Tanpa 0, sisa tempat diisi spasi."
],
[
"3.14159 diformat dengan dua angka desimal hasilnya?",
[
"3.14",
"3.15",
"3.1"
],
0,
"Dibulatkan ke 2 angka di belakang koma: 3.14159 → 3.14."
],
[
"Untuk menampilkan harga ke pengguna Indonesia, cara yang dianjurkan adalah?",
[
"Menyusun titik ribuan sendiri dengan replace",
"Memakai format berbasis lokal id-ID",
"Menampilkan angka mentah"
],
1,
"Format lokal menangani pemisah ribuan, desimal, dan simbol mata uang dengan benar."
]
],
"so": [
{
"q": "Tampilkan daftar 3 mahasiswa dengan kolom rapi: nomor (lebar 3, rata kanan), nama (lebar 10, rata kiri), dan IPK (2 angka desimal). Data: Ani 3.5, Budi 3.257, Citra 3.9.",
"h": "Gabungkan lebar dan perataan dengan presisi. Untuk IPK: lebar 5 dan 2 desimal, misalnya %5.2f atau {ipk:5.2f}.",
"a": "public class Main {\n    public static void main(String[] args) {\n        String[] nama = {\"Ani\", \"Budi\", \"Citra\"};\n        double[] ipk = {3.5, 3.257, 3.9};\n        for (int i = 0; i < nama.length; i++) {\n            System.out.printf(\"%3d %-10s %5.2f%n\", i + 1, nama[i], ipk[i]);\n        }\n    }\n}",
"out": "  1 Ani         3.50\n  2 Budi        3.26\n  3 Citra       3.90"
},
{
"q": "Buat nomor antrean 5 pelanggan dengan format A-001 sampai A-005.",
"h": "Isi angka dengan nol di depan sampai 3 digit: %03d di Java, {n:03d} di Python, padStart(3, \"0\") di JavaScript/TypeScript.",
"a": "public class Main {\n    public static void main(String[] args) {\n        for (int n = 1; n <= 5; n++) {\n            System.out.println(String.format(\"A-%03d\", n));\n        }\n    }\n}",
"out": "A-001\nA-002\nA-003\nA-004\nA-005"
}
]
},
{
"k": "c",
"t": "Kapan for, kapan while, kapan do-while",
"nodes": [
"Loops"
],
"viz": "looppick",
"b": [
"Semua loop bisa saling menggantikan, tetapi programmer yang baik memilih loop yang <b>paling jujur menggambarkan niatnya</b>. Pertanyaan kuncinya satu: <b>apakah jumlah putarannya sudah diketahui sebelum loop dimulai?</b>",
"Jika jumlahnya pasti (5 hari, 10 suku, setiap kursi 1 sampai 40), pakai <b>for</b> seperti <code>for (int i = 0; i &lt; n; i++)</code>. Jika yang diketahui hanya <b>kondisi berhentinya</b> (sampai saldo cukup, sampai data habis, sampai tidak ada pertukaran lagi), pakai <b>while</b>. Jika badan loop harus jalan <b>minimal sekali</b> sebelum dicek (menampilkan menu, meminta PIN), pakai <b>do-while</b>: <code>do { ... } while (kondisi);</code>.",
"Untuk membaca setiap isi koleksi tanpa butuh nomor indeks, pakai <b>for-each</b>: <code>for (String k : kota)</code>. Lebih ringkas dan tidak mungkin salah indeks (error klasik \"off by one\").",
"Pada contoh kode di bawah, keempat jenis loop dipakai sesuai kasusnya masing-masing. Tebak keluarannya dulu, lalu coba latihan memilih loop di visual interaktif."
],
"tb": [
{
"c": "Memilih jenis loop",
"h": [
"Jenis loop",
"Pakai saat",
"Contoh kasus",
"Bentuk di Java"
],
"r": [
[
"for",
"Jumlah putaran sudah diketahui",
"Cetak nomor 1 sampai 40, n suku Fibonacci",
"for (int i = 0; i < n; i++)"
],
[
"while",
"Hanya kondisi berhenti yang diketahui",
"Menabung sampai target, membaca data sampai habis",
"while (kondisi)"
],
[
"do-while",
"Badan loop wajib jalan minimal sekali",
"Menu kasir, meminta PIN",
"do { ... } while (kondisi);"
],
[
"for-each",
"Membaca setiap isi koleksi",
"Menjumlahkan harga di keranjang",
"for (String k : kota)"
]
]
}
],
"code": "public class Main {\n    public static void main(String[] args) {\n        // FOR: jumlah pengulangan sudah diketahui (5 hari)\n        int total = 0;\n        for (int hari = 1; hari <= 5; hari++) {\n            total += 10000;\n        }\n        System.out.println(\"Tabungan 5 hari: \" + total);\n\n        // WHILE: berhenti saat kondisi tercapai, jumlah putaran belum diketahui\n        int saldo = 0, minggu = 0;\n        while (saldo < 75000) {\n            saldo += 20000;\n            minggu++;\n        }\n        System.out.println(\"Target tercapai di minggu ke-\" + minggu);\n\n        // DO-WHILE: badan loop dijalankan minimal sekali\n        int[] pilihanUser = {2, 1, 0};\n        int i = 0, pilihan;\n        do {\n            pilihan = pilihanUser[i++];\n            System.out.println(\"Menu dipilih: \" + pilihan);\n        } while (pilihan != 0);\n\n        // FOR-EACH: membaca setiap isi koleksi\n        String[] kota = {\"Medan\", \"Bandung\", \"Makassar\"};\n        for (String k : kota) {\n            System.out.println(\"Kirim ke \" + k);\n        }\n    }\n}",
"out": "Tabungan 5 hari: 50000\nTarget tercapai di minggu ke-4\nMenu dipilih: 2\nMenu dipilih: 1\nMenu dipilih: 0\nKirim ke Medan\nKirim ke Bandung\nKirim ke Makassar",
"pts": [
"Jumlah putaran diketahui → for.",
"Hanya kondisi berhenti yang diketahui → while.",
"Harus jalan minimal sekali → do-while.",
"Hanya membaca isi koleksi → for-each."
],
"q": [
[
"Program meminta pengguna mengetik kata sandi sampai benar. Loop paling cocok?",
[
"for",
"do-while (atau while True + break)",
"for-each"
],
1,
"Pertanyaan harus muncul minimal sekali, dan jumlah percobaannya tidak diketahui."
],
[
"Menghitung rata-rata 30 nilai siswa di sebuah array. Loop paling cocok?",
[
"while",
"for atau for-each",
"do-while"
],
1,
"Jumlah datanya pasti, cukup membaca setiap isi."
],
[
"Mengapa while lebih cocok untuk \"menabung sampai Rp1 juta\"?",
[
"Karena while lebih cepat",
"Karena jumlah minggunya belum diketahui, yang diketahui hanya kondisi berhenti",
"Karena for tidak bisa menjumlah"
],
1,
"Pilihan loop menggambarkan apa yang kita ketahui sebelum mulai."
]
],
"lang": "java",
"so": [
{
"q": "Hitung mundur peluncuran roket: tampilkan 5, 4, 3, 2, 1 lalu \"Meluncur!\". Loop apa yang paling cocok?",
"h": "Awal dan akhir hitungan sudah pasti (5 sampai 1), jadi pakai for yang nilainya berkurang.",
"a": "public class Main {\n    public static void main(String[] args) {\n        for (int detik = 5; detik >= 1; detik--) {\n            System.out.println(detik);\n        }\n        System.out.println(\"Meluncur!\");\n    }\n}",
"out": "5\n4\n3\n2\n1\nMeluncur!"
},
{
"q": "Galon diisi 3 liter setiap menit, mulai dari kosong. Berapa menit sampai isinya minimal 19 liter? Tampilkan menit dan isinya.",
"h": "Jumlah menit belum diketahui, yang diketahui hanya kondisi berhenti (isi ≥ 19). Itu tanda while.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int isi = 0, menit = 0;\n        while (isi < 19) {\n            isi += 3;\n            menit++;\n        }\n        System.out.println(menit + \" menit, isi \" + isi + \" liter\");\n    }\n}",
"out": "7 menit, isi 21 liter"
}
]
},
{
"k": "c",
"t": "Bilangan Fibonacci: for dan while",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "FibonacciDiBawah100",
"p": [
{
"t": "dec",
"v": "a, b, c, banyak",
"ty": "Integer"
},
{
"t": "asg",
"v": "a",
"e": "0"
},
{
"t": "asg",
"v": "b",
"e": "1"
},
{
"t": "asg",
"v": "banyak",
"e": "0"
},
{
"t": "while",
"c": "a < 100",
"b": [
{
"t": "asg",
"v": "banyak",
"e": "banyak + 1"
},
{
"t": "asg",
"v": "c",
"e": "a + b"
},
{
"t": "asg",
"v": "a",
"e": "b"
},
{
"t": "asg",
"v": "b",
"e": "c"
}
]
},
{
"t": "out",
"e": "\"Banyak suku: \" & banyak"
}
]
},
"b": [
"Deret Fibonacci dimulai dari 0 dan 1, lalu setiap suku adalah jumlah dua suku sebelumnya: 0, 1, 1, 2, 3, 5, 8, 13, ... Polanya muncul di banyak tempat, dari susunan biji bunga matahari sampai soal tes kerja programmer.",
"Kuncinya adalah dua variabel <code>a</code> dan <code>b</code> yang terus <b>digeser</b>: <code>a</code> menjadi <code>b</code>, dan <code>b</code> menjadi <code>a + b</code>. Di Java kita butuh variabel bantu, misalnya <code>int c = a + b; a = b; b = c;</code>, agar nilai lama <code>a</code> tidak hilang.",
"Perhatikan dua bagian contoh. \"10 suku pertama\" memakai <b>for</b> karena jumlah putarannya pasti 10. \"Semua suku di bawah 100\" memakai <b>while</b> karena kita tidak tahu ada berapa suku sampai benar-benar menghitungnya.",
"Visual di bawah menjalankan bagian while langkah demi langkah sebagai flowchart dan pseudocode. Perhatikan kolom <b>Variabel</b>: nilai yang berubah diberi warna."
],
"tb": [
{
"c": "Jejak variabel 6 putaran pertama",
"h": [
"Putaran",
"a",
"b",
"Suku yang dicatat"
],
"r": [
[
"1",
"0",
"1",
"0"
],
[
"2",
"1",
"1",
"1"
],
[
"3",
"1",
"2",
"1"
],
[
"4",
"2",
"3",
"2"
],
[
"5",
"3",
"5",
"3"
],
[
"6",
"5",
"8",
"5"
]
]
}
],
"code": "public class Main {\n    public static void main(String[] args) {\n        // FOR: n suku pertama (jumlah putaran diketahui)\n        int n = 10;\n        long a = 0, b = 1;\n        StringBuilder deret = new StringBuilder();\n        for (int i = 0; i < n; i++) {\n            deret.append(a).append(\" \");\n            long berikut = a + b;\n            a = b;\n            b = berikut;\n        }\n        System.out.println(\"10 suku pertama: \" + deret.toString().trim());\n\n        // WHILE: semua suku di bawah 100 (jumlah putaran belum diketahui)\n        a = 0; b = 1;\n        int banyak = 0;\n        while (a < 100) {\n            banyak++;\n            long berikut = a + b;\n            a = b;\n            b = berikut;\n        }\n        System.out.println(\"Banyak suku di bawah 100: \" + banyak);\n    }\n}",
"out": "10 suku pertama: 0 1 1 2 3 5 8 13 21 34\nBanyak suku di bawah 100: 12",
"pts": [
"Fibonacci butuh dua variabel yang terus digeser.",
"n suku pertama → for; suku di bawah batas → while.",
"Geser nilai dengan urutan yang benar agar nilai lama tidak hilang."
],
"q": [
[
"Suku Fibonacci ke-8 (mulai dari 0) adalah?",
[
"8",
"13",
"21"
],
1,
"0, 1, 1, 2, 3, 5, 8, 13: suku ke-8 adalah 13."
],
[
"Mengapa menghitung \"suku di bawah 1000\" memakai while?",
[
"Karena jumlah sukunya belum diketahui sebelum dihitung",
"Karena for tidak bisa memakai angka besar",
"Karena while selalu lebih cepat"
],
0,
"Batasnya nilai, bukan banyak putaran."
]
],
"lang": "java",
"so": [
{
"q": "Tampilkan hanya suku Fibonacci ke-20 (suku pertama adalah 0).",
"h": "Kamu tahu persis butuh 19 kali geser pasangan (a, b), jadi pakai for. Tidak perlu menyimpan semua suku.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int a = 0, b = 1;\n        for (int i = 0; i < 19; i++) {\n            int c = a + b;\n            a = b;\n            b = c;\n        }\n        System.out.println(\"Suku ke-20: \" + a);\n    }\n}",
"out": "Suku ke-20: 4181"
},
{
"q": "Cari suku Fibonacci pertama yang lebih dari 1000, dan suku ke berapa itu.",
"h": "Kamu tidak tahu butuh berapa suku, jadi pakai while dengan kondisi a <= 1000.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int a = 0, b = 1, ke = 1;\n        while (a <= 1000) {\n            int c = a + b;\n            a = b;\n            b = c;\n            ke++;\n        }\n        System.out.println(\"Suku ke-\" + ke + \": \" + a);\n    }\n}",
"out": "Suku ke-18: 1597"
}
]
},
{
"k": "c",
"t": "Bubble sort: loop di dalam loop",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BubbleSort",
"p": [
{
"t": "dec",
"v": "a",
"ty": "Integer",
"arr": "4"
},
{
"t": "asg",
"v": "a",
"e": "[25, 12, 22, 11]"
},
{
"t": "dec",
"v": "j, t, putaran",
"ty": "Integer"
},
{
"t": "dec",
"v": "adaTukar",
"ty": "Boolean"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
},
{
"t": "asg",
"v": "putaran",
"e": "0"
},
{
"t": "while",
"c": "adaTukar",
"b": [
{
"t": "asg",
"v": "adaTukar",
"e": "false"
},
{
"t": "asg",
"v": "putaran",
"e": "putaran + 1"
},
{
"t": "for",
"v": "j",
"a": "0",
"z": "3 - putaran",
"b": [
{
"t": "if",
"c": "a[j] > a[j + 1]",
"y": [
{
"t": "asg",
"v": "t",
"e": "a[j]"
},
{
"t": "asg",
"v": "a[j]",
"e": "a[j + 1]"
},
{
"t": "asg",
"v": "a[j + 1]",
"e": "t"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
}
],
"n": []
}
]
}
]
},
{
"t": "out",
"e": "\"Terurut: \" & a"
}
]
},
"b": [
"Bubble sort mengurutkan data dengan cara paling sederhana: bandingkan dua angka yang <b>bersebelahan</b>, tukar jika urutannya salah, lalu geser ke pasangan berikutnya. Setelah satu putaran, angka terbesar pasti sudah \"menggelembung\" ke ujung kanan.",
"Algoritma ini memakai dua loop. <b>Loop dalam (for)</b> berjalan dari kiri ke kanan, jumlah pasangannya jelas. <b>Loop luar (while)</b> mengulang putaran selama masih ada pertukaran. Variabel penanda <code>adaTukar</code> membuat program berhenti lebih awal jika data sudah terurut.",
"Setiap putaran, satu angka terbesar sudah di tempatnya, jadi loop dalam cukup sampai <code>n - putaran</code>. Detail kecil ini menghemat perbandingan yang tidak perlu.",
"Bubble sort lambat untuk data besar (sekitar n² perbandingan), jadi di dunia kerja kita memakai fungsi sort bawaan bahasa. Tetapi bubble sort adalah latihan terbaik untuk memahami loop bersarang, indeks, dan menukar nilai."
],
"tb": [
{
"c": "Isi array setiap putaran",
"h": [
"Putaran",
"Isi array",
"Yang sudah di tempat"
],
"r": [
[
"Awal",
"64 25 12 22 11",
"-"
],
[
"1",
"25 12 22 11 64",
"64"
],
[
"2",
"12 22 11 25 64",
"25, 64"
],
[
"3",
"12 11 22 25 64",
"22, 25, 64"
],
[
"4",
"11 12 22 25 64",
"semua"
]
]
}
],
"code": "import java.util.Arrays;\n\npublic class Main {\n    public static void main(String[] args) {\n        int[] nilai = {64, 25, 12, 22, 11};\n        int n = nilai.length;\n        boolean adaTukar = true;\n        int putaran = 0;\n        // WHILE luar: berhenti jika satu putaran tidak ada pertukaran\n        while (adaTukar) {\n            adaTukar = false;\n            putaran++;\n            // FOR dalam: bandingkan pasangan bersebelahan\n            for (int j = 0; j < n - putaran; j++) {\n                if (nilai[j] > nilai[j + 1]) {\n                    int sementara = nilai[j];\n                    nilai[j] = nilai[j + 1];\n                    nilai[j + 1] = sementara;\n                    adaTukar = true;\n                }\n            }\n            System.out.println(\"Putaran \" + putaran + \": \" + Arrays.toString(nilai));\n        }\n        System.out.println(\"Terurut: \" + Arrays.toString(nilai));\n    }\n}",
"out": "Putaran 1: [25, 12, 22, 11, 64]\nPutaran 2: [12, 22, 11, 25, 64]\nPutaran 3: [12, 11, 22, 25, 64]\nPutaran 4: [11, 12, 22, 25, 64]\nPutaran 5: [11, 12, 22, 25, 64]\nTerurut: [11, 12, 22, 25, 64]",
"pts": [
"Bandingkan pasangan bersebelahan, tukar jika salah urutan.",
"Loop dalam for (jumlah pasangan jelas), loop luar while (sampai tidak ada pertukaran).",
"Penanda pertukaran membuat sort berhenti lebih awal."
],
"q": [
[
"Setelah putaran pertama bubble sort (urut naik), di mana angka terbesar?",
[
"Di indeks 0",
"Di ujung kanan",
"Belum pasti"
],
1,
"Angka terbesar selalu terbawa sampai ujung kanan pada putaran pertama."
],
[
"Untuk apa variabel penanda pertukaran?",
[
"Menghitung jumlah data",
"Menghentikan loop luar jika satu putaran tidak ada pertukaran",
"Menyimpan angka terbesar"
],
1,
"Jika tidak ada pertukaran, data sudah terurut."
],
[
"Kenapa loop dalam cukup sampai n - putaran?",
[
"Agar tidak error",
"Karena angka di ujung kanan sudah pasti di tempatnya",
"Karena aturan bahasa"
],
1,
"Bagian kanan yang sudah terurut tidak perlu dibandingkan lagi."
]
],
"lang": "java",
"so": [
{
"q": "Urutkan nama [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"] sesuai abjad dengan bubble sort.",
"h": "Logikanya sama, hanya cara membandingkan teks yang berbeda: Python memakai >, JavaScript/TypeScript memakai localeCompare, Java memakai compareTo.",
"a": "public class Main {\n    public static void main(String[] args) {\n        String[] nama = {\"Rina\", \"Agus\", \"Dewi\", \"Budi\"};\n        boolean adaTukar = true;\n        while (adaTukar) {\n            adaTukar = false;\n            for (int j = 0; j < nama.length - 1; j++) {\n                if (nama[j].compareTo(nama[j + 1]) > 0) {\n                    String t = nama[j];\n                    nama[j] = nama[j + 1];\n                    nama[j + 1] = t;\n                    adaTukar = true;\n                }\n            }\n        }\n        System.out.println(String.join(\", \", nama));\n    }\n}",
"out": "Agus, Budi, Dewi, Rina"
},
{
"q": "Ubah bubble sort agar mengurutkan dari besar ke kecil, lalu hitung berapa kali terjadi pertukaran untuk [3, 1, 4, 1, 5].",
"h": "Cukup balik tanda perbandingan menjadi <, dan tambah penghitung setiap kali menukar.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int[] data = {3, 1, 4, 1, 5};\n        int tukar = 0;\n        for (int i = 0; i < data.length - 1; i++) {\n            for (int j = 0; j < data.length - 1 - i; j++) {\n                if (data[j] < data[j + 1]) {\n                    int t = data[j];\n                    data[j] = data[j + 1];\n                    data[j + 1] = t;\n                    tukar++;\n                }\n            }\n        }\n        System.out.println(java.util.Arrays.toString(data) + \" pertukaran: \" + tukar);\n    }\n}",
"out": "[5, 4, 3, 1, 1] pertukaran: 6"
}
]
},
{
"k": "c",
"t": "FizzBuzz dan bilangan prima: break dan loop bersarang",
"nodes": [
"Loops",
"Conditionals"
],
"viz": "fc",
"fc": {
"name": "CekPrima",
"in": [
"29"
],
"p": [
{
"t": "dec",
"v": "x, d",
"ty": "Integer"
},
{
"t": "dec",
"v": "prima",
"ty": "Boolean"
},
{
"t": "in",
"v": "x"
},
{
"t": "asg",
"v": "prima",
"e": "x >= 2"
},
{
"t": "asg",
"v": "d",
"e": "2"
},
{
"t": "while",
"c": "d * d <= x and prima",
"b": [
{
"t": "if",
"c": "x mod d = 0",
"y": [
{
"t": "asg",
"v": "prima",
"e": "false"
}
],
"n": []
},
{
"t": "asg",
"v": "d",
"e": "d + 1"
}
]
},
{
"t": "if",
"c": "prima",
"y": [
{
"t": "out",
"e": "x & \" adalah prima\""
}
],
"n": [
{
"t": "out",
"e": "x & \" bukan prima\""
}
]
}
]
},
"b": [
"<b>FizzBuzz</b> adalah soal wawancara klasik: untuk angka 1 sampai 15, tampilkan \"Fizz\" jika habis dibagi 3, \"Buzz\" jika habis dibagi 5, \"FizzBuzz\" jika habis dibagi keduanya, dan angkanya sendiri jika tidak. Rentangnya jelas, jadi pakai <b>for</b>. Jebakannya: cek kelipatan 15 lebih dulu, karena jika cek 3 duluan, angka 15 sudah keburu menjadi \"Fizz\".",
"<b>Bilangan prima</b> hanya habis dibagi 1 dan dirinya sendiri. Untuk setiap angka (loop luar), kita coba pembagi dari 2 (loop dalam). Begitu ketemu satu pembagi, angka itu pasti bukan prima, jadi <b>break</b> menghentikan loop dalam tanpa membuang waktu.",
"Pembagi cukup dicoba sampai akar angkanya (<code>d * d &lt;= x</code>). Jika 36 = 4 × 9, salah satu faktornya pasti ≤ 6. Ini mengubah 1.000 percobaan menjadi sekitar 31. Variabel penanda <code>isPrima</code> mencatat apakah loop dalam pernah berhenti karena break.",
"Visual di bawah memeriksa satu angka dengan while dan penanda, karena Flowgorithm tidak punya break. Ganti inputnya, misalnya 91 atau 97, lalu jalankan."
],
"tb": [
{
"c": "break dan continue",
"h": [
"Perintah",
"Efek",
"Kapan dipakai"
],
"r": [
[
"break",
"Keluar dari loop terdekat",
"Jawaban sudah ditemukan, sisa putaran tidak perlu"
],
[
"continue",
"Lompat ke putaran berikutnya",
"Lewati data yang tidak relevan"
],
[
"penanda (flag)",
"Variabel boolean yang dicek setelah loop",
"Bahasa atau alat tanpa break, misalnya Flowgorithm"
]
]
}
],
"code": "public class Main {\n    public static void main(String[] args) {\n        // FizzBuzz: FOR karena rentangnya jelas (1 sampai 15)\n        StringBuilder sb = new StringBuilder();\n        for (int i = 1; i <= 15; i++) {\n            if (i % 15 == 0) sb.append(\"FizzBuzz \");\n            else if (i % 3 == 0) sb.append(\"Fizz \");\n            else if (i % 5 == 0) sb.append(\"Buzz \");\n            else sb.append(i).append(\" \");\n        }\n        System.out.println(sb.toString().trim());\n\n        // Bilangan prima 2..30: FOR bersarang + break\n        StringBuilder prima = new StringBuilder();\n        for (int x = 2; x <= 30; x++) {\n            boolean isPrima = true;\n            for (int d = 2; d * d <= x; d++) {\n                if (x % d == 0) {\n                    isPrima = false;\n                    break;          // tidak perlu cek pembagi lain\n                }\n            }\n            if (isPrima) prima.append(x).append(\" \");\n        }\n        System.out.println(\"Prima: \" + prima.toString().trim());\n    }\n}",
"out": "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\nPrima: 2 3 5 7 11 13 17 19 23 29",
"pts": [
"Urutan if penting: kondisi paling khusus dicek lebih dulu.",
"break menghentikan loop terdekat saat jawaban sudah pasti.",
"Pembagi prima cukup dicek sampai akar angkanya."
],
"q": [
[
"Jika FizzBuzz mengecek \"habis dibagi 3\" lebih dulu, apa yang tampil untuk 15?",
[
"FizzBuzz",
"Fizz",
"Buzz"
],
1,
"Kondisi pertama yang benar langsung dipakai."
],
[
"Pada loop bersarang, break menghentikan loop yang mana?",
[
"Semua loop",
"Loop terdekat yang membungkusnya",
"Loop terluar"
],
1,
"break hanya keluar dari satu tingkat loop."
],
[
"Untuk mengecek apakah 97 prima, pembagi paling besar yang perlu dicoba adalah?",
[
"96",
"48",
"9"
],
2,
"9 × 9 = 81 ≤ 97, sedangkan 10 × 10 = 100 > 97."
]
],
"lang": "java",
"so": [
{
"q": "Tampilkan tabel perkalian 1 sampai 5 dalam bentuk kotak (5 baris, 5 kolom).",
"h": "For luar untuk baris, for dalam untuk kolom. Keduanya punya batas yang jelas.",
"a": "public class Main {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 5; i++) {\n            StringBuilder baris = new StringBuilder();\n            for (int j = 1; j <= 5; j++) {\n                baris.append(String.format(\"%4d\", i * j));\n            }\n            System.out.println(baris);\n        }\n    }\n}",
"out": "   1   2   3   4   5\n   2   4   6   8  10\n   3   6   9  12  15\n   4   8  12  16  20\n   5  10  15  20  25"
},
{
"q": "Cari bilangan prima pertama yang lebih besar dari 100.",
"h": "Kita tidak tahu harus mencoba berapa angka, jadi loop luar memakai while. Pengecekan pembagi tetap memakai for dengan break.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int x = 101;\n        while (true) {\n            boolean prima = true;\n            for (int d = 2; d * d <= x; d++) {\n                if (x % d == 0) { prima = false; break; }\n            }\n            if (prima) break;\n            x++;\n        }\n        System.out.println(\"Prima pertama > 100: \" + x);\n    }\n}",
"out": "Prima pertama > 100: 101"
}
]
},
{
"k": "c",
"t": "Faktorial, jumlah digit, dan palindrom",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "JumlahDigit",
"in": [
"90417"
],
"p": [
{
"t": "dec",
"v": "angka, jumlah",
"ty": "Integer"
},
{
"t": "in",
"v": "angka"
},
{
"t": "asg",
"v": "jumlah",
"e": "0"
},
{
"t": "while",
"c": "angka > 0",
"b": [
{
"t": "asg",
"v": "jumlah",
"e": "jumlah + angka mod 10"
},
{
"t": "asg",
"v": "angka",
"e": "Int(angka / 10)"
}
]
},
{
"t": "out",
"e": "\"Jumlah digit: \" & jumlah"
}
]
},
"b": [
"Tiga soal ini melatih kapan memakai for dan kapan while. <b>Faktorial</b> 5! = 1 × 2 × 3 × 4 × 5: banyak perkaliannya pasti, jadi <b>for</b>.",
"<b>Jumlah digit</b> 90417 = 9 + 0 + 4 + 1 + 7 = 21. Kita tidak tahu angkanya punya berapa digit, jadi pakai <b>while</b>: ambil digit terakhir dengan <code>% 10</code>, lalu buang dengan pembagian bulat <code>/ 10</code> (int di Java otomatis membulatkan ke bawah). Berhenti saat angkanya habis (0).",
"<b>Palindrom</b> adalah kata yang sama jika dibaca dari depan dan belakang, seperti \"katak\". Pakai <b>dua penunjuk</b>: satu dari kiri, satu dari kanan, bergerak ke tengah selama <code>kiri &lt; kanan</code>. Begitu ada huruf yang berbeda, langsung break.",
"Visual di bawah menjalankan jumlah digit. Coba ganti inputnya dengan angka lain dan hitung dulu di kepala sebelum menekan Berikutnya."
],
"tb": [
{
"c": "Jejak jumlah digit 90417",
"h": [
"Putaran",
"angka % 10",
"jumlah",
"angka setelah dibagi 10"
],
"r": [
[
"1",
"7",
"7",
"9041"
],
[
"2",
"1",
"8",
"904"
],
[
"3",
"4",
"12",
"90"
],
[
"4",
"0",
"12",
"9"
],
[
"5",
"9",
"21",
"0"
]
]
}
],
"code": "public class Main {\n    public static void main(String[] args) {\n        // Faktorial: FOR, jumlah perkalian = n\n        int n = 5;\n        long faktorial = 1;\n        for (int i = 2; i <= n; i++) {\n            faktorial *= i;\n        }\n        System.out.println(n + \"! = \" + faktorial);\n\n        // Jumlah digit: WHILE, banyak digit belum diketahui\n        int angka = 90417, sisa = angka, jumlah = 0;\n        while (sisa > 0) {\n            jumlah += sisa % 10;   // ambil digit terakhir\n            sisa /= 10;            // buang digit terakhir\n        }\n        System.out.println(\"Jumlah digit \" + angka + \" = \" + jumlah);\n\n        // Palindrom: WHILE dua penunjuk bergerak ke tengah\n        String kata = \"katak\";\n        int kiri = 0, kanan = kata.length() - 1;\n        boolean palindrom = true;\n        while (kiri < kanan) {\n            if (kata.charAt(kiri) != kata.charAt(kanan)) {\n                palindrom = false;\n                break;\n            }\n            kiri++;\n            kanan--;\n        }\n        System.out.println(kata + \" palindrom? \" + palindrom);\n    }\n}",
"out": "5! = 120\nJumlah digit 90417 = 21\nkatak palindrom? true",
"pts": [
"% 10 mengambil digit terakhir, bagi 10 (bulat) membuangnya.",
"Banyak digit tidak diketahui → while.",
"Dua penunjuk bergerak ke tengah untuk memeriksa palindrom."
],
"q": [
[
"Berapa hasil 4827 % 10?",
[
"4",
"7",
"482"
],
1,
"Sisa bagi 10 adalah digit terakhir."
],
[
"Loop paling cocok untuk menghitung 10! (faktorial 10)?",
[
"for",
"while",
"do-while"
],
0,
"Banyak perkaliannya pasti."
],
[
"Pada pemeriksaan palindrom \"level\", berapa kali perbandingan huruf terjadi?",
[
"5",
"2",
"1"
],
1,
"Pasangan (l, l) dan (e, e); huruf tengah v tidak perlu dibandingkan."
]
],
"lang": "java",
"so": [
{
"q": "Balik angka 12345 menjadi 54321 tanpa mengubahnya menjadi teks.",
"h": "Ambil digit terakhir dengan % 10, tempel ke hasil dengan hasil * 10 + digit, buang digit terakhir dengan pembagian bulat. Ulangi selama angka > 0.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int angka = 12345, balik = 0;\n        while (angka > 0) {\n            balik = balik * 10 + angka % 10;\n            angka /= 10;\n        }\n        System.out.println(\"Dibalik: \" + balik);\n    }\n}",
"out": "Dibalik: 54321"
},
{
"q": "Hitung 2 pangkat 10 dengan loop, tanpa operator pangkat.",
"h": "Perkalian diulang tepat 10 kali, jadi for.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int hasil = 1;\n        for (int i = 0; i < 10; i++) {\n            hasil *= 2;\n        }\n        System.out.println(\"2^10 = \" + hasil);\n    }\n}",
"out": "2^10 = 1024"
}
]
},
{
"k": "c",
"t": "Binary search: membagi dua sampai ketemu",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BinarySearch",
"in": [
"20000"
],
"p": [
{
"t": "dec",
"v": "harga",
"ty": "Integer",
"arr": "7"
},
{
"t": "asg",
"v": "harga",
"e": "[5000, 8000, 12000, 15000, 20000, 27000, 35000]"
},
{
"t": "dec",
"v": "cari, kiri, kanan, tengah, posisi",
"ty": "Integer"
},
{
"t": "in",
"v": "cari"
},
{
"t": "asg",
"v": "kiri",
"e": "0"
},
{
"t": "asg",
"v": "kanan",
"e": "6"
},
{
"t": "asg",
"v": "posisi",
"e": "-1"
},
{
"t": "while",
"c": "kiri <= kanan and posisi = -1",
"b": [
{
"t": "asg",
"v": "tengah",
"e": "Int((kiri + kanan) / 2)"
},
{
"t": "if",
"c": "harga[tengah] = cari",
"y": [
{
"t": "asg",
"v": "posisi",
"e": "tengah"
}
],
"n": [
{
"t": "if",
"c": "harga[tengah] < cari",
"y": [
{
"t": "asg",
"v": "kiri",
"e": "tengah + 1"
}
],
"n": [
{
"t": "asg",
"v": "kanan",
"e": "tengah - 1"
}
]
}
]
}
]
},
{
"t": "out",
"e": "\"Posisi: \" & posisi"
}
]
},
"b": [
"Mencari harga di daftar 1.000 barang satu per satu (linear search) bisa butuh 1.000 langkah. Jika daftarnya <b>sudah terurut</b>, kita bisa jauh lebih cepat: lihat bagian tengah, lalu buang separuh daftar yang pasti tidak berisi jawabannya.",
"Simpan dua batas, <code>kiri</code> dan <code>kanan</code>. Selama <code>kiri &lt;= kanan</code>, hitung <code>tengah</code>. Jika nilai tengah terlalu kecil, geser kiri ke tengah + 1. Jika terlalu besar, geser kanan ke tengah - 1. Banyak langkahnya tidak diketahui sebelumnya, jadi loopnya <b>while</b>.",
"Setiap langkah membuang separuh data, jadi 1.000 data cukup dicari dalam paling banyak 10 langkah, dan 1 juta data dalam 20 langkah. Inilah alasan database dan kamus memakai data terurut.",
"Visual di bawah mencari harga di 7 data. Coba input 5000, 35000, atau 9000 (tidak ada di daftar) dan perhatikan bagaimana kiri dan kanan bergerak."
],
"tb": [
{
"c": "Linear search vs binary search",
"h": [
"Aspek",
"Linear search",
"Binary search"
],
"r": [
[
"Syarat data",
"Bebas",
"Harus terurut"
],
[
"Langkah terburuk (1.000 data)",
"1.000",
"10"
],
[
"Jenis loop",
"for (setiap data)",
"while (sampai ketemu atau habis)"
],
[
"Kapan dipakai",
"Data sedikit atau tidak terurut",
"Data besar dan terurut"
]
]
}
],
"code": "public class Main {\n    public static void main(String[] args) {\n        int[] harga = {5000, 8000, 12000, 15000, 20000, 27000, 35000};\n        int cari = 20000;\n        int kiri = 0, kanan = harga.length - 1, langkah = 0, posisi = -1;\n        // WHILE: berhenti saat ketemu atau ruang pencarian habis\n        while (kiri <= kanan) {\n            langkah++;\n            int tengah = (kiri + kanan) / 2;\n            System.out.println(\"Langkah \" + langkah + \": cek indeks \" + tengah + \" (\" + harga[tengah] + \")\");\n            if (harga[tengah] == cari) {\n                posisi = tengah;\n                break;\n            } else if (harga[tengah] < cari) {\n                kiri = tengah + 1;\n            } else {\n                kanan = tengah - 1;\n            }\n        }\n        System.out.println(\"Ketemu di indeks \" + posisi + \" setelah \" + langkah + \" langkah\");\n    }\n}",
"out": "Langkah 1: cek indeks 3 (15000)\nLangkah 2: cek indeks 5 (27000)\nLangkah 3: cek indeks 4 (20000)\nKetemu di indeks 4 setelah 3 langkah",
"pts": [
"Binary search hanya untuk data terurut.",
"Setiap langkah membuang separuh ruang pencarian.",
"Berhenti saat ketemu atau kiri > kanan."
],
"q": [
[
"Apa syarat utama binary search?",
[
"Data berupa angka",
"Data sudah terurut",
"Data kurang dari 100"
],
1,
"Tanpa urutan, kita tidak tahu separuh mana yang harus dibuang."
],
[
"Jika harga[tengah] lebih kecil dari yang dicari, apa yang dilakukan?",
[
"kanan = tengah - 1",
"kiri = tengah + 1",
"Berhenti"
],
1,
"Jawabannya pasti di sebelah kanan tengah."
],
[
"Kira-kira berapa langkah maksimum untuk 1 juta data terurut?",
[
"20",
"1.000",
"500.000"
],
0,
"2 pangkat 20 ≈ 1 juta."
]
],
"lang": "java",
"so": [
{
"q": "Komputer menebak angka rahasia 73 di antara 1 sampai 100 dengan cara binary search. Tampilkan setiap tebakan.",
"h": "Sama seperti mencari di array terurut, hanya saja \"array\"-nya adalah rentang angka 1 sampai 100.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int rahasia = 73, bawah = 1, atas = 100;\n        while (true) {\n            int tebak = (bawah + atas) / 2;\n            System.out.println(\"Tebak \" + tebak);\n            if (tebak == rahasia) break;\n            if (tebak < rahasia) bawah = tebak + 1;\n            else atas = tebak - 1;\n        }\n    }\n}",
"out": "Tebak 50\nTebak 75\nTebak 62\nTebak 68\nTebak 71\nTebak 73"
},
{
"q": "Berapa langkah paling banyak yang dibutuhkan binary search untuk 1.000 data? Hitung dengan membagi dua terus sampai habis.",
"h": "Selama masih ada data (n > 0), bagi dua dan tambah 1 langkah. Ini while karena jumlah langkah adalah hal yang dicari.",
"a": "public class Main {\n    public static void main(String[] args) {\n        int n = 1000, langkah = 0;\n        while (n > 0) {\n            n /= 2;\n            langkah++;\n        }\n        System.out.println(\"Maksimal \" + langkah + \" langkah\");\n    }\n}",
"out": "Maksimal 10 langkah"
}
]
}
]
},
"python": {
"t": "Format keluaran dan latihan algoritma",
"lvl": "Menengah",
"d": "Format specifier, Fibonacci, bubble sort, FizzBuzz, bilangan prima, palindrom, dan binary search di Python, dengan alasan memilih for, while, do-while, atau for-each.",
"nodes": [
"Loops",
"Arrays"
],
"lessons": [
{
"k": "c",
"t": "Format specifier: merapikan keluaran",
"nodes": [
"Basic Syntax"
],
"lang": "python",
"b": [
"<b>Format specifier</b> adalah kode kecil yang mengatur <b>bagaimana sebuah nilai ditampilkan</b>: berapa angka di belakang koma, selebar apa kolomnya, rata kiri atau kanan, diberi nol di depan, atau diberi pemisah ribuan. Nilainya tidak berubah, hanya tampilannya. Hampir semua program nyata membutuhkannya: struk belanja, laporan nilai, nomor invoice, dan log server.",
"Polanya mirip di semua bahasa: <b>[perataan][lebar][.presisi][tipe]</b>. Contoh <code>%-10s</code> berarti teks rata kiri selebar 10, <code>%8.2f</code> berarti desimal 2 angka dalam kolom selebar 8, dan <code>%05d</code> berarti bilangan bulat selebar 5 yang diisi nol di depan.",
"Python modern memakai <b>f-string</b>: <code>f\"{nilai:spesifikasi}\"</code>. Perataan ditulis dengan simbol: <code>&lt;</code> kiri, <code>&gt;</code> kanan, <code>^</code> tengah. Tambahan khas Python: <code>{x:,}</code> untuk pemisah ribuan, <code>{x:.0%}</code> untuk persen, dan <code>{x=}</code> untuk debugging cepat yang mencetak nama variabel beserta nilainya.",
"Kamu juga akan menemui gaya lama <code>\"%s %d\" % (a, b)</code> dan <code>\"{}\".format(x)</code> di kode lama dan modul logging. Spesifikasinya sama, jadi cukup pelajari sekali. Untuk kode baru, f-string adalah standar industri karena paling mudah dibaca.",
"Contoh terakhir di kode adalah <b>struk belanja</b>: format di dalam loop membuat setiap baris punya lebar kolom yang sama, sehingga angka tersusun rapi ke kanan. Ini pola yang akan sering kamu pakai di soal-soal berikutnya."
],
"tb": [
{
"c": "Format specifier di berbagai bahasa",
"h": [
"Tujuan",
"Java / C (printf)",
"Python (f-string)",
"JavaScript / TypeScript"
],
"r": [
[
"Teks",
"%s",
"{x}",
"${x}"
],
[
"Bilangan bulat",
"%d",
"{x:d}",
"${x}"
],
[
"Desimal 2 angka",
"%.2f",
"{x:.2f}",
"x.toFixed(2)"
],
[
"Lebar 8, rata kanan",
"%8s",
"{x:>8}",
"String(x).padStart(8)"
],
[
"Lebar 8, rata kiri",
"%-8s",
"{x:<8}",
"String(x).padEnd(8)"
],
[
"Isi nol di depan",
"%05d",
"{x:05d}",
"String(x).padStart(5, \"0\")"
],
[
"Pemisah ribuan",
"%,d",
"{x:,}",
"x.toLocaleString(\"id-ID\")"
],
[
"Persen",
"%.0f%%",
"{x:.0%}",
"(x * 100).toFixed(0) + \"%\""
],
[
"Heksadesimal",
"%x",
"{x:x}",
"x.toString(16)"
],
[
"Notasi ilmiah",
"%.3e",
"{x:.3e}",
"x.toExponential(3)"
],
[
"Baris baru",
"%n atau \\n",
"\\n",
"\\n"
]
]
},
{
"c": "Yang paling sering dipakai di industri",
"h": [
"Kebutuhan",
"Pilihan umum",
"Alasan"
],
"r": [
[
"Menyusun teks di kode baru",
"f-string (Python), template literal (JS/TS), String.format atau formatted() (Java)",
"Paling mudah dibaca dan dirawat"
],
[
"Angka dan uang ke pengguna",
"Format berbasis lokal: Intl.NumberFormat, Locale id-ID, Babel",
"Titik, koma, dan simbol Rp mengikuti aturan negara"
],
[
"Laporan dan struk berkolom",
"Lebar + perataan: %-12s, %10.2f, padEnd/padStart",
"Kolom tetap lurus berapa pun panjang datanya"
],
[
"Kode dokumen dan antrean",
"Isi nol: %04d, {n:04d}",
"INV-0007 lebih mudah diurutkan dan dicari"
],
[
"Logging",
"Placeholder %s atau {}: logger.info(\"user %s\", id)",
"Teks hanya disusun jika log benar-benar dicetak"
],
[
"Tanggal",
"ISO 8601 (2026-11-02) atau pola yyyy-MM-dd",
"Standar internasional dan mudah diurutkan"
]
]
}
],
"code": "nama = \"Rina\"\numur = 20\nipk = 3.4567\n# f-string: {nilai:spesifikasi}\nprint(f\"Nama: {nama}, umur {umur}, IPK {ipk:.2f}\")\n\n# lebar dan perataan: > kanan, < kiri, ^ tengah, 0 isi nol\nprint(f\"[{nama:>8}] [{nama:<8}] [{nama:^8}] [{umur:05d}]\")\n\n# pemisah ribuan, persen, basis lain, notasi ilmiah\nprint(f\"Gaji {7500000:,} | diskon {0.15:.0%} | hex {255:x} | biner {5:b}\")\nprint(f\"{123456.789:.3e} | {umur > 17} | {nama!r}\")\n\n# debugging cepat: {variabel=} mencetak nama dan nilainya\nprint(f\"{umur=}, {ipk=:.1f}\")\n\n# gaya lama yang masih ditemui di kode lama dan logging\nprint(\"Nama: %s, umur %d, IPK %.2f\" % (nama, umur, ipk))\nprint(\"Kode: INV-{:04d}\".format(7))\n\n# struk belanja\nbarang = [\"Kopi susu\", \"Roti bakar\", \"Air mineral\"]\nharga = [18000, 22500, 5000]\nprint(f\"{'Barang':<12} {'Harga':>10}\")\nfor b, h in zip(barang, harga):\n    print(f\"{b:<12} {h:>10,}\")\nprint(f\"{'TOTAL':<12} {sum(harga):>10,}\")",
"out": "Nama: Rina, umur 20, IPK 3.46\n[    Rina] [Rina    ] [  Rina  ] [00020]\nGaji 7,500,000 | diskon 15% | hex ff | biner 101\n1.235e+05 | True | 'Rina'\numur=20, ipk=3.5\nNama: Rina, umur 20, IPK 3.46\nKode: INV-0007\nBarang            Harga\nKopi susu        18,000\nRoti bakar       22,500\nAir mineral       5,000\nTOTAL            45,500",
"pts": [
"Pola umum: [perataan][lebar][.presisi][tipe].",
"Lebar + perataan membuat kolom laporan lurus.",
"Untuk angka ke pengguna, pakai format lokal (id-ID).",
"Kode baru: f-string, template literal, atau String.format."
],
"q": [
[
"Apa arti format %-10s?",
[
"Teks rata kanan selebar 10",
"Teks rata kiri selebar 10",
"10 karakter pertama saja"
],
1,
"Tanda minus berarti rata kiri, angka 10 adalah lebar kolom minimum."
],
[
"Format apa yang menampilkan 7 sebagai 007?",
[
"%.3d atau {x:.3}",
"%03d atau {x:03d}",
"%3d atau {x:3}"
],
1,
"Angka 0 di depan lebar berarti isi nol. Tanpa 0, sisa tempat diisi spasi."
],
[
"3.14159 diformat dengan dua angka desimal hasilnya?",
[
"3.14",
"3.15",
"3.1"
],
0,
"Dibulatkan ke 2 angka di belakang koma: 3.14159 → 3.14."
],
[
"Untuk menampilkan harga ke pengguna Indonesia, cara yang dianjurkan adalah?",
[
"Menyusun titik ribuan sendiri dengan replace",
"Memakai format berbasis lokal id-ID",
"Menampilkan angka mentah"
],
1,
"Format lokal menangani pemisah ribuan, desimal, dan simbol mata uang dengan benar."
]
],
"so": [
{
"q": "Tampilkan daftar 3 mahasiswa dengan kolom rapi: nomor (lebar 3, rata kanan), nama (lebar 10, rata kiri), dan IPK (2 angka desimal). Data: Ani 3.5, Budi 3.257, Citra 3.9.",
"h": "Gabungkan lebar dan perataan dengan presisi. Untuk IPK: lebar 5 dan 2 desimal, misalnya %5.2f atau {ipk:5.2f}.",
"a": "data = [(\"Ani\", 3.5), (\"Budi\", 3.257), (\"Citra\", 3.9)]\nfor no, (nama, ipk) in enumerate(data, start=1):\n    print(f\"{no:>3} {nama:<10} {ipk:5.2f}\")",
"out": "  1 Ani         3.50\n  2 Budi        3.26\n  3 Citra       3.90"
},
{
"q": "Buat nomor antrean 5 pelanggan dengan format A-001 sampai A-005.",
"h": "Isi angka dengan nol di depan sampai 3 digit: %03d di Java, {n:03d} di Python, padStart(3, \"0\") di JavaScript/TypeScript.",
"a": "for n in range(1, 6):\n    print(f\"A-{n:03d}\")",
"out": "A-001\nA-002\nA-003\nA-004\nA-005"
}
]
},
{
"k": "c",
"t": "Kapan for, kapan while, kapan do-while",
"nodes": [
"Loops"
],
"viz": "looppick",
"b": [
"Semua loop bisa saling menggantikan, tetapi programmer yang baik memilih loop yang <b>paling jujur menggambarkan niatnya</b>. Pertanyaan kuncinya satu: <b>apakah jumlah putarannya sudah diketahui sebelum loop dimulai?</b>",
"Jika jumlahnya pasti (5 hari, 10 suku, setiap kursi 1 sampai 40), pakai <b>for</b> seperti <code>for i in range(n)</code>. Jika yang diketahui hanya <b>kondisi berhentinya</b> (sampai saldo cukup, sampai data habis, sampai tidak ada pertukaran lagi), pakai <b>while</b>. Jika badan loop harus jalan <b>minimal sekali</b> sebelum dicek (menampilkan menu, meminta PIN), pakai <b>do-while</b>: <code>while True: ... if kondisi_berhenti: break</code>. Python memang tidak punya do-while, jadi polanya ditulis dengan <code>while True</code> dan <code>break</code>.",
"Untuk membaca setiap isi koleksi tanpa butuh nomor indeks, pakai <b>for-each</b>: <code>for k in daftar</code>. Lebih ringkas dan tidak mungkin salah indeks (error klasik \"off by one\").",
"Pada contoh kode di bawah, keempat jenis loop dipakai sesuai kasusnya masing-masing. Tebak keluarannya dulu, lalu coba latihan memilih loop di visual interaktif."
],
"tb": [
{
"c": "Memilih jenis loop",
"h": [
"Jenis loop",
"Pakai saat",
"Contoh kasus",
"Bentuk di Python"
],
"r": [
[
"for",
"Jumlah putaran sudah diketahui",
"Cetak nomor 1 sampai 40, n suku Fibonacci",
"for i in range(n)"
],
[
"while",
"Hanya kondisi berhenti yang diketahui",
"Menabung sampai target, membaca data sampai habis",
"while kondisi:"
],
[
"do-while",
"Badan loop wajib jalan minimal sekali",
"Menu kasir, meminta PIN",
"while True: ... if kondisi_berhenti: break"
],
[
"for-each",
"Membaca setiap isi koleksi",
"Menjumlahkan harga di keranjang",
"for k in daftar"
]
]
}
],
"code": "# FOR: jumlah pengulangan sudah diketahui (5 hari)\ntotal = 0\nfor hari in range(1, 6):\n    total += 10000\nprint(\"Tabungan 5 hari:\", total)\n\n# WHILE: berhenti saat kondisi tercapai, jumlah putaran belum diketahui\nsaldo, minggu = 0, 0\nwhile saldo < 75000:\n    saldo += 20000\n    minggu += 1\nprint(f\"Target tercapai di minggu ke-{minggu}\")\n\n# Python tidak punya do-while: pakai while True + break\npilihan_user = [2, 1, 0]\ni = 0\nwhile True:\n    pilihan = pilihan_user[i]\n    i += 1\n    print(\"Menu dipilih:\", pilihan)\n    if pilihan == 0:\n        break\n\n# FOR atas koleksi: membaca setiap isi list\nfor k in [\"Medan\", \"Bandung\", \"Makassar\"]:\n    print(\"Kirim ke\", k)",
"out": "Tabungan 5 hari: 50000\nTarget tercapai di minggu ke-4\nMenu dipilih: 2\nMenu dipilih: 1\nMenu dipilih: 0\nKirim ke Medan\nKirim ke Bandung\nKirim ke Makassar",
"pts": [
"Jumlah putaran diketahui → for.",
"Hanya kondisi berhenti yang diketahui → while.",
"Harus jalan minimal sekali → do-while.",
"Hanya membaca isi koleksi → for-each."
],
"q": [
[
"Program meminta pengguna mengetik kata sandi sampai benar. Loop paling cocok?",
[
"for",
"do-while (atau while True + break)",
"for-each"
],
1,
"Pertanyaan harus muncul minimal sekali, dan jumlah percobaannya tidak diketahui."
],
[
"Menghitung rata-rata 30 nilai siswa di sebuah array. Loop paling cocok?",
[
"while",
"for atau for-each",
"do-while"
],
1,
"Jumlah datanya pasti, cukup membaca setiap isi."
],
[
"Mengapa while lebih cocok untuk \"menabung sampai Rp1 juta\"?",
[
"Karena while lebih cepat",
"Karena jumlah minggunya belum diketahui, yang diketahui hanya kondisi berhenti",
"Karena for tidak bisa menjumlah"
],
1,
"Pilihan loop menggambarkan apa yang kita ketahui sebelum mulai."
]
],
"lang": "python",
"so": [
{
"q": "Hitung mundur peluncuran roket: tampilkan 5, 4, 3, 2, 1 lalu \"Meluncur!\". Loop apa yang paling cocok?",
"h": "Awal dan akhir hitungan sudah pasti (5 sampai 1), jadi pakai for yang nilainya berkurang.",
"a": "for detik in range(5, 0, -1):\n    print(detik)\nprint(\"Meluncur!\")",
"out": "5\n4\n3\n2\n1\nMeluncur!"
},
{
"q": "Galon diisi 3 liter setiap menit, mulai dari kosong. Berapa menit sampai isinya minimal 19 liter? Tampilkan menit dan isinya.",
"h": "Jumlah menit belum diketahui, yang diketahui hanya kondisi berhenti (isi ≥ 19). Itu tanda while.",
"a": "isi, menit = 0, 0\nwhile isi < 19:\n    isi += 3\n    menit += 1\nprint(f\"{menit} menit, isi {isi} liter\")",
"out": "7 menit, isi 21 liter"
}
]
},
{
"k": "c",
"t": "Bilangan Fibonacci: for dan while",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "FibonacciDiBawah100",
"p": [
{
"t": "dec",
"v": "a, b, c, banyak",
"ty": "Integer"
},
{
"t": "asg",
"v": "a",
"e": "0"
},
{
"t": "asg",
"v": "b",
"e": "1"
},
{
"t": "asg",
"v": "banyak",
"e": "0"
},
{
"t": "while",
"c": "a < 100",
"b": [
{
"t": "asg",
"v": "banyak",
"e": "banyak + 1"
},
{
"t": "asg",
"v": "c",
"e": "a + b"
},
{
"t": "asg",
"v": "a",
"e": "b"
},
{
"t": "asg",
"v": "b",
"e": "c"
}
]
},
{
"t": "out",
"e": "\"Banyak suku: \" & banyak"
}
]
},
"b": [
"Deret Fibonacci dimulai dari 0 dan 1, lalu setiap suku adalah jumlah dua suku sebelumnya: 0, 1, 1, 2, 3, 5, 8, 13, ... Polanya muncul di banyak tempat, dari susunan biji bunga matahari sampai soal tes kerja programmer.",
"Kuncinya adalah dua variabel <code>a</code> dan <code>b</code> yang terus <b>digeser</b>: <code>a</code> menjadi <code>b</code>, dan <code>b</code> menjadi <code>a + b</code>. Python bisa menggeser keduanya sekaligus dengan <code>a, b = b, a + b</code>.",
"Perhatikan dua bagian contoh. \"10 suku pertama\" memakai <b>for</b> karena jumlah putarannya pasti 10. \"Semua suku di bawah 100\" memakai <b>while</b> karena kita tidak tahu ada berapa suku sampai benar-benar menghitungnya.",
"Visual di bawah menjalankan bagian while langkah demi langkah sebagai flowchart dan pseudocode. Perhatikan kolom <b>Variabel</b>: nilai yang berubah diberi warna."
],
"tb": [
{
"c": "Jejak variabel 6 putaran pertama",
"h": [
"Putaran",
"a",
"b",
"Suku yang dicatat"
],
"r": [
[
"1",
"0",
"1",
"0"
],
[
"2",
"1",
"1",
"1"
],
[
"3",
"1",
"2",
"1"
],
[
"4",
"2",
"3",
"2"
],
[
"5",
"3",
"5",
"3"
],
[
"6",
"5",
"8",
"5"
]
]
}
],
"code": "# FOR: n suku pertama (jumlah putaran diketahui)\nn = 10\na, b = 0, 1\nderet = []\nfor _ in range(n):\n    deret.append(a)\n    a, b = b, a + b\nprint(\"10 suku pertama:\", *deret)\n\n# WHILE: semua suku di bawah 100 (jumlah putaran belum diketahui)\na, b = 0, 1\nbanyak = 0\nwhile a < 100:\n    banyak += 1\n    a, b = b, a + b\nprint(\"Banyak suku di bawah 100:\", banyak)",
"out": "10 suku pertama: 0 1 1 2 3 5 8 13 21 34\nBanyak suku di bawah 100: 12",
"pts": [
"Fibonacci butuh dua variabel yang terus digeser.",
"n suku pertama → for; suku di bawah batas → while.",
"Geser nilai dengan urutan yang benar agar nilai lama tidak hilang."
],
"q": [
[
"Suku Fibonacci ke-8 (mulai dari 0) adalah?",
[
"8",
"13",
"21"
],
1,
"0, 1, 1, 2, 3, 5, 8, 13: suku ke-8 adalah 13."
],
[
"Mengapa menghitung \"suku di bawah 1000\" memakai while?",
[
"Karena jumlah sukunya belum diketahui sebelum dihitung",
"Karena for tidak bisa memakai angka besar",
"Karena while selalu lebih cepat"
],
0,
"Batasnya nilai, bukan banyak putaran."
]
],
"lang": "python",
"so": [
{
"q": "Tampilkan hanya suku Fibonacci ke-20 (suku pertama adalah 0).",
"h": "Kamu tahu persis butuh 19 kali geser pasangan (a, b), jadi pakai for. Tidak perlu menyimpan semua suku.",
"a": "a, b = 0, 1\nfor _ in range(19):\n    a, b = b, a + b\nprint(\"Suku ke-20:\", a)",
"out": "Suku ke-20: 4181"
},
{
"q": "Cari suku Fibonacci pertama yang lebih dari 1000, dan suku ke berapa itu.",
"h": "Kamu tidak tahu butuh berapa suku, jadi pakai while dengan kondisi a <= 1000.",
"a": "a, b, ke = 0, 1, 1\nwhile a <= 1000:\n    a, b = b, a + b\n    ke += 1\nprint(f\"Suku ke-{ke}: {a}\")",
"out": "Suku ke-18: 1597"
}
]
},
{
"k": "c",
"t": "Bubble sort: loop di dalam loop",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BubbleSort",
"p": [
{
"t": "dec",
"v": "a",
"ty": "Integer",
"arr": "4"
},
{
"t": "asg",
"v": "a",
"e": "[25, 12, 22, 11]"
},
{
"t": "dec",
"v": "j, t, putaran",
"ty": "Integer"
},
{
"t": "dec",
"v": "adaTukar",
"ty": "Boolean"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
},
{
"t": "asg",
"v": "putaran",
"e": "0"
},
{
"t": "while",
"c": "adaTukar",
"b": [
{
"t": "asg",
"v": "adaTukar",
"e": "false"
},
{
"t": "asg",
"v": "putaran",
"e": "putaran + 1"
},
{
"t": "for",
"v": "j",
"a": "0",
"z": "3 - putaran",
"b": [
{
"t": "if",
"c": "a[j] > a[j + 1]",
"y": [
{
"t": "asg",
"v": "t",
"e": "a[j]"
},
{
"t": "asg",
"v": "a[j]",
"e": "a[j + 1]"
},
{
"t": "asg",
"v": "a[j + 1]",
"e": "t"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
}
],
"n": []
}
]
}
]
},
{
"t": "out",
"e": "\"Terurut: \" & a"
}
]
},
"b": [
"Bubble sort mengurutkan data dengan cara paling sederhana: bandingkan dua angka yang <b>bersebelahan</b>, tukar jika urutannya salah, lalu geser ke pasangan berikutnya. Setelah satu putaran, angka terbesar pasti sudah \"menggelembung\" ke ujung kanan.",
"Algoritma ini memakai dua loop. <b>Loop dalam (for)</b> berjalan dari kiri ke kanan, jumlah pasangannya jelas. <b>Loop luar (while)</b> mengulang putaran selama masih ada pertukaran. Variabel penanda <code>ada_tukar</code> membuat program berhenti lebih awal jika data sudah terurut.",
"Setiap putaran, satu angka terbesar sudah di tempatnya, jadi loop dalam cukup sampai <code>n - putaran</code>. Detail kecil ini menghemat perbandingan yang tidak perlu.",
"Bubble sort lambat untuk data besar (sekitar n² perbandingan), jadi di dunia kerja kita memakai fungsi sort bawaan bahasa. Tetapi bubble sort adalah latihan terbaik untuk memahami loop bersarang, indeks, dan menukar nilai."
],
"tb": [
{
"c": "Isi array setiap putaran",
"h": [
"Putaran",
"Isi array",
"Yang sudah di tempat"
],
"r": [
[
"Awal",
"64 25 12 22 11",
"-"
],
[
"1",
"25 12 22 11 64",
"64"
],
[
"2",
"12 22 11 25 64",
"25, 64"
],
[
"3",
"12 11 22 25 64",
"22, 25, 64"
],
[
"4",
"11 12 22 25 64",
"semua"
]
]
}
],
"code": "nilai = [64, 25, 12, 22, 11]\nn = len(nilai)\nada_tukar = True\nputaran = 0\n# WHILE luar: berhenti jika satu putaran tidak ada pertukaran\nwhile ada_tukar:\n    ada_tukar = False\n    putaran += 1\n    # FOR dalam: bandingkan pasangan bersebelahan\n    for j in range(n - putaran):\n        if nilai[j] > nilai[j + 1]:\n            nilai[j], nilai[j + 1] = nilai[j + 1], nilai[j]\n            ada_tukar = True\n    print(f\"Putaran {putaran}: {nilai}\")\nprint(\"Terurut:\", nilai)",
"out": "Putaran 1: [25, 12, 22, 11, 64]\nPutaran 2: [12, 22, 11, 25, 64]\nPutaran 3: [12, 11, 22, 25, 64]\nPutaran 4: [11, 12, 22, 25, 64]\nPutaran 5: [11, 12, 22, 25, 64]\nTerurut: [11, 12, 22, 25, 64]",
"pts": [
"Bandingkan pasangan bersebelahan, tukar jika salah urutan.",
"Loop dalam for (jumlah pasangan jelas), loop luar while (sampai tidak ada pertukaran).",
"Penanda pertukaran membuat sort berhenti lebih awal."
],
"q": [
[
"Setelah putaran pertama bubble sort (urut naik), di mana angka terbesar?",
[
"Di indeks 0",
"Di ujung kanan",
"Belum pasti"
],
1,
"Angka terbesar selalu terbawa sampai ujung kanan pada putaran pertama."
],
[
"Untuk apa variabel penanda pertukaran?",
[
"Menghitung jumlah data",
"Menghentikan loop luar jika satu putaran tidak ada pertukaran",
"Menyimpan angka terbesar"
],
1,
"Jika tidak ada pertukaran, data sudah terurut."
],
[
"Kenapa loop dalam cukup sampai n - putaran?",
[
"Agar tidak error",
"Karena angka di ujung kanan sudah pasti di tempatnya",
"Karena aturan bahasa"
],
1,
"Bagian kanan yang sudah terurut tidak perlu dibandingkan lagi."
]
],
"lang": "python",
"so": [
{
"q": "Urutkan nama [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"] sesuai abjad dengan bubble sort.",
"h": "Logikanya sama, hanya cara membandingkan teks yang berbeda: Python memakai >, JavaScript/TypeScript memakai localeCompare, Java memakai compareTo.",
"a": "nama = [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"]\nada_tukar = True\nwhile ada_tukar:\n    ada_tukar = False\n    for j in range(len(nama) - 1):\n        if nama[j] > nama[j + 1]:\n            nama[j], nama[j + 1] = nama[j + 1], nama[j]\n            ada_tukar = True\nprint(nama)",
"out": "['Agus', 'Budi', 'Dewi', 'Rina']"
},
{
"q": "Ubah bubble sort agar mengurutkan dari besar ke kecil, lalu hitung berapa kali terjadi pertukaran untuk [3, 1, 4, 1, 5].",
"h": "Cukup balik tanda perbandingan menjadi <, dan tambah penghitung setiap kali menukar.",
"a": "data = [3, 1, 4, 1, 5]\ntukar = 0\nfor i in range(len(data) - 1):\n    for j in range(len(data) - 1 - i):\n        if data[j] < data[j + 1]:\n            data[j], data[j + 1] = data[j + 1], data[j]\n            tukar += 1\nprint(data, \"pertukaran:\", tukar)",
"out": "[5, 4, 3, 1, 1] pertukaran: 6"
}
]
},
{
"k": "c",
"t": "FizzBuzz dan bilangan prima: break dan loop bersarang",
"nodes": [
"Loops",
"Conditionals"
],
"viz": "fc",
"fc": {
"name": "CekPrima",
"in": [
"29"
],
"p": [
{
"t": "dec",
"v": "x, d",
"ty": "Integer"
},
{
"t": "dec",
"v": "prima",
"ty": "Boolean"
},
{
"t": "in",
"v": "x"
},
{
"t": "asg",
"v": "prima",
"e": "x >= 2"
},
{
"t": "asg",
"v": "d",
"e": "2"
},
{
"t": "while",
"c": "d * d <= x and prima",
"b": [
{
"t": "if",
"c": "x mod d = 0",
"y": [
{
"t": "asg",
"v": "prima",
"e": "false"
}
],
"n": []
},
{
"t": "asg",
"v": "d",
"e": "d + 1"
}
]
},
{
"t": "if",
"c": "prima",
"y": [
{
"t": "out",
"e": "x & \" adalah prima\""
}
],
"n": [
{
"t": "out",
"e": "x & \" bukan prima\""
}
]
}
]
},
"b": [
"<b>FizzBuzz</b> adalah soal wawancara klasik: untuk angka 1 sampai 15, tampilkan \"Fizz\" jika habis dibagi 3, \"Buzz\" jika habis dibagi 5, \"FizzBuzz\" jika habis dibagi keduanya, dan angkanya sendiri jika tidak. Rentangnya jelas, jadi pakai <b>for</b>. Jebakannya: cek kelipatan 15 lebih dulu, karena jika cek 3 duluan, angka 15 sudah keburu menjadi \"Fizz\".",
"<b>Bilangan prima</b> hanya habis dibagi 1 dan dirinya sendiri. Untuk setiap angka (loop luar), kita coba pembagi dari 2 (loop dalam). Begitu ketemu satu pembagi, angka itu pasti bukan prima, jadi <b>break</b> menghentikan loop dalam tanpa membuang waktu.",
"Pembagi cukup dicoba sampai akar angkanya (<code>d * d &lt;= x</code>). Jika 36 = 4 × 9, salah satu faktornya pasti ≤ 6. Ini mengubah 1.000 percobaan menjadi sekitar 31. Python punya fitur unik <code>for ... else</code>: blok else jalan hanya jika loop selesai <b>tanpa</b> break.",
"Visual di bawah memeriksa satu angka dengan while dan penanda, karena Flowgorithm tidak punya break. Ganti inputnya, misalnya 91 atau 97, lalu jalankan."
],
"tb": [
{
"c": "break dan continue",
"h": [
"Perintah",
"Efek",
"Kapan dipakai"
],
"r": [
[
"break",
"Keluar dari loop terdekat",
"Jawaban sudah ditemukan, sisa putaran tidak perlu"
],
[
"continue",
"Lompat ke putaran berikutnya",
"Lewati data yang tidak relevan"
],
[
"penanda (flag)",
"Variabel boolean yang dicek setelah loop",
"Bahasa atau alat tanpa break, misalnya Flowgorithm"
]
]
}
],
"code": "# FizzBuzz: FOR karena rentangnya jelas (1 sampai 15)\nhasil = []\nfor i in range(1, 16):\n    if i % 15 == 0:\n        hasil.append(\"FizzBuzz\")\n    elif i % 3 == 0:\n        hasil.append(\"Fizz\")\n    elif i % 5 == 0:\n        hasil.append(\"Buzz\")\n    else:\n        hasil.append(str(i))\nprint(\" \".join(hasil))\n\n# Bilangan prima 2..30: FOR bersarang + break\nprima = []\nfor x in range(2, 31):\n    for d in range(2, int(x ** 0.5) + 1):\n        if x % d == 0:\n            break           # tidak perlu cek pembagi lain\n    else:\n        prima.append(x)     # for-else: jalan jika loop tidak di-break\nprint(\"Prima:\", *prima)",
"out": "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\nPrima: 2 3 5 7 11 13 17 19 23 29",
"pts": [
"Urutan if penting: kondisi paling khusus dicek lebih dulu.",
"break menghentikan loop terdekat saat jawaban sudah pasti.",
"Pembagi prima cukup dicek sampai akar angkanya."
],
"q": [
[
"Jika FizzBuzz mengecek \"habis dibagi 3\" lebih dulu, apa yang tampil untuk 15?",
[
"FizzBuzz",
"Fizz",
"Buzz"
],
1,
"Kondisi pertama yang benar langsung dipakai."
],
[
"Pada loop bersarang, break menghentikan loop yang mana?",
[
"Semua loop",
"Loop terdekat yang membungkusnya",
"Loop terluar"
],
1,
"break hanya keluar dari satu tingkat loop."
],
[
"Untuk mengecek apakah 97 prima, pembagi paling besar yang perlu dicoba adalah?",
[
"96",
"48",
"9"
],
2,
"9 × 9 = 81 ≤ 97, sedangkan 10 × 10 = 100 > 97."
]
],
"lang": "python",
"so": [
{
"q": "Tampilkan tabel perkalian 1 sampai 5 dalam bentuk kotak (5 baris, 5 kolom).",
"h": "For luar untuk baris, for dalam untuk kolom. Keduanya punya batas yang jelas.",
"a": "for i in range(1, 6):\n    baris = \"\"\n    for j in range(1, 6):\n        baris += f\"{i * j:4}\"\n    print(baris)",
"out": "   1   2   3   4   5\n   2   4   6   8  10\n   3   6   9  12  15\n   4   8  12  16  20\n   5  10  15  20  25"
},
{
"q": "Cari bilangan prima pertama yang lebih besar dari 100.",
"h": "Kita tidak tahu harus mencoba berapa angka, jadi loop luar memakai while. Pengecekan pembagi tetap memakai for dengan break.",
"a": "x = 101\nwhile True:\n    prima = True\n    for d in range(2, int(x ** 0.5) + 1):\n        if x % d == 0:\n            prima = False\n            break\n    if prima:\n        break\n    x += 1\nprint(\"Prima pertama > 100:\", x)",
"out": "Prima pertama > 100: 101"
}
]
},
{
"k": "c",
"t": "Faktorial, jumlah digit, dan palindrom",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "JumlahDigit",
"in": [
"90417"
],
"p": [
{
"t": "dec",
"v": "angka, jumlah",
"ty": "Integer"
},
{
"t": "in",
"v": "angka"
},
{
"t": "asg",
"v": "jumlah",
"e": "0"
},
{
"t": "while",
"c": "angka > 0",
"b": [
{
"t": "asg",
"v": "jumlah",
"e": "jumlah + angka mod 10"
},
{
"t": "asg",
"v": "angka",
"e": "Int(angka / 10)"
}
]
},
{
"t": "out",
"e": "\"Jumlah digit: \" & jumlah"
}
]
},
"b": [
"Tiga soal ini melatih kapan memakai for dan kapan while. <b>Faktorial</b> 5! = 1 × 2 × 3 × 4 × 5: banyak perkaliannya pasti, jadi <b>for</b>.",
"<b>Jumlah digit</b> 90417 = 9 + 0 + 4 + 1 + 7 = 21. Kita tidak tahu angkanya punya berapa digit, jadi pakai <b>while</b>: ambil digit terakhir dengan <code>% 10</code>, lalu buang dengan pembagian bulat <code>// 10</code>. Berhenti saat angkanya habis (0).",
"<b>Palindrom</b> adalah kata yang sama jika dibaca dari depan dan belakang, seperti \"katak\". Pakai <b>dua penunjuk</b>: satu dari kiri, satu dari kanan, bergerak ke tengah selama <code>kiri &lt; kanan</code>. Begitu ada huruf yang berbeda, langsung break.",
"Visual di bawah menjalankan jumlah digit. Coba ganti inputnya dengan angka lain dan hitung dulu di kepala sebelum menekan Berikutnya."
],
"tb": [
{
"c": "Jejak jumlah digit 90417",
"h": [
"Putaran",
"angka % 10",
"jumlah",
"angka setelah dibagi 10"
],
"r": [
[
"1",
"7",
"7",
"9041"
],
[
"2",
"1",
"8",
"904"
],
[
"3",
"4",
"12",
"90"
],
[
"4",
"0",
"12",
"9"
],
[
"5",
"9",
"21",
"0"
]
]
}
],
"code": "# Faktorial: FOR, jumlah perkalian = n\nn = 5\nfaktorial = 1\nfor i in range(2, n + 1):\n    faktorial *= i\nprint(f\"{n}! = {faktorial}\")\n\n# Jumlah digit: WHILE, banyak digit belum diketahui\nangka = 90417\nsisa, jumlah = angka, 0\nwhile sisa > 0:\n    jumlah += sisa % 10   # ambil digit terakhir\n    sisa //= 10           # buang digit terakhir\nprint(f\"Jumlah digit {angka} = {jumlah}\")\n\n# Palindrom: WHILE dua penunjuk bergerak ke tengah\nkata = \"katak\"\nkiri, kanan = 0, len(kata) - 1\npalindrom = True\nwhile kiri < kanan:\n    if kata[kiri] != kata[kanan]:\n        palindrom = False\n        break\n    kiri += 1\n    kanan -= 1\nprint(f\"{kata} palindrom? {palindrom}\")",
"out": "5! = 120\nJumlah digit 90417 = 21\nkatak palindrom? True",
"pts": [
"% 10 mengambil digit terakhir, bagi 10 (bulat) membuangnya.",
"Banyak digit tidak diketahui → while.",
"Dua penunjuk bergerak ke tengah untuk memeriksa palindrom."
],
"q": [
[
"Berapa hasil 4827 % 10?",
[
"4",
"7",
"482"
],
1,
"Sisa bagi 10 adalah digit terakhir."
],
[
"Loop paling cocok untuk menghitung 10! (faktorial 10)?",
[
"for",
"while",
"do-while"
],
0,
"Banyak perkaliannya pasti."
],
[
"Pada pemeriksaan palindrom \"level\", berapa kali perbandingan huruf terjadi?",
[
"5",
"2",
"1"
],
1,
"Pasangan (l, l) dan (e, e); huruf tengah v tidak perlu dibandingkan."
]
],
"lang": "python",
"so": [
{
"q": "Balik angka 12345 menjadi 54321 tanpa mengubahnya menjadi teks.",
"h": "Ambil digit terakhir dengan % 10, tempel ke hasil dengan hasil * 10 + digit, buang digit terakhir dengan pembagian bulat. Ulangi selama angka > 0.",
"a": "angka, balik = 12345, 0\nwhile angka > 0:\n    balik = balik * 10 + angka % 10\n    angka //= 10\nprint(\"Dibalik:\", balik)",
"out": "Dibalik: 54321"
},
{
"q": "Hitung 2 pangkat 10 dengan loop, tanpa operator pangkat.",
"h": "Perkalian diulang tepat 10 kali, jadi for.",
"a": "hasil = 1\nfor _ in range(10):\n    hasil *= 2\nprint(\"2^10 =\", hasil)",
"out": "2^10 = 1024"
}
]
},
{
"k": "c",
"t": "Binary search: membagi dua sampai ketemu",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BinarySearch",
"in": [
"20000"
],
"p": [
{
"t": "dec",
"v": "harga",
"ty": "Integer",
"arr": "7"
},
{
"t": "asg",
"v": "harga",
"e": "[5000, 8000, 12000, 15000, 20000, 27000, 35000]"
},
{
"t": "dec",
"v": "cari, kiri, kanan, tengah, posisi",
"ty": "Integer"
},
{
"t": "in",
"v": "cari"
},
{
"t": "asg",
"v": "kiri",
"e": "0"
},
{
"t": "asg",
"v": "kanan",
"e": "6"
},
{
"t": "asg",
"v": "posisi",
"e": "-1"
},
{
"t": "while",
"c": "kiri <= kanan and posisi = -1",
"b": [
{
"t": "asg",
"v": "tengah",
"e": "Int((kiri + kanan) / 2)"
},
{
"t": "if",
"c": "harga[tengah] = cari",
"y": [
{
"t": "asg",
"v": "posisi",
"e": "tengah"
}
],
"n": [
{
"t": "if",
"c": "harga[tengah] < cari",
"y": [
{
"t": "asg",
"v": "kiri",
"e": "tengah + 1"
}
],
"n": [
{
"t": "asg",
"v": "kanan",
"e": "tengah - 1"
}
]
}
]
}
]
},
{
"t": "out",
"e": "\"Posisi: \" & posisi"
}
]
},
"b": [
"Mencari harga di daftar 1.000 barang satu per satu (linear search) bisa butuh 1.000 langkah. Jika daftarnya <b>sudah terurut</b>, kita bisa jauh lebih cepat: lihat bagian tengah, lalu buang separuh daftar yang pasti tidak berisi jawabannya.",
"Simpan dua batas, <code>kiri</code> dan <code>kanan</code>. Selama <code>kiri &lt;= kanan</code>, hitung <code>tengah</code>. Jika nilai tengah terlalu kecil, geser kiri ke tengah + 1. Jika terlalu besar, geser kanan ke tengah - 1. Banyak langkahnya tidak diketahui sebelumnya, jadi loopnya <b>while</b>.",
"Setiap langkah membuang separuh data, jadi 1.000 data cukup dicari dalam paling banyak 10 langkah, dan 1 juta data dalam 20 langkah. Inilah alasan database dan kamus memakai data terurut.",
"Visual di bawah mencari harga di 7 data. Coba input 5000, 35000, atau 9000 (tidak ada di daftar) dan perhatikan bagaimana kiri dan kanan bergerak."
],
"tb": [
{
"c": "Linear search vs binary search",
"h": [
"Aspek",
"Linear search",
"Binary search"
],
"r": [
[
"Syarat data",
"Bebas",
"Harus terurut"
],
[
"Langkah terburuk (1.000 data)",
"1.000",
"10"
],
[
"Jenis loop",
"for (setiap data)",
"while (sampai ketemu atau habis)"
],
[
"Kapan dipakai",
"Data sedikit atau tidak terurut",
"Data besar dan terurut"
]
]
}
],
"code": "harga = [5000, 8000, 12000, 15000, 20000, 27000, 35000]\ncari = 20000\nkiri, kanan = 0, len(harga) - 1\nlangkah, posisi = 0, -1\n# WHILE: berhenti saat ketemu atau ruang pencarian habis\nwhile kiri <= kanan:\n    langkah += 1\n    tengah = (kiri + kanan) // 2\n    print(f\"Langkah {langkah}: cek indeks {tengah} ({harga[tengah]})\")\n    if harga[tengah] == cari:\n        posisi = tengah\n        break\n    elif harga[tengah] < cari:\n        kiri = tengah + 1\n    else:\n        kanan = tengah - 1\nprint(f\"Ketemu di indeks {posisi} setelah {langkah} langkah\")",
"out": "Langkah 1: cek indeks 3 (15000)\nLangkah 2: cek indeks 5 (27000)\nLangkah 3: cek indeks 4 (20000)\nKetemu di indeks 4 setelah 3 langkah",
"pts": [
"Binary search hanya untuk data terurut.",
"Setiap langkah membuang separuh ruang pencarian.",
"Berhenti saat ketemu atau kiri > kanan."
],
"q": [
[
"Apa syarat utama binary search?",
[
"Data berupa angka",
"Data sudah terurut",
"Data kurang dari 100"
],
1,
"Tanpa urutan, kita tidak tahu separuh mana yang harus dibuang."
],
[
"Jika harga[tengah] lebih kecil dari yang dicari, apa yang dilakukan?",
[
"kanan = tengah - 1",
"kiri = tengah + 1",
"Berhenti"
],
1,
"Jawabannya pasti di sebelah kanan tengah."
],
[
"Kira-kira berapa langkah maksimum untuk 1 juta data terurut?",
[
"20",
"1.000",
"500.000"
],
0,
"2 pangkat 20 ≈ 1 juta."
]
],
"lang": "python",
"so": [
{
"q": "Komputer menebak angka rahasia 73 di antara 1 sampai 100 dengan cara binary search. Tampilkan setiap tebakan.",
"h": "Sama seperti mencari di array terurut, hanya saja \"array\"-nya adalah rentang angka 1 sampai 100.",
"a": "rahasia, bawah, atas = 73, 1, 100\nwhile True:\n    tebak = (bawah + atas) // 2\n    print(\"Tebak\", tebak)\n    if tebak == rahasia:\n        break\n    if tebak < rahasia:\n        bawah = tebak + 1\n    else:\n        atas = tebak - 1",
"out": "Tebak 50\nTebak 75\nTebak 62\nTebak 68\nTebak 71\nTebak 73"
},
{
"q": "Berapa langkah paling banyak yang dibutuhkan binary search untuk 1.000 data? Hitung dengan membagi dua terus sampai habis.",
"h": "Selama masih ada data (n > 0), bagi dua dan tambah 1 langkah. Ini while karena jumlah langkah adalah hal yang dicari.",
"a": "n, langkah = 1000, 0\nwhile n > 0:\n    n //= 2\n    langkah += 1\nprint(\"Maksimal\", langkah, \"langkah\")",
"out": "Maksimal 10 langkah"
}
]
}
]
},
"ts": {
"t": "Format keluaran dan latihan algoritma",
"lvl": "Menengah",
"d": "Format specifier, Fibonacci, bubble sort, FizzBuzz, bilangan prima, palindrom, dan binary search di TypeScript, dengan alasan memilih for, while, do-while, atau for-each.",
"nodes": [
"Loops",
"Arrays"
],
"lessons": [
{
"k": "c",
"t": "Format specifier: merapikan keluaran",
"nodes": [
"Basic Syntax"
],
"lang": "ts",
"b": [
"<b>Format specifier</b> adalah kode kecil yang mengatur <b>bagaimana sebuah nilai ditampilkan</b>: berapa angka di belakang koma, selebar apa kolomnya, rata kiri atau kanan, diberi nol di depan, atau diberi pemisah ribuan. Nilainya tidak berubah, hanya tampilannya. Hampir semua program nyata membutuhkannya: struk belanja, laporan nilai, nomor invoice, dan log server.",
"Polanya mirip di semua bahasa: <b>[perataan][lebar][.presisi][tipe]</b>. Contoh <code>%-10s</code> berarti teks rata kiri selebar 10, <code>%8.2f</code> berarti desimal 2 angka dalam kolom selebar 8, dan <code>%05d</code> berarti bilangan bulat selebar 5 yang diisi nol di depan.",
"JavaScript dan TypeScript tidak punya printf. Gantinya: <b>template literal</b> <code>`${nilai}`</code> untuk menyisipkan nilai, <code>toFixed(2)</code> untuk presisi, <code>padStart</code>/<code>padEnd</code> untuk lebar dan perataan, dan <code>toString(16)</code> untuk basis lain. <code>console.log</code> mengenal <code>%s %d %f %o</code>, tetapi hanya untuk mencetak ke konsol.",
"Untuk angka dan uang yang tampil ke pengguna, industri memakai <code>Intl.NumberFormat</code> atau <code>toLocaleString(\"id-ID\")</code>, sehingga 7500000 tampil sebagai 7.500.000 atau Rp 7.500.000 sesuai aturan Indonesia. Hindari menyusun format uang sendiri dengan replace atau regex. TypeScript menambahkan pengecekan tipe: <code>toFixed</code> hanya bisa dipanggil pada <code>number</code>, jadi salah tipe ketahuan sebelum program dijalankan.",
"Contoh terakhir di kode adalah <b>struk belanja</b>: format di dalam loop membuat setiap baris punya lebar kolom yang sama, sehingga angka tersusun rapi ke kanan. Ini pola yang akan sering kamu pakai di soal-soal berikutnya."
],
"tb": [
{
"c": "Format specifier di berbagai bahasa",
"h": [
"Tujuan",
"Java / C (printf)",
"Python (f-string)",
"JavaScript / TypeScript"
],
"r": [
[
"Teks",
"%s",
"{x}",
"${x}"
],
[
"Bilangan bulat",
"%d",
"{x:d}",
"${x}"
],
[
"Desimal 2 angka",
"%.2f",
"{x:.2f}",
"x.toFixed(2)"
],
[
"Lebar 8, rata kanan",
"%8s",
"{x:>8}",
"String(x).padStart(8)"
],
[
"Lebar 8, rata kiri",
"%-8s",
"{x:<8}",
"String(x).padEnd(8)"
],
[
"Isi nol di depan",
"%05d",
"{x:05d}",
"String(x).padStart(5, \"0\")"
],
[
"Pemisah ribuan",
"%,d",
"{x:,}",
"x.toLocaleString(\"id-ID\")"
],
[
"Persen",
"%.0f%%",
"{x:.0%}",
"(x * 100).toFixed(0) + \"%\""
],
[
"Heksadesimal",
"%x",
"{x:x}",
"x.toString(16)"
],
[
"Notasi ilmiah",
"%.3e",
"{x:.3e}",
"x.toExponential(3)"
],
[
"Baris baru",
"%n atau \\n",
"\\n",
"\\n"
]
]
},
{
"c": "Yang paling sering dipakai di industri",
"h": [
"Kebutuhan",
"Pilihan umum",
"Alasan"
],
"r": [
[
"Menyusun teks di kode baru",
"f-string (Python), template literal (JS/TS), String.format atau formatted() (Java)",
"Paling mudah dibaca dan dirawat"
],
[
"Angka dan uang ke pengguna",
"Format berbasis lokal: Intl.NumberFormat, Locale id-ID, Babel",
"Titik, koma, dan simbol Rp mengikuti aturan negara"
],
[
"Laporan dan struk berkolom",
"Lebar + perataan: %-12s, %10.2f, padEnd/padStart",
"Kolom tetap lurus berapa pun panjang datanya"
],
[
"Kode dokumen dan antrean",
"Isi nol: %04d, {n:04d}",
"INV-0007 lebih mudah diurutkan dan dicari"
],
[
"Logging",
"Placeholder %s atau {}: logger.info(\"user %s\", id)",
"Teks hanya disusun jika log benar-benar dicetak"
],
[
"Tanggal",
"ISO 8601 (2026-11-02) atau pola yyyy-MM-dd",
"Standar internasional dan mudah diurutkan"
]
]
}
],
"code": "const nama: string = \"Rina\";\nconst umur: number = 20;\nconst ipk: number = 3.4567;\n// template literal: ${ekspresi}, angka desimal dengan toFixed\nconsole.log(`Nama: ${nama}, umur ${umur}, IPK ${ipk.toFixed(2)}`);\n\n// lebar dan perataan: padStart (rata kanan), padEnd (rata kiri)\nconsole.log(`[${nama.padStart(8)}] [${nama.padEnd(8)}] [${String(umur).padStart(5, \"0\")}]`);\n\n// basis lain, notasi ilmiah, persen\nconsole.log(`hex ${(255).toString(16)} | biner ${(5).toString(2)} | ${(123456.789).toExponential(3)} | ${(0.15 * 100).toFixed(0)}%`);\n\n// format lokal Indonesia: ribuan dengan titik, mata uang Rupiah\nconst rupiah: Intl.NumberFormat = new Intl.NumberFormat(\"id-ID\", { style: \"currency\", currency: \"IDR\", maximumFractionDigits: 0 });\nconsole.log((7500000).toLocaleString(\"id-ID\"), \"|\", rupiah.format(7500000));\n\n// console.log juga mengenal %s %d %f %o (gaya printf)\nconsole.log(\"Nama: %s, umur %d\", nama, umur);\n\n// struk belanja\nconst barang: string[] = [\"Kopi susu\", \"Roti bakar\", \"Air mineral\"];\nconst harga: number[] = [18000, 22500, 5000];\nconsole.log(`${\"Barang\".padEnd(12)} ${\"Harga\".padStart(10)}`);\nbarang.forEach((b, i) => console.log(`${b.padEnd(12)} ${harga[i].toLocaleString(\"id-ID\").padStart(10)}`));\nconst total: number = harga.reduce((a, b) => a + b, 0);\nconsole.log(`${\"TOTAL\".padEnd(12)} ${total.toLocaleString(\"id-ID\").padStart(10)}`);",
"out": "Nama: Rina, umur 20, IPK 3.46\n[    Rina] [Rina    ] [00020]\nhex ff | biner 101 | 1.235e+5 | 15%\n7.500.000 | Rp 7.500.000\nNama: Rina, umur 20\nBarang            Harga\nKopi susu        18.000\nRoti bakar       22.500\nAir mineral       5.000\nTOTAL            45.500",
"pts": [
"Pola umum: [perataan][lebar][.presisi][tipe].",
"Lebar + perataan membuat kolom laporan lurus.",
"Untuk angka ke pengguna, pakai format lokal (id-ID).",
"Kode baru: f-string, template literal, atau String.format."
],
"q": [
[
"Apa arti format %-10s?",
[
"Teks rata kanan selebar 10",
"Teks rata kiri selebar 10",
"10 karakter pertama saja"
],
1,
"Tanda minus berarti rata kiri, angka 10 adalah lebar kolom minimum."
],
[
"Format apa yang menampilkan 7 sebagai 007?",
[
"%.3d atau {x:.3}",
"%03d atau {x:03d}",
"%3d atau {x:3}"
],
1,
"Angka 0 di depan lebar berarti isi nol. Tanpa 0, sisa tempat diisi spasi."
],
[
"3.14159 diformat dengan dua angka desimal hasilnya?",
[
"3.14",
"3.15",
"3.1"
],
0,
"Dibulatkan ke 2 angka di belakang koma: 3.14159 → 3.14."
],
[
"Untuk menampilkan harga ke pengguna Indonesia, cara yang dianjurkan adalah?",
[
"Menyusun titik ribuan sendiri dengan replace",
"Memakai format berbasis lokal id-ID",
"Menampilkan angka mentah"
],
1,
"Format lokal menangani pemisah ribuan, desimal, dan simbol mata uang dengan benar."
]
],
"so": [
{
"q": "Tampilkan daftar 3 mahasiswa dengan kolom rapi: nomor (lebar 3, rata kanan), nama (lebar 10, rata kiri), dan IPK (2 angka desimal). Data: Ani 3.5, Budi 3.257, Citra 3.9.",
"h": "Gabungkan lebar dan perataan dengan presisi. Untuk IPK: lebar 5 dan 2 desimal, misalnya %5.2f atau {ipk:5.2f}.",
"a": "const data: [string, number][] = [[\"Ani\", 3.5], [\"Budi\", 3.257], [\"Citra\", 3.9]];\ndata.forEach(([nama, ipk], i) => {\n  console.log(`${String(i + 1).padStart(3)} ${nama.padEnd(10)} ${ipk.toFixed(2).padStart(5)}`);\n});",
"out": "  1 Ani         3.50\n  2 Budi        3.26\n  3 Citra       3.90"
},
{
"q": "Buat nomor antrean 5 pelanggan dengan format A-001 sampai A-005.",
"h": "Isi angka dengan nol di depan sampai 3 digit: %03d di Java, {n:03d} di Python, padStart(3, \"0\") di JavaScript/TypeScript.",
"a": "for (let n: number = 1; n <= 5; n++) {\n  console.log(`A-${String(n).padStart(3, \"0\")}`);\n}",
"out": "A-001\nA-002\nA-003\nA-004\nA-005"
}
]
},
{
"k": "c",
"t": "Kapan for, kapan while, kapan do-while",
"nodes": [
"Loops"
],
"viz": "looppick",
"b": [
"Semua loop bisa saling menggantikan, tetapi programmer yang baik memilih loop yang <b>paling jujur menggambarkan niatnya</b>. Pertanyaan kuncinya satu: <b>apakah jumlah putarannya sudah diketahui sebelum loop dimulai?</b>",
"Jika jumlahnya pasti (5 hari, 10 suku, setiap kursi 1 sampai 40), pakai <b>for</b> seperti <code>for (let i = 0; i &lt; n; i++)</code>. Jika yang diketahui hanya <b>kondisi berhentinya</b> (sampai saldo cukup, sampai data habis, sampai tidak ada pertukaran lagi), pakai <b>while</b>. Jika badan loop harus jalan <b>minimal sekali</b> sebelum dicek (menampilkan menu, meminta PIN), pakai <b>do-while</b>: <code>do { ... } while (kondisi);</code>.",
"Untuk membaca setiap isi koleksi tanpa butuh nomor indeks, pakai <b>for-each</b>: <code>for (const k of daftar)</code>. Lebih ringkas dan tidak mungkin salah indeks (error klasik \"off by one\").",
"Pada contoh kode di bawah, keempat jenis loop dipakai sesuai kasusnya masing-masing. Tebak keluarannya dulu, lalu coba latihan memilih loop di visual interaktif."
],
"tb": [
{
"c": "Memilih jenis loop",
"h": [
"Jenis loop",
"Pakai saat",
"Contoh kasus",
"Bentuk di TypeScript"
],
"r": [
[
"for",
"Jumlah putaran sudah diketahui",
"Cetak nomor 1 sampai 40, n suku Fibonacci",
"for (let i = 0; i < n; i++)"
],
[
"while",
"Hanya kondisi berhenti yang diketahui",
"Menabung sampai target, membaca data sampai habis",
"while (kondisi)"
],
[
"do-while",
"Badan loop wajib jalan minimal sekali",
"Menu kasir, meminta PIN",
"do { ... } while (kondisi);"
],
[
"for-each",
"Membaca setiap isi koleksi",
"Menjumlahkan harga di keranjang",
"for (const k of daftar)"
]
]
}
],
"code": "// FOR: jumlah pengulangan sudah diketahui (5 hari)\nlet total: number = 0;\nfor (let hari = 1; hari <= 5; hari++) {\n  total += 10000;\n}\nconsole.log(\"Tabungan 5 hari:\", total);\n\n// WHILE: berhenti saat kondisi tercapai\nlet saldo: number = 0;\nlet minggu: number = 0;\nwhile (saldo < 75000) {\n  saldo += 20000;\n  minggu++;\n}\nconsole.log(`Target tercapai di minggu ke-${minggu}`);\n\n// DO-WHILE: badan loop dijalankan minimal sekali\nconst pilihanUser: number[] = [2, 1, 0];\nlet i = 0;\nlet pilihan: number;\ndo {\n  pilihan = pilihanUser[i++];\n  console.log(\"Menu dipilih:\", pilihan);\n} while (pilihan !== 0);\n\n// FOR...OF: membaca setiap isi array bertipe string[]\nconst kota: string[] = [\"Medan\", \"Bandung\", \"Makassar\"];\nfor (const k of kota) {\n  console.log(\"Kirim ke\", k);\n}",
"out": "Tabungan 5 hari: 50000\nTarget tercapai di minggu ke-4\nMenu dipilih: 2\nMenu dipilih: 1\nMenu dipilih: 0\nKirim ke Medan\nKirim ke Bandung\nKirim ke Makassar",
"pts": [
"Jumlah putaran diketahui → for.",
"Hanya kondisi berhenti yang diketahui → while.",
"Harus jalan minimal sekali → do-while.",
"Hanya membaca isi koleksi → for-each."
],
"q": [
[
"Program meminta pengguna mengetik kata sandi sampai benar. Loop paling cocok?",
[
"for",
"do-while (atau while True + break)",
"for-each"
],
1,
"Pertanyaan harus muncul minimal sekali, dan jumlah percobaannya tidak diketahui."
],
[
"Menghitung rata-rata 30 nilai siswa di sebuah array. Loop paling cocok?",
[
"while",
"for atau for-each",
"do-while"
],
1,
"Jumlah datanya pasti, cukup membaca setiap isi."
],
[
"Mengapa while lebih cocok untuk \"menabung sampai Rp1 juta\"?",
[
"Karena while lebih cepat",
"Karena jumlah minggunya belum diketahui, yang diketahui hanya kondisi berhenti",
"Karena for tidak bisa menjumlah"
],
1,
"Pilihan loop menggambarkan apa yang kita ketahui sebelum mulai."
]
],
"lang": "ts",
"so": [
{
"q": "Hitung mundur peluncuran roket: tampilkan 5, 4, 3, 2, 1 lalu \"Meluncur!\". Loop apa yang paling cocok?",
"h": "Awal dan akhir hitungan sudah pasti (5 sampai 1), jadi pakai for yang nilainya berkurang.",
"a": "for (let detik: number = 5; detik >= 1; detik--) {\n  console.log(detik);\n}\nconsole.log(\"Meluncur!\");",
"out": "5\n4\n3\n2\n1\nMeluncur!"
},
{
"q": "Galon diisi 3 liter setiap menit, mulai dari kosong. Berapa menit sampai isinya minimal 19 liter? Tampilkan menit dan isinya.",
"h": "Jumlah menit belum diketahui, yang diketahui hanya kondisi berhenti (isi ≥ 19). Itu tanda while.",
"a": "let isi: number = 0, menit: number = 0;\nwhile (isi < 19) {\n  isi += 3;\n  menit++;\n}\nconsole.log(`${menit} menit, isi ${isi} liter`);",
"out": "7 menit, isi 21 liter"
}
]
},
{
"k": "c",
"t": "Bilangan Fibonacci: for dan while",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "FibonacciDiBawah100",
"p": [
{
"t": "dec",
"v": "a, b, c, banyak",
"ty": "Integer"
},
{
"t": "asg",
"v": "a",
"e": "0"
},
{
"t": "asg",
"v": "b",
"e": "1"
},
{
"t": "asg",
"v": "banyak",
"e": "0"
},
{
"t": "while",
"c": "a < 100",
"b": [
{
"t": "asg",
"v": "banyak",
"e": "banyak + 1"
},
{
"t": "asg",
"v": "c",
"e": "a + b"
},
{
"t": "asg",
"v": "a",
"e": "b"
},
{
"t": "asg",
"v": "b",
"e": "c"
}
]
},
{
"t": "out",
"e": "\"Banyak suku: \" & banyak"
}
]
},
"b": [
"Deret Fibonacci dimulai dari 0 dan 1, lalu setiap suku adalah jumlah dua suku sebelumnya: 0, 1, 1, 2, 3, 5, 8, 13, ... Polanya muncul di banyak tempat, dari susunan biji bunga matahari sampai soal tes kerja programmer.",
"Kuncinya adalah dua variabel <code>a</code> dan <code>b</code> yang terus <b>digeser</b>: <code>a</code> menjadi <code>b</code>, dan <code>b</code> menjadi <code>a + b</code>. JavaScript/TypeScript bisa memakai <code>[a, b] = [b, a + b]</code>.",
"Perhatikan dua bagian contoh. \"10 suku pertama\" memakai <b>for</b> karena jumlah putarannya pasti 10. \"Semua suku di bawah 100\" memakai <b>while</b> karena kita tidak tahu ada berapa suku sampai benar-benar menghitungnya.",
"Visual di bawah menjalankan bagian while langkah demi langkah sebagai flowchart dan pseudocode. Perhatikan kolom <b>Variabel</b>: nilai yang berubah diberi warna."
],
"tb": [
{
"c": "Jejak variabel 6 putaran pertama",
"h": [
"Putaran",
"a",
"b",
"Suku yang dicatat"
],
"r": [
[
"1",
"0",
"1",
"0"
],
[
"2",
"1",
"1",
"1"
],
[
"3",
"1",
"2",
"1"
],
[
"4",
"2",
"3",
"2"
],
[
"5",
"3",
"5",
"3"
],
[
"6",
"5",
"8",
"5"
]
]
}
],
"code": "function fibonacci(n: number): number[] {\n  const deret: number[] = [];\n  let a = 0, b = 1;\n  for (let i = 0; i < n; i++) {   // FOR: n sudah diketahui\n    deret.push(a);\n    [a, b] = [b, a + b];\n  }\n  return deret;\n}\n\nfunction banyakSukuDiBawah(batas: number): number {\n  let a = 0, b = 1, banyak = 0;\n  while (a < batas) {             // WHILE: berhenti saat melewati batas\n    banyak++;\n    [a, b] = [b, a + b];\n  }\n  return banyak;\n}\n\nconsole.log(\"10 suku pertama:\", fibonacci(10).join(\" \"));\nconsole.log(\"Banyak suku di bawah 100:\", banyakSukuDiBawah(100));",
"out": "10 suku pertama: 0 1 1 2 3 5 8 13 21 34\nBanyak suku di bawah 100: 12",
"pts": [
"Fibonacci butuh dua variabel yang terus digeser.",
"n suku pertama → for; suku di bawah batas → while.",
"Geser nilai dengan urutan yang benar agar nilai lama tidak hilang."
],
"q": [
[
"Suku Fibonacci ke-8 (mulai dari 0) adalah?",
[
"8",
"13",
"21"
],
1,
"0, 1, 1, 2, 3, 5, 8, 13: suku ke-8 adalah 13."
],
[
"Mengapa menghitung \"suku di bawah 1000\" memakai while?",
[
"Karena jumlah sukunya belum diketahui sebelum dihitung",
"Karena for tidak bisa memakai angka besar",
"Karena while selalu lebih cepat"
],
0,
"Batasnya nilai, bukan banyak putaran."
]
],
"lang": "ts",
"so": [
{
"q": "Tampilkan hanya suku Fibonacci ke-20 (suku pertama adalah 0).",
"h": "Kamu tahu persis butuh 19 kali geser pasangan (a, b), jadi pakai for. Tidak perlu menyimpan semua suku.",
"a": "let a: number = 0, b: number = 1;\nfor (let i = 0; i < 19; i++) {\n  [a, b] = [b, a + b];\n}\nconsole.log(\"Suku ke-20:\", a);",
"out": "Suku ke-20: 4181"
},
{
"q": "Cari suku Fibonacci pertama yang lebih dari 1000, dan suku ke berapa itu.",
"h": "Kamu tidak tahu butuh berapa suku, jadi pakai while dengan kondisi a <= 1000.",
"a": "let a: number = 0, b: number = 1, ke: number = 1;\nwhile (a <= 1000) {\n  [a, b] = [b, a + b];\n  ke++;\n}\nconsole.log(`Suku ke-${ke}: ${a}`);",
"out": "Suku ke-18: 1597"
}
]
},
{
"k": "c",
"t": "Bubble sort: loop di dalam loop",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BubbleSort",
"p": [
{
"t": "dec",
"v": "a",
"ty": "Integer",
"arr": "4"
},
{
"t": "asg",
"v": "a",
"e": "[25, 12, 22, 11]"
},
{
"t": "dec",
"v": "j, t, putaran",
"ty": "Integer"
},
{
"t": "dec",
"v": "adaTukar",
"ty": "Boolean"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
},
{
"t": "asg",
"v": "putaran",
"e": "0"
},
{
"t": "while",
"c": "adaTukar",
"b": [
{
"t": "asg",
"v": "adaTukar",
"e": "false"
},
{
"t": "asg",
"v": "putaran",
"e": "putaran + 1"
},
{
"t": "for",
"v": "j",
"a": "0",
"z": "3 - putaran",
"b": [
{
"t": "if",
"c": "a[j] > a[j + 1]",
"y": [
{
"t": "asg",
"v": "t",
"e": "a[j]"
},
{
"t": "asg",
"v": "a[j]",
"e": "a[j + 1]"
},
{
"t": "asg",
"v": "a[j + 1]",
"e": "t"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
}
],
"n": []
}
]
}
]
},
{
"t": "out",
"e": "\"Terurut: \" & a"
}
]
},
"b": [
"Bubble sort mengurutkan data dengan cara paling sederhana: bandingkan dua angka yang <b>bersebelahan</b>, tukar jika urutannya salah, lalu geser ke pasangan berikutnya. Setelah satu putaran, angka terbesar pasti sudah \"menggelembung\" ke ujung kanan.",
"Algoritma ini memakai dua loop. <b>Loop dalam (for)</b> berjalan dari kiri ke kanan, jumlah pasangannya jelas. <b>Loop luar (while)</b> mengulang putaran selama masih ada pertukaran. Variabel penanda <code>adaTukar</code> membuat program berhenti lebih awal jika data sudah terurut.",
"Setiap putaran, satu angka terbesar sudah di tempatnya, jadi loop dalam cukup sampai <code>n - putaran</code>. Detail kecil ini menghemat perbandingan yang tidak perlu.",
"Bubble sort lambat untuk data besar (sekitar n² perbandingan), jadi di dunia kerja kita memakai fungsi sort bawaan bahasa. Tetapi bubble sort adalah latihan terbaik untuk memahami loop bersarang, indeks, dan menukar nilai."
],
"tb": [
{
"c": "Isi array setiap putaran",
"h": [
"Putaran",
"Isi array",
"Yang sudah di tempat"
],
"r": [
[
"Awal",
"64 25 12 22 11",
"-"
],
[
"1",
"25 12 22 11 64",
"64"
],
[
"2",
"12 22 11 25 64",
"25, 64"
],
[
"3",
"12 11 22 25 64",
"22, 25, 64"
],
[
"4",
"11 12 22 25 64",
"semua"
]
]
}
],
"code": "function bubbleSort(data: number[]): number[] {\n  const a = [...data];           // salin agar data asli tidak berubah\n  let adaTukar = true;\n  let putaran = 0;\n  while (adaTukar) {             // WHILE: belum tahu butuh berapa putaran\n    adaTukar = false;\n    putaran++;\n    for (let j = 0; j < a.length - putaran; j++) {   // FOR: batas jelas\n      if (a[j] > a[j + 1]) {\n        [a[j], a[j + 1]] = [a[j + 1], a[j]];\n        adaTukar = true;\n      }\n    }\n    console.log(`Putaran ${putaran}: [${a.join(\", \")}]`);\n  }\n  return a;\n}\n\nconst hasil: number[] = bubbleSort([64, 25, 12, 22, 11]);\nconsole.log(`Terurut: [${hasil.join(\", \")}]`);",
"out": "Putaran 1: [25, 12, 22, 11, 64]\nPutaran 2: [12, 22, 11, 25, 64]\nPutaran 3: [12, 11, 22, 25, 64]\nPutaran 4: [11, 12, 22, 25, 64]\nPutaran 5: [11, 12, 22, 25, 64]\nTerurut: [11, 12, 22, 25, 64]",
"pts": [
"Bandingkan pasangan bersebelahan, tukar jika salah urutan.",
"Loop dalam for (jumlah pasangan jelas), loop luar while (sampai tidak ada pertukaran).",
"Penanda pertukaran membuat sort berhenti lebih awal."
],
"q": [
[
"Setelah putaran pertama bubble sort (urut naik), di mana angka terbesar?",
[
"Di indeks 0",
"Di ujung kanan",
"Belum pasti"
],
1,
"Angka terbesar selalu terbawa sampai ujung kanan pada putaran pertama."
],
[
"Untuk apa variabel penanda pertukaran?",
[
"Menghitung jumlah data",
"Menghentikan loop luar jika satu putaran tidak ada pertukaran",
"Menyimpan angka terbesar"
],
1,
"Jika tidak ada pertukaran, data sudah terurut."
],
[
"Kenapa loop dalam cukup sampai n - putaran?",
[
"Agar tidak error",
"Karena angka di ujung kanan sudah pasti di tempatnya",
"Karena aturan bahasa"
],
1,
"Bagian kanan yang sudah terurut tidak perlu dibandingkan lagi."
]
],
"lang": "ts",
"so": [
{
"q": "Urutkan nama [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"] sesuai abjad dengan bubble sort.",
"h": "Logikanya sama, hanya cara membandingkan teks yang berbeda: Python memakai >, JavaScript/TypeScript memakai localeCompare, Java memakai compareTo.",
"a": "const nama: string[] = [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"];\nlet adaTukar: boolean = true;\nwhile (adaTukar) {\n  adaTukar = false;\n  for (let j = 0; j < nama.length - 1; j++) {\n    if (nama[j].localeCompare(nama[j + 1]) > 0) {\n      [nama[j], nama[j + 1]] = [nama[j + 1], nama[j]];\n      adaTukar = true;\n    }\n  }\n}\nconsole.log(nama.join(\", \"));",
"out": "Agus, Budi, Dewi, Rina"
},
{
"q": "Ubah bubble sort agar mengurutkan dari besar ke kecil, lalu hitung berapa kali terjadi pertukaran untuk [3, 1, 4, 1, 5].",
"h": "Cukup balik tanda perbandingan menjadi <, dan tambah penghitung setiap kali menukar.",
"a": "const data: number[] = [3, 1, 4, 1, 5];\nlet tukar: number = 0;\nfor (let i = 0; i < data.length - 1; i++) {\n  for (let j = 0; j < data.length - 1 - i; j++) {\n    if (data[j] < data[j + 1]) {\n      [data[j], data[j + 1]] = [data[j + 1], data[j]];\n      tukar++;\n    }\n  }\n}\nconsole.log(`[${data.join(\", \")}] pertukaran: ${tukar}`);",
"out": "[5, 4, 3, 1, 1] pertukaran: 6"
}
]
},
{
"k": "c",
"t": "FizzBuzz dan bilangan prima: break dan loop bersarang",
"nodes": [
"Loops",
"Conditionals"
],
"viz": "fc",
"fc": {
"name": "CekPrima",
"in": [
"29"
],
"p": [
{
"t": "dec",
"v": "x, d",
"ty": "Integer"
},
{
"t": "dec",
"v": "prima",
"ty": "Boolean"
},
{
"t": "in",
"v": "x"
},
{
"t": "asg",
"v": "prima",
"e": "x >= 2"
},
{
"t": "asg",
"v": "d",
"e": "2"
},
{
"t": "while",
"c": "d * d <= x and prima",
"b": [
{
"t": "if",
"c": "x mod d = 0",
"y": [
{
"t": "asg",
"v": "prima",
"e": "false"
}
],
"n": []
},
{
"t": "asg",
"v": "d",
"e": "d + 1"
}
]
},
{
"t": "if",
"c": "prima",
"y": [
{
"t": "out",
"e": "x & \" adalah prima\""
}
],
"n": [
{
"t": "out",
"e": "x & \" bukan prima\""
}
]
}
]
},
"b": [
"<b>FizzBuzz</b> adalah soal wawancara klasik: untuk angka 1 sampai 15, tampilkan \"Fizz\" jika habis dibagi 3, \"Buzz\" jika habis dibagi 5, \"FizzBuzz\" jika habis dibagi keduanya, dan angkanya sendiri jika tidak. Rentangnya jelas, jadi pakai <b>for</b>. Jebakannya: cek kelipatan 15 lebih dulu, karena jika cek 3 duluan, angka 15 sudah keburu menjadi \"Fizz\".",
"<b>Bilangan prima</b> hanya habis dibagi 1 dan dirinya sendiri. Untuk setiap angka (loop luar), kita coba pembagi dari 2 (loop dalam). Begitu ketemu satu pembagi, angka itu pasti bukan prima, jadi <b>break</b> menghentikan loop dalam tanpa membuang waktu.",
"Pembagi cukup dicoba sampai akar angkanya (<code>d * d &lt;= x</code>). Jika 36 = 4 × 9, salah satu faktornya pasti ≤ 6. Ini mengubah 1.000 percobaan menjadi sekitar 31. Variabel penanda <code>isPrima</code> mencatat apakah loop dalam pernah berhenti karena break.",
"Visual di bawah memeriksa satu angka dengan while dan penanda, karena Flowgorithm tidak punya break. Ganti inputnya, misalnya 91 atau 97, lalu jalankan."
],
"tb": [
{
"c": "break dan continue",
"h": [
"Perintah",
"Efek",
"Kapan dipakai"
],
"r": [
[
"break",
"Keluar dari loop terdekat",
"Jawaban sudah ditemukan, sisa putaran tidak perlu"
],
[
"continue",
"Lompat ke putaran berikutnya",
"Lewati data yang tidak relevan"
],
[
"penanda (flag)",
"Variabel boolean yang dicek setelah loop",
"Bahasa atau alat tanpa break, misalnya Flowgorithm"
]
]
}
],
"code": "function fizzBuzz(n: number): string[] {\n  const hasil: string[] = [];\n  for (let i = 1; i <= n; i++) {            // FOR: rentang jelas\n    if (i % 15 === 0) hasil.push(\"FizzBuzz\");\n    else if (i % 3 === 0) hasil.push(\"Fizz\");\n    else if (i % 5 === 0) hasil.push(\"Buzz\");\n    else hasil.push(String(i));\n  }\n  return hasil;\n}\n\nfunction isPrima(x: number): boolean {\n  if (x < 2) return false;\n  for (let d = 2; d * d <= x; d++) {\n    if (x % d === 0) return false;          // keluar lebih awal\n  }\n  return true;\n}\n\nconsole.log(fizzBuzz(15).join(\" \"));\nconst prima: number[] = [];\nfor (let x = 2; x <= 30; x++) if (isPrima(x)) prima.push(x);\nconsole.log(\"Prima:\", prima.join(\" \"));",
"out": "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\nPrima: 2 3 5 7 11 13 17 19 23 29",
"pts": [
"Urutan if penting: kondisi paling khusus dicek lebih dulu.",
"break menghentikan loop terdekat saat jawaban sudah pasti.",
"Pembagi prima cukup dicek sampai akar angkanya."
],
"q": [
[
"Jika FizzBuzz mengecek \"habis dibagi 3\" lebih dulu, apa yang tampil untuk 15?",
[
"FizzBuzz",
"Fizz",
"Buzz"
],
1,
"Kondisi pertama yang benar langsung dipakai."
],
[
"Pada loop bersarang, break menghentikan loop yang mana?",
[
"Semua loop",
"Loop terdekat yang membungkusnya",
"Loop terluar"
],
1,
"break hanya keluar dari satu tingkat loop."
],
[
"Untuk mengecek apakah 97 prima, pembagi paling besar yang perlu dicoba adalah?",
[
"96",
"48",
"9"
],
2,
"9 × 9 = 81 ≤ 97, sedangkan 10 × 10 = 100 > 97."
]
],
"lang": "ts",
"so": [
{
"q": "Tampilkan tabel perkalian 1 sampai 5 dalam bentuk kotak (5 baris, 5 kolom).",
"h": "For luar untuk baris, for dalam untuk kolom. Keduanya punya batas yang jelas.",
"a": "for (let i = 1; i <= 5; i++) {\n  let baris: string = \"\";\n  for (let j = 1; j <= 5; j++) {\n    baris += String(i * j).padStart(4);\n  }\n  console.log(baris);\n}",
"out": "   1   2   3   4   5\n   2   4   6   8  10\n   3   6   9  12  15\n   4   8  12  16  20\n   5  10  15  20  25"
},
{
"q": "Cari bilangan prima pertama yang lebih besar dari 100.",
"h": "Kita tidak tahu harus mencoba berapa angka, jadi loop luar memakai while. Pengecekan pembagi tetap memakai for dengan break.",
"a": "let x: number = 101;\nwhile (true) {\n  let prima: boolean = true;\n  for (let d = 2; d * d <= x; d++) {\n    if (x % d === 0) { prima = false; break; }\n  }\n  if (prima) break;\n  x++;\n}\nconsole.log(\"Prima pertama > 100:\", x);",
"out": "Prima pertama > 100: 101"
}
]
},
{
"k": "c",
"t": "Faktorial, jumlah digit, dan palindrom",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "JumlahDigit",
"in": [
"90417"
],
"p": [
{
"t": "dec",
"v": "angka, jumlah",
"ty": "Integer"
},
{
"t": "in",
"v": "angka"
},
{
"t": "asg",
"v": "jumlah",
"e": "0"
},
{
"t": "while",
"c": "angka > 0",
"b": [
{
"t": "asg",
"v": "jumlah",
"e": "jumlah + angka mod 10"
},
{
"t": "asg",
"v": "angka",
"e": "Int(angka / 10)"
}
]
},
{
"t": "out",
"e": "\"Jumlah digit: \" & jumlah"
}
]
},
"b": [
"Tiga soal ini melatih kapan memakai for dan kapan while. <b>Faktorial</b> 5! = 1 × 2 × 3 × 4 × 5: banyak perkaliannya pasti, jadi <b>for</b>.",
"<b>Jumlah digit</b> 90417 = 9 + 0 + 4 + 1 + 7 = 21. Kita tidak tahu angkanya punya berapa digit, jadi pakai <b>while</b>: ambil digit terakhir dengan <code>% 10</code>, lalu buang dengan pembagian bulat <code>Math.floor(x / 10)</code>. Berhenti saat angkanya habis (0).",
"<b>Palindrom</b> adalah kata yang sama jika dibaca dari depan dan belakang, seperti \"katak\". Pakai <b>dua penunjuk</b>: satu dari kiri, satu dari kanan, bergerak ke tengah selama <code>kiri &lt; kanan</code>. Begitu ada huruf yang berbeda, langsung break.",
"Visual di bawah menjalankan jumlah digit. Coba ganti inputnya dengan angka lain dan hitung dulu di kepala sebelum menekan Berikutnya."
],
"tb": [
{
"c": "Jejak jumlah digit 90417",
"h": [
"Putaran",
"angka % 10",
"jumlah",
"angka setelah dibagi 10"
],
"r": [
[
"1",
"7",
"7",
"9041"
],
[
"2",
"1",
"8",
"904"
],
[
"3",
"4",
"12",
"90"
],
[
"4",
"0",
"12",
"9"
],
[
"5",
"9",
"21",
"0"
]
]
}
],
"code": "function faktorial(n: number): number {\n  let hasil = 1;\n  for (let i = 2; i <= n; i++) hasil *= i;   // FOR: n kali\n  return hasil;\n}\n\nfunction jumlahDigit(angka: number): number {\n  let sisa = angka, jumlah = 0;\n  while (sisa > 0) {                          // WHILE: digit belum diketahui\n    jumlah += sisa % 10;\n    sisa = Math.floor(sisa / 10);\n  }\n  return jumlah;\n}\n\nfunction isPalindrom(kata: string): boolean {\n  let kiri = 0, kanan = kata.length - 1;\n  while (kiri < kanan) {                      // WHILE: dua penunjuk\n    if (kata[kiri] !== kata[kanan]) return false;\n    kiri++;\n    kanan--;\n  }\n  return true;\n}\n\nconsole.log(`5! = ${faktorial(5)}`);\nconsole.log(`Jumlah digit 90417 = ${jumlahDigit(90417)}`);\nconsole.log(`katak palindrom? ${isPalindrom(\"katak\")}`);",
"out": "5! = 120\nJumlah digit 90417 = 21\nkatak palindrom? true",
"pts": [
"% 10 mengambil digit terakhir, bagi 10 (bulat) membuangnya.",
"Banyak digit tidak diketahui → while.",
"Dua penunjuk bergerak ke tengah untuk memeriksa palindrom."
],
"q": [
[
"Berapa hasil 4827 % 10?",
[
"4",
"7",
"482"
],
1,
"Sisa bagi 10 adalah digit terakhir."
],
[
"Loop paling cocok untuk menghitung 10! (faktorial 10)?",
[
"for",
"while",
"do-while"
],
0,
"Banyak perkaliannya pasti."
],
[
"Pada pemeriksaan palindrom \"level\", berapa kali perbandingan huruf terjadi?",
[
"5",
"2",
"1"
],
1,
"Pasangan (l, l) dan (e, e); huruf tengah v tidak perlu dibandingkan."
]
],
"lang": "ts",
"so": [
{
"q": "Balik angka 12345 menjadi 54321 tanpa mengubahnya menjadi teks.",
"h": "Ambil digit terakhir dengan % 10, tempel ke hasil dengan hasil * 10 + digit, buang digit terakhir dengan pembagian bulat. Ulangi selama angka > 0.",
"a": "let angka: number = 12345, balik: number = 0;\nwhile (angka > 0) {\n  balik = balik * 10 + (angka % 10);\n  angka = Math.floor(angka / 10);\n}\nconsole.log(\"Dibalik:\", balik);",
"out": "Dibalik: 54321"
},
{
"q": "Hitung 2 pangkat 10 dengan loop, tanpa operator pangkat.",
"h": "Perkalian diulang tepat 10 kali, jadi for.",
"a": "let hasil: number = 1;\nfor (let i = 0; i < 10; i++) {\n  hasil *= 2;\n}\nconsole.log(\"2^10 =\", hasil);",
"out": "2^10 = 1024"
}
]
},
{
"k": "c",
"t": "Binary search: membagi dua sampai ketemu",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BinarySearch",
"in": [
"20000"
],
"p": [
{
"t": "dec",
"v": "harga",
"ty": "Integer",
"arr": "7"
},
{
"t": "asg",
"v": "harga",
"e": "[5000, 8000, 12000, 15000, 20000, 27000, 35000]"
},
{
"t": "dec",
"v": "cari, kiri, kanan, tengah, posisi",
"ty": "Integer"
},
{
"t": "in",
"v": "cari"
},
{
"t": "asg",
"v": "kiri",
"e": "0"
},
{
"t": "asg",
"v": "kanan",
"e": "6"
},
{
"t": "asg",
"v": "posisi",
"e": "-1"
},
{
"t": "while",
"c": "kiri <= kanan and posisi = -1",
"b": [
{
"t": "asg",
"v": "tengah",
"e": "Int((kiri + kanan) / 2)"
},
{
"t": "if",
"c": "harga[tengah] = cari",
"y": [
{
"t": "asg",
"v": "posisi",
"e": "tengah"
}
],
"n": [
{
"t": "if",
"c": "harga[tengah] < cari",
"y": [
{
"t": "asg",
"v": "kiri",
"e": "tengah + 1"
}
],
"n": [
{
"t": "asg",
"v": "kanan",
"e": "tengah - 1"
}
]
}
]
}
]
},
{
"t": "out",
"e": "\"Posisi: \" & posisi"
}
]
},
"b": [
"Mencari harga di daftar 1.000 barang satu per satu (linear search) bisa butuh 1.000 langkah. Jika daftarnya <b>sudah terurut</b>, kita bisa jauh lebih cepat: lihat bagian tengah, lalu buang separuh daftar yang pasti tidak berisi jawabannya.",
"Simpan dua batas, <code>kiri</code> dan <code>kanan</code>. Selama <code>kiri &lt;= kanan</code>, hitung <code>tengah</code>. Jika nilai tengah terlalu kecil, geser kiri ke tengah + 1. Jika terlalu besar, geser kanan ke tengah - 1. Banyak langkahnya tidak diketahui sebelumnya, jadi loopnya <b>while</b>.",
"Setiap langkah membuang separuh data, jadi 1.000 data cukup dicari dalam paling banyak 10 langkah, dan 1 juta data dalam 20 langkah. Inilah alasan database dan kamus memakai data terurut.",
"Visual di bawah mencari harga di 7 data. Coba input 5000, 35000, atau 9000 (tidak ada di daftar) dan perhatikan bagaimana kiri dan kanan bergerak."
],
"tb": [
{
"c": "Linear search vs binary search",
"h": [
"Aspek",
"Linear search",
"Binary search"
],
"r": [
[
"Syarat data",
"Bebas",
"Harus terurut"
],
[
"Langkah terburuk (1.000 data)",
"1.000",
"10"
],
[
"Jenis loop",
"for (setiap data)",
"while (sampai ketemu atau habis)"
],
[
"Kapan dipakai",
"Data sedikit atau tidak terurut",
"Data besar dan terurut"
]
]
}
],
"code": "function binarySearch(data: number[], cari: number): number {\n  let kiri = 0, kanan = data.length - 1, langkah = 0;\n  while (kiri <= kanan) {                     // WHILE: berhenti saat ketemu/habis\n    langkah++;\n    const tengah = Math.floor((kiri + kanan) / 2);\n    console.log(`Langkah ${langkah}: cek indeks ${tengah} (${data[tengah]})`);\n    if (data[tengah] === cari) return tengah;\n    if (data[tengah] < cari) kiri = tengah + 1;\n    else kanan = tengah - 1;\n  }\n  return -1;\n}\n\nconst harga: number[] = [5000, 8000, 12000, 15000, 20000, 27000, 35000];\nconsole.log(`Ketemu di indeks ${binarySearch(harga, 20000)}`);",
"out": "Langkah 1: cek indeks 3 (15000)\nLangkah 2: cek indeks 5 (27000)\nLangkah 3: cek indeks 4 (20000)\nKetemu di indeks 4",
"pts": [
"Binary search hanya untuk data terurut.",
"Setiap langkah membuang separuh ruang pencarian.",
"Berhenti saat ketemu atau kiri > kanan."
],
"q": [
[
"Apa syarat utama binary search?",
[
"Data berupa angka",
"Data sudah terurut",
"Data kurang dari 100"
],
1,
"Tanpa urutan, kita tidak tahu separuh mana yang harus dibuang."
],
[
"Jika harga[tengah] lebih kecil dari yang dicari, apa yang dilakukan?",
[
"kanan = tengah - 1",
"kiri = tengah + 1",
"Berhenti"
],
1,
"Jawabannya pasti di sebelah kanan tengah."
],
[
"Kira-kira berapa langkah maksimum untuk 1 juta data terurut?",
[
"20",
"1.000",
"500.000"
],
0,
"2 pangkat 20 ≈ 1 juta."
]
],
"lang": "ts",
"so": [
{
"q": "Komputer menebak angka rahasia 73 di antara 1 sampai 100 dengan cara binary search. Tampilkan setiap tebakan.",
"h": "Sama seperti mencari di array terurut, hanya saja \"array\"-nya adalah rentang angka 1 sampai 100.",
"a": "const rahasia: number = 73;\nlet bawah: number = 1, atas: number = 100;\nwhile (true) {\n  const tebak: number = Math.floor((bawah + atas) / 2);\n  console.log(\"Tebak\", tebak);\n  if (tebak === rahasia) break;\n  if (tebak < rahasia) bawah = tebak + 1;\n  else atas = tebak - 1;\n}",
"out": "Tebak 50\nTebak 75\nTebak 62\nTebak 68\nTebak 71\nTebak 73"
},
{
"q": "Berapa langkah paling banyak yang dibutuhkan binary search untuk 1.000 data? Hitung dengan membagi dua terus sampai habis.",
"h": "Selama masih ada data (n > 0), bagi dua dan tambah 1 langkah. Ini while karena jumlah langkah adalah hal yang dicari.",
"a": "let n: number = 1000, langkah: number = 0;\nwhile (n > 0) {\n  n = Math.floor(n / 2);\n  langkah++;\n}\nconsole.log(\"Maksimal\", langkah, \"langkah\");",
"out": "Maksimal 10 langkah"
}
]
}
]
},
"fe0": {
"t": "Format keluaran dan latihan algoritma",
"lvl": "Menengah",
"d": "Format specifier, Fibonacci, bubble sort, FizzBuzz, bilangan prima, palindrom, dan binary search di JavaScript, dengan alasan memilih for, while, do-while, atau for-each.",
"nodes": [
"Loops",
"Arrays"
],
"lessons": [
{
"k": "c",
"t": "Format specifier: merapikan keluaran",
"nodes": [
"Basic Syntax"
],
"lang": "js",
"b": [
"<b>Format specifier</b> adalah kode kecil yang mengatur <b>bagaimana sebuah nilai ditampilkan</b>: berapa angka di belakang koma, selebar apa kolomnya, rata kiri atau kanan, diberi nol di depan, atau diberi pemisah ribuan. Nilainya tidak berubah, hanya tampilannya. Hampir semua program nyata membutuhkannya: struk belanja, laporan nilai, nomor invoice, dan log server.",
"Polanya mirip di semua bahasa: <b>[perataan][lebar][.presisi][tipe]</b>. Contoh <code>%-10s</code> berarti teks rata kiri selebar 10, <code>%8.2f</code> berarti desimal 2 angka dalam kolom selebar 8, dan <code>%05d</code> berarti bilangan bulat selebar 5 yang diisi nol di depan.",
"JavaScript tidak punya printf. Gantinya: <b>template literal</b> <code>`${nilai}`</code> untuk menyisipkan nilai, <code>toFixed(2)</code> untuk presisi, <code>padStart</code>/<code>padEnd</code> untuk lebar dan perataan, dan <code>toString(16)</code> untuk basis lain. <code>console.log</code> mengenal <code>%s %d %f %o</code>, tetapi hanya untuk mencetak ke konsol.",
"Untuk angka dan uang yang tampil ke pengguna, industri memakai <code>Intl.NumberFormat</code> atau <code>toLocaleString(\"id-ID\")</code>, sehingga 7500000 tampil sebagai 7.500.000 atau Rp 7.500.000 sesuai aturan Indonesia. Hindari menyusun format uang sendiri dengan replace atau regex.",
"Contoh terakhir di kode adalah <b>struk belanja</b>: format di dalam loop membuat setiap baris punya lebar kolom yang sama, sehingga angka tersusun rapi ke kanan. Ini pola yang akan sering kamu pakai di soal-soal berikutnya."
],
"tb": [
{
"c": "Format specifier di berbagai bahasa",
"h": [
"Tujuan",
"Java / C (printf)",
"Python (f-string)",
"JavaScript / TypeScript"
],
"r": [
[
"Teks",
"%s",
"{x}",
"${x}"
],
[
"Bilangan bulat",
"%d",
"{x:d}",
"${x}"
],
[
"Desimal 2 angka",
"%.2f",
"{x:.2f}",
"x.toFixed(2)"
],
[
"Lebar 8, rata kanan",
"%8s",
"{x:>8}",
"String(x).padStart(8)"
],
[
"Lebar 8, rata kiri",
"%-8s",
"{x:<8}",
"String(x).padEnd(8)"
],
[
"Isi nol di depan",
"%05d",
"{x:05d}",
"String(x).padStart(5, \"0\")"
],
[
"Pemisah ribuan",
"%,d",
"{x:,}",
"x.toLocaleString(\"id-ID\")"
],
[
"Persen",
"%.0f%%",
"{x:.0%}",
"(x * 100).toFixed(0) + \"%\""
],
[
"Heksadesimal",
"%x",
"{x:x}",
"x.toString(16)"
],
[
"Notasi ilmiah",
"%.3e",
"{x:.3e}",
"x.toExponential(3)"
],
[
"Baris baru",
"%n atau \\n",
"\\n",
"\\n"
]
]
},
{
"c": "Yang paling sering dipakai di industri",
"h": [
"Kebutuhan",
"Pilihan umum",
"Alasan"
],
"r": [
[
"Menyusun teks di kode baru",
"f-string (Python), template literal (JS/TS), String.format atau formatted() (Java)",
"Paling mudah dibaca dan dirawat"
],
[
"Angka dan uang ke pengguna",
"Format berbasis lokal: Intl.NumberFormat, Locale id-ID, Babel",
"Titik, koma, dan simbol Rp mengikuti aturan negara"
],
[
"Laporan dan struk berkolom",
"Lebar + perataan: %-12s, %10.2f, padEnd/padStart",
"Kolom tetap lurus berapa pun panjang datanya"
],
[
"Kode dokumen dan antrean",
"Isi nol: %04d, {n:04d}",
"INV-0007 lebih mudah diurutkan dan dicari"
],
[
"Logging",
"Placeholder %s atau {}: logger.info(\"user %s\", id)",
"Teks hanya disusun jika log benar-benar dicetak"
],
[
"Tanggal",
"ISO 8601 (2026-11-02) atau pola yyyy-MM-dd",
"Standar internasional dan mudah diurutkan"
]
]
}
],
"code": "const nama = \"Rina\";\nconst umur = 20;\nconst ipk = 3.4567;\n// template literal: ${ekspresi}, angka desimal dengan toFixed\nconsole.log(`Nama: ${nama}, umur ${umur}, IPK ${ipk.toFixed(2)}`);\n\n// lebar dan perataan: padStart (rata kanan), padEnd (rata kiri)\nconsole.log(`[${nama.padStart(8)}] [${nama.padEnd(8)}] [${String(umur).padStart(5, \"0\")}]`);\n\n// basis lain, notasi ilmiah, persen\nconsole.log(`hex ${(255).toString(16)} | biner ${(5).toString(2)} | ${(123456.789).toExponential(3)} | ${(0.15 * 100).toFixed(0)}%`);\n\n// format lokal Indonesia: ribuan dengan titik, mata uang Rupiah\nconst rupiah = new Intl.NumberFormat(\"id-ID\", { style: \"currency\", currency: \"IDR\", maximumFractionDigits: 0 });\nconsole.log((7500000).toLocaleString(\"id-ID\"), \"|\", rupiah.format(7500000));\n\n// console.log juga mengenal %s %d %f %o (gaya printf)\nconsole.log(\"Nama: %s, umur %d\", nama, umur);\n\n// struk belanja\nconst barang = [\"Kopi susu\", \"Roti bakar\", \"Air mineral\"];\nconst harga = [18000, 22500, 5000];\nconsole.log(`${\"Barang\".padEnd(12)} ${\"Harga\".padStart(10)}`);\nbarang.forEach((b, i) => console.log(`${b.padEnd(12)} ${harga[i].toLocaleString(\"id-ID\").padStart(10)}`));\nconst total = harga.reduce((a, b) => a + b, 0);\nconsole.log(`${\"TOTAL\".padEnd(12)} ${total.toLocaleString(\"id-ID\").padStart(10)}`);",
"out": "Nama: Rina, umur 20, IPK 3.46\n[    Rina] [Rina    ] [00020]\nhex ff | biner 101 | 1.235e+5 | 15%\n7.500.000 | Rp 7.500.000\nNama: Rina, umur 20\nBarang            Harga\nKopi susu        18.000\nRoti bakar       22.500\nAir mineral       5.000\nTOTAL            45.500",
"pts": [
"Pola umum: [perataan][lebar][.presisi][tipe].",
"Lebar + perataan membuat kolom laporan lurus.",
"Untuk angka ke pengguna, pakai format lokal (id-ID).",
"Kode baru: f-string, template literal, atau String.format."
],
"q": [
[
"Apa arti format %-10s?",
[
"Teks rata kanan selebar 10",
"Teks rata kiri selebar 10",
"10 karakter pertama saja"
],
1,
"Tanda minus berarti rata kiri, angka 10 adalah lebar kolom minimum."
],
[
"Format apa yang menampilkan 7 sebagai 007?",
[
"%.3d atau {x:.3}",
"%03d atau {x:03d}",
"%3d atau {x:3}"
],
1,
"Angka 0 di depan lebar berarti isi nol. Tanpa 0, sisa tempat diisi spasi."
],
[
"3.14159 diformat dengan dua angka desimal hasilnya?",
[
"3.14",
"3.15",
"3.1"
],
0,
"Dibulatkan ke 2 angka di belakang koma: 3.14159 → 3.14."
],
[
"Untuk menampilkan harga ke pengguna Indonesia, cara yang dianjurkan adalah?",
[
"Menyusun titik ribuan sendiri dengan replace",
"Memakai format berbasis lokal id-ID",
"Menampilkan angka mentah"
],
1,
"Format lokal menangani pemisah ribuan, desimal, dan simbol mata uang dengan benar."
]
],
"so": [
{
"q": "Tampilkan daftar 3 mahasiswa dengan kolom rapi: nomor (lebar 3, rata kanan), nama (lebar 10, rata kiri), dan IPK (2 angka desimal). Data: Ani 3.5, Budi 3.257, Citra 3.9.",
"h": "Gabungkan lebar dan perataan dengan presisi. Untuk IPK: lebar 5 dan 2 desimal, misalnya %5.2f atau {ipk:5.2f}.",
"a": "const data = [[\"Ani\", 3.5], [\"Budi\", 3.257], [\"Citra\", 3.9]];\ndata.forEach(([nama, ipk], i) => {\n  console.log(`${String(i + 1).padStart(3)} ${nama.padEnd(10)} ${ipk.toFixed(2).padStart(5)}`);\n});",
"out": "  1 Ani         3.50\n  2 Budi        3.26\n  3 Citra       3.90"
},
{
"q": "Buat nomor antrean 5 pelanggan dengan format A-001 sampai A-005.",
"h": "Isi angka dengan nol di depan sampai 3 digit: %03d di Java, {n:03d} di Python, padStart(3, \"0\") di JavaScript/TypeScript.",
"a": "for (let n = 1; n <= 5; n++) {\n  console.log(`A-${String(n).padStart(3, \"0\")}`);\n}",
"out": "A-001\nA-002\nA-003\nA-004\nA-005"
}
]
},
{
"k": "c",
"t": "Kapan for, kapan while, kapan do-while",
"nodes": [
"Loops"
],
"viz": "looppick",
"b": [
"Semua loop bisa saling menggantikan, tetapi programmer yang baik memilih loop yang <b>paling jujur menggambarkan niatnya</b>. Pertanyaan kuncinya satu: <b>apakah jumlah putarannya sudah diketahui sebelum loop dimulai?</b>",
"Jika jumlahnya pasti (5 hari, 10 suku, setiap kursi 1 sampai 40), pakai <b>for</b> seperti <code>for (let i = 0; i &lt; n; i++)</code>. Jika yang diketahui hanya <b>kondisi berhentinya</b> (sampai saldo cukup, sampai data habis, sampai tidak ada pertukaran lagi), pakai <b>while</b>. Jika badan loop harus jalan <b>minimal sekali</b> sebelum dicek (menampilkan menu, meminta PIN), pakai <b>do-while</b>: <code>do { ... } while (kondisi);</code>.",
"Untuk membaca setiap isi koleksi tanpa butuh nomor indeks, pakai <b>for-each</b>: <code>for (const k of daftar)</code>. Lebih ringkas dan tidak mungkin salah indeks (error klasik \"off by one\").",
"Pada contoh kode di bawah, keempat jenis loop dipakai sesuai kasusnya masing-masing. Tebak keluarannya dulu, lalu coba latihan memilih loop di visual interaktif."
],
"tb": [
{
"c": "Memilih jenis loop",
"h": [
"Jenis loop",
"Pakai saat",
"Contoh kasus",
"Bentuk di JavaScript"
],
"r": [
[
"for",
"Jumlah putaran sudah diketahui",
"Cetak nomor 1 sampai 40, n suku Fibonacci",
"for (let i = 0; i < n; i++)"
],
[
"while",
"Hanya kondisi berhenti yang diketahui",
"Menabung sampai target, membaca data sampai habis",
"while (kondisi)"
],
[
"do-while",
"Badan loop wajib jalan minimal sekali",
"Menu kasir, meminta PIN",
"do { ... } while (kondisi);"
],
[
"for-each",
"Membaca setiap isi koleksi",
"Menjumlahkan harga di keranjang",
"for (const k of daftar)"
]
]
}
],
"code": "// FOR: jumlah pengulangan sudah diketahui (5 hari)\nlet total = 0;\nfor (let hari = 1; hari <= 5; hari++) {\n  total += 10000;\n}\nconsole.log(\"Tabungan 5 hari:\", total);\n\n// WHILE: berhenti saat kondisi tercapai, jumlah putaran belum diketahui\nlet saldo = 0, minggu = 0;\nwhile (saldo < 75000) {\n  saldo += 20000;\n  minggu++;\n}\nconsole.log(`Target tercapai di minggu ke-${minggu}`);\n\n// DO-WHILE: badan loop dijalankan minimal sekali\nconst pilihanUser = [2, 1, 0];\nlet i = 0, pilihan;\ndo {\n  pilihan = pilihanUser[i++];\n  console.log(\"Menu dipilih:\", pilihan);\n} while (pilihan !== 0);\n\n// FOR...OF: membaca setiap isi array\nfor (const k of [\"Medan\", \"Bandung\", \"Makassar\"]) {\n  console.log(\"Kirim ke\", k);\n}",
"out": "Tabungan 5 hari: 50000\nTarget tercapai di minggu ke-4\nMenu dipilih: 2\nMenu dipilih: 1\nMenu dipilih: 0\nKirim ke Medan\nKirim ke Bandung\nKirim ke Makassar",
"pts": [
"Jumlah putaran diketahui → for.",
"Hanya kondisi berhenti yang diketahui → while.",
"Harus jalan minimal sekali → do-while.",
"Hanya membaca isi koleksi → for-each."
],
"q": [
[
"Program meminta pengguna mengetik kata sandi sampai benar. Loop paling cocok?",
[
"for",
"do-while (atau while True + break)",
"for-each"
],
1,
"Pertanyaan harus muncul minimal sekali, dan jumlah percobaannya tidak diketahui."
],
[
"Menghitung rata-rata 30 nilai siswa di sebuah array. Loop paling cocok?",
[
"while",
"for atau for-each",
"do-while"
],
1,
"Jumlah datanya pasti, cukup membaca setiap isi."
],
[
"Mengapa while lebih cocok untuk \"menabung sampai Rp1 juta\"?",
[
"Karena while lebih cepat",
"Karena jumlah minggunya belum diketahui, yang diketahui hanya kondisi berhenti",
"Karena for tidak bisa menjumlah"
],
1,
"Pilihan loop menggambarkan apa yang kita ketahui sebelum mulai."
]
],
"lang": "js",
"so": [
{
"q": "Hitung mundur peluncuran roket: tampilkan 5, 4, 3, 2, 1 lalu \"Meluncur!\". Loop apa yang paling cocok?",
"h": "Awal dan akhir hitungan sudah pasti (5 sampai 1), jadi pakai for yang nilainya berkurang.",
"a": "for (let detik = 5; detik >= 1; detik--) {\n  console.log(detik);\n}\nconsole.log(\"Meluncur!\");",
"out": "5\n4\n3\n2\n1\nMeluncur!"
},
{
"q": "Galon diisi 3 liter setiap menit, mulai dari kosong. Berapa menit sampai isinya minimal 19 liter? Tampilkan menit dan isinya.",
"h": "Jumlah menit belum diketahui, yang diketahui hanya kondisi berhenti (isi ≥ 19). Itu tanda while.",
"a": "let isi = 0, menit = 0;\nwhile (isi < 19) {\n  isi += 3;\n  menit++;\n}\nconsole.log(`${menit} menit, isi ${isi} liter`);",
"out": "7 menit, isi 21 liter"
}
]
},
{
"k": "c",
"t": "Bilangan Fibonacci: for dan while",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "FibonacciDiBawah100",
"p": [
{
"t": "dec",
"v": "a, b, c, banyak",
"ty": "Integer"
},
{
"t": "asg",
"v": "a",
"e": "0"
},
{
"t": "asg",
"v": "b",
"e": "1"
},
{
"t": "asg",
"v": "banyak",
"e": "0"
},
{
"t": "while",
"c": "a < 100",
"b": [
{
"t": "asg",
"v": "banyak",
"e": "banyak + 1"
},
{
"t": "asg",
"v": "c",
"e": "a + b"
},
{
"t": "asg",
"v": "a",
"e": "b"
},
{
"t": "asg",
"v": "b",
"e": "c"
}
]
},
{
"t": "out",
"e": "\"Banyak suku: \" & banyak"
}
]
},
"b": [
"Deret Fibonacci dimulai dari 0 dan 1, lalu setiap suku adalah jumlah dua suku sebelumnya: 0, 1, 1, 2, 3, 5, 8, 13, ... Polanya muncul di banyak tempat, dari susunan biji bunga matahari sampai soal tes kerja programmer.",
"Kuncinya adalah dua variabel <code>a</code> dan <code>b</code> yang terus <b>digeser</b>: <code>a</code> menjadi <code>b</code>, dan <code>b</code> menjadi <code>a + b</code>. JavaScript/TypeScript bisa memakai <code>[a, b] = [b, a + b]</code>.",
"Perhatikan dua bagian contoh. \"10 suku pertama\" memakai <b>for</b> karena jumlah putarannya pasti 10. \"Semua suku di bawah 100\" memakai <b>while</b> karena kita tidak tahu ada berapa suku sampai benar-benar menghitungnya.",
"Visual di bawah menjalankan bagian while langkah demi langkah sebagai flowchart dan pseudocode. Perhatikan kolom <b>Variabel</b>: nilai yang berubah diberi warna."
],
"tb": [
{
"c": "Jejak variabel 6 putaran pertama",
"h": [
"Putaran",
"a",
"b",
"Suku yang dicatat"
],
"r": [
[
"1",
"0",
"1",
"0"
],
[
"2",
"1",
"1",
"1"
],
[
"3",
"1",
"2",
"1"
],
[
"4",
"2",
"3",
"2"
],
[
"5",
"3",
"5",
"3"
],
[
"6",
"5",
"8",
"5"
]
]
}
],
"code": "// FOR: n suku pertama (jumlah putaran diketahui)\nconst n = 10;\nlet a = 0, b = 1;\nconst deret = [];\nfor (let i = 0; i < n; i++) {\n  deret.push(a);\n  [a, b] = [b, a + b];\n}\nconsole.log(\"10 suku pertama:\", deret.join(\" \"));\n\n// WHILE: semua suku di bawah 100 (jumlah putaran belum diketahui)\na = 0; b = 1;\nlet banyak = 0;\nwhile (a < 100) {\n  banyak++;\n  [a, b] = [b, a + b];\n}\nconsole.log(\"Banyak suku di bawah 100:\", banyak);",
"out": "10 suku pertama: 0 1 1 2 3 5 8 13 21 34\nBanyak suku di bawah 100: 12",
"pts": [
"Fibonacci butuh dua variabel yang terus digeser.",
"n suku pertama → for; suku di bawah batas → while.",
"Geser nilai dengan urutan yang benar agar nilai lama tidak hilang."
],
"q": [
[
"Suku Fibonacci ke-8 (mulai dari 0) adalah?",
[
"8",
"13",
"21"
],
1,
"0, 1, 1, 2, 3, 5, 8, 13: suku ke-8 adalah 13."
],
[
"Mengapa menghitung \"suku di bawah 1000\" memakai while?",
[
"Karena jumlah sukunya belum diketahui sebelum dihitung",
"Karena for tidak bisa memakai angka besar",
"Karena while selalu lebih cepat"
],
0,
"Batasnya nilai, bukan banyak putaran."
]
],
"lang": "js",
"so": [
{
"q": "Tampilkan hanya suku Fibonacci ke-20 (suku pertama adalah 0).",
"h": "Kamu tahu persis butuh 19 kali geser pasangan (a, b), jadi pakai for. Tidak perlu menyimpan semua suku.",
"a": "let a = 0, b = 1;\nfor (let i = 0; i < 19; i++) {\n  [a, b] = [b, a + b];\n}\nconsole.log(\"Suku ke-20:\", a);",
"out": "Suku ke-20: 4181"
},
{
"q": "Cari suku Fibonacci pertama yang lebih dari 1000, dan suku ke berapa itu.",
"h": "Kamu tidak tahu butuh berapa suku, jadi pakai while dengan kondisi a <= 1000.",
"a": "let a = 0, b = 1, ke = 1;\nwhile (a <= 1000) {\n  [a, b] = [b, a + b];\n  ke++;\n}\nconsole.log(`Suku ke-${ke}: ${a}`);",
"out": "Suku ke-18: 1597"
}
]
},
{
"k": "c",
"t": "Bubble sort: loop di dalam loop",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BubbleSort",
"p": [
{
"t": "dec",
"v": "a",
"ty": "Integer",
"arr": "4"
},
{
"t": "asg",
"v": "a",
"e": "[25, 12, 22, 11]"
},
{
"t": "dec",
"v": "j, t, putaran",
"ty": "Integer"
},
{
"t": "dec",
"v": "adaTukar",
"ty": "Boolean"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
},
{
"t": "asg",
"v": "putaran",
"e": "0"
},
{
"t": "while",
"c": "adaTukar",
"b": [
{
"t": "asg",
"v": "adaTukar",
"e": "false"
},
{
"t": "asg",
"v": "putaran",
"e": "putaran + 1"
},
{
"t": "for",
"v": "j",
"a": "0",
"z": "3 - putaran",
"b": [
{
"t": "if",
"c": "a[j] > a[j + 1]",
"y": [
{
"t": "asg",
"v": "t",
"e": "a[j]"
},
{
"t": "asg",
"v": "a[j]",
"e": "a[j + 1]"
},
{
"t": "asg",
"v": "a[j + 1]",
"e": "t"
},
{
"t": "asg",
"v": "adaTukar",
"e": "true"
}
],
"n": []
}
]
}
]
},
{
"t": "out",
"e": "\"Terurut: \" & a"
}
]
},
"b": [
"Bubble sort mengurutkan data dengan cara paling sederhana: bandingkan dua angka yang <b>bersebelahan</b>, tukar jika urutannya salah, lalu geser ke pasangan berikutnya. Setelah satu putaran, angka terbesar pasti sudah \"menggelembung\" ke ujung kanan.",
"Algoritma ini memakai dua loop. <b>Loop dalam (for)</b> berjalan dari kiri ke kanan, jumlah pasangannya jelas. <b>Loop luar (while)</b> mengulang putaran selama masih ada pertukaran. Variabel penanda <code>adaTukar</code> membuat program berhenti lebih awal jika data sudah terurut.",
"Setiap putaran, satu angka terbesar sudah di tempatnya, jadi loop dalam cukup sampai <code>n - putaran</code>. Detail kecil ini menghemat perbandingan yang tidak perlu.",
"Bubble sort lambat untuk data besar (sekitar n² perbandingan), jadi di dunia kerja kita memakai fungsi sort bawaan bahasa. Tetapi bubble sort adalah latihan terbaik untuk memahami loop bersarang, indeks, dan menukar nilai."
],
"tb": [
{
"c": "Isi array setiap putaran",
"h": [
"Putaran",
"Isi array",
"Yang sudah di tempat"
],
"r": [
[
"Awal",
"64 25 12 22 11",
"-"
],
[
"1",
"25 12 22 11 64",
"64"
],
[
"2",
"12 22 11 25 64",
"25, 64"
],
[
"3",
"12 11 22 25 64",
"22, 25, 64"
],
[
"4",
"11 12 22 25 64",
"semua"
]
]
}
],
"code": "const nilai = [64, 25, 12, 22, 11];\nconst n = nilai.length;\nlet adaTukar = true;\nlet putaran = 0;\n// WHILE luar: berhenti jika satu putaran tidak ada pertukaran\nwhile (adaTukar) {\n  adaTukar = false;\n  putaran++;\n  // FOR dalam: bandingkan pasangan bersebelahan\n  for (let j = 0; j < n - putaran; j++) {\n    if (nilai[j] > nilai[j + 1]) {\n      [nilai[j], nilai[j + 1]] = [nilai[j + 1], nilai[j]];\n      adaTukar = true;\n    }\n  }\n  console.log(`Putaran ${putaran}: [${nilai.join(\", \")}]`);\n}\nconsole.log(`Terurut: [${nilai.join(\", \")}]`);",
"out": "Putaran 1: [25, 12, 22, 11, 64]\nPutaran 2: [12, 22, 11, 25, 64]\nPutaran 3: [12, 11, 22, 25, 64]\nPutaran 4: [11, 12, 22, 25, 64]\nPutaran 5: [11, 12, 22, 25, 64]\nTerurut: [11, 12, 22, 25, 64]",
"pts": [
"Bandingkan pasangan bersebelahan, tukar jika salah urutan.",
"Loop dalam for (jumlah pasangan jelas), loop luar while (sampai tidak ada pertukaran).",
"Penanda pertukaran membuat sort berhenti lebih awal."
],
"q": [
[
"Setelah putaran pertama bubble sort (urut naik), di mana angka terbesar?",
[
"Di indeks 0",
"Di ujung kanan",
"Belum pasti"
],
1,
"Angka terbesar selalu terbawa sampai ujung kanan pada putaran pertama."
],
[
"Untuk apa variabel penanda pertukaran?",
[
"Menghitung jumlah data",
"Menghentikan loop luar jika satu putaran tidak ada pertukaran",
"Menyimpan angka terbesar"
],
1,
"Jika tidak ada pertukaran, data sudah terurut."
],
[
"Kenapa loop dalam cukup sampai n - putaran?",
[
"Agar tidak error",
"Karena angka di ujung kanan sudah pasti di tempatnya",
"Karena aturan bahasa"
],
1,
"Bagian kanan yang sudah terurut tidak perlu dibandingkan lagi."
]
],
"lang": "js",
"so": [
{
"q": "Urutkan nama [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"] sesuai abjad dengan bubble sort.",
"h": "Logikanya sama, hanya cara membandingkan teks yang berbeda: Python memakai >, JavaScript/TypeScript memakai localeCompare, Java memakai compareTo.",
"a": "const nama = [\"Rina\", \"Agus\", \"Dewi\", \"Budi\"];\nlet adaTukar = true;\nwhile (adaTukar) {\n  adaTukar = false;\n  for (let j = 0; j < nama.length - 1; j++) {\n    if (nama[j].localeCompare(nama[j + 1]) > 0) {\n      [nama[j], nama[j + 1]] = [nama[j + 1], nama[j]];\n      adaTukar = true;\n    }\n  }\n}\nconsole.log(nama.join(\", \"));",
"out": "Agus, Budi, Dewi, Rina"
},
{
"q": "Ubah bubble sort agar mengurutkan dari besar ke kecil, lalu hitung berapa kali terjadi pertukaran untuk [3, 1, 4, 1, 5].",
"h": "Cukup balik tanda perbandingan menjadi <, dan tambah penghitung setiap kali menukar.",
"a": "const data = [3, 1, 4, 1, 5];\nlet tukar = 0;\nfor (let i = 0; i < data.length - 1; i++) {\n  for (let j = 0; j < data.length - 1 - i; j++) {\n    if (data[j] < data[j + 1]) {\n      [data[j], data[j + 1]] = [data[j + 1], data[j]];\n      tukar++;\n    }\n  }\n}\nconsole.log(`[${data.join(\", \")}] pertukaran: ${tukar}`);",
"out": "[5, 4, 3, 1, 1] pertukaran: 6"
}
]
},
{
"k": "c",
"t": "FizzBuzz dan bilangan prima: break dan loop bersarang",
"nodes": [
"Loops",
"Conditionals"
],
"viz": "fc",
"fc": {
"name": "CekPrima",
"in": [
"29"
],
"p": [
{
"t": "dec",
"v": "x, d",
"ty": "Integer"
},
{
"t": "dec",
"v": "prima",
"ty": "Boolean"
},
{
"t": "in",
"v": "x"
},
{
"t": "asg",
"v": "prima",
"e": "x >= 2"
},
{
"t": "asg",
"v": "d",
"e": "2"
},
{
"t": "while",
"c": "d * d <= x and prima",
"b": [
{
"t": "if",
"c": "x mod d = 0",
"y": [
{
"t": "asg",
"v": "prima",
"e": "false"
}
],
"n": []
},
{
"t": "asg",
"v": "d",
"e": "d + 1"
}
]
},
{
"t": "if",
"c": "prima",
"y": [
{
"t": "out",
"e": "x & \" adalah prima\""
}
],
"n": [
{
"t": "out",
"e": "x & \" bukan prima\""
}
]
}
]
},
"b": [
"<b>FizzBuzz</b> adalah soal wawancara klasik: untuk angka 1 sampai 15, tampilkan \"Fizz\" jika habis dibagi 3, \"Buzz\" jika habis dibagi 5, \"FizzBuzz\" jika habis dibagi keduanya, dan angkanya sendiri jika tidak. Rentangnya jelas, jadi pakai <b>for</b>. Jebakannya: cek kelipatan 15 lebih dulu, karena jika cek 3 duluan, angka 15 sudah keburu menjadi \"Fizz\".",
"<b>Bilangan prima</b> hanya habis dibagi 1 dan dirinya sendiri. Untuk setiap angka (loop luar), kita coba pembagi dari 2 (loop dalam). Begitu ketemu satu pembagi, angka itu pasti bukan prima, jadi <b>break</b> menghentikan loop dalam tanpa membuang waktu.",
"Pembagi cukup dicoba sampai akar angkanya (<code>d * d &lt;= x</code>). Jika 36 = 4 × 9, salah satu faktornya pasti ≤ 6. Ini mengubah 1.000 percobaan menjadi sekitar 31. Variabel penanda <code>isPrima</code> mencatat apakah loop dalam pernah berhenti karena break.",
"Visual di bawah memeriksa satu angka dengan while dan penanda, karena Flowgorithm tidak punya break. Ganti inputnya, misalnya 91 atau 97, lalu jalankan."
],
"tb": [
{
"c": "break dan continue",
"h": [
"Perintah",
"Efek",
"Kapan dipakai"
],
"r": [
[
"break",
"Keluar dari loop terdekat",
"Jawaban sudah ditemukan, sisa putaran tidak perlu"
],
[
"continue",
"Lompat ke putaran berikutnya",
"Lewati data yang tidak relevan"
],
[
"penanda (flag)",
"Variabel boolean yang dicek setelah loop",
"Bahasa atau alat tanpa break, misalnya Flowgorithm"
]
]
}
],
"code": "// FizzBuzz: FOR karena rentangnya jelas (1 sampai 15)\nconst hasil = [];\nfor (let i = 1; i <= 15; i++) {\n  if (i % 15 === 0) hasil.push(\"FizzBuzz\");\n  else if (i % 3 === 0) hasil.push(\"Fizz\");\n  else if (i % 5 === 0) hasil.push(\"Buzz\");\n  else hasil.push(i);\n}\nconsole.log(hasil.join(\" \"));\n\n// Bilangan prima 2..30: FOR bersarang + break\nconst prima = [];\nfor (let x = 2; x <= 30; x++) {\n  let isPrima = true;\n  for (let d = 2; d * d <= x; d++) {\n    if (x % d === 0) {\n      isPrima = false;\n      break;          // tidak perlu cek pembagi lain\n    }\n  }\n  if (isPrima) prima.push(x);\n}\nconsole.log(\"Prima:\", prima.join(\" \"));",
"out": "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\nPrima: 2 3 5 7 11 13 17 19 23 29",
"pts": [
"Urutan if penting: kondisi paling khusus dicek lebih dulu.",
"break menghentikan loop terdekat saat jawaban sudah pasti.",
"Pembagi prima cukup dicek sampai akar angkanya."
],
"q": [
[
"Jika FizzBuzz mengecek \"habis dibagi 3\" lebih dulu, apa yang tampil untuk 15?",
[
"FizzBuzz",
"Fizz",
"Buzz"
],
1,
"Kondisi pertama yang benar langsung dipakai."
],
[
"Pada loop bersarang, break menghentikan loop yang mana?",
[
"Semua loop",
"Loop terdekat yang membungkusnya",
"Loop terluar"
],
1,
"break hanya keluar dari satu tingkat loop."
],
[
"Untuk mengecek apakah 97 prima, pembagi paling besar yang perlu dicoba adalah?",
[
"96",
"48",
"9"
],
2,
"9 × 9 = 81 ≤ 97, sedangkan 10 × 10 = 100 > 97."
]
],
"lang": "js",
"so": [
{
"q": "Tampilkan tabel perkalian 1 sampai 5 dalam bentuk kotak (5 baris, 5 kolom).",
"h": "For luar untuk baris, for dalam untuk kolom. Keduanya punya batas yang jelas.",
"a": "for (let i = 1; i <= 5; i++) {\n  let baris = \"\";\n  for (let j = 1; j <= 5; j++) {\n    baris += String(i * j).padStart(4);\n  }\n  console.log(baris);\n}",
"out": "   1   2   3   4   5\n   2   4   6   8  10\n   3   6   9  12  15\n   4   8  12  16  20\n   5  10  15  20  25"
},
{
"q": "Cari bilangan prima pertama yang lebih besar dari 100.",
"h": "Kita tidak tahu harus mencoba berapa angka, jadi loop luar memakai while. Pengecekan pembagi tetap memakai for dengan break.",
"a": "let x = 101;\nwhile (true) {\n  let prima = true;\n  for (let d = 2; d * d <= x; d++) {\n    if (x % d === 0) { prima = false; break; }\n  }\n  if (prima) break;\n  x++;\n}\nconsole.log(\"Prima pertama > 100:\", x);",
"out": "Prima pertama > 100: 101"
}
]
},
{
"k": "c",
"t": "Faktorial, jumlah digit, dan palindrom",
"nodes": [
"Loops"
],
"viz": "fc",
"fc": {
"name": "JumlahDigit",
"in": [
"90417"
],
"p": [
{
"t": "dec",
"v": "angka, jumlah",
"ty": "Integer"
},
{
"t": "in",
"v": "angka"
},
{
"t": "asg",
"v": "jumlah",
"e": "0"
},
{
"t": "while",
"c": "angka > 0",
"b": [
{
"t": "asg",
"v": "jumlah",
"e": "jumlah + angka mod 10"
},
{
"t": "asg",
"v": "angka",
"e": "Int(angka / 10)"
}
]
},
{
"t": "out",
"e": "\"Jumlah digit: \" & jumlah"
}
]
},
"b": [
"Tiga soal ini melatih kapan memakai for dan kapan while. <b>Faktorial</b> 5! = 1 × 2 × 3 × 4 × 5: banyak perkaliannya pasti, jadi <b>for</b>.",
"<b>Jumlah digit</b> 90417 = 9 + 0 + 4 + 1 + 7 = 21. Kita tidak tahu angkanya punya berapa digit, jadi pakai <b>while</b>: ambil digit terakhir dengan <code>% 10</code>, lalu buang dengan pembagian bulat <code>Math.floor(x / 10)</code>. Berhenti saat angkanya habis (0).",
"<b>Palindrom</b> adalah kata yang sama jika dibaca dari depan dan belakang, seperti \"katak\". Pakai <b>dua penunjuk</b>: satu dari kiri, satu dari kanan, bergerak ke tengah selama <code>kiri &lt; kanan</code>. Begitu ada huruf yang berbeda, langsung break.",
"Visual di bawah menjalankan jumlah digit. Coba ganti inputnya dengan angka lain dan hitung dulu di kepala sebelum menekan Berikutnya."
],
"tb": [
{
"c": "Jejak jumlah digit 90417",
"h": [
"Putaran",
"angka % 10",
"jumlah",
"angka setelah dibagi 10"
],
"r": [
[
"1",
"7",
"7",
"9041"
],
[
"2",
"1",
"8",
"904"
],
[
"3",
"4",
"12",
"90"
],
[
"4",
"0",
"12",
"9"
],
[
"5",
"9",
"21",
"0"
]
]
}
],
"code": "// Faktorial: FOR, jumlah perkalian = n\nconst n = 5;\nlet faktorial = 1;\nfor (let i = 2; i <= n; i++) {\n  faktorial *= i;\n}\nconsole.log(`${n}! = ${faktorial}`);\n\n// Jumlah digit: WHILE, banyak digit belum diketahui\nconst angka = 90417;\nlet sisa = angka, jumlah = 0;\nwhile (sisa > 0) {\n  jumlah += sisa % 10;          // ambil digit terakhir\n  sisa = Math.floor(sisa / 10); // buang digit terakhir\n}\nconsole.log(`Jumlah digit ${angka} = ${jumlah}`);\n\n// Palindrom: WHILE dua penunjuk bergerak ke tengah\nconst kata = \"katak\";\nlet kiri = 0, kanan = kata.length - 1, palindrom = true;\nwhile (kiri < kanan) {\n  if (kata[kiri] !== kata[kanan]) { palindrom = false; break; }\n  kiri++;\n  kanan--;\n}\nconsole.log(`${kata} palindrom? ${palindrom}`);",
"out": "5! = 120\nJumlah digit 90417 = 21\nkatak palindrom? true",
"pts": [
"% 10 mengambil digit terakhir, bagi 10 (bulat) membuangnya.",
"Banyak digit tidak diketahui → while.",
"Dua penunjuk bergerak ke tengah untuk memeriksa palindrom."
],
"q": [
[
"Berapa hasil 4827 % 10?",
[
"4",
"7",
"482"
],
1,
"Sisa bagi 10 adalah digit terakhir."
],
[
"Loop paling cocok untuk menghitung 10! (faktorial 10)?",
[
"for",
"while",
"do-while"
],
0,
"Banyak perkaliannya pasti."
],
[
"Pada pemeriksaan palindrom \"level\", berapa kali perbandingan huruf terjadi?",
[
"5",
"2",
"1"
],
1,
"Pasangan (l, l) dan (e, e); huruf tengah v tidak perlu dibandingkan."
]
],
"lang": "js",
"so": [
{
"q": "Balik angka 12345 menjadi 54321 tanpa mengubahnya menjadi teks.",
"h": "Ambil digit terakhir dengan % 10, tempel ke hasil dengan hasil * 10 + digit, buang digit terakhir dengan pembagian bulat. Ulangi selama angka > 0.",
"a": "let angka = 12345, balik = 0;\nwhile (angka > 0) {\n  balik = balik * 10 + (angka % 10);\n  angka = Math.floor(angka / 10);\n}\nconsole.log(\"Dibalik:\", balik);",
"out": "Dibalik: 54321"
},
{
"q": "Hitung 2 pangkat 10 dengan loop, tanpa operator pangkat.",
"h": "Perkalian diulang tepat 10 kali, jadi for.",
"a": "let hasil = 1;\nfor (let i = 0; i < 10; i++) {\n  hasil *= 2;\n}\nconsole.log(\"2^10 =\", hasil);",
"out": "2^10 = 1024"
}
]
},
{
"k": "c",
"t": "Binary search: membagi dua sampai ketemu",
"nodes": [
"Loops",
"Arrays"
],
"viz": "fc",
"fc": {
"name": "BinarySearch",
"in": [
"20000"
],
"p": [
{
"t": "dec",
"v": "harga",
"ty": "Integer",
"arr": "7"
},
{
"t": "asg",
"v": "harga",
"e": "[5000, 8000, 12000, 15000, 20000, 27000, 35000]"
},
{
"t": "dec",
"v": "cari, kiri, kanan, tengah, posisi",
"ty": "Integer"
},
{
"t": "in",
"v": "cari"
},
{
"t": "asg",
"v": "kiri",
"e": "0"
},
{
"t": "asg",
"v": "kanan",
"e": "6"
},
{
"t": "asg",
"v": "posisi",
"e": "-1"
},
{
"t": "while",
"c": "kiri <= kanan and posisi = -1",
"b": [
{
"t": "asg",
"v": "tengah",
"e": "Int((kiri + kanan) / 2)"
},
{
"t": "if",
"c": "harga[tengah] = cari",
"y": [
{
"t": "asg",
"v": "posisi",
"e": "tengah"
}
],
"n": [
{
"t": "if",
"c": "harga[tengah] < cari",
"y": [
{
"t": "asg",
"v": "kiri",
"e": "tengah + 1"
}
],
"n": [
{
"t": "asg",
"v": "kanan",
"e": "tengah - 1"
}
]
}
]
}
]
},
{
"t": "out",
"e": "\"Posisi: \" & posisi"
}
]
},
"b": [
"Mencari harga di daftar 1.000 barang satu per satu (linear search) bisa butuh 1.000 langkah. Jika daftarnya <b>sudah terurut</b>, kita bisa jauh lebih cepat: lihat bagian tengah, lalu buang separuh daftar yang pasti tidak berisi jawabannya.",
"Simpan dua batas, <code>kiri</code> dan <code>kanan</code>. Selama <code>kiri &lt;= kanan</code>, hitung <code>tengah</code>. Jika nilai tengah terlalu kecil, geser kiri ke tengah + 1. Jika terlalu besar, geser kanan ke tengah - 1. Banyak langkahnya tidak diketahui sebelumnya, jadi loopnya <b>while</b>.",
"Setiap langkah membuang separuh data, jadi 1.000 data cukup dicari dalam paling banyak 10 langkah, dan 1 juta data dalam 20 langkah. Inilah alasan database dan kamus memakai data terurut.",
"Visual di bawah mencari harga di 7 data. Coba input 5000, 35000, atau 9000 (tidak ada di daftar) dan perhatikan bagaimana kiri dan kanan bergerak."
],
"tb": [
{
"c": "Linear search vs binary search",
"h": [
"Aspek",
"Linear search",
"Binary search"
],
"r": [
[
"Syarat data",
"Bebas",
"Harus terurut"
],
[
"Langkah terburuk (1.000 data)",
"1.000",
"10"
],
[
"Jenis loop",
"for (setiap data)",
"while (sampai ketemu atau habis)"
],
[
"Kapan dipakai",
"Data sedikit atau tidak terurut",
"Data besar dan terurut"
]
]
}
],
"code": "const harga = [5000, 8000, 12000, 15000, 20000, 27000, 35000];\nconst cari = 20000;\nlet kiri = 0, kanan = harga.length - 1, langkah = 0, posisi = -1;\n// WHILE: berhenti saat ketemu atau ruang pencarian habis\nwhile (kiri <= kanan) {\n  langkah++;\n  const tengah = Math.floor((kiri + kanan) / 2);\n  console.log(`Langkah ${langkah}: cek indeks ${tengah} (${harga[tengah]})`);\n  if (harga[tengah] === cari) { posisi = tengah; break; }\n  else if (harga[tengah] < cari) kiri = tengah + 1;\n  else kanan = tengah - 1;\n}\nconsole.log(`Ketemu di indeks ${posisi} setelah ${langkah} langkah`);",
"out": "Langkah 1: cek indeks 3 (15000)\nLangkah 2: cek indeks 5 (27000)\nLangkah 3: cek indeks 4 (20000)\nKetemu di indeks 4 setelah 3 langkah",
"pts": [
"Binary search hanya untuk data terurut.",
"Setiap langkah membuang separuh ruang pencarian.",
"Berhenti saat ketemu atau kiri > kanan."
],
"q": [
[
"Apa syarat utama binary search?",
[
"Data berupa angka",
"Data sudah terurut",
"Data kurang dari 100"
],
1,
"Tanpa urutan, kita tidak tahu separuh mana yang harus dibuang."
],
[
"Jika harga[tengah] lebih kecil dari yang dicari, apa yang dilakukan?",
[
"kanan = tengah - 1",
"kiri = tengah + 1",
"Berhenti"
],
1,
"Jawabannya pasti di sebelah kanan tengah."
],
[
"Kira-kira berapa langkah maksimum untuk 1 juta data terurut?",
[
"20",
"1.000",
"500.000"
],
0,
"2 pangkat 20 ≈ 1 juta."
]
],
"lang": "js",
"so": [
{
"q": "Komputer menebak angka rahasia 73 di antara 1 sampai 100 dengan cara binary search. Tampilkan setiap tebakan.",
"h": "Sama seperti mencari di array terurut, hanya saja \"array\"-nya adalah rentang angka 1 sampai 100.",
"a": "const rahasia = 73;\nlet bawah = 1, atas = 100;\nwhile (true) {\n  const tebak = Math.floor((bawah + atas) / 2);\n  console.log(\"Tebak\", tebak);\n  if (tebak === rahasia) break;\n  if (tebak < rahasia) bawah = tebak + 1;\n  else atas = tebak - 1;\n}",
"out": "Tebak 50\nTebak 75\nTebak 62\nTebak 68\nTebak 71\nTebak 73"
},
{
"q": "Berapa langkah paling banyak yang dibutuhkan binary search untuk 1.000 data? Hitung dengan membagi dua terus sampai habis.",
"h": "Selama masih ada data (n > 0), bagi dua dan tambah 1 langkah. Ini while karena jumlah langkah adalah hal yang dicari.",
"a": "let n = 1000, langkah = 0;\nwhile (n > 0) {\n  n = Math.floor(n / 2);\n  langkah++;\n}\nconsole.log(\"Maksimal\", langkah, \"langkah\");",
"out": "Maksimal 10 langkah"
}
]
}
]
}
};
const T={java:JAVA_MODULES,python:PY_MODULES,ts:TS_MODULES,fe0:FE0_MODULES};
for(const k in ALGO)if(!T[k].some(m=>m.t===ALGO[k].t))T[k].push(ALGO[k]);
})();
