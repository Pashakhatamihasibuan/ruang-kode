/* ===================== PERBAIKI KODE YANG ERROR =====================
   Dibuat oleh tools/gen/bugs.py: satu kesalahan khas pemula ditanam di contoh kode, lalu kode
   rusak itu dijalankan dan pesan error aslinya disimpan. l.bug = {code, err, line, kind, why}. */
(()=>{
const BUGS={
"java:Tipe data primitif & type casting": {
"code": "public class Casting {\n    public static void main(String[] args) {\n        int jumlah = 7\n        double rata = jumlah;          // widening: otomatis\n        double harga = 9.99;\n        int dibulatkan = (int) harga;  // narrowing: buang pecahan\n        long besar = 3_000_000_000L;\n        int kecil = (int) besar;       // nilai meluap (overflow)\n        char huruf = 'A';\n        int kode = huruf;              // char -> int: kode Unicode\n\n        System.out.println(rata);\n        System.out.println(dibulatkan);\n        System.out.println(kecil);\n        System.out.println(kode);\n        System.out.println(7 / 2);\n        System.out.println((double) 7 / 2);\n    }\n}",
"err": "Casting.java:3: error: ';' expected\n        int jumlah = 7\n                      ^",
"line": 3,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:Kelas Math & operasi angka": {
"code": "public class Hitung {\n    public static void main(String[] args) {\n        System.out.println(Math.pow(2, 10));\n        System.out.println(Math.sqrt(144));\n        System.out.println(Math.abs(-25));\n        System.out.println(Math.max(17, 42));\n        System.out.println(Math.round(2.5));\n        System.out.println(Math.floor(2.9));\n        System.out.println(Math.ceil(2.1));\n        System.out.println(0.1 + 0.2);\n        int dadu = (int) (Math.random() * 6) + 1;\n        System.out.println(ddu >= 1 && dadu <= 6);\n    }\n}",
"err": "Hitung.java:12: error: cannot find symbol\n        System.out.println(ddu >= 1 && dadu <= 6);\n                           ^",
"line": 12,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"java:Scope: di mana variabel hidup": {
"code": "public class Scope {\n    static int total = 0;               // field: hidup selama program\n\n    static void tambah(int n) {          // n: parameter, lokal di method\n        int dobel = n * 2;               // lokal\n        total += dobel;\n    }\n\n    public static void main(String[] args) {\n        for (int i = 1; i <= 3; i++) {   // i hanya hidup di dalam for\n            tambah(i);\n        }\n        // System.out.println(i);        // error: cannot find symbol\n        System.out.println(total;\n        {\n            int sementara = 99;          // blok bebas punya scope sendiri\n            System.out.println(sementara);\n        }\n    }\n}",
"err": "Scope.java:14: error: ')' or ',' expected\n        System.out.println(total;\n                                ^",
"line": 14,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Method String & StringBuilder": {
"code": "public class Teks {\n    public static void main(String[] args) {\n        String nama = \"  Budi Santoso  \"\n        String rapi = nama.trim();\n        System.out.println(rapi.toUpperCase());\n        System.out.println(rapi.length());\n        System.out.println(rapi.indexOf(\"Santoso\"));\n        System.out.println(rapi.substring(0, 4));\n        System.out.println(rapi.replace(\"Budi\", \"Bu\"));\n        System.out.println(rapi.contains(\"ant\"));\n\n        String a = \"halo\";\n        String b = new String(\"halo\");\n        System.out.println(a == b);\n        System.out.println(a.equals(b));\n\n        StringBuilder sb = new StringBuilder();\n        for (int i = 1; i <= 5; i++) {\n            sb.append(i).append(i < 5 ? \"-\" : \"\");\n        }\n        System.out.println(sb.toString());\n        System.out.println(String.join(\", \", \"Java\", \"Kotlin\", \"SQL\"));\n    }\n}",
"err": "Teks.java:3: error: ';' expected\n        String nama = \"  Budi Santoso  \"\n                                        ^",
"line": 3,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:switch & operator ternary": {
"code": "public class Hari {\n    public static void main(String[] args) {\n        int hari = 6;\n        String jenis = switch (hri) {\n            case 1, 2, 3, 4, 5 -> \"Hari kerja\";\n            case 6, 7 -> \"Akhir pekan\";\n            default -> \"Tidak valid\";\n        };\n        System.out.println(jenis);\n\n        String nilai = \"B\";\n        switch (nilai) {\n            case \"A\":\n                System.out.println(\"Istimewa\");\n                break;\n            case \"B\":\n                System.out.println(\"Baik\");\n                break;\n            default:\n                System.out.println(\"Tetap semangat\");\n        }\n\n        int umur = 17;\n        String status = umur >= 17 ? \"boleh punya KTP\" : \"belum\";\n        System.out.println(status);\n    }\n}",
"err": "Hari.java:4: error: cannot find symbol\n        String jenis = switch (hri) {\n                               ^",
"line": 4,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"java:Kelas Arrays & array dua dimensi": {
"code": "import java.util.Arrays;\n\npublic class Tabel {\n    public static void main(String[] args) {\n        int[] nilai = {78, 92, 65, 88};\n        Arrays.sort(nilai);\n        System.out.println(Arrays.toString(nilai);\n\n        int[] salinan = Arrays.copyOf(nilai, 6);\n        System.out.println(Arrays.toString(salinan));\n\n        int[][] kursi = new int[2][3];\n        kursi[0][1] = 1;\n        kursi[1][2] = 1;\n        for (int r = 0; r < kursi.length; r++) {\n            for (int c = 0; c < kursi[r].length; c++) {\n                System.out.print((c > 0 ? \" \" : \"\") + (kursi[r][c] == 1 ? \"X\" : \".\"));\n            }\n            System.out.println();\n        }\n        System.out.println(Arrays.deepToString(kursi));\n    }\n}",
"err": "Tabel.java:7: error: ')' or ',' expected\n        System.out.println(Arrays.toString(nilai);\n                                                 ^",
"line": 7,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Access specifier: public, private, protected": {
"code": "class Rekening {\n    private long saldo;              // hanya kelas ini yang boleh mengubah\n    public final String pemilik;\n\n    public Rekening(String pemilik) {\n        this.pemilik = pemilik;\n    }\n    public void setor(long jumlah) {\n        if (jumlah > 0) saldo += jumlah;\n    }\n    public boolean tarik(long jumlah) {\n        if (jumlah <= 0 || jumlah > saldo) return false;\n        saldo -= jumlah;\n        return true;\n    }\n    public long getSaldo() { return saldo; }\n}\n\npublic class Bank {\n    public static void main(String[] args) {\n        Rekening r = new Rekening(\"Andi\");\n        r.setor(100_000);\n        System.out.println(r.tarik(250_000);\n        System.out.println(r.tarik(40_000));\n        System.out.println(r.pemilik + \": \" + r.getSaldo());\n        // r.saldo = 999_999;  // error: saldo has private access\n    }\n}",
"err": "Bank.java:23: error: ')' or ',' expected\n        System.out.println(r.tarik(250_000);\n                                           ^",
"line": 23,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Kata kunci static & final": {
"code": "class Siswa {\n    static int jumlah = 0;          // satu untuk semua objek\n    static final int MAKS = 30;     // konstanta\n    final String nis;               // diisi sekali di konstruktor\n    String nama;\n\n    Siswa(String nis, String nama) {\n        this.nis = nis;\n        this.nama = nama;\n        jumlah++;\n    }\n    static boolean kelasPenuh() {\n        return jumlah >= MAKS;\n    }\n}\n\npublic class Sekolah {\n    public static void main(String[] args) {\n        new Siswa(\"001\", \"Rina\");\n        new Siswa(\"002\", \"Sandi\");\n        Siswa s = new Siswa(\"003\", \"Tari\");\n        s.nama = \"Tari A.\";          // boleh: bukan final\n        // s.nis = \"999\";            // error: cannot assign a value to final variable\n        System.out.println(Siswa.jumlah;\n        System.out.println(Siswa.kelasPenuh());\n        System.out.println(s.nis + \" \" + s.nama);\n    }\n}",
"err": "Sekolah.java:24: error: ')' or ',' expected\n        System.out.println(Siswa.jumlah;\n                                       ^",
"line": 24,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Siklus hidup objek & garbage collector": {
"code": "class Kotak {\n    String label;\n    Kotak(String label) {\n        this.label = label;\n        System.out.println(\"Dibuat: \" + label;\n    }\n}\n\npublic class Siklus {\n    public static void main(String[] args) {\n        Kotak a = new Kotak(\"A\");\n        Kotak b = new Kotak(\"B\");\n        Kotak c = a;          // dua referensi ke objek A\n        a = null;             // A masih dijangkau lewat c\n        b = null;             // B tidak terjangkau lagi -> calon GC\n        System.out.println(c.label);\n        c = new Kotak(\"C\");   // A kini juga tidak terjangkau\n        System.out.println(c.label);\n    }\n}",
"err": "Siklus.java:5: error: ')' or ',' expected\n        System.out.println(\"Dibuat: \" + label;\n                                             ^",
"line": 5,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Pass by value (juga untuk objek)": {
"code": "import java.util.ArrayList;\nimport java.util.List\n\npublic class Salin {\n    static void ubahAngka(int x) { x = 99; }\n    static void ubahIsi(List<String> d) { d.add(\"baru\"); }\n    static void gantiObjek(List<String> d) {\n        d = new ArrayList<>();\n        d.add(\"lain\");\n    }\n\n    public static void main(String[] args) {\n        int n = 5;\n        ubahAngka(n);\n        System.out.println(n);\n\n        List<String> daftar = new ArrayList<>();\n        daftar.add(\"awal\");\n        ubahIsi(daftar);\n        System.out.println(daftar);\n        gantiObjek(daftar);\n        System.out.println(daftar);\n    }\n}",
"err": "Salin.java:2: error: ';' expected\nimport java.util.List\n                     ^",
"line": 2,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:Kelas abstrak & abstraksi": {
"code": "abstract class Bentuk {\n    private final String nama\n    Bentuk(String nama) { this.nama = nama; }\n    abstract double luas();                 // wajib diisi subclass\n    String info() {                         // dipakai bersama\n        return nama + \": \" + String.format(\"%.2f\", luas());\n    }\n}\nclass Lingkaran extends Bentuk {\n    double r;\n    Lingkaran(double r) { super(\"Lingkaran\"); this.r = r; }\n    double luas() { return Math.PI * r * r; }\n}\nclass Persegi extends Bentuk {\n    double s;\n    Persegi(double s) { super(\"Persegi\"); this.s = s; }\n    double luas() { return s * s; }\n}\n\npublic class Abstraksi {\n    public static void main(String[] args) {\n        Bentuk[] semua = { new Lingkaran(1), new Persegi(3) };\n        for (Bentuk b : semua) System.out.println(b.info());\n        // new Bentuk(\"x\");  // error: Bentuk is abstract\n    }\n}",
"err": "Abstraksi.java:2: error: ';' expected\n    private final String nama\n                             ^",
"line": 2,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:Overloading, overriding & binding": {
"code": "class Hewan {\n    String suara() { return \"...\"; }\n}\nclass Kucing extends Hewan {\n    @Override\n    String suara() { return \"Meong\"; }\n}\n\npublic class Binding {\n    static String jelaskan(Hewan h) { return \"Hewan\"; }\n    static String jelaskan(Kucing k) { return \"Kucing\"; }\n\n    static int tambah(int a, int b) { return a + b; }\n    static double tambah(double a, double b) { return a + b; }\n\n    public static void main(String[] args) {\n        Hewan h = new Kucing();\n        System.out.println(h.suara();       // dynamic: tipe objek\n        System.out.println(jelaskan(h));     // static: tipe variabel\n        System.out.println(tambah(2, 3));\n        System.out.println(tambah(2.5, 3));\n    }\n}",
"err": "Binding.java:18: error: ')' or ',' expected\n        System.out.println(h.suara();       // dynamic: tipe objek\n                                    ^",
"line": 18,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Enum & record": {
"code": "enum Status {\n    BARU(\"Menunggu\"), DIKIRIM(\"Dalam perjalanan\"), SELESAI(\"Diterima\")\n    private final String label;\n    Status(String label) { this.label = label; }\n    String label() { return label; }\n}\n\nrecord Pesanan(int id, String barang, Status status) {}\n\npublic class Toko {\n    public static void main(String[] args) {\n        Pesanan p = new Pesanan(101, \"Kopi Gayo\", Status.DIKIRIM);\n        System.out.println(p);\n        System.out.println(p.barang() + \" - \" + p.status().label());\n        System.out.println(p.equals(new Pesanan(101, \"Kopi Gayo\", Status.DIKIRIM)));\n        StringBuilder sb = new StringBuilder();\n        for (Status s : Status.values()) {\n            sb.append(s).append(\"(\").append(s.ordinal()).append(\") \");\n        }\n        System.out.println(sb.toString().trim());\n        System.out.println(Status.valueOf(\"SELESAI\").label());\n    }\n}",
"err": "Toko.java:2: error: ',', '}', or ';' expected\n    BARU(\"Menunggu\"), DIKIRIM(\"Dalam perjalanan\"), SELESAI(\"Diterima\")\n                                                                      ^",
"line": 2,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:Kelas bersarang & initializer block": {
"code": "public class Luar {\n    static int dimuat;\n    int nomor;\n\n    static {                         // sekali, saat kelas dimuat\n        dimuat = 1;\n        System.out.println(\"static block\";\n    }\n    {                                // setiap objek dibuat\n        nomor = 7;\n        System.out.println(\"instance block\");\n    }\n    Luar() { System.out.println(\"konstruktor, nomor=\" + nomor); }\n\n    static class Pembantu {           // static nested\n        String sapa() { return \"halo dari Pembantu\"; }\n    }\n    class Dalam {                     // inner: butuh objek Luar\n        int ambil() { return nomor * 2; }\n    }\n\n    public static void main(String[] args) {\n        Luar o = new Luar();\n        System.out.println(new Pembantu().sapa());\n        Luar.Dalam d = o.new Dalam();\n        System.out.println(d.ambil());\n        Runnable r = new Runnable() {     // anonymous class\n            public void run() { System.out.println(\"anonim jalan\"); }\n        };\n        r.run();\n    }\n}",
"err": "Luar.java:7: error: ')' or ',' expected\n        System.out.println(\"static block\";\n                                         ^",
"line": 7,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Array lawan ArrayList": {
"code": "import java.util.ArrayList;\nimport java.util.Arrays;\nimport java.util.List;\n\npublic class Banding {\n    public static void main(String[] args) {\n        int[] arr = new int[3];\n        arr[0] = 10;\n        System.out.println(arr.length + \" \" + Arrays.toString(arr);\n\n        List<Integer> list = new ArrayList<>();\n        list.add(10);\n        list.add(20);\n        list.add(0, 5);           // sisip di depan\n        list.remove(Integer.valueOf(20));\n        System.out.println(list.size() + \" \" + list);\n        System.out.println(list.get(1) + \" \" + list.contains(10));\n\n        List<String> tetap = List.of(\"a\", \"b\");\n        try {\n            tetap.add(\"c\");\n        } catch (UnsupportedOperationException e) {\n            System.out.println(\"List.of tidak bisa diubah\");\n        }\n    }\n}",
"err": "Banding.java:9: error: ')' or ',' expected\n        System.out.println(arr.length + \" \" + Arrays.toString(arr);\n                                                                  ^",
"line": 9,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Deque & Iterator": {
"code": "import java.util.*;\n\npublic class DekIter {\n    public static void main(String[] args) {\n        Deque<String> tumpuk = new ArrayDeque<>()\n        tumpuk.push(\"piring1\");\n        tumpuk.push(\"piring2\");\n        System.out.println(tumpuk.pop());\n\n        Deque<String> antre = new ArrayDeque<>();\n        antre.offer(\"Ani\");\n        antre.offer(\"Bayu\");\n        antre.offerFirst(\"VIP\");\n        System.out.println(antre.poll() + \" \" + antre);\n\n        List<Integer> nilai = new ArrayList<>(List.of(80, 45, 90, 30));\n        Iterator<Integer> it = nilai.iterator();\n        while (it.hasNext()) {\n            if (it.next() < 50) it.remove();\n        }\n        System.out.println(nilai);\n    }\n}",
"err": "DekIter.java:5: error: ';' expected\n        Deque<String> tumpuk = new ArrayDeque<>()\n                                                 ^",
"line": 5,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:Generics: kode yang aman tipe": {
"code": "import java.util.List;\n\nclass Kotak<T> {\n    private final T isi;\n    Kotak(T isi) { this.isi = isi; }\n    T ambil() { return isi; }\n}\n\npublic class Generik {\n    static <T> T pertama(List<T> data) {\n        return data.get(0);\n    }\n    static <T extends Number> double jumlah(List<T> angka) {\n        double total = 0;\n        for (T x : angka) totl += x.doubleValue();\n        return total;\n    }\n    static void cetak(List<?> apaSaja) {\n        System.out.println(\"Isi: \" + apaSaja);\n    }\n\n    public static void main(String[] args) {\n        Kotak<String> k = new Kotak<>(\"rahasia\");\n        String s = k.ambil();             // tanpa cast\n        System.out.println(s.toUpperCase());\n        System.out.println(pertama(List.of(3, 1, 2)));\n        System.out.println(jumlah(List.of(1.5, 2, 3L)));\n        cetak(List.of('a', 'b'));\n    }\n}",
"err": "Generik.java:15: error: cannot find symbol\n        for (T x : angka) totl += x.doubleValue();\n                          ^",
"line": 15,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"java:Checked, unchecked & exception buatan sendiri": {
"code": "class SaldoKurangException extends Exception {\n    SaldoKurangException(long kurang) {\n        super(\"Saldo kurang Rp\" + kurang);\n    }\n}\n\npublic class Atm {\n    static long saldo = 50_000;\n\n    static void tarik(long jumlah) throws SaldoKurangException {\n        if (jumlah > saldo) throw new SaldoKurangException(jumlah - saldo);\n        saldo -= jumlah;\n    }\n    static void layani(long jumlah) throws SaldoKurangException {\n        System.out.println(\"Memproses \" + jumlah;\n        tarik(jumlah);                    // exception naik dari sini\n        System.out.println(\"Berhasil\");\n    }\n\n    public static void main(String[] args) {\n        try {\n            layani(20_000);\n            layani(80_000);\n        } catch (SaldoKurangException e) {\n            System.out.println(\"Gagal: \" + e.getMessage());\n        } finally {\n            System.out.println(\"Sisa saldo \" + saldo);\n        }\n    }\n}",
"err": "Atm.java:15: error: ')' or ',' expected\n        System.out.println(\"Memproses \" + jumlah;\n                                                ^",
"line": 15,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Anotasi": {
"code": "import java.lang.annotation.*;\nimport java.lang.reflect.Method\n\n@Retention(RetentionPolicy.RUNTIME)\n@Target(ElementType.METHOD)\n@interface Tugas {\n    String pemilik();\n    int prioritas() default 1;\n}\n\npublic class Anotasi {\n    @Tugas(pemilik = \"Rina\", prioritas = 3)\n    public void kirimEmail() {}\n\n    @Deprecated\n    public void caraLama() {}\n\n    @Override\n    public String toString() { return \"Anotasi demo\"; }\n\n    public static void main(String[] args) throws Exception {\n        Method m = Anotasi.class.getMethod(\"kirimEmail\");\n        Tugas t = m.getAnnotation(Tugas.class);\n        System.out.println(t.pemilik() + \" prioritas \" + t.prioritas());\n        System.out.println(new Anotasi());\n    }\n}",
"err": "Anotasi.java:2: error: ';' expected\nimport java.lang.reflect.Method\n                               ^",
"line": 2,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:Functional interface & komposisi fungsi": {
"code": "import java.util.function.*;\n\npublic class Fungsi {\n    static Function<Integer, Integer> kaliDengan(int n) {   // mengembalikan fungsi\n        return x -> x * n;\n    }\n\n    public static void main(String[] args) {\n        Function<Integer, Integer> tambah10 = x -> x + 10;\n        Function<Integer, Integer> kali2 = kaliDengan(2);\n        System.out.println(tambah10.andThen(kali2).apply(5);\n        System.out.println(tambah10.compose(kali2).apply(5));\n\n        Predicate<String> panjang = s -> s.length() > 4;\n        Predicate<String> awalanK = s -> s.startsWith(\"K\");\n        System.out.println(panjang.and(awalanK).test(\"Kopi\"));\n        System.out.println(panjang.and(awalanK).test(\"Keripik\"));\n\n        Supplier<String> sapa = () -> \"Halo\";\n        Consumer<String> cetak = System.out::println;\n        cetak.accept(sapa.get());\n\n        BinaryOperator<Integer> maks = Math::max;\n        System.out.println(maks.apply(3, 9));\n    }\n}",
"err": "Fungsi.java:11: error: ')' or ',' expected\n        System.out.println(tambah10.andThen(kali2).apply(5);\n                                                           ^",
"line": 11,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Stream API & method chaining": {
"code": "import java.util.*;\nimport java.util.stream.*;\n\npublic class Aliran {\n    record Produk(String nama, String kategori, int harga) {}\n\n    public static void main(String[] args) {\n        List<Produk> data = List.of(\n            new Produk(\"Kopi Gayo\", \"Minuman\", 85000),\n            new Produk(\"Teh Melati\", \"Minuman\", 25000),\n            new Produk(\"Keripik\", \"Camilan\", 15000),\n            new Produk(\"Kacang Mete\", \"Camilan\", 60000),\n            new Produk(\"Madu Hutan\", \"Minuman\", 120000));\n\n        List<String> mahal = data.stream()\n            .filter(p -> p.harga() > 50000)\n            .sorted(Comparator.comparingInt(Produk::harga))\n            .map(Produk::nama)\n            .collect(Collectors.toList());\n        System.out.println(mahal;\n\n        int total = data.stream().mapToInt(Produk::harga).sum();\n        System.out.println(total);\n\n        Map<String, Long> perKategori = data.stream()\n            .collect(Collectors.groupingBy(Produk::kategori, TreeMap::new, Collectors.counting()));\n        System.out.println(perKategori);\n\n        String nama = IntStream.rangeClosed(1, 5)\n            .filter(i -> i % 2 == 1)\n            .mapToObj(i -> \"#\" + i)\n            .collect(Collectors.joining(\" \"));\n        System.out.println(nama);\n    }\n}",
"err": "Aliran.java:20: error: ')' or ',' expected\n        System.out.println(mahal;\n                                ^",
"line": 20,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Optional: mengganti null dengan aman": {
"code": "import java.util.*;\n\npublic class Opsional {\n    static Map<String, String> kotaPelanggan = Map.of(\"Andi\", \"Jakarta\", \"Budi\", \"Bandung\")\n\n    static Optional<String> cariKota(String nama) {\n        return Optional.ofNullable(kotaPelanggan.get(nama));\n    }\n\n    public static void main(String[] args) {\n        System.out.println(cariKota(\"Andi\").map(String::toUpperCase).orElse(\"-\"));\n        System.out.println(cariKota(\"Gita\").map(String::toUpperCase).orElse(\"-\"));\n        cariKota(\"Budi\").ifPresent(k -> System.out.println(\"Kirim ke \" + k));\n        System.out.println(cariKota(\"Andi\").filter(k -> k.startsWith(\"B\")).isPresent());\n        String kota = cariKota(\"Zaki\").orElseGet(() -> \"Kota belum diisi\");\n        System.out.println(kota);\n    }\n}",
"err": "Opsional.java:4: error: ';' expected\n    static Map<String, String> kotaPelanggan = Map.of(\"Andi\", \"Jakarta\", \"Budi\", \"Bandung\")\n                                                                                           ^",
"line": 4,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:File modern dengan java.nio": {
"code": "import java.io.IOException;\nimport java.nio.file.*;\nimport java.util.List;\nimport java.util.stream.Stream;\n\npublic class Berkas {\n    public static void main(String[] args) throws IOException {\n        Path p = Path.of(\"catatan.txt\");\n        Files.writeString(p, \"kopi,85000\\nteh,25000\\nmadu,120000\\n\");\n\n        List<String> baris = Files.readAllLines(p);\n        System.out.println(baris.size() + \" baris\");\n\n        try (Stream<String> s = Files.lines(p)) {\n            int total = s.mapToInt(b -> Integer.parseInt(b.split(\",\")[1])).sum();\n            System.out.println(\"Total \" + totl);\n        }\n\n        Files.writeString(p, \"gula,18000\\n\", StandardOpenOption.APPEND);\n        System.out.println(Files.readAllLines(p).get(3));\n        System.out.println(Files.exists(p));\n        Files.delete(p);\n        System.out.println(Files.exists(p));\n    }\n}",
"err": "Berkas.java:16: error: cannot find symbol\n            System.out.println(\"Total \" + totl);\n                                          ^",
"line": 16,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"java:Tanggal & waktu (java.time)": {
"code": "import java.time.*;\nimport java.time.format.DateTimeFormatter;\nimport java.time.temporal.ChronoUnit;\n\npublic class Waktu {\n    public static void main(String[] args) {\n        LocalDate pesan = LocalDate.of(2024, 10, 28);\n        LocalDate tiba = pesan.plusDays(5);\n        System.out.println(tiba;\n        System.out.println(tiba.getDayOfWeek());\n        System.out.println(ChronoUnit.DAYS.between(pesan, tiba));\n\n        DateTimeFormatter f = DateTimeFormatter.ofPattern(\"dd/MM/yyyy\");\n        System.out.println(tiba.format(f));\n\n        Period umur = Period.between(LocalDate.of(2005, 8, 17), LocalDate.of(2024, 10, 28));\n        System.out.println(umur.getYears() + \" tahun \" + umur.getMonths() + \" bulan\");\n\n        ZonedDateTime jkt = LocalDateTime.of(2024, 10, 28, 9, 0).atZone(ZoneId.of(\"Asia/Jakarta\"));\n        System.out.println(jkt.withZoneSameInstant(ZoneId.of(\"Asia/Tokyo\")).toLocalTime());\n    }\n}",
"err": "Waktu.java:9: error: ')' or ',' expected\n        System.out.println(tiba;\n                               ^",
"line": 9,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"java:Regular expression": {
"code": "import java.util.regex.*;\n\npublic class Pola {\n    public static void main(String[] args) {\n        String email = \"rina@kampus.ac.id\"\n        System.out.println(email.matches(\"[\\\\w.]+@[\\\\w.]+\\\\.[a-z]{2,}\"));\n\n        String teks = \"Hubungi 0812-3456-7890 atau 0857-1111-2222\";\n        Matcher m = Pattern.compile(\"(\\\\d{4})-(\\\\d{4})-(\\\\d{4})\").matcher(teks);\n        while (m.find()) {\n            System.out.println(\"Nomor: \" + m.group() + \" | awalan \" + m.group(1));\n        }\n\n        String tgl = \"2024-10-28\";\n        System.out.println(tgl.replaceAll(\"(\\\\d{4})-(\\\\d{2})-(\\\\d{2})\", \"$3/$2/$1\"));\n        System.out.println(String.join(\"|\", \"a, b ,c\".split(\"\\\\s*,\\\\s*\")));\n    }\n}",
"err": "Pola.java:5: error: ';' expected\n        String email = \"rina@kampus.ac.id\"\n                                          ^",
"line": 5,
"kind": "semicolon",
"why": "Setiap statement Java diakhiri titik koma."
},
"java:ExecutorService & virtual thread": {
"code": "import java.util.*;\nimport java.util.concurrent.*;\n\npublic class Pekerja {\n    static int hitungHarga(int id) throws InterruptedException {\n        Thread.sleep(100);                 // pura-pura memanggil database\n        return id * 1000;\n    }\n\n    public static void main(String[] args) throws Exception {\n        try (ExecutorService ex = Executors.newVirtualThreadPerTaskExecutor()) {\n            List<Future<Integer>> hasil = new ArrayList<>();\n            for (int i = 1; i <= 10_000; i++) {\n                final int id = i;\n                hasil.add(ex.submit(() -> hitungHarga(id)));\n            }\n            long total = 0;\n            for (Future<Integer> f : hasil) totl += f.get();\n            System.out.println(\"Total: \" + total);\n        }\n        // 10.000 tugas x 100 ms selesai sekitar sepersekian detik,\n        // karena virtual thread yang menunggu tidak memblokir thread OS.\n    }\n}",
"err": "Pekerja.java:18: error: cannot find symbol\n            for (Future<Integer> f : hasil) totl += f.get();\n                                            ^",
"line": 18,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"java:volatile & Java Memory Model": {
"code": "public class Bendera {\n    private static volatile boolean jalan = true;   // tanpa volatile, loop bisa tak berhenti\n\n    public static void main(String[] args) throws InterruptedException {\n        Thread pekerja = new Thread(() -> {\n            long putaran = 0;\n            while (jalan) putaran++;\n            System.out.println(\"Pekerja berhenti\";\n        });\n        pekerja.start();\n        Thread.sleep(200);\n        jalan = false;              // perubahan langsung terlihat oleh pekerja\n        pekerja.join();\n        System.out.println(\"Selesai\");\n    }\n}",
"err": "Bendera.java:8: error: ')' or ',' expected\n            System.out.println(\"Pekerja berhenti\";\n                                                 ^",
"line": 8,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Tipe data & typecasting": {
"code": "umur = \"17\"\nprint(type(umr))\numur = int(umur)            # str -> int\nprint(umur + 1)\n\nharga = 9.99\nprint(int(harga))           # potong pecahan\nprint(round(harga))         # bulatkan\nprint(float(\"3.5\") * 2)\nprint(str(2024) + \" tahun\")\n\nprint(bool(0), bool(\"\"), bool([]), bool(\"0\"), bool(None))\n\ntry:\n    print(\"5\" + 3)\nexcept TypeError as e:\n    print(\"TypeError:\", e)\n\nprint(int(\"ff\", 16))        # dari heksadesimal",
"err": "File \"main.py\", line 2, in <module>\n    print(type(umr))\nNameError: name 'umr' is not defined. Did you mean: 'umur'?",
"line": 2,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:Operator lengkap: //, **, walrus, dan @": {
"code": "print(7 / 2, 7 // 2, 7 % 2, 2 ** 10)\nprint(-7 // 2)              # dibulatkan ke bawah, bukan ke nol\n\nnilai = 85\nprint(0 <= nili <= 100)\nprint(\"a\" in \"kata\", 3 in [1, 2, 3])\n\ndata = None\nprint(data is None)\n\nskor = [70, 95, 88]\nif (n := len(skor)) > 2:\n    print(f\"ada {n} skor\")\n\nclass Matriks:\n    def __init__(self, baris):\n        self.b = baris\n    def __matmul__(self, lain):\n        return Matriks([[sum(a * b for a, b in zip(r, k)) for k in zip(*lain.b)] for r in self.b])\n\nA = Matriks([[1, 2], [3, 4]])\nB = Matriks([[5, 6], [7, 8]])\nprint((A @ B).b)",
"err": "File \"main.py\", line 5, in <module>\n    print(0 <= nili <= 100)\nNameError: name 'nili' is not defined. Did you mean: 'nilai'?",
"line": 5,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:Argumen default, keyword, *args, **kwargs": {
"code": "def sapa(nama, salam=\"Halo\", tanda=\"!\"):\n    return f\"{salam}, {nama}{tanda}\"\n\nprint(sapa(\"Rina\")\nprint(sapa(\"Budi\", tanda=\"?\"))\nprint(sapa(salam=\"Selamat pagi\", nama=\"Citra\"))\n\ndef total(*harga, diskon=0):\n    return sum(harga) * (100 - diskon) // 100\n\nprint(total(10000, 25000, 5000))\nprint(total(10000, 25000, diskon=10))\n\ndef profil(**data):\n    return \", \".join(f\"{k}={v}\" for k, v in data.items())\n\nprint(profil(nama=\"Eko\", kota=\"Medan\"))\n\ndef tambah(item, wadah=None):\n    if wadah is None:\n        wadah = []\n    wadah.append(item)\n    return wadah\n\nprint(tambah(1), tambah(2))",
"err": "File \"main.py\", line 4\n    print(sapa(\"Rina\")\nSyntaxError: '(' was never closed",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Scope variabel: aturan LEGB": {
"code": "pajak = 0.11                     # global\n\ndef harga_akhir(harga)\n    diskon = 0.05                # local\n    return harga * (1 - diskon) * (1 + pajak)\n\nprint(round(harga_akhir(100000)))\n\nhitungan = 0\ndef klik():\n    global hitungan\n    hitungan += 1\n\nklik(); klik()\nprint(hitungan)\n\ndef buat_penghitung():\n    n = 0                        # enclosing\n    def tambah():\n        nonlocal n\n        n += 1\n        return n\n    return tambah\n\nc = buat_penghitung()\nc(); c()\nprint(c())\n\ndef rusak():\n    try:\n        hitungan += 1            # dianggap lokal, belum ada nilainya\n    except UnboundLocalError as e:\n        print(\"UnboundLocalError\")\n\nrusak()",
"err": "File \"main.py\", line 3\n    def harga_akhir(harga)\nSyntaxError: expected ':'",
"line": 3,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:f-string, slicing & method string": {
"code": "nama = \"  budi santoso \"\nrapi = nma.strip().title()\nprint(rapi)\nprint(rapi[:4], rapi[-7:], rapi[::-1])\n\nharga = 1250000\nprint(f\"Harga: Rp{harga:,}\".replace(\",\", \".\"))\nprint(f\"Rata-rata: {85.666:.2f}\")\nprint(f\"[{'kopi':>8}] [{'teh':<6}] [{7:03d}]\")\n\nkalimat = \"saya belajar python dan sql\"\nkata = kalimat.split()\nprint(len(kata), kata[2])\nprint(\"-\".join(kata))\nprint(kalimat.count(\"a\"), kalimat.find(\"python\"))\nprint(kalimat.startswith(\"saya\"), \"SQL\" in kalimat.upper())",
"err": "File \"main.py\", line 2, in <module>\n    rapi = nma.strip().title()\nNameError: name 'nma' is not defined. Did you mean: 'nama'?",
"line": 2,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:match-case & ekspresi kondisional": {
"code": "def jenis_hari(h):\n    match h:\n        case \"sabtu\" | \"minggu\":\n            return \"akhir pekan\"\n        case \"senin\" | \"selasa\" | \"rabu\" | \"kamis\" | \"jumat\":\n            return \"hari kerja\"\n        case _:\n            return \"tidak dikenal\"\n\nprint(jenis_hari(\"sabtu\"), \"/\", jenis_hari(\"rabu\")\n\ndef arah(perintah):\n    match perintah.split():\n        case [\"jalan\", tujuan]:\n            return f\"berjalan ke {tujuan}\"\n        case [\"ambil\", benda, *sisa] if sisa:\n            return f\"ambil {benda} dan {len(sisa)} barang lain\"\n        case [\"ambil\", benda]:\n            return f\"ambil {benda}\"\n        case _:\n            return \"perintah tidak dikenal\"\n\nprint(arah(\"jalan utara\"))\nprint(arah(\"ambil kunci peta senter\"))\nprint(arah(\"ambil kunci\"))\n\numur = 16\nprint(\"dewasa\" if umur >= 17 else \"remaja\")",
"err": "File \"main.py\", line 10\n    print(jenis_hari(\"sabtu\"), \"/\", jenis_hari(\"rabu\")\nSyntaxError: '(' was never closed",
"line": 10,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:enumerate, zip, break, continue, else": {
"code": "buah = [\"apel\", \"jeruk\", \"mangga\"]\nfor i, b in enumerate(buah, start=1)\n    print(i, b)\n\nharga = [12000, 8000, 15000]\nfor b, h in zip(buah, harga):\n    print(f\"{b}: {h}\")\n\nganjil = []\nfor n in range(1, 10):\n    if n % 2 == 0:\n        continue\n    if n > 7:\n        break\n    ganjil.append(n)\nprint(ganjil)\n\ntarget = \"durian\"\nfor b in buah:\n    if b == target:\n        print(\"ketemu\")\n        break\nelse:\n    print(target, \"tidak ada\")\n\nprint(list(range(10, 0, -3)), list(reversed(buah)))",
"err": "File \"main.py\", line 2\n    for i, b in enumerate(buah, start=1)\nSyntaxError: expected ':'",
"line": 2,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:Tuple & unpacking": {
"code": "titik = (3, 4)\nx, y = titk\nprint(x, y)\n\ndef statistik(data):\n    return min(data), max(data), sum(data) / len(data)\n\nlo, hi, rata = statistik([70, 85, 90, 65])\nprint(lo, hi, rata)\n\npertama, *tengah, terakhir = [1, 2, 3, 4, 5]\nprint(pertama, tengah, terakhir)\n\na, b = 10, 20\na, b = b, a\nprint(a, b)\n\njarak = {(\"Jakarta\", \"Bandung\"): 150, (\"Jakarta\", \"Bogor\"): 60}\nprint(jarak[(\"Jakarta\", \"Bogor\")])\n\ntry:\n    titik[0] = 9\nexcept TypeError:\n    print(\"tuple tidak bisa diubah\")\n\nsatu = (5,)\nprint(type(satu).__name__, type((5)).__name__)",
"err": "File \"main.py\", line 2, in <module>\n    x, y = titk\nNameError: name 'titk' is not defined. Did you mean: 'titik'?",
"line": 2,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:Dictionary lanjutan & operasi set": {
"code": "from collections import Counter, defaultdict\n\nstok = {\"kopi\": 40, \"teh\": 120}\nprint(stok.get(\"madu\", 0)\nstok |= {\"madu\": 15}\nfor nama, jml in stok.items():\n    print(f\"{nama:5} {jml}\")\n\npesanan = [\"kopi\", \"teh\", \"kopi\", \"madu\", \"kopi\"]\nprint(Counter(pesanan).most_common(2))\n\nper_kota = defaultdict(list)\nfor nama, kota in [(\"Andi\", \"Jakarta\"), (\"Budi\", \"Bandung\"), (\"Dewi\", \"Jakarta\")]:\n    per_kota[kota].append(nama)\nprint(dict(per_kota))\n\nkelas_a = {\"Andi\", \"Budi\", \"Citra\"}\nkelas_b = {\"Budi\", \"Dewi\"}\nprint(sorted(kelas_a & kelas_b), sorted(kelas_a - kelas_b), sorted(kelas_a | kelas_b))",
"err": "File \"main.py\", line 4\n    print(stok.get(\"madu\", 0)\nSyntaxError: '(' was never closed",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:raise, exception buatan sendiri & else/finally": {
"code": "class SaldoKurang(Exception)\n    def __init__(self, kurang):\n        super().__init__(f\"saldo kurang Rp{kurang:,}\")\n        self.kurang = kurang\n\nsaldo = 50_000\n\ndef tarik(jumlah):\n    global saldo\n    if jumlah <= 0:\n        raise ValueError(\"jumlah harus positif\")\n    if jumlah > saldo:\n        raise SaldoKurang(jumlah - saldo)\n    saldo -= jumlah\n\ndef layani(jumlah):\n    print(\"memproses\", jumlah)\n    tarik(jumlah)\n    print(\"berhasil\")\n\nfor j in [20_000, 80_000, -5]:\n    try:\n        layani(j)\n    except SaldoKurang as e:\n        print(\"gagal:\", e)\n    except ValueError as e:\n        print(\"input salah:\", e)\n    else:\n        print(\"transaksi tercatat\")\n    finally:\n        print(\"sisa\", saldo)",
"err": "File \"main.py\", line 1\n    class SaldoKurang(Exception)\nSyntaxError: expected ':'",
"line": 1,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:Context manager: with": {
"code": "from contextlib import contextmanager\nimport time\n\nwith open(\"catatan.txt\", \"w\") as f:\n    f.write(\"baris 1\\nbaris 2\\n\")\nprint(f.closed)\n\nwith open(\"catatan.txt\") as sumber, open(\"salinan.txt\", \"w\") as tujuan:\n    for baris in sumber:\n        tujuan.write(baris.upper())\nprint(open(\"salinan.txt\").read().strip())\n\n@contextmanager\ndef stopwatch(label):\n    mulai = time.perf_counter()\n    print(f\"[{label}] mulai\")\n    try:\n        yield\n    finally:\n        print(f\"[{label}] selesai\")\n\nwith stopwatch(\"hitung\"):\n    total = sum(range(1_000_000))\nprint(totl)\n\nclass Kunci:\n    def __enter__(self):\n        print(\"kunci dipasang\"); return self\n    def __exit__(self, tipe, nilai, jejak):\n        print(\"kunci dilepas\", tipe.__name__ if tipe else \"tanpa error\")\n        return True                          # telan exception\n\nwith Kunci():\n    1 / 0\nprint(\"program lanjut\")",
"err": "File \"main.py\", line 24, in <module>\n    print(totl)\nNameError: name 'totl' is not defined. Did you mean: 'total'?",
"line": 24,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:pathlib & modul glob": {
"code": "from pathlib import Path\nimport glob\n\nfolder = Path(\"laporan\")\nfolder.mkdir(exist_ok=True)\nfor bulan in [\"jan\", \"feb\", \"mar\"]:\n    (folder / f\"penjualan_{bulan}.csv\").write_text(\"produk,jumlah\\nkopi,10\\n\")\n(folder / \"catatan.txt\").write_text(\"rahasia\")\n\ncsv = sorted(folder.glob(\"*.csv\"))\nprint([p.name for p in csv]\nprint(csv[0].stem, csv[0].suffix)\n\nprint(sorted(glob.glob(\"laporan/penjualan_?a?.csv\")))\n\ntotal = sum(len(p.read_text().splitlines()) - 1 for p in csv)\nprint(\"total baris data:\", total)\n\nfor p in folder.iterdir():\n    p.unlink()\nfolder.rmdir()\nprint(folder.exists())",
"err": "File \"main.py\", line 11\n    print([p.name for p in csv]\nSyntaxError: '(' was never closed",
"line": 11,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Modul bawaan yang sering dipakai": {
"code": "import math, random, json, statistics, itertools\nfrom datetime import date, timedelta\n\nprint(math.sqrt(144), math.pi.__round__(4), math.factorial(5))\n\nrandom.seed(42)\nprint(random.randint(1, 6), random.choice([\"kopi\", \"teh\", \"jus\"]))\n\nhari_ini = date(2024, 10, 28)\nprint(hari_ni + timedelta(days=5), hari_ini.strftime(\"%d/%m/%Y\"))\n\ndata = {\"nama\": \"Rina\", \"nilai\": [80, 92]}\nteks = json.dumps(data)\nprint(teks, json.loads(teks)[\"nilai\"][1])\n\nprint(statistics.mean([80, 92, 75]), statistics.median([80, 92, 75]))\nprint(list(itertools.combinations(\"ABC\", 2)))",
"err": "File \"main.py\", line 10, in <module>\n    print(hari_ni + timedelta(days=5), hari_ini.strftime(\"%d/%m/%Y\"))\nNameError: name 'hari_ni' is not defined. Did you mean: 'hari_ini'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:Enkapsulasi: property & dataclass": {
"code": "from dataclasses import dataclass, field\n\nclass Rekening:\n    def __init__(self, pemilik):\n        self.pemilik = pemilik\n        self._saldo = 0\n\n    @property\n    def saldo(self):\n        return self._saldo\n\n    @saldo.setter\n    def saldo(self, nilai):\n        if nilai < 0:\n            raise ValueError(\"saldo tidak boleh negatif\")\n        self._saldo = nilai\n\nr = Rekening(\"Andi\")\nr.saldo = 75_000\nprint(r.saldo\ntry:\n    r.saldo = -1\nexcept ValueError as e:\n    print(e)\n\n@dataclass\nclass Produk:\n    nama: str\n    harga: int\n    tag: list = field(default_factory=list)\n\n@dataclass(frozen=True)\nclass Titik:\n    x: int\n    y: int\n\np = Produk(\"Kopi Gayo\", 85000)\nprint(p)\nprint(p == Produk(\"Kopi Gayo\", 85000))\nt = Titik(1, 2)\ntry:\n    t.x = 5\nexcept Exception as e:\n    print(type(e).__name__)",
"err": "File \"main.py\", line 20\n    print(r.saldo\nSyntaxError: '(' was never closed",
"line": 20,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Dunder method: membuat objek terasa bawaan": {
"code": "class Uang:\n    def __init__(self, rupiah):\n        self.rupiah = rupiah\n    def __str__(self):\n        return f\"Rp{self.rupiah:,}\".replace(\",\", \".\")\n    def __repr__(self):\n        return f\"Uang({self.rupiah})\"\n    def __add__(self, lain):\n        return Uang(self.rupiah + lain.rupiah)\n    def __eq__(self, lain):\n        return self.rupiah == lain.rupiah\n    def __lt__(self, lain):\n        return self.rupiah < lain.rupiah\n\nclass Keranjang:\n    def __init__(self):\n        self.isi = []\n    def tambah(self, nama, harga):\n        self.isi.append((nama, Uang(harga)))\n    def __len__(self):\n        return len(self.isi)\n    def __getitem__(self, i):\n        return self.isi[i]\n    def __iter__(self):\n        return iter(self.isi)\n\nk = Keranjang()\nk.tambah(\"kopi\", 85000)\nk.tambah(\"teh\", 25000)\nprint(len(k), k[1][0]\ntotal = Uang(0)\nfor nama, harga in k:\n    total = total + harga\nprint(total)\nprint(sorted([Uang(5), Uang(2), Uang(9)]))\nprint(Uang(100) == Uang(100))",
"err": "File \"main.py\", line 30\n    print(len(k), k[1][0]\nSyntaxError: '(' was never closed",
"line": 30,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Paradigma: prosedural, OOP, fungsional": {
"code": "belanja = [(\"kopi\", 85000), (\"keripik\", 15000), (\"madu\", 120000)]\n\n# 1. Prosedural\ntotal = 0\nfor nama, harga in belanja\n    if harga > 20000:\n        total += harga\nprint(\"prosedural:\", total)\n\n# 2. Berorientasi objek\nclass Keranjang:\n    def __init__(self, isi):\n        self.isi = isi\n    def total_di_atas(self, batas):\n        return sum(h for _, h in self.isi if h > batas)\nprint(\"OOP:\", Keranjang(belanja).total_di_atas(20000))\n\n# 3. Fungsional\nfrom functools import reduce\nmahal = filter(lambda b: b[1] > 20000, belanja)\nprint(\"fungsional:\", reduce(lambda a, b: a + b, map(lambda b: b[1], mahal), 0))",
"err": "File \"main.py\", line 5\n    for nama, harga in belanja\nSyntaxError: expected ':'",
"line": 5,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:List, dict & set comprehension": {
"code": "harga = {\"kopi\": 85000, \"teh\": 25000, \"keripik\": 15000, \"madu\": 120000}\n\nkuadrat = [n * n for n in range(1, 6)]\nprint(kuadrat)\n\nmahal = [nama for nama, h in hrga.items() if h > 50000]\nprint(mahal)\n\ndiskon = {nama: h * 9 // 10 for nama, h in harga.items()}\nprint(diskon[\"kopi\"])\n\nhuruf_awal = {nama[0] for nama in harga}\nprint(sorted(huruf_awal))\n\nlabel = [\"genap\" if n % 2 == 0 else \"ganjil\" for n in range(4)]\nprint(label)\n\nmatriks = [[1, 2, 3], [4, 5, 6]]\nprint([x for baris in matriks for x in baris])",
"err": "File \"main.py\", line 6, in <module>\n    mahal = [nama for nama, h in hrga.items() if h > 50000]\nNameError: name 'hrga' is not defined. Did you mean: 'harga'?",
"line": 6,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:Iterator & generator": {
"code": "import sys\n\ndef hitung_mundur(n):\n    print(\"mulai\"\n    while n > 0:\n        yield n\n        n -= 1\n    print(\"habis\")\n\ng = hitung_mundur(3)\nprint(next(g))\nprint(next(g))\nfor x in g:\n    print(\"loop\", x)\n\ndef fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n\nfib = fibonacci()\nprint([next(fib) for _ in range(8)])\n\ndaftar = [x * x for x in range(100_000)]\ngen = (x * x for x in range(100_000))\nprint(sys.getsizeof(daftar) > 100_000, sys.getsizeof(gen) < 1000)\nprint(sum(gen))",
"err": "File \"main.py\", line 4\n    print(\"mulai\"\nSyntaxError: '(' was never closed",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Decorator": {
"code": "import functools, time\n\ndef catat(fungsi)\n    @functools.wraps(fungsi)\n    def pembungkus(*args, **kwargs):\n        print(f\"-> {fungsi.__name__}{args}\")\n        hasil = fungsi(*args, **kwargs)\n        print(f\"<- {hasil}\")\n        return hasil\n    return pembungkus\n\ndef ulangi(n):                      # decorator dengan parameter\n    def dekor(fungsi):\n        @functools.wraps(fungsi)\n        def pembungkus(*args):\n            return [fungsi(*args) for _ in range(n)]\n        return pembungkus\n    return dekor\n\n@catat\ndef bayar(harga, diskon=0):\n    return harga - diskon\n\nbayar(85000, 5000)\nprint(bayar.__name__)\n\n@ulangi(3)\ndef sapa(nama):\n    return f\"hai {nama}\"\nprint(sapa(\"Rina\"))\n\n@functools.lru_cache\ndef fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)\nprint(fib(80))",
"err": "File \"main.py\", line 3\n    def catat(fungsi)\nSyntaxError: expected ':'",
"line": 3,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:Regular expression (modul re)": {
"code": "import re\n\nteks = \"Hubungi 0812-3456-7890 atau 0857-1111-2222 sebelum 28/10/2024\"\nprint(re.findall(r\"\\d{4}-\\d{4}-\\d{4}\", tks))\n\nm = re.search(r\"(?P<tgl>\\d{2})/(?P<bln>\\d{2})/(?P<thn>\\d{4})\", teks)\nprint(m.group(\"thn\"), m.group(\"bln\"))\n\nprint(re.sub(r\"(\\d{2})/(\\d{2})/(\\d{4})\", r\"\\3-\\2-\\1\", teks)[-10:])\n\nemail = \"rina@kampus.ac.id\"\nprint(bool(re.fullmatch(r\"[\\w.]+@[\\w.]+\\.[a-z]{2,}\", email)))\n\nprint(re.split(r\"\\s*[,;]\\s*\", \"kopi , teh;madu\"))",
"err": "File \"main.py\", line 4, in <module>\n    print(re.findall(r\"\\d{4}-\\d{4}-\\d{4}\", tks))\nNameError: name 'tks' is not defined. Did you mean: 'teks'?",
"line": 4,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:deque, heapq & bisect: struktur data siap pakai": {
"code": "from collections import deque\nimport heapq, bisect\n\nantre = deque([\"Ani\", \"Bayu\"])\nantre.append(\"Citra\")\nantre.appendleft(\"VIP\")\nprint(antre.popleft(), list(antre)\n\nriwayat = deque(maxlen=3)\nfor hal in [\"beranda\", \"produk\", \"keranjang\", \"bayar\"]:\n    riwayat.append(hal)\nprint(list(riwayat))\n\ntugas = []\nheapq.heappush(tugas, (2, \"balas email\"))\nheapq.heappush(tugas, (1, \"server mati\"))\nheapq.heappush(tugas, (3, \"rapat\"))\nprint(heapq.heappop(tugas))\nprint(heapq.nlargest(2, [70, 95, 88, 60, 91]))\n\nnilai = [55, 70, 85, 90]\nprint(bisect.bisect_left(nilai, 80))\nbisect.insort(nilai, 80)\nprint(nilai)",
"err": "File \"main.py\", line 7\n    print(antre.popleft(), list(antre)\nSyntaxError: '(' was never closed",
"line": 7,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Anotasi tipe & modul typing": {
"code": "from typing import Callable, Literal, TypedDict, TypeVar\n\nT = TypeVar(\"T\")\n\nclass Produk(TypedDict)\n    nama: str\n    harga: int\n\nStatus = Literal[\"baru\", \"dikirim\", \"selesai\"]\n\ndef termahal(data: list[Produk]) -> Produk | None:\n    return max(data, key=lambda p: p[\"harga\"]) if data else None\n\ndef terapkan(f: Callable[[int], int], nilai: list[int]) -> list[int]:\n    return [f(x) for x in nilai]\n\ndef pertama(xs: list[T]) -> T:\n    return xs[0]\n\ndef ubah_status(s: Status) -> str:\n    return s.upper()\n\nkatalog: list[Produk] = [{\"nama\": \"Kopi\", \"harga\": 85000}, {\"nama\": \"Teh\", \"harga\": 25000}]\nprint(termahal(katalog))\nprint(terapkan(lambda x: x * 2, [1, 2, 3]))\nprint(pertama([\"a\", \"b\"]), ubah_status(\"dikirim\"))\nprint(termahal.__annotations__[\"return\"])",
"err": "File \"main.py\", line 5\n    class Produk(TypedDict)\nSyntaxError: expected ':'",
"line": 5,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:Docstring, komentar & Sphinx": {
"code": "def hitung_ongkir(berat_kg: float, kota: str) -> int:\n    \"\"\"Menghitung ongkos kirim dalam rupiah.\n\n    Tarif dasar Rp10.000 per kg, ditambah biaya luar Jawa.\n\n    Args:\n        berat_kg: Berat paket dalam kilogram, harus lebih dari 0.\n        kota: Kota tujuan.\n\n    Returns:\n        Ongkos kirim yang dibulatkan ke atas per kilogram.\n\n    Raises:\n        ValueError: Jika berat tidak positif.\n    \"\"\"\n    if berat_kg <= 0:\n        raise ValueError(\"berat harus positif\")\n    # dibulatkan ke atas karena kurir menghitung per kg penuh\n    kg = -(-berat_kg // 1)\n    tambahan = 15000 if kota not in {\"Jakarta\", \"Bandung\", \"Surabaya\"} else 0\n    return int(kg * 10000 + tambahn)\n\nprint(hitung_ongkir(2.3, \"Medan\"))\nprint(hitung_ongkir.__doc__.splitlines()[0])",
"err": "File \"main.py\", line 23, in <module>\n    print(hitung_ongkir(2.3, \"Medan\"))\n  File \"main.py\", line 21, in hitung_ongkir\n    return int(kg * 10000 + tambahn)\nNameError: name 'tambahn' is not defined. Did you mean: 'tambahan'?",
"line": 21,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:unittest, doctest & tox": {
"code": "import unittest\n\ndef rupiah(n):\n    \"\"\"Format angka menjadi rupiah.\n\n    >>> rupiah(1500000)\n    'Rp1.500.000'\n    >>> rupiah(0)\n    'Rp0'\n    \"\"\"\n    return f\"Rp{n:,}\".replace(\",\", \".\")\n\nclass TesRupiah(unittest.TestCase):\n    def test_ribuan(self):\n        self.assertEqual(rupiah(85000), \"Rp85.000\")\n    def test_tipe(self):\n        self.assertIsInstance(rupiah(1), str)\n\nif __name__ == \"__main__\":\n    import doctest, io, contextlib\n    hasil = doctest.testmod()\n    print(\"doctest gagal:\", hasil.failed, \"dari\", hasil.attempted\n    buf = io.StringIO()\n    with contextlib.redirect_stderr(buf):\n        r = unittest.main(exit=False).result\n    print(\"unittest jalan:\", r.testsRun, \"gagal:\", len(r.failures))",
"err": "File \"main.py\", line 22\n    print(\"doctest gagal:\", hasil.failed, \"dari\", hasil.attempted\nSyntaxError: '(' was never closed",
"line": 22,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"python:Threading & GIL": {
"code": "import threading, time\nfrom concurrent.futures import ThreadPoolExecutor\n\ndef unduh(nama)\n    time.sleep(0.5)                  # pura-pura menunggu jaringan\n    return f\"{nama} selesai\"\n\nmulai = time.perf_counter()\nwith ThreadPoolExecutor(max_workers=5) as ex:\n    hasil = list(ex.map(unduh, [\"a.jpg\", \"b.jpg\", \"c.jpg\", \"d.jpg\", \"e.jpg\"]))\nprint(hasil[0], \"| 5 unduhan dalam\", round(time.perf_counter() - mulai, 1), \"detik\")\n\nsaldo = 0\nkunci = threading.Lock()\ndef setor():\n    global saldo\n    for _ in range(100_000):\n        with kunci:                  # bagian kritis\n            saldo += 1\n\nts = [threading.Thread(target=setor) for _ in range(4)]\nfor t in ts: t.start()\nfor t in ts: t.join()\nprint(\"saldo:\", saldo)",
"err": "File \"main.py\", line 4\n    def unduh(nama)\nSyntaxError: expected ':'",
"line": 4,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"python:Multiprocessing": {
"code": "from concurrent.futures import ProcessPoolExecutor\nimport math, os\n\ndef jumlah_prima(batas):\n    return sum(1 for n in range(2, batas) if all(n % d for d in range(2, int(math.isqrt(n)) + 1)))\n\nif __name__ == \"__main__\":\n    tugas = [50_000, 60_000, 70_000, 80_000]\n    with ProcessPoolExecutor() as ex:\n        hasil = list(ex.map(jumlah_prima, tugs))\n    print(hasil)\n    print(\"inti CPU tersedia:\", os.cpu_count() is not None)",
"err": "File \"main.py\", line 10, in <module>\n    hasil = list(ex.map(jumlah_prima, tugs))\nNameError: name 'tugs' is not defined. Did you mean: 'tugas'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"python:asyncio, async/await & gevent": {
"code": "import asyncio, time\n\nasync def ambil(nama, detik):\n    print(f\"mulai {nama}\"\n    await asyncio.sleep(detik)        # menunggu tanpa memblokir\n    print(f\"selesai {nama}\")\n    return f\"{nama}:{detik}s\"\n\nasync def main():\n    mulai = time.perf_counter()\n    hasil = await asyncio.gather(\n        ambil(\"cuaca\", 0.3),\n        ambil(\"kurs\", 0.1),\n        ambil(\"berita\", 0.2),\n    )\n    print(hasil)\n    print(\"total sekitar\", round(time.perf_counter() - mulai, 1), \"detik\")\n\nasyncio.run(main())",
"err": "File \"main.py\", line 4\n    print(f\"mulai {nama}\"\nSyntaxError: '(' was never closed",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Kenapa TypeScript?": {
"code": "function totalHarga(harga: number, jumlah: number): number {\n  return harga * jumlah;\n}\n\nvar produk = { nama: \"Kopi Gayo\", harga: 85000 };\nconsole.log(totalHarga(produk.harga, 2);\n// totalHarga(\"85000\", 2);   // error: Argument of type 'string' is not assignable to parameter of type 'number'.",
"err": "main.ts(6,40): error TS1005: ')' expected.",
"line": 6,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Primitif, array & tuple": {
"code": "let stok = 40;                      // ditebak: number\nvar nama: string = \"Kopi Gayo\";\nvar aktif: boolean = true;\nvar kategori: string[] = [\"Minuman\", \"Camilan\"];\nvar item: [string, number] = [\"Teh Melati\", 25000];\n\nvar [n, h] = item;\nconsole.log(nama, stok, aktif;\nconsole.log(kategori.length, n, h);\n// stok = \"banyak\";   // error: Type 'string' is not assignable to type 'number'.",
"err": "main.ts(8,30): error TS1005: ')' expected.",
"line": 8,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Objek, literal & enum": {
"code": "type Status = \"baru\" | \"dikirim\" | \"selesai\";\n\nvar pesanan: { id: number; status: Status; catatan?: string } = {\n  id: 101,\n  status: \"dikirim\",\n};\n\nenum Kurir { JNE = \"jne\", JNT = \"jnt\", SiCepat = \"sicepat\" }\n\nconsole.log(pesanan.id, pesanan.status, pesanan.catatan ?? \"tanpa catatan\";\nconsole.log(Kurir.SiCepat, Object.keys(Kurir).length);\n// pesanan.status = \"hilang\";  // error: Type '\"hilang\"' is not assignable to type 'Status'.",
"err": "main.ts(10,75): error TS1005: ')' expected.",
"line": 10,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:any, unknown, never & void": {
"code": "function cetak(pesan: string): void {\n  console.log(\"LOG:\", pesan;\n}\n\nfunction gagal(pesan: string): never {\n  throw new Error(pesan);\n}\n\nfunction panjang(x: unknown): number {\n  if (typeof x === \"string\") return x.length;     // aman setelah diperiksa\n  if (Array.isArray(x)) return x.length;\n  return 0;\n}\n\ncetak(\"mulai\");\nconsole.log(panjang(\"halo\"), panjang([1, 2, 3]), panjang(42));\ntry { gagal(\"stok habis\"); } catch (e) { console.log((e as Error).message); }",
"err": "main.ts(2,28): error TS1005: ')' expected.",
"line": 2,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Menulis tipe fungsi": {
"code": "type Diskon = (harga: number) => number;\n\nvar potong10: Diskon = h => h * 0.9;\nvar potong20: Diskon = h => h * 0.8;\n\nfunction bayar(harga: number, diskon?: Diskon, ongkir = 15000): number {\n  const setelah = diskon ? diskon(harga) : harga;\n  return setelh + ongkir;\n}\n\nfunction jumlahkan(...angka: number[]): number {\n  return angka.reduce((a, b) => a + b, 0);\n}\n\nconsole.log(bayar(100000));\nconsole.log(bayar(100000, potong20, 0));\nconsole.log(jumlahkan(85000, 25000, 15000));",
"err": "main.ts(8,10): error TS2552: Cannot find name 'setelh'. Did you mean 'setelah'?",
"line": 8,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"ts:Overload fungsi": {
"code": "function format(nilai: number): string;\nfunction format(nilai: Date): string;\nfunction format(nilai: number | Date): string {\n  if (typeof nilai === \"number\") return \"Rp\" + nilai.toLocaleString(\"id-ID\");\n  return nilai.toISOString().slice(0, 10);\n}\n\nconsole.log(format(85000);\nconsole.log(format(new Date(\"2024-10-01T00:00:00Z\")));",
"err": "main.ts(8,26): error TS1005: ')' expected.",
"line": 8,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Fungsi orde tinggi & callback bertipe": {
"code": "type Aturan = (harga: number) => number;\n\nconst diskon = (persen: number): Aturan => (harga) => harga * (1 - persen / 100);\nconst ongkir = (biaya: number): Aturan => (harga) => harga + biaya;\n\nfunction terapkan(harga: number, ...aturan: Aturan[]): number {\n  return aturan.reduce((h, f) => f(h), harga);\n}\n\nconsole.log(terapkan(100_000, diskn(10), ongkir(15_000)));\nconsole.log(terapkan(100_000, ongkir(15_000), diskon(10)));\nconst hargaAkhir = [50_000, 80_000].map(diskon(20));\nconsole.log(hargaAkhir);",
"err": "main.ts(10,31): error TS2552: Cannot find name 'diskn'. Did you mean 'diskon'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"ts:Interface & extends": {
"code": "interface Produk {\n  id: number;\n  nama: string;\n  harga: number;\n}\n\ninterface ProdukDigital extends Produk {\n  urlUnduh: string;\n  hitungDiskon(persen: number): number;\n}\n\nvar ebook: ProdukDigital = {\n  id: 9, nama: \"E-book Resep Kopi\", harga: 49000, urlUnduh: \"https://contoh.id/resep.pdf\",\n  hitungDiskon(p) { return this.harga * (1 - p / 100); },\n};\n\nfunction label(p: Produk): string {        // ProdukDigital juga diterima\n  return `#${p.id} ${p.nama}`;\n}\nconsole.log(label(ebook), ebook.hitungDiskon(10);",
"err": "main.ts(20,49): error TS1005: ')' expected.",
"line": 20,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Type alias, union & intersection": {
"code": "type Id = number | string;\ntype Bertanggal = { dibuat: string };\ntype Pelanggan = { id: Id; nama: string } & Bertanggal;\n\nvar a: Pelanggan = { id: 1, nama: \"Andi\", dibuat: \"2023-01-15\" };\nvar b: Pelanggan = { id: \"PLG-008\", nama: \"Hadi\", dibuat: \"2024-09-03\" };\n\nfunction tampil(id: Id): string {\n  return typeof id === \"number\" ? id.toString().padStart(4, \"0\") : id;\n}\nconsole.log(tampil(a.id), tampil(b.id), b.dibuat;",
"err": "main.ts(11,49): error TS1005: ')' expected.",
"line": 11,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Type guard & discriminated union": {
"code": "type Bayar =\n  | { jenis: \"qris\"; merchant: string }\n  | { jenis: \"va\"; bank: string; nomor: string }\n  | { jenis: \"cod\" };\n\nfunction keterangan(b: Bayar): string {\n  switch (b.jenis) {\n    case \"qris\": return \"QRIS \" + b.merchant;\n    case \"va\": return `VA ${b.bank} ${b.nomor}`;\n    case \"cod\": return \"Bayar di tempat\";\n    default: { const cek: never = b; return cek; }\n  }\n}\n\nvar adalahVA = (b: Bayar): b is Extract<Bayar, { jenis: \"va\" }> => b.jenis === \"va\";\n\nvar daftar: Bayar[] = [{ jenis: \"qris\", merchant: \"Toko Nusantara\" }, { jenis: \"va\", bank: \"BCA\", nomor: \"8808\" }, { jenis: \"cod\" }];\ndaftar.forEach(b => console.log(keterangan(b)));\nconsole.log(daftar.filter(adalahVA).map(b => b.bank);",
"err": "main.ts(19,53): error TS1005: ')' expected.",
"line": 19,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:as, as const, ! & satisfies": {
"code": "const KATEGORI = [\"Minuman\", \"Camilan\", \"Bumbu\"] as const;\ntype Kategori = typeof KATEGORI[number];          // \"Minuman\" | \"Camilan\" | \"Bumbu\"\n\nvar warna = {\n  Minuman: \"#2E5E8C\",\n  Camilan: \"#B4532A\",\n  Bumbu: \"#2F7A52\",\n} satisfies Record<Kategori, string>;\n\nvar k: Kategori = \"Camilan\";\nconsole.log(k, warna[k], KATEGORI.length;\nvar data = JSON.parse('{\"nama\":\"Kopi\"}') as { nama: string };\nconsole.log(data.nama.toUpperCase());",
"err": "main.ts(11,41): error TS1005: ')' expected.",
"line": 11,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Validasi data dari API dengan type predicate": {
"code": "type Produk = { nama: string; harga: number };\n\nfunction isProduk(x: unknown): x is Produk {\n  return typeof x === \"object\" && x !== null\n    && typeof (x as Produk).nama === \"string\"\n    && typeof (x as Produk).harga === \"number\";\n}\n\nconst dariServer: unknown = JSON.parse(\n  '[{\"nama\":\"Kopi\",\"harga\":85000},{\"nama\":\"Teh\",\"harga\":\"25rb\"},null]'\n);\nconst daftar = Array.isArray(dariServer) ? dariServer.filter(isProduk) : [];\nconsole.log(daftar.length, \"produk valid\";\nfor (const p of daftar) console.log(p.nama, p.harga * 2);",
"err": "main.ts(13,42): error TS1005: ')' expected.",
"line": 13,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Kelas & modifier akses": {
"code": "class Rekening {\n  #riwayat: string[] = [];\n  constructor(public readonly pemilik: string, private saldo: number) {}\n\n  setor(n: number): void {\n    this.saldo += n;\n    this.#riwayat.push(\"setor \" + n);\n  }\n  tarik(n: number): boolean {\n    if (n > this.saldo) return false;\n    this.saldo -= n;\n    this.#riwayat.push(\"tarik \" + n);\n    return true;\n  }\n  get info(): string { return `${this.pemilik}: ${this.saldo} (${this.#riwayat.length} transaksi)`; }\n}\n\nvar r = new Rekening(\"Andi\", 500000);\nr.setor(100000);\nconsole.log(r.tarik(900000), r.tarik(200000);\nconsole.log(r.info);\n// r.saldo = 0;   // error: Property 'saldo' is private and only accessible within class 'Rekening'.",
"err": "main.ts(20,45): error TS1005: ')' expected.",
"line": 20,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Fungsi & tipe generik": {
"code": "function pertama<T>(arr: T[]): T | undefined {\n  return arr[0];\n}\n\nfunction cariById<T extends { id: number }>(daftar: T[], id: number): T | undefined {\n  return daftar.find(x => x.id === id);\n}\n\ntype Hasil<T> = { ok: true; data: T } | { ok: false; error: string };\n\nfunction bagi(a: number, b: number): Hasil<number> {\n  return b === 0 ? { ok: false, error: \"pembagi nol\" } : { ok: true, data: a / b };\n}\n\nvar produk = [{ id: 1, nama: \"Kopi\" }, { id: 2, nama: \"Teh\" }];\nconsole.log(pertama([\"a\", \"b\"]), pertama([10, 20]);\nconsole.log(cariById(produk, 2)?.nama);\nvar h = bagi(10, 0);\nconsole.log(h.ok ? h.data : h.error);",
"err": "main.ts(16,51): error TS1005: ')' expected.",
"line": 16,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Constraint generik & tipe bawaan": {
"code": "function termahal<T extends { harga: number }>(daftar: T[]): T {\n  return daftar.reduce((a, b) => (b.harga > a.harga ? b : a));\n}\n\nfunction ambil<T, K extends keyof T>(obj: T, kunci: K): T[K] {\n  return obj[kunci];\n}\n\ntype Respons<T = string> = { ok: boolean; data: T };\n\nconst produk = [\n  { nama: \"Kopi Gayo\", harga: 85_000, stok: 40 },\n  { nama: \"Madu Hutan\", harga: 120_000, stok: 15 },\n];\nconst teratas = termahal(produk);\nconsole.log(teratas.nama;          // tipe teratas: { nama, harga, stok }\nconsole.log(ambil(teratas, \"stok\")); // ambil(teratas, \"warna\") ditolak compiler\nconst r: Respons = { ok: true, data: \"tersimpan\" };\nconsole.log(r.data.toUpperCase());",
"err": "main.ts(16,25): error TS1005: ')' expected.",
"line": 16,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Partial, Pick, Omit, Readonly & Record": {
"code": "interface Produk { id: number; nama: string; harga: number; stok: number }\n\ntype UbahProduk = Partial<Omit<Produk, \"id\">>;\ntype Ringkas = Pick<Produk, \"nama\" | \"harga\">;\ntype StokPerKota = Record<\"Jakarta\" | \"Bandung\", number>;\n\nfunction ubah(p: Produk, perubahan: UbahProduk): Produk {\n  return { ...p, ...perubahan };\n}\n\nvar kopi: Readonly<Produk> = { id: 1, nama: \"Kopi Gayo\", harga: 85000, stok: 40 };\nvar baru = ubah(kopi, { harga: 80000 });\nvar r: Ringkas = { nama: baru.nama, harga: baru.harga };\nvar stok: StokPerKota = { Jakarta: 25, Bandung: 15 };\nconsole.log(r, stok.Bandung;\n// kopi.harga = 1;   // error: Cannot assign to 'harga' because it is a read-only property.",
"err": "main.ts(15,28): error TS1005: ')' expected.",
"line": 15,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:keyof, mapped & conditional types": {
"code": "function ambil<T, K extends keyof T>(obj: T, kunci: K): T[K] {\n  return obj[kunci];\n}\n\ntype Opsional<T> = { [K in keyof T]?: T[K] };\ntype JadiString<T> = { [K in keyof T]: string };\ntype IsiArray<T> = T extends (infer E)[] ? E : never;\n\nvar p = { nama: \"Kopi Gayo\", harga: 85000 };\nvar h = ambil(p, \"harga\");                 // number\nvar form: JadiString<typeof p> = { nama: \"Kopi Gayo\", harga: \"85000\" };\nvar draf: Opsional<typeof p> = { nama: \"Draf\" };\ntype X = IsiArray<string[]>;                 // string\nvar x: X = \"ok\";\nconsole.log(h + 1, form.harga + \"!\", draf.harga ?? \"-\", x;",
"err": "main.ts(15,58): error TS1005: ')' expected.",
"line": 15,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Template literal & tipe rekursif": {
"code": "type Peristiwa = \"klik\" | \"ubah\";\ntype Handler = `on${Capitalize<Peristiwa>}`;      // \"onKlik\" | \"onUbah\"\n\ntype Kategori = { nama: string; anak?: Kategori[] };\nvar pohon: Kategori = { nama: \"Minuman\", anak: [{ nama: \"Kopi\", anak: [{ nama: \"Arabika\" }] }, { nama: \"Teh\" }] };\n\nfunction hitung(k: Kategori): number {\n  return 1 + (k.anak ?? []).reduce((n, a) => n + hitung(a), 0);\n}\n\nvar h: Handler = \"onKlik\";\nconsole.log(h, hitung(pohon);",
"err": "main.ts(12,29): error TS1005: ')' expected.",
"line": 12,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"ts:Decorator & alat ekosistem": {
"code": "function catat(asli: any, konteks: ClassMethodDecoratorContext) {\n  return function (this: unknown, ...args: unknown[]) {\n    console.log(`panggil ${String(konteks.name)}(${args.join(\", \")})`;\n    return asli.apply(this, args);\n  };\n}\n\nclass Kasir {\n  @catat\n  bayar(total: number, uang: number) { return uang - total; }\n}\n\nconsole.log(\"kembalian\", new Kasir().bayar(85000, 100000));",
"err": "main.ts(3,70): error TS1005: ')' expected.",
"line": 3,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"fe0:Perulangan: for, for...of & while": {
"code": "const keranjang = [\"kopi\", \"teh\", \"gula\"];\n\nfor (let i = 0; i < keranjang.length; i++) {\n  console.log(`${i + 1}. ${keranjang[i]}`;\n}\n\nfor (const barang of keranjang) {\n  if (barang === \"teh\") continue;\n  console.log(\"dikemas:\", barang);\n}\n\nlet tabungan = 0;\nlet minggu = 0;\nwhile (tabungan < 100_000) {\n  tabungan += 30_000;\n  minggu++;\n}\nconsole.log(`Target tercapai di minggu ke-${minggu}: Rp${tabungan}`);",
"err": "main.js:4\n  console.log(`${i + 1}. ${keranjang[i]}`;\n                                       ^^\nSyntaxError: missing ) after argument list",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"fe0:Menangani error dengan try...catch": {
"code": "function bacaKeranjang(teks) {\n  try {\n    const data = JSON.parse(teks);\n    if (!Array.isArray(data)) throw new Error(\"format keranjang salah\");\n    return data;\n  } catch (err) {\n    console.log(\"Gagal membaca keranjang:\", err.message;\n    return [];\n  } finally {\n    console.log(\"selesai memeriksa\");\n  }\n}\n\nconsole.log(bacaKeranjang('[\"kopi\",\"teh\"]'));\nconsole.log(bacaKeranjang(\"{rusak\"));\nconsole.log(bacaKeranjang('{\"kopi\": 1}'));",
"err": "main.js:7\n    console.log(\"Gagal membaca keranjang:\", err.message;\n                                                ^^^^^^^\nSyntaxError: missing ) after argument list",
"line": 7,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"fe:Closure: fungsi yang mengingat": {
"code": "function buatKeranjang() {\n  let isi = [];                       // privat, tidak bisa diakses langsung\n  return {\n    tambah(barang) { isi.push(barang); return isi.length; },\n    lihat() { return [...isi]; },\n  };\n}\nconst k = buatKeranjang();\nk.tambah(\"kopi\");\nk.tambah(\"teh\");\nconsole.log(k.lihat(), k.isi;\n\nconst pakaiVar = [], pakaiLet = [];\nfor (var i = 0; i < 3; i++) pakaiVar.push(() => i);\nfor (let j = 0; j < 3; j++) pakaiLet.push(() => j);\nconsole.log(pakaiVar.map((f) => f()), pakaiLet.map((f) => f()));",
"err": "main.js:11\nconsole.log(k.lihat(), k.isi;\n                         ^^^\nSyntaxError: missing ) after argument list",
"line": 11,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"fe:Debounce & throttle": {
"code": "function debounce(fn, ms) {\n  let t;\n  return (...args) => {\n    clearTimeout(t);\n    t = setTimeout(() => fn(...args), ms);\n  };\n}\n\nconst panggilan = [];\nconst cari = debounce((kata) => {\n  panggiln.push(kata);\n  console.log(\"cari ke server:\", kata);\n}, 300);\n\n[\"k\", \"ko\", \"kop\", \"kopi\", \"kopi g\"].forEach((kata, i) => setTimeout(() => cari(kata), i * 50));\nsetTimeout(() => console.log(\"jumlah panggilan:\", panggilan.length), 700);",
"err": "main.js:11\n  panggiln.push(kata);\n  ^\nReferenceError: panggiln is not defined",
"line": 11,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Membaca file besar per potongan": {
"code": "import pandas as pd, io\ncsv = \"kota,total\\n\" + \"\\n\".join(f\"{k},{t}\" for k, t in\n       [(\"Medan\", 120), (\"Bandung\", 90), (\"Medan\", 45), (\"Ambon\", 70), (\"Bandung\", 30), (\"Medan\", 60), (\"Ambon\", 25)])\n\nbagian = []\nfor potongan in pd.read_csv(io.StringIO(csv), chunksize=3, usecols=[\"kota\", \"total\"]):\n    print(\"potongan\", len(potongan), \"baris\")\n    bagin.append(potongan.groupby(\"kota\")[\"total\"].sum())\n\nhasil = pd.concat(bagian).groupby(level=0).sum()\nprint(hasil.to_dict())",
"err": "File \"main.py\", line 8, in <module>\n    bagin.append(potongan.groupby(\"kota\")[\"total\"].sum())\nNameError: name 'bagin' is not defined. Did you mean: 'bagian'?",
"line": 8,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Array NumPy & operasi vektor": {
"code": "import numpy as np\n\nharga = np.array([85000, 25000, 15000, 120000])\njumlah = np.array([3, 10, 25, 1])\n\nomzet = harga * jumlah          # per elemen, tanpa for\nprint(omzet\nprint(\"total:\", omzet.sum())\n\ndiskon = 0.1\nprint(harga * (1 - diskon))\n\nstok = np.array([[40, 120], [200, 15]])\nprint(stok.shape, stok.ndim, stok.dtype)\nprint(stok + np.array([10, 0]))  # broadcasting per kolom",
"err": "File \"main.py\", line 7\n    print(omzet\nSyntaxError: '(' was never closed",
"line": 7,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:Indexing, boolean mask & statistik": {
"code": "import numpy as np\n\nharga = np.array([85000, 25000, 15000, 60000, 30000, 120000, 75000, 20000])\nprint(hrga[harga > 50000])\nprint(harga[(harga >= 20000) & (harga <= 60000)])\nprint(\"rata-rata:\", harga.mean(), \"median:\", np.median(harga))\nprint(\"p75:\", np.percentile(harga, 75))\n\nrng = np.random.default_rng(42)\nsampel = rng.integers(1, 7, size=10)   # 10 lemparan dadu\nprint(sampel)",
"err": "File \"main.py\", line 4, in <module>\n    print(hrga[harga > 50000])\nNameError: name 'hrga' is not defined. Did you mean: 'harga'?",
"line": 4,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Series & DataFrame": {
"code": "import pandas as pd\npenjualan = pd.DataFrame({\n    \"tanggal\": [\"2024-10-01\",\"2024-10-01\",\"2024-10-02\",\"2024-10-03\",\"2024-10-03\",\"2024-10-04\",\"2024-10-05\",\"2024-10-05\"],\n    \"kota\": [\"Jakarta\",\"Bandung\",\"Jakarta\",\"Surabaya\",\"Bandung\",\"Jakarta\",\"Medan\",\"Surabaya\"],\n    \"produk\": [\"Kopi Gayo\",\"Teh Melati\",\"Keripik\",\"Kopi Gayo\",\"Madu Hutan\",\"Teh Melati\",\"Kopi Gayo\",\"Keripik\"],\n    \"jumlah\": [3, 10, 25, 2, 1, 6, 4, 30],\n    \"harga\": [85000, 25000, 15000, 85000, 120000, 25000, 85000, 15000],\n})\n\nprint(penjualn.head(3))\nprint(penjualan.shape)\n\npenjualan[\"omzet\"] = penjualan[\"jumlah\"] * penjualan[\"harga\"]\nprint(penjualan[\"omzet\"].describe().round(0))",
"err": "File \"main.py\", line 10, in <module>\n    print(penjualn.head(3))\nNameError: name 'penjualn' is not defined. Did you mean: 'penjualan'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Membaca CSV, Excel, JSON & web": {
"code": "import io\nimport pandas as pd\n\ncsv = \"\"\"tanggal;kota;omzet\n2024-10-01;Jakarta;255000,5\n2024-10-02;Bandung;250000\n2024-10-03;Surabaya;170000\"\"\"\n\ndf = pd.read_csv(io.StringIO(csv), sep=\";\", decimal=\",\", parse_dates=[\"tanggal\"])\nprint(df\nprint(df[\"tanggal\"].dt.day_name().tolist())\n\ndata_api = [{\"id\": 1, \"kota\": {\"nama\": \"Medan\", \"prov\": \"Sumut\"}},\n            {\"id\": 2, \"kota\": {\"nama\": \"Bogor\", \"prov\": \"Jabar\"}}]\nprint(pd.json_normalize(data_api))",
"err": "File \"main.py\", line 10\n    print(df\nSyntaxError: '(' was never closed",
"line": 10,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:Memilih & menyaring: loc, iloc, query": {
"code": "import pandas as pd\npenjualan = pd.DataFrame({\n    \"tanggal\": [\"2024-10-01\",\"2024-10-01\",\"2024-10-02\",\"2024-10-03\",\"2024-10-03\",\"2024-10-04\",\"2024-10-05\",\"2024-10-05\"],\n    \"kota\": [\"Jakarta\",\"Bandung\",\"Jakarta\",\"Surabaya\",\"Bandung\",\"Jakarta\",\"Medan\",\"Surabaya\"],\n    \"produk\": [\"Kopi Gayo\",\"Teh Melati\",\"Keripik\",\"Kopi Gayo\",\"Madu Hutan\",\"Teh Melati\",\"Kopi Gayo\",\"Keripik\"],\n    \"jumlah\": [3, 10, 25, 2, 1, 6, 4, 30],\n    \"harga\": [85000, 25000, 15000, 85000, 120000, 25000, 85000, 15000],\n})\n\nprint(penjualn.loc[penjualan[\"kota\"] == \"Jakarta\", [\"produk\", \"jumlah\"]])\nprint(penjualan.iloc[0:2, 1:3])\nprint(penjualan.query(\"jumlah >= 10\")[[\"kota\", \"produk\", \"jumlah\"]])\nprint(penjualan[penjualan[\"produk\"].isin([\"Madu Hutan\", \"Keripik\"])].shape[0])",
"err": "File \"main.py\", line 10, in <module>\n    print(penjualn.loc[penjualan[\"kota\"] == \"Jakarta\", [\"produk\", \"jumlah\"]])\nNameError: name 'penjualn' is not defined. Did you mean: 'penjualan'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Nilai hilang: isna, dropna, fillna, ffill": {
"code": "import pandas as pd\nimport numpy as np\n\ndf = pd.DataFrame({\n    \"kota\": [\"Jakarta\", None, \"Bandung\", \"Medan\", None],\n    \"umur\": [24, 31, np.nan, 45, 29],\n    \"harga_kopi\": [85000, np.nan, np.nan, 90000, 88000],\n})\nprint(df.isna().sum()\nprint(df.dropna().shape)\n\ndf[\"kota\"] = df[\"kota\"].fillna(\"Tidak diketahui\")\ndf[\"umur\"] = df[\"umur\"].fillna(df[\"umur\"].median())\ndf[\"harga_kopi\"] = df[\"harga_kopi\"].ffill()\nprint(df)",
"err": "File \"main.py\", line 9\n    print(df.isna().sum()\nSyntaxError: '(' was never closed",
"line": 9,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:Teks, tanggal & tipe data": {
"code": "import pandas as pd\n\ndf = pd.DataFrame({\n    \"kota\": [\"  jakarta\", \"BANDUNG \", \"Surabaya\"],\n    \"harga\": [\"Rp 85.000\", \"Rp 25.000\", \"Rp 120.000\"],\n    \"tgl\": [\"01/10/2024\", \"15/10/2024\", \"03/11/2024\"],\n})\ndf[\"kota\"] = df[\"kota\"].str.strip().str.title()\ndf[\"harga\"] = df[\"harga\"].str.replace(\"Rp \", \"\").str.replace(\".\", \"\").astype(int)\ndf[\"tgl\"] = pd.to_datetime(df[\"tgl\"], format=\"%d/%m/%Y\")\ndf[\"bulan\"] = df[\"tgl\"].dt.month\nprint(df\nprint(df[\"harga\"].sum())",
"err": "File \"main.py\", line 12\n    print(df\nSyntaxError: '(' was never closed",
"line": 12,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:Duplikat & encoding kategori": {
"code": "import pandas as pd\n\ndf = pd.DataFrame({\n    \"id_trx\": [1, 2, 2, 3],\n    \"kota\": [\"Jakarta\", \"Bandung\", \"Bandung\", \"Medan\"],\n    \"ukuran\": [\"M\", \"L\", \"L\", \"S\"],\n})\nprint(df.duplicated().tolist()\ndf = df.drop_duplicates(subset=\"id_trx\")\n\nprint(pd.get_dummies(df[\"kota\"], dtype=int))\ndf[\"ukuran_kode\"] = df[\"ukuran\"].map({\"S\": 1, \"M\": 2, \"L\": 3})\nprint(df[[\"ukuran\", \"ukuran_kode\"]])",
"err": "File \"main.py\", line 8\n    print(df.duplicated().tolist()\nSyntaxError: '(' was never closed",
"line": 8,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:groupby & agregasi": {
"code": "import pandas as pd\npenjualan = pd.DataFrame({\n    \"tanggal\": [\"2024-10-01\",\"2024-10-01\",\"2024-10-02\",\"2024-10-03\",\"2024-10-03\",\"2024-10-04\",\"2024-10-05\",\"2024-10-05\"],\n    \"kota\": [\"Jakarta\",\"Bandung\",\"Jakarta\",\"Surabaya\",\"Bandung\",\"Jakarta\",\"Medan\",\"Surabaya\"],\n    \"produk\": [\"Kopi Gayo\",\"Teh Melati\",\"Keripik\",\"Kopi Gayo\",\"Madu Hutan\",\"Teh Melati\",\"Kopi Gayo\",\"Keripik\"],\n    \"jumlah\": [3, 10, 25, 2, 1, 6, 4, 30],\n    \"harga\": [85000, 25000, 15000, 85000, 120000, 25000, 85000, 15000],\n})\n\npenjualn[\"omzet\"] = penjualan[\"jumlah\"] * penjualan[\"harga\"]\nper_kota = (penjualan.groupby(\"kota\")\n            .agg(transaksi=(\"omzet\", \"size\"), omzet=(\"omzet\", \"sum\"))\n            .sort_values(\"omzet\", ascending=False))\nper_kota[\"persen\"] = (per_kota[\"omzet\"] / per_kota[\"omzet\"].sum() * 100).round(1)\nprint(per_kota)\nprint(penjualan.groupby(\"produk\")[\"jumlah\"].sum().idxmax())",
"err": "File \"main.py\", line 10, in <module>\n    penjualn[\"omzet\"] = penjualan[\"jumlah\"] * penjualan[\"harga\"]\nNameError: name 'penjualn' is not defined. Did you mean: 'penjualan'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:merge & concat": {
"code": "import pandas as pd\n\npesanan = pd.DataFrame({\"id\": [101, 102, 103, 104], \"pelanggan_id\": [1, 2, 1, 9], \"total\": [255000, 250000, 375000, 90000]})\npelanggan = pd.DataFrame({\"pelanggan_id\": [1, 2, 3], \"nama\": [\"Andi\", \"Budi\", \"Citra\"]})\n\nprint(pd.merge(pesanan, pelanggan, on=\"pelanggan_id\", how=\"left\", validate=\"many_to_one\")\n\nokt = pd.DataFrame({\"bulan\": [\"Okt\"], \"omzet\": [1_200_000]})\nnov = pd.DataFrame({\"bulan\": [\"Nov\"], \"omzet\": [1_450_000]})\nprint(pd.concat([okt, nov], ignore_index=True))",
"err": "File \"main.py\", line 6\n    print(pd.merge(pesanan, pelanggan, on=\"pelanggan_id\", how=\"left\", validate=\"many_to_one\")\nSyntaxError: '(' was never closed",
"line": 6,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:pivot_table, crosstab & melt": {
"code": "import pandas as pd\npenjualan = pd.DataFrame({\n    \"tanggal\": [\"2024-10-01\",\"2024-10-01\",\"2024-10-02\",\"2024-10-03\",\"2024-10-03\",\"2024-10-04\",\"2024-10-05\",\"2024-10-05\"],\n    \"kota\": [\"Jakarta\",\"Bandung\",\"Jakarta\",\"Surabaya\",\"Bandung\",\"Jakarta\",\"Medan\",\"Surabaya\"],\n    \"produk\": [\"Kopi Gayo\",\"Teh Melati\",\"Keripik\",\"Kopi Gayo\",\"Madu Hutan\",\"Teh Melati\",\"Kopi Gayo\",\"Keripik\"],\n    \"jumlah\": [3, 10, 25, 2, 1, 6, 4, 30],\n    \"harga\": [85000, 25000, 15000, 85000, 120000, 25000, 85000, 15000],\n})\n\npenjualn[\"omzet\"] = penjualan[\"jumlah\"] * penjualan[\"harga\"]\nprint(penjualan.pivot_table(index=\"kota\", columns=\"produk\", values=\"omzet\", aggfunc=\"sum\", fill_value=0))\nprint(pd.crosstab(penjualan[\"kota\"], penjualan[\"produk\"]).loc[[\"Jakarta\"]])\n\nlebar = pd.DataFrame({\"kota\": [\"Jakarta\", \"Bandung\"], \"Okt\": [12, 8], \"Nov\": [15, 9]})\nprint(lebar.melt(id_vars=\"kota\", var_name=\"bulan\", value_name=\"pesanan\"))",
"err": "File \"main.py\", line 10, in <module>\n    penjualn[\"omzet\"] = penjualan[\"jumlah\"] * penjualan[\"harga\"]\nNameError: name 'penjualn' is not defined. Did you mean: 'penjualan'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Rantai transformasi dengan assign & pipe": {
"code": "import pandas as pd\npesanan = pd.DataFrame({\n    \"kota\": [\"Medan\", \"Bandung\", \"Medan\", \"Ambon\", \"Bandung\", \"Medan\"],\n    \"harga\": [85000, 25000, 25000, 85000, 85000, 18000],\n    \"qty\": [2, 4, 1, 3, 1, 5],\n})\n\ndef tandai_besar(df, batas):\n    return df.assign(besar=df[\"total\"] >= batas)\n\nringkas = (\n    pesann\n    .assign(total=lambda d: d[\"harga\"] * d[\"qty\"])\n    .query(\"qty >= 2\")\n    .pipe(tandai_besar, batas=150_000)\n    .groupby(\"kota\", as_index=False)[\"total\"].sum()\n    .sort_values(\"total\", ascending=False)\n)\nprint(ringkas.to_string(index=False))",
"err": "File \"main.py\", line 12, in <module>\n    pesann\nNameError: name 'pesann' is not defined. Did you mean: 'pesanan'?",
"line": 12,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Pemusatan & sebaran": {
"code": "import pandas as pd\n\ngaji = pd.Series([5.2, 5.5, 5.8, 6.0, 6.1, 6.3, 6.5, 48.0], name=\"gaji_juta\")\nprint(\"mean  :\", round(gaji.mean(), 2)\nprint(\"median:\", gaji.median())\nprint(\"std   :\", round(gaji.std(), 2))\n\nkota = pd.Series([\"Jakarta\", \"Bandung\", \"Jakarta\", \"Medan\", \"Jakarta\"])\nprint(\"modus :\", kota.mode()[0])\nprint(gaji.drop(7).agg([\"mean\", \"median\", \"std\"]).round(2))",
"err": "File \"main.py\", line 4\n    print(\"mean  :\", round(gaji.mean(), 2)\nSyntaxError: '(' was never closed",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:Outlier: IQR & z-score": {
"code": "import pandas as pd\n\nbelanja = pd.Series([120, 135, 150, 160, 170, 180, 195, 210, 2400], name=\"ribu\")\nq1, q3 = belnja.quantile([0.25, 0.75])\niqr = q3 - q1\nbawah, atas = q1 - 1.5 * iqr, q3 + 1.5 * iqr\nprint(q1, q3, iqr, bawah, atas)\nprint(belanja[(belanja < bawah) | (belanja > atas)].tolist())\n\nz = (belanja - belanja.mean()) / belanja.std()\nprint(z.round(2).tolist())",
"err": "File \"main.py\", line 4, in <module>\n    q1, q3 = belnja.quantile([0.25, 0.75])\nNameError: name 'belnja' is not defined. Did you mean: 'belanja'?",
"line": 4,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"pda:Korelasi": {
"code": "import pandas as pd\n\ndf = pd.DataFrame({\n    \"iklan_juta\": [1, 2, 3, 4, 5, 6],\n    \"pengunjung\": [120, 190, 260, 300, 390, 450],\n    \"hari_hujan\": [9, 7, 8, 6, 8, 7],\n})\nprint(df.corr().round(2)",
"err": "File \"main.py\", line 8\n    print(df.corr().round(2)\nSyntaxError: '(' was never closed",
"line": 8,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:Deret waktu: resample & rolling": {
"code": "import pandas as pd\ndf = pd.DataFrame({\"tanggal\": pd.date_range(\"2024-01-01\", periods=10, freq=\"D\"), \"omzet\": [120, 95, 130, 88, 150, 101, 115, 99, 140, 105]})\nharian = df.set_index(\"tanggal\")[\"omzet\"]\nprint(harian.resample(\"W\").sum().to_string()\nprint(harian.rolling(3).mean().round(1).tolist())\nprint((harian.pct_change() * 100).round(1).head(4).tolist())",
"err": "File \"main.py\", line 4\n    print(harian.resample(\"W\").sum().to_string()\nSyntaxError: '(' was never closed",
"line": 4,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"pda:SQL dari Python: sqlite3 & read_sql": {
"code": "import sqlite3\nimport pandas as pd\n\ncon = sqlite3.connect(\":memory:\")\ncon.executescript(\"\"\"\nCREATE TABLE pesanan(id INTEGER, kota TEXT, total INTEGER);\nINSERT INTO pesanan VALUES (1,'Jakarta',255000),(2,'Bandung',250000),\n  (3,'Jakarta',375000),(4,'Medan',340000);\n\"\"\")\nq = \"SELECT kota, COUNT(*) AS n, SUM(total) AS omzet FROM pesanan GROUP BY kota ORDER BY omzet DESC\"\ndf = pd.read_sql(q, con)\nprint(df\nprint(df[\"omzet\"].sum())",
"err": "File \"main.py\", line 12\n    print(df\nSyntaxError: '(' was never closed",
"line": 12,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"da:Menstandarkan data kotor dengan pandas": {
"code": "import pandas as pd\ndf = pd.DataFrame({\n    \"kota\": [\"medan\", \"MEDAN \", \"Kota Medan\", \"bandung\", \" Bandung\"],\n    \"hp\": [\"0812-3456-7890\", \"+62 812 3456 7891\", \"081234567892\", \"62812-3456-7893\", \"0812 3456 7894\"],\n})\ndf[\"kota\"] = df[\"kota\"].str.strip().str.title().str.replace(r\"^Kota \", \"\", regex=True)\ndf[\"hp\"] = df[\"hp\"].str.replace(r\"\\D\", \"\", regex=True).str.replace(r\"^(62|0)\", \"+62\", regex=True)\nprint(df.to_string(index=False)\nprint(df[\"kota\"].value_counts().to_dict())",
"err": "File \"main.py\", line 8\n    print(df.to_string(index=False)\nSyntaxError: '(' was never closed",
"line": 8,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"da:Rentang, varians & bentuk distribusi": {
"code": "import pandas as pd\nimport numpy as np\n\nbelanja = pd.Series([45, 60, 62, 70, 75, 80, 85, 95, 110, 150, 320], name=\"ribu\")\nprint(\"rentang :\", belanja.max() - belanja.min()\nprint(\"varians :\", round(belanja.var(), 1))\nprint(\"std     :\", round(belanja.std(), 1))\nprint(\"mean vs median:\", round(belanja.mean(), 1), belanja.median())\nprint(\"skew    :\", round(belanja.skew(), 2))\nprint(\"kurtosis:\", round(belanja.kurt(), 2))\nprint(\"skew log:\", round(np.log(belanja).skew(), 2))",
"err": "File \"main.py\", line 5\n    print(\"rentang :\", belanja.max() - belanja.min()\nSyntaxError: '(' was never closed",
"line": 5,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"da:Regresi linear sederhana": {
"code": "import numpy as np\n\niklan = np.array([1, 2, 3, 4, 5, 6])          # juta rupiah\npengunjung = np.array([120, 190, 260, 300, 390, 450])\n\nb, a = np.polyfit(ikln, pengunjung, 1)\nprediksi = a + b * iklan\nr2 = 1 - ((pengunjung - prediksi) ** 2).sum() / ((pengunjung - pengunjung.mean()) ** 2).sum()\nprint(f\"pengunjung = {a:.1f} + {b:.1f} x iklan\")\nprint(f\"R2 = {r2:.3f}\")\nprint(\"prediksi iklan 8 juta:\", round(a + b * 8))",
"err": "File \"main.py\", line 6, in <module>\n    b, a = np.polyfit(ikln, pengunjung, 1)\nNameError: name 'ikln' is not defined. Did you mean: 'iklan'?",
"line": 6,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"da:Persentil, kuartil & median": {
"code": "import pandas as pd\npenjualan = pd.Series([120, 95, 130, 88, 2100, 101, 115, 99, 140, 105], name=\"omzet_ribu\")\nprint(\"rata-rata :\", penjualn.mean())\nprint(\"median    :\", penjualan.median())\nprint(\"Q1, Q3    :\", penjualan.quantile(0.25), penjualan.quantile(0.75))\nprint(\"P90       :\", round(penjualan.quantile(0.9), 1))",
"err": "File \"main.py\", line 3, in <module>\n    print(\"rata-rata :\", penjualn.mean())\nNameError: name 'penjualn' is not defined. Did you mean: 'penjualan'?",
"line": 3,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"da:Funnel & stacked chart": {
"code": "import pandas as pd\n\nfunnel = pd.DataFrame({\n    \"tahap\": [\"Kunjungan\", \"Lihat produk\", \"Keranjang\", \"Checkout\", \"Bayar\"],\n    \"pengguna\": [10000, 6200, 1900, 1100, 820],\n})\nfunnel[\"dari_awal_%\"] = (funnel[\"pengguna\"] / funnel[\"pengguna\"].iloc[0] * 100).round(1)\nfunnel[\"dari_sebelumnya_%\"] = (funnel[\"pengguna\"] / funnel[\"pengguna\"].shift() * 100).round(1)\nprint(funnel.to_string(index=False)\nbocor = funnel.loc[funnel[\"dari_sebelumnya_%\"].idxmin(), \"tahap\"]\nprint(\"kebocoran terbesar sebelum:\", bocor)",
"err": "File \"main.py\", line 9\n    print(funnel.to_string(index=False)\nSyntaxError: '(' was never closed",
"line": 9,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"da:Big data, MapReduce & Spark": {
"code": "from collections import defaultdict\n\npotongan = [\n    \"kopi enak kirim cepat\",\n    \"kopi wangi harga pas\",\n    \"kirim lambat kopi enak\",\n]\n# map: setiap potongan -> (kata, 1)\npasangan = [(kata, 1) for teks in potongan for kata in teks.split()]\n# shuffle: kelompokkan menurut kunci\nkelompok = defaultdict(list)\nfor kata, n in pasangan\n    kelompok[kata].append(n)\n# reduce: jumlahkan tiap kelompok\nhasil = {kata: sum(ns) for kata, ns in kelompok.items()}\nprint(sorted(hasil.items(), key=lambda x: (-x[1], x[0]))[:4])",
"err": "File \"main.py\", line 12\n    for kata, n in pasangan\nSyntaxError: expected ':'",
"line": 12,
"kind": "colon",
"why": "Baris yang membuka blok (def, for, if, while, class) wajib diakhiri titik dua."
},
"da:Peta machine learning untuk analis": {
"code": "aktual   = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]   # 1 = pelanggan berhenti\nprediksi = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]\n\ntp = sum(a == 1 and p == 1 for a, p in zip(aktul, prediksi))\ntn = sum(a == 0 and p == 0 for a, p in zip(aktual, prediksi))\nfp = sum(a == 0 and p == 1 for a, p in zip(aktual, prediksi))\nfn = sum(a == 1 and p == 0 for a, p in zip(aktual, prediksi))\nprint(\"TP TN FP FN:\", tp, tn, fp, fn)\nprint(\"akurasi :\", (tp + tn) / len(aktual))\nprint(\"presisi :\", tp / (tp + fp))\nprint(\"recall  :\", tp / (tp + fn))",
"err": "File \"main.py\", line 4, in <module>\n    tp = sum(a == 1 and p == 1 for a, p in zip(aktul, prediksi))\nNameError: name 'aktul' is not defined. Did you mean: 'aktual'?",
"line": 4,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"de:Slowly changing dimension (SCD tipe 2)": {
"code": "import pandas as pd\n\ndim = pd.DataFrame([\n    {\"sk\": 1, \"pelanggan_id\": 41, \"kota\": \"Bandung\", \"berlaku_dari\": \"2023-01-15\", \"berlaku_sampai\": \"9999-12-31\", \"aktif\": True},\n    {\"sk\": 2, \"pelanggan_id\": 42, \"kota\": \"Medan\",   \"berlaku_dari\": \"2023-03-02\", \"berlaku_sampai\": \"9999-12-31\", \"aktif\": True},\n])\nperubahan = {\"pelanggan_id\": 41, \"kota\": \"Jakarta\", \"tanggal\": \"2024-06-01\"}\n\nlama = (dim[\"pelanggan_id\"] == perubahan[\"pelanggan_id\"]) & dim[\"aktif\"]\nif dim.loc[lama, \"kota\"].iloc[0] != perubahan[\"kota\"]:\n    dim.loc[lama, [\"berlaku_sampai\", \"aktif\"]] = [perubahan[\"tanggal\"], False]\n    baru = {\"sk\": dim[\"sk\"].max() + 1, \"pelanggan_id\": 41, \"kota\": perubahan[\"kota\"],\n            \"berlaku_dari\": perubahan[\"tanggal\"], \"berlaku_sampai\": \"9999-12-31\", \"aktif\": True}\n    dim = pd.concat([dim, pd.DataFrame([baru])], ignore_index=True)\nprint(dim.to_string(index=False)",
"err": "File \"main.py\", line 15\n    print(dim.to_string(index=False)\nSyntaxError: '(' was never closed",
"line": 15,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"de:Idempotensi & upsert": {
"code": "import sqlite3\n\nbatch = [(101, \"2024-10-01\", 255000), (102, \"2024-10-01\", 250000)]\n\ncon = sqlite3.connect(\":memory:\")\ncon.execute(\"CREATE TABLE naif (id INTEGER, tanggal TEXT, total INTEGER)\")\ncon.execute(\"CREATE TABLE aman (id INTEGER PRIMARY KEY, tanggal TEXT, total INTEGER)\")\n\nfor percobaan in range(2):           # pipeline dijalankan ulang\n    con.executemany(\"INSERT INTO naif VALUES (?, ?, ?)\", btch)\n    con.executemany(\"\"\"INSERT INTO aman VALUES (?, ?, ?)\n        ON CONFLICT(id) DO UPDATE SET tanggal = excluded.tanggal, total = excluded.total\"\"\", batch)\n\nprint(\"naif:\", con.execute(\"SELECT COUNT(*), SUM(total) FROM naif\").fetchone())\nprint(\"aman:\", con.execute(\"SELECT COUNT(*), SUM(total) FROM aman\").fetchone())",
"err": "File \"main.py\", line 10, in <module>\n    con.executemany(\"INSERT INTO naif VALUES (?, ?, ?)\", btch)\nNameError: name 'btch' is not defined. Did you mean: 'batch'?",
"line": 10,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"de:Kontrak data & validasi skema": {
"code": "KONTRAK = {\n    \"id_pesanan\": lambda v: isinstance(v, int) and v > 0,\n    \"kota\": lambda v: isinstance(v, str) and v.strip() != \"\",\n    \"total\": lambda v: isinstance(v, (int, float)) and v >= 0,\n}\n\nmasuk = [\n    {\"id_pesanan\": 1, \"kota\": \"Medan\", \"total\": 120000},\n    {\"id_pesanan\": 2, \"kota\": \"\", \"total\": 90000},\n    {\"id_pesanan\": 3, \"kota\": \"Ambon\", \"total\": \"45rb\"},\n    {\"id_pesanan\": 4, \"kota\": \"Bandung\"},\n]\n\nlolos, karantina = [], []\nfor baris in mask:\n    salah = [k for k, cek in KONTRAK.items() if k not in baris or not cek(baris[k])]\n    (karantina if salah else lolos).append((baris[\"id_pesanan\"], salah))\n\nprint(\"lolos    :\", [i for i, _ in lolos])\nprint(\"karantina:\", karantina)",
"err": "File \"main.py\", line 15, in <module>\n    for baris in mask:\nNameError: name 'mask' is not defined. Did you mean: 'masuk'?",
"line": 15,
"kind": "typo",
"why": "Nama variabel harus ditulis persis sama dengan saat dibuat, termasuk huruf besar-kecil."
},
"de:Tes pipeline & observabilitas data": {
"code": "from datetime import datetime, timedelta\n\nmuatan = {\"baris\": 41_250, \"kolom\": [\"id\", \"tanggal\", \"kota\", \"total\"],\n          \"terakhir\": datetime(2024, 10, 2, 2, 14), \"total_negatif\": 0}\nkemarin = {\"baris\": 43_900}\nsekarang = datetime(2024, 10, 2, 7, 0)\n\ncek = {\n    \"segar (< 6 jam)\": sekarang - muatan[\"terakhir\"] < timedelta(hours=6),\n    \"volume (±20%)\": abs(muatan[\"baris\"] / kemarin[\"baris\"] - 1) <= 0.20,\n    \"skema sama\": muatan[\"kolom\"] == [\"id\", \"tanggal\", \"kota\", \"total\"],\n    \"tidak ada total negatif\": muatan[\"total_negatif\"] == 0,\n}\nfor nama, ok in cek.items():\n    print((\"LULUS \" if ok else \"GAGAL \") + nama\nprint(\"pipeline sehat\" if all(cek.values()) else \"kirim peringatan ke on-call\")",
"err": "File \"main.py\", line 15\n    print((\"LULUS \" if ok else \"GAGAL \") + nama\nSyntaxError: '(' was never closed",
"line": 15,
"kind": "paren",
"why": "Setiap kurung buka harus punya pasangan kurung tutup."
},
"bi:Running total & perubahan bulan ke bulan": {
"code": "WITH bulanan AS (\n  SELET t.bulan, SUM(f.jumlah * f.harga) AS omzet\n  FROM fakta_penjualan f\n  JOIN dim_tanggal t ON t.tanggal_id = f.tanggal_id\n  GROUP BY t.bulan\n)\nSELECT bulan, omzet,\n       SUM(omzet) OVER (ORDER BY bulan) AS kumulatif,\n       ROUND(100.0 * (omzet - LAG(omzet) OVER (ORDER BY bulan))\n             / NULLIF(LAG(omzet) OVER (ORDER BY bulan), 0), 1) AS ubah_persen\nFROM bulanan\nORDER BY bulan;",
"err": "Diharapkan SELECT, tetapi yang ditemukan \"SELET\".",
"line": 2,
"kind": "sqlkw",
"why": "Kata kunci SQL harus dieja dengan benar."
}
};
const M={java:JAVA_MODULES,python:PY_MODULES,ts:TS_MODULES,fe0:FE0_MODULES,fe:FE_MODULES,pda:PDA_MODULES,da:DA_MODULES,de:DE_MODULES,bi:BI_MODULES,sql:SQL_MODULES};
for(const [key,b] of Object.entries(BUGS)){const i=key.indexOf(':'),mods=M[key.slice(0,i)],ti=key.slice(i+1);
  const l=mods&&mods.flatMap(m=>m.lessons).find(x=>x.t===ti&&x.k==='c');if(!l)throw new Error('bugs: pelajaran tidak ditemukan: '+key);l.bug=b}
})();
