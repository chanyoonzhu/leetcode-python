"""
- hashmap
- init: O(n), O(n); pick: O(1), O(n)
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.num_to_idx = self._prepare(nums)
        
    def _prepare(self, nums):
        num_to_idx = defaultdict(list)
        for i, x in enumerate(nums):
            num_to_idx[x].append(i)
        return num_to_idx
    
    def pick(self, target):
        indexes = self.num_to_idx[target]
        return indexes[random.randint(0, len(indexes) - 1)]

"""
- reservoir sampling - suitable for array of a large size 
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