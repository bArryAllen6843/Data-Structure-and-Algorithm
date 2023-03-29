class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy=jump=ListNode(0)
        dummy.next=l=r=head

        while True:
            count=0
            while r and count<k:
                r=r.next
                count+=1

            if count==k:
                prev,curr=r,l
                for _ in range(k):
                    curr.next,curr,prev=prev,curr.next,curr
                # connect two k-groups
                jump.next,jump,l=prev,l,r
            else:
                return dummy.next

def printList(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next

if __name__ == '__main__':
    k=2
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(4)
    head.next.next.next.next=ListNode(5)

    a=Solution()
    printList(a.reverseKGroup(head,k))