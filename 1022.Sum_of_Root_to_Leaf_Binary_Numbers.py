# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(0, root)]
        res = 0

        while stack:
            v, n = stack.pop()
            v = 2*v + n.val

            # if n.left:
            #     stack.append((v, n.left))
            # if n.right:
            #     stack.append((v, n.right))
            for child in filter(bool, [n.left, n.right]):
                stack.append((v, child))

            if not n.left and not n.right:
                res += v

        return res
