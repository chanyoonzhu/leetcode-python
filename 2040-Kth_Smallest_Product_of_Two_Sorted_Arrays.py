"""
- heap
- O(mn + klog(mn))
- TLE
"""
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        h = []
        for x1 in nums1:
            for x2 in nums2:
                h.append(x1 * x2)
                
        heapq.heapify(h)
        res = 0
        for _ in range(k):
            res = heapq.heappop(h)
            
        return res

"""
- binary search
"""
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l1, l2 = len(nums1), len(nums2)
        lo, hi = -10**10 - 1, 10**10 + 1
        
        def nth(x):
            count = 0
            for x1 in nums1:
                if x1 > 0: 
                    count += bisect_right(nums2, x // x1)
                elif x1 < 0: 
                    count += len(nums2) - bisect_left(nums2, ceil(x / x1))
                elif x1 == 0 and x >= 0: 
                    count += len(nums2)
            return count
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nth(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo