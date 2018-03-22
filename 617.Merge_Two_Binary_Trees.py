#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            result = TreeNode(t1.val + t2.val)
            result.left, result.right = self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)
            return result

        return t1 or t2

