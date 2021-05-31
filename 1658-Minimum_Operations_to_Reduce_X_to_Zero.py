"""
- prefix sum with hashtable
- O(n), O(n)
- this solution can handle negative numbers (not required by the problem itself)
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left_prefix = dict({0: -1})
        _sum = 0
        for i, n in enumerate(nums):
            _sum += n
            if _sum not in left_prefix:
                left_prefix[_sum] = i
        
        m = len(nums)
        result = m + 1
        _sum = 0
        for i in range(m, -1, -1):
            if i < m:
                _sum += nums[i]
            if x - _sum in left_prefix:
                result = min(result, left_prefix[x - _sum] + 1 + m - i)
        return result if result <= m else -1

"""
- two pointers / sliding window
- O(n), O(1)
- intuition: this problem is equal to finding the longest subarray with a sum equal to sum(nums) - x
- this solution can only handle positive numbers
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        _sum = 0
        removed = -1
        for right, n in enumerate(nums):
            _sum += n
            while _sum > target and left <= right:
                _sum -= nums[left]
                left += 1
            if _sum == target:
                removed = max(removed, right - left + 1)
        return len(nums) - removed if removed >= 0 else -1

"""
- two pointers / sliding window
- O(n), O(1)
- this solution can only handle positive numbers
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        _sum = sum(nums)
        n = len(nums)
        result = n + 1
        left = 0
        
        for right in range(n):
            _sum -= nums[right]
            while _sum < x and left <= right:
                _sum += nums[left]
                left += 1
            if _sum == x:
                result = min(result, (left + (n - 1 - right)))
        return result if result <= n else -1