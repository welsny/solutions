# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def make_node(left, right):
            node = TreeNode(0)
            node.left, node.right = left, right
            return node

        trees = defaultdict(list)
        trees[1] = [TreeNode(0)]

        for i in range(3, N+1):
            # This syntax doesn't work?
            # trees[i] = [make_node(l, r) for l in trees[j] for r in trees[i-j-1] for j in range(1, i)]

            for j in range(1, i):
                trees[i].extend(
                    [make_node(l, r) for l in trees[j] for r in trees[i-j-1]]
                )

        return trees[N]

