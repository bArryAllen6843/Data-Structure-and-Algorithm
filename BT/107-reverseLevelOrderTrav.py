class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def levelOrderBottom(root):
    res = []
    dfs(root, 0, res)
    return res


def dfs(root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level + 1)].append(root.val)
        dfs(root.left, level + 1, res)
        dfs(root.right, level + 1, res)


if __name__ == '__main__':

    a = Node("a", Node("b", Node("d"), Node("e")),
             Node("c", Node("f"), Node("g")))

    print(levelOrderBottom(a))
