"""
- dynamic programming (top-down)
- dp[i] - the length of the arithmetic subarray
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i < 2: return 0
            
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                return 1 + dp(i - 1)
            return 0
          
        result = 0
        for i in range(len(nums)):
            seq_len = dp(i)
            result = (result + seq_len)
        return result

"""
- dynamic programming (bottom-up)
- O(n), O(n)
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        N = len(nums)
        dp = [0] * N
        result = 0
        for i in range(2, N):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = 1 + dp[i-1]
                result += dp[i] # length is also the number of subarrays
        return result

"""
- dynamic programming (bottom-up: space optimized)
- O(n), O(1)
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        N = len(nums)
        if N < 3: return 0
        
        diff, prev = nums[1] - nums[0], 0
        result = 0
        for i in range(2, N):
            cur_diff = nums[i] - nums[i-1]
            if cur_diff == diff:
                prev += 1
                result += prev
            else:
                diff = cur_diff
                prev = 0
        return result