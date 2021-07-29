"""
- greedy with priority queue
- O(dlogn) d: max day, n: len(events)?
"""
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        q = [] # keeps available events on current day
        result = 0
        days = max(end for _, end in events)
        i_event = 0
        for day in range(1, days + 1):
            while q and q[0] < day:
                heapq.heappop(q)
            while i_event < len(events) and day >= events[i_event][0]:
                heapq.heappush(q, events[i_event][1])
                i_event += 1
            if q:
                heapq.heappop(q) # greedily attend event that ends sooner
                result += 1
        return result