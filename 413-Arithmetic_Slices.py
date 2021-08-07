"""
- dynamic programming
- O(n), O(n)
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3: return 0
        
        dp = [0] * N
        prev_diff = nums[1] - nums[0]
        for i in range(1, N - 1):
            cur_diff = nums[i+1] - nums[i]
            if prev_diff == cur_diff:
                dp[i+1] = dp[i] + 1 # smart
            else:
                prev_diff = cur_diff
        return sum(dp)

"""
- dynamic programming (space optimized)
- O(n), O(n)
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3: return 0
        
        result = 0
        count = 0
        prev_diff = nums[1] - nums[0]
        for i in range(1, N - 1):
            cur_diff = nums[i+1] - nums[i]
            if prev_diff == cur_diff:
                count += 1
                result += count
            else:
                prev_diff = cur_diff
                count = 0
        return result