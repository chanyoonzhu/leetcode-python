from heapq import *

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        """
        O(n^2)
        - brute force
        
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        res = []
        
        import heapq
        hp = [[i + j, i, j] for j in nums2 for i in nums1]
        heapq.heapify(hp)
        
        while hp and len(res) < k:
            sum, i, j = heapq.heappop(hp)
            res.append([i, j])
            
        return res
        """
        
        """
        O(klog(k))
        - keep a heap, after popping the smallest at nums1[i], nums2[j],
        - add nums1[i+1], nums1[j] and nums[j+1], nums[i] to the heap 
        """
        res, hp, visited = [], [], []
        
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        heappush(hp, [nums1[0] + nums2[0], 0, 0])
        visited.append([0,0])
        
        while hp and len(res) < k:
            sum, i, j = heappop(hp)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and [i+1,j] not in visited:
                heappush(hp, [nums1[i+1] + nums2[j], i+1, j])
                visited.append([i+1,j])
            if j + 1 < len(nums2) and [i,j+1] not in visited:
                heappush(hp, [nums1[i] + nums2[j+1], i, j+1])
                visited.append([i,j+1])
        return res
            