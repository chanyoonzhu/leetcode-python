"""
- binary search
- O(log(sum(weights))), O(1)
"""
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        r = sum(weights)
        l = max(weights)
        
        def can_ship(capacity):
            days_taken = 0
            remain_capacity = capacity
            for w in weights:
                if w <= remain_capacity:
                    remain_capacity -= w
                else:
                    days_taken += 1
                    if days_taken >= D:
                        return False
                    remain_capacity = capacity - w # easy to miss: need to subtract w
            return True
        
        while l < r:
            mid = l + (r - l) // 2
            if can_ship(mid):
                r = mid
            else:
                l = mid + 1
        return l