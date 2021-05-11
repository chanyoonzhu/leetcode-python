"""
- default comparator: Python2
- O(nlogn) for sorting, O(n)
"""
def compare(a, b):
    if a + b > b + a: return 1
    if a + b == b + a: return 0
    return -1

class Solution:
    def largestNumber(self, nums):
        if not any(map(bool, nums)): return '0' # edge case: [0, 0] -> '0'
        return ''.join(sorted([str(n) for n in nums], cmp = compare, reverse = True))

"""
- default comparator: Python3
- O(nlogn) for sorting, O(n)
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        compare = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0
        if not any(map(bool, nums)): return '0'
        return ''.join(sorted([str(n) for n in nums], key=functools.cmp_to_key(compare)))