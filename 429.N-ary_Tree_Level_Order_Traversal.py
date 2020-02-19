"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        curr = [root]

        while curr:
            next = []
            res.append([n.val for n in curr])
            for n in curr:
                next.extend(n.children)
            curr = next

        return res
