"""
- priority queue
- O(tlogt), O(t)
"""
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        N = len(tasks)
        tasks_sorted = sorted([(tasks[i][0], tasks[i][1], i) for i in range(N)], key=lambda x: x[0])
        res = []
        h = [] # processing time, idx
        
        i = tasks_sorted[0][0]
        while len(res) < len(tasks):
            while tasks_sorted and tasks_sorted[0][0] <= i:
                _, processing_time, idx = tasks_sorted.pop(0)
                heapq.heappush(h, (processing_time, idx))
            if h:
                processing_time, idx = heapq.heappop(h)
                res.append(idx)
                i += processing_time
            else: # easy to miss, no start time is smaller than i, need to go with the next start time
                i = tasks_sorted[0][0] 
        return res