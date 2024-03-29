"""
- dp (top-down) interleaving s1[i1:] and s2[i2:] to get s3[i1 + i2:]
- tip: index in s3 (i3) can be determined by i1 + i2, so no need to keep track of i3 separately
- O(mn), O(mn)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1:
                return True
            
            if i >= 0 and s1[i] == s3[i+j+1] and dp(i-1, j): # caveat: s3 index needs +1
                return True
            if j >= 0 and s2[j] == s3[i+j+1] and dp(i, j-1):
                return True
            return False

            """ faster
            if i == n1:
                return s2[j:] == s3[i+j:]
            if j == n2:
                return s1[i:] == s3[i+j:]
            if s1[i] == s3[i+j] and dp(i+1, j):
                return True
            if s2[j] == s3[i+j] and dp(i, j+1):
                return True
            return False
            """
        
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3): return False
        return dp(n1 - 1, n2 - 1)

"""
- dp (bottom-up) interleaving s1[:i1 + 1] and s2[:i2 + 1] to get s3[:i1 + i2 + 2]
- O(mn), O(mn)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]  # dp[i, j] -> s1[:i+1] s2[:j+1] can interleave or not
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