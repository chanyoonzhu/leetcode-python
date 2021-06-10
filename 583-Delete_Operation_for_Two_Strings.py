"""
- dp (top-down), dp[i1][i2] - the deletes needed for matching word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def dp(i1, i2, n1, n2):
            if i1 == n1: return n2 - i2
            if i2 == n2: return n1 - i1
            if word1[i1] == word2[i2]:
                return dp(i1 + 1, i2 + 1, n1, n2)
            return min(dp(i1 + 1, i2, n1, n2), dp(i1, i2 + 1, n1, n2)) + 1
        
        return dp(0, 0, len(word1), len(word2))

"""
- dp (bottom-up), dp[i1][i2] - the deletes needed for matching word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n2 + 1):
            dp[0][i] = i
        for i in range(1, n1 + 1):
            dp[i][0] = i
            
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1]
                else:
                    dp[i1][i2] = min(dp[i1 - 1][i2], dp[i1][i2 - 1]) + 1
        
        return dp[-1][-1]

"""
- dp (bottom-up), space optimized
- O(mn), O(m)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        dp_prev = [i for i in range(n2 + 1)]
            
        for i1 in range(1, n1 + 1):
            dp = [0] * (n2 + 1)
            dp[0] = i1
            for i2 in range(1, n2 + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    dp[i2] = dp_prev[i2 - 1]
                else:
                    dp[i2] = min(dp_prev[i2], dp[i2 - 1]) + 1
            dp_prev = dp
        
        return dp_prev[-1]