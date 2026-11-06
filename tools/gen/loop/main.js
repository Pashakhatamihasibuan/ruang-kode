// 1. for: jumlah putaran sudah pasti
for (let i = 1; i <= 3; i++) {
  console.log("for: i = " + i);
}

// 2. while: kondisi dicek DULU, bisa 0 kali
let n = 3;
while (n > 0) {
  console.log("while: n = " + n);
  n--;
}

// 3. do-while: badan jalan DULU, kondisi dicek di akhir
let x = 10;
do {
  console.log("do-while: x = " + x + " (tetap jalan sekali)");
  x++;
} while (x < 5);

// 4. for...of: menelusuri isi array tanpa indeks
const buah = ["apel", "jeruk", "mangga"];
for (const b of buah) {
  console.log("for-each: " + b);
}

// 5. bersarang: loop di dalam loop
for (let baris = 1; baris <= 2; baris++) {
  const isi = [];
  for (let kolom = 1; kolom <= 3; kolom++) {
    isi.push(baris * kolom);
  }
  console.log("nested: " + isi.join(" "));
}

// 6. break: keluar dari loop lebih awal
let hasil = [];
for (let i = 1; i <= 10; i++) {
  if (i === 4) break;
  hasil.push(i);
}
console.log("break: " + hasil.join(" "));

// 7. continue: lewati sisa badan untuk putaran ini saja
hasil = [];
for (let i = 1; i <= 6; i++) {
  if (i % 2 === 0) continue;
  hasil.push(i);
}
console.log("continue: " + hasil.join(" "));
