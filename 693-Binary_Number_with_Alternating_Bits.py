"""
- bitwise operation
- O(1), O(1)
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n_xor_shift = n ^ (n >> 1)
        return not n_xor_shift & (n_xor_shift + 1) # test if n_xor_shift is composed of all 1