"""
- prefix sum with hashmap
- O(n), O(n)
"""
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixes = {0: -1}
        sum_ = 0
        max_len = 0
        for i in range(n):
            sum_ += nums[i]
            if sum_ - k in prefixes:
                max_len = max(max_len, i - prefixes[sum_ - k])
            if sum_ not in prefixes:
                prefixes[sum_] = i
        return max_len