// 1. Hasil perbandingan selalu boolean: true atau false
const nilai = 82, hadir = 70;
const nilaiCukup = nilai >= 75;
const hadirCukup = hadir >= 80;
console.log("nilaiCukup = " + nilaiCukup);
console.log("hadirCukup = " + hadirCukup);

// 2. AND (&&), OR (||), NOT (!)
console.log("AND: lulus = " + (nilaiCukup && hadirCukup));
console.log("OR : remedial = " + (!nilaiCukup || !hadirCukup));
console.log("NOT: !hadirCukup = " + !hadirCukup);

// 3. Tabel kebenaran semua kombinasi p dan q
const tf = [true, false];
const kol = (v) => String(v).padEnd(6);
console.log("p     q     AND   OR    XOR");
for (const p of tf) {
  for (const q of tf) {
    console.log(kol(p) + kol(q) + kol(p && q) + kol(p || q) + (p !== q));
  }
}

// 4. Hukum De Morgan, dicek untuk semua kombinasi
let hukum1 = true, hukum2 = true;
for (const p of tf) {
  for (const q of tf) {
    if (!(p && q) !== (!p || !q)) hukum1 = false;
    if (!(p || q) !== (!p && !q)) hukum2 = false;
  }
}
console.log("De Morgan 1: !(p && q) == !p || !q -> " + hukum1);
console.log("De Morgan 2: !(p || q) == !p && !q -> " + hukum2);

// 5. Urutan: ! dulu, lalu &&, baru ||
console.log("true || false && false = " + (true || false && false));

// 6. Short-circuit: sisi kanan tidak dihitung jika hasil sudah pasti
const pembagi = 0;
if (pembagi !== 0 && 10 / pembagi > 1) {
  console.log("hasil bagi besar");
} else {
  console.log("short-circuit: 10 / 0 tidak pernah dihitung");
}
