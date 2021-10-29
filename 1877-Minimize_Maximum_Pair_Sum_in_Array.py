"""
- greedy
- O(n), O(1)
"""
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        result = 0
        while l < r:
            result = max(result, nums[l] + nums[r]) # greedily pair min with max
            l += 1
            r -= 1
        return result