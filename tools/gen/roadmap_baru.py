"""Jalur baru dari roadmap.sh: Struktur Data & Algoritma, PostgreSQL DBA, QA, Django, Next.js, Vue, Data Science & AI."""
from rb_dsa import DSA, DSA_SO
from rb_pg import PG, PG_SO
from rb_qa import QA, QA_SO
from rb_django import DJ, DJ_SO
from rb_next import NX, NX_SO
from rb_vue import VUE, VUE_SO
from rb_dsci import DSCI, DSCI_SO
from rb_proj import PROJ, PROJ_SO
from rb_js import JS1
from rb_js2 import JS2
from rb_js3 import JS3
from rb_js4 import JS4
from rb_js5 import JS5
from rb_js6 import JS6

JS = JS1 + JS2 + JS3 + JS4 + JS5 + JS6
JS_SO = {}

# analogi "Sekilas" (an) dan visual 3D otomatis (v3) per pelajaran, agar tidak salah tebak dari judul
_JS_OVR = {
  'Hoisting dan Temporal Dead Zone': {'an': 'Hoisting itu seperti daftar hadir yang dibacakan sebelum kelas mulai: semua nama sudah tercatat, tetapi let dan const belum boleh menjawab sampai gilirannya tiba.'},
  'Block, function, dan global scope': {'v3': None, 'an': 'Scope itu seperti ruangan di rumah: barang di kamar hanya terlihat dari dalam kamar, sedangkan barang di ruang tamu terlihat dari mana saja.'},
  'Tipe primitif: string, number, boolean': {'an': 'Tipe data itu seperti jenis wadah: teks, angka, dan benar/salah disimpan dan diolah dengan cara yang berbeda.'},
  'Object dan operator typeof': {'an': 'Object itu seperti lemari berlaci berlabel: setiap laci (key) menyimpan satu barang (value), dan typeof seperti membaca label jenis barangnya.'},
  'Built-in objects': {'v3': None, 'an': 'Built-in objects itu seperti perkakas bawaan di dapur baru: Math, Date, JSON, dan Intl sudah tersedia tanpa perlu membeli.'},
  'Array: map, filter, reduce, dan kawan-kawan': {'an': 'map, filter, dan reduce itu seperti jalur produksi: setiap item lewat mesin pengubah, lalu penyaring, lalu dikumpulkan menjadi satu hasil.'},
  'Map dan Set': {'v3': 'hash'},
  'WeakMap dan WeakSet': {'an': 'WeakMap itu seperti catatan tempel pada barang pinjaman: saat barangnya dibuang, catatannya ikut hilang.'},
  'JSON': {'an': 'JSON itu seperti formulir standar pengiriman paket: semua pihak sepakat formatnya sehingga data bisa dikirim dan dibaca di mana saja.'},
  '== versus ===': {'an': '=== itu seperti petugas yang mencocokkan nama dan foto KTP sekaligus, sedangkan == menerjemahkan dulu sebelum mencocokkan, sehingga kadang tertipu.'},
  'Object.is, SameValue, dan SameValueZero': {'v3': None, 'an': 'Object.is itu seperti pemeriksa sidik jari: dua nilai dianggap sama hanya jika benar-benar identik, termasuk kasus khusus NaN dan -0.'},
  'break, continue, dan label': {'v3': 'loop'},
  'Error objects dan custom error': {'v3': None, 'an': 'Error object itu seperti laporan kejadian: ada jenisnya, pesannya, dan jejak lokasi kejadiannya (stack trace).'},
  'Operator logika, kondisional, dan string': {'an': 'Operator logika itu seperti satpam bertingkat: && meloloskan jika semua syarat terpenuhi, || cukup salah satu, dan ?? hanya memberi cadangan jika nilainya kosong.'},
  'Destructuring, spread, rest, dan presedensi': {'an': 'Destructuring itu seperti membongkar kardus kiriman lalu langsung menaruh setiap barang di raknya; spread kebalikannya, menuang isi satu wadah ke wadah lain.'},
  'Lexical scoping dan closure': {'an': 'Closure itu seperti tas bekal: fungsi membawa variabel dari tempat ia dibuat, dan bekal itu tetap ada walaupun rumahnya sudah ditinggalkan.'},
  'Strict mode': {'an': 'Strict mode itu seperti wasit yang ketat: pelanggaran kecil yang biasanya dibiarkan langsung diberi kartu.'},
  'Nilai this di berbagai konteks': {'an': 'this itu seperti kata "saya": artinya bergantung pada siapa yang sedang berbicara, yaitu bagaimana fungsi dipanggil.'},
  'Event loop: cara JS menangani hal asinkron': {'v3': None, 'viz': 'jsloop', 'an': 'Event loop itu seperti satu kasir yang melayani antrean: pekerjaan lama dititipkan ke dapur, dan pesanan yang sudah jadi dipanggil saat kasir senggang.'},
  'setTimeout dan setInterval': {'an': 'setTimeout itu seperti alarm: kamu memasangnya sekarang, lalu pekerjaan dijalankan saat alarm berbunyi dan kasir (event loop) sedang senggang.'},
  'XMLHttpRequest dan perbandingannya dengan fetch': {'an': 'XMLHttpRequest itu seperti telepon rumah generasi lama: masih bisa menelepon server, tetapi fetch adalah ponsel modern yang lebih praktis.'},
  'Protokol iterable dan iterator': {'an': 'Iterator itu seperti petugas yang membagikan nomor antrean satu per satu: setiap dipanggil ia memberi nomor berikutnya sampai habis.'},
  'Generator function dan yield': {'v3': None, 'an': 'Generator itu seperti cerita bersambung: berhenti di setiap bab (yield) dan baru melanjutkan saat kamu meminta bab berikutnya.'},
  'Siklus hidup memori dan garbage collection': {'v3': None, 'an': 'Garbage collector itu seperti petugas kebersihan: barang yang tidak lagi dipegang siapa pun diangkut, sedangkan yang masih dipegang dibiarkan.'},
  'Memory leak dan cara mencegahnya': {'an': 'Memory leak itu seperti keran yang lupa ditutup: sedikit demi sedikit air (memori) terbuang sampai bak penuh.'},
  'Konsol tingkat lanjut': {'an': 'Konsol DevTools itu seperti dasbor mobil: menampilkan petunjuk dan peringatan agar kamu tahu apa yang terjadi di dalam mesin.'},
  'Debugging dengan breakpoint': {'an': 'Breakpoint itu seperti tombol jeda pada video: kamu menghentikan program di adegan tertentu untuk memeriksa setiap detailnya.'},
  'Menemukan memory leak dengan panel Memory': {'an': 'Memory leak itu seperti keran yang lupa ditutup: sedikit demi sedikit air (memori) terbuang sampai bak penuh. Panel Memory membantu menemukan kerannya.'},
  'Mengukur dan memperbaiki performa': {'an': 'Mengukur performa itu seperti stopwatch pelatih lari: ukur dulu siapa yang lambat, latih bagian itu, lalu ukur lagi.'},
}
for _m in JS:
    for _l in _m['lessons']:
        _l.update(_JS_OVR.get(_l['t'], {}))
assert all(any(l['t'] == k for m in JS for l in m['lessons']) for k in _JS_OVR)

BARU = [('DSA', DSA, DSA_SO), ('PGDBA', PG, PG_SO), ('QA', QA, QA_SO),
        ('DJANGO', DJ, DJ_SO), ('NEXTJS', NX, NX_SO), ('VUE', VUE, VUE_SO), ('DSCI', DSCI, DSCI_SO), ('PROJ', PROJ, PROJ_SO), ('JS', JS, JS_SO)]
