"""
- backtrack
- O(n x n!), O(n!)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, part):
            if not nums:
                result.append(part)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i] + nums[i + 1:], part + [nums[i]])
        
        result = []
        backtrack(nums, [])
        return result