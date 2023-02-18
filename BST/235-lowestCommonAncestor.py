class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    large = max(p.val, q.val)
    small = min(p.val, q.val)
    while root:
        if root.val > large:  # p, q belong to the left subtree
            root = root.left
        elif root.val < small:  # p, q belong to the right subtree
            root = root.right
        else:  # Now, small <= root.val <= large -> This is the LCA between p and q
            return root
    return None


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    p = TreeNode(0)
    q = TreeNode(3)
    print(lowestCommonAncestor(root, p, q).val)
