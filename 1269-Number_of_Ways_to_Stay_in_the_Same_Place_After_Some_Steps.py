"""
- dynamic programming (bottom-up)
- O(n*s), O(n)
"""
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        prev_dp = [0] * arrLen
        prev_dp[0] = 1
        
        for _ in range(steps):
            dp = prev_dp[:]
            for i in range(arrLen):
                if i > 0:
                    dp[i] += prev_dp[i - 1]
                if i < arrLen - 1:
                    dp[i] += prev_dp[i + 1]
            prev_dp = dp
        
        return prev_dp[0] % (10**9 + 7)