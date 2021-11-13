"""
- dynamic programming (top-down)
- intuition: there is one and only one way to create a array satisfying dp(n, k) given an array that satisfies dp(n-1, j) where j < k.
    eg. given [3,2,1,4] (which is a dp(4, 3)), to create dp(5, 4), we have only one solution [3,2,1,5,4], to create dp(5, 5), we only have on solution [3,2,5,1,4], so on and so forth,
    so transition function is dp(n, k) = dp(n-1,k) + dp(n-1,k-1) + ... + dp(n-1,k-n+1) -> need to bound by n because can only add n more pairs by inserting n
- TLE
"""
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(n, k):
            if n == 0:
                return 0
            if k == 0:
                return 1
            pairs = 0
            for j in range(min(k + 1, n)): # easy to miss: need to bound by n, can only add n more pairs by inserting n
                pairs = (pairs + dp(n-1, k-j)) % MOD
            return pairs
        
        return dp(n, k)

"""
- dynamic programming (top-down)
- optimized: 
dp(n, k) = dp(n-1,k) + dp(n-1,k-1) + ... + dp(n-1,k-n+1)
dp(n, k-1) = dp(n-1,k-1) + dp(n-1,k-2) + ... + dp(n-1,k-n+1) + dp(n-1,k-n)
replace right side of equation 1 with right side of equation 2:
dp(n, k) = dp(n-1,k) + dp(n, k-1) - dp(n-1,k-n) if k - n >= 0 else: 0)
"""
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(n, k):
            if n == 0 or k < 0:
                return 0
            if k == 0:
                return 1
            if n == 1 and k >= 1: # easy to miss: k cannot be too larger than n
                return 0
            return (dp(n, k-1) + dp(n-1,k) - dp(n-1,k-n)) % MOD
        
        return dp(n, k)