"""
- dynamic programming
- O(n)
"""
class Solution:
    def findDerangement(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0
        for n in range(2, n + 1):
            # n - 1 ways to place n
            # when n place at i
                # if i placed at n (swapping), then we only need to arrange n-2 numbers: dp[n-2]
                # if i placed not at n, then we need to arrange n-1 numbers: dp[n-1]
            dp[n] = (n - 1) * (dp[n - 1] + dp[n - 2]) % 1000000007
        return dp[n]