"""
- greedy (*2) with priority queue 
- O(n*(logn+logk)), O(n)
"""
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7
        
        candidates = sorted(zip(efficiency, speed), key=lambda c: -c[0]) # greedily compute candidates with higher efficiency sooner
        
        h = []
        speed_sum = perf= 0
        for e, s in candidates:
            heapq.heappush(h, s)
            speed_sum += s
            if len(h) > k: # when more than target candidates are selected, greedily remove candidates with lowest speed
                speed_sum -= heapq.heappop(h)
            
            perf = max(perf, speed_sum * e)
        
        return perf % modulo