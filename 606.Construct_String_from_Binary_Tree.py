#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result = ''

        if t:
            result += str(t.val)
            if t.left:
                result += '(' + self.tree2str(t.left) + ')'
            if t.right:
                if not t.left: result += '()'
                result += '(' + self.tree2str(t.right) + ')'

        return result

