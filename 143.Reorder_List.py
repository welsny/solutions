#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        print([n.val for n in nodes])

        # O(n) runtime, O(n) space

        def node_inds(n=len(nodes)):
            for i in range(n//2):
                yield i
                yield n-i-1
            if n%2:
                yield i//2

        print(list(node_inds()))

        curr = ListNode(None)
        for n in node_inds():
            curr.next = nodes[n]
            curr = curr.next
        curr.next = None

