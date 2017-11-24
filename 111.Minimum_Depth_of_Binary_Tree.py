#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import numpy as np

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        nodes = [root]
        depth = 1

        while True:
            next = []

            for node in nodes:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            nodes, depth = next, depth+1

