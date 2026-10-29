public class Main {
    public static void main(String[] args) {
        Rekening r = new Rekening();
        System.out.println(r.setor(50000));
        System.out.println(r.tarik(80000));
        System.out.println(r.tarik(20000));
        System.out.println("Saldo: " + r.getSaldo());
    }
}

class Rekening {
    private int saldo;

    public boolean setor(int x) {
        if (x <= 0) return false;
        saldo += x;
        return true;
    }

    public boolean tarik(int x) {
        if (x <= 0 || x > saldo) return false;
        saldo -= x;
        return true;
    }

    public int getSaldo() {
        return saldo;
    }
}
