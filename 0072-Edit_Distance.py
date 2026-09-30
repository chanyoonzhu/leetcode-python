"""
- dp (top-down), dp[i1][i2] - the edits needed for converting word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def dp(i1, i2, n1, n2):
            if i2 < 0: # delete extra letters in word1
                return i1 + 1 
            if i1 < 0: # insert when no more letter in word1
                return i2 + 1
            if word1[i1] == word2[i2]: # match
                return dp(i1 - 1, i2 - 1, n1, n2)
            # min of delete, replace, or insert
            return min(1 + dp(i1 - 1, i2, n1, n2), 1 + dp(i1 - 1, i2 - 1, n1, n2), 1 + dp(i1, i2 - 1, n1, n2)) 
        
        n1, n2 = len(word1), len(word2)
        return dp(n1 - 1, n2 - 1, n1, n2)

"""
- dp (bottom-up), dp[i1][i2] - the edits needed for converting word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """ 
        n1, n2 = len(word1), len(word2)
        dp = [[float("inf")] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0: # base case
                    dp[i][j] = j
                elif j == 0: # base case
                    dp[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]: # match
                        dp[i][j] = dp[i - 1][j - 1]
                    else: # min of delete, replace, or insert
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return dp[n1][n2]

"""
- dp (bottom-up): space optimized
- O(mn), O(m)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:  
        n1, n2 = len(word1), len(word2)
        dp_prev = [x for x in range(n1 + 1)]
        
        for i2 in range(1, n2 + 1):
            dp = [i2] * (n1 + 1)
            for i1 in range(1, n1 + 1):
                if word1[i1 - 1] == word2[i2 - 1]: # match
                    dp[i1] = dp_prev[i1 - 1]
                else: # min of delete, replace, or insert
                    dp[i1] = min(dp[i1 - 1], dp_prev[i1 - 1], dp_prev[i1]) + 1
            dp_prev = dp
        return dp_prev[n1]

sl = Solution()
print(sl.minDistance("horse", "ros"))


