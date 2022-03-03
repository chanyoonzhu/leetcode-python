"""
- 1D array
- O(n), O(n)
"""
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        res = -1
        min_dist = float("inf")
        for i in range(len(points)):
            xb, yb = points[i]
            if x != xb and y != yb:
                continue
            dist = abs(xb - x) + abs(yb - y)
            if dist < min_dist:
                min_dist = dist
                res = i
        return res