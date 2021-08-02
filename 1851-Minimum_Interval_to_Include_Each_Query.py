"""
- greedy with priority queue
- O(max(nlogn, qlogq))
"""
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1] * len(queries)
        intervals.sort()
        queries_info = [(n, i) for i, n in enumerate(queries)]
        queries_info.sort() # key: sort the queries
        h = []
        N = len(intervals)
        interval_i = 0
        
        for q, query_i in queries_info:
            while interval_i < N and intervals[interval_i][0] <= q:
                start, end = intervals[interval_i]
                heapq.heappush(h, (end - start + 1, end))
                interval_i += 1
            while h and h[0][1] < q:
                heapq.heappop(h)
            if h:
                result[query_i] = h[0][0]
        return result