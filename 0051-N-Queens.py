"""
- backtracking
- intuition: mark all illegal pos after placing a queen
- O(n!), O(n^2)
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        
        def get_condensed_board(board):
            return [''.join(row) for row in board]
        
        def place_queen(board, r, c):
            new_board = [row[:] for row in board]
            new_board[r][c] = "Q"
            # update row
            for i in range(n):
                if i != c:
                    new_board[r][i] = "."
                    
            # update col
            for i in range(n):
                if i != r:
                    new_board[i][c] = "."
            
            # update diag
            DIR = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
            for i, j in DIR:
                rr, cc = r + i, c + j
                while 0 <= rr < n and 0 <= cc < n:
                    new_board[rr][cc] = "."
                    rr += i
                    cc += j
            return new_board
            
        
        def backtrack(i, board):
            if i == n:
                result.append(get_condensed_board(board))
                return
            for c in range(n):
                if board[i][c] == " ":
                    updated_board = place_queen(board, i, c)
                    backtrack(i + 1, updated_board)
            
        
        backtrack(0, [[" "] * n for _ in range(n)])
        return result