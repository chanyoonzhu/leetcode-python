"""
- backtrack
- O(n x n!), O(n!)
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
         
        result = []
        
        def backtrack(nums, path):
            if not nums:
                result.append(path)
            else:
                prev, i = -11, 0 # key: dedup: same number only picked once for a slot
                while i < len(nums):
                    if nums[i] != prev:
                        backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])
                        prev = nums[i]
                    i += 1
                    
        backtrack(sorted(nums), [])
        return result