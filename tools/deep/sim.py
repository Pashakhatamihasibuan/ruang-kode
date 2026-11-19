"""Pendalaman jalur Sistem Informasi Manajemen (pelajaran khusus SIM; pelajaran lain merujuk ke MSI)."""
K = 'sim'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, code, b=None, lang='text'):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


D = {
'Apa itu sistem informasi manajemen': dict(
  ist=[('SIM', 'Sistem yang mengolah data transaksi menjadi laporan rutin untuk perencanaan, pengendalian, dan pengambilan keputusan manajer.'),
       ('Pengguna SIM', 'Terutama manajer menengah dan supervisor yang memantau kinerja harian sampai bulanan.'),
       ('Periodic report', 'Laporan terjadwal (harian, mingguan, bulanan) dengan format tetap.'),
       ('Ad-hoc query', 'Pertanyaan tak terjadwal yang dijawab dengan menyaring atau mengolah data saat dibutuhkan.')],
  cx=[P('SIM mini: dari catatan kasir menjadi laporan manajer toko', '''
from collections import defaultdict
TRX = [("Sen", "Kopi", 42, 18000), ("Sen", "Teh", 18, 12000), ("Sel", "Kopi", 38, 18000), ("Sel", "Teh", 25, 12000),
       ("Rab", "Kopi", 51, 18000), ("Rab", "Teh", 12, 12000), ("Kam", "Kopi", 47, 18000), ("Kam", "Teh", 20, 12000)]
harian = defaultdict(int); produk = defaultdict(int)
for h, p, q, harga in TRX:
    harian[h] += q * harga; produk[p] += q
TARGET = 1_000_000
print("Laporan harian (target Rp1 juta)")
for h, v in harian.items():
    print(f"  {h}  Rp{v:>9,}  {'tercapai' if v >= TARGET else 'DI BAWAH TARGET'}".replace(",", "."))
print("Laporan produk minggu ini:", dict(produk))
''')]),

'Jenis laporan SIM': dict(
  ist=[('Scheduled report', 'Laporan rutin berjadwal, misalnya rekap penjualan harian.'),
       ('Exception report', 'Hanya menampilkan yang menyimpang dari batas, misalnya stok di bawah minimum.'),
       ('Demand report', 'Dibuat saat diminta, misalnya riwayat transaksi satu pelanggan.'),
       ('Drill-down report', 'Ringkasan yang bisa ditelusuri ke rincian (wilayah → cabang → kasir).')],
  cx=[P('Empat jenis laporan dari data stok yang sama', '''
STOK = {"Beras 5kg": (42, 50), "Minyak 2L": (8, 30), "Gula 1kg": (120, 40), "Telur 1kg": (5, 25), "Mi instan": (300, 100)}
print("SCHEDULED: posisi stok harian")
for b, (s, m) in STOK.items(): print(f"  {b:<10} {s:>4}")
print("EXCEPTION: di bawah stok minimum")
for b, (s, m) in STOK.items():
    if s < m: print(f"  {b:<10} {s:>4} < min {m}  -> pesan {m * 2 - s}")
print("DEMAND: 'berapa stok telur?' ->", STOK["Telur 1kg"][0])
print("DRILL-DOWN: total unit", sum(s for s, _ in STOK.values()), "-> kategori sembako basah: telur", STOK["Telur 1kg"][0])
''')]),

'Merancang laporan yang benar-benar dipakai': dict(
  ist=[('Decision-first design', 'Mulai dari keputusan yang akan diambil pembaca, baru menentukan angka yang ditampilkan.'),
       ('Actionable metric', 'Angka yang jika berubah membuat seseorang tahu apa yang harus dilakukan.'),
       ('Vanity metric', 'Angka yang enak dilihat tetapi tidak membantu keputusan (total unduhan aplikasi sepanjang masa).'),
       ('Report usage analytics', 'Mengukur laporan mana yang benar-benar dibuka; laporan tak terpakai sebaiknya dipensiunkan.')],
  cx=[T('Kartu desain laporan sebelum dibuat', '''
Nama laporan   : Piutang jatuh tempo mingguan
Pembaca        : Manajer keuangan, kepala sales area
Keputusan      : pelanggan mana yang ditelepon minggu ini, siapa yang kreditnya dihentikan
Angka utama    : piutang > 30 hari per pelanggan, umur piutang, limit kredit terpakai
Pembanding     : minggu lalu, rata-rata 3 bulan
Ambang tindakan: > 60 hari = stop kirim; > 45 hari = telepon sales
Frekuensi      : Senin 07.00, dikirim ke email + WA grup
Bukan isi      : total omzet tahunan, grafik pie seluruh pelanggan (tidak membantu keputusan ini)'''),
     P('Laporan mana yang layak dipensiunkan?', '''
LAPORAN = {"Rekap penjualan harian": 412, "Piutang jatuh tempo": 96, "Kunjungan web per jam": 3,
           "Stok di bawah minimum": 230, "Total unduhan aplikasi": 1, "Absensi lembur": 58}
for n, buka in sorted(LAPORAN.items(), key=lambda x: -x[1]):
    print(f"{n:<26} dibuka {buka:>3}x/bulan  {'pertahankan' if buka >= 10 else 'tanya pemilik, lalu pensiunkan'}")
''')]),

'Dari transaksi ke laporan': dict(
  ist=[('Transaction record', 'Catatan satu kejadian bisnis lengkap: siapa, apa, kapan, berapa.'),
       ('Agregasi', 'Menjumlah, merata-rata, atau menghitung data per kelompok (per hari, per cabang).'),
       ('Rekonsiliasi', 'Mencocokkan angka laporan dengan sumber lain (mutasi bank, stok fisik) untuk memastikan benar.'),
       ('Cut-off', 'Batas waktu transaksi masuk periode laporan; penting untuk tutup buku.')],
  cx=[P('Rekonsiliasi penjualan kasir dengan mutasi QRIS', '''
KASIR = [("T-01", "QRIS", 85000), ("T-02", "tunai", 42000), ("T-03", "QRIS", 120000), ("T-04", "QRIS", 33000), ("T-05", "QRIS", 57000)]
MUTASI_QRIS = [("T-01", 85000), ("T-03", 120000), ("T-05", 57000), ("T-09", 40000)]
k = {t: n for t, m, n in KASIR if m == "QRIS"}; b = dict(MUTASI_QRIS)
print("di kasir, tidak ada di bank:", {t: k[t] for t in k.keys() - b.keys()})
print("di bank, tidak ada di kasir:", {t: b[t] for t in b.keys() - k.keys()})
selisih = sum(b.values()) - sum(k.values())
print(f"bank lebih besar Rp{selisih:,} dari catatan kasir -> telusuri T-04 dan T-09".replace(",", "."))
''')]),

'Membangun SIM sederhana dengan spreadsheet': dict(
  ist=[('Tabel data vs tabel laporan', 'Pisahkan sheet input transaksi (satu baris satu kejadian) dari sheet laporan.'),
       ('Data validation', 'Daftar pilihan dan aturan isian agar input konsisten (dropdown cabang, tanggal valid).'),
       ('SUMIFS / pivot table', 'Rumus dan fitur ringkasan untuk laporan per kategori dan periode.'),
       ('Proteksi sheet', 'Mengunci rumus dan laporan agar hanya kolom input yang bisa diubah.')],
  cx=[T('Struktur spreadsheet SIM penjualan yang rapi', '''
Sheet "Transaksi" (input, satu baris = satu penjualan)
  A Tanggal | B Cabang (dropdown) | C Produk (dropdown dari sheet Master) | D Qty | E Harga (otomatis) | F Total = D*E

Sheet "Master"  : daftar produk + harga, daftar cabang (hanya admin yang boleh ubah)

Sheet "Laporan"
  Omzet per cabang bulan ini : =SUMIFS(Transaksi!F:F; Transaksi!B:B; A2; Transaksi!A:A; ">="&$B$1; Transaksi!A:A; "<="&EOMONTH($B$1;0))
  Produk terlaris           : pivot table Produk x Qty, urut menurun
  Hari di bawah target       : conditional formatting merah jika < 1.000.000

Aturan: tidak ada sel gabungan di sheet data, tidak ada baris subtotal di tengah data, satu format tanggal.''', lang='text')]),

'Mengukur keberhasilan SIM': dict(
  ist=[('DeLone & McLean IS success model', 'Model keberhasilan SI: kualitas sistem, informasi, layanan → penggunaan, kepuasan → manfaat bersih.'),
       ('Adoption rate', 'Persentase pengguna sasaran yang benar-benar memakai sistem secara rutin.'),
       ('Before-after measurement', 'Membandingkan metrik proses sebelum dan sesudah sistem diterapkan.'),
       ('Benefit realization', 'Memastikan manfaat yang dijanjikan di business case benar-benar tercapai.')],
  cx=[P('Before-after enam bulan setelah SIM diterapkan', '''
METRIK = [("waktu menyusun laporan bulanan (jam)", 26, 3, "turun"), ("selisih stok fisik vs sistem", 0.071, 0.018, "turun"),
          ("keputusan pembelian telat (kali/bln)", 9, 2, "turun"), ("manajer yang membuka dashboard tiap minggu", 0.30, 0.82, "naik")]
for n, sebelum, sesudah, arah in METRIK:
    perubahan = (sesudah - sebelum) / sebelum
    ok = perubahan < 0 if arah == "turun" else perubahan > 0
    print(f"{n:<44} {sebelum:>6} -> {sesudah:<6} {perubahan:+.0%} {'membaik' if ok else 'memburuk'}")
''')]),

'Bangun SIM mini dengan laporan nyata': dict(
  ist=[('Scope', 'Batas proyek: proses, pengguna, dan laporan yang dicakup.'),
       ('Data dictionary', 'Daftar kolom beserta arti, tipe, contoh, dan aturan validasi.'),
       ('Prototype', 'Versi awal yang bisa dicoba pengguna untuk mendapatkan masukan.'),
       ('Demo & retrospective', 'Presentasi hasil ke pengguna, lalu evaluasi apa yang berhasil dan diperbaiki.')],
  cx=[T('Contoh data dictionary untuk proyek akhir', '''
Kolom        Tipe      Contoh        Aturan                         Arti
tanggal      tanggal   2026-11-19    tidak boleh di masa depan      tanggal transaksi
cabang       teks      MDN           salah satu: MDN, BDG, SBY      kode cabang
produk_id    teks      KOP-0001      ada di tabel master produk     kode produk
qty          bilangan  3             1-999                          jumlah dibeli
harga        rupiah    18000         diambil dari master, > 0       harga satuan saat transaksi
metode_bayar teks      QRIS          tunai, QRIS, transfer          cara bayar''')]),
}
