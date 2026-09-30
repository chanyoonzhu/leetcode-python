"""
- dynamic programming (top-down)
- dp[i] represents the count of unique subsequence ends with S[i].
- O(n^2), O(n)
"""
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10 ** 9 + 7
        N = len(s)

        @lru_cache(None)
        def dp(i):
            if i == -1: return 0
            total_end_i = 1 # s[i] itself
            for j in range(i):
                if s[j] != s[i]: # those ends at j is repeated when ends at i, so not adding to total
                    total_end_i = (total_end_i + dp(j)) % MOD
            return total_end_i
        
        return sum(dp(i) for i in range(N)) % MOD

"""
- dynamic programming (bottom-up)
- O(n^2), O(n)
"""
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10 ** 9 + 7
        N = len(s)
        dp = [1] * N
        
        for i in range(N):
            for j in range(i):
                if s[j] != s[i]:
                    dp[i] = (dp[i] + dp[j]) % MOD
        return sum(dp) % MOD

"""
- dynamic programming (bottom-up)
- O(n), O(n)
"""
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10 ** 9 + 7
        N = len(s)
        dp = [1] * N
        
        total = 0
        dedup_counter = collections.Counter()
        for i in range(N):
            c = s[i]
            dp[i] = (dp[i] + total - dedup_counter[c]) % MOD
            total = (total + dp[i]) % MOD
            dedup_counter[c] = (dedup_counter[c] + dp[i]) % MOD
        return total

"""
- dynamic programming (bottom-up)
- O(n), O(1)
"""
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10 ** 9 + 7
        N = len(s)
        
        total = 0
        dedup_counter = collections.Counter()
        for i in range(N):
            c = s[i]
            cur = (1 + total - dedup_counter[c]) % MOD
            total = (total + cur) % MOD
            dedup_counter[c] = (dedup_counter[c] + cur) % MOD
        return total