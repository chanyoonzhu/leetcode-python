"""
- bitwise operation
- O(n), O(1)
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result += (n & 1) << (31 - i)
            n >>= 1
        return result