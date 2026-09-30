
"""
- dynamic programming
- O(kn^2), O(kn)
 * dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
 * dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
 * dp[0, j] = 0; 0 transactions makes 0 profit
 * dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        N = len(prices)
        dp = [[0] * N for _ in range(k + 1)]
        if N == 0: return 0
        
        for i in range(1, k + 1): # when i == 0, maxprofit = 0
            for j in range(1, N): # when j == 0, maxprofit = 0
                # not selling at j
                dp[i][j] = max(dp[i][j], dp[i][j-1])
                # selliing at j when buying at p
                for p in range(j):
                    dp[i][j] = max(dp[i][j], prices[j] - prices[p] + dp[i-1][p])
        return dp[k][N - 1]
        
"""
- dynamic programming
- O(kn), O(kn)
* dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
*          = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        N = len(prices)
        dp = [[0] * N for _ in range(k + 1)]
        if N == 0: return 0
        
        for i in range(1, k + 1):
            localMax = dp[i - 1][0] - prices[0]
            for j in range(1, N):
                dp[i][j] = max(dp[i][j-1],  prices[j] + localMax)
                localMax = max(localMax, dp[i-1][j] - prices[j])
        return dp[k][N - 1]