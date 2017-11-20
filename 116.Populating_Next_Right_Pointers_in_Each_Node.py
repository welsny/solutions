# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        curr = root
        next = curr.left

        while curr:
            if curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = next

# class Solution:
#     # @param root, a tree link node
#     # @return nothing
#     def connect(self, root):
#         curr_layer = [root]
#         next_layer = []

#         if not root:
#             return

#         while curr_layer:
#             for i, node in enumerate(curr_layer):
#                 if i != len(curr_layer) - 1:
#                     node.next = curr_layer[i+1]
#                 if node.left:
#                     next_layer.append(node.left)
#                     next_layer.append(node.right)
#             curr_layer = next_layer
#             next_layer = []

