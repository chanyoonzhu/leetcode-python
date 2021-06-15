"""
- monotonically increasing stack
- O(n), O(n)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)): # i is the right boundary
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 # stack[-1] is the left boundary
                result = max(result, h * w)
            stack.append(i)
        return result