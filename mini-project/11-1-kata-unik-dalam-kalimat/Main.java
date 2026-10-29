import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        String kalimat = "saya suka kopi dan saya suka teh";
        Set<String> unik = new TreeSet<>();
        for (String kata : kalimat.split(" ")) {
            unik.add(kata);
        }
        System.out.println(unik);
        System.out.println("Jumlah kata unik: " + unik.size());
    }
}
