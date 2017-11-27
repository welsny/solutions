#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, node, acc=0):
        if node:
            acc = 10*acc + node.val
            if not node.left and not node.right:
                self.result += acc
            self.dfs(node.left, acc)
            self.dfs(node.right, acc)

