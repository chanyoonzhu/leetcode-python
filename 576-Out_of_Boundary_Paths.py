"""
- dynamic programming
- O(mn*maxMove)
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        MOD = 10**9 + 7
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        prev_dp = [[0] * n for _ in range(m)]
        prev_dp[startRow][startColumn] = 1
        result = 0
        for _ in range(maxMove):
            dp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for i, j in DIR:
                        nr, nc = r + i, c + j
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            result = (result + prev_dp[r][c]) % MOD
                        else:
                            dp[nr][nc] = (dp[nr][nc] + prev_dp[r][c]) % MOD
            
            prev_dp = dp
        return result