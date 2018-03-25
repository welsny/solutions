#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]

        while nodes:
            next = []
            for node in nodes:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if not next:
                return nodes[0].val
            nodes = next

