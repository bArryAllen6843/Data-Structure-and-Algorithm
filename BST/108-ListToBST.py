class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    n = len(nums)
    if not n:
        return None
    mid = n // 2
    return TreeNode(nums[mid], sortedArrayToBST(nums[:mid]), sortedArrayToBST(nums[mid + 1:]))


A = [-10, -3, 0, 5, 9]
print(sortedArrayToBST(A))
