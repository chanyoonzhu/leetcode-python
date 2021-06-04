"""
- binary search + greedy
- O(nlogn + nlogMax(position)), O(1)
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1, position[-1] - position[0]
        
        def can_distribute(x):
            remain = m - 1
            cur_pos = position[0]
            for pos in position:
                if pos - cur_pos >= x:
                    remain -= 1
                    if remain <= 0:
                        return True
                    cur_pos = pos
            return False
        
        while low < high:
            mid = low + (high - low + 1) // 2
            if can_distribute(mid):
                low = mid
            else:
                high = mid - 1
        return low