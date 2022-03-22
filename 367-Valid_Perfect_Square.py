"""
- binary search
- O(logn), O(1)
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            power4 = mid ** 2
            if power4 == num:
                return True
            elif power4 > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

"""
- todo: Newton's method
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num