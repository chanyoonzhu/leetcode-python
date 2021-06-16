"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        
        for i, val in enumerate(nums):
            if not stack or val < nums[stack[-1]]:
                stack.append(i) # indices that can be left boundary: if there's a value greater to the right, that value can't be the left boundary
                
        result = 0
        for i in range(len(nums) - 1, -1, -1):
            val = nums[i]
            while stack and val >= nums[stack[-1]]:
                result = max(result, i - stack.pop())
            
        return result