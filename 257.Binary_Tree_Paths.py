#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        result = []
        def dfs(root, path=[]):
            if not root.left and not root.right:
                result.append("->".join(map(str, path + [root.val])))

            if root.left:
                dfs(root.left, path + [root.val])
            if root.right:
                dfs(root.right, path + [root.val])

        dfs(root)
        return result

