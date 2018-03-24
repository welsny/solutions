#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n%2:
            for i, row in enumerate(matrix[:n//2]):
                for j, val in enumerate(row[:n//2+1]):
                    matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i] = matrix[-j-1][i], matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1]
        else:
            for i, row in enumerate(matrix[:n//2]):
                for j, val in enumerate(row[:n//2]):
                    matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i] = matrix[-j-1][i], matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1]

