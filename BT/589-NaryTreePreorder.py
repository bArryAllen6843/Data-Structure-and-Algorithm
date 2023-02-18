class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):
    if root is None:
        return []

    stack = [root]
    ans = []
    while stack:
        x = stack.pop()
        ans.append(x.val)
        stack.extend(x.children[::-1])
    return ans


root = Node(1)
root.children = Node(3)
root.children = Node(2)
root.children = Node(4)
root.children.children = Node(5)
root.children.children = Node(6)
print(preorder(root))
