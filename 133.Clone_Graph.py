"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        seen = set([node])
        stack = [node]
        while stack:
            n = stack.pop()

            n.clone = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in seen:
                    seen.add(neigh)
                    stack.append(neigh)

        for n in seen:
            n.clone.neighbors = [neigh.clone for neigh in n.neighbors]

        return node.clone
