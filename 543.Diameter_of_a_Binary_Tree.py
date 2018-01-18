#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, node):
        """
        Returns the node's maximum depth and updates our result for longest diameter
        """
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        diam = 0
        if left:
            diam += left
        if right:
            diam += right

        self.result = max(self.result, diam)

        return max(left, right) + 1

