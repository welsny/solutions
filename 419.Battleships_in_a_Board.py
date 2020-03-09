class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])

        ct = 0
        for i, row in enumerate(board):
            for j, ship in enumerate(row):
                if ship == '.':
                    continue

                adj_ct = sum(1 for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)] if 0 <= x < n and 0 <= y < m and board[x][y] == 'X')
                if not adj_ct:
                    ct += 1
                if adj_ct == 1 and ((i < n-1 and board[i+1][j] == 'X') or (j < m-1 and board[i][j+1] == 'X')):
                    ct += 1

        return ct
