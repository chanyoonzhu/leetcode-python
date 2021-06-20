"""
- sliding window
- O(n), O(1)
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        total_k = left = result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                total_k += 1
                if total_k > k:
                    # let left skip the next 0
                    while nums[left] != 0:
                        left += 1
                    left += 1
                    total_k -= 1
            result = max(result, i - left + 1)
        return result