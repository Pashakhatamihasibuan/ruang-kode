public class Main {
    public static void main(String[] args) {
        int[] a = {70, 85, 60, 90, 75};
        int total = 0;
        for (int i = 0; i < a.length; i++) {
            total += a[i];
        }
        int rata = total / a.length;
        System.out.println("Rata-rata: " + rata);
        for (int i = 0; i < a.length; i++) {
            if (a[i] > rata) {
                System.out.println("a[" + i + "] = " + a[i]);
            }
        }
    }
}
