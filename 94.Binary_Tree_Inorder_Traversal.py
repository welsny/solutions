#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.inorder(root)
        return self.result

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.result.append(node.val)
            self.inorder(node.right)

