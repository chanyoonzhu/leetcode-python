"""
- dynamic programming (top-down)
- O(n^2), O(n^2)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(1, n)
    
    @lru_cache(None)
    def helper(self, lo, hi):
        if lo > hi: return 1
        return sum(self.helper(lo, k-1) * self.helper(k+1, hi) for k in range(lo, hi + 1))

"""
- dynamic programming (top-down)
- dp(n): the number of unique BST for a sequence of length n
- O(n^2), O(n)
"""
class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0: return 1
        return sum(self.numTrees(k-1) * self.numTrees(n-k) for k in range(1, n + 1))

"""
- dynamic programming (bottom-up)
- dp(n): the number of unique BST for a sequence of length n
- O(n^2), O(n)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (1 + n)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[n]