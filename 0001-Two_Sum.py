"""
- Questions:
    * Can same element be used twice?
    * duplicate numbers?
    * many solutions?
    * no solution?
- Caveats:
    * same number can appear multiple times - dic has to store list
    * same idx cannot be used multiple times - if statement
- Solution:
    * O(n), O(n)
    * hash-table one pass
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = dict()
        for i, n in enumerate(nums):
            if target - n in indexes:
                return [indexes[target - n ], i]
            indexes[n] = i