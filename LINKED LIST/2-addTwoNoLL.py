class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addLL(l1, l2):
    carry = 0
    ans = p = ListNode(-1)

    while l1 or l2:
        l1data, l2data = l1.val if l1 else 0, l2.val if l2 else 0
        k = l1data + l2data + carry
        n = ListNode(k % 10)
        carry = k // 10
        p.next = n
        p = p.next
        l1 = l1.next
        l2 = l2.next
        if carry:
            p.next = ListNode(carry)
    return ans.next


def printList(node):
    if node is None:
        return
    while node is not None:
        print(node.val, end=" ")
        node = node.next


head = ListNode(3)
head.next = ListNode(3)
head.next.next = ListNode(7)

head1 = ListNode(0)
head1.next = ListNode(4)
head1.next.next = ListNode(2)

printList(head)
print()
printList(head1)
print("\n------------------")
printList(addLL(head, head1))
