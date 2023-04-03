class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        # If root is None then either lh or rh will be True
        # at the end when lh=True and rh=True it will return 2 to the last called function
        # and value of that lh or rh will be 2
        if root is None:
            return True

        lh = self.isBalanced(root.left)
        if lh == 0:
            return 0

        rh = self.isBalanced(root.right)
        if rh == 0:
            return 0

        if abs(lh - rh) > 1:
            return 0

        else:
            return 1 + max(lh, rh)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(4)

    a = Solution()
    print(a.isBalanced(root))
