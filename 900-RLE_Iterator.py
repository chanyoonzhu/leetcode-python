"""
- one pointer
- O(n), O(n)
"""
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.values = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.values) and n > self.values[self.index]:
            n -= self.values[self.index]
            self.index += 2
        if self.index == len(self.values): return -1 # edge case
        self.values[self.index] -= n # modifies value in-place to simplify calculation
        return self.values[self.index + 1]