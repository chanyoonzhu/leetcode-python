"""
- linear iteration
- O(nlogn), O(n)
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(1, len(nums)):
            result = max(result, nums[i] - nums[i - 1])
        return result

"""
- bucket sort
- intuition: https://leetcode.com/problems/maximum-gap/discuss/330028/Explaining-the-bucket-method-in-layman-terms-%2B-python-code
    - group as many adjacent(sorted) numbers into the same bucket as possible, but at the same time make the bucket size the minimum possible value of the maximum gap such that 
    the two numbers that form the maximum gap don't fall into the same bucket (the pigeon hole principle).
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2 or min(nums) == max(nums):
            return 0
        
        _min, _max = float("inf"), float("-inf")
        for n in nums:
            _min = min(_min, n)
            _max = max(_max, n)
        
        buckets = [[float("inf"), float("-inf")] for _ in range(N - 1)]
        
        bucket_size = ceil((_max - _min) / (N - 1)) # min gap (ceil)
        
        for n in nums:
            if n != _min and n != _max:
                index = (n - _min) // bucket_size
                buckets[index] = [min(buckets[index][0], n), max(buckets[index][1], n)]
        
        result = -float('inf')
        previous_max = _min
        for i in range(len(buckets)):
            if buckets[i][0] != float("inf"): # skip empty bucket
                result = max(result, buckets[i][0] - previous_max)
                previous_max = buckets[i][1]
        result = max(result, _max - previous_max)
        
        return result