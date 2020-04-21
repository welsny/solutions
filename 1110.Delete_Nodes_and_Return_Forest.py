# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        to_delete = set(to_delete)
        res = []
        if root.val not in to_delete:
            res.append(root)
        stack = [(root, root.val in to_delete)]
        while stack:
            n, deleted = stack.pop()

            if n.left:
                to_del = n.left.val in to_delete
                stack.append((n.left, to_del))
                if deleted and not to_del:
                    res.append(n.left)
                if to_del:
                    n.left = None

            if n.right:
                to_del = n.right.val in to_delete
                stack.append((n.right, to_del))
                if deleted and not to_del:
                    res.append(n.right)
                if to_del:
                    n.right = None

        return res
