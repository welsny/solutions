# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        verts = defaultdict(list)
        dq = deque([(0, root)])

        while dq:
            x, n = dq.popleft()
            verts[x].append(n.val)

            if n.left:
                dq.append((x-1, n.left))
            if n.right:
                dq.append((x+1, n.right))

        return [v for k, v in sorted(verts.items())]