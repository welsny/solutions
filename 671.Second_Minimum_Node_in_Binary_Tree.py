#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min, self.min2 = float('Inf'), float('Inf')
        self.dfs(root)
        return -1 if self.min2 == float('Inf') else self.min2

    def dfs(self, node):
        if node:
            self.min2 = min(sorted([node.val, self.min, self.min2])[1:])
            self.min = min(self.min, node.val)

            self.dfs(node.left)
            self.dfs(node.right)

