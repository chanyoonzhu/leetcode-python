"""
- dp (top-down), dp[i1][i2] - the deletes needed for matching word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1: return 0
            if i == -1: return j + 1
            if j == -1: return i + 1
            
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i - 1, j), dp(i, j - 1)) + 1
        
        return dp(len(word1) - 1, len(word2) - 1)

"""
- dp (bottom-up), dp[i1][i2] - the deletes needed for matching word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        N1, N2 = len(word1), len(word2)
        dp = [[float("inf")] * (N2 + 1) for _ in range(N1 + 1)]
        
        for i in range(N1 + 1):
            for j in range(N2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
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