"""
- line sweep
- O(nlogn), O(n)
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        loc_info = []
        for p, start, end in trips:
            loc_info.append((start, p))
            loc_info.append((end, -p))
        loc_info.sort()
        
        load = 0
        for _, delta in loc_info:
            load += delta
            if load > capacity:
                return False
        return True