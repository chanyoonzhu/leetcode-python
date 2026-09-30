"""
- dynamic programming
- O(n^2), O(n^2)
"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        return self.dp(s, 0, len(s) - 1, memo)

    def dp(self, s, i, j, memo):
        if i > j:
            return 0
        if (i, j) not in memo:
            prints = self.dp(s, i + 1, j, memo) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    prints = min(prints, self.dp(s, i, k - 1, memo) + self.dp(s, k + 1, j, memo))
            memo[(i, j)] = prints
        return memo[(i, j)]