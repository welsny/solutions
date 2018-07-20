#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.board, self.n_rows, self.n_cols = board, len(board), len(board[0])
        i, j = click

        neighs = [(a, b) for a in (i-1, i, i+1) for b in (j-1, j, j+1) if 0 <= a < self.n_rows and 0 <= b < self.n_cols]
        neigh_bombs = [(a, b) for (a, b) in neighs if board[a][b] == 'M']

        if board[i][j] == 'M':
            self.board[i][j] = 'X'
        elif neigh_bombs:
            self.board[i][j] = str(len(neigh_bombs))
        else:
            self.board[i][j] = 'B'
            for a, b in neighs:
                if self.board[a][b] == 'E':
                    self.updateBoard(board, [a, b])

        return self.board

