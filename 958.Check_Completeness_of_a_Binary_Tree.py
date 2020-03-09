# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        level, curr = 0, [(0, root)]
        
        while curr:
            next = []
            for i, n in curr:
                if n.left:
                    next.append((2*i, n.left))
                if n.right:
                    next.append((2*i+1, n.right))

            n = len(curr)
            if n == 2**level:
                level += 1
                if not next:
                    return True
                curr = next
                continue

            if next and len(curr) != 2**level:
                return False

            return sum(i for i, n in curr) == (n*(n-1))//2