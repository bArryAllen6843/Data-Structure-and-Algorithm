class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        d = ListNode(-1)
        d.next = head
        p, c = d, head

        while c:
            while c.next and c.val == c.next.val:
                c = c.next

            if p.next == c:
                p, c = p.next, c.next
            else:
                p.next = c.next
                c = p.next
        return d.next


def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)

    a = Solution()
    printLL(a.deleteDuplicates(head))
