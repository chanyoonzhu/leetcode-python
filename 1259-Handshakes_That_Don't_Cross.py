"""
- dynamic programming (top-down)
- O(n^2), O(n)
"""
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        
        MOD = 10 ** 9 + 7
    
        @lru_cache(None)
        def dp(n):
            if n % 2 == 1: # odd or none
                return 0
            if n <= 0: 
                return 1
            ways = 0
            for k in range(1, n+1, 2):
                ways = (ways + (dp(k-1) * dp(n-k-1))) % MOD
            return ways
        
        return dp(num_people)

"""
- dynamic programming (bottom-up)
- O(n^2), O(n)
"""
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        
        MOD = 10 ** 9 + 7
    
        dp = [0] * (1 + num_people)
        dp[0] = dp[2] = 1
        for x in range(4, num_people + 1):
            for k in range(1, x + 1, 2):
                dp[x] = (dp[x] + dp[k-1] * dp[x-k-1]) % MOD
        
        return dp[num_people]

"""
- todo: Catalan Numbers
"""