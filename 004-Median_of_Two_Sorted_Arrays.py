"""
- two pointers
- O(m + n), O(1) 
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
       
        end = n // 2    
        i, i1, i2  = 0, 0, 0             # Pointer for implict merge list, nums1 pointer, nums2 pointer 
        current, previous = 0, 0         # current and previous value in implict merge
        
        # Implictly build half of the sorted merge list
        # but only save last values
        while i <= end:
            previous = current
            if i1 == n1:                 # First list is exhausted ==> choose from second list
                current = nums2[i2] 
                i2 += 1
            elif i2 == n2:               # Second list ist exhaused ==> choose from first list
                current = nums1[i1]
                i1 += 1
            elif nums1[i1] < nums2[i2]:  # Choose element from first list
                current = nums1[i1]
                i1 += 1
            else:                        # Choose element from second list
                current = nums2[i2]      
                i2 += 1

            i += 1
        
        if n % 2 == 0:
            return (previous + current) / 2.0
        else: 
            return current


"""
- binary search
- intuition: same as finding the kth largest element
- O(log(m + n)), O(m + n) 
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

