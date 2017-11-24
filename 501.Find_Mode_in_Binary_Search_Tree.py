#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter, deque

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        cts = Counter()
        def dfs(node):
            if not node:
                return
            cts[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        max_ct = max(cts.values())
        return [val for val, ct in cts.items() if ct == max_ct]

        # if not root:
        #     return []

        # cts = Counter()

        # nodes = deque([root])
        # while nodes:            
        #     node = nodes.popleft()
        #         cts[node.val] += 1
        #     if node.left:
        #         nodes.append(node.left)
        #     if node.right:
        #         nodes.append(node.right)

        # max_ct = max(cts.values())
        # return [val for val, ct in cts.items() if ct == max_ct]

