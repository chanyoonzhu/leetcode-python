"""
- dynamic programming (bottom-up)
- O(n), O(n) - can be optimized to O(1)
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n == 1: return k
        if n == 2: return k * k
        
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        
        """
        intuition:
        num_ways(i) = num_ways_diff(i) + num_ways_same(i)
                    = num_ways(i-1) * (k-1) + num_ways_diff(i-1)
                    = num_ways(i-1) * (k-1) + num_ways(i-2) * (k-1)   
                    = (num_ways(i-1) + num_ways(i-2)) * (k-1)
        """
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
        
        return dp[-1]