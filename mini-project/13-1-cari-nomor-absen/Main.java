public class Main {
    public static void main(String[] args) {
        int[] a = {3, 8, 15, 21, 30, 42, 57};
        System.out.println("Ketemu di indeks " + cari(a, 42));
    }

    public static int cari(int[] a, int target) {
        int lo = 0, hi = a.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            System.out.println("cek a[" + mid + "] = " + a[mid]);
            if (a[mid] == target) return mid;
            else if (a[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
