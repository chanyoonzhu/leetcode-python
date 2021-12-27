"""
- backtracking
- O(2^n), O(n)
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        res = []
            
        def backtrack(i, path, target):
            if target == 0:
                res.append(path)
            for k in range(i, N):
                x = candidates[k]
                if k > i and candidates[k] == candidates[k-1]: # TLE without this: skip repetitive number, res no need to dedup
                    continue
                if x <= target:
                    backtrack(k + 1, path + [x], target - x)
                    
        backtrack(0, [], target)
        return list(res)
                
        

"""
- bitmasking
- TLE
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        bitmask = 2 ** N - 1
        res = set()
        
        def getPath(bitmask):
            path = []
            for i in range(N):
                if not bitmask & (1 << i):
                    path.append(candidates[i])
            return tuple(path)
            
        def backtrack(bitmask, target):
            if target == 0:
                res.add(getPath(bitmask))
            for i in range(N):
                if bitmask & (1 << i) and candidates[i] <= target:
                    backtrack(bitmask ^ (1 << i), target - candidates[i])
                    
        backtrack(bitmask, target)
        return list(res)