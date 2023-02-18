class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        dp = head
        while dp and dp.next:
            if dp.val == dp.next.val:
                dp.next = dp.next.next
            else:
                dp = dp.next
        return head


def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    a = Solution()
    printLL(a.deleteDuplicates(head))
