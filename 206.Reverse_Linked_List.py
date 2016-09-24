#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return prev

        rest = head.next

        head.next = prev

        return self.reverseList(rest, prev=head)

