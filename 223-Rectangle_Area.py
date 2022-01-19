"""
- math
"""
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        cx1, cx2, cy1, cy2 = max(ax1, bx1), min(ax2, bx2), max(ay1, by1), min(ay2, by2)
        return area - max((cx2 - cx1), 0) * max((cy2 - cy1), 0) # if cx2 - cx1 < 0, or cy2 < cy1, there's no overlap, minus 0
        