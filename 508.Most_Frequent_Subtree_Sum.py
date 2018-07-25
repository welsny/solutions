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
    """
    Initial solution - March 2018
    """
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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

class Solution(object):
    """
    More direct solution - July 2018
    """
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        self.cts = Counter()
        self.dfs(root)

        max_val = max(self.cts.values())
        return [s for s, ct in self.cts.items() if ct == max_val]

    def dfs(self, node):
        """
        Recursive DFS - adds subtree sum count to `self.cts`
        :returns: integer value of `node`'s subtree sum.
        """
        if node:
            sum = node.val + self.dfs(node.left) + self.dfs(node.right)
            self.cts[sum] += 1
            return sum

        return 0

