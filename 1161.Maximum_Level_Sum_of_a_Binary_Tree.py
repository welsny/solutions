# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = mx = 0
        level, curr = 1, [root]
        while curr:
            s = sum(n.val for n in curr)
            if s > mx:
                res, mx = level, s

            next = []
            for n in curr:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)

            level += 1
            curr = next

        return res
