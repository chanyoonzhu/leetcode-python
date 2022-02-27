"""
- dynamic programming (top-down)
- O(m*n*n), O(m*n)
- TLE
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        M, N = len(points), len(points[0])
        
        @lru_cache(None)
        def dp(r, c):
            if r < 0: return 0
            return max([points[r][c] - abs(c - cc) + dp(r - 1, cc) for cc in range(N)])
        
        return max([dp(M - 1, n) for n in range(N)])

"""
- dynamic programming (bottom-up)
- O(m*n*n), O(n)
- TLE
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if not points or not points[0]: return 0
        
        M, N = len(points), len(points[0])
        prev = points[0]
        
        for r in range(1, M):
            cur = [0] * N
            for c in range(N):
                cur[c] = max([points[r][c] + prev[cc] - abs(c - cc) for cc in range(N)])
            prev = cur
        
        return max(prev)

"""
- dynamic programming (bottom-up)
- similar: 1014-Best_Sightseeing_Pair
- O(m*n), O(n)
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        M, N  = len(points), len(points[0])
        prev_dp = points[0] # max points at i
        
        for i in range(1, M):
            dp = prev_dp[:] # rolling max of prev_row
            rolling_max = 0
            for j in range(N): # left pass
                rolling_max = max(rolling_max - 1, dp[j])
                dp[j] = max(dp[j], rolling_max)
            rolling_max = 0
            for j in range(N-1, -1, -1): # right pass
                rolling_max = max(rolling_max - 1, dp[j])
                dp[j] = max(dp[j], rolling_max)
            prev_dp = [dp[j] + points[i][j] for j in range(N)]
        return max(prev_dp)