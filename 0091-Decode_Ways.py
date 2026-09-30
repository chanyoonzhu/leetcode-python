"""
- dynamic programming (top-down)
- O(n), O(n)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)
        
        @lru_cache(None)
        def dfs(i):
            nonlocal N
            if i == N: return 1
            if s[i] == '0': return 0
            ways = 0
            if i < N - 1 and int(s[i:i+2]) <= 26:
                ways = dfs(i+2)
            ways += dfs(i+1)
            return ways
    
        return dfs(0)

"""
- dynamnic programming (bottom-up) dp[i] is number of ways to parse s[:i], similar to "climb stairs" (with conditions)
- O(n), O(n)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        
        for i in range(1, N + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

"""
- dynamnic programming (bottom-up, space optimized)
- O(n), O(1)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)
        p, pp = 1, 0
        
        for i in range(1, N + 1):
            total = 0
            if s[i-1] != '0':
                total += p
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                total += pp
            pp = p
            p = total
        return p
