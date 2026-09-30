"""
- bitwise operation
- O(1), O(1)
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        diff = x ^ y
        while diff:
            if diff & 1: result += 1
            diff >>= 1
        return result