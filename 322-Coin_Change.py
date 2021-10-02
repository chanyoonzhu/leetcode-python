"""
- dp (bottom-up)
- O(S*n), O(S)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        
        for c in coins:
            for i in range(amount + 1 - c):
                dp[i + c] = min(dp[i] + 1, dp[i + c])
        return dp[-1] if dp[-1] < float("inf") else -1
        
"""
- dp (top-down)
- O(S*n), O(S)
- time limit exceeded
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        
        def dfs(dp, total):
            if dp[total] != float("inf"):
                return dp[total]
            min_coin = min([dfs(dp, total - coin) + 1 for coin in coins if total - coin >= 0] + [dp[total]])
            dp[total] = min_coin
            return min_coin
        
        dfs(dp, amount)
        
        return dp[-1] if dp[-1] != float("inf") else -1

"""
- dp (top-down) - with cache
- O(S*n), O(S)
"""
class Solution:
    def coinChange(self, coins, amount):
        INF = float("inf")
        @lru_cache(None)
        def dp(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            ans = INF
            for m in coins:
                if dp(n-m) >= 0:
                    ans = min(ans, 1 + dp(n-m))
            return ans
        
        return dp(amount) if dp(amount) < INF else -1