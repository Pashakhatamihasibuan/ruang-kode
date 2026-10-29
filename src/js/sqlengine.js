/* ===================== MESIN SQL =====================
   Simulator SQL kecil untuk belajar: dialek mirip SQLite/PostgreSQL, data di memori.
   Selain hasil, mesin ini merekam jejak tiap tahap (FROM, WHERE, GROUP BY, ...) untuk visualisasi. */
const SQLE=(()=>{
class SqlError extends Error{constructor(msg,hint){super(msg);this.hint=hint||''}}
const lc=s=>String(s).toLowerCase();

/* ---------- tokenizer ---------- */
function tokenize(src){
  const T=[];let i=0;const n=src.length;
  while(i<n){
    const c=src[i];
    if(/\s/.test(c)){i++;continue}
    if(c==='-'&&src[i+1]==='-'){while(i<n&&src[i]!=='\n')i++;continue}
    if(c==='/'&&src[i+1]==='*'){const j=src.indexOf('*/',i+2);i=j<0?n:j+2;continue}
    const p=i;
    if(/[0-9]/.test(c)||(c==='.'&&/[0-9]/.test(src[i+1]||''))){
      let j=i;while(j<n&&/[0-9]/.test(src[j]))j++;
      if(src[j]==='.'){j++;while(j<n&&/[0-9]/.test(src[j]))j++}
      if(/[eE]/.test(src[j]||'')&&/[-+0-9]/.test(src[j+1]||'')){j+=2;while(j<n&&/[0-9]/.test(src[j]))j++}
      T.push({t:'num',v:Number(src.slice(i,j)),p});i=j;continue}
    if(c==="'"){let j=i+1,s='';
      for(;;){if(j>=n)throw new SqlError("Teks belum ditutup: tanda kutip ' tidak berpasangan.","Setiap teks diapit dua kutip tunggal, misalnya 'Jakarta'.");
        if(src[j]==="'"){if(src[j+1]==="'"){s+="'";j+=2;continue}break}s+=src[j++]}
      T.push({t:'str',v:s,p});i=j+1;continue}
    if(c==='"'||c==='`'||c==='['){const cl=c==='['?']':c,j=src.indexOf(cl,i+1);
      if(j<0)throw new SqlError(`Nama berkutip ${c} belum ditutup.`);T.push({t:'id',v:src.slice(i+1,j),q:1,p});i=j+1;continue}
    if(/[A-Za-z_]/.test(c)){let j=i;while(j<n&&/[A-Za-z0-9_]/.test(src[j]))j++;const w=src.slice(i,j);T.push({t:'id',v:w,u:w.toUpperCase(),p});i=j;continue}
    const two=src.substr(i,2);
    if(['<=','>=','<>','!=','==','||'].includes(two)){T.push({t:'op',v:two,p});i+=2;continue}
    if('(),.;=<>+-*/%'.includes(c)){T.push({t:'op',v:c,p});i++;continue}
    throw new SqlError(`Karakter tidak dikenal: ${c}`,'Periksa tanda baca. Teks memakai kutip tunggal, bukan kutip miring.');
  }
  T.push({t:'eof',v:'',p:n});return T;
}

/* kata yang tidak boleh dianggap alias */
const RES=new Set('SELECT FROM WHERE GROUP BY HAVING ORDER LIMIT OFFSET JOIN INNER LEFT RIGHT FULL OUTER CROSS NATURAL ON USING AS AND OR NOT UNION ALL INTERSECT EXCEPT INTO VALUES SET WINDOW CASE WHEN THEN ELSE END ASC DESC IS NULL IN LIKE BETWEEN DISTINCT EXISTS'.split(' '));
const KWLIST='SELECT FROM WHERE GROUP BY HAVING ORDER LIMIT OFFSET JOIN INNER LEFT RIGHT FULL OUTER CROSS ON AS AND OR NOT UNION INSERT INTO VALUES UPDATE SET DELETE CREATE TABLE ALTER DROP TRUNCATE VIEW INDEX DISTINCT BETWEEN LIKE NULL PRIMARY KEY FOREIGN REFERENCES UNIQUE CHECK DEFAULT BEGIN COMMIT ROLLBACK SAVEPOINT CASE WHEN THEN ELSE END WITH RECURSIVE OVER PARTITION'.split(' ');
function lev(a,b){const d=[...Array(b.length+1).keys()];for(let i=1;i<=a.length;i++){let p=d[0];d[0]=i;for(let j=1;j<=b.length;j++){const t=d[j];d[j]=Math.min(d[j]+1,d[j-1]+1,p+(a[i-1]===b[j-1]?0:1));p=t}}return d[b.length]}
function guessKw(w){if(!w)return null;const u=w.toUpperCase();if(KWLIST.includes(u))return null;let best=null,bd=3;
  for(const k of KWLIST){const d=lev(u,k);if(d<bd&&k.length>2){bd=d;best=k}}return bd<=(u.length>=4?2:1)?best:null}

/* ---------- parser ---------- */
class Parser{
  constructor(src){this.src=src;this.T=tokenize(src);this.i=0}
  get pk(){return this.T[this.i]}
  la(k=1){return this.T[this.i+k]}
  next(){return this.T[this.i++]}
  isKw(...w){const t=this.pk;return t.t==='id'&&!t.q&&w.includes(t.u)}
  kw(...w){if(this.isKw(...w))return this.next().u;return null}
  needKw(w,ctx){if(!this.kw(w))this.fail(`Diharapkan ${w}${ctx?' '+ctx:''}`);}
  isOp(o){const t=this.pk;return t.t==='op'&&t.v===o}
  op(o){if(this.isOp(o)){this.i++;return true}return false}
  needOp(o,ctx){if(!this.op(o))this.fail(`Diharapkan tanda ${o}${ctx?' '+ctx:''}`)}
  fail(msg){const t=this.pk;const near=t.t==='eof'?'akhir perintah':`"${t.t==='str'?"'"+t.v+"'":t.v}"`;
    const g=t.t==='id'?guessKw(t.v):null;
    throw new SqlError(`${msg}, tetapi yang ditemukan ${near}.`,g?`Mungkin maksudmu ${g}?`:'')}
  ident(what='nama'){const t=this.pk;if(t.t!=='id')this.fail(`Diharapkan ${what}`);this.i++;return t.v}
  identList(){const a=[this.ident()];while(this.op(','))a.push(this.ident());return a}
  all(){const out=[];
    while(this.pk.t!=='eof'){if(this.op(';'))continue;const st=this.statement();out.push(st);
      if(!this.op(';')&&this.pk.t!=='eof')this.fail('Perintah seharusnya selesai di sini (pisahkan dengan titik koma ;)')}
    return out}
  statement(){
    const start=this.pk.p,st=this.stmt0();st.sql=this.src.slice(start,this.pk.p).trim();return st}
  stmt0(){
    if(this.kw('EXPLAIN')){if(this.kw('QUERY'))this.needKw('PLAN');return {type:'explain',q:this.select()}}
    if(this.isKw('SELECT','WITH')||this.isOp('('))return this.select();
    const t=this.pk;
    switch(t.t==='id'?t.u:''){
      case 'INSERT':return this.insert();
      case 'UPDATE':return this.update();
      case 'DELETE':return this.del();
      case 'CREATE':return this.create();
      case 'ALTER':return this.alter();
      case 'DROP':return this.drop();
      case 'TRUNCATE':this.next();this.kw('TABLE');return {type:'truncate',name:this.ident('nama tabel')};
      case 'BEGIN':case 'START':this.next();this.kw('TRANSACTION','WORK');return {type:'begin'};
      case 'COMMIT':case 'END':this.next();this.kw('TRANSACTION','WORK');return {type:'commit'};
      case 'ROLLBACK':{this.next();this.kw('TRANSACTION','WORK');if(this.kw('TO')){this.kw('SAVEPOINT');return {type:'rollback',to:this.ident()}}return {type:'rollback'}}
      case 'SAVEPOINT':this.next();return {type:'savepoint',name:this.ident()};
      case 'RELEASE':this.next();this.kw('SAVEPOINT');return {type:'release',name:this.ident()};
      case 'GRANT':case 'REVOKE':return this.grant();
    }
    const g=t.t==='id'?guessKw(t.v):null;
    throw new SqlError(`Perintah tidak dikenali: "${t.v}".`,g?`Mungkin maksudmu ${g}?`:'Perintah SQL biasanya dimulai dengan SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, atau DROP.');
  }
  /* SELECT */
  select(){
    let ctes=null;
    if(this.kw('WITH')){const rec=!!this.kw('RECURSIVE');ctes=[];
      do{const name=this.ident('nama CTE');let cols=null;if(this.op('(')){cols=this.identList();this.needOp(')')}
        this.needKw('AS','setelah nama CTE');this.needOp('(');const q=this.select();this.needOp(')');ctes.push({name,cols,q,rec})}while(this.op(','))}
    let body=this.core();
    while(this.isKw('UNION','INTERSECT','EXCEPT')){let o=this.next().u;if(o==='UNION'&&this.kw('ALL'))o='UNION ALL';else this.kw('DISTINCT');
      body={type:'compound',op:o,l:body,r:this.core()}}
    let order=null,limit=null,offset=null;
    if(this.kw('ORDER')){this.needKw('BY','setelah ORDER');order=this.orderList()}
    if(this.kw('LIMIT')){limit=this.expr();if(this.kw('OFFSET'))offset=this.expr();else if(this.op(',')){offset=limit;limit=this.expr()}}
    else if(this.kw('OFFSET')){offset=this.expr();this.kw('ROWS','ROW');if(this.kw('FETCH')){this.kw('FIRST','NEXT');limit=this.expr();this.kw('ROWS','ROW');this.needKw('ONLY')}}
    else if(this.kw('FETCH')){this.kw('FIRST','NEXT');limit=this.expr();this.kw('ROWS','ROW');this.needKw('ONLY')}
    return {type:'select',ctes,body,order,limit,offset};
  }
  orderList(){const a=[];do{const e=this.expr();let desc=false;if(this.kw('DESC'))desc=true;else this.kw('ASC');
      let nulls=null;if(this.kw('NULLS')){nulls=this.kw('FIRST','LAST')}a.push({e,desc,nulls})}while(this.op(','));return a}
  core(){
    if(this.op('(')){const q=this.select();this.needOp(')');return {type:'paren',q}}
    if(this.kw('VALUES')){const rows=[];do{this.needOp('(');rows.push(this.exprList());this.needOp(')')}while(this.op(','));return {type:'values',rows}}
    if(!this.kw('SELECT'))this.fail('Diharapkan SELECT');
    const distinct=!!this.kw('DISTINCT');this.kw('ALL');
    if(this.kw('TOP')){this._top=this.primary()}
    const cols=[];
    do{
      if(this.op('*')){cols.push({star:true});continue}
      if(this.pk.t==='id'&&this.la().t==='op'&&this.la().v==='.'&&this.la(2).t==='op'&&this.la(2).v==='*'){const tb=this.next().v;this.i+=2;cols.push({star:true,table:tb});continue}
      const s=this.pk.p,e=this.expr(),txt=this.src.slice(s,this.pk.p).trim();let alias=null;
      if(this.kw('AS'))alias=this.pk.t==='str'?this.next().v:this.ident('alias');
      else if(this.pk.t==='id'&&(this.pk.q||!RES.has(this.pk.u))&&!this.isKw('FROM'))alias=this.next().v;
      cols.push({e,alias,txt});
    }while(this.op(','));
    if(this.isKw('FORM','FRM','FRON','FOM'))this.fail('Diharapkan FROM atau koma');
    let from=null,where=null,group=null,having=null;
    if(this.kw('FROM'))from=this.from();
    if(this.kw('WHERE'))where=this.expr();
    if(this.kw('GROUP')){this.needKw('BY','setelah GROUP');group=this.exprList()}
    if(this.kw('HAVING'))having=this.expr();
    const top=this._top;this._top=null;
    return {type:'core',distinct,cols,from,where,group,having,top};
  }
  fromItem(){
    if(this.op('(')){
      if(this.isKw('SELECT','WITH','VALUES')){const q=this.select();this.needOp(')');return {kind:'sub',q,alias:this.alias()}}
      const f=this.from();this.needOp(')');return f}
    const name=this.ident('nama tabel');return {kind:'table',name,alias:this.alias()}
  }
  alias(){if(this.kw('AS'))return this.ident('alias');
    if(this.pk.t==='id'&&(this.pk.q||!RES.has(this.pk.u))&&!this.isKw('WHERE','GROUP','ORDER','LIMIT','HAVING','ON','USING','JOIN','INNER','LEFT','RIGHT','FULL','CROSS','UNION','EXCEPT','INTERSECT','SET','OFFSET','FETCH','NATURAL'))return this.next().v;
    return null}
  from(){
    let L=this.fromItem();
    for(;;){
      if(this.op(',')){L={kind:'join',jt:'CROSS',comma:true,l:L,r:this.fromItem()};continue}
      let jt=null;
      if(this.kw('JOIN'))jt='INNER';
      else if(this.kw('INNER')){this.needKw('JOIN','setelah INNER');jt='INNER'}
      else if(this.isKw('LEFT','RIGHT','FULL')){jt=this.next().u;this.kw('OUTER');this.needKw('JOIN',`setelah ${jt}`)}
      else if(this.kw('CROSS')){this.needKw('JOIN','setelah CROSS');jt='CROSS'}
      else break;
      const R=this.fromItem();let on=null,using=null;
      if(this.kw('ON'))on=this.expr();else if(this.kw('USING')){this.needOp('(');using=this.identList();this.needOp(')')}
      else if(jt!=='CROSS')this.fail(`${jt} JOIN perlu kondisi ON, misalnya ON a.id = b.a_id`);
      L={kind:'join',jt,l:L,r:R,on,using};
    }
    return L;
  }
  /* ekspresi */
  exprList(){const a=[this.expr()];while(this.op(','))a.push(this.expr());return a}
  expr(){return this.or()}
  or(){let l=this.and();while(this.kw('OR'))l={op:'OR',l,r:this.and()};return l}
  and(){let l=this.not();while(this.kw('AND'))l={op:'AND',l,r:this.not()};return l}
  not(){if(this.kw('NOT'))return {op:'NOT',e:this.not()};return this.cmp()}
  cmp(){
    let l=this.cat();
    for(;;){
      const t=this.pk;
      if(t.t==='op'&&['=','==','!=','<>','<','<=','>','>='].includes(t.v)){this.i++;
        const o=t.v==='=='?'=':t.v==='<>'?'!=':t.v;
        if(this.isKw('ANY','ALL','SOME')){const q=this.next().u;this.needOp('(');const s=this.select();this.needOp(')');l={op:'quant',o,q:q==='SOME'?'ANY':q,e:l,s};continue}
        l={op:'cmp',o,l,r:this.cat()};continue}
      if(this.kw('IS')){const not=!!this.kw('NOT');if(this.kw('NULL')){l={op:'isnull',e:l,not};continue}
        if(this.kw('DISTINCT')){this.needKw('FROM');l={op:'is',l,r:this.cat(),not:!not};continue}
        l={op:'is',l,r:this.cat(),not};continue}
      if(this.kw('ISNULL')){l={op:'isnull',e:l,not:false};continue}
      if(this.kw('NOTNULL')){l={op:'isnull',e:l,not:true};continue}
      const save=this.i,not=!!this.kw('NOT');
      if(this.kw('IN')){this.needOp('(','setelah IN');
        if(this.isKw('SELECT','WITH')){const q=this.select();this.needOp(')');l={op:'in',e:l,q,not}}
        else{const list=this.isOp(')')?[]:this.exprList();this.needOp(')');l={op:'in',e:l,list,not}}continue}
      if(this.kw('LIKE','ILIKE')){const p=this.cat();let esc=null;if(this.kw('ESCAPE'))esc=this.cat();l={op:'like',e:l,p,not,esc};continue}
      if(this.kw('BETWEEN')){const a=this.cat();this.needKw('AND','di BETWEEN ... AND ...');l={op:'between',e:l,a,b:this.cat(),not};continue}
      if(not)this.i=save;
      break;
    }
    return l;
  }
  cat(){let l=this.add();while(this.op('||'))l={op:'bin',o:'||',l,r:this.add()};return l}
  add(){let l=this.mul();for(;;){if(this.op('+'))l={op:'bin',o:'+',l,r:this.mul()};else if(this.op('-'))l={op:'bin',o:'-',l,r:this.mul()};else return l}}
  mul(){let l=this.un();for(;;){const t=this.pk;if(t.t==='op'&&'*/%'.includes(t.v)&&t.v.length===1){this.i++;l={op:'bin',o:t.v,l,r:this.un()}}else return l}}
  un(){if(this.op('-'))return {op:'neg',e:this.un()};if(this.op('+'))return this.un();return this.primary()}
  primary(){
    const t=this.pk;
    if(t.t==='num'){this.i++;return {op:'lit',v:t.v}}
    if(t.t==='str'){this.i++;return {op:'lit',v:t.v}}
    if(this.op('(')){
      if(this.isKw('SELECT','WITH')){const q=this.select();this.needOp(')');return {op:'sub',q}}
      const e=this.expr();
      if(this.op(',')){const list=[e,...this.exprList()];this.needOp(')');return {op:'row',list}}
      this.needOp(')');return e}
    if(t.t!=='id'){if(t.t==='eof')this.fail('Perintah berhenti di tengah jalan: masih kurang ekspresi');this.fail('Diharapkan nilai, nama kolom, atau fungsi')}
    if(!t.q){
      switch(t.u){
        case 'NULL':this.i++;return {op:'lit',v:null};
        case 'TRUE':this.i++;return {op:'lit',v:1};
        case 'FALSE':this.i++;return {op:'lit',v:0};
        case 'CURRENT_DATE':case 'CURRENT_TIMESTAMP':case 'CURRENT_TIME':this.i++;return {op:'fn',name:t.u,args:[]};
        case 'CASE':return this.caseExpr();
        case 'CAST':{this.i++;this.needOp('(');const e=this.expr();this.needKw('AS');const ty=this.typeName();this.needOp(')');return {op:'cast',e,ty}}
        case 'EXISTS':{this.i++;this.needOp('(');const q=this.select();this.needOp(')');return {op:'exists',q}}
        case 'EXTRACT':if(this.la().v==='('){this.i+=2;const part=this.ident();this.needKw('FROM');const e=this.expr();this.needOp(')');return {op:'fn',name:'DATEPART',args:[{op:'lit',v:lc(part)},e]}}break;
        case 'INTERVAL':break;
      }
    }
    this.i++;
    if(this.isOp('(')&&!t.q){
      this.i++;const name=t.u;let args=[],star=false,distinct=false;
      if(this.op('*')){star=true}
      else if(!this.isOp(')')){
        distinct=!!this.kw('DISTINCT');
        if(['DATEADD','DATEPART','DATEDIFF','DATE_PART','DATETRUNC','DATE_TRUNC'].includes(name)&&this.pk.t==='id'&&!this.pk.q&&this.la().v===','){args.push({op:'lit',v:lc(this.next().v)});this.needOp(',')}
        args.push(...this.exprList());
        if(name==='STRING_AGG'||name==='GROUP_CONCAT'){if(this.kw('ORDER')){this.needKw('BY');this.orderList()}}
      }
      this.needOp(')',`untuk menutup ${name}(`);
      const f={op:'fn',name,args,star,distinct};
      if(this.kw('FILTER')){this.needOp('(');this.needKw('WHERE');f.filter=this.expr();this.needOp(')')}
      if(this.kw('OVER'))f.over=this.overSpec();
      return f;
    }
    if(this.op('.')){
      if(this.pk.t!=='id')this.fail('Diharapkan nama kolom setelah titik');
      return {op:'col',table:t.v,name:this.next().v}}
    return {op:'col',name:t.v,q:t.q}
  }
  overSpec(){
    this.needOp('(','setelah OVER');const w={part:null,order:null,frame:null};
    if(this.kw('PARTITION')){this.needKw('BY');w.part=this.exprList()}
    if(this.kw('ORDER')){this.needKw('BY');w.order=this.orderList()}
    if(this.isKw('ROWS','RANGE')){const k=this.next().u;let depth=0;const s=this.i;while(!(depth===0&&this.isOp(')'))){if(this.pk.t==='eof')this.fail('Diharapkan )');if(this.isOp('('))depth++;if(this.isOp(')'))depth--;this.i++}
      const txt=this.T.slice(s,this.i).map(x=>String(x.v).toUpperCase()).join(' ');
      w.frame=k+' '+txt}
    this.needOp(')');return w}
  caseExpr(){this.i++;let base=null;if(!this.isKw('WHEN'))base=this.expr();const whens=[];
    while(this.kw('WHEN')){const c=this.expr();this.needKw('THEN','setelah WHEN');whens.push([c,this.expr()])}
    if(!whens.length)this.fail('CASE butuh minimal satu WHEN ... THEN ...');
    let els=null;if(this.kw('ELSE'))els=this.expr();this.needKw('END','untuk menutup CASE');return {op:'case',base,whens,els}}
  typeName(){let ty=this.ident('tipe data');while(this.pk.t==='id'&&['VARYING','PRECISION'].includes(this.pk.u))ty+=' '+this.next().v;
    if(this.op('(')){ty+='('+this.next().v;while(this.op(','))ty+=','+this.next().v;this.needOp(')');ty+=')'}return ty}
  /* DML */
  insert(){this.next();this.kw('OR')&&this.next();this.needKw('INTO','setelah INSERT');const name=this.ident('nama tabel');let cols=null;
    if(this.isOp('(')&&!(this.la().t==='id'&&['SELECT','WITH'].includes(this.la().u))){this.i++;cols=this.identList();this.needOp(')')}
    if(this.kw('DEFAULT')){this.needKw('VALUES');return {type:'insert',name,cols,rows:[[]]}}
    if(this.kw('VALUES')){const rows=[];do{this.needOp('(','sebelum daftar nilai');rows.push(this.exprList());this.needOp(')','setelah daftar nilai')}while(this.op(','));
      return {type:'insert',name,cols,rows}}
    if(this.isKw('SELECT','WITH')||this.isOp('('))return {type:'insert',name,cols,q:this.select()};
    this.fail('Diharapkan VALUES atau SELECT');}
  update(){this.next();const name=this.ident('nama tabel');const alias=this.alias();this.needKw('SET','setelah nama tabel');const sets=[];
    do{const c=this.ident('nama kolom');this.needOp('=','setelah nama kolom di SET');sets.push([c,this.expr()])}while(this.op(','));
    let where=null;if(this.kw('WHERE'))where=this.expr();return {type:'update',name,alias,sets,where}}
  del(){this.next();this.needKw('FROM','setelah DELETE');const name=this.ident('nama tabel');const alias=this.alias();let where=null;if(this.kw('WHERE'))where=this.expr();return {type:'delete',name,alias,where}}
  /* DDL */
  create(){this.next();
    let replace=false,unique=false,temp=false;
    if(this.kw('OR')){this.needKw('REPLACE');replace=true}
    if(this.kw('TEMP','TEMPORARY'))temp=true;
    if(this.kw('UNIQUE'))unique=true;
    if(this.kw('TABLE')){let ine=false;if(this.kw('IF')){this.needKw('NOT');this.needKw('EXISTS');ine=true}
      const name=this.ident('nama tabel');
      if(this.kw('AS'))return {type:'createas',name,q:this.select(),ine};
      this.needOp('(','setelah nama tabel');const cols=[],cons=[];
      do{
        if(this.isKw('PRIMARY','FOREIGN','UNIQUE','CHECK','CONSTRAINT')){cons.push(this.tableCons());continue}
        cols.push(this.colDef());
      }while(this.op(','));
      this.needOp(')','untuk menutup daftar kolom');return {type:'create',name,cols,cons,ine}}
    if(this.kw('VIEW')){let ine=false;if(this.kw('IF')){this.needKw('NOT');this.needKw('EXISTS');ine=true}
      const name=this.ident('nama view');let cols=null;if(this.op('(')){cols=this.identList();this.needOp(')')}this.needKw('AS');const s=this.pk.p;const q=this.select();
      return {type:'view',name,q,replace,cols,ine,body:this.src.slice(s,this.pk.p).trim()}}
    if(this.kw('INDEX')){let ine=false;if(this.kw('IF')){this.needKw('NOT');this.needKw('EXISTS');ine=true}
      const name=this.ident('nama index');this.needKw('ON');const table=this.ident('nama tabel');this.needOp('(');const cols=[];
      do{cols.push(this.ident('nama kolom'));this.kw('ASC','DESC')}while(this.op(','));this.needOp(')');return {type:'index',name,table,cols,unique,ine}}
    if(this.isKw('PROCEDURE','FUNCTION','TRIGGER'))throw new SqlError(`CREATE ${this.pk.u} tidak didukung di simulator ini.`,'Simulator memakai dialek mirip SQLite yang tidak punya stored procedure. Baca contoh sintaks MySQL/PostgreSQL di materi, lalu coba di database sungguhan.');
    this.fail('Diharapkan TABLE, VIEW, atau INDEX setelah CREATE')}
  colDef(){const c={name:this.ident('nama kolom'),type:''};
    if(this.pk.t==='id'&&!['PRIMARY','NOT','NULL','UNIQUE','DEFAULT','CHECK','REFERENCES','CONSTRAINT','AUTOINCREMENT','AUTO_INCREMENT','GENERATED'].includes(this.pk.u))c.type=this.typeName();
    for(;;){
      if(this.kw('CONSTRAINT')){this.ident();continue}
      if(this.kw('PRIMARY')){this.needKw('KEY');this.kw('ASC','DESC');c.pk=true;if(this.kw('AUTOINCREMENT','AUTO_INCREMENT'))c.auto=true;continue}
      if(this.kw('AUTOINCREMENT','AUTO_INCREMENT')){c.auto=true;continue}
      if(this.kw('NOT')){this.needKw('NULL');c.nn=true;continue}
      if(this.kw('NULL'))continue;
      if(this.kw('UNIQUE')){c.unique=true;continue}
      if(this.kw('DEFAULT')){c.def=this.isOp('(')?(this.i++,(e=>(this.needOp(')'),e))(this.expr())):this.un();continue}
      if(this.kw('CHECK')){this.needOp('(');const s=this.pk.p;c.check=this.expr();c.checkTxt=this.src.slice(s,this.pk.p).trim();this.needOp(')');continue}
      if(this.kw('REFERENCES')){c.ref=this.refClause();continue}
      break;
    }
    return c}
  refClause(){const table=this.ident('nama tabel rujukan');let cols=null;if(this.op('(')){cols=this.identList();this.needOp(')')}
    let onDelete=null,onUpdate=null;
    while(this.kw('ON')){const w=this.kw('DELETE','UPDATE');let a;if(this.kw('CASCADE'))a='CASCADE';else if(this.kw('SET')){a=this.kw('NULL','DEFAULT')==='NULL'?'SET NULL':'SET DEFAULT'}else if(this.kw('RESTRICT'))a='RESTRICT';else{this.needKw('NO');this.needKw('ACTION');a='NO ACTION'}
      if(w==='DELETE')onDelete=a;else onUpdate=a}
    return {table,cols,onDelete,onUpdate}}
  tableCons(){let cname=null;if(this.kw('CONSTRAINT'))cname=this.ident();
    if(this.kw('PRIMARY')){this.needKw('KEY');this.needOp('(');const cols=this.identList();this.needOp(')');return {k:'pk',cols,cname}}
    if(this.kw('UNIQUE')){this.needOp('(');const cols=this.identList();this.needOp(')');return {k:'unique',cols,cname}}
    if(this.kw('CHECK')){this.needOp('(');const e=this.expr();this.needOp(')');return {k:'check',e,cname}}
    if(this.kw('FOREIGN')){this.needKw('KEY');this.needOp('(');const cols=this.identList();this.needOp(')');this.needKw('REFERENCES');return {k:'fk',cols,ref:this.refClause(),cname}}
    this.fail('Diharapkan PRIMARY KEY, FOREIGN KEY, UNIQUE, atau CHECK')}
  alter(){this.next();if(this.kw('VIEW'))throw new SqlError('ALTER VIEW tidak didukung.','Untuk mengubah view, pakai CREATE OR REPLACE VIEW nama AS SELECT ...');
    this.needKw('TABLE','setelah ALTER');const name=this.ident('nama tabel');
    if(this.kw('ADD')){if(this.isKw('CONSTRAINT','PRIMARY','FOREIGN','UNIQUE','CHECK'))return {type:'alter',name,act:'addcons',cons:this.tableCons()};this.kw('COLUMN');return {type:'alter',name,act:'add',col:this.colDef()}}
    if(this.kw('DROP')){this.kw('COLUMN');return {type:'alter',name,act:'drop',col:this.ident('nama kolom')}}
    if(this.kw('RENAME')){if(this.kw('TO'))return {type:'alter',name,act:'rename',to:this.ident()};this.kw('COLUMN');const a=this.ident();this.needKw('TO');return {type:'alter',name,act:'renamecol',from:a,to:this.ident()}}
    if(this.kw('ALTER','MODIFY')){this.kw('COLUMN');const c=this.ident();this.kw('TYPE');this.kw('SET','DATA')&&this.kw('TYPE');const ty=this.typeName();return {type:'alter',name,act:'type',col:c,ty}}
    this.fail('Diharapkan ADD, DROP, RENAME, atau ALTER COLUMN')}
  drop(){this.next();const k=this.kw('TABLE','VIEW','INDEX');if(!k)this.fail('Diharapkan TABLE, VIEW, atau INDEX setelah DROP');
    let ie=false;if(this.kw('IF')){this.needKw('EXISTS');ie=true}const name=this.ident();this.kw('CASCADE','RESTRICT');return {type:'drop',k,name,ie}}
  grant(){const g=this.next().u;const privs=[];
    do{let p=this.ident('hak akses').toUpperCase();if(p==='ALL')this.kw('PRIVILEGES');privs.push(p)}while(this.op(','));
    this.needKw('ON');this.kw('TABLE');const obj=this.ident('nama tabel');
    if(g==='GRANT')this.needKw('TO');else this.needKw('FROM');const who=this.ident('nama pengguna');
    return {type:'grant',g,privs,obj,who}}
}

/* ---------- nilai & perbandingan ---------- */
const isNum=v=>typeof v==='number';
const numish=s=>typeof s==='string'&&/^\s*[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?\s*$/.test(s);
function toNum(v){if(v==null)return null;if(isNum(v))return v;if(numish(v))return Number(v);const m=/^\s*[-+]?\d+(\.\d+)?/.exec(v);return m?Number(m[0]):0}
function cmpv(a,b){
  if(isNum(a)&&isNum(b))return a-b;
  if(isNum(a))return numish(b)?a-Number(b):-1;
  if(isNum(b))return numish(a)?Number(a)-b:1;
  return a<b?-1:a>b?1:0;
}
function truth(v){if(v==null)return null;if(isNum(v))return v!==0;return toNum(v)!==0}
const B=x=>x==null?null:(x?1:0);
function sortKey(a,b){if(a==null&&b==null)return 0;if(a==null)return -1;if(b==null)return 1;return cmpv(a,b)}
const keyOf=arr=>JSON.stringify(arr.map(v=>v==null?null:isNum(v)?v:'s'+v));
function affinity(type,v){
  if(v==null)return null;const t=(type||'').toUpperCase();
  if(/INT/.test(t)){if(numish(v)){const n=Number(v);return n}return v}
  if(/REAL|FLOA|DOUB|NUM|DEC/.test(t)){return numish(v)?Number(v):v}
  if(/CHAR|CLOB|TEXT|DATE|TIME/.test(t)){return isNum(v)?String(v):v}
  if(/BOOL/.test(t)){if(typeof v==='string'&&/^(true|false)$/i.test(v))return /^t/i.test(v)?1:0;return v}
  return v;
}
function likeRe(p,esc){let s='^';for(let i=0;i<p.length;i++){const c=p[i];if(esc&&c===esc){s+=p[++i].replace(/[.*+?^${}()|[\]\\]/g,'\\$&');continue}
  if(c==='%')s+='[\\s\\S]*';else if(c==='_')s+='[\\s\\S]';else s+=c.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}return new RegExp(s+'$','i')}

/* ---------- tanggal ---------- */
const pad=(n,w=2)=>String(n).padStart(w,'0');
function pdate(v){if(v==null)return null;if(v==='now'){return new Date()}
  const m=/^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}):(\d{2})(?::(\d{2}))?)?/.exec(String(v));if(!m)return null;
  return new Date(Date.UTC(+m[1],+m[2]-1,+m[3],+(m[4]||0),+(m[5]||0),+(m[6]||0)))}
const fdate=d=>`${d.getUTCFullYear()}-${pad(d.getUTCMonth()+1)}-${pad(d.getUTCDate())}`;
const ftime=d=>`${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}:${pad(d.getUTCSeconds())}`;
function nowUTC(){const n=new Date();return new Date(Date.UTC(n.getFullYear(),n.getMonth(),n.getDate(),n.getHours(),n.getMinutes(),n.getSeconds()))}
function addPart(d,part,n){d=new Date(d.getTime());part=lc(part).replace(/s$/,'');
  const map={year:'FullYear',yy:'FullYear',yyyy:'FullYear',month:'Month',mm:'Month',m:'Month',day:'Date',dd:'Date',d:'Date',hour:'Hours',hh:'Hours',minute:'Minutes',mi:'Minutes',second:'Seconds',ss:'Seconds'};
  if(part==='week'||part==='wk'){d.setUTCDate(d.getUTCDate()+7*n);return d}
  const k=map[part];if(!k)throw new SqlError(`Bagian tanggal tidak dikenal: ${part}`,'Gunakan year, month, day, hour, minute, atau second.');
  d['setUTC'+k](d['getUTC'+k]()+n);return d}
function getPart(d,part){part=lc(part).replace(/s$/,'');
  switch(part){case 'year':case 'yy':case 'yyyy':return d.getUTCFullYear();case 'month':case 'mm':case 'm':return d.getUTCMonth()+1;case 'day':case 'dd':case 'd':return d.getUTCDate();
    case 'hour':case 'hh':return d.getUTCHours();case 'minute':case 'mi':return d.getUTCMinutes();case 'second':case 'ss':return d.getUTCSeconds();
    case 'dow':case 'weekday':case 'dw':return d.getUTCDay();case 'quarter':case 'qq':return Math.floor(d.getUTCMonth()/3)+1;case 'doy':case 'dayofyear':return Math.floor((d-Date.UTC(d.getUTCFullYear(),0,1))/864e5)+1}
  throw new SqlError(`Bagian tanggal tidak dikenal: ${part}`)}
function dateMods(d,mods){for(const m of mods){const s=String(m).trim().toLowerCase();let r;
  if((r=/^([-+]?\d+(?:\.\d+)?)\s+(year|month|day|hour|minute|second)s?$/.exec(s)))d=addPart(d,r[2],+r[1]);
  else if(s==='start of month')d=new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),1));
  else if(s==='start of year')d=new Date(Date.UTC(d.getUTCFullYear(),0,1));
  else if(s==='start of day')d=new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),d.getUTCDate()));
  else throw new SqlError(`Pengubah tanggal tidak dikenal: '${m}'`,"Contoh yang benar: '+7 days', '-1 month', 'start of month'.")}return d}
function strftime(f,d){return f.replace(/%([dmYHMSjwf%])/g,(_,c)=>({d:pad(d.getUTCDate()),m:pad(d.getUTCMonth()+1),Y:d.getUTCFullYear(),H:pad(d.getUTCHours()),M:pad(d.getUTCMinutes()),S:pad(d.getUTCSeconds()),j:pad(getPart(d,'doy'),3),w:d.getUTCDay(),f:pad(d.getUTCSeconds())+'.000','%':'%'}[c]))}

/* ---------- fungsi ---------- */
const AGG=new Set(['COUNT','SUM','AVG','MIN','MAX','TOTAL','GROUP_CONCAT','STRING_AGG']);
const WIN=new Set(['ROW_NUMBER','RANK','DENSE_RANK','NTILE','LAG','LEAD','FIRST_VALUE','LAST_VALUE','PERCENT_RANK','CUME_DIST']);
const round=(x,n=0)=>{const f=Math.pow(10,n);return Math.round((x+Math.sign(x)*1e-12)*f)/f};
const SCALAR={
  ABS:a=>a[0]==null?null:Math.abs(toNum(a[0])),
  ROUND:a=>a[0]==null?null:round(toNum(a[0]),a[1]==null?0:toNum(a[1])),
  CEIL:a=>a[0]==null?null:Math.ceil(toNum(a[0])),CEILING:a=>a[0]==null?null:Math.ceil(toNum(a[0])),
  FLOOR:a=>a[0]==null?null:Math.floor(toNum(a[0])),
  MOD:a=>a[0]==null||a[1]==null||toNum(a[1])===0?null:toNum(a[0])%toNum(a[1]),
  POWER:a=>a[0]==null||a[1]==null?null:Math.pow(toNum(a[0]),toNum(a[1])),POW:a=>SCALAR.POWER(a),
  SQRT:a=>a[0]==null?null:Math.sqrt(toNum(a[0])),SIGN:a=>a[0]==null?null:Math.sign(toNum(a[0])),
  UPPER:a=>a[0]==null?null:String(a[0]).toUpperCase(),LOWER:a=>a[0]==null?null:String(a[0]).toLowerCase(),
  LENGTH:a=>a[0]==null?null:String(a[0]).length,LEN:a=>SCALAR.LENGTH(a),CHAR_LENGTH:a=>SCALAR.LENGTH(a),
  SUBSTR:a=>{if(a[0]==null)return null;const s=String(a[0]);let st=toNum(a[1]);const n=a[2]==null?undefined:toNum(a[2]);const i=st>0?st-1:(st<0?s.length+st:0);return n===undefined?s.slice(i):s.substr(i,st===0?Math.max(0,n-1):n)},
  SUBSTRING:a=>SCALAR.SUBSTR(a),
  REPLACE:a=>a[0]==null?null:String(a[0]).split(String(a[1]??'')).join(String(a[2]??'')),
  CONCAT:a=>a.map(x=>x==null?'':String(x)).join(''),
  CONCAT_WS:a=>a.slice(1).filter(x=>x!=null).map(String).join(a[0]==null?'':String(a[0])),
  TRIM:a=>a[0]==null?null:String(a[0]).trim(),LTRIM:a=>a[0]==null?null:String(a[0]).replace(/^\s+/,''),RTRIM:a=>a[0]==null?null:String(a[0]).replace(/\s+$/,''),
  INSTR:a=>a[0]==null||a[1]==null?null:String(a[0]).indexOf(String(a[1]))+1,
  LEFT:a=>a[0]==null?null:String(a[0]).slice(0,toNum(a[1])),RIGHT:a=>a[0]==null?null:(toNum(a[1])?String(a[0]).slice(-toNum(a[1])):''),
  REVERSE:a=>a[0]==null?null:[...String(a[0])].reverse().join(''),
  LPAD:a=>a[0]==null?null:String(a[0]).padStart(toNum(a[1]),a[2]==null?' ':String(a[2])),RPAD:a=>a[0]==null?null:String(a[0]).padEnd(toNum(a[1]),a[2]==null?' ':String(a[2])),
  COALESCE:a=>{for(const x of a)if(x!=null)return x;return null},IFNULL:a=>a[0]!=null?a[0]:a[1],ISNULL:a=>a[0]!=null?a[0]:a[1],NVL:a=>a[0]!=null?a[0]:a[1],
  NULLIF:a=>a[0]!=null&&a[1]!=null&&cmpv(a[0],a[1])===0?null:a[0],
  IIF:a=>truth(a[0])?a[1]:a[2],
  TYPEOF:a=>a[0]==null?'null':isNum(a[0])?(Number.isInteger(a[0])?'integer':'real'):'text',
  GREATEST:a=>a.some(x=>x==null)?null:a.reduce((m,x)=>cmpv(x,m)>0?x:m),LEAST:a=>a.some(x=>x==null)?null:a.reduce((m,x)=>cmpv(x,m)<0?x:m),
  RANDOM:()=>Math.floor(Math.random()*2**31),
  CURRENT_DATE:()=>fdate(nowUTC()),CURRENT_TIMESTAMP:()=>{const d=nowUTC();return fdate(d)+' '+ftime(d)},CURRENT_TIME:()=>ftime(nowUTC()),
  NOW:()=>SCALAR.CURRENT_TIMESTAMP(),GETDATE:()=>SCALAR.CURRENT_TIMESTAMP(),
  DATE:a=>{let d=a[0]==='now'||a[0]===undefined?nowUTC():pdate(a[0]);if(!d)return null;return fdate(dateMods(d,a.slice(1)))},
  TIME:a=>{let d=a[0]==='now'?nowUTC():pdate(a[0]);if(!d)return null;return ftime(dateMods(d,a.slice(1)))},
  DATETIME:a=>{let d=a[0]==='now'?nowUTC():pdate(a[0]);if(!d)return null;d=dateMods(d,a.slice(1));return fdate(d)+' '+ftime(d)},
  TIMESTAMP:a=>SCALAR.DATETIME(a),
  STRFTIME:a=>{const d=a[1]==='now'?nowUTC():pdate(a[1]);return d?strftime(String(a[0]),dateMods(d,a.slice(2))):null},
  DATEADD:a=>{const d=pdate(a[2]);if(!d)return null;const r=addPart(d,a[0],toNum(a[1]));return /\d\d:\d\d/.test(String(a[2]))?fdate(r)+' '+ftime(r):fdate(r)},
  DATE_ADD:a=>{const d=pdate(a[0]);if(!d)return null;const m=/^\s*([-+]?\d+)\s+(\w+)/.exec(String(a[1]));if(!m)throw new SqlError("DATE_ADD butuh teks seperti '7 day'");return fdate(addPart(d,m[2],+m[1]))},
  DATEPART:a=>{const d=pdate(a[1]);return d?getPart(d,a[0]):null},DATE_PART:a=>SCALAR.DATEPART(a),
  DATEDIFF:a=>{if(a.length===3){const x=pdate(a[1]),y=pdate(a[2]);if(!x||!y)return null;const p=lc(a[0]);if(/^(year|yy)/.test(p))return y.getUTCFullYear()-x.getUTCFullYear();if(/^(month|mm)/.test(p))return (y.getUTCFullYear()-x.getUTCFullYear())*12+y.getUTCMonth()-x.getUTCMonth();return Math.round((y-x)/864e5)}
    const x=pdate(a[0]),y=pdate(a[1]);return x&&y?Math.round((x-y)/864e5):null},
  JULIANDAY:a=>{const d=a[0]==='now'?nowUTC():pdate(a[0]);return d?d.getTime()/864e5+2440587.5:null},
  YEAR:a=>{const d=pdate(a[0]);return d?d.getUTCFullYear():null},MONTH:a=>{const d=pdate(a[0]);return d?d.getUTCMonth()+1:null},DAY:a=>{const d=pdate(a[0]);return d?d.getUTCDate():null},
};

/* ---------- basis data ---------- */
function newDb(){return {tables:{},views:{},indexes:{},grants:[],tx:null}}
const snap=db=>JSON.parse(JSON.stringify({tables:db.tables,views:db.views,indexes:db.indexes,grants:db.grants}));
function restore(db,s){const c=JSON.parse(JSON.stringify(s));db.tables=c.tables;db.views=c.views;db.indexes=c.indexes;db.grants=c.grants}
function getTable(db,name,ctx){const t=db.tables[lc(name)];if(!t){
  const all=Object.values(db.tables).map(x=>x.name);let g=null,bd=3;for(const n of all){const d=lev(lc(name),lc(n));if(d<bd){bd=d;g=n}}
  throw new SqlError(`Tabel "${name}" tidak ada${ctx?' '+ctx:''}.`,g?`Mungkin maksudmu ${g}?`:(all.length?`Tabel yang tersedia: ${all.join(', ')}.`:'Belum ada tabel. Buat dulu dengan CREATE TABLE.'))}return t}
const colIx=(t,c)=>t.cols.findIndex(x=>lc(x.name)===lc(c));

/* ---------- evaluasi ekspresi ---------- */
/* scope: {src:[{alias,label,cols:[nama]}], row:[[...] per sumber], parent, grp:[row...]|null, win:Map, aliases:{}, ctx} */
function findCol(sc,node){
  for(let s=sc;s;s=s.parent){
    if(!s.src)continue;
    let hit=null;
    for(let i=0;i<s.src.length;i++){const S=s.src[i];
      if(node.table&&lc(S.alias)!==lc(node.table))continue;
      const j=S.cols.findIndex(c=>lc(c)===lc(node.name));
      if(j>=0){if(hit&&!node.table)throw new SqlError(`Nama kolom "${node.name}" ambigu: ada di ${hit.S.label} dan ${S.label}.`,`Tulis lengkap dengan nama tabelnya, misalnya ${S.label}.${node.name}`);hit={s,i,j,S}}}
    if(hit)return hit;
    if(s.aliases&&!node.table){const a=s.aliases[lc(node.name)];if(a)return {alias:a,s}}
  }
  return null;
}
function colErr(sc,node){
  const names=[];for(let s=sc;s;s=s.parent)if(s.src)s.src.forEach(S=>S.cols.forEach(c=>names.push(c)));
  if(node.table){let ok=false;for(let s=sc;s;s=s.parent)if(s.src&&s.src.some(S=>lc(S.alias)===lc(node.table)))ok=true;
    if(!ok)return new SqlError(`Tabel atau alias "${node.table}" tidak dikenal di query ini.`,'Pastikan tabel itu ada di FROM/JOIN, dan kalau memakai alias, tulis aliasnya.')}
  let g=null,bd=3;for(const n of names){const d=lev(lc(node.name),lc(n));if(d<bd){bd=d;g=n}}
  const looksText=node.q;
  return new SqlError(`Kolom "${node.table?node.table+'.':''}${node.name}" tidak ditemukan.`,looksText?`Teks diapit kutip tunggal ('...'), bukan kutip ganda.`:(g?`Mungkin maksudmu ${g}?`:(names.length?`Kolom yang tersedia: ${[...new Set(names)].join(', ')}.`:'')))}
function rowsOfGroup(sc){return sc.grp}
function ev(n,sc){
  switch(n.op){
    case 'lit':return n.v;
    case 'col':{const h=findCol(sc,n);if(!h){throw colErr(sc,n)}
      if(h.alias){return ev(h.alias,{...h.s,aliases:null})}
      const s=h.s;
      if(s.grp&&s.row==null){const r=s.grp[0];return r?(r[h.i]?r[h.i][h.j]:null):null}
      const r=s.row[h.i];return r?r[h.j]:null}
    case 'neg':{const v=ev(n.e,sc);return v==null?null:-toNum(v)}
    case 'bin':{const a=ev(n.l,sc),b=ev(n.r,sc);
      if(n.o==='||')return a==null||b==null?null:String(a)+String(b);
      if(a==null||b==null)return null;const x=toNum(a),y=toNum(b);
      switch(n.o){case '+':return x+y;case '-':return x-y;case '*':return x*y;
        case '/':return y===0?null:x/y;case '%':return y===0?null:x%y}}
    case 'cmp':{const a=ev(n.l,sc),b=ev(n.r,sc);if(a==null||b==null)return null;const c=cmpv(a,b);
      return B({'=':c===0,'!=':c!==0,'<':c<0,'<=':c<=0,'>':c>0,'>=':c>=0}[n.o])}
    case 'is':{const a=ev(n.l,sc),b=ev(n.r,sc);const eq=(a==null&&b==null)||(a!=null&&b!=null&&cmpv(a,b)===0);return B(n.not?!eq:eq)}
    case 'isnull':{const v=ev(n.e,sc);return B(n.not?v!=null:v==null)}
    case 'AND':{const a=truth(ev(n.l,sc));if(a===false)return 0;const b=truth(ev(n.r,sc));if(b===false)return 0;return a===null||b===null?null:1}
    case 'OR':{const a=truth(ev(n.l,sc));if(a===true)return 1;const b=truth(ev(n.r,sc));if(b===true)return 1;return a===null||b===null?null:0}
    case 'NOT':{const a=truth(ev(n.e,sc));return a===null?null:B(!a)}
    case 'between':{const v=ev(n.e,sc),a=ev(n.a,sc),b=ev(n.b,sc);if(v==null||a==null||b==null)return null;const r=cmpv(v,a)>=0&&cmpv(v,b)<=0;return B(n.not?!r:r)}
    case 'like':{const v=ev(n.e,sc),p=ev(n.p,sc);if(v==null||p==null)return null;const r=likeRe(String(p),n.esc?ev(n.esc,sc):null).test(String(v));return B(n.not?!r:r)}
    case 'in':{const v=ev(n.e,sc);let vals;
      if(n.q){const r=runQuery(n.q,sc.ctx,sc);if(r.cols.length!==1)throw new SqlError('Subquery di IN harus mengembalikan tepat satu kolom.');vals=r.rows.map(x=>x[0])}
      else vals=n.list.map(e=>ev(e,sc));
      if(v==null)return vals.length?null:B(n.not);
      let found=false,hasNull=false;for(const x of vals){if(x==null){hasNull=true;continue}if(cmpv(v,x)===0){found=true;break}}
      if(found)return B(!n.not);return hasNull?null:B(n.not)}
    case 'quant':{const v=ev(n.e,sc);const r=runQuery(n.s,sc.ctx,sc);const vals=r.rows.map(x=>x[0]);
      const t=x=>{if(v==null||x==null)return null;const c=cmpv(v,x);return {'=':c===0,'!=':c!==0,'<':c<0,'<=':c<=0,'>':c>0,'>=':c>=0}[n.o]};
      if(n.q==='ALL'){let nul=false;for(const x of vals){const z=t(x);if(z===false)return 0;if(z===null)nul=true}return nul?null:1}
      let nul=false;for(const x of vals){const z=t(x);if(z===true)return 1;if(z===null)nul=true}return nul?null:0}
    case 'exists':{const r=runQuery(n.q,sc.ctx,sc,{limit1:true});return B(r.rows.length>0)}
    case 'sub':{const r=runQuery(n.q,sc.ctx,sc);if(r.cols.length!==1)throw new SqlError('Subquery skalar harus mengembalikan tepat satu kolom.','Pilih satu kolom saja di SELECT dalam kurung.');
      return r.rows.length?r.rows[0][0]:null}
    case 'row':throw new SqlError('Daftar nilai dalam kurung tidak bisa dipakai di sini.');
    case 'case':{
      if(n.base){const b=ev(n.base,sc);for(const [w,t] of n.whens){const x=ev(w,sc);if(b!=null&&x!=null&&cmpv(b,x)===0)return ev(t,sc)}}
      else for(const [w,t] of n.whens)if(truth(ev(w,sc))===true)return ev(t,sc);
      return n.els?ev(n.els,sc):null}
    case 'cast':{const v=ev(n.e,sc);if(v==null)return null;const t=n.ty.toUpperCase();
      if(/INT/.test(t))return Math.trunc(toNum(v));if(/REAL|FLOA|DOUB|NUM|DEC/.test(t))return toNum(v);if(/CHAR|TEXT|STR/.test(t))return isNum(v)?String(v):String(v);
      if(/DATE/.test(t)){const d=pdate(v);return d?fdate(d):null}return v}
    case 'fn':{
      if(n.over){if(!sc.win||!sc.win.has(n))throw new SqlError(`Fungsi window ${n.name}() hanya boleh dipakai di SELECT atau ORDER BY.`);return sc.win.get(n)}
      if(AGG.has(n.name)&&!(['MIN','MAX'].includes(n.name)&&n.args.length>1)){
        const G=sc.grp;if(!G)throw new SqlError(`Fungsi agregat ${n.name}() tidak boleh dipakai di sini.`,n.name+'() menghitung banyak baris sekaligus. Pakai di SELECT atau HAVING, bukan di WHERE. Untuk menyaring hasil agregat, gunakan HAVING.');
        return aggregate(n,G,sc)}
      if(WIN.has(n.name))throw new SqlError(`${n.name}() adalah fungsi window dan butuh OVER (...).`,`Contoh: ${n.name}() OVER (ORDER BY harga DESC)`);
      if(n.name==='MIN'||n.name==='MAX'){const a=n.args.map(e=>ev(e,sc));return SCALAR[n.name==='MIN'?'LEAST':'GREATEST'](a)}
      const f=SCALAR[n.name];if(!f)throw new SqlError(`Fungsi ${n.name}() tidak dikenal.`,'Fungsi yang didukung antara lain: COUNT, SUM, AVG, MIN, MAX, ROUND, UPPER, LOWER, LENGTH, SUBSTR, REPLACE, COALESCE, NULLIF, DATE.');
      return f(n.args.map(e=>ev(e,sc)))}
  }
  throw new SqlError('Ekspresi tidak didukung.');
}
function aggregate(n,G,sc){
  let vals=[];
  for(const r of G){const s2={...sc,row:r,grp:null};if(n.filter&&truth(ev(n.filter,s2))!==true)continue;vals.push(n.star?1:ev(n.args[0],s2))}
  if(!n.star)vals=vals.filter(v=>v!=null);
  if(n.distinct){const seen=new Set;vals=vals.filter(v=>{const k=keyOf([v]);if(seen.has(k))return false;seen.add(k);return true})}
  switch(n.name){
    case 'COUNT':return vals.length;
    case 'SUM':return vals.length?vals.reduce((a,b)=>a+toNum(b),0):null;
    case 'TOTAL':return vals.reduce((a,b)=>a+toNum(b),0);
    case 'AVG':return vals.length?vals.reduce((a,b)=>a+toNum(b),0)/vals.length:null;
    case 'MIN':return vals.length?vals.reduce((m,x)=>cmpv(x,m)<0?x:m):null;
    case 'MAX':return vals.length?vals.reduce((m,x)=>cmpv(x,m)>0?x:m):null;
    case 'GROUP_CONCAT':case 'STRING_AGG':{const sep=n.args[1]?ev(n.args[1],{...sc,row:G[0]||null,grp:null}):',';return vals.length?vals.map(String).join(sep):null}
  }
}
function hasAgg(n){if(!n||typeof n!=='object')return false;
  if(n.op==='fn'&&!n.over&&AGG.has(n.name)&&!(['MIN','MAX'].includes(n.name)&&n.args.length>1))return true;
  if(n.op==='sub'||n.op==='exists'||n.op==='in'&&n.q||n.op==='quant'){if(n.op==='in')return hasAgg(n.e);return n.op==='quant'?hasAgg(n.e):false}
  for(const k in n){if(k==='over')continue;const v=n[k];if(Array.isArray(v)){for(const x of v)if(Array.isArray(x)?x.some(hasAgg):hasAgg(x))return true}else if(v&&typeof v==='object'&&hasAgg(v))return true}
  return false}
function collectWin(n,out){if(!n||typeof n!=='object')return out;if(n.op==='fn'&&n.over)out.push(n);
  if(n.op==='sub'||n.op==='exists')return out;
  for(const k in n){const v=n[k];if(Array.isArray(v))v.forEach(x=>Array.isArray(x)?x.forEach(y=>collectWin(y,out)):collectWin(x,out));else if(v&&typeof v==='object'&&k!=='q')collectWin(v,out)}return out}

/* ---------- FROM ---------- */
function nullRow(S){return S.cols.map(()=>null)}
function evalFrom(it,ctx,outer,tr){
  if(it.kind==='table'){
    const key=lc(it.name),alias=it.alias||it.name;
    if(ctx.ctes&&ctx.ctes[key]){const c=ctx.ctes[key];return {src:[{alias,label:alias,cols:c.cols,tbl:it.name}],rows:c.rows.map(r=>[r])}}
    if(ctx.db.views[key]){const v=ctx.db.views[key];const r=runQuery(v.q,{...ctx,ctes:null},null);const cols=v.cols||r.cols;return {src:[{alias,label:alias,cols,tbl:v.name,view:1}],rows:r.rows.map(x=>[x])}}
    const t=getTable(ctx.db,it.name);
    ctx.stats.scanned+=t.rows.length;
    return {src:[{alias,label:alias,cols:t.cols.map(c=>c.name),tbl:t.name}],rows:t.rows.map(r=>[r])};
  }
  if(it.kind==='sub'){const r=runQuery(it.q,{...ctx},outer);const alias=it.alias||'subquery';return {src:[{alias,label:alias,cols:r.cols}],rows:r.rows.map(x=>[x])}}
  const L=evalFrom(it.l,ctx,outer),R=evalFrom(it.r,ctx,outer);
  const src=[...L.src,...R.src],rows=[],pairs=[];
  let cond=it.on;
  if(it.using){cond=it.using.map(c=>({op:'cmp',o:'=',l:{op:'col',table:L.src[L.src.length-1].alias,name:c},r:{op:'col',table:R.src[0].alias,name:c}})).reduce((a,b)=>a?{op:'AND',l:a,r:b}:b,null)}
  const rm=new Array(R.rows.length).fill(false);
  L.rows.forEach((l,li)=>{let hit=false;
    R.rows.forEach((r,ri)=>{const row=[...l,...r];
      if(it.jt==='CROSS'||truth(ev(cond,{src,row,parent:outer,ctx}))===true){rows.push(row);pairs.push([li,ri]);hit=true;rm[ri]=true}});
    if(!hit&&(it.jt==='LEFT'||it.jt==='FULL')){rows.push([...l,...R.src.map(nullRow)]);pairs.push([li,null])}});
  if(it.jt==='RIGHT'||it.jt==='FULL')R.rows.forEach((r,ri)=>{if(!rm[ri]){rows.push([...L.src.map(nullRow),...r]);pairs.push([null,ri])}});
  if(tr&&!tr.join&&L.src.length===1&&R.src.length===1)tr.join={type:it.jt,comma:!!it.comma,on:it.on||it.using?true:false,
    left:{label:L.src[0].label,cols:L.src[0].cols,rows:L.rows.map(x=>x[0])},right:{label:R.src[0].label,cols:R.src[0].cols,rows:R.rows.map(x=>x[0])},pairs};
  return {src,rows};
}

/* ---------- SELECT ---------- */
function runQuery(q,ctx,outer,opt={}){
  if(q.type!=='select')throw new SqlError('Diharapkan SELECT');
  let c={...ctx,ctes:{...(ctx.ctes||{})}};
  if(q.ctes)for(const ct of q.ctes){
    const key=lc(ct.name);
    if(ct.rec&&q.ctes&&refersTo(ct.q,key)){
      const b=ct.q.body;if(b.type!=='compound'||!/UNION/.test(b.op))throw new SqlError('CTE rekursif harus berbentuk: query awal UNION [ALL] query rekursif.');
      const all=b.op==='UNION ALL';
      const anchor=runBody(b.l,c,outer);const cols=ct.cols||anchor.cols;
      let total=anchor.rows.slice(),work=anchor.rows.slice();const seen=new Set(total.map(keyOf));let it=0;
      while(work.length){if(++it>1000)throw new SqlError('CTE rekursif berhenti setelah 1000 putaran.','Pastikan bagian rekursif punya kondisi berhenti, misalnya WHERE n < 10.');
        const step=runBody(b.r,{...c,ctes:{...c.ctes,[key]:{cols,rows:work}}},outer);
        let nw=step.rows;if(!all)nw=nw.filter(r=>{const k=keyOf(r);if(seen.has(k))return false;seen.add(k);return true});
        total.push(...nw);work=nw;if(total.length>5000)throw new SqlError('Hasil CTE rekursif terlalu besar (lebih dari 5000 baris).')}
      c.ctes[key]={cols,rows:total};
    }else{const r=runQuery(ct.q,c,outer);c.ctes[key]={cols:ct.cols||r.cols,rows:r.rows}}
  }
  const tr=opt.trace?{}:null;
  if(q.body.type==='core'){
    return runCore(q.body,c,outer,{order:q.order,limit:q.limit,offset:q.offset,tr,limit1:opt.limit1});
  }
  const r=runBody(q.body,c,outer);
  let rows=r.rows;
  if(q.order){
    const pos=q.order.map(o=>{if(o.e.op==='lit'&&isNum(o.e.v))return o.e.v-1;if(o.e.op==='col'&&!o.e.table){const i=r.cols.findIndex(x=>lc(x)===lc(o.e.name));if(i>=0)return i}
      throw new SqlError('ORDER BY pada UNION harus memakai nama kolom hasil atau nomor kolom.')});
    rows=rows.slice().sort((a,b)=>{for(let k=0;k<pos.length;k++){const d=sortKey(a[pos[k]],b[pos[k]]);if(d)return q.order[k].desc?-d:d}return 0})}
  rows=applyLimit(rows,q.limit,q.offset,c);
  return {cols:r.cols,rows};
}
function refersTo(q,key){let f=false;(function w(n){if(!n||typeof n!=='object'||f)return;if(n.kind==='table'&&lc(n.name)===key){f=true;return}for(const k in n){const v=n[k];if(Array.isArray(v))v.forEach(w);else if(v&&typeof v==='object')w(v)}})(q);return f}
function applyLimit(rows,limit,offset,ctx){
  const off=offset?toNum(ev(offset,{ctx})):0;let lim=limit?toNum(ev(limit,{ctx})):null;if(lim!=null&&lim<0)lim=null;
  return rows.slice(off,lim==null?undefined:off+lim)}
function runBody(b,ctx,outer){
  if(b.type==='core')return runCore(b,ctx,outer,{});
  if(b.type==='paren')return runQuery(b.q,ctx,outer);
  if(b.type==='values'){const rows=b.rows.map(r=>r.map(e=>ev(e,{ctx,parent:outer})));return {cols:rows[0].map((_,i)=>'column'+(i+1)),rows}}
  const L=runBody(b.l,ctx,outer),R=runBody(b.r,ctx,outer);
  if(L.cols.length!==R.cols.length)throw new SqlError(`Kedua sisi ${b.op} harus punya jumlah kolom yang sama (${L.cols.length} lawan ${R.cols.length}).`);
  let rows;const K=new Set(R.rows.map(keyOf));
  if(b.op==='UNION ALL')rows=[...L.rows,...R.rows];
  else if(b.op==='UNION'){const s=new Set;rows=[...L.rows,...R.rows].filter(r=>{const k=keyOf(r);if(s.has(k))return false;s.add(k);return true})}
  else if(b.op==='INTERSECT'){const s=new Set;rows=L.rows.filter(r=>{const k=keyOf(r);if(!K.has(k)||s.has(k))return false;s.add(k);return true})}
  else{const s=new Set;rows=L.rows.filter(r=>{const k=keyOf(r);if(K.has(k)||s.has(k))return false;s.add(k);return true})}
  return {cols:L.cols,rows};
}
function colLabel(c){if(c.alias)return c.alias;if(c.e.op==='col')return c.e.name;return c.txt}
function runCore(core,ctx,outer,o){
  const tr=o.tr;
  const F=core.from?evalFrom(core.from,ctx,outer,tr):{src:[],rows:[[]]};
  const src=F.src;
  if(tr){tr.from={cols:src.flatMap(S=>S.cols.map(c=>src.length>1?S.label+'.'+c:c)),rows:F.rows.map(r=>r.flat()),tables:src.map(S=>S.label)}}
  // alias SELECT boleh dipakai di GROUP BY/HAVING/ORDER BY
  const aliases={};core.cols.forEach(c=>{if(!c.star&&c.alias)aliases[lc(c.alias)]=c.e});
  const base={src,parent:outer,ctx};
  let rows=F.rows;
  if(core.where){if(hasAgg(core.where))throw new SqlError('Fungsi agregat tidak boleh dipakai di WHERE.','WHERE menyaring baris satu per satu, sebelum dikelompokkan. Untuk menyaring hasil COUNT/SUM/AVG, gunakan HAVING setelah GROUP BY.');
    const keep=rows.map(r=>truth(ev(core.where,{...base,row:r}))===true);
    if(tr)tr.where={keep};rows=rows.filter((r,i)=>keep[i])}
  // ekspansi bintang
  const outCols=[],exprs=[];
  for(const c of core.cols){
    if(c.star){let any=false;src.forEach((S,i)=>{if(c.table&&lc(S.alias)!==lc(c.table))return;any=true;S.cols.forEach((cn,j)=>{outCols.push(cn);exprs.push({op:'col',table:S.alias,name:cn,_ix:[i,j]})})});
      if(!any)throw new SqlError(c.table?`Tabel "${c.table}" tidak ada di FROM.`:'SELECT * butuh FROM.');continue}
    outCols.push(colLabel(c));exprs.push(c.e)}
  const agg=!!core.group||exprs.some(hasAgg)||(core.having&&hasAgg(core.having))||(o.order||[]).some(x=>hasAgg(x.e));
  let items;
  if(agg){
    const gsc=r=>({...base,row:r,aliases});
    const groupExprs=(core.group||[]).map(g=>g.op==='lit'&&isNum(g.v)?(exprs[g.v-1]||(()=>{throw new SqlError('Nomor kolom di GROUP BY di luar jangkauan.')})()):g);
    if(groupExprs.some(hasAgg))throw new SqlError('Fungsi agregat tidak boleh dipakai di GROUP BY.');
    const map=new Map;const order=[];
    rows.forEach((r,ri)=>{const k=keyOf(groupExprs.map(g=>ev(g,gsc(r))));if(!map.has(k)){map.set(k,[]);order.push(k)}map.get(k).push(ri)});
    let groups=order.map(k=>map.get(k));
    if(!core.group&&!groups.length)groups=[[]];
    if(tr&&core.group)tr.group={groups:groups.map(ix=>({idx:ix.map(i=>tr.where?tr.where.keep.reduce((a,kp,j)=>{if(kp)a.push(j);return a},[])[i]:i),label:ix.length?groupExprs.map(g=>fmt(ev(g,gsc(rows[ix[0]])))).join(', '):''}))};
    items=groups.map(ix=>({...base,row:null,grp:ix.map(i=>rows[i]),aliases}));
    if(core.having){const keep=items.map(s=>truth(ev(core.having,s))===true);if(tr)tr.having={keep};items=items.filter((s,i)=>keep[i])}
  }else{
    if(core.having)throw new SqlError('HAVING hanya dipakai bersama GROUP BY atau fungsi agregat.','Untuk menyaring baris biasa, gunakan WHERE.');
    items=rows.map(r=>({...base,row:r,aliases}));
  }
  // fungsi window
  const wins=[];exprs.forEach(e=>collectWin(e,wins));(o.order||[]).forEach(x=>collectWin(x.e,wins));
  if(wins.length){items.forEach(s=>s.win=new Map);for(const w of wins)computeWin(w,items)}
  // proyeksi
  let out=items.map(s=>exprs.map(e=>e._ix?(s.row?(s.row[e._ix[0]]||[])[e._ix[1]]??null:(s.grp[0]?s.grp[0][e._ix[0]][e._ix[1]]:null)):ev(e,s)));
  if(tr)tr.select={cols:outCols,rows:out.map(r=>r.slice())};
  let idx=out.map((_,i)=>i);
  if(core.distinct){const s=new Set;idx=idx.filter(i=>{const k=keyOf(out[i]);if(s.has(k))return false;s.add(k);return true});if(tr)tr.distinct={keep:out.map((_,i)=>idx.includes(i))}}
  if(o.order){
    const keys=idx.map(i=>o.order.map(x=>{
      if(x.e.op==='lit'&&isNum(x.e.v)){if(x.e.v<1||x.e.v>outCols.length)throw new SqlError('Nomor kolom di ORDER BY di luar jangkauan.');return out[i][x.e.v-1]}
      if(x.e.op==='col'&&!x.e.table){const ai=core.cols.findIndex(c=>!c.star&&c.alias&&lc(c.alias)===lc(x.e.name));if(ai>=0){const pos=exprs.indexOf(core.cols[ai].e);return out[i][pos]}}
      return ev(x.e,items[i])}));
    const pos=idx.map((_,k)=>k);
    pos.sort((a,b)=>{for(let k=0;k<o.order.length;k++){const X=o.order[k];let d;const va=keys[a][k],vb=keys[b][k];
      if(X.nulls&&(va==null)!==(vb==null))return (va==null)===(X.nulls==='FIRST')?-1:1;
      d=sortKey(va,vb);if(d)return X.desc?-d:d}return a-b});
    idx=pos.map(k=>idx[k]);
    if(tr)tr.order={idx:idx.slice()};
  }
  let fin=idx.map(i=>out[i]);
  const top=core.top?toNum(ev(core.top,{ctx})):null;
  if(o.limit||o.offset){const before=fin.length;fin=applyLimit(fin,o.limit,o.offset,ctx);if(tr)tr.limit={n:fin.length,from:before,offset:o.offset?toNum(ev(o.offset,{ctx})):0}}
  else if(top!=null){fin=fin.slice(0,top);if(tr)tr.limit={n:fin.length,from:idx.length,offset:0}}
  const res={cols:outCols,rows:fin};if(tr)res.trace=tr;return res;
}
function computeWin(w,items){
  const spec=w.over;
  const parts=new Map;const ord=[];
  items.forEach((s,i)=>{const k=keyOf((spec.part||[]).map(e=>ev(e,s)));if(!parts.has(k)){parts.set(k,[]);ord.push(k)}parts.get(k).push(i)});
  for(const k of ord){
    let P=parts.get(k);
    const okeys=P.map(i=>(spec.order||[]).map(x=>ev(x.e,items[i])));
    const pos=P.map((_,j)=>j);
    if(spec.order)pos.sort((a,b)=>{for(let q=0;q<spec.order.length;q++){const d=sortKey(okeys[a][q],okeys[b][q]);if(d)return spec.order[q].desc?-d:d}return a-b});
    const S=pos.map(j=>P[j]),K=pos.map(j=>keyOf(okeys[j]));
    const n=S.length;
    const argv=(i,ai,def)=>w.args[ai]?ev(w.args[ai],items[i]):def;
    let rank=0,dense=0;
    S.forEach((ii,j)=>{
      const peerStart=j===0||K[j]!==K[j-1];if(peerStart){rank=j+1;dense++}
      let v;
      switch(w.name){
        case 'ROW_NUMBER':v=j+1;break;
        case 'RANK':v=rank;break;
        case 'DENSE_RANK':v=dense;break;
        case 'PERCENT_RANK':v=n>1?(rank-1)/(n-1):0;break;
        case 'CUME_DIST':{let e=j;while(e+1<n&&K[e+1]===K[j])e++;v=(e+1)/n;break}
        case 'NTILE':{const b=toNum(argv(ii,0,1));const per=Math.floor(n/b),extra=n%b;let acc=0,t=1;for(;t<=b;t++){const sz=per+(t<=extra?1:0);if(j<acc+sz)break;acc+=sz}v=t;break}
        case 'LAG':case 'LEAD':{const off=toNum(argv(ii,1,1));const t=w.name==='LAG'?j-off:j+off;v=t>=0&&t<n?ev(w.args[0],items[S[t]]):argv(ii,2,null);break}
        case 'FIRST_VALUE':v=ev(w.args[0],items[S[0]]);break;
        case 'LAST_VALUE':{let e=spec.order?j:n-1;if(spec.order&&!/UNBOUNDED FOLLOWING/.test(spec.frame||''))while(e+1<n&&K[e+1]===K[j])e++;else e=n-1;v=ev(w.args[0],items[S[e]]);break}
        default:{
          if(!AGG.has(w.name))throw new SqlError(`Fungsi ${w.name}() tidak bisa dipakai dengan OVER.`);
          let end=n-1;
          if(spec.order){end=j;if(!/ROWS/.test(spec.frame||''))while(end+1<n&&K[end+1]===K[j])end++}
          let start=0;const fm=/ROWS BETWEEN (\d+) PRECEDING AND CURRENT ROW/.exec(spec.frame||'');if(fm)start=Math.max(0,j-+fm[1]);
          const G=[];for(let q=start;q<=end;q++){const it=items[S[q]];if(it.grp)G.push(...it.grp);else G.push(it.row)}
          const it0=items[ii];
          if(it0.grp){ // agregat di atas grup: nilai agregat per grup lalu dijumlah
            const vals=[];for(let q=start;q<=end;q++)vals.push(ev(w.args[0],items[S[q]]));
            const nn=vals.filter(x=>x!=null);
            v=w.name==='COUNT'?(w.star?end-start+1:nn.length):w.name==='SUM'?(nn.length?nn.reduce((a,b)=>a+toNum(b),0):null):w.name==='AVG'?(nn.length?nn.reduce((a,b)=>a+toNum(b),0)/nn.length:null):w.name==='MIN'?(nn.length?nn.reduce((m,x)=>cmpv(x,m)<0?x:m):null):(nn.length?nn.reduce((m,x)=>cmpv(x,m)>0?x:m):null);
          }else v=aggregate({...w,over:null},G,it0);
        }
      }
      items[ii].win.set(w,v);
    });
  }
}

/* ---------- penulisan data & batasan ---------- */
function checkRow(db,t,row,skipIdx){
  t.cols.forEach((c,i)=>{if((c.nn||c.pk)&&row[i]==null&&!(c.pk&&isIntPk(t,c)))throw new SqlError(`Kolom ${t.name}.${c.name} tidak boleh kosong (NOT NULL).`,`Isi nilai untuk ${c.name} di INSERT/UPDATE.`)});
  const sc={src:[{alias:t.name,label:t.name,cols:t.cols.map(c=>c.name)}],row:[row]};
  t.cols.forEach(c=>{if(c.check&&truth(ev(c.check,sc))===false)throw new SqlError(`Nilai melanggar aturan CHECK pada kolom ${t.name}.${c.name}.`,'Aturan: '+(c.checkTxt||'lihat definisi tabel'))});
  (t.checks||[]).forEach(ch=>{if(truth(ev(ch.e,sc))===false)throw new SqlError(`Baris melanggar aturan CHECK${ch.cname?' '+ch.cname:''} pada tabel ${t.name}.`)});
  for(const u of uniqueSets(db,t)){
    const vals=u.cols.map(i=>row[i]);if(vals.some(v=>v==null))continue;
    t.rows.forEach((r,ri)=>{if(ri===skipIdx)return;if(u.cols.every((i,k)=>r[i]!=null&&cmpv(r[i],vals[k])===0))
      throw new SqlError(`Nilai ${vals.map(fmt).join(', ')} sudah ada di ${t.name}.${u.cols.map(i=>t.cols[i].name).join(', ')} (${u.why}).`,u.why==='PRIMARY KEY'?'Primary key harus unik untuk setiap baris.':'Kolom ini tidak boleh punya nilai kembar.')})}
  for(const fk of t.fks||[]){
    const vals=fk.cols.map(c=>row[colIx(t,c)]);if(vals.some(v=>v==null))continue;
    const p=db.tables[lc(fk.table)];if(!p)throw new SqlError(`Tabel rujukan ${fk.table} tidak ada.`);
    const pc=(fk.refCols||pkCols(p)).map(c=>colIx(p,c));
    if(!p.rows.some(r=>pc.every((i,k)=>r[i]!=null&&cmpv(r[i],vals[k])===0)))
      throw new SqlError(`FOREIGN KEY gagal: ${t.name}.${fk.cols.join(',')} = ${vals.map(fmt).join(', ')} tidak ada di ${p.name}.${pc.map(i=>p.cols[i].name).join(',')}.`,`Tambahkan dulu barisnya di tabel ${p.name}, atau pakai nilai yang sudah ada.`)}
}
const pkCols=t=>t.cols.filter(c=>c.pk).map(c=>c.name);
const isIntPk=(t,c)=>c.pk&&/INT/i.test(c.type)&&t.cols.filter(x=>x.pk).length===1;
function uniqueSets(db,t){const u=[];const pk=t.cols.map((c,i)=>c.pk?i:-1).filter(i=>i>=0);if(pk.length)u.push({cols:pk,why:'PRIMARY KEY'});
  t.cols.forEach((c,i)=>{if(c.unique)u.push({cols:[i],why:'UNIQUE'})});(t.uniques||[]).forEach(cs=>u.push({cols:cs.map(c=>colIx(t,c)),why:'UNIQUE'}));
  Object.values(db.indexes).forEach(ix=>{if(ix.unique&&lc(ix.table)===lc(t.name))u.push({cols:ix.cols.map(c=>colIx(t,c)),why:'UNIQUE INDEX '+ix.name})});return u}
function children(db,t){const out=[];for(const c of Object.values(db.tables))for(const fk of c.fks||[])if(lc(fk.table)===lc(t.name))out.push({c,fk});return out}
function deleteRows(db,t,idxSet,depth=0){
  // aturan ON DELETE di tabel anak
  const doomed=t.rows.filter((r,i)=>idxSet.has(i));
  for(const {c,fk} of children(db,t)){
    const pc=(fk.refCols||pkCols(t)).map(x=>colIx(t,x)),cc=fk.cols.map(x=>colIx(c,x));
    const hit=new Set;c.rows.forEach((r,ri)=>{if(doomed.some(d=>pc.every((pi,k)=>r[cc[k]]!=null&&cmpv(r[cc[k]],d[pi])===0)))hit.add(ri)});
    if(!hit.size)continue;
    if(fk.onDelete==='CASCADE'){if(c===t){hit.forEach(i=>idxSet.add(i))}else deleteRows(db,c,hit,depth+1)}
    else if(fk.onDelete==='SET NULL'){hit.forEach(ri=>cc.forEach(ci=>c.rows[ri][ci]=null))}
    else if(!(c===t&&[...hit].every(i=>idxSet.has(i))))throw new SqlError(`Tidak bisa menghapus dari ${t.name}: baris itu masih dirujuk oleh ${c.name}.${fk.cols.join(',')} (FOREIGN KEY).`,`Hapus dulu baris terkait di ${c.name}, atau buat FOREIGN KEY dengan ON DELETE CASCADE.`)
  }
  const n=t.rows.length;t.rows=t.rows.filter((r,i)=>!idxSet.has(i));return n-t.rows.length;
}

/* ---------- eksekusi perintah ---------- */
function fmt(v){if(v==null)return 'NULL';if(isNum(v))return Number.isInteger(v)?String(v):String(round(v,4));return String(v)}
function tableFromDef(db,st){
  const cols=st.cols.map(c=>({name:c.name,type:c.type||'',pk:!!c.pk,nn:!!c.nn,unique:!!c.unique,def:c.def||null,check:c.check||null,checkTxt:c.checkTxt||'',auto:!!c.auto}));
  const names=new Set;cols.forEach(c=>{if(names.has(lc(c.name)))throw new SqlError(`Kolom ${c.name} ditulis dua kali.`);names.add(lc(c.name))});
  const t={name:st.name,cols,rows:[],fks:[],uniques:[],checks:[]};
  st.cols.forEach(c=>{if(c.ref)t.fks.push({cols:[c.name],table:c.ref.table,refCols:c.ref.cols,onDelete:c.ref.onDelete})});
  for(const k of st.cons){
    if(k.k==='pk'){k.cols.forEach(n=>{const i=colIx(t,n);if(i<0)throw new SqlError(`PRIMARY KEY menyebut kolom ${n} yang tidak ada.`);t.cols[i].pk=true})}
    else if(k.k==='unique')t.uniques.push(k.cols);
    else if(k.k==='check')t.checks.push({e:k.e,cname:k.cname});
    else if(k.k==='fk')t.fks.push({cols:k.cols,table:k.ref.table,refCols:k.ref.cols,onDelete:k.ref.onDelete,cname:k.cname});
  }
  for(const fk of t.fks){fk.cols.forEach(n=>{if(colIx(t,n)<0)throw new SqlError(`FOREIGN KEY menyebut kolom ${n} yang tidak ada.`)});
    if(lc(fk.table)!==lc(t.name)&&!db.tables[lc(fk.table)])throw new SqlError(`FOREIGN KEY merujuk tabel ${fk.table} yang belum ada.`,'Buat tabel induknya lebih dulu.')}
  return t;
}
function insertRow(db,t,vals,cols){
  const row=t.cols.map(c=>c.def?ev(c.def,{}):null);
  const set=cols?cols.map(n=>{const i=colIx(t,n);if(i<0)throw new SqlError(`Kolom "${n}" tidak ada di tabel ${t.name}.`,`Kolom ${t.name}: ${t.cols.map(c=>c.name).join(', ')}.`);return i}):t.cols.map((_,i)=>i);
  if(vals.length!==set.length)throw new SqlError(`Jumlah nilai (${vals.length}) tidak sama dengan jumlah kolom (${set.length}).`,cols?'Setiap kolom yang disebut butuh tepat satu nilai.':`Tabel ${t.name} punya ${t.cols.length} kolom: ${t.cols.map(c=>c.name).join(', ')}. Sebutkan kolomnya, misalnya INSERT INTO ${t.name} (kolom1, kolom2) VALUES (...).`);
  set.forEach((ci,k)=>row[ci]=affinity(t.cols[ci].type,vals[k]));
  t.cols.forEach((c,i)=>{if(row[i]==null&&isIntPk(t,c)){t.seq=Math.max(t.seq||0,...t.rows.map(r=>toNum(r[i])||0))+1;row[i]=t.seq}});
  checkRow(db,t,row,-1);t.rows.push(row);
}
function execOne(db,st,opt){
  const ctx={db,ctes:null,stats:{scanned:0}};
  switch(st.type){
    case 'select':{const r=runQuery(st,ctx,null,{trace:opt.trace});return {kind:'rows',cols:r.cols,rows:r.rows,trace:r.trace,stats:ctx.stats}}
    case 'explain':return {kind:'rows',cols:['detail'],rows:plan(db,st.q).map(x=>[x])};
    case 'create':{const k=lc(st.name);if(db.tables[k]||db.views[k]){if(st.ine)return {kind:'msg',msg:`Tabel ${st.name} sudah ada, dilewati.`};throw new SqlError(`Tabel ${st.name} sudah ada.`,'Pakai CREATE TABLE IF NOT EXISTS, atau hapus dulu dengan DROP TABLE.')}
      db.tables[k]=tableFromDef(db,st);return {kind:'msg',msg:`Tabel ${st.name} dibuat dengan ${st.cols.length} kolom.`,ddl:true}}
    case 'createas':{const r=runQuery(st.q,ctx,null);const k=lc(st.name);if(db.tables[k])throw new SqlError(`Tabel ${st.name} sudah ada.`);
      db.tables[k]={name:st.name,cols:r.cols.map(n=>({name:n,type:''})),rows:r.rows.map(x=>x.slice()),fks:[],uniques:[],checks:[]};return {kind:'msg',msg:`Tabel ${st.name} dibuat dari hasil query (${r.rows.length} baris).`,ddl:true}}
    case 'insert':{const t=getTable(db,st.name,'untuk INSERT');let rows;
      if(st.q){rows=runQuery(st.q,ctx,null).rows}else rows=st.rows.map(r=>r.map(e=>ev(e,{ctx})));
      if(st.rows&&st.rows.length===1&&st.rows[0].length===0){rows=[[]];t.rows.push(t.cols.map(c=>c.def?ev(c.def,{}):null));return {kind:'msg',msg:'1 baris ditambahkan.'}}
      rows.forEach(r=>insertRow(db,t,r,st.cols));return {kind:'msg',msg:`${rows.length} baris ditambahkan ke ${t.name}.`,changed:t.name}}
    case 'update':{const t=getTable(db,st.name,'untuk UPDATE');const al=st.alias||t.name;const S=[{alias:al,label:t.name,cols:t.cols.map(c=>c.name)}];
      const sets=st.sets.map(([c,e])=>{const i=colIx(t,c);if(i<0)throw new SqlError(`Kolom "${c}" tidak ada di tabel ${t.name}.`);return [i,e]});
      let n=0;const old=t.rows.map(r=>r.slice());
      t.rows.forEach((r,ri)=>{const sc={src:S,row:[old[ri]],ctx};if(st.where&&truth(ev(st.where,sc))!==true)return;
        const nr=old[ri].slice();sets.forEach(([i,e])=>nr[i]=affinity(t.cols[i].type,ev(e,sc)));
        // jangan putus rujukan anak
        for(const {c,fk} of children(db,t)){const pc=(fk.refCols||pkCols(t)).map(x=>colIx(t,x)),cc=fk.cols.map(x=>colIx(c,x));
          if(pc.some(i=>cmpv(old[ri][i]??'',nr[i]??'')!==0)&&c.rows.some(x=>pc.every((pi,k)=>x[cc[k]]!=null&&cmpv(x[cc[k]],old[ri][pi])===0)))
            throw new SqlError(`Tidak bisa mengubah ${t.name}.${pc.map(i=>t.cols[i].name)}: nilainya masih dirujuk oleh ${c.name}.`)}
        checkRow(db,t,nr,ri);t.rows[ri]=nr;n++});
      return {kind:'msg',msg:`${n} baris diubah di ${t.name}.`+(st.where?'':' (Tanpa WHERE: semua baris ikut berubah!)'),changed:t.name,warn:!st.where}}
    case 'delete':{const t=getTable(db,st.name,'untuk DELETE');const al=st.alias||t.name;const S=[{alias:al,label:t.name,cols:t.cols.map(c=>c.name)}];
      const set=new Set;t.rows.forEach((r,ri)=>{if(!st.where||truth(ev(st.where,{src:S,row:[r],ctx}))===true)set.add(ri)});
      const n=deleteRows(db,t,set);return {kind:'msg',msg:`${n} baris dihapus dari ${t.name}.`+(st.where?'':' (Tanpa WHERE: semua baris terhapus!)'),changed:t.name,warn:!st.where}}
    case 'truncate':{const t=getTable(db,st.name);if(children(db,t).some(({c,fk})=>c!==t&&c.rows.length))throw new SqlError(`TRUNCATE ${t.name} ditolak: tabel lain masih merujuk ke tabel ini.`,'Kosongkan dulu tabel anaknya.');
      const n=t.rows.length;t.rows=[];t.seq=0;return {kind:'msg',msg:`Tabel ${t.name} dikosongkan (${n} baris hilang). Strukturnya tetap ada.`,changed:t.name}}
    case 'drop':{const k=lc(st.name);
      if(st.k==='TABLE'){const t=db.tables[k];if(!t){if(st.ie)return {kind:'msg',msg:'Tabel tidak ada, dilewati.'};getTable(db,st.name)}
        const ch=children(db,t).filter(x=>x.c!==t);if(ch.length)throw new SqlError(`Tabel ${t.name} tidak bisa dihapus: masih dirujuk FOREIGN KEY dari ${ch.map(x=>x.c.name).join(', ')}.`,'Hapus dulu tabel anaknya, atau hapus constraint-nya.');
        delete db.tables[k];Object.keys(db.indexes).forEach(i=>{if(lc(db.indexes[i].table)===k)delete db.indexes[i]});return {kind:'msg',msg:`Tabel ${t.name} dihapus beserta seluruh datanya.`,ddl:true}}
      if(st.k==='VIEW'){if(!db.views[k]){if(st.ie)return {kind:'msg',msg:'View tidak ada, dilewati.'};throw new SqlError(`View ${st.name} tidak ada.`)}delete db.views[k];return {kind:'msg',msg:`View ${st.name} dihapus. Tabel aslinya tidak terpengaruh.`,ddl:true}}
      if(!db.indexes[k]){if(st.ie)return {kind:'msg',msg:'Index tidak ada, dilewati.'};throw new SqlError(`Index ${st.name} tidak ada.`)}delete db.indexes[k];return {kind:'msg',msg:`Index ${st.name} dihapus.`,ddl:true}}
    case 'alter':{const t=getTable(db,st.name);
      if(st.act==='add'){if(colIx(t,st.col.name)>=0)throw new SqlError(`Kolom ${st.col.name} sudah ada.`);const c={name:st.col.name,type:st.col.type||'',nn:!!st.col.nn,unique:!!st.col.unique,def:st.col.def||null,check:st.col.check||null};
        const dv=c.def?ev(c.def,{}):null;if(c.nn&&dv==null&&t.rows.length)throw new SqlError(`Kolom NOT NULL baru butuh DEFAULT karena tabel ${t.name} sudah berisi data.`);
        t.cols.push(c);t.rows.forEach(r=>r.push(dv));if(st.col.ref)t.fks.push({cols:[c.name],table:st.col.ref.table,refCols:st.col.ref.cols,onDelete:st.col.ref.onDelete});
        return {kind:'msg',msg:`Kolom ${c.name} ditambahkan ke ${t.name}.`,ddl:true}}
      if(st.act==='drop'){const i=colIx(t,st.col);if(i<0)throw new SqlError(`Kolom ${st.col} tidak ada di ${t.name}.`);if(t.cols[i].pk)throw new SqlError('Kolom PRIMARY KEY tidak bisa dihapus.');
        if(children(db,t).some(({fk})=>(fk.refCols||[]).some(c=>lc(c)===lc(st.col))))throw new SqlError('Kolom ini masih dirujuk FOREIGN KEY tabel lain.');
        t.cols.splice(i,1);t.rows.forEach(r=>r.splice(i,1));t.fks=(t.fks||[]).filter(f=>!f.cols.some(c=>lc(c)===lc(st.col)));return {kind:'msg',msg:`Kolom ${st.col} dihapus dari ${t.name}.`,ddl:true}}
      if(st.act==='rename'){const k2=lc(st.to);if(db.tables[k2])throw new SqlError(`Tabel ${st.to} sudah ada.`);const old=t.name;delete db.tables[lc(old)];t.name=st.to;db.tables[k2]=t;
        Object.values(db.tables).forEach(x=>(x.fks||[]).forEach(f=>{if(lc(f.table)===lc(old))f.table=st.to}));return {kind:'msg',msg:`Tabel ${old} diganti nama menjadi ${st.to}.`,ddl:true}}
      if(st.act==='renamecol'){const i=colIx(t,st.from);if(i<0)throw new SqlError(`Kolom ${st.from} tidak ada.`);t.cols[i].name=st.to;return {kind:'msg',msg:`Kolom ${st.from} diganti nama menjadi ${st.to}.`,ddl:true}}
      if(st.act==='type'){const i=colIx(t,st.col);if(i<0)throw new SqlError(`Kolom ${st.col} tidak ada.`);t.cols[i].type=st.ty;t.rows.forEach(r=>r[i]=affinity(st.ty,r[i]));return {kind:'msg',msg:`Tipe kolom ${st.col} diubah menjadi ${st.ty}.`,ddl:true}}
      if(st.act==='addcons'){const k=st.cons;if(k.k==='check'){t.checks.push({e:k.e,cname:k.cname});try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){t.checks.pop();throw e}}
        else if(k.k==='unique'){t.uniques.push(k.cols);try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){t.uniques.pop();throw e}}
        else if(k.k==='fk'){t.fks.push({cols:k.cols,table:k.ref.table,refCols:k.ref.cols,onDelete:k.ref.onDelete});try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){t.fks.pop();throw e}}
        else throw new SqlError('Menambah PRIMARY KEY lewat ALTER tidak didukung.');
        return {kind:'msg',msg:`Constraint ditambahkan ke ${t.name}.`,ddl:true}}}
    case 'view':{const k=lc(st.name);if(db.tables[k])throw new SqlError(`Sudah ada tabel bernama ${st.name}.`);
      if(db.views[k]&&!st.replace){if(st.ine)return {kind:'msg',msg:'View sudah ada, dilewati.'};throw new SqlError(`View ${st.name} sudah ada.`,'Pakai CREATE OR REPLACE VIEW untuk mengubahnya.')}
      runQuery(st.q,ctx,null);const existed=!!db.views[k];db.views[k]={name:st.name,q:st.q,cols:st.cols,body:st.body};
      return {kind:'msg',msg:existed?`View ${st.name} diperbarui.`:`View ${st.name} dibuat. Pakai seperti tabel: SELECT * FROM ${st.name};`,ddl:true}}
    case 'index':{const k=lc(st.name);const t=getTable(db,st.table);if(db.indexes[k]){if(st.ine)return {kind:'msg',msg:'Index sudah ada, dilewati.'};throw new SqlError(`Index ${st.name} sudah ada.`)}
      st.cols.forEach(c=>{if(colIx(t,c)<0)throw new SqlError(`Kolom ${c} tidak ada di ${t.name}.`)});
      db.indexes[k]={name:st.name,table:t.name,cols:st.cols,unique:st.unique};
      if(st.unique){try{t.rows.forEach((r,i)=>checkRow(db,t,r,i))}catch(e){delete db.indexes[k];throw new SqlError(`UNIQUE INDEX gagal dibuat: sudah ada nilai kembar di ${st.cols.join(', ')}.`)}}
      return {kind:'msg',msg:`Index ${st.name} dibuat pada ${t.name}(${st.cols.join(', ')}).`,ddl:true}}
    case 'begin':if(db.tx)throw new SqlError('Transaksi sudah berjalan.','Akhiri dulu dengan COMMIT atau ROLLBACK.');db.tx={snap:snap(db),sp:[]};return {kind:'msg',msg:'Transaksi dimulai. Perubahan berikutnya belum permanen sampai COMMIT.',tx:true};
    case 'commit':if(!db.tx)throw new SqlError('Tidak ada transaksi yang sedang berjalan.','Mulai dengan BEGIN.');db.tx=null;return {kind:'msg',msg:'COMMIT: semua perubahan dalam transaksi disimpan permanen.',tx:true};
    case 'rollback':{if(!db.tx)throw new SqlError('Tidak ada transaksi yang sedang berjalan.','Mulai dengan BEGIN.');
      if(st.to){const i=db.tx.sp.map(s=>lc(s.name)).lastIndexOf(lc(st.to));if(i<0)throw new SqlError(`Savepoint ${st.to} tidak ada.`);restore(db,db.tx.sp[i].snap);db.tx.sp=db.tx.sp.slice(0,i+1);return {kind:'msg',msg:`Kembali ke savepoint ${st.to}. Perubahan setelahnya dibatalkan, transaksi masih berjalan.`,tx:true}}
      restore(db,db.tx.snap);db.tx=null;return {kind:'msg',msg:'ROLLBACK: semua perubahan sejak BEGIN dibatalkan.',tx:true}}
    case 'savepoint':if(!db.tx){db.tx={snap:snap(db),sp:[]}}db.tx.sp.push({name:st.name,snap:snap(db)});return {kind:'msg',msg:`Savepoint ${st.name} dibuat.`,tx:true};
    case 'release':if(!db.tx)throw new SqlError('Tidak ada transaksi.');db.tx.sp=db.tx.sp.filter(s=>lc(s.name)!==lc(st.name));return {kind:'msg',msg:`Savepoint ${st.name} dilepas.`,tx:true};
    case 'grant':{getTable(db,st.obj);
      if(st.g==='GRANT'){st.privs.forEach(p=>{if(!db.grants.some(g=>g.who===st.who&&g.obj===st.obj&&g.p===p))db.grants.push({who:st.who,obj:st.obj,p})});return {kind:'msg',msg:`(Simulasi) Hak ${st.privs.join(', ')} pada ${st.obj} diberikan ke ${st.who}.`,grant:true}}
      db.grants=db.grants.filter(g=>!(g.who===st.who&&g.obj===st.obj&&(st.privs.includes(g.p)||st.privs.includes('ALL'))));return {kind:'msg',msg:`(Simulasi) Hak ${st.privs.join(', ')} pada ${st.obj} dicabut dari ${st.who}.`,grant:true}}
  }
  throw new SqlError('Perintah belum didukung.');
}
/* rencana eksekusi sederhana untuk EXPLAIN */
function plan(db,q){
  const out=[];const b=q.body;if(b.type!=='core'){out.push('COMPOUND QUERY');return out}
  const eqs=[];(function w(e){if(!e)return;if(e.op==='AND'){w(e.l);w(e.r);return}if(e.op==='cmp'&&e.o==='='){if(e.l.op==='col'&&e.r.op!=='col')eqs.push([e.l,'=']);else if(e.r.op==='col'&&e.l.op!=='col')eqs.push([e.r,'='])}
    if(e.op==='cmp'&&['<','>','<=','>='].includes(e.o)&&e.l.op==='col'&&e.r.op==='lit')eqs.push([e.l,'>']);if(e.op==='between'&&e.e.op==='col')eqs.push([e.e,'>'])})(b.where);
  const tables=[];(function w(f,on){if(!f)return;if(f.kind==='join'){w(f.l);w(f.r,f.on);return}tables.push({f,on})})(b.from);
  tables.forEach(({f,on},ti)=>{
    if(f.kind!=='table'){out.push('SCAN subquery');return}
    const t=db.tables[lc(f.name)];if(!t){out.push(`SCAN ${f.name}`);return}
    const al=lc(f.alias||f.name);const preds=[...eqs];
    if(on)(function w(e){if(!e)return;if(e.op==='AND'){w(e.l);w(e.r);return}if(e.op==='cmp'&&e.o==='='&&e.l.op==='col'&&e.r.op==='col'){[e.l,e.r].forEach(c=>{if(c.table&&lc(c.table)===al)preds.push([c,'='])})}})(on);
    const mine=preds.filter(([c])=>(!c.table||lc(c.table)===al)&&colIx(t,c.name)>=0);
    const pk=t.cols.find(c=>c.pk);
    let used=null;
    for(const [c,k] of mine){
      if(pk&&lc(pk.name)===lc(c.name)&&isIntPk(t,pk)&&k==='='){used=`SEARCH ${t.name} USING INTEGER PRIMARY KEY (${c.name}=?)`;break}
      const ix=Object.values(db.indexes).find(x=>lc(x.table)===lc(t.name)&&lc(x.cols[0])===lc(c.name));
      if(ix){used=`SEARCH ${t.name} USING INDEX ${ix.name} (${c.name}${k==='='?'=?':'>?'})`;if(k==='=')break}
    }
    out.push(used||`SCAN ${t.name}`+(ti>0?' (cek setiap baris untuk setiap baris tabel sebelumnya)':''));
  });
  if(b.group)out.push('USE TEMP B-TREE FOR GROUP BY');
  if(q.order){const oc=q.order[0].e;const ix=oc.op==='col'&&tables.length===1&&Object.values(db.indexes).find(x=>tables[0].f.kind==='table'&&lc(x.table)===lc(tables[0].f.name)&&lc(x.cols[0])===lc(oc.name));if(!ix)out.push('USE TEMP B-TREE FOR ORDER BY')}
  return out;
}

/* ---------- API publik ---------- */
function parse(sql){return new Parser(sql).all()}
function exec(db,sql,opt={}){
  const stmts=parse(sql);if(!stmts.length)throw new SqlError('Belum ada perintah untuk dijalankan.','Tulis query, misalnya SELECT * FROM produk;');
  const res=[];
  for(let i=0;i<stmts.length;i++){
    const st=stmts[i];const before=db.tx?null:snap(db);
    try{const r=execOne(db,st,{trace:opt.trace&&i===stmts.length-1});r.sql=st.sql;r.type=st.type;res.push(r)}
    catch(e){if(before)restore(db,before);if(e instanceof SqlError){e.stmt=i;e.sql=st.sql;e.done=res}throw e}
  }
  return res;
}
function create(seed){const db=newDb();if(seed)exec(db,seed);return db}
function schema(db){return Object.values(db.tables).map(t=>({name:t.name,rows:t.rows.length,cols:t.cols.map(c=>({name:c.name,type:c.type,pk:c.pk,fk:(t.fks||[]).find(f=>f.cols.some(x=>lc(x)===lc(c.name)))}))}))
  .concat(Object.values(db.views).map(v=>({name:v.name,view:true,cols:[]})))}
function clone(db){const c=newDb();restore(c,snap(db));return c}
return {exec,parse,create,schema,clone,fmt,SqlError,tokenize,snap,restore};
})();
if(typeof module!=='undefined')module.exports=SQLE;
