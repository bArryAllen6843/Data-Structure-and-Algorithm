class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root) -> None:
    curr = root
    while curr:
        if curr.left is not None:
            p = curr.left
            while p.right is not None:
                p = p.right
            p.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    print(flatten(root))
