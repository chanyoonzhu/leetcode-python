"""
- monotonic decreasing stack
- O(n), O(n)
"""
class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        # for a number to be guaranteed to be researched, all numbers to its left should be smaller (no previous greater number) and all to its right should be larger (no next smaller number)
        
        N = len(nums)
        stack = []
        has_prev_greater_or_next_smaller = [False] * N
        res = set()
        
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] > x: # has next smaller
                has_prev_greater_or_next_smaller[stack.pop()] = True
            stack.append(i)
            
        stack.clear()
        for i in range(N-1, -1, -1): # reverse
            while stack and nums[stack[-1]] < nums[i]: # has prev greater
                has_prev_greater_or_next_smaller[stack.pop()] = True
            stack.append(i)
        return sum(1 for i in range(N) if not has_prev_greater_or_next_smaller[i])