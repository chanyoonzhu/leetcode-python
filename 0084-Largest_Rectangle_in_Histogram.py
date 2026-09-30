"""
- monotonically increasing stack
- intuition: iterate through each bar, find the area of the largest histogram with that bar being its lowest, the global largest must be one of them
    for each bar (with height rec_h), to calculate the largest histogram including that bar with height exactly equal to h, 
    we only need to find which bars on its left (i) and right (j) is the first one lower than itself, those two bars form the left/right bound of histogram (not included)
    then the rectangle size is then:  h * (i - j - 1)
- O(n), O(n)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0) # dummy value at the end
        stack = [-1]
        result = 0
        for i in range(len(heights)): # i is the right boundary
            while heights[stack[-1]] > heights[i]:
                rec_h = heights[stack.pop()]
                rec_w = i - stack[-1] - 1 # stack[-1] is the left boundary
                result = max(result, rec_h * rec_w)
            stack.append(i)
        return result

"""
- easier to read version
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        mono_stack = []
        res = 0
        for i, h in enumerate(heights): # iterate through each right bound
            while mono_stack and heights[mono_stack[-1]] > h:
                rec_h = heights[mono_stack.pop()] # the bar with lowest height in the histogram determines the height of the histogram, this is the bar that's lowest between (left and right bound - not inclusive)
                rec_w = i - (mono_stack[-1] if mono_stack else -1) - 1 # mono_stack[-1] is the left bound
                res = max(res, rec_h * rec_w)
            mono_stack.append(i)
        
        while mono_stack: # easy to miss: need to compute the rest in the stack
            rec_h = heights[mono_stack.pop()]
            rec_w = len(heights) - (mono_stack[-1] if mono_stack else -1) - 1
            res = max(res, rec_h * rec_w)
            
        return res