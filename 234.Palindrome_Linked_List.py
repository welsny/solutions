#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        prev = None

        curr = head
        while True:
            curr.prev = prev
            if not curr.next:
                break
            prev = curr
            curr = curr.next

        while head:
            if head.val != curr.val:
                return False
            head = head.next
            curr = curr.prev

        return True
