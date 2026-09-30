"""
- 2D array
- O(mn), O(mn)
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        copy = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                copy[i][j] = board[i][j]
        for i in range(M):
            for j in range(N):
                self.cell_next(copy, board, i, j, M, N)

    def cell_next(self, prev_board, board, r, c, m, n):
        DIR = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        live = dead = 0
        for i, j in DIR:
            nr, nc = r + i, c + j
            if 0 <= nr < m and 0 <= nc < n:
                if prev_board[nr][nc] == 1:
                    live += 1
                else:
                    dead += 1
        if prev_board[r][c] == 1 and (live < 2 or live > 3):
            board[r][c] = 0
        elif prev_board[r][c] == 0 and live == 3:
            board[r][c] = 1

"""
- 2D array
- key: use -1 and 2 to mark flipped number, then iterate again to transform the final number
- O(mn), O(1)
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                self.cell_next(board, i, j, M, N)
        for i in range(M):
            for j in range(N):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

    def cell_next(self, board, r, c, m, n):
        DIR = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        live = dead = 0
        for i, j in DIR:
            nr, nc = r + i, c + j
            if 0 <= nr < m and 0 <= nc < n:
                if board[nr][nc] in (1, -1): # key: need to test -1 (previous 1 changed to 0) as well
                    live += 1
                else:
                    dead += 1
        if board[r][c] == 1 and (live < 2 or live > 3):
            board[r][c] = -1
        elif board[r][c] == 0 and live == 3:
            board[r][c] = 2

"""
- todo: infinite sparse board
"""