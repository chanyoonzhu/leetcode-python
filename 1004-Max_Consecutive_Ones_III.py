"""
- sliding window
- O(n), O(1)
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        cur_k = k
        l = 0
        for r, x in enumerate(nums):
            if x == 0:
                if cur_k:
                    cur_k -= 1
                else: # k becomes negative, need to exlude the leftmost 0
                    while nums[l] != 0:
                        l += 1
                    l += 1
            res = max(res, r - l + 1)
        return res