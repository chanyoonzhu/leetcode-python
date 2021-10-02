class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = lptr = 0
        r = rptr = len(height) - 1
        total = 0
        
        while l < r:
            lower = l if height[l] < height[r] else r
            
            if height[l] < height[r]:
                while lptr < r and height[lptr] <= height[l]:
                    total += (height[l] - height[lptr])
                    lptr += 1
                l = lptr
                continue
            else:
                while rptr > l and height[rptr] <= height[r]:
                    total += (height[r] - height[rptr])
                    rptr -= 1
                r = rptr
                continue
                
        return total

"""
- stack (monotonically decreasing)
- O(n), O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                min_height = height[stack.pop()]
                if not stack: break # no elevation on the left side to trap water with
                min_i = stack[-1]
                result += (min(h, height[min_i]) - min_height) * (i - 1 - min_i) # height diff * width
            stack.append(i)
        return result