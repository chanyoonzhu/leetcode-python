"""
- dp (top-down): 
    dp[i][j] = minimum cost to achieve all the cuts between i and j
- O(n^3), O(n^2)
"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def dp(l, r):
            if (l, r) not in memo:
                memo[l, r] = min([dp(l, cut) + dp(cut, r) + (r - l) for cut in cuts if l < cut < r] or [0])
            return memo[l, r]
        return dp(0, n)

"""
- dp (buttom-up): 
    dp[i][j] = minimum cost to achieve all the cuts between i and j
- O(n^3), O(n^2)
"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])
        k = len(cuts)
        dp = [[0] * k for _ in range(k)]
        for d in range(2, k): # will not cut stick with length <= 1
            for l in range(k - d):
                r = l + d
                dp[l][r] = min(dp[l][k] + dp[k][r] for k in range(l + 1, r)) + cuts[r] - cuts[l]
        return dp[0][k - 1]

