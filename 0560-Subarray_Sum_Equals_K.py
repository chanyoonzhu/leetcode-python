from collections import defaultdict

"""
- prefix sum
- O(n^2), O(n)
- TLE
"""
class Solution(object):
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        res = 0
        sums = [0] * (n+1) # has to allocate one more space, or would miss cases where some number is directly equal to k
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]
        for i in range(n+1):
            for j in range(i+1, n+1):
                if sums[j] - sums[i] == k:
                    res += 1                  
        return res

"""
- prefix sum with hashmap
- O(n), O(n)
- similar problem: 437(tree)
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _sum = 0
        prefixes = collections.Counter({0: 1})
        result = 0
        for n in nums:
            _sum += n
            result += prefixes[_sum - k]
            prefixes[_sum] += 1
        return result
                    
s = Solution()
# s.subarraySum([1,1,1], 2)
s.subarraySum_hashmap([1,2,3], 3)