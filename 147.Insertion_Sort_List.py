#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(float('-inf'))

        while head:
            next = head.next
            curr = result
            while curr.next and head.val > curr.next.val:
                curr = curr.next
            head.next = curr.next
            curr.next = head
            head = next

        return result.next

