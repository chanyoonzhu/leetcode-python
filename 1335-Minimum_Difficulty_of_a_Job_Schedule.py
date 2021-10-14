"""
- dynamic programming
- O(d*n^2), O(nd) - space can be optimized to n
"""
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d: return -1
        
        dp = [[float("inf")] * (N + 1) for _ in range(d)]
        dp[0][0] = 0
        for i in range(1, N + 1):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i-1])
        dp[0][0] = float("inf") # ?
        
        for di in range(1, d):
            for ni in range(di + 1, N + 1):
                maxx = 0
                for nj in range(ni, 0, -1):
                    maxx = max(jobDifficulty[nj-1], maxx)
                    dp[di][ni] = min(dp[di][ni], dp[di-1][nj-1] + maxx)
        return dp[d-1][N]