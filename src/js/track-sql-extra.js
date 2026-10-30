/* ===================== SQL: PROYEK MINI =====================
   Menambahkan satu proyek mini (beberapa tantangan berurutan, tasks:[...]) ke modul
   jalur SQL, serta proyek akhir. Ditaruh terpisah agar track-sql.js tetap utuh. */
(()=>{
const add=(title,lesson)=>{const m=SQL_MODULES.find(x=>x.t===title);if(m)m.lessons.push(lesson)};
const mini=(t,b,tasks,ex)=>({k:'s',t:'Proyek mini: '+t,mini:true,b,ex:ex||[],tasks,pts:[],q:[]});
add('Membaca data dengan SELECT',mini('Katalog Toko Nusantara',
 ['Manajer toko meminta beberapa daftar untuk katalog cetak. Kerjakan tantangan berurutan; setiap tantangan dinilai otomatis dan progresnya tersimpan.'],
 [{q:'Tampilkan nama dan harga semua produk kategori Camilan, urut dari harga termurah.',a:"SELECT nama, harga FROM produk WHERE kategori = 'Camilan' ORDER BY harga;",order:true},
  {q:'Tampilkan 3 produk termahal (nama, harga).',a:'SELECT nama, harga FROM produk ORDER BY harga DESC LIMIT 3;',order:true},
  {q:'Tampilkan daftar kategori tanpa duplikat, urut abjad.',a:'SELECT DISTINCT kategori FROM produk ORDER BY kategori;',order:true},
  {q:'Tampilkan nama produk yang stoknya kurang dari 50 tetapi tidak habis (stok > 0).',a:'SELECT nama FROM produk WHERE stok < 50 AND stok > 0;'}],
 [['Lihat produk','SELECT * FROM produk;']]));
add('Agregasi & pengelompokan',mini('Ringkasan stok gudang',
 ['Tim gudang butuh ringkasan untuk rapat mingguan. Gunakan fungsi agregat, GROUP BY, dan HAVING.'],
 [{q:'Hitung jumlah produk (kolom jumlah_produk) dan total stok (kolom total_stok) per kategori.',a:'SELECT kategori, COUNT(*) AS jumlah_produk, SUM(stok) AS total_stok FROM produk GROUP BY kategori;'},
  {q:'Tampilkan nilai persediaan per kategori (harga × stok, kolom nilai), urut dari terbesar.',a:'SELECT kategori, SUM(harga * stok) AS nilai FROM produk GROUP BY kategori ORDER BY nilai DESC;',order:true},
  {q:'Tampilkan kategori yang rata-rata harganya di atas 50000 beserta rata-ratanya (kolom rata).',a:'SELECT kategori, AVG(harga) AS rata FROM produk GROUP BY kategori HAVING AVG(harga) > 50000;'},
  {q:'Hitung jumlah pesanan per status (kolom n).',a:'SELECT status, COUNT(*) AS n FROM pesanan GROUP BY status;'}],
 [['Lihat produk','SELECT * FROM produk;']]));
add('JOIN',mini('Laporan pesanan pelanggan',
 ['Tim layanan pelanggan ingin melihat siapa membeli apa. Gabungkan pelanggan, pesanan, detail_pesanan, dan produk.'],
 [{q:'Tampilkan id pesanan, nama pelanggan, dan status untuk semua pesanan.',a:'SELECT s.id, p.nama, s.status FROM pesanan s JOIN pelanggan p ON p.id = s.pelanggan_id;'},
  {q:'Tampilkan nama pelanggan yang belum pernah memesan.',a:'SELECT p.nama FROM pelanggan p LEFT JOIN pesanan s ON s.pelanggan_id = p.id WHERE s.id IS NULL;'},
  {q:'Hitung total belanja (jumlah × harga, kolom total) setiap pesanan berstatus selesai, tampilkan id pesanan dan total.',a:"SELECT s.id, SUM(d.jumlah * pr.harga) AS total FROM pesanan s JOIN detail_pesanan d ON d.pesanan_id = s.id JOIN produk pr ON pr.id = d.produk_id WHERE s.status = 'selesai' GROUP BY s.id;"},
  {q:'Tampilkan nama karyawan dan nama atasannya (kolom atasan); karyawan tanpa atasan tetap tampil.',a:'SELECT k.nama, a.nama AS atasan FROM karyawan k LEFT JOIN karyawan a ON a.id = k.atasan_id;'}],
 [['Lihat pesanan','SELECT * FROM pesanan;']]));
add('Subquery',mini('Mencari produk istimewa',
 ['Bagian pemasaran mencari produk untuk promosi. Selesaikan dengan subquery.'],
 [{q:'Tampilkan nama dan harga produk yang harganya di atas rata-rata semua produk.',a:'SELECT nama, harga FROM produk WHERE harga > (SELECT AVG(harga) FROM produk);'},
  {q:'Tampilkan nama produk yang ada di pesanan berstatus batal (pakai subquery IN bertingkat).',a:"SELECT nama FROM produk WHERE id IN (SELECT produk_id FROM detail_pesanan WHERE pesanan_id IN (SELECT id FROM pesanan WHERE status = 'batal'));"},
  {q:'Tampilkan nama pelanggan yang punya minimal satu pesanan berstatus dikirim (pakai EXISTS).',a:"SELECT nama FROM pelanggan p WHERE EXISTS (SELECT 1 FROM pesanan s WHERE s.pelanggan_id = p.id AND s.status = 'dikirim');"}],
 [['Rata-rata harga','SELECT AVG(harga) FROM produk;']]));
add('Fungsi lanjutan',mini('Merapikan laporan',
 ['Laporan untuk direksi harus rapi: label yang jelas dan tanpa nilai kosong.'],
 [{q:"Tampilkan nama produk dan label harga: 'Premium' jika harga ≥ 75000, 'Reguler' jika ≥ 25000, selain itu 'Hemat' (kolom label).",a:"SELECT nama, CASE WHEN harga >= 75000 THEN 'Premium' WHEN harga >= 25000 THEN 'Reguler' ELSE 'Hemat' END AS label FROM produk;"},
  {q:"Tampilkan nama pelanggan dan kota; kota kosong diganti 'Belum diisi' (kolom kota).",a:"SELECT nama, COALESCE(kota, 'Belum diisi') AS kota FROM pelanggan;"},
  {q:'Tampilkan nama pelanggan dalam huruf besar (kolom nama_besar) dan panjang namanya (kolom panjang).',a:'SELECT UPPER(nama) AS nama_besar, LENGTH(nama) AS panjang FROM pelanggan;'}],
 [['Lihat pelanggan','SELECT * FROM pelanggan;']]));
add('SQL lanjutan',mini('Peringkat & tren',
 ['Analisis lanjutan dengan CTE dan window function.'],
 [{q:'Beri peringkat produk dalam setiap kategori berdasarkan harga tertinggi (kolom peringkat, pakai RANK). Tampilkan kategori, nama, harga, peringkat.',a:'SELECT kategori, nama, harga, RANK() OVER (PARTITION BY kategori ORDER BY harga DESC) AS peringkat FROM produk;'},
  {q:'Dengan CTE, hitung jumlah pesanan per pelanggan (kolom n) lalu tampilkan hanya pelanggan dengan n ≥ 2 beserta namanya.',a:'WITH hitung AS (SELECT pelanggan_id, COUNT(*) AS n FROM pesanan GROUP BY pelanggan_id) SELECT p.nama, h.n FROM hitung h JOIN pelanggan p ON p.id = h.pelanggan_id WHERE h.n >= 2;'},
  {q:'Tampilkan id pesanan, tanggal, dan tanggal pesanan sebelumnya (kolom sebelumnya) memakai LAG, urut tanggal lalu id.',a:'SELECT id, tanggal, LAG(tanggal) OVER (ORDER BY tanggal, id) AS sebelumnya FROM pesanan ORDER BY tanggal, id;',order:true}],
 [['Lihat produk','SELECT * FROM produk;']]));
SQL_MODULES.push({t:'Proyek akhir',lvl:'Profesional',d:'Rancang, isi, dan analisis database dari nol.',nodes:['Project'],
 lessons:[{k:'proj',t:'Database toko buku online',stack:'SQL (PostgreSQL/SQLite)',
  brief:'Rancang database toko buku "Pustaka Nusantara": buku, penulis, pelanggan, pesanan. Isi data contoh, lalu jawab pertanyaan bisnis dengan query.',
  feats:['Diagram ERD dengan relasi banyak-ke-banyak buku-penulis','CREATE TABLE dengan PRIMARY KEY, FOREIGN KEY, CHECK, NOT NULL','Minimal 20 buku, 10 penulis, 15 pelanggan, 40 pesanan','Index untuk kolom yang sering dicari','View laporan_penjualan_bulanan','Transaksi pemesanan yang mengurangi stok secara atomik','Query: 5 penulis terlaris, pelanggan tanpa pesanan 90 hari, pertumbuhan MoM','Window function untuk peringkat buku per genre'],
  steps:['Rancang ERD dan normalisasi sampai 3NF.','Tulis DDL dan data contoh.','Tambah index, view, dan transaksi.','Jawab pertanyaan bisnis.'],
  files:[['skema.sql','sql',`CREATE TABLE penulis (id INTEGER PRIMARY KEY, nama TEXT NOT NULL);
CREATE TABLE buku (
  id INTEGER PRIMARY KEY,
  judul TEXT NOT NULL,
  genre TEXT,
  harga INTEGER CHECK (harga > 0),
  stok INTEGER NOT NULL DEFAULT 0 CHECK (stok >= 0)
);
CREATE TABLE buku_penulis (
  buku_id INTEGER REFERENCES buku(id),
  penulis_id INTEGER REFERENCES penulis(id),
  PRIMARY KEY (buku_id, penulis_id)
);
INSERT INTO penulis VALUES (1,'Andrea Hirata'),(2,'Dee Lestari'),(3,'Tere Liye');
INSERT INTO buku VALUES (1,'Laskar Pelangi','Novel',89000,12),(2,'Supernova','Novel',99000,5),(3,'Hujan','Novel',95000,0);
INSERT INTO buku_penulis VALUES (1,1),(2,2),(3,3);
SELECT b.judul, p.nama, b.stok FROM buku b
JOIN buku_penulis bp ON bp.buku_id = b.id
JOIN penulis p ON p.id = bp.penulis_id
ORDER BY b.judul;`]],sql:{db:'kosong',file:0}}]});
})();
