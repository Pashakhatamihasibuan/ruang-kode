public class Main {
    public static void main(String[] args) {
        ListNode front = null;
        front = new ListNode(30, front);
        front = new ListNode(20, front);
        front = new ListNode(10, front);
        System.out.println(front.data);
        System.out.println(front.next.data);
        System.out.println(front.next.next.data);
    }
}

class ListNode {
    int data;
    ListNode next;
    ListNode(int data, ListNode next) {
        this.data = data;
        this.next = next;
    }
}
