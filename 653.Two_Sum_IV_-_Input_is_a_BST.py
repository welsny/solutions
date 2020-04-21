# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def search(node, target):
            curr = root
            while curr:
                if curr != node and curr.val == target:
                    return True
                elif curr.val > target:
                    curr = curr.left
                else:
                    curr = curr.right
            return False

        stack = [root]
        while stack:
            n = stack.pop()

            if search(n, k-n.val):
                return True

            for child in filter(None, [n.left, n.right]):
                stack.append(child)

        return False
