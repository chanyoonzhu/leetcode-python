"""
- monotonically increasing stack
- O(n), O(n)
- similar problem: 496-Next Greater Element
"""
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        
        N = len(nums)
        res = 0
        stack = []
        
        for i, x in enumerate(nums):
            while stack and x < nums[stack[-1]]:
                prev_idx = stack.pop()
                res += i - prev_idx
            stack.append(i)
        
        # remained in stack are indexes with subarrays all the way to the end of the array
        while stack:
            idx = stack.pop()
            res += N - idx
        
        return res