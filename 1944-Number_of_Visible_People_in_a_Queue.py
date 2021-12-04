"""
- monotonic decreasing stack
- O(n), O(n)
"""
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        res = [0] * n
        
        for i in range(n):
            height = heights[i]
            while stack and heights[stack[-1]] <= height:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res