"""
- dynamic programming
- O(mn), O(mn)
"""
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        MOD = 10**9 + 7
        M, N = len(board), len(board[0])
        ways = [[0] * N for _ in range(M)]
        dp = [[0] * N for _ in range(M)]
        ways[M-1][N-1] = 1
        
        for col in range(N-2, -1, -1):
            c = board[M-1][col]
            if c == 'X':
                ways[M-1][col] = 0
            else:
                dp[M-1][col] = ord(c) - ord('0') + dp[M-1][col + 1] if ways[M-1][col + 1] else 0 # easy to miss: if ways[M-1][col + 1] else 0
                ways[M-1][col] = (ways[M-1][col] + ways[M-1][col + 1]) % MOD
        
        for row in range(M-2, -1, -1):
            c = board[row][N-1]
            if c == 'X':
                ways[row][N-1] = 0
            else:
                dp[row][N-1] = ord(c) - ord('0') + dp[row+1][N-1] if ways[row+1][N-1] else 0
                ways[row][N-1] = (ways[row][N-1] + ways[row+1][N-1]) % MOD
                
        for row in range(M-2, -1, -1):
            for col in range(N-2, -1, -1):
                c = board[row][col]
                if c == 'X':
                    ways[row][col] = 0
                else:
                    cur_num = ord(c) - ord('0') if c != 'E' else 0 # easy to miss: c != 'E'
                    max_prev = max(dp[row+1][col], dp[row][col+1], dp[row+1][col+1])
                    if dp[row+1][col] == max_prev: 
                        ways[row][col] = (ways[row][col] + ways[row+1][col]) % MOD
                    if dp[row][col+1] == max_prev:
                        ways[row][col] = (ways[row][col] + ways[row][col+1]) % MOD
                    if dp[row+1][col+1] == max_prev:
                        ways[row][col] = (ways[row][col] + ways[row+1][col+1]) % MOD
                    dp[row][col] = cur_num + max_prev if ways[row][col] else 0
        
        return [dp[0][0], ways[0][0]]
                
        