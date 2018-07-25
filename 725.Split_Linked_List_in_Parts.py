#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr, list_len = root, 0

        while curr:
            curr, list_len = curr.next, list_len + 1

        section_size, remainder = list_len//k, list_len%k

        curr = root
        result = [[] for i in range(k)]
        for i in result:
            for j in range(section_size + int(remainder > 0)):
                i.append(curr.val)
                curr = curr and curr.next
            remainder -= 1

        return result
