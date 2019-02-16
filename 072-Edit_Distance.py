class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1 = " " + word1
        word2 = " " + word2
        x, y = len(word1), len(word2)
        dp = [[0] * x for _ in range(y)]
        # initialize dp
        dp[0] = [j for j in range(x)]
        for i in range(y):
            dp[i][0] = i
        # update dp
        for i in range(1, y):
            for j in range(1, x):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        return dp[-1][-1]

sl = Solution()
print(sl.minDistance("horse", "ros"))