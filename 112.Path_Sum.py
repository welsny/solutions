#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        sums = []

        def dfs(root, curr=0):
            if not root.left and not root.right:
                sums.append(curr+root.val)
                return

            if root.left:
                dfs(root.left, curr+root.val)
            if root.right:
                dfs(root.right, curr+root.val)

        dfs(root)
        return sum in sums
