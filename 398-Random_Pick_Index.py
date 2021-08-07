"""
- hashmap
- init: O(n), O(n); pick: O(1), O(n)
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.indexes_mapping = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.indexes_mapping[n].append(i)

    def pick(self, target: int) -> int:
        indexes = self.indexes_mapping[target]
        rand_i = random.randint(0, len(indexes) - 1)
        return indexes[rand_i]

"""
- reservoir sampling
- init: O(n), O(n); pick: O(n), O(1)
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def pick(self, target):
        result = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                if random.randint(1, count) == 1:
                    result = i
        return result