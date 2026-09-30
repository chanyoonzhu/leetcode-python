"""
- dfs
- intuition: start from 'O' on the border, recursively search escapable regions connected to it using dfs
- O(mn), O(1)
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        M, N = len(board), len(board[0])
        
        for r in range(M):
            for c in range(N):
                if (r == 0 or r == M-1 or c == 0 or c == N-1) and board[r][c] == 'O':
                    self.dfs(board, r, c)
        
        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O': # 'O's that cannot escape
                    board[r][c] = 'X'
                elif board[r][c] == 'E': # 'O's that escaped
                    board[r][c] = 'O'
                    
    def dfs(self, board, r, c):
        board[r][c] = 'E' # mark as escaped
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + i, c + j
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'O':
                self.dfs(board, nr, nc)

"""
- bfs
"""
                
        