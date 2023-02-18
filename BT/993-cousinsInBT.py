from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def cousins(root, x, y):
    res = []
    # que = deque([root, None, 0])

    def dfs(node, parent, depth):
        if not node:
            return
        if node.val == x or node.val == y:
            res.append((parent, depth))
        dfs(node.left, node, depth + 1)
        dfs(node.right, node, depth + 1)

    dfs(root, None, 0)

    node_x, node_y = res
    return node_x[0] != node_y[0] and node_x[1] == node_y[1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    a = 4
    b = 3
    print(cousins(root, a, b))
