"""
- dp (top-down) - knapsack (0/n)
- O(S*n), O(S)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def dp(total):
            if total == 0: return 0
            if total < 0: return float("inf") # easy to miss: need to match exact total
            return min([1 + dp(total - n) for n in coins])
        
        result = dp(amount)
        return result if result < float("inf") else -1

"""
- dp (bottom-up) - knapsack (0/n)
- O(S*n), O(S)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for total in range(1, amount + 1):
            for c in coins:
                if total >= c: # easy to miss
                    dp[total] = min(dp[total], dp[total-c] + 1)
        result = dp[-1]
        return result if result < float("inf") else -1