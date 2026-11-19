"""Pendalaman jalur Git & GitHub: istilah dunia kerja dan contoh perintah dengan keluaran nyata."""
K = 'git'


def B(t, code, out=None, b=None):
    return dict(t=t, b=b, code=code, lang='bash', run=False, out=out)


D = {
'Apa itu version control & Git?': dict(
  ist=[('VCS', 'Version Control System: sistem pencatat riwayat perubahan berkas.'),
       ('Distributed VCS', 'Setiap orang punya salinan lengkap riwayat (Git); kebalikannya centralized (SVN).'),
       ('Repository (repo)', 'Folder proyek beserta seluruh riwayat perubahannya.'),
       ('Source of truth', 'Repo utama di GitHub/GitLab yang dianggap versi resmi.')],
  cx=[B('Identitas sebelum commit pertama', "git config --global user.name \"Sari Lubis\"\ngit config --global user.email \"sari@contoh.id\"\ngit config --global init.defaultBranch main\ngit config --list --global",
        "user.name=Sari Lubis\nuser.email=sari@contoh.id\ninit.defaultbranch=main", 'Nama dan email tercatat di setiap commit. Gunakan email yang sama dengan akun GitHub.')]),
'Membaca status repositori': dict(
  ist=[('Working tree', 'Berkas yang sedang kamu edit.'),
       ('Staging area / index', 'Tempat menyiapkan perubahan yang akan masuk commit berikutnya.'),
       ('Untracked', 'Berkas baru yang belum pernah dilacak Git.'),
       ('Clean working tree', 'Tidak ada perubahan yang belum di-commit.')],
  cx=[B('Status ringkas', "git status -sb", "## main...origin/main [ahead 1]\n M src/app.js\nA  src/util.js\n?? catatan.txt",
        'M = diubah, A = baru di staging, ?? = belum dilacak. "ahead 1" berarti ada 1 commit lokal yang belum di-push.')]),
'init, add, commit': dict(
  ist=[('Atomic commit', 'Satu commit untuk satu perubahan logis; mudah di-review dan di-revert.'),
       ('Conventional Commits', 'Format pesan: feat:, fix:, docs:, refactor:, test:, chore:.'),
       ('Commit hash (SHA)', 'Sidik jari unik tiap commit, misalnya a1b2c3d.'),
       ('git add -p', 'Memilih potongan perubahan (hunk) yang ingin di-stage.')],
  cx=[B('Commit dengan pesan Conventional Commits', "git add src/keranjang.js\ngit commit -m \"feat(keranjang): hitung ongkir berdasarkan berat\"\ngit log --oneline -3",
        "7c1e9a2 (HEAD -> main) feat(keranjang): hitung ongkir berdasarkan berat\n3f0b5d1 fix(login): pesan error saat email kosong\n91ad4e0 chore: inisialisasi proyek")]),
'Riwayat & perbedaan: log dan diff': dict(
  ist=[('HEAD', 'Penunjuk ke commit yang sedang kamu pakai.'),
       ('Diff', 'Perbedaan isi berkas antara dua keadaan.'),
       ('Blame', 'git blame: siapa terakhir mengubah tiap baris; dipakai untuk mencari konteks, bukan menyalahkan.'),
       ('Range', 'main..fitur: commit yang ada di fitur tetapi belum di main.')],
  cx=[B('Riwayat bercabang dan perubahan staging', "git log --oneline --graph --all -6\ngit diff --staged --stat",
        "* 9e2f1aa (fitur/kupon) feat: validasi kode kupon\n* 4b77c02 feat: tabel kupon\n| * 7c1e9a2 (HEAD -> main) feat(keranjang): hitung ongkir\n|/\n* 3f0b5d1 fix(login): pesan error saat email kosong\n src/keranjang.js | 14 ++++++++++----\n 1 file changed, 10 insertions(+), 4 deletions(-)")]),
'.gitignore': dict(
  ist=[('Secret leakage', 'Kebocoran kunci API/password karena .env ikut ter-commit.'),
       ('Build artifact', 'Hasil build (dist/, target/, node_modules/) yang tidak perlu disimpan.'),
       ('.env.example', 'Contoh variabel lingkungan tanpa nilai rahasia; ini yang di-commit.'),
       ('git rm --cached', 'Berhenti melacak berkas tanpa menghapusnya dari disk.')],
  cx=[B('.gitignore umum untuk proyek Java + Node', "cat .gitignore\ngit check-ignore -v .env target/app.jar",
        "# rahasia\n.env\n*.pem\n# build\ntarget/\ndist/\nnode_modules/\n# IDE\n.idea/\n.vscode/\n.gitignore:2:.env\t.env\n.gitignore:5:target/\ttarget/app.jar",
        'Jika .env sudah terlanjur di-push, menghapusnya tidak cukup. Kunci harus diganti (rotate) karena riwayat Git tetap menyimpannya.')]),
'Membatalkan perubahan': dict(
  ist=[('git restore', 'Membuang perubahan di working tree atau mengeluarkan dari staging.'),
       ('git revert', 'Membuat commit baru yang membalik commit lama; aman untuk cabang bersama.'),
       ('git reset', 'Memindahkan cabang ke commit lain; berbahaya untuk commit yang sudah di-push.'),
       ('Reflog', 'Catatan semua pergerakan HEAD; penyelamat saat "kehilangan" commit.')],
  cx=[B('Membatalkan commit yang sudah di-push dengan aman', "git revert 7c1e9a2 --no-edit\ngit log --oneline -2",
        "b40d2c9 (HEAD -> main) Revert \"feat(keranjang): hitung ongkir berdasarkan berat\"\n7c1e9a2 feat(keranjang): hitung ongkir berdasarkan berat"),
      B('Menemukan commit yang hilang setelah reset', "git reflog -3\ngit branch penyelamatan 9e2f1aa",
        "3f0b5d1 HEAD@{0}: reset: moving to HEAD~2\n9e2f1aa HEAD@{1}: commit: feat: validasi kode kupon\n4b77c02 HEAD@{2}: commit: feat: tabel kupon")]),
'Tag & rilis dengan semantic versioning': dict(
  ist=[('SemVer', 'MAJOR.MINOR.PATCH: MAJOR untuk perubahan yang merusak, MINOR fitur baru, PATCH perbaikan.'),
       ('Annotated tag', 'Tag dengan pesan, penulis, dan tanggal; dipakai untuk rilis.'),
       ('Changelog', 'Catatan perubahan tiap versi untuk pengguna.'),
       ('Release candidate (rc)', 'Versi kandidat sebelum rilis final, misalnya v2.0.0-rc.1.')],
  cx=[B('Membuat dan mendorong tag rilis', "git tag -a v1.4.0 -m \"Rilis 1.4.0: kupon diskon\"\ngit push origin v1.4.0\ngit describe --tags",
        "To github.com:sari/toko.git\n * [new tag]         v1.4.0 -> v1.4.0\nv1.4.0")]),
'Branch & merge': dict(
  ist=[('Feature branch', 'Cabang untuk satu fitur; nama seperti fitur/kupon atau feat/123-kupon.'),
       ('Fast-forward', 'Merge tanpa commit baru karena main belum berubah.'),
       ('Merge commit', 'Commit dengan dua induk yang menyatukan dua cabang.'),
       ('Stale branch', 'Cabang lama yang tidak lagi dipakai; sebaiknya dihapus.')],
  cx=[B('Alur cabang fitur', "git switch -c fitur/kupon\n# ... edit, add, commit ...\ngit switch main\ngit merge --no-ff fitur/kupon -m \"Merge fitur kupon\"\ngit branch -d fitur/kupon",
        "Switched to a new branch 'fitur/kupon'\nSwitched to branch 'main'\nMerge made by the 'ort' strategy.\n src/kupon.js | 42 ++++++++++++++++++++++++++++\n 1 file changed, 42 insertions(+)\nDeleted branch fitur/kupon (was 9e2f1aa).")]),
'Menyelesaikan konflik merge': dict(
  ist=[('Merge conflict', 'Dua cabang mengubah baris yang sama; Git minta manusia memutuskan.'),
       ('Conflict markers', 'Penanda <<<<<<<, =======, >>>>>>> di berkas.'),
       ('ours / theirs', 'Versi cabang kita / versi cabang yang digabungkan.'),
       ('Rerere', 'Fitur Git yang mengingat cara menyelesaikan konflik yang sama.')],
  cx=[B('Isi berkas saat konflik', "git merge fitur/ongkir\ncat src/ongkir.js",
        "CONFLICT (content): Merge conflict in src/ongkir.js\nAutomatic merge failed; fix conflicts and then commit the result.\n<<<<<<< HEAD\nconst ONGKIR_PER_KG = 9000;\n=======\nconst ONGKIR_PER_KG = 10000;\n>>>>>>> fitur/ongkir",
        'Diskusikan dengan rekan, sisakan nilai yang benar, hapus penanda, lalu git add dan git commit.')]),
'Stash & rebase': dict(
  ist=[('Stash', 'Menyimpan sementara perubahan yang belum siap di-commit.'),
       ('Rebase', 'Memindahkan commit ke atas basis baru agar riwayat lurus.'),
       ('Interactive rebase', 'git rebase -i untuk squash, ubah pesan, atau urutkan commit sebelum PR.'),
       ('Golden rule of rebasing', 'Jangan rebase commit yang sudah dipakai orang lain.')],
  cx=[B('Memperbarui cabang fitur dengan main terbaru', "git stash push -m \"setengah jadi\"\ngit fetch origin\ngit rebase origin/main\ngit stash pop",
        "Saved working directory and index state On fitur/kupon: setengah jadi\nSuccessfully rebased and updated refs/heads/fitur/kupon.\nOn branch fitur/kupon\nChanges not staged for commit:\n\tmodified:   src/kupon.js\nDropped refs/stash@{0}")]),
'Strategi cabang: GitHub Flow & trunk-based': dict(
  ist=[('Trunk-based development', 'Semua orang sering menggabung ke main dalam cabang berumur pendek.'),
       ('Feature flag', 'Saklar untuk menyembunyikan fitur yang belum selesai meski kodenya sudah di main.'),
       ('Git Flow', 'Model lama dengan develop, release, hotfix; cocok untuk rilis berjadwal.'),
       ('Continuous delivery', 'Main selalu siap rilis kapan saja.')],
  cx=[B('Aturan cabang tim (contoh CONTRIBUTING.md)', "cat CONTRIBUTING.md",
        "1. Buat cabang dari main: feat/<nomor-issue>-<ringkas>\n2. Umur cabang maksimal 2 hari; pecah PR besar\n3. Fitur belum selesai disembunyikan dengan feature flag\n4. PR wajib lolos CI dan 1 review\n5. Squash merge, hapus cabang setelah merge")]),
'Remote, push & pull': dict(
  ist=[('origin / upstream', 'origin: remote milikmu; upstream: repo asli yang kamu fork.'),
       ('Tracking branch', 'Cabang lokal yang terhubung dengan cabang remote.'),
       ('Force push', 'Menimpa riwayat remote; gunakan --force-with-lease jika benar-benar perlu.'),
       ('Pull --rebase', 'Ambil perubahan remote lalu letakkan commit lokal di atasnya, tanpa merge commit.')],
  cx=[B('Push pertama dan pull yang rapi', "git remote add origin git@github.com:sari/toko.git\ngit push -u origin main\ngit pull --rebase",
        "Enumerating objects: 42, done.\nTo github.com:sari/toko.git\n * [new branch]      main -> main\nbranch 'main' set up to track 'origin/main'.\nCurrent branch main is up to date.")]),
'Fork & pull request': dict(
  ist=[('Pull request (PR) / merge request (MR)', 'Permintaan menggabungkan perubahan, tempat review dan diskusi.'),
       ('Code review', 'Pemeriksaan kode oleh rekan sebelum digabung.'),
       ('LGTM', '"Looks good to me": persetujuan informal dalam review.'),
       ('Draft PR', 'PR yang belum siap di-review, untuk berbagi progres lebih awal.')],
  cx=[B('Membuat PR dari terminal dengan GitHub CLI', "gh pr create --base main --title \"feat: kupon diskon\" --body \"Menutup #42. Cara uji: tambahkan kupon HARBOLNAS di keranjang.\"\ngh pr checks",
        "https://github.com/sari/toko/pull/57\nAll checks were successful\n✓  build   1m12s\n✓  test    2m03s")]),
'Issue, label & project board': dict(
  ist=[('Backlog', 'Daftar pekerjaan yang belum dikerjakan, diurutkan prioritas.'),
       ('Acceptance criteria', 'Syarat yang harus terpenuhi agar issue dianggap selesai.'),
       ('Triage', 'Memilah issue baru: valid atau tidak, prioritas, siapa yang mengerjakan.'),
       ('Closing keyword', '"Closes #42" di PR otomatis menutup issue saat merge.')],
  cx=[B('Membuat issue dengan label', "gh issue create --title \"Kupon tidak berlaku di checkout\" --label bug,prioritas-tinggi --body \"Langkah: ... Diharapkan: ... Terjadi: ...\"\ngh issue list --label bug",
        "https://github.com/sari/toko/issues/58\n58  Kupon tidak berlaku di checkout  bug, prioritas-tinggi  about 1 minute ago")]),
'README & Markdown': dict(
  ist=[('README-driven development', 'Menulis README dulu untuk memperjelas tujuan sebelum coding.'),
       ('Badge', 'Gambar kecil status (build passing, versi, lisensi) di README.'),
       ('Quick start', 'Langkah tersingkat agar orang bisa menjalankan proyek.'),
       ('LICENSE', 'Berkas lisensi; tanpa lisensi, orang lain tidak berhak memakai kodemu.')],
  cx=[B('Kerangka README yang disukai rekruter', "cat README.md",
        "# Toko Kopi Nusantara\nAplikasi toko online dengan kupon diskon dan ongkir otomatis.\n\n![CI](https://github.com/sari/toko/actions/workflows/ci.yml/badge.svg)\n\n## Fitur\n- Katalog, keranjang, checkout\n## Teknologi\nJava 21, Spring Boot 3, PostgreSQL 16\n## Menjalankan\n    docker compose up\n## Arsitektur\n(diagram)\n## Yang saya pelajari")]),
'GitHub Pages & Actions': dict(
  ist=[('CI', 'Continuous Integration: build dan tes otomatis setiap push/PR.'),
       ('Workflow / job / step', 'Struktur berkas GitHub Actions di .github/workflows/.'),
       ('Runner', 'Mesin yang menjalankan job (ubuntu-latest).'),
       ('Secrets', 'Nilai rahasia yang disimpan di pengaturan repo, dipanggil ${{ secrets.NAMA }}.')],
  cx=[dict(t='Workflow CI untuk proyek Java (Maven)', lang='yaml', run=False, code="name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-java@v4\n        with:\n          distribution: temurin\n          java-version: '21'\n          cache: maven\n      - run: mvn -B verify")]),
'Keamanan & aturan cabang': dict(
  ist=[('Branch protection', 'Aturan: main tidak boleh di-push langsung, wajib PR, review, dan CI hijau.'),
       ('CODEOWNERS', 'Berkas yang menentukan siapa reviewer wajib untuk folder tertentu.'),
       ('Dependabot', 'Bot yang membuat PR pembaruan dependensi rentan.'),
       ('Signed commit', 'Commit bertanda tangan GPG/SSH sebagai bukti identitas penulis.')],
  cx=[B('Commit bertanda tangan dengan kunci SSH', "git config --global gpg.format ssh\ngit config --global user.signingkey ~/.ssh/id_ed25519.pub\ngit config --global commit.gpgsign true\ngit log --show-signature -1",
        "commit 5ac3e10 (HEAD -> main)\nGood \"git\" signature for sari@contoh.id with ED25519 key SHA256:Qm...\nAuthor: Sari Lubis <sari@contoh.id>\n    docs: perbarui README")]),
'git bisect: mencari commit penyebab bug': dict(
  ist=[('Regression', 'Fitur yang dulu jalan menjadi rusak setelah perubahan baru.'),
       ('Binary search', 'Bisect membagi dua rentang commit sampai penyebabnya ketemu.'),
       ('Good / bad commit', 'Commit yang diketahui sehat / rusak sebagai batas awal.'),
       ('git bisect run', 'Mengotomatiskan bisect dengan skrip tes.')],
  cx=[B('Bisect otomatis dengan tes', "git bisect start\ngit bisect bad HEAD\ngit bisect good v1.3.0\ngit bisect run mvn -q test -Dtest=OngkirTest",
        "Bisecting: 12 revisions left to test after this (roughly 4 steps)\n...\n4b77c02 is the first bad commit\n    feat: pembulatan ongkir ke ribuan\nbisect found first bad commit")]),
'Portofolio di GitHub Pages dengan alur PR': dict(
  ist=[('Portfolio repo', 'Repo yang dipamerkan ke rekruter: README rapi, demo, riwayat commit bersih.'),
       ('Pinned repositories', 'Repo yang disematkan di profil GitHub.'),
       ('Contribution graph', 'Grafik aktivitas commit; konsistensi lebih penting dari jumlah.'),
       ('Custom domain', 'Domain sendiri untuk GitHub Pages lewat berkas CNAME.')],
  cx=[B('Mengaktifkan GitHub Pages dari terminal', "gh api -X POST repos/sari/sari.github.io/pages -f 'source[branch]=main' -f 'source[path]=/'\ngh api repos/sari/sari.github.io/pages --jq .html_url",
        "https://sari.github.io/")]),
}
