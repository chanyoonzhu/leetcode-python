"""
- prefix sum with hashmap + mod
- O(n), O(k)
- similar: 974
- intuition: find extra k = sum(nums) % p, then problem becomes find the shortest subarray that has a sum S where S % p = k
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_last_index = {0: -1}
        _sum = 0
        result = len(nums)
        k = sum(nums) % p        
        for i, n in enumerate(nums):
            _sum = (_sum + n) % p
            prefix_last_index[_sum] = i
            need = (_sum - k) % p
            if need in prefix_last_index:
                result = min(result, i - prefix_last_index[need])
        return result if result < len(nums) else -1