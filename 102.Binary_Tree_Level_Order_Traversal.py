#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        nodes = [root] # A list of nodes on the current level

        while any(nodes):
            result.append([n.val for n in nodes])

            next = []

            for node in nodes:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            nodes = next

        return result

