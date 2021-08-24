"""
- dynamic programming (top-down)
- O(L^2 * n), O(n)
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        memo = {}
        words_set = set(words)
        
        def dp(word):
            if word not in words_set: return 0
            if word not in memo:
                memo[word] = 1
                for i in range(len(word)):
                    prev = word[:i] + word[i + 1:]
                    memo[word] = max(memo[word], dp(prev) + 1)
            return memo[word]
        
        return max(dp(word) for word in words)

"""
- dynamic programming (bottom-up)
- O(L * n + nlogn), O(n)
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        result = 1
        
        words.sort(key=len)
        
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            result = max(result, dp[word])
        return result