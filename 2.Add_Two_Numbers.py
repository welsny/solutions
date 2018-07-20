#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        curr = None
        next_val = 0

        while l1 or l2:
            if l1:
                next_val += l1.val
                l1 = l1.next
            if l2:
                next_val += l2.val
                l2 = l2.next

            next_node = ListNode(next_val % 10)
            next_val //= 10

            if not head:
                head = next_node
                curr = head
            else:
                curr.next = next_node
                curr = curr.next

        if next_val:
            curr.next = ListNode(1)

        return head

