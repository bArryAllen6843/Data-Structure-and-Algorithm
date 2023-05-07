class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head) -> int:
        fast=slow=head
        maxValue=0

        # Get middle of linked list
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next

        #  Reverse second part of linked list
        prev,cur=None,slow
        while cur:
            cur.next,prev,cur=prev,cur,cur.next

        # Get max sum of pairs
        while prev:
            maxValue=max(maxValue, head.val+prev.val)
            prev=prev.next
            head=head.next
        return maxValue


if __name__ == '__main__':
    head=ListNode(5)
    head.next=ListNode(4)
    head.next.next=ListNode(2)
    head.next.next.next=ListNode(1)

    a=Solution()
    print(a.pairSum(head))