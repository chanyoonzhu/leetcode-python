"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                i_smaller = stack.pop()
                result[i_smaller] = i - i_smaller
            stack.append(i)
        return result