"""
- Array
- O(n), O(n)
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        N = len(heights)
        res = [N-1]
        
        for i in range(N - 2, -1, -1):
            if heights[i] > heights[res[0]]:
                res.insert(0, i)
                
        return res

"""
- Monotonic stack
- O(n), O(n)
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        N = len(heights)
        decreasing_stack = []
        
        for i in range(N):
            while decreasing_stack and heights[decreasing_stack[-1]] <= heights[i]:
                decreasing_stack.pop()
            decreasing_stack.append(i)
        
        return decreasing_stack