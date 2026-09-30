"""
- add all increments
- O(n), O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        for i in range(1, len(prices)):
            p = prices[i]
            if p > prices[i-1]:
                result += (p - prices[i-1])
                
        return result