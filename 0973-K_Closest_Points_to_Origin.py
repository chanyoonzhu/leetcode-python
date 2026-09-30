"""
- priority queue
- O(klogn)， O(n)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        N = len(points)
        
        heap = [(self.getDistSquared(points[i]), i) for i in range(N)]
        heapq.heapify(heap)
        return [points[i] for _, i in heapq.nsmallest(k, heap)]
        
    def getDistSquared(self, point: List[int]) -> int:
        x, y = point
        return x ** 2 + y ** 2

"""
- priority queue
- O(nlogk)， O(k)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        N = len(points)
        
        heap = [(-self.getDistSquared(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        
        for i in range(k, N):
            heapq.heappush(heap, (-self.getDistSquared(points[i]), i))
            heapq.heappop(heap)
            
        return [points[i] for _, i in heap]
        
    def getDistSquared(self, point: List[int]) -> int:
        x, y = point
        return x ** 2 + y ** 2
    
"""
- quick select
- O(n), O(n)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        N = len(points)
        dists = [(self.getDistSquared(points[i]), i) for i in range(N)]
        
        
        l, r = 0, len(dists) - 1
        while l <= r:
            idx = self.partition(dists, l, r)
            if idx == k - 1:
                return [points[i] for dist, i in dists[:k]]
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1
        
            
    def partition(self, dists, start, end):
        pivot = dists[end][0]
        idx = start
        for i in range(start, end):
            if dists[i][0] <= pivot:
                dists[i], dists[idx] = dists[idx], dists[i]
                idx += 1
        dists[end], dists[idx] = dists[idx], dists[end]
        return idx
    
    def getDistSquared(self, point: List[int]) -> int:
        x, y = point
        return x ** 2 + y ** 2
