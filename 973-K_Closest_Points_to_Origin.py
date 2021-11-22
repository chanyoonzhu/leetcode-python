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
        
        l, r = 0, N - 1
        pivot_index = r
        while l <= r:
            pivot_index = self.partition(dists, l, r)
            if pivot_index == k - 1:
                return [points[i] for _, i in dists[:k]]
            if pivot_index < k - 1:
                left = pivot_index + 1
            else:
                right = pivot_index - 1        
    
    
    def getDistSquared(self, point: List[int]) -> int:
        x, y = point
        return x ** 2 + y ** 2

    
    def partition(self, dists, l, r):
        end = dists[r][0]
        idx = l
        for i in range(l, r):
            if dists[idx][0] <= end:
                dists[idx], dists[i] = dists[i], dists[idx]
                idx += 1
        dists[idx], dists[r] = dists[r], dists[idx]
        return idx
