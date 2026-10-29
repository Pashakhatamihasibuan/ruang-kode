public class Main {
    public static void main(String[] args) {
        int[] data = {7, 9, 4, 0, 0};
        int size = 3;
        for (int i : new int[]{1, 3, -1}) {
            try {
                System.out.println("get(" + i + ") = " + get(data, size, i));
            } catch (IndexOutOfBoundsException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }

    static int get(int[] data, int size, int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index " + index + " di luar 0.." + (size - 1));
        }
        return data[index];
    }
}
