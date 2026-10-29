class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

front = ListNode(4, ListNode(9, ListNode(2, ListNode(7))))
count, total, maks = 0, 0, front.data
cur = front
while cur is not None:
    count += 1
    total += cur.data
    if cur.data > maks:
        maks = cur.data
    cur = cur.next
print(f"count={count} total={total} maks={maks}")
