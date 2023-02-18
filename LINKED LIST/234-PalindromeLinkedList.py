class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def palindrome(head):
    slow, fast, prev = head, head, None

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    prev, slow, prev.next = slow, slow.next, None

    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    fast, slow = head, prev

    while slow:
        if fast.val != slow.val: return False
        fast, slow = fast.next, slow.next
    return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(6)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(1)

    print(palindrome(head))
