"""
- greedy with sort
- O(nlogn), O(n)
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i = 0
        remaining = truckSize
        res = 0
        while remaining and i < len(boxTypes):
            box_count = min(remaining, boxTypes[i][0])
            res += box_count * boxTypes[i][1]
            remaining -= box_count
            i += 1
        
        return res