/* ===================== GLOSARIUM & ISTILAH DI PELAJARAN =====================
   Daftar istilah dimuat bersama inti aplikasi agar istilah di setiap pelajaran bisa disentuh
   untuk melihat artinya tanpa membuka halaman glosarium. */
/* ===================== GLOSARIUM ===================== */
const CATS = ['Dasar','Alur Kontrol','Fungsi & Data','OOP','Struktur Data','Algoritma','Fungsional','Alat & Proses'];
const GL = [
{id:'algoritma',t:'Algoritma',en:'algorithm',c:'Dasar',d:'Langkah-langkah terurut dan jelas untuk menyelesaikan suatu masalah. Program adalah algoritma yang ditulis dalam bahasa pemrograman.'},
{id:'pseudocode',t:'Pseudocode',en:'pseudocode',c:'Alat & Proses',d:'Rancangan algoritma dalam bahasa campuran manusia dan kode, tanpa aturan sintaks ketat. Dipakai untuk berpikir sebelum menulis kode sungguhan.'},
{id:'sintaks',t:'Sintaks',en:'syntax',c:'Dasar',d:'Aturan tata tulis sebuah bahasa pemrograman, misalnya letak titik koma atau indentasi. Melanggarnya menghasilkan error sintaks.'},
{id:'semantik',t:'Semantik',en:'semantics',c:'Dasar',d:'Makna atau perilaku dari kode yang sintaksnya benar. Kode bisa benar secara sintaks tetapi salah secara semantik.'},
{id:'statement',t:'Statement',en:'statement',c:'Dasar',d:'Satu instruksi lengkap yang dijalankan komputer, misalnya mencetak teks atau mengisi variabel.',ex:`System.out.println("Hai");   // Java
print("Hai")                  # Python`},
{id:'komentar',t:'Komentar',en:'comment',c:'Dasar',d:'Catatan di dalam kode untuk manusia. Diabaikan oleh compiler atau interpreter.',ex:`// komentar Java
# komentar Python`},
{id:'compiler',t:'Compiler',en:'compiler',c:'Alat & Proses',d:'Program yang menerjemahkan seluruh kode sumber ke bentuk lain (misalnya bytecode) sebelum dijalankan. Java memakai compiler javac.'},
{id:'interpreter',t:'Interpreter',en:'interpreter',c:'Alat & Proses',d:'Program yang membaca dan menjalankan kode secara langsung tanpa langkah kompilasi terpisah. Python dijalankan oleh interpreter.'},
{id:'bytecode',t:'Bytecode',en:'bytecode',c:'Alat & Proses',d:'Kode perantara hasil kompilasi Java (file .class). Bukan kode mesin, sehingga bisa dijalankan di sistem operasi apa pun yang punya JVM.'},
{id:'jvm',t:'JVM',en:'Java Virtual Machine',c:'Alat & Proses',d:'Mesin virtual yang menjalankan bytecode Java. Berkat JVM, program Java bersifat "tulis sekali, jalan di mana saja".'},
{id:'ide',t:'IDE',en:'integrated development environment',c:'Alat & Proses',d:'Aplikasi untuk menulis, menjalankan, dan men-debug kode di satu tempat. Contoh: IntelliJ IDEA, VS Code, PyCharm, jGRASP.'},
{id:'debugging',t:'Debugging',en:'debugging',c:'Alat & Proses',d:'Proses mencari dan memperbaiki bug. Bisa dengan mencetak nilai variabel atau memakai debugger untuk menjalankan kode baris per baris.'},
{id:'bug',t:'Bug',en:'bug',c:'Alat & Proses',d:'Kesalahan dalam program yang membuatnya berperilaku tidak sesuai harapan.'},
{id:'error-sintaks',t:'Error sintaks',en:'syntax error',c:'Alat & Proses',d:'Kesalahan tata tulis, misalnya kurung tidak ditutup. Di Java terdeteksi saat kompilasi, di Python saat file mulai dijalankan.'},
{id:'runtime-error',t:'Runtime error',en:'runtime error',c:'Alat & Proses',d:'Kesalahan yang muncul saat program sedang berjalan, misalnya membagi dengan nol atau indeks di luar batas.'},
{id:'logic-error',t:'Logic error',en:'logic error',c:'Alat & Proses',d:'Program berjalan tanpa error tetapi hasilnya salah, misalnya memakai + padahal seharusnya *. Paling sulit dilacak.'},
{id:'dekomposisi',t:'Dekomposisi prosedural',en:'procedural decomposition',c:'Fungsi & Data',d:'Memecah masalah besar menjadi method atau fungsi kecil yang masing-masing punya satu tugas.'},
{id:'method',t:'Method / Fungsi',en:'method / function',c:'Fungsi & Data',d:'Blok kode bernama yang bisa dipanggil berulang kali. Di Java disebut method (selalu di dalam kelas). Di Python disebut fungsi bila berdiri sendiri.',ex:`public static void sapa() { ... }   // Java
def sapa(): ...                      # Python`},
{id:'variabel',t:'Variabel',en:'variable',c:'Dasar',d:'Nama untuk lokasi memori yang menyimpan sebuah nilai. Nilainya bisa diubah selama program berjalan.',ex:`int umur = 20;    // Java
umur = 20         # Python`},
{id:'tipe-data',t:'Tipe data',en:'data type',c:'Dasar',d:'Jenis nilai yang disimpan dan operasi yang boleh dilakukan padanya, misalnya bilangan bulat, pecahan, teks, atau boolean.'},
{id:'primitif',t:'Tipe primitif',en:'primitive type',c:'Dasar',d:'Tipe data dasar bawaan Java yang bukan objek: int, double, boolean, char, long, dan lainnya. Python tidak punya tipe primitif karena semua nilai adalah objek.'},
{id:'boolean',t:'Boolean',en:'boolean',c:'Dasar',d:'Tipe dengan dua nilai saja: benar atau salah. Java menulis true/false, Python menulis True/False.'},
{id:'char',t:'Char',en:'character',c:'Dasar',d:'Tipe Java untuk satu karakter, ditulis dengan kutip tunggal: \'A\'. Python tidak punya tipe char; satu karakter adalah string sepanjang 1.'},
{id:'string',t:'String',en:'string',c:'Fungsi & Data',d:'Rangkaian karakter atau teks. Di Java dan Python, string tidak bisa diubah (immutable); setiap operasi menghasilkan string baru.'},
{id:'literal',t:'Literal',en:'literal',c:'Dasar',d:'Nilai yang ditulis langsung di kode, seperti 42, 3.14, "halo", atau true.'},
{id:'ekspresi',t:'Ekspresi',en:'expression',c:'Dasar',d:'Gabungan nilai, variabel, dan operator yang menghasilkan sebuah nilai, misalnya (a + b) * 2.'},
{id:'operator',t:'Operator',en:'operator',c:'Dasar',d:'Simbol yang melakukan operasi pada nilai: aritmetika (+ - * /), perbandingan (< ==), dan logika (&& / and).'},
{id:'modulus',t:'Modulus (%)',en:'modulus / remainder',c:'Dasar',d:'Operator sisa bagi. 17 % 5 menghasilkan 2. Sering dipakai untuk mengecek genap/ganjil atau mengambil digit terakhir.',ex:`n % 2 == 0   // genap?`},
{id:'precedence',t:'Precedence',en:'operator precedence',c:'Dasar',d:'Urutan prioritas operator. Perkalian, pembagian, dan modulus dikerjakan sebelum penjumlahan dan pengurangan. Pakai kurung untuk memperjelas.'},
{id:'casting',t:'Casting',en:'type casting',c:'Dasar',d:'Mengubah nilai dari satu tipe ke tipe lain.',ex:`double d = (double) 7 / 2;   // Java -> 3.5
x = int("42")                # Python`},
{id:'assignment',t:'Assignment',en:'assignment',c:'Dasar',d:'Memberi nilai ke variabel dengan tanda =. Bukan "sama dengan" dalam arti matematika. x = x + 1 berarti "nilai baru x adalah x lama ditambah 1".'},
{id:'increment',t:'Increment',en:'increment',c:'Dasar',d:'Menambah nilai variabel sebanyak 1. Java: x++. Python: x += 1.'},
{id:'konstanta',t:'Konstanta',en:'constant',c:'Dasar',d:'Variabel yang nilainya tidak boleh berubah. Java memakai kata kunci final. Python memakai konvensi nama HURUF_BESAR.',ex:`public static final int MAKS = 10;   // Java
MAKS = 10                            # Python`},
{id:'perulangan',t:'Perulangan (loop)',en:'loop',c:'Alur Kontrol',d:'Struktur yang menjalankan blok kode berulang kali selama kondisi tertentu terpenuhi.'},
{id:'for',t:'For loop',en:'for loop',c:'Alur Kontrol',d:'Perulangan pasti, dipakai saat jumlah pengulangan sudah diketahui.',ex:`for (int i = 0; i < 5; i++) { }   // Java
for i in range(5): ...           # Python`},
{id:'nested-loop',t:'Nested loop',en:'nested loop',c:'Alur Kontrol',d:'Loop di dalam loop. Loop dalam berjalan penuh untuk setiap satu putaran loop luar. Cocok untuk pola baris dan kolom.'},
{id:'while',t:'While loop',en:'while loop',c:'Alur Kontrol',d:'Perulangan tak pasti yang terus berjalan selama kondisinya benar. Kondisi dicek sebelum setiap putaran.',ex:`while (x > 0) { x--; }   // Java
while x > 0: x -= 1     # Python`},
{id:'do-while',t:'Do-while',en:'do/while loop',c:'Alur Kontrol',d:'Variasi while di Java yang mengecek kondisi di akhir, sehingga badan loop dijalankan minimal sekali. Python tidak memilikinya.'},
{id:'perulangan-tak-hingga',t:'Perulangan tak hingga',en:'infinite loop',c:'Alur Kontrol',d:'Loop yang tidak pernah berhenti karena kondisinya tidak pernah menjadi salah. Biasanya bug, kadang disengaja dengan break di dalamnya.'},
{id:'fencepost',t:'Masalah fencepost',en:'fencepost problem',c:'Alur Kontrol',d:'Situasi n bagian dengan n-1 pemisah, seperti tiang dan kawat pagar. Solusinya: tangani satu bagian di luar loop.',ex:`System.out.print(1);
for (int i = 2; i <= 5; i++) System.out.print(", " + i);`},
{id:'sentinel',t:'Sentinel',en:'sentinel value',c:'Alur Kontrol',d:'Nilai khusus yang menandai akhir data, misalnya "ketik -1 untuk berhenti".'},
{id:'kondisional',t:'Kondisional (if/else)',en:'conditional',c:'Alur Kontrol',d:'Struktur yang menjalankan kode berbeda tergantung benar atau salahnya suatu kondisi.'},
{id:'operator-relasional',t:'Operator relasional',en:'relational operator',c:'Alur Kontrol',d:'Operator pembanding yang menghasilkan boolean: <, >, <=, >=, ==, !=.'},
{id:'logika-boolean',t:'Logika boolean',en:'boolean logic',c:'Alur Kontrol',d:'Menggabungkan kondisi dengan AND, OR, dan NOT. Java: && || !. Python: and or not.'},
{id:'short-circuit',t:'Short-circuit',en:'short-circuit evaluation',c:'Alur Kontrol',d:'Evaluasi berhenti begitu hasil sudah pasti. Pada a && b, jika a salah maka b tidak dievaluasi. Berguna untuk mencegah error, misalnya x != 0 && 10 / x > 1.'},
{id:'blok',t:'Blok',en:'block',c:'Dasar',d:'Kumpulan statement yang dikelompokkan. Java memakai kurung kurawal, Python memakai indentasi.'},
{id:'algoritma-kumulatif',t:'Algoritma kumulatif',en:'cumulative algorithm',c:'Algoritma',d:'Pola menghitung hasil secara bertahap: siapkan penampung di luar loop, lalu perbarui di setiap putaran.',ex:`total = 0
for x in data:
    total += x`},
{id:'pseudorandom',t:'Bilangan acak semu',en:'pseudorandom number',c:'Fungsi & Data',d:'Angka yang tampak acak tetapi dihasilkan oleh rumus matematis dari sebuah seed. Java: Random. Python: modul random.'},
{id:'parameter',t:'Parameter',en:'parameter',c:'Fungsi & Data',d:'Variabel di definisi method yang menerima nilai dari pemanggil.',ex:`double luas(double r)   // r adalah parameter`},
{id:'argumen',t:'Argumen',en:'argument',c:'Fungsi & Data',d:'Nilai nyata yang dikirim saat memanggil method. Pada luas(5), angka 5 adalah argumen.'},
{id:'return',t:'Return',en:'return value',c:'Fungsi & Data',d:'Nilai yang dikirim balik oleh method ke pemanggilnya. Statement return juga langsung menghentikan method.'},
{id:'scope',t:'Scope',en:'scope',c:'Fungsi & Data',d:'Wilayah kode tempat sebuah variabel bisa dipakai. Variabel yang dideklarasikan di dalam method atau blok hanya hidup di sana.'},
{id:'call-stack',t:'Call stack',en:'call stack',c:'Fungsi & Data',d:'Tumpukan bingkai (frame) untuk setiap method yang sedang berjalan. Pemanggilan baru ditumpuk di atas, dan dibuang saat method selesai.'},
{id:'library',t:'Library / API',en:'library / API',c:'Alat & Proses',d:'Kumpulan kode siap pakai yang disediakan bahasa atau pihak lain, misalnya Math, Scanner, atau modul math. API adalah daftar cara memakainya.'},
{id:'package-modul',t:'Package / Modul',en:'package / module',c:'Alat & Proses',d:'Cara mengelompokkan kode. Java memakai package dan import. Python memakai modul (satu file .py) dan import.',ex:`import java.util.Scanner;   // Java
import math                  # Python`},
{id:'scanner',t:'Scanner',en:'Scanner',c:'Fungsi & Data',d:'Kelas Java untuk membaca masukan dari keyboard, file, atau string, token demi token atau baris demi baris.'},
{id:'objek',t:'Objek',en:'object',c:'OOP',d:'Entitas yang menggabungkan data (state) dan perilaku (method). Dibuat dari sebuah kelas.'},
{id:'file-io',t:'File I/O',en:'file input/output',c:'Fungsi & Data',d:'Membaca data dari file dan menulis data ke file.'},
{id:'token',t:'Token',en:'token',c:'Fungsi & Data',d:'Potongan masukan yang dipisahkan spasi. Baris "Budi 85 90" terdiri dari tiga token.'},
{id:'exception',t:'Exception',en:'exception',c:'Fungsi & Data',d:'Objek yang mewakili kesalahan saat program berjalan. Bisa dilempar (throw/raise) dan ditangkap (catch/except).',ex:`try { ... } catch (Exception e) { ... }   // Java
try: ... except ValueError: ...          # Python`},
{id:'checked-exception',t:'Checked exception',en:'checked exception',c:'Fungsi & Data',d:'Exception di Java yang wajib ditangani atau dideklarasikan dengan throws, misalnya FileNotFoundException. Python tidak punya konsep ini.'},
{id:'array',t:'Array',en:'array',c:'Struktur Data',d:'Kumpulan elemen bertipe sama dengan ukuran tetap, diakses lewat indeks.',ex:`int[] a = new int[5];`},
{id:'list',t:'List',en:'list',c:'Struktur Data',d:'Koleksi berurutan yang boleh berisi duplikat. Di Python, list bisa tumbuh dan boleh berisi tipe campuran. Di Java, List adalah interface dengan implementasi ArrayList dan LinkedList.'},
{id:'indeks',t:'Indeks',en:'index',c:'Struktur Data',d:'Nomor posisi elemen, dimulai dari 0.'},
{id:'traversal',t:'Traversal',en:'traversal',c:'Algoritma',d:'Mengunjungi setiap elemen struktur data satu per satu, misalnya dengan loop pada array atau rekursi pada pohon.'},
{id:'off-by-one',t:'Off-by-one',en:'off-by-one error',c:'Alat & Proses',d:'Bug karena batas loop meleset satu, misalnya memakai <= padahal seharusnya <.'},
{id:'referensi',t:'Referensi',en:'reference',c:'OOP',d:'Nilai yang menunjuk ke objek di memori, bukan objek itu sendiri. Dua variabel bisa mereferensikan objek yang sama.'},
{id:'null',t:'Null / None',en:'null',c:'OOP',d:'Nilai khusus yang berarti "tidak menunjuk objek apa pun". Memanggil method pada null menyebabkan NullPointerException (Java) atau AttributeError (Python).'},
{id:'kelas',t:'Kelas',en:'class',c:'OOP',d:'Cetak biru yang mendefinisikan field dan method untuk objek-objek jenis tertentu.'},
{id:'instance',t:'Instance',en:'instance',c:'OOP',d:'Satu objek konkret dari sebuah kelas. p = new Titik(1, 2) membuat instance Titik.'},
{id:'field',t:'Field / Atribut',en:'field / attribute',c:'OOP',d:'Variabel milik objek yang menyimpan state-nya. Setiap instance punya salinan sendiri.'},
{id:'konstruktor',t:'Konstruktor',en:'constructor',c:'OOP',d:'Method khusus yang dijalankan saat objek dibuat untuk mengisi nilai awal. Java: nama sama dengan kelas. Python: __init__.'},
{id:'this-self',t:'this / self',en:'this / self',c:'OOP',d:'Referensi ke objek yang sedang menjalankan method. Java: this. Python: self, yang wajib menjadi parameter pertama.'},
{id:'enkapsulasi',t:'Enkapsulasi',en:'encapsulation',c:'OOP',d:'Menyembunyikan detail internal objek dan hanya membuka method tertentu. Melindungi data agar tetap valid.'},
{id:'getter-setter',t:'Getter / Setter',en:'accessor / mutator',c:'OOP',d:'Method untuk membaca (getter) dan mengubah (setter) field privat secara terkendali.'},
{id:'tostring',t:'toString / __str__',en:'string representation',c:'OOP',d:'Method yang menentukan teks objek saat dicetak.'},
{id:'pewarisan',t:'Pewarisan',en:'inheritance',c:'OOP',d:'Membuat kelas baru (subclass) yang mewarisi field dan method kelas lain (superclass), lalu menambah atau mengubahnya.'},
{id:'superclass',t:'Superclass',en:'superclass / parent class',c:'OOP',d:'Kelas induk yang diwarisi.'},
{id:'subclass',t:'Subclass',en:'subclass / child class',c:'OOP',d:'Kelas anak yang mewarisi superclass.'},
{id:'override',t:'Override',en:'method overriding',c:'OOP',d:'Subclass menulis ulang method induk dengan nama dan parameter yang sama untuk mengganti perilakunya.'},
{id:'overload',t:'Overload',en:'method overloading',c:'OOP',d:'Beberapa method dengan nama sama tetapi parameter berbeda dalam satu kelas. Didukung Java, tidak didukung Python secara langsung.'},
{id:'polimorfisme',t:'Polimorfisme',en:'polymorphism',c:'OOP',d:'Kemampuan kode yang sama bekerja dengan objek dari berbagai kelas, dan setiap objek merespons sesuai kelasnya sendiri.'},
{id:'interface',t:'Interface',en:'interface',c:'OOP',d:'Kontrak berisi daftar method yang wajib disediakan kelas yang mengimplementasikannya.'},
{id:'kelas-abstrak',t:'Kelas abstrak',en:'abstract class',c:'OOP',d:'Kelas yang tidak bisa dibuat objeknya langsung. Boleh berisi method lengkap dan method abstrak yang wajib di-override.'},
{id:'duck-typing',t:'Duck typing',en:'duck typing',c:'OOP',d:'Gaya Python: yang penting objek punya method yang dibutuhkan, bukan apa kelasnya. "Kalau berjalan dan bersuara seperti bebek, anggap saja bebek."'},
{id:'arraylist',t:'ArrayList',en:'ArrayList',c:'Struktur Data',d:'Implementasi List di Java berbasis array yang bisa membesar otomatis.'},
{id:'generics',t:'Generics',en:'generics',c:'Struktur Data',d:'Fitur Java untuk menentukan tipe isi koleksi, misalnya ArrayList<String>, sehingga kesalahan tipe ketahuan saat kompilasi.'},
{id:'wrapper-class',t:'Wrapper class',en:'wrapper class',c:'Struktur Data',d:'Kelas objek pembungkus tipe primitif: Integer untuk int, Double untuk double, Boolean untuk boolean, Character untuk char.'},
{id:'autoboxing',t:'Autoboxing',en:'autoboxing',c:'Struktur Data',d:'Konversi otomatis Java antara tipe primitif dan wrapper-nya, misalnya int ke Integer saat dimasukkan ke ArrayList.'},
{id:'collection',t:'Collection',en:'collection',c:'Struktur Data',d:'Objek yang menyimpan sekumpulan elemen, seperti List, Set, Map, Stack, dan Queue.'},
{id:'set',t:'Set',en:'set',c:'Struktur Data',d:'Koleksi tanpa duplikat dengan pengecekan keanggotaan yang cepat.',ex:`Set<String> s = new HashSet<>();   // Java
s = set()                          # Python`},
{id:'map',t:'Map / Dictionary',en:'map / dictionary',c:'Struktur Data',d:'Koleksi pasangan kunci dan nilai. Setiap kunci unik.',ex:`Map<String, Integer> m = new HashMap<>();   // Java
m = {"ani": 20}                             # Python`},
{id:'iterator',t:'Iterator',en:'iterator',c:'Struktur Data',d:'Objek untuk menjelajahi elemen koleksi satu per satu. For-each memakai iterator di belakang layar.'},
{id:'adt',t:'Abstract data type',en:'abstract data type (ADT)',c:'Struktur Data',d:'Spesifikasi sekumpulan data beserta operasinya tanpa menentukan cara implementasinya. Contoh: List, Stack, Queue.'},
{id:'rekursi',t:'Rekursi',en:'recursion',c:'Algoritma',d:'Teknik di mana fungsi memanggil dirinya sendiri untuk menyelesaikan versi masalah yang lebih kecil.'},
{id:'base-case',t:'Base case',en:'base case',c:'Algoritma',d:'Kasus paling sederhana dalam rekursi yang dijawab langsung tanpa memanggil diri sendiri. Tanpanya rekursi tidak berhenti.'},
{id:'recursive-case',t:'Recursive case',en:'recursive case',c:'Algoritma',d:'Bagian rekursi yang memecah masalah dan memanggil diri sendiri dengan input yang lebih kecil.'},
{id:'stack-overflow',t:'Stack overflow',en:'stack overflow',c:'Algoritma',d:'Error ketika call stack penuh, biasanya karena rekursi tanpa base case atau terlalu dalam.'},
{id:'backtracking',t:'Backtracking',en:'recursive backtracking',c:'Algoritma',d:'Teknik mencoba pilihan satu per satu secara rekursif dan mundur bila pilihan itu buntu. Dipakai untuk sudoku, labirin, dan teka-teki.'},
{id:'pencarian-linear',t:'Pencarian linear',en:'linear search',c:'Algoritma',d:'Memeriksa elemen satu per satu dari awal sampai ketemu. O(n).'},
{id:'binary-search',t:'Binary search',en:'binary search',c:'Algoritma',d:'Pencarian pada data terurut dengan membandingkan elemen tengah lalu membuang separuh data. O(log n).'},
{id:'big-o',t:'Notasi Big-O',en:'Big-O notation',c:'Algoritma',d:'Cara menyatakan pertumbuhan waktu atau memori algoritma terhadap ukuran data n, misalnya O(1), O(log n), O(n), O(n²).'},
{id:'sorting',t:'Sorting',en:'sorting',c:'Algoritma',d:'Menyusun data menurut urutan tertentu, misalnya dari kecil ke besar.'},
{id:'selection-sort',t:'Selection sort',en:'selection sort',c:'Algoritma',d:'Pengurutan dengan berulang kali memilih elemen terkecil dari sisa data lalu menukarnya ke depan. O(n²).'},
{id:'merge-sort',t:'Merge sort',en:'merge sort',c:'Algoritma',d:'Pengurutan rekursif: bagi dua, urutkan tiap bagian, lalu gabungkan. O(n log n).'},
{id:'stack',t:'Stack',en:'stack',c:'Struktur Data',d:'Koleksi LIFO (last in, first out). Operasi utamanya push, pop, dan peek.'},
{id:'queue',t:'Queue',en:'queue',c:'Struktur Data',d:'Koleksi FIFO (first in, first out). Elemen ditambah di belakang dan diambil dari depan.'},
{id:'deque',t:'Deque',en:'double-ended queue',c:'Struktur Data',d:'Antrean yang bisa ditambah dan diambil dari kedua ujung. Java: ArrayDeque. Python: collections.deque.'},
{id:'kapasitas',t:'Kapasitas',en:'capacity',c:'Struktur Data',d:'Panjang array internal sebuah koleksi, berbeda dengan size yaitu jumlah elemen yang benar-benar terisi.'},
{id:'precondition',t:'Precondition',en:'precondition / postcondition',c:'Alat & Proses',d:'Precondition adalah syarat yang harus benar sebelum method dipanggil. Postcondition adalah janji tentang keadaan setelah method selesai.'},
{id:'linked-list',t:'Linked list',en:'linked list',c:'Struktur Data',d:'Struktur data berupa rantai node yang saling menunjuk lewat referensi next.'},
{id:'node',t:'Node',en:'node',c:'Struktur Data',d:'Satu unit dalam linked list atau pohon yang berisi data dan referensi ke node lain.'},
{id:'binary-tree',t:'Pohon biner',en:'binary tree',c:'Struktur Data',d:'Struktur bercabang di mana setiap node punya paling banyak dua anak: kiri dan kanan.'},
{id:'akar-daun',t:'Akar & daun',en:'root & leaf',c:'Struktur Data',d:'Akar (root) adalah node paling atas pohon. Daun (leaf) adalah node tanpa anak.'},
{id:'bst',t:'Binary search tree',en:'binary search tree (BST)',c:'Struktur Data',d:'Pohon biner dengan aturan: nilai di subpohon kiri lebih kecil, di kanan lebih besar. Pencarian rata-rata O(log n).'},
{id:'hashing',t:'Hashing',en:'hashing',c:'Struktur Data',d:'Mengubah kunci menjadi angka (hash code) untuk menentukan lokasi penyimpanannya.'},
{id:'hash-table',t:'Hash table',en:'hash table',c:'Struktur Data',d:'Struktur data array of buckets yang memakai hashing sehingga tambah, hapus, dan cari rata-rata O(1). Dasar HashMap dan dict.'},
{id:'collision',t:'Collision',en:'hash collision',c:'Struktur Data',d:'Dua kunci berbeda menghasilkan indeks bucket yang sama. Ditangani dengan chaining atau probing.'},
{id:'heap',t:'Heap',en:'heap',c:'Struktur Data',d:'Pohon biner lengkap di mana setiap induk lebih kecil (min-heap) atau lebih besar (max-heap) dari anaknya. Biasanya disimpan dalam array.'},
{id:'priority-queue',t:'Priority queue',en:'priority queue',c:'Struktur Data',d:'Antrean yang selalu mengeluarkan elemen dengan prioritas tertinggi lebih dulu, bukan yang datang pertama.'},
{id:'fungsional',t:'Pemrograman fungsional',en:'functional programming',c:'Fungsional',d:'Gaya pemrograman yang menyusun program dari fungsi-fungsi murni dan menghindari perubahan state.'},
{id:'lambda',t:'Lambda',en:'lambda expression',c:'Fungsional',d:'Fungsi tanpa nama yang ditulis ringkas di tempat ia dipakai.',ex:`x -> x * 2           // Java
lambda x: x * 2      # Python`},
{id:'higher-order',t:'Higher-order function',en:'higher-order function',c:'Fungsional',d:'Fungsi yang menerima fungsi lain sebagai argumen atau mengembalikan fungsi. Contoh: map, filter, sorted(key=...).'},
{id:'map-filter-reduce',t:'Map, filter, reduce',en:'map / filter / reduce',c:'Fungsional',d:'Tiga operasi dasar: map mengubah setiap elemen, filter menyaring elemen, reduce menggabungkan semua elemen menjadi satu nilai.'},
{id:'stream',t:'Stream',en:'stream',c:'Fungsional',d:'API Java 8 untuk memproses koleksi secara berantai dan deklaratif: list.stream().filter(...).map(...).'},
{id:'pure-function',t:'Fungsi murni',en:'pure function',c:'Fungsional',d:'Fungsi yang hasilnya hanya bergantung pada input dan tidak punya efek samping.'},
{id:'side-effect',t:'Efek samping',en:'side effect',c:'Fungsional',d:'Perubahan di luar fungsi, seperti mengubah variabel global, mencetak ke layar, atau menulis file.'},
{id:'immutable',t:'Immutable / mutable',en:'immutable / mutable',c:'Fungsional',d:'Objek immutable tidak bisa diubah setelah dibuat (String, tuple). Objek mutable bisa diubah (ArrayList, list).'},
{id:'javadoc',t:'Javadoc / Docstring',en:'documentation comment',c:'Alat & Proses',d:'Komentar dokumentasi resmi. Java memakai /** ... */ yang bisa diubah menjadi halaman HTML. Python memakai string """...""" di baris pertama fungsi.'},
{id:'gui',t:'GUI',en:'graphical user interface',c:'Alat & Proses',d:'Antarmuka berupa jendela, tombol, dan gambar. Java: Swing/JavaFX. Python: tkinter.'},
{id:'refactoring',t:'Refactoring',en:'refactoring',c:'Alat & Proses',d:'Merapikan struktur kode tanpa mengubah perilakunya, misalnya memecah method panjang atau mengganti nama variabel.'},
{id:'version-control',t:'Version control (Git)',en:'version control',c:'Alat & Proses',d:'Sistem pencatat riwayat perubahan kode sehingga kamu bisa kembali ke versi lama dan bekerja bersama orang lain.'},
{id:'unit-test',t:'Unit test',en:'unit testing',c:'Alat & Proses',d:'Kode kecil yang menguji satu method atau fungsi secara otomatis. Java: JUnit. Python: unittest atau pytest.'}
];
const GLMAP = Object.fromEntries(GL.map(g=>[g.id,g]));

/* istilah basis data */
CATS.push('Basis Data');
[['sql-rdbms','Basis data relasional','relational database (RDBMS)','Basis data yang menyimpan data dalam tabel-tabel yang saling terhubung lewat kunci. Contoh: PostgreSQL, MySQL, SQLite, SQL Server, Oracle.'],
 ['sql-query','Query','query','Perintah untuk meminta atau mengubah data di basis data, ditulis dalam SQL.','SELECT nama FROM pelanggan;'],
 ['sql-tabel','Tabel, baris, kolom','table, row, column','Tabel menyimpan data sejenis. Setiap baris adalah satu catatan, setiap kolom satu atribut dengan tipe data tertentu.'],
 ['sql-pk','Primary key','primary key','Kolom (atau gabungan kolom) yang nilainya unik dan tidak boleh NULL, dipakai untuk menunjuk satu baris dengan pasti.','id INTEGER PRIMARY KEY'],
 ['sql-fk','Foreign key','foreign key','Kolom yang menunjuk primary key di tabel lain. Database menolak nilai yang tidak punya pasangan.','pelanggan_id INTEGER REFERENCES pelanggan(id)'],
 ['sql-constraint','Constraint','constraint','Aturan yang dijaga database: NOT NULL, UNIQUE, CHECK, PRIMARY KEY, FOREIGN KEY, DEFAULT.','harga INTEGER CHECK (harga > 0)'],
 ['sql-null','NULL (SQL)','NULL','Penanda nilai yang tidak diketahui atau tidak ada. Bukan 0 dan bukan teks kosong. Diperiksa dengan IS NULL, bukan = NULL.','WHERE kota IS NULL'],
 ['sql-ddl','DDL dan DML','data definition / manipulation language','DDL mengatur struktur (CREATE, ALTER, DROP). DML mengubah isi data (INSERT, UPDATE, DELETE). DQL membaca data (SELECT).'],
 ['sql-where','WHERE','WHERE clause','Klausa untuk menyaring baris berdasarkan kondisi sebelum dikelompokkan atau ditampilkan.','WHERE harga > 50000'],
 ['sql-agregat','Fungsi agregat','aggregate function','Fungsi yang meringkas banyak baris menjadi satu nilai: COUNT, SUM, AVG, MIN, MAX.','SELECT AVG(harga) FROM produk;'],
 ['sql-groupby','GROUP BY dan HAVING','GROUP BY / HAVING','GROUP BY mengelompokkan baris yang nilainya sama. HAVING menyaring kelompok setelah agregat dihitung.','GROUP BY kategori HAVING COUNT(*) > 1'],
 ['sql-join','JOIN','join','Menggabungkan baris dari dua tabel berdasarkan kondisi. INNER JOIN hanya yang cocok; LEFT JOIN mempertahankan semua baris tabel kiri.','FROM pesanan s JOIN pelanggan p ON s.pelanggan_id = p.id'],
 ['sql-subquery','Subquery','subquery','Query di dalam query lain, misalnya di WHERE atau FROM. Correlated subquery merujuk baris query luarnya.','WHERE harga > (SELECT AVG(harga) FROM produk)'],
 ['sql-view','View','view','Query yang disimpan dengan nama dan bisa dipakai seperti tabel. Tidak menyimpan data sendiri.','CREATE VIEW laris AS SELECT ...;'],
 ['sql-index','Index','index','Struktur data tambahan (biasanya B-tree) agar pencarian tidak perlu membaca seluruh tabel. Mempercepat baca, sedikit memperlambat tulis.','CREATE INDEX idx_kota ON pelanggan(kota);'],
 ['sql-transaksi','Transaksi','transaction','Sekelompok perintah yang diperlakukan sebagai satu kesatuan: COMMIT menyimpan semuanya, ROLLBACK membatalkan semuanya.','BEGIN; ... COMMIT;'],
 ['sql-acid','ACID','atomicity, consistency, isolation, durability','Empat jaminan transaksi: utuh (semua atau tidak sama sekali), konsisten dengan aturan, terisolasi dari transaksi lain, dan tahan lama setelah COMMIT.'],
 ['sql-normalisasi','Normalisasi','normalization','Merancang tabel agar data tidak berulang (1NF, 2NF, 3NF), dengan memecah data ke tabel terpisah yang dihubungkan foreign key.'],
 ['sql-injection','SQL injection','SQL injection','Serangan dengan menyisipkan potongan SQL lewat input pengguna. Dicegah dengan parameter (prepared statement), bukan menyambung string.'],
 ['sql-prepared','Prepared statement','prepared statement','Query dengan placeholder (?) yang nilainya dikirim terpisah, sehingga input selalu dianggap data, bukan perintah.','SELECT * FROM akun WHERE username = ?'],
 ['sql-cte','CTE','common table expression','Query bernama sementara yang ditulis dengan WITH di awal query. CTE rekursif bisa menelusuri hierarki seperti bagan organisasi.','WITH laris AS (SELECT ...) SELECT * FROM laris;'],
 ['sql-window','Window function','window function','Fungsi yang menghitung nilai dari sekelompok baris terkait tanpa menggabungkannya: ROW_NUMBER, RANK, LAG, LEAD, SUM OVER.','RANK() OVER (PARTITION BY divisi ORDER BY gaji DESC)'],
 ['sql-explain','EXPLAIN','query plan','Perintah untuk melihat rencana eksekusi query: tabel dibaca penuh (SCAN) atau lewat index (SEARCH).','EXPLAIN QUERY PLAN SELECT ...;'],
 ['sql-procedure','Stored procedure','stored procedure','Kumpulan perintah SQL yang disimpan di server database dan dipanggil dengan nama, misalnya CALL proses_gaji().']
].forEach(([id,t,en,d,ex])=>{const g={id,t,en,c:'Basis Data',d};if(ex)g.ex=ex;GL.push(g);GLMAP[id]=g});

/* istilah web, data, dan desain untuk jalur roadmap.sh */
CATS.push('Web','Data & BI','Desain');
[['web-html','HTML','HyperText Markup Language','Web','Bahasa penanda yang menyusun struktur halaman web: judul, paragraf, gambar, link, dan form.'],
 ['web-elemen','Elemen & tag','element, tag','Web','Elemen HTML ditulis dengan tag pembuka dan penutup, misalnya <p>…</p>. Isinya bisa teks atau elemen lain.'],
 ['web-atribut','Atribut HTML','attribute','Web','Keterangan tambahan pada tag, misalnya href pada <a> atau alt pada <img>.'],
 ['web-semantik','HTML semantik','semantic HTML','Web','Memakai elemen sesuai maknanya (header, nav, main, article, button) agar mudah dipahami pembaca layar dan mesin pencari.'],
 ['web-dom','DOM','Document Object Model','Web','Representasi halaman sebagai pohon objek yang bisa dibaca dan diubah JavaScript, misalnya lewat document.querySelector.'],
 ['web-css','CSS','Cascading Style Sheets','Web','Bahasa untuk mengatur tampilan halaman: warna, ukuran, jarak, dan tata letak.'],
 ['web-selector','Selector','CSS selector','Web','Pola yang memilih elemen yang akan diberi gaya, misalnya .kartu, #menu, atau nav a.'],
 ['web-boxmodel','Box model','box model','Web','Setiap elemen adalah kotak berlapis: content, padding, border, dan margin.'],
 ['web-flexbox','Flexbox','flexible box layout','Web','Tata letak satu arah (baris atau kolom) untuk menyusun dan meratakan elemen dengan mudah.'],
 ['web-grid','CSS Grid','grid layout','Web','Tata letak dua arah dengan baris dan kolom, cocok untuk kerangka halaman dan galeri.'],
 ['web-responsif','Desain responsif','responsive design','Web','Halaman yang menyesuaikan diri dengan ukuran layar, dari HP sampai monitor lebar.'],
 ['web-mediaquery','Media query','media query','Web','Aturan CSS yang hanya berlaku pada kondisi tertentu, misalnya lebar layar minimal 768px.'],
 ['web-event','Event','event','Web','Kejadian di halaman, misalnya klik, ketikan, atau halaman selesai dimuat, yang bisa ditangani dengan JavaScript.'],
 ['web-json','JSON','JavaScript Object Notation','Web','Format teks untuk bertukar data, berisi objek {kunci: nilai} dan array. Dipakai hampir semua API web.'],
 ['web-http','HTTP','Hypertext Transfer Protocol','Web','Aturan percakapan browser dan server: permintaan (GET, POST) dan jawaban dengan kode status seperti 200 atau 404.'],
 ['web-promise','Promise & async/await','promise, async/await','Web','Cara JavaScript menangani pekerjaan yang hasilnya datang belakangan, misalnya mengambil data dari server.'],
 ['web-npm','npm','Node package manager','Web','Pengelola paket JavaScript. Daftar paket proyek dicatat di package.json.'],
 ['web-komponen','Komponen','component','Web','Potongan antarmuka yang bisa dipakai ulang, misalnya Tombol atau KartuProduk di React.'],
 ['web-props','Props','props','Web','Data yang dikirim dari komponen induk ke komponen anak di React. Bersifat hanya-baca bagi anak.'],
 ['web-state','State','state','Web','Data milik komponen yang bisa berubah. Saat state berubah, React menggambar ulang tampilan.'],
 ['web-hook','Hook','React hook','Web','Fungsi khusus React yang diawali use, misalnya useState dan useEffect.'],
 ['web-tipestatis','Tipe statis','static typing','Web','Tipe variabel diperiksa sebelum program dijalankan, seperti di TypeScript dan Java, sehingga banyak kesalahan tertangkap lebih awal.'],
 ['web-aksesibilitas','Aksesibilitas','accessibility (a11y)','Web','Membuat produk bisa dipakai semua orang, termasuk pengguna pembaca layar, keyboard, atau penglihatan terbatas.'],
 ['git-commit','Commit','commit','Alat & Proses','Titik simpan riwayat di Git yang berisi perubahan dan pesan penjelasnya.'],
 ['git-branch','Branch','branch','Alat & Proses','Cabang riwayat untuk mengerjakan fitur tanpa mengganggu cabang utama.'],
 ['git-merge','Merge','merge','Alat & Proses','Menggabungkan perubahan dari satu branch ke branch lain.'],
 ['git-repo','Repositori','repository','Alat & Proses','Folder proyek beserta seluruh riwayat Git-nya. Di GitHub disebut repo.'],
 ['git-pr','Pull request','pull request','Alat & Proses','Permintaan agar perubahan di sebuah branch ditinjau lalu digabung, biasanya lewat GitHub.'],
 ['data-dataframe','DataFrame','DataFrame','Data & BI','Tabel di pandas: baris dan kolom berlabel, mirip lembar kerja spreadsheet.'],
 ['data-dataset','Dataset','dataset','Data & BI','Kumpulan data yang dianalisis, biasanya berbentuk tabel.'],
 ['data-median','Median','median','Data & BI','Nilai tengah setelah data diurutkan. Lebih tahan terhadap outlier dibanding rata-rata.'],
 ['data-outlier','Outlier','outlier','Data & BI','Nilai yang jauh berbeda dari kebanyakan data. Bisa kesalahan input, bisa juga temuan penting.'],
 ['data-korelasi','Korelasi','correlation','Data & BI','Ukuran seberapa kuat dua variabel bergerak bersama, dari -1 sampai 1. Korelasi bukan sebab-akibat.'],
 ['data-kpi','KPI','key performance indicator','Data & BI','Angka utama yang dipakai untuk menilai apakah tujuan bisnis tercapai.'],
 ['data-dashboard','Dashboard','dashboard','Data & BI','Satu layar berisi grafik dan angka penting untuk memantau kinerja.'],
 ['data-etl','ETL / ELT','extract, transform, load','Data & BI','Proses mengambil data dari sumber, membersihkan dan mengubahnya, lalu memuatnya ke gudang data.'],
 ['data-warehouse','Data warehouse','data warehouse','Data & BI','Database khusus analisis yang menyatukan data dari banyak sistem.'],
 ['data-pipeline','Pipeline data','data pipeline','Data & BI','Rangkaian langkah otomatis yang memindahkan dan mengolah data dari sumber ke tujuan.'],
 ['des-persona','Persona','persona','Desain','Gambaran tokoh pengguna yang disusun dari riset, untuk membantu tim memahami kebutuhan pengguna.'],
 ['des-wireframe','Wireframe','wireframe','Desain','Sketsa tata letak layar tanpa warna dan detail visual, untuk membahas struktur dan prioritas konten.'],
 ['des-prototipe','Prototipe','prototype','Desain','Versi tiruan produk yang bisa diklik untuk diuji sebelum dibangun.'],
 ['des-usability','Usability test','usability testing','Desain','Mengamati pengguna nyata mencoba menyelesaikan tugas dengan produk untuk menemukan bagian yang membingungkan.'],
 ['des-token','Design token','design token','Desain','Nilai desain bernama (warna, jarak, ukuran huruf) yang dipakai bersama oleh desainer dan developer.'],
 ['des-kontras','Rasio kontras','contrast ratio','Desain','Perbandingan terang teks dan latarnya. Teks biasa minimal 4.5:1 agar mudah dibaca.'],
].forEach(([id,t,en,c,d])=>{const g={id,t,en,c,d};GL.push(g);GLMAP[id]=g});

/* ---------- istilah yang bisa disentuh di pelajaran ----------
   Kemunculan pertama setiap istilah di teks pelajaran diberi garis bawah titik-titik;
   disentuh atau diklik akan menampilkan artinya. */
const GL_SKIP=new Set(['set','map','list','node','token','blok','char','heap','this','self','stream','return','literal','baris','kolom','table','element','component','objek','operator','array','string','indeks','index','query','tabel']);
let GLRX=null;
function glIndex(){
  if(GLRX)return GLRX;const al=new Map();
  GL.forEach(g=>{const names=[...g.t.replace(/\s*\(.*\)$/,'').split(/\s+\/\s+/),g.t.replace(/\s*\(.*\)$/,''),g.en];
    names.map(s=>(s||'').trim()).filter(s=>s.length>=4&&!GL_SKIP.has(s.toLowerCase())&&!/[^\w\s\-.&]/.test(s)).forEach(s=>{const k=s.toLowerCase();if(!al.has(k))al.set(k,g.id)})});
  const keys=[...al.keys()].sort((a,b)=>b.length-a.length).map(k=>k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'));
  GLRX={al,rx:new RegExp(`(^|[^\\p{L}\\p{N}_])(${keys.join('|')})(?=$|[^\\p{L}\\p{N}_])`,'iu')};return GLRX;
}
function linkTerms(root,max=8){
  if(!root)return;const {al,rx}=glIndex(),seen=new Set();let n=0;
  const walk=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:t=>t.parentElement.closest('code,pre,a,button,.gt,h1,h2,h3,summary,.pane,.quiz,textarea,.eyebrow,.trbox,.pr-sec,.pro-sec,.console,table,label')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT});
  const nodes=[];while(walk.nextNode())nodes.push(walk.currentNode);
  for(const tn of nodes){if(n>=max)break;let t=tn,m;
    while(t&&n<max&&(m=rx.exec(t.data))){const id=al.get(m[2].toLowerCase()),at=m.index+m[1].length;
      if(seen.has(id)){const rest=t.splitText(at+m[2].length);t=rest;continue}
      seen.add(id);n++;const word=t.splitText(at),rest=word.splitText(m[2].length);
      const b=document.createElement('button');b.type='button';b.className='gt';b.dataset.gt=id;b.setAttribute('aria-expanded','false');b.textContent=word.data;word.replaceWith(b);t=rest}}
}
function glPop(b){
  let p=$('#gtPop');const close=()=>{if(p){p.hidden=true;document.querySelectorAll('.gt[aria-expanded="true"]').forEach(x=>x.setAttribute('aria-expanded','false'))}};
  if(!b){close();return}
  if(!p){p=document.createElement('div');p.id='gtPop';p.className='gt-pop';p.setAttribute('role','dialog');p.hidden=true;document.body.appendChild(p)}
  const open=b.getAttribute('aria-expanded')==='true';close();if(open)return;
  const g=GLMAP[b.dataset.gt];if(!g)return;
  p.innerHTML=`<b>${esc(g.t)}</b>${g.en?`<i>${esc(g.en)}</i>`:''}<p>${esc(g.d)}</p>${g.ex?`<code>${esc(g.ex)}</code>`:''}<a href="#glosarium" data-term="${g.id}">Buka di glosarium →</a>`;
  p.hidden=false;b.setAttribute('aria-expanded','true');
  const r=b.getBoundingClientRect(),w=Math.min(320,innerWidth-24),x=Math.max(12,Math.min(r.left,innerWidth-w-12));
  p.style.width=w+'px';p.style.left=x+scrollX+'px';
  const below=r.bottom+8+p.offsetHeight<innerHeight;p.style.top=(below?r.bottom+8:r.top-8-p.offsetHeight)+scrollY+'px';
}
document.addEventListener('click',e=>{const b=e.target.closest('.gt');if(b){e.preventDefault();glPop(b);return}if(!e.target.closest('#gtPop'))glPop(null);else if(e.target.closest('a'))glPop(null)});
document.addEventListener('keydown',e=>{if(e.key==='Escape')glPop(null)});
