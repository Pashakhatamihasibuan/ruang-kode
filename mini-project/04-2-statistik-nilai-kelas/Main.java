public class Main {
    public static void main(String[] args) {
        int[] nilai = {78, 92, 65, 88, 70};
        int total = 0;
        int maks = nilai[0];
        for (int n : nilai) {
            total += n;
            if (n > maks) {
                maks = n;
            }
        }
        System.out.println("Total     : " + total);
        System.out.println("Rata-rata : " + total / nilai.length);
        System.out.println("Tertinggi : " + maks);
    }
}
