"""
- prefix sum with hashmap + mod
- O(n), O(k)
- similar: 1590
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = collections.Counter({0: 1})
        _sum = 0
        result = 0
        for i, n in enumerate(nums):
            _sum = (_sum + n) % k # key: stores mod, not original value
            result += prefix_sum[_sum]
            prefix_sum[_sum] += 1
        return result