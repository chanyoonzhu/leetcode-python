"""
- binary with greedy
- O(logN), O(1)
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour): return -1 # caveat: need to ceil the hour
        
        def can_arrive(speed):
            total = 0
            for d in dist[:-1]:
                total += ceil(d / speed)
                if total > hour:
                    return False
            total += dist[-1] / speed # caveat: time taken for last dist can be float
            return total <= hour
        
        low, high = 1, 10 ** 7
        # low, high = 1, max(dist) # this is wrong [1,1,100000] 2.01 -> should be 10000000 > 100000
        while low < high:
            mid = low + (high - low) // 2
            if can_arrive(mid):
                high = mid
            else:
                low = mid + 1
        return low