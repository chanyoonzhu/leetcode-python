"""
- dynamic programming (top-down)
- O(n^2), O(n^2)
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if i >= j: return 0
            if i == j: return piles[i]
            # greedily choose the end that maximize Alex's yield, and greedily make Bob choose the end that minimize Alex's yield 
            return max(piles[i] + min(dp(i + 2, j), dp(i + 1, j - 1)), piles[j] + min(dp(i + 1, j - 1), dp(i, j - 2)))
        
        alex = dp(0, len(piles) - 1)
        return alex > sum(piles) - alex

"""
- mathematics
- intuition: Alex can always take all the stones at the odd position, or she can take all at the even position. She just need to figure out which is bigger: odd sum or even sum
- O(1), O(1)
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if i >= j: return 0
            if i == j: return piles[i]
            # greedily choose the end that maximize Alex's yield, and greedily make Bob choose the end that minimize Alex's yield 
            return max(piles[i] + min(dp(i + 2, j), dp(i + 1, j - 1)), piles[j] + min(dp(i + 1, j - 1), dp(i, j - 2)))
        
        alex = dp(0, len(piles) - 1)
        return alex > sum(piles) - alex