// Fungsi bantu: bilangan bulat acak bawah..atas (kedua batas ikut)
function acakAntara(bawah, atas) {
  return Math.floor(Math.random() * (atas - bawah + 1)) + bawah;
}

// 1. Desimal acak: 0.0 sampai KURANG DARI 1.0
const r = Math.random();
console.log("desimal: " + r.toFixed(4));

// 2. Dadu 1..6
let dadu = "5 dadu :";
for (let i = 0; i < 5; i++) {
  dadu += " " + acakAntara(1, 6);
}
console.log(dadu);

// 3. Rentang bebas
console.log("10..20 : " + acakAntara(10, 20));

// 4. Lempar dadu sampai keluar angka 6
let lemparan = 0, hasil = 0;
while (hasil !== 6) {
  hasil = acakAntara(1, 6);
  lemparan++;
}
console.log(`dapat 6 setelah ${lemparan} lemparan`);

// 5. Memilih satu isi array dan mengocok array (algoritma Fisher-Yates)
const menu = ["soto", "bakso", "gado-gado", "nasi goreng"];
console.log("menu   : " + menu[acakAntara(0, menu.length - 1)]);
const kartu = [1, 2, 3, 4, 5];
for (let i = kartu.length - 1; i > 0; i--) {
  const j = acakAntara(0, i);
  [kartu[i], kartu[j]] = [kartu[j], kartu[i]];
}
console.log("kocok  : [" + kartu.join(", ") + "]");

// 6. Math.random() tidak bisa diberi seed
console.log("seed: Math.random() tidak punya seed, pakai pustaka bila perlu");
