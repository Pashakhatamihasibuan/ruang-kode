"""Pendalaman jalur UX Design: istilah dunia kerja dan contoh (perhitungan riset/eksperimen dijalankan dengan Python)."""
K = 'ux'


def P(t, code, b=None):
    return dict(t=t, b=b, code=code.strip('\n'))


def T(t, teks, b=None, lang='text'):
    return dict(t=t, b=b, code=teks.strip('\n'), lang=lang, run=False)


D = {
'Dua sistem berpikir': dict(
  ist=[('System 1 / System 2', 'Berpikir cepat-otomatis vs lambat-penuh usaha (Kahneman). Sebagian besar interaksi aplikasi terjadi di System 1.'),
       ('Cognitive load', 'Beban mental yang dibutuhkan untuk memahami layar; makin tinggi, makin besar peluang salah dan berhenti.'),
       ('Satisficing', 'Pengguna memilih opsi pertama yang "cukup baik", bukan yang terbaik.'),
       ('Friction', 'Hambatan dalam alur. Ada friksi buruk (form panjang) dan friksi baik (konfirmasi sebelum transfer besar).')],
  cx=[T('Desain untuk System 1, rem dengan System 2 saat berisiko', '''
LAYAR                   SYSTEM 1 (cepat)                       SYSTEM 2 (sengaja diperlambat)
---------------------   ------------------------------------   ------------------------------------------
Top up e-wallet         nominal cepat 50rb/100rb/200rb          -
Transfer ke rekening    rekening favorit di atas                konfirmasi nama penerima + nominal besar
baru > Rp5 juta                                                 jeda 5 detik + ketik ulang PIN
Hapus akun              -                                       tulis "HAPUS", jelaskan dampak, opsi unduh data
Checkout                metode bayar terakhir terpilih          ringkasan total sebelum tombol Bayar
''', 'Friksi ditempatkan hanya di titik yang mahal jika salah; sisanya dibuat semulus mungkin.')]),

'Ekonomi perilaku & nudge': dict(
  ist=[('Nudge', 'Mengubah susunan pilihan agar orang cenderung memilih yang baik untuk dirinya, tanpa melarang opsi lain.'),
       ('Choice architecture', 'Cara pilihan disusun: urutan, default, pengelompokan, jumlah.'),
       ('Anchoring', 'Angka pertama yang dilihat memengaruhi penilaian berikutnya (harga coret).'),
       ('Loss aversion', 'Rasa kehilangan terasa sekitar dua kali lebih kuat dari rasa mendapat.'),
       ('Dark pattern', 'Nudge yang menipu atau merugikan pengguna (biaya tersembunyi, sulit berhenti langganan). Dilarang secara etis dan makin diatur hukum.')],
  cx=[T('Nudge etis vs dark pattern pada fitur langganan', '''
NUDGE ETIS                                         DARK PATTERN (hindari)
-----------------------------------------------    -------------------------------------------------
Paket tahunan ditandai "hemat 20%" dengan harga    Harga bulanan disembunyikan, hanya terlihat
per bulan yang jujur                               setelah memasukkan kartu
Pengingat 3 hari sebelum trial berakhir            Trial otomatis jadi berbayar tanpa pemberitahuan
Tombol "Berhenti langganan" sama mudahnya          Berhenti harus lewat telepon CS jam kerja
dengan berlangganan                                (roach motel)
Default: notifikasi promo MATI, bisa dinyalakan    Kotak "kirimi saya promo" sudah dicentang
''')]),

'Hukum UX: Hick, Fitts, Jakob & Miller': dict(
  ist=[('Hick\'s Law', 'Waktu memutuskan naik seiring jumlah dan kerumitan pilihan: T = a + b·log2(n + 1).'),
       ('Fitts\'s Law', 'Waktu mencapai target bergantung jarak dan ukurannya: target penting harus besar dan dekat.'),
       ('Jakob\'s Law', 'Pengguna menghabiskan sebagian besar waktunya di produk lain, jadi mereka berharap pola yang sama.'),
       ('Miller\'s Law', 'Memori kerja terbatas (sering dikutip 7±2); kelompokkan informasi menjadi potongan (chunking).')],
  cx=[P('Menghitung Hick dan Fitts untuk dua rancangan', '''
import math
a, b = 0.2, 0.15                          # konstanta contoh (detik)
for n in (3, 6, 12, 24):
    print(f"Hick: {n:>2} pilihan -> {a + b * math.log2(n + 1):.2f} s")

def fitts(jarak_px, lebar_px, a=0.1, b=0.12):
    return a + b * math.log2(2 * jarak_px / lebar_px)

print(f"Fitts: tombol Bayar 44px, 600px dari jempol  -> {fitts(600, 44):.2f} s")
print(f"Fitts: tombol Bayar 56px full-width di bawah -> {fitts(120, 56):.2f} s")
print("Chunking nomor VA:", " ".join(["8808", "1234", "5678", "9012"]), "lebih mudah dibaca dari 8808123456789012")
''')]),

'Model perilaku Fogg: B = MAP': dict(
  ist=[('Motivation', 'Seberapa ingin seseorang melakukan perilaku (harapan, takut, penerimaan sosial).'),
       ('Ability', 'Seberapa mudah dilakukan: waktu, uang, usaha fisik, usaha mental, rutinitas.'),
       ('Prompt', 'Pemicu pada saat yang tepat: notifikasi, tombol, pengingat.'),
       ('Action line', 'Garis di mana kombinasi motivasi dan kemampuan cukup untuk memicu perilaku saat ada prompt.')],
  cx=[P('Simulasi: menaikkan ability lebih efektif dari menambah motivasi', '''
def terjadi(motivasi, kemampuan, prompt, garis=25):
    return prompt and motivasi * kemampuan >= garis

skenario = [
    ("Onboarding lama: KTP + selfie + 12 field", 6, 3, True),
    ("Kampanye cashback (motivasi naik)", 8, 3, True),
    ("Onboarding baru: nomor HP + OTP dulu", 6, 6, True),
    ("Onboarding baru tanpa notifikasi lanjutan", 6, 6, False),
]
for nama, m, k, p in skenario:
    print(f"{'YA' if terjadi(m, k, p) else 'TIDAK':5} | M={m} A={k} P={'ada' if p else 'tidak'} | {nama}")
''')]),

'Hook model & kebiasaan': dict(
  ist=[('Trigger (eksternal/internal)', 'Pemicu dari luar (notifikasi) atau dari dalam diri (bosan, cemas).'),
       ('Variable reward', 'Hadiah yang tidak terduga (feed baru, poin acak) yang membuat orang kembali.'),
       ('Investment', 'Usaha pengguna (data, koleksi, pengikut) yang membuat produk makin bernilai baginya.'),
       ('Habit-forming ethics', 'Uji etika: apakah produk benar membantu pengguna, dan apakah kamu sendiri mau memakainya?')],
  cx=[T('Hook pada aplikasi tabungan (versi etis)', '''
TRIGGER     Eksternal: notifikasi "Gajian! Sisihkan Rp200.000 ke Celengan Liburan?"
            Internal : cemas soal akhir bulan
ACTION      Satu ketuk: "Sisihkan" (nominal dan tujuan sudah terisi)
REWARD      Progres 64% -> 68%, estimasi tercapai maju 2 minggu (variabel tapi jujur)
INVESTMENT  Pengguna menambah foto tujuan + jadwal autodebet
            -> trigger berikutnya makin relevan, tanpa memancing belanja impulsif
''')]),

'Kurangi beban: default, sedikit pilihan, aksi jelas': dict(
  ist=[('Smart default', 'Nilai awal yang paling mungkin benar untuk mayoritas pengguna.'),
       ('Progressive disclosure', 'Tampilkan yang penting dulu; opsi lanjutan disembunyikan sampai dibutuhkan.'),
       ('Primary action', 'Satu aksi utama per layar yang paling menonjol.'),
       ('Redundant entry (WCAG 3.3.7)', 'Jangan minta pengguna mengetik ulang data yang sudah diberikan.')],
  cx=[P('Menghitung beban form sebelum dan sesudah', '''
sebelum = {"nama": 1, "email": 1, "hp": 1, "tgl_lahir": 1, "jenis_kelamin": 1, "alamat": 1, "kota": 1,
           "kode_pos": 1, "pekerjaan": 1, "penghasilan": 1, "sumber_dana": 1, "ulang_password": 1}
sesudah = {"hp": 1, "otp": 1, "nama": 1}          # sisanya ditanya saat benar-benar dibutuhkan
ketukan_sebelum = len(sebelum) * 2                 # fokus + isi
ketukan_sesudah = len(sesudah) * 2 - 1            # OTP terisi otomatis dari SMS
print(f"field: {len(sebelum)} -> {len(sesudah)}")
print(f"perkiraan ketukan: {ketukan_sebelum} -> {ketukan_sesudah}")
print("ditunda:", ", ".join(k for k in sebelum if k not in sesudah))
''')]),

'Progres, bukti sosial & pengingat': dict(
  ist=[('Goal-gradient effect', 'Orang makin bersemangat saat merasa dekat dengan tujuan; progress bar yang tidak mulai dari nol membantu.'),
       ('Endowed progress', 'Memberi "langkah gratis" di awal (misal 2 dari 10 stempel) menaikkan penyelesaian.'),
       ('Social proof', 'Orang mengikuti perilaku orang lain; harus jujur dan relevan ("3.200 orang di Medan menabung minggu ini").'),
       ('Reminder fatigue', 'Pengingat terlalu sering membuat pengguna mematikan notifikasi atau menghapus aplikasi.')],
  cx=[P('Aturan pengingat yang menghormati pengguna', '''
from datetime import datetime, timedelta
riwayat = [datetime(2026, 11, 17, 19), datetime(2026, 11, 18, 19)]
def boleh_kirim(sekarang, riwayat, maks_per_minggu=3, jam_tenang=(21, 7)):
    if sekarang.hour >= jam_tenang[0] or sekarang.hour < jam_tenang[1]:
        return False, "jam tenang"
    minggu_ini = [r for r in riwayat if sekarang - r < timedelta(days=7)]
    if len(minggu_ini) >= maks_per_minggu:
        return False, "batas mingguan"
    if riwayat and sekarang - riwayat[-1] < timedelta(hours=20):
        return False, "terlalu dekat dengan pengingat terakhir"
    return True, "kirim"
for jam in (datetime(2026, 11, 19, 6), datetime(2026, 11, 19, 12), datetime(2026, 11, 19, 19)):
    print(jam.strftime("%d/%m %H:%M"), boleh_kirim(jam, riwayat))
''')]),

'Outcome, aktor, dan aksi': dict(
  ist=[('Output vs outcome', 'Output: fitur yang dirilis. Outcome: perubahan perilaku/hasil yang terjadi karena fitur itu.'),
       ('Impact mapping', 'Peta Why (tujuan) → Who (aktor) → How (perubahan perilaku) → What (fitur).'),
       ('OKR', 'Objective dan Key Results; KR yang baik adalah outcome yang terukur.'),
       ('Leading vs lagging indicator', 'Indikator awal (aktivasi minggu pertama) vs akhir (retensi 6 bulan).')],
  cx=[T('Impact map: menaikkan nasabah aktif menabung', '''
WHY   Nasabah aktif menabung bulanan naik dari 18% ke 25% dalam 2 kuartal
 |
 +-- WHO  Pekerja muda bergaji UMR
 |    +-- HOW  Menyisihkan saat gajian, bukan di akhir bulan
 |         +-- WHAT  Autodebet di tanggal gajian (default nominal 5%)
 |         +-- WHAT  Notifikasi gajian dengan satu ketuk
 +-- WHO  Pedagang UMKM
      +-- HOW  Menabung dari omzet QRIS harian
           +-- WHAT  "Sisihkan otomatis 2% setiap transaksi QRIS"
''')]),

'Kanvas bisnis, SWOT & kompetitor': dict(
  ist=[('Business Model Canvas', '9 blok: segmen, proposisi nilai, kanal, hubungan, pendapatan, sumber daya, aktivitas, mitra, biaya.'),
       ('Value proposition', 'Alasan pengguna memilih produkmu dibanding alternatif, termasuk "tidak melakukan apa-apa".'),
       ('Competitive benchmark', 'Membandingkan alur kunci dengan 3-5 produk lokal dan global, bukan meniru tampilan.'),
       ('SWOT', 'Kekuatan, kelemahan (internal), peluang, ancaman (eksternal).')],
  cx=[P('Matriks benchmark alur pendaftaran (skor 1-5)', '''
kriteria = ["langkah", "kejelasan biaya", "bantuan", "aksesibilitas", "kecepatan"]
produk = {
    "Kita (sekarang)": [2, 3, 2, 2, 3],
    "Kompetitor A":    [4, 4, 3, 3, 4],
    "Kompetitor B":    [3, 5, 4, 2, 3],
    "Aplikasi global": [5, 4, 3, 4, 5],
}
bobot = [0.3, 0.25, 0.15, 0.15, 0.15]
print(f"{'Produk':16}" + "".join(f"{k[:10]:>11}" for k in kriteria) + "   skor")
for nama, s in sorted(produk.items(), key=lambda x: -sum(a * b for a, b in zip(x[1], bobot))):
    print(f"{nama:16}" + "".join(f"{v:>11}" for v in s) + f"   {sum(a * b for a, b in zip(s, bobot)):.2f}")
selisih = {k: max(t) - v for k, v, t in zip(kriteria, produk["Kita (sekarang)"], zip(*produk.values()))}
print("Dua celah terbesar:", sorted(selisih, key=selisih.get, reverse=True)[:2])
''')]),

'Persona berbasis data': dict(
  ist=[('Proto-persona', 'Persona dari asumsi tim; boleh dipakai di awal asal diberi label dan divalidasi.'),
       ('Behavioral segment', 'Segmen berdasarkan perilaku (frekuensi, tujuan), lebih berguna dari demografi.'),
       ('Jobs To Be Done', '"Ketika [situasi], saya ingin [motivasi], agar [hasil]."'),
       ('Anti-persona', 'Pengguna yang sengaja tidak dilayani agar fokus tetap jelas.')],
  cx=[P('Membentuk segmen perilaku dari data aktivitas', '''
import pandas as pd
d = pd.DataFrame({
    "user": range(1, 13),
    "transaksi_bulan": [2, 30, 25, 1, 3, 40, 28, 2, 4, 35, 1, 26],
    "pakai_fitur_tabungan": [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    "jam_dominan": ["malam", "siang", "siang", "malam", "malam", "pagi", "siang", "malam", "malam", "pagi", "malam", "siang"],
})
d["segmen"] = pd.cut(d.transaksi_bulan, [0, 5, 100], labels=["Penabung santai", "Pedagang aktif"])
print(d.groupby("segmen", observed=True).agg(jumlah=("user", "count"), trx_rata=("transaksi_bulan", "mean"),
      pakai_tabungan=("pakai_fitur_tabungan", "mean"), jam=("jam_dominan", lambda s: s.mode()[0])).round(2))
print("\\nJTBD Pedagang aktif: Ketika toko ramai siang hari, saya ingin menerima pembayaran tanpa uang kembalian, agar antrean cepat.")
''')]),

'User story & peta pengalaman': dict(
  ist=[('User story', '"Sebagai [peran], saya ingin [tujuan], agar [manfaat]" disertai acceptance criteria.'),
       ('Acceptance criteria', 'Syarat terukur bahwa story selesai, sering ditulis Given-When-Then.'),
       ('Customer journey map', 'Tahap, aksi, pikiran, emosi, pain point, dan peluang sepanjang pengalaman.'),
       ('Service blueprint', 'Journey map ditambah lapisan belakang layar: staf, sistem, dan proses pendukung.')],
  cx=[T('User story + acceptance criteria (Given-When-Then)', '''
STORY
  Sebagai pedagang yang baru mendaftar,
  saya ingin melihat status verifikasi KTP saya,
  agar saya tahu kapan bisa menerima pembayaran QRIS.

ACCEPTANCE CRITERIA
  Given KTP sudah diunggah
  When  saya membuka beranda
  Then  saya melihat status "Sedang diperiksa" beserta perkiraan selesai (maks. 1x24 jam)

  Given verifikasi ditolak karena foto buram
  When  saya membuka notifikasi
  Then  saya melihat alasan penolakan dan tombol "Unggah ulang" yang membuka kamera

  Given verifikasi selesai
  Then  saya menerima notifikasi dan QRIS siap diunduh
''')]),

'Wawancara pengguna yang tidak mengarahkan': dict(
  ist=[('Leading question', 'Pertanyaan yang menggiring jawaban ("Fitur ini memudahkan, kan?"). Hindari.'),
       ('Past behavior question', 'Tanyakan kejadian nyata terakhir, bukan prediksi ("Ceritakan terakhir kali...").'),
       ('Discussion guide', 'Panduan topik wawancara, bukan naskah kaku.'),
       ('Affinity mapping', 'Mengelompokkan catatan wawancara menjadi tema dan insight.')],
  cx=[P('Mendeteksi pertanyaan yang mengarahkan di panduan wawancara', '''
import re
pola = [r"\\b(kan|bukan)\\?$", r"^apakah anda (suka|setuju|mau)", r"\\b(mudah|bagus|membantu)\\b.*\\?$", r"^bagaimana jika"]
panduan = [
    "Ceritakan terakhir kali kamu menabung untuk sesuatu.",
    "Fitur celengan ini memudahkan, kan?",
    "Apakah anda suka desain baru kami?",
    "Apa yang kamu lakukan sebelum membuka aplikasi tadi?",
    "Bagaimana jika ada fitur investasi emas?",
    "Apa yang paling menyulitkan saat itu?",
]
for p in panduan:
    masalah = any(re.search(x, p.lower()) for x in pola)
    print(f"{'PERBAIKI' if masalah else 'oke     '} | {p}")
''')]),

'Aturan tata letak yang baik': dict(
  ist=[('Visual hierarchy', 'Urutan baca yang diatur lewat ukuran, bobot, warna, dan posisi.'),
       ('F-pattern / Z-pattern', 'Pola pindai mata: F untuk halaman berteks, Z untuk halaman sederhana.'),
       ('Whitespace', 'Ruang kosong untuk mengelompokkan dan memberi napas, bukan ruang terbuang.'),
       ('Thumb zone', 'Area layar ponsel yang nyaman dijangkau jempol; aksi utama ditaruh di bawah.')],
  cx=[T('Wireframe ASCII: beranda e-wallet, aksi utama di zona jempol', '''
+----------------------------------+
| Halo, Rina            [notif]    |   <- identitas & status
|                                  |
|  Saldo                           |
|  Rp 1.250.000        [mata]      |   <- informasi terpenting, terbesar
|                                  |
|  [Isi]  [Kirim]  [Tarik] [Lain]  |   <- 4 aksi, label + ikon
|----------------------------------|
|  Promo minggu ini  >             |   <- sekunder
|  Riwayat terakhir                |
|   Kopi Kita        -Rp 25.000    |
|   Transfer Dodi    -Rp 100.000   |
|----------------------------------|
|      [  SCAN QRIS  ]             |   <- aksi paling sering, zona jempol
| Beranda  Riwayat  Kartu  Profil  |
+----------------------------------+
''')]),

'Fidelity prototipe & alat desain': dict(
  ist=[('Low / mid / high fidelity', 'Sketsa kasar → wireframe abu-abu → tampilan final interaktif.'),
       ('Clickable prototype', 'Prototipe yang bisa diklik antar layar untuk usability test.'),
       ('Figma, Penpot, Framer', 'Alat desain populer; Penpot open source, Framer kuat untuk situs interaktif.'),
       ('Design-to-code', 'Alur dari desain ke kode lewat Dev Mode, token, dan Code Connect.')],
  cx=[T('Memilih fidelity berdasarkan pertanyaan yang ingin dijawab', '''
PERTANYAAN                                        FIDELITY        ALAT                WAKTU
------------------------------------------------  --------------  ------------------  ---------
Urutan langkah onboarding masuk akal?             low (kertas)    kertas, FigJam      1-2 jam
Pengguna menemukan menu "Tarik tunai"?            mid (wireframe) Figma prototype     1 hari
Label & mikro-copy dipahami?                      mid + teks asli Figma               1 hari
Animasi konfirmasi terasa meyakinkan?             high            Figma/ProtoPie      2-3 hari
Performa di HP 2 GB RAM?                          kode            Flutter/web build   1 minggu
''')]),

'Usability test & 10 heuristik Nielsen': dict(
  ist=[('Task success rate', 'Persentase peserta yang menyelesaikan tugas tanpa bantuan.'),
       ('Think-aloud', 'Peserta menyuarakan pikirannya saat mencoba; moderator tidak membantu.'),
       ('Severity rating (0-4)', 'Tingkat keparahan masalah Nielsen: 0 bukan masalah, 4 bencana usability.'),
       ('SUS (System Usability Scale)', 'Kuesioner 10 butir dengan skor 0-100; rata-rata industri sekitar 68.')],
  cx=[P('Menghitung skor SUS dari jawaban 5 peserta', '''
# Jawaban 1-5 untuk 10 butir SUS (butir ganjil positif, genap negatif)
jawaban = {
    "P1": [4, 2, 4, 1, 5, 2, 4, 2, 4, 2],
    "P2": [3, 3, 3, 2, 4, 3, 3, 3, 3, 3],
    "P3": [5, 1, 5, 1, 5, 1, 5, 1, 4, 2],
    "P4": [2, 4, 3, 4, 3, 4, 2, 4, 3, 3],
    "P5": [4, 2, 4, 2, 4, 2, 4, 1, 4, 2],
}
def sus(j):
    return sum((v - 1) if i % 2 == 0 else (5 - v) for i, v in enumerate(j)) * 2.5
skor = {p: sus(j) for p, j in jawaban.items()}
for p, s in skor.items():
    print(f"{p}: {s:5.1f}")
rata = sum(skor.values()) / len(skor)
print(f"Rata-rata SUS: {rata:.1f} -> {'di atas' if rata > 68 else 'di bawah'} rata-rata industri (68)")
''')]),

'A/B test yang benar': dict(
  ist=[('Hypothesis', '"Jika X, maka metrik Y naik karena Z" ditulis sebelum eksperimen.'),
       ('Sample size & power', 'Jumlah pengguna yang dibutuhkan agar efek kecil bisa terdeteksi (power biasanya 80%).'),
       ('Statistical significance (p-value)', 'Peluang melihat selisih sebesar ini jika sebenarnya tidak ada efek; ambang umum 0,05.'),
       ('Peeking problem', 'Mengintip hasil berkali-kali lalu berhenti saat "signifikan" menaikkan false positive.'),
       ('Guardrail metric', 'Metrik yang tidak boleh memburuk (keluhan, refund, waktu muat).')],
  cx=[P('Ukuran sampel dan uji dua proporsi', '''
from math import sqrt, ceil
from statistics import NormalDist
Z = NormalDist()

def ukuran_sampel(p, mde, alpha=0.05, power=0.8):
    p2 = p + mde
    za, zb = Z.inv_cdf(1 - alpha / 2), Z.inv_cdf(power)
    return ceil(((za * sqrt(2 * p * (1 - p)) + zb * sqrt(p * (1 - p) + p2 * (1 - p2))) ** 2) / mde ** 2)

print("butuh per varian (konversi 12%, ingin deteksi +1,5 poin):", ukuran_sampel(0.12, 0.015))

def uji(konv_a, n_a, konv_b, n_b):
    pa, pb = konv_a / n_a, konv_b / n_b
    p = (konv_a + konv_b) / (n_a + n_b)
    z = (pb - pa) / sqrt(p * (1 - p) * (1 / n_a + 1 / n_b))
    return pa, pb, 2 * (1 - Z.cdf(abs(z)))

pa, pb, pval = uji(1_120, 9_000, 1_265, 9_000)
print(f"A {pa:.2%} vs B {pb:.2%} | selisih {pb - pa:+.2%} | p-value {pval:.4f} -> {'signifikan' if pval < 0.05 else 'belum signifikan'}")
''')]),

'Metrik HEART & North Star': dict(
  ist=[('HEART', 'Happiness, Engagement, Adoption, Retention, Task success (Google). Dipasangkan dengan Goals-Signals-Metrics.'),
       ('North Star Metric', 'Satu metrik yang paling mencerminkan nilai bagi pengguna dan bisnis (misal "nasabah yang menabung tiap bulan").'),
       ('Vanity metric', 'Metrik yang terlihat bagus tetapi tidak menuntun keputusan (total unduhan).'),
       ('Cohort retention', 'Persentase pengguna dari kelompok yang sama yang masih aktif setelah N minggu.')],
  cx=[P('Tabel retensi kohort mingguan', '''
import pandas as pd
kohort = {"M1 Okt": [1000, 520, 410, 360, 330], "M2 Okt": [1200, 660, 540, 480, None],
          "M3 Okt (onboarding baru)": [1100, 715, 605, None, None], "M4 Okt (onboarding baru)": [1050, 693, None, None, None]}
df = pd.DataFrame(kohort, index=["minggu 0", "minggu 1", "minggu 2", "minggu 3", "minggu 4"]).T
ret = df.div(df["minggu 0"], axis=0).mul(100).round(0)
print(ret.map(lambda v: "-" if v != v else f"{v:.0f}%"))
print("\\nRetensi minggu 1 naik dari ~53% ke ~65% setelah onboarding baru.")
''')]),

'Rancang ulang onboarding aplikasi tabungan': dict(
  ist=[('Funnel analysis', 'Melihat persentase pengguna yang lanjut di setiap langkah dan di mana mereka berhenti.'),
       ('Time to value', 'Waktu sampai pengguna merasakan manfaat pertama (misalnya setoran pertama).'),
       ('Activation', 'Momen pengguna baru melakukan aksi bernilai pertama kali.'),
       ('eKYC', 'Verifikasi identitas elektronik (KTP + selfie + liveness) yang diwajibkan regulator untuk layanan keuangan.')],
  cx=[P('Funnel onboarding: lama vs baru', '''
lama = [("Buka aplikasi", 10_000), ("Isi data diri", 6_200), ("Foto KTP", 4_100), ("Selfie", 3_500), ("Buat PIN", 3_200), ("Setoran pertama", 1_400)]
baru = [("Buka aplikasi", 10_000), ("Nomor HP + OTP", 8_300), ("Pilih tujuan menabung", 7_600), ("Buat PIN", 7_200), ("Setoran pertama (tanpa eKYC, maks Rp2 jt)", 4_900), ("eKYC saat saldo > Rp2 jt", 2_800)]
for nama, f in (("LAMA", lama), ("BARU", baru)):
    print(nama)
    for i, (langkah, n) in enumerate(f):
        turun = "" if i == 0 else f"  (-{1 - n / f[i - 1][1]:.0%})"
        print(f"  {langkah:42} {n:>6,} {n / f[0][1]:>5.0%}{turun}".replace(",", "."))
print("Aktivasi (setoran pertama): 14% -> 49%")
''', 'Batas saldo tanpa eKYC penuh harus mengikuti ketentuan regulator; konfirmasikan ke tim kepatuhan.')]),

'Apa itu design system dan kenapa penting untuk UX': dict(
  ist=[('Single source of truth', 'Satu sumber resmi untuk komponen, token, dan pedoman, dipakai desainer dan developer.'),
       ('Consistency', 'Pola yang sama di seluruh produk mengurangi beban belajar pengguna (Jakob\'s Law di dalam produkmu sendiri).'),
       ('Design debt', 'Tumpukan variasi komponen yang tidak konsisten akibat keputusan cepat.'),
       ('Velocity', 'Kecepatan tim merilis fitur; design system mengurangi waktu mendesain dan membangun ulang komponen.')],
  cx=[P('Audit design debt: berapa variasi tombol yang ada?', '''
from collections import Counter
tombol = ["#2563EB/8px/44", "#2563EB/8px/44", "#2563EA/6px/40", "#1D4ED8/8px/44", "#2563EB/12px/48",
          "#2563EB/8px/44", "#3B82F6/4px/36", "#2563EA/6px/40", "#2563EB/8px/44", "#1E40AF/8px/44"]
c = Counter(tombol)
print(f"{len(tombol)} tombol primer di 10 layar -> {len(c)} variasi warna/radius/tinggi")
for v, n in c.most_common():
    print(f"  {n}x {v}")
print("Target: 1 komponen Button primary (token color.action.primary, radius.md, size.touch = 44)")
''')]),

'Material Design 3, Apple HIG, dan design system besar lainnya': dict(
  ist=[('Material 3 (M3) & M3 Expressive', 'Design system Google; M3 Expressive (2025) menekankan bentuk, warna, dan motion berbasis fisika.'),
       ('Apple HIG & Liquid Glass', 'Pedoman Apple; bahasa visual Liquid Glass diperkenalkan 2025 untuk iOS 26 dan platform Apple lainnya.'),
       ('Fluent 2, Carbon, Polaris', 'Design system Microsoft, IBM, dan Shopify.'),
       ('Touch target', 'Minimal 48x48 dp (Android), 44x44 pt (iOS), 24x24 CSS px (WCAG 2.2 AA minimum).')],
  cx=[P('Perbandingan aturan dasar beberapa design system', '''
sistem = [
    ("Material 3", "48 dp", "4 dp", "Roboto / Google Sans", "dynamic color dari wallpaper"),
    ("Apple HIG", "44 pt", "8 pt (umum)", "SF Pro", "Dynamic Type, Liquid Glass"),
    ("Fluent 2", "44 px (sentuh)", "4 px", "Segoe UI Variable", "token alias berlapis"),
    ("Carbon (IBM)", "48 px (lg)", "8 px (2x grid)", "IBM Plex", "fokus enterprise & data"),
]
print(f"{'Sistem':13}| {'Target sentuh':15}| {'Grid':15}| {'Font':21}| Ciri")
for s in sistem:
    print(f"{s[0]:13}| {s[1]:15}| {s[2]:15}| {s[3]:21}| {s[4]}")
''')]),

'Memakai design system lewat CDN dan paket': dict(
  ist=[('npm package', 'Cara utama memasang design system di proyek: npm install @material/web, @fluentui/react-components, dll.'),
       ('Web Components', 'Komponen berbasis standar browser yang bisa dipakai di framework apa pun.'),
       ('Theming', 'Mengganti token (warna, radius, font) agar design system terasa milik brand sendiri.'),
       ('Tree shaking', 'Hanya komponen yang dipakai yang masuk bundle.')],
  cx=[T('Material Web (web components) dengan tema brand', '''
<!-- index.html -->
<script type="importmap">
  { "imports": { "@material/web/": "https://esm.run/@material/web/" } }
</script>
<script type="module">
  import '@material/web/button/filled-button.js';
  import '@material/web/textfield/outlined-text-field.js';
</script>

<style>
  :root {
    --md-sys-color-primary: #0F766E;        /* hijau brand koperasi */
    --md-sys-color-on-primary: #FFFFFF;
    --md-sys-shape-corner-full: 12px;
    --md-ref-typeface-brand: "Plus Jakarta Sans", system-ui, sans-serif;
  }
</style>

<md-outlined-text-field label="Nomor HP" type="tel" supporting-text="Contoh: 0812 3456 7890"></md-outlined-text-field>
<md-filled-button>Lanjut</md-filled-button>
''', lang='html')]),

'Memilih, mengadaptasi, dan mengaudit design system': dict(
  ist=[('Build vs adopt', 'Membangun sendiri (mahal, kontrol penuh) vs memakai yang ada dan diberi tema (cepat).'),
       ('Component coverage', 'Persentase kebutuhan UI produk yang sudah tersedia di design system.'),
       ('Accessibility audit', 'Memeriksa kontras, fokus, label, dan keyboard pada setiap komponen.'),
       ('Detach rate', 'Seberapa sering desainer melepas (detach) komponen di Figma; tanda komponen kurang fleksibel.')],
  cx=[P('Skor kelayakan tiga kandidat design system', '''
kriteria = {"cakupan komponen": 0.3, "aksesibilitas": 0.25, "kemudahan tema": 0.2, "dukungan framework": 0.15, "komunitas": 0.1}
kandidat = {
    "Material Web": {"cakupan komponen": 3, "aksesibilitas": 4, "kemudahan tema": 4, "dukungan framework": 5, "komunitas": 4},
    "shadcn/ui":    {"cakupan komponen": 4, "aksesibilitas": 4, "kemudahan tema": 5, "dukungan framework": 2, "komunitas": 5},
    "Fluent UI":    {"cakupan komponen": 5, "aksesibilitas": 5, "kemudahan tema": 3, "dukungan framework": 3, "komunitas": 4},
}
for nama, s in sorted(kandidat.items(), key=lambda x: -sum(x[1][k] * w for k, w in kriteria.items())):
    total = sum(s[k] * w for k, w in kriteria.items())
    print(f"{nama:13} {total:.2f}  " + ", ".join(f"{k}={v}" for k, v in s.items()))
print("Catatan: 'dukungan framework' bergantung stack tim (shadcn/ui khusus React).")
''')]),

'Studi kasus UX: menonjolkan riset dan keputusan': dict(
  ist=[('Case study', 'Cerita proyek: konteks, masalah, peranmu, proses, keputusan, hasil, refleksi.'),
       ('Design rationale', 'Alasan di balik keputusan desain, didukung bukti riset atau data.'),
       ('Trade-off', 'Apa yang dikorbankan dan kenapa; menunjukkan kedewasaan berpikir.'),
       ('NDA', 'Perjanjian kerahasiaan; samarkan nama klien dan data sensitif di portofolio.')],
  cx=[T('Kerangka studi kasus yang dibaca perekrut dalam 2 menit', '''
1. RINGKASAN (3 baris)  Aplikasi tabungan koperasi · peran: UX designer tunggal · 10 minggu
                         Masalah: 86% pendaftar berhenti sebelum setoran pertama
                         Hasil : aktivasi 14% -> 49% (uji 4 minggu, 20.000 pengguna)
2. KONTEKS & BATASAN   regulasi eKYC, tim 2 developer, HP entry-level
3. RISET               12 wawancara, analisis funnel, benchmark 4 aplikasi
4. INSIGHT KUNCI       "Saya belum tahu mau nabung buat apa" -> tujuan dulu, data diri nanti
5. KEPUTUSAN           3 alternatif onboarding, kenapa memilih versi "tujuan dulu" (trade-off: data KYC tertunda)
6. VALIDASI            2 putaran usability test (5 + 5 peserta), SUS 61 -> 78
7. HASIL & REFLEKSI    angka + apa yang akan dilakukan berbeda
''')]),

'Menulis dampak dan metrik dengan jujur': dict(
  ist=[('Attribution', 'Seberapa besar perubahan metrik benar-benar disebabkan desainmu, bukan faktor lain (promo, musim).'),
       ('Baseline & periode', 'Angka awal dan rentang waktu pengukuran wajib disebut.'),
       ('Relative vs absolute change', '"Naik 50%" bisa berarti 2% → 3% (relatif) atau +50 poin (absolut). Sebutkan keduanya.'),
       ('Qualitative impact', 'Dampak non-angka yang tetap bernilai: keluhan CS berkurang, kutipan pengguna.')],
  cx=[P('Mengubah klaim berlebihan menjadi klaim yang jujur', '''
awal, akhir = 0.021, 0.031
relatif = (akhir - awal) / awal
absolut = (akhir - awal) * 100
print(f"Klaim berlebihan : 'Konversi naik {relatif:.0%}!'")
print(f"Klaim jujur      : 'Konversi checkout naik dari {awal:.1%} ke {akhir:.1%} (+{absolut:.1f} poin, relatif +{relatif:.0%})")
print("                   selama uji A/B 4 minggu (n = 18.000), p < 0,05; promo 11.11 dikecualikan dari periode.'")
''')]),

'Presentasi portofolio saat wawancara': dict(
  ist=[('Portfolio review', 'Sesi 30-60 menit mempresentasikan 1-2 studi kasus kepada panel.'),
       ('STAR', 'Situation, Task, Action, Result: struktur menjawab pertanyaan perilaku.'),
       ('Whiteboard / app critique', 'Tugas mengkritik aplikasi atau merancang solusi singkat secara langsung.'),
       ('Design challenge', 'Tugas rumah 3-7 hari; tanyakan batas waktu yang wajar dan hak atas hasilnya.')],
  cx=[P('Membagi waktu presentasi 30 menit', '''
agenda = [("Perkenalan & peranmu", 2), ("Konteks & masalah", 4), ("Riset & insight", 6), ("Eksplorasi & keputusan", 8),
          ("Hasil & metrik", 4), ("Refleksi", 2), ("Tanya jawab", 4)]
mulai = 0
for nama, menit in agenda:
    print(f"{mulai:02d}:00 - {mulai + menit:02d}:00  {nama}")
    mulai += menit
print("Total:", mulai, "menit. Siapkan versi 10 menit jika panel kekurangan waktu.")
''')]),
}
