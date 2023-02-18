class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if not head: return head
        if not head.next: return head

        prev, curr = None, head
        ans = head.next

        while curr and curr.next:
            a = curr.next

            if prev: prev.next = a
            curr.next, a.next = a.next, curr
            prev, curr = curr, curr.next
        return ans


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
    printLL(a.swapPairs(head))
