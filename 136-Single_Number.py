"""
- bitwise operation
- O(n), O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

"""
- other solutions:
    hashset; hashmap; math with hashset
"""