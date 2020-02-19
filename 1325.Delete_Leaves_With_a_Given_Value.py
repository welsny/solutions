# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if not node:
                return True
            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None
            if not node.left and not node.right and node.val == target:
                return True

        head = TreeNode(0)
        head.left = root
        dfs(head)
        return head.left