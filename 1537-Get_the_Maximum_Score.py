class Solution:
    """
    - sliding window - my solution
    - O(m + n), O(1)
    """
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        part_total1 = part_total2 = total = 0 # part_total1 and part_total2 tracks the sum in between two shared points
        mod = 10 ** 9 + 7
        i1 = i2 = 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                total += (max(part_total1, part_total2) + nums1[i1])
                part_total1 = part_total2 = 0
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                part_total1 += nums1[i1]
                i1 += 1
            else:
                part_total2 += nums2[i2]
                i2 += 1
        while i1 < n1:
            part_total1 += nums1[i1]
            i1 += 1
        while i2 < n2:
            part_total2 += nums2[i2]
            i2 += 1
        total += max(part_total1, part_total2)
        
        return total % mod
    
    """
    - sliding window - better solution
    - O(m + n), O(1)
    """
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        total1 = total2 = 0
        mod = 10 ** 9 + 7
        i1 = i2 = 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 or i2 < n2:
            if i1 < n1 and (i2 == n2 or nums1[i1] < nums2[i2]):
                total1 += nums1[i1]
                i1 += 1
            elif i2 < n2 and (i1 == n1 or nums1[i1] > nums2[i2]):
                total2 += nums2[i2]
                i2 += 1
            else:
                total1 = total2 = max(total1, total2) + nums1[i1]
                i1 += 1
                i2 += 1
        
        return max(total1, total2) % mod