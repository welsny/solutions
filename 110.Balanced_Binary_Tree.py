# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, node: TreeNode) -> bool:
        if not node:
            return True

        return abs(self.dfs(node.left) - self.dfs(node.right)) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right)

    def dfs(self, node, depth=0):
        if not node:
            return depth

        return max(self.dfs(node.left, depth+1), self.dfs(node.right, depth+1))
