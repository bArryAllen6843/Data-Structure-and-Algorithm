class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root):
        if root:
            return 1 + max(self.height(root.left), self.height(root.right))
        return 0


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(1)

    ls = Solution()
    ls.height(root)
    print(ls)
