"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head
        while curr:
            curr.copy = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            curr.copy.next = curr.next and curr.next.copy
            curr.copy.random = curr.random and curr.random.copy
            curr = curr.next

        return head.copy
