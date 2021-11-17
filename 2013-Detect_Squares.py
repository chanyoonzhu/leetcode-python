"""
- hashmap
- O(n), O(n)
"""
class DetectSquares:

    def __init__(self):
        self.xs = defaultdict(list)
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xs[x].append(y)
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for y2 in self.xs[x1]:
            if y2 == y1: continue  # easy to miss: skip square side len == 0
            sideLen = abs(y2 - y1)

            for x3 in x1 - sideLen, x1 + sideLen:
                y3, x4, y4 = y2, x3, y1
                res += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

        return res