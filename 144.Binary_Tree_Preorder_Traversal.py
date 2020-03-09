# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node:
            self.res.append(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

        return res
