class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low: int, high: int) -> int:
    sum = 0

    def f(root):
        nonlocal sum
        if not root:
            return
        if low <= root.val <= high:
            sum += root.val

        if root.val > low:
            f(root.left)
        if root.val < high:
            f(root.right)
    f(root)
    return sum



if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    print(rangeSumBST(root, 7, 15))
