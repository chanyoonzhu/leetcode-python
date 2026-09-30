"""
- backtracking
- O(n*2^n), O(n)
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(nums, path):
            if len(path) >= 2:
                result.append(path)
            visited = set()
            for i in range(len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in visited:
                    visited.add(nums[i])
                    backtrack(nums[i+1:], path + [nums[i]])
        
        backtrack(nums, [])
        return result

"""
- bitmasking
- O(n*2^n), O(n)
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        candidates, result = [], []
        for mask in range(2 ** n):
            subsequence = []
            for i in range(n):
                if mask & (1 << (n - 1 - i)):
                    if not subsequence or nums[i] >= subsequence[-1]:
                        subsequence.append(nums[i])
                    else:
                        break
            if len(subsequence) >= 2:
                candidates.append(subsequence)
        # dedup
        candidates.sort()
        for cand in candidates:
            if not result or cand != result[-1]:
                result.append(cand)
        return result