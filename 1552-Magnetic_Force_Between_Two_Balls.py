"""
- binary search + greedy
- O(nlogn + nlogMax(position)), O(1)
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if self.canAllocate(mid, m, position):
                lo = mid
            else:
                hi = mid - 1
        return lo
    
    def canAllocate(self, min_dist, m, position):
        next_min_pos = position[0] + min_dist
        m -= 1
        for pos in position:
            if pos >= next_min_pos:
                m -= 1
                if m == 0:
                    return True
                next_min_pos = pos + min_dist
        return False