/* ===================== DATABASE CONTOH =====================
   "Toko Nusantara": pelanggan, produk, pesanan, detail_pesanan, karyawan, rekening. */
const SEED={toko:`CREATE TABLE pelanggan (
  id INTEGER PRIMARY KEY,
  nama TEXT NOT NULL,
  kota TEXT,
  bergabung DATE
);
INSERT INTO pelanggan VALUES
 (1,'Andi','Jakarta','2023-01-15'),
 (2,'Budi','Bandung','2023-03-02'),
 (3,'Citra','Surabaya','2023-06-20'),
 (4,'Dewi','Jakarta','2024-01-08'),
 (5,'Eko','Medan','2024-02-14'),
 (6,'Fitri','Bandung','2024-05-30'),
 (7,'Gita',NULL,'2024-07-11'),
 (8,'Hadi','Yogyakarta','2024-09-03');
CREATE TABLE produk (
  id INTEGER PRIMARY KEY,
  nama TEXT NOT NULL,
  kategori TEXT NOT NULL,
  harga INTEGER CHECK (harga > 0),
  stok INTEGER DEFAULT 0
);
INSERT INTO produk VALUES
 (1,'Kopi Gayo','Minuman',85000,40),
 (2,'Teh Melati','Minuman',25000,120),
 (3,'Keripik Singkong','Camilan',15000,200),
 (4,'Kacang Mete','Camilan',60000,35),
 (5,'Sambal Bawang','Bumbu',30000,80),
 (6,'Madu Hutan','Minuman',120000,15),
 (7,'Rendang Kaleng','Makanan',75000,0),
 (8,'Kerupuk Udang','Camilan',20000,150);
CREATE TABLE pesanan (
  id INTEGER PRIMARY KEY,
  pelanggan_id INTEGER REFERENCES pelanggan(id),
  tanggal DATE NOT NULL,
  status TEXT DEFAULT 'baru'
);
INSERT INTO pesanan VALUES
 (101,1,'2024-10-01','selesai'),
 (102,2,'2024-10-03','selesai'),
 (103,1,'2024-10-07','dikirim'),
 (104,3,'2024-10-12','selesai'),
 (105,4,'2024-10-15','batal'),
 (106,2,'2024-10-20','selesai'),
 (107,6,'2024-11-02','dikirim'),
 (108,1,'2024-11-05','baru'),
 (109,5,'2024-11-09','selesai'),
 (110,8,'2024-11-15','baru');
CREATE TABLE detail_pesanan (
  pesanan_id INTEGER REFERENCES pesanan(id),
  produk_id INTEGER REFERENCES produk(id),
  jumlah INTEGER NOT NULL CHECK (jumlah > 0),
  PRIMARY KEY (pesanan_id, produk_id)
);
INSERT INTO detail_pesanan VALUES
 (101,1,2),(101,3,5),(102,2,3),(102,8,4),(103,6,1),(104,4,2),(104,3,3),(104,5,1),
 (105,1,1),(106,7,2),(106,2,2),(107,8,10),(108,1,1),(108,6,1),(109,5,6),(110,3,2);
CREATE TABLE karyawan (
  id INTEGER PRIMARY KEY,
  nama TEXT NOT NULL,
  jabatan TEXT,
  atasan_id INTEGER REFERENCES karyawan(id),
  divisi TEXT,
  gaji INTEGER
);
INSERT INTO karyawan VALUES
 (1,'Sari','Direktur',NULL,'Pusat',30000000),
 (2,'Tono','Manajer Gudang',1,'Gudang',15000000),
 (3,'Umi','Manajer Penjualan',1,'Penjualan',16000000),
 (4,'Vino','Staf Gudang',2,'Gudang',7000000),
 (5,'Wati','Staf Gudang',2,'Gudang',7500000),
 (6,'Yudi','Sales',3,'Penjualan',8000000),
 (7,'Zahra','Sales',3,'Penjualan',8500000),
 (8,'Rio','Sales',3,'Penjualan',8000000);
CREATE TABLE rekening (
  id INTEGER PRIMARY KEY,
  pemilik TEXT NOT NULL,
  saldo INTEGER NOT NULL CHECK (saldo >= 0)
);
INSERT INTO rekening VALUES (1,'Andi',500000),(2,'Budi',300000);`};
