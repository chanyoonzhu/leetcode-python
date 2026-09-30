"""
- dynamic programming
- O(mn), O(mn) - can be optimized to O(n)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        if obstacleGrid[0][0] != 1: dp[0][0] = 1
        for r in range(M):
            for c in range(N):
                if obstacleGrid[r][c] != 1:
                    if r > 0: dp[r][c] += dp[r-1][c]
                    if c > 0: dp[r][c] += dp[r][c-1]
        return dp[M-1][N-1]