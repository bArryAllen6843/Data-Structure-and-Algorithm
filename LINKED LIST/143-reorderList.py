class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):

        if not head: return None
        f, s = head, head
        while f.next and f.next.next:
            f, s = f.next.next, s.next

        prev = None
        curr = s.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        s.next = None

        head1, head2 = head, prev
        ans=head1
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
        return ans


def printList(node):
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
    printList(a.reorderList(head))
