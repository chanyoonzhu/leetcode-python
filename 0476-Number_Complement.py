"""
- bitwise operation
- O(1), O(1)
"""
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = len(str(bin(num))[2:])
        mask = (1 << bit_length) - 1
        return mask ^ num