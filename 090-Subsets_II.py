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

"""
- enumeration with bit-masking
- O(n* 2^n), O(n) - excluding result arr
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        result = []
        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if(i & (1 << j)):
                    subset.append(nums[j])
            if(subset not in result):
                result.append(subset)
                
        return result