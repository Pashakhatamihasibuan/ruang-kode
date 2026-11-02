import json,sys
sys.path.insert(0,'.')
exec(open('progs.py').read()); exec(open('soal.py').read())
OUT=json.load(open('out.json')); SO=json.load(open('soalout.json'))
TR={'java':('java','JAVA_MODULES','Java'),'python':('python','PY_MODULES','Python'),'ts':('ts','TS_MODULES','TypeScript'),'fe0':('js','FE0_MODULES','JavaScript')}
def each(l): return {'java':'for (String k : kota)','python':'for k in daftar','js':'for (const k of daftar)','ts':'for (const k of daftar)'}[l]
def dow(l): return {'java':'do { ... } while (kondisi);','python':'while True: ... if kondisi_berhenti: break','js':'do { ... } while (kondisi);','ts':'do { ... } while (kondisi);'}[l]
def forn(l): return {'java':'for (int i = 0; i < n; i++)','python':'for i in range(n)','js':'for (let i = 0; i < n; i++)','ts':'for (let i = 0; i < n; i++)'}[l]
def code(s): return '<code>'+s.replace('&','&amp;').replace('<','&lt;')+'</code>'
FC={
'fib':{'name':'FibonacciDiBawah100','p':[{'t':'dec','v':'a, b, c, banyak','ty':'Integer'},{'t':'asg','v':'a','e':'0'},{'t':'asg','v':'b','e':'1'},{'t':'asg','v':'banyak','e':'0'},
  {'t':'while','c':'a < 100','b':[{'t':'asg','v':'banyak','e':'banyak + 1'},{'t':'asg','v':'c','e':'a + b'},{'t':'asg','v':'a','e':'b'},{'t':'asg','v':'b','e':'c'}]},{'t':'out','e':'"Banyak suku: " & banyak'}]},
'bubble':{'name':'BubbleSort','p':[{'t':'dec','v':'a','ty':'Integer','arr':'4'},{'t':'asg','v':'a','e':'[25, 12, 22, 11]'},{'t':'dec','v':'j, t, putaran','ty':'Integer'},{'t':'dec','v':'adaTukar','ty':'Boolean'},
  {'t':'asg','v':'adaTukar','e':'true'},{'t':'asg','v':'putaran','e':'0'},
  {'t':'while','c':'adaTukar','b':[{'t':'asg','v':'adaTukar','e':'false'},{'t':'asg','v':'putaran','e':'putaran + 1'},
    {'t':'for','v':'j','a':'0','z':'3 - putaran','b':[{'t':'if','c':'a[j] > a[j + 1]','y':[{'t':'asg','v':'t','e':'a[j]'},{'t':'asg','v':'a[j]','e':'a[j + 1]'},{'t':'asg','v':'a[j + 1]','e':'t'},{'t':'asg','v':'adaTukar','e':'true'}],'n':[]}]}]},
  {'t':'out','e':'"Terurut: " & a'}]},
'prima':{'name':'CekPrima','in':['29'],'p':[{'t':'dec','v':'x, d','ty':'Integer'},{'t':'dec','v':'prima','ty':'Boolean'},{'t':'in','v':'x'},{'t':'asg','v':'prima','e':'x >= 2'},{'t':'asg','v':'d','e':'2'},
  {'t':'while','c':'d * d <= x and prima','b':[{'t':'if','c':'x mod d = 0','y':[{'t':'asg','v':'prima','e':'false'}],'n':[]},{'t':'asg','v':'d','e':'d + 1'}]},
  {'t':'if','c':'prima','y':[{'t':'out','e':'x & " adalah prima"'}],'n':[{'t':'out','e':'x & " bukan prima"'}]}]},
'digit':{'name':'JumlahDigit','in':['90417'],'p':[{'t':'dec','v':'angka, jumlah','ty':'Integer'},{'t':'in','v':'angka'},{'t':'asg','v':'jumlah','e':'0'},
  {'t':'while','c':'angka > 0','b':[{'t':'asg','v':'jumlah','e':'jumlah + angka mod 10'},{'t':'asg','v':'angka','e':'Int(angka / 10)'}]},{'t':'out','e':'"Jumlah digit: " & jumlah'}]},
'binser':{'name':'BinarySearch','in':['20000'],'p':[{'t':'dec','v':'harga','ty':'Integer','arr':'7'},{'t':'asg','v':'harga','e':'[5000, 8000, 12000, 15000, 20000, 27000, 35000]'},{'t':'dec','v':'cari, kiri, kanan, tengah, posisi','ty':'Integer'},
  {'t':'in','v':'cari'},{'t':'asg','v':'kiri','e':'0'},{'t':'asg','v':'kanan','e':'6'},{'t':'asg','v':'posisi','e':'-1'},
  {'t':'while','c':'kiri <= kanan and posisi = -1','b':[{'t':'asg','v':'tengah','e':'Int((kiri + kanan) / 2)'},
    {'t':'if','c':'harga[tengah] = cari','y':[{'t':'asg','v':'posisi','e':'tengah'}],'n':[{'t':'if','c':'harga[tengah] < cari','y':[{'t':'asg','v':'kiri','e':'tengah + 1'}],'n':[{'t':'asg','v':'kanan','e':'tengah - 1'}]}]}]},
  {'t':'out','e':'"Posisi: " & posisi'}]}}
def lessons(l):
  N=TR_NAME[l]
  py=l=='python'
  L=[]
  L.append({'k':'c','t':'Kapan for, kapan while, kapan do-while','nodes':['Loops'],'viz':'looppick',
   'b':['Semua loop bisa saling menggantikan, tetapi programmer yang baik memilih loop yang <b>paling jujur menggambarkan niatnya</b>. Pertanyaan kuncinya satu: <b>apakah jumlah putarannya sudah diketahui sebelum loop dimulai?</b>',
    f'Jika jumlahnya pasti (5 hari, 10 suku, setiap kursi 1 sampai 40), pakai <b>for</b> seperti {code(forn(l))}. Jika yang diketahui hanya <b>kondisi berhentinya</b> (sampai saldo cukup, sampai data habis, sampai tidak ada pertukaran lagi), pakai <b>while</b>. Jika badan loop harus jalan <b>minimal sekali</b> sebelum dicek (menampilkan menu, meminta PIN), pakai <b>do-while</b>: {code(dow(l))}.'+(' Python memang tidak punya do-while, jadi polanya ditulis dengan <code>while True</code> dan <code>break</code>.' if py else ''),
    f'Untuk membaca setiap isi koleksi tanpa butuh nomor indeks, pakai <b>for-each</b>: {code(each(l))}. Lebih ringkas dan tidak mungkin salah indeks (error klasik "off by one").',
    'Pada contoh kode di bawah, keempat jenis loop dipakai sesuai kasusnya masing-masing. Tebak keluarannya dulu, lalu coba latihan memilih loop di visual interaktif.'],
   'tb':[{'c':'Memilih jenis loop','h':['Jenis loop','Pakai saat','Contoh kasus','Bentuk di '+N],'r':[
     ['for','Jumlah putaran sudah diketahui','Cetak nomor 1 sampai 40, n suku Fibonacci',forn(l)],
     ['while','Hanya kondisi berhenti yang diketahui','Menabung sampai target, membaca data sampai habis','while (kondisi)' if not py else 'while kondisi:'],
     ['do-while','Badan loop wajib jalan minimal sekali','Menu kasir, meminta PIN',dow(l)],
     ['for-each','Membaca setiap isi koleksi','Menjumlahkan harga di keranjang',each(l)]]}],
   'code':P['pilih'][l],'out':OUT['pilih'][l],
   'pts':['Jumlah putaran diketahui → for.','Hanya kondisi berhenti yang diketahui → while.','Harus jalan minimal sekali → do-while.','Hanya membaca isi koleksi → for-each.'],
   'q':[['Program meminta pengguna mengetik kata sandi sampai benar. Loop paling cocok?',['for','do-while (atau while True + break)','for-each'],1,'Pertanyaan harus muncul minimal sekali, dan jumlah percobaannya tidak diketahui.'],
        ['Menghitung rata-rata 30 nilai siswa di sebuah array. Loop paling cocok?',['while','for atau for-each','do-while'],1,'Jumlah datanya pasti, cukup membaca setiap isi.'],
        ['Mengapa while lebih cocok untuk "menabung sampai Rp1 juta"?',['Karena while lebih cepat','Karena jumlah minggunya belum diketahui, yang diketahui hanya kondisi berhenti','Karena for tidak bisa menjumlah'],1,'Pilihan loop menggambarkan apa yang kita ketahui sebelum mulai.']]})
  L.append({'k':'c','t':'Bilangan Fibonacci: for dan while','nodes':['Loops'],'viz':'fc','fc':FC['fib'],
   'b':['Deret Fibonacci dimulai dari 0 dan 1, lalu setiap suku adalah jumlah dua suku sebelumnya: 0, 1, 1, 2, 3, 5, 8, 13, ... Polanya muncul di banyak tempat, dari susunan biji bunga matahari sampai soal tes kerja programmer.',
    'Kuncinya adalah dua variabel <code>a</code> dan <code>b</code> yang terus <b>digeser</b>: <code>a</code> menjadi <code>b</code>, dan <code>b</code> menjadi <code>a + b</code>. '+('Python bisa menggeser keduanya sekaligus dengan <code>a, b = b, a + b</code>.' if py else ('JavaScript/TypeScript bisa memakai <code>[a, b] = [b, a + b]</code>.' if l in('js','ts') else 'Di Java kita butuh variabel bantu, misalnya <code>int c = a + b; a = b; b = c;</code>, agar nilai lama <code>a</code> tidak hilang.')),
    'Perhatikan dua bagian contoh. "10 suku pertama" memakai <b>for</b> karena jumlah putarannya pasti 10. "Semua suku di bawah 100" memakai <b>while</b> karena kita tidak tahu ada berapa suku sampai benar-benar menghitungnya.',
    'Visual di bawah menjalankan bagian while langkah demi langkah sebagai flowchart dan pseudocode. Perhatikan kolom <b>Variabel</b>: nilai yang berubah diberi warna.'],
   'tb':[{'c':'Jejak variabel 6 putaran pertama','h':['Putaran','a','b','Suku yang dicatat'],'r':[['1','0','1','0'],['2','1','1','1'],['3','1','2','1'],['4','2','3','2'],['5','3','5','3'],['6','5','8','5']]}],
   'code':P['fib'][l],'out':OUT['fib'][l],
   'pts':['Fibonacci butuh dua variabel yang terus digeser.','n suku pertama → for; suku di bawah batas → while.','Geser nilai dengan urutan yang benar agar nilai lama tidak hilang.'],
   'q':[['Suku Fibonacci ke-8 (mulai dari 0) adalah?',['8','13','21'],1,'0, 1, 1, 2, 3, 5, 8, 13: suku ke-8 adalah 13.'],
        ['Mengapa menghitung "suku di bawah 1000" memakai while?',['Karena jumlah sukunya belum diketahui sebelum dihitung','Karena for tidak bisa memakai angka besar','Karena while selalu lebih cepat'],0,'Batasnya nilai, bukan banyak putaran.']]})
  L.append({'k':'c','t':'Bubble sort: loop di dalam loop','nodes':['Loops','Arrays'],'viz':'fc','fc':FC['bubble'],
   'b':['Bubble sort mengurutkan data dengan cara paling sederhana: bandingkan dua angka yang <b>bersebelahan</b>, tukar jika urutannya salah, lalu geser ke pasangan berikutnya. Setelah satu putaran, angka terbesar pasti sudah "menggelembung" ke ujung kanan.',
    'Algoritma ini memakai dua loop. <b>Loop dalam (for)</b> berjalan dari kiri ke kanan, jumlah pasangannya jelas. <b>Loop luar (while)</b> mengulang putaran selama masih ada pertukaran. Variabel penanda <code>'+('ada_tukar' if py else 'adaTukar')+'</code> membuat program berhenti lebih awal jika data sudah terurut.',
    'Setiap putaran, satu angka terbesar sudah di tempatnya, jadi loop dalam cukup sampai <code>n - putaran</code>. Detail kecil ini menghemat perbandingan yang tidak perlu.',
    'Bubble sort lambat untuk data besar (sekitar n² perbandingan), jadi di dunia kerja kita memakai fungsi sort bawaan bahasa. Tetapi bubble sort adalah latihan terbaik untuk memahami loop bersarang, indeks, dan menukar nilai.'],
   'tb':[{'c':'Isi array setiap putaran','h':['Putaran','Isi array','Yang sudah di tempat'],'r':[['Awal','64 25 12 22 11','-'],['1','25 12 22 11 64','64'],['2','12 22 11 25 64','25, 64'],['3','12 11 22 25 64','22, 25, 64'],['4','11 12 22 25 64','semua']]}],
   'code':P['bubble'][l],'out':OUT['bubble'][l],
   'pts':['Bandingkan pasangan bersebelahan, tukar jika salah urutan.','Loop dalam for (jumlah pasangan jelas), loop luar while (sampai tidak ada pertukaran).','Penanda pertukaran membuat sort berhenti lebih awal.'],
   'q':[['Setelah putaran pertama bubble sort (urut naik), di mana angka terbesar?',['Di indeks 0','Di ujung kanan','Belum pasti'],1,'Angka terbesar selalu terbawa sampai ujung kanan pada putaran pertama.'],
        ['Untuk apa variabel penanda pertukaran?',['Menghitung jumlah data','Menghentikan loop luar jika satu putaran tidak ada pertukaran','Menyimpan angka terbesar'],1,'Jika tidak ada pertukaran, data sudah terurut.'],
        ['Kenapa loop dalam cukup sampai n - putaran?',['Agar tidak error','Karena angka di ujung kanan sudah pasti di tempatnya','Karena aturan bahasa'],1,'Bagian kanan yang sudah terurut tidak perlu dibandingkan lagi.']]})
  L.append({'k':'c','t':'FizzBuzz dan bilangan prima: break dan loop bersarang','nodes':['Loops','Conditionals'],'viz':'fc','fc':FC['prima'],
   'b':['<b>FizzBuzz</b> adalah soal wawancara klasik: untuk angka 1 sampai 15, tampilkan "Fizz" jika habis dibagi 3, "Buzz" jika habis dibagi 5, "FizzBuzz" jika habis dibagi keduanya, dan angkanya sendiri jika tidak. Rentangnya jelas, jadi pakai <b>for</b>. Jebakannya: cek kelipatan 15 lebih dulu, karena jika cek 3 duluan, angka 15 sudah keburu menjadi "Fizz".',
    '<b>Bilangan prima</b> hanya habis dibagi 1 dan dirinya sendiri. Untuk setiap angka (loop luar), kita coba pembagi dari 2 (loop dalam). Begitu ketemu satu pembagi, angka itu pasti bukan prima, jadi <b>break</b> menghentikan loop dalam tanpa membuang waktu.',
    'Pembagi cukup dicoba sampai akar angkanya (<code>d * d &lt;= x</code>). Jika 36 = 4 × 9, salah satu faktornya pasti ≤ 6. Ini mengubah 1.000 percobaan menjadi sekitar 31.'+(' Python punya fitur unik <code>for ... else</code>: blok else jalan hanya jika loop selesai <b>tanpa</b> break.' if py else ' Variabel penanda <code>isPrima</code> mencatat apakah loop dalam pernah berhenti karena break.'),
    'Visual di bawah memeriksa satu angka dengan while dan penanda, karena Flowgorithm tidak punya break. Ganti inputnya, misalnya 91 atau 97, lalu jalankan.'],
   'tb':[{'c':'break dan continue','h':['Perintah','Efek','Kapan dipakai'],'r':[['break','Keluar dari loop terdekat','Jawaban sudah ditemukan, sisa putaran tidak perlu'],['continue','Lompat ke putaran berikutnya','Lewati data yang tidak relevan'],['penanda (flag)','Variabel boolean yang dicek setelah loop','Bahasa atau alat tanpa break, misalnya Flowgorithm']]}],
   'code':P['prima'][l],'out':OUT['prima'][l],
   'pts':['Urutan if penting: kondisi paling khusus dicek lebih dulu.','break menghentikan loop terdekat saat jawaban sudah pasti.','Pembagi prima cukup dicek sampai akar angkanya.'],
   'q':[['Jika FizzBuzz mengecek "habis dibagi 3" lebih dulu, apa yang tampil untuk 15?',['FizzBuzz','Fizz','Buzz'],1,'Kondisi pertama yang benar langsung dipakai.'],
        ['Pada loop bersarang, break menghentikan loop yang mana?',['Semua loop','Loop terdekat yang membungkusnya','Loop terluar'],1,'break hanya keluar dari satu tingkat loop.'],
        ['Untuk mengecek apakah 97 prima, pembagi paling besar yang perlu dicoba adalah?',['96','48','9'],2,'9 × 9 = 81 ≤ 97, sedangkan 10 × 10 = 100 > 97.']]})
  L.append({'k':'c','t':'Faktorial, jumlah digit, dan palindrom','nodes':['Loops'],'viz':'fc','fc':FC['digit'],
   'b':['Tiga soal ini melatih kapan memakai for dan kapan while. <b>Faktorial</b> 5! = 1 × 2 × 3 × 4 × 5: banyak perkaliannya pasti, jadi <b>for</b>.',
    '<b>Jumlah digit</b> 90417 = 9 + 0 + 4 + 1 + 7 = 21. Kita tidak tahu angkanya punya berapa digit, jadi pakai <b>while</b>: ambil digit terakhir dengan <code>% 10</code>, lalu buang dengan pembagian bulat '+('<code>// 10</code>' if py else ('<code>/ 10</code> (int di Java otomatis membulatkan ke bawah)' if l=='java' else '<code>Math.floor(x / 10)</code>'))+'. Berhenti saat angkanya habis (0).',
    '<b>Palindrom</b> adalah kata yang sama jika dibaca dari depan dan belakang, seperti "katak". Pakai <b>dua penunjuk</b>: satu dari kiri, satu dari kanan, bergerak ke tengah selama <code>kiri &lt; kanan</code>. Begitu ada huruf yang berbeda, langsung break.',
    'Visual di bawah menjalankan jumlah digit. Coba ganti inputnya dengan angka lain dan hitung dulu di kepala sebelum menekan Berikutnya.'],
   'tb':[{'c':'Jejak jumlah digit 90417','h':['Putaran','angka % 10','jumlah','angka setelah dibagi 10'],'r':[['1','7','7','9041'],['2','1','8','904'],['3','4','12','90'],['4','0','12','9'],['5','9','21','0']]}],
   'code':P['digit'][l],'out':OUT['digit'][l],
   'pts':['% 10 mengambil digit terakhir, bagi 10 (bulat) membuangnya.','Banyak digit tidak diketahui → while.','Dua penunjuk bergerak ke tengah untuk memeriksa palindrom.'],
   'q':[['Berapa hasil 4827 % 10?',['4','7','482'],1,'Sisa bagi 10 adalah digit terakhir.'],
        ['Loop paling cocok untuk menghitung 10! (faktorial 10)?',['for','while','do-while'],0,'Banyak perkaliannya pasti.'],
        ['Pada pemeriksaan palindrom "level", berapa kali perbandingan huruf terjadi?',['5','2','1'],1,'Pasangan (l, l) dan (e, e); huruf tengah v tidak perlu dibandingkan.']]})
  L.append({'k':'c','t':'Binary search: membagi dua sampai ketemu','nodes':['Loops','Arrays'],'viz':'fc','fc':FC['binser'],
   'b':['Mencari harga di daftar 1.000 barang satu per satu (linear search) bisa butuh 1.000 langkah. Jika daftarnya <b>sudah terurut</b>, kita bisa jauh lebih cepat: lihat bagian tengah, lalu buang separuh daftar yang pasti tidak berisi jawabannya.',
    'Simpan dua batas, <code>kiri</code> dan <code>kanan</code>. Selama <code>kiri &lt;= kanan</code>, hitung <code>tengah</code>. Jika nilai tengah terlalu kecil, geser kiri ke tengah + 1. Jika terlalu besar, geser kanan ke tengah - 1. Banyak langkahnya tidak diketahui sebelumnya, jadi loopnya <b>while</b>.',
    'Setiap langkah membuang separuh data, jadi 1.000 data cukup dicari dalam paling banyak 10 langkah, dan 1 juta data dalam 20 langkah. Inilah alasan database dan kamus memakai data terurut.',
    'Visual di bawah mencari harga di 7 data. Coba input 5000, 35000, atau 9000 (tidak ada di daftar) dan perhatikan bagaimana kiri dan kanan bergerak.'],
   'tb':[{'c':'Linear search vs binary search','h':['Aspek','Linear search','Binary search'],'r':[['Syarat data','Bebas','Harus terurut'],['Langkah terburuk (1.000 data)','1.000','10'],['Jenis loop','for (setiap data)','while (sampai ketemu atau habis)'],['Kapan dipakai','Data sedikit atau tidak terurut','Data besar dan terurut']]}],
   'code':P['binser'][l],'out':OUT['binser'][l],
   'pts':['Binary search hanya untuk data terurut.','Setiap langkah membuang separuh ruang pencarian.','Berhenti saat ketemu atau kiri > kanan.'],
   'q':[['Apa syarat utama binary search?',['Data berupa angka','Data sudah terurut','Data kurang dari 100'],1,'Tanpa urutan, kita tidak tahu separuh mana yang harus dibuang.'],
        ['Jika harga[tengah] lebih kecil dari yang dicari, apa yang dilakukan?',['kanan = tengah - 1','kiri = tengah + 1','Berhenti'],1,'Jawabannya pasti di sebelah kanan tengah.'],
        ['Kira-kira berapa langkah maksimum untuk 1 juta data terurut?',['20','1.000','500.000'],0,'2 pangkat 20 ≈ 1 juta.']]})
  keys=['pilih','fib','bubble','prima','digit','binser']
  for x,k in zip(L,keys):
    x['lang']=l
    x['so']=[{'q':s['q'],'h':s['h'],'a':s['a'][l],'out':SO[k][i][l]} for i,s in enumerate(Q[k])]
  return L

FM=json.load(open('fmt.json'))
def fmtlesson(l):
  py=l=='python';jv=l=='java';js=l in('js','ts')
  b=['<b>Format specifier</b> adalah kode kecil yang mengatur <b>bagaimana sebuah nilai ditampilkan</b>: berapa angka di belakang koma, selebar apa kolomnya, rata kiri atau kanan, diberi nol di depan, atau diberi pemisah ribuan. Nilainya tidak berubah, hanya tampilannya. Hampir semua program nyata membutuhkannya: struk belanja, laporan nilai, nomor invoice, dan log server.',
     'Polanya mirip di semua bahasa: <b>[perataan][lebar][.presisi][tipe]</b>. Contoh <code>%-10s</code> berarti teks rata kiri selebar 10, <code>%8.2f</code> berarti desimal 2 angka dalam kolom selebar 8, dan <code>%05d</code> berarti bilangan bulat selebar 5 yang diisi nol di depan.']
  if jv: b+=['Di Java, pakai <code>System.out.printf(...)</code> untuk langsung mencetak, atau <code>String.format(...)</code> untuk menghasilkan teks (misalnya kode invoice). <code>%n</code> adalah baris baru yang benar di semua sistem operasi, dan <code>%%</code> mencetak tanda persen. Jumlah dan tipe argumen harus cocok: <code>%d</code> dengan nilai double akan error <code>IllegalFormatConversionException</code> saat program berjalan.',
     'Pemisah ribuan <code>%,d</code> mengikuti <b>lokal</b> komputer. Untuk format Indonesia (titik sebagai pemisah ribuan) tulis <code>String.format(Locale.forLanguageTag("id-ID"), "%,d", 7500000)</code>, yang menghasilkan 7.500.000.']
  if py: b+=['Python modern memakai <b>f-string</b>: <code>f"{nilai:spesifikasi}"</code>. Perataan ditulis dengan simbol: <code>&lt;</code> kiri, <code>&gt;</code> kanan, <code>^</code> tengah. Tambahan khas Python: <code>{x:,}</code> untuk pemisah ribuan, <code>{x:.0%}</code> untuk persen, dan <code>{x=}</code> untuk debugging cepat yang mencetak nama variabel beserta nilainya.',
     'Kamu juga akan menemui gaya lama <code>"%s %d" % (a, b)</code> dan <code>"{}".format(x)</code> di kode lama dan modul logging. Spesifikasinya sama, jadi cukup pelajari sekali. Untuk kode baru, f-string adalah standar industri karena paling mudah dibaca.']
  if js: b+=['JavaScript'+(' dan TypeScript' if l=='ts' else '')+' tidak punya printf. Gantinya: <b>template literal</b> <code>`${nilai}`</code> untuk menyisipkan nilai, <code>toFixed(2)</code> untuk presisi, <code>padStart</code>/<code>padEnd</code> untuk lebar dan perataan, dan <code>toString(16)</code> untuk basis lain. <code>console.log</code> mengenal <code>%s %d %f %o</code>, tetapi hanya untuk mencetak ke konsol.',
     'Untuk angka dan uang yang tampil ke pengguna, industri memakai <code>Intl.NumberFormat</code> atau <code>toLocaleString("id-ID")</code>, sehingga 7500000 tampil sebagai 7.500.000 atau Rp 7.500.000 sesuai aturan Indonesia. Hindari menyusun format uang sendiri dengan replace atau regex.'+(' TypeScript menambahkan pengecekan tipe: <code>toFixed</code> hanya bisa dipanggil pada <code>number</code>, jadi salah tipe ketahuan sebelum program dijalankan.' if l=='ts' else '')]
  b+=['Contoh terakhir di kode adalah <b>struk belanja</b>: format di dalam loop membuat setiap baris punya lebar kolom yang sama, sehingga angka tersusun rapi ke kanan. Ini pola yang akan sering kamu pakai di soal-soal berikutnya.']
  tb=[{'c':'Format specifier di berbagai bahasa','h':['Tujuan','Java / C (printf)','Python (f-string)','JavaScript / TypeScript'],'r':[
      ['Teks','%s','{x}','${x}'],['Bilangan bulat','%d','{x:d}','${x}'],['Desimal 2 angka','%.2f','{x:.2f}','x.toFixed(2)'],
      ['Lebar 8, rata kanan','%8s','{x:>8}','String(x).padStart(8)'],['Lebar 8, rata kiri','%-8s','{x:<8}','String(x).padEnd(8)'],
      ['Isi nol di depan','%05d','{x:05d}','String(x).padStart(5, "0")'],['Pemisah ribuan','%,d','{x:,}','x.toLocaleString("id-ID")'],
      ['Persen','%.0f%%','{x:.0%}','(x * 100).toFixed(0) + "%"'],['Heksadesimal','%x','{x:x}','x.toString(16)'],
      ['Notasi ilmiah','%.3e','{x:.3e}','x.toExponential(3)'],['Baris baru','%n atau \\n','\\n','\\n']]},
     {'c':'Yang paling sering dipakai di industri','h':['Kebutuhan','Pilihan umum','Alasan'],'r':[
      ['Menyusun teks di kode baru','f-string (Python), template literal (JS/TS), String.format atau formatted() (Java)','Paling mudah dibaca dan dirawat'],
      ['Angka dan uang ke pengguna','Format berbasis lokal: Intl.NumberFormat, Locale id-ID, Babel','Titik, koma, dan simbol Rp mengikuti aturan negara'],
      ['Laporan dan struk berkolom','Lebar + perataan: %-12s, %10.2f, padEnd/padStart','Kolom tetap lurus berapa pun panjang datanya'],
      ['Kode dokumen dan antrean','Isi nol: %04d, {n:04d}','INV-0007 lebih mudah diurutkan dan dicari'],
      ['Logging','Placeholder %s atau {}: logger.info("user %s", id)','Teks hanya disusun jika log benar-benar dicetak'],
      ['Tanggal','ISO 8601 (2026-11-02) atau pola yyyy-MM-dd','Standar internasional dan mudah diurutkan']]}]
  q=[['Apa arti format %-10s?',['Teks rata kanan selebar 10','Teks rata kiri selebar 10','10 karakter pertama saja'],1,'Tanda minus berarti rata kiri, angka 10 adalah lebar kolom minimum.'],
     ['Format apa yang menampilkan 7 sebagai 007?',['%.3d atau {x:.3}','%03d atau {x:03d}','%3d atau {x:3}'],1,'Angka 0 di depan lebar berarti isi nol. Tanpa 0, sisa tempat diisi spasi.'],
     ['3.14159 diformat dengan dua angka desimal hasilnya?',['3.14','3.15','3.1'],0,'Dibulatkan ke 2 angka di belakang koma: 3.14159 → 3.14.'],
     ['Untuk menampilkan harga ke pengguna Indonesia, cara yang dianjurkan adalah?',['Menyusun titik ribuan sendiri dengan replace','Memakai format berbasis lokal id-ID','Menampilkan angka mentah'],1,'Format lokal menangani pemisah ribuan, desimal, dan simbol mata uang dengan benar.']]
  return {'k':'c','t':'Format specifier: merapikan keluaran','nodes':['Basic Syntax'],'lang':l,'b':b,'tb':tb,'code':FM['code'][l],'out':FM['out'][l],
    'pts':['Pola umum: [perataan][lebar][.presisi][tipe].','Lebar + perataan membuat kolom laporan lurus.','Untuk angka ke pengguna, pakai format lokal (id-ID).','Kode baru: f-string, template literal, atau String.format.'],'q':q,
    'so':[{'q':s['q'],'h':s['h'],'a':s['a'][l],'out':SO['format'][i][l]} for i,s in enumerate(Q['format'])]}
TR_NAME={'java':'Java','python':'Python','js':'JavaScript','ts':'TypeScript'}
data={}
for tk,(l,mods,n) in TR.items():
  data[tk]={'mods':mods,'mod':{'t':'Format keluaran dan latihan algoritma','lvl':'Menengah','d':f'Format specifier, Fibonacci, bubble sort, FizzBuzz, bilangan prima, palindrom, dan binary search di {n}, dengan alasan memilih for, while, do-while, atau for-each.','nodes':['Loops','Arrays'],'lessons':[fmtlesson(l)]+lessons(l)}}
js='/* ===================== LATIHAN ALGORITMA PER BAHASA =====================\n   Dibuat oleh tools/gen/algo/gen.py (jalankan dari folder itu). Modul ditambahkan di AKHIR jalur agar alamat pelajaran lama tidak bergeser.\n   Semua kode dan keluaran sudah dijalankan (Java 21, Python 3, Node 22). */\n(()=>{\nconst ALGO='+json.dumps({k:v['mod'] for k,v in data.items()},ensure_ascii=False,indent=0)+';\n'
js+='const T={java:JAVA_MODULES,python:PY_MODULES,ts:TS_MODULES,fe0:FE0_MODULES};\nfor(const k in ALGO)if(!T[k].some(m=>m.t===ALGO[k].t))T[k].push(ALGO[k]);\n})();\n'
open(sys.argv[1],'w').write(js)
print(len(js))
