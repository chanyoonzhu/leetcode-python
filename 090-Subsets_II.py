"""
- backtracking
- O(n* 2^n), O(n) - excluding result arr
- similar problem:78-Subsets
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(nums, path):
            result.append(path)
            i = 0
            prev = -11
            while i < len(nums):
                if nums[i] != prev: # skip same path (num has to be sorted)
                    backtrack(nums[i+1:], path + [nums[i]])
                    prev = nums[i]
                i += 1
          
        backtrack(sorted(nums), [])
        return result