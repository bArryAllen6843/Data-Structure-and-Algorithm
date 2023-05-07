class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        if not root: return None

        if root.val == key:
            if not root.right: return root.left
            if not root.left: return root.right
            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    a = Solution()
    print(a.deleteNode(root, 3))
