/* ===================== DATA BAB ===================== */
const LEVELS = [
  {k:'Dasar', d:'Bab 1 sampai 6. Cara program berjalan, data, perulangan, percabangan, dan file.'},
  {k:'Menengah', d:'Bab 7 sampai 12. Array, kelas dan objek, pewarisan, koleksi, dan rekursi.'},
  {k:'Lanjutan', d:'Bab 13 sampai 19. Algoritma, struktur data buatan sendiri, dan gaya fungsional.'}
];

const CH = [
{n:1, lvl:'Dasar', t:'Program Pertama', en:'Basic Java Programs', py:'Pengantar pemrograman Python', viz:'compile',
 vizT:'Dari kode ke layar', vizD:'Bandingkan jalur Java (dikompilasi) dengan Python (diinterpretasi).',
 body:[
  'Program adalah daftar instruksi yang dijalankan komputer satu per satu. Setiap instruksi disebut <b>statement</b>. Di Java, statement diakhiri titik koma dan dikelompokkan dengan kurung kurawal. Di Python, pengelompokan memakai indentasi.',
  'Java <b>dikompilasi</b>: perintah <code>javac</code> memeriksa seluruh kode lalu menerjemahkannya menjadi <b>bytecode</b>, kemudian JVM menjalankannya. Python <b>diinterpretasi</b>: kamu cukup menjalankan <code>python halo.py</code>.',
  'Begitu program bertambah panjang, pecah menjadi bagian kecil bernama <b>method</b> (Java) atau <b>fungsi</b> (Python). Teknik ini disebut dekomposisi prosedural. Setiap bagian punya satu tugas yang jelas dan bisa dipanggil berkali-kali.'
 ],
 points:['Java wajib punya kelas dan method <code>main</code> sebagai titik awal.','Python menjalankan file dari atas ke bawah. Pola <code>main()</code> dipakai agar rapi.','Komentar (<code>//</code> di Java, <code>#</code> di Python) diabaikan komputer.','Nama method/fungsi sebaiknya kata kerja: <code>cetakLaporan</code>, <code>cetak_laporan</code>.'],
 tip:'Ketik ulang contoh kodenya, jangan hanya disalin. Kesalahan ketik kecil adalah cara tercepat mengenal pesan error.',
 java:`public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, dunia!");
        sapa();
        sapa();
    }

    // static method: memecah program jadi bagian kecil
    public static void sapa() {
        System.out.println("Selamat belajar!");
    }
}`,
 python:`def sapa():
    # fungsi: memecah program jadi bagian kecil
    print("Selamat belajar!")

def main():
    print("Halo, dunia!")
    sapa()
    sapa()

main()`,
 out:`Halo, dunia!
Selamat belajar!
Selamat belajar!`,
 cmp:[['Menjalankan','<code>javac Halo.java</code> lalu <code>java Halo</code>','<code>python halo.py</code>'],['Struktur minimum','Wajib kelas dan <code>main</code>','Boleh langsung menulis statement'],['Blok kode','Kurung kurawal <code>{ }</code> dan <code>;</code>','Titik dua <code>:</code> dan indentasi'],['Konvensi nama','camelCase: <code>hitungTotal</code>','snake_case: <code>hitung_total</code>']],
 terms:['statement','sintaks','compiler','interpreter','bytecode','jvm','method','komentar','dekomposisi'],
 quiz:[{q:'Apa yang dihasilkan perintah <code>javac Halo.java</code>?',o:['File bytecode Halo.class','Langsung tampil di layar','File halo.py','Tidak menghasilkan apa-apa'],a:0,w:'javac adalah compiler. Ia membuat bytecode yang kemudian dijalankan JVM.'},
       {q:'Di Python, apa yang menandai bahwa beberapa baris berada di dalam satu blok?',o:['Kurung kurawal','Indentasi (spasi di awal baris)','Titik koma','Tanda kutip'],a:1,w:'Python memakai indentasi sebagai bagian dari sintaks. Salah indentasi berarti error.'}]},

{n:2, lvl:'Dasar', t:'Data Primitif & Perulangan Pasti', en:'Primitive Data and Definite Loops', py:'Data dan perulangan pasti', viz:'forloop',
 vizT:'Menelusuri perulangan for', vizD:'Ikuti urutan inisialisasi, cek kondisi, badan loop, lalu update.',
 body:[
  'Data disimpan di <b>variabel</b>. Java mewajibkan kamu menulis <b>tipe data</b>: <code>int</code> untuk bilangan bulat, <code>double</code> untuk pecahan, <code>boolean</code> untuk benar/salah, <code>char</code> untuk satu karakter. Python menebak tipenya sendiri dari nilai yang diberikan.',
  'Ekspresi seperti <code>7 / 2</code> punya jebakan. Di Java, pembagian dua <code>int</code> membuang pecahannya sehingga hasilnya 3. Di Python, <code>/</code> selalu menghasilkan pecahan (3.5), sedangkan <code>//</code> adalah pembagian bulat. Operator <code>%</code> memberi sisa bagi dan sering dipakai untuk cek genap/ganjil.',
  '<b>Perulangan pasti</b> dipakai saat jumlah pengulangan sudah diketahui. Java memakai <code>for (init; kondisi; update)</code>. Python memakai <code>for i in range(awal, akhir)</code>, dengan <code>akhir</code> tidak ikut dihitung. Loop di dalam loop (nested loop) cocok untuk pola dua dimensi seperti segitiga bintang.'
 ],
 points:['<code>(double) a / b</code> mengubah tipe sebelum membagi (casting).','Urutan operasi: <code>* / %</code> dikerjakan sebelum <code>+ -</code>.','<code>range(1, 5)</code> menghasilkan 1, 2, 3, 4.','Konstanta ditulis HURUF_BESAR. Java memakai <code>final</code>.'],
 tip:'Saat loop terasa membingungkan, buat tabel di kertas berisi nilai setiap variabel per putaran. Visual di atas melakukan hal yang sama.',
 java:`public class Segitiga {
    public static final int TINGGI = 4;   // konstanta kelas

    public static void main(String[] args) {
        int a = 7, b = 2;
        System.out.println(a / b);           // 3  (pembagian bulat)
        System.out.println(a % b);           // 1  (sisa bagi)
        System.out.println((double) a / b);  // 3.5

        for (int baris = 1; baris <= TINGGI; baris++) {
            for (int k = 1; k <= baris; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}`,
 python:`TINGGI = 4  # konstanta (konvensi huruf besar)

def main():
    a, b = 7, 2
    print(a // b)   # 3  (pembagian bulat)
    print(a % b)    # 1  (sisa bagi)
    print(a / b)    # 3.5

    for baris in range(1, TINGGI + 1):
        for k in range(baris):
            print("*", end="")
        print()

main()`,
 out:`3
1
3.5
*
**
***
****`,
 cmp:[['Deklarasi','Tipe wajib: <code>int x = 5;</code>','Tanpa tipe: <code>x = 5</code>'],['Pembagian 7 / 2','<code>3</code> bila keduanya int','<code>3.5</code>; pakai <code>7 // 2</code> untuk 3'],['Perulangan pasti','<code>for (int i = 0; i &lt; n; i++)</code>','<code>for i in range(n)</code>'],['Pangkat','<code>Math.pow(2, 3)</code>','<code>2 ** 3</code>']],
 terms:['variabel','tipe-data','primitif','ekspresi','operator','modulus','precedence','casting','konstanta','perulangan','for','nested-loop'],
 quiz:[{q:'Berapa hasil <code>7 % 3</code>?',o:['1','2','0','2.33'],a:0,w:'7 dibagi 3 adalah 2 sisa 1. Operator % mengambil sisanya.'},
       {q:'Nilai apa saja yang dihasilkan <code>range(1, 5)</code>?',o:['1, 2, 3, 4, 5','1, 2, 3, 4','0, 1, 2, 3, 4, 5','1 dan 5'],a:1,w:'Batas akhir range tidak ikut. range(1, 5) berhenti sebelum 5.'}]},

{n:3, lvl:'Dasar', t:'Parameter & Objek', en:'Parameters and Objects', py:'Parameter dan grafis', viz:'callstack',
 vizT:'Call stack saat method dipanggil', vizD:'Setiap pemanggilan membuat bingkai baru berisi parameternya sendiri.',
 body:[
  '<b>Parameter</b> membuat method lebih umum. Daripada menulis <code>luasLingkaranJari3()</code>, tulis <code>luas(r)</code> dan kirim nilai apa pun. Nilai yang dikirim saat memanggil disebut <b>argumen</b>. Nilai yang dikirim balik memakai <code>return</code>.',
  'Setiap pemanggilan method mendapat ruang variabelnya sendiri di <b>call stack</b>. Variabel di dalam method hanya hidup di sana. Inilah yang disebut <b>scope</b>.',
  'Bab ini juga mengenalkan <b>objek</b> bawaan. <code>String</code> punya method seperti <code>length()</code> dan <code>toUpperCase()</code>. <code>Scanner</code> membaca masukan pengguna. Kelas <code>Math</code> menyediakan rumus siap pakai. Suplemen 3G buku ini memakai objek <code>DrawingPanel</code> untuk menggambar.'
 ],
 points:['Parameter Java wajib bertipe: <code>double luas(double r)</code>.','Fungsi Python tanpa <code>return</code> mengembalikan <code>None</code>.','<code>input()</code> di Python selalu menghasilkan string. Ubah dengan <code>int()</code> atau <code>float()</code>.','String tidak bisa diubah. <code>s.toUpperCase()</code> membuat string baru.'],
 tip:'Kalau satu method melakukan dua hal, misalnya menghitung sekaligus mencetak, pisahkan. Method yang me-return nilai lebih mudah diuji dan dipakai ulang.',
 java:`import java.util.Scanner;

public class Lingkaran {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Jari-jari? ");
        double r = input.nextDouble();
        System.out.println("Luas = " + luas(r));

        String nama = "Building Java";
        System.out.println(nama.length());        // 13
        System.out.println(nama.toUpperCase());   // BUILDING JAVA
        System.out.println(nama.substring(0, 8)); // Building
    }

    // parameter r, mengembalikan nilai double
    public static double luas(double r) {
        return Math.PI * Math.pow(r, 2);
    }
}`,
 python:`import math

def luas(r):
    # parameter r, mengembalikan nilai
    return math.pi * r ** 2

def main():
    r = float(input("Jari-jari? "))
    print("Luas =", luas(r))

    nama = "Building Python"
    print(len(nama))       # 15
    print(nama.upper())    # BUILDING PYTHON
    print(nama[0:8])       # Building

main()`,
 out:{java:`Jari-jari? 2
Luas = 12.566370614359172
13
BUILDING JAVA
Building`, python:`Jari-jari? 2
Luas = 12.566370614359172
15
BUILDING PYTHON
Building`},
 cmp:[['Tipe parameter','Wajib ditulis','Tidak ditulis (opsional: type hint)'],['Membaca input','<code>Scanner</code>: <code>nextInt()</code>, <code>nextLine()</code>','<code>input()</code> lalu konversi'],['Panjang string','<code>s.length()</code>','<code>len(s)</code>'],['Potong string','<code>s.substring(a, b)</code>','<code>s[a:b]</code>']],
 terms:['parameter','argumen','return','scope','call-stack','string','objek','scanner','library'],
 quiz:[{q:'Fungsi Python yang tidak punya <code>return</code> mengembalikan apa?',o:['0','None','String kosong','Error'],a:1,w:'Python otomatis mengembalikan None bila tidak ada return.'},
       {q:'Pada <code>luas(5)</code>, angka 5 disebut apa?',o:['Parameter','Argumen','Field','Konstanta'],a:1,w:'Argumen adalah nilai yang dikirim. Parameter adalah variabel penerimanya di definisi method.'}]},

{n:4, lvl:'Dasar', t:'Eksekusi Bersyarat', en:'Conditional Execution', py:'Eksekusi bersyarat', viz:'ifelse',
 vizT:'Jalur if / else if / else', vizD:'Geser skor dan lihat kondisi mana yang dicek, mana yang dilewati.',
 body:[
  'Percabangan membuat program memilih. <code>if</code> menjalankan blok hanya bila kondisinya benar. Rantai <code>if / else if / else</code> (Python: <code>if / elif / else</code>) dicek dari atas. Begitu satu kondisi benar, sisanya dilewati.',
  'Kondisi dibangun dari <b>operator relasional</b>: <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>, <code>==</code>, <code>!=</code>. Urutan kondisi penting. Jika <code>skor &gt;= 70</code> dicek lebih dulu, skor 95 akan ikut mendapat C.',
  'Bab ini juga membahas <b>algoritma kumulatif</b>: menyiapkan variabel penampung (misalnya <code>total = 0</code>) di luar loop lalu menambahkannya sedikit demi sedikit di dalam loop. Pola ini dipakai untuk jumlah, rata-rata, nilai maksimum, dan sebagainya.'
 ],
 points:['Gunakan <code>if/else if</code> bila pilihan saling eksklusif. Gunakan beberapa <code>if</code> terpisah bila boleh lebih dari satu.','Di Java, bandingkan isi String dengan <code>.equals()</code>, bukan <code>==</code>.','Variabel penampung kumulatif dideklarasikan di luar loop.','Method boleh punya beberapa <code>return</code> di cabang berbeda.'],
 tip:'Uji percabangan dengan nilai di batasnya: 89, 90, dan 91. Bug paling sering muncul tepat di tepi kondisi.',
 java:`public class Nilai {
    public static String huruf(int skor) {
        if (skor >= 90) {
            return "A";
        } else if (skor >= 80) {
            return "B";
        } else if (skor >= 70) {
            return "C";
        } else {
            return "D";
        }
    }

    public static void main(String[] args) {
        int total = 0;                       // penampung kumulatif
        for (int i = 1; i <= 10; i++) {
            total += i;
        }
        System.out.println("Jumlah 1..10 = " + total);
        System.out.println(huruf(85));
    }
}`,
 python:`def huruf(skor):
    if skor >= 90:
        return "A"
    elif skor >= 80:
        return "B"
    elif skor >= 70:
        return "C"
    else:
        return "D"

def main():
    total = 0                           # penampung kumulatif
    for i in range(1, 11):
        total += i
    print("Jumlah 1..10 =", total)
    print(huruf(85))

main()`,
 out:`Jumlah 1..10 = 55
B`,
 cmp:[['Cabang lanjutan','<code>else if</code>','<code>elif</code>'],['Kurung kondisi','Wajib: <code>if (x &gt; 0)</code>','Tidak perlu: <code>if x &gt; 0:</code>'],['Bandingkan string','<code>a.equals(b)</code>','<code>a == b</code>'],['Ekspresi bersyarat','<code>x &gt; 0 ? "pos" : "neg"</code>','<code>"pos" if x &gt; 0 else "neg"</code>']],
 terms:['kondisional','operator-relasional','blok','algoritma-kumulatif','boolean'],
 quiz:[{q:'Dengan method <code>huruf</code> di atas, berapa hasil <code>huruf(80)</code>?',o:['A','B','C','D'],a:1,w:'80 >= 90 salah, 80 >= 80 benar, jadi B. Kondisi berikutnya tidak dicek lagi.'},
       {q:'Di Java, cara yang benar untuk membandingkan isi dua String adalah...',o:['a == b','a.equals(b)','a = b','a === b'],a:1,w:'== membandingkan alamat objek, bukan isinya. equals membandingkan karakter demi karakter.'}]},

{n:5, lvl:'Dasar', t:'Logika & Perulangan Tak Pasti', en:'Program Logic and Indefinite Loops', py:'Logika program dan perulangan tak pasti', viz:'boolean',
 vizT:'Logika boolean & loop while', vizD:'Ubah p dan q, lalu lempar dadu sampai keluar angka 6.',
 body:[
  '<b>Perulangan tak pasti</b> dipakai ketika jumlah putaran belum diketahui, misalnya "ulangi sampai pengguna mengetik 0". Bentuknya <code>while (kondisi)</code>. Pastikan sesuatu di dalam loop mengubah kondisi, atau loop akan berjalan selamanya.',
  'Kondisi bisa digabung dengan <b>logika boolean</b>: AND (<code>&amp;&amp;</code> / <code>and</code>), OR (<code>||</code> / <code>or</code>), dan NOT (<code>!</code> / <code>not</code>). Keduanya memakai <b>short-circuit</b>: jika bagian kiri sudah menentukan hasil, bagian kanan tidak dievaluasi.',
  'Ada dua pola klasik. <b>Fencepost</b>: untuk mencetak <code>1, 2, 3</code> kamu butuh 3 angka tapi hanya 2 koma, jadi satu bagian ditaruh di luar loop. <b>Sentinel</b>: nilai khusus (misalnya -1) yang menandai akhir masukan. Bilangan acak dibuat dengan <code>Random</code> atau modul <code>random</code>.'
 ],
 points:['<code>while</code> mengecek kondisi sebelum setiap putaran. Bisa saja tidak pernah masuk.','Java punya <code>do/while</code> yang pasti berjalan minimal sekali.','<code>!(a &amp;&amp; b)</code> sama dengan <code>!a || !b</code> (hukum De Morgan).','<code>nextInt(6) + 1</code> dan <code>randint(1, 6)</code> sama-sama memberi 1 sampai 6.'],
 tip:'Sebelum menulis while, ucapkan kondisinya dalam bahasa sehari-hari: "selama dadu belum 6". Lalu terjemahkan apa adanya: <code>dadu != 6</code>.',
 java:`import java.util.Random;

public class Dadu {
    public static void main(String[] args) {
        Random acak = new Random();
        int lemparan = 0;
        int dadu = 0;
        while (dadu != 6) {                 // perulangan tak pasti
            dadu = acak.nextInt(6) + 1;     // 1..6
            lemparan++;
            System.out.println("Dapat " + dadu);
        }
        System.out.println("Butuh " + lemparan + " lemparan");

        boolean hujan = true, punyaPayung = false;
        if (hujan && !punyaPayung) {
            System.out.println("Tunggu reda dulu");
        }
    }
}`,
 python:`import random

def main():
    lemparan = 0
    dadu = 0
    while dadu != 6:                    # perulangan tak pasti
        dadu = random.randint(1, 6)     # 1..6
        lemparan += 1
        print("Dapat", dadu)
    print("Butuh", lemparan, "lemparan")

    hujan, punya_payung = True, False
    if hujan and not punya_payung:
        print("Tunggu reda dulu")

main()`,
 out:`Dapat 3
Dapat 1
Dapat 6
Butuh 3 lemparan
Tunggu reda dulu
(angka dadu acak, hasilmu bisa berbeda)`,
 cmp:[['Operator logika','<code>&amp;&amp;</code>, <code>||</code>, <code>!</code>','<code>and</code>, <code>or</code>, <code>not</code>'],['Nilai boolean','<code>true</code>, <code>false</code>','<code>True</code>, <code>False</code>'],['Tambah satu','<code>x++</code>','<code>x += 1</code>'],['Minimal sekali jalan','<code>do { } while (...);</code>','<code>while True:</code> + <code>break</code>']],
 terms:['while','do-while','perulangan-tak-hingga','logika-boolean','short-circuit','fencepost','sentinel','pseudorandom'],
 quiz:[{q:'Apa hasil <code>true || (10 / 0 &gt; 1)</code> di Java?',o:['Error pembagian nol','true','false','Tidak bisa dikompilasi'],a:1,w:'Short-circuit: karena kiri sudah true, OR pasti true. Bagian kanan tidak pernah dihitung.'},
       {q:'Masalah fencepost muncul ketika...',o:['Loop tidak pernah berhenti','Ada n bagian tapi hanya n-1 pemisah, jadi satu bagian harus di luar loop','Variabel belum dideklarasikan','Indeks array negatif'],a:1,w:'Seperti pagar: 4 tiang hanya butuh 3 kawat. Cetak satu elemen dulu, lalu loop mencetak "pemisah + elemen".'}]},

{n:6, lvl:'Dasar', t:'Pemrosesan File', en:'File Processing', py:'Pemrosesan file', viz:'file',
 vizT:'Membaca file token demi token', vizD:'Lihat bagaimana setiap baris dipecah menjadi token lalu dijumlahkan.',
 body:[
  'Program nyata membaca data dari file, bukan hanya dari keyboard. Di Java, <code>Scanner</code> yang sama bisa diarahkan ke <code>new File("nilai.txt")</code>. Di Python, gunakan <code>open()</code> di dalam blok <code>with</code> agar file otomatis ditutup.',
  'Ada dua cara membaca. <b>Berbasis token</b>: membaca potongan yang dipisah spasi (<code>next()</code>, <code>nextInt()</code>). <b>Berbasis baris</b>: membaca satu baris utuh lalu memecahnya. Pola paling aman adalah membaca per baris, lalu memecah baris itu menjadi token.',
  'Membuka file bisa gagal, misalnya karena file tidak ada. Java memaksa kamu menangani kemungkinan itu (<code>throws FileNotFoundException</code>), karena ini termasuk <b>checked exception</b>. Python melempar <code>FileNotFoundError</code> yang bisa ditangkap dengan <code>try/except</code>.'
 ],
 points:['<code>hasNextInt()</code> mengecek dulu sebelum <code>nextInt()</code>, supaya tidak crash.','<code>str.split()</code> memecah string berdasarkan spasi.','Menulis file: <code>PrintStream</code> di Java, <code>open(nama, "w")</code> di Python.','Isi contoh <code>nilai.txt</code>: dua baris, "Budi 85 90" dan "Sari 78 92".'],
 tip:'Buat file contoh kecil (3 sampai 5 baris) saat menguji. Setelah benar, baru coba file besar.',
 java:`import java.io.*;
import java.util.*;

public class RataRata {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner file = new Scanner(new File("nilai.txt"));
        while (file.hasNextLine()) {
            String baris = file.nextLine();      // "Budi 85 90"
            Scanner token = new Scanner(baris);
            String nama = token.next();
            int total = 0, n = 0;
            while (token.hasNextInt()) {
                total += token.nextInt();
                n++;
            }
            System.out.println(nama + ": " + (double) total / n);
        }
    }
}`,
 python:`def main():
    with open("nilai.txt") as file:
        for baris in file:                   # "Budi 85 90"
            token = baris.split()
            nama = token[0]
            total = 0
            for t in token[1:]:
                total += int(t)
            print(nama + ":", total / (len(token) - 1))

main()`,
 out:`Budi: 87.5
Sari: 85.0`,
 cmp:[['Buka file','<code>new Scanner(new File("a.txt"))</code>','<code>open("a.txt")</code>'],['Per baris','<code>hasNextLine()</code> + <code>nextLine()</code>','<code>for baris in file:</code>'],['Pecah token','<code>Scanner</code> atas String','<code>baris.split()</code>'],['File tidak ada','<code>FileNotFoundException</code> (wajib ditangani)','<code>FileNotFoundError</code>']],
 terms:['file-io','token','scanner','exception','checked-exception'],
 quiz:[{q:'Token berikutnya adalah "abc". Apa hasil <code>hasNextInt()</code>?',o:['true','false','Error','0'],a:1,w:'hasNextInt hanya melihat, tidak membaca. "abc" bukan bilangan bulat, jadi false.'},
       {q:'Mengapa memakai <code>with open(...)</code> di Python?',o:['Supaya lebih cepat','File otomatis ditutup walau terjadi error','Wajib secara sintaks','Untuk membuat file baru'],a:1,w:'Blok with menjamin file ditutup saat blok selesai.'}]},

{n:7, lvl:'Menengah', t:'Array', en:'Arrays', py:'List', viz:'array',
 vizT:'Indeks dan referensi', vizD:'Akses elemen lewat indeks, lalu lihat apa yang terjadi saat dua variabel menunjuk array yang sama.',
 body:[
  '<b>Array</b> menyimpan banyak nilai bertipe sama di bawah satu nama. Setiap elemen punya <b>indeks</b> mulai dari 0. Array 5 elemen punya indeks 0 sampai 4. Mengakses indeks 5 menghasilkan <code>ArrayIndexOutOfBoundsException</code>. Python memakai <b>list</b> yang mirip, tapi ukurannya bisa berubah.',
  'Pola paling umum adalah <b>traversal</b>: mengunjungi setiap elemen dengan loop untuk mencari maksimum, menjumlah, atau menghitung. For-each (<code>for (int x : a)</code> / <code>for x in a</code>) cocok bila kamu tidak butuh indeksnya.',
  'Array dan list adalah objek, jadi variabelnya menyimpan <b>referensi</b> (alamat), bukan isinya. <code>b = a</code> tidak menyalin isi. Keduanya menunjuk array yang sama, sehingga perubahan lewat <code>b</code> juga terlihat di <code>a</code>. Hal yang sama berlaku saat array dikirim sebagai parameter.'
 ],
 points:['Ukuran array Java tetap setelah dibuat: <code>new int[5]</code>.','Python mengizinkan indeks negatif: <code>a[-1]</code> adalah elemen terakhir.','Cetak array Java dengan <code>Arrays.toString(a)</code>, bukan <code>println(a)</code>.','Array 2D: <code>int[][] m = new int[3][4];</code>'],
 tip:'Batas loop yang benar hampir selalu <code>i &lt; a.length</code>, bukan <code>&lt;=</code>. Kesalahan satu langkah ini disebut off-by-one.',
 java:`import java.util.Arrays;

public class Larik {
    public static void main(String[] args) {
        int[] a = {3, 8, 1, 9, 4};
        System.out.println(a[0]);         // 3
        System.out.println(a.length);     // 5

        int maks = a[0];
        for (int x : a) {                 // for-each
            if (x > maks) {
                maks = x;
            }
        }
        System.out.println("Maks: " + maks);

        int[] b = a;      // b menunjuk array yang SAMA
        b[0] = 99;
        System.out.println(Arrays.toString(a));
    }
}`,
 python:`def main():
    a = [3, 8, 1, 9, 4]
    print(a[0])       # 3
    print(len(a))     # 5

    maks = a[0]
    for x in a:
        if x > maks:
            maks = x
    print("Maks:", maks)

    b = a             # b menunjuk list yang SAMA
    b[0] = 99
    print(a)

main()`,
 out:`3
5
Maks: 9
[99, 8, 1, 9, 4]`,
 cmp:[['Ukuran','Tetap','Bisa tumbuh: <code>append</code>'],['Isi','Satu tipe','Boleh campur tipe'],['Panjang','<code>a.length</code> (tanpa kurung)','<code>len(a)</code>'],['Menyalin','<code>Arrays.copyOf(a, a.length)</code>','<code>a.copy()</code> atau <code>a[:]</code>']],
 terms:['array','list','indeks','traversal','off-by-one','referensi'],
 quiz:[{q:'Array Java berisi 5 elemen. Berapa indeks elemen terakhir?',o:['5','4','6','-1'],a:1,w:'Indeks mulai dari 0, jadi elemen terakhir ada di panjang - 1.'},
       {q:'Setelah <code>b = a; b[0] = 99;</code>, berapa nilai <code>a[0]</code>?',o:['3 (tetap)','99','Error','0'],a:1,w:'a dan b adalah dua nama untuk array yang sama.'}]},

{n:8, lvl:'Menengah', t:'Kelas & Objek', en:'Classes', py:'Kelas dan objek', viz:'objects',
 vizT:'Satu cetak biru, banyak objek', vizD:'Buat beberapa objek Titik dan ubah masing-masing secara terpisah.',
 body:[
  '<b>Kelas</b> adalah cetak biru. <b>Objek</b> adalah benda nyata yang dibuat dari cetak biru itu. Kelas <code>Titik</code> mendefinisikan bahwa setiap titik punya <code>x</code> dan <code>y</code> (disebut <b>field</b>) serta bisa <code>geser()</code> (disebut method instance).',
  '<b>Konstruktor</b> dijalankan saat objek dibuat dengan <code>new Titik(3, 4)</code> di Java atau <code>Titik(3, 4)</code> di Python. Tugasnya mengisi nilai awal field. Kata <code>this</code> (Java) dan <code>self</code> (Python) merujuk ke objek yang sedang dipakai.',
  '<b>Enkapsulasi</b> berarti menyembunyikan field (<code>private</code>) dan hanya membuka method tertentu. Dengan begitu objek bisa menjaga datanya tetap valid. Method <code>toString()</code> / <code>__str__</code> menentukan bagaimana objek tampil saat dicetak.'
 ],
 points:['Setiap objek punya salinan field sendiri.','Python tidak punya <code>private</code>. Konvensinya: awali nama dengan <code>_</code>.','Java memberi nilai default (0, null). Python mewajibkan field dibuat di <code>__init__</code>.','Method yang mengubah objek disebut mutator, yang hanya membaca disebut accessor.'],
 tip:'Rancang kelas dari kata benda dalam soal (Titik, Akun, Mahasiswa). Kata kerjanya menjadi method.',
 java:`public class Titik {
    private int x, y;                     // field (dienkapsulasi)

    public Titik(int x, int y) {          // konstruktor
        this.x = x;
        this.y = y;
    }

    public void geser(int dx, int dy) {
        x += dx;
        y += dy;
    }

    public double jarakKeAsal() {
        return Math.sqrt(x * x + y * y);
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        Titik p = new Titik(3, 4);
        System.out.println(p + " jarak " + p.jarakKeAsal());
        p.geser(1, -1);
        System.out.println(p);
    }
}`,
 python:`import math

class Titik:
    def __init__(self, x, y):         # konstruktor
        self._x = x                    # _ = "privat" (konvensi)
        self._y = y

    def geser(self, dx, dy):
        self._x += dx
        self._y += dy

    def jarak_ke_asal(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __str__(self):
        return f"({self._x}, {self._y})"

p = Titik(3, 4)
print(p, "jarak", p.jarak_ke_asal())
p.geser(1, -1)
print(p)`,
 out:`(3, 4) jarak 5.0
(4, 3)`,
 cmp:[['Konstruktor','Nama sama dengan kelas','<code>__init__</code>'],['Objek saat ini','<code>this</code> (sering opsional)','<code>self</code> (wajib jadi parameter pertama)'],['Privat','<code>private</code>, ditegakkan compiler','Konvensi <code>_nama</code>'],['Teks objek','<code>toString()</code>','<code>__str__</code>']],
 terms:['kelas','objek','instance','field','konstruktor','this-self','enkapsulasi','tostring'],
 quiz:[{q:'Apa tugas konstruktor?',o:['Menghapus objek','Mengisi nilai awal objek baru','Mencetak objek','Membandingkan dua objek'],a:1,w:'Konstruktor berjalan sekali saat objek dibuat dan menyiapkan field-nya.'},
       {q:'Mengapa field sebaiknya <code>private</code>?',o:['Supaya program lebih cepat','Supaya data hanya bisa diubah lewat method yang menjaga validitasnya','Diwajibkan Java','Supaya bisa diwarisi'],a:1,w:'Itulah enkapsulasi. Kode luar tidak bisa mengisi nilai sembarangan.'}]},

{n:9, lvl:'Menengah', t:'Pewarisan & Interface', en:'Inheritance and Interfaces', py:'Pewarisan', viz:'inherit',
 vizT:'Hierarki kelas dan polimorfisme', vizD:'Pilih kelas anak untuk melihat method yang diwarisi dan yang di-override.',
 body:[
  '<b>Pewarisan</b> membuat kelas baru dari kelas yang sudah ada. <code>Kucing extends Hewan</code> berarti Kucing otomatis punya semua field dan method Hewan. Kelas induk disebut <b>superclass</b>, kelas anak disebut <b>subclass</b>. Hubungannya selalu "adalah": kucing adalah hewan.',
  'Subclass boleh <b>meng-override</b> method induk untuk mengganti perilakunya. Karena itu, variabel bertipe <code>Hewan</code> bisa menunjuk Kucing atau Anjing, dan <code>h.suara()</code> menjalankan versi milik objek sebenarnya. Inilah <b>polimorfisme</b>.',
  '<b>Interface</b> adalah kontrak berisi daftar method tanpa isi. Kelas yang meng-<i>implement</i>-nya wajib menyediakan semua method itu. <b>Kelas abstrak</b> berada di tengah: boleh punya method lengkap dan method abstrak, tapi tidak bisa dibuat objeknya langsung. Lab "Critters" di buku ini melatih semua konsep tersebut.'
 ],
 points:['<code>super(...)</code> memanggil konstruktor induk.','Java hanya mengizinkan satu superclass, tapi banyak interface.','Python mengizinkan banyak kelas induk sekaligus.','Override: nama dan parameter sama. Overload: nama sama, parameter berbeda.'],
 tip:'Jangan memakai pewarisan hanya untuk berbagi kode. Pakai hanya bila hubungan "adalah" benar-benar masuk akal.',
 java:`interface Bersuara {
    String suara();
}

abstract class Hewan implements Bersuara {
    protected String nama;
    public Hewan(String nama) { this.nama = nama; }
    public String kenalkan() {
        return nama + " berkata " + suara();
    }
}

class Kucing extends Hewan {
    public Kucing(String n) { super(n); }
    public String suara() { return "Meong"; }
}

class Anjing extends Hewan {
    public Anjing(String n) { super(n); }
    public String suara() { return "Guk"; }
}

public class Kebun {
    public static void main(String[] args) {
        Hewan[] kebun = { new Kucing("Tom"), new Anjing("Spike") };
        for (Hewan h : kebun) {
            System.out.println(h.kenalkan());   // polimorfisme
        }
    }
}`,
 python:`from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def suara(self):            # wajib di-override
        pass

    def kenalkan(self):
        return f"{self.nama} berkata {self.suara()}"

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk"

kebun = [Kucing("Tom"), Anjing("Spike")]
for h in kebun:
    print(h.kenalkan())         # polimorfisme`,
 out:`Tom berkata Meong
Spike berkata Guk`,
 cmp:[['Mewarisi','<code>class A extends B</code>','<code>class A(B):</code>'],['Panggil induk','<code>super(nama)</code>','<code>super().__init__(nama)</code>'],['Kontrak','<code>interface</code>','<code>ABC</code> atau duck typing'],['Banyak induk','Hanya lewat interface','Boleh: <code>class A(B, C):</code>']],
 terms:['pewarisan','superclass','subclass','override','overload','polimorfisme','interface','kelas-abstrak'],
 quiz:[{q:'Apa arti polimorfisme?',o:['Satu kelas punya banyak konstruktor','Satu pemanggilan method berperilaku berbeda sesuai jenis objek sebenarnya','Kelas tidak bisa diwarisi','Variabel bisa berganti nama'],a:1,w:'h.suara() memanggil versi Kucing atau Anjing tergantung objek yang ditunjuk h.'},
       {q:'Kata kunci Java untuk memanggil konstruktor kelas induk?',o:['this','super','parent','base'],a:1,w:'super(...) harus menjadi baris pertama konstruktor subclass.'}]},

{n:10, lvl:'Menengah', t:'ArrayList', en:'ArrayLists', py:'List (lanjutan)', viz:'arraylist',
 vizT:'Menyisip dan menghapus elemen', vizD:'Perhatikan elemen yang bergeser saat kamu menyisip atau menghapus di tengah.',
 body:[
  'Array berukuran tetap sering merepotkan. <code>ArrayList</code> adalah daftar yang bisa tumbuh dan menyusut sendiri. Kamu bisa <code>add</code>, <code>remove</code>, <code>get</code>, dan <code>set</code> tanpa memikirkan ukuran. List bawaan Python sudah bekerja seperti ini sejak awal.',
  'ArrayList memakai <b>generics</b>: <code>ArrayList&lt;String&gt;</code> berarti daftar yang hanya berisi String. Generics hanya menerima tipe objek, jadi untuk angka kamu memakai <b>wrapper class</b> <code>Integer</code>, <code>Double</code>, dan seterusnya. Java mengubah <code>int</code> ke <code>Integer</code> secara otomatis (autoboxing).',
  'Menyisip atau menghapus di tengah membuat elemen di belakangnya <b>bergeser</b>. Akibatnya, menghapus elemen sambil berjalan maju dengan loop indeks bisa melewatkan elemen. Solusinya: jalan mundur dari belakang, atau buat list baru.'
 ],
 points:['<code>list.size()</code> di Java, <code>len(lst)</code> di Python.','<code>remove(1)</code> menghapus indeks 1. <code>remove("a")</code> menghapus nilai "a".','<code>contains</code> / <code>in</code> untuk mengecek keberadaan.','Python: list comprehension <code>[x * 2 for x in a]</code> membuat list baru dengan ringkas.'],
 tip:'Bayangkan antrean bangku bioskop. Kalau satu orang keluar dari tengah, semua orang di belakangnya bergeser satu kursi. Itulah biaya remove di tengah ArrayList.',
 java:`import java.util.ArrayList;

public class Daftar {
    public static void main(String[] args) {
        ArrayList<String> buah = new ArrayList<>();
        buah.add("apel");
        buah.add("jeruk");
        buah.add(1, "mangga");       // sisip di indeks 1
        System.out.println(buah);    // [apel, mangga, jeruk]

        buah.remove(0);              // sisanya bergeser ke kiri
        System.out.println(buah.get(0) + ", ukuran " + buah.size());

        ArrayList<Integer> angka = new ArrayList<>();  // Integer = wrapper
        for (int i = 1; i <= 5; i++) {
            angka.add(i * i);
        }
        System.out.println(angka);
    }
}`,
 python:`def main():
    buah = []
    buah.append("apel")
    buah.append("jeruk")
    buah.insert(1, "mangga")     # sisip di indeks 1
    print(buah)                  # ['apel', 'mangga', 'jeruk']

    buah.pop(0)                  # sisanya bergeser ke kiri
    print(buah[0] + ", ukuran", len(buah))

    angka = [i * i for i in range(1, 6)]
    print(angka)

main()`,
 out:{java:`[apel, mangga, jeruk]
mangga, ukuran 2
[1, 4, 9, 16, 25]`, python:`['apel', 'mangga', 'jeruk']
mangga, ukuran 2
[1, 4, 9, 16, 25]`},
 cmp:[['Tambah di akhir','<code>add(x)</code>','<code>append(x)</code>'],['Sisip','<code>add(i, x)</code>','<code>insert(i, x)</code>'],['Hapus indeks','<code>remove(i)</code>','<code>pop(i)</code> atau <code>del a[i]</code>'],['Angka','Wajib wrapper: <code>ArrayList&lt;Integer&gt;</code>','Langsung saja']],
 terms:['arraylist','list','generics','wrapper-class','autoboxing'],
 quiz:[{q:'List berisi [a, b, c, d]. Setelah <code>remove(1)</code>, isinya menjadi...',o:['[a, c, d]','[b, c, d]','[a, b, d]','[a, b, c]'],a:0,w:'Indeks 1 adalah b. Setelah dihapus, c dan d bergeser ke kiri.'},
       {q:'Mengapa <code>ArrayList&lt;int&gt;</code> tidak boleh di Java?',o:['Terlalu lambat','Generics hanya menerima tipe objek, jadi pakai Integer','int sudah usang','Sebenarnya boleh'],a:1,w:'Tipe primitif bukan objek. Wrapper class Integer membungkusnya.'}]},

{n:11, lvl:'Menengah', t:'Java Collections Framework', en:'Java Collection Framework', py:'Dictionary dan set', viz:'collections',
 vizT:'List, Set, dan Map dari kalimat yang sama', vizD:'Ketik kalimatmu sendiri dan lihat bagaimana tiap koleksi menyimpannya.',
 body:[
  'Selain List, ada dua koleksi penting. <b>Set</b> adalah himpunan: tidak ada duplikat dan pengecekan <code>contains</code> sangat cepat. <b>Map</b> (Python: <b>dictionary</b>) memasangkan <b>kunci</b> dengan <b>nilai</b>, misalnya kata dengan jumlah kemunculannya.',
  'Java menyediakan beberapa implementasi. <code>HashSet</code>/<code>HashMap</code> sangat cepat tapi urutannya acak. <code>TreeSet</code>/<code>TreeMap</code> sedikit lebih lambat tapi selalu terurut. Kamu menulis kode terhadap <b>interface</b> (<code>Set</code>, <code>Map</code>) supaya implementasinya mudah diganti.',
  'Koleksi-koleksi ini adalah contoh <b>abstract data type</b>: kamu tahu operasinya (tambah, hapus, cari) tanpa perlu tahu cara kerjanya di dalam. Untuk menjelajahi isinya, gunakan for-each atau <b>iterator</b>.'
 ],
 points:['<code>map.getOrDefault(k, 0)</code> dan <code>d.get(k, 0)</code> menghindari error kunci belum ada.','Kunci Map unik. <code>put</code> pada kunci yang sama menimpa nilai lama.','Python <code>dict</code> menyimpan urutan saat data dimasukkan.','Pilih koleksi dari pertanyaannya: urutan penting? duplikat boleh? butuh pasangan?'],
 tip:'Hampir setiap soal "hitung berapa kali X muncul" diselesaikan dengan Map dari X ke jumlah.',
 java:`import java.util.*;

public class HitungKata {
    public static void main(String[] args) {
        String teks = "satu dua tiga dua satu satu";
        Set<String> unik = new TreeSet<>();
        Map<String, Integer> jumlah = new TreeMap<>();

        for (String kata : teks.split(" ")) {
            unik.add(kata);
            jumlah.put(kata, jumlah.getOrDefault(kata, 0) + 1);
        }
        System.out.println(unik);
        System.out.println(jumlah);
    }
}`,
 python:`def main():
    teks = "satu dua tiga dua satu satu"
    unik = set()
    jumlah = {}

    for kata in teks.split():
        unik.add(kata)
        jumlah[kata] = jumlah.get(kata, 0) + 1

    print(sorted(unik))
    print(jumlah)

main()`,
 out:{java:`[dua, satu, tiga]
{dua=2, satu=3, tiga=1}`, python:`['dua', 'satu', 'tiga']
{'satu': 3, 'dua': 2, 'tiga': 1}`},
 cmp:[['Himpunan','<code>HashSet</code>, <code>TreeSet</code>','<code>set()</code>, <code>{1, 2}</code>'],['Kunci ke nilai','<code>HashMap</code>, <code>TreeMap</code>','<code>dict</code>, <code>{"a": 1}</code>'],['Ambil nilai','<code>map.get(k)</code>','<code>d[k]</code> atau <code>d.get(k)</code>'],['Urutkan','<code>TreeSet</code> / <code>TreeMap</code>','<code>sorted(...)</code>']],
 terms:['collection','set','map','iterator','adt'],
 quiz:[{q:'Kata "a" dimasukkan dua kali ke Set kosong. Berapa ukurannya?',o:['2','1','0','Error'],a:1,w:'Set menolak duplikat secara diam-diam.'},
       {q:'Struktur paling cocok untuk menyimpan kata dan jumlah kemunculannya?',o:['List','Set','Map / dictionary','Array 2D'],a:2,w:'Map memasangkan kunci (kata) dengan nilai (jumlah).'}]},

{n:12, lvl:'Menengah', t:'Rekursi', en:'Recursion', py:'Rekursi', viz:'recursion',
 vizT:'Tumpukan pemanggilan faktorial', vizD:'Pemanggilan menumpuk sampai base case, lalu hasilnya kembali satu per satu.',
 body:[
  '<b>Rekursi</b> adalah method yang memanggil dirinya sendiri untuk menyelesaikan versi masalah yang lebih kecil. <code>faktorial(4)</code> sama dengan <code>4 * faktorial(3)</code>, dan seterusnya sampai <code>faktorial(1)</code>.',
  'Setiap rekursi butuh dua bagian. <b>Base case</b> adalah kasus paling kecil yang langsung dijawab tanpa rekursi. <b>Recursive case</b> memecah masalah dan memanggil diri sendiri dengan input yang mendekati base case. Tanpa base case, pemanggilan tidak pernah berhenti dan program kehabisan memori stack.',
  'Rekursi sangat cocok untuk struktur yang bersifat rekursif: folder di dalam folder, pohon, dan fraktal. Bab ini juga mengenalkan <b>backtracking</b>: mencoba satu pilihan, dan bila buntu, mundur lalu mencoba pilihan lain.'
 ],
 points:['Percayai pemanggilan rekursif: anggap ia sudah benar untuk input yang lebih kecil.','Setiap pemanggilan punya variabel sendiri di call stack.','Java: <code>StackOverflowError</code>. Python: <code>RecursionError</code> (batas sekitar 1000).','Sebagian rekursi bisa ditulis ulang dengan loop.'],
 tip:'Tulis base case lebih dulu. Lalu tanyakan: "jika aku sudah punya jawaban untuk n-1, bagaimana mendapat jawaban untuk n?"',
 java:`public class Rekursi {
    public static int faktorial(int n) {
        if (n <= 1) {
            return 1;                     // base case
        }
        return n * faktorial(n - 1);      // recursive case
    }

    public static String balik(String s) {
        if (s.length() <= 1) {
            return s;
        }
        return balik(s.substring(1)) + s.charAt(0);
    }

    public static void main(String[] args) {
        System.out.println(faktorial(4));
        System.out.println(balik("java"));
    }
}`,
 python:`def faktorial(n):
    if n <= 1:
        return 1                      # base case
    return n * faktorial(n - 1)       # recursive case

def balik(s):
    if len(s) <= 1:
        return s
    return balik(s[1:]) + s[0]

print(faktorial(4))
print(balik("python"))`,
 out:{java:`24
avaj`, python:`24
nohtyp`},
 cmp:[['Batas kedalaman','Bergantung ukuran stack JVM','Sekitar 1000 (bisa diubah)'],['Error','<code>StackOverflowError</code>','<code>RecursionError</code>'],['Potong string','<code>s.substring(1)</code>','<code>s[1:]</code>']],
 terms:['rekursi','base-case','recursive-case','call-stack','stack-overflow','backtracking'],
 quiz:[{q:'Apa yang terjadi jika rekursi tidak punya base case?',o:['Hasilnya 0','StackOverflowError / RecursionError','Menjadi loop biasa','Compiler menolak'],a:1,w:'Pemanggilan terus menumpuk sampai memori stack habis.'},
       {q:'Berapa <code>faktorial(3)</code>?',o:['3','6','9','1'],a:1,w:'3 * 2 * 1 = 6.'}]},

{n:13, lvl:'Lanjutan', t:'Pencarian & Pengurutan', en:'Searching and Sorting', py:'Pencarian dan pengurutan', viz:'sorting',
 vizT:'Selection sort dan binary search', vizD:'Jalankan langkah demi langkah dan hitung berapa perbandingan yang dibutuhkan.',
 body:[
  '<b>Pencarian linear</b> memeriksa elemen satu per satu dari depan. Mudah, tapi untuk sejuta data bisa butuh sejuta langkah. <b>Binary search</b> jauh lebih cepat: lihat elemen tengah, lalu buang separuh data yang pasti tidak berisi target. Syaratnya, data harus sudah terurut.',
  'Kecepatan algoritma diukur dengan notasi <b>Big-O</b>, yaitu bagaimana jumlah langkah tumbuh seiring jumlah data <i>n</i>. Linear search O(n), binary search O(log n). Untuk sejuta data, log₂ hanya sekitar 20 langkah.',
  '<b>Selection sort</b> mencari elemen terkecil lalu menukarnya ke depan, diulang untuk setiap posisi. Hasilnya O(n²). <b>Merge sort</b> membagi data menjadi dua, mengurutkan masing-masing secara rekursif, lalu menggabungkannya, dengan hasil O(n log n). Dalam praktik, pakai pengurutan bawaan bahasa.'
 ],
 points:['Binary search pada data acak memberi jawaban yang salah.','O(1) konstan, O(log n) logaritmik, O(n) linear, O(n²) kuadratik.','<code>Arrays.sort</code> dan <code>sorted()</code> sudah sangat dioptimalkan.','Python bisa menukar tanpa variabel bantu: <code>a, b = b, a</code>.'],
 tip:'Hitung langkah dengan tangan untuk 8 data, lalu 16 data. Pola pertumbuhannya akan memperlihatkan Big-O-nya.',
 java:`public class Cari {
    // binary search: data HARUS sudah terurut
    public static int cariBiner(int[] a, int target) {
        int kiri = 0, kanan = a.length - 1;
        while (kiri <= kanan) {
            int tengah = (kiri + kanan) / 2;
            if (a[tengah] == target) {
                return tengah;
            } else if (a[tengah] < target) {
                kiri = tengah + 1;
            } else {
                kanan = tengah - 1;
            }
        }
        return -1;   // tidak ditemukan
    }

    public static void selectionSort(int[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[min]) {
                    min = j;
                }
            }
            int tmp = a[i];      // tukar
            a[i] = a[min];
            a[min] = tmp;
        }
    }
}`,
 python:`def cari_biner(a, target):
    # data HARUS sudah terurut
    kiri, kanan = 0, len(a) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if a[tengah] == target:
            return tengah
        elif a[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1   # tidak ditemukan

def selection_sort(a):
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]   # tukar`,
 out:null,
 cmp:[['Urutkan bawaan','<code>Arrays.sort(a)</code>, <code>Collections.sort(list)</code>','<code>a.sort()</code>, <code>sorted(a)</code>'],['Binary search bawaan','<code>Arrays.binarySearch(a, x)</code>','modul <code>bisect</code>'],['Tukar dua nilai','Butuh variabel <code>tmp</code>','<code>a[i], a[j] = a[j], a[i]</code>']],
 terms:['pencarian-linear','binary-search','big-o','sorting','selection-sort','merge-sort'],
 quiz:[{q:'Binary search pada 1.000.000 data terurut butuh paling banyak sekitar...',o:['1.000.000 langkah','500.000 langkah','20 langkah','1 langkah'],a:2,w:'Setiap langkah membagi dua: 2²⁰ ≈ 1 juta, jadi sekitar 20 langkah.'},
       {q:'Kompleksitas selection sort adalah...',o:['O(n)','O(log n)','O(n²)','O(1)'],a:2,w:'Ada loop di dalam loop yang masing-masing berjalan sekitar n kali.'}]},

{n:14, lvl:'Lanjutan', t:'Stack & Queue', en:'Stacks and Queues', py:'Stack dan queue', viz:'stackqueue',
 vizT:'LIFO lawan FIFO', vizD:'Masukkan dan keluarkan nilai. Perhatikan siapa yang keluar lebih dulu.',
 body:[
  '<b>Stack</b> (tumpukan) bekerja seperti tumpukan piring: yang terakhir ditaruh, pertama diambil (LIFO, last in first out). Operasinya <code>push</code> untuk menaruh, <code>pop</code> untuk mengambil, dan <code>peek</code> untuk melihat yang paling atas.',
  '<b>Queue</b> (antrean) bekerja seperti antrean kasir: yang pertama datang, pertama dilayani (FIFO, first in first out). Elemen ditambah di belakang dan diambil dari depan.',
  'Keduanya terlihat sederhana tetapi dipakai di mana-mana. Tombol undo dan pengecekan kurung seimbang memakai stack. Antrean cetak, penjadwalan proses, dan pencarian melebar (BFS) memakai queue.'
 ],
 points:['Stack dan queue hanya mengizinkan akses di ujungnya. Tidak ada akses indeks.','Java: <code>Stack</code> atau <code>ArrayDeque</code>. Queue memakai <code>LinkedList</code>.','Python: list untuk stack, <code>collections.deque</code> untuk queue.','<code>list.pop(0)</code> di Python lambat (O(n)). Pakai <code>deque.popleft()</code>.'],
 tip:'Latihan klasik: cek apakah "(()[{}])" seimbang memakai stack. Push setiap kurung buka, pop saat bertemu kurung tutup.',
 java:`import java.util.*;

public class TumpukAntre {
    public static void main(String[] args) {
        Stack<String> tumpukan = new Stack<>();
        tumpukan.push("piring1");
        tumpukan.push("piring2");
        System.out.println(tumpukan.pop());   // LIFO

        Queue<String> antre = new LinkedList<>();
        antre.add("Ani");
        antre.add("Budi");
        System.out.println(antre.remove());   // FIFO
    }
}`,
 python:`from collections import deque

tumpukan = []
tumpukan.append("piring1")
tumpukan.append("piring2")
print(tumpukan.pop())        # LIFO

antre = deque()
antre.append("Ani")
antre.append("Budi")
print(antre.popleft())       # FIFO`,
 out:`piring2
Ani`,
 cmp:[['Stack','<code>push</code>, <code>pop</code>, <code>peek</code>','<code>append</code>, <code>pop</code>, <code>s[-1]</code>'],['Queue','<code>add</code>, <code>remove</code>, <code>peek</code>','<code>append</code>, <code>popleft</code>, <code>q[0]</code>'],['Kosong?','<code>isEmpty()</code>','<code>not s</code> atau <code>len(s) == 0</code>']],
 terms:['stack','queue','deque','adt'],
 quiz:[{q:'Push 1, 2, 3 ke stack, lalu pop sekali. Nilai apa yang keluar?',o:['1','2','3','Stack kosong'],a:2,w:'LIFO: yang terakhir masuk (3) keluar pertama.'},
       {q:'Antrean dokumen ke printer paling cocok memakai...',o:['Stack','Queue','Set','Pohon biner'],a:1,w:'Dokumen dicetak sesuai urutan kedatangan: FIFO.'}]},

{n:15, lvl:'Lanjutan', t:'Membuat Kelas Koleksi', en:'Implementing a Collection Class', py:'Kelas koleksi buatan sendiri', viz:'arrayintlist',
 vizT:'Isi ArrayIntList dan perbesar kapasitasnya', vizD:'Tambah elemen sampai penuh dan lihat array internal diperbesar.',
 body:[
  'Di bab ini kamu membangun versi sederhana ArrayList bernama <code>ArrayIntList</code>. Di dalamnya ada sebuah array biasa (<code>elementData</code>) dan penghitung <code>size</code>. Pengguna kelas hanya melihat method <code>add</code>, <code>get</code>, <code>size</code>, dan seterusnya.',
  'Perbedaan <b>size</b> dan <b>kapasitas</b> adalah kunci. Kapasitas adalah panjang array internal. Size adalah berapa slot yang benar-benar terisi. Saat size sama dengan kapasitas, kelas membuat array baru dua kali lebih besar lalu menyalin isinya. Karena pembesaran jarang terjadi, rata-rata <code>add</code> tetap cepat.',
  'Kelas yang baik memeriksa <b>precondition</b>, yaitu syarat yang harus dipenuhi pemanggil. Misalnya indeks untuk <code>get</code> harus di antara 0 dan size - 1. Bila dilanggar, lempar exception dengan pesan yang jelas, jangan diam-diam mengembalikan nilai sampah.'
 ],
 points:['Field selalu <code>private</code>. Pengguna tidak boleh mengubah <code>size</code> langsung.','Slot di atas size berisi sisa data yang tidak dianggap ada.','Dokumentasikan precondition dan postcondition setiap method.','Python: method khusus <code>__len__</code> dan <code>__getitem__</code> membuat objekmu bisa dipakai seperti list.'],
 tip:'Setelah menulis tiap method, tulis tes kecil untuk kondisi kosong, satu elemen, dan penuh. Di tiga kondisi itulah bug koleksi biasanya bersembunyi.',
 java:`import java.util.Arrays;

public class ArrayIntList {
    private int[] elementData;   // array internal
    private int size;            // jumlah slot terpakai

    public ArrayIntList() {
        elementData = new int[4];
        size = 0;
    }

    public void add(int nilai) {
        if (size == elementData.length) {         // penuh?
            elementData = Arrays.copyOf(elementData, size * 2);
        }
        elementData[size] = nilai;
        size++;
    }

    public int get(int i) {
        if (i < 0 || i >= size) {                 // precondition
            throw new IndexOutOfBoundsException("indeks: " + i);
        }
        return elementData[i];
    }

    public int size() {
        return size;
    }
}`,
 python:`class ArrayIntList:
    def __init__(self):
        self._data = [0] * 4     # "array" internal
        self._size = 0           # jumlah slot terpakai

    def add(self, nilai):
        if self._size == len(self._data):          # penuh?
            self._data = self._data + [0] * len(self._data)
        self._data[self._size] = nilai
        self._size += 1

    def get(self, i):
        if i < 0 or i >= self._size:               # precondition
            raise IndexError(f"indeks: {i}")
        return self._data[i]

    def __len__(self):
        return self._size`,
 out:null,
 cmp:[['Lempar error','<code>throw new IllegalArgumentException(...)</code>','<code>raise ValueError(...)</code>'],['Ukuran objek','method <code>size()</code>','<code>__len__</code> agar bisa <code>len(obj)</code>'],['Perbesar array','<code>Arrays.copyOf(a, n)</code>','gabung list atau list bawaan']],
 terms:['kapasitas','precondition','exception','enkapsulasi','adt'],
 quiz:[{q:'Kapasitas 4 dan sudah berisi 4 elemen. Setelah <code>add</code> sekali lagi, kapasitasnya menjadi...',o:['5','8','4','Error'],a:1,w:'Array internal digandakan dari 4 menjadi 8.'},
       {q:'Mengapa size dan kapasitas dipisah?',o:['Supaya add tidak perlu membuat array baru setiap kali','Itu bug','Supaya selalu hemat memori','Diwajibkan Java'],a:0,w:'Slot cadangan membuat sebagian besar add cukup mengisi slot kosong.'}]},

{n:16, lvl:'Lanjutan', t:'Linked List', en:'Linked Lists', py:'Linked list', viz:'linkedlist',
 vizT:'Node yang saling menunjuk', vizD:'Tambah dan hapus node. Perhatikan referensi mana yang berubah.',
 body:[
  '<b>Linked list</b> menyimpan data dalam <b>node</b> terpisah. Setiap node berisi data dan referensi <code>next</code> ke node berikutnya. Node terakhir menunjuk <code>null</code> (Python: <code>None</code>). Kelas list hanya perlu mengingat <code>front</code>, yaitu node pertama.',
  'Menambah di depan sangat murah: buat node baru yang <code>next</code>-nya menunjuk <code>front</code> lama, lalu pindahkan <code>front</code>. Tidak ada yang bergeser. Sebaliknya, mengakses elemen ke-i harus berjalan dari depan sebanyak i langkah.',
  'Kunci menulis kode linked list adalah urutan mengubah referensi. Gambar kotak dan panah di kertas sebelum menulis kode. Pola umumnya: variabel <code>current</code> berjalan maju sampai berhenti tepat <i>sebelum</i> posisi yang ingin diubah.'
 ],
 points:['Selalu tangani kasus list kosong (<code>front == null</code>) secara terpisah.','<code>current.next.next</code> berbahaya bila <code>current.next</code> null.','Linked list cepat di ujung depan, array cepat untuk akses indeks.','<code>java.util.LinkedList</code> sudah tersedia untuk pemakaian nyata.'],
 tip:'Bila kode linked list error NullPointerException, cek setiap titik pada <code>a.b.c</code>: siapa yang mungkin null?',
 java:`class ListNode {
    int data;
    ListNode next;
    ListNode(int data, ListNode next) {
        this.data = data;
        this.next = next;
    }
}

public class LinkedIntList {
    private ListNode front;   // null bila kosong

    public void addFirst(int nilai) {
        front = new ListNode(nilai, front);
    }

    public void addLast(int nilai) {
        if (front == null) {
            front = new ListNode(nilai, null);
        } else {
            ListNode cur = front;
            while (cur.next != null) {   // jalan ke node terakhir
                cur = cur.next;
            }
            cur.next = new ListNode(nilai, null);
        }
    }
}`,
 python:`class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedIntList:
    def __init__(self):
        self.front = None        # None bila kosong

    def add_first(self, nilai):
        self.front = ListNode(nilai, self.front)

    def add_last(self, nilai):
        if self.front is None:
            self.front = ListNode(nilai)
        else:
            cur = self.front
            while cur.next is not None:   # jalan ke node terakhir
                cur = cur.next
            cur.next = ListNode(nilai)`,
 out:null,
 cmp:[['Referensi kosong','<code>null</code>','<code>None</code>'],['Cek kosong','<code>front == null</code>','<code>self.front is None</code>'],['Bawaan','<code>java.util.LinkedList</code>','<code>collections.deque</code> (mirip)']],
 terms:['linked-list','node','null','referensi','traversal'],
 quiz:[{q:'Berapa biaya mengakses elemen ke-i pada linked list?',o:['O(1)','O(i), harus berjalan dari depan','O(log n)','Tidak bisa'],a:1,w:'Tidak ada indeks. Harus mengikuti next sebanyak i kali.'},
       {q:'Berapa biaya addFirst pada linked list?',o:['O(1)','O(n)','O(n²)','O(log n)'],a:0,w:'Hanya membuat satu node dan mengubah front, berapa pun panjang list.'}]},

{n:17, lvl:'Lanjutan', t:'Pohon Biner', en:'Binary Trees', py:'Pohon biner', viz:'bst',
 vizT:'Binary search tree', vizD:'Sisipkan angka, lalu jalankan traversal pre-order, in-order, dan post-order.',
 body:[
  '<b>Pohon biner</b> adalah struktur bercabang. Setiap node punya paling banyak dua anak: kiri dan kanan. Node paling atas disebut <b>akar</b> (root), node tanpa anak disebut <b>daun</b> (leaf). Karena setiap anak juga merupakan pohon, hampir semua kode pohon ditulis secara rekursif.',
  '<b>Binary search tree</b> (BST) menambahkan aturan: semua nilai di kiri lebih kecil dari node, semua nilai di kanan lebih besar. Mencari nilai cukup menelusuri satu jalur dari akar, sehingga pada pohon seimbang hanya butuh O(log n) langkah.',
  'Ada tiga urutan <b>traversal</b> klasik. Pre-order: akar, kiri, kanan. In-order: kiri, akar, kanan. Post-order: kiri, kanan, akar. Pada BST, in-order selalu menghasilkan data terurut.'
 ],
 points:['Base case kode pohon hampir selalu <code>node == null</code>.','Pola <code>root = add(root, v)</code> membuat penyisipan rekursif menjadi rapi.','Memasukkan data yang sudah terurut ke BST membuatnya miring seperti linked list.','<code>TreeSet</code> dan <code>TreeMap</code> di Java memakai pohon seimbang.'],
 tip:'Untuk fungsi pohon apa pun, tanyakan: apa jawabannya untuk pohon kosong? Bagaimana menggabungkan jawaban subpohon kiri dan kanan?',
 java:`class IntTreeNode {
    int data;
    IntTreeNode left, right;
    IntTreeNode(int data) { this.data = data; }
}

public class BST {
    private IntTreeNode root;

    public void add(int v) {
        root = add(root, v);
    }

    private IntTreeNode add(IntTreeNode node, int v) {
        if (node == null) {
            return new IntTreeNode(v);       // tempat kosong ditemukan
        }
        if (v < node.data) {
            node.left = add(node.left, v);
        } else {
            node.right = add(node.right, v);
        }
        return node;
    }

    private void inOrder(IntTreeNode node) {  // kiri, akar, kanan
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.data + " ");
            inOrder(node.right);
        }
    }
}`,
 python:`class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, v):
        self.root = self._add(self.root, v)

    def _add(self, node, v):
        if node is None:
            return TreeNode(v)               # tempat kosong ditemukan
        if v < node.data:
            node.left = self._add(node.left, v)
        else:
            node.right = self._add(node.right, v)
        return node

    def _in_order(self, node):              # kiri, akar, kanan
        if node is not None:
            self._in_order(node.left)
            print(node.data, end=" ")
            self._in_order(node.right)`,
 out:null,
 cmp:[['Method pembantu privat','<code>private</code> + overload','Awalan <code>_</code>'],['Pohon terurut bawaan','<code>TreeSet</code>, <code>TreeMap</code>','Tidak ada bawaan'],['Logika rekursif','Sama persis','Sama persis']],
 terms:['binary-tree','akar-daun','bst','traversal','rekursi'],
 quiz:[{q:'Traversal in-order pada BST menghasilkan data yang...',o:['Acak','Terurut naik','Terurut turun','Hanya berisi daun'],a:1,w:'Kiri (lebih kecil), akar, lalu kanan (lebih besar), di setiap tingkat.'},
       {q:'Mencari nilai di BST seimbang berisi n node butuh sekitar...',o:['O(n)','O(log n)','O(1)','O(n²)'],a:1,w:'Setiap perbandingan membuang separuh pohon, mirip binary search.'}]},

{n:18, lvl:'Lanjutan', t:'Struktur Data Lanjutan', en:'Advanced Data Structures', py:'Hashing dan heap', viz:'hashheap',
 vizT:'Hash table dan min-heap', vizD:'Masukkan angka ke tabel hash (dengan collision) dan ke heap.',
 body:[
  '<b>Hashing</b> adalah rahasia kecepatan HashMap dan dict. Sebuah fungsi hash mengubah kunci menjadi angka, lalu angka itu dipetakan ke indeks array yang disebut ember (bucket). Mencari kunci cukup menghitung hash-nya dan langsung melompat ke ember yang tepat, rata-rata O(1).',
  'Dua kunci berbeda bisa jatuh di ember yang sama. Ini disebut <b>collision</b>. Salah satu solusinya adalah <i>separate chaining</i>: setiap ember menyimpan daftar kecil. Agar daftar tetap pendek, tabel diperbesar ketika load factor (jumlah data dibagi jumlah ember) terlalu tinggi.',
  '<b>Priority queue</b> selalu mengeluarkan elemen dengan prioritas tertinggi, misalnya angka terkecil. Implementasinya memakai <b>heap</b>: pohon biner lengkap yang disimpan dalam array, dengan aturan setiap induk lebih kecil dari anaknya. Menambah dan mengambil elemen sama-sama O(log n).'
 ],
 points:['Di Java, objek yang dijadikan kunci harus meng-override <code>equals</code> dan <code>hashCode</code> secara konsisten.','Kunci dict Python harus immutable, misalnya string, angka, atau tuple.','Pada heap berbasis array, anak dari indeks i ada di 2i+1 dan 2i+2.','Heap dipakai di algoritma Dijkstra, penjadwalan, dan heap sort.'],
 tip:'Kapan pakai apa? Butuh cari cepat berdasarkan kunci, pakai hash. Butuh selalu ambil yang terkecil atau terbesar, pakai heap.',
 java:`import java.util.*;

public class Lanjutan {
    public static void main(String[] args) {
        // HashMap memakai hashCode() untuk memilih ember
        Map<String, Integer> umur = new HashMap<>();
        umur.put("Ani", 20);
        System.out.println(umur.get("Ani"));     // rata-rata O(1)

        // PriorityQueue = min-heap: terkecil keluar duluan
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(42);
        pq.add(7);
        pq.add(19);
        while (!pq.isEmpty()) {
            System.out.print(pq.remove() + " ");
        }
    }
}`,
 python:`import heapq

umur = {}                  # dict = hash table
umur["Ani"] = 20
print(umur["Ani"])         # rata-rata O(1)

pq = []
for x in [42, 7, 19]:
    heapq.heappush(pq, x)            # min-heap
while pq:
    print(heapq.heappop(pq), end=" ")`,
 out:`20
7 19 42`,
 cmp:[['Hash table','<code>HashMap</code>, <code>HashSet</code>','<code>dict</code>, <code>set</code>'],['Priority queue','<code>PriorityQueue</code>','modul <code>heapq</code> (min-heap)'],['Fungsi hash','<code>obj.hashCode()</code>','<code>hash(obj)</code>']],
 terms:['hashing','hash-table','collision','priority-queue','heap'],
 quiz:[{q:'Apa yang dimaksud collision pada hash table?',o:['Dua kunci berbeda masuk ember yang sama','Program crash','Kunci hilang','Heap penuh'],a:0,w:'Collision wajar terjadi. Yang penting cara menanganinya, misalnya chaining.'},
       {q:'Pada min-heap, elemen apa yang ada di akar?',o:['Terbesar','Terkecil','Terakhir dimasukkan','Acak'],a:1,w:'Aturan heap menjamin induk lebih kecil dari anaknya, jadi akar adalah minimum.'}]},

{n:19, lvl:'Lanjutan', t:'Pemrograman Fungsional', en:'Functional Programming', py:'Pemrograman fungsional', viz:'functional',
 vizT:'Pipeline filter, map, reduce', vizD:'Susun pipeline sendiri dan lihat kode Java Stream serta Python yang setara.',
 body:[
  'Pemrograman fungsional memandang program sebagai rangkaian fungsi yang mengubah data, bukan sebagai urutan perintah yang mengubah variabel. Fungsi bisa dikirim sebagai argumen, disimpan di variabel, dan dikembalikan dari fungsi lain. Fungsi seperti itu disebut <b>higher-order function</b>.',
  '<b>Lambda</b> adalah fungsi tanpa nama yang ditulis ringkas: <code>n -&gt; n * 2</code> di Java, <code>lambda n: n * 2</code> di Python. Tiga operasi utamanya: <b>filter</b> menyaring elemen, <b>map</b> mengubah setiap elemen, <b>reduce</b> menggabungkan semuanya menjadi satu nilai.',
  'Java 8 menghadirkan <b>Stream</b> untuk menulis pipeline ini secara berantai. Python punya <code>map</code>, <code>filter</code>, <code>functools.reduce</code>, dan yang paling populer, list comprehension. Gaya ini mendorong <b>fungsi murni</b> dan data <b>immutable</b>, sehingga kode lebih mudah diuji dan aman dijalankan paralel.'
 ],
 points:['Stream Java tidak mengubah list asal.','Method reference: <code>String::toUpperCase</code> sama dengan <code>s -&gt; s.toUpperCase()</code>.','Python lebih menyukai comprehension daripada map/filter dengan lambda.','Hindari efek samping (mencetak, mengubah variabel luar) di dalam lambda.'],
 tip:'Baca pipeline dari atas ke bawah seperti resep: "ambil yang genap, kuadratkan, jumlahkan". Jika kalimatnya jelas, kodenya pun jelas.',
 java:`import java.util.*;
import java.util.stream.*;

public class Fungsional {
    public static void main(String[] args) {
        List<Integer> angka = List.of(1, 2, 3, 4, 5, 6);

        int hasil = angka.stream()
                .filter(n -> n % 2 == 0)     // 2, 4, 6
                .map(n -> n * n)             // 4, 16, 36
                .reduce(0, Integer::sum);    // 56
        System.out.println(hasil);

        List<String> nama = List.of("budi", "ani", "sari");
        System.out.println(nama.stream()
                .map(String::toUpperCase)
                .collect(Collectors.toList()));
    }
}`,
 python:`from functools import reduce

angka = [1, 2, 3, 4, 5, 6]

genap = filter(lambda n: n % 2 == 0, angka)      # 2, 4, 6
kuadrat = map(lambda n: n * n, genap)            # 4, 16, 36
hasil = reduce(lambda a, b: a + b, kuadrat, 0)   # 56
print(hasil)

# gaya Pythonic: comprehension
print(sum(n * n for n in angka if n % 2 == 0))
print([s.upper() for s in ["budi", "ani", "sari"]])`,
 out:{java:`56
[BUDI, ANI, SARI]`, python:`56
56
['BUDI', 'ANI', 'SARI']`},
 cmp:[['Lambda','<code>n -&gt; n * 2</code>','<code>lambda n: n * 2</code>'],['Pipeline','<code>stream().filter(...).map(...)</code>','<code>filter</code>/<code>map</code> atau comprehension'],['Reduce','<code>.reduce(0, Integer::sum)</code>','<code>reduce(f, data, 0)</code> atau <code>sum()</code>']],
 terms:['fungsional','higher-order','lambda','map-filter-reduce','stream','pure-function','side-effect','immutable'],
 quiz:[{q:'Apa hasil map "x * 10" pada [1, 2, 3]?',o:['[10, 20, 30]','60','[1, 2, 3]','[11, 12, 13]'],a:0,w:'map mengubah setiap elemen dan menghasilkan koleksi baru dengan panjang yang sama.'},
       {q:'Fungsi murni (pure function) adalah fungsi yang...',o:['Tidak punya parameter','Hasilnya hanya bergantung pada input dan tanpa efek samping','Namanya pendek','Selalu rekursif'],a:1,w:'Input sama selalu memberi output sama, dan tidak mengubah apa pun di luar dirinya.'}]}
];



/* ===================== TOPIK PER BAB =====================
   tr   : kalimat manusia -> potongan kode [kalimat, java, python]
   ex   : latihan menerjemahkan (opsi berpasangan [java, python])
   java/python : kode dengan penanda «kunci|teks» untuk anatomi
   legend : kunci -> [id glosarium, penjelasan]
   trace  : langkah eksekusi {j,p: baris; s/sj/sp: isi memori; d/dj/dp: hapus; o/oj/op: keluaran; n/nj/np: catatan; only:'j'|'p'}
   rumus  : {f: rumus, i: poin} */
const TOPICS = {
1:[
{t:'Struktur program & statement',
 tr:[['Tampilkan tulisan "Halo" di layar','System.out.println("Halo");','print("Halo")'],['Lalu tampilkan "Dunia" di baris berikutnya','System.out.println("Dunia");','print("Dunia")'],['(Java saja) Semua perintah harus di dalam kelas dan method main','public class Halo { public static void main(String[] args) { ... } }','(tidak perlu)']],
 ex:{q:'Tampilkan tulisan Selamat pagi',o:[['System.out.println("Selamat pagi");','print("Selamat pagi")'],['System.out.println(Selamat pagi);','print(Selamat pagi)'],['println "Selamat pagi"','echo "Selamat pagi"']],a:0,w:'Teks harus diapit tanda kutip agar dianggap string, bukan nama variabel.'},
 java:`«kelas|public class Halo» {
    «main|public static void main(String[] args)» {
        System.out.println(«lit|"Halo"»);
        «stmt|System.out.println("Dunia");»
    }
}`,
 python:`«fn|print»(«lit|"Halo"»)
«stmt|print("Dunia")»`,
 legend:{kelas:['kelas','Wadah wajib setiap program Java. Nama file harus sama: Halo.java.'],main:['method','Method main adalah titik awal. Program Java selalu mulai dari sini.'],fn:['method','print adalah fungsi bawaan Python untuk mencetak.'],lit:['literal','Teks yang ditulis langsung di kode, diapit tanda kutip.'],stmt:['statement','Satu instruksi lengkap. Java mengakhirinya dengan titik koma.']},
 trace:[
  {j:2,only:'j',n:'JVM mencari method main lalu masuk ke dalamnya.'},
  {j:3,p:1,o:'Halo\n',nj:'Statement pertama mencetak Halo lalu pindah baris.',np:'Python langsung menjalankan baris pertama: mencetak Halo lalu pindah baris.'},
  {j:4,p:2,o:'Dunia\n',n:'Statement berikutnya dijalankan, tepat di bawahnya.'},
  {j:5,only:'j',n:'Tidak ada statement lagi. Program selesai.'}],
 rumus:{f:'program = statement₁ → statement₂ → … (atas ke bawah)',i:['Komputer tidak melompat sendiri. Urutan baris adalah urutan eksekusi, kecuali ada percabangan, perulangan, atau pemanggilan method.','Java: kelas → main → statement. Python: langsung statement.','println / print selalu menambah pindah baris di akhir. Java print (tanpa ln) tidak.']}},
{t:'Method statis (memecah program)',
 tr:[['Buat langkah bernama "sapa" yang menampilkan Hai!','public static void sapa() { System.out.println("Hai!"); }','def sapa():\n    print("Hai!")'],['Jalankan langkah sapa','sapa();','sapa()'],['Jalankan sekali lagi','sapa();','sapa()']],
 ex:{q:'Jalankan method bernama garis',o:[['garis();','garis()'],['void garis();','def garis()'],['garis;','garis']],a:0,w:'Memanggil method cukup menulis namanya diikuti kurung. void dan def hanya dipakai saat mendefinisikan.'},
 java:`«main|public static void main(String[] args)» {
    «call|sapa();»
    sapa();
}
«def|public static void sapa()» {
    «body|System.out.println("Hai!");»
}`,
 python:`«def|def sapa():»
    «body|print("Hai!")»

«call|sapa()»
sapa()`,
 legend:{main:['method','Titik awal program Java.'],def:['method','Definisi: nama dan isi. Hanya resep, belum dijalankan.'],call:['dekomposisi','Pemanggilan: menjalankan isi method lalu kembali ke sini.'],body:['blok','Badan method, dijalankan setiap kali dipanggil.']},
 trace:[
  {j:1,only:'j',n:'Program mulai dari main.'},
  {p:1,only:'p',n:'Python membaca definisi sapa dan mengingatnya. Isinya belum dijalankan.'},
  {j:2,p:4,n:'Pemanggilan pertama: lompat ke definisi sapa.'},
  {j:6,p:2,o:'Hai!\n',n:'Badan sapa dijalankan.'},
  {j:3,p:5,n:'Selesai, kembali ke baris setelah pemanggilan. Di sini sapa dipanggil lagi.'},
  {j:6,p:2,o:'Hai!\n',n:'Badan sapa dijalankan untuk kedua kalinya.'},
  {j:4,p:5,n:'Kembali dan program selesai. Satu definisi, dua kali pakai.'}],
 rumus:{f:'definisi = resep · pemanggilan = memasak resep',i:['Definisi tidak berjalan sendiri. Hanya pemanggilan yang menjalankannya.','Setiap pemanggilan: lompat ke definisi → jalankan badan → kembali ke baris setelah pemanggilan.','Jika satu tugas ditulis dua kali, jadikan method.']}}
],
2:[
{t:'Variabel',
 tr:[['Siapkan kotak bernama umur untuk bilangan bulat','int umur;','(Python membuat kotak saat diisi)'],['Isi kotak umur dengan 17','umur = 17;','umur = 17'],['Tambah umur satu tahun','umur = umur + 1;','umur = umur + 1'],['Tampilkan isi umur','System.out.println(umur);','print(umur)']],
 ex:{q:'Simpan harga 15000 ke dalam variabel harga (bilangan bulat)',o:[['int harga = 15000;','harga = 15000'],['harga int = 15000;','int harga = 15000'],['15000 = harga;','15000 = harga']],a:0,w:'Pola Java: tipe nama = nilai. Python cukup nama = nilai. Nama selalu di kiri tanda =.'},
 java:`«tipe|int» «nama|umur»;
umur «assign|=» «nilai|17»;
double tinggi = 165.5;
umur = «expr|umur + 1»;
System.out.println(umur);`,
 python:`# Python tidak bisa deklarasi tanpa nilai
«nama|umur» «assign|=» «nilai|17»
tinggi = 165.5
umur = «expr|umur + 1»
print(umur)`,
 legend:{tipe:['tipe-data','Jenis isi kotak. Java wajib menulisnya; Python menebak dari nilainya.'],nama:['variabel','Nama kotak. Dipakai untuk membaca atau mengganti isinya.'],assign:['assignment','Artinya "simpan ke", bukan "sama dengan".'],nilai:['literal','Nilai yang dimasukkan ke kotak.'],expr:['ekspresi','Dihitung dulu, hasilnya baru disimpan.']},
 trace:[
  {j:1,only:'j',s:{umur:['int','?']},n:'Deklarasi. Komputer menyiapkan kotak bernama umur yang hanya boleh berisi int. Isinya belum ada.'},
  {j:2,p:2,s:{umur:['int',17]},nj:'Assignment. Nilai 17 dimasukkan ke kotak umur.',np:'Python membuat kotak umur sekaligus mengisinya dengan 17. Tipenya ditebak: int.'},
  {j:3,p:3,s:{tinggi:['double|float',165.5]},n:'Kotak tinggi dibuat dan diisi bilangan pecahan.'},
  {j:4,p:4,s:{umur:['int',18]},n:'Kanan dulu: umur + 1 = 17 + 1 = 18. Lalu 18 disimpan ke kotak umur. Nilai 17 tertimpa.'},
  {j:5,p:5,o:'18\n',n:'Isi kotak umur dibaca lalu dicetak.'}],
 rumus:{f:'tipe nama = nilai;      (Python: nama = nilai)',i:['Baca assignment dari KANAN ke KIRI: hitung nilai di kanan → simpan ke kotak di kiri.','Satu kotak hanya menyimpan SATU nilai. Mengisi lagi berarti menimpa nilai lama.','x = x + 1 bukan persamaan matematika. Artinya: "nilai baru x = nilai lama x ditambah 1".','Variabel harus diisi sebelum dibaca.']}},
{t:'Ekspresi & operator',
 tr:[['Bagi 7 dengan 2, ambil hasil bulatnya','a / b   (keduanya int)','a // b'],['Ambil sisa pembagiannya','a % b','a % b'],['Bagi 7 dengan 2 sebagai pecahan','(double) a / b','a / b'],['Apakah n genap?','n % 2 == 0','n % 2 == 0']],
 ex:{q:'Ambil digit terakhir dari angka n',o:[['n % 10','n % 10'],['n / 10','n // 10'],['n - 10','n - 10']],a:0,w:'Sisa bagi 10 selalu digit terakhir: 472 % 10 = 2. Sedangkan n / 10 membuang digit terakhir.'},
 java:`int a = 7;
int b = 2;
int bagi = «intdiv|a / b»;
int sisa = «mod|a % b»;
double hasil = «cast|(double)» a / b;`,
 python:`a = 7
b = 2
bagi = «intdiv|a // b»
sisa = «mod|a % b»
hasil = «div|a / b»`,
 legend:{intdiv:['operator','Pembagian bulat: pecahan dibuang.'],mod:['modulus','Sisa bagi.'],cast:['casting','Ubah a menjadi double dulu, jadi pembagiannya pecahan.'],div:['operator','Di Python, / selalu menghasilkan pecahan.']},
 trace:[
  {j:1,p:1,s:{a:['int',7]},n:'a = 7.'},
  {j:2,p:2,s:{b:['int',2]},n:'b = 2.'},
  {j:3,p:3,s:{bagi:['int',3]},nj:'7 / 2 = 3,5, tapi int / int membuang pecahannya → 3.',np:'7 // 2 adalah pembagian bulat → 3.'},
  {j:4,p:4,s:{sisa:['int',1]},n:'7 = 2 × 3 + 1. Sisanya 1.'},
  {j:5,p:5,s:{hasil:['double|float',3.5]},nj:'(double) 7 = 7.0, lalu 7.0 / 2 = 3.5.',np:'Di Python, 7 / 2 langsung 3.5.'}],
 rumus:{f:'a = b × (a / b) + (a % b)      → 7 = 2 × 3 + 1',i:['int / int → int. Jika salah satunya double → hasilnya double.','n % 2 == 0 → genap. n % 10 → digit terakhir. n / 10 → buang digit terakhir.','Urutan: ( ) dulu, lalu * / %, lalu + −, dari kiri ke kanan.']}},
{t:'Perulangan for',
 tr:[['Ulangi untuk i dari 1 sampai 3','for (int i = 1; i <= 3; i++)','for i in range(1, 4):'],['Setiap putaran, tampilkan "Putaran i"','System.out.println("Putaran " + i);','print("Putaran", i)'],['Setelah selesai, tampilkan "Selesai"','System.out.println("Selesai");','print("Selesai")']],
 ex:{q:'Ulangi sebanyak 5 kali (mulai dari 0)',o:[['for (int i = 0; i < 5; i++)','for i in range(5):'],['for (int i = 0; i <= 5; i++)','for i in range(6):'],['for (int i = 1; i < 5; i++)','for i in range(1, 5):']],a:0,w:'0 sampai 4 berarti 5 putaran. <= 5 memberi 6 putaran, mulai dari 1 dengan < 5 hanya 4 putaran.'},
 java:`for («init|int i = 1»; «cond|i <= 3»; «upd|i++») {
    «body|System.out.println("Putaran " + i);»
}
System.out.println("Selesai");`,
 python:`for «var|i» in «range|range(1, 4)»:
    «body|print("Putaran", i)»

print("Selesai")`,
 legend:{init:['for','Inisialisasi: dijalankan sekali di awal.'],cond:['kondisional','Kondisi: dicek sebelum setiap putaran.'],upd:['increment','Update: dijalankan setelah badan loop.'],var:['variabel','Variabel loop: berisi nilai berikutnya dari range di setiap putaran.'],range:['for','Menghasilkan 1, 2, 3. Angka 4 tidak ikut.'],body:['blok','Badan loop: diulang setiap putaran.']},
 trace:()=>{const s=[{j:1,only:'j',s:{i:['int',1]},n:'Inisialisasi: i = 1. Hanya sekali.'}];
  for(let i=1;i<=3;i++){
   s.push({j:1,only:'j',n:`Cek ${i} <= 3 → true. Masuk badan loop.`});
   s.push({p:1,only:'p',s:{i:['int',i]},n:`range memberi nilai berikutnya: i = ${i}.`});
   s.push({j:2,p:2,o:`Putaran ${i}\n`,n:`Badan loop mencetak Putaran ${i}.`});
   s.push({j:1,only:'j',s:{i:['int',i+1]},n:`Update i++ → i = ${i+1}.`});}
  s.push({j:1,only:'j',n:'Cek 4 <= 3 → false. Keluar dari loop.'});
  s.push({p:1,only:'p',n:'range(1, 4) sudah habis. Keluar dari loop.'});
  s.push({j:4,only:'j',d:['i'],o:'Selesai\n',n:'Baris setelah loop. Variabel i sudah hilang karena scope-nya hanya di dalam for.'});
  s.push({p:4,only:'p',o:'Selesai\n',n:'Baris setelah loop. Di Python, i tetap ada setelah loop (nilainya 3).'});
  return s},
 rumus:{f:'putaran = akhir − awal + 1      (untuk i <= akhir)',i:['Untuk i < akhir dan range(awal, akhir): putaran = akhir − awal.','Urutan Java: init → [cek → badan → update] berulang → cek gagal → keluar.','Contoh: for (int i = 0; i < 10; i += 2) → 0, 2, 4, 6, 8 → 5 putaran.']}},
{t:'Loop bersarang (nested loop)',
 tr:[['Untuk setiap baris 1 sampai 3','for (int baris = 1; baris <= 3; baris++)','for baris in range(1, 4):'],['cetak bintang sebanyak nomor barisnya','for (int k = 1; k <= baris; k++) System.out.print("*");','for k in range(baris): print("*", end="")'],['lalu pindah ke baris baru','System.out.println();','print()']],
 ex:{q:'Untuk setiap baris (3 baris), cetak 4 bintang',o:[['for (int b = 0; b < 3; b++) { for (int k = 0; k < 4; k++) System.out.print("*"); System.out.println(); }','for b in range(3):\n    print("*" * 4)'],['for (int b = 0; b < 4; b++) System.out.print("***");','for b in range(4): print("***", end="")'],['for (int b = 0; b < 12; b++) System.out.println("*");','for b in range(12): print("*")']],a:0,w:'Loop luar mengatur baris, loop dalam mengatur isi setiap baris. Python bisa meringkas loop dalam dengan "*" * 4.'},
 java:`«outer|for (int baris = 1; baris <= 3; baris++)» {
    «inner|for (int k = 1; k <= baris; k++)» {
        System.out.print("*");
    }
    «nl|System.out.println();»
}`,
 python:`«outer|for baris in range(1, 4):»
    «inner|for k in range(baris):»
        print("*", end="")
    «nl|print()»`,
 legend:{outer:['nested-loop','Loop luar: satu putaran = satu baris.'],inner:['nested-loop','Loop dalam: jalan penuh setiap putaran luar. Batasnya bergantung pada baris.'],nl:['statement','Pindah baris setelah loop dalam selesai.']},
 trace:()=>{const s=[];for(let b=1;b<=3;b++){s.push({j:1,p:1,s:{baris:['int',b]},d:['k'],n:`Loop luar: baris = ${b}. Loop dalam akan berjalan ${b} kali.`});
  for(let k=1;k<=b;k++){s.push({j:2,p:2,sj:{k:['int',k]},sp:{k:['int',k-1]},n:`Loop dalam putaran ke-${k}.`});s.push({j:3,p:3,o:'*',n:'Cetak satu bintang tanpa pindah baris.'})}
  s.push({j:5,p:4,o:'\n',n:`Loop dalam selesai. Pindah baris. Baris ${b} berisi ${b} bintang.`})}
  s.push({j:6,only:'j',d:['baris','k'],n:'Loop luar selesai. Total 1 + 2 + 3 = 6 bintang.'});return s},
 rumus:{f:'total badan dalam = Σ putaran dalam      (1 + 2 + 3 = 6)',i:['Jika batas dalam tetap (misal m), total = n × m.','Loop luar = baris, loop dalam = kolom.','Variabel loop dalam (k) dimulai ulang setiap putaran luar.']}}
],
3:[
{t:'Parameter & return',
 tr:[['Buat rumus kuadrat yang menerima satu angka x','public static int kuadrat(int x)','def kuadrat(x):'],['dan mengembalikan x dikali x','return x * x;','return x * x'],['Hitung kuadrat dari 3 dan simpan di a','int a = kuadrat(3);','a = kuadrat(3)']],
 ex:{q:'Buat fungsi luas persegi panjang yang menerima panjang dan lebar lalu mengembalikan hasil kalinya',o:[['public static int luas(int p, int l) { return p * l; }','def luas(p, l):\n    return p * l'],['public static void luas(int p, int l) { System.out.println(p * l); }','def luas(p, l):\n    print(p * l)'],['public static int luas() { return p * l; }','def luas():\n    return p * l']],a:0,w:'"Mengembalikan" berarti return. Mencetak dengan println/print bukan mengembalikan. Panjang dan lebar harus menjadi parameter.'},
 java:`public static «rt|int» kuadrat(«param|int x») {
    «ret|return x * x;»
}
// di main:
int a = «call|kuadrat»(«arg|3»);
System.out.println(a + 1);`,
 python:`def kuadrat(«param|x»):
    «ret|return x * x»

# di main:
a = «call|kuadrat»(«arg|3»)
print(a + 1)`,
 legend:{rt:['tipe-data','Tipe nilai yang dikembalikan.'],param:['parameter','Variabel penerima nilai dari pemanggil.'],ret:['return','Kirim hasil balik dan akhiri method.'],call:['method','Memanggil method kuadrat.'],arg:['argumen','Nilai yang dikirim ke parameter.']},
 trace:[
  {j:5,p:5,n:'Bagian kanan berisi pemanggilan kuadrat(3). Program lompat ke definisi.'},
  {j:1,p:1,s:{'x · kuadrat':['int',3]},n:'Bingkai baru dibuat. Argumen 3 disalin ke parameter x.'},
  {j:2,p:2,n:'Hitung x * x = 9, lalu return 9.'},
  {j:5,p:5,d:['x · kuadrat'],s:{a:['int',9]},n:'Kembali ke pemanggil. kuadrat(3) diganti hasilnya: a = 9. Parameter x ikut hilang.'},
  {j:6,p:6,o:'10\n',n:'Cetak a + 1 = 10.'}],
 rumus:{f:'a = kuadrat(3)   →   a = 9',i:['Argumen disalin ke parameter sesuai urutan. Jumlahnya harus sama.','return mengganti teks pemanggilan dengan nilai hasil.','Parameter dan variabel lokal hilang saat method selesai (scope).','Method void / tanpa return dipakai sebagai statement, bukan di dalam ekspresi.']}},
{t:'String',
 tr:[['Simpan teks "Halo Dunia"','String s = "Halo Dunia";','s = "Halo Dunia"'],['Berapa panjangnya?','s.length()','len(s)'],['Ambil huruf pertama','s.charAt(0)','s[0]'],['Ambil 4 huruf pertama','s.substring(0, 4)','s[0:4]'],['Ubah jadi huruf besar','s.toUpperCase()','s.upper()']],
 ex:{q:'Ambil huruf terakhir dari string s',o:[['s.charAt(s.length() - 1)','s[len(s) - 1]'],['s.charAt(s.length())','s[len(s)]'],['s.charAt(-1)','s[1]']],a:0,w:'Indeks terakhir = panjang − 1. Python juga bisa menulis s[-1].'},
 java:`String s = «lit|"Halo Dunia"»;
int n = «len|s.length()»;
char c = «idx|s.charAt(0)»;
String p = «sub|s.substring(0, 4)»;
String b = «meth|s.toUpperCase()»;`,
 python:`s = «lit|"Halo Dunia"»
n = «len|len(s)»
c = «idx|s[0]»
p = «sub|s[0:4]»
b = «meth|s.upper()»`,
 legend:{lit:['string','Teks diapit tanda kutip.'],len:['string','Banyaknya karakter, termasuk spasi.'],idx:['indeks','Karakter di posisi 0 (pertama).'],sub:['string','Potongan dari indeks 0 sampai sebelum 4.'],meth:['method','Method milik objek String. Menghasilkan string baru.']},
 trace:[
  {j:1,p:1,s:{s:['String|str',{str:'Halo Dunia'}]},n:'String "Halo Dunia": 10 karakter, indeks 0 sampai 9.'},
  {j:2,p:2,s:{n:['int',10]},n:'Panjang 10. Spasi juga dihitung.'},
  {j:3,p:3,sj:{c:['char',"'H'"]},sp:{c:['str','"H"']},s:{s:['String|str',{str:'Halo Dunia',hl:[0]}]},n:'Karakter di indeks 0.'},
  {j:4,p:4,s:{p:['String|str','"Halo"'],s:['String|str',{str:'Halo Dunia',hl:[0,1,2,3]}]},n:'Ambil indeks 0, 1, 2, 3. Berhenti sebelum 4. Panjang = 4 − 0 = 4.'},
  {j:5,p:5,s:{b:['String|str','"HALO DUNIA"'],s:['String|str',{str:'Halo Dunia'}]},n:'String baru dibuat. s sendiri tidak berubah (immutable).'}],
 rumus:{f:'panjang potongan = akhir − awal      (s[a:b] → b − a karakter)',i:['Indeks karakter: 0 sampai panjang − 1.','substring(a, b) / s[a:b]: ambil dari a, BERHENTI SEBELUM b.','String tidak bisa diubah. Method seperti toUpperCase membuat string baru.','Java: "Nilai: " + 5 → "Nilai: 5". Python perlu str(5) atau f-string.']}},
{t:'Membaca input pengguna',
 tr:[['Siapkan pembaca keyboard','Scanner in = new Scanner(System.in);','(tidak perlu)'],['Tanyakan "Umur?"','System.out.print("Umur? ");','input("Umur? ")'],['Baca jawabannya sebagai bilangan bulat','int umur = in.nextInt();','umur = int(input("Umur? "))'],['Tampilkan umur dalam bulan','System.out.println(umur * 12 + " bulan");','print(umur * 12, "bulan")']],
 ex:{q:'Tanyakan berat badan (boleh pecahan) dan simpan',o:[['double berat = in.nextDouble();','berat = float(input("Berat? "))'],['int berat = in.nextLine();','berat = input("Berat? ")'],['double berat = in.next();','berat = int(input("Berat? "))']],a:0,w:'Pecahan → double / float. Di Python, tanpa float() hasilnya masih teks.'},
 java:`«sc|Scanner in = new Scanner(System.in);»
System.out.print(«prompt|"Umur? "»);
int umur = «read|in.nextInt()»;
System.out.println(umur * 12 + " bulan");`,
 python:`umur = «conv|int»(«read|input»(«prompt|"Umur? "»))
print(umur * 12, "bulan")`,
 legend:{sc:['scanner','Membuat objek Scanner yang membaca keyboard.'],prompt:['string','Teks pertanyaan untuk pengguna.'],read:['scanner','Menunggu pengguna mengetik lalu menekan Enter.'],conv:['casting','Ubah teks "20" menjadi angka 20.']},
 trace:[
  {j:1,only:'j',s:{in:['Scanner','objek Scanner (keyboard)']},n:'Objek Scanner dibuat untuk membaca keyboard.'},
  {j:2,only:'j',o:'Umur? ',n:'Tampilkan pertanyaan tanpa pindah baris.'},
  {j:3,only:'j',o:'20\n',s:{umur:['int',20]},n:'Program berhenti menunggu. Pengguna mengetik 20 lalu Enter. nextInt() memberi 20.'},
  {j:4,only:'j',o:'240 bulan\n',n:'20 * 12 = 240.'},
  {p:1,only:'p',o:'Umur? ',n:'input() menampilkan pertanyaan lalu menunggu.'},
  {p:1,only:'p',o:'20\n',s:{umur:['int',20]},n:'Pengguna mengetik 20. input() mengembalikan teks "20", lalu int() mengubahnya menjadi angka 20.'},
  {p:2,only:'p',o:'240 bulan\n',n:'20 * 12 = 240.'}],
 rumus:{f:'Python: input() → str → int() / float()',i:['Java: pilih method sesuai tipe: nextInt(), nextDouble(), next() (satu kata), nextLine() (satu baris).','Lupa int() di Python → "20" * 12 menghasilkan teks 20 diulang 12 kali.','Selalu tampilkan pertanyaan agar pengguna tahu harus mengetik apa.']}}
],
4:[
{t:'if / else if / else',
 tr:[['Jika skor minimal 90, tampilkan A','if (skor >= 90) { System.out.println("A"); }','if skor >= 90:\n    print("A")'],['Kalau tidak, jika minimal 80, tampilkan B','else if (skor >= 80) { ... }','elif skor >= 80:'],['Selain itu, tampilkan C','else { System.out.println("C"); }','else:\n    print("C")']],
 ex:{q:'Jika suhu di atas 30, tampilkan "Panas", selain itu tampilkan "Sejuk"',o:[['if (suhu > 30) { System.out.println("Panas"); } else { System.out.println("Sejuk"); }','if suhu > 30:\n    print("Panas")\nelse:\n    print("Sejuk")'],['if (suhu >= 30) { System.out.println("Panas"); } System.out.println("Sejuk");','if suhu >= 30:\n    print("Panas")\nprint("Sejuk")'],['if (suhu > 30) System.out.println("Sejuk"); else System.out.println("Panas");','if suhu > 30:\n    print("Sejuk")\nelse:\n    print("Panas")']],a:0,w:'"Di atas 30" berarti > 30. "Selain itu" adalah else. Opsi kedua selalu mencetak Sejuk karena di luar if.'},
 java:`int skor = 85;
«kw|if» («cond|skor >= 90») {
    System.out.println("A");
} «kw2|else if» (skor >= 80) {
    System.out.println("B");
} «kw3|else» {
    System.out.println("C");
}`,
 python:`skor = 85
«kw|if» «cond|skor >= 90»:
    print("A")
«kw2|elif» skor >= 80:
    print("B")
«kw3|else»:
    print("C")`,
 legend:{kw:['kondisional','Cabang pertama.'],cond:['operator-relasional','Kondisi bernilai true atau false.'],kw2:['kondisional','Dicek hanya jika semua kondisi di atasnya false.'],kw3:['kondisional','Dijalankan jika tidak ada kondisi yang true.']},
 trace:[
  {j:1,p:1,s:{skor:['int',85]},n:'skor = 85.'},
  {j:2,p:2,n:'85 >= 90? false. Blok A dilewati.'},
  {j:4,p:4,n:'85 >= 80? true. Masuk blok B.'},
  {j:5,p:5,o:'B\n',n:'Cetak B. Cabang else tidak akan dicek lagi.'},
  {j:8,only:'j',n:'Keluar dari rantai if. Hanya satu cabang yang berjalan.'}],
 rumus:{f:'cek dari atas → yang PERTAMA true menang → sisanya dilewati',i:['Urutkan kondisi dari yang paling ketat (≥ 90) ke yang paling longgar (≥ 70).','Tepat satu cabang dari rantai if / else if / else yang dijalankan.','Beberapa if terpisah (tanpa else) bisa menjalankan lebih dari satu blok.','Kata "jika … selain itu" → if … else. "jika … kalau tidak jika" → else if / elif.']}},
{t:'Algoritma kumulatif',
 tr:[['Mulai dengan total nol','int total = 0;','total = 0'],['Untuk setiap angka 1 sampai 4','for (int i = 1; i <= 4; i++)','for i in range(1, 5):'],['tambahkan angka itu ke total','total = total + i;','total = total + i'],['Tampilkan total','System.out.println(total);','print(total)']],
 ex:{q:'Hitung hasil kali 1 × 2 × 3 × 4 × 5',o:[['int hasil = 1; for (int i = 1; i <= 5; i++) hasil *= i;','hasil = 1\nfor i in range(1, 6):\n    hasil *= i'],['int hasil = 0; for (int i = 1; i <= 5; i++) hasil *= i;','hasil = 0\nfor i in range(1, 6):\n    hasil *= i'],['for (int i = 1; i <= 5; i++) { int hasil = 1; hasil *= i; }','for i in range(1, 6):\n    hasil = 1\n    hasil *= i']],a:0,w:'Penampung perkalian mulai dari 1 (0 membuat semuanya 0) dan harus dibuat di luar loop.'},
 java:`«acc|int total = 0;»
for (int i = 1; i <= 4; i++) {
    «upd|total = total + i;»
}
System.out.println(total);`,
 python:`«acc|total = 0»
for i in range(1, 5):
    «upd|total = total + i»
print(total)`,
 legend:{acc:['algoritma-kumulatif','Penampung dimulai dari nilai netral, DI LUAR loop.'],upd:['algoritma-kumulatif','Setiap putaran menambahkan satu bagian.']},
 trace:()=>{const s=[{j:1,p:1,s:{total:['int',0]},n:'Penampung disiapkan di luar loop dengan nilai netral 0.'}];let t=0;
  for(let i=1;i<=4;i++){s.push({j:2,p:2,s:{i:['int',i]},n:`Putaran i = ${i}.`});t+=i;s.push({j:3,p:3,s:{total:['int',t]},n:`total = ${t-i} + ${i} = ${t}.`})}
  s.push({j:5,p:4,o:'10\n',dj:['i'],n:'Loop selesai. Cetak total 10.'});return s},
 rumus:{f:'penampung = netral;   ulangi { penampung = penampung ⊕ elemen }',i:['Nilai netral: 0 untuk jumlah, 1 untuk perkalian, elemen pertama untuk maks/min, "" untuk teks.','Jika penampung dibuat di dalam loop, ia di-reset setiap putaran (bug klasik).','Cek cepat: 1 + 2 + … + n = n(n + 1) / 2 → 4 × 5 / 2 = 10.']}}
],
5:[
{t:'Perulangan while',
 tr:[['Selama n masih lebih dari 1','while (n > 1)','while n > 1:'],['bagi dua n','n = n / 2;','n = n // 2'],['dan hitung langkahnya','langkah++;','langkah += 1']],
 ex:{q:'Selama saldo kurang dari 1000, tambahkan 100 ke saldo',o:[['while (saldo < 1000) { saldo += 100; }','while saldo < 1000:\n    saldo += 100'],['if (saldo < 1000) { saldo += 100; }','if saldo < 1000:\n    saldo += 100'],['while (saldo < 1000) { saldo = 100; }','while saldo < 1000:\n    saldo = 100']],a:0,w:'"Selama" → while. if hanya sekali. saldo = 100 tidak menambah, sehingga loop tidak pernah berhenti.'},
 java:`int n = 20;
int langkah = 0;
«cond|while (n > 1)» {
    «chg|n = n / 2;»
    langkah++;
}
System.out.println(langkah);`,
 python:`n = 20
langkah = 0
«cond|while n > 1:»
    «chg|n = n // 2»
    langkah += 1
print(langkah)`,
 legend:{cond:['while','Dicek sebelum setiap putaran. False → keluar.'],chg:['perulangan-tak-hingga','Baris ini mengubah n sehingga kondisi suatu saat false. Tanpanya, loop tidak pernah berhenti.']},
 trace:()=>{const s=[{j:1,p:1,s:{n:['int',20]},n:'n = 20.'},{j:2,p:2,s:{langkah:['int',0]},n:'langkah = 0.'}];let n=20,l=0;
  while(n>1){s.push({j:3,p:3,n:`Cek ${n} > 1 → true. Masuk badan loop.`});n=Math.floor(n/2);s.push({j:4,p:4,s:{n:['int',n]},n:`n dibagi dua (bulat) → ${n}.`});l++;s.push({j:5,p:5,s:{langkah:['int',l]},n:`langkah = ${l}.`})}
  s.push({j:3,p:3,n:'Cek 1 > 1 → false. Keluar dari loop.'});s.push({j:7,p:6,o:'4\n',n:'Cetak 4.'});return s},
 rumus:{f:'while = if yang diulang',i:['Pola: siapkan variabel → cek → kerjakan & UBAH variabel → cek lagi.','Jumlah putaran tidak tertulis di kode. Ia bergantung pada data.','Kata kunci kalimat: "selama", "sampai", "ulangi hingga" → while (untuk "sampai X", tulis kondisi kebalikannya: while (!X)).']}},
{t:'Logika boolean & short-circuit',
 tr:[['x tidak nol DAN 10 dibagi x lebih dari 1','x != 0 && 10 / x > 1','x != 0 and 10 / x > 1'],['sedang libur ATAU x lebih dari 5','libur || x > 5','libur or x > 5'],['TIDAK pergi','!pergi','not pergi']],
 ex:{q:'Boleh masuk jika umur minimal 17 dan punya tiket',o:[['umur >= 17 && punyaTiket','umur >= 17 and punya_tiket'],['umur > 17 || punyaTiket','umur > 17 or punya_tiket'],['umur >= 17 & !punyaTiket','umur >= 17 and not punya_tiket']],a:0,w:'"dan" → && / and, "minimal 17" → >= 17. "atau" akan membolehkan orang tanpa tiket.'},
 java:`int x = 0;
boolean aman = «and|x != 0 && 10 / x > 1»;
boolean libur = true;
boolean pergi = «or|libur || x > 5»;
boolean tinggal = «not|!pergi»;`,
 python:`x = 0
aman = «and|x != 0 and 10 / x > 1»
libur = True
pergi = «or|libur or x > 5»
tinggal = «not|not pergi»`,
 legend:{and:['short-circuit','AND berhenti di bagian kiri jika sudah false. 10 / x tidak pernah dihitung.'],or:['logika-boolean','OR berhenti jika bagian kiri sudah true.'],not:['logika-boolean','NOT membalik true ↔ false.']},
 trace:[
  {j:1,p:1,s:{x:['int',0]},n:'x = 0.'},
  {j:2,p:2,s:{aman:['boolean|bool',false]},n:'x != 0 → false. AND pasti false, jadi 10 / x DILEWATI. Tidak ada error bagi nol.'},
  {j:3,p:3,s:{libur:['boolean|bool',true]},n:'libur = true.'},
  {j:4,p:4,s:{pergi:['boolean|bool',true]},n:'libur true → OR pasti true. x > 5 tidak dicek.'},
  {j:5,p:5,s:{tinggal:['boolean|bool',false]},n:'NOT true = false.'}],
 rumus:{f:'AND: semua true · OR: minimal satu true · NOT: dibalik',i:['Short-circuit: false && … → false tanpa melihat kanan. true || … → true tanpa melihat kanan.','Taruh pengecekan "aman" di kiri: x != 0 && 10 / x > 1.','De Morgan: !(a && b) = !a || !b, dan !(a || b) = !a && !b.','Kalimat "dan" → &&, "atau" → ||, "bukan / tidak" → !.']}},
{t:'Masalah fencepost',
 tr:[['Tampilkan angka 1 sampai 4','(tiang)','(tiang)'],['dipisah koma, tanpa koma di akhir','(kawat di antara tiang)','(kawat di antara tiang)'],['Langkah: cetak 1 dulu, lalu ulangi ", angka" untuk 2 sampai 4','System.out.print(1); for (...) System.out.print(", " + i);','print(1, end="")\nfor i in range(2, 5): print(",", i, end="")']],
 ex:{q:'Cetak isi daftar a dipisah tanda " - " tanpa pemisah berlebih',o:[['System.out.print(a[0]); for (int i = 1; i < a.length; i++) System.out.print(" - " + a[i]);','print(a[0], end="")\nfor x in a[1:]:\n    print(" -", x, end="")'],['for (int x : a) System.out.print(x + " - ");','for x in a:\n    print(x, "- ", end="")'],['for (int i = 1; i < a.length; i++) System.out.print(" - " + a[i]);','for x in a[1:]:\n    print(" -", x, end="")']],a:0,w:'Elemen pertama dicetak di luar loop, sisanya "pemisah + elemen". Opsi ketiga lupa elemen pertama.'},
 java:`«post|System.out.print(1);»
for (int i = 2; i <= 4; i++) {
    «wire|System.out.print(", " + i);»
}`,
 python:`«post|print(1, end="")»
for i in range(2, 5):
    «wire|print(",", i, end="")»`,
 legend:{post:['fencepost','Tiang pertama dicetak di luar loop.'],wire:['fencepost','Setiap putaran mencetak "kawat + tiang".']},
 trace:()=>{const s=[{j:1,p:1,o:'1',n:'Tiang pertama dicetak di luar loop.'}];for(let i=2;i<=4;i++){s.push({j:2,p:2,s:{i:['int',i]},n:`i = ${i}.`});s.push({j:3,p:3,o:', '+i,n:`Cetak kawat ", " lalu tiang ${i}.`})}
  s.push({j:4,only:'j',d:['i'],n:'Selesai: 4 angka, 3 pemisah, tanpa koma berlebih.'});return s},
 rumus:{f:'n tiang → n − 1 kawat',i:['Cetak satu elemen di luar loop, lalu loop (n − 1) kali mencetak "pemisah + elemen".','Alternatif: if (i > 1) cetak pemisah, di dalam loop.','Output berakhir dengan koma berlebih adalah tanda masalah fencepost.']}}
],
6:[
{t:'Membaca file baris demi baris',
 tr:[['Buka file nilai.txt','new Scanner(new File("nilai.txt"))','open("nilai.txt")'],['Selama masih ada baris, ambil satu baris','while (f.hasNextLine()) { ... f.nextLine() ... }','for baris in f:'],['Pecah baris menjadi kata-kata','new Scanner(baris) / baris.split(" ")','baris.split()'],['Jumlahkan dua angka setelah nama','t.nextInt() + t.nextInt()','int(t[1]) + int(t[2])']],
 ex:{q:'Untuk setiap baris di file data.txt, tampilkan barisnya',o:[['Scanner f = new Scanner(new File("data.txt")); while (f.hasNextLine()) System.out.println(f.nextLine());','with open("data.txt") as f:\n    for baris in f:\n        print(baris, end="")'],['Scanner f = new Scanner("data.txt"); System.out.println(f.nextLine());','print(open("data.txt"))'],['while (true) System.out.println(f.nextLine());','while True:\n    print(f.readline())']],a:0,w:'new Scanner("data.txt") membaca teks "data.txt" itu sendiri, bukan file. Perlu new File(...). Loop harus berhenti saat baris habis.'},
 java:`Scanner f = new Scanner(«file|new File("nilai.txt")»);
while («chk|f.hasNextLine()») {
    Scanner t = new Scanner(«line|f.nextLine()»);
    String nama = «tok|t.next()»;
    int total = t.nextInt() + t.nextInt();
    System.out.println(nama + " " + total);
}`,
 python:`with «file|open("nilai.txt")» as f:
    «line|for baris in f:»
        t = «tok|baris.split()»
        nama = t[0]
        total = int(t[1]) + int(t[2])
        print(nama, total)`,
 legend:{file:['file-io','Membuka file untuk dibaca.'],chk:['while','Masih ada baris? Cek sebelum membaca.'],line:['file-io','Mengambil satu baris utuh.'],tok:['token','Memecah atau mengambil token (potongan dipisah spasi).']},
 trace:()=>{const L=[['Budi',85,90],['Sari',78,92]];const s=[];
  s.push({j:1,only:'j',s:{f:['Scanner','nilai.txt (posisi awal)']},n:'File dibuka. Isinya dua baris: "Budi 85 90" dan "Sari 78 92".'});
  s.push({p:1,only:'p',s:{f:['file','nilai.txt (terbuka)']},n:'File dibuka. with menjamin file ditutup di akhir. Isinya: "Budi 85 90" dan "Sari 78 92".'});
  L.forEach(([nm,a,b],k)=>{const line=`${nm} ${a} ${b}`;
   s.push({j:2,only:'j',n:`hasNextLine() → true. Masih ada baris "${line}".`});
   s.push({j:3,only:'j',s:{t:['Scanner',`"${line}"`],f:['Scanner',`nilai.txt (setelah baris ${k+1})`]},n:'nextLine() mengambil satu baris utuh. Scanner kecil t akan memecahnya.'});
   s.push({j:4,only:'j',s:{nama:['String',`"${nm}"`]},n:'next() mengambil token pertama.'});
   s.push({j:5,only:'j',s:{total:['int',a+b]},n:`nextInt() = ${a}, nextInt() = ${b}. total = ${a+b}.`});
   s.push({j:6,only:'j',o:`${nm} ${a+b}\n`,n:'Cetak hasil baris ini.'});
   s.push({p:2,only:'p',s:{baris:['str',`"${line}"`]},n:`Baris ke-${k+1} dibaca.`});
   s.push({p:3,only:'p',s:{t:['list',[`"${nm}"`,`"${a}"`,`"${b}"`]]},n:'split() memecah baris menjadi 3 token. Semuanya masih teks.'});
   s.push({p:4,only:'p',s:{nama:['str',`"${nm}"`]},n:'Token pertama adalah nama.'});
   s.push({p:5,only:'p',s:{total:['int',a+b]},n:`int("${a}") + int("${b}") = ${a+b}.`});
   s.push({p:6,only:'p',o:`${nm} ${a+b}\n`,n:'Cetak hasil baris ini.'});});
  s.push({j:2,only:'j',n:'hasNextLine() → false. Semua baris sudah dibaca.'});
  s.push({p:2,only:'p',n:'Tidak ada baris lagi. Keluar dari with, file otomatis ditutup.'});return s},
 rumus:{f:'per baris → pecah token → ubah tipe → olah',i:['Selalu cek dulu (hasNextInt / hasNextLine) sebelum mengambil (nextInt / nextLine).','Token dari file selalu teks. "85" harus diubah ke int sebelum dijumlah.','Token = potongan yang dipisah spasi. "Budi 85 90" → 3 token.']}},
{t:'Menangani error (exception)',
 tr:[['Coba buka file x.txt','try { new Scanner(new File("x.txt")); }','try:\n    open("x.txt")'],['Kalau file tidak ada, tampilkan pesan','catch (FileNotFoundException e) { System.out.println("File tidak ada"); }','except FileNotFoundError:\n    print("File tidak ada")']],
 ex:{q:'Coba ubah teks s menjadi angka. Kalau gagal, pakai 0',o:[['int n; try { n = Integer.parseInt(s); } catch (NumberFormatException e) { n = 0; }','try:\n    n = int(s)\nexcept ValueError:\n    n = 0'],['int n = Integer.parseInt(s); if (error) n = 0;','n = int(s)\nif error:\n    n = 0'],['try { n = 0; } catch (Exception e) { n = Integer.parseInt(s); }','try:\n    n = 0\nexcept:\n    n = int(s)']],a:0,w:'Kode yang mungkin gagal masuk ke try, rencana cadangan masuk ke catch/except.'},
 java:`«try|try» {
    Scanner f = new Scanner(new File("x.txt"));
    System.out.println("Berhasil dibuka");
} «catch|catch (FileNotFoundException e)» {
    System.out.println("File tidak ada");
}`,
 python:`«try|try:»
    f = open("x.txt")
    print("Berhasil dibuka")
«catch|except FileNotFoundError:»
    print("File tidak ada")`,
 legend:{try:['exception','Coba jalankan blok ini.'],catch:['exception','Jika terjadi error jenis ini di dalam try, lompat ke sini.']},
 trace:[
  {j:1,p:1,n:'Masuk blok try.'},
  {j:2,p:2,n:'File x.txt tidak ditemukan. Exception dilempar! Sisa baris di dalam try dilewati.'},
  {j:4,p:4,n:'Jenis exception cocok dengan blok ini. Program lompat ke sini.'},
  {j:5,p:5,o:'File tidak ada\n',n:'Rencana B dijalankan. Program tidak crash.'}],
 rumus:{f:'try { coba } catch (Jenis) { rencana B }',i:['Saat exception terjadi, sisa baris di try langsung dilewati.','catch hanya menangkap jenis yang cocok.','Java memaksa menangani checked exception seperti FileNotFoundException. Python tidak memaksa.']}}
],
7:[
{t:'Membuat & mengakses array',
 tr:[['Siapkan 4 slot angka','int[] a = new int[4];','a = [0] * 4'],['Isi slot pertama dengan 5','a[0] = 5;','a[0] = 5'],['Isi slot terakhir dengan 9','a[3] = 9;','a[3] = 9'],['Tampilkan elemen terakhir','System.out.println(a[a.length - 1]);','print(a[len(a) - 1])']],
 ex:{q:'Ambil elemen ketiga dari array nilai',o:[['nilai[2]','nilai[2]'],['nilai[3]','nilai[3]'],['nilai(3)','nilai(3)']],a:0,w:'Hitungan manusia ke-3 = indeks 2, karena indeks mulai dari 0.'},
 java:`int[] a = «new|new int[4]»;
«idx|a[0]» = 5;
a[3] = 9;
int n = «len|a.length»;
System.out.println(«last|a[n - 1]»);`,
 python:`a = «new|[0] * 4»
«idx|a[0]» = 5
a[3] = 9
n = «len|len(a)»
print(«last|a[n - 1]»)`,
 legend:{new:['array','Membuat 4 slot sekaligus, semua berisi 0.'],idx:['indeks','Slot nomor 0, yaitu yang pertama.'],len:['array','Banyaknya slot.'],last:['off-by-one','Elemen terakhir ada di indeks panjang − 1.']},
 trace:[
  {j:1,p:1,s:{a:['int[]|list',{arr:[0,0,0,0]}]},n:'4 slot dibuat, semua berisi 0.'},
  {j:2,p:2,s:{a:['int[]|list',{arr:[5,0,0,0],hl:[0]}]},n:'Slot indeks 0 diisi 5.'},
  {j:3,p:3,s:{a:['int[]|list',{arr:[5,0,0,9],hl:[3]}]},n:'Slot indeks 3 (yang terakhir) diisi 9.'},
  {j:4,p:4,s:{n:['int',4]},n:'Panjang array 4.'},
  {j:5,p:5,o:'9\n',s:{a:['int[]|list',{arr:[5,0,0,9],hl:[3]}]},n:'a[n − 1] = a[3] = 9. Ingat: a[4] tidak ada.'}],
 rumus:{f:'indeks terakhir = panjang − 1',i:['Elemen ke-k (hitungan manusia) ada di a[k − 1].','Java mengisi array baru dengan nilai default: 0, 0.0, false, atau null.','Akses a[panjang] → error. Java: ArrayIndexOutOfBoundsException, Python: IndexError.']}},
{t:'Traversal: mencari maksimum',
 tr:[['Anggap elemen pertama sebagai yang terbesar','int maks = a[0];','maks = a[0]'],['Periksa setiap elemen berikutnya','for (int i = 1; i < a.length; i++)','for i in range(1, len(a)):'],['Jika lebih besar dari juara, jadikan juara baru','if (a[i] > maks) maks = a[i];','if a[i] > maks:\n    maks = a[i]']],
 ex:{q:'Hitung berapa banyak elemen array a yang negatif',o:[['int c = 0; for (int x : a) if (x < 0) c++;','c = 0\nfor x in a:\n    if x < 0:\n        c += 1'],['int c = 0; for (int x : a) c += x;','c = 0\nfor x in a:\n    c += x'],['for (int x : a) { int c = 0; if (x < 0) c++; }','for x in a:\n    c = 0\n    if x < 0:\n        c += 1']],a:0,w:'Penghitung dibuat di luar loop dan bertambah hanya bila syarat terpenuhi. Opsi kedua menjumlahkan, bukan menghitung.'},
 java:`int[] a = {3, 8, 1, 9};
int maks = a[0];
«loop|for (int i = 1; i < a.length; i++)» {
    if («cmp|a[i] > maks») {
        maks = a[i];
    }
}
System.out.println(maks);`,
 python:`a = [3, 8, 1, 9]
maks = a[0]
«loop|for i in range(1, len(a)):»
    if «cmp|a[i] > maks»:
        maks = a[i]
print(maks)`,
 legend:{loop:['traversal','Mengunjungi indeks 1 sampai terakhir.'],cmp:['operator-relasional','Bandingkan elemen sekarang dengan juara sementara.']},
 trace:()=>{const a=[3,8,1,9],T='int[]|list';const s=[{j:1,p:1,s:{a:[T,{arr:a}]},n:'Array berisi 4 elemen, indeks 0 sampai 3.'},{j:2,p:2,s:{maks:['int',3]},n:'Juara sementara = a[0] = 3.'}];let m=3;
  for(let i=1;i<4;i++){s.push({j:3,p:3,s:{i:['int',i],a:[T,{arr:a,hl:[i]}]},n:`i = ${i}, kunjungi a[${i}] = ${a[i]}.`});
   if(a[i]>m){s.push({j:4,p:4,n:`${a[i]} > ${m}? true.`});m=a[i];s.push({j:5,p:5,s:{maks:['int',m]},n:`Juara baru: maks = ${m}.`})}
   else s.push({j:4,p:4,n:`${a[i]} > ${m}? false. maks tetap.`})}
  s.push({j:8,p:6,o:'9\n',dj:['i'],s:{a:[T,{arr:a}]},n:'Traversal selesai. Cetak 9.'});return s},
 rumus:{f:'for (i = 0; i < panjang; i++) → kunjungi a[i]',i:['Juara sementara = elemen pertama, lalu tantang dengan sisanya.','Batas yang benar: i < panjang. Memakai <= berarti satu langkah kelewatan.','Pola sama untuk jumlah, hitung, dan cari. Hanya isi badan loop yang berubah.']}},
{t:'Referensi (dua nama, satu array)',
 tr:[['Buat array berisi 1, 2, 3','int[] a = {1, 2, 3};','a = [1, 2, 3]'],['Beri nama lain b untuk array yang sama','int[] b = a;','b = a'],['Ubah elemen pertama lewat b','b[0] = 99;','b[0] = 99'],['(Kalau mau salinan terpisah)','int[] b = Arrays.copyOf(a, a.length);','b = a.copy()']],
 ex:{q:'Buat salinan terpisah dari list nilai agar aslinya aman',o:[['int[] salin = Arrays.copyOf(nilai, nilai.length);','salin = nilai.copy()'],['int[] salin = nilai;','salin = nilai'],['int[] salin = new int[nilai];','salin = list[nilai]']],a:0,w:'= hanya menyalin alamat. copyOf / copy() membuat array baru.'},
 java:`int[] a = {1, 2, 3};
int[] b = «alias|a»;
«mut|b[0] = 99»;
System.out.println(a[0]);`,
 python:`a = [1, 2, 3]
b = «alias|a»
«mut|b[0] = 99»
print(a[0])`,
 legend:{alias:['referensi','Yang disalin adalah alamat array, bukan isinya.'],mut:['referensi','Mengubah array yang juga ditunjuk a.']},
 trace:[
  {j:1,p:1,s:{a:['int[]|list',{ref:'A',arr:[1,2,3]}]},n:'Array dibuat sebagai objek A di memori. Variabel a menyimpan alamatnya.'},
  {j:2,p:2,s:{b:['int[]|list',{ref:'A',arr:[1,2,3]}]},n:'b menerima alamat yang sama. Tidak ada array baru.'},
  {j:3,p:3,s:{a:['int[]|list',{ref:'A',arr:[99,2,3],hl:[0]}],b:['int[]|list',{ref:'A',arr:[99,2,3],hl:[0]}]},n:'Objek A diubah lewat b. a melihat perubahan yang sama.'},
  {j:4,p:4,o:'99\n',n:'a[0] = 99.'}],
 rumus:{f:'b = a   →   dua nama, SATU objek',i:['Variabel bertipe objek (array, list, objek) menyimpan alamat, bukan isi.','Untuk salinan sungguhan: Arrays.copyOf(a, a.length) atau a.copy().','Mengirim array ke method juga mengirim alamat. Method bisa mengubah isi array pemanggil.']}}
],
8:[
{t:'Kelas, konstruktor, objek',
 tr:[['Rancang "Akun" yang punya nama dan saldo','class Akun { String nama; int saldo; }','class Akun: (field dibuat di __init__)'],['Saat akun dibuat, isi nama dan saldo awal','Akun(String n, int s) { nama = n; saldo = s; }','def __init__(self, n, s):\n    self.nama = n\n    self.saldo = s'],['Buat akun milik Rina dengan saldo 100','Akun a = new Akun("Rina", 100);','a = Akun("Rina", 100)']],
 ex:{q:'Buat objek Buku berjudul "Laskar Pelangi" dengan 529 halaman',o:[['Buku b = new Buku("Laskar Pelangi", 529);','b = Buku("Laskar Pelangi", 529)'],['Buku b = Buku.new("Laskar Pelangi", 529);','b = new Buku("Laskar Pelangi", 529)'],['Buku("Laskar Pelangi", 529) = b;','Buku("Laskar Pelangi", 529) = b']],a:0,w:'Java memakai new, Python cukup memanggil nama kelas. Variabel tetap di sebelah kiri.'},
 java:`«cls|class Akun» {
    «field|String nama;»
    «field|int saldo;»
    «ctor|Akun(String n, int s)» {
        nama = n;
        saldo = s;
    }
}
Akun a = «new|new Akun("Rina", 100)»;`,
 python:`«cls|class Akun:»
    «ctor|def __init__(self, n, s):»
        «field|self.nama» = n
        «field|self.saldo» = s

a = «new|Akun("Rina", 100)»`,
 legend:{cls:['kelas','Cetak biru bernama Akun.'],field:['field','Data yang dimiliki setiap objek Akun.'],ctor:['konstruktor','Dijalankan otomatis saat objek dibuat.'],new:['instance','Membuat satu objek baru dari kelas Akun.']},
 trace:[
  {j:9,only:'j',s:{'objek A':['Akun',{obj:{nama:'null',saldo:0}}]},n:'new Akun(...) menyiapkan objek kosong. Field diberi nilai default.'},
  {j:4,only:'j',s:{n:['String','"Rina"'],s:['int',100]},n:'Konstruktor dipanggil. Argumen masuk ke parameter n dan s.'},
  {j:5,only:'j',s:{'objek A':['Akun',{obj:{nama:'"Rina"',saldo:0}}]},n:'Field nama diisi.'},
  {j:6,only:'j',s:{'objek A':['Akun',{obj:{nama:'"Rina"',saldo:100}}]},n:'Field saldo diisi.'},
  {j:9,only:'j',d:['n','s'],s:{a:['Akun','→ objek A']},n:'Konstruktor selesai dan parameternya hilang. a menyimpan alamat objek.'},
  {p:6,only:'p',s:{'objek A':['Akun',{obj:{}}]},n:'Akun(...) membuat objek kosong.'},
  {p:2,only:'p',s:{self:['Akun','→ objek A'],n:['str','"Rina"'],s:['int',100]},n:'__init__ dipanggil. self menunjuk objek baru, argumen masuk ke n dan s.'},
  {p:3,only:'p',s:{'objek A':['Akun',{obj:{nama:'"Rina"'}}]},n:'self.nama = n membuat field nama.'},
  {p:4,only:'p',s:{'objek A':['Akun',{obj:{nama:'"Rina"',saldo:100}}]},n:'self.saldo = s membuat field saldo.'},
  {p:6,only:'p',d:['self','n','s'],s:{a:['Akun','→ objek A']},n:'__init__ selesai. a menyimpan alamat objek.'}],
 rumus:{f:'new Kelas(args) = alokasi → konstruktor → alamat',i:['Kelas = cetak biru, objek = rumah yang dibangun darinya. Satu kelas, banyak objek.','Konstruktor mengisi field. Parameternya hilang setelah selesai, field tetap ada.','Kata benda dalam soal → kelas / field. Kata kerja → method.']}},
{t:'Method & enkapsulasi',
 tr:[['Saldo disembunyikan dari luar','private int saldo = 0;','self._saldo = 0'],['Akun bisa menerima setoran','public void setor(int x)','def setor(self, x):'],['tapi hanya jika jumlahnya positif','if (x > 0) saldo += x;','if x > 0:\n    self._saldo += x'],['Setor 50 ke akun a','a.setor(50);','a.setor(50)']],
 ex:{q:'Tambahkan method tarik(x) yang hanya mengurangi saldo jika saldo cukup',o:[['public void tarik(int x) { if (x <= saldo) saldo -= x; }','def tarik(self, x):\n    if x <= self._saldo:\n        self._saldo -= x'],['public void tarik(int x) { saldo -= x; }','def tarik(self, x):\n    self._saldo -= x'],['public void tarik(int x) { if (x > saldo) saldo -= x; }','def tarik(self, x):\n    if x > self._saldo:\n        self._saldo -= x']],a:0,w:'"Hanya jika cukup" → x <= saldo. Tanpa pengecekan, saldo bisa negatif.'},
 java:`class Akun {
    «priv|private int saldo = 0;»
    public void setor(int x) {
        «guard|if (x > 0)» saldo += x;
    }
}
Akun a = new Akun();
«call|a.setor(50)»;
a.setor(-20);`,
 python:`class Akun:
    def __init__(self):
        «priv|self._saldo» = 0
    def setor(self, x):
        «guard|if x > 0:»
            self._saldo += x

a = Akun()
«call|a.setor(50)»
a.setor(-20)`,
 legend:{priv:['enkapsulasi','Field tersembunyi. Kode luar tidak bisa menulis a.saldo = -999.'],guard:['precondition','Penjaga: hanya setoran positif yang diterima.'],call:['this-self','Di dalam setor, this/self menunjuk objek a.']},
 trace:[
  {j:7,only:'j',s:{a:['Akun',{obj:{saldo:0}}]},n:'Objek dibuat dengan saldo 0.'},
  {j:8,only:'j',n:'Panggil setor(50) pada objek a.'},
  {j:3,only:'j',s:{x:['int',50]},n:'x = 50. Di dalam method, this = objek a.'},
  {j:4,only:'j',s:{a:['Akun',{obj:{saldo:50}}]},n:'50 > 0 → true. saldo += 50.'},
  {j:9,only:'j',d:['x'],n:'Panggil setor(-20).'},
  {j:3,only:'j',s:{x:['int',-20]},n:'x = −20.'},
  {j:4,only:'j',n:'−20 > 0 → false. Saldo tidak berubah. Data tetap valid.'},
  {p:8,only:'p',s:{a:['Akun',{obj:{_saldo:0}}]},n:'Objek dibuat dengan _saldo 0.'},
  {p:9,only:'p',n:'Panggil setor(50) pada objek a.'},
  {p:4,only:'p',s:{x:['int',50]},n:'x = 50, self = objek a.'},
  {p:5,only:'p',n:'50 > 0 → true.'},
  {p:6,only:'p',s:{a:['Akun',{obj:{_saldo:50}}]},n:'_saldo bertambah 50.'},
  {p:10,only:'p',d:['x'],n:'Panggil setor(-20).'},
  {p:4,only:'p',s:{x:['int',-20]},n:'x = −20.'},
  {p:5,only:'p',n:'−20 > 0 → false. Saldo tidak berubah. Data tetap valid.'}],
 rumus:{f:'objek.method(args)   →   di dalamnya this / self = objek itu',i:['Field private + method dengan pengecekan = data selalu valid.','Accessor hanya membaca (getSaldo), mutator mengubah (setor).','Python tidak memaksa privat. Awalan _ adalah tanda sopan "jangan disentuh".']}}
],
9:[
{t:'Pewarisan & override',
 tr:[['Kucing adalah sejenis Hewan','class Kucing extends Hewan','class Kucing(Hewan):'],['Suara kucing berbeda: "Meong"','String suara() { return "Meong"; }','def suara(self): return "Meong"'],['Simpan kucing di variabel bertipe Hewan dan minta suaranya','Hewan h = new Kucing(); h.suara();','h = Kucing()\nh.suara()']],
 ex:{q:'Buat kelas Mobil yang merupakan sejenis Kendaraan',o:[['class Mobil extends Kendaraan { }','class Mobil(Kendaraan):\n    pass'],['class Kendaraan extends Mobil { }','class Kendaraan(Mobil):\n    pass'],['class Mobil implements Kendaraan()','class Mobil = Kendaraan']],a:0,w:'"A adalah sejenis B" → A extends B. Kelas anak di kiri, induk di kanan.'},
 java:`«sup|class Hewan» {
    String suara() { return "..."; }
}
class Kucing «ext|extends Hewan» {
    «ovr|String suara() { return "Meong"; }»
}
«decl|Hewan» h = new Kucing();
System.out.println(«poly|h.suara()»);`,
 python:`«sup|class Hewan:»
    def suara(self): return "..."

class Kucing«ext|(Hewan)»:
    «ovr|def suara(self): return "Meong"»

h = Kucing()
print(«poly|h.suara()»)`,
 legend:{sup:['superclass','Kelas induk.'],ext:['pewarisan','Kucing mewarisi semua isi Hewan.'],ovr:['override','Menulis ulang suara() dengan versi Kucing.'],decl:['polimorfisme','Variabel bertipe induk boleh menunjuk objek anak.'],poly:['polimorfisme','Versi yang dijalankan ditentukan objek sebenarnya.']},
 trace:[
  {j:7,p:7,s:{h:['Hewan|Kucing','→ objek Kucing']},nj:'Variabel bertipe Hewan, tetapi objeknya Kucing.',np:'h menunjuk objek Kucing.'},
  {j:8,p:8,n:'h.suara(): cari suara() mulai dari kelas objek sebenarnya, yaitu Kucing.'},
  {j:5,p:5,n:'Ketemu di Kucing. Versi milik Hewan tidak dipakai.'},
  {j:8,p:8,o:'Meong\n',n:'Cetak Meong.'}],
 rumus:{f:'cari method: kelas objek → induknya → … → yang pertama ketemu dipakai',i:['Tipe VARIABEL menentukan method apa yang BOLEH dipanggil (dicek compiler Java).','Tipe OBJEK menentukan versi MANA yang dijalankan.','Kalimat "X adalah sejenis Y" → X extends Y. Kalimat "X punya Y" → Y menjadi field di X.']}},
{t:'Interface',
 tr:[['Setiap Bentuk harus bisa menghitung luas','interface Bentuk { double luas(); }','(Python: cukup sepakat punya method luas)'],['Persegi adalah Bentuk','class Persegi implements Bentuk','class Persegi:'],['Luas persegi = sisi × sisi','public double luas() { return s * s; }','def luas(self):\n    return self.s * self.s']],
 ex:{q:'Kelas Lingkaran harus memenuhi kontrak Bentuk',o:[['class Lingkaran implements Bentuk { public double luas() { return 3.14 * r * r; } }','class Lingkaran:\n    def luas(self):\n        return 3.14 * self.r ** 2'],['class Lingkaran extends Bentuk { }','class Lingkaran(Bentuk):\n    pass'],['interface Lingkaran implements Bentuk','class Lingkaran = Bentuk']],a:0,w:'implements = berjanji. Janji ditepati dengan menulis isi luas().'},
 java:`«iface|interface Bentuk» {
    «abs|double luas();»
}
class Persegi «impl|implements Bentuk» {
    double s = 3;
    «ful|public double luas() { return s * s; }»
}
«decl|Bentuk» b = new Persegi();
System.out.println(b.luas());`,
 python:`class Persegi:
    def __init__(self):
        self.s = 3
    «duck|def luas(self):»
        return self.s * self.s

b = Persegi()
print(b.luas())`,
 legend:{iface:['interface','Kontrak: daftar method tanpa isi.'],abs:['interface','Janji: setiap Bentuk punya luas().'],impl:['interface','Persegi berjanji menepati kontrak Bentuk.'],ful:['override','Isi nyata dari janji luas().'],decl:['polimorfisme','Variabel bertipe interface.'],duck:['duck-typing','Python tidak butuh interface: cukup punya method luas().']},
 trace:[
  {j:8,only:'j',s:{b:['Bentuk','→ objek Persegi (s = 3)']},n:'Variabel bertipe interface Bentuk menunjuk objek Persegi.'},
  {j:9,only:'j',n:'b.luas() → versi milik Persegi.'},
  {j:6,only:'j',n:'return 3 * 3 = 9.0'},
  {j:9,only:'j',o:'9.0\n',n:'Cetak 9.0 (double).'},
  {p:7,only:'p',s:{b:['Persegi','→ objek Persegi (s = 3)']},n:'Objek Persegi dibuat.'},
  {p:8,only:'p',n:'b.luas() dipanggil. Python tidak peduli interface, yang penting method-nya ada.'},
  {p:5,only:'p',n:'return 3 * 3 = 9.'},
  {p:8,only:'p',o:'9\n',n:'Cetak 9.'}],
 rumus:{f:'interface = daftar janji · implements = menepati semua janji',i:['Satu kelas Java boleh implements banyak interface.','Kode yang menerima Bentuk bisa bekerja dengan Persegi, Lingkaran, dan bentuk baru di masa depan.','Python memakai duck typing: "punya method-nya? berarti boleh".']}}
],
10:[
{t:'add, sisip, hapus',
 tr:[['Buat daftar teks kosong','ArrayList<String> L = new ArrayList<>();','L = []'],['Tambah "a" di akhir','L.add("a");','L.append("a")'],['Sisipkan "b" di posisi 1','L.add(1, "b");','L.insert(1, "b")'],['Hapus elemen pertama','L.remove(0);','L.pop(0)'],['Berapa isinya sekarang?','L.size()','len(L)']],
 ex:{q:'Sisipkan "Budi" di urutan paling depan daftar nama',o:[['nama.add(0, "Budi");','nama.insert(0, "Budi")'],['nama.add("Budi");','nama.append("Budi")'],['nama.set(0, "Budi");','nama[0] = "Budi"']],a:0,w:'add(0, x) / insert(0, x) menyisip dan menggeser. set / = menimpa elemen pertama.'},
 java:`ArrayList«gen|<String>» L = new ArrayList<>();
«add|L.add("a")»;
L.add("c");
«ins|L.add(1, "b")»;
«rem|L.remove(0)»;
System.out.println(«size|L.size()»);`,
 python:`L = []
«add|L.append("a")»
L.append("c")
«ins|L.insert(1, "b")»
«rem|L.pop(0)»
print(«size|len(L)»)`,
 legend:{gen:['generics','Isi list hanya boleh String.'],add:['arraylist','Tambah di akhir. Tidak ada yang bergeser.'],ins:['arraylist','Sisip di indeks 1. Elemen mulai indeks 1 bergeser ke kanan.'],rem:['arraylist','Hapus indeks 0. Sisanya bergeser ke kiri.'],size:['arraylist','Jumlah elemen saat ini.']},
 trace:[
  {j:1,p:1,s:{L:['ArrayList<String>|list',{arr:[]}]},n:'List kosong.'},
  {j:2,p:2,s:{L:['ArrayList<String>|list',{arr:['"a"'],hl:[0]}]},n:'"a" masuk di akhir.'},
  {j:3,p:3,s:{L:['ArrayList<String>|list',{arr:['"a"','"c"'],hl:[1]}]},n:'"c" masuk di akhir.'},
  {j:4,p:4,s:{L:['ArrayList<String>|list',{arr:['"a"','"b"','"c"'],hl:[1]}]},n:'"b" disisip di indeks 1. "c" bergeser dari indeks 1 ke 2.'},
  {j:5,p:5,s:{L:['ArrayList<String>|list',{arr:['"b"','"c"']}]},n:'Indeks 0 dihapus. "b" dan "c" bergeser ke kiri.'},
  {j:6,p:6,o:'2\n',n:'Ukuran sekarang 2.'}],
 rumus:{f:'biaya add(i, x) / remove(i) ≈ size − i elemen bergeser',i:['add(x) di akhir murah. Sisip atau hapus di depan paling mahal.','Setelah remove(i), elemen yang tadinya di i + 1 sekarang di i.','"tambahkan" → add / append. "sisipkan di posisi" → add(i, x) / insert. "ganti" → set / L[i] = x.']}},
{t:'Menghapus sambil berjalan mundur',
 tr:[['Periksa setiap elemen dari belakang ke depan','for (int i = L.size() - 1; i >= 0; i--)','for i in range(len(L) - 1, -1, -1):'],['jika genap','if (L.get(i) % 2 == 0)','if L[i] % 2 == 0:'],['hapus','L.remove(i);','L.pop(i)']],
 ex:{q:'Hapus semua nama yang kosong ("") dari list nama',o:[['for (int i = nama.size() - 1; i >= 0; i--) if (nama.get(i).isEmpty()) nama.remove(i);','for i in range(len(nama) - 1, -1, -1):\n    if nama[i] == "":\n        nama.pop(i)'],['for (int i = 0; i < nama.size(); i++) if (nama.get(i).isEmpty()) nama.remove(i);','for i in range(len(nama)):\n    if nama[i] == "":\n        nama.pop(i)'],['nama.remove("");','nama.remove("")']],a:0,w:'Berjalan maju sambil menghapus bisa melewatkan elemen (dan di Python bisa IndexError). remove("") hanya menghapus satu.'},
 java:`ArrayList<Integer> L = new ArrayList<>(List.of(2, 4, 5, 6));
for («back|int i = L.size() - 1; i >= 0; i--») {
    if (L.get(i) % 2 == 0) {
        «rm|L.remove(i)»;
    }
}`,
 python:`L = [2, 4, 5, 6]
for i in «back|range(len(L) - 1, -1, -1)»:
    if L[i] % 2 == 0:
        «rm|L.pop(i)»`,
 legend:{back:['traversal','Berjalan mundur dari indeks terakhir ke 0.'],rm:['arraylist','Menghapus tidak mengganggu indeks yang belum dikunjungi.']},
 trace:()=>{let L=[2,4,5,6];const T='ArrayList<Integer>|list';const s=[{j:1,p:1,s:{L:[T,{arr:[...L]}]},n:'Tugas: hapus semua angka genap.'}];
  for(let i=L.length-1;i>=0;i--){s.push({j:2,p:2,s:{i:['int',i],L:[T,{arr:[...L],hl:[i]}]},n:`i = ${i}, periksa ${L[i]}.`});
   if(L[i]%2===0){s.push({j:3,p:3,n:`${L[i]} genap → hapus.`});L.splice(i,1);s.push({j:4,p:4,s:{L:[T,{arr:[...L]}]},n:`Dihapus. Yang bergeser hanya elemen setelah indeks ${i}, yang sudah diperiksa.`})}
   else s.push({j:3,p:3,n:`${L[i]} ganjil → biarkan.`})}
  s.push({j:6,only:'j',d:['i'],n:'Selesai: [5]. Tidak ada yang terlewat.'});return s},
 rumus:{f:'hapus saat MAJU → ada yang terlewat · hapus saat MUNDUR → aman',i:['Maju: setelah remove(i), elemen berikutnya pindah ke i, lalu i++ melompatinya.','Mundur: yang bergeser hanya elemen yang sudah dikunjungi.','Alternatif modern: L.removeIf(x -> x % 2 == 0) atau [x for x in L if x % 2 != 0].']}}
],
11:[
{t:'Set: himpunan tanpa duplikat',
 tr:[['Siapkan himpunan buah','Set<String> s = new TreeSet<>();','s = set()'],['Masukkan apel, jeruk, lalu apel lagi','s.add("apel"); s.add("jeruk"); s.add("apel");','s.add("apel")\ns.add("jeruk")\ns.add("apel")'],['Ada berapa buah berbeda?','s.size()','len(s)']],
 ex:{q:'Apakah "mangga" ada di himpunan buah?',o:[['buah.contains("mangga")','"mangga" in buah'],['buah.get("mangga")','buah["mangga"]'],['buah.indexOf("mangga")','buah.index("mangga")']],a:0,w:'Pertanyaan "apakah ada" → contains / in. Set tidak punya indeks.'},
 java:`Set<String> s = new «impl|TreeSet<>()»;
s.add("apel");
s.add("jeruk");
«dup|s.add("apel")»;
System.out.println(s.size());`,
 python:`s = «impl|set()»
s.add("apel")
s.add("jeruk")
«dup|s.add("apel")»
print(len(s))`,
 legend:{impl:['set','Membuat himpunan kosong.'],dup:['set','Menambah nilai yang sudah ada: diabaikan.']},
 trace:[
  {j:1,p:1,s:{s:['Set<String>|set',{set:[]}]},n:'Himpunan kosong.'},
  {j:2,p:2,s:{s:['Set<String>|set',{set:['"apel"']}]},n:'apel masuk.'},
  {j:3,p:3,s:{s:['Set<String>|set',{set:['"apel"','"jeruk"']}]},n:'jeruk masuk.'},
  {j:4,p:4,n:'apel sudah ada. Set mengabaikannya, tidak ada error.'},
  {j:5,p:5,o:'2\n',n:'Ukuran 2: hanya nilai yang berbeda.'}],
 rumus:{f:'ukuran set = banyaknya nilai BERBEDA',i:['Pertanyaan khas set: "apakah X ada?" → contains / in, sangat cepat.','Ubah list menjadi set untuk membuang duplikat: new HashSet<>(list) / set(lst).','HashSet urutannya acak, TreeSet selalu terurut.']}},
{t:'Map: menghitung kemunculan',
 tr:[['Siapkan catatan kata → jumlah','Map<String, Integer> m = new TreeMap<>();','m = {}'],['Untuk setiap kata','for (String k : teks.split(" "))','for k in teks.split():'],['jumlahnya = jumlah lama (atau 0) + 1','m.put(k, m.getOrDefault(k, 0) + 1);','m[k] = m.get(k, 0) + 1']],
 ex:{q:'Ambil nomor telepon milik "Ani" dari map telepon',o:[['telepon.get("Ani")','telepon["Ani"]'],['telepon.get(0)','telepon[0]'],['telepon.contains("Ani")','"Ani" in telepon']],a:0,w:'Map diakses lewat kunci, bukan indeks. contains / in hanya menjawab ya/tidak.'},
 java:`Map«kv|<String, Integer>» m = new TreeMap<>();
for (String k : "a b a".split(" ")) {
    m.put(k, «gd|m.getOrDefault(k, 0)» + 1);
}
System.out.println(m);`,
 python:`«kv|m = {}»
for k in "a b a".split():
    m[k] = «gd|m.get(k, 0)» + 1
print(m)`,
 legend:{kv:['map','Peta dari kunci (kata) ke nilai (jumlah).'],gd:['map','Ambil nilai lama, atau 0 jika kunci belum ada.']},
 trace:()=>{const m={};const T='Map<String,Integer>|dict';const s=[{j:1,p:1,s:{m:[T,{map:{}}]},n:'Map kosong.'}];
  for(const k of ['a','b','a']){s.push({j:2,p:2,s:{k:['String|str',`"${k}"`]},n:`Kata berikutnya: "${k}".`});const old=m[k]||0;m[k]=old+1;s.push({j:3,p:3,s:{m:[T,{map:{...m},hl:k}]},n:old?`"${k}" sudah ada (nilai ${old}). Simpan ${old} + 1 = ${m[k]}.`:`"${k}" belum ada → nilai default 0. Simpan 0 + 1 = 1.`})}
  s.push({j:5,p:4,oj:'{a=2, b=1}\n',op:"{'a': 2, 'b': 1}\n",dj:['k'],n:'Cetak isi map.'});return s},
 rumus:{f:'m[k] = (nilai lama atau 0) + 1',i:['Kunci unik. put dengan kunci yang sudah ada menimpa nilainya.','Ambil semua kunci: keySet() / keys(). Pasangan: entrySet() / items().','Kalimat "berapa kali …" atau "… untuk setiap …" hampir selalu dijawab dengan map.']}}
],
12:[
{t:'Base case & recursive case',
 tr:[['Faktorial n adalah 1 jika n paling besar 1','if (n <= 1) return 1;','if n <= 1: return 1'],['selain itu, n dikali faktorial (n − 1)','return n * fakt(n - 1);','return n * fakt(n - 1)']],
 ex:{q:'Jumlah 1 + 2 + … + n secara rekursif',o:[['int jml(int n) { if (n == 0) return 0; return n + jml(n - 1); }','def jml(n):\n    if n == 0: return 0\n    return n + jml(n - 1)'],['int jml(int n) { return n + jml(n - 1); }','def jml(n):\n    return n + jml(n - 1)'],['int jml(int n) { if (n == 0) return 0; return n + jml(n); }','def jml(n):\n    if n == 0: return 0\n    return n + jml(n)']],a:0,w:'Butuh base case (n == 0) dan pemanggilan yang mengecil (n − 1). Opsi lain tidak pernah berhenti.'},
 java:`int fakt(int n) {
    «base|if (n <= 1) return 1;»
    «rec|return n * fakt(n - 1);»
}
// dipanggil: fakt(3)`,
 python:`def fakt(n):
    «base|if n <= 1: return 1»
    «rec|return n * fakt(n - 1)»

# dipanggil: fakt(3)`,
 legend:{base:['base-case','Kasus paling kecil, dijawab langsung.'],rec:['recursive-case','Memanggil diri sendiri dengan n yang lebih kecil.']},
 trace:()=>{const nm=k=>`n · fakt(${k})`;const s=[{j:5,p:5,n:'Program memanggil fakt(3).'}];
  for(const k of [3,2,1]){s.push({j:1,p:1,s:{[nm(k)]:['int',k]},n:`Bingkai baru untuk fakt(${k}) dengan n = ${k}. Bingkai lama tetap ada di bawahnya.`});
   if(k>1){s.push({j:2,p:2,n:`${k} <= 1? false. Bukan base case.`});s.push({j:3,p:3,n:`Perlu ${k} * fakt(${k-1}). Bingkai ini MENUNGGU, lalu fakt(${k-1}) dipanggil.`})}
   else s.push({j:2,p:2,n:'1 <= 1 → true. Base case: langsung return 1.'})}
  s.push({j:3,p:3,d:[nm(1)],n:'Bingkai fakt(1) dibuang. Kembali ke fakt(2): 2 * 1 = 2, return 2.'});
  s.push({j:3,p:3,d:[nm(2)],n:'Bingkai fakt(2) dibuang. Kembali ke fakt(3): 3 * 2 = 6, return 6.'});
  s.push({j:5,p:5,d:[nm(3)],s:{hasil:['int',6]},n:'fakt(3) mengembalikan 6. Stack kosong lagi.'});return s},
 rumus:{f:'f(n) = jawaban untuk n − 1 + satu langkah kecil',i:['Cek dua hal: (1) ada base case? (2) setiap panggilan mendekati base case?','Kedalaman rekursi = banyaknya bingkai yang menumpuk.','Ubah kalimat definisi menjadi kode: "faktorial n adalah n kali faktorial n−1, dan faktorial 1 adalah 1".']}},
{t:'Rekursi pada angka',
 tr:[['Jumlah digit dari angka satu digit adalah angka itu sendiri','if (n < 10) return n;','if n < 10: return n'],['selain itu: digit terakhir + jumlah digit sisanya','return n % 10 + jumlahDigit(n / 10);','return n % 10 + jumlah_digit(n // 10)']],
 ex:{q:'Hitung banyaknya digit angka n secara rekursif',o:[['int dig(int n) { if (n < 10) return 1; return 1 + dig(n / 10); }','def dig(n):\n    if n < 10: return 1\n    return 1 + dig(n // 10)'],['int dig(int n) { if (n < 10) return n; return n % 10 + dig(n / 10); }','def dig(n):\n    if n < 10: return n\n    return n % 10 + dig(n // 10)'],['int dig(int n) { return 1 + dig(n / 10); }','def dig(n):\n    return 1 + dig(n // 10)']],a:0,w:'Setiap langkah membuang satu digit dan menambah hitungan 1. Opsi kedua menjumlahkan digit, bukan menghitungnya.'},
 java:`int jumlahDigit(int n) {
    «base|if (n < 10) return n;»
    return «last|n % 10» + jumlahDigit(«rest|n / 10»);
}
// dipanggil: jumlahDigit(472)`,
 python:`def jumlah_digit(n):
    «base|if n < 10: return n»
    return «last|n % 10» + jumlah_digit(«rest|n // 10»)

# dipanggil: jumlah_digit(472)`,
 legend:{base:['base-case','Angka satu digit: jawabannya angka itu sendiri.'],last:['modulus','Digit terakhir.'],rest:['recursive-case','Angka tanpa digit terakhir, lebih kecil, mendekati base case.']},
 trace:()=>{const nm=k=>`n · jd(${k})`;const s=[{j:5,p:5,n:'Panggil jumlahDigit(472).'}];
  for(const k of [472,47]){s.push({j:1,p:1,s:{[nm(k)]:['int',k]},n:`Bingkai baru: n = ${k}.`});s.push({j:2,p:2,n:`${k} < 10? false.`});s.push({j:3,p:3,n:`Digit terakhir ${k%10}, sisanya ${Math.floor(k/10)}. Hitung ${k%10} + jumlahDigit(${Math.floor(k/10)}) dan tunggu hasilnya.`})}
  s.push({j:1,p:1,s:{[nm(4)]:['int',4]},n:'Bingkai baru: n = 4.'});s.push({j:2,p:2,n:'4 < 10 → true. Base case: return 4.'});
  s.push({j:3,p:3,d:[nm(4)],n:'Kembali ke n = 47: 7 + 4 = 11.'});s.push({j:3,p:3,d:[nm(47)],n:'Kembali ke n = 472: 2 + 11 = 13.'});
  s.push({j:5,p:5,d:[nm(472)],s:{hasil:['int',13]},n:'Hasil akhir 13 (2 + 7 + 4).'});return s},
 rumus:{f:'n % 10 = digit terakhir · n / 10 = sisanya',i:['472 → 2 + jumlahDigit(47) → 2 + (7 + jumlahDigit(4)) → 2 + 7 + 4 = 13.','Banyak soal rekursi angka memakai pasangan % 10 dan / 10.','Kedalaman rekursi = banyaknya digit.']}}
],
13:[
{t:'Binary search',
 tr:[['Selama rentang pencarian belum kosong','while (kiri <= kanan)','while kiri <= kanan:'],['lihat elemen di tengah','int t = (kiri + kanan) / 2;','t = (kiri + kanan) // 2'],['jika itu targetnya, selesai','if (a[t] == x) return t;','if a[t] == x: return t'],['jika terlalu kecil, cari di kanan; kalau terlalu besar, cari di kiri','kiri = t + 1;  /  kanan = t - 1;','kiri = t + 1  /  kanan = t - 1']],
 ex:{q:'Elemen tengah lebih BESAR dari target. Apa langkah berikutnya?',o:[['kanan = t - 1;','kanan = t - 1'],['kiri = t + 1;','kiri = t + 1'],['t = t + 1;','t = t + 1']],a:0,w:'Target lebih kecil dari tengah, jadi pasti ada di separuh kiri. Geser batas kanan.'},
 java:`int kiri = 0, kanan = a.length - 1;
«loop|while (kiri <= kanan)» {
    «mid|int t = (kiri + kanan) / 2;»
    if (a[t] == x) return t;
    else if (a[t] < x) «cut|kiri = t + 1»;
    else kanan = t - 1;
}
return -1;`,
 python:`kiri, kanan = 0, len(a) - 1
«loop|while kiri <= kanan:»
    «mid|t = (kiri + kanan) // 2»
    if a[t] == x: return t
    elif a[t] < x: «cut|kiri = t + 1»
    else: kanan = t - 1
return -1`,
 legend:{loop:['binary-search','Selama rentang pencarian belum kosong.'],mid:['binary-search','Ambil posisi tengah rentang.'],cut:['big-o','Buang separuh kiri sekaligus.']},
 trace:()=>{const A=[2,5,8,12,16,23,38,45,56],x=45,T='int[]|list';const s=[{j:1,p:1,s:{x:['int',x],a:[T,{arr:A,lo:0,hi:8}],kiri:['int',0],kanan:['int',8]},n:`Cari ${x} di 9 data terurut. Rentang awal: seluruh array.`}];let L=0,R=8;
  while(L<=R){const t=Math.floor((L+R)/2);s.push({j:2,p:2,n:`${L} <= ${R} → masih ada rentang.`});s.push({j:3,p:3,s:{t:['int',t],a:[T,{arr:A,lo:L,hi:R,hl:[t]}]},n:`Tengah = (${L} + ${R}) / 2 = ${t}. a[${t}] = ${A[t]}.`});
   if(A[t]===x){s.push({j:4,p:4,s:{hasil:['int',t]},n:`a[${t}] == ${x}. Ketemu! return ${t}.`});break}
   if(A[t]<x){L=t+1;s.push({j:5,p:5,s:{kiri:['int',L],a:[T,{arr:A,lo:L,hi:R}]},n:`${A[t]} < ${x}. Buang separuh kiri: kiri = ${L}.`})}
   else{R=t-1;s.push({j:6,p:6,s:{kanan:['int',R],a:[T,{arr:A,lo:L,hi:R}]},n:`${A[t]} > ${x}. Buang separuh kanan: kanan = ${R}.`})}}
  return s},
 rumus:{f:'langkah maksimum ≈ ⌊log₂ n⌋ + 1',i:['9 data → 4 langkah, 1.000 → 10, 1.000.000 → 20.','Syarat mutlak: data sudah terurut.','Tidak ketemu → kiri melewati kanan → return −1.']}},
{t:'Selection sort',
 tr:[['Untuk setiap posisi i dari depan','for (int i = 0; i < a.length - 1; i++)','for i in range(len(a) - 1):'],['cari elemen terkecil dari i sampai akhir','int m = i; for (j = i + 1 ...) if (a[j] < a[m]) m = j;','m = i\nfor j in range(i + 1, len(a)):\n    if a[j] < a[m]: m = j'],['tukar elemen terkecil itu ke posisi i','tmp = a[i]; a[i] = a[m]; a[m] = tmp;','a[i], a[m] = a[m], a[i]']],
 ex:{q:'Tukar isi variabel x dan y',o:[['int tmp = x; x = y; y = tmp;','x, y = y, x'],['x = y; y = x;','x = y\ny = x'],['x == y;','x == y']],a:0,w:'Tanpa variabel bantu, nilai x hilang setelah x = y. Python bisa menukar sekaligus.'},
 java:`for (int i = 0; i < a.length - 1; i++) {
    int m = i;
    for (int j = i + 1; j < a.length; j++) {
        if («cmp|a[j] < a[m]») m = j;
    }
    «swap|int tmp = a[i]; a[i] = a[m]; a[m] = tmp;»
}`,
 python:`for i in range(len(a) - 1):
    m = i
    for j in range(i + 1, len(a)):
        if «cmp|a[j] < a[m]»: m = j
    «swap|a[i], a[m] = a[m], a[i]»`,
 legend:{cmp:['selection-sort','Bandingkan dengan minimum sementara.'],swap:['selection-sort','Tukar minimum ke posisi i.']},
 trace:()=>{const a=[5,2,4,1],T='int[]|list';const s=[{j:1,p:1,s:{a:[T,{arr:[...a]}]},n:'Data awal [5, 2, 4, 1].'}];let c=0;
  for(let i=0;i<a.length-1;i++){s.push({j:1,p:1,s:{i:['int',i],a:[T,{arr:[...a],done:i}]},n:`Putaran i = ${i}: cari minimum dari indeks ${i} sampai 3.`});let m=i;s.push({j:2,p:2,s:{m:['int',m]},n:`Minimum sementara: a[${m}] = ${a[m]}.`});
   for(let j=i+1;j<a.length;j++){c++;s.push({j:3,p:3,s:{j:['int',j],a:[T,{arr:[...a],hl:[j,m],done:i}]},n:`Bandingkan a[${j}] = ${a[j]} dengan a[${m}] = ${a[m]}.`});
    if(a[j]<a[m]){m=j;s.push({j:4,p:4,s:{m:['int',m]},n:`${a[j]} lebih kecil → m = ${j}.`})}else s.push({j:4,p:4,n:'Tidak lebih kecil. m tetap.'})}
   [a[i],a[m]]=[a[m],a[i]];s.push({j:6,p:5,s:{a:[T,{arr:[...a],hl:[i],done:i+1}]},n:`Tukar a[${i}] dengan a[${m}]. Indeks 0..${i} sudah final.`})}
  s.push({j:7,only:'j',d:['i','j','m'],s:{a:[T,{arr:[...a],done:4}]},n:`Selesai dengan ${c} perbandingan = 4 × 3 / 2.`});return s},
 rumus:{f:'perbandingan = n(n − 1) / 2',i:['Putaran ke-i: cari minimum dari i sampai akhir, tukar ke posisi i.','Setelah putaran i, bagian 0..i sudah final.','4 data → 6 perbandingan, 100 data → 4.950. Pertumbuhannya O(n²).']}},
{t:'Menghitung Big-O',
 tr:[['Untuk setiap i dari 0 sampai n − 1','for (int i = 0; i < n; i++)','for i in range(n):'],['dan untuk setiap j dari 0 sampai n − 1','for (int j = 0; j < n; j++)','for j in range(n):'],['kerjakan satu langkah','hitung++;','hitung += 1']],
 ex:{q:'Berapa Big-O kode: for (i = 0; i < n; i++) cetak(i); lalu for (j = 0; j < n; j++) cetak(j); (dua loop berurutan, tidak bersarang)',o:[['O(n)','O(n)'],['O(n²)','O(n²)'],['O(log n)','O(log n)']],a:0,w:'Berurutan dijumlah: n + n = 2n → O(n). Hanya loop bersarang yang dikalikan.'},
 java:`int hitung = 0;
«outer|for (int i = 0; i < n; i++)» {
    «inner|for (int j = 0; j < n; j++)» {
        «work|hitung++;»
    }
}`,
 python:`hitung = 0
«outer|for i in range(n):»
    «inner|for j in range(n):»
        «work|hitung += 1»`,
 legend:{outer:['big-o','Berjalan n kali.'],inner:['big-o','Berjalan n kali UNTUK SETIAP putaran luar.'],work:['big-o','Dijalankan n × n kali → O(n²).']},
 trace:()=>{const s=[{j:1,p:1,s:{n:['int',3],hitung:['int',0]},n:'n = 3. Hitung berapa kali baris terdalam dijalankan.'}];let h=0;
  for(let i=0;i<3;i++){s.push({j:2,p:2,s:{i:['int',i]},n:`Loop luar i = ${i}.`});for(let j=0;j<3;j++){s.push({j:3,p:3,s:{j:['int',j]},n:`Loop dalam j = ${j}.`});h++;s.push({j:4,p:4,s:{hitung:['int',h]},n:h===9?'hitung = 9 = 3 × 3 = n². Untuk n = 1.000, satu juta kali.':`hitung = ${h}.`})}}
  return s},
 rumus:{f:'satu loop → O(n) · loop bersarang → O(n²) · bagi dua → O(log n)',i:['Abaikan konstanta dan suku kecil: 3n² + 5n + 2 → O(n²).','n = 3 → 9 kali. n = 1.000 → 1.000.000 kali.','Loop berurutan (bukan bersarang) dijumlah: O(n) + O(n) = O(n).']}}
],
14:[
{t:'Stack (LIFO)',
 tr:[['Siapkan tumpukan','Stack<Integer> s = new Stack<>();','s = []'],['Taruh 1, 2, 3 di atasnya','s.push(1); s.push(2); s.push(3);','s.append(1); s.append(2); s.append(3)'],['Ambil yang paling atas','s.pop()','s.pop()'],['Lihat yang paling atas tanpa mengambil','s.peek()','s[-1]']],
 ex:{q:'Batalkan aksi terakhir (undo) dari tumpukan riwayat',o:[['riwayat.pop()','riwayat.pop()'],['riwayat.remove(0)','riwayat.pop(0)'],['riwayat.push()','riwayat.append()']],a:0,w:'Aksi terakhir ada di atas stack. pop mengambilnya.'},
 java:`Stack<Integer> s = new Stack<>();
«push|s.push(1)»;
s.push(2);
s.push(3);
int x = «pop|s.pop()»;
int y = «peek|s.peek()»;`,
 python:`s = []
«push|s.append(1)»
s.append(2)
s.append(3)
x = «pop|s.pop()»
y = «peek|s[-1]»`,
 legend:{push:['stack','Taruh di atas.'],pop:['stack','Ambil dan buang yang paling atas.'],peek:['stack','Lihat yang paling atas tanpa mengambil.']},
 trace:[
  {j:1,p:1,s:{s:['Stack<Integer>|list',{stack:[]}]},n:'Stack kosong.'},
  {j:2,p:2,s:{s:['Stack<Integer>|list',{stack:[1]}]},n:'push 1.'},
  {j:3,p:3,s:{s:['Stack<Integer>|list',{stack:[1,2]}]},n:'push 2. Sekarang 2 di atas.'},
  {j:4,p:4,s:{s:['Stack<Integer>|list',{stack:[1,2,3]}]},n:'push 3. Sekarang 3 paling atas.'},
  {j:5,p:5,s:{s:['Stack<Integer>|list',{stack:[1,2]}],x:['int',3]},n:'pop mengambil yang paling atas: 3.'},
  {j:6,p:6,s:{y:['int',2]},n:'peek hanya melihat yang paling atas (2). Isinya tidak berubah.'}],
 rumus:{f:'LIFO: urutan keluar = KEBALIKAN urutan masuk',i:['push 1, 2, 3 → pop menghasilkan 3, 2, 1.','Kalimat "yang terakhir", "batalkan", "kembali" → stack.','pop pada stack kosong → error. Cek isEmpty() / not s dulu.']}},
{t:'Queue (FIFO)',
 tr:[['Siapkan antrean','Queue<String> q = new LinkedList<>();','q = deque()'],['Ani, Budi, Cici datang berurutan','q.add("Ani"); q.add("Budi"); q.add("Cici");','q.append("Ani") ...'],['Layani yang paling depan','q.remove()','q.popleft()'],['Siapa berikutnya?','q.peek()','q[0]']],
 ex:{q:'Pelanggan baru datang dan ikut antrean',o:[['antre.add(pelanggan);','antre.append(pelanggan)'],['antre.push(pelanggan);','antre.appendleft(pelanggan)'],['antre.remove(pelanggan);','antre.popleft()']],a:0,w:'Yang baru datang masuk di belakang antrean.'},
 java:`Queue<String> q = new LinkedList<>();
«add|q.add("Ani")»;
q.add("Budi");
q.add("Cici");
String d = «rem|q.remove()»;
String e = «peek|q.peek()»;`,
 python:`from collections import deque
q = deque()
«add|q.append("Ani")»
q.append("Budi")
q.append("Cici")
d = «rem|q.popleft()»
e = «peek|q[0]»`,
 legend:{add:['queue','Masuk di belakang antrean.'],rem:['queue','Keluar dari depan: yang paling lama menunggu.'],peek:['queue','Lihat siapa di depan tanpa mengeluarkan.']},
 trace:[
  {j:1,p:2,s:{q:['Queue<String>|deque',{queue:[]}]},n:'Antrean kosong.'},
  {j:2,p:3,s:{q:['Queue<String>|deque',{queue:['"Ani"']}]},n:'Ani datang.'},
  {j:3,p:4,s:{q:['Queue<String>|deque',{queue:['"Ani"','"Budi"']}]},n:'Budi di belakang Ani.'},
  {j:4,p:5,s:{q:['Queue<String>|deque',{queue:['"Ani"','"Budi"','"Cici"']}]},n:'Cici di paling belakang.'},
  {j:5,p:6,s:{q:['Queue<String>|deque',{queue:['"Budi"','"Cici"']}],d:['String|str','"Ani"']},n:'Yang keluar Ani, yang datang pertama.'},
  {j:6,p:7,s:{e:['String|str','"Budi"']},n:'Sekarang Budi di depan.'}],
 rumus:{f:'FIFO: urutan keluar = SAMA dengan urutan masuk',i:['Masuk di belakang, keluar dari depan.','Kalimat "antrean", "sesuai urutan datang", "giliran" → queue.','Python: pakai deque.popleft(), bukan list.pop(0) yang lambat.']}}
],
15:[
{t:'Menambah elemen & memperbesar kapasitas',
 tr:[['Jika array sudah penuh','if (size == data.length)','if size == len(data):'],['buat array baru dua kali lebih besar dan salin isinya','data = Arrays.copyOf(data, size * 2);','data = data + [0] * len(data)'],['taruh nilai di slot kosong berikutnya','data[size] = nilai;','data[size] = nilai'],['dan catat bahwa isinya bertambah','size++;','size += 1']],
 ex:{q:'Kosongkan list tanpa membuat array baru',o:[['size = 0;','self._size = 0'],['data = null;','self._data = None'],['data[0] = 0;','self._data[0] = 0']],a:0,w:'Elemen di atas size dianggap tidak ada, jadi cukup mengatur size ke 0.'},
 java:`int[] data = new int[2];
int size = 0;
// add(nilai) dipanggil 3x: 5, 7, 9
if («full|size == data.length») {
    data = «grow|Arrays.copyOf(data, size * 2)»;
}
«put|data[size] = nilai;»
size++;`,
 python:`data = [0] * 2
size = 0
# add(nilai) dipanggil 3x: 5, 7, 9
if «full|size == len(data)»:
    data = «grow|data + [0] * len(data)»
«put|data[size] = nilai»
size += 1`,
 legend:{full:['kapasitas','Penuh jika size sudah sama dengan kapasitas.'],grow:['kapasitas','Array baru 2× lebih besar, isi lama disalin.'],put:['kapasitas','Elemen baru selalu masuk di slot data[size].']},
 trace:()=>{const T='int[]|list';let data=[0,0],size=0;const s=[{j:1,p:1,s:{data:[T,{arr:[...data],used:0}]},n:'Kapasitas awal 2. Slot bertitik masih dianggap kosong.'},{j:2,p:2,s:{size:['int',0]},n:'Belum ada elemen.'}];
  for(const v of [5,7,9]){s.push({j:3,p:3,s:{nilai:['int',v]},n:`add(${v}) dipanggil.`});
   if(size===data.length){s.push({j:4,p:4,n:`size (${size}) == kapasitas (${data.length}) → penuh!`});data=data.concat(new Array(data.length).fill(0));s.push({j:5,p:5,s:{data:[T,{arr:[...data],used:size}]},n:`Array baru berkapasitas ${data.length}. ${size} elemen lama disalin.`})}
   else s.push({j:4,p:4,n:`size (${size}) < kapasitas (${data.length}). Masih ada slot.`});
   data[size]=v;s.push({j:7,p:6,s:{data:[T,{arr:[...data],used:size+1,hl:[size]}]},n:`data[${size}] = ${v}.`});size++;s.push({j:8,p:7,s:{size:['int',size]},n:`size = ${size}.`})}
  return s},
 rumus:{f:'slot berikutnya = data[size] · penuh → kapasitas × 2',i:['size = yang dipakai. Kapasitas = data.length.','Penggandaan membuat add rata-rata tetap cepat.','Slot di atas size dianggap kosong walau berisi angka sisa.']}},
{t:'Precondition & exception',
 tr:[['Ambil elemen ke-i','public int get(int i)','def get(self, i):'],['Jika i di luar 0 sampai size − 1','if (i < 0 || i >= size)','if i < 0 or i >= self._size:'],['tolak dengan error yang jelas','throw new IndexOutOfBoundsException("i=" + i);','raise IndexError(f"i={i}")']],
 ex:{q:'Tolak umur negatif di method setUmur',o:[['if (u < 0) throw new IllegalArgumentException("umur negatif");','if u < 0:\n    raise ValueError("umur negatif")'],['if (u < 0) return;','if u < 0:\n    return'],['if (u < 0) u = 0;','if u < 0:\n    u = 0']],a:0,w:'Menolak dengan exception membuat kesalahan pemanggil langsung ketahuan. Diam-diam mengabaikan atau mengganti nilai menyembunyikan bug.'},
 java:`public int get(int i) {
    if («pre|i < 0 || i >= size») {
        «thr|throw new IndexOutOfBoundsException("i=" + i);»
    }
    return data[i];
}`,
 python:`def get(self, i):
    if «pre|i < 0 or i >= self._size»:
        «thr|raise IndexError(f"i={i}")»
    return self._data[i]`,
 legend:{pre:['precondition','Syarat indeks valid: 0 ≤ i < size.'],thr:['exception','Lempar error yang jelas, bukan nilai sampah.']},
 trace:[
  {j:1,p:1,s:{data:['int[]|list',{arr:[5,7,9,0],used:3}],size:['int',3],i:['int',1]},n:'Panggil get(1). size = 3, kapasitas 4.'},
  {j:2,p:2,n:'1 < 0 atau 1 >= 3? false. Indeks valid.'},
  {j:5,p:4,s:{hasil:['int',7],data:['int[]|list',{arr:[5,7,9,0],used:3,hl:[1]}]},n:'return data[1] = 7.'},
  {j:1,p:1,s:{i:['int',3],data:['int[]|list',{arr:[5,7,9,0],used:3}]},d:['hasil'],n:'Panggil get(3). Slot 3 ada di array, tapi belum dipakai.'},
  {j:2,p:2,n:'3 >= 3 → true. Precondition dilanggar.'},
  {j:3,p:3,oj:'IndexOutOfBoundsException: i=3\n',op:'IndexError: i=3\n',n:'Exception dilempar. return tidak pernah dicapai.'}],
 rumus:{f:'indeks valid: 0 ≤ i < size      (bukan < kapasitas)',i:['Cek precondition di baris paling awal method.','Pesan exception sebaiknya menyebut nilai yang salah.','Kalimat "hanya boleh jika …" dalam soal adalah precondition.']}}
],
16:[
{t:'Node & menambah di depan',
 tr:[['List kosong','ListNode front = null;','front = None'],['Taruh 3 di depan','front = new ListNode(3, front);','front = ListNode(3, front)'],['Taruh 7 di depan','front = new ListNode(7, front);','front = ListNode(7, front)'],['Isi node kedua','front.next.data','front.next.data']],
 ex:{q:'Ambil isi node KETIGA',o:[['front.next.next.data','front.next.next.data'],['front.next.data','front.next.data'],['front[2]','front[2]']],a:0,w:'Node pertama = front, kedua = front.next, ketiga = front.next.next. Linked list tidak punya indeks.'},
 java:`ListNode front = «nul|null»;
front = «newn|new ListNode(3, front)»;
front = new ListNode(7, front);
System.out.println(«data|front.data»);
System.out.println(«next|front.next.data»);`,
 python:`front = «nul|None»
front = «newn|ListNode(3, front)»
front = ListNode(7, front)
print(«data|front.data»)
print(«next|front.next.data»)`,
 legend:{nul:['null','List kosong: front tidak menunjuk apa pun.'],newn:['node','Node baru berisi 3, next-nya = front lama.'],data:['node','Isi node pertama.'],next:['referensi','Ikuti satu panah, lalu ambil isinya.']},
 trace:[
  {j:1,p:1,s:{front:['ListNode',null]},n:'List kosong.'},
  {j:2,p:2,s:{front:['ListNode',{chain:[3],at:0}]},n:'Node 3 dibuat. next-nya = front lama (null). front pindah ke node baru.'},
  {j:3,p:3,s:{front:['ListNode',{chain:[7,3],at:0}]},n:'Node 7 dibuat, next-nya menunjuk node 3. front pindah ke 7.'},
  {j:4,p:4,o:'7\n',n:'front.data = 7.'},
  {j:5,p:5,o:'3\n',s:{front:['ListNode',{chain:[7,3],at:1}]},n:'front.next → node 3, lalu .data = 3.'}],
 rumus:{f:'setiap .next = ikuti satu panah',i:['Baca dari kiri: front → .next → .data.','addFirst: front = new ListNode(x, front). Node baru menunjuk front LAMA.','front.next.next.data = elemen ketiga.']}},
{t:'Menelusuri linked list',
 tr:[['Mulai dari node pertama','ListNode cur = front;','cur = front'],['Selama masih ada node','while (cur != null)','while cur is not None:'],['tambahkan isinya ke total','total += cur.data;','total += cur.data'],['lalu maju ke node berikutnya','cur = cur.next;','cur = cur.next']],
 ex:{q:'Hitung banyaknya node',o:[['int c = 0; ListNode cur = front; while (cur != null) { c++; cur = cur.next; }','c = 0\ncur = front\nwhile cur is not None:\n    c += 1\n    cur = cur.next'],['int c = 0; while (front != null) c++;','c = 0\nwhile front is not None:\n    c += 1'],['int c = front.size();','c = len(front)']],a:0,w:'Template penelusuran dengan cur. Opsi kedua tidak pernah maju sehingga loop tidak berhenti.'},
 java:`ListNode cur = front;
int total = 0;
«cond|while (cur != null)» {
    total += cur.data;
    «step|cur = cur.next;»
}`,
 python:`cur = front
total = 0
«cond|while cur is not None:»
    total += cur.data
    «step|cur = cur.next»`,
 legend:{cond:['null','Berhenti saat cur jatuh ke null (lewat node terakhir).'],step:['traversal','Maju satu node. Lupa baris ini → loop tak hingga.']},
 trace:()=>{const C=[7,3,5];const s=[{j:1,p:1,s:{cur:['ListNode',{chain:C,at:0}]},n:'cur mulai dari node pertama (list: 7 → 3 → 5).'},{j:2,p:2,s:{total:['int',0]},n:'total = 0.'}];let t=0;
  C.forEach((v,k)=>{s.push({j:3,p:3,n:`cur menunjuk node ${v}, bukan null → masuk.`});t+=v;s.push({j:4,p:4,s:{total:['int',t]},n:`total += ${v} → ${t}.`});s.push({j:5,p:5,s:{cur:['ListNode',k<2?{chain:C,at:k+1}:null]},n:k<2?`cur maju ke node ${C[k+1]}.`:'cur = next dari node terakhir = null.'})});
  s.push({j:3,p:3,n:'cur == null → keluar. total = 15.'});return s},
 rumus:{f:'cur = front; while (cur != null) { …; cur = cur.next; }',i:['Ini template untuk hampir semua operasi linked list.','Untuk mengubah list, berhenti SATU node sebelum target: while (cur.next != null).','Selalu pikirkan kasus front == null.']}}
],
17:[
{t:'Menyisipkan ke BST',
 tr:[['Jika tempatnya kosong, taruh node baru di sini','if (node == null) return new IntTreeNode(v);','if node is None: return TreeNode(v)'],['Jika lebih kecil, sisipkan ke kiri','if (v < node.data) node.left = add(node.left, v);','if v < node.data: node.left = add(node.left, v)'],['Selain itu, sisipkan ke kanan','else node.right = add(node.right, v);','else: node.right = add(node.right, v)']],
 ex:{q:'Cari apakah nilai v ada di BST (rekursif)',o:[['boolean ada(Node n, int v) { if (n == null) return false; if (v == n.data) return true; if (v < n.data) return ada(n.left, v); return ada(n.right, v); }','def ada(n, v):\n    if n is None: return False\n    if v == n.data: return True\n    if v < n.data: return ada(n.left, v)\n    return ada(n.right, v)'],['boolean ada(Node n, int v) { return ada(n.left, v) || ada(n.right, v); }','def ada(n, v):\n    return ada(n.left, v) or ada(n.right, v)'],['boolean ada(Node n, int v) { if (v < n.data) return ada(n.right, v); return ada(n.left, v); }','def ada(n, v):\n    if v < n.data: return ada(n.right, v)\n    return ada(n.left, v)']],a:0,w:'Butuh base case null, berhenti saat ketemu, dan arah yang benar: kecil ke kiri.'},
 java:`IntTreeNode add(IntTreeNode node, int v) {
    if («spot|node == null») return new IntTreeNode(v);
    if («go|v < node.data») node.left = add(node.left, v);
    else node.right = add(node.right, v);
    return node;
}`,
 python:`def add(node, v):
    if «spot|node is None»: return TreeNode(v)
    if «go|v < node.data»: node.left = add(node.left, v)
    else: node.right = add(node.right, v)
    return node`,
 legend:{spot:['base-case','Tempat kosong ditemukan: buat node baru di sini.'],go:['bst','Lebih kecil ke kiri, selain itu ke kanan.']},
 trace:()=>{const T='IntTreeNode|TreeNode';const path=[[50,'kiri'],[30,'kiri'],[20,'kanan']];const s=[{j:1,p:1,s:{v:['int',25],node:[T,'→ 50 (akar)']},n:'add(akar, 25). Pohon berisi 50, 30, 70, 20, 40.'}];
  path.forEach(([nv,dir],k)=>{s.push({j:2,p:2,n:`node ${nv} bukan null.`});s.push({j:dir==='kiri'?3:4,p:dir==='kiri'?3:4,n:`25 < ${nv}? ${dir==='kiri'?'true → ke kiri':'false → ke kanan'}.`});const nx=k<2?path[k+1][0]:null;
   s.push({j:1,p:1,s:{node:[T,nx?`→ ${nx}`:null],jalur:['',path.slice(0,k+1).map(x=>x[0]).join(' → ')]},n:nx?`Rekursi: add(node ${nx}, 25).`:`Rekursi: add(null, 25). Anak ${dir} dari 20 kosong.`})});
  s.push({j:2,p:2,s:{node:[T,'→ 25 (baru)']},n:'node == null → base case. Buat node baru 25 dan kembalikan.'});
  s.push({j:4,p:4,n:'Kembali ke node 20: node.right = node 25. Tersambung.'});s.push({j:5,p:5,n:'Setiap level mengembalikan node-nya sendiri sampai ke akar. Total 3 perbandingan.'});return s},
 rumus:{f:'kecil → kiri · besar → kanan · ulangi sampai null',i:['Banyak perbandingan = kedalaman tempat node baru.','node.left = add(node.left, v) menyambung node baru ke induknya saat rekursi kembali.','Data masuk terurut (10, 20, 30, …) → pohon miring → lambat seperti linked list.']}},
{t:'Traversal in-order',
 tr:[['Kunjungi seluruh subpohon kiri','inOrder(node.left);','in_order(node.left)'],['cetak akar','System.out.print(node.data + " ");','print(node.data, end=" ")'],['lalu kunjungi subpohon kanan','inOrder(node.right);','in_order(node.right)']],
 ex:{q:'Ubah menjadi traversal PRE-order',o:[['print(node.data); inOrder(node.left); inOrder(node.right);','print(node.data)\npre(node.left)\npre(node.right)'],['inOrder(node.left); inOrder(node.right); print(node.data);','pre(node.left)\npre(node.right)\nprint(node.data)'],['inOrder(node.right); print(node.data); inOrder(node.left);','pre(node.right)\nprint(node.data)\npre(node.left)']],a:0,w:'Pre = akar dicetak di AWAL, sebelum kedua pemanggilan rekursif.'},
 java:`void inOrder(IntTreeNode node) {
    if (node != null) {
        «L|inOrder(node.left);»
        «P|System.out.print(node.data + " ");»
        «R|inOrder(node.right);»
    }
}`,
 python:`def in_order(node):
    if node is not None:
        «L|in_order(node.left)»
        «P|print(node.data, end=" ")»
        «R|in_order(node.right)»`,
 legend:{L:['traversal','Kunjungi seluruh subpohon kiri dulu.'],P:['traversal','Cetak akar. Posisinya di TENGAH → in-order.'],R:['traversal','Lalu subpohon kanan.']},
 trace:()=>{const s=[];const T='IntTreeNode|TreeNode';const nm=k=>`node · level ${k}`;
  const go=(n,lv)=>{s.push({j:1,p:1,s:{[nm(lv)]:[T,`→ ${n.v}`]},n:`inOrder(node ${n.v}).`});
   s.push({j:3,p:3,n:n.l?`Kunjungi kiri dulu: node ${n.l.v}.`:`node ${n.v} tidak punya anak kiri (null). Langsung lanjut.`});if(n.l)go(n.l,lv+1);
   s.push({j:4,p:4,o:n.v+' ',n:`Kembali di node ${n.v}. Cetak ${n.v}.`});
   s.push({j:5,p:5,n:n.r?`Lalu kanan: node ${n.r.v}.`:'Anak kanan null.'});if(n.r)go(n.r,lv+1);
   s.push({j:7,p:2,d:[nm(lv)],n:`Node ${n.v} selesai. Kembali ke pemanggil.`})};
  go({v:2,l:{v:1},r:{v:3}},0);return s},
 rumus:{f:'pre = cetak di awal · in = di tengah · post = di akhir',i:['Posisi baris cetak di antara dua pemanggilan rekursif menentukan jenis traversal.','In-order BST → terurut naik.','Post-order cocok untuk menghapus pohon (anak dulu, baru induk).']}}
],
18:[
{t:'Hashing & collision',
 tr:[['Tentukan ember untuk kunci 23 dari 7 ember','int i = 23 % 7;','i = 23 % 7'],['Simpan kunci di ember itu','tabel[i].add(23);','tabel[i].append(23)'],['Kunci 16 jatuh di ember yang sama: sambung di rantai','tabel[16 % 7].add(16);','tabel[16 % 7].append(16)']],
 ex:{q:'Tabel punya 10 ember. Di ember mana kunci 1234 disimpan?',o:[['1234 % 10 = 4','1234 % 10 = 4'],['1234 / 10 = 123','1234 // 10 = 123'],['1234 % 4 = 2','1234 % 4 = 2']],a:0,w:'indeks = kunci % jumlahEmber.'},
 java:`List<Integer>[] tabel = new List[7];
int k1 = 23;
int i1 = «hash|k1 % 7»;
tabel[i1].add(k1);
int k2 = 16;
int i2 = k2 % 7;
«col|tabel[i2].add(k2)»;`,
 python:`tabel = [[] for _ in range(7)]
k1 = 23
i1 = «hash|k1 % 7»
tabel[i1].append(k1)
k2 = 16
i2 = k2 % 7
«col|tabel[i2].append(k2)»`,
 legend:{hash:['hashing','Fungsi hash sederhana: sisa bagi jumlah ember.'],col:['collision','Ember 2 sudah berisi 23 → collision, disambung di rantai.']},
 trace:()=>{const T='List[]|list';const b=Array.from({length:7},()=>[]);const cp=h=>({buckets:b.map(x=>[...x]),hit:h});const s=[{j:1,p:1,s:{tabel:[T,cp(-1)]},n:'Tabel 7 ember, semuanya kosong.'}];
  s.push({j:2,p:2,s:{k1:['int',23]},n:'Kunci pertama: 23.'});s.push({j:3,p:3,s:{i1:['int',2]},n:'23 % 7 = 2 (23 = 7 × 3 + 2).'});b[2].push(23);s.push({j:4,p:4,s:{tabel:[T,cp(2)]},n:'Masukkan ke ember 2.'});
  s.push({j:5,p:5,s:{k2:['int',16]},n:'Kunci kedua: 16.'});s.push({j:6,p:6,s:{i2:['int',2]},n:'16 % 7 = 2 juga!'});b[2].push(16);s.push({j:7,p:7,s:{tabel:[T,cp(2)]},n:'Collision: ember 2 sudah berisi 23. 16 disambung di rantai yang sama.'});return s},
 rumus:{f:'indeks = hash(kunci) % jumlahEmber',i:['Kunci sama → selalu indeks sama. Itu yang membuat pencarian cepat.','Kunci berbeda bisa jatuh di indeks sama (collision) → disimpan berantai.','Load factor = data / ember. Terlalu tinggi → tabel diperbesar dan semua kunci di-hash ulang.']}},
{t:'Heap & priority queue',
 tr:[['Masukkan 5, 3, 8, 1 ke antrean prioritas','pq.add(x);','heapq.heappush(pq, x)'],['Ambil yang paling kecil','pq.remove()','heapq.heappop(pq)']],
 ex:{q:'Di heap berbasis array, siapa induk dari elemen di indeks 5?',o:[['(5 − 1) / 2 = 2','(5 - 1) // 2 = 2'],['5 / 2 = 2,5','5 / 2'],['2 × 5 + 1 = 11','2 * 5 + 1']],a:0,w:'Rumus induk: (i − 1) / 2. Rumus 2i + 1 adalah anak kiri.'},
 java:`PriorityQueue<Integer> pq = new PriorityQueue<>();
for (int x : new int[]{5, 3, 8, 1}) {
    «add|pq.add(x)»;
}
int min = «rm|pq.remove()»;`,
 python:`pq = []
for x in [5, 3, 8, 1]:
    «add|heapq.heappush(pq, x)»
mn = «rm|heapq.heappop(pq)»`,
 legend:{add:['heap','Masuk di ujung array, lalu naik selama lebih kecil dari induk.'],rm:['priority-queue','Ambil akar (minimum), isi akar dengan elemen terakhir, lalu turunkan.']},
 trace:()=>{const T='PriorityQueue|list';const h=[];const s=[{j:1,p:1,s:{pq:[T,{arr:[]}]},n:'Heap kosong.'}];
  for(const x of [5,3,8,1]){s.push({j:2,p:2,s:{x:['int',x]},n:`x = ${x}.`});h.push(x);let i=h.length-1;s.push({j:3,p:3,s:{pq:[T,{arr:[...h],hl:[i]}]},n:`Taruh ${x} di ujung, indeks ${i}.`});
   while(i>0){const p=Math.floor((i-1)/2);if(h[p]<=h[i]){s.push({j:3,p:3,n:`Induk di indeks ${p} bernilai ${h[p]} ≤ ${h[i]}. Berhenti.`});break}[h[p],h[i]]=[h[i],h[p]];s.push({j:3,p:3,s:{pq:[T,{arr:[...h],hl:[p]}]},n:`Induk (${i} − 1) / 2 = ${p} lebih besar → tukar, ${h[p]} naik ke indeks ${p}.`});i=p}}
  const top=h[0],last=h.pop();h[0]=last;s.push({j:5,p:4,sj:{min:['int',top]},sp:{mn:['int',top]},s:{pq:[T,{arr:[...h],hl:[0]}]},dj:['x'],n:`Ambil akar ${top} (minimum). Elemen terakhir (${last}) dipindah ke akar.`});
  let i=0;while(true){const l=2*i+1,r=l+1;let m=i;if(l<h.length&&h[l]<h[m])m=l;if(r<h.length&&h[r]<h[m])m=r;if(m===i){s.push({j:5,p:4,n:'Anak-anaknya tidak lebih kecil. Heap valid lagi.'});break}[h[m],h[i]]=[h[i],h[m]];s.push({j:5,p:4,s:{pq:[T,{arr:[...h],hl:[m]}]},n:`Anak terkecil (indeks ${m}) lebih kecil → tukar, turun.`});i=m}
  return s},
 rumus:{f:'anak = 2i + 1, 2i + 2 · induk = (i − 1) / 2',i:['Akar (indeks 0) selalu minimum.','add dan remove masing-masing O(log n): naik atau turun paling banyak setinggi pohon.','Kalimat "yang paling penting / paling kecil / paling mendesak duluan" → priority queue.']}}
],
19:[
{t:'Lambda',
 tr:[['Buat fungsi kecil "dobel" yang menerima x dan mengembalikan x × 2','Function<Integer, Integer> dobel = x -> x * 2;','dobel = lambda x: x * 2'],['Jalankan dobel dengan 5','dobel.apply(5)','dobel(5)']],
 ex:{q:'Fungsi tanpa nama yang menerima a dan b lalu mengembalikan yang lebih besar',o:[['(a, b) -> Math.max(a, b)','lambda a, b: max(a, b)'],['a, b -> return max','lambda: max(a, b)'],['(a, b) => a > b','def (a, b): max']],a:0,w:'Pola lambda: (parameter) -> ekspresi hasil. Python: lambda parameter: ekspresi.'},
 java:`Function<Integer, Integer> dobel = «lam|x -> x * 2»;
int a = «app|dobel.apply(5)»;
int b = dobel.apply(a);`,
 python:`dobel = «lam|lambda x: x * 2»
a = «app|dobel(5)»
b = dobel(a)`,
 legend:{lam:['lambda','Fungsi tanpa nama: terima x, kembalikan x * 2.'],app:['higher-order','Fungsi disimpan di variabel lalu dipanggil.']},
 trace:[
  {j:1,p:1,s:{dobel:['Function|function','fungsi: x → x * 2']},n:'Fungsi disimpan di variabel. Belum dijalankan.'},
  {j:2,p:2,s:{a:['int',10]},n:'Jalankan dengan x = 5 → 5 * 2 = 10.'},
  {j:3,p:3,s:{b:['int',20]},n:'Jalankan lagi dengan x = a = 10 → 20.'}],
 rumus:{f:'(parameter) -> ekspresi hasil',i:['x -> x * 2 dibaca "terima x, kembalikan x kali 2".','Lebih dari satu parameter: (a, b) -> a + b / lambda a, b: a + b.','Lambda hanya untuk logika pendek. Yang panjang, tulis method biasa.']}},
{t:'filter, map, reduce',
 tr:[['Dari daftar angka','List.of(1, 2, 3, 4)','[1, 2, 3, 4]'],['ambil yang genap','.filter(n -> n % 2 == 0)','[n for n in a if n % 2 == 0]'],['kuadratkan masing-masing','.map(n -> n * n)','[n * n for n in g]'],['lalu jumlahkan semuanya','.reduce(0, Integer::sum)','sum(k)']],
 ex:{q:'Dari daftar nama, ambil yang panjangnya lebih dari 3 lalu ubah jadi huruf besar',o:[['nama.stream().filter(s -> s.length() > 3).map(String::toUpperCase).toList()','[s.upper() for s in nama if len(s) > 3]'],['nama.stream().map(s -> s.length() > 3).toList()','[len(s) > 3 for s in nama]'],['nama.stream().filter(String::toUpperCase).toList()','[s for s in nama if s.upper()]']],a:0,w:'"ambil yang …" → filter, "ubah jadi …" → map. Urutan kalimat = urutan pipeline.'},
 java:`List<Integer> a = List.of(1, 2, 3, 4);
List<Integer> g = a.stream().«flt|filter(n -> n % 2 == 0)».toList();
List<Integer> k = g.stream().«mp|map(n -> n * n)».toList();
int s = k.stream().«rd|reduce(0, Integer::sum)»;`,
 python:`a = [1, 2, 3, 4]
g = «flt|[n for n in a if n % 2 == 0]»
k = «mp|[n * n for n in g]»
s = «rd|sum(k)»`,
 legend:{flt:['map-filter-reduce','filter: ambil yang memenuhi syarat.'],mp:['map-filter-reduce','map: ubah setiap elemen.'],rd:['map-filter-reduce','reduce: gabungkan semua menjadi satu nilai.']},
 trace:[
  {j:1,p:1,s:{a:['List|list',[1,2,3,4]]},n:'Data awal empat angka.'},
  {j:2,p:2,s:{g:['List|list',[2,4]]},n:'filter menyisakan yang genap: 2 dan 4. a tidak berubah.'},
  {j:3,p:3,s:{k:['List|list',[4,16]]},n:'map mengkuadratkan setiap elemen: 4 dan 16.'},
  {j:4,p:4,s:{s:['int',20]},n:'reduce / sum menjumlahkan: 0 + 4 + 16 = 20.'}],
 rumus:{f:'filter: jumlah ↓ · map: jumlah tetap · reduce: banyak → 1',i:['filter bisa mengurangi jumlah elemen, map tidak pernah.','Setiap tahap menghasilkan koleksi baru. Data asal tidak berubah (immutable).','Baca kalimat soal dari kiri: "ambil … → ubah … → gabungkan …" menjadi filter → map → reduce.']}}
]
};

/* ===================== KUIS CERITA ===================== */
const STORIES = [
{b:2,t:'Uang jajan Dina',s:'Dina punya Rp7.000 dan ingin membeli permen seharga Rp2.000 sebanyak mungkin. Ia menulis program untuk menghitung jumlah permen dan sisa uangnya.',
 java:`int uang = 7000;
int harga = 2000;
int permen = uang / harga;
int sisa = uang % harga;
System.out.println(permen + " permen, sisa " + sisa);`,
 python:`uang = 7000
harga = 2000
permen = uang // harga
sisa = uang % harga
print(permen, "permen, sisa", sisa)`,
 q:'Apa yang dicetak program?',o:['3 permen, sisa 1000','3.5 permen, sisa 0','4 permen, sisa -1000','3 permen, sisa 0'],a:0,w:'7000 / 2000 = 3 (pecahan dibuang), 7000 % 2000 = 1000.'},
{b:2,t:'Tangga bintang Budi',s:'Budi menggambar tangga setinggi 5 anak tangga. Baris pertama berisi 1 bintang, baris kedua 2 bintang, dan seterusnya.',
 java:`for (int b = 1; b <= 5; b++) {
    for (int k = 1; k <= b; k++) {
        System.out.print("*");
    }
    System.out.println();
}`,
 python:`for b in range(1, 6):
    for k in range(b):
        print("*", end="")
    print()`,
 q:'Berapa total bintang yang tercetak?',o:['15','25','10','5'],a:0,w:'1 + 2 + 3 + 4 + 5 = 15, atau 5 × 6 / 2.'},
{b:3,t:'Diskon toko Pak Andi',s:'Pak Andi membuat method untuk menghitung harga setelah diskon. Seorang pembeli membeli barang Rp50.000 dengan diskon 15%.',
 java:`public static int hargaDiskon(int harga, int persen) {
    return harga - harga * persen / 100;
}
// hargaDiskon(50000, 15)`,
 python:`def harga_diskon(harga, persen):
    return harga - harga * persen // 100

# harga_diskon(50000, 15)`,
 q:'Berapa nilai yang dikembalikan?',o:['42500','7500','49985','35000'],a:0,w:'50000 × 15 / 100 = 7500 (perkalian dulu, dari kiri), lalu 50000 − 7500 = 42500.'},
{b:3,t:'Username Rina',s:'Aplikasi sekolah membuat username dari bagian email sebelum tanda titik. Email Rina adalah "rina.putri@mail.com".',
 java:`String email = "rina.putri@mail.com";
String user = email.substring(0, email.indexOf("."));`,
 python:`email = "rina.putri@mail.com"
user = email[:email.index(".")]`,
 q:'Apa isi variabel user?',o:['rina','rina.','putri','r'],a:0,w:'indexOf(".") = 4. substring(0, 4) mengambil indeks 0 sampai 3: "rina".'},
{b:4,t:'Tarif parkir mal',s:'Parkir di mal gratis tidak ada. Dua jam pertama Rp5.000, setiap jam berikutnya Rp3.000. Ayah parkir selama 5 jam.',
 java:`int jam = 5;
int tarif;
if (jam <= 2) {
    tarif = 5000;
} else {
    tarif = 5000 + (jam - 2) * 3000;
}`,
 python:`jam = 5
if jam <= 2:
    tarif = 5000
else:
    tarif = 5000 + (jam - 2) * 3000`,
 q:'Berapa tarif yang harus dibayar?',o:['14000','20000','15000','9000'],a:0,w:'(5 − 2) × 3000 = 9000, ditambah 5000 = 14000.'},
{b:4,t:'Bug di rapor',s:'Pak Guru menulis program huruf nilai. Siswa dengan skor 95 protes karena hurufnya aneh.',
 java:`int skor = 95;
if (skor >= 70) {
    System.out.println("C");
} else if (skor >= 80) {
    System.out.println("B");
} else if (skor >= 90) {
    System.out.println("A");
}`,
 python:`skor = 95
if skor >= 70:
    print("C")
elif skor >= 80:
    print("B")
elif skor >= 90:
    print("A")`,
 q:'Apa yang dicetak?',o:['A','C','B','A, B, lalu C'],a:1,w:'95 >= 70 sudah true di cabang pertama, sisanya dilewati. Perbaikannya: urutkan dari kondisi paling ketat (>= 90) dulu.'},
{b:5,t:'Tabungan Sari',s:'Sari punya tabungan Rp100.000 dan menabung Rp20.000 setiap bulan sampai tabungannya minimal Rp150.000.',
 java:`int saldo = 100000;
int bulan = 0;
while (saldo < 150000) {
    saldo += 20000;
    bulan++;
}`,
 python:`saldo = 100000
bulan = 0
while saldo < 150000:
    saldo += 20000
    bulan += 1`,
 q:'Berapa nilai bulan setelah loop selesai?',o:['3','2','2.5','5'],a:0,w:'120.000 (1), 140.000 (2), 160.000 (3). Setelah itu 160.000 < 150.000 false.'},
{b:5,t:'Satpam gerbang sekolah',s:'Siswa boleh masuk jika punya kartu dan tidak terlambat, atau jika ia tamu VIP. Hari ini Doni punya kartu tetapi terlambat, dan ia bukan VIP.',
 java:`boolean kartu = true, telat = true, vip = false;
boolean masuk = (kartu && !telat) || vip;`,
 python:`kartu, telat, vip = True, True, False
masuk = (kartu and not telat) or vip`,
 q:'Berapa nilai masuk?',o:['false','true','Error','Tergantung urutan'],a:0,w:'kartu && !telat = true && false = false. false || false = false.'},
{b:5,t:'Daftar belanja Ibu',s:'Ibu ingin mencetak daftar belanja "apel, susu, roti". Program anaknya mencetak sesuatu yang sedikit berbeda.',
 java:`String[] b = {"apel", "susu", "roti"};
for (String x : b) {
    System.out.print(x + ", ");
}`,
 python:`b = ["apel", "susu", "roti"]
for x in b:
    print(x + ", ", end="")`,
 q:'Apa masalahnya dan bagaimana memperbaikinya?',o:['Ada koma berlebih di akhir. Cetak item pertama di luar loop (fencepost).','Loop tidak pernah berhenti.','Item terakhir tidak tercetak.','Tidak ada masalah.'],a:0,w:'Hasilnya "apel, susu, roti, ". Tiga item hanya butuh dua koma.'},
{b:6,t:'Rekap absensi',s:'Satu baris file absen berisi nama lalu kode kehadiran per hari: H (hadir), A (alfa), I (izin).',
 java:`Scanner baris = new Scanner("Ani H H A H I");
String nama = baris.next();
int hadir = 0;
while (baris.hasNext()) {
    if (baris.next().equals("H")) {
        hadir++;
    }
}`,
 python:`t = "Ani H H A H I".split()
nama = t[0]
hadir = 0
for s in t[1:]:
    if s == "H":
        hadir += 1`,
 q:'Berapa nilai hadir?',o:['3','4','5','2'],a:0,w:'Token setelah nama: H H A H I. Ada tiga H. Nama sudah diambil lebih dulu.'},
{b:7,t:'Suhu seminggu',s:'BMKG mencatat suhu harian selama seminggu. Kamu diminta menghitung berapa hari yang suhunya di atas 30°C.',
 java:`int[] suhu = {30, 32, 29, 35, 31, 28, 33};
int panas = 0;
for (int s : suhu) {
    if (s > 30) panas++;
}`,
 python:`suhu = [30, 32, 29, 35, 31, 28, 33]
panas = 0
for s in suhu:
    if s > 30:
        panas += 1`,
 q:'Berapa nilai panas?',o:['4','3','5','7'],a:0,w:'Yang di atas 30: 32, 35, 31, 33. Angka 30 tidak termasuk karena syaratnya > 30.'},
{b:7,t:'Kursi bioskop',s:'Bioskop kecil punya 10 kursi. Petugas ingin menandai kursi nomor 10 sebagai terisi.',
 java:`boolean[] kursi = new boolean[10];
kursi[10] = true;`,
 python:`kursi = [False] * 10
kursi[10] = True`,
 q:'Apa yang terjadi?',o:['Kursi terakhir terisi','Error: ArrayIndexOutOfBoundsException / IndexError','Kursi pertama terisi','Array otomatis bertambah'],a:1,w:'Indeks valid 0 sampai 9. Kursi nomor 10 (hitungan manusia) ada di kursi[9].'},
{b:7,t:'Fotokopi nilai',s:'Guru ingin mencoba mengubah nilai tanpa merusak data asli. Ia "menyalin" array lalu mengubah salinannya.',
 java:`int[] asli = {80, 90};
int[] salinan = asli;
salinan[0] = 0;
System.out.println(asli[0]);`,
 python:`asli = [80, 90]
salinan = asli
salinan[0] = 0
print(asli[0])`,
 q:'Apa yang dicetak?',o:['80','0','Error','90'],a:1,w:'salinan = asli hanya menyalin alamat. Keduanya array yang sama.'},
{b:8,t:'Rekening bersama',s:'Ayah dan Ibu memakai satu rekening. Di program, keduanya diwakili dua variabel.',
 java:`Akun ayah = new Akun(100);
Akun ibu = ayah;
ibu.setor(50);
System.out.println(ayah.getSaldo());`,
 python:`ayah = Akun(100)
ibu = ayah
ibu.setor(50)
print(ayah.get_saldo())`,
 q:'Apa yang dicetak?',o:['100','150','50','200'],a:1,w:'ayah dan ibu menunjuk objek Akun yang sama. Setoran lewat ibu terlihat lewat ayah.'},
{b:9,t:'Kebun binatang',s:'Kelas Burung mewarisi Hewan dan punya method tambahan terbang(). Seorang programmer menulis kode berikut.',
 java:`class Hewan { void makan() { } }
class Burung extends Hewan { void terbang() { } }

Hewan h = new Burung();
h.terbang();`,
 q:'Apa yang terjadi saat kode Java ini dikompilasi?',o:['Burung terbang','Error kompilasi: Hewan tidak punya method terbang()','Runtime error','Tidak terjadi apa-apa'],a:1,w:'Tipe variabel (Hewan) menentukan method yang boleh dipanggil. Solusinya ((Burung) h).terbang(). Di Python, kode serupa berjalan karena duck typing.'},
{b:9,t:'Pentas suara hewan',s:'Di acara sekolah, setiap hewan maju dan bersuara. Kucing berkata "Meong", Anjing berkata "Guk".',
 java:`Hewan[] hs = { new Kucing(), new Anjing(), new Kucing() };
for (Hewan h : hs) {
    System.out.print(h.suara() + " ");
}`,
 python:`hs = [Kucing(), Anjing(), Kucing()]
for h in hs:
    print(h.suara(), end=" ")`,
 q:'Apa yang dicetak?',o:['Meong Guk Meong','... ... ...','Meong Meong Meong','Error'],a:0,w:'Polimorfisme: setiap objek menjalankan versi suara() miliknya sendiri.'},
{b:10,t:'Daftar undangan',s:'Panitia punya daftar undangan. Dua orang membatalkan, dan panitia menghapus indeks 1 dua kali.',
 java:`ArrayList<String> u = new ArrayList<>(List.of("Ani", "Budi", "Cici", "Dodi"));
u.remove(1);
u.remove(1);`,
 python:`u = ["Ani", "Budi", "Cici", "Dodi"]
u.pop(1)
u.pop(1)`,
 q:'Apa isi daftar sekarang?',o:['[Ani, Dodi]','[Ani, Cici]','[Cici, Dodi]','[Ani, Budi]'],a:0,w:'Setelah Budi dihapus, Cici bergeser ke indeks 1, lalu Cici yang terhapus.'},
{b:11,t:'Kata di status',s:'Rara menulis status "aku suka kopi aku suka teh". Ia ingin tahu berapa kata berbeda yang ia pakai.',
 java:`Set<String> s = new HashSet<>();
for (String w : "aku suka kopi aku suka teh".split(" ")) {
    s.add(w);
}
System.out.println(s.size());`,
 python:`s = set("aku suka kopi aku suka teh".split())
print(len(s))`,
 q:'Apa yang dicetak?',o:['4','6','3','2'],a:0,w:'Kata berbeda: aku, suka, kopi, teh.'},
{b:11,t:'Buku nilai',s:'Guru mencatat nilai di map. Nilai Ani dimasukkan dua kali karena ada perbaikan.',
 java:`Map<String, Integer> m = new HashMap<>();
m.put("Ani", 80);
m.put("Budi", 70);
m.put("Ani", 90);
System.out.println(m.get("Ani") + " " + m.size());`,
 python:`m = {}
m["Ani"] = 80
m["Budi"] = 70
m["Ani"] = 90
print(m["Ani"], len(m))`,
 q:'Apa yang dicetak?',o:['90 2','80 3','170 2','80 2'],a:0,w:'Kunci unik. put kedua untuk Ani menimpa 80 menjadi 90.'},
{b:12,t:'Hitung mundur roket',s:'Tim robotik menulis hitung mundur rekursif, tetapi baris cetaknya diletakkan setelah pemanggilan rekursif.',
 java:`void hitung(int n) {
    if (n == 0) {
        System.out.print("Meluncur! ");
    } else {
        hitung(n - 1);
        System.out.print(n + " ");
    }
}
// hitung(3)`,
 python:`def hitung(n):
    if n == 0:
        print("Meluncur!", end=" ")
    else:
        hitung(n - 1)
        print(n, end=" ")

# hitung(3)`,
 q:'Apa yang dicetak oleh hitung(3)?',o:['3 2 1 Meluncur!','Meluncur! 1 2 3','Meluncur! 3 2 1','1 2 3 Meluncur!'],a:1,w:'Cetak dilakukan setelah panggilan rekursif kembali. Yang paling dalam (base case) mencetak lebih dulu.'},
{b:13,t:'Kamus tebal',s:'Kamus 1.000 halaman tersusun alfabetis. Kamu mencari kata dengan selalu membuka bagian tengah dari sisa halaman yang mungkin.',
 q:'Paling banyak berapa kali kamu membuka kamus?',o:['10','100','500','1000'],a:0,w:'Binary search: ⌊log₂ 1000⌋ + 1 = 10 langkah.'},
{b:13,t:'Mengurutkan antrean upacara',s:'Ketua kelas mengurutkan tinggi badan [4, 1, 3, 2] dengan selection sort.',
 q:'Bagaimana isi array setelah putaran pertama (i = 0)?',o:['[1, 4, 3, 2]','[1, 2, 3, 4]','[1, 3, 4, 2]','[4, 1, 3, 2]'],a:0,w:'Minimum (1) ditukar ke indeks 0. Hanya satu pertukaran per putaran.'},
{b:14,t:'Tombol undo',s:'Kamu mengetik huruf A, B, lalu C di editor. Setiap ketikan disimpan di stack. Lalu kamu menekan undo dua kali.',
 java:`Stack<String> s = new Stack<>();
s.push("A"); s.push("B"); s.push("C");
s.pop();
s.pop();`,
 python:`s = ["A", "B", "C"]
s.pop()
s.pop()`,
 q:'Huruf apa yang tersisa?',o:['A','C','AB','BC'],a:0,w:'LIFO: C dan B diambil lebih dulu.'},
{b:14,t:'Loket tiket',s:'Ani dan Budi mengantre. Petugas melayani satu orang, lalu Cici datang, lalu petugas melayani satu orang lagi.',
 java:`Queue<String> q = new LinkedList<>();
q.add("Ani"); q.add("Budi");
q.remove();
q.add("Cici");
String kedua = q.remove();`,
 python:`q = deque(["Ani", "Budi"])
q.popleft()
q.append("Cici")
kedua = q.popleft()`,
 q:'Siapa yang dilayani kedua?',o:['Ani','Budi','Cici','Tidak ada'],a:1,w:'FIFO: Ani dulu, lalu Budi. Cici datang belakangan.'},
{b:15,t:'Rak gudang',s:'Gudang memakai ArrayIntList dengan kapasitas awal 4 yang berlipat dua saat penuh. Petugas menambahkan 5 barang.',
 q:'Berapa size dan kapasitasnya sekarang?',o:['size 5, kapasitas 8','size 5, kapasitas 5','size 4, kapasitas 8','size 5, kapasitas 10'],a:0,w:'Barang ke-5 datang saat penuh (4), jadi kapasitas berlipat menjadi 8.'},
{b:16,t:'Kereta gerbong',s:'Rangkaian kereta digambarkan sebagai linked list: front → 1 → 2 → 3. Gerbong pertama dilepas.',
 java:`// front: 1 -> 2 -> 3
front = front.next;
System.out.println(front.data);`,
 python:`# front: 1 -> 2 -> 3
front = front.next
print(front.data)`,
 q:'Apa yang dicetak?',o:['2','1','3','null'],a:0,w:'front pindah ke node berikutnya (2). Node 1 tidak lagi direferensikan.'},
{b:17,t:'Pohon angka',s:'Angka 40, 20, 60, 10, 30 dimasukkan berurutan ke BST kosong.',
 q:'Apa hasil traversal pre-order?',o:['40 20 10 30 60','10 20 30 40 60','10 30 20 60 40','40 20 60 10 30'],a:0,w:'Akar 40, kiri 20 (anak 10 dan 30), kanan 60. Pre-order: akar, kiri, kanan.'},
{b:18,t:'Loker siswa',s:'Sekolah punya 10 loker. Nomor loker ditentukan dari nomor induk % 10. Nomor induk Dina 1023 dan Eko 2043.',
 q:'Apa yang terjadi?',o:['Keduanya mendapat loker 3: collision','Loker 3 dan loker 4','Loker 2 dan loker 4','Tidak bisa dihitung'],a:0,w:'1023 % 10 = 3 dan 2043 % 10 = 3. Kunci berbeda, ember sama.'},
{b:18,t:'Ruang UGD',s:'Pasien UGD dilayani berdasarkan tingkat kegawatan (angka kecil = paling gawat). Datang berurutan: kegawatan 3, 1, 2.',
 java:`PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(3); pq.add(1); pq.add(2);
System.out.println(pq.remove());`,
 python:`pq = []
for x in [3, 1, 2]:
    heapq.heappush(pq, x)
print(heapq.heappop(pq))`,
 q:'Apa yang dicetak?',o:['1','3','2','Urutan datang'],a:0,w:'Priority queue (min-heap) selalu mengeluarkan yang terkecil.'},
{b:19,t:'Flash sale',s:'Toko daring memberi diskon 50% hanya untuk barang di atas Rp20.000. Kamu menghitung total harga barang yang didiskon.',
 java:`List<Integer> h = List.of(10000, 25000, 40000);
int total = h.stream()
        .filter(x -> x > 20000)
        .map(x -> x / 2)
        .reduce(0, Integer::sum);`,
 python:`h = [10000, 25000, 40000]
total = sum(x // 2 for x in h if x > 20000)`,
 q:'Berapa nilai total?',o:['32500','37500','65000','12500'],a:0,w:'filter → 25000, 40000. map → 12500, 20000. reduce → 32500.'}
];

/* rumus praktis dalam sintaks asli: [java, python] per topik "bab.indeks" */
const RUMUS = {
'1.0':[`public class ClassName {
    public static void main(String[] args) {
        statement1;
        statement2;
    }
}`,`statement1
statement2`],
'1.1':[`// definisi
public static void methodName() {
    statements;
}
// pemanggilan
methodName();`,`# definisi
def method_name():
    statements

# pemanggilan
method_name()`],
'2.0':[`type name;          // deklarasi
name = value;       // assignment
type name = value;  // keduanya sekaligus`,`name = value`],
'2.1':[`a / b    // int / int -> int (dibulatkan ke bawah)
a % b    // sisa bagi
(double) a / b      // pembagian pecahan
a == b * (a / b) + a % b   // selalu true`,`a // b   # pembagian bulat
a % b    # sisa bagi
a / b    # selalu float
a == b * (a // b) + a % b  # selalu True`],
'2.2':[`for (int i = start; i <= end; i++) {
    statements;   // jalan (end - start + 1) kali
}`,`for i in range(start, end + 1):
    statements    # jalan (end - start + 1) kali`],
'2.3':[`for (int i = 1; i <= rows; i++) {
    for (int j = 1; j <= cols; j++) {
        statements;   // jalan rows * cols kali
    }
}`,`for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        statements    # jalan rows * cols kali`],
'3.0':[`public static returnType name(type param) {
    return expression;
}
type result = name(argument);`,`def name(param):
    return expression

result = name(argument)`],
'3.1':[`s.length()          // jumlah karakter
s.charAt(i)         // 0 <= i < s.length()
s.substring(a, b)   // panjangnya b - a`,`len(s)      # jumlah karakter
s[i]        # 0 <= i < len(s)
s[a:b]      # panjangnya b - a`],
'3.2':[`Scanner console = new Scanner(System.in);
System.out.print("prompt: ");
int n = console.nextInt();`,`n = int(input("prompt: "))`],
'4.0':[`if (condition1) {
    statements;
} else if (condition2) {
    statements;
} else {
    statements;
}`,`if condition1:
    statements
elif condition2:
    statements
else:
    statements`],
'4.1':[`type acc = identity;     // 0, 1, "" ...
for (type x : items) {
    acc = acc + x;
}`,`acc = identity           # 0, 1, "" ...
for x in items:
    acc = acc + x`],
'5.0':[`initialization;
while (condition) {
    statements;
    update;
}`,`initialization
while condition:
    statements
    update`],
'5.1':[`a && b    // AND
a || b    // OR
!a        // NOT
!(a && b) == (!a || !b)   // De Morgan`,`a and b   # AND
a or b    # OR
not a     # NOT
(not (a and b)) == (not a or not b)  # De Morgan`],
'5.2':[`System.out.print(first);
for (int i = 2; i <= n; i++) {
    System.out.print(", " + i);
}`,`print(first, end="")
for i in range(2, n + 1):
    print(",", i, end="")`],
'6.0':[`Scanner input = new Scanner(new File("data.txt"));
while (input.hasNextLine()) {
    String line = input.nextLine();
    String[] tokens = line.split(" ");
    int value = Integer.parseInt(tokens[1]);
}`,`with open("data.txt") as f:
    for line in f:
        tokens = line.split()
        value = int(tokens[1])`],
'6.1':[`try {
    statements;
} catch (ExceptionType e) {
    handler;
}`,`try:
    statements
except ExceptionType as e:
    handler`],
'7.0':[`type[] a = new type[length];
a[0]                // elemen pertama
a[a.length - 1]     // elemen terakhir`,`a = [0] * length
a[0]            # elemen pertama
a[len(a) - 1]   # elemen terakhir (atau a[-1])`],
'7.1':[`for (int i = 0; i < a.length; i++) {
    // proses a[i]
}`,`for i in range(len(a)):
    # proses a[i]
    pass`],
'7.2':[`int[] b = a;                       // referensi yang sama
int[] c = Arrays.copyOf(a, a.length); // salinan baru`,`b = a          # referensi yang sama
c = a.copy()   # salinan baru`],
'8.0':[`public class ClassName {
    private type field;
    public ClassName(type param) {
        field = param;
    }
}
ClassName obj = new ClassName(arg);`,`class ClassName:
    def __init__(self, param):
        self.field = param

obj = ClassName(arg)`],
'8.1':[`private type field;
public type getField() { return field; }       // accessor
public void setField(type v) { this.field = v; } // mutator
obj.method(args);`,`def get_field(self):        # accessor
    return self._field
def set_field(self, v):     # mutator
    self._field = v
obj.method(args)`],
'9.0':[`public class Child extends Parent {
    @Override
    public returnType method() {
        return super.method();
    }
}`,`class Child(Parent):
    def method(self):
        return super().method()`],
'9.1':[`public interface Name {
    returnType method();
}
public class ClassName implements Name {
    public returnType method() { ... }
}`,`from abc import ABC, abstractmethod

class Name(ABC):
    @abstractmethod
    def method(self): ...

class ClassName(Name):
    def method(self): ...`],
'10.0':[`list.add(x);         // di akhir
list.add(i, x);      // sisip di indeks i
list.remove(i);      // hapus indeks i
list.set(i, x);      // ganti`,`lst.append(x)      # di akhir
lst.insert(i, x)   # sisip di indeks i
lst.pop(i)         # hapus indeks i
lst[i] = x         # ganti`],
'10.1':[`for (int i = list.size() - 1; i >= 0; i--) {
    if (condition) {
        list.remove(i);
    }
}`,`for i in range(len(lst) - 1, -1, -1):
    if condition:
        lst.pop(i)`],
'11.0':[`Set<type> s = new HashSet<>(list);
s.add(x);
s.contains(x);
s.size();      // jumlah nilai berbeda`,`s = set(lst)
s.add(x)
x in s
len(s)         # jumlah nilai berbeda`],
'11.1':[`Map<K, Integer> m = new HashMap<>();
m.put(key, m.getOrDefault(key, 0) + 1);`,`m = {}
m[key] = m.get(key, 0) + 1`],
'12.0':[`public static type f(int n) {
    if (n <= base) {
        return baseValue;           // base case
    }
    return combine(n, f(n - 1));    // recursive case
}`,`def f(n):
    if n <= base:
        return base_value           # base case
    return combine(n, f(n - 1))     # recursive case`],
'12.1':[`n % 10    // digit terakhir
n / 10    // sisa digit
return n % 10 + f(n / 10);`,`n % 10    # digit terakhir
n // 10   # sisa digit
return n % 10 + f(n // 10)`],
'13.0':[`int lo = 0, hi = a.length - 1;
while (lo <= hi) {
    int mid = (lo + hi) / 2;
    if (a[mid] == target) return mid;
    else if (a[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
return -1;   // O(log n)`,`lo, hi = 0, len(a) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == target: return mid
    elif a[mid] < target: lo = mid + 1
    else: hi = mid - 1
return -1    # O(log n)`],
'13.1':[`for (int i = 0; i < n - 1; i++) {
    int min = i;
    for (int j = i + 1; j < n; j++)
        if (a[j] < a[min]) min = j;
    swap(a, i, min);
}   // n * (n - 1) / 2 perbandingan`,`for i in range(n - 1):
    m = i
    for j in range(i + 1, n):
        if a[j] < a[m]: m = j
    a[i], a[m] = a[m], a[i]
# n * (n - 1) / 2 perbandingan`],
'13.2':[`for (...) { }                    // O(n)
for (...) { for (...) { } }      // O(n^2)
while (n > 1) { n = n / 2; }     // O(log n)`,`for ...:                        # O(n)
for ...:
    for ...:                    # O(n^2)
while n > 1: n //= 2            # O(log n)`],
'14.0':[`Stack<type> s = new Stack<>();
s.push(x);
s.pop();       // ambil yang terakhir masuk
s.peek();
s.isEmpty();`,`s = []
s.append(x)    # push
s.pop()        # ambil yang terakhir masuk
s[-1]          # peek
not s          # kosong?`],
'14.1':[`Queue<type> q = new LinkedList<>();
q.add(x);
q.remove();    // ambil yang pertama masuk
q.peek();`,`from collections import deque
q = deque()
q.append(x)
q.popleft()    # ambil yang pertama masuk
q[0]           # peek`],
'15.0':[`if (size == elementData.length) {
    elementData = Arrays.copyOf(elementData, 2 * size);
}
elementData[size] = value;
size++;`,`if self.size == len(self.data):
    self.data = self.data + [0] * len(self.data)
self.data[self.size] = value
self.size += 1`],
'15.1':[`if (index < 0 || index >= size) {
    throw new IndexOutOfBoundsException("index: " + index);
}`,`if index < 0 or index >= self.size:
    raise IndexError(f"index: {index}")`],
'16.0':[`front = new ListNode(value, front);   // addFirst
front.data          // elemen ke-1
front.next.data     // elemen ke-2`,`front = ListNode(value, front)   # add_first
front.data          # elemen ke-1
front.next.data     # elemen ke-2`],
'16.1':[`ListNode current = front;
while (current != null) {
    // proses current.data
    current = current.next;
}`,`current = front
while current is not None:
    # proses current.data
    current = current.next`],
'17.0':[`private TreeNode add(TreeNode node, int value) {
    if (node == null) return new TreeNode(value);
    if (value < node.data) node.left = add(node.left, value);
    else node.right = add(node.right, value);
    return node;
}`,`def add(node, value):
    if node is None: return TreeNode(value)
    if value < node.data: node.left = add(node.left, value)
    else: node.right = add(node.right, value)
    return node`],
'17.1':[`void inOrder(TreeNode node) {
    if (node != null) {
        inOrder(node.left);
        System.out.print(node.data + " ");   // pre / in / post
        inOrder(node.right);
    }
}`,`def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")   # pre / in / post
        in_order(node.right)`],
'18.0':[`int index = Math.abs(key.hashCode()) % table.length;
table[index].add(key);   // chaining saat collision`,`index = hash(key) % len(table)
table[index].append(key)  # chaining saat collision`],
'18.1':[`int left = 2 * i + 1;
int right = 2 * i + 2;
int parent = (i - 1) / 2;`,`left = 2 * i + 1
right = 2 * i + 2
parent = (i - 1) // 2`],
'19.0':[`(params) -> expression
x -> x * 2
(a, b) -> a + b`,`lambda params: expression
lambda x: x * 2
lambda a, b: a + b`],
'19.1':[`list.stream()
    .filter(x -> condition)
    .map(x -> transform)
    .reduce(identity, (a, b) -> combine)`,`from functools import reduce
reduce(lambda a, b: combine,
       map(lambda x: transform,
           filter(lambda x: condition, lst)),
       identity)`]
};

/* mini project per topik: tugas, langkah, solusi [java, python], keluaran hasil eksekusi nyata (oj/op) */
const PROJ = {"1.0": {"t": "Kartu nama digital", "s": "Cetak kartu nama kamu dengan bingkai dari tanda bintang. Isinya nama, jurusan, dan hobi.", "l": ["Satu baris tampilan = satu statement cetak.", "Cetak bingkai atas, tiga baris isi, lalu bingkai bawah.", "Perhatikan urutan: atas ke bawah."], "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"************************\");\n        System.out.println(\"* Nama   : Rina        *\");\n        System.out.println(\"* Jurusan: Informatika *\");\n        System.out.println(\"* Hobi   : Membaca     *\");\n        System.out.println(\"************************\");\n    }\n}", "python": "print(\"************************\")\nprint(\"* Nama   : Rina        *\")\nprint(\"* Jurusan: Informatika *\")\nprint(\"* Hobi   : Membaca     *\")\nprint(\"************************\")", "oj": "************************\n* Nama   : Rina        *\n* Jurusan: Informatika *\n* Hobi   : Membaca     *\n************************\n", "op": "************************\n* Nama   : Rina        *\n* Jurusan: Informatika *\n* Hobi   : Membaca     *\n************************\n"}, "1.1": {"t": "Lirik lagu dengan reff", "s": "Cetak lirik lagu pendek yang punya reff (chorus) dua kali. Reff ditulis sekali sebagai method, lalu dipanggil dua kali.", "l": ["Cari bagian yang berulang: itulah reff.", "Buat method reff() berisi baris-baris reff.", "Di main: bait 1 → reff() → bait 2 → reff()."], "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Pagi cerah datang lagi\");\n        reff();\n        System.out.println(\"Sore tiba, langit jingga\");\n        reff();\n    }\n\n    public static void reff() {\n        System.out.println(\"  Ayo belajar, ayo coba\");\n        System.out.println(\"  Kode jalan, hati gembira\");\n    }\n}", "python": "def reff():\n    print(\"  Ayo belajar, ayo coba\")\n    print(\"  Kode jalan, hati gembira\")\n\nprint(\"Pagi cerah datang lagi\")\nreff()\nprint(\"Sore tiba, langit jingga\")\nreff()", "oj": "Pagi cerah datang lagi\n  Ayo belajar, ayo coba\n  Kode jalan, hati gembira\nSore tiba, langit jingga\n  Ayo belajar, ayo coba\n  Kode jalan, hati gembira\n", "op": "Pagi cerah datang lagi\n  Ayo belajar, ayo coba\n  Kode jalan, hati gembira\nSore tiba, langit jingga\n  Ayo belajar, ayo coba\n  Kode jalan, hati gembira\n"}, "2.0": {"t": "Struk belanja", "s": "Kamu membeli 3 buku seharga 12500 dan 2 pulpen seharga 4000. Hitung subtotal setiap barang dan total bayar, lalu cetak struknya.", "l": ["Simpan harga dan jumlah setiap barang di variabel.", "subtotal = harga × jumlah.", "total = subtotal buku + subtotal pulpen."], "java": "public class Main {\n    public static void main(String[] args) {\n        int hargaBuku = 12500;\n        int jumlahBuku = 3;\n        int hargaPulpen = 4000;\n        int jumlahPulpen = 2;\n\n        int subBuku = hargaBuku * jumlahBuku;\n        int subPulpen = hargaPulpen * jumlahPulpen;\n        int total = subBuku + subPulpen;\n\n        System.out.println(\"Buku   : \" + subBuku);\n        System.out.println(\"Pulpen : \" + subPulpen);\n        System.out.println(\"Total  : \" + total);\n    }\n}", "python": "harga_buku = 12500\njumlah_buku = 3\nharga_pulpen = 4000\njumlah_pulpen = 2\n\nsub_buku = harga_buku * jumlah_buku\nsub_pulpen = harga_pulpen * jumlah_pulpen\ntotal = sub_buku + sub_pulpen\n\nprint(\"Buku   :\", sub_buku)\nprint(\"Pulpen :\", sub_pulpen)\nprint(\"Total  :\", total)", "oj": "Buku   : 37500\nPulpen : 8000\nTotal  : 45500\n", "op": "Buku   : 37500\nPulpen : 8000\nTotal  : 45500\n"}, "2.1": {"t": "Konversi detik ke jam", "s": "Durasi video 3725 detik. Ubah menjadi format jam, menit, dan detik.", "l": ["1 jam = 3600 detik. jam = total / 3600.", "Sisa setelah jam diambil: total % 3600.", "menit = sisa / 60, detik = sisa % 60."], "java": "public class Main {\n    public static void main(String[] args) {\n        int total = 3725;\n        int jam = total / 3600;\n        int sisa = total % 3600;\n        int menit = sisa / 60;\n        int detik = sisa % 60;\n        System.out.println(jam + \" jam \" + menit + \" menit \" + detik + \" detik\");\n    }\n}", "python": "total = 3725\njam = total // 3600\nsisa = total % 3600\nmenit = sisa // 60\ndetik = sisa % 60\nprint(jam, \"jam\", menit, \"menit\", detik, \"detik\")", "oj": "1 jam 2 menit 5 detik\n", "op": "1 jam 2 menit 5 detik\n"}, "2.2": {"t": "Tabel perkalian", "s": "Cetak tabel perkalian 7 dari 7 × 1 sampai 7 × 5.", "l": ["Yang berubah setiap baris hanya pengalinya: 1 sampai 5.", "Gunakan for dengan i dari 1 sampai 5.", "Isi badan: cetak 7 x i = 7 * i."], "java": "public class Main {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 5; i++) {\n            System.out.println(\"7 x \" + i + \" = \" + (7 * i));\n        }\n    }\n}", "python": "for i in range(1, 6):\n    print(\"7 x\", i, \"=\", 7 * i)", "oj": "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n", "op": "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n"}, "2.3": {"t": "Segitiga angka", "s": "Cetak segitiga angka 4 baris. Baris ke-b berisi angka 1 sampai b.", "l": ["Loop luar: baris b = 1..4.", "Loop dalam: k = 1..b, cetak k dan spasi tanpa pindah baris.", "Setelah loop dalam selesai, pindah baris."], "java": "public class Main {\n    public static void main(String[] args) {\n        for (int b = 1; b <= 4; b++) {\n            for (int k = 1; k <= b; k++) {\n                System.out.print(k + \" \");\n            }\n            System.out.println();\n        }\n    }\n}", "python": "for b in range(1, 5):\n    for k in range(1, b + 1):\n        print(k, end=\" \")\n    print()", "oj": "1 \n1 2 \n1 2 3 \n1 2 3 4 \n", "op": "1 \n1 2 \n1 2 3 \n1 2 3 4 \n"}, "3.0": {"t": "Kalkulator BMI", "s": "Buat method bmi(berat, tinggiCm) yang mengembalikan BMI (berat / tinggi² dalam meter), dibulatkan 1 angka di belakang koma. Hitung untuk 2 orang.", "l": ["Parameter: berat (kg) dan tinggi (cm).", "Ubah tinggi ke meter: tinggi / 100.0.", "return hasilnya, lalu panggil method dua kali dengan data berbeda."], "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Andi: \" + bmi(60, 170));\n        System.out.println(\"Bela: \" + bmi(48, 155));\n    }\n\n    public static double bmi(int berat, int tinggiCm) {\n        double m = tinggiCm / 100.0;\n        double hasil = berat / (m * m);\n        return Math.round(hasil * 10) / 10.0;\n    }\n}", "python": "def bmi(berat, tinggi_cm):\n    m = tinggi_cm / 100\n    hasil = berat / (m * m)\n    return round(hasil, 1)\n\nprint(\"Andi:\", bmi(60, 170))\nprint(\"Bela:\", bmi(48, 155))", "oj": "Andi: 20.8\nBela: 20.0\n", "op": "Andi: 20.8\nBela: 20.0\n"}, "3.1": {"t": "Pembuat inisial", "s": "Dari nama lengkap \"Budi Santoso\", buat inisial \"B.S.\" dan hitung jumlah hurufnya tanpa spasi.", "l": ["Cari posisi spasi dengan indexOf / find.", "Huruf pertama ada di indeks 0, huruf kedua tepat setelah spasi.", "Jumlah huruf = panjang − 1 (satu spasi)."], "java": "public class Main {\n    public static void main(String[] args) {\n        String nama = \"Budi Santoso\";\n        int spasi = nama.indexOf(\" \");\n        String inisial = nama.charAt(0) + \".\" + nama.charAt(spasi + 1) + \".\";\n        System.out.println(\"Inisial: \" + inisial);\n        System.out.println(\"Jumlah huruf: \" + (nama.length() - 1));\n    }\n}", "python": "nama = \"Budi Santoso\"\nspasi = nama.find(\" \")\ninisial = nama[0] + \".\" + nama[spasi + 1] + \".\"\nprint(\"Inisial:\", inisial)\nprint(\"Jumlah huruf:\", len(nama) - 1)", "oj": "Inisial: B.S.\nJumlah huruf: 11\n", "op": "Inisial: B.S.\nJumlah huruf: 11\n"}, "3.2": {"t": "Kalkulator umur", "s": "Tanyakan tahun lahir pengguna, lalu cetak umurnya di tahun 2026. (Contoh input: 2008)", "l": ["Tampilkan pertanyaan dulu.", "Baca input sebagai bilangan bulat.", "umur = 2026 − tahunLahir."], "java": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner console = new Scanner(System.in);\n        System.out.print(\"Tahun lahir: \");\n        int tahun = console.nextInt();\n        int umur = 2026 - tahun;\n        System.out.println(\"Umurmu \" + umur + \" tahun\");\n    }\n}", "python": "tahun = int(input(\"Tahun lahir: \"))\numur = 2026 - tahun\nprint(\"Umurmu\", umur, \"tahun\")", "inp": "2008\n", "oj": "Tahun lahir: Umurmu 18 tahun\n", "op": "Tahun lahir: Umurmu 18 tahun\n"}, "4.0": {"t": "Konversi nilai ke huruf", "s": "Ubah nilai 95, 82, 74, dan 50 menjadi huruf: A (≥ 90), B (≥ 80), C (≥ 70), selain itu D.", "l": ["Buat method huruf(nilai) berisi rantai if / else if / else.", "Urutkan dari syarat paling tinggi.", "Panggil untuk setiap nilai."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] nilai = {95, 82, 74, 50};\n        for (int n : nilai) {\n            System.out.println(n + \" -> \" + huruf(n));\n        }\n    }\n\n    public static String huruf(int n) {\n        if (n >= 90) {\n            return \"A\";\n        } else if (n >= 80) {\n            return \"B\";\n        } else if (n >= 70) {\n            return \"C\";\n        } else {\n            return \"D\";\n        }\n    }\n}", "python": "def huruf(n):\n    if n >= 90:\n        return \"A\"\n    elif n >= 80:\n        return \"B\"\n    elif n >= 70:\n        return \"C\"\n    else:\n        return \"D\"\n\nfor n in [95, 82, 74, 50]:\n    print(n, \"->\", huruf(n))", "oj": "95 -> A\n82 -> B\n74 -> C\n50 -> D\n", "op": "95 -> A\n82 -> B\n74 -> C\n50 -> D\n"}, "4.1": {"t": "Statistik nilai kelas", "s": "Dari nilai 78, 92, 65, 88, 70, hitung total, rata-rata (bilangan bulat), dan nilai tertinggi.", "l": ["Siapkan total = 0 dan maks = elemen pertama.", "Dalam loop: total += nilai, dan perbarui maks jika lebih besar.", "rata-rata = total / banyak data."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] nilai = {78, 92, 65, 88, 70};\n        int total = 0;\n        int maks = nilai[0];\n        for (int n : nilai) {\n            total += n;\n            if (n > maks) {\n                maks = n;\n            }\n        }\n        System.out.println(\"Total     : \" + total);\n        System.out.println(\"Rata-rata : \" + total / nilai.length);\n        System.out.println(\"Tertinggi : \" + maks);\n    }\n}", "python": "nilai = [78, 92, 65, 88, 70]\ntotal = 0\nmaks = nilai[0]\nfor n in nilai:\n    total += n\n    if n > maks:\n        maks = n\nprint(\"Total     :\", total)\nprint(\"Rata-rata :\", total // len(nilai))\nprint(\"Tertinggi :\", maks)", "oj": "Total     : 393\nRata-rata : 78\nTertinggi : 92\n", "op": "Total     : 393\nRata-rata : 78\nTertinggi : 92\n"}, "5.0": {"t": "Target tabungan", "s": "Tabungan awal 100000 bertambah 10% setiap tahun (pecahan rupiah dibuang). Berapa tahun sampai tabungan mencapai minimal 200000?", "l": ["Kalimat \"sampai mencapai\" → while (saldo < target).", "Di badan loop: saldo += saldo / 10, tahun++.", "Cetak saldo setiap tahun supaya mudah dilacak."], "java": "public class Main {\n    public static void main(String[] args) {\n        int saldo = 100000;\n        int tahun = 0;\n        while (saldo < 200000) {\n            saldo += saldo / 10;\n            tahun++;\n            System.out.println(\"Tahun \" + tahun + \": \" + saldo);\n        }\n        System.out.println(\"Butuh \" + tahun + \" tahun\");\n    }\n}", "python": "saldo = 100000\ntahun = 0\nwhile saldo < 200000:\n    saldo += saldo // 10\n    tahun += 1\n    print(\"Tahun\", str(tahun) + \":\", saldo)\nprint(\"Butuh\", tahun, \"tahun\")", "oj": "Tahun 1: 110000\nTahun 2: 121000\nTahun 3: 133100\nTahun 4: 146410\nTahun 5: 161051\nTahun 6: 177156\nTahun 7: 194871\nTahun 8: 214358\nButuh 8 tahun\n", "op": "Tahun 1: 110000\nTahun 2: 121000\nTahun 3: 133100\nTahun 4: 146410\nTahun 5: 161051\nTahun 6: 177156\nTahun 7: 194871\nTahun 8: 214358\nButuh 8 tahun\n"}, "5.1": {"t": "Pengecek tahun kabisat", "s": "Tahun kabisat: habis dibagi 4 dan tidak habis dibagi 100, atau habis dibagi 400. Cek tahun 1900, 2000, 2024, dan 2025.", "l": ["\"habis dibagi 4\" → t % 4 == 0.", "\"dan tidak\" → && !(...) / and not.", "\"atau\" → || / or. Gunakan kurung agar jelas."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] daftar = {1900, 2000, 2024, 2025};\n        for (int t : daftar) {\n            boolean kabisat = (t % 4 == 0 && t % 100 != 0) || t % 400 == 0;\n            System.out.println(t + \" kabisat? \" + kabisat);\n        }\n    }\n}", "python": "for t in [1900, 2000, 2024, 2025]:\n    kabisat = (t % 4 == 0 and t % 100 != 0) or t % 400 == 0\n    print(t, \"kabisat?\", kabisat)", "oj": "1900 kabisat? false\n2000 kabisat? true\n2024 kabisat? true\n2025 kabisat? false\n", "op": "1900 kabisat? False\n2000 kabisat? True\n2024 kabisat? True\n2025 kabisat? False\n"}, "5.2": {"t": "Cetak daftar rapi", "s": "Cetak angka 1 sampai 5 dalam format [1, 2, 3, 4, 5], tanpa koma berlebih di akhir.", "l": ["Cetak \"[\" dan angka pertama di luar loop.", "Loop dari 2: cetak \", \" lalu angkanya.", "Tutup dengan \"]\"."], "java": "public class Main {\n    public static void main(String[] args) {\n        int n = 5;\n        System.out.print(\"[1\");\n        for (int i = 2; i <= n; i++) {\n            System.out.print(\", \" + i);\n        }\n        System.out.println(\"]\");\n    }\n}", "python": "n = 5\nprint(\"[1\", end=\"\")\nfor i in range(2, n + 1):\n    print(\", \" + str(i), end=\"\")\nprint(\"]\")", "oj": "[1, 2, 3, 4, 5]\n", "op": "[1, 2, 3, 4, 5]\n"}, "6.0": {"t": "Rapor dari file", "s": "File nilai.txt berisi nama dan dua nilai per baris. Baca filenya dan cetak rata-rata setiap siswa.", "l": ["Buka file, lalu ulangi selama masih ada baris.", "Pecah baris menjadi token: nama, nilai1, nilai2.", "Ubah token angka ke int sebelum dijumlah."], "java": "import java.io.File;\nimport java.io.FileNotFoundException;\nimport java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) throws FileNotFoundException {\n        Scanner input = new Scanner(new File(\"nilai.txt\"));\n        while (input.hasNextLine()) {\n            String[] t = input.nextLine().split(\" \");\n            int a = Integer.parseInt(t[1]);\n            int b = Integer.parseInt(t[2]);\n            System.out.println(t[0] + \": \" + (a + b) / 2);\n        }\n    }\n}", "python": "with open(\"nilai.txt\") as f:\n    for line in f:\n        t = line.split()\n        a = int(t[1])\n        b = int(t[2])\n        print(t[0] + \":\", (a + b) // 2)", "file": ["nilai.txt", "Budi 80 90\nSari 75 85\nTono 60 71\n"], "oj": "Budi: 85\nSari: 80\nTono: 65\n", "op": "Budi: 85\nSari: 80\nTono: 65\n"}, "6.1": {"t": "Penjumlah data kotor", "s": "Data dari formulir: \"12\", \"abc\", \"7\", \"3x\", \"20\". Jumlahkan yang berupa angka dan laporkan yang tidak valid.", "l": ["Coba ubah setiap teks menjadi int di dalam try.", "Jika gagal, catch menangkap error lalu cetak peringatan.", "Hanya yang berhasil ditambahkan ke total."], "java": "public class Main {\n    public static void main(String[] args) {\n        String[] data = {\"12\", \"abc\", \"7\", \"3x\", \"20\"};\n        int total = 0;\n        for (String s : data) {\n            try {\n                total += Integer.parseInt(s);\n            } catch (NumberFormatException e) {\n                System.out.println(\"Lewati: \" + s);\n            }\n        }\n        System.out.println(\"Total: \" + total);\n    }\n}", "python": "data = [\"12\", \"abc\", \"7\", \"3x\", \"20\"]\ntotal = 0\nfor s in data:\n    try:\n        total += int(s)\n    except ValueError:\n        print(\"Lewati:\", s)\nprint(\"Total:\", total)", "oj": "Lewati: abc\nLewati: 3x\nTotal: 39\n", "op": "Lewati: abc\nLewati: 3x\nTotal: 39\n"}, "7.0": {"t": "Suhu seminggu", "s": "Simpan suhu 7 hari (31, 29, 33, 30, 28, 32, 34) dalam array. Cetak suhu hari pertama, hari ketiga, dan hari terakhir.", "l": ["Hari ke-k ada di indeks k − 1.", "Hari terakhir = indeks panjang − 1.", "Jangan menulis 7 langsung, pakai length / len."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] suhu = {31, 29, 33, 30, 28, 32, 34};\n        System.out.println(\"Hari 1  : \" + suhu[0]);\n        System.out.println(\"Hari 3  : \" + suhu[2]);\n        System.out.println(\"Terakhir: \" + suhu[suhu.length - 1]);\n    }\n}", "python": "suhu = [31, 29, 33, 30, 28, 32, 34]\nprint(\"Hari 1  :\", suhu[0])\nprint(\"Hari 3  :\", suhu[2])\nprint(\"Terakhir:\", suhu[len(suhu) - 1])", "oj": "Hari 1  : 31\nHari 3  : 33\nTerakhir: 34\n", "op": "Hari 1  : 31\nHari 3  : 33\nTerakhir: 34\n"}, "7.1": {"t": "Di atas rata-rata", "s": "Dari nilai 70, 85, 60, 90, 75, hitung rata-ratanya, lalu cetak nilai yang di atas rata-rata beserta indeksnya.", "l": ["Traversal pertama: jumlahkan untuk rata-rata.", "Traversal kedua: bandingkan setiap a[i] dengan rata-rata.", "Pakai i < length agar tidak kelewatan."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] a = {70, 85, 60, 90, 75};\n        int total = 0;\n        for (int i = 0; i < a.length; i++) {\n            total += a[i];\n        }\n        int rata = total / a.length;\n        System.out.println(\"Rata-rata: \" + rata);\n        for (int i = 0; i < a.length; i++) {\n            if (a[i] > rata) {\n                System.out.println(\"a[\" + i + \"] = \" + a[i]);\n            }\n        }\n    }\n}", "python": "a = [70, 85, 60, 90, 75]\ntotal = 0\nfor i in range(len(a)):\n    total += a[i]\nrata = total // len(a)\nprint(\"Rata-rata:\", rata)\nfor i in range(len(a)):\n    if a[i] > rata:\n        print(\"a[\" + str(i) + \"] =\", a[i])", "oj": "Rata-rata: 76\na[1] = 85\na[3] = 90\n", "op": "Rata-rata: 76\na[1] = 85\na[3] = 90\n"}, "7.2": {"t": "Diskon yang menular", "s": "Buat method diskon(harga) yang memotong setiap harga 50% langsung di array. Buktikan array asli ikut berubah, sedangkan salinannya tidak.", "l": ["Buat salinan dulu: Arrays.copyOf / list.copy().", "Kirim array asli ke method. Method menerima alamat yang sama.", "Cetak keduanya untuk membandingkan."], "java": "import java.util.Arrays;\n\npublic class Main {\n    public static void main(String[] args) {\n        int[] harga = {10000, 20000, 30000};\n        int[] cadangan = Arrays.copyOf(harga, harga.length);\n        diskon(harga);\n        System.out.println(\"harga    = \" + Arrays.toString(harga));\n        System.out.println(\"cadangan = \" + Arrays.toString(cadangan));\n    }\n\n    public static void diskon(int[] a) {\n        for (int i = 0; i < a.length; i++) {\n            a[i] = a[i] / 2;\n        }\n    }\n}", "python": "def diskon(a):\n    for i in range(len(a)):\n        a[i] = a[i] // 2\n\nharga = [10000, 20000, 30000]\ncadangan = harga.copy()\ndiskon(harga)\nprint(\"harga    =\", harga)\nprint(\"cadangan =\", cadangan)", "oj": "harga    = [5000, 10000, 15000]\ncadangan = [10000, 20000, 30000]\n", "op": "harga    = [5000, 10000, 15000]\ncadangan = [10000, 20000, 30000]\n"}, "8.0": {"t": "Rak buku", "s": "Buat kelas Buku dengan field judul dan halaman. Buat dua objek buku dan cetak informasinya lewat method info().", "l": ["Kata benda \"buku\" → kelas Buku. Sifatnya (judul, halaman) → field.", "Konstruktor mengisi field.", "Setiap objek punya isi field sendiri."], "java": "public class Main {\n    public static void main(String[] args) {\n        Buku a = new Buku(\"Laskar Pelangi\", 529);\n        Buku b = new Buku(\"Bumi\", 440);\n        System.out.println(a.info());\n        System.out.println(b.info());\n    }\n}\n\nclass Buku {\n    private String judul;\n    private int halaman;\n\n    public Buku(String judul, int halaman) {\n        this.judul = judul;\n        this.halaman = halaman;\n    }\n\n    public String info() {\n        return judul + \" (\" + halaman + \" hlm)\";\n    }\n}", "python": "class Buku:\n    def __init__(self, judul, halaman):\n        self.judul = judul\n        self.halaman = halaman\n\n    def info(self):\n        return self.judul + \" (\" + str(self.halaman) + \" hlm)\"\n\na = Buku(\"Laskar Pelangi\", 529)\nb = Buku(\"Bumi\", 440)\nprint(a.info())\nprint(b.info())", "oj": "Laskar Pelangi (529 hlm)\nBumi (440 hlm)\n", "op": "Laskar Pelangi (529 hlm)\nBumi (440 hlm)\n"}, "8.1": {"t": "Rekening bank aman", "s": "Buat kelas Rekening. setor dan tarik harus menolak jumlah tidak valid (negatif atau melebihi saldo). Saldo hanya bisa dibaca lewat getSaldo.", "l": ["Field saldo dibuat private / _saldo.", "Di dalam setor & tarik, cek dulu syaratnya dengan if.", "Kembalikan true/false agar pemanggil tahu berhasil atau tidak."], "java": "public class Main {\n    public static void main(String[] args) {\n        Rekening r = new Rekening();\n        System.out.println(r.setor(50000));\n        System.out.println(r.tarik(80000));\n        System.out.println(r.tarik(20000));\n        System.out.println(\"Saldo: \" + r.getSaldo());\n    }\n}\n\nclass Rekening {\n    private int saldo;\n\n    public boolean setor(int x) {\n        if (x <= 0) return false;\n        saldo += x;\n        return true;\n    }\n\n    public boolean tarik(int x) {\n        if (x <= 0 || x > saldo) return false;\n        saldo -= x;\n        return true;\n    }\n\n    public int getSaldo() {\n        return saldo;\n    }\n}", "python": "class Rekening:\n    def __init__(self):\n        self._saldo = 0\n\n    def setor(self, x):\n        if x <= 0:\n            return False\n        self._saldo += x\n        return True\n\n    def tarik(self, x):\n        if x <= 0 or x > self._saldo:\n            return False\n        self._saldo -= x\n        return True\n\n    def get_saldo(self):\n        return self._saldo\n\nr = Rekening()\nprint(r.setor(50000))\nprint(r.tarik(80000))\nprint(r.tarik(20000))\nprint(\"Saldo:\", r.get_saldo())", "oj": "true\nfalse\ntrue\nSaldo: 30000\n", "op": "True\nFalse\nTrue\nSaldo: 30000\n"}, "9.0": {"t": "Kebun binatang", "s": "Kelas Hewan punya method suara(). Kucing dan Anjing mewarisi Hewan dan meng-override suara(). Cetak suara semua hewan dalam satu daftar.", "l": ["\"Kucing adalah sejenis hewan\" → Kucing extends Hewan.", "Override: tulis ulang method dengan nama yang sama.", "Satu loop memanggil suara(); versi yang jalan ditentukan objeknya."], "java": "public class Main {\n    public static void main(String[] args) {\n        Hewan[] kebun = {new Kucing(\"Oyen\"), new Anjing(\"Doggo\"), new Hewan(\"Ikan\")};\n        for (Hewan h : kebun) {\n            System.out.println(h.nama + \": \" + h.suara());\n        }\n    }\n}\n\nclass Hewan {\n    String nama;\n    Hewan(String nama) { this.nama = nama; }\n    String suara() { return \"...\"; }\n}\n\nclass Kucing extends Hewan {\n    Kucing(String nama) { super(nama); }\n    @Override\n    String suara() { return \"Meong\"; }\n}\n\nclass Anjing extends Hewan {\n    Anjing(String nama) { super(nama); }\n    @Override\n    String suara() { return \"Guk guk\"; }\n}", "python": "class Hewan:\n    def __init__(self, nama):\n        self.nama = nama\n    def suara(self):\n        return \"...\"\n\nclass Kucing(Hewan):\n    def suara(self):\n        return \"Meong\"\n\nclass Anjing(Hewan):\n    def suara(self):\n        return \"Guk guk\"\n\nkebun = [Kucing(\"Oyen\"), Anjing(\"Doggo\"), Hewan(\"Ikan\")]\nfor h in kebun:\n    print(h.nama + \":\", h.suara())", "oj": "Oyen: Meong\nDoggo: Guk guk\nIkan: ...\n", "op": "Oyen: Meong\nDoggo: Guk guk\nIkan: ...\n"}, "9.1": {"t": "Kalkulator luas bangun", "s": "Interface Bentuk menjanjikan method luas(). Persegi, PersegiPanjang, dan Segitiga menepatinya. Hitung total luas semua bangun.", "l": ["Tulis interface Bentuk dengan satu method luas().", "Setiap kelas implements Bentuk dan menulis rumusnya sendiri.", "Simpan semuanya dalam satu array bertipe Bentuk."], "java": "public class Main {\n    public static void main(String[] args) {\n        Bentuk[] daftar = {new Persegi(4), new PersegiPanjang(3, 5), new Segitiga(6, 4)};\n        int total = 0;\n        for (Bentuk b : daftar) {\n            System.out.println(b.getClass().getSimpleName() + \": \" + b.luas());\n            total += b.luas();\n        }\n        System.out.println(\"Total: \" + total);\n    }\n}\n\ninterface Bentuk {\n    int luas();\n}\n\nclass Persegi implements Bentuk {\n    int s;\n    Persegi(int s) { this.s = s; }\n    public int luas() { return s * s; }\n}\n\nclass PersegiPanjang implements Bentuk {\n    int p, l;\n    PersegiPanjang(int p, int l) { this.p = p; this.l = l; }\n    public int luas() { return p * l; }\n}\n\nclass Segitiga implements Bentuk {\n    int a, t;\n    Segitiga(int a, int t) { this.a = a; this.t = t; }\n    public int luas() { return a * t / 2; }\n}", "python": "from abc import ABC, abstractmethod\n\nclass Bentuk(ABC):\n    @abstractmethod\n    def luas(self): ...\n\nclass Persegi(Bentuk):\n    def __init__(self, s): self.s = s\n    def luas(self): return self.s * self.s\n\nclass PersegiPanjang(Bentuk):\n    def __init__(self, p, l): self.p, self.l = p, l\n    def luas(self): return self.p * self.l\n\nclass Segitiga(Bentuk):\n    def __init__(self, a, t): self.a, self.t = a, t\n    def luas(self): return self.a * self.t // 2\n\ndaftar = [Persegi(4), PersegiPanjang(3, 5), Segitiga(6, 4)]\ntotal = 0\nfor b in daftar:\n    print(type(b).__name__ + \":\", b.luas())\n    total += b.luas()\nprint(\"Total:\", total)", "oj": "Persegi: 16\nPersegiPanjang: 15\nSegitiga: 12\nTotal: 43\n", "op": "Persegi: 16\nPersegiPanjang: 15\nSegitiga: 12\nTotal: 43\n"}, "10.0": {"t": "Daftar belanja", "s": "Mulai dari daftar kosong. Tambahkan beras, telur, susu. Sisipkan gula di posisi 1. Hapus telur. Ganti susu menjadi teh. Cetak hasil setiap langkah.", "l": ["\"tambahkan\" → add / append.", "\"sisipkan di posisi\" → add(i, x) / insert(i, x).", "\"hapus\" → remove / remove(x). \"ganti\" → set / L[i] = x."], "java": "import java.util.ArrayList;\n\npublic class Main {\n    public static void main(String[] args) {\n        ArrayList<String> belanja = new ArrayList<>();\n        belanja.add(\"beras\");\n        belanja.add(\"telur\");\n        belanja.add(\"susu\");\n        System.out.println(belanja);\n        belanja.add(1, \"gula\");\n        System.out.println(belanja);\n        belanja.remove(\"telur\");\n        System.out.println(belanja);\n        belanja.set(belanja.indexOf(\"susu\"), \"teh\");\n        System.out.println(belanja);\n    }\n}", "python": "belanja = []\nbelanja.append(\"beras\")\nbelanja.append(\"telur\")\nbelanja.append(\"susu\")\nprint(belanja)\nbelanja.insert(1, \"gula\")\nprint(belanja)\nbelanja.remove(\"telur\")\nprint(belanja)\nbelanja[belanja.index(\"susu\")] = \"teh\"\nprint(belanja)", "oj": "[beras, telur, susu]\n[beras, gula, telur, susu]\n[beras, gula, susu]\n[beras, gula, teh]\n", "op": "['beras', 'telur', 'susu']\n['beras', 'gula', 'telur', 'susu']\n['beras', 'gula', 'susu']\n['beras', 'gula', 'teh']\n"}, "10.1": {"t": "Saring nama pendek", "s": "Dari daftar nama, hapus semua nama yang kurang dari 4 huruf. Lakukan langsung di list yang sama.", "l": ["Hapus sambil berjalan MUNDUR agar tidak ada yang terlewat.", "i mulai dari size − 1 sampai 0.", "Syarat hapus: panjang nama < 4."], "java": "import java.util.ArrayList;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<String> nama = new ArrayList<>(List.of(\"Ani\", \"Budi\", \"Eko\", \"Ida\", \"Sari\", \"Tono\"));\n        for (int i = nama.size() - 1; i >= 0; i--) {\n            if (nama.get(i).length() < 4) {\n                nama.remove(i);\n            }\n        }\n        System.out.println(nama);\n    }\n}", "python": "nama = [\"Ani\", \"Budi\", \"Eko\", \"Ida\", \"Sari\", \"Tono\"]\nfor i in range(len(nama) - 1, -1, -1):\n    if len(nama[i]) < 4:\n        nama.pop(i)\nprint(nama)", "oj": "[Budi, Sari, Tono]\n", "op": "['Budi', 'Sari', 'Tono']\n"}, "11.0": {"t": "Kata unik dalam kalimat", "s": "Dari kalimat \"saya suka kopi dan saya suka teh\", cetak kata-kata unik secara terurut dan jumlahnya.", "l": ["Pecah kalimat menjadi kata dengan split.", "Masukkan semua kata ke set: duplikat otomatis dibuang.", "Pakai TreeSet / sorted() agar urutannya pasti."], "java": "import java.util.Set;\nimport java.util.TreeSet;\n\npublic class Main {\n    public static void main(String[] args) {\n        String kalimat = \"saya suka kopi dan saya suka teh\";\n        Set<String> unik = new TreeSet<>();\n        for (String kata : kalimat.split(\" \")) {\n            unik.add(kata);\n        }\n        System.out.println(unik);\n        System.out.println(\"Jumlah kata unik: \" + unik.size());\n    }\n}", "python": "kalimat = \"saya suka kopi dan saya suka teh\"\nunik = set(kalimat.split())\nprint(sorted(unik))\nprint(\"Jumlah kata unik:\", len(unik))", "oj": "[dan, kopi, saya, suka, teh]\nJumlah kata unik: 5\n", "op": "['dan', 'kopi', 'saya', 'suka', 'teh']\nJumlah kata unik: 5\n"}, "11.1": {"t": "Hitung suara voting", "s": "Hasil voting ketua kelas: Ani, Budi, Ani, Cici, Budi, Ani. Hitung suara setiap calon dan tentukan pemenangnya.", "l": ["\"berapa kali setiap …\" → map dari nama ke jumlah.", "m[nama] = (nilai lama atau 0) + 1.", "Telusuri map untuk mencari jumlah terbesar."], "java": "import java.util.Map;\nimport java.util.TreeMap;\n\npublic class Main {\n    public static void main(String[] args) {\n        String[] suara = {\"Ani\", \"Budi\", \"Ani\", \"Cici\", \"Budi\", \"Ani\"};\n        Map<String, Integer> hitung = new TreeMap<>();\n        for (String s : suara) {\n            hitung.put(s, hitung.getOrDefault(s, 0) + 1);\n        }\n        System.out.println(hitung);\n        String juara = \"\";\n        int maks = 0;\n        for (String nama : hitung.keySet()) {\n            if (hitung.get(nama) > maks) {\n                maks = hitung.get(nama);\n                juara = nama;\n            }\n        }\n        System.out.println(\"Pemenang: \" + juara + \" (\" + maks + \" suara)\");\n    }\n}", "python": "suara = [\"Ani\", \"Budi\", \"Ani\", \"Cici\", \"Budi\", \"Ani\"]\nhitung = {}\nfor s in suara:\n    hitung[s] = hitung.get(s, 0) + 1\nprint(dict(sorted(hitung.items())))\njuara = \"\"\nmaks = 0\nfor nama in sorted(hitung):\n    if hitung[nama] > maks:\n        maks = hitung[nama]\n        juara = nama\nprint(\"Pemenang:\", juara, \"(\" + str(maks), \"suara)\")", "oj": "{Ani=3, Budi=2, Cici=1}\nPemenang: Ani (3 suara)\n", "op": "{'Ani': 3, 'Budi': 2, 'Cici': 1}\nPemenang: Ani (3 suara)\n"}, "12.0": {"t": "Pangkat rekursif", "s": "Tulis method pangkat(a, b) secara rekursif tanpa loop dan tanpa Math.pow / **. Hitung 2⁵ dan 3⁴.", "l": ["Base case: a pangkat 0 = 1.", "Recursive case: a^b = a × a^(b − 1).", "Setiap panggilan mengurangi b, jadi pasti mencapai 0."], "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"2^5 = \" + pangkat(2, 5));\n        System.out.println(\"3^4 = \" + pangkat(3, 4));\n    }\n\n    public static int pangkat(int a, int b) {\n        if (b == 0) {\n            return 1;\n        }\n        return a * pangkat(a, b - 1);\n    }\n}", "python": "def pangkat(a, b):\n    if b == 0:\n        return 1\n    return a * pangkat(a, b - 1)\n\nprint(\"2^5 =\", pangkat(2, 5))\nprint(\"3^4 =\", pangkat(3, 4))", "oj": "2^5 = 32\n3^4 = 81\n", "op": "2^5 = 32\n3^4 = 81\n"}, "12.1": {"t": "Pengubah ke biner", "s": "Tulis method rekursif biner(n) yang mengembalikan bentuk biner dari n sebagai teks. Uji dengan 13 dan 6.", "l": ["n % 2 = bit terakhir, n / 2 = bit-bit sisanya.", "Base case: n < 2 → teksnya n itu sendiri.", "Hasil = biner(n / 2) + bit terakhir (sisanya ditulis di depan)."], "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"13 = \" + biner(13));\n        System.out.println(\"6  = \" + biner(6));\n    }\n\n    public static String biner(int n) {\n        if (n < 2) {\n            return \"\" + n;\n        }\n        return biner(n / 2) + (n % 2);\n    }\n}", "python": "def biner(n):\n    if n < 2:\n        return str(n)\n    return biner(n // 2) + str(n % 2)\n\nprint(\"13 =\", biner(13))\nprint(\"6  =\", biner(6))", "oj": "13 = 1101\n6  = 110\n", "op": "13 = 1101\n6  = 110\n"}, "13.0": {"t": "Cari nomor absen", "s": "Daftar nomor terurut: 3, 8, 15, 21, 30, 42, 57. Cari nomor 42 dengan binary search dan cetak setiap tebakan tengahnya.", "l": ["lo = 0, hi = panjang − 1.", "Selama lo <= hi: hitung mid, bandingkan a[mid] dengan target.", "Terlalu kecil → lo = mid + 1. Terlalu besar → hi = mid − 1."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] a = {3, 8, 15, 21, 30, 42, 57};\n        System.out.println(\"Ketemu di indeks \" + cari(a, 42));\n    }\n\n    public static int cari(int[] a, int target) {\n        int lo = 0, hi = a.length - 1;\n        while (lo <= hi) {\n            int mid = (lo + hi) / 2;\n            System.out.println(\"cek a[\" + mid + \"] = \" + a[mid]);\n            if (a[mid] == target) return mid;\n            else if (a[mid] < target) lo = mid + 1;\n            else hi = mid - 1;\n        }\n        return -1;\n    }\n}", "python": "def cari(a, target):\n    lo, hi = 0, len(a) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        print(\"cek a[\" + str(mid) + \"] =\", a[mid])\n        if a[mid] == target: return mid\n        elif a[mid] < target: lo = mid + 1\n        else: hi = mid - 1\n    return -1\n\na = [3, 8, 15, 21, 30, 42, 57]\nprint(\"Ketemu di indeks\", cari(a, 42))", "oj": "cek a[3] = 21\ncek a[5] = 42\nKetemu di indeks 5\n", "op": "cek a[3] = 21\ncek a[5] = 42\nKetemu di indeks 5\n"}, "13.1": {"t": "Urutkan tinggi badan", "s": "Urutkan tinggi badan 165, 150, 172, 158 dengan selection sort dan cetak isi array setelah setiap putaran.", "l": ["Putaran i: cari indeks minimum dari i sampai akhir.", "Tukar minimum ke posisi i.", "Cetak array di akhir setiap putaran."], "java": "import java.util.Arrays;\n\npublic class Main {\n    public static void main(String[] args) {\n        int[] a = {165, 150, 172, 158};\n        for (int i = 0; i < a.length - 1; i++) {\n            int min = i;\n            for (int j = i + 1; j < a.length; j++) {\n                if (a[j] < a[min]) min = j;\n            }\n            int tmp = a[i];\n            a[i] = a[min];\n            a[min] = tmp;\n            System.out.println(\"Putaran \" + (i + 1) + \": \" + Arrays.toString(a));\n        }\n    }\n}", "python": "a = [165, 150, 172, 158]\nfor i in range(len(a) - 1):\n    m = i\n    for j in range(i + 1, len(a)):\n        if a[j] < a[m]: m = j\n    a[i], a[m] = a[m], a[i]\n    print(\"Putaran\", str(i + 1) + \":\", a)", "oj": "Putaran 1: [150, 165, 172, 158]\nPutaran 2: [150, 158, 172, 165]\nPutaran 3: [150, 158, 165, 172]\n", "op": "Putaran 1: [150, 165, 172, 158]\nPutaran 2: [150, 158, 172, 165]\nPutaran 3: [150, 158, 165, 172]\n"}, "13.2": {"t": "Lomba kecepatan algoritma", "s": "Hitung berapa kali langkah inti dijalankan oleh tiga pola (satu loop, loop bersarang, dan bagi dua) untuk n = 8 dan n = 1024.", "l": ["Satu loop 1..n → tambah penghitung n kali.", "Loop bersarang → n × n kali.", "Bagi dua: while (n > 1) n /= 2 → sekitar log₂ n kali."], "java": "public class Main {\n    public static void main(String[] args) {\n        for (int n : new int[]{8, 1024}) {\n            System.out.println(\"n=\" + n + \" linear=\" + linear(n)\n                + \" kuadrat=\" + kuadrat(n) + \" log=\" + logaritma(n));\n        }\n    }\n\n    static int linear(int n) {\n        int c = 0;\n        for (int i = 0; i < n; i++) c++;\n        return c;\n    }\n\n    static int kuadrat(int n) {\n        int c = 0;\n        for (int i = 0; i < n; i++)\n            for (int j = 0; j < n; j++) c++;\n        return c;\n    }\n\n    static int logaritma(int n) {\n        int c = 0;\n        while (n > 1) { n /= 2; c++; }\n        return c;\n    }\n}", "python": "def linear(n):\n    c = 0\n    for i in range(n): c += 1\n    return c\n\ndef kuadrat(n):\n    c = 0\n    for i in range(n):\n        for j in range(n): c += 1\n    return c\n\ndef logaritma(n):\n    c = 0\n    while n > 1:\n        n //= 2\n        c += 1\n    return c\n\nfor n in [8, 1024]:\n    print(f\"n={n} linear={linear(n)} kuadrat={kuadrat(n)} log={logaritma(n)}\")", "oj": "n=8 linear=8 kuadrat=64 log=3\nn=1024 linear=1024 kuadrat=1048576 log=10\n", "op": "n=8 linear=8 kuadrat=64 log=3\nn=1024 linear=1024 kuadrat=1048576 log=10\n"}, "14.0": {"t": "Pengecek kurung", "s": "Periksa apakah kurung dalam teks seimbang: \"(a[b]{c})\", \"(]\", dan \"((x)\".", "l": ["Kurung buka → push ke stack.", "Kurung tutup → stack tidak boleh kosong, dan pop harus pasangannya.", "Di akhir, stack harus kosong."], "java": "import java.util.Stack;\n\npublic class Main {\n    public static void main(String[] args) {\n        for (String s : new String[]{\"(a[b]{c})\", \"(]\", \"((x)\"}) {\n            System.out.println(s + \" -> \" + seimbang(s));\n        }\n    }\n\n    static boolean seimbang(String s) {\n        Stack<Character> st = new Stack<>();\n        for (char c : s.toCharArray()) {\n            if (\"([{\".indexOf(c) >= 0) {\n                st.push(c);\n            } else if (\")]}\".indexOf(c) >= 0) {\n                if (st.isEmpty()) return false;\n                char buka = st.pop();\n                if (\"([{\".indexOf(buka) != \")]}\".indexOf(c)) return false;\n            }\n        }\n        return st.isEmpty();\n    }\n}", "python": "def seimbang(s):\n    st = []\n    for c in s:\n        if c in \"([{\":\n            st.append(c)\n        elif c in \")]}\":\n            if not st:\n                return False\n            buka = st.pop()\n            if \"([{\".index(buka) != \")]}\".index(c):\n                return False\n    return not st\n\nfor s in [\"(a[b]{c})\", \"(]\", \"((x)\"]:\n    print(s, \"->\", seimbang(s))", "oj": "(a[b]{c}) -> true\n(] -> false\n((x) -> false\n", "op": "(a[b]{c}) -> True\n(] -> False\n((x) -> False\n"}, "14.1": {"t": "Antrean loket", "s": "Empat orang datang berurutan: Ani, Budi, Cici, Dodi. Loket melayani satu per satu sesuai urutan datang. Cetak siapa yang dilayani dan sisa antrean.", "l": ["\"sesuai urutan datang\" → queue (FIFO).", "Masukkan semua nama di belakang antrean.", "Selama antrean tidak kosong: ambil dari depan, layani."], "java": "import java.util.LinkedList;\nimport java.util.Queue;\n\npublic class Main {\n    public static void main(String[] args) {\n        Queue<String> q = new LinkedList<>();\n        for (String n : new String[]{\"Ani\", \"Budi\", \"Cici\", \"Dodi\"}) {\n            q.add(n);\n        }\n        while (!q.isEmpty()) {\n            String orang = q.remove();\n            System.out.println(\"Melayani \" + orang + \", sisa \" + q);\n        }\n    }\n}", "python": "from collections import deque\n\nq = deque()\nfor n in [\"Ani\", \"Budi\", \"Cici\", \"Dodi\"]:\n    q.append(n)\nwhile q:\n    orang = q.popleft()\n    print(\"Melayani\", orang + \", sisa\", list(q))", "oj": "Melayani Ani, sisa [Budi, Cici, Dodi]\nMelayani Budi, sisa [Cici, Dodi]\nMelayani Cici, sisa [Dodi]\nMelayani Dodi, sisa []\n", "op": "Melayani Ani, sisa ['Budi', 'Cici', 'Dodi']\nMelayani Budi, sisa ['Cici', 'Dodi']\nMelayani Cici, sisa ['Dodi']\nMelayani Dodi, sisa []\n"}, "15.0": {"t": "ArrayList buatan sendiri", "s": "Buat kelas ArrayIntList dengan array internal berkapasitas 2. add(x) menggandakan kapasitas saat penuh. Tambahkan 5 angka dan cetak setiap kali kapasitas berubah.", "l": ["Field: data (array) dan size.", "Jika size == data.length → buat array 2× lebih besar, salin isi lama.", "Taruh nilai di data[size], lalu size++."], "java": "import java.util.Arrays;\n\npublic class Main {\n    public static void main(String[] args) {\n        ArrayIntList list = new ArrayIntList();\n        for (int x = 10; x <= 50; x += 10) {\n            list.add(x);\n        }\n        System.out.println(list);\n    }\n}\n\nclass ArrayIntList {\n    private int[] data = new int[2];\n    private int size = 0;\n\n    public void add(int value) {\n        if (size == data.length) {\n            data = Arrays.copyOf(data, data.length * 2);\n            System.out.println(\"Kapasitas naik menjadi \" + data.length);\n        }\n        data[size] = value;\n        size++;\n    }\n\n    public String toString() {\n        return Arrays.toString(Arrays.copyOf(data, size)) + \" size=\" + size + \" kapasitas=\" + data.length;\n    }\n}", "python": "class ArrayIntList:\n    def __init__(self):\n        self.data = [0] * 2\n        self.size = 0\n\n    def add(self, value):\n        if self.size == len(self.data):\n            self.data = self.data + [0] * len(self.data)\n            print(\"Kapasitas naik menjadi\", len(self.data))\n        self.data[self.size] = value\n        self.size += 1\n\n    def __str__(self):\n        return f\"{self.data[:self.size]} size={self.size} kapasitas={len(self.data)}\"\n\nlst = ArrayIntList()\nfor x in range(10, 51, 10):\n    lst.add(x)\nprint(lst)", "oj": "Kapasitas naik menjadi 4\nKapasitas naik menjadi 8\n[10, 20, 30, 40, 50] size=5 kapasitas=8\n", "op": "Kapasitas naik menjadi 4\nKapasitas naik menjadi 8\n[10, 20, 30, 40, 50] size=5 kapasitas=8\n"}, "15.1": {"t": "Akses aman", "s": "Tambahkan method get(index) yang melempar exception bila index di luar 0..size−1. Uji dengan indeks valid dan tidak valid.", "l": ["Precondition dicek di baris pertama method.", "Pesan exception menyebut indeks yang salah.", "Pemanggil memakai try / catch untuk menangkapnya."], "java": "public class Main {\n    public static void main(String[] args) {\n        int[] data = {7, 9, 4, 0, 0};\n        int size = 3;\n        for (int i : new int[]{1, 3, -1}) {\n            try {\n                System.out.println(\"get(\" + i + \") = \" + get(data, size, i));\n            } catch (IndexOutOfBoundsException e) {\n                System.out.println(\"Error: \" + e.getMessage());\n            }\n        }\n    }\n\n    static int get(int[] data, int size, int index) {\n        if (index < 0 || index >= size) {\n            throw new IndexOutOfBoundsException(\"index \" + index + \" di luar 0..\" + (size - 1));\n        }\n        return data[index];\n    }\n}", "python": "def get(data, size, index):\n    if index < 0 or index >= size:\n        raise IndexError(f\"index {index} di luar 0..{size - 1}\")\n    return data[index]\n\ndata = [7, 9, 4, 0, 0]\nsize = 3\nfor i in [1, 3, -1]:\n    try:\n        print(f\"get({i}) =\", get(data, size, i))\n    except IndexError as e:\n        print(\"Error:\", e)", "oj": "get(1) = 9\nError: index 3 di luar 0..2\nError: index -1 di luar 0..2\n", "op": "get(1) = 9\nError: index 3 di luar 0..2\nError: index -1 di luar 0..2\n"}, "16.0": {"t": "Rantai gerbong", "s": "Bangun linked list dengan menambah di depan: 30, lalu 20, lalu 10. Cetak data node pertama, kedua, dan ketiga lewat .next.", "l": ["addFirst: front = new ListNode(x, front).", "Node pertama: front.data. Kedua: front.next.data.", "Setiap .next = ikuti satu panah."], "java": "public class Main {\n    public static void main(String[] args) {\n        ListNode front = null;\n        front = new ListNode(30, front);\n        front = new ListNode(20, front);\n        front = new ListNode(10, front);\n        System.out.println(front.data);\n        System.out.println(front.next.data);\n        System.out.println(front.next.next.data);\n    }\n}\n\nclass ListNode {\n    int data;\n    ListNode next;\n    ListNode(int data, ListNode next) {\n        this.data = data;\n        this.next = next;\n    }\n}", "python": "class ListNode:\n    def __init__(self, data, next=None):\n        self.data = data\n        self.next = next\n\nfront = None\nfront = ListNode(30, front)\nfront = ListNode(20, front)\nfront = ListNode(10, front)\nprint(front.data)\nprint(front.next.data)\nprint(front.next.next.data)", "oj": "10\n20\n30\n", "op": "10\n20\n30\n"}, "16.1": {"t": "Statistik linked list", "s": "Untuk linked list 4 → 9 → 2 → 7, hitung banyak node, jumlah, dan nilai terbesar dengan satu kali penelusuran.", "l": ["cur = front, lalu while (cur != null).", "Di setiap node: count++, total += data, perbarui maks.", "Jangan lupa cur = cur.next agar tidak loop selamanya."], "java": "public class Main {\n    public static void main(String[] args) {\n        ListNode front = new ListNode(4, new ListNode(9, new ListNode(2, new ListNode(7, null))));\n        int count = 0, total = 0, maks = front.data;\n        ListNode cur = front;\n        while (cur != null) {\n            count++;\n            total += cur.data;\n            if (cur.data > maks) maks = cur.data;\n            cur = cur.next;\n        }\n        System.out.println(\"count=\" + count + \" total=\" + total + \" maks=\" + maks);\n    }\n}\n\nclass ListNode {\n    int data;\n    ListNode next;\n    ListNode(int data, ListNode next) {\n        this.data = data;\n        this.next = next;\n    }\n}", "python": "class ListNode:\n    def __init__(self, data, next=None):\n        self.data = data\n        self.next = next\n\nfront = ListNode(4, ListNode(9, ListNode(2, ListNode(7))))\ncount, total, maks = 0, 0, front.data\ncur = front\nwhile cur is not None:\n    count += 1\n    total += cur.data\n    if cur.data > maks:\n        maks = cur.data\n    cur = cur.next\nprint(f\"count={count} total={total} maks={maks}\")", "oj": "count=4 total=22 maks=9\n", "op": "count=4 total=22 maks=9\n"}, "17.0": {"t": "Kamus angka (BST)", "s": "Masukkan 8, 3, 10, 1, 6, 14 ke binary search tree. Lalu cek apakah 6 dan 9 ada, dan hitung tinggi pohonnya.", "l": ["add: kecil → kiri, besar → kanan, sampai ketemu null.", "contains: ikuti arah yang sama; null berarti tidak ada.", "tinggi = 1 + maks(tinggi kiri, tinggi kanan); pohon kosong = 0."], "java": "public class Main {\n    public static void main(String[] args) {\n        TreeNode root = null;\n        for (int v : new int[]{8, 3, 10, 1, 6, 14}) {\n            root = add(root, v);\n        }\n        System.out.println(\"ada 6? \" + contains(root, 6));\n        System.out.println(\"ada 9? \" + contains(root, 9));\n        System.out.println(\"tinggi = \" + height(root));\n    }\n\n    static TreeNode add(TreeNode node, int v) {\n        if (node == null) return new TreeNode(v);\n        if (v < node.data) node.left = add(node.left, v);\n        else node.right = add(node.right, v);\n        return node;\n    }\n\n    static boolean contains(TreeNode node, int v) {\n        if (node == null) return false;\n        if (v == node.data) return true;\n        if (v < node.data) return contains(node.left, v);\n        return contains(node.right, v);\n    }\n\n    static int height(TreeNode node) {\n        if (node == null) return 0;\n        return 1 + Math.max(height(node.left), height(node.right));\n    }\n}\n\nclass TreeNode {\n    int data;\n    TreeNode left, right;\n    TreeNode(int data) { this.data = data; }\n}", "python": "class TreeNode:\n    def __init__(self, data):\n        self.data = data\n        self.left = None\n        self.right = None\n\ndef add(node, v):\n    if node is None: return TreeNode(v)\n    if v < node.data: node.left = add(node.left, v)\n    else: node.right = add(node.right, v)\n    return node\n\ndef contains(node, v):\n    if node is None: return False\n    if v == node.data: return True\n    if v < node.data: return contains(node.left, v)\n    return contains(node.right, v)\n\ndef height(node):\n    if node is None: return 0\n    return 1 + max(height(node.left), height(node.right))\n\nroot = None\nfor v in [8, 3, 10, 1, 6, 14]:\n    root = add(root, v)\nprint(\"ada 6?\", contains(root, 6))\nprint(\"ada 9?\", contains(root, 9))\nprint(\"tinggi =\", height(root))", "oj": "ada 6? true\nada 9? false\ntinggi = 3\n", "op": "ada 6? True\nada 9? False\ntinggi = 3\n"}, "17.1": {"t": "Tiga cara menelusuri pohon", "s": "Untuk BST dari 8, 3, 10, 1, 6, cetak urutan pre-order, in-order, dan post-order.", "l": ["Ketiganya sama: kunjungi kiri dan kanan secara rekursif.", "Bedanya hanya posisi baris cetak: sebelum, di antara, atau sesudah.", "In-order pada BST selalu terurut."], "java": "public class Main {\n    public static void main(String[] args) {\n        TreeNode root = null;\n        for (int v : new int[]{8, 3, 10, 1, 6}) root = add(root, v);\n        System.out.print(\"pre : \"); pre(root); System.out.println();\n        System.out.print(\"in  : \"); in(root); System.out.println();\n        System.out.print(\"post: \"); post(root); System.out.println();\n    }\n\n    static TreeNode add(TreeNode n, int v) {\n        if (n == null) return new TreeNode(v);\n        if (v < n.data) n.left = add(n.left, v); else n.right = add(n.right, v);\n        return n;\n    }\n\n    static void pre(TreeNode n)  { if (n != null) { System.out.print(n.data + \" \"); pre(n.left); pre(n.right); } }\n    static void in(TreeNode n)   { if (n != null) { in(n.left); System.out.print(n.data + \" \"); in(n.right); } }\n    static void post(TreeNode n) { if (n != null) { post(n.left); post(n.right); System.out.print(n.data + \" \"); } }\n}\n\nclass TreeNode {\n    int data;\n    TreeNode left, right;\n    TreeNode(int data) { this.data = data; }\n}", "python": "class TreeNode:\n    def __init__(self, data):\n        self.data, self.left, self.right = data, None, None\n\ndef add(n, v):\n    if n is None: return TreeNode(v)\n    if v < n.data: n.left = add(n.left, v)\n    else: n.right = add(n.right, v)\n    return n\n\ndef pre(n):\n    if n: print(n.data, end=\" \"); pre(n.left); pre(n.right)\n\ndef ino(n):\n    if n: ino(n.left); print(n.data, end=\" \"); ino(n.right)\n\ndef post(n):\n    if n: post(n.left); post(n.right); print(n.data, end=\" \")\n\nroot = None\nfor v in [8, 3, 10, 1, 6]:\n    root = add(root, v)\nprint(\"pre : \", end=\"\"); pre(root); print()\nprint(\"in  : \", end=\"\"); ino(root); print()\nprint(\"post: \", end=\"\"); post(root); print()", "oj": "pre : 8 3 1 6 10 \nin  : 1 3 6 8 10 \npost: 1 6 3 10 8 \n", "op": "pre : 8 3 1 6 10 \nin  : 1 3 6 8 10 \npost: 1 6 3 10 8 \n"}, "18.0": {"t": "Loker hash", "s": "Buat tabel hash 5 ember dengan chaining. Masukkan kunci 12, 7, 9, 3, 15, lalu cetak isi setiap ember dan tunjukkan collision.", "l": ["indeks = kunci % 5.", "Setiap ember adalah list; kunci baru di-append ke ember itu.", "Ember berisi lebih dari satu kunci = terjadi collision."], "java": "import java.util.ArrayList;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<List<Integer>> tabel = new ArrayList<>();\n        for (int i = 0; i < 5; i++) tabel.add(new ArrayList<>());\n        for (int k : new int[]{12, 7, 9, 3, 15}) {\n            tabel.get(k % 5).add(k);\n        }\n        for (int i = 0; i < 5; i++) {\n            String tanda = tabel.get(i).size() > 1 ? \"  <- collision\" : \"\";\n            System.out.println(\"[\" + i + \"] \" + tabel.get(i) + tanda);\n        }\n    }\n}", "python": "tabel = [[] for _ in range(5)]\nfor k in [12, 7, 9, 3, 15]:\n    tabel[k % 5].append(k)\nfor i in range(5):\n    tanda = \"  <- collision\" if len(tabel[i]) > 1 else \"\"\n    print(\"[\" + str(i) + \"] \" + str(tabel[i]) + tanda)", "oj": "[0] [15]\n[1] []\n[2] [12, 7]  <- collision\n[3] [3]\n[4] [9]\n", "op": "[0] [15]\n[1] []\n[2] [12, 7]  <- collision\n[3] [3]\n[4] [9]\n"}, "18.1": {"t": "Daftar tugas prioritas", "s": "Tugas datang dengan prioritas (angka kecil = paling mendesak): Cuci piring 3, Kerjakan PR 1, Main game 5, Belajar ujian 2. Kerjakan sesuai prioritas.", "l": ["Masukkan semua tugas ke priority queue berdasarkan angkanya.", "Selama tidak kosong: ambil yang terkecil.", "Python: simpan sebagai tuple (prioritas, nama)."], "java": "import java.util.PriorityQueue;\n\npublic class Main {\n    public static void main(String[] args) {\n        PriorityQueue<Tugas> pq = new PriorityQueue<>((a, b) -> a.prioritas - b.prioritas);\n        pq.add(new Tugas(\"Cuci piring\", 3));\n        pq.add(new Tugas(\"Kerjakan PR\", 1));\n        pq.add(new Tugas(\"Main game\", 5));\n        pq.add(new Tugas(\"Belajar ujian\", 2));\n        while (!pq.isEmpty()) {\n            Tugas t = pq.remove();\n            System.out.println(t.prioritas + \". \" + t.nama);\n        }\n    }\n}\n\nclass Tugas {\n    String nama;\n    int prioritas;\n    Tugas(String nama, int prioritas) { this.nama = nama; this.prioritas = prioritas; }\n}", "python": "import heapq\n\npq = []\nheapq.heappush(pq, (3, \"Cuci piring\"))\nheapq.heappush(pq, (1, \"Kerjakan PR\"))\nheapq.heappush(pq, (5, \"Main game\"))\nheapq.heappush(pq, (2, \"Belajar ujian\"))\nwhile pq:\n    prioritas, nama = heapq.heappop(pq)\n    print(str(prioritas) + \".\", nama)", "oj": "1. Kerjakan PR\n2. Belajar ujian\n3. Cuci piring\n5. Main game\n", "op": "1. Kerjakan PR\n2. Belajar ujian\n3. Cuci piring\n5. Main game\n"}, "19.0": {"t": "Urutkan dengan aturan sendiri", "s": "Urutkan nama Siti, Al, Budiman, Eka berdasarkan panjang nama (pendek dulu) memakai lambda, lalu cetak dalam huruf besar.", "l": ["Aturan urut ditulis sebagai lambda: (a, b) -> a.length() - b.length() / key=lambda s: len(s).", "Lambda kedua mengubah setiap nama: s -> s.toUpperCase().", "Lambda = method kecil tanpa nama."], "java": "import java.util.ArrayList;\nimport java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<String> nama = new ArrayList<>(List.of(\"Siti\", \"Al\", \"Budiman\", \"Eka\"));\n        nama.sort((a, b) -> a.length() - b.length());\n        System.out.println(nama);\n        nama.forEach(s -> System.out.println(s.toUpperCase()));\n    }\n}", "python": "nama = [\"Siti\", \"Al\", \"Budiman\", \"Eka\"]\nnama.sort(key=lambda s: len(s))\nprint(nama)\nfor s in map(lambda s: s.upper(), nama):\n    print(s)", "oj": "[Al, Eka, Siti, Budiman]\nAL\nEKA\nSITI\nBUDIMAN\n", "op": "['Al', 'Eka', 'Siti', 'Budiman']\nAL\nEKA\nSITI\nBUDIMAN\n"}, "19.1": {"t": "Kasir diskon", "s": "Harga belanja: 30000, 75000, 120000, 45000, 60000. Barang di atas 50000 diberi diskon 20%. Hitung total yang dibayar untuk barang-barang yang didiskon saja.", "l": ["\"barang di atas 50000\" → filter.", "\"diberi diskon 20%\" → map: x -> x * 80 / 100.", "\"hitung total\" → reduce / sum."], "java": "import java.util.List;\n\npublic class Main {\n    public static void main(String[] args) {\n        List<Integer> harga = List.of(30000, 75000, 120000, 45000, 60000);\n        int total = harga.stream()\n                .filter(x -> x > 50000)\n                .map(x -> x * 80 / 100)\n                .reduce(0, Integer::sum);\n        System.out.println(\"Total diskon: \" + total);\n    }\n}", "python": "from functools import reduce\n\nharga = [30000, 75000, 120000, 45000, 60000]\nmahal = filter(lambda x: x > 50000, harga)\ndiskon = map(lambda x: x * 80 // 100, mahal)\ntotal = reduce(lambda a, b: a + b, diskon, 0)\nprint(\"Total diskon:\", total)", "oj": "Total diskon: 204000\n", "op": "Total diskon: 204000\n"}};


/* ===================== VERSI JAVA SAJA =====================
   Bab (CH) dan topik (TOPICS) di data.js dipakai bersama jalur Java dan Python, jadi teksnya
   membandingkan keduanya. Di jalur Java, perbandingan dengan Python dihapus: kalimat yang
   menyebut Python diganti versi Java, dan soal kuis tentang Python diganti soal Java.
   Kunci: b<i> paragraf, p<i> poin, q<i> soal, q<i>.o<k> pilihan, selain itu nama field.
   Nilai null berarti dihapus. */
const JFIX={
 1:{b0:'Program adalah daftar instruksi yang dijalankan komputer satu per satu. Setiap instruksi disebut <b>statement</b>. Di Java, statement diakhiri titik koma dan dikelompokkan dengan kurung kurawal.',
    b1:'Java <b>dikompilasi</b>: perintah <code>javac</code> memeriksa seluruh kode lalu menerjemahkannya menjadi <b>bytecode</b>, kemudian JVM menjalankannya. Kesalahan sintaks sudah ketahuan sebelum program berjalan.',
    b2:'Begitu program bertambah panjang, pecah menjadi bagian kecil bernama <b>method</b>. Teknik ini disebut dekomposisi prosedural. Setiap bagian punya satu tugas yang jelas dan bisa dipanggil berkali-kali.',
    p1:'Program Java selalu mulai dari method <code>main</code>, lalu dijalankan dari atas ke bawah.',
    p2:'Komentar (<code>//</code> untuk satu baris, <code>/* ... */</code> untuk beberapa baris) diabaikan komputer.',
    vizD:'Ikuti jalur program Java dari kode sumber sampai tampil di layar.',
    'q0.o2':'File Halo.txt',
    q1:{q:'Di Java, apa yang menandai bahwa beberapa baris berada di dalam satu blok?',o:['Kurung kurawal { }','Indentasi (spasi di awal baris)','Titik koma','Tanda kutip'],a:0,w:'Java mengelompokkan baris dengan kurung kurawal. Indentasi hanya membantu manusia membaca.'}},
 2:{b0:'Data disimpan di <b>variabel</b>. Java mewajibkan kamu menulis <b>tipe data</b>: <code>int</code> untuk bilangan bulat, <code>double</code> untuk pecahan, <code>boolean</code> untuk benar/salah, <code>char</code> untuk satu karakter.',
    b1:'Ekspresi seperti <code>7 / 2</code> punya jebakan. Di Java, pembagian dua <code>int</code> membuang pecahannya sehingga hasilnya 3. Agar hasilnya 3.5, salah satu angka harus <code>double</code>, misalnya <code>7.0 / 2</code>. Operator <code>%</code> memberi sisa bagi dan sering dipakai untuk cek genap/ganjil.',
    b2:'<b>Perulangan pasti</b> dipakai saat jumlah pengulangan sudah diketahui. Java memakai <code>for (init; kondisi; update)</code>. Loop di dalam loop (nested loop) cocok untuk pola dua dimensi seperti segitiga bintang.',
    p2:'<code>for (int i = 1; i &lt; 5; i++)</code> menghasilkan i = 1, 2, 3, 4.',
    q1:{q:'Nilai i apa saja yang dihasilkan <code>for (int i = 1; i &lt; 5; i++)</code>?',o:['1, 2, 3, 4, 5','1, 2, 3, 4','0, 1, 2, 3, 4, 5','1 dan 5'],a:1,w:'Kondisi i < 5 berhenti sebelum 5, jadi i bernilai 1 sampai 4.'}},
 3:{p1:'Method bertipe <code>void</code> tidak mengembalikan nilai. Method bertipe lain wajib memakai <code>return</code>.',
    p2:'<code>Scanner.nextLine()</code> selalu menghasilkan String. Ubah dengan <code>Integer.parseInt()</code> atau <code>Double.parseDouble()</code>.',
    q0:{q:'Method Java bertipe <code>void</code> mengembalikan apa?',o:['0','Tidak mengembalikan nilai apa pun','String kosong','Error'],a:1,w:'void berarti method hanya mengerjakan tugas tanpa mengembalikan nilai.'}},
 4:{b0:'Percabangan membuat program memilih. <code>if</code> menjalankan blok hanya bila kondisinya benar. Rantai <code>if / else if / else</code> dicek dari atas. Begitu satu kondisi benar, sisanya dilewati.'},
 5:{b1:'Kondisi bisa digabung dengan <b>logika boolean</b>: AND (<code>&amp;&amp;</code>), OR (<code>||</code>), dan NOT (<code>!</code>). <code>&amp;&amp;</code> dan <code>||</code> memakai <b>short-circuit</b>: jika bagian kiri sudah menentukan hasil, bagian kanan tidak dievaluasi.'},
 6:{b0:'Program nyata membaca data dari file, bukan hanya dari keyboard. Di Java, <code>Scanner</code> yang sama bisa diarahkan ke <code>new File("nilai.txt")</code>.',
    b2:'Membuka file bisa gagal, misalnya karena file tidak ada. Java memaksa kamu menangani kemungkinan itu (<code>throws FileNotFoundException</code>), karena ini termasuk <b>checked exception</b>.',
    p2:'Menulis file: <code>PrintStream</code> atau <code>FileWriter</code>.',
    q1:{q:'Mengapa memakai <code>try (Scanner sc = new Scanner(file))</code> (try-with-resources)?',o:['Supaya lebih cepat','File otomatis ditutup walau terjadi error','Wajib secara sintaks','Untuk membuat file baru'],a:1,w:'Try-with-resources menjamin file ditutup saat blok selesai, walau terjadi error.'}},
 7:{b0:'<b>Array</b> menyimpan banyak nilai bertipe sama di bawah satu nama. Setiap elemen punya <b>indeks</b> mulai dari 0. Array 5 elemen punya indeks 0 sampai 4. Mengakses indeks 5 menghasilkan <code>ArrayIndexOutOfBoundsException</code>. Ukuran array tetap setelah dibuat.',
    p1:'Elemen terakhir array adalah <code>a[a.length - 1]</code>. Java tidak mengenal indeks negatif.'},
 8:{b1:'<b>Konstruktor</b> dijalankan saat objek dibuat dengan <code>new Titik(3, 4)</code>. Tugasnya mengisi nilai awal field. Kata <code>this</code> merujuk ke objek yang sedang dipakai.',
    b2:'<b>Enkapsulasi</b> berarti menyembunyikan field (<code>private</code>) dan hanya membuka method tertentu. Dengan begitu objek bisa menjaga datanya tetap valid. Method <code>toString()</code> menentukan bagaimana objek tampil saat dicetak.',
    p1:'Field <code>private</code> hanya bisa diakses dari dalam kelasnya sendiri.',
    p2:'Java memberi nilai default pada field (0, false, null) bila konstruktor tidak mengisinya.'},
 9:{p2:'Java hanya mengizinkan satu kelas induk (<code>extends</code>), tetapi boleh banyak interface (<code>implements</code>).'},
 10:{b0:'Array berukuran tetap sering merepotkan. <code>ArrayList</code> adalah daftar yang bisa tumbuh dan menyusut sendiri. Kamu bisa <code>add</code>, <code>remove</code>, <code>get</code>, dan <code>set</code> tanpa memikirkan ukuran.',
    p0:'<code>list.size()</code> untuk ArrayList, <code>a.length</code> untuk array.',
    p3:'Stream: <code>a.stream().map(x -&gt; x * 2).toList()</code> membuat list baru dengan ringkas.'},
 11:{b0:'Selain List, ada dua koleksi penting. <b>Set</b> adalah himpunan: tidak ada duplikat dan pengecekan <code>contains</code> sangat cepat. <b>Map</b> memasangkan <b>kunci</b> dengan <b>nilai</b>, misalnya kata dengan jumlah kemunculannya.',
    p2:'<code>HashMap</code> tidak menjamin urutan. Pakai <code>LinkedHashMap</code> bila urutan saat data dimasukkan perlu dijaga.'},
 12:{p2:'Rekursi tanpa base case berakhir dengan <code>StackOverflowError</code>.'},
 13:{p3:'Menukar dua nilai butuh variabel bantu: <code>int t = a; a = b; b = t;</code>.'},
 14:{p2:'<code>ArrayDeque</code> bisa dipakai sebagai stack (<code>push</code>/<code>pop</code>) maupun queue (<code>offer</code>/<code>poll</code>).',
    p3:'<code>ArrayList.remove(0)</code> lambat (O(n)) karena semua elemen bergeser. Pakai <code>ArrayDeque.poll()</code>.'},
 15:{p3:'Implementasikan <code>Iterable</code> agar objekmu bisa dipakai di for-each seperti list.'},
 16:{b0:'<b>Linked list</b> menyimpan data dalam <b>node</b> terpisah. Setiap node berisi data dan referensi <code>next</code> ke node berikutnya. Node terakhir menunjuk <code>null</code>. Kelas list hanya perlu mengingat <code>front</code>, yaitu node pertama.'},
 18:{b0:'<b>Hashing</b> adalah rahasia kecepatan HashMap dan HashSet. Sebuah fungsi hash mengubah kunci menjadi angka, lalu angka itu dipetakan ke indeks array yang disebut ember (bucket). Mencari kunci cukup menghitung hash-nya dan langsung melompat ke ember yang tepat, rata-rata O(1).',
    p1:'Kunci HashMap sebaiknya immutable, misalnya String atau Integer, dengan <code>equals</code> dan <code>hashCode</code> yang konsisten.'},
 19:{b1:'<b>Lambda</b> adalah fungsi tanpa nama yang ditulis ringkas, misalnya <code>n -&gt; n * 2</code>. Tiga operasi utamanya: <b>filter</b> menyaring elemen, <b>map</b> mengubah setiap elemen, <b>reduce</b> menggabungkan semuanya menjadi satu nilai.',
    b2:'Java 8 menghadirkan <b>Stream</b> untuk menulis pipeline ini secara berantai. Gaya ini mendorong <b>fungsi murni</b> dan data <b>immutable</b>, sehingga kode lebih mudah diuji dan aman dijalankan paralel.',
    p2:'Pakai Stream untuk mengolah data. Untuk logika yang rumit, loop biasa sering lebih mudah dibaca.',
    vizD:'Susun pipeline sendiri dan lihat kode Java Stream yang setara.'}
};
/* Topik: exw = penjelasan latihan, ri<k> = catatan rumus, lg.<kunci> = legenda, pj.l<k> = langkah mini project. */
const TJFIX={
 '1.0':{ri1:'Java: kelas → main → statement.'},
 '1.1':{exw:'Memanggil method cukup menulis namanya diikuti kurung. void hanya dipakai saat mendefinisikan method.'},
 '2.0':{exw:'Pola Java: tipe nama = nilai. Nama selalu di kiri tanda =.','lg.tipe':'Jenis isi kotak. Java wajib menulisnya.'},
 '2.2':{ri0:'Untuk i = awal; i < akhir: putaran = akhir − awal.'},
 '2.3':{exw:'Loop luar mengatur baris, loop dalam mengatur isi setiap baris.'},
 '3.1':{exw:'Indeks terakhir = panjang − 1.',ri3:'Angka yang digabung dengan String ikut menjadi teks: "Nilai: " + 5 → "Nilai: 5".'},
 '3.2':{exw:'Pecahan → double.',ri1:'Lupa Integer.parseInt() → "20" + 12 menghasilkan teks "2012", bukan 32.'},
 '4.0':{ri3:'Kata "jika … selain itu" → if … else. "jika … kalau tidak jika" → else if.'},
 '5.0':{'lg.cond':'Dicek sebelum setiap putaran. false → keluar.'},
 '5.1':{exw:'"dan" → &&, "minimal 17" → >= 17. "atau" akan membolehkan orang tanpa tiket.','pj.l1':'"dan tidak" → && !(...).'},
 '6.1':{ri2:'Java memaksa menangani checked exception seperti FileNotFoundException.'},
 '7.0':{ri2:'Akses a[panjang] → ArrayIndexOutOfBoundsException.'},
 '8.0':{exw:'Java memakai new untuk membuat objek. Variabel tetap di sebelah kiri.'},
 '8.1':{ri2:'private dijaga compiler: kode di luar kelas tidak bisa menyentuh field itu.','lg.call':'Di dalam setor, this menunjuk objek a.'},
 '9.1':{ri2:'Kelas yang implements sebuah interface wajib punya semua method interface itu.'},
 '10.1':{exw:'Berjalan maju sambil menghapus bisa melewatkan elemen. remove("") hanya menghapus satu.'},
 '13.1':{exw:'Tanpa variabel bantu, nilai x hilang setelah x = y.'},
 '14.0':{ri2:'pop pada stack kosong → error. Cek isEmpty() dulu.'},
 '14.1':{ri2:'Pakai ArrayDeque.poll(), bukan ArrayList.remove(0) yang lambat.'},
 '18.1':{'pj.l2':'Simpan sebagai objek kecil berisi prioritas dan nama, lalu urutkan dengan Comparator.'},
 '19.0':{exw:'Pola lambda: (parameter) -> ekspresi hasil.','pj.l0':'Aturan urut ditulis sebagai lambda: (a, b) -> a.length() - b.length().'}
};
/* Nama istilah glosarium yang memuat padanan Python. */
const JGLN={'Null / None':'Null','this / self':'this','toString / __str__':'toString()','Javadoc / Docstring':'Javadoc'};
const glName=(g,lang)=>lang==='java'&&JGLN[g.t]||g.t;
const CHJ_={};
function chJ(n){
  if(CHJ_[n])return CHJ_[n];
  const c=JSON.parse(JSON.stringify(CH[n-1])),f=JFIX[n]||{};
  for(const [k,v] of Object.entries(f)){let m;
    if((m=/^b(\d+)$/.exec(k)))c.body[+m[1]]=v;
    else if((m=/^p(\d+)$/.exec(k)))c.points[+m[1]]=v;
    else if((m=/^q(\d+)$/.exec(k)))c.quiz[+m[1]]=v;
    else if((m=/^q(\d+)\.o(\d+)$/.exec(k)))c.quiz[+m[1]].o[+m[2]]=v;
    else c[k]=v}
  c.body=c.body.filter(x=>x!=null);c.points=c.points.filter(x=>x!=null);c.quiz=c.quiz.filter(x=>x!=null);
  return CHJ_[n]=c;
}
const chFor=(n,lang)=>lang==='java'?chJ(n):CH[n-1];
/* Topik versi Java: teks diganti dan legenda hanya berisi bagian yang ada di kode Java. */
function tpJ(ref,tp){
  const f=TJFIX[ref]||{},t={...tp,ex:{...tp.ex},rumus:{...tp.rumus,i:[...(tp.rumus.i||[])]},legend:{}};
  for(const [k,v] of Object.entries(tp.legend))if(tp.java.includes('«'+k+'|'))t.legend[k]=f['lg.'+k]?[v[0],f['lg.'+k]]:v;
  if(f.exw)t.ex.w=f.exw;
  for(const [k,v] of Object.entries(f)){const m=/^ri(\d+)$/.exec(k);if(m)t.rumus.i[+m[1]]=v}
  return t;
}
const projJ=(ref,p)=>{const f=TJFIX[ref]||{};if(!p||!Object.keys(f).some(k=>k.startsWith('pj.')))return p;
  return {...p,l:p.l.map((x,i)=>f['pj.l'+i]||x)}};

/* ===================== PELAJARAN JAVA & PYTHON (lab & topic) =====================
   Dipindahkan dari app.js lama tanpa perubahan perilaku. */
function labHTML(n,lang){
  const c=chFor(n,lang);
  return `<nav class="toc" aria-label="Di halaman ini">${[['Konsep','#konsep'],['Lab','#lab'],['Program','#prog'],['Istilah','#istilah'],['Kuis','#quiz']].map(([a,b])=>`<button data-to="${b}">${a}</button>`).join('')}</nav>
  <section class="prose" id="konsep">${c.body.map(p=>`<p>${p}</p>`).join('')}</section>
  <ul class="points">${c.points.map(p=>`<li>${p}</li>`).join('')}</ul>
  <section class="viz" id="lab" aria-label="Visualisasi"><div class="viz-head"><span class="eyebrow">Lab interaktif</span><h3>${c.vizT}</h3><p>${c.vizD}</p></div><div id="vizHost" class="vizhost"></div></section>
  <section class="section" id="prog"><h2>Program lengkap</h2>${pane(lang,c[lang],{out:c.out==null?null:typeof c.out==='string'?c.out:c.out[lang]})}</section>
  <div class="tip"><b>Tip mentor.</b> ${c.tip}</div>
  <section class="section" id="istilah"><h2>Istilah di pelajaran ini</h2><div class="terms">${c.terms.map(id=>`<button class="term-chip" data-term="${id}">${glName(GLMAP[id],lang)}</button>`).join('')}</div></section>
  <section class="section" id="quiz"><h2>Kuis cepat</h2>${quizHTML(c.quiz,n)}</section>`;
}
function wireLab(n,lang){const c=chFor(n,lang);VLANG=lang;VIZ[c.viz]($('#vizHost'));wireQuiz($('#quiz'),c.quiz)}

/* ---------- jenis topic: lima langkah, satu bahasa ---------- */
const MK_RE=/«(\w+)\|([^»]*)»/g;
const strip=code=>code.replace(/«\w+\|([^»]*)»/g,'$1');
function markHL(code,lang,keys){
  let out='',last=0,m;MK_RE.lastIndex=0;
  while((m=MK_RE.exec(code))){const i=keys.indexOf(m[1]);
    out+=hl(code.slice(last,m.index),lang)+`<span class="mk" data-k="${m[1]}" style="--mc:var(--m${i%6})" tabindex="0" role="button" aria-label="Bagian ${i+1}">${hl(m[2],lang)}<sup>${i+1}</sup></span>`;last=MK_RE.lastIndex}
  return out+hl(code.slice(last),lang);
}
const traceSteps=tp=>typeof tp.trace==='function'?tp.trace():tp.trace;
function tracerFrames(tp,L){
  let mem={},out='';
  return traceSteps(tp).filter(s=>!s.only||s.only===L).map(s=>{
    mem={...mem};const chg=new Set();
    [...(s.d||[]),...(s['d'+L]||[])].forEach(k=>delete mem[k]);
    for(const src of [s.s,s['s'+L]])if(src)for(const k in src){mem[k]=src[k];chg.add(k)}
    const o=(s.o||'')+(s['o'+L]||'');out+=o;
    return {line:s[L],mem,chg,out,fresh:!!o,note:esc(s['n'+L]||s.n||'')};
  });
}
function prim(v,L){if(v===null||v===undefined)return L==='j'?'null':'None';if(typeof v==='boolean')return L==='j'?String(v):(v?'True':'False');const s=String(v);if(L==='p'&&s==='null')return 'None';return s}
function rv(v,L){
  const P=x=>esc(prim(x,L));
  if(v===null||typeof v!=='object')return P(v);
  const hs=h=>new Set(h==null?[]:[].concat(h));
  const cells=(arr,cls=()=>'',lab=i=>i)=>arr.length?`<div class="cells sm">${arr.map((x,i)=>`<div class="cell ${cls(i)}"><span class="ix">${lab(i)}</span>${P(x)}</div>`).join('')}</div>`:'<span class="mempty">(kosong)</span>';
  if(Array.isArray(v))return cells(v);
  if(v.arr){const H=hs(v.hl),lo=v.lo??0,hi=v.hi??v.arr.length-1;
    return (v.ref?`<span class="ref">→ menunjuk objek ${esc(v.ref)}</span>`:'')
      +cells(v.arr,i=>[H.has(i)?'hl':'',(i<lo||i>hi)?'dim':'',v.used!=null&&i>=v.used?'empty':'',v.done!=null&&i<v.done?'sorted':''].join(' '))
      +(v.lo!=null?`<span class="ref">${lo<=hi?`wilayah pencarian: indeks ${lo} sampai ${hi}`:'wilayah pencarian kosong'}</span>`:'')
      +(v.used!=null?`<span class="ref">terpakai: ${v.used} dari ${v.arr.length}</span>`:'');}
  if(v.str!=null){const H=hs(v.hl);return cells([...v.str].map(ch=>ch===' '?'␣':ch),i=>H.has(i)?'hl':'')}
  if(v.obj){const e=Object.entries(v.obj);return e.length?`<div class="ofields">${e.map(([k,x])=>`<span><i>${esc(k)}</i> = ${P(x)}</span>`).join('')}</div>`:'<span class="mempty">(objek baru, belum ada field)</span>'}
  if(v.map){const e=Object.entries(v.map);return e.length?`<div class="ofields">${e.map(([k,x])=>`<span class="${k===v.hl?'hl':''}"><i>"${esc(k)}"</i> → ${P(x)}</span>`).join('')}</div>`:'<span class="mempty">{ } kosong</span>'}
  if(v.set)return v.set.length?`<div class="ofields">${v.set.map(x=>`<span>${P(x)}</span>`).join('')}</div>`:'<span class="mempty">(himpunan kosong)</span>';
  if(v.chain)return `<div class="ll sm">${v.chain.map((x,i)=>`<div class="lnode ${i===v.at?'hl':''}"><span>${P(x)}</span><span>next</span></div><span class="ptr">→</span>`).join('')}<span class="ptr">${L==='j'?'null':'None'}</span></div>`;
  if(v.buckets)return `<div class="buckets">${v.buckets.map((b,i)=>`<div class="bucket ${i===v.hit?'hit':''}"><span class="bi">[${i}]</span><div class="chain">${b.map((x,k)=>`<span class="tok ${k>0?'col':''}">${P(x)}</span>`).join('')}</div></div>`).join('')}</div>`;
  if(v.stack)return cells(v.stack,()=>'',i=>i===v.stack.length-1?'atas':'');
  if(v.queue)return cells(v.queue,()=>'',i=>i===0?'depan':(i===v.queue.length-1?'belakang':''));
  return esc(JSON.stringify(v));
}
function drawTrace(stage,f,tp,L){
  const lang=L==='j'?'java':'python',lines=strip(tp[lang]).split('\n'),mem=Object.entries(f.mem);
  stage.innerHTML=`<div class="tracer">
   <div class="pane ${lang}"><div class="pane-h"><span>${lang.toUpperCase()}</span><span class="tl-hint">${f.line?`baris ${f.line} sedang dijalankan`:''}</span></div>
    <ol class="tlines">${lines.map((ln,i)=>`<li class="${f.line===i+1?'cur':''}"><span class="ln">${i+1}</span><span>${hl(ln,lang)||' '}</span></li>`).join('')}</ol></div>
   <div class="tside"><div><div class="eyebrow">Memori</div><div class="mem">${mem.length?mem.map(([k,[t,v]])=>{const ts=t.split('|');const wide=v!==null&&typeof v==='object';
      return `<div class="mbox ${f.chg.has(k)?'chg':''} ${wide?'wide':''}"><div class="mh"><span class="mn">${esc(k)}</span><span class="mt">${esc(L==='j'?ts[0]:(ts[1]??ts[0]))}</span></div><div class="mv">${rv(v,L)}</div></div>`}).join(''):'<span class="mempty">Belum ada variabel di memori.</span>'}</div></div>
    <div><div class="eyebrow">Keluaran</div><div class="console ${f.fresh?'fresh':''}">${esc(f.out)}</div></div></div></div>`;
}
const topicOf=(ref,lang)=>{const [n,i]=ref.split('.').map(Number),tp=TOPICS[n][i];return {n,i,tp:lang==='java'?tpJ(ref,tp):tp}};
function topicHTML1(ref,lang){
  const {n,i,tp}=topicOf(ref,lang),keys=Object.keys(tp.legend),J=lang==='java',ord=perm(tp.ex.o.length,n*10+i),p=J?projJ(ref,PROJ[ref]):PROJ[ref],R2=RUMUS[ref];
  const pyCell=s=>s.startsWith('(')?`<span class="c">${esc(s)}</span>`:hl(s,'python');
  const o=p&&(J?p.oj:p.op);
  return `<div class="steps" role="list">${['Kalimat → kode','Anatomi','Eksekusi','Rumus','Mini project'].map((x,k)=>`<button role="listitem" data-ph="${k}"><span>${k+1}</span>${x}</button>`).join('')}</div>
  <article class="phase"><header class="ph-h"><span class="ph-n">1</span><div><h3>Dari kalimat ke kode</h3><p>Tulis dulu maksudmu dalam bahasa sehari-hari. Setiap kalimat menjadi satu baris kode.</p></div></header>
   <div class="trt one"><div class="trr th"><div>Kalimat manusia</div><div class="${J?'j':'p'}">${J?'Java':'Python'}</div></div>
    ${tp.tr.map(r=>`<div class="trr"><div class="trs">${esc(r[0])}</div><pre class="trc" data-l="${J?'Java':'Python'}">${J?hl(r[1],'java'):pyCell(r[2])}</pre></div>`).join('')}</div>
   <div class="ex"><div><span class="eyebrow">Giliranmu menerjemahkan</span><p class="exq">“${esc(tp.ex.q)}”</p></div>
    <div class="exo">${ord.map(oi=>`<button class="opt code-opt" data-o="${oi}"><pre>${hl(tp.ex.o[oi][J?0:1],lang)}</pre></button>`).join('')}</div><p class="why" hidden></p></div></article>
  <article class="phase" id="anat"><header class="ph-h"><span class="ph-n">2</span><div><h3>Anatomi kode</h3><p>Klik bagian kode yang bernomor, atau klik istilah di daftar, untuk melihat bagian mana yang dimaksud.</p></div></header>
   <div class="pane ${lang}"><div class="pane-h"><span>${J?'JAVA':'PYTHON'}</span></div><pre class="code">${markHL(tp[lang],lang,keys)}</pre></div>
   <ol class="legend">${keys.map((k,q)=>{const [id,d]=tp.legend[k],g=GLMAP[id];return `<li style="--mc:var(--m${q%6})" data-k="${k}"><button class="lg" data-k="${k}"><span class="badge">${q+1}</span><span><b>${g?glName(g,lang):id}</b>${g?` <small>${g.en}</small>`:''}<span class="ld">${esc(d)}</span></span></button><button class="glink" data-term="${id}" title="Buka di glosarium">Glosarium</button></li>`}).join('')}</ol></article>
  <article class="phase"><header class="ph-h"><span class="ph-n">3</span><div><h3>Eksekusi baris demi baris</h3><p>Garis kuning adalah baris yang sedang dijalankan. Kotak hijau di memori berarti nilainya baru saja berubah.</p></div></header><div id="trHost" class="trhost"></div></article>
  <article class="phase"><header class="ph-h"><span class="ph-n">4</span><div><h3>Rumus praktis</h3><p>Pola sintaks yang dipakai programmer. Ganti kata seperti <code>type</code>, <code>name</code>, dan <code>value</code> dengan milikmu sendiri.</p></div></header>
   ${pane(lang,R2[J?0:1],{copy:false})}<ul class="rl">${tp.rumus.i.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></article>
  ${p?`<article class="phase" id="proj"><header class="ph-h"><span class="ph-n">5</span><div><h3>Mini project: ${esc(p.t)}</h3><p>Kerjakan sendiri dulu di editor atau IDE kamu. Buka solusi hanya untuk mencocokkan.</p></div></header>
   <p class="pj-s">${esc(p.s)}</p>
   ${p.file?`<div><div class="eyebrow">Isi file ${esc(p.file[0])}</div><div class="console">${esc(p.file[1])}</div></div>`:''}
   ${p.inp?`<div><div class="eyebrow">Contoh input dari pengguna</div><div class="console">${esc(p.inp)}</div></div>`:''}
   <div><div class="eyebrow">Langkah dari kalimat ke kode</div><ol class="rl">${p.l.map(s=>`<li>${esc(s)}</li>`).join('')}</ol></div>
   <div><div class="eyebrow">Keluaran yang diharapkan</div><div class="console">${esc(o)}</div></div>
   <button class="btn primary pj-tg" aria-expanded="false" aria-controls="pjSol">Tampilkan solusi</button>
   <div id="pjSol" hidden>${pane(lang,p[lang])}</div></article>`:''}`;
}
function activateMark(root,k,scroll){
  const box=$('#anat',root);if(!box)return;
  const on=k&&!box.querySelector(`.legend li[data-k="${k}"].on`);
  box.querySelectorAll('.mk,.legend li').forEach(e=>e.classList.toggle('on',on&&e.dataset.k===k));
  box.classList.toggle('has-active',!!on);
  if(on&&scroll){const m=box.querySelector(`.mk[data-k="${k}"]`)||box.querySelector(`.legend li[data-k="${k}"]`);m.scrollIntoView({block:'center',behavior:'smooth'})}
}
function wireTopic1(ref,lang){
  const {tp}=topicOf(ref,lang),host=$('.l-body'),L=lang==='java'?'j':'p';
  player($('#trHost'),tracerFrames(tp,L),(st,f)=>drawTrace(st,f,tp,L),{speed:1500});
  const ex=$('.ex',host);
  ex.addEventListener('click',e=>{const b=e.target.closest('.opt');if(!b||b.disabled)return;const pick=+b.dataset.o;
    ex.querySelectorAll('.opt').forEach(x=>{x.disabled=true;const o=+x.dataset.o;if(o===tp.ex.a)x.classList.add('right');else if(o===pick)x.classList.add('wrong')});
    const w=$('.why',ex);w.hidden=false;w.innerHTML=(pick===tp.ex.a?'<b class="okc">Tepat.</b> ':'<b class="badc">Belum tepat.</b> ')+esc(tp.ex.w)});
  const an=$('#anat',host);
  an.addEventListener('click',e=>{const m=e.target.closest('.mk,.lg');if(m)activateMark(host,m.dataset.k,false)});
  an.addEventListener('keydown',e=>{const m=e.target.closest('.mk');if(m&&(e.key==='Enter'||e.key===' ')){e.preventDefault();activateMark(host,m.dataset.k,false)}});
  const pj=$('#proj',host);
  if(pj)pj.addEventListener('click',e=>{const tg=e.target.closest('.pj-tg');if(!tg)return;const sol=$('#pjSol',pj),show=sol.hidden;sol.hidden=!show;tg.setAttribute('aria-expanded',show);tg.textContent=show?'Sembunyikan solusi':'Tampilkan solusi';tg.classList.toggle('primary',!show)});
  $('.steps',host).addEventListener('click',e=>{const b=e.target.closest('[data-ph]');if(b)host.querySelectorAll('.phase')[+b.dataset.ph].scrollIntoView({behavior:'smooth',block:'start'})});
  if(pendingFocus){const k=pendingFocus.k;pendingFocus=null;setTimeout(()=>{activateMark(host,k,true);an.classList.add('flash');setTimeout(()=>an.classList.remove('flash'),2200)},60)}
}

/* ===================== KUIS CERITA & GLOSARIUM ===================== */
/* ===================== KUIS CERITA ===================== */
const SQL_STORIES=[
  {lvl:'Dasar',m:3,t:'Promo khusus Jakarta',s:'Tim pemasaran ingin mengirim voucher hanya ke pelanggan yang tinggal di Jakarta. Rina menulis query untuk mengambil nama mereka.',sql:"SELECT nama FROM pelanggan\nWHERE kota = 'Jakarta';",q:'Apa hasil query ini?',o:['2 baris: Andi dan Dewi','1 baris: Andi','8 baris, semua pelanggan','0 baris, karena huruf J kapital'],a:0,w:'Hanya Andi dan Dewi yang kotanya Jakarta. WHERE menyaring baris sebelum hasil ditampilkan.'},
  {lvl:'Dasar',m:5,t:'Menghitung pelanggan',s:'Manajer bertanya berapa pelanggan yang sudah mengisi kota. Salah satu pelanggan, Gita, belum mengisinya.',sql:'SELECT COUNT(*) AS a, COUNT(kota) AS b\nFROM pelanggan;',q:'Berapa nilai a dan b?',o:['a = 8, b = 7','a = 8, b = 8','a = 7, b = 7','a = 7, b = 8'],a:0,w:'COUNT(*) menghitung semua baris (8), COUNT(kota) melewati nilai NULL, jadi 7.'},
  {lvl:'Dasar',m:3,t:'Mencari yang belum isi kota',s:'Admin ingin menemukan pelanggan yang kotanya kosong, lalu menulis kondisi dengan tanda sama dengan.',sql:'SELECT nama FROM pelanggan\nWHERE kota = NULL;',q:'Apa yang terjadi?',o:['0 baris; seharusnya pakai IS NULL','1 baris: Gita','Error sintaks','8 baris'],a:0,w:'NULL berarti "tidak diketahui". Membandingkan apa pun dengan = NULL hasilnya bukan TRUE, jadi tidak ada baris yang lolos. Pakai WHERE kota IS NULL.'},
  {lvl:'Dasar',m:4,t:'Lupa WHERE',s:'Budi ingin mengubah harga Teh Melati menjadi Rp10.000, tapi terburu-buru dan lupa menulis WHERE.',sql:'UPDATE produk SET harga = 10000;',q:'Berapa produk yang harganya berubah?',o:['Semua 8 produk','Hanya 1 produk','Tidak ada, karena error','Hanya produk di atas Rp10.000'],a:0,w:'Tanpa WHERE, UPDATE berlaku untuk semua baris. Biasakan menulis SELECT dengan WHERE yang sama dulu untuk mengecek baris yang akan terkena.'},
  {lvl:'Dasar',m:3,t:'Produk termahal',s:'Pemilik toko ingin tahu satu produk paling mahal untuk dipajang di halaman depan.',sql:'SELECT nama FROM produk\nORDER BY harga DESC\nLIMIT 1;',q:'Produk apa yang muncul?',o:['Madu Hutan','Kopi Gayo','Rendang Kaleng','Keripik Singkong'],a:0,w:'ORDER BY harga DESC menaruh harga tertinggi (Madu Hutan, Rp120.000) di atas, lalu LIMIT 1 mengambil baris pertama.'},
  {lvl:'Menengah',m:5,t:'Rekap per kategori',s:'Untuk laporan bulanan, Sari menghitung jumlah produk di setiap kategori.',sql:'SELECT kategori, COUNT(*)\nFROM produk\nGROUP BY kategori;',q:'Berapa baris hasilnya?',o:['4 baris','8 baris','1 baris','3 baris'],a:0,w:'GROUP BY membuat satu baris per kategori: Minuman, Camilan, Bumbu, dan Makanan.'},
  {lvl:'Menengah',m:7,t:'Pelanggan yang belum belanja',s:'Tim CRM mencari pelanggan yang belum pernah memesan untuk diberi ucapan selamat datang.',sql:'SELECT p.nama\nFROM pelanggan p\nLEFT JOIN pesanan s ON s.pelanggan_id = p.id\nGROUP BY p.nama\nHAVING COUNT(s.id) = 0;',q:'Siapa yang muncul?',o:['Gita','Tidak ada','Gita dan Hadi','Error: COUNT tidak boleh di HAVING'],a:0,w:'LEFT JOIN mempertahankan pelanggan tanpa pesanan dengan s.id NULL. COUNT(s.id) untuk Gita bernilai 0.'},
  {lvl:'Menengah',m:7,t:'Berapa baris gabungan?',s:'Ada 8 pelanggan dan 10 pesanan. Setiap pesanan pasti punya pelanggan yang terdaftar.',sql:'SELECT COUNT(*)\nFROM pelanggan p\nJOIN pesanan s ON s.pelanggan_id = p.id;',q:'Berapa hasil COUNT(*)?',o:['10','8','18','80'],a:0,w:'INNER JOIN menghasilkan satu baris untuk setiap pasangan yang cocok. Setiap dari 10 pesanan punya tepat satu pelanggan, jadi 10 baris.'},
  {lvl:'Menengah',m:8,t:'Di atas rata-rata',s:'Bagian keuangan ingin daftar produk yang harganya di atas rata-rata semua produk.',sql:'SELECT nama FROM produk\nWHERE harga > (SELECT AVG(harga) FROM produk);',q:'Berapa produk yang muncul?',o:['4 produk','3 produk','5 produk','Error: subquery tidak boleh di WHERE'],a:0,w:'Rata-rata harga Rp53.750. Yang di atasnya: Kopi Gayo, Kacang Mete, Madu Hutan, Rendang Kaleng.'},
  {lvl:'Lanjutan',m:11,t:'Transfer yang dibatalkan',s:'Saldo Andi Rp500.000. Kasir memulai transfer, lalu sadar salah nominal dan membatalkannya.',sql:'BEGIN;\nUPDATE rekening SET saldo = saldo - 100000 WHERE id = 1;\nROLLBACK;\nSELECT saldo FROM rekening WHERE id = 1;',q:'Berapa saldo yang tampil?',o:['500000','400000','0','Error karena ROLLBACK'],a:0,w:'ROLLBACK membatalkan semua perubahan sejak BEGIN, jadi saldo kembali Rp500.000.'},
  {lvl:'Lanjutan',m:14,t:'Peringkat gaji tim penjualan',s:'HR membuat peringkat gaji di divisi Penjualan. Yudi dan Rio sama-sama bergaji Rp8.000.000.',sql:"SELECT nama, RANK() OVER (ORDER BY gaji DESC) AS r\nFROM karyawan\nWHERE divisi = 'Penjualan';",q:'Berapa peringkat Rio?',o:['3, sama dengan Yudi','4','2','1'],a:0,w:'Umi 1, Zahra 2, lalu Yudi dan Rio seri di 3. RANK memberi angka sama untuk nilai seri.'},
  {lvl:'Lanjutan',m:12,t:'Form login yang bocor',s:"Aplikasi menyusun query dengan menyambung teks dari form: \"... WHERE username = '\" + input + \"'\". Seseorang mengetik ' OR '1'='1 di kolom username.",sql:"SELECT * FROM akun\nWHERE username = '' OR '1'='1';",q:'Apa yang terjadi?',o:['Semua akun terbaca karena kondisinya selalu benar','Error sintaks, login gagal','Hanya akun bernama OR yang terbaca','Tabel akun terhapus'],a:0,w:"Input penyerang menjadi bagian dari perintah SQL. '1'='1' selalu benar. Solusinya: parameter (prepared statement), bukan menyambung string."}];
let storyAns=store.get('rk-story2',{}),storyHide=store.get('rk-story-hide',true),storyLv='Semua';
function storiesOf(tk){
  if(tk==='sql')return SQL_STORIES.map((s,i)=>({key:'s'+i,lvl:s.lvl,s,code:s.sql,lang:'sql',link:{h:'#sql-'+s.m+'-1',t:`Modul ${s.m}: ${SQL_MODULES[s.m-1].t}`}}));
  return STORIES.map((s,i)=>[s,i]).filter(([s])=>s[tk]).map(([s,i])=>{const x=FLAT[tk].find(y=>y.l.k==='lab'&&y.l.n===s.b);return {key:tk[0]+i,lvl:CH[s.b-1].lvl,s,code:s[tk],lang:tk,link:x?{h:'#'+x.id,t:`${x.title}`}:null}});
}
function storyCard(it,ix){
  const s=it.s,a=storyAns[it.key],ans=a!=null,ord=perm(s.o.length,ix+3),hid=storyHide&&!ans;
  return `<article class="story ${ans?(a===s.a?'is-ok':'is-bad'):''}" data-key="${it.key}">
   <div class="tags"><span class="tag">${it.lvl}</span>${ans?`<span class="tag ${a===s.a?'okt':'badt'}">${a===s.a?'Benar':'Belum tepat'}</span>`:''}</div>
   <h3>${esc(s.t)}</h3><p class="st">${esc(s.s)}</p>
   <button class="btn peek" aria-expanded="${!hid}">${hid?'Tampilkan':'Sembunyikan'} kode</button><div ${hid?'hidden':''}>${pane(it.lang,it.code,{copy:false})}</div>
   <b>${esc(s.q)}</b>
   <div class="opts">${ord.map(oi=>`<button class="opt ${ans?(oi===s.a?'right':(oi===a?'wrong':'')):''}" data-o="${oi}" ${ans?'disabled':''}>${esc(s.o[oi])}</button>`).join('')}</div>
   <p class="why" ${ans?'':'hidden'}>${ans?esc(s.w):''}</p>
   ${it.link?`<a class="more" href="${it.link.h}">Pelajari lagi: ${esc(it.link.t)} →</a>`:''}</article>`;
}
function renderStories(tk){
  const all=storiesOf(tk),list=all.filter(x=>storyLv==='Semua'||x.lvl===storyLv);
  const ans=all.filter(x=>storyAns[x.key]!=null),ok=ans.filter(x=>storyAns[x.key]===x.s.a);
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Kuis cerita</span></nav>
   <div class="eyebrow">Kuis cerita</div><h1>Kode di kehidupan sehari-hari</h1>
   <p class="lead muted">Setiap soal adalah cerita kecil. Baca situasinya, bayangkan langkahnya, lalu tebak apa yang dilakukan kodenya.</p></header>
  <div class="tabs3" role="tablist" aria-label="Jalur">${TRACKS.filter(t=>['java','python','sql'].includes(t.k)).map(t=>`<a role="tab" class="t-${t.k}" href="#kuis-${t.k}" aria-selected="${t.k===tk}"><span class="tmark">${t.mark}</span>${t.name} <small>${storiesOf(t.k).length} soal</small></a>`).join('')}</div>
  <div class="score"><div><span class="big">${ok.length}</span><span class="of"> / ${all.length} benar</span></div>
   <div class="sc-bar"><div class="bar"><i style="width:${all.length?ans.length/all.length*100:0}%"></i></div><small>${ans.length} dari ${all.length} sudah dijawab</small></div>
   <label class="donebox hidebox"><input type="checkbox" id="stHide" ${storyHide?'checked':''}> Sembunyikan kode</label>
   <button class="btn" id="stReset" ${ans.length?'':'disabled'}>Ulangi</button></div>
  <div class="chips" role="group" aria-label="Tingkat" id="stLv">${['Semua',...LEVELS.map(L=>L.k)].map(L=>`<button class="chip" data-l="${L}" aria-pressed="${L===storyLv}">${L}</button>`).join('')}</div>
  <div class="stories" id="stories">${list.length?list.map((x,i)=>storyCard(x,all.indexOf(x))).join(''):'<p class="empty">Belum ada soal di tingkat ini.</p>'}</div>`;
}
function wireStories(tk){
  const all=storiesOf(tk);
  $('#stHide').onchange=e=>{storyHide=e.target.checked;store.set('rk-story-hide',storyHide);const y=scrollY;route();scrollTo(0,y)};
  $('#stLv').addEventListener('click',e=>{const b=e.target.closest('[data-l]');if(!b)return;storyLv=b.dataset.l;const y=scrollY;route();scrollTo(0,y)});
  $('#stories').addEventListener('click',e=>{
    const pk=e.target.closest('.peek');if(pk){const cd=pk.nextElementSibling,show=cd.hidden;cd.hidden=!show;pk.setAttribute('aria-expanded',show);pk.textContent=`${show?'Sembunyikan':'Tampilkan'} kode`;return}
    const b=e.target.closest('.opt');if(!b||b.disabled)return;const card=b.closest('.story'),it=all.find(x=>x.key===card.dataset.key);
    storyAns[it.key]=+b.dataset.o;store.set('rk-story2',storyAns);
    const tmp=document.createElement('div');tmp.innerHTML=storyCard(it,all.indexOf(it));card.replaceWith(tmp.firstElementChild);
    const ans=all.filter(x=>storyAns[x.key]!=null),ok=ans.filter(x=>storyAns[x.key]===x.s.a);
    $('.score .big').textContent=ok.length;$('.score .bar i').style.width=`${ans.length/all.length*100}%`;$('.score small').textContent=`${ans.length} dari ${all.length} sudah dijawab`;$('#stReset').disabled=false});
  $('#stReset').onclick=()=>{all.forEach(x=>delete storyAns[x.key]);store.set('rk-story2',storyAns);route()};
}

/* ===================== GLOSARIUM ===================== */
const GLUSE={};
for(const n in TOPICS)TOPICS[n].forEach((tp,ti)=>{for(const k in tp.legend){const id=tp.legend[k][0];(GLUSE[id]=GLUSE[id]||[]);if(!GLUSE[id].some(u=>u.n==n&&u.ti===ti))GLUSE[id].push({n:+n,ti,k,t:tp.t})}});
const topicLesson=(n,ti)=>FLAT.java.find(x=>x.l.k==='topic'&&x.l.ref===n+'.'+ti)||FLAT.python.find(x=>x.l.k==='topic'&&x.l.ref===n+'.'+ti);
const labLesson=n=>FLAT.java.find(x=>x.l.k==='lab'&&x.l.n===n);
function renderGlossary(){
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span><span>Glosarium</span></nav><div class="eyebrow">Kamus</div><h1>Glosarium istilah</h1>
  <p class="lead muted">${GL.length} istilah pemrograman dan basis data, lengkap dengan padanan bahasa Inggrisnya. Tombol "Tunjukkan di kode" membawamu ke bagian kode yang dimaksud.</p></header>
  <div class="gl-tools"><input class="gl-search" id="glq" type="search" placeholder="Cari istilah, misalnya rekursi, JOIN, atau polymorphism" aria-label="Cari istilah"></div>
  <div class="chips" id="glc">${['Semua',...CATS].map(k=>`<button class="chip" data-c="${k}" aria-pressed="false">${k}</button>`).join('')}</div>
  <div class="gl-list" id="gll"></div>`;
}
function drawGlossary(){
  const q=glState.q.trim().toLowerCase();
  document.querySelectorAll('#glc .chip').forEach(b=>b.setAttribute('aria-pressed',b.dataset.c===glState.cat));
  const list=GL.filter(g=>(glState.cat==='Semua'||g.c===glState.cat)&&(!q||(g.t+' '+g.en+' '+g.d).toLowerCase().includes(q))).sort((a,b)=>a.t.localeCompare(b.t,'id'));
  $('#gll').innerHTML=list.length?list.map(g=>{const s=CH.filter(c=>c.terms.includes(g.id)),u=(GLUSE[g.id]||[]).slice(0,4).filter(x=>topicLesson(x.n,x.ti));
    return `<article class="gl" id="t-${g.id}"><span class="cat">${g.c}</span><h3>${g.t}<small>${g.en}</small></h3><p>${esc(g.d)}</p>${g.ex?`<pre>${esc(g.ex)}</pre>`:''}${u.length?`<div class="show-in"><span>Tunjukkan di kode:</span>${u.map(x=>`<button class="show" data-n="${x.n}" data-ti="${x.ti}" data-k="${x.k}">${esc(x.t)}</button>`).join('')}</div>`:''}${s.length?`<div class="seen">Dibahas di: ${s.map(c=>{const x=labLesson(c.n);return x?`<a href="#${x.id}">${esc(c.t)}</a>`:''}).join('')}</div>`:''}</article>`}).join('')
    :`<p class="empty">Tidak ada istilah yang cocok dengan "${esc(glState.q)}". Coba kata lain atau pilih kategori Semua.</p>`;
}
function wireGlossary(){
  const inp=$('#glq');inp.value=glState.q;
  inp.addEventListener('input',()=>{glState.q=inp.value;glState.focus=null;drawGlossary()});
  $('#glc').addEventListener('click',e=>{const b=e.target.closest('.chip');if(!b)return;glState.cat=b.dataset.c;drawGlossary()});
  $('#gll').addEventListener('click',e=>{const b=e.target.closest('.show');if(!b)return;const x=topicLesson(+b.dataset.n,+b.dataset.ti);if(!x)return;pendingFocus={k:b.dataset.k};
    if(location.hash==='#'+x.id)route();else location.hash=x.id});
  drawGlossary();
  if(glState.focus){const el=document.getElementById('t-'+glState.focus);if(el){el.classList.add('flash');el.scrollIntoView({block:'center'});setTimeout(()=>el.classList.remove('flash'),2200)}glState.focus=null}
}
