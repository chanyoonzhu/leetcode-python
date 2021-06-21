"""
- backtracking
- O(n* 2^n), O(n) - excluding result arr
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(nums, path):
            result.append(path)
            for i in range(len(nums)):
                backtrack(nums[i+1:], path + [nums[i]])
          
        backtrack(nums, [])
        return result

"""
- bit mask
- todo
"""