# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import numpy as np

class Solution:
    """
    Original approach from 2018 -- level order traversal:
    """
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []

        nodes = [root]
        while any(nodes):
            result.append(float(np.mean([node.val for node in nodes])))
            next = []

            for node in nodes:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            nodes = next
        return result

    """
    Use any search (this case DFS). This uses slightly less memory, but with messier syntax:
    """
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        levels = []

        stack = [(0, root)]
        while stack:
            d, n = stack.pop()

            if len(levels) <= d:
                levels.append([0, 0])

            levels[d][0] += n.val
            levels[d][1] += 1

            if n.left:
                stack.append((d+1, n.left))
            if n.right:
                stack.append((d+1, n.right))

        return [s/ct for s, ct in levels]
