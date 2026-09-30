"""
- hashmap with prefix sum
- O(n), O(n)
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        sums = collections.Counter({0: 1})
        _sum = 0
        for num in nums:
            _sum += num
            result += sums[_sum - goal]
            sums[_sum] += 1
        return result

"""
- sliding window with prefix sum
- O(n), O(1)
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        l = 0
        _sum = 0
        count = 0
        
        for r, n in enumerate(nums):
            if n == 1: # n > 0 if nums have not only 0 but 1
                count = 0
            _sum += n
            while l <= r and _sum >= goal:
                if _sum == goal:
                    count += 1
                _sum -= nums[l]
                l += 1
            result += count
        
        return result