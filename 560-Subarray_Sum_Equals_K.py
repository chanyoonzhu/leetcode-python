from collections import defaultdict

class Solution(object):
    """
    - cumulative sum: time exceeded
    - O(n^2), O(n)
    """
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
    - hashmap
    - O(n), O(n)
    """
    def subarraySum_hashmap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _sum, sums = 0, defaultdict(int)
        sums[0] = 1 # easy to miss, for where the number itself equals k
        res = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum - k in sums:
                res += sums[_sum - k]
            sums[_sum] += 1
        return res
                    
s = Solution()
# s.subarraySum([1,1,1], 2)
s.subarraySum_hashmap([1,2,3], 3)