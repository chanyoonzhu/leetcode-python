class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        @lru_cache(None)
        def dp(i, target):
            if target < 0: return False # pruning
            if i == -1:
                return True if target == 0 else False
            for n in mat[i]:
                if dp(i - 1, target - n):
                    return True
            return False
        
        diff = 0
        while True:
            if dp(len(mat) - 1, target + diff) or dp(len(mat) - 1, target - diff):
                return diff
            diff += 1

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:      
        maxx = sum([max(arr) for arr in mat])
        if maxx <= target: return target - maxx
        
        prev_dp = [True] + [False] * maxx
        for i in range(len(mat)):
            dp = [False] * (maxx + 1)
            for j in range(len(prev_dp)):
                if prev_dp[j]:
                    for n in mat[i]:
                        dp[j + n] = True
            prev_dp = dp
        
        diff = 0
        while True:
            if target + diff < len(prev_dp) and prev_dp[target + diff]:
                return diff
            if target - diff >= 0 and prev_dp[target - diff]:
                return diff
            diff += 1