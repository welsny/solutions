#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.convert_tree(root)
        self.counter = defaultdict(int)
        self.dfs(root)

        max_ct = max(self.counter.values())
        return [k for k, ct in self.counter.items() if ct == max_ct]

    def convert_tree(self, node):
        """
        Convert each node's 'val' into it's subtree sum
        """
        if not node:
            return

        if node.left:
            self.convert_tree(node.left)
            node.val += node.left.val
        if node.right:
            self.convert_tree(node.right)
            node.val += node.right.val

    def dfs(self, node):
        if node:
            self.counter[node.val] += 1
            self.dfs(node.left)
            self.dfs(node.right)

