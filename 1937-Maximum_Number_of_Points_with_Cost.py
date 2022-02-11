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
- TLE
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        dp = [0] * N
        
        for r in range(M):
            left_max, right_max = self.buildLeftRightMax(dp)
            dp = [0] * N
            for c in range(N):
                dp[c] = points[r][c] + max(left_max[c], right_max[c])
        return max(dp)
    
    def buildLeftRightMax(self, arr):
        """
        eg. [6,4,2,4,6] -> [6,5,4,5,6]
        """
        N = len(arr)
        cur_max = 0
        left_max, right_max = [0] * N, [0] * N
        for i in range(N):
            cur_max = max(cur_max - 1, arr[i])
            left_max[i] = cur_max
        for i in range(N-1, -1, -1):
            cur_max = max(cur_max - 1, arr[i]) # decrement cur_max by 1 now one cell farther
            right_max[i] = cur_max
        return left_max, right_max