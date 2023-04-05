class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None: return TreeNode(val);
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val);
        else:
            root.left = self.insertIntoBST(root.left, val);
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    a = Solution()
    print(a.insertIntoBST(root, 5))
