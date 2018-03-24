# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head

        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        if not k % length:
            return head

        curr = head
        for i in range(length-k%length-1):
            curr = curr.next
        result = curr.next
        curr.next = None

        curr = result
        while curr.next:
            curr = curr.next
        curr.next = head

        return result

