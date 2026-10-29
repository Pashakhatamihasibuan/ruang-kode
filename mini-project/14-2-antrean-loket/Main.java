import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Queue<String> q = new LinkedList<>();
        for (String n : new String[]{"Ani", "Budi", "Cici", "Dodi"}) {
            q.add(n);
        }
        while (!q.isEmpty()) {
            String orang = q.remove();
            System.out.println("Melayani " + orang + ", sisa " + q);
        }
    }
}
