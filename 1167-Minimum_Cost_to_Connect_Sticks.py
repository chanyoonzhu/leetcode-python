"""
- greedy with heap: merge the shortest two sticks first
- O(nlogn), O(n)
"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        h = sticks[:]
        heapq.heapify(h)
        res = 0
        while len(h) > 1:
            cost = heapq.heappop(h) + heapq.heappop(h)
            res += cost
            heapq.heappush(h, cost)
        return res
        