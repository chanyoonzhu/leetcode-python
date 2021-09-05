"""
- dynamic programming
- O(n), O(n)
"""
class Solution:
    def checkRecord(self, n):
        if n == 1:return 3
        if n == 0: return 0
        mod = 1000000007
        dp=[0 for i in range(n + 1)] # dp[i] - the number of all possible attendance (without 'A') records with length i
        # i=0, possible = 1; i=1, possible = 2 (P,L); i=2, possible = 4 (PP,PL,LP,LL)
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3,n + 1):
            # end with "P": dp[i-1]; end with "PL": dp[i-2]; end with "PLL": dp[i-3]; end with "LLL": is not allowed
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3] ) % mod
        res = dp[n]
        # with one 'A'
        for i in range(1, n + 1):
            res += dp[i - 1] * dp[n - i] % mod
        res %= mod
        return res