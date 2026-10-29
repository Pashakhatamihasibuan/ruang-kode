public class Main {
    public static void main(String[] args) {
        for (int n : new int[]{8, 1024}) {
            System.out.println("n=" + n + " linear=" + linear(n)
                + " kuadrat=" + kuadrat(n) + " log=" + logaritma(n));
        }
    }

    static int linear(int n) {
        int c = 0;
        for (int i = 0; i < n; i++) c++;
        return c;
    }

    static int kuadrat(int n) {
        int c = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) c++;
        return c;
    }

    static int logaritma(int n) {
        int c = 0;
        while (n > 1) { n /= 2; c++; }
        return c;
    }
}
