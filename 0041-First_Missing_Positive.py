"""
- hashset
- O(n), O(n)
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        x = 1
        while True:
            if x not in all_nums:
                return x
            x += 1

"""
- array modify in-memory
- todo: https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
"""
