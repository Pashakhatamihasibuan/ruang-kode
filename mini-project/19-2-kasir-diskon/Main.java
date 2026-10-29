import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> harga = List.of(30000, 75000, 120000, 45000, 60000);
        int total = harga.stream()
                .filter(x -> x > 50000)
                .map(x -> x * 80 / 100)
                .reduce(0, Integer::sum);
        System.out.println("Total diskon: " + total);
    }
}
