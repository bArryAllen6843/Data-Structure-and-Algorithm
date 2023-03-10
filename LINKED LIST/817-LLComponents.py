class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head, nums) -> int:
        s = set(nums)
        connections = 0
        while head:
            if head.val in s and (head.next == None or head.next.val not in s):
                connections += 1
            head = head.next
        return connections


if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    nums = [0, 1, 3]
    a = Solution()
    print(a.numComponents(head, nums))
