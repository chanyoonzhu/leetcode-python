"""
- backtracking
- O(k * 2^n)
- TlE
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
        return False

"""
- todo: bit-masking
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sub_sum, mod = divmod(sum(nums), k)
        if mod != 0: return False
        nums.sort(reverse=True)
        n = len(nums)

        bitmask = (1 << n) - 1
    
        @lru_cache(None)
        def backtrack(part, bitmask):
            if not bitmask:
                return part == 0
            if part == 0:
                return backtrack(sub_sum, bitmask)
            res = False
            for i in range(n):
                if bitmask & (1 << i) and nums[i] <= part:
                    if backtrack(part - nums[i], bitmask ^ (1 << i)):
                        return True
        
        return backtrack(sub_sum, bitmask)