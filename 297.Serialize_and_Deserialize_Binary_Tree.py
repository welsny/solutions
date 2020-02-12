#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return '{}'

        result = {}

        dq = deque([(0, root)])
        while dq:
            i, node = dq.popleft()

            if node.left: dq.append([2*i+1, node.left])
            if node.right: dq.append([2*i+2, node.right])

            result[i] = node.val

        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = {i: TreeNode(val) for i, val in eval(data).items()}

        for i, node in nodes.items():
            if node:
                node.left = nodes.get(2*i+1)
                node.right = nodes.get(2*i+2)

        return nodes.get(0, [])

