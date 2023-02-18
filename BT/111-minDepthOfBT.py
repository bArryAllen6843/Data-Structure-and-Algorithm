class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        if root:
            if root.left is None:
                return 1 + self.minDepth(root.right)
            if root.right is None:
                return 1 + self.minDepth(root.left)

            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        return 0


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(1)

ls = Solution()
ls.minDepth(root)
print(ls)
