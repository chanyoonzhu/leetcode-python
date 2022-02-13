"""
- dynamic programming
- intuition: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/575000/DP-solution-with-illustration
"""
class Solution:
    def numOfWays(self, n: int) -> int:
        Mod = 10 ** 9 + 7
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 6 # i - row, j - 0:ABC  1:ABA pattern
        dp[0][1] = 6
        for i in range(1,n) :
            dp[i][0] = (dp[i-1][0]*2 + dp[i-1][1]*2) % Mod
            dp[i][1] = (dp[i-1][0]*2 + dp[i-1][1]*3) % Mod
        return (dp[n-1][0] + dp[n-1][1]) % Mod


"""
- dynamic programming (optimized)
"""
class Solution:
    def numOfWays(self, n: int) -> int:
        Mod = 10 ** 9 + 7
        abc, aba = 6, 6
        for i in range(1,n) :
            abc, aba = (abc*2 + aba*2) % Mod, (abc*2 + aba*3) % Mod
        return (abc + aba) % Mod