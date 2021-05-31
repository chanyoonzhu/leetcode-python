"""
- brute force
- O(n^2), O(n)
- Time limit exceeded
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum = 0
        n = len(nums)
        result = n + 1
        for i, num in enumerate(nums):
            _sum += num
            cur_sum = _sum
            for j in range(i + 1):
                if cur_sum >= target:
                    result = min(result, i - j + 1)
                    cur_sum -= nums[j]
        return result if result <= n else 0

"""
- prefix sum with binary search
- O(nlogn), O(n)
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sums = [0]
        n = len(nums)
        result = n + 1
        for i, num in enumerate(nums):
            sums.append(sums[-1] + num)
            if sums[-1] >= target:
                left = bisect.bisect_right(sums, sums[-1] - target) - 1
                result = min(result, i - left + 1)
        return result if result <= n else 0

"""
- two pointers / sliding window
- O(n), O(1)
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum = 0
        n = len(nums)
        result = n + 1
        left = 0
        for right in range(n):
            _sum += nums[right]
            while _sum >= target:
                _sum -= nums[left]
                left += 1
                result = min(result, right - left + 2)
        return result if result <= n else 0