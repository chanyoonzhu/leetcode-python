"""
- dynamic programming
- MLE
"""
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        bitmask = 0
        for x in nums:
            bitmask <<= 1
            if x == 0:
                bitmask |= 1 # all 0 is easier if we flip all bits at the start
        
        @lru_cache(None)
        def dp(i, bitmask):
            if bitmask == 0:
                return 0
            if i == N:
                return float("inf")
            flips = dp(i + 1, bitmask) # not flip current
            # flip current
            flipped = bitmask
            for j in range (i, i+k):
                flipped ^= (1 << j)
            flips = min(flips, 1 + dp(i + 1, flipped))
            return flips
        
        res = dp(0, bitmask)
        return res if res < float("inf") else -1

"""
- greedy
- intuition: flip 0 whenever seeing one
- O(n), O(k)
- TLE
"""
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        flips = 0
        for i in range(N-k+1):
            if nums[i] == 0:
                flips += 1
                for j in range(i, i + k):
                    nums[j] = 1 - nums[j]
        if all(nums[i] == 1 for i in range(N-k, N)):
            return flips
        return -1