import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        ArrayIntList list = new ArrayIntList();
        for (int x = 10; x <= 50; x += 10) {
            list.add(x);
        }
        System.out.println(list);
    }
}

class ArrayIntList {
    private int[] data = new int[2];
    private int size = 0;

    public void add(int value) {
        if (size == data.length) {
            data = Arrays.copyOf(data, data.length * 2);
            System.out.println("Kapasitas naik menjadi " + data.length);
        }
        data[size] = value;
        size++;
    }

    public String toString() {
        return Arrays.toString(Arrays.copyOf(data, size)) + " size=" + size + " kapasitas=" + data.length;
    }
}
