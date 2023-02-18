class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return None
        f = head
        length = 1
        while f.next:
            f = f.next
            length += 1

        k = k % length
        f.next = head

        temp = head
        for i in range(length - 1 - k):
            temp = temp.next

        answer = temp.next
        temp.next = None
        return answer


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
    printLL(a.rotateRight(head, 2))
