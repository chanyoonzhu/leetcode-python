"""
- hashmap
- hashmap + hashset
- O(n), O(1)
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = list(pattern)
        words = s.split()
        if len(patterns) != len(words):
            return False
        
        mapping, mapped = {}, set() # mapping: a -> "dog"
        for i, word in enumerate(words):
            pattern = patterns[i]
            if pattern in mapping:
                if mapping[pattern] != word:
                    return False
            else:
                if word in mapped:
                    return False
                mapping[pattern] = word
                mapped.add(word)
        return True
        