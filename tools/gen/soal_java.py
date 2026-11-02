"""Soal latihan tambahan untuk pelajaran konsep (k:'c') di jalur Java."""
from mobile_dart_x import S


def Jv(q, h, a, out=None): return S(q, h, a, out, lang='java')
def Tx(q, h, a): return S(q, h, a, lang='text')
def Bs(q, h, a): return S(q, h, a, lang='bash')
def Xm(q, h, a): return S(q, h, a, lang='xml')
def Sq(q, h, a): return S(q, h, a, lang='sql')


JAVA = {
'Tipe data primitif & type casting': [
  Jv('Harga kopi <code>double harga = 18750.75</code>. Ubah ke <code>int</code> lalu cetak keduanya. Apa yang terjadi pada angka di belakang koma?', 'Casting sempit (narrowing) ditulis <code>(int) harga</code> dan memotong desimal, bukan membulatkan.',
     'public class Main {\n    public static void main(String[] args) {\n        double harga = 18750.75;\n        int bulat = (int) harga;      // dipotong, bukan dibulatkan\n        System.out.println(harga);\n        System.out.println(bulat);\n    }\n}', '18750.75\n18750'),
  Jv('Kenapa <code>int total = 7 / 2;</code> menghasilkan 3? Tulis cara mendapat 3.5.', 'int dibagi int tetap int. Jadikan salah satunya double.',
     'public class Main {\n    public static void main(String[] args) {\n        int a = 7, b = 2;\n        System.out.println(a / b);           // pembagian bulat\n        System.out.println((double) a / b);  // salah satu jadi double\n        System.out.println(a % b);           // sisa bagi\n    }\n}', '3\n3.5\n1'),
  Jv('Apa yang tercetak? <code>byte b = (byte) 200;</code> lalu <code>char c = \'A\'; c += 2;</code>', 'byte hanya -128 sampai 127, jadi 200 "berputar" (200 - 256). char adalah angka Unicode.',
     'public class Main {\n    public static void main(String[] args) {\n        byte b = (byte) 200;\n        char c = \'A\';\n        c += 2;\n        System.out.println(b);\n        System.out.println(c);\n        System.out.println((int) c);\n    }\n}', '-56\nC\n67'),
],
'Kelas Math & operasi angka': [
  Jv('Hitung sisi miring segitiga siku-siku dengan sisi 6 dan 8, lalu luas lingkaran berjari-jari 7 dibulatkan 2 desimal.', 'Math.hypot atau Math.sqrt, Math.PI, Math.round(x * 100) / 100.0.',
     'public class Main {\n    public static void main(String[] args) {\n        double miring = Math.sqrt(6 * 6 + 8 * 8);\n        double luas = Math.PI * Math.pow(7, 2);\n        System.out.println(miring);\n        System.out.println(Math.round(luas * 100) / 100.0);\n    }\n}', '10.0\n153.94'),
  Jv('Buat angka acak dadu 1 sampai 6 memakai <code>Math.random()</code>, dan tunjukkan beda <code>Math.floor</code>, <code>Math.ceil</code>, <code>Math.round</code> untuk -2.5.', 'Math.random() menghasilkan 0.0 sampai kurang dari 1.0.',
     'public class Main {\n    public static void main(String[] args) {\n        int dadu = (int) (Math.random() * 6) + 1;   // 1..6\n        System.out.println("Dadu: " + dadu);\n        System.out.println(Math.floor(-2.5));\n        System.out.println(Math.ceil(-2.5));\n        System.out.println(Math.round(-2.5));\n    }\n}', 'Dadu: 4   (acak)\n-3.0\n-2.0\n-2'),
],
'Scope: di mana variabel hidup': [
  Jv('Kode berikut gagal dikompilasi. Kenapa, dan bagaimana memperbaikinya?<br><code>for (int i = 0; i &lt; 3; i++) { int kuadrat = i * i; }<br>System.out.println(kuadrat);</code>', 'Variabel yang dibuat di dalam blok { } hilang setelah blok selesai.',
     'public class Main {\n    public static void main(String[] args) {\n        int kuadrat = 0;                 // pindahkan ke luar blok\n        for (int i = 0; i < 3; i++) {\n            kuadrat = i * i;\n        }\n        System.out.println(kuadrat);\n    }\n}', '4'),
  Jv('Apa yang tercetak? Field <code>nilai = 10</code>, lalu method punya variabel lokal <code>nilai = 99</code> dan mencetak <code>nilai</code> serta <code>this.nilai</code>.', 'Variabel lokal "membayangi" (shadowing) field yang bernama sama.',
     'public class Main {\n    int nilai = 10;\n\n    void cetak() {\n        int nilai = 99;\n        System.out.println(nilai);\n        System.out.println(this.nilai);\n    }\n\n    public static void main(String[] args) {\n        new Main().cetak();\n    }\n}', '99\n10'),
],
'Method String & StringBuilder': [
  Jv('Dari <code>"  rina siregar  "</code>, buat nama rapi "Rina Siregar" dan hitung jumlah huruf a.', 'trim, split(" "), substring(0,1).toUpperCase(), lalu loop charAt.',
     'public class Main {\n    public static void main(String[] args) {\n        String mentah = "  rina siregar  ";\n        StringBuilder sb = new StringBuilder();\n        for (String kata : mentah.trim().split(" ")) {\n            sb.append(kata.substring(0, 1).toUpperCase())\n              .append(kata.substring(1)).append(" ");\n        }\n        String rapi = sb.toString().trim();\n        int a = 0;\n        for (char c : rapi.toLowerCase().toCharArray()) if (c == \'a\') a++;\n        System.out.println(rapi);\n        System.out.println(a);\n    }\n}', 'Rina Siregar\n2'),
  Jv('Cek apakah "Kasur ini rusak" palindrom (abaikan spasi dan huruf besar).', 'Hapus spasi dengan replace, kecilkan huruf, lalu bandingkan dengan new StringBuilder(s).reverse().',
     'public class Main {\n    public static void main(String[] args) {\n        String s = "Kasur ini rusak".replace(" ", "").toLowerCase();\n        String balik = new StringBuilder(s).reverse().toString();\n        System.out.println(s.equals(balik));\n    }\n}', 'true'),
  Jv('Kenapa <code>==</code> tidak boleh dipakai untuk membandingkan isi String? Tunjukkan contohnya.', '== membandingkan alamat objek, equals membandingkan isi.',
     'public class Main {\n    public static void main(String[] args) {\n        String a = "kopi";\n        String b = new String("kopi");\n        System.out.println(a == b);       // objek berbeda\n        System.out.println(a.equals(b));  // isi sama\n    }\n}', 'false\ntrue'),
],
'switch & operator ternary': [
  Jv('Pakai switch expression (Java 14+) untuk mengubah angka hari 1 sampai 7 menjadi "Kerja" atau "Libur" (6 dan 7 libur).', 'case 6, 7 -> "Libur"; default -> "Kerja";',
     'public class Main {\n    public static void main(String[] args) {\n        for (int hari = 5; hari <= 7; hari++) {\n            String jenis = switch (hari) {\n                case 6, 7 -> "Libur";\n                default -> "Kerja";\n            };\n            System.out.println(hari + " " + jenis);\n        }\n    }\n}', '5 Kerja\n6 Libur\n7 Libur'),
  Jv('Pakai ternary untuk mencetak "Lulus" jika nilai &gt;= 75 dan "Remedial" jika tidak, untuk nilai 80 dan 60.', 'kondisi ? nilaiJikaBenar : nilaiJikaSalah',
     'public class Main {\n    public static void main(String[] args) {\n        int[] nilai = {80, 60};\n        for (int n : nilai) {\n            System.out.println(n + " " + (n >= 75 ? "Lulus" : "Remedial"));\n        }\n    }\n}', '80 Lulus\n60 Remedial'),
],
'Kelas Arrays & array dua dimensi': [
  Jv('Urutkan <code>{42, 7, 19, 3}</code>, cetak dengan <code>Arrays.toString</code>, lalu cari posisi 19 dengan binarySearch.', 'binarySearch hanya benar pada array yang sudah terurut.',
     'import java.util.Arrays;\n\npublic class Main {\n    public static void main(String[] args) {\n        int[] a = {42, 7, 19, 3};\n        Arrays.sort(a);\n        System.out.println(Arrays.toString(a));\n        System.out.println(Arrays.binarySearch(a, 19));\n    }\n}', '[3, 7, 19, 42]\n2'),
  Jv('Nilai 3 siswa untuk 2 ujian disimpan di array 2D <code>{{80, 90}, {70, 65}, {95, 85}}</code>. Cetak rata-rata tiap siswa.', 'Loop luar untuk baris (siswa), loop dalam untuk kolom (ujian).',
     'public class Main {\n    public static void main(String[] args) {\n        int[][] nilai = {{80, 90}, {70, 65}, {95, 85}};\n        for (int i = 0; i < nilai.length; i++) {\n            int total = 0;\n            for (int n : nilai[i]) total += n;\n            System.out.println("Siswa " + (i + 1) + ": " + (double) total / nilai[i].length);\n        }\n    }\n}', 'Siswa 1: 85.0\nSiswa 2: 67.5\nSiswa 3: 90.0'),
  Jv('Cetak matriks 3x3 berikut dalam bentuk tabel memakai format specifier lebar 4: <code>{{1,2,3},{4,5,6},{7,8,9}}</code>, lalu cetak hasil transposnya.', 'printf("%4d", x) membuat setiap angka selebar 4 karakter. Transpos: baris jadi kolom.',
     'public class Main {\n    public static void main(String[] args) {\n        int[][] m = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n        for (int i = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++) System.out.printf("%4d", m[j][i]);\n            System.out.println();\n        }\n    }\n}', '   1   4   7\n   2   5   8\n   3   6   9'),
],
'Access specifier: public, private, protected': [
  Jv('Buat kelas <code>Rekening</code> dengan saldo private. Sediakan setor() yang menolak jumlah negatif dan getter getSaldo().', 'Field private hanya bisa diubah lewat method kelas itu sendiri, jadi aturannya terjaga.',
     'class Rekening {\n    private long saldo;\n\n    public void setor(long jumlah) {\n        if (jumlah <= 0) {\n            System.out.println("Jumlah tidak valid");\n            return;\n        }\n        saldo += jumlah;\n    }\n\n    public long getSaldo() { return saldo; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Rekening r = new Rekening();\n        r.setor(50000);\n        r.setor(-1000);\n        System.out.println(r.getSaldo());\n    }\n}', 'Jumlah tidak valid\n50000'),
  Tx('Isi tabel: dari mana saja anggota dengan modifier public, protected, tanpa modifier (default), dan private bisa diakses?', 'Urutan dari paling terbuka: public, protected, default, private.',
     '             kelas sama  paket sama  subclass beda paket  di mana saja\npublic           ya          ya              ya                ya\nprotected        ya          ya              ya                tidak\n(default)        ya          ya              tidak             tidak\nprivate          ya          tidak           tidak             tidak'),
],
'Kata kunci static & final': [
  Jv('Buat kelas <code>Tiket</code> yang memberi nomor urut otomatis (1, 2, 3, ...) ke setiap objek baru memakai field static.', 'static int berikutnya = 1; lalu di konstruktor: nomor = berikutnya++;',
     'class Tiket {\n    private static int berikutnya = 1;\n    final int nomor;\n\n    Tiket() { nomor = berikutnya++; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Tiket a = new Tiket(), b = new Tiket(), c = new Tiket();\n        System.out.println(a.nomor + " " + b.nomor + " " + c.nomor);\n    }\n}', '1 2 3'),
  Jv('Apakah isi list yang dideklarasikan <code>final</code> masih bisa diubah? Buktikan.', 'final mengunci variabelnya (tidak bisa diisi objek lain), bukan isi objeknya.',
     'import java.util.ArrayList;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        final List<String> menu = new ArrayList<>();\n        menu.add("Kopi");          // boleh: isi objek berubah\n        menu.add("Teh");\n        // menu = new ArrayList<>(); // error: variabel final\n        System.out.println(menu);\n    }\n}', '[Kopi, Teh]'),
],
'Siklus hidup objek & garbage collector': [
  Tx('Tandai kapan objek "Kopi" boleh dibersihkan garbage collector:<br><code>Produk p = new Produk("Kopi");<br>Produk q = p;<br>p = null;<br>q = new Produk("Teh");</code>', 'Objek bisa dibersihkan jika tidak ada lagi variabel yang merujuknya.',
     'Baris 1: objek Kopi dirujuk p.\nBaris 2: Kopi dirujuk p dan q.\nBaris 3: p = null, Kopi masih dirujuk q.\nBaris 4: q menunjuk Teh. Kopi tidak dirujuk siapa pun,\n        sekarang Kopi boleh dibersihkan GC (kapan tepatnya ditentukan JVM).'),
  Jv('Pakai try-with-resources agar sumber daya ditutup otomatis. Buat kelas <code>Koneksi</code> yang implements AutoCloseable dan mencetak "dibuka", "dipakai", "ditutup".', 'Jangan mengandalkan finalize() (sudah usang). Pakai AutoCloseable.',
     'class Koneksi implements AutoCloseable {\n    Koneksi() { System.out.println("dibuka"); }\n    void pakai() { System.out.println("dipakai"); }\n    @Override public void close() { System.out.println("ditutup"); }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        try (Koneksi k = new Koneksi()) {\n            k.pakai();\n        }\n    }\n}', 'dibuka\ndipakai\nditutup'),
],
'Pass by value (juga untuk objek)': [
  Jv('Tebak hasilnya, lalu jelaskan: method <code>ubah(int x)</code> mengisi x = 100, dan method <code>tambah(int[] a)</code> mengisi a[0] = 100.', 'Java selalu menyalin nilai. Untuk objek, yang disalin adalah referensinya, jadi isi objek yang sama bisa diubah.',
     'public class Main {\n    static void ubah(int x) { x = 100; }\n    static void tambah(int[] a) { a[0] = 100; }\n\n    public static void main(String[] args) {\n        int n = 5;\n        int[] arr = {5};\n        ubah(n);\n        tambah(arr);\n        System.out.println(n);       // salinan yang diubah\n        System.out.println(arr[0]);  // objek yang sama diubah\n    }\n}', '5\n100'),
  Jv('Kenapa method <code>tukar(String a, String b)</code> tidak bisa menukar dua variabel pemanggil? Tunjukkan cara yang berhasil.', 'Mengisi ulang parameter hanya mengubah salinan referensi. Kembalikan hasil atau pakai array.',
     'public class Main {\n    static String[] tukar(String a, String b) {\n        return new String[]{b, a};\n    }\n\n    public static void main(String[] args) {\n        String x = "kiri", y = "kanan";\n        String[] hasil = tukar(x, y);\n        x = hasil[0];\n        y = hasil[1];\n        System.out.println(x + " " + y);\n    }\n}', 'kanan kiri'),
],
'Kelas abstrak & abstraksi': [
  Jv('Buat kelas abstrak <code>Karyawan</code> dengan method abstrak <code>gaji()</code>. Turunkan Tetap (gaji 5.000.000) dan Harian (upah 150.000 x hari).', 'Subclass wajib meng-override method abstrak. Simpan dalam array bertipe Karyawan.',
     'abstract class Karyawan {\n    final String nama;\n    Karyawan(String nama) { this.nama = nama; }\n    abstract long gaji();\n}\n\nclass Tetap extends Karyawan {\n    Tetap(String n) { super(n); }\n    long gaji() { return 5_000_000; }\n}\n\nclass Harian extends Karyawan {\n    final int hari;\n    Harian(String n, int hari) { super(n); this.hari = hari; }\n    long gaji() { return 150_000L * hari; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Karyawan[] semua = {new Tetap("Rina"), new Harian("Sandi", 20)};\n        for (Karyawan k : semua) System.out.println(k.nama + " " + k.gaji());\n    }\n}', 'Rina 5000000\nSandi 3000000'),
  Tx('Kapan memilih kelas abstrak dan kapan interface?', 'Pikirkan: apakah ada state (field) bersama, dan apakah kelas perlu "menjadi" beberapa hal sekaligus?',
     'Kelas abstrak: ada field atau konstruktor bersama dan logika dasar yang\n  dipakai semua turunan (hubungan "adalah", satu induk saja).\nInterface: hanya kontrak kemampuan ("bisa"), tanpa state objek;\n  satu kelas boleh mengimplementasikan banyak interface.'),
],
'Overloading, overriding & binding': [
  Jv('Buat method overloading <code>luas</code>: satu parameter (persegi), dua parameter (persegi panjang), dan double (lingkaran).', 'Overloading: nama sama, daftar parameter berbeda. Dipilih saat kompilasi.',
     'public class Main {\n    static int luas(int s) { return s * s; }\n    static int luas(int p, int l) { return p * l; }\n    static double luas(double r) { return Math.PI * r * r; }\n\n    public static void main(String[] args) {\n        System.out.println(luas(4));\n        System.out.println(luas(4, 5));\n        System.out.printf("%.2f%n", luas(1.0));\n    }\n}', '16\n20\n3.14'),
  Jv('Apa yang tercetak? <code>Hewan h = new Kucing();</code> lalu <code>h.suara()</code>, di mana Kucing meng-override suara().', 'Method override dipilih saat program berjalan berdasarkan objek aslinya (dynamic binding).',
     'class Hewan { String suara() { return "..."; } }\nclass Kucing extends Hewan {\n    @Override String suara() { return "Meong"; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Hewan h = new Kucing();\n        System.out.println(h.suara());\n    }\n}', 'Meong'),
],
'Enum & record': [
  Jv('Buat enum <code>Ukuran</code> (KECIL, SEDANG, BESAR) yang menyimpan tambahan harga 0, 3000, 6000. Cetak semua beserta harganya.', 'Enum boleh punya field dan konstruktor. values() mengembalikan semua konstanta.',
     'enum Ukuran {\n    KECIL(0), SEDANG(3000), BESAR(6000);\n    final int tambahan;\n    Ukuran(int t) { tambahan = t; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        for (Ukuran u : Ukuran.values()) {\n            System.out.println(u + " +" + u.tambahan);\n        }\n    }\n}', 'KECIL +0\nSEDANG +3000\nBESAR +6000'),
  Jv('Buat record <code>Produk(String nama, int harga)</code> yang menolak harga negatif, lalu cetak objeknya dan bandingkan dua record yang isinya sama.', 'Compact constructor: record Produk(...) { Produk { if (...) throw ...; } }. equals record membandingkan isi.',
     'record Produk(String nama, int harga) {\n    Produk {\n        if (harga < 0) throw new IllegalArgumentException("harga negatif");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Produk a = new Produk("Kopi", 18000);\n        Produk b = new Produk("Kopi", 18000);\n        System.out.println(a);\n        System.out.println(a.equals(b));\n        System.out.println(a.harga());\n    }\n}', 'Produk[nama=Kopi, harga=18000]\ntrue\n18000'),
],
'Kelas bersarang & initializer block': [
  Jv('Buat kelas <code>Keranjang</code> dengan static nested class <code>Item</code>, lalu hitung total dua item.', 'Static nested class tidak butuh objek luar: new Keranjang.Item(...).',
     'import java.util.ArrayList;\nimport java.util.List;\n\nclass Keranjang {\n    static class Item {\n        final String nama; final int harga, qty;\n        Item(String n, int h, int q) { nama = n; harga = h; qty = q; }\n    }\n    private final List<Item> isi = new ArrayList<>();\n    void tambah(Item i) { isi.add(i); }\n    int total() {\n        int t = 0;\n        for (Item i : isi) t += i.harga * i.qty;\n        return t;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Keranjang k = new Keranjang();\n        k.tambah(new Keranjang.Item("Kopi", 18000, 2));\n        k.tambah(new Keranjang.Item("Roti", 12000, 1));\n        System.out.println(k.total());\n    }\n}', '48000'),
  Jv('Tebak urutan cetak: kelas dengan static block, instance block, dan konstruktor, lalu dibuat dua objek.', 'Static block jalan sekali saat kelas dimuat. Instance block jalan sebelum isi konstruktor, setiap objek dibuat.',
     'class Demo {\n    static { System.out.println("static"); }\n    { System.out.println("instance"); }\n    Demo() { System.out.println("konstruktor"); }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        new Demo();\n        new Demo();\n    }\n}', 'static\ninstance\nkonstruktor\ninstance\nkonstruktor'),
],
'Array lawan ArrayList': [
  Jv('Simpan nama tamu di ArrayList, tambahkan "Dewi" di posisi pertama, hapus "Sandi", lalu cetak jumlah dan isinya.', 'add(index, nilai), remove(Object), size().',
     'import java.util.ArrayList;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<String> tamu = new ArrayList<>(List.of("Rina", "Sandi", "Tari"));\n        tamu.add(0, "Dewi");\n        tamu.remove("Sandi");\n        System.out.println(tamu.size());\n        System.out.println(tamu);\n    }\n}', '3\n[Dewi, Rina, Tari]'),
  Jv('Hati-hati dengan <code>remove</code> pada <code>ArrayList&lt;Integer&gt;</code>. Apa beda <code>remove(1)</code> dan <code>remove(Integer.valueOf(1))</code>?', 'remove(int) menghapus berdasarkan indeks, remove(Object) berdasarkan nilai.',
     'import java.util.ArrayList;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<Integer> a = new ArrayList<>(List.of(5, 1, 9));\n        a.remove(1);                     // indeks 1 (nilai 1)\n        System.out.println(a);\n        List<Integer> b = new ArrayList<>(List.of(5, 1, 9));\n        b.remove(Integer.valueOf(9));    // nilai 9\n        System.out.println(b);\n    }\n}', '[5, 9]\n[5, 1]'),
],
'Deque & Iterator': [
  Jv('Pakai ArrayDeque sebagai stack untuk membalik kata "JAVA", lalu sebagai antrean (queue) untuk melayani pelanggan A, B, C.', 'Stack: push/pop. Queue: offer/poll.',
     'import java.util.ArrayDeque;\nimport java.util.Deque;\n\npublic class Main {\n    public static void main(String[] args) {\n        Deque<Character> stack = new ArrayDeque<>();\n        for (char c : "JAVA".toCharArray()) stack.push(c);\n        StringBuilder sb = new StringBuilder();\n        while (!stack.isEmpty()) sb.append(stack.pop());\n        System.out.println(sb);\n\n        Deque<String> antre = new ArrayDeque<>();\n        antre.offer("A"); antre.offer("B"); antre.offer("C");\n        System.out.println(antre.poll() + " dilayani, sisa " + antre);\n    }\n}', 'AVAJ\nA dilayani, sisa [B, C]'),
  Jv('Hapus semua angka genap dari list sambil melakukan iterasi tanpa ConcurrentModificationException.', 'Pakai Iterator dan it.remove(), atau removeIf.',
     'import java.util.ArrayList;\nimport java.util.Iterator;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<Integer> a = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6));\n        Iterator<Integer> it = a.iterator();\n        while (it.hasNext()) {\n            if (it.next() % 2 == 0) it.remove();\n        }\n        System.out.println(a);\n    }\n}', '[1, 3, 5]'),
],
'Generics: kode yang aman tipe': [
  Jv('Buat kelas generik <code>Pasangan&lt;A, B&gt;</code> dan method generik <code>terbesar</code> yang menerima list bertipe <code>T extends Comparable&lt;T&gt;</code>.', 'Bounded type: &lt;T extends Comparable&lt;T&gt;&gt;. Bandingkan dengan compareTo.',
     'import java.util.List;\n\nrecord Pasangan<A, B>(A kiri, B kanan) {}\n\npublic class Main {\n    static <T extends Comparable<T>> T terbesar(List<T> data) {\n        T maks = data.get(0);\n        for (T x : data) if (x.compareTo(maks) > 0) maks = x;\n        return maks;\n    }\n\n    public static void main(String[] args) {\n        Pasangan<String, Integer> p = new Pasangan<>("Kopi", 18000);\n        System.out.println(p.kiri() + " " + p.kanan());\n        System.out.println(terbesar(List.of(4, 19, 7)));\n        System.out.println(terbesar(List.of("apel", "jeruk", "mangga")));\n    }\n}', 'Kopi 18000\n19\nmangga'),
  Jv('Tulis method yang menjumlahkan list angka apa pun (Integer, Double) memakai wildcard.', '<code>List&lt;? extends Number&gt;</code> lalu panggil doubleValue().',
     'import java.util.List;\n\npublic class Main {\n    static double jumlah(List<? extends Number> data) {\n        double t = 0;\n        for (Number n : data) t += n.doubleValue();\n        return t;\n    }\n\n    public static void main(String[] args) {\n        System.out.println(jumlah(List.of(1, 2, 3)));\n        System.out.println(jumlah(List.of(1.5, 2.5)));\n    }\n}', '6.0\n4.0'),
],
'Checked, unchecked & exception buatan sendiri': [
  Jv('Buat exception sendiri <code>SaldoKurangException</code> (checked). Method tarik() melemparnya jika saldo tidak cukup; tangkap di main.', 'extends Exception (checked) dan wajib dideklarasikan dengan throws.',
     'class SaldoKurangException extends Exception {\n    SaldoKurangException(String pesan) { super(pesan); }\n}\n\npublic class Main {\n    static long saldo = 100_000;\n\n    static void tarik(long n) throws SaldoKurangException {\n        if (n > saldo) throw new SaldoKurangException("Saldo kurang " + (n - saldo));\n        saldo -= n;\n    }\n\n    public static void main(String[] args) {\n        try {\n            tarik(30_000);\n            tarik(90_000);\n        } catch (SaldoKurangException e) {\n            System.out.println(e.getMessage());\n        } finally {\n            System.out.println("Saldo " + saldo);\n        }\n    }\n}', 'Saldo kurang 20000\nSaldo 70000'),
  Jv('Ubah teks "12a" menjadi angka dengan aman: jika gagal, pakai 0 dan cetak pesan.', 'Integer.parseInt melempar NumberFormatException (unchecked).',
     'public class Main {\n    static int keAngka(String s) {\n        try {\n            return Integer.parseInt(s);\n        } catch (NumberFormatException e) {\n            System.out.println("Bukan angka: " + s);\n            return 0;\n        }\n    }\n\n    public static void main(String[] args) {\n        System.out.println(keAngka("42"));\n        System.out.println(keAngka("12a"));\n    }\n}', '42\nBukan angka: 12a\n0'),
],
'Anotasi': [
  Jv('Apa gunanya <code>@Override</code>? Tunjukkan kesalahan yang ditangkapnya.', 'Tanpa @Override, salah ketik nama method membuat method baru diam-diam.',
     'class Hewan { String suara() { return "..."; } }\n\nclass Anjing extends Hewan {\n    // @Override String suaraa() { ... }  -> error kompilasi: method tidak meng-override\n    @Override\n    String suara() { return "Guk"; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(new Anjing().suara());\n    }\n}', 'Guk'),
  Jv('Buat anotasi sendiri <code>@Wajib</code> untuk field, lalu baca dengan reflection field mana saja yang ditandai.', '@Retention(RetentionPolicy.RUNTIME) agar anotasi bisa dibaca saat program berjalan.',
     'import java.lang.annotation.*;\nimport java.lang.reflect.Field;\n\n@Retention(RetentionPolicy.RUNTIME)\n@Target(ElementType.FIELD)\n@interface Wajib {}\n\nclass Formulir {\n    @Wajib String nama;\n    String catatan;\n    @Wajib String email;\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        for (Field f : Formulir.class.getDeclaredFields()) {\n            if (f.isAnnotationPresent(Wajib.class)) System.out.println(f.getName());\n        }\n    }\n}', 'nama\nemail'),
],
'Functional interface & komposisi fungsi': [
  Jv('Buat <code>Function&lt;Integer, Integer&gt;</code> diskon10 dan tambahOngkir (+10.000), lalu gabungkan dengan andThen dan compose untuk harga 100.000.', 'f.andThen(g) = g(f(x)); f.compose(g) = f(g(x)).',
     'import java.util.function.Function;\n\npublic class Main {\n    public static void main(String[] args) {\n        Function<Integer, Integer> diskon10 = h -> h * 90 / 100;\n        Function<Integer, Integer> ongkir = h -> h + 10_000;\n        System.out.println(diskon10.andThen(ongkir).apply(100_000));\n        System.out.println(diskon10.compose(ongkir).apply(100_000));\n    }\n}', '100000\n99000'),
  Jv('Pakai <code>Predicate</code> untuk memilih nama yang diawali "R" dan panjangnya lebih dari 3, memakai and().', 'Predicate&lt;String&gt; p = s -> ...; p.and(q).test(x)',
     'import java.util.List;\nimport java.util.function.Predicate;\n\npublic class Main {\n    public static void main(String[] args) {\n        Predicate<String> awalR = s -> s.startsWith("R");\n        Predicate<String> panjang = s -> s.length() > 3;\n        for (String n : List.of("Rina", "Rio", "Sandi", "Rahmat")) {\n            if (awalR.and(panjang).test(n)) System.out.println(n);\n        }\n    }\n}', 'Rina\nRahmat'),
],
'Stream API & method chaining': [
  Jv('Dari daftar harga <code>[18000, 25000, 9000, 40000, 12000]</code>, ambil yang di atas 10.000, beri diskon 10%, urutkan, lalu jumlahkan.', 'filter, map, sorted, lalu mapToInt(...).sum() atau collect.',
     'import java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<Integer> harga = List.of(18000, 25000, 9000, 40000, 12000);\n        List<Integer> hasil = harga.stream()\n            .filter(h -> h > 10_000)\n            .map(h -> h * 90 / 100)\n            .sorted()\n            .toList();\n        System.out.println(hasil);\n        System.out.println(hasil.stream().mapToInt(Integer::intValue).sum());\n    }\n}', '[10800, 16200, 22500, 36000]\n85500'),
  Jv('Kelompokkan nama berdasarkan huruf awalnya dan hitung jumlahnya dengan Collectors.groupingBy.', 'groupingBy(n -> n.charAt(0), TreeMap::new, Collectors.counting()) agar urut.',
     'import java.util.List;\nimport java.util.TreeMap;\nimport java.util.stream.Collectors;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<String> nama = List.of("Rina", "Sandi", "Rio", "Tari", "Santi");\n        var hasil = nama.stream().collect(\n            Collectors.groupingBy(n -> n.charAt(0), TreeMap::new, Collectors.counting()));\n        System.out.println(hasil);\n    }\n}', '{R=2, S=2, T=1}'),
],
'Optional: mengganti null dengan aman': [
  Jv('Method <code>cariEmail(String nama)</code> mengembalikan Optional. Cetak email Rina dalam huruf besar, dan "tidak ada" untuk Budi.', 'Optional.ofNullable(map.get(nama)), lalu map dan orElse.',
     'import java.util.Map;\nimport java.util.Optional;\n\npublic class Main {\n    static final Map<String, String> EMAIL = Map.of("Rina", "rina@mail.id");\n\n    static Optional<String> cariEmail(String nama) {\n        return Optional.ofNullable(EMAIL.get(nama));\n    }\n\n    public static void main(String[] args) {\n        System.out.println(cariEmail("Rina").map(String::toUpperCase).orElse("tidak ada"));\n        System.out.println(cariEmail("Budi").map(String::toUpperCase).orElse("tidak ada"));\n    }\n}', 'RINA@MAIL.ID\ntidak ada'),
  Tx('Sebutkan tiga kebiasaan buruk dengan Optional.', 'Ingat: Optional untuk nilai kembalian yang mungkin kosong.',
     '1. Memanggil get() tanpa memeriksa: sama saja dengan risiko null.\n2. Memakai Optional untuk field kelas atau parameter method.\n3. Mengembalikan null dari method yang tipenya Optional.\nLebih baik: orElse, orElseGet, orElseThrow, map, ifPresent.'),
],
'Package & modul': [
  Bs('Susun folder untuk kelas <code>id.ruangkode.toko.Produk</code> dan <code>id.ruangkode.App</code>, lalu kompilasi dan jalankan dari terminal.', 'Nama package mengikuti folder. Kompilasi ke folder out dengan -d.',
     '# struktur\n# src/id/ruangkode/App.java          -> package id.ruangkode;\n# src/id/ruangkode/toko/Produk.java   -> package id.ruangkode.toko;\n\njavac -d out src/id/ruangkode/App.java src/id/ruangkode/toko/Produk.java\njava -cp out id.ruangkode.App'),
  Jv('Tulis <code>module-info.java</code> untuk modul <code>id.ruangkode.toko</code> yang memakai java.sql dan hanya membuka paket <code>id.ruangkode.toko.api</code>.', 'requires untuk dependensi, exports untuk paket yang boleh dipakai modul lain.',
     'module id.ruangkode.toko {\n    requires java.sql;\n    exports id.ruangkode.toko.api;\n}'),
],
'File modern dengan java.nio': [
  Jv('Tulis tiga baris ke <code>catatan.txt</code>, baca kembali, lalu cetak jumlah baris dan baris yang mengandung "kopi".', 'Files.write / Files.writeString dan Files.readAllLines dengan Path.of.',
     'import java.nio.file.Files;\nimport java.nio.file.Path;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        Path p = Path.of("catatan.txt");\n        Files.write(p, List.of("beli kopi", "bayar listrik", "kopi untuk kantor"));\n        List<String> baris = Files.readAllLines(p);\n        System.out.println(baris.size());\n        baris.stream().filter(b -> b.contains("kopi")).forEach(System.out::println);\n    }\n}', '3\nbeli kopi\nkopi untuk kantor'),
  Jv('Hitung jumlah kata dalam file besar tanpa memuat semuanya ke memori.', 'Files.lines mengembalikan Stream yang membaca bertahap. Tutup dengan try-with-resources.',
     'import java.nio.file.Files;\nimport java.nio.file.Path;\nimport java.util.stream.Stream;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        Files.writeString(Path.of("data.txt"), "satu dua tiga\\nempat lima\\n");\n        try (Stream<String> baris = Files.lines(Path.of("data.txt"))) {\n            long kata = baris.mapToLong(b -> b.split("\\\\s+").length).sum();\n            System.out.println(kata);\n        }\n    }\n}', '5'),
],
'Tanggal & waktu (java.time)': [
  Jv('Hitung umur orang yang lahir 17 Agustus 2005 pada tanggal 2 November 2026, dan hari apa dia lahir.', 'Period.between(lahir, hariIni).getYears(), lahir.getDayOfWeek().',
     'import java.time.LocalDate;\nimport java.time.Period;\n\npublic class Main {\n    public static void main(String[] args) {\n        LocalDate lahir = LocalDate.of(2005, 8, 17);\n        LocalDate hariIni = LocalDate.of(2026, 11, 2);\n        System.out.println(Period.between(lahir, hariIni).getYears());\n        System.out.println(lahir.getDayOfWeek());\n    }\n}', '21\nWEDNESDAY'),
  Jv('Format tanggal jatuh tempo 30 hari setelah 15 Oktober 2026 menjadi "14/11/2026", dan hitung selisih hari antara dua tanggal.', 'plusDays, DateTimeFormatter.ofPattern("dd/MM/yyyy"), ChronoUnit.DAYS.between.',
     'import java.time.LocalDate;\nimport java.time.format.DateTimeFormatter;\nimport java.time.temporal.ChronoUnit;\n\npublic class Main {\n    public static void main(String[] args) {\n        LocalDate pinjam = LocalDate.of(2026, 10, 15);\n        LocalDate tempo = pinjam.plusDays(30);\n        System.out.println(tempo.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));\n        System.out.println(ChronoUnit.DAYS.between(pinjam, LocalDate.of(2026, 12, 25)));\n    }\n}', '14/11/2026\n71'),
],
'Regular expression': [
  Jv('Validasi nomor HP Indonesia: diawali 08 atau +628, lalu 8 sampai 11 digit. Uji "081234567890", "+62812345678", "0712345".', 'Pola: ^(\\+62|0)8\\d{8,11}$ dan String.matches.',
     'public class Main {\n    public static void main(String[] args) {\n        String pola = "^(\\\\+62|0)8\\\\d{8,11}$";\n        for (String hp : new String[]{"081234567890", "+62812345678", "0712345"}) {\n            System.out.println(hp + " " + hp.matches(pola));\n        }\n    }\n}', '081234567890 true\n+62812345678 true\n0712345 false'),
  Jv('Ambil semua nominal rupiah dari teks "Kopi Rp18.000, roti Rp12.500" lalu jumlahkan.', 'Pattern.compile("Rp([\\d.]+)"), Matcher.find(), group(1), hapus titik.',
     'import java.util.regex.Matcher;\nimport java.util.regex.Pattern;\n\npublic class Main {\n    public static void main(String[] args) {\n        Matcher m = Pattern.compile("Rp([\\\\d.]+)").matcher("Kopi Rp18.000, roti Rp12.500");\n        int total = 0;\n        while (m.find()) total += Integer.parseInt(m.group(1).replace(".", ""));\n        System.out.println(total);\n    }\n}', '30500'),
],
'Jaringan & kriptografi dasar': [
  Jv('Hitung hash SHA-256 dari teks "ruangkode" dan cetak dalam heksadesimal.', 'MessageDigest.getInstance("SHA-256"), lalu HexFormat.of().formatHex (Java 17+).',
     'import java.nio.charset.StandardCharsets;\nimport java.security.MessageDigest;\nimport java.util.HexFormat;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        MessageDigest md = MessageDigest.getInstance("SHA-256");\n        byte[] h = md.digest("ruangkode".getBytes(StandardCharsets.UTF_8));\n        System.out.println(HexFormat.of().formatHex(h).length());\n    }\n}', '64'),
  Jv('Tulis permintaan GET ke <code>https://api.contoh.id/produk</code> dengan HttpClient dan cetak kode status serta isi respons.', 'HttpClient.newHttpClient(), HttpRequest.newBuilder(URI.create(...)), BodyHandlers.ofString().',
     'import java.net.URI;\nimport java.net.http.HttpClient;\nimport java.net.http.HttpRequest;\nimport java.net.http.HttpResponse;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        HttpClient client = HttpClient.newHttpClient();\n        HttpRequest req = HttpRequest.newBuilder(URI.create("https://api.contoh.id/produk"))\n            .header("Accept", "application/json")\n            .GET().build();\n        HttpResponse<String> res = client.send(req, HttpResponse.BodyHandlers.ofString());\n        System.out.println(res.statusCode());\n        System.out.println(res.body());\n    }\n}'),
],
'Thread & race condition': [
  Jv('Dua thread masing-masing menambah penghitung 10.000 kali. Perbaiki agar hasilnya selalu 20.000.', 'count++ bukan operasi atomik. Pakai synchronized atau AtomicInteger, dan join() sebelum mencetak.',
     'import java.util.concurrent.atomic.AtomicInteger;\n\npublic class Main {\n    public static void main(String[] args) throws InterruptedException {\n        AtomicInteger hitung = new AtomicInteger();\n        Runnable kerja = () -> { for (int i = 0; i < 10_000; i++) hitung.incrementAndGet(); };\n        Thread a = new Thread(kerja), b = new Thread(kerja);\n        a.start(); b.start();\n        a.join(); b.join();\n        System.out.println(hitung.get());\n    }\n}', '20000'),
  Tx('Jelaskan apa itu race condition dengan contoh dua kasir yang mengurangi stok yang sama.', 'Baca, ubah, tulis bisa saling menyela.',
     'Stok = 1.\nKasir A membaca stok 1, kasir B juga membaca stok 1.\nA menulis stok 0, B juga menulis stok 0.\nDua barang terjual padahal stok hanya 1.\nHasil bergantung pada urutan waktu thread: itulah race condition.\nSolusinya: kunci bagian kritis (synchronized/Lock) atau operasi atomik.'),
],
'ExecutorService & virtual thread': [
  Jv('Jalankan tiga tugas penghitungan kuadrat (2, 3, 4) memakai ExecutorService dan kumpulkan hasilnya dengan Future.', 'submit mengembalikan Future; future.get() menunggu hasil.',
     'import java.util.ArrayList;\nimport java.util.List;\nimport java.util.concurrent.*;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        try (ExecutorService ex = Executors.newFixedThreadPool(3)) {\n            List<Future<Integer>> hasil = new ArrayList<>();\n            for (int n : new int[]{2, 3, 4}) hasil.add(ex.submit(() -> n * n));\n            for (Future<Integer> f : hasil) System.out.println(f.get());\n        }\n    }\n}', '4\n9\n16'),
  Jv('Buat 10.000 virtual thread yang masing-masing tidur 10 ms, lalu hitung berapa yang selesai.', 'Executors.newVirtualThreadPerTaskExecutor() (Java 21+). try-with-resources menunggu semua selesai.',
     'import java.util.concurrent.Executors;\nimport java.util.concurrent.atomic.AtomicInteger;\n\npublic class Main {\n    public static void main(String[] args) {\n        AtomicInteger selesai = new AtomicInteger();\n        try (var ex = Executors.newVirtualThreadPerTaskExecutor()) {\n            for (int i = 0; i < 10_000; i++) {\n                ex.submit(() -> {\n                    Thread.sleep(10);\n                    return selesai.incrementAndGet();\n                });\n            }\n        }\n        System.out.println(selesai.get());\n    }\n}', '10000'),
],
'volatile & Java Memory Model': [
  Jv('Thread pekerja berhenti ketika flag <code>jalan</code> menjadi false. Kenapa flag perlu <code>volatile</code>? Tulis kodenya.', 'Tanpa volatile, thread lain bisa terus membaca salinan lama dari cache.',
     'public class Main {\n    static volatile boolean jalan = true;\n\n    public static void main(String[] args) throws InterruptedException {\n        Thread pekerja = new Thread(() -> {\n            long n = 0;\n            while (jalan) n++;\n            System.out.println("berhenti");\n        });\n        pekerja.start();\n        Thread.sleep(100);\n        jalan = false;      // langsung terlihat oleh pekerja\n        pekerja.join();\n    }\n}', 'berhenti'),
  Tx('Apakah <code>volatile int hitung; hitung++</code> aman dari race condition? Jelaskan.', 'volatile menjamin visibilitas, bukan atomisitas.',
     'Tidak aman. hitung++ terdiri dari baca, tambah, tulis.\nvolatile hanya menjamin setiap thread melihat nilai terbaru,\ntetapi dua thread tetap bisa membaca nilai yang sama lalu menulis hasil yang sama.\nPakai AtomicInteger atau synchronized.'),
],
'Build tool: Maven, Gradle, Bazel': [
  Xm('Tambahkan dependensi JUnit Jupiter 5.11.0 untuk test di <code>pom.xml</code>.', 'Di dalam &lt;dependencies&gt;, scope test.',
     '<dependencies>\n  <dependency>\n    <groupId>org.junit.jupiter</groupId>\n    <artifactId>junit-jupiter</artifactId>\n    <version>5.11.0</version>\n    <scope>test</scope>\n  </dependency>\n</dependencies>'),
  Bs('Tulis perintah Maven dan Gradle untuk menjalankan test dan membuat file JAR.', 'Maven: mvn test, mvn package. Gradle wrapper: ./gradlew test, ./gradlew build.',
     '# Maven\nmvn test\nmvn package          # hasil di target/*.jar\n\n# Gradle\n./gradlew test\n./gradlew build      # hasil di build/libs/*.jar'),
],
'Logging: SLF4J, Logback, Log4j2': [
  Jv('Tulis log memakai SLF4J dengan placeholder untuk login berhasil (info) dan gagal (warn). Kenapa placeholder lebih baik dari penggabungan string?', 'log.info("User {} login", nama). Placeholder hanya dirangkai jika level aktif.',
     'import org.slf4j.Logger;\nimport org.slf4j.LoggerFactory;\n\npublic class Login {\n    private static final Logger log = LoggerFactory.getLogger(Login.class);\n\n    void masuk(String user, boolean ok) {\n        if (ok) log.info("User {} berhasil login", user);\n        else log.warn("Login gagal untuk {}", user);\n        // jangan: log.debug("data " + objekBesar)  -> string tetap dibuat walau debug mati\n    }\n}'),
  Tx('Urutkan level log dari paling rinci ke paling penting, dan sebutkan kapan memakai masing-masing.', 'TRACE, DEBUG, INFO, WARN, ERROR.',
     'TRACE : jejak sangat rinci (masuk/keluar method)\nDEBUG : info untuk mencari bug saat pengembangan\nINFO  : peristiwa normal penting (server menyala, pesanan dibuat)\nWARN  : hal aneh tapi program tetap jalan (retry, konfigurasi bawaan)\nERROR : kegagalan yang butuh perhatian (exception tidak tertangani)'),
],
'Unit test dengan JUnit 5': [
  Jv('Tulis test JUnit 5 untuk method <code>Diskon.hitung(harga, persen)</code>: kasus normal, persen 0, dan persen lebih dari 100 harus melempar exception.', '@Test, assertEquals, assertThrows.',
     'import org.junit.jupiter.api.Test;\nimport static org.junit.jupiter.api.Assertions.*;\n\nclass DiskonTest {\n    @Test\n    void diskonNormal() {\n        assertEquals(90_000, Diskon.hitung(100_000, 10));\n    }\n\n    @Test\n    void tanpaDiskon() {\n        assertEquals(50_000, Diskon.hitung(50_000, 0));\n    }\n\n    @Test\n    void persenTidakValid() {\n        assertThrows(IllegalArgumentException.class, () -> Diskon.hitung(10_000, 120));\n    }\n}'),
  Jv('Ubah tiga test kasus angka genap menjadi satu parameterized test.', '@ParameterizedTest dengan @ValueSource(ints = {...}).',
     'import org.junit.jupiter.params.ParameterizedTest;\nimport org.junit.jupiter.params.provider.ValueSource;\nimport static org.junit.jupiter.api.Assertions.assertTrue;\n\nclass GenapTest {\n    @ParameterizedTest\n    @ValueSource(ints = {2, 4, 100})\n    void semuaGenap(int n) {\n        assertTrue(Angka.genap(n));\n    }\n}'),
],
'Mocking & jenis tes lain': [
  Jv('Uji <code>LayananPesanan</code> yang memanggil <code>PengirimEmail</code> tanpa benar-benar mengirim email, memakai Mockito.', 'mock(), when(...).thenReturn(...), verify(...).',
     'import org.junit.jupiter.api.Test;\nimport static org.mockito.Mockito.*;\n\nclass LayananPesananTest {\n    @Test\n    void kirimEmailSetelahPesan() {\n        PengirimEmail email = mock(PengirimEmail.class);\n        LayananPesanan layanan = new LayananPesanan(email);\n\n        layanan.pesan("rina@mail.id", "Kopi");\n\n        verify(email).kirim("rina@mail.id", "Pesanan Kopi diterima");\n    }\n}'),
  Tx('Bedakan unit test, integration test, dan end-to-end test, beserta contohnya di aplikasi toko.', 'Lihat cakupan: satu kelas, beberapa komponen nyata, atau seluruh sistem lewat UI/API.',
     'Unit test        : satu kelas terisolasi, misal hitung total keranjang.\nIntegration test : beberapa bagian nyata, misal repository + database Testcontainers.\nEnd-to-end test  : alur lengkap dari luar, misal pengguna checkout lewat browser.\nSemakin ke atas semakin lambat dan mahal, jadi jumlahnya makin sedikit.'),
],
'JDBC: Java bicara dengan database': [
  Jv('Cari produk berdasarkan kategori dengan PreparedStatement (bukan menggabungkan string) dan cetak nama serta harganya.', 'Placeholder ? mencegah SQL injection. setString(1, ...), executeQuery, while (rs.next()).',
     'import java.sql.*;\n\npublic class Main {\n    public static void main(String[] args) throws SQLException {\n        String sql = "SELECT nama, harga FROM produk WHERE kategori = ?";\n        try (Connection c = DriverManager.getConnection("jdbc:postgresql://localhost/toko", "app", "rahasia");\n             PreparedStatement ps = c.prepareStatement(sql)) {\n            ps.setString(1, "Minuman");\n            try (ResultSet rs = ps.executeQuery()) {\n                while (rs.next()) {\n                    System.out.println(rs.getString("nama") + " " + rs.getInt("harga"));\n                }\n            }\n        }\n    }\n}'),
  Jv('Pindahkan saldo antar dua rekening dalam satu transaksi: jika salah satu UPDATE gagal, batalkan semuanya.', 'setAutoCommit(false), commit(), rollback() di catch.',
     'static void transfer(Connection c, int dari, int ke, long n) throws SQLException {\n    c.setAutoCommit(false);\n    try (PreparedStatement kurang = c.prepareStatement("UPDATE rekening SET saldo = saldo - ? WHERE id = ?");\n         PreparedStatement tambah = c.prepareStatement("UPDATE rekening SET saldo = saldo + ? WHERE id = ?")) {\n        kurang.setLong(1, n); kurang.setInt(2, dari); kurang.executeUpdate();\n        tambah.setLong(1, n); tambah.setInt(2, ke);   tambah.executeUpdate();\n        c.commit();\n    } catch (SQLException e) {\n        c.rollback();\n        throw e;\n    } finally {\n        c.setAutoCommit(true);\n    }\n}'),
],
'ORM: Hibernate, Spring Data JPA, Ebean': [
  Jv('Buat entity JPA <code>Produk</code> (id otomatis, nama wajib, harga) dan repository Spring Data dengan method mencari produk yang lebih murah dari harga tertentu.', '@Entity, @Id, @GeneratedValue, interface extends JpaRepository dan nama method findByHargaLessThan.',
     'import jakarta.persistence.*;\nimport java.util.List;\nimport org.springframework.data.jpa.repository.JpaRepository;\n\n@Entity\npublic class Produk {\n    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)\n    private Long id;\n    @Column(nullable = false)\n    private String nama;\n    private int harga;\n    // getter dan setter\n}\n\ninterface ProdukRepository extends JpaRepository<Produk, Long> {\n    List<Produk> findByHargaLessThan(int batas);\n}'),
  Tx('Apa itu masalah N+1 query pada ORM, dan bagaimana mengatasinya?', 'Bayangkan 100 pesanan yang masing-masing memuat pelanggannya.',
     'Masalah: 1 query mengambil 100 pesanan, lalu ORM menjalankan 100 query lagi\nuntuk memuat pelanggan tiap pesanan (total 101 query).\nSolusi: JOIN FETCH di JPQL, @EntityGraph, atau batch fetching,\nsehingga data terkait diambil sekaligus dalam 1-2 query.'),
],
'Spring Boot & dependency injection': [
  Jv('Buat REST controller Spring Boot dengan endpoint <code>GET /produk/{id}</code> yang memakai service lewat constructor injection.', '@RestController, @GetMapping, @PathVariable. Constructor injection tidak perlu @Autowired jika hanya satu konstruktor.',
     'import org.springframework.web.bind.annotation.*;\n\n@RestController\n@RequestMapping("/produk")\npublic class ProdukController {\n    private final ProdukService service;\n\n    public ProdukController(ProdukService service) {   // constructor injection\n        this.service = service;\n    }\n\n    @GetMapping("/{id}")\n    public Produk satu(@PathVariable long id) {\n        return service.cari(id);\n    }\n}'),
  Tx('Kenapa constructor injection lebih disarankan daripada field injection (@Autowired di field)?', 'Pikirkan tentang final, test, dan dependensi yang wajib.',
     '1. Field bisa final, jadi objek tidak berubah setelah dibuat.\n2. Mudah dites: cukup new ProdukController(serviceTiruan) tanpa Spring.\n3. Dependensi wajib terlihat jelas di konstruktor.\n4. Terlalu banyak parameter memberi tanda kelas memikul terlalu banyak tugas.'),
],
'Framework web lain: Quarkus, Javalin, Play': [
  Jv('Buat server Javalin kecil dengan endpoint <code>GET /halo/{nama}</code> yang membalas "Halo, Rina!".', 'Javalin.create().get(path, ctx -> ...).start(7070); ctx.pathParam("nama").',
     'import io.javalin.Javalin;\n\npublic class App {\n    public static void main(String[] args) {\n        Javalin.create()\n            .get("/halo/{nama}", ctx -> ctx.result("Halo, " + ctx.pathParam("nama") + "!"))\n            .start(7070);\n    }\n}\n// GET http://localhost:7070/halo/Rina  ->  Halo, Rina!'),
  Tx('Pilih framework yang cocok: (a) API kecil untuk belajar, (b) layanan cloud native yang harus menyala sangat cepat, (c) aplikasi perusahaan besar dengan banyak integrasi.', 'Bandingkan ukuran, waktu start, dan ekosistem.',
     '(a) Javalin: ringan, kode sedikit, mudah dipahami.\n(b) Quarkus: start cepat dan hemat memori, bisa dikompilasi native (GraalVM).\n(c) Spring Boot: ekosistem paling lengkap (security, data, cloud) dan banyak dipakai industri.'),
],
'Dokumentasi dengan Javadoc': [
  Jv('Tulis Javadoc lengkap untuk method <code>hitungCicilan(long pokok, double bungaTahunan, int bulan)</code>.', '@param untuk tiap parameter, @return, @throws.',
     '/**\n * Menghitung cicilan bulanan dengan bunga flat.\n *\n * @param pokok        jumlah pinjaman dalam rupiah, harus lebih dari 0\n * @param bungaTahunan bunga per tahun dalam persen, misalnya 12.0\n * @param bulan        lama cicilan dalam bulan\n * @return besar cicilan per bulan dalam rupiah\n * @throws IllegalArgumentException jika pokok atau bulan tidak positif\n */\npublic static long hitungCicilan(long pokok, double bungaTahunan, int bulan) {\n    if (pokok <= 0 || bulan <= 0) throw new IllegalArgumentException("tidak valid");\n    double bunga = pokok * bungaTahunan / 100 * bulan / 12;\n    return Math.round((pokok + bunga) / bulan);\n}'),
  Bs('Buat dokumentasi HTML dari folder src ke folder docs.', 'Perintah javadoc dengan -d untuk folder tujuan.',
     'javadoc -d docs -sourcepath src -subpackages id.ruangkode\n# buka docs/index.html di browser'),
],
}

SOAL = {'JAVA_MODULES': JAVA}
