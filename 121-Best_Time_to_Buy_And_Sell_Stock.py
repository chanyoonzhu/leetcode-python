"""
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Questions: buy first, then sell?
- negative numbers? empty array? numbers getting smaller and smaller - Don't buy or profit can be negative?
"""

"""
- Brute Force
- O(n^2), O(1)
- TLE
"""
class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
                
        return maxProfit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo = prices[0]
        res = 0
        for p in prices:
            lo = min(lo, p)
            res = max(res, p - lo)
        return res