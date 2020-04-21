# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [
            (root, float('-inf'), float('inf'))
        ]

        while stack:
            n, min_bound, max_bound = stack.pop()

            if not min_bound < n.val < max_bound:
                return False

            if n.left:
                stack.append((n.left, min_bound, n.val))
            if n.right:
                stack.append((n.right, n.val, max_bound))

        return True
