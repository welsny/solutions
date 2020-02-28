# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        is_unival = True
        for c in filter(None, [node.left, node.right]):
            is_unival &= (self.dfs(c) and c.val == node.val)

        self.res += int(is_unival)
        return is_unival
