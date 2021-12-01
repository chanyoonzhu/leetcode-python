"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        stack = []
        res = 0
        for i, x in enumerate(nums):
            if not stack or x < nums[stack[-1]]: # greedily stores element that can be left boundary
                stack.append(i)
                
        for i in range(len(nums) - 1, -1, -1): # greedily look at right boundary with the largest index
            x = nums[i]
            while stack and x >= nums[stack[-1]]:
                res = max(res, i - stack.pop())
            if not stack: # for speeding up, can omit
                break
        
        return res