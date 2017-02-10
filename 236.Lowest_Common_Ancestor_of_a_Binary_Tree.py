# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def update(node):
            """
            Removes a node if it does not contain 'p' or 'q'.

            Contains the value of 'Node' after it is updated.
            """

            if not node:
                return None

            node.left = update(node.left)
            node.right = update(node.right)

            if node not in [p, q] and not node.left and not node.right:
                return None

            return node

        update(root)

        search = root
        while search not in [p, q] and not (search.left and search.right):
            if search.left:
                search = search.left
            else:
                search = search.right

        return search

