class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def detectCycle(head):
    s, f = head, head
    while f and f.next:
        s = s.next
        f = f.next.next
        if f is s:
            f = head
            break
    if f and f.next:
        while f is not s:
            f = f.next
            s = s.next
        return f
    return None


root = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
root.next.next.next.next = root.next

print(detectCycle(root).val)
