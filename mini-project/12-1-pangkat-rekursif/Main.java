public class Main {
    public static void main(String[] args) {
        System.out.println("2^5 = " + pangkat(2, 5));
        System.out.println("3^4 = " + pangkat(3, 4));
    }

    public static int pangkat(int a, int b) {
        if (b == 0) {
            return 1;
        }
        return a * pangkat(a, b - 1);
    }
}
