/* ===================== JALUR JAVA =====================
   Mengikuti roadmap.sh/java. Pelajaran jenis:
   lab   = konsep bab + lab interaktif (dari CH)
   topic = topik 5 langkah (dari TOPICS), satu bahasa
   c     = pelajaran konsep baru: b (paragraf), code/out, pts, q, viz */
const R=String.raw;
const JAVA_MODULES=[
{t:'Fondasi Java',lvl:'Pemula',d:'Cara program Java berjalan, variabel, tipe data, operator, dan membaca input.',
 nodes:['Basic Syntax','Lifecycle of a Program','Data Types','Variables and Scopes','Type Casting','Math Operations'],
 lessons:[
  {k:'lab',n:1,nodes:['Lifecycle of a Program']},
  {k:'topic',ref:'1.0',nodes:['Basic Syntax']},
  {k:'topic',ref:'2.0',nodes:['Variables and Scopes','Data Types']},
  {k:'c',t:'Tipe data primitif & type casting',nodes:['Data Types','Type Casting'],viz:'casting',
   b:['Java punya delapan <b>tipe primitif</b>: <code>byte</code>, <code>short</code>, <code>int</code>, <code>long</code> untuk bilangan bulat, <code>float</code> dan <code>double</code> untuk pecahan, <code>char</code> untuk satu huruf, dan <code>boolean</code> untuk benar/salah. Setiap tipe punya ukuran tetap di memori, sehingga rentang nilainya terbatas.',
      'Memindahkan nilai dari tipe kecil ke tipe besar disebut <b>widening</b> dan terjadi otomatis, karena tidak ada informasi yang hilang. Sebaliknya, dari tipe besar ke tipe kecil disebut <b>narrowing</b>. Java memaksa kamu menulis <b>cast</b> eksplisit seperti <code>(int) 9.99</code>, sebagai tanda kamu sadar ada bagian yang bisa terbuang.',
      'Hati-hati dengan pembagian. <code>7 / 2</code> menghasilkan <code>3</code> karena kedua operand bertipe int. Ubah salah satunya menjadi double, misalnya <code>(double) 7 / 2</code>, untuk mendapat <code>3.5</code>.'],
   code:R`public class Casting {
    public static void main(String[] args) {
        int jumlah = 7;
        double rata = jumlah;          // widening: otomatis
        double harga = 9.99;
        int dibulatkan = (int) harga;  // narrowing: buang pecahan
        long besar = 3_000_000_000L;
        int kecil = (int) besar;       // nilai meluap (overflow)
        char huruf = 'A';
        int kode = huruf;              // char -> int: kode Unicode

        System.out.println(rata);
        System.out.println(dibulatkan);
        System.out.println(kecil);
        System.out.println(kode);
        System.out.println(7 / 2);
        System.out.println((double) 7 / 2);
    }
}`,
   out:`7.0
9
-1294967296
65
3
3.5
`,
   pts:['Urutan widening: byte → short → int → long → float → double.','Cast <code>(int)</code> memotong pecahan, bukan membulatkan. Pakai <code>Math.round</code> untuk pembulatan.','Narrowing di luar rentang menghasilkan overflow: angkanya "berputar" menjadi nilai aneh.','<code>String</code> bukan tipe primitif. Untuk mengubah teks ke angka pakai <code>Integer.parseInt("42")</code>.'],
   q:[['Apa hasil <code>(int) 4.8</code>?',['4','5','4.8'],0,'Cast ke int membuang bagian pecahan tanpa membulatkan.'],
      ['Mana yang butuh cast eksplisit?',['int ke double','double ke int','int ke long'],1,'double ke int adalah narrowing: informasi bisa hilang, jadi Java meminta cast.']]},
  {k:'topic',ref:'2.1',nodes:['Math Operations']},
  {k:'c',t:'Kelas Math & operasi angka',nodes:['Math Operations'],
   b:['Selain operator <code>+ - * / %</code>, Java menyediakan kelas <code>Math</code> berisi method statis yang siap pakai: pangkat, akar, nilai mutlak, pembulatan, minimum, dan maksimum. Kamu tidak perlu membuat objeknya, cukup panggil <code>Math.namaMethod(...)</code>.',
      'Ada tiga cara membulatkan: <code>Math.round</code> ke bilangan bulat terdekat, <code>Math.floor</code> selalu ke bawah, dan <code>Math.ceil</code> selalu ke atas. Untuk angka acak, pakai <code>Math.random()</code> yang menghasilkan double dari 0.0 sampai sebelum 1.0, atau kelas <code>Random</code>.',
      'Untuk uang, hindari double karena pecahan biner tidak selalu tepat (0.1 + 0.2 tidak persis 0.3). Di aplikasi sungguhan, programmer memakai <code>BigDecimal</code> atau menyimpan nilai dalam satuan terkecil (rupiah tanpa koma).'],
   code:R`public class Hitung {
    public static void main(String[] args) {
        System.out.println(Math.pow(2, 10));
        System.out.println(Math.sqrt(144));
        System.out.println(Math.abs(-25));
        System.out.println(Math.max(17, 42));
        System.out.println(Math.round(2.5));
        System.out.println(Math.floor(2.9));
        System.out.println(Math.ceil(2.1));
        System.out.println(0.1 + 0.2);
        int dadu = (int) (Math.random() * 6) + 1;
        System.out.println(dadu >= 1 && dadu <= 6);
    }
}`,
   out:`1024.0
12.0
25
42
3
2.0
3.0
0.30000000000000004
true
`,
   pts:['<code>Math.pow</code> dan <code>Math.sqrt</code> selalu mengembalikan double.','Rumus angka acak 1 sampai n: <code>(int)(Math.random() * n) + 1</code>.','Perhatikan <code>0.1 + 0.2</code>: double menyimpan pecahan secara mendekati.','<code>%</code> (modulus) berguna untuk cek genap/ganjil: <code>x % 2 == 0</code>.'],
   q:[['<code>Math.ceil(4.01)</code> menghasilkan?',['4.0','5.0','4'],1,'ceil selalu membulatkan ke atas dan mengembalikan double.'],
      ['Kenapa double kurang cocok untuk menyimpan saldo bank?',['Terlalu lambat','Pecahannya tidak selalu tepat','Tidak bisa negatif'],1,'Pecahan biner membuat 0.1 + 0.2 bukan tepat 0.3. Pakai BigDecimal atau satuan terkecil.']]},
  {k:'topic',ref:'3.2',nodes:['Basic Syntax']}
 ]},
{t:'Method & String',lvl:'Pemula',d:'Memecah program menjadi method, parameter dan nilai kembali, scope, serta mengolah teks.',
 nodes:['Strings and Methods','Variables and Scopes'],
 lessons:[
  {k:'topic',ref:'1.1',nodes:['Strings and Methods']},
  {k:'topic',ref:'3.0',nodes:['Strings and Methods']},
  {k:'c',t:'Scope: di mana variabel hidup',nodes:['Variables and Scopes'],
   b:['<b>Scope</b> adalah wilayah kode tempat sebuah variabel bisa dipakai. Di Java, aturannya sederhana: variabel hanya hidup di dalam pasangan kurung kurawal <code>{ }</code> tempat ia dideklarasikan, mulai dari baris deklarasinya.',
      'Variabel yang dibuat di dalam method disebut <b>variabel lokal</b>. Ia lahir saat method dipanggil dan hilang saat method selesai. Variabel di kepala <code>for</code> hanya hidup selama perulangan. Field (variabel milik kelas) hidup selama objeknya ada.',
      'Kalau kamu memakai variabel di luar scope-nya, compiler menolak dengan pesan <i>cannot find symbol</i>. Ini bukan musuh: scope yang sempit membuat program lebih mudah dibaca karena setiap nama hanya berlaku di area kecil.'],
   code:R`public class Scope {
    static int total = 0;               // field: hidup selama program

    static void tambah(int n) {          // n: parameter, lokal di method
        int dobel = n * 2;               // lokal
        total += dobel;
    }

    public static void main(String[] args) {
        for (int i = 1; i <= 3; i++) {   // i hanya hidup di dalam for
            tambah(i);
        }
        // System.out.println(i);        // error: cannot find symbol
        System.out.println(total);
        {
            int sementara = 99;          // blok bebas punya scope sendiri
            System.out.println(sementara);
        }
    }
}`,
   out:`12
99
`,
   pts:['Scope ditentukan oleh kurung kurawal terdekat.','Parameter berperilaku seperti variabel lokal yang nilainya diisi pemanggil.','Dua method boleh punya variabel lokal dengan nama sama karena scope-nya terpisah.','Deklarasikan variabel sedekat mungkin dengan tempat pemakaiannya.'],
   q:[['Variabel <code>i</code> di <code>for (int i = 0; ...)</code> bisa dipakai di mana?',['Di seluruh method','Hanya di dalam perulangan','Di seluruh kelas'],1,'Variabel kepala for hanya hidup selama perulangan itu.'],
      ['Pesan compiler kalau variabel dipakai di luar scope?',['cannot find symbol','NullPointerException','missing return'],0,'Compiler tidak menemukan nama itu di scope saat ini.']]},
  {k:'topic',ref:'3.1',nodes:['Strings and Methods']},
  {k:'c',t:'Method String & StringBuilder',nodes:['Strings and Methods'],
   b:['String di Java adalah objek yang <b>immutable</b>: isinya tidak bisa diubah. Method seperti <code>toUpperCase()</code> atau <code>replace()</code> tidak mengubah string lama, melainkan mengembalikan string baru. Itu sebabnya kamu harus menyimpan hasilnya: <code>s = s.trim();</code>.',
      'Membandingkan isi string wajib memakai <code>equals</code>, bukan <code>==</code>. Operator <code>==</code> membandingkan alamat objek, sehingga dua string dengan isi sama bisa dianggap berbeda.',
      'Kalau kamu menyambung teks berkali-kali di dalam loop, gunakan <code>StringBuilder</code>. Ia bisa diubah di tempat sehingga jauh lebih hemat daripada membuat string baru di setiap putaran.'],
   code:R`public class Teks {
    public static void main(String[] args) {
        String nama = "  Budi Santoso  ";
        String rapi = nama.trim();
        System.out.println(rapi.toUpperCase());
        System.out.println(rapi.length());
        System.out.println(rapi.indexOf("Santoso"));
        System.out.println(rapi.substring(0, 4));
        System.out.println(rapi.replace("Budi", "Bu"));
        System.out.println(rapi.contains("ant"));

        String a = "halo";
        String b = new String("halo");
        System.out.println(a == b);
        System.out.println(a.equals(b));

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 5; i++) {
            sb.append(i).append(i < 5 ? "-" : "");
        }
        System.out.println(sb.toString());
        System.out.println(String.join(", ", "Java", "Kotlin", "SQL"));
    }
}`,
   out:`BUDI SANTOSO
12
5
Budi
Bu Santoso
true
false
true
1-2-3-4-5
Java, Kotlin, SQL
`,
   pts:['String immutable: method string selalu mengembalikan string baru.','Bandingkan isi dengan <code>equals</code> atau <code>equalsIgnoreCase</code>.','<code>substring(a, b)</code> mengambil indeks a sampai sebelum b.','<code>StringBuilder</code> untuk menyusun teks panjang di dalam loop.'],
   q:[['Hasil <code>"kopi".substring(1, 3)</code>?',['"op"','"opi"','"kop"'],0,'Indeks 1 sampai sebelum 3: huruf o dan p.'],
      ['Cara benar membandingkan isi dua String?',['a == b','a.equals(b)','a = b'],1,'== membandingkan alamat objek, equals membandingkan isi.']]}
 ]},
{t:'Percabangan & perulangan',lvl:'Pemula',d:'Membuat program yang memilih jalan dan mengulang pekerjaan.',
 nodes:['Conditionals','Loops'],
 lessons:[
  {k:'lab',n:4,nodes:['Conditionals']},
  {k:'topic',ref:'4.0',nodes:['Conditionals']},
  {k:'c',t:'switch & operator ternary',nodes:['Conditionals'],
   b:['Ketika sebuah nilai dibandingkan dengan banyak kemungkinan tetap, <code>switch</code> lebih rapi daripada rantai <code>if-else</code>. Sejak Java 14 ada <b>switch expression</b> dengan panah <code>-></code>: tidak perlu <code>break</code>, dan hasilnya bisa langsung disimpan ke variabel.',
      'Switch klasik dengan titik dua masih banyak ditemui di kode lama. Di sana kamu wajib menulis <code>break</code>, kalau tidak eksekusi "jatuh" ke case berikutnya (fall-through).',
      'Untuk pilihan dua arah yang pendek, ada operator <b>ternary</b>: <code>kondisi ? nilaiJikaBenar : nilaiJikaSalah</code>. Pakai seperlunya, karena ternary bersarang cepat sulit dibaca.'],
   code:R`public class Hari {
    public static void main(String[] args) {
        int hari = 6;
        String jenis = switch (hari) {
            case 1, 2, 3, 4, 5 -> "Hari kerja";
            case 6, 7 -> "Akhir pekan";
            default -> "Tidak valid";
        };
        System.out.println(jenis);

        String nilai = "B";
        switch (nilai) {
            case "A":
                System.out.println("Istimewa");
                break;
            case "B":
                System.out.println("Baik");
                break;
            default:
                System.out.println("Tetap semangat");
        }

        int umur = 17;
        String status = umur >= 17 ? "boleh punya KTP" : "belum";
        System.out.println(status);
    }
}`,
   out:`Akhir pekan
Baik
boleh punya KTP
`,
   pts:['Switch expression (<code>-></code>) tidak butuh break dan bisa mengembalikan nilai.','Switch bisa dipakai untuk int, char, String, dan enum.','Lupa <code>break</code> di switch klasik menyebabkan fall-through.','Ternary cocok untuk pilihan dua nilai yang sederhana.'],
   q:[['Apa yang terjadi jika <code>break</code> lupa ditulis di switch klasik?',['Error kompilasi','Eksekusi lanjut ke case berikutnya','Program berhenti'],1,'Ini disebut fall-through.'],
      ['Hasil <code>5 > 3 ? "ya" : "tidak"</code>?',['"ya"','"tidak"','true'],0,'Kondisinya benar sehingga nilai pertama dipilih.']]},
  {k:'topic',ref:'4.1',nodes:['Conditionals','Loops']},
  {k:'lab',n:2,nodes:['Loops']},
  {k:'topic',ref:'2.2',nodes:['Loops']},
  {k:'topic',ref:'2.3',nodes:['Loops']},
  {k:'lab',n:5,nodes:['Loops','Conditionals']},
  {k:'topic',ref:'5.0',nodes:['Loops']},
  {k:'topic',ref:'5.1',nodes:['Conditionals']},
  {k:'topic',ref:'5.2',nodes:['Loops']}
 ]},
{t:'Array',lvl:'Pemula',d:'Menyimpan banyak nilai bertipe sama dalam satu variabel.',
 nodes:['Arrays'],
 lessons:[
  {k:'lab',n:7,nodes:['Arrays']},
  {k:'topic',ref:'7.0',nodes:['Arrays']},
  {k:'topic',ref:'7.1',nodes:['Arrays']},
  {k:'topic',ref:'7.2',nodes:['Arrays']},
  {k:'c',t:'Kelas Arrays & array dua dimensi',nodes:['Arrays'],
   b:['Kelas <code>java.util.Arrays</code> berisi alat bantu siap pakai: <code>Arrays.toString</code> untuk mencetak isi array, <code>Arrays.sort</code> untuk mengurutkan, <code>Arrays.fill</code> untuk mengisi semua elemen, dan <code>Arrays.copyOf</code> untuk menyalin.',
      'Array dua dimensi adalah array berisi array. Bayangkan tabel: indeks pertama memilih baris, indeks kedua memilih kolom. Ini cocok untuk papan permainan, nilai siswa per mata pelajaran, atau kursi bioskop.',
      'Untuk menelusurinya, pakai loop bersarang: loop luar berjalan per baris, loop dalam per kolom. Panjang baris adalah <code>grid.length</code>, panjang kolom adalah <code>grid[r].length</code>.'],
   code:R`import java.util.Arrays;

public class Tabel {
    public static void main(String[] args) {
        int[] nilai = {78, 92, 65, 88};
        Arrays.sort(nilai);
        System.out.println(Arrays.toString(nilai));

        int[] salinan = Arrays.copyOf(nilai, 6);
        System.out.println(Arrays.toString(salinan));

        int[][] kursi = new int[2][3];
        kursi[0][1] = 1;
        kursi[1][2] = 1;
        for (int r = 0; r < kursi.length; r++) {
            for (int c = 0; c < kursi[r].length; c++) {
                System.out.print((c > 0 ? " " : "") + (kursi[r][c] == 1 ? "X" : "."));
            }
            System.out.println();
        }
        System.out.println(Arrays.deepToString(kursi));
    }
}`,
   out:`[65, 78, 88, 92]
[65, 78, 88, 92, 0, 0]
. X .
. . X
[[0, 1, 0], [0, 0, 1]]
`,
   pts:['Mencetak array langsung menampilkan alamat aneh. Pakai <code>Arrays.toString</code>.','<code>Arrays.sort</code> mengurutkan di tempat (array asli berubah).','Array 2D: <code>tipe[][] nama = new tipe[baris][kolom];</code>','Elemen array angka otomatis bernilai 0 saat dibuat.'],
   q:[['Bagaimana mengakses kolom ke-3 di baris pertama <code>grid</code>?',['grid[3][1]','grid[0][2]','grid[1][3]'],1,'Indeks mulai dari 0: baris 0, kolom 2.'],
      ['Isi awal <code>new int[3]</code>?',['[null, null, null]','[0, 0, 0]','Acak'],1,'Elemen bertipe angka diisi 0 secara otomatis.']]}
 ]},
{t:'OOP dasar',lvl:'Menengah',d:'Kelas, objek, enkapsulasi, static dan final, serta bagaimana objek hidup dan mati.',
 nodes:['Basics of OOP','Classes and Objects','Attributes and Methods','Access Specifiers','Static Keyword','Final Keyword','Object Lifecycle','Encapsulation','Pass by Value / Pass by Reference'],
 lessons:[
  {k:'lab',n:8,nodes:['Basics of OOP','Classes and Objects']},
  {k:'topic',ref:'8.0',nodes:['Classes and Objects','Attributes and Methods']},
  {k:'topic',ref:'8.1',nodes:['Encapsulation','Attributes and Methods']},
  {k:'c',t:'Access specifier: public, private, protected',nodes:['Access Specifiers','Encapsulation'],
   b:['<b>Access specifier</b> menentukan siapa yang boleh melihat sebuah kelas, field, atau method. Ada empat tingkat: <code>public</code> (semua orang), <code>protected</code> (paket yang sama dan subclass), tanpa kata kunci atau <i>package-private</i> (hanya paket yang sama), dan <code>private</code> (hanya kelas itu sendiri).',
      'Aturan praktis bootcamp: buat semua field <code>private</code>, lalu sediakan method <code>public</code> untuk akses yang memang diizinkan. Dengan begitu, aturan seperti "saldo tidak boleh negatif" dijaga di satu tempat.',
      'Jika kode di luar kelas mencoba mengakses field private, compiler langsung menolak. Itu jauh lebih baik daripada bug yang baru ketahuan saat aplikasi sudah dipakai.'],
   code:R`class Rekening {
    private long saldo;              // hanya kelas ini yang boleh mengubah
    public final String pemilik;

    public Rekening(String pemilik) {
        this.pemilik = pemilik;
    }
    public void setor(long jumlah) {
        if (jumlah > 0) saldo += jumlah;
    }
    public boolean tarik(long jumlah) {
        if (jumlah <= 0 || jumlah > saldo) return false;
        saldo -= jumlah;
        return true;
    }
    public long getSaldo() { return saldo; }
}

public class Bank {
    public static void main(String[] args) {
        Rekening r = new Rekening("Andi");
        r.setor(100_000);
        System.out.println(r.tarik(250_000));
        System.out.println(r.tarik(40_000));
        System.out.println(r.pemilik + ": " + r.getSaldo());
        // r.saldo = 999_999;  // error: saldo has private access
    }
}`,
   out:`false
true
Andi: 60000
`,
   pts:['<code>private</code> &lt; package-private &lt; <code>protected</code> &lt; <code>public</code>.','Field private + method public = enkapsulasi.','Satu file boleh punya banyak kelas, tapi hanya satu yang public dan namanya sama dengan file.','Getter tanpa setter membuat nilai hanya bisa dibaca dari luar.'],
   q:[['Siapa yang bisa mengakses field <code>private</code>?',['Semua kelas di paket yang sama','Hanya kelas pemiliknya','Subclass saja'],1,'private paling ketat: hanya kelas itu sendiri.'],
      ['Kenapa saldo dibuat private?',['Supaya lebih cepat','Supaya aturan perubahan saldo dijaga di satu tempat','Karena wajib'],1,'Semua perubahan lewat setor/tarik yang memeriksa aturan.']]},
  {k:'c',t:'Kata kunci static & final',nodes:['Static Keyword','Final Keyword'],
   b:['<code>static</code> berarti "milik kelas, bukan milik objek". Field static hanya ada satu salinan yang dipakai bersama semua objek. Method static bisa dipanggil tanpa membuat objek, seperti <code>Math.max</code>. Karena tidak terikat objek, method static tidak bisa memakai <code>this</code>.',
      '<code>final</code> berarti "tidak bisa diubah lagi". Variabel final hanya bisa diisi sekali. Method final tidak bisa di-override, dan kelas final tidak bisa diturunkan (contohnya <code>String</code>).',
      'Gabungan <code>static final</code> dipakai untuk konstanta, ditulis HURUF_BESAR dengan garis bawah, misalnya <code>static final double PAJAK = 0.11;</code>.'],
   code:R`class Siswa {
    static int jumlah = 0;          // satu untuk semua objek
    static final int MAKS = 30;     // konstanta
    final String nis;               // diisi sekali di konstruktor
    String nama;

    Siswa(String nis, String nama) {
        this.nis = nis;
        this.nama = nama;
        jumlah++;
    }
    static boolean kelasPenuh() {
        return jumlah >= MAKS;
    }
}

public class Sekolah {
    public static void main(String[] args) {
        new Siswa("001", "Rina");
        new Siswa("002", "Sandi");
        Siswa s = new Siswa("003", "Tari");
        s.nama = "Tari A.";          // boleh: bukan final
        // s.nis = "999";            // error: cannot assign a value to final variable
        System.out.println(Siswa.jumlah);
        System.out.println(Siswa.kelasPenuh());
        System.out.println(s.nis + " " + s.nama);
    }
}`,
   out:`3
false
003 Tari A.
`,
   pts:['Akses anggota static lewat nama kelas: <code>Siswa.jumlah</code>.','Method static tidak bisa langsung memakai field non-static.','final pada referensi objek: referensinya tetap, tapi isi objeknya masih bisa berubah.','Konstanta: <code>static final</code> + HURUF_BESAR.'],
   q:[['Jika 3 objek Siswa dibuat, berapa salinan field static <code>jumlah</code>?',['3','1','0'],1,'Field static milik kelas, hanya satu salinan.'],
      ['Kelas final berarti?',['Tidak bisa dibuat objeknya','Tidak bisa diturunkan','Semua field-nya final'],1,'Kelas final tidak bisa punya subclass.']]},
  {k:'c',t:'Siklus hidup objek & garbage collector',nodes:['Object Lifecycle'],viz:'gc',
   b:['Setiap <code>new</code> membuat objek baru di area memori bernama <b>heap</b>. Variabel hanya menyimpan <b>referensi</b> (alamat) ke objek itu. Objek bisa punya banyak referensi sekaligus.',
      'Ketika tidak ada lagi referensi yang menunjuk sebuah objek, objek itu <b>tidak terjangkau</b>. Di Java kamu tidak menghapus objek secara manual. <b>Garbage collector</b> (GC) milik JVM berkala mencari objek tak terjangkau lalu membebaskan memorinya.',
      'Siklus hidupnya: dibuat (<code>new</code> + konstruktor), dipakai, tidak terjangkau, lalu dibersihkan GC. Kamu tidak bisa memastikan kapan GC berjalan, jadi jangan menaruh logika penting di sana. Untuk menutup file atau koneksi, pakai <code>try-with-resources</code>.'],
   code:R`class Kotak {
    String label;
    Kotak(String label) {
        this.label = label;
        System.out.println("Dibuat: " + label);
    }
}

public class Siklus {
    public static void main(String[] args) {
        Kotak a = new Kotak("A");
        Kotak b = new Kotak("B");
        Kotak c = a;          // dua referensi ke objek A
        a = null;             // A masih dijangkau lewat c
        b = null;             // B tidak terjangkau lagi -> calon GC
        System.out.println(c.label);
        c = new Kotak("C");   // A kini juga tidak terjangkau
        System.out.println(c.label);
    }
}`,
   out:`Dibuat: A
Dibuat: B
A
Dibuat: C
C
`,
   pts:['Variabel menyimpan referensi, objeknya ada di heap.','Objek tanpa referensi menjadi calon garbage collection.','<code>null</code> berarti referensi tidak menunjuk objek apa pun.','GC berjalan otomatis; jangan bergantung pada waktunya.'],
   q:[['Setelah <code>b = null</code>, objek B...',['Langsung terhapus','Menjadi calon dibersihkan GC','Pindah ke stack'],1,'GC yang menentukan kapan memorinya dibebaskan.'],
      ['Dua variabel menunjuk objek yang sama, lalu salah satunya diisi null. Objeknya?',['Masih hidup','Dibersihkan','Error'],0,'Masih ada satu referensi yang menjangkaunya.']]},
  {k:'c',t:'Pass by value (juga untuk objek)',nodes:['Pass by Value / Pass by Reference'],viz:'passval',
   b:['Java <b>selalu pass by value</b>: saat memanggil method, nilai argumen disalin ke parameter. Untuk tipe primitif, yang disalin adalah angkanya. Mengubah parameter di dalam method tidak mengubah variabel pemanggil.',
      'Untuk objek, yang disalin adalah <b>referensinya</b>. Parameter dan variabel pemanggil menunjuk objek yang sama di heap. Jadi jika method mengubah isi objek (misalnya <code>daftar.add(...)</code>), perubahan itu terlihat di luar.',
      'Namun jika method mengganti parameter dengan objek baru (<code>p = new ...</code>), hanya salinan referensi yang berubah. Variabel pemanggil tetap menunjuk objek lama. Inilah bukti Java tidak pass by reference.'],
   code:R`import java.util.ArrayList;
import java.util.List;

public class Salin {
    static void ubahAngka(int x) { x = 99; }
    static void ubahIsi(List<String> d) { d.add("baru"); }
    static void gantiObjek(List<String> d) {
        d = new ArrayList<>();
        d.add("lain");
    }

    public static void main(String[] args) {
        int n = 5;
        ubahAngka(n);
        System.out.println(n);

        List<String> daftar = new ArrayList<>();
        daftar.add("awal");
        ubahIsi(daftar);
        System.out.println(daftar);
        gantiObjek(daftar);
        System.out.println(daftar);
    }
}`,
   out:`5
[awal, baru]
[awal, baru]
`,
   pts:['Primitif: salinan nilai, aman dari perubahan.','Objek: salinan referensi, isi objek bisa diubah method.','Mengganti parameter dengan objek baru tidak berpengaruh ke pemanggil.','Untuk melindungi objek, kirim salinannya atau pakai koleksi immutable.'],
   q:[['Setelah <code>ubahAngka(n)</code> dengan n = 5, nilai n?',['99','5','0'],1,'Primitif disalin; parameter x bukan n.'],
      ['Method memanggil <code>d.add("x")</code> pada list parameter. List pemanggil?',['Ikut berubah','Tidak berubah','Error'],0,'Keduanya menunjuk objek list yang sama.']]}
 ]},
{t:'OOP lanjutan',lvl:'Menengah',d:'Pewarisan, abstraksi, interface, polimorfisme, enum, record, dan kelas bersarang.',
 nodes:['Inheritance','Abstraction','Interfaces','Method Overloading and Overriding','Static vs Dynamic Binding','Enums','Record','Nested Classes','Initializer Block'],
 lessons:[
  {k:'lab',n:9,nodes:['Inheritance']},
  {k:'topic',ref:'9.0',nodes:['Inheritance','Method Overloading and Overriding']},
  {k:'c',t:'Kelas abstrak & abstraksi',nodes:['Abstraction'],
   b:['<b>Abstraksi</b> berarti menyembunyikan detail dan hanya menampilkan apa yang penting. Pengguna kelas cukup tahu sebuah Bentuk punya <code>luas()</code>, tanpa peduli rumusnya.',
      'Kelas <code>abstract</code> adalah kelas setengah jadi. Ia boleh punya method biasa dan method abstrak (tanpa isi). Kelas abstrak tidak bisa dibuat objeknya langsung; subclass wajib melengkapi semua method abstraknya.',
      'Gunakan kelas abstrak ketika beberapa kelas berbagi kode dan field yang sama, tetapi masing-masing punya cara sendiri untuk sebagian perilakunya.'],
   code:R`abstract class Bentuk {
    private final String nama;
    Bentuk(String nama) { this.nama = nama; }
    abstract double luas();                 // wajib diisi subclass
    String info() {                         // dipakai bersama
        return nama + ": " + String.format("%.2f", luas());
    }
}
class Lingkaran extends Bentuk {
    double r;
    Lingkaran(double r) { super("Lingkaran"); this.r = r; }
    double luas() { return Math.PI * r * r; }
}
class Persegi extends Bentuk {
    double s;
    Persegi(double s) { super("Persegi"); this.s = s; }
    double luas() { return s * s; }
}

public class Abstraksi {
    public static void main(String[] args) {
        Bentuk[] semua = { new Lingkaran(1), new Persegi(3) };
        for (Bentuk b : semua) System.out.println(b.info());
        // new Bentuk("x");  // error: Bentuk is abstract
    }
}`,
   out:`Lingkaran: 3.14
Persegi: 9.00
`,
   pts:['Kelas abstrak tidak bisa di-<code>new</code>.','Method abstrak tidak punya badan dan diakhiri titik koma.','Subclass konkret wajib meng-override semua method abstrak.','Kelas abstrak boleh punya konstruktor dan field.'],
   q:[['Bisakah membuat <code>new Bentuk()</code> jika Bentuk abstrak?',['Bisa','Tidak bisa','Bisa jika tanpa parameter'],1,'Kelas abstrak hanya bisa dipakai lewat subclass.'],
      ['Subclass tidak mengisi method abstrak. Akibatnya?',['Error kompilasi, kecuali subclass juga abstract','Method otomatis kosong','Error saat runtime'],0,'Compiler menuntut semua method abstrak diisi.']]},
  {k:'topic',ref:'9.1',nodes:['Interfaces']},
  {k:'c',t:'Overloading, overriding & binding',nodes:['Method Overloading and Overriding','Static vs Dynamic Binding'],
   b:['<b>Overloading</b>: beberapa method dengan nama sama tetapi daftar parameter berbeda, di kelas yang sama. Compiler memilih versi yang cocok berdasarkan tipe argumen <i>saat kompilasi</i>. Ini disebut <b>static binding</b>.',
      '<b>Overriding</b>: subclass menulis ulang method milik superclass dengan tanda tangan yang sama. Versi yang dijalankan ditentukan oleh tipe objek sebenarnya <i>saat program berjalan</i>. Ini disebut <b>dynamic binding</b> dan menjadi dasar polimorfisme.',
      'Tulis anotasi <code>@Override</code> di atas method yang menimpa. Jika kamu salah ketik nama atau parameter, compiler langsung memberi tahu.'],
   code:R`class Hewan {
    String suara() { return "..."; }
}
class Kucing extends Hewan {
    @Override
    String suara() { return "Meong"; }
}

public class Binding {
    static String jelaskan(Hewan h) { return "Hewan"; }
    static String jelaskan(Kucing k) { return "Kucing"; }

    static int tambah(int a, int b) { return a + b; }
    static double tambah(double a, double b) { return a + b; }

    public static void main(String[] args) {
        Hewan h = new Kucing();
        System.out.println(h.suara());       // dynamic: tipe objek
        System.out.println(jelaskan(h));     // static: tipe variabel
        System.out.println(tambah(2, 3));
        System.out.println(tambah(2.5, 3));
    }
}`,
   out:`Meong
Hewan
5
5.5
`,
   pts:['Overloading = nama sama, parameter beda; dipilih saat kompilasi.','Overriding = tanda tangan sama di subclass; dipilih saat runtime.','Method static, private, dan final tidak bisa di-override.','Selalu pakai <code>@Override</code>.'],
   q:[['<code>Hewan h = new Kucing(); h.suara()</code> menjalankan versi?',['Hewan','Kucing','Keduanya'],1,'Dynamic binding memakai tipe objek sebenarnya.'],
      ['Overloading dipilih berdasarkan?',['Tipe objek saat runtime','Tipe argumen saat kompilasi','Urutan method di file'],1,'Itu sebabnya disebut static binding.']]},
  {k:'c',t:'Enum & record',nodes:['Enums','Record'],
   b:['<b>Enum</b> adalah tipe dengan daftar nilai tetap, misalnya status pesanan atau hari. Dibanding memakai String bebas, enum mencegah salah ketik karena compiler hanya menerima nilai yang terdaftar. Enum juga bisa punya field dan method.',
      '<b>Record</b> (Java 16+) adalah cara singkat membuat kelas pembawa data yang immutable. Cukup satu baris <code>record Titik(int x, int y) {}</code>, Java otomatis membuat konstruktor, getter <code>x()</code>, <code>equals</code>, <code>hashCode</code>, dan <code>toString</code>.',
      'Pakai record untuk data yang tidak berubah seperti hasil query, DTO di API, atau koordinat. Pakai kelas biasa jika objek perlu diubah-ubah.'],
   code:R`enum Status {
    BARU("Menunggu"), DIKIRIM("Dalam perjalanan"), SELESAI("Diterima");
    private final String label;
    Status(String label) { this.label = label; }
    String label() { return label; }
}

record Pesanan(int id, String barang, Status status) {}

public class Toko {
    public static void main(String[] args) {
        Pesanan p = new Pesanan(101, "Kopi Gayo", Status.DIKIRIM);
        System.out.println(p);
        System.out.println(p.barang() + " - " + p.status().label());
        System.out.println(p.equals(new Pesanan(101, "Kopi Gayo", Status.DIKIRIM)));
        StringBuilder sb = new StringBuilder();
        for (Status s : Status.values()) {
            sb.append(s).append("(").append(s.ordinal()).append(") ");
        }
        System.out.println(sb.toString().trim());
        System.out.println(Status.valueOf("SELESAI").label());
    }
}`,
   out:`Pesanan[id=101, barang=Kopi Gayo, status=DIKIRIM]
Kopi Gayo - Dalam perjalanan
true
BARU(0) DIKIRIM(1) SELESAI(2)
Diterima
`,
   pts:['<code>Status.values()</code> memberi semua nilai enum berurutan.','Enum aman dipakai di switch.','Record immutable: field-nya final dan tidak ada setter.','Getter record memakai nama field: <code>p.barang()</code>, bukan <code>getBarang()</code>.'],
   q:[['Apa yang otomatis dibuat Java untuk record?',['Setter','Konstruktor, getter, equals, toString','Method main'],1,'Record dirancang sebagai pembawa data immutable.'],
      ['Kenapa enum lebih baik daripada String untuk status?',['Lebih pendek','Nilai di luar daftar ditolak compiler','Bisa diubah kapan saja'],1,'Salah ketik ketahuan saat kompilasi.']]},
  {k:'c',t:'Kelas bersarang & initializer block',nodes:['Nested Classes','Initializer Block'],
   b:['Kelas bisa ditulis di dalam kelas lain. <b>Static nested class</b> berdiri sendiri dan sering dipakai untuk kelas pembantu, misalnya <code>Node</code> di dalam <code>LinkedList</code>. <b>Inner class</b> (non-static) terikat pada objek luarnya dan bisa mengakses field objek itu.',
      '<b>Anonymous class</b> adalah kelas tanpa nama yang dibuat sekaligus dipakai, biasanya untuk mengimplementasi interface sekali pakai. Sejak Java 8, banyak anonymous class diganti lambda.',
      '<b>Initializer block</b> adalah blok <code>{ ... }</code> di dalam kelas yang berjalan setiap objek dibuat, sebelum isi konstruktor. Versi <code>static { ... }</code> berjalan sekali saat kelas pertama kali dimuat, cocok untuk menyiapkan data statis.'],
   code:R`public class Luar {
    static int dimuat;
    int nomor;

    static {                         // sekali, saat kelas dimuat
        dimuat = 1;
        System.out.println("static block");
    }
    {                                // setiap objek dibuat
        nomor = 7;
        System.out.println("instance block");
    }
    Luar() { System.out.println("konstruktor, nomor=" + nomor); }

    static class Pembantu {           // static nested
        String sapa() { return "halo dari Pembantu"; }
    }
    class Dalam {                     // inner: butuh objek Luar
        int ambil() { return nomor * 2; }
    }

    public static void main(String[] args) {
        Luar o = new Luar();
        System.out.println(new Pembantu().sapa());
        Luar.Dalam d = o.new Dalam();
        System.out.println(d.ambil());
        Runnable r = new Runnable() {     // anonymous class
            public void run() { System.out.println("anonim jalan"); }
        };
        r.run();
    }
}`,
   out:`static block
instance block
konstruktor, nomor=7
halo dari Pembantu
14
anonim jalan
`,
   pts:['Urutan: static block (sekali) → instance block → konstruktor.','Static nested class tidak butuh objek luar.','Inner class dibuat lewat objek luar: <code>luar.new Dalam()</code>.','Anonymous class untuk implementasi sekali pakai; lambda lebih ringkas.'],
   q:[['Kapan static block berjalan?',['Setiap objek dibuat','Sekali saat kelas dimuat','Saat main selesai'],1,'Static block milik kelas, bukan objek.'],
      ['Inner class (non-static) bisa mengakses?',['Field objek luarnya','Hanya field static','Tidak ada'],0,'Inner class terikat pada satu objek luar.']]}
 ]},
{t:'Koleksi',lvl:'Menengah',d:'ArrayList, Set, Map, Stack, Queue, Deque, dan Iterator dari Java Collections Framework.',
 nodes:['Array vs ArrayList','Set','Map','Queue','Dequeue','Stack','Iterator'],
 lessons:[
  {k:'lab',n:10,nodes:['Array vs ArrayList']},
  {k:'c',t:'Array lawan ArrayList',nodes:['Array vs ArrayList'],
   b:['<b>Array</b> punya ukuran tetap yang ditentukan saat dibuat, dan bisa menyimpan tipe primitif secara langsung. <b>ArrayList</b> bisa tumbuh dan menyusut sendiri, punya banyak method siap pakai, tetapi hanya menyimpan objek. Angka primitif dibungkus otomatis menjadi <code>Integer</code> (autoboxing).',
      'Pilih array jika jumlah data pasti dan performa sangat penting, misalnya piksel gambar. Pilih ArrayList untuk hampir semua kebutuhan sehari-hari: daftar belanja, hasil pencarian, atau data dari database.',
      'Perhatikan perbedaan cara menulisnya: panjang array memakai field <code>length</code>, ukuran list memakai method <code>size()</code>. Akses elemen: <code>arr[i]</code> lawan <code>list.get(i)</code>.'],
   code:R`import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Banding {
    public static void main(String[] args) {
        int[] arr = new int[3];
        arr[0] = 10;
        System.out.println(arr.length + " " + Arrays.toString(arr));

        List<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(0, 5);           // sisip di depan
        list.remove(Integer.valueOf(20));
        System.out.println(list.size() + " " + list);
        System.out.println(list.get(1) + " " + list.contains(10));

        List<String> tetap = List.of("a", "b");
        try {
            tetap.add("c");
        } catch (UnsupportedOperationException e) {
            System.out.println("List.of tidak bisa diubah");
        }
    }
}`,
   out:`3 [10, 0, 0]
2 [5, 10]
10 true
List.of tidak bisa diubah
`,
   pts:['Array: ukuran tetap, <code>length</code>, bisa primitif.','ArrayList: ukuran dinamis, <code>size()</code>, hanya objek.','<code>List.of(...)</code> membuat list immutable.','Tulis tipe variabel sebagai interface: <code>List&lt;T&gt; x = new ArrayList&lt;&gt;()</code>.'],
   q:[['Cara mendapat jumlah elemen ArrayList?',['list.length','list.size()','list.count'],1,'ArrayList memakai method size().'],
      ['Bisakah <code>ArrayList&lt;int&gt;</code>?',['Bisa','Tidak, pakai ArrayList<Integer>','Bisa jika di-import'],1,'Generics hanya menerima tipe objek.']]},
  {k:'topic',ref:'10.0',nodes:['Array vs ArrayList']},
  {k:'topic',ref:'10.1',nodes:['Iterator']},
  {k:'lab',n:11,nodes:['Set','Map']},
  {k:'topic',ref:'11.0',nodes:['Set']},
  {k:'topic',ref:'11.1',nodes:['Map']},
  {k:'lab',n:14,nodes:['Stack','Queue']},
  {k:'topic',ref:'14.0',nodes:['Stack']},
  {k:'topic',ref:'14.1',nodes:['Queue']},
  {k:'c',t:'Deque & Iterator',nodes:['Dequeue','Iterator'],
   b:['<b>Deque</b> (double-ended queue, dibaca "dek") bisa ditambah dan diambil dari kedua ujung. <code>ArrayDeque</code> adalah implementasi yang cepat dan direkomendasikan untuk menggantikan kelas <code>Stack</code> lama maupun sebagai antrean.',
      'Sebagai stack, pakai <code>push</code>, <code>pop</code>, dan <code>peek</code>. Sebagai queue, pakai <code>offer</code>, <code>poll</code>, dan <code>peek</code>. Satu kelas, dua peran.',
      '<b>Iterator</b> adalah objek penunjuk yang berjalan di atas koleksi dengan <code>hasNext()</code> dan <code>next()</code>. Loop for-each sebenarnya memakai iterator di balik layar. Gunakan iterator secara langsung jika ingin menghapus elemen saat berjalan dengan <code>it.remove()</code>, karena menghapus lewat list saat for-each memicu <code>ConcurrentModificationException</code>.'],
   code:R`import java.util.*;

public class DekIter {
    public static void main(String[] args) {
        Deque<String> tumpuk = new ArrayDeque<>();
        tumpuk.push("piring1");
        tumpuk.push("piring2");
        System.out.println(tumpuk.pop());

        Deque<String> antre = new ArrayDeque<>();
        antre.offer("Ani");
        antre.offer("Bayu");
        antre.offerFirst("VIP");
        System.out.println(antre.poll() + " " + antre);

        List<Integer> nilai = new ArrayList<>(List.of(80, 45, 90, 30));
        Iterator<Integer> it = nilai.iterator();
        while (it.hasNext()) {
            if (it.next() < 50) it.remove();
        }
        System.out.println(nilai);
    }
}`,
   out:`piring2
VIP [Ani, Bayu]
[80, 90]
`,
   pts:['<code>ArrayDeque</code> lebih disarankan daripada <code>Stack</code> dan <code>LinkedList</code>.','Stack: push/pop/peek. Queue: offer/poll/peek.','<code>offerFirst</code>/<code>offerLast</code> memilih ujung.','Hapus saat iterasi hanya lewat <code>iterator.remove()</code> atau <code>removeIf</code>.'],
   q:[['Struktur yang bisa ditambah dari kedua ujung?',['Queue','Deque','Set'],1,'Deque = double-ended queue.'],
      ['Menghapus elemen list di dalam for-each biasanya memicu?',['ConcurrentModificationException','NullPointerException','Tidak apa-apa'],0,'Gunakan iterator.remove() atau list.removeIf(...).']]}
 ]},
{t:'Generics, exception & anotasi',lvl:'Menengah',d:'Kode yang aman tipe, menangani kesalahan dengan rapi, dan metadata pada kode.',
 nodes:['Generics','Exception Handling','Annotations'],
 lessons:[
  {k:'c',t:'Generics: kode yang aman tipe',nodes:['Generics'],
   b:['<b>Generics</b> membuat kelas dan method bisa bekerja dengan berbagai tipe sambil tetap diperiksa compiler. <code>List&lt;String&gt;</code> hanya menerima String, sehingga kamu tidak perlu cast dan tidak akan kemasukan tipe lain.',
      'Kamu bisa membuat kelas generik sendiri dengan parameter tipe seperti <code>&lt;T&gt;</code>. Huruf T adalah penampung yang diganti tipe sungguhan saat kelas dipakai: <code>Kotak&lt;Integer&gt;</code>, <code>Kotak&lt;String&gt;</code>.',
      'Batas tipe (<i>bounded type</i>) seperti <code>&lt;T extends Number&gt;</code> berarti T harus Number atau turunannya, sehingga method di dalamnya boleh memanggil <code>doubleValue()</code>. Wildcard <code>?</code> dipakai pada parameter yang menerima "list berisi tipe apa pun".'],
   code:R`import java.util.List;

class Kotak<T> {
    private final T isi;
    Kotak(T isi) { this.isi = isi; }
    T ambil() { return isi; }
}

public class Generik {
    static <T> T pertama(List<T> data) {
        return data.get(0);
    }
    static <T extends Number> double jumlah(List<T> angka) {
        double total = 0;
        for (T x : angka) total += x.doubleValue();
        return total;
    }
    static void cetak(List<?> apaSaja) {
        System.out.println("Isi: " + apaSaja);
    }

    public static void main(String[] args) {
        Kotak<String> k = new Kotak<>("rahasia");
        String s = k.ambil();             // tanpa cast
        System.out.println(s.toUpperCase());
        System.out.println(pertama(List.of(3, 1, 2)));
        System.out.println(jumlah(List.of(1.5, 2, 3L)));
        cetak(List.of('a', 'b'));
    }
}`,
   out:`RAHASIA
3
6.5
Isi: [a, b]
`,
   pts:['Generics memindahkan kesalahan tipe dari runtime ke waktu kompilasi.','Nama parameter tipe yang lazim: T (type), E (element), K/V (key/value).','<code>&lt;&gt;</code> (diamond) membiarkan compiler menebak tipe di sisi kanan.','Generics tidak menerima primitif: pakai Integer, Double, dan lainnya.'],
   q:[['Keuntungan utama generics?',['Program lebih cepat','Kesalahan tipe ketahuan saat kompilasi','Bisa menyimpan primitif'],1,'Compiler memeriksa tipe sehingga cast tidak diperlukan.'],
      ['<code>&lt;T extends Number&gt;</code> berarti?',['T harus subclass Number atau Number itu sendiri','T adalah angka primitif','T boleh apa saja'],0,'Ini disebut bounded type parameter.']]},
  {k:'topic',ref:'6.1',nodes:['Exception Handling']},
  {k:'c',t:'Checked, unchecked & exception buatan sendiri',nodes:['Exception Handling'],viz:'unwind',
   b:['Exception di Java terbagi dua. <b>Checked exception</b> (turunan <code>Exception</code>, misalnya <code>IOException</code>) wajib ditangani dengan try-catch atau dideklarasikan dengan <code>throws</code>; compiler memaksanya. <b>Unchecked exception</b> (turunan <code>RuntimeException</code>, misalnya <code>NullPointerException</code>) biasanya tanda bug dan tidak wajib ditangkap.',
      'Saat exception dilempar, Java mencari <code>catch</code> yang cocok mulai dari method saat ini, lalu naik ke pemanggilnya, dan seterusnya. Proses naik tumpukan pemanggilan ini disebut <b>stack unwinding</b>. Kalau sampai main tidak ada yang menangkap, program berhenti dan mencetak stack trace.',
      'Buat exception sendiri dengan menurunkan <code>Exception</code> atau <code>RuntimeException</code> agar pesan kesalahan bermakna bagi domainmu. Blok <code>finally</code> selalu dijalankan, dan <code>try-with-resources</code> menutup file atau koneksi secara otomatis.'],
   code:R`class SaldoKurangException extends Exception {
    SaldoKurangException(long kurang) {
        super("Saldo kurang Rp" + kurang);
    }
}

public class Atm {
    static long saldo = 50_000;

    static void tarik(long jumlah) throws SaldoKurangException {
        if (jumlah > saldo) throw new SaldoKurangException(jumlah - saldo);
        saldo -= jumlah;
    }
    static void layani(long jumlah) throws SaldoKurangException {
        System.out.println("Memproses " + jumlah);
        tarik(jumlah);                    // exception naik dari sini
        System.out.println("Berhasil");
    }

    public static void main(String[] args) {
        try {
            layani(20_000);
            layani(80_000);
        } catch (SaldoKurangException e) {
            System.out.println("Gagal: " + e.getMessage());
        } finally {
            System.out.println("Sisa saldo " + saldo);
        }
    }
}`,
   out:`Memproses 20000
Berhasil
Memproses 80000
Gagal: Saldo kurang Rp50000
Sisa saldo 30000
`,
   pts:['Checked: wajib ditangani atau dideklarasikan dengan throws.','Unchecked (RuntimeException): biasanya bug, perbaiki kodenya.','Exception naik ke pemanggil sampai ada catch yang cocok.','<code>finally</code> selalu berjalan, cocok untuk membereskan sumber daya.'],
   q:[['Kenapa "Berhasil" tidak tercetak untuk 80.000?',['Karena finally','Exception melompati sisa method dan naik ke catch','Karena saldo nol'],1,'Setelah throw, sisa baris di method itu dilewati.'],
      ['<code>IOException</code> termasuk?',['Checked','Unchecked','Error'],0,'Compiler memaksa kamu menanganinya.']]},
  {k:'c',t:'Anotasi',nodes:['Annotations'],
   b:['<b>Anotasi</b> adalah label yang ditempel pada kode dengan tanda <code>@</code>. Anotasi tidak mengubah logika secara langsung, tetapi memberi informasi tambahan kepada compiler, alat bantu, atau framework.',
      'Anotasi bawaan yang sering kamu temui: <code>@Override</code> (pastikan benar-benar menimpa method), <code>@Deprecated</code> (tandai fitur usang), <code>@SuppressWarnings</code> (redam peringatan tertentu), dan <code>@FunctionalInterface</code>.',
      'Framework memakai anotasi secara besar-besaran. Spring Boot memakai <code>@RestController</code> dan <code>@GetMapping</code>, JUnit memakai <code>@Test</code>, Hibernate memakai <code>@Entity</code>. Kamu juga bisa membuat anotasi sendiri dan membacanya lewat reflection.'],
   code:R`import java.lang.annotation.*;
import java.lang.reflect.Method;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Tugas {
    String pemilik();
    int prioritas() default 1;
}

public class Anotasi {
    @Tugas(pemilik = "Rina", prioritas = 3)
    public void kirimEmail() {}

    @Deprecated
    public void caraLama() {}

    @Override
    public String toString() { return "Anotasi demo"; }

    public static void main(String[] args) throws Exception {
        Method m = Anotasi.class.getMethod("kirimEmail");
        Tugas t = m.getAnnotation(Tugas.class);
        System.out.println(t.pemilik() + " prioritas " + t.prioritas());
        System.out.println(new Anotasi());
    }
}`,
   out:`Rina prioritas 3
Anotasi demo
`,
   pts:['Anotasi = metadata, ditulis dengan <code>@</code>.','<code>@Override</code> mencegah salah ketik saat menimpa method.','<code>@Retention(RUNTIME)</code> membuat anotasi bisa dibaca saat program berjalan.','Framework seperti Spring dan JUnit dikendalikan lewat anotasi.'],
   q:[['Fungsi <code>@Override</code>?',['Mempercepat method','Meminta compiler memastikan method benar-benar menimpa','Membuat method final'],1,'Salah nama atau parameter langsung ketahuan.'],
      ['Anotasi <code>@Test</code> milik framework?',['Spring','JUnit','Maven'],1,'JUnit menjalankan method bertanda @Test sebagai tes.']]}
 ]},
{t:'Rekursi & algoritma',lvl:'Menengah',d:'Berpikir rekursif, mencari, mengurutkan, dan mengukur kecepatan algoritma.',
 nodes:[],
 lessons:[
  {k:'lab',n:12},{k:'topic',ref:'12.0'},{k:'topic',ref:'12.1'},
  {k:'lab',n:13},{k:'topic',ref:'13.0'},{k:'topic',ref:'13.1'},{k:'topic',ref:'13.2'}
 ]},
{t:'Struktur data buatan sendiri',lvl:'Lanjutan',d:'Membangun koleksi, linked list, pohon biner, hash table, dan heap dari nol.',
 nodes:[],
 lessons:[
  {k:'lab',n:15},{k:'topic',ref:'15.0'},{k:'topic',ref:'15.1'},
  {k:'lab',n:16},{k:'topic',ref:'16.0'},{k:'topic',ref:'16.1'},
  {k:'lab',n:17},{k:'topic',ref:'17.0'},{k:'topic',ref:'17.1'},
  {k:'lab',n:18},{k:'topic',ref:'18.0'},{k:'topic',ref:'18.1'}
 ]},
{t:'Pemrograman fungsional',lvl:'Lanjutan',d:'Lambda, functional interface, stream, method chaining, dan Optional.',
 nodes:['Lambda Expressions','Functional Interfaces','High Order Functions','Functional Composition','Method Chaining','Streams','Optionals'],
 lessons:[
  {k:'lab',n:19,nodes:['Lambda Expressions']},
  {k:'topic',ref:'19.0',nodes:['Lambda Expressions']},
  {k:'c',t:'Functional interface & komposisi fungsi',nodes:['Functional Interfaces','High Order Functions','Functional Composition'],
   b:['<b>Functional interface</b> adalah interface dengan tepat satu method abstrak. Lambda bisa dipakai di mana pun functional interface diminta. Paket <code>java.util.function</code> menyediakan yang paling umum: <code>Function&lt;T,R&gt;</code> (ubah T jadi R), <code>Predicate&lt;T&gt;</code> (uji benar/salah), <code>Consumer&lt;T&gt;</code> (pakai tanpa hasil), dan <code>Supplier&lt;T&gt;</code> (hasilkan nilai).',
      '<b>Higher-order function</b> adalah fungsi yang menerima atau mengembalikan fungsi lain. Contohnya method yang menerima <code>Predicate</code> untuk menentukan data mana yang disaring.',
      '<b>Komposisi fungsi</b> merangkai fungsi kecil menjadi fungsi besar: <code>f.andThen(g)</code> menjalankan f lalu g, <code>f.compose(g)</code> menjalankan g dulu baru f. Predicate bisa digabung dengan <code>and</code>, <code>or</code>, dan <code>negate</code>.'],
   code:R`import java.util.function.*;

public class Fungsi {
    static Function<Integer, Integer> kaliDengan(int n) {   // mengembalikan fungsi
        return x -> x * n;
    }

    public static void main(String[] args) {
        Function<Integer, Integer> tambah10 = x -> x + 10;
        Function<Integer, Integer> kali2 = kaliDengan(2);
        System.out.println(tambah10.andThen(kali2).apply(5));
        System.out.println(tambah10.compose(kali2).apply(5));

        Predicate<String> panjang = s -> s.length() > 4;
        Predicate<String> awalanK = s -> s.startsWith("K");
        System.out.println(panjang.and(awalanK).test("Kopi"));
        System.out.println(panjang.and(awalanK).test("Keripik"));

        Supplier<String> sapa = () -> "Halo";
        Consumer<String> cetak = System.out::println;
        cetak.accept(sapa.get());

        BinaryOperator<Integer> maks = Math::max;
        System.out.println(maks.apply(3, 9));
    }
}`,
   out:`30
20
false
true
Halo
9
`,
   pts:['Functional interface = satu method abstrak; tandai dengan <code>@FunctionalInterface</code>.','Method reference <code>Kelas::method</code> adalah lambda yang lebih ringkas.','<code>andThen</code> = kiri ke kanan, <code>compose</code> = kanan ke kiri.','Fungsi yang mengembalikan fungsi memungkinkan "pabrik" perilaku.'],
   q:[['<code>tambah10.andThen(kali2).apply(5)</code>?',['20','30','25'],1,'(5 + 10) * 2 = 30.'],
      ['Interface untuk "ambil T, kembalikan boolean"?',['Function','Predicate','Supplier'],1,'Predicate menguji kondisi.']]},
  {k:'topic',ref:'19.1',nodes:['High Order Functions']},
  {k:'c',t:'Stream API & method chaining',nodes:['Streams','Method Chaining'],viz:'stream',
   b:['<b>Stream</b> adalah aliran data yang diproses lewat rangkaian operasi. Kamu menulis <i>apa</i> yang diinginkan (saring, ubah, kumpulkan), bukan <i>bagaimana</i> cara looping-nya. Gaya merangkai panggilan <code>a().b().c()</code> ini disebut <b>method chaining</b>.',
      'Operasi stream ada dua jenis. <b>Intermediate</b> (<code>filter</code>, <code>map</code>, <code>sorted</code>, <code>limit</code>) mengembalikan stream baru dan bersifat malas: belum ada yang dikerjakan. <b>Terminal</b> (<code>collect</code>, <code>forEach</code>, <code>count</code>, <code>reduce</code>) memicu seluruh pipeline berjalan.',
      'Stream memproses elemen satu per satu melewati semua tahap, bukan tahap per tahap. Jadi dengan <code>limit(2)</code>, pemrosesan berhenti begitu dua hasil didapat. Stream juga tidak mengubah koleksi asal.'],
   code:R`import java.util.*;
import java.util.stream.*;

public class Aliran {
    record Produk(String nama, String kategori, int harga) {}

    public static void main(String[] args) {
        List<Produk> data = List.of(
            new Produk("Kopi Gayo", "Minuman", 85000),
            new Produk("Teh Melati", "Minuman", 25000),
            new Produk("Keripik", "Camilan", 15000),
            new Produk("Kacang Mete", "Camilan", 60000),
            new Produk("Madu Hutan", "Minuman", 120000));

        List<String> mahal = data.stream()
            .filter(p -> p.harga() > 50000)
            .sorted(Comparator.comparingInt(Produk::harga))
            .map(Produk::nama)
            .collect(Collectors.toList());
        System.out.println(mahal);

        int total = data.stream().mapToInt(Produk::harga).sum();
        System.out.println(total);

        Map<String, Long> perKategori = data.stream()
            .collect(Collectors.groupingBy(Produk::kategori, TreeMap::new, Collectors.counting()));
        System.out.println(perKategori);

        String nama = IntStream.rangeClosed(1, 5)
            .filter(i -> i % 2 == 1)
            .mapToObj(i -> "#" + i)
            .collect(Collectors.joining(" "));
        System.out.println(nama);
    }
}`,
   out:`[Kacang Mete, Kopi Gayo, Madu Hutan]
305000
{Camilan=2, Minuman=3}
#1 #3 #5
`,
   pts:['Pipeline: sumber → operasi intermediate → satu operasi terminal.','Tanpa operasi terminal, stream tidak melakukan apa pun (lazy).','Stream sekali pakai: setelah terminal, buat stream baru.','<code>Collectors.groupingBy</code> mirip GROUP BY di SQL.'],
   q:[['Operasi mana yang terminal?',['filter','map','collect'],2,'collect memicu pipeline berjalan dan menghasilkan nilai.'],
      ['Apakah <code>stream().filter(...)</code> mengubah list asal?',['Ya','Tidak','Hanya jika di-collect'],1,'Stream menghasilkan data baru dan tidak mengubah sumbernya.']]},
  {k:'c',t:'Optional: mengganti null dengan aman',nodes:['Optionals'],
   b:['<code>NullPointerException</code> adalah salah satu bug paling sering di Java. <code>Optional&lt;T&gt;</code> adalah wadah yang mungkin berisi nilai, mungkin kosong. Dengan mengembalikan Optional, method memberi tahu pemanggilnya secara jelas: "hasilnya bisa tidak ada, tangani itu".',
      'Daripada memeriksa <code>if (x != null)</code>, kamu merangkai operasi: <code>map</code> untuk mengubah isi jika ada, <code>filter</code> untuk menyaring, <code>orElse</code> untuk nilai cadangan, dan <code>ifPresent</code> untuk menjalankan sesuatu hanya jika ada isinya.',
      'Pakai Optional sebagai tipe kembalian method. Jangan memakainya untuk field atau parameter, dan hindari <code>get()</code> tanpa pemeriksaan karena akan melempar exception jika kosong.'],
   code:R`import java.util.*;

public class Opsional {
    static Map<String, String> kotaPelanggan = Map.of("Andi", "Jakarta", "Budi", "Bandung");

    static Optional<String> cariKota(String nama) {
        return Optional.ofNullable(kotaPelanggan.get(nama));
    }

    public static void main(String[] args) {
        System.out.println(cariKota("Andi").map(String::toUpperCase).orElse("-"));
        System.out.println(cariKota("Gita").map(String::toUpperCase).orElse("-"));
        cariKota("Budi").ifPresent(k -> System.out.println("Kirim ke " + k));
        System.out.println(cariKota("Andi").filter(k -> k.startsWith("B")).isPresent());
        String kota = cariKota("Zaki").orElseGet(() -> "Kota belum diisi");
        System.out.println(kota);
    }
}`,
   out:`JAKARTA
-
Kirim ke Bandung
false
Kota belum diisi
`,
   pts:['<code>Optional.ofNullable(x)</code> membungkus nilai yang mungkin null.','<code>orElse</code> memberi nilai cadangan.','<code>map</code> hanya berjalan jika ada isi.','Jangan memanggil <code>get()</code> tanpa memeriksa isinya.'],
   q:[['<code>Optional.empty().orElse("x")</code>?',['null','"x"','Exception'],1,'Optional kosong, jadi nilai cadangan dipakai.'],
      ['Tempat terbaik memakai Optional?',['Field kelas','Tipe kembalian method','Parameter method'],1,'Itu tujuan awal Optional dirancang.']]}
 ]},
{t:'Paket, I/O & API standar',lvl:'Lanjutan',d:'Mengatur kode dalam paket dan modul, membaca file, tanggal, regex, jaringan, dan kriptografi.',
 nodes:['Packages','Modules','I/O Operations','File Operations','Date and Time','Regular Expressions','Networking in Java','Cryptography'],
 lessons:[
  {k:'c',t:'Package & modul',nodes:['Packages','Modules'],
   b:['<b>Package</b> mengelompokkan kelas yang berkaitan, seperti folder. Nama package ditulis di baris pertama file, misalnya <code>package com.toko.pesanan;</code>, dan harus cocok dengan struktur folder. Konvensinya memakai nama domain terbalik agar unik di seluruh dunia.',
      'Untuk memakai kelas dari package lain, tulis <code>import</code>. Kelas di <code>java.lang</code> (String, Math, System) otomatis tersedia tanpa import.',
      'Sejak Java 9 ada <b>module system</b>. Sebuah modul adalah kumpulan package dengan file <code>module-info.java</code> yang menyatakan modul apa yang dibutuhkan (<code>requires</code>) dan package mana yang boleh dipakai pihak luar (<code>exports</code>). Ini membantu aplikasi besar menjaga batas antarbagian.'],
   code:R`// File: src/com/toko/model/Produk.java
package com.toko.model;

public class Produk {
    private final String nama;
    public Produk(String nama) { this.nama = nama; }
    public String getNama() { return nama; }
}

// File: src/com/toko/App.java
package com.toko;

import com.toko.model.Produk;
import java.util.List;

public class App {
    public static void main(String[] args) {
        List<Produk> daftar = List.of(new Produk("Kopi"));
        System.out.println(daftar.get(0).getNama());
    }
}

// File: src/module-info.java
module com.toko {
    requires java.sql;
    exports com.toko.model;
}`,
   out:null,
   pts:['Satu file = satu package (baris <code>package</code> paling atas).','Struktur folder mengikuti nama package.','<code>import</code> hanya mempersingkat nama, tidak menyalin kode.','<code>module-info.java</code>: requires = butuh, exports = dibagikan.'],
   q:[['Kelas mana yang bisa dipakai tanpa import?',['ArrayList','String','Scanner'],1,'String ada di java.lang yang otomatis diimpor.'],
      ['Di module-info, kata kunci untuk membagikan package?',['requires','exports','opens'],1,'exports membuat package bisa dipakai modul lain.']]},
  {k:'lab',n:6,nodes:['I/O Operations','File Operations']},
  {k:'topic',ref:'6.0',nodes:['File Operations']},
  {k:'c',t:'File modern dengan java.nio',nodes:['File Operations','I/O Operations'],
   b:['Paket <code>java.nio.file</code> menyediakan cara modern dan ringkas untuk bekerja dengan file. <code>Path</code> mewakili lokasi file, dan kelas <code>Files</code> berisi method statis: <code>writeString</code>, <code>readString</code>, <code>readAllLines</code>, <code>lines</code>, <code>exists</code>, <code>delete</code>.',
      'Untuk file besar, jangan baca semuanya sekaligus. Pakai <code>Files.lines(path)</code> yang menghasilkan stream baris demi baris, dan bungkus dengan try-with-resources supaya file ditutup otomatis.',
      'Operasi file bisa gagal (file tidak ada, tidak punya izin), jadi method-method ini melempar <code>IOException</code> yang wajib ditangani.'],
   code:R`import java.io.IOException;
import java.nio.file.*;
import java.util.List;
import java.util.stream.Stream;

public class Berkas {
    public static void main(String[] args) throws IOException {
        Path p = Path.of("catatan.txt");
        Files.writeString(p, "kopi,85000\nteh,25000\nmadu,120000\n");

        List<String> baris = Files.readAllLines(p);
        System.out.println(baris.size() + " baris");

        try (Stream<String> s = Files.lines(p)) {
            int total = s.mapToInt(b -> Integer.parseInt(b.split(",")[1])).sum();
            System.out.println("Total " + total);
        }

        Files.writeString(p, "gula,18000\n", StandardOpenOption.APPEND);
        System.out.println(Files.readAllLines(p).get(3));
        System.out.println(Files.exists(p));
        Files.delete(p);
        System.out.println(Files.exists(p));
    }
}`,
   out:`3 baris
Total 230000
gula,18000
true
false
`,
   pts:['<code>Path.of("nama")</code> membuat path.','<code>Files.readAllLines</code> untuk file kecil, <code>Files.lines</code> untuk file besar.','<code>StandardOpenOption.APPEND</code> menambah di akhir file.','Bungkus stream file dengan try-with-resources.'],
   q:[['Cara membaca file sangat besar dengan hemat memori?',['Files.readString','Files.lines dalam try-with-resources','Files.readAllLines'],1,'Files.lines membaca bertahap sebagai stream.'],
      ['Exception yang dilempar operasi file?',['IOException','ArithmeticException','ClassCastException'],0,'IOException adalah checked exception.']]},
  {k:'c',t:'Tanggal & waktu (java.time)',nodes:['Date and Time'],
   b:['Paket <code>java.time</code> (Java 8+) menggantikan <code>Date</code> dan <code>Calendar</code> yang membingungkan. Kelas utamanya: <code>LocalDate</code> (tanggal saja), <code>LocalTime</code> (jam saja), <code>LocalDateTime</code> (keduanya), dan <code>ZonedDateTime</code> (dengan zona waktu seperti Asia/Jakarta).',
      'Semua objek java.time immutable. Method seperti <code>plusDays</code> mengembalikan tanggal baru. Untuk selisih, pakai <code>Period</code> (tahun/bulan/hari) atau <code>ChronoUnit.DAYS.between</code>. Untuk tampilan, pakai <code>DateTimeFormatter</code>.',
      'Simpan waktu di server dalam UTC atau dengan zona yang jelas, lalu ubah ke zona pengguna saat ditampilkan. Ini menghindari bug saat aplikasi dipakai lintas zona waktu.'],
   code:R`import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class Waktu {
    public static void main(String[] args) {
        LocalDate pesan = LocalDate.of(2024, 10, 28);
        LocalDate tiba = pesan.plusDays(5);
        System.out.println(tiba);
        System.out.println(tiba.getDayOfWeek());
        System.out.println(ChronoUnit.DAYS.between(pesan, tiba));

        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println(tiba.format(f));

        Period umur = Period.between(LocalDate.of(2005, 8, 17), LocalDate.of(2024, 10, 28));
        System.out.println(umur.getYears() + " tahun " + umur.getMonths() + " bulan");

        ZonedDateTime jkt = LocalDateTime.of(2024, 10, 28, 9, 0).atZone(ZoneId.of("Asia/Jakarta"));
        System.out.println(jkt.withZoneSameInstant(ZoneId.of("Asia/Tokyo")).toLocalTime());
    }
}`,
   out:`2024-11-02
SATURDAY
5
02/11/2024
19 tahun 2 bulan
11:00
`,
   pts:['LocalDate/LocalTime/LocalDateTime tanpa zona; ZonedDateTime dengan zona.','Objek java.time immutable: simpan hasil plusX.','Format dengan <code>DateTimeFormatter.ofPattern</code>.','<code>ChronoUnit.DAYS.between(a, b)</code> untuk selisih hari.'],
   q:[['<code>tanggal.plusDays(3)</code> mengubah objek <code>tanggal</code>?',['Ya','Tidak, menghasilkan objek baru','Hanya jika final'],1,'Semua kelas java.time immutable.'],
      ['Kelas untuk tanggal tanpa jam?',['LocalDate','LocalTime','Instant'],0,'LocalDate hanya menyimpan tahun, bulan, hari.']]},
  {k:'c',t:'Regular expression',nodes:['Regular Expressions'],
   b:['<b>Regular expression</b> (regex) adalah pola untuk mencocokkan teks. Satu baris regex bisa menggantikan puluhan baris if dan substring. Contohnya memvalidasi email, mengambil nomor telepon dari kalimat, atau mengganti format tanggal.',
      'Simbol dasar: <code>\\d</code> angka, <code>\\w</code> huruf/angka/garis bawah, <code>\\s</code> spasi, <code>.</code> karakter apa pun, <code>+</code> satu atau lebih, <code>*</code> nol atau lebih, <code>{3}</code> tepat tiga kali, <code>[abc]</code> salah satu dari a, b, c, <code>^</code> awal, <code>$</code> akhir. Tanda kurung <code>( )</code> membuat grup yang bisa diambil.',
      'Di Java, garis miring terbalik harus ditulis dua kali di dalam string: <code>"\\\\d+"</code>. Gunakan <code>String.matches</code> untuk validasi singkat, atau <code>Pattern</code> dan <code>Matcher</code> untuk mencari dan mengambil bagian teks.'],
   code:R`import java.util.regex.*;

public class Pola {
    public static void main(String[] args) {
        String email = "rina@kampus.ac.id";
        System.out.println(email.matches("[\\w.]+@[\\w.]+\\.[a-z]{2,}"));

        String teks = "Hubungi 0812-3456-7890 atau 0857-1111-2222";
        Matcher m = Pattern.compile("(\\d{4})-(\\d{4})-(\\d{4})").matcher(teks);
        while (m.find()) {
            System.out.println("Nomor: " + m.group() + " | awalan " + m.group(1));
        }

        String tgl = "2024-10-28";
        System.out.println(tgl.replaceAll("(\\d{4})-(\\d{2})-(\\d{2})", "$3/$2/$1"));
        System.out.println(String.join("|", "a, b ,c".split("\\s*,\\s*")));
    }
}`,
   out:`true
Nomor: 0812-3456-7890 | awalan 0812
Nomor: 0857-1111-2222 | awalan 0857
28/10/2024
a|b|c
`,
   pts:['<code>matches</code> mencocokkan seluruh string.','<code>Matcher.find()</code> mencari kecocokan berikutnya di dalam teks.','Grup ( ) bisa dipakai lagi di penggantian sebagai <code>$1</code>, <code>$2</code>.','Di string Java, <code>\\d</code> ditulis <code>"\\\\d"</code>.'],
   q:[['Pola <code>\\d{3}</code> cocok dengan?',['"12a"','"123"','"1234" seluruhnya'],1,'Tepat tiga digit.'],
      ['Untuk mengambil semua nomor dari sebuah paragraf, gunakan?',['String.matches','Matcher.find dalam loop','String.equals'],1,'find mencari kecocokan satu per satu.']]},
  {k:'c',t:'Jaringan & kriptografi dasar',nodes:['Networking in Java','Cryptography'],
   b:['Untuk memanggil API lewat HTTP, Java 11+ punya <code>HttpClient</code> bawaan. Kamu membuat <code>HttpRequest</code> dengan URL dan method (GET, POST), mengirimnya, lalu membaca <code>HttpResponse</code> berisi kode status dan body. Untuk komunikasi tingkat rendah tersedia <code>Socket</code> dan <code>ServerSocket</code>.',
      'Paket <code>java.security</code> dan <code>javax.crypto</code> menyediakan kriptografi. <b>Hash</b> seperti SHA-256 mengubah data menjadi sidik jari tetap yang tidak bisa dibalik, berguna untuk memeriksa keaslian file. Enkripsi (misalnya AES) menyandikan data agar bisa dibuka kembali dengan kunci.',
      'Aturan emas keamanan: jangan pernah menyimpan kata sandi apa adanya, dan jangan membuat algoritma kripto sendiri. Untuk password, pakai algoritma khusus seperti bcrypt atau Argon2 dengan salt.'],
   code:R`import java.net.URI;
import java.net.http.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.HexFormat;

public class Jaringan {
    public static void main(String[] args) throws Exception {
        // Hash SHA-256: sidik jari data
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] h = md.digest("halo".getBytes(StandardCharsets.UTF_8));
        System.out.println(HexFormat.of().formatHex(h).substring(0, 16) + "...");

        // Memanggil API lewat HTTP (butuh internet)
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest req = HttpRequest.newBuilder(URI.create("https://api.github.com/zen")).GET().build();
        HttpResponse<String> res = client.send(req, HttpResponse.BodyHandlers.ofString());
        System.out.println(res.statusCode());
        System.out.println(res.body());
    }
}`,
   out:`b94d27b9934d3e08...
200
(sebuah kutipan pendek dari GitHub)
`,
   run:false,
   pts:['<code>HttpClient</code> untuk memanggil REST API.','Kode status 200 berarti berhasil, 404 tidak ditemukan, 500 error server.','Hash satu arah; enkripsi dua arah dengan kunci.','Simpan password dengan bcrypt/Argon2, bukan SHA mentah.'],
   q:[['Hash SHA-256 bisa dibalik untuk mendapat data aslinya?',['Bisa','Tidak','Bisa dengan kunci'],1,'Hash adalah fungsi satu arah.'],
      ['Kode status HTTP untuk "tidak ditemukan"?',['200','404','500'],1,'404 Not Found.']]}
 ]},
{t:'Konkurensi',lvl:'Lanjutan',d:'Thread, race condition, sinkronisasi, executor, virtual thread, dan Java Memory Model.',
 nodes:['Concurrency','Threads','Virtual Threads','Volatile Keyword','Java Memory Model'],
 lessons:[
  {k:'c',t:'Thread & race condition',nodes:['Threads','Concurrency'],viz:'race',
   b:['<b>Thread</b> adalah jalur eksekusi. Program biasa punya satu thread (main), tetapi kamu bisa membuat thread lain agar beberapa pekerjaan berjalan bersamaan, misalnya mengunduh file sambil tetap merespons pengguna.',
      'Masalah muncul ketika dua thread mengubah data yang sama. <code>counter++</code> terlihat satu langkah, padahal sebenarnya tiga: baca, tambah, tulis. Jika dua thread membaca nilai yang sama sebelum salah satunya menulis, satu penambahan hilang. Ini disebut <b>race condition</b>, dan hasilnya berubah-ubah setiap dijalankan.',
      'Solusinya adalah membuat bagian kritis hanya bisa dimasuki satu thread pada satu waktu, dengan <code>synchronized</code>, <code>Lock</code>, atau memakai kelas atomik seperti <code>AtomicInteger</code>.'],
   code:R`import java.util.concurrent.atomic.AtomicInteger;

public class Balapan {
    static int biasa = 0;
    static int aman = 0;
    static AtomicInteger atomik = new AtomicInteger();

    static synchronized void tambahAman() { aman++; }

    public static void main(String[] args) throws InterruptedException {
        Runnable kerja = () -> {
            for (int i = 0; i < 100_000; i++) {
                biasa++;              // tidak aman
                tambahAman();         // satu thread per waktu
                atomik.incrementAndGet();
            }
        };
        Thread t1 = new Thread(kerja);
        Thread t2 = new Thread(kerja);
        t1.start(); t2.start();
        t1.join();  t2.join();        // tunggu keduanya selesai
        System.out.println("biasa  = " + biasa + " (seharusnya 200000)");
        System.out.println("aman   = " + aman);
        System.out.println("atomik = " + atomik.get());
    }
}`,
   out:`biasa  = 137482 (seharusnya 200000)
aman   = 200000
atomik = 200000
`,
   run:false,
   pts:['<code>start()</code> menjalankan thread baru; <code>run()</code> langsung hanya memanggil method biasa.','<code>join()</code> menunggu thread selesai.','Race condition: hasil bergantung pada urutan thread yang tidak bisa ditebak.','<code>synchronized</code> dan kelas atomik mencegah update yang hilang.'],
   q:[['Kenapa <code>counter++</code> tidak aman di banyak thread?',['Karena lambat','Karena terdiri dari baca, tambah, tulis yang bisa disela','Karena int terlalu kecil'],1,'Thread lain bisa menyela di antara langkah-langkahnya.'],
      ['Method untuk menunggu thread selesai?',['wait()','join()','sleep()'],1,'join memblokir sampai thread itu berakhir.']]},
  {k:'c',t:'ExecutorService & virtual thread',nodes:['Virtual Threads','Concurrency'],
   b:['Membuat <code>new Thread</code> untuk setiap tugas itu boros. <b>ExecutorService</b> mengelola kumpulan thread (thread pool): kamu cukup menyerahkan tugas, dan executor yang mengatur thread mana yang mengerjakannya. Hasil tugas bisa diambil lewat <code>Future</code>.',
      'Java 21 memperkenalkan <b>virtual thread</b>: thread ringan yang dikelola JVM, bukan sistem operasi. Kamu bisa membuat ratusan ribu virtual thread sekaligus. Ini cocok untuk server yang banyak menunggu I/O, misalnya memanggil database atau API, karena saat menunggu, virtual thread tidak memakan thread sistem.',
      'Cara memakainya hampir sama: <code>Executors.newVirtualThreadPerTaskExecutor()</code>. Kode tetap ditulis gaya biasa (blocking), tanpa callback yang rumit.'],
   code:R`import java.util.*;
import java.util.concurrent.*;

public class Pekerja {
    static int hitungHarga(int id) throws InterruptedException {
        Thread.sleep(100);                 // pura-pura memanggil database
        return id * 1000;
    }

    public static void main(String[] args) throws Exception {
        try (ExecutorService ex = Executors.newVirtualThreadPerTaskExecutor()) {
            List<Future<Integer>> hasil = new ArrayList<>();
            for (int i = 1; i <= 10_000; i++) {
                final int id = i;
                hasil.add(ex.submit(() -> hitungHarga(id)));
            }
            long total = 0;
            for (Future<Integer> f : hasil) total += f.get();
            System.out.println("Total: " + total);
        }
        // 10.000 tugas x 100 ms selesai sekitar sepersekian detik,
        // karena virtual thread yang menunggu tidak memblokir thread OS.
    }
}`,
   out:`Total: 50005000000
`,
   pts:['Thread pool menghindari biaya membuat thread berulang.','<code>submit</code> mengembalikan <code>Future</code>; <code>get()</code> menunggu hasilnya.','Virtual thread (Java 21) cocok untuk tugas yang banyak menunggu I/O.','ExecutorService dalam try-with-resources ditutup otomatis setelah semua tugas selesai.'],
   q:[['Keunggulan virtual thread?',['Lebih cepat menghitung matematika','Sangat ringan, bisa dibuat ratusan ribu','Tidak butuh JVM'],1,'Cocok untuk banyak tugas yang menunggu I/O.'],
      ['Objek yang mewakili hasil tugas yang belum selesai?',['Future','Promise','Thread'],0,'Future.get() menunggu dan mengambil hasilnya.']]},
  {k:'c',t:'volatile & Java Memory Model',nodes:['Volatile Keyword','Java Memory Model'],
   b:['Demi kecepatan, setiap inti CPU bisa menyimpan salinan variabel di cache-nya sendiri, dan compiler boleh mengubah urutan instruksi. Akibatnya, perubahan yang dibuat satu thread belum tentu langsung terlihat oleh thread lain.',
      '<b>Java Memory Model</b> (JMM) adalah aturan resmi tentang kapan perubahan dijamin terlihat. Kuncinya adalah hubungan <i>happens-before</i>: misalnya, keluar dari blok synchronized "terjadi sebelum" thread lain masuk ke blok dengan kunci yang sama, sehingga perubahannya terlihat.',
      'Kata kunci <code>volatile</code> menjamin setiap baca dan tulis variabel langsung ke memori utama, sehingga semua thread melihat nilai terbaru. Cocok untuk flag sederhana seperti <code>berhenti = true</code>. Namun volatile tidak membuat <code>x++</code> menjadi atomik; untuk itu tetap pakai synchronized atau Atomic.'],
   code:R`public class Bendera {
    private static volatile boolean jalan = true;   // tanpa volatile, loop bisa tak berhenti

    public static void main(String[] args) throws InterruptedException {
        Thread pekerja = new Thread(() -> {
            long putaran = 0;
            while (jalan) putaran++;
            System.out.println("Pekerja berhenti");
        });
        pekerja.start();
        Thread.sleep(200);
        jalan = false;              // perubahan langsung terlihat oleh pekerja
        pekerja.join();
        System.out.println("Selesai");
    }
}`,
   out:`Pekerja berhenti
Selesai
`,
   pts:['Tanpa sinkronisasi, thread bisa membaca nilai basi dari cache.','<code>volatile</code> = visibilitas terjamin, bukan atomisitas.','synchronized memberi visibilitas sekaligus eksklusivitas.','Happens-before adalah inti aturan JMM.'],
   q:[['Apakah <code>volatile int x; x++</code> aman di banyak thread?',['Aman','Tidak, x++ tetap bukan operasi atomik','Aman jika x private'],1,'volatile hanya menjamin visibilitas.'],
      ['Kegunaan tepat volatile?',['Flag berhenti yang dibaca thread lain','Penjumlahan bersama','Mengunci method'],0,'Satu thread menulis, thread lain membaca.']]}
 ]},
{t:'Build, logging & testing',lvl:'Profesional',d:'Alat yang dipakai tim profesional: Maven/Gradle, log yang rapi, dan tes otomatis.',
 nodes:['Build Tools','Maven','Gradle','Bazel','Logging Frameworks','Log4j2','Logback','Slf4j','TinyLog','Testing','JUnit','Testng','Mockito','Cucumber JVM','Rest assured','JMeter'],
 lessons:[
  {k:'c',t:'Build tool: Maven, Gradle, Bazel',nodes:['Build Tools','Maven','Gradle','Bazel'],viz:'build',
   b:['Proyek nyata punya puluhan library (dependency), tes, dan langkah pengemasan. <b>Build tool</b> mengotomatiskan semuanya: mengunduh library, mengompilasi, menjalankan tes, dan membungkus aplikasi menjadi file <code>.jar</code> siap dijalankan.',
      '<b>Maven</b> memakai file XML <code>pom.xml</code> dan siklus hidup baku: <code>validate → compile → test → package → install → deploy</code>. Menjalankan satu tahap otomatis menjalankan tahap sebelumnya. <b>Gradle</b> memakai skrip Groovy/Kotlin (<code>build.gradle.kts</code>) yang lebih ringkas dan cepat berkat cache; Gradle juga menjadi standar proyek Android.',
      '<b>Bazel</b> dari Google dirancang untuk monorepo raksasa dengan banyak bahasa. Untuk proyek belajar dan kebanyakan perusahaan, Maven atau Gradle sudah lebih dari cukup.'],
   code:R`<!-- pom.xml (Maven) -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.toko</groupId>
  <artifactId>kasir</artifactId>
  <version>1.0.0</version>
  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>5.10.2</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>

// build.gradle.kts (Gradle, isi yang setara)
plugins { java }
java { toolchain { languageVersion = JavaLanguageVersion.of(21) } }
repositories { mavenCentral() }
dependencies { testImplementation("org.junit.jupiter:junit-jupiter:5.10.2") }

# Perintah yang sering dipakai
mvn package          # compile + test + buat target/kasir-1.0.0.jar
./gradlew build      # setara di Gradle`,
   out:null,lang:'text',
   pts:['Dependency ditulis dengan koordinat groupId:artifactId:version.','Library diunduh otomatis dari Maven Central.','Maven: konvensi kuat, XML. Gradle: skrip ringkas, build inkremental.','Tahap <code>test</code> berjalan otomatis sebelum <code>package</code>.'],
   q:[['File konfigurasi utama Maven?',['build.gradle','pom.xml','package.json'],1,'POM = Project Object Model.'],
      ['Menjalankan <code>mvn package</code> juga menjalankan?',['compile dan test','deploy','tidak ada yang lain'],0,'Tahap sebelumnya di siklus hidup selalu ikut dijalankan.']]},
  {k:'c',t:'Logging: SLF4J, Logback, Log4j2',nodes:['Logging Frameworks','Slf4j','Logback','Log4j2','TinyLog'],
   b:['<code>System.out.println</code> cukup untuk belajar, tetapi aplikasi produksi butuh <b>logging</b>: pesan bertingkat (TRACE, DEBUG, INFO, WARN, ERROR), dilengkapi waktu dan nama kelas, yang bisa diarahkan ke file atau layanan pemantauan, dan bisa diatur tanpa mengubah kode.',
      '<b>SLF4J</b> adalah lapisan antarmuka (facade). Kode kamu hanya bicara dengan SLF4J, sedangkan implementasinya bisa <b>Logback</b> (bawaan Spring Boot) atau <b>Log4j2</b> (sangat cepat). <b>TinyLog</b> adalah alternatif yang sangat ringan untuk aplikasi kecil.',
      'Pakai placeholder <code>{}</code> alih-alih menyambung string, supaya teks hanya disusun jika level itu memang aktif. Jangan pernah mencatat data sensitif seperti password atau nomor kartu.'],
   code:R`import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Kasir {
    private static final Logger log = LoggerFactory.getLogger(Kasir.class);

    public void bayar(String idPesanan, long total) {
        log.info("Memproses pembayaran {} sebesar {}", idPesanan, total);
        if (total <= 0) {
            log.warn("Total tidak wajar untuk pesanan {}", idPesanan);
            return;
        }
        try {
            // ... panggil payment gateway
            log.debug("Respons gateway diterima");
        } catch (Exception e) {
            log.error("Pembayaran {} gagal", idPesanan, e);
        }
    }
}

// Contoh keluaran (format Logback):
// 10:15:02.341 INFO  Kasir - Memproses pembayaran 101 sebesar 85000`,
   out:null,
   pts:['Level: TRACE &lt; DEBUG &lt; INFO &lt; WARN &lt; ERROR.','SLF4J = antarmuka, Logback/Log4j2 = mesin.','Pakai <code>{}</code>, bukan penyambungan string.','Level dan tujuan log diatur di file konfigurasi, misalnya logback.xml.'],
   q:[['Kenapa memakai SLF4J, bukan langsung Logback?',['Lebih cepat','Implementasi bisa diganti tanpa mengubah kode','Wajib di Java'],1,'SLF4J adalah facade.'],
      ['Level untuk kegagalan yang perlu ditangani segera?',['DEBUG','INFO','ERROR'],2,'ERROR untuk kejadian gagal.']]},
  {k:'c',t:'Unit test dengan JUnit 5',nodes:['Testing','JUnit','Testng'],
   b:['<b>Unit test</b> adalah kode kecil yang memeriksa satu bagian program bekerja sesuai harapan. Tes dijalankan otomatis setiap kali kode berubah, sehingga bug ketahuan sebelum sampai ke pengguna.',
      '<b>JUnit 5</b> adalah framework tes paling populer di Java. Method tes diberi anotasi <code>@Test</code>, lalu memakai assertion seperti <code>assertEquals(harapan, kenyataan)</code> dan <code>assertThrows</code>. Pola yang dianjurkan: <b>Arrange</b> (siapkan), <b>Act</b> (jalankan), <b>Assert</b> (periksa).',
      '<b>TestNG</b> adalah alternatif dengan fitur pengelompokan dan dependensi antartes yang kuat. Di kedua framework, tes ditaruh di <code>src/test/java</code> dan dijalankan dengan <code>mvn test</code> atau <code>./gradlew test</code>.'],
   code:R`import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;

class Diskon {
    static long hitung(long harga, int persen) {
        if (persen < 0 || persen > 100) throw new IllegalArgumentException("persen salah");
        return harga - harga * persen / 100;
    }
}

class DiskonTest {
    @Test
    void diskonSepuluhPersen() {
        long hasil = Diskon.hitung(50_000, 10);   // act
        assertEquals(45_000, hasil);              // assert
    }

    @Test
    void persenNegatifDitolak() {
        assertThrows(IllegalArgumentException.class, () -> Diskon.hitung(1000, -5));
    }

    @ParameterizedTest
    @CsvSource({"100000, 0, 100000", "100000, 100, 0", "80000, 25, 60000"})
    void banyakKasus(long harga, int persen, long harapan) {
        assertEquals(harapan, Diskon.hitung(harga, persen));
    }
}`,
   out:null,
   pts:['Satu tes memeriksa satu perilaku, dengan nama yang jelas.','Arrange, Act, Assert.','<code>@ParameterizedTest</code> menguji banyak data dengan satu method.','Tes yang baik cepat, mandiri, dan bisa diulang.'],
   q:[['Assertion untuk memastikan exception dilempar?',['assertEquals','assertThrows','assertTrue'],1,'assertThrows menerima tipe exception dan lambda.'],
      ['Di folder mana tes ditaruh pada proyek Maven?',['src/main/java','src/test/java','test/'],1,'Konvensi Maven memisahkan kode dan tes.']]},
  {k:'c',t:'Mocking & jenis tes lain',nodes:['Mockito','Cucumber JVM','Rest assured','JMeter'],
   b:['Kadang kelas yang diuji bergantung pada database atau API luar. <b>Mockito</b> membuat <i>mock</i>: objek tiruan yang perilakunya kamu atur (<code>when(...).thenReturn(...)</code>), lalu kamu periksa apakah ia dipanggil dengan benar (<code>verify</code>). Tes jadi cepat dan tidak bergantung pada sistem lain.',
      '<b>Cucumber JVM</b> menulis skenario tes dalam bahasa mirip kalimat (Given, When, Then) sehingga bisa dibaca orang bisnis. <b>REST Assured</b> menguji REST API dengan gaya berantai: kirim request, periksa status dan isi JSON.',
      '<b>JMeter</b> menguji beban: mensimulasikan ribuan pengguna sekaligus untuk melihat apakah aplikasi tetap cepat. Bersama unit test, ini membentuk piramida tes: banyak unit test, lebih sedikit tes integrasi, dan sedikit tes end-to-end.'],
   code:R`// Mockito: uji LayananPesanan tanpa database sungguhan
@Test
void totalDihitungDariRepo() {
    RepoProduk repo = mock(RepoProduk.class);
    when(repo.harga("KOPI")).thenReturn(85_000L);

    LayananPesanan layanan = new LayananPesanan(repo);
    assertEquals(170_000L, layanan.total("KOPI", 2));
    verify(repo).harga("KOPI");
}

// REST Assured: uji endpoint API
given().when().get("/api/produk/1")
       .then().statusCode(200)
       .body("nama", equalTo("Kopi Gayo"));

# Cucumber: skenario dalam bahasa manusia
Scenario: Diskon member
  Given pelanggan adalah member
  When ia membeli Kopi Gayo seharga 85000
  Then total yang dibayar adalah 76500`,
   out:null,
   pts:['Mock menggantikan dependensi yang lambat atau tidak stabil.','<code>when...thenReturn</code> mengatur, <code>verify</code> memeriksa interaksi.','REST Assured untuk tes API, Cucumber untuk skenario bisnis, JMeter untuk tes beban.','Piramida tes: banyak unit, sedikit end-to-end.'],
   q:[['Kegunaan mock?',['Menggantikan dependensi luar saat tes','Mempercepat produksi','Mengganti database selamanya'],0,'Tes fokus pada satu kelas saja.'],
      ['Alat untuk mensimulasikan ribuan pengguna?',['JUnit','JMeter','Mockito'],1,'JMeter dipakai untuk load test.']]}
 ]},
{t:'Database, web & dokumentasi',lvl:'Profesional',d:'Menghubungkan Java ke database, membuat REST API dengan framework, dependency injection, dan Javadoc.',
 nodes:['Database Access','Java JDBC','Hibernate','Spring data jpa','Ebean','Web Frameworks','Spring Boot','Quarkus','Javalin','Play Framework','Dependency Injection','Documentation','Javadoc'],
 lessons:[
  {k:'c',t:'JDBC: Java bicara dengan database',nodes:['Database Access','Java JDBC'],
   b:['<b>JDBC</b> (Java Database Connectivity) adalah API standar untuk menjalankan SQL dari Java. Alurnya: buka <code>Connection</code> dengan URL database, siapkan <code>PreparedStatement</code>, jalankan, lalu baca <code>ResultSet</code> baris demi baris.',
      'Selalu pakai <code>PreparedStatement</code> dengan tanda tanya <code>?</code> sebagai tempat nilai. Jangan menyambung input pengguna langsung ke string SQL, karena itu membuka celah <b>SQL injection</b>. Materi SQL di jalur SQL menjelaskan serangan ini secara visual.',
      'Bungkus koneksi dengan try-with-resources supaya tertutup otomatis. Di aplikasi sungguhan, koneksi diambil dari <i>connection pool</i> seperti HikariCP agar tidak membuat koneksi baru setiap query.'],
   code:R`import java.sql.*;

public class DaftarProduk {
    public static void main(String[] args) throws SQLException {
        String url = "jdbc:postgresql://localhost:5432/toko";
        String sql = "SELECT nama, harga FROM produk WHERE kategori = ? AND harga <= ? ORDER BY harga";

        try (Connection con = DriverManager.getConnection(url, "app", "rahasia");
             PreparedStatement ps = con.prepareStatement(sql)) {
            ps.setString(1, "Minuman");
            ps.setInt(2, 100_000);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    System.out.println(rs.getString("nama") + " " + rs.getInt("harga"));
                }
            }
        }
    }
}`,
   out:`Teh Melati 25000
Kopi Gayo 85000
`,
   run:false,
   pts:['Connection → PreparedStatement → ResultSet.','Tanda <code>?</code> diisi dengan <code>setString</code>, <code>setInt</code>, dan lainnya.','<code>executeQuery</code> untuk SELECT, <code>executeUpdate</code> untuk INSERT/UPDATE/DELETE.','Jangan pernah menyambung input pengguna ke SQL.'],
   q:[['Cara aman memasukkan input pengguna ke query?',['Sambung string','PreparedStatement dengan ?','Pakai String.format'],1,'Nilai dikirim terpisah dari perintah SQL.'],
      ['Method ResultSet untuk pindah ke baris berikutnya?',['next()','hasNext()','fetch()'],0,'rs.next() mengembalikan false jika baris habis.']]},
  {k:'c',t:'ORM: Hibernate, Spring Data JPA, Ebean',nodes:['Hibernate','Spring data jpa','Ebean'],
   b:['Menulis JDBC untuk setiap tabel itu melelahkan. <b>ORM</b> (Object-Relational Mapping) memetakan kelas Java ke tabel database: satu objek = satu baris, satu field = satu kolom. Kamu bekerja dengan objek, ORM yang menulis SQL-nya.',
      '<b>JPA</b> adalah standar anotasinya (<code>@Entity</code>, <code>@Id</code>, <code>@ManyToOne</code>), dan <b>Hibernate</b> adalah implementasi paling populer. <b>Spring Data JPA</b> melangkah lebih jauh: cukup tulis interface repository, dan query seperti <code>findByKategori</code> dibuat otomatis dari nama method.',
      '<b>Ebean</b> adalah ORM alternatif yang lebih sederhana. Apa pun ORM-nya, tetap pahami SQL: kamu perlu membaca query yang dihasilkan untuk menemukan masalah performa seperti N+1 query.'],
   code:R`@Entity
@Table(name = "produk")
public class Produk {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String nama;
    private String kategori;
    private Integer harga;
    // getter & setter
}

public interface ProdukRepository extends JpaRepository<Produk, Long> {
    List<Produk> findByKategoriOrderByHargaAsc(String kategori);

    @Query("SELECT p FROM Produk p WHERE p.harga > :min")
    List<Produk> mahalDari(@Param("min") int min);
}

// Pemakaian di service
List<Produk> minuman = repo.findByKategoriOrderByHargaAsc("Minuman");
// SQL yang dibuat: select ... from produk where kategori=? order by harga asc`,
   out:null,
   pts:['ORM memetakan kelas ke tabel.','JPA = standar, Hibernate = implementasi.','Spring Data membuat query dari nama method.','Tetap periksa SQL yang dihasilkan ORM.'],
   q:[['Anotasi yang menandai kelas sebagai tabel?',['@Table saja','@Entity','@Column'],1,'@Entity menandai kelas sebagai entitas JPA.'],
      ['<code>findByKategori</code> di Spring Data artinya?',['Harus ditulis SQL-nya manual','Query dibuat otomatis dari nama method','Error'],1,'Spring Data mengurai nama method.']]},
  {k:'c',t:'Spring Boot & dependency injection',nodes:['Spring Boot','Dependency Injection'],
   b:['<b>Dependency injection</b> (DI) berarti sebuah kelas tidak membuat sendiri objek yang ia butuhkan, melainkan menerimanya dari luar, biasanya lewat konstruktor. Hasilnya: kelas lebih mudah diuji (dependency bisa diganti mock) dan bagian-bagian aplikasi tidak saling terikat erat.',
      '<b>Spring Boot</b> adalah framework Java paling populer untuk membuat REST API dan aplikasi web. Ia punya <i>container</i> yang membuat dan menyambungkan objek (bean) secara otomatis. Kelas bertanda <code>@Service</code>, <code>@Repository</code>, atau <code>@RestController</code> dikelola Spring, dan dependency-nya disuntikkan lewat konstruktor.',
      'Dengan beberapa anotasi, sebuah method menjadi endpoint HTTP: <code>@GetMapping("/produk")</code> menangani GET, dan objek yang dikembalikan otomatis diubah menjadi JSON.'],
   code:R`@SpringBootApplication
public class TokoApp {
    public static void main(String[] args) {
        SpringApplication.run(TokoApp.class, args);
    }
}

@Service
class ProdukService {
    private final ProdukRepository repo;
    ProdukService(ProdukRepository repo) {   // disuntikkan Spring
        this.repo = repo;
    }
    List<Produk> minuman() { return repo.findByKategoriOrderByHargaAsc("Minuman"); }
}

@RestController
@RequestMapping("/api/produk")
class ProdukController {
    private final ProdukService service;
    ProdukController(ProdukService service) { this.service = service; }

    @GetMapping("/minuman")
    List<Produk> daftarMinuman() { return service.minuman(); }
}
// GET http://localhost:8080/api/produk/minuman -> [{"id":2,"nama":"Teh Melati",...}]`,
   out:null,
   pts:['DI: terima dependency lewat konstruktor, jangan <code>new</code> sendiri.','Lapisan umum: Controller → Service → Repository.','Spring Boot menyiapkan server web (Tomcat) secara otomatis.','Objek yang dikembalikan controller diubah menjadi JSON.'],
   q:[['Manfaat utama dependency injection?',['Kode lebih pendek','Kelas mudah diuji dan tidak terikat erat','Program lebih cepat'],1,'Dependency bisa diganti, misalnya dengan mock.'],
      ['Anotasi untuk endpoint HTTP GET?',['@GetMapping','@Get','@Request'],0,'@GetMapping memetakan request GET ke method.']]},
  {k:'c',t:'Framework web lain: Quarkus, Javalin, Play',nodes:['Web Frameworks','Quarkus','Javalin','Play Framework'],
   b:['Selain Spring Boot, ada beberapa framework web Java dengan karakter berbeda. <b>Quarkus</b> dirancang untuk cloud dan container: startup sangat cepat dan hemat memori, bahkan bisa dikompilasi menjadi native executable dengan GraalVM.',
      '<b>Javalin</b> adalah framework mini yang sangat sederhana, cocok untuk belajar atau layanan kecil: beberapa baris sudah menjadi API. <b>Play Framework</b> bersifat reaktif dan tanpa state, populer untuk aplikasi web dengan Scala dan Java.',
      'Pilih berdasarkan kebutuhan: Spring Boot untuk ekosistem terlengkap dan lowongan kerja terbanyak, Quarkus untuk microservice di Kubernetes, Javalin untuk API kecil yang cepat dibuat.'],
   code:R`// Javalin: REST API dalam beberapa baris
import io.javalin.Javalin;
import java.util.Map;

public class ApiMini {
    public static void main(String[] args) {
        var app = Javalin.create().start(7070);
        app.get("/halo", ctx -> ctx.result("Halo dari Javalin"));
        app.get("/produk/{id}", ctx -> {
            int id = Integer.parseInt(ctx.pathParam("id"));
            ctx.json(Map.of("id", id, "nama", "Kopi Gayo"));
        });
    }
}

// Quarkus: gaya anotasi JAX-RS
@Path("/halo")
public class HaloResource {
    @GET
    public String halo() { return "Halo dari Quarkus"; }
}`,
   out:null,
   pts:['Spring Boot: ekosistem terbesar.','Quarkus: startup cepat, cocok untuk container.','Javalin: minimalis, mudah dipelajari.','Play: reaktif, tanpa state.'],
   q:[['Framework yang terkenal dengan startup cepat dan native image?',['Quarkus','Play','Javalin'],0,'Quarkus dioptimalkan untuk cloud dan GraalVM.'],
      ['Framework paling minimalis di antara pilihan ini?',['Spring Boot','Javalin','Quarkus'],1,'Javalin sengaja dibuat kecil dan sederhana.']]},
  {k:'c',t:'Dokumentasi dengan Javadoc',nodes:['Documentation','Javadoc'],
   b:['<b>Javadoc</b> adalah komentar khusus yang diawali <code>/**</code> dan ditulis tepat di atas kelas atau method. Alat <code>javadoc</code> mengubah komentar ini menjadi situs dokumentasi HTML, persis seperti dokumentasi resmi Java yang kamu baca saat mencari method String.',
      'Gunakan tag standar: <code>@param</code> untuk setiap parameter, <code>@return</code> untuk nilai kembali, <code>@throws</code> untuk exception, dan <code>{@code ...}</code> untuk potongan kode. Kalimat pertama sebaiknya ringkasan satu baris tentang apa yang dilakukan method.',
      'Dokumentasikan <i>apa</i> dan <i>kenapa</i>, bukan mengulang kode baris per baris. IDE seperti IntelliJ menampilkan Javadoc saat kursor diarahkan ke method, sehingga rekan tim langsung paham cara memakainya.'],
   code:R`/**
 * Menghitung harga setelah diskon.
 *
 * <p>Diskon dibulatkan ke bawah ke rupiah terdekat.
 *
 * @param harga  harga awal dalam rupiah, tidak boleh negatif
 * @param persen besar diskon, dari 0 sampai 100
 * @return harga akhir setelah diskon
 * @throws IllegalArgumentException jika {@code persen} di luar 0..100
 */
public static long hargaDiskon(long harga, int persen) {
    if (persen < 0 || persen > 100) {
        throw new IllegalArgumentException("persen harus 0..100");
    }
    return harga - harga * persen / 100;
}

// Buat situs dokumentasi:
// javadoc -d docs src/com/toko/*.java
// mvn javadoc:javadoc`,
   out:null,
   pts:['Javadoc diawali <code>/**</code>, bukan <code>/*</code>.','Tag: @param, @return, @throws, {@code}.','Kalimat pertama = ringkasan.','Tulis kenapa dan bagaimana memakai, bukan menerjemahkan kode.'],
   q:[['Komentar Javadoc diawali dengan?',['//','/*','/**'],2,'Dua bintang menandai komentar dokumentasi.'],
      ['Tag untuk menjelaskan nilai kembali?',['@param','@return','@value'],1,'@return mendeskripsikan hasil method.']]}
 ]}
];
