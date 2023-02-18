class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(root):
    string = str(root.val)

    if root.left:
        string += "(" + tree2str(root.left) + ")"
    if root.right:
        if not root.left:
            string += "()"
        string += "(" + tree2str(root.right) + ")"
    return string


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(tree2str(root))
