class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    i = 0
    n = None

    def kthSmallest(self, root, k: int) -> int:
        if root:
            global i, n
            self.kthSmallest(root.left, k)
            self.i += 1
            if self.i == k:
                self.n = root.val
            elif self.i < k:
                self.kthSmallest(root.right, k)
            return self.n


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    a = Solution()
    print(a.kthSmallest(root, 3))
