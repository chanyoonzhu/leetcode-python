"""
- hashmap
- O(n), O(n)
"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
                
        for c in t:
            if c in counts:
                counts[c] -= 1
                if counts[c] == 0:
                    del counts[c]
        
        return sum(counts.values())