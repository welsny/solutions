#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

# # # # #

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        dq = deque([(root, 1)])
        while dq:
            n, d = dq.popleft()

            if not n.left and not n.right:
                return d
            if n.left:
                dq.append((n.left, d+1))
            if n.right:
                dq.append((n.right, d+1))
