"""
- dynamic programming (top-down)
- O(n^2), O(n^2)
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(l, h):
            if l >= h: return 0 # easy to miss: l == h should return 0 because correct guess won't cost money
            return min([x + max(dp(l, x - 1), dp(x + 1, h)) for x in range(l, h + 1)])
        
        return dp(1, n)

"""
- dynamic programming (bottom-up)
- O(n^2), O(n^2)
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float("inf")] * n for _ in range(n)]
    
        for diff in range(n):
            for left in range(n - diff):
                if diff == 0: 
                    dp[left][left] = 0
                else:
                    right = left + diff
                    for k in range(left, right + 1):
                        dp[left][right] = min(dp[left][right], (k + 1) + max(dp[left][k-1] if k > 0 else 0, dp[k+1][right] if k < n-1 else 0))
        return dp[0][n-1]