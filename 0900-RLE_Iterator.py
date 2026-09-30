"""
- one pointer
- O(n), O(n)
"""
class RLEIterator:

    # O(n)
    def __init__(self, encoding: List[int]):
        self.values = encoding
        self.index = 0

    # O(n)
    def next(self, n: int) -> int:
        while self.index < len(self.values) and n > self.values[self.index]:
            n -= self.values[self.index]
            self.index += 2
        if self.index == len(self.values): return -1 # edge case
        self.values[self.index] -= n # modifies value in-place to simplify calculation
        return self.values[self.index + 1]

"""
- prefix sum + binary search
"""
class RLEIterator:

    # O(n)
    def __init__(self, encoding: List[int]):
        self.prefix_sum_encoding = self._buildEncoding(encoding)
        self.exhausted = 0
        
    def _buildEncoding(self, encoding):
        if not encoding:
            return []
        res = []
        for i in range(0, len(encoding), 2):
            count = encoding[i]
            x = encoding[i+1]
            if count == 0:
                continue
            if not res:
                res.append([count, x])
            elif x == res[-1][1]:
                res[-1][0] += count
            else:
                res.append([res[-1][0] + count, x])
        return res

    # O(logn)         
    def next(self, n: int) -> int:
        self.exhausted += n
        idx = bisect.bisect_left(self.prefix_sum_encoding, [self.exhausted, 0])
        if idx == len(self.prefix_sum_encoding):
            return -1
        return self.prefix_sum_encoding[idx][1]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)