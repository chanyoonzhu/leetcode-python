"""
- greedy (two pointers)
- intuition: move the index on the shorter side towards middle (water will always be trapped as it moves)
- O(n), O(1)
"""
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
                # trap all bounded by l
                while lptr < r and height[lptr] <= height[l]:
                    total += (height[l] - height[lptr])
                    lptr += 1
                l = lptr
            else:
                # trap all bounded by r
                while rptr > l and height[rptr] <= height[r]:
                    total += (height[r] - height[rptr])
                    rptr -= 1
                r = rptr
                
        return total

"""
- stack (monotonically decreasing)
- O(n), O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # mono-decreasing
        result = 0
        for right_i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                min_height = height[stack.pop()]
                if not stack: break # no elevation on the left side to trap water with
                left_i = stack[-1]
                result += (min(h, height[left_i]) - min_height) * (right_i - 1 - left_i) # height diff * width
            stack.append(right_i)
        return result