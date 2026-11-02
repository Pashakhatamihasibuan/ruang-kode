/* ===================== ANIMASI KODE OTOMATIS =====================
   Setiap blok kode di pelajaran mendapat tombol "▶ Animasikan". Kode lalu dijalankan
   baris demi baris: baris "diketik", disorot, dan diberi penjelasan singkat yang dibuat
   dari pola umum tiap bahasa. Keluaran (bila ada) muncul di langkah terakhir. */
const CA_LBL={dart:'dart',kotlin:'kotlin',java:'java',python:'python',sql:'sql',js:'js',jsx:'js',ts:'js',tsx:'js',html:'html',css:'css',bash:'bash',yaml:'yaml',json:'json',text:'text'};
function caWhat(line,lang){
  const s=line.trim(),L=CA_LBL[lang]||lang;let m;
  if(!s)return '';
  /* komentar */
  if((m=/^(?:\/\/|#(?!!)|--(?!-)|\/\*+|\*)\s*(.*?)\s*(?:\*\/)?$/.exec(s))&&!(L==='css'&&s.startsWith('#'))&&!(L==='text'))return m[1]?`Komentar: <i>${esc(m[1])}</i>. Komentar tidak dijalankan, hanya catatan untuk pembaca.`:'Komentar, tidak dijalankan.';
  if(L==='sql'){const u=s.toUpperCase();
    const R=[[/^SELECT\b/,'<b>SELECT</b> memilih kolom yang ingin ditampilkan.'],[/^FROM\b/,'<b>FROM</b> menentukan tabel sumber data.'],[/^(LEFT |RIGHT |INNER |FULL |CROSS )?(OUTER )?JOIN\b/,'<b>JOIN</b> menggabungkan baris dari tabel lain yang cocok.'],[/^ON\b/,'<b>ON</b> adalah syarat pencocokan JOIN.'],[/^WHERE\b/,'<b>WHERE</b> menyaring baris sebelum dikelompokkan.'],[/^GROUP BY\b/,'<b>GROUP BY</b> mengelompokkan baris yang nilainya sama.'],[/^HAVING\b/,'<b>HAVING</b> menyaring hasil setelah dikelompokkan.'],[/^ORDER BY\b/,'<b>ORDER BY</b> mengurutkan hasil.'],[/^LIMIT\b/,'<b>LIMIT</b> membatasi jumlah baris hasil.'],[/^INSERT\b/,'<b>INSERT</b> menambah baris baru.'],[/^VALUES\b/,'<b>VALUES</b> berisi nilai untuk baris baru.'],[/^UPDATE\b/,'<b>UPDATE</b> mengubah baris yang sudah ada.'],[/^SET\b/,'<b>SET</b> menentukan kolom dan nilai barunya.'],[/^DELETE\b/,'<b>DELETE</b> menghapus baris.'],[/^CREATE TABLE\b/,'<b>CREATE TABLE</b> membuat tabel baru.'],[/^CREATE (UNIQUE )?INDEX\b/,'<b>CREATE INDEX</b> membuat index agar pencarian lebih cepat.'],[/^CREATE VIEW\b/,'<b>CREATE VIEW</b> menyimpan query sebagai tabel virtual.'],[/^ALTER\b/,'<b>ALTER</b> mengubah struktur tabel.'],[/^DROP\b/,'<b>DROP</b> menghapus objek database.'],[/^WITH\b/,'<b>WITH</b> membuat CTE, query bernama sementara.'],[/^(BEGIN|START TRANSACTION)\b/,'Transaksi dimulai: semua perintah berikut berhasil bersama atau batal bersama.'],[/^COMMIT\b/,'<b>COMMIT</b> menyimpan permanen semua perubahan transaksi.'],[/^ROLLBACK\b/,'<b>ROLLBACK</b> membatalkan perubahan transaksi.'],[/^UNION\b/,'<b>UNION</b> menggabungkan hasil dua query.'],[/^CASE\b|^WHEN\b|^ELSE\b|^END\b/,'<b>CASE</b> memilih nilai berdasarkan kondisi.']];
    for(const [r,t] of R)if(r.test(u))return t;
    if(/^\w+\s+(INTEGER|INT|TEXT|VARCHAR|REAL|DECIMAL|DATE|NUMERIC|BOOLEAN)/i.test(s))return `Kolom <code>${esc(s.split(/\s/)[0])}</code> beserta tipe datanya.`;
    if(/^\)/.test(s))return 'Penutup daftar.';
    return 'Lanjutan perintah SQL di atasnya.'}
  if(L==='html'){
    if((m=/^<!doctype/i.exec(s)))return 'Deklarasi dokumen HTML5.';
    if((m=/^<\/(\w+)/.exec(s)))return `Penutup elemen <code>&lt;${m[1]}&gt;</code>.`;
    if((m=/^<([\w-]+)/.exec(s))){const T={html:'akar dokumen',head:'info halaman (tidak tampil)',body:'isi yang tampil',title:'judul di tab browser',meta:'info tambahan untuk browser/mesin pencari',link:'menghubungkan file lain, misalnya CSS',script:'memuat JavaScript',h1:'judul utama',h2:'subjudul',h3:'subjudul kecil',p:'paragraf',a:'tautan',img:'gambar',ul:'daftar tanpa urutan',ol:'daftar berurutan',li:'butir daftar',div:'wadah umum',span:'wadah dalam baris',form:'formulir',input:'kolom isian',label:'label untuk isian',button:'tombol',table:'tabel',tr:'baris tabel',td:'sel tabel',th:'judul kolom tabel',nav:'navigasi',header:'kepala halaman/bagian',main:'konten utama',footer:'kaki halaman',section:'bagian bertema',article:'konten mandiri',style:'aturan CSS',select:'pilihan',option:'opsi pilihan',textarea:'isian teks panjang',video:'video',audio:'audio',figure:'gambar beserta keterangan'};
      return `Elemen <code>&lt;${m[1]}&gt;</code>${T[m[1]]?': '+T[m[1]]:''}.${/\s(class|id)=/.test(s)?' Atribut class/id dipakai CSS dan JavaScript untuk menemukannya.':''}`}
    return 'Isi teks di dalam elemen.'}
  if(L==='css'){
    if((m=/^@media\s*(.*)\{?/.exec(s)))return `<b>Media query</b>: aturan di dalamnya hanya berlaku saat ${esc(m[1].replace('{','').trim())}.`;
    if((m=/^@keyframes\s+([\w-]+)/.exec(s)))return `Mendefinisikan animasi bernama <code>${m[1]}</code>.`;
    if((m=/^([^{]+)\{\s*$/.exec(s)))return `Selector <code>${esc(m[1].trim())}</code>: aturan berikut berlaku untuk elemen yang cocok.`;
    if((m=/^([^{]+)\{(.+)\}$/.exec(s)))return `Selector <code>${esc(m[1].trim())}</code> mendapat gaya: <code>${esc(m[2].trim())}</code>.`;
    if((m=/^(--[\w-]+)\s*:\s*(.+?);?$/.exec(s)))return `Variabel CSS <code>${m[1]}</code> diisi <code>${esc(m[2])}</code>.`;
    if((m=/^([\w-]+)\s*:\s*(.+?);?$/.exec(s)))return `Properti <code>${m[1]}</code> diatur ke <code>${esc(m[2])}</code>.`;
    if(s==='}')return 'Akhir blok aturan.';return ''}
  if(L==='bash'){
    const G=[[/^git init/,'Membuat repositori Git baru di folder ini.'],[/^git clone/,'Menyalin repositori dari server ke komputer.'],[/^git status/,'Melihat file yang berubah dan yang sudah di-stage.'],[/^git add/,'Memasukkan perubahan ke staging, siap di-commit.'],[/^git commit/,'Menyimpan snapshot perubahan beserta pesannya.'],[/^git push/,'Mengirim commit ke repositori remote.'],[/^git pull/,'Mengambil dan menggabungkan perubahan dari remote.'],[/^git fetch/,'Mengambil perubahan dari remote tanpa menggabungkan.'],[/^git (switch|checkout)/,'Berpindah branch (atau membuat branch baru dengan -c / -b).'],[/^git branch/,'Melihat atau membuat branch.'],[/^git merge/,'Menggabungkan branch lain ke branch aktif.'],[/^git rebase/,'Memindahkan commit ke atas branch lain.'],[/^git log/,'Melihat riwayat commit.'],[/^git diff/,'Melihat perbedaan isi file.'],[/^git restore/,'Mengembalikan file ke versi tersimpan.'],[/^git stash/,'Menyimpan sementara perubahan yang belum di-commit.'],[/^git remote/,'Mengatur alamat repositori remote.'],[/^git tag/,'Memberi label versi pada commit.'],[/^git revert/,'Membuat commit baru yang membatalkan commit lama.'],[/^git reset/,'Memindahkan HEAD; hati-hati, bisa membuang perubahan.'],[/^npm (i|install)/,'Memasang paket dari npm.'],[/^npm run/,'Menjalankan skrip di package.json.'],[/^npx/,'Menjalankan alat dari npm tanpa memasangnya permanen.'],[/^pip install/,'Memasang paket Python.'],[/^python/,'Menjalankan program Python.'],[/^javac/,'Mengompilasi kode Java menjadi bytecode.'],[/^java\b/,'Menjalankan program Java.'],[/^cd\b/,'Pindah folder.'],[/^ls\b/,'Melihat isi folder.'],[/^mkdir/,'Membuat folder.'],[/^(cat|echo)\b/,'Menampilkan teks atau isi file.'],[/^docker/,'Perintah Docker untuk container.']];
    const c=s.replace(/^\$\s*/,'');for(const [r,t] of G)if(r.test(c))return t;return s.startsWith('$')?'Perintah terminal.':'Keluaran dari perintah di atasnya.'}
  if(L==='text')return '';
  /* bahasa pemrograman umum: Java, Python, JS/TS */
  const R=[
   [/^(suspend )?((private|internal|override|public|protected|open|inline) )*fun\s+(<[^>]+>\s*)?([\w.]+)\s*\((.*?)\)?/,m=>`Mendefinisikan fungsi <code>${m[5]}</code>${m[6]?` dengan parameter <code>${esc(m[6])}</code>`:''}${m[1]?' yang bisa ditangguhkan (suspend, untuk coroutine)':''}.`],
   [/^@Composable/,()=>'<b>@Composable</b>: fungsi di bawahnya menggambar bagian UI di Jetpack Compose.'],
   [/^(private |internal )?(data |sealed |abstract |open |enum )+class\s+(\w+)/,m=>`Mendefinisikan ${m[2].trim()} class <code>${m[3]}</code>.`],
   [/^(private |internal )?(val|var)\s+(\w+)\s*(:\s*([^=]+?))?\s*(=|by)\s*(.+)$/,m=>`Membuat ${m[2]==='val'?'nilai tetap (val)':'variabel (var)'} <code>${m[3]}</code>${m[5]?` bertipe <code>${esc(m[5].trim())}</code>`:''}${m[6]==='by'?' yang didelegasikan (by)':''}.`],
   [/^(late )?(final|const)\s+(\w+(<.+>)?\??\s+)?(\w+)\s*=\s*(.+?);?$/,m=>`Membuat nilai ${m[2]==='const'?'konstan saat kompilasi (const)':'yang tidak bisa diisi ulang (final)'} <code>${m[5]}</code>.`],
   [/^(bool|num|dynamic|Widget)\s+(\w+)\s*=\s*(.+?);$/,m=>`Membuat variabel <code>${m[2]}</code> bertipe <code>${m[1]}</code>.`],
   [/^(Widget|void|Future<.+>|Stream<.+>)\s+(\w+)\s*\((.*)\)\s*(async\s*)?(\{|=>)/,m=>`Mendefinisikan fungsi <code>${m[2]}</code>${m[1]==='Widget'?' yang mengembalikan widget (tampilan)':''}${m[4]?' secara asinkron':''}.`],
   [/^setState\s*\(/,()=>'<b>setState</b>: mengubah state lalu meminta Flutter menggambar ulang widget.'],
   [/^println\s*\((.*)\)/,m=>`Menampilkan ke konsol: <code>${esc((m[1]||'').slice(0,50))}</code>.`],
   [/^(public |private |protected )?(static )?(final )?class\s+(\w+)/,m=>`Mendefinisikan class <code>${m[4]}</code>, cetak biru untuk objek.`],
   [/^(export )?(default )?interface\s+(\w+)/,m=>`Interface <code>${m[3]}</code>: kontrak bentuk data.`],
   [/^(export )?type\s+(\w+)\s*=/,m=>`Type alias <code>${m[2]}</code>: nama untuk sebuah tipe.`],
   [/^(export )?enum\s+(\w+)/,m=>`Enum <code>${m[2]}</code>: sekumpulan nilai bernama.`],
   [/^(async )?def\s+(\w+)\s*\((.*)\)/,m=>`Mendefinisikan fungsi <code>${m[2]}</code>${m[3]?` dengan parameter <code>${esc(m[3])}</code>`:''}. Isinya baru jalan saat fungsi dipanggil.`],
   [/^(export )?(default )?(async )?function\*?\s*(\w*)\s*\((.*)\)/,m=>`Mendefinisikan fungsi <code>${m[4]||'(tanpa nama)'}</code>${m[5]?` dengan parameter <code>${esc(m[5])}</code>`:''}.`],
   [/^(public |private |protected )(static )?[\w<>\[\],\s]+\s+(\w+)\s*\(.*\)\s*(throws [\w, ]+)?\s*\{?$/,m=>`Mendefinisikan method <code>${m[3]}</code>.`],
   [/^@(\w+)/,m=>`Anotasi/decorator <code>@${m[1]}</code> menambah perilaku pada baris berikutnya.`],
   [/^(import|from)\s/,()=>'Mengimpor modul atau library agar bisa dipakai.'],
   [/^package\s/,()=>'Menentukan package (folder logis) file Java ini.'],
   [/^(export )?(const|let|var)\s+\[(.+?)\]\s*=\s*useState/,m=>`Membuat state React <code>${esc(m[3])}</code>.`],
   [/^(export )?(const|let|var)\s+\{(.+?)\}\s*=/,m=>`Destructuring: mengambil <code>${esc(m[3])}</code> dari sebuah objek.`],
   [/^(export )?(const|let|var)\s+(\w+)\s*(?::\s*([^=]+))?=\s*(\(.*\)|\w+)\s*=>/,m=>`Fungsi panah disimpan di <code>${m[3]}</code>.`],
   [/^(export )?(const|let|var)\s+(\w+)\s*(?::\s*([^=]+?))?\s*=\s*(.+?);?$/,m=>`Membuat variabel <code>${m[3]}</code>${m[4]?` bertipe <code>${esc(m[4].trim())}</code>`:''} (${m[2]==='const'?'tidak bisa diisi ulang':'bisa diubah'}) berisi <code>${esc(m[5].slice(0,40))}</code>.`],
   [/^(final\s+)?(int|long|double|float|boolean|char|byte|short|String|var|[A-Z]\w*(<.+>)?(\[\])?)\s+(\w+)\s*=\s*(.+?);$/,m=>`Membuat variabel <code>${m[5]}</code> bertipe <code>${esc(m[2])}</code> berisi <code>${esc(m[6].slice(0,40))}</code>.${m[1]?' <code>final</code>: tidak bisa diubah.':''}`],
   [/^(int|long|double|float|boolean|char|String|[A-Z]\w*(<.+>)?(\[\])?)\s+(\w+);$/,m=>`Mendeklarasikan variabel <code>${m[4]}</code> bertipe <code>${esc(m[1])}</code> tanpa nilai awal.`],
   [/^(if|elif|else if)\b|^\}\s*else if\b/,()=>'<b>Percabangan</b>: blok di bawahnya hanya jalan jika kondisinya benar.'],
   [/^(else|\}\s*else)\b/,()=>'<b>else</b>: dijalankan jika semua kondisi sebelumnya salah.'],
   [/^for\b/,()=>'<b>Perulangan for</b>: blok di bawahnya diulang untuk setiap nilai.'],
   [/^while\b/,()=>'<b>Perulangan while</b>: diulang selama kondisinya benar.'],
   [/^do\b/,()=>'<b>do-while</b>: dijalankan minimal sekali, lalu diulang selama kondisi benar.'],
   [/^switch\b|^match\b/,()=>'Memilih satu cabang berdasarkan nilai.'],
   [/^(case|default)\b/,()=>'Satu pilihan cabang.'],
   [/^try\b/,()=>'<b>try</b>: mencoba kode yang mungkin gagal.'],
   [/^(\}\s*)?(catch|except)\b/,()=>'Menangani error jika terjadi di blok try.'],
   [/^(\}\s*)?finally\b/,()=>'<b>finally</b>: selalu dijalankan, error atau tidak.'],
   [/^with\b/,()=>'<b>with</b>: membuka sumber daya dan menutupnya otomatis.'],
   [/^return\b\s*(.*?);?$/,m=>m[1]?`Mengembalikan nilai <code>${esc(m[1].slice(0,40))}</code> ke pemanggil.`:'Keluar dari fungsi.'],
   [/^(break)\b/,()=>'<b>break</b>: keluar dari perulangan.'],
   [/^(continue)\b/,()=>'<b>continue</b>: lompat ke putaran berikutnya.'],
   [/^(raise|throw)\b/,()=>'Melempar error.'],
   [/^(System\.out\.print(ln|f)?|print|console\.(log|error|warn|table))\s*\((.*)\)/,m=>`Menampilkan ke layar/konsol: <code>${esc((m[4]||'').slice(0,50))}</code>.`],
   [/^(await\s+)?(\w+(\.\w+)*)\s*\((.*)\);?$/,m=>`Memanggil <code>${m[2]}()</code>${m[1]?' dan menunggu hasilnya (await)':''}.`],
   [/^(\w+(\.\w+|\[.+\])*)\s*(\+|-|\*|\/|%)?=\s*(.+?);?$/,m=>m[3]?`Mengubah <code>${m[1]}</code>: dihitung dengan operator <code>${m[3]}=</code>.`:`Mengisi <code>${esc(m[1])}</code> dengan <code>${esc(m[4].slice(0,40))}</code>.`],
   [/^(\w+)(\+\+|--);?$/,m=>`<code>${m[1]}</code> ${m[2]==='++'?'bertambah':'berkurang'} 1.`],
   [/^<\/?[A-Za-z]/,()=>'JSX: menulis tampilan seperti HTML di dalam JavaScript.'],
   [/^[}\])]+;?\)?;?$/,()=>'Penutup blok.'],
   [/^(pass)$/,()=>'<b>pass</b>: tidak melakukan apa-apa (penanda blok kosong).']];
  for(const [r,f] of R){const m=r.exec(s);if(m)return f(m)}
  return '';
}
/* susun langkah: baris kosong digabung; jalur teks melangkah per paragraf */
function caSteps(lines,lang){
  const st=[];if((CA_LBL[lang]||lang)==='text'){let a=null;lines.forEach((ln,i)=>{if(!ln.trim()){a=null;return}if(!a){a={from:i,to:i};st.push(a)}else a.to=i});return st.map(x=>({...x,note:x.from===0?'Mulai dari judul contoh.':''}))}
  lines.forEach((ln,i)=>{if(ln.trim())st.push({from:i,to:i,note:caWhat(ln,lang)})});
  /* gabungkan baris tanpa penjelasan ke langkah sebelumnya agar tidak terlalu banyak langkah */
  const out=[];st.forEach(x=>{const p=out[out.length-1];if(p&&!x.note&&p.to===x.from-1&&p.to-p.from<4)p.to=x.to;else out.push(x)});return out;
}
function caStart(pane){
  if(pane.classList.contains('ca-on'))return;
  const pre=pane.querySelector('pre.code'),lang=pane.dataset.lang||(pane.classList.contains('python')?'python':pane.classList.contains('java')?'java':'text'),lines=pre.textContent.replace(/\n$/,'').split('\n'),out=pane.querySelector('pre.out');
  const steps=caSteps(lines,lang);if(!steps.length)return;
  pane.classList.add('ca-on');
  const box=document.createElement('div');box.className='ca';
  box.innerHTML=`<pre class="code ca-pre">${lines.map((ln,i)=>`<span class="ca-ln" data-i="${i}">${hl(ln,lang)||' '}</span>`).join('')}</pre>${out?`<pre class="out ca-out" hidden>${esc(out.textContent)}</pre>`:''}
   <div class="ca-note" aria-live="polite"></div><div class="ca-ctl"><button class="btn sm" data-c="prev">◀</button><button class="btn sm primary" data-c="next">Berikutnya ▶</button><button class="btn sm" data-c="play">Putar otomatis</button><span class="ca-cnt"></span><button class="btn sm" data-c="stop">Selesai</button></div>`;
  pre.after(box);pre.hidden=true;if(out)out.hidden=true;
  let i=0,t=null;const stop=()=>{if(t){clearInterval(t);t=null}box.querySelector('[data-c=play]').textContent='Putar otomatis'};
  const show=()=>{const s=steps[i];box.querySelectorAll('.ca-ln').forEach(el=>{const k=+el.dataset.i;el.classList.toggle('shown',k<=s.to);el.classList.toggle('cur',k>=s.from&&k<=s.to);el.classList.toggle('typing',k>=s.from&&k<=s.to)});
    const last=i===steps.length-1,o=box.querySelector('.ca-out');if(o)o.hidden=!last;
    box.querySelector('.ca-note').innerHTML=(s.note||(lang==='text'?'':'Lanjutan dari baris sebelumnya.'))+(last&&o?'<br><b>Selesai.</b> Keluaran program tampil di bawah kode.':last?'<br><b>Selesai.</b>':'');
    box.querySelector('.ca-note').hidden=!box.querySelector('.ca-note').innerHTML;
    box.querySelector('.ca-cnt').textContent=`${i+1} / ${steps.length}`;box.querySelector('[data-c=prev]').disabled=i===0;box.querySelector('[data-c=next]').disabled=last;
    const c=box.querySelector('.ca-ln.cur');if(c){const p=box.querySelector('.ca-pre');const top=c.offsetTop-p.clientHeight/2;if(top>0||p.scrollTop)p.scrollTop=Math.max(0,top)}};
  box.addEventListener('click',e=>{const b=e.target.closest('[data-c]');if(!b)return;const c=b.dataset.c;
    if(c==='next'&&i<steps.length-1)i++;if(c==='prev'&&i>0)i--;
    if(c==='play'){if(t){stop();return}if(i===steps.length-1)i=0;b.textContent='Jeda';t=setInterval(()=>{if(i<steps.length-1){i++;show()}else stop()},1700);TIMERS.push(t)}
    if(c==='stop'){stop();box.remove();pre.hidden=false;if(out)out.hidden=false;pane.classList.remove('ca-on');pane.querySelector('.ca-btn').focus();return}
    if(c!=='play')stop();show()});
  show();box.querySelector('[data-c=next]').focus();
}
/* pasang tombol pada semua blok kode statis di halaman pelajaran */
function caWire(root){
  if(!root)return;root.querySelectorAll('.pane').forEach(p=>{
    const pre=p.querySelector(':scope>pre.code');if(!pre||p.querySelector('.ca-btn'))return;
    if(pre.textContent.trim().split('\n').length<2)return;
    const h=p.querySelector('.pane-h');if(!h)return;
    const b=document.createElement('button');b.className='ca-btn';b.type='button';b.textContent='▶ Animasikan';b.title='Jalankan kode baris demi baris dengan penjelasan';
    b.onclick=()=>caStart(p);const cp=h.querySelector('.copy');if(cp)cp.before(b);else h.append(b)});
}
