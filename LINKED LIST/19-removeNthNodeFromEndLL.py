class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def removeNthFromEnd(head, n):
    lag, lead = head, head
    cnt = 1

    while lead.next is not None:
        lead, cnt = lead.next, cnt + 1
        if cnt - n > 1:
            lag = lag.next

    if cnt - n == 0:
        return head.next
    else:
        lag.next = lag.next.next
        return head


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next


if __name__ == '__main__':
    head = Node(2, Node(4, Node(5, Node(7, Node(9)))))
    printList(removeNthFromEnd(head, 2))
