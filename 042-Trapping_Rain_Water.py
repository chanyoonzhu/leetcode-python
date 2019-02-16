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