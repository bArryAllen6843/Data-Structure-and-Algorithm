class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_LL(head):
    def merge(head1, head2):
        prev, curr1, curr2 = None, head1, head2
        while curr2 is not None:
            if curr1.val > curr2.val:
                if prev is None:
                    prev = curr2
                    head1 = prev
                    curr2 = curr2.next
                    prev.next = curr1
                else:
                    prev.next = curr2
                    curr2 = curr2.next
                    prev = prev.next
                    prev.next = curr1
            else:
                if curr1.next is None:
                    curr1.next = curr2
                    break
                else:
                    prev = curr1
                    curr1 = curr1.next
        return head1

    def mergeSort(head):
        slow = head
        fast = head

        if head.next is None: return head
        if head.next.next is None:
            head1 = head
            head2 = head.next
            head.next = None
        else:
            while fast.next is not None and fast.next.next is not None :
                slow, fast = slow.next, fast.next.next
            head1 = head
            head2 = slow.next
            slow.next = None

        head1 = mergeSort(head1)
        head2 = mergeSort(head2)
        return merge(head1, head2)

    if head is None: return head
    return mergeSort(head)


def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(2)

    printLL(head)
    print()
    printLL(sort_LL(head))
