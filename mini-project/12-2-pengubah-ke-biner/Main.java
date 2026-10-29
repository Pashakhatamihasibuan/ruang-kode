public class Main {
    public static void main(String[] args) {
        System.out.println("13 = " + biner(13));
        System.out.println("6  = " + biner(6));
    }

    public static String biner(int n) {
        if (n < 2) {
            return "" + n;
        }
        return biner(n / 2) + (n % 2);
    }
}
