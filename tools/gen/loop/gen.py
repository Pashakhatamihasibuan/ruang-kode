"""Membuat src/js/track-loop.js: pelajaran "Semua jenis perulangan" yang ditaruh di AKHIR
modul perulangan tiap jalur (bukan di modul terakhir jalur), sehingga alamat pelajaran lama tidak bergeser.
Kode Java, Python, dan JavaScript dijalankan dulu dan keluarannya dibandingkan (harus sama).
Jalankan: python3 tools/gen/loop/gen.py"""
import json, subprocess
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[2]
baca = lambda f: (here / f).read_text().rstrip('\n')

out = subprocess.run(['python3', str(here / 'main.py')], capture_output=True, text=True, check=True).stdout
for cmd in (['node', str(here / 'main.js')], ['java', str(here / 'Main.java')]):
    o = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=here).stdout
    assert o == out, cmd
out = out.rstrip('\n')

TB = [{'c': 'Perbandingan jenis perulangan', 'h': ['Jenis', 'Kondisi dicek', 'Paling sedikit jalan', 'Cocok untuk'], 'r': [
    ['for', 'sebelum tiap putaran', '0 kali', 'jumlah putaran sudah diketahui (1 sampai 10, 12 bulan)'],
    ['while', 'sebelum tiap putaran', '0 kali', 'berhenti karena keadaan, jumlahnya belum tahu (sampai saldo habis)'],
    ['do-while', 'sesudah tiap putaran', '1 kali', 'badan harus jalan dulu (tampilkan menu, minta input lalu cek)'],
    ['for-each', 'otomatis sampai elemen habis', '0 kali (jika koleksi kosong)', 'membaca setiap isi array atau list tanpa indeks'],
    ['bersarang', 'loop dalam selesai dulu tiap putaran loop luar', 'luar × dalam', 'tabel, baris dan kolom, membandingkan semua pasangan'],
    ['break', 'saat ditemui', 'langsung keluar', 'berhenti begitu yang dicari ketemu'],
    ['continue', 'saat ditemui', 'lompat ke putaran berikutnya', 'melewati data yang tidak perlu diproses']]}]

UMUM = [
    'Perulangan (loop) menyuruh komputer <b>mengulang</b> sekelompok perintah tanpa kita menulis ulang. Semua jenis loop punya tiga bagian yang sama: <b>nilai awal</b>, <b>kondisi</b> kapan terus mengulang, dan <b>perubahan</b> di setiap putaran agar suatu saat berhenti. Bedanya ada pada <i>kapan</i> kondisi dicek dan <i>apa</i> yang diulang.',
    '<b>for</b> dipakai ketika jumlah putaran sudah pasti, misalnya mencetak angka 1 sampai 3. Nilai awal, kondisi, dan perubahan ditulis dalam satu baris sehingga mudah dibaca.',
    '<b>while</b> mengecek kondisi <b>sebelum</b> badan dijalankan. Jika kondisinya sudah salah sejak awal, badan tidak pernah dijalankan sama sekali (0 putaran). Cocok saat kita tidak tahu berapa kali harus mengulang.',
    '<b>do-while</b> menjalankan badan <b>dulu</b>, baru mengecek kondisi di akhir. Akibatnya badan <b>pasti jalan minimal sekali</b>. Lihat contoh: x = 10 dan kondisinya x &lt; 5 sudah salah, tetapi barisnya tetap tercetak satu kali. Inilah perbedaan terpenting antara while dan do-while.',
    '<b>for-each</b> menelusuri setiap isi koleksi (array atau list) satu per satu tanpa mengurus indeks, sehingga tidak mungkin salah indeks. Loop <b>bersarang</b> adalah loop di dalam loop: untuk setiap putaran loop luar, loop dalam berjalan sampai selesai, seperti baris dan kolom tabel perkalian.',
    '<b>break</b> menghentikan loop saat itu juga, sedangkan <b>continue</b> hanya melewati sisa badan pada putaran ini lalu lanjut ke putaran berikutnya. Buka visual 3D di bawah, pilih jenis loop di panel Eksperimen, dan bandingkan sendiri jalannya.']

PTS = ['for: jumlah putaran pasti; while: berhenti karena keadaan.',
       'while mengecek kondisi di awal (bisa 0 kali), do-while di akhir (minimal 1 kali).',
       'for-each membaca setiap isi koleksi tanpa indeks.',
       'break keluar dari loop; continue melompat ke putaran berikutnya.']
Q = [['Kondisi sudah salah sejak awal. Loop mana yang badannya tetap jalan satu kali?', ['do-while', 'while', 'for'], 0, 'do-while mengecek kondisi di akhir, jadi badan jalan dulu.'],
     ['Ingin mencetak semua nama dalam list tanpa memakai indeks. Loop yang paling tepat?', ['for-each', 'do-while', 'while dengan break'], 0, 'for-each menelusuri setiap isi koleksi langsung.'],
     ['Apa beda break dan continue?', ['break keluar dari loop, continue melewati putaran ini saja', 'Keduanya sama-sama keluar dari loop', 'continue keluar dari loop, break melewati putaran'], 0, 'continue tetap melanjutkan putaran berikutnya.'],
     ['Loop luar 2 putaran, loop dalam 3 putaran. Berapa kali badan loop dalam dijalankan?', ['6', '5', '3'], 0, 'Setiap putaran luar menjalankan loop dalam sampai habis: 2 × 3.']]

CATATAN = {
    'python': 'Catatan Python: tidak ada <code>do-while</code>. Polanya ditiru dengan <code>while True:</code> lalu <code>break</code> di akhir badan. <code>for</code> di Python sebenarnya sudah for-each: ia menelusuri isi <code>range()</code>, list, atau string.',
    'js': 'Catatan JavaScript: for-each ditulis <code>for (const x of array)</code>. Jangan tertukar dengan <code>for...in</code> yang menelusuri <b>nama properti/indeks</b>, bukan isinya. Ada juga method <code>array.forEach()</code>, tetapi di dalamnya <code>break</code> tidak bisa dipakai.',
    'java': 'Catatan Java: for-each disebut <b>enhanced for</b>, ditulis <code>for (String b : buah)</code>. Ia bisa dipakai untuk array dan semua koleksi seperti <code>ArrayList</code>.',
    'kotlin': 'Catatan Kotlin: tidak ada for gaya C. Semua <code>for</code> di Kotlin adalah for-each atas range (<code>1..3</code>, <code>0 until n</code>, <code>10 downTo 1 step 2</code>) atau koleksi.',
    'dart': 'Catatan Dart: for-each ditulis <code>for (final b in buah)</code>. List juga punya <code>forEach()</code>, tetapi <code>break</code> dan <code>continue</code> hanya bisa dipakai di loop biasa.',
    'text': 'Catatan pseudocode: beberapa buku menulis do-while sebagai <code>REPEAT ... UNTIL kondisi</code>. Bedanya, REPEAT-UNTIL berhenti ketika kondisi <b>benar</b>, sedangkan DO-WHILE berhenti ketika kondisi <b>salah</b>.'}

JALUR = [('JAVA_MODULES', 'Percabangan & perulangan', 'java', 'Main.java'),
         ('PY_MODULES', 'Percabangan & perulangan', 'python', 'main.py'),
         ('FE0_MODULES', 'JavaScript dasar', 'js', 'main.js'),
         ('DART_MODULES', 'Alur program dan fungsi', 'dart', 'main.dart'),
         ('KOTLIN_MODULES', 'Alur program, fungsi, dan koleksi', 'kotlin', 'main.kt'),
         ('PSEUDO_MODULES', 'Proses perulangan', 'text', 'main.pseudo')]

js = ['/* ===================== SEMUA JENIS PERULANGAN =====================',
      '   Dibuat oleh tools/gen/loop/gen.py. Pelajaran ditambahkan di akhir modul perulangan tiap jalur.',
      '   Keluaran Java, Python, dan JavaScript sudah dijalankan dan identik. */',
      '(()=>{const tambah=(mods,judul,l)=>{const m=mods.find(x=>x.t===judul);if(m&&!m.lessons.some(x=>x.t===l.t))m.lessons.push(l)};']
for const, modul, lang, f in JALUR:
    l = {'k': 'c', 't': 'Semua jenis perulangan: for, while, do-while, for-each, break, continue',
         'nodes': ['Loops'], 'lang': lang, 'b': UMUM + [CATATAN[lang]], 'code': baca(f), 'out': out, 'run': False,
         'tb': TB, 'pts': PTS, 'q': Q, 'v3p': {'jenis': 'banding'}}
    js.append(f'if(typeof {const}!=="undefined")tambah({const},{json.dumps(modul, ensure_ascii=False)},{json.dumps(l, ensure_ascii=False)});')
js.append('})();\n')
(root / 'src/js/track-loop.js').write_text('\n'.join(js))
print('ok', len(JALUR), 'jalur')
