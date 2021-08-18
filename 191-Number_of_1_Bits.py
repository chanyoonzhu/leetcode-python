"""
- bitwise operation
- O(n), O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            if n & 1: result += 1
            n >>= 1
        return result

"""
- bitwise operation
- n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
- O(n), O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n &= (n - 1)
            result += 1
        return result