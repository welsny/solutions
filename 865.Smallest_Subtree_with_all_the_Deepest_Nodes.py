# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    """
    First attempt -- iterative and recursive hybrid approach:
    """
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nodes = defaultdict(set)

        stack = [(root, 0)]
        while stack:
            n, d = stack.pop()

            nodes[d].add(n)
            if n.left:
                stack.append((n.left, d+1))
            if n.right:
                stack.append((n.right, d+1))

        self.deepest = nodes[max(nodes)]

        self.max_depth = 0
        self.res = root
        self.dfs(root)
        return self.res

    def dfs(self, node, d=0):
        if not node:
            return set()

        l_desc = self.dfs(node.left, d+1)
        r_desc = self.dfs(node.right, d+1)

        descs = set([node]) | l_desc | r_desc
        if d > self.max_depth and (descs & self.deepest) == self.deepest:
            self.max_depth = d
            self.res = node
        return descs


# # # # #


from collections import defaultdict


class Solution:
    """
    Second approach which commits to the iterative approach. It is slower!
    """
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nodes = defaultdict(set)

        stack = [(root, 0)]
        while stack:
            n, d = stack.pop()

            nodes[d].add(n)
            if n.left:
                stack.append((n.left, d+1))
            if n.right:
                stack.append((n.right, d+1))

        descs = defaultdict(set)
        descs[None] = set()

        max_depth, res = 0, root
        deepest = nodes[max(nodes)]

        stack = [(root, 0)]
        while stack:
            n, d = stack.pop()

            nodes[d].add(n)

            children = [c for c in [n.left, n.right] if c]

            if not all(c in descs for c in children):
                stack.append((n, d))
                for c in children:
                    stack.append((c, d+1))
            else:
                descs[n] = set([n]) | descs[n.left] | descs[n.right]
                if d > max_depth and (descs[n] & deepest) == deepest:
                    max_depth, res = d, n

        return res
