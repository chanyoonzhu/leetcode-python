"""
- obvious (yet space-consuming) solution
- initialization: O(n * k), O(n * k), pick: O(1), O(1)
- MLE
"""
import random

class Solution:

    def __init__(self, w: list[int]):
        self.samples = []
        for i, weight in enumerate(w):
            self.samples.extend([i] * weight)
        
    def pickIndex(self) -> int:
        return self.samples[random.randint(0, len(self.samples) - 1)]

"""
- prefix-sum with binary search
- initialization: O(n), O(n), pick: O(logn), O(1)
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

"""
- prefix-sum with binary search (with bisect)
- initialization: O(n), O(n), pick: O(log1), O(1)
"""
class Solution:

    def __init__(self, w: List[int]):
        self.weight_prefixes = [w[0]]
        for weight in w[1:]:
            self.weight_prefixes.append(self.weight_prefixes[-1] + weight)
        

    def pickIndex(self) -> int:
        weight = random.randint(1, self.weight_prefixes[-1])
        return bisect.bisect_left(self.weight_prefixes, weight)   