public class Main {
    public static void main(String[] args) {
        // 1. for: jumlah putaran sudah pasti
        for (int i = 1; i <= 3; i++) {
            System.out.println("for: i = " + i);
        }

        // 2. while: kondisi dicek DULU, bisa 0 kali
        int n = 3;
        while (n > 0) {
            System.out.println("while: n = " + n);
            n--;
        }

        // 3. do-while: badan jalan DULU, kondisi dicek di akhir
        int x = 10;
        do {
            System.out.println("do-while: x = " + x + " (tetap jalan sekali)");
            x++;
        } while (x < 5);

        // 4. for-each: menelusuri isi koleksi tanpa indeks
        String[] buah = {"apel", "jeruk", "mangga"};
        for (String b : buah) {
            System.out.println("for-each: " + b);
        }

        // 5. bersarang: loop di dalam loop
        for (int baris = 1; baris <= 2; baris++) {
            String isi = "";
            for (int kolom = 1; kolom <= 3; kolom++) {
                isi += (baris * kolom) + " ";
            }
            System.out.println("nested: " + isi.trim());
        }

        // 6. break: keluar dari loop lebih awal
        String hasil = "";
        for (int i = 1; i <= 10; i++) {
            if (i == 4) break;
            hasil += i + " ";
        }
        System.out.println("break: " + hasil.trim());

        // 7. continue: lewati sisa badan untuk putaran ini saja
        hasil = "";
        for (int i = 1; i <= 6; i++) {
            if (i % 2 == 0) continue;
            hasil += i + " ";
        }
        System.out.println("continue: " + hasil.trim());
    }
}
