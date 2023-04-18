import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # By using bisect method which bisects the list from root which gives us the left part of the list and right part
    def bstFromPreorder(self, preorder):
        if not preorder: return None
        root = TreeNode(preorder[0])
        i = bisect.bisect(preorder, preorder[0])
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

    # using stack
    def bstFromPreorder1(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()

                last.right = TreeNode(value)
                stack.append(last.right)
        return root


if __name__ == '__main__':
    preorder = [8, 5, 1, 7, 10, 12]
    a = Solution()
    print(a.bstFromPreorder(preorder))
    print(a.bstFromPreorder1(preorder))
