P={}
# ---------- 1. kapan for / while / do-while ----------
P['pilih']={
'java':'''public class Main {
    public static void main(String[] args) {
        // FOR: jumlah pengulangan sudah diketahui (5 hari)
        int total = 0;
        for (int hari = 1; hari <= 5; hari++) {
            total += 10000;
        }
        System.out.println("Tabungan 5 hari: " + total);

        // WHILE: berhenti saat kondisi tercapai, jumlah putaran belum diketahui
        int saldo = 0, minggu = 0;
        while (saldo < 75000) {
            saldo += 20000;
            minggu++;
        }
        System.out.println("Target tercapai di minggu ke-" + minggu);

        // DO-WHILE: badan loop dijalankan minimal sekali
        int[] pilihanUser = {2, 1, 0};
        int i = 0, pilihan;
        do {
            pilihan = pilihanUser[i++];
            System.out.println("Menu dipilih: " + pilihan);
        } while (pilihan != 0);

        // FOR-EACH: membaca setiap isi koleksi
        String[] kota = {"Medan", "Bandung", "Makassar"};
        for (String k : kota) {
            System.out.println("Kirim ke " + k);
        }
    }
}''',
'python':'''# FOR: jumlah pengulangan sudah diketahui (5 hari)
total = 0
for hari in range(1, 6):
    total += 10000
print("Tabungan 5 hari:", total)

# WHILE: berhenti saat kondisi tercapai, jumlah putaran belum diketahui
saldo, minggu = 0, 0
while saldo < 75000:
    saldo += 20000
    minggu += 1
print(f"Target tercapai di minggu ke-{minggu}")

# Python tidak punya do-while: pakai while True + break
pilihan_user = [2, 1, 0]
i = 0
while True:
    pilihan = pilihan_user[i]
    i += 1
    print("Menu dipilih:", pilihan)
    if pilihan == 0:
        break

# FOR atas koleksi: membaca setiap isi list
for k in ["Medan", "Bandung", "Makassar"]:
    print("Kirim ke", k)''',
'js':'''// FOR: jumlah pengulangan sudah diketahui (5 hari)
let total = 0;
for (let hari = 1; hari <= 5; hari++) {
  total += 10000;
}
console.log("Tabungan 5 hari:", total);

// WHILE: berhenti saat kondisi tercapai, jumlah putaran belum diketahui
let saldo = 0, minggu = 0;
while (saldo < 75000) {
  saldo += 20000;
  minggu++;
}
console.log(`Target tercapai di minggu ke-${minggu}`);

// DO-WHILE: badan loop dijalankan minimal sekali
const pilihanUser = [2, 1, 0];
let i = 0, pilihan;
do {
  pilihan = pilihanUser[i++];
  console.log("Menu dipilih:", pilihan);
} while (pilihan !== 0);

// FOR...OF: membaca setiap isi array
for (const k of ["Medan", "Bandung", "Makassar"]) {
  console.log("Kirim ke", k);
}''',
'ts':'''// FOR: jumlah pengulangan sudah diketahui (5 hari)
let total: number = 0;
for (let hari = 1; hari <= 5; hari++) {
  total += 10000;
}
console.log("Tabungan 5 hari:", total);

// WHILE: berhenti saat kondisi tercapai
let saldo: number = 0;
let minggu: number = 0;
while (saldo < 75000) {
  saldo += 20000;
  minggu++;
}
console.log(`Target tercapai di minggu ke-${minggu}`);

// DO-WHILE: badan loop dijalankan minimal sekali
const pilihanUser: number[] = [2, 1, 0];
let i = 0;
let pilihan: number;
do {
  pilihan = pilihanUser[i++];
  console.log("Menu dipilih:", pilihan);
} while (pilihan !== 0);

// FOR...OF: membaca setiap isi array bertipe string[]
const kota: string[] = ["Medan", "Bandung", "Makassar"];
for (const k of kota) {
  console.log("Kirim ke", k);
}'''}
# ---------- 2. fibonacci ----------
P['fib']={
'java':'''public class Main {
    public static void main(String[] args) {
        // FOR: n suku pertama (jumlah putaran diketahui)
        int n = 10;
        long a = 0, b = 1;
        StringBuilder deret = new StringBuilder();
        for (int i = 0; i < n; i++) {
            deret.append(a).append(" ");
            long berikut = a + b;
            a = b;
            b = berikut;
        }
        System.out.println("10 suku pertama: " + deret.toString().trim());

        // WHILE: semua suku di bawah 100 (jumlah putaran belum diketahui)
        a = 0; b = 1;
        int banyak = 0;
        while (a < 100) {
            banyak++;
            long berikut = a + b;
            a = b;
            b = berikut;
        }
        System.out.println("Banyak suku di bawah 100: " + banyak);
    }
}''',
'python':'''# FOR: n suku pertama (jumlah putaran diketahui)
n = 10
a, b = 0, 1
deret = []
for _ in range(n):
    deret.append(a)
    a, b = b, a + b
print("10 suku pertama:", *deret)

# WHILE: semua suku di bawah 100 (jumlah putaran belum diketahui)
a, b = 0, 1
banyak = 0
while a < 100:
    banyak += 1
    a, b = b, a + b
print("Banyak suku di bawah 100:", banyak)''',
'js':'''// FOR: n suku pertama (jumlah putaran diketahui)
const n = 10;
let a = 0, b = 1;
const deret = [];
for (let i = 0; i < n; i++) {
  deret.push(a);
  [a, b] = [b, a + b];
}
console.log("10 suku pertama:", deret.join(" "));

// WHILE: semua suku di bawah 100 (jumlah putaran belum diketahui)
a = 0; b = 1;
let banyak = 0;
while (a < 100) {
  banyak++;
  [a, b] = [b, a + b];
}
console.log("Banyak suku di bawah 100:", banyak);''',
'ts':'''function fibonacci(n: number): number[] {
  const deret: number[] = [];
  let a = 0, b = 1;
  for (let i = 0; i < n; i++) {   // FOR: n sudah diketahui
    deret.push(a);
    [a, b] = [b, a + b];
  }
  return deret;
}

function banyakSukuDiBawah(batas: number): number {
  let a = 0, b = 1, banyak = 0;
  while (a < batas) {             // WHILE: berhenti saat melewati batas
    banyak++;
    [a, b] = [b, a + b];
  }
  return banyak;
}

console.log("10 suku pertama:", fibonacci(10).join(" "));
console.log("Banyak suku di bawah 100:", banyakSukuDiBawah(100));'''}
# ---------- 3. bubble sort ----------
P['bubble']={
'java':'''import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] nilai = {64, 25, 12, 22, 11};
        int n = nilai.length;
        boolean adaTukar = true;
        int putaran = 0;
        // WHILE luar: berhenti jika satu putaran tidak ada pertukaran
        while (adaTukar) {
            adaTukar = false;
            putaran++;
            // FOR dalam: bandingkan pasangan bersebelahan
            for (int j = 0; j < n - putaran; j++) {
                if (nilai[j] > nilai[j + 1]) {
                    int sementara = nilai[j];
                    nilai[j] = nilai[j + 1];
                    nilai[j + 1] = sementara;
                    adaTukar = true;
                }
            }
            System.out.println("Putaran " + putaran + ": " + Arrays.toString(nilai));
        }
        System.out.println("Terurut: " + Arrays.toString(nilai));
    }
}''',
'python':'''nilai = [64, 25, 12, 22, 11]
n = len(nilai)
ada_tukar = True
putaran = 0
# WHILE luar: berhenti jika satu putaran tidak ada pertukaran
while ada_tukar:
    ada_tukar = False
    putaran += 1
    # FOR dalam: bandingkan pasangan bersebelahan
    for j in range(n - putaran):
        if nilai[j] > nilai[j + 1]:
            nilai[j], nilai[j + 1] = nilai[j + 1], nilai[j]
            ada_tukar = True
    print(f"Putaran {putaran}: {nilai}")
print("Terurut:", nilai)''',
'js':'''const nilai = [64, 25, 12, 22, 11];
const n = nilai.length;
let adaTukar = true;
let putaran = 0;
// WHILE luar: berhenti jika satu putaran tidak ada pertukaran
while (adaTukar) {
  adaTukar = false;
  putaran++;
  // FOR dalam: bandingkan pasangan bersebelahan
  for (let j = 0; j < n - putaran; j++) {
    if (nilai[j] > nilai[j + 1]) {
      [nilai[j], nilai[j + 1]] = [nilai[j + 1], nilai[j]];
      adaTukar = true;
    }
  }
  console.log(`Putaran ${putaran}: [${nilai.join(", ")}]`);
}
console.log(`Terurut: [${nilai.join(", ")}]`);''',
'ts':'''function bubbleSort(data: number[]): number[] {
  const a = [...data];           // salin agar data asli tidak berubah
  let adaTukar = true;
  let putaran = 0;
  while (adaTukar) {             // WHILE: belum tahu butuh berapa putaran
    adaTukar = false;
    putaran++;
    for (let j = 0; j < a.length - putaran; j++) {   // FOR: batas jelas
      if (a[j] > a[j + 1]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        adaTukar = true;
      }
    }
    console.log(`Putaran ${putaran}: [${a.join(", ")}]`);
  }
  return a;
}

const hasil: number[] = bubbleSort([64, 25, 12, 22, 11]);
console.log(`Terurut: [${hasil.join(", ")}]`);'''}
# ---------- 4. fizzbuzz & prima ----------
P['prima']={
'java':'''public class Main {
    public static void main(String[] args) {
        // FizzBuzz: FOR karena rentangnya jelas (1 sampai 15)
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 15; i++) {
            if (i % 15 == 0) sb.append("FizzBuzz ");
            else if (i % 3 == 0) sb.append("Fizz ");
            else if (i % 5 == 0) sb.append("Buzz ");
            else sb.append(i).append(" ");
        }
        System.out.println(sb.toString().trim());

        // Bilangan prima 2..30: FOR bersarang + break
        StringBuilder prima = new StringBuilder();
        for (int x = 2; x <= 30; x++) {
            boolean isPrima = true;
            for (int d = 2; d * d <= x; d++) {
                if (x % d == 0) {
                    isPrima = false;
                    break;          // tidak perlu cek pembagi lain
                }
            }
            if (isPrima) prima.append(x).append(" ");
        }
        System.out.println("Prima: " + prima.toString().trim());
    }
}''',
'python':'''# FizzBuzz: FOR karena rentangnya jelas (1 sampai 15)
hasil = []
for i in range(1, 16):
    if i % 15 == 0:
        hasil.append("FizzBuzz")
    elif i % 3 == 0:
        hasil.append("Fizz")
    elif i % 5 == 0:
        hasil.append("Buzz")
    else:
        hasil.append(str(i))
print(" ".join(hasil))

# Bilangan prima 2..30: FOR bersarang + break
prima = []
for x in range(2, 31):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            break           # tidak perlu cek pembagi lain
    else:
        prima.append(x)     # for-else: jalan jika loop tidak di-break
print("Prima:", *prima)''',
'js':'''// FizzBuzz: FOR karena rentangnya jelas (1 sampai 15)
const hasil = [];
for (let i = 1; i <= 15; i++) {
  if (i % 15 === 0) hasil.push("FizzBuzz");
  else if (i % 3 === 0) hasil.push("Fizz");
  else if (i % 5 === 0) hasil.push("Buzz");
  else hasil.push(i);
}
console.log(hasil.join(" "));

// Bilangan prima 2..30: FOR bersarang + break
const prima = [];
for (let x = 2; x <= 30; x++) {
  let isPrima = true;
  for (let d = 2; d * d <= x; d++) {
    if (x % d === 0) {
      isPrima = false;
      break;          // tidak perlu cek pembagi lain
    }
  }
  if (isPrima) prima.push(x);
}
console.log("Prima:", prima.join(" "));''',
'ts':'''function fizzBuzz(n: number): string[] {
  const hasil: string[] = [];
  for (let i = 1; i <= n; i++) {            // FOR: rentang jelas
    if (i % 15 === 0) hasil.push("FizzBuzz");
    else if (i % 3 === 0) hasil.push("Fizz");
    else if (i % 5 === 0) hasil.push("Buzz");
    else hasil.push(String(i));
  }
  return hasil;
}

function isPrima(x: number): boolean {
  if (x < 2) return false;
  for (let d = 2; d * d <= x; d++) {
    if (x % d === 0) return false;          // keluar lebih awal
  }
  return true;
}

console.log(fizzBuzz(15).join(" "));
const prima: number[] = [];
for (let x = 2; x <= 30; x++) if (isPrima(x)) prima.push(x);
console.log("Prima:", prima.join(" "));'''}
# ---------- 5. faktorial, digit, palindrom ----------
P['digit']={
'java':'''public class Main {
    public static void main(String[] args) {
        // Faktorial: FOR, jumlah perkalian = n
        int n = 5;
        long faktorial = 1;
        for (int i = 2; i <= n; i++) {
            faktorial *= i;
        }
        System.out.println(n + "! = " + faktorial);

        // Jumlah digit: WHILE, banyak digit belum diketahui
        int angka = 90417, sisa = angka, jumlah = 0;
        while (sisa > 0) {
            jumlah += sisa % 10;   // ambil digit terakhir
            sisa /= 10;            // buang digit terakhir
        }
        System.out.println("Jumlah digit " + angka + " = " + jumlah);

        // Palindrom: WHILE dua penunjuk bergerak ke tengah
        String kata = "katak";
        int kiri = 0, kanan = kata.length() - 1;
        boolean palindrom = true;
        while (kiri < kanan) {
            if (kata.charAt(kiri) != kata.charAt(kanan)) {
                palindrom = false;
                break;
            }
            kiri++;
            kanan--;
        }
        System.out.println(kata + " palindrom? " + palindrom);
    }
}''',
'python':'''# Faktorial: FOR, jumlah perkalian = n
n = 5
faktorial = 1
for i in range(2, n + 1):
    faktorial *= i
print(f"{n}! = {faktorial}")

# Jumlah digit: WHILE, banyak digit belum diketahui
angka = 90417
sisa, jumlah = angka, 0
while sisa > 0:
    jumlah += sisa % 10   # ambil digit terakhir
    sisa //= 10           # buang digit terakhir
print(f"Jumlah digit {angka} = {jumlah}")

# Palindrom: WHILE dua penunjuk bergerak ke tengah
kata = "katak"
kiri, kanan = 0, len(kata) - 1
palindrom = True
while kiri < kanan:
    if kata[kiri] != kata[kanan]:
        palindrom = False
        break
    kiri += 1
    kanan -= 1
print(f"{kata} palindrom? {palindrom}")''',
'js':'''// Faktorial: FOR, jumlah perkalian = n
const n = 5;
let faktorial = 1;
for (let i = 2; i <= n; i++) {
  faktorial *= i;
}
console.log(`${n}! = ${faktorial}`);

// Jumlah digit: WHILE, banyak digit belum diketahui
const angka = 90417;
let sisa = angka, jumlah = 0;
while (sisa > 0) {
  jumlah += sisa % 10;          // ambil digit terakhir
  sisa = Math.floor(sisa / 10); // buang digit terakhir
}
console.log(`Jumlah digit ${angka} = ${jumlah}`);

// Palindrom: WHILE dua penunjuk bergerak ke tengah
const kata = "katak";
let kiri = 0, kanan = kata.length - 1, palindrom = true;
while (kiri < kanan) {
  if (kata[kiri] !== kata[kanan]) { palindrom = false; break; }
  kiri++;
  kanan--;
}
console.log(`${kata} palindrom? ${palindrom}`);''',
'ts':'''function faktorial(n: number): number {
  let hasil = 1;
  for (let i = 2; i <= n; i++) hasil *= i;   // FOR: n kali
  return hasil;
}

function jumlahDigit(angka: number): number {
  let sisa = angka, jumlah = 0;
  while (sisa > 0) {                          // WHILE: digit belum diketahui
    jumlah += sisa % 10;
    sisa = Math.floor(sisa / 10);
  }
  return jumlah;
}

function isPalindrom(kata: string): boolean {
  let kiri = 0, kanan = kata.length - 1;
  while (kiri < kanan) {                      // WHILE: dua penunjuk
    if (kata[kiri] !== kata[kanan]) return false;
    kiri++;
    kanan--;
  }
  return true;
}

console.log(`5! = ${faktorial(5)}`);
console.log(`Jumlah digit 90417 = ${jumlahDigit(90417)}`);
console.log(`katak palindrom? ${isPalindrom("katak")}`);'''}
# ---------- 6. binary search ----------
P['binser']={
'java':'''public class Main {
    public static void main(String[] args) {
        int[] harga = {5000, 8000, 12000, 15000, 20000, 27000, 35000};
        int cari = 20000;
        int kiri = 0, kanan = harga.length - 1, langkah = 0, posisi = -1;
        // WHILE: berhenti saat ketemu atau ruang pencarian habis
        while (kiri <= kanan) {
            langkah++;
            int tengah = (kiri + kanan) / 2;
            System.out.println("Langkah " + langkah + ": cek indeks " + tengah + " (" + harga[tengah] + ")");
            if (harga[tengah] == cari) {
                posisi = tengah;
                break;
            } else if (harga[tengah] < cari) {
                kiri = tengah + 1;
            } else {
                kanan = tengah - 1;
            }
        }
        System.out.println("Ketemu di indeks " + posisi + " setelah " + langkah + " langkah");
    }
}''',
'python':'''harga = [5000, 8000, 12000, 15000, 20000, 27000, 35000]
cari = 20000
kiri, kanan = 0, len(harga) - 1
langkah, posisi = 0, -1
# WHILE: berhenti saat ketemu atau ruang pencarian habis
while kiri <= kanan:
    langkah += 1
    tengah = (kiri + kanan) // 2
    print(f"Langkah {langkah}: cek indeks {tengah} ({harga[tengah]})")
    if harga[tengah] == cari:
        posisi = tengah
        break
    elif harga[tengah] < cari:
        kiri = tengah + 1
    else:
        kanan = tengah - 1
print(f"Ketemu di indeks {posisi} setelah {langkah} langkah")''',
'js':'''const harga = [5000, 8000, 12000, 15000, 20000, 27000, 35000];
const cari = 20000;
let kiri = 0, kanan = harga.length - 1, langkah = 0, posisi = -1;
// WHILE: berhenti saat ketemu atau ruang pencarian habis
while (kiri <= kanan) {
  langkah++;
  const tengah = Math.floor((kiri + kanan) / 2);
  console.log(`Langkah ${langkah}: cek indeks ${tengah} (${harga[tengah]})`);
  if (harga[tengah] === cari) { posisi = tengah; break; }
  else if (harga[tengah] < cari) kiri = tengah + 1;
  else kanan = tengah - 1;
}
console.log(`Ketemu di indeks ${posisi} setelah ${langkah} langkah`);''',
'ts':'''function binarySearch(data: number[], cari: number): number {
  let kiri = 0, kanan = data.length - 1, langkah = 0;
  while (kiri <= kanan) {                     // WHILE: berhenti saat ketemu/habis
    langkah++;
    const tengah = Math.floor((kiri + kanan) / 2);
    console.log(`Langkah ${langkah}: cek indeks ${tengah} (${data[tengah]})`);
    if (data[tengah] === cari) return tengah;
    if (data[tengah] < cari) kiri = tengah + 1;
    else kanan = tengah - 1;
  }
  return -1;
}

const harga: number[] = [5000, 8000, 12000, 15000, 20000, 27000, 35000];
console.log(`Ketemu di indeks ${binarySearch(harga, 20000)}`);'''}
