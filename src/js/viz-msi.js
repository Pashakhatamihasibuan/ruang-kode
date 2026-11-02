/* ===================== VISUAL JALUR MANAJEMEN SISTEM INFORMASI =====================
   Visual dan animasi untuk pelajaran MSI. Memakai pola umum dari viz3.js (player,
   stageViz, seqViz, seg) dan didaftarkan ke VIZ2 sehingga dipakai lewat field viz. */
const ORG4=[['perusahaan','Perusahaan'],['startup','Startup'],['sekolah','Sekolah'],['organisasi','Organisasi']];
const orgSeg=cur=>seg('Konteks',ORG4,cur||'perusahaan');
/* pasang pemilih konteks + area isi; fn(v, el) menggambar ulang */
function orgWrap(host,fn,first='perusahaan'){
  host.innerHTML=`<div class="v3-ctl">${orgSeg(first)}</div><div class="mv-body"></div>`;
  const body=$('.mv-body',host);segWire(host,'.seg',v=>fn(v,body));fn(first,body);
}

/* 1. SIM vs MSI */
function simmsiViz(host){
  const D={perusahaan:{sys:['ERP','CRM','Kasir (TPS)','Absensi'],sim:'Laporan stok & penjualan harian',mgr:'manajer cabang',msi:['Strategi: ERP mendukung ekspansi 10 cabang','Anggaran: Rp 1,2 M selama 3 tahun','Proyek: migrasi data 6 bulan','Keamanan: hak akses per gudang','SDM: pelatihan 80 staf']},
    startup:{sys:['Aplikasi pemesanan','Dasbor metrik','SaaS akuntansi','CRM ringan'],sim:'Dasbor pesanan & retensi mingguan',mgr:'founder',msi:['Strategi: bangun inti, langganan sisanya','Anggaran: biaya cloud < 8% omzet','Proyek: rilis tiap 2 minggu','Keamanan: MFA semua akun admin','SDM: satu orang pemilik data']},
    sekolah:{sys:['SIAKAD','Dapodik','Presensi','Situs sekolah'],sim:'Rekap nilai & presensi per kelas',mgr:'kepala sekolah',msi:['Strategi: rapor digital untuk orang tua','Anggaran: dana BOS untuk lisensi','Proyek: input nilai online semester ini','Keamanan: data siswa hanya untuk wali kelas','SDM: pelatihan guru 2 sesi']},
    organisasi:{sys:['Simpan pinjam','Pendataan anggota','Formulir donasi','Grup pesan'],sim:'Laporan simpanan & pinjaman bulanan',mgr:'pengurus',msi:['Strategi: transparansi untuk anggota','Anggaran: hosting Rp 150 rb/bulan','Proyek: pindah dari buku besar ke aplikasi','Keamanan: dua admin, kata sandi kuat','SDM: serah terima saat pengurus ganti']}};
  orgWrap(host,(v,el)=>{const d=D[v];
    el.innerHTML=`<div class="mv-nest"><div class="mv-outer"><span class="mv-lab">MSI · cara mengelola</span>
      <ul class="mv-acts">${d.msi.map((m,i)=>`<li style="--d:${i}">${esc(m)}</li>`).join('')}</ul>
      <div class="mv-inner"><span class="mv-lab">Sistem informasi organisasi</span>
        <div class="mv-sys">${d.sys.map(s=>`<span>${esc(s)}</span>`).join('')}<span class="sim">SIM</span></div>
        <div class="mv-flow"><b>SIM</b><i>→</i><span>${esc(d.sim)}</span><i>→</i><span>keputusan ${esc(d.mgr)}</span></div></div></div></div>
      <p class="v3-verdict">SIM adalah salah satu <b>sistem</b> di kotak dalam. MSI adalah kotak luar: semua keputusan untuk <b>mengelola</b> sistem-sistem itu.</p>`},'sekolah');
}

/* 2. Data → informasi → pengetahuan → keputusan */
function dikViz(host){
  const D={perusahaan:['4.210 struk kasir','dijumlah per produk & cabang','Produk A habis di 3 cabang sebelum 14.00','Pola sama tiap gajian','Naikkan stok minimum produk A'],
    startup:['Log klik 50.000 pengguna','dihitung per langkah daftar','40% berhenti di verifikasi KTP','Verifikasi rumit memang menurunkan konversi','Sederhanakan verifikasi'],
    sekolah:['Presensi 960 siswa','direkap per kelas','XI-4 terlambat 2x seminggu','Angkot jalur itu sering telat','Wali kelas cek jadwal angkutan'],
    organisasi:['300 formulir relawan','dikelompokkan per hari','Relawan terbanyak Sabtu pagi','Kegiatan Sabtu biasanya ramai','Pindahkan baksos ke Sabtu']};
  const S=[['Data','fakta mentah'],['Pengolahan','urut, hitung, banding'],['Informasi','bermakna'],['Pengetahuan','+ pengalaman'],['Keputusan','tindakan']];
  orgWrap(host,(v,el)=>{const d=D[v];stageViz(el,S,S.map((s,i)=>({on:[i],extra:`<code>${esc(d[i])}</code>`,note:[`<b>Data</b> mentah belum membantu siapa pun mengambil keputusan.`,`Data <b>diolah</b>: diurutkan, dijumlah, dibandingkan.`,`Hasilnya <b>informasi</b>: akurat, tepat waktu, relevan.`,`Informasi + pengalaman = <b>pengetahuan</b> tentang mengapa itu terjadi.`,`Pengetahuan menjadi <b>keputusan</b> yang bisa diukur hasilnya.`][i]})),{speed:1700})});
}

/* 3. Input-proses-output dan 6 komponen */
function ipoViz(host){
  const C=['Perangkat keras','Perangkat lunak','Data','Prosedur','Manusia','Jaringan'];
  const F=[{on:[0],c:[0,4],note:'<b>Input</b>: kasir memindai barcode dengan pemindai (perangkat keras) dan dioperasikan manusia.'},
    {on:[1],c:[1,2],note:'<b>Proses</b>: aplikasi kasir (perangkat lunak) mencari harga di data barang dan menghitung total.'},
    {on:[2],c:[0,1],note:'<b>Output</b>: struk tercetak dan stok berkurang.'},
    {on:[3],c:[2,5],note:'<b>Penyimpanan</b>: transaksi dikirim lewat jaringan ke server pusat agar bisa dipakai lagi.'},
    {on:[4],c:[3,4],note:'<b>Umpan balik</b>: manajer melihat selisih stok; prosedur stok opname diperbaiki. Tanpa prosedur dan manusia yang terlatih, teknologi saja tidak cukup.'}];
  const S=[['Input','scan barang'],['Proses','hitung total'],['Output','struk, stok'],['Simpan','server pusat'],['Umpan balik','perbaiki']];
  player(host,F,(st,f)=>{st.innerHTML=`<div class="v3-stages">${S.map((s,k)=>`<div class="v3-st ${f.on.includes(k)?'on':''}"><b>${s[0]}</b><small>${s[1]}</small></div>`).join('<span class="v3-arr" aria-hidden="true">→</span>')}</div>
    <div class="mv-comp">${C.map((c,k)=>`<span class="${f.c.includes(k)?'on':''}">${c}</span>`).join('')}</div>`},{speed:1800});
}

/* 4-5. Piramida tingkat manajemen */
function pyramidViz(host){
  const L=[['Strategis','pimpinan puncak','EIS','tidak terstruktur','5 tahun ke depan'],['Taktis','manajer menengah','MIS / DSS','semi-terstruktur','bulanan, kuartalan'],['Operasional','supervisor & staf','TPS','terstruktur','harian']];
  const D={perusahaan:['Buka 10 cabang di Sumatra?','Berapa stok tiap gudang bulan depan?','Catat 4.000 transaksi kasir hari ini'],
    startup:['Masuk kota baru atau perdalam kota lama?','Kanal promosi mana yang paling efisien?','Proses 1.200 pesanan hari ini'],
    sekolah:['Buka jurusan baru tahun depan?','Kelas mana butuh remedial semester ini?','Catat presensi 960 siswa pagi ini'],
    organisasi:['Ubah koperasi menjadi digital penuh?','Berapa batas pinjaman anggota bulan ini?','Catat setoran simpanan hari ini']};
  orgWrap(host,(v,el)=>{const fr=[2,1,0].map(i=>({i,note:`<b>${L[i][0]}</b> (${L[i][1]}): keputusan ${L[i][3]}, rentang ${L[i][4]}. Contoh: <i>${esc(D[v][i])}</i> Sistem pendukung: <b>${L[i][2]}</b>.`}));
    fr.push({i:-1,all:1,note:'Data mengalir ke atas: transaksi TPS diringkas MIS, dianalisis DSS, lalu tampil di dasbor EIS pimpinan.'});
    player(el,fr,(st,f)=>{st.innerHTML=`<svg class="mv-pyr" viewBox="0 0 320 210" role="img" aria-label="Piramida tingkat manajemen">${L.map((l,k)=>{const y=10+k*66,w1=60+k*90,w2=150+k*90;return `<g class="${f.i===k||f.all?'on':''}"><polygon points="${160-w1/2},${y} ${160+w1/2},${y} ${160+w2/2},${y+62} ${160-w2/2},${y+62}"/><text x="160" y="${y+30}">${l[0]}</text><text x="160" y="${y+48}" class="s">${l[2]}</text></g>`}).join('')}${f.all?'<path d="M300 195 L300 20" class="up"/><text x="296" y="16" class="s" text-anchor="end">data naik</text>':''}</svg>`},{speed:2000})},'sekolah');
}

/* 7. ERP, CRM, SCM: satu pesanan melewati modul */
function erpViz(host){
  seqViz(host,[['Pelanggan','toko'],['CRM','data pelanggan'],['ERP Penjualan','pesanan'],['SCM Gudang','stok & kirim'],['ERP Keuangan','faktur']],[
    {on:[0],note:'Toko Maju memesan 50 karton minyak lewat sales.'},
    {from:0,to:1,on:[0,1],label:'riwayat & limit kredit',note:'<b>CRM</b> menampilkan riwayat belanja dan limit kredit pelanggan. Sales tahu toko ini pelanggan setia.'},
    {from:1,to:2,on:[1,2],label:'buat sales order',note:'Pesanan dibuat di modul penjualan <b>ERP</b>, memakai data pelanggan yang sama (tanpa ketik ulang).'},
    {from:2,to:3,on:[2,3],label:'cek & pesan stok',note:'<b>SCM</b> memeriksa stok di gudang terdekat dan menjadwalkan truk.'},
    {from:3,to:4,on:[3,4],label:'barang terkirim',note:'Saat barang dikirim, <b>keuangan</b> otomatis membuat faktur dan piutang.'},
    {from:4,to:1,on:[1,4],label:'status bayar',note:'Status pembayaran kembali ke CRM. Satu basis data, semua bagian melihat angka yang sama.'}],{speed:1700});
}

/* 11. SDLC: waterfall vs agile */
function sdlcViz(host){
  const S=[['Rencana',''],['Analisis',''],['Desain',''],['Bangun',''],['Uji',''],['Rilis & rawat','']];
  host.innerHTML=`<div class="v3-ctl">${seg('Model',[['wf','Waterfall'],['ag','Agile']],'wf')}</div><div class="mv-body"></div>`;
  const body=$('.mv-body',host);
  const run=v=>{if(v==='wf'){stageViz(body,S,S.map((s,i)=>({on:[i],note:`Waterfall: <b>${s[0]}</b> selesai dulu sebelum tahap berikutnya. Cocok saat kebutuhan stabil, misalnya integrasi Dapodik dengan aturan yang sudah baku.${i===5?' Pengguna baru melihat hasil di akhir: perubahan kebutuhan jadi mahal.':''}`})),{speed:1300})}
    else{const fr=[];for(let sp=1;sp<=3;sp++)['Rencana','Desain','Bangun','Uji','Rilis'].forEach((x,i)=>fr.push({sp,i,note:`Sprint ${sp} (2 minggu): <b>${x}</b>.${i===4?` Rilis kecil ke pengguna: ${['pesan & bayar','status kirim','langganan'][sp-1]}. Masukan dipakai di sprint berikutnya.`:''}`}));
      player(body,fr,(st,f)=>{st.innerHTML=`<div class="mv-sprints">${[1,2,3].map(sp=>`<div class="mv-spr ${sp===f.sp?'on':''} ${sp<f.sp?'done':''}"><b>Sprint ${sp}</b><div>${['Rencana','Desain','Bangun','Uji','Rilis'].map((x,i)=>`<span class="${sp<f.sp||(sp===f.sp&&i<=f.i)?'on':''}">${x}</span>`).join('')}</div></div>`).join('')}</div>`},{speed:900})}};
  segWire(host,'.seg',run);run('wf');
}

/* 12. DFD pendaftaran siswa */
function dfdViz(host){
  seqViz(host,[['Calon siswa','entitas luar'],['1.0 Pendaftaran','proses'],['D1 Data siswa','penyimpanan'],['2.0 Verifikasi','proses'],['Bendahara','entitas luar']],[
    {on:[0],note:'DFD memakai empat simbol: <b>entitas luar</b>, <b>proses</b>, <b>penyimpanan data</b>, dan <b>aliran data</b>.'},
    {from:0,to:1,on:[0,1],label:'formulir + berkas',note:'Calon siswa mengirim formulir dan berkas.'},
    {from:1,to:2,on:[1,2],label:'data pendaftar',note:'Proses pendaftaran menyimpan data ke D1.'},
    {from:2,to:3,on:[2,3],label:'data untuk dicek',note:'Panitia memverifikasi berkas dari D1.'},
    {from:3,to:4,on:[3,4],label:'daftar lolos',note:'Daftar siswa lolos dikirim ke bendahara untuk tagihan daftar ulang.'},
    {from:3,to:0,on:[0,3],label:'pengumuman',note:'Hasil verifikasi kembali ke calon siswa. Setiap aliran data diberi nama, dan tidak ada data yang muncul tanpa sumber.'}],{speed:1700});
}

/* 13. Studi kelayakan: biaya-manfaat */
function roiViz(host){
  host.innerHTML=`<div class="v3-ctl">${rng('rB','Biaya awal (juta)',10,300,120,10)}${rng('rO','Biaya per tahun (juta)',0,100,20,5)}${rng('rM','Manfaat per tahun (juta)',0,200,70,5)}</div><div class="mv-roi"></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const B=+$('#rB',host).value,O=+$('#rO',host).value,M=+$('#rM',host).value;['rB','rO','rM'].forEach(id=>$('#'+id+'o',host).textContent=$('#'+id,host).value);
    const cum=[];let c=-B;for(let y=1;y<=5;y++){c+=M-O;cum.push(c)}const mx=Math.max(B,...cum.map(Math.abs),1),pb=cum.findIndex(x=>x>=0);
    const roi=Math.round((cum[4])/(B+O*5)*100);
    $('.mv-roi',host).innerHTML=`<div class="mv-bars"><div><i class="neg" style="height:${B/mx*50}%;top:50%"></i><small>Th 0</small></div>${cum.map((x,i)=>`<div><i class="${x>=0?'pos':'neg'}" style="height:${Math.abs(x)/mx*50}%;${x>=0?`bottom:50%`:'top:50%'}"></i><small>Th ${i+1}</small><em>${x}</em></div>`).join('')}<span class="zero"></span></div>`;
    const v=$('.v3-verdict',host);v.innerHTML=pb>=0?`Balik modal di <b>tahun ke-${pb+1}</b>. ROI 5 tahun <b>${roi}%</b>. Ingat aspek TELOS lain: teknis, hukum, operasional, dan jadwal.`:`Belum balik modal dalam 5 tahun (ROI ${roi}%). Kecilkan biaya awal, pilih SaaS, atau cari manfaat yang lebih besar.`;v.classList.toggle('ok',pb>=0)};
  host.addEventListener('input',draw);draw();
}

/* 14. Cloud: siapa mengelola apa */
function cloudViz(host){
  const L=['Aplikasi','Data','Runtime','Sistem operasi','Server & penyimpanan','Gedung & listrik'];
  const M={onprem:[0,0,0,0,0,0],iaas:[0,0,0,0,1,1],paas:[0,0,1,1,1,1],saas:[1,0,1,1,1,1]};
  const N={onprem:'<b>On-premise</b>: semua milik dan urusan organisasi. Contoh: server SIAKAD di ruang TU sekolah.',iaas:'<b>IaaS</b>: sewa server virtual. Contoh: startup menyewa VM untuk aplikasi pesanan.',paas:'<b>PaaS</b>: cukup unggah kode. Contoh: tim kecil memakai platform hosting aplikasi.',saas:'<b>SaaS</b>: langsung pakai aplikasinya. Contoh: koperasi memakai aplikasi akuntansi langganan. Data tetap tanggung jawabmu.'};
  host.innerHTML=`<div class="v3-ctl">${seg('Model',[['onprem','On-premise'],['iaas','IaaS'],['paas','PaaS'],['saas','SaaS']],'onprem')}</div><div class="mv-stack"></div><p class="v3-verdict"></p>`;
  const draw=v=>{$('.mv-stack',host).innerHTML=L.map((l,i)=>`<div class="${M[v][i]?'vendor':'own'}"><span>${l}</span><small>${M[v][i]?'penyedia':'organisasi'}</small></div>`).join('');$('.v3-verdict',host).innerHTML=N[v]};
  segWire(host,'.seg',draw);draw('onprem');
}

/* 15. Keamanan: kendali vs ancaman */
function ciaViz(host){
  const K=[['mfa','MFA'],['enk','Enkripsi'],['bak','Backup 3-2-1'],['akses','Hak akses minimum'],['log','Log audit']];
  const T=[['Kata sandi admin bocor','C',['mfa']],['Laptop bendahara hilang','C',['enk']],['Ransomware mengunci server','A',['bak']],['Staf magang mengubah nilai','I',['akses','log']],['Server mati saat rapor dibagikan','A',['bak']],['Data pelanggan disadap di Wi-Fi publik','C',['enk']]];
  host.innerHTML=`<div class="mv-chk">${K.map(([k,n])=>`<label><input type="checkbox" value="${k}"> ${n}</label>`).join('')}</div><ul class="mv-threats"></ul><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const on=[...host.querySelectorAll('input:checked')].map(x=>x.value);let n=0;
    $('.mv-threats',host).innerHTML=T.map(([t,c,need])=>{const ok=need.every(x=>on.includes(x));n+=ok;return `<li class="${ok?'ok':'bad'}"><span class="cia">${c}</span>${t}<b>${ok?'✓ tertangani':'✗ berisiko'}</b></li>`}).join('');
    const v=$('.v3-verdict',host);v.innerHTML=`${n} dari ${T.length} ancaman tertangani. C = kerahasiaan, I = integritas, A = ketersediaan.${n===T.length?' Lengkap: keamanan butuh beberapa lapis kendali sekaligus.':''}`;v.classList.toggle('ok',n===T.length)};
  host.addEventListener('change',draw);draw();
}

/* 16. Backup 3-2-1 vs bencana */
function backupViz(host){
  const C=[['asli','Server kantor','lokal'],['nas','NAS di kantor','lokal'],['usb','Hard disk di lemari','lokal'],['cloud','Cloud (offsite)','luar']];
  const E=[['ransom','Ransomware',['asli','nas']],['api','Kebakaran kantor',['asli','nas','usb']],['rusak','Server rusak',['asli']]];
  host.innerHTML=`<p class="small muted">Pilih salinan yang dimiliki, lalu uji dengan bencana.</p><div class="mv-chk">${C.map(([k,n],i)=>`<label><input type="checkbox" value="${k}" ${i===0?'checked disabled':''}> ${n}</label>`).join('')}</div><div class="v3-ctl">${seg('Bencana',E.map(e=>[e[0],e[1]]),'')}</div><div class="mv-copies"></div><p class="v3-verdict" aria-live="polite"></p>`;
  let ev='';const draw=()=>{const on=[...host.querySelectorAll('input:checked')].map(x=>x.value),hit=ev?E.find(e=>e[0]===ev)[2]:[];
    $('.mv-copies',host).innerHTML=C.filter(c=>on.includes(c[0])).map(c=>`<span class="${hit.includes(c[0])?'lost':'safe'}">${c[1]}<small>${hit.includes(c[0])?'hilang':'aman'}</small></span>`).join('');
    const survive=on.filter(c=>!hit.includes(c)).length,r321=on.length>=3&&on.includes('cloud');
    const v=$('.v3-verdict',host);v.innerHTML=(ev?(survive?`Data selamat (${survive} salinan tersisa). `:'<b>Semua salinan hilang.</b> ')
      :'')+(r321?'Aturan 3-2-1 terpenuhi: 3 salinan, 2 media, 1 di luar lokasi.':'Belum 3-2-1: butuh 3 salinan dan 1 di luar lokasi.');v.classList.toggle('ok',!!(ev?survive:r321))};
  host.addEventListener('change',draw);segWire(host,'.seg',v=>{ev=v;draw()});draw();
}

/* 18. Balanced scorecard */
function bscViz(host){
  const P=['Keuangan','Pelanggan','Proses internal','Belajar & tumbuh'];
  const D={perusahaan:['Margin naik 2%','Keluhan kirim < 1%','Pesanan diproses < 4 jam','80% staf lulus pelatihan ERP'],
    startup:['Biaya akuisisi < Rp 40 rb','Retensi bulan-1 > 35%','Rilis tiap 2 minggu','Setiap fitur diuji 5 pengguna'],
    sekolah:['Dana BOS terserap 100%','Kepuasan orang tua > 4/5','Rapor terbit H+3 ujian','Semua guru mahir SIAKAD'],
    organisasi:['Kas tercatat 100%','Anggota aktif naik 20%','Laporan RAT tepat waktu','Pengurus baru terlatih 1 bulan']};
  orgWrap(host,(v,el)=>{el.innerHTML=`<div class="mv-bsc">${P.map((p,i)=>`<div style="--d:${i}"><small>${p}</small><b>${esc(D[v][i])}</b></div>`).join('')}<span class="mid">Visi &amp; strategi</span></div><p class="v3-verdict">Empat sudut pandang saling terhubung: orang yang terlatih memperbaiki proses, proses yang baik memuaskan pelanggan, pelanggan puas memperbaiki keuangan.</p>`});
}

/* 19. Segitiga proyek */
function triangleViz(host){
  host.innerHTML=`<div class="v3-ctl">${rng('tS','Lingkup (jumlah fitur)',2,20,8)}${rng('tW','Waktu (minggu)',2,24,8)}${rng('tT','Anggota tim',1,8,3)}</div><div class="mv-tri"></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const s=+$('#tS',host).value,w=+$('#tW',host).value,t=+$('#tT',host).value;['tS','tW','tT'].forEach(id=>$('#'+id+'o',host).textContent=$('#'+id,host).value);
    const cap=w*t/3,ratio=s/cap,biaya=w*t*12;
    $('.mv-tri',host).innerHTML=`<div class="mv-meter"><span>Beban kerja vs kapasitas</span><div><i class="${ratio>1.15?'bad':ratio>0.95?'warn':'ok'}" style="width:${Math.min(100,ratio*60)}%"></i></div><small>${Math.round(ratio*100)}% · biaya ±Rp ${biaya} juta</small></div>`;
    const v=$('.v3-verdict',host);v.innerHTML=ratio>1.15?'Terlalu ambisius: <b>kualitas</b> akan dikorbankan. Kurangi lingkup (MVP), tambah waktu, atau tambah tim (dengan biaya).':ratio>0.95?'Ketat. Siapkan cadangan waktu dan prioritas fitur (MoSCoW).':'Realistis. Lingkup, waktu, dan biaya seimbang.';v.classList.toggle('ok',ratio<=0.95)};
  host.addEventListener('input',draw);draw();
}

/* 20-23. Studi kasus: sebelum dan sesudah */
function caseViz(host,o={}){
  const t=(o.lesson&&o.lesson.t)||'';
  const C=/perusahaan/i.test(t)?{s:[['Sales','order'],['ERP','satu data'],['Gudang','ambil barang'],['Kirim','truk'],['Faktur','otomatis'],['Dasbor','direksi']],b:'Pesanan lewat telepon, ditulis ulang 3 kali, stok di Excel tiap gudang.',a:'Satu pesanan masuk sekali, semua bagian melihat stok yang sama.',k:['Salah kirim 6% → 1%','Tutup buku 10 → 3 hari']}
    :/startup/i.test(t)?{s:[['Pelanggan','pesan'],['Aplikasi','pesanan'],['QRIS','bayar'],['Dapur','siapkan'],['Kurir','antar'],['Dasbor','metrik']],b:'Pesanan via chat dan spreadsheet; sering salah porsi dan alamat.',a:'Pesanan terstruktur, pembayaran tercatat otomatis.',k:['Salah kirim 5% → 1,4%','Waktu admin 4 → 1 jam/hari']}
    :/sekolah/i.test(t)?{s:[['Guru','input nilai'],['SIAKAD','olah'],['Wali kelas','cek'],['Rapor','digital'],['Orang tua','lihat'],['Dapodik','sinkron']],b:'Nilai di kertas dan file terpisah; rapor terlambat 2 minggu.',a:'Nilai masuk sekali, rapor dan laporan ke Dapodik dari data yang sama.',k:['Rapor H+14 → H+3','Rekap presensi otomatis']}
    :{s:[['Anggota','setor'],['Bendahara','catat'],['Aplikasi','simpan pinjam'],['Anggota','cek saldo'],['Pengurus','laporan'],['RAT','transparan']],b:'Buku besar tulisan tangan; anggota tidak bisa cek saldo.',a:'Setiap anggota melihat simpanan dan pinjamannya sendiri.',k:['Laporan RAT siap H-7','Selisih kas mendekati 0']};
  const fr=[{on:[],before:1,note:'<b>Sebelum</b>: '+C.b}].concat(C.s.map((s,i)=>({on:[i],note:`<b>${s[0]}</b>: ${s[1]}.`})),[{on:C.s.map((_,i)=>i),after:1,note:'<b>Sesudah</b>: '+C.a}]);
  player(host,fr,(st,f)=>{st.innerHTML=`<div class="v3-stages">${C.s.map((s,k)=>`<div class="v3-st ${f.on.includes(k)?'on':''} ${f.before?'skip':''}"><b>${s[0]}</b><small>${s[1]}</small></div>`).join('<span class="v3-arr" aria-hidden="true">→</span>')}</div>${f.after?`<div class="mv-kpi">${C.k.map(k=>`<span>${k}</span>`).join('')}</div>`:''}`},{speed:1400});
}

/* 27. MSI dan UX: diagram Venn bertahap */
function rolesViz(host){
  const I=[['m','Anggaran & ROI'],['m','Keamanan data'],['m','Integrasi sistem'],['u','Riset pengguna'],['u','Alur & wireframe'],['u','Uji kegunaan'],['b','Kebutuhan'],['b','Prioritas'],['b','KPI sukses']];
  const fr=I.map((x,i)=>({n:i+1,note:`<b>${x[1]}</b>: ${x[0]==='m'?'tanggung jawab pengelola SI (MSI)':x[0]==='u'?'tanggung jawab UX Designer':'dikerjakan <b>bersama</b>, di sinilah keduanya bertemu'}.`}));
  player(host,fr,(st,f)=>{const pos={m:[82,0],u:[278,0],b:[180,0]},cnt={m:0,u:0,b:0};
    st.innerHTML=`<svg class="mv-venn" viewBox="0 0 360 210" role="img" aria-label="Peran MSI dan UX"><circle cx="125" cy="105" r="100" class="m"/><circle cx="235" cy="105" r="100" class="u"/><text x="70" y="20" class="h">MSI</text><text x="290" y="20" class="h">UX</text>${I.slice(0,f.n).map((x,i)=>{const y=72+cnt[x[0]]++*28;return `<text x="${pos[x[0]][0]}" y="${y}" class="${i===f.n-1?'cur':''}">${x[1]}</text>`}).join('')}</svg>`},{speed:1500});
}

/* 28. Alur aplikasi baru */
function newappViz(host){
  const S=[['Masalah','MSI+UX'],['Riset','UX'],['Kelayakan','MSI'],['Kebutuhan','MSI+UX'],['Rancang','UX+MSI'],['Prototipe & uji','UX'],['Bangun MVP','dev'],['Uji','QA'],['Rilis','MSI'],['Ukur','MSI+UX']];
  const N=['Tetapkan masalah dan target terukur: salah kirim di bawah 2%.','Wawancara 8 pelanggan dan 3 kurir.','TELOS dan biaya-manfaat: bangun sendiri atau langganan SaaS?','User story, aturan data, dan persetujuan UU PDP.','User flow, wireframe, ERD, arsitektur.','Prototipe diuji 5 pengguna. <b>Gerbang</b>: lanjut atau perbaiki desain dulu.','Bangun fitur inti saja dulu.','Uji fungsi, keamanan, WCAG 2.2 AA, HP murah. <b>Gerbang</b>: siap rilis?','Pelatihan, migrasi data, rilis bertahap.','Bandingkan dengan target di langkah 1, lalu putuskan fitur berikutnya.'];
  player(host,S.map((s,i)=>({i,note:`<b>${i+1}. ${s[0]}</b> (${s[1]}): ${N[i]}`})),(st,f)=>{st.innerHTML=`<ol class="mv-steps">${S.map((s,k)=>`<li class="${k===f.i?'on':''} ${k<f.i?'done':''} ${k===5||k===7?'gate':''}"><b>${s[0]}</b><small>${s[1]}</small></li>`).join('')}</ol>`},{speed:1500});
}

/* 29. Audit dan prioritas perbaikan aplikasi lama */
function auditViz(host){
  const F=[['pw','Password disimpan polos','OWASP A02',5,2],['bak','Tidak ada backup','BCP 3-2-1',5,2],['cap','Login hanya captcha gambar','WCAG 3.3.8',4,2],['lambat','Halaman nilai 9 detik di 3G','Performa',4,3],['kontras','Kontras teks 2.8:1','WCAG 1.4.3',3,1],['tombol','Tombol 16px di ponsel','WCAG 2.5.8',3,1],['ikon','Ikon terlihat kuno','Estetika',1,3]];
  const done=new Set();
  host.innerHTML=`<div class="mv-audit"><svg class="mv-mx" viewBox="0 0 220 220" role="img" aria-label="Matriks dampak dan usaha"></svg><ul class="mv-find"></ul></div><div class="mv-meter"><span>Skor kepatuhan standar</span><div><i class="ok"></i></div><small></small></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const X=e=>20+(e-0.5)*62,Y=d=>185-(d-1)*36;
    $('.mv-mx',host).innerHTML=`<rect x="20" y="10" width="200" height="200" class="bg"/><line x1="120" y1="10" x2="120" y2="210"/><line x1="20" y1="110" x2="220" y2="110"/><text x="70" y="24" class="q">kerjakan dulu</text><text x="170" y="24" class="q">rencanakan</text><text x="70" y="206" class="q">sambil lalu</text><text x="170" y="206" class="q">tunda</text><text x="6" y="110" class="ax" transform="rotate(-90 6 110)">dampak →</text><text x="120" y="219" class="ax">usaha →</text>${F.map(([k,,,d,e],i)=>`<circle cx="${X(e)+(i%3)*16-8}" cy="${Y(d)}" r="7" class="${done.has(k)?'fixed':d>=5?'crit':'open'}"/>`).join('')}`;
    const sorted=[...F].sort((a,b)=>(b[3]-a[3])||(a[4]-b[4]));
    $('.mv-find',host).innerHTML=sorted.map(([k,n,s,d])=>`<li class="${done.has(k)?'fixed':''}"><span><b>${n}</b><small>${s} · dampak ${d}</small></span><button class="btn sm" data-k="${k}" ${done.has(k)?'disabled':''}>${done.has(k)?'Selesai':'Perbaiki'}</button></li>`).join('');
    const tot=F.reduce((a,f)=>a+f[3],0),got=F.filter(f=>done.has(f[0])).reduce((a,f)=>a+f[3],0),p=Math.round(30+got/tot*70);
    $('.mv-meter i',host).style.width=p+'%';$('.mv-meter small',host).textContent=p+'%';
    const next=sorted.find(f=>!done.has(f[0]));const v=$('.v3-verdict',host);
    v.innerHTML=next?`Daftar sudah diurutkan: keamanan dan hukum dulu, lalu dampak terbesar per usaha. Berikutnya: <b>${next[1]}</b>.`:'Semua temuan selesai. Langkah terakhir: <b>ukur ulang</b> dengan metrik yang sama seperti saat audit.';v.classList.toggle('ok',!next)};
  host.addEventListener('click',e=>{const b=e.target.closest('[data-k]');if(b){done.add(b.dataset.k);draw()}});draw();
}

Object.assign(VIZ2,{simmsi:simmsiViz,dik:dikViz,ipo:ipoViz,pyramid:pyramidViz,erp:erpViz,sdlc:sdlcViz,dfd:dfdViz,roi:roiViz,cloud:cloudViz,cia:ciaViz,backup:backupViz,bsc:bscViz,triangle:triangleViz,mcase:caseViz,roles:rolesViz,newapp:newappViz,audit:auditViz});
Object.assign(VIZ2T,{simmsi:'SIM di dalam MSI',dik:'Dari data menjadi keputusan',ipo:'Input, proses, output, dan komponennya',pyramid:'Piramida tingkat manajemen',erp:'Satu pesanan melewati ERP, CRM, dan SCM',sdlc:'Waterfall lawan Agile',dfd:'Diagram aliran data (DFD)',roi:'Kalkulator biaya-manfaat',cloud:'Siapa mengelola apa di cloud',cia:'Kendali keamanan lawan ancaman',backup:'Uji cadangan 3-2-1',bsc:'Balanced scorecard',triangle:'Segitiga proyek',mcase:'Sebelum dan sesudah sistem',roles:'Peran MSI dan UX Designer',newapp:'Alur membuat aplikasi baru',audit:'Audit dan prioritas perbaikan'});

/* SIM: empat jenis laporan dari data yang sama */
function reportsViz(host){
  const D=[['Jakarta','Budi',42,5],['Jakarta','Sari',38,22],['Bandung','Dewi',27,3],['Bandung','Eko',31,18],['Medan','Fitri',19,2],['Medan','Gita',24,15]];
  const rp=n=>'Rp '+n+' jt';
  host.innerHTML=`<div class="v3-ctl">${seg('Jenis laporan',[['jad','Terjadwal'],['adh','Sesuai permintaan'],['exc','Pengecualian'],['dd','Drill-down']],'jad')}</div><div class="mv-rep"></div><p class="v3-verdict" aria-live="polite"></p>`;
  let open='';
  const draw=v=>{const el=$('.mv-rep',host),vd=$('.v3-verdict',host);let h='';
    const cab=[...new Set(D.map(r=>r[0]))].map(c=>[c,D.filter(r=>r[0]===c).reduce((a,r)=>a+r[2],0),D.filter(r=>r[0]===c).reduce((a,r)=>a+r[3],0)]);
    if(v==='jad'){h=`<table class="lt"><caption>Penjualan mingguan per cabang · terbit tiap Senin 07.00</caption><thead><tr><th>Cabang</th><th>Omzet</th><th>Stok tersisa</th></tr></thead><tbody>${cab.map(c=>`<tr><th>${c[0]}</th><td>${rp(c[1])}</td><td>${c[2]} karton</td></tr>`).join('')}</tbody></table>`;vd.innerHTML='<b>Terjadwal</b>: format sama, waktu sama, untuk pemantauan rutin.'}
    if(v==='adh'){h=`<p class="mv-q">❓ "Kasir mana yang omzetnya di atas Rp 30 jt minggu ini?"</p><table class="lt"><thead><tr><th>Kasir</th><th>Cabang</th><th>Omzet</th></tr></thead><tbody>${D.filter(r=>r[2]>30).map(r=>`<tr><th>${r[1]}</th><td>${r[0]}</td><td>${rp(r[2])}</td></tr>`).join('')}</tbody></table>`;vd.innerHTML='<b>Sesuai permintaan</b>: dibuat saat manajer punya pertanyaan khusus.'}
    if(v==='exc'){h=`<table class="lt"><caption>Hanya stok di bawah minimum (10 karton)</caption><thead><tr><th>Cabang</th><th>Pos kasir</th><th>Stok</th></tr></thead><tbody>${D.filter(r=>r[3]<10).map(r=>`<tr class="mv-bad"><th>${r[0]}</th><td>${r[1]}</td><td>${r[3]} karton ⚠</td></tr>`).join('')}</tbody></table>`;vd.innerHTML=`<b>Pengecualian</b>: dari ${D.length} baris, hanya ${D.filter(r=>r[3]<10).length} yang butuh tindakan.`}
    if(v==='dd'){const tot=D.reduce((a,r)=>a+r[2],0);h=`<div class="mv-dd"><button class="mv-ddb" data-c="">Total nasional: ${rp(tot)}</button>${cab.map(c=>`<div><button class="mv-ddb" data-c="${c[0]}" aria-expanded="${open===c[0]}">${open===c[0]?'▾':'▸'} ${c[0]}: ${rp(c[1])}</button>${open===c[0]?`<ul>${D.filter(r=>r[0]===c[0]).map(r=>`<li>${r[1]}: ${rp(r[2])}</li>`).join('')}</ul>`:''}</div>`).join('')}</div>`;vd.innerHTML='<b>Drill-down</b>: klik cabang untuk merinci sampai ke kasir.'}
    el.innerHTML=h};
  let cur='jad';segWire(host,'.seg',v=>{cur=v;draw(v)});
  host.addEventListener('click',e=>{const b=e.target.closest('.mv-ddb');if(b&&b.dataset.c){open=open===b.dataset.c?'':b.dataset.c;draw('dd')}});draw('jad');
}
/* SIM: model keberhasilan DeLone & McLean */
function deloneViz(host){
  const K=[['sys','Kualitas sistem'],['inf','Kualitas informasi'],['svc','Kualitas layanan']];
  host.innerHTML=`<div class="v3-ctl">${rng('dlS','Kualitas sistem',1,5,2)}${rng('dlI','Kualitas informasi',1,5,3)}${rng('dlV','Kualitas layanan',1,5,3)}</div><div class="mv-dl"></div><p class="v3-verdict" aria-live="polite"></p>`;
  const draw=()=>{const a=+$('#dlS',host).value,b=+$('#dlI',host).value,c=+$('#dlV',host).value;['dlS','dlI','dlV'].forEach(id=>$('#'+id+'o',host).textContent=$('#'+id,host).value);
    const use=Math.min(5,(a*0.45+b*0.35+c*0.2)),sat=Math.min(5,(a*0.3+b*0.4+c*0.3)),net=Math.min(5,(use*0.5+sat*0.5));
    const bar=(n,v)=>`<div class="mv-dlb"><span>${n}</span><div><i class="${v>=3.5?'ok':v>=2.5?'warn':'bad'}" style="width:${v/5*100}%"></i></div><b>${v.toFixed(1)}</b></div>`;
    $('.mv-dl',host).innerHTML=`<div class="mv-dlc"><small>Penyebab</small>${bar('Sistem',a)}${bar('Informasi',b)}${bar('Layanan',c)}</div><span class="v3-arr" aria-hidden="true">→</span><div class="mv-dlc"><small>Akibat</small>${bar('Penggunaan',use)}${bar('Kepuasan',sat)}</div><span class="v3-arr" aria-hidden="true">→</span><div class="mv-dlc"><small>Hasil</small>${bar('Manfaat bersih',net)}</div>`;
    const v=$('.v3-verdict',host),low=K[[a,b,c].indexOf(Math.min(a,b,c))][1];v.innerHTML=net>=3.5?'SIM berhasil: dipakai, disukai, dan memberi manfaat nyata.':`Manfaat belum terasa. Perbaiki dulu dimensi terlemah: <b>${low}</b>. Contoh: SIAKAD yang lambat membuat guru kembali ke spreadsheet.`;v.classList.toggle('ok',net>=3.5)};
  host.addEventListener('input',draw);draw();
}
Object.assign(VIZ2,{reports:reportsViz,delone:deloneViz});
Object.assign(VIZ2T,{reports:'Empat jenis laporan SIM',delone:'Model keberhasilan DeLone & McLean'});

/* ===== berpikir sistem dan problem solving ===== */
function icebergViz(host){
  const D={perusahaan:['Pesanan salah kirim minggu ini','Naik setiap akhir bulan','Stok di Excel tiap gudang, tidak sinkron','"Yang penting barang keluar dulu"'],
    startup:['Banyak pengguna berhenti','Selalu di langkah verifikasi','Verifikasi 6 langkah, server lambat','"Fitur baru lebih penting dari kemudahan"'],
    sekolah:['Rapor terlambat','Setiap akhir semester','Nilai dikirim via file berbeda, diketik ulang','"Sistem itu urusan operator"'],
    organisasi:['Laporan RAT terlambat','Setiap tahun','Catatan di buku, bendahara sendirian','"Pengurus lama pasti ingat"']};
  const L=[['Kejadian','apa yang terlihat','Reaksi: memadamkan api'],['Pola','apa yang berulang','Antisipasi'],['Struktur','apa yang menyebabkan','Rancang ulang proses & sistem'],['Pola pikir','keyakinan di baliknya','Ubah cara pandang']];
  orgWrap(host,(v,el)=>{const fr=L.map((l,i)=>({i,note:`<b>${l[0]}</b> (${l[1]}): <i>${esc(D[v][i])}</i>. Tindakan di lapisan ini: ${l[2]}.${i===3?' Semakin dalam lapisannya, semakin besar dan tahan lama dampak solusinya.':''}`}));
    player(el,fr,(st,f)=>{st.innerHTML=`<svg class="mv-ice" viewBox="0 0 340 250" role="img" aria-label="Model gunung es"><rect x="0" y="62" width="340" height="188" class="sea"/><line x1="0" y1="62" x2="340" y2="62" class="wl"/><text x="6" y="76" class="s" text-anchor="start">permukaan air</text>
      ${L.map((l,k)=>{const y=[14,70,128,186][k],h=[48,54,54,58][k],w=[90,170,240,300][k];return `<g class="${k<=f.i?'on':''} ${k===f.i?'cur':''}"><path d="M${170-w/2+ (k?0:20)},${y+h} L${170-w/2+(k?0:30)},${y} L${170+w/2-(k?0:30)},${y} L${170+w/2-(k?0:20)},${y+h} Z"/><text x="170" y="${y+22}">${l[0]}</text><text x="170" y="${y+38}" class="s">${k<=f.i?esc(D[v][k].length>34?D[v][k].slice(0,33)+'…':D[v][k]):'?'}</text></g>`}).join('')}</svg>`},{speed:2200})},'sekolah');
}
function lensViz(host){
  const P=[['Guru','Pengguna','Harus < 1 menit per kelas'],['Orang tua','Pengguna','Kabar saat anak tidak hadir'],['Kepala sekolah','Manajemen','Alpa tanpa keterangan turun'],['Tata usaha','Proses','Rekap bulanan tidak perlu lagi'],['Guru BK','Data','Lihat siswa berisiko saja'],['Tim TI','Teknologi','Ringan di Android murah'],['Bendahara','Keuangan','Rp 3 jt/th, hemat 40 jam/bln'],['Siswa tanpa HP','Hukum & etika','Tetap tercatat, data dilindungi']];
  host.innerHTML=`<p class="small muted">Masalah: <b>membuat aplikasi presensi sekolah</b>. Klik setiap pemangku kepentingan untuk menyalakan lensanya.</p><div class="mv-lens"><div class="mv-lc">Aplikasi presensi<small>0 / ${P.length} lensa</small></div>${P.map((p,i)=>`<button class="mv-lp" data-i="${i}" style="--a:${i/P.length}" aria-pressed="false"><b>${p[0]}</b><small>${p[1]}</small></button>`).join('')}</div><ul class="mv-lfind"></ul><p class="v3-verdict" aria-live="polite"></p>`;
  const on=new Set();const draw=()=>{host.querySelectorAll('.mv-lp').forEach(b=>b.setAttribute('aria-pressed',on.has(+b.dataset.i)));$('.mv-lc small',host).textContent=`${on.size} / ${P.length} lensa`;
    $('.mv-lfind',host).innerHTML=[...on].map(i=>`<li><b>${P[i][0]}</b> · ${P[i][1]}: ${P[i][2]}</li>`).join('');
    const v=$('.v3-verdict',host);v.innerHTML=on.size===P.length?'Gambaran utuh: keputusan sekarang bisa dijelaskan dari semua sudut pandang.':on.size?`Masih ${P.length-on.size} sudut pandang yang belum dilihat. Solusi dari sebagian lensa berisiko gagal di lensa lain.`:'Belum ada sudut pandang. Mulai dari siapa saja.';v.classList.toggle('ok',on.size===P.length)};
  host.addEventListener('click',e=>{const b=e.target.closest('.mv-lp');if(b){const i=+b.dataset.i;on.has(i)?on.delete(i):on.add(i);draw()}});draw();
}
function whysViz(host){
  const W=[['Pesanan salah kirim','gejala'],['Kotak tertukar saat diambil kurir',''],['Label ditulis tangan dan mirip',''],['Admin menyalin pesanan dari chat',''],['Tidak ada formulir pesanan terstruktur',''],['Proses tidak pernah ditinjau saat bisnis tumbuh','akar']];
  const F=[['Orang','Guru belum terlatih input online'],['Proses','Nilai lewat 3 tahap kirim file'],['Data','Format nilai beda tiap guru'],['Teknologi','Server lambat di jam sibuk'],['Kebijakan','Batas input tidak jelas'],['Lingkungan','Sinyal lemah di ruang guru']];
  host.innerHTML=`<div class="v3-ctl">${seg('Alat',[['why','5 Why'],['fish','Tulang ikan']],'why')}</div><div class="mv-body"></div>`;const body=$('.mv-body',host);
  const run=v=>{if(v==='why'){player(body,W.map((w,i)=>({i,note:i===0?'Mulai dari <b>gejala</b> yang terlihat. Tanyakan: <b>mengapa?</b>':i===W.length-1?'<b>Akar masalah</b> ditemukan: sesuatu yang bisa diperbaiki. Solusi: formulir pesanan + label cetak otomatis, bukan sekadar menegur kurir.':`Mengapa? → ${esc(w[0])}.`})),(st,f)=>{st.innerHTML=`<ol class="mv-why">${W.slice(0,f.i+1).map((w,k)=>`<li class="${w[1]} ${k===f.i?'cur':''}">${k?'<span class="q">Mengapa?</span>':''}<b>${esc(w[0])}</b>${w[1]?`<small>${w[1]}</small>`:''}</li>`).join('')}</ol>`},{speed:1600})}
    else{player(body,F.map((x,i)=>({i,note:`Kategori <b>${x[0]}</b>: ${x[1]}.${i===F.length-1?' Semua tulang terisi: penyebab ternyata ada di banyak kategori, bukan hanya teknologi.':''}`})),(st,f)=>{st.innerHTML=`<svg class="mv-fish" viewBox="0 0 360 200" role="img" aria-label="Diagram tulang ikan rapor terlambat"><line x1="20" y1="100" x2="290" y2="100" class="sp"/><polygon points="290,82 340,100 290,118" class="hd"/><text x="315" y="96" class="hdt">Rapor</text><text x="315" y="108" class="hdt">telat</text>
      ${F.map((x,k)=>{const top=k%2===0,col=Math.floor(k/2),xx=70+col*85,y2=top?28:172;return `<g class="${k<=f.i?'on':''} ${k===f.i?'cur':''}"><line x1="${xx}" y1="${y2}" x2="${xx+30}" y2="100"/><text x="${xx}" y="${top?20:190}" class="cat">${x[0]}</text>${k<=f.i?`<text x="${xx+18}" y="${top?62:142}" class="c">${esc(x[1].length>22?x[1].slice(0,21)+'…':x[1])}</text>`:''}</g>`}).join('')}</svg>`},{speed:1500})}};
  segWire(host,'.seg',run);run('why');
}
function loopViz(host){
  const N=[['Data lengkap',170,30],['Laporan berguna',272,110],['Guru rajin input',170,190],['Aplikasi cepat',68,110]];
  host.innerHTML=`<div class="v3-ctl">${seg('Arah',[['up','Lingkaran baik'],['down','Lingkaran buruk']],'up')}</div><div class="mv-body"></div>`;const body=$('.mv-body',host);
  const run=v=>{const good=v==='up',lab=good?['Data lengkap ↑','Laporan berguna ↑','Guru rajin input ↑','Aplikasi cepat ↑']:['Data bolong ↓','Laporan tak dipercaya ↓','Guru pakai kertas ↓','Aplikasi lambat ↓'];
    const fr=[];for(let lap=1;lap<=2;lap++)[3,0,1,2].forEach((k,j)=>fr.push({k,lap,note:`${lap===2&&j===0?'Putaran kedua, efeknya makin besar. ':''}<b>${lab[k]}</b>${j<3?' menyebabkan langkah berikutnya.':' kembali memengaruhi awal lingkaran.'}${lap===2&&j===3?(good?' <b>Titik ungkit</b>: buat aplikasinya cepat dan satu laporan yang benar-benar membantu guru.':' Untuk memutusnya, perbaiki titik paling awal: kecepatan aplikasi.'):''}`}));
    player(body,fr,(st,f)=>{st.innerHTML=`<svg class="mv-loop ${good?'g':'b'}" viewBox="0 0 340 220" role="img" aria-label="Lingkaran sebab-akibat"><circle cx="170" cy="110" r="72" class="ring"/><text x="170" y="106" class="mid">${good?'R+':'R−'}</text><text x="170" y="122" class="ms">putaran ${f.lap}</text>${N.map((n,k)=>`<g class="${k===f.k?'cur':''}"><rect x="${n[1]-60}" y="${n[2]-16}" width="120" height="32" rx="10"/><text x="${n[1]}" y="${n[2]+4}">${lab[k]}</text></g>`).join('')}</svg>`},{speed:1400})};
  segWire(host,'.seg',run);run('up');
}
function holisticViz(host){
  const S=[['Keluhan','"Kami butuh aplikasi baru"'],['Definisi','60% anggota ragu saldo; RAT 6 jam'],['Gunung es','Struktur: buku tunggal, satu bendahara'],['Lensa','Lansia tanpa HP pintar; dinas butuh laporan baku'],['5 Why','Akar: tidak ada transparansi rutin'],['Alternatif','Aplikasi lengkap · Spreadsheet + slip cetak · Papan pengumuman'],['Keputusan','Spreadsheet + slip cetak (dampak tinggi, biaya rendah)'],['Efek samping','Slip berisi data pribadi → amplop tertutup'],['Ukur ulang','Survei kepercayaan + durasi RAT berikutnya']];
  player(host,S.map((s,i)=>({i,note:`<b>${s[0]}</b>: ${s[1]}.${i===0?' Pemikir sepotong-sepotong langsung membeli aplikasi. Pemikir sistem bertanya dulu.':''}${i===S.length-1?' Solusinya ternyata gabungan proses dan teknologi sederhana.':''}`})),(st,f)=>{st.innerHTML=`<ol class="mv-steps mv-hol">${S.map((s,k)=>`<li class="${k===f.i?'on':''} ${k<f.i?'done':''}"><b>${s[0]}</b><small>${k<=f.i?esc(s[1]):'…'}</small></li>`).join('')}</ol>`},{speed:1800});
}
Object.assign(VIZ2,{iceberg:icebergViz,lens:lensViz,whys:whysViz,loop:loopViz,holistic:holisticViz});
Object.assign(VIZ2T,{iceberg:'Model gunung es',lens:'Lensa pemangku kepentingan',whys:'5 Why dan diagram tulang ikan',loop:'Lingkaran sebab-akibat',holistic:'Berpikir utuh, langkah demi langkah'});
