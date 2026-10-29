class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

front = None
front = ListNode(30, front)
front = ListNode(20, front)
front = ListNode(10, front)
print(front.data)
print(front.next.data)
print(front.next.next.data)
