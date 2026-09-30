"""
- dynamic programming (top-down)
- O(k*n^2), O(kn)
"""
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        @lru_cache(None)
        def dp(k, n):
            if n <= 1: return n
            if k == 1: return n
            moves = float("inf")
            for f in range(1, n + 1):
                moves = min(moves, 1 + max(dp(k-1, f-1), dp(k, n-f)))
            return moves
        
        return dp(k, n)