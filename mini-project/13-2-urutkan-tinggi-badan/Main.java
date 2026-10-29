import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] a = {165, 150, 172, 158};
        for (int i = 0; i < a.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[min]) min = j;
            }
            int tmp = a[i];
            a[i] = a[min];
            a[min] = tmp;
            System.out.println("Putaran " + (i + 1) + ": " + Arrays.toString(a));
        }
    }
}
