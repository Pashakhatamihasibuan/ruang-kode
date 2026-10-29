import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] harga = {10000, 20000, 30000};
        int[] cadangan = Arrays.copyOf(harga, harga.length);
        diskon(harga);
        System.out.println("harga    = " + Arrays.toString(harga));
        System.out.println("cadangan = " + Arrays.toString(cadangan));
    }

    public static void diskon(int[] a) {
        for (int i = 0; i < a.length; i++) {
            a[i] = a[i] / 2;
        }
    }
}
