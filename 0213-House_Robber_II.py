"""
- dp - #198 with two passes
- O(n), O(1)
- intuition: exclude first/last number in each pass
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            prev_two = [0, 0]
            result = 0
            for i, n in enumerate(nums):
                result = max(prev_two[1], prev_two[0] + n)
                prev_two = [prev_two[1], result]
            return result
            
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(rob(nums[1:]), rob(nums[:-1]))

"""
- dp - #198 with one pass (two states)
- O(n), O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n: return 0
        if n <= 2: return max(nums)
        prev_two_1 = [0, 0]
        prev_two_2 = [0, 0]
        for i in range(n):
            if i < n - 1:
                prev_two_1 = [prev_two_1[1], max(prev_two_1[1], prev_two_1[0] + nums[i])]
            if i > 0:
                prev_two_2 = [prev_two_2[1], max(prev_two_2[1], prev_two_2[0] + nums[i])]
        return max(max(prev_two_1), max(prev_two_2))