"""
- two pointers
- O(max(m, n)), O(1)
"""     
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  
        i = j = 0
        while i < len(s):
            if j >= len(t):
                return False
            if s[i] == t[j]: # greedily cancels on the first match
                i += 1
            j += 1
        return True

"""
- hashmap
- for follow up: what if we need to test on a stream of incoming s?
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  
        c_to_pos = defaultdict(list)
        for i, c in enumerate(t):
            c_to_pos[c].append(i)
        right_pos = -1
        for c in s:
            if not c_to_pos[c]: return False
            i = bisect.bisect(c_to_pos[c], right_pos)
            if i >= len(c_to_pos[c]): return False
            right_pos = c_to_pos[c][i]
        return True

"""
- dynamic programming (top-down) - not the optimal solution: can be more greedy!
- O(mn), O(mn)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if i < 0: return True
            if j < 0: return False
            is_subseq = dp(i, j - 1) # not matching
            if s[i] == t[j]:
                is_subseq |= dp(i - 1, j - 1)
            return is_subseq
        
        return dp(len(s) - 1, len(t) - 1)
                
            
        