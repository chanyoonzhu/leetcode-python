"""
- dynamic programming (top-down): knapsack 0/1
- O(l*m*n), O(l*m*n)
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        N = len(strs)
        counts = [[s.count("0"), s.count("1")] for s in strs]
        
        @lru_cache(None)
        def dp(i, m, n):
            if m < 0 or n < 0: return float("-inf")
            if i == -1: return 0
            count0, count1 = counts[i]
            return max(dp(i - 1, m, n), dp(i - 1, m - count0, n - count1) + 1)
        
        return dp(N - 1, m, n)

"""
- dynamic programming (bottom-up with space optimized): knapsack (0/1)
- O(l*m*n), O(l*m*n)
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        N = len(strs)
        counts = [[s.count("0"), s.count("1")] for s in strs]
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(N):
            count0, count1 = counts[i]
            for mi in range(m - count0, - 1, -1):
                for ni in range(n - count1, - 1, -1):
                    dp[mi+count0][ni+count1] = max(dp[mi+count0][ni+count1], dp[mi][ni] + 1)
        return dp[m][n]