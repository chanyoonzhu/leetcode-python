"""
- dynamic programming 
- dp[i] - (min, max) of subarray ending at nums[i]
- O(n), O(n) - space can be improved to O(1) if only keeping min_max of the previous item
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        min_max = [(1, 1)]
        
        for i in range(N):
            if nums[i] == 0:
                min_max.append((0, 0))
            elif nums[i] > 0:
                prev_min, prev_max = min_max[-1]
                min_max.append((prev_min * nums[i], max(prev_max * nums[i], nums[i])))
            else:
                prev_min, prev_max = min_max[-1]
                min_max.append((min(prev_max * nums[i], nums[i]), prev_min * nums[i]))
        
        return max([max_ for _, max_ in  min_max[1:]])