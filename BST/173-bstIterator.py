class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    def next(self) -> int:
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    obj = BSTIterator(root)
    param_1 = obj.next()
    print(param_1)
    param_3 = obj.next()
    print(param_3)
    param_2 = obj.hasNext()
    print(param_2)
    param_4 = obj.next()
    print(param_4)
    param_5 = obj.hasNext()
    print(param_5)
