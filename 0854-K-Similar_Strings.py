"""
- dynamic programming
- O(n^3), O(n^2)
"""
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        return self.dp(s1, s2)
    
    @lru_cache(None)
    def dp(self, s1, s2):
        if not s1:
            return 0
        if s1[0] == s2[0]:
            return self.dp(s1[1:], s2[1:])
        min_k = float("inf")
        for i in range(1, len(s2)):
            if s1[0] == s2[i]:
                min_k = min(min_k, 1 + self.dp(s1[1:], s2[1:i] + s2[0] + s2[i+1:]))
        return min_k