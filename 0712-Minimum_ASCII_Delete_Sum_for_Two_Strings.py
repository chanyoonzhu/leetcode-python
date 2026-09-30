"""
- dp (top-down), dp[i1][i2] - the delete cost needed for matching word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        chars = set(list(s1) + list(s2))
        values = {char: ord(char) for char in chars}
        
        @lru_cache(None)
        def dp(i1, i2, n1, n2):
            if i1 == n1: return sum(values[s2[i]] for i in range(i2, n2))
            if i2 == n2: return sum(values[s1[i]] for i in range(i1, n1))
            if s1[i1] == s2[i2]: return dp(i1 + 1, i2 + 1, n1, n2) # match if the same
            # delete s1[i1] or delete s2[i2]
            return min(dp(i1 + 1, i2, n1, n2) + values[s1[i1]], dp(i1, i2 + 1, n1, n2) + values[s2[i2]])
        
        return dp(0, 0, len(s1), len(s2))

"""
- dp (bottom-up), dp[i1][i2] - the delete cost needed for matching word1[:i1 + 1] to word2[:i2 + 1]
- O(mn), O(mn)
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        chars = set(list(s1) + list(s2))
        values = {char: ord(char) for char in chars}
        n1, n2 = len(s1), len(s2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + values[s1[i - 1]]
        for i in range(1, n2 + 1):
            dp[0][i] =  dp[0][i - 1] + values[s2[i - 1]]
            
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                if s1[i1 - 1] == s2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1]
                else:
                    dp[i1][i2] = min(dp[i1 - 1][i2] + values[s1[i1 - 1]], dp[i1][i2 - 1] + values[s2[i2 - 1]])
        
        return dp[-1][-1]

"""
- dp (bottom-up), space optimized
- O(mn), O(m)
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        chars = set(list(s1) + list(s2))
        values = {char: ord(char) for char in chars}
        n1, n2 = len(s1), len(s2)
        
        dp_prev = [0]
        for i in range(1, n2 + 1):
            dp_prev.append(dp_prev[i - 1] + values[s2[i - 1]])
            
        for i1 in range(1, n1 + 1):
            dp = [0] * (n2 + 1)
            dp[0] = dp_prev[0] + values[s1[i1 - 1]]
            for i2 in range(1, n2 + 1):
                if s1[i1 - 1] == s2[i2 - 1]:
                    dp[i2] = dp_prev[i2 - 1]
                else:
                    dp[i2] = min(dp_prev[i2] + values[s1[i1 - 1]], dp[i2 - 1] + values[s2[i2 - 1]])
            dp_prev = dp
        
        return dp_prev[-1]