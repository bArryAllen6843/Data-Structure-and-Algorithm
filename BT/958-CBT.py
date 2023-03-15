class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # simple bfs solution: here append every root.left and root.right in bfs list which already contains root
    # suppose the tree is not a complete BT then what will happen is our bfs list will contain None in between
    # due to None while loop will break when root is None and at the end we will check whether the bfs list contains
    # element after that None if yes then it is not a CBT
    def isCompleteTree(self, root) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    a = Solution()
    print(a.isCompleteTree(root))
