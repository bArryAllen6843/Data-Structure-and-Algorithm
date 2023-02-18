class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []
    queue = [root]
    next_que = []
    level = []
    result = []

    while queue:
        for root in queue:
            level.append(root.data)
            if root.left:
                next_que.append(root.left)
            if root.right:
                next_que.append(root.right)
        result.append(level)
        level = []
        queue = next_que
        next_que = []

    return result


a = Node("a", Node("b", Node("d"), Node("e")),
         Node("c", Node("f"), Node("g")))

print(levelOrder(a))
