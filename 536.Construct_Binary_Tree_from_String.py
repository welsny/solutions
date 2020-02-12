#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s: return None

        val = ''
        for char in s:
            if char != '(':
                val += char
            else:
                break

        head = TreeNode(int(val))
        stack = [head]

        for i, char in enumerate(s):
            if i < len(val): continue

            if char == '(':
                val = ''
                while s[i+1] not in '()':
                    val += s[i+1]
                    i += 1

                n = TreeNode(int(val))
                if not stack[-1].left: stack[-1].left = n
                elif not stack[-1].right: stack[-1].right = n
                stack.append(n)

            elif char == ')':
                stack.pop()

        return head

