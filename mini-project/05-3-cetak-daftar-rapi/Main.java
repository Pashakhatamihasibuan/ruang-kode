public class Main {
    public static void main(String[] args) {
        int n = 5;
        System.out.print("[1");
        for (int i = 2; i <= n; i++) {
            System.out.print(", " + i);
        }
        System.out.println("]");
    }
}
