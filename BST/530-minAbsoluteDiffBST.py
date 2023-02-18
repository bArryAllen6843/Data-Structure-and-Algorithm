class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root):
    def f(node, lo, hi):
        if not node: return hi - lo
        left = f(node.left, lo, node.val)
        right = f(node.right, node.val, hi)
        return min(left, right)

    return f(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print(getMinimumDifference(root))
