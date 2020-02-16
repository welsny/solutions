"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = [None]

        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
            elif not curr.next:
                next = stack.pop()
                curr.next = next

            curr.child = None
            if curr.next:
                curr.next.prev = curr
            curr = curr.next

        return head