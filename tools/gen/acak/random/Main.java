import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random acak = new Random();

        // 1. Desimal acak: 0.0 sampai KURANG DARI 1.0
        double r = Math.random();
        System.out.printf("desimal: %.4f%n", r);

        // 2. Dadu 1..6: nextInt(6) memberi 0..5, lalu ditambah 1
        System.out.print("5 dadu :");
        for (int i = 0; i < 5; i++) {
            System.out.print(" " + (acak.nextInt(6) + 1));
        }
        System.out.println();

        // 3. Rentang bebas bawah..atas (kedua batas ikut)
        int bawah = 10, atas = 20;
        System.out.println("10..20 : " + (acak.nextInt(atas - bawah + 1) + bawah));

        // 4. Lempar dadu sampai keluar angka 6
        int lemparan = 0, hasil = 0;
        while (hasil != 6) {
            hasil = acak.nextInt(6) + 1;
            lemparan++;
        }
        System.out.println("dapat 6 setelah " + lemparan + " lemparan");

        // 5. Memilih satu isi array dan mengocok list
        String[] menu = {"soto", "bakso", "gado-gado", "nasi goreng"};
        System.out.println("menu   : " + menu[acak.nextInt(menu.length)]);
        List<Integer> kartu = new ArrayList<>(List.of(1, 2, 3, 4, 5));
        Collections.shuffle(kartu, acak);
        System.out.println("kocok  : " + kartu);

        // 6. Seed sama menghasilkan urutan yang sama (berguna untuk pengujian)
        Random a = new Random(42), b = new Random(42);
        boolean sama = true;
        for (int i = 0; i < 5; i++) {
            if (a.nextInt(100) != b.nextInt(100)) sama = false;
        }
        System.out.println("seed 42 dua kali, urutan sama: " + sama);
    }
}
