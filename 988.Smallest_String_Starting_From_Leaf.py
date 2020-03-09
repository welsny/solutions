# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = None
        dq = deque([(root, '')])

        while dq:
            n, s = dq.popleft()
            s = chr(97+n.val) + s

            if not n.left and not n.right:
                if not res:
                    res = s
                res = min(res, s)

            for child in filter(bool, [n.left, n.right]):
                append((child, s))

        return res
