"""
- dynamic programming (top-down): knapsack 0/1
- O(l*m*n), O(l*m*n)
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        str_len = len(strs)
        counts = [[s.count("0"), s.count("1")] for s in strs]
              
        @lru_cache(None)
        def dp(i, m, n):
            if m < 0 or n < 0: return float("-inf")
            if i == len(strs):
                return 0
            else:
                m_cost, n_cost = counts[i]
                return max(dp(i + 1, m - m_cost, n - n_cost) + 1, dp(i + 1, m, n))
                
        return dp(0, m, n)

"""
- dynamic programming (bottom-up with space optimized): knapsack
- O(l*m*n), O(l*m*n)
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0] * (n + 1) for _ in range(m + 1)] # only need previous strs to calculate the dp for current str
        
        for s in strs:
            count = Counter(s)
            zeros, ones = count['0'], count['1']

            for i in range(m, zeros - 1, -1): # need to iterate from right to left because state function needs value with smaller indexes
                for j in range(n, ones - 1, -1): # need to iterate from right to left
                    dp[i][j] = max(1 + dp[i - zeros][j - ones], dp[i][j])

        return dp[m][n]