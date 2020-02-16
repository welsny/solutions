# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = None

        from collections import deque
        dq = deque([(root, '')])

        while dq:
            n, s = dq.popleft()
            s = chr(97+n.val) + s

            if not n.left and not n.right:
                if not res:
                    res = s
                res = min(res, s)
            if n.left:
                dq.append((n.left, s))
            if n.right:
                dq.append((n.right, s))

        return res
