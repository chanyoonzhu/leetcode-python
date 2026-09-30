"""
- monotonically increasing stack
- O(n), O(n)
"""
class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        span = 1
        while self.s and self.s[-1][0] <= price:
            span += self.s.pop()[1]
        self.s.append((price, span))
        return span