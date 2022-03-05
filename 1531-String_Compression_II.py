"""
- dynamic programming (top-down)
- wrong intuition: delete single characters greedily. Counter example: "xyzaabbbaa", deleting "bbb" get xyza4 which is shorter
- can't use greedy, need to backtrack with memoization
"""
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
                
        @lru_cache(None)
        def dp(i, prev_c, prev_len, k): # encoded length of s[i:] with k deletions remain
            if i == len(s):
                return 0
            
            min_run_length = float("inf")
            # delete i
            if k > 0:
                min_run_length = dp(i+1, prev_c, prev_len, k-1)
                
            # not deleting i
            if s[i] == prev_c:
                added_length = 0
                if prev_len == 1 or len(str(prev_len + 1)) > len(str(prev_len)):
                    added_length = 1
                min_run_length = min(min_run_length, added_length + dp(i+1, prev_c, prev_len+1, k))
            else:
                min_run_length = min(min_run_length, 1 + dp(i+1, s[i], 1, k))
            return min_run_length
                
        return dp(0, "", 0, k)