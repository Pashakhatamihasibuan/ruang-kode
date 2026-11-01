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
