#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.levels = defaultdict(list)
        self.dfs(root)
        return max(pos[-1]-pos[0]+1 for pos in self.levels.values())

    def dfs(self, root):
        def dfs(node, pos=0, level=0):
            if node:
                dfs(node.left, 2*pos, level+1)
                self.levels[level].append(pos)
                dfs(node.right, 2*pos+1, level+1)
        dfs(root)

