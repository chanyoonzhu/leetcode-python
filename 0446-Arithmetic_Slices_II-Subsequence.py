"""
- similar: 413-Arithmetic Slices
"""
"""
- dynamic programming (bottom-up)
- O(n^2, O(nk))
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        dp = defaultdict(int) # dp[i][k] - the number of arithmetic subsequences ending at i with increment k
        result = 0
        
        for i in range(1, len(nums)):                       
            for j in range(i):                           
                diff = nums[i] - nums[j]                 
                dp[(i, diff)] += dp[(j, diff)] + 1     
                result += dp[(j, diff)]              
        return result