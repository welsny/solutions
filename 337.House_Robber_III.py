# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.rob2(root))

    def rob2(self, node):
        """
        Returns a tuple

        (max rob including this node, max rob exluding this node)
        """
        if not node:
            return 0, 0

        l_rob = self.rob2(node.left)
        r_rob = self.rob2(node.right)
        return node.val + l_rob[1] + r_rob[1], max(l_rob) + max(r_rob)
