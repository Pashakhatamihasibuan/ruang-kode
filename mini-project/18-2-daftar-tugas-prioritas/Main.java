import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        PriorityQueue<Tugas> pq = new PriorityQueue<>((a, b) -> a.prioritas - b.prioritas);
        pq.add(new Tugas("Cuci piring", 3));
        pq.add(new Tugas("Kerjakan PR", 1));
        pq.add(new Tugas("Main game", 5));
        pq.add(new Tugas("Belajar ujian", 2));
        while (!pq.isEmpty()) {
            Tugas t = pq.remove();
            System.out.println(t.prioritas + ". " + t.nama);
        }
    }
}

class Tugas {
    String nama;
    int prioritas;
    Tugas(String nama, int prioritas) { this.nama = nama; this.prioritas = prioritas; }
}
