"""
- Dynamic programming
"""
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        N1, N2 = len(s1), len(s2)
        
        @lru_cache(None)
        def dp(i1, i2, diff): # encoding length diff
            if i1 == N1 and i2 == N2:
                return diff == 0
            if i1 < N1 and s1[i1].isdigit():
                if s1[i1] == "0": return False
                r1 = i1
                while r1 < len(s1) and s1[r1].isdigit(): 
                    r1 += 1
                for k1 in range(i1+1, r1+1): 
                    if dp(k1, i2, diff - int(s1[i1:k1])): 
                        return True
            elif i2 < N2 and s2[i2].isdigit():
                r2 = i2
                while r2 < len(s2) and s2[r2].isdigit(): 
                    r2 += 1
                for k2 in range(i2+1, r2+1): 
                    if dp(i1, k2, diff + int(s2[i2:k2])): 
                        return True
            # i1, i2 are letters
            elif diff == 0: 
                if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2]: 
                    return dp(i1+1, i2+1, 0)
            elif diff > 0: 
                if i1 < len(s1): 
                    return dp(i1+1, i2, diff-1)
            else: 
                if i2 < len(s2): 
                    return dp(i1, i2+1, diff+1)
            return False 
        
        return dp(0, 0, 0)