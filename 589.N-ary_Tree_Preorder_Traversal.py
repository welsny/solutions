"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        self.res.append(node.val)
        for c in node.children:
            self.dfs(c)

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            n = stack.pop()
            res.append(n.val)
            for c in reversed(n.children):
                stack.append(c)

        return res
