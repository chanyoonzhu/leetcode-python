"""
- binary search
"""
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        lo, hi = 0, sum(ribbons) // k
        
        def canCut(l):
            total = 0
            for ribbon in ribbons:
                total += ribbon // l
            return total >= k
        
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if canCut(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo