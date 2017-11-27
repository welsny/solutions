#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(root, sum)
        return self.result

    def dfs(self, node, sum, path=[]):
        if node:
            sum, path = sum-node.val, path+[node.val]
            self.dfs(node.left, sum, path)
            self.dfs(node.right, sum, path)
            if not node.left and not node.right and not sum:
                self.result.append(path)

