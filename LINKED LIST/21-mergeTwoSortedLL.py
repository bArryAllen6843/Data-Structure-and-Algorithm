class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    cur = dummy = ListNode(-1)
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


def printList(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next


if __name__ == '__main__':
    # ll1 = ListNode(1, ListNode(2, ListNode(4)))
    # ll2 = ListNode(1, ListNode(3, ListNode(4)))
    ll1 = ListNode(-9, ListNode(3))
    ll2 = ListNode(5, ListNode(7))

    printList(mergeTwoLists(ll1, ll2))
