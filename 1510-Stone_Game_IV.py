"""
- dynamic programming (top-down)
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
            
        @lru_cache(None)
        def dp(n):
            if n <= 0: return False
            for i in range(1, floor(n ** 0.5) + 1):
                if not dp(n - i ** 2):
                    return True
            return False
        
        return dp(n)