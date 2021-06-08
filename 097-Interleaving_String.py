"""
- dp (top-down) interleaving s1[i1:] and s2[i2:] to get s3[i1 + i2:]
- O(mn), O(mn)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def dp(i1, i2):
            if i1 + i2 == len(s3):
                return i1 == len(s1) and i2 == len(s2) # test if s1 and s2 are used up
            can_interleave = False
            if i1 < len(s1):
                can_interleave = s1[i1] == s3[i1 + i2] and dp(i1 + 1, i2)
            if i2 < len(s2):
                can_interleave = can_interleave or (s2[i2] == s3[i1 + i2] and dp(i1, i2 + 1))
            return can_interleave
        
        return dp(0, 0)

"""
- dp (top-down) interleaving s1[:i1 + 1] and s2[:i2 + 1] to get s3[:i1 + i2 + 2]
- O(mn), O(mn)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def dp(i1, i2):
            if i1 == -1 and i2 == -1: return True
            can_interleave = False
            if i1 >= 0 and s1[i1] == s3[i1 + i2 + 1]:
                can_interleave |= dp(i1 - 1, i2)
            if i2 >= 0 and s2[i2] == s3[i1 + i2 + 1]:
                can_interleave |= dp(i1, i2 - 1)
            return can_interleave        
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        return n1 + n2 == n3 and dp(n1 - 1, n2 - 1)

"""
- dp (bottom-up) interleaving s1[:i1 + 1] and s2[:i2 + 1] to get s3[:i1 + i2 + 2]
- O(mn), O(mn)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i1 in range(n1 + 1):
            for i2 in range(n2 + 1):
                if i1 > 0 and s1[i1 - 1] == s3[i1 + i2 - 1]:
                    dp[i1][i2] |= dp[i1 - 1][i2]
                if i2 > 0 and s2[i2 - 1] == s3[i1 + i2 - 1]:
                    dp[i1][i2] |= dp[i1][i2 - 1]
        return dp[n1][n2]

"""
- dp (bottom-up) space optimized
- O(mn), O(n)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        
        dp_prev, dp = [False] * (n2 + 1), [False] * (n2 + 1)
        dp[0] = True # so that L78 can be true in first loop
        for i1 in range(n1 + 1):
            for i2 in range(n2 + 1):
                if i1 > 0 and s1[i1 - 1] == s3[i1 + i2 - 1]:
                    dp[i2] |= dp_prev[i2]
                if i2 > 0 and s2[i2 - 1] == s3[i1 + i2 - 1]:
                    dp[i2] |= dp[i2 - 1]
            dp_prev, dp = dp, [False] * (n2 + 1)
        return dp_prev[n2]