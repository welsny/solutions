#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head

        curr = head
        next = head.next
        while next:
            if curr.val == next.val:
                curr.next, next = next.next, next.next
            else:
                curr, next = next, next.next

        return head

