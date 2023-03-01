class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        m = left
        n = right
        if not head or m == n: return head
        p = dummy = ListNode(-1)
        dummy.next = head
        for i in range(m - 1):
            p = p.next
        tail = p.next

        for i in range(n - m):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next


def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    left = 2
    right = 4
    a = Solution()
    print_list(a.reverseBetween(head, left, right))
