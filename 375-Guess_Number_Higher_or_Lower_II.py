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
        dp = [[0] * n for _ in range(n)]
        
        for diff in range(1, n + 1):
            for l in range(n - diff):
                h = l + diff
                dp[l][h] = float("inf")
                for x in range(l, h + 1):
                    dp[l][h] = min(dp[l][h], x + 1 + max(dp[l][max(l, x - 1)], dp[min(h, x + 1)][h])) # easy to miss: x - 1, x + 1 can fall out of dp's index range
        return dp[0][n - 1]