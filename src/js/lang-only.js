/* ===================== SATU BAHASA PER JALUR =====================
   Bab (CH) dan topik (TOPICS) di data.js dipakai bersama jalur Java dan Python, jadi teksnya
   membandingkan keduanya. Di jalur Java, perbandingan dengan Python dihapus; di jalur Python,
   perbandingan dengan Java dihapus. Kalimat diganti versi satu bahasa, dan soal kuis tentang
   bahasa lain diganti soal bahasa jalur itu.
   Kunci: b<i> paragraf, p<i> poin, q<i> soal, q<i>.o<k> pilihan, selain itu nama field (t, tip, vizT, vizD). */
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
const PFIX={
 1:{b0:'Program adalah daftar instruksi yang dijalankan komputer satu per satu. Setiap instruksi disebut <b>statement</b>. Di Python, satu baris biasanya satu statement, dan baris-baris dalam satu blok ditandai dengan <b>indentasi</b> (spasi di awal baris).',
    b1:'Python <b>diinterpretasi</b>: interpreter membaca dan menjalankan kode baris demi baris, jadi kamu cukup menjalankan <code>python halo.py</code>. Kesalahan di sebuah baris baru ketahuan saat baris itu dijalankan.',
    b2:'Begitu program bertambah panjang, pecah menjadi bagian kecil bernama <b>fungsi</b>. Teknik ini disebut dekomposisi prosedural. Setiap bagian punya satu tugas yang jelas dan bisa dipanggil berkali-kali.',
    p0:'Program Python bisa langsung berisi statement, tanpa kelas atau method <code>main</code>.',
    p2:'Komentar diawali <code>#</code> dan diabaikan komputer.',
    p3:'Nama fungsi sebaiknya kata kerja, huruf kecil dengan garis bawah: <code>cetak_laporan</code>.',
    vizD:'Ikuti jalur program Python dari kode sumber sampai tampil di layar.',
    q0:{q:'Apa yang terjadi saat kamu menjalankan <code>python halo.py</code>?',o:['Interpreter menjalankan kode baris demi baris','Muncul file Halo.class','Kode harus dikompilasi manual dulu','Tidak terjadi apa-apa'],a:0,w:'python adalah interpreter. Ia membaca halo.py lalu langsung menjalankannya dari atas ke bawah.'}},
 2:{b0:'Data disimpan di <b>variabel</b>. Python menebak <b>tipe data</b> sendiri dari nilai yang diberikan: <code>int</code> untuk bilangan bulat, <code>float</code> untuk pecahan, <code>bool</code> untuk benar/salah (<code>True</code>/<code>False</code>), dan <code>str</code> untuk teks.',
    b1:'Ekspresi seperti <code>7 / 2</code> menghasilkan 3.5, karena di Python <code>/</code> selalu menghasilkan pecahan. Untuk pembagian bulat pakai <code>//</code>, hasilnya 3. Operator <code>%</code> memberi sisa bagi dan sering dipakai untuk cek genap/ganjil.',
    b2:'<b>Perulangan pasti</b> dipakai saat jumlah pengulangan sudah diketahui. Python memakai <code>for i in range(awal, akhir)</code>, dengan <code>akhir</code> tidak ikut dihitung. Loop di dalam loop (nested loop) cocok untuk pola dua dimensi seperti segitiga bintang.',
    p0:'<code>int(x)</code>, <code>float(x)</code>, dan <code>str(x)</code> mengubah tipe sebuah nilai (konversi).',
    p3:'Konstanta ditulis HURUF_BESAR, misalnya <code>MAKS = 10</code>. Python tidak melarang mengubahnya; ini kesepakatan antarprogrammer.',
    vizD:'Ikuti cara <code>range</code> memberi nilai i satu per satu, lalu badan loop dijalankan.'},
 3:{b0:'<b>Parameter</b> membuat fungsi lebih umum. Daripada menulis <code>luas_lingkaran_jari3()</code>, tulis <code>luas(r)</code> dan kirim nilai apa pun. Nilai yang dikirim saat memanggil disebut <b>argumen</b>. Nilai yang dikirim balik memakai <code>return</code>.',
    b1:'Setiap pemanggilan fungsi mendapat ruang variabelnya sendiri di <b>call stack</b>. Variabel di dalam fungsi hanya hidup di sana. Inilah yang disebut <b>scope</b>.',
    b2:'Bab ini juga mengenalkan <b>objek</b> bawaan. String (<code>str</code>) punya method seperti <code>upper()</code> dan <code>split()</code>, dan panjangnya dihitung dengan <code>len()</code>. <code>input()</code> membaca masukan pengguna. Modul <code>math</code> menyediakan rumus siap pakai.',
    p0:'Parameter Python tidak wajib bertipe, tapi boleh diberi petunjuk tipe: <code>def luas(r: float) -&gt; float</code>.',
    p3:'String tidak bisa diubah. <code>s.upper()</code> membuat string baru.',
    tip:'Kalau satu fungsi melakukan dua hal, misalnya menghitung sekaligus mencetak, pisahkan. Fungsi yang me-return nilai lebih mudah diuji dan dipakai ulang.',
    vizT:'Call stack saat fungsi dipanggil',
    q1:{q:'Pada <code>luas(5)</code>, angka 5 disebut apa?',o:['Parameter','Argumen','Atribut','Konstanta'],a:1,w:'Argumen adalah nilai yang dikirim. Parameter adalah variabel penerimanya di definisi fungsi.'}},
 4:{b0:'Percabangan membuat program memilih. <code>if</code> menjalankan blok hanya bila kondisinya benar. Rantai <code>if / elif / else</code> dicek dari atas. Begitu satu kondisi benar, sisanya dilewati.',
    p0:'Gunakan <code>if/elif</code> bila pilihan saling eksklusif. Gunakan beberapa <code>if</code> terpisah bila boleh lebih dari satu.',
    p1:'Di Python, <code>==</code> membandingkan isi string. <code>is</code> memeriksa apakah dua nama menunjuk objek yang sama.',
    p3:'Fungsi boleh punya beberapa <code>return</code> di cabang berbeda.',
    vizT:'Jalur if / elif / else',
    q0:{q:'Dengan fungsi <code>huruf</code> di atas, berapa hasil <code>huruf(80)</code>?',o:['A','B','C','D'],a:1,w:'80 >= 90 salah, 80 >= 80 benar, jadi B. Kondisi berikutnya tidak dicek lagi.'},
    q1:{q:'Di Python, cara yang benar untuk membandingkan isi dua string adalah...',o:['a == b','a.equals(b)','a = b','a === b'],a:0,w:'== membandingkan isi string karakter demi karakter. a = b adalah pengisian, bukan perbandingan.'}},
 5:{b1:'Kondisi bisa digabung dengan <b>logika boolean</b>: AND (<code>and</code>), OR (<code>or</code>), dan NOT (<code>not</code>). <code>and</code> dan <code>or</code> memakai <b>short-circuit</b>: jika bagian kiri sudah menentukan hasil, bagian kanan tidak dievaluasi.',
    p1:'Python tidak punya <code>do/while</code>. Polanya: <code>while True:</code> lalu <code>break</code> saat syaratnya terpenuhi.',
    p2:'<code>not (a and b)</code> sama dengan <code>not a or not b</code> (hukum De Morgan).',
    p3:'<code>random.randint(1, 6)</code> memberi angka 1 sampai 6, termasuk 6.',
    q0:{q:'Apa hasil <code>True or (10 / 0 &gt; 1)</code> di Python?',o:['ZeroDivisionError','True','False','SyntaxError'],a:1,w:'Short-circuit: karena kiri sudah True, or pasti True. Bagian kanan tidak pernah dihitung.'}},
 6:{b0:'Program nyata membaca data dari file, bukan hanya dari keyboard. Di Python, gunakan <code>open()</code> di dalam blok <code>with</code> agar file otomatis ditutup.',
    b2:'Membuka file bisa gagal, misalnya karena file tidak ada. Python melempar <code>FileNotFoundError</code> yang bisa ditangkap dengan <code>try/except</code>.',
    p0:'Cek dulu dengan <code>token.isdigit()</code> sebelum <code>int(token)</code>, supaya tidak crash.',
    p2:'Menulis file: <code>open(nama, "w")</code> lalu <code>f.write(teks)</code>.',
    q0:{q:'Token berikutnya adalah "abc". Apa hasil <code>"abc".isdigit()</code>?',o:['True','False','Error','0'],a:1,w:'isdigit hanya memeriksa, tidak mengubah. "abc" bukan angka, jadi False.'}},
 7:{t:'List',
    b0:'<b>List</b> menyimpan banyak nilai di bawah satu nama. Setiap elemen punya <b>indeks</b> mulai dari 0. List 5 elemen punya indeks 0 sampai 4. Mengakses indeks 5 menghasilkan <code>IndexError</code>.',
    b1:'Pola paling umum adalah <b>traversal</b>: mengunjungi setiap elemen dengan loop untuk mencari maksimum, menjumlah, atau menghitung. <code>for x in a</code> cocok bila kamu tidak butuh indeksnya.',
    b2:'List adalah objek, jadi variabelnya menyimpan <b>referensi</b> (alamat), bukan isinya. <code>b = a</code> tidak menyalin isi. Keduanya menunjuk list yang sama, sehingga perubahan lewat <code>b</code> juga terlihat di <code>a</code>. Hal yang sama berlaku saat list dikirim sebagai parameter.',
    p0:'List bisa tumbuh: <code>a.append(x)</code> menambah elemen di akhir.',
    p2:'Cetak list langsung dengan <code>print(a)</code>.',
    p3:'List 2D: <code>m = [[0] * 4 for _ in range(3)]</code>.',
    tip:'Batas loop yang benar adalah <code>range(len(a))</code>, bukan <code>range(len(a) + 1)</code>. Kesalahan satu langkah ini disebut off-by-one.',
    vizD:'Akses elemen lewat indeks, lalu lihat apa yang terjadi saat dua variabel menunjuk list yang sama.',
    q0:{q:'List Python berisi 5 elemen. Berapa indeks elemen terakhir?',o:['5','4','6','Tidak ada'],a:1,w:'Indeks mulai dari 0, jadi elemen terakhir ada di len(a) - 1. Python juga menerima a[-1].'}},
 8:{b0:'<b>Kelas</b> adalah cetak biru. <b>Objek</b> adalah benda nyata yang dibuat dari cetak biru itu. Kelas <code>Titik</code> mendefinisikan bahwa setiap titik punya <code>x</code> dan <code>y</code> (disebut <b>atribut</b>) serta bisa <code>geser()</code> (disebut method).',
    b1:'<b>Konstruktor</b> <code>__init__</code> dijalankan saat objek dibuat dengan <code>Titik(3, 4)</code>. Tugasnya mengisi nilai awal atribut. Kata <code>self</code> merujuk ke objek yang sedang dipakai.',
    b2:'<b>Enkapsulasi</b> berarti menyembunyikan atribut (konvensinya diawali <code>_</code>) dan hanya membuka method tertentu. Dengan begitu objek bisa menjaga datanya tetap valid. Method <code>__str__</code> menentukan bagaimana objek tampil saat dicetak.',
    p0:'Setiap objek punya salinan atribut sendiri.',
    p1:'Atribut yang diawali <code>_</code> berarti internal: jangan diubah dari luar kelas.',
    p2:'Semua atribut dibuat di <code>__init__</code> lewat <code>self.nama = nilai</code>.',
    tip:'Rancang kelas dari kata benda dalam soal (Titik, Akun, Mahasiswa). Kata kerjanya menjadi method.',
    q0:{q:'Apa tugas konstruktor <code>__init__</code>?',o:['Menghapus objek','Mengisi nilai awal objek baru','Mencetak objek','Membandingkan dua objek'],a:1,w:'__init__ berjalan sekali saat objek dibuat dan menyiapkan atributnya.'},
    q1:{q:'Mengapa atribut sebaiknya diubah lewat method, bukan langsung?',o:['Supaya program lebih cepat','Supaya data hanya bisa diubah lewat method yang menjaga validitasnya','Diwajibkan Python','Supaya bisa diwarisi'],a:1,w:'Itulah enkapsulasi. Kode luar tidak mengisi nilai sembarangan.'}},
 9:{t:'Pewarisan & Kelas Abstrak',
    b0:'<b>Pewarisan</b> membuat kelas baru dari kelas yang sudah ada. <code>class Kucing(Hewan)</code> berarti Kucing otomatis punya semua atribut dan method Hewan. Kelas induk disebut <b>superclass</b>, kelas anak disebut <b>subclass</b>. Hubungannya selalu "adalah": kucing adalah hewan.',
    b1:'Subclass boleh <b>meng-override</b> method induk untuk mengganti perilakunya. Karena itu, variabel <code>h</code> bisa menunjuk Kucing atau Anjing, dan <code>h.suara()</code> menjalankan versi milik objek sebenarnya. Inilah <b>polimorfisme</b>.',
    b2:'Python tidak punya kata kunci interface. Kontraknya cukup kesepakatan: objek yang punya method yang dibutuhkan boleh dipakai. Ini disebut <b>duck typing</b>. Bila kontrak ingin dipaksa, pakai <b>kelas abstrak</b> dari modul <code>abc</code>: boleh punya method lengkap dan method abstrak, tapi tidak bisa dibuat objeknya langsung.',
    p0:'<code>super().__init__(...)</code> memanggil konstruktor induk.',
    p1:'Kelas abstrak (<code>ABC</code> dan <code>@abstractmethod</code>) memaksa subclass menulis method tertentu.',
    p3:'Override: method dengan nama sama di subclass. Python tidak punya overload; pakai nilai default parameter.',
    q1:{q:'Cara Python memanggil konstruktor kelas induk?',o:['self.__init__()','super().__init__()','parent()','base()'],a:1,w:'super().__init__(...) dipanggil di dalam __init__ milik subclass.'}},
 10:{t:'List Dinamis',
    b0:'List Python bisa tumbuh dan menyusut sendiri. Kamu bisa <code>append</code>, <code>insert</code>, <code>remove</code>, <code>pop</code>, dan mengubah elemen lewat indeks tanpa memikirkan ukuran.',
    b1:'List boleh berisi nilai apa saja, bahkan campuran tipe. Agar kode mudah dibaca, biasakan satu list berisi satu jenis data. Petunjuk tipe seperti <code>list[str]</code> membantu editor menemukan kesalahan.',
    p0:'<code>len(lst)</code> memberi jumlah elemen.',
    p1:'<code>pop(1)</code> menghapus indeks 1. <code>remove("a")</code> menghapus nilai "a".',
    p2:'<code>in</code> untuk mengecek keberadaan: <code>"a" in lst</code>.',
    tip:'Bayangkan antrean bangku bioskop. Kalau satu orang keluar dari tengah, semua orang di belakangnya bergeser satu kursi. Itulah biaya menghapus di tengah list.',
    q0:{q:'List berisi [a, b, c, d]. Setelah <code>pop(1)</code>, isinya menjadi...',o:['[a, c, d]','[b, c, d]','[a, b, d]','[a, b, c]'],a:0,w:'Indeks 1 adalah b. Setelah dihapus, c dan d bergeser ke kiri.'},
    q1:{q:'Apa hasil <code>len(a)</code> setelah <code>a = [1, 2]</code> lalu <code>a.append(3)</code>?',o:['2','3','Error','[1, 2, 3]'],a:1,w:'append menambah satu elemen di akhir, jadi panjangnya 3.'}},
 11:{t:'Koleksi: List, Set, Dict',
    b0:'Selain list, ada dua koleksi penting. <b>Set</b> adalah himpunan: tidak ada duplikat dan pengecekan <code>in</code> sangat cepat. <b>Dictionary</b> (<code>dict</code>) memasangkan <b>kunci</b> dengan <b>nilai</b>, misalnya kata dengan jumlah kemunculannya.',
    b1:'<code>set</code> dan <code>dict</code> bawaan Python sangat cepat. <code>dict</code> menyimpan urutan saat data dimasukkan, sedangkan <code>set</code> tidak menjamin urutan. Butuh hasil terurut? Pakai <code>sorted()</code>. Modul <code>collections</code> menambah <code>Counter</code> dan <code>defaultdict</code> untuk kasus menghitung.',
    p0:'<code>d.get(k, 0)</code> menghindari <code>KeyError</code> saat kunci belum ada.',
    p1:'Kunci dict unik. Mengisi <code>d[k] = v</code> pada kunci yang sama menimpa nilai lama.',
    tip:'Hampir setiap soal "hitung berapa kali X muncul" diselesaikan dengan dict dari X ke jumlah.',
    'q1.o2':'Dictionary'},
 12:{b0:'<b>Rekursi</b> adalah fungsi yang memanggil dirinya sendiri untuk menyelesaikan versi masalah yang lebih kecil. <code>faktorial(4)</code> sama dengan <code>4 * faktorial(3)</code>, dan seterusnya sampai <code>faktorial(1)</code>.',
    p2:'Rekursi terlalu dalam menghasilkan <code>RecursionError</code> (batas bawaan sekitar 1000 pemanggilan).',
    'q0.o1':'RecursionError'},
 13:{p2:'<code>sorted()</code> dan <code>list.sort()</code> sudah sangat dioptimalkan.'},
 14:{p1:'Stack: pakai list dengan <code>append</code> dan <code>pop</code>.',
    p2:'Queue: pakai <code>collections.deque</code> dengan <code>append</code> dan <code>popleft</code>.'},
 15:{b0:'Di bab ini kamu membangun list sederhana bernama <code>ArrayIntList</code>. Di dalamnya ada "array" internal berukuran tetap (<code>_data</code>) dan penghitung <code>_size</code>. Pengguna kelas hanya melihat method <code>add</code>, <code>get</code>, <code>size</code>, dan seterusnya.',
    p0:'Atribut diawali <code>_</code>. Pengguna tidak boleh mengubah <code>_size</code> langsung.',
    vizD:'Tambah elemen sampai penuh dan lihat "array" internal diperbesar.',
    'q1.o3':'Diwajibkan Python'},
 16:{b0:'<b>Linked list</b> menyimpan data dalam <b>node</b> terpisah. Setiap node berisi data dan referensi <code>next</code> ke node berikutnya. Node terakhir menunjuk <code>None</code>. Kelas list hanya perlu mengingat <code>front</code>, yaitu node pertama.',
    p0:'Selalu tangani kasus list kosong (<code>front is None</code>) secara terpisah.',
    p1:'<code>current.next.next</code> berbahaya bila <code>current.next</code> bernilai None.',
    p3:'<code>collections.deque</code> sudah tersedia untuk pemakaian nyata dan cepat di kedua ujung.',
    tip:'Bila muncul AttributeError: \'NoneType\' object has no attribute, cek setiap titik pada <code>a.b.c</code>: siapa yang mungkin None?'},
 17:{p0:'Base case kode pohon hampir selalu <code>node is None</code>.',
    p3:'Python tidak punya pohon terurut bawaan. Modul <code>bisect</code> bisa menjaga list tetap terurut.'},
 18:{b0:'<b>Hashing</b> adalah rahasia kecepatan dict dan set. Sebuah fungsi hash mengubah kunci menjadi angka, lalu angka itu dipetakan ke indeks array yang disebut ember (bucket). Mencari kunci cukup menghitung hash-nya dan langsung melompat ke ember yang tepat, rata-rata O(1).',
    p0:'Objek yang dijadikan kunci dict harus punya <code>__eq__</code> dan <code>__hash__</code> yang konsisten.'},
 19:{b1:'<b>Lambda</b> adalah fungsi tanpa nama yang ditulis ringkas, misalnya <code>lambda n: n * 2</code>. Tiga operasi utamanya: <b>filter</b> menyaring elemen, <b>map</b> mengubah setiap elemen, <b>reduce</b> menggabungkan semuanya menjadi satu nilai.',
    b2:'Python punya <code>map</code>, <code>filter</code>, <code>functools.reduce</code>, dan yang paling populer, list comprehension. Gaya ini mendorong <b>fungsi murni</b> dan data <b>immutable</b>, sehingga kode lebih mudah diuji dan aman dijalankan paralel.',
    p0:'<code>map</code>, <code>filter</code>, dan comprehension tidak mengubah list asal.',
    p1:'Fungsi bisa dikirim langsung: <code>map(str.upper, kata)</code> sama dengan <code>map(lambda s: s.upper(), kata)</code>.',
    vizD:'Susun pipeline sendiri dan lihat kode Python yang setara.'}
};
const TPFIX={
 '1.0':{ri0:'Komputer tidak melompat sendiri. Urutan baris adalah urutan eksekusi, kecuali ada percabangan, perulangan, atau pemanggilan fungsi.',ri1:'Python: langsung statement, dijalankan dari atas ke bawah.',ri2:'print selalu menambah pindah baris di akhir. Tulis print(..., end="") bila tidak ingin pindah baris.','lg.stmt':'Satu instruksi lengkap. Di Python, satu baris biasanya satu statement.'},
 '1.1':{t:'Fungsi (memecah program)',exq:'Jalankan fungsi bernama garis',exw:'Memanggil fungsi cukup menulis namanya diikuti kurung. def hanya dipakai saat mendefinisikan.','lg.call':'Pemanggilan: menjalankan isi fungsi lalu kembali ke sini.','lg.body':'Badan fungsi, dijalankan setiap kali dipanggil.',ri2:'Jika satu tugas ditulis dua kali, jadikan fungsi.','pj.s':'Cetak lirik lagu pendek yang punya reff (chorus) dua kali. Reff ditulis sekali sebagai fungsi, lalu dipanggil dua kali.','pj.l1':'Buat fungsi reff() berisi baris-baris reff.'},
 '2.0':{exw:'Pola Python: nama = nilai. Nama selalu di kiri tanda =.'},
 '2.1':{ri0:'/ selalu menghasilkan float. // membuang pecahan (pembagian bulat).'},
 '2.2':{ri0:'Untuk range(awal, akhir): putaran = akhir − awal.',ri1:'Urutan Python: range menyiapkan deret → setiap putaran i mengambil nilai berikutnya → deret habis → keluar.',ri2:'Contoh: for i in range(0, 10, 2) → 0, 2, 4, 6, 8 → 5 putaran.'},
 '3.0':{exw:'"Mengembalikan" berarti return. Mencetak dengan print bukan mengembalikan. Panjang dan lebar harus menjadi parameter.','lg.ret':'Kirim hasil balik dan akhiri fungsi.','lg.call':'Memanggil fungsi kuadrat.',ri2:'Parameter dan variabel lokal hilang saat fungsi selesai (scope).',ri3:'Fungsi tanpa return mengembalikan None, jadi dipakai sebagai statement, bukan di dalam ekspresi.','pj.s':'Buat fungsi bmi(berat, tinggi_cm) yang mengembalikan BMI (berat / tinggi² dalam meter), dibulatkan 1 angka di belakang koma. Hitung untuk 2 orang.','pj.l2':'return hasilnya, lalu panggil fungsi dua kali dengan data berbeda.'},
 '3.1':{'lg.meth':'Method milik objek str. Menghasilkan string baru.',ri1:'s[a:b]: ambil dari a, BERHENTI SEBELUM b.',ri2:'String tidak bisa diubah. Method seperti upper() membuat string baru.',ri3:'Gabungkan angka ke teks dengan f-string: f"Nilai: {5}" → "Nilai: 5".'},
 '3.2':{exw:'Pecahan → float. Tanpa float() hasilnya masih teks.',ri0:'input() selalu mengembalikan teks. Ubah dengan int() untuk bilangan bulat atau float() untuk pecahan.'},
 '4.0':{t:'if / elif / else',ri1:'Tepat satu cabang dari rantai if / elif / else yang dijalankan.',ri3:'Kata "jika … selain itu" → if … else. "jika … kalau tidak jika" → elif.','pj.l0':'Buat fungsi huruf(nilai) berisi rantai if / elif / else.'},
 '5.0':{'lg.cond':'Dicek sebelum setiap putaran. False → keluar.'},
 '5.1':{exw:'"dan" → and, "minimal 17" → >= 17. "atau" akan membolehkan orang tanpa tiket.',ri0:'Short-circuit: False and … → False tanpa melihat kanan. True or … → True tanpa melihat kanan.',ri1:'Taruh pengecekan "aman" di kiri: x != 0 and 10 / x > 1.',ri2:'De Morgan: not (a and b) = not a or not b, dan not (a or b) = not a and not b.',ri3:'Kalimat "dan" → and, "atau" → or, "bukan / tidak" → not.','pj.l1':'"dan tidak" → and not.','pj.l2':'"atau" → or. Gunakan kurung agar jelas.'},
 '6.0':{exw:'open() membuka file dan for baris in f membaca satu baris per putaran. Blok with menutup file otomatis.'},
 '6.1':{ri2:'Python tidak memaksa menangkap exception, jadi pikirkan sendiri di mana error bisa terjadi.'},
 '7.0':{ri1:'List baru langsung berisi nilai yang kamu tulis. [0] * 5 membuat lima angka 0.',ri2:'Akses a[len(a)] → IndexError.'},
 '7.1':{rf:'for i in range(len(a)) → kunjungi a[i]'},
 '7.2':{ri1:'Untuk salinan sungguhan: a.copy() atau list(a).',ri2:'Mengirim list ke fungsi juga mengirim referensi. Fungsi bisa mengubah isi list pemanggil.','pj.s':'Buat fungsi diskon(harga) yang memotong setiap harga 50% langsung di list. Buktikan list asli ikut berubah, sedangkan salinannya tidak.','pj.l1':'Kirim list asli ke fungsi. Fungsi menerima objek yang sama.'},
 '8.0':{exo1:'b = Buku.buat("Laskar Pelangi", 529)',exw:'Python cukup memanggil nama kelas seperti memanggil fungsi. Variabel tetap di sebelah kiri.',rf:'Kelas(args) = buat objek → __init__ → referensi',ri1:'__init__ mengisi atribut. Parameternya hilang setelah selesai, atribut tetap ada.',ri2:'Kata benda dalam soal → kelas / atribut. Kata kerja → method.','pj.s':'Buat kelas Buku dengan atribut judul dan halaman. Buat dua objek buku dan cetak informasinya lewat method info().','pj.l0':'Kata benda "buku" → kelas Buku. Sifatnya (judul, halaman) → atribut.','pj.l1':'__init__ mengisi atribut.','pj.l2':'Setiap objek punya isi atribut sendiri.'},
 '8.1':{'lg.priv':'Atribut internal (awalan _). Kesepakatannya: kode luar tidak menulis a._saldo = -999.','lg.call':'Di dalam setor, self menunjuk objek a.',rf:'objek.method(args)   →   di dalamnya self = objek itu',ri0:'Atribut internal + method dengan pengecekan = data selalu valid.','pj.l0':'Atribut saldo dibuat internal: _saldo.'},
 '9.0':{exw:'"A adalah sejenis B" → class A(B). Kelas anak di depan, induk di dalam kurung.',ri0:'Python memeriksa method saat program berjalan: bila objeknya punya method itu, pemanggilan berhasil.',ri2:'Kalimat "X adalah sejenis Y" → class X(Y). Kalimat "X punya Y" → Y menjadi atribut di X.','pj.l0':'"Kucing adalah sejenis hewan" → class Kucing(Hewan).'},
 '9.1':{t:'Duck typing (kontrak tanpa interface)',exw:'Cukup tulis method luas(). Python tidak memeriksa nama kontraknya, yang penting method-nya ada.',rf:'kontrak = sepakat punya method yang sama · objek yang punya method-nya boleh dipakai',ri0:'Untuk kontrak yang dipaksa, pakai kelas abstrak: class Bentuk(ABC) dengan @abstractmethod.','pj.s':'Persegi, PersegiPanjang, dan Segitiga masing-masing punya method luas(). Hitung total luas semua bangun.','pj.l0':'Sepakati bahwa setiap bentuk punya method luas().','pj.l1':'Setiap kelas menulis method luas() dengan rumusnya sendiri.'},
 '10.1':{ri0:'Maju: setelah pop(i), elemen berikutnya pindah ke i, lalu loop melompatinya.'},
 '11.0':{ri1:'Ubah list menjadi set untuk membuang duplikat: set(lst).',ri2:'set tidak menjamin urutan. Pakai sorted() bila butuh hasil terurut.','pj.l2':'Pakai sorted() agar urutannya pasti.'},
 '12.0':{'pj.s':'Tulis fungsi pangkat(a, b) secara rekursif tanpa loop dan tanpa **. Hitung 2⁵ dan 3⁴.'},
 '12.1':{'pj.s':'Tulis fungsi rekursif biner(n) yang mengembalikan bentuk biner dari n sebagai teks. Uji dengan 13 dan 6.'},
 '13.2':{exq:'Berapa Big-O kode: for i in range(n): cetak(i), lalu for j in range(n): cetak(j) (dua loop berurutan, tidak bersarang)'},
 '15.0':{ri0:'size = yang dipakai. Kapasitas = len(data).','pj.t':'List buatan sendiri','pj.l1':'Jika size == len(data) → buat list 2× lebih besar, salin isi lama.'},
 '15.1':{exq:'Tolak umur negatif di method set_umur'},
 '16.0':{ri1:'Tambah di depan: front = ListNode(x, front). Node baru menunjuk front LAMA.','pj.l0':'Tambah di depan: front = ListNode(x, front).'},
 '16.1':{rf:'cur = front; while cur is not None: …; cur = cur.next',ri1:'Untuk mengubah list, berhenti SATU node sebelum target: while cur.next is not None.','pj.l0':'cur = front, lalu while cur is not None.'},
 '19.0':{ri2:'Lambda hanya untuk logika pendek. Yang panjang, tulis fungsi biasa dengan def.','pj.l0':'Aturan urut ditulis sebagai lambda: key=lambda s: len(s).','pj.l2':'Lambda = fungsi kecil tanpa nama.'}
};
const FIX={java:{ch:JFIX,tp:TJFIX},python:{ch:PFIX,tp:TPFIX}};
/* Nama istilah glosarium yang memuat padanan bahasa lain. */
const GLN={java:{'Null / None':'Null','this / self':'this','toString / __str__':'toString()','Javadoc / Docstring':'Javadoc'},
  python:{'Null / None':'None','this / self':'self','toString / __str__':'__str__','Javadoc / Docstring':'Docstring','Method / Fungsi':'Fungsi','Field / Atribut':'Atribut','Map / Dictionary':'Dictionary','Package / Modul':'Modul','Getter / Setter':'Property (getter/setter)','ArrayList':'List'}};
const glName=(g,lang)=>GLN[lang]&&GLN[lang][g.t]||g.t;
/* Di jalur Python, sebutan null di catatan topik linked list dan pohon menjadi None. */
const pyNone=s=>typeof s!=='string'?s:s.replace(/ != null\b/g,' is not None').replace(/ == null\b/g,' is None').replace(/\bnull\b/g,'None');
const CHL_={};
function chFor(n,lang){
  const f=FIX[lang]&&FIX[lang].ch[n];if(!f)return CH[n-1];
  const key=lang+n;if(CHL_[key])return CHL_[key];
  const c=JSON.parse(JSON.stringify(CH[n-1]));
  for(const [k,v] of Object.entries(f)){let m;
    if((m=/^b(\d+)$/.exec(k)))c.body[+m[1]]=v;
    else if((m=/^p(\d+)$/.exec(k)))c.points[+m[1]]=v;
    else if((m=/^q(\d+)$/.exec(k)))c.quiz[+m[1]]=v;
    else if((m=/^q(\d+)\.o(\d+)$/.exec(k)))c.quiz[+m[1]].o[+m[2]]=v;
    else c[k]=v}
  c.body=c.body.filter(x=>x!=null);c.points=c.points.filter(x=>x!=null);c.quiz=c.quiz.filter(x=>x!=null);
  return CHL_[key]=c;
}
const chJ=n=>chFor(n,'java');
/* Topik versi satu bahasa: teks diganti, legenda hanya berisi bagian yang ada di kode bahasa itu,
   dan baris "(Java saja)" / "(Python saja)" di tabel kalimat→kode dibuang. */
function tpFor(ref,tp,lang){
  if(lang!=='java'&&lang!=='python')return tp;
  const f=FIX[lang].tp[ref]||{},P=lang==='python',fx=s=>P?pyNone(s):s,other=P?'(Java saja)':'(Python saja)';
  const t={...tp,ex:{...tp.ex},rumus:{...tp.rumus,f:fx(f.rf||tp.rumus.f),i:(tp.rumus.i||[]).map(fx)},legend:{},tr:tp.tr.filter(r=>!r[0].startsWith(other)).map(r=>[r[0].replace(/^\((Java|Python) saja\)\s*/,''),...r.slice(1)])};
  for(const [k,v] of Object.entries(tp.legend))if(tp[lang].includes('«'+k+'|'))t.legend[k]=[v[0],f['lg.'+k]||fx(v[1])];
  if(f.t)t.t=f.t;if(f.exq)t.ex.q=f.exq;if(f.exw)t.ex.w=f.exw;
  const col=P?1:0;if(Object.keys(f).some(k=>/^exo\d+$/.test(k)))t.ex.o=tp.ex.o.map((o,k)=>{const c=[...o];if(f['exo'+k])c[col]=f['exo'+k];return c});
  for(const [k,v] of Object.entries(f)){const m=/^ri(\d+)$/.exec(k);if(m)t.rumus.i[+m[1]]=v}
  return t;
}
const tpJ=(ref,tp)=>tpFor(ref,tp,'java');
const projFor=(ref,p,lang)=>{if(!p||!FIX[lang])return p;const f=FIX[lang].tp[ref]||{},fx=lang==='python'?pyNone:s=>s;
  return {...p,t:f['pj.t']||p.t,s:f['pj.s']||p.s,l:p.l.map((x,i)=>f['pj.l'+i]||fx(x))}};
const lessonTitleIn=(l,lang)=>l.k==='lab'?chFor(l.n,lang).t:l.k==='topic'?(()=>{const [n,i]=l.ref.split('.').map(Number);return tpFor(l.ref,TOPICS[n][i],lang).t})():null;
/* Kuis cerita: teks soal yang menyebut bahasa lain, per indeks STORIES. */
const SFIX={
 java:{11:{'o1':'Error: ArrayIndexOutOfBoundsException'},14:{w:'Tipe variabel (Hewan) menentukan method yang boleh dipanggil. Solusinya ((Burung) h).terbang().'}},
 python:{0:{w:'7000 // 2000 = 3 (pembagian bulat, pecahan dibuang), 7000 % 2000 = 1000.'},5:{w:'95 >= 70 sudah True di cabang pertama, sisanya dilewati. Perbaikannya: urutkan dari kondisi paling ketat (>= 90) dulu.'},
  6:{w:'120.000 (1), 140.000 (2), 160.000 (3). Setelah itu 160.000 < 150.000 bernilai False.'},7:{o0:'False',o1:'True',w:'kartu and not telat = True and False = False. False or False = False.'},
  11:{'o1':'Error: IndexError','o3':'List otomatis bertambah'},25:{o3:'None'}}};
const storyFor=(s,i,lang)=>{const f=SFIX[lang]&&SFIX[lang][i];if(!f)return s;const o=[...s.o];
  for(const [k,v] of Object.entries(f)){const m=/^o(\d+)$/.exec(k);if(m)o[+m[1]]=v}return {...s,o,w:f.w||s.w,q:f.q||s.q}};
/* Istilah yang hanya ada di bahasa lain disembunyikan dari daftar istilah pelajaran. */
const GLONLY={python:['jvm','arraylist','generics','wrapper-class','autoboxing','checked-exception'],java:[]};
const termsFor=(ids,lang)=>ids.filter(id=>!(GLONLY[lang]||[]).includes(id));
const glEn=(g,lang)=>GLN[lang]&&GLN[lang][g.t]?'':g.en;
