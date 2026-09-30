class Solution:

    """
    - dp - wrong answer: 5+2 and 2+5 are counted twice
    """
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(1, len(dp)):
            for coin in coins:
                dp[i] += dp[i - coin]
        
        return dp[-1]
    
    """
    - dp (bottom-up)
    - O(S*n), O(S)
    """
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins: # using coin in the outer loop guarantees that one combination only calculated once
            for i in range(coin, len(dp)):
                dp[i] += dp[i - coin]
        
        return dp[-1]