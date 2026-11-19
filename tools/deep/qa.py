"""Pendalaman jalur QA / Software Tester: istilah dunia kerja dan contoh (Python dijalankan; Playwright/k6/CI sebagai kode rujukan)."""
K = 'qa'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def S(t, code, lang, b=None):
    return dict(t=t, b=b, code=code.strip('\n'), lang=lang, run=False)


# Pelari unittest dengan keluaran tetap (tanpa durasi), agar hasil contoh selalu sama
RUNNER = '''import unittest, io
def jalankan_tes(*kelas):
    suite = unittest.TestSuite()
    for k in kelas:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(k))
    ids = [t.id() for t in suite]
    hasil = unittest.TestResult()
    suite.run(hasil)
    gagal = {t.id(): "GAGAL" for t, _ in hasil.failures} | {t.id(): "ERROR" for t, _ in hasil.errors}
    for i in ids:
        print(f"  {gagal.get(i, 'LULUS'):<6} {i.split('.', 1)[1]}")
    for t, tb in hasil.failures:
        print("   ->", tb.strip().splitlines()[-1])
    print(f"{hasil.testsRun} tes, {len(hasil.failures)} gagal, {len(hasil.errors)} error")
'''

D = {
'Apa itu QA dan apa kerjanya': dict(
  ist=[('Quality Assurance (QA)', 'Upaya mencegah cacat lewat proses: review kebutuhan, standar, dan pengujian sejak awal.'),
       ('Quality Control (QC)', 'Pemeriksaan hasil (produk) untuk menemukan cacat; testing adalah bagian dari QC.'),
       ('Defect / bug', 'Perbedaan antara perilaku aktual dan yang diharapkan menurut kebutuhan.'),
       ('Acceptance criteria', 'Syarat terukur agar sebuah user story dianggap selesai; dasar test case.'),
       ('Definition of Done (DoD)', 'Kesepakatan tim kapan pekerjaan selesai, misalnya: kode direview, tes otomatis lulus, QA sign-off.')],
  cx=[P('Biaya bug naik di setiap tahap yang terlewat', '''
# Perkiraan biaya relatif memperbaiki 1 cacat (pola yang sering dikutip industri; angka ilustrasi)
TAHAP = [("kebutuhan", 1), ("desain", 3), ("kode", 10), ("testing", 25), ("produksi", 100)]
BIAYA_JAM = 250_000                   # Rp per jam kerja tim
JAM_DASAR = 0.5                       # memperbaiki di tahap kebutuhan: 30 menit diskusi

cacat = {"kebutuhan": 12, "desain": 8, "kode": 30, "testing": 15, "produksi": 4}   # tempat cacat DITEMUKAN
total = 0
for tahap, faktor in TAHAP:
    biaya = cacat[tahap] * faktor * JAM_DASAR * BIAYA_JAM
    total += biaya
    print(f"{tahap:<10} {cacat[tahap]:>3} cacat x{faktor:>3}  Rp{biaya:>12,.0f}".replace(",", "."))
print(f"total      Rp{total:,.0f}".replace(",", "."))
print("4 bug produksi =", f"{cacat['produksi'] * 100 / (sum(cacat.values())) :.0f}% jumlah cacat,",
      f"tetapi {cacat['produksi'] * 100 * JAM_DASAR * BIAYA_JAM / total:.0%} biaya")
''', 'Inilah alasan QA dilibatkan sejak refinement (shift-left): bertanya "bagaimana kalau..." saat kebutuhan ditulis jauh lebih murah daripada hotfix.')]),

'Jenis pengujian dan piramida testing': dict(
  ist=[('Functional vs non-functional', 'Fungsional menguji apa yang dilakukan sistem; non-fungsional menguji seberapa baik (performa, keamanan, aksesibilitas).'),
       ('Smoke test', 'Tes cepat fungsi paling penting setelah deploy untuk memastikan build layak diuji lebih lanjut.'),
       ('Regression test', 'Tes ulang fitur lama untuk memastikan perubahan baru tidak merusaknya.'),
       ('Test pyramid', 'Banyak unit test, sedang integrasi/API, sedikit E2E UI; makin atas makin lambat dan mahal.'),
       ('Ice cream cone', 'Anti-pola: sebagian besar tes manual/E2E UI dan sedikit unit test, sehingga lambat dan rapuh.')],
  cx=[P('Membandingkan waktu umpan balik dua strategi', '''
# (jumlah tes, detik per tes) per lapisan
PIRAMIDA = {"unit": (1200, 0.01), "integrasi/API": (180, 0.4), "E2E UI": (25, 12)}
CONE     = {"unit": (150, 0.01), "integrasi/API": (40, 0.4), "E2E UI": (220, 12), "manual": (300, 90)}

def ringkas(nama, s, paralel=4):
    total = sum(n * d for n, d in s.values())
    print(f"{nama}")
    for lapis, (n, d) in s.items():
        print(f"  {lapis:<14} {n:>5} tes  {n * d / 60:>7.1f} menit")
    print(f"  waktu CI (paralel {paralel}) ~ {total / paralel / 60:.0f} menit\\n")

ringkas("Piramida", PIRAMIDA)
ringkas("Ice cream cone", CONE)
''', 'Tes manual tetap penting untuk exploratory dan UX, tetapi regresi rutin sebaiknya diotomasi di lapisan serendah mungkin.')]),

'Siklus pengujian (STLC) dan peran QA di Agile': dict(
  ist=[('STLC', 'Software Testing Life Cycle: analisis kebutuhan → perencanaan → desain test case → setup environment → eksekusi → penutupan.'),
       ('Test plan', 'Dokumen ruang lingkup, pendekatan, environment, jadwal, risiko, dan kriteria masuk/keluar pengujian.'),
       ('Entry/exit criteria', 'Syarat mulai dan selesai menguji, misalnya exit: 0 bug kritis terbuka dan 95% test case lulus.'),
       ('Three Amigos', 'Diskusi PO, developer, dan QA sebelum sprint untuk menyamakan pemahaman story dan contoh perilakunya.'),
       ('Shift-left / shift-right', 'Menguji lebih awal (review, unit test) dan juga di produksi (monitoring, feature flag, canary).')],
  cx=[P('Memeriksa exit criteria sebelum rilis', '''
HASIL = {"test case": 248, "lulus": 236, "gagal": 7, "terblokir": 5}
BUG_TERBUKA = [("BUG-311", "kritis"), ("BUG-318", "mayor"), ("BUG-320", "minor"), ("BUG-322", "minor")]
EXIT = {"min_lulus": 0.95, "maks_kritis": 0, "maks_mayor": 2, "maks_terblokir": 3}

tereksekusi = HASIL["lulus"] + HASIL["gagal"]
laju = HASIL["lulus"] / HASIL["test case"]
kritis = sum(s == "kritis" for _, s in BUG_TERBUKA)
mayor = sum(s == "mayor" for _, s in BUG_TERBUKA)
cek = [
    (f"pass rate {laju:.1%} >= {EXIT['min_lulus']:.0%}", laju >= EXIT["min_lulus"]),
    (f"bug kritis terbuka {kritis} <= {EXIT['maks_kritis']}", kritis <= EXIT["maks_kritis"]),
    (f"bug mayor terbuka {mayor} <= {EXIT['maks_mayor']}", mayor <= EXIT["maks_mayor"]),
    (f"test terblokir {HASIL['terblokir']} <= {EXIT['maks_terblokir']}", HASIL["terblokir"] <= EXIT["maks_terblokir"]),
]
for teks, ok in cek:
    print(("LULUS " if ok else "GAGAL ") + teks)
print("Rekomendasi:", "GO" if all(ok for _, ok in cek) else "NO-GO, bahas di go/no-go meeting dengan PO")
''')]),

'Equivalence partitioning dan boundary value': dict(
  ist=[('Equivalence partitioning (EP)', 'Membagi input ke kelas yang diperlakukan sama; cukup satu wakil per kelas.'),
       ('Boundary value analysis (BVA)', 'Menguji di tepi kelas (min-1, min, max, max+1) karena bug sering di batas.'),
       ('Valid / invalid partition', 'Kelas yang harus diterima dan kelas yang harus ditolak sistem.'),
       ('Off-by-one', 'Bug klasik karena < tertukar <= di batas.')],
  cx=[P('Menurunkan test case BVA otomatis dan menemukan bug off-by-one', '''
# Aturan: usia pendaftar asuransi 17-65 tahun, premi 3 tingkat: 17-30, 31-50, 51-65
def premi(usia):                       # implementasi developer (ada bug)
    if usia < 17 or usia > 65: return "ditolak"
    if usia < 30: return "A"           # seharusnya <= 30
    if usia <= 50: return "B"
    return "C"

KELAS = [(17, 30, "A"), (31, 50, "B"), (51, 65, "C")]
kasus = []
for lo, hi, exp in KELAS:
    kasus += [(lo, exp), (hi, exp)]
kasus += [(16, "ditolak"), (66, "ditolak"), (0, "ditolak"), (40, "B")]   # BVA luar + wakil EP
for usia, harap in sorted(set(kasus)):
    hasil = premi(usia)
    print(f"usia {usia:>3}: harap {harap:<8} dapat {hasil:<8} {'OK' if hasil == harap else '<-- BUG'}")
''', 'Hanya 10 kasus, tetapi bug di batas 30 langsung tertangkap. Menguji usia acak 25 atau 45 tidak akan menemukannya.')]),

'Decision table': dict(
  ist=[('Decision table', 'Tabel kombinasi kondisi dan aksi yang diharapkan; cocok untuk aturan bisnis bercabang.'),
       ('Rule', 'Satu kolom kombinasi kondisi; setiap rule menjadi minimal satu test case.'),
       ('Collapsed table', 'Rule yang hasilnya sama digabung dengan nilai "-" (tidak berpengaruh) untuk mengurangi kasus.'),
       ('Business rule', 'Kebijakan bisnis yang ditulis eksplisit, misalnya syarat gratis ongkir.')],
  cx=[P('Membangkitkan semua kombinasi dan mengecek aturan gratis ongkir', '''
from itertools import product

# Aturan: gratis ongkir jika (member DAN belanja >= 100rb) ATAU pakai voucher ongkir; tidak berlaku untuk barang besar
def gratis_ongkir(member, belanja_100rb, voucher, barang_besar):
    if barang_besar: return False
    return (member and belanja_100rb) or voucher

KOND = ["member", "belanja>=100rb", "voucher", "barang besar"]
print(" | ".join(f"{k:<14}" for k in KOND), "| gratis?")
for r, kombinasi in enumerate(product([True, False], repeat=4), 1):
    hasil = gratis_ongkir(*kombinasi)
    print(" | ".join(f"{'Y' if v else 'T':<14}" for v in kombinasi), "|", "YA" if hasil else "-")
print("16 rule penuh; setelah digabung cukup 5: barang besar=Y | voucher=Y | member+belanja | member saja | bukan member")
''')]),

'State transition testing': dict(
  ist=[('State transition', 'Teknik menguji perpindahan status objek (pesanan, akun) beserta event pemicunya.'),
       ('Valid / invalid transition', 'Perpindahan yang diizinkan vs yang harus ditolak (misalnya pesanan "selesai" tidak boleh kembali "dibayar").'),
       ('0-switch / 1-switch coverage', 'Menguji setiap transisi tunggal / setiap pasangan transisi berurutan.'),
       ('State diagram', 'Gambar status dan panah transisi; sumber test case yang mudah direview bersama developer.')],
  cx=[P('Menguji semua transisi pesanan, termasuk yang tidak valid', '''
TRANSISI = {
    ("dibuat", "bayar"): "dibayar", ("dibuat", "batal"): "dibatalkan",
    ("dibayar", "kirim"): "dikirim", ("dibayar", "batal"): "refund",
    ("dikirim", "terima"): "selesai", ("dikirim", "retur"): "retur",
}
STATUS = ["dibuat", "dibayar", "dikirim", "selesai", "dibatalkan", "refund", "retur"]
EVENT = ["bayar", "batal", "kirim", "terima", "retur"]

def proses(status, event):            # sistem yang diuji
    if (status, event) not in TRANSISI:
        raise ValueError(f"transisi {status} --{event}--> tidak diizinkan")
    return TRANSISI[(status, event)]

valid = invalid = 0
for s in STATUS:
    for e in EVENT:
        try:
            proses(s, e); valid += 1
        except ValueError:
            invalid += 1
print(f"{valid} transisi valid diuji, {invalid} transisi invalid harus ditolak")
# Skenario 1-switch: urutan nyata yang sering bermasalah
for jalur in (["bayar", "kirim", "terima"], ["bayar", "batal"], ["bayar", "kirim", "batal"]):
    s = "dibuat"
    try:
        for e in jalur: s = proses(s, e)
        print(" -> ".join(jalur), "=", s)
    except ValueError as err:
        print(" -> ".join(jalur), "= DITOLAK:", err)
''')]),

'Menulis test case yang baik': dict(
  ist=[('Test case', 'Langkah, data uji, dan hasil yang diharapkan untuk memverifikasi satu perilaku.'),
       ('Precondition', 'Kondisi yang harus ada sebelum tes dijalankan, misalnya "pengguna sudah login, saldo Rp100.000".'),
       ('Traceability matrix', 'Pemetaan kebutuhan ke test case untuk memastikan tidak ada kebutuhan yang tidak diuji.'),
       ('Gherkin (Given-When-Then)', 'Format skenario BDD yang bisa dibaca bisnis dan diotomasi (Cucumber, pytest-bdd).'),
       ('Test management tool', 'Alat seperti TestRail, Qase, Zephyr, Xray untuk mengelola suite dan hasil eksekusi.')],
  cx=[P('Traceability: kebutuhan mana yang belum punya test case?', '''
KEBUTUHAN = {"REQ-01": "login dengan email", "REQ-02": "login dengan OTP", "REQ-03": "lupa password",
             "REQ-04": "kunci akun 5x gagal", "REQ-05": "logout semua perangkat"}
TEST_CASE = {
    "TC-101": ("REQ-01", "Login email valid"), "TC-102": ("REQ-01", "Login password salah"),
    "TC-103": ("REQ-02", "OTP benar"), "TC-104": ("REQ-02", "OTP kedaluwarsa 5 menit"),
    "TC-105": ("REQ-04", "Gagal ke-5 mengunci akun 15 menit"),
}
peta = {r: [tc for tc, (req, _) in TEST_CASE.items() if req == r] for r in KEBUTUHAN}
for r, tcs in peta.items():
    print(f"{r} {KEBUTUHAN[r]:<26} {', '.join(tcs) if tcs else 'BELUM ADA TEST CASE'}")
cakupan = sum(bool(v) for v in peta.values()) / len(peta)
print(f"cakupan kebutuhan {cakupan:.0%}")
'''),
     S('Test case yang sama dalam format Gherkin', '''
Fitur: Penguncian akun
  Skenario: Akun terkunci setelah 5 kali password salah
    Diberikan pengguna "rina@contoh.id" terdaftar dan belum terkunci
    Ketika ia memasukkan password salah 5 kali berturut-turut
    Maka ia melihat pesan "Akun dikunci 15 menit demi keamanan"
    Dan email pemberitahuan terkirim ke "rina@contoh.id"
    Dan percobaan login ke-6 dengan password benar tetap ditolak''', 'gherkin')]),

'Laporan bug, severity, dan priority': dict(
  ist=[('Severity', 'Seberapa parah dampak teknis bug (kritis, mayor, minor, trivial); ditentukan QA.'),
       ('Priority', 'Seberapa cepat harus diperbaiki menurut bisnis (P1-P4); biasanya diputuskan PO.'),
       ('Steps to reproduce', 'Langkah persis yang membuat bug muncul lagi; bug yang tidak bisa direproduksi sulit diperbaiki.'),
       ('Bug life cycle', 'New → Assigned → In progress → Fixed → Retest → Closed / Reopened.'),
       ('Defect leakage', 'Persentase bug yang lolos ke produksi dibanding total bug yang ditemukan.')],
  cx=[P('Metrik bug untuk retrospektif rilis', '''
BUG = [  # (id, severity, ditemukan di, hari sampai ditutup)
    ("B1", "kritis", "testing", 1), ("B2", "mayor", "testing", 3), ("B3", "minor", "testing", 6),
    ("B4", "mayor", "produksi", 2), ("B5", "kritis", "produksi", 1), ("B6", "minor", "review", 1),
    ("B7", "mayor", "testing", 4), ("B8", "minor", "testing", 9), ("B9", "trivial", "testing", 12),
]
prod = [b for b in BUG if b[2] == "produksi"]
print(f"defect leakage: {len(prod)}/{len(BUG)} = {len(prod)/len(BUG):.0%}")
for sev in ("kritis", "mayor", "minor", "trivial"):
    hari = [b[3] for b in BUG if b[1] == sev]
    print(f"{sev:<8} {len(hari)} bug, rata-rata ditutup {sum(hari)/len(hari):.1f} hari")
print("Contoh severity rendah + priority tinggi: logo salah di halaman utama saat kampanye nasional.")
'''),
     S('Template laporan bug yang baik', '''
Judul   : [Checkout] Total tidak berubah setelah voucher dihapus (Android 14, app 5.12.0)
Severity: Mayor        Priority: P2        Environment: staging, build 5.12.0-rc3
Langkah :
  1. Login sebagai pembeli@contoh.id, tambah "Kopi Gayo 250g" (Rp85.000) ke keranjang
  2. Pakai voucher HEMAT20 -> total Rp68.000
  3. Hapus voucher
Hasil aktual   : total tetap Rp68.000
Hasil harapan  : total kembali Rp85.000
Frekuensi      : 5/5 percobaan
Lampiran       : video_layar.mp4, log_network.har
Catatan        : terjadi juga di iOS 18; web tidak terpengaruh''', 'text')]),

'Exploratory testing': dict(
  ist=[('Exploratory testing', 'Belajar, merancang, dan mengeksekusi tes sekaligus, dipandu rasa ingin tahu dan pengalaman.'),
       ('Test charter', 'Misi sesi: "Jelajahi <area> dengan <sumber daya> untuk menemukan <informasi>".'),
       ('Session-based test management', 'Eksplorasi dalam sesi berwaktu (60-90 menit) dengan catatan dan debrief.'),
       ('Heuristik / tour', 'Pemandu ide tes, misalnya SFDIPOT, "tur uang", atau "tur data ekstrem".')],
  cx=[P('Membangkitkan data uji "nakal" untuk sesi eksplorasi form nama', '''
NAKAL = {
    "kosong": "", "spasi saja": "   ", "sangat panjang": "A" * 256,
    "nama satu kata": "Sukarno", "apostrof": "Ma'ruf", "tanda hubung": "Siti-Aisyah",
    "unicode": "Zoë Müller", "emoji": "Budi 🚀", "aksara Jawa": "ꦧꦸꦢꦶ",
    "HTML": "<b>Budi</b>", "SQL": "x'; DROP TABLE users;--", "angka": "12345",
}
def validasi_nama(n):                    # validasi aplikasi yang sedang diuji
    n = n.strip()
    return 2 <= len(n) <= 100 and not any(c in n for c in "<>;")

for label, nilai in NAKAL.items():
    tampil = nilai if len(nilai) <= 20 else nilai[:17] + "..."
    print(f"{label:<15} {tampil!r:<26} {'diterima' if validasi_nama(nilai) else 'DITOLAK'}")
print("Pertanyaan debrief: apakah Ma'ruf dan nama satu kata seharusnya diterima? (ya, nama Indonesia)")
''')]),

'Unit test dengan pola Arrange-Act-Assert': dict(
  ist=[('Arrange-Act-Assert (AAA)', 'Susun data, jalankan aksi, periksa hasil; satu perilaku per tes.'),
       ('Test fixture', 'Data atau objek siap pakai yang disiapkan sebelum tes (setUp, fixture pytest).'),
       ('Parametrized test', 'Satu fungsi tes dijalankan dengan banyak data (subTest, @pytest.mark.parametrize).'),
       ('Code coverage', 'Persentase baris/cabang yang dieksekusi tes; alat bantu, bukan target mutlak.'),
       ('Mutation testing', 'Mengubah kode sedikit (mutan) untuk melihat apakah tes gagal; mengukur kekuatan tes.')],
  cx=[P('Unit test kalkulator diskon dengan unittest', RUNNER + '''
def harga_akhir(harga, diskon_persen, member=False):
    if not 0 <= diskon_persen <= 90: raise ValueError("diskon 0-90%")
    h = harga * (100 - diskon_persen) / 100
    if member: h -= 5_000
    return max(round(h), 0)

class TesHargaAkhir(unittest.TestCase):
    def test_diskon_biasa(self):
        # Arrange
        harga, diskon = 200_000, 25
        # Act
        hasil = harga_akhir(harga, diskon)
        # Assert
        self.assertEqual(hasil, 150_000)
    def test_member_dapat_potongan_tambahan(self):
        self.assertEqual(harga_akhir(100_000, 10, member=True), 85_000)
    def test_tidak_pernah_negatif(self):
        self.assertEqual(harga_akhir(4_000, 0, member=True), 0)
    def test_batas_diskon(self):
        for d, ok in [(0, True), (90, True), (91, False), (-1, False)]:
            with self.subTest(diskon=d):
                if ok: harga_akhir(10_000, d)
                else: self.assertRaises(ValueError, harga_akhir, 10_000, d)

jalankan_tes(TesHargaAkhir)
'''),
     S('Versi pytest yang dipakai di banyak tim', '''
import pytest
from toko.harga import harga_akhir

@pytest.mark.parametrize("harga, diskon, member, harap", [
    (200_000, 25, False, 150_000),
    (100_000, 10, True, 85_000),
    (4_000, 0, True, 0),
])
def test_harga_akhir(harga, diskon, member, harap):
    assert harga_akhir(harga, diskon, member) == harap

@pytest.mark.parametrize("diskon", [-1, 91])
def test_diskon_di_luar_batas_ditolak(diskon):
    with pytest.raises(ValueError, match="0-90%"):
        harga_akhir(10_000, diskon)

# jalankan: pytest -q --cov=toko --cov-branch''', 'python')]),

'Mock dan stub': dict(
  ist=[('Test double', 'Pengganti dependensi asli saat tes: dummy, stub, fake, spy, mock.'),
       ('Stub', 'Mengembalikan jawaban yang sudah ditentukan (misalnya kurs selalu 16.000).'),
       ('Mock', 'Double yang juga memverifikasi interaksi: dipanggil berapa kali dan dengan argumen apa.'),
       ('Fake', 'Implementasi ringan yang benar-benar bekerja, misalnya database di memori.'),
       ('Dependency injection', 'Dependensi diberikan dari luar sehingga mudah diganti double saat tes.')],
  cx=[P('Mock gateway pembayaran dan notifikasi dengan unittest.mock', RUNNER + '''
from unittest.mock import Mock

class LayananPesanan:
    def __init__(self, gateway, notif):
        self.gateway, self.notif = gateway, notif
    def bayar(self, pesanan_id, nominal):
        r = self.gateway.tagih(pesanan_id, nominal)
        if r["status"] == "sukses":
            self.notif.kirim(pesanan_id, "Pembayaran diterima")
            return "dibayar"
        return "gagal"

class TesPembayaran(unittest.TestCase):
    def test_sukses_mengirim_notifikasi(self):
        gw = Mock(); gw.tagih.return_value = {"status": "sukses"}       # stub
        notif = Mock()                                                    # mock
        self.assertEqual(LayananPesanan(gw, notif).bayar("INV-9", 85_000), "dibayar")
        gw.tagih.assert_called_once_with("INV-9", 85_000)
        notif.kirim.assert_called_once_with("INV-9", "Pembayaran diterima")
    def test_gagal_tidak_mengirim_notifikasi(self):
        gw = Mock(); gw.tagih.return_value = {"status": "ditolak"}
        notif = Mock()
        self.assertEqual(LayananPesanan(gw, notif).bayar("INV-10", 85_000), "gagal")
        notif.kirim.assert_not_called()
    def test_timeout_gateway(self):
        gw = Mock(); gw.tagih.side_effect = TimeoutError("gateway 30 detik")
        with self.assertRaises(TimeoutError):
            LayananPesanan(gw, Mock()).bayar("INV-11", 1)

jalankan_tes(TesPembayaran)
''')]),

'Pengujian API REST': dict(
  ist=[('Status code', 'Kode hasil HTTP: 2xx sukses, 4xx kesalahan klien (400, 401, 403, 404, 409, 422), 5xx kesalahan server.'),
       ('Contract testing', 'Memastikan respons sesuai kontrak (OpenAPI/JSON Schema) yang disepakati konsumen dan penyedia (Pact).'),
       ('Idempotency', 'Permintaan yang diulang memberi efek sama; penting untuk POST pembayaran dengan Idempotency-Key.'),
       ('Negative testing', 'Menguji input salah, token kedaluwarsa, hak akses kurang; bukan hanya happy path.'),
       ('Postman / Newman, REST Assured', 'Alat populer pengujian API manual dan otomatis di CI.')],
  cx=[P('Menguji API dengan server lokal sungguhan (http.server + urllib)', '''
import json, threading, urllib.request, urllib.error
from http.server import BaseHTTPRequestHandler, HTTPServer

PRODUK = {1: {"id": 1, "nama": "Kopi Gayo 250g", "harga": 85000}}
class Api(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def balas(self, kode, isi):
        self.send_response(kode); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps(isi).encode())
    def do_GET(self):
        if self.headers.get("Authorization") != "Bearer token-uji": return self.balas(401, {"error": "unauthorized"})
        pid = self.path.rsplit("/", 1)[-1]
        if not pid.isdigit(): return self.balas(400, {"error": "id harus angka"})
        p = PRODUK.get(int(pid))
        self.balas(200, p) if p else self.balas(404, {"error": "tidak ditemukan"})

srv = HTTPServer(("127.0.0.1", 0), Api); threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/produk/"

def panggil(path, token="token-uji"):
    req = urllib.request.Request(BASE + path, headers={"Authorization": f"Bearer {token}"} if token else {})
    try:
        with urllib.request.urlopen(req) as r: return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read())

KASUS = [("1", "token-uji", 200), ("99", "token-uji", 404), ("abc", "token-uji", 400), ("1", None, 401)]
for path, tok, harap in KASUS:
    kode, isi = panggil(path, tok)
    print(f"GET /produk/{path:<4} token={'ya' if tok else 'tidak':<5} -> {kode} {'OK' if kode == harap else 'SALAH'}  {isi}")
kode, isi = panggil("1")
skema = {"id": int, "nama": str, "harga": int}
print("cek skema:", all(isinstance(isi[k], t) for k, t in skema.items()) and set(isi) == set(skema))
srv.shutdown()
''')]),

'Tes E2E dengan Playwright': dict(
  ist=[('End-to-end (E2E) test', 'Menguji alur pengguna lengkap lewat UI sungguhan, dari login sampai transaksi.'),
       ('Locator berbasis peran', 'getByRole, getByLabel, getByText: tahan perubahan CSS dan sekaligus menguji aksesibilitas.'),
       ('Auto-waiting', 'Playwright menunggu elemen siap sebelum aksi; hindari sleep tetap.'),
       ('Page Object Model (POM)', 'Membungkus halaman menjadi kelas berisi locator dan aksi agar tes rapi dan mudah dirawat.'),
       ('Trace viewer', 'Rekaman langkah, DOM, network, dan konsol untuk menyelidiki tes yang gagal di CI.')],
  cx=[S('Tes checkout dengan Page Object Model (TypeScript)', '''
// pages/CheckoutPage.ts
import { Page, expect } from '@playwright/test';
export class CheckoutPage {
  constructor(private page: Page) {}
  voucher = () => this.page.getByLabel('Kode voucher');
  total   = () => this.page.getByTestId('total-bayar');
  async pakaiVoucher(kode: string) {
    await this.voucher().fill(kode);
    await this.page.getByRole('button', { name: 'Pakai' }).click();
  }
}

// tests/checkout.spec.ts
import { test, expect } from '@playwright/test';
import { CheckoutPage } from '../pages/CheckoutPage';

test.use({ storageState: 'auth/pembeli.json' });          // login sekali di global setup

test('voucher HEMAT20 memotong total 20%', async ({ page }) => {
  await page.goto('/checkout?item=kopi-gayo-250g');
  const co = new CheckoutPage(page);
  await expect(co.total()).toHaveText('Rp85.000');
  await co.pakaiVoucher('HEMAT20');
  await expect(co.total()).toHaveText('Rp68.000');        // auto-retry sampai teks cocok
});

test('voucher kedaluwarsa menampilkan pesan yang jelas', async ({ page }) => {
  await page.route('**/api/voucher', r => r.fulfill({ status: 422, json: { error: 'Voucher sudah berakhir 31 Okt' } }));
  await page.goto('/checkout?item=kopi-gayo-250g');
  await new CheckoutPage(page).pakaiVoucher('LAMA10');
  await expect(page.getByRole('status')).toHaveText('Voucher sudah berakhir 31 Okt');
});
// npx playwright test --project=chromium --project="Mobile Safari" --trace on-first-retry''', 'ts')]),

'Tes flaky dan strategi data uji': dict(
  ist=[('Flaky test', 'Tes yang kadang lulus kadang gagal tanpa perubahan kode; merusak kepercayaan pada CI.'),
       ('Quarantine', 'Memindahkan tes flaky ke jalur terpisah sementara sambil diperbaiki, dengan pemilik dan tenggat.'),
       ('Test data management', 'Cara menyiapkan data uji: factory/builder, seed per tes, data sintetis, masking data produksi.'),
       ('Test isolation', 'Setiap tes membuat dan membersihkan datanya sendiri sehingga urutan tes tidak berpengaruh.'),
       ('Deterministic', 'Hasil sama setiap kali: waktu, acak, dan jaringan dikendalikan (clock palsu, seed, mock).')],
  cx=[P('Mendeteksi tes flaky dari riwayat CI', '''
RIWAYAT = {  # hasil 20 run terakhir di commit yang sama (L=lulus, G=gagal)
    "checkout.voucher":       "LLLLLLLLLLLLLLLLLLLL",
    "login.otp_kedaluwarsa":  "LLGLLLLGLLLLLGLLLLLL",
    "keranjang.update_qty":   "GGGGGGGGGGGGGGGGGGGG",
    "laporan.export_pdf":     "LLLLLLLLLGLLLLLLLLLL",
}
for nama, r in RIWAYAT.items():
    gagal = r.count("G") / len(r)
    if gagal == 0: status = "stabil"
    elif gagal == 1: status = "RUSAK (bug nyata, bukan flaky)"
    else:
        perpindahan = sum(a != b for a, b in zip(r, r[1:]))
        status = f"FLAKY {gagal:.0%} gagal, {perpindahan} kali berganti -> karantina + tiket"
    print(f"{nama:<24} {status}")
print("Penyebab umum: menunggu dengan sleep, data bersama antar-tes, jam/zona waktu, urutan tes, jaringan eksternal")
'''),
     P('Builder data uji: setiap tes membuat data unik sendiri', '''
import itertools, random
from dataclasses import dataclass, field, replace

_seq = itertools.count(1)
random.seed(42)                                # deterministik: hasil sama di setiap run

@dataclass
class Pengguna:
    email: str = field(default_factory=lambda: f"uji{next(_seq)}@contoh.id")
    nama: str = "Pengguna Uji"
    saldo: int = 0
    terverifikasi: bool = True

def pengguna(**ubah):                          # builder: default masuk akal, ubah seperlunya
    return replace(Pengguna(), **ubah)

a = pengguna()
b = pengguna(saldo=100_000)
c = pengguna(terverifikasi=False, nama="Belum KYC")
for p in (a, b, c): print(p)
print("email unik:", len({a.email, b.email, c.email}) == 3)
''')]),

'Uji performa dengan k6 dan tes di CI': dict(
  ist=[('Load / stress / spike / soak test', 'Beban normal / di atas kapasitas / lonjakan mendadak / beban lama untuk mencari kebocoran memori.'),
       ('Persentil p95/p99', 'Waktu respons yang dialami 95%/99% permintaan; lebih jujur daripada rata-rata.'),
       ('Threshold', 'Batas lulus otomatis, misalnya http_req_duration p(95) < 500 ms dan error < 1%.'),
       ('Throughput (RPS)', 'Jumlah permintaan per detik yang sanggup dilayani.'),
       ('Quality gate', 'Syarat di pipeline CI yang harus lulus sebelum merge/deploy: tes, coverage, scan keamanan, performa.')],
  cx=[P('Menghitung persentil dan memeriksa threshold dari hasil uji beban', '''
import random, statistics
random.seed(7)
# 2.000 waktu respons (ms) simulasi: kebanyakan cepat, sebagian kecil lambat (ekor panjang)
waktu = [random.gauss(180, 40) for _ in range(1900)] + [random.uniform(600, 2500) for _ in range(100)]
error = 14

def persentil(data, p):
    s = sorted(data); i = (len(s) - 1) * p / 100
    lo = int(i); return s[lo] + (s[min(lo + 1, len(s) - 1)] - s[lo]) * (i - lo)

print(f"rata-rata {statistics.mean(waktu):.0f} ms   median {persentil(waktu, 50):.0f} ms")
print(f"p95 {persentil(waktu, 95):.0f} ms   p99 {persentil(waktu, 99):.0f} ms   maks {max(waktu):.0f} ms")
THRESH = {"p95 < 500 ms": persentil(waktu, 95) < 500, "p99 < 1500 ms": persentil(waktu, 99) < 1500,
          "error < 1%": error / len(waktu) < 0.01}
for k, ok in THRESH.items(): print(("LULUS " if ok else "GAGAL ") + k)
print("Rata-rata terlihat sehat, tetapi 1 dari 20 permintaan menunggu jauh lebih lama.")
'''),
     S('Skrip k6 dan quality gate di GitHub Actions', '''
// perf/checkout.js — k6 run perf/checkout.js
import http from 'k6/http';
import { check, sleep } from 'k6';
export const options = {
  stages: [{ duration: '2m', target: 200 }, { duration: '5m', target: 200 }, { duration: '1m', target: 0 }],
  thresholds: { http_req_duration: ['p(95)<500', 'p(99)<1500'], http_req_failed: ['rate<0.01'] },
};
export default function () {
  const r = http.get(`${__ENV.BASE_URL}/api/produk?kategori=kopi`);
  check(r, { 'status 200': x => x.status === 200 });
  sleep(1);
}

# .github/workflows/qa.yml
jobs:
  tes:
    steps:
      - run: pytest -q --cov --cov-fail-under=80          # unit + integrasi
      - run: npx playwright test --shard=${{ matrix.shard }}/4
      - run: k6 run perf/checkout.js                      # gagal otomatis jika threshold dilanggar
      - uses: actions/upload-artifact@v4
        if: failure()
        with: { name: playwright-trace, path: test-results/ }''', 'yaml')]),
}
