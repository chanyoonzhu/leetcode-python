"""
- backtracking
- O(n*2^n), O(n)
"""
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        result = []
    
        def backtrack(nums, path):
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: # skip duplicates
                    continue
                if path and not square(path[-1] + nums[i]):
                    continue
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        def square(num):
            return int((num) ** 0.5) ** 2 == num
        
        backtrack(sorted(nums), [])
        return len(result)