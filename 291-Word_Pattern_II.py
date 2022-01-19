"""
- backtrack with hashmap
- O(n), O(1)
"""
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.backtrack(s, 0, pattern, 0, {})
        
    def backtrack(self, s, i, p, j, mapping):
        n_s, n_p = len(s), len(p)
        if i == n_s and j == n_p:
            return True
        if i >= n_s or j >= n_p:
            return False
        pattern = p[j]
        if pattern in mapping:
            word = mapping[pattern]
            if s[i:min(n_s, i + len(word))] != word:
                return False
            return self.backtrack(s, i + len(word), p, j + 1, mapping)
        else:
            for k in range(i+1, n_s+1):
                word = s[i:k]
                if word in mapping.values(): # easy to miss: bidirectional check
                    continue
                mapping[pattern] = word
                if self.backtrack(s, k, p, j+1, mapping):
                    return True
                del mapping[pattern]
        return False
        