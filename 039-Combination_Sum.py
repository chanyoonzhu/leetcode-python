"""
- dynamic programming (0/n knapsack)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        dp = [set() for _ in range(1 + target)] # dp[i] stores all the unique paths (as tuples) to reach target i
		# dp initialization
        for cand in candidates:
            if cand <= target:
                dp[cand].add((cand,)) # easy to miss: one item tuple needs a trailing comma
        
		# dp
        for x in range(1, target + 1):
            for cand in candidates:
                for path in dp[x]:
                    if x + cand <= target:
                        next_path = sorted(list(path) + [cand])
                        dp[x + cand].add(tuple(next_path))
        
        return [list(t) for t in dp[-1]]

"""
- backtracking
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = set()
        M = len(candidates)
        
        def backtrack(path, total):
            if total == target:
                result.add(tuple(sorted(path)))
            elif total > target:
                return
            else:
                for c in candidates:
                    backtrack(path + [c], total + c)
        
        backtrack([], 0)
        return [list(p) for p in result]