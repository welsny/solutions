# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0

        l_sum, r_sum = self.dfs(node.left), self.dfs(node.right)

        self.res = max(
            self.res,
            node.val,
            node.val+l_sum,
            node.val+r_sum,
            node.val+l_sum+r_sum
        )

        return node.val + max(l_sum, r_sum, 0)
