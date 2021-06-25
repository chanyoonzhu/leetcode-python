"""
- greedy with sort and two pointers
- O(nlogn + mlogm), O(logm + logn)
"""
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if (sum1 > sum2):
            return self.minOperations(nums2, nums1)
        
        nums1.sort(), nums2.sort()
        i, j = 0, len(nums2) - 1
        result = 0
        while (sum1 < sum2):
            if i == len(nums1) and j < 0:
                return -1
            if j < 0 or i < len(nums1) and 6 - nums1[i] > nums2[j] - 1:
                sum1 += 6 - nums1[i]
                i += 1
            else: 
                sum2 -= nums2[j] - 1
                j -= 1
            result += 1
        return result