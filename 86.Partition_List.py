# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1, h2 = ListNode(None), ListNode(None)

        curr = head
        c1, c2 = h1, h2
        while curr:
            if curr.val < x:
                c1.next = curr
                c1 = c1.next
            else:
                c2.next = curr
                c2 = c2.next
            curr = curr.next

        c1.next = h2.next
        c2.next = None
        return h1.next
