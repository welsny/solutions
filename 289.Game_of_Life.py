#!/usr/bin/env python3

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        n, m = len(board), len(board[0])
        def adjs(i, j):
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1),
                         (i, j-1), (i, j+1),
                         (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if 0 <= x < n and 0 <= y < m:
                    yield board[x][y]

        temp = [[0 for _ in range(m)] for _ in range(n)]
        for i, row in enumerate(board):
            for j, alive in enumerate(row):
                if (alive and sum(adjs(i, j)) in [2, 3]) or (not alive and sum(adjs(i, j)) == 3):
                    temp[i][j] = 1

        for i, row in enumerate(temp):
            for j, state in enumerate(row):
                board[i][j] = state
