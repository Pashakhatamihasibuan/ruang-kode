"""Proyek Backend Java berpenyelesaian: 6 mini (dijalankan dengan JDK saat generate) + 4 besar (Spring Boot)."""
from rb_pj_lib import MINI, BESAR, JALUR_M, q, jalan_java

KASIR = r'''import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

public class Main {
    record Produk(String sku, String nama, BigDecimal harga, boolean kenaPpn) {}
    record Item(Produk produk, int qty) {
        BigDecimal subtotal() { return produk.harga().multiply(BigDecimal.valueOf(qty)); }
    }

    static class Keranjang {
        private final Map<String, Item> item = new LinkedHashMap<>();
        void tambah(Produk p, int qty) {
            if (qty <= 0) throw new IllegalArgumentException("qty harus positif");
            item.merge(p.sku(), new Item(p, qty), (a, b) -> new Item(p, a.qty() + b.qty()));
        }
        Collection<Item> isi() { return item.values(); }
    }

    static final BigDecimal PPN = new BigDecimal("0.12");

    static String rp(BigDecimal n) {
        return String.format(Locale.forLanguageTag("id-ID"), "Rp%,d", n.setScale(0, RoundingMode.HALF_UP).longValue());
    }

    static void cetakStruk(Keranjang k, BigDecimal bayar) {
        BigDecimal dpp = BigDecimal.ZERO, ppn = BigDecimal.ZERO;
        for (Item i : k.isi()) {
            dpp = dpp.add(i.subtotal());
            if (i.produk().kenaPpn()) ppn = ppn.add(i.subtotal().multiply(PPN));
        }
        BigDecimal total = dpp.add(ppn).setScale(0, RoundingMode.HALF_UP);
        if (bayar.compareTo(total) < 0) throw new IllegalStateException("uang kurang " + rp(total.subtract(bayar)));

        System.out.println("TOKO NUSANTARA - Medan\n------------------------------------");
        for (Item i : k.isi())
            System.out.printf("%-18s %2d x %-9s%n%36s%n", i.produk().nama(), i.qty(), rp(i.produk().harga()), rp(i.subtotal()));
        System.out.println("------------------------------------");
        String[][] baris = {{"Subtotal", rp(dpp)}, {"PPN 12%", rp(ppn)}, {"TOTAL", rp(total)}, {"Tunai", rp(bayar)}, {"Kembali", rp(bayar.subtract(total))}};
        for (String[] b : baris) System.out.printf("%-12s %23s%n", b[0], b[1]);
    }

    public static void main(String[] args) {
        Produk beras = new Produk("BRS5", "Beras 5 kg", new BigDecimal("78500"), false);
        Produk sabun = new Produk("SBN1", "Sabun cair 450ml", new BigDecimal("23900"), true);
        Produk kopi = new Produk("KPI2", "Kopi bubuk 200g", new BigDecimal("31500"), true);
        Keranjang k = new Keranjang();
        k.tambah(beras, 1); k.tambah(sabun, 2); k.tambah(kopi, 1); k.tambah(sabun, 1);
        cetakStruk(k, new BigDecimal("200000"));
        try {
            cetakStruk(k, new BigDecimal("100000"));
        } catch (IllegalStateException e) {
            System.out.println("\nTransaksi kedua ditolak: " + e.getMessage());
        }
    }
}
'''

PERPUS = r'''import java.time.*;
import java.time.temporal.ChronoUnit;
import java.util.*;

public class Main {
    record Buku(String isbn, String judul) {}
    record Pinjaman(String isbn, String anggota, LocalDate tglPinjam, LocalDate jatuhTempo) {}

    static class BukuTidakTersedia extends RuntimeException { BukuTidakTersedia(String m) { super(m); } }

    static class Perpustakaan {
        static final int MAKS_PINJAM = 2, LAMA_HARI = 7, DENDA_PER_HARI = 1_000;
        private final Map<String, Buku> katalog = new LinkedHashMap<>();
        private final Map<String, Pinjaman> dipinjam = new HashMap<>();
        private final Clock clock;
        Perpustakaan(Clock clock) { this.clock = clock; }

        void tambah(Buku b) { katalog.put(b.isbn(), b); }

        Pinjaman pinjam(String isbn, String anggota) {
            Buku b = Optional.ofNullable(katalog.get(isbn)).orElseThrow(() -> new NoSuchElementException("ISBN tidak dikenal: " + isbn));
            if (dipinjam.containsKey(isbn)) throw new BukuTidakTersedia(b.judul() + " sedang dipinjam");
            long aktif = dipinjam.values().stream().filter(p -> p.anggota().equals(anggota)).count();
            if (aktif >= MAKS_PINJAM) throw new BukuTidakTersedia(anggota + " sudah meminjam " + MAKS_PINJAM + " buku");
            LocalDate hariIni = LocalDate.now(clock);
            Pinjaman p = new Pinjaman(isbn, anggota, hariIni, hariIni.plusDays(LAMA_HARI));
            dipinjam.put(isbn, p);
            return p;
        }

        long kembalikan(String isbn, LocalDate tanggal) {
            Pinjaman p = dipinjam.remove(isbn);
            long telat = Math.max(0, ChronoUnit.DAYS.between(p.jatuhTempo(), tanggal));
            return telat * DENDA_PER_HARI;
        }
    }

    public static void main(String[] args) {
        Clock tetap = Clock.fixed(Instant.parse("2026-11-02T02:00:00Z"), ZoneId.of("Asia/Jakarta"));
        Perpustakaan lib = new Perpustakaan(tetap);
        lib.tambah(new Buku("978-602-1", "Laskar Pelangi"));
        lib.tambah(new Buku("978-602-2", "Bumi Manusia"));
        lib.tambah(new Buku("978-602-3", "Clean Code"));

        System.out.println("Pinjam: " + lib.pinjam("978-602-1", "sari"));
        lib.pinjam("978-602-2", "sari");
        for (String[] uji : new String[][]{{"978-602-3", "sari"}, {"978-602-1", "budi"}, {"978-999", "budi"}}) {
            try { lib.pinjam(uji[0], uji[1]); }
            catch (RuntimeException e) { System.out.println("Ditolak: " + e.getMessage()); }
        }
        System.out.println("Denda tepat waktu : Rp" + lib.kembalikan("978-602-1", LocalDate.of(2026, 11, 9)));
        System.out.println("Denda telat 4 hari: Rp" + lib.kembalikan("978-602-2", LocalDate.of(2026, 11, 13)));
    }
}
'''

MUTASI = r'''import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.*;
import java.util.stream.*;

public class Main {
    record Transaksi(LocalDate tanggal, String keterangan, String kategori, BigDecimal nominal) {}
    record Gagal(int baris, String alasan) {}

    static final String CSV = """
        tanggal,keterangan,nominal
        2026-10-01,GAJI PT MAJU JAYA,8500000
        2026-10-02,QRIS KOPI KENANGAN,-32000
        2026-10-03,TRANSFER KE IBU,-1500000
        2026-10-05,GOJEK GORIDE,-18500
        2026-10-05,QRIS INDOMARET,-87600
        2026-10-07,LISTRIK PLN TOKEN,-200000
        2026-10-08,GOFOOD,abc
        2026-13-09,QRIS ALFAMART,-45000
        2026-10-10,GRAB CAR,-56000
        2026-10-12,QRIS KOPI KENANGAN,-29000
        """;

    static final Map<String, String> ATURAN = new LinkedHashMap<>(Map.of(
        "GAJI", "Pemasukan", "KOPI", "Makan & Minum", "GOFOOD", "Makan & Minum", "GOJEK", "Transportasi",
        "GRAB", "Transportasi", "INDOMARET", "Belanja", "ALFAMART", "Belanja", "PLN", "Tagihan", "TRANSFER", "Transfer"));

    static final Locale ID = Locale.forLanguageTag("id-ID");

    static String kategori(String ket) {
        return ATURAN.entrySet().stream().filter(e -> ket.contains(e.getKey())).map(Map.Entry::getValue).findFirst().orElse("Lainnya");
    }

    public static void main(String[] args) {
        List<Transaksi> ok = new ArrayList<>();
        List<Gagal> gagal = new ArrayList<>();
        String[] baris = CSV.strip().split("\n");
        for (int i = 1; i < baris.length; i++) {
            String[] k = baris[i].split(",");
            try {
                ok.add(new Transaksi(LocalDate.parse(k[0]), k[1], kategori(k[1]), new BigDecimal(k[2])));
            } catch (RuntimeException e) {
                gagal.add(new Gagal(i + 1, e.getClass().getSimpleName()));
            }
        }
        System.out.println("Baris valid: " + ok.size() + ", ditolak: " + gagal);

        Map<String, BigDecimal> keluar = ok.stream().filter(t -> t.nominal().signum() < 0)
            .collect(Collectors.groupingBy(Transaksi::kategori, TreeMap::new,
                Collectors.reducing(BigDecimal.ZERO, t -> t.nominal().negate(), BigDecimal::add)));
        BigDecimal totalKeluar = keluar.values().stream().reduce(BigDecimal.ZERO, BigDecimal::add);
        keluar.entrySet().stream().sorted(Map.Entry.<String, BigDecimal>comparingByValue().reversed())
            .forEach(e -> System.out.printf(ID, "%-14s %,12d  %5.1f%%%n", e.getKey(), e.getValue().longValue(),
                e.getValue().doubleValue() * 100 / totalKeluar.doubleValue()));
        BigDecimal masuk = ok.stream().map(Transaksi::nominal).filter(n -> n.signum() > 0).reduce(BigDecimal.ZERO, BigDecimal::add);
        System.out.printf(ID, "Pemasukan %,d | Pengeluaran %,d | Rasio tabungan %.1f%%%n", masuk.longValue(), totalKeluar.longValue(),
            masuk.subtract(totalKeluar).doubleValue() * 100 / masuk.doubleValue());
    }
}
'''

RATE = r'''import java.util.*;

public class Main {
    interface Jam { long milis(); }

    static class JamPalsu implements Jam {
        long t = 0;
        public long milis() { return t; }
        void maju(long ms) { t += ms; }
    }

    /** Token bucket per API key: kapasitas token, isi ulang per detik. */
    static class RateLimiter {
        private record Ember(double token, long terakhir) {}
        private final Map<String, Ember> ember = new HashMap<>();
        private final int kapasitas; private final double isiPerDetik; private final Jam jam;
        RateLimiter(int kapasitas, double isiPerDetik, Jam jam) { this.kapasitas = kapasitas; this.isiPerDetik = isiPerDetik; this.jam = jam; }

        synchronized boolean izinkan(String key) {
            long now = jam.milis();
            Ember e = ember.getOrDefault(key, new Ember(kapasitas, now));
            double token = Math.min(kapasitas, e.token() + (now - e.terakhir()) / 1000.0 * isiPerDetik);
            boolean boleh = token >= 1;
            ember.put(key, new Ember(boleh ? token - 1 : token, now));
            return boleh;
        }
    }

    static class LruCache<K, V> extends LinkedHashMap<K, V> {
        private final int maks; int hit, miss;
        LruCache(int maks) { super(16, 0.75f, true); this.maks = maks; }
        @Override protected boolean removeEldestEntry(Map.Entry<K, V> e) { return size() > maks; }
        V ambil(K k, java.util.function.Function<K, V> muat) {
            V v = get(k);
            if (v != null) { hit++; return v; }
            miss++; v = muat.apply(k); put(k, v); return v;
        }
    }

    public static void main(String[] args) {
        JamPalsu jam = new JamPalsu();
        RateLimiter rl = new RateLimiter(5, 2, jam); // burst 5, lalu 2 permintaan/detik
        StringBuilder log = new StringBuilder();
        for (int i = 0; i < 8; i++) log.append(rl.izinkan("key-A") ? "200 " : "429 ");
        System.out.println("8 request sekaligus : " + log);
        jam.maju(1500);
        log.setLength(0);
        for (int i = 0; i < 4; i++) log.append(rl.izinkan("key-A") ? "200 " : "429 ");
        System.out.println("1,5 detik kemudian  : " + log);
        System.out.println("Key lain tidak ikut terbatas: " + (rl.izinkan("key-B") ? "200" : "429"));

        LruCache<String, String> cache = new LruCache<>(3);
        String[] akses = {"p1", "p2", "p1", "p3", "p4", "p1", "p2", "p1"};
        for (String k : akses) cache.ambil(k, id -> "produk " + id + " dari DB");
        System.out.printf("Cache hit %d, miss %d, isi sekarang %s%n", cache.hit, cache.miss, cache.keySet());
    }
}
'''

TIKET = r'''import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

public class Main {
    /** Stok tiket tanpa overselling: compare-and-set atomik, bukan "cek lalu kurangi". */
    static class StokTiket {
        private final AtomicInteger sisa;
        StokTiket(int awal) { sisa = new AtomicInteger(awal); }
        boolean pesan(int jumlah) {
            while (true) {
                int s = sisa.get();
                if (s < jumlah) return false;
                if (sisa.compareAndSet(s, s - jumlah)) return true;
            }
        }
        int sisa() { return sisa.get(); }
    }

    /** Versi salah untuk perbandingan: cek dan kurangi tidak atomik. */
    static class StokNaif {
        int sisa;
        StokNaif(int awal) { sisa = awal; }
        boolean pesan(int jumlah) {
            if (sisa >= jumlah) { Thread.yield(); sisa -= jumlah; return true; }
            return false;
        }
    }

    public static void main(String[] args) throws Exception {
        int kuota = 1_000, pembeli = 5_000;
        StokTiket stok = new StokTiket(kuota);
        Set<Integer> idempoten = ConcurrentHashMap.newKeySet();
        AtomicInteger berhasil = new AtomicInteger(), duplikat = new AtomicInteger();
        try (ExecutorService ex = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < pembeli; i++) {
                int idRequest = i % 4_500; // 500 request dikirim ulang (klik dua kali / retry)
                ex.submit(() -> {
                    if (!idempoten.add(idRequest)) { duplikat.incrementAndGet(); return; }
                    if (stok.pesan(1)) berhasil.incrementAndGet();
                });
            }
        }
        System.out.println("Tiket terjual : " + berhasil.get() + " dari kuota " + kuota);
        System.out.println("Sisa stok     : " + stok.sisa());
        System.out.println("Request ganda : " + duplikat.get() + " diabaikan (idempotency key)");
        System.out.println("Overselling   : " + (berhasil.get() > kuota ? "YA" : "tidak"));
    }
}
'''

KURIR = r'''import java.util.*;

public class Main {
    record Jalan(String ke, int menit) {}

    static Map<String, List<Jalan>> peta = new TreeMap<>();
    static void hubung(String a, String b, int menit) {
        peta.computeIfAbsent(a, k -> new ArrayList<>()).add(new Jalan(b, menit));
        peta.computeIfAbsent(b, k -> new ArrayList<>()).add(new Jalan(a, menit));
    }

    static List<String> rute(String asal, String tujuan, Map<String, Integer> jarakOut) {
        Map<String, Integer> jarak = new HashMap<>();
        Map<String, String> dari = new HashMap<>();
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(Map.Entry.comparingByValue());
        jarak.put(asal, 0);
        pq.add(Map.entry(asal, 0));
        while (!pq.isEmpty()) {
            var cur = pq.poll();
            if (cur.getValue() > jarak.get(cur.getKey())) continue;
            if (cur.getKey().equals(tujuan)) break;
            for (Jalan j : peta.getOrDefault(cur.getKey(), List.of())) {
                int baru = cur.getValue() + j.menit();
                if (baru < jarak.getOrDefault(j.ke(), Integer.MAX_VALUE)) {
                    jarak.put(j.ke(), baru);
                    dari.put(j.ke(), cur.getKey());
                    pq.add(Map.entry(j.ke(), baru));
                }
            }
        }
        if (!jarak.containsKey(tujuan)) return List.of();
        LinkedList<String> jalur = new LinkedList<>();
        for (String s = tujuan; s != null; s = dari.get(s)) jalur.addFirst(s);
        jarakOut.put(tujuan, jarak.get(tujuan));
        return jalur;
    }

    public static void main(String[] args) {
        hubung("Gudang Tanjung Morawa", "Amplas", 25);
        hubung("Gudang Tanjung Morawa", "Pancing", 40);
        hubung("Amplas", "Medan Kota", 15);
        hubung("Amplas", "Pancing", 18);
        hubung("Medan Kota", "Petisah", 12);
        hubung("Pancing", "Petisah", 30);
        hubung("Petisah", "Sunggal", 14);
        hubung("Medan Kota", "Sunggal", 28);

        for (String tujuan : List.of("Petisah", "Sunggal", "Binjai")) {
            Map<String, Integer> menit = new HashMap<>();
            List<String> r = rute("Gudang Tanjung Morawa", tujuan, menit);
            System.out.println(tujuan + ": " + (r.isEmpty() ? "tidak terjangkau" : String.join(" -> ", r) + " (" + menit.get(tujuan) + " menit)"));
        }
    }
}
'''

JV_MINI = [
MINI(1, 'Sistem kasir minimarket dengan struk dan PPN',
  'Minimarket di Medan masih menghitung manual. Mereka butuh modul kasir: produk ada yang kena PPN 12% dan ada yang tidak (beras), item yang sama digabung, kembalian dihitung, dan transaksi ditolak jika uang kurang.',
  ['Model domain dengan record: Produk, Item', 'Keranjang menggabungkan item dengan SKU sama', 'Perhitungan uang memakai BigDecimal, bukan double', 'Struk rapi dengan format rupiah Indonesia', 'Tolak transaksi jika uang kurang (exception domain)'],
  ['Definisikan <code>record Produk</code> dengan flag <code>kenaPpn</code> dan <code>record Item</code> dengan method <code>subtotal()</code>.', 'Simpan item di <code>LinkedHashMap</code> berkunci SKU; <code>merge</code> menjumlahkan qty.', 'Semua harga <code>BigDecimal</code>; pembulatan <code>HALF_UP</code> hanya di akhir.', '<code>String.format(Locale "id-ID", "%,d")</code> menghasilkan titik ribuan.', 'Bandingkan dengan <code>compareTo</code>; lempar <code>IllegalStateException</code> berisi kekurangannya.'],
  KASIR, 'java', out=jalan_java(KASIR),
  kunci='tambahkan diskon per item, poin member, dan simpan transaksi ke berkas CSV harian.',
  cek=q('Kenapa harga disimpan sebagai BigDecimal?', ['double tidak bisa menyimpan desimal tertentu dengan tepat sehingga total bisa meleset', 'BigDecimal lebih cepat', 'Karena wajib di Java 21'], 0, 'Uang harus presisi.')),

MINI(2, 'Peminjaman perpustakaan dengan denda',
  'Perpustakaan sekolah ingin aturan pinjam yang konsisten: maksimal 2 buku per anggota, lama pinjam 7 hari, denda Rp1.000 per hari terlambat, dan buku yang sedang dipinjam tidak bisa dipinjam orang lain.',
  ['Katalog buku dan daftar pinjaman aktif', 'Aturan maksimal pinjam dan ketersediaan buku', 'Exception yang jelas untuk setiap penolakan', 'Denda dihitung dengan java.time', 'Waktu disuntikkan (Clock) agar bisa diuji'],
  ['<code>Map&lt;String, Buku&gt;</code> untuk katalog dan <code>Map&lt;String, Pinjaman&gt;</code> untuk buku yang sedang keluar.', 'Cek urut: ISBN dikenal → buku tersedia → kuota anggota.', 'Buat <code>BukuTidakTersedia extends RuntimeException</code> dengan pesan yang bisa ditampilkan ke petugas.', '<code>ChronoUnit.DAYS.between(jatuhTempo, tanggalKembali)</code>; denda tidak boleh negatif.', 'Konstruktor menerima <code>Clock</code>; tes memakai <code>Clock.fixed</code>.'],
  PERPUS, 'java', out=jalan_java(PERPUS),
  kunci='tambahkan reservasi (antrean per buku dengan <code>Queue</code>) dan perpanjangan pinjaman satu kali.',
  cek=q('Kenapa Clock disuntikkan ke kelas Perpustakaan?', ['Agar tanggal bisa dibuat tetap saat pengujian sehingga hasil tes selalu sama', 'Agar lebih cepat', 'Karena LocalDate tidak bisa dipakai tanpa Clock'], 0, 'Kode yang bergantung waktu harus bisa diuji.')),

MINI(3, 'Analisis mutasi rekening dari CSV',
  'Aplikasi keuangan pribadi menerima ekspor mutasi bank berformat CSV. Sebagian baris rusak. Pengguna ingin tahu ke mana uangnya pergi per kategori dan berapa rasio tabungannya.',
  ['Parsing CSV dengan validasi per baris (baris rusak dicatat, bukan menghentikan program)', 'Kategorisasi otomatis berdasarkan kata kunci keterangan', 'Ringkasan pengeluaran per kategori beserta persentasenya', 'Rasio tabungan = (pemasukan − pengeluaran) ÷ pemasukan'],
  ['Baca baris demi baris; bungkus parsing dengan try-catch dan simpan nomor baris yang gagal.', 'Peta kata kunci → kategori; ambil kecocokan pertama, sisanya "Lainnya".', '<code>Collectors.groupingBy</code> + <code>reducing</code> dengan BigDecimal.', 'Urutkan kategori dari pengeluaran terbesar agar langsung terlihat prioritas penghematan.'],
  MUTASI, 'java', out=jalan_java(MUTASI),
  kunci='baca berkas CSV sungguhan dengan <code>Files.lines</code>, dukung format beberapa bank, dan ekspor ringkasan ke JSON.',
  cek=q('Kenapa baris CSV yang rusak dicatat dan dilewati, bukan menghentikan seluruh proses?', ['Satu baris rusak tidak boleh membuat ribuan baris valid gagal diproses; baris rusak dilaporkan untuk diperbaiki', 'Agar program lebih pendek', 'Karena Java tidak bisa berhenti'], 0, 'Pola umum di data pipeline.')),

MINI(4, 'Rate limiter dan cache untuk API publik',
  'API katalog produk sering dibanjiri request dari satu klien sehingga melambat untuk semua orang. Tim butuh pembatas laju per API key dan cache untuk produk yang sering diminta.',
  ['Token bucket: burst 5 request, lalu 2 request/detik per API key', 'Balas 429 Too Many Requests saat token habis', 'Jam bisa dipalsukan agar perilaku bisa diuji tanpa menunggu', 'LRU cache dengan statistik hit dan miss'],
  ['Simpan <code>(token, waktu terakhir)</code> per key; isi ulang token sebanding waktu yang berlalu.', 'Method <code>synchronized</code> agar aman dipanggil banyak thread.', 'Antarmuka <code>Jam</code> dengan implementasi palsu untuk tes.', '<code>LinkedHashMap</code> dengan access-order dan <code>removeEldestEntry</code>.'],
  RATE, 'java', out=jalan_java(RATE),
  kunci='pindahkan penyimpanan token ke Redis agar berlaku di banyak instance server, dan tambahkan header <code>Retry-After</code>.',
  cek=q('Kode status HTTP yang tepat saat klien melebihi batas laju?', ['429 Too Many Requests', '404 Not Found', '500 Internal Server Error'], 0, 'Sertakan header Retry-After.')),

MINI(5, 'Penjualan tiket konser tanpa overselling',
  'Saat war tiket, 5.000 orang menekan tombol beli hampir bersamaan untuk 1.000 kursi. Sebagian menekan dua kali. Sistem tidak boleh menjual lebih dari kuota dan tidak boleh mencatat pesanan ganda.',
  ['Simulasi 5.000 request bersamaan dengan virtual thread', 'Pengurangan stok atomik (compare-and-set)', 'Idempotency key: request yang dikirim ulang tidak diproses dua kali', 'Laporan: terjual, sisa, request ganda, dan bukti tidak ada overselling'],
  ['<code>Executors.newVirtualThreadPerTaskExecutor()</code> untuk ribuan tugas ringan.', 'Loop <code>compareAndSet</code> pada <code>AtomicInteger</code>: kurangi hanya jika nilai belum berubah.', '<code>ConcurrentHashMap.newKeySet()</code>; <code>add</code> mengembalikan false untuk ID yang sudah ada.', 'Di database nyata, gunakan <code>UPDATE ... WHERE sisa &gt;= 1</code> atau <code>SELECT ... FOR UPDATE</code>.'],
  TIKET, 'java', out=jalan_java(TIKET),
  kunci='ganti stok di memori dengan PostgreSQL dan uji dengan 2 instance aplikasi; bandingkan penguncian optimistik dan pesimistik.',
  cek=q('Kenapa pola "if (sisa >= 1) sisa--" tidak aman di banyak thread?', ['Dua thread bisa sama-sama lolos pengecekan sebelum salah satunya mengurangi stok', 'Karena if lambat', 'Karena int tidak bisa dikurangi'], 0, 'Check-then-act harus atomik.')),

MINI(6, 'Rute tercepat kurir antar kecamatan',
  'Jasa kurir lokal di Medan ingin menentukan rute tercepat dari gudang ke setiap kecamatan berdasarkan perkiraan waktu tempuh, termasuk mendeteksi tujuan yang tidak terjangkau.',
  ['Peta jalan sebagai graf berbobot (menit)', 'Algoritma Dijkstra dengan PriorityQueue', 'Rekonstruksi jalur, bukan hanya total menit', 'Tangani tujuan yang tidak terhubung'],
  ['Adjacency list: <code>Map&lt;String, List&lt;Jalan&gt;&gt;</code>, jalan dua arah.', 'Ambil simpul dengan jarak terkecil dari heap; perbarui tetangga jika lebih cepat.', 'Simpan <code>dari</code> untuk setiap simpul lalu telusuri mundur dari tujuan.', 'Jika tujuan tidak pernah dicapai, kembalikan daftar kosong dan laporkan.'],
  KURIR, 'java', out=jalan_java(KURIR),
  kunci='tambahkan jam sibuk (bobot berubah per jam) dan urutan antar beberapa alamat (traveling salesman sederhana dengan heuristik nearest neighbor).',
  cek=q('Struktur data yang membuat Dijkstra efisien?', ['Priority queue (heap) untuk mengambil simpul dengan jarak terkecil', 'Stack', 'Array tanpa urutan'], 0, 'O((V + E) log V).')),
]

JV_BESAR = [
BESAR(1, 'REST API e-commerce dengan Spring Boot dan PostgreSQL',
  'UMKM fesyen ingin pindah dari marketplace ke toko sendiri. Mereka butuh backend untuk katalog, keranjang, checkout, dan panel admin yang aman, terdokumentasi, dan siap dipakai aplikasi web serta mobile.',
  ['API REST berversi (/api/v1) dengan validasi dan format error standar (RFC 9457 Problem Details)', 'Autentikasi JWT + refresh token, peran ADMIN dan PELANGGAN', 'Migrasi database dengan Flyway, tidak ada perubahan skema manual', 'Checkout transaksional: stok berkurang dan pesanan tercatat bersama', 'Integration test dengan Testcontainers (PostgreSQL asli) dan dokumentasi OpenAPI'],
  'Java 21, Spring Boot 3, Spring Security, Spring Data JPA, PostgreSQL 16, Flyway, Testcontainers, springdoc-openapi, Docker',
  [('Lapisan', 'controller (DTO + validasi) → service (aturan bisnis, @Transactional) → repository (JPA)'), ('Paket', 'per fitur: katalog, keranjang, pesanan, auth'),
   ('Database', 'produk, varian(sku, ukuran, warna, stok), pelanggan, pesanan, item_pesanan; migrasi V1__, V2__'), ('Keamanan', 'JWT akses 15 menit + refresh token di DB; BCrypt; CORS hanya domain toko'),
   ('Kualitas', 'JUnit 5 + Mockito untuk service, Testcontainers untuk repository dan API, JaCoCo ≥ 70%'), ('Deploy', 'Docker image multi-stage, docker compose untuk lokal, CI GitHub Actions')],
  ['Rancang ERD dan kontrak API (OpenAPI) dulu; sepakati dengan tim frontend.', 'Buat migrasi Flyway dan entity; uji repository dengan Testcontainers.', 'Tulis service checkout dengan <code>@Transactional</code> dan pengurangan stok bersyarat.', 'Tambahkan Spring Security: endpoint publik (katalog), pelanggan (keranjang), admin (kelola produk).', 'Seragamkan error dengan <code>@RestControllerAdvice</code> + <code>ProblemDetail</code>.', 'Kemas dengan Docker, jalankan CI, dan tulis README dengan cara menjalankan dalam satu perintah.'],
  r'''// src/main/resources/db/migration/V1__skema_awal.sql
CREATE TABLE produk (id BIGSERIAL PRIMARY KEY, nama TEXT NOT NULL, harga NUMERIC(12,0) NOT NULL CHECK (harga > 0), aktif BOOLEAN DEFAULT true);
CREATE TABLE varian (id BIGSERIAL PRIMARY KEY, produk_id BIGINT REFERENCES produk(id), sku TEXT UNIQUE NOT NULL, ukuran TEXT, stok INT NOT NULL CHECK (stok >= 0));
CREATE TABLE pesanan (id BIGSERIAL PRIMARY KEY, pelanggan_id BIGINT NOT NULL, status TEXT NOT NULL, total NUMERIC(12,0) NOT NULL, dibuat_pada TIMESTAMPTZ DEFAULT now());
CREATE TABLE item_pesanan (pesanan_id BIGINT REFERENCES pesanan(id), varian_id BIGINT REFERENCES varian(id), qty INT CHECK (qty > 0), harga NUMERIC(12,0), PRIMARY KEY (pesanan_id, varian_id));

// pesanan/CheckoutRequest.java
public record CheckoutRequest(@NotEmpty List<@Valid Baris> item, @NotBlank String alamat) {
    public record Baris(@NotNull Long varianId, @Min(1) @Max(10) int qty) {}
}

// katalog/VarianRepository.java
public interface VarianRepository extends JpaRepository<Varian, Long> {
    @Modifying
    @Query("update Varian v set v.stok = v.stok - :qty where v.id = :id and v.stok >= :qty")
    int kurangiStok(@Param("id") Long id, @Param("qty") int qty);
}

// pesanan/CheckoutService.java
@Service
@RequiredArgsConstructor
public class CheckoutService {
    private final VarianRepository varian;
    private final PesananRepository pesanan;

    @Transactional
    public PesananResponse checkout(Long pelangganId, CheckoutRequest req) {
        var p = new Pesanan(pelangganId, Status.MENUNGGU_BAYAR, req.alamat());
        for (var b : req.item()) {
            var v = varian.findById(b.varianId()).orElseThrow(() -> new TidakDitemukan("varian " + b.varianId()));
            if (varian.kurangiStok(v.getId(), b.qty()) == 0) throw new StokHabis(v.getSku());
            p.tambahItem(v, b.qty());
        }
        return PesananResponse.dari(pesanan.save(p)); // gagal di mana pun -> seluruh transaksi rollback
    }
}

// pesanan/PesananController.java
@RestController
@RequestMapping("/api/v1/pesanan")
@RequiredArgsConstructor
class PesananController {
    private final CheckoutService checkout;

    @PostMapping
    @PreAuthorize("hasRole('PELANGGAN')")
    ResponseEntity<PesananResponse> buat(@AuthenticationPrincipal Jwt jwt, @Valid @RequestBody CheckoutRequest req) {
        var hasil = checkout.checkout(Long.valueOf(jwt.getSubject()), req);
        return ResponseEntity.created(URI.create("/api/v1/pesanan/" + hasil.id())).body(hasil);
    }
}

// common/PenanganError.java
@RestControllerAdvice
class PenanganError {
    @ExceptionHandler(StokHabis.class)
    ProblemDetail stokHabis(StokHabis e) {
        var pd = ProblemDetail.forStatusAndDetail(HttpStatus.CONFLICT, "Stok " + e.sku() + " tidak mencukupi");
        pd.setType(URI.create("https://tokofesyen.id/errors/stok-habis"));
        return pd;
    }
}

// test: pesanan/CheckoutIT.java
@SpringBootTest @Testcontainers
class CheckoutIT {
    @Container @ServiceConnection static PostgreSQLContainer<?> db = new PostgreSQLContainer<>("postgres:16");
    @Autowired CheckoutService service; @Autowired VarianRepository varian;

    @Test void stokTidakBolehMinus() {
        assertThrows(StokHabis.class, () -> service.checkout(1L, new CheckoutRequest(List.of(new Baris(SKU_STOK_1, 2)), "Medan")));
        assertEquals(1, varian.findById(SKU_STOK_1).orElseThrow().getStok()); // rollback terbukti
    }
}''',
  'java', standar='migrasi berversi, validasi input, error format standar, transaksi teruji dengan database asli, OpenAPI, CI hijau, satu perintah untuk menjalankan',
  cek=q('Kenapa integration test memakai Testcontainers, bukan H2 in-memory?', ['Perilaku PostgreSQL asli (constraint, tipe data, query) bisa berbeda dari H2, jadi bug baru ketahuan di produksi', 'Agar tes lebih lambat', 'Karena H2 tidak bisa dipakai Spring'], 0, 'Uji dengan database yang sama dengan produksi.')),

BESAR(2, 'Layanan pembayaran QRIS dengan idempotency dan outbox',
  'Platform tiket event menerima pembayaran QRIS dan virtual account lewat payment gateway. Masalahnya: webhook kadang terkirim dua kali, layanan email/e-tiket kadang mati, dan tim keuangan menemukan selisih saat rekonsiliasi.',
  ['Endpoint buat pembayaran dengan Idempotency-Key', 'Webhook diverifikasi tanda tangannya (HMAC) dan diproses idempoten', 'Transactional outbox: event "PembayaranLunas" dijamin terkirim ke Kafka meski broker sempat mati', 'State machine status pembayaran yang tidak bisa mundur', 'Job rekonsiliasi harian dengan laporan selisih'],
  'Java 21, Spring Boot 3, PostgreSQL, Kafka (atau Redpanda), Resilience4j, Micrometer + Prometheus, Testcontainers',
  [('Tabel', 'pembayaran(id, order_id, status, nominal, versi), idempotensi(key, hash_body, respons), outbox(id, tipe, payload, terkirim_pada)'), ('Status', 'DIBUAT → MENUNGGU → LUNAS | KEDALUWARSA | GAGAL; tidak ada transisi mundur'),
   ('Webhook', 'verifikasi HMAC → cari pembayaran → transisi status + tulis outbox dalam 1 transaksi → 200 OK'), ('Outbox relay', 'scheduler membaca outbox yang belum terkirim, publish ke Kafka, tandai terkirim'),
   ('Ketahanan', 'Resilience4j: timeout + retry + circuit breaker saat memanggil gateway'), ('Observabilitas', 'metrik pembayaran_lunas_total, latensi webhook, umur outbox tertua')],
  ['Modelkan state machine pembayaran dan tulis unit test untuk setiap transisi.', 'Implementasikan Idempotency-Key: simpan hash body dan respons; request ulang mendapat respons yang sama.', 'Verifikasi webhook dengan HMAC dan perbandingan waktu konstan; tolak tanda tangan salah dengan 401.', 'Tulis perubahan status dan baris outbox dalam satu transaksi database.', 'Buat relay outbox dan konsumen di layanan e-tiket yang juga idempoten.', 'Jadwalkan rekonsiliasi: bandingkan laporan settlement gateway dengan tabel pembayaran, kirim selisih ke Slack.'],
  r'''public enum Status {
    DIBUAT, MENUNGGU, LUNAS, KEDALUWARSA, GAGAL;
    private static final Map<Status, Set<Status>> BOLEH = Map.of(
        DIBUAT, Set.of(MENUNGGU, GAGAL), MENUNGGU, Set.of(LUNAS, KEDALUWARSA, GAGAL),
        LUNAS, Set.of(), KEDALUWARSA, Set.of(), GAGAL, Set.of());
    public boolean bisaKe(Status s) { return BOLEH.get(this).contains(s); }
}

@RestController
@RequiredArgsConstructor
class WebhookController {
    private final WebhookService service;
    @Value("${gateway.webhook-secret}") private String rahasia;

    @PostMapping("/webhook/gateway")
    ResponseEntity<Void> terima(@RequestHeader("X-Signature") String tanda, @RequestBody String body) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(rahasia.getBytes(UTF_8), "HmacSHA256"));
        byte[] harapan = HexFormat.of().formatHex(mac.doFinal(body.getBytes(UTF_8))).getBytes(UTF_8);
        if (!MessageDigest.isEqual(harapan, tanda.getBytes(UTF_8))) return ResponseEntity.status(401).build();
        service.proses(objectMapper.readValue(body, NotifikasiGateway.class));
        return ResponseEntity.ok().build(); // gateway berhenti mengirim ulang setelah 200
    }
}

@Service
@RequiredArgsConstructor
class WebhookService {
    private final PembayaranRepository repo;
    private final OutboxRepository outbox;

    @Transactional
    public void proses(NotifikasiGateway n) {
        Pembayaran p = repo.findByOrderIdForUpdate(n.orderId()).orElseThrow();
        Status baru = n.status().equals("settlement") ? Status.LUNAS : Status.GAGAL;
        if (p.getStatus() == baru) return;                 // webhook ganda: abaikan (idempoten)
        if (!p.getStatus().bisaKe(baru)) throw new TransisiTidakSah(p.getStatus(), baru);
        if (p.getNominal().compareTo(n.nominal()) != 0) throw new NominalTidakCocok(n.orderId());
        p.setStatus(baru);
        outbox.save(Outbox.event("PembayaranLunas", Map.of("orderId", n.orderId(), "nominal", n.nominal())));
        // commit: status dan event tersimpan bersama, atau tidak sama sekali
    }
}

@Component
@RequiredArgsConstructor
class OutboxRelay {
    private final OutboxRepository outbox;
    private final KafkaTemplate<String, String> kafka;

    @Scheduled(fixedDelay = 1000)
    @Transactional
    public void kirim() {
        for (Outbox o : outbox.ambilBelumTerkirim(100)) {   // SELECT ... FOR UPDATE SKIP LOCKED
            kafka.send("pembayaran", o.getAgregatId(), o.getPayload()).join();
            o.tandaiTerkirim(Instant.now());
        }
    }
}''',
  'java', standar='idempotensi teruji (request dan webhook ganda), tanda tangan webhook diverifikasi, outbox menjamin event, state machine tanpa transisi mundur, rekonsiliasi harian',
  cek=q('Masalah apa yang diselesaikan transactional outbox?', ['Perubahan database dan pengiriman event bisa tidak sinkron jika broker gagal; outbox membuat keduanya tercatat dalam satu transaksi', 'Mempercepat query', 'Mengganti Kafka'], 0, 'Dual-write problem.')),

BESAR(3, 'Sistem reservasi klinik berkapasitas tinggi',
  'Jaringan klinik dengan 40 cabang membuka pendaftaran online pukul 06.00 setiap hari dan diserbu ribuan pasien sekaligus. Sistem lama sering down dan terjadi double booking pada slot dokter.',
  ['Slot dokter per 15 menit tanpa double booking (constraint database)', 'Tahan lonjakan 2.000 request/detik saat pembukaan', 'Antrean virtual saat beban puncak dan notifikasi WhatsApp/SMS asinkron', 'Cache jadwal di Redis dengan invalidasi saat slot berubah', 'Uji beban (k6) dan target SLO: p95 < 300 ms, error < 0,1%'],
  'Java 21 (virtual thread), Spring Boot 3, PostgreSQL, Redis, RabbitMQ, k6, Grafana',
  [('Data', 'slot(dokter_id, mulai, status) dengan UNIQUE(dokter_id, mulai); reservasi(slot_id UNIQUE, pasien_id)'), ('Konkurensi', 'INSERT reservasi dengan unique constraint: pemenang tunggal per slot, yang kalah mendapat 409'),
   ('Skala', 'spring.threads.virtual.enabled=true; HikariCP dibatasi sesuai kapasitas DB'), ('Cache', 'jadwal per cabang per hari di Redis, TTL 30 detik + invalidasi event'),
   ('Asinkron', 'event ReservasiDibuat → RabbitMQ → layanan notifikasi'), ('Uji', 'k6: ramp 0 → 2.000 rps dalam 60 detik; ambang p95 dan error rate di CI')],
  ['Tentukan SLO dan skenario beban bersama tim operasional klinik.', 'Rancang tabel dengan unique constraint sebagai pertahanan terakhir terhadap double booking.', 'Aktifkan virtual thread dan ukur; batasi pool koneksi agar database tidak tumbang.', 'Tambahkan cache Redis untuk endpoint jadwal (paling sering dibaca).', 'Kirim notifikasi lewat antrean agar API tetap cepat walau penyedia SMS lambat.', 'Jalankan k6, temukan bottleneck dengan metrik dan trace, ulangi sampai SLO tercapai.'],
  r'''# application.yml
spring:
  threads.virtual.enabled: true
  datasource.hikari.maximum-pool-size: 40      # batas koneksi DB, bukan batas request
  data.redis.host: redis

// ReservasiService.java
@Service
@RequiredArgsConstructor
class ReservasiService {
    private final JdbcClient jdbc;
    private final RabbitTemplate mq;
    private final CacheManager cache;

    @Transactional
    public Reservasi pesan(long slotId, long pasienId) {
        try {
            long id = jdbc.sql("INSERT INTO reservasi (slot_id, pasien_id) VALUES (?, ?) RETURNING id")
                          .params(slotId, pasienId).query(Long.class).single();
            jdbc.sql("UPDATE slot SET status = 'TERISI' WHERE id = ?").param(slotId).update();
            mq.convertAndSend("reservasi", "dibuat", new ReservasiDibuat(id, slotId, pasienId));
            cache.getCache("jadwal").evict(cabangDari(slotId));
            return new Reservasi(id, slotId, pasienId);
        } catch (DuplicateKeyException e) {
            throw new SlotSudahTerisi(slotId); // -> 409 Conflict, frontend menawarkan slot lain
        }
    }

    @Cacheable(value = "jadwal", key = "#cabangId + ':' + #tanggal")
    public List<SlotDto> jadwal(long cabangId, LocalDate tanggal) {
        return jdbc.sql("SELECT s.id, s.mulai, d.nama, s.status FROM slot s JOIN dokter d ON d.id = s.dokter_id WHERE d.cabang_id = ? AND s.mulai::date = ?")
                   .params(cabangId, tanggal).query(SlotDto.class).list();
    }
}

// k6/pembukaan.js
import http from 'k6/http';
import { check } from 'k6';
export const options = {
  scenarios: { buka: { executor: 'ramping-arrival-rate', startRate: 0, timeUnit: '1s', preAllocatedVUs: 3000,
                       stages: [{ target: 2000, duration: '60s' }, { target: 2000, duration: '120s' }] } },
  thresholds: { http_req_duration: ['p(95)<300'], http_req_failed: ['rate<0.001'] },
};
export default function () {
  const slot = 1 + Math.floor(Math.random() * 5000);
  const r = http.post(`${__ENV.BASE}/api/v1/reservasi`, JSON.stringify({ slotId: slot }), { headers: { 'Content-Type': 'application/json' } });
  check(r, { '201 atau 409': (x) => x.status === 201 || x.status === 409 });
}''',
  'java', standar='tidak ada double booking dalam uji beban, SLO tercapai dan dibuktikan dengan laporan k6, notifikasi asinkron, cache dengan invalidasi',
  cek=q('Kenapa unique constraint di database tetap dibutuhkan walau aplikasi sudah mengecek slot kosong?', ['Pengecekan di aplikasi bisa kalah balapan oleh request lain; constraint database adalah pertahanan terakhir yang pasti', 'Agar query lebih cepat', 'Karena Java tidak bisa mengecek'], 0, 'Biarkan database menjaga invariant.')),

BESAR(4, 'Asisten layanan pelanggan berbasis AI dengan Spring AI',
  'Perusahaan logistik menerima ribuan chat per hari berisi pertanyaan status paket, ongkir, dan klaim. Mereka ingin asisten AI yang menjawab dari data nyata (bukan mengarang), bisa memanggil sistem internal, dan menyerahkan ke agen manusia bila perlu.',
  ['Tool calling: cek status resi dan hitung ongkir dari API internal', 'RAG dari dokumen SOP dan syarat klaim (pgvector)', 'Guardrail: tidak pernah mengubah data tanpa konfirmasi, masking data pribadi, batas biaya per percakapan', 'Eskalasi ke agen manusia dengan ringkasan percakapan', 'Evaluasi otomatis 100 skenario sebelum rilis dan pemantauan kualitas'],
  'Java 21, Spring Boot 3, Spring AI, Claude API, PostgreSQL + pgvector, Redis (memori percakapan), OpenTelemetry',
  [('Model', 'Claude melalui Spring AI ChatClient; model kecil untuk klasifikasi niat, model besar untuk jawaban'), ('Tools', '@Tool cekResi(nomor), hitungOngkir(asal, tujuan, berat), buatTiketKlaim (perlu konfirmasi)'),
   ('Pengetahuan', 'SOP & syarat klaim → chunk → embedding → pgvector; QuestionAnswerAdvisor'), ('Keamanan', 'masking NIK/nomor HP sebelum dikirim ke model; log tanpa PII; rate limit per pengguna'),
   ('Evaluasi', 'golden set 100 percakapan: ketepatan tool, jawaban berdasar sumber, eskalasi tepat'), ('Operasional', 'trace tiap panggilan model: token, biaya, latensi, tool yang dipanggil')],
  ['Kumpulkan 100 contoh percakapan nyata (dianonimkan) dan jawaban yang diharapkan sebagai golden set.', 'Bungkus API internal sebagai tool dengan deskripsi dan validasi parameter yang jelas.', 'Indeks dokumen SOP ke pgvector dan uji ketepatan pencarian dulu.', 'Rangkai ChatClient dengan system prompt, memori percakapan, RAG, dan tool.', 'Tambahkan guardrail: masking PII, konfirmasi untuk aksi yang mengubah data, eskalasi ke manusia.', 'Jalankan evaluasi di CI; rilis bertahap ke 10% pengguna dan pantau CSAT serta tingkat eskalasi.'],
  r'''@Component
class AlatLogistik {
    private final ResiClient resi; private final OngkirClient ongkir;
    AlatLogistik(ResiClient resi, OngkirClient ongkir) { this.resi = resi; this.ongkir = ongkir; }

    @Tool(description = "Cek status dan riwayat perjalanan paket berdasarkan nomor resi 12 digit")
    StatusResi cekResi(@ToolParam(description = "nomor resi, contoh 004512345678") String nomor) {
        if (!nomor.matches("\\d{12}")) throw new IllegalArgumentException("Format resi harus 12 digit");
        return resi.status(nomor);
    }

    @Tool(description = "Hitung ongkos kirim reguler dan kilat antar kota di Indonesia")
    List<Tarif> hitungOngkir(String kotaAsal, String kotaTujuan, @ToolParam(description = "berat dalam gram") int beratGram) {
        return ongkir.tarif(kotaAsal, kotaTujuan, beratGram);
    }
}

@Configuration
class KonfigurasiAsisten {
    @Bean
    ChatClient asisten(ChatClient.Builder b, VectorStore sop, ChatMemory memori, AlatLogistik alat) {
        return b.defaultSystem("""
                Kamu asisten layanan pelanggan Kirim Cepat. Jawab dalam bahasa Indonesia yang ramah dan singkat.
                Gunakan tool untuk status resi dan ongkir; jangan pernah menebak data paket.
                Untuk aturan klaim, jawab hanya dari dokumen SOP yang diberikan dan sebutkan nomor pasalnya.
                Jika pelanggan marah, meminta manusia, atau kasus di luar SOP, balas dengan token [ESKALASI].
                """)
            .defaultTools(alat)
            .defaultAdvisors(MessageChatMemoryAdvisor.builder(memori).build(),
                             QuestionAnswerAdvisor.builder(sop).searchRequest(SearchRequest.builder().topK(4).build()).build())
            .build();
    }
}

@RestController
@RequiredArgsConstructor
class ChatController {
    private final ChatClient asisten; private final Masker masker; private final Eskalasi eskalasi;

    @PostMapping("/api/v1/chat/{percakapanId}")
    Balasan chat(@PathVariable String percakapanId, @RequestBody @Valid Pesan pesan) {
        String aman = masker.sembunyikanPii(pesan.teks());          // NIK, nomor HP, email
        String jawaban = asisten.prompt().user(aman)
            .advisors(a -> a.param(ChatMemory.CONVERSATION_ID, percakapanId))
            .call().content();
        if (jawaban.contains("[ESKALASI]")) return eskalasi.keAgen(percakapanId);   // ringkasan ikut dikirim
        return new Balasan(jawaban);
    }
}''',
  'java', standar='jawaban berdasar data dan sumber, tool tervalidasi, PII dimasking, eskalasi ke manusia, evaluasi otomatis sebelum rilis, biaya dan latensi terpantau',
  cek=q('Kenapa status paket diambil lewat tool, bukan dibiarkan dijawab model?', ['Model tidak tahu data terbaru dan bisa mengarang; tool mengambil data nyata dari sistem', 'Agar biaya token lebih tinggi', 'Karena model tidak bisa berbahasa Indonesia'], 0, 'Grounding pada sistem sumber.')),
]

PJ_JAVA = JALUR_M('Backend Java', 'Menengah',
  'Enam proyek mini Java 21 yang benar-benar dijalankan (kasir, perpustakaan, mutasi rekening, rate limiter, tiket tanpa overselling, rute kurir) dan empat proyek besar Spring Boot berskala industri (REST API e-commerce, pembayaran QRIS dengan outbox, reservasi klinik berkapasitas tinggi, asisten AI dengan Spring AI), lengkap dengan penyelesaiannya.',
  ['Java projects', 'Spring Boot', 'PostgreSQL', 'Konkurensi', 'Spring AI'], JV_MINI, JV_BESAR)
