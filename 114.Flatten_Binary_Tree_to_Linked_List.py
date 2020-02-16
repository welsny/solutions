# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten2(root)

    def flatten2(self, node):
        joins = []
        if node.left:
            joins.append(self.flatten2(node.left))
        if node.right:
            joins.append(self.flatten2(node.right))

        if not joins:
            return node, node
        
        node.left = None

        prev = node
        for start, end in joins:
            prev.right = start
            prev = end
        
        return node, end
            