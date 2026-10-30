/* ===================== JALUR GIT & GITHUB =====================
   Mengikuti roadmap.sh/git-github-beginner. Contoh perintah ditampilkan bersama
   keluaran terminal yang khas (run:false); simulasi grafik commit ada di viz 'gitsim'. */
const GIT_MODULES=[
{t:'Dasar version control',lvl:'Pemula',d:'Kenapa kode perlu riwayat, apa itu Git, dan cara memasangnya.',
 nodes:['What is Version Control?','Why use Version Control?','Git vs Other VCS','Installing Git Locally','Learn the Basics'],
 lessons:[
  {k:'c',t:'Apa itu version control & Git?',nodes:['What is Version Control?','Why use Version Control?','Git vs Other VCS'],lang:'bash',run:false,
   b:['<b>Version control</b> mencatat setiap perubahan pada berkas sehingga kamu bisa melihat siapa mengubah apa, kapan, dan kenapa, lalu kembali ke versi mana pun. Tanpa itu, folder proyek cepat dipenuhi <code>final.html</code>, <code>final-revisi.html</code>, <code>final-benar-benar.html</code>.',
      '<b>Git</b> adalah version control <b>terdistribusi</b>: setiap salinan proyek menyimpan riwayat lengkap, jadi kamu bisa bekerja dan membuat commit tanpa internet. Sistem lama seperti SVN bersifat terpusat, setiap commit harus terhubung ke server.',
      '<b>GitHub</b> bukan Git. GitHub adalah layanan yang menyimpan repositori Git di internet dan menambahkan fitur kolaborasi: pull request, issue, review, dan Actions. Alternatifnya GitLab dan Bitbucket.'],
   code:`$ git --version
git version 2.47.0

$ git config --global user.name "Sari Wulandari"
$ git config --global user.email "sari@contoh.id"
$ git config --global init.defaultBranch main
$ git config --list | grep user
user.name=Sari Wulandari
user.email=sari@contoh.id`,
   pts:['Version control = riwayat perubahan yang bisa dikembalikan.','Git terdistribusi: riwayat lengkap ada di setiap salinan.','GitHub adalah tempat menyimpan dan berkolaborasi, Git adalah alatnya.','Atur nama dan email sekali dengan git config --global.'],
   q:[['Apa perbedaan Git dan GitHub?',['Git alat version control, GitHub layanan hosting repositori','Keduanya sama','GitHub versi baru dari Git'],0,'Git berjalan di komputermu; GitHub menyimpan salinan di internet.'],
      ['Kenapa Git disebut terdistribusi?',['Setiap salinan menyimpan riwayat lengkap','Kode dibagi ke banyak server','Hanya bisa dipakai berkelompok'],0,'Kamu bisa commit tanpa koneksi ke server.']]},
  {k:'c',t:'Membaca status repositori',nodes:['Learn the Basics'],lang:'bash',run:false,
   b:['Setiap berkas di repositori berada di salah satu dari tiga tempat: <b>working directory</b> (berkas yang kamu edit), <b>staging area</b> (perubahan yang sudah dipilih untuk commit berikutnya), dan <b>repositori</b> (riwayat commit di folder <code>.git</code>).',
      '<code>git status</code> adalah perintah yang paling sering dipakai. Ia memberi tahu cabang aktif, berkas yang berubah, dan berkas yang belum dilacak, sekaligus menyarankan perintah berikutnya.',
      'Biasakan menjalankan <code>git status</code> sebelum dan sesudah setiap perintah. Kebiasaan ini mencegah sebagian besar kesalahan pemula.'],
   code:`$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   index.html

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   gaya.css

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        logo.svg`,
   pts:['Tiga tempat: working directory, staging area, repositori.','git status menunjukkan posisi setiap berkas.','Untracked = berkas baru yang belum pernah di-add.'],
   q:[['Dari keluaran di atas, berkas mana yang akan masuk commit berikutnya?',['index.html','gaya.css','logo.svg'],0,'Hanya berkas di "Changes to be committed" yang ikut.'],
      ['logo.svg berstatus?',['Untracked, belum pernah dilacak','Sudah di-commit','Dihapus'],0,'Perlu git add agar mulai dilacak.']]}
 ]},
{t:'Penggunaan dasar Git',lvl:'Pemula',d:'Membuat repositori, commit, melihat riwayat, dan membatalkan perubahan.',
 nodes:['git init','git add','git commit','git log','.gitignore','git diff','git restore','git reset','git revert','Commit Messages'],
 lessons:[
  {k:'c',t:'init, add, commit',nodes:['git init','git add','git commit','Commit Messages'],lang:'bash',run:false,viz:'gitsim',
   b:['<code>git init</code> mengubah folder biasa menjadi repositori dengan membuat folder tersembunyi <code>.git</code>. Lalu alurnya selalu sama: ubah berkas, <code>git add</code> untuk memasukkannya ke staging, <code>git commit</code> untuk menyimpan potret permanen.',
      'Setiap commit punya <b>hash</b> unik (misalnya <code>3f9a1c2</code>), penulis, waktu, pesan, dan penunjuk ke commit sebelumnya. Rangkaian penunjuk inilah yang membentuk riwayat.',
      'Pesan commit yang baik menjelaskan <b>apa</b> dan <b>kenapa</b> dalam kalimat perintah singkat: <code>Tambah validasi email di form daftar</code>, bukan <code>update</code> atau <code>fix</code>. Banyak tim memakai Conventional Commits: <code>feat:</code>, <code>fix:</code>, <code>docs:</code>.'],
   code:`$ mkdir toko-nusantara && cd toko-nusantara
$ git init
Initialized empty Git repository in /home/sari/toko-nusantara/.git/

$ echo "<h1>Toko Nusantara</h1>" > index.html
$ git add index.html
$ git commit -m "feat: halaman awal toko"
[main (root-commit) 3f9a1c2] feat: halaman awal toko
 1 file changed, 1 insertion(+)
 create mode 100644 index.html`,
   pts:['git init sekali per proyek.','Ubah → git add → git commit.','Commit = potret + hash + pesan + induk.','Pesan commit menjelaskan apa dan kenapa.'],
   q:[['Perintah apa yang memindahkan perubahan ke staging area?',['git add','git commit','git init'],0,'Commit hanya menyimpan apa yang sudah di-stage.'],
      ['Pesan commit mana yang paling baik?',['fix: harga diskon tidak dibulatkan ke rupiah','update','perbaikan lagi'],0,'Spesifik dan menjelaskan masalahnya.']]},
  {k:'c',t:'Riwayat & perbedaan: log dan diff',nodes:['git log','git diff'],lang:'bash',run:false,
   b:['<code>git log</code> menampilkan riwayat dari commit terbaru. Versi ringkas <code>git log --oneline --graph</code> menampilkan satu baris per commit beserta gambar cabang.',
      '<code>git diff</code> menunjukkan baris yang berubah tetapi belum di-stage. <code>git diff --staged</code> menunjukkan apa yang akan masuk commit. Baris diawali <code>-</code> dihapus, <code>+</code> ditambahkan.',
      'Sebelum commit, lihat <code>git diff --staged</code> agar tidak ada berkas debug atau kata sandi yang ikut tersimpan.'],
   code:`$ git log --oneline
a71be04 (HEAD -> main) style: warna tombol beli
5c2d9e1 feat: daftar produk
3f9a1c2 feat: halaman awal toko

$ git diff
diff --git a/gaya.css b/gaya.css
@@ -1,3 +1,3 @@
 .tombol {
-  background: #2563eb;
+  background: #b4532a;
 }`,
   pts:['git log --oneline untuk riwayat ringkas.','git diff = belum di-stage; --staged = akan di-commit.','HEAD menunjuk commit tempat kamu berada sekarang.'],
   q:[['Perintah untuk melihat perubahan yang SUDAH di-stage?',['git diff --staged','git diff','git log'],0,'Tanpa --staged, diff hanya menampilkan yang belum di-stage.'],
      ['Pada diff, baris berawalan + artinya?',['Baris ditambahkan','Baris dihapus','Baris penting'],0,'Tanda - untuk baris yang dihapus.']]},
  {k:'c',t:'.gitignore',nodes:['.gitignore'],lang:'text',run:false,
   b:['Tidak semua berkas pantas masuk repositori: folder <code>node_modules</code> (bisa dipasang ulang), hasil build <code>dist/</code>, berkas sistem <code>.DS_Store</code>, dan terutama <b>rahasia</b> seperti <code>.env</code> yang berisi kunci API.',
      'Tuliskan pola nama berkas di <code>.gitignore</code> di akar proyek. Git akan berhenti menampilkannya sebagai untracked. Tanda <code>!</code> membuat pengecualian.',
      'Penting: .gitignore tidak berlaku untuk berkas yang <b>sudah</b> di-commit. Kalau kunci API terlanjur masuk riwayat, ganti kuncinya, karena riwayat Git bisa dibaca siapa pun yang punya salinan.'],
   code:`# dependensi dan hasil build
node_modules/
dist/

# rahasia: jangan pernah di-commit
.env
.env.*
!.env.example

# berkas sistem dan editor
.DS_Store
.vscode/
*.log`,
   pts:['Abaikan dependensi, hasil build, log, dan rahasia.','Pola: folder/, *.ext, ! untuk pengecualian.','Berkas yang terlanjur di-commit tetap ada di riwayat.'],
   q:[['Berkas .env.example pada contoh di atas?',['Tetap dilacak karena pola !','Diabaikan','Dihapus'],0,'Berkas contoh tanpa nilai rahasia boleh dibagikan.'],
      ['Kunci API terlanjur di-commit lalu ditambahkan ke .gitignore. Apa yang harus dilakukan?',['Ganti (rotate) kuncinya','Cukup .gitignore','Hapus folder .git'],0,'Riwayat lama masih memuat kunci itu.']]},
  {k:'c',t:'Membatalkan perubahan',nodes:['git restore','git reset','git revert'],lang:'bash',run:false,
   b:['Ada tiga situasi umum. Membuang perubahan berkas yang belum di-stage: <code>git restore berkas</code>. Mengeluarkan berkas dari staging: <code>git restore --staged berkas</code>.',
      'Membatalkan commit yang <b>belum</b> di-push: <code>git reset --soft HEAD~1</code> menghapus commit terakhir tetapi menyimpan perubahannya di staging. <code>--hard</code> membuang perubahan sama sekali, jadi pakai dengan hati-hati.',
      'Membatalkan commit yang <b>sudah</b> di-push: gunakan <code>git revert hash</code>. Revert membuat commit baru yang membalik perubahan, sehingga riwayat orang lain tidak rusak.'],
   code:`$ git restore gaya.css            # buang editan yang belum di-stage
$ git restore --staged index.html  # keluarkan dari staging

$ git reset --soft HEAD~1          # batalkan commit terakhir (lokal)

$ git revert a71be04
[main 9d0e3f7] Revert "style: warna tombol beli"
 1 file changed, 1 insertion(+), 1 deletion(-)`,
   pts:['restore: berkas di working directory atau staging.','reset: hapus commit lokal (--soft simpan, --hard buang).','revert: commit pembalik, aman untuk riwayat bersama.'],
   q:[['Commit salah sudah di-push ke main tim. Cara aman membatalkannya?',['git revert','git reset --hard','Hapus repositori'],0,'Revert tidak menulis ulang riwayat yang sudah dimiliki orang lain.'],
      ['git reset --soft HEAD~1 melakukan apa?',['Membatalkan commit terakhir, perubahan tetap di staging','Membuang semua perubahan','Push ulang'],0,'--soft menjaga perubahanmu.']]}
 ]},
{t:'Branch & merge',lvl:'Pemula',d:'Bekerja paralel dengan cabang, menggabungkan, dan menyelesaikan konflik.',
 nodes:['Branching Basics','git branch','git switch','git merge','Merge Conflicts','Fast-Forward vs Non-FF','git stash','git rebase'],
 lessons:[
  {k:'c',t:'Branch & merge',nodes:['Branching Basics','git branch','git switch','git merge','Fast-Forward vs Non-FF'],lang:'bash',run:false,viz:'gitsim',
   b:['<b>Branch</b> adalah penunjuk ringan ke sebuah commit. Membuat cabang <code>fitur-keranjang</code> memungkinkanmu bereksperimen tanpa mengganggu <code>main</code> yang harus selalu siap rilis.',
      '<code>git switch -c nama</code> membuat dan pindah ke cabang baru. Setelah fitur selesai, kembali ke main lalu <code>git merge nama</code>.',
      'Jika main tidak berubah sejak cabang dibuat, Git cukup menggeser penunjuk main (<b>fast-forward</b>). Jika keduanya punya commit baru, Git membuat <b>merge commit</b> dengan dua induk.'],
   code:`$ git switch -c fitur-keranjang
Switched to a new branch 'fitur-keranjang'
$ git commit -am "feat: tombol tambah ke keranjang"

$ git switch main
$ git merge fitur-keranjang
Updating a71be04..c4e8b21
Fast-forward
 index.html | 4 ++++
 1 file changed, 4 insertions(+)

$ git branch -d fitur-keranjang
Deleted branch fitur-keranjang (was c4e8b21).`,
   pts:['Branch = penunjuk ke commit, murah dibuat.','git switch -c untuk cabang baru.','Fast-forward: cukup geser penunjuk; selain itu merge commit.','Hapus cabang setelah digabung.'],
   q:[['Kapan merge menjadi fast-forward?',['Saat main tidak punya commit baru sejak cabang dibuat','Selalu','Saat ada konflik'],0,'Git cukup menggeser penunjuk main ke depan.'],
      ['Perintah membuat sekaligus pindah ke cabang baru?',['git switch -c nama','git branch','git merge nama'],0,'Versi lama: git checkout -b nama.']]},
  {k:'c',t:'Menyelesaikan konflik merge',nodes:['Merge Conflicts'],lang:'text',run:false,
   b:['<b>Konflik</b> terjadi saat dua cabang mengubah baris yang sama. Git tidak menebak; ia menandai bagian itu dan menunggu keputusanmu.',
      'Di antara <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code> dan <code>=======</code> adalah versi cabangmu sekarang (HEAD); di antara <code>=======</code> dan <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> versi cabang yang digabung. Edit berkas sampai benar, hapus penandanya, lalu <code>git add</code> dan <code>git commit</code>.',
      'Konflik itu normal, bukan tanda gagal. Kurangi frekuensinya dengan cabang berumur pendek dan sering menarik perubahan terbaru dari main.'],
   code:`<<<<<<< HEAD
<button class="tombol">Beli sekarang</button>
=======
<button class="tombol tombol--utama">Tambah ke keranjang</button>
>>>>>>> fitur-keranjang

# setelah diputuskan:
<button class="tombol tombol--utama">Beli sekarang</button>

$ git add index.html
$ git commit -m "merge: gabung fitur-keranjang"`,
   pts:['Konflik = baris yang sama diubah di dua cabang.','HEAD di atas =======, cabang lain di bawah.','Edit, hapus penanda, add, commit.'],
   q:[['Setelah mengedit berkas berkonflik, langkah berikutnya?',['git add lalu git commit','git reset --hard','git init'],0,'git add menandai konflik sudah diselesaikan.']]},
  {k:'c',t:'Stash & rebase',nodes:['git stash','git rebase'],lang:'bash',run:false,
   b:['<code>git stash</code> menyimpan sementara perubahan yang belum di-commit, membuat working directory bersih. Berguna saat harus pindah cabang mendadak untuk memperbaiki bug. Kembalikan dengan <code>git stash pop</code>.',
      '<code>git rebase main</code> memindahkan commit cabangmu seolah dibuat di atas main terbaru, menghasilkan riwayat lurus tanpa merge commit.',
      'Aturan emas: jangan rebase commit yang sudah di-push dan dipakai orang lain, karena rebase membuat hash baru dan menulis ulang riwayat.'],
   code:`$ git stash
Saved working directory and index state WIP on fitur-ongkir: 5c2d9e1
$ git switch main && git switch -c perbaikan-harga
# ... perbaiki, commit ...
$ git switch fitur-ongkir
$ git stash pop

$ git rebase main
Successfully rebased and updated refs/heads/fitur-ongkir.`,
   pts:['stash = simpan sementara, pop = kembalikan.','rebase = tanam ulang commit di atas basis baru.','Jangan rebase riwayat yang sudah dibagikan.'],
   q:[['Kenapa rebase berbahaya untuk commit yang sudah di-push?',['Hash berubah sehingga riwayat orang lain tidak cocok','Rebase menghapus berkas','Rebase lambat'],0,'Rebase menulis ulang riwayat.']]}
 ]},
{t:'GitHub: remote & kolaborasi',lvl:'Menengah',d:'Menghubungkan repositori lokal ke GitHub dan bekerja bersama lewat pull request.',
 nodes:['GitHub','Creating Account','git remote','git push','git pull','git fetch','git clone','Forking','Pull Requests','Code Reviews','Issues','SSH Keys'],
 lessons:[
  {k:'c',t:'Remote, push & pull',nodes:['git remote','git push','git pull','git fetch','git clone','SSH Keys'],lang:'bash',run:false,viz:'gitsim',
   b:['<b>Remote</b> adalah salinan repositori di server, biasanya diberi nama <code>origin</code>. Hubungkan dengan <code>git remote add origin URL</code>, lalu kirim commit dengan <code>git push -u origin main</code> (flag <code>-u</code> cukup sekali).',
      '<code>git fetch</code> mengunduh commit baru dari remote tanpa mengubah cabangmu. <code>git pull</code> = fetch + merge. Biasakan pull sebelum mulai bekerja.',
      '<code>git clone URL</code> mengunduh repositori lengkap beserta riwayatnya. Untuk autentikasi, GitHub memakai kunci SSH atau token, bukan kata sandi akun.'],
   code:`$ git remote add origin git@github.com:sariw/toko-nusantara.git
$ git push -u origin main
Enumerating objects: 9, done.
To github.com:sariw/toko-nusantara.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

$ git pull
Updating c4e8b21..e02f7aa
Fast-forward
 README.md | 12 ++++++++++++

$ git clone https://github.com/sariw/toko-nusantara.git`,
   pts:['origin = nama remote default.','push mengirim, fetch mengunduh, pull = fetch + merge.','clone untuk salinan baru.','Pakai SSH key atau token.'],
   q:[['Apa beda git fetch dan git pull?',['fetch hanya mengunduh, pull mengunduh lalu menggabung','Sama saja','fetch mengirim commit'],0,'fetch aman karena tidak mengubah cabangmu.'],
      ['Flag -u pada git push -u origin main untuk?',['Mengatur cabang upstream agar push/pull berikutnya cukup tanpa argumen','Memaksa push','Menghapus remote'],0,'Setelah itu cukup git push.']]},
  {k:'c',t:'Fork & pull request',nodes:['Forking','Pull Requests','Code Reviews'],lang:'bash',run:false,
   b:['<b>Fork</b> adalah salinan repositori orang lain di akunmu sendiri. Dipakai untuk berkontribusi ke proyek open source tempat kamu tidak punya hak tulis.',
      '<b>Pull request</b> (PR) adalah permintaan agar perubahan di cabangmu digabung ke cabang tujuan. Di PR, rekan tim membaca diff, memberi komentar per baris, dan menyetujui. CI otomatis menjalankan tes.',
      'PR yang mudah direview: kecil (di bawah 400 baris), satu tujuan, judul jelas, deskripsi berisi apa yang berubah, kenapa, dan cara mengujinya, plus tangkapan layar untuk perubahan tampilan.'],
   code:`# 1. Fork lewat tombol Fork di GitHub, lalu:
$ git clone git@github.com:sariw/kamus-daerah.git
$ cd kamus-daerah
$ git remote add upstream https://github.com/komunitas/kamus-daerah.git

# 2. Kerjakan di cabang sendiri
$ git switch -c tambah-bahasa-sunda
$ git commit -am "feat: 120 kosakata bahasa Sunda"
$ git push -u origin tambah-bahasa-sunda

# 3. Buka Pull Request di GitHub: tambah-bahasa-sunda -> komunitas:main

# 4. Selaraskan dengan proyek asal
$ git fetch upstream && git rebase upstream/main`,
   pts:['Fork = salinan di akunmu; upstream = proyek asal.','PR = minta perubahan digabung, tempat review.','PR kecil dan berdeskripsi jelas lebih cepat disetujui.'],
   q:[['Remote upstream biasanya menunjuk ke?',['Repositori asal yang di-fork','Fork milikmu','Komputer lain'],0,'origin = fork milikmu, upstream = proyek asal.'],
      ['Ciri PR yang baik?',['Kecil, satu tujuan, deskripsi jelas','Menggabungkan banyak fitur sekaligus','Tanpa deskripsi'],0,'Reviewer bisa memahami dan menguji dengan cepat.']]},
  {k:'c',t:'Issue, label & project board',nodes:['Issues','GitHub Projects','Labels'],lang:'text',run:false,
   b:['<b>Issue</b> mencatat bug, ide fitur, atau pertanyaan. Issue yang baik untuk bug berisi langkah mereproduksi, hasil yang diharapkan, hasil sebenarnya, dan lingkungan (browser, versi).',
      'Hubungkan PR dengan issue lewat kata kunci di deskripsi: <code>Closes #42</code>. Saat PR digabung, issue otomatis ditutup.',
      '<b>Projects</b> menyusun issue dalam papan kanban (Todo, In progress, Done) sehingga tim melihat pekerjaan yang sedang berjalan.'],
   code:`Judul: Total keranjang salah saat jumlah produk 0

Langkah:
1. Tambah "Kopi Gayo" ke keranjang
2. Ubah jumlah menjadi 0
Diharapkan: produk hilang, total Rp 0
Terjadi: total tetap Rp 85.000
Lingkungan: Chrome 130, Android 14

Label: bug, prioritas-tinggi
---
PR #57: fix: hapus item berjumlah 0 dari keranjang
Closes #42`,
   pts:['Issue bug: langkah, harapan, kenyataan, lingkungan.','Closes #nomor menutup issue saat PR digabung.','Projects untuk papan kerja tim.'],
   q:[['Bagaimana PR menutup issue #42 secara otomatis?',['Tulis "Closes #42" di deskripsi PR','Beri label','Tutup manual saja'],0,'Kata kunci fixes/closes/resolves dikenali GitHub.']]}
 ]},
{t:'Lebih jauh dengan GitHub',lvl:'Menengah',d:'Profil, README, GitHub Pages, Actions, dan keamanan repositori.',
 nodes:['GitHub Profile','README','Markdown','GitHub Pages','GitHub Actions','Branch Protection','Secrets','GitHub CLI'],
 lessons:[
  {k:'c',t:'README & Markdown',nodes:['README','Markdown','GitHub Profile'],lang:'text',run:false,
   b:['<b>README.md</b> adalah halaman depan repositori: apa proyek ini, cara memasang, cara menjalankan, dan cara berkontribusi. Recruiter sering hanya membaca README.',
      'Markdown memakai simbol sederhana: <code>#</code> judul, <code>**tebal**</code>, <code>-</code> daftar, <code>[teks](url)</code> link, dan tiga backtick untuk blok kode.',
      'Repositori bernama sama dengan username-mu (<code>sariw/sariw</code>) menjadi README profil yang tampil di halaman GitHub-mu.'],
   code:`# Toko Nusantara

Toko online produk UMKM: katalog, keranjang, dan checkout.

![Tangkapan layar](docs/layar.png)

## Menjalankan
\`\`\`bash
npm install
npm run dev
\`\`\`

## Fitur
- Pencarian produk
- Keranjang tersimpan di perangkat
- **Mode gelap**

Lisensi: MIT`,
   pts:['README: apa, cara pasang, cara jalankan, kontribusi.','Markdown: # judul, ** tebal, - daftar, [teks](url).','Repositori username/username = README profil.'],
   q:[['Sintaks Markdown untuk link?',['[teks](url)','<link>','(url)[teks]'],0,'Teks dalam kurung siku, alamat dalam kurung biasa.']]},
  {k:'c',t:'GitHub Pages & Actions',nodes:['GitHub Pages','GitHub Actions'],lang:'yaml',run:false,
   b:['<b>GitHub Pages</b> menerbitkan situs statis gratis langsung dari repositori di alamat <code>username.github.io/repo</code>. Cocok untuk portofolio.',
      '<b>GitHub Actions</b> menjalankan alur kerja otomatis saat terjadi peristiwa (push, PR). Berkasnya YAML di <code>.github/workflows/</code>. Contoh umum: menjalankan tes di setiap PR lalu menerbitkan situs dari main.',
      'Setiap job berjalan di mesin baru, jadi langkah pertama selalu <code>actions/checkout</code> untuk mengambil kode.'],
   code:`# .github/workflows/tes.yml
name: Tes
on:
  pull_request:
  push:
    branches: [main]
jobs:
  tes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npm test`,
   pts:['Pages: hosting situs statis gratis.','Actions: otomatisasi berbasis peristiwa (CI/CD).','Workflow YAML di .github/workflows/.'],
   q:[['Kapan workflow di atas berjalan?',['Setiap PR dan setiap push ke main','Hanya manual','Setiap jam'],0,'Lihat bagian on:.']]},
  {k:'c',t:'Keamanan & aturan cabang',nodes:['Branch Protection','Secrets'],lang:'text',run:false,
   b:['<b>Branch protection</b> melindungi main: wajib lewat PR, wajib minimal satu persetujuan, dan wajib lulus tes sebelum boleh digabung. Ini mencegah push langsung yang tidak sengaja merusak produksi.',
      'Simpan kunci API di <b>Secrets</b> (Settings → Secrets and variables → Actions), lalu panggil di workflow sebagai <code>${{ secrets.NAMA }}</code>. Nilainya disamarkan di log.',
      'Aktifkan Dependabot agar GitHub membuka PR otomatis saat ada versi dependensi yang menambal celah keamanan.'],
   code:`Settings → Branches → Add rule: main
  [x] Require a pull request before merging
      Required approvals: 1
  [x] Require status checks to pass: Tes
  [x] Do not allow bypassing the above settings

# di workflow
- run: npm run deploy
  env:
    API_KEY: \${{ secrets.API_KEY }}`,
   pts:['Lindungi main: PR, review, tes wajib.','Rahasia di Secrets, bukan di kode.','Dependabot menjaga dependensi tetap aman.'],
   q:[['Di mana menyimpan kunci API untuk GitHub Actions?',['Repository Secrets','Di README','Di berkas .js'],0,'Secrets terenkripsi dan disamarkan di log.']]}
 ]},
{t:'Proyek akhir',lvl:'Menengah',d:'Praktik seluruh alur Git dan GitHub dari awal sampai situs terbit.',nodes:['Project'],
 lessons:[
  {k:'proj',t:'Portofolio di GitHub Pages dengan alur PR',stack:'Git + GitHub',
   brief:'Buat repositori portofolio, kerjakan setiap bagian di cabang terpisah, gabungkan lewat pull request yang lulus tes otomatis, lalu terbitkan ke GitHub Pages.',
   feats:['Repositori dengan README lengkap dan lisensi','.gitignore untuk node_modules, dist, dan .env','Minimal 3 cabang fitur yang digabung lewat pull request','Satu konflik merge yang diselesaikan dan dicatat di PR','Pesan commit mengikuti Conventional Commits','Branch protection di main: wajib PR dan tes lulus','Workflow Actions yang memeriksa HTML setiap PR','Situs terbit di username.github.io'],
   steps:['Buat repositori dan commit pertama.','Push ke GitHub dan aktifkan branch protection.','Kerjakan bagian "Tentang", "Proyek", "Kontak" di cabang masing-masing.','Buka PR, minta teman mereview, gabungkan.','Aktifkan Pages dari main.'],
   files:[['.github/workflows/cek.yml','yaml',`name: Cek HTML
on: [pull_request]
jobs:
  cek:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx --yes html-validate "**/*.html"`],
    ['urutan-perintah.sh','bash',`git init && git add . && git commit -m "feat: kerangka portofolio"
git remote add origin git@github.com:sariw/portofolio.git
git push -u origin main

git switch -c bagian-proyek
git commit -am "feat: kartu tiga proyek"
git push -u origin bagian-proyek
# buka PR di GitHub, tunggu tes hijau, minta review, merge

git switch main && git pull
git branch -d bagian-proyek`]]}
 ]}
];
