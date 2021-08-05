"""
- random with binary search
"""
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.ranges = []
        total = 0
        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(total)
        

    def pick(self) -> List[int]:
        n = random.randint(1, self.ranges[-1])
        i = bisect.bisect_left(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i]
        return [random.randint(x1, x2), random.randint(y1, y2)]