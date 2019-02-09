import collections

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        - brutal force
        - time limit exceeded
        
        
        sums = [[0]*len(nums) for _ in nums]
        maxLen = 0
        
        for i in range(len(sums)):
            for j in range(i, len(sums)):
                if i == j:
                    sums[i][i] = nums[i]
                else:
                    sums[i][j] = sums[i][j-1] + nums[j]
                if sums[i][j] == k and j - i + 1 > maxLen:
                    maxLen = j - i + 1
        
        return maxLen
        """
    
        """
        - O(n)
        - range sum and hashtable
        - next: try do it in one pass
        """
        
        table = collections.defaultdict(list)
        maxLen = 0
        sums = [0] * (len(nums) + 1) # df: extra space for range sum at nums[0]
        
        sum_ = 0
        for i in range(1, len(sums)):
            sum_ += nums[i-1]
            sums[i] = sum_
            table[sum_].append(i)
        
        for i in range(len(sums)):
            if k+sums[i] in table:
                maxComplement = table[k+sums[i]][-1]
                maxLen = max(maxLen, maxComplement - i)
        
        return maxLen

sl = Solution()
print(sl.maxSubArrayLen([1, -1, 5, -2, 3], 3))