/* ===================== PERSIAPAN LAPTOP =====================
   Panduan memasang alat coding di laptop siswa (Windows, macOS, Linux) dan memasang Ruang Kode
   sebagai aplikasi. Rute: #persiapan dan #persiapan-<jalur> (hanya alat yang dibutuhkan jalur itu). */
const OSES=[['win','Windows'],['mac','macOS'],['lin','Linux (Ubuntu/Debian)']];
const SETUP=[
  {id:'browser',name:'Browser modern',why:'Untuk membuka Ruang Kode, melihat hasil HTML/CSS, dan memakai DevTools (tekan F12).',
   tr:['html','css','fe0','fe','react','ux','ds'],
   os:{win:['Pakai Google Chrome, Microsoft Edge, atau Firefox versi terbaru. Edge sudah terpasang di Windows 10/11.'],
       mac:['Pakai Chrome, Edge, Firefox, atau Safari versi terbaru.'],
       lin:['Pakai Chrome atau Firefox versi terbaru. Firefox biasanya sudah terpasang.']}},
  {id:'vscode',name:'Visual Studio Code',why:'Editor kode gratis untuk semua bahasa di Ruang Kode. Pasang ekstensi sesuai jalur dari menu Extensions (Ctrl+Shift+X).',
   tr:['java','python','ts','fe0','html','css','fe','react','pda','da','de','git'],
   os:{win:['Unduh dari code.visualstudio.com lalu jalankan installer. Centang "Add to PATH" dan "Open with Code".'],
       mac:['Unduh dari code.visualstudio.com, buka file zip, lalu seret Visual Studio Code ke folder Applications.'],
       lin:['Unduh paket .deb dari code.visualstudio.com, atau pasang lewat Snap.']},
   cmd:{win:'winget install Microsoft.VisualStudioCode',mac:'brew install --cask visual-studio-code',lin:'sudo snap install code --classic'},
   check:'code --version',ext:{java:['Extension Pack for Java (Microsoft)'],python:['Python (Microsoft)'],pda:['Python (Microsoft)','Jupyter (Microsoft)'],da:['Python (Microsoft)','Jupyter (Microsoft)'],de:['Python (Microsoft)','Jupyter (Microsoft)'],ts:['ESLint','Prettier'],fe0:['Live Server','Prettier'],html:['Live Server','Prettier'],css:['Live Server','Prettier'],fe:['Live Server','ESLint','Prettier'],react:['ESLint','Prettier'],git:['GitLens']}},
  {id:'python',name:'Python 3',why:'Untuk jalur Python, Python Analisis Data, Data Analyst, dan Data Engineer.',
   tr:['python','pda','da','de'],
   os:{win:['Unduh installer dari python.org (Downloads → Windows).','Saat installer terbuka, centang "Add python.exe to PATH" sebelum menekan Install Now. Langkah ini yang paling sering terlewat.'],
       mac:['Unduh installer .pkg dari python.org lalu ikuti langkahnya. Di macOS, perintahnya python3 (bukan python).'],
       lin:['Python 3 biasanya sudah ada. Pasang juga pip dan venv dengan perintah di bawah. Perintahnya python3.']},
   cmd:{win:'winget install Python.Python.3.13',mac:'brew install python@3.13',lin:'sudo apt install python3 python3-pip python3-venv'},
   check:{win:'python --version',mac:'python3 --version',lin:'python3 --version'},
   first:{file:'halo.py',code:'nama = "Ruang Kode"\nprint(f"Halo dari {nama}!")',run:{win:'python halo.py',mac:'python3 halo.py',lin:'python3 halo.py'},out:'Halo dari Ruang Kode!'}},
  {id:'pandas',name:'pandas, NumPy & Matplotlib',why:'Pustaka analisis data. Pasang di lingkungan virtual (venv) agar tidak bentrok dengan proyek lain.',
   tr:['pda','da','de'],
   os:{win:['Buka folder proyek di terminal VS Code (Ctrl+`), lalu jalankan perintah di bawah satu per satu.'],
       mac:['Buka folder proyek di Terminal, lalu jalankan perintah di bawah satu per satu.'],
       lin:['Buka folder proyek di terminal, lalu jalankan perintah di bawah satu per satu.']},
   cmd:{win:'python -m venv .venv\n.venv\\Scripts\\activate\npip install pandas numpy matplotlib',
        mac:'python3 -m venv .venv\nsource .venv/bin/activate\npip install pandas numpy matplotlib',
        lin:'python3 -m venv .venv\nsource .venv/bin/activate\npip install pandas numpy matplotlib'},
   check:{win:'python -c "import pandas; print(pandas.__version__)"',mac:'python3 -c "import pandas; print(pandas.__version__)"',lin:'python3 -c "import pandas; print(pandas.__version__)"'},
   note:'Jika PowerShell menolak menjalankan activate, jalankan sekali: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned'},
  {id:'java',name:'Java JDK 21',why:'Untuk jalur Java. Pakai JDK (bukan hanya JRE), misalnya Eclipse Temurin yang gratis.',
   tr:['java'],
   os:{win:['Unduh Temurin 21 (LTS) untuk Windows x64 dari adoptium.net, format .msi.','Saat memasang, aktifkan "Set JAVA_HOME variable" dan "Add to PATH".'],
       mac:['Unduh Temurin 21 (LTS) dari adoptium.net, format .pkg. Pilih aarch64 untuk Mac M1/M2/M3/M4, x64 untuk Mac Intel.'],
       lin:['Pasang OpenJDK 21 dari repositori distro dengan perintah di bawah.']},
   cmd:{win:'winget install EclipseAdoptium.Temurin.21.JDK',mac:'brew install --cask temurin@21',lin:'sudo apt install openjdk-21-jdk'},
   check:'java -version',
   first:{file:'Main.java',code:'public class Main {\n    public static void main(String[] args) {\n        String nama = "Ruang Kode";\n        System.out.println("Halo dari " + nama + "!");\n    }\n}',run:'java Main.java',out:'Halo dari Ruang Kode!'}},
  {id:'node',name:'Node.js (versi LTS)',why:'Untuk menjalankan JavaScript dan TypeScript di luar browser, serta npm untuk React, Vite, dan Tailwind.',
   tr:['ts','fe0','fe','react'],
   os:{win:['Unduh installer LTS dari nodejs.org lalu jalankan dengan pilihan bawaan.'],
       mac:['Unduh installer LTS (.pkg) dari nodejs.org lalu ikuti langkahnya.'],
       lin:['Paket Node di repositori Ubuntu sering terlalu lama. Pakai nvm: pasang nvm dari github.com/nvm-sh/nvm, tutup lalu buka lagi terminal, kemudian jalankan perintah di bawah.']},
   cmd:{win:'winget install OpenJS.NodeJS.LTS',mac:'brew install node',lin:'nvm install --lts'},
   check:'node -v',
   first:{file:'halo.js',code:'const nama = "Ruang Kode";\nconsole.log(`Halo dari ${nama}!`);',run:'node halo.js',out:'Halo dari Ruang Kode!'},
   note:'TypeScript dan React dipasang per proyek lewat npm, misalnya npm install -D typescript atau npm create vite@latest. Tidak perlu dipasang global.'},
  {id:'git',name:'Git',why:'Untuk menyimpan riwayat kode dan berkolaborasi di GitHub.',
   tr:['git','fe0','fe','react','de'],
   os:{win:['Unduh Git for Windows dari git-scm.com. Pilihan bawaan sudah cukup; Git Bash ikut terpasang.'],
       mac:['Jalankan xcode-select --install di Terminal, atau pasang lewat Homebrew.'],
       lin:['Pasang dengan perintah di bawah.']},
   cmd:{win:'winget install Git.Git',mac:'brew install git',lin:'sudo apt install git'},
   check:'git --version',
   note:'Setelah terpasang, kenalkan dirimu sekali saja: git config --global user.name "Nama Kamu" lalu git config --global user.email "email@kamu.com".'},
  {id:'sqlite',name:'SQLite & DB Browser for SQLite',why:'Database ringan untuk latihan SQL di laptop. DB Browser memberi tampilan tabel dan editor query.',
   tr:['sql','bi','da','de'],
   os:{win:['Unduh DB Browser for SQLite dari sqlitebrowser.org (versi Standard installer).'],
       mac:['Unduh DB Browser for SQLite dari sqlitebrowser.org, atau pasang lewat Homebrew.'],
       lin:['Pasang dengan perintah di bawah.']},
   cmd:{win:'winget install DBBrowserForSQLite.DBBrowserForSQLite',mac:'brew install --cask db-browser-for-sqlite',lin:'sudo apt install sqlitebrowser sqlite3'},
   note:'Buat database baru (New Database), buka tab Execute SQL, lalu salin query dari pelajaran. Konsol SQL di Ruang Kode tetap bisa dipakai tanpa memasang apa pun.'},
  {id:'figma',name:'Figma',why:'Alat desain antarmuka untuk jalur UX Design dan Design System. Paket gratisnya cukup untuk belajar.',
   tr:['ux','ds'],
   os:{win:['Buka figma.com di browser dan daftar akun gratis. Aplikasi desktop opsional.'],mac:['Buka figma.com di browser dan daftar akun gratis. Aplikasi desktop opsional.'],lin:['Buka figma.com di browser dan daftar akun gratis.']}}];

let SETUP_OS=(()=>{const s=store.get('rk-os',null);if(s)return s;const p=(navigator.userAgentData&&navigator.userAgentData.platform)||navigator.platform||'';return /mac/i.test(p)?'mac':/linux/i.test(p)&&!/android/i.test(navigator.userAgent)?'lin':'win'})();
const pick=(v,os)=>v==null?null:typeof v==='string'?v:v[os];
const cmdBox=c=>pane('bash',c,{label:'TERMINAL'});
function setupItems(tk){return tk?SETUP.filter(s=>s.tr.includes(tk)):SETUP}
function renderSetup(tk){
  const t=tk&&TK[tk],items=setupItems(tk);
  return `<header class="ch-head"><nav class="crumb" aria-label="Lokasi"><a href="#beranda">Beranda</a><span>/</span>${t?`<a href="#${t.k}">${t.name}</a><span>/</span>`:''}<span>Persiapan laptop</span></nav>
   <div class="eyebrow">Persiapan</div><h1>${t?`Siapkan laptop untuk ${t.name}`:'Siapkan laptop untuk belajar'}</h1>
   <p class="lead muted">Semua latihan di Ruang Kode bisa langsung dikerjakan di browser. Pasang alat di bawah agar kamu juga bisa menulis dan menjalankan program sendiri di laptop, seperti di dunia kerja.</p></header>
  <div class="su-bar"><div class="chips" role="group" aria-label="Sistem operasi" id="suOs">${OSES.map(([k,n])=>`<button class="chip" data-os="${k}" aria-pressed="${k===SETUP_OS}">${n}</button>`).join('')}</div>
   <label class="su-tk">Jalur <select id="suTk"><option value="">Semua alat</option>${TRACKS.map(x=>`<option value="${x.k}" ${x.k===tk?'selected':''}>${x.name}</option>`).join('')}</select></label></div>
  <section class="section su-app" id="pasang"><h2>1. Pasang Ruang Kode di laptop</h2>
   <p>Ruang Kode bisa dipasang seperti aplikasi: muncul di menu Start atau Dock, terbuka di jendelanya sendiri, dan tetap bisa dipakai tanpa internet setelah dibuka sekali.</p>
   <ol class="su-steps">${{win:['Buka Ruang Kode di Chrome atau Edge.','Klik ikon pasang (layar dengan panah ke bawah) di ujung kanan kolom alamat. Di Edge bisa juga lewat menu ⋯ → Aplikasi → Pasang situs ini sebagai aplikasi.','Klik Pasang. Ruang Kode muncul di menu Start dan bisa disematkan ke taskbar.'],
     mac:['Buka Ruang Kode di Chrome atau Edge, lalu klik ikon pasang di ujung kanan kolom alamat.','Di Safari (macOS Sonoma ke atas): menu File → Tambahkan ke Dock.','Ruang Kode muncul di Launchpad dan Dock.'],
     lin:['Buka Ruang Kode di Chrome atau Chromium.','Klik ikon pasang di ujung kanan kolom alamat, lalu Pasang.','Firefox belum mendukung pemasangan aplikasi web; simpan sebagai bookmark saja.']}[SETUP_OS].map(s=>`<li>${s}</li>`).join('')}</ol>
   <div class="su-row"><button class="btn primary" id="suInst" ${INSTALL?'':'hidden'}>Pasang Ruang Kode sekarang</button>
   <p class="muted small">Progres tersimpan di browser yang dipakai. Pindah laptop? Salin cadangan progres dari halaman <a href="#saya">Belajar saya</a>.</p></div></section>
  <section class="section"><h2>2. Pasang alat coding</h2><p class="muted">${t?`Yang dibutuhkan jalur ${t.name}: ${items.map(s=>s.name).join(', ')}.`:'Pasang sesuai jalur yang kamu ikuti. Pilih jalur di atas untuk menyaring.'}</p>
   <div class="su-list">${items.map((s,i)=>{const c=pick(s.cmd,SETUP_OS),ck=pick(s.check,SETUP_OS),f=s.first;
     return `<article class="su-card" id="su-${s.id}"><div class="su-h"><span class="su-n">${i+1}</span><div><h3>${s.name}</h3><p class="muted">${s.why}</p>
       <div class="su-for">${s.tr.filter(k=>!tk||k===tk).map(k=>`<a class="rn ${tcls(TK[k])}" href="#persiapan-${k}">${TK[k].name}</a>`).join('')}</div></div></div>
      <ol class="su-steps">${s.os[SETUP_OS].map(x=>`<li>${x}</li>`).join('')}</ol>
      ${c?`<p class="su-lbl">${s.id==='pandas'?'Perintah':`Atau pasang lewat terminal${SETUP_OS==='mac'?' (butuh Homebrew dari brew.sh)':''}`}:</p>${cmdBox(c)}`:''}
      ${ck?`<p class="su-lbl">Cek berhasil atau belum: tutup lalu buka lagi terminal, kemudian jalankan</p>${cmdBox(ck)}<p class="muted small">Jika muncul nomor versi, berarti sudah terpasang. Jika muncul "not recognized" atau "command not found", ulangi pemasangan atau mulai ulang laptop.</p>`:''}
      ${(e=>e.length?`<p class="small">Ekstensi yang disarankan: ${e.join(', ')}.</p>`:'')(s.ext?[...new Set(tk?s.ext[tk]||[]:Object.values(s.ext).flat())]:[])}${s.note?`<p class="su-note">💡 ${esc(s.note)}</p>`:''}
      ${f?`<details class="su-first"><summary>Program pertama dengan ${s.name}</summary><div class="su-fi"><p>Buat folder <code>latihan</code>, buka di VS Code (File → Open Folder), buat file <code>${f.file}</code> berisi:</p>
        ${pane(s.id==='node'?'js':s.id,f.code,{label:f.file})}
        <p>Simpan, buka terminal di VS Code (Ctrl+\`), lalu jalankan:</p>${cmdBox(pick(f.run,SETUP_OS))}<p>Hasilnya:</p><div class="console">${esc(f.out)}</div></div></details>`:''}</article>`}).join('')}</div></section>
  <section class="section"><h2>3. Kalau ada kendala</h2><ul class="points">
   <li><b>Perintah tidak dikenali</b> setelah memasang: tutup semua jendela terminal dan VS Code lalu buka lagi. Di Windows, pastikan pilihan "Add to PATH" dicentang saat memasang.</li>
   <li><b>Laptop sekolah atau kampus</b> tidak mengizinkan memasang aplikasi: minta bantuan admin, atau kerjakan latihan langsung di Ruang Kode yang berjalan di browser.</li>
   <li><b>Ruang penyimpanan</b>: siapkan sekitar 2 GB ruang kosong. Setiap alat di atas umumnya butuh kurang dari 500 MB.</li>
   <li><b>Laptop lama</b>: semua alat ini berjalan di laptop dengan RAM 4 GB, meski lebih nyaman dengan 8 GB.</li></ul></section>`;
}
function wireSetup(tk){
  $('#suOs').addEventListener('click',e=>{const b=e.target.closest('[data-os]');if(!b)return;SETUP_OS=b.dataset.os;store.set('rk-os',SETUP_OS);const y=scrollY;route();scrollTo(0,y)});
  $('#suTk').onchange=e=>{location.hash=e.target.value?'persiapan-'+e.target.value:'persiapan'};
  const ib=$('#suInst');if(ib)ib.onclick=async()=>{if(!INSTALL)return;INSTALL.prompt();const r=await INSTALL.userChoice;INSTALL=null;ib.hidden=true;if(r.outcome==='accepted')toast('Ruang Kode dipasang')};
}
