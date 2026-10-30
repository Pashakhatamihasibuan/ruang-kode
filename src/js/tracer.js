/* ===================== JALANKAN LANGKAH DEMI LANGKAH =====================
   Memutar ulang rekaman eksekusi (l.trc dari tools/gen/traces.py): baris yang akan dijalankan,
   isi variabel, dan keluaran sejauh ini. Bisa maju-mundur dengan tombol, slider, atau panah kiri/kanan. */
function trSteps(trc){let pv={},pf=null;return trc.s.map(([ln,fn,d,o,full])=>{
  let v;if(full||fn!==pf)v={...d};else{v={...pv,...d};(d['-']||[]).forEach(k=>delete v[k]);delete v['-']}
  const ch=Object.keys(v).filter(k=>pv[k]!==v[k]&&(fn===pf)),st={ln,fn,v,o,ch,prev:pv};pv=v;pf=fn;return st})}
const trBtn=l=>l.trc?'<button class="btn" id="trBtn" aria-expanded="false" aria-controls="trBox">👣 Langkah demi langkah</button>':'';
function tracerHTML(l,lang){
  if(!l.trc)return '';
  const lines=l.code.split('\n');
  return `<div class="trbox" id="trBox" hidden tabindex="-1" aria-label="Eksekusi langkah demi langkah">
   <div class="tr-top"><div class="tr-ctl" role="group" aria-label="Kontrol langkah"><button class="btn" data-tr="first" title="Ke awal" aria-label="Ke awal">⏮</button><button class="btn" data-tr="prev" title="Mundur (panah kiri)">◀ Mundur</button><button class="btn primary" data-tr="next" title="Maju (panah kanan)">Maju ▶</button><button class="btn" data-tr="last" title="Ke akhir" aria-label="Ke akhir">⏭</button></div>
    <input type="range" id="trRange" min="0" max="${l.trc.s.length-1}" value="0" aria-label="Pilih langkah"><span class="tr-n" id="trN"></span></div>
   <p class="tr-say" id="trSay" aria-live="polite"></p>
   <div class="tr-grid"><div class="tr-code"><pre class="code">${lines.map((s,i)=>`<span class="tr-l" data-ln="${i+1}"><i>${i+1}</i>${hl(s,lang)||' '}</span>`).join('')}</pre></div>
    <div class="tr-side"><div class="eyebrow">Variabel <span id="trFn"></span></div><table class="tr-vars" id="trVars"></table>
     <div class="eyebrow">Keluaran sejauh ini</div><pre class="tr-out" id="trOut"></pre></div></div>
   ${l.trc.cut?'<p class="muted small">Program ini panjang, jadi hanya 200 langkah pertama yang ditampilkan.</p>':''}
   <p class="muted small">Panah kuning menunjuk baris yang <b>akan</b> dijalankan berikutnya. Variabel yang baru berubah diberi warna.</p></div>`;
}
function wireTracer(l){
  const box=$('#trBox'),btn=$('#trBtn');if(!box||!btn)return;
  const S=trSteps(l.trc),fnName=f=>f==='<module>'||f==='main'?'program utama':f+'()';let i=0;
  const draw=()=>{const s=S[i];
    box.querySelectorAll('.tr-l').forEach(e=>{e.classList.toggle('on',+e.dataset.ln===s.ln)});
    const cur=box.querySelector('.tr-l.on');if(cur){const c=box.querySelector('.tr-code');const top=cur.offsetTop-c.clientHeight/2;c.scrollTop=Math.max(0,top)}
    $('#trN').textContent=`Langkah ${i+1} dari ${S.length}`;$('#trRange').value=i;
    $('#trFn').textContent=s.ln?`· di ${fnName(s.fn)}`:'';
    const ks=Object.keys(s.v);
    $('#trVars').innerHTML=ks.length?ks.map(k=>`<tr class="${s.ch.includes(k)?'chg':''}"><th>${esc(k)}</th><td>${esc(s.v[k])}</td></tr>`).join(''):'<tr><td class="muted">Belum ada variabel.</td></tr>';
    $('#trOut').textContent=l.trc.o.slice(0,s.o)||' ';
    const p=S[i-1],newOut=p&&s.o>p.o?l.trc.o.slice(p.o,s.o).trimEnd():'';
    const changes=s.ch.map(k=>s.prev[k]==null?`${k} dibuat = ${s.v[k]}`:`${k}: ${s.prev[k]} → ${s.v[k]}`);
    const main=s.fn==='<module>'||s.fn==='main',enter=p&&s.fn!==p.fn&&s.ln?(main?'Kembali ke program utama. ':`Masuk ke ${fnName(s.fn)}. `):'';
    $('#trSay').innerHTML=!s.ln?'<b>Program selesai.</b> Tekan ⏮ untuk mengulang dari awal.'
      :`${enter}${i===0?'Program dimulai. ':''}${changes.length?`<b>Berubah:</b> ${esc(changes.join(', '))}. `:''}${newOut?`<b>Tercetak:</b> <code>${esc(newOut.split('\n').pop())}</code>. `:''}Berikutnya baris ${s.ln} dijalankan.`;
    box.querySelector('[data-tr="prev"]').disabled=box.querySelector('[data-tr="first"]').disabled=i===0;
    box.querySelector('[data-tr="next"]').disabled=box.querySelector('[data-tr="last"]').disabled=i===S.length-1};
  const go=k=>{i=Math.max(0,Math.min(S.length-1,k));draw()};
  btn.onclick=()=>{const o=box.hidden;box.hidden=!o;btn.setAttribute('aria-expanded',o);if(o){go(0);box.focus({preventScroll:true});box.scrollIntoView({behavior:RM()?'auto':'smooth',block:'nearest'})}};
  box.querySelector('.tr-ctl').onclick=e=>{const b=e.target.closest('[data-tr]');if(!b)return;go({first:0,prev:i-1,next:i+1,last:S.length-1}[b.dataset.tr])};
  $('#trRange').oninput=e=>go(+e.target.value);
  box.addEventListener('keydown',e=>{if(e.target.matches('input'))return;if(e.key==='ArrowRight'){e.preventDefault();go(i+1)}else if(e.key==='ArrowLeft'){e.preventDefault();go(i-1)}});
}
