import heapq

class KthLargest(object):
    
    """
    - time limit exceeded
    - Overkill, only need a heap for largest elements, rest not care
    
    def __init__(self, k, nums):
        self.heap = [-n for n in nums]
        self.k = k
        heapq.heapify(self.heap)
        

    def add(self, val):
        kLargest = []
        heapq.heappush(self.heap, -val)
        for i in range(self.k):
            kLargest.append(heapq.heappop(self.heap))
        res = -kLargest[-1]
        for i in range(self.k):
            heapq.heappush(self.heap, kLargest[i])
        return res
    """

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # df: initial nums size may be smaller than k
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
            

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(2, [0])
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(3))