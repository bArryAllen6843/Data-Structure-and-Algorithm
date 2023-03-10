class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head):
        if not head: return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head


def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    a = Solution()
    printList(a.removeNodes(head))
