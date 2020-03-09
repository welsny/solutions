# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        verts = defaultdict(
            lambda: defaultdict(list)
        )
        dq = deque([(0, 0, root)])

        while dq:
            x, y, n = dq.popleft()
            verts[x][y].append(n.val)

            if n.left:
                dq.append((x-1, y-1, n.left))
            if n.right:
                dq.append((x+1, y-1, n.right))

        res = []
        for x, d in sorted(verts.items()):
            app = []
            for y, vals in sorted(d.items(), reverse=True):
                app.extend(sorted(vals))
            res.append(app)
        return res
