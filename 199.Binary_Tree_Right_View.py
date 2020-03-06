#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 'distance' parameter represents distance from right

        # Store buckets for each level of the tree, and keep track of the rightmost node for each level (i.e. the one with the least 'score' distance)
        min_node = {}

        def dfs(node, depth=0, distance=0):
            if not node:
                return
            if depth not in min_node or min_node[depth][1] > distance:
                min_node[depth] = (node, distance)

            dfs(node.right, depth+1, 2*distance)
            dfs(node.left, depth+1, 2*distance + 1)

        dfs(root)

        result = []

        i = 0
        while i in min_node:
            result.append(min_node[i][0].val)
            i += 1

        return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Better solution with Level-order traversal
    """
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        curr = [root]
        while any(curr):
            result.append(curr[-1].val)
            next = []
            for n in curr:
                if n.left: next.append(n.left)
                if n.right: next.append(n.right)
            curr = next
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    """
    Use BFS which is slightly more space efficient:
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        dq = deque([(0, root)])
        while root and dq:
            d, n = dq.popleft()
            if len(res) <= d:
                res.append(n.val)

            res[d] = n.val
            for c in filter(None, [n.left, n.right]):
                dq.append((d+1, c))

        return res
