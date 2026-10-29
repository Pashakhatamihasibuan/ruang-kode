public class Main {
    public static void main(String[] args) {
        ListNode front = new ListNode(4, new ListNode(9, new ListNode(2, new ListNode(7, null))));
        int count = 0, total = 0, maks = front.data;
        ListNode cur = front;
        while (cur != null) {
            count++;
            total += cur.data;
            if (cur.data > maks) maks = cur.data;
            cur = cur.next;
        }
        System.out.println("count=" + count + " total=" + total + " maks=" + maks);
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
