"""
- hashmap
- O(len(s))
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = ""
        
        for c in order: # O(26) -> O(1)
            if counter[c]:
                res += c * counter[c]
                del counter[c]
        
        for c in counter: #O(len(s))
            res += c * counter[c]
        
        return res