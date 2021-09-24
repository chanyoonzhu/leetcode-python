
"""
- dynamic programming (top-down)
- TLE
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
    
        @lru_cache(None)
        def dp(i, s, l): # s: shorter length, l: longer length
            
            if i == len(rods):
                return 0 if s == l else float("-inf")
            
            if s > l: return dp(i, l, s)
            
            rod_len = rods[i]
            
            # max of (add to longer beam, add to longer beam, do not add)
            return max(min(rod_len, l - s) + dp(i + 1, s + rod_len, l), dp(i + 1, s, l + rod_len), dp(i + 1, s, l))
                       
        return dp(0, 0, 0)

"""
- dynamic programming (top-down)
- O(n * sum(rods)), O(n * sum(rods))
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, diff): # i - rod index; diff - diff b/t shorter and longer beam; dp[i][diff] max shorter beam length
            
            if i == len(rods):
                return 0 if diff == 0 else float("-inf")
            
            rod_len = rods[i]
            # max of (add to longer beam, add to longer beam, do not add)
            return max(dp(i + 1, diff + rod_len), rod_len + dp(i + 1, diff - rod_len), dp(i + 1, diff))
        
        return dp(0, 0)

"""
- todo: 1D bottom-up
"""
    
    

