class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertSort(head):
    dummy = ListNode(0)
    dummy.next = head

    while head and head.next:
        if head.val > head.next.val:
            nodeToInsert = head.next
            nodeToInsertPre = dummy
            while nodeToInsertPre.next.val < nodeToInsertPre.val:
                nodeToInsertPre = nodeToInsertPre.next

            head.next = nodeToInsert.next
            nodeToInsert.next = nodeToInsertPre.next
            nodeToInsertPre.next = nodeToInsert

        else:
            head = head.next
    return dummy.next


def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(1)

    printLL(head)
    print()
    printLL(insertSort(head))
