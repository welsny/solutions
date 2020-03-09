# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [(0, None, root)]

        nodes = []
        while stack:
            d, p, n = stack.pop()

            if n.val in [x, y]:
                nodes.append((d, p))

            if n.left:
                stack.append((d+1, n, n.left))
            if n.right:
                stack.append((d+1, n, n.right))

        return nodes[0][0] == nodes[1][0] and nodes[0][1] != nodes[1][1]
