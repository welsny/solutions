#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.sums = defaultdict(int)
        total = self.subtree_sum(root)
        if self.sums[total] == 1: del(self.sums[total])

        return bool(not total%2 and total//2 in self.sums)

    def subtree_sum(self, node):
        if node:
            s = self.subtree_sum(node.left) + node.val + self.subtree_sum(node.right)
            self.sums[s] += 1
            return s

        return 0

