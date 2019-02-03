class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        """
        - O(n), O(n)
        """
        
        def getDistance(pointA, pointB):
            return (pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2
        
        origin = [0, 0]
        
        import heapq
        heap = []
        
        for point in points:
            heap.append((-getDistance(point, origin), point))
            
        heapq.heapify(heap)
        
        while len(heap) > K:
            heapq.heappop(heap)
            
        res = [p[1] for p in heap]
        
        return res