from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def avgBT(root):
    avg = []
    q = deque()
    y=0
    q.appendleft(root)
    while q:
        x = q.pop()
        y+=x.val
        if x.left:
            q.appendleft(x.left)
        if x.right:
            q.appendleft(x.right)



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    avgBT(root)
