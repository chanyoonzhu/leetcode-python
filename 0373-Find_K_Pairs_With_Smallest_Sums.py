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
- priority queue
- intuition: if current smallest is nums1[i] + nums2[j], the next smallest can only be nums1[i + 1] + nums2[j] or nums1[i] + nums2[j + 1]
- O(klog(k))
"""
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set((0, 0))
        N1, N2 = len(nums1), len(nums2)
        
        while len(result) < k and heap: # easy to miss: check heap
            _, i1, i2 = heapq.heappop(heap)
            result.append((nums1[i1], nums2[i2]))
            
            if i1 < N1 - 1 and (i1 + 1, i2) not in visited:
                heapq.heappush(heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
                visited.add((i1 + 1, i2))
                
            if i2 < N2 - 1 and (i1, i2 + 1) not in visited:
                heapq.heappush(heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                visited.add((i1, i2 + 1))
            
        return result

"""
solution: heap
intuition: if current smallest is nums1[i] + nums2[j], the next smallest can only be nums1[i + 1] + nums2[j] or nums1[i] + nums2[j + 1]
easy to miss: dedup
- O(klog(k))
"""
import heapq
class SolutionMock:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        res = []
        heap = [(nums1[0] + nums2[0], 0, 0)] # sum, idx1, idx2
        visited = set((0, 0)) # easy to miss, dedup
        N1, N2 = len(nums1), len(nums2)
        for _ in range(k):
            if not heap:
                break
            _, idx1, idx2 = heapq.heappop(heap)
            res.append([nums1[idx1], nums2[idx2]])
            if idx1 < N1 - 1 and (idx1+1, idx2) not in visited: # easy to miss: idx1+1, idx2 can be reached from idx1, idx2 and idx1+1, idx2-1, need to dedup
                heapq.heappush(heap, (nums1[idx1+1] + nums2[idx2], idx1 + 1, idx2))
                visited.add((idx1+1, idx2))
            if idx2 < N2 - 1 and (idx1, idx2+1) not in visited:
                heapq.heappush(heap, (nums1[idx1] + nums2[idx2+1], idx1, idx2 + 1))
                visited.add((idx1, idx2+1))
        return res

# test case 1:
nums1 = [1, 7, 11] 
nums2 = [2, 4, 6]
k = 3
# [[1,2],[1,4],[1,6]]

s = SolutionMock()
s.kSmallestPairs(nums1, nums2, k)