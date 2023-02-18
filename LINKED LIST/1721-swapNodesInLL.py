class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # swapping nodes from beginning of kth node and from end of kth node
    def swapNodes(self, head, k: int):
        last = head
        length = 0
        while last:
            last = last.next
            length += 1
        b = head
        e = head
        for i in range(k - 1):
            b = b.next
        for i in range(length - k):
            e = e.next
        b.val, e.val = e.val, b.val
        return head


def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    a = Solution()
    printLL(a.swapNodes(head, 2))
