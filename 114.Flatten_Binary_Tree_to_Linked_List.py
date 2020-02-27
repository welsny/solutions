# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    First approach, recursion:
    """

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten2(root)

    def flatten2(self, node):
        joins = []
        if node.left:
            joins.append(self.flatten2(node.left))
        if node.right:
            joins.append(self.flatten2(node.right))

        if not joins:
            return node, node

        node.left = None

        prev = node
        for start, end in joins:
            prev.right = start
            prev = end
        return node, end

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Second approach, stack:
    """
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [None]

        curr = root
        while curr:
            if curr.left:
                if curr.right:
                    stack.append(curr.right)
                curr.right = curr.left
            elif not curr.right:
                curr.right = stack.pop()

            curr.left = None
            curr = curr.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        head = TreeNode(None)
        head.right = root

        stack = [root]
        curr = head
        while stack:
            n = stack.pop()

            curr.left, curr.right = None, n
            curr = curr.right

            for c in filter(bool, [n.right, n.left]):
                stack.append(c)
