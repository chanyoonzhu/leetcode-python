"""
- Dynamic Programming (with bitmasks)
- time: O(N * 3^M * 2^M) - N * 3^M states in dp params, each state has up to (2^M) neighbors to calculate (at most only 2 colors to choose for a cell in a new col).
- space: O(N * 3^M + M * 3^M * 2^M)
"""
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        colors = set([1, 2, 3])
            
        @lru_cache(None)
        def getNextColMasks(r, mask, prev_mask):
            if r == m:
                return [mask]
            masks = []
            left = (prev_mask >> (2 * r)) & 3 # get two bits of prev_mask at r
            up = ((mask >> (2 * (r - 1))) & 3) if r > 0 else 0 # get two bits of mask at r-1
            available_colors = colors - set([left, up])
            for color in available_colors:
                masks.extend(getNextColMasks(r+1, mask | (color << (2 * r)), prev_mask))
            return masks
        
        @lru_cache(None)
        def dp(c, prev_col_mask): # c - col index
            if c == n:
                return 1
            total = 0
            for cur_col_mask in getNextColMasks(0, 0, prev_col_mask):
                total = (total + dp(c+1, cur_col_mask)) % MOD
            return total
        
        return dp(0, 0)
        