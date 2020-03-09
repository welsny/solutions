"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Recursive solution:
        """
        if not root:
            return []

        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        for c in node.children:
            self.dfs(c)
        self.res.append(node.val)

    def postorder(self, root: 'Node') -> List[int]:
        """
        Follow-up: iterative solution w. stack
        """
        if not root:
            return []

        res = []
        stack = [root]
        seen = set()

        while stack:
            if stack[-1] not in seen:
                seen.add(stack[-1])
                # stack.extend(stack[-1].children[::-1])
                for c in reversed(stack[-1].children):
                    stack.append(c)
            else:
                res.append(stack.pop().val)

        return res
