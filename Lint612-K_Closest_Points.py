def kClosest(self, points, origin, k):
    # write your code here
    
    import heapq
    
    def getDistance(a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
        
    heap, res = [], []
    for point in points:
        distance = getDistance(point, origin)
        # '-' for max heap
        heapq.heappush(heap, [-distance, -point.x, -point.y])
        if len(heap) > k:
            heapq.heappop(heap)
        
    for _ in range(len(heap)):
        point = heapq.heappop(heap)
        # reverse pop order by insertion at 0
        res.insert(0, [-point[1], -point[2]])
    
    return res