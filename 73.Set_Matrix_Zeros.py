#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        targ_row = [False]*len(matrix)
        targ_col = [False]*len(matrix[0])

        for i, row in enumerate(matrix):
            for j, elt in enumerate(row):
                if not elt:
                    targ_row[i], targ_col[j] = True, True

        for i, row in enumerate(matrix):
            for j, elt in enumerate(row):
                if targ_row[i] or targ_col[j]:
                    matrix[i][j] = 0

