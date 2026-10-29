import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<List<Integer>> tabel = new ArrayList<>();
        for (int i = 0; i < 5; i++) tabel.add(new ArrayList<>());
        for (int k : new int[]{12, 7, 9, 3, 15}) {
            tabel.get(k % 5).add(k);
        }
        for (int i = 0; i < 5; i++) {
            String tanda = tabel.get(i).size() > 1 ? "  <- collision" : "";
            System.out.println("[" + i + "] " + tabel.get(i) + tanda);
        }
    }
}
