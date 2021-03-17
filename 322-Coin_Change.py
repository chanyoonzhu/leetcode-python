class Solution:
    """
    - dp (bottom-up)
    - O(S*n), O(S)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        
        for i in range(1, len(dp)):
            min_coins = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    min_coins = min(min_coins, dp[i - coin] + 1)
            dp[i] = min_coins
            
        return dp[-1] if dp[-1] != float("inf") else -1
    
    """
    - dp (top-down)
    - O(S*n), O(S)
    - time limit exceeded
    """
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