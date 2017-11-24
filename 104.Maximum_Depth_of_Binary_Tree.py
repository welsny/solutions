#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root, depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return depth

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

