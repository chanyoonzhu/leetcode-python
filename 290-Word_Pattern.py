"""
- hashmap
- hashmap + hashset
- O(n), O(1)
"""     
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        mapping = {} # mapping: word -> char
        assigned = set() # assigned char
        for p, w in zip(list(pattern), words):
            if w not in mapping:
                if p in assigned: # easy to miss: bidirectional check
                    return False
                mapping[w] = p
                assigned.add(p)
            else:
                if mapping[w] != p:
                    return False
        return True