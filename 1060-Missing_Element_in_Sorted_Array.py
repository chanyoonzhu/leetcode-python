"""
- linear search
- O(n), O(1)
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        i, N = 1, len(nums)
        missing_idx_count = 0
        while i < N:
            if nums[i] > nums[i - 1] + 1:
                if missing_idx_count + nums[i] - nums[i - 1] - 1 < k:
                    missing_idx_count += (nums[i] - nums[i - 1] - 1)
                else:
                    return nums[i-1] + (k - missing_idx_count)
            i += 1
        return nums[N-1] + (k - missing_idx_count)

"""
- binary search
- O(logn), O(1)
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, N - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            missing = self.getNumOfMissing(nums, l, mid)
            if missing < k:
                l = mid
                k -= missing
            else:
                r = mid - 1
        return nums[r] + k  
        
    def getNumOfMissing(self, nums, l, r):
        if l == r: return 0
        return nums[r] - nums[l] - (r - l)