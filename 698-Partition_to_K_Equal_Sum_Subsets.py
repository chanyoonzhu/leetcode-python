"""
- backtracking
- O(k * 2^n)
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        div, mod = divmod(sum(nums), k)
        if mod != 0: return False
        nums.sort(reverse=True)
        parts = [div] * k
        return self.backtrack(parts, nums, 0)
    
    def backtrack(self, parts, nums, i):
        if i == len(nums):
            return sum(parts) == 0
        for j in range(len(parts)):
            if parts[j] >= nums[i]:
                parts[j] -= nums[i]
                if self.backtrack(parts, nums, i + 1):
                    return True
                parts[j] += nums[i]

"""
- todo: bit-masking
"""