class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


inomap = None
post = None


def buildTree(inorder, postorder):
    n = len(inorder)
    global inomap, post
    post = postorder
    inomap = {el: i for i, el in enumerate(inorder)}
    return f(0, n - 1, 0, n - 1)


def f(poststart, postend, instart, inend):
    inoidx = inomap[post[postend]]
    l = inoidx - instart
    r = inend - inoidx

    root = TreeNode(post[postend])
    root.left = f(poststart, postend-r-1, instart, inoidx - 1) if l else None
    root.right = f(poststart + l, postend - 1, inoidx + 1, inend) if r else None
    return root


if __name__ == '__main__':
    postOrder = ['9', '15', '7', '20', '3']

    inOrder = ['9', '3', '15', '20', '7']
    buildTree(inOrder,postOrder)
