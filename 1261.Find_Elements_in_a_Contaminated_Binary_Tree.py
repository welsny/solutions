# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.elts = set()
        self.dfs(root)

    def dfs(self, node, val=0):
        if node:
            self.elts.add(val)
            self.dfs(node.left, 2*val+1)
            self.dfs(node.right, 2*val+2)

    def find(self, target: int) -> bool:
        return target in self.elts


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
