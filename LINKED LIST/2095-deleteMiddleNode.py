class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):
        dummy = prev = ListNode(123)
        slow = fast = head
        prev.next = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(1)
    head.next.next=ListNode(1)
    head.next.next.next=ListNode(1)

    a=Solution()
    printList(a.deleteMiddle(head))