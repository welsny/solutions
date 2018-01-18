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
        self.min, self.min2 = None, None
        self.dfs(root)
        return self.min2 if self.min2 is not None else -1

    def dfs(self, node):
        if not node:
            return
        if self.min is None:
            self.min = node.val
        elif self.min != node.val and self.min2 is None:
            self.min = min(self.min, node.val)
            self.min2 = max(self.min, node.val)
        elif self.min < node.val < self.min2:
            self.min2 = node.val
        elif node.val < self.min:
            self.min, self.min2 = node.val, self.min

        self.dfs(node.left)
        self.dfs(node.right)
