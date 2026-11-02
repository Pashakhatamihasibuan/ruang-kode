const nama: string = "Rina";
const umur: number = 20;
const ipk: number = 3.4567;
// template literal: ${ekspresi}, angka desimal dengan toFixed
console.log(`Nama: ${nama}, umur ${umur}, IPK ${ipk.toFixed(2)}`);

// lebar dan perataan: padStart (rata kanan), padEnd (rata kiri)
console.log(`[${nama.padStart(8)}] [${nama.padEnd(8)}] [${String(umur).padStart(5, "0")}]`);

// basis lain, notasi ilmiah, persen
console.log(`hex ${(255).toString(16)} | biner ${(5).toString(2)} | ${(123456.789).toExponential(3)} | ${(0.15 * 100).toFixed(0)}%`);

// format lokal Indonesia: ribuan dengan titik, mata uang Rupiah
const rupiah: Intl.NumberFormat = new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 });
console.log((7500000).toLocaleString("id-ID"), "|", rupiah.format(7500000));

// console.log juga mengenal %s %d %f %o (gaya printf)
console.log("Nama: %s, umur %d", nama, umur);

// struk belanja
const barang: string[] = ["Kopi susu", "Roti bakar", "Air mineral"];
const harga: number[] = [18000, 22500, 5000];
console.log(`${"Barang".padEnd(12)} ${"Harga".padStart(10)}`);
barang.forEach((b, i) => console.log(`${b.padEnd(12)} ${harga[i].toLocaleString("id-ID").padStart(10)}`));
const total: number = harga.reduce((a, b) => a + b, 0);
console.log(`${"TOTAL".padEnd(12)} ${total.toLocaleString("id-ID").padStart(10)}`);
