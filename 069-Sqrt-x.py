"""
- binary search
- O(logx), O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            mid_squared = mid ** 2
            if mid_squared == x:
                return mid
            elif mid_squared > x:
                hi = mid - 1
            else:
                lo = mid
        return lo
                
        