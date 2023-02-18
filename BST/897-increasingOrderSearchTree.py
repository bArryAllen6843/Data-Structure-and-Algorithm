class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# morris inorder traversal
def increasingOrder(node):
    dummy = tail = TreeNode(-1)
    while node:
        if node.left:
            predecessor = node.left
            while predecessor.right:
                predecessor = predecessor.right

            predecessor.right = node
            left, node.left = node.left, None
            node = left
        else:
            tail.right = node
            tail=node
            node = node.right
    return dummy.right


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(1)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)

    print(increasingOrder(root))
