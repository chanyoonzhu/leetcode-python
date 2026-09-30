"""
- bitwise operation
- O(logn), O(1)
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n:
            if n & 1: 
                return n == 1
            n >>= 1
            if not n or n & 1: return False
            n >>= 1
        return False

"""
- bitwise operation
- O(1), O(1)
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # positive, in the format of 10000......, and not just power of 2 (%3=2)
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1