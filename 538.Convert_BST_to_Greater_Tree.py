#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.s = 0
        self.dfs(root)
        return root

    def dfs(self, node):
        if node:
            node.right and self.dfs(node.right)
            node.val = self.s = self.s + node.val
            node.left and self.dfs(node.left)

