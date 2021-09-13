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
- O(m*n), O(n)
- TLE
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        dp = [0] * len(points[0])
        for line in points:
            # after this loop, dp[i] will be the max for previous lines if next line choosing column i (it bubbles up max value from side to middle)
            for i in range(1, len(line)):
                dp[i] = max(dp[i], dp[i - 1] - 1)
                dp[-i - 1] = max(dp[-i - 1], dp[-i] - 1)
            for i in range(len(line)):
                dp[i] += line[i]
        return max(dp)