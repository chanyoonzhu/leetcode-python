"""
- monotonically increasing stack
- O(n), O(n)
- similar problem: 496-Next Greater Element
"""
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        next_smaller = [n] * n
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] > v:
                next_smaller[stack.pop()] = i
            stack.append(i)
        return sum([next_smaller[i] - i for i in range(n)])