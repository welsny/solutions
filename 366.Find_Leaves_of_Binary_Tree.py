"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import defaultdict

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        if not root:
            return []

        self.res = defaultdict(list)
        self.dfs(root)

        # Python 3.8 -- insertion order of dict maintained.
        return list(self.res.values())

    def dfs(self, node):
        if not node:
            return -1

        leaf = 1 + max(self.dfs(node.left), self.dfs(node.right))
        self.res[leaf].append(node.val)

        return leaf
