# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    First solution uses class methods, which is the default for LC even though the syntax is uglier.
    """
    def maxProduct(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.root = root
        self.dfs(root)
        self.dfs2(root)
        return self.res % (10**9 + 7)

    def dfs(self, node):
        if not node:
            return 0
        node.sum = node.val + self.dfs(node.left) + self.dfs(node.right)
        return node.sum

    def dfs2(self, node):
        if not node:
            return
        self.res = max(self.res, node.sum*(self.root.sum-node.sum))
        self.dfs2(node.left)
        self.dfs2(node.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    IMO cleaner syntax, but performance on LC client is worse in terms of speed & memory usage.
    """
    def maxProduct(self, root: TreeNode) -> int:
        def dfs(node=root):
            if not node:
                return 0
            node.sum = node.val + dfs(node.left) + dfs(node.right)
            return node.sum

        def dfs2(node=root):
            if not node:
                return
            self.res = max(self.res, node.sum*(root.sum-node.sum))
            dfs2(node.left)
            dfs2(node.right)

        self.res = float('-inf')
        dfs()
        dfs2()
        return self.res % (10**9 + 7)
