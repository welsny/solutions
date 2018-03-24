#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cts = [set() for i in range(27)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue
                if val in cts[i] | cts[9+j] | cts[18+3*(i//3)+j//3]:
                    print(val, cts)
                    return False
                cts[i].add(val)
                cts[9+j].add(val)
                cts[18+3*(i//3)+j//3].add(val)

        return True

