"""
- binary representation
- O(nlogn), O(nlogn)
"""
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        bin_concat = ''.join([bin(x)[2:] for x in range(1, n + 1)])
        return int(bin_concat, 2) % MOD

"""
- bit operation
- O(n), O(1)
"""
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        length = 0  # bit length of addends
        result = 0 
        for x in range(1, n + 1):
            # when meets power of 2, increase the bit length
            if x & (x - 1) == 0: # eg. 1000 & 111 == 0
                length += 1
            result = ((result << length) | x) % MOD
        return result