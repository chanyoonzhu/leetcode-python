"""
- obvious (yet space-consuming) solution
- initialization: O(n * k), O(n * k), pick: O(1), O(1)
- time limit exceeded
"""
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.samples = []
        for i, n in enumerate(w):
            self.samples.extend([(n, i)] * n)

    def pickIndex(self) -> int:
        _, index = self.samples[random.randint(0, len(self.samples) - 1)]
        return index

"""
- prefix-sum with binary search
- initialization: O(n), O(1), pick: O(1), O(1)
"""
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.w[-1])
        l, r = 0, len(self.w) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.w[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l